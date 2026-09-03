#!/usr/bin/env python3
"""Verify the frozen source render against the canonical Banks PDF."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import struct
import subprocess
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXPECTED_SOURCE_SHA256 = "31de7827e7bc636feaa7028fe4dbb63a718b3926ee43ff3d96d91185a44eafe3"
EXPECTED_SOURCE_PAGES = 281
EXPECTED_RENDER_DPI = 150
EXPECTED_RENDER_BOX = "cropbox"
EXPECTED_RENDER_PATTERN = "page-%03d.png"
EXPECTED_RENDER_COMMAND = "pdftoppm -cropbox -r 150 -png banks-qft.pdf page"
PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"
PAGE_RE = re.compile(r"page-(\d{3})\.png$")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def scalar(text: str, key: str, indent: int) -> str:
    indentation = " " * indent
    pattern = rf"(?m)^{indentation}{re.escape(key)}:\s*(.+?)\s*$"
    match = re.search(pattern, text)
    if match is None:
        raise SystemExit(f"SOURCE_MANIFEST.yaml lacks {key}")
    value = match.group(1).strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {'"', "'"}:
        value = value[1:-1]
    return value


def page_count(pdf: Path) -> int:
    result = subprocess.run(["pdfinfo", str(pdf)], check=True, text=True, capture_output=True)
    match = re.search(r"^Pages:\s+(\d+)\s*$", result.stdout, re.MULTILINE)
    if match is None:
        raise SystemExit(f"Could not read source page count: {pdf}")
    return int(match.group(1))


def png_dimensions(path: Path) -> tuple[int, int]:
    with path.open("rb") as handle:
        header = handle.read(24)
    if len(header) != 24 or header[:8] != PNG_SIGNATURE:
        raise SystemExit(f"Invalid source-render PNG: {path}")
    return struct.unpack(">II", header[16:24])


def render_digest(paths: list[Path]) -> str:
    digest = hashlib.sha256()
    for path in paths:
        digest.update(sha256(path).encode("ascii"))
        digest.update(b"  ")
        digest.update(path.name.encode("utf-8"))
        digest.update(b"\n")
    return digest.hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    try:
        manifest_text = args.manifest.read_text(encoding="utf-8")
    except OSError as error:
        raise SystemExit(f"Cannot read source manifest: {error}") from error

    source_relative = scalar(manifest_text, "path", 2)
    source_hash = scalar(manifest_text, "sha256", 2)
    source_pages = int(scalar(manifest_text, "physical_pages", 2))
    render_directory = Path(scalar(manifest_text, "directory", 4))
    render_pattern = scalar(manifest_text, "filename_pattern", 4)
    render_count = int(scalar(manifest_text, "count", 4))
    render_dpi = int(scalar(manifest_text, "dpi", 4))
    render_box = scalar(manifest_text, "box", 4)
    render_command = scalar(manifest_text, "command", 4)

    source = (ROOT / source_relative).resolve()
    canonical_source = (ROOT / "banks-qft.pdf").resolve()
    if source_relative != "banks-qft.pdf" or source != canonical_source:
        raise SystemExit(f"SOURCE_MANIFEST.yaml source path is not canonical: {source_relative}")
    if source_hash != EXPECTED_SOURCE_SHA256:
        raise SystemExit("SOURCE_MANIFEST.yaml source hash is not canonical")
    if source_pages != EXPECTED_SOURCE_PAGES or render_count != EXPECTED_SOURCE_PAGES:
        raise SystemExit("SOURCE_MANIFEST.yaml source/render page count is not 281")
    if render_pattern != EXPECTED_RENDER_PATTERN:
        raise SystemExit(f"Unexpected source-render filename pattern: {render_pattern}")
    if render_command != EXPECTED_RENDER_COMMAND:
        raise SystemExit("SOURCE_MANIFEST.yaml source-render command differs from the frozen contract")
    if render_dpi != EXPECTED_RENDER_DPI or render_box != EXPECTED_RENDER_BOX:
        raise SystemExit("SOURCE_MANIFEST.yaml source-render geometry differs from the frozen contract")
    if not source.is_file() or sha256(source) != EXPECTED_SOURCE_SHA256:
        raise SystemExit("Canonical source PDF is missing or has the wrong hash")
    if page_count(source) != EXPECTED_SOURCE_PAGES:
        raise SystemExit("Canonical source PDF page count differs from 281")
    if not render_directory.is_dir():
        raise SystemExit(f"Missing shared source-render directory: {render_directory}")

    expected_names = {f"page-{page:03d}.png" for page in range(1, EXPECTED_SOURCE_PAGES + 1)}
    actual_paths = sorted(render_directory.glob("page-*.png"), key=lambda path: path.name)
    actual_names = {path.name for path in actual_paths}
    if actual_names != expected_names:
        missing = sorted(expected_names - actual_names)
        extra = sorted(actual_names - expected_names)
        raise SystemExit(f"Shared source-render set differs: missing={missing}; extra={extra}")
    for path in actual_paths:
        if path.stat().st_size == 0:
            raise SystemExit(f"Empty shared source-render image: {path}")
        png_dimensions(path)

    with tempfile.TemporaryDirectory(prefix="banks-source-render-") as temporary:
        generated_prefix = Path(temporary) / "page"
        result = subprocess.run(
            [
                "pdftoppm",
                "-cropbox",
                "-r",
                str(EXPECTED_RENDER_DPI),
                "-png",
                str(source),
                str(generated_prefix),
            ],
            check=False,
            text=True,
            capture_output=True,
        )
        if result.returncode != 0:
            raise SystemExit("Source-render rerender failed:\n" + (result.stdout + result.stderr)[-4000:])
        generated_paths = sorted(Path(temporary).glob("page-*.png"), key=lambda path: path.name)
        if {path.name for path in generated_paths} != expected_names:
            raise SystemExit("Source-render rerender produced an unexpected page set")
        for generated in generated_paths:
            stored = render_directory / generated.name
            if sha256(generated) != sha256(stored):
                raise SystemExit(f"Shared source-render differs from deterministic rerender: {stored.name}")

    records = {
        "schema_version": 1,
        "status": "pass",
        "source_sha256": EXPECTED_SOURCE_SHA256,
        "source_pages": EXPECTED_SOURCE_PAGES,
        "render_directory": str(render_directory),
        "render_filename_pattern": EXPECTED_RENDER_PATTERN,
        "render_count": EXPECTED_SOURCE_PAGES,
        "render_dpi": EXPECTED_RENDER_DPI,
        "render_box": EXPECTED_RENDER_BOX,
        "render_sha256": render_digest(actual_paths),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(records, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"Source-render provenance passes: {records['render_sha256']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
