# Implicit exercises in Tom Banks, *Modern Quantum Field Theory*

This index records the unnumbered exercises embedded in the prose. It excludes the numbered end-of-chapter problems. An entry is included when Banks directly assigns work to the reader, labels a derivation easy or obvious while leaving a step unstated, calls a result straightforward, or explicitly withholds a proof. Routine uses of words such as “simply” that carry no identifiable mathematical task are omitted.

Locations give the printed page followed by the page number in `banks-qft.pdf`. The body of the book has a ten-page offset, so printed page 1 is PDF page 11.

Source: Thomas Banks, *Modern Quantum Field Theory: A Concise Introduction* (Cambridge University Press, 2008), 281 PDF pages. The repository copy is byte-identical to `/Users/wlancer/Desktop/Physics/Subjects/qft/Books/banksQFT.pdf`. SHA-256: `31de7827e7bc636feaa7028fe4dbb63a718b3926ee43ff3d96d91185a44eafe3`.

## Chapter 2: Quantum theory of free scalar fields

1. **Printed p. 8; PDF p. 18; opening discussion of Fock space.** Supply the general argument that Lorentz-invariant local QFT in at least three spatial dimensions (D-1 >= 3, equivalently D >= 4) permits only Bose and Fermi statistics. Banks states the result and says that he will not prove it in general.

2. **Printed p. 9; PDF p. 19; before Eq. (2.5).** Verify directly on a general (k)-particle state that
   \[
   P^\mu=\int \dd^{D-1}\mathbf p\,p^\mu
   a^\dagger(\mathbf p)a(\mathbf p)
   \]
   returns the sum of the one-particle (D)-momenta.

3. **Printed p. 9; PDF p. 19; after Eq. (2.5).** Prove that the stated action of (U(\Lambda)) on delta-function-normalized one-particle states is unitary. Track the Lorentz transformation of the non-covariant spatial measure `\dd^{D-1}\mathbf p` and its delta function.

4. **Printed p. 9; PDF p. 19; footnote 1.** Derive the Fock-space inner product from the creation and annihilation algebra, starting with (a(\mathbf p)|0\rangle=0). Banks extends the assignment to every equation in the opening Fock-space subsection, so the full task also checks Eqs. (2.1)-(2.5), including the number-density and Poincare-generator formulas.

5. **Printed p. 11; PDF p. 21; after Eq. (2.15).** Obtain the iterated-integral solution of (i\partial_tU_D=W(t)U_D), including the ordered integration region and the passage to the time-ordered exponential in Eqs. (2.16)-(2.18).

6. **Printed p. 13; PDF p. 23; end of Sec. 2.1.** Fill in the general spin-statistics theorem that all integer-spin particles are bosons and all half-integer-spin particles are fermions in local QFT in D >= 4 spacetime dimensions. Banks identifies this as an omitted proof and points to Refs. [6-8].

## Chapter 3: Interacting field theory

1. **Printed p. 18; PDF p. 28; Sec. 3.1, after Eq. (3.3).** Work out the free scalar generating functional (Z[J]) by operator methods, including the creation-annihilation decomposition and the contractions that exponentiate.

2. **Printed p. 19; PDF p. 29; after Eq. (3.4).** Check the time ordering in the Schwinger-Dyson derivation. It acts on the distinguished field at (x) together with every field inserted through the expansion of the source exponential.

3. **Printed p. 21; PDF p. 31; after Eq. (3.11).** Fourier transform the finite-dimensional Schwinger-Dyson equations and verify the displayed relation
   \[
   \frac{\partial S}{\partial \phi^A}=K_{AB}\phi^B-\frac{\partial V}{\partial\phi^A},
   \]
   together with its integrated solution.

4. **Printed p. 22; PDF p. 32; Eq. (3.16).** Derive the oscillatory (n)-dimensional Gaussian integral with source, including the determinant, phase convention, and quadratic form (J K^{-1}J/2).

5. **Printed p. 22; PDF p. 32; discussion after Eq. (3.19).** Recompute the free Feynman propagator by brute-force creation and annihilation operators, then match its boundary conditions and (i\epsilon) prescription to the Schwinger-Dyson solution.

6. **Printed p. 23; PDF p. 33; imaginary-time discussion.** Derive the analytic continuation of time-ordered correlation functions to imaginary time from their spectral representation. Account for operator ordering and decay at large complex energies.

