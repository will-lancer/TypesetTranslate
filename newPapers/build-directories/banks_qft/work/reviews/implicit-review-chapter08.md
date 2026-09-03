# Independent implicit-exercise review: Chapter 8

Scope: I-CH08-001 through I-CH08-020, their twenty prompt files, and
`latex/solutions/chapter08-implicit.tex`. I compared each unit with
`implicit-exercises.json`, its native hook, and the cited source pages. The
review covered the mathematics, conventions, assumptions, requested parts,
pedagogy, and local connection.

Overall: **PASS**. Every in-scope finding was repaired. All twenty inventory
IDs occur once in the prompt files, once in the solution file, and once at a
native hook. Compilation was excluded by instruction.

## Coverage

| ID | Printed / PDF pages | Audited content | Disposition |
| --- | --- | --- | --- |
| I-CH08-001 | 94 / 104 | General renormalizable gauge theory, invariant tensors, and quantum consistency | PASS after convention, scalar-normalization, and anomaly-scope repairs. |
| I-CH08-002 | 94 / 104 | Renormalizability of charged vectors and the Yang--Mills completion | PASS after adding the magnetic-moment check. |
| I-CH08-003 | 97 / 107 | Unfixed kernels, vertices, and gauge-orbit zero directions | PASS after covering a symmetry-breaking stationary vacuum. |
| I-CH08-004 | 99 / 109 | BRST state cohomology, local cohomology, quartets, and gauge independence | PASS after separating the two cohomologies and their assumptions. |
| I-CH08-005 | 103 / 113 | Scalar vacuum polarization, Ward identity, divergence, and decoupling | PASS after fixing the high-energy logarithm convention. |
| I-CH08-006 | 107 / 117 | Nielsen--Olesen flux-tube tail in the monopole-confinement discussion | PASS after correcting the locator language. |
| I-CH08-007 | 111 / 121 | Strong-coupling Wilson loop, minimal surface, and string tension | PASS after correcting the first local-deformation estimate. |
| I-CH08-008 | 116 / 126 | Light-quark masses, GMOR, anomalous single-flavor rotations, and instantons | PASS. The conclusion is limited to the symmetry protected by the Ward identity. |
| I-CH08-009 | 116 / 126 | Electroweak currents, Fermi matching, QED scattering, and CKM structure | PASS after adding the gauge-propagator cancellation check. |
| I-CH08-010 | 118 / 128 | Vafa--Witten propagator bound and current-correlator analyticity | PASS after repairing the weight and separating perturbative from uniform bounds. |
| I-CH08-011 | 120 / 130 | Consistent anomaly, covariant anomaly, and Bardeen--Zumino current | PASS after replacing the false action-counterterm equivalence with the current-improvement identity. |
| I-CH08-012 | 122--123 / 132--133 | Representation classes with zero perturbative cubic anomaly | PASS after excluding the abelian $SO(2)$ case and separating the $SU(2)$ global anomaly. |
| I-CH08-013 | 124 / 134 | Descent, nontriviality, uniqueness, and product-group anomalies | PASS after making the $U(1)^3$ and $U(1)G^2$ sectors explicit. |
| I-CH08-014 | 125 / 135 | Spin connection and all hypercharge branches | PASS after repairing the connection sign and classifying $Y_q=0$. |
| I-CH08-015 | 127 / 137 | $B$ and $L$ anomalies, topology, and $B-L$ | PASS with the gravity and right-handed-neutrino scope stated. |
| I-CH08-016 | 127 / 137 | Instanton and sphaleron suppression | PASS after distinguishing an amplitude from a squared probability or rate. |
| I-CH08-017 | 128 / 138 | Wess--Zumino quantization, descent, anomaly matching, and decay coupling | PASS after fixing the $K/f$ convention and the angular-field map. |
| I-CH08-018 | 129--130 / 139--140 | Baryon anomaly matching and flavor decoupling | PASS after making the general exclusion conditional and stating the restriction-matrix test. |
| I-CH08-019 | 130 / 140 | Anomaly pole, discontinuity, triangle cut, and mass-gap implication | PASS after separating a massless singularity from a one-particle pole. |
| I-CH08-020 | 132 / 142 | Dressed fields and the unitary-gauge limit | PASS after deriving residual-$H$ transformation laws and using the broken projection. |

