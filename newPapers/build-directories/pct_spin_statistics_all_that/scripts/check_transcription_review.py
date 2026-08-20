#!/usr/bin/env python3
"""Require an explicit review for every transcription-audit heading candidate."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

from audit_release_pipeline import review_provenance_failures


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_REPORT = ROOT / "work" / "reviews" / "transcription_audit.json"
DEFAULT_MANIFEST = ROOT / "work" / "reviews" / "transcription_audit_reviewed.json"
ALLOWED_CLASSES = {
    "title_metadata_master",
    "native_heading",
    "native_caption",
    "formula_ocr_noise",
    "bibliography_macro",
}


def load_json(path: Path, label: str, errors: list[str]) -> dict[str, Any] | None:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        errors.append(f"cannot read {label} {path}: {error}")
        return None
    if not isinstance(value, dict):
        errors.append(f"{label} must contain a JSON object: {path}")
        return None
    return value


def candidate_key(item: Any, label: str, index: int, errors: list[str]) -> tuple[int, str] | None:
    if not isinstance(item, dict):
        errors.append(f"{label}[{index}] is not an object")
        return None
    page = item.get("pdf_page")
    heading = item.get("heading")
    if not isinstance(page, int) or isinstance(page, bool) or page < 1:
        errors.append(f"{label}[{index}] has an invalid pdf_page")
        return None
    if not isinstance(heading, str) or not heading:
        errors.append(f"{label}[{index}] has an invalid heading")
        return None
    return page, heading


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--strict", action="store_true", help="require a complete reviewed candidate set")
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--report", type=Path, default=None)
    parser.add_argument("--manifest", type=Path, default=None)
    parser.add_argument("--provenance", type=Path, default=None)
    args = parser.parse_args(argv)

    root = args.root.resolve()
    report_path = (args.report or (root / "work" / "reviews" / "transcription_audit.json")).resolve()
    manifest_path = (args.manifest or (root / "work" / "reviews" / "transcription_audit_reviewed.json")).resolve()
    errors: list[str] = []
    provenance_path = (args.provenance or (root / "review-provenance.json")).resolve()
    errors.extend(
        review_provenance_failures(
            root=root,
            provenance_path=provenance_path,
            require_pdf=False,
        )
    )
    report = load_json(report_path, "audit report", errors)
    manifest = load_json(manifest_path, "review manifest", errors)
    if report is None or manifest is None:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    if args.strict:
        if report.get("mode") != "strict":
            errors.append(f"audit report mode is {report.get('mode')!r}; strict mode is required")
    if manifest.get("schema") != "pct-transcription-audit-reviewed/v1":
        errors.append("review manifest schema is not pct-transcription-audit-reviewed/v1")
    if manifest.get("status") != "reviewed":
        errors.append(f"review manifest status is {manifest.get('status')!r}; reviewed is required")
    if manifest.get("source_audit") != "work/reviews/transcription_audit.json":
        errors.append("review manifest source_audit must point to work/reviews/transcription_audit.json")

    report_candidates = report.get("findings", {}).get("missing_headings")
    manifest_candidates = manifest.get("candidates")
    if not isinstance(report_candidates, list):
        errors.append("audit report has no findings.missing_headings list")
        report_candidates = []
    if not isinstance(manifest_candidates, list):
        errors.append("review manifest has no candidates list")
        manifest_candidates = []

    report_keys: list[tuple[int, str]] = []
    for index, item in enumerate(report_candidates):
        key = candidate_key(item, "audit report candidates", index, errors)
        if key is not None:
            report_keys.append(key)
    manifest_keys: list[tuple[int, str]] = []
    for index, item in enumerate(manifest_candidates):
        key = candidate_key(item, "review manifest candidates", index, errors)
        if key is not None:
            manifest_keys.append(key)
        if isinstance(item, dict):
            if item.get("disposition") != "resolved":
                errors.append(f"review manifest candidate {index} is not resolved")
            if item.get("classification") not in ALLOWED_CLASSES:
                errors.append(f"review manifest candidate {index} has an unknown classification")
            if not isinstance(item.get("evidence"), str) or not item["evidence"].strip():
                errors.append(f"review manifest candidate {index} has no evidence field")

    expected_count = manifest.get("candidate_count")
    if expected_count != len(report_keys) or expected_count != len(manifest_keys):
        errors.append(
            f"candidate count mismatch: manifest declares {expected_count!r}, "
            f"audit has {len(report_keys)}, manifest has {len(manifest_keys)}"
        )
    if report_keys != manifest_keys:
        report_set = set(report_keys)
        manifest_set = set(manifest_keys)
        missing = sorted(report_set - manifest_set)
        extra = sorted(manifest_set - report_set)
        errors.append(f"reviewed candidate set differs from audit report; missing={missing!r}, extra={extra!r}")

    review_path_value = manifest.get("review_path")
    review_text: str | None = None
    if not isinstance(review_path_value, str) or not review_path_value:
        errors.append("review manifest has no review_path")
    else:
        review_path = (root / review_path_value).resolve()
        try:
            review_text = review_path.read_text(encoding="utf-8")
        except OSError as error:
            errors.append(f"cannot read review record {review_path}: {error}")
        else:
            if review_text.rstrip().splitlines()[-1:] != ["Unresolved blockers: none"]:
                errors.append("review record must end with 'Unresolved blockers: none'")

    if review_text is not None:
        for item in manifest_candidates:
            if not isinstance(item, dict):
                continue
            page = item.get("pdf_page")
            heading = item.get("heading")
            if isinstance(page, int) and isinstance(heading, str):
                needle = f"PDF {page:03d}, candidate `{heading}`"
                if needle not in review_text:
                    errors.append(f"review record has no entry for PDF {page:03d} candidate {heading!r}")

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print(f"Reviewed transcription candidates: {len(report_keys)}")
    print("RESULT: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
