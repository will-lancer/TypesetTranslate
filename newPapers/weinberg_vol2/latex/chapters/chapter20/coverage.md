# Chapter 20 coverage manifest

Source: `origPapers/weinberg_vol2.pdf`, physical PDF pages 275--317
inclusive, printed pages 252--294. Chapter 20 starts on physical page 275;
Chapter 21 starts on physical page 318 and is excluded. Fresh rendered pages,
not OCR, were authoritative throughout transcription and review.

## Semantic ownership and numbered equations

| File | Material | Physical pages | Printed pages | Numbered equations |
|---|---|---:|---:|---|
| `introduction.tex` | Chapter introduction | 275--276 (partial last page) | 252--253 | none |
| `sec201.tex` | 20.1 The Expansion: Description and Derivation | 276 (from heading)--278 (partial last page) | 253--255 | 20.1.1--20.1.9 |
| `sec202.tex` | 20.2 Momentum Flow | 278 (from heading)--285 | 255--262 | 20.2.1--20.2.20 |
| `sec203.tex` | 20.3 Renormalization Group Equations for Coefficient Functions | 286--288 (partial last page) | 263--265 | 20.3.1--20.3.10 |
| `sec204.tex` | 20.4 Symmetry Properties of Coefficient Functions | 288 (from heading)--289 (partial last page) | 265--266 | 20.4.1--20.4.8 |
| `sec205.tex` | 20.5 Spectral Function Sum Rules | 289 (from heading)--295 (partial last page) | 266--272 | 20.5.1--20.5.19 |
| `sec206.tex` | 20.6 Deep Inelastic Scattering | 295 (from heading)--306 (partial last page) | 272--283 | 20.6.1--20.6.60 |
| `sec207.tex` | 20.7 Renormalons | 306 (from heading)--311 (partial last page) | 283--288 | 20.7.1--20.7.22 |
| `appendix.tex` | Appendix: Momentum Flow: The General Case | 311 (from heading)--315 (partial last page) | 288--292 | 20.A.1--20.A.12 |
| `backmatter.tex` | Problems and References | 315 (from Problems heading)--317 | 292--294 | none |

Every numbered equation has an explicit tag and matching stable label. The
complete inventory is 160 equations, and every section sequence is
consecutive.

## Required inventories

- Figures: Figures 20.1 and 20.2 in Section 20.2, and Figure 20.3 in
  Section 20.7. All three are faithful TikZ reconstructions with complete
  captions. Numbered tables: zero.
- Semantic footnotes: 15: 13 ordinary `\footnote` calls and two
  optional-reading title notes implemented with automatic
  `\footnotemark`/`\footnotetext` pairing.
- Centered three-asterisk dividers: zero.
- Problems: five.
- References: 22, numbered 1--22. Every entry has a stable `ch20-ref-*`
  destination, and every source paper-reference marker is linked.

## Shared transition pages

Semantic ownership is by heading. The preceding section owns all material
above each heading on physical pages 276, 278, 288, 289, 295, 306, 311, and
315. In particular, Section 20.6 owns its continuation at the top of physical
page 306; Section 20.7 starts at the heading later on that page and owns its
continuation through the appendix heading on physical page 311; the appendix
owns its continuation above the Problems heading on physical page 315. The
source-page join from physical pages 285 to 286 contains no omitted material.
Every adjacent source-page join from 275/276 through 316/317 was reviewed
exactly once.

## Verification record

- Four non-overlapping worker assignments compiled and rendered their ranges
  in isolation. Every isolated output page was compared with the
  corresponding source renders; correction pages were recompiled, rerendered,
  and reinspected.
- Static integration checks found exactly 160 unique equation tags and 160
  matching equation labels, three unique figure labels, 15 semantic
  footnotes, five problem items, and 22 reference items. There are no
  duplicate labels, missing internal targets, scaffold markers, or unresolved
  transcription notes.
- The integrated chapter check compiles to 38 A4 pages. Check-only
  destinations represent the legitimate links into Chapters 5, 8, 10, 17,
  18, and 19, so the chapter-only PDF contains no unresolved references. The
  final log has no LaTeX errors, undefined links, duplicate destinations, or
  underfull boxes. Six bounded overfull-box warnings (0.70--10.99 pt) occur in
  prose containing long mathematical expressions or citation groups; all six
  locations were inspected at full resolution and have no clipping or
  collision.
- All 38 integrated pages were rendered with Poppler and inspected in two
  complete contact sheets. Full-resolution checks covered every section
  boundary, all figures, dense mathematics and long footnotes, the complete
  corrected appendix, the Problems/References transition, and the final
  reference page. No clipping, overlap, malformed glyph, equation-tag
  collision, blank-content loss, or misplaced figure remains.
- Final full-volume integration and export are deferred until Chapters
  21--23 and the indexes are complete.

Source anomalies were preserved rather than silently corrected. These include
“renormalization group expansions” in the introduction, “external lines” in
the Figure 20.1 caption, the ordering printed in Eq. 20.2.18, “a Greens
function” in Section 20.3, the equality `F=F_\pi=184\,\mathrm{MeV}` in
Section 20.5, “yielding a electron” and the other reported grammatical or
notation irregularities in Section 20.6, the positive exponential signs in
Eqs. 20.7.18--20.7.19, the year 1972 in Reference 15, and the
vacuum-to-vacuum summands printed in Problem 2.
