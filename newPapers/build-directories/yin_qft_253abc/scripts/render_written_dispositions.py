#!/usr/bin/env python3
"""Refresh chapter links in the frozen transcript-disposition ledger."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re
import sys
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
PILOT = ROOT / "work" / "pilot"
CHAPTER = ROOT / "latex" / "chapters" / "253a" / "chapter01.tex"
INPUT = PILOT / "transcript-dispositions.jsonl"

SOURCE_RE = re.compile(r"(?m)^\s*%\s*YIN-SOURCE:\s*id=([^;\s]+)")
TRANSCRIPT_ID_RE = re.compile(r"^YIN-OY-(T\d{6}[AB]?)$")
ACTIVE_USES = frozenset(
    {
        "included",
        "included_clear_portion_uncertainty_excluded",
        "merged_into_preceding_written_answer",
    }
)


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    return [
        json.loads(line)
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]


def render() -> tuple[str, dict[str, int | str]]:
    chapter_text = CHAPTER.read_text(encoding="utf-8")
    chapter_hash = hashlib.sha256(CHAPTER.read_bytes()).hexdigest()
    source_ids = set(SOURCE_RE.findall(chapter_text))
    rows = load_jsonl(INPUT)
    linked = 0
    removed_stale = 0
    for row in rows:
        old_links = row.get("included_unit_ids")
        old_links = old_links if isinstance(old_links, list) else []
        valid_links = [link for link in old_links if link in source_ids]
        removed_stale += len(old_links) - len(valid_links)
        transcript_id = row.get("transcript_record_id")
        match = TRANSCRIPT_ID_RE.fullmatch(str(transcript_id or ""))
        source_id = f"YIN253A-C01-V-{match.group(1)}" if match else None
        chapter_use = row.get("chapter_use")
        if chapter_use in ACTIVE_USES:
            if source_id not in source_ids:
                raise ValueError(
                    f"active transcript record {transcript_id} lacks chapter source span"
                )
            if source_id not in valid_links:
                valid_links.insert(0, source_id)
            linked += 1
        elif source_id in valid_links:
            valid_links.remove(source_id)
        row["included_unit_ids"] = valid_links
        row["chapter_sha256"] = chapter_hash
        row["written_linkage_mode"] = "current_chapter_source_ids"
    rendered = "".join(
        json.dumps(row, ensure_ascii=False, separators=(",", ":")) + "\n"
        for row in rows
    )
    return rendered, {
        "chapter_sha256": chapter_hash,
        "disposition_records": len(rows),
        "active_records_linked": linked,
        "stale_links_removed": removed_stale,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    action = parser.add_mutually_exclusive_group(required=True)
    action.add_argument("--write", action="store_true")
    action.add_argument("--check", action="store_true")
    args = parser.parse_args()
    rendered, stats = render()
    if args.check:
        if INPUT.read_text(encoding="utf-8") != rendered:
            print(
                f"{INPUT.relative_to(ROOT)} is stale; run "
                "scripts/render_written_dispositions.py --write",
                file=sys.stderr,
            )
            return 1
    else:
        temporary = INPUT.with_suffix(".jsonl.tmp")
        temporary.write_text(rendered, encoding="utf-8")
        temporary.replace(INPUT)
    print(json.dumps(stats, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
