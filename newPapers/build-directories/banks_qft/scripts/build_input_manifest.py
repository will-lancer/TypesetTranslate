#!/usr/bin/env python3
"""Hash the native files recorded by a LaTeX build."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LATEX = ROOT / "latex"
REPRODUCIBILITY_ENV = "reproducible-build.env"

# The local closure is intentionally explicit.  A recursive scan would make a
# deleted or orphaned source file invisible to the release audit.  Keep this
# list in source order by unit; the digest itself is path-sorted below.
CHAPTER_FILES = {
    "chapter01": ("opening.tex", "sec1_1.tex", "sec1_2.tex"),
    "chapter02": ("opening.tex", "sec2_1.tex", "problems.tex"),
    "chapter03": (
        "opening.tex",
        "sec3_2.tex",
        "sec3_3.tex",
        "sec3_4.tex",
        "sec3_5.tex",
        "sec3_6.tex",
        "sec3_7.tex",
        "problems.tex",
    ),
    "chapter04": ("sec4_1.tex", "sec4_2.tex", "sec4_3.tex", "problems.tex"),
    "chapter05": ("opening.tex", "sec5_1.tex", "sec5_2.tex", "sec5_3.tex", "problems.tex"),
    "chapter06": (
        "opening.tex",
        "sec6_1.tex",
        "sec6_2.tex",
        "sec6_3.tex",
        "sec6_4.tex",
        "problems.tex",
    ),
    "chapter07": (
        "opening.tex",
        "sec7_1.tex",
        "sec7_2.tex",
        "sec7_3.tex",
        "sec7_4.tex",
        "problems.tex",
    ),
    "chapter08": (
        "opening.tex",
        "sec8_1.tex",
        "sec8_2.tex",
        "sec8_3.tex",
        "sec8_4.tex",
        "sec8_5.tex",
        "sec8_6.tex",
        "sec8_7.tex",
        "sec8_8.tex",
        "sec8_9.tex",
        "problems.tex",
    ),
    "chapter09": (
        "opening.tex",
        "sec9_1.tex",
        "sec9_2.tex",
        "sec9_3.tex",
        "sec9_4.tex",
        "sec9_5.tex",
        "sec9_6.tex",
        "sec9_7.tex",
        "sec9_8.tex",
        "sec9_9.tex",
        "sec9_10.tex",
        "sec9_11.tex",
        "sec9_12.tex",
        "sec9_13.tex",
        "sec9_14.tex",
        "sec9_15.tex",
        "problems.tex",
    ),
    "chapter10": (
        "sec10_1.tex",
        "sec10_2.tex",
        "sec10_3.tex",
        "sec10_4.tex",
        "sec10_5.tex",
        "sec10_6.tex",
        "sec10_7.tex",
        "sec10_8.tex",
        "problems.tex",
    ),
    "chapter11": ("chapter11.tex",),
}

APPENDIX_FILES = tuple(f"appendix{letter}.tex" for letter in "ABCDEF")
BACKMATTER_FILES = ("references.tex", "author-index.tex", "subject-index.tex")
FIGURE_FILES = (
    "appendixD.tex",
    "chapter01-fig-1-1.tex",
    "chapter01-fig-1-2.tex",
    "chapter03-connected-graphs.tex",
    "chapter03-fig-3-1.tex",
    "chapter04-massive-photon-propagator.tex",
    "chapter05-dirac-propagator.tex",
    "chapter06-fermion-gauge-vertex.tex",
    "chapter06-fig6.1.tex",
    "chapter06-fig6.2.tex",
    "chapter06-fig6.3.tex",
    "chapter06-fig6.4.tex",
    "chapter07-figure-7-1.tex",
    "chapter07-figure-7-2.tex",
    "chapter08-figure-8-1.tex",
    "chapter08-figure-8-2.tex",
    "chapter08-figure-8-3.tex",
    "chapter09-fig910.tex",
    "chapter09-fig94.tex",
    "chapter09-fig95.tex",
    "chapter09-fig96.tex",
    "chapter09-fig97.tex",
    "chapter09-fig98.tex",
    "chapter09-fig99.tex",
    "figure9_1.tex",
    "figure9_2.tex",
    "figure9_3.tex",
)
NUMBERED_SOLUTION_FILES = tuple(
    f"chapter{number:02d}-numbered.tex" for number in range(2, 11)
)
COMMON_LOCAL_INPUTS = {
    "latex/book.tex",
    "latex/banks.sty",
    "latex/jheppub.sty",
    "latex/frontmatter/editorial-note.tex",
    *(f"latex/chapters/{chapter}/{name}" for chapter, names in CHAPTER_FILES.items() for name in names),
    *(f"latex/appendices/{name}" for name in APPENDIX_FILES),
    *(f"latex/backmatter/{name}" for name in BACKMATTER_FILES),
    *(f"latex/figures/{name}" for name in FIGURE_FILES),
    *(f"latex/solutions/{name}" for name in NUMBERED_SOLUTION_FILES),
}

GENERATED_INPUT_ENDINGS = (
    ".aux",
    ".bbl",
    ".bcf",
    ".blg",
    ".dvi",
    ".fdb_latexmk",
    ".fls",
    ".glg",
    ".glo",
    ".gls",
    ".idx",
    ".ilg",
    ".ind",
    ".log",
    ".lof",
    ".lol",
    ".lot",
    ".nav",
    ".out",
    ".run.xml",
    ".snm",
    ".synctex",
    ".synctex.gz",
    ".toc",
    ".vrb",
)
HEX64_RE = re.compile(r"^[0-9a-f]{64}$")
SYSTEM_INPUT_PREFIXES = (
    Path("/System"),
    Path("/Library"),
    Path("/opt"),
    Path("/nix"),
    Path("/private/var"),
    Path("/usr"),
)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def is_generated_input(path: Path) -> bool:
    name = path.name.lower()
    return any(name.endswith(ending) for ending in GENERATED_INPUT_ENDINGS)


def expected_compiled_inputs(edition: str) -> set[str]:
    """Return the exact root-relative local closure for one entry point."""

    if edition not in {"base", "implicit"}:
        raise ValueError(f"Unknown edition: {edition}")
    expected = set(COMMON_LOCAL_INPUTS)
    expected.add("latex/master.tex" if edition == "base" else "latex/master-implicit.tex")
    expected.add(REPRODUCIBILITY_ENV)
    if edition == "implicit":
        inventory_path = ROOT / "implicit-exercises.json"
        inventory = json.loads(inventory_path.read_text(encoding="utf-8"))
        if not isinstance(inventory, list):
            raise ValueError("implicit-exercises.json must contain an array")
        identifiers = []
        units = set()
        for row in inventory:
            if not isinstance(row, dict):
                raise ValueError("implicit-exercises.json contains a non-object row")
            identifier = str(row.get("id", ""))
            unit = str(row.get("unit", ""))
            if not re.fullmatch(r"I-[A-Z0-9-]+", identifier):
                raise ValueError(f"Invalid implicit exercise ID: {identifier!r}")
            if not re.fullmatch(r"chapter(?:0[2-9]|10|11)|appendix[CE]", unit):
                raise ValueError(f"Invalid implicit exercise unit: {unit!r}")
            identifiers.append(identifier)
            units.add(unit)
        if len(identifiers) != len(set(identifiers)):
            raise ValueError("implicit-exercises.json contains duplicate IDs")
        expected.update(f"latex/implicit/{identifier}.tex" for identifier in identifiers)
        expected.update(f"latex/solutions/{unit}-implicit.tex" for unit in units)
    return expected


def _resolve_fls_path(value: str) -> Path:
    path = Path(value)
    if not path.is_absolute():
        path = LATEX / path
    return path


def _is_under(path: Path, parent: Path) -> bool:
    try:
        path.relative_to(parent)
    except ValueError:
        return False
    return True


def recorded_inputs(fls: Path) -> list[Path]:
    paths: set[Path] = set()
    for raw in fls.read_text(encoding="utf-8", errors="replace").splitlines():
        if not raw.startswith("INPUT "):
            continue
        candidate = _resolve_fls_path(raw[6:])
        if is_generated_input(candidate):
            continue
        try:
            path = candidate.resolve(strict=True)
        except FileNotFoundError:
            # TeX may probe for an optional generated file.  A missing native
            # or system input is still a failed build and must not disappear.
            if not is_generated_input(candidate):
                raise SystemExit(f"Recorded input does not exist: {candidate}")
            continue
        if _is_under(path, ROOT):
            if path.is_file():
                paths.add(path)
            continue
        # TeX Live and other system inputs are expected.  Any external
        # project-local input is outside the frozen build contract.
        if not any(_is_under(path, prefix) for prefix in SYSTEM_INPUT_PREFIXES):
            raise SystemExit(f"External non-system input is forbidden: {path}")
    env = (ROOT / REPRODUCIBILITY_ENV).resolve(strict=True)
    paths.add(env)
    return sorted(paths, key=lambda item: item.relative_to(ROOT).as_posix())


def input_digest(files: list[dict[str, object]]) -> str:
    combined = hashlib.sha256()
    for item in sorted(files, key=lambda row: str(row["path"])):
        relative = str(item["path"])
        file_hash = str(item["sha256"])
        combined.update(relative.encode("utf-8"))
        combined.update(b"\0")
        combined.update(file_hash.encode("ascii"))
        combined.update(b"\n")
    return combined.hexdigest()


def validate_manifest(
    manifest: object,
    *,
    edition: str | None = None,
    pdf: Path | None = None,
) -> list[str]:
    """Validate manifest structure, hashes, and root confinement."""

    failures: list[str] = []
    if not isinstance(manifest, dict):
        return ["Build-input manifest must be a JSON object"]
    if manifest.get("schema_version") != 1:
        failures.append("Build-input manifest schema_version must be 1")
    if edition is not None and manifest.get("edition") != edition:
        failures.append(f"Build-input manifest edition must be {edition}")
    rows = manifest.get("files")
    if not isinstance(rows, list):
        return failures + ["Build-input manifest files must be an array"]
    if manifest.get("file_count") != len(rows):
        failures.append("Build-input manifest file_count is inconsistent")

    paths: list[str] = []
    valid_rows: list[dict[str, object]] = []
    for index, raw in enumerate(rows, 1):
        if not isinstance(raw, dict):
            failures.append(f"Build-input manifest row {index} is not an object")
            continue
        relative = raw.get("path")
        digest = raw.get("sha256")
        size = raw.get("bytes")
        if not isinstance(relative, str) or not relative or Path(relative).is_absolute():
            failures.append(f"Build-input manifest row {index} has an invalid path")
            continue
        paths.append(relative)
        valid_rows.append(raw)
        if not isinstance(digest, str) or HEX64_RE.fullmatch(digest) is None:
            failures.append(f"Build-input manifest row {index} has an invalid SHA-256")
        if type(size) is not int or size <= 0:
            failures.append(f"Build-input manifest row {index} has an invalid byte count")
        candidate = ROOT / relative
        try:
            resolved = candidate.resolve(strict=True)
            resolved.relative_to(ROOT)
        except (FileNotFoundError, ValueError):
            failures.append(f"Build-input manifest row {index} escapes or lacks a local file: {relative}")
            continue
        if candidate.is_symlink() or not candidate.is_file():
            failures.append(f"Build-input manifest row {index} is not a regular file: {relative}")
            continue
        if isinstance(digest, str) and HEX64_RE.fullmatch(digest) and sha256(candidate) != digest:
            failures.append(f"Build-input manifest hash mismatch: {relative}")
        if type(size) is int and candidate.stat().st_size != size:
            failures.append(f"Build-input manifest byte-count mismatch: {relative}")

    if paths != sorted(paths):
        failures.append("Build-input manifest paths are not in lexical order")
    if len(paths) != len(set(paths)):
        failures.append("Build-input manifest contains duplicate paths")
    digest = manifest.get("build_input_sha256")
    if not isinstance(digest, str) or HEX64_RE.fullmatch(digest) is None:
        failures.append("Build-input manifest has an invalid build_input_sha256")
    elif valid_rows and input_digest(valid_rows) != digest:
        failures.append("Build-input manifest build_input_sha256 does not match its rows")
    pdf_hash = manifest.get("pdf_sha256")
    pdf_bytes = manifest.get("pdf_bytes")
    if not isinstance(pdf_hash, str) or HEX64_RE.fullmatch(pdf_hash) is None:
        failures.append("Build-input manifest has an invalid pdf_sha256")
    if type(pdf_bytes) is not int or pdf_bytes <= 0:
        failures.append("Build-input manifest has an invalid pdf_bytes")
    if pdf is not None and pdf.is_file():
        if isinstance(pdf_hash, str) and HEX64_RE.fullmatch(pdf_hash) and sha256(pdf) != pdf_hash:
            failures.append("Build-input manifest PDF hash does not match the compiled PDF")
        if type(pdf_bytes) is int and pdf.stat().st_size != pdf_bytes:
            failures.append("Build-input manifest PDF byte count does not match the compiled PDF")
    return failures


def create_manifest(edition: str, fls: Path, pdf: Path) -> dict[str, object]:
    files = []
    for path in recorded_inputs(fls):
        relative = path.relative_to(ROOT).as_posix()
        file_hash = sha256(path)
        size = path.stat().st_size
        files.append({"path": relative, "sha256": file_hash, "bytes": size})
    return {
        "schema_version": 1,
        "edition": edition,
        "build_input_sha256": input_digest(files),
        "file_count": len(files),
        "files": files,
        "pdf_sha256": sha256(pdf),
        "pdf_bytes": pdf.stat().st_size,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--edition", choices=("base", "implicit"), required=True)
    parser.add_argument("--fls", type=Path, required=True)
    parser.add_argument("--pdf", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    for path in (args.fls, args.pdf):
        if not path.is_file() or path.stat().st_size == 0:
            raise SystemExit(f"Missing build artifact: {path}")
    manifest = create_manifest(args.edition, args.fls, args.pdf)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"Build-input SHA-256: {manifest['build_input_sha256']}")
    print(f"PDF SHA-256: {manifest['pdf_sha256']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
