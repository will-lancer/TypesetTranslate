# Mathematical review: Chapter 1 near-verbatim pilot

Status: blocked pending regenerated provenance for the current 231 source
units.

## Scope

I reviewed the current 198 near-verbatim transcript blocks and every inserted
note, equation, notation statement, figure, and Q&A formula in
`latex/chapters/253a/chapter01.tex`. The comparison set was
`notes-exact.tex`, `09-equation-interleave.md`, all 64 records in
`verbatim-formulas.jsonl`, the five mathematical page-audit files, the frozen
382-record cleaned transcript, its disposition ledger, and the current
19-page PDF.

The formula pass covers all 64 formula-sidecar records: 36 `SPEECH_CLEAN`,
14 `EQUATION_NORMALIZED`, nine note-authoritative, three `SOURCE_CONFLICT`,
and two `SOURCE_COMPOSITE`. I also checked every displayed note formula that
has no separate spoken derivation.

## Blocking finding

### MATH-B05: provenance has not been regenerated for the near-verbatim chapter

Classification: provenance blocker.

The chapter currently contains 231 `YIN-SOURCE` comments: 198 transcript
blocks and 33 note, equation, notation, figure, or editorial units. The
canonical `work/pilot/provenance.jsonl` still has 95 records for the previous
compressed chapter. It lacks the transcript-block IDs, `YIN253A-C01-N001`,
`YIN253A-C01-N002`, and split generator units `YIN253A-C01-U076A` through
`U076C`; it also retains many IDs absent from the new TeX. Its current
timestamp is 20:55:47, while the chapter was rebuilt after 22:15.

This prevents final verification of the source classes and of the required
normalization records for the following mathematical changes:

- `YIN253A-C01-U030`, note 3 / source PDF 8, video
  `00:33:21.559-00:33:52.940`: the handwritten Hamiltonian shorthand is
  printed as an operator eigenvalue equation.
- `YIN253A-C01-N001`, notes 3-4 / source PDFs 8-9, video
  `00:35:48.260-00:37:00.480`: the literal note symbol satisfies
  (a_{\vec p}^{+}\equiv a_{\vec p}^{\dagger}).
- `YIN253A-C01-U056`, note 6 / source PDF 11, video
  `00:55:20.000-00:56:40.000`: the four-entry metric is extended to general
  (D).
- `YIN253A-C01-U086`, note 8 / source PDF 13, notes-only derivation: the
  literal anomaly (d^D p^\mu) is normalized to (d^D p), and the two
  transformation annotations are mathematically restricted.
- `YIN253A-C01-U087`, note 8 / source PDF 13, notes-only derivation: the
  global squared-interval claim is restricted to the spacelike orbit needed
  for microcausality.
- Transcript formula records `T000141`, `T000279`, and `T000281`, at
  `00:39:53.940-00:40:20.510`, `01:15:00.540-01:15:19.970`, and
  `01:15:19.980-01:15:43.550`: their sidecar class is `SOURCE_CONFLICT` and
  the unresolved normalization factor or note-board hat distinction must
  remain recorded.

Required resolution: regenerate provenance one-to-one with all 231 current
source IDs. Each record should preserve the frozen transcript SHA-256
`5ac8ac5fb25a3235d8fa11b2b6be99b5f2bb9329d307c4045629544f4e43e9bd`.
The records for normalized equations must retain the literal source form,
the printed form, the operation, and the reason. Formula-bearing transcript
records must carry the authority object from `verbatim-formulas.jsonl`,
including all three `SOURCE_CONFLICT` records.

## Formula findings that pass at source level

