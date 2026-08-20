#!/usr/bin/env python3
"""Build two isolated copies of the native inputs and compare their PDFs.

The checker uses the fixed values in ``reproducible-build.env``.  It copies
only native TeX and style inputs into temporary directories, so generated
auxiliary files cannot become a hidden input to either build.  A JSON evidence
record is written only after both builds succeed and have identical bytes.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import subprocess
import tempfile
from pathlib import Path
from typing import Any, Sequence

import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
from audit_release_pipeline import deterministic_input_tree_hash  # noqa: E402


ROOT = Path(__file__).resolve().parents[1]
LATEX = ROOT / "latex"
ENV_FILE = ROOT / "reproducible-build.env"
EVIDENCE = ROOT / "work" / "reviews" / "reproducibility.json"
EXPECTED_ENV = {
    "SOURCE_DATE_EPOCH": "946684800",
    "FORCE_SOURCE_DATE": "1",
    "TZ": "UTC",
    "LC_ALL": "C",
}
GENERATED_SUFFIXES = {
    ".aux",
    ".bbl",
    ".bcf",
    ".blg",
    ".dvi",
    ".fdb_latexmk",
    ".fls",
    ".idx",
    ".ilg",
    ".ind",
    ".log",
    ".out",
    ".pdf",
    ".run.xml",
    ".snm",
    ".synctex",
    ".synctex.gz",
    ".toc",
    ".vrb",
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def is_generated_file(path: Path) -> bool:
    name = path.name.lower()
    return any(name.endswith(suffix) for suffix in GENERATED_SUFFIXES)


def load_fixed_environment(path: Path = ENV_FILE) -> dict[str, str]:
    values: dict[str, str] = {}
    for line_number, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        if "=" not in line:
            raise ValueError(f"{path}:{line_number}: expected KEY=value")
        key, value = line.split("=", 1)
        values[key.strip()] = value.strip()
    if values != EXPECTED_ENV:
        raise ValueError(
            f"{path} must contain exactly the fixed reproducibility environment: {EXPECTED_ENV}"
        )
    return values


def copy_native_inputs(source: Path, destination: Path) -> None:
    for path in source.rglob("*"):
        relative = path.relative_to(source)
        if any(part == "__pycache__" for part in relative.parts):
            continue
        if path.is_dir():
            continue
        if path.is_symlink() or is_generated_file(path):
            continue
        target = destination / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(path, target)


def pdf_page_count(path: Path) -> int | None:
    result = subprocess.run(["pdfinfo", str(path)], capture_output=True, text=True, check=False)
    if result.returncode != 0 or result.stderr.strip():
        return None
    for line in result.stdout.splitlines():
        if line.startswith("Pages:"):
            try:
                return int(line.split(":", 1)[1].strip())
            except ValueError:
                return None
    return None


def build_once(destination: Path, environment: dict[str, str]) -> dict[str, Any]:
    env = os.environ.copy()
    env.update(environment)
    env["SOURCE_DATE_EPOCH"] = environment["SOURCE_DATE_EPOCH"]
    env["FORCE_SOURCE_DATE"] = environment["FORCE_SOURCE_DATE"]
    env["TZ"] = environment["TZ"]
    env["LC_ALL"] = environment["LC_ALL"]
    command = ["latexmk", "-g", "-pdf", "-interaction=nonstopmode", "-halt-on-error", "master.tex"]
    result = subprocess.run(command, cwd=destination, env=env, capture_output=True, text=True, check=False)
    if result.returncode != 0:
        detail = (result.stdout + "\n" + result.stderr)[-4000:]
        raise RuntimeError(f"latexmk failed in {destination}:\n{detail}")
    pdf = destination / "master.pdf"
    if not pdf.is_file() or pdf.stat().st_size == 0:
        raise RuntimeError(f"latexmk produced no nonempty PDF in {destination}")
    return {
        "sha256": sha256(pdf),
        "bytes": pdf.stat().st_size,
        "pages": pdf_page_count(pdf),
    }


def check() -> int:
    environment = load_fixed_environment()
    tree_hash, _ = deterministic_input_tree_hash(ROOT)
    with tempfile.TemporaryDirectory(prefix="pct-repro-") as temporary:
        first = Path(temporary) / "first"
        second = Path(temporary) / "second"
        first.mkdir()
        second.mkdir()
        copy_native_inputs(LATEX, first)
        copy_native_inputs(LATEX, second)
        build_one = build_once(first, environment)
        build_two = build_once(second, environment)
    for label, build in (("first", build_one), ("second", build_two)):
        if not isinstance(build.get("bytes"), int) or isinstance(build.get("bytes"), bool) or build["bytes"] <= 0:
            print(f"Reproducibility check failed: {label} build has no positive byte count", flush=True)
            return 1
        if not isinstance(build.get("pages"), int) or isinstance(build.get("pages"), bool) or build["pages"] <= 0:
            print(f"Reproducibility check failed: {label} build has no positive page count", flush=True)
            return 1
    if build_one["sha256"] != build_two["sha256"]:
        print("Reproducibility check failed: isolated build hashes differ", flush=True)
        print(json.dumps({"first": build_one, "second": build_two}, sort_keys=True))
        return 1
    if build_one["bytes"] != build_two["bytes"]:
        print("Reproducibility check failed: isolated build byte counts differ", flush=True)
        print(json.dumps({"first": build_one, "second": build_two}, sort_keys=True))
        return 1
    if build_one["pages"] != build_two["pages"]:
        print("Reproducibility check failed: isolated build page counts differ", flush=True)
        print(json.dumps({"first": build_one, "second": build_two}, sort_keys=True))
        return 1
    record = {
        "schema_version": 1,
        "status": "pass",
        "environment": environment,
        "build_command": ["latexmk", "-g", "-pdf", "-interaction=nonstopmode", "-halt-on-error", "master.tex"],
        "input_tree_sha256": tree_hash,
        "builds": [build_one, build_two],
        "pdf_sha256": build_one["sha256"],
    }
    EVIDENCE.parent.mkdir(parents=True, exist_ok=True)
    EVIDENCE.write_text(json.dumps(record, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"Reproducible PDF SHA-256: {build_one['sha256']}")
    print(f"Evidence: {EVIDENCE}")
    return 0


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("check", nargs="?", default="check")
    args = parser.parse_args(argv)
    if args.check != "check":
        parser.error("the only command is check")
    return check()


if __name__ == "__main__":
    raise SystemExit(main())
