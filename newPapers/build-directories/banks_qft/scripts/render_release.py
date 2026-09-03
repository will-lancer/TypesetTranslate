#!/usr/bin/env python3
"""Render every output page and validate checksum-bound visual reviews."""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import re
import struct
import subprocess
from pathlib import Path


PAGE_RE = re.compile(r"page-(\d+)\.png$")
PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"
ROOT = Path(__file__).resolve().parents[1]
VISUAL_CHECKS = ("layout", "legibility", "clipping", "mathematics", "figures")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def page_count(pdf: Path) -> int:
    result = subprocess.run(["pdfinfo", str(pdf)], check=True, text=True, capture_output=True)
    match = re.search(r"^Pages:\s+(\d+)\s*$", result.stdout, re.MULTILINE)
    if match is None:
        raise SystemExit(f"Could not read page count from {pdf}")
    return int(match.group(1))


def dimensions(path: Path) -> tuple[int, int]:
    with path.open("rb") as handle:
        header = handle.read(24)
    if len(header) != 24 or header[:8] != PNG_SIGNATURE:
        raise SystemExit(f"Invalid PNG: {path}")
    return struct.unpack(">II", header[16:24])


def read_jsonl(path: Path) -> list[dict[str, object]]:
    if not path.is_file():
        raise SystemExit(f"Missing JSONL file: {path}")
    rows: list[dict[str, object]] = []
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        value = json.loads(line)
        if not isinstance(value, dict):
            raise SystemExit(f"{path}:{number}: expected a JSON object")
        rows.append(value)
    return rows


def render(pdf: Path, output_dir: Path, manifest: Path) -> int:
    output_dir.mkdir(parents=True, exist_ok=True)
    for path in output_dir.glob("page-*.png"):
        if PAGE_RE.fullmatch(path.name):
            path.unlink()
    subprocess.run(
        ["pdftoppm", "-png", "-r", "150", str(pdf), str(output_dir / "page")],
        check=True,
    )
    pages: dict[int, Path] = {}
    for path in output_dir.glob("page-*.png"):
        match = PAGE_RE.fullmatch(path.name)
        if match:
            pages[int(match.group(1))] = path
    count = page_count(pdf)
    if set(pages) != set(range(1, count + 1)):
        raise SystemExit("Rendered page set differs from compiled PDF")
    pdf_hash = sha256(pdf)
    rows = []
    for number in range(1, count + 1):
        path = pages[number]
        width, height = dimensions(path)
        rows.append(
            {
                "pdf_page": number,
                "filename": path.name,
                "sha256": sha256(path),
                "width_px": width,
                "height_px": height,
                "dpi": 150,
                "pdf_sha256": pdf_hash,
            }
        )
    manifest.parent.mkdir(parents=True, exist_ok=True)
    manifest.write_text(
        "".join(json.dumps(row, sort_keys=True) + "\n" for row in rows),
        encoding="utf-8",
    )
    print(f"Rendered {count} pages at 150 DPI: {output_dir}")
    return 0


def parse_pages(specification: str, maximum: int) -> list[int]:
    pages: set[int] = set()
    for part in specification.split(","):
        bounds = part.strip().split("-", 1)
        start = int(bounds[0])
        end = int(bounds[-1])
        if start > end:
            raise SystemExit(f"Invalid page range: {part}")
        pages.update(range(start, end + 1))
    if not pages or min(pages) < 1 or max(pages) > maximum:
        raise SystemExit(f"Review pages must lie in 1-{maximum}")
    return sorted(pages)


def record(
    manifest: Path,
    output: Path,
    pages_spec: str,
    reviewer: str,
    observation: str,
    report: Path,
) -> int:
    rows = read_jsonl(manifest)
    by_page = {int(row["pdf_page"]): row for row in rows}
    selected = parse_pages(pages_spec, len(rows))
    manifest_hash = sha256(manifest)
    if not reviewer.strip() or len(observation.strip()) < 20:
        raise SystemExit("Reviewer and a substantive observation are required")
    report = report.resolve()
    try:
        report_name = report.relative_to(ROOT).as_posix()
    except ValueError as error:
        raise SystemExit("Visual-review report must be inside the package root") from error
    if not report.is_file() or re.search(
        r"^FINAL STATUS:\s*PASS\s*$",
        report.read_text(encoding="utf-8", errors="replace"),
        re.MULTILINE,
    ) is None:
        raise SystemExit("Visual-review report is missing or has no PASS verdict")
    report_hash = sha256(report)
    inspected_at = dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat()
    records = []
    for page in selected:
        rendered = by_page[page]
        records.append(
            {
                "pdf_page": page,
                "status": "pass",
                "reviewer": reviewer,
                "inspected_at": inspected_at,
                "observation": observation,
                "checks": {name: "pass" for name in VISUAL_CHECKS},
                "rendered_sha256": rendered["sha256"],
                "render_manifest_sha256": manifest_hash,
                "pdf_sha256": rendered["pdf_sha256"],
                "review_report": report_name,
                "review_report_sha256": report_hash,
            }
        )
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        "".join(json.dumps(row, sort_keys=True) + "\n" for row in records),
        encoding="utf-8",
    )
    print(f"Recorded {len(records)} reviewed pages: {output}")
    return 0


