#!/usr/bin/env python3
"""Report LaTeX box warnings and reject horizontal overflow in strict builds."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent
LOG = ROOT / "latex" / "master.log"
OVERFULL_RE = re.compile(r"Overfull \\hbox \(([0-9.]+)pt too wide\)")
UNDERFULL_RE = re.compile(r"Underfull \\hbox")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--report-only",
        action="store_true",
        help="report overflow without failing (for partial draft builds)",
    )
    args = parser.parse_args()

    if not LOG.exists():
        print(f"Missing LaTeX log: {LOG}", file=sys.stderr)
        return 1

    text = LOG.read_text(encoding="utf-8")
    widths = [float(value) for value in OVERFULL_RE.findall(text)]
    maximum = max(widths, default=0.0)
    underfull = len(UNDERFULL_RE.findall(text))
    print(
        "Layout audit: "
        f"overfull hboxes={len(widths)}, max overflow={maximum:.5f}pt; "
        f"underfull hboxes={underfull}."
    )

    if widths and not args.report_only:
        print(
            "FAIL: strict publication builds require zero overfull hboxes.",
            file=sys.stderr,
        )
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
