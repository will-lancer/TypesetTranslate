#!/usr/bin/env python3
"""Audit and finalize the evidence for a native PCT release.

The existing build script performs the compilation.  This script owns the
post-compile evidence contract.  It checks the review-coverage ledger,
compiled input trace, diagnostics, fonts, raster objects, rendered-page
inspection, export identity, and the populated release record.  ``finalize``
can perform the staged export after its preflight passes.

The input-tree digest is a content digest.  It includes source and tooling
files in this edition directory while excluding generated build output under
``work/``, TeX auxiliary output, PDFs, and this release record.  The mutable
``status`` values in ``review-coverage.json`` are normalized to ``pending``
before hashing, so finalization can close the Pass 4 gate without changing the
digest cited by the release record.  It therefore cannot depend on the record
that reports the digest.

Finalization owns two narrow state transitions. The writing-audit record
``pass-4-release`` and the release-evidence record ``export-byte-identity`` may
be pending while preflight runs. The finalizer creates and verifies the export,
writes the release records, and closes both statuses before the last audit.
Every other required record must already be passing.
"""

from __future__ import annotations

import argparse
import datetime as _datetime
import filecmp
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any, Iterable, Sequence


ROOT = Path(__file__).resolve().parents[1]
LATEX = ROOT / "latex"
MASTER_TEX = LATEX / "master.tex"
MASTER_LOG = LATEX / "master.log"
MASTER_FLS = LATEX / "master.fls"
MASTER_PDF = LATEX / "master.pdf"
EXPORT_DIR = ROOT / ".." / ".." / "pct-spin-statistics-all-that"
EXPORT_PDF = EXPORT_DIR / "pct-spin-statistics-all-that.pdf"
SOURCE_PDF = ROOT.parents[2] / "origPapers" / "pct_spin_statistics_all_that.pdf"
SOURCE_MANIFEST = ROOT / "SOURCE_MANIFEST.yaml"
COVERAGE_MANIFEST = ROOT / "review-coverage.json"
WARNING_ALLOWLIST = ROOT / "release-warning-allowlist.json"
IMAGE_ALLOWLIST = ROOT / "release-image-allowlist.json"
RELEASE_RECORD = ROOT / "RELEASE_VERIFICATION.md"
REVIEW_PROVENANCE = ROOT / "review-provenance.json"
VISUAL_REVIEWER_MAP = ROOT / "visual-reviewer-map.json"
RENDERED_DIR = ROOT / "work" / "rendered-output"
RENDER_MANIFEST = RENDERED_DIR / "manifest.jsonl"
INSPECTION_MANIFEST = ROOT / "work" / "reviews" / "page-inspection.jsonl"
REPRODUCIBILITY_ENV = ROOT / "reproducible-build.env"
REPRODUCIBILITY_EVIDENCE = ROOT / "work" / "reviews" / "reproducibility.json"

EXPECTED_SOURCE_SHA256 = "44fadba731cafe7f009d4e561372febb3597e1f2a4819346ce2efd16befcb889"
EXPECTED_SOURCE_PAGES = 221
EXPECTED_COVERAGE_COUNTS = {
    "source_ranges": 17,
    "figures": 13,
    "global_audits": 4,
    "required_pass_records": 4,
    "release_evidence_requirements": 4,
}
EXPECTED_REPRODUCIBILITY_ENV = {
    "SOURCE_DATE_EPOCH": "946684800",
    "FORCE_SOURCE_DATE": "1",
    "TZ": "UTC",
    "LC_ALL": "C",
}

SOURCE_PAGE_RENDER_SPEC = {
    "directory": "work/source-pages",
    "filename_pattern": "pdf-%03d.jpg",
    "renderer": "pdftoppm",
    "dpi": 180,
    "jpeg_quality": 92,
    "command_template": "pdftoppm -jpeg -jpegopt quality=92 -r 180 -f {page} -l {page} source.pdf prefix",
}

REVIEW_PROVENANCE_EXCLUDED = {
    "work/reviews/PASS_4_RELEASE.md",
    "work/reviews/reproducibility.json",
}

EXPECTED_NATIVE_TEX = (
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
)
EXPECTED_FIGURES = (
    "figures/fig1_1.tex",
    "figures/fig1_2.tex",
    "figures/fig1_3.tex",
    "figures/fig2_1.tex",
    "figures/fig2_2.tex",
    "figures/fig2_3.tex",
    "figures/fig2_4.tex",
    "figures/fig2_5.tex",
    "figures/fig2_6.tex",
    "figures/fig2_7.tex",
    "figures/figA1.tex",
    "figures/figA2.tex",
    "figures/figA3.tex",
)
EXPECTED_LOCAL_INPUTS = ("master.tex", "jheppub.sty", "pct.sty") + EXPECTED_NATIVE_TEX + EXPECTED_FIGURES
EXPECTED_FIGURE_PAGES = {
    "1-1": 23,
    "1-2": 25,
    "1-3": 38,
    "2-1": 70,
    "2-2": 77,
    "2-3": 84,
    "2-4": 85,
    "2-5": 86,
    "2-6": 87,
    "2-7": 91,
    "A-1": 196,
    "A-2": 200,
    "A-3": 210,
}
REQUIRED_COMMANDS = (
    "python3",
    "latexmk",
    "tesseract",
    "rg",
    "pdfinfo",
    "pdffonts",
    "pdftotext",
    "pdfimages",
    "pdftoppm",
    "gs",
    "shasum",
    "cmp",
)

FORBIDDEN_FLS_TEXT = re.compile(
    r"(?:facsimile|source-pages|origPapers|pct_spin_statistics_all_that\.pdf|"
    r"pdfpages|includepdf)",
    re.IGNORECASE,
)
FORBIDDEN_NATIVE_TEXT = re.compile(
    r"\\(?:usepackage|RequirePackage)\s*\{\s*pdfpages\s*\}|"
    r"\\(?:includepdf|facsimilepages|frontmatterpages)\b|"
    r"(?:source-pages|origPapers|pct_spin_statistics_all_that\.pdf|facsimile|scan[-_]?page)",
    re.IGNORECASE,
)

# A warning is a diagnostic line, including layout diagnostics that do not
# contain the word "warning".  The release allowlist is the only way to
# admit one.
WARNING_LINE = re.compile(
    r"(?:\bwarning\b|Overfull\\[hv]box|Underfull\\[hv]box|Missing character)",
    re.IGNORECASE,
)
PLACEHOLDER = re.compile(
    r"(?:\[(?:populate|pending|record|tbd|todo|fill|insert)[^\]]*\]|"
    r"\b(?:TBD|TODO|FIXME|PLACEHOLDER)\b)",
    re.IGNORECASE,
)
NATIVE_PLACEHOLDER = re.compile(
    r"\b(?:TODO|FIXME|TBD|PLACEHOLDER|TRANSCRIBE|INSERT\s+(?:TEXT|EQUATION)|"
    r"PCT[-_ ]?(?:QUERY|REVIEW)|SOURCE[-_ ]?QUERY|MISSING\s+CHUNK)\b",
    re.IGNORECASE,
)
SHA256 = re.compile(r"^[0-9a-f]{64}$")


def display_path(path: Path, root: Path = ROOT) -> str:
    try:
        return path.resolve().relative_to(root.resolve()).as_posix()
    except ValueError:
        return str(path)


def is_generated_file(path: Path) -> bool:
    generated_suffixes = {
        ".aux",
        ".bbl",
        ".bcf",
        ".blg",
        ".dvi",
        ".fdb_latexmk",
        ".fls",
        ".idx",
        ".ilg",
        ".ind",
        ".log",
        ".nav",
        ".out",
        ".pdf",
        ".run.xml",
        ".snm",
        ".synctex",
        ".synctex.gz",
        ".toc",
        ".vrb",
    }
    name = path.name.lower()
    return any(name.endswith(suffix) for suffix in generated_suffixes)


def input_content_sha256(path: Path, root: Path = ROOT) -> str:
    """Hash one input file, normalizing only mutable coverage statuses."""

    if path.resolve() == (root / "review-coverage.json").resolve():
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            data = None
        if data is not None:
            def normalize_statuses(value: Any) -> Any:
                if isinstance(value, dict):
                    return {
                        key: "pending" if key == "status" else normalize_statuses(item)
                        for key, item in value.items()
                    }
                if isinstance(value, list):
                    return [normalize_statuses(item) for item in value]
                return value

            canonical = json.dumps(
                normalize_statuses(data),
                ensure_ascii=False,
                sort_keys=True,
                separators=(",", ":"),
            ).encode("utf-8")
            return hashlib.sha256(canonical).hexdigest()
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def run_checked(command: Sequence[str]) -> subprocess.CompletedProcess[str]:
    """Run a diagnostic command without allowing a shell interpretation."""

    return subprocess.run(command, capture_output=True, text=True, check=False)


def dependency_failures() -> list[str]:
    return [f"Missing required dependency: {name}" for name in REQUIRED_COMMANDS if shutil.which(name) is None]


def load_json(path: Path) -> tuple[Any | None, list[str]]:
    if not path.is_file() or path.is_symlink():
        return None, [f"Missing JSON data file: {display_path(path)}"]
    try:
        return json.loads(path.read_text(encoding="utf-8")), []
    except json.JSONDecodeError as error:
        return None, [f"{display_path(path)} is invalid JSON: {error}"]


def iter_input_files(root: Path) -> Iterable[Path]:
    """Yield the deterministic, non-generated input tree in path order."""

    excluded_dirs = {".git", "__pycache__", "work"}
    excluded_names = {RELEASE_RECORD.name}
    paths: list[Path] = []
    for path in root.rglob("*"):
        if not path.is_file() or path.is_symlink():
            continue
        relative = path.relative_to(root)
        if any(part in excluded_dirs for part in relative.parts[:-1]):
            continue
        if path.name in excluded_names:
            continue
        if is_generated_file(path):
            continue
        paths.append(path)
    yield from sorted(paths, key=lambda path: path.relative_to(root).as_posix())


