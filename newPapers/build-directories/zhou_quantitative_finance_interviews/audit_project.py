#!/usr/bin/env python3
"""Audit source-page dispositions and JHEP assembly structure."""

from __future__ import annotations

import re
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parent
LATEX = ROOT / "latex"

INCLUDED = set([5, 13, 14, 15])
INCLUDED.update(range(17, 120))
INCLUDED.update(range(121, 186))
INCLUDED.update(range(187, 208))
INCLUDED.update(range(209, 212))

REPLACED = {1, 3, 7, 8, 9, 10, 11}
OMITTED = {2, 4, 6, 12, 16, 120, 186, 208, 212}


def expand_pages(spec: str) -> set[int]:
    pages: set[int] = set()
    for token in spec.split(","):
        token = token.strip()
        if not token:
            continue
        if "-" in token:
            start, end = (int(value) for value in token.split("-", 1))
            pages.update(range(start, end + 1))
        else:
            pages.add(int(token))
    return pages


def main() -> None:
    master = (LATEX / "master.tex").read_text(encoding="utf-8")
    expected_inputs = [
        "frontmatter/frontmatter.tex",
        *(f"chapters/chapter{number:02d}.tex" for number in range(1, 8)),
        "backmatter/index.tex",
    ]
    missing_inputs = [path for path in expected_inputs if f"\\input{{{path}}}" not in master]
    if missing_inputs:
        raise SystemExit(f"Missing master inputs: {missing_inputs}")

    if "\\usepackage{quantguide}" not in master:
        raise SystemExit("master.tex does not load the project style")

    style = (LATEX / "quantguide.sty").read_text(encoding="utf-8")
    if "\\RequirePackage{jheppub}" not in style:
        raise SystemExit("quantguide.sty does not load jheppub")

    texmf_style = subprocess.run(
        ["kpsewhich", "jheppub.sty"],
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()
    if not texmf_style:
        raise SystemExit("jheppub.sty is missing from the TeX tree")

    seen: set[int] = set()
    source_files = [LATEX / path for path in expected_inputs]
    pattern = re.compile(r"\\(?:frontmatterpages|facsimilepages)(?:\[[\s\S]*?\])?\{([0-9,\- ]+)\}")
    for path in source_files:
        text = path.read_text(encoding="utf-8")
        for match in pattern.finditer(text):
            pages = expand_pages(match.group(1))
            overlap = seen.intersection(pages)
            if overlap:
                raise SystemExit(f"Duplicate included pages in {path}: {sorted(overlap)}")
            seen.update(pages)

    if seen != INCLUDED:
        missing = sorted(INCLUDED - seen)
        extra = sorted(seen - INCLUDED)
        raise SystemExit(f"Source coverage mismatch; missing={missing}, extra={extra}")

    all_pages = INCLUDED | REPLACED | OMITTED
    if all_pages != set(range(1, 213)):
        raise SystemExit("Disposition map does not cover physical pages 1-212")
    if (INCLUDED & REPLACED) or (INCLUDED & OMITTED) or (REPLACED & OMITTED):
        raise SystemExit("Disposition sets overlap")

    print(
        "Project audit passed: "
        f"{len(INCLUDED)} included source pages, "
        f"{len(REPLACED)} replaced pages, {len(OMITTED)} omitted leaves; "
        f"JHEP style at {texmf_style}"
    )


if __name__ == "__main__":
    main()

