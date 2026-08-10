#!/usr/bin/env python3
"""Freeze the audited Chapter 2 cleaned transcript and its source packet."""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
from typing import Any


ROOT = Path(__file__).resolve().parents[3]
WORK = ROOT / "work" / "253a-ch02"
MERGER = WORK / "tools" / "merge_cleaned_transcript.py"
TRANSCRIPT = WORK / "transcript.cleaned.jsonl"
DISPOSITIONS = WORK / "transcript-dispositions.jsonl"
PASS1_VALIDATION = WORK / "pass1-validation.json"
PASS1_MANIFEST = WORK / "source-packet-manifest.pass1.json"
PASS2_MANIFEST = WORK / "source-packet-manifest.pass2.json"
SOURCE_PACKET_MANIFEST = WORK / "source-packet-manifest.json"
PASS2_VALIDATION = WORK / "pass2-validation.json"

AUDITS = (
    WORK / "pass2-audits" / "audit-96-uz.md",
    WORK / "pass2-audits" / "audit-M0py5a4RWhE.md",
    WORK / "pass2-audits" / "audit-vk_RlYUKUyM.md",
    WORK / "pass2-audits" / "audit-3VG2kDHso08.md",
    WORK / "pass2-audits" / "audit-TtMNnZ8__UU.md",
    WORK / "pass2-audits" / "audit-global-mechanical.md",
    WORK / "pass2-audits" / "audit-global-semantic.md",
)

PASS2_INDEXES = (
    WORK / "pass2-voice-cues.jsonl",
    WORK / "pass2-equation-index.jsonl",
)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{rel(path)} must contain a JSON object")
    return value


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


