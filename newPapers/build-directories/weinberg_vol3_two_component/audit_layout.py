#!/usr/bin/env python3
"""Reject horizontal-overflow regressions relative to the untouched edition."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent
LOG = ROOT / "latex" / "master.log"

# Measured by compiling an isolated copy of ../weinberg_vol3/latex.
BASELINE_OVERFULL_COUNT = 22
BASELINE_MAX_WIDTH_PT = 41.26297
OVERFULL_RE = re.compile(r"Overfull \\hbox \(([0-9.]+)pt too wide\)")


def main() -> int:
    if not LOG.exists():
        print(f"Missing LaTeX log: {LOG}", file=sys.stderr)
        return 1

    widths = [
        float(value)
        for value in OVERFULL_RE.findall(LOG.read_text(encoding="utf-8"))
    ]
    maximum = max(widths, default=0.0)
    print(
        "Horizontal overflow audit: "
        f"count={len(widths)} (baseline {BASELINE_OVERFULL_COUNT}), "
        f"max={maximum:.5f}pt (baseline {BASELINE_MAX_WIDTH_PT:.5f}pt)"
    )

    if len(widths) > BASELINE_OVERFULL_COUNT:
        print("FAIL: the two-component edition adds overfull boxes.")
        return 1
    if maximum > BASELINE_MAX_WIDTH_PT + 1e-5:
        print("FAIL: the widest overfull box exceeds the original edition.")
        return 1
    print("No horizontal-overflow regression relative to the original edition.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
