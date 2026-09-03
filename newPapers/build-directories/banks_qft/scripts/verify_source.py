#!/usr/bin/env python3
"""Verify the canonical Banks PDF identity and fixed metadata."""

from __future__ import annotations

import hashlib
import re
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "banks-qft.pdf"
EXPECTED_SHA256 = "31de7827e7bc636feaa7028fe4dbb63a718b3926ee43ff3d96d91185a44eafe3"
JHEPPUB = ROOT / "latex" / "jheppub.sty"
EXPECTED_JHEPPUB_SHA256 = "8771cbcc63db02d48243effe911571ad8967ccb68d79129011a5ccc2ab0a7527"


def main() -> int:
    digest = hashlib.sha256(SOURCE.read_bytes()).hexdigest()
    if digest != EXPECTED_SHA256:
        raise SystemExit(f"Source hash mismatch: {digest}")
    style_digest = hashlib.sha256(JHEPPUB.read_bytes()).hexdigest()
    if style_digest != EXPECTED_JHEPPUB_SHA256:
        raise SystemExit(f"Pinned jheppub.sty hash mismatch: {style_digest}")
    info = subprocess.run(
        ["pdfinfo", str(SOURCE)], check=True, text=True, capture_output=True
    ).stdout
    pages = re.search(r"^Pages:\s+(\d+)\s*$", info, re.MULTILINE)
    size = re.search(r"^Page size:\s+([0-9.]+) x ([0-9.]+) pts", info, re.MULTILINE)
    if not pages or int(pages.group(1)) != 281:
        raise SystemExit("Source page count differs from 281")
    if not size or tuple(map(float, size.groups())) != (235.0, 335.0):
        raise SystemExit("Source page size differs from 235 x 335 pt")
    print(f"source verification pass: 281 pages; sha256={digest}; pinned JHEP style pass")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
