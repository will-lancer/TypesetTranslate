#!/usr/bin/env python3
"""Audit GR source structure, handoff metadata, tags, and references."""

from __future__ import annotations

import argparse
import re
import sys
from collections import Counter
from pathlib import Path

from scaffold_sections import ROOT, parse_plan


LATEX = ROOT / "latex"
CHAPTERS = LATEX / "chapters"
MASTER = LATEX / "master.tex"
GLOBAL_GROUPS = (
    (
        "FRONT MATTER",
        (
            LATEX / "frontmatter" / "publication.tex",
            LATEX / "frontmatter" / "preface.tex",
            LATEX / "frontmatter" / "notation.tex",
            LATEX / "frontmatter" / "copyright-acknowledgements.tex",
        ),
    ),
    (
        "BACK MATTER",
        (
            LATEX / "backmatter" / "appendix.tex",
            LATEX / "backmatter" / "index.tex",
        ),
    ),
)
HEADER_FIELDS = (
    "Source",
    "Coverage",
    "Figures/tables/footnotes",
    "Status",
    "Uncertainties",
)
LABEL_RE = re.compile(r"\\label\{([^}]+)\}")
TAG_RE = re.compile(r"\\tag\{([^}]+)\}")
TAG_LABEL_RE = re.compile(
    r"\\tag\{([^}]+)\}\s*\\label\{eq:([^}]+)\}",
    re.DOTALL,
)
TARGET_RES = (
    re.compile(r"\\(?:eqref|ref|pageref|autoref)\{([^}]+)\}"),
    re.compile(r"\\hyperref\[([^\]]+)\]"),
)
SUPPLEMENT_REQUIREMENTS = {
    LATEX / "frontmatter" / "notation.tex": ("contents-pxxii.png",),
    CHAPTERS / "chapter11" / "sec112.tex": ("printed-p306.png",),
    CHAPTERS / "chapter13" / "sec133.tex": (
        "printed-p390.png",
        "printed-p392.png",
    ),
    CHAPTERS / "chapter13" / "sec134.tex": ("printed-p392.png",),
    CHAPTERS / "chapter14" / "sec143.tex": ("printed-p418.png",),
    CHAPTERS / "chapter14" / "sec144.tex": ("printed-p418.png",),
    CHAPTERS / "chapter14" / "sec145.tex": ("printed-p440.png",),
    CHAPTERS / "chapter15" / "sec1511.tex": ("printed-p594.png",),
    CHAPTERS / "chapter15" / "backmatter.tex": ("printed-p602.png",),
}


