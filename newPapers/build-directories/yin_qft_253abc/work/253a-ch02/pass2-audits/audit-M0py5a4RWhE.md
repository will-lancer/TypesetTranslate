# Independent Pass 2 audit: M0py5a4RWhE

Audit basis: all eight M0py5a4RWhE raw-caption lanes and cleaned outputs, the raw-caption lane manifest, video-M0py5a4RWhE.md, playlist-chronology.md, boundary-assignment.md, and the mapped note captures notes-031-032.md, notes-033-034.md, notes-035-036.md, and notes-037-038.md. The frozen source report places this lecture on physical pages 32–38, with handwritten note pages 21–27. The recoverable Chapter 2 interval is 00:00:02.340–01:23:40.920. The closing okay at 01:24:12.060 and unresolved information tail at 01:24:32.400 remain separate evidence intervals.

## Current artifact hashes

The hashes below were computed after the source-backed repair pass. Raw lanes were not edited.

| lane | raw lane SHA-256 | cleaned output SHA-256 |
|---|---|---|
| M0py5a4RWhE-000000-001200 | 29f57c42133fe47ff84fa12a8bc13fea58663bd26f23eb9ee2b7532cb56bd4e | fd9d5236d35b87a69b37ec69b8d8e988bd49b5fd595b895867f71d7593127449 |
| M0py5a4RWhE-001200-002400 | dfe61b3ad48d5f744f45a54ff4fc811985f65e89108bc3c7d78fff848dbc8377 | 55baa79e19dfa52a2c23ba56069a5ccdf42b91cc026e24c3154c6ea3221f304b |
| M0py5a4RWhE-002400-003600 | 9215816289f14b9e73096c904f5998c9b23663e916563f32556e472cd9d980d5 | 87145b1728958dbf2e274df8938c6afe21862252628c1bf0eb1f2e13132960f5 |
| M0py5a4RWhE-003600-004800 | 1f671a45ba1562600d63a31a5f643efd3f202470ed4192513dea0a86301cf8a5 | 7d55d6361d61732231c9352d85f7042f394207ec079d3e8264345d3e8c29e5d8 |
| M0py5a4RWhE-004800-010000 | f7515e061fdeb2be5d76a80bc965ef064e422e8c09a1b3683d35c8acbc8cb0ba | 594e046a301d435302aaf7245345cd91dffeb789054db638feb000f38c660d69 |
| M0py5a4RWhE-010000-011200 | c0daa759df4cdd96d0a01662b533340f946e6457623c1a7a1187339c29941ef1 | 42632de5e5ed3de687b65b03eed17e3d9e19a99dde696678c59d6a182ce18195 |
| M0py5a4RWhE-011200-012400 | 0b69090a07805d698a4f25ec89fe54de54acc3d5c1c9a6f38b98dac03684bd9f | f51cfcbb38205dbfcec624141c99b3aa28f8731a3f5971e035f1aa6d133eb31d |
| M0py5a4RWhE-012400-012502 | 4f47220454793ff75c95f0e09a1b4c90a9aae4e409b8391d6ff9a011db731de8 | facede55c3e0c27fb9b924f81131099550027e772b91007ed2b687c8135b6b2b8 |

## Mechanical coverage

Every output parses as JSON. Each file has one lane_audit and every transcript record has the required lane, time, ordered source indices, raw text, cleaned text, disposition, operations, page fields, confidence, uncertainty, and formula-authority fields. Raw text matches the normalized concatenation of its source events, and each segment start/end matches the first and last source event.

| lane | raw events | transcript records | source-index span | exact audit | raw/time checks |
|---|---:|---:|---|---|---|
| M0py5a4RWhE-000000-001200 | 234 | 15 | 1–467 | pass | pass |
| M0py5a4RWhE-001200-002400 | 221 | 24 | 469–909 | pass | pass |
| M0py5a4RWhE-002400-003600 | 254 | 28 | 911–1417 | pass | pass |
| M0py5a4RWhE-003600-004800 | 252 | 21 | 1419–1921 | pass | pass |
| M0py5a4RWhE-004800-010000 | 253 | 13 | 1923–2427 | pass | pass |
| M0py5a4RWhE-010000-011200 | 239 | 15 | 2429–2905 | pass | pass |
| M0py5a4RWhE-011200-012400 | 227 | 21 | 2907–3359 | pass | pass |
| M0py5a4RWhE-012400-012502 | 2 | 2 | 3361–3363 | pass | pass |

