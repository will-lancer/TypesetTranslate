#!/usr/bin/env python3
"""Guard reviewed Wald corrections against regression."""

from __future__ import annotations

import re
import sys
from collections import defaultdict
from pathlib import Path

from scaffold_sections import ROOT


LATEX = ROOT / "latex"

FORBIDDEN = {
    r"serious error is they were": "uncorrected grammar in Section 2.1",
    r"\bLeibnitz\b": "nonstandard spelling of Leibniz",
    r"trace tree part": "uncorrected trace-free typo",
    r"\bspacial\b": "uncorrected spatial typo",
    r"For nonstatic configurations": "transcription differs from source",
    r"\bsatisying\b": "uncorrected satisfying typo",
    r"\bartifical\b": "uncorrected artificial typo",
    r"past direct timelike": "uncorrected past-directed wording",
    r"\bcontraints\b": "uncorrected constraints typo",
    r"Schwartz inequality": "incorrect name for Cauchy--Schwarz inequality",
    r"Boltzman's constant": "misspelling of Boltzmann",
    r"await to complete theory": "uncorrected grammar in Section 14.3",
    r"\bwih respect\b": "uncorrected with typo",
    r"\bUniverity Press\b": "uncorrected University typo",
    r"\bCentennary Survey\b": "uncorrected Centenary typo",
    r"Gauss-Codacci": "misspelling of Gauss--Codazzi",
}


def strip_comments(text: str) -> str:
    """Remove TeX comments while preserving escaped percent signs."""

    visible: list[str] = []
    for line in text.splitlines():
        cutoff = len(line)
        for position, character in enumerate(line):
            if character != "%":
                continue
            backslashes = 0
            cursor = position - 1
            while cursor >= 0 and line[cursor] == "\\":
                backslashes += 1
                cursor -= 1
            if backslashes % 2 == 0:
                cutoff = position
                break
        visible.append(line[:cutoff])
    return "\n".join(visible)


def main() -> int:
    findings: list[str] = []
    tags: dict[str, list[str]] = defaultdict(list)
    files = sorted(LATEX.rglob("*.tex"))

    for path in files:
        relative = path.relative_to(ROOT)
        text = strip_comments(path.read_text(encoding="utf-8"))
        for pattern, description in FORBIDDEN.items():
            if match := re.search(pattern, text):
                line = text.count("\n", 0, match.start()) + 1
                findings.append(f"{relative}:{line}: {description}")

        for match in re.finditer(
            r"\\tag\{([^}]+)\}\\label\{eq:([^}]+)\}", text
        ):
            tag, label = match.groups()
            line = text.count("\n", 0, match.start()) + 1
            location = f"{relative}:{line}"
            tags[tag].append(location)
            if tag != label:
                findings.append(
                    f"{location}: equation tag {tag!r} disagrees with label {label!r}"
                )

    for tag, locations in sorted(tags.items()):
        if len(locations) > 1:
            findings.append(
                f"duplicate displayed equation tag {tag}: {', '.join(locations)}"
            )

    sec72 = strip_comments(
        (LATEX / "chapters" / "chapter07" / "sec72.tex").read_text(
            encoding="utf-8"
        )
    )
    if not re.search(
        r"&=-\\left\(\\sum_\\beta f_\\beta\^\{-1\}k_\\beta\\right\)",
        sec72,
    ):
        findings.append("latex/chapters/chapter07/sec72.tex: equation (7.2.50) lacks its corrected minus sign")

    sec74 = strip_comments(
        (LATEX / "chapters" / "chapter07" / "sec74.tex").read_text(
            encoding="utf-8"
        )
    )
    if "7.2.12" in sec74:
        findings.append("latex/chapters/chapter07/sec74.tex: stale reference to (7.2.12)")
    if sec74.count(r"\eqref{eq:7.4.12}") < 4:
        findings.append("latex/chapters/chapter07/sec74.tex: corrected (7.4.12) references are incomplete")

    sec62 = strip_comments(
        (LATEX / "chapters" / "chapter06" / "sec62.tex").read_text(
            encoding="utf-8"
        )
    )
    if "For nonstationary configurations" not in sec62:
        findings.append("latex/chapters/chapter06/sec62.tex: source wording 'nonstationary' is missing")

    if findings:
        print("CORRECTION AUDIT FAILED", file=sys.stderr)
        for finding in findings:
            print(f"  - {finding}", file=sys.stderr)
        return 1

    print(
        f"Correction audit passed: {len(files)} TeX files, "
        f"{sum(len(locations) for locations in tags.values())} numbered equations, "
        "19 reviewed correction classes."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
