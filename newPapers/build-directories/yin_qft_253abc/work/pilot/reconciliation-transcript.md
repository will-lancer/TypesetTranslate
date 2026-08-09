# Wave 2 transcript source freeze

## Verdict

Status: PASS for the source transcript.

The frozen artifact is `work/pilot/transcript.cleaned.jsonl` at SHA-256 `5ac8ac5fb25a3235d8fa11b2b6be99b5f2bb9329d307c4045629544f4e43e9bd`, 580,840 bytes, and 383 JSONL lines. The verdict applies only to that fingerprint and the ten input-packet hashes below.

The file contains one schema-v2 metadata object and 382 timeline objects: 291 source-derived transcript segments and 91 generated coverage segments. All 382 timeline IDs are unique. The numeric sequence covers `T000001` through `T000381`; the optional-lead boundary replaces `T000015` with `T000015A` and `T000015B`.

Every required timeline field parses with the allowed schema-v2 union types. Each interval has positive duration. Stored lexical counts recompute exactly. Seven continuation groups have reciprocal links. The timeline is continuous over `[00:00:00.000,01:31:35.900)`, with zero gaps and zero overlaps.

`transcript-dispositions.jsonl` and `provenance.jsonl` are downstream chapter artifacts. Their semantic content is outside this source freeze while the chapter is rebuilt in near-verbatim form. Retention figures in this report come directly from the frozen canonical transcript.

## Raw source and strict packets

The raw VTT has SHA-256 `46001b0b7c22a4fa76db5ccf88e2c8d83eaf9134062dd564239f4d02f8fdebf9`, size 504,005 bytes, and 3,399 cue lines. The ten packet files contain 290 valid JSON records. Their combined lexical totals are 9,657 raw words and 7,684 cleaned words.

| Packet | SHA-256 | Records | Raw words | Cleaned words |
|---|---|---:|---:|---:|
| `00-00-00_to_00-04-45.jsonl` | `48126553695e487d5c871d07eb34e570b55c8e9881c10eb810529f3eb71dc309` | 13 | 752 | 344 |
| `00-04-45_to_00-15-00.jsonl` | `b9446b8c9889985958e247d1f52b2e943d53d69fa929ff52a0a575c5a06eb5b3` | 37 | 1,226 | 1,041 |
| `00-15-00_to_00-25-00.jsonl` | `c50339923474437e3cb656a914a202c933ab3cace53e51c957debe559060ea28` | 31 | 1,171 | 1,036 |
| `00-25-00_to_00-35-00.jsonl` | `74d15961c8c0862959f2558ae0d8ad04cdbff195058558523b2fd42132440c4c` | 31 | 1,272 | 1,046 |
| `00-35-00_to_00-45-00.jsonl` | `1110a3cb5f7c8bc3688189101478f212a374e161363ac28f133ebcd319f1f5fa` | 26 | 1,148 | 1,010 |
| `00-45-00_to_00-55-00.jsonl` | `419922f0c00d8801222133b26a6bccc0b8c687ccc9081e5f4326a66a60ffd702` | 23 | 1,260 | 1,007 |
| `00-55-00_to_01-05-00.jsonl` | `827c71bc9ec48a197c584c64c884896e33e39bb546aacfcdb8c1ecd237e0677b` | 30 | 1,033 | 856 |
| `01-05-00_to_01-15-00.jsonl` | `596b12549110520dbb1cab29c3a6fbb72f76b991408138355dac8cba50d97c67` | 39 | 989 | 660 |
| `01-15-00_to_01-22-00.jsonl` | `f43f64ad6ed104783f1f2bf9893c16ed4f62ea474a65a57db1684acd38fd2a34` | 31 | 733 | 649 |
| `01-22-00_to_end.jsonl` | `1b9de92d20786b80aaad584e5b01022febd584dc0db8c7d934c8dd85056e436a` | 29 | 73 | 35 |

Every metadata manifest entry agrees with the corresponding file hash, byte content, row count, first and last timestamps, and both word counts. The 290 source rows have no overlap. They leave 91 caption gaps totaling 24.742 seconds. The canonical file represents those exact gaps with 91 coverage records.

All 290 packet rows have source provenance in the canonical file. A single packet row, `00-04-45_to_00-15-00.jsonl` row 1, becomes the two records `T000015A` and `T000015B` at the optional-lead boundary. The concatenated canonical raw stream equals the packet raw stream exactly.

