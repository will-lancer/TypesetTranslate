# Explicit solution review: Chapters 6–7

Scope: numbered solutions `6.1`–`6.7` and `7.1`–`7.6`. I re-reviewed the
repaired solution snapshots against each source problem, the relevant chapter
text, Appendix C where used, the adopted conventions, and `ERRATA.md`. This
was a static, report-only review; no TeX or source file was edited.

Overall verdict: all 13 assigned solutions pass. The prior findings are
resolved: 6.3 has the corrected proper-time and curvature signs, 6.5 has the
commutator consistent with its magnetic term, 7.1 includes the independent
imaginary \(U(n)\) invariant, 7.2 follows the factor-of-two stress-tensor
erratum E-030, and 7.5 uses a declared half-current normalization throughout
the weak-current calculation.

## Chapter 6

### 6.1: PASS

Lines 6–36 give both Compton orderings, internal momenta, massive-vector
propagator, external spinors, and the Bose-symmetrized amplitude. The Ward
identity is explicitly limited to the massless-photon case, while massive
vectors are handled through physical polarizations.

### 6.2: PASS

Lines 40–122 give the crossed \(t\)-channel amplitude, conserved currents,
spin-averaged trace, center-of-mass kinematics, heavy-target limit, and the
Mott factor reducing to Rutherford’s formula. The mass and coupling factors
are consistent with the source calculation.

### 6.3: PASS

Lines 126–215 provide the determinant series, position- and momentum-space
traces, derivative expansion, and a Euclidean proper-time organization. The
repaired formula uses

\[
\operatorname{Re}\log\det\mathscr D_E=-\frac12\int_0^\infty\frac{\dd s}{s}
\operatorname{Tr}e^{-s\mathscr D_E^\dagger\mathscr D_E},
\]

and the displayed heat-kernel coefficient is
\(-F_{\mu\nu}F^{\mu\nu}/12\), consistent with
\(D_\mu=\partial_\mu+\ii A_\mu\), \(F=[D,D]/\ii\), and
\(\Omega=[D,D]=\ii F\). The source’s Hermitian matrix-valued fields and
large-mass assumptions are stated.

### 6.4: PASS

Lines 219–256 give the scalar-photon vertex, transverse equal-mass scalar
current, massless-electron spin average, \(\beta^3\) threshold behavior,
angular distribution, and integrated cross section. The electron-mass
approximation is stated and matches the source setup.

### 6.5: PASS

Lines 260–319 derive the nonrelativistic Dirac Hamiltonian and magnetic moment.
The repaired relation
\([\pi_i,\pi_j]=+\ii e\epsilon_{ijk}B_k\) agrees with
\(\pi=p-eA\) and the source convention \(F_{ij}=\epsilon_{ijk}B^k\), and it
gives the displayed \(-e\,\boldsymbol\sigma\cdot\mathbf B/(2m)\) term. The
form-factor decomposition and \(g=2[1+F_2(0)]\) relation are consistent.

### 6.6: PASS

Lines 323–352 give the Schwinger product, simplex change of variables,
\((n-1)\)-simplex Jacobian, delta constraint, and final \((n-1)!\) integral.
The positivity condition needed for the final \(s\)-integral is stated.

### 6.7: PASS

Lines 356–418 exhibit the soft eikonal virtual logarithm, the real one-photon
soft theorem, the matching \(\ln\mu\) terms, cancellation at fixed energy
resolution, and the all-orders inclusive and Faddeev–Kulish conclusions.
Finite hard-emission terms are separated from the infrared argument.

## Chapter 7

### 7.1: PASS

Lines 6–61 give the general \(O(n)\) currents and the canonical \(U(n)\)
current. The repaired \(U(n)\) discussion lists the real and imaginary parts of
\((\phi^\dagger\partial_\mu\phi)^2\), retains the imaginary invariant unless
CP is imposed, and then derives the chiral flavor symmetry and singlet axial
anomaly with its gauge-coupling convention.

### 7.2: PASS

Lines 104–200 derive the canonical and gauge-invariant stress tensors, metric
variation, conservation, translation-charge equality, and Lorentz generators.
The Hilbert tensor uses the adopted E-030 definition
\(T_{\mu\nu}=2\,\delta S/(\sqrt{-g}\,\delta g^{\mu\nu})\), and the source’s
original factor-one form is identified as the erratum. Boundary assumptions
for equality of charges are explicit.

### 7.3: PASS

Lines 204–256 find the five parameters, the allowed quadratic coefficient
\(C^\mu{}_{\nu\kappa}\), the conserved dilatation and special-conformal
charges, and representative \(\mathfrak{so}(2,4)\) commutators. The trace and
symmetry assumptions are used in the conservation check.

### 7.4: PASS

Lines 260–308 establish equal pion masses from the invariant two-point
function, decompose the four-point tensor into the three pairings, impose
permutation and crossing relations, and identify two independent physical
charge amplitudes. Common LSZ residues are stated.

### 7.5: PASS

Lines 312–447 construct the Maurer–Cartan fields, parity-selected vector and
axial couplings, Noether currents, gauge-fixed \(\Sigma\) Lagrangian, and the
\(g_A/f_\pi\) pion force. Lines 431–493 explicitly declare
\(J_L=(V-A)/2\), \(J_R=(V+A)/2\), use half-sized charged-current matrix
elements, and keep those factors consistent with
\(G_F/\sqrt2=g_W^2/(8m_W^2)\), neutron decay, pion decay, and the final width.

### 7.6: PASS

Lines 498–647 derive the component Ward identity and its converse, formulate
the stationary nonstandard transform, relate its coefficients to connected and
one-particle-irreducible kernels, establish gauge invariance of \(\Gamma\), and
write the Yang–Mills and coset couplings. The NGB-induced vector mass matrix,
left/right chiral blocks, and the \(\rho\), \(\omega\), and \(A_1\) interpretation
are included with normalization qualifications.

FINAL STATUS: PASS
