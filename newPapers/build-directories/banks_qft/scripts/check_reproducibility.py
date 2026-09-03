#!/usr/bin/env python3
"""Build two isolated native copies and require byte-identical PDFs."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import subprocess
import tempfile
from pathlib import Path

try:
    from build_input_manifest import expected_compiled_inputs, validate_manifest
except ModuleNotFoundError:
    from scripts.build_input_manifest import expected_compiled_inputs, validate_manifest


ROOT = Path(__file__).resolve().parents[1]
LATEX = ROOT / "latex"
EXPECTED_ENV = {
    "SOURCE_DATE_EPOCH": "946684800",
    "FORCE_SOURCE_DATE": "1",
    "TZ": "UTC",
    "LC_ALL": "C",
}
TOOLCHAIN_COMMANDS = ("latexmk", "pdflatex", "kpsewhich")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def load_environment() -> dict[str, str]:
    values: dict[str, str] = {}
    for raw in (ROOT / "reproducible-build.env").read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if line and not line.startswith("#"):
            key, value = line.split("=", 1)
            values[key] = value
    if values != EXPECTED_ENV:
        raise SystemExit("Reproducibility environment differs from its frozen values")
    return values


def toolchain_identity() -> dict[str, str]:
    identity: dict[str, str] = {}
    for command in TOOLCHAIN_COMMANDS:
        executable = shutil.which(command)
        if executable is None:
            raise SystemExit(f"Missing reproducibility tool: {command}")
        result = subprocess.run(
            [command, "--version"],
            check=False,
            text=True,
            capture_output=True,
        )
        if result.returncode != 0:
            raise SystemExit(f"Could not query toolchain version: {command}")
        version = next(
            (line.strip() for line in (result.stdout + result.stderr).splitlines() if line.strip()),
            "",
        )
        if not version:
            raise SystemExit(f"Toolchain version output is empty: {command}")
        identity[command] = version
        identity[f"{command}_path"] = executable
        identity[f"{command}_sha256"] = sha256(Path(executable).resolve())
    return identity


def copy_native(destination: Path, relative_paths: list[str]) -> None:
    for relative in relative_paths:
        if relative == "reproducible-build.env":
            continue
        source = (ROOT / relative).resolve(strict=True)
        try:
            source.relative_to(LATEX.resolve())
        except ValueError as error:
            raise SystemExit(f"Isolated build input is outside latex/: {relative}") from error
        target = destination / source.relative_to(LATEX.resolve())
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, target)


def pages(pdf: Path) -> int:
    result = subprocess.run(["pdfinfo", str(pdf)], check=True, text=True, capture_output=True)
    for line in result.stdout.splitlines():
        if line.startswith("Pages:"):
            return int(line.split(":", 1)[1].strip())
    raise SystemExit(f"Could not read page count: {pdf}")


def build(destination: Path, entry: str, environment: dict[str, str]) -> dict[str, object]:
    env = os.environ.copy()
    env.update(environment)
    result = subprocess.run(
        ["latexmk", "-g", "-pdf", "-interaction=nonstopmode", "-halt-on-error", entry],
        cwd=destination,
        env=env,
        text=True,
        capture_output=True,
    )
    if result.returncode:
        raise SystemExit((result.stdout + "\n" + result.stderr)[-5000:])
    pdf = destination / f"{Path(entry).stem}.pdf"
    if not pdf.is_file() or pdf.stat().st_size == 0:
        raise SystemExit(f"Isolated build produced no PDF: {pdf}")
    return {"sha256": sha256(pdf), "bytes": pdf.stat().st_size, "pages": pages(pdf)}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--edition", choices=("base", "implicit"), required=True)
    parser.add_argument("--current-pdf", type=Path, required=True)
    parser.add_argument("--input-manifest", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    environment = load_environment()
    if not args.current_pdf.is_file() or args.current_pdf.stat().st_size == 0:
        raise SystemExit(f"Missing compiled PDF: {args.current_pdf}")
    try:
        input_manifest = json.loads(args.input_manifest.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise SystemExit(f"Cannot read build-input manifest: {error}") from error
    manifest_failures = validate_manifest(input_manifest, edition=args.edition, pdf=args.current_pdf)
    if manifest_failures:
        raise SystemExit("\n".join(manifest_failures))
    relative_paths = [str(item["path"]) for item in input_manifest["files"]]
    expected_paths = expected_compiled_inputs(args.edition)
    actual_paths = set(relative_paths)
    if actual_paths != expected_paths:
        missing = sorted(expected_paths - actual_paths)
        unexpected = sorted(actual_paths - expected_paths)
        raise SystemExit(
            "Reproducibility input closure mismatch: "
            f"missing={missing}; unexpected={unexpected}"
        )
    toolchain = toolchain_identity()
    entry = "master.tex" if args.edition == "base" else "master-implicit.tex"
    with tempfile.TemporaryDirectory(prefix=f"banks-{args.edition}-repro-") as temporary:
        first = Path(temporary) / "first"
        second = Path(temporary) / "second"
        first.mkdir()
        second.mkdir()
        copy_native(first, relative_paths)
        copy_native(second, relative_paths)
        first_build = build(first, entry, environment)
        second_build = build(second, entry, environment)
    current_hash = sha256(args.current_pdf)
    hashes = {current_hash, str(first_build["sha256"]), str(second_build["sha256"])}
    if len(hashes) != 1 or first_build != second_build:
        raise SystemExit(
            "Reproducibility failure:\n"
            + json.dumps(
                {"current": current_hash, "first": first_build, "second": second_build},
                indent=2,
                sort_keys=True,
            )
        )
    record = {
        "schema_version": 1,
        "edition": args.edition,
        "status": "pass",
        "environment": environment,
        "toolchain": toolchain,
        "entry": entry,
        "input_manifest_sha256": sha256(args.input_manifest),
        "build_input_sha256": input_manifest["build_input_sha256"],
        "pdf_sha256": current_hash,
        "builds": [first_build, second_build],
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(record, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"Reproducibility passes: {current_hash}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
