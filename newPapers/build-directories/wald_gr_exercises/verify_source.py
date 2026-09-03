#!/usr/bin/env python3
"""Verify the authoritative Wald GR source before any build."""

from __future__ import annotations

import hashlib
import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent
SOURCE = ROOT.parents[2] / "origPapers" / "wald_gr.pdf"
EXPECTED_SHA256 = (
    "c0ca3f87d5dc8689ec89a2b9aef376a00670160b593e17dc533546f22b094599"
)
EXPECTED_PAGES = 505


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def main() -> int:
    if not SOURCE.exists():
        print(f"Missing authoritative source: {SOURCE}", file=sys.stderr)
        return 1

    actual_hash = sha256(SOURCE)
    if actual_hash != EXPECTED_SHA256:
        print(
            "Source checksum mismatch:\n"
            f"  expected {EXPECTED_SHA256}\n"
            f"  actual   {actual_hash}",
            file=sys.stderr,
        )
        return 1

    try:
        result = subprocess.run(
            ["pdfinfo", str(SOURCE)],
            check=True,
            capture_output=True,
            text=True,
        )
    except (FileNotFoundError, subprocess.CalledProcessError) as error:
        print(f"Unable to inspect source with pdfinfo: {error}", file=sys.stderr)
        return 1

    match = re.search(r"^Pages:\s+(\d+)\s*$", result.stdout, re.MULTILINE)
    pages = int(match.group(1)) if match else None
    if pages != EXPECTED_PAGES:
        print(
            f"Source page-count mismatch: expected {EXPECTED_PAGES}, "
            f"found {pages!r}.",
            file=sys.stderr,
        )
        return 1

    print(
        f"Authoritative source OK: {SOURCE.name}, {pages} pages, "
        f"SHA-256 {actual_hash}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

