#!/usr/bin/env python3
"""Audit the source structure and common OCR failure modes in the combined index."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent
INDEX = ROOT / "latex" / "backmatter" / "index.tex"
EXPECTED_MAIN_ENTRIES = 1207
EXPECTED_SUBENTRIES = 269
EXPECTED_OBJECTS = list(range(668, 685))
EXPECTED_PRINTED_PAGES = list(range(641, 658))
# The source visibly prints an italic 653 in the M. E. Ash entry on printed
# p. 642, even though the book's non-index content ends on printed p. 639.
SOURCE_HIGH_LOCATOR_EXCEPTIONS = {653}


def line_number(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--force",
        action="store_true",
        help="run structural checks before the index header is marked complete",
    )
    args = parser.parse_args()

    if not INDEX.exists():
        print(f"Missing combined index: {INDEX}", file=sys.stderr)
        return 1

    text = INDEX.read_text(encoding="utf-8")
    header = "\n".join(text.splitlines()[:20]).lower()
    if (
        "% status: source-reviewed and compile-clean." not in header
        and not args.force
    ):
        print("Index audit: pending source review; structural strict checks deferred.")
        return 0

    failures: list[str] = []

    main_entries = len(re.findall(r"\\idxentry\{", text))
    subentries = len(re.findall(r"\\idxsubentry\{", text))
    if main_entries != EXPECTED_MAIN_ENTRIES:
        failures.append(
            f"expected {EXPECTED_MAIN_ENTRIES} main entries, found {main_entries}"
        )
    if subentries != EXPECTED_SUBENTRIES:
        failures.append(
            f"expected {EXPECTED_SUBENTRIES} subentries, found {subentries}"
        )

    markers = re.findall(
        r"% Source IA object (\d+); printed p\. (\d+)\.", text
    )
    objects = [int(obj) for obj, _ in markers]
    printed_pages = [int(page) for _, page in markers]
    if objects != EXPECTED_OBJECTS or printed_pages != EXPECTED_PRINTED_PAGES:
        failures.append(
            "source markers must cover IA objects 668--684 and printed "
            "pp. 641--657 exactly once, in order"
        )

    entries = re.findall(r"\\idxentry\{([^\n]*)\}", text)
    if not entries or not entries[0].startswith("Abell, G. O.,"):
        failures.append("first main entry is not Abell, G. O.")
    if not entries or not entries[-1].startswith("Zwicky, F.,"):
        failures.append("last main entry is not Zwicky, F.")

    for match in re.finditer(r"\\idxbib\{([^{}]*)\}", text):
        contents = match.group(1)
        number = line_number(text, match.start())
        if not contents.strip():
            failures.append(f"line {number}: empty \\idxbib span")
            continue
        if re.search(r"[A-Za-z]", contents):
            failures.append(
                f"line {number}: publication-locator italics contain letters: "
                f"{contents!r}"
            )
        if re.search(r"\d\s+\d", contents):
            failures.append(
                f"line {number}: split digits in italic locator: {contents!r}"
            )
        for locator in re.findall(r"\d+", contents):
            value = int(locator)
            if value > 639 and value not in SOURCE_HIGH_LOCATOR_EXCEPTIONS:
                failures.append(
                    f"line {number}: italic locator exceeds final content "
                    f"page 639 without a pinned source exception: {locator}"
                )

    checks = (
        (
            re.compile(r"\d\s+\d"),
            "split page-number digits",
        ),
        (
            re.compile(r"(?<!-)\d-(?!-)\d"),
            "single TeX hyphen in numeric range; use --",
        ),
        (
            re.compile(r"\d[—–]\d"),
            "Unicode dash in numeric range; use LaTeX --",
        ),
        (
            re.compile(r",,"),
            "doubled comma",
        ),
        (
            re.compile(r"\uFFFD"),
            "Unicode replacement character",
        ),
    )
    for pattern, explanation in checks:
        for match in pattern.finditer(text):
            failures.append(
                f"line {line_number(text, match.start())}: {explanation}: "
                f"{match.group(0)!r}"
            )

    if failures:
        print("COMBINED INDEX FAILURES", file=sys.stderr)
        for failure in failures:
            print(f"  - {failure}", file=sys.stderr)
        return 1

    print(
        "Index audit: "
        f"{main_entries} main entries, {subentries} subentries, "
        "17 source-page markers; no common OCR-structure failures."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
