#!/usr/bin/env python3
"""Audit the complete, source-bound GR exercise edition.

Draft mode keeps the provisional tree buildable while reporting unfinished
editorial work.  Strict mode is the release gate: it requires explicit stable
IDs, one complete inventoried source parent per exercise, one matching
solution, exact ledger reconciliation, and two current content-addressed
reviews for every selected problem.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from collections import Counter
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parent
EXERCISES = ROOT / "latex" / "exercises"
ADDITIONAL = EXERCISES / "additional"
CHAPTERS = ROOT / "latex" / "chapters"
MASTER = ROOT / "latex" / "master.tex"
EDITION = ROOT / "exercise-edition.json"
INVENTORY = ROOT / "exercise-source-inventory.json"
LEDGER = ROOT / "exercise-ledger.json"
FIDELITY = ROOT / "source-fidelity-audit.json"
REPORT = ROOT / "exercise-audit-report.json"

USE_MODES = {"adapted", "original-inspired", "verbatim-permitted"}
REVIEW_ROLES = {"source-fidelity", "solution-verification"}
CHECKLIST_KEYS = {
    "source_parent_complete",
    "setup_self_contained",
    "conventions_and_definitions",
    "supplied_formulas_data_figures_hints",
    "connected_subparts",
    "one_parent_one_number",
    "credit_and_locator",
    "chapter_fit_and_quality",
    "solution_covers_all_subparts",
    "solution_mathematics_checked",
    "notation_checked",
}
CHECK_STATES = {"pass", "not-applicable", "pending", "fail"}
ID_RE = re.compile(r"\AGR-(?P<chapter>\d{2})-(?P<number>\d{2})\Z")
ISO_DATE_RE = re.compile(r"\A\d{4}-\d{2}-\d{2}\Z")
PLACEHOLDER_RE = re.compile(
    r"\b(?:TODO|TBD|FIXME|solution goes here|inserted here|placeholder)\b",
    re.IGNORECASE,
)
WORD_RE = re.compile(r"[A-Za-z0-9]+")


@dataclass(frozen=True)
class EnvironmentCall:
    name: str
    args: tuple[str, ...]
    body: str
    path: Path
    line: int


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


def load_json(path: Path, audit: Audit, *, incomplete: bool = False) -> object | None:
    if not path.is_file():
        audit.require(False, f"Missing {path.name}", incomplete=incomplete)
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        audit.failures.append(f"Cannot parse {path.name}: {error}")
        return None


def strip_comments(text: str) -> str:
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
        raise ValueError(f"expected braced argument near character {cursor}")
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
    raise ValueError(f"unclosed braced argument at character {start - 1}")


def environment_calls(path: Path, name: str, argument_count: int) -> list[EnvironmentCall]:
    text = strip_comments(path.read_text(encoding="utf-8"))
    marker = rf"\begin{{{name}}}"
    end_marker = rf"\end{{{name}}}"
    calls: list[EnvironmentCall] = []
    cursor = 0
    while True:
        start = text.find(marker, cursor)
        if start < 0:
            return calls
        argument_cursor = start + len(marker)
        args: list[str] = []
        try:
            for _ in range(argument_count):
                value, argument_cursor = braced_argument(text, argument_cursor)
                args.append(value.strip())
        except ValueError as error:
            raise ValueError(f"{path.relative_to(ROOT)}: {error}") from error
        end = text.find(end_marker, argument_cursor)
        if end < 0:
            raise ValueError(
                f"{path.relative_to(ROOT)}: unclosed {name} environment"
            )
        calls.append(
            EnvironmentCall(
                name=name,
                args=tuple(args),
                body=text[argument_cursor:end].strip(),
                path=path,
                line=text.count("\n", 0, start) + 1,
            )
        )
        cursor = end + len(end_marker)


def sha256_text(text: str) -> str:
    return hashlib.sha256((text.strip() + "\n").encode("utf-8")).hexdigest()


def words(text: str) -> int:
    return len(WORD_RE.findall(text))


def chapter_files(chapter: int) -> list[Path]:
    return [
        EXERCISES / f"chapter{chapter}.tex",
        ADDITIONAL / f"chapter{chapter}-exercises.tex",
        ADDITIONAL / f"chapter{chapter}-solutions.tex",
    ]


def source_parent_map(payload: object, audit: Audit) -> dict[str, dict[str, object]]:
    result: dict[str, dict[str, object]] = {}
    if not isinstance(payload, dict) or payload.get("schema_version") != 1:
        audit.failures.append("exercise-source-inventory.json must use schema_version 1")
        return result
    documents = payload.get("documents")
    if not isinstance(documents, list):
        audit.failures.append("exercise-source-inventory.json has no documents array")
        return result
    for document in documents:
        if not isinstance(document, dict):
            continue
        for problem in document.get("problems", []):
            if not isinstance(problem, dict):
                continue
            parent_id = problem.get("source_parent_id")
            if not isinstance(parent_id, str):
                continue
            if parent_id in result:
                audit.failures.append(f"Duplicate inventory parent {parent_id}")
                continue
            combined = dict(problem)
            combined["_document"] = document
            result[parent_id] = combined
    return result


def ledger_entries(payload: object, audit: Audit) -> list[dict[str, object]]:
    if not isinstance(payload, dict) or payload.get("schema_version") != 1:
        audit.require(False, "exercise-ledger.json must use schema_version 1", incomplete=True)
        return []
    entries = payload.get("exercises")
    if not isinstance(entries, list):
        audit.require(False, "exercise-ledger.json has no exercises array", incomplete=True)
        return []
    return [entry for entry in entries if isinstance(entry, dict)]


def audit_fidelity(
    payload: object,
    expected: dict[str, dict[str, object]],
    prompts: dict[str, EnvironmentCall],
    solutions: dict[str, EnvironmentCall],
    audit: Audit,
) -> Counter[str]:
    statuses: Counter[str] = Counter()
    if not isinstance(payload, dict) or payload.get("schema_version") != 1:
        audit.require(
            False,
            "source-fidelity-audit.json must use schema_version 1",
            incomplete=True,
        )
        return statuses
    records = payload.get("audits")
    if not isinstance(records, list):
        audit.require(
            False,
            "source-fidelity-audit.json has no audits array",
            incomplete=True,
        )
        return statuses
    by_id: dict[str, dict[str, object]] = {}
    for index, record in enumerate(records, start=1):
        if not isinstance(record, dict) or not isinstance(record.get("exercise_id"), str):
            audit.failures.append(f"Fidelity record {index} has no exercise_id")
            continue
        exercise_id = record["exercise_id"]
        if exercise_id in by_id:
            audit.failures.append(f"Duplicate fidelity record {exercise_id}")
        by_id[exercise_id] = record
    audit.require(
        set(by_id) == set(expected),
        "Fidelity records must cover exactly the ledger exercise IDs",
        incomplete=True,
    )
    for exercise_id, entry in expected.items():
        record = by_id.get(exercise_id)
        if record is None:
            continue
        for field in ("source_parent_id", "use_mode"):
            audit.require(
                record.get(field) == entry.get(field),
                f"{exercise_id}: fidelity {field} differs from ledger",
                incomplete=True,
            )
        prompt = prompts.get(exercise_id)
        solution = solutions.get(exercise_id)
        expected_prompt_hash = sha256_text(prompt.body) if prompt else None
        expected_solution_hash = sha256_text(solution.body) if solution else None
        audit.require(
            record.get("prompt_sha256") == expected_prompt_hash,
            f"{exercise_id}: stale prompt review hash",
            incomplete=True,
        )
        audit.require(
            record.get("solution_sha256") == expected_solution_hash,
            f"{exercise_id}: stale solution review hash",
            incomplete=True,
        )
        status = record.get("status")
        statuses[str(status)] += 1
        audit.require(
            status == "passed",
            f"{exercise_id}: source-fidelity status is not passed",
            incomplete=True,
        )
        checklist = record.get("checklist")
        audit.require(
            isinstance(checklist, dict) and set(checklist) == CHECKLIST_KEYS,
            f"{exercise_id}: fidelity checklist keys are incomplete",
            incomplete=True,
        )
        if isinstance(checklist, dict):
            for key, state in checklist.items():
                audit.require(
                    state in CHECK_STATES,
                    f"{exercise_id}: invalid checklist state {key}={state!r}",
                    incomplete=True,
                )
                audit.require(
                    state not in {"pending", "fail"},
                    f"{exercise_id}: unresolved checklist item {key}",
                    incomplete=True,
                )
        reviews = record.get("reviews")
        roles: set[str] = set()
        reviewers: set[str] = set()
        if isinstance(reviews, list):
            for review in reviews:
                if not isinstance(review, dict):
                    continue
                role = review.get("role")
                reviewer = review.get("reviewer")
                if isinstance(role, str):
                    roles.add(role)
                if isinstance(reviewer, str) and reviewer.strip():
                    reviewers.add(reviewer.strip())
                audit.require(
                    review.get("status") == "passed",
                    f"{exercise_id}: review {role!r} is not passed",
                    incomplete=True,
                )
                audit.require(
                    isinstance(review.get("checked_at"), str)
                    and bool(ISO_DATE_RE.fullmatch(str(review.get("checked_at")))),
                    f"{exercise_id}: review {role!r} needs an ISO date",
                    incomplete=True,
                )
                audit.require(
                    isinstance(review.get("notes"), str)
                    and words(str(review.get("notes"))) >= 12,
                    f"{exercise_id}: review {role!r} needs substantive notes",
                    incomplete=True,
                )
        audit.require(
            roles == REVIEW_ROLES,
            f"{exercise_id}: needs source-fidelity and solution-verification reviews",
            incomplete=True,
        )
        audit.require(
            len(reviewers) == 2,
            f"{exercise_id}: the two review passes need distinct reviewer identities",
            incomplete=True,
        )
    obsolete = sorted(set(by_id) - set(expected))
    if obsolete:
        audit.failures.append(f"Obsolete fidelity records: {obsolete}")
    return statuses


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--strict", action="store_true")
    args = parser.parse_args()
    audit = Audit(strict=args.strict, failures=[], warnings=[])

    config = load_json(EDITION, audit)
    inventory_payload = load_json(INVENTORY, audit, incomplete=True)
    ledger_payload = load_json(LEDGER, audit, incomplete=True)
    fidelity_payload = load_json(FIDELITY, audit, incomplete=True)
    if not isinstance(config, dict) or not isinstance(config.get("chapters"), list):
        audit.failures.append("exercise-edition.json has no chapters array")
        config_chapters: dict[int, dict[str, object]] = {}
    else:
        config_chapters = {
            int(item["chapter"]): item
            for item in config["chapters"]
            if isinstance(item, dict) and isinstance(item.get("chapter"), int)
        }

    inventory = source_parent_map(inventory_payload, audit)
    ledger = ledger_entries(ledger_payload, audit)
    ledger_by_id: dict[str, dict[str, object]] = {}
    for index, entry in enumerate(ledger, start=1):
        exercise_id = entry.get("exercise_id")
        if not isinstance(exercise_id, str) or not exercise_id:
            audit.failures.append(f"Ledger entry {index} has no exercise_id")
            continue
        if exercise_id in ledger_by_id:
            audit.failures.append(f"Duplicate ledger exercise ID {exercise_id}")
        ledger_by_id[exercise_id] = entry

    master = MASTER.read_text(encoding="utf-8")
    chapter_one = (CHAPTERS / "chapter01.tex").read_text(encoding="utf-8")
    audit.require(
        r"\chapterexercises{1}" not in master and r"\chapterexercises{1}" not in chapter_one,
        "Chapter 1 must remain exercise-free",
    )

    prompt_by_id: dict[str, EnvironmentCall] = {}
    solution_by_id: dict[str, EnvironmentCall] = {}
    chapter_summaries: list[dict[str, object]] = []
    legacy_total = 0
    all_selected_parents: list[str] = []

    for chapter in range(2, 17):
        wrapper_path = CHAPTERS / f"chapter{chapter:02d}.tex"
        wrapper = wrapper_path.read_text(encoding="utf-8")
        hook = rf"\chapterexercises{{{chapter}}}"
        backmatter = rf"\input{{chapters/chapter{chapter:02d}/backmatter.tex}}"
        audit.require(wrapper.count(hook) == 1, f"Chapter {chapter}: needs one exercise hook")
        audit.require(
            wrapper.count(backmatter) == 1,
            f"Chapter {chapter}: needs one backmatter input",
        )
        if hook in wrapper and backmatter in wrapper:
            audit.require(
                wrapper.index(hook) < wrapper.index(backmatter),
                f"Chapter {chapter}: exercises must precede references",
            )

        paths = chapter_files(chapter)
        for path in paths:
            audit.require(path.is_file(), f"Chapter {chapter}: missing {path.name}")
        existing_paths = [path for path in paths if path.is_file()]
        chapter_prompts: list[EnvironmentCall] = []
        chapter_solutions: list[EnvironmentCall] = []
        legacy = 0
        for path in existing_paths:
            text = path.read_text(encoding="utf-8")
            legacy += len(re.findall(r"\\begin\{exercise\}", text))
            legacy += len(re.findall(r"\\begin\{solution\}", text))
            try:
                chapter_prompts.extend(environment_calls(path, "sourceexercise", 4))
                chapter_solutions.extend(environment_calls(path, "sourcesolution", 3))
            except ValueError as error:
                audit.failures.append(str(error))
        legacy_total += legacy
        audit.require(
            legacy == 0,
            f"Chapter {chapter}: {legacy} provisional positional environments remain",
            incomplete=True,
        )

        chapter_prompts.sort(key=lambda call: int(call.args[1]) if call.args[1].isdigit() else 999)
        chapter_solutions.sort(key=lambda call: int(call.args[1]) if call.args[1].isdigit() else 999)
        config_item = config_chapters.get(chapter, {})
        minimum = config_item.get("minimum", 10)
        maximum = config_item.get("maximum", 30)
        audit.require(
            isinstance(minimum, int) and isinstance(maximum, int),
            f"Chapter {chapter}: invalid configured bounds",
        )
        if isinstance(minimum, int) and isinstance(maximum, int):
            audit.require(
                minimum <= len(chapter_prompts) <= maximum,
                f"Chapter {chapter}: {len(chapter_prompts)} audited exercises; expected {minimum}--{maximum}",
                incomplete=True,
            )
        audit.require(
            len(chapter_prompts) == len(chapter_solutions),
            f"Chapter {chapter}: prompt/solution count mismatch",
            incomplete=True,
        )

        expected_numbers = list(range(1, len(chapter_prompts) + 1))
        prompt_numbers: list[int] = []
        solution_numbers: list[int] = []
        for call, kind, target, numbers in (
            *((call, "prompt", prompt_by_id, prompt_numbers) for call in chapter_prompts),
            *((call, "solution", solution_by_id, solution_numbers) for call in chapter_solutions),
        ):
            exercise_id = call.args[0]
            number_text = call.args[1]
            number = int(number_text) if number_text.isdigit() else -1
            numbers.append(number)
            match = ID_RE.fullmatch(exercise_id)
            audit.require(
                bool(match)
                and int(match.group("chapter")) == chapter
                and int(match.group("number")) == number,
                f"{call.path.relative_to(ROOT)}:{call.line}: ID/number mismatch {exercise_id!r}/{number_text!r}",
                incomplete=True,
            )
            if exercise_id in target:
                audit.failures.append(f"Duplicate {kind} ID {exercise_id}")
            target[exercise_id] = call
            audit.require(
                not PLACEHOLDER_RE.search(call.body),
                f"{exercise_id}: {kind} contains placeholder text",
                incomplete=True,
            )
            threshold = 45 if kind == "prompt" else 80
            audit.require(
                words(call.body) >= threshold,
                f"{exercise_id}: {kind} is too short for an independently usable complete parent ({words(call.body)} words)",
                incomplete=True,
            )
        audit.require(
            prompt_numbers == expected_numbers,
            f"Chapter {chapter}: prompt numbers are not exactly sequential",
            incomplete=True,
        )
        audit.require(
            solution_numbers == expected_numbers,
            f"Chapter {chapter}: solution numbers are not exactly sequential",
            incomplete=True,
        )
        for prompt in chapter_prompts:
            solution = solution_by_id.get(prompt.args[0])
            if solution:
                audit.require(
                    prompt.args[2] == solution.args[2],
                    f"{prompt.args[0]}: prompt/solution titles differ",
                    incomplete=True,
                )
        chapter_summaries.append(
            {
                "chapter": chapter,
                "prompts": len(chapter_prompts),
                "solutions": len(chapter_solutions),
                "legacy_environments": legacy,
                "prompt_words": sum(words(call.body) for call in chapter_prompts),
                "solution_words": sum(words(call.body) for call in chapter_solutions),
            }
        )

    audit.require(
        set(prompt_by_id) == set(solution_by_id),
        "Prompt and solution ID sets differ",
        incomplete=True,
    )
    audit.require(
        set(ledger_by_id) == set(prompt_by_id),
        "Exercise ledger must cover exactly the sourceexercise IDs",
        incomplete=True,
    )

    required_ledger_fields = {
        "exercise_id",
        "source_parent_id",
        "chapter",
        "number",
        "title",
        "source_credit",
        "use_mode",
        "departures",
        "prompt_file",
        "solution_file",
    }
    for exercise_id, entry in ledger_by_id.items():
        missing = required_ledger_fields - set(entry)
        audit.require(
            not missing,
            f"{exercise_id}: ledger fields missing {sorted(missing)}",
            incomplete=True,
        )
        prompt = prompt_by_id.get(exercise_id)
        solution = solution_by_id.get(exercise_id)
        parent_id = entry.get("source_parent_id")
        parent = inventory.get(str(parent_id))
        audit.require(parent is not None, f"{exercise_id}: unknown source parent {parent_id}", incomplete=True)
        if parent is not None:
            audit.require(
                parent.get("disposition") == "selected",
                f"{exercise_id}: source parent is not marked selected in inventory",
                incomplete=True,
            )
            audit.require(
                parent.get("recommended_chapter") == entry.get("chapter"),
                f"{exercise_id}: chapter differs from inventory recommendation",
                incomplete=True,
            )
        if isinstance(parent_id, str):
            all_selected_parents.append(parent_id)
        audit.require(
            entry.get("use_mode") in USE_MODES,
            f"{exercise_id}: invalid use_mode {entry.get('use_mode')!r}",
            incomplete=True,
        )
        audit.require(
            isinstance(entry.get("departures"), str) and words(str(entry.get("departures"))) >= 8,
            f"{exercise_id}: departures must be explicit and substantive",
            incomplete=True,
        )
        if prompt:
            audit.require(entry.get("number") == int(prompt.args[1]), f"{exercise_id}: ledger number differs", incomplete=True)
            audit.require(entry.get("title") == prompt.args[2], f"{exercise_id}: ledger title differs", incomplete=True)
            audit.require(entry.get("source_credit") == prompt.args[3], f"{exercise_id}: printed credit differs from ledger", incomplete=True)
            audit.require(entry.get("chapter") == int(exercise_id[3:5]), f"{exercise_id}: ledger chapter differs", incomplete=True)
            audit.require(
                entry.get("prompt_file") == prompt.path.relative_to(ROOT).as_posix(),
                f"{exercise_id}: ledger prompt_file differs",
                incomplete=True,
            )
        if solution:
            audit.require(
                entry.get("solution_file") == solution.path.relative_to(ROOT).as_posix(),
                f"{exercise_id}: ledger solution_file differs",
                incomplete=True,
            )

    duplicates = [parent for parent, count in Counter(all_selected_parents).items() if count > 1]
    audit.require(
        not duplicates,
        f"A complete source parent may receive only one exercise number: {duplicates}",
        incomplete=True,
    )

    fidelity_statuses = audit_fidelity(
        fidelity_payload,
        ledger_by_id,
        prompt_by_id,
        solution_by_id,
        audit,
    )

    report = {
        "schema_version": 1,
        "strict": args.strict,
        "summary": {
            "audited_exercises": len(prompt_by_id),
            "audited_solutions": len(solution_by_id),
            "ledger_entries": len(ledger_by_id),
            "unique_selected_source_parents": len(set(all_selected_parents)),
            "legacy_environments": legacy_total,
            "fidelity_statuses": dict(sorted(fidelity_statuses.items())),
            "warnings": len(audit.warnings),
            "failures": len(audit.failures),
        },
        "chapters": chapter_summaries,
        "warnings": audit.warnings,
        "failures": audit.failures,
    }
    REPORT.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")

    if audit.warnings:
        print("EXERCISE AUDIT DRAFT WARNINGS")
        for warning in audit.warnings:
            print(f"  - {warning}")
    if audit.failures:
        print("EXERCISE AUDIT FAILURES", file=sys.stderr)
        for failure in audit.failures:
            print(f"  - {failure}", file=sys.stderr)
        return 1
    print(
        "Exercise audit: "
        f"{len(prompt_by_id)} source-bound exercises, {len(solution_by_id)} solutions, "
        f"{len(set(all_selected_parents))} unique complete parents; "
        f"strict={args.strict}."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
