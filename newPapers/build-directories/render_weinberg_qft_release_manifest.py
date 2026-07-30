#!/usr/bin/env python3
"""Render final machine-readable and Markdown manifests for all three editions."""

from __future__ import annotations

import hashlib
import json
import re
import subprocess
from pathlib import Path


HERE = Path(__file__).resolve().parent
EXPORT_ROOT = HERE.parent / "weinberg-qft-exercises"
VOLUMES = (
    ("weinberg_vol1_exercises", "weinberg-vol1-exercises.pdf"),
    ("weinberg_vol2_exercises", "weinberg-vol2-exercises.pdf"),
    ("weinberg_vol3_exercises", "weinberg-vol3-exercises.pdf"),
)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def pdf_pages(path: Path) -> int:
    output = subprocess.check_output(
        ["pdfinfo", str(path)], text=True, stderr=subprocess.STDOUT
    )
    match = re.search(r"^Pages:\s+(\d+)\s*$", output, re.MULTILINE)
    if not match:
        raise SystemExit(f"pdfinfo did not report Pages for {path}")
    return int(match.group(1))


def main() -> int:
    volumes: list[dict[str, object]] = []
    for edition_name, export_name in VOLUMES:
        edition_root = HERE / edition_name
        inventory_path = edition_root / "exercise-inventory.json"
        build_pdf = edition_root / "latex" / "master.pdf"
        export_pdf = EXPORT_ROOT / export_name
        for path in (inventory_path, build_pdf, export_pdf):
            if not path.is_file():
                raise SystemExit(f"Missing release input: {path}")

        inventory = json.loads(inventory_path.read_text(encoding="utf-8"))
        if inventory.get("strict") is not True or inventory.get("failures"):
            raise SystemExit(f"{edition_name} inventory is not a passing strict audit")
        build_hash = sha256(build_pdf)
        export_hash = sha256(export_pdf)
        if build_hash != export_hash:
            raise SystemExit(f"Build/export hash mismatch for {edition_name}")

        chapters = inventory.get("chapters")
        if not isinstance(chapters, list):
            raise SystemExit(f"Malformed chapter inventory for {edition_name}")
        volumes.append(
            {
                "edition": edition_name,
                "export": str(export_pdf.relative_to(HERE.parent)),
                "sha256": export_hash,
                "bytes": export_pdf.stat().st_size,
                "pages": pdf_pages(export_pdf),
                "totals": inventory["totals"],
                "chapters": chapters,
            }
        )

    cross_report_path = HERE / "weinberg-qft-cross-volume-audit.json"
    if not cross_report_path.is_file():
        raise SystemExit(f"Missing cross-volume audit: {cross_report_path}")
    cross_report = json.loads(cross_report_path.read_text(encoding="utf-8"))
    if cross_report.get("failures"):
        raise SystemExit("Cross-volume audit contains failures")

    payload = {
        "series": "Weinberg, The Quantum Theory of Fields — Exercise Editions",
        "canonical_trees_modified": False,
        "volumes": volumes,
        "cross_volume_audit": cross_report,
    }
    EXPORT_ROOT.mkdir(parents=True, exist_ok=True)
    json_path = EXPORT_ROOT / "RELEASE_MANIFEST.json"
    markdown_path = EXPORT_ROOT / "RELEASE_MANIFEST.md"
    json_path.write_text(
        json.dumps(payload, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    lines = [
        "# Weinberg QFT exercise-edition release manifest",
        "",
        "| Edition | Pages | W solved | Supplementary pairs | Sources | SHA-256 |",
        "|---|---:|---:|---:|---:|---|",
    ]
    for volume in volumes:
        totals = volume["totals"]
        lines.append(
            f"| {volume['edition']} | {volume['pages']} | "
            f"{totals['weinberg_solutions']} | "
            f"{totals['supplementary_exercises']} | "
            f"{totals['ledger_sources']} | `{volume['sha256']}` |"
        )
    cross_totals = cross_report["totals"]
    lines.extend(
        [
            "",
            f"Series total: {cross_totals['supplementary_exercises']} "
            "supplementary exercises with matching solutions.",
            "",
            "Cross-volume duplicate failures: 0.",
            "",
            "The three canonical source trees were not modified.",
            "",
        ]
    )
    markdown_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {json_path}")
    print(f"Wrote {markdown_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
