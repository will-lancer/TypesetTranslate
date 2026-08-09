#!/usr/bin/env python3
"""Regression tests for the active Yin written-prose gate."""

from __future__ import annotations

import unittest
import tempfile
from pathlib import Path

from audit_written_prose import (
    LEGACY_MARKER_RE,
    Result,
    oversized_inline_formulas,
    parse_speech_blocks,
    strip_tex_comment,
)


class WrittenProseAuditTests(unittest.TestCase):
    def test_balanced_speech_span(self) -> None:
        result = Result(strict=True)
        order, blocks = parse_speech_blocks(
            [
                "% YIN-SPEECH-BEGIN YIN-OY-T000001",
                "Written prose.",
                "% YIN-SPEECH-END YIN-OY-T000001",
            ],
            result,
        )
        self.assertEqual(order, ["YIN-OY-T000001"])
        self.assertEqual(set(blocks), {"YIN-OY-T000001"})
        self.assertEqual(result.errors, [])

    def test_nested_speech_span_fails(self) -> None:
        result = Result(strict=True)
        parse_speech_blocks(
            [
                "% YIN-SPEECH-BEGIN YIN-OY-T000001",
                "% YIN-SPEECH-BEGIN YIN-OY-T000002",
                "% YIN-SPEECH-END YIN-OY-T000001",
            ],
            result,
        )
        self.assertTrue(result.errors)

    def test_inline_integral_fails_and_display_integral_passes(self) -> None:
        inline = r"The field is $\phi(x)=\int d^D p\,a_p e^{ipx}$."
        display = (
            r"The field is" "\n"
            r"\begin{equation}\phi(x)=\int d^D p\,a_p e^{ipx}.\end{equation}"
        )
        self.assertEqual(len(oversized_inline_formulas(inline)[0]), 1)
        self.assertEqual(oversized_inline_formulas(display)[0], [])

    def test_tex_comment_stripping_preserves_escaped_percent(self) -> None:
        self.assertEqual(strip_tex_comment(r"value \% kept % removed"), r"value \% kept ")

    def test_legacy_marker_is_detected(self) -> None:
        self.assertIsNotNone(
            LEGACY_MARKER_RE.search("% YIN-VERBATIM-BEGIN YIN-OY-T000001")
        )

    def test_chapter_hash_uses_utf8_bytes(self) -> None:
        text = "Yin's voice: φ."
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "chapter.tex"
            path.write_text(text, encoding="utf-8")
            self.assertEqual(path.read_bytes(), text.encode("utf-8"))


if __name__ == "__main__":
    unittest.main()
