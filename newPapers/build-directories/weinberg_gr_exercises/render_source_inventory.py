#!/usr/bin/env python3
"""Render the machine-readable exercise source inventory as Markdown."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent
INVENTORY = ROOT / "exercise-source-inventory.json"
OUTPUT = ROOT / "EXERCISE_SOURCE_INVENTORY.md"


def escaped(value: object) -> str:
    return str(value).replace("|", r"\|").replace("\n", " ")


def main() -> int:
    payload = json.loads(INVENTORY.read_text(encoding="utf-8"))
    summary = payload["summary"]
    lines = [
        "# Supplementary exercise source inventory",
        "",
        (
            f"Corpus: {summary['corpus_documents']} hashed source documents. "
            f"Problem-level inventory: {summary['inventory_documents']}/"
            f"{summary['expected_problem_documents']} documents and "
            f"{summary['inspected_parent_problems']} complete parent problems."
        ),
        "",
        "Disposition totals: "
        + (
            ", ".join(
                f"`{name}`={count}"
                for name, count in summary["dispositions"].items()
            )
            or "none yet"
        )
        + ".",
        "",
        "The indivisible inventory unit is the complete numbered source parent. "
        "A `selected` row must correspond to exactly one edition exercise; "
        "subparts are never separate rows.",
        "",
        "| Parent ID | Family | Course | Year | Document | Problem | Printed pages | PDF pages | Disposition | Chapter | Topic | Rationale | Source | Local PDF |",
        "|---|---|---|---:|---|---|---|---|---|---:|---|---|---|---|",
    ]
    for document in payload["documents"]:
        for problem in document["problems"]:
            problem_label = problem.get("question_number", problem.get("problem_number", ""))
            chapter = problem.get("recommended_chapter")
            lines.append(
                "| "
                + " | ".join(
                    (
                        f"`{escaped(problem['source_parent_id'])}`",
                        escaped(document["source_family"]),
                        escaped(document["course"]),
                        escaped(document["year"]),
                        f"`{escaped(document['document_id'])}`",
                        escaped(problem_label),
                        escaped(problem["printed_pages"]),
                        escaped(problem["pdf_pages"]),
                        escaped(problem["disposition"]),
                        "" if chapter is None else str(chapter),
                        escaped(problem["short_topic"]),
                        escaped(problem["disposition_rationale"]),
                        f"[source]({document['stable_url']})",
                        f"`{escaped(document['local_pdf'])}`",
                    )
                )
                + " |"
            )
    if payload.get("warnings"):
        lines.extend(("", "## Current inventory warnings", ""))
        lines.extend(f"- {escaped(message)}" for message in payload["warnings"])
    if payload.get("failures"):
        lines.extend(("", "## Current inventory failures", ""))
        lines.extend(f"- {escaped(message)}" for message in payload["failures"])
    OUTPUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {OUTPUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
