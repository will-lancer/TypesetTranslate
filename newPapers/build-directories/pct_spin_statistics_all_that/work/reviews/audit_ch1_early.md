# Independent fidelity audit: Chapter 1, pages 4--8

## Scope

This independent pass covers physical PDF pages 016--020, printed pages 4--8,
against:

- `latex/chapters/chapter01/opening.tex`
- `latex/chapters/chapter01/sec1_1.tex`
- `latex/chapters/chapter01/sec1_2.tex`

The page images in `work/source-pages/pdf-016.jpg` through
`pdf-020.jpg` were inspected at the stored original render. OCR was used as a
locator only. The scan controls every word, punctuation mark, mathematical
glyph, display, footnote, printed result number, and page-boundary decision.

## Page ledger

| PDF | Printed page | Checked material | Result |
|---:|---:|---|---|
| 016 | 4 | Chapter 1 title, Wigner epigraph, Heisenberg-picture opening, transition probability, unit-ray definition, state footnote | pass |
| 017 | 5 | Section 1-1 opening through the projection-operator footnote and the sentence ending “commute with all the” | pass |
| 018 | 6 | Commutant continuation, coherent subspaces, complete commuting set, realizability assumption, Dirac-terminology footnote | pass |
| 019 | 7 | Closing paragraph of Section 1-1, Section 1-2, (1-1), symmetry discussion, Theorem 1-1 and (1-2) | pass |
| 020 | 8 | Theorem 1-1 continuation, linearity displays, parity examples, (1-3), final sentence boundary | pass |

## Fidelity checks

Page 016 preserves the epigraph wording, the distinction between the
Schrödinger, Heisenberg, and interaction pictures, the Hilbert-space
description, the transition-probability display, the unit-ray set, the norm
definition, and the pure/mixed-state footnote. The prose ends at “unit rays”
as in the scan.

Page 017 preserves the charge, baryon, and univalence discussion, including
the signs in the (2\pi) rotation argument, the (Q,B,(-1)^F) eigenvalue
conditions, the (x)- and (z)-component examples, the definition of a
super-selection rule, the bounded-operator inequality, and the projection
operator footnote. The source sentence is intentionally continued on PDF
018.

Page 018 preserves the commutant definition and notation, the identity
operator conclusion, the coherent-subspace characterization, the complete
commuting-set argument, the infinite-energy example, the mathematical-
convenience qualification, and the maximal-Abelian-set footnote.

Page 019 preserves the experiment-dependent qualification, the Section 1-2
heading, the transition-probability equality (1-1), the one-to-one mapping
discussion, the unitary and anti-unitary examples, the CPT operator, Ref. 1,
Theorem 1-1, and equation (1-2). The theorem's invariant and moved coherent
subspace cases remain separate statements in source order.

Page 020 preserves the theorem explanation, both unnumbered linearity tests,
the “one or the other, not both!” wording, the spinless-particle parity
example, equation (1-3), the exchanged-particle transformation, the two
center-of-mass displays, and the sentence ending “observables of”. The
continuation is left to the next source packet.

## Notation audit

The source Hilbert-space vectors and scalar products are converted to the
authorized Dirac forms `\ket{...}`, `\bra{...}`, and `\braket{...}{...}`.
The projection formula retains the source factor order and normalization
factor. The norm remains attached to the ket. The anti-unitary identity is
written as
`\braket{\Theta\Phi}{\Theta\Psi}=\overline{\braket{\Phi}{\Psi}}`,
the contracted Dirac form required by `NOTATION.md`.

The source script Hilbert space is `\mathcal H`; the observable set and its
commutant are `\theta` and `\theta'`; the identity operator is `\mathbf{1}`.
The source `CPT` label is rendered upright as `\mathrm{CPT}`. These choices
preserve the source roles while following the project notation contract.

The printed equation tags `(1-1)`, `(1-2)`, and `(1-3)` are present exactly
once. The two linearity displays on printed page 8 remain unnumbered. The
JHEP section commands supply the modern structural heading treatment while
the source markers retain the printed chapter and section identities.

## Source markers and boundaries

Every substantive unit in the three assigned files carries a marker for its
physical PDF page and printed folio. The PDF 017 sentence fragment is joined
to its PDF 018 continuation. The PDF 020 final fragment remains open for the
next packet. No scan page, footnote, equation, or theorem statement is
duplicated or omitted within this packet.

## Corrections made

No content correction was required. The assigned transcription already agrees
with the source at the word, equation, number, footnote, punctuation, and
authorized notation levels.

Unresolved blockers: none
