# Weinberg QFT Supplementary Exercise Source Inventory

This is the parent-level working inventory for the supplementary exercise
editions of all three volumes.  It is deliberately separate from each
volume's source ledger: the ledger records material that has actually been
used, whereas this file also records complete parent problems that were
inspected and retained or rejected.  A source is not "covered" merely because
one exercise from it has been used.

## Acceptance rule

- The unit of selection is the complete numbered parent problem.
- Preserve its setup, action or Lagrangian, conventions, definitions,
  supplied formulae, hints, figures or sufficient figure data, and every
  connected subpart under one supplementary number.
- Do not split a parent into several exercises, fuse unrelated parents, or
  shorten a parent into a topic prompt.
- Use verbatim prose only when reuse is documented.  Otherwise preserve the
  complete mathematical task with the smallest necessary independent wording
  changes.
- A selected problem is accepted only after a side-by-side source audit and a
  complete independent solution.

Status meanings: `selected` is assigned to a supplementary slot, `retain` is
a strong unused candidate, `duplicate` substantially repeats a stronger
selected parent, and `out-of-scope` is not a good fit for these volumes.

## Source-coverage register

| Source family | Material inspected | Parent-level coverage | Remaining work |
|---|---|---:|---|
| Harlow QFT I | Physics 8.323 notes, 2024 edition | Homework sections 1.6--11.3 are locally available and under parent-level review | Finish the per-problem disposition table and audit all currently used Harlow-I parents |
| Harlow QFT II | Physics 8.324 notes, Fall 2024 | Problem sections 2.5--13.7 are locally available and under parent-level review | Finish the per-problem disposition table; prioritize intact later-section parents |
| Harlow QFT III | Physics 8.325 notes, Spring 2026 | Homework/problem sections 1.6--10.7 are locally available and under parent-level review | Finish the per-problem disposition table and retain all required figure dependencies |
| McGreevy QFT | Physics 215A Fall 2023, 215B Winter 2025, and 215C Spring 2025 | 215C Assignments 1--9 and the currently used 215A/215B sheets are locally available | Complete the parent-by-parent 215A/215B register and audit older split adaptations |
| Cambridge Part III QFT | Papers 301, 2021--2025; Example Sheets 3P1a--d (Michaelmas 2024) | All exam questions and all four current example sheets are locally available as PDF and layout-preserving text | Complete parent-level disposition of the newly cached example sheets and unused exam parents |
| Cambridge Part III Advanced QFT | Papers 304, 2021--2025, plus 2020 source used in Volume II; Example Sheets 3P5b--e (2022) | All exam questions and four example sheets are locally available as PDF and layout-preserving text | Complete parent-level disposition of the example sheets and unused exam parents |
| Cambridge Part III Statistical Field Theory | Papers 303, 2021--2025; Example Sheets 3P3a--c (Michaelmas 2025) | All exam questions and three current example sheets are locally available as PDF and layout-preserving text | Complete parent-level disposition of the newly cached example sheets and unused exam parents |
| Cambridge Part III Standard Model | Papers 305, 2021--2025; Example Sheets 3P4a--d (2024/25) | All exam questions and four example sheets are locally available as PDF and layout-preserving text | Complete parent-level disposition of the newly cached example sheets and unused exam parents |
| Cambridge Part III Applications of QFT | Papers 337, 2023--2025 | All questions locally available as PDF and layout-preserving text; the official 2021/2022 paper lists do not contain this course under its later title/code | Locate and inspect the course example sheets; no earlier Paper 337 was found before the course first appears in the 2023 examination list |
| Cambridge Part III Supersymmetry | Papers 307, 2021--2025; Example Sheets 3P7a--d (archived 2015--2022) | All exam questions and four archived example sheets are locally available as PDF and layout-preserving text | Implement and source-audit selected Volume III parents; complete parent-level example-sheet disposition |
| Cambridge Part III Solitons | Paper 308 (2021), Paper 313 (2022--2025), and Example Sheet 1 | All exam questions and the currently used example-sheet parents are locally available | Implement and source-audit selected Volume II parents; inspect remaining example sheets |
| Kevin Zhou / Stanford PHYS 330 | Problem Sets 2--9, 2022 | Sets 2--9 are locally available; several complete parents are already selected | Complete per-problem disposition and redo older fragmented adaptations |

The register remains open until every row's remaining-work item has been
resolved.  The tables below are expanded source by source.

## Cambridge Part III: Advanced Quantum Field Theory