7. **Printed p. 23; PDF p. 33; same discussion.** Show order by order around free-field theory that the spectral function is analytic in its energy variables and decreases when those variables become large.

8. **Printed p. 25; PDF p. 35; perturbative expansion before Eq. (3.27).** Check that every numerator integral in the normalized functional integral carries the vacuum denominator (I_0), yielding the normalized free generating functional (Z_0[J]).

9. **Printed p. 25; PDF p. 35; Feynman-rule list.** Extend the scalar rules to a derivative interaction such as (\phi^2(\partial_\mu\phi)^2), with every derivative acting on the correct propagator argument.

10. **Printed p. 25; PDF p. 35; same list.** Generalize the rules to several scalar fields. Track species labels, allowed contractions, vertex tensors, and internal-line propagator matrices.

11. **Printed p. 25; PDF p. 35; symmetry-number paragraph.** Prove that a graph’s combinatorial factor (S_G) is the inverse of the order of its geometrical automorphism group. Match that result to a direct count of Wick contractions.

12. **Printed p. 26; PDF p. 36; continuation of the Feynman-rule list.** Derive the momentum-space and Euclidean Feynman rules from the position-space functional integral, including momentum-conservation delta functions, loop measures, derivative vertices, propagator factors, and signs.

13. **Printed p. 26; PDF p. 36; paragraph before Sec. 3.4.** Set up several sample Feynman-graph computations using Appendix D until each vertex, external leg, internal line, loop momentum, and symmetry factor can be assigned without consulting the prose. Banks calls this a point where students should stop and do exercises.

14. **Printed p. 29; PDF p. 39; Sec. 3.5.** Derive the functional inverse identity `W_2 = -Gamma_2^{-1}` from the Legendre transform. Differentiate it to obtain the three-point tree relation, then prove by induction that connected Green functions are sums of trees whose vertices are 1PI functions and whose branches are full propagators.

15. **Printed p. 33; PDF p. 43; Sec. 3.7.** Prove from Lorentz invariance that the vacuum-to-one-particle matrix element of an interpolating scalar operator has the functional form used in the LSZ derivation.

16. **Printed p. 33; PDF p. 43; footnote 10.** Extend the scalar LSZ construction to nonzero spin, supplying the polarization tensors or spinors, their normalization, the pole residue, and the external-leg amputation factors.

## Chapter 4: Particles of spin 1 and gauge invariance

1. **Printed p. 41; PDF p. 51; Proca two-point function.** Use the symmetry of the displayed Proca propagator to show that fermionic quantization of the massive vector field is inconsistent.

2. **Printed p. 41; PDF p. 51; same paragraph.** Derive the diagrammatic rules for general perturbations of the free Proca Lagrangian.

3. **Printed pp. 41-42; PDF pp. 51-52; suggested calculation.** Draw every two-, three-, and four-point diagram through one loop for
   \[
   \mathcal L_I=igB_\mu(\phi^*\partial^\mu\phi-\phi\partial^\mu\phi^*),
   \]
   including symmetry factors and momentum routing. Banks asks for graph setup only, with the loop integrals left unevaluated.

4. **Printed p. 42; PDF p. 52; Stueckelberg discussion.** Integrate by parts in the source coupling and prove that gauge invariance of (A_\mu J^\mu) requires (\partial_\mu J^\mu=0), with the stated falloff condition at infinity.

## Chapter 5: Spin-one-half particles and Fermi statistics

1. **Printed p. 44; PDF p. 54; opening paragraph.** In D=4, verify that (\epsilon_{ijk}J_{ij}\pm iJ_{0k}) form two mutually commuting copies of the (\mathfrak{su}(2)) algebra.

2. **Printed p. 48; PDF p. 58; footnote 7.** In D=4, prove that the factor (\gamma^0) in (\bar\psi=\psi^\dagger\gamma^0) is required for Lorentz invariance of the Dirac Lagrangian.

3. **Printed p. 53; PDF p. 63; CP discussion.** In D=4, prove the stated criterion that the remaining fermion Lagrangian is CP-invariant exactly when a field basis exists in which every Yukawa coupling is real.

4. **Printed p. 57; PDF p. 67; Grassmann integration.** Derive the rule that a Grassmann integral extracts the coefficient of the top monomial. Establish the sign from the ordering of the measure and variables.

