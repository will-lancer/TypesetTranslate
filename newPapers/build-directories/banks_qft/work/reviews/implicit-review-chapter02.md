# Independent implicit-exercise review: Chapter 2

Scope: exercises and solutions I-CH02-001 through I-CH02-006. I compared the
six exercise files and `latex/solutions/chapter02-implicit.tex` with
`implicit-exercises.json`, their native chapter hooks, and physical PDF pages
18, 19, 21, 22, and 23. The review covered mathematical accuracy,
completeness, assumptions, pedagogy, requested subparts, and local source
connections.

Overall: **PASS**. Every in-scope finding was repaired. The six exercise IDs
are present exactly once in the prompt files and exactly once in the collected
solution file. Compilation was excluded by instruction.

## Coverage

| ID | Printed / PDF pages | Required work | Post-repair disposition |
| --- | --- | --- | --- |
| I-CH02-001 | 8 / 18 | Configuration-space exchanges, one-dimensional statistics, parastatistics, local-QFT equivalence, and the planar exception | PASS. The solution distinguishes the permutation-group argument from the DHR reconstruction needed to handle higher-dimensional representations. |
| I-CH02-002 | 9 / 19 | Action of four-momentum on a general Fock state and the distributional meaning of number density | PASS. Both statistics signs, smearing, the total-number check, and the commutator test are explicit. |
| I-CH02-003 | 9 / 19 | Positive-shell Jacobian, transformed delta function, unitarity, and composition | PASS. The proper-orthochronous assumption and every cancellation factor are stated. |
| I-CH02-004 | 9 / 19 | Fock inner product, Eqs. (2.1)--(2.5), number and Poincare generators, and the boost formulas | PASS. The source normalization conflict is resolved transparently with \(c_k=1/\sqrt{k!}\), and the boost convention is identified. |
| I-CH02-005 | 11--12 / 21--22 | Volterra iteration, ordered simplex, full cube, time ordering, second-order check, and commuting case | PASS. The formal-domain assumption, differential equation, and initial condition are checked. |
| I-CH02-006 | 13 / 23 | General spin-statistics theorem, assumptions, positivity, locality, sample spins, higher dimensions, and braid exception | PASS. The proof is scoped to positive-metric Wightman fields and gives the analytic continuation and Reeh--Schlieder steps. |

## Findings and dispositions

### Major, repaired

- **I-CH02-006: the norm did not match the displayed two-point kernel.** The
  kernel is
  \(\langle0|\Phi(z)\Phi^\dagger(0)|0\rangle\), so its vanishing controls
  \(\Phi^\dagger(f)|0\rangle\). The earlier text instead wrote the norm of
  \(\Phi(f)|0\rangle\). Lines 406--411 now use the adjoint field and apply
  Reeh--Schlieder to it before concluding that \(\Phi\) vanishes.
- **I-CH02-006: the theorem's exclusion of wrong-statistics ghosts needed an
  explicit scope statement.** Lines 349--352 now declare a nonzero
  finite-component Wightman field, positive Hilbert metric, cyclic invariant
  vacuum, spectrum condition, and graded locality. The statistics sign is
  defined at line 398. This keeps the theorem from being applied to
  indefinite-metric ghost fields.

### Moderate, repaired

- **I-CH02-004: the source boost display is anti-Hermitian while nearby
  rotation generators use the usual Hermitian language.** Lines 279--282 now
  state the convention \(\delta|p\rangle=v^iJ_{0i}|p\rangle\) and identify
  the Hermitian generator \(K_i=\mathrm{i}J_{0i}\) in
  \(U=\exp(-\mathrm{i}v^iK_i)\).
- **I-CH02-005: the Dyson series lacked a general verification and an operator
  domain assumption.** Lines 285--288 state the common-domain or regulated
  formal-series interpretation. Lines 311--314 differentiate the outer
  integration limit and recover both the evolution equation and initial
  condition.

### Minor, repaired

- I-CH02-001 now repeats the prompt's unique-vacuum assumption in the DHR
  paragraph.
- I-CH02-002 now defines \(\varepsilon\), records
  \([P^\mu,a^\dagger(q)]=q^\mu a^\dagger(q)\), and restricts the extensions
  \(f=1\) and \(f=p^\mu\) to the finite-particle domain.
- I-CH02-003 now states that \(\Lambda\) is proper orthochronous before using
  invariance of the positive mass shell.
- I-CH02-004 now defines the provisional \(c_k\)-normalized state before
  displaying its inner product.

## Source and base-file findings

- **Fock normalization conflict, resolved in the editorial exercise.** PDF
  pages 18--19 combine Eq. (2.1), with a factor \(1/k!\), Eq. (2.2), with an
  unnormalized creator product, and Eq. (2.3), with canonical delta
  normalization. A direct two-particle contraction gives the permutation sum
  with coefficient one when \(c_k=1\). The current prompt and solution derive
  \(c_k=1/\sqrt{k!}\) and state the literal \(c_k=1\) outcome.
- **Base cross-reference defect, outside this lane.** In
  `latex/chapters/chapter02/sec2_1.tex`, line 253 cites Eq. (2.19), while PDF
  page 21 cites Eq. (2.14). Line 256 cites Eq. (2.17), while the PDF cites Eq.
  (2.12). The base transcription was left unchanged.
- **Inventory page span.** I-CH02-005 records PDF page 21, although its target
  includes Eqs. (2.17)--(2.18) on PDF page 22. The review used both pages. The
  inventory was left unchanged.

## Static checks

- JSON-to-prompt and JSON-to-solution ID comparison: six expected IDs; six
  exact matches in each location; no duplicates or omissions.
- Structural counts: six `exercise` starts and ends; six
  `\BanksImplicitSolution` entries; one balanced `bankssolutions` environment.
- Raw brace count across the seven reviewed TeX files: 290 opening and 290
  closing braces.
- `chktex` with the repository's fragment-appropriate warning exclusions:
  clean.
- `lacheck`: four messages, all its known punctuation heuristic applied to
  mathematical factorial signs such as `k!`; no structural or prose defect.
- Trailing-whitespace and placeholder scan: clean.
- Compilation: not run, as instructed.

FINAL STATUS: **PASS**. No in-scope mathematical, coverage, clarity,
assumption, or static-structure issue remains.
