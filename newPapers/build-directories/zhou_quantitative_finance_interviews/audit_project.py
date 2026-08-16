#!/usr/bin/env python3
"""Audit the native Zhou JHEP transcription and its source-page coverage."""

from __future__ import annotations

import argparse
import re
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parent
LATEX = ROOT / "latex"
TRANSCRIPTION = LATEX / "transcription"

EXPECTED_CHUNKS = [
    "pp0005-0015.tex",
    "pp0017-0018.tex",
    "pp0019-0023.tex",
    "pp0024-0028.tex",
    "pp0029-0033.tex",
    "pp0034-0038.tex",
    "pp0039-0043.tex",
    "pp0044-0048.tex",
    "pp0049-0053.tex",
    "pp0054-0058.tex",
    "pp0059-0063.tex",
    "pp0064-0068.tex",
    "pp0069-0074.tex",
    "pp0075-0079.tex",
    "pp0080-0084.tex",
    "pp0085-0089.tex",
    "pp0090-0094.tex",
    "pp0095-0099.tex",
    "pp0100-0104.tex",
    "pp0105-0109.tex",
    "pp0110-0114.tex",
    "pp0115-0119.tex",
    "pp0121-0125.tex",
    "pp0126-0130.tex",
    "pp0131-0135.tex",
    "pp0136-0140.tex",
    "pp0141-0145.tex",
    "pp0146-0150.tex",
    "pp0151-0152.tex",
    "pp0153-0157.tex",
    "pp0158-0162.tex",
    "pp0163-0167.tex",
    "pp0168-0172.tex",
    "pp0173-0177.tex",
    "pp0178-0182.tex",
    "pp0183-0185.tex",
    "pp0187-0191.tex",
    "pp0192-0196.tex",
    "pp0197-0201.tex",
    "pp0202-0206.tex",
    "pp0207-0207.tex",
    "pp0209-0211.tex",
]

ASSEMBLY_FILES = [
    "frontmatter/frontmatter.tex",
    "chapters/chapter01.tex",
    "chapters/chapter02.tex",
    "chapters/chapter03.tex",
    "chapters/chapter04.tex",
    "chapters/chapter05.tex",
    "chapters/chapter06.tex",
    "chapters/chapter07.tex",
    "backmatter/index.tex",
]

INCLUDED = {5, 13, 14, 15}
INCLUDED.update(range(17, 120))
INCLUDED.update(range(121, 186))
INCLUDED.update(range(187, 208))
INCLUDED.update(range(209, 212))
REPLACED = {1, 3, 7, 8, 9, 10, 11}
OMITTED = {2, 4, 6, 12, 16, 120, 186, 208, 212}
FRONTMATTER_PAGES = {5, 13, 14, 15}

PAGE_MARKER = re.compile(
    r"^% ZHOU-SOURCE-PAGE: (?P<physical>\d+) PRINTED: "
    r"(?P<printed>FRONTMATTER|\d+)\s*$",
    re.MULTILINE,
)
INPUT = re.compile(r"\\input\{transcription/([^}]+)\}")
BEGIN = re.compile(r"\\begin\{([^}]+)\}")
END = re.compile(r"\\end\{([^}]+)\}")
UNNUMBERED_SOURCE_NOTE = re.compile(
    r"\\footnote\s*\{|"
    r"\\footnotemark(?!\s*\[)|"
    r"\\footnotetext(?!\s*\[)"
)


def fail(message: str) -> None:
    raise SystemExit(message)


