# Errata ledger

## E-001: Appendix cross-reference

- Physical PDF page: 12
- Printed page: 2
- Source form: `Appendix G`
- Adopted form: `Appendix E`
- Reason: The source's group theory and Lie algebras material is Appendix E.

## E-002: Circular polarization basis

- Physical PDF page: 264
- Printed page: 254
- Source form: `2^{-1/2}(\hat e_1\pm\hat e_1)`
- Adopted form: `2^{-1/2}(\hat{bold e}_1\pm i\hat{bold e}_2)` in the
  `D=4` specialization
- Reason: Circular polarization uses the two orthogonal transverse vectors with
  a relative imaginary coefficient. The printed form repeats the first vector.

## E-003: Interaction-picture boundary factor

- Physical PDF page: 24
- Printed page: 14
- Source form: `e^{-iHt_0}` in Problem 2.2
- Adopted form: `e^{-iH_0t_0}`
- Reason: Equation (2.11) supplies this definition, and the corrected factor gives
  `U_D(t_0,t_0)=1`.

## E-004: Finite-volume vacuum-overlap threshold

- Physical PDF page: 24
- Printed page: 14
- Source form: overlap vanishes in finite volume for two or more space dimensions
- Adopted form: overlap vanishes in finite volume for four or more spatial
  dimensions, equivalently for spacetime dimension `D >= 5`
- Reason: The logarithm of each high-momentum overlap is proportional to
  `|\mathbf k|^{-4}`, so the ultraviolet mode integral diverges for `D-1 >= 4`.

## E-005: Gaussian source-functional sign

- Physical PDF page: 26
- Printed page: 16
- Source form: `+i/2` multiplying the source-convention kernel
  `1/(p_old^2-m^2+i epsilon)` in Problem 2.11
- Source-convention correction: `-i/2` multiplying that same kernel
- Convention-adapted form: `+i/2` multiplying
  `1/(p^2+m^2-i epsilon)`
- Reason: Expanding `exp(i integral J phi)` to second order fixes the sign
  relative to the time-ordered propagator. The metric conversion changes the
  denominator by an overall minus sign, so the adapted coefficient returns to
  `+i/2` while preserving the corrected functional.

## E-006: Static-source delta functions

- Physical PDF page: 26
- Printed page: 16
- Source form: `delta^4(x)-delta^4(x-R)` inside a finite time window
- Adopted form: `delta^(D-1)(bold x)-delta^(D-1)(bold x-bold R)` for the
  spatial source profile
- Reason: Four-dimensional delta functions localize the sources at one time and
  remove the stated large-`T` limit. Static sources require spatial deltas.

## E-007: Opening typo in Chapter 10

- Physical PDF page: 216
- Printed page: 206
- Source form: `purse the subject`
- Adopted form: `pursue the subject`
- Reason: The surrounding sentence concerns readers who wish to study the topic.

## E-008: Typo in Problem 10.2

- Physical PDF page: 250
- Printed page: 240
- Source form: `arbitary`
- Adopted form: `arbitrary`
- Reason: This is a spelling error.

## E-009: Nielsen spelling in Problem 10.4

- Physical PDF page: 251
- Printed page: 241
- Source form: `Abrikosov--Nielson--Olesen`
- Adopted form: `Abrikosov--Nielsen--Olesen`
- Reason: This restores the standard spelling of Holger Bech Nielsen's name.

## E-010: Heat-flow sentence

- Physical PDF page: 161
- Printed page: 151
- Source form: `the sub-manifold of quasilocal cut-off actions it preserved`
- Adopted form: `the sub-manifold of quasilocal cut-off actions is preserved`
- Reason: The printed sentence contains a typographical substitution in its verb.

## E-011: Typo in Problem 7.1

- Physical PDF page: 99
- Printed page: 89
- Source form: `Lagrangrian`
- Adopted form: `Lagrangian`
- Reason: This is a spelling error.

## E-012: Goldstone kinetic field in Equation (7.3)

- Physical PDF page: 96
- Printed page: 86
- Source form: `(partial_mu phi)^2`
- Adopted form: `(partial_mu G)^2`
- Reason: The surrounding construction defines `G` as the Goldstone field and
  couples that same field to the fermion axial current.

## E-013: Magnetic-current propagator argument

- Physical PDF page: 115
- Printed page: 105
- Source form: `D(x,y)` in the quadratic magnetic-current term
- Adopted form: `D(x-y)`
- Reason: Translation invariance and the adjacent electric-current term require
  the propagator to depend on the coordinate difference.