def issue(message: str, collection: list[str]) -> None:
    collection.append(message)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--strict",
        action="store_true",
        help="also fail on incomplete files, placeholders, and forward refs",
    )
    args = parser.parse_args()

    chapter_titles, plan = parse_plan()
    hard_issues: list[str] = []
    incomplete: list[str] = []
    completed_files = 0
    planned_files = 0

    expected_master_inputs = [
        "frontmatter/publication.tex",
        "frontmatter/preface.tex",
        "frontmatter/notation.tex",
        "frontmatter/copyright-acknowledgements.tex",
        *(f"chapters/chapter{chapter:02d}.tex" for chapter in range(1, 17)),
        "backmatter/appendix.tex",
        "backmatter/index.tex",
    ]
    expected_parts = [
        "Preliminaries",
        "The General Theory of Relativity",
        "Applications of General Relativity",
        "Formal Developments",
        "Cosmology",
    ]
    if not MASTER.exists():
        issue("Missing latex/master.tex.", hard_issues)
    else:
        master_text = MASTER.read_text(encoding="utf-8")
        actual_master_inputs = re.findall(r"\\input\{([^}]+)\}", master_text)
        if actual_master_inputs != expected_master_inputs:
            issue(
                "latex/master.tex inputs do not match the complete book order.",
                hard_issues,
            )
        actual_parts = re.findall(r"\\bookpart\{([^}]+)\}", master_text)
        if actual_parts != expected_parts:
            issue(
                "latex/master.tex part headings do not match the source order.",
                hard_issues,
            )

    for group_name, paths in GLOBAL_GROUPS:
        planned_files += len(paths)
        group_complete = 0
        for path in paths:
            if not path.exists():
                issue(
                    f"{group_name}: missing planned file "
                    f"{path.relative_to(ROOT)}.",
                    incomplete,
                )
                continue

            text = path.read_text(encoding="utf-8")
            header = "\n".join(text.splitlines()[:20])
            for field in HEADER_FIELDS:
                if not re.search(rf"^% {re.escape(field)}:", header, re.MULTILINE):
                    issue(
                        f"{path.relative_to(ROOT)}: missing `% {field}:` header.",
                        hard_issues,
                    )

            status_match = re.search(
                r"^% Status:\s*(.+)$", header, re.MULTILINE
            )
            status = status_match.group(1).strip() if status_match else ""
            if "source-reviewed and compile-clean" in status:
                completed_files += 1
                group_complete += 1
            else:
                issue(
                    f"{path.relative_to(ROOT)}: incomplete status `{status}`.",
                    incomplete,
                )

            has_verify = "VERIFY" in text or "MODERNIZATION CHECK" in text
            uncertainty_none = re.search(
                r"^% Uncertainties:\s*none\.", header, re.MULTILINE
            )
            if has_verify and uncertainty_none:
                issue(
                    f"{path.relative_to(ROOT)}: VERIFY/MODERNIZATION marker "
                    "is not reported in the Uncertainties header.",
                    hard_issues,
                )

        print(
            f"{group_name}: {group_complete}/{len(paths)} content files complete"
        )

    for chapter in range(1, 17):
        chapter_dir = CHAPTERS / f"chapter{chapter:02d}"
        expected_names = [
            "introduction.tex",
            *(spec.filename for spec in plan[chapter]),
            "backmatter.tex",
        ]
        planned_files += len(expected_names)
        missing = [
            name for name in expected_names if not (chapter_dir / name).exists()
        ]
        if missing:
            issue(
                f"Chapter {chapter}: missing {len(missing)} planned files: "
                + ", ".join(missing),
                incomplete,
            )

        assembly = CHAPTERS / f"chapter{chapter:02d}.tex"
        if not assembly.exists():
            issue(f"Chapter {chapter}: missing assembly file.", hard_issues)
        else:
            text = assembly.read_text(encoding="utf-8")
            actual_inputs = re.findall(
                rf"\\input\{{chapters/chapter{chapter:02d}/([^}}]+)\}}",
                text,
            )
            if actual_inputs != expected_names:
                issue(
                    f"Chapter {chapter}: assembly inputs do not match "
                    "SECTION_PLAN.md order.",
                    hard_issues if not missing else incomplete,
                )
            expected_heading = rf"\section{{{chapter_titles[chapter]}}}"
            if expected_heading not in text:
                issue(
                    f"Chapter {chapter}: assembly heading differs from plan.",
                    hard_issues,
                )

        chapter_complete = 0
        for name in expected_names:
            path = chapter_dir / name
            if not path.exists():
                continue
            text = path.read_text(encoding="utf-8")
            header = "\n".join(text.splitlines()[:20])
            for field in HEADER_FIELDS:
                if not re.search(rf"^% {re.escape(field)}:", header, re.MULTILINE):
                    issue(
                        f"{path.relative_to(ROOT)}: missing `% {field}:` header.",
                        hard_issues,
                    )

            status_match = re.search(
                r"^% Status:\s*(.+)$", header, re.MULTILINE
            )
            status = status_match.group(1).strip() if status_match else ""
            if "source-reviewed and compile-clean" in status:
                completed_files += 1
                chapter_complete += 1
            else:
                issue(
                    f"{path.relative_to(ROOT)}: incomplete status `{status}`.",
                    incomplete,
                )

            has_verify = "VERIFY" in text or "MODERNIZATION CHECK" in text
            uncertainty_none = re.search(
                r"^% Uncertainties:\s*none\.", header, re.MULTILINE
            )
            if has_verify and uncertainty_none:
                issue(
                    f"{path.relative_to(ROOT)}: VERIFY/MODERNIZATION marker "
                    "is not reported in the Uncertainties header.",
                    hard_issues,
                )

        print(
            f"CHAPTER {chapter:02d}: "
            f"{chapter_complete}/{len(expected_names)} content files complete"
        )

        for spec in plan[chapter]:
            path = chapter_dir / spec.filename
            if not path.exists():
                continue
            text = path.read_text(encoding="utf-8")
            if rf"\label{{sec:{spec.number}}}" not in text:
                issue(
                    f"{path.relative_to(ROOT)}: missing section label "
                    f"`sec:{spec.number}`.",
                    hard_issues,
                )

    tex_files = sorted(LATEX.rglob("*.tex"))
    labels: Counter[str] = Counter()
    tags: Counter[str] = Counter()
    paired_tags: Counter[str] = Counter()
    targets: Counter[str] = Counter()
    todo_locations: list[str] = []
    verify_locations: list[str] = []

    for path in tex_files:
        text = path.read_text(encoding="utf-8")
        labels.update(LABEL_RE.findall(text))
        tags.update(TAG_RE.findall(text))
        for tag, label in TAG_LABEL_RE.findall(text):
            if tag != label:
                issue(
                    f"{path.relative_to(ROOT)}: equation tag `{tag}` is paired "
                    f"with label `eq:{label}`.",
                    hard_issues,
                )
            paired_tags[tag] += 1
        for pattern in TARGET_RES:
            targets.update(pattern.findall(text))
        for line_number, line in enumerate(text.splitlines(), start=1):
            if "TODO" in line or "not started" in line or "pending source" in line:
                todo_locations.append(
                    f"{path.relative_to(ROOT)}:{line_number}: {line.strip()}"
                )
            if "VERIFY" in line or "MODERNIZATION CHECK" in line:
                verify_locations.append(
                    f"{path.relative_to(ROOT)}:{line_number}: {line.strip()}"
                )

    duplicate_labels = sorted(label for label, count in labels.items() if count > 1)
    duplicate_tags = sorted(tag for tag, count in tags.items() if count > 1)
    if duplicate_labels:
        issue("Duplicate labels: " + ", ".join(duplicate_labels), hard_issues)
    if duplicate_tags:
        issue("Duplicate equation tags: " + ", ".join(duplicate_tags), hard_issues)

    unpaired_tags = tags - paired_tags
    unpaired_eq_labels = Counter(
        {
            label.removeprefix("eq:"): count
            for label, count in labels.items()
            if label.startswith("eq:")
        }
    ) - paired_tags
    if unpaired_tags:
        issue(
            "Equation tags without matching `eq:` labels: "
            + ", ".join(sorted(unpaired_tags.elements())),
            hard_issues,
        )
    if unpaired_eq_labels:
        issue(
            "`eq:` labels without matching equation tags: "
            + ", ".join(sorted(unpaired_eq_labels.elements())),
            hard_issues,
        )

    missing_targets = sorted(set(targets) - set(labels))
    if missing_targets:
        issue(
            "Reference targets not yet defined: " + ", ".join(missing_targets),
            incomplete,
        )
    if todo_locations:
        issue(
            f"{len(todo_locations)} TODO/not-started markers remain.",
            incomplete,
        )

    for path, required_markers in SUPPLEMENT_REQUIREMENTS.items():
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        header = "\n".join(text.splitlines()[:20])
        status_match = re.search(r"^% Status:\s*(.+)$", header, re.MULTILINE)
        status = status_match.group(1).strip() if status_match else ""
        if "source-reviewed and compile-clean" not in status:
            continue
        for marker in required_markers:
            if marker not in header:
                issue(
                    f"{path.relative_to(ROOT)}: completed source header does "
                    f"not cite supplemental source `{marker}`.",
                    hard_issues,
                )

    print(
        "\nSOURCE INVENTORY: "
        f"{completed_files}/{planned_files} planned content files complete; "
        f"{sum(tags.values())} equation tags; {sum(labels.values())} labels."
    )
    if verify_locations:
        print(f"REPORTED SOURCE/MODERNIZATION NOTES: {len(verify_locations)}")
        for location in verify_locations:
            print(f"  {location}")

    if hard_issues:
        print("\nSTRUCTURAL FAILURES", file=sys.stderr)
        for message in hard_issues[:30]:
            print(f"  - {message}", file=sys.stderr)
        if len(hard_issues) > 30:
            print(
                f"  - ... and {len(hard_issues) - 30} more.",
                file=sys.stderr,
            )
    if incomplete:
        heading = "STRICT COMPLETION FAILURES" if args.strict else "INCOMPLETE (allowed in draft mode)"
        print(f"\n{heading}", file=sys.stderr)
        for message in incomplete[:20]:
            print(f"  - {message}", file=sys.stderr)
        if len(incomplete) > 20:
            print(
                f"  - ... and {len(incomplete) - 20} more.",
                file=sys.stderr,
            )

    if hard_issues or (args.strict and incomplete):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
