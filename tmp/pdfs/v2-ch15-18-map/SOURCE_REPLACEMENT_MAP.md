# Weinberg Volume II, Chapters 15--18: whole-parent source replacement map

Date: 2026-07-31

Scope: read-only source audit and replacement planning. This report does **not** edit the exercise edition, solutions, inventory, source ledger, or fidelity audit.

## Binding editorial rule for the rewrite

- Treat one source problem, including all of its connected subparts, as one indivisible parent exercise.
- Retain every action or Lagrangian, definition, normalization, kinematic assumption, supplied identity, hint, diagram, and dependency needed to solve the parent.
- Do not turn subparts of one parent into separate supplementary exercises, and do not fuse unrelated source parents into a synthetic omnibus problem.
- Mild adaptation means notation/convention harmonization and enough restored context to make the parent standalone. It does not mean shortening the mathematical arc.
- If a parent refers to earlier equations, diagrams, or results, import those items into the exercise or state them explicitly. A bare cross-reference is not standalone.
- A source parent may appear only once in the edition. In particular, the same Cambridge exam question must not be reused in both Chapters 15 and 17.
- The repository's source policy still controls `use_mode`. Cambridge Part III papers and unlicensed author-posted material should be recorded as `adapted`, not as verbatim-permitted, even when the mathematical structure and all substantive context are retained.
- Preserve supplied figures by redrawing them faithfully in TikZ or equivalent; do not replace a required diagram with prose.

## Current edition: highest-priority weaknesses

| Chapter | Current state | Highest-priority correction |
|---|---|---|
| 15 | 15 exercises. S15.7 is a very short adjoint-representation check; S15.11 is a very short ghost-number-current calculation. S15.13--S15.15 are substantial but are broad source-inspired editorial constructions rather than identifiable complete exercise parents. | Replace S15.7 and S15.11 first. Add complete BRST/gauge parents rather than deleting the advanced BV coverage unless an equally complete BV source parent is found. |
| 16 | 11 exercises. S16.3--S16.8 are mostly large editorial fusions: Legendre geometry, imaginary potential, Goldstone theory, anomalies, loop counting, supertraces, derivative expansion, determinants, and renormalization conditions are combined without one exact source parent. | Replace the fused items with complete Cambridge AQFT and Applications parents. S16.10 is coherent, but it is not itself traceable to an exercise parent and may be displaced by the much stronger Applications large-N problem. |
| 17 | 11 exercises. Only S17.9 (Harlow) and S17.11 (Cambridge) are already complete source parents. S17.4 and S17.10 are especially short; S17.1--S17.8 and S17.10 are broad original-inspired constructions, with S17.8 especially synthetic. | Replace short/synthetic entries with complete renormalization parents. Restore all diagrams and prerequisite formulas for the Harlow and Zhou calculations. |
| 18 | 12 exercises. S18.9, S18.10, and S18.12 are complete McGreevy parents; S18.11 is a recognizable McGreevy parent. S18.1--S18.8 are original-inspired constructions, and S18.7/S18.8 divide adjacent Wilson--Fisher material into separate mini-problems. | Replace S18.1--S18.8 selectively with whole SFT, Standard Model, and McGreevy parents. One full O(N) Cambridge parent should replace the artificial S18.7/S18.8 split. |

## Chapter 15: Non-Abelian gauge theories

### 15-A. Replace S15.7 with Cambridge AQFT 2021, Paper 304, Question 4

- Source: University of Cambridge, Part III Advanced Quantum Field Theory, 2021 Paper 304, Question 4, printed page 5.
- Official URL: https://www.maths.cam.ac.uk/postgrad/part-iii/files/pastpapers/2021/paper_304.pdf
- Local cache: `tmp/pdfs/v1-ch7-11-map/cambridge-2021-304.pdf` and `.txt`.
- Recommended use mode: `adapted`.
- Why it fits: it begins with the adjoint/fundamental representation material of S15.7, then carries it through a full gauge-invariant Lagrangian and BRST construction.

Complete parent arc to retain:

1. Four-dimensional Euclidean (SU(2)) gauge theory with a massive Dirac fermion in the fundamental and a massive real scalar in the adjoint, including the stated transformation laws, Pauli-matrix fundamental generators, epsilon-symbol adjoint generators, and the fact that the adjoint field is real.
2. Construct covariant derivatives for both matter representations and derive the gauge-field transformation.
3. Enumerate **all** gauge-invariant renormalizable Lagrangian terms and demonstrate their invariance.
4. Explain why gauge fixing is necessary; introduce ghosts, antighosts, and the Nakanishi--Lautrup field.
5. Use the supplied BRST transformations of (A_μ,c,̅c,B) to prove nilpotence on a general polynomial observable.
6. Retain the source hint using two successive Grassmann parameters.