def deterministic_input_tree_hash(root: Path = ROOT) -> tuple[str, list[str]]:
    """Return a deterministic digest and the relative paths included in it.

    Each line commits both the relative POSIX path and the content hash.  File
    order is lexical and file metadata never enters the digest.  The caller
    receives the paths for release-record diagnostics and tests.
    """

    entries: list[str] = []
    for path in iter_input_files(root):
        relative = path.relative_to(root).as_posix()
        entries.append(f"{input_content_sha256(path, root)}  {relative}\n")
    digest = hashlib.sha256("".join(entries).encode("utf-8")).hexdigest()
    return digest, [line.rstrip("\n") for line in entries]


def native_input_hash(root: Path = ROOT) -> str | None:
    """Hash the native manuscript inputs that source reviews inspect.

    Generated files and review records are deliberately outside this digest.
    A review provenance record stores the result, so a later manuscript change
    invalidates the review snapshot before release closeout.
    """

    entries: list[str] = []
    for relative in sorted(EXPECTED_LOCAL_INPUTS):
        path = root / "latex" / relative
        if not path.is_file() or path.is_symlink():
            return None
        entries.append(f"{sha256(path)}  latex/{relative}\n")
    return hashlib.sha256("".join(entries).encode("utf-8")).hexdigest()


def _source_pdf_path(root: Path = ROOT) -> Path:
    return root.parents[2] / "origPapers" / "pct_spin_statistics_all_that.pdf"


def _master_pdf_path(root: Path = ROOT) -> Path:
    return root / "latex" / "master.pdf"


def _aggregate_file_hash(root: Path, paths: Iterable[Path]) -> tuple[str, list[str]]:
    """Hash a path/content list with stable relative names."""

    entries: list[str] = []
    missing: list[str] = []
    for path in sorted(paths, key=lambda item: item.relative_to(root).as_posix()):
        relative = path.relative_to(root).as_posix()
        if not path.is_file() or path.is_symlink():
            missing.append(relative)
            entries.append(f"MISSING  {relative}\n")
            continue
        entries.append(f"{sha256(path)}  {relative}\n")
    return hashlib.sha256("".join(entries).encode("utf-8")).hexdigest(), missing


def review_record_paths(root: Path = ROOT) -> list[Path]:
    """Return the human and machine review files bound by provenance.

    Pass 4 and reproducibility evidence are generated by the finalizer or the
    build checker and remain covered by their dedicated validators.
    """

    review_root = root / "work" / "reviews"
    if not review_root.is_dir():
        return []
    return [
        path
        for path in review_root.rglob("*")
        if (path.is_file() or path.is_symlink())
        and path.relative_to(root).as_posix() not in REVIEW_PROVENANCE_EXCLUDED
    ]


def required_review_record_failures(
    root: Path = ROOT,
    coverage_path: Path | None = None,
) -> list[str]:
    """Require every coverage-declared review record bound by provenance."""

    manifest = coverage_path or (root / "review-coverage.json")
    data, failures = load_json(manifest)
    if failures:
        return failures
    if not isinstance(data, dict):
        return ["review-coverage.json must be an object"]
    for group, records in _record_groups(data):
        for index, record in enumerate(records, 1):
            if not isinstance(record, dict):
                continue
            review_files = record.get("review_files")
            if not isinstance(review_files, list):
                continue
            for raw_path in review_files:
                if not isinstance(raw_path, str) or not raw_path.strip():
                    continue
                if raw_path in REVIEW_PROVENANCE_EXCLUDED:
                    continue
                candidate = root / raw_path
                if not candidate.is_file() or candidate.is_symlink():
                    failures.append(
                        f"review provenance requires {group}[{index}] record: {raw_path}"
                    )
    return failures


def source_page_hash(root: Path = ROOT) -> tuple[str | None, list[str], int]:
    """Hash the complete 180-dpi source-page review image set."""

    directory = root / SOURCE_PAGE_RENDER_SPEC["directory"]
    expected = {
        f"pdf-{page:03d}.jpg"
        for page in range(1, EXPECTED_SOURCE_PAGES + 1)
    }
    if not directory.is_dir() or directory.is_symlink():
        return None, [SOURCE_PAGE_RENDER_SPEC["directory"]], 0
    actual = {path.name for path in directory.iterdir()}
    failures: list[str] = []
    for name in sorted(expected - actual):
        failures.append(f"missing source review image: {directory.relative_to(root)}/{name}")
    for name in sorted(actual - expected):
        failures.append(f"unexpected source review image: {directory.relative_to(root)}/{name}")
    paths = [directory / name for name in sorted(expected)]
    digest, missing = _aggregate_file_hash(root, paths)
    failures.extend(f"missing source review image: {item}" for item in missing)
    for path in paths:
        if not path.is_file() or path.is_symlink():
            continue
        try:
            if path.stat().st_size == 0:
                failures.append(f"empty source review image: {path.relative_to(root)}")
                continue
            with path.open("rb") as handle:
                header = handle.read(3)
                handle.seek(-2, os.SEEK_END)
                trailer = handle.read(2)
        except (OSError, ValueError) as error:
            failures.append(f"unreadable source review image {path.relative_to(root)}: {error}")
            continue
        if header != b"\xff\xd8\xff" or trailer != b"\xff\xd9":
            failures.append(f"malformed JPEG source review image: {path.relative_to(root)}")
    return digest, failures, len(actual)


def source_page_rerender_failures(
    root: Path = ROOT,
    source_pages_dir: Path | None = None,
) -> list[str]:
    """Rerender every canonical source page and compare bytes with the review set."""

    source_pdf = _source_pdf_path(root)
    if not source_pdf.is_file() or source_pdf.is_symlink():
        return [f"Missing canonical source PDF for source-page rerender: {source_pdf}"]
    stored_dir = source_pages_dir or (root / SOURCE_PAGE_RENDER_SPEC["directory"])
    if not stored_dir.is_dir() or stored_dir.is_symlink():
        return [f"Missing source review image directory for rerender: {stored_dir}"]

    expected = {
        f"pdf-{page:03d}.jpg"
        for page in range(1, EXPECTED_SOURCE_PAGES + 1)
    }
    failures: list[str] = []
    with tempfile.TemporaryDirectory(prefix="pct-source-rerender-") as temporary:
        output_dir = Path(temporary)
        output_prefix = output_dir / "pdf"
        command = [
            SOURCE_PAGE_RENDER_SPEC["renderer"],
            "-jpeg",
            "-jpegopt",
            f"quality={SOURCE_PAGE_RENDER_SPEC['jpeg_quality']}",
            "-r",
            str(SOURCE_PAGE_RENDER_SPEC["dpi"]),
            "-f",
            "1",
            "-l",
            str(EXPECTED_SOURCE_PAGES),
            str(source_pdf),
            str(output_prefix),
        ]
        try:
            result = run_checked(command)
        except OSError as error:
            return [f"Source-page rerender could not run: {error}"]
        if result.returncode != 0:
            failures.append(f"Source-page rerender exited with status {result.returncode}")
        if (result.stderr or "").strip():
            failures.append("Source-page rerender emitted stderr diagnostics")
        generated = {path.name for path in output_dir.iterdir()}
        if generated != expected:
            failures.append(
                f"Source-page rerender set differs from expected pages; missing={sorted(expected - generated)}, extra={sorted(generated - expected)}"
            )
        for name in sorted(expected & generated):
            rendered = output_dir / name
            stored = stored_dir / name
            if not stored.is_file() or stored.is_symlink():
                failures.append(f"Missing stored source review image during rerender: {stored}")
                continue
            if not filecmp.cmp(rendered, stored, shallow=False):
                failures.append(f"Source-page rerender differs from stored review image: {stored}")
    return failures


def review_pdf_hash_failures(root: Path = ROOT) -> list[str]:
    """Require every page-inspection record to name the current PDF hash."""

    pdf_path = _master_pdf_path(root)
    if not pdf_path.is_file() or pdf_path.is_symlink():
        return ["Cannot bind page-inspection reviews to a missing master.pdf"]
    current_pdf_hash = sha256(pdf_path)
    inspection_paths = [root / "work" / "reviews" / "page-inspection.jsonl"]
    failures: list[str] = []
    mismatched: list[int] = []
    for path in inspection_paths:
        records, read_failures = read_jsonl(path)
        failures.extend(read_failures)
        for index, record in enumerate(records, 1):
            if record.get("pdf_sha256") != current_pdf_hash:
                page = record.get("pdf_page")
                if isinstance(page, int) and not isinstance(page, bool):
                    mismatched.append(page)
                else:
                    failures.append(f"{display_path(path)}:{index}: page-inspection record has no PDF page")
    if mismatched:
        unique_pages = sorted(set(mismatched))
        if unique_pages == list(range(unique_pages[0], unique_pages[-1] + 1)):
            page_summary = f"{unique_pages[0]}-{unique_pages[-1]}"
        else:
            page_summary = repr(unique_pages[:12])
        failures.append(
            f"page-inspection PDF checksum mismatch for {len(mismatched)} records; current master.pdf is required (pages={page_summary})"
        )
    return failures