| Parent | Complete scope retained during selection | Best fit | Status |
|---|---|---:|---|
| 2019, Paper 304, Q1 | Source functional, connected and 1PI generators, diagrammatic interpretation, and exact zero-dimensional split-independence identity | V2 Ch. 16 | selected; fidelity re-audit required |
| 2021, Paper 304, Q1 | Full generating-functional and Legendre-transform problem, including first/second derivatives, connected/1PI diagram expansions, and arbitrary invertible linear symmetries | V2 Ch. 16 | selected |
| 2021, Paper 304, Q4 | Complete fundamental-fermion/adjoint-scalar (SU(2)) gauge theory, all renormalizable terms, gauge fixing, and off-shell BRST nilpotence | V2 Ch. 15 | selected |
| 2022, Paper 304, Q3 | Complete QED current-conservation, Schwinger--Dyson, Ward--Takahashi, and renormalization problem | V2 Ch. 17 | selected |
| 2022, Paper 304, Q4 | Complete Yang--Mills gauge invariance, BRST nilpotence, general linear gauge fixing, and Lorenz/axial-gauge one-loop graph problem | V2 Ch. 15 | selected |
| 2023, Paper 304, Q3 | Complete Yang--Mills plus adjoint scalar and fundamental fermion problem: field-strength covariance, component adjoint transformation, all gauge-invariant interactions through quartic order with coupling dimensions/RG behavior, and the full one-loop four-scalar 1PI topology request | V2 Ch. 17 | selected |
| 2023, Paper 304, Q4 | Complete non-Abelian BRST nilpotence, gauge-fixing-fermion construction, gauge-choice independence, and physical-state condition | V2 Ch. 15 | selected |
| 2024, Paper 304, Q3 | Complete momentum-shell integration in (d)-dimensional (Phi^3) theory through the order-(g^3) coupling flow | V2 Ch. 16 | selected |
| 2024, Paper 304, Q4 | Fundamental versus adjoint matter, gauge covariance/current construction, and every connected gluon-propagator graph through one loop | V2 Ch. 17 | selected |
| 2025, Paper 304, Q4 | Adjoint scalar gauge covariance, invariant cubic tensor, BRST rules, and gauge-fixing independence | V2 Ch. 17 | selected |

## Cambridge Part III: Statistical Field Theory and Standard Model

| Parent | Complete scope retained during selection | Best fit | Status |
|---|---|---:|---|
| SFT 2021, Paper 303, Q3 | \(O(N)\) nonlinear sigma model: engineering dimension, constrained parametrization, shell integration with supplied propagator/rescaling, beta function near two dimensions, fixed points, and \(\nu\) | V2 Ch. 18 | selected |
| SFT 2023, Paper 303, Q2 | Complete momentum-shell RG procedure; engineering and scaling dimensions of \(\phi^n(\nabla^2\phi)^m\); and every requested \(\phi^4\)-\(\phi^6\) correction to the mass flow through orders \(g_0^2\), \(\lambda_0g_0\), and \(\lambda_0\), with the supplied shell propagator | V2 Ch. 18 | selected |
| SFT 2023, Paper 303, Q3 | Full (O(N)) mean-field vacuum, gapless modes, supplied Gaussian correlator, long-distance behavior/lower critical dimension, and anisotropic three-component symmetry-breaking cases | V2 Ch. 19 | retain |
| SFT 2024, Paper 303, Q2 | Complete shell-RG setup; engineering dimensions and relevance conditions for derivative operators; anomalous-dimension graph; and all requested \(\phi^5\)-\(\phi^6\) mixing and \(\phi^4\) flow diagrams/calculations through order \(\lambda_0^2\), including the supplied graph | V2 Ch. 18 | selected |
| SFT 2025, Paper 303, Q2 | Momentum-shell RG definitions and the full \(\lambda\phi^3+g\phi^4\) correction problem with supplied shell propagator and diagram questions | V2 Ch. 18 | selected |
| SFT 2025, Paper 303, Q3 | Hyperscaling, full \(O(N)\) Goldstone analysis, and the complete \(\mathbb Z_2\times O(2)\) three-field mean-field phase diagram | V2 Ch. 19 | selected |
| Standard Model 2021, Paper 305, Q2 | Definition of anomalies, full Abelian axial-anomaly derivation with supplied gamma trace, and Standard-Model anomaly cancellation/charge relation | V2 Ch. 22 | selected |
| Standard Model 2021, Paper 305, Q3 | Classical and quantum proofs of Goldstone's theorem plus complete fundamental-scalar \(SU(3)\) Higgs theory and spectrum | V2 Ch. 21 | selected |
| Standard Model 2022, Paper 305, Q4 | Full Standard-Model anomaly cancellation, consequences, anomalous baryon number, CKM parameters, and two sources of CP violation | V2 Ch. 22 | selected |
| Standard Model 2023, Paper 305, Q4 | RG solution/QCD scale/unification relation; complete low-energy two-flavour QCD Lagrangian, accidental baryon number, chiral breaking and pion EFT; extension to strange/charm | V2 Ch. 19 | selected |
| Standard Model 2024, Paper 305, Q2 | Asymptotic freedom, strong scale, Standard-Model generation bounds, coupling relation, and (SU(5)) embedding/normalization | V2 Ch. 18 | selected |
| Standard Model 2024, Paper 305, Q3 | Arbitrary integral Standard-Model hypercharges, all anomaly equations, Diophantine reduction and uniqueness, mixed gravitational anomaly | V2 Ch. 22 | selected |
| Standard Model 2024, Paper 305, Q4 | Complete one-generation fermion content, Yukawa masses, seesaw and dimension-five description, scalar triplet charges and neutrino Majorana mass | V2 Ch. 21 | selected |
| Standard Model 2025, Paper 305, Q1 | Full Abelian Higgs spectrum, current/London penetration depth, and two-scalar global symmetry, spectrum and gauge-inequivalent vacuum manifold | V2 Ch. 21 | selected |
| Standard Model 2025, Paper 305, Q2 | Two-flavour massless QCD, classical/quantum symmetry, condensate and vacuum manifold, pion EFT through quartic order, electromagnetic gauging and pion charges | V2 Ch. 19 | selected |
| Standard Model 2025, Paper 305, Q3 | (SU(2)) gauge theory with fundamental Dirac fermions and an adjoint Weyl fermion: quantum global symmetries, all requested UV/IR 't Hooft anomalies, composite spectrum and matching | V2 Ch. 22 | selected |

