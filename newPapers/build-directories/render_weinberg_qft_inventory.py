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
            f"{totals['ledger_sources']} provenance records across "
            f"{totals['ledger_documents']} source documents; "
            f"{totals['preferred_source_records']} problems use a first-choice "
            f"source family, {totals['exact_source_problem_records']} preserve "
            "an exact source-problem parent, and "
            f"{totals['original_inspired_records']} are original syntheses."
        ),
        "",
        "| Chapter | Title | W ex./sol. | S ex./sol. | Allowed | Documents | First-choice pool | Exact parents | Median prompt/solution words | Exception |",
        "|---:|---|---:|---:|---:|---:|---:|---:|---:|---|",
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
                    (
                        f"{chapter['supplementary_minimum']}–"
                        f"{chapter['supplementary_maximum']}"
                    ),
                    str(len(chapter["source_distribution"])),
                    str(chapter["preferred_source_exercises"]),
                    str(chapter["exact_source_problem_exercises"]),
                    (
                        f"{chapter['prompt_word_statistics']['median']:g}/"
                        f"{chapter['solution_word_statistics']['median']:g}"
                    ),
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

    lines.extend(("", "## First-choice source families by chapter", ""))
    for chapter in payload["chapters"]:
        distribution = chapter["source_family_distribution"]
        if not distribution:
            continue
        rendered = ", ".join(
            f"`{family}` ({count})"
            for family, count in distribution.items()
        )
        lines.append(f"- Chapter {chapter['chapter']}: {rendered}")

    lines.extend(("", "## Source-use mode by chapter", ""))
    for chapter in payload["chapters"]:
        distribution = chapter["use_mode_distribution"]
        if not distribution:
            continue
        rendered = ", ".join(
            f"`{mode}` ({count})"
            for mode, count in distribution.items()
        )
        lines.append(f"- Chapter {chapter['chapter']}: {rendered}")

    lines.extend(("", "## Curation notes", ""))
    for chapter in payload["chapters"]:
        note = chapter.get("curation_note")
        if note:
            lines.append(f"- Chapter {chapter['chapter']}: {escaped(note)}")

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
