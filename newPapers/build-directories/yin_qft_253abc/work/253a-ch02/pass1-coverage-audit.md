# Pass 1 coverage audit

This audit uses the repository evidence and the recorded source PDF. The governing scope files were read in full. They identify Chapter 2 as the span from physical page 20 through physical page 62, with Problem Set 2 on pages 63 through 67 and the Chapter 3 divider on page 68. The Pass 1 source-map status remains `Pass 1 reconciled; transcript freeze pending`.

## Source identity

`SOURCE_MANIFEST.yaml:4-8` gives the source PDF as `/Users/wlancer/Desktop/IAS/phy/qft/qft_253abc_book.pdf` with canonical SHA-256

`9e5e4d241fffffa56c1c3df6dce4b83178f75787dd5d794a18c5d0c087769f21`.

The local PDF hash matches that value. `chapter-metadata.json:400-568` records 24 video sources, covering JSON3, VTT, and MP4 files for the six core lectures and the two later boundary recordings. Every recorded byte count and hash matches its local file.

## Physical-page coverage

`chapter-metadata.json:136-394` contains an exact page map for physical pages 20 through 62. Page 20 is the structural Chapter 2 divider and has no handwritten note-page assignment. Pages 21 through 62 map to original note pages 10 through 51. The mapping contains 42 physical note pages.

`synthesis-lanes/page-dispositions.jsonl:1-42` contains 42 reviewed records. The physical-page sequence is exactly 21 through 62, and the note-page sequence is exactly `253a:10` through `253a:51`. Every record has disposition `included`.

The 21 note source lanes run through the consecutive pairs `notes-021-022.md` to `notes-061-062.md`. Their page-pair mapping produces each physical page from 21 through 62 once. The ambiguity ledger records the same 42-row mapping as `O10` through `O51` to `P21` through `P62` (`notes-ambiguities.md:1236-1303`). The original handwritten numerals are absent in the scans, so the original-page labels remain an evidence-based mapping rather than a visual numeral claim.

Physical pages 63 through 67 carry Problem Set 2 and have no Chapter 2 note-lane or page-disposition record. Physical page 68 carries the Chapter 3 divider. `source-map.md:7-16` and `chapter-metadata.json:112-134` record this as the next boundary. The page-disposition set contains no page from 63 through 68, which keeps the assignment span and the next divider outside the Chapter 2 note-page set.

## Chronological lecture identity and intervals

`playlist.jsonl:1-9` declares recorded UTC date as the chronology basis. The six core rows resolve to the following chronological sequence. `source-map.md:24-34`, `chapter-metadata.json:17-110`, and `alignment.jsonl:2-8` agree on each interval and page range.

| Recorded date | Video | Chapter 2 interval | Physical pages |
|---|---|---|---|
| 2022-09-06 | `96lN2omwit4` | `[00:01:26.700, 01:20:25.500)` | 21–25 |
| 2022-09-08 | `uzixOflp0tY` | `[00:02:50.879, 01:19:02.520)` | 26–31 |
| 2022-09-13 | `M0py5a4RWhE` | `[00:00:02.340, 01:23:02.640)` | 32–39 |
| 2022-09-15 | `vk_RlYUKUyM` | `[00:00:12.660, 01:18:28.140)` | 40–48 |
| 2022-09-20 | `3VG2kDHso08` | `[00:01:10.080, 01:18:54.780)` | 49–55 |
| 2022-09-22 | `TtMNnZ8__UU` | `[00:00:14.179, 00:51:10.020)` | 56–62 |

All six starts and ends occur at checked source-VTT cue boundaries. The interval convention is half-open, `[start,end)`. The playlist positions for these six rows are 3, 9, 4, 10, 1, and 6; their recorded dates establish the chronological lecture order.