Four cleaned-source differences are fully recorded. `T000141` withholds the unresolved normalization factor. `T000314` replaces partly inaudible student wording with a labeled sense gloss. `T000316` and `T000317` move the word “thing” across the packet-row boundary according to its VTT onset. The joined text of the latter pair reconstructs the source sentence.

## Coverage and frozen boundaries

| Frozen interval | Timeline records | Raw words | Cleaned words | Disposition |
|---|---:|---:|---:|---|
| `[00:00:00.000,00:04:52.520)` | 15 | 756 | 345 | Course setup and classroom logistics |
| `[00:04:52.520,00:05:02.580)` | 1 | 6 | 4 | Optional lead-in |
| `[00:05:02.580,01:19:47.090)` | 295 | 8,714 | 7,201 | Frozen Chapter 1 core |
| `[01:19:47.090,01:19:47.100)` | 1 | 0 | 0 | Ten-millisecond separator |
| `[01:19:47.100,01:20:13.920)` | 5 | 72 | 67 | Clear construction Q&A |
| `[01:20:13.920,01:20:36.000)` | 1 | 1 | 1 | Final boundary word followed by weak room audio |
| `[01:20:36.000,01:21:26.360)` | 4 | 31 | 29 | Music and candidate post-class Q&A |
| `[01:21:26.360,01:31:35.900)` | 60 | 77 | 37 | Outside-section tail |

The core duration is 4,484.510 seconds. It has 239 source-derived records and 56 coverage records. Its lexical retention is 82.6371 percent. Overall retention is 79.5692 percent.

The clear Q&A endpoint follows the half-open convention. The word “thing” starts at `01:20:13.920`, so `T000317`, whose interval begins there, carries it. `T000316` ends with “construct this” and links reciprocally to `T000317`.

Every one of the 60 records beginning at `01:21:26.360` has an `outside_section_*` disposition, `section_status: outside_section`, and a separate `auditory_status`. Raw text and fragmentary cleaned text remain available for later source work.

The downloaded video ends at `01:31:34.282`. The final 1.618 seconds belong only to the caption timeline and already lie inside the outside-section tail.

## Retention by canonical disposition family

The families below partition all 382 records. The source labels and record type determine the family. Fine-grained labels remain unchanged in the JSONL.

| Canonical disposition family | Records | Raw words | Cleaned words | Retention |
|---|---:|---:|---:|---:|
| Retained clear or substantive speech | 169 | 7,032 | 5,879 | 83.6035% |
| Retained speech with marked uncertainty | 34 | 1,325 | 1,119 | 84.4528% |
| Unresolved or withheld speech | 15 | 242 | 174 | 71.9008% |
| Question management and repetition | 12 | 164 | 133 | 81.0976% |
| Setup, logistics, and optional lead-in | 19 | 812 | 341 | 41.9951% |
| Non-speech and writing pauses | 11 | 5 | 1 | 20.0000% |
| Generated coverage and separators within the section range | 62 | 0 | 0 | n/a |
| Outside-section tail, including 29 coverage records | 60 | 77 | 37 | 48.0519% |
| Total | 382 | 9,657 | 7,684 | 79.5692% |

The ratio records lexical survival. Each record's uncertainty, formula authority, and section status control source use.

## Page, frame, and formula alignment

`alignment.jsonl` has SHA-256 `dbfbc0d7454db3fce60c5687120670186fe80060520afddb8dc73b8c22776b5d`, 23 valid records, and nine page alignments. Note pages 1–9 map exactly to combined PDF pages 6–14. All 17 distinct referenced keyframes exist.

Every canonical page pair obeys `pdf_page = note_page + 5`. Substantive core speech has page authority. The only page-empty source records inside the core are two classroom-management records, `T000027` and `T000045`.

Several records use semantic or cross-page evidence beyond the active alignment interval:

| Records | Reconciled page use |
|---|---|
| `T000149`, `T000151`, `T000153`, `T000155` | Q&A during the p.4 interval refers back to p.3 vacuum and operator material. |
| `T000297`–`T000301` | The free-scalar unit begins on note p.7 and its blue phase and frequency definitions continue on p.8. `T000297` carries explicit `NOTES_EXACT` cross-page authority. |
| `T000303`, `T000305` | The spoken covariance and microcausality assertion bridges p.8 and p.9. `T000303` uses `SOURCE_COMPOSITE`; the p.8 derivation remains in the note layer. |
| `T000312`, `T000314`, `T000316`, `T000317` | Post-core construction Q&A refers semantically to the p.7 scalar field and the p.9 closing question. |

