# Volume I, Chapters 7--11: whole-parent replacement map

This is a discovery map only. It does not alter the exercise edition, solutions,
ledger, or fidelity records. Each recommendation replaces the named supplementary
exercise in full; do not split a source parent into several numbered exercises.

## Fidelity and reuse boundary

- Cambridge past papers carry an explicit University of Cambridge notice that they
  may not be reproduced without permission. Treat every Cambridge item below as
  `adapted`, even when its mathematical architecture is retained closely.
- The author-posted Harlow, McGreevy, and Zhou files do not display an affirmative
  reuse licence in the inspected problem pages. Under the project's current policy,
  classify them as `adapted` unless separate permission is documented.
- For all sources, preserve the whole parent: introductory motivation, action or
  Hamiltonian, conventions, every subpart, supplied identities/data, figures,
  footnotes, and hints. Translate only notation/signature and document every such
  translation.
- Cambridge paper numbers and page locators below refer to the printed page number.
  Harlow locators also use the printed page number. McGreevy and Zhou page locators
  use the page number printed in the assignment.

## Chapter 7: The Canonical Formalism

### 7A. Replace S.7.6 with Cambridge Part III QFT 2025, Paper 301, Question 2

- **Source:** University of Cambridge, Mathematical Tripos Part III, *Quantum Field
  Theory*, Paper 301 (2025), Question 2, printed p. 3, parts (a)(i)--(v) and
  (b)(i)--(ii).
- **Primary URL:**
  https://www.maths.cam.ac.uk/postgrad/part-iii/files/pastpapers/2025/III_Paper_301.pdf
- **Whole-parent content:** the most general quadratic massive-vector Lagrangian
  with coefficients `a,b,c`; reduction up to total derivatives to the starred
  Lagrangian; equations of motion; Noether energy--momentum tensor and Hamiltonian;
  positivity analysis; the condition enforcing `partial_mu V^mu=0`; transverse plus
  longitudinal decomposition `V^mu=A^mu+partial^mu pi`; equations for both modes;
  and the supplied two-pole propagator for `pi` with its Green-function hint.
- **Imports/cross-references:** none external. The starred reduced Lagrangian and the
  full displayed `pi` propagator are internal and must be retained verbatim in
  mathematical content. Keep the hint that the propagator may be treated as a
  Green function.
- **Why this target:** S.7.6 is an editorial three-part constraint sampler. This
  Cambridge parent is a coherent canonical stability/positivity problem with the
  complete Lagrangian and a substantial Hamiltonian calculation.

### 7B. Replace S.7.7 with McGreevy 215A Fall 2023, Assignment 6, Problem 3

- **Source:** John McGreevy, UC San Diego Physics 215A, Fall 2023, Assignment 6,
  Problem 3, "Recovering non-relativistic quantum mechanics," printed pp. 1--2,
  parts (a)--(c).
- **Primary URL:**
  https://mcgreevy.physics.ucsd.edu/f23/2023-215A-hw06.pdf
- **Whole-parent content:** the nonrelativistic complex-field limit
  `Phi=sqrt(2m)e^{-imt} Psi`, the slow-field assumption, both mode expansions,
  the second-quantized momentum operator, the position operator, the localized
  one-particle state, a general one-particle wave packet, and the derivation of the
  usual `-i partial_i` and multiplication actions on its wavefunction.
- **Imports/cross-references:** none external, provided the introductory limit,
  both mode expansions, definitions of `P^i`, `X^i`, `|x>`, and `|psi>` are all
  retained. Do not reduce the problem to only the final commutators.
- **Why this target:** S.7.7 is an abstract mini-proof about reduced Poisson geometry.
  McGreevy's intact parent connects canonical charges to ordinary one-particle
  quantum mechanics and is both more physical and more self-contained.

### 7C. Replace S.7.8 with Cambridge Part III QFT 2025, Paper 301, Question 4

- **Source:** University of Cambridge, Mathematical Tripos Part III, *Quantum Field
  Theory*, Paper 301 (2025), Question 4, printed p. 6, parts (a)--(d), including the
  boxed graphical hint.
- **Primary URL:**
  https://www.maths.cam.ac.uk/postgrad/part-iii/files/pastpapers/2025/III_Paper_301.pdf
