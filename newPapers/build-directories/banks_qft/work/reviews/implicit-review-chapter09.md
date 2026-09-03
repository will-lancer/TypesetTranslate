# Independent review: Chapter 9 implicit solutions

**Verdict: PASS.** I-CH09-001 through I-CH09-023 are complete after the
repairs listed below. No in-scope mathematical or expository defect remains.

## Scope and evidence

Reviewed artifacts:

- all 23 Chapter 9 records in `implicit-exercises.json`;
- all 23 prompts in `latex/implicit/`;
- every native `\BanksImplicitHook` context in `latex/chapters/chapter09/`;
- `latex/solutions/chapter09-implicit.tex` in full;
- the cited Banks pages, extracted with `pdftotext -layout` in short ranges.

The source is Tom Banks, *Modern Quantum Field Theory: A Concise
Introduction*, 281 pages, SHA-256
`31de7827e7bc636feaa7028fe4dbb63a718b3926ee43ff3d96d91185a44eafe3`.
The page pairs below are printed/PDF pages:

`001-002 138/148; 003 140/150; 004 145/155; 005 147/157; 006 148/158;
007 154/164; 008 155/165; 009 158/168; 010 165/175; 011 167/177;
012 168/178; 013-014 169/179; 015-016 172/182; 017 174/184;
018 178/188; 019 180/190; 020 185/195; 021 187/197;
022 191-192/201-202; 023 201/211`.