| Check | Chapter unit or formula record; exact source locator | Result |
|---|---|---|
| Vacuum and particle energies | `U024`, `U028`, `U030`, plus `F-000097` through `F-000109`; note 3 / PDF 8; video `00:28:32.100-00:33:52.940` | The vacuum, one-particle, and multiparticle eigenvalue equations are dimensionally and operator-theoretically correct. |
| Creator notation | `N001`, `U035`, `U037`, `U043`, `U046`, `U076A-B`, `U080`; notes 3-4 and 7 / PDFs 8-9 and 12; video `00:35:48.260-00:47:15.170` and `01:14:44.760-01:17:42.360` | Displayed note equations preserve every literal (a^+). Near-verbatim speech keeps spoken (a^\dagger). The identity in `N001` makes the semantics explicit. |
| State normalization | `U035`, `U037`; notes 3-4 / PDFs 8-9; video `00:37:00.480-00:40:20.510` | The bare delta commutator gives the printed one-particle overlap. `T000141` withholds the uncertain relativistic factor and records the normalization discussion as a source conflict. |
| Free Hamiltonian | `U043`, `U076A`; notes 4 and 7 / PDFs 9 and 12; video `00:43:21.319-00:44:05.270` and `01:14:44.760-01:15:00.000` | The spatial measure, energy weight, and (a^+a) order agree with the bare-delta convention and the zero-energy vacuum. |
| Interaction examples | `U046`, `N002`; note 4 / PDF 9; video `00:46:08.040-00:47:23.030` | The cubic monomials have the source order. The editorial Hermiticity note states that kernels and conjugate terms are understood. |
| Coordinate convention | `U056`; note 6 / PDF 11; video `00:55:20.000-00:57:00.000` | The mostly-plus general-(D) metric is consistent with (p^2+m^2), the dispersion relation, and the spacelike condition. |
| Scalar covariance and infinitesimal generators | `U059`, `U062`, `U064`; note 6 / PDF 11; video `00:59:00.000-01:04:40.000` | The active scalar rule, translation sign, factor (1/2), Lorentz-generator sign, and Hermiticity convention are mutually consistent. |
| Poincare law and algebra | `U067`, `U068`; note 6 / PDF 11; video `01:07:33.240-01:08:47.880` | Expansion of the semidirect-product law gives the printed translation slot and both commutators with the displayed signs. |
| Free energy-momentum generator | `U076A-C`, `F-000277`, `F-000279`, `F-000281`; note 7 / PDF 12; video `01:14:27.659-01:15:43.550` | The note's un-hatted component symbols and the board's explicit hats denote the same operators. The sidecar records the note-board distinction. |
| Scalar expansion | `U080`, `U081`, `F-000295`, `F-000297`, `F-000299`; notes 7-8 / PDFs 12-13; video `01:17:04.560-01:18:04.729` | The radical covers ((2\pi)^{D-1}2\omega_{\vec p}). The operator order, Fourier signs, and (p\cdot x=\vec p\cdot\vec x-\omega_{\vec p}x^0) make the field Hermitian under `N001`. |
| Scalar commutator | `U085`; note 8 / PDF 13; no oral derivation | Direct use of the oscillator algebra gives (1/[(2\pi)^{D-1}2\omega_{\vec p}]) and (e^{ip\cdot z}-e^{-ip\cdot z}), with no extra factor of (i). |
| Covariant measure | `U086`; note 8 / PDF 13; aligned claim `01:18:04.739-01:18:35.390` | Integrating (dp^0\,\theta(p^0)\delta(-(p^0)^2+\omega_{\vec p}^2)) gives (1/(2\omega_{\vec p})). The normalized (d^D p), mass-shell sign, denominator, and (SO^+(1,D-1)) scope are correct. |
| Microcausality proof | `U087`, `U088`; note 8 / PDF 13; aligned claim `01:18:04.739-01:18:35.390` | A proper orthochronous transformation reaches an equal-time frame for spacelike (z). The remaining integrand is odd under (\vec p\to-\vec p), so the commutator vanishes. |
| Covariance check and final Q&A | `U089`, `U090`, `F-000303`, `V-T000314`, `V-T000316`, `V-T000317`; notes 8-9 / PDFs 13-14 and note 7 / PDF 12; video `01:18:19.080-01:20:36.000` | The text distinguishes the stated covariance property from its deferred oscillator-level verification. The partly inaudible final question is a labeled sense gloss and introduces no unsupported formula. |

## Render note

The current PDF has 19 A4 pages with embedded subset fonts. Every displayed
equation is legible. The log reports one 42.55591 pt overfull line at TeX line
1265, the near-verbatim inline Hamiltonian in `T000277`; it remains inside the
physical page edge. This is a reflow issue for the render review and does not
change the formula.

Unresolved blockers: MATH-B05 (the 95-record provenance ledger does not describe the current 231-source-unit near-verbatim chapter)
