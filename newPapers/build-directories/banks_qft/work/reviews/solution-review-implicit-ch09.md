# Bounded mathematical review: implicit Chapter 9

Date: 2026-09-02

Scope: `I-CH09-001` through `I-CH09-023`. I read each current exercise beside
its matching solution and checked the nearby Chapter 9 source hook. This was
one focused review at the requested 98%-threshold. I checked prompt-solution
fit, the main derivations, signs and factors, hypotheses, and the requested
subparts. No TeX files were edited.

## Coverage

| ID | Native source context | Decisive check | Status |
|---|---|---|---|
| I-CH09-001 | opening, pp. 137–138 | gradient sign, Lyapunov decrease, compact omega-limit argument, RG-time orientation | PASS |
| I-CH09-002 | opening, pp. 137–138 | fixed-point dilatation, \(y=d-\Delta\), correlator scaling, free-scalar check | PASS |
| I-CH09-003 | sec. 9.1, pp. 139–140 | BRST-exact gauge variation, \(R_\kappa\) limit, propagator falloff, conserved-current check | PASS |
| I-CH09-004 | sec. 9.3, pp. 145–146 | finite-volume analyticity, positivity/log branch, thermodynamic zero accumulation, Ising check | PASS |
| I-CH09-005 | sec. 9.3, pp. 147–148 | cumulant locality, iterated quasi-locality, block-average mesh, Gaussian central region | PASS |
| I-CH09-006 | sec. 9.4, p. 148 | loop-momentum routing, UV subintegrability, coefficientwise finiteness, mass rearrangement | PASS |
| I-CH09-007 | sec. 9.5, pp. 154–155 | local Weyl Ward identity, distributional trace, finite Weyl path, scalar improvement | PASS |
| I-CH09-008 | sec. 9.5, pp. 155–156 | Euclidean insertion sign, geometric resummation, Minkowski \(i0\), Dyson equation | PASS |
| I-CH09-009 | sec. 9.6, pp. 156–159 | two-loop topologies, forest poles, \(Z_\phi\) subtraction, MS relation and beta function | PASS |
| I-CH09-010 | sec. 9.8, pp. 165–166 | Dirac/scalar polarization and seagull, multiplicities, self-energies, Ward-linked counterterms | PASS |
| I-CH09-011 | sec. 9.8, p. 167 | inverse-propagator Ward identity, translation shift, transverse tensor form | PASS |
| I-CH09-012 | sec. 9.8, p. 168 | gamma recurrence/reflection, positivity, proper-time and Gaussian factors | PASS |
| I-CH09-013 | sec. 9.8, p. 169 | total derivative, boundary strip, dimensional continuation, massive \(1/p^2\) conclusion | PASS |
| I-CH09-014 | sec. 9.8, p. 169 | small-\(s\) power count, tensor momentum order, differentiated check | PASS |
| I-CH09-015 | sec. 9.8, p. 172 | cancellation of both fermion poles, omitted \(O(\alpha^2)\) product, gauge limits | PASS |
| I-CH09-016 | sec. 9.8, p. 172 | characteristic solution, running coupling, branch exponent and discontinuity | PASS |
| I-CH09-017 | sec. 9.9, p. 174 | forest pole order, MS recursion, beta residue, anomalous-dimension pole cancellation | PASS |
| I-CH09-018 | sec. 9.10, p. 178 | \(\Delta=2\) shortening, Maxwell equations, positivity/free-sector conclusion | PASS |
| I-CH09-019 | sec. 9.10, p. 180 | SU(2) curvature decomposition, magnetic term, Proca comparison, \(g_{\mathrm{mag}}=2\) | PASS |
| I-CH09-020 | sec. 9.11, pp. 185–187 | separate triple/tadpole/ghost poles, longitudinal cancellation, matter normalization, beta distinction | PASS |
| I-CH09-021 | sec. 9.11, p. 187 | Schwinger integrals, Wick factors, gamma arguments, tensor contraction | PASS |
| I-CH09-022 | sec. 9.13, pp. 191–192 | simple/double pole separation, LSZ \(Z^{-1/2}\) cancellation, on-shell assumptions | PASS |
| I-CH09-023 | sec. 9.14, p. 201 | Weinberg counting, \(f\)-scaling, loop/derivative expansion, Adler zero | PASS |

## Findings

No release-blocking mathematical error remains in the assigned current files.

The Chapter 9 solutions preserve the source conventions and the relevant
qualifications. In I-CH09-004, the classical-integral analyticity statement
uses the exercise's uniform analytic domination assumption; that assumption
must be read locally on a complex parameter neighborhood, as required for the
Taylor-series conclusion. I-CH09-006 uses a Gaussian shorthand for the
exponential UV falloff; the source hypothesis supplies the needed integrable
decay. I-CH09-009 compresses the finite two-loop algebra into representative
iterated-bubble and wineglass parameter integrals plus the pole table, while
including the forest subtraction and \(Z_\phi\) contribution needed for the MS
result. I-CH09-010 states the arbitrary-charge quartic counterterms in tensor
and allowed-monomial form, which is the appropriate generalization because no
particular flavor symmetry was fixed. I-CH09-019 uses a charge-sign convention
for \(W^\pm\); the curvature square and magnetic interaction are consistent
with that convention and give the required gyromagnetic magnitude.

The matter rows in I-CH09-020 agree with the source's Weyl/complex-scalar
normalization after factoring \(i g^2/(16\pi^2\epsilon)\) in \(d=4-\epsilon\):
the Weyl row is \(-4D(R_F)/3\) and the complex-scalar row is
\(-2D(R_S)/3\). The solution also keeps this gauge-field wave-function
coefficient distinct from the gauge-independent beta-function coefficient.

## Static checks

- Every assigned exercise ID occurs once in the implicit exercise inventory.
- Every assigned ID occurs once in `chapter09-implicit.tex`.
- The solutions cover the requested subparts, including assumptions and
  convention-sensitive signs.
- No placeholder marker occurs in the assigned exercise or solution blocks.

FINAL STATUS: PASS