## Findings and dispositions

### Major, repaired

- **I-CH08-011:** The source identifies the difference between covariant and
  consistent anomalies with the variation of a local action. That reading
  conflicts with Wess--Zumino consistency. The prompt and solution now use
  $J_{\rm cov}=J_{\rm cons}+K_{\rm BZ}$ and
  $\mathcal A_{\rm cov}-\mathcal A_{\rm cons}=D K_{\rm BZ}$. The graded-form
  expansion checks every term through the quartic divergence.
- **I-CH08-014:** The authored spin-connection formula had the opposite sign
  from the displayed torsion convention. The corrected expression was
  substituted back into the torsion equation. The anomaly system now includes
  the full $Y_q=0$ branch,
  $Y_l=Y_{\bar e}=0,\ Y_{\bar d}=-Y_{\bar u}$, with arbitrary
  $Y_{\bar u}$.
- **I-CH08-018:** A fixed-flavor ansatz had been presented as a general
  all-$(N,N_F)$ no-go. The solution now proves only the explicit
  $N=N_F=3$ decuplet obstruction and the even-$N$ statistics obstruction.
  For odd $N$, it states the integer branching equations and lists the
  persistent-mass, continuity, confinement, spectrum, and topological-sector
  premises needed for Banks's broader claim. The $N_F=2$ boundary receives
  separate treatment.

### Moderate, repaired

- **I-CH08-001:** The prompt and solution now use the consistent Hermitian
  convention $D=\partial-\mathrm{i}A$,
  $[D,D]=-\mathrm{i}F$, and $F=\dd A-\mathrm{i}A^2$. A real scalar carries
  the required factor $1/2$, and the quantum anomaly conditions are stated.
- **I-CH08-004:** The oscillator quartet argument for asymptotic states is now
  separate from the doublet theorem for local polynomials. Equations of motion,
  total derivatives, boundary conditions, BRST invariance, and the perturbative
  gauge-patch assumption are identified.
- **I-CH08-006:** The title now names the Nielsen--Olesen flux tube. Its
  $K_0$ and $K_1$ tails describe the tube that confines monopole flux.
- **I-CH08-007:** The first correction now scales with the minimal area.
  Replacing one plaquette by the other five cube faces gives
  $A_{\min}e^{-4g^2}$, whose connected repetitions shift the string tension.
- **I-CH08-010:** The exponential weight is centered at the second endpoint,
  which produces the intended distance factor. The Born-series discussion and
  the gauge-uniform lattice Combes--Thomas estimate are kept logically
  distinct. Contact subtraction and the connected nonsinglet scope are stated.
- **I-CH08-020:** The solution derives the compensating $H$ action on
  $\Omega,\Delta,\Psi$ and the connection law for $B_\mu$. It projects the
  vector onto broken generators, retains residual $H$ covariance, and states
  the order-of-limits restriction.

### Minor, repaired

- I-CH08-002 now checks the Yang--Mills Pauli term and
  $g_{\rm mag}=2$.
- I-CH08-003 now includes the scalar Hessian, vector--Goldstone mixing, vector
  mass matrix, fermion kernel, and combined gauge zero direction at a broken
  vacuum.
- I-CH08-005 now gives the sign and coefficient of the ultraviolet logarithm
  in its displayed tensor convention.
- I-CH08-009 now verifies electromagnetic-current transversality before using
  a covariant-gauge photon propagator.
- I-CH08-012 now states $n\ge3$, so $SO(2)\simeq U(1)$ lies outside its
  non-abelian classification.
