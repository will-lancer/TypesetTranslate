# Weinberg QFT Volume III — Exercise Edition

This is an independent, expanded exercise edition of the repository's
modernized transcription of Steven Weinberg's *The Quantum Theory of Fields,
Volume III: Supersymmetry*. It is built from the sibling canonical tree
`../weinberg_vol3`, which is never modified by this project.

The conventional four-component Volume III is the authoritative base for this
edition. The repository's two-component-spinor tree is a specialized parallel
edition and is not modified here.

The edition is a work in progress until `./build_and_verify.sh` passes without
`--draft` and `RELEASE_VERIFICATION.md` records a stable export.

## Chapter structure

Every chapter loads four modular fragments before its original bibliography or
references:

1. Weinberg Exercises
2. Solutions to Weinberg Exercises
3. Supplementary Exercises
4. Solutions to Supplementary Exercises

Weinberg's existing exercise prompts are preserved verbatim in the first
fragment. All solutions are editorial additions. Supplementary prompts are
newly edited adaptations or original editorial problems and carry an inline
source credit tied to `source-ledger.json`.
Chapter 24, the Historical Introduction, retains and solves its three
original Weinberg problems but intentionally has no supplementary set.

The files for Chapter `NN` are under
`latex/exercises/chapterNN/`. See `AUTHORING.md` for the required macros and
`NOTATION.md` for binding conventions. `WORKFLOW.md` defines the
chapter-ownership, source-verification, audit, and release sequence.
`INDEX_PAGINATION.md` is regenerated from the completed build. It crosswalks
the inherited printed-source index pagination to live chapter, exercise,
solution, and reference page starts in this expanded edition.

## Build and audit

From this directory:

```sh
./build_and_verify.sh --draft
```

Draft mode compiles the whole volume and reports unfinished chapter counts and
solutions. The release gate is:

```sh
./build_and_verify.sh
```

Strict mode requires complete one-to-one solutions, source-ledger coverage,
continuous numbering, count targets or written exceptions, canonical-source
hash integrity, zero undefined or duplicate references, zero overfull boxes,
parseable PDF output, and embedded/subset fonts. It exports only to:

```text
../../weinberg-qft-exercises/weinberg-vol3-exercises.pdf
```

Neither command writes a canonical Weinberg PDF.
