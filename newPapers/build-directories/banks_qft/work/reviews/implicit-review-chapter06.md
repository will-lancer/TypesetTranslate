# Independent review: Chapter 6 implicit exercises

## Scope and sources

- Exercise IDs: `I-CH06-001` through `I-CH06-007`.
- Reviewed files: the seven matching files under `latex/implicit/` and
  `latex/solutions/chapter06-implicit.tex`.
- Compared against `implicit-exercises.json`, all seven native hooks, nearby
  chapter text, Appendix C, and `banks-qft.pdf`.
- Source identity: SHA-256
  `31de7827e7bc636feaa7028fe4dbb63a718b3926ee43ff3d96d91185a44eafe3`.
- Source review used layout-preserving extraction for PDF pp. 76-84 and
  258-260. Rendered checks covered PDF pp. 77, 79, 81-82, and 258-260.

## Coverage after repair

| ID | Printed / PDF pages | Obligation and decisive check | Status |
|---|---|---|---|
| I-CH06-001 | 66-67 / 76-77 | Restore the finite-electron-mass trace bracket, convert it to `q^2`, and check high-energy suppression. Direct matrices give the full trace product as 32 times the stated bracket. | PASS |
| I-CH06-002 | cue 67 / 77; Appendix C 248-250 / 258-260 | Derive the three gamma bases, Eq. (C.3), antisymmetric dualities, traces, contractions, and normalized spinors. Explicit matrices check every duality component, every displayed contraction, and both completeness sums. | PASS |
| I-CH06-003 | 68 / 78 | Derive the `alpha^2/E^2` law and expand Eq. (6.11). The binomial expansion confirms the cancellation of the term linear in `m_mu^2/E^2`. | PASS |
| I-CH06-004 | 69 / 79 | Rescale all four worldline phases and compare their powers of `M_mu`. Direct substitution gives orders `1`, `M_mu^2`, `1`, and `M_mu^-2`. | PASS |
| I-CH06-005 | 71-72 / 81-82 | Reduce the on-shell parity-even vertex and fix the Gordon sign. The Dirac equations give `P_mu = 2m gamma_mu - gamma_munu q^nu` between spinors. | PASS |
| I-CH06-006 | 72-73 / 82-83 | Remove the longitudinal form factor, including `q^2=0`, and test the parameter integral. The numerator is odd under `x <-> y` while the domain and denominator are invariant. | PASS |
| I-CH06-007 | 74 / 84 | Evaluate the simplex integral and justify the massless-photon limit. The interval length cancels the endpoint factor, and a uniform bound by `z` proves dominated convergence. | PASS |

## Findings and dispositions

| ID | Severity | Finding | Disposition |
|---|---|---|---|
| CH06-1 | High | `I-CH06-005` repeated the sign in the faulty Gordon rearrangement on printed p. 71. With Banks's stated `gamma_munu` convention, that sign conflicts with Problem 5.14 and the Dirac equations. | Repaired. The tensor term now has a minus sign, its equivalent Problem 5.14 form is shown, and the source conflict is identified. |
| CH06-2 | High | `I-CH06-002` propagated the reversed `gamma_alpha gamma_kappa` order from the printed four-matrix contraction on p. 250. | Repaired. The recurrence-derived order is displayed, Erratum E-022 is separated from this defect, and a distinct-index contradiction is supplied. |
| CH06-3 | High | The compound Diracology assignment used numbered items and its solution had no matching subpart headings. This violated the one-cue and lettered-subpart contract. | Repaired. The prompt and solution now align as parts (a)-(d). |
| CH06-4 | Medium | The antisymmetrization weight and the Dirac-basis `v` rephasing were implicit even though the prompt asks for every phase convention. The native appendix also drops the source's spin label in `eta_s`. | Repaired. The normalized permutation sum, the common `v` phase, and the source factor `2s` are explicit. |
| CH06-5 | Medium | The proof of the antisymmetric contraction identity skipped the anticommutator count. The worldline rescaling displayed action terms without the factors of `i` carried by the phases. | Repaired. Both contributions to the contraction coefficient are derived, and all four rescaled exponents retain their phases. |
| CH06-6 | Medium | The infrared discussion in `I-CH06-007` inferred the photon-mass limit from the endpoint cancellation alone. | Repaired. The regulated integrand is bounded by `z`, so dominated convergence proves the limit. The nearby printed photon-mass sign is identified. |
| CH06-7 | Medium | The finite-`m_e` answer stated the right bracket while only alluding to the separate normalization problem in Eqs. (6.7)-(6.8). | Repaired. It now derives the factor 32 and confines the requested answer to `Delta B_e`. `I-CH06-003` treats Eq. (6.11) as its stated starting normalization. |
| CH06-8 | Medium | The eight authored files lacked source markers, and the inventory page spans for `I-CH06-005` and `I-CH06-006` stop before source material used by their prompts. | Repaired in scope. Every exercise and solution has a marker covering the pages used. The inventory remains unchanged. |