Non-negotiable context: both masses (m,M); representation matrices and reality condition; full transformation laws; Euclidean setting; every supplied BRST rule; the successive-parameter hint. Do not reduce the parent to “show the adjoint is three-dimensional.”

Risk/QA note: the “all renormalizable terms” part requires an exhaustive term audit. If conventions are translated to the volume's mostly-plus Minkowski conventions, mark the translation visibly and check every sign rather than silently changing the source setup.

### 15-B. Replace S15.11 with Harlow QFT III, Section 5.7, Homework Problem 3

- Source: Daniel Harlow, *Relativistic Quantum Field Theory III* (2026), Section 5.7, Problem 3, printed page 63.
- Official URL: https://www.mit.edu/~harlow/HarlowQFT3.pdf
- Local cache: `tmp/pdfs/v2-quality-pass/harlow-qft3.pdf` and `.txt`.
- Recommended use mode: `adapted`.
- Why it fits: it is an exact BRST-invariance calculation and is much more useful than the current isolated ghost-number-current mini-problem.

The printed homework prompt is cross-referential. A standalone transcription must import:

1. Lorenz gauge (B^{a,x}[A]=∂^μ A^a_μ), source Eq. (5.37).
2. The general auxiliary-field gauge-fixed Lagrangian, source Eq. (5.44), including ℒ_GI, the (g^2ξ n^an_a/2) term, (n_aB^{a,x}), and the ghost/Faddeev--Popov functional-derivative term.
3. For Lorenz gauge, the explicit ghost term (-∂^μ b_aD_μc^a), source Eq. (5.42), or enough information to derive it in the exercise.
4. Every BRST transformation in source Eq. (5.47): matter, gauge field, ghost, antighost, and auxiliary field, with Harlow's Grassmann-parameter convention.
5. The actual request: verify invariance by direct calculation and **do not** use the nilpotence shortcut Eq. (5.49).

Non-negotiable context: definitions of (D_μ c^a), structure constants, Grassmann parity, and the action of the odd variation on products. Without these, the one-line source prompt repeats the exact context-omission problem identified by the user.

Risk/QA note: this parent is compact even after context restoration. It is a good direct-calculation replacement, but should not be counted as a long capstone problem.

### 15-C. Add as a new exercise: Cambridge AQFT 2023, Paper 304, Question 4

- Source: University of Cambridge, Part III Advanced Quantum Field Theory, 2023 Paper 304, Question 4, printed page 5.
- Official URL: https://www.maths.cam.ac.uk/postgrad/part-iii/files/pastpapers/2023/Paper_304.pdf
- Local cache: `tmp/pdfs/v1-ch7-11-map/cambridge-2023-304.pdf` and `.txt`.
- Recommended use mode: `adapted`.
- Suggested placement: new S15.16 rather than deleting S15.13--S15.15, because those current entries preserve BV/consistent-deformation coverage not present in this exam parent.

Complete parent arc to retain:

1. The full gauge-fixed non-Abelian Lagrangian with fermionic matter, Faddeev--Popov operator ((δG^a/δA^b_μ)D_μ^{bc}c^c), and (B^aG^a-ξ B^aB^a/2).
2. All supplied BRST transformations of (A,ψ,c,̅c,B).
3. The nilpotence proof, including the supplied Jacobi identity.
4. The gauge fermion (Ψ=̅c^a(G^a-ξ B^a/2)) and proof of invariance of the full Lagrangian.
5. The operator \hat Q and the full transition-amplitude expression involving ({Q,Ψ}).
6. The final argument that gauge-choice independence forces \hat Q to annihilate physical states.

Non-negotiable context: the matter BRST transformation; all signs in the ghost and (B)-field sector; the Jacobi identity; the operator-amplitude setup. This must remain one problem, not one “nilpotence” problem plus a separate “physical states” problem.

Risk/QA note: carefully distinguish classical BRST variation, the operator \hat Q, and graded commutators. Preserve the source's logic from Lagrangian invariance to the physical-state condition.

### 15-D. Add as a new exercise: Cambridge AQFT 2024, Paper 304, Question 4

- Source: University of Cambridge, Part III Advanced Quantum Field Theory, 2024 Paper 304, Question 4, printed page 5.
- Official URL: https://www.maths.cam.ac.uk/postgrad/part-iii/files/pastpapers/2024/Paper_304.pdf
- Local cache: `tmp/pdfs/v1-ch7-11-map/cambridge-2024-304.pdf` and `.txt`.
- Recommended use mode: `adapted`.
- Suggested placement: new S15.17.

Complete parent arc to retain:

