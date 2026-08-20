#!/usr/bin/env python3
"""Build ordered 2x2 contact sheets from a rendered-page manifest.

The renderer owns ``work/rendered-output/page-*.png`` and its manifest.  This
helper reads those files, creates scaled copies in memory, and writes review
contact sheets under ``work/contact-sheets``.  It never writes to the rendered
page directory.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_MANIFEST = ROOT / "work" / "rendered-output" / "manifest.jsonl"
DEFAULT_OUTPUT_DIR = ROOT / "work" / "contact-sheets"
PAGE_FILE_RE = re.compile(r"^page-(\d+)\.png$")
SHEET_FILE_RE = re.compile(r"^contact-sheet-\d+-pages-\d+-\d+\.png$")


def read_manifest(manifest: Path) -> list[dict[str, Any]]:
    """Read and validate a complete rendered-page manifest."""

    if not manifest.is_file():
        raise SystemExit(f"Missing rendered-page manifest: {manifest}")

    records: list[dict[str, Any]] = []
    for line_number, raw in enumerate(
        manifest.read_text(encoding="utf-8").splitlines(), 1
    ):
        if not raw.strip():
            continue
        try:
            record = json.loads(raw)
        except json.JSONDecodeError as error:
            raise SystemExit(
                f"{manifest}:{line_number}: invalid JSON: {error}"
            ) from error
        if not isinstance(record, dict):
            raise SystemExit(
                f"{manifest}:{line_number}: each record must be a JSON object"
            )
        records.append(record)

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
        pages[page] = record

    expected = set(range(1, len(records) + 1))
    if set(pages) != expected:
        raise SystemExit(
            "Rendered-page manifest must contain one contiguous record for every "
            f"page: missing={sorted(expected - set(pages))}, "
            f"extra={sorted(set(pages) - expected)}"
        )
    return [pages[page] for page in sorted(pages)]


def load_font(image_font: Any, size: int) -> Any:
    """Load a readable label font, with platform-independent fallbacks."""

    candidates = (
        "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/Library/Fonts/Arial.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    )
    for candidate in candidates:
        try:
            return image_font.truetype(candidate, size)
        except OSError:
            continue
    return image_font.load_default()


def build_contact_sheets(
    manifest: Path,
    output_dir: Path,
    thumbnail_width: int,
) -> int:
    """Create one 2x2 PNG sheet for each group of four manifest records."""

    if thumbnail_width <= 0:
        raise SystemExit("--thumbnail-width must be positive")

    # Pillow is imported only when the build command runs.  ``--help`` and
    # ``py_compile`` remain available on systems without the optional package.
    try:
        from PIL import Image, ImageDraw, ImageFont, ImageOps
    except ImportError as error:
        raise SystemExit("make_contact_sheets.py requires Pillow") from error

    records = read_manifest(manifest)
    rendered_dir = manifest.parent
    image_paths: list[tuple[int, str, Path, tuple[int, int]]] = []
    for record in records:
        page = record["pdf_page"]
        filename = record["filename"]
        path = rendered_dir / filename
        if not path.is_file():
            raise SystemExit(f"Manifest page {page} is missing: {path}")
        try:
            with Image.open(path) as source:
                source.load()
                width, height = source.size
        except (OSError, ValueError) as error:
            raise SystemExit(f"Could not read rendered page {path}: {error}") from error
        if width <= 0 or height <= 0:
            raise SystemExit(f"Rendered page has invalid dimensions: {path}")
        image_paths.append((page, filename, path, (width, height)))

    max_thumbnail_height = max(
        round(thumbnail_width * height / width)
        for _, _, _, (width, height) in image_paths
    )
    label_height = 34
    panel_padding = 14
    sheet_margin = 24
    sheet_gap = 20
    header_height = 48
    panel_width = thumbnail_width + 2 * panel_padding
    panel_height = label_height + max_thumbnail_height + 2 * panel_padding
    sheet_width = 2 * panel_width + sheet_gap + 2 * sheet_margin
    sheet_height = (
        header_height + 2 * panel_height + sheet_gap + 2 * sheet_margin
    )
    label_font = load_font(ImageFont, 18)
    header_font = load_font(ImageFont, 22)
    resampling = getattr(Image, "Resampling", Image).LANCZOS

    output_dir.mkdir(parents=True, exist_ok=True)
    for old_sheet in output_dir.iterdir():
        if old_sheet.is_file() and SHEET_FILE_RE.fullmatch(old_sheet.name):
            old_sheet.unlink()

    sheet_count = 0
    for offset in range(0, len(image_paths), 4):
        batch = image_paths[offset : offset + 4]
        sheet_count += 1
        first_page = batch[0][0]
        last_page = batch[-1][0]
        sheet = Image.new("RGB", (sheet_width, sheet_height), "#eef1f5")
        draw = ImageDraw.Draw(sheet)
        title = (
            f"Pages {first_page:04d}-{last_page:04d}  "
            f"(sheet {sheet_count:03d})"
        )
        draw.text((sheet_margin, 15), title, fill="#17212b", font=header_font)

        for slot in range(4):
            column = slot % 2
            row = slot // 2
            x = sheet_margin + column * (panel_width + sheet_gap)
            y = sheet_margin + header_height + row * (panel_height + sheet_gap)
            draw.rounded_rectangle(
                (x, y, x + panel_width, y + panel_height),
                radius=10,
                fill="#ffffff",
                outline="#c7ced8",
                width=2,
            )
            if slot >= len(batch):
                draw.text(
                    (x + panel_padding, y + panel_padding),
                    "empty slot",
                    fill="#87919e",
                    font=label_font,
                )
                continue

            page, filename, path, _ = batch[slot]
            label = f"PDF page {page:04d}  |  {filename}"
            draw.text(
                (x + panel_padding, y + panel_padding),
                label,
                fill="#17212b",
                font=label_font,
            )
            image_box = (
                x + panel_padding,
                y + panel_padding + label_height,
                x + panel_padding + thumbnail_width,
                y + panel_padding + label_height + max_thumbnail_height,
            )
            with Image.open(path) as source:
                page_image = source.convert("RGB")
            thumbnail = ImageOps.contain(
                page_image,
                (thumbnail_width, max_thumbnail_height),
                method=resampling,
            )
            page_image.close()
            paste_x = image_box[0] + (thumbnail_width - thumbnail.width) // 2
            paste_y = image_box[1] + (max_thumbnail_height - thumbnail.height) // 2
            sheet.paste(thumbnail, (paste_x, paste_y))
            thumbnail.close()

        output_path = output_dir / (
            f"contact-sheet-{sheet_count:03d}-pages-"
            f"{first_page:04d}-{last_page:04d}.png"
        )
        sheet.save(output_path, format="PNG", optimize=True)
        sheet.close()

    print(f"Contact sheets written: {sheet_count}")
    print(f"Contact-sheet directory: {output_dir}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--manifest", type=Path, default=DEFAULT_MANIFEST,
        help="rendered-page manifest JSONL (default: work/rendered-output/manifest.jsonl)",
    )
    parser.add_argument(
        "--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR,
        help="directory for ordered contact sheets (default: work/contact-sheets)",
    )
    parser.add_argument(
        "--thumbnail-width", type=int, default=480,
        help="thumbnail width in pixels for each page (default: 480)",
    )
    args = parser.parse_args()
    return build_contact_sheets(args.manifest, args.output_dir, args.thumbnail_width)


if __name__ == "__main__":
    raise SystemExit(main())
