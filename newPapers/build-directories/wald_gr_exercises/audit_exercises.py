#!/usr/bin/env python3
"""Audit solution coverage, supplementary credits, and source preservation."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent
LATEX = ROOT / "latex"
EXERCISES = LATEX / "exercises"
CANONICAL = ROOT.parent / "wald_gr" / "latex"
EXPECTED = (1, 8, 8, 9, 5, 6, 5, 8, 3, 6, 6, 5, 8, 7)


def main() -> int:
    findings: list[str] = []
    ledger = json.loads((ROOT / "exercise-source-ledger.json").read_text())
    entries = {entry["id"]: entry for entry in ledger["entries"]}
    used_sources: set[str] = set()
    wald_total = 0
    supplementary_total = 0

    for chapter, count in enumerate(EXPECTED, start=1):
        directory = EXERCISES / f"chapter{chapter:02d}"
        wald_path = directory / "wald-solutions.tex"
        problem_path = directory / "supplementary-exercises.tex"
        solution_path = directory / "supplementary-solutions.tex"
        paths = (wald_path, problem_path, solution_path)
        missing = [path for path in paths if not path.exists()]
        if missing:
            findings.extend(f"Missing {path.relative_to(ROOT)}" for path in missing)
            continue

        wald_text = wald_path.read_text()
        numbers = [int(value) for value in re.findall(r"\\WaldSolution\{(\d+)\}", wald_text)]
        expected_numbers = list(range(1, count + 1))
        if numbers != expected_numbers:
            findings.append(f"Chapter {chapter}: Wald solution IDs {numbers}, expected {expected_numbers}")
        wald_total += len(numbers)

        problem_text = problem_path.read_text()
        solution_text = solution_path.read_text()
        problem_ids = re.findall(r"\\SupplementaryExercise\{(\d+)\}", problem_text)
        solution_ids = re.findall(r"\\SupplementarySolution\{(\d+)\}", solution_text)
        if not problem_ids or problem_ids != solution_ids:
            findings.append(f"Chapter {chapter}: supplementary IDs do not match")
        supplementary_total += len(problem_ids)

        source_ids = re.findall(
            r"\\SupplementaryExercise\{\d+\}\{.*?\}\{.*?\}\{([^{}]+)\}",
            problem_text,
            flags=re.DOTALL,
        )
        if len(source_ids) != len(problem_ids):
            findings.append(f"Chapter {chapter}: missing machine-readable source ID")
        for source_id in source_ids:
            used_sources.add(source_id)
            entry = entries.get(source_id)
            if entry is None:
                findings.append(f"Chapter {chapter}: source ID {source_id!r} absent from ledger")
                continue
            if entry["chapter"] != chapter:
                findings.append(f"Chapter {chapter}: ledger mismatch for {source_id}")
            source_path = entry.get("source_path")
            if source_path and not (ROOT / source_path).resolve().exists():
                findings.append(f"Chapter {chapter}: missing ledger source for {source_id}")

        joined = wald_text + problem_text + solution_text
        if re.search(r"\b(?:TODO|TBD|PLACEHOLDER)\b", joined, re.IGNORECASE):
            findings.append(f"Chapter {chapter}: placeholder text remains")

    if wald_total != sum(EXPECTED):
        findings.append(f"Wald solution total is {wald_total}, expected {sum(EXPECTED)}")
    if supplementary_total != 14:
        findings.append(f"Supplementary total is {supplementary_total}, expected 14")
    if used_sources != set(entries):
        findings.append("Supplementary source IDs and ledger IDs differ")

    for canonical_path in CANONICAL.rglob("*"):
        if not canonical_path.is_file():
            continue
        if canonical_path.suffix in {
            ".aux", ".fdb_latexmk", ".fls", ".log", ".out", ".pdf", ".toc"
        }:
            continue
        relative = canonical_path.relative_to(CANONICAL)
        edition_path = LATEX / relative
        if relative == Path("master.tex"):
            continue
        if re.fullmatch(r"chapters/chapter\d{2}\.tex", relative.as_posix()):
            if not edition_path.exists():
                findings.append(f"Missing edition wrapper {relative}")
                continue
            edition_text = re.sub(
                r"^\\chapterexercisehook\{\d{2}\}\n?", "", edition_path.read_text(), flags=re.MULTILINE
            )
            if edition_text != canonical_path.read_text():
                findings.append(f"Canonical wrapper changed beyond exercise hook: {relative}")
            continue
        if not edition_path.exists() or edition_path.read_bytes() != canonical_path.read_bytes():
            findings.append(f"Canonical content differs in exercise edition: {relative}")

    if findings:
        print("EXERCISE AUDIT FAILED", file=sys.stderr)
        for finding in findings:
            print(f"  - {finding}", file=sys.stderr)
        return 1

    print(f"Wald solutions: {wald_total}/{sum(EXPECTED)}")
    print(f"Supplementary problems with solutions: {supplementary_total}")
    print("Canonical-content guard: passed")
    print("Exercise source ledger: passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