1. The full (SU(N)) gauge-field plus fundamental-fermion Lagrangian, including the source (J_μ^aA_a^μ), index ranges, (A_μ=A_μ^aT_a), (F_μν=F_μν^aT_a), and finite gauge transformations.
2. Derive the finite and infinitesimal transformation of (F_μν), and define the structure constants from the generators.
3. Infer the covariant transformation of (J^μ) and find its fermion-bilinear form.
4. Repeat the matter analysis for fermions in the adjoint representation and construct the gauge-invariant Lagrangian.
5. Draw every diagram contributing to the gluon propagator through one loop and compare fundamental versus adjoint fermion representations without evaluating the integrals.

Non-negotiable context: source-current term, finite transformations, generator definitions, both matter representations, and the full one-loop diagram request.

Risk/QA note: the current term is written in an exam-specific compact form. Do not silently repair or delete it; clarify index contractions in an editorial note if necessary. The one-loop diagrams must be drawn, including ghost, gauge, and matter loops appropriate to the chosen gauge-fixed rules.

## Chapter 16: External-field methods

### 16-A. Replace S16.3 with Cambridge AQFT 2021, Paper 304, Question 1

- Source: University of Cambridge, Part III Advanced Quantum Field Theory, 2021 Paper 304, Question 1, printed page 2.
- Official URL: https://www.maths.cam.ac.uk/postgrad/part-iii/files/pastpapers/2021/paper_304.pdf
- Local cache: `tmp/pdfs/v1-ch7-11-map/cambridge-2021-304.pdf` and `.txt`.
- Recommended use mode: `adapted`.

Complete parent arc to retain:

1. The general Euclidean action (S[φ]) for (N) real scalar fields.
2. Define (Z[J]), explain its physical/generating role, and derive connected functions from (W[J]=-\log Z[J]).
3. Define the classical field and Legendre transform Γ; derive first- and second-derivative identities.
4. Explain mathematically and diagrammatically why (W) generates connected diagrams while Γ generates one-particle-irreducible vertices.
5. For an arbitrary invertible constant linear transformation (U), derive the source transformation and prove invariance of Γ.

Non-negotiable context: (N)-field indices, Euclidean signs, definitions of (Z,W,Φ,Γ), matrix ordering in second derivatives, and the full symmetry argument.

Risk/QA note: the source calls (W) a “Wilsonian effective action,” an unusual terminology. Retain the source equation but flag the terminology editorially rather than silently rewriting the logic. Do not append unrelated Goldstone, anomaly, or imaginary-potential material from the current synthetic S16.3.

### 16-B. Replace S16.5 with Cambridge AQFT 2025, Paper 304, Question 1

- Source: University of Cambridge, Part III Advanced Quantum Field Theory, 2025 Paper 304, Question 1, printed page 2.
- Official URL: https://www.maths.cam.ac.uk/postgrad/part-iii/files/pastpapers/2025/III_Paper_304.pdf
- Local cache: `tmp/pdfs/v1-ch7-11-map/cambridge-2025-304.pdf` and `.txt`.
- Recommended use mode: `adapted`.

Complete parent arc to retain:

1. The full massive four-dimensional Minkowski φ⁴ Lagrangian and its normalization.
2. Draw **all** diagrams through order λ² contributing to the quadratic and quartic pieces Γ₂ and Γ₄ of the quantum effective action.
3. Evaluate the one-loop Γ₄ with a cutoff.
4. Add the counterterm (-δλφ^4/4!), impose the stated zero-momentum renormalization condition, and determine the source's function (F) in the supplied form of δλ.
5. Derive the renormalized Γ₄ as a function of (s,t,u) and obtain the beta function.
6. Retain the supplied Feynman-parameter integral hint.

Non-negotiable context: the massive action, orders in λ, **both** Γ₂ and Γ₄ diagram lists, regulator, renormalization condition, Mandelstam variables, counterterm normalization, and hint.

Risk/QA note: the source uses Minkowski signs and a cutoff. Check all factors of (i), channel multiplicities, and the definition of the zero-momentum coupling. Do not omit the Γ₂ diagrams simply because the explicit calculation focuses on Γ₄.

### 16-C. Replace S16.7 with Cambridge AQFT 2025, Paper 304, Question 2

- Source: University of Cambridge, Part III Advanced Quantum Field Theory, 2025 Paper 304, Question 2, printed page 3.
- Official URL: https://www.maths.cam.ac.uk/postgrad/part-iii/files/pastpapers/2025/III_Paper_304.pdf
- Local cache: `tmp/pdfs/v1-ch7-11-map/cambridge-2025-304.pdf` and `.txt`.
- Recommended use mode: `adapted`.

Complete parent arc to retain:

