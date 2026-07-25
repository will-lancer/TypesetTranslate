# Chapter 22 wave 1 — agent 3 report

## Scope and source boundary

- Transcribed complete Section 22.2, “Transformation of the Measure: The
  Abelian Anomaly,” from physical PDF p. 385 through the upper portion of
  physical p. 393 (printed pp. 362--370).
- The assigned p. 392 endpoint is not the semantic section boundary:
  Eqs. (22.2.46)--(22.2.49) and the closing Atiyah--Singer paragraph are
  above the Section 22.3 heading on physical p. 393. They are therefore
  included. The Section 22.3 heading and all text below it are excluded.
- Fresh 300-DPI renders of physical pp. 385--393 were inspected
  individually, with 450/600-DPI rerenders and enlarged crops used for
  dense equations, anomalous references, Eq. (22.2.47), and the closing
  boundary. OCR and PDF text extraction were used only as aids; the rendered
  scans were authoritative.
- No Chapter 22 assembly file or content outside Section 22.2 was edited.

## Delivered files

- `latex/chapters/chapter22/sec222.tex`
- `latex/checks/chapter22-wave1-agent3-check.tex`
- `latex/chapters/chapter22/reports/wave1-agent3.md`

## Exact content inventory

- 49 numbered equations, (22.2.1)--(22.2.49), in strict sequence. Every
  equation has an explicit `\tag{22.2.N}` and matching
  `\label{eq:22.2.N}`.
- 4 unnumbered mathematical displays:
  the two-line Fourier representation of the anomaly, the electromagnetic
  anomaly formula, the quark-charge trace, and the Euclidean Dirac trace.
- 1 automatic semantic footnote, attached to the regulator-function
  condition.
- 1 centered three-asterisk divider.
- 2 linked Chapter 22 citations: [6] and [6a].
- No figures, tables, or section-title notes.
- Equation and section references are linked. Notation follows
  `NOTATION.md`, including `\mathcal`, `\mathbf{1}`, `\sl{}`, and `\cdot`
  in place of printed multiplication signs.

## Preserved source anomalies

The following forms were verified at high resolution and intentionally
preserved instead of silently corrected:

- Physical p. 391 / printed p. 368 says that “the constant \(g\) in
  Eq. (22.2.1)” must have the stated value, even though the immediately
  preceding comparison is to Eq. (22.1.1), where \(g\) is defined. The
  visible reference `(22.2.1)` is retained and linked to `eq:22.2.1`.
- Physical p. 392 / printed p. 369 prints formula `(22.12.13)` where the
  intended target is Eq. (22.2.13). The printed text is retained and linked
  to `eq:22.2.13`.
- Physical p. 393 / printed p. 370 prints `Eq. (2.2.44)` where the intended
  target is Eq. (22.2.44). The printed text is retained and linked to
  `eq:22.2.44`.
- Eq. (22.2.47) prints
  \(\varphi_u^\dagger(x)\varphi_v(x)\) in its second sum, rather than the
  contextually expected
  \(\varphi_v^\dagger(x)\varphi_v(x)\). The mixed \(u,v\) subscripts were
  confirmed in a 600-DPI crop and retained.
- The paragraph before Eq. (22.2.46) prints “orthornormal.” That spelling is
  retained.

## Build and visual QA

- Isolated wrapper:
  `checks/chapter22-wave1-agent3-check.tex`.
- Build command, run from `newPapers/weinberg_vol2/latex`:
  `latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error
  -outdir=../../../tmp/pdfs/ch22-sec222-check
  checks/chapter22-wave1-agent3-check.tex`.
- Result: successful 8-page A4 PDF.
- All 8 final pages were rendered at 180 DPI and inspected individually.
  The section opening, every equation and unnumbered display, the footnote,
  divider, linked anomalous references, Eq. (22.2.47), page edges, and the
  closing boundary are clear and unclipped.
- One of the permitted two bounded finishing cycles was used. The initial
  build had one 60.9692-pt overfull inline explanation. A source-neutral
  forced line break removed it without changing wording or adding a display.
- The final log has no undefined or multiply defined references, overfull
  or underfull boxes, missing files, or content warnings. Its sole warning
  is the inherited `jheppub`/`hyperref` warning that option `pagecolor` is
  no longer available.
- Static audits confirmed 49 strict-sequence tags, 49 matching
  strict-sequence labels, 4 unnumbered displays, 1 footnote, 1 divider,
  2 citation links, zero figures/tables/placeholders, no prohibited notation,
  and a clean scoped `git diff --check`.

## Full-integration requirements

- Include `sec222.tex` after Section 22.1 and before `sec223.tex`.
- Section 22.1 must provide `eq:22.1.1`, `eq:22.1.2`, and `eq:22.1.3`;
  these already exist in `sec221.tex`.
- The Chapter 22 backmatter must provide `ch22-ref-6` and
  `ch22-ref-6a`.
- Full-book destinations must provide `sec:7.3`, `sec:19.4`,
  `app:23.A`, and `sec:23.5`. The current isolated wrapper supplies
  check-only stubs; the present repository does not yet define those four
  destinations in content files.
- The assembled preamble must retain the existing `slashed`, `amsmath`,
  `amssymb`, and `hyperref` support used throughout the chapter.

## Uncertainty

None. The mathematics, prose, punctuation, source anomalies, exact p. 393
boundary, and final render were checked directly against the source.
