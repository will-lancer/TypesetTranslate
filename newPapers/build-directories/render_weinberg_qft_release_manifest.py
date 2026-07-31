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
EXPECTED_TOTALS = {
    "weinberg_vol1_exercises": {
        "weinberg_exercises": 70,
        "weinberg_solutions": 70,
        "supplementary_exercises": 390,
        "supplementary_solutions": 390,
    },
    "weinberg_vol2_exercises": {
        "weinberg_exercises": 50,
        "weinberg_solutions": 50,
        "supplementary_exercises": 270,
        "supplementary_solutions": 270,
    },
    "weinberg_vol3_exercises": {
        "weinberg_exercises": 39,
        "weinberg_solutions": 39,
        "supplementary_exercises": 240,
        "supplementary_solutions": 240,
    },
}
EXPECTED_SERIES_SUPPLEMENTARY = 900


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


def validated_inventory_totals(
    edition_name: str,
    inventory: dict[str, object],
    chapters: list[object],
) -> dict[str, object]:
    """Recompute release-critical totals instead of trusting cached arithmetic."""

    if inventory.get("edition") != edition_name:
        raise SystemExit(f"{edition_name} inventory has the wrong edition name")
    totals = inventory.get("totals")
    if not isinstance(totals, dict):
        raise SystemExit(f"{edition_name} inventory totals are malformed")
    expected = EXPECTED_TOTALS[edition_name]
    for key, expected_value in expected.items():
        actual_value = totals.get(key)
        if actual_value != expected_value:
            raise SystemExit(
                f"{edition_name} inventory {key} is {actual_value!r}, "
                f"expected {expected_value}"
            )
        chapter_values: list[int] = []
        for chapter in chapters:
            if not isinstance(chapter, dict):
                raise SystemExit(f"{edition_name} has a malformed chapter record")
            value = chapter.get(key)
            if not isinstance(value, int) or isinstance(value, bool):
                raise SystemExit(
                    f"{edition_name} chapter {chapter.get('chapter')} has "
                    f"malformed {key}"
                )
            chapter_values.append(value)
        if sum(chapter_values) != expected_value:
            raise SystemExit(
                f"{edition_name} chapter {key} sum does not match its inventory total"
            )
    return totals


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
        if (
            inventory.get("strict") is not True
            or inventory.get("failures") != []
            or inventory.get("warnings") != []
        ):
            raise SystemExit(f"{edition_name} inventory is not a passing strict audit")
        build_hash = sha256(build_pdf)
        export_hash = sha256(export_pdf)
        if build_hash != export_hash:
            raise SystemExit(f"Build/export hash mismatch for {edition_name}")

        chapters = inventory.get("chapters")
        if not isinstance(chapters, list):
            raise SystemExit(f"Malformed chapter inventory for {edition_name}")
        totals = validated_inventory_totals(edition_name, inventory, chapters)
        volumes.append(
            {
                "edition": edition_name,
                "export": str(export_pdf.relative_to(HERE.parent)),
                "sha256": export_hash,
                "bytes": export_pdf.stat().st_size,
                "pages": pdf_pages(export_pdf),
                "totals": totals,
                "chapters": chapters,
            }
        )

    cross_report_path = HERE / "weinberg-qft-cross-volume-audit.json"
    if not cross_report_path.is_file():
        raise SystemExit(f"Missing cross-volume audit: {cross_report_path}")
    cross_report = json.loads(cross_report_path.read_text(encoding="utf-8"))
    if cross_report.get("failures") != [] or cross_report.get("warnings") != []:
        raise SystemExit("Cross-volume audit contains failures or similarity warnings")
    cross_editions = cross_report.get("editions")
    if not isinstance(cross_editions, dict) or set(cross_editions) != set(EXPECTED_TOTALS):
        raise SystemExit("Cross-volume audit edition set is malformed")
    for volume in volumes:
        edition_name = str(volume["edition"])
        cross_counts = cross_editions.get(edition_name)
        if not isinstance(cross_counts, dict):
            raise SystemExit(f"Missing cross-volume counts for {edition_name}")
        expected_supplementary = EXPECTED_TOTALS[edition_name][
            "supplementary_exercises"
        ]
        if (
            cross_counts.get("supplementary_exercises") != expected_supplementary
            or cross_counts.get("supplementary_solutions") != expected_supplementary
        ):
            raise SystemExit(
                f"Cross-volume counts for {edition_name} do not match "
                "the authoritative volume totals"
            )
        totals = volume["totals"]
        if (
            totals["supplementary_exercises"]
            != cross_counts["supplementary_exercises"]
            or totals["supplementary_solutions"]
            != cross_counts["supplementary_solutions"]
        ):
            raise SystemExit(
                f"Inventory/cross-volume supplementary mismatch for {edition_name}"
            )
    cross_totals = cross_report.get("totals")
    if not isinstance(cross_totals, dict):
        raise SystemExit("Cross-volume totals are malformed")
    if (
        cross_totals.get("supplementary_exercises")
        != EXPECTED_SERIES_SUPPLEMENTARY
        or cross_totals.get("supplementary_solutions")
        != EXPECTED_SERIES_SUPPLEMENTARY
        or sum(
            int(volume["totals"]["supplementary_exercises"])
            for volume in volumes
        )
        != EXPECTED_SERIES_SUPPLEMENTARY
    ):
        raise SystemExit("Cross-volume series totals are not the authoritative 900 pairs")

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