def review_provenance_failures(
    root: Path = ROOT,
    provenance_path: Path = REVIEW_PROVENANCE,
    *,
    require_pdf: bool = True,
) -> list[str]:
    """Validate review/source provenance against the current project state."""

    data, failures = load_json(provenance_path)
    if failures:
        return failures
    if not isinstance(data, dict) or data.get("schema_version") != 1:
        failures.append("review-provenance.json must be a schema_version 1 object")
        return failures

    source_pdf = _source_pdf_path(root)
    if not source_pdf.is_file() or source_pdf.is_symlink():
        failures.append(f"Missing canonical source PDF for review provenance: {source_pdf}")
    else:
        current_source = sha256(source_pdf)
        if data.get("source_sha256") != current_source:
            failures.append("review-provenance.json source SHA-256 does not match the canonical source")
        if current_source != EXPECTED_SOURCE_SHA256:
            failures.append("canonical source SHA-256 differs from the frozen authority")

    current_native = native_input_hash(root)
    if current_native is None:
        failures.append("review-provenance.json cannot hash the complete native input set")
    elif data.get("native_input_sha256") != current_native:
        failures.append("review-provenance.json native-input SHA-256 does not match the current manuscript")

    current_pdf = _master_pdf_path(root)
    if require_pdf:
        if not current_pdf.is_file() or current_pdf.is_symlink():
            failures.append("review-provenance.json requires a current latex/master.pdf")
        elif data.get("master_pdf_sha256") != sha256(current_pdf):
            failures.append("review-provenance.json PDF SHA-256 does not match the current master.pdf")

    reviewer_map = root / "visual-reviewer-map.json"
    if not reviewer_map.is_file() or reviewer_map.is_symlink():
        failures.append("Missing visual reviewer authorization map: visual-reviewer-map.json")
    elif data.get("visual_reviewer_map_sha256") != sha256(reviewer_map):
        failures.append("review-provenance.json visual reviewer map SHA-256 is stale")

    source_pages = data.get("source_pages")
    if not isinstance(source_pages, dict):
        failures.append("review-provenance.json has no source_pages object")
    else:
        for key, expected in SOURCE_PAGE_RENDER_SPEC.items():
            if source_pages.get(key) != expected:
                failures.append(f"review-provenance.json source_pages.{key} is not {expected!r}")
        source_digest, source_page_failures, source_count = source_page_hash(root)
        failures.extend(source_page_failures)
        if source_pages.get("count") != EXPECTED_SOURCE_PAGES:
            failures.append("review-provenance.json source_pages.count must be 221")
        if source_pages.get("source_sha256") != data.get("source_sha256"):
            failures.append("review-provenance.json source-page authority hash differs from source_sha256")
        if source_digest is not None and source_pages.get("sha256") != source_digest:
            failures.append("review-provenance.json source-page SHA-256 does not match the current image set")
        if source_count != EXPECTED_SOURCE_PAGES:
            failures.append(f"source review image count is {source_count}; expected {EXPECTED_SOURCE_PAGES}")
        failures.extend(source_page_rerender_failures(root))

    review_paths = review_record_paths(root)
    failures.extend(required_review_record_failures(root))
    if not review_paths:
        failures.append("review-provenance.json has no review records to bind")
    review_digest, review_missing = _aggregate_file_hash(root, review_paths)
    failures.extend(f"missing review record: {item}" for item in review_missing)
    if data.get("review_records_sha256") != review_digest:
        failures.append("review-provenance.json review-record SHA-256 does not match current review files")
    if require_pdf:
        failures.extend(review_pdf_hash_failures(root))
    return failures


def parse_source_manifest(failures: list[str]) -> str | None:
    if not SOURCE_MANIFEST.is_file() or SOURCE_MANIFEST.is_symlink():
        failures.append("Missing SOURCE_MANIFEST.yaml")
        return None
    text = SOURCE_MANIFEST.read_text(encoding="utf-8")
    match = re.search(r"^\s*sha256:\s*([0-9a-f]{64})\s*$", text, re.MULTILINE)
    if match is None:
        failures.append("SOURCE_MANIFEST.yaml has no canonical source SHA-256")
        return None
    if match.group(1) != EXPECTED_SOURCE_SHA256:
        failures.append(
            "SOURCE_MANIFEST.yaml source SHA-256 differs from the frozen authority"
        )
    page_match = re.search(r"^\s*physical_pdf_pages:\s*(\d+)\s*$", text, re.MULTILINE)
    if page_match is None or int(page_match.group(1)) != EXPECTED_SOURCE_PAGES:
        failures.append("SOURCE_MANIFEST.yaml must record 221 physical source pages")
    if not SOURCE_PDF.is_file() or SOURCE_PDF.is_symlink():
        failures.append(f"Missing canonical source PDF: {SOURCE_PDF}")
        return match.group(1)
    actual = sha256(SOURCE_PDF)
    if actual != EXPECTED_SOURCE_SHA256:
        failures.append(
            f"Canonical source SHA-256 mismatch: expected {EXPECTED_SOURCE_SHA256}, got {actual}"
        )
    return match.group(1)


def _record_groups(manifest: dict[str, Any]) -> Iterable[tuple[str, list[Any]]]:
    for group in EXPECTED_COVERAGE_COUNTS:
        value = manifest.get(group)
        yield group, value if isinstance(value, list) else []


def coverage_failures(
    root: Path = ROOT,
    manifest_path: Path = COVERAGE_MANIFEST,
    allow_pending_ids: set[str] | None = None,
) -> list[str]:
    data, failures = load_json(manifest_path)
    if failures:
        return failures
    if not isinstance(data, dict):
        return ["review-coverage.json must contain an object"]
    if data.get("schema_version") != 1:
        failures.append("review-coverage.json schema_version must be 1")
    if data.get("project") != "pct_spin_statistics_all_that":
        failures.append("review-coverage.json has the wrong project identifier")
    if data.get("source_pdf_pages") != EXPECTED_SOURCE_PAGES:
        failures.append("review-coverage.json must declare 221 source PDF pages")

    seen_ids: set[str] = set()
    source_range_pages: set[int] = set()
    source_range_total = 0
    for group, records in _record_groups(data):
        expected_count = EXPECTED_COVERAGE_COUNTS[group]
        if len(records) != expected_count:
            failures.append(
                f"review-coverage.json {group} count is {len(records)}, expected {expected_count}"
            )
        for index, record in enumerate(records, 1):
            prefix = f"review-coverage.json {group}[{index}]"
            if not isinstance(record, dict):
                failures.append(f"{prefix} must be an object")
                continue
            identifier = record.get("id")
            if not isinstance(identifier, str) or not identifier.strip():
                failures.append(f"{prefix} has no nonempty id")
            elif identifier in seen_ids:
                failures.append(f"duplicate review-coverage id: {identifier}")
            else:
                seen_ids.add(identifier)
            if record.get("required") is not True:
                failures.append(f"{prefix} must have required: true")
            status = record.get("status")
            pending_release_record = status == "pending" and identifier in (allow_pending_ids or set())
            if status != "pass" and not (
                status == "pending" and identifier in (allow_pending_ids or set())
            ):
                failures.append(
                    f"{prefix} status is {status!r}; strict release requires 'pass'"
                )
            if group == "source_ranges":
                page_spec = record.get("pdf_pages")
                match = re.fullmatch(r"(\d{3})-(\d{3})", page_spec) if isinstance(page_spec, str) else None
                if match is None:
                    failures.append(f"{prefix} has no zero-padded PDF page range")
                else:
                    start, end = (int(value) for value in match.groups())
                    if start < 1 or end < start or end > EXPECTED_SOURCE_PAGES:
                        failures.append(f"{prefix} has an invalid PDF page range: {page_spec}")
                    source_range_total += end - start + 1
                    source_range_pages.update(range(start, end + 1))
            if group == "figures":
                identifier = record.get("id")
                source_page = record.get("source_pdf_page")
                native_file = record.get("native_file")
                if identifier not in EXPECTED_FIGURE_PAGES:
                    failures.append(f"{prefix} has an unknown canonical figure id: {identifier!r}")
                elif source_page != EXPECTED_FIGURE_PAGES[identifier]:
                    failures.append(
                        f"{prefix} source page differs from SOURCE_MANIFEST.yaml: expected {EXPECTED_FIGURE_PAGES[identifier]}, got {source_page!r}"
                    )
                if not isinstance(native_file, str) or not native_file.startswith("latex/"):
                    failures.append(f"{prefix} has no latex/ native figure path")
                elif not (root / native_file).is_file() or (root / native_file).is_symlink():
                    failures.append(f"{prefix} native figure file is missing: {native_file}")
            is_review_record = isinstance(record.get("review_files"), list)
            paths = record.get("review_files", record.get("evidence", []))
            if not isinstance(paths, list) or not paths:
                failures.append(f"{prefix} has no review/evidence paths")
                continue
            required_fields = record.get("required_fields")
            if required_fields is not None:
                if not isinstance(required_fields, list) or not required_fields or not all(
                    isinstance(field, str) and field.strip() for field in required_fields
                ):
                    failures.append(f"{prefix} has an invalid required_fields schema")
            for raw_path in paths:
                if not isinstance(raw_path, str) or not raw_path.strip():
                    failures.append(f"{prefix} contains an invalid review/evidence path")
                    continue
                candidate = (root / raw_path).resolve()
                try:
                    candidate.relative_to(root.resolve())
                except ValueError:
                    failures.append(f"{prefix} path escapes the edition root: {raw_path}")
                    continue
                if not candidate.is_file():
                    if not pending_release_record:
                        failures.append(f"{prefix} evidence file is missing: {raw_path}")
                    continue
                if is_review_record and candidate.suffix.lower() == ".md":
                    review_text = candidate.read_text(encoding="utf-8", errors="replace")
                    if not re.search(r"^Unresolved blockers:\s*none\s*$", review_text, re.MULTILINE):
                        failures.append(
                            f"{prefix} review file lacks the exact 'Unresolved blockers: none' disposition: {raw_path}"
                        )
                    if isinstance(required_fields, list):
                        for field in required_fields:
                            if isinstance(field, str) and field not in review_text:
                                failures.append(
                                    f"{prefix} review file lacks required field {field!r}: {raw_path}"
                                )
    if source_range_total != len(source_range_pages):
        failures.append("review-coverage.json source ranges overlap")
    if source_range_pages != set(range(3, 220)):
        failures.append(
            "review-coverage.json source ranges must partition PDF pages 003-219 exactly: "
            f"missing={sorted(set(range(3, 220)) - source_range_pages)}, "
            f"extra={sorted(source_range_pages - set(range(3, 220)))}"
        )
    return failures


