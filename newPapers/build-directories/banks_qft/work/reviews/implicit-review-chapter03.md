# Independent implicit-solution review: Chapter 3

Scope: `I-CH03-001` through `I-CH03-016` in
`latex/solutions/chapter03-implicit.tex`. Each solution was checked against
`implicit-exercises.json`, its native hook context, and the cited source in
`banks-qft.pdf`.

The core source pages are printed 18, 19, 21-23, 25-26, 29, and 33, which are
PDF pages 28, 29, 31-33, 35-36, 39, and 43. Supplemental convention checks used
printed page 9, PDF page 19, for one-particle normalization; printed page 250,
PDF page 260, for Dirac spinors; and printed pages 254-255, PDF pages 264-265,
for external lines and graph combinatorics. I used short `pdftotext -layout`
extracts. Targeted renders of PDF pages 30, 32, 36, and 39 resolved source
signs, Gaussian normalization, the Fourier delta factor, and the missing
inverse in the Legendre-transform display. The reviewed PDF has 281 pages and
SHA-256
`31de7827e7bc636feaa7028fe4dbb63a718b3926ee43ff3d96d91185a44eafe3`.

## Coverage

| ID | Decisive check | Disposition |
|---|---|---|
| `I-CH03-001` | Wick pairings give `(2r)!/(2^r r!)`; two source derivatives recover `D_F`. | PASS |
| `I-CH03-002` | The exposed point `x` stays inside the same time ordering as every source insertion; later time derivatives retain contact terms. | PASS |
| `I-CH03-003` | Fourier insertion and integration by parts give `S_,A=K_AB phi^B-V_,A` only with the corrected `-J_A` term and `K=-partial^2`. | PASS after repair |
| `I-CH03-004` | Completion of the square gives `(2pi)^(n/2) (det K)^(-1/2)` on the analytic branch; the Fresnel limit gives the signature phase. | PASS |
| `I-CH03-005` | Operator time ordering, pole closure, and the derivative jump all give `i(Box+m^2)D_F=delta^4`. | PASS after repair |
| `I-CH03-006` | Positive spectral support and `Im z_r<0` give a holomorphic tube with preserved operator order; the free contour rotation yields `D_E`. | PASS |
| `I-CH03-007` | The free spectral measure supplies a threshold and an unsmeared counterexample; the valid fixed-order claim is tempered and distributional. | PASS after repair |
| `I-CH03-008` | Every coefficient is divided by `I_0`; numerator and denominator exponentiation cancels every vacuum component and gives `Z[0,g]=1`. | PASS after repair |
| `I-CH03-009` | Each derivative acts on its own propagator endpoint; the symmetrized vertex is `i g sum_(a<b) p_a.p_b`, with the massive equation-of-motion check. | PASS after repair |
| `I-CH03-010` | The inverse mass matrix propagates species indices, symmetric coupling tensors define allowed vertices, and orthogonal basis changes cancel internally. | PASS after repair |
| `I-CH03-011` | Orbit-stabilizer gives `S_G=1/|Aut(G)|`; the tadpole and four-parallel-line counts give `1/2` and `1/48`. | PASS after repair |
| `I-CH03-012` | Vertex integration gives `(2pi)^4 delta^4`; `V-1` constraints leave `L=I-V+1`, with explicit Lorentzian, derivative, and Euclidean signs. | PASS after repair |
| `I-CH03-013` | Contact, tadpole, sunset, bubble, and vacuum examples identify every requested graph component and reproduce their symmetry factors. | PASS after repair |
| `I-CH03-014` | Kernel inversion gives `W_2=-Gamma_2^(-1)`; differentiation gives `W_3`, all four-point channels, and a reversible leaf-removal induction. | PASS |
| `I-CH03-015` | Lorentz covariance with delta-normalized states fixes `F(p) proportional to omega_p^(-1/2)` and the isolated pole has residue `Z`. | PASS after repair |
| `I-CH03-016` | Vector and spinor residues, polarization sums, inverse kinetic operators, and all four fermion orientations match the stated normalization and Appendix D. | PASS after repair |

## Findings and repairs

### Major

None.

### Minor, repaired

1. **`I-CH03-003`: the source-sign explanation cited Problem 3.3 and left the
   sign of the lattice kernel implicit.** The contact-term derivation is
   Eq. (3.9), with Problem 3.1 supplying its general contact term.

   **Repair:** stated that the `K` used in Eqs. (3.12)-(3.14) discretizes
   `-partial^2`, derived `V'-J_A` from Eq. (3.9), and showed directly why the
   printed `+J_A` produces the opposite action.

2. **`I-CH03-005`: the final sentence described both time branches as the same
   positive-frequency wave.**

   **Repair:** identified propagation from `y` to `x` for positive time
   difference and from `x` to `y` for negative time difference.

