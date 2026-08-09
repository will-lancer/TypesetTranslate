#!/usr/bin/env python3
"""Write or verify the manifest for the hash-addressed rendered PDF pages."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / "latex" / "master.pdf"
OUTPUT = ROOT / "work" / "pilot" / "render-manifest.json"
RENDER_ROOT = ROOT / "qa" / "rendered"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def pdf_pages() -> int:
    result = subprocess.run(
        ["pdfinfo", str(PDF)],
        check=True,
        capture_output=True,
        text=True,
    )
    match = re.search(r"(?m)^Pages:\s+(\d+)\s*$", result.stdout)
    if match is None:
        raise ValueError("pdfinfo did not report a page count")
    return int(match.group(1))


def render() -> tuple[str, dict[str, int | str]]:
    pdf_hash = digest(PDF)
    page_count = pdf_pages()
    directory = RENDER_ROOT / pdf_hash
    images = sorted(directory.glob("page-*.png"))
    expected_names = [f"page-{page:02d}.png" for page in range(1, page_count + 1)]
    actual_names = [path.name for path in images]
    if actual_names != expected_names:
        raise ValueError(
            f"rendered page set for {pdf_hash} is incomplete: "
            f"expected {expected_names}, found {actual_names}"
        )
    payload = {
        "schema_version": 1,
        "pdf_path": "latex/master.pdf",
        "pdf_sha256": pdf_hash,
        "page_count": page_count,
        "dpi": 180,
        "render_directory": f"qa/rendered/{pdf_hash}",
        "images": [
            {
                "page": page,
                "path": f"qa/rendered/{pdf_hash}/{path.name}",
                "sha256": digest(path),
                "bytes": path.stat().st_size,
            }
            for page, path in enumerate(images, 1)
        ],
    }
    text = json.dumps(payload, indent=2, ensure_ascii=False, sort_keys=True) + "\n"
    return text, {"pdf_sha256": pdf_hash, "page_count": page_count}


def main() -> int:
    parser = argparse.ArgumentParser()
    action = parser.add_mutually_exclusive_group(required=True)
    action.add_argument("--write", action="store_true")
    action.add_argument("--check", action="store_true")
    args = parser.parse_args()
    try:
        rendered, stats = render()
    except (OSError, ValueError, subprocess.CalledProcessError) as exc:
        print(f"render manifest failed: {exc}", file=sys.stderr)
        return 1
    if args.check:
        if not OUTPUT.is_file() or OUTPUT.read_text(encoding="utf-8") != rendered:
            print(
                f"{OUTPUT.relative_to(ROOT)} is stale; render the current PDF and "
                "run scripts/render_render_manifest.py --write",
                file=sys.stderr,
            )
            return 1
    else:
        temporary = OUTPUT.with_suffix(".json.tmp")
        temporary.write_text(rendered, encoding="utf-8")
        temporary.replace(OUTPUT)
    print(json.dumps(stats, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