## Exact repairs

- Added source markers to every prompt, every collected solution, and the
  solution section.
- Converted `I-CH06-002` to four lettered subparts with matching solution
  headings.
- Defined normalized antisymmetrization, completed its contraction proof,
  corrected the four-matrix gamma order, and added the distinct-index test.
- Recorded the source's `2s` spin-basis factor and the allowed common phase
  used for the displayed Dirac-basis antiparticle spinors.
- Isolated the finite-`m_e` bracket from the faulty overall normalization and
  made the use of Eq. (6.11) conditional on its printed normalization.
- Restored every factor of `i` in the rescaled worldline phases.
- Corrected the Gordon identity and connected it to Problem 5.14.
- Added a regulated endpoint bound for Schwinger's parameter integral.

## Static and mathematical checks

- Seven inventory IDs match seven exercise labels, seven hooks, and seven
  collected solutions, each exactly once.
- All exercise, enumerate, and solution environments balance. Raw brace counts
  across the eight reviewed TeX files are 359 opening and 359 closing braces.
- Source-marker, equation-reference, placeholder, tab, trailing-whitespace,
  and Unicode-dash scans pass. Every `eqref` resolves in the native LaTeX tree.
- `chktex` passes with the repository's fragment-level exclusions for IDs,
  mathematical parentheses, enum labels, and intersentence heuristics.
  `lacheck` is clean.
- Explicit Weyl, Dirac, and Majorana matrices give maximum representation
  residual `3.33e-16`. All 336 rank-two, rank-three, and rank-four duality
  components have zero residual.
- All 340 index tuples in the displayed `K_1` through `K_4` contractions pass.
  The printed `K_4` order has maximum entry residual 4 and vanishes on a
  mutually distinct-index test where the left side is nonzero.
- Generic massive Weyl spinors solve both Dirac equations to `1.41e-15`; both
  completeness sums pass to `1.11e-15`. The stated Dirac-basis `v` rephasing
  passes to `2.71e-16`.
- A generic on-shell Gordon check passes to `7.12e-15`; the printed Section 6.4
  sign gives a nonzero residual. The identity
  `gamma_munu P^nu = -q_mu` passes to `1.94e-15`.
- A finite-mass annihilation check returns `trace product / bracket = 32` and
  zero residual for `Delta B_e = m_e^2(q^2+2m_mu^2)/2`.
- The large-energy series, worldline powers, Ward contraction, odd-parameter
  cancellation, simplex value `1/2`, and regulator bound were checked
  independently.
- Compilation was omitted by instruction.

## Source, base, and inventory issues

- Printed p. 67, PDF p. 77 says the calculation sums initial spins and averages
  final spins. The factor `1/4` does the reverse: it averages the two incoming
  spins and sums the outgoing spins.
- On the same page, the product of traces in Eq. (6.7) equals 32 times the
  bracket in Eq. (6.8), while Eq. (6.8) retains the same prefactor. Equation
  (6.9) also lacks the factor `E^-2` required by dimensions and two-body phase
  space. Equations (6.10)-(6.11) have the expected dimensions despite this
  broken intermediate chain.
- Printed p. 71, PDF p. 81 has the wrong tensor sign in its rearranged Gordon
  identity. Problem 5.14 gives the consistent form. The native Chapter 6 text
  preserves the printed sign.
- Printed p. 72, PDF p. 82 gives
  `U=-xy q^2+(1-z)^2m^2-z mu^2`. Completing the square in the displayed three
  denominators gives `+z mu^2`. Equation (6.18) has already set `mu=0`, so its
  value and `F_2(0)` are unchanged.
- Printed p. 249, PDF p. 259 omits factors of `i` in the gamma dualities under
  its stated `gamma_5` and epsilon conventions. The Chapter 6 solution uses
  the component-checked phases.
- Printed p. 250, PDF p. 260 reverses two gamma matrices in `K_4`. The native
  appendix preserves that order. Erratum E-022 covers the separate `K_3`
  metric-index defect.
- Printed p. 250 has `eta(s)=2s i sigma_2 chi^*(s)`. The native appendix drops
  `s`. The solution keeps the source factor. Completeness is phase-insensitive.
- Erratum E-031 supplies the Majorana transformation used in the solution.
- The inventory lists only PDF p. 81 for `I-CH06-005` and p. 82 for
  `I-CH06-006`. Their requested derivations use the continuations on pp. 82
  and 83. The source markers cover those continuations.
- Source chapters, Appendix C, `ERRATA.md`, `QUERY_LEDGER.md`, and the inventory
  received no edits.

## Verdict

**PASS**

Open in-scope findings: 0.