## Chapter 6: Massive quantum electrodynamics

1. **Printed pp. 66-67; PDF pp. 76-77; heavy-fermion production.** Restore and calculate the term proportional to (m_e^2) that Banks drops from the spin-averaged squared annihilation amplitude.

2. **Printed p. 67; PDF p. 77; Diracology instruction.** In D=4, treat every result in Appendix C as an exercise, including results whose derivations appear there. The concrete targets are the Weyl, Dirac, and Majorana bases; Hermiticity relation (C.3); the basis of antisymmetrized gamma products; duality formulas involving (\gamma_5); trace identities; contraction identities; spinor completeness; explicit (u,v) solutions; and their normalization.

3. **Printed p. 68; PDF p. 78; end of Sec. 6.2.** In D=4, derive the high-energy scaling `sigma_tot proportional to alpha^2/E^2` from dimensions and the scale-free massless limit, then identify how masses correct this behavior.

4. **Printed p. 69; PDF p. 79; Sec. 6.3.** After the rescaling (sM^2=u), (\tau M^2=v), show that the large-mass worldline action is dominated by its free kinetic term of order (M^2). Identify the suppressed corrections from the background fields.

5. **Printed p. 71; PDF p. 81; Sec. 6.4.** Reduce the most general on-shell current vertex to the three form factors multiplying (\gamma_\mu), (\gamma_{\mu\nu}q^\nu/(2m)), and (q_\mu). Use parity, the Dirac equations, and the Gordon identity.

6. **Printed p. 72; PDF p. 82; Sec. 6.4.** Prove that current conservation removes the coefficient of (q_\mu) after the loop result has been reduced to the basis ((2p+q)_\mu,\gamma_\mu,q_\mu).

7. **Printed p. 74; PDF p. 84; end of Sec. 6.4.** In D=4, evaluate the remaining Feynman-parameter integrals at (q^2=0) and recover Schwinger’s (F_2(0)=\alpha/(2\pi)).

## Chapter 7: Symmetries, Ward identities, and Nambu-Goldstone bosons

1. **Printed p. 77; PDF p. 87; internal-symmetry Ward identities.** Starting from invariance of `Z[J]`, prove that the connected functional `W[J]` is invariant under the inverse source transformation and that the 1PI functional `Gamma[phi]` is invariant under the original field transformation.

2. **Printed p. 78; PDF p. 88; before Sec. 7.1.** Use (O(n)) symmetry, the Lehmann representation, and LSZ to determine the invariant tensor structures and crossing relations for scattering among the (n) degenerate particles created by (\phi^a). Banks assigns the scattering constraints to the reader without numbering them.

3. **Printed pp. 78-81; PDF pp. 88-91; Sec. 7.1, footnote 4.** Use D-dimensional formulas where stated, with the conformal-algebra and free Dirac/Maxwell subparts specialized to D=4. Banks assigns every unproved statement in Sec. 7.1 as an additional exercise. The section-wide assignment contains the following concrete tasks:

   - Derive the translation Ward-Takahashi identity with an insertion of (T^{\mu\nu}).
   - Prove that (T^{\mu\nu}\mapsto T^{\mu\nu}+\partial_\lambda M^{\mu\nu\lambda}), with (M^{\mu\nu\lambda}=-M^{\lambda\nu\mu}), preserves conservation and the (D)-momentum.
   - Verify general-coordinate invariance of the curved-space scalar and Maxwell actions.
   - Derive the conformal Killing transformations of (D)-dimensional Minkowski space, identify their algebra with (\mathfrak{so}(2,D)), and obtain the traceless-stress-tensor condition.
   - Show that a conformal theory with a discrete particle spectrum can contain only massless particles.
   - Establish the symmetry and conservation of the metric-variation stress tensor, its relation to the Noether tensor, and the conservation of the Lorentz currents (J^{\mu\nu\lambda}).
   - Compute the Belinfante tensor for free massless spin-one-half and spin-one theories and show that it is traceless.
   - Verify that the improved free-scalar tensor is traceless and that its improvement term breaks the constant field-shift symmetry.

4. **Printed p. 87; PDF p. 97; Sec. 7.4.** In D=4, work through the full massless-QCD example: identify (G/H), construct the nonlinear pion field and its leading invariant Lagrangian, derive the currents, and recover the soft-pion consequences described around the example.