## Cambridge Part III: Supersymmetry

| Parent | Complete scope retained during selection | Best fit | Status |
|---|---|---:|---|
| 2021, Paper 307, Q1 | Supersymmetric quantum mechanics action, Noether symmetry/charges, canonical quantization, differential-form realization, and supersymmetric ground states | V3 Ch. 29 | selected |
| 2021, Paper 307, Q2 | Two-dimensional \(\mathcal N=(2,2)\) \(U(1)\) gauge theory, twisted-chiral field strength, component structure, and axial anomaly | V3 Ch. 29 | selected |
| 2021, Paper 307, Q3 | Complete \((0,2)\) superspace construction with chiral and Fermi multiplets, supersymmetric actions, constraints, and scalar potential | V3 Chs. 26/30 | retain |
| 2022, Paper 307, Q1 | Chiral superspace, chiral multiplets, superpotential interactions, and nonrenormalization argument | V3 Ch. 26 | selected |
| 2022, Paper 307, Q2 | Real vector superfield, Wess--Zumino gauge, field-strength multiplet, Maxwell action and supersymmetry | V3 Ch. 27 | selected; fidelity re-audit required |
| 2022, Paper 307, Q3 | Chiral gauge theory, anomalies, low-energy spectrum and anomaly matching | V3 Ch. 29 | selected; fidelity re-audit required |
| 2022, Paper 307, Q4 | \(Sp(N_c)\) supersymmetric gauge theory, phases/conformal window and Seiberg-dual description | V3 Ch. 29 | selected; fidelity re-audit required |
| 2023, Paper 307, Q1 | Kahler potential, superpotential, component actions, supersymmetric vacua and O'Raifeartaigh-type breaking | V3 Ch. 26 | selected |
| 2023, Paper 307, Q2 | Supersymmetric QED with FI term and masses: scalar potential, vacua, moduli and Kahler metric | V3 Ch. 27 | selected |
| 2023, Paper 307, Q3 | \(SU(2)\) SQCD for several \(N_f\): classical/quantum moduli, dynamically generated superpotential and anomaly matching | V3 Ch. 29 | selected |
| 2023, Paper 307, Q4 | Seiberg duality for chiral \(SU(N)\)/Spin(8)-type theories and global-anomaly checks | V3 Ch. 29 | selected |
| 2024, Paper 307, Q1 | Full super-Poincare algebra, Coleman--Mandula restrictions, parity and boson/fermion state pairing | V3 Ch. 25 | selected |
| 2024, Paper 307, Q2 | Chiral expansion and a complete supersymmetric \(U(1)\) model: anomaly, superpotential, FI term, and supersymmetry/gauge breaking | V3 Chs. 26/27 | retain |
| 2024, Paper 307, Q3 | Supersymmetric gauge unification and MSSM running | V3 Ch. 28 | selected; fidelity re-audit required |
| 2025, Paper 307, Q1 | Renormalizable \(\mathcal N=1\) \(SU(3)\) gauge theory in superspace, representations and gauge invariance | V3 Ch. 27 | selected |
| 2025, Paper 307, Q2 | MSSM naturalness, R parity, R-parity violation/proton decay, bounds, and gauge four-point rule | V3 Ch. 28 | selected |
| 2025, Paper 307, Q3 | Full super-Poincare representation problem including the superspin Casimir | V3 Ch. 25 | selected |