def parse_fls_inputs(fls_path: Path) -> set[str]:
    """Read local INPUT paths from a recorder file.

    TeX writes both ``./foo`` and ``foo`` forms.  Absolute system paths are
    excluded; an absolute path beneath the recorder's PWD is retained as a
    local path.
    """

    if not fls_path.is_file() or fls_path.is_symlink():
        return set()
    pwd: Path | None = None
    raw_inputs: list[str] = []
    for line in fls_path.read_text(encoding="utf-8", errors="replace").splitlines():
        if line.startswith("PWD "):
            pwd = Path(line[4:].strip()).resolve()
        elif line.startswith("INPUT "):
            raw_inputs.append(line[6:].strip())
    result: set[str] = set()
    base = pwd or LATEX.resolve()
    for raw in raw_inputs:
        candidate = Path(raw)
        if candidate.is_absolute():
            try:
                relative = candidate.resolve().relative_to(base)
            except ValueError:
                continue
        else:
            relative = Path(raw)
        normalized = relative.as_posix()
        while normalized.startswith("./"):
            normalized = normalized[2:]
        if normalized and not normalized.startswith("../"):
            result.add(normalized)
    return result


def expected_local_inputs(coverage_path: Path = COVERAGE_MANIFEST) -> set[str]:
    expected = set(EXPECTED_LOCAL_INPUTS)
    data, failures = load_json(coverage_path)
    if failures or not isinstance(data, dict):
        return expected
    figures = data.get("figures", [])
    if isinstance(figures, list):
        for figure in figures:
            if isinstance(figure, dict) and isinstance(figure.get("native_file"), str):
                native_file = figure["native_file"]
                if native_file.startswith("latex/"):
                    native_file = native_file[len("latex/") :]
                expected.add(native_file)
    return expected


def compiled_input_failures(
    root: Path = ROOT,
    fls_path: Path = MASTER_FLS,
    coverage_path: Path = COVERAGE_MANIFEST,
) -> list[str]:
    failures: list[str] = []
    if not fls_path.is_file() or fls_path.is_symlink():
        return [f"Missing recorder file: {display_path(fls_path, root)}"]
    text = fls_path.read_text(encoding="utf-8", errors="replace")
    if FORBIDDEN_FLS_TEXT.search(text):
        failures.append("master.fls contains a source-scan or facsimile import marker")
    actual = parse_fls_inputs(fls_path)
    expected = expected_local_inputs(coverage_path)
    missing = sorted(expected - actual)
    for path in missing:
        failures.append(f"master.fls does not prove local input was compiled: {path}")
    for relative in sorted(expected):
        if not (LATEX / relative).is_file() or (LATEX / relative).is_symlink():
            failures.append(f"Expected compiled input is absent from the tree: latex/{relative}")
    return failures


def native_content_failures(root: Path = ROOT) -> list[str]:
    """Scan every expected local TeX/style input for placeholders and imports."""

    failures: list[str] = []
    for relative in sorted(expected_local_inputs()):
        path = LATEX / relative
        if not path.is_file() or path.is_symlink():
            failures.append(f"Expected native input is missing: latex/{relative}")
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        for line_number, line in enumerate(text.splitlines(), 1):
            if FORBIDDEN_NATIVE_TEXT.search(line):
                failures.append(f"Forbidden source/facsimile import in latex/{relative}:{line_number}")
            if NATIVE_PLACEHOLDER.search(line):
                failures.append(f"Placeholder remains in latex/{relative}:{line_number}")
    return failures


def _allowlist_patterns(path: Path, label: str) -> tuple[list[re.Pattern[str]], list[str]]:
    data, failures = load_json(path)
    if failures:
        return [], failures
    if not isinstance(data, dict) or data.get("schema_version") != 1:
        return [], [f"{label} must be a schema_version 1 object"]
    entries = data.get("allowed")
    if not isinstance(entries, list):
        return [], [f"{label}.allowed must be a list"]
    patterns: list[re.Pattern[str]] = []
    for index, entry in enumerate(entries, 1):
        if not isinstance(entry, dict):
            failures.append(f"{label}.allowed[{index}] must be an object")
            continue
        pattern = entry.get("pattern")
        reason = entry.get("reason")
        if not isinstance(pattern, str) or not pattern.strip():
            failures.append(f"{label}.allowed[{index}] has no pattern")
            continue
        if not isinstance(reason, str) or not reason.strip():
            failures.append(f"{label}.allowed[{index}] has no review reason")
        try:
            patterns.append(re.compile(pattern))
        except re.error as error:
            failures.append(f"{label}.allowed[{index}] has invalid regex: {error}")
    return patterns, failures


def warning_lines(log_text: str) -> list[str]:
    diagnostics: list[str] = []
    for line in log_text.splitlines():
        # TeX package metadata often says "info/warning/error" in prose.  It
        # is not a compiler diagnostic.  Actual package diagnostics use the
        # ``Package name Warning:`` form and remain covered.
        if re.match(r"^(?:Package|Class):\s", line):
            continue
        if WARNING_LINE.search(line):
            diagnostics.append(line.rstrip())
    return diagnostics


def warning_failures(
    log_path: Path = MASTER_LOG,
    allowlist_path: Path = WARNING_ALLOWLIST,
) -> tuple[list[str], list[str]]:
    if not log_path.is_file() or log_path.is_symlink():
        return [f"Missing compiler log: {display_path(log_path)}"], []
    patterns, failures = _allowlist_patterns(allowlist_path, "release-warning-allowlist.json")
    diagnostics = warning_lines(log_path.read_text(encoding="utf-8", errors="replace"))
    accepted: list[str] = []
    for diagnostic in diagnostics:
        if any(pattern.search(diagnostic) for pattern in patterns):
            accepted.append(diagnostic)
        else:
            failures.append(f"Unallowlisted compiler/PDF diagnostic: {diagnostic}")
    return failures, accepted


def command_failures(command: Sequence[str], label: str) -> tuple[list[str], str]:
    try:
        result = run_checked(command)
    except OSError as error:
        return [f"{label} could not run: {error}"], ""
    output = (result.stdout or "")
    if result.stderr:
        output += "\n[stderr]\n" + result.stderr
    failures: list[str] = []
    if result.returncode != 0:
        failures.append(f"{label} exited with status {result.returncode}")
    if result.stderr.strip():
        failures.append(f"{label} emitted stderr diagnostics")
    return failures, output


def font_failures(pdf_path: Path = MASTER_PDF) -> tuple[list[str], dict[str, Any]]:
    failures, output = command_failures(["pdffonts", str(pdf_path)], "pdffonts")
    rows: list[str] = []
    header_seen = False
    for line in output.splitlines():
        if line.startswith("name "):
            header_seen = True
            continue
        if not header_seen or not line.strip() or re.fullmatch(r"[-\s]+", line):
            continue
        fields = line.split()
        if len(fields) < 7:
            failures.append(f"pdffonts emitted an unparseable row: {line}")
            continue
        rows.append(line)
        status_start = next(
            (
                index
                for index in range(len(fields) - 2)
                if all(field.lower() in {"yes", "no"} for field in fields[index : index + 3])
            ),
            None,
        )
        if status_start is None:
            failures.append(f"Font is not both embedded and subset: {line}")
        elif fields[status_start].lower() != "yes" or fields[status_start + 1].lower() != "yes":
            failures.append(f"Font is not both embedded and subset: {line}")
    if not rows:
        failures.append("pdffonts reported no usable font rows")
    return failures, {"font_count": len(rows), "output": output}


def image_failures(
    pdf_path: Path = MASTER_PDF,
    allowlist_path: Path = IMAGE_ALLOWLIST,
) -> tuple[list[str], dict[str, Any]]:
    failures, output = command_failures(["pdfimages", "-list", str(pdf_path)], "pdfimages")
    patterns, allowlist_failures = _allowlist_patterns(allowlist_path, "release-image-allowlist.json")
    failures.extend(allowlist_failures)
    rows: list[str] = []
    header_seen = False
    separator_seen = False
    for line in output.splitlines():
        if re.match(r"^page\s+num\s+type\s+", line):
            header_seen = True
            continue
        if line.startswith("---"):
            separator_seen = True
            continue
        if not separator_seen or not line.strip():
            continue
        fields = line.split()
        if len(fields) < 5:
            failures.append(f"pdfimages emitted an unparseable image row: {line}")
            continue
        rows.append(line)
        failures.append(f"Raster image object is forbidden in the native release: {line}")
    if not header_seen:
        failures.append("pdfimages emitted no parseable table header")
    if not separator_seen:
        failures.append("pdfimages emitted no parseable table separator")
    if patterns:
        failures.append("release-image-allowlist.json must remain empty: native figures are TikZ")
    return failures, {"image_count": len(rows), "output": output, "rows": rows}


def pdf_page_count(pdf_path: Path) -> int | None:
    try:
        result = run_checked(["pdfinfo", str(pdf_path)])
    except OSError:
        return None
    if result.returncode != 0 or result.stderr.strip():
        return None
    match = re.search(r"^Pages:\s+(\d+)\s*$", result.stdout, re.MULTILINE)
    return int(match.group(1)) if match else None