3. **`I-CH03-007`: spatial smearing was credited with rapid decrease for a
   general interacting spectral distribution.** Spatial smearing can leave
   polynomial energy growth.

   **Repair:** separated spatial smearing from full space-time smearing and
   made the Euclidean Laplace factor responsible for controlling the remaining
   polynomial growth.

4. **`I-CH03-008`: the use of `a=i g` did not identify the source omission in
   Eq. (3.26).**

   **Repair:** tied `a=i g` to the expansion of `exp(i(S_0+gA))` and recorded
   the omitted power of `i` in the printed equation.

5. **`I-CH03-009` and `I-CH03-010`: coupling normalizations were inferable
   from the answers but unstated.** The derivative example also called the
   massive interaction equation-of-motion redundant without naming the
   induced mass term.

   **Repair:** supplied the exact derivative-interaction Lagrangian, its
   integration-by-parts identity, the induced `m^2 phi^4/3` operator, and the
   canonical contact-term qualification. For multiple real scalars, supplied
   the free and interacting Lagrangians, the symmetry of `M^2`, and complete
   symmetrization of every coupling tensor.

6. **`I-CH03-011`: the automorphism statement named incidences and valences
   only.** Decorated or multi-species graphs require automorphisms to preserve
   every interaction type.

   **Repair:** indexed identical vertices by interaction type and required
   preservation of species, vertex types, and derivative decorations.

7. **`I-CH03-012` and `I-CH03-013`: the Lorentzian coupling sign appeared
   after the momentum-space rules, and the sample `phi^4` sign differed from
   Appendix D without a local note.**

   **Repair:** moved the exact `L_I=-g sum_k v_k phi^k/k!` convention before
   the rules, retained its Euclidean continuation, and stated the equivalent
   coupling-sign map for the Appendix D examples.

8. **`I-CH03-015` and `I-CH03-016`: the LSZ pole required its isolation
   assumption, while the vector leg left the universal `1/i` inside a prose
   convention note.**

   **Repair:** stated the isolated-pole assumption, wrote
   `Z_A^(-1/2) D_(F,0)^(-1)=(p^2-m^2)/(i sqrt(Z_A))`, kept the incoming and
   outgoing polarization rules explicit, and added the spin-zero reduction as
   a final check.

No in-scope finding remains open.

## Source and base-text issues

- Eq. (3.10) prints `+J_A`. Its Fourier kernel and Eq. (3.12) require `-J_A`
  when `K=-partial^2`. The nearby prose also calls `K` the discretization of
  `partial^2`, while Eqs. (3.12)-(3.14) use the opposite sign.
- Eq. (3.16) has `(sqrt(pi/2))^n` in place of `(2pi)^(n/2)` and uses an
  absolute determinant that loses the complex Gaussian phase.
- The printed spectral-density claim on page 23 is false literally. Free
  spectral measures have delta functions or thresholds, and the unsmeared
  infinite-volume density grows. The solution gives the distributional
  statement needed for Euclidean continuation.
- Eq. (3.26) omits `i^n` under its stated `S=S_0+gV` convention.
- The free generator at the start of Sec. 3.4 has a positive quadratic
  exponent, unlike the correct negative exponent in Eq. (3.27).
- The momentum-space rule prints `2 pi^4 delta^4`; Fourier transformation
  gives `(2pi)^4 delta^4`.
- The first Legendre-transform display on printed page 29 omits the inverse on
  `Gamma_2`. The next paragraph and Eqs. (3.36)-(3.38) use the correct
  `W_2=-Gamma_2^(-1)` identity.

These base files were left unchanged.

## Out-of-scope hook order

`latex/chapters/chapter03/sec3_7.tex` places the `I-CH03-016` hook before the
`I-CH03-015` hook. The inventory and solution file order them as 015, then 016.
The chapter hook order was recorded here and left unchanged as instructed.

## Static checks

- The inventory and solution file contain the same 16 IDs, each exactly once.
- All 16 solution source markers are present and use the inventory page map.
- TeX brace counts match: 520 opening and 520 closing braces.
- Display delimiters match: 86 opening and 86 closing delimiters.
- The TeX environment stack closes cleanly.
- Every `eqref` in the solution resolves to a label in the edition.
- The solution file has no trailing whitespace.
- Critical literals were rechecked: corrected `V'-J_A`, the Gaussian
  determinant branch and signature phase, the distributional spectral
  qualification, `(2pi)^4 delta^4`, and the vector and spinor LSZ factors.
- Compilation was omitted as instructed.

FINAL STATUS: **PASS**. Every in-scope Chapter 3 finding was repaired.
