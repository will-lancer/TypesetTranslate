#!/usr/bin/env python3
"""Render ``exercise-inventory.json`` as a reviewable Markdown report."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent
INVENTORY = ROOT / "exercise-inventory.json"
OUTPUT = ROOT / "EXERCISE_INVENTORY.md"


def escaped(value: object) -> str:
    return str(value).replace("|", r"\|").replace("\n", " ")


def main() -> int:
    payload = json.loads(INVENTORY.read_text(encoding="utf-8"))
    totals = payload["totals"]
    lines = [
        "# Exercise inventory",
        "",
        f"Edition: `{payload['edition']}`",
        "",
        (
            f"Totals: {totals['weinberg_exercises']} Weinberg exercises, "
            f"{totals['weinberg_solutions']} Weinberg solutions, "
            f"{totals['supplementary_exercises']} supplementary exercises, "
            f"{totals['supplementary_solutions']} supplementary solutions, "
            f"and {totals['ledger_sources']} ledger sources."
        ),
        "",
        "| Chapter | Title | W ex./sol. | S ex./sol. | Target | Sources | Exception |",
        "|---:|---|---:|---:|---:|---:|---|",
    ]
    for chapter in payload["chapters"]:
        exception = chapter.get("count_exception") or ""
        lines.append(
            "| "
            + " | ".join(
                (
                    str(chapter["chapter"]),
                    escaped(chapter["title"]),
                    (
                        f"{chapter['weinberg_exercises']}/"
                        f"{chapter['weinberg_solutions']}"
                    ),
                    (
                        f"{chapter['supplementary_exercises']}/"
                        f"{chapter['supplementary_solutions']}"
                    ),
                    str(chapter["supplementary_target"]),
                    str(len(chapter["source_distribution"])),
                    escaped(exception),
                )
            )
            + " |"
        )

    lines.extend(("", "## Source use by chapter", ""))
    for chapter in payload["chapters"]:
        distribution = chapter["source_distribution"]
        if not distribution:
            continue
        rendered = ", ".join(
            f"`{source_id}` ({count})"
            for source_id, count in distribution.items()
        )
        lines.append(f"- Chapter {chapter['chapter']}: {rendered}")

    warnings = payload.get("warnings", [])
    failures = payload.get("failures", [])
    lines.extend(("", "## Audit status", ""))
    lines.append(
        f"- Mode: {'strict' if payload.get('strict') else 'draft'}"
    )
    lines.append(f"- Warnings: {len(warnings)}")
    lines.append(f"- Failures: {len(failures)}")
    if warnings:
        lines.extend(("", "### Current draft warnings", ""))
        lines.extend(f"- {escaped(warning)}" for warning in warnings)
    if failures:
        lines.extend(("", "### Failures", ""))
        lines.extend(f"- {escaped(failure)}" for failure in failures)

    OUTPUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {OUTPUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
