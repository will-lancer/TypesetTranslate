# Pass 2 audit: vk_RlYUKUyM

## Scope and evidence

This independent audit covers all seven completed Pass 2 lanes for vk_RlYUKUyM:

- 000000-001200
- 001200-002400
- 002400-003600
- 003600-004800
- 004800-010000
- 010000-011200
- 011200-012327

The six binding documents were read in full. The audit follows the lane contract in
work/253a-ch02/dispatch_luna_pass2.sh and compares each raw lane, expected output,
the frozen raw-caption-lane-manifest.jsonl, source-lanes/video-vk_RlYUKUyM.md,
notes-037-038.md through notes-047-048.md, and the frozen source interval. The
recorded source PDF SHA-256 is
9e5e4d241fffffa56c1c3df6dce4b83178f75787dd5d794a18c5d0c087769f21.

## Frozen interval and page authority

The video report gives these source intervals.

| Video interval | Physical pages | Handwritten notes | Topic |
|---|---:|---:|---|
| 00:00:12.660-00:14:07.439 | 37-40, with spoken cross-reference to 26-29 | 26-29, cross-reference 15-18 | Gaussian functional integral, real/imaginary time |
| 00:14:13.220-00:21:06.199 | 41 | 30 | Example 2 and oscillator action |
| 00:21:12.360-00:31:00.719 | 42 | 31 | Denominator and expansion in g |
| 00:31:00.720-00:43:57.779 | 42-43 | 31-32 | Wick contractions and order-g^2 discussion |
| 00:44:31.160-01:07:07.798 | 44-45 | 33-34 | Connected components and exponentiation |
| 01:07:07.799-01:12:38.459 | 46-47 | 35-36 | Z, log Z, and ground-state projection |
| 01:12:38.460-01:17:27.419 | 47-48 | 36-37 | Energy correction and Hamiltonian comparison |
| 01:17:56.880-01:20:16.460 | 48 | 37 | Numerator handoff and convergence qualification |

The page map used for every segment and formula authority is
26→15, 27→16, 28→17, 29→18, 37→26, 38→27, 39→28, 40→29,
41→30, 42→31, 43→32, 44→33, 45→34, 46→35, 47→36, and 48→37.
All segment note_pages and formula-authority note_pages equal the mapped
pdf_pages. The 003600-004800 lane therefore records [31,32] for physical
[42,43], [32] for physical [43], and [33] for physical [44].

## Exact event coverage

| Lane | Raw events | Transcript segments | Source-event range | Raw SHA-256 | Exact coverage | Blank lines |
|---|---:|---:|---:|---|---|---:|
| 000000-001200 | 174 | 18 | 1-347 | b12b7dc6b79301eb33614c7638a5ca68aa49780af37adcd59ac8d8a236cbab2f | pass | none |
| 001200-002400 | 256 | 33 | 349-859 | bdd19042ab06b1331b71ede5098ace5be7015b0a0625fc9f1b455a4e0427be83 | pass | none |
| 002400-003600 | 215 | 23 | 861-1289 | 585258a7009a595c2b17b301276c24ff7f3c5e49d6b9231eb282825296ea9ae7 | pass | none |
| 003600-004800 | 199 | 20 | 1291-1687 | 9bcf10f505e10a805178392af7efb86c52f21a7f5324ce6a70625d6ea4f35e84 | pass | none |
| 004800-010000 | 198 | 12 | 1689-2083 | 044e21cd811aa2df64d13ed3f99207c197bf0d77baac30e2fa32f71771b942bc | pass | none |
| 010000-011200 | 225 | 22 | 2085-2533 | 61213d2d020d74199ae28a14b900dc9202acda5ca2676016dececf174707803d | pass | none |
| 011200-012327 | 189 | 17 | 2535-2911 | a9efc9f62b2c1f4f140f79cf5b614a3a3430d3d65201657532548de151eaab4d | pass | none |

The seven lanes contain 1456 raw events. For every lane, the validator loaded
the raw event indices, checked one-to-one ordered consumption, compared each
output raw_text to the single-space concatenation of its assigned raw events,
and compared output start/end to the first and last assigned raw-event times.
All seven checks pass. Each output has one lane_audit row with matching counts,
first and last source indices, and coverage_exact: true. No duplicate, missing,
or out-of-lane event index occurs.

Current expected-output SHA-256 values are:

