# Independent audit: Chapter 3 opening, Sections 3-1 and 3-2

Source packet: PDF pages 108--117, printed pages 96--105 of
`origPapers/pct_spin_statistics_all_that.pdf`.

Transcription files checked:

- `latex/chapters/chapter03/opening.tex`
- `latex/chapters/chapter03/sec3_1.tex`
- `latex/chapters/chapter03/sec3_2.tex`

The source pages were inspected from the stored 180 dpi renders and from
600 dpi crops of the small formulas, footnotes, and page-boundary material.
Every paragraph was read against the source image in order. The equation
labels, axiom labels, examples, citations, and two dagger footnotes were
checked separately.

## Page disposition

| PDF | Printed | Reviewed material |
| ---: | ---: | --- |
| 108 | 96 | Chapter 3 title, Carroll epigraph, opening discussion, start of Section 3-1 |
| 109 | 97 | Opening continuation, axiom O, the representation map, (3-1), vacuum paragraph |
| 110 | 98 | Axiom I, dagger footnote, (3-2), (3-3), domain discussion |
| 111 | 99 | Domain continuation, axiom II, (3-4), (3-5), three field examples |
| 112 | 100 | Axiom III, (3-6), adjoint locality, unsmeared locality, canonical relation (3-7) |
| 113 | 101 | (3-7) discussion, irreducibility, (3-8), field-theory definition, dagger footnote |
| 114 | 102 | Cyclicity continuation, proof, axiom IV, asymptotic completeness, Section 3-2 opening |
| 115 | 103 | Free-field Hilbert direct sum, (3-9)--(3-14) |
| 116 | 104 | (3-15)--(3-18), Wick-polynomial construction |
| 117 | 105 | Wick-polynomial conclusion, generalized free fields, independence remarks, time-slice axiom |

The continuation at the top of PDF 114 is part of Section 3-1 and is now
marked in `sec3_1.tex` before the Section 3-2 heading. The Section 3-2
heading and its opening sentence retain their PDF 114 marker in `sec3_2.tex`.

## Formula and result inventory

The packet contains the unnumbered representation map in axiom O, equations
(3-1)--(3-8), the axiom-IV display
`\Hilbert=\Hilbert^{\mathrm{in}}=\Hilbert^{\mathrm{out}}`, and equations
(3-9)--(3-18). The field examples on PDF 111 and the adjoint-locality,
unsmeared-locality, and spin-zero displays on PDF 112 remain unnumbered as in
the source. The proof after the definition on PDF 114 carries every source
step through the asymptotic-completeness discussion.

Equation (3-8) retains the source's matrix-element order after conversion:
`\bra{\Phi}B\varphi_j(f)\ket{\Psi}` equals
`\bra{\varphi_j(f)^\dagger\Phi}B\ket{\Psi}`. Equations (3-13)--(3-17)
retain all particle labels, spinor indices, products, limits, subtraction
terms, and source order.

## Notation audit

- Hilbert-space vectors and matrix elements use Dirac notation. The state
  vectors in (3-1), (3-2), the definition, the cyclicity proof, and the
  domain paragraph in Section 3-2 are kets. Scalar products in (3-8) and
  (3-11)--(3-13) use the project bra-ket macros.
- Operator stars in the source are represented as `^\dagger` for field
  adjoints. The field relation involving the conjugated test function keeps
  `\overline{g}` and the source's operator order.
- Spatial arguments in the prose and canonical relation use the project
  spatial-vector convention. `\mathcal{S}`, `\mathcal{H}`, and the polynomial
  subspace `\mathcal{P}\ket{\Psi}` follow the Weinberg-oriented script-letter
  convention.
- The house metric is mostly plus. The mass shell in axiom O and in the
  free-field domain is written `-m^2`. The source complement condition for
  spacelike support, `(x-y)^2\geq0`, becomes `(x-y)^2\leq0`; the unsmeared
  locality condition `(x-y)^2<0` becomes `(x-y)^2>0`. The large-distance
  condition in Section 3-2 is written `(x-y)^2>\ell^2`.
- The source translation phase in axiom O is written with the house-sign
  convention as `\exp(-\ii P^\mu a_\mu)`. The source Fourier phase in (3-15)
  becomes `\ee^{+\ii p\cdot x}`. The source phase in (3-16) becomes
  `\exp[-\ii(\sum_jp_j)\cdot a]`. These are formula-level conversions under
  the metric contract.

## Footnotes, citations, and continuity

PDF 110 carries the source dagger footnote “Defined in Section 2-6.” PDF 113
carries “This idea was introduced in Ref. 5.” Both are present at their source
positions. The references to Section 2-1, Section 2-6, Section 3-2, Section
4-2, Ref. 4, Ref. 5, Ref. 15, Ref. 20 of the Chapter 2 bibliography, Ref. 25
of Chapter II, and the original papers and Jost's book are present in the
same reading order.

The opening paragraph continues from PDF 108 into PDF 109. The definition
and irreducibility discussion continues from PDF 113 into PDF 114. Equation
(3-14) continues into the PDF 116 explanation of the hat convention. The
Wick-polynomial construction and (3-18) finish on PDF 116, with its
consequences continuing on PDF 117.

## Build check

The project draft compile entered all three audited files and passed through
the added PDF 114 continuation and the phase-converted equations. The run
later stopped in the separately assigned Chapter 4 Section 4-1 file at its
existing line 262 error. The source hash and page-count audit passed for the
canonical 221-page source. The packet has no figures.

Unresolved blockers: none
