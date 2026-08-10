#!/usr/bin/env python3
"""Assemble and freeze the Chapter 2 Pass 1 source packet."""

from __future__ import annotations

import hashlib
import json
import re
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
WORK = ROOT / "work/253a-ch02"
SYNTH = WORK / "synthesis-lanes"
BOUNDARY_RE = re.compile(r"\\YinPageBoundary\{(\d+)\}\{(\d+)\}")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def read_jsonl(path: Path) -> list[dict]:
    records: list[dict] = []
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            records.append(json.loads(line))
        except json.JSONDecodeError as exc:
            raise SystemExit(f"{path}:{line_number}: invalid JSON: {exc}") from exc
    return records


def write_json(path: Path, value: object) -> None:
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def write_jsonl(path: Path, records: list[dict]) -> None:
    path.write_text(
        "".join(json.dumps(record, separators=(",", ":"), ensure_ascii=False) + "\n" for record in records),
        encoding="utf-8",
    )


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(message)


def validate_status(path: Path, expected_count: int) -> None:
    lines = [line for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]
    require(len(lines) == expected_count, f"{path}: expected {expected_count} status rows, found {len(lines)}")
    failures = [line for line in lines if not line.endswith("\tcomplete")]
    require(not failures, f"{path}: failed lanes: {failures}")


def assemble_notes() -> tuple[Path, Path]:
    first = SYNTH / "notes-exact-a.tex"
    candidates = [SYNTH / "notes-exact-b.tex", SYNTH / "notes-exact-b-alt.tex"]
    second = next((path for path in candidates if path.exists()), None)
    require(first.exists(), f"missing {first}")
    require(second is not None, "neither notes-exact-b.tex nor notes-exact-b-alt.tex exists")

    first_text = first.read_text(encoding="utf-8")
    second_text = second.read_text(encoding="utf-8")
    first_pairs = [(int(a), int(b)) for a, b in BOUNDARY_RE.findall(first_text)]
    second_pairs = [(int(a), int(b)) for a, b in BOUNDARY_RE.findall(second_text)]
    require(first_pairs == [(page, page + 11) for page in range(10, 30)], f"bad A page boundaries: {first_pairs}")
    require(second_pairs == [(page, page + 11) for page in range(30, 52)], f"bad B page boundaries: {second_pairs}")

    marker = "\\YinPageBoundary{30}{41}"
    start = second_text.find(marker)
    require(start >= 0, f"{second}: missing first page marker")
    output = WORK / "notes-exact.tex"
    generated_note = (
        "\n% ---------------------------------------------------------------------------\n"
        f"% PASS-1-MERGE: second half from {second.relative_to(ROOT)}.\n"
    )
    output.write_text(first_text.rstrip() + generated_note + second_text[start:].lstrip(), encoding="utf-8")
    combined_pairs = [(int(a), int(b)) for a, b in BOUNDARY_RE.findall(output.read_text(encoding="utf-8"))]
    require(combined_pairs == [(page, page + 11) for page in range(10, 52)], "combined note boundaries are incomplete")
    return output, second


def assemble_page_dispositions() -> Path:
    source = SYNTH / "page-dispositions.jsonl"
    records = read_jsonl(source)
    require(len(records) == 42, f"{source}: expected 42 records")
    expected_ids = [f"YIN253A-C02-PD{page:03d}" for page in range(10, 52)]
    require([record.get("id") for record in records] == expected_ids, "note page disposition IDs are incomplete or unordered")
    require([record.get("pdf_page") for record in records] == list(range(21, 63)), "note page disposition PDF pages are incomplete")

    divider = {
        "id": "YIN253A-C02-PD000",
        "note_page": None,
        "pdf_page": 20,
        "page_kind": "chapter_divider",
        "disposition": "included_structural_boundary",
        "retained_elements": [
            "chapter number 2",
            "title Lagrangian Quantum Mechanics, Path Integrals, and Perturbation Theory",
            "divider establishes the lower physical-page boundary for the chapter",
        ],
        "normalized_elements": ["divider title represented by the canonical LaTeX chapter heading"],
        "omitted_elements": ["source divider typography omitted as source-page facsimile styling"],
        "unresolved_elements": [],
        "reason": "Physical page 20 is the Chapter 2 divider and contains no handwritten note-page number.",
        "confidence": 1.0,
        "review_status": "reviewed_against_rendered_note",
        "included_unit_ids": [],
        "normalized_unit_ids": [],
    }
    output = WORK / "page-dispositions.jsonl"
    write_jsonl(output, [divider, *records])
    return output


