#!/usr/bin/env python3
"""Check source-page prose shingles against the native output text layer."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from statistics import median
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "banks-qft.pdf"
LIGATURES = str.maketrans({"ﬁ": "fi", "ﬂ": "fl", "ﬀ": "ff", "ﬃ": "ffi", "ﬄ": "ffl"})


def extract(pdf: Path) -> list[str]:
    result = subprocess.run(
        ["pdftotext", "-layout", "-enc", "UTF-8", str(pdf), "-"],
        check=True,
        text=True,
        capture_output=True,
    )
    return result.stdout.split("\f")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def tokens(text: str) -> list[str]:
    text = text.translate(LIGATURES).lower()
    text = re.sub(r"([a-z])-[ \t]*\n[ \t]*([a-z])", r"\1\2", text)
    text = re.sub(r"\b(?:contents|references|author index|subject index)\b", " ", text)
    # Single-letter variables and digits are unstable in PDF text extraction.
    # Equation identity is checked separately through the numbered-object ledger.
    return [
        word for word in re.findall(r"[a-z]+(?:'[a-z]+)?", text)
        if len(word) > 1
    ]


def shingles(words: list[str], width: int = 4) -> set[tuple[str, ...]]:
    return {tuple(words[index:index + width]) for index in range(len(words) - width + 1)}


def output_windows(pages: list[list[str]], width: int, span: int = 6) -> list[set[tuple[str, ...]]]:
    windows: list[set[tuple[str, ...]]] = []
    for start in range(len(pages)):
        words: list[str] = []
        for page in pages[start:start + span]:
            words.extend(page)
        windows.append(shingles(words, width))
    return windows


def brace_groups(text: str) -> list[str]:
    """Parse balanced top-level brace groups from one .aux payload."""
    groups: list[str] = []
    index = 0
    while index < len(text):
        while index < len(text) and text[index].isspace():
            index += 1
        if index >= len(text) or text[index] != "{":
            return []
        start = index + 1
        depth = 1
        index += 1
        while index < len(text) and depth:
            if text[index] == "{" and (index == 0 or text[index - 1] != "\\"):
                depth += 1
            elif text[index] == "}" and (index == 0 or text[index - 1] != "\\"):
                depth -= 1
            index += 1
        if depth:
            return []
        groups.append(text[start:index - 1])
    return groups


def unwrap_braces(value: str) -> str:
    while len(value) >= 2 and value.startswith("{") and value.endswith("}"):
        groups = brace_groups(value)
        if len(groups) != 1:
            break
        value = groups[0]
    return value


def parse_equation_aux(aux: Path, expected_ids: list[str]) -> tuple[dict[str, dict[str, object]], list[str]]:
    if not aux.is_file():
        return {}, [f"missing equation auxiliary file: {aux}"]
    records: dict[str, dict[str, object]] = {}
    failures: list[str] = []
    for line in aux.read_text(encoding="utf-8", errors="replace").splitlines():
        match = re.match(r"^\\newlabel\{eq:([^{}]+)\}(.*)$", line)
        if match is None:
            continue
        identifier = match.group(1)
        outer = brace_groups(match.group(2).strip())
        fields = brace_groups(outer[0]) if len(outer) == 1 else []
        if len(fields) < 2:
            failures.append(f"malformed equation auxiliary record: {identifier}")
            continue
        display = unwrap_braces(fields[0]).strip()
        page_text = unwrap_braces(fields[1]).strip()
        try:
            page = int(page_text)
        except ValueError:
            failures.append(f"non-numeric equation page: {identifier}")
            continue
        if identifier in records:
            failures.append(f"duplicate equation auxiliary record: {identifier}")
            continue
        records[identifier] = {"display": display, "aux_page": page}

    expected = set(expected_ids)
    for identifier in expected_ids:
        if identifier not in records:
            failures.append(f"missing equation auxiliary record: {identifier}")
    for identifier in sorted(set(records) - expected):
        # Numbered solution derivations have their own stable labels. They are
        # audited as editorial output, while the native equation ledger remains
        # the exact expected set for the transcription.
        if re.search(r"(?:^|-)sol(?:-|$)", identifier):
            continue
        failures.append(f"unexpected equation auxiliary record: {identifier}")
    return records, failures


def equation_audit(pdf: Path, output_pages: list[str]) -> tuple[dict[str, object], list[str]]:
    expected_ids = [str(value) for value in json.loads(
        (ROOT / "numbered-equations.json").read_text(encoding="utf-8")
    )]
    aux_records, failures = parse_equation_aux(pdf.with_suffix(".aux"), expected_ids)
    occurrences: dict[str, list[int]] = {}
    for identifier in expected_ids:
        record = aux_records.get(identifier)
        if record is None:
            continue
        display = str(record["display"])
        compact = re.sub(r"\s+", "", display)
        target = f"({compact})"
        occurrences[identifier] = [
            page_number
            for page_number, page_text in enumerate(output_pages, 1)
            if target in re.sub(r"\s+", "", page_text)
        ]

    offset_candidates: list[int] = []
    for identifier in expected_ids[:8]:
        record = aux_records.get(identifier)
        pages = occurrences.get(identifier, [])
        if record is not None and pages:
            offset_candidates.append(pages[0] - int(record["aux_page"]))
    offset = int(median(offset_candidates)) if offset_candidates else 0
    tolerance = max(12, (len(output_pages) + 12) // 13)
    equation_records: list[dict[str, object]] = []
    selected_pages: list[int] = []
    matched = 0
    for identifier in expected_ids:
        record = aux_records.get(identifier)
        pages = occurrences.get(identifier, [])
        if record is None:
            continue
        expected_page = int(record["aux_page"]) + offset
        chosen_page = min(pages, key=lambda page: abs(page - expected_page)) if pages else None
        position_delta = None if chosen_page is None else chosen_page - expected_page
        page_status = chosen_page is not None and abs(int(position_delta)) <= tolerance
        if chosen_page is None:
            failures.append(f"equation label is absent from output: {identifier}")
        elif not page_status:
            failures.append(
                f"equation label is out of position: {identifier} "
                f"output={chosen_page} expected={expected_page} tolerance={tolerance}"
            )
        else:
            matched += 1
            selected_pages.append(chosen_page)
        equation_records.append(
            {
                "id": identifier,
                "display": record["display"],
                "aux_page": record["aux_page"],
                "output_pages": pages,
                "selected_output_page": chosen_page,
                "expected_output_page": expected_page,
                "position_delta_pages": position_delta,
                "position_tolerance_pages": tolerance,
                "status": "pass" if page_status else "fail",
            }
        )
    if selected_pages != sorted(selected_pages):
        failures.append("Equation labels are out of source order in the output text layer")
    evidence = {
        "expected": len(expected_ids),
        "aux_records": len(aux_records),
        "matched": matched,
        "aux_to_output_page_offset": offset,
        "position_tolerance_pages": tolerance,
        "records": equation_records,
        "status": "pass" if not failures else "fail",
    }
    return evidence, failures


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--edition", choices=("base", "implicit"), required=True)
    parser.add_argument("--pdf", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--strict", action="store_true")
    args = parser.parse_args()
    source_pages = extract(SOURCE)
    if len(source_pages) < 281:
        raise SystemExit("Source text extraction returned fewer than 281 pages")
    output_pages = extract(args.pdf)
    output_page_words = [tokens(page) for page in output_pages]
    while output_page_words and not output_page_words[-1]:
        output_page_words.pop()
    output_pages = output_pages[:len(output_page_words)]
    if not output_page_words:
        raise SystemExit("Output text extraction returned no pages")
    candidate_windows = {
        1: output_windows(output_page_words, 1),
        2: output_windows(output_page_words, 2),
        4: output_windows(output_page_words, 4),
    }
    records = []
    failures: list[str] = []
    recall_failures: list[tuple[int, float, float]] = []
    position_failures: list[str] = []
    cursor = 0
    position_tolerance = max(24, (len(output_page_words) + 9) // 10)
    source_page_count = 282 - 11
    for pdf_page in range(11, 282):
        # pdftotext interleaves the two index columns according to layout.
        # Local word-set recall checks those pages without assuming column order.
        width = 1 if pdf_page >= 278 else 4
        page_shingles = shingles(tokens(source_pages[pdf_page - 1]), width)
        source_index = pdf_page - 11
        expected_position = round(
            source_index * max(len(output_page_words) - 1, 0) / max(source_page_count - 1, 1)
        )
        window_low = max(cursor, expected_position - position_tolerance)
        window_high = min(len(output_page_words) - 1, expected_position + position_tolerance)
        if not page_shingles:
            recall = 1.0
            matched = 0
            best_start = max(window_low, min(expected_position, window_high))
        else:
            best_start = window_low
            matched = -1
            for start in range(window_low, window_high + 1):
                count = len(page_shingles & candidate_windows[width][start])
                if count > matched:
                    matched = count
                    best_start = start
            if matched < 0:
                matched = 0
            recall = matched / len(page_shingles)
        cursor = best_start
        threshold = 0.98 if pdf_page >= 278 else (0.45 if pdf_page >= 272 else 0.68)
        position_delta = best_start - expected_position
        record = {
            "source_pdf_page": pdf_page,
            "printed_page": pdf_page - 10,
            "shingle_width": width,
            "source_shingles": len(page_shingles),
            "matched_shingles": matched,
            "recall": round(recall, 6),
            "threshold": threshold,
            "expected_output_pdf_page": expected_position + 1,
            "position_delta_pages": position_delta,
            "position_tolerance_pages": position_tolerance,
            "candidate_output_start": [window_low + 1, window_high + 1],
            "output_pdf_window": [best_start + 1, min(best_start + 6, len(output_page_words))],
            "status": "pass"
            if recall >= threshold and abs(position_delta) <= position_tolerance
            else "fail",
        }
        records.append(record)
        if recall < threshold:
            recall_failures.append((pdf_page, recall, threshold))
            failures.append(f"low recall source page {pdf_page}: {recall:.3f} < {threshold:.3f}")
        if abs(position_delta) > position_tolerance:
            position_failures.append(
                f"source page {pdf_page} output start delta {position_delta} exceeds "
                f"{position_tolerance} pages"
            )
            failures.append(position_failures[-1])
    equation_evidence, equation_failures = equation_audit(args.pdf, output_pages)
    failures.extend(equation_failures)
    evidence = {
        "schema_version": 2,
        "edition": args.edition,
        "source_sha256": sha256(SOURCE),
        "output_sha256": sha256(args.pdf),
        "method": "normalized source-page shingles matched inside position-bounded monotonically ordered six-page output windows; equation labels are checked from the output auxiliary file",
        "output_page_count": len(output_page_words),
        "position_tolerance_pages": position_tolerance,
        "pages": records,
        "equations": equation_evidence,
        "minimum_recall": min(row["recall"] for row in records),
        "status": "pass" if not failures else "fail",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(evidence, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    if recall_failures:
        print("Low-recall source pages: " + ", ".join(f"{p}={r:.3f}" for p, r, _ in recall_failures))
        if args.strict:
            return 1
    if position_failures:
        print("Position failures: " + "; ".join(position_failures))
        if args.strict:
            return 1
    if equation_failures:
        print("Equation failures: " + "; ".join(equation_failures))
        if args.strict:
            return 1
    print(f"Text recall audit: {len(records) - len(recall_failures)}/{len(records)} pages pass")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
