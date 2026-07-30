# Release Verification

Release date: 2026-07-30 PDT

## Artifacts

- Untouched comparison edition:
  `../../weinberg-qft/weinberg-vol3.pdf`
- Two-component edition:
  `../../weinberg-qft-two-component/weinberg-vol3-two-component.pdf`
- Two-component PDF SHA-256:
  `38ccbfffee7626988bc599063166c6c18aeddd99c67268dbc89e60812dfbe90b`
- Comparison PDF SHA-256:
  `5a69c9fbd0fa6f3ef570e88750762b71ce9f2980a634530d0356f9a823c68f3d`

## Automated gates

`./build_and_verify.sh` completed successfully:

- sigma, barred-sigma, Lorentz-generator, and gamma-block identities pass;
- independent four-generator exterior-algebra checks give
  `D^2 theta^2 = bar D^2 bar theta^2 = -4` and verify the F-to-D
  projection and even-superfield conjugation rules;
- Chapters 24–32 have exact equation-label, equation-tag,
  cross-reference-target, heading, display, and footnote parity with the
  comparison source;
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
  759,664 non-whitespace characters.

## Visual QA

Every one of the 370 rendered pages was inspected across three independent
page ranges: 1–128, 129–256, and 257–370. Dense formula pages, figures,
chapter transitions, appendices, references, and both indexes received
additional checks. No clipping, overlap, malformed equation, broken
figure, black box, missing page, bad margin, or font corruption was found.
Page 2 is the intentional blank title verso, and the whitespace at the end
of page 370 is the intentional end of the subject index. A fresh
370-page render of the final release binary was then compared
pixel-for-pixel with the inspected render at the QA resolution, with zero
mismatches.

## Editorial scope

Four-dimensional spinors and superspace formulas in Chapters 24–31 use
dotted/undotted two-component notation under
`TWO_COMPONENT_CONVENTIONS.md`. Chapter 32 retains general
dimension-dependent Clifford notation where a four-dimensional Weyl
decomposition is unavailable; its strictly four-dimensional references use
the edition conventions.
