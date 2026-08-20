# Chapter 1, packet C review

## Scope

This packet covers physical PDF pages 33--42, printed pages 21--30. The
transcription starts at Section 1-4, *Relativistic Transformation Laws of
States*, and ends with the Chapter 1 bibliography. The source pages were
inspected as rendered page images, with a 400 dpi review render used for the
symbols and footnotes. The source PDF is
`origPapers/pct_spin_statistics_all_that.pdf`.

The top of physical PDF page 33 contains Eqs. (1-51)--(1-53), which close
Section 1-3. They are outside this packet's Section 1-4 boundary. The current
`sec1_3.tex` ends at Eq. (1-50), so that page-33 continuation needs an
upstream section packet before the whole chapter can pass coverage audit.

| PDF | Printed | Objects transcribed |
| ---: | ---: | --- |
| 33 | 21 | Section 1-4 opening; vacuum-state heading and opening paragraph |
| 34 | 22 | Eq. (1-54); vacuum prose; one-particle heading; scalar measure and transformation laws; Dirac-formalism footnote |
| 35 | 23 | Spinor wavefunction; Eqs. (1-57)--(1-59); elementary-system discussion |
| 36 | 24 | Stable-particle discussion; two-or-more-particle heading; two-particle scalar product and transformation law |
| 37 | 25 | Multiparticle decomposition; interaction and collision-state setup |
| 38 | 26 | Figure 1-3; collision states; asymptotic completeness; S-matrix; asymptotic-field setup |
| 39 | 27 | In-field expression and transformation law; relation-to-general-analysis heading and footnote |
| 40 | 28 | General-analysis argument; Eq. (1-60); projective composition law; Theorem 1-2 |
| 41 | 29 | Wigner decomposition; energy-momentum cases; restrictions (1)--(3) |
| 42 | 30 | Continuation of restriction (3); closing prose; bibliography entries 1--10 |

## Equation and theorem inventory

The packet carries the printed equation identifiers `(1-54)` through `(1-60)`.
Unnumbered source displays have source markers with descriptive IDs. Theorem
1-2 is marked as a theorem and retains its printed number. Figure 1-3 is
represented by TikZ line art in `sec1_4.tex`; its caption and labels are
transcribed from the scan. The native theorem counter is advanced past the
source-rendered Theorem 1-1 in Section 1-2, and the figure counter is scoped to
the printed Figure 1-3 label.

## Notation decisions

- Abstract states use Dirac notation. The source vacuum vector `\Psi_0` is
  represented by `\ket{\Omega}`. The continuous momentum eigenvectors in the
  source footnote use `\ket{p}`, `\bra{p}`, and `\braket{\Phi}{\Psi}`.
  The scalar-product displays are likewise headed by `\braket{\Phi}{\Psi}`.
- The in/out state labels in the S-matrix display are outside the delimiters,
  using `\InBra`, `\InKet`, and `\OutBra`.
- The source's `a_r^{\mathrm{in}}(p)^*` and `b_r(p)^*` are creation operators,
  so those stars are rendered as Hermitian adjoints `\dagger`. Matrix
  complex-conjugation in `A^*\widetilde p A` remains `*`.
- Spatial momenta use `\mathbf p` in the invariant measure. The project
  mostly-plus metric changes the source's timelike shell from `p^2=m^2` to
  `p^2=-m^2`, changes `M^2=(p_1+p_2)^2` to
  `M^2=-(p_1+p_2)^2`, and changes the sign attached to the source's imaginary
  mass case. These changes are notation conversions, not content corrections.
- The source's two-component matrix `\widetilde p=p_\mu\tau^\mu` is retained
  rather than silently replacing it by a four-component Dirac slash.

## Review items

1. The source prints “There are six cases” but displays four semicolon-separated
   momentum classes, with the negative-energy analogues described in the next
   sentence. The transcription keeps the printed wording and records the four
   displayed classes after the mostly-plus sign conversion.
2. The source footnote writes the continuum normalization as
   `\delta(p-p')p^0`. The delta's dimensional convention is not expanded or
   guessed.
3. The source uses `\Phi_{\alpha_1\ldots\alpha_{2s}}(p)` without a visible
   complex-conjugation mark in Eq. (1-57); the transcription keeps that reading.
4. The source calls the states satisfying the outgoing wave condition
   “in-states” and those satisfying the ingoing wave condition “out-states”.
   This wording is retained, even though the labels run opposite to common
   scattering terminology.
5. Figure 1-3 has been rebuilt as native TikZ line art without inventing a
   numerical spectrum. A visual comparison against the source scan remains a
   release check for curve placement, hatch density, and label geometry.

## Files

- `latex/chapters/chapter01/sec1_4.tex`
- `latex/chapters/chapter01/bibliography.tex`

Both files carry `% PCT-SOURCE:` markers before substantive prose, displays,
footnotes, the theorem, the figure, and bibliography blocks.

The current project master reaches these files cleanly. Its auxiliary labels
resolve Figure 1-3 and Theorem 1-2. The full master run remains blocked later
by an existing missing-math error in Chapter 2 `sec2_4.tex`.

## Later-audit disposition

The earlier PDF 033 boundary note records the state before the upstream
continuation was restored. `audit_ch1_late.md` now records PDF 033 equations
`(1-51)`--`(1-53)`, the dotted-index definitions, and the PCT state law in
`sec1_3.tex`, followed by the PDF 033 to PDF 034 Section 1-4 handoff. Its
page ledger covers PDF 033--041, including every equation `(1-54)`--`(1-60)`,
Theorem 1-2, and Figure 1-3. `audit_ch1_bibliography.md` checks PDF 042 and
all ten bibliography entries, with the source prose and printed numbering
preserved. The later draft build and rendered figure checks close the earlier
Chapter 2 snapshot error; the chapter packet has a complete audited handoff.

Unresolved blockers: none
