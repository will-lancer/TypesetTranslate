# Chapter 21 Wave 2 — Agent 2 report

## Scope and source

- Owned transcription scope: Sections 21.4 and 21.5 and the isolated
  validation wrapper.
- Source coverage: physical PDF pages 341--355, beginning with the Section
  21.4 heading on page 341 and ending immediately before the Section 21.6
  heading on page 355.
- Fresh 300-DPI source renders were made for all fifteen physical pages and
  inspected at original resolution. Enlarged views were used to resolve dense
  equations and ambiguous indices.
- No figures or tables occur in this source range.

## Delivered files

- `latex/chapters/chapter21/sec214.tex`
- `latex/chapters/chapter21/sec215.tex`
- `latex/checks/chapter21-wave2-agent2-check.tex`
- `latex/chapters/chapter21/reports/wave2-agent2.md`

## Content inventory

### Section 21.4, “Dynamically Broken Local Symmetries”

- 36 numbered equations: (21.4.1)--(21.4.36), each with an explicit tag and
  label.
- All unnumbered source displays, including the custodial-symmetry and
  technicolor material.
- One automatic footnote, attached to the section heading.
- Linked citations to Chapter 21 references 28--31 and linked internal
  section, equation, and appendix references.

### Section 21.5, “Electroweak--Strong Unification”

- 16 numbered equations: (21.5.1)--(21.5.16), each with an explicit tag and
  label.
- All unnumbered source displays, including the fermion-generation array.
- Two automatic footnotes.
- Linked citations to Chapter 21 references 32--36, 36a, and 47, plus linked
  internal section and equation references.

Total numbered equations: 52. Total semantic footnotes: three.

## Build and QA

- Isolated build command, run from `newPapers/weinberg_vol2/latex`:

  `latexmk -pdf -interaction=nonstopmode -halt-on-error checks/chapter21-wave2-agent2-check.tex`

- Result: successful 12-page A4 PDF,
  `latex/chapter21-wave2-agent2-check.pdf`.
- Structural audits confirmed consecutive tags and labels for all 36 Section
  21.4 equations and all 16 Section 21.5 equations, three semantic footnotes,
  and no unresolved references, duplicate labels, placeholders, banned
  notation, overfull or underfull boxes, or fatal errors.
- The sole log warning is the inherited `hyperref` warning that option
  `pagecolor` is no longer available.
- All 12 final output pages were rendered at 180 DPI and individually
  inspected. No clipping, collisions, overflow, malformed mathematics,
  illegible text, bad page breaks, or footnote-placement problems remain.
- Correction cycles used: one of the permitted two. The correction completed
  internal links, fixed a contraction index, restored source punctuation in
  the generation display, and normalized trace products to the house
  `\cdot` convention.

## Verification notes

- The unnumbered Section 21.4 expression
  \(F_{ab}^{2}=-\sum_{nm\ell}(x_a)_{nm}(x_b)_{n\ell}v_m v_\ell\) was
  rechecked against both the enlarged source and Eq. (21.1.7); its printed
  absence of conjugation marks was preserved.
- The source-range boundary on physical page 355 was checked visually: the
  final two Section 21.5 paragraphs are included, and the Section 21.6
  heading and subsequent text are excluded.
- No unresolved transcription uncertainty remains.
