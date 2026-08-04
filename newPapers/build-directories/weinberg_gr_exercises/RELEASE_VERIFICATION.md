# Release Verification

Status: **PENDING — exercise collection rebuild in progress**

The former 2026-08-01 release statement described the inherited 300-item
layer.  That layer is now explicitly provisional and its old passing build is
not release evidence for this rebuild.  See
`provisional-exercise-dispositions.json` for the immutable item-level audit.

This document must remain pending until all of the following describe the same
final exported binary:

- `source-corpus.json` and `exercise-source-inventory.json` cover every cached
  source document and every complete parent problem with an explicit
  disposition;
- `exercise-ledger.json` reconciles exactly with every printed prompt and
  solution ID, exact locator, use mode, and departure;
- `source-fidelity-audit.json` contains two distinct passed, content-addressed
  reviews for every selected problem;
- `./build_and_verify.sh` passes in strict mode, including notation, canonical
  isolation, references, layout, Ghostscript parsing, and font checks;
- the final PDF is rendered with Poppler and every changed exercise/solution
  page plus all transitions is visually inspected at readable resolution;
- the stable export is byte-identical to the verified build and its path,
  byte count, page count, PDF metadata, and SHA-256 are recorded below;
- the canonical sibling tree and canonical export still match
  `canonical-baseline.json` exactly.

## Final artifact record

- Release date: pending
- Exercise-ready PDF: `../../weinberg-gr-exercises/weinberg-gr-exercises.pdf`
- PDF SHA-256: pending
- Bytes: pending
- Pages: pending
- Poppler visual-QA record: pending
- Strict build transcript/result: pending
- Canonical-guard result: pending