1. The free scalar Lagrangian, (Z_0[J]), normalization, and explicit scalar propagator (D_F).
2. The free spinor Lagrangian, Grassmann-source functional (Z_0[η̅,η]), normalization, and explicit spinor propagator (S_F).
3. The Yukawa interaction ℒ_int (=-gψ̅φψ) and the interacting generating functional written purely as source derivatives.
4. The heavy-scalar regime (M^2gg m^2,p^2), the low-energy expansion of (D_F), and the order-(g^2) derivation of the induced four-spinor interaction.
5. Determine the induced coupling and its mass dimension.

Non-negotiable context: both free actions, all source conventions and normalizations, propagator definitions, the Yukawa action, the heavy-mass inequalities, and the requested perturbative order.

Risk/QA note: Grassmann derivative ordering and signs are part of the problem. A shortened “integrate out a heavy scalar” prompt would discard half the parent and is not acceptable.

### 16-D. Replace S16.8 with Cambridge Applications of QFT 2024, Paper 337, Question 1

- Source: University of Cambridge, Part III Applications of Quantum Field Theory, 2024 Paper 337, Question 1, printed page 2.
- Official URL: https://www.maths.cam.ac.uk/postgrad/part-iii/files/pastpapers/2024/Paper_337.pdf
- Local cache: `tmp/pdfs/v2-ch15-18-map/cambridge-2024-337.pdf` and `.txt`.
- Recommended use mode: `adapted`.

Complete parent arc to retain:

1. The full nonrelativistic complex Landau--Ginzburg Lagrangian with (iΨ^†∂_tΨ), gradient term, (r), and λ.
2. Derive particle number and use (Ψ=√ρ,e^{-iθ}) to identify the density/phase canonical pair and uncertainty relation.
3. In the broken phase, expand about the radial saddle.
4. Integrate out δρ in the path integral and obtain the derivative-expanded Goldstone EFT and sound velocity.
5. At finite temperature, use the supplied Matsubara expression for phase fluctuations and prove the supplied coth summation identity.
6. Analyze convergence and spontaneous symmetry breaking in (d=1,2,3).
7. Subtract the ultraviolet contribution and estimate the restoration temperature in (d=3).

Non-negotiable context: the first-order time derivative, phase convention, full Lagrangian, finite-temperature sum, supplied coth identity, and all three spatial dimensions.

Risk/QA note: this is deliberately nonrelativistic. Do not force it into a relativistic scalar convention or change the conjugacy structure. Keep the statistical/thermal interpretation explicit.

### 16-E. Replace S16.10 with Cambridge Applications of QFT 2023, Paper 337, Question 1

- Source: University of Cambridge, Part III Applications of Quantum Field Theory, 2023 Paper 337, Question 1, printed pages 2--3.
- Official URL: https://www.maths.cam.ac.uk/postgrad/part-iii/files/pastpapers/2023/Paper_337.pdf
- Local cache: `tmp/pdfs/v2-ch15-18-map/cambridge-2023-337.pdf` and `.txt`.
- Recommended use mode: `adapted`.

Complete parent arc to retain:

1. The full (O(N)) nonlinear-sigma-model partition function and imaginary-time action in two spatial dimensions, including (bn^2=N), the Lagrange multiplier λ, temperature (T), velocity (v), and coupling (g).
2. Integrate out bn to obtain the trace-log effective action.
3. Derive the large-(N) saddle equation, with Matsubara sum and momentum integral, using (iλ=m^2).
4. At (T=0), regulate with a cutoff, determine (g_c), derive the supplied gap form, and identify the phase for (g<g_c).
5. At finite (T), use the supplied contour/coth summation formula.
6. Perform the momentum integral, subtract the critical saddle, and derive the supplied closed form (m(T)=2T\sinh^{-1}[\tfrac12e^{Δ/2T}]), using the supplied frequency integral.
7. Analyze low- and high-temperature limits.
8. Starting from the supplied Matsubara Green function, obtain the retarded Green function, spectral weight, and quantum-critical scaling.

Non-negotiable context: the question continues onto the next printed page. Preserve both pages, every definition, both supplied integral identities, the (T=0) subtraction, and the real-time continuation.

Risk/QA note: do not stop after the trace-log or saddle equation. The spectral/quantum-critical portion is part of the same parent. This is an especially strong replacement because it connects effective action, saddle methods, and observables.

## Chapter 17: Renormalization of gauge theories

### Source reservation

Reserve Cambridge AQFT 2022 Paper 304 Question 4 for **this chapter only**. Do not also use it in Chapter 15. Chapter 15 has three other complete Cambridge gauge/BRST parents, whereas the one-loop gauge-propagator component makes this question especially useful here.

### 17-A. Replace S17.4 with Cambridge AQFT 2022, Paper 304, Question 4

