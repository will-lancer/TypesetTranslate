# Independent Pass 2 audit: `3VG2kDHso08`

## Audit basis

I read `SOURCE_MANIFEST.yaml`, `AGENT_POLICY.md`, `WRITING_STYLE.md`,
`WORKFLOW.md`, `CHAPTER_PLAN.md`, and `MASTER_PROMPT.md` in full. I followed
the lane contract in `work/253a-ch02/dispatch_luna_pass2.sh` and checked the
raw-caption manifest, chapter metadata, `source-map.md`,
`boundary-assignment.md`, `playlist-chronology.md`,
`source-lanes/video-3VG2kDHso08.md`, and the mapped note captures
`notes-047-048.md` through `notes-055-056.md`.

The chapter metadata assigns this recording the interval
`00:01:10.080`--`01:18:54.780`, handwritten pages 38--44, and physical pages
49--55. The video source report extends the recoverable closing qualification
to `01:19:01.510`, then labels `01:19:01.520`--`01:19:04.699` as a low-confidence
`I don't know` tail. The final `um` at `01:19:17.940` is room logistics. The
source PDF hash in the manifest is
`9e5e4d241fffffa56c1c3df6dce4b83178f75787dd5d794a18c5d0c087769f21`.

## Current artifact hashes

The hashes below were recomputed after the source-backed T000639 repair. Raw
caption lanes are unchanged.

| lane | raw lane SHA-256 | cleaned output SHA-256 |
|---|---|---|
| `000000-001200` | `c1730c48064e84846a61136fcf2379221e5fddb8aa57b6a3cc0f09df002085e6` | `fbf80d189aa804502c5961247c38fb80aa0cbb942bd62a7093f1aabb54acd9b4` |
| `001200-002400` | `6bfb241c82783730822f7362b0e9a84cf4c21aee604b436fa04e4947b676a3fb` | `042bfd8f375cb89ce8878b66f55199cb2720e1714a47904f6f61475d81d0bb95` |
| `002400-003600` | `c63df29b9c1a44101051d07303b0b893edc2dd2f58f2e3735d412cd12ab38bde` | `e9328024e989895979f1c39ace904ebaad9c8c6d84986a745801c3c555209871` |
| `003600-004800` | `8b2cfabbbbb549936b29823bc7e76ad06dc9d6a3c161b738cda9999e8e511209` | `0a1025689c6a8b60aa4682ab7f6567584e581accb6e3d4a12467c2d7acdbfa6c` |
| `004800-010000` | `7ad9d4ba33c9f895858f0b7267c2cc70919c8a230f31671f0f57b23472ed4bb3` | `ca4129126dc0b44b5ac44fc0ea0b688bdaf5936a670258e746a067c739cc0d0b` |
| `010000-011200` | `713218a85d675566645855799adfa3997c35eceb17656a07bbcc7f568f91910b` | `65e210d808305a65a5c02327eb2af269fcf5ab6ccce421e92dcdb2e59abe543b` |
| `011200-011922` | `a1c42c1da17326459f5f78da4e6bbbadf7aed4a851e8d17b6791149f85a90188` | `ef1f63f83564f48401887aa7f57fcfd509b9a4a7163f45f0419508b83f1b3f03` |

## Mechanical coverage

Every raw lane and expected output parsed as JSONL. Each output has the
required transcript fields, one `lane_audit` object, and no blank lines.
`raw_text` equals the normalized concatenation of its assigned raw events.
Each transcript start and end equals the first and last assigned raw-event
boundary. The source indices are unique and ordered across every lane.

| lane | raw events | transcript segments | source-event span | exact coverage | cue-start scope |
|---|---:|---:|---|---|---|
| `000000-001200` | 236 | 23 | 1--471 | pass | 28 pre-core, 208 core |
| `001200-002400` | 229 | 19 | 473--929 | pass | 229 core |
| `002400-003600` | 255 | 20 | 931--1439 | pass | 255 core |
| `003600-004800` | 250 | 24 | 1441--1939 | pass | 250 core |
| `004800-010000` | 215 | 20 | 1941--2369 | pass | 215 core |
| `010000-011200` | 253 | 20 | 2371--2875 | pass | 253 core |
| `011200-011922` | 169 | 17 | 2877--3213 | pass | 166 core, 3 post-core |

The seven lanes contain 1,607 raw events and 143 transcript segments. The
flattened output contains 1,607 unique source indices, exactly the raw sequence
`1,3,5,...,3213`. Every lane audit reports matching input and consumed counts,
the correct first and last index, and `coverage_exact: true`.

The three pre-core segments contain the opening logistics and transition. They
finish before the first Chapter 2 cue at `00:01:10.080`. The final lane has an
explicit boundary split. The segment ending with source event 3207 keeps its
cue because that cue starts before `01:18:54.780`; source event 3209 starts at
the boundary and is a separate post-core continuation. The continuation is
retained as the clipped `will result...` with a boundary operation and low
confidence. Source event 3211 is null-cleaned as unusable uncertainty, and
3213 is null-cleaned as logistics. No transcript segment mixes cue-start
scopes.

## Source-page alignment

The page assignments follow the source report and chronology:

| physical pages | handwritten pages | lecture material | output mapping |
|---|---|---|---|
| 49 | 38 | Euclidean two-point expansion, Wick contractions, connected/disconnected factorization | lane 000000 and early lane 001200 |
| 50 | 39 | free Euclidean propagator and Fourier representation | lane 001200, with the p49/p50 overlap retained |
| 51 | 40 | graph orders and the `4 x 3` contraction count | lane 001200 and early lane 002400 |
| 52 | 41 | Fourier routing, 1PI graphs, self-energy, geometric chain | lane 002400 through lane 004800 |
| 53 | 42 | full denominator and spectral decomposition | late lane 004800 and early lane 010000 |
| 54 | 43 | contour residues, energy gaps, and Example 3 opening | lane 010000 and early lane 011200 |
| 55 | 44 | nonlinear coordinate and corrected Hamiltonian | lane 011200 |
| 56 | 45 | spoken derivative-graph and divergence preview | lane 011200 only as overlap metadata |