def strip_comments(text: str) -> str:
    return "\n".join(
        re.split(r"(?<!\\)%", line, maxsplit=1)[0] for line in text.splitlines()
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--allow-queries",
        action="store_true",
        help="allow ZHOU-QUERY markers during active transcription",
    )
    args = parser.parse_args()

    expected_paths = {TRANSCRIPTION / name for name in EXPECTED_CHUNKS}
    actual_paths = set(TRANSCRIPTION.glob("*.tex"))
    missing = sorted(path.name for path in expected_paths - actual_paths)
    extra = sorted(path.name for path in actual_paths - expected_paths)
    if missing or extra:
        fail(f"Chunk set mismatch; missing={missing}, extra={extra}")

    assembly_inputs: list[str] = []
    for relative in ASSEMBLY_FILES:
        path = LATEX / relative
        if not path.is_file():
            fail(f"Missing assembly file: {relative}")
        assembly_inputs.extend(INPUT.findall(path.read_text(encoding="utf-8")))
    if assembly_inputs != EXPECTED_CHUNKS:
        fail(
            "Assembly order mismatch; "
            f"expected={EXPECTED_CHUNKS}, actual={assembly_inputs}"
        )

    master = (LATEX / "master.tex").read_text(encoding="utf-8")
    for relative in ASSEMBLY_FILES:
        if f"\\input{{{relative}}}" not in master:
            fail(f"master.tex omits {relative}")
    if "\\usepackage{quantguide}" not in master:
        fail("master.tex does not load quantguide")

    marker_records: list[tuple[int, str, str]] = []
    all_tex = [LATEX / "master.tex", LATEX / "quantguide.sty"]
    all_tex.extend(LATEX / relative for relative in ASSEMBLY_FILES)
    all_tex.extend(TRANSCRIPTION / name for name in EXPECTED_CHUNKS)

    forbidden = re.compile(
        r"\\(?:includepdf|facsimilepages|frontmatterpages)|"
        r"\\RequirePackage\{pdfpages\}|sourcepdf"
    )
    unresolved = re.compile(r"ZHOU-QUERY|\bTODO\b|\bTBD\b|\bFIXME\b")
    non_ascii: list[str] = []

    for path in all_tex:
        text = path.read_text(encoding="utf-8")
        match = forbidden.search(text)
        if match:
            fail(f"Forbidden facsimile command in {path}: {match.group(0)}")
        if not args.allow_queries:
            match = unresolved.search(text)
            if match:
                fail(f"Unresolved marker in {path}: {match.group(0)}")
        for line_number, line in enumerate(text.splitlines(), start=1):
            if any(ord(character) > 127 for character in line):
                non_ascii.append(f"{path}:{line_number}")

        if path.parent == TRANSCRIPTION:
            if path.stat().st_size < 80:
                fail(f"Suspiciously short transcription chunk: {path.name}")
            match = UNNUMBERED_SOURCE_NOTE.search(text)
            if match:
                fail(
                    f"Source footnote lacks an explicit source number in "
                    f"{path.name}: {match.group(0)}"
                )
            for match in PAGE_MARKER.finditer(text):
                marker_records.append(
                    (int(match.group("physical")), match.group("printed"), path.name)
                )
            visible = strip_comments(text)
            if Counter(BEGIN.findall(visible)) != Counter(END.findall(visible)):
                fail(f"Unbalanced LaTeX environments in {path.name}")

    if non_ascii:
        fail(f"Non-ASCII source remains in TeX: {non_ascii}")

    page_counts = Counter(physical for physical, _, _ in marker_records)
    duplicated = sorted(page for page, count in page_counts.items() if count != 1)
    seen_pages = set(page_counts)
    if seen_pages != INCLUDED or duplicated:
        fail(
            "Source marker coverage mismatch; "
            f"missing={sorted(INCLUDED - seen_pages)}, "
            f"extra={sorted(seen_pages - INCLUDED)}, duplicated={duplicated}"
        )

    for physical, printed, chunk in marker_records:
        expected_printed = "FRONTMATTER" if physical in FRONTMATTER_PAGES else str(physical - 16)
        if printed != expected_printed:
            fail(
                f"Printed folio mismatch in {chunk}: physical {physical} "
                f"has {printed}, expected {expected_printed}"
            )

    dispositions = INCLUDED | REPLACED | OMITTED
    if dispositions != set(range(1, 213)):
        fail("Disposition map does not cover physical pages 1-212")
    if (INCLUDED & REPLACED) or (INCLUDED & OMITTED) or (REPLACED & OMITTED):
        fail("Disposition sets overlap")

    required_sections = [
        "General Principles",
        "Brain Teasers",
        "Calculus and Linear Algebra",
        "Probability Theory",
        "Stochastic Process and Stochastic Calculus",
        "Finance",
        "Algorithms and Numerical Methods",
    ]
    combined = "\n".join(
        (TRANSCRIPTION / name).read_text(encoding="utf-8") for name in EXPECTED_CHUNKS
    )
    for heading in required_sections:
        if combined.count(f"\\section{{{heading}}}") != 1:
            fail(f"Required chapter section is missing or duplicated: {heading}")

    print(
        "Project audit passed: "
        f"{len(EXPECTED_CHUNKS)} native chunks, {len(INCLUDED)} source pages, "
        f"{len(REPLACED)} replaced pages, {len(OMITTED)} omitted leaves"
    )


if __name__ == "__main__":
    main()
