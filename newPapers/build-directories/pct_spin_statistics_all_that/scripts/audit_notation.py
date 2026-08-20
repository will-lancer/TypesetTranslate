#!/usr/bin/env python3
"""Check the PCT transcription against the house QFT notation contract."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LATEX = ROOT / "latex"
NOTATION = ROOT / "NOTATION.md"
NOTATION_MAP = ROOT / "notation-map.jsonl"
REVIEWED_STATUSES = {"reviewed", "reviewed-current-corpus", "resolved"}


RULES: tuple[tuple[str, re.Pattern[str], str, bool], ...] = (
    (
        "legacy-script-alphabet",
        re.compile(r"\\mathscr\b"),
        r"use the stable project \mathcal alphabet and named AQFT macros",
        True,
    ),
    (
        "arrow-vector",
        re.compile(r"\\(?:vec|overrightarrow|overleftarrow)\b"),
        r"use \mathbf for spatial vectors and reserve hats for unit vectors",
        True,
    ),
    (
        "state-label-inside-asymptotic-delimiter",
        re.compile(
            r"\\(?:ket|bra)\s*\{[^}\n]*\}\s*_\s*\{?\s*"
            r"\\(?:mathrm|text|operatorname)\s*\{?\s*(?:in|out)\b"
        ),
        r"use \InKet, \OutKet, \InBra, or \OutBra",
        True,
    ),
    (
        "raw-inner-product-bar",
        re.compile(r"\\langle[^\n]{0,120}(?<!\\)\|[^\n]{0,120}\\rangle"),
        r"use \braket or \matrixel with \vert",
        True,
    ),
    (
        "raw-source-star",
        re.compile(r"(?<![\\A-Za-z])(?:[A-Za-z]|\})\s*\^\s*\*"),
        r"classify the star as conjugation, adjoint, or dual in context",
        False,
    ),
    (
        "legacy-metric-signature",
        re.compile(
            r"(?:\\operatorname\s*\{\s*diag\s*\}|\\diag)"
            r"\s*\([^\n)]*(?:\+?1\s*,\s*-1|-1\s*,\s*\+1)[^\n)]*\)"
        ),
        "record the source signature as an exception or use the house metric macro",
        True,
    ),
    (
        "raw-hilbert-product-tuple",
        re.compile(r"\(\s*(?:\\psi|\\phi|\\Psi|\\Phi)\s*,\s*(?:\\psi|\\phi|\\Psi|\\Phi)\s*\)"),
        r"use explicit Dirac notation for a Hilbert-space product",
        False,
    ),
    (
        "source-metric-symbol",
        re.compile(r"(?<![A-Za-z\\])g\s*_\s*\{?\\(?:mu|nu)"),
        "check every source metric against eta and record a notation-map entry",
        False,
    ),
)


def uncommented(line: str) -> str:
    return re.split(r"(?<!\\)%", line, maxsplit=1)[0]


def has_exception(lines: list[str], index: int) -> bool:
    return any("NOTATION EXCEPTION:" in line for line in lines[max(0, index - 8) : index + 1])


def source_files() -> list[Path]:
    if not LATEX.exists():
        return []
    return sorted(
        path
        for path in LATEX.rglob("*.tex")
        if path.name != "master.tex"
    )


def load_candidate_map() -> tuple[dict[tuple[str, int, str], list[dict]], list[str]]:
    """Load exact audit candidates from the notation ledger.

    The audit emits a file, line, and rule for each review candidate.  A
    ledger row must carry the same triple and a reviewed classification.  The
    separate error list keeps malformed rows visible in draft mode while
    strict mode can fail deterministically.
    """

    index: dict[tuple[str, int, str], list[dict]] = {}
    errors: list[str] = []
    if not NOTATION_MAP.is_file():
        errors.append(f"Missing notation ledger: {NOTATION_MAP.name}")
        return index, errors

    for line_number, raw_line in enumerate(
        NOTATION_MAP.read_text(encoding="utf-8").splitlines(), 1
    ):
        if not raw_line.strip():
            continue
        try:
            record = json.loads(raw_line)
        except json.JSONDecodeError as error:
            errors.append(
                f"{NOTATION_MAP.name}:{line_number}: invalid JSON: {error.msg}"
            )
            continue
        if not isinstance(record, dict):
            errors.append(
                f"{NOTATION_MAP.name}:{line_number}: notation record is not an object"
            )
            continue
        candidate = record.get("audit_candidate")
        if candidate is None:
            continue
        if not isinstance(candidate, dict):
            errors.append(
                f"{NOTATION_MAP.name}:{line_number}: audit_candidate is not an object"
            )
            continue

        file_name = candidate.get("file")
        source_line = candidate.get("line")
        rule = candidate.get("rule")
        classification = candidate.get("classification")
        valid_key = (
            isinstance(file_name, str)
            and bool(file_name)
            and isinstance(source_line, int)
            and not isinstance(source_line, bool)
            and source_line > 0
            and isinstance(rule, str)
            and bool(rule)
        )
        if not valid_key:
            errors.append(
                f"{NOTATION_MAP.name}:{line_number}: audit_candidate needs a valid file, line, and rule"
            )
            continue
        if not isinstance(classification, str) or not classification.strip():
            errors.append(
                f"{NOTATION_MAP.name}:{line_number}: audit_candidate classification is empty"
            )
        verification = record.get("verification")
        status = verification.get("status") if isinstance(verification, dict) else None
        if status not in REVIEWED_STATUSES:
            errors.append(
                f"{NOTATION_MAP.name}:{line_number}: audit candidate status is not reviewed: {status!r}"
            )
        key = (file_name, source_line, rule)
        index.setdefault(key, []).append(
            {
                "line_number": line_number,
                "classification": classification.strip()
                if isinstance(classification, str)
                else "",
                "status": status,
            }
        )
    return index, errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--strict", action="store_true")
    args = parser.parse_args()

    failures: list[str] = []
    reviews: list[str] = []
    candidate_hits: list[tuple[tuple[str, int, str], str]] = []
    if not NOTATION.is_file():
        item = f"Missing binding notation policy: {NOTATION.name}"
        (failures if args.strict else reviews).append(item)

    for path in source_files():
        lines = path.read_text(encoding="utf-8").splitlines()
        for index, raw_line in enumerate(lines):
            code = uncommented(raw_line)
            if not code.strip() or has_exception(lines, index):
                continue
            for name, pattern, explanation, fatal in RULES:
                if not pattern.search(code):
                    continue
                relative = path.relative_to(ROOT)
                finding = f"{relative}:{index + 1}: {name}: {explanation}"
                candidate_hits.append(((str(relative), index + 1, name), finding))
                (failures if fatal else reviews).append(finding)

    candidate_map, map_errors = load_candidate_map()
    for error in map_errors:
        (failures if args.strict else reviews).append(error)

    emitted_keys = {key for key, _ in candidate_hits}
    classifications: list[str] = []
    for key, finding in candidate_hits:
        records = candidate_map.get(key, [])
        if len(records) != 1:
            if not records:
                reason = "no exact reviewed notation-map classification"
            else:
                reason = f"{len(records)} exact notation-map classifications"
            message = f"{finding}: {reason}"
            (failures if args.strict else reviews).append(message)
            continue
        record = records[0]
        classifications.append(
            f"{key[0]}:{key[1]}:{key[2]} -> {record['classification']}"
        )

    for key in sorted(candidate_map):
        if key in emitted_keys:
            continue
        message = (
            f"{NOTATION_MAP.name}: stale audit candidate {key[0]}:{key[1]}:{key[2]} "
            "has no current audit_notation emission"
        )
        (failures if args.strict else reviews).append(message)

    print(f"Notation policy: {'present' if NOTATION.is_file() else 'missing'}")
    print(f"Transcription files scanned: {len(source_files())}")
    if reviews:
        print("NOTATION REVIEW CANDIDATES")
        for finding in reviews:
            print(f"  - {finding}")
    if classifications:
        print("NOTATION MAP CLASSIFICATIONS")
        for classification in classifications:
            print(f"  - {classification}")
    if failures:
        print("DEFINITE NOTATION REGRESSIONS", file=sys.stderr)
        for finding in failures:
            print(f"  - {finding}", file=sys.stderr)
        if args.strict:
            return 1
        print("Draft mode: notation findings are reported and do not stop the pilot build.")
    else:
        print("No definite notation regressions found.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
