#!/usr/bin/env python3
"""Materialize the stable section plan without overwriting transcription."""

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
    optional: bool


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
            r"\((?:printed\s+)?p\.\s*(?P<page>\d+)\)",
            body,
        )
        if parsed is None:
            raise ValueError(
                f"Cannot parse SECTION_PLAN.md entry for "
                f"chapter{chapter:02d}/{match.group('filename')}: {body}"
            )
        raw_title = parsed.group("title").strip()
        optional = raw_title.endswith("*")
        title = raw_title.removesuffix("*").rstrip()
        sections.setdefault(chapter, []).append(
            SectionSpec(
                chapter=chapter,
                filename=match.group("filename"),
                number=parsed.group("number"),
                title=title,
                printed_page=int(parsed.group("page")),
                optional=optional,
            )
        )

    if set(chapter_titles) != set(range(1, 17)):
        raise ValueError("SECTION_PLAN.md must define Chapters 1--16.")
    if sum(map(len, sections.values())) != 122:
        raise ValueError("SECTION_PLAN.md must define exactly 122 sections.")
    return chapter_titles, sections


def introduction_stub(chapter: int, title: str) -> str:
    return (
        f"% Source: Weinberg GR, physical PDF pp. TODO--TODO "
        f"(printed chapter start TODO).\n"
        f"% Coverage: Chapter {chapter} opening material before Section "
        f"{chapter}.1.\n"
        "% Figures/tables/footnotes: pending source inventory.\n"
        "% Status: not started.\n"
        "% Uncertainties: none.\n\n"
        f"% TODO TRANSCRIPTION: Chapter {chapter}, {title}, opening material.\n"
    )


def section_stub(spec: SectionSpec) -> str:
    optional = r"\optionalreading" if spec.optional else ""
    return (
        "% Source: Weinberg GR, physical PDF pp. TODO--TODO "
        f"(printed p. {spec.printed_page} onward).\n"
        f"% Coverage: Section {spec.number}, {spec.title}; "
        "equation inventory pending.\n"
        "% Figures/tables/footnotes: pending source inventory.\n"
        "% Status: not started.\n"
        "% Uncertainties: none.\n\n"
        f"\\subsection{{{spec.title}{optional}}}"
        f"\\label{{sec:{spec.number}}}\n"
        f"% TODO TRANSCRIPTION: Section {spec.number}.\n"
    )


def backmatter_stub(chapter: int) -> str:
    return (
        "% Source: Weinberg GR, physical PDF pp. TODO--TODO "
        "(printed pp. TODO--TODO).\n"
        f"% Coverage: Chapter {chapter} bibliography, references, and "
        "end material.\n"
        "% Figures/tables/footnotes: pending source inventory.\n"
        "% Status: not started.\n"
        "% Uncertainties: none.\n\n"
        f"% TODO TRANSCRIPTION: Chapter {chapter} back matter.\n"
    )


def assembly_text(
    chapter: int,
    title: str,
    specs: list[SectionSpec],
) -> str:
    inputs = ["introduction.tex", *(spec.filename for spec in specs), "backmatter.tex"]
    lines = [
        f"% Chapter {chapter}: physical source range TODO--TODO.",
        f"\\section{{{title}}}",
        "",
    ]
    lines.extend(
        f"\\input{{chapters/chapter{chapter:02d}/{filename}}}"
        for filename in inputs
    )
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--write",
        action="store_true",
        help="create missing files and replace untouched TODO chapter wrappers",
    )
    args = parser.parse_args()

    chapter_titles, sections = parse_plan()
    pending: list[tuple[Path, str]] = []

    for chapter in range(1, 17):
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
            (chapter_dir / "backmatter.tex", backmatter_stub(chapter)),
        ]
        pending.extend(
            (path, content) for path, content in candidates if not path.exists()
        )

        wrapper = CHAPTERS / f"chapter{chapter:02d}.tex"
        if wrapper.exists():
            wrapper_text = wrapper.read_text(encoding="utf-8")
            untouched = (
                "TODO TRANSCRIPTION" in wrapper_text
                and "\\input{" not in wrapper_text
            )
            if untouched:
                pending.append(
                    (
                        wrapper,
                        assembly_text(
                            chapter,
                            chapter_titles[chapter],
                            sections[chapter],
                        ),
                    )
                )

    creates = sum(not path.exists() for path, _ in pending)
    updates = len(pending) - creates
    print(
        f"Scaffold plan: {creates} missing files and "
        f"{updates} untouched wrappers."
    )
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
