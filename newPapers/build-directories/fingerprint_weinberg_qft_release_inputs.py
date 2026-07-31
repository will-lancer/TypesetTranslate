#!/usr/bin/env python3
"""Fingerprint every release-relevant Weinberg QFT exercise-edition input."""

from __future__ import annotations

import hashlib
from pathlib import Path


HERE = Path(__file__).resolve().parent
EDITIONS = (
    "weinberg_vol1_exercises",
    "weinberg_vol2_exercises",
    "weinberg_vol3_exercises",
)
EDITION_METADATA = (
    "exercise-edition.json",
    "source-ledger.json",
    "canonical-source-sha256.json",
    "canonical-export-sha256.json",
    "weinberg-exercise-source-sha256.json",
)
BUILD_OUTPUT_NAMES = {
    "master.aux",
    "master.fdb_latexmk",
    "master.fls",
    "master.log",
    "master.out",
    "master.pdf",
    "master.synctex.gz",
    "master.toc",
}


def release_scripts(root: Path) -> set[Path]:
    return {
        path
        for path in root.iterdir()
        if path.is_file()
        and path.suffix in {".py", ".sh"}
        and path.name.startswith(("audit_", "build_", "render_", "fingerprint_"))
    }


def release_inputs() -> list[Path]:
    paths = release_scripts(HERE)
    for edition_name in EDITIONS:
        edition_root = HERE / edition_name
        if not edition_root.is_dir():
            raise SystemExit(f"Missing exercise edition: {edition_root}")
        latex_root = edition_root / "latex"
        if not latex_root.is_dir():
            raise SystemExit(f"Missing LaTeX source tree: {latex_root}")
        paths.update(
            path
            for path in latex_root.rglob("*")
            if path.is_file()
            and not (
                path.parent == latex_root and path.name in BUILD_OUTPUT_NAMES
            )
        )
        for relative in EDITION_METADATA:
            path = edition_root / relative
            if not path.is_file():
                raise SystemExit(f"Missing release metadata input: {path}")
            paths.add(path)
        paths.update(release_scripts(edition_root))
    return sorted(paths, key=lambda path: str(path.relative_to(HERE)))


def fingerprint(paths: list[Path]) -> str:
    digest = hashlib.sha256()
    for path in paths:
        relative = str(path.relative_to(HERE)).encode("utf-8")
        content_digest = hashlib.sha256(path.read_bytes()).digest()
        digest.update(len(relative).to_bytes(8, "big"))
        digest.update(relative)
        digest.update(content_digest)
    return digest.hexdigest()


def main() -> int:
    print(fingerprint(release_inputs()))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
