# Release Verification

Release date: 2026-07-31 PDT

## Artifacts

- Untouched comparison edition:
  `../../weinberg-qft/weinberg-vol3.pdf`
- Two-component edition:
  `../../weinberg-qft-two-component/weinberg-vol3-two-component.pdf`
- Two-component PDF SHA-256:
  `8054a1624f75ebc847055700a58d716d7814dd60340a698d549c273699307b83`
- Comparison PDF SHA-256:
  `d9e3f5552091e13019402fde159603f54c09851931b9e137a23a24aca8ab56b3`

## Automated gates

`./build_and_verify.sh` completed successfully:

- sigma, barred-sigma, Lorentz-generator, and gamma-block identities pass;
- independent four-generator exterior-algebra checks give
  `D^2 theta^2 = bar D^2 bar theta^2 = -4` and verify the F-to-D
  projection and even-superfield conjugation rules;
- Chapters 24–32 have exact equation-label, equation-tag, heading, display,
  and footnote parity with the comparison source; corrected cross-reference
  targets are explicitly declared in the audit and `ERRATA.md`;
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
  759,426 non-whitespace characters;
- the built PDF and stable exported PDF are byte-identical.

## Visual QA

All 57 affected or adjacent pages were freshly rendered at 120 dpi and
inspected in ten contact sheets. No clipping, overlap, malformed formula,
missing content, or bad margin was found. The complete 370-page release also
passed Ghostscript parsing, PDF metadata, font embedding, layout, and text
extraction checks.

## Editorial scope

Four-dimensional spinors and superspace formulas in Chapters 24–31 use
dotted/undotted two-component notation under
`TWO_COMPONENT_CONVENTIONS.md`. Chapter 32 retains general
dimension-dependent Clifford notation where a four-dimensional Weyl
decomposition is unavailable; its strictly four-dimensional references use
the edition conventions. The source errors corrected in this review are
listed in `ERRATA.md`.