- Source: University of Cambridge, Part III Advanced Quantum Field Theory, 2022 Paper 304, Question 4, printed page 5.
- Official URL: https://www.maths.cam.ac.uk/postgrad/part-iii/files/pastpapers/2022/paper_304.pdf
- Local cache: `tmp/pdfs/v1-ch7-11-map/cambridge-2022-304.pdf` and `.txt`.
- Recommended use mode: `adapted`.

Complete parent arc to retain:

1. The (SU(N)) infinitesimal gauge transformation δA (=g^{-1}∂α-i[A,α]=g^{-1}Dα), the field strength, and Hermitian-generator conventions.
2. Derive the field-strength transformation and Yang--Mills invariance.
3. Introduce (c,̅c,B), use the graded BRST product rule, and prove nilpotence from the supplied transformations.
4. Start from the supplied BRST-exact gauge-fixed Lagrangian involving a linear gauge-fixing operator (L); decide whether (sℒ=0), then expand the Lagrangian explicitly.
5. Compare Lorenz and axial choices of (L), explain every term, and draw every nonvanishing one-loop contribution to the gauge-field propagator.

Non-negotiable context: all (g)-normalizations, Hermiticity, graded rule, the complete (s)-exact expression, both gauge choices, and the diagram request.

Risk/QA note: the exam uses (L) both in gauge-fixing notation and visually close to the Lagrangian symbol. Preserve the original structure and clarify typography. Do not invent a second exercise from part (d).

### 17-B. Replace S17.7 with Cambridge AQFT 2025, Paper 304, Question 4

- Source: University of Cambridge, Part III Advanced Quantum Field Theory, 2025 Paper 304, Question 4, printed page 5.
- Official URL: https://www.maths.cam.ac.uk/postgrad/part-iii/files/pastpapers/2025/III_Paper_304.pdf
- Local cache: `tmp/pdfs/v1-ch7-11-map/cambridge-2025-304.pdf` and `.txt`.
- Recommended use mode: `adapted`.

Complete parent arc to retain:

1. The full (SU(N)) Yang--Mills plus adjoint-scalar action, including the cubic scalar interaction, covariant derivative, field strength, and finite transformations.
2. Prove covariance of (D_μφ), derive ([D_μ,D_ν]φ), prove covariance of (F_μν), and establish action invariance.
3. Use the stated generator commutator and normalization, introduce the anticommutator with (d^{abc}), and express \(\operatorname{Tr}φ^3\) in components.
4. For the gauge-fixed action (S=∫ℒ+∫ QΨ), give the BRST transformations of (A) and φ, prove invariance, and prove gauge-choice independence of gauge-invariant correlators.

Non-negotiable context: the complete action including cubic scalar term, all group identities, finite transformations, gauge fermion, and correlator argument.

Risk/QA note: check the source's scalar reality and trace normalizations before translating to chapter notation. The cubic interaction is not optional context.

### 17-C. Replace S17.10 with Harlow QFT III, Section 7.8, Homework Problem 2

- Source: Daniel Harlow, *Relativistic Quantum Field Theory III* (2026), Section 7.8, Problem 2, printed page 90, with Figure 15 and Eqs. (7.97)--(7.100) on printed page 87.
- Official URL: https://www.mit.edu/~harlow/HarlowQFT3.pdf
- Local cache: `tmp/pdfs/v2-quality-pass/harlow-qft3.pdf` and `.txt`.
- Recommended use mode: `adapted`.

The printed homework prompt is only two lines because it depends on the preceding chapter. A standalone transcription must import:

1. The bare Yang--Mills plus fermion Lagrangian and the gauge, ghost, and fermion Feynman-rule conventions from the source setup.
2. Field and coupling renormalizations, including the definitions of (Z_1,Z_2,Z_3) and (Z_{1,3g}).
3. The bare and renormalized three-gauge-field correlator relations, source Eqs. (7.97)--(7.99).
4. The target counterterm identity (δZ_{1,3g}=δZ_1+δZ_3-δZ_2), source Eq. (7.100).
5. **The complete Figure 15**, which shows the one-loop three-gauge-boson vertex diagrams. Its caption states that only four topologies are distinct, followed by permutations of attachments to the external legs.
6. Every source hint: divergent parts only; use the (Z_1) calculation as a model; the bottom three diagrams have a nontrivial symmetry factor.

Complete parent request: compute the diagrams in Figure 15 and verify Eq. (7.100).

Non-negotiable context: the figure cannot be replaced by “draw the usual diagrams.” Redraw all displayed diagrams and specify the permutation sum. State whether prior values of δZ₁, δZ₂, and δZ₃ are supplied or are to be recomputed.

Risk/QA note: this is a high-load calculation. It is an excellent capstone only if the Feynman rules, group invariants, regulator, and previously computed counterterms are restored. Otherwise it recreates the user's complaint about omitted necessary context.

