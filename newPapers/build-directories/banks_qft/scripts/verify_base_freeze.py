#!/usr/bin/env python3
"""Require the rebuilt base edition to match its frozen release record."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
from pathlib import Path

try:
    from build_input_manifest import create_manifest, expected_compiled_inputs, validate_manifest
except ModuleNotFoundError:
    from scripts.build_input_manifest import create_manifest, expected_compiled_inputs, validate_manifest


ROOT = Path(__file__).resolve().parents[1]
EXPECTED_SOURCE_SHA256 = "31de7827e7bc636feaa7028fe4dbb63a718b3926ee43ff3d96d91185a44eafe3"
HEX64_RE = re.compile(r"^[0-9a-f]{64}$")
EXPECTED_AUDITS = {
    "source_identity": "pass",
    "page_dispositions": "281/281",
    "project_structure": "pass",
    "latex_diagnostics": "pass",
    "pdf_integrity_and_fonts": "pass",
    "reproducibility": "pass",
    "visual_review": "complete",
    "source_text_recall": "pass",
    "convention_audit": "pass",
}
EXPECTED_EVIDENCE_DOCUMENTS = (
    "AUTHORING_CONVENTIONS.md",
    "ERRATA.md",
    "NOTATION.md",
    "SOURCE_MANIFEST.yaml",
    "SOURCE_MAP.md",
    "TRANSCRIPTION_CONTRACT.md",
    "TRANSCRIPTION_STATUS.md",
    "explicit-problems.json",
    "figures.json",
    "implicit-exercises.json",
    "numbered-equations.json",
    "page-dispositions.jsonl",
    "query-ledger.json",
    "unnumbered-diagrams.json",
)
EXPECTED_RECORD_FIELDS = {
    "schema_version",
    "edition",
    "status",
    "source_sha256",
    "build_input_sha256",
    "output_sha256",
    "output_bytes",
    "page_count",
    "visual_review_pages",
    "render_manifest_sha256",
    "review_coverage_sha256",
    "solution_review_sha256",
    "source_render_sha256",
    "visual_review_sha256",
    "reproducibility_sha256",
    "text_recall_sha256",
    "convention_audit_sha256",
    "release_path",
    "byte_identical_to_compiled",
    "audits",
    "evidence_documents",
}
EXPECTED_EVIDENCE_ARTIFACTS = {
    "render_manifest_sha256": ROOT / "work" / "rendered-base" / "manifest.jsonl",
    "review_coverage_sha256": ROOT / "review-coverage-base.json",
    "solution_review_sha256": ROOT / "solution-review-base.json",
    "source_render_sha256": ROOT / "work" / "reviews" / "source-render-provenance.json",
    "visual_review_sha256": ROOT / "work" / "reviews" / "visual-review-base.json",
    "reproducibility_sha256": ROOT / "work" / "reviews" / "reproducibility-base.json",
    "text_recall_sha256": ROOT / "work" / "reviews" / "text-recall-base.json",
    "convention_audit_sha256": ROOT / "work" / "reviews" / "convention-audit-base.json",
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def page_count(pdf: Path) -> int:
    result = subprocess.run(["pdfinfo", str(pdf)], check=True, text=True, capture_output=True)
    for line in result.stdout.splitlines():
        if line.startswith("Pages:"):
            return int(line.split(":", 1)[1].strip())
    raise SystemExit(f"Could not read page count: {pdf}")


def valid_hash(value: object) -> bool:
    return isinstance(value, str) and HEX64_RE.fullmatch(value) is not None


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--pdf", type=Path, required=True)
    parser.add_argument("--fls", type=Path, required=True)
    parser.add_argument("--release-record", type=Path, required=True)
    args = parser.parse_args()
    try:
        frozen = json.loads(args.release_record.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise SystemExit(f"Cannot read frozen base release record: {error}") from error
    if not isinstance(frozen, dict):
        raise SystemExit("Frozen base release record must be a JSON object")
    missing = sorted(EXPECTED_RECORD_FIELDS - set(frozen))
    unexpected = sorted(set(frozen) - EXPECTED_RECORD_FIELDS)
    if missing or unexpected:
        details = []
        if missing:
            details.append(f"missing={missing}")
        if unexpected:
            details.append(f"unexpected={unexpected}")
        raise SystemExit("Frozen base release record schema mismatch: " + "; ".join(details))
    if frozen.get("schema_version") != 1:
        raise SystemExit("Frozen base release record schema_version must be 1")
    if frozen.get("edition") != "base" or frozen.get("status") != "pass":
        raise SystemExit("Frozen base release record is not a passing base record")
    if not valid_hash(frozen.get("source_sha256")):
        raise SystemExit("Frozen base release record has an invalid source hash")
    if frozen.get("source_sha256") != EXPECTED_SOURCE_SHA256:
        raise SystemExit("Frozen base release record source hash is not canonical")
    if not valid_hash(frozen.get("build_input_sha256")):
        raise SystemExit("Frozen base release record has an invalid build-input hash")
    if not valid_hash(frozen.get("output_sha256")):
        raise SystemExit("Frozen base release record has an invalid output hash")
    for field in (
        "render_manifest_sha256",
        "review_coverage_sha256",
        "source_render_sha256",
        "visual_review_sha256",
        "reproducibility_sha256",
        "text_recall_sha256",
        "convention_audit_sha256",
    ):
        if not valid_hash(frozen.get(field)):
            raise SystemExit(f"Frozen base release record has an invalid {field}")
    if not valid_hash(frozen.get("solution_review_sha256")):
        raise SystemExit("Frozen base release record has an invalid solution_review_sha256")
    for field in ("output_bytes", "page_count", "visual_review_pages"):
        if type(frozen.get(field)) is not int or frozen[field] <= 0:
            raise SystemExit(f"Frozen base release record has an invalid {field}")
    if frozen.get("visual_review_pages") != frozen.get("page_count"):
        raise SystemExit("Frozen base release record visual-review count differs from page count")
    if frozen.get("byte_identical_to_compiled") is not True:
        raise SystemExit("Frozen base release record does not assert byte identity")
    if frozen.get("audits") != EXPECTED_AUDITS:
        raise SystemExit("Frozen base release record audit summary is incomplete")
    evidence_documents = frozen.get("evidence_documents")
    if not isinstance(evidence_documents, dict) or set(evidence_documents) != set(EXPECTED_EVIDENCE_DOCUMENTS):
        raise SystemExit("Frozen base release record evidence-document map is incomplete")
    for name in EXPECTED_EVIDENCE_DOCUMENTS:
        digest = evidence_documents[name]
        evidence_path = (ROOT / name).resolve()
        if not valid_hash(digest) or not evidence_path.is_file() or sha256(evidence_path) != digest:
            raise SystemExit(f"Frozen base release evidence hash mismatch: {name}")
    for field, evidence_path in EXPECTED_EVIDENCE_ARTIFACTS.items():
        digest = frozen[field]
        if not evidence_path.is_file() or sha256(evidence_path) != digest:
            raise SystemExit(f"Frozen base release artifact hash mismatch: {field}")
    convention_path = EXPECTED_EVIDENCE_ARTIFACTS["convention_audit_sha256"]
    try:
        convention_audit = json.loads(convention_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise SystemExit(f"Cannot read frozen convention-audit evidence: {error}") from error
    if not isinstance(convention_audit, dict):
        raise SystemExit("Frozen convention-audit evidence must be a JSON object")
    if (
        convention_audit.get("schema_version") != 1
        or convention_audit.get("edition") != "base"
        or convention_audit.get("status") != "pass"
        or convention_audit.get("findings_count") != 0
        or not valid_hash(convention_audit.get("native_snapshot_sha256"))
        or type(convention_audit.get("reviewed_candidates_count")) is not int
        or convention_audit.get("reviewed_candidates_count") < 0
        or "conventions" not in convention_audit
    ):
        raise SystemExit("Frozen convention-audit evidence did not pass")
    try:
        frozen_source_review = json.loads(
            EXPECTED_EVIDENCE_ARTIFACTS["review_coverage_sha256"].read_text(encoding="utf-8")
        )
        frozen_solution_review = json.loads(
            EXPECTED_EVIDENCE_ARTIFACTS["solution_review_sha256"].read_text(encoding="utf-8")
        )
    except (OSError, json.JSONDecodeError) as error:
        raise SystemExit(f"Cannot read frozen review snapshots: {error}") from error
    if (
        not isinstance(frozen_source_review, dict)
        or not isinstance(frozen_solution_review, dict)
        or convention_audit.get("native_snapshot_sha256")
        != frozen_source_review.get("native_snapshot_sha256")
        or convention_audit.get("native_snapshot_sha256")
        != frozen_solution_review.get("native_snapshot_sha256")
    ):
        raise SystemExit("Frozen convention-audit snapshot differs from review snapshots")

    release = ROOT / ".." / ".." / "banks-qft" / "banks-qft-exercise-edition.pdf"
    release = release.resolve()
    try:
        recorded_release = Path(str(frozen["release_path"])).resolve()
    except (OSError, RuntimeError) as error:
        raise SystemExit(f"Frozen base release path is invalid: {error}") from error
    if recorded_release != release:
        raise SystemExit(f"Frozen base release path is not canonical: {recorded_release}")
    if release.is_symlink() or not release.is_file() or release.stat().st_size == 0:
        raise SystemExit(f"Frozen base release PDF is missing: {release}")
    if sha256(release) != frozen["output_sha256"]:
        raise SystemExit("Frozen base release PDF hash differs from its record")
    if release.stat().st_size != frozen["output_bytes"]:
        raise SystemExit("Frozen base release PDF byte count differs from its record")
    if page_count(release) != frozen["page_count"]:
        raise SystemExit("Frozen base release PDF page count differs from its record")

    current = create_manifest("base", args.fls, args.pdf)
    manifest_failures = validate_manifest(current, edition="base", pdf=args.pdf)
    if manifest_failures:
        raise SystemExit("\n".join(manifest_failures))
    current_paths = {str(item["path"]) for item in current["files"]}
    expected_paths = expected_compiled_inputs("base")
    if current_paths != expected_paths:
        missing = sorted(expected_paths - current_paths)
        unexpected = sorted(current_paths - expected_paths)
        raise SystemExit(
            "Rebuilt base compiled dependency closure differs from the frozen contract: "
            f"missing={missing}; unexpected={unexpected}"
        )
    if current["pdf_sha256"] != frozen.get("output_sha256"):
        raise SystemExit("Expanded-edition work changed the frozen base PDF")
    if current["build_input_sha256"] != frozen.get("build_input_sha256"):
        raise SystemExit("Expanded-edition work changed the frozen base input set")
    if args.pdf.stat().st_size != frozen["output_bytes"] or page_count(args.pdf) != frozen["page_count"]:
        raise SystemExit("Rebuilt base PDF metadata differs from the frozen record")
    if args.pdf.read_bytes() != release.read_bytes():
        raise SystemExit("Rebuilt base PDF differs byte-for-byte from the frozen release PDF")
    print("Frozen base PDF and build-input hash remain exact")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
