# Exercise-edition authoring rules

These rules are release requirements, not suggestions.

## Files and order

Chapter `NN` owns exactly these files:

```text
latex/exercises/chapterNN/weinberg-exercises.tex
latex/exercises/chapterNN/weinberg-solutions.tex
latex/exercises/chapterNN/supplementary-exercises.tex
latex/exercises/chapterNN/supplementary-solutions.tex
```

The chapter backmatter contains one `\chapterexercisehook{NN}` before the
original bibliography or references. Do not place exercise prose in chapter
wrappers or edit the canonical sibling tree.

## Item macros

Populated fragments use one outer `enumerate` environment. Use:

```tex
\WeinbergExercise{3} ...
\WeinbergSolution{3} ...
\SupplementaryExercise{7}{Title}
  {(Adapted from Author, Course, Problem Set 2, Problem 4)}
  {stable-ledger-id}
...
\SupplementarySolution{7}{Title} ...
```

Numbers begin at 1 and are continuous within each chapter. Solution numbers
and supplementary solution titles must exactly match their exercises.
Weinberg exercise prompts are not editorially rewritten.

The title is short and unique. The printed credit contains enough provenance
to identify the exact sheet, chapter, page, or question. Use “Adapted from”
whenever notation, wording, context, or subparts have changed.

## Problem integrity and chapter size

Every substantive chapter contains 10--30 complete supplementary problems.
Ten is a floor and thirty is a ceiling, not a target that licenses filler.
Preserve a source problem's connected subparts as one numbered problem.
Never turn intermediate steps from one parent problem into separate exercises
to increase the count. Short problems remain welcome when they stand on their
own; otherwise retain short checks as subparts of the coherent parent.
Within a multipart problem, refer to the “preceding part,” not the “preceding
exercise.” A separately numbered exercise must restate every result it needs
or cite an explicit supplementary number.
Record a chapter-specific `curation_note` in `exercise-edition.json`
explaining why the final count is the natural complete set.

Treat McGreevy, Harlow, official Cambridge Part III exams and example sheets,
and Kevin Zhou as an unordered first-choice pool, then consult other strong
books, exams, and author-posted lecture notes. Source choice within the pool is
based on problem quality and chapter fit, not a family ranking or quota.

## Source ledger

Every source ID must resolve in `source-ledger.json`, and each ID represents
one provenance parent used by exactly one supplementary exercise. For
`adapted` and `verbatim-permitted` records that parent is one exact source
problem; reusing it for several exercises is treated as an artificial split.
Each ledger object has:

```json
{
  "id": "stable-ledger-id",
  "source_family": "mcgreevy",
  "document_id": "mcgreevy-physics-215b-2024-ps2",
  "parent_problem": "Problem 4, parts (a)--(e)",
  "use_mode": "adapted",
  "author_or_institution": "Author or institution",
  "title": "Course, notes, book, or examination title",
  "year": "2024",
  "locator": "Problem Set 2, Problem 4",
  "url": "https://stable.example/source",
  "chapters": [2],
  "adaptation_notes": "What was selected, reorganized, or converted."
}
```

`source_family` is one of `mcgreevy`, `harlow`, `cambridge-part-iii`,
`knzhou`, or `other`. `use_mode` is `adapted`, `original-inspired`, or
`verbatim-permitted`. Verbatim use requires a concrete `reproduction_basis`
identifying workspace-supplied text or an explicit reuse license or
permission. Otherwise write the problem independently at the full depth of
the source and credit it as “Adapted from” or “Inspired by,” as appropriate.
“Adapted from” is permitted only when the edition preserves the cited
problem's complete connected conceptual and subpart arc under one number.
Sharing a topic, theorem, or final result is not enough. Before release,
compare every adapted prompt directly with the source parent. If the source
arc is not preserved, either rewrite the prompt and solution to preserve it
or classify the genuinely independent problem as `original-inspired` with a
broad, accurate locator.

Use only verified public, official, or author-posted sources. Never use
pirated books or solution manuals. Cambridge sources must be Part III, never
Part II, and the archive has no 2020 papers. Do not invent a year or locator.
Third-party solutions may be used to check work but are never copied.

## Solutions

Every solution must show the central reasoning and enough intermediate steps
to be independently checked. Define nonstandard notation; state assumptions;
check dimensions, signs, normalizations, symmetry factors, and relevant
limits. Prefer unnumbered display equations in backmatter so editorial
equations cannot collide with the chapter's numbered equations.

Follow `NOTATION.md`. In particular, use `\InKet`, `\OutKet`, `\InBra`, and
`\OutBra` whenever an asymptotic-state label is intended.

## Continuous checks

Run:

```sh
python3 audit_exercises.py
./build_and_verify.sh --draft
```

Before release, both commands must pass in strict mode through
`./build_and_verify.sh`.
