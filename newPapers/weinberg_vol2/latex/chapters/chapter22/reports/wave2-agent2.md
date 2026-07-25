# Chapter 22 Wave 2 — Agent 2 report

## Coverage and boundaries

- Section 22.7, “Anomalies and Goldstone Bosons”: physical PDF pp. 431--439
  (printed pp. 408--416), beginning at the section heading and ending with
  the final prose immediately before the Problems heading.
- Chapter 22 Problems and References: physical PDF pp. 439--443 (printed
  pp. 416--420), beginning at the Problems heading and continuing through
  Ref. 26, the final Chapter 22 entry.
- Physical p. 439 was checked at original detail to enforce the shared
  boundary: `sec227.tex` contains no Problems content, and `backmatter.tex`
  begins exactly at the Problems heading.
- All thirteen source pages were freshly rendered at 300 DPI and inspected
  individually. Dense equations on physical pp. 434--435 were additionally
  checked in fresh 600-DPI renders.

## File inventory

- `chapters/chapter22/sec227.tex`
- `chapters/chapter22/backmatter.tex`
- `checks/chapter22-wave2-agent2-check.tex`
- `chapters/chapter22/reports/wave2-agent2.md`

No chapter assembly file, master file, bibliography file, or content outside
the assigned span was edited.

## Content inventory

- Eqs. (22.7.1)--(22.7.38), all in strict sequence, each with an explicit
  `\tag{22.7.N}` and matching `\label{eq:22.7.N}`.
- Five unnumbered mathematical displays, one automatic semantic body
  footnote, and one centered `* * *` divider.
- Four Problems.
- Thirty-seven reference entries: 1--26 plus 6a, 7a, 8a, 10a, 10b, 13a,
  16a, 18a, 18b, 18c, and 19a.
- Every reference entry has a unique stable destination
  `\label{ch22-ref-ID}`. Printed reference-to-reference citations in
  Refs. 10a, 19a, and 21 are linked.
- All six Chapter 22 citation occurrences in Section 22.7 are linked to
  Refs. 16, 18, and 24--26. Applicable equation and section references in
  the section and Problems are linked.
- No figures or tables occur in the assigned span.

## Dependencies

- The isolated wrapper supplies check-only equation destinations for
  (15.1.17), (19.6.17), (19.6.18), (19.7.2), (19.8.1)--(19.8.3),
  (22.3.12), (22.3.34)--(22.3.38), (22.5.5), (22.5.6), (22.6.1),
  (22.6.2), (22.6.5), and (22.6.6), plus section destinations for
  Sections 19.8 and 22.5.
- Section 22.7 provides `sec:22.7` and `eq:22.7.1`--`eq:22.7.38` to the
  integrated chapter. The backmatter provides all `ch22-ref-*` destinations
  used throughout Chapter 22.
- There are no media or asset dependencies.

## Build and visual QA

- From `newPapers/weinberg_vol2/latex`,
  `latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error
  checks/chapter22-wave2-agent2-check.tex` succeeds and produces an
  11-page A4 PDF.
- The final log has no LaTeX errors, unresolved links, duplicate labels,
  overfull boxes, or underfull boxes. The inherited `hyperref` `pagecolor`
  notice is the only package warning.
- All eleven output pages were rendered at 180 DPI and inspected
  individually. Checks covered every page edge, all dense multiline
  equations, the footnote, all unnumbered displays, the centered divider,
  the Problems transition, every reference-list page, and the final entry.
  No clipping, collision, bad glyph, or unreadable material remains.
- Finishing cycle 1 restored the semantic paragraph break after
  Eq. (22.7.17), which the initial render visually swallowed. Finishing
  cycle 2 normalized six multiplication continuation signs to the
  project-standard `\cdot`; affected pages 5--7 were rerendered and
  reinspected.
- Static audits confirm 38 strict-sequence tags, 38 matching labels, five
  unnumbered displays, one footnote, one divider, four Problems, 37
  reference items and destinations, no unlinked citation tokens, no
  placeholders or prohibited notation macros, and a clean scoped
  `git diff --check`.
- Correction cycles used: two of the permitted two.

## Source anomalies preserved

- Eq. (22.7.16) visibly has upper integration limit \(t\), although its
  following boundary evaluation runs from \(t=0\) to \(t=1\). Its second
  line also omits the preceding \(d^4y\) integral. Both printed forms were
  retained.
- The prose after Eq. (22.7.33) prints `form.We`, `zerofor`, `$z^5=0$and`,
  `$z^\mu$of`, and `haveshown`; these missing spaces were retained.
- Ref. 2 has no final period.
- Ref. 10 prints `Georgi,Lie`.
- Ref. 10a prints missing spaces in `Zumino,Nucl. Phys.`,
  `et al.(Plenum`, and `Singer,and`; these were retained.
- Ref. 11 prints the anomalous volume `96`.
- Ref. 15 prints `review,see` and abbreviates its final journal as
  `Nuc. Phys.`.
- Ref. 16 prints a double comma after `E. Witten` and omits the comma
  between `P. Roy` and `Phys. Lett.`.

No unresolved transcription uncertainty remains.