- **Whole-parent content:** the free massive-scalar Lagrangian, field redefinition
  `Phi=phi+lambda phi^2`, complete transformed Lagrangian, momentum-space rules,
  all connected leading diagrams for `phi phi -> phi phi`, and the explicit
  cancellation of the on-shell amplitude.
- **Imports/cross-references:** none external. The source hint is indispensable:
  reproduce its derivative three-scalar vertex with the three labelled momenta,
  momentum-conserving delta function, and warning about identical scalars. This is
  a genuine source figure and must be redrawn, not summarized in prose.
- **Why this target:** S.7.8 currently isolates only the equation-of-motion operator
  identity. The exam parent tests the full equivalence-theorem mechanism, including
  the induced interactions and their scattering cancellation.

### 7D. Replace S.7.10 with Cambridge Part III Applications of QFT 2024, Paper 337,
Question 2

- **Source:** University of Cambridge, Mathematical Tripos Part III,
  *Applications of Quantum Field Theory*, Paper 337 (2024), Question 2, printed
  p. 3, parts (a)--(h).
- **Primary URL:**
  https://www.maths.cam.ac.uk/postgrad/part-iii/files/pastpapers/2024/Paper_337.pdf
- **Whole-parent content:** ferromagnetic `SU(2)` symmetry; constrained unit vector
  `n`; failure of a first-order term written directly in `n`; `CP^1` variables
  `n^i=z^dagger sigma^i z`; their redundancy; the Wess--Zumino term; the supplied
  spinor parametrization; quadratic canonical fluctuations; spin-wave dispersion;
  retarded Green function and spectral weight; fluctuation--dissipation theorem;
  damping with a causal pole prescription; the supplied static structure factor;
  and large-distance correlations.
- **Imports/cross-references:** none external. Retain every displayed parametrization,
  the exact supplied `S(k)` expression, and the instruction that the Wess--Zumino
  coefficient need not be fixed. No source figure occurs.
- **Why this target:** S.7.10 is a three-part synthetic sigma-model exercise. This is
  a single deep parent that carries canonical first-order dynamics all the way to a
  measurable response function.

### 7E. Replace S.7.11 with Harlow QFT I, Section 3.8, Problem 4

- **Source:** Daniel Harlow, *Lecture Notes for Physics 8.323: Relativistic Quantum
  Field Theory I* (2024), Section 3.8, Homework Problem 4, printed p. 44.
- **Primary URL:** https://www.mit.edu/~harlow/HarlowQFT1.pdf
- **Whole-parent content:** derive the oscillator algebra for a complex scalar from
  its field expansion and equal-time commutators; construct the Hamiltonian and
  global `U(1)` charge; identify the charges of particles and antiparticles.
- **Imports/cross-references:** **mandatory.** The printed problem directly invokes
  Eq. (3.64), Eq. (3.66), and the previous homework. Import: the complex-scalar
  Lagrangian (3.62); the complete field expansion (3.64) with independent `a_p` and
  `b_p`; `Pi=dot Phi^dagger` (3.65); both equal-time commutators and the statement
  that all others vanish (3.66); and the symmetry `phi'(x)=e^{i theta}phi(x)` together
  with the Noether charge convention established in Section 2.6 Problem 5. Without
  these, reject the candidate as context-deficient.
- **Why this target:** S.7.11 is another synthetic geometry sampler. Harlow's actual
  homework is a compact but complete canonical-field calculation with an immediate
  particle interpretation.

## Chapter 8: Electrodynamics

### 8A. Replace S.8.1 with Cambridge Part III QFT 2024, Paper 301, Question 1

- **Source:** University of Cambridge, Mathematical Tripos Part III, *Quantum Field
  Theory*, Paper 301 (2024), Question 1, printed p. 2, parts (a)--(d).
- **Primary URL:**
  https://www.maths.cam.ac.uk/postgrad/part-iii/files/pastpapers/2024/Paper_301.pdf
- **Whole-parent content:** Proca Lagrangian; loss of gauge invariance; equations of
  motion and transversality; stress tensor and positive on-shell energy; plane waves
  and three polarizations; and construction of the vector propagator as the inverse
  of the differential operator.
- **Imports/cross-references:** none external. Retain the propagator/Green-function
  hint and the exact sign/normalization of the Proca action.
- **Why this target:** S.8.1 is an editorial merger of two Coulomb-gauge derivations.
  The Proca question is a complete benchmark for vector-field dynamics,
  polarizations, positivity, and propagators.

