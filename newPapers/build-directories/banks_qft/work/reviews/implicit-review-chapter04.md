# Independent implicit-solution review: Chapter 4

Scope: `I-CH04-001` through `I-CH04-004` in
`latex/solutions/chapter04-implicit.tex`. I compared each solution with its
record in `implicit-exercises.json`, the native hook in `chapter04/sec4_3.tex`,
and printed pages 41–42, PDF pages 51–52, of `banks-qft.pdf` using
`pdftotext -layout`.

The review covered mathematical accuracy, every requested subpart, assumptions,
local connection, conventions, clarity, pedagogy, diagram completeness,
momentum routing, and symmetry factors.

## Coverage and disposition

- **I-CH04-001: PASS after repair.** The exchange argument uses the complete
  indices `(mu,x)` and `(nu,y)`, verifies symmetry of the Proca kernel, derives
  the Grassmann-source cancellation, and checks the three physical residues.
- **I-CH04-002: PASS after repair.** The solution derives the free propagator,
  functional perturbation formula, vertex prescription, derivative momenta,
  loop measure, fermionic signs, symmetry factors, and the distinction among
  full, connected, and 1PI functions.
- **I-CH04-003: PASS after repair.** The solution fixes an all-incoming momentum
  convention, derives the cubic vertex, classifies every charge-neutral external
  sector, gives all nonzero tree and one-loop cores, supplies reducible
  insertions, routes loop momenta, and assigns symmetry factor one to every
  labeled contraction. The repaired census also includes every vanishing or
  cancelling connected contraction.
- **I-CH04-004: PASS.** The integration by parts includes the boundary flux,
  derives conservation distributionally, proves the converse under the stated
  falloff, establishes the equality of the `A` and `B` source couplings, and
  checks the smooth conserved-source massless limit.

## Findings and repairs

### Major, repaired

1. **I-CH04-003 omitted one class from its claimed exhaustive census.** Two
   labeled `BB phi phi*` diagrams consist of a tree `B phi phi*` vertex joined
   by a vector line to an oriented scalar triangle whose other vector legs are
   the two external `B` fields. They cancel as a charge-conjugate pair. They do
   not contain the vector tadpole named in the former completeness claim.

   **Repair:** added both incidence diagrams, their symmetry factors, the
   `r=3` routing inherited from Eq. (4.I.12), and their explicit cancellation.
   Replaced the former blanket tadpole claim with a complete pre-cancellation
   census.

2. **I-CH04-003 did not enumerate the zero tadpole attachments.** The source
   asks for every diagram, while the former text grouped these contractions
   without counts or incidence data.

   **Repair:** added the complete labeled one-loop totals

   | external sector | total | surviving | zero or cancelled |
   |---|---:|---:|---:|
   | `BB` | 1 | 1 | 0 |
   | `phi phi*` | 2 | 1 | 1 |
   | `BBB` | 2 | 0 | 2 |
   | `B phi phi*` | 6 | 4 | 2 |
   | `BBBB` | 6 | 6 | 0 |
   | `BB phi phi*` | 24 | 16 | 8 |
   | `phi phi phi* phi*` | 26 | 18 | 8 |

   The text now constructs every tadpole topology from its self-contracted
   vertex, bridge, and remaining typed tree. It states that each labeled graph
   has symmetry factor one. The tadpole loop momentum and zero-momentum vector
   bridge are explicit.

### Minor, repaired

3. **I-CH04-001 described the rest-frame numerator with an imprecise sign.**
   The tensor inside the propagator is `eta_ij = -delta_ij`; the propagator's
   overall minus makes the physical pole residue proportional to `delta_ij`.

   **Repair:** separated these two signs and retained the rank-three check.

4. **I-CH04-002's test monomial joined two legs while discussing an arbitrary
   n-point vertex.**

   **Repair:** the check now joins all `n` legs and identifies one external
   Proca propagator on every leg.

5. **I-CH04-003 introduced `m` without identifying it.**

   **Repair:** identified `m` as the scalar mass beside the propagator rules.

## Independent graph checks

For a connected graph with `b` external vectors, `n` external `phi` fields,
`n` external `phi*` fields, and `V` cubic vertices, the solution's relations

`I_B=(V-b)/2`, `I_phi=V-n`, and `V=E+2L-2`

are correct. Exhaustive typed-half-edge enumeration with fixed external labels
gave the totals in the table above. The nonzero counts 1, 1, 4, 6, 16, and 18
agree with the detailed self-energy, vertex, polygon, and box lists. All
automorphism groups are trivial after external labels, field species, scalar
orientation, and derivative incidences are fixed, so every listed contraction
has symmetry factor one.

## Static checks

- Inventory IDs and solution IDs match exactly and occur once each:
  `I-CH04-001`, `I-CH04-002`, `I-CH04-003`, `I-CH04-004`.
- Equation tags are unique and consecutive from `4.I.1` through `4.I.22`.
- TeX brace counts match: 269 opening and 269 closing braces.
- The TeX environment stack closes cleanly.
- The solution file has no trailing whitespace.
- Source extraction covered PDF pages 51–52 with layout preserved.
- Compilation was omitted as requested.

FINAL STATUS: **PASS**. Every issue found in the assigned chapter 4 implicit
unit has been repaired, and no open finding remains.
