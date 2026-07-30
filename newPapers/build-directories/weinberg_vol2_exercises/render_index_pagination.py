#!/usr/bin/env python3
"""Render a source-to-live pagination crosswalk from a completed LaTeX build."""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path


CHAPTER_RE = re.compile(
    r"\\contentsline \{section\}\{\\numberline \{(\d+)\}(.*?)\}\{(\d+)\}\{"
)
INDEX_RE = re.compile(
    r"\\contentsline \{section\}\{(Author Index|Subject Index)\}\{(\d+)\}\{"
)
SUBSECTION_RE = re.compile(
    r"\\contentsline \{subsection\}\{"
    r"(Weinberg Exercises|Solutions to Weinberg Exercises|"
    r"Supplementary Exercises|Solutions to Supplementary Exercises|"
    r"Bibliography|References)"
    r"\}\{(\d+)\}\{"
)

PAGE_KEYS = {
    "Weinberg Exercises": "weinberg_exercises_page",
    "Solutions to Weinberg Exercises": "weinberg_solutions_page",
    "Supplementary Exercises": "supplementary_exercises_page",
    "Solutions to Supplementary Exercises": "supplementary_solutions_page",
    "Bibliography": "bibliography_page",
    "References": "references_page",
}


def pdf_page_count(pdf_path: Path) -> int:
    try:
        output = subprocess.check_output(
            ["pdfinfo", str(pdf_path)], text=True, stderr=subprocess.STDOUT
        )
    except (OSError, subprocess.CalledProcessError) as exc:
        raise SystemExit(f"Could not read page count from {pdf_path}: {exc}") from exc
    match = re.search(r"^Pages:\s+(\d+)\s*$", output, re.MULTILINE)
    if not match:
        raise SystemExit(f"pdfinfo did not report a page count for {pdf_path}")
    return int(match.group(1))


def page_span(start: int, end: int) -> str:
    return str(start) if start == end else f"{start}–{end}"


def live_pdf_locator(start: int, end: int, offset: int) -> str:
    return (
        f"{page_span(start, end)} / "
        f"{page_span(start + offset, end + offset)}"
    )


def parse_toc(toc_path: Path) -> tuple[dict[int, dict[str, object]], dict[str, int]]:
    chapters: dict[int, dict[str, object]] = {}
    indexes: dict[str, int] = {}
    current_chapter: int | None = None

    for line in toc_path.read_text(encoding="utf-8").splitlines():
        chapter_match = CHAPTER_RE.search(line)
        if chapter_match:
            current_chapter = int(chapter_match.group(1))
            chapters[current_chapter] = {
                "toc_title": chapter_match.group(2),
                "chapter_start": int(chapter_match.group(3)),
            }
            continue

        index_match = INDEX_RE.search(line)
        if index_match:
            indexes[index_match.group(1)] = int(index_match.group(2))
            current_chapter = None
            continue

        subsection_match = SUBSECTION_RE.search(line)
        if subsection_match and current_chapter is not None:
            chapters[current_chapter][PAGE_KEYS[subsection_match.group(1)]] = int(
                subsection_match.group(2)
            )

    return chapters, indexes


