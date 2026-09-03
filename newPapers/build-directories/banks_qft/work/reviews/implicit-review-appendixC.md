# Independent review: Appendix C implicit exercises

## Scope and sources

- Exercise IDs: `I-APPC-001` and `I-APPC-002`.
- Reviewed files: `latex/implicit/I-APPC-001.tex`,
  `latex/implicit/I-APPC-002.tex`, and
  `latex/solutions/appendixC-implicit.tex`.
- Inventory targets: direct proof of Eq. (C.3) and its preservation under
  unitary basis changes; higher ordinary and chiral traces; higher gamma
  contractions; metric and Levi-Civita reductions; arbitrary-order
  recurrences.
- Authoritative locations: printed p. 248, PDF p. 258 for `I-APPC-001`;
  printed pp. 249-250, PDF pp. 259-260 for `I-APPC-002`.
- Source identity: SHA-256
  `31de7827e7bc636feaa7028fe4dbb63a718b3926ee43ff3d96d91185a44eafe3`.
- Native hooks follow Eq. (C.3) and Banks's request to continue the trace and
  contraction calculations. The relevant PDF pages were checked through
  layout-preserving extraction and rendered page images.

## Coverage after repair

`I-APPC-001` separates the temporal and spatial Weyl matrices, checks the two
Clifford facts used in Eq. (C.3), and identifies the insertion
`UU^\dagger=1` in the transformed-basis proof. Its solution gives every block
calculation and keeps the transformed time matrix inside the adjoint formula.

`I-APPC-002` now asks the reader to test Banks's displayed lower-order
contractions before extending them. The solution derives the even-trace
recurrence, expands `T_6`, supplies `T_8` and the all-order pairing rule,
derives the chiral seed and `T_{6,5}`, and gives two constructions for every
higher chiral trace. It also proves the ordered-string and antisymmetric
contraction recurrences, computes `K_5`, `K_6`, and their gamma-five versions,
and records decisive repeated-index and distinct-index checks.

## Findings and dispositions

| ID | Severity | Finding | Disposition |
|---|---|---|---|
| APPC-1 | High | The prompt treated Banks's four-factor contraction as part of the list to extend, while the solution's correct recurrence and distinct-index check did not identify the source's reversed `gamma_alpha gamma_kappa` order. | Repaired. The prompt now requires a lower-order audit. The solution displays the recurrence-derived order `gamma_kappa gamma_alpha gamma_nu`, explains the printed defect, and gives the `0123` check. |
| APPC-2 | Medium | The explicit `T_6` and `T_{6,5}` reductions carried labels inside starred `align` environments. Their later `eqref` calls had no reliable numbered targets. | Repaired. Each reduction now uses one `equation` containing `aligned`, with a valid unique label. |
| APPC-3 | Low | The all-order chiral pairing rule called its pairs oriented without fixing their orientation locally. This left the sign prescription needlessly implicit. | Repaired. Every pair is now declared to satisfy `a<b` before the permutation parity is taken. |

No finding arose in `I-APPC-001` or its solution.

## Exact repairs

- Expanded the final paragraph of `I-APPC-002` so the induction starts by
  testing Banks's displayed `K_3` and `K_4` lines.
- Added the corrected `K_4` formula and its distinct-index contradiction with
  the printed p. 250 order to the collected solution.
- Replaced two labeled starred alignments with single numbered equations.
- Fixed the orientation convention in the chiral all-order pairing formula.
- Left `I-APPC-001.tex` unchanged because its prompt and proof passed as
  written.

## Static and mathematical checks

- Both inventory IDs have one native hook, one exercise, and one collected
  solution. Source markers and page ranges agree with the inventory.
- Seven equation labels are unique, sit inside numbered environments, and
  have balanced environment stacks.
- Brace counts, exercise and solution environments, placeholder scans,
  trailing-whitespace scans, Unicode-dash scans, and tab scans pass.
- ChkTeX reports fragment-level warnings 2, 3, and 25 for equation references,
  parenthesized superscripts, and `(-1)^r`. None identifies a structural or
  mathematical defect.
- Explicit Weyl matrices give zero residual for all four components of Eq.
  (C.3). A seeded random unitary basis change gives maximum residual
  `6.50e-16`.
- Exhaustive index checks pass for all 4,368 ordinary traces through six
  gamma matrices and all 4,352 chiral traces at four and six gamma matrices.
  Another 250 seeded eight-gamma chiral cases pass the all-order pairing rule.
- Every one of the 1,024 `K_5` and 4,096 `K_6` index tuples passes, as do their
  gamma-five counterparts. For indices `0123`, the printed `K_4` right-hand
  side has norm zero, the left-hand side has norm four, and the repaired
  formula has zero residual.
- Compilation was omitted by instruction.

## Source and base issues

- Printed p. 250 has two contraction defects. Erratum E-022 already corrects
  the contracted metric index in `K_3`. The `K_4` gamma order remains in the
  source and native transcription; the implicit prompt and solution now
  identify and neutralize it. The base file and ledgers remain unchanged.
- Printed p. 250 gives `eta(s)=2 s i sigma_2 chi^*(s)`. The native appendix
  drops the factor `s`. Since `2s` is a sign for `s=+/-1/2`, this changes a
  spin-dependent phase and leaves the completeness sums intact. It remains a
  source-fidelity issue for the broader Chapter 6 Diracology exercise, outside
  these two Appendix C targets. The base file and ledgers remain unchanged.
- Existing Erratum E-031 concerns the nearby Majorana-basis transformation and
  does not enter either assigned Appendix C exercise.

## Verdict

**PASS**

Open in-scope findings: 0. The two repaired exercises now meet their inventory
targets, source conventions, mathematical checks, and authoring contract under
the requested static-review scope.
