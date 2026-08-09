#!/usr/bin/env python3
"""Render deterministic provenance for the active written Yin chapter."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re
import sys
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
PILOT = ROOT / "work" / "pilot"
CHAPTER = ROOT / "latex" / "chapters" / "253a" / "chapter01.tex"
TRANSCRIPT = PILOT / "transcript.cleaned.jsonl"
OUTPUT = PILOT / "provenance.jsonl"

SOURCE_RE = re.compile(r"(?m)^\s*%\s*YIN-SOURCE:\s*(.*?)\s*$")
TRANSCRIPT_SOURCE_RE = re.compile(r"^YIN253A-C01-V-(T\d{6}[AB]?)$")
VIDEO_RE = re.compile(
    r"^([^:]+):(\d{2,}:[0-5]\d:[0-5]\d(?:\.\d{1,3})?)-"
    r"(\d{2,}:[0-5]\d:[0-5]\d(?:\.\d{1,3})?)$"
)


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    return [
        json.loads(line)
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]


def strip_tex_comment(line: str) -> str:
    for index, character in enumerate(line):
        if character != "%":
            continue
        backslashes = 0
        cursor = index - 1
        while cursor >= 0 and line[cursor] == "\\":
            backslashes += 1
            cursor -= 1
        if backslashes % 2 == 0:
            return line[:index]
    return line


def visible_body(chunk: str) -> str:
    lines = [strip_tex_comment(line).rstrip() for line in chunk.splitlines()]
    while lines and not lines[0].strip():
        lines.pop(0)
    while lines and not lines[-1].strip():
        lines.pop()
    compact: list[str] = []
    previous_blank = False
    for line in lines:
        blank = not line.strip()
        if blank and previous_blank:
            continue
        compact.append(line)
        previous_blank = blank
    return "\n".join(compact)


def parse_fields(payload: str, line: int) -> dict[str, str]:
    fields: dict[str, str] = {}
    for item in payload.split(";"):
        item = item.strip()
        if not item:
            continue
        if "=" not in item:
            raise ValueError(f"chapter line {line}: malformed source field {item!r}")
        key, value = item.split("=", 1)
        fields[key.strip().lower()] = value.strip()
    required = {"id", "notes", "pdf", "video", "class"}
    missing = sorted(required - set(fields))
    if missing:
        raise ValueError(f"chapter line {line}: missing source fields {missing}")
    return fields


def page_values(value: str, prefix: str | None = None) -> list[int]:
    text = value.strip()
    if text.casefold() in {"none", "n/a", "na"}:
        return []
    if prefix and text.startswith(prefix):
        text = text[len(prefix) :]
    pages: set[int] = set()
    for part in text.split(","):
        part = part.strip()
        if not part:
            continue
        if prefix and part.startswith(prefix):
            part = part[len(prefix) :]
        if "-" in part:
            start_text, end_text = part.split("-", 1)
            start = int(start_text)
            end = int(end_text)
            pages.update(range(start, end + 1))
        else:
            pages.add(int(part))
    return sorted(pages)


def video_values(value: str) -> tuple[str | None, str | None, str | None]:
    if value.casefold() in {"none", "n/a", "na"}:
        return None, None, None
    match = VIDEO_RE.fullmatch(value)
    if match is None:
        raise ValueError(f"malformed video source {value!r}")
    return match.group(1), match.group(2), match.group(3)


def argument_id(source_id: str, note_pages: list[int]) -> list[str]:
    match = TRANSCRIPT_SOURCE_RE.fullmatch(source_id)
    if match:
        number = int(re.search(r"\d{6}", match.group(1)).group(0))
        ranges = (
            (16, 61, "YIN253A-C01-A01"),
            (64, 91, "YIN253A-C01-A02"),
            (94, 182, "YIN253A-C01-A03"),
            (185, 200, "YIN253A-C01-A04"),
            (204, 257, "YIN253A-C01-A05"),
            (262, 303, "YIN253A-C01-A06"),
            (306, 317, "YIN253A-C01-A07"),
        )
        for start, end, target in ranges:
            if start <= number <= end:
                return [target]
    if source_id in {"YIN253A-C01-N001", "YIN253A-C01-N002"}:
        return ["YIN253A-C01-A03"]
    if source_id.endswith("U095"):
        return ["YIN253A-C01-A07"]
    if note_pages:
        page = min(note_pages)
        by_page = {
            1: "YIN253A-C01-A01",
            2: "YIN253A-C01-A02",
            3: "YIN253A-C01-A03",
            4: "YIN253A-C01-A03",
            5: "YIN253A-C01-A04",
            6: "YIN253A-C01-A05",
            7: "YIN253A-C01-A06",
            8: "YIN253A-C01-A06",
            9: "YIN253A-C01-A07",
        }
        if page in by_page:
            return [by_page[page]]
    return []


def unit_type(source_class: str, body: str) -> str:
    if "\\begin{figure}" in body or "\\begin{tikzpicture}" in body:
        return "figure"
    if re.search(r"\\begin\{(?:equation\*?|align\*?|gather\*?|multline\*?)\}", body):
        return "equation"
    if source_class == "EDITORIAL_NOTE":
        return "editorial_note"
    if not body.strip():
        return "source_span"
    return "prose_span"


def operations(source_class: str, body: str) -> list[str]:
    mapping = {
        "NOTES_EXACT": ["notes_exact_typesetting"],
        "SPEECH_CLEAN": ["written_prose_recast"],
        "SOURCE_COMPOSITE": [
            "written_prose_recast",
            "note_video_reconciliation",
        ],
        "EQUATION_NORMALIZED": ["reviewed_equation_normalization"],
        "EDITORIAL_NOTE": ["editorial_bridge"],
        "SOURCE_CONFLICT": ["source_conflict_recorded"],
    }
    value = list(mapping.get(source_class, ["source_preserved"]))
    if not body.strip():
        value.append("merged_into_adjacent_written_unit")
    return value


def normalize_confidence(value: Any) -> float:
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        return float(value)
    if isinstance(value, str):
        return {"high": 0.99, "medium": 0.85, "low": 0.6}.get(
            value.casefold(), 0.8
        )
    return 0.99


def render() -> tuple[str, dict[str, int | str]]:
    chapter_text = CHAPTER.read_text(encoding="utf-8")
    chapter_hash = hashlib.sha256(CHAPTER.read_bytes()).hexdigest()
    transcript_hash = hashlib.sha256(TRANSCRIPT.read_bytes()).hexdigest()
    transcript_rows = load_jsonl(TRANSCRIPT)
    transcript = {
        row["id"]: row
        for row in transcript_rows
        if isinstance(row.get("id"), str)
    }

    matches = list(SOURCE_RE.finditer(chapter_text))
    output: list[dict[str, Any]] = []
    empty = 0
    for index, match in enumerate(matches):
        line = chapter_text.count("\n", 0, match.start()) + 1
        fields = parse_fields(match.group(1), line)
        end = matches[index + 1].start() if index + 1 < len(matches) else len(chapter_text)
        body = visible_body(chapter_text[match.end() : end])
        if not body:
            empty += 1
        source_id = fields["id"]
        source_class = fields["class"].upper()
        notes = page_values(fields["notes"], "253a:")
        pdfs = page_values(fields["pdf"])
        video_id, video_start, video_end = video_values(fields["video"])
        transcript_ids: list[str] = []
        source_excerpt: str
        confidence = 0.99
        transcript_match = TRANSCRIPT_SOURCE_RE.fullmatch(source_id)
        if transcript_match:
            transcript_id = "YIN-OY-" + transcript_match.group(1)
            transcript_ids = [transcript_id]
            source = transcript.get(transcript_id, {})
            source_excerpt = (
                source.get("cleaned_text")
                or source.get("raw_text")
                or f"Transcript span {transcript_id} has no retained lexical text."
            )
            confidence = normalize_confidence(source.get("confidence"))
        elif source_class in {"NOTES_EXACT", "EQUATION_NORMALIZED"}:
            source_excerpt = (
                "Exact handwritten source in work/pilot/notes-exact.tex, "
                f"note page(s) {notes or 'not applicable'}."
            )
        else:
            source_excerpt = (
                "Editorial or reconciled source unit identified by its chapter "
                "source comment."
            )

        output.append(
            {
                "id": source_id,
                "tex_target": f"latex/chapters/253a/chapter01.tex:{line}",
                "unit_type": unit_type(source_class, body),
                "source_class": source_class,
                "note_pages": notes,
                "pdf_pages": pdfs,
                "video_id": video_id,
                "video_start": video_start,
                "video_end": video_end,
                "transcript_record_ids": transcript_ids,
                "argument_unit_ids": argument_id(source_id, notes),
                "source_excerpt": source_excerpt,
                "final_text": body,
                "cleaning_operations": operations(source_class, body),
                "reason": (
                    "The source span is absorbed into the adjacent written argument."
                    if not body
                    else "The source material is recast under WRITING_STYLE.md."
                ),
                "confidence": confidence,
                "review_status": "generated_from_current_chapter",
                "writing_mode": "written_prose",
                "chapter_sha256": chapter_hash,
                "transcript_sha256": transcript_hash,
            }
        )

    rendered = "".join(
        json.dumps(row, ensure_ascii=False, separators=(",", ":")) + "\n"
        for row in output
    )
    return rendered, {
        "chapter_sha256": chapter_hash,
        "empty_source_spans": empty,
        "provenance_records": len(output),
        "transcript_sha256": transcript_hash,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    action = parser.add_mutually_exclusive_group(required=True)
    action.add_argument("--write", action="store_true")
    action.add_argument("--check", action="store_true")
    args = parser.parse_args()
    rendered, stats = render()
    if args.check:
        if not OUTPUT.is_file() or OUTPUT.read_text(encoding="utf-8") != rendered:
            print(
                f"{OUTPUT.relative_to(ROOT)} is stale; run "
                "scripts/render_written_provenance.py --write",
                file=sys.stderr,
            )
            return 1
    else:
        temporary = OUTPUT.with_suffix(".jsonl.tmp")
        temporary.write_text(rendered, encoding="utf-8")
        temporary.replace(OUTPUT)
    print(json.dumps(stats, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
