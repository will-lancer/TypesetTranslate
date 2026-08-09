# Mathematical review: Chapter 1 pilot

Status: pass.

## Scope and final result

I re-reviewed every mathematical unit in
`latex/chapters/253a/chapter01.tex` against the frozen note transcription,
physical-page audits, `reconciliation-notes.md`, the final cleaned transcript
and alignment, the provenance, page-disposition, and transcript-disposition
ledgers, and the official pinned-style draft PDF built at 20:56:08.

The four blocking findings `MATH-B01` through `MATH-B04` and the three
nonblocking findings `MATH-N01` through `MATH-N03` are resolved. No new
mathematical blockers appeared in the corrected chapter.

The final structural audit passes with 95 substantive units, 95 source
comments, 95 provenance records, nine page dispositions, and 382 transcript
dispositions. All 477 transcript hash references match the final cleaned
transcript SHA-256
`5ac8ac5fb25a3235d8fa11b2b6be99b5f2bb9329d307c4045629544f4e43e9bd`.
The frozen source PDF still verifies at
`9e5e4d241fffffa56c1c3df6dce4b83178f75787dd5d794a18c5d0c087769f21`.

The official `latex/master.pdf` has 11 A4 pages. I extracted its text and
rendered all 11 pages at 170 dpi, then inspected each corrected mathematical
display at original image resolution. All signs, radicals, hats, indices,
superscripts, underbraces, group labels, and equation numbers are legible.
Every font is embedded and subset. The log reports the expected `pagecolor`
and missing-email package warnings, with no overfull box, underfull box,
undefined reference, or mathematical rendering warning.

## Resolved blocking findings

### MATH-B01: multiparticle Hamiltonian action

Classification: resolved.

Chapter unit `YIN253A-C01-U030`, note 3, source physical PDF page 8, and
video `OY_napMPywE` interval `00:33:21.559-00:33:52.940` now print

$$
H\ket{\vec p_1,\ldots,\vec p_n}
=\left(\sum_{i=1}^{n}\sqrt{\vec p_i^{\,2}+m^2}\right)
\ket{\vec p_1,\ldots,\vec p_n}.
$$

This restores the operator action on the displayed basis state. The
provenance record classifies the unit as `EQUATION_NORMALIZED`, preserves
the handwritten source form (H=\sum_i\sqrt{\vec p_i^{,2}+m^2}), and cites
Yin's spoken eigenvalue statement as the reason. The page-disposition record
lists `U030` among its normalized units. The formula renders correctly as
equation 1.3 on master-PDF file page 6.

### MATH-B02: invariant-measure and phase scope

Classification: resolved.

Chapter unit `YIN253A-C01-U086`, note 8, source physical PDF page 13, has no
separate oral derivation. The aligned lecture claim occurs at
`01:18:04.739-01:18:35.390`. Equation 1.19 now labels

$$
\frac{d^D p}{(2\pi)^{D-1}}\theta(p^0)\delta(p^2+m^2)
$$

as invariant for (Lambda\in SO^+(1,D-1)). Its second annotation states
that the phase bracket is scalar when (p\to\Lambda p) and
(x-y\to\Lambda(x-y)) simultaneously. These are the correct scopes: the
proper-orthochronous restriction preserves the positive-energy sheet, and a
change of integration variable establishes invariance of the integral.

The `EQUATION_NORMALIZED` provenance record preserves the literal
handwritten (d^D p^\mu) source form and records both corrections. Page
disposition `YIN253A-C01-PD008` lists `U086` as normalized. Both underbraces
render legibly on master-PDF file page 10.

### MATH-B03: Lorentz-orbit statement in the microcausality proof

Classification: resolved.

Chapter unit `YIN253A-C01-U087`, note 8, source physical PDF page 13, also
has no oral derivation. The corrected paragraph restricts the argument to
proper orthochronous transformations and spacelike (z=x-y). It then chooses
an equal-time frame, where the integrand is odd under
(\vec p\to-\vec p), proving the vanishing of the commutator.

The provenance record preserves the note's broader source claim that the
result depends only on ((x-y)^2). Its reason identifies the omitted
time-orientation invariant on timelike proper-orthochronous orbits and
classifies the printed text as `SOURCE_COMPOSITE`. Page disposition
`YIN253A-C01-PD008` lists `U087` among its normalized units. The argument and
equation 1.20 render without ambiguity on master-PDF file page 10.

### MATH-B04: general-dimensional metric

Classification: resolved.

Chapter unit `YIN253A-C01-U056`, note 6, source physical PDF page 11, and
video interval `00:55:20.000-00:56:40.000` now print

$$
\eta^{\mu\nu}=\operatorname{diag}
\left(-1,\underbrace{1,\ldots,1}_{D-1}\right).
$$

This agrees with the general-(D) convention in `YIN253A-C01-U027`, note 3,
source physical PDF page 8, video `00:30:38.399-00:31:36.059`. The
`EQUATION_NORMALIZED` provenance record retains the handwritten four-entry
metric and explains the general-dimensional extension. Page disposition
`YIN253A-C01-PD006` records the normalization. Equation 1.8 is legible on
master-PDF file page 8.

## Resolved nonblocking findings

### MATH-N01: scope of the covariance check

