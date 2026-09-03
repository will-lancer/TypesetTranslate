# Independent implicit-solution review: Chapter 10

Scope: `I-CH10-001` through `I-CH10-021` in
`latex/solutions/chapter10-implicit.tex`. I compared every unit with
`implicit-exercises.json`, its native `\BanksImplicitHook`, and the cited pages
of `banks-qft.pdf`. Source text came from short `pdftotext -layout` ranges.
Printed pages 221–222, PDF pages 231–232, were also rendered to settle the
Bogomolny normalization.

The review covered each requested subpart, mathematical assumptions,
conventions, nearby-text connection, pedagogy, and internal checks.

## Coverage

| ID | printed / PDF pages | decisive check | disposition |
|---|---:|---|---|
| I-CH10-001 | 206 / 216 | Legendre transform and WKB `g^2` scaling | PASS |
| I-CH10-002 | 209 / 219 | derivative of the translated saddle | PASS |
| I-CH10-003 | 209 / 219 | tubular-coordinate Jacobian at Gaussian order | PASS |
| I-CH10-004 | 211 / 221 | alternating even/odd dilute-gas sums | PASS after repair |
| I-CH10-005 | 212 / 222 | zero-mode equation and single-lump norm | PASS after repair |
| I-CH10-006 | 213 / 223 | nodeless mode and Sturm ordering | PASS |
| I-CH10-007 | 214–215 / 224–225 | tangent and normal field-space equations | PASS after repair |
| I-CH10-008 | 216 / 226 | `d` normalizable translation modes | PASS |
| I-CH10-009 | 218 / 228 | radial measure gives `g_c^2=1/2` | PASS |
| I-CH10-010 | 218–220 / 228–230 | core/tail integrability and symmetry hypotheses | PASS after repair |
| I-CH10-011 | 220 / 230 | Stokes phase and interior theta shift | PASS |
| I-CH10-012 | 221–222 / 231–232 | BPS square and surface-flux factors | PASS after repair |
| I-CH10-013 | 226–227 / 236–237 | graded Chern–Simons calculation | PASS |
| I-CH10-014 | 227 / 237 | `pi_3` factorization and instanton bound | PASS after repair |
| I-CH10-015 | 228–229 / 238–239 | residual generator and theta-shifted momentum | PASS after repair |
| I-CH10-016 | 233 / 243 | proper-time sign, period integral, and `i epsilon` | PASS |
| I-CH10-017 | 233 / 243 | explicit boost and covariant four-momentum | PASS |
| I-CH10-018 | 235 / 245 | first integral gives `M_X=E_c` | PASS |
| I-CH10-019 | 237 / 247 | exact homotopy sequence and clutching map | PASS after repair |
| I-CH10-020 | 237–238 / 247–248 | character/cocharacter duality and smooth-core kernel | PASS after repair |
| I-CH10-021 | 238 / 248 | direct electromagnetic angular-momentum integral | PASS |

## Findings and disposition

### Major, repaired

1. **I-CH10-010 required a global radial-minimizer theorem absent from the
   source assumptions.** Finite action and massive tails establish admissible
   configurations. They do not establish uniqueness or rotational symmetry.

   **Repair:** scoped the proof to the centered unit-winding sector and stated
   the needed existence, unique-zero, and uniqueness-modulo-gauge hypothesis.
   The solution now separates symmetric criticality from global minimality and
   records the higher-winding splitting issue.

2. **I-CH10-012 inherited incompatible source coefficients.** The action on
   printed page 221 places `1/2 (D phi)^2` inside `1/(4g^2)`. It cannot expand
   to the square, BPS equation, or bound on printed page 222.

   **Repair:** stated the canonical action normalization fixed by the displayed
   square and verified that its cross term is `nu M`, yielding
   `S >= nu |M|/g^2`. The surface-charge derivation keeps every factor of two.