### 17-D. Replace S17.3 with Zhou/Mistlberger Stanford PHYS 330, Problem Set 9, Problem 4

- Source: Kevin Zhou / Bernhard Mistlberger, Stanford PHYS 330 QFT I (2022), Problem Set 9, Problem 4, “Self-energy corrections in QED,” printed pages 3--4.
- Official URL: https://knzhou.github.io/qft/PS9.pdf
- Local cache: `tmp/pdfs/v1-ch7-11-map/zhou-ps9.pdf` and `.txt`.
- Recommended use mode: `adapted` unless explicit reusable licensing is documented.

Complete parent arc to retain:

1. The problem-set convention (d=4-2ε) and the (i0) prescription.
2. The two supplied one-loop diagrams for the electron and photon self energies in massless QED.
3. Write the spinor-matrix self energy Σ and rank-two vacuum polarization Π, excluding external-leg factors.
4. Evaluate both in dimensional regularization using the earlier problem-set integrals.
5. Use and prove the supplied Euler gamma-function integral/value and derive the stated small-ε expansion of Γ.
6. Complete the requested expansion, dropping only terms that genuinely vanish in the stated limit.

Required imported dependencies from Problems 2--3 of the same set:

- The scalar bubble master integral (I_B(a,b;p^2)) and its Feynman-parameter evaluation.
- Tadpole and tensor Passarino--Veltman reductions used in the hint, including the source equations immediately preceding Problem 4.
- Momentum-routing and measure conventions.

Non-negotiable context: both diagrams, all master integrals actually invoked, (d=4-2ε), (i0), tensor structure, and the supplied gamma-function identity. Do not write “use the previous problem” without reproducing the result.

Risk/QA note: preserve transversality of the photon result and keep matrix/tensor indices until the end. This is the strongest Kevin Zhou replacement for the chapter, but it is sequential and therefore must be made explicitly standalone.

### 17-E. Replace S17.5 with Cambridge AQFT 2021, Paper 304, Question 2

- Source: University of Cambridge, Part III Advanced Quantum Field Theory, 2021 Paper 304, Question 2, printed page 3.
- Official URL: https://www.maths.cam.ac.uk/postgrad/part-iii/files/pastpapers/2021/paper_304.pdf
- Local cache: `tmp/pdfs/v1-ch7-11-map/cambridge-2021-304.pdf` and `.txt`.
- Recommended use mode: `adapted`.

Complete parent arc to retain:

1. The full Euclidean action for two real scalar fields φ₀ and χ₀ with masses (m_0,M_0) and interaction (λ_0φ_0^2χ_0).
2. Derive the momentum-space Feynman rules.
3. At one loop, draw every 1PI diagram with one, two, or three external legs.
4. Relate the exact connected φ two-point function to the self energy Π.
5. In (d=6-ε), derive (Π_1(p^2)=(A+Bp^2)/ε+C(p^2,μ)), determining (A,B,C), with finite terms allowed in integral form.
6. Explain renormalization of the two-point function and relate the minimal-subtraction running mass to the physical mass.
7. Explain superficial degree of divergence and identify all additional counterterms needed for a fully renormalized action.
8. Retain the supplied (d)-dimensional integral formula, the gamma-function Laurent expansion, and recurrence identity.

Non-negotiable context: both fields/masses, exact interaction normalization, complete diagram census, regulator dimension, MS prescription, and all hints.

Risk/QA note: this is not gauge-specific, but it is a rigorous direct-renormalization parent that balances the chapter's gauge-heavy selection and is far stronger than the current generic invariant-counterterm composite.

## Chapter 18: Renormalization-group methods

### 18-A. Replace S18.2 with Cambridge Statistical Field Theory 2025, Paper 303, Question 2

- Source: University of Cambridge, Part III Statistical Field Theory, 2025 Paper 303, Question 2, printed page 3.
- Official URL: https://www.maths.cam.ac.uk/postgrad/part-iii/files/pastpapers/2025/III_Paper_303.pdf
- Local cache: `tmp/pdfs/v2-ch15-18-map/cambridge-2025-303.pdf` and `.txt`.
- Recommended use mode: `adapted`.

Complete parent arc to retain:

1. The cutoff scalar free energy with kinetic and mass terms and interactions represented initially by an ellipsis such as (gφ^4).
2. Explain the three Wilsonian RG steps and why they generate a flow on coupling space.
3. Define beta functions, fixed-point scaling dimensions, relevant/irrelevant/marginal couplings, critical surfaces, and universality.
4. Add both λφ³ and (gφ^4), start from small bare (μ_0^2,λ_0,g_0), and integrate the shell to find the leading mass corrections from both interactions.
5. Determine the lowest order at which λ corrects (g), draw the corresponding diagram, and determine the lowest order at which (g) corrects λ when (λ_0=0).
6. Retain the supplied Wick theorem/propagator statement and permission to leave answers in integral form.