## E-014: Nielsen spelling in Section 8.6

- Physical PDF page: 125
- Printed page: 115
- Source form: `Froggatt--Nielson`
- Adopted form: `Froggatt--Nielsen`
- Reason: This restores the spelling used in reference 96.

## E-015: Nielsen spelling in the author index

- Physical PDF page: 278
- Printed page: 268
- Source form: `Nielson, H. B.`
- Adopted form: `Nielsen, H. B.`
- Reason: This restores the spelling used in references 84 and 96.

## E-016: Nielsen spelling in the subject index

- Physical PDF page: 280
- Printed page: 270
- Source form: `Nielson--Olesen vortex`
- Adopted form: `Nielsen--Olesen vortex`
- Reason: This restores the spelling used in reference 84.

## E-017: Chapter 4 problem cross-reference

- Physical PDF page: 48
- Printed page: 38
- Source form: `Problem 2.6`
- Adopted form: `Problem 2.8`
- Reason: Problem 2.8 constructs the massive spin-j states discussed in Section 4.1.

## E-018: Symmetric mass-matrix description

- Physical PDF page: 63
- Printed page: 53
- Source form: `general compact symmetric matrix`
- Adopted form: `general complex symmetric matrix`
- Reason: The Weyl-fermion mass matrix is complex and symmetric; compactness is
  a property of the gauge group in the preceding sentence.

## E-019: Outgoing antimuon momentum in Figure 6.3

- Physical PDF page: 76
- Printed page: 66
- Source form: the displayed `K_+` and `K_-` labels repeat the same two
  negative spatial components
- Adopted form: `K_+` retains the negative components and `K_-` has the
  opposite, positive components
- Reason: Center-of-mass momentum conservation requires `K_+ + K_-` to have
  zero spatial part, in agreement with the scalar products on the next page.

## E-020: Typo in Section 6.4

- Physical PDF page: 82
- Printed page: 72
- Source form: `unambigous`
- Adopted form: `unambiguous`
- Reason: This is a spelling error.

## E-021: Final outgoing-field index in the LSZ formula

- Physical PDF page: 44
- Printed page: 34
- Source form: `Phi(y_1) ... Phi(y_m)`
- Adopted form: `Phi(y_1) ... Phi(y_n)`
- Reason: The formula has `n` outgoing wave functions and integration variables
  `y_1` through `y_n`; `m` labels the incoming fields.

## E-022: Contracted metric index in Appendix C

- Physical PDF page: 260
- Printed page: 250
- Source form: `-4 gamma_mu eta_{nu lambda}`
- Adopted form: `-4 gamma_mu eta_{nu kappa}`
- Reason: The `lambda` index is contracted on the left-hand side. Direct Clifford
  algebra reduction leaves `nu` and `kappa` as the metric indices.

## E-023: External Lorentz index in Equation (9.8)

- Physical PDF page: 196
- Printed page: 186
- Source form: `delta_alpha^mu` in the second three-gauge-boson vertex
- Adopted form: `delta_alpha{}^nu`
- Reason: The second vertex carries the free external index `nu`; retaining `mu`
  would duplicate the first vertex's free index.

## E-024: Typo in Section 9.12

- Physical PDF page: 200
- Printed page: 190
- Source form: `forseeable`
- Adopted form: `foreseeable`
- Reason: This is a spelling error.

## E-025: Reducible-diagram acronym in Section 9.14

- Physical PDF page: 206
- Printed page: 196
- Source form: `1P reducible` followed by `ignoring all 1PI diagrams`
- Adopted form: `one-particle-reducible (1PR)` followed by `ignoring all 1PR diagrams`
- Reason: Tadpole cancellation removes one-particle-reducible vacuum graphs;
  the remaining 1PI vacuum graphs generate the effective potential.

## E-026: Clifford-oscillator normalization in Problem 8.9

- Physical PDF page: 144
- Printed page: 134
- Source form: `sqrt(2) a_i = Gamma_(2i-1) + i Gamma_(2i)` together with
  `{Gamma_mu,Gamma_nu}=2 delta_(mu nu)` and `{a_i,a_j^dagger}=delta_(ij)`
- Adopted form: `2 a_i = Gamma_(2i-1) + i Gamma_(2i)`
- Reason: The adopted coefficient gives the stated canonical fermion
  anticommutator under the source's Clifford normalization.

## E-027: Cutoff-kernel derivative before Figure 9.2