5. **Printed p. 89; PDF p. 99; end of Sec. 7.4.** Verify that
   \[
   A_\mu{}^m=\operatorname{Tr}(t^m g^{-1}\partial_\mu g)
   \]
   transforms as an (H)-connection under the local right action (g(x)\mapsto g(x)h(x)).

## Chapter 8: Non-abelian gauge theory

1. **Printed p. 94; PDF p. 104; chapter opening.** In D=4, construct the most general perturbatively renormalizable action for scalars, fermions, and Yang-Mills fields in the stated gauge representations.

2. **Printed p. 94; PDF p. 104; footnote 1.** In D=4, prove the withheld claim that perturbative renormalizability permits charged vector fields only when they are themselves Yang-Mills gauge fields.

3. **Printed p. 97; PDF p. 107; opening of Sec. 8.2.** Derive the Feynman rules for the general gauge-invariant Lagrangian before gauge fixing, and identify the singular gauge-orbit directions that obstruct the naive propagator.

4. **Printed p. 99; PDF p. 109; BRST cohomology discussion.** Show that BRST-closed physical representatives and BRST-exact states are disjoint classes. Then study the harder statement that every BRST-invariant state belongs to one of these classes, using Refs. [48-50].

5. **Printed p. 103; PDF p. 113; end of Sec. 8.4.** Perform sample loop calculations in a non-abelian Higgs model in (R_\alpha) gauge using the rules in Appendix D. Banks leaves all explicit Higgs-model loop computations to the exercises.

6. **Printed p. 107; PDF p. 117; monopole asymptotics in Sec. 8.4.** Linearize the monopole field equations at large radius and show that the profile (f(r)) approaches its asymptotic value exponentially.

7. **Printed p. 111; PDF p. 121; lattice strong-coupling expansion in Sec. 8.5.** Prove that the dominant surface at large (g^2) is the minimal-area surface bounded by the Wilson loop and derive the resulting area law.

8. **Printed p. 116; PDF p. 126; strong-interaction chiral symmetry.** In D=4, show that the observed nonzero pion mass rules out any exact standard-model symmetry that could enforce \(\det(y_u y_d)=0\).

9. **Printed p. 116; PDF p. 126; end of Sec. 8.6.** In D=4 Minkowski space, carry out representative tree-level calculations in the (SU(2)\times U(1)) electroweak model using the listed charged-current, neutral-current, and electromagnetic couplings. Banks leaves the actual calculations to the exercises.

10. **Printed p. 118; PDF p. 128; Vafa-Witten argument before Sec. 8.8.** In D=4 Euclidean signature, establish the gauge-background-independent exponential bound on the quark propagator (S(x,0)), beginning with the perturbative and rapidly decaying-background cases that Banks calls obvious. Use the bound to show that the averaged current two-point function has no zero-momentum pole.

11. **Printed p. 120; PDF p. 130; anomaly discussion.** In D=4, prove that the difference between the covariant anomaly and the consistent anomaly is the variation of a local functional of the gauge field.

12. **Printed p. 122; PDF p. 132; consistent anomaly equation.** Verify from the group-theory trace that the gauge anomaly vanishes for the representation classes identified in the text.

13. **Printed p. 124; PDF p. 134; Wess-Zumino consistency.** In D=4, prove that no local four-dimensional action has a gauge variation equal to the consistent anomaly. Then prove the harder uniqueness statement that any Wess-Zumino-consistent anomaly differs from the displayed one by the variation of a local four-dimensional action.

14. **Printed p. 125; PDF p. 135; standard-model anomaly calculation.** Solve algebraically for the spin connection and verify its inhomogeneous local-Lorentz transformation law. Use the anomaly equations to derive quantization of all hypercharges in units of the quark hypercharge.

15. **Printed p. 127; PDF p. 137; global anomalies.** In D=4, compute the baryon-number and lepton-number anomalies and show directly that (B-L) is conserved.

16. **Printed p. 127; PDF p. 137; same discussion.** In D=4, supply the finite-temperature argument that electroweak baryon-number violation becomes unsuppressed around the electroweak scale.

17. **Printed p. 128; PDF p. 138; Wess-Zumino effective action.** In D=4, derive the Wess-Zumino Lagrangian and its anomaly-matching role, which Banks says will be investigated in the exercises.

