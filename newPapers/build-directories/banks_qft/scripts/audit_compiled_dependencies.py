#!/usr/bin/env python3
"""Check that the compiled edition read exactly the intended native inputs."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

try:
    from build_input_manifest import expected_compiled_inputs, validate_manifest
except ModuleNotFoundError:
    from scripts.build_input_manifest import expected_compiled_inputs, validate_manifest


ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--edition", choices=("base", "implicit"), required=True)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--pdf", type=Path)
    args = parser.parse_args()
    try:
        manifest = json.loads(args.manifest.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise SystemExit(f"Cannot read build-input manifest: {error}") from error
    failures = validate_manifest(manifest, edition=args.edition, pdf=args.pdf)
    if failures:
        raise SystemExit("\n".join(failures))
    rows = manifest["files"]
    paths = {str(item["path"]) for item in rows}
    expected = expected_compiled_inputs(args.edition)
    missing = sorted(expected - paths)
    unexpected = sorted(paths - expected)
    if missing or unexpected:
        details = []
        if missing:
            details.append(f"missing={missing}")
        if unexpected:
            details.append(f"unexpected={unexpected}")
        raise SystemExit("Compiled dependency closure mismatch: " + "; ".join(details))
    print(f"Compiled dependency audit passes: edition={args.edition}; exact inputs={len(paths)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
