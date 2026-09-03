# Bounded implicit-solution review: Chapter 8

Date: 2026-09-02

Scope: `I-CH08-001` through `I-CH08-020` in
`latex/solutions/chapter08-implicit.tex`.  I read each exercise beside its
solution and checked the nearby native hook in `latex/chapters/chapter08/`
against the relevant local derivation.  This was one release pass at the
requested 98% threshold.

## Coverage

| ID | source context | decisive check | disposition |
|---|---|---|---|
| I-CH08-001 | `opening.tex` | complete dimension-four operator list, invariant tensors, anomaly condition | PASS |
| I-CH08-002 | `opening.tex` | longitudinal cancellation, Yang--Mills cubic/quartic form, antisymmetry and Jacobi | PASS |
| I-CH08-003 | `sec8_2.tex` | unfixed kernels, gauge/scalar vertices, broken-orbit zero modes | PASS |
| I-CH08-004 | `sec8_2.tex` | quartet and doublet homotopies, ghost-number-zero cohomology, gauge-fixing independence | PASS |
| I-CH08-005 | `sec8_4.tex` | bubble plus seagull transversality, pole, UV logarithm, and small-momentum decoupling | PASS |
| I-CH08-006 | `sec8_5.tex` | BPS linearization, modified-Bessel tail, magnetic-field localization | PASS |
| I-CH08-007 | `sec8_5.tex` | integer two-chain constraint, minimal surface, strong-coupling correction and tension | PASS |
| I-CH08-008 | `sec8_6.tex` | nonsinglet Ward identity, GMOR, one-flavor anomaly, instanton-induced mass, logical scope | PASS |
| I-CH08-009 | `sec8_6.tex` | Fermi normalization, QED cross section, neutral current, CKM cancellation | PASS |
| I-CH08-010 | `sec8_7.tex` | uniform weighted resolvent estimate, positive average, analyticity at zero momentum | PASS |
| I-CH08-011 | `sec8_8.tex` | consistent/covariant anomaly relation, Bardeen--Zumino polynomial and WZ qualification | PASS |
| I-CH08-012 | `sec8_8.tex` | conjugate, real/pseudoreal, SU(2), SO(6), symplectic and exceptional cases | PASS |
| I-CH08-013 | `sec8_8.tex` | descent, nontriviality of the cubic class, local WZ classification | PASS |
| I-CH08-014 | `sec8_8.tex` | torsion-free spin connection, Lorentz transformation, all hypercharge branches | PASS |
| I-CH08-015 | `sec8_8.tex` | B/L triangle traces, equal gauge terms, B-L, and Chern--Simons changes | PASS |
| I-CH08-016 | `sec8_8.tex` | instanton and sphaleron exponents, symmetric-phase rate dimensions, selection rules | PASS |
| I-CH08-017 | `sec8_8.tex` | Wess--Zumino extension quantization, `k=N`, gauged descent and `K/f` scaling | PASS |
| I-CH08-018 | `sec8_8.tex` | 10-representation anomaly fraction, even-N obstruction, conditional flavor restriction | PASS |
| I-CH08-019 | `sec8_8.tex` | longitudinal `1/q^2`, discontinuity, Goldstone and collinear-triangle realizations | PASS |
| I-CH08-020 | `sec8_9.tex` | dressed-field transformations, broken/unbroken split, `R_kappa` limit and noncommuting UV limit | PASS |

## Findings

No release-blocking mathematical error was found in the assigned twenty
solutions.  The solutions retain the source conventions while stating the
needed qualifications: the anomaly representatives differ by a local current
improvement, the Wess--Zumino quantization statement is for `N_F >= 3`, the
all-`(N,N_F)` baryon exclusion is conditional on the persistent composite-mass
and integer-restriction inputs, and the instanton discussion distinguishes a
tunneling amplitude from a rate.

The only delicate limit is `I-CH08-020`: the unphysical pole masses scale with
`kappa`, while the finite low-energy massive-vector residue retains its
physical longitudinal polarization.  The solution's conclusion is stated at
the pole-residue level and correctly keeps the ultraviolet/noncommuting-limit
caveat.

## Static checks

- All twenty exercise files exist and each contains its matching
  `\\BanksImplicitSolution` block.
- Each assigned ID occurs once in the exercise inventory and once in the
  Chapter 8 implicit solution file.
- The solution covers every requested subpart, including assumptions and
  convention-dependent overall signs where appropriate.
- No TeX files were edited during this review.

FINAL STATUS: PASS
