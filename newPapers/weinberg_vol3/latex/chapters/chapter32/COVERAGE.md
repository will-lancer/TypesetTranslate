# Chapter 32 coverage manifest

## Source boundary

- Chapter: 32, *Supersymmetry Algebras in Higher Dimensions*
- Source: `origPapers/weiberg_vol3.pdf`
- Physical PDF pages: 405--433 inclusive
- Printed pages: 382--410
- References end on physical p. 432 (printed p. 409)
- Physical p. 433 (printed p. 410) is intentionally blank
- The Author Index begins on physical p. 434 and is excluded

Rendered source pages are authoritative. OCR and the PDF text layer are
only aids.

## Semantic ownership

| File | Content | Physical pages | Printed pages |
|---|---|---:|---:|
| `introduction.tex` | Chapter introduction before 32.1 | 405 | 382 |
| `sec321.tex` | 32.1 General Supersymmetry Algebras | 405--416 | 382--393 |
| `sec322.tex` | 32.2 Massless Multiplets | 416--420 | 393--397 |
| `sec323.tex` | 32.3 \(p\)-Branes | 420--424 | 397--401 |
| `appendix.tex` | Appendix, “Spinors in Higher Dimensions” | 424--430 | 401--407 |
| `backmatter.tex` | Problems and References | 430--432 | 407--409 |

The physical pages at every row boundary are read-only overlaps for
neighboring assignments. Text is owned by the visible heading boundary
and must occur exactly once. The type-II/heterotic discussion at the
top of physical p. 420 belongs to section 32.2, and section 32.3 begins
at its heading later on the page. The discussion of two-brane and
five-brane sources at the top of physical p. 424 belongs to section
32.3; the appendix begins at its heading below. The first two
paragraphs on physical p. 430 close the appendix before Problems begin.

## Expected numbered-equation coverage

- Section 32.1: (32.1.1)--(32.1.54)
- Section 32.2: (32.2.1)
- Section 32.3: (32.3.1)--(32.3.9)
- Appendix: (32.A.1)--(32.A.45)

Expected total: 109 numbered equations, including the appendix. Every
unnumbered display and every dimension-by-dimension classification
line must be inventoried during visual transcription.

## Expected inventories

- Numbered figures: none
- Numbered tables: none
- Problems: 1--4 on physical p. 430
- References: base References 1--13 plus lettered References 6a and
  6b on physical pp. 430--432, for 15 displayed entries
- Source footnotes: two, both converted to ordinary automatically
  numbered footnotes:
  - physical p. 421: proof that the displayed \(p\)-brane integral is
    topologically invariant;
  - physical p. 427: qualification concerning a Lorentz-algebra
    representation, its complex-conjugate representation, and the
    local form of group elements near the identity.
- Centered three-asterisk dividers: none

The all-page source render contains no numbered or unnumbered
diagrammatic figures and no tables. Physical p. 433 contains no printed
material and must not be mistaken for a dropped reference page.

## Appendix structure

The appendix remains one chapter-local file but preserves its two
unnumbered internal headings:

- “Even Dimensions: \(d=2n\)” begins on physical p. 424;
- “Odd Dimensions: \(d=2n+1\)” begins on physical p. 428.

## Continuity and high-risk checks

- Check every transition page listed in the ownership table,
  especially physical pp. 405, 416, 420, 424, and 430, and verify the
  References/blank-page/Author-Index boundary at pp. 432--434.
- Preserve the source's mostly-plus metric, index ordering,
  \(O(d-1,1)\) versus \(O(d)\) distinction, Hermitian-adjoint,
  transpose, and complex-conjugation operations, and all reality,
  pseudoreality, chirality, and mod-eight cases.
- Verify every graded commutator and anticommutator, super-Jacobi
  identity, spinor-representation index, momentum and tensor central
  charge, charge-conjugation matrix, automorphism group, and symmetry
  condition on \(g_{rs}\) and \(z_{rs}\).
- Preserve the separate classifications for even and odd dimensions,
  all \(N_\pm\) conditions, \(U(N)\), \(O(N)\), and \(USp(N)\)
  automorphism groups, and every symmetric/antisymmetric qualification.
- In section 32.2, check all little-group representations, state-count
  binomial coefficients, maximum-spin arguments, chirality choices,
  and the type IIA, type IIB, heterotic, and eleven-dimensional
  multiplet component counts.
- In section 32.3, preserve the rank and duality of every
  antisymmetric tensor charge, the topological integral and its
  footnote proof, transpose symmetries of antisymmetrized gamma
  products, the \(d=11\) count \(528\), and the two-brane/five-brane
  source discussion.
- In the appendix, verify every explicit tensor-product gamma matrix,
  occupation-number basis, chirality matrix, Lorentz generator,
  similarity transformation, charge-conjugation matrix, parity and
  reality condition, antisymmetric gamma product, binomial identity,
  and Cartan-subalgebra eigenvalue.
- OCR or the PDF text layer missed the visible labels (32.1.23),
  (32.1.24), (32.1.34), (32.1.35), (32.1.44), (32.A.9), and
  (32.A.40). Inspect the rendered source rather than inferring these
  equations from neighboring text.
- Every superscript source citation becomes a linked bracketed marker;
  none may be confused with the two source footnotes.

## Progress record

- The complete physical-page range 405--433 has been rendered at 120
  dpi and inspected in two all-page contact sheets. Section, appendix,
  Problems, References, equation-range, footnote, divider, figure,
  table, and blank-page inventories above were checked against the
  rendered pages.
- `backmatter.tex` now covers all four Problems and all 15 displayed
  References (1--13 plus 6a and 6b) on physical pp. 430--432.
  `checks/chapter32-backmatter.tex` compiles to three A4 pages with no
  unresolved references, errors, or box warnings; all three rendered
  pages were inspected at full resolution. Source-visible anomalies
  retained there include “Aitkens,” “similiar,” “Gueven,” and the
  missing comma after Townsend in Reference 10.
- The introduction, sections 32.1--32.3, and appendix remain to be
  transcribed.
