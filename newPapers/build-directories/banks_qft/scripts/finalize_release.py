#!/usr/bin/env python3
"""Stage an audited PDF, verify byte identity, and write release evidence."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import subprocess
import tempfile
from pathlib import Path

from audit_project import native_snapshot_sha256


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "banks-qft.pdf"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def pages(pdf: Path) -> int:
    result = subprocess.run(["pdfinfo", str(pdf)], check=True, text=True, capture_output=True)
    for line in result.stdout.splitlines():
        if line.startswith("Pages:"):
            return int(line.split(":", 1)[1].strip())
    raise SystemExit(f"Could not read page count: {pdf}")


def load(path: Path) -> dict[str, object]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise SystemExit(f"Expected JSON object: {path}")
    return value


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--edition", choices=("base", "implicit"), required=True)
    parser.add_argument("--compiled", type=Path, required=True)
    parser.add_argument("--release", type=Path, required=True)
    parser.add_argument("--input-manifest", type=Path, required=True)
    parser.add_argument("--reproducibility", type=Path, required=True)
    parser.add_argument("--render-manifest", type=Path, required=True)
    parser.add_argument("--review-coverage", type=Path, required=True)
    parser.add_argument("--solution-review", type=Path, required=True)
    parser.add_argument("--source-render", type=Path, required=True)
    parser.add_argument("--visual-review", type=Path, required=True)
    parser.add_argument("--text-recall", type=Path, required=True)
    parser.add_argument("--convention-audit", type=Path, required=True)
    parser.add_argument("--output-record", type=Path, required=True)
    args = parser.parse_args()
    compiled_hash = sha256(args.compiled)
    source_hash = sha256(SOURCE)
    if source_hash != "31de7827e7bc636feaa7028fe4dbb63a718b3926ee43ff3d96d91185a44eafe3":
        raise SystemExit("Canonical source hash changed")
    input_manifest = load(args.input_manifest)
    reproducibility = load(args.reproducibility)
    review_coverage = load(args.review_coverage)
    solution_review = load(args.solution_review)
    source_render = load(args.source_render)
    visual_review = load(args.visual_review)
    text_recall = load(args.text_recall)
    convention_audit = load(args.convention_audit)
    if input_manifest.get("edition") != args.edition or input_manifest.get("pdf_sha256") != compiled_hash:
        raise SystemExit("Build-input manifest does not bind the compiled PDF")
    if reproducibility.get("status") != "pass" or reproducibility.get("pdf_sha256") != compiled_hash:
        raise SystemExit("Reproducibility evidence does not bind the compiled PDF")
    snapshot = native_snapshot_sha256(args.edition)
    if (
        review_coverage.get("edition") != args.edition
        or review_coverage.get("status") != "pass"
        or review_coverage.get("native_snapshot_sha256") != snapshot
    ):
        raise SystemExit("Source-review coverage belongs to another edition")
    if (
        solution_review.get("edition") != args.edition
        or solution_review.get("status") != "pass"
        or solution_review.get("native_snapshot_sha256") != snapshot
    ):
        raise SystemExit("Solution-review evidence does not bind this edition")
    if (
        source_render.get("schema_version") != 1
        or source_render.get("status") != "pass"
        or source_render.get("source_sha256") != source_hash
        or source_render.get("source_pages") != 281
        or source_render.get("render_count") != 281
        or source_render.get("render_dpi") != 150
        or source_render.get("render_box") != "cropbox"
    ):
        raise SystemExit("Source-render provenance evidence did not pass")
    if (
        visual_review.get("status") != "pass"
        or visual_review.get("pdf_sha256") != compiled_hash
        or len(set(visual_review.get("reviewers", []))) < 3
    ):
        raise SystemExit("Visual-review evidence does not bind the compiled PDF")
    if (
        text_recall.get("schema_version") != 2
        or text_recall.get("edition") != args.edition
        or text_recall.get("status") != "pass"
        or text_recall.get("source_sha256") != source_hash
        or text_recall.get("output_sha256") != compiled_hash
    ):
        raise SystemExit("Text-recall evidence did not pass for this edition")
    if (
        convention_audit.get("schema_version") != 1
        or convention_audit.get("edition") != args.edition
        or convention_audit.get("status") != "pass"
        or convention_audit.get("native_snapshot_sha256") != snapshot
        or convention_audit.get("findings_count") != 0
        or type(convention_audit.get("reviewed_candidates_count")) is not int
        or convention_audit.get("reviewed_candidates_count") < 0
        or "conventions" not in convention_audit
    ):
        raise SystemExit("Convention-audit evidence did not pass for this edition")
    args.release.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary_name = tempfile.mkstemp(prefix=f".{args.release.name}.", dir=args.release.parent)
    os.close(descriptor)
    temporary = Path(temporary_name)
    try:
        shutil.copyfile(args.compiled, temporary)
        if sha256(temporary) != compiled_hash:
            raise SystemExit("Staged release bytes differ from compiled PDF")
        os.replace(temporary, args.release)
    finally:
        if temporary.exists():
            temporary.unlink()
    if sha256(args.release) != compiled_hash or args.release.read_bytes() != args.compiled.read_bytes():
        raise SystemExit("Release copy failed byte-identity verification")
    record = {
        "schema_version": 1,
        "edition": args.edition,
        "status": "pass",
        "source_sha256": source_hash,
        "build_input_sha256": input_manifest["build_input_sha256"],
        "output_sha256": compiled_hash,
        "output_bytes": args.release.stat().st_size,
        "page_count": pages(args.release),
        "visual_review_pages": visual_review["pages_reviewed"],
        "render_manifest_sha256": sha256(args.render_manifest),
        "review_coverage_sha256": sha256(args.review_coverage),
        "solution_review_sha256": sha256(args.solution_review),
        "source_render_sha256": sha256(args.source_render),
        "visual_review_sha256": sha256(args.visual_review),
        "reproducibility_sha256": sha256(args.reproducibility),
        "text_recall_sha256": sha256(args.text_recall),
        "convention_audit_sha256": sha256(args.convention_audit),
        "release_path": str(args.release.resolve()),
        "byte_identical_to_compiled": True,
        "audits": {
            "source_identity": "pass",
            "page_dispositions": "281/281",
            "project_structure": "pass",
            "latex_diagnostics": "pass",
            "pdf_integrity_and_fonts": "pass",
            "reproducibility": "pass",
            "visual_review": "complete",
            "source_text_recall": "pass",
            "convention_audit": "pass",
        },
        "evidence_documents": {
            name: sha256(ROOT / name)
            for name in (
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
        },
    }
    args.output_record.parent.mkdir(parents=True, exist_ok=True)
    encoded = json.dumps(record, indent=2, sort_keys=True) + "\n"
    args.output_record.write_text(encoded, encoding="utf-8")
    if args.edition == "base":
        freeze = ROOT / "work" / "reviews" / "base-freeze.json"
        freeze.parent.mkdir(parents=True, exist_ok=True)
        freeze.write_text(encoded, encoding="utf-8")
    print(f"Release finalized: {args.release}")
    print(f"SHA-256: {compiled_hash}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
