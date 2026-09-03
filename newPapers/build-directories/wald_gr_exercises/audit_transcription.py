#!/usr/bin/env python3
"""Audit the Wald scaffold, file headers, and completion status."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

from scaffold_sections import ROOT, parse_plan


LATEX = ROOT / "latex"
CHAPTERS = LATEX / "chapters"
HEADER_FIELDS = (
    "Source",
    "Coverage",
    "Figures/tables/footnotes",
    "Status",
    "Uncertainties",
)
GLOBAL_CONTENT = (
    LATEX / "frontmatter" / "preface.tex",
    LATEX / "frontmatter" / "notation.tex",
    LATEX / "appendices" / "appendixA.tex",
    LATEX / "appendices" / "appendixB" / "secB1.tex",
    LATEX / "appendices" / "appendixB" / "secB2.tex",
    LATEX / "appendices" / "appendixB" / "secB3.tex",
    LATEX / "appendices" / "appendixC" / "secC1.tex",
    LATEX / "appendices" / "appendixC" / "secC2.tex",
    LATEX / "appendices" / "appendixC" / "secC3.tex",
    LATEX / "appendices" / "appendixD.tex",
    LATEX / "appendices" / "appendixE" / "secE1.tex",
    LATEX / "appendices" / "appendixE" / "secE2.tex",
    LATEX / "appendices" / "appendixF.tex",
    LATEX / "backmatter" / "references.tex",
    LATEX / "backmatter" / "index.tex",
)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--strict", action="store_true")
    args = parser.parse_args()

    chapter_titles, sections = parse_plan()
    structural: list[str] = []
    incomplete: list[str] = []
    content_files: list[Path] = list(GLOBAL_CONTENT)

    master = LATEX / "master.tex"
    if not master.exists():
        structural.append("Missing latex/master.tex.")

    for chapter in range(1, 15):
        chapter_dir = CHAPTERS / f"chapter{chapter:02d}"
        expected = [
            chapter_dir / "introduction.tex",
            *(chapter_dir / spec.filename for spec in sections[chapter]),
            chapter_dir / "problems.tex",
        ]
        content_files.extend(expected)
        wrapper = CHAPTERS / f"chapter{chapter:02d}.tex"
        if not wrapper.exists():
            structural.append(f"Missing {wrapper.relative_to(ROOT)}.")
        else:
            wrapper_text = wrapper.read_text(encoding="utf-8")
            if f"\\section{{{chapter_titles[chapter]}}}" not in wrapper_text:
                structural.append(
                    f"{wrapper.relative_to(ROOT)} has the wrong heading."
                )

    complete = 0
    for path in content_files:
        if not path.exists():
            structural.append(f"Missing planned file {path.relative_to(ROOT)}.")
            continue
        text = path.read_text(encoding="utf-8")
        header = "\n".join(text.splitlines()[:20])
        for field in HEADER_FIELDS:
            if not re.search(rf"^% {re.escape(field)}:", header, re.MULTILINE):
                structural.append(
                    f"{path.relative_to(ROOT)} lacks `% {field}:`."
                )
        status = re.search(r"^% Status:\s*(.+)$", header, re.MULTILINE)
        value = status.group(1).strip() if status else "missing"
        if "source-reviewed and compile-clean" in value:
            complete += 1
        else:
            incomplete.append(f"{path.relative_to(ROOT)}: {value}")

    print(f"Content files complete: {complete}/{len(content_files)}")
    if structural:
        print("STRUCTURAL ISSUES", file=sys.stderr)
        for finding in structural:
            print(f"  - {finding}", file=sys.stderr)
    if incomplete:
        print(f"Incomplete content files: {len(incomplete)}")
        if args.strict:
            for finding in incomplete:
                print(f"  - {finding}", file=sys.stderr)

    if structural or (args.strict and incomplete):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