### 8B. Replace S.8.3 with Zhou/Mistlberger PHYS 330, Problem Set 8, Problem 3

- **Source:** Bernhard Mistlberger and Kevin Zhou, Stanford PHYS 330, Fall 2022,
  Problem Set 8, Problem 3, "Electron-positron annihilation to muons," printed
  pp. 2--3, parts (a)--(d).
- **Primary URL:** https://knzhou.github.io/qft/PS8.pdf
- **Whole-parent content:** full process and masses; leading QED amplitude; complete
  spin sum/average in `s,t,u` without dropping the electron mass; center-of-mass
  angular form; differential and total cross sections.
- **Imports/cross-references:** **mandatory.** Import the center-of-mass two-body
  formula cited as Peskin--Schroeder Eq. (4.84), rather than leaving a bare book
  reference:
  `d sigma/d Omega = [1/(64 pi^2 s)] (|p_f|/|p_i|) overline{|M|^2}`
  in the source's conventions, together with the identical-particle caveat (not used
  here). Retain the definitions of `s,t,u`, all four masses/momenta, the instruction
  to keep `m_e`, and the note that Peskin--Schroeder drops it.
- **Why this target:** S.8.3 is an artificial two-item threshold/R-ratio exercise.
  This is a classic complete QED calculation with all kinematic stages intact.

### 8C. Replace S.8.4 with Cambridge Part III QFT 2023, Paper 301, Question 4

- **Source:** University of Cambridge, Mathematical Tripos Part III, *Quantum Field
  Theory*, Paper 301 (2023), Question 4, printed p. 5.
- **Primary URL:**
  https://www.maths.cam.ac.uk/postgrad/part-iii/files/pastpapers/2023/Paper_301.pdf
- **Whole-parent content:** definition of gauge symmetry; complete spinor-QED
  Lagrangian and proof of gauge invariance; covariant-gauge Feynman rules; all
  labelled tree diagrams and amplitudes for Bhabha scattering, pair annihilation to
  two photons, and positron Compton scattering.
- **Imports/cross-references:** none external. Preserve the direction to identify all
  initial/final quantum numbers and label each diagram. Every requested topology
  belongs to the parent; do not turn the three processes into separate exercises.
- **Why this target:** S.8.4 is only the scalar-QED Ward cancellation. The Cambridge
  parent is a broad, standard, high-value electrodynamics examination problem.

### 8D. Replace S.8.5 with Harlow QFT II, Section 9.8, Problem 5

- **Source:** Daniel Harlow, *Lecture Notes for Physics 8.324: Relativistic Quantum
  Field Theory II* (Fall 2024), Section 9.8, Problem 5, printed p. 110.
- **Primary URL:** https://www.mit.edu/~harlow/HarlowQFT2.pdf
- **Whole-parent content:** the complete scalar-electrodynamics Lagrangian; Maxwell
  current; charged-scalar equation; canonical momenta; current in phase-space
  variables; and proof of the stated local gauge transformation.
- **Imports/cross-references:** none external: the action and gauge transformations
  are printed in the problem. Retain the precise covariant-derivative signs and do not
  add unrelated vertex derivations to this parent.
- **Why this target:** S.8.5 synthesizes several lecture-note sections. Harlow's actual
  homework has a clean source boundary and the full action needed for every part.

### 8E. Replace S.8.12 by retranscribing Zhou/Mistlberger PS8, Problem 4 in full

- **Source:** Bernhard Mistlberger and Kevin Zhou, Stanford PHYS 330, Fall 2022,
  Problem Set 8, Problem 4, "Nonminimal couplings," printed p. 3, parts (a)--(d).
- **Primary URL:** https://knzhou.github.io/qft/PS8.pdf
- **Whole-parent content:** physical interpretation of the Pauli magnetic moment,
  the `gamma_5` dipole term, the dimension-six vector-current operator, and the
  dimension-six axial-current operator, all in the nonrelativistic limit.
- **Imports/cross-references:** **mandatory.** This parent explicitly depends on
  Problem 1. Import Problem 1's interaction Hamiltonian (Eq. 1), relativistic
  one-particle normalization and classical-field assumption, the nonrelativistic
  Hamiltonian (Eq. 3), the matching equation with its factor `2m` (Eq. 4), and the
  Gordon identity from PS7 Problem 2(a). Preserve the statement that qualitative
  answers with justification suffice. The current S.8.12 omits most of this setup.