3. **I-CH10-014 used an unstated index-one `SU(2)` embedding and gave no
   global-form scope.** A general embedding can multiply the generator by its
   Dynkin index. A semisimple product has one `pi_3` integer per simple factor,
   while a central quotient may contain the image only as an `SU(2)` quotient.

   **Repair:** used the long-root index-one homomorphism for a compact,
   connected, simply connected simple group. Added the finite-cover,
   semisimple-product, and torus cases. The topological charge and trace
   normalization are explicit. The bound now follows as
   `S_E >= 8 pi^2 |n|/g^2` with the correct self-dual sign.

4. **I-CH10-015 asserted the theta correction without deriving the canonical
   shift.** This left the source symbol `E_i` ambiguous.

   **Repair:** introduced separate physical field `mathcal E_i` and canonical
   momentum `Pi_i`, differentiated the velocity-dependent Lagrangian, and used
   the patchwise Bianchi identity. The distributional monopole term now follows
   from `Pi_i=mathcal E_i/g^2+(theta/2pi)B_i`.

### Moderate, repaired

5. **I-CH10-007 faced a source normalization conflict.** Printed page 214
   omits `1/2` from the radial kinetic term, while the equation on page 215
   requires it.

   **Repair:** adopted the convention fixed by the equation and documented the
   mismatch before deriving both field-space projections.

6. **I-CH10-005 reused `S_0` across single- and multi-instanton profiles.**

   **Repair:** distinguished the exact single-lump norm, the overall
   `sqrt(n S_0)` translation norm, and each constituent's approximate
   `sqrt(S_0)` mode.

7. **I-CH10-019 omitted the hypotheses behind the bundle sequence.**

   **Repair:** stated that `G` is connected and `H` is closed, fixed basepoints,
   and identified `pi_1(H)` with the identity component when needed.

8. **I-CH10-020 could conflate the global character lattice with the weights
   carried by dynamical matter.**

   **Repair:** identified the full lattice, the possible dynamical sublattice,
   the quotient cocharacters, and the stricter smooth-monopole kernel.

### Minor, repaired

9. **I-CH10-004 used `kappa` before defining it.** Added the one-event fugacity
   `kappa=D^{-1/2} exp(-S_0/g^2)` and retained the resulting splitting `2 kappa`.

10. **I-CH10-014 left the charge normalization implicit and contained a prose
    typo.** Defined `n` by the Pontryagin integral, scoped the invariant trace,
    and corrected the self-duality sentence.

## Source and base-text issues

- Printed page 212 uses `S_0` for a multi-lump profile before returning to the
  one-lump norm. I-CH10-005 now distinguishes them.
- Printed page 213 says every positive mode is a scattering state. A generic
  one-dimensional fluctuation potential can also have positive bound shape
  modes. I-CH10-006 already states the valid node-theorem conclusion.
- Printed pages 214–215 disagree by a factor of two in the scalar kinetic
  normalization. I-CH10-007 follows the printed equation of motion.
- Printed page 220 states radial global minimality without sufficient
  hypotheses. I-CH10-010 gives the strongest conditional proof supported by
  the data.
- Printed pages 221–222 have the BPS coefficient mismatch described above.
- Printed page 227 phrases the topology claim for a general gauge group as a
  single `SU(2)` subgroup statement. I-CH10-014 supplies the simple-factor and
  global-quotient qualifications.
- Printed page 229 calls the theta-shifted canonical momentum the electric
  field. I-CH10-015 separates the two quantities.

## Static checks

- The inventory, native hooks, and solution each contain the same 21 IDs,
  once per ID.
- TeX braces match: 480 opening and 480 closing braces.
- Display delimiters match: 138 opening and 138 closing delimiters.
- The TeX environment stack closes cleanly.
- The solution has no trailing whitespace or review sentinels.
- Source extraction covered PDF pages 216, 219, 221–226, 228, 230–232,
  236–239, 243, 245, and 247–248. PDF pages 231–232 received visual checks.
- Compilation was omitted as requested.

FINAL STATUS: **PASS**. Every in-scope solution finding is repaired. The source
and base-text defects are explicit in the affected units, with no false
unconditional claim left in the chapter 10 solution.
