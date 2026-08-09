# Weinberg GR exercise edition

This workspace is an exercise-ready copy of the modernized LaTeX edition of
Steven Weinberg's
*Gravitation and Cosmology: Principles and Applications of the General Theory
of Relativity*.

The original edition remains in the sibling `weinberg_gr` build directory and
is protected by `canonical-baseline.json` plus `canonical_guard.py`.  This copy
has its own export path and can be changed without modifying or overwriting
that edition.  The inherited 300-item exercise layer is currently being
replaced: none of those items is accepted merely because the old build passed.
Its immutable, exercise-by-exercise keep/rebuild/reject evidence is recorded in
`provisional-exercise-dispositions.json`; the twelve entries whose old credits
did identify a parent receive full side-by-side findings in
`provisional-exact-parent-comparisons.json`.  Chapter 1 remains exercise-free;
the release target for each of Chapters 2--16 is 10--30 independently usable,
source-bound exercises with complete matching solutions.

See `EXERCISES.md` for the authoring interface and `EXERCISE_SOURCES.md` for
the source policy.  The content-addressed source cache is indexed by
`source-corpus.json`; the comprehensive parent-level decisions are merged into
`exercise-source-inventory.json`; final selections will be bound through
`exercise-ledger.json` and `source-fidelity-audit.json`.  While this rebuild is
in progress, `./build_and_verify.sh --draft` is the appropriate command and the
release record remains pending.

## Source

- Repository source: `../../../origPapers/weinberg_gr.pdf`
- 681 physical PDF pages
- Image-only scan with no useful OCR text layer
- The local scan omits Contents page xxii and printed pages 306, 390, 392,
  418, 440, 594, and 602. Matching pages from the same Internet Archive scan are
  preserved and hashed under `source-supplements/`; each adjacent provenance
  file records the exact item, page mapping, extraction command, dimensions,
  and checksum.
- The PDF permissions flag copying and printing as disabled, but Poppler can
  render it locally for visual transcription.

The rendered local page image, together with the eight hashed supplemental
pages, is authoritative. OCR may be used as a drafting aid, but equations,
symbols, accents, punctuation, figures, and page boundaries must be checked
visually.

## Build and verification

For an in-progress integration build, run from this directory:

```bash
./build_and_verify.sh --draft
```

Draft mode verifies the immutable book source and canonical sibling, checks the
downloaded source corpus and currently available disposition fragments, audits
every materialized section, scans exercise notation, compiles the whole book,
and reports unfinished editorial work without treating it as a publication.

The final gate is:

```bash
./build_and_verify.sh
```

Strict mode additionally requires every planned file to be source-reviewed and
compile-clean, every reference to resolve, zero overfull boxes, a successful
full-PDF Ghostscript parse, and embedded/subset fonts. Only a strictly verified
build is exported to
`../../weinberg-gr-exercises.pdf`.

The publisher publication-data leaf and the separate copyright-
acknowledgements leaf are retained as source transcriptions under
`latex/frontmatter/` but are intentionally excluded from `latex/master.tex`
and from the compiled edition.

`RELEASE_VERIFICATION.md` is the final hash and all-page visual-QA record. It
must remain marked pending until the exported release binary—not an earlier
draft—has passed those checks.

The 122-section handoff scaffold is generated from `SECTION_PLAN.md`. Check it
without writing, or safely create only missing files and replace untouched TODO
chapter wrappers, with:

```bash
python3 scaffold_sections.py
python3 scaffold_sections.py --write
```

The generator never overwrites a section that already exists.

Before transcribing or reviewing a section, read:

- `NOTATION.md` for binding mathematical conventions;
- `MODERNIZATION.md` for source-to-target conversion rules;
- `SECTION_PLAN.md` for stable section filenames and headings;
- `TRANSCRIPTION.md` for file headers, labels, references, figures, and QA.

The reusable QA programs are:

- `verify_source.py`: SHA-256 and page-count check for the 681-page scan;
- `audit_transcription.py`: plan, assembly, metadata, tag, label, and reference
  inventory;
- `source_manifest.py`: generated physical-page/source inventory and
  `TRANSCRIPTION_STATUS.md`; refresh both with
  `python3 source_manifest.py --write`;
- `audit_notation.py`: definite old-signature and source-notation regressions,
  plus compact-derivative review candidates;
- `audit_index.py`: source-page structure, entry counts, selective-italic
  locator integrity, and common OCR-failure checks for the combined index
  (`--force` runs it before the completion header is set);
- `source_corpus.py`: exact official-source URLs, local PDF/text paths, page
  counts, and content hashes for the inspected research corpus;
- `source_inventory.py`: comprehensive document and complete-parent
  disposition coverage, including duplicate and dependency decisions;
- `provisional_dispositions.py`: immutable 300-item inherited-layer audit;
- `audit_exercises.py`: stable prompt/solution IDs, Chapter 1 exclusion,
  10--30 bounds, one-complete-parent/one-number binding, exact ledger
  reconciliation, and two current content-addressed review passes;
- `canonical_guard.py`: exact canonical subtree and canonical-export guard;
- `audit_layout.py`: box-warning inventory and a zero-overflow strict gate.

After a draft or strict build, render a page range to a fresh ignored directory
under `/private/tmp` for visual QA:

```bash
./render_for_review.sh 1 20
```

An optional third argument chooses another output directory. Review images are
derived artifacts and must not be committed.

## Suggested transcription layout

Keep one writable target per agent:

```text
latex/
  chapters/
    chapter01.tex
    chapter01/
      sec11.tex
      sec12.tex
      ...
  figures/
    chapter01/
      fig01-01.tex
      ...
```

The chapter index file should contain only its `\section` heading and `\input`
statements. Put substantial transcription in section files so work can be
assigned without merge collisions.

## Fidelity rules

1. Assign work by physical PDF page, not the printed page number.
2. Preserve visible wording, physical claims, numbering, references, footnotes,
   epigraphs, and front/back matter while applying the notation conversions in
   `NOTATION.md`, except for the two intentionally omitted copyright leaves.
3. Remove scan-induced line-wrap hyphenation, but do not paraphrase.
4. Recreate diagrams as TikZ where practical; use an explicit
   `TODO FIGURE:` comment rather than guessing.
5. Mark uncertain readings with `VERIFY:` comments.
6. Follow `NOTATION.md` and `MODERNIZATION.md`; do not import conventions from
   the Weinberg QFT projects.
7. Treat the signature conversion as a mathematical conversion, not a textual
   substitution. Recheck time-index signs, curvature signs, determinants,
   contractions, and limiting cases.
8. Compile each section or chapter after editing, then render and inspect the
   resulting PDF.