## Cambridge Part III: Solitons

| Parent | Complete scope retained during selection | Best fit | Status |
|---|---|---:|---|
| 2021, Paper 308, Q1 | Complete scalar \(\phi^6\) kink, perturbing force/acceleration, and kink--antikink separation problem | V2 Ch. 23 | selected |
| 2021, Paper 308, Q2 | Vortex moduli space and low-energy scattering | V2 Ch. 23 | selected |
| 2021, Paper 308, Q3 | Skyrmion topology and rational-map construction | V2 Ch. 23 | selected |
| 2022, Paper 313, Q1 | Derrick scaling followed by the complete \(\phi^6\) kink profile and mass | V2 Ch. 23 | selected |
| 2022, Paper 313, Q2 | Abelian-Higgs vortices and Bogomolny equations/bound | V2 Ch. 23 | selected |
| 2022, Paper 313, Q3 | Hodge star, anti-self-dual Yang--Mills and its Lax formulation | V2 Ch. 23 | retain |
| 2023, Paper 313, Q1 | Scalar soliton definitions, topological sectors, first-order equations and stability | V2 Ch. 23 | selected |
| 2023, Paper 313, Q2 | Complete Abelian-Higgs vortex problem | V2 Ch. 23 | retain |
| 2023, Paper 313, Q3 | Complete instanton/self-duality problem | V2 Ch. 23 | selected |
| 2024, Paper 313, Q1 | Nonlinear Schrodinger soliton, action, conserved quantities and collective-coordinate dynamics | V2 Ch. 23 | selected |
| 2024, Paper 313, Q2 | Anti-self-dual Yang--Mills geometry and reductions | V2 Ch. 23 | retain |
| 2024, Paper 313, Q3 | Abelian-Higgs theory on the disk | V2 Ch. 23 | retain |
| 2025, Paper 313, Q1 | Complete scalar-soliton variational and profile problem | V2 Ch. 23 | selected |
| 2025, Paper 313, Q2 | Complete four-dimensional instanton problem | V2 Ch. 23 | selected |
| 2025, Paper 313, Q3 | Topological degree of smooth maps and its integral properties | V2 Ch. 23 | retain |

## Harlow parents already promoted in the current pass

| Parent | Complete scope | Best fit | Status |
|---|---|---:|---|
| QFT II, Sec. 13.7, Problem 3 | Matrix scalar Lagrangian, exact minima, generic stabilizer, Goldstone count, special vacua, and the \(SU(N)/\mathbb Z_N\) qualification | V2 Ch. 19 | selected |
| QFT II, Sec. 13.7, Problem 4 | Complete Abelian-Higgs expansion, gauge fixing, propagators and all interaction vertices | V2 Ch. 21 | selected |
| QFT II, Sec. 5.6, Problem 5 | Complete free Wess--Zumino Lagrangian and the supplied Majorana supersymmetry transformations, with the requested direct invariance proof and charge-conjugation identity | V3 Ch. 26 | selected |
| QFT III, Sec. 7.8, Problem 1 | Complex scalar contribution to the non-Abelian one-loop beta function, including both vacuum-polarization graphs, the massless seagull limit, and the source's coupling-renormalization footnote | V2 Ch. 17 | selected |
| QFT III, Sec. 7.8, Problem 2 | Counterterm relation from every diagram in Figure 15, with all definitions and hints needed to read the figure | V2 Ch. 17 | selected |
| QFT III, Sec. 9.8, Problem 1 | \(SU(3)\) triple-product decomposition and baryon-decuplet branching to \(SU(2)\) | V2 Ch. 19 | retain |
| QFT III, Sec. 9.8, Problem 3 | Full \(U(1)_L\times U(1)_R/U(1)\) coset, transformation laws, matter covariant derivative and invariant terms | V2 Ch. 19 | selected |
| QFT III, Sec. 10.7, Problem 1 | General unitarity gauge for \(G\to H\), with the complete setup and all subparts | V2 Ch. 21 | selected |

