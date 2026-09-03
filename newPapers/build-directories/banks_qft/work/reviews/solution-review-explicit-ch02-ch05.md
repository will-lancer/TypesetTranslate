# Explicit-solution review: Chapters 2–5

Scope: numbered solutions 2.1–2.11, 3.1–3.6, 4.1–4.4, and 5.1–5.16. I compared the current solution files with the corresponding problem files, the relevant chapter and appendix text, and the current \`ERRATA.md\` ledger. All 37 solution IDs are present.

Overall: **PASS**. The repaired 3.5 generator supplies a deterministic exhaustive topology enumeration, and 5.1 now keeps the Lorentz square-root normalization in the operator law only.

## Chapter 2

- **2.1: PASS.** The determinant, time-component bound, four components, component representatives, time orientation, and spacelike sign-change arguments are correct.
- **2.2: PASS.** The differentiation uses the corrected right factor \(e^{-\ii H_0t_0}\) from E-003 and gives the interaction-picture equation with the proper initial condition.
- **2.3: PASS.** The iterated integral, time ordering, and \(n!\) conversion give the Dyson series with the correct signs.
- **2.4: PASS.** The oscillator overlap and its mode product are correct. The ultraviolet term \(-(\Delta m^2)^2/(64|\mathbf k|^4)\) gives the finite-volume threshold \(d\ge4\) recorded in E-004.
- **2.5: PASS.** Scalar covariance, the Bose locality test, the fermionic comparison, and both equal-time canonical commutators are correctly derived.
- **2.6: PASS.** The unequal-mass Fourier comparison forces equal masses and \(|\eta|=1\), after which a rephasing of \(b\) removes \(\eta\).
- **2.7: PASS.** The solution establishes Lorentz invariance of the infinite-time operator from scalar covariance, invariant measure, locality, and the endpoint limit.
- **2.8: PASS.** The Wigner rotation, massive intertwiners, Hermiticity and locality requirements, statistics choice, and ultraviolet propagator powers are handled correctly under the stated neutral-field assumptions.
- **2.9: PASS.** The explicit generator basis and component commutators agree with the source convention \(J_{ij}=+\epsilon_{ijk}J_k\).
- **2.10: PASS.** The \(ISO(2)\) little group, trivial finite-dimensional translation representation, helicity quantization, induced state law, and \(h=1,\frac32,2\) field-strength examples are correct.
- **2.11: PASS.** The creation-annihilation split, Gaussian exponent, odd-term argument, static-source limit, self-energy separation, and Yukawa dependence agree with E-005 and E-006.

## Chapter 3

- **3.1: PASS.** Spectral reconstruction is correctly restricted to the cyclic subspace, and the solution states the determinate-moment or analytic-characteristic-function condition needed to recover the ground-state wavefunction. The moment, Wigner-kernel, and potential steps are checkable.
- **3.2: PASS.** The Euclidean Gaussian, large-\(T\) delta limit, self-energy term, and Yukawa interaction agree with the source convention and the requested \(e^{-2V(R)T}\) form.
- **3.3: PASS.** The Heaviside derivatives produce the contact term with the correct sign for \(Z[J]=\langle T\exp(+\ii\int J\phi)\rangle\). The source Eq. (3.9) sign defect is now documented in E-028, and the solution states the adopted convention.
- **3.4: PASS.** The Euclidean and Minkowski tree graphs, coupling orders, tree pole and residue, LSZ reduction, \(s+t+u=4m_0^2\), center-of-mass formulas, and crossing statement are correct.
- **3.5: PASS.** The repaired solution gives the complete \((a,b)\) vertex-count classes for \(E\le8\) and \(L\le2\), defines canonical \((e,n,\ell)\) incidence records, and embeds a deterministic standard-library generator. Its loops cover every external allocation, every multigraph edge multiplicity and self-contraction pattern, and every connected topology; canonicalization removes only permutations of unmarked same-valence vertices. The emitted records contain \(|\operatorname{Aut}G|\), \(S_G\), and \(N_G\), with the geometric and Wick formulas linked explicitly. The corrected vacuum theta example has \(S_G=1/12\), and the marked example uses a valid \(E=1\) graph. The embedded code and its row-count/digest output make the exhaustive result reproducible and checkable without an external topology list.
- **3.6: PASS.** The fluctuation expansion gives vertex power \(g^{k-2}\), external lines carry no extra \(g\), and half-edge counting with \(L=I-V+1\) yields \(g^{2L-2+E}\).

## Chapter 4

- **4.1: PASS.** The boosted polarization vectors, transversality, completeness relation, and vector-field covariance follow from the stated standard boost and operator law.
- **4.2: PASS.** The Proca constraints, reduced canonical algebra, mode expansion, covariant propagator, and Feynman Green-function equation have consistent signs.
- **4.3: PASS.** The chiral fields, paired helicities, spacelike locality argument, and quantization condition are correct. The measure \(d^3p/(2|\mathbf p|)\) presumes the corresponding covariant massless operator normalization, which is implicit in the displayed field.
- **4.4: PASS.** The repaired proof uses the Chapter 2 delta normalization, the correct mass-shell delta Jacobian, unitary Wigner matrices, and the cocycle identity. The square-root factors cancel correctly.

## Chapter 5

- **5.1: PASS.** Appendix C fixes \(\sum_su\bar u=\slashed p+m\) and \(\sum_sv\bar v=\slashed p-m\), with the Fourier coefficient \((2\omega_p(2\pi)^3)^{-1/2}\) multiplying the covariant wavefunctions. The repaired solution uses square-root-free spinor intertwiners and retains one \(\sqrt{\omega_{\Lambda p}/\omega_p}\) in each delta-normalized creation-operator law. The displayed invariant-measure identity cancels that factor exactly once after the momentum change of variables, so the field covariance, canonical algebra, spin sums, and locality conclusion are consistent.
- **5.2: PASS.** The repaired block matrix in E-031 gives an explicit unitary Majorana-basis transformation, all four gamma matrices are imaginary, and the Dirac-basis adjoint relation is verified.
- **5.3: PASS.** The corrected creation-operator law is explicit, the anti-unitary phase conjugation is accounted for, and the relations \(\eta_T=\zeta_T^*\), \(\bar\eta_T=\zeta_T=\eta_T^*\) are derived. The source dagger defect is recorded in E-029.
- **5.4: PASS.** The rank-three and rank-four gamma identities, charge-conjugation parities, and \(P,T\) bilinear table are correct. The axial-current time-space \(T\) entry is repaired to \((+,-)\), with the raw \(\bar\psi\gamma_5\psi\) convention stated.
- **5.5: PASS.** The charged-sector SVD and residual Dirac phases, neutral-sector Takagi form, and stated discrete-symmetry conditions are correct under the representation assumptions.
- **5.6: PASS.** The Dirac and conserved-current spectral matrices, positivity bounds, pole residues, transverse tensor, and contact or subtraction terms are correctly stated.
- **5.7: PASS.** The covariant-momentum algebra, spin term, Wilson factor, constant-field proper-time kernel, and free-field limit are consistent after distinguishing the potential parameter \(F\) from the curl \(\mathcal F\).
- **5.8: PASS.** The Weyl-basis Clifford relations, \(\gamma_5\), \(\gamma_5^2=1\), and anticommutation proof are correct.
- **5.9: PASS.** The Grassmann Gaussian, source shift, determinant contractions, and signed fermionic Wick theorem follow from the declared ordering convention.
- **5.10: PASS.** The repaired derivation displays the Berezinian, measure orientation, factor-of-two rescaling, Pfaffian product, odd-dimensional case, and congruence check, yielding \(\det A=(\operatorname{Pf}A)^2\).
- **5.11: PASS.** The Yukawa vertex, scalar and fermion propagators, arrow ordering, external spinors, and Hermiticity convention for the pseudoscalar coupling are correct.
- **5.12: PASS.** The contraction identities, ordinary traces, \(\gamma_5\) traces, six-gamma extension, and \(\gamma_5\)-inserted contraction cover the requested Appendix C generalization.
- **5.13: PASS.** Algebraic elimination of the auxiliary fields, the five Lorentz channels, the global \(U(1)\), and the determinant-versus-inverse-determinant loop sign are correctly derived.
- **5.14: PASS.** The Gordon derivation is correct with the explicitly stated convention \(\gamma^{\mu\nu}=\frac12(\gamma^\nu\gamma^\mu-\gamma^\mu\gamma^\nu)\), matching the displayed identity and the later source use. The convention should remain cross-referenced wherever \(\gamma^{\mu\nu}\) appears.
- **5.15: PASS.** The Dirac- and Weyl-basis spinors solve their equations and have the Appendix C completeness normalization. The chosen \(\eta_s\) differs from the source convention only by allowed spin-basis phases after normalization.
- **5.16: PASS.** The repaired anti-linear-map argument uses Schur's lemma and anti-unitarity to obtain \(J^2=\pm1\) without the earlier invalid phase-rescaling step, then identifies real, pseudo-real, and conjugate-pair cases.

FINAL STATUS: PASS