PDF pages 179 and 190 were also rendered as single pages to verify the
zero-momentum wording and the charged-vector conventions. Printed pages
173-174/PDF pages 183-184 were checked for the gauge-parameter RG relation.
The scalar-QED quartic normalization received a supplemental check against
[Srednicki's scalar-electrodynamics derivation](https://web.physics.ucsb.edu/~mark/ms-qft-DRAFT.pdf),
Sections 65-66.

## Coverage

| ID | Obligations checked | Result |
|---|---|---|
| 001 | Gradient identity, Lyapunov decrease, compact-orbit convergence, isolated limit point, RG-time signs | Complete and conditional |
| 002 | Wilson step, operator eigenvalue, correlator scaling, free-scalar check | Complete |
| 003 | BRST gauge independence, unitary limit, UV behavior, conserved-current check | Repaired |
| 004 | Quantum and classical analyticity, thermodynamic limit, Lee-Yang mechanism, Ising check | Repaired |
| 005 | Exact blocking, connected cumulants, quasi-locality, continuum mesh, central limit | Repaired |
| 006 | Full graph and subgraph UV bounds, termwise scope, infrared rearrangement | Complete |
| 007 | Local trace Ward identity, finite Weyl path, conformal map, improved scalar | Repaired |
| 008 | Euclidean and Minkowski insertion signs, convergence, Dyson check | Complete |
| 009 | All two-loop topologies, forests, field subtraction, MS poles, beta function | Repaired |
| 010 | Fermion and scalar species, seagulls, Ward identities, scalar potential, quartic normalization | Repaired |
| 011 | Inverse-propagator contraction, shift invariance, regulator caveat, tensor form | Complete |
| 012 | Gamma recursion, reflection, proper time, Gaussian factors, continuation | Complete |
| 013 | Total derivative, convergence strip, analytic continuation, meaning of the zero | Complete |
| 014 | Small-proper-time degree, tensor order, differentiated check | Complete |
| 015 | Wave-function and mass-pole cancellation, omitted product, limiting checks | Complete |
| 016 | Characteristic solution, running coupling and gauge parameter, cut phase, Landau limit | Repaired |
| 017 | Forest pole order, coupling and field recursions, several couplings | Repaired |
| 018 | Unitarity shortening, Maxwell equations, free-field theorem, Wick factorization | Repaired |
| 019 | Curvature decomposition, magnetic term, quartic term, Proca comparison, `g=2` | Repaired |
| 020 | Separate tensor coefficients, tadpole, ghosts, matter, transversality, beta distinction | Repaired |
| 021 | Euclidean integrals, Wick phases, tensor factor, contraction and dimensions | Complete |
| 022 | Simple/double pole separation, every LSZ factor, assumptions, free check | Complete |
| 023 | Weinberg counting, powers of `f` and `4 pi`, counterterms, Adler limit | Repaired |

## Findings and disposition

| Severity | ID | Finding | Disposition |
|---|---|---|---|
| Major | 009 | The two-loop answer lacked a usable topology and forest ledger and did not separate the proper vertex from `Z_phi`. | Added the three iterated bubbles, six wineglass graphs, mass forest, six coupling-counterterm insertions, nonlocal-pole cancellation, `Z_4`, `Z_phi`, and the `-17/6` check. |
| Major | 010 | The scalar-QED quartic pole had an ambiguous normalization, and scalar-potential tadpoles were absent from the many-field scalar self-energy. | Fixed the canonical `V=lambda*abs(phi)^4/4` relation to `5 lambda^2-12 e^2 lambda+24 e^4`; added the general real-component quartic tensor and its mass-matrix tadpole pole. |
| Major | 018 | Linear equations were used as though they alone implied Gaussian correlators. | Inserted the positivity shortening step and the Wightman/Jost-Schroer free-field theorem, with locality, spectrum, vacuum, and mixing assumptions. |
| Moderate | 007 | A constant rescaling could only prove an integrated trace statement. | Made arbitrary compactly supported Weyl test functions explicit before the distributional conclusion. |
| Moderate | 016 | The running gauge parameter followed a coefficient inconsistent with `kappa_0=Z_3 kappa`. | Derived `d kappa/d ln k=-2 alpha kappa/(3 pi)` and the exact four-dimensional invariance of `alpha kappa`. |
| Moderate | 019 | The sign of `D_mu W^+` disagreed with the prompt's definitions of `F^a` and `W^+`. | Changed it to `partial_mu-i e A_mu`; the Pauli term and `g_mag=2` now share one convention. |
| Moderate | 020 | The general-gauge triple-gluon row appeared without its gauge-parameter decomposition. | Added the Feynman-gauge pair `(19/6,-11/3)`, the longitudinal shift, its quadratic cancellation, and the scaleless tadpole. |
| Moderate | 023 | Derivative counting was presented as a diagram-by-diagram proof of the Adler zero. | Assigned the zero to the nonlinear-symmetry Ward identity and stated the required fixed-order diagram sum. |
| Minor | 003 | The unitary-gauge limit lacked the renormalized order of limits. | Required renormalization first and stated the existence condition. |
| Minor | 004 | The classical analytic-integral step needed a theorem-level bound. | Added holomorphic extension, a locally uniform integrable majorant, Morera, and Cauchy estimates. |
| Minor | 005 | The kernel formula used a schematic derivative in place of the linked-cluster identity. | Replaced it with the exact logarithm and connected-cumulant expansion. |
| Minor | 017 | The several-coupling case stopped before the higher-pole equations. | Added both multivariate recursions and the maximal-forest qualification. |

No finding remains open.

## Source and base-text issues

- On printed page 138/PDF 148, the prose about asymptotic fixed-point behavior
  omits the compactness and isolation conditions needed for the stated
  convergence. The prompt supplies them, and solution 001 uses them.
- On printed page 154/PDF 164, an integrated metric variation does not by
  itself yield local Weyl invariance. The prompt adds arbitrary local
  rescalings plus the anomaly and virial assumptions. Solution 007 keeps that
  boundary visible.
- On printed page 169/PDF 179, “the formula ... vanishes” refers to the
  right-hand side of the equation for `p^2 Pi(p^2)`. It does not say
  `Pi(0)=0`. Solution 013 states this explicitly.
- The displayed gauge-parameter term near printed pages 173-174/PDF 183-184
  conflicts with the same text's `kappa_0=Z_3 kappa` and definition of the
  photon anomalous dimension. Solution 016 follows the bare-parameter
  identity, which also gives the check `D(alpha kappa)=0` in four dimensions.
- Printed page 180/PDF 190 uses an equivalent charged-vector convention with
  a different placement of `i`. Exercise 019 fixes its own `W^+` definition;
  the repaired solution follows that definition throughout.

These source limits require no chapter-text edit for this review.

## Static checks

- Inventory records, prompt files, native hooks, and solution blocks each
  number 23. Their ID set is exactly `I-CH09-001` through `I-CH09-023`.
- Every solution ID occurs once and appears in numeric order.
- One `bankssolutions` opening and one closing were found.
- Unescaped brace counts are balanced: 660 opening and 660 closing.
- Placeholder scan found zero `TODO`, `FIXME`, `TBD`, or placeholder markers.
- A ChkTeX sample produced only known house-notation warnings for hyphenated
  IDs, derivative shorthand, graded brackets, and antisymmetrized indices.

Compilation was excluded by the review instructions and was not performed.
