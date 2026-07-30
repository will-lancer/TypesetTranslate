#!/usr/bin/env python3
"""Generate a scan-aware source manifest and transcription status report."""

from __future__ import annotations

import argparse
import csv
import io
import re
import sys
from pathlib import Path

from scaffold_sections import ROOT, parse_plan


CHAPTERS = ROOT / "latex" / "chapters"
MANIFEST = ROOT / "SOURCE_MANIFEST.tsv"
STATUS = ROOT / "TRANSCRIPTION_STATUS.md"
GLOBAL_UNITS = (
    (
        "frontmatter",
        "Front matter",
        "publication",
        "Title, publication data, and dedication",
        ROOT / "latex" / "frontmatter" / "publication.tex",
    ),
    (
        "frontmatter",
        "Front matter",
        "preface",
        "Preface",
        ROOT / "latex" / "frontmatter" / "preface.tex",
    ),
    (
        "frontmatter",
        "Front matter",
        "notation-and-contents",
        "Notation and contents",
        ROOT / "latex" / "frontmatter" / "notation.tex",
    ),
    (
        "frontmatter",
        "Front matter",
        "copyright-acknowledgements",
        "Copyright acknowledgements and Part One divider",
        ROOT / "latex" / "frontmatter" / "copyright-acknowledgements.tex",
    ),
    (
        "backmatter",
        "Back matter",
        "appendix",
        "Appendix: Some Useful Numbers",
        ROOT / "latex" / "backmatter" / "appendix.tex",
    ),
    (
        "backmatter",
        "Back matter",
        "index",
        "Index",
        ROOT / "latex" / "backmatter" / "index.tex",
    ),
)
FIELD_RE = re.compile(
    r"^% (Source|Coverage|Figures/tables/footnotes|Status|Uncertainties):"
    r"\s*(.*)$"
)


def header_fields(path: Path) -> dict[str, str]:
    fields: dict[str, str] = {}
    current: str | None = None
    for line in path.read_text(encoding="utf-8").splitlines()[:24]:
        match = FIELD_RE.match(line)
        if match:
            current = match.group(1)
            fields[current] = match.group(2).strip()
            continue
        if current and line.startswith("%") and line.strip() != "%":
            continuation = line[1:].strip()
            if continuation and not continuation.startswith("TODO"):
                fields[current] = f"{fields[current]} {continuation}".strip()
            continue
        if not line.strip() or not line.startswith("%"):
            current = None
    return fields


def source_ranges(source: str) -> tuple[str, str]:
    physical_match = re.search(
        r"physical PDF (?:p|pp)\.\s*"
        r"(.+?)(?=\s*\(printed|\s*$)",
        source,
    )
    printed_match = re.search(r"\(printed\s+(.+?)\)", source)
    physical = physical_match.group(1).strip() if physical_match else "UNKNOWN"
    printed = printed_match.group(1).strip() if printed_match else "UNKNOWN"
    return physical, printed


def rows() -> list[dict[str, str]]:
    chapter_titles, plan = parse_plan()
    result: list[dict[str, str]] = []

    def append_row(
        chapter: str,
        chapter_title: str,
        unit: str,
        title: str,
        path: Path,
    ) -> None:
        fields = header_fields(path) if path.exists() else {}
        physical, printed = source_ranges(fields.get("Source", ""))
        result.append(
            {
                "chapter": chapter,
                "chapter_title": chapter_title,
                "unit": unit,
                "title": title,
                "path": str(path.relative_to(ROOT)),
                "physical_pdf_pages": physical,
                "printed_pages": printed,
                "coverage": fields.get("Coverage", "MISSING"),
                "figures_tables_footnotes": fields.get(
                    "Figures/tables/footnotes", "MISSING"
                ),
                "status": fields.get("Status", "MISSING"),
                "uncertainties": fields.get("Uncertainties", "MISSING"),
            }
        )

    for chapter, chapter_title, unit, title, path in GLOBAL_UNITS[:4]:
        append_row(chapter, chapter_title, unit, title, path)

    for chapter in range(1, 17):
        units = [
            ("opening", "introduction.tex", f"Chapter {chapter} opening"),
            *[
                (spec.number, spec.filename, spec.title)
                for spec in plan[chapter]
            ],
            ("backmatter", "backmatter.tex", f"Chapter {chapter} back matter"),
        ]
        for unit, filename, title in units:
            path = CHAPTERS / f"chapter{chapter:02d}" / filename
            append_row(
                str(chapter),
                chapter_titles[chapter],
                unit,
                title,
                path,
            )

    for chapter, chapter_title, unit, title, path in GLOBAL_UNITS[4:]:
        append_row(chapter, chapter_title, unit, title, path)

    return result


