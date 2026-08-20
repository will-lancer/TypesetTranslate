#!/usr/bin/env python3
"""Regenerate the source and review provenance record after a review pass."""

from __future__ import annotations

import argparse
import json
import os
import sys
import tempfile
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parent))
import audit_release_pipeline as audit  # noqa: E402


ROOT = Path(__file__).resolve().parents[1]


def current_provenance(root: Path = ROOT) -> tuple[dict[str, Any] | None, list[str]]:
    """Collect current hashes only when every provenance input is valid."""

    failures: list[str] = []
    source = audit._source_pdf_path(root)
    if not source.is_file() or source.is_symlink():
        failures.append(f"Missing canonical source PDF: {source}")
        source_sha256 = None
    else:
        source_sha256 = audit.sha256(source)
        if source_sha256 != audit.EXPECTED_SOURCE_SHA256:
            failures.append("canonical source SHA-256 differs from the frozen authority")

    native_sha256 = audit.native_input_hash(root)
    if native_sha256 is None:
        failures.append("native input set is incomplete")

    master = audit._master_pdf_path(root)
    if not master.is_file() or master.is_symlink() or master.stat().st_size == 0:
        failures.append("current latex/master.pdf is missing or empty")
        master_sha256 = None
    else:
        master_sha256 = audit.sha256(master)

    reviewer_map = root / "visual-reviewer-map.json"
    if not reviewer_map.is_file() or reviewer_map.is_symlink():
        failures.append("visual-reviewer-map.json is missing")
        reviewer_map_sha256 = None
    else:
        reviewer_map_sha256 = audit.sha256(reviewer_map)

    page_digest, page_failures, page_count = audit.source_page_hash(root)
    failures.extend(page_failures)
    if page_digest is None or page_count != audit.EXPECTED_SOURCE_PAGES:
        failures.append("source review image set is incomplete")
    failures.extend(audit.source_page_rerender_failures(root))

    inspection_path = root / "work" / "reviews" / "page-inspection.jsonl"
    inspections, inspection_failures = audit.read_jsonl(inspection_path)
    failures.extend(inspection_failures)
    if master_sha256 is not None:
        page_count_value = audit.pdf_page_count(master)
    else:
        page_count_value = None
    if page_count_value is None or page_count_value <= 0:
        failures.append("current master.pdf has no readable positive page count")
    else:
        failures.extend(
            audit.visual_reviewer_failures(
                set(range(1, page_count_value + 1)),
                inspections,
                root=root,
                mapping_path=reviewer_map,
            )
        )
    failures.extend(audit.review_pdf_hash_failures(root))

    review_paths = audit.review_record_paths(root)
    failures.extend(audit.required_review_record_failures(root))
    if not review_paths:
        failures.append("no review records are available")
    review_digest, review_missing = audit._aggregate_file_hash(root, review_paths)
    failures.extend(f"missing review record: {item}" for item in review_missing)

    if failures:
        return None, failures
    payload = {
        "schema_version": 1,
        "source_sha256": source_sha256,
        "native_input_sha256": native_sha256,
        "master_pdf_sha256": master_sha256,
        "visual_reviewer_map_sha256": reviewer_map_sha256,
        "source_pages": {
            **audit.SOURCE_PAGE_RENDER_SPEC,
            "source_sha256": source_sha256,
            "count": audit.EXPECTED_SOURCE_PAGES,
            "sha256": page_digest,
        },
        "review_records_sha256": review_digest,
    }
    return payload, []


def write_payload(output: Path, payload: dict[str, Any]) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    temporary_path: Path | None = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="w",
            encoding="utf-8",
            dir=output.parent,
            prefix=f".{output.name}.",
            suffix=".tmp",
            delete=False,
        ) as handle:
            temporary_path = Path(handle.name)
            json.dump(payload, handle, indent=2, sort_keys=False)
            handle.write("\n")
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary_path, output)
    finally:
        if temporary_path is not None and temporary_path.exists():
            temporary_path.unlink()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--output", type=Path, default=None)
    parser.add_argument("--check", action="store_true", help="validate inputs without writing the record")
    args = parser.parse_args(argv)

    root = args.root.resolve()
    output = (args.output or (root / "review-provenance.json")).resolve()
    payload, failures = current_provenance(root)
    if failures:
        print("REVIEW PROVENANCE GENERATION FAILED", file=sys.stderr)
        for failure in failures:
            print(f"  - {failure}", file=sys.stderr)
        return 1
    assert payload is not None
    if not args.check:
        write_payload(output, payload)
        print(f"Wrote review provenance: {output}")
    else:
        print("Review provenance inputs passed; no file written.")
    print(f"Source SHA-256: {payload['source_sha256']}")
    print(f"Native input SHA-256: {payload['native_input_sha256']}")
    print(f"Review records SHA-256: {payload['review_records_sha256']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
