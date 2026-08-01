#!/usr/bin/env python3
"""Regression checks for corrections shared by both Volume I editions."""

from __future__ import annotations

from pathlib import Path


EDITION_ROOT = Path(__file__).resolve().parent
CANONICAL_ROOT = EDITION_ROOT.parent / "weinberg_vol1"

CHECKS = {
    "latex/chapters/chapter03/sec38.tex": (
        "resonant energy, the the `eigenphase'",
        "resonant energy, the `eigenphase'",
    ),
    "latex/chapters/chapter05/sec57.tex": (
        "theories of a charged massive particles",
        "theories of charged massive particles",
        "a electromagnetic background field",
        "an electromagnetic background field",
    ),
    "latex/chapters/chapter07/sec77.tex": (
        "an redundant coupling",
        "a redundant coupling",
    ),
    "latex/chapters/chapter07/appendix.tex": (
        "constraints can `solved'",
        "constraints can be `solved'",
    ),
    "latex/chapters/chapter12/sec122.tex": (
        "a unconventional renormalization point",
        "an unconventional renormalization point",
    ),
}


def audit(root: Path) -> list[str]:
    failures: list[str] = []
    for relative, phrases in CHECKS.items():
        path = root / relative
        if not path.is_file():
            failures.append(f"missing source file: {path}")
            continue
        text = path.read_text(encoding="utf-8")
        for old, new in zip(phrases[::2], phrases[1::2], strict=True):
            if old in text:
                failures.append(f"obsolete wording remains in {path}: {old!r}")
            if text.count(new) != 1:
                failures.append(
                    f"expected exactly one corrected phrase in {path}: {new!r}"
                )
    return failures


def main() -> int:
    failures = audit(CANONICAL_ROOT) + audit(EDITION_ROOT)
    if failures:
        for failure in failures:
            print(f"ERROR: {failure}")
        return 1
    print("Errata regression audit passed for canonical and exercise editions.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