def validate_metadata() -> dict:
    path = WORK / "chapter-metadata.json"
    metadata = json.loads(path.read_text(encoding="utf-8"))
    require(metadata.get("schema_version") == 2, "chapter metadata schema must be 2")
    require(metadata.get("chapter_id") == "253a-ch02", "wrong chapter_id")
    page_map = metadata.get("page_map", [])
    require([row.get("pdf_page") for row in page_map] == list(range(20, 63)), "metadata physical-page map must be 20-62")
    require(page_map[0].get("note_page") is None, "physical page 20 must have no note-page number")
    require([row.get("note_page") for row in page_map[1:]] == list(range(10, 52)), "metadata note-page map must be 10-51")
    require(metadata.get("excluded_assignment_pages", {}).get("physical_pdf_pages") == [63, 67], "assignment pages must be 63-67")
    require(metadata.get("next_chapter_boundary", {}).get("physical_pdf_page") == 68, "next chapter boundary must be physical page 68")

    expected_videos = ["96lN2omwit4", "uzixOflp0tY", "M0py5a4RWhE", "vk_RlYUKUyM", "3VG2kDHso08", "TtMNnZ8__UU"]
    intervals = metadata.get("chapter_intervals", [])
    require([row.get("video_id") for row in intervals] == expected_videos, "chapter video chronology mismatch")
    require(intervals[0].get("core_start") == "00:01:26.700", "Chapter 2 opening timestamp mismatch")
    require(intervals[-1].get("core_end") == "00:51:10.020", "Chapter 2 closing timestamp mismatch")
    require(metadata.get("endpoint_convention") == "[start,end)", "endpoint convention mismatch")

    for source in metadata.get("raw_sources", []):
        source_path = ROOT / source["path"]
        require(source_path.exists(), f"missing raw source {source_path}")
        require(source_path.stat().st_size == source["bytes"], f"size mismatch for {source_path}")
        require(sha256(source_path) == source["sha256"], f"hash mismatch for {source_path}")
    return metadata


def validate_raw_lanes(metadata: dict) -> None:
    records = read_jsonl(WORK / "raw-caption-lane-manifest.jsonl")
    require(len(records) == 45, f"expected 45 raw caption lanes, found {len(records)}")
    expected_videos = [row["video_id"] for row in metadata["chapter_intervals"]]
    require(sorted({row["video_id"] for row in records}) == sorted(expected_videos), "raw lanes contain the wrong videos")
    lane_ids = [row["lane_id"] for row in records]
    require(len(lane_ids) == len(set(lane_ids)), "duplicate raw caption lane IDs")
    total_events = 0
    for record in records:
        lane_path = ROOT / record["raw_lane_path"]
        require(lane_path.exists(), f"missing raw lane {lane_path}")
        require(sha256(lane_path) == record["raw_lane_sha256"], f"raw lane hash mismatch: {lane_path}")
        lane_records = read_jsonl(lane_path)
        require(len(lane_records) == record["raw_event_count"] + 1, f"raw event count mismatch: {lane_path}")
        total_events += record["raw_event_count"]
    require(total_events == 9693, f"expected 9693 raw caption events, found {total_events}")


