#!/usr/bin/env python3
"""Audit the PCT assembly, native chunk set, and release ledgers."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

from audit_source import EXPECTED_CHUNKS, EXPECTED_PAGES, MARKER


ROOT = Path(__file__).resolve().parents[1]
LATEX = ROOT / "latex"
MASTER = LATEX / "master.tex"
REQUIRED_PROJECT_FILES = (
    "PLAN.md",
    "README.md",
    "SOURCE_MANIFEST.yaml",
    "SOURCE_MAP.md",
    "NOTATION.md",
    "ERRATA.md",
    "TRANSCRIPTION_CONTRACT.md",
    "TRANSCRIPTION_STATUS.md",
    "RELEASE_VERIFICATION.md",
    "notation-map.jsonl",
    "page-dispositions.jsonl",
)
PLACEHOLDER = re.compile(
    r"\b(?:TODO|FIXME|TBD|PLACEHOLDER|TRANSCRIBE|INSERT\s+(?:TEXT|EQUATION)|"
    r"PCT[-_ ]?(?:QUERY|REVIEW)|SOURCE[-_ ]?QUERY|MISSING\s+CHUNK)\b",
    re.IGNORECASE,
)
FORBIDDEN_SOURCE_IMPORT = re.compile(
    r"\\(?:usepackage|RequirePackage)\s*\{\s*pdfpages\s*\}|"
    r"\\(?:includepdf|facsimilepages|frontmatterpages)\b|"
    r"(?:source-pages|origPapers|facsimile|scan[-_]?page)",
    re.IGNORECASE,
)
INPUT = re.compile(r"\\PCTInput\s*\{([^}\n]+)\}")
LABEL = re.compile(r"\\label\s*\{([^}\n]+)\}")
REFERENCE = re.compile(r"\\(?:ref|pageref|eqref|autoref)\s*\{([^}\n]+)\}")
ENVIRONMENT = re.compile(r"\\(?P<command>begin|end)\s*\{(?P<name>[^}\n]+)\}")
BIB_ENTRY = re.compile(r"\\bibitem\b|\\item(?:\[[^]]*\])?")


def uncommented(line: str) -> str:
    return re.split(r"(?<!\\)%", line, maxsplit=1)[0]


def text_without_comments(text: str) -> str:
    return "\n".join(uncommented(line) for line in text.splitlines())


def fail_or_review(items: list[str], message: str, strict: bool) -> None:
    if strict:
        items.append(message)


def audit_environment_nesting(text: str, issues: list[str]) -> None:
    stack: list[tuple[str, int]] = []
    for token in ENVIRONMENT.finditer(text_without_comments(text)):
        name = token.group("name")
        line = text.count("\n", 0, token.start()) + 1
        if token.group("command") == "begin":
            stack.append((name, line))
            continue
        if not stack:
            issues.append(f"environment {name} closes at line {line} without an opening")
            continue
        opened, opened_line = stack.pop()
        if opened != name:
            issues.append(
                f"environment {name} closes at line {line}; "
                f"{opened} from line {opened_line} was open"
            )
    for name, line in reversed(stack):
        issues.append(f"environment {name} opened at line {line} is not closed")


def audit_page_ledger(issues: list[str]) -> None:
    path = ROOT / "page-dispositions.jsonl"
    if not path.is_file():
        issues.append("Missing page-dispositions.jsonl")
        return
    pages: dict[int, dict[str, object]] = {}
    allowed = {
        "transcribed",
        "represented",
        "represented_elsewhere",
        "omitted",
        "intentionally_omitted",
        "pending",
        "review",
    }
    for line_number, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if not raw.strip():
            continue
        try:
            record = json.loads(raw)
        except json.JSONDecodeError as error:
            issues.append(f"page-dispositions.jsonl:{line_number}: invalid JSON: {error}")
            continue
        raw_page = record.get("pdf_page", record.get("page"))
        try:
            page = int(raw_page)
        except (TypeError, ValueError):
            issues.append(f"page-dispositions.jsonl:{line_number}: missing integer pdf_page")
            continue
        if not 1 <= page <= EXPECTED_PAGES:
            issues.append(
                f"page-dispositions.jsonl:{line_number}: PDF page {page} is outside 1--{EXPECTED_PAGES}"
            )
        if page in pages:
            issues.append(f"page-dispositions.jsonl:{line_number}: duplicate PDF page {page}")
        pages[page] = record
        classification = str(record.get("classification", record.get("status", ""))).lower()
        if classification not in allowed:
            issues.append(
                f"page-dispositions.jsonl:{line_number}: unsupported classification {classification!r}"
            )
        if not str(record.get("reason", "")).strip():
            issues.append(f"page-dispositions.jsonl:{line_number}: missing reason")
        if "markers" not in record or not isinstance(record.get("markers"), list):
            issues.append(f"page-dispositions.jsonl:{line_number}: markers must be a list")
        if classification in {"pending", "review"}:
            issues.append(
                f"page-dispositions.jsonl:{line_number}: unresolved disposition {classification!r}"
            )
    missing = sorted(set(range(1, EXPECTED_PAGES + 1)) - set(pages))
    if missing:
        issues.append(f"page-dispositions.jsonl: missing PDF pages {missing}")
    if len(pages) != EXPECTED_PAGES:
        issues.append(
            f"page-dispositions.jsonl: expected {EXPECTED_PAGES} unique pages, found {len(pages)}"
        )


def audit_notation_map(issues: list[str]) -> None:
    path = ROOT / "notation-map.jsonl"
    if not path.is_file():
        issues.append("Missing notation-map.jsonl")
        return
    records = 0
    for line_number, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if not raw.strip():
            continue
        try:
            record = json.loads(raw)
        except json.JSONDecodeError as error:
            issues.append(f"notation-map.jsonl:{line_number}: invalid JSON: {error}")
            continue
        records += 1
        if not any(key in record for key in ("pdf_page", "source_page", "page")):
            issues.append(f"notation-map.jsonl:{line_number}: missing source-page key")
        else:
            raw_page = next(
                record[key]
                for key in ("pdf_page", "source_page", "page")
                if key in record
            )
            page_text = str(raw_page).strip()
            page_match = re.fullmatch(r"(\d+)(?:\s*[-–]\s*(\d+))?", page_text)
            if page_match is None:
                issues.append(f"notation-map.jsonl:{line_number}: invalid source-page value {raw_page!r}")
            else:
                first = int(page_match.group(1))
                last = int(page_match.group(2) or first)
                if first < 1 or last > EXPECTED_PAGES or first > last:
                    issues.append(f"notation-map.jsonl:{line_number}: source page outside 1--{EXPECTED_PAGES}")
        if not any(key in record for key in ("source", "from", "original")):
            issues.append(f"notation-map.jsonl:{line_number}: missing source notation")
        elif not str(next(record[key] for key in ("source", "from", "original") if key in record)).strip():
            issues.append(f"notation-map.jsonl:{line_number}: empty source notation")
        if not any(key in record for key in ("native", "to", "adopted")):
            issues.append(f"notation-map.jsonl:{line_number}: missing native notation")
        elif not str(next(record[key] for key in ("native", "to", "adopted") if key in record)).strip():
            issues.append(f"notation-map.jsonl:{line_number}: empty native notation")
        verification = record.get("verification")
        if not isinstance(verification, dict):
            issues.append(f"notation-map.jsonl:{line_number}: missing verification object")
        else:
            status = verification.get("status")
            if not isinstance(status, str) or not status.strip():
                issues.append(f"notation-map.jsonl:{line_number}: missing verification status")
            else:
                status_text = status.strip().lower()
                blocked = re.search(
                    r"(?:^|[-_\s])(needs-correction|pending|unresolved|review)(?:$|[-_\s])",
                    status_text,
                )
                if blocked:
                    issues.append(
                        f"notation-map.jsonl:{line_number}: blocked verification status {status!r}"
                    )
    if records == 0:
        issues.append("notation-map.jsonl has no notation conversion records")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--strict", action="store_true")
    args = parser.parse_args()

    failures: list[str] = []
    reviews: list[str] = []

    if not MASTER.is_file():
        failures.append("Missing latex/master.tex")
        master = ""
    else:
        master = MASTER.read_text(encoding="utf-8")

    for relative in REQUIRED_PROJECT_FILES:
        if not (ROOT / relative).is_file():
            fail_or_review(failures, f"Missing required project file: {relative}", args.strict)

    actual_chunks = sorted(
        path.relative_to(LATEX).as_posix()
        for path in LATEX.rglob("*.tex")
        if path.name != "master.tex"
    )
    missing_chunks = [relative for relative in EXPECTED_CHUNKS if relative not in actual_chunks]
    # Native figure source files are support inputs owned by the manuscript
    # chunks.  The expected-chunk ledger covers prose and back matter, while
    # figure files remain independently auditable under latex/figures/.
    extra_chunks = [
        relative
        for relative in actual_chunks
        if relative not in EXPECTED_CHUNKS and not relative.startswith("figures/")
    ]
    if missing_chunks:
        fail_or_review(
            failures,
            "Missing native chunks: " + ", ".join(missing_chunks),
            args.strict,
        )
    if extra_chunks:
        fail_or_review(
            failures,
            "Unexpected native chunks: " + ", ".join(extra_chunks),
            args.strict,
        )

    assembly = INPUT.findall(master)
    if assembly != EXPECTED_CHUNKS:
        message = f"master.tex assembly order mismatch; expected {EXPECTED_CHUNKS}, got {assembly}"
        fail_or_review(failures, message, args.strict)

    required_master_tokens = (
        r"\documentclass[11pt,a4paper]{article}",
        r"\usepackage{jheppub}",
        r"\usepackage{pct}",
        r"\title{PCT, Spin and Statistics, and All That}",
        r"\author[a]{R. F. Streater}",
        r"\author[b]{A. S. Wightman}",
        r"\maketitle",
        r"\appendix",
    )
    for token in required_master_tokens:
        if token not in master:
            failures.append(f"master.tex is missing required token {token}")
    if r"\subheader{" in master:
        failures.append("master.tex carries an editorial subheader")

    style = LATEX / "pct.sty"
    if not style.is_file():
        failures.append("Missing latex/pct.sty")
        style_text = ""
    else:
        style_text = style.read_text(encoding="utf-8")
    for macro in (r"\ket", r"\bra", r"\braket", r"\InKet", r"\OutBra", r"\PCT"):
        if macro not in style_text:
            failures.append(f"pct.sty is missing required notation macro {macro}")
    for environment in ("theorem", "definition", "lemma", "epigraph"):
        if not re.search(rf"\\new(?:theorem|environment)\s*\{{{environment}\}}", style_text):
            failures.append(f"pct.sty is missing required environment {environment}")
    if r"\renewcommand{\theequation}{\thesection-\arabic{equation}}" not in style_text:
        failures.append("pct.sty does not set source-style chapter equation tags")

    labels: dict[str, str] = {}
    assembled = ""
    native_findings: list[str] = []
    support_paths = sorted(
        path.relative_to(LATEX).as_posix()
        for path in (LATEX / "figures").glob("*.tex")
        if path.is_file()
    )
    census_paths = list(EXPECTED_CHUNKS) + support_paths
    scaffold_paths = ("master.tex", "pct.sty", "jheppub.sty")
    for relative in list(census_paths) + list(scaffold_paths):
        path = LATEX / relative
        if not path.is_file():
            native_findings.append(f"{relative}: required native input is missing")
            continue
        text = path.read_text(encoding="utf-8")
        if FORBIDDEN_SOURCE_IMPORT.search(text):
            native_findings.append(f"{relative}: facsimile/source import found")
        if PLACEHOLDER.search(text):
            native_findings.append(f"{relative}: unresolved placeholder found")
    for relative in census_paths:
        path = LATEX / relative
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        assembled += "\n" + text
        if relative in EXPECTED_CHUNKS:
            native = text_without_comments(text).strip()
            if len(native) < 32:
                native_findings.append(f"{relative}: native content is absent or too short")
            if not MARKER.search(text):
                native_findings.append(f"{relative}: no PCT-SOURCE marker")
        for line_number, line in enumerate(text.splitlines(), start=1):
            for match in LABEL.finditer(uncommented(line)):
                label = match.group(1)
                prior = labels.get(label)
                if prior:
                    native_findings.append(
                        f"{relative}:{line_number}: duplicate label {label!r}; first at {prior}"
                    )
                else:
                    labels[label] = f"{relative}:{line_number}"

    failures.extend(native_findings)
    audit_environment_nesting(assembled, failures)

    for relative in EXPECTED_CHUNKS:
        if not relative.endswith("bibliography.tex"):
            continue
        path = LATEX / relative
        if path.is_file():
            text = text_without_comments(path.read_text(encoding="utf-8"))
            if not BIB_ENTRY.search(text):
                failures.append(f"{relative}: bibliography has no native bibliography entries")

    index = LATEX / "backmatter/index.tex"
    if index.is_file():
        index_text = text_without_comments(index.read_text(encoding="utf-8"))
        if "\\begin{theindex}" not in index_text and "\\index{" not in index_text:
            failures.append("backmatter/index.tex has no structured native index")

    references = set(REFERENCE.findall(text_without_comments(assembled)))
    unresolved = sorted(reference for reference in references if reference not in labels)
    if unresolved:
        message = "Static reference candidates not defined in native chunks: " + ", ".join(unresolved)
        (failures if args.strict else reviews).append(message)

    if args.strict:
        audit_page_ledger(failures)
        audit_notation_map(failures)
        review_dir = ROOT / "work" / "reviews"
        if not review_dir.is_dir() or not any(review_dir.iterdir()):
            failures.append("Missing packet review records under work/reviews")
        else:
            review_files = sorted(review_dir.rglob("*.md"))
            if not review_files:
                failures.append("No Markdown packet review records found under work/reviews")
            for path in review_files:
                if not path.is_file():
                    continue
                text = path.read_text(encoding="utf-8")
                blockers = re.findall(
                    r"^Unresolved blockers:\s*(.+?)\s*$", text, re.MULTILINE
                )
                if not blockers:
                    failures.append(
                        f"{path.relative_to(ROOT)}: missing 'Unresolved blockers:' disposition"
                    )
                elif any(value.strip().lower() != "none" for value in blockers):
                    failures.append(f"{path.relative_to(ROOT)}: unresolved review item")

    print(f"Native chunk set: {len(EXPECTED_CHUNKS) - len(missing_chunks)}/{len(EXPECTED_CHUNKS)} present")
    print(f"Assembly inputs: {len(assembly)}")
    print(f"Native labels: {len(labels)}")
    if reviews:
        print("PROJECT REVIEW ITEMS")
        for item in reviews:
            print(f"  - {item}")
    if failures:
        print("PROJECT AUDIT FAILURES", file=sys.stderr)
        for failure in failures:
            print(f"  - {failure}", file=sys.stderr)
        if args.strict:
            return 1
        print("Draft mode: project findings are reported and do not stop the pilot build.")
    else:
        print("Project audit passed for the current draft state.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
