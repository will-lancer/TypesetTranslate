# Bounded implicit-solution review: Chapters 2--4 and Appendix C

Scope: one mathematical pass over the assigned implicit exercises and their
solutions. I checked prompt--solution fit, the main derivation, signs, stated
assumptions, and the nearby source convention. The exercise's explicitly
stated metric or Fourier convention governs where it differs from the
mostly-plus Banks convention.

## Chapter 2

- `I-CH02-001`: **PASS**. The ordered/unordered configuration-space covering,
  transposition relations, one-dimensional characters, Bose/Fermi local
  operators, DHR finite-statistics qualification, and the planar braid-group
  change are all addressed coherently.
- `I-CH02-002`: **PASS**. The graded commutation calculation gives the sum of
  one-particle four-momenta, and the smearing prescription gives the correct
  distributional meaning of momentum number density.
- `I-CH02-003`: **PASS**. The positive-shell Jacobian, delta-function
  transformation, inner-product preservation, inverse map, and composition
  law are consistent.
- `I-CH02-004`: **PASS**. The missing `1/sqrt(k!)` normalization is identified,
  the one-body lift is derived with wave packets, and the rotation and boost
  formulas are reconciled with the source convention.
- `I-CH02-005`: **PASS**. The Volterra iteration, ordered simplex, cube
  replacement, second-order check, commuting limit, and unitarity statement
  are correct.
- `I-CH02-006`: **PASS**. The parity of the spins in `(A,B)`, the analytic
  spin-statistics step, the roles of positivity and locality, the higher-D
  central rotation, and the braid-statistics qualification are covered.

## Chapter 3

- `I-CH03-001`: **PASS**. The operator contraction, pairing count
  `(2r)!/(2^r r!)`, exponentiation, normalization, and two-source derivative
  check have the correct signs for the stated field expansion.
- `I-CH03-002`: **PASS**. The functional derivative remains inside the same
  time-ordering operation, including the explicit `n=1` Heaviside form and the
  polynomial insertion extension.
- `I-CH03-003`: **PASS**. The Fourier rules, source-sign reconciliation, action
  integration, constant phase, and substitution check match the `+iJ phi`
  kernel and the printed sign issue.
- `I-CH03-004`: **PASS**. Square completion, contour-shift conditions, analytic
  determinant branch, Fresnel phase, one-dimensional check, and the printed
  normalization discrepancy are handled correctly.
- `I-CH03-005`: **PASS**. The operator-mode calculation has the correct
  time-ordering pieces, the final propagator is kept in Banks's mostly-plus
  form `-i/(p^2+m^2-i epsilon)`, and the Green-function equation is stated as
  `-i(Box-m^2+i epsilon)D_F=delta^4` with the correct limiting jump.
- `I-CH03-006`: **PASS**. The spectral weights, sufficient exponential growth
  condition, tube analyticity, ordered Euclidean continuation, and contour-arc
  qualification are adequate.
- `I-CH03-007`: **PASS**. The free smeared spectral measure, threshold,
  high-energy behavior, Cutkosky support, tempered/distributional formulation,
  and Euclidean Laplace convergence are correctly distinguished. The displayed
  absolute square implicitly takes a real smearing function, which is harmless
  here.
- `I-CH03-008`: **PASS**. The expansion and vacuum-bubble cancellation are
  correct, and the solution now attributes the displayed `\ii g` factor to
  Eq. (3.26) accurately.
- `I-CH03-009`: **PASS**. The differentiated-slot vertex derivation is sound,
  and with the surrounding mostly-plus convention `p_a^2=-m^2` the on-shell
  value is now correctly reported as `+2 i g m^2`. The EOM comparison agrees.
- `I-CH03-010`: **PASS**. Under the scalar convention explicitly chosen in the
  exercise, the matrix propagator, symmetric-tensor vertex, species routing,
  mass basis, and orthogonal-basis invariance are correct.
- `I-CH03-011`: **PASS**. Orbit--stabilizer is applied correctly, including the
  tadpole factor `1/2` and the two-quartic-vertex vacuum factor `1/48`.
- `I-CH03-012`: **PASS**. The vertex and propagator factors, momentum deltas,
  loop count `L=I-V+1`, derivative momenta, and Euclidean continuation are
  consistent with the convention stated in the exercise.
- `I-CH03-013`: **PASS**. The tadpole, contact, sunset, and bubble setup has
  the appropriate position-space factors, line and loop counts, symmetry
  factors, momentum integral, and superficial degrees of divergence.
- `I-CH03-014`: **PASS**. Kernel inversion, the three-point formula, the three
  four-point exchange channels, and the tree induction are correctly derived.
- `I-CH03-015`: **PASS**. Translation and Lorentz covariance give the stated
  momentum dependence, the normalization defines a momentum-independent `Z`,
  covariant-state conversion is correct, and the pole residue check follows.
- `I-CH03-016`: **PASS**. The massive vector, Dirac, higher-spin, and
  tensor--spinor residues and LSZ external-leg operations are consistent with
  the explicitly requested mostly-minus convention, including anti-fermion
  orientations and the massless gauge qualification.

## Chapter 4

- `I-CH04-001`: **PASS**. The odd-field time-ordered kernel is antisymmetric,
  the Proca kernel is symmetric, and the Grassmann-source quadratic form gives
  the same obstruction.
- `I-CH04-002`: **PASS**. The Proca propagator, generic derivative vertex,
  momentum factors, fermion signs, symmetry factors, connected/1PI distinction,
  source legs, and monomial check are all present and consistent.
- `I-CH04-003`: **PASS**. The one-loop census is organized by field content,
  the routings and integrals are supplied, charge-conjugate odd-vector loops
  and tadpoles are identified, reducible insertions are counted, and the free
  disconnected products are stated.
- `I-CH04-004`: **PASS**. Integration by parts proves necessity and
  sufficiency of current conservation, gives source equality in the
  Stueckelberg variables, and removes the longitudinal Proca term.

## Appendix C

- `I-APPC-001`: **PASS**. The Weyl-basis adjoints, squared time matrix,
  anticommutator, unitary basis change, and exact use of `UU^dagger=1` are
  correct.
- `I-APPC-002`: **PASS**. The ordinary and chiral trace recurrences, explicit
  six- and eight-gamma reductions, Levi--Civita signs, contraction recurrence,
  corrected Banks `K_3`/`K_4` ordering, `K_5`/`K_6`, and antisymmetric-product
  identity are mutually consistent with the stated Clifford convention.

The single repair pass addressed the three local convention and sign issues.
The assigned solution blocks are now release-ready.

FINAL STATUS: PASS
