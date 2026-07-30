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

## Source ledger

Every source ID must resolve in `source-ledger.json`. Each ledger object has:

```json
{
  "id": "stable-ledger-id",
  "author_or_institution": "Author or institution",
  "title": "Course, notes, book, or examination title",
  "year": "2024",
  "locator": "Problem Set 2, Problem 4",
  "url": "https://stable.example/source",
  "chapters": [2],
  "adaptation_notes": "What was selected, reorganized, or converted."
}
```

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

