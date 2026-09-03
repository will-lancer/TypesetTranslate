#!/usr/bin/env python3
"""Create and verify the complete Banks source-page disposition ledger."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "page-dispositions.jsonl"

FRONT = {
    1: ("front-cover", "omit", "cover artwork"),
    2: ("intentional-blank", "omit", "publisher-marked blank page"),
    3: ("publisher-description", "omit", "publisher-only description"),
    4: ("blank-verso", "omit", "blank page"),
    5: ("title-page", "generated", "native title treatment"),
    6: ("copyright-imprint", "omit", "publisher-only legal and imprint data"),
    7: ("contents-1", "generated", "native table of contents"),
    8: ("contents-2", "generated", "native table of contents"),
    9: ("contents-3", "generated", "native table of contents"),
    10: ("blank-leaf", "omit", "blank page"),
}

BODY_RANGES = (
    (11, 17, "chapter01"),
    (18, 26, "chapter02"),
    (27, 47, "chapter03"),
    (48, 53, "chapter04"),
    (54, 71, "chapter05"),
    (72, 85, "chapter06"),
    (86, 102, "chapter07"),
    (103, 146, "chapter08"),
    (147, 215, "chapter09"),
    (216, 251, "chapter10"),
    (252, 254, "chapter11"),
    (255, 256, "appendixA"),
    (257, 257, "appendixB"),
    (258, 260, "appendixC"),
    (261, 265, "appendixD"),
    (266, 269, "appendixE"),
    (270, 271, "appendixF"),
    (272, 277, "references"),
    (278, 278, "author-index"),
    (279, 281, "subject-index"),
)


def body_unit(page: int) -> str:
    for start, end, unit in BODY_RANGES:
        if start <= page <= end:
            return unit
    raise ValueError(f"Unmapped body page {page}")


def records() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    roman = {7: "v", 8: "vi", 9: "vii"}
    for page in range(1, 282):
        if page in FRONT:
            unit, disposition, reason = FRONT[page]
            rows.append(
                {
                    "pdf_page": page,
                    "printed_page": roman.get(page, "unnumbered"),
                    "unit": unit,
                    "disposition": disposition,
                    "reason": reason,
                }
            )
            continue
        rows.append(
            {
                "pdf_page": page,
                "printed_page": page - 10,
                "unit": body_unit(page),
                "disposition": "native",
                "reason": "source content transcribed in reading order",
            }
        )
    return rows


def encoded() -> str:
    return "".join(json.dumps(row, sort_keys=True) + "\n" for row in records())


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--strict", action="store_true")
    args = parser.parse_args()

    expected = encoded()
    if args.write:
        OUTPUT.write_text(expected, encoding="utf-8")

    if not OUTPUT.exists():
        raise SystemExit(f"Missing disposition ledger: {OUTPUT}")
    if OUTPUT.read_text(encoding="utf-8") != expected:
        raise SystemExit("Page disposition ledger differs from the frozen map")

    rows = records()
    assert [row["pdf_page"] for row in rows] == list(range(1, 282))
    counts = {name: sum(row["disposition"] == name for row in rows) for name in ("native", "generated", "omit")}
    print(f"page dispositions pass: 281/281; {counts}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

