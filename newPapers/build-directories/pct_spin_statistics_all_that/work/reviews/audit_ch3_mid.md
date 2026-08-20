# Chapter 3, Section 3-3 audit

Scope: PDF pages 118--128, printed pages 106--116, against
`latex/chapters/chapter03/sec3_3.tex`.

The canonical source is `origPapers/pct_spin_statistics_all_that.pdf`, with
SHA-256
`44fadba731cafe7f009d4e561372febb3597e1f2a4819346ce2efd16befcb889`.
I inspected each rendered source image in `work/source-pages/`, checked the
transcription in printed order, and compiled the section in a standalone
article wrapper.

## Page ledger

| PDF page | Printed page | Native coverage checked |
| --- | --- | --- |
| 118 | 106 | Opening paragraph, section 3-3 heading, (3-19)--(3-23), the tensor-component prose, and the product decomposition of (f_J). |
| 119 | 107 | Completion of the (f_J) approximation, (3-24), the norm argument, the definition on (D_1), the domain statement, and (3-25)--(3-26), including the Section 2-6 footnote. |
| 120 | 108 | Proof of the relativistic transformation law, Theorem 3-2, (3-27)--(3-33), and the spectral and hermiticity statements. Minkowski Fourier phases follow the house mostly-plus conversion. |
| 121 | 109 | (3-34), the translation-invariance Fourier calculation, the three spectral-support displays, and the test-function proof of (c) and (d). |
| 122 | 110 | Completion of the proof, Theorem 3-3, (3-35)--(3-36), the positive-definiteness proof, and the printed footnote on p. 121. |
| 123 | 111 | Theorem 3-4, (3-37), the unnumbered Remark, and the opening of the cluster-decomposition proof through (F_1) and (F_2). |
| 124 | 112 | Polynomial bounds, the Euclidean (R)-norm, the spacelike separation estimate, the (R_0) choice, and the polar-coordinate estimate. The old mostly-minus quadratic form is converted to the house mostly-plus form. |
| 125 | 113 | The inverse-power limit, the spectral cutoff argument, the physical interpretation, (3-38), (3-39), and the definitions of (F) and (J). |
| 126 | 114 | The symmetry continuation, Theorem 3-5, the tube boundary-value statement, its footnote, and the Laplace-transform proof. |
| 127 | 115 | The complex Lorentz continuation, the (Lambda=-1) relation (3-40), Theorem 3-6, and the start of its edge-of-the-wedge proof. |
| 128 | 116 | Completion of the edge-of-the-wedge proof, the Figure 2-4 reference, the free-field expectation values, the mass-shell formulas, (3-41), and the source's incomplete final sentence. |

The source markers cover all eleven pages. Their counts are 16, 13, 16, 15,
13, 9, 14, 12, 12, 12, and 13 from PDF 118 through PDF 128. The final
sentence stops after “we can”, exactly where the source page ends.

## Fidelity decisions

The scalar-product tuples are rendered in Dirac order. The vacuum vector is
written as `\(\ket{\Omega}\)` throughout this section. Hermitian-conjugate
fields use `\(\dagger\)` in the scalar-product and hermiticity statements.
The componentwise stars in charge-conjugation and antiunitary formulas remain
stars. The source's script W symbols are rendered as `\(\mathcal W\)` and
the source Schwartz symbols as `\(\mathcal S\)`.

The source Fourier phases use the old mostly-minus contraction. Equations
(3-29), (3-30), and the translation-invariance calculation therefore use the
converted negative phase. The three spectral-support integrals use the same
conversion. The Laplace proof uses the corresponding positive phase. The
free-field mass shell is `\(p^2=-m^2\)`, so the source deltas become
`\(\delta(p^2+m^2)\)` and the source `\(\exp(-\ii p\cdot_{m src}x)\)`
becomes `\(\exp(+\ii p\cdot x)\)`.

The cluster proof's source choice (a^2=-1) becomes (a^2=1), the
mass-gap support condition becomes (P^2\leq -M^2), and the separation
estimate is negated with its inequality direction reversed. The resulting
bound is positive in the mostly-plus metric, which is the condition needed
for the spacelike locality argument.

The printed Remark is unnumbered. A local `pctremark` environment keeps it
out of the theorem counter, and the local proof setting produces one solid
QED square per proof. Long displays were split with aligned rows where the
source line would exceed the JHEP text width. Their factors and order are
unchanged.

## Build evidence

`python3 scripts/audit_source.py` passed with 36/36 native chunks and 211
distinct marked PDF pages. `python3 scripts/audit_notation.py` reported no
definite notation regressions. A standalone `pdflatex` run on this section
completed with return code 0 and produced a 12-page PDF. The full draft build
also entered and compiled `sec3_3.tex`; its later failure occurred in a
different Chapter 4 file. The source comparison and standalone rendering
cover every page assigned to this review.

Unresolved blockers: none