18. **Printed pp. 129-130; PDF pp. 139-140; anomaly matching.** Complete the Vafa-Witten-style argument that massless composite baryons cannot satisfy anomaly matching for any (N,N_F) in the parity-symmetric gauge theories under discussion. Check the claim that physically consistent solutions disappear even where the algebraic matching equations have solutions.

19. **Printed p. 130; PDF p. 140; end of anomaly matching.** In D=4, derive the massless momentum-space discontinuity (\operatorname{disc}A\propto\delta(q^2)) in a three-current Green function with one anomalous current.

20. **Printed p. 132; PDF p. 142; end of Sec. 8.9.** Show in the (\kappa\to\infty) limit that the massive physical fields agree, to leading semiclassical order, with the gauge-invariant field combinations constructed from the scalar vacuum and gauge orbit.

## Chapter 9: Renormalization and effective field theory

1. **Printed p. 138; PDF p. 148; introductory RG discussion.** For the class of models named by Banks, derive the RG flow as a gradient flow and show why its general asymptotic behavior approaches a fixed point.

2. **Printed p. 138; PDF p. 148; same discussion.** Show that a fixed-point Lagrangian must be invariant under space-time dilatations and translate this into scaling dimensions for fields and operators.

3. **Printed p. 140; PDF p. 150; footnote 1.** Prove equality of the physical S-matrix computed in unitary gauge and in renormalizable (R_\kappa) gauge, while allowing their off-shell Green functions to have different ultraviolet behavior.

4. **Printed p. 145; PDF p. 155; critical phenomena.** Prove analyticity of the finite-volume free energy in couplings and temperature for a system with finitely many degrees of freedom, then identify the infinite-volume step that permits a phase transition.

5. **Printed p. 147; PDF p. 157; block-spin construction.** Show that the induced kernels (K_{n_1\ldots n_k}) have short-range correlations and justify replacing the large-block discrete variables by continuous fields.

6. **Printed p. 148; PDF p. 158; exact RG setup.** Verify that the cutoff action written with arbitrary smooth coefficient functions has a finite perturbation series term by term.

7. **Printed p. 154; PDF p. 164; mathematical QFT discussion.** Under the assumptions stated there, prove that vanishing of the integrated metric variation forces local Weyl invariance.

8. **Printed p. 155; PDF p. 165; perturbations of a fixed-point CFT.** Explicitly resum insertions of a quadratic relevant operator and show that the resulting geometric series replaces the massless propagator by the massive one.

9. **Printed p. 158; PDF p. 168; footnote 10.** In physical D=4 with d_reg=4-\varepsilon_UV, compute the two-loop 1PI four-point function in (\phi^4) theory and finish the renormalization program that the text leaves incomplete.

10. **Printed p. 165; PDF p. 175; QED renormalization setup.** In physical D=4 with d_reg=4-\varepsilon_UV, generalize the one-loop renormalization analysis from one Dirac field to arbitrary collections of charged scalar and spinor fields.

11. **Printed p. 167; PDF p. 177; photon vacuum polarization.** Prove transversality of the one-loop tensor (\Pi_{\alpha\beta}(p)) by contracting with (p^\alpha), rewriting (\slashed p) as a difference of inverse fermion propagators, and shifting the (d_{\mathrm{reg}})-dimensional loop momentum.

12. **Printed p. 168; PDF p. 178; Schwinger-parameter integral.** Reproduce the gamma-function manipulations used to perform the proper-time integral, including the recursion, reflection identity, and (\Gamma(1/2)=\sqrt\pi).

13. **Printed p. 169; PDF p. 179; photon two-point function.** Verify that the displayed vacuum-polarization expression vanishes at (p^2=0), as required by the absence of a massless pole shift.

14. **Printed p. 169; PDF p. 179; same calculation.** Show by small-(s) power counting that terms above order (p^2) are ultraviolet finite.

15. **Printed p. 172; PDF p. 182; fermion two-point function.** Check that the displayed pole terms are removed by the stated field rescaling and mass renormalization.

16. **Printed p. 172; PDF p. 182; same discussion.** Use the RG equation and QED infrared freedom to derive the gauge-dependent branch cut replacing the fermion pole in leading RG-improved perturbation theory.

