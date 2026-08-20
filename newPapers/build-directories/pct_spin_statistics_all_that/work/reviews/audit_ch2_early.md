# Chapter 2 early-range fidelity audit

Scope: physical PDF pages 43--58, printed pages 31--46. The audit covers
`opening.tex`, `sec2_1.tex`, and `sec2_2.tex`. I inspected the rendered source
JPEG for every page, then checked every source paragraph, displayed formula,
footnote, heading, result boundary, proof boundary, and printed equation tag
against the native files.

## Page evidence

- PDF 43, print 31: chapter opening, Jost epigraph, and the start of
  Section 2-1. The delta-function definition is present as (2-1), followed
  by the definition of a test function.
- PDF 44, print 32: linear-functional definition (2-2), function realization
  (2-3), support discussion, and the support/supremum footnote are present.
- PDF 45, print 33: the Schwartz-space definition, Euclidean norm, multi-index
  formulas (2-4)--(2-7), and the convergence statement are present.
- PDF 46, print 34: tempered-distribution continuity (2-8)--(2-12), the
  bounded representation (2-11), and its polynomial bound are present.
- PDF 47, print 35: representation (2-13), the finite-order discussion, the
  definition of \(\mathcal D'\), the compact-support footnote, and the example
  \(T(x)=\sum_{n\geq0}\delta^{(n)}(x-n)\) are present.
- PDF 48, print 36: convergence of distributions, the three topological-vector
  space remarks, and the bounded-set transition are present.
- PDF 49, print 37: the bounded-set continuation, local test-function spaces,
  the “Miscellaneous Properties of Distributions” subheading, and formulas
  (2-14)--(2-16) are present.
- PDF 50, print 38: formula (2-17), the translation derivative computation,
  the affine action \(\{a,L\}\), its distributional action, composition, and
  invariance formulas are present.
- PDF 51, print 39: translation invariance (2-18), center/difference
  coordinates (2-19), transformed invariance (2-20), derivative condition
  (2-21), and the test-function construction (2-22)--(2-23) are present.
- PDF 52, print 40: formulas (2-24)--(2-26), the multiplication-by-a-function
  discussion, fast-decrease distributions, and the tensor-product definition
  are present.
- PDF 53, print 41: tensor product (2-27)--(2-28), convolution
  (2-29)--(2-31), and the successive-integral computation are present.
- PDF 54, print 42: the second tensor-product form, regularization argument,
  the Schwartz Nuclear Theorem heading, and multilinearity formula (2-32) are
  present.
- PDF 55, print 43: the continuation of the nuclear-theorem discussion, the
  complete printed Theorem 2-1 statement and example, followed by Section 2-2
  and Fourier definitions (2-33)--(2-34), are present.
- PDF 56, print 44: Fourier derivative and multiplication rules
  (2-35)--(2-36), continuity estimate (2-37), the inversion lemma and (2-38),
  the start of its proof, and delta identity (2-40) are present.
- PDF 57, print 45: Gaussian regularization (2-41)--(2-43), the estimate,
  Parseval identity (2-44), pairing (2-45), and distributional definition
  (2-46) are present.
- PDF 58, print 46: continuity of the distributional transform, (2-47),
  Theorem 2-2 and (2-48), its proof, and the closing prose are present.

## Corrections made

The source-page comparison found two transcription defects. The continuation
of the nuclear-theorem section had stopped after “of a sufficiently”; I added
the missing PDF 55 text, theorem statement, displayed representation, example,
and evaluation formulas. Equation (2-35) used \(r\) where the source uses the
multi-index \(k\); the native formula now uses \(D^k\) and \((\pm ip)^k\).
The native theorem counter is advanced at the manually typeset Theorem 2-1 so
that the following environment prints and labels Theorem 2-2. A fresh draft
LaTeX run reached the end of both audited files, and the auxiliary file records
`thm:ch2-nuclear` as 2-1, `thm:ch2-fourier-distribution-inverse` as 2-2, and
the first theorem in Section 2-3 as 2-3.

## Notation checks

The source script alphabets for Schwartz/test-function spaces and Fourier maps
are rendered with the house `\mathcal` forms. The source mostly-minus metric
statement is represented with the project’s recorded house metric in the
Minkowski scalar-product display. The Fourier phases, Euclidean Gaussian
factors, hats, delta derivatives, and all printed equation numbers were checked
at formula level. This range contains no Hilbert-space state vectors or
in/out labels requiring Dirac delimiters.

## Marker and build checks

Every substantive unit in the assigned files has a `% PCT-SOURCE` marker with
physical PDF page and printed folio. The source audit reports no forbidden
source import or placeholder in these files. The draft compilation processed
pages through `sec2_2.tex` without an error; the run later stopped in an
unassigned Chapter 4 file. The remaining overfull boxes reported by that run
are outside this packet except for the pre-existing Chapter 2 paragraph at
`sec2_1.tex` lines 685--689, which contains the long source equation sentence
and requires layout review in the project-wide pass.

Unresolved blockers: none