- **Why this target:** this is not a new source choice; it is a required restoration of
  the same cited parent. The current adaptation is too compressed to support the
  requested nonrelativistic interpretation.

## Chapter 9: Path-Integral Methods

### 9A. Replace S.9.3 with Harlow QFT I, Section 5.8, Problem 3

- **Source:** Daniel Harlow, *Lecture Notes for Physics 8.323: Relativistic Quantum
  Field Theory I* (2024), Section 5.8, Homework Problem 3, printed p. 68.
- **Primary URL:** https://www.mit.edu/~harlow/HarlowQFT1.pdf
- **Whole-parent content:** calculate the simple-harmonic-oscillator propagator by
  expanding about the classical path, Fourier expanding Dirichlet fluctuations, and
  fixing the determinant prefactor by the free-particle limit.
- **Imports/cross-references:** **mandatory.** Import the full Hamiltonian
  `H=P^2/(2m)+(k/2)Q^2`, the fixed endpoint/time notation, and the result of the
  preceding free-particle Problem 2,
  `K_0(q',T;q,0)=sqrt[m/(2 pi i T)] exp[i m(q'-q)^2/(2T)]`, including its phase
  prescription. Retain the source hint about separating `q_cl+delta q`, Fourier
  modes, and fixing all `k`-independent factors only at the end.
- **Why this target:** S.9.3 merges three distinct MIT-derived tasks. Harlow's one
  parent is the canonical determinant calculation and has a single coherent endpoint.

### 9B. Replace S.9.4 with Cambridge Part III AQFT 2023, Paper 304, Question 1

- **Source:** University of Cambridge, Mathematical Tripos Part III, *Advanced
  Quantum Field Theory*, Paper 304 (2023), Question 1, printed p. 2, parts (a)--(c).
- **Primary URL:**
  https://www.maths.cam.ac.uk/postgrad/part-iii/files/pastpapers/2023/Paper_304.pdf
- **Whole-parent content:** unit-mass harmonic-oscillator action; propagator;
  source-dependent Gaussian generating functional; cubic anharmonic interaction;
  derivative representation of the interacting functional and convergence comment;
  Feynman rules; and all connected two-point terms through order `lambda^2`, with
  a divergence assessment.
- **Imports/cross-references:** none external. Retain the displayed target propagator,
  `Z_0[J]`, and the exact normalization of the cubic action.
- **Why this target:** S.9.4 is only a contour integral. This exam parent retains the
  full bridge from the Gaussian path integral to perturbation theory.

### 9C. Replace S.9.7 with McGreevy 215A Fall 2023, Assignment 5, Problem 2

- **Source:** John McGreevy, UC San Diego Physics 215A, Fall 2023, Assignment 5,
  Problem 2, "The propagator is a Green's function," printed pp. 1--2,
  parts (a)--(d).
- **Primary URL:**
  https://mcgreevy.physics.ucsd.edu/f23/2023-215A-hw05.pdf
- **Whole-parent content:** retarded Klein--Gordon propagator and its delta-function
  normalization; sourced mode expansion; time-ordered propagator as a Green
  function; and the path-integral/contact-term interpretation.
- **Imports/cross-references:** the problem is self-contained only if both propagator
  definitions, the definition of the wave operator, the source term `phi j`, both
  equal-time canonical commutators, and the full hint about derivatives acting on
  time ordering are retained. Part (d) is a forward pointer, not a separate problem.
- **Why this target:** S.9.7 is one short contact-term calculation. McGreevy's complete
  parent adds the causal propagator, source response, and the operator/path-integral
  connection.

### 9D. Replace S.9.10 with McGreevy 215A Fall 2023, Assignment 5, Problem 3

- **Source:** John McGreevy, UC San Diego Physics 215A, Fall 2023, Assignment 5,
  Problem 3, "Schwinger-Dyson equations," printed pp. 2--3, parts (a)--(c).
- **Primary URL:**
  https://mcgreevy.physics.ucsd.edu/f23/2023-215A-hw05.pdf
- **Whole-parent content:** functional integration by parts explained through a
  spacetime lattice; derivation of the basic Schwinger--Dyson identity; the contact
  equation for the free two-point function; and its three-point generalization.