def png_dimensions(path: Path) -> tuple[int, int]:
    import struct

    signature = b"\x89PNG\r\n\x1a\n"
    with path.open("rb") as handle:
        header = handle.read(24)
    if len(header) != 24 or header[:8] != signature:
        raise ValueError(f"Invalid PNG header: {path}")
    width, height = struct.unpack(">II", header[16:24])
    if width <= 0 or height <= 0:
        raise ValueError(f"Invalid PNG dimensions: {path}")
    return width, height


def read_jsonl(path: Path) -> tuple[list[dict[str, Any]], list[str]]:
    if not path.is_file() or path.is_symlink():
        return [], [f"Missing JSONL file: {display_path(path)}"]
    records: list[dict[str, Any]] = []
    failures: list[str] = []
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            record = json.loads(line)
        except json.JSONDecodeError as error:
            failures.append(f"{display_path(path)}:{line_number}: invalid JSON: {error}")
            continue
        if not isinstance(record, dict):
            failures.append(f"{display_path(path)}:{line_number}: record is not an object")
            continue
        records.append(record)
    return records, failures


def _page_range(value: Any) -> tuple[int, int] | None:
    if not isinstance(value, str):
        return None
    match = re.fullmatch(r"(\d{3})-(\d{3})", value)
    if match is None:
        return None
    start, end = (int(match.group(index)) for index in (1, 2))
    return (start, end) if start <= end else None


def visual_reviewer_failures(
    expected: set[int],
    inspections: Sequence[dict[str, Any]],
    *,
    root: Path = ROOT,
    mapping_path: Path = VISUAL_REVIEWER_MAP,
) -> list[str]:
    """Check page reviewers against an explicit, range-bound authorization map."""

    mapping, failures = load_json(mapping_path)
    if failures:
        return failures
    if not isinstance(mapping, dict) or mapping.get("schema_version") != 1:
        return ["visual-reviewer-map.json must be a schema_version 1 object"]
    entries = mapping.get("reviewers")
    if not isinstance(entries, list) or not entries:
        return ["visual-reviewer-map.json must contain a nonempty reviewers list"]

    authorized: dict[str, tuple[int, int, Path]] = {}
    covered: dict[int, str] = {}
    part_paths: set[Path] = set()
    for index, entry in enumerate(entries, 1):
        if not isinstance(entry, dict):
            failures.append(f"visual-reviewer-map.json reviewers[{index}] is not an object")
            continue
        reviewer = entry.get("id")
        if not isinstance(reviewer, str) or not reviewer.strip():
            failures.append(f"visual-reviewer-map.json reviewers[{index}] has no reviewer id")
            continue
        if reviewer in authorized:
            failures.append(f"visual-reviewer-map.json repeats reviewer id {reviewer!r}")
            continue
        page_range = _page_range(entry.get("pdf_pages"))
        if page_range is None:
            failures.append(f"visual-reviewer-map.json reviewers[{index}] has an invalid pdf_pages range")
            continue
        start, end = page_range
        if start not in expected or end not in expected:
            failures.append(f"visual-reviewer-map.json reviewer {reviewer!r} is outside the PDF")
        part_value = entry.get("part")
        if not isinstance(part_value, str) or not part_value or Path(part_value).is_absolute():
            failures.append(f"visual-reviewer-map.json reviewer {reviewer!r} has no relative part path")
            continue
        part_path = (root / part_value).resolve()
        try:
            part_path.relative_to(root.resolve())
        except ValueError:
            failures.append(f"visual-reviewer-map.json reviewer {reviewer!r} part escapes the project root")
            continue
        if not part_path.is_file() or part_path.is_symlink():
            failures.append(f"Missing visual review part for reviewer {reviewer!r}: {part_value}")
        if part_path in part_paths:
            failures.append(f"visual-reviewer-map.json reuses part path {part_value!r}")
        part_paths.add(part_path)
        authorized[reviewer] = (start, end, part_path)
        for page in range(start, end + 1):
            previous = covered.get(page)
            if previous is not None:
                failures.append(f"visual-reviewer-map.json overlaps page {page} between {previous!r} and {reviewer!r}")
            covered[page] = reviewer

    if set(covered) != expected:
        failures.append(
            f"visual-reviewer-map.json ranges must cover every PDF page; missing={sorted(expected - set(covered))}, extra={sorted(set(covered) - expected)}"
        )

    for index, record in enumerate(inspections, 1):
        page = record.get("pdf_page")
        reviewer = record.get("reviewer")
        if not isinstance(page, int) or isinstance(page, bool) or not isinstance(reviewer, str):
            continue
        authorization = authorized.get(reviewer.strip())
        if authorization is None:
            failures.append(f"page-inspection record {index} names unauthorized reviewer {reviewer!r}")
            continue
        start, end, _ = authorization
        if not start <= page <= end:
            failures.append(
                f"page-inspection record {index} assigns page {page} to reviewer {reviewer!r}, authorized for {start:03d}-{end:03d}"
            )

    for reviewer, (start, end, part_path) in authorized.items():
        if not part_path.is_file() or part_path.is_symlink():
            continue
        part_records, part_failures = read_jsonl(part_path)
        failures.extend(part_failures)
        part_pages: set[int] = set()
        for index, record in enumerate(part_records, 1):
            page = record.get("pdf_page")
            record_reviewer = record.get("reviewer")
            if not isinstance(page, int) or isinstance(page, bool):
                continue
            if page in part_pages:
                failures.append(f"{display_path(part_path)}:{index}: duplicate page {page}")
            part_pages.add(page)
            if record_reviewer != reviewer:
                failures.append(
                    f"{display_path(part_path)}:{index}: reviewer must be authorized id {reviewer!r}"
                )
            if not start <= page <= end:
                failures.append(
                    f"{display_path(part_path)}:{index}: page {page} lies outside reviewer range {start:03d}-{end:03d}"
                )
        expected_part_pages = set(range(start, end + 1))
        if part_pages != expected_part_pages:
            failures.append(
                f"{display_path(part_path)} must cover reviewer range {start:03d}-{end:03d}; missing={sorted(expected_part_pages - part_pages)}, extra={sorted(part_pages - expected_part_pages)}"
            )
    return failures


def rendered_inspection_failures(
    pdf_path: Path = MASTER_PDF,
    rendered_dir: Path = RENDERED_DIR,
    render_manifest: Path = RENDER_MANIFEST,
    inspection_manifest: Path = INSPECTION_MANIFEST,
) -> tuple[list[str], dict[str, Any]]:
    failures: list[str] = []
    count = pdf_page_count(pdf_path)
    if count is None:
        return ["Could not read the compiled PDF page count"], {}
    render_records, render_read_failures = read_jsonl(render_manifest)
    failures.extend(render_read_failures)
    rendered: dict[int, dict[str, Any]] = {}
    for index, record in enumerate(render_records, 1):
        raw_page = record.get("pdf_page")
        if not isinstance(raw_page, int):
            failures.append(f"{render_manifest}:{index}: pdf_page must be an integer")
            continue
        page = raw_page
        if page in rendered:
            failures.append(f"{render_manifest}:{index}: duplicate PDF page {page}")
        rendered[page] = record
        filename = record.get("filename")
        filename_match = re.fullmatch(r"page-(\d+)\.png", filename) if isinstance(filename, str) else None
        if filename_match is None or int(filename_match.group(1)) != page:
            failures.append(
                f"{render_manifest}:{index}: filename must encode PDF page {page}"
            )
            continue
        image = rendered_dir / filename
        if not image.is_file() or image.is_symlink():
            failures.append(f"Missing rendered page image: {display_path(image)}")
            continue
        try:
            width, height = png_dimensions(image)
        except ValueError as error:
            failures.append(str(error))
            continue
        if record.get("width_px") != width or record.get("height_px") != height:
            failures.append(f"Rendered dimensions changed for PDF page {page}")
        recorded_hash = record.get("sha256")
        if not isinstance(recorded_hash, str) or recorded_hash != sha256(image):
            failures.append(f"Rendered checksum changed for PDF page {page}")
        dpi = record.get("dpi")
        if not isinstance(dpi, int) or dpi < 150:
            failures.append(f"Rendered page {page} has no useful DPI record")
    expected = set(range(1, count + 1))
    if set(rendered) != expected:
        failures.append(
            f"Render manifest must match {count} PDF pages; missing={sorted(expected - set(rendered))}, extra={sorted(set(rendered) - expected)}"
        )
    actual_pngs = {
        int(match.group(1)): path
        for path in rendered_dir.glob("page-*.png")
        if (match := re.fullmatch(r"page-(\d+)\.png", path.name))
    } if rendered_dir.is_dir() else {}
    if set(actual_pngs) != expected:
        failures.append(
            f"Rendered PNG directory must match {count} PDF pages; missing={sorted(expected - set(actual_pngs))}, extra={sorted(set(actual_pngs) - expected)}"
        )

    inspections, inspection_read_failures = read_jsonl(inspection_manifest)
    failures.extend(inspection_read_failures)
    inspected: dict[int, dict[str, Any]] = {}
    render_hash = sha256(render_manifest) if render_manifest.is_file() and not render_manifest.is_symlink() else None
    pdf_hash = sha256(pdf_path) if pdf_path.is_file() and not pdf_path.is_symlink() else None
    for index, record in enumerate(inspections, 1):
        page = record.get("pdf_page")
        if not isinstance(page, int):
            failures.append(f"{inspection_manifest}:{index}: pdf_page must be an integer")
            continue
        if page in inspected:
            failures.append(f"{inspection_manifest}:{index}: duplicate PDF page {page}")
        inspected[page] = record
        if page not in expected:
            failures.append(f"{inspection_manifest}:{index}: page {page} is outside the PDF")
        if record.get("inspected") is not True:
            failures.append(f"{inspection_manifest}:{index}: page {page} is not inspected: true")
        rendered_hash = record.get("rendered_sha256")
        if not isinstance(rendered_hash, str) or rendered_hash != rendered.get(page, {}).get("sha256"):
            failures.append(f"{inspection_manifest}:{index}: page {page} has the wrong rendered checksum")
        if record.get("render_manifest_sha256") != render_hash:
            failures.append(f"{inspection_manifest}:{index}: page {page} has the wrong render-manifest checksum")
        if record.get("pdf_sha256") != pdf_hash:
            failures.append(f"{inspection_manifest}:{index}: page {page} has the wrong PDF checksum")
        if not isinstance(record.get("reviewer"), str) or not record["reviewer"].strip():
            failures.append(f"{inspection_manifest}:{index}: page {page} lacks a reviewer")
        inspected_at = record.get("inspected_at")
        if not isinstance(inspected_at, str) or not inspected_at.strip():
            failures.append(f"{inspection_manifest}:{index}: page {page} lacks inspected_at")
        else:
            try:
                parsed_time = _datetime.datetime.fromisoformat(inspected_at.replace("Z", "+00:00"))
            except ValueError:
                parsed_time = None
            if parsed_time is None or parsed_time.tzinfo is None:
                failures.append(f"{inspection_manifest}:{index}: page {page} has no timezone-aware inspected_at")
        observation = record.get("observation", record.get("notes"))
        if not isinstance(observation, str) or not observation.strip():
            failures.append(f"{inspection_manifest}:{index}: page {page} lacks inspection observation")
    if set(inspected) != expected:
        failures.append(
            f"Inspection manifest must contain one record per page; missing={sorted(expected - set(inspected))}, extra={sorted(set(inspected) - expected)}"
        )
    failures.extend(visual_reviewer_failures(expected, inspections))
    reviewers = sorted({record.get("reviewer", "").strip() for record in inspected.values() if isinstance(record.get("reviewer"), str) and record.get("reviewer", "").strip()})
    dpi_values = sorted({record.get("dpi") for record in rendered.values() if isinstance(record.get("dpi"), int)})
    if len(dpi_values) != 1:
        failures.append("Rendered page manifest must use one consistent DPI value")
    return failures, {
        "page_count": count,
        "render_dpi": dpi_values[0] if len(dpi_values) == 1 else None,
        "inspected_count": sum(record.get("inspected") is True for record in inspected.values()),
        "reviewers": reviewers,
    }