def validate(
    pdf: Path,
    output_dir: Path,
    manifest: Path,
    reviews: list[Path],
    summary: Path | None,
) -> int:
    render_rows = read_jsonl(manifest)
    count = page_count(pdf)
    pdf_hash = sha256(pdf)
    manifest_hash = sha256(manifest)
    by_page: dict[int, dict[str, object]] = {}
    for row in render_rows:
        page = int(row.get("pdf_page", 0))
        if page in by_page:
            raise SystemExit(f"Duplicate rendered page {page}")
        by_page[page] = row
        path = output_dir / str(row.get("filename", ""))
        if not path.is_file() or sha256(path) != row.get("sha256"):
            raise SystemExit(f"Rendered file changed for page {page}")
        if row.get("dpi") != 150 or row.get("pdf_sha256") != pdf_hash:
            raise SystemExit(f"Rendered provenance mismatch for page {page}")
    if set(by_page) != set(range(1, count + 1)):
        raise SystemExit("Render manifest page coverage is incomplete")

    inspected: dict[int, dict[str, object]] = {}
    reviewers: set[str] = set()
    reports: dict[str, str] = {}
    for review_path in reviews:
        part_rows = read_jsonl(review_path)
        part_pages = [int(row.get("pdf_page", 0)) for row in part_rows]
        if not part_pages or sorted(part_pages) != list(range(min(part_pages), max(part_pages) + 1)):
            raise SystemExit(f"Visual-review part is not one contiguous lane: {review_path}")
        part_reviewers = {str(row.get("reviewer", "")).strip() for row in part_rows}
        if len(part_reviewers) != 1 or "" in part_reviewers:
            raise SystemExit(f"Visual-review part must have one named reviewer: {review_path}")
        reviewers.update(part_reviewers)
        for row in part_rows:
            page = int(row.get("pdf_page", 0))
            if page in inspected:
                raise SystemExit(f"Duplicate visual review for page {page}")
            inspected[page] = row
            if row.get("status") != "pass" or not str(row.get("reviewer", "")).strip():
                raise SystemExit(f"Visual review did not pass for page {page}")
            if len(str(row.get("observation", "")).strip()) < 20:
                raise SystemExit(f"Visual review lacks a substantive observation for page {page}")
            checks = row.get("checks")
            if not isinstance(checks, dict) or any(checks.get(name) != "pass" for name in VISUAL_CHECKS):
                raise SystemExit(f"Visual review lacks structured checks for page {page}")
            report_name = str(row.get("review_report", ""))
            report = (ROOT / report_name).resolve()
            try:
                report.relative_to(ROOT)
            except ValueError as error:
                raise SystemExit(f"Visual-review report escapes package root for page {page}") from error
            if not report.is_file() or sha256(report) != row.get("review_report_sha256"):
                raise SystemExit(f"Visual-review report hash mismatch for page {page}")
            if re.search(
                r"^FINAL STATUS:\s*PASS\s*$",
                report.read_text(encoding="utf-8", errors="replace"),
                re.MULTILINE,
            ) is None:
                raise SystemExit(f"Visual-review report has no PASS verdict for page {page}")
            previous_reporter = reports.setdefault(report_name, str(row["reviewer"]))
            if previous_reporter != str(row["reviewer"]):
                raise SystemExit(f"Visual-review report is shared by multiple reviewers: {report_name}")
            if row.get("rendered_sha256") != by_page.get(page, {}).get("sha256"):
                raise SystemExit(f"Rendered checksum mismatch for reviewed page {page}")
            if row.get("render_manifest_sha256") != manifest_hash:
                raise SystemExit(f"Manifest checksum mismatch for reviewed page {page}")
            if row.get("pdf_sha256") != pdf_hash:
                raise SystemExit(f"PDF checksum mismatch for reviewed page {page}")
    if set(inspected) != set(range(1, count + 1)):
        missing = sorted(set(range(1, count + 1)) - set(inspected))
        raise SystemExit(f"Visual review coverage incomplete: missing {missing}")
    if len(reviewers) < 3:
        raise SystemExit("Visual review requires at least three disjoint reviewer lanes")
    if summary is not None:
        summary.parent.mkdir(parents=True, exist_ok=True)
        evidence = {
            "schema_version": 1,
            "status": "pass",
            "pdf_sha256": pdf_hash,
            "page_count": count,
            "pages_reviewed": len(inspected),
            "render_manifest_sha256": manifest_hash,
            "review_parts": [
                {"path": str(path), "sha256": sha256(path)} for path in reviews
            ],
            "reviewers": sorted(reviewers),
            "review_reports": [
                {"path": name, "sha256": sha256(ROOT / name), "reviewer": reviewer}
                for name, reviewer in sorted(reports.items())
            ],
        }
        summary.write_text(json.dumps(evidence, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"Visual review coverage passes: {count}/{count} pages")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command", required=True)
    render_parser = subparsers.add_parser("render")
    render_parser.add_argument("--pdf", type=Path, required=True)
    render_parser.add_argument("--output-dir", type=Path, required=True)
    render_parser.add_argument("--manifest", type=Path, required=True)
    record_parser = subparsers.add_parser("record")
    record_parser.add_argument("--manifest", type=Path, required=True)
    record_parser.add_argument("--output", type=Path, required=True)
    record_parser.add_argument("--pages", required=True)
    record_parser.add_argument("--reviewer", required=True)
    record_parser.add_argument("--observation", required=True)
    record_parser.add_argument("--report", type=Path, required=True)
    validate_parser = subparsers.add_parser("validate")
    validate_parser.add_argument("--pdf", type=Path, required=True)
    validate_parser.add_argument("--output-dir", type=Path, required=True)
    validate_parser.add_argument("--manifest", type=Path, required=True)
    validate_parser.add_argument("--reviews", type=Path, nargs="+", required=True)
    validate_parser.add_argument("--summary", type=Path)
    args = parser.parse_args()
    if args.command == "render":
        return render(args.pdf, args.output_dir, args.manifest)
    if args.command == "record":
        return record(
            args.manifest,
            args.output,
            args.pages,
            args.reviewer,
            args.observation,
            args.report,
        )
    return validate(args.pdf, args.output_dir, args.manifest, args.reviews, args.summary)


if __name__ == "__main__":
    raise SystemExit(main())
