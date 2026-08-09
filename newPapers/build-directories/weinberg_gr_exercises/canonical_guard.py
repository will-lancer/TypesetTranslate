#!/usr/bin/env python3
"""Freeze and verify the independent canonical Weinberg GR edition.

The exercise edition must never mutate its sibling ``weinberg_gr`` tree or
the canonical exported PDF.  Git status alone is insufficient because that
tree contains ignored build artifacts, so this guard records every regular
file by relative path, mode, size, and SHA-256 digest.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import stat
import sys
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parent
CANONICAL_ROOT = (ROOT.parent / "weinberg_gr").resolve()
BASELINE = ROOT / "canonical-baseline.json"
CANONICAL_EXPORT = (ROOT / "../../weinberg-gr-modernized.pdf").resolve()


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def file_record(path: Path, base: Path) -> dict[str, object]:
    metadata = path.lstat()
    return {
        "path": path.relative_to(base).as_posix(),
        "mode": stat.S_IMODE(metadata.st_mode),
        "size": metadata.st_size,
        "sha256": sha256(path),
    }


def snapshot() -> dict[str, object]:
    if not CANONICAL_ROOT.is_dir():
        raise FileNotFoundError(f"Canonical tree is missing: {CANONICAL_ROOT}")
    if not CANONICAL_EXPORT.is_file():
        raise FileNotFoundError(f"Canonical export is missing: {CANONICAL_EXPORT}")

    files = [
        file_record(path, CANONICAL_ROOT)
        for path in sorted(CANONICAL_ROOT.rglob("*"))
        if path.is_file() and not path.is_symlink()
    ]
    symlinks = [
        {
            "path": path.relative_to(CANONICAL_ROOT).as_posix(),
            "target": str(path.readlink()),
        }
        for path in sorted(CANONICAL_ROOT.rglob("*"))
        if path.is_symlink()
    ]
    return {
        "schema_version": 1,
        "canonical_root": "../weinberg_gr",
        "generated_at": date.today().isoformat(),
        "files": files,
        "symlinks": symlinks,
        "canonical_export": {
            "path": "../../weinberg-gr-modernized.pdf",
            "mode": stat.S_IMODE(CANONICAL_EXPORT.stat().st_mode),
            "size": CANONICAL_EXPORT.stat().st_size,
            "sha256": sha256(CANONICAL_EXPORT),
        },
    }


def comparable(payload: dict[str, object]) -> dict[str, object]:
    payload = dict(payload)
    payload.pop("generated_at", None)
    return payload


def check() -> int:
    if not BASELINE.is_file():
        print(f"Canonical baseline is missing: {BASELINE}", file=sys.stderr)
        return 1
    try:
        expected = json.loads(BASELINE.read_text(encoding="utf-8"))
    except json.JSONDecodeError as error:
        print(f"Cannot parse canonical baseline: {error}", file=sys.stderr)
        return 1
    current = snapshot()
    if comparable(current) != comparable(expected):
        expected_files = {
            item["path"]: item for item in expected.get("files", [])
        }
        current_files = {
            item["path"]: item for item in current.get("files", [])
        }
        for path in sorted(set(expected_files) | set(current_files)):
            if expected_files.get(path) != current_files.get(path):
                print(f"Canonical tree changed: {path}", file=sys.stderr)
        if expected.get("symlinks") != current.get("symlinks"):
            print("Canonical symlink inventory changed", file=sys.stderr)
        if expected.get("canonical_export") != current.get("canonical_export"):
            print("Canonical exported PDF changed", file=sys.stderr)
        return 1
    print(
        "Canonical guard: "
        f"{len(current['files'])} files and the canonical export are unchanged."
    )
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--write-baseline",
        action="store_true",
        help="write the initial canonical manifest; refuses to overwrite it",
    )
    args = parser.parse_args()

    if args.write_baseline:
        if BASELINE.exists():
            print(f"Refusing to overwrite existing baseline: {BASELINE}", file=sys.stderr)
            return 1
        payload = snapshot()
        BASELINE.write_text(
            json.dumps(payload, indent=2, ensure_ascii=True) + "\n",
            encoding="utf-8",
        )
        print(
            f"Wrote {BASELINE} with {len(payload['files'])} canonical files."
        )
        return 0
    return check()


if __name__ == "__main__":
    raise SystemExit(main())