- 000000-001200: 7fa18d4394793407ceaec5c9f437d5bf963ad8dabe162d5583412f972476bc3c
- 001200-002400: ca30b6234458a700089f99529fc827e16dc5892bd55e61a659b5a780821f18c3
- 002400-003600: 243a0d73dc5e75d57d1043b4cdb8cbd09bc9b498fc1b2888f9f68032f4b10bb0
- 003600-004800: 8732d9eb2d709171db7235299c77366543be2013442148f995d7a5d9e63bb97d
- 004800-010000: f595460dc52030483ca1b28cf60b75044ee99576cd9f5eda825c3f3d3805ccfe
- 010000-011200: c89605384ae1a64b8ae40a9d05b8d0ee70c7b14332f676608b8ab8bbdb4d1b62
- 011200-012327: b1895bb72c10f823407b63a283edd32a43347cfa446c3cb5b6cc67d20d404867

## Cleanup, source authority, and notation

Raw evidence is unchanged. Cleanup removes fillers, logistics, music, and
unusable fragments only through recorded operations. The first lane's
low-confidence ASR is now bracketed in cleaned_text, including the phrases
around “correlation like the whole body,” “there's no how and how to
arbitrary,” “the anti-convention,” “doesn't care about the weather,” the
real/imaginary-time equation words, “energy potential and release this,”
“significant values,” “time boilers,” and incomplete trailing clauses. The
foreign plus music interval at 00:07:17.160 is
unusable_uncertainty: [Music] is omitted and foreign is retained as an
unresolved low-confidence ASR marker.

The Example 2 segment now preserves the exact page-41 quoted heading
“an harmonic oscillator.” The connected-graph notation uses \ell, m_\ell,
G^{(\ell)}, and \ell! throughout the repaired 004800-010000 formulas. The
grouping denominator includes the visible centered multiplication dot:
\prod_{\ell\ge1}(\ell!)^{m_\ell}\cdot m_\ell!. The exponential step uses
(\frac{1}{\ell!}G^{(\ell)})^{m_\ell} and
\exp(\sum_{\ell\ge1}\frac{1}{\ell!}G^{(\ell)}). The 004800-010000 music
marker is absent from cleaned_text, matching its remove_nonspeech operation.
The 011200-012327 “number three” phrase is bracketed as unresolved, matching
its uncertainty operation and the source report.

Questions and qualifications remain in the output. Checked examples include
the denominator normalization exchange, the expectation-value factorization
question, the connected-versus-disconnected order-g^2 divergence question,
the “feature, not a bug” joke, the finite-range normalization qualification,
the zero-radius perturbative-series warning, the small-g qualification, the
first-order correction check, and the numerator handoff. The room exchanges
remain marked where their captions are sparse.

## Formula and LaTeX checks

The source-backed Gaussian Green function, oscillator actions, denominator
expansion, order-g and order-g^2 terms, connected-component count, connected
graph exponential, log-Z relation, first-order energy correction, Hamiltonian
comparison, and convergence example are represented in the relevant lanes.
A JSON parse and math scan over cleaned_text, formula-authority items, and
equations found 390 dollar delimiters, all paired, with balanced braces and no
malformed JSON escape. Every formula authority page set also passes the frozen
physical-to-handwritten page map.

## Cross-lane seams

Source-event ranges advance contiguously by the raw caption sequence:
347→349, 859→861, 1289→1291, 1687→1689, 2083→2085, and 2533→2535.
Rolling captions overlap in time at 00:12:00, 00:24:00, and 00:48:00. The
00:36:00 transition and the 00:59:44→01:00:04 transition contain the board
or room gaps identified by the video report. The final lane's frozen interval
ends at 01:23:27.000 while its raw sequence reaches 01:23:28.159; that
rolling-caption extension is preserved in outside_section_tail records.
The 01:18:28.140 cue is allocated to post_core_boundary with “Next time.”
retained exactly once. No seam loses an event.

## Findings

1. Exact raw-event coverage, raw text, timestamps, lane audits, manifest hashes,
   page mappings, formula delimiters, and cross-lane seams pass.
2. The source-authority repairs requested for the seven lanes are present:
   handwritten note mappings in 003600-004800, exact Example 2 wording,
   \ell notation and source factor order, music cleanup, bracketed ASR, and
   the 011200-012327 boundary/number-three uncertainty alignment.
3. The audit records no remaining strict or source-authority blocker.

Unresolved blockers: none
