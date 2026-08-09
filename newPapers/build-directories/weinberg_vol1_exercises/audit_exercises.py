#!/usr/bin/env python3
"""Audit one independent Weinberg QFT exercise-edition source tree.

The audit has two modes. Draft mode reports incomplete editorial material
without blocking ordinary scaffold builds. Strict mode is the release gate:
every original and supplementary exercise must have one matching solution,
every source must resolve through the ledger, and every chapter must meet its
declared target or carry a written exception in ``exercise-edition.json``.
"""

from __future__ import annotations

import argparse
import difflib
import hashlib
import json
import re
import statistics
import sys
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable
from urllib.parse import urlparse


REQUIRED_FRAGMENT_FILES = (
    "weinberg-exercises.tex",
    "weinberg-solutions.tex",
    "supplementary-exercises.tex",
    "supplementary-solutions.tex",
)
REQUIRED_HEADINGS = (
    r"\chapterbackmatter{Weinberg Exercises}",
    r"\chapterbackmatter{Solutions to Weinberg Exercises}",
    r"\chapterbackmatter{Supplementary Exercises}",
    r"\chapterbackmatter{Solutions to Supplementary Exercises}",
)
REQUIRED_HOOK_INPUTS = tuple(
    rf"\input{{exercises/chapter#1/{filename}}}"
    for filename in REQUIRED_FRAGMENT_FILES
)
REQUIRED_ASYMPTOTIC_HELPERS = (
    r"\newcommand{\InKet}[1]{\ket{#1}_{\mathrm{in}}}",
    r"\newcommand{\InKetWith}[2]{\ket{#1}_{\mathrm{in},#2}}",
    r"\newcommand{\OutKet}[1]{\ket{#1}_{\mathrm{out}}}",
    r"\newcommand{\InBra}[1]{{}_{\mathrm{in}}\!\bra{#1}}",
    r"\newcommand{\OutBra}[1]{{}_{\mathrm{out}}\!\bra{#1}}",
    r"\newcommand{\InOutKet}[1]{\ket{#1}_{\mathrm{in/out}}}",
    r"\newcommand{\OutInKet}[1]{\ket{#1}_{\mathrm{out/in}}}",
    r"\newcommand{\InOutBra}[1]{{}_{\mathrm{in/out}}\!\bra{#1}}",
    r"\newcommand{\OutInBra}[1]{{}_{\mathrm{out/in}}\!\bra{#1}}",
)
BUILD_SUFFIXES = {
    ".aux",
    ".fdb_latexmk",
    ".fls",
    ".log",
    ".out",
    ".pdf",
    ".toc",
}
KNOWN_CHAPTER_RANGES = {
    "weinberg_vol1_exercises": (1, 14),
    "weinberg_vol2_exercises": (15, 23),
    "weinberg_vol3_exercises": (24, 32),
}
ZERO_TARGET_HISTORY_EXCEPTIONS = {
    (
        "weinberg_vol1_exercises",
        1,
    ): "Historical chapter: exercises are intentionally omitted at the user's direction.",
    (
        "weinberg_vol3_exercises",
        24,
    ): (
        "Historical chapter: supplementary exercises are intentionally omitted "
        "at the user's direction."
    ),
}
MIN_SUPPLEMENTARY_EXERCISES = 10
MAX_SUPPLEMENTARY_EXERCISES = 30
SOURCE_FAMILIES = {
    "mcgreevy",
    "harlow",
    "cambridge-part-iii",
    "knzhou",
    "other",
}
PREFERRED_SOURCE_FAMILIES = SOURCE_FAMILIES - {"other"}
USE_MODES = {
    "adapted",
    "original-inspired",
    "verbatim-permitted",
}
FIDELITY_AUDIT_STATUSES = {
    "passed",
    "pending",
    "rejected",
}
FIDELITY_CHECK_STATES = {
    "pass",
    "not-applicable",
    "pending",
    "fail",
}
FIDELITY_CHECKS = (
    "source_parent_complete",
    "setup_self_contained",
    "action_or_lagrangian",
    "conventions_and_definitions",
    "supplied_formulas_data_figures",
    "hints",
    "connected_subparts",
    "one_parent_one_number",
    "credit_and_locator",
    "chapter_fit_and_quality",
    "solution_coverage",
)
ISO_DATE_RE = re.compile(r"\A\d{4}-\d{2}-\d{2}\Z")
EXACT_PROBLEM_LOCATOR_RE = re.compile(
    r"\b(?:problem|question|exercise|exam(?:ination)?\s+question)\b",
    re.IGNORECASE,
)
EXACT_PARENT_ROOT_RE = re.compile(
    r"\b(?P<kind>problem|question|exercise|exam(?:ination)?\s+question)"
    r"\s*(?:no\.?\s*)?(?P<number>\d+(?:\.\d+)*[A-Za-z]?)\b",
    re.IGNORECASE,
)
PART_II_RE = re.compile(r"\bPart[\s~–—-]*II(?!I)\b", re.IGNORECASE)
CAMBRIDGE_2020_RE = re.compile(
    r"Cambridge.{0,80}(?:Part[\s~–—-]*III)?.{0,80}\b2020\b",
    re.IGNORECASE | re.DOTALL,
)
LABEL_RE = re.compile(r"\\label\{([^{}]+)\}")
WORD_RE = re.compile(r"[A-Za-z0-9]+")
PLACEHOLDER_RE = re.compile(
    r"\b(?:TODO|TBD|FIXME|solution\s+goes\s+here|inserted\s+here)\b",
    re.IGNORECASE,
)
KET_BRA_INTERNAL_ASYMPTOTIC_RE = re.compile(
    r"\\(?:ket|bra)\{[^{}\n]*(?:"
    r"\\(?:mathrm|text|rm)\{(?:in|out)\}"
    r"|(?:^|[\s,;])(?:in|out)(?:$|[\s,;])"
    r")[^{}\n]*\}",
    re.IGNORECASE,
)
KET_BRA_ASYMPTOTIC_SUPERSCRIPT_RE = re.compile(
    r"\\(?:ket|bra)\{[^{}\n]*\}\s*\^\s*"
    r"(?:\{[^{}\n]*(?:in|out)[^{}\n]*\}|\\(?:mathrm|text)\{(?:in|out)\})",
    re.IGNORECASE,
)
BRA_ASYMPTOTIC_RIGHT_SUBSCRIPT_RE = re.compile(
    r"\\bra\{[^{}\n]*\}\s*_\s*"
    r"(?:\{[^{}\n]*(?:in|out)[^{}\n]*\}|\\(?:mathrm|text)\{(?:in|out)\})",
    re.IGNORECASE,
)
RAW_KET_ASYMPTOTIC_SUBSCRIPT_RE = re.compile(
    r"\\ket\{[^{}\n]*\}\s*_\s*"
    r"(?:\{\\(?:mathrm|text)\{(?:in|out)(?:/(?:in|out))?\}\}"
    r"|\\(?:mathrm|text)\{(?:in|out)(?:/(?:in|out))?\})",
    re.IGNORECASE,
)
RAW_BRA_ASYMPTOTIC_PREFIX_RE = re.compile(
    r"\{\}\s*_\s*\{\\(?:mathrm|text)\{(?:in|out)(?:/(?:in|out))?\}\}"
    r"\s*(?:\\!)?\s*\\bra",
    re.IGNORECASE,
)
MOMENTUM_MODE_E_RE = re.compile(
    r"E_\s*(?:"
    r"\{\s*\\mathbf(?:\s*\{\s*[A-Za-z]+\s*\}|\s+[A-Za-z]+(?:')?)\s*\}"
    r"|\{\s*[kpq](?:')?\s*\}|[kpq](?:')?(?![A-Za-z]))"
)
LITERAL_SUPPLEMENTARY_REFERENCE_RE = re.compile(
    r"\b(?P<kind>Exercise|Solution)\s+S\."
    r"(?P<chapter>\d+)\.(?P<number>\d+)\b"
)
LOCAL_SUPPLEMENTARY_REFERENCE_RE = re.compile(
    r"\bSupplementary\s+(?P<kind>Exercise|Solution)(?:\s|~)+"
    r"(?P<number>\d+)\b",
    re.IGNORECASE,
)
AMBIGUOUS_DEPENDENCY_RE = re.compile(
    r"\b(?:preceding|previous)\s+(?:two\s+)?"
    r"(?:exercise|solution)s?\b",
    re.IGNORECASE,
)


