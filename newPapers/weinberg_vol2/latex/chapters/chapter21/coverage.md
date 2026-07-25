# Chapter 21 coverage manifest

Source: `origPapers/weinberg_vol2.pdf`, physical PDF pages 318--381
inclusive, printed pages 295--358. Chapter 21 starts on physical page 318;
Chapter 22 starts on physical page 382 and is excluded. Fresh rendered pages,
not OCR, were authoritative throughout transcription and review.

## Semantic ownership and numbered equations

| File | Material | Physical pages | Printed pages | Numbered equations |
|---|---|---:|---:|---|
| `introduction.tex` | Chapter introduction | 318 (before heading) | 295 | none |
| `sec211.tex` | 21.1 Unitarity Gauge | 318 (from heading)--323 (partial last page) | 295--300 | 21.1.1--21.1.25 |
| `sec212.tex` | 21.2 Renormalizable \(\xi\)-Gauges | 323 (from heading)--327 | 300--304 | 21.2.1--21.2.23 |
| `sec213.tex` | 21.3 The Electroweak Theory | 328--341 (partial last page) | 305--318 | 21.3.1--21.3.55 |
| `sec214.tex` | 21.4 Dynamically Broken Local Symmetries | 341 (from heading)--350 (partial last page) | 318--327 | 21.4.1--21.4.36 |
| `sec215.tex` | 21.5 Electroweak--Strong Unification | 350 (from heading)--355 (partial last page) | 327--332 | 21.5.1--21.5.16 |
| `sec216.tex` | 21.6 Superconductivity | 355 (from heading)--375 (partial last page) | 332--352 | 21.6.1--21.6.86 |
| `appendix.tex` | Appendix: General Unitarity Gauge | 375 (from heading)--376 (partial last page) | 352--353 | 21.A.1--21.A.11 |
| `backmatter.tex` | Problems and References | 376 (from Problems heading)--381 | 353--358 | none |

Every numbered equation has an explicit tag and matching stable label. The
complete inventory is 252 equations, and every section sequence is
consecutive.

## Required inventories

- Numbered figures and tables: zero.
- Semantic footnotes: 17, comprising 15 ordinary `\footnote` calls and two
  optional-reading title notes implemented with automatic
  `\footnotemark`/`\footnotetext` pairing.
- Unnumbered mathematical displays: 31.
- Centered three-asterisk dividers: three.
- Problems: six.
- References: 57, numbered 1--47 with entries 3a, 5a, 20a, 20b, 27a--27c,
  36a, 43a, and 44a in their printed positions. Every entry has a stable
  `ch21-ref-*` destination, and every source paper-reference marker is linked.

## Shared transition pages

Semantic ownership is by heading. The preceding section owns all material
above each heading on physical pages 323, 341, 350, 355, 375, and 376.
Section 21.2 ends on physical page 327 and Section 21.3 begins on physical
page 328; Section 21.6 owns its continuation above the Appendix heading on
physical page 375; the appendix owns its continuation above the Problems
heading on physical page 376. Every adjacent source-page join from physical
pages 318/319 through 380/381 was reviewed exactly once.

## Verification record

- Five non-overlapping worker assignments compiled and rendered their ranges
  in isolation. Every isolated output page was compared with the
  corresponding source renders; correction pages were recompiled,
  rerendered, and reinspected.
- Static integration checks found exactly 252 unique equation tags and 252
  matching equation labels, 17 semantic footnotes, 31 unnumbered displays,
  three centered dividers, six problem items, and 57 reference items. There
  are no duplicate labels, missing internal targets, scaffold markers, or
  unresolved transcription notes.
- The integrated chapter check compiles to 56 A4 pages. Check-only
  destinations represent legitimate links into other chapters and
  appendices, so the chapter-only PDF contains no unresolved references. The
  final log has no LaTeX errors, undefined links, duplicate destinations, or
  overfull or underfull boxes. A final source-neutral pair of permitted
  inline-math breakpoints removed the former 6.09952 pt Section 21.1
  overflow; the affected page was rerendered and inspected at full
  resolution.
- All 56 integrated pages were rendered with Poppler and inspected in four
  complete contact sheets. Full-resolution checks covered every section and
  appendix boundary, dense mathematics, long footnotes, the Problems and
  References transition, and the final reference page. The corrected
  anomalous summation index in Eq. (21.A.5) and the final Section 21.1 layout
  were separately rerendered and reinspected. No clipping, overlap, malformed
  glyph, equation-tag collision, blank-content loss, or misplaced footnote
  remains.
- Final full-volume integration and export are deferred until Chapters
  22--23 and both indexes are complete.
- The volume-wide notation pass normalized the four residual product glyphs
  in Sections 21.3 and 21.6 to `\cdot`, rebuilt the chapter cleanly, and
  rerendered and reinspected all affected section pages.

Source anomalies were preserved rather than silently corrected. These include
the `S_{CD,BD}` subscripts in Eqs. 21.1.21, 21.1.22, and 21.1.24; the
coefficient \(-\xi/2\) in Eq. 21.2.16; “ha an eigenvector”; “which can be
eliminating”; the un-conjugated printed form of the unnumbered \(F_{ab}^2\)
expression in Section 21.4; the references to Eqs. 21.6.9 and 21.6.8 in the
type-II-vortex paragraph; the \(\sum_i\) index in Eq. 21.A.5; and the
bibliographic irregularities itemized in the section reports.