def diagnostics_failures(pdf_path: Path = MASTER_PDF) -> tuple[list[str], dict[str, Any]]:
    failures: list[str] = []
    evidence: dict[str, Any] = {}
    for path, label in ((MASTER_LOG, "master.log"), (MASTER_FLS, "master.fls"), (pdf_path, "master.pdf")):
        if not path.is_file() or path.is_symlink():
            failures.append(f"Missing compiled artifact: {display_path(path)}")
        elif path.stat().st_size == 0:
            failures.append(f"Compiled artifact is empty: {label}")
    if not pdf_path.is_file() or pdf_path.is_symlink():
        return failures, evidence
    page_count = pdf_page_count(pdf_path)
    if page_count is None or page_count <= 0:
        failures.append("Compiled PDF has no readable positive page count")
    else:
        evidence["page_count"] = page_count
    try:
        text_result = run_checked(["pdftotext", str(pdf_path), "-"])
    except OSError as error:
        failures.append(f"pdftotext could not run: {error}")
    else:
        if text_result.returncode != 0 or text_result.stderr.strip() or not text_result.stdout.strip():
            failures.append("pdftotext did not extract nonempty text")
        evidence["text_chars"] = len(text_result.stdout)
    gs_failures, _ = command_failures(
        ["gs", "-q", "-dNOPAUSE", "-dBATCH", "-sDEVICE=nullpage", str(pdf_path)],
        "Ghostscript",
    )
    failures.extend(gs_failures)
    evidence["ghostscript"] = not gs_failures
    warning_errors, accepted = warning_failures()
    failures.extend(warning_errors)
    evidence["warnings"] = accepted
    return failures, evidence


def export_failures(
    verified_pdf: Path = MASTER_PDF,
    export_pdf: Path = EXPORT_PDF,
    require_export: bool = True,
) -> tuple[list[str], dict[str, Any]]:
    failures: list[str] = []
    evidence: dict[str, Any] = {}
    if not verified_pdf.is_file() or verified_pdf.is_symlink():
        failures.append(f"Missing verified PDF: {display_path(verified_pdf)}")
        return failures, evidence
    verified_hash = sha256(verified_pdf)
    evidence["verified_pdf_sha256"] = verified_hash
    if not require_export:
        return failures, evidence
    if not export_pdf.is_file() or export_pdf.is_symlink():
        failures.append(f"Missing exported PDF: {export_pdf}")
        return failures, evidence
    if not filecmp.cmp(verified_pdf, export_pdf, shallow=False):
        failures.append("Verified and exported PDFs are not byte-identical")
    exported_hash = sha256(export_pdf)
    if verified_hash != exported_hash:
        failures.append("Verified and exported PDF SHA-256 values differ")
    evidence["exported_pdf_sha256"] = exported_hash
    evidence["byte_identity"] = not failures
    return failures, evidence


def reproducibility_failures() -> tuple[list[str], dict[str, Any]]:
    """Validate the two-build evidence against the current input tree."""

    data, failures = load_json(REPRODUCIBILITY_EVIDENCE)
    if failures:
        return failures, {}
    if not isinstance(data, dict):
        return ["reproducibility.json must contain an object"], {}
    if data.get("schema_version") != 1 or data.get("status") != "pass":
        failures.append("reproducibility.json must have schema_version 1 and status pass")
    if data.get("environment") != EXPECTED_REPRODUCIBILITY_ENV:
        failures.append("reproducibility.json does not record the fixed build environment")
    expected_command = [
        "latexmk",
        "-g",
        "-pdf",
        "-interaction=nonstopmode",
        "-halt-on-error",
        "master.tex",
    ]
    if data.get("build_command") != expected_command:
        failures.append("reproducibility.json does not record the canonical double-build command")
    current_tree, _ = deterministic_input_tree_hash(ROOT)
    if data.get("input_tree_sha256") != current_tree:
        failures.append("reproducibility.json input-tree SHA-256 does not match the current tree")
    builds = data.get("builds")
    if not isinstance(builds, list) or len(builds) != 2:
        failures.append("reproducibility.json must contain exactly two build records")
        builds = []
    hashes: list[str] = []
    byte_counts: list[int] = []
    pages: list[int] = []
    current_bytes: int | None = None
    current_pages: int | None = None
    if not MASTER_PDF.is_file() or MASTER_PDF.is_symlink():
        failures.append("reproducibility evidence cannot be checked against missing master.pdf")
    else:
        current_bytes = MASTER_PDF.stat().st_size
        current_pages = pdf_page_count(MASTER_PDF)
        if current_bytes <= 0:
            failures.append("current master.pdf has no positive byte count")
        if current_pages is None or current_pages <= 0:
            failures.append("current master.pdf has no positive page count")
    for index, build in enumerate(builds, 1):
        if not isinstance(build, dict):
            failures.append(f"reproducibility.json build[{index}] must be an object")
            continue
        build_hash = build.get("sha256")
        if not isinstance(build_hash, str) or not SHA256.fullmatch(build_hash):
            failures.append(f"reproducibility.json build[{index}] has no valid SHA-256")
        else:
            hashes.append(build_hash)
        build_bytes = build.get("bytes")
        if not isinstance(build_bytes, int) or isinstance(build_bytes, bool) or build_bytes <= 0:
            failures.append(f"reproducibility.json build[{index}] has no positive byte count")
        else:
            byte_counts.append(build_bytes)
        build_pages = build.get("pages")
        if not isinstance(build_pages, int) or isinstance(build_pages, bool) or build_pages <= 0:
            failures.append(f"reproducibility.json build[{index}] has no positive page count")
        else:
            pages.append(build_pages)
    if len(hashes) == 2 and hashes[0] != hashes[1]:
        failures.append("The two reproducibility build hashes differ")
    if len(byte_counts) == 2 and byte_counts[0] != byte_counts[1]:
        failures.append("The two reproducibility build byte counts differ")
    if len(pages) == 2 and pages[0] != pages[1]:
        failures.append("The two reproducibility build page counts differ")
    if current_bytes is not None:
        for index, build in enumerate(builds, 1):
            if isinstance(build, dict) and isinstance(build.get("bytes"), int) and not isinstance(build.get("bytes"), bool):
                if build["bytes"] != current_bytes:
                    failures.append(
                        f"reproducibility.json build[{index}] byte count does not match current master.pdf"
                    )
    if current_pages is not None:
        for index, build in enumerate(builds, 1):
            if isinstance(build, dict) and isinstance(build.get("pages"), int) and not isinstance(build.get("pages"), bool):
                if build["pages"] != current_pages:
                    failures.append(
                        f"reproducibility.json build[{index}] page count does not match current master.pdf"
                    )
    evidence_hash = data.get("pdf_sha256")
    if not isinstance(evidence_hash, str) or not SHA256.fullmatch(evidence_hash):
        failures.append("reproducibility.json has no valid pdf_sha256")
    elif hashes and evidence_hash != hashes[0]:
        failures.append("reproducibility.json pdf_sha256 differs from the build records")
    if MASTER_PDF.is_file() and isinstance(evidence_hash, str) and SHA256.fullmatch(evidence_hash):
        if evidence_hash != sha256(MASTER_PDF):
            failures.append("reproducibility evidence does not describe the current master.pdf")
    return failures, {
        "reproducible_pdf_sha256": evidence_hash,
        "reproducible_bytes": byte_counts[0] if byte_counts else None,
        "reproducible_pages": pages[0] if pages else None,
    }


