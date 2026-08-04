#!/usr/bin/env python3
"""Capture and validate the one-time disposition ledger for the old 300 items.

``--write`` is intentionally one-shot: it snapshots the provisional TeX,
records content hashes, and refuses to overwrite the resulting evidence.
Normal operation validates the immutable JSON and rendered Markdown after the
provisional TeX has been replaced by the audited edition.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent
EXERCISES = ROOT / "latex" / "exercises"
CORPUS = ROOT / "source-corpus.json"
OUTPUT = ROOT / "provisional-exercise-dispositions.json"
MARKDOWN = ROOT / "PROVISIONAL_EXERCISE_DISPOSITIONS.md"
COMPARISONS = ROOT / "provisional-exact-parent-comparisons.json"
COMPARISON_MARKDOWN = ROOT / "PROVISIONAL_EXACT_PARENT_COMPARISONS.md"
WORD_RE = re.compile(r"[A-Za-z0-9]+")
PROMPT_RE = re.compile(
    r"\\begin\{exercise\}(?:\[([^]]*)\])?\{([^{}\n]+)\}(.*?)"
    r"\\end\{exercise\}",
    re.DOTALL,
)
SOLUTION_RE = re.compile(
    r"\\begin\{solution\}(?:\[([^]]*)\])?(.*?)\\end\{solution\}",
    re.DOTALL,
)
EXACT_CAMBRIDGE_RE = re.compile(
    r"Cambridge Part III, (?P<year>20\d{2}) exam, Question (?P<question>\d+)\Z"
)


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_text(text: str) -> str:
    return sha256_bytes((text.strip() + "\n").encode("utf-8"))


def words(text: str) -> int:
    return len(WORD_RE.findall(text))


def legacy_files(chapter: int) -> tuple[Path, Path, Path]:
    return (
        EXERCISES / f"chapter{chapter}.tex",
        EXERCISES / "additional" / f"chapter{chapter}-exercises.tex",
        EXERCISES / "additional" / f"chapter{chapter}-solutions.tex",
    )


def cambridge_candidate(year: int, question: int) -> str | None:
    corpus = json.loads(CORPUS.read_text(encoding="utf-8"))
    matches = [
        document
        for document in corpus["documents"]
        if document.get("source_family") == "cambridge-part-iii"
        and document.get("course") == "General Relativity"
        and document.get("kind") == "examination"
        and document.get("year") == year
    ]
    if len(matches) != 1:
        return None
    return f"{matches[0]['document_id']}-q{question}"


def locator_assessment(credit: str) -> tuple[str, str | None, str, str]:
    exact = EXACT_CAMBRIDGE_RE.fullmatch(credit)
    if exact:
        candidate = cambridge_candidate(
            int(exact.group("year")), int(exact.group("question"))
        )
        return (
            "document-and-question",
            candidate,
            "rebuild",
            "The credit identifies an examination parent, but the provisional prompt is a short extraction and its abbreviated solution has no recorded side-by-side completeness or convention review. Rebuild only from the inventoried complete parent.",
        )
    if re.search(r"Problem Set \d+\Z", credit):
        level = "document-only-no-problem"
    elif re.search(r"Sheet \d+\Z", credit):
        level = "sheet-only-no-problem"
    elif re.search(r"20\d{2} exam\Z", credit):
        level = "exam-only-no-question"
    elif "examples" in credit.lower():
        level = "generic-examples-no-document-or-problem"
    else:
        level = "outside-or-unresolved-source"
    return (
        level,
        None,
        "reject",
        "The printed credit does not resolve to one exact complete parent problem in the inspected corpus. The short provisional prompt and solution therefore cannot establish source completeness, connected-subpart coverage, or fidelity, and are rejected rather than silently retained.",
    )


def capture() -> dict[str, object]:
    captured_files: list[dict[str, object]] = []
    entries: list[dict[str, object]] = []
    for chapter in range(2, 17):
        main, extra_prompts, extra_solutions = legacy_files(chapter)
        for path in (main, extra_prompts, extra_solutions):
            data = path.read_bytes()
            captured_files.append(
                {
                    "path": path.relative_to(ROOT).as_posix(),
                    "bytes": len(data),
                    "sha256": sha256_bytes(data),
                }
            )
        main_text = main.read_text(encoding="utf-8")
        prompt_calls = PROMPT_RE.findall(main_text) + PROMPT_RE.findall(
            extra_prompts.read_text(encoding="utf-8")
        )
        solution_calls = SOLUTION_RE.findall(main_text) + SOLUTION_RE.findall(
            extra_solutions.read_text(encoding="utf-8")
        )
        if len(prompt_calls) != 20 or len(solution_calls) != 20:
            raise ValueError(
                f"Chapter {chapter}: expected 20 provisional prompts and solutions, "
                f"found {len(prompt_calls)} and {len(solution_calls)}"
            )
        for number, ((title, credit, prompt), (_, solution)) in enumerate(
            zip(prompt_calls, solution_calls), start=1
        ):
            locator, candidate, decision, rationale = locator_assessment(credit.strip())
            entries.append(
                {
                    "provisional_id": f"P.{chapter}.{number}",
                    "chapter": chapter,
                    "number": number,
                    "title": title.strip(),
                    "printed_credit": credit.strip(),
                    "prompt_sha256": sha256_text(prompt),
                    "solution_sha256": sha256_text(solution),
                    "prompt_words": words(prompt),
                    "solution_words": words(solution),
                    "locator_assessment": locator,
                    "candidate_source_parent_id": candidate,
                    "decision": decision,
                    "decision_rationale": rationale,
                }
            )
    tree_digest = hashlib.sha256()
    for item in captured_files:
        tree_digest.update(str(item["path"]).encode("utf-8") + b"\0")
        tree_digest.update(str(item["sha256"]).encode("ascii") + b"\n")
    decisions: dict[str, int] = {}
    for entry in entries:
        value = str(entry["decision"])
        decisions[value] = decisions.get(value, 0) + 1
    return {
        "schema_version": 1,
        "captured_at": "2026-08-03",
        "policy": (
            "Every one of the 300 inherited items is provisional. Only a credit "
            "that resolves to a unique source document and parent question earns "
            "a rebuild candidate; nothing is kept without a fresh complete-parent "
            "comparison, full solution, notation pass, and content-addressed review."
        ),
        "captured_source_tree_sha256": tree_digest.hexdigest(),
        "captured_files": captured_files,
        "summary": {
            "provisional_exercises": len(entries),
            "decisions": decisions,
        },
        "exercises": entries,
    }


def validate(payload: object) -> list[str]:
    failures: list[str] = []
    if not isinstance(payload, dict) or payload.get("schema_version") != 1:
        return ["Ledger must be an object with schema_version 1"]
    files = payload.get("captured_files")
    entries = payload.get("exercises")
    if not isinstance(files, list) or len(files) != 45:
        failures.append("Ledger must record the 45 provisional TeX source files")
    if not isinstance(entries, list) or len(entries) != 300:
        failures.append("Ledger must record exactly 300 provisional exercises")
        return failures
    expected = [f"P.{chapter}.{number}" for chapter in range(2, 17) for number in range(1, 21)]
    actual = [entry.get("provisional_id") for entry in entries if isinstance(entry, dict)]
    if actual != expected:
        failures.append("Provisional IDs must be exactly P.2.1 through P.16.20")
    for entry in entries:
        if not isinstance(entry, dict):
            failures.append("Non-object provisional entry")
            continue
        provisional_id = entry.get("provisional_id")
        if entry.get("decision") not in {"rebuild", "reject"}:
            failures.append(f"{provisional_id}: invalid decision")
        if not isinstance(entry.get("decision_rationale"), str) or words(
            str(entry.get("decision_rationale"))
        ) < 20:
            failures.append(f"{provisional_id}: rationale is not substantive")
        for field in ("prompt_sha256", "solution_sha256"):
            value = entry.get(field)
            if not isinstance(value, str) or not re.fullmatch(r"[0-9a-f]{64}", value):
                failures.append(f"{provisional_id}: invalid {field}")
        if entry.get("decision") == "rebuild" and not entry.get(
            "candidate_source_parent_id"
        ):
            failures.append(f"{provisional_id}: rebuild lacks a candidate parent")
    summary = payload.get("summary")
    counts: dict[str, int] = {}
    for entry in entries:
        if isinstance(entry, dict):
            decision = str(entry.get("decision"))
            counts[decision] = counts.get(decision, 0) + 1
    if not isinstance(summary, dict) or summary.get("decisions") != counts:
        failures.append("Summary decision counts are stale")
    return failures


def render(payload: dict[str, object]) -> str:
    summary = payload["summary"]
    lines = [
        "# Provisional Exercise Dispositions",
        "",
        str(payload["policy"]),
        "",
        f"Captured source-tree SHA-256: `{payload['captured_source_tree_sha256']}`.",
        "",
        f"Total: **{summary['provisional_exercises']}**; decisions: "
        + ", ".join(f"**{key} {value}**" for key, value in sorted(summary["decisions"].items()))
        + ".",
        "",
        "| ID | Title | Printed credit | Locator assessment | Decision | Candidate parent | Rationale |",
        "|---|---|---|---|---|---|---|",
    ]
    for entry in payload["exercises"]:
        escape = lambda value: str(value).replace("|", "\\|").replace("\n", " ")
        lines.append(
            "| "
            + " | ".join(
                [
                    escape(entry["provisional_id"]),
                    escape(entry["title"]),
                    escape(entry["printed_credit"]),
                    escape(entry["locator_assessment"]),
                    escape(entry["decision"]),
                    escape(entry["candidate_source_parent_id"] or "—"),
                    escape(entry["decision_rationale"]),
                ]
            )
            + " |"
        )
    return "\n".join(lines) + "\n"


def validate_comparisons(
    payload: object, provisional: dict[str, object]
) -> list[str]:
    failures: list[str] = []
    if not isinstance(payload, dict) or payload.get("schema_version") != 1:
        return ["Exact-parent comparison ledger must use schema_version 1"]
    if not isinstance(payload.get("reviewer"), str) or not payload["reviewer"].strip():
        failures.append("Exact-parent comparison ledger needs a reviewer")
    if not isinstance(payload.get("method"), str) or words(str(payload.get("method"))) < 15:
        failures.append("Exact-parent comparison method is not substantive")
    if not isinstance(payload.get("checked_at"), str) or not re.fullmatch(
        r"\d{4}-\d{2}-\d{2}", str(payload.get("checked_at"))
    ):
        failures.append("Exact-parent comparison ledger needs an ISO date")
    entries = payload.get("comparisons")
    if not isinstance(entries, list):
        return failures + ["Exact-parent comparison ledger has no comparisons array"]
    rebuilds = {
        str(entry["provisional_id"]): entry
        for entry in provisional["exercises"]
        if entry["decision"] == "rebuild"
    }
    by_id = {
        str(entry.get("provisional_id")): entry
        for entry in entries
        if isinstance(entry, dict)
    }
    if set(by_id) != set(rebuilds):
        failures.append("Exact-parent comparisons must cover exactly the 12 rebuild items")
    for provisional_id, baseline in rebuilds.items():
        comparison = by_id.get(provisional_id)
        if comparison is None:
            continue
        if comparison.get("source_parent_id") != baseline.get(
            "candidate_source_parent_id"
        ):
            failures.append(f"{provisional_id}: compared parent differs from candidate")
        if comparison.get("decision") != "rebuild":
            failures.append(f"{provisional_id}: exact comparison decision must be rebuild")
        for field in ("retained_components", "missing_or_changed_components"):
            values = comparison.get(field)
            if (
                not isinstance(values, list)
                or len(values) < 2
                or any(not isinstance(value, str) or words(value) < 4 for value in values)
            ):
                failures.append(f"{provisional_id}: {field} is incomplete")
        for field in ("prompt_assessment", "solution_assessment"):
            if not isinstance(comparison.get(field), str) or words(
                str(comparison.get(field))
            ) < 20:
                failures.append(f"{provisional_id}: {field} is not substantive")
        if not isinstance(comparison.get("pdf_pages"), str) or not comparison[
            "pdf_pages"
        ].strip():
            failures.append(f"{provisional_id}: exact comparison needs PDF pages")
    return failures


def render_comparisons(payload: dict[str, object]) -> str:
    lines = [
        "# Exact-parent comparisons for provisional rebuild candidates",
        "",
        str(payload["method"]),
        "",
        f"Reviewer: **{payload['reviewer']}**; checked: **{payload['checked_at']}**.",
        "",
    ]
    for item in payload["comparisons"]:
        lines.extend(
            [
                f"## {item['provisional_id']} — `{item['source_parent_id']}`",
                "",
                f"Source PDF page(s): {item['pdf_pages']}.",
                "",
                "Retained components:",
                "",
                *[f"- {value}" for value in item["retained_components"]],
                "",
                "Missing or materially changed components:",
                "",
                *[f"- {value}" for value in item["missing_or_changed_components"]],
                "",
                f"Prompt assessment: {item['prompt_assessment']}",
                "",
                f"Solution assessment: {item['solution_assessment']}",
                "",
                f"Decision: **{item['decision']}**.",
                "",
            ]
        )
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    parser.add_argument(
        "--render-comparisons",
        action="store_true",
        help="render the validated exact-parent comparison ledger",
    )
    args = parser.parse_args()
    if args.write and args.render_comparisons:
        parser.error("choose only one write operation")
    if args.render_comparisons:
        try:
            provisional = json.loads(OUTPUT.read_text(encoding="utf-8"))
            comparisons = json.loads(COMPARISONS.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as error:
            print(f"Cannot render exact-parent comparisons: {error}", file=sys.stderr)
            return 1
        failures = validate(provisional) + validate_comparisons(
            comparisons, provisional
        )
        if failures:
            for failure in failures:
                print(f"PROVISIONAL COMPARISON FAILURE: {failure}", file=sys.stderr)
            return 1
        COMPARISON_MARKDOWN.write_text(
            render_comparisons(comparisons), encoding="utf-8"
        )
        print(f"Rendered {len(comparisons['comparisons'])} exact-parent comparisons.")
        return 0
    if args.write:
        if OUTPUT.exists():
            print(f"Refusing to overwrite immutable snapshot: {OUTPUT}", file=sys.stderr)
            return 1
        try:
            payload = capture()
        except (OSError, ValueError, json.JSONDecodeError) as error:
            print(f"Cannot capture provisional collection: {error}", file=sys.stderr)
            return 1
        OUTPUT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
        MARKDOWN.write_text(render(payload), encoding="utf-8")
        print(f"Captured {len(payload['exercises'])} provisional dispositions.")
        return 0
    try:
        payload = json.loads(OUTPUT.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        print(f"Cannot read provisional disposition ledger: {error}", file=sys.stderr)
        return 1
    failures = validate(payload)
    expected_markdown = render(payload)
    if not MARKDOWN.is_file() or MARKDOWN.read_text(encoding="utf-8") != expected_markdown:
        failures.append("PROVISIONAL_EXERCISE_DISPOSITIONS.md is missing or stale")
    try:
        comparisons = json.loads(COMPARISONS.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        failures.append(f"Cannot read exact-parent comparison ledger: {error}")
        comparisons = None
    if comparisons is not None:
        failures.extend(validate_comparisons(comparisons, payload))
        expected_comparison_markdown = render_comparisons(comparisons)
        if (
            not COMPARISON_MARKDOWN.is_file()
            or COMPARISON_MARKDOWN.read_text(encoding="utf-8")
            != expected_comparison_markdown
        ):
            failures.append("PROVISIONAL_EXACT_PARENT_COMPARISONS.md is missing or stale")
    if failures:
        for failure in failures:
            print(f"PROVISIONAL DISPOSITION FAILURE: {failure}", file=sys.stderr)
        return 1
    print(
        f"Provisional disposition ledger: {len(payload['exercises'])} inherited items, "
        f"{payload['summary']['decisions']}."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