- Physical PDF page: 160
- Printed page: 150
- Source form: `partial_t K`
- Adopted form: `partial_t K^{-1}`
- Reason: Both terms in the preceding exact RG equation contain
  `partial_t K^{-1}`, and the internal diagram lines represent that kernel.

## E-028: Source sign in Equation (3.9)

- Physical PDF page: 30
- Printed page: 20
- Source form: `-[V'(delta/(i delta J)) + J] Z[J]`
- Source-convention correction: `-[V'(delta/(i delta J)) - J] Z[J]`
- Convention-adapted form: `[V'(delta/(i delta J)) - J] Z[J]`
- Reason: Equation (3.3) defines `Z[J]` with `exp(+i integral J phi)`; the
  time-ordering contact term changes the printed `+J` to `-J`. Converting the
  old mostly-minus d'Alembertian to the adapted mostly-plus one removes the
  source-convention overall minus.

## E-029: Time-reversed creation operator in Problem 5.3

- Physical PDF page: 69
- Printed page: 59
- Source form: `T^dagger a^dagger(p,s) T = eta_T a(-p,-s)`
- Adopted form:
  `T^dagger a^dagger(bold p,s) T = eta_T a^dagger(-bold p,-s)`
- Reason: A symmetry maps a one-particle creation operator to another creation
  operator; the undaggered right-hand side would annihilate the vacuum.

## E-030: Metric-variation normalization in Problem 7.2

- Physical PDF page: 100
- Printed page: 90
- Source form: `T_(mu nu)=(1/sqrt(-g)) delta S/delta g^(mu nu)`
- Source-convention correction: `T_(mu nu)=(2/sqrt(-g)) delta S/delta g^(mu nu)`
- Convention-adapted form:
  `T_(mu nu)=(-2/sqrt(-g)) delta S/delta g^(mu nu)`
- Reason: With the adapted mostly-plus matter action, the Hilbert definition is
  `delta S=-(1/2) integral sqrt(-g) T_(mu nu) delta g^(mu nu)`. The factor of
  two and the adapted sign give the canonical translation charge.

## E-031: Majorana-basis transformation in Appendix C

- Physical PDF page: 258
- Printed page: 248
- Source form: `S_M=2^(-1/2)(sigma_3+sigma_2) tensor 1`
- Adopted form: `S_M=2^(-1/2) [[1,sigma_2],[sigma_2,-1]]`
- Reason: In `D=4`, conjugating the displayed Dirac matrices by the source
  matrix leaves `gamma_M^2` real. The adopted unitary block matrix makes all four gamma
  matrices imaginary and gives the stated Majorana representation.

## E-032: Muon momentum in Figure 6.3

- Physical PDF page: 76
- Printed page: 66
- Source form: `K_-^\nu = (E,0,-\sqrt{E^2-m_\mu^2}\sin\theta,-\sqrt{E^2-m_\mu^2}\cos\theta)`,
  identical to the `K_+^\nu` label directly above it in the same figure
- Adopted form:
  `K_-^\nu = (E_(bold k),0,|bold k|\sin\theta,|bold k|\cos\theta)`
- Reason: The figure draws the two muons back to back about the annihilation
  vertex, and the text sets `q = p_+ + p_- = k_+ + k_-` with
  `p_\pm^\nu = (E,0,0,\pm E)`, so `q^\nu = (2E,0,0,0)` and the two muon spatial
  momenta must be equal and opposite. The printed label repeats the `K_+^\nu`
  right-hand side, which would give the pair a net spatial momentum.

## E-033: Fermion-line arrow in Figure 6.4

- Physical PDF page: 80
- Printed page: 70
- Source form: both fermion arrowheads on the one-loop vertex correction point
  inward, toward the external-photon vertex
- Adopted form: the upper (`p+q`) arrowhead is reversed, so the arrows run
  continuously along the fermion line from `p` in to `p+q` out
- Reason: Section 6.4 evaluates this graph as the one-loop correction to
  `\bar u(p+q)\Gamma^\mu u(p)`, a fermion-number-conserving vertex. Two inward
  arrows would mark the line as fermion-number violating and contradict the
  amplitude the section computes from it.

## E-034: Massless Weyl Green-function pole

- Physical PDF page: 57
- Printed page: 47
- Source form: `sigma^mu p_mu/(p^2+m^2-i epsilon)`
- Adopted form: `sigma^mu p_mu/(p^2-i epsilon)`
- Reason: The displayed Weyl equation is massless, so its inverse has its pole
  at `p^2=0`; no mass parameter occurs in the operator being inverted.

## E-035: Proca connected generating functional

