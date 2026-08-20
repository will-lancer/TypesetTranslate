#!/usr/bin/env python3
"""Audit the frozen PCT source and native provenance markers.

The scan is the authority for the source identity.  The native transcription
must cite the scan page that supplied each substantive unit.  Draft mode emits
findings so work can start before all packets exist; strict mode turns those
findings into release failures.
"""

from __future__ import annotations

import argparse
import hashlib
import re
import subprocess
import sys
from pathlib import Path

from audit_release_pipeline import review_provenance_failures


ROOT = Path(__file__).resolve().parents[1]
LATEX = ROOT / "latex"
SOURCE = ROOT.parents[2] / "origPapers" / "pct_spin_statistics_all_that.pdf"
MANIFEST = ROOT / "SOURCE_MANIFEST.yaml"
EXPECTED_SHA256 = "44fadba731cafe7f009d4e561372febb3597e1f2a4819346ce2efd16befcb889"
EXPECTED_PAGES = 221

EXPECTED_CHUNKS = [
    "frontmatter/copyright.tex",
    "frontmatter/preface.tex",
    "frontmatter/introduction.tex",
    "chapters/chapter01/opening.tex",
    "chapters/chapter01/sec1_1.tex",
    "chapters/chapter01/sec1_2.tex",
    "chapters/chapter01/sec1_3.tex",
    "chapters/chapter01/sec1_4.tex",
    "chapters/chapter01/bibliography.tex",
    "chapters/chapter02/opening.tex",
    "chapters/chapter02/sec2_1.tex",
    "chapters/chapter02/sec2_2.tex",
    "chapters/chapter02/sec2_3.tex",
    "chapters/chapter02/sec2_4.tex",
    "chapters/chapter02/sec2_5.tex",
    "chapters/chapter02/sec2_6.tex",
    "chapters/chapter02/bibliography.tex",
    "chapters/chapter03/opening.tex",
    "chapters/chapter03/sec3_1.tex",
    "chapters/chapter03/sec3_2.tex",
    "chapters/chapter03/sec3_3.tex",
    "chapters/chapter03/sec3_4.tex",
    "chapters/chapter03/sec3_5.tex",
    "chapters/chapter03/bibliography.tex",
    "chapters/chapter04/opening.tex",
    "chapters/chapter04/sec4_1.tex",
    "chapters/chapter04/sec4_2.tex",
    "chapters/chapter04/sec4_3.tex",
    "chapters/chapter04/sec4_4.tex",
    "chapters/chapter04/sec4_5.tex",
    "chapters/chapter04/sec4_6.tex",
    "chapters/chapter04/bibliography.tex",
    "appendix/constructive.tex",
    "appendix/local-algebras.tex",
    "appendix/bibliography.tex",
    "backmatter/index.tex",
]

MARKER = re.compile(
    r"^\s*%\s*PCT-SOURCE:\s*"
    r"pdf=(?P<pdf>\d+)\s+"
    r"print=(?P<printed>[A-Za-z0-9_.-]+)\s+"
    r"kind=(?P<kind>[A-Za-z0-9_.-]+)"
    r"(?:\s+id=(?P<identifier>[^\s]+))?\s*$",
    re.MULTILINE,
)
FORBIDDEN = re.compile(
    r"\\(?:usepackage|RequirePackage)\s*\{\s*pdfpages\s*\}|"
    r"\\(?:includepdf|facsimilepages|frontmatterpages)\b|"
    r"(?:source-pages|origPapers|pct_spin_statistics_all_that\.pdf|"
    r"facsimile|scan[-_]?page)",
    re.IGNORECASE,
)
PLACEHOLDER = re.compile(
    r"\b(?:TODO|FIXME|TBD|PLACEHOLDER|TRANSCRIBE|INSERT\s+(?:TEXT|EQUATION)|"
    r"PCT[-_ ]?(?:QUERY|REVIEW)|SOURCE[-_ ]?QUERY|MISSING\s+CHUNK)\b",
    re.IGNORECASE,
)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def pdf_page_count(path: Path) -> int | None:
    try:
        result = subprocess.run(
            ["pdfinfo", str(path)],
            check=True,
            capture_output=True,
            text=True,
        )
    except (FileNotFoundError, subprocess.CalledProcessError):
        return None
    match = re.search(r"^Pages:\s+(\d+)\s*$", result.stdout, re.MULTILINE)
    return int(match.group(1)) if match else None


def content_without_comments(text: str) -> str:
    return "\n".join(re.split(r"(?<!\\)%", line, maxsplit=1)[0] for line in text.splitlines())