def _extract_record_field(text: str, field: str, pattern: str, failures: list[str]) -> str | None:
    match = re.search(pattern, text, re.MULTILINE)
    if match is None:
        failures.append(f"RELEASE_VERIFICATION.md lacks a populated {field} field")
        return None
    value = match.group(1).strip()
    if not value or PLACEHOLDER.search(value):
        failures.append(f"RELEASE_VERIFICATION.md {field} is still a placeholder")
        return None
    return value


def release_record_failures(
    record_path: Path = RELEASE_RECORD,
    evidence: dict[str, Any] | None = None,
) -> list[str]:
    failures: list[str] = []
    if not record_path.is_file() or record_path.is_symlink():
        return [f"Missing release verification record: {record_path.name}"]
    text = record_path.read_text(encoding="utf-8")
    if PLACEHOLDER.search(text):
        failures.append("RELEASE_VERIFICATION.md contains an unresolved placeholder")
    source_hash = _extract_record_field(
        text, "source SHA-256", r"^- Source SHA-256:\s*`([^`]+)`\s*$", failures
    )
    tree_hash = _extract_record_field(
        text, "input-tree SHA-256", r"^- Input-tree SHA-256:\s*`([^`]+)`\s*$", failures
    )
    verified_hash = _extract_record_field(
        text, "verified PDF SHA-256", r"^- Verified PDF SHA-256:\s*`([^`]+)`\s*$", failures
    )
    exported_hash = _extract_record_field(
        text, "exported PDF SHA-256", r"^- Exported PDF SHA-256:\s*`([^`]+)`\s*$", failures
    )
    for label, value in (("source SHA-256", source_hash), ("input-tree SHA-256", tree_hash), ("verified PDF SHA-256", verified_hash), ("exported PDF SHA-256", exported_hash)):
        if value is not None and not SHA256.fullmatch(value):
            failures.append(f"RELEASE_VERIFICATION.md {label} is not a lowercase SHA-256")
    expected_tree, _ = deterministic_input_tree_hash(ROOT)
    if tree_hash and tree_hash != expected_tree:
        failures.append("RELEASE_VERIFICATION.md input-tree SHA-256 does not match the current input tree")
    if source_hash and source_hash != EXPECTED_SOURCE_SHA256:
        failures.append("RELEASE_VERIFICATION.md source SHA-256 does not match the authority")
    if verified_hash and MASTER_PDF.is_file() and verified_hash != sha256(MASTER_PDF):
        failures.append("RELEASE_VERIFICATION.md verified PDF SHA-256 does not match master.pdf")
    if exported_hash and EXPORT_PDF.is_file() and exported_hash != sha256(EXPORT_PDF):
        failures.append("RELEASE_VERIFICATION.md exported PDF SHA-256 does not match the export")

    required_pass_fields = {
        "Byte identity": r"^- Byte identity:\s*(PASS\b.*)$",
        "Ghostscript": r"^- Ghostscript parse check:\s*(PASS\b.*)$",
        "Extracted text": r"^- Extracted text check:\s*(PASS\b.*)$",
        "Warning disposition": r"^- Warning disposition:\s*(PASS\b.*)$",
        "Font audit": r"^- Font embedding and subsetting:\s*(PASS\b.*)$",
        "Raster audit": r"^- Full-page raster check:\s*(PASS\b.*)$",
        "Recorder audit": r"^- Facsimile or source-PDF import check:\s*(PASS\b.*)$",
        "Native chunk audit": r"^- Native chunk audit:\s*(PASS\b.*)$",
        "Notation audit": r"^- Notation audit:\s*(PASS\b.*)$",
        "Reference audit": r"^- Reference audit:\s*(PASS\b.*)$",
        "Rendered inspection": r"^- Inspection result:\s*(PASS\b.*)$",
        "Double-build reproducibility": r"^- Double-build reproducibility:\s*(PASS\b.*)$",
        "Release disposition": r"^- Release disposition:\s*(PASS\b.*)$",
    }
    for field, pattern in required_pass_fields.items():
        _extract_record_field(text, field, pattern, failures)
    page_count_value = _extract_record_field(
        text, "native PDF page count", r"^- Native PDF page count:\s*`(\d+)`\s*$", failures
    )
    rendered_value = _extract_record_field(
        text, "pages rendered", r"^- Pages rendered:\s*`(\d+)`\s*$", failures
    )
    inspected_value = _extract_record_field(
        text, "pages visually inspected", r"^- Pages visually inspected:\s*`(\d+)`\s*$", failures
    )
    if page_count_value and int(page_count_value) <= 0:
        failures.append("RELEASE_VERIFICATION.md has a nonpositive page count")
    if page_count_value and evidence and isinstance(evidence.get("page_count"), int):
        if int(page_count_value) != evidence["page_count"]:
            failures.append("RELEASE_VERIFICATION.md page count differs from the current PDF")
    if rendered_value and inspected_value and rendered_value != inspected_value:
        failures.append("RELEASE_VERIFICATION.md rendered and inspected page counts differ")
    if rendered_value and evidence and isinstance(evidence.get("page_count"), int):
        if int(rendered_value) != evidence["page_count"]:
            failures.append("RELEASE_VERIFICATION.md rendered page count differs from the current PDF")
    if inspected_value and evidence and isinstance(evidence.get("inspected_count"), int):
        if int(inspected_value) != evidence["inspected_count"]:
            failures.append("RELEASE_VERIFICATION.md inspected page count differs from the inspection manifest")
    for field, pattern in (
        ("Build date", r"^- Build date:\s*(\S+)\s*$"),
        ("Render DPI", r"^- Render DPI:\s*`(\d+)`\s*$"),
        ("Reviewer", r"^- Reviewer:\s*(.+?)\s*$"),
        ("Review date", r"^- Review date:\s*(\S+)\s*$"),
    ):
        _extract_record_field(text, field, pattern, failures)
    if not re.search(
        r"^- Fixed build environment: `SOURCE_DATE_EPOCH=946684800`, `FORCE_SOURCE_DATE=1`, `TZ=UTC`, `LC_ALL=C`\s*$",
        text,
        re.MULTILINE,
    ):
        failures.append("RELEASE_VERIFICATION.md lacks the fixed reproducibility environment")
    if evidence:
        if verified_hash and evidence.get("verified_pdf_sha256") and verified_hash != evidence["verified_pdf_sha256"]:
            failures.append("RELEASE_VERIFICATION.md verified hash differs from the audit evidence")
        if exported_hash and evidence.get("exported_pdf_sha256") and exported_hash != evidence["exported_pdf_sha256"]:
            failures.append("RELEASE_VERIFICATION.md export hash differs from the audit evidence")
    return failures


def audit_pipeline(
    require_record: bool = True,
    require_export: bool = True,
    allow_pending_coverage: set[str] | None = None,
) -> tuple[list[str], dict[str, Any]]:
    failures: list[str] = []
    evidence: dict[str, Any] = {}
    failures.extend(dependency_failures())
    source_hash = parse_source_manifest(failures)
    if source_hash:
        evidence["source_sha256"] = source_hash
    provenance_errors = review_provenance_failures()
    failures.extend(provenance_errors)
    failures.extend(coverage_failures(allow_pending_ids=allow_pending_coverage))
    tree_hash, tree_entries = deterministic_input_tree_hash(ROOT)
    evidence["input_tree_sha256"] = tree_hash
    evidence["input_tree_entries"] = len(tree_entries)
    reproducibility_errors, reproducibility_evidence = reproducibility_failures()
    failures.extend(reproducibility_errors)
    evidence.update(reproducibility_evidence)
    diagnostic_errors, diagnostic_evidence = diagnostics_failures()
    failures.extend(diagnostic_errors)
    evidence.update(diagnostic_evidence)
    failures.extend(compiled_input_failures())
    failures.extend(native_content_failures())
    font_errors, font_evidence = font_failures()
    failures.extend(font_errors)
    evidence.update(font_evidence)
    image_errors, image_evidence = image_failures()
    failures.extend(image_errors)
    evidence.update(image_evidence)
    render_errors, render_evidence = rendered_inspection_failures()
    failures.extend(render_errors)
    evidence.update(render_evidence)
    export_errors, export_evidence = export_failures(require_export=require_export)
    failures.extend(export_errors)
    evidence.update(export_evidence)
    if require_record:
        failures.extend(release_record_failures(evidence=evidence))
    return failures, evidence