The formula audit passes after these explicit repairs:

- Fourteen dagger-bearing records document the exact-note `a^+` to transcript `a^\dagger` normalization. Composite `SOURCE_CONFLICT` records embed that normalization where another source issue is present.
- Eight records document typography-only conversion from exact-note `\hat\phi` to either Unicode `φ̂` or `\widehat\phi`.
- `T000141` withholds the student's factor. Its authority records `$2p^0$` and `$2E_{\vec p}$` as unresolved alternatives.
- `T000263` labels `U\hat\phi U^{-1}` as oral shorthand and records the full note form with `U(\Lambda,a)`.
- `T000279` and `T000281` preserve the visible board and oral hats under `SOURCE_CONFLICT`, while `NOTES_EXACT` retains `\vec P` and `\hat P^\mu=(H,\vec P)`.
- `T000297` fixes the scalar expansion from note pp.7–8 and frames. `T000303` records a spoken assertion supported by both note pages and keeps the detailed commutator proof in the note layer.

The note-p.8 invariant-integral proof and the note-p.9 compact postulate list remain notes-only material. The speech transcript contains Yin's assertions and closing bridge at their actual timestamps.

## Relevant Q&A

The interval `[01:19:47.100,01:20:13.920)` remains relevant. It records the construction question, Yin's admission that the field was supplied for motivation, the claim that its properties can be checked, and his promise of a systematic construction later. `T000314` marks the student's contribution as a sense gloss because its exact words are partly inaudible. Yin's reply is retained.

The weak-room interval begins with the half-open boundary word at `01:20:13.920`. Music follows at `01:20:36.000`. The fragment at `01:21:03.980–01:21:26.350` may concern nonuniqueness of local operators. Missing nouns prevent source-faithful chapter prose. Its disposition remains unresolved.

Material from `01:21:26.360` belongs outside Chapter 1. One later operator exchange around `01:25:28–01:25:46` lacks the noun that would determine its meaning.

## Unresolved source ledger

These source intervals remain explicitly unresolved:

| Records | Interval | Unresolved content |
|---|---|---|
| `T000060`, `T000062` | `00:17:22.140–00:18:56.460` | Exact course allocation and the renormalizability comparison need audio review. |
| `T000092` | `00:26:50.760–00:27:13.919` | The referent in the course-order answer is unstable. |
| `T000112`, `T000114`, `T000115` | `00:34:25.500–00:35:28.329` | Student question, boundary fragment, and quiet continuation remain incomplete. |
| `T000163` | `00:44:05.271–00:44:33.559` | The student question before Yin's answer is unrecoverable. |
| `T000238`, `T000239` | `01:04:40.000–01:05:14.579` | Boundary-crossing Q&A has an unclear speaker turn and damaged reply. |
| `T000242` | `01:05:43.200–01:06:12.200` | The student's question loses its ending. |
| `T000245`, `T000246` | `01:06:38.400–01:07:33.240` | An example and the indexed quantity are missing. |
| `T000252` | `01:08:47.880–01:09:06.480` | The conserved-charge clause is too damaged to use. |
| `T000259`, `T000260` | `01:10:29.820–01:11:09.420` | The unitarity question and weak-room continuation remain unclear. |
| `T000317`, `T000318`, `T000320` | `01:20:13.920–01:21:26.350` | Boundary token, room tail, music, and candidate operator Q&A remain separated by disposition. |

Seven generated coverage records mark uncaptioned intervals that still require audio or frame evidence: `00:36:08.210–00:36:09.480`, `00:36:58.190–00:37:00.480`, `00:37:56.810–00:38:00.260`, `00:38:19.849–00:38:22.140`, `00:38:51.890–00:38:56.240`, `00:41:30.710–00:41:34.160`, and `00:42:24.050–00:42:25.920`.

## Compatibility notes

The canonical transcript uses half-open intervals throughout. `source-map.md` and schema-v1 `alignment.jsonl` retain legacy inclusive-millisecond end labels at several page cuts. Seven adjacent page pairs differ by one millisecond, while the p.3/p.4 cut already shares `00:37:24.780`. A later alignment serializer should express every page cut with one half-open convention. The transcript timeline already supplies exact continuous coverage.

Schema v2 preserves lane-native `confidence` values as either strings or numbers. Operation entries may be strings or structured objects. Consumers should accept both declared unions.

Required corrections to the frozen source transcript: none. New evidence for an unresolved interval would create a new fingerprint and require another reconciliation pass.
