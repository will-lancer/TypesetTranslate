# Chapter 20 Wave 2 — Agent 2 report

## Scope and source

- Owned transcription scope: Section 20.7, the chapter appendix, the problems
  and references, Figure 20.3, and the isolated validation wrapper.
- Source coverage: physical PDF pages 306--317.
- Fresh 300-DPI source renders were made for all twelve physical pages and
  inspected at original resolution. Enlarged crops were used to resolve the
  denser equations, the problem displays, and ambiguous reference details.

## Delivered files

- `latex/chapters/chapter20/sec207.tex`
- `latex/chapters/chapter20/appendix.tex`
- `latex/chapters/chapter20/backmatter.tex`
- `latex/chapters/chapter20/figures/fig20-03.tex`
- `latex/checks/chapter20-wave2-agent2-check.tex`
- `latex/chapters/chapter20/reports/wave2-agent2.md`

## Content inventory

### Section 20.7, “Renormalons”

- 22 numbered equations: (20.7.1)--(20.7.22), each with an explicit tag and
  label.
- Two unnumbered displays.
- Figure 20.3, redrawn in TikZ with its source caption and label.
- Two automatic footnotes, including the optional section-heading note.
- Linked citations to Chapter 20 references 18--22.

### Appendix, “Momentum Flow: The General Case”

- 12 numbered equations: (20.A.1)--(20.A.12), each with an explicit tag and
  label.
- One automatic footnote.
- Linked citation to Chapter 20 reference 3.

### Backmatter

- Five problems.
- Two unnumbered spectral-function displays in Problem 2.
- 22 references, labeled exactly once as `ch20-ref-1` through
  `ch20-ref-22`.
- No lettered reference identifiers occur in this source range.

Total semantic footnotes: three.

## Build and QA

- Isolated build command, run from `newPapers/weinberg_vol2/latex`:

  `latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error checks/chapter20-wave2-agent2-check.tex`

- Result: successful 11-page A4 PDF,
  `latex/chapter20-wave2-agent2-check.pdf`.
- Final structural counts: 22 Section 20.7 tags, 12 appendix tags, and 22
  reference labels.
- Final log has no undefined references, `??`, overfull or underfull boxes,
  duplicate destinations, fatal errors, or emergency stops.
- The sole log warning is the inherited `hyperref` warning that option
  `pagecolor` is no longer available.
- All 11 final output pages were rendered at 180 DPI and visually inspected,
  with every source page in physical PDF pages 306--317 covered during
  comparison. No clipping, collisions, missing content, malformed
  mathematics, or figure-label problems remain.
- Correction cycles used: one of the permitted two. The sole correction
  locally disabled an automatic page break inside Eq. (20.A.8), keeping the
  complete equation together while retaining its automatic footnote.

## Source anomalies and verification notes

- Reference 15 prints the Altarelli--Parisi citation year as 1972. This was
  preserved exactly, although it appears historically anomalous.
- Problem 2 visibly sums over \(N\) while the two matrix-element factors in
  each summand are printed as vacuum-to-vacuum products. Fresh enlarged
  source crops confirmed this, so it was preserved rather than silently
  repaired.
- The positive exponential signs in Eqs. (20.7.18) and (20.7.19) were
  rechecked against enlarged 300-DPI source crops and retained.
- No unresolved transcription uncertainty remains.
