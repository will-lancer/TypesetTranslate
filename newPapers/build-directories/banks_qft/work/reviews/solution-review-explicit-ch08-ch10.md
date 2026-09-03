# Explicit solution review: Chapters 8 and 10

Scope: solutions `8.1`--`8.15` and `10.1`--`10.5`, checked against the corresponding problem text, the Chapter 8 and Chapter 10 source sections, and `ERRATA.md`. The re-reviewed solution snapshots have SHA-256 `7b37cc8bc2089804ffec84835fd88cd013e6a2cb7769357a92c290d7d5659bfc` (Chapter 8) and `f1eed246fa2ed66769dea8c19925c1064be244552ebfe6285daa92b1884f5d17` (Chapter 10). This review is static and report-only.

Overall verdict: all 20 assigned solutions pass after the re-review. The Chapter 8 source and solution now record the Clifford normalization correction as E-026.

## Chapter 8

### 8.1: PASS

The re-review of lines 8--49 finds a coherent convention: `sX=[X,c]`, `s\varphi=-c\varphi`, `sc=-[c,c]/2`, and `sA=Dc`. The graded Leibniz calculation now gives zero, and the adjoint, ghost, anti-ghost, and Nakanishi--Lautrup transformations are nilpotent.

### 8.2: PASS

Lines 53--126 provide the BRST rules, gauge-fixed Maxwell action, Noether charge, oscillator charge, quartet pairing, and transverse cohomology requested by the source problem. Normalization and polarization signs are declared as conventions and the physical conclusion is correct.

### 8.3: PASS

The re-review of lines 145--179 finds the full vector--Goldstone--ghost--anti-ghost quartet and an image-projection argument for non-exactness. The three `p\cdot\epsilon=0` massive-vector states remain non-exact even at `\kappa=1`, and the massless and scalar cohomology conclusions follow.

### 8.4: PASS

Lines 179--262 derive the covariant-gauge propagator, remove the longitudinal contour term, pass from the single Wilson-loop trace to `R\otimes\bar R`, use the Casimir identity, and identify the singlet as the most attractive channel. The baryon `3\otimes3=\bar3\oplus6` argument is included with the correct sign.

### 8.5: PASS

Lines 265--287 correctly relate the conjugate-representation symmetric trace to its negative and use real or pseudo-real equivalence to force its vanishing for a compact group.

### 8.6: PASS

Lines 289--387 cancel the diagonal-subgroup anomaly in the block representation, give a finite Chern--Simons descent representative with stated anti-Hermitian conventions, establish right-subgroup/coset invariance, and recover the consistent fermion anomaly under left gauge transformations. The source's `M` versus `N` coset typo is handled with the correct `M`.

### 8.7: PASS

Lines 390--420 use the traceless SU(5) hypercharge generator and obtain the correct `\bar5` and `10` decompositions, left-handed identifications, and SU(5) anomaly cancellation.

### 8.8: PASS

The re-review of lines 428--504 confirms that equations (8.8.1) and (8.8.4)--(8.8.6) are explicitly scoped to the intended `N\geq5` chiral construction. The `N=3`, `N=4`, and `N=2` edge cases are identified; the `N=2` singlet, even Witten count, and pseudoreal flavor enhancement are separated from the displayed analysis.

### 8.9: PASS

The re-review of the source problem, solution lines 528--593, and ERRATA E-026 confirms the corrected definition `2a_i=\Gamma_{2i-1}+i\Gamma_{2i}`. The canonical anticommutator, Fock dimension, chiral split, and `1_5\oplus10_1\oplus\bar5_{-3}` decomposition are now consistent.

### 8.10: PASS

Lines 591--628 compute the baryon and lepton mixed SU(2) anomalies and their cancellation in `B-L`, then obtain `(B-L)=(X+2Y)/5` in the doubled-hypercharge convention and check all fields in the SO(10) `16`. The full anomaly-free interpretation uses the singlet `\nu^c` supplied by 8.9, as the solution states.

### 8.11: PASS

Lines 630--732 give the left- and right-handed tree amplitudes, the `R_\kappa` neutral propagator, the conserved massless-electron current argument for `\kappa` independence, and the longitudinal-W cancellation/equivalence-theorem behavior. Couplings and signs are consistent up to the declared common interaction convention.

### 8.12: PASS

Lines 734--777 use the Weyl block form, negative-semidefinite chiral Laplacian, paired nonzero Dirac eigenvalues, and positive mass contribution. The field-independent phase from the source's factors of `i` is explicitly isolated, matching the source's “formally positive” wording.

### 8.13: PASS

Lines 779--814 use static spatial delta-function currents, so the source static-current erratum E-006 is respected. The current version has the required positive cross term `+g^2 t_1\!\cdot t_2/(4\pi L)`, removes the covariant-gauge term by conservation, and separates the `L`-independent self-energy.

### 8.14: PASS

Lines 817--860 apply equal-time fermion anticommutators and `A^2=2A` to obtain the charged-current commutator. The result is weak-isospin third-current structure and differs from electromagnetic charge density as required.

### 8.15: PASS

Lines 862--1047 state the non-abelian contact Ward identities, derive functional gauge invariance of `W`, relate the non-standard transform to connected kernels, and construct the coset Maurer--Cartan coupling. The additional NGB vector-mass matrix and the SU(2) chiral example agree with the source conventions.

## Chapter 10

### 10.1: PASS

Lines 5--119 derive the `SO(d)` bounce equation, frictional energy loss, finite-action tail, fluctuation harmonics, `d` translational zero modes in the defining representation, and the standard single-field one-negative-mode argument under the stated monotone-bounce assumptions.

### 10.2: PASS

Lines 122--201 correctly separate spatial dimension from spacetime dimension, derive Derrick scaling for any number of scalars, compute the charged ansatz energy and charge, and show that the fixed-charge term reverses the scaling descent. The charge and Q-ball virial relation match the source convention.

### 10.3: PASS

Lines 203--287 construct lifted winding sectors, finite instanton action, the topological phase, the circle Hamiltonian, and the real-line Bloch-sector path integral. The literal coefficient of `\dot\phi` is distinguished from the normalized angular Bloch parameter, resolving the source's theta normalization.

### 10.4: PASS

Lines 289--344 correctly reinterpret the quantum-mechanical instanton as a kink/domain wall and the two-dimensional Higgs instanton as a particle or a flux string, including the charge-`m` flux `2\pi n/m`.

### 10.5: PASS

Lines 346--386 use the left/right SU(2) action on quaternionic coordinates to show that a rotation changes the instanton by a constant gauge conjugation. The field strength and all gauge-invariant contractions are therefore rotation-invariant.

FINAL STATUS: PASS
