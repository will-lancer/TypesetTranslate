# Chapter 22 coverage and QA

## Source coverage

Chapter 22, “Anomalies,” is fully represented from physical PDF pages
382--443 (printed pages 359--420). Shared physical pages are divided at the
visible semantic headings so that every source element is represented
exactly once.

| Output | Physical pages | Printed pages | Numbered equations |
|---|---:|---:|---:|
| `introduction.tex` | 382, before Section 22.1 | 359 | none |
| `sec221.tex` | 382--384 | 359--361 | 22.1.1--22.1.9 |
| `sec222.tex` | 385--393, before Section 22.3 | 362--370 | 22.2.1--22.2.49 |
| `sec223.tex` | 393--406, before Section 22.4 | 370--383 | 22.3.1--22.3.47 |
| `sec224.tex` | 406--411 | 383--388 | 22.4.1--22.4.3 |
| `sec225.tex` | 412--419, before Section 22.6 | 389--396 | 22.5.1--22.5.9 |
| `sec226.tex` | 419--430 | 396--407 | 22.6.1--22.6.35 |
| `sec227.tex` | 431--439, before Problems | 408--416 | 22.7.1--22.7.38 |
| `backmatter.tex` | 439, from Problems--443 | 416--420 | none |

## Complete inventory

- 190 numbered equations, all explicitly tagged and labeled in strict
  sequence.
- 62 unnumbered mathematical displays.
- Figures 22.1 and 22.2, recreated as TikZ; no scan images are embedded.
- Table 22.1, recreated as a native LaTeX table.
- 13 semantic notes: one section-title note and 12 body footnotes.
- Five centered three-asterisk dividers.
- Four Problems.
- 37 displayed reference entries: 1--26 plus 6a, 7a, 8a, 10a, 10b, 13a,
  16a, 18a, 18b, 18c, and 19a. Every citation and applicable
  reference-to-reference citation has a stable linked destination.

## Verification

- Every section and the chapter backmatter passed an isolated
  `latexmk` compile, complete log audit, and all-page render inspection.
  Detailed source anomalies and local finishing cycles are recorded in
  `reports/`.
- The integrated wrapper is `latex/checks/chapter22.tex`. Its accepted build
  is a 53-page PDF with no LaTeX errors, undefined references, duplicate
  labels, overfull boxes, or underfull boxes. The inherited `hyperref`
  `pagecolor` notice is the only warning.
- All 53 integrated pages were rendered at 150 DPI to
  `/private/tmp/ch22-integrated-qa.eQx6c7/` and visually inspected. Section
  transitions, both figures, the table, dense multiline equations,
  footnotes, Problems, the entire reference list, and all page edges are
  clear and unclipped.
- Mechanical checks confirm the seven expected equation sequences,
  190 matching unique equation labels, zero duplicate labels, four
  Problems, 37 references, and no `\times`, `\mathscr`, placeholder, or
  unfinished-marker macros in the chapter sources.

No unresolved transcription uncertainty remains beyond the
scan-authoritative anomalies documented in the section reports.
