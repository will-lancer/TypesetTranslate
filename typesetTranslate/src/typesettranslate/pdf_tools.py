from __future__ import annotations

import re
import shutil
import subprocess
from pathlib import Path


def _tool_exists(name: str) -> bool:
    return shutil.which(name) is not None


def detect_page_count(pdf_path: Path) -> tuple[int | None, str | None]:
    if not _tool_exists("pdfinfo"):
        return None, "pdfinfo not available; page count not detected"

    result = subprocess.run(
        ["pdfinfo", str(pdf_path)],
        check=False,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        return None, f"pdfinfo failed: {result.stderr.strip() or result.stdout.strip()}"

    match = re.search(r"^Pages:\s+(\d+)$", result.stdout, re.MULTILINE)
    if not match:
        return None, "pdfinfo output did not contain a page count"

    return int(match.group(1)), None


def collect_page_images(pages_dir: Path) -> list[Path]:
    return sorted(pages_dir.glob("page-*.png"))


def build_page_manifest(page_count: int | None, pages_dir: Path) -> list[dict[str, str | int]]:
    manifest: list[dict[str, str | int]] = []
    page_images = collect_page_images(pages_dir)
    for index, page_image in enumerate(page_images, start=1):
        manifest.append(
            {
                "page_number": index,
                "image_path": str(page_image.resolve()),
            }
        )
    if page_count and len(manifest) > page_count:
        return manifest[:page_count]
    return manifest


def render_pages(pdf_path: Path, output_dir: Path) -> tuple[bool, str | None]:
    existing_pages = collect_page_images(output_dir)
    if existing_pages:
        return True, None

    if not _tool_exists("pdftoppm"):
        return False, "pdftoppm not available; page images not rendered"

    output_prefix = output_dir / "page"
    result = subprocess.run(
        [
            "pdftoppm",
            "-png",
            "-r",
            "200",
            str(pdf_path),
            str(output_prefix),
        ],
        check=False,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        return False, f"pdftoppm failed: {result.stderr.strip() or result.stdout.strip()}"

    raw_pages = sorted(
        output_dir.glob("page-*.png"),
        key=lambda path: int(path.stem.split("-")[-1]),
    )
    for index, raw_page in enumerate(raw_pages, start=1):
        normalized_path = output_dir / f"page-{index:04d}.png"
        if raw_page != normalized_path:
            raw_page.rename(normalized_path)

    return True, None
