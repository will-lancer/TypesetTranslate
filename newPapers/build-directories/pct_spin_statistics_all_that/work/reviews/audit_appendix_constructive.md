# Appendix Constructive QFT audit

## Scope and source authority

This audit covers `latex/appendix/constructive.tex`, `latex/figures/figA1.tex`, and `latex/figures/figA2.tex` against canonical PDF pages 191 through 202, printed pages 179 through 190. PDF 203, printed page 191, was checked for the handoff boundary. The source is `origPapers/pct_spin_statistics_all_that.pdf`, SHA-256 `44fadba731cafe7f009d4e561372febb3597e1f2a4819346ce2efd16befcb889`. Each source raster page was inspected at original detail. Prose, displayed mathematics, list items, footnotes, citations, captions, figure labels, equation tags, notation changes, and page transitions were checked in reading order.

## Page pass record

| Source page | Printed page | Units checked | Result |
| --- | ---: | --- | --- |
| PDF 191 | 179 | Appendix title, opening survey, Main Problem quotation, constructive-QFT heading, citations [1] and [2], and the closing paragraph | PASS |
| PDF 192 | 180 | Pioneers [3]--[7], cutoff $Y_4$ prose, Yukawa interaction, total Hamiltonian, free-field definitions [8, 9], cutoff interaction, and cutoff Hamiltonian | PASS |
| PDF 193 | 181 | Self-adjointness result [10], unitary evolution, vacuum matrix element (A.1), ground-state qualification, polynomial interaction [11], total Hamiltonian, vacuum matrix element (A.2), and generalization [12] | PASS |
| PDF 194 | 182 | Conclusions (a) and (b), non-relativistic Hamiltonian, number operator, commutator, renormalized limit, evolution, self-energy explanation, references [13, 14], and continuation into lower dimensions | PASS |
| PDF 195 | 183 | Lower-dimensional singularities [15]--[19], the $λ(\varphi^4)_2$ discussion, semigroup, multiplication Hamiltonian, lower-bound argument, $Y_2$, $λ(\varphi^4)_3$, wave-function renormalization [20, 21], proof [22], box result [15]--[22], and strategy references [23, 18, 24] | PASS |
| PDF 196 | 184 | Strategy item (c), localized Hamiltonian $H_1(g)$, $H(g)$, local time evolution, Figure A.1, item (d), smeared field, local automorphism, and the page boundary | PASS |
| PDF 197 | 185 | Inner and outer automorphism statements, item (e), GNS construction and state sequence, references [25]--[27], Hamiltonian strategy, semigroup, Euclidean continuation, and references [28]--[32] | PASS |
| PDF 198 | 186 | Euclidean Gell--Mann--Low formula, $Z$, Gaussian covariance, interaction density, cutoff qualification, reconstruction theorem [34], and Euclidean references [33] and [35] | PASS |
| PDF 199 | 187 | Nelson symmetry, $H_1$, ground state, Euclidean invariant integral, reconstruction conditions [36], statistical-mechanics comparison, lattice result [37, 38], and magnetic-field result [39] | PASS |
| PDF 200 | 188 | Fourth-degree polynomial, unique-vacuum statement [40, 41], two-solution statement [42], Ising comparison, Figure A.2, survey references [43, 44], and the beginning of axiomatic verification | PASS |
| PDF 201 | 189 | Axiomatic alternative [46, 47], four skeptical questions, mass spectrum, vacuum-to-one-particle matrix element, Haag--Ruelle references [48, 49], Feynman-rule statements [50]--[54], and the non-triviality conclusion | PASS |
| PDF 202 | 190 | Asymptotic-completeness discussion, $Y_2$ Hamiltonian results [55], Euclidean fermion-integrated formula [57], both determinants, kernel, $L^p$ statement, axioms [58, 59], further references [60], and the unfinished $λ(\varphi^4)_3$ sentence | PASS |

The source has only the printed equation identifiers (A.1) and (A.2) in this packet. The native equations retain those tags and labels. Other displays remain unnumbered. Citation order and citation ranges match the scan. No footnote occurs on PDF 191 through PDF 202.

## Figure checks

Figure A.1 on PDF 196 has the source diamond, horizontal $x$ axis, detached upward $t$ arrow above the right vertex, endpoint ticks, inward arrows, $g=1$ label, and caption. The time-arrow placement was aligned to the source after rendered inspection.

Figure A.2 on PDF 200 has the $B$ axis, $β=(kT)^{-1}$ axis, diagonal hatching, the white two-phase strip beginning at $β_c$, the $β_c$ label, and the source caption. The source caption reads $Ψ_{0I}$ and $Ψ_{0II}$, with roman state labels I and II. The native caption uses the house vacuum-state labels `\Omega_{0I}` and `\Omega_{0II}` inside
`\matrixel{\Omega_{0I}}{\varphi_1(x)}{\Omega_{0I}}=-\matrixel{\Omega_{0II}}{\varphi_1(x)}{\Omega_{0II}}\ne0`.

## Notation decisions and corrections

The source Yukawa bar is rendered as `\bar\psi`, with the defining prose now using `\bar\psi=\psi^\dagger\beta` under the Weinberg house convention in `NOTATION.md`. Source $ψ^+$ products become `\bar\psi` products. Source Hilbert products become `\matrixel` expressions in the source order. Source $ψ_0$ vacuum vectors become the house `\Omega` state labels. Source script letters become `\mathcal` forms. Spatial variables use `\mathbf{x}` where the source denotes a spatial point. The source metric phrase $c^2t^2-\mathbf{x}^2$ is rendered as the equivalent mostly-plus form $-c^2t^2+\mathbf{x}^2$.

The PDF 195 semigroup display was also corrected from the draft `H_{V,\lambda}` to source-order `H_{\kappa,V}`. The subscript denotes the cutoff and box; `\lambda` remains the interaction coupling in the neighboring multiplication Hamiltonian.

The two corresponding entries in `notation-map.jsonl` now have status `reviewed`. The Figure A.2 entry records PDF 200, printed page 188, and the roman state labels. The Dirac-adjoint entry records the beta conversion at PDF 192, printed page 180.

## Boundary and marker validation

The final constructive sentence ends with “and the Euclidean” on PDF 202. `latex/appendix/local-algebras.tex` begins PDF 203 with the exact continuation “Gell--Mann--Low formula has been made to work [61, 62, 60].” The boundary carries separate `% PCT-SOURCE` markers and preserves the source reading order.

The granular marker scan found the following counts in `constructive.tex`: PDF 191, 5; PDF 192, 10; PDF 193, 13; PDF 194, 13; PDF 195, 13; PDF 196, 13; PDF 197, 9; PDF 198, 11; PDF 199, 10; PDF 200, 7; PDF 201, 5; PDF 202, 7. Figure A.1 carries its PDF 196 marker and Figure A.2 carries its PDF 200 marker. The assigned files contain no facsimile import, placeholder, or source-page dependency.

`python3 scripts/audit_source.py --strict` passed with the frozen source identity, 36 of 36 native chunks present, and 211 distinct marked PDF pages. A dedicated appendix packet wrapper containing `constructive.tex` and the following local-algebras continuation was compiled twice with `pdflatex -interaction=nonstopmode -halt-on-error`. The second pass produced an 18-page PDF with no TeX errors, undefined references, overfull boxes, underfull boxes, or remaining warnings. Rendered packet pages containing Figures A.1 and A.2 were inspected after the final corrections.

Unresolved blockers: none