The raw lanes contain 1,682 selected events. The outputs consume 1,682 unique source indices in the same order, with no missing or extra event. Lane seams retain their raw one- to two-second timestamp overlaps. The closing and tail records keep cleaned_text null and give complete omission reasons in operations.

The 2026-08-09 rerun parsed all eight JSONL lane pairs. It verified 1,682 raw events, 139 transcript segments, eight lane_audit rows, ordered unique source indices, normalized raw_text equality, segment boundary equality, required field presence, and audit count and span fields. All checks passed.

## Source, voice, and formula checks

The outputs retain the argument sequence from mode covariance and the sum-to-integral limit through contour evaluation, the oscillator correlator, finite-dimensional Gaussian generating functions, four-point pairings, and the functional Gaussian inverse-kernel proof. They preserve finite and infinite T qualifications, arbitrary endpoint data, imaginary-time non-Hermiticity, the direct-infinity warning, contour half-plane choices, normalization cancellation versus the Problem 2 qualification, even and odd Gaussian moments, the function-space rigor limit, the functional normalization warning, and functional integration by parts.

The classroom voice remains present. The bracket-definition question, trivial trivia and really funny aside, Mathematica suggestion, oh my God residue aside, I'll let you figure out the signs, pain and overkill remarks, diagram-counting question, Go home and do all kinds of examples, no-restriction answer, and You have to trust me qualification remain in their source records. Student questions and clipped answers stay marked as questions or uncertainty.

The parsed cleaned_text scan found no actual doubled backslashes, dangling backslashes, or odd dollar-delimiter counts. Formula fragments are delimited where repairs introduced LaTeX notation. Functional mathematical fragments use the source-page lower-case g, with the raw q/Q/g alternation recorded as SOURCE_CONFLICT in the derivative record. The page-37 Dg/Dx normalization inconsistency remains an explicit source conflict. The repaired functional lane's canonical spans T000445 (source events 3107–3131), T000446 (3133–3143), T000449 (3171–3195), and T000451 (3231–3255) now carry explicit SOURCE_CONFLICT authority for the page-37 Dg/Dx normalization mismatch and the raw q/Q/g alternation. Physical pages 37–38 and handwritten note pages 26–27 govern the repaired formulas. Frame checks at the target intervals show the board's lower-case g and functional-derivative notation; they do not resolve the spoken caption fragments, which remain bracketed.

## Repairs completed

1. The opening lane now maps every substantive record to handwritten note 21 and physical PDF page 32. Speech-only record 13 keeps empty page fields. Nested formula-authority page fields were corrected with the same basis.

2. The 00:41:31.940 record now carries note pages 23–24 and PDF pages 34–35 across the p35 generating-function anchor. The 00:42:01.380 record remains on note 24/PDF 35.

3. The 01:06:45.740 record now carries note pages 25–26 and PDF pages 36–37 across the p37 functional-generalization anchor.

4. The functional lane now uses note 26/PDF 37 through 01:15:33.179, carries both page pairs for the 01:15:34.260 crossing record, and uses note 27/PDF 38 from 01:16:02.000 onward.

5. The imaginary-time exponential in 00:18:43.400 is enclosed in math delimiters. The uncertain q-alpha and q-gamma index fragments in 01:00:53.180 are also delimited.

6. Source-exact functional repairs resolve the action shorthand and operator, the linear inverse and identity action, the higher-insertion Wick rule, the functional action shorthand, the g variable in the page-38 derivative calculation, the [Dg] measure, the inverse-kernel result G(tau_1,tau_2), the expectation-value and arbitrary-insertion conclusion, and the delta argument tau-prime minus tau_2. Residual unreadable spans are bracketed and retain their raw captions and uncertainty fields.

7. The four requested semantic spans were repaired in the 01:17:01.199–01:20:22.400 interval. T000445 brackets the unresolved denominator and requested phrase, restores \((A^{-1})_{nm}\), and preserves the open qualification. T000446 brackets the unresolved measure wording and trailing clause. T000449 brackets the unresolved Italian and Q-of-Taiwan/Holy-way speech, restores the \(\tau_1,\tau_2\) labels, and uses the exact page-38 lower-case \(g\) functional derivative. T000451 brackets the unresolved Q phrase, keeps the numerator and first-order differential-operator explanation, and uses lower-case \(g\). Raw text, source-event indices, timing, and the single lane_audit remain unchanged; each repair is recorded in operations.

No source-backed page, delimiter, variable, or functional-lane repair remains outstanding. The Omega-versus-omega glyph in functional record 4 and the page-37 Dg/Dx denominator conflict are source-level conflicts carried explicitly for later notation review. They are not silent canonical edits.

Unresolved blockers: none