@dataclass(frozen=True)
class MacroCall:
    name: str
    args: tuple[str, ...]
    start: int
    end: int


@dataclass
class Audit:
    strict: bool
    failures: list[str]
    warnings: list[str]

    def require(self, condition: bool, message: str, *, incomplete: bool = False) -> None:
        if condition:
            return
        if incomplete and not self.strict:
            self.warnings.append(message)
        else:
            self.failures.append(message)

    def warn(self, message: str) -> None:
        self.warnings.append(message)


def strip_comments(text: str) -> str:
    """Remove unescaped TeX comments while preserving line boundaries."""

    output: list[str] = []
    for line in text.splitlines(keepends=True):
        cut = len(line)
        for index, char in enumerate(line):
            if char != "%":
                continue
            slashes = 0
            cursor = index - 1
            while cursor >= 0 and line[cursor] == "\\":
                slashes += 1
                cursor -= 1
            if slashes % 2 == 0:
                cut = index
                break
        kept = line[:cut]
        if line.endswith("\n") and not kept.endswith("\n"):
            kept += "\n"
        output.append(kept)
    return "".join(output)


def braced_argument(text: str, cursor: int) -> tuple[str, int]:
    while cursor < len(text) and text[cursor].isspace():
        cursor += 1
    if cursor >= len(text) or text[cursor] != "{":
        raise ValueError(f"Expected braced argument near character {cursor}")
    start = cursor + 1
    depth = 1
    cursor += 1
    while cursor < len(text):
        char = text[cursor]
        if char == "\\":
            cursor += 2
            continue
        if char == "{":
            depth += 1
        elif char == "}":
            depth -= 1
            if depth == 0:
                return text[start:cursor], cursor + 1
        cursor += 1
    raise ValueError(f"Unclosed braced argument beginning at character {start - 1}")


def macro_calls(text: str, name: str, argument_count: int) -> list[MacroCall]:
    """Return calls to a macro, parsing nested braced arguments."""

    clean = strip_comments(text)
    marker = "\\" + name
    calls: list[MacroCall] = []
    cursor = 0
    while True:
        start = clean.find(marker, cursor)
        if start < 0:
            return calls
        after_name = start + len(marker)
        if after_name < len(clean) and clean[after_name].isalpha():
            cursor = after_name
            continue
        args: list[str] = []
        end = after_name
        try:
            for _ in range(argument_count):
                arg, end = braced_argument(clean, end)
                args.append(arg)
        except ValueError:
            cursor = after_name
            continue
        calls.append(MacroCall(name, tuple(args), start, end))
        cursor = end


def macro_bodies(text: str, calls: list[MacroCall]) -> list[str]:
    clean = strip_comments(text)
    bodies: list[str] = []
    for index, call in enumerate(calls):
        end = calls[index + 1].start if index + 1 < len(calls) else len(clean)
        bodies.append(clean[call.end:end])
    return bodies


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def text_sha256(*parts: str) -> str:
    digest = hashlib.sha256()
    for part in parts:
        digest.update(part.encode("utf-8"))
        digest.update(b"\x00")
    return digest.hexdigest()


def continuous_numbers(values: Iterable[str], expected_count: int | None = None) -> bool:
    numbers: list[int] = []
    for value in values:
        try:
            numbers.append(int(value.strip()))
        except ValueError:
            return False
    desired_count = len(numbers) if expected_count is None else expected_count
    return numbers == list(range(1, desired_count + 1))


def normalized_title(text: str) -> str:
    return " ".join(WORD_RE.findall(text.lower()))


def normalized_problem(text: str) -> str:
    clean = strip_comments(text)
    clean = re.sub(
        r"\\(?:begin|end)\{(?:enumerate|itemize|description)\}",
        " ",
        clean,
    )
    return " ".join(WORD_RE.findall(clean.lower()))


def normalized_parent_problem(text: str) -> tuple[str, ...]:
    """Canonicalize a ledger parent, ignoring repeated constituent locators."""

    parts = {
        normalized_title(part)
        for part in text.split("|")
        if normalized_title(part)
    }
    return tuple(sorted(parts))


def exact_parent_roots(text: str) -> tuple[tuple[str, str], ...]:
    """Return source-question roots while deliberately discarding subpart labels."""

    roots = {
        (
            re.sub(r"\s+", " ", match.group("kind").lower()).replace(
                "examination question", "exam question"
            ),
            match.group("number").lower(),
        )
        for match in EXACT_PARENT_ROOT_RE.finditer(text)
    }
    return tuple(sorted(roots))


def source_ledger(root: Path, audit: Audit) -> dict[str, dict[str, object]]:
    path = root / "source-ledger.json"
    audit.require(path.exists(), f"Missing source ledger: {path}", incomplete=True)
    if not path.exists():
        return {}
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        audit.failures.append(f"Cannot parse {path}: {error}")
        return {}
    sources = payload.get("sources")
    audit.require(
        isinstance(sources, list),
        "source-ledger.json must contain a top-level sources array",
    )
    if not isinstance(sources, list):
        return {}

    required_fields = (
        "id",
        "source_family",
        "document_id",
        "parent_problem",
        "use_mode",
        "author_or_institution",
        "title",
        "year",
        "locator",
        "url",
        "chapters",
        "adaptation_notes",
    )
    by_id: dict[str, dict[str, object]] = {}
    parent_owners: dict[tuple[str, str], str] = {}
    exact_root_owners: dict[tuple[str, str, str], str] = {}
    for index, source in enumerate(sources, start=1):
        if not isinstance(source, dict):
            audit.failures.append(f"Ledger entry {index} is not an object")
            continue
        for field in required_fields:
            value = source.get(field)
            audit.require(
                value not in (None, "", []),
                f"Ledger entry {index} has empty field {field!r}",
                incomplete=True,
            )
        source_id = source.get("id")
        if not isinstance(source_id, str) or not source_id.strip():
            continue
        if source_id in by_id:
            audit.failures.append(f"Duplicate source ledger id: {source_id}")
            continue
        source_family = source.get("source_family")
        audit.require(
            source_family in SOURCE_FAMILIES,
            f"Ledger source {source_id}: source_family must be one of "
            + ", ".join(sorted(SOURCE_FAMILIES)),
        )
        document_id = source.get("document_id")
        parent_problem = source.get("parent_problem")
        if (
            isinstance(document_id, str)
            and document_id.strip()
            and isinstance(parent_problem, str)
            and parent_problem.strip()
        ):
            parent_key = (
                document_id.strip(),
                "\x1f".join(normalized_parent_problem(parent_problem)),
            )
            previous_owner = parent_owners.get(parent_key)
            audit.require(
                previous_owner is None,
                f"Ledger sources {previous_owner!r} and {source_id!r} describe "
                f"the same parent problem {parent_key!r}",
            )
            parent_owners[parent_key] = source_id
        use_mode = source.get("use_mode")
        audit.require(
            use_mode in USE_MODES,
            f"Ledger source {source_id}: use_mode must be one of "
            + ", ".join(sorted(USE_MODES)),
        )
        if use_mode == "verbatim-permitted":
            reproduction_basis = source.get("reproduction_basis")
            audit.require(
                isinstance(reproduction_basis, str)
                and bool(reproduction_basis.strip()),
                f"Ledger source {source_id}: verbatim-permitted use requires "
                "a concrete reproduction_basis",
            )
        if isinstance(use_mode, str) and use_mode in {
            "adapted",
            "verbatim-permitted",
        }:
            normalized_parents = (
                normalized_parent_problem(parent_problem)
                if isinstance(parent_problem, str)
                else ()
            )
            audit.require(
                isinstance(parent_problem, str)
                and bool(EXACT_PROBLEM_LOCATOR_RE.search(parent_problem)),
                f"Ledger source {source_id}: {use_mode} use must identify an "
                "exact source Problem, Question, or Exercise; use "
                "original-inspired for a general section or chapter",
            )
            audit.require(
                len(normalized_parents) == 1,
                f"Ledger source {source_id}: {use_mode} use combines multiple "
                "constituent parent locators; keep one source problem intact "
                "or classify a genuinely new synthesis as original-inspired",
            )
            if isinstance(document_id, str) and isinstance(parent_problem, str):
                for kind, number in exact_parent_roots(parent_problem):
                    root_key = (document_id.strip(), kind, number)
                    previous_owner = exact_root_owners.get(root_key)
                    audit.require(
                        previous_owner is None,
                        f"Ledger sources {previous_owner!r} and {source_id!r} split "
                        f"the same source parent {kind.title()} {number}; retain all "
                        "connected subparts under one supplementary number",
                    )
                    exact_root_owners[root_key] = source_id
        url = source.get("url")
        if isinstance(url, str):
            parsed = urlparse(url)
            audit.require(
                parsed.scheme in {"http", "https"} and bool(parsed.netloc),
                f"Ledger source {source_id}: URL is not an absolute HTTP(S) URL",
            )
        chapters = source.get("chapters")
        audit.require(
            isinstance(chapters, list)
            and all(isinstance(chapter, int) for chapter in chapters),
            f"Ledger source {source_id}: chapters must be an integer array",
        )
        searchable = json.dumps(source, ensure_ascii=False)
        audit.require(
            not PART_II_RE.search(searchable),
            f"Ledger source {source_id}: Cambridge Part II material is forbidden",
        )
        audit.require(
            not CAMBRIDGE_2020_RE.search(searchable),
            f"Ledger source {source_id}: Cambridge 2020 material is forbidden",
        )
        by_id[source_id] = source
    return by_id


