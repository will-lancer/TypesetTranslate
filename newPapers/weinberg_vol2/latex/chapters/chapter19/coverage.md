# Chapter 19 coverage manifest

Source: `origPapers/weinberg_vol2.pdf`, physical PDF pages 186--274
inclusive, printed pages 163--251. Chapter 19 starts on physical page 186;
Chapter 20 starts on physical page 275 and is excluded. Fresh rendered pages,
not OCR, were authoritative throughout transcription and review.

## Semantic ownership and numbered equations

| File | Material | Physical pages | Printed pages | Numbered equations |
|---|---|---:|---:|---|
| `introduction.tex` | Chapter introduction | 186 | 163 | none |
| `sec191.tex` | 19.1 The Goldstone Theorem | 186--190 (partial last page) | 163--167 | 19.1.1--19.1.9 |
| `sec192.tex` | 19.2 Goldstone Bosons | 190 (from heading)--200 (partial last page) | 167--177 | 19.2.1--19.2.56 |
| `sec193.tex` | 19.3 Spontaneously Broken Approximate Symmetries | 200 (from heading)--205 (partial last page) | 177--182 | 19.3.1--19.3.20 |
| `sec194.tex` | 19.4 Pions as Goldstone Bosons | 205 (from heading)--214 | 182--191 | 19.4.1--19.4.51 |
| `sec195.tex` | 19.5 Effective Field Theories: Pions and Nucleons | 215--234 (partial last page) | 192--211 | 19.5.1--19.5.71 |
| `sec196.tex` | 19.6 Effective Field Theories: General Broken Symmetries | 234 (from heading)--248 (partial last page) | 211--225 | 19.6.1--19.6.47 |
| `sec197.tex` | 19.7 Effective Field Theories: SU(3) · SU(3) | 248 (from heading)--257 (partial last page) | 225--234 | 19.7.1--19.7.32 |
| `sec198.tex` | 19.8 Anomalous Terms in Effective Field Theories | 257 (from heading)--261 (partial last page) | 234--238 | 19.8.1--19.8.11 |
| `sec199.tex` | 19.9 Unbroken Symmetries | 261 (from heading)--266 (partial last page) | 238--243 | 19.9.1--19.9.14 |
| `sec1910.tex` | 19.10 The U(1) Problem | 266 (from heading)--269 (partial last page) | 243--246 | 19.10.1--19.10.12 |
| `backmatter.tex` | Problems and References | 269 (from Problems heading)--274 | 246--251 | none |

Every numbered equation has an explicit tag and stable label. The complete
inventory is 323 equations, and every section sequence is consecutive.

## Required inventories

- Figures: Figure 19.1 and Figure 19.2 in Section 19.2, and the three-panel
  Figure 19.3 in Section 19.5. All three are faithful TikZ reconstructions
  with complete captions. Numbered tables: zero.
- Ordinary automatic footnotes: 25, including the optional-reading title
  note in Section 19.8.
- Centered three-asterisk dividers: four, in Sections 19.4--19.7.
- Problems: six.
- References: 56 displayed entries: 1--52 plus 30a, 32a, 38a, and 38b.
  Every displayed entry has a stable `ch19-ref-*` destination, and every
  source paper-reference marker is linked.

## Shared transition pages

Semantic ownership is by heading. The preceding section owns all material
above each heading on physical pages 190, 200, 205, 234, 248, 257, 261, 266,
and 269. In particular, Section 19.5 owns its continuation at the top of
physical page 234, and Section 19.10 owns its closing prose and footnote above
the Problems heading on physical page 269. Every adjacent source-page join
from 186/187 through 273/274 was reviewed exactly once.

## Verification record

- Six non-overlapping worker assignments compiled and rendered in isolation.
  Every isolated output page was compared with the corresponding source
  renders; correction pages were recompiled, rerendered, and reinspected.
- Static integration checks found exactly 323 unique equation tags and 323
  matching equation labels, three unique figure labels, 25 footnotes, six
  problem items, and 56 reference items. There are no duplicate labels,
  missing internal targets, scaffold markers, or unresolved transcription
  notes.
- The integrated chapter check compiles cleanly to 78 A4 pages. Check-only
  destinations represent the two legitimate links into Chapters 15 and 18,
  so the chapter-only PDF contains no unresolved references. The final log
  has no LaTeX errors, undefined links, duplicate destinations, overfull
  boxes, or underfull boxes.
- All 78 integrated pages were rendered with Poppler and inspected in four
  complete contact sheets. Full-resolution checks covered every section
  boundary, all figures, dense mathematics and long footnotes, the
  Problems/References transition, and the final reference page. No clipping,
  overlap, malformed glyph, equation-tag collision, blank-content loss, or
  misplaced figure remains.
- The volume-wide notation audit normalized all residual product glyphs to
  `\cdot` and all 54 residual script glyphs in Section 19.6 to `\mathcal`.
  The chapter was rebuilt cleanly, and integrated pages 17--54 were
  rerendered and reinspected without changing the page count.
- Final full-volume integration and export are deferred until Chapters
  20--23 and the indexes are complete.

Source anomalies were preserved rather than silently corrected. These include
the swapped reflexive/symmetric glosses in Section 19.6, the visibly reversed
range `0 >= s >= 1` and “external derivative” wording in Section 19.8, the
Section 19.9 expectation-value reference mismatch and omitted differential in
its long footnote, the scalar/pseudoscalar and decay-constant-ratio
inconsistencies in the final Section 19.10 footnote, the year printed in
Reference 11, and the unusual `hep-ph/-9602366` identifier in Reference 38a.