- **Imports/cross-references:** retain the complete measure-independence argument,
  the ordinary finite-dimensional integration-by-parts analogue, the normalized
  `1/Z` expectation in Eq. (2), the `i epsilon` prescription, and the target Eq. (3).
  No outside equation is required if these source displays are copied into the prompt.
- **Why this target:** S.9.10 is an abbreviated Wick-topology exercise. This parent is
  a fundamental nonperturbative identity with all conceptual context supplied.

### 9E. Replace S.9.18 with Cambridge Part III AQFT 2024, Paper 304, Question 1

- **Source:** University of Cambridge, Mathematical Tripos Part III, *Advanced
  Quantum Field Theory*, Paper 304 (2024), Question 1, printed p. 2,
  parts (a)--(d).
- **Primary URL:**
  https://www.maths.cam.ac.uk/postgrad/part-iii/files/pastpapers/2024/Paper_304.pdf
- **Whole-parent content:** the `phi^n` Lagrangian and normalized generating
  functional; leading connected vacuum graphs for `n=5`; exact Gaussian functional
  for `n=2` with `Z_2[0]=1`; functional-derivative representation for general `n`;
  assumptions behind it; and the explicit first nontrivial-order consistency check.
- **Imports/cross-references:** none external. Retain `L_n`, the definition of
  `Z_n[J]`, the normalization condition, and the exact functional differential
  operator. Diagrams requested in part (a) belong to the parent.
- **Why this target:** S.9.18 is a synthetic Gaussian checklist. The exam problem
  gives it a concrete interacting generating-functional arc.

## Chapter 10: Non-Perturbative Methods

### 10A. Replace S.10.3 with Cambridge Part III AQFT 2022, Paper 304, Question 3

- **Source:** University of Cambridge, Mathematical Tripos Part III, *Advanced
  Quantum Field Theory*, Paper 304 (2022), Question 3, printed p. 4,
  parts (a)--(d).
- **Primary URL:**
  https://www.maths.cam.ac.uk/postgrad/part-iii/files/pastpapers/2022/paper_304.pdf
- **Whole-parent content:** Euclidean QED Lagrangian; global `U(1)` current and its
  conservation; current-insertion Schwinger--Dyson equation; momentum-space
  Ward--Takahashi identity for the exact vertex and propagator; renormalization
  implications; and what remains true nonperturbatively.
- **Imports/cross-references:** none external. Preserve the full Euclidean action,
  the contact-term identity, the exact momentum routing in the displayed
  Ward--Takahashi identity, and the request for a nonperturbative conclusion.
- **Why this target:** S.10.3 is a source-inspired derivation assembled from prose.
  Cambridge Question 3 is the exact complete parent for precisely this topic.

### 10B. Replace S.10.5 with Cambridge Part III QFT 2025, Paper 301, Question 3

- **Source:** University of Cambridge, Mathematical Tripos Part III, *Quantum Field
  Theory*, Paper 301 (2025), Question 3, printed pp. 4--5, parts (a)(i)--(iv)
  and (b).
- **Primary URL:**
  https://www.maths.cam.ac.uk/postgrad/part-iii/files/pastpapers/2025/III_Paper_301.pdf
- **Whole-parent content:** scalar plus Dirac free theory; scalar Yukawa interaction;
  classical equations and three Schwinger--Dyson equations; LSZ construction of
  `phi -> psi psi-bar`; leading correlator and S-matrix from Schwinger--Dyson;
  complete spin sum; pseudoscalar interaction; comparison of scalar and
  pseudoscalar decay observables.
- **Imports/cross-references:** none external because the question supplies both
  free-field mode expansions, on-shell equations, completeness relations,
  normalizations, and orthogonality identities on printed p. 5. They are
  indispensable and must travel with the prompt.
- **Why this target:** S.10.5 is a single short LSZ consequence. This parent combines
  exact identities, asymptotic states, LSZ, and an observable calculation.

### 10C. Replace S.10.7 with Harlow QFT I, Section 9.5, Problem 4

- **Source:** Daniel Harlow, *Lecture Notes for Physics 8.323: Relativistic Quantum
  Field Theory I* (2024), Section 9.5, Homework Problem 4, printed p. 120.
- **Primary URL:** https://www.mit.edu/~harlow/HarlowQFT1.pdf
- **Whole-parent content:** evaluate the nested ordered time integrals in the general
  LSZ derivation and obtain the complete pole product, using the terminal energy
  delta function to rewrite the final denominators.
