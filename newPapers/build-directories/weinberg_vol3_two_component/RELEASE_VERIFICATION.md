# Release Verification

Release date: 2026-08-01 PDT

## Artifacts

- Corrected comparison edition:
  `../../weinberg-vol3.pdf`
- Two-component edition:
  `../../weinberg-vol3-two-component.pdf`
- Two-component PDF SHA-256:
  `4b854add595303e833dca642283c1a14e89d68a71b06396e0996fac4b3f28e1f`
- Comparison PDF SHA-256:
  `e031856555caaca5425dd7c4539652a95f6f129b5998b4344871b7f6b3db84e2`

## Automated gates

`./build_and_verify.sh` completed successfully:

- sigma, barred-sigma, Lorentz-generator, and gamma-block identities pass;
- independent four-generator exterior-algebra checks give
  `D^2 theta^2 = bar D^2 bar theta^2 = -4` and verify the F-to-D
  projection and even-superfield conjugation rules;
- Chapters 24–32 have exact equation-label, equation-tag, heading, display,
  footnote, and reference-target parity with the corrected comparison source;
- no unmarked forbidden four-component syntax remains in the strict
  four-dimensional scope;
- all guarded semantic hotspots pass;
- LaTeX finishes cleanly with no errors or undefined references;
- layout has 20 overfull boxes versus 22 in the comparison source, with
  the same maximum overflow, 41.26297 pt;
- PDF text extraction succeeds and the stable export is produced.

Independent integrity checks also pass:

- Ghostscript parses and renders all pages to a null device without error;
- `pdfinfo` reports 370 A4 pages, PDF 1.7, no encryption, and no suspect
  structure;
- every listed font is embedded and subset;
- layout-preserving text extraction contains 370 page separators and
  759,427 non-whitespace characters;
- the built PDF and stable exported PDF are byte-identical.

## Visual QA

The original 57-page review remains valid. For the comparison integration, 11
affected two-component pages were freshly rendered along with the matching
mass-matrix pages in the original and exercise editions, for 13 pages across
three contact sheets. No clipping, overlap, malformed formula, missing
content, bad glyph, or bad margin was found. The complete 370-page release
also passed Ghostscript parsing, PDF metadata, font embedding, layout, and
text extraction checks.

## Editorial scope

Four-dimensional spinors and superspace formulas in Chapters 24–31 use
dotted/undotted two-component notation under
`TWO_COMPONENT_CONVENTIONS.md`. Chapter 32 retains general
dimension-dependent Clifford notation where a four-dimensional Weyl
decomposition is unavailable; its strictly four-dimensional references use
the edition conventions. The source errors corrected in this review are
listed in `ERRATA.md`.
