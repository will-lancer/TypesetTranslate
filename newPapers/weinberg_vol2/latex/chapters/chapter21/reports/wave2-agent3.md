# Chapter 21 Wave 2 — Agent 3 report

## Coverage and boundaries

- Appendix, “General Unitarity Gauge”: physical PDF pp. 375--376 (printed
  pp. 352--353), beginning at the Appendix heading and ending immediately
  after Eq. (21.A.11) and the sentence “as was to be shown.”
- Problems and the complete Chapter 21 reference list: physical PDF
  pp. 376--381 (printed pp. 353--358), beginning at the Problems heading and
  continuing through Ref. 47.
- Physical p. 376 was inspected at original detail to enforce the shared
  boundary: no Problems content is present in `appendix.tex`, and no Appendix
  content is duplicated in `backmatter.tex`.
- All seven source pages in the span were freshly rendered at 300 DPI and
  inspected individually.

## File inventory

- `chapters/chapter21/appendix.tex`
- `chapters/chapter21/backmatter.tex`
- `checks/chapter21-wave2-agent3-check.tex`
- `chapters/chapter21/reports/wave2-agent3.md`

No chapter assembly file, master file, bibliography file, or content outside
the assigned span was edited.

## Content inventory

- Eqs. (21.A.1)--(21.A.11), all in strict sequence, with an explicit
  `\tag{21.A.N}` and matching `\label{eq:21.A.N}` on every equation.
- Six problems.
- Fifty-seven reference entries: 1--47 plus 3a, 5a, 20a, 20b, 27a--27c,
  36a, 43a, and 44a.
- Every reference entry has a unique stable destination
  `\label{ch21-ref-ID}`. Six printed cross-references between reference
  entries are linked to those destinations.
- The three cross-references in the Problems and the three Chapter 21
  equation references in Ref. 47 are linked.
- There are no unnumbered displays, footnotes, figures, tables, citations, or
  centered dividers in the assigned span.
- Notation follows `NOTATION.md`, including `\cdot` for the
  \(SU(2)\cdot U(1)\) product and `\mathcal T` for the gauge generators.

## Verification

- Compile command, run from `newPapers/weinberg_vol2/latex`:

  `latexmk -pdf -interaction=nonstopmode -halt-on-error checks/chapter21-wave2-agent3-check.tex`

- Result: success after the normal reference-resolution passes, producing a
  six-page PDF with all references resolved.
- The final log contains no undefined references, multiply defined labels,
  missing inputs, undefined control sequences, fatal errors, overfull boxes,
  or underfull boxes.
- All six output pages were rendered at 300 DPI and inspected individually.
  The appendix ending, the Problems transition, every reference-list page,
  all page edges, and the final entry were checked; no clipping, collision,
  bad glyph, or unreadable material was found.
- The long inline gauge transformation before Eq. (21.A.11) initially
  produced a 32.25014 pt overfull line in both the isolated and integrated
  builds. A source-neutral forced line break was added before the formula.
  The rebuilt affected page was inspected at full resolution, and the final
  log is free of box warnings.
- Static audits confirmed 11 strict-sequence tags, 11 matching labels, six
  Problems items, 57 reference items in the exact printed sequence, 57 unique
  reference destinations, six internal reference links, no placeholders or
  prohibited notation macros, and a clean scoped `git diff --check`.

## Warnings

- One inherited `hyperref` warning from `jheppub.sty`: option `pagecolor` is
  no longer available.
- There are no content-file or box warnings in the final isolated build.

## Source anomalies preserved

- Eq. (21.A.5) prints subscript \(i\) on the first summation,
  \(i\sum_i\phi_a x_a\), even though its summand uses \(a\) and Eq. (21.A.4)
  immediately above uses \(\sum_a\). The printed index was preserved.
- Ref. 9 prints the surname “J. Leites-Lopes.”
- Ref. 10 prints `Phys. Lett. 46` without a `B` volume prefix.
- Ref. 14 prints its second citation as `Phys. Rev. 5, 1413 (1972)`, without
  a `D` before the volume.
- Ref. 22 has no comma between `et al.` and the following journal title.
- Ref. 25 prints `Nucl. Phys. B169, 137 1980);`, without the opening
  parenthesis before the year.
- Ref. 26 prints “S. Fanchotti” and `Phys. Rev. D48, 307 (1973)`.
- Ref. 31 prints `Nucl. Phys. B15, 237 (1979)`.
- Ref. 38 has no comma after “P. M. Anderson.”
- Ref. 44 prints `Phys. Rev. 42, 9967 (1990)`, without a `B` before the
  volume.

These forms were verified against the rendered pages and preserved rather
than silently corrected.

## Uncertainty

None. Appendix prose and mathematics, all six Problems, all 57 references,
the p. 376 boundary, and the final render were checked directly against the
source.
