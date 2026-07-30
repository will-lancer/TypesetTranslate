#!/usr/bin/env python3
"""Audit supplementary-material duplication across all three QFT editions."""

from __future__ import annotations

import argparse
import difflib
import json
import sys
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path

import audit_weinberg_qft_exercises as edition_audit


HERE = Path(__file__).resolve().parent
EDITION_NAMES = (
    "weinberg_vol1_exercises",
    "weinberg_vol2_exercises",
    "weinberg_vol3_exercises",
)


@dataclass(frozen=True)
class Record:
    volume: int
    chapter: int
    number: str
    title: str
    body: str

    @property
    def identifier(self) -> str:
        return f"V{self.volume}:S.{self.chapter}.{self.number}"


def records_for(
    root: Path,
    volume: int,
    filename: str,
    macro: str,
    argument_count: int,
) -> list[Record]:
    records: list[Record] = []
    pattern = f"chapter*/{filename}"
    for path in sorted((root / "latex" / "exercises").glob(pattern)):
        chapter = int(path.parent.name.removeprefix("chapter"))
        text = path.read_text(encoding="utf-8")
        calls = edition_audit.macro_calls(text, macro, argument_count)
        bodies = edition_audit.macro_bodies(text, calls)
        for call, body in zip(calls, bodies):
            records.append(
                Record(
                    volume=volume,
                    chapter=chapter,
                    number=call.args[0].strip(),
                    title=call.args[1].strip(),
                    body=body,
                )
            )
    return records


def cross_volume_pairs(records: list[Record]):
    for left_index, left in enumerate(records):
        for right in records[left_index + 1 :]:
            if left.volume != right.volume:
                yield left, right


def exact_duplicate_groups(
    records: list[Record],
    normalizer,
    minimum_words: int = 0,
) -> list[list[Record]]:
    groups: dict[str, list[Record]] = defaultdict(list)
    for record in records:
        normalized = normalizer(record)
        if normalized and len(normalized.split()) >= minimum_words:
            groups[normalized].append(record)
    return [
        group
        for group in groups.values()
        if len({record.volume for record in group}) > 1
    ]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--root",
        type=Path,
        default=HERE,
        help="directory containing all three exercise-edition roots",
    )
    parser.add_argument(
        "--output",
        type=Path,
        help="JSON report path (default: ROOT/weinberg-qft-cross-volume-audit.json)",
    )
    args = parser.parse_args()
    root = args.root.resolve()

    failures: list[str] = []
    warnings: list[str] = []
    prompts: list[Record] = []
    solutions: list[Record] = []
    counts: dict[str, dict[str, int]] = {}

    for volume, name in enumerate(EDITION_NAMES, start=1):
        edition_root = root / name
        if not edition_root.is_dir():
            failures.append(f"Missing exercise edition: {edition_root}")
            continue
        volume_prompts = records_for(
            edition_root,
            volume,
            "supplementary-exercises.tex",
            "SupplementaryExercise",
            4,
        )
        volume_solutions = records_for(
            edition_root,
            volume,
            "supplementary-solutions.tex",
            "SupplementarySolution",
            2,
        )
        prompts.extend(volume_prompts)
        solutions.extend(volume_solutions)
        counts[name] = {
            "supplementary_exercises": len(volume_prompts),
            "supplementary_solutions": len(volume_solutions),
        }

    prompt_by_id = {
        (record.volume, record.chapter, record.number): record for record in prompts
    }
    solution_by_id = {
        (record.volume, record.chapter, record.number): record
        for record in solutions
    }
    for key in sorted(set(prompt_by_id) - set(solution_by_id)):
        failures.append(
            f"Supplementary exercise has no cross-volume solution record: "
            f"{prompt_by_id[key].identifier}"
        )
    for key in sorted(set(solution_by_id) - set(prompt_by_id)):
        failures.append(
            f"Supplementary solution has no cross-volume exercise record: "
            f"{solution_by_id[key].identifier}"
        )
    for key in sorted(set(prompt_by_id) & set(solution_by_id)):
        prompt_title = edition_audit.normalized_title(prompt_by_id[key].title)
        solution_title = edition_audit.normalized_title(solution_by_id[key].title)
        if prompt_title != solution_title:
            failures.append(
                "Supplementary title mismatch across exercise/solution records: "
                f"{prompt_by_id[key].identifier}"
            )

    title_groups = exact_duplicate_groups(
        prompts,
        lambda record: edition_audit.normalized_title(record.title),
    )
    for group in title_groups:
        failures.append(
            "Duplicate supplementary title across volumes: "
            + ", ".join(record.identifier for record in group)
        )

    prompt_groups = exact_duplicate_groups(
        prompts,
        lambda record: edition_audit.normalized_problem(record.body),
        minimum_words=18,
    )
    for group in prompt_groups:
        failures.append(
            "Duplicate supplementary prompt across volumes: "
            + ", ".join(record.identifier for record in group)
        )

    solution_groups = exact_duplicate_groups(
        solutions,
        lambda record: edition_audit.normalized_problem(record.body),
        minimum_words=35,
    )
    for group in solution_groups:
        failures.append(
            "Duplicate supplementary solution across volumes: "
            + ", ".join(record.identifier for record in group)
        )

    normalized_titles = {
        record: edition_audit.normalized_title(record.title) for record in prompts
    }
    normalized_prompts = {
        record: edition_audit.normalized_problem(record.body) for record in prompts
    }
    for left, right in cross_volume_pairs(prompts):
        left_title = normalized_titles[left]
        right_title = normalized_titles[right]
        if min(len(left_title), len(right_title)) >= 24:
            title_ratio = difflib.SequenceMatcher(
                None, left_title, right_title
            ).ratio()
            if title_ratio >= 0.88 and left_title != right_title:
                warnings.append(
                    "Suspiciously similar titles "
                    f"{left.identifier} and {right.identifier} "
                    f"(ratio {title_ratio:.2f})"
                )

        left_body = normalized_prompts[left]
        right_body = normalized_prompts[right]
        left_words = left_body.split()
        right_words = right_body.split()
        if min(len(left_words), len(right_words)) < 24:
            continue
        length_ratio = min(len(left_words), len(right_words)) / max(
            len(left_words), len(right_words)
        )
        if length_ratio < 0.75:
            continue
        body_ratio = difflib.SequenceMatcher(None, left_body, right_body).ratio()
        if body_ratio >= 0.90 and left_body != right_body:
            warnings.append(
                "Suspiciously similar prompt bodies "
                f"{left.identifier} and {right.identifier} "
                f"(ratio {body_ratio:.2f})"
            )

    payload = {
        "editions": counts,
        "totals": {
            "supplementary_exercises": len(prompts),
            "supplementary_solutions": len(solutions),
        },
        "warnings": warnings,
        "failures": failures,
    }
    output_path = (
        args.output.resolve()
        if args.output
        else root / "weinberg-qft-cross-volume-audit.json"
    )
    output_path.write_text(
        json.dumps(payload, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    for warning in warnings:
        print(f"WARNING: {warning}", file=sys.stderr)
    if failures:
        print("CROSS-VOLUME AUDIT FAILURES", file=sys.stderr)
        for failure in failures:
            print(f"  - {failure}", file=sys.stderr)
        return 1
    print(
        "Cross-volume audit passed: "
        f"{len(prompts)} supplementary exercises / "
        f"{len(solutions)} supplementary solutions; "
        f"{len(warnings)} similarity warnings."
    )
    print(f"Wrote report: {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