def freeze_manifest(notes_path: Path, second_half: Path, page_dispositions: Path) -> Path:
    required = [
        ROOT / "SOURCE_MANIFEST.yaml",
        ROOT / "AGENT_POLICY.md",
        ROOT / "WRITING_STYLE.md",
        ROOT / "WORKFLOW.md",
        ROOT / "CHAPTER_PLAN.md",
        ROOT / "MASTER_PROMPT.md",
        WORK / "source-map.md",
        WORK / "chapter-metadata.json",
        WORK / "playlist.jsonl",
        WORK / "alignment.jsonl",
        notes_path,
        WORK / "ambiguities.md",
        page_dispositions,
        WORK / "transcript.raw.vtt",
        WORK / "raw-caption-lane-manifest.jsonl",
        WORK / "pass1-coverage-audit.md",
    ]
    required.extend(sorted((WORK / "source-lanes").glob("*.md")))
    required.extend(sorted((WORK / "captions").glob("*")))
    required.extend(sorted((WORK / "raw-caption-lanes").glob("*.jsonl")))
    require(all(path.is_file() for path in required), "Pass 1 manifest has a missing required file")
    unique = sorted(set(required), key=lambda path: str(path.relative_to(ROOT)))
    entries = [
        {
            "path": str(path.relative_to(ROOT)),
            "sha256": sha256(path),
            "bytes": path.stat().st_size,
        }
        for path in unique
    ]
    packet_basis = json.dumps(entries, separators=(",", ":"), sort_keys=True).encode("utf-8")
    manifest = {
        "record_type": "source_packet_manifest",
        "schema_version": 2,
        "chapter_id": "253a-ch02",
        "pass": 1,
        "status": "frozen",
        "notes_second_half_selected": str(second_half.relative_to(ROOT)),
        "entry_count": len(entries),
        "source_packet_sha256": hashlib.sha256(packet_basis).hexdigest(),
        "entries": entries,
    }
    output = WORK / "source-packet-manifest.pass1.json"
    write_json(output, manifest)
    return output


def main() -> None:
    validate_status(WORK / "agent-logs/pass1/status.tsv", 31)
    notes_path, second_half = assemble_notes()
    ambiguities = WORK / "ambiguities.md"
    shutil.copyfile(SYNTH / "notes-ambiguities.md", ambiguities)
    page_dispositions = assemble_page_dispositions()
    metadata = validate_metadata()
    validate_raw_lanes(metadata)

    transcript_raw = WORK / "transcript.raw.vtt"
    require(sha256(transcript_raw) == "b74eced69262827b17a84ab03e00049f82d1b1b14869f624f6df4bd6b6d8fbbe", "raw transcript hash mismatch")
    audit = WORK / "pass1-coverage-audit.md"
    require(audit.exists(), "independent Pass 1 coverage audit is not complete")
    require("Unresolved blockers: none" in audit.read_text(encoding="utf-8"), "Pass 1 coverage audit has blockers")

    metadata["pass1_review_status"] = "frozen"
    metadata["notes_exact_path"] = "work/253a-ch02/notes-exact.tex"
    metadata["page_dispositions_path"] = "work/253a-ch02/page-dispositions.jsonl"
    metadata["raw_transcript_path"] = "work/253a-ch02/transcript.raw.vtt"
    write_json(WORK / "chapter-metadata.json", metadata)

    manifest = freeze_manifest(notes_path, second_half, page_dispositions)
    validation = {
        "record_type": "pass1_validation",
        "schema_version": 1,
        "chapter_id": "253a-ch02",
        "status": "pass",
        "physical_pages": [20, 62],
        "note_pages": [10, 51],
        "page_disposition_count": 43,
        "note_boundary_count": 42,
        "chapter_video_count": 6,
        "raw_caption_lane_count": 45,
        "raw_caption_event_count": 9693,
        "chapter_start": {"video_id": "96lN2omwit4", "timestamp": "00:01:26.700"},
        "chapter_end": {"video_id": "TtMNnZ8__UU", "timestamp": "00:51:10.020", "endpoint": "exclusive"},
        "source_packet_manifest": str(manifest.relative_to(ROOT)),
        "source_packet_sha256": json.loads(manifest.read_text(encoding="utf-8"))["source_packet_sha256"],
    }
    write_json(WORK / "pass1-validation.json", validation)
    print(json.dumps(validation, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
