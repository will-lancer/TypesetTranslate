# Chapter 1 late-page audit

## Scope and authority

- Canonical source: `origPapers/pct_spin_statistics_all_that.pdf`.
- Source digest: `44fadba731cafe7f009d4e561372febb3597e1f2a4819346ce2efd16befcb889`.
- Audited physical pages: PDF 021--041.
- Printed folios: 9--29.
- Assigned native files: `latex/chapters/chapter01/sec1_3.tex`, `latex/chapters/chapter01/sec1_4.tex`, and `latex/figures/fig1_1.tex` through `fig1_3.tex`.
- Contract and notation rules: `TRANSCRIPTION_CONTRACT.md` and `NOTATION.md` read before review.
- Comparison surface: all twenty-one source JPEGs, OCR used as a second text pass, and rendered native pages containing the audited sections and figures.

## Page pass record

| Source page | Printed page | Native units checked |
|---|---:|---|
| PDF 021 | 9 | Section 1-3 opening, (1-4)--(1-6), mostly-plus scalar product, metric matrix, Lorentz condition, inverse and group law. |
| PDF 022 | 10 | Component classification (1-7), inversions (1-8), decomposition (1-9), boost continuation, component terminology, and source boundary into PDF 023. |
| PDF 023 | 11 | Boost formula (1-10), subgroup display, Lorentz-group prose, Figure 1-1 reference, caption, and figure labels. |
| PDF 024 | 12 | Matrix map (1-11)--(1-17), Pauli matrices, determinant polarization, (A^\dagger) conversion, and figure-to-prose boundary. |
| PDF 025 | 13 | Inverse identity (1-18), complex Lorentz group discussion, complex path, Figure 1-2 reference, labels, and caption. |
| PDF 026 | 14 | Complex pair law, (1-19)--(1-23), Poincare and complex Poincare groups, and inhomogeneous (SL(2,\mathbb C)) notation. |
| PDF 027 | 15 | Complex (SL(2,\mathbb C)\times SL(2,\mathbb C)) law (1-24), representation block (1-25), irreducible spinor action (1-26), and references 7, 9, and 10. |
| PDF 028 | 16 | (SU_2) restriction, angular-momentum decomposition, (1-27), the PCT setup, and the footnote boundary into the anti-unitary discussion. |
| PDF 029 | 17 | Anti-unitary substitution (1-30), reversal (1-31), scalar PCT rule (1-32), vector spinor map (1-33)--(1-36), and componentwise conjugation. |
| PDF 030 | 18 | Vector-pair rules (1-37)--(1-40), Dirac equation (1-41), Clifford identity (1-42), and (SL(2,\mathbb C)) representation law (1-43). |
| PDF 031 | 19 | Explicit Dirac representation (1-44), P/C/T rules (1-45), charge-conjugation relation, Dirac footnote, gamma matrices, and two-component split boundary. |
| PDF 032 | 20 | Two-component equations (1-46), P/C/T rules (1-47), operator rules (1-48), PCT operator (1-49), and general-spinor substitution rules (1-50). |
| PDF 033 | 21 | General-spinor PCT rule (1-51), dotted-index definitions, state transformations (1-52), PCT state law (1-53), phase discussion, and the page boundary at the Section 1-4 heading. |
| PDF 034 | 22 | Section 1-4 opening, vacuum law (1-54), scalar one-particle states, Dirac-state footnote, mass-shell measure (1-55), scalar transformation (1-56), and unitarity argument. |
| PDF 035 | 23 | Spinor wavefunction, scalar product (1-57), corrected (\widetilde p), transformation (1-58), adjoint identity (1-59), and elementary-system definition. |
| PDF 036 | 24 | Infrared proviso, two-particle scalar product and transformation law, tensor-product notation, and combined mass definition. |
| PDF 037 | 25 | Orbital angular momentum and multiplicity, interaction and bound-state prose, spectrum discussion, Figure 1-3 reference, and collision-state setup boundary. |
| PDF 038 | 26 | Figure 1-3, collision-state continuation, asymptotic completeness, (S)-matrix equation, and in/out-state labels. |
| PDF 039 | 27 | In-field mode expansion, charge-conjugate replacement prose, in-field transformation, (S^{-1}\varphi^{\mathrm{in}}S), section heading, and references 5--7 footnote. |
| PDF 040 | 28 | Transition probability (1-60), coherent-subspace argument, projective composition, phase factor, and Wigner Theorem 1-2. |
| PDF 041 | 29 | Irreducible-representation summary, translation generator phase, six momentum cases, negative-energy branches, vacuum interpretation, and assumptions (1)--(3). |