def main() -> int:
    edition_root = Path(__file__).resolve().parent
    metadata_path = edition_root / "exercise-edition.json"
    toc_path = edition_root / "latex" / "master.toc"
    pdf_path = edition_root / "latex" / "master.pdf"
    output_path = edition_root / "INDEX_PAGINATION.md"

    for required in (metadata_path, toc_path, pdf_path):
        if not required.is_file():
            raise SystemExit(f"Missing completed-build input: {required}")

    metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
    toc_chapters, indexes = parse_toc(toc_path)
    chapter_specs = metadata["chapters"]
    expected = [int(chapter["chapter"]) for chapter in chapter_specs]
    if sorted(toc_chapters) != expected:
        raise SystemExit(
            "TOC chapter mismatch: "
            f"expected {expected}, found {sorted(toc_chapters)}"
        )

    required_page_keys = [
        "weinberg_exercises_page",
        "weinberg_solutions_page",
        "supplementary_exercises_page",
        "supplementary_solutions_page",
        "references_page",
    ]
    for chapter_number in expected:
        missing = [
            key for key in required_page_keys if key not in toc_chapters[chapter_number]
        ]
        if missing:
            raise SystemExit(
                f"Chapter {chapter_number} is missing TOC page entries: {missing}"
            )

    total_pages = pdf_page_count(pdf_path)
    page_offset = metadata.get("pdf_arabic_page_offset")
    if not isinstance(page_offset, int) or page_offset < 0:
        raise SystemExit("Metadata pdf_arabic_page_offset must be a nonnegative integer")
    final_live_page = total_pages - page_offset
    if final_live_page < 1:
        raise SystemExit("PDF page count is inconsistent with pdf_arabic_page_offset")
    first_index_page = min(indexes.values()) if indexes else None
    source_index = bool(metadata.get("source_index"))
    if source_index and not first_index_page:
        raise SystemExit("Metadata declares a source index, but no index page is in the TOC")

    lines = [
        "# Index and pagination crosswalk",
        "",
        "This file is generated from `exercise-edition.json` and the completed "
        "`latex/master.toc` by `render_index_pagination.py`; do not edit it by hand.",
        "",
        "Every live locator is shown as **displayed page label / physical PDF "
        f"page**. In this volume the physical PDF page is the Arabic page label "
        f"plus {page_offset}, accounting for the title and Roman-numbered front "
        "matter.",
        "",
    ]
    if source_index:
        lines.extend(
            [
                "The inherited Author and Subject Index entries reproduce Weinberg's "
                "**printed-source page numbers**. They remain source-page references "
                "rather than live page numbers in this expanded, reflowed PDF. Use the "
                "source span below to interpret an inherited index entry and the live "
                "columns or PDF table of contents to navigate this edition.",
                "",
            ]
        )
    else:
        lines.extend(
            [
                "The canonical source volume has no inherited printed Author or Subject "
                "Index in this transcription. The table therefore records only live "
                "exercise-edition pagination.",
                "",
            ]
        )

    lines.extend(
        [
            "| Chapter | Title | Source printed pages | Live chapter pages | "
            "W exercises | W solutions | S exercises | S solutions | References |",
            "|---:|---|---:|---:|---:|---:|---:|---:|---:|",
        ]
    )

    for position, spec in enumerate(chapter_specs):
        number = int(spec["chapter"])
        toc_data = toc_chapters[number]
        start = int(toc_data["chapter_start"])
        if position + 1 < len(chapter_specs):
            next_number = int(chapter_specs[position + 1]["chapter"])
            end = int(toc_chapters[next_number]["chapter_start"]) - 1
        elif first_index_page is not None:
            end = first_index_page - 1
        else:
            end = final_live_page

        source_pages = spec.get("source_printed_pages")
        if source_pages:
            source_span = page_span(int(source_pages[0]), int(source_pages[1]))
        else:
            source_span = "—"

        title = str(spec["title"]).replace("|", r"\|")
        lines.append(
            f"| {number} | {title} | {source_span} | "
            f"{live_pdf_locator(start, end, page_offset)} | "
            f"{live_pdf_locator(int(toc_data['weinberg_exercises_page']), int(toc_data['weinberg_exercises_page']), page_offset)} | "
            f"{live_pdf_locator(int(toc_data['weinberg_solutions_page']), int(toc_data['weinberg_solutions_page']), page_offset)} | "
            f"{live_pdf_locator(int(toc_data['supplementary_exercises_page']), int(toc_data['supplementary_exercises_page']), page_offset)} | "
            f"{live_pdf_locator(int(toc_data['supplementary_solutions_page']), int(toc_data['supplementary_solutions_page']), page_offset)} | "
            f"{live_pdf_locator(int(toc_data['references_page']), int(toc_data['references_page']), page_offset)} |"
        )

    if indexes:
        lines.extend(
            [
                "",
                "Live inherited-index starts: "
                + "; ".join(
                    f"{name} p. {page} / PDF {page + page_offset}"
                    for name, page in sorted(indexes.items())
                )
                + ".",
            ]
        )
    lines.extend(["", f"Completed PDF page count: {total_pages}.", ""])
    output_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {output_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