## McGreevy Physics 215C, Spring 2025

| Parent | Complete scope retained during selection | Best fit | Status |
|---|---|---:|---|
| Assignment 1, Problem 1 | Complete effective-field-theory application in quantum mechanics | V1 Ch. 12 | retain; audit current related entries |
| Assignment 1, Problem 2 | Entanglement and effective field theory, including the bonus scope | V1 Ch. 12 | retain |
| Assignment 1, Problem 3 | Lattice-fermion chain and emergence of the continuum Dirac equation | V1 Chs. 5--6 | retain |
| Assignment 2, Problem 1 | Optional anomaly warm-up | V2 Ch. 22 | duplicate of stronger parents |
| Assignment 2, Problem 2 | Full heat-kernel derivation of the two-dimensional chiral anomaly | V2 Ch. 22 | selected |
| Assignment 2, Problem 3 | Six-dimensional chiral anomaly | V2 Ch. 22 / V3 Ch. 30 | retain |
| Assignment 2, Problem 4 | Full anomaly application without gauge fields, including all subparts and domain-wall charge | V2 Ch. 23 | selected |
| Assignment 3, Problem 1 | Complete polyacetylene/dimerization problem, including bonus material and wall mode | V2 Ch. 23 | selected |
| Assignment 3, Problem 2 | Complete Standard-Model anomaly-cancellation problem, including bonus subparts | V2 Ch. 22 | selected |
| Assignment 4, Problem 1 | \(\phi^6\) deformation at the Wilson--Fisher fixed point | V2 Ch. 18 | selected |
| Assignment 4, Problem 2 | RG relevance of a particle potential and Weyl asymptotics, including the singular-potential footnote and both hints | V2 Ch. 18 | selected |
| Assignment 4, Problem 3 | Complete Coleman--Mermin--Wagner massless-scalar argument, including the extended physical discussion | V2 Ch. 19 | selected |
| Assignment 4, Problem 4 | Complete free-boson generating functional, zero mode, vertex correlators and compactification | V2 Ch. 20 | duplicate of the expanded Assignment 9 version |
| Assignment 5, Problem 1 | Wilson--Fisher order-parameter exponent at order \(\epsilon^2\) | V2 Ch. 18 | retain |
| Assignment 5, Problem 2 | \(O(N)\) Gaussian OPE, beta function, Wilson--Fisher fixed point and \(\nu\) | V2 Ch. 20 | selected |
| Assignment 5, Problem 3 | Full cubic-anisotropy RG problem: invariant operators, two-coupling beta functions, four fixed points, stability/phase diagram and fluctuation-induced first order behavior | V2 Ch. 18 | selected |
| Assignment 6, Problem 1 | Full large-\(N\) \(O(N)\) model, diagram counting, Hubbard--Stratonovich saddle in all dimension ranges and bonus \(\nu\) | V2 Ch. 18 | selected |
| Assignment 6, Problem 2 | Right-handed neutrino, tree-level matching, dimension-five operator, mass and heavy-scale bound | V3 Ch. 28 | selected; fidelity re-audit required |
| Assignment 7, Problem 1 | Complete Gross--Neveu large-\(N\) saddle and dimensional transmutation | V2 Ch. 18 | selected |
| Assignment 7, Problem 2 | Galilean transformation of a nonrelativistic field and action on the broken-phase Goldstone mode | V2 Chs. 19/21 | retain |
| Assignment 8, Problem 1 | Complete diagrammatic BCS instability of a Fermi liquid | V2 Ch. 21 | selected |
| Assignment 8, Problem 2 | Fermion propagator in a metal, including bonus scope | V2 Ch. 20/21 | retain |
| Assignment 9, Problem 1 | Hohenberg--Mermin--Wagner--Coleman fact from the massless two-dimensional scalar | V2 Ch. 19 | duplicate of Assignment 4, Problem 3 |
| Assignment 9, Problem 2 | Free-boson generating functional with zero mode, all warnings and cultural remarks, \(N\)-vertex correlator, scaling and compact boson | V2 Ch. 20 | selected |
| Assignment 9, Problem 3 | Stress-tensor OPE, infinitesimal and finite Schwarzian transformations, cylinder Casimir energy and optional composition check | V2 Ch. 20 | selected |
| Assignment 9, Problem 4 | Compact-boson radius and full \(SU(2)_1\) current algebra, normalization footnote, OPE and bonus affine modes | V2 Ch. 20 | selected |
| Assignment 9, Problem 5 | Virasoro-unitarity proof of positivity of \(c\) and primary weights | V2 Ch. 20 | selected |