## Equation and result inventory

The printed equation sequence (1-4) through (1-60) was checked against the
native tags. The late-page gap in the previous draft was filled with (1-51),
(1-52), and (1-53). The unnumbered displays on the same pages were checked for
placement and source order. The printed theorem on PDF 040 is transcribed as
Theorem 1-2, with the existing theorem counter preserved for the native build.

## Figure audit

- `fig1_1.tex`: label `fig:ch1-lorentz-components`, caption, four component names, subgroup names, dashed connectivity regions, and solid component circles checked against PDF 023. The lower-left component is (L^\downarrow_+); the lower-right component is (L^\downarrow_-).
- `fig1_2.tex`: label `fig:ch1-complex-lorentz-components`, four component labels, two solid (L_+(\mathbb C)) paths, dashed surrounding paths, leader labels, and caption checked against PDF 025.
- `fig1_3.tex`: label `fig:1-3`, spectral axes, vacuum, one-particle mass shell, two-particle vertical hatching, three-particle crossed hatching, legend, mass-shell label, and caption checked against PDF 038. The prose reference remains `Figure~\ref{fig:1-3}`.

## Notation conversion audit

- The source mostly-minus metric was converted to \(\eta=\operatorname{diag}(-1,+1,+1,+1)\). Timelike shells appear as \(p^2=-m^2\), and spacelike cases as \(p^2=+m^2\).
- Source Minkowski phases were converted with the contract rule. The scalar, spinor, two-particle, in-field, ket footnote, and translation-generator phases now carry the converted signs.
- The spinor matrix is written as \(\widetilde p=-p_\mu\tau^\mu=p^0\mathbf 1-\mathbf p\cdot\boldsymbol\tau\). The matrix identity uses \(A^\dagger\) for the source Hermitian-adjoint star.
- Hilbert-space vectors use kets and bras. In/out labels remain outside the delimiters. Componentwise spinor conjugation remains a star.
- The Dirac gamma convention uses \(\gamma_5=i\gamma^0\gamma^1\gamma^2\gamma^3\), which is the house form of the printed \(i\gamma^5\) diagonal relation. The Clifford identity and charge-conjugation relation were checked with that conversion.
- The six momentum cases are represented by \(p^0\gtreqless0\) on the massive and massless branches, retaining the two negative-energy branches named in the source prose.

## Corrections applied

1. Added the omitted PDF 033 material for (1-51), (1-52), (1-53), the index definitions, and the closing PCT discussion to `sec1_3.tex`.
2. Converted the Chapter 1.4 translation and mode phases, corrected the conjugate in (1-57), corrected \(\widetilde p\), and changed (1-59) to the house Hermitian adjoint.
3. Corrected the right-hand scattering bra to the out-state bra.
4. Restored both negative-energy branches in the momentum classification display.
5. Added the PDF 042 marker at the continuation of assumption (3), preserving the source page boundary after the audited range.
6. Corrected the lower component labels in Figure 1-1.

## Build and render verification

`./build_and_verify.sh --draft` completed with exit status 0 after the edits.
The build produced `latex/master.pdf` with 184 pages. The project source audit,
native chunk audit, and label scan passed. Native render pages covering the
audited material were inspected after compilation, including the PCT page,
the Section 1-4 pages, both Lorentz diagrams, the spectrum figure, the
scattering display, and the six-case momentum display.

Unresolved blockers: none