17. **Printed p. 174; PDF p. 184; dimensional-regularization RGE.** Show that a (k)-loop renormalization factor can contain poles through order (k), then derive why the simple-pole residue determines the beta function and anomalous dimensions.

18. **Printed p. 178; PDF p. 188; alternative proof of QED infrared freedom.** Use four-dimensional conformal representation theory to show that all connected Green functions of (F_{\mu\nu}) above the two-point function vanish under the assumptions made in the text.

19. **Printed p. 180; PDF p. 190; charged-vector susceptibility.** Expand the (SU(2)) Yang-Mills Lagrangian into a photon and charged vector fields and verify that the charged vectors have gyromagnetic ratio (2).

20. **Printed p. 185; PDF p. 195; non-abelian vacuum polarization.** Calculate every tensor component of the one-loop gluon self-energy in a general covariant gauge and verify transversality only after summing all graphs at that order.

21. **Printed p. 187; PDF p. 197; dimensionally regulated integral table.** Derive the two displayed Minkowski-space integrals from their Euclidean continuations and explain how the numerator gamma-function argument fixes the resulting power of (U).

22. **Printed pp. 191-192; PDF pp. 201-202; Sec. 9.13.** Derive (DS=0) for S-matrix elements from the Green-function RG equations, the LSZ residues, and the first-order nature of the RG differential operator (D).

23. **Printed p. 201; PDF p. 211; Nambu-Goldstone effective theory.** In D=4, prove by derivative power counting that operators beyond the leading NGB action correct low-momentum amplitudes in a systematic expansion in (p/f).

## Chapter 10: Instantons and solitons

1. **Printed p. 206; PDF p. 216; Eq. (10.2).** Verify that the dimensionless Schrödinger equation (10.1) follows from the classical action (10.2), including the placement of every factor of (g^2).

2. **Printed p. 209; PDF p. 219; instanton collective coordinate.** Differentiate the translated instanton family and prove that \(\dot X(t)\) is a zero mode of the quadratic fluctuation operator.

3. **Printed p. 209; PDF p. 219; same discussion.** Draw the finite-dimensional analogue of a saddle-point manifold and show geometrically why the nearby measure splits into a uniform collective-coordinate direction and orthogonal Gaussian directions.

4. **Printed p. 211; PDF p. 221; footnote 3.** Repeat the periodic-potential instanton-gas calculation for the double well, enforcing the equality of instanton and anti-instanton numbers and deriving the energy splitting.

5. **Printed p. 212; PDF p. 222; normalized zero mode.** Substitute the stated \(\delta_0\) into the fluctuation equation and verify its zero eigenvalue and normalization using \(\dot x_c^{\,2}=2V\).

6. **Printed p. 213; PDF p. 223; determinant discussion.** Prove that the single-instanton translation mode is the lowest eigenfunction by applying the node theorem to the monotone wavefunction (\dot x_c).

7. **Printed p. 215; PDF p. 225; field-space bounce.** Extend the one-dimensional field-space variational argument to several fields, deriving the effective path-length variable and the equations that determine the path through field space.

8. **Printed p. 216; PDF p. 226; field-theory fluctuation operator.** Show from translation invariance and by direct substitution that the (D) functions (\partial_\mu I) are zero modes around a localized instanton.

9. **Printed p. 218; PDF p. 228; two-dimensional instanton gas.** Determine the critical value of (g^2) at which the instanton-anti-instanton relative-coordinate integral ceases to converge and relate it to the phase transition described in the text.

10. **Printed p. 220; PDF p. 230; two-dimensional Higgs instanton.** Verify that the vortex boundary conditions make finite Euclidean action possible. Then supply the harder proof that the minimum-action configuration lies within the rotationally symmetric ansatz.

11. **Printed p. 220; PDF p. 230; Wilson loop in the Higgs model.** Evaluate the Wilson-loop expectation value using Stokes’ theorem and show how a charge-(k) loop shifts the interior theta parameter by (2\pi k).

12. **Printed p. 222; PDF p. 232; magnetic charge of the monopole instanton.** Use the covariant Leibniz rule, the Bianchi identity, and singlet differentiation to derive the surface formula for the magnetic charge.

13. **Printed p. 226; PDF p. 236; Yang-Mills instantons.** In D=4 Euclidean dimensions, show in the abelian case that (F\widetilde F) is a total derivative, then reproduce the non-abelian result with matrix-valued differential forms.