def audit_manifest(failures: list[str]) -> None:
    """Keep the checked source identity in sync with the release manifest."""

    if not MANIFEST.is_file():
        failures.append(f"Missing source manifest: {MANIFEST.name}")
        return
    text = MANIFEST.read_text(encoding="utf-8")
    hash_match = re.search(r"^\s*sha256:\s*([0-9a-f]{64})\s*$", text, re.MULTILINE)
    if hash_match is None:
        failures.append("SOURCE_MANIFEST.yaml has no canonical sha256 field")
    elif hash_match.group(1) != EXPECTED_SHA256:
        failures.append(
            "SOURCE_MANIFEST.yaml sha256 differs from the frozen authority: "
            f"expected {EXPECTED_SHA256}, got {hash_match.group(1)}"
        )
    page_match = re.search(r"^\s*physical_pdf_pages:\s*(\d+)\s*$", text, re.MULTILINE)
    if page_match is None:
        failures.append("SOURCE_MANIFEST.yaml has no physical_pdf_pages field")
    elif int(page_match.group(1)) != EXPECTED_PAGES:
        failures.append(
            "SOURCE_MANIFEST.yaml physical_pdf_pages differs from the frozen authority: "
            f"expected {EXPECTED_PAGES}, got {page_match.group(1)}"
        )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--strict", action="store_true")
    args = parser.parse_args()

    failures: list[str] = []
    reviews: list[str] = []
    audit_manifest(failures)
    failures.extend(
        review_provenance_failures(
            root=ROOT,
            provenance_path=ROOT / "review-provenance.json",
            require_pdf=False,
        )
    )

    if not SOURCE.is_file():
        failures.append(f"Missing canonical source PDF: {SOURCE}")
    else:
        actual_hash = sha256(SOURCE)
        if actual_hash != EXPECTED_SHA256:
            failures.append(
                f"Source SHA-256 mismatch: expected {EXPECTED_SHA256}, got {actual_hash}"
            )
        actual_pages = pdf_page_count(SOURCE)
        if actual_pages is None:
            failures.append("Could not read the canonical source page count with pdfinfo")
        elif actual_pages != EXPECTED_PAGES:
            failures.append(
                f"Source page-count mismatch: expected {EXPECTED_PAGES}, got {actual_pages}"
            )

    present: list[tuple[str, Path, str]] = []
    missing = []
    for relative in EXPECTED_CHUNKS:
        path = LATEX / relative
        if not path.is_file():
            missing.append(relative)
            continue
        text = path.read_text(encoding="utf-8")
        present.append((relative, path, text))

        native = content_without_comments(text).strip()
        if len(native) < 32:
            failures.append(f"{relative}: native content is absent or too short")

        markers = list(MARKER.finditer(text))
        if not markers:
            failures.append(f"{relative}: no % PCT-SOURCE marker")
        for marker in markers:
            page = int(marker.group("pdf"))
            if not 1 <= page <= EXPECTED_PAGES:
                failures.append(f"{relative}: source marker has invalid PDF page {page}")

        for line_number, line in enumerate(text.splitlines(), start=1):
            if FORBIDDEN.search(line):
                failures.append(
                    f"{relative}:{line_number}: source scan/facsimile import is forbidden"
                )
            if PLACEHOLDER.search(line):
                failures.append(f"{relative}:{line_number}: unresolved placeholder text")

    if missing:
        message = f"Missing native chunks ({len(missing)}): " + ", ".join(missing)
        (failures if args.strict else reviews).append(message)

    all_native = "\n".join(text for _, _, text in present)
    unique_pages = {
        int(match.group("pdf")) for match in MARKER.finditer(all_native)
    }
    if present and not unique_pages:
        failures.append("Native transcription has no parseable source pages")
    if len(unique_pages) < len(present) and present:
        reviews.append(
            "Several native chunks share source pages; verify packet boundaries against the scan"
        )

    print(f"Canonical source: {SOURCE}")
    if SOURCE.is_file():
        print(f"Source SHA-256: {sha256(SOURCE)}")
        print(f"Source pages: {pdf_page_count(SOURCE) or 'unknown'}")
    print(f"Native chunks present: {len(present)}/{len(EXPECTED_CHUNKS)}")
    print(f"Distinct marked PDF pages: {len(unique_pages)}")

    if reviews:
        print("SOURCE REVIEW ITEMS")
        for item in reviews:
            print(f"  - {item}")

    if failures:
        print("SOURCE AUDIT FAILURES", file=sys.stderr)
        for failure in failures:
            print(f"  - {failure}", file=sys.stderr)
        if args.strict:
            return 1
        print("Draft mode: source failures are reported and do not stop the pilot build.")
    else:
        print("Source audit passed for the current draft state.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
