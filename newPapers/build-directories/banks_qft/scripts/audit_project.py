#!/usr/bin/env python3
"""Fail-closed structural audit for the Banks QFT editions."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LATEX = ROOT / "latex"
SOURCE_MARKER_RE = re.compile(
    r"^% BANKS-SOURCE: pdf=(\d+) print=(\S+) kind=(\S+)(?: id=(\S+))?[ \t]*$",
    re.MULTILINE,
)
PROBLEM_RE = re.compile(r"\\BanksProblem\{([^{}]+)\}\{([^{}]*)\}")
SOLUTION_RE = re.compile(r"\\BanksSolution\{([^{}]+)\}")
IMPLICIT_RE = re.compile(
    r"\\begin\{exercise\}(?:\[[^\]]*\])?\{([^{}]+)\}"
    r"|\\begin\{exercise\}\[[^\]]*\]\{([^{}]+)\}"
)
IMPLICIT_SOLUTION_RE = re.compile(r"\\BanksImplicitSolution\{([^{}]+)\}")
LABEL_RE = re.compile(r"\\label\{([^{}]+)\}")
INPUT_RE = re.compile(r"\\input\{([^{}]+)\}")
BIBITEM_RE = re.compile(r"\\bibitem\{banks-ref-(\d+)\}")
CITE_RE = re.compile(r"\\cite(?:\[[^\]]*\])?\{([^{}]+)\}")
HOOK_RE = re.compile(r"\\BanksImplicitHook\{([^{}]+)\}")
PLACEHOLDER_RE = re.compile(
    r"\b(?:TODO|TBD|FIXME|solution goes here|insert text|placeholder)\b",
    re.IGNORECASE,
)


class Audit:
    def __init__(self, strict: bool) -> None:
        self.strict = strict
        self.failures: list[str] = []
        self.warnings: list[str] = []

    def require(self, condition: bool, message: str, *, incomplete: bool = False) -> None:
        if condition:
            return
        if incomplete and not self.strict:
            self.warnings.append(message)
        else:
            self.failures.append(message)


def read_json(path: Path) -> list[dict[str, object]]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, list):
        raise ValueError(f"Expected a JSON array in {path}")
    return value


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def input_names(text: str) -> list[str]:
    uncommented = "\n".join(re.split(r"(?<!\\)%", line, maxsplit=1)[0] for line in text.splitlines())
    return INPUT_RE.findall(uncommented)


def edition_sources(edition: str) -> tuple[dict[Path, str], list[Path]]:
    """Return the exact native TeX closure selected by an edition entry point."""
    entry = LATEX / ("master.tex" if edition == "base" else "master-implicit.tex")
    pending = [entry, LATEX / "banks.sty", LATEX / "jheppub.sty"]
    if edition == "implicit":
        for row in read_json(ROOT / "implicit-exercises.json"):
            pending.append(LATEX / "implicit" / f"{row['id']}.tex")
    sources: dict[Path, str] = {}
    missing: list[Path] = []
    while pending:
        path = pending.pop()
        if path in sources or path in missing:
            continue
        if not path.is_file():
            missing.append(path)
            continue
        text = path.read_text(encoding="utf-8")
        sources[path] = text
        for name in input_names(text):
            if "#" in name:
                continue
            relative = Path(name)
            if not relative.suffix:
                relative = relative.with_suffix(".tex")
            if edition == "base" and (
                relative.parts[:1] == ("implicit",) or relative.stem.endswith("-implicit")
            ):
                continue
            pending.append(LATEX / relative)
    return dict(sorted(sources.items())), sorted(missing)


def native_snapshot_sha256(edition: str) -> str:
    sources, missing = edition_sources(edition)
    if missing:
        return "missing-inputs"
    support = [
        ROOT / "ERRATA.md",
        ROOT / "AUTHORING_CONVENTIONS.md",
        ROOT / "NOTATION.md",
        ROOT / "SOURCE_MANIFEST.yaml",
        ROOT / "SOURCE_MAP.md",
        ROOT / "TRANSCRIPTION_CONTRACT.md",
        ROOT / "TRANSCRIPTION_STATUS.md",
        ROOT / "explicit-problems.json",
        ROOT / "figures.json",
        ROOT / "implicit-exercises.json",
        ROOT / "numbered-equations.json",
        ROOT / "page-dispositions.jsonl",
        ROOT / "query-ledger.json",
        ROOT / "unnumbered-diagrams.json",
        ROOT / "reproducible-build.env",
    ]
    digest = hashlib.sha256()
    for path in sorted([*sources, *support], key=lambda item: item.relative_to(ROOT).as_posix()):
        relative = path.relative_to(ROOT).as_posix()
        digest.update(relative.encode("utf-8"))
        digest.update(b"\0")
        digest.update(sha256(path).encode("ascii"))
        digest.update(b"\n")
    return digest.hexdigest()


def content_inputs() -> list[str]:
    book = (LATEX / "book.tex").read_text(encoding="utf-8")
    return [name for name in INPUT_RE.findall(book) if name != "frontmatter/editorial-note.tex"]


def marker_audit(audit: Audit, sources: dict[Path, str]) -> None:
    rows = [
        json.loads(line)
        for line in (ROOT / "page-dispositions.jsonl").read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    audit.require(len(rows) == 281, "Disposition ledger must contain 281 records")
    audit.require(
        [row.get("pdf_page") for row in rows] == list(range(1, 282)),
        "Disposition pages must cover 1 through 281 exactly once",
    )
    for row in rows:
        page = int(row["pdf_page"])
        if page >= 11:
            audit.require(
                row.get("printed_page") == page - 10,
                f"Bad printed-page disposition for PDF page {page}",
            )
    required = {
        int(row["pdf_page"])
        for row in rows
        if row.get("disposition") in {"native", "generated"}
    }
    seen: set[int] = set()
    for path, text in sources.items():
        for match in SOURCE_MARKER_RE.finditer(text):
            page = int(match.group(1))
            audit.require(1 <= page <= 281, f"Out-of-range source marker in {path}: {page}")
            printed = match.group(2)
            if page >= 11:
                audit.require(
                    printed.isdigit() and int(printed) == page - 10,
                    f"Bad marker page offset in {path}: PDF {page}, print {printed}",
                )
            seen.add(page)
    missing = sorted(required - seen)
    audit.require(
        not missing,
        f"Included source pages lack BANKS-SOURCE markers: {missing}",
        incomplete=True,
    )


def assembly_audit(audit: Audit, missing: list[Path]) -> None:
    audit.require(not missing, f"Selected master has missing native inputs: {[str(path) for path in missing]}")
    inputs = content_inputs()
    duplicates = [name for name, count in Counter(inputs).items() if count > 1]
    audit.require(not duplicates, f"Duplicate book inputs: {duplicates}")
    for name in inputs:
        path = LATEX / name
        if not path.suffix:
            path = LATEX / f"{name}.tex"
        implicit = Path(name).stem.endswith("-implicit")
        if implicit and getattr(audit, "edition", "base") == "base":
            continue
        if path.exists():
            audit.require(path.stat().st_size > 30, f"Empty content file: {path}", incomplete=True)
        else:
            audit.require(False, f"Missing content file: {path}", incomplete=True)


def source_unit(path: Path) -> str | None:
    """Return the chapter or appendix unit containing a source hook."""
    try:
        relative = path.relative_to(LATEX)
    except ValueError:
        return None
    if len(relative.parts) >= 2 and relative.parts[0] in {"chapters", "appendices"}:
        return relative.parts[1] if relative.parts[0] == "chapters" else Path(relative.parts[1]).stem
    return None


def hook_placement_audit(
    audit: Audit,
    sources: dict[Path, str],
    implicit: list[dict[str, object]],
) -> None:
    """Bind each implicit hook to its inventory unit and nearby source-page marker."""
    rows_by_id = {str(row.get("id", "")): row for row in implicit}
    for path, text in sources.items():
        for match in HOOK_RE.finditer(text):
            identifier = match.group(1)
            row = rows_by_id.get(identifier)
            if row is None:
                continue

            expected_unit = str(row.get("unit", "")).strip()
            audit.require(
                bool(expected_unit) and source_unit(path) == expected_unit,
                f"Implicit hook {identifier} is in {path} but inventory unit is {expected_unit}",
                incomplete=True,
            )

            raw_pages = row.get("pdf_pages")
            expected_pages: set[int] = set()
            if isinstance(raw_pages, list):
                try:
                    expected_pages = {int(page) for page in raw_pages}
                except (TypeError, ValueError):
                    expected_pages = set()
            audit.require(
                bool(expected_pages),
                f"Implicit hook {identifier} has no valid inventory PDF locator",
                incomplete=True,
            )

            anchor = str(row.get("placement_anchor", "")).strip()
            anchor_match = re.fullmatch(r"([^:]+):pdf-(\d+)(?:-(\d+))?(?::.*)?", anchor)
            audit.require(
                anchor_match is not None,
                f"Implicit hook {identifier} has an invalid placement anchor",
                incomplete=True,
            )
            if anchor_match is not None:
                anchor_unit, anchor_start, anchor_end = anchor_match.groups()
                anchor_pages = range(int(anchor_start), int(anchor_end or anchor_start) + 1)
                audit.require(
                    anchor_unit == expected_unit
                    and any(page in expected_pages for page in anchor_pages),
                    f"Implicit locator disagrees with placement anchor for {identifier}",
                    incomplete=True,
                )

            preceding = list(SOURCE_MARKER_RE.finditer(text[:match.start()]))
            following = list(SOURCE_MARKER_RE.finditer(text[match.end():]))
            neighboring_pages = [int(item.group(1)) for item in preceding[-1:] + following[:1]]
            audit.require(
                bool(neighboring_pages),
                f"Implicit hook {identifier} has no nearby BANKS-SOURCE marker in {path}",
                incomplete=True,
            )
            audit.require(
                any(abs(marker_page - expected_page) <= 1
                    for marker_page in neighboring_pages
                    for expected_page in expected_pages),
                f"Implicit hook {identifier} is not adjacent to its inventory PDF page",
                incomplete=True,
            )


def inventory_audit(audit: Audit, sources: dict[Path, str]) -> None:
    joined = "\n".join(sources.values())
    explicit = read_json(ROOT / "explicit-problems.json")
    expected_ids = [str(row["id"]) for row in explicit]
    audit.require(len(explicit) == 80, "Explicit inventory must contain 80 records")
    audit.require(len(set(expected_ids)) == 80, "Explicit inventory IDs must be unique")
    audit.require(sum(bool(row["starred"]) for row in explicit) == 65, "Explicit inventory must preserve 65 stars")
    for row in explicit:
        audit.require(int(row["pdf_page"]) == int(row["printed_page"]) + 10, f"Bad explicit page offset: {row['id']}")

    problems = PROBLEM_RE.findall(joined)
    problem_ids = [item[0] for item in problems]
    solutions = SOLUTION_RE.findall(joined)
    audit.require(len(problem_ids) == len(set(problem_ids)), "Duplicate BanksProblem IDs")
    audit.require(len(solutions) == len(set(solutions)), "Duplicate BanksSolution IDs")
    audit.require(
        problem_ids == expected_ids,
        f"Explicit problem sequence differs from inventory: found {len(problem_ids)}",
        incomplete=True,
    )
    audit.require(
        solutions == expected_ids,
        f"Explicit solution sequence differs from inventory: found {len(solutions)}",
        incomplete=True,
    )
    star_by_id = {item[0]: item[1] == "*" for item in problems}
    for row in explicit:
        if str(row["id"]) in star_by_id:
            audit.require(
                star_by_id[str(row["id"])] == bool(row["starred"]),
                f"Star mismatch for Problem {row['id']}",
            )

    implicit = read_json(ROOT / "implicit-exercises.json")
    implicit_ids = [str(row["id"]) for row in implicit]
    audit.require(len(implicit) == 110, "Implicit inventory must contain 110 records")
    audit.require(len(set(implicit_ids)) == 110, "Implicit inventory IDs must be unique")
    for row in implicit:
        printed = list(row["printed_pages"])
        pdf = list(row["pdf_pages"])
        audit.require(len(printed) == len(pdf), f"Implicit locator length mismatch: {row['id']}")
        audit.require(all(int(p) == int(q) + 10 for p, q in zip(pdf, printed)), f"Bad implicit page offset: {row['id']}")

    exercise_ids = [a or b for a, b in IMPLICIT_RE.findall(joined)]
    implicit_solutions = IMPLICIT_SOLUTION_RE.findall(joined)
    audit.require(len(exercise_ids) == len(set(exercise_ids)), "Duplicate implicit exercise IDs")
    audit.require(len(implicit_solutions) == len(set(implicit_solutions)), "Duplicate implicit solution IDs")
    if getattr(audit, "edition", "base") == "implicit":
        audit.require(
            set(exercise_ids) == set(implicit_ids) and len(exercise_ids) == len(implicit_ids),
            f"Implicit exercises differ from inventory: found {len(exercise_ids)}",
            incomplete=True,
        )

    hooks = HOOK_RE.findall(joined)
    audit.require(len(hooks) == len(set(hooks)), "Duplicate implicit hook IDs")
    audit.require(
        set(hooks) == set(implicit_ids) and len(hooks) == len(implicit_ids),
        f"Implicit hook anchors differ from inventory: found {len(hooks)}",
        incomplete=True,
    )
    hook_placement_audit(audit, sources, implicit)

    for path, text in sources.items():
        if "solutions" not in path.parts:
            continue
        matches = list(SOLUTION_RE.finditer(text))
        for index, match in enumerate(matches):
            end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
            body = text[match.end():end]
            body = re.sub(r"%.*", "", body)
            audit.require(
                len(body.strip()) >= 240,
                f"Numbered solution {match.group(1)} is too short for a checkable derivation",
                incomplete=True,
            )
        implicit_matches = list(IMPLICIT_SOLUTION_RE.finditer(text))
        for index, match in enumerate(implicit_matches):
            end = (
                implicit_matches[index + 1].start()
                if index + 1 < len(implicit_matches)
                else len(text)
            )
            body = re.sub(r"%.*", "", text[match.end():end])
            audit.require(
                len(body.strip()) >= 180,
                f"Implicit solution {match.group(1)} is too short for a checkable derivation",
                incomplete=True,
            )
    if getattr(audit, "edition", "base") == "implicit":
        audit.require(
            set(implicit_solutions) == set(implicit_ids)
            and len(implicit_solutions) == len(implicit_ids),
            f"Implicit solutions differ from inventory: found {len(implicit_solutions)}",
            incomplete=True,
        )


def object_audit(audit: Audit, sources: dict[Path, str]) -> None:
    joined = "\n".join(sources.values())
    labels = LABEL_RE.findall(joined)
    duplicate_labels = sorted(label for label, count in Counter(labels).items() if count > 1)
    audit.require(not duplicate_labels, f"Duplicate labels: {duplicate_labels}")
    audit.require(not PLACEHOLDER_RE.search(joined), "Placeholder token found in native source")
    audit.require("\\includepdf" not in joined, "Source PDF inclusion is forbidden")
    audit.require("\\includegraphics" not in joined, "Raster or external figure inclusion is forbidden")
    audit.require("banks-qft.pdf" not in joined, "Native TeX imports the canonical PDF")

    figures = read_json(ROOT / "figures.json")
    audit.require(len(figures) == 23, "Figure inventory must contain 23 records")
    figure_ids = [str(row.get("id", "")).strip() for row in figures]
    audit.require(all(figure_ids), "Figure inventory contains an empty ID")
    audit.require(len(figure_ids) == len(set(figure_ids)), "Figure inventory IDs must be unique")
    source_figure_ids = {
        label.removeprefix("fig:")
        for label in labels
        if label.startswith("fig:")
        and "#" not in label
    }
    audit.require(
        source_figure_ids == set(figure_ids) and len(source_figure_ids) == len(figure_ids),
        "Figure inventory must have one-to-one source figure labels",
        incomplete=True,
    )
    for identifier in figure_ids:
        label = f"fig:{identifier}"
        audit.require(label in labels, f"Missing source figure label {label}", incomplete=True)
    figure_by_id = {identifier: row for identifier, row in zip(figure_ids, figures)}
    # Appendix-D figure markers group several diagrams under descriptive IDs.
    inventory_marker_ids = {identifier for identifier in figure_ids if not identifier.startswith("D.")}
    source_figure_markers = [
        marker
        for text in sources.values()
        for marker in SOURCE_MARKER_RE.finditer(text)
        if marker.group(3) == "figure" and marker.group(4)
    ]
    numbered_figure_markers = [
        marker for marker in source_figure_markers if marker.group(4) in inventory_marker_ids
    ]
    audit.require(
        {marker.group(4) for marker in numbered_figure_markers} == inventory_marker_ids,
        "Numbered figure inventory must have source markers",
        incomplete=True,
    )
    for marker in numbered_figure_markers:
        identifier = marker.group(4)
        audit.require(
            int(marker.group(1)) == int(figure_by_id[identifier]["pdf_page"]),
            f"Figure source marker page disagrees with inventory: {identifier}",
        )

    numbered_equations: list[str] = []
    for text in sources.values():
        for marker in SOURCE_MARKER_RE.finditer(text):
            if marker.group(3) == "equation" and marker.group(4):
                numbered_equations.append(marker.group(4))
    expected_equations = [str(value) for value in read_json(ROOT / "numbered-equations.json")]
    audit.require(
        len(numbered_equations) == len(set(numbered_equations)),
        "Duplicate numbered-equation source markers",
    )
    audit.require(
        set(numbered_equations) == set(expected_equations)
        and len(numbered_equations) == len(expected_equations),
        f"Numbered-equation inventory differs from source markers: found {len(numbered_equations)}",
        incomplete=True,
    )
    for equation_id in expected_equations:
        audit.require(
            f"eq:{equation_id}" in labels,
            f"Numbered equation {equation_id} lacks label eq:{equation_id}",
            incomplete=True,
        )

    unnumbered = read_json(ROOT / "unnumbered-diagrams.json")
    audit.require(len(unnumbered) == 14, "Unnumbered diagram inventory must contain 14 records")
    unnumbered_ids = [str(row.get("id", "")).strip() for row in unnumbered]
    audit.require(all(unnumbered_ids), "Unnumbered diagram inventory contains an empty ID")
    audit.require(
        len(unnumbered_ids) == len(set(unnumbered_ids)),
        "Unnumbered diagram inventory IDs must be unique",
    )
    for row in unnumbered:
        identifier = str(row.get("id", "")).strip()
        try:
            pdf_page = int(row["pdf_page"])
            printed_page = int(row["printed_page"])
        except (KeyError, TypeError, ValueError):
            audit.require(False, f"Unnumbered diagram {identifier} has an invalid page locator")
            continue
        audit.require(
            pdf_page == printed_page + 10,
            f"Bad unnumbered-diagram page offset: {identifier}",
        )
    source_unnumbered_ids = [
        marker.group(4)
        for text in sources.values()
        for marker in SOURCE_MARKER_RE.finditer(text)
        if marker.group(3) == "figure"
        and marker.group(4)
        and marker.group(4).startswith("unnumbered-")
    ]
    # The three main-text records use the exact source-marker ID. Appendix-D
    # records have descriptive source markers, so their IDs are not comparable.
    inventory_unnumbered_ids = {
        identifier for identifier in unnumbered_ids if identifier.startswith("unnumbered-main-")
    }
    audit.require(
        len(source_unnumbered_ids) == len(set(source_unnumbered_ids)),
        "Duplicate source markers for inventory-addressable unnumbered diagrams",
    )
    audit.require(
        set(source_unnumbered_ids) == inventory_unnumbered_ids
        and len(source_unnumbered_ids) == len(inventory_unnumbered_ids),
        "Inventory-addressable unnumbered diagrams must have one-to-one source markers",
        incomplete=True,
    )
    unnumbered_by_id = {identifier: row for identifier, row in zip(unnumbered_ids, unnumbered)}
    for text in sources.values():
        for marker in SOURCE_MARKER_RE.finditer(text):
            identifier = marker.group(4)
            if marker.group(3) != "figure" or identifier not in inventory_unnumbered_ids:
                continue
            audit.require(
                int(marker.group(1)) == int(unnumbered_by_id[identifier]["pdf_page"]),
                f"Unnumbered-diagram source marker page disagrees with inventory: {identifier}",
            )

    bibliography = [int(value) for value in BIBITEM_RE.findall(joined)]
    audit.require(
        bibliography == list(range(1, 181)),
        f"Bibliography sequence must be banks-ref-1 through banks-ref-180; found {len(bibliography)}",
        incomplete=True,
    )
    for citation in CITE_RE.findall(joined):
        for key in (item.strip() for item in citation.split(",")):
            match = re.fullmatch(r"banks-ref-(\d+)", key)
            audit.require(match is not None, f"Noncanonical bibliography key: {key}")
            if match is not None:
                audit.require(1 <= int(match.group(1)) <= 180, f"Citation key out of range: {key}")


def checked_report(audit: Audit, item: dict[str, object], label: str) -> str:
    reviewer = str(item.get("reviewer", "")).strip()
    report_name = str(item.get("report", "")).strip()
    audit.require(bool(reviewer), f"{label} lacks a reviewer")
    audit.require(item.get("status") == "pass", f"{label} did not pass")
    if not report_name:
        audit.require(False, f"{label} lacks a report path")
        return reviewer
    report = (ROOT / report_name).resolve()
    try:
        report.relative_to(ROOT.resolve())
    except ValueError:
        audit.require(False, f"{label} report escapes the package root")
        return reviewer
    audit.require(report.is_file() and report.stat().st_size > 0, f"Missing {label} report: {report_name}")
    if report.is_file():
        audit.require(item.get("report_sha256") == sha256(report), f"{label} report hash mismatch")
        body = report.read_text(encoding="utf-8", errors="replace")
        audit.require(
            re.search(r"^FINAL STATUS:\s*PASS\s*$", body, re.MULTILINE) is not None,
            f"{label} report has no machine-readable PASS verdict",
        )
    return reviewer


def ledger_audit(audit: Audit) -> None:
    query_path = ROOT / "query-ledger.json"
    audit.require(query_path.is_file(), "Missing structured query ledger", incomplete=True)
    if query_path.is_file():
        query_rows = json.loads(query_path.read_text(encoding="utf-8"))
        audit.require(isinstance(query_rows, list), "Structured query ledger must be a JSON array")
        if isinstance(query_rows, list):
            unresolved = [row for row in query_rows if not isinstance(row, dict) or row.get("status") != "closed"]
            audit.require(not unresolved, "Query ledger contains unresolved readings", incomplete=True)
    if audit.strict:
        edition = getattr(audit, "edition", "base")
        snapshot = native_snapshot_sha256(edition)
        review_path = ROOT / f"review-coverage-{edition}.json"
        audit.require(review_path.exists(), f"Missing {review_path.name}")
        if review_path.exists():
            review = json.loads(review_path.read_text(encoding="utf-8"))
            audit.require(review.get("schema_version") == 1, "Review coverage schema mismatch")
            audit.require(review.get("edition") == edition, "Review coverage edition mismatch")
            audit.require(review.get("status") == "pass", "Source review did not pass")
            audit.require(review.get("native_snapshot_sha256") == snapshot, "Source review does not bind the native snapshot")
            audit.require(
                review.get("source_sha256")
                == "31de7827e7bc636feaa7028fe4dbb63a718b3926ee43ff3d96d91185a44eafe3",
                "Review coverage source hash mismatch",
            )
            audit.require(review.get("source_pages_reviewed") == 281, "Source review coverage must be 281")
            audit.require(review.get("equations") == "pass", "Equation review must pass")
            audit.require(review.get("figures") == "23/23", "Figure review must be 23/23")
            audit.require(review.get("problems") == "80/80", "Problem review must be 80/80")
            ranges = review.get("source_ranges", [])
            covered: list[int] = []
            reviewers: set[str] = set()
            if isinstance(ranges, list):
                for index, item in enumerate(ranges, 1):
                    if not isinstance(item, dict):
                        continue
                    try:
                        start = int(item["start"])
                        end = int(item["end"])
                    except (KeyError, TypeError, ValueError):
                        continue
                    reviewer = checked_report(audit, item, f"source review range {index}")
                    if reviewer:
                        reviewers.add(reviewer)
                    if 1 <= start <= end <= 281:
                        covered.extend(range(start, end + 1))
            audit.require(
                sorted(covered) == list(range(1, 282)) and len(covered) == 281,
                "Source-review ranges must cover 1 through 281 exactly once",
            )
            audit.require(len(reviewers) >= 2, "Source review requires at least two independent reviewers")
            if edition == "implicit":
                audit.require(review.get("implicit") == "110/110", "Implicit review must be 110/110")
        solution_review_path = ROOT / f"solution-review-{edition}.json"
        audit.require(solution_review_path.exists(), f"Missing {solution_review_path.name}")
        if solution_review_path.exists():
            solution_review = json.loads(solution_review_path.read_text(encoding="utf-8"))
            audit.require(solution_review.get("schema_version") == 1, "Solution-review schema mismatch")
            audit.require(solution_review.get("edition") == edition, "Solution-review edition mismatch")
            audit.require(solution_review.get("status") == "pass", "Solution review did not pass")
            audit.require(
                solution_review.get("native_snapshot_sha256") == snapshot,
                "Solution review does not bind the native snapshot",
            )
            audit.require(solution_review.get("explicit") == "80/80", "Numbered solution review must be 80/80")
            solution_reviewers = solution_review.get("reviewers", [])
            reviewed_explicit: list[str] = []
            reviewed_implicit: list[str] = []
            reviewer_names: list[str] = []
            if isinstance(solution_reviewers, list):
                for index, item in enumerate(solution_reviewers, 1):
                    if not isinstance(item, dict):
                        audit.require(False, f"Solution reviewer {index} is not an object")
                        continue
                    reviewer_names.append(checked_report(audit, item, f"solution review {index}"))
                    explicit_ids = item.get("explicit_ids", [])
                    implicit_ids = item.get("implicit_ids", [])
                    if isinstance(explicit_ids, list):
                        reviewed_explicit.extend(str(value) for value in explicit_ids)
                    if isinstance(implicit_ids, list):
                        reviewed_implicit.extend(str(value) for value in implicit_ids)
                    report_name = str(item.get("report", ""))
                    report_path = ROOT / report_name
                    if report_path.is_file():
                        report_body = report_path.read_text(encoding="utf-8", errors="replace")
                        for identifier in [*explicit_ids, *implicit_ids]:
                            pattern = rf"(?<![A-Za-z0-9]){re.escape(str(identifier))}(?![A-Za-z0-9])"
                            audit.require(
                                re.search(pattern, report_body) is not None,
                                f"Solution report {report_name} does not mention {identifier}",
                            )
            audit.require(
                len(set(reviewer_names)) >= 2,
                "Solution review requires at least two independent reviewers",
            )
            expected_explicit = [str(row["id"]) for row in read_json(ROOT / "explicit-problems.json")]
            audit.require(
                sorted(reviewed_explicit) == sorted(expected_explicit) and len(reviewed_explicit) == len(expected_explicit),
                "Solution-review reports must cover every numbered solution exactly once",
            )
            if edition == "implicit":
                audit.require(
                    solution_review.get("implicit") == "110/110",
                    "Implicit solution review must be 110/110",
                )
                expected_implicit = [str(row["id"]) for row in read_json(ROOT / "implicit-exercises.json")]
                audit.require(
                    sorted(reviewed_implicit) == sorted(expected_implicit)
                    and len(reviewed_implicit) == len(expected_implicit),
                    "Solution-review reports must cover every implicit solution exactly once",
                )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--strict", action="store_true")
    parser.add_argument("--edition", choices=("base", "implicit"), default="base")
    args = parser.parse_args()

    audit = Audit(args.strict)
    audit.edition = args.edition
    sources, missing = edition_sources(args.edition)
    assembly_audit(audit, missing)
    marker_audit(audit, sources)
    inventory_audit(audit, sources)
    object_audit(audit, sources)
    ledger_audit(audit)

    for warning in audit.warnings:
        print(f"WARNING: {warning}", file=sys.stderr)
    for failure in audit.failures:
        print(f"FAIL: {failure}", file=sys.stderr)
    if audit.failures:
        print(f"project audit failed: {len(audit.failures)} failure(s)", file=sys.stderr)
        return 1
    print(
        f"project audit pass: edition={args.edition}; strict={args.strict}; "
        f"warnings={len(audit.warnings)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
