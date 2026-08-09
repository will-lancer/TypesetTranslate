# Render review: Yin Physics 253a pilot

Reviewed `latex/master.pdf` rebuilt at 2026-08-08 22:19:34. It contains 19 PDF
pages. `qa/rendered/pilot-01.png` through `pilot-19.png` still have the earlier
21:34--21:35 timestamps, so I rendered the rebuilt PDF at native readable
resolution in a temporary QA location for this review.

## Page review

| PDF page | Content | Result |
|---:|---|---|
| 1 | Title and abstract | Clean JHEP title block, rule, and abstract. |
| 2 | Contents and Part I opener | Hierarchy and linked contents are clear. |
| 3 | Section 1.1 opening | Text fits and hyphenation is clean; printed uncertainty label present. |
| 4 | Section 1.1 continuation | Dense text remains readable; printed uncertainty labels present. |
| 5 | Figure 1 and Section 1.2 start | Diagram and caption are clear; no collision or clipping. |
| 6 | Course plan | List hierarchy and text density are clear. |
| 7 | Section 1.3 opening, (1.1) | Display and section break are clean; one uncertainty label is printed. |
| 8 | Free-particle states, (1.2)--(1.3) | Formulae, labels, and dialogue layout are clear. |
| 9 | Creation operators, (1.4)--(1.5) | Equations fit and remain legible. |
| 10 | Hamiltonian, (1.6) | Equation layout is clean; printed uncertainty labels remain. |
| 11 | Interaction Hamiltonian, (1.7), Section 1.4 | Spacious but balanced; heading and first paragraph are clean. |
| 12 | Figure 2 and Section 1.5 start | Figure labels, paths, caption, and section break are clear. |
| 13 | Poincare covariance, (1.8)--(1.9) | Long displays and prose fit; printed uncertainty labels remain. |
| 14 | Infinitesimal transformations, (1.10) | Equation and text block are clean; printed uncertainty labels remain. |
| 15 | Infinitesimal transformations, (1.10) | Equation and text block are clean; printed uncertainty labels remain. |
| 16 | Generators and Section 1.6 start, (1.11)--(1.13) | Formulae fit; printed unresolved labels remain. |
| 17 | Microcausality, (1.14)--(1.17) | The former overfull Hamiltonian now wraps inside the text block. |
| 18 | Free scalar field, (1.18)--(1.23) | Displays, underbraces, and explanation remain legible. |
| 19 | Section 1.7, Final question, and Problem Set note | Hierarchy, final Q&A, and required note are readable and correctly placed. |

## Figure fidelity

- Figure 1 on PDF page 5 matches source-note physical page 6: the QFT fork,
  central dashed divider, color-coded course arrows, classifications, and
  examples are retained.
- Figure 2 on PDF page 12 matches source-note physical page 10: the offset
  axes, shared blue event, four green light-cone branches, purple timelike
  response, and red forbidden path are retained.

## Blockers

1. The compiled chapter prints unresolved transcription annotations in reader
   text. Examples are PDF page 3/source line 24; PDF page 4/lines 109, 130,
   136, 147, and 153; PDF page 5/lines 197 and 212; PDF page 7/line 546; PDF
   page 6/line 385; PDF page 7/line 546; PDF page 8/line 605; PDF page 9/line
   710; PDF page 11/lines 720, 766, and 771; PDF page 14/lines 925, 980, and
   985; PDF page 15/lines 1022, 1027, 1060, and 1075; PDF page 16/lines 1155,
   1171, and 1209; PDF page 17/lines 1239 and 1290; PDF page 18/line 1330;
   and PDF page 19/lines 1448 and 1465 in
   `latex/chapters/253a/chapter01.tex`. Bracketed labels include `unclear`,
   `unresolved`, `inaudible`, and `likely`. Resolve them from the source,
   reword them as editorial prose, or move them out of reader-facing text.
2. The official PNG render set is stale: `latex/master.pdf` is stamped
   22:19:34, while `qa/rendered/pilot-01.png` through `pilot-19.png` are
   stamped 21:34--21:35. Regenerate the official nineteen-page PNG set from
   this PDF before release.

## Checks

- Ghostscript processed all 19 pages with `-dPDFSTOPONERROR`.
- All listed fonts are embedded. Contents, sections, figures, and equations
  have named destinations. No external URL object is present.
- `latex/master.log` has no overfull box, undefined reference, undefined
  citation, or fatal error. It retains one underfull-vbox warning and the
  non-rendering `hyperref` pagecolor and JHEP missing-email warnings.
- The final Problem Set 1 note correctly identifies source physical pages
  15--19 and defers them to the exercises appendix.

Unresolved blockers: reader-facing uncertainty annotations remain throughout the chapter; official `qa/rendered/pilot-01.png` through `pilot-19.png` do not match the rebuilt PDF.