- **Imports/cross-references:** **large and mandatory.** Import the Fourier-transformed
  `M+N`-point correlator and regulator (9.44), on-shell limit (9.45), time ordering
  (9.46), definition of `G_epsilon` and inserted-state form (9.47)--(9.50), the full
  nested integral `T` (9.51), its target value (9.52), and definitions of
  `k_tot,k'_tot` (9.53). Also retain Harlow's instruction to integrate right-to-left
  and use the delta function only at the end. Without Eqs. (9.44)--(9.53), this
  otherwise excellent problem is unusable.
- **Why this target:** S.10.7 is a speculative form-factor exercise. Harlow's problem
  supplies a rigorous piece of the nonperturbative LSZ pole derivation and directly
  exercises the volume's in/out notation.

### 10D. Replace S.10.13 with Cambridge Part III AQFT 2021, Paper 304, Question 1

- **Source:** University of Cambridge, Mathematical Tripos Part III, *Advanced
  Quantum Field Theory*, Paper 304 (2021), Question 1, printed p. 2.
- **Primary URL:**
  https://www.maths.cam.ac.uk/postgrad/part-iii/files/pastpapers/2021/paper_304.pdf
- **Whole-parent content:** `N`-scalar generating functional; source meaning;
  connected/Wilsonian functional `W=-log Z`; Legendre-transform effective action;
  interpretation of its first two functional derivatives; connected and 1PI diagram
  expansions; and inheritance of a general constant linear symmetry by the full
  quantum effective action.
- **Imports/cross-references:** none external. Preserve the source's definitions and
  transformation laws for both `phi` and `J`. Do not silently replace its terminology;
  if the editorial edition prefers `W` as the connected generator, note the source's
  label in an editorial convention note.
- **Why this target:** S.10.13 is an editorial synthesis of forward-Compton material.
  This Cambridge parent is a genuinely nonperturbative effective-action problem with
  a clean, complete source boundary.

## Chapter 11: One-Loop Radiative Corrections in QED

The first four recommendations are restorations of the already cited Zhou/Mistlberger
parents. The current prompts preserve the topic but omit much of the mathematical
scaffolding. They should be re-transcribed from the source rather than merely expanded
from their current summaries.

### 11A. Replace S.11.1 by the complete Zhou/Mistlberger PS9, Problem 1

- **Source:** Bernhard Mistlberger and Kevin Zhou, Stanford PHYS 330, Fall 2022,
  Problem Set 9, Problem 1, "e+e- to mu+mu- at one loop," printed p. 1,
  parts (a)--(b).
- **Primary URL:** https://knzhou.github.io/qft/PS9.pdf
- **Whole-parent content:** the supplied labelled leading-order annihilation diagram
  and exact tree amplitude; definition that NLO is order `e^4`; drawing every NLO
  diagram; and writing the full NLO expression without evaluating the integrals.
- **Imports/cross-references:** reproduce the labelled source diagram and Eq. (2),
  including all spin labels, momenta, signs, propagator, and vertex factors. Do not
  replace it with a verbal reference to the tree graph. The current S.11.1 adds an
  on-shell-renormalization task not present in the parent; remove that editorial
  addition when fidelity is the goal.
- **Why this target:** restores the exact starting amplitude and diagram that anchor
  all later problems in this sequential set.

### 11B. Replace S.11.2 by the complete Zhou/Mistlberger PS9, Problem 2

- **Source:** Bernhard Mistlberger and Kevin Zhou, Stanford PHYS 330, Fall 2022,
  Problem Set 9, Problem 2, "Feynman parameters," printed pp. 1--2,
  parts (a)--(d).
- **Primary URL:** https://knzhou.github.io/qft/PS9.pdf
- **Whole-parent content:** definitions of the tadpole, bubble, and triangle families
  with general indices; Gamma-function definition; Schwinger parameter; general
  `n`-denominator simplex identity; application to the bubble; Wick rotation and
  all radial/parameter integrations; and the exact `d=4-2 epsilon` check.
- **Imports/cross-references:** retain Eqs. (3)--(11), including implicit `i0`, the
  warning not to use Peskin--Schroeder's integer-only derivation, the sphere area,
  Beta-function identity, and the complete target bubble formula. The current
  prompt omits the tadpole/triangle setup and several essential intermediate steps.
