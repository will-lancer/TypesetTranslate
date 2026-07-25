# Chapter 21 Wave 1 — Agent 3 report

## Coverage and boundaries

- Chapter 21 introductory text on physical PDF p. 318 (printed p. 295), immediately before Section 21.1.
- Section 21.1, “Unitarity Gauge”: physical PDF pp. 318--323 (printed pp. 295--300), ending immediately before the Section 21.2 heading.
- Section 21.2, “Renormalizable \(\xi\)-Gauges”: physical PDF pp. 323--327 (printed pp. 300--304), ending immediately before the Section 21.3 heading on physical p. 328.
- Every source page in the span, plus physical p. 328 for the closing boundary, was freshly rendered and inspected.

## File inventory

- `chapters/chapter21/introduction.tex`
- `chapters/chapter21/sec211.tex`
- `chapters/chapter21/sec212.tex`
- `checks/chapter21-wave1-agent3-check.tex`
- `chapters/chapter21/reports/wave1-agent3.md`

No chapter assembly file, master file, bibliography file, or content outside the assigned span was edited.

## Content inventory

- Eqs. (21.1.1)--(21.1.25) and (21.2.1)--(21.2.23), for 48 numbered equations in strict sequence, plus the unnumbered scalar--gauge cross-term display in Section 21.2.
- Every numbered equation has an explicit `\tag{21.X.N}` and matching `\label{eq:21.X.N}`.
- One source footnote and the centered `* * *` break in Section 21.1 are present.
- Eight citation occurrences are present, covering seven distinct targets: [1], [2], [3], [3a], [4], [5], and [5a].
- Citation markers use `\hyperref[ch21-ref-ID]{[ID]}`; equation references within and outside the wave are linked.
- There are no figures or tables in the assigned span.
- Notation follows `NOTATION.md`, including `\cdot` for products, `\bra`/`\ket` for states, `\mathbf1` for the identity, and `\sl` for slashed quantities.

## Verification

- Compile command, run from `newPapers/weinberg_vol2/latex`:

  `latexmk -pdf -interaction=nonstopmode -halt-on-error checks/chapter21-wave1-agent3-check.tex`

- Result: success after the normal reference-resolution passes, producing a 9-page PDF with all references resolved.
- The final log contains no undefined references, multiply defined labels, missing inputs, undefined control sequences, or fatal errors.
- All nine output pages were rendered at 180 DPI and inspected individually. The opening and closing boundaries, the footnote, the centered divider, dense multiline equations, and every page edge were checked; no clipping, collision, bad glyph, or unreadable material was found.
- Static audits confirmed 48 strict-sequence tags, 48 matching labels, one footnote, one unnumbered display, one centered divider, eight linked citation occurrences, no placeholders or prohibited notation macros, and a clean scoped `git diff --check`.

## Warnings

- One inherited `hyperref` warning from `jheppub.sty`: option `pagecolor` is no longer available.
- One 6.09952 pt overfull box occurs in the long inline kinetic-gauge formula in Section 21.1. The affected rendered line was inspected at full-page and high resolution; it remains inside the readable page area with no clipping or collision.

## Source anomalies preserved

- Eqs. (21.1.21), (21.1.22), and (21.1.24) print the matrix-element subscript as \(S_{CD,BD}\), despite the surrounding process \(A+B\to C+D\). The printed subscript was preserved.
- Eq. (21.2.16) prints the scalar mass-matrix contribution with coefficient \(-\xi/2\). It was preserved even though the surrounding derivation and Eq. (21.2.19) may suggest a different coefficient.
- The prose before Eq. (21.2.19) says “\(\mu^2_{\alpha\beta}\) ha an eigenvector.” The source typo “ha” was preserved.

## Uncertainty

None. Prose, numbered and unnumbered mathematics, the footnote, citations, paragraph structure, and both section boundaries were checked directly against the rendered source.
