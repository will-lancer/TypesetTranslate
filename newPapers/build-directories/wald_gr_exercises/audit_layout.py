#!/usr/bin/env python3
"""Report or reject layout warnings in the Wald build log."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent
LOG = ROOT / "latex" / "master.log"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--report-only", action="store_true")
    args = parser.parse_args()

    if not LOG.exists():
        print(f"Missing build log: {LOG}")
        return 1
    text = LOG.read_text(encoding="utf-8", errors="replace")
    overfull = re.findall(r"^Overfull \\hbox.*$", text, re.MULTILINE)
    underfull = re.findall(r"^Underfull \\hbox.*$", text, re.MULTILINE)
    print(f"Layout warnings: {len(overfull)} overfull, {len(underfull)} underfull.")
    for finding in overfull:
        print(f"  - {finding}")
    return 0 if args.report_only or not overfull else 1


if __name__ == "__main__":
    raise SystemExit(main())

