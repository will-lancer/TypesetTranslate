from __future__ import annotations

import json
import re
import sys
import unittest
from collections import Counter
from pathlib import Path


PROJECT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT / "scripts"))

import audit_transcription  # noqa: E402


MARKER_LINE = re.compile(r"PCT-SOURCE:\s*pdf=")


def source_marker_records() -> tuple[list[tuple[int, str, int, str, str]], int]:
    records: list[tuple[int, str, int, str, str]] = []
    marker_lines = 0
    for path in sorted(audit_transcription.LATEX.rglob("*.tex")):
        text = path.read_text(encoding="utf-8")
        for line in text.splitlines():
            if MARKER_LINE.search(line):
                marker_lines += 1
        for match in audit_transcription.PAGE_MARKER.finditer(text):
            records.append(
                (
                    int(match.group("physical")),
                    path.relative_to(PROJECT).as_posix(),
                    text.count("\n", 0, match.start()) + 1,
                    match.group("printed"),
                    match.group("kind"),
                )
            )
    return records, marker_lines


def ledger_marker_records() -> list[tuple[int, str, int, str, str]]:
    records: list[tuple[int, str, int, str, str]] = []
    ledger = PROJECT / "page-dispositions.jsonl"
    for line in ledger.read_text(encoding="utf-8").splitlines():
        page_record = json.loads(line)
        page = int(page_record["pdf_page"])
        for marker in page_record.get("markers", []):
            records.append(
                (
                    page,
                    str(marker["file"]),
                    int(marker["line"]),
                    str(marker["print"]),
                    str(marker["kind"]),
                )
            )
    return records


class SourceMarkerProvenanceTests(unittest.TestCase):
    def test_reading_edition_has_no_inline_source_markers(self) -> None:
        source, marker_lines = source_marker_records()
        self.assertEqual(marker_lines, 0)
        self.assertEqual(source, [])

        for path in sorted(audit_transcription.LATEX.rglob("*.tex")):
            for line_number, line in enumerate(
                path.read_text(encoding="utf-8").splitlines(), start=1
            ):
                self.assertIsNone(
                    MARKER_LINE.search(line),
                    f"inline PCT-SOURCE marker at {path}:{line_number}",
                )

    def test_master_assembles_the_native_chunks(self) -> None:
        paths, assembly_issues = audit_transcription.collect_assembled_files(
            audit_transcription.MASTER, audit_transcription.LATEX
        )
        segments, segment_issues = audit_transcription.collect_segments(paths)

        self.assertEqual(assembly_issues, [])
        self.assertEqual(segment_issues, [])
        self.assertEqual(len(paths), 50)
        self.assertEqual(segments, [])


if __name__ == "__main__":
    unittest.main()
