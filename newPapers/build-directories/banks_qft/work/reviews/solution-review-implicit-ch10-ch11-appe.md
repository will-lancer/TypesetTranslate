# Bounded mathematical review: implicit Chapter 10, Chapter 11, Appendix E

Date: 2026-09-02

Scope: one focused review of `I-CH10-001` through `I-CH10-021`,
`I-CH11-001`, and `I-APPE-001`.  I read each current exercise beside its
matching solution, checked the nearby native source context, and tested the
main derivation, signs, factors, hypotheses, and requested subparts.  This is
the requested 98%-threshold review.  TeX compilation and rendered-page QA are
release-stage checks outside this report.

## Coverage

| ID | Local source context | Main check | Status |
|---|---|---|---|
| I-CH10-001 | pp. 206 / 216 | Legendre transform, operator ordering, and WKB `g^2` factors | PASS |
| I-CH10-002 | p. 209 / 219 | Translation family, Hessian kernel, and normalizability | PASS |
| I-CH10-003 | p. 209 / 219 | Tubular Jacobian, curvature term, and Gaussian measure | PASS |
| I-CH10-004 | p. 211 / 221 | Alternating double-well histories, factorial, trace, and splitting | PASS |
| I-CH10-005 | p. 212 / 222 | Differentiated instanton equation, first integral, and zero-mode norm | PASS |
| I-CH10-006 | p. 213 / 223 | Sturm ordering, non-negativity, threshold, and shape-mode scope | PASS |
| I-CH10-007 | pp. 214–215 / 224–225 | Tangential and normal bounce equations, boundary data, and covariant form | PASS |
| I-CH10-008 | p. 216 / 226 | Translation tangents, direct operator check, and square integrability | PASS |
| I-CH10-009 | p. 218 / 228 | Two-dimensional radial integral and `g_c^2=1/2` | PASS |
| I-CH10-010 | pp. 218–220 / 228–230 | Radial action, finite tails, and explicitly stated minimizer hypothesis | PASS |
| I-CH10-011 | p. 220 / 230 | Stokes phase, local theta shift, factorization, and screening condition | PASS |
| I-CH10-012 | pp. 221–222 / 231–232 | Covariant divergence, Bianchi identity, and form/vector factors | PASS |
| I-CH10-013 | pp. 226–227 / 236–237 | Abelian total derivative and graded Chern–Simons signs | PASS |
| I-CH10-014 | p. 227 / 237 | `SU(2)` factorization, square bound, self-duality sign, and Bianchi check | PASS |
| I-CH10-015 | pp. 228–229 / 238–239 | Gauss generator, canonical theta shift, and monopole charge | PASS |
| I-CH10-016 | p. 233 / 243 | Proper-time sign, periodic trace path integral, and `i epsilon` | PASS |
| I-CH10-017 | p. 233 / 243 | Boosted stress tensor, mass shell, and soliton pole | PASS |
| I-CH10-018 | p. 235 / 245 | Collective-coordinate kinetic term and static first integral | PASS |
| I-CH10-019 | p. 237 / 247 | Clutching map, homomorphism, and exact-sequence kernel | PASS |
| I-CH10-020 | pp. 237–238 / 247–248 | Character/cocharacter pairing, global quotient, and `SU(2)`/`SO(3)` | PASS |
| I-CH10-021 | p. 238 / 248 | Cross-term field angular momentum and Schwinger–Zwanziger factor | PASS |
| I-CH11-001 | pp. 243–244 / 253–254 | Complex slices, Wick rotation, spectral continuation, and free propagator | PASS |
| I-APPE-001 | p. 258 / 268 | Symmetric adjoint, `SU(N)` factors, classification, and anomaly tensor | PASS |

## Findings

No blocking mathematical finding remains in the assigned current files.

The Chapter 10 solutions preserve the local repairs required by their source
context.  These include the WKB energy rescaling in I-CH10-001, the positive
shape-mode qualification in I-CH10-006, the scalar kinetic normalization note
in I-CH10-007, the unit-winding uniqueness hypothesis in I-CH10-010, the
Bogomolny normalization note in I-CH10-012, the index-one and global-form
qualification in I-CH10-014, and the distinction between physical electric
field and canonical momentum in I-CH10-015.  The signs in the Chern–Simons
calculation, proper-time identity, boosted momentum, monopole kernel, and
dyon angular momentum agree with the displayed exercise conventions.

I-CH11-001 is internally consistent with the current project mostly-plus
convention.  The solution derives the positive Euclidean metric, uses Banks's
continued source `+i J phi`, supplies the ordered complex-time gaps, and
recovers `-i/(p^2+m^2-i0)` with `p^2=-(p^0)^2+mathbf p^2`.

I-APPE-001 states the symmetric and alternating invariant-tensor mechanism,
derives
`T^a T^b = delta^{ab} 1/(2N) + (d^{abc}+i f^{abc})T^c/2`,
handles `SU(2)`, lists the cubic-invariant classification, and checks the
reality/source-typo issue in the printed anomaly formula.  The conjugate and
adjoint checks are present.

## Structural check

Each assigned solution ID occurs once in its current solution unit, and every
assigned exercise prompt has a matching ID.  The exercise and solution
subparts align.  No placeholder marker occurs in the assigned files.

FINAL STATUS: PASS
