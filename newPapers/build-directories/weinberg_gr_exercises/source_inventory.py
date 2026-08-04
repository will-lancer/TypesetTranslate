#!/usr/bin/env python3
"""Merge and validate the problem-level supplementary-source inventory."""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parent
CORPUS = ROOT / "source-corpus.json"
FRAGMENTS = ROOT / "source-inventory-fragments"
OUTPUT = ROOT / "exercise-source-inventory.json"

DISPOSITIONS = {
    "selected",
    "reserved_for_chapter",
    "duplicate",
    "unsuitable_for_weinberg",
    "too_dependent",
    "outside_scope",
}
REQUIRED_DOCUMENT_FIELDS = {
    "document_id",
    "source_family",
    "institution",
    "course",
    "year",
    "kind",
    "stable_url",
    "local_pdf",
    "local_text",
    "source_sha256",
    "pdf_pages",
    "problems",
}
REQUIRED_PROBLEM_FIELDS = {
    "source_parent_id",
    "question_number",
    "parent_scope",
    "printed_pages",
    "pdf_pages",
    "short_topic",
    "disposition",
    "recommended_chapter",
    "duplicate_of",
    "disposition_rationale",
}
WORD_RE = re.compile(r"[A-Za-z0-9]+")


def load_json(path: Path) -> object:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise ValueError(f"Cannot parse {path}: {error}") from error


def corpus_documents() -> dict[str, dict[str, object]]:
    payload = load_json(CORPUS)
    if not isinstance(payload, dict) or payload.get("schema_version") != 1:
        raise ValueError("source-corpus.json must use schema_version 1")
    documents = payload.get("documents")
    if not isinstance(documents, list):
        raise ValueError("source-corpus.json has no documents array")
    result: dict[str, dict[str, object]] = {}
    for document in documents:
        if not isinstance(document, dict) or not isinstance(
            document.get("document_id"), str
        ):
            raise ValueError("Invalid document in source-corpus.json")
        document_id = document["document_id"]
        if document_id in result:
            raise ValueError(f"Duplicate corpus document id: {document_id}")
        result[document_id] = document
    return result


def fragment_documents() -> tuple[list[dict[str, object]], list[str]]:
    documents: list[dict[str, object]] = []
    scopes: list[str] = []
    for path in sorted(FRAGMENTS.glob("*.json")):
        payload = load_json(path)
        if not isinstance(payload, dict) or payload.get("schema_version") != 1:
            raise ValueError(f"{path} must use schema_version 1")
        scope = payload.get("scope")
        if not isinstance(scope, str) or not scope.strip():
            raise ValueError(f"{path} has no scope")
        scopes.append(scope.strip())
        values = payload.get("documents")
        if not isinstance(values, list):
            raise ValueError(f"{path} has no documents array")
        for value in values:
            if not isinstance(value, dict):
                raise ValueError(f"{path} contains a non-object document")
            copied = dict(value)
            copied["inventory_fragment"] = path.relative_to(ROOT).as_posix()
            documents.append(copied)
    return documents, scopes


