# Chapter 1, Section 1-3 review packet

## Scope

- Source: origPapers/pct_spin_statistics_all_that.pdf
- Physical PDF pages: 21-32
- Printed pages: 9-20
- Content: Section 1-3, “THE LORENTZ AND POINCARÉ GROUPS”
- Output: latex/chapters/chapter01/sec1_3.tex
- Equation range: (1-4) through (1-50)
- Figures: 1-1 and 1-2
- Footnotes: the representation-theory footnote on printed page 15 and the
  complex-conjugation footnote on printed page 19

The preceding three lines at the top of printed page 9 close Section 1-2 and
are intentionally left to the Section 1-2 packet. The Section 1-3 heading
starts below them and is the first unit in sec1_3.tex. The final display on
printed page 20 ends the assigned packet in the middle of the general-spinor
substitution-rule discussion; the source section continues on the next page.

## Visual review

All twelve assigned source images (work/source-pages/pdf-021.jpg through
pdf-032.jpg) were inspected at their stored original detail. The equations,
indices, accents, matrices, captions, and footnotes were rechecked against
500 dpi renders for physical pages 22, 24, 29, 30, 31, and 32. The source is a
scan with no usable text layer, so the page image is authoritative.

The native figure code preserves the connectivity information and all four
Lorentz components in Figure 1-1, together with the two connected components
and the indicated cross-connections in Figure 1-2. The geometry is redrawn for
the JHEP page rather than embedding a raster page crop.

## Fidelity and notation decisions

1. The source uses the \(+---\) metric matrix \(G\). The project-wide Weinberg
   convention is used here: \(\eta=\operatorname{diag}(-1,+1,+1,+1)\).
   Consequently the scalar product in (1-4), the determinant identities in
   (1-13), and \(\det\check{x}=-x^\mu x_\mu\) carry the corresponding sign.
   The Lorentz condition remains \(A^{\mathsf T}\eta A=\eta\).
2. The source's \(A^*\) in the \(2\times2\) Lorentz map is a Hermitian
   adjoint. It is written \(A^\dagger\) in (1-14) and (1-17), following the
   notation guide. Componentwise complex conjugation is written \(A^*\) or an
   overline where the source means it.
3. The source matrices \(\check{x}\) and \(\widetilde{x}\) are retained. With
   the mostly-plus metric, (1-16) is written
   \(\widetilde{x}=-x_\mu\tau^\mu=x^0\mathbf 1-\mathbf{x}\cdot\boldsymbol\tau\).
4. The source writes the Dirac Clifford relation as
   \(\gamma^\mu\gamma^\nu+\gamma^\nu\gamma^\mu=-2g^{\mu\nu}\). It is rendered
   as \(2\eta^{\mu\nu}\mathbf 1\). The project convention
   \(\gamma_5=i\gamma^0\gamma^1\gamma^2\gamma^3\) is used, so the source's
   \(i\gamma^5\) in (1-44) becomes \(\gamma_5\).
5. State and Hilbert-space inner products in (1-28) and the anti-unitary
   discussion use Dirac bras and kets. The operator-order reversal in
   (1-31) and the anti-unitary complex conjugation are kept.
6. The source's componentwise \(\overline{\psi(x)}\) is written
   \(\psi^*(x)\); the footnote explicitly distinguishes it from the Dirac
   adjoint \(\bar\psi=\psi^\dagger\beta\).
7. Direct products are written with \(\times\), as required by the house
   notation policy, in the prose for the complex Lorentz group. The source
   displays \(\zeta\otimes\zeta\) for the action on two spinor indices and
   that tensor-product notation is retained.
   The repeated tensor products at the end of (1-50) are compactly written as
   \(\zeta^{\otimes j}\) and \(\zeta^{\otimes k}\) to keep the displayed rule
   within the JHEP measure.
8. Matrix identity symbols use \(\mathbf 1\) or \(\mathbf 1_2\), and semantic
   labels use the eq:ch1-* and fig:ch1-* namespace.

## Equation and unit ledger

| Printed page | Source units |
|---:|---|
| 9 | heading; scalar product (1-4); metric/lowering display; Lorentz condition (1-5); index-lowering display; group law (1-6) |
| 10 | four-component argument; component classification (1-7); inversions (1-8); decomposition (1-9) |
| 11 | boost (1-10); subgroup display; Figure 1-1 |
| 12 | matrix correspondence (1-11); Pauli matrices; inverse correspondence (1-12); determinant identities (1-13); \(SL(2,\mathbb C)\) map (1-14); homomorphism (1-15); opposite matrix (1-16); transformed opposite matrix (1-17) |
| 13 | transpose identity (1-18); complex Lorentz curve; Figure 1-2 |
| 14 | complex pair group; complex map (1-19); composition (1-20); kernel (1-21); Poincaré law (1-22); inhomogeneous \(SL(2,\mathbb C)\) law (1-23) |
| 15 | inhomogeneous complex \(SL(2,\mathbb C)\) law (1-24); block representation (1-25); tensor-spinor representation (1-26); representation footnote |
| 16 | \(SU_2\) restriction; angular-momentum decomposition; analytic continuation; signs (1-27); symmetry-substitution setup; unitary inner product (1-28); unitary substitution (1-29) |
| 17 | anti-unitary display; anti-unitary substitution (1-30); order reversal (1-31); PCT scalar rule (1-32); coordinate-spinor setup; vector-spinor (1-33); parity (1-34); time inversion (1-35); conjugate spinor (1-36) |
| 18 | Hermiticity; pair parity (1-37); pair time inversion (1-38); operator parity (1-39); anti-unitary intermediate display; operator time inversion (1-40); Dirac equation (1-41); Clifford relation (1-42); \(SL(2,\mathbb C)\) representation (1-43) |
| 19 | explicit representation (1-44); \(P,C,T\) rules (1-45); gamma and \(C\) matrices; two-component Dirac equations (1-46); complex-conjugation footnote |
| 20 | two-component substitution rules (1-47); operator rules (1-48); PCT operator (1-49); general-spinor rules (1-50) |

## Open checks for integration

- The TikZ figure code assumes the final PCT master loads tikz. The figures
  use the standard stealth arrow tip and need no extra TikZ library.
- The source uses a small visual distinction between the matrix
  \(\check{x}\), the transformed \(\widehat{x}\), and the opposite matrix
  \(\widetilde{x}\). The submitted file keeps all three accents distinct.
- Equation (1-50) ends at the bottom edge of printed page 20. Its continuation
  belongs to the next packet and should follow immediately after this file.
- No unresolved glyph reading remains in the assigned images. The only
  editorial changes are the recorded metric and notation conversions.

## Smoke-build evidence

The section was compiled in a minimal article harness with amsmath, amssymb,
mathtools, and tikz. The input produced a 12-page PDF with no LaTeX errors.
The equation scan found the complete consecutive tag range (1-4) through
(1-50). The narrow article harness reports two small prose overfull boxes; the
final JHEP master should be the authority for page-width and float checks.

## Later-audit disposition

`audit_ch1_late.md` reread PDF 021--032 at source-image resolution and checked
the native section and figure files. It confirms the complete `(1-4)` through
`(1-50)` sequence, the two figure reconstructions, the footnote boundaries,
the distinct matrix accents, and the source continuation into PDF 033. Its
corrections record the later PDF 033 equations `(1-51)`--`(1-53)` in the same
upstream section file, so the packet boundary is joined in source order. The
same audit records a successful draft master run and rendered inspection of
both Lorentz figures. The harness overfull boxes therefore remain local pilot
diagnostics, with the master build serving as the page-width check.

Unresolved blockers: none
