#!/usr/bin/env python3
"""Verify the immutable source scan before any build."""

from __future__ import annotations

import hashlib
import re
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "source" / "zhou-quantitative-finance-interviews.pdf"
EXPECTED_SHA256 = "a31f318b4d017d9eab7887cd91b9f5ca65542e6b31bce541039e2ef24828d026"
EXPECTED_PAGES = 212


def main() -> None:
    if not SOURCE.is_file():
        raise SystemExit(f"Missing source: {SOURCE}")

    digest = hashlib.sha256(SOURCE.read_bytes()).hexdigest()
    if digest != EXPECTED_SHA256:
        raise SystemExit(f"Source hash mismatch: {digest}")

    info = subprocess.run(
        ["pdfinfo", str(SOURCE)],
        check=True,
        capture_output=True,
        text=True,
    ).stdout
    match = re.search(r"^Pages:\s+(\d+)\s*$", info, re.MULTILINE)
    pages = int(match.group(1)) if match else None
    if pages != EXPECTED_PAGES:
        raise SystemExit(f"Source page-count mismatch: {pages}")

    print(f"Source verified: {pages} pages, SHA-256 {digest}")


if __name__ == "__main__":
    main()

