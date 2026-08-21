#!/usr/bin/env python3
"""Render the physical-page disposition ledger from native source markers."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LATEX = ROOT / "latex"
SOURCE = ROOT.parents[2] / "origPapers" / "pct_spin_statistics_all_that.pdf"
OVERRIDES = ROOT / "page-disposition-overrides.json"
OUTPUT = ROOT / "page-dispositions.jsonl"
EXPECTED_PAGES = 221
ALLOWED_STATUSES = {
    "transcribed",
    "represented",
    "represented_elsewhere",
    "omitted",
    "intentionally_omitted",
    "pending",
    "review",
}
CANONICAL_OVERRIDE_STATUSES = {
    1: "intentionally_omitted",
    2: "intentionally_omitted",
    3: "represented_elsewhere",
    4: "intentionally_omitted",
    7: "represented_elsewhere",
    8: "represented_elsewhere",
    11: "represented_elsewhere",
    12: "intentionally_omitted",
    220: "intentionally_omitted",
    221: "intentionally_omitted",
}

MARKER_RE = re.compile(
    r"PCT-SOURCE:\s*pdf=(?P<first>\d+)(?:--(?P<last>\d+))?"
    r"\s+print=(?P<printed>[^\s]+)\s+kind=(?P<kind>[^\s]+)"
)


def page_count() -> int:
    result = subprocess.run(
        ["pdfinfo", str(SOURCE)], check=True, capture_output=True, text=True
    )
    match = re.search(r"^Pages:\s+(\d+)\s*$", result.stdout, re.MULTILINE)
    if match is None:
        raise SystemExit("Could not read source page count from pdfinfo.")
    return int(match.group(1))


def collect_markers() -> dict[int, list[dict[str, str]]]:
    found: dict[int, list[dict[str, str]]] = defaultdict(list)
    for path in sorted(LATEX.rglob("*.tex")):
        relative = path.relative_to(ROOT).as_posix()
        for line_number, line in enumerate(path.read_text().splitlines(), start=1):
            match = MARKER_RE.search(line)
            if match is None:
                continue
            first = int(match.group("first"))
            last = int(match.group("last") or first)
            for page in range(first, last + 1):
                found[page].append(
                    {
                        "file": relative,
                        "line": str(line_number),
                        "print": match.group("printed"),
                        "kind": match.group("kind"),
                    }
                )
    return found


def load_overrides() -> dict[int, dict[str, object]]:
    raw = json.loads(OVERRIDES.read_text(encoding="utf-8"))
    if not isinstance(raw, dict):
        raise SystemExit("Page-disposition overrides must be a JSON object.")
    overrides: dict[int, dict[str, object]] = {}
    for raw_page, value in raw.items():
        try:
            page = int(raw_page)
        except (TypeError, ValueError) as error:
            raise SystemExit(f"Invalid override page {raw_page!r}: {error}") from error
        if not isinstance(value, dict):
            raise SystemExit(f"Override for PDF page {page} must be a JSON object.")
        overrides[page] = value
    if set(overrides) != set(CANONICAL_OVERRIDE_STATUSES):
        raise SystemExit(
            "Page-disposition overrides must match the frozen cover, blank-leaf, "
            f"title-leaf, and Contents set: {sorted(CANONICAL_OVERRIDE_STATUSES)}"
        )
    for page, expected_status in CANONICAL_OVERRIDE_STATUSES.items():
        actual_status = str(overrides[page].get("status", "")).strip().lower()
        if actual_status != expected_status:
            raise SystemExit(
                f"Override for PDF page {page} must be {expected_status!r}; "
                f"got {actual_status!r}"
            )
    return overrides


def validate_records(
    records: list[dict[str, object]],
    source_pages: int,
    *,
    strict: bool,
) -> list[str]:
    """Validate the rendered ledger before it is written or released.

    The renderer creates one record per physical page.  This second check keeps
    a malformed override, a stale source count, or an unresolved status from
    looking like complete coverage merely because the output has 221 lines.
    """

    issues: list[str] = []
    if source_pages != EXPECTED_PAGES:
        issues.append(
            f"Canonical source page count must be {EXPECTED_PAGES}; got {source_pages}"
        )
    expected_pages = set(range(1, source_pages + 1))
    seen: set[int] = set()
    for index, record in enumerate(records, start=1):
        raw_page = record.get("pdf_page")
        try:
            page = int(raw_page)
        except (TypeError, ValueError):
            issues.append(f"ledger record {index}: missing integer pdf_page")
            continue
        if page in seen:
            issues.append(f"ledger record {index}: duplicate PDF page {page}")
        seen.add(page)
        if page not in expected_pages:
            issues.append(f"ledger record {index}: PDF page {page} is outside source")
        status = str(record.get("status", record.get("classification", ""))).strip().lower()
        if status not in ALLOWED_STATUSES:
            issues.append(f"ledger record {index}, PDF page {page}: invalid status {status!r}")
        reason = record.get("reason")
        if not isinstance(reason, str) or not reason.strip():
            issues.append(f"ledger record {index}, PDF page {page}: missing reason")
        markers = record.get("markers")
        if not isinstance(markers, list):
            issues.append(f"ledger record {index}, PDF page {page}: markers must be a list")
        if strict and status in {"pending", "review"}:
            issues.append(f"ledger record {index}, PDF page {page}: unresolved status {status!r}")
    missing = sorted(expected_pages - seen)
    if missing:
        issues.append(f"ledger is missing PDF pages: {missing}")
    if len(records) != source_pages:
        issues.append(
            f"ledger must contain exactly {source_pages} records; found {len(records)}"
        )
    return issues


def render() -> tuple[list[dict[str, object]], list[int]]:
    count = page_count()
    markers = collect_markers()
    overrides = load_overrides()
    unknown_override_pages = sorted(set(overrides) - set(range(1, count + 1)))
    if unknown_override_pages:
        raise SystemExit(f"Override pages outside source: {unknown_override_pages}")

    records: list[dict[str, object]] = []
    pending: list[int] = []
    for page in range(1, count + 1):
        page_markers = markers.get(page, [])
        if page in overrides:
            record = {"pdf_page": page, **overrides[page]}
            record["markers"] = page_markers
        elif page_markers:
            printed = sorted({item["print"] for item in page_markers})
            record = {
                "pdf_page": page,
                "printed_page": printed[0] if len(printed) == 1 else printed,
                "status": "transcribed",
                "reason": "Native LaTeX source markers cover this physical page.",
                "markers": page_markers,
            }
        else:
            record = {
                "pdf_page": page,
                "printed_page": None,
                "status": "pending",
                "reason": "Awaiting native transcription or an explicit disposition.",
                "markers": [],
            }
            pending.append(page)
        records.append(record)
    return records, pending


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--strict", action="store_true")
    args = parser.parse_args()

    collected = collect_markers()
    if not any(collected.values()) and OUTPUT.is_file():
        records = [
            json.loads(line)
            for line in OUTPUT.read_text(encoding="utf-8").splitlines()
            if line.strip()
        ]
        pending = [
            int(record["pdf_page"])
            for record in records
            if str(record.get("status", record.get("classification", ""))).lower()
            in {"pending", "review"}
        ]
        print("No inline source markers; validating existing page-dispositions.jsonl.")
        issues = validate_records(records, page_count(), strict=args.strict)
    else:
        records, pending = render()
        issues = validate_records(records, page_count(), strict=args.strict)
        if args.write:
            OUTPUT.write_text(
                "".join(json.dumps(record, sort_keys=True) + "\n" for record in records),
                encoding="utf-8",
            )
    covered = len(records) - len(pending)
    print(f"Physical pages with dispositions: {covered}/{len(records)}")
    if pending:
        print("Pending PDF pages: " + ", ".join(str(page) for page in pending))
    if issues:
        print("PAGE-DISPOSITION AUDIT FAILURES", file=sys.stderr)
        for issue in issues:
            print(f"  - {issue}", file=sys.stderr)
    if args.strict and issues:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