- Physical PDF page: 51
- Printed page: 41
- Source form: `W_0[J]=-i/2 integral J J N/(p^2+mu^2-i epsilon)`
- Adopted form: `W_0[J]=1/2 integral J J N/(p^2+mu^2-i epsilon)`
- Reason: Chapter 3 defines `Z_0=exp(i W_0)=exp(-J D_F J/2)`, while the
  adapted Proca propagator is `D_F=-i N/(p^2+mu^2-i epsilon)`.

## E-036: Lorentz-operator conjugation in Section 4.3

- Physical PDF page: 50
- Printed page: 40
- Source form: `U^dagger a^dagger(p) U` carries `p` to `Lambda p`, followed by
  `U^dagger A(x) U=S(Lambda)A(Lambda^{-1}x)`
- Adopted form: `U a^dagger(p) U^{-1}` carries `p` to `Lambda p`, followed by
  `U A(x) U^{-1}=S(Lambda^{-1})A(Lambda x)`
- Reason: This active transformation agrees with Equation (4.1), the
  positive-frequency phase, and the mode expansion used in Problem 4.1.

## E-037: Free index in Equation (10.16)

- Physical PDF page: 238
- Printed page: 228
- Source form: `A_mu=g_1^{-1}(hat x) partial_i g_1(hat x) f(x^2)`
- Adopted form: `A_mu=g_1^{-1}(hat x) partial_mu g_1(hat x) f(x^2)`
- Reason: The left-hand side carries the free Euclidean index `mu`; the
  solution states the same gauge potential as the one-form `A=g_1^{-1} d g_1 f`.

## E-038: Gamma-matrix order in Appendix C

- Physical PDF page: 260
- Printed page: 250
- Source form: the three-gamma term in the displayed `K_4` contraction uses
  `gamma_alpha gamma_kappa gamma_nu`
- Adopted form: `gamma_kappa gamma_alpha gamma_nu`
- Reason: The Clifford recurrence fixes the displayed order. Repeated-index
  substitution distinguishes it from the printed expression.

## E-039: Anomaly-coefficient normalization in Appendix E

- Physical PDF page: 268
- Printed page: 258
- Source form: `tr({T_R^a,T_R^b}T_R^c)=i A(R)d^{abc}`
- Adopted form: `tr({T_R^a,T_R^b}T_R^c)=(1/2)A(R)d^{abc}`
- Reason: The appendix defines
  `d^{abc}=2 tr_F(T_F^a{T_F^b,T_F^c})`; the fundamental representation must
  therefore have `A(F)=1`, and the symmetric trace is real.

## E-040: Generator product in Appendix E

- Physical PDF page: 268
- Printed page: 258
- Source form: `T^aT^b=(1/(2N))delta^{ab}1_N+(d^{abc}+i f^{abc})T^c`
- Adopted form:
  `T^aT^b=(1/(2N))delta^{ab}1_N+(1/2)(d^{abc}+i f^{abc})T^c`
- Reason: Adding and subtracting the normalized commutator and anticommutator
  gives the factor `1/2` on both tensor terms.

## E-041: Longitudinal gauge pole in Appendix D

- Physical PDF page: 261
- Printed page: 251
- Source form: the Euclidean longitudinal denominator is `p_E^2+m_A^2`
- Adopted form: `p_E^2+kappa m_A^2`
- Reason: In `R_kappa` gauge the longitudinal mode has gauge-dependent mass
  squared `kappa m_A^2`, matching the continued Lorentzian propagator.

## E-042: Wick-contraction factors in Figure D.1

- Physical PDF page: 265
- Printed page: 255
- Source form: the seven displayed factors are
  `1/72, 1/36, 1/48, 1/6, 1/3, 1/9, 1/6`
- Adopted form: `1/128, 1/16, 1/48, 1/16, 1/4, 1/4, 1/6`
- Reason: Dividing the seven Wick counts
  `9, 72, 24, 72, 288, 288, 192` by `2!(4!)^2=1152` gives the adopted list.
  The printed first and fourth numerators count indistinguishable self-pairings
  twice; four other printed fractions also fail their displayed arithmetic.

## E-043: Compactness criterion in Appendix E

- Physical PDF page: 267
- Printed page: 257
- Source form: every Lie group with a faithful finite-dimensional unitary
  representation is compact
- Adopted form: every such Lie group whose image is closed is compact
- Reason: A closed subgroup of the compact group `U(N)` is compact. A faithful
  homomorphism can instead have a nonclosed dense image.

Each future entry must give the physical PDF page, printed page, source form,
adopted form, and reason.