def pending_fidelity_record(
    expected: dict[str, str],
    *,
    changed: bool = False,
) -> dict[str, object]:
    use_mode = expected["use_mode"]
    checklist = {
        check: (
            "not-applicable"
            if use_mode == "original-inspired"
            and check in {"source_parent_complete", "one_parent_one_number"}
            else "pending"
        )
        for check in FIDELITY_CHECKS
    }
    note = (
        "Prompt, solution, source classification, or locator changed after the "
        "previous review; repeat the side-by-side audit."
        if changed
        else ""
    )
    return {
        **expected,
        "status": "pending",
        "checked_at": "",
        "auditor": "",
        "checklist": checklist,
        "notes": note,
    }


def source_fidelity_audit(
    root: Path,
    ledger: dict[str, dict[str, object]],
    expected_records: list[dict[str, str]],
    audit: Audit,
    *,
    write_template: bool,
) -> dict[str, int]:
    """Require a current, content-addressed review for every S problem."""

    path = root / "source-fidelity-audit.json"
    payload: object = {}
    if path.is_file():
        try:
            payload = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as error:
            audit.failures.append(f"Cannot parse {path}: {error}")
            payload = {}

    raw_audits = payload.get("audits") if isinstance(payload, dict) else None
    existing: dict[str, dict[str, object]] = {}
    if isinstance(raw_audits, list):
        for index, record in enumerate(raw_audits, start=1):
            if not isinstance(record, dict):
                audit.failures.append(
                    f"Source-fidelity audit entry {index} is not an object"
                )
                continue
            source_id = record.get("source_id")
            if not isinstance(source_id, str) or not source_id:
                audit.failures.append(
                    f"Source-fidelity audit entry {index} has no source_id"
                )
                continue
            if source_id in existing:
                audit.failures.append(
                    f"Duplicate source-fidelity audit id: {source_id}"
                )
                continue
            existing[source_id] = record

    expected_by_id = {record["source_id"]: record for record in expected_records}
    if write_template:
        merged: list[dict[str, object]] = []
        for expected in expected_records:
            source_id = expected["source_id"]
            prior = existing.get(source_id)
            stable_fields = tuple(expected)
            unchanged = (
                isinstance(prior, dict)
                and all(prior.get(field) == expected[field] for field in stable_fields)
            )
            if unchanged:
                merged.append(prior)
            else:
                merged.append(
                    pending_fidelity_record(
                        expected,
                        changed=isinstance(prior, dict),
                    )
                )
        payload = {
            "schema_version": 1,
            "audits": merged,
        }
        path.write_text(
            json.dumps(payload, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
        existing = {
            str(record["source_id"]): record
            for record in merged
        }

    audit.require(
        path.is_file(),
        f"Missing source-fidelity audit: {path}",
        incomplete=True,
    )
    if not path.is_file():
        return {
            "expected": len(expected_records),
            "passed": 0,
            "pending": len(expected_records),
            "rejected": 0,
        }
    audit.require(
        isinstance(payload, dict) and payload.get("schema_version") == 1,
        "source-fidelity-audit.json must declare schema_version 1",
    )
    audit.require(
        isinstance(raw_audits, list) or write_template,
        "source-fidelity-audit.json must contain an audits array",
    )

    missing = sorted(set(expected_by_id) - set(existing))
    obsolete = sorted(set(existing) - set(expected_by_id))
    audit.require(
        not missing,
        "Source-fidelity audit is missing current supplementary records: "
        + ", ".join(missing),
        incomplete=True,
    )
    audit.require(
        not obsolete,
        "Source-fidelity audit contains obsolete supplementary records: "
        + ", ".join(obsolete),
        incomplete=True,
    )

    status_counter: Counter[str] = Counter()
    not_passed: list[str] = []
    for source_id, expected in expected_by_id.items():
        record = existing.get(source_id)
        if not isinstance(record, dict):
            status_counter["pending"] += 1
            continue
        for field, expected_value in expected.items():
            audit.require(
                record.get(field) == expected_value,
                f"Source-fidelity record {source_id}: stale or incorrect {field}",
                incomplete=True,
            )
        ledger_record = ledger.get(source_id, {})
        audit.require(
            record.get("source_url") == ledger_record.get("url"),
            f"Source-fidelity record {source_id}: source_url differs from ledger",
            incomplete=True,
        )
        audit.require(
            record.get("source_locator") == ledger_record.get("locator"),
            f"Source-fidelity record {source_id}: source_locator differs from ledger",
            incomplete=True,
        )
        status = record.get("status")
        audit.require(
            status in FIDELITY_AUDIT_STATUSES,
            f"Source-fidelity record {source_id}: invalid status {status!r}",
        )
        if isinstance(status, str):
            status_counter[status] += 1
        if status != "passed":
            not_passed.append(source_id)
        checked_at = record.get("checked_at")
        auditor = record.get("auditor")
        notes = record.get("notes")
        checklist = record.get("checklist")
        audit.require(
            status != "passed"
            or (
                isinstance(checked_at, str)
                and bool(ISO_DATE_RE.fullmatch(checked_at))
            ),
            f"Source-fidelity record {source_id}: passed review needs ISO checked_at",
        )
        audit.require(
            status != "passed"
            or (isinstance(auditor, str) and bool(auditor.strip())),
            f"Source-fidelity record {source_id}: passed review needs an auditor",
        )
        audit.require(
            status != "passed"
            or (isinstance(notes, str) and bool(notes.strip())),
            f"Source-fidelity record {source_id}: passed review needs substantive notes",
        )
        audit.require(
            isinstance(checklist, dict)
            and set(checklist) == set(FIDELITY_CHECKS),
            f"Source-fidelity record {source_id}: checklist keys are incomplete",
        )
        if not isinstance(checklist, dict):
            continue
        for check in FIDELITY_CHECKS:
            state = checklist.get(check)
            audit.require(
                state in FIDELITY_CHECK_STATES,
                f"Source-fidelity record {source_id}: invalid {check} state {state!r}",
            )
            audit.require(
                status != "passed" or state in {"pass", "not-applicable"},
                f"Source-fidelity record {source_id}: passed review leaves "
                f"{check} at {state!r}",
            )
        use_mode = expected["use_mode"]
        if status == "passed" and use_mode in {"adapted", "verbatim-permitted"}:
            for check in ("source_parent_complete", "one_parent_one_number"):
                audit.require(
                    checklist.get(check) == "pass",
                    f"Source-fidelity record {source_id}: {use_mode} use requires "
                    f"{check}=pass",
                )
        elif status == "passed" and use_mode == "original-inspired":
            for check in ("source_parent_complete", "one_parent_one_number"):
                audit.require(
                    checklist.get(check) == "not-applicable",
                    f"Source-fidelity record {source_id}: original-inspired use "
                    f"requires {check}=not-applicable",
                )

    audit.require(
        not not_passed,
        f"{len(not_passed)} source-fidelity records have not passed; "
        "inspect source-fidelity-audit.json for the pending or rejected entries",
        incomplete=True,
    )
    return {
        "expected": len(expected_records),
        "passed": status_counter["passed"],
        "pending": status_counter["pending"] + len(missing),
        "rejected": status_counter["rejected"],
    }


def audit_hook_style(root: Path, audit: Audit) -> None:
    style_path = root / "latex" / "exercise-edition.sty"
    audit.require(style_path.exists(), f"Missing {style_path}")
    if not style_path.exists():
        return
    style = strip_comments(style_path.read_text(encoding="utf-8"))
    positions: list[int] = []
    for item in REQUIRED_HOOK_INPUTS:
        audit.require(
            style.count(item) == 1,
            f"exercise-edition.sty must input {item} exactly once",
        )
        positions.append(style.find(item))
    if all(position >= 0 for position in positions):
        audit.require(
            positions == sorted(positions),
            "The four exercise fragments are not loaded in the required order",
        )
    audit.require(
        "These editorial solutions were added by Codex" in style,
        "The required editorial attribution note is missing",
    )
    for definition in REQUIRED_ASYMPTOTIC_HELPERS:
        audit.require(
            style.count(definition) == 1,
            "exercise-edition.sty must define the exact asymptotic-state "
            f"helper {definition}",
        )


def audit_canonical_isolation(
    root: Path,
    metadata: dict[str, object],
    audit: Audit,
) -> None:
    canonical_name = metadata.get("canonical_source")
    if not isinstance(canonical_name, str):
        audit.failures.append("Metadata has no canonical_source string")
        return
    canonical = root.parent / canonical_name
    audit.require(canonical.exists(), f"Canonical source tree is missing: {canonical}")
    manifest_path = root / "canonical-source-sha256.json"
    audit.require(
        manifest_path.exists(),
        f"Missing canonical hash manifest: {manifest_path}",
    )
    if not canonical.exists() or not manifest_path.exists():
        return
    try:
        expected = json.loads(manifest_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as error:
        audit.failures.append(f"Cannot parse canonical hash manifest: {error}")
        return
    audit.require(
        isinstance(expected, dict) and bool(expected),
        "Canonical hash manifest must be a nonempty object",
    )
    if not isinstance(expected, dict):
        return
    actual_files = {
        str(path.relative_to(canonical))
        for path in canonical.rglob("*")
        if path.is_file() and path.suffix not in BUILD_SUFFIXES
    }
    audit.require(
        set(expected) == actual_files,
        "Canonical hash manifest does not cover the exact canonical source file set",
    )
    for relative, expected_hash in expected.items():
        path = canonical / relative
        audit.require(path.is_file(), f"Canonical file disappeared: {path}")
        if path.is_file():
            audit.require(
                sha256(path) == expected_hash,
                f"Canonical source changed after edition copy: {path}",
            )
    canonical_tex = canonical / "latex"
    if canonical_tex.exists():
        hook_hits = []
        for path in canonical_tex.rglob("*.tex"):
            if r"\chapterexercisehook" in path.read_text(
                encoding="utf-8", errors="replace"
            ):
                hook_hits.append(path)
        audit.require(
            not hook_hits,
            "Canonical edition contains exercise hooks: "
            + ", ".join(str(path) for path in hook_hits),
        )
        audit.require(
            not (canonical_tex / "exercises").exists(),
            f"Canonical edition unexpectedly contains {canonical_tex / 'exercises'}",
        )


def audit_metadata_structure(
    root: Path,
    metadata: dict[str, object],
    chapters: list[object],
    audit: Audit,
) -> None:
    """Pin each edition to its authoritative, ordered chapter sequence."""

    edition_name = metadata.get("edition")
    audit.require(
        edition_name == root.name,
        f"Metadata edition must equal the edition directory name {root.name!r}",
    )
    known_range = KNOWN_CHAPTER_RANGES.get(root.name)
    audit.require(
        known_range is not None,
        f"Unsupported exercise-edition directory: {root.name}",
    )
    raw_range = metadata.get("chapter_range")
    valid_range = (
        isinstance(raw_range, list)
        and len(raw_range) == 2
        and all(
            isinstance(number, int) and not isinstance(number, bool)
            for number in raw_range
        )
        and raw_range[0] <= raw_range[1]
    )
    audit.require(
        valid_range,
        "Metadata chapter_range must be an ordered two-integer array",
    )
    if not valid_range or known_range is None:
        return
    declared_range = (raw_range[0], raw_range[1])
    audit.require(
        declared_range == known_range,
        f"Metadata chapter_range must be {list(known_range)} for {root.name}",
    )

    chapter_numbers: list[int] = []
    valid_chapters = True
    for raw_chapter in chapters:
        if not isinstance(raw_chapter, dict):
            valid_chapters = False
            continue
        number = raw_chapter.get("chapter")
        if not isinstance(number, int) or isinstance(number, bool):
            valid_chapters = False
            continue
        chapter_numbers.append(number)
    audit.require(
        valid_chapters,
        "Every metadata chapter entry must have an integer chapter number",
    )
    expected_numbers = list(range(known_range[0], known_range[1] + 1))
    audit.require(
        chapter_numbers == expected_numbers,
        "Metadata chapters must be the exact ordered unique sequence "
        f"{expected_numbers}",
    )


def audit_pagination_policy(
    root: Path,
    metadata: dict[str, object],
    chapters: list[object],
    audit: Audit,
) -> None:
    source_index = metadata.get("source_index")
    audit.require(
        isinstance(source_index, bool),
        "Metadata source_index must be a boolean",
    )
    page_offset = metadata.get("pdf_arabic_page_offset")
    audit.require(
        isinstance(page_offset, int)
        and not isinstance(page_offset, bool)
        and page_offset >= 0,
        "Metadata pdf_arabic_page_offset must be a nonnegative integer",
    )
    renderer = root / "render_index_pagination.py"
    build_script = root / "build_and_verify.sh"
    audit.require(
        renderer.is_file(),
        f"Missing pagination renderer: {renderer}",
    )
    if build_script.is_file():
        build_text = strip_comments(build_script.read_text(encoding="utf-8"))
        audit.require(
            'python3 "$edition_root/render_index_pagination.py"' in build_text,
            "Build script must regenerate INDEX_PAGINATION.md after LaTeX",
        )

    previous_end: int | None = None
    for raw_chapter in chapters:
        if not isinstance(raw_chapter, dict):
            audit.failures.append("Every metadata chapter entry must be an object")
            continue
        number = raw_chapter.get("chapter")
        source_pages = raw_chapter.get("source_printed_pages")
        if source_index:
            valid = (
                isinstance(source_pages, list)
                and len(source_pages) == 2
                and all(isinstance(page, int) for page in source_pages)
                and source_pages[0] <= source_pages[1]
            )
            audit.require(
                valid,
                f"Chapter {number}: source_printed_pages must be [start, end]",
            )
            if valid:
                start, end = source_pages
                if previous_end is not None:
                    audit.require(
                        start == previous_end + 1,
                        f"Chapter {number}: printed-source page span must follow "
                        f"page {previous_end} contiguously",
                    )
                previous_end = end
        else:
            audit.require(
                source_pages is None,
                f"Chapter {number}: source_printed_pages supplied although "
                "source_index is false",
            )

    if source_index:
        style_path = root / "latex" / "exercise-edition.sty"
        style = (
            strip_comments(style_path.read_text(encoding="utf-8"))
            if style_path.is_file()
            else ""
        )
        audit.require(
            style.count(r"\newcommand{\ExerciseIndexPaginationNote}") == 1,
            "Indexed editions must define ExerciseIndexPaginationNote exactly once",
        )
        note_calls = 0
        backmatter_root = root / "latex" / "backmatter"
        if backmatter_root.is_dir():
            for path in backmatter_root.rglob("*.tex"):
                note_calls += strip_comments(
                    path.read_text(encoding="utf-8")
                ).count(r"\ExerciseIndexPaginationNote")
        audit.require(
            note_calls == 2,
            "Indexed editions must show the pagination note once in each "
            "inherited index",
        )


def audit_weinberg_prompt_integrity(
    root: Path,
    chapters: list[object],
    audit: Audit,
) -> None:
    manifest_path = root / "weinberg-exercise-source-sha256.json"
    audit.require(
        manifest_path.exists(),
        f"Missing Weinberg exercise hash manifest: {manifest_path}",
    )
    if not manifest_path.exists():
        return
    try:
        expected = json.loads(manifest_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as error:
        audit.failures.append(f"Cannot parse Weinberg exercise hash manifest: {error}")
        return
    audit.require(
        isinstance(expected, dict) and bool(expected),
        "Weinberg exercise hash manifest must be a nonempty object",
    )
    if not isinstance(expected, dict):
        return
    required_keys = {
        (
            "latex/exercises/"
            f"chapter{int(chapter['chapter']):02d}/weinberg-exercises.tex"
        )
        for chapter in chapters
        if isinstance(chapter, dict)
        and isinstance(chapter.get("chapter"), int)
        and not isinstance(chapter.get("chapter"), bool)
    }
    audit.require(
        set(expected) == required_keys,
        "Weinberg exercise hash manifest must cover exactly one prompt fragment "
        "for every declared chapter",
    )
    for relative, expected_hash in expected.items():
        path = root / relative
        audit.require(path.is_file(), f"Extracted Weinberg exercise file is missing: {path}")
        if path.is_file():
            audit.require(
                sha256(path) == expected_hash,
                f"Weinberg exercise prompt fragment changed: {path}",
            )


def audit_labels(root: Path, audit: Audit) -> None:
    owners: dict[str, list[Path]] = {}
    for path in (root / "latex").rglob("*.tex"):
        text = strip_comments(path.read_text(encoding="utf-8", errors="replace"))
        for label in LABEL_RE.findall(text):
            owners.setdefault(label, []).append(path)
    duplicates = {
        label: paths
        for label, paths in owners.items()
        if len(paths) > 1
    }
    for label, paths in sorted(duplicates.items()):
        audit.failures.append(
            f"Duplicate literal label {label!r}: "
            + ", ".join(str(path.relative_to(root)) for path in paths)
        )


def audit_asymptotic_notation(root: Path, audit: Audit) -> None:
    """Enforce the outside-the-state in/out convention throughout the edition."""

    for path in (root / "latex").rglob("*.tex"):
        text = strip_comments(path.read_text(encoding="utf-8", errors="replace"))
        checks = (
            (
                KET_BRA_INTERNAL_ASYMPTOTIC_RE,
                "places an in/out label inside a ket or bra",
            ),
            (
                KET_BRA_ASYMPTOTIC_SUPERSCRIPT_RE,
                "uses an in/out superscript on a ket or bra",
            ),
            (
                BRA_ASYMPTOTIC_RIGHT_SUBSCRIPT_RE,
                "places a bra's in/out label on the right",
            ),
            (
                RAW_KET_ASYMPTOTIC_SUBSCRIPT_RE,
                "spells out a ket's in/out subscript instead of using an asymptotic-state helper",
            ),
            (
                RAW_BRA_ASYMPTOTIC_PREFIX_RE,
                "spells out a bra's in/out prefix instead of using an asymptotic-state helper",
            ),
        )
        for pattern, explanation in checks:
            match = pattern.search(text)
            audit.require(
                match is None,
                f"{path.relative_to(root)} {explanation}: "
                f"{match.group(0)!r}" if match else "",
            )


def audit_momentum_mode_notation(root: Path, audit: Audit) -> None:
    """Reserve omega for on-shell energies attached to individual momentum modes."""

    for path in (root / "latex").rglob("*.tex"):
        if path.relative_to(root) == Path("latex/frontmatter/notation.tex"):
            continue
        text = strip_comments(path.read_text(encoding="utf-8", errors="replace"))
        match = MOMENTUM_MODE_E_RE.search(text)
        audit.require(
            match is None,
            f"{path.relative_to(root)} uses {match.group(0)!r} for a momentum-mode "
            "energy; use \\omega_k with matching variable typography" if match else "",
        )


def exercise_similarity(
    records: list[tuple[int, str, str]],
    audit: Audit,
) -> None:
    exact: dict[str, list[tuple[int, str]]] = {}
    for chapter, number, title in records:
        exact.setdefault(normalized_title(title), []).append((chapter, number))
    for title, locations in exact.items():
        if title and len(locations) > 1:
            audit.failures.append(
                f"Duplicate supplementary title {title!r}: "
                + ", ".join(f"S.{chapter}.{number}" for chapter, number in locations)
            )

    for left_index, left in enumerate(records):
        left_normal = normalized_title(left[2])
        if len(left_normal) < 24:
            continue
        for right in records[left_index + 1 :]:
            right_normal = normalized_title(right[2])
            if len(right_normal) < 24:
                continue
            ratio = difflib.SequenceMatcher(None, left_normal, right_normal).ratio()
            if ratio >= 0.88:
                audit.warn(
                    "Suspiciously similar supplementary titles "
                    f"S.{left[0]}.{left[1]} and S.{right[0]}.{right[1]} "
                    f"(ratio {ratio:.2f})"
                )


def exercise_body_similarity(
    records: list[tuple[int, str, str, str]],
    audit: Audit,
) -> None:
    """Report duplicated prompts even when their titles have been changed."""

    normalized = [
        (chapter, number, title, normalized_problem(body))
        for chapter, number, title, body in records
    ]
    exact: dict[str, list[tuple[int, str, str]]] = {}
    for chapter, number, title, body in normalized:
        if len(body.split()) >= 18:
            exact.setdefault(body, []).append((chapter, number, title))
    for body, locations in exact.items():
        if len(locations) > 1:
            audit.failures.append(
                "Duplicate supplementary prompt body: "
                + ", ".join(
                    f"S.{chapter}.{number} ({title})"
                    for chapter, number, title in locations
                )
            )

    for left_index, left in enumerate(normalized):
        left_words = left[3].split()
        if len(left_words) < 24:
            continue
        for right in normalized[left_index + 1 :]:
            right_words = right[3].split()
            if len(right_words) < 24:
                continue
            length_ratio = min(len(left_words), len(right_words)) / max(
                len(left_words), len(right_words)
            )
            if length_ratio < 0.75:
                continue
            ratio = difflib.SequenceMatcher(None, left[3], right[3]).ratio()
            if ratio >= 0.90 and left[3] != right[3]:
                audit.warn(
                    "Suspiciously similar supplementary prompt bodies "
                    f"S.{left[0]}.{left[1]} ({left[2]}) and "
                    f"S.{right[0]}.{right[1]} ({right[2]}) "
                    f"(ratio {ratio:.2f})"
                )


def recorded_build_inputs(root: Path, audit: Audit) -> set[Path] | None:
    """Return resolved TeX recorder inputs for strict post-build verification."""

    recorder = root / "latex" / "master.fls"
    if not audit.strict or not recorder.is_file():
        return None
    latex_root = recorder.parent.resolve()
    inputs: set[Path] = set()
    for line in recorder.read_text(encoding="utf-8", errors="replace").splitlines():
        if not line.startswith("INPUT "):
            continue
        raw_path = line.removeprefix("INPUT ").strip()
        if not raw_path:
            continue
        path = Path(raw_path)
        if not path.is_absolute():
            path = latex_root / path
        inputs.add(path.resolve())
    return inputs


def audit_chapter(
    root: Path,
    chapter_info: dict[str, object],
    ledger: dict[str, dict[str, object]],
    audit: Audit,
    recorder_inputs: set[Path] | None,
) -> dict[str, object]:
    chapter = int(chapter_info["chapter"])
    chapter_id = f"{chapter:02d}"
    fragment_dir = root / "latex" / "exercises" / f"chapter{chapter_id}"
    fragment_paths = [fragment_dir / filename for filename in REQUIRED_FRAGMENT_FILES]
    for path, filename in zip(fragment_paths, REQUIRED_FRAGMENT_FILES):
        audit.require(
            path.is_file(),
            f"Chapter {chapter}: missing {filename}",
        )

    backmatter_value = chapter_info.get("backmatter")
    backmatter: Path | None = None
    if isinstance(backmatter_value, str) and backmatter_value:
        relative_backmatter = Path(backmatter_value)
        candidate = (root / relative_backmatter).resolve()
        try:
            candidate.relative_to(root)
            inside_root = not relative_backmatter.is_absolute()
        except ValueError:
            inside_root = False
        audit.require(
            inside_root,
            f"Chapter {chapter}: backmatter path must stay inside the edition root",
        )
        if inside_root:
            backmatter = candidate
    else:
        audit.failures.append(f"Chapter {chapter}: invalid backmatter path")

    audit.require(
        backmatter is not None and backmatter.is_file(),
        f"Chapter {chapter}: missing backmatter",
    )
    if recorder_inputs is not None:
        recorder_paths = fragment_paths + ([backmatter] if backmatter is not None else [])
        for path in recorder_paths:
            audit.require(
                path.resolve() in recorder_inputs,
                f"Chapter {chapter}: build recorder did not load "
                f"{path.relative_to(root)}",
            )
    if backmatter is not None and backmatter.is_file():
        backmatter_text = strip_comments(backmatter.read_text(encoding="utf-8"))
        hook = rf"\chapterexercisehook{{{chapter_id}}}"
        audit.require(
            backmatter_text.count(hook) == 1,
            f"Chapter {chapter}: expected exactly one {hook}",
        )
        reference_positions = [
            position
            for marker in (
                r"\chapterbackmatter{Bibliography}",
                r"\chapterbackmatter{References}",
            )
            if (position := backmatter_text.find(marker)) >= 0
        ]
        audit.require(
            bool(reference_positions),
            f"Chapter {chapter}: original Bibliography/References marker is missing",
        )
        if hook in backmatter_text and reference_positions:
            audit.require(
                backmatter_text.index(hook) < min(reference_positions),
                f"Chapter {chapter}: exercise hook must precede original references",
            )

    texts: dict[str, str] = {}
    for filename, heading in zip(REQUIRED_FRAGMENT_FILES, REQUIRED_HEADINGS):
        path = fragment_dir / filename
        if not path.is_file():
            texts[filename] = ""
            continue
        text = path.read_text(encoding="utf-8")
        texts[filename] = text
        audit.require(
            strip_comments(text).count(heading) == 1,
            f"Chapter {chapter}: {filename} must contain heading {heading}",
        )
        if filename.startswith("supplementary-"):
            match = AMBIGUOUS_DEPENDENCY_RE.search(strip_comments(text))
            audit.require(
                match is None,
                f"Chapter {chapter}: {filename} contains ambiguous dependency "
                f"{match.group(0)!r}; use 'preceding part,' restate the needed "
                "result, or cite an explicit supplementary number"
                if match
                else "",
            )

    w_exercises = macro_calls(
        texts.get("weinberg-exercises.tex", ""),
        "WeinbergExercise",
        1,
    )
    w_solutions = macro_calls(
        texts.get("weinberg-solutions.tex", ""),
        "WeinbergSolution",
        1,
    )
    s_exercises = macro_calls(
        texts.get("supplementary-exercises.tex", ""),
        "SupplementaryExercise",
        4,
    )
    s_solutions = macro_calls(
        texts.get("supplementary-solutions.tex", ""),
        "SupplementarySolution",
        2,
    )

    expected_w = int(chapter_info["weinberg_exercises"])
    audit.require(
        len(w_exercises) == expected_w,
        f"Chapter {chapter}: metadata expects {expected_w} Weinberg exercises, "
        f"found {len(w_exercises)}",
    )
    audit.require(
        continuous_numbers((call.args[0] for call in w_exercises), expected_w),
        f"Chapter {chapter}: Weinberg exercise numbering is not 1--{expected_w}",
    )
    audit.require(
        continuous_numbers((call.args[0] for call in w_solutions), expected_w),
        f"Chapter {chapter}: Weinberg solutions are incomplete or discontinuous "
        f"({len(w_solutions)}/{expected_w})",
        incomplete=True,
    )
    for call, body in zip(
        w_solutions,
        macro_bodies(texts.get("weinberg-solutions.tex", ""), w_solutions),
    ):
        number = call.args[0].strip()
        audit.require(
            len(WORD_RE.findall(body)) >= 35,
            f"Chapter {chapter} W.{number}: solution is too short to be worked",
            incomplete=True,
        )
        audit.require(
            not PLACEHOLDER_RE.search(body),
            f"Chapter {chapter} W.{number}: solution contains placeholder text",
        )

    s_count = len(s_exercises)
    audit.require(
        continuous_numbers((call.args[0] for call in s_exercises)),
        f"Chapter {chapter}: supplementary exercise numbering is not continuous",
    )
    audit.require(
        continuous_numbers((call.args[0] for call in s_solutions), s_count),
        f"Chapter {chapter}: supplementary solutions are incomplete or "
        f"discontinuous ({len(s_solutions)}/{s_count})",
        incomplete=True,
    )
    solution_titles = {
        call.args[0].strip(): normalized_title(call.args[1])
        for call in s_solutions
    }
    s_exercise_bodies = macro_bodies(
        texts.get("supplementary-exercises.tex", ""),
        s_exercises,
    )
    prompt_prefixes = Counter(
        " ".join(normalized_problem(body).split()[:12])
        for body in s_exercise_bodies
        if len(normalized_problem(body).split()) >= 12
    )
    for prefix, repetition_count in sorted(prompt_prefixes.items()):
        audit.require(
            repetition_count < 3,
            f"Chapter {chapter}: {repetition_count} supplementary prompts repeat "
            f"the same boilerplate opening ({prefix!r})",
            incomplete=True,
        )
    s_exercise_word_counts: list[int] = []
    for call, body in zip(s_exercises, s_exercise_bodies):
        number, title, credit, source_id = (arg.strip() for arg in call.args)
        audit.require(
            bool(title),
            f"Chapter {chapter} S.{number}: empty title",
            incomplete=True,
        )
        audit.require(
            bool(credit),
            f"Chapter {chapter} S.{number}: empty printed source credit",
            incomplete=True,
        )
        audit.require(
            not PART_II_RE.search(credit),
            f"Chapter {chapter} S.{number}: Cambridge Part II is forbidden",
        )
        audit.require(
            not CAMBRIDGE_2020_RE.search(credit),
            f"Chapter {chapter} S.{number}: Cambridge 2020 is forbidden",
        )
        audit.require(
            source_id in ledger,
            f"Chapter {chapter} S.{number}: unknown source id {source_id!r}",
            incomplete=True,
        )
        if source_id in ledger:
            source_record = ledger[source_id]
            chapters = source_record.get("chapters")
            audit.require(
                isinstance(chapters, list) and chapter in chapters,
                f"Chapter {chapter} S.{number}: ledger source {source_id!r} "
                "does not list this chapter",
            )
            use_mode = source_record.get("use_mode")
            credit_lower = credit.lower()
            if use_mode == "adapted":
                audit.require(
                    "adapted from" in credit_lower,
                    f"Chapter {chapter} S.{number}: an adapted problem's credit "
                    "must say 'Adapted from'",
                )
            elif use_mode == "original-inspired":
                audit.require(
                    "inspired by" in credit_lower,
                    f"Chapter {chapter} S.{number}: an independently written "
                    "counterpart's credit must say 'Inspired by'",
                )
            elif use_mode == "verbatim-permitted":
                audit.require(
                    "from" in credit_lower
                    and "adapted from" not in credit_lower
                    and "inspired by" not in credit_lower,
                    f"Chapter {chapter} S.{number}: a verbatim-permitted problem "
                    "must use a direct 'From' credit",
                )
        if number in solution_titles:
            audit.require(
                solution_titles[number] == normalized_title(title),
                f"Chapter {chapter} S.{number}: exercise and solution titles differ",
            )
        word_count = len(WORD_RE.findall(body))
        s_exercise_word_counts.append(word_count)
        audit.require(
            word_count >= 18,
            f"Chapter {chapter} S.{number}: exercise statement is too short",
            incomplete=True,
        )
        audit.require(
            not PLACEHOLDER_RE.search(body),
            f"Chapter {chapter} S.{number}: exercise contains placeholder text",
        )

    s_solution_word_counts: list[int] = []
    s_solution_bodies = macro_bodies(
        texts.get("supplementary-solutions.tex", ""),
        s_solutions,
    )
    for call, body in zip(
        s_solutions,
        s_solution_bodies,
    ):
        number = call.args[0].strip()
        word_count = len(WORD_RE.findall(body))
        s_solution_word_counts.append(word_count)
        audit.require(
            word_count >= 35,
            f"Chapter {chapter} S.{number}: solution is too short to be worked",
            incomplete=True,
        )
        audit.require(
            not PLACEHOLDER_RE.search(body),
            f"Chapter {chapter} S.{number}: solution contains placeholder text",
        )

    target = int(chapter_info.get("supplementary_target", 30))
    exception = chapter_info.get("count_exception")
    curation_note = chapter_info.get("curation_note")
    history_key = (root.name, chapter)
    expected_exception = ZERO_TARGET_HISTORY_EXCEPTIONS.get(history_key)
    if expected_exception is not None:
        audit.require(
            chapter_info.get("title") == "Historical Introduction",
            f"Chapter {chapter}: the zero-target exception must be Historical Introduction",
        )
        audit.require(
            target == 0,
            f"Chapter {chapter}: the pinned historical supplementary target must be 0",
        )
        audit.require(
            exception == expected_exception,
            f"Chapter {chapter}: historical count exception text is not authoritative",
        )
        expected_count = 0
    else:
        audit.require(
            target == 30,
            f"Chapter {chapter}: nonhistorical supplementary ceiling must be 30",
        )
        audit.require(
            exception in (None, ""),
            f"Chapter {chapter}: only the two pinned historical chapters may "
            "carry count exceptions",
        )
        audit.require(
            isinstance(curation_note, str)
            and len(WORD_RE.findall(curation_note)) >= 12,
            f"Chapter {chapter}: metadata needs a substantive curation_note "
            "explaining why the selected 10--30 parent problems form the "
            "natural complete set",
            incomplete=True,
        )
        audit.require(
            MIN_SUPPLEMENTARY_EXERCISES
            <= s_count
            <= MAX_SUPPLEMENTARY_EXERCISES,
            f"Chapter {chapter}: expected "
            f"{MIN_SUPPLEMENTARY_EXERCISES}--{MAX_SUPPLEMENTARY_EXERCISES} "
            f"complete supplementary exercises, found {s_count}",
            incomplete=True,
        )
        expected_count = s_count
    audit.require(
        len(s_solutions) == expected_count,
        f"Chapter {chapter}: expected {expected_count} matching supplementary "
        f"solutions, found {len(s_solutions)}",
        incomplete=True,
    )

    if s_count:
        median_prompt_words = float(statistics.median(s_exercise_word_counts))
        median_solution_words = (
            float(statistics.median(s_solution_word_counts))
            if s_solution_word_counts
            else 0.0
        )
        short_prompt_count = sum(
            word_count < 35 for word_count in s_exercise_word_counts
        )
        short_solution_count = sum(
            word_count < 70 for word_count in s_solution_word_counts
        )
        audit.require(
            median_prompt_words >= 55,
            f"Chapter {chapter}: median supplementary prompt is only "
            f"{median_prompt_words:g} words; the collection still appears "
            "fragmented",
            incomplete=True,
        )
        audit.require(
            short_prompt_count <= max(2, s_count // 4),
            f"Chapter {chapter}: {short_prompt_count}/{s_count} prompts are "
            "under 35 words; retain short checks as subparts unless they are "
            "independently worthwhile",
            incomplete=True,
        )
        audit.require(
            median_solution_words >= 100,
            f"Chapter {chapter}: median supplementary solution is only "
            f"{median_solution_words:g} words; solutions need fuller reasoning",
            incomplete=True,
        )
        audit.require(
            short_solution_count <= max(2, s_count // 4),
            f"Chapter {chapter}: {short_solution_count}/{s_count} solutions are "
            "under 70 words",
            incomplete=True,
        )
    else:
        median_prompt_words = 0.0
        median_solution_words = 0.0
        short_prompt_count = 0
        short_solution_count = 0

    source_ids = [
        call.args[3].strip() for call in s_exercises if call.args[3].strip()
    ]
    document_counter = Counter(
        str(ledger[source_id].get("document_id"))
        for source_id in source_ids
        if source_id in ledger
    )
    family_counter = Counter(
        str(ledger[source_id].get("source_family"))
        for source_id in source_ids
        if source_id in ledger
    )
    use_mode_counter = Counter(
        str(ledger[source_id].get("use_mode"))
        for source_id in source_ids
        if source_id in ledger
    )
    if s_count:
        audit.require(
            len(document_counter) >= 3,
            f"Chapter {chapter}: supplementary collection uses only "
            f"{len(document_counter)} distinct source documents",
            incomplete=True,
        )
        audit.require(
            max(document_counter.values()) <= max(1, int(0.70 * s_count)),
            f"Chapter {chapter}: one source document supplies more than 70% of "
            "supplementary exercises",
            incomplete=True,
        )
    return {
        "chapter": chapter,
        "title": chapter_info.get("title"),
        "weinberg_exercises": len(w_exercises),
        "weinberg_solutions": len(w_solutions),
        "supplementary_exercises": s_count,
        "supplementary_solutions": len(s_solutions),
        "supplementary_minimum": 0
        if expected_exception is not None
        else MIN_SUPPLEMENTARY_EXERCISES,
        "supplementary_maximum": 0
        if expected_exception is not None
        else MAX_SUPPLEMENTARY_EXERCISES,
        "supplementary_target": target,
        "count_exception": exception,
        "curation_note": curation_note,
        "source_distribution": dict(sorted(document_counter.items())),
        "source_family_distribution": dict(sorted(family_counter.items())),
        "use_mode_distribution": dict(sorted(use_mode_counter.items())),
        "exact_source_problem_exercises": (
            use_mode_counter["adapted"]
            + use_mode_counter["verbatim-permitted"]
        ),
        "preferred_source_exercises": sum(
            family_counter[family] for family in PREFERRED_SOURCE_FAMILIES
        ),
        "prompt_word_statistics": {
            "median": median_prompt_words,
            "under_35": short_prompt_count,
        },
        "solution_word_statistics": {
            "median": median_solution_words,
            "under_70": short_solution_count,
        },
        "_titles": [
            (chapter, call.args[0].strip(), call.args[1].strip())
            for call in s_exercises
        ],
        "_problems": [
            (
                chapter,
                call.args[0].strip(),
                call.args[1].strip(),
                body,
            )
            for call, body in zip(s_exercises, s_exercise_bodies)
        ],
        "_source_ids": [call.args[3].strip() for call in s_exercises],
        "_fidelity_records": [
            {
                "source_id": exercise_call.args[3].strip(),
                "supplementary_id": f"S.{chapter}.{exercise_call.args[0].strip()}",
                "use_mode": str(
                    ledger.get(exercise_call.args[3].strip(), {}).get(
                        "use_mode",
                        "",
                    )
                ),
                "source_url": str(
                    ledger.get(exercise_call.args[3].strip(), {}).get("url", "")
                ),
                "source_locator": str(
                    ledger.get(exercise_call.args[3].strip(), {}).get(
                        "locator",
                        "",
                    )
                ),
                "prompt_sha256": text_sha256(
                    *exercise_call.args,
                    exercise_body,
                ),
                "solution_sha256": (
                    text_sha256(
                        *s_solutions[index].args,
                        s_solution_bodies[index],
                    )
                    if index < len(s_solutions)
                    and index < len(s_solution_bodies)
                    else ""
                ),
            }
            for index, (exercise_call, exercise_body) in enumerate(
                zip(s_exercises, s_exercise_bodies)
            )
        ],
        "_literal_references": (
            [
                (
                    chapter,
                    match.group("kind"),
                    int(match.group("chapter")),
                    int(match.group("number")),
                )
                for text in texts.values()
                for match in LITERAL_SUPPLEMENTARY_REFERENCE_RE.finditer(
                    strip_comments(text)
                )
            ]
            + [
                (
                    chapter,
                    match.group("kind").title(),
                    chapter,
                    int(match.group("number")),
                )
                for text in texts.values()
                for match in LOCAL_SUPPLEMENTARY_REFERENCE_RE.finditer(
                    strip_comments(text)
                )
            ]
        ),
    }


def audit_exports(root: Path, metadata: dict[str, object], audit: Audit) -> None:
    canonical_name = metadata.get("canonical_source")
    edition_name = metadata.get("edition")
    audit.require(
        isinstance(edition_name, str) and edition_name.endswith("_exercises"),
        "Edition name must end in _exercises",
    )
    audit.require(
        edition_name == root.name,
        "Edition name must match its directory",
    )
    audit.require(
        edition_name != canonical_name,
        "Exercise edition and canonical source names must differ",
    )
    script = root / "build_and_verify.sh"
    if script.exists():
        text = strip_comments(script.read_text(encoding="utf-8"))
        if isinstance(canonical_name, str):
            canonical_exports = (
                f"{canonical_name}.pdf",
                canonical_name.replace("_", "-") + ".pdf",
            )
            for name in canonical_exports:
                audit.require(
                    name not in text,
                    f"Build script appears to target canonical export name {name}",
                )
    export_manifest = root / "canonical-export-sha256.json"
    audit.require(
        export_manifest.exists(),
        f"Missing canonical export hash manifest: {export_manifest}",
    )
    if export_manifest.exists():
        try:
            expected_exports = json.loads(
                export_manifest.read_text(encoding="utf-8")
            )
        except json.JSONDecodeError as error:
            audit.failures.append(f"Cannot parse canonical export manifest: {error}")
            expected_exports = {}
        expected_key = (
            f"../../{canonical_name.replace('_', '-')}.pdf"
            if isinstance(canonical_name, str)
            else None
        )
        audit.require(
            isinstance(expected_exports, dict)
            and bool(expected_exports)
            and expected_key is not None
            and set(expected_exports) == {expected_key},
            "Canonical export manifest must contain exactly the authoritative "
            "canonical PDF",
        )
        if not isinstance(expected_exports, dict):
            expected_exports = {}
        for relative, expected_hash in expected_exports.items():
            canonical_export = (root / relative).resolve()
            audit.require(
                canonical_export.is_file(),
                f"Canonical export is missing: {canonical_export}",
            )
            if canonical_export.is_file():
                audit.require(
                    sha256(canonical_export) == expected_hash,
                    f"Canonical export was changed or overwritten: {canonical_export}",
                )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parent,
        help="exercise-edition root (default: directory containing this script)",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="treat unfinished counts and missing solutions as failures",
    )
    parser.add_argument(
        "--inventory",
        type=Path,
        help="write the machine-readable chapter inventory to this path",
    )
    parser.add_argument(
        "--write-fidelity-template",
        action="store_true",
        help=(
            "create or refresh pending content-addressed source-fidelity "
            "records without marking any review as passed"
        ),
    )
    args = parser.parse_args()

    root = args.root.resolve()
    audit = Audit(args.strict, [], [])
    metadata_path = root / "exercise-edition.json"
    if not metadata_path.exists():
        print(f"Missing metadata: {metadata_path}", file=sys.stderr)
        return 1
    try:
        metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as error:
        print(f"Cannot parse {metadata_path}: {error}", file=sys.stderr)
        return 1

    chapters = metadata.get("chapters")
    if not isinstance(chapters, list):
        print("exercise-edition.json has no chapters array", file=sys.stderr)
        return 1

    audit_metadata_structure(root, metadata, chapters, audit)
    audit_hook_style(root, audit)
    audit_pagination_policy(root, metadata, chapters, audit)
    audit_canonical_isolation(root, metadata, audit)
    audit_weinberg_prompt_integrity(root, chapters, audit)
    audit_labels(root, audit)
    audit_asymptotic_notation(root, audit)
    audit_momentum_mode_notation(root, audit)
    ledger = source_ledger(root, audit)
    recorder_inputs = recorded_build_inputs(root, audit)
    inventory = [
        audit_chapter(root, chapter, ledger, audit, recorder_inputs)
        for chapter in chapters
        if isinstance(chapter, dict)
    ]
    audit_exports(root, metadata, audit)

    all_titles = [
        title_record
        for chapter in inventory
        for title_record in chapter.pop("_titles")
    ]
    all_source_ids = [
        source_id
        for chapter in inventory
        for source_id in chapter.pop("_source_ids")
    ]
    all_fidelity_records = [
        record
        for chapter in inventory
        for record in chapter.pop("_fidelity_records")
    ]
    all_literal_references = [
        reference
        for chapter in inventory
        for reference in chapter.pop("_literal_references")
    ]
    all_problems = [
        problem_record
        for chapter in inventory
        for problem_record in chapter.pop("_problems")
    ]
    available_supplementary_numbers = {
        (int(chapter["chapter"]), number)
        for chapter in inventory
        for number in range(1, int(chapter["supplementary_exercises"]) + 1)
    }
    for (
        owner_chapter,
        reference_kind,
        reference_chapter,
        reference_number,
    ) in all_literal_references:
        audit.require(
            (reference_chapter, reference_number)
            in available_supplementary_numbers,
            f"Chapter {owner_chapter}: literal {reference_kind} reference "
            f"S.{reference_chapter}.{reference_number} has no matching "
            "supplementary parent after consolidation",
        )
    source_use_counts = Counter(all_source_ids)
    for source_id, use_count in sorted(source_use_counts.items()):
        audit.require(
            use_count == 1,
            f"Provenance source id {source_id!r} is used by "
            f"{use_count} supplementary exercises; merge split parts into one "
            "coherent parent problem",
            incomplete=True,
        )
    fidelity_summary = source_fidelity_audit(
        root,
        ledger,
        all_fidelity_records,
        audit,
        write_template=args.write_fidelity_template,
    )
    exercise_similarity(all_titles, audit)
    exercise_body_similarity(all_problems, audit)
    unused_sources = sorted(set(ledger) - set(all_source_ids))
    for source_id in unused_sources:
        audit.require(
            False,
            f"Ledger source is currently unused: {source_id}",
            incomplete=True,
        )

    payload = {
        "edition": metadata.get("edition"),
        "strict": args.strict,
        "chapters": inventory,
        "totals": {
            "weinberg_exercises": sum(
                int(chapter["weinberg_exercises"]) for chapter in inventory
            ),
            "weinberg_solutions": sum(
                int(chapter["weinberg_solutions"]) for chapter in inventory
            ),
            "supplementary_exercises": sum(
                int(chapter["supplementary_exercises"]) for chapter in inventory
            ),
            "supplementary_solutions": sum(
                int(chapter["supplementary_solutions"]) for chapter in inventory
            ),
            "ledger_sources": len(ledger),
            "ledger_documents": len(
                {
                    str(source.get("document_id"))
                    for source in ledger.values()
                    if source.get("document_id")
                }
            ),
            "preferred_source_records": sum(
                source.get("source_family") in PREFERRED_SOURCE_FAMILIES
                for source in ledger.values()
            ),
            "exact_source_problem_records": sum(
                source.get("use_mode") in {"adapted", "verbatim-permitted"}
                for source in ledger.values()
            ),
            "original_inspired_records": sum(
                source.get("use_mode") == "original-inspired"
                for source in ledger.values()
            ),
            "fidelity_records_expected": fidelity_summary["expected"],
            "fidelity_records_passed": fidelity_summary["passed"],
            "fidelity_records_pending": fidelity_summary["pending"],
            "fidelity_records_rejected": fidelity_summary["rejected"],
        },
        "warnings": audit.warnings,
        "failures": audit.failures,
    }
    inventory_path = (
        args.inventory.resolve()
        if args.inventory
        else root / "exercise-inventory.json"
    )
    inventory_path.write_text(
        json.dumps(payload, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    for warning in audit.warnings:
        print(f"WARNING: {warning}", file=sys.stderr)
    if audit.failures:
        print("EXERCISE AUDIT FAILURES", file=sys.stderr)
        for failure in audit.failures:
            print(f"  - {failure}", file=sys.stderr)
        return 1

    totals = payload["totals"]
    mode = "strict" if args.strict else "draft"
    print(
        f"Exercise audit ({mode}) passed for {metadata.get('edition')}: "
        f"{totals['weinberg_exercises']} W exercises / "
        f"{totals['weinberg_solutions']} W solutions; "
        f"{totals['supplementary_exercises']} S exercises / "
        f"{totals['supplementary_solutions']} S solutions; "
        f"{totals['ledger_sources']} provenance records, including "
        f"{totals['exact_source_problem_records']} exact-source problem "
        f"records, across {totals['ledger_documents']} source documents."
    )
    print(f"Wrote inventory: {inventory_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