The later recordings `82__84nYd4I` and `ph3wE8cFMmk` are dated September 27 and September 29. Their first substantive or coherent material begins at `00:00:26.119` and `00:00:23.279`, respectively. Their source lanes serve as post-Chapter 2 boundary evidence. The six-lecture Chapter 2 sequence ends with the September 22 recording.

## Page-62 and page-68 boundary

The last page-bearing claim assigned to page 62 occurs at `TtMNnZ8__UU:00:50:15.599`. The same source records a close cue from `00:50:22.579` to `00:50:29.280`, followed by a closing recap from `00:50:29.280` to `00:51:10.020`. The operational Chapter 2 endpoint is therefore `00:51:10.020`, including the recap. The next bridge begins at `00:51:10.020` with “But before that”, and the first explicit Chapter 3 topic begins at `00:51:15.660` (`source-map.md:81-100`, `alignment.jsonl:9`).

This preserves the page-bearing endpoint at `00:50:15.599` while retaining the recorded closing material through the half-open interval endpoint. The boundary alignment spans `[00:50:22.579, 00:51:15.660)` across page 62 and the page-68 divider. Page 68 is the next source boundary, with the assignment pages 63 through 67 between the two spans.

## Transcript and caption-lane integrity

`transcript.raw.vtt` contains 77,583 lines and 19,380 cue blocks. Its SHA-256 is

`b74eced69262827b17a84ab03e00049f82d1b1b14869f624f6df4bd6b6d8fbbe`.

The file has six sections in the same chronological order as the table. Their cue counts are 3,177, 3,373, 3,363, 2,911, 3,213, and 3,343. Each section’s complete cue-timestamp sequence matches its corresponding source VTT sequence. The section boundaries and source identities remain distinct throughout the raw stream.

The raw caption-lane manifest has 45 records (`raw-caption-lane-manifest.jsonl:1-45`) covering the six core videos. The lane intervals are contiguous within each video and cover the full recorded caption duration:

| Video | Lanes | Coverage in milliseconds | Raw events |
|---|---:|---:|---:|
| `96lN2omwit4` | 8 | 0–5,412,000 | 1,589 |
| `uzixOflp0tY` | 8 | 0–5,128,000 | 1,687 |
| `M0py5a4RWhE` | 8 | 0–5,102,000 | 1,682 |
| `vk_RlYUKUyM` | 7 | 0–5,007,000 | 1,456 |
| `3VG2kDHso08` | 7 | 0–4,762,000 | 1,607 |
| `TtMNnZ8__UU` | 7 | 0–4,796,000 | 1,672 |
| Total | 45 |  | 9,693 |

Every recorded JSON3/VTT caption hash in the raw-lane manifest matches the local caption file. Every recorded raw-lane SHA-256 matches its lane file. The manifest contains no missing, repeated, overlapping, or gapped lane interval.

## Recorded provenance discrepancy

The local source PDF and all governing metadata use the canonical hash above. The source-lane prose at `source-lanes/video-3VG2kDHso08.md:11` records a 60-character value:

The `video-3VG2kDHso08.md` source-identity field was corrected to the canonical
64-character digest
`9e5e4d241fffffa56c1c3df6dce4b83178f75787dd5d794a18c5d0c087769f21`.
The actual PDF hash, the 24 recorded video-source hashes, the 45 raw-lane
hashes, and the other source-lane provenance records pass their local checks.

## Ambiguity and pending artifact

The source lanes and `synthesis-lanes/notes-ambiguities.md` retain unresolved glyph, formula, diagram, and ASR readings as source ambiguities. The audit found no silent page omission or duplicate note assignment. The zero-omission record at `notes-ambiguities.md:1283-1303` agrees with the page map, dispositions, source lanes, and boundary records.

`work/253a-ch02/synthesis-lanes/notes-exact-b.tex` is pending. `notes-exact-b-alt.tex` is present as an alternate artifact under the synthesis lane, while the requested canonical filename remains absent. This is pending work for the next stage and does not block the Pass 1 coverage audit.

Unresolved blockers: none
