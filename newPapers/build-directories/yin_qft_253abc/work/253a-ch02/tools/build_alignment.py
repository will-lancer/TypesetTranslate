#!/usr/bin/env python3
"""Render the reconciled Chapter 2 lecture and page alignment."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
WORK = ROOT / "work" / "253a-ch02"


def main() -> None:
    metadata = json.loads((WORK / "chapter-metadata.json").read_text(encoding="utf-8"))
    playlist_rows = [
        json.loads(line)
        for line in (WORK / "playlist.jsonl").read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    rows: list[dict[str, object]] = [
        {
            "record_type": "alignment_metadata",
            "schema_version": 2,
            "chapter_id": metadata["chapter_id"],
            "playlist_id": "PLAd5nTR2YCdoAkJnywB0B9f8cghPSLM9m",
            "note_pages": [10, 51],
            "pdf_pages": [20, 62],
            "video_order": metadata["video_order"],
            "chapter_intervals": metadata["chapter_intervals"],
            "endpoint_convention": "[start,end)",
            "method": [
                "recording-date chronology",
                "complete JSON3 and VTT caption tracks",
                "downloaded 640x360 source videos",
                "targeted opening and boundary frames",
                "rendered handwritten note pages",
                "adjacent-lecture transition language",
            ],
            "confidence": 0.99,
        },
        {
            "record_type": "structural_alignment",
            "id": "YIN253A-C02-AL000",
            "page_kind": "chapter_divider",
            "note_pages": [],
            "pdf_pages": [20],
            "title": metadata["title"],
            "video_id": "96lN2omwit4",
            "start": "00:01:26.700",
            "end": "00:02:13.319",
            "evidence": "spoken chapter announcement and board title",
            "confidence": 0.99,
        },
    ]

    for interval in metadata["chapter_intervals"]:
        order = int(interval["order"])
        note_start, note_end = interval["note_pages"]
        pdf_start, pdf_end = interval["pdf_pages"]
        rows.append(
            {
                "record_type": "alignment",
                "schema_version": 2,
                "id": f"YIN253A-C02-AL{order:03d}",
                "video_id": interval["video_id"],
                "start": interval["core_start"],
                "end": interval["core_end"],
                "note_pages": list(range(int(note_start), int(note_end) + 1)),
                "pdf_pages": list(range(int(pdf_start), int(pdf_end) + 1)),
                "alignment_kind": "chapter_lecture_span",
                "source_report": f"work/253a-ch02/source-lanes/video-{interval['video_id']}.md",
                "disposition": "included",
                "confidence": 0.98,
            }
        )

    rows.append(
        {
            "record_type": "boundary_alignment",
            "schema_version": 2,
            "id": "YIN253A-C02-AL068",
            "video_id": "TtMNnZ8__UU",
            "start": "00:50:22.579",
            "end": "00:51:15.660",
            "note_pages": [51],
            "pdf_pages": [62, 68],
            "chapter2_half_open_end": "00:51:10.020",
            "disposition": "chapter2_close_and_chapter3_boundary_evidence",
            "confidence": 0.99,
        }
    )

    for row in playlist_rows[1:]:
        rows.append(
            {
                "record_type": "video_examined",
                "video_id": row["video_id"],
                "title": row["title"],
                "recorded_at_utc": row["recorded_at_utc"],
                "playlist_position": row["playlist_position"],
                "duration_seconds_playlist": row["duration_seconds"],
                "chapter_role": row["chapter_role"],
                "examined": "complete JSON3 and VTT tracks; complete downloaded video; targeted frames where the boundary required them",
                "raw_sources": row["raw_sources"],
                "confidence": 1.0,
            }
        )

    rendered = "".join(
        json.dumps(row, ensure_ascii=False, separators=(",", ":")) + "\n"
        for row in rows
    )
    (WORK / "alignment.jsonl").write_text(rendered, encoding="utf-8")
    print(json.dumps({"alignment_records": len(rows)}, indent=2))


if __name__ == "__main__":
    main()