def write_json(path: Path, value: dict[str, Any]) -> None:
    path.write_text(
        json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def rendered_json(value: dict[str, Any]) -> str:
    return json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n"


def entry(path: Path) -> dict[str, Any]:
    return {"path": rel(path), "bytes": path.stat().st_size, "sha256": sha256(path)}


def validate_pass1() -> None:
    validation = load_json(PASS1_VALIDATION)
    if validation.get("status") != "pass":
        raise ValueError("Pass 1 validation is not passing")
    expected = validation.get("source_packet_sha256")
    manifest = load_json(PASS1_MANIFEST)
    if manifest.get("source_packet_sha256") != expected:
        raise ValueError("Pass 1 source-packet digest disagrees with Pass 1 validation")


def validate_audits() -> None:
    missing = [rel(path) for path in AUDITS if not path.is_file()]
    if missing:
        raise ValueError(f"missing Pass 2 audits: {missing}")
    for path in AUDITS:
        lines = path.read_text(encoding="utf-8").rstrip().splitlines()
        if not lines or lines[-1] != "Unresolved blockers: none":
            raise ValueError(f"{rel(path)} does not end with the zero-blocker line")
    missing_indexes = [rel(path) for path in PASS2_INDEXES if not path.is_file()]
    if missing_indexes:
        raise ValueError(f"missing Pass 2 indexes: {missing_indexes}")
    for path in PASS2_INDEXES:
        if not load_jsonl(path):
            raise ValueError(f"{rel(path)} is empty")


def validate_transcript() -> dict[str, Any]:
    transcript_rows = load_jsonl(TRANSCRIPT)
    if not transcript_rows or transcript_rows[0].get("record_type") != "transcript_metadata":
        raise ValueError("cleaned transcript lacks its leading metadata record")
    metadata = transcript_rows[0]
    segments = transcript_rows[1:]
    if any(row.get("record_type") != "transcript_segment" for row in segments):
        raise ValueError("cleaned transcript contains a non-segment body record")
    expected_ids = [f"YIN253A-C02-T{index:06d}" for index in range(1, len(segments) + 1)]
    actual_ids = [row.get("id") for row in segments]
    if actual_ids != expected_ids:
        raise ValueError("cleaned transcript IDs are not contiguous in canonical order")
    source_span_ids = [row.get("source_span_id") for row in segments]
    if len(set(source_span_ids)) != len(source_span_ids) or any(
        not isinstance(value, str) or not value.startswith("YIN253A-C02-V-T")
        for value in source_span_ids
    ):
        raise ValueError("cleaned transcript source-span IDs are missing or duplicated")
    if any(row.get("chapter_scope") == "boundary_overlap" for row in segments):
        raise ValueError("cleaned transcript retains a boundary-overlap scope")
    if metadata.get("counts", {}).get("raw_event_count") != 9693:
        raise ValueError("cleaned transcript does not account for all 9,693 raw events")

    dispositions = load_jsonl(DISPOSITIONS)
    by_transcript = {row.get("transcript_record_id"): row for row in dispositions}
    if len(dispositions) != len(segments) or len(by_transcript) != len(segments):
        raise ValueError("transcript dispositions are not one-to-one with cleaned segments")
    for segment in segments:
        disposition = by_transcript.get(segment["id"])
        if disposition is None:
            raise ValueError(f"missing disposition for {segment['id']}")
        for field in ("source_span_id", "video_id", "start", "end", "chapter_scope"):
            if disposition.get(field) != segment.get(field):
                raise ValueError(f"disposition mismatch for {segment['id']} field {field}")

    return {
        "canonical_segment_count": len(segments),
        "raw_event_count": metadata["counts"]["raw_event_count"],
        "scope_counts": metadata["counts"]["scope_counts"],
        "transcript_sha256": sha256(TRANSCRIPT),
        "dispositions_sha256": sha256(DISPOSITIONS),
    }


def validate_merge_is_current() -> None:
    spec = importlib.util.spec_from_file_location("chapter02_pass2_merger", MERGER)
    if spec is None or spec.loader is None:
        raise ValueError("could not load the Pass 2 merger")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    with tempfile.TemporaryDirectory(prefix="yin-ch02-pass2-check-") as directory:
        temporary = Path(directory)
        module.OUTPUT = temporary / "transcript.cleaned.jsonl"
        module.DISPOSITIONS = temporary / "transcript-dispositions.jsonl"
        module.main()
        if module.OUTPUT.read_bytes() != TRANSCRIPT.read_bytes():
            raise ValueError("transcript.cleaned.jsonl is stale relative to cleaned lanes")
        if module.DISPOSITIONS.read_bytes() != DISPOSITIONS.read_bytes():
            raise ValueError("transcript-dispositions.jsonl is stale relative to cleaned lanes")


def build_manifest() -> dict[str, Any]:
    paths = [
        ROOT / "AGENT_POLICY.md",
        ROOT / "CHAPTER_PLAN.md",
        ROOT / "MASTER_PROMPT.md",
        ROOT / "SOURCE_MANIFEST.yaml",
        ROOT / "WORKFLOW.md",
        ROOT / "WRITING_STYLE.md",
        PASS1_MANIFEST,
        WORK / "alignment.jsonl",
        WORK / "ambiguities.md",
        WORK / "chapter-metadata.json",
        WORK / "notes-exact.tex",
        WORK / "page-dispositions.jsonl",
        WORK / "source-map.md",
        WORK / "transcript.raw.vtt",
        WORK / "raw-caption-lane-manifest.jsonl",
        MERGER,
        TRANSCRIPT,
        *AUDITS,
        *PASS2_INDEXES,
    ]
    paths.extend(sorted((WORK / "cleaned-segments").glob("*.jsonl")))
    entries = [entry(path) for path in sorted(paths, key=rel)]
    digest_payload = json.dumps(entries, ensure_ascii=False, separators=(",", ":"), sort_keys=True)
    manifest = {
        "record_type": "source_packet_manifest",
        "schema_version": 2,
        "chapter_id": "253a-ch02",
        "pass": 2,
        "status": "frozen",
        "entry_count": len(entries),
        "entries": entries,
        "source_packet_sha256": hashlib.sha256(digest_payload.encode("utf-8")).hexdigest(),
    }
    return manifest


def main() -> None:
    parser = argparse.ArgumentParser()
    action = parser.add_mutually_exclusive_group(required=True)
    action.add_argument("--write", action="store_true")
    action.add_argument("--check", action="store_true")
    args = parser.parse_args()
    validate_pass1()
    if args.write:
        subprocess.run([sys.executable, str(MERGER)], cwd=ROOT, check=True)
    else:
        validate_merge_is_current()
    validate_audits()
    transcript_stats = validate_transcript()
    manifest = build_manifest()
    validation = {
        "record_type": "pass2_validation",
        "schema_version": 2,
        "chapter_id": "253a-ch02",
        "status": "pass",
        "audit_count": len(AUDITS),
        "source_packet_manifest": rel(SOURCE_PACKET_MANIFEST),
        "source_packet_sha256": manifest["source_packet_sha256"],
        **transcript_stats,
    }
    if args.write:
        write_json(PASS2_MANIFEST, manifest)
        write_json(SOURCE_PACKET_MANIFEST, manifest)
        write_json(PASS2_VALIDATION, validation)
    else:
        expected_manifest = rendered_json(manifest)
        for path in (PASS2_MANIFEST, SOURCE_PACKET_MANIFEST):
            if not path.is_file() or path.read_text(encoding="utf-8") != expected_manifest:
                raise ValueError(f"{rel(path)} is stale")
        expected_validation = rendered_json(validation)
        if (
            not PASS2_VALIDATION.is_file()
            or PASS2_VALIDATION.read_text(encoding="utf-8") != expected_validation
        ):
            raise ValueError(f"{rel(PASS2_VALIDATION)} is stale")
    if sha256(PASS2_MANIFEST) != sha256(SOURCE_PACKET_MANIFEST):
        raise ValueError("canonical and Pass 2 source-packet manifests differ")
    print(json.dumps(validation, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
