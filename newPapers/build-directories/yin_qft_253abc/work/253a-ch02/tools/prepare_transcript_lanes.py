#!/usr/bin/env python3
"""Prepare deterministic raw-caption packets for Chapter 2 Pass 2 lanes."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
WORK = ROOT / "work" / "253a-ch02"
CAPTIONS = WORK / "captions"
RAW_LANES = WORK / "raw-caption-lanes"
WINDOW_MS = 12 * 60 * 1000

VIDEOS = (
    ("96lN2omwit4", "2022-09-06", 5_412_000),
    ("uzixOflp0tY", "2022-09-08", 5_128_000),
    ("M0py5a4RWhE", "2022-09-13", 5_102_000),
    ("vk_RlYUKUyM", "2022-09-15", 5_007_000),
    ("3VG2kDHso08", "2022-09-20", 4_762_000),
    ("TtMNnZ8__UU", "2022-09-22", 4_796_000),
)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def timestamp(milliseconds: int) -> str:
    hours, remainder = divmod(milliseconds, 3_600_000)
    minutes, remainder = divmod(remainder, 60_000)
    seconds, millis = divmod(remainder, 1_000)
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}.{millis:03d}"


def compact_timestamp(milliseconds: int) -> str:
    hours, remainder = divmod(milliseconds, 3_600_000)
    minutes, remainder = divmod(remainder, 60_000)
    seconds = remainder // 1_000
    return f"{hours:02d}{minutes:02d}{seconds:02d}"


def caption_path(video_id: str, suffix: str) -> Path:
    matches = sorted(CAPTIONS.glob(f"*-{video_id}.en.{suffix}"))
    if len(matches) != 1:
        raise RuntimeError(
            f"expected one {suffix} caption file for {video_id}, found {matches}"
        )
    return matches[0]


def load_events(path: Path) -> list[dict[str, object]]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    source_events = payload.get("events")
    if not isinstance(source_events, list):
        raise RuntimeError(f"{path} has no JSON3 events array")

    events: list[dict[str, object]] = []
    for source_index, event in enumerate(source_events):
        if not isinstance(event, dict) or not isinstance(event.get("segs"), list):
            continue
        segments = event["segs"]
        text = "".join(
            segment.get("utf8", "")
            for segment in segments
            if isinstance(segment, dict)
        )
        if not text.strip():
            continue
        start_ms = int(event.get("tStartMs", 0))
        duration_ms = event.get("dDurationMs")
        duration_ms = int(duration_ms) if isinstance(duration_ms, (int, float)) else None
        words = []
        for segment in segments:
            if not isinstance(segment, dict):
                continue
            words.append(
                {
                    "utf8": segment.get("utf8", ""),
                    "offset_ms": int(segment.get("tOffsetMs", 0)),
                    "asr_confidence": segment.get("acAsrConf"),
                }
            )
        events.append(
            {
                "source_event_index": source_index,
                "start_ms": start_ms,
                "duration_ms": duration_ms,
                "text": text,
                "words": words,
            }
        )

    for index, event in enumerate(events):
        start_ms = int(event["start_ms"])
        duration_ms = event["duration_ms"]
        if isinstance(duration_ms, int) and duration_ms > 0:
            end_ms = start_ms + duration_ms
        elif index + 1 < len(events):
            end_ms = int(events[index + 1]["start_ms"])
        else:
            end_ms = start_ms + 1
        event["end_ms"] = max(end_ms, start_ms + 1)
    return events


def write_jsonl(path: Path, rows: list[dict[str, object]]) -> None:
    rendered = "".join(
        json.dumps(row, ensure_ascii=False, separators=(",", ":")) + "\n"
        for row in rows
    )
    path.write_text(rendered, encoding="utf-8")


def main() -> None:
    RAW_LANES.mkdir(parents=True, exist_ok=True)
    manifest: list[dict[str, object]] = []
    anthology = ["WEBVTT", "", "NOTE Chapter 2 raw-caption anthology.", ""]

    for chronology, (video_id, recorded_date, duration_ms) in enumerate(VIDEOS, 1):
        json3 = caption_path(video_id, "json3")
        vtt = caption_path(video_id, "vtt")
        events = load_events(json3)
        json3_hash = sha256(json3)
        vtt_hash = sha256(vtt)

        anthology.extend(
            [
                f"NOTE BEGIN VIDEO {chronology}: {video_id} ({recorded_date})",
                f"NOTE JSON3 SHA-256 {json3_hash}",
                f"NOTE VTT SHA-256 {vtt_hash}",
                "",
            ]
        )
        vtt_lines = vtt.read_text(encoding="utf-8").splitlines()
        if vtt_lines and vtt_lines[0].lstrip("\ufeff") == "WEBVTT":
            vtt_lines = vtt_lines[1:]
        anthology.extend(vtt_lines)
        anthology.extend(["", f"NOTE END VIDEO {video_id}", ""])

        for start_ms in range(0, duration_ms, WINDOW_MS):
            end_ms = min(start_ms + WINDOW_MS, duration_ms)
            lane_events = [
                event
                for event in events
                if start_ms <= int(event["start_ms"]) < end_ms
            ]
            lane_tag = (
                f"{video_id}-{compact_timestamp(start_ms)}-"
                f"{compact_timestamp(end_ms)}"
            )
            lane_rel = Path("work") / "253a-ch02" / "raw-caption-lanes" / f"{lane_tag}.jsonl"
            output_rel = Path("work") / "253a-ch02" / "cleaned-segments" / f"{lane_tag}.jsonl"
            metadata = {
                "record_type": "raw_lane_metadata",
                "schema_version": 1,
                "lane_id": lane_tag,
                "video_id": video_id,
                "recorded_date": recorded_date,
                "start": timestamp(start_ms),
                "end": timestamp(end_ms),
                "json3_source": str(json3.relative_to(ROOT)),
                "json3_sha256": json3_hash,
                "vtt_source": str(vtt.relative_to(ROOT)),
                "vtt_sha256": vtt_hash,
                "raw_event_count": len(lane_events),
                "expected_output": str(output_rel),
            }
            rows: list[dict[str, object]] = [metadata]
            for lane_index, event in enumerate(lane_events, 1):
                rows.append(
                    {
                        "record_type": "raw_caption_event",
                        "lane_id": lane_tag,
                        "lane_event_index": lane_index,
                        "source_event_index": event["source_event_index"],
                        "video_id": video_id,
                        "start": timestamp(int(event["start_ms"])),
                        "end": timestamp(int(event["end_ms"])),
                        "raw_text": event["text"],
                        "words": event["words"],
                    }
                )
            lane_path = ROOT / lane_rel
            write_jsonl(lane_path, rows)
            lane_hash = sha256(lane_path)
            manifest.append(
                {
                    **metadata,
                    "raw_lane_path": str(lane_rel),
                    "raw_lane_sha256": lane_hash,
                }
            )

    write_jsonl(WORK / "raw-caption-lane-manifest.jsonl", manifest)
    (WORK / "transcript.raw.vtt").write_text(
        "\n".join(anthology).rstrip() + "\n", encoding="utf-8"
    )
    print(
        json.dumps(
            {
                "lanes": len(manifest),
                "raw_events": sum(int(row["raw_event_count"]) for row in manifest),
                "transcript_raw_sha256": sha256(WORK / "transcript.raw.vtt"),
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
