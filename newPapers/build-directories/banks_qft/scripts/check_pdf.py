#!/usr/bin/env python3
"""Validate a compiled Banks PDF and its LaTeX recorder files."""

from __future__ import annotations

import argparse
import re
import subprocess
from pathlib import Path


ERROR_RE = re.compile(
    r"Undefined control sequence|LaTeX Error|Fatal error|Emergency stop|"
    r"Runaway argument|Missing \\endgroup|There were undefined references|"
    r"Citation .+ undefined|Label\(s\) may have changed"
)


def run(command: list[str]) -> str:
    return subprocess.run(command, check=True, text=True, capture_output=True).stdout


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("pdf", type=Path)
    parser.add_argument("--log", type=Path, required=True)
    parser.add_argument("--fls", type=Path, required=True)
    parser.add_argument("--strict", action="store_true")
    args = parser.parse_args()

    for path in (args.pdf, args.log, args.fls):
        if not path.is_file() or path.stat().st_size == 0:
            raise SystemExit(f"Missing required build artifact: {path}")

    log = args.log.read_text(encoding="utf-8", errors="replace")
    if ERROR_RE.search(log):
        raise SystemExit("LaTeX diagnostic audit failed")
    if args.strict:
        overfull = [kind for kind in ("hbox", "vbox") if f"Overfull \\{kind}" in log]
        if overfull:
            raise SystemExit("Strict build contains overfull " + ", ".join(overfull) + " boxes")

    recorder = args.fls.read_text(encoding="utf-8", errors="replace")
    forbidden = ("banks-qft.pdf", "source-render", "source-pages", "\\includepdf")
    if any(token in recorder for token in forbidden):
        raise SystemExit("Compiled PDF imported a source or facsimile artifact")

    info = run(["pdfinfo", str(args.pdf)])
    if "Page size:       595.276 x 841.89 pts (A4)" not in info:
        raise SystemExit("Compiled PDF is not A4")
    run(["pdftotext", str(args.pdf), "-"])
    subprocess.run(
        ["gs", "-q", "-dNOPAUSE", "-dBATCH", "-sDEVICE=nullpage", str(args.pdf)],
        check=True,
    )
    fonts = run(["pdffonts", str(args.pdf)]).splitlines()[2:]
    if not fonts:
        raise SystemExit("No font table returned")
    unembedded = [line for line in fonts if len(line.split()) >= 5 and line.split()[-5] != "yes"]
    if unembedded:
        raise SystemExit("Compiled PDF contains unembedded fonts")
    if args.strict:
        images = run(["pdfimages", "-list", str(args.pdf)]).splitlines()[2:]
        if any(line.strip() for line in images):
            raise SystemExit("Strict native PDF contains raster image objects")
    print(f"PDF checks pass: {args.pdf}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