def validate(
    documents: list[dict[str, object]],
    corpus: dict[str, dict[str, object]],
    *,
    strict: bool,
) -> tuple[list[str], list[str]]:
    failures: list[str] = []
    warnings: list[str] = []
    document_ids: set[str] = set()
    parent_ids: set[str] = set()
    parent_records: dict[str, dict[str, object]] = {}
    duplicate_targets: list[tuple[str, str]] = []

    for index, document in enumerate(documents, start=1):
        missing = REQUIRED_DOCUMENT_FIELDS - set(document)
        if missing:
            failures.append(f"Document {index} misses fields: {sorted(missing)}")
            continue
        document_id = document.get("document_id")
        if not isinstance(document_id, str) or not document_id:
            failures.append(f"Document {index} has no document_id")
            continue
        if document_id in document_ids:
            failures.append(f"Duplicate inventory document: {document_id}")
        document_ids.add(document_id)
        source = corpus.get(document_id)
        if source is None:
            failures.append(f"Inventory document is absent from corpus: {document_id}")
            continue
        field_map = {
            "source_family": "source_family",
            "course": "course",
            "year": "year",
            "kind": "kind",
            "stable_url": "stable_url",
            "local_pdf": "local_pdf",
            "local_text": "local_text",
            "source_sha256": "source_sha256",
            "pdf_pages": "pdf_pages",
        }
        for inventory_field, corpus_field in field_map.items():
            if document.get(inventory_field) != source.get(corpus_field):
                failures.append(
                    f"{document_id}: {inventory_field} differs from source-corpus.json"
                )
        problems = document.get("problems")
        if not isinstance(problems, list) or not problems:
            failures.append(f"{document_id}: no inspected parent problems")
            continue
        for problem_index, problem in enumerate(problems, start=1):
            prefix = f"{document_id} problem {problem_index}"
            if not isinstance(problem, dict):
                failures.append(f"{prefix}: entry is not an object")
                continue
            missing_problem = REQUIRED_PROBLEM_FIELDS - set(problem)
            if missing_problem:
                failures.append(f"{prefix}: misses fields {sorted(missing_problem)}")
                continue
            parent_id = problem.get("source_parent_id")
            if not isinstance(parent_id, str) or not parent_id.strip():
                failures.append(f"{prefix}: no source_parent_id")
                continue
            if parent_id in parent_ids:
                failures.append(f"Duplicate source parent id: {parent_id}")
            parent_ids.add(parent_id)
            parent_records[parent_id] = problem
            if not parent_id.startswith(document_id + "-"):
                failures.append(
                    f"{parent_id}: source parent id must begin with its document id"
                )
            question_number = problem.get("question_number")
            if isinstance(question_number, str):
                question_number_valid = bool(question_number.strip())
            else:
                question_number_valid = isinstance(question_number, int) and not isinstance(
                    question_number, bool
                )
            if not question_number_valid:
                failures.append(f"{parent_id}: empty question_number")
            disposition = problem.get("disposition")
            if disposition not in DISPOSITIONS:
                failures.append(f"{parent_id}: invalid disposition {disposition!r}")
            chapter = problem.get("recommended_chapter")
            if disposition in {"selected", "reserved_for_chapter"}:
                if not isinstance(chapter, int) or not 2 <= chapter <= 16:
                    failures.append(
                        f"{parent_id}: {disposition} needs a Chapter 2--16 assignment"
                    )
            elif chapter is not None and (
                not isinstance(chapter, int) or not 2 <= chapter <= 16
            ):
                failures.append(f"{parent_id}: invalid recommended chapter {chapter!r}")
            duplicate_of = problem.get("duplicate_of")
            if disposition == "duplicate":
                if not isinstance(duplicate_of, str) or not duplicate_of:
                    failures.append(f"{parent_id}: duplicate needs duplicate_of")
                else:
                    duplicate_targets.append((parent_id, duplicate_of))
            elif duplicate_of is not None:
                failures.append(f"{parent_id}: only duplicates may set duplicate_of")
            for field in ("parent_scope", "printed_pages", "pdf_pages", "short_topic"):
                if not isinstance(problem.get(field), str) or not problem[field].strip():
                    failures.append(f"{parent_id}: empty {field}")
            pdf_page_locator = problem.get("pdf_pages")
            if isinstance(pdf_page_locator, str):
                page_numbers = [int(value) for value in re.findall(r"\d+", pdf_page_locator)]
                document_pages = document.get("pdf_pages")
                if (
                    not page_numbers
                    or not isinstance(document_pages, int)
                    or min(page_numbers) < 1
                    or max(page_numbers) > document_pages
                ):
                    failures.append(
                        f"{parent_id}: PDF-page locator {pdf_page_locator!r} "
                        f"falls outside the {document_pages!r}-page document"
                    )
            rationale = problem.get("disposition_rationale")
            if not isinstance(rationale, str) or len(WORD_RE.findall(rationale)) < 8:
                failures.append(f"{parent_id}: disposition rationale is not substantive")

    for parent_id, target in duplicate_targets:
        if target not in parent_ids:
            failures.append(f"{parent_id}: duplicate target does not exist: {target}")
        if target == parent_id:
            failures.append(f"{parent_id}: cannot duplicate itself")
        target_record = parent_records.get(target)
        if target_record is not None and target_record.get("disposition") == "duplicate":
            failures.append(
                f"{parent_id}: duplicate target {target} is itself a duplicate"
            )

    expected_documents = {
        document_id
        for document_id, document in corpus.items()
        if not bool(document.get("ancillary"))
    }
    missing_documents = sorted(expected_documents - document_ids)
    extra_documents = sorted(document_ids - set(corpus))
    if extra_documents:
        failures.append(f"Inventory has unknown documents: {extra_documents}")
    if missing_documents:
        message = (
            f"{len(missing_documents)} cached source documents still lack "
            "problem-level disposition inventories"
        )
        (failures if strict else warnings).append(message)
    ancillary_inventory = sorted(
        document_id
        for document_id in document_ids
        if bool(corpus.get(document_id, {}).get("ancillary"))
    )
    if ancillary_inventory:
        warnings.append(
            "Ancillary correction documents are recorded separately: "
            + ", ".join(ancillary_inventory)
        )
    return failures, warnings


