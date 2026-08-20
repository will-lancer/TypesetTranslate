#!/usr/bin/env python3
"""Validate and merge page-inspection JSONL parts into one release manifest.

Reviewers write one JSONL file per page range under
``work/reviews/page-inspection-parts``.  This helper checks every record
against the current rendered-page manifest and compiled PDF, then writes a
deterministically ordered ``page-inspection.jsonl``.  It requires the fields
checked by ``render_release_evidence.py`` and leaves the output untouched when
validation fails.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_PDF = ROOT / "latex" / "master.pdf"
DEFAULT_MANIFEST = ROOT / "work" / "rendered-output" / "manifest.jsonl"
DEFAULT_PARTS_DIR = ROOT / "work" / "reviews" / "page-inspection-parts"
DEFAULT_OUTPUT = ROOT / "work" / "reviews" / "page-inspection.jsonl"
PAGE_FILE_RE = re.compile(r"^page-(\d+)\.png$")
REQUIRED_FIELDS = (
    "pdf_page",
    "inspected",
    "rendered_sha256",
    "render_manifest_sha256",
    "pdf_sha256",
    "reviewer",
    "inspected_at",
    "observation",
)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def read_jsonl_with_lines(path: Path) -> list[tuple[int, dict[str, Any]]]:
    if not path.is_file():
        raise SystemExit(f"Missing JSONL file: {path}")
    records: list[tuple[int, dict[str, Any]]] = []
    for line_number, raw in enumerate(
        path.read_text(encoding="utf-8").splitlines(), 1
    ):
        if not raw.strip():
            continue
        try:
            record = json.loads(raw)
        except json.JSONDecodeError as error:
            raise SystemExit(f"{path}:{line_number}: invalid JSON: {error}") from error
        if not isinstance(record, dict):
            raise SystemExit(f"{path}:{line_number}: each record must be a JSON object")
        records.append((line_number, record))
    return records


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    return [record for _, record in read_jsonl_with_lines(path)]


def pdf_page_count(pdf: Path) -> int:
    if not pdf.is_file():
        raise SystemExit(f"Missing compiled PDF: {pdf}")
    try:
        result = subprocess.run(
            ["pdfinfo", str(pdf)], check=True, capture_output=True, text=True
        )
    except (OSError, subprocess.CalledProcessError) as error:
        raise SystemExit(f"Could not inspect PDF page count for {pdf}: {error}") from error
    match = re.search(r"^Pages:\s+(\d+)\s*$", result.stdout, re.MULTILINE)
    if match is None:
        raise SystemExit(f"Could not read page count from {pdf}")
    return int(match.group(1))


def read_render_manifest(manifest: Path) -> dict[int, dict[str, Any]]:
    records = read_jsonl(manifest)
    if not records:
        raise SystemExit(f"Rendered-page manifest is empty: {manifest}")
    pages: dict[int, dict[str, Any]] = {}
    for index, record in enumerate(records, 1):
        page = record.get("pdf_page")
        if isinstance(page, bool) or not isinstance(page, int):
            raise SystemExit(f"{manifest}:{index}: pdf_page must be an integer")
        if page in pages:
            raise SystemExit(f"{manifest}:{index}: duplicate PDF page {page}")
        filename = record.get("filename")
        if not isinstance(filename, str) or PAGE_FILE_RE.fullmatch(filename) is None:
            raise SystemExit(f"{manifest}:{index}: invalid rendered filename {filename!r}")
        rendered_hash = record.get("sha256")
        if not isinstance(rendered_hash, str) or not rendered_hash:
            raise SystemExit(f"{manifest}:{index}: missing rendered-page sha256")
        rendered_path = manifest.parent / filename
        if not rendered_path.is_file():
            raise SystemExit(f"{manifest}:{index}: missing rendered page {rendered_path}")
        if sha256(rendered_path) != rendered_hash:
            raise SystemExit(f"{manifest}:{index}: rendered checksum changed for {filename}")
        pages[page] = record

    expected = set(range(1, len(records) + 1))
    if set(pages) != expected:
        raise SystemExit(
            "Rendered-page manifest must contain one contiguous record for every "
            f"page: missing={sorted(expected - set(pages))}, "
            f"extra={sorted(set(pages) - expected)}"
        )
    return pages


def validate_and_merge(
    pdf: Path,
    manifest: Path,
    parts_dir: Path,
    output: Path,
) -> int:
    pages = read_render_manifest(manifest)
    manifest_hash = sha256(manifest)
    compiled_page_count = pdf_page_count(pdf)
    pdf_hash = sha256(pdf)
    if compiled_page_count != len(pages):
        raise SystemExit(
            "Compiled PDF and rendered-page manifest disagree: "
            f"pdf={compiled_page_count}, manifest={len(pages)}"
        )
    if not parts_dir.is_dir():
        raise SystemExit(f"Missing page-inspection parts directory: {parts_dir}")

    part_paths = sorted(parts_dir.glob("*.jsonl"))
    if output.resolve() in {path.resolve() for path in part_paths}:
        part_paths = [path for path in part_paths if path.resolve() != output.resolve()]
    if not part_paths:
        raise SystemExit(f"No page-inspection JSONL parts found in {parts_dir}")

    merged: dict[int, dict[str, Any]] = {}
    errors: list[str] = []
    for part_path in part_paths:
        try:
            records = read_jsonl_with_lines(part_path)
        except SystemExit as error:
            errors.append(str(error))
            continue
        for line_number, parsed in records:
            page = parsed.get("pdf_page")
            location = f"{part_path}:{line_number}"
            if isinstance(page, bool) or not isinstance(page, int):
                errors.append(f"{location}: pdf_page must be an integer")
                continue
            if page not in pages:
                errors.append(f"{location}: PDF page {page} is outside the rendered page set")
                continue
            if page in merged:
                errors.append(f"{location}: duplicate inspection record for PDF page {page}")
                continue
            missing = [field for field in REQUIRED_FIELDS if field not in parsed]
            if missing:
                errors.append(f"{location}: PDF page {page} lacks fields {missing}")
                continue
            if parsed["inspected"] is not True:
                errors.append(f"{location}: PDF page {page} must set inspected to true")
            expected_rendered_hash = pages[page]["sha256"]
            if parsed["rendered_sha256"] != expected_rendered_hash:
                errors.append(f"{location}: rendered checksum mismatch for PDF page {page}")
            if parsed["render_manifest_sha256"] != manifest_hash:
                errors.append(
                    f"{location}: render-manifest checksum mismatch for PDF page {page}"
                )
            if parsed["pdf_sha256"] != pdf_hash:
                errors.append(f"{location}: compiled-PDF checksum mismatch for PDF page {page}")
            for field in ("rendered_sha256", "render_manifest_sha256", "pdf_sha256"):
                if not isinstance(parsed[field], str) or not parsed[field].strip():
                    errors.append(f"{location}: PDF page {page} lacks non-empty {field}")
            for field in ("reviewer", "inspected_at", "observation"):
                if not isinstance(parsed[field], str) or not parsed[field].strip():
                    errors.append(f"{location}: PDF page {page} lacks non-empty {field}")
            merged[page] = parsed

    expected_pages = set(pages)
    if set(merged) != expected_pages:
        errors.append(
            "Inspection parts must contain exactly one record for every rendered page: "
            f"missing={sorted(expected_pages - set(merged))}, "
            f"extra={sorted(set(merged) - expected_pages)}"
        )
    if errors:
        print("PAGE INSPECTION ASSEMBLY FAILURES", file=sys.stderr)
        for error in errors:
            print(f"  - {error}", file=sys.stderr)
        return 1

    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        "".join(json.dumps(merged[page], sort_keys=True) + "\n" for page in sorted(merged)),
        encoding="utf-8",
    )
    print(f"Page inspection records assembled: {len(merged)}")
    print(f"Page inspection manifest: {output}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--input", "--pdf", dest="pdf", type=Path, default=DEFAULT_PDF,
        help="compiled PDF used for the release hash (default: latex/master.pdf)",
    )
    parser.add_argument(
        "--manifest", type=Path, default=DEFAULT_MANIFEST,
        help="rendered-page manifest JSONL (default: work/rendered-output/manifest.jsonl)",
    )
    parser.add_argument(
        "--parts-dir", type=Path, default=DEFAULT_PARTS_DIR,
        help="directory containing per-range inspection JSONL files",
    )
    parser.add_argument(
        "--output", type=Path, default=DEFAULT_OUTPUT,
        help="merged inspection manifest path",
    )
    args = parser.parse_args()
    return validate_and_merge(args.pdf, args.manifest, args.parts_dir, args.output)


if __name__ == "__main__":
    raise SystemExit(main())
