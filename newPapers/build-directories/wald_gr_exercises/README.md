# Wald GR solutions and supplementary problems edition

This directory is a parallel, reproducible edition of Robert M. Wald's
*General Relativity*.  It preserves the completed notation-modernized text and
adds worked solutions to all 85 original problems, followed by 14 new problems
and their solutions.

## Source

- Repository source: `../../../origPapers/wald_gr.pdf`
- 505 physical PDF pages
- SHA-256:
  `c0ca3f87d5dc8689ec89a2b9aef376a00670160b593e17dc533546f22b094599`
- Searchable text is available as a drafting aid, but equations, accents,
  symbols, index positions, and page boundaries must be checked against the
  rendered source page.

The source PDF remains authoritative for Wald's text.  The solutions are
editorial additions.  Supplementary problem credits are recorded in
`exercise-source-ledger.json`.

## Project policy

Read these files in order:

1. `NOTATION.md` — binding mathematical and typographic policy.
2. `MODERNIZATION.md` — permitted editorial transformations.
3. `SECTION_PLAN.md` — stable filenames and source starts.
4. `TRANSCRIPTION.md` — file headers, equation labels, and QA requirements.
5. `SOURCE_MAP.md` — physical/printed page mapping and source integrity.
6. `EXERCISE_EDITION.md` — exercise structure, numbering, and credit policy.

The complete transcription is organized into 95 source-reviewed transcription
units. Chapter and appendix wrappers, plus implementation subfiles within a
unit, are not counted separately. The local `latex/jheppub.sty` pins the JHEP
layout dependency used by the build.

## Build and verification

For a non-exporting integration build:

```sh
./build_and_verify.sh --draft
```

Strict mode additionally requires all planned files to be source-reviewed,
all references to resolve, and layout and font checks to pass:

```sh
./build_and_verify.sh
```

Only strict mode exports
`output/pdf/wald-gr-solutions-exercises.pdf`.  The canonical
`../wald_gr` tree and its release artifact are never overwritten.

The original scaffold generator can still be checked without writing, or used
to materialize only missing files without overwriting existing content:

```sh
python3 scaffold_sections.py
python3 scaffold_sections.py --write
```
