# Pass 2 audit: TtMNnZ8__UU

## Scope and authority

This audit covers the seven Pass 2 lanes for TtMNnZ8__UU, from 00:00:00.179 through 01:19:57.620. The raw-caption lanes, cleaned outputs, video-TtMNnZ8__UU.md, note-page source lanes for physical pages 55–62, source-map.md, and boundary-assignment.md were checked.

The frozen Chapter 2 core interval is [00:00:14.179, 00:51:10.020). The binding boundary record uses the clear spoken handoff at 00:50:25.680–00:50:29.280 and assigns the first sustained Chapter 3 topic to 00:51:15.660. Physical page 68 is the Chapter 3 divider.

## Exact lane coverage

| Lane | Raw events | Segments | Source-event range | Output span |
|---|---:|---:|---:|---|
| 000000-001200 | 245 | 25 | 1–489 | 00:00:00.179–00:12:03.720 |
| 001200-002400 | 242 | 23 | 491–973 | 00:12:01.860–00:24:04.380 |
| 002400-003600 | 272 | 28 | 975–1517 | 00:24:01.679–00:36:02.579 |
| 003600-004800 | 275 | 22 | 1519–2067 | 00:36:00.480–00:48:02.339 |
| 004800-010000 | 248 | 20 | 2069–2563 | 00:48:00.720–01:00:05.640 |
| 010000-011200 | 239 | 22 | 2565–3041 | 01:00:01.579–01:12:04.739 |
| 011200-011956 | 151 | 14 | 3043–3343 | 01:12:01.800–01:19:57.620 |

The seven lanes contain 1,672 raw caption events and 154 transcript segments. Flattened source_event_indices are exactly 1,3,5,...,3343, with 1,672 unique values. Every lane has one lane_audit with matching input and consumed counts and coverage_exact true. Every segment start and end equals the first and last raw event boundary. Every raw_text value equals the ordered raw-event concatenation after whitespace normalization.

There are 53 null cleaned_text rows: one opening logistics row, two Chapter 2 nonspeech or unusable rows, one nonspeech-excluded music row, one null next-chapter boundary row, 46 post-boundary Chapter 3 rows, one outside-or-unusable row, and one isolated uncertain tail. Each null row retains its complete raw text and an omission reason in operations.

## Boundary audit

The completed boundary repair is consistent with the frozen assignment.

- The 00:50:10.319–00:50:31.020 chapter2_boundary row retains the close cue and uses [unclear] for the unresolved noun phrase.
- The 00:50:29.280–00:51:13.079 boundary_overlap row remains cleaned because every covered raw cue starts before 00:51:10.020. Its cumulative cue end extends past the core endpoint, as allowed for rolling captions.
- The 00:51:10.020–00:51:17.339 next_chapter_boundary row has cleaned_text null, note_pages [], pdf_pages [68], and an explicit omit_outside_chapter2 operation.
- The 00:51:15.660–00:51:57.079 outside_chapter2 row is null-cleaned with pdf_pages [68]. No Chapter 3 words enter the non-null Chapter 2 cleanup.

The clear handoff wording and the first sustained classical-field-theory topic therefore have distinct coverage. The operational endpoint is exact at 00:51:10.020.

## Page-map audit

Direct page arrays now follow the frozen video and note anchors.

- 00:24:01.679 through 00:25:52.559 uses note_pages [47] and pdf_pages [58]; the formula-authority spans on these rows use the same source page.
- 00:30:29.880–00:30:46.980 crosses the 00:30:44.340 page transition and uses note_pages [48,49] and pdf_pages [59,60].
- 00:30:44.340–00:31:24.620 starts on physical page 60 and uses note_pages [49] and pdf_pages [60].
- 00:42:24.599–00:43:04.380 uses note_pages [49] and pdf_pages [60].
- 00:43:01.800–00:43:36.060 crosses the inferred page-60/page-61 transition and uses [49,50]/[60,61].
- 00:43:31.260–00:47:15.319 stays on page 61 with [50]/[61].
- 00:47:26.599–00:48:02.339 is the inferred page-61/page-62 crossing and uses [50,51]/[61,62].

## Schema and source-fidelity audit

All 154 transcript segments have the required fields. Every operations object uses type and, when applicable, omitted. No operation or omitted_text keys remain. All 98 formula_authority objects have class, note_pages, pdf_pages, and items; the other 56 formula_authority values are null. The 22 formerly bare source-reference formula authorities in lane 003600-004800 are object-shaped with page-aligned note and PDF arrays.

All cleaned_text LaTeX delimiters are balanced. The malformed formula-authority equation in 00:03:55.500–00:04:25.440 now ends with its closing dollar delimiter. Raw text and source-event indices were unchanged by every repair. The page-60 counterterm formula is written exactly as
`\Delta L^E=c\cdot g\hbar\frac{q^2}{2}`,
matching `notes-059-060.md`; the same source lane records the corresponding `\Sigma(k)` expansion with `\Lambda/(4\pi)`, `-c`, and the visible `O(g^2)` remainder.

