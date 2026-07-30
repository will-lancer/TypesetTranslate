#!/usr/bin/env python3
"""Audit the chapter exercise/solution structure and source coverage."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent
EXERCISES = ROOT / "latex" / "exercises"
ADDITIONAL = EXERCISES / "additional"
CHAPTERS = ROOT / "latex" / "chapters"
MASTER = ROOT / "latex" / "master.tex"
TARGET_EXERCISES_PER_CHAPTER = 20
AVAILABLE_CAMBRIDGE_YEARS = [
    *range(2001, 2020),
    *range(2021, 2026),
]

EXERCISE_RE = re.compile(
    r"^\\begin\{exercise\}(?:\[[^\]]*\])?\{([^{}\n]+)\}",
    re.MULTILINE,
)
SOLUTION_RE = re.compile(r"^\\begin\{solution\}(?:\[[^\]]*\])?", re.MULTILINE)
PART_II_RE = re.compile(r"\bPart[\s~-]*II(?!I)\b", re.IGNORECASE)


def fail(message: str, failures: list[str]) -> None:
    failures.append(message)


def main() -> int:
    failures: list[str] = []
    all_sources: list[str] = []
    total_exercises = 0
    total_solutions = 0

    master = MASTER.read_text(encoding="utf-8")
    chapter_one = (CHAPTERS / "chapter01.tex").read_text(encoding="utf-8")
    if r"\chapterexercises{1}" in master or r"\chapterexercises{1}" in chapter_one:
        fail("Chapter 1 must not have an exercise hook", failures)

    for chapter in range(2, 17):
        wrapper_path = CHAPTERS / f"chapter{chapter:02d}.tex"
        wrapper = wrapper_path.read_text(encoding="utf-8")
        hook = rf"\chapterexercises{{{chapter}}}"
        backmatter = rf"\input{{chapters/chapter{chapter:02d}/backmatter.tex}}"
        if wrapper.count(hook) != 1:
            fail(f"Chapter {chapter}: expected exactly one exercise hook", failures)
        if wrapper.count(backmatter) != 1:
            fail(f"Chapter {chapter}: expected exactly one backmatter input", failures)
        if hook in wrapper and backmatter in wrapper:
            if wrapper.index(hook) > wrapper.index(backmatter):
                fail(
                    f"Chapter {chapter}: exercises must precede references",
                    failures,
                )

        exercise_path = EXERCISES / f"chapter{chapter}.tex"
        if not exercise_path.exists():
            fail(f"Chapter {chapter}: missing {exercise_path.name}", failures)
            continue
        text = exercise_path.read_text(encoding="utf-8")

        markers = [
            r"\begin{exercises}",
            r"\end{exercises}",
            r"\begin{solutions}",
            r"\end{solutions}",
        ]
        if any(text.count(marker) != 1 for marker in markers):
            fail(
                f"Chapter {chapter}: expected one Exercises and one Solutions block",
                failures,
            )
        elif [text.index(marker) for marker in markers] != sorted(
            text.index(marker) for marker in markers
        ):
            fail(
                f"Chapter {chapter}: block order must be Exercises then Solutions",
                failures,
            )

        extra_exercises = ADDITIONAL / f"chapter{chapter}-exercises.tex"
        extra_solutions = ADDITIONAL / f"chapter{chapter}-solutions.tex"
        expected_inputs = [
            rf"\input{{exercises/additional/{extra_exercises.name}}}",
            rf"\input{{exercises/additional/{extra_solutions.name}}}",
        ]
        for fragment, input_line in zip(
            (extra_exercises, extra_solutions), expected_inputs
        ):
            if not fragment.exists():
                fail(f"Chapter {chapter}: missing {fragment.name}", failures)
            if text.count(input_line) != 1:
                fail(
                    f"Chapter {chapter}: expected exactly one input of "
                    f"{fragment.name}",
                    failures,
                )

        expanded_text = text
        for fragment in (extra_exercises, extra_solutions):
            if fragment.exists():
                expanded_text += "\n" + fragment.read_text(encoding="utf-8")

        sources = EXERCISE_RE.findall(expanded_text)
        solutions = SOLUTION_RE.findall(expanded_text)
        if len(sources) < TARGET_EXERCISES_PER_CHAPTER:
            fail(
                f"Chapter {chapter}: expected at least "
                f"{TARGET_EXERCISES_PER_CHAPTER} exercises, found {len(sources)}",
                failures,
            )
        if len(sources) != len(solutions):
            fail(
                f"Chapter {chapter}: {len(sources)} exercises but "
                f"{len(solutions)} solutions",
                failures,
            )
        for source in sources:
            if not source.strip():
                fail(f"Chapter {chapter}: empty source credit", failures)
            if PART_II_RE.search(source):
                fail(
                    f"Chapter {chapter}: forbidden Part II source credit: {source}",
                    failures,
                )

        all_sources.extend(sources)
        total_exercises += len(sources)
        total_solutions += len(solutions)

    joined_sources = "\n".join(all_sources)
    for year in AVAILABLE_CAMBRIDGE_YEARS:
        credit = f"Cambridge Part III, {year} exam"
        if credit not in joined_sources:
            fail(f"Cambridge Part III GR exam year {year} is not represented", failures)
    if "Cambridge Part III, 2020 exam" in joined_sources:
        fail("2020 must not be listed: Cambridge has no Part III exam archive for it", failures)

    for sheet in range(1, 5):
        if f"Cambridge Part III Sheet {sheet}" not in joined_sources:
            fail(f"Tong Cambridge Part III Sheet {sheet} is not represented", failures)
    for problem_set in range(1, 10):
        if f"McGreevy, Problem Set {problem_set}" not in joined_sources:
            fail(f"McGreevy Problem Set {problem_set} is not represented", failures)
    if "MIT 8.962" not in joined_sources:
        fail("No complementary MIT 8.962 source is represented", failures)

    if failures:
        print("EXERCISE AUDIT FAILURES", file=sys.stderr)
        for failure in failures:
            print(f"  - {failure}", file=sys.stderr)
        return 1

    unique_sources = len(set(all_sources))
    print(
        "Exercise audit: "
        f"{total_exercises} exercises, {total_solutions} solutions, "
        f"{unique_sources} credited source labels; Chapters 2--16 have at "
        f"least {TARGET_EXERCISES_PER_CHAPTER} each, Chapter 1 has none, "
        "and all available Cambridge "
        "Part III GR exam years 2001--2025 (except 2020) are represented."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