- **Why this target:** this is the mathematical engine for the rest of PS9 and should
  not be compressed to a generic simplex identity plus one final bubble.

### 11C. Replace S.11.3 by the complete Zhou/Mistlberger PS9, Problem 3

- **Source:** Bernhard Mistlberger and Kevin Zhou, Stanford PHYS 330, Fall 2022,
  Problem Set 9, Problem 3, "Passarino--Veltman reduction," printed pp. 2--3,
  parts (a)--(b).
- **Primary URL:** https://knzhou.github.io/qft/PS9.pdf
- **Whole-parent content:** the rank-two tadpole worked example; derivation of its
  scalar reduction; rank-three and rank-four tadpoles; and rank-one/rank-two bubble
  decompositions with the determination of `A_perp`, `B_parallel`, and `C`.
- **Imports/cross-references:** retain the full worked derivation and Eqs. (12)--(19),
  not just its conclusions. Problem 2's scalar integrals `I_T` and `I_B` are direct
  prerequisites and must be imported or explicitly cross-linked within the same
  chapter. No figure is required.
- **Why this target:** the current S.11.3 strips away the worked tensor-decomposition
  logic and changes the exact requested coefficients; restoring the parent preserves
  the sequential pedagogy.

### 11D. Replace S.11.4 by the complete Zhou/Mistlberger PS9, Problem 4

- **Source:** Bernhard Mistlberger and Kevin Zhou, Stanford PHYS 330, Fall 2022,
  Problem Set 9, Problem 4, "Self-energy corrections in QED," printed pp. 3--4,
  parts (a)--(d).
- **Primary URL:** https://knzhou.github.io/qft/PS9.pdf
- **Whole-parent content:** the supplied labelled electron and photon self-energy
  diagrams; massless-QED assumption; construction of matrix/tensor self-energies
  without external spinors or polarizations; evaluation in terms of `p^2` and
  `epsilon`; derivation of the Gamma-function expansion; and the final Laurent
  expansion.
- **Imports/cross-references:** redraw both source diagrams with all `p,k,k+p,mu,nu`
  labels and preserve Eqs. (20)--(22). Problem 2's bubble and Problem 3's tensor
  reductions are direct prerequisites; either include their final formulas in a
  supplied-data box or cross-link explicitly to the immediately preceding restored
  parents. The current prompt incorrectly turns the endpoint into counterterm
  identification, which is not a source subpart.
- **Why this target:** this is the set's complete QED loop calculation and provides
  exactly the missing numerator, diagram, and expansion context.

### 11E. Replace S.11.8 with Cambridge Part III AQFT 2022, Paper 304, Question 3

- **Source:** University of Cambridge, Mathematical Tripos Part III, *Advanced
  Quantum Field Theory*, Paper 304 (2022), Question 3, printed p. 4,
  parts (a)--(d).
- **Primary URL:**
  https://www.maths.cam.ac.uk/postgrad/part-iii/files/pastpapers/2022/paper_304.pdf
- **Whole-parent content:** Euclidean QED current conservation, exact current-insertion
  Schwinger--Dyson identity, exact Ward--Takahashi vertex identity, consequences for
  on-shell renormalization, and the nonperturbative statement.
- **Imports/cross-references:** none external. Preserve the full Lagrangian, contact
  terms, momentum routing, and exact inverse-propagator identity. If 10A is adopted,
  do not duplicate this question in Chapter 11; assign it to Chapter 10 or 11 once.
- **Why this target:** S.11.8 asks for four renormalization constants from a book
  exercise with thin setup. The Cambridge parent gives a complete derivation of the
  physically central equality of vertex and wave-function renormalization.

## Recommended implementation order

1. Restore PS9 Problems 1--4 together, because they form one sequential block and
   later problems explicitly depend on earlier formulas.
2. Implement the Cambridge parents with no external imports (7A, 7C, 7D, 8A, 8C,
   9B, 9E, 10A/11E, 10B, 10D).
3. Implement the McGreevy parents, retaining every displayed setup and hint.
4. Implement Harlow parents only after their imported equation blocks have been
   transcribed and independently checked; Harlow 9.5 Problem 4 is particularly
   context-heavy.
5. Run source-side fidelity review before writing solutions: compare every action,
   subpart, supplied identity, diagram, hint, footnote, and cross-reference against the
   cached PDFs in this directory.