def generate(*, strict: bool) -> dict[str, object]:
    corpus = corpus_documents()
    documents, scopes = fragment_documents()
    documents.sort(key=lambda item: str(item.get("document_id", "")))
    failures, warnings = validate(documents, corpus, strict=strict)
    problem_count = sum(
        len(document.get("problems", []))
        for document in documents
        if isinstance(document.get("problems"), list)
    )
    dispositions = Counter(
        problem.get("disposition")
        for document in documents
        for problem in document.get("problems", [])
        if isinstance(problem, dict)
    )
    covered = {str(document.get("document_id")) for document in documents}
    expected = {
        document_id
        for document_id, document in corpus.items()
        if not bool(document.get("ancillary"))
    }
    return {
        "schema_version": 1,
        "strict": strict,
        "scopes": scopes,
        "summary": {
            "corpus_documents": len(corpus),
            "inventory_documents": len(documents),
            "expected_problem_documents": len(expected),
            "missing_problem_documents": len(expected - covered),
            "inspected_parent_problems": problem_count,
            "dispositions": dict(sorted(dispositions.items())),
        },
        "documents": documents,
        "warnings": warnings,
        "failures": failures,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--strict", action="store_true")
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    try:
        payload = generate(strict=args.strict)
    except ValueError as error:
        print(f"Source inventory error: {error}", file=sys.stderr)
        return 1
    rendered = json.dumps(payload, indent=2, ensure_ascii=True) + "\n"
    if args.write:
        OUTPUT.write_text(rendered, encoding="utf-8")
        print(
            f"Wrote {OUTPUT}: {payload['summary']['inventory_documents']} documents, "
            f"{payload['summary']['inspected_parent_problems']} parent problems."
        )
    elif not OUTPUT.is_file() or OUTPUT.read_text(encoding="utf-8") != rendered:
        print("Problem-level source inventory is missing or stale.", file=sys.stderr)
        return 1

    for warning in payload["warnings"]:
        print(f"SOURCE INVENTORY WARNING: {warning}", file=sys.stderr)
    for failure in payload["failures"]:
        print(f"SOURCE INVENTORY FAILURE: {failure}", file=sys.stderr)
    if payload["failures"]:
        return 1
    summary = payload["summary"]
    print(
        "Source inventory: "
        f"{summary['inventory_documents']}/{summary['expected_problem_documents']} "
        f"documents and {summary['inspected_parent_problems']} parents dispositioned."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
