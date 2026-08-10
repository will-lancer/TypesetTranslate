#!/usr/bin/env python3
"""Write or verify the reviewed render manifest for the current Yin QFT book."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / "latex" / "master.pdf"
AUX = ROOT / "latex" / "master.aux"
MASTER = ROOT / "latex" / "master.tex"
OUTPUT = ROOT / "work" / "release" / "render-manifest.json"
RENDER_ROOT = ROOT / "qa" / "rendered"
DPI = 180

CHAPTERS = (
    {
        "chapter_id": "253a-ch01",
        "tex_path": "latex/chapters/253a/chapter01.tex",
        "start_label": "ch:253a-basic-generalities",
        "end_label": None,
    },
    {
        "chapter_id": "253a-ch02",
        "tex_path": "latex/chapters/253a/chapter02.tex",
        "start_label": "ch:253a-lagrangian-qm",
        "end_label": "ch:253a-lagrangian-qm-end",
    },
)


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def pdf_pages() -> int:
    result = subprocess.run(
        ["pdfinfo", str(PDF)], check=True, capture_output=True, text=True
    )
    match = re.search(r"(?m)^Pages:\s+(\d+)\s*$", result.stdout)
    if match is None:
        raise ValueError("pdfinfo did not report a page count")
    return int(match.group(1))


def label_page(aux_text: str, label: str) -> int:
    pattern = re.compile(
        rf"\\newlabel\{{{re.escape(label)}\}}\{{\{{[^}}]*\}}\{{(\d+)\}}"
    )
    match = pattern.search(aux_text)
    if match is None:
        raise ValueError(f"master.aux lacks label {label!r}")
    return int(match.group(1))


def image_set(page_count: int, pdf_hash: str) -> list[Path]:
    directory = RENDER_ROOT / pdf_hash
    width = max(2, len(str(page_count)))
    expected = [directory / f"page-{page:0{width}d}.png" for page in range(1, page_count + 1)]
    missing = [path.relative_to(ROOT).as_posix() for path in expected if not path.is_file()]
    if missing:
        raise ValueError(f"rendered page set is incomplete: {missing[:8]}")
    actual = sorted(directory.glob("page-*.png"))
    if actual != expected:
        raise ValueError("render directory contains an unexpected page set")
    return expected


def range_digest(images: list[Path], first_page: int, last_page: int) -> str:
    state = hashlib.sha256()
    for path in images[first_page - 1 : last_page]:
        state.update(path.read_bytes())
    return state.hexdigest()


def render() -> tuple[str, dict[str, Any]]:
    if not PDF.is_file() or not AUX.is_file():
        raise ValueError("latex/master.pdf and latex/master.aux must exist")
    pdf_hash = digest(PDF)
    page_count = pdf_pages()
    images = image_set(page_count, pdf_hash)
    aux_text = AUX.read_text(encoding="utf-8", errors="replace")

    chapter_ranges: list[tuple[int, int]] = []
    starts = [label_page(aux_text, str(spec["start_label"])) for spec in CHAPTERS]
    for index, spec in enumerate(CHAPTERS):
        first_page = starts[index]
        if spec["end_label"] is not None:
            last_page = label_page(aux_text, str(spec["end_label"]))
        elif index + 1 < len(CHAPTERS):
            last_page = starts[index + 1] - 1
        else:
            last_page = page_count
        if not 1 <= first_page <= last_page <= page_count:
            raise ValueError(
                f"invalid page range for {spec['chapter_id']}: {first_page}--{last_page}"
            )
        chapter_ranges.append((first_page, last_page))

    image_rows = [
        {
            "page": page,
            "path": path.relative_to(ROOT).as_posix(),
            "sha256": digest(path),
            "bytes": path.stat().st_size,
        }
        for page, path in enumerate(images, 1)
    ]
    chapters = []
    for spec, (first_page, last_page) in zip(CHAPTERS, chapter_ranges, strict=True):
        tex_path = ROOT / str(spec["tex_path"])
        if not tex_path.is_file():
            raise ValueError(f"missing {spec['tex_path']}")
        chapters.append(
            {
                "chapter_id": spec["chapter_id"],
                "tex_path": spec["tex_path"],
                "tex_sha256": digest(tex_path),
                "first_pdf_page": first_page,
                "last_pdf_page": last_page,
                "chapter_render_sha256": range_digest(images, first_page, last_page),
                "images": image_rows[first_page - 1 : last_page],
            }
        )

    payload = {
        "record_type": "release_render_manifest",
        "schema_version": 2,
        "pdf_path": "latex/master.pdf",
        "pdf_sha256": pdf_hash,
        "pdf_bytes": PDF.stat().st_size,
        "page_count": page_count,
        "dpi": DPI,
        "render_directory": (RENDER_ROOT / pdf_hash).relative_to(ROOT).as_posix(),
        "master_tex_sha256": digest(MASTER),
        "images": image_rows,
        "chapters": chapters,
    }
    text = json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    return text, {
        "pdf_sha256": pdf_hash,
        "page_count": page_count,
        "chapter_ranges": {
            chapter["chapter_id"]: [
                chapter["first_pdf_page"],
                chapter["last_pdf_page"],
            ]
            for chapter in chapters
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    action = parser.add_mutually_exclusive_group(required=True)
    action.add_argument("--write", action="store_true")
    action.add_argument("--check", action="store_true")
    args = parser.parse_args()
    try:
        rendered, stats = render()
    except (OSError, ValueError, subprocess.CalledProcessError) as exc:
        print(f"release render manifest failed: {exc}", file=sys.stderr)
        return 1
    if args.check:
        if not OUTPUT.is_file() or OUTPUT.read_text(encoding="utf-8") != rendered:
            print(
                f"{OUTPUT.relative_to(ROOT)} is stale; complete a reviewed draft render first",
                file=sys.stderr,
            )
            return 1
    else:
        OUTPUT.parent.mkdir(parents=True, exist_ok=True)
        temporary = OUTPUT.with_suffix(".json.tmp")
        temporary.write_text(rendered, encoding="utf-8")
        temporary.replace(OUTPUT)
    print(json.dumps(stats, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
