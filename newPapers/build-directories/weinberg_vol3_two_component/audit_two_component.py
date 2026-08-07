#!/usr/bin/env python3
"""Source-level audit for the parallel two-component Weinberg edition."""

from __future__ import annotations

import argparse
import re
import sys
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parent
BASELINE = ROOT.parent / "weinberg_vol3" / "latex"
EDITION = ROOT / "latex"

LABEL_RE = re.compile(r"\\label\{([^}]+)\}")
TAG_RE = re.compile(r"\\tag\{([^}]+)\}")
STRUCTURE_PATTERNS = {
    "numbered equations": re.compile(r"\\begin\{equation\}"),
    "unnumbered displays": re.compile(r"\\\["),
    "footnotes": re.compile(r"\\footnote\{"),
    "hyperrefs": re.compile(r"\\hyperref\["),
    "section headings": re.compile(r"\\(?:sub)*section\*?\{"),
}
TARGET_PATTERNS = {
    "equation references": re.compile(r"\\eqref\{([^}]+)\}"),
    "plain references": re.compile(r"(?<!eq)\\ref\{([^}]+)\}"),
    "hyperlink targets": re.compile(r"\\hyperref\[([^\]]+)\]"),
}

# The corrected comparison source now carries the shared reference errata, so
# the two-component edition preserves its reference inventory without deltas.
TARGET_ADJUSTMENTS: dict[int, dict[str, dict[str, int]]] = {}

FORBIDDEN = {
    "gamma5": re.compile(r"\\gamma_?5(?![0-9])"),
    "gamma-matrix": re.compile(
        r"(?<!_)\\gamma(?:\^|_)\{?"
        r"(?:\\(?:mu|nu|rho|sigma|lambda|kappa|tau)|"
        r"[0-46-9]|i(?!j)|j(?!i))"
    ),
    "chiral-projector": re.compile(r"\bP_[LR]\b"),
    "projected-superderivative": re.compile(
        r"\\(?:mathcal\{D\}|SuperD)_[LR]\b"
    ),
    "projected-field-strength": re.compile(
        r"\\(?:bar\s*)?W_\{[^}\n]*[LR][^}\n]*\}"
    ),
    "majorana-helper": re.compile(r"\\MajoranaQ\b"),
    "dirac-slash": re.compile(r"\\(?:sl|slashed)\{"),
}

REVIEW = {
    "four-component-prose": re.compile(
        r"four[- ]component|Dirac (?:spinor|notation|formalism)|"
        r"Majorana (?:spinor|four-spinor|notation)"
    ),
    "dirac-adjoint-candidate": re.compile(r"\\bar\{?[A-Za-z\\]+"),
}

SUSPECTS = {**FORBIDDEN, **REVIEW}

REQUIRED_ASYMPTOTIC_HELPERS = (
    r"\newcommand{\InKet}[1]{\ket{#1}_{\mathrm{in}}}",
    r"\newcommand{\OutKet}[1]{\ket{#1}_{\mathrm{out}}}",
    r"\newcommand{\InBra}[1]{{}_{\mathrm{in}}\!\bra{#1}}",
    r"\newcommand{\OutBra}[1]{{}_{\mathrm{out}}\!\bra{#1}}",
)
RAW_EXTERNAL_ASYMPTOTIC_RE = re.compile(
    r"(?:"
    r"\{\}_\{?\\mathrm\{(?:in|out)\}\}?\s*\\!\s*\\bra"
    r"|\\ket\{[^{}\n]*\}\s*_\{?\\mathrm\{(?:in|out)\}\}?"
    r")",
    re.IGNORECASE,
)
LEGACY_CH24_INTERNAL_INDEX_RE = re.compile(
    r"\\(?:alpha|beta|gamma|delta)(?![A-Za-z])"
)
LEGACY_CH24_APPENDIX_INDEX_RE = re.compile(
    r"\\(?:alpha|beta|gamma)(?![A-Za-z])"
)


def tex_files(root: Path, chapter: int | None = None) -> list[Path]:
    if chapter is None:
        return sorted(root.rglob("*.tex"))
    chapter_root = root / "chapters" / f"chapter{chapter}"
    wrapper = root / "chapters" / f"chapter{chapter}.tex"
    files = sorted(chapter_root.rglob("*.tex"))
    if wrapper.exists():
        files.insert(0, wrapper)
    return files


def collect(pattern: re.Pattern[str], files: list[Path]) -> Counter[str]:
    values: Counter[str] = Counter()
    for path in files:
        values.update(pattern.findall(path.read_text(encoding="utf-8")))
    return values


def count_matches(pattern: re.Pattern[str], files: list[Path]) -> int:
    return sum(
        len(pattern.findall(path.read_text(encoding="utf-8")))
        for path in files
    )


def adjusted_baseline_targets(
    chapter: int,
    name: str,
    targets: Counter[str],
) -> Counter[str]:
    adjusted = targets.copy()
    for target, delta in TARGET_ADJUSTMENTS.get(chapter, {}).get(
        name, {}
    ).items():
        adjusted[target] += delta
        if adjusted[target] < 0:
            raise AssertionError(
                f"invalid target adjustment for Chapter {chapter}: {target}"
            )
        if adjusted[target] == 0:
            del adjusted[target]
    return adjusted


