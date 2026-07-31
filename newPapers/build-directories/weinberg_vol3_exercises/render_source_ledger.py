#!/usr/bin/env python3
"""Render ``source-ledger.json`` as a human-readable Markdown ledger."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent
LEDGER = ROOT / "source-ledger.json"
OUTPUT = ROOT / "SOURCE_LEDGER.md"


def escaped(value: object) -> str:
    return str(value).replace("|", r"\|").replace("\n", " ")


def main() -> int:
    if not LEDGER.exists():
        OUTPUT.write_text(
            "# Source ledger\n\nStatus: source ledger not yet populated.\n",
            encoding="utf-8",
        )
        print(f"Wrote draft placeholder: {OUTPUT}")
        return 0

    payload = json.loads(LEDGER.read_text(encoding="utf-8"))
    sources = sorted(payload.get("sources", []), key=lambda item: item["id"])
    lines = [
        "# Source ledger",
        "",
        (
            "Every supplementary exercise prints a credit and stores the "
            "corresponding stable ID in its LaTeX macro. This table is "
            "generated from `source-ledger.json`."
        ),
        "",
        "| Parent ID | Family | Document | Provenance parent / source scope | Use | Author/institution | Source | Year | Locator | Chapters | URL |",
        "|---|---|---|---|---|---|---|---:|---|---|---|",
    ]
    for source in sources:
        chapters = ", ".join(str(chapter) for chapter in source["chapters"])
        url = str(source["url"])
        lines.append(
            "| "
            + " | ".join(
                (
                    f"`{escaped(source['id'])}`",
                    escaped(source["source_family"]),
                    f"`{escaped(source['document_id'])}`",
                    escaped(source["parent_problem"]),
                    escaped(source["use_mode"]),
                    escaped(source["author_or_institution"]),
                    escaped(source["title"]),
                    escaped(source["year"]),
                    escaped(source["locator"]),
                    chapters,
                    f"[source]({url})",
                )
            )
            + " |"
        )

    lines.extend(("", "## Adaptation notes", ""))
    for source in sources:
        lines.append(
            f"- `{source['id']}`: {escaped(source['adaptation_notes'])}"
        )
    OUTPUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {OUTPUT} with {len(sources)} sources")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