The listed counterterm-lane recognition artifacts are absent from cleaned_text. The repaired text uses source-supported terms for hbar counting, the Lagrangian, counterterms, finite-part and operator qualifications, the energy spectrum, and the energy gap. Unsupported fragments remain [unclear]. Lane 000000-001200 no longer carries source-editorial bracket prose or the raw Animal Hospital marker in cleaned_text. Lane 001200-002400 uses [unclear] for the finite-difference and larger-wave-number markers.

## G4 semantic repair review

The seven formerly flagged counterterm and operator-renormalization spans were reread against `video-TtMNnZ8__UU.md`, the exact note captures for physical pages 60–62, the page map, and the raw events. The current cleaned records preserve Xi's questions, qualifications, connective tissue, and clipped speech while marking unrecoverable words explicitly.

| Segment and interval | Current cleaned excerpt | Finding |
|---|---|---|
| `YIN253A-C02-T000828` `00:37:57.300–00:38:34.500` | `...modify [the Lagrangian] by adding [a term]... include in the Lagrangian of the regularized [theory]...` | The definition of a counterterm remains literal and source-backed. The clipped Lagrangian and theory nouns are bracketed, so no unsupported noun fragment remains. |
| `YIN253A-C02-T000830` `00:39:00.720–00:39:39.780` | `...develop [a counterterm]... At order $g$... some coefficient $c$... this [term] carries $\hbar$... because it's ...` | The order-$g$, coefficient-$c$, and hbar bookkeeping follows the page-60 discussion. The clipped term and final justification retain explicit uncertainty. |
| `YIN253A-C02-T000831` `00:39:37.740–00:40:01.820` | `$\Delta L^E=c\cdot g\hbar\frac{q^2}{2}$... proportional to $q^2$... correcting the frequency of the harmonic oscillator...` | The counterterm equation matches `notes-059-060.md` exactly in field, coupling, coefficient, hbar, and factor of one-half. The frequency-correction explanation is source-backed. |
| `YIN253A-C02-T000834` `00:41:32.460–00:42:01.320` | `...$\frac{\Lambda}{4\pi}$... finite part of the other diagrams... This part of the stuff is [not central].` | The divergent term and finite-part qualification match physical page 60. The clipped relevance cue is marked rather than completed. |
| `YIN253A-C02-T000837` `00:43:01.800–00:43:36.060` | `...correct this propagator term... an order $\hbar$ term... shifting this [term] is the correction we're adding... choose ...` | The propagator correction and order-$\hbar$ status are source-backed. The deictic noun and unfinished choice remain bracketed or ellipsized. |
| `YIN253A-C02-T000844` `00:46:33.900–00:47:15.319` | `[unclear]. Okay, so let me emphasize this important point... $\Sigma(k)$ to have a finite limit... operator itself may need to be redefined or renormalized... [unclear].` | The clipped opening is explicitly uncertain. The finite-`\Sigma(k)` and operator-renormalization claims follow physical page 61, with no invented comparison. |
| `YIN253A-C02-T000845` `00:47:26.599–00:48:02.339` | `...same finite part, and [unclear]... operator $q$... infinite renormalization... but in quantum mechanics [unclear].` | The page-61/page-62 seam is preserved. The final quantum-mechanics comparison is marked uncertain, while the finite-part and operator claims remain source-backed. |

No G4 residual remains in the current cleaned output. The exact note notation check found no counterterm formula mismatch.

## Current cleaned-output hashes

| Output | SHA-256 |
|---|---|
| TtMNnZ8__UU-000000-001200.jsonl | e69ba7298da16338ef639c5ddfe191746c511cf96c62aaccd0a6d799b19ac0fa |
| TtMNnZ8__UU-001200-002400.jsonl | 2852f7a862e215b284a08a768c51a80988ab5a0069e4bab7354968cd4212885f |
| TtMNnZ8__UU-002400-003600.jsonl | a093a55b1c3368bdc19f184c758a6c05d1f1ea5ad538ffd5e39ca17d8a3af81f |
| TtMNnZ8__UU-003600-004800.jsonl | ea51f5ffd6f57d42fe5707b77dd9d1b0669f249ff15e7b780681a560c10d086f |
| TtMNnZ8__UU-004800-010000.jsonl | 2a527802b68c14108f5c5223ef0e0c9121951d6b04c173cdd18789548e0d424c |
| TtMNnZ8__UU-010000-011200.jsonl | ff4634693392fb412af0174eed6b7bfb2a631c38dbdd9b48d439def745d2f3fc |
| TtMNnZ8__UU-011200-011956.jsonl | 695f6d5b02a54b41db5ff1df5ff2b103d0b7d5afb28a4de3f8e7879b0c81cf08 |

Checks passed: exact event coverage, raw text and timing fidelity, one lane_audit per lane, boundary nulling, direct page maps, operation-key normalization, formula-authority object shape, balanced LaTeX delimiters, and cleaned-text residual scan.

Unresolved blockers: none
