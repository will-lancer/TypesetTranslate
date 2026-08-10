#!/usr/bin/env python3
"""Render deterministic written-use artifacts for Physics 253a Chapter 2."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re
import sys
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / "work" / "253a-ch02"
CHAPTER = ROOT / "latex" / "chapters" / "253a" / "chapter02.tex"
TRANSCRIPT = WORK / "transcript.cleaned.jsonl"
ARGUMENT_MAP = WORK / "argument-map.jsonl"
SOURCE_PACKET = WORK / "source-packet-manifest.json"
PROVENANCE = WORK / "provenance.jsonl"
WRITTEN_TRANSCRIPT = WORK / "written-transcript-dispositions.jsonl"
WRITTEN_PAGES = WORK / "written-page-dispositions.jsonl"

SOURCE_RE = re.compile(r"(?m)^\s*%\s*YIN-SOURCE:\s*(.*?)\s*$")
UNIT_ID_RE = re.compile(r"^YIN253A-C02-U\d{3}$")
ARGUMENT_ID_RE = re.compile(r"^YIN253A-C02-A\d{2}$")
EQUATION_ID_RE = re.compile(r"^YIN253A-C02-EQ\d{3}$")
TRANSCRIPT_ID_RE = re.compile(r"^YIN253A-C02-T(\d{6})$")
VIDEO_RE = re.compile(
    r"^([^:]+):(\d{2,}:[0-5]\d:[0-5]\d(?:\.\d{1,3})?)-"
    r"(\d{2,}:[0-5]\d:[0-5]\d(?:\.\d{1,3})?)$"
)
ALLOWED_SOURCE_CLASSES = frozenset(
    {
        "NOTES_EXACT",
        "SPEECH_CLEAN",
        "SOURCE_COMPOSITE",
        "EQUATION_NORMALIZED",
        "EDITORIAL_NOTE",
        "SOURCE_CONFLICT",
    }
)


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            raise ValueError(f"{rel(path)}:{number}: blank JSONL line")
        value = json.loads(line)
        if not isinstance(value, dict):
            raise ValueError(f"{rel(path)}:{number}: row is not an object")
        rows.append(value)
    return rows


def rendered_jsonl(rows: list[dict[str, Any]]) -> str:
    return "".join(
        json.dumps(row, ensure_ascii=False, separators=(",", ":"), sort_keys=True)
        + "\n"
        for row in rows
    )


def parse_fields(payload: str, line: int) -> dict[str, str]:
    fields: dict[str, str] = {}
    for item in payload.split(";"):
        item = item.strip()
        if not item:
            continue
        if "=" not in item:
            raise ValueError(f"chapter line {line}: malformed source field {item!r}")
        key, value = item.split("=", 1)
        key = key.strip().lower()
        if key in fields:
            raise ValueError(f"chapter line {line}: duplicate source field {key}")
        fields[key] = value.strip()
    required = {
        "id",
        "arguments",
        "notes",
        "pdf",
        "video",
        "transcript",
        "equations",
        "class",
    }
    missing = sorted(required - set(fields))
    if missing:
        raise ValueError(f"chapter line {line}: missing source fields {missing}")
    return fields


def comma_values(value: str) -> list[str]:
    if value.strip().casefold() in {"none", "n/a", "na"}:
        return []
    return [item.strip() for item in value.split(",") if item.strip()]


def page_values(value: str, prefix: str | None = None) -> list[int]:
    text = value.strip()
    if text.casefold() in {"none", "n/a", "na"}:
        return []
    pages: set[int] = set()
    for part in comma_values(text):
        if prefix and part.startswith(prefix):
            part = part[len(prefix) :]
        if "-" in part:
            start_text, end_text = part.split("-", 1)
            start, end = int(start_text), int(end_text)
            if end < start:
                raise ValueError(f"descending page range {part!r}")
            pages.update(range(start, end + 1))
        else:
            pages.add(int(part))
    return sorted(pages)


def expand_transcript_values(value: str) -> list[str]:
    output: list[str] = []
    for item in comma_values(value):
        if ".." not in item:
            if TRANSCRIPT_ID_RE.fullmatch(item) is None:
                raise ValueError(f"malformed transcript ID {item!r}")
            output.append(item)
            continue
        start_text, end_text = item.split("..", 1)
        start_match = TRANSCRIPT_ID_RE.fullmatch(start_text)
        end_match = TRANSCRIPT_ID_RE.fullmatch(end_text)
        if start_match is None or end_match is None:
            raise ValueError(f"malformed transcript range {item!r}")
        start, end = int(start_match.group(1)), int(end_match.group(1))
        if end < start:
            raise ValueError(f"descending transcript range {item!r}")
        output.extend(f"YIN253A-C02-T{number:06d}" for number in range(start, end + 1))
    return list(dict.fromkeys(output))


def video_values(value: str) -> list[dict[str, str]]:
    values: list[dict[str, str]] = []
    for item in comma_values(value):
        match = VIDEO_RE.fullmatch(item)
        if match is None:
            raise ValueError(f"malformed video span {item!r}")
        values.append(
            {"video_id": match.group(1), "start": match.group(2), "end": match.group(3)}
        )
    return values


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
    # Labels affect cross-references but print no body text.  Excluding
    # standalone labels keeps the generated span aligned with the renderer's
    # one-comment/one-printed-block contract, including the chapter-end label.
    lines = [
        line
        for line in lines
        if re.fullmatch(r"\s*\\label\{[^{}]+\}\s*", line) is None
    ]
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


def unit_type(body: str, source_class: str) -> str:
    if "\\begin{figure}" in body or "\\begin{tikzpicture}" in body:
        return "figure"
    if re.search(r"\\begin\{(?:equation\*?|align\*?|gather\*?|multline\*?)\}", body):
        return "equation"
    if source_class == "EDITORIAL_NOTE":
        return "editorial_note"
    if re.match(r"\\(?:YinChapter|subsection|subsubsection|label)\b", body):
        return "structural"
    return "prose_span"


def argument_rows() -> list[dict[str, Any]]:
    rows = [row for row in load_jsonl(ARGUMENT_MAP) if ARGUMENT_ID_RE.fullmatch(str(row.get("id", "")))]
    if not rows:
        raise ValueError("argument map has no drafting records")
    ids = [str(row["id"]) for row in rows]
    if len(ids) != len(set(ids)):
        raise ValueError("argument map has duplicate drafting IDs")
    return rows


def argument_ranges(rows: list[dict[str, Any]]) -> dict[str, range]:
    ranges: dict[str, range] = {}
    for row in rows:
        if row.get("record_type") != "conceptual_unit":
            continue
        start_match = TRANSCRIPT_ID_RE.fullmatch(str(row.get("transcript_start_id", "")))
        end_match = TRANSCRIPT_ID_RE.fullmatch(str(row.get("transcript_end_id", "")))
        if start_match is None or end_match is None:
            raise ValueError(f"{row['id']} lacks a valid transcript interval")
        start, end = int(start_match.group(1)), int(end_match.group(1))
        if end < start:
            raise ValueError(f"{row['id']} has a descending transcript interval")
        ranges[str(row["id"])] = range(start, end + 1)
    return ranges


def render() -> tuple[dict[Path, str], dict[str, Any]]:
    if not CHAPTER.is_file():
        raise ValueError(f"missing {rel(CHAPTER)}")
    chapter_text = CHAPTER.read_text(encoding="utf-8")
    chapter_hash = digest(CHAPTER)
    transcript_hash = digest(TRANSCRIPT)
    argument_hash = digest(ARGUMENT_MAP)
    source_packet_hash = json.loads(SOURCE_PACKET.read_text(encoding="utf-8"))[
        "source_packet_sha256"
    ]
    transcript_rows = load_jsonl(TRANSCRIPT)
    segments = [row for row in transcript_rows if row.get("record_type") == "transcript_segment"]
    transcript = {str(row["id"]): row for row in segments}
    arguments = argument_rows()
    ranges = argument_ranges(arguments)

    matches = list(SOURCE_RE.finditer(chapter_text))
    if not matches:
        raise ValueError("Chapter 2 has no YIN-SOURCE comments")
    provenance: list[dict[str, Any]] = []
    seen_units: set[str] = set()
    printed_by_transcript: dict[str, list[str]] = {}
    source_units_by_page: dict[int, list[str]] = {}
    for index, match in enumerate(matches):
        line = chapter_text.count("\n", 0, match.start()) + 1
        fields = parse_fields(match.group(1), line)
        source_id = fields["id"]
        if UNIT_ID_RE.fullmatch(source_id) is None:
            raise ValueError(f"chapter line {line}: malformed unit ID {source_id!r}")
        if source_id in seen_units:
            raise ValueError(f"chapter line {line}: duplicate unit ID {source_id}")
        seen_units.add(source_id)
        argument_ids = comma_values(fields["arguments"])
        if not argument_ids or any(ARGUMENT_ID_RE.fullmatch(value) is None for value in argument_ids):
            raise ValueError(f"chapter line {line}: malformed argument IDs")
        known_argument_ids = {str(row["id"]) for row in arguments}
        unknown_arguments = sorted(set(argument_ids) - known_argument_ids)
        if unknown_arguments:
            raise ValueError(f"chapter line {line}: unknown arguments {unknown_arguments}")
        equation_ids = comma_values(fields["equations"])
        if any(EQUATION_ID_RE.fullmatch(value) is None for value in equation_ids):
            raise ValueError(f"chapter line {line}: malformed equation IDs")
        transcript_ids = expand_transcript_values(fields["transcript"])
        unknown_transcript = sorted(set(transcript_ids) - set(transcript))
        if unknown_transcript:
            raise ValueError(f"chapter line {line}: unknown transcript IDs {unknown_transcript}")
        source_class = fields["class"].upper()
        if source_class not in ALLOWED_SOURCE_CLASSES:
            raise ValueError(f"chapter line {line}: unsupported source class {source_class}")
        note_pages = page_values(fields["notes"], "253a:")
        pdf_pages = page_values(fields["pdf"])
        video_spans = video_values(fields["video"])
        end = matches[index + 1].start() if index + 1 < len(matches) else len(chapter_text)
        body = visible_body(chapter_text[match.end() : end])
        if not body:
            raise ValueError(f"chapter line {line}: source unit {source_id} has no printed body")
        for transcript_id in transcript_ids:
            printed_by_transcript.setdefault(transcript_id, []).append(source_id)
        for page in pdf_pages:
            source_units_by_page.setdefault(page, []).append(source_id)
        excerpt = " ".join(
            str(transcript[transcript_id].get("cleaned_text") or transcript[transcript_id].get("raw_text") or "")
            for transcript_id in transcript_ids
        )
        excerpt = " ".join(excerpt.split())
        if len(excerpt) > 1200:
            excerpt = excerpt[:1197].rstrip() + "..."
        provenance.append(
            {
                "id": source_id,
                "record_type": "written_provenance",
                "tex_target": f"latex/chapters/253a/chapter02.tex:{line}",
                "unit_type": unit_type(body, source_class),
                "source_class": source_class,
                "argument_unit_ids": argument_ids,
                "note_pages": note_pages,
                "pdf_pages": pdf_pages,
                "video_spans": video_spans,
                "transcript_record_ids": transcript_ids,
                "equation_source_ids": equation_ids,
                "source_excerpt": excerpt or "Handwritten or boundary evidence named by the source comment.",
                "final_text": body,
                "editorial_operations": [
                    "written_prose_recast" if source_class != "NOTES_EXACT" else "notes_exact_typesetting"
                ],
                "confidence": 1.0 if source_class in {"NOTES_EXACT", "SPEECH_CLEAN"} else 0.95,
                "review_status": "generated_from_current_chapter",
                "chapter_sha256": chapter_hash,
                "transcript_sha256": transcript_hash,
                "argument_map_sha256": argument_hash,
                "source_packet_sha256": source_packet_hash,
            }
        )

    written_transcript: list[dict[str, Any]] = []
    for segment in segments:
        transcript_id = str(segment["id"])
        number_match = TRANSCRIPT_ID_RE.fullmatch(transcript_id)
        assert number_match is not None
        number = int(number_match.group(1))
        scope = str(segment.get("chapter_scope"))
        allocated = [argument_id for argument_id, interval in ranges.items() if number in interval]
        if scope == "core" and len(allocated) != 1:
            raise ValueError(
                f"core transcript {transcript_id} has {len(allocated)} argument allocations"
            )
        printed_units = printed_by_transcript.get(transcript_id, [])
        if scope != "core":
            written_use = "outside_chapter"
            reason = f"Frozen chapter scope is {scope}."
        elif segment.get("cleaned_text") is None:
            written_use = "source_material_removed"
            reason = f"Frozen disposition: {segment.get('disposition')}."
        elif printed_units:
            written_use = "included_directly"
            reason = "The source record is cited by one or more printed source units."
        else:
            written_use = "merged_into_argument"
            reason = "The cleaned source is absorbed into its allocated conceptual argument."
        written_transcript.append(
            {
                "record_type": "written_transcript_disposition",
                "transcript_record_id": transcript_id,
                "source_span_id": segment.get("source_span_id"),
                "video_id": segment.get("video_id"),
                "start": segment.get("start"),
                "end": segment.get("end"),
                "chapter_scope": scope,
                "argument_unit_ids": allocated,
                "printed_source_unit_ids": printed_units,
                "written_use": written_use,
                "reason": reason,
                "chapter_sha256": chapter_hash,
                "transcript_sha256": transcript_hash,
                "argument_map_sha256": argument_hash,
            }
        )

    written_pages: list[dict[str, Any]] = []
    for page in range(20, 69):
        argument_ids = [
            str(row["id"])
            for row in arguments
            if page in [int(value) for value in row.get("pdf_pages", [])]
        ]
        if page == 20:
            outcome = "included_chapter_divider"
            reason = "Physical page 20 supplies the Chapter 2 title and opening boundary."
        elif 21 <= page <= 62:
            outcome = "included_in_written_chapter"
            reason = "The handwritten lecture page is covered by the argument map and provenance."
            if not argument_ids:
                raise ValueError(f"physical page {page} has no argument-map allocation")
        elif 63 <= page <= 67:
            outcome = "deferred_assignment_integration"
            reason = "Problem Set 2 is reserved for later assignment integration."
        else:
            outcome = "next_chapter_boundary_evidence_only"
            reason = "Physical page 68 is the Chapter 3 divider and supplies no Chapter 2 content."
        written_pages.append(
            {
                "record_type": "written_page_disposition",
                "physical_pdf_page": page,
                "note_page": page - 11 if 21 <= page <= 62 else None,
                "outcome": outcome,
                "argument_unit_ids": argument_ids,
                "printed_source_unit_ids": source_units_by_page.get(page, []),
                "reason": reason,
                "chapter_sha256": chapter_hash,
                "argument_map_sha256": argument_hash,
                "source_packet_sha256": source_packet_hash,
            }
        )

    rendered = {
        PROVENANCE: rendered_jsonl(provenance),
        WRITTEN_TRANSCRIPT: rendered_jsonl(written_transcript),
        WRITTEN_PAGES: rendered_jsonl(written_pages),
    }
    stats = {
        "argument_records": len(arguments),
        "argument_units": len(ranges),
        "chapter_sha256": chapter_hash,
        "provenance_records": len(provenance),
        "source_packet_sha256": source_packet_hash,
        "transcript_dispositions": len(written_transcript),
        "transcript_sha256": transcript_hash,
        "written_page_dispositions": len(written_pages),
    }
    return rendered, stats


def main() -> int:
    parser = argparse.ArgumentParser()
    action = parser.add_mutually_exclusive_group(required=True)
    action.add_argument("--write", action="store_true")
    action.add_argument("--check", action="store_true")
    args = parser.parse_args()
    try:
        rendered, stats = render()
    except (OSError, ValueError, KeyError, json.JSONDecodeError) as exc:
        print(f"Chapter 2 artifact render failed: {exc}", file=sys.stderr)
        return 1
    if args.check:
        stale = [rel(path) for path, text in rendered.items() if not path.is_file() or path.read_text(encoding="utf-8") != text]
        if stale:
            print(f"stale Chapter 2 generated artifacts: {stale}", file=sys.stderr)
            return 1
    else:
        for path, text in rendered.items():
            temporary = path.with_suffix(path.suffix + ".tmp")
            temporary.write_text(text, encoding="utf-8")
            temporary.replace(path)
    print(json.dumps(stats, ensure_ascii=False, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