14. **Printed p. 227; PDF p. 237; topology and self-duality.** Prove that every nontrivial map (S^3\to G) relevant here deforms into an (SU(2)) subgroup. For the D=4 Euclidean specialization, use the inequality from \(\int\mathrm{tr}(F\pm{}^*F)^2\ge 0\) to derive the instanton action bound and its saturation by self-dual fields.

15. **Printed pp. 228-229; PDF pp. 238-239; Hamiltonian Yang-Mills theory.** In D=4 Lorentzian space, derive Gauss’s-law constraint in temporal gauge, show that each smeared generator (G(\omega)) commutes with the Hamiltonian, and compute the theta-term modification of the abelian constraint.

16. **Printed p. 233; PDF p. 243; resolvent trace.** Derive the Lorentzian path-integral representation
   \[
   \operatorname{Tr}(z-H)^{-1}=\int[dq(t)]\,e^{iT[q]z}e^{iS[q]/g^2}
   \]
   over periodic paths, including the integration over the period and the generalization to field theory. Banks labels this derivation an exercise.

17. **Printed p. 233; PDF p. 243; solitons as particles.** Fill in the Lorentz-covariant proof that a localized static solution generates a one-particle dispersion relation (E_{\mathbf p}^2=\mathbf p^2+m^2), starting with the explicit (1+1)-dimensional boost argument.

18. **Printed p. 235; PDF p. 245; soliton collective coordinate.** Verify that the coefficient of the nonrelativistic kinetic term for the collective coordinate equals the static soliton energy.

19. **Printed p. 237; PDF p. 247; monopole topology.** Prove that the constructed map (\pi_2(G/H)\to\pi_1(H)) is a group homomorphism and establish the stated isomorphism when (G) is simply connected.

20. **Printed pp. 237-238; PDF pp. 247-248; Dirac quantization.** Generalize the (SO(3)/U(1)) argument to arbitrary (G/H), tracking the covering group, center, allowed electric weights, magnetic cocharacters, and the subgroup that becomes trivial in (\pi_1(G)).

21. **Printed p. 238; PDF p. 248; electromagnetic angular momentum.** Compute the field angular momentum of a dyon pair and recover
   \[
   \Delta \mathbf L=\frac{e_i g_j-e_j g_i}{4\pi}\,\hat{\mathbf r},
   \]
   then derive the Dirac quantization condition from half-integer angular-momentum quantization.

## Chapter 11: Concluding remarks

1. **Printed p. 243; PDF p. 253; omitted topics.** Starting from a curved space-time whose complexification has a real Euclidean section, define its Euclidean functional integral and derive the analytic continuation that produces Lorentzian correlation functions. State the geometric conditions needed for the continuation.

## Appendix C: Diracology

1. **Printed p. 248; PDF p. 258; Eq. (C.3).** In D=4 with the adopted mostly-plus Clifford algebra, verify directly in the Weyl representation that ((\gamma^\mu)^\dagger=\gamma^0\gamma^\mu\gamma^0), and show that unitary changes of gamma-matrix basis preserve the relation.

2. **Printed pp. 249-250; PDF pp. 259-260; trace and contraction identities.** In D=4 with the adopted Clifford algebra and Levi-Civita convention, continue the inductive gamma-matrix trace and contraction calculations to higher orders than those displayed. Include versions with (\gamma_5), reduce them to metric and Levi-Civita tensors, and state the recurrence used at arbitrary order.

## Appendix E: Group theory and Lie algebras

1. **Printed p. 258; PDF p. 268; anomaly coefficient.** Prove uniqueness of the symmetric invariant (d^{abc}) by decomposing the tensor product of two adjoint representations. Explain why a second adjoint occurs for (SU(N)) and why the invariant vanishes for the other compact simple Lie algebras described by Banks. For the spacetime-anomaly application, specialize to D=4.

## Coverage notes

The sweep covered all 281 PDF pages using both layout-preserving text extraction and page-image checks. Search cues included `reader`, `exercise`, `show`, `check`, `verify`, `prove`, `work out`, `fill in`, `easy`, `obvious`, `straightforward`, `clear`, and statements whose proof Banks explicitly withholds. Each candidate was read in page context. References that merely direct the reader to a numbered problem were excluded from this implicit-only index.
