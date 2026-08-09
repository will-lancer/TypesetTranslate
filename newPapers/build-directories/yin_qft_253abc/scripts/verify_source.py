#!/usr/bin/env python3
from __future__ import annotations

import hashlib
from pathlib import Path
import sys

SOURCE = Path("/Users/wlancer/Desktop/IAS/phy/qft/qft_253abc_book.pdf")
EXPECTED = "9e5e4d241fffffa56c1c3df6dce4b83178f75787dd5d794a18c5d0c087769f21"


def main() -> int:
    if not SOURCE.is_file():
        print(f"Missing source PDF: {SOURCE}", file=sys.stderr)
        return 1
    digest = hashlib.sha256()
    with SOURCE.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    actual = digest.hexdigest()
    if actual != EXPECTED:
        print(f"Source hash mismatch: {actual}", file=sys.stderr)
        return 1
    print(f"Verified source PDF: {actual}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