- I-CH08-013 now includes product-group abelian and mixed cubic polynomials.
- I-CH08-016 now distinguishes the one-instanton amplitude from a squared
  probability and an inclusive rate.
- I-CH08-017 now defines dimensionless
  $K=g^2\mathcal C_{XQQ}/(16\pi^2)$ and relates the canonical Goldstone field
  to Banks's angular field.
- I-CH08-019 now scopes the mass-gap conclusion to an ordinary local particle
  description without an anomaly-matching topological sector.
- Malformed TeX control sequences were repaired in I-CH08-001, 004, 006, 009,
  011, 014, 015, 019, and 020.

## Source, base, and inventory findings

- PDF page 104 combines $D=\partial-\mathrm{i}A$ with
  $[D,D]=+\mathrm{i}F$ and
  $F=\dd A+\mathrm{i}A^2$. The editorial unit uses the algebraically
  consistent signs. The base transcription remains unchanged.
- The I-CH08-006 inventory calls the target ``monopole asymptotics.'' PDF page
  117 gives the large-radius Nielsen--Olesen vortex profile used to confine
  monopole flux. The prompt title was repaired; the inventory was left intact.
- PDF pages 130 and 134 describe the covariant-consistent anomaly difference
  as a local action variation. The Bardeen--Zumino current relation is the
  consistent local statement. The base text was left intact.
- I-CH08-012 records PDF page 132, while its representation classification and
  native hook continue on page 133. Both pages were reviewed.
- PDF page 134 attributes the Standard Model $SU(3)^3$ cancellation to real
  or pseudoreal representations. The color representations are complex; the
  cubic anomaly cancels between $q_L$ and $u^c,d^c$. PDF page 135 also
  omits the degenerate $Y_q=0$ branch. Both points were corrected within the
  editorial unit, with the base text unchanged.
- PDF pages 139--140 assert the all-flavor chiral-breaking conclusion without
  displaying the restriction matrices or the dynamical assumptions needed to
  promote a single massive-propagator bound to a composite-correlator bound.
  I-CH08-018 now records those dependencies and treats the broad claim as
  conditional. The base text remains unchanged.

## Files repaired

- `latex/implicit/I-CH08-001.tex`
- `latex/implicit/I-CH08-003.tex`
- `latex/implicit/I-CH08-004.tex`
- `latex/implicit/I-CH08-006.tex`
- `latex/implicit/I-CH08-010.tex`
- `latex/implicit/I-CH08-012.tex`
- `latex/implicit/I-CH08-014.tex`
- `latex/implicit/I-CH08-017.tex`
- `latex/implicit/I-CH08-018.tex`
- `latex/implicit/I-CH08-019.tex`
- `latex/implicit/I-CH08-020.tex`
- `latex/solutions/chapter08-implicit.tex`

## Checks

- Inventory, prompt, solution, and hook ID comparison: twenty exact ordered
  matches in every location, with no duplicate or missing ID.
- Structural scan: balanced braces, balanced environments, twenty solution
  entries, and seventy-six unique equation tags.
- Direct arithmetic checks: scalar-loop moments $1/3$ and $1/30$, both
  hypercharge branches, and the fundamental/decuplet anomaly traces
  $-6$ and $-162$.
- Direct tensor check: substitution of the repaired spin connection satisfies
  the source torsion equation for arbitrary antisymmetric anholonomy data.
- Differential-form check: the displayed Bardeen--Zumino polynomial reproduces
  $3F^2-\dd(A\dd A+A^3/2)$.
- `lacheck`: clean on all twenty prompt files and the collected solution.
- `chktex` with fragment-appropriate warning exclusions: clean.
- Trailing-whitespace and placeholder scan: clean.
- Compilation: not run, as instructed.

FINAL STATUS: **PASS**. Every in-scope mathematical, coverage, clarity,
assumption, and static-structure issue has a complete disposition.
