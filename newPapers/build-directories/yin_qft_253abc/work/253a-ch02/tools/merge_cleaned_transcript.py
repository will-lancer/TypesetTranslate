#!/usr/bin/env python3
"""Validate Pass 2 lanes and render the canonical Chapter 2 transcript."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import re
from typing import Any


ROOT = Path(__file__).resolve().parents[3]
WORK = ROOT / "work" / "253a-ch02"
MANIFEST = WORK / "raw-caption-lane-manifest.jsonl"
OUTPUT = WORK / "transcript.cleaned.jsonl"
DISPOSITIONS = WORK / "transcript-dispositions.jsonl"

TIME_RE = re.compile(r"(\d{2}):(\d{2}):(\d{2})(?:\.(\d{1,3}))?")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    rows = []
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            raise ValueError(f"{path}:{number}: blank JSONL line")
        value = json.loads(line)
        if not isinstance(value, dict):
            raise ValueError(f"{path}:{number}: JSONL row is not an object")
        rows.append(value)
    return rows


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    rendered = "".join(
        json.dumps(row, ensure_ascii=False, separators=(",", ":")) + "\n"
        for row in rows
    )
    path.write_text(rendered, encoding="utf-8")


def milliseconds(value: str) -> int:
    match = TIME_RE.fullmatch(value)
    if match is None:
        raise ValueError(f"malformed timestamp: {value!r}")
    hours, minutes, seconds = (int(match.group(index)) for index in range(1, 4))
    fraction = (match.group(4) or "").ljust(3, "0")
    return ((hours * 60 + minutes) * 60 + seconds) * 1000 + int(fraction or 0)


def normalize_space(value: str) -> str:
    return " ".join(value.split())


def is_audit_row(row: dict[str, Any]) -> bool:
    kind = str(row.get("record_type", "")).casefold()
    return kind in {"lane_audit", "transcript_lane_audit", "metadata"} or (
        "coverage_exact" in row and "raw_text" not in row
    )


def scope_for(
    video_id: str,
    start: str,
    intervals: dict[str, tuple[int, int]],
) -> str:
    core_start, core_end = intervals[video_id]
    row_start = milliseconds(start)
    if row_start < core_start:
        return "pre_core"
    if row_start >= core_end:
        if video_id == "TtMNnZ8__UU":
            return "next_chapter"
        return "post_core"
    return "core"


def main() -> None:
    chapter_metadata = json.loads(
        (WORK / "chapter-metadata.json").read_text(encoding="utf-8")
    )
    video_order = list(chapter_metadata["video_order"])
    video_rank = {video_id: index for index, video_id in enumerate(video_order)}
    intervals = {
        row["video_id"]: (milliseconds(row["core_start"]), milliseconds(row["core_end"]))
        for row in chapter_metadata["chapter_intervals"]
    }

    manifest = load_jsonl(MANIFEST)
    errors: list[str] = []
    lane_summaries: list[dict[str, Any]] = []
    collected: list[dict[str, Any]] = []

    for lane in manifest:
        lane_id = lane["lane_id"]
        raw_path = ROOT / lane["raw_lane_path"]
        cleaned_path = ROOT / lane["expected_output"]
        if not cleaned_path.is_file():
            errors.append(f"{lane_id}: missing {cleaned_path.relative_to(ROOT)}")
            continue
        raw_rows = load_jsonl(raw_path)
        raw_events = [row for row in raw_rows if row.get("record_type") == "raw_caption_event"]
        raw_by_source_index = {int(row["source_event_index"]): row for row in raw_events}
        expected_indices = [int(row["source_event_index"]) for row in raw_events]

        cleaned_rows = load_jsonl(cleaned_path)
        segments = [row for row in cleaned_rows if row.get("record_type") == "transcript_segment"]
        audit_rows = [row for row in cleaned_rows if is_audit_row(row)]
        if len(audit_rows) != 1:
            errors.append(f"{lane_id}: expected one lane audit row, found {len(audit_rows)}")

        consumed: list[int] = []
        previous_end = -1
        for row_number, segment in enumerate(segments, 1):
            context = f"{lane_id}:segment {row_number}"
            if segment.get("lane_id") != lane_id:
                errors.append(f"{context}: lane_id mismatch")
            if segment.get("video_id") != lane["video_id"]:
                errors.append(f"{context}: video_id mismatch")
            indices = segment.get("source_event_indices")
            if not isinstance(indices, list) or not indices or not all(
                isinstance(value, int) and not isinstance(value, bool) for value in indices
            ):
                errors.append(f"{context}: source_event_indices must be a nonempty integer list")
                continue
            if indices != sorted(indices):
                errors.append(f"{context}: source_event_indices are not ordered")
            missing = [value for value in indices if value not in raw_by_source_index]
            if missing:
                errors.append(f"{context}: unknown source_event_indices {missing[:8]}")
                continue
            if indices[0] <= previous_end:
                errors.append(f"{context}: source-event overlap or order reversal")
            previous_end = indices[-1]
            consumed.extend(indices)

            source_events = [raw_by_source_index[value] for value in indices]
            event_scopes = {
                scope_for(lane["video_id"], str(event["start"]), intervals)
                for event in source_events
            }
            if len(event_scopes) != 1:
                errors.append(
                    f"{context}: source-event cue starts cross a frozen core boundary "
                    f"({', '.join(sorted(event_scopes))})"
                )
            expected_raw_text = normalize_space(
                " ".join(str(event["raw_text"]) for event in source_events)
            )
            supplied_raw_text = normalize_space(str(segment.get("raw_text", "")))
            if supplied_raw_text != expected_raw_text:
                errors.append(
                    f"{context}: raw_text differs from source events "
                    f"({len(supplied_raw_text)} versus {len(expected_raw_text)} characters)"
                )
            expected_start = source_events[0]["start"]
            expected_end = source_events[-1]["end"]
            if segment.get("start") != expected_start:
                errors.append(
                    f"{context}: start {segment.get('start')!r} != {expected_start!r}"
                )
            if segment.get("end") != expected_end:
                errors.append(
                    f"{context}: end {segment.get('end')!r} != {expected_end!r}"
                )
            if milliseconds(str(expected_start)) >= milliseconds(str(expected_end)):
                errors.append(f"{context}: nonpositive interval")

            cleaned_text = segment.get("cleaned_text")
            if cleaned_text is not None and not isinstance(cleaned_text, str):
                errors.append(f"{context}: cleaned_text must be a string or null")
            operations = segment.get("operations")
            if not isinstance(operations, list):
                errors.append(f"{context}: operations must be a list")
            for field in ("disposition", "confidence"):
                if field not in segment:
                    errors.append(f"{context}: missing {field}")

            collected.append(
                {
                    **segment,
                    "source": {
                        "lane_id": lane_id,
                        "lane_path": lane["expected_output"],
                        "raw_lane_path": lane["raw_lane_path"],
                        "source_event_indices": indices,
                    },
                }
            )

        if consumed != expected_indices:
            missing = [value for value in expected_indices if value not in set(consumed)]
            duplicate_count = len(consumed) - len(set(consumed))
            errors.append(
                f"{lane_id}: coverage mismatch; expected={len(expected_indices)} "
                f"consumed={len(consumed)} missing={missing[:12]} duplicates={duplicate_count}"
            )

        lane_summaries.append(
            {
                "lane_id": lane_id,
                "video_id": lane["video_id"],
                "start": lane["start"],
                "end": lane["end"],
                "raw_lane_path": lane["raw_lane_path"],
                "raw_lane_sha256": lane["raw_lane_sha256"],
                "cleaned_lane_path": lane["expected_output"],
                "cleaned_lane_sha256": sha256(cleaned_path),
                "raw_event_count": len(expected_indices),
                "consumed_event_count": len(consumed),
                "segment_count": len(segments),
            }
        )

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        raise SystemExit(f"Pass 2 merge failed with {len(errors)} error(s)")

    collected.sort(
        key=lambda row: (
            video_rank[row["video_id"]],
            milliseconds(row["start"]),
            milliseconds(row["end"]),
        )
    )
    canonical: list[dict[str, Any]] = []
    counts = {"core": 0, "pre_core": 0, "post_core": 0, "next_chapter": 0}
    for index, row in enumerate(collected, 1):
        transcript_id = f"YIN253A-C02-T{index:06d}"
        source_span_id = f"YIN253A-C02-V-T{index:06d}"
        scope = scope_for(row["video_id"], row["start"], intervals)
        counts[scope] += 1
        canonical.append(
            {
                **row,
                "id": transcript_id,
                "source_span_id": source_span_id,
                "chapter_scope": scope,
                "record_type": "transcript_segment",
            }
        )

    metadata = {
        "id": "YIN253A-C02-TRANSCRIPT-METADATA",
        "record_type": "transcript_metadata",
        "schema_version": 2,
        "chapter_id": "253a-ch02",
        "video_order": video_order,
        "chapter_intervals": chapter_metadata["chapter_intervals"],
        "endpoint_convention": "[start,end)",
        "raw_vtt": {
            "path": "work/253a-ch02/transcript.raw.vtt",
            "sha256": sha256(WORK / "transcript.raw.vtt"),
            "bytes": (WORK / "transcript.raw.vtt").stat().st_size,
            "caption_kind": "six-video YouTube autogenerated English VTT anthology",
        },
        "inputs": lane_summaries,
        "counts": {
            "lane_count": len(lane_summaries),
            "canonical_segment_count": len(canonical),
            "raw_event_count": sum(row["raw_event_count"] for row in lane_summaries),
            "cleaned_nonnull_count": sum(row.get("cleaned_text") is not None for row in canonical),
            "scope_counts": counts,
        },
        "cleaning_policy": {
            "role": "literal cleanup under MASTER_PROMPT.md and WRITING_STYLE.md",
            "boundary_assignment": (
                "Each cumulative caption event is assigned by cue start under the frozen "
                "half-open chapter interval; a cue may end beyond the boundary, and no "
                "cleaned segment may combine event starts from different scopes."
            ),
            "allowed": [
                "punctuation and capitalization",
                "isolated filler removal",
                "immediate false-start removal",
                "evidence-backed caption repair",
                "spoken mathematics rendered in LaTeX",
                "explicit exclusion of logistics, nonspeech, unusable uncertainty, or outside-scope content",
            ],
            "prohibited": [
                "paraphrase",
                "summary substitution",
                "unstated mathematical completion",
                "silent omission",
            ],
        },
    }
    write_jsonl(OUTPUT, [metadata, *canonical])
    transcript_hash = sha256(OUTPUT)

    disposition_rows: list[dict[str, Any]] = []
    for row in canonical:
        scope = row["chapter_scope"]
        if scope == "next_chapter":
            chapter_use = "outside_section"
        elif scope in {"pre_core", "post_core"}:
            chapter_use = "coverage_only"
        elif row.get("cleaned_text") is None:
            chapter_use = "logistics_or_nonspeech_excluded"
        else:
            chapter_use = "pending_editorial_disposition"
        disposition_rows.append(
            {
                "record_type": "transcript_disposition",
                "schema_version": 2,
                "id": row["id"].replace("-T", "-TD"),
                "transcript_record_id": row["id"],
                "source_span_id": row["source_span_id"],
                "video_id": row["video_id"],
                "start": row["start"],
                "end": row["end"],
                "chapter_scope": scope,
                "chapter_use": chapter_use,
                "source_disposition": row.get("disposition"),
                "included_unit_ids": [],
                "reason": "Pass 2 literal-cleanup disposition; final chapter linkage is assigned in Pass 3.",
                "confidence": row.get("confidence"),
                "review_status": "pass2_complete_pending_pass3_linkage",
                "transcript_sha256": transcript_hash,
                "chapter_sha256": None,
            }
        )
    write_jsonl(DISPOSITIONS, disposition_rows)
    print(
        json.dumps(
            {
                "canonical_segments": len(canonical),
                "lane_count": len(lane_summaries),
                "scope_counts": counts,
                "transcript_sha256": transcript_hash,
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
