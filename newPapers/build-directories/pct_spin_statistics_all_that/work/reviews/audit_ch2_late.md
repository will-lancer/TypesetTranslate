# Independent audit: Chapter 2, Section 2-6 and bibliography

Source packet: physical PDF pages 96--107, printed pages 84--95, from the
frozen source
`origPapers/pct_spin_statistics_all_that.pdf`.

The audit used the 180 dpi source renders in `work/source-pages/` and read the
native files in source order. Every paragraph, displayed formula, printed
equation tag, proof line, footnote, citation, and bibliography entry was
checked against the scan.

## Files checked

- `latex/chapters/chapter02/sec2_6.tex`
- `latex/chapters/chapter02/bibliography.tex`

## Corrections made during this pass

- Restored the missing backslashes in `\mathcal{D}'(E)` and
  `\mathcal{B}` on physical page 96.
- Added a physical-page-98 marker after the printed line ending
  “separable Hilbert” and a physical-page-103 marker before “vectors, but”
  in the common-domain sentence. These markers preserve the two source
  boundaries inside reflowed prose.
- Applied the Weinberg mostly-plus phase rule from `NOTATION.md`. The source
  phases `e^{-i p\cdot_{\rm src}a}`, `e^{+i Q\cdot_{\rm src}a}`, and
  `e^{+i p\cdot_{\rm src}a}` appear as `e^{+i p\cdot a}`,
  `e^{-i Q\cdot a}`, and `e^{-i p\cdot a}`. The Fourier inverse now carries
  the corresponding positive phase.
- Replaced the project wrapper with an explicit native
  `thebibliography` environment of width 25. The visible numbering 1--25 and
  every bibliography datum remain in source order.

## Page-by-page result

- PDF 96 / print 84: Theorem 2-17 continuation and proof, Section 2-6
  heading, Hilbert-space definition, real-Hilbert-space footnote, equations
  (2-111) and (2-112), and the Cauchy completeness display match the scan.
  Dirac products and kets follow the house contract.
- PDF 97 / print 85: Separability discussion, the `L^2(\mathbb{R}^n)`
  example, the two-line schematic, and the direct-sum opening match. The
  source line ending is marked at the physical-page boundary.
- PDF 98 / print 86: Direct-sum norm and product, sequence description,
  multiparticle direct sum, collision-state bracket, and infinite-tensor-
  product discussion match.
- PDF 99 / print 87: Separable subspace, statistical-mechanics example,
  operator definition, graph, linearity display, closure, and extension
  criterion match.
- PDF 100 / print 88: Orthogonal-complement discussion, both graph
  conditions, adjoint definition, minimal closed extension, hermitian and
  self-adjoint distinctions, and the hermitian condition match.
- PDF 101 / print 89: Boundedness definition, inequality, scaling argument,
  extension construction, closed graph theorem paragraph, and unbounded
  operator discussion match.
- PDF 102 / print 90: Hilbert-space pathology, the domain-intersection
  display, and the common-domain paragraph through the printed word “such”
  match.
- PDF 103 / print 91: The common-domain continuation, translation
  representations, equations (2-113) and (2-114), intermediate-state
  expansion, Fourier calculation, translation eigenvalue relation, and the
  direct-integral qualification match.
- PDF 104 / print 92: SNAG integral, projection-measure identities,
  `E(\mathbb{R}^4)=\mathbf{1}`, spectral-support criterion, Fourier inverse,
  matrix-element criterion, and discrete-spectrum argument match.
- PDF 105 / print 93: Bibliography heading, items 1--11, and the Bargmann
  note match. The printed names, titles, journal data, page data, years, and
  prose introductions were retained.
- PDF 106 / print 94: Items 12--19, the Vladimirov note, Dyson note, and
  Borchers--Glaser note match, including the source's printed “follows' their
  method” punctuation.
- PDF 107 / print 95: Items 20--25 match, including the SNAG expansion,
  accented book titles, page references, and final Section 116 reference.

## Structural checks

The section has 63 source markers covering every physical page 96--104. The
bibliography has 50 markers covering every physical page 105--107. The four
printed equation tags (2-111)--(2-114) remain explicit. The bibliography has
25 `\bibitem` entries inside the native environment. No placeholder or
facsimile-import text occurs in either assigned file.

Unresolved blockers: none