Non-negotiable context: cutoff Λ, shell bounds, all three couplings, starting values, propagator, and mixing-order questions. Keep (a) and (b) together.

Risk/QA note: the ellipsis in part (a) becomes explicit in part (b); do not delete it or replace the source action with a different normalization.

### 18-B. Replace S18.4 with Cambridge Statistical Field Theory 2021, Paper 303, Question 3

- Source: University of Cambridge, Part III Statistical Field Theory, 2021 Paper 303, Question 3, printed page 4.
- Official URL: https://www.maths.cam.ac.uk/postgrad/part-iii/files/pastpapers/2021/paper_303.pdf
- Local cache: `tmp/pdfs/v2-ch15-18-map/cambridge-2021-303.pdf` and `.txt`.
- Recommended use mode: `adapted`.

Complete parent arc to retain:

1. The (N)-component unit-vector nonlinear sigma model bn·bn (=1) with free energy (F=(2g)^{-1}∫(∂_i n_A)^2).
2. Determine the engineering dimension of (g).
3. Parameterize bn (=(bπ,σ)) and derive the exact π action, including the nonlinear denominator.
4. Expand for small π, integrate the shell Λ/ξ to Λ, and derive the supplied running (1/g(ξ)).
5. Retain the supplied π propagator and the nontrivial field-rescaling factor (A).
6. In (d=2+ε), derive the beta function with the supplied sphere-area factor.
7. Find fixed points and, identifying (g) with temperature, determine the correlation-length exponent ν.

Non-negotiable context: unit-length constraint, (N-1) Goldstone components, exact nonlinear action, shell integral (I_d), propagator, rescaling factor, and Ω convention.

Risk/QA note: the rescaling contribution is essential to the (2-N) coefficient. A shortened engineering-dimension problem loses the central calculation.

### 18-C. Replace S18.6 with Cambridge Standard Model 2024, Paper 305, Question 2

- Source: University of Cambridge, Part III Standard Model, 2024 Paper 305, Question 2, printed page 3.
- Official URL: https://www.maths.cam.ac.uk/postgrad/part-iii/files/pastpapers/2024/Paper_305.pdf
- Local cache: `tmp/pdfs/v2-ch15-18-map/cambridge-2024-305.pdf` and `.txt`.
- Recommended use mode: `adapted`.

Complete parent arc to retain:

1. The supplied one-loop running formula for (1/g^2(μ)) with UV cutoff and (b_0).
2. The supplied (SU(N_c)) coefficient (b_0=11N_c-N_f-\tfrac12N_s), with (N_f) Weyl fermions and (N_s) fundamental scalars.
3. Derive the asymptotic-freedom condition.
4. Derive the strong-coupling/dimensional-transmutation scale.
5. Find the maximum number of Standard Model generations compatible with asymptotic freedom for both (SU(3)) and (SU(2)).
6. Starting from the unification relation (g_s^2=g_w^2=\tfrac53g_Y^2) at (M), derive the stated relation among couplings at a lower scale.
7. Show (U(1)_Y×SU(2)_w×SU(3)_s) is a subgroup of (SU(5)), then use the fundamental covariant derivative to explain the (5/3) normalization.

Non-negotiable context: Weyl-versus-Dirac counting, scalar counting, all beta coefficients, hypercharge normalization, unification scale, and the exact lower-scale relation.

Risk/QA note: do not substitute a memorized beta-function convention. The exam's (b_0) normalization differs from common textbook forms; solve in the supplied normalization and only then translate.

### 18-D. Replace S18.5 with McGreevy Physics 215C Spring 2025, Homework 7, Problem 1

- Source: John McGreevy, Physics 215C QFT, Spring 2025, Assignment 7, Problem 1, “Gross--Neveu model,” printed page 1.
- Official URL: https://mcgreevy.physics.ucsd.edu/s25/2025-215C-hw07.pdf
- Local cache: `tmp/pdfs/v2-ch15-18-map/mcgreevy-215c-s25-hw07.pdf` and `.txt`.
- Recommended use mode: `adapted` unless explicit reusable licensing is documented.

Complete parent arc to retain:

1. The source preamble explaining the connection to the (O(N)) model, BCS methods, and fermionic path integrals.
2. The full partition function and action for an (N)-vector of fermion spinors in (D) dimensions, including the ((g/N)(ψ̅_aψ^a)^2) normalization.
3. Determine the engineering dimension of (g) and show classical marginality in (D=2).
4. Use the Hubbard--Stratonovich replacement of the four-fermion term by σψ̅ψ plus σ².
5. Integrate out the fermions, obtain the saddle equation, explain large-(N) dominance, find a translation-invariant saddle, and substitute it back to identify the dynamically generated mass gap and dimensional transmutation.

