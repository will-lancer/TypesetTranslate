# Exercise-edition workflow

## 1. Reserve a nonoverlapping scope

One editor owns one chapter's four files at a time. Source-ledger changes are
append-only. Never edit the canonical sibling tree, another editor's chapter,
or a stable export during authoring.

## 2. Inspect the chapter

Read the chapter wrapper, its included sections and appendices, the extracted
Weinberg exercises, `NOTATION.md`, and `MODERNIZATION.md`. List the actual
chapter topics before selecting supplementary material.

## 3. Verify sources

Use public official, institutional, or author-posted material. Record the
author/institution, exact title, year, locator, stable URL, chapter use, and
adaptation notes in `source-ledger.json`. Exclude pirated texts, solution
manuals, Cambridge Part II, and nonexistent Cambridge 2020 papers.

## 4. Write the four components

- Leave `weinberg-exercises.tex` unchanged.
- Solve every W item in `weinberg-solutions.tex`.
- Curate 10--30 complete, nonduplicative, chapter-specific parent problems in
  `supplementary-exercises.tex`; never split one source problem to raise the
  item count.
- Give every S item a complete independently written solution in
  `supplementary-solutions.tex`.

Follow `AUTHORING.md` for macros, titles, credits, and numbering. Use the
modernized in/out helpers and prefer unnumbered editorial displays.
Treat McGreevy, Harlow, official Cambridge Part III examinations and example
sheets, and Kevin Zhou as an unordered first-choice pool. Choose within it by
quality and chapter fit, then consult other strong sources.

## 5. Audit continuously

Run:

```sh
python3 audit_exercises.py
python3 render_inventory.py
python3 render_source_ledger.py
```

Resolve numbering, title, provenance, duplicate, notation, short-solution, and
source-diversity findings before proceeding.

Generate or refresh content-addressed review records with:

```sh
python3 audit_exercises.py --write-fidelity-template
```

Then compare every adapted prompt side by side with its exact source parent,
and review every independently written problem for self-containment, quality,
chapter fit, and solution coverage. Mark a record passed in
`source-fidelity-audit.json` only after every checklist item has been inspected.
Any subsequent prompt, solution, locator, or use-mode change invalidates the
record and requires a new review.

## 6. Build the complete volume

Run:

```sh
./build_and_verify.sh --draft
```

Inspect any warning introduced by the owned chapter. The chapter handoff
requires zero new undefined references, duplicate labels, or overfull boxes.

## 7. Release only when complete

After every chapter in all three volumes is finished, run
`../build_all_weinberg_qft_exercise_editions.sh`. This executes each strict
volume gate, the cross-volume duplicate audit, and the release-manifest
renderer. Then render representative pages to PNG, visually inspect exercise
and solution pages and at least one transition into original references,
verify the inherited-index notice and regenerated `INDEX_PAGINATION.md`
source-to-live page map, record PDF/font/text checks and hashes in
`RELEASE_VERIFICATION.md`, and retain only the distinct exercise-edition
export.
