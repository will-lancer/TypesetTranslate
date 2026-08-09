# Near-verbatim source-fidelity review

Review result: blocked by stale ledgers. The current chapter text passes the frozen near-verbatim content trace.

## Acceptance counts

| Check | Observed | Result |
|---|---:|---|
| Frozen transcript SHA-256 | `5ac8ac5fb25a3235d8fa11b2b6be99b5f2bb9329d307c4045629544f4e43e9bd` | Matches the contract and the canonical file. |
| Eligible source records | 198 | One begin/end block per record, 198 unique IDs, exact transcript order. |
| Eligible lexical words | 6,542 | The strict contract audit aligns 6,542 of 6,542 words in source order, recall 1.000000. |
| In-scope exclusions | 103 | Exactly 103 `record_exclusion` rows, with the excluded ID set equal to the contract set. |
| Span omissions | 62 rows across 49 records | Every eligible uncertainty span has a sidecar row. |
| Formula-bearing records | 64 | Exactly 64 sidecar rows and 64 unique formula IDs in their corresponding record blocks. |
| Formula source classes | 64 | 36 `SPEECH_CLEAN`, 14 `EQUATION_NORMALIZED`, 9 `NOTES_EXACT`, 3 `SOURCE_CONFLICT`, 2 `SOURCE_COMPOSITE`. |
| Note-page coverage | 9 pages | Chapter record markers cover note pp. 1 through 9 and PDF pp. 6 through 14. Formula rows cover every formula-bearing page, with every PDF page equal to note page plus five. |
| Hash references | 706 rows | All 382 transcript-disposition, 95 provenance, 165 omission, and 64 formula rows cite the frozen transcript hash. |

The baseline and masks come from `verbatim-sections/11-verbatim-contract.md:18-52`. The rejection rules bar substitution, compression, reordering, silent removal, and supplied transitions at lines 131-155. The 198-record, 103-exclusion, per-record, and formula gates appear at lines 157-176.

## Text, order, uncertainty, and Q&A

The 198 printed blocks trace the complete eligible sequence from `T000016` through `T000317`. The alignment found no paraphrase, generic compression, clause reordering, or unsupported bridge inside a source-linked block. The strict audit reports `hidden_text_blocks: 0`; a direct scan also found no `phantom`, zero-width box, white-text, or conditional-suppression construction.

The 24 secure-portion records preserve their uncertainty as bracketed text, while the lexical gate excludes those labeled spans. `T000149` prints the sense gloss outside its eligible words and retains Yin's exact answer, matching `verbatim-sections/10-speaker-qna.md:65-71` and `chapter01.tex:724-726`. `T000314` labels the question as a sense gloss, marks Yin's speaker assignment as likely, and retains only “For now, yes” as eligible speech, matching the Q&A audit at lines 134-143 and the chapter at lines 1473-1476. Speaker labels in the recoverable mixed-voice records follow the speaker map. No unstable student wording is presented as verbatim dialogue.

The half-open boundary is correct in the chapter. `T000316` ends with “construct this” and `T000317` supplies exactly `thing` at `01:20:13.920`; see `chapter01.tex:1478-1486`. This agrees with the frozen contract at `verbatim-sections/11-verbatim-contract.md:9-16` and the speaker audit at `verbatim-sections/10-speaker-qna.md:143`.

The 64 formula links use allowed source classes, cite nonempty note and PDF page sets, carry unique printed IDs, and have `math_reviewed` status. Their note/PDF mapping agrees with the exact-note page boundaries in `notes-exact.tex:37,112,139,175,225,289,377,429,476`. Page 2 contributes prose and diagrams but has no formula-bearing eligible record, which accounts for its absence from the formula-page union.

## Blockers

### B1: the provenance and disposition ledgers still describe the removed 95-unit chapter

The chapter now contains 231 source comments: 198 `V-T...` record blocks, 31 retained `U...` note/equation units, and 2 `N...` note units. `provenance.jsonl` still has 95 rows for the earlier compressed chapter. It covers none of the 198 `V-T...` IDs. Only 28 of its 95 IDs remain in the TeX, while 67 provenance IDs point to removed units. In the other direction, 203 of the chapter's 231 current source IDs lack provenance rows.

The same stale unit references remain in both disposition ledgers. `page-dispositions.jsonl` contains 95 unique `included_unit_ids`, of which 67 are absent from the current TeX. `transcript-dispositions.jsonl` contains 88 unique included-unit references, with the same 67 absent IDs. Hash equality therefore establishes source-file identity without establishing source-to-current-chapter linkage. Regenerate these fields against the 231 current source IDs, including all 198 `YIN253A-C01-V-T...` blocks.

### B1: `T000317` is still labeled excluded in the transcript disposition ledger

`transcript-dispositions.jsonl:318` gives `T000317` the fields `chapter_use:"unresolved_excluded"`, `included_unit_ids:[]`, and `disposition:"weak_audio_excluded"`. The contract includes its boundary word, and `chapter01.tex:1483-1485` prints that word in a source-linked block. Update the disposition to record the included boundary token while keeping the later weak-room tail excluded.

The executable strict audit now contains the contract's two TeX normalizations. `T000221` and `T000237` pass without omission rows.

Unresolved blockers: stale provenance and included-unit linkages for the 198-block chapter; contradictory `T000317` transcript disposition
