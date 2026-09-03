#!/usr/bin/env python3
"""Materialize the Wald section plan without overwriting transcription."""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parent
PLAN = ROOT / "SECTION_PLAN.md"
CHAPTERS = ROOT / "latex" / "chapters"

CHAPTER_RE = re.compile(r"^## Chapter (\d+) — (.+)$", re.MULTILINE)
SECTION_RE = re.compile(
    r"^- `chapter(?P<chapter>\d{2})/(?P<filename>sec\d+\.tex)` — "
    r"(?P<body>.*?)(?=^- `chapter|^## |\Z)",
    re.MULTILINE | re.DOTALL,
)


@dataclass(frozen=True)
class SectionSpec:
    chapter: int
    filename: str
    number: str
    title: str
    printed_page: int


def parse_plan() -> tuple[dict[int, str], dict[int, list[SectionSpec]]]:
    text = PLAN.read_text(encoding="utf-8")
    chapter_titles = {
        int(number): title.strip()
        for number, title in CHAPTER_RE.findall(text)
    }
    sections: dict[int, list[SectionSpec]] = {
        chapter: [] for chapter in chapter_titles
    }

    for match in SECTION_RE.finditer(text):
        chapter = int(match.group("chapter"))
        body = re.sub(r"\s+", " ", match.group("body")).strip()
        parsed = re.fullmatch(
            r"(?P<number>\d+\.\d+)\s+(?P<title>.+?)\s+"
            r"\(printed p\. (?P<page>\d+)\)",
            body,
        )
        if parsed is None:
            raise ValueError(
                "Cannot parse SECTION_PLAN.md entry for "
                f"chapter{chapter:02d}/{match.group('filename')}: {body}"
            )
        sections[chapter].append(
            SectionSpec(
                chapter=chapter,
                filename=match.group("filename"),
                number=parsed.group("number"),
                title=parsed.group("title").strip(),
                printed_page=int(parsed.group("page")),
            )
        )

    if set(chapter_titles) != set(range(1, 15)):
        raise ValueError("SECTION_PLAN.md must define Chapters 1--14.")
    if sum(map(len, sections.values())) != 52:
        raise ValueError("SECTION_PLAN.md must define exactly 52 sections.")
    return chapter_titles, sections


def header(coverage: str, printed: str = "TODO--TODO") -> str:
    return (
        "% Source: Wald GR, physical PDF pp. TODO--TODO\n"
        f"%         (printed pp. {printed}).\n"
        f"% Coverage: {coverage}\n"
        "% Figures/tables/footnotes: pending source inventory.\n"
        "% Status: not started.\n"
        "% Uncertainties: none.\n\n"
    )


def introduction_stub(chapter: int, title: str) -> str:
    return header(
        f"Chapter {chapter} opening material before Section {chapter}.1."
    ) + f"% TODO TRANSCRIPTION: Chapter {chapter}, {title}, opening material.\n"


def section_stub(spec: SectionSpec) -> str:
    return (
        header(
            f"Section {spec.number}, {spec.title}; equation inventory pending.",
            f"{spec.printed_page} onward",
        )
        + f"\\subsection{{{spec.title}}}\\label{{sec:{spec.number}}}\n"
        + f"% TODO TRANSCRIPTION: Section {spec.number}.\n"
    )


def problems_stub(chapter: int) -> str:
    return header(
        f"Chapter {chapter} problems and end material."
    ) + f"% TODO TRANSCRIPTION: Chapter {chapter} problems.\n"


def assembly_text(
    chapter: int,
    title: str,
    specs: list[SectionSpec],
) -> str:
    filenames = [
        "introduction.tex",
        *(spec.filename for spec in specs),
        "problems.tex",
    ]
    lines = [
        f"% Chapter {chapter}: physical source range TODO--TODO.",
        f"\\section{{{title}}}",
        "",
    ]
    lines.extend(
        f"\\input{{chapters/chapter{chapter:02d}/{filename}}}"
        for filename in filenames
    )
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--write",
        action="store_true",
        help="create missing files without overwriting existing files",
    )
    args = parser.parse_args()

    chapter_titles, sections = parse_plan()
    pending: list[tuple[Path, str]] = []

    for chapter in range(1, 15):
        chapter_dir = CHAPTERS / f"chapter{chapter:02d}"
        candidates = [
            (
                chapter_dir / "introduction.tex",
                introduction_stub(chapter, chapter_titles[chapter]),
            ),
            *[
                (chapter_dir / spec.filename, section_stub(spec))
                for spec in sections[chapter]
            ],
            (chapter_dir / "problems.tex", problems_stub(chapter)),
            (
                CHAPTERS / f"chapter{chapter:02d}.tex",
                assembly_text(chapter, chapter_titles[chapter], sections[chapter]),
            ),
        ]
        pending.extend(
            (path, content) for path, content in candidates if not path.exists()
        )

    print(f"Scaffold plan: {len(pending)} missing files.")
    if not args.write:
        print("Dry run only; pass --write to materialize the plan.")
        return 0

    for path, content in pending:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        print(f"WROTE {path.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

