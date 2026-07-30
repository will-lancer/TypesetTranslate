# Weinberg QFT Volume I — Exercise Edition

This is an independent, expanded exercise edition of the repository's
modernized transcription of Steven Weinberg's *The Quantum Theory of Fields,
Volume I: Foundations*. It is built from the sibling canonical tree
`../weinberg_vol1`, which is never modified by this project.

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

The files for Chapter `NN` are under
`latex/exercises/chapterNN/`. See `AUTHORING.md` for the required macros and
`NOTATION.md` for binding conventions. `WORKFLOW.md` defines the
chapter-ownership, source-verification, audit, and release sequence.

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
../../weinberg-qft-exercises/weinberg-vol1-exercises.pdf
```

Neither command writes a canonical Weinberg PDF.
