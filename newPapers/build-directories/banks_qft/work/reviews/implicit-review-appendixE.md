# Independent review: Appendix E implicit exercise

## Scope and sources

- Exercise ID: `I-APPE-001`.
- Reviewed files: `latex/implicit/I-APPE-001.tex` and
  `latex/solutions/appendixE-implicit.tex`.
- Inventory target: prove uniqueness of the symmetric invariant through the
  adjoint-square decomposition, construct the second adjoint for `SU(N)`, and
  explain its absence for the remaining compact simple Lie algebras.
- Authoritative location: printed page 258, PDF page 268.
- Native context: Appendix E's Dynkin-index convention on printed page 257 and
  the anomaly-coefficient discussion and hook on printed page 258.
- Local normalization check: the Chapter 8 anomaly discussion defines
  `d^{abc}=2 tr(T^a{T^b,T^c})` and states that anomaly coefficients are real.

## Coverage after repair

The exercise has four lettered parts.  Part (a) treats the alternating bracket,
the symmetric adjoint, and invariant cubics.  Part (b) gives the `SU(N)` matrix
construction, the full generator product, the restriction `N >= 3`, and the
`SU(2)` check.  Part (c) supplies the simple-type classification, accidental
isomorphisms, and the explicit `8 tensor 8` decomposition for `SU(3)`.  Part
(d) proves invariance of the symmetrized trace, fixes `A(F)=1`, derives the
one-generator ratio, connects the tensor to the anomaly, and checks conjugate,
real, pseudoreal, and adjoint representations.

## Findings and dispositions

| ID | Severity | Finding | Disposition |
|---|---|---|---|
| APPE-1 | High | The compound exercise lacked the lettered subparts required by the transcription contract, which obscured one-to-one coverage. | Repaired.  The prompt now has parts (a)-(d), and the solution carries matching headings. |
| APPE-2 | High | The key passage invoked an unnamed adjoint-square theorem at the point where the exercise asks for the tensor-product mechanism. | Repaired.  The solution now states the invariant three-tensor decomposition, identifies the absent mixed `S_3` sector, outlines the highest-weight and Chevalley-restriction argument, and displays the final adjoint multiplicities. |
| APPE-3 | High | The discussion treated the factor `i` in the printed symmetrized trace as a Euclidean convention.  Under Hermitian generators the trace and `A(R)` are real. | Repaired.  The text identifies the printed factor as a source error and confines the Euclidean `i` to the spacetime anomaly equation. |
| APPE-4 | Medium | The comparison with the printed `T^aT^b` formula singled out only the missing half on the structure-constant term. | Repaired.  It now states that the declared Chapter 8 normalization puts `1/2` on both `d^{abc}` and `i f^{abc}`, with an explicit identity matrix in the scalar term. |
| APPE-5 | Low | Several phrases blurred the compact real algebra with its complexification, the mathematical anti-Hermitian convention with the physicists' Hermitian convention, and Banks's matrix-size notation for `Sp(2n)` with rank notation for `sp(n)`. | Repaired.  The inner product is extended complex-bilinearly, the Hermitian realization is labeled, and both symplectic conventions are stated. |

## Exact repairs

- Converted the exercise into four contract-compliant subparts.
- Added a precise tensor-product bridge and a displayed final multiplicity
  statement for the symmetric and alternating adjoint copies.
- Aligned every solution block with its exercise subpart.
- Clarified the `SU(N)` generator normalization and both defects in the printed
  product formula.
- Recorded the repeated basic-invariant degree in even-rank `D_r` and separated
  Banks's symplectic group labels from rank notation for the Lie algebra.
- Replaced the anomaly-normalization explanation with a direct Hermiticity
  check and an explicit source-error disposition.

## Static checks

- Inventory ID, source marker, PDF page, and printed page agree in both files.
- The native hook and Appendix E solution include each resolve exactly once.
- Brace and environment stacks pass for both TeX fragments.
- Four prompt items match four solution headings.
- Equation tags are unique and sequential from `E.1` through `E.15`.
- Placeholder, trailing-whitespace, and Unicode-dash scans return zero hits.
- ChkTeX reports only reviewed fragment-level style warnings concerning its
  parsing of superscripts, the `enumitem` label, TeX double hyphens, and the
  array separator.  It reports no actionable structural defect.
- A Gell-Mann matrix spot check gives a maximum product-formula residual of
  `8.327e-17`; the raw-trace residual is `0`; the Pauli-matrix `SU(2)` symmetric
  map residual is `0`.
- Compilation was intentionally omitted by instruction.

## Verdict

**PASS**

Open findings: 0.  The exercise and solution now satisfy the inventory target,
source conventions, mathematical checks, and local authoring contract within
the requested non-compiling review scope.