Classification: resolved by explicit deferral.

Chapter units `YIN253A-C01-U089` and `YIN253A-C01-U090`, note 9, source
physical PDF page 14, and video interval `01:18:19.080-01:18:35.390` state the
free-field covariance property. Unit `U089` now says that direct verification
is deferred until the systematic construction. This is mathematically
accurate because the present source does not supply the oscillator
transformation law needed for that calculation.

The `SOURCE_COMPOSITE` provenance record explains the limitation. Page
disposition `YIN253A-C01-PD009` lists `U089` as normalized. The wording and
equation 1.21 render together on master-PDF file page 10.

### MATH-N02: Hermiticity of schematic interaction terms

Classification: resolved.

Chapter unit `YIN253A-C01-U047`, note 4, source physical PDF page 9, and
video interval `00:46:08.040-00:47:23.030` now state that momentum kernels
and Hermitian-conjugate terms are understood so that
(H_{\mathrm{int}}) is Hermitian. This supplies the required qualification
for the schematic cubic monomials in `YIN253A-C01-U046`.

The provenance reason connects the qualifier to Yin's Hermiticity premise
and the note-governed monomial order. The interaction display and qualifier
render correctly on master-PDF file page 7.

### MATH-N03: meaning of the creation-operator plus

Classification: resolved.

Chapter unit `YIN253A-C01-U034`, notes 3-4, source physical PDF pages 8-9,
and video interval `00:35:48.260-00:37:00.480` now defines

$$
a_{\vec p}^{+}\equiv a_{\vec p}^{\dagger}.
$$

The displayed equations continue to preserve the handwritten plus. The
`SOURCE_COMPOSITE` provenance record and transcript disposition
`YIN253A-C01-TD124` document the semantic equivalence between Yin's spoken
dagger and the note notation. The definition, state construction, and
commutator appear clearly on master-PDF file page 6.

## Independent mathematical checks

| Check | Chapter units and exact source locator | Result |
|---|---|---|
| Vacuum, one-particle, and multiparticle energies | `U023-U030`; note 3 / source PDF 8; video `00:28:32.100-00:33:52.940` | (H\ket\Omega=0), (p^\mu=(p^0,\vec p)), and both eigenvalue equations agree with the mostly-plus dispersion relation. |
| State normalization and (a^+\) semantics | `U034-U039`; notes 3-4 / source PDFs 8-9; video `00:35:48.260-00:41:18.890` | The bare delta commutator gives the printed one-particle overlap. The alternative (2p^0) convention is correctly described as a rescaling. |
| Free Hamiltonian and momentum | `U042-U043`, `U075-U077`; notes 4 and 7 / source PDFs 9 and 12; video `00:43:00.920-00:44:05.270` and `01:14:27.659-01:15:43.550` | The measure, energy weight, operator order, and (P^\mu=(H,\vec P)) agree with the bare-delta normalization. |
| Interaction Hamiltonian | `U046-U048`; note 4 / source PDF 9; video `00:46:08.040-00:48:05.390` | The cubic terms are schematic, change particle number as described, and now carry the required Hermiticity qualifier. |
| Poincare coordinate and field convention | `U056-U065`; note 6 / source PDF 11; video `00:55:20.000-01:05:37.380` | The mostly-plus metric, active scalar rule, translation sign, Lorentz-generator sign, factor (1/2), and Hermiticity convention are mutually consistent. |
| Poincare group law and algebra | `U067-U070`; note 6 / source PDF 11; video `01:07:33.240-01:10:22.500` | Expanding the semidirect-product law gives the displayed translation slot, mixed commutator, and Lorentz commutator with the printed signs. |
| Scalar Fourier expansion | `U080-U083`; notes 7-9 / source PDFs 12-14; video `01:17:04.560-01:18:35.390` | The radical contains ((2\pi)^{D-1}2\omega_{\vec p}). The phases and (p\cdot x=\vec p\cdot\vec x-\omega_{\vec p}x^0) make the field Hermitian under (a^+=a^\dagger). |
| Scalar commutator | `U085`; note 8 / source PDF 13; no oral derivation | Direct use of the oscillator algebra gives the coefficient (1/[(2\pi)^{D-1}2\omega_{\vec p}]) and the ordered difference (e^{ip\cdot z}-e^{-ip\cdot z}), with no extra factor of (i). |
| On-shell measure | `U086`; note 8 / source PDF 13; aligned claim `01:18:04.739-01:18:35.390` | Integrating (dp^0\,\theta(p^0)\delta(-(p^0)^2+\omega_{\vec p}^2)) gives (1/(2\omega_{\vec p})). The mass-shell sign, ((2\pi)^{D-1}) factor, and (SO^+) scope are correct. |
| Microcausality | `U087-U088`; note 8 / source PDF 13; aligned claim `01:18:04.739-01:18:35.390` | A proper orthochronous transformation reaches an equal-time frame for spacelike separation. Oddness in spatial momentum makes the commutator vanish. |
| Covariance claim | `U089-U090`; note 9 / source PDF 14; video `01:18:19.080-01:18:35.390` | The covariance equation uses the same active convention as equation 1.9. The text accurately marks the unshown oscillator-level calculation as deferred. |

Unresolved blockers: none