def render_manifest(data: list[dict[str, str]]) -> str:
    output = io.StringIO()
    writer = csv.DictWriter(
        output,
        fieldnames=list(data[0]),
        delimiter="\t",
        lineterminator="\n",
    )
    writer.writeheader()
    writer.writerows(data)
    return output.getvalue()


def render_status(data: list[dict[str, str]]) -> str:
    chapter_titles, _ = parse_plan()
    lines = [
        "# Transcription status",
        "",
        "Generated from the required `% Status:` headers by "
        "`source_manifest.py`; do not edit this table by hand.",
        "",
        "| Chapter | Title | Complete files | Total files | Status |",
        "|---:|---|---:|---:|---|",
    ]
    total_complete = 0
    front_rows = [row for row in data if row["chapter"] == "frontmatter"]
    front_complete = sum(
        "source-reviewed and compile-clean" in row["status"]
        for row in front_rows
    )
    total_complete += front_complete
    lines.append(
        f"| — | Front matter | {front_complete} | {len(front_rows)} | "
        f"{'complete' if front_complete == len(front_rows) else 'in progress'} |"
    )

    for chapter in range(1, 17):
        chapter_rows = [
            row for row in data if row["chapter"] == str(chapter)
        ]
        complete = sum(
            "source-reviewed and compile-clean" in row["status"]
            for row in chapter_rows
        )
        total_complete += complete
        state = "complete" if complete == len(chapter_rows) else "in progress"
        lines.append(
            f"| {chapter} | {chapter_titles[chapter]} | {complete} | "
            f"{len(chapter_rows)} | {state} |"
        )

    back_rows = [row for row in data if row["chapter"] == "backmatter"]
    back_complete = sum(
        "source-reviewed and compile-clean" in row["status"]
        for row in back_rows
    )
    total_complete += back_complete
    lines.append(
        f"| — | Back matter | {back_complete} | {len(back_rows)} | "
        f"{'complete' if back_complete == len(back_rows) else 'in progress'} |"
    )
    lines.extend(
        [
            "",
            f"Overall: **{total_complete}/{len(data)}** planned content files "
            "are source-reviewed and compile-clean.",
            "",
            "The strict release gate is `./build_and_verify.sh`.",
            "",
        ]
    )
    return "\n".join(lines)


def check_file(path: Path, expected: str) -> bool:
    if not path.exists():
        print(f"Missing generated file: {path.relative_to(ROOT)}", file=sys.stderr)
        return False
    if path.read_text(encoding="utf-8") != expected:
        print(
            f"Stale generated file: {path.relative_to(ROOT)}; "
            "run `python3 source_manifest.py --write`.",
            file=sys.stderr,
        )
        return False
    return True


def main() -> int:
    parser = argparse.ArgumentParser()
    action = parser.add_mutually_exclusive_group()
    action.add_argument("--write", action="store_true")
    action.add_argument("--check", action="store_true")
    args = parser.parse_args()

    data = rows()
    manifest = render_manifest(data)
    status = render_status(data)

    if args.write:
        MANIFEST.write_text(manifest, encoding="utf-8")
        STATUS.write_text(status, encoding="utf-8")
        print(f"WROTE {MANIFEST.relative_to(ROOT)}")
        print(f"WROTE {STATUS.relative_to(ROOT)}")
        return 0
    if args.check:
        ok = check_file(MANIFEST, manifest) and check_file(STATUS, status)
        if ok:
            print("Source manifest and transcription status are current.")
        return 0 if ok else 1

    complete = sum(
        "source-reviewed and compile-clean" in row["status"] for row in data
    )
    print(f"Manifest inventory: {complete}/{len(data)} files complete.")
    print("Pass --write to refresh generated reports or --check to verify them.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