def release_record_text(evidence: dict[str, Any]) -> str:
    now = _datetime.datetime.now(_datetime.timezone.utc).replace(microsecond=0).isoformat()
    page_count = int(evidence["page_count"])
    render_dpi = int(evidence["render_dpi"])
    inspected_count = int(evidence["inspected_count"])
    reviewers = ", ".join(evidence.get("reviewers", []))
    warnings = evidence.get("warnings", [])
    warning_text = "none" if not warnings else "; ".join(warnings)
    image_count = int(evidence.get("image_count", 0))
    font_count = int(evidence.get("font_count", 0))
    return f"""# Release verification record

This record was written by `scripts/audit_release_pipeline.py finalize` after
the strict post-compile checks completed. The source PDF remains the authority
named in `SOURCE_MANIFEST.yaml`.

## Identity

- Source PDF: `../../../origPapers/pct_spin_statistics_all_that.pdf`
- Source SHA-256: `{evidence['source_sha256']}`
- Input-tree definition: deterministic SHA-256 over sorted relative paths and
  file-content hashes, excluding generated files under `work/`, TeX auxiliary
  output, PDFs, and this release record. Mutable `status` values in
  `review-coverage.json` are normalized to `pending`.
- Input-tree SHA-256: `{evidence['input_tree_sha256']}`
- Verified build PDF: `latex/master.pdf`
- Verified PDF SHA-256: `{evidence['verified_pdf_sha256']}`
- Exported PDF: `../../pct-spin-statistics-all-that/pct-spin-statistics-all-that.pdf`
- Exported PDF SHA-256: `{evidence['exported_pdf_sha256']}`
- Byte identity: PASS (staged export and verified build compared byte-for-byte)

## Build

- Build command: `./build_and_verify.sh`
- Fixed build environment: `SOURCE_DATE_EPOCH=946684800`, `FORCE_SOURCE_DATE=1`, `TZ=UTC`, `LC_ALL=C`
- Build date: `{now}`
- Native PDF page count: `{page_count}`
- Double-build reproducibility: PASS (two isolated builds have the same PDF SHA-256)
- Ghostscript parse check: PASS
- Extracted text check: PASS ({evidence.get('text_chars', 0)} characters)
- Warning disposition: PASS ({warning_text})

## Fonts and native inputs

- Font embedding and subsetting: PASS ({font_count} font rows; every row is embedded and subset)
- Full-page raster check: PASS ({image_count} embedded raster objects)
- Facsimile or source-PDF import check: PASS (all expected local inputs appear in master.fls)
- Native chunk audit: PASS (review-coverage source and figure records are complete)
- Notation audit: PASS (review-coverage notation record is complete)
- Reference audit: PASS (review-coverage citation record is complete)

## Rendered-page inspection

- Render command: `python3 scripts/render_release_evidence.py render --input latex/master.pdf`
- Rendered output directory: `work/rendered-output/`
- Page manifest: `work/rendered-output/manifest.jsonl`
- Inspection manifest: `work/reviews/page-inspection.jsonl`
- Render DPI: `{render_dpi}`
- Pages rendered: `{page_count}`
- Pages visually inspected: `{inspected_count}`
- Inspection result: PASS
- Inspection notes: none recorded by the page reviewers

## Sign-off

- Reviewer: {reviewers}
- Review date: {now[:10]}
- Release disposition: PASS
"""


def pass4_release_text(evidence: dict[str, Any]) -> str:
    reviewers = ", ".join(evidence.get("reviewers", [])) or "page-inspection reviewers"
    page_count = int(evidence.get("page_count", 0))
    inspected_count = int(evidence.get("inspected_count", 0))
    verified_hash = evidence.get("verified_pdf_sha256", "")
    exported_hash = evidence.get("exported_pdf_sha256", "")
    tree_hash = evidence.get("input_tree_sha256", "")
    return f"""# PASS 4 RELEASE

PASS: 4
INPUT SNAPSHOT: Source SHA-256 `{EXPECTED_SOURCE_SHA256}`; input-tree SHA-256 `{tree_hash}`; verified PDF SHA-256 `{verified_hash}`; exported PDF SHA-256 `{exported_hash}`; compiled page count {page_count}.
FULL SCOPE READ: `RELEASE_VERIFICATION.md`, reproducibility evidence, the rendered-page manifest, the page-inspection manifest, the recorder file, diagnostics, fonts, images, export bytes, and all {page_count} rendered pages were checked.
FINDINGS: The native PDF and staged export are byte-identical, reproducibility evidence matches the compiled PDF, and {inspected_count} of {page_count} rendered pages carry checksum-bound inspection records.
EDITS MADE: Wrote the populated release verification record and this Pass 4 record; closed the Pass 4 and export-byte coverage statuses after the export audit.
CHECKS RUN: `python3 scripts/check_reproducibility.py check`, rendered-page checksum validation, page-inspection validation, `python3 scripts/audit_release_pipeline.py finalize`, and the final release-record audit.
UNRESOLVED: none
STATUS: PASS
Unresolved blockers: none
"""


def set_finalization_statuses(status: str) -> None:
    """Update only finalizer-owned statuses while preserving the schema."""

    data, failures = load_json(COVERAGE_MANIFEST)
    if failures or not isinstance(data, dict):
        raise RuntimeError("Cannot update review-coverage.json: " + "; ".join(failures))
    targets = {
        "pass-4-release": data.get("required_pass_records"),
        "export-byte-identity": data.get("release_evidence_requirements"),
    }
    for identifier, records in targets.items():
        if not isinstance(records, list):
            raise RuntimeError(f"review-coverage.json has no record list for {identifier}")
        found = False
        for record in records:
            if isinstance(record, dict) and record.get("id") == identifier:
                record["status"] = status
                found = True
                break
        if not found:
            raise RuntimeError(f"review-coverage.json has no {identifier} record")
    temporary = COVERAGE_MANIFEST.with_name(f"{COVERAGE_MANIFEST.name}.tmp.{os.getpid()}")
    temporary.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    os.replace(temporary, COVERAGE_MANIFEST)


def write_pass4_record(evidence: dict[str, Any]) -> None:
    PASS4_RECORD = ROOT / "work" / "reviews" / "PASS_4_RELEASE.md"
    PASS4_RECORD.parent.mkdir(parents=True, exist_ok=True)
    PASS4_RECORD.write_text(pass4_release_text(evidence), encoding="utf-8")


def finalize() -> int:
    """Run preflight, stage the export, then write the final evidence record."""

    pending_finalizer_records = {"pass-4-release", "export-byte-identity"}
    coverage_before = COVERAGE_MANIFEST.read_bytes() if COVERAGE_MANIFEST.is_file() else None
    release_before = RELEASE_RECORD.read_bytes() if RELEASE_RECORD.is_file() else None
    pass4_path = ROOT / "work" / "reviews" / "PASS_4_RELEASE.md"
    pass4_before = pass4_path.read_bytes() if pass4_path.is_file() else None
    export_before = EXPORT_PDF.read_bytes() if EXPORT_PDF.is_file() else None

    def rollback() -> None:
        if coverage_before is not None:
            COVERAGE_MANIFEST.write_bytes(coverage_before)
        if release_before is None:
            try:
                RELEASE_RECORD.unlink()
            except FileNotFoundError:
                pass
        else:
            RELEASE_RECORD.write_bytes(release_before)
        if pass4_before is None:
            try:
                pass4_path.unlink()
            except FileNotFoundError:
                pass
        else:
            pass4_path.write_bytes(pass4_before)
        if export_before is None:
            try:
                EXPORT_PDF.unlink()
            except FileNotFoundError:
                pass
        else:
            EXPORT_DIR.mkdir(parents=True, exist_ok=True)
            EXPORT_PDF.write_bytes(export_before)

    preflight_failures, _ = audit_pipeline(
        require_record=False,
        require_export=False,
        allow_pending_coverage=pending_finalizer_records,
    )
    if preflight_failures:
        print("RELEASE PREFLIGHT FAILED", file=sys.stderr)
        for failure in preflight_failures:
            print(f"  - {failure}", file=sys.stderr)
        return 1
    EXPORT_DIR.mkdir(parents=True, exist_ok=True)
    staged = EXPORT_PDF.with_name(f"{EXPORT_PDF.name}.tmp.{os.getpid()}")
    try:
        shutil.copyfile(MASTER_PDF, staged)
        if not filecmp.cmp(MASTER_PDF, staged, shallow=False):
            raise RuntimeError("staged export differs from master.pdf")
        os.replace(staged, EXPORT_PDF)
    except (OSError, RuntimeError) as error:
        try:
            staged.unlink()
        except FileNotFoundError:
            pass
        print(f"Could not create byte-identical export: {error}", file=sys.stderr)
        return 1
    post_failures, evidence = audit_pipeline(
        require_record=False,
        require_export=True,
        allow_pending_coverage=pending_finalizer_records,
    )
    if post_failures:
        rollback()
        print("RELEASE EXPORT AUDIT FAILED", file=sys.stderr)
        for failure in post_failures:
            print(f"  - {failure}", file=sys.stderr)
        return 1
    try:
        RELEASE_RECORD.write_text(release_record_text(evidence), encoding="utf-8")
        write_pass4_record(evidence)
        set_finalization_statuses("pass")
    except (OSError, RuntimeError) as error:
        rollback()
        print(f"Could not write release evidence: {error}", file=sys.stderr)
        return 1
    final_failures, _ = audit_pipeline(require_record=True, require_export=True)
    if final_failures:
        rollback()
        print("RELEASE RECORD AUDIT FAILED", file=sys.stderr)
        for failure in final_failures:
            print(f"  - {failure}", file=sys.stderr)
        return 1
    print(f"Release finalized: {EXPORT_PDF}")
    print(f"Verified PDF SHA-256: {evidence['verified_pdf_sha256']}")
    print(f"Input-tree SHA-256: {evidence['input_tree_sha256']}")
    return 0


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)
    audit_parser = subparsers.add_parser("audit", help="audit existing post-compile evidence")
    audit_parser.add_argument("--allow-template", action="store_true", help="skip the populated-record check for preflight")
    audit_parser.add_argument("--allow-missing-export", action="store_true", help="skip the export check for preflight")
    subparsers.add_parser("finalize", help="stage the export and write the release record after preflight")
    hash_parser = subparsers.add_parser("hash-tree", help="print the deterministic input-tree hash")
    hash_parser.add_argument("--list", action="store_true", help="also print included path/hash lines")
    args = parser.parse_args(argv)
    if args.command == "hash-tree":
        digest, entries = deterministic_input_tree_hash(ROOT)
        print(digest)
        if args.list:
            print("\n".join(entries))
        return 0
    if args.command == "finalize":
        return finalize()
    failures, evidence = audit_pipeline(
        require_record=not args.allow_template,
        require_export=not args.allow_missing_export,
    )
    print(f"Input-tree SHA-256: {evidence.get('input_tree_sha256', 'unavailable')}")
    if failures:
        print("RELEASE PIPELINE FAILURES", file=sys.stderr)
        for failure in failures:
            print(f"  - {failure}", file=sys.stderr)
        return 1
    print("Release pipeline evidence passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