Non-negotiable context: real-time (e^{iS}) convention or an explicitly declared Euclidean continuation, (N)-scaling, HS contour/sign, regulator, and translation-invariant saddle ansatz.

Risk/QA note: the source says to use steps similar to an earlier (O(N)) analysis. To make the exercise standalone without changing its arc, explicitly give the HS identity/contour and regularization convention. Do not merely say “repeat the earlier calculation.”

### 18-E. Replace the S18.7/S18.8 split with Cambridge Statistical Field Theory 2024, Paper 303, Question 3

- Source: University of Cambridge, Part III Statistical Field Theory, 2024 Paper 303, Question 3, printed page 4.
- Official URL: https://www.maths.cam.ac.uk/postgrad/part-iii/files/pastpapers/2024/Paper_303.pdf
- Local cache: `tmp/pdfs/v2-ch15-18-map/cambridge-2024-303.pdf` and `.txt`.
- Recommended use mode: `adapted`.
- Suggested edition action: use one whole parent in place of the two current adjacent Wilson--Fisher mini-problems. The chapter remains above the 10-exercise floor.

Complete parent arc to retain:

1. The full (O(N)) scalar free energy with component masses and quartic interaction.
2. Determine the symmetry and mean-field ground state.
3. Draw the leading mass and quartic corrections and compute their (N)-dependent combinatorial factors.
4. Starting from the supplied shell-flow equations with unknown coefficients (A,B), determine those coefficients and derive beta functions.
5. In (d=4-ε), find fixed points and determine ν.
6. For (N=2) with unequal component masses, draw the mean-field phase diagram, derive separate mass flows, and decide whether a mixed φ₁φ₂ term is generated.

Non-negotiable context: all component indices, supplied flow equations, both mass parameters in part (b), diagram requests, combinatorial factors, and the full phase-diagram analysis.

Risk/QA note: parts (a) and (b) are one parent. Do not preserve the current editorial split by extracting the Wilson--Fisher exponent into one problem and the unequal-mass theory into another.

## Recommended implementation order

1. Replace the unmistakably short or fused items: S15.7, S15.11, S16.3, S16.5, S16.7, S16.8, S17.3, S17.4, S17.10, S18.2, S18.4, S18.5, S18.6, and the S18.7/S18.8 pair.
2. Add the 2023 and 2024 Cambridge Chapter 15 parents so the chapter gains complete source exercises without sacrificing BV coverage.
3. Add/replace the long Applications 2023 parent in Chapter 16 only after its two-page prompt, solution, and thermal/retarded continuation have been checked as one unit.
4. Add the Harlow Figure 15 calculation only after the full figure and prerequisite (Z)-factor conventions have been recreated. It should fail fidelity review if the figure is absent.
5. Add the Zhou QED self-energy parent only after the Problem Set 9 master integrals from Problems 2--3 are embedded in the prompt or a boxed supplied-results block.
6. For every implemented parent, update exercise text and solution together, then source ledger, fidelity audit, inventory, and source-coverage validation in the repository-prescribed order.

## Fidelity gates specific to these candidates

- **Whole-parent gate:** every source subpart is represented in the exercise and answered in the solution.
- **Context gate:** every referenced action/equation/result is present locally; no unexpanded “as shown in lecture” dependency remains.
- **Figure gate:** Harlow Figure 15, Zhou's two self-energy diagrams, and every requested exam diagram census are present and legible.
- **Convention gate:** Euclidean/Minkowski, metric, (i0), generator trace, coupling, beta-function, and Grassmann-derivative conventions are declared and consistently translated.
- **No-padding gate:** no source parent is split to increase the exercise count.
- **No-collision gate:** Cambridge AQFT 2022 Q4 appears only in Chapter 17; all other exact parents likewise have one edition destination.
- **Solution gate:** long parents receive correspondingly complete solutions. A one-paragraph answer to a five- or eight-part source problem is a fidelity failure.

## Cached visual checks completed

Rendered pages in `tmp/pdfs/v2-ch15-18-map/qa/` confirm the formulas and page continuations for the Cambridge AQFT 2021/2022/2023/2025 questions, Applications 2023/2024 questions, Harlow Section 5.7 Problem 3, Harlow Figure 15 and Section 7.8 Problem 2, Zhou PS9 Problem 4, McGreevy Homework 7 Problem 1, SFT 2021/2025 questions, and Standard Model 2024 Question 2. The Harlow diagram page is `harlowqft3p87-087.jpg`; the initially rendered page 86 contains the preceding discussion, not Figure 15.