def compare_inventory() -> bool:
    ok = True
    for chapter in range(24, 33):
        old_files = tex_files(BASELINE, chapter)
        new_files = tex_files(EDITION, chapter)
        old_labels = collect(LABEL_RE, old_files)
        new_labels = collect(LABEL_RE, new_files)
        old_tags = collect(TAG_RE, old_files)
        new_tags = collect(TAG_RE, new_files)
        structural_changes = {
            name: (
                count_matches(pattern, old_files),
                count_matches(pattern, new_files),
            )
            for name, pattern in STRUCTURE_PATTERNS.items()
        }
        structural_changes = {
            name: counts
            for name, counts in structural_changes.items()
            if counts[0] != counts[1]
        }
        target_changes = {}
        for name, pattern in TARGET_PATTERNS.items():
            old_targets = adjusted_baseline_targets(
                chapter,
                name,
                collect(pattern, old_files),
            )
            new_targets = collect(pattern, new_files)
            if old_targets != new_targets:
                target_changes[name] = (old_targets, new_targets)

        missing_labels = old_labels - new_labels
        extra_labels = new_labels - old_labels
        missing_tags = old_tags - new_tags
        extra_tags = new_tags - old_tags
        if (
            missing_labels
            or extra_labels
            or missing_tags
            or extra_tags
            or structural_changes
            or target_changes
        ):
            ok = False
            print(f"CHAPTER {chapter}: inventory mismatch")
            if missing_labels:
                print("  missing labels:", sorted(missing_labels.elements()))
            if extra_labels:
                print("  extra labels:", sorted(extra_labels.elements()))
            if missing_tags:
                print("  missing tags:", sorted(missing_tags.elements()))
            if extra_tags:
                print("  extra tags:", sorted(extra_tags.elements()))
            for name, (old_count, new_count) in structural_changes.items():
                print(f"  {name}: {old_count} -> {new_count}")
            for name, (old_targets, new_targets) in target_changes.items():
                missing = old_targets - new_targets
                extra = new_targets - old_targets
                if missing:
                    print(f"  missing {name}:", sorted(missing.elements()))
                if extra:
                    print(f"  extra {name}:", sorted(extra.elements()))
        else:
            print(
                f"CHAPTER {chapter}: labels={sum(new_labels.values())} "
                f"tags={sum(new_tags.values())} OK"
            )
    return ok


def report_suspects() -> tuple[int, int]:
    total = 0
    forbidden_total = 0
    print("\nFOUR-DIMENSIONAL SPINOR SUSPECTS (Chapters 24-31)")
    for chapter in range(24, 32):
        counts: Counter[str] = Counter()
        samples: dict[str, list[str]] = {name: [] for name in SUSPECTS}
        for path in tex_files(EDITION, chapter):
            relative = path.relative_to(EDITION)
            for line_number, line in enumerate(
                path.read_text(encoding="utf-8").splitlines(), start=1
            ):
                if "2C-EXCEPTION" in line:
                    continue
                for name, pattern in SUSPECTS.items():
                    if pattern.search(line):
                        counts[name] += 1
                        if name in FORBIDDEN:
                            forbidden_total += 1
                        if len(samples[name]) < 3:
                            samples[name].append(
                                f"{relative}:{line_number}: {line.strip()}"
                            )
        chapter_total = sum(counts.values())
        total += chapter_total
        print(f"CHAPTER {chapter}: {dict(counts)}")
        for name, lines in samples.items():
            if lines:
                print(f"  {name}:")
                for line in lines:
                    print(f"    {line}")
    print(f"TOTAL SUSPECT LINES: {total}")
    print(f"TOTAL UNMARKED FORBIDDEN LINES: {forbidden_total}")
    return total, forbidden_total


def audit_shared_notation() -> bool:
    """Check notation rules shared with the canonical Volume III edition."""

    ok = True
    master = (EDITION / "master.tex").read_text(encoding="utf-8")
    for helper in REQUIRED_ASYMPTOTIC_HELPERS:
        if master.count(helper) != 1:
            ok = False
            print(f"NOTATION: master.tex must define exactly once: {helper}")

    chapter24_checks = (
        (
            EDITION / "chapters/chapter24/sec241.tex",
            LEGACY_CH24_INTERNAL_INDEX_RE,
        ),
        (
            EDITION / "chapters/chapter24/appendixB.tex",
            LEGACY_CH24_APPENDIX_INDEX_RE,
        ),
    )
    for path, pattern in chapter24_checks:
        match = pattern.search(path.read_text(encoding="utf-8"))
        if match:
            ok = False
            print(
                "NOTATION: legacy Greek internal Lie-algebra index in "
                f"{path.relative_to(EDITION)}: {match.group(0)!r}"
            )

    for path in EDITION.rglob("*.tex"):
        if path == EDITION / "master.tex":
            continue
        match = RAW_EXTERNAL_ASYMPTOTIC_RE.search(
            path.read_text(encoding="utf-8")
        )
        if match:
            ok = False
            print(
                "NOTATION: manual asymptotic-state spelling in "
                f"{path.relative_to(EDITION)}: {match.group(0)!r}"
            )
    if ok:
        print("SHARED NOTATION: OK")
    return ok


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--strict",
        action="store_true",
        help="fail on any unmarked forbidden four-component construct",
    )
    args = parser.parse_args()
    inventory_ok = compare_inventory()
    _, forbidden_total = report_suspects()
    notation_ok = audit_shared_notation()
    strict_ok = not args.strict or forbidden_total == 0
    return 0 if inventory_ok and notation_ok and strict_ok else 1


if __name__ == "__main__":
    sys.exit(main())
