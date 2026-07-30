#!/usr/bin/env python3
"""Verify that the authoritative Weinberg GR source images have not changed."""

from __future__ import annotations

import hashlib
import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent
SOURCE = ROOT.parents[2] / "origPapers" / "weinberg_gr.pdf"
EXPECTED_SHA256 = (
    "da6fca5e44d31417e0d370108a622f9444602d68f"
    "b5768ec8edbc5b8ce5a78f9"
)
EXPECTED_PAGES = 681
SUPPLEMENTS = (
    (
        ROOT / "source-supplements" / "contents-pxxii.png",
        "00e14fa83d0876aefa3ba861e912bdbe8f3fec6d2f53ea24e"
        "f55e7a0cca2a846",
    ),
    (
        ROOT / "source-supplements" / "printed-p306.png",
        "c95152340f04500518044e41168f47f4b39ab654cbb60720d"
        "852ce842568d361",
    ),
    (
        ROOT / "source-supplements" / "printed-p390.png",
        "788956392f51d4f048866d4edd69f0cf050a6fc17fb202271"
        "4aafb35d552e252",
    ),
    (
        ROOT / "source-supplements" / "printed-p392.png",
        "8939772852a85b1d635b239d7a6b1d2fa87be2f1015aa00d"
        "0ed27ead0546bbd4",
    ),
    (
        ROOT / "source-supplements" / "printed-p418.png",
        "8258b17d0a56f6dde94184c0976cd710b2669b8ac19efbcdf"
        "1276f0283e51575",
    ),
    (
        ROOT / "source-supplements" / "printed-p440.png",
        "1873eaa778d3a98ac4b2994bff2c5947f50901acbd8b7afb"
        "5c7f3279d1d2f9ad",
    ),
    (
        ROOT / "source-supplements" / "printed-p594.png",
        "ff9de0953a07355d16720a37e59547c61c17018bebd95b826"
        "bb348ad715a676d",
    ),
    (
        ROOT / "source-supplements" / "printed-p602.png",
        "077103c327a4741aaa586691f52f523f5cf24456430a25fac"
        "28e8032a143dc2b",
    ),
)


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

    verified_supplements = []
    for supplement, expected_hash in SUPPLEMENTS:
        if not supplement.exists():
            print(f"Missing supplemental source: {supplement}", file=sys.stderr)
            return 1

        supplement_hash = sha256(supplement)
        if supplement_hash != expected_hash:
            print(
                f"Supplement checksum mismatch ({supplement.name}):\n"
                f"  expected {expected_hash}\n"
                f"  actual   {supplement_hash}",
                file=sys.stderr,
            )
            return 1
        verified_supplements.append((supplement.name, supplement_hash))

    print(
        f"Authoritative source OK: {SOURCE.name}, {pages} pages, "
        f"SHA-256 {actual_hash}"
    )
    for name, supplement_hash in verified_supplements:
        print(f"Supplemental source OK: {name}, SHA-256 {supplement_hash}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
