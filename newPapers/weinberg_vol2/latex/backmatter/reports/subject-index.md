# Subject Index transcription report

## Scope and boundary

- Transcribed the complete Subject Index from physical PDF pages 507--512
  (printed pages 484--489), beginning with the `Subject Index` heading and
  ending with `Zinn--Justin equation, 42, 80--2, 93, 405--6`.
- Verified the outer boundaries against physical page 506, which ends the
  Author Index, and physical page 513, which is blank.
- Used fresh 300-DPI renders of physical pages 506--513 in
  `/private/tmp/weinberg-vol2-subject-source-300/`. Ambiguous symbols and
  group names were checked against 600-DPI crops in
  `/private/tmp/weinberg-vol2-subject-source-600/`.
- Did not edit the Author Index, the backmatter assembly, the volume master,
  the README, or the work plan.

## Structural inventory

- 308 top-level entries and 71 indented subentries, for 379 transcribed
  entries in total.
- 43 cross-references: 26 `see` references and 17 `also see` references,
  with source italics retained.
- 23 source-style alphabetic gaps.
- Native two-column composition using `multicols*`, with eleven explicit
  column breaks reproducing the source's twelve columns across six pages.
- Mathematical symbols, italics, capitalization, punctuation, page-number
  lists, and page ranges are encoded directly in the index source.

## Scan-authoritative readings retained

Potentially surprising punctuation was checked against the scan and retained:

- `differential forms 36, 38--9, 400` has no comma after `forms`.
- `vector (of isospin) 185` has no comma before the page number.
- The `nucleon` subentry reads `masses 209, 233--4`, without a comma after
  `masses`.
- `spontaneous symmetry breaking 63` has no comma before `63`.
- `proton decay, 318,` ends with the comma printed in the source.

High-resolution review also confirmed the theta, eta, xi, lambda, and Lambda
symbols; neutrino notation; group names; the page number 471; and the
distinction among `Z`, `Z_n`, and `Z^0`.

## Notation normalization

The source prints direct-product signs in six affected index entries. In
accordance with the volume-wide rule in `NOTATION.md`, these are encoded as
`\cdot` rather than `\times`. There are seven product glyphs in those six
entries because the `chiral symmetry` cross-reference names both
`SU(2)\cdot SU(2)` and `SU(3)\cdot SU(3)`. A final source audit confirms that
no `\times` remains in the Subject Index.

## Verification

- Isolated build command, run from `newPapers/weinberg_vol2/latex`:
  `latexmk -pdf -interaction=nonstopmode -halt-on-error
  checks/subject-index-check.tex`
- Result: successful six-page PDF. The final log contains no overfull boxes,
  undefined references, font warnings, LaTeX errors, or fatal errors. Four
  benign underfull boxes remain in narrow index entries; the inherited
  `hyperref` warning about the removed `pagecolor` option is unchanged.
- Rendered every final page at 180 DPI in
  `/private/tmp/weinberg-vol2-subject-index-render-final/` and visually
  inspected all six pages. No clipping, collision, overflow, missing entry,
  or column-boundary drift was found. The normalized products were
  specifically rechecked on output pages 2, 3, and 6.
- Numeric-token sequences were compared page by page against source OCR.
  An alphabetic word-frequency audit was also compared against the OCR, with
  OCR confusions resolved from the 300- and 600-DPI scans.
- The first and last entries of all twelve columns match the source. The
  outer endpoints are `$a_1$ meson, 271` and
  `Zinn--Justin equation, 42, 80--2, 93, 405--6`.
- Mechanical counts confirm 308 top-level entries, 71 subentries, 26 `see`
  references, 17 `also see` references, 23 alphabetic gaps, eleven column
  breaks, and no forbidden `\times`.
- Two layout-finishing cycles were used. The final required notation-only
  normalization and rebuild did not alter pagination or column layout.
- `git diff --check` passes for the Subject Index, its isolated check wrapper,
  and this report.