The output uses handwritten page numbers in `note_pages` and physical PDF page
numbers in `pdf_pages`. Transition records carry both adjacent page pairs where
the report identifies a genuine overlap. Pages 56--62 remain preview evidence;
the direct equations for those pages belong to the successor recording. No
Problem Set 2 page is assigned as a primary lecture page.

## Formula and authority audit

The source equations and notation were compared with `notes-049-050.md`,
`notes-051-052.md`, `notes-053-054.md`, and `notes-055-056.md`:

- the p49 vertex factor is `-g/4!`, the `d tau'` insertion, and the free-line
  `G` factor;
- `G_0(tau)`, its piecewise ordering, and the Fourier denominator
  `1/(k^2+1)` are retained;
- p52 carries the `4 x 3` count, `-g/2`, external `G-tilde_0(k)` factors,
  the `1PI` definition, the amputated self-energy `Sigma(k)`, and the
  geometric chain;
- p53 carries the full denominator, the spectral sum, the complex-k contour,
  and the residue exponent;
- p54 carries the pole relation and
  `1 + g/8 - g^2/32 + O(g^3)`;
- p55 carries the nonlinear coordinate, transformed Lagrangian, corrected
  kinetic term, and Hamiltonian ordering qualification.

The p49 `-g/4!` reading was repaired across the lane seam. Segment 20 now
renders the complete factor, while segment 21 accounts for its leading raw
`factorial` in a cross-segment repair operation before continuing with the
`tau'` integration. The raw events and timestamps remain unchanged.

The audit found 78 transcript records with itemized formula authority: 33
`NOTES_EXACT`, 19 `NOTES_EXACT_AND_FRAME`, 9 `SOURCE_COMPOSITE`, 5
`SOURCE_CONFLICT`, and 12 `SPEECH_WITH_NOTES`. The source-exact authorities
carry plural `note_pages` and `pdf_pages`; the p51 frame authorities retain
their source class, frame list, and items. The five `SOURCE_CONFLICT`
authorities retain their conflict class and video basis because their caption
wording remains incomplete. Formula-like strings in unresolved
graph-orientation or deictic prose carry uncertainty markers and make no
standalone equation claim.

The repaired T000639 record at `00:18:50.039` remains a
`SPEECH_WITH_NOTES` authority on note 40 / physical page 51. Its source-backed
caption repair reads `Wick contraction` for the raw `weak attraction` phrase
and `$q$` for each of the two raw `queue`/`cute` insertions. The final deictic
tail stays `[unresolved]` with its uncertainty operation.

All dollar, `\\(...\\)`, and `\\[...\\]` delimiters are balanced. Braces are
balanced, JSON escaping is valid, and the scan found no malformed backslash
sequence. Formula operations agree with the source page and with the
`cleaned_text` strings.

## Voice, questions, and ASR uncertainty

The cleanup preserves Yin's connective language, questions, qualifications,
homework references, graph-counting exchange, 1PI explanation, contour
motivation, and Hamiltonian-versus-Lagrangian warning. The report's material
recognition clusters are either repaired from the mapped notes or left in
brackets: `harmonic object there is`, `Galaxy integral`, `cubes`, `cues`,
`one Pi`, `ypi`, `posts`, `parody symmetry`, `celebrity perspective`, `video
diagrams`, `naive learning`, and the closing `I don't know`.

Unresolved graph orientation, deictic board references, student questions,
and contour-language fragments carry low or medium confidence together with
an uncertainty operation. The p52 and p54 `SOURCE_CONFLICT` authorities make
the unresolved source layer visible. Nonspeech and room material have explicit
operations. Every null-cleaned segment records its complete lane-local raw text
in an omission field or equivalent operation object with a reason.

## Findings

1. All seven lanes pass JSONL parsing, required-field checks, exact ordered
   event coverage, raw-text reconstruction, timestamp equality, page mapping,
   operation accounting, and delimiter checks.
2. T000639 now carries the source-backed `Wick contraction` reading and two
   `$q$` insertions, with the final deictic speech still bracketed as
   `[unresolved]`. The lane hash table records the repaired output.
3. The remaining low-confidence graph directions, contour fragments, student
   questions, and closing tail are explicitly marked as uncertainty or
   omission operations.

## Repairs and final verification

The audit repairs were limited to source-settled transcript metadata and the
split vertex factor:

1. Completed `-g/4!` across the p49 segment seam.
2. Added source-exact p52 and p53/p54 authorities where the mapped notes fix
   the displayed notation, while retaining `SOURCE_CONFLICT` for unresolved
   readings.
3. Normalized p51 frame authority page keys to `note_pages` and `pdf_pages`.
4. Repaired T000639's `weak attraction` graph phrase to `Wick contraction`
   and rendered the two external insertions as `$q$`, while retaining the
   unresolved final deictic.

The post-repair audit reran JSONL parsing, required-field checks, exact raw
event coverage, raw-text reconstruction, timestamp equality, cross-lane order,
cue-start scope classification, page mapping, authority-page shape, operation
consistency, uncertainty markers, and LaTeX delimiter and brace checks. Every
check passes, including the updated T000639 cleaned-output hash in the table
above.

Unresolved blockers: none
