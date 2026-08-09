# Near-verbatim packet audit

## Scope

Audited on 2026-08-08 against the frozen source
`work/pilot/transcript.cleaned.jsonl`.

| Check | Result |
|---|---|
| Frozen transcript SHA-256 | `5ac8ac5fb25a3235d8fa11b2b6be99b5f2bb9329d307c4045629544f4e43e9bd` matches the contract. |
| Packet files read | `01-0502-1500.tex` through `08-7500-8013.tex`, plus `10-speaker-qna.md` and `11-verbatim-contract.md`. |
| Contract pool | 198 eligible records, 6,542 eligible lexical words, 103 excluded in-scope records, and 64 formula-bearing eligible records. |
| Packet source order | The source-marker sequence increases from `T000016` through `T000316`. The mixed-speaker repetitions of `T000141`, `T000145`, `T000149`, and `T000151` stay in their canonical positions. |
| Speaker handling | The packet separates student speech from Yin's replies where the speaker map permits it. The partially recoverable questions retain a bracketed uncertainty or sense gloss. |
| Compression/paraphrase scan | The packet preserves the canonical sentence order and local discourse pivots across the eight lanes. I found no summary prose substituted for eligible lecture speech. |

## Packet-stage integration requirements

All five requirements below are satisfied by the current marked chapter and
its two sidecars. They remain here as the trace from packet to chapter.

1. `YIN-OY-T000317` is absent from every fragment. It is the contract's one-word
   boundary carryover, `thing`, at `01:20:13.920`. The chapter now has its own
   block immediately after `T000316`, so the closing sentence reads “construct
   this thing.”

2. The fragments are a full working packet. They contain 276 distinct source
   IDs: 197 eligible IDs, 78 in-scope excluded IDs, and separator `T000311`.
   The final chapter must contain exactly the 198 eligible IDs. The 103
   excluded records belong in `verbatim-omissions.jsonl`, rather than in
   source-linked printed blocks.

3. The fragments split a few canonical containers around classroom turns. The
   final chapter must use one begin/end pair per eligible record. In particular,
   `T000141`, `T000145`, `T000149`, and `T000151` each require one combined
   record block after the unsafe student wording has moved to a documented
   omission or an editorial passage outside the block.

4. `T000149` must retain only the Yin portion after `[Yin:]`; `T000314` must
   retain only “For now, yes.” in its source-linked block. Their student
   content has the contract's pre-baseline omission status. The speaker map
   supplies a print-safe sense gloss if the chapter needs to mention either
   question.

5. Six formula-bearing eligible records in the opening lane have prose and
   broad note-page placeholders, rather than individual displayed formulas in
   their fragments: `T000041`, `T000043`, `T000044`, `T000048`, `T000049`, and
   `T000050`. The equation-interleave map must supply their individual
   formula-ledger rows, note/PDF page links, and allowed source classes. The
   remaining 58 formula-bearing eligible records have packet-level formula or
   note anchors.

## Uncertainty and speaker audit

The 24 secure-portion records in the contract remain marked in the packet.
Their bracketed material is visible as uncertainty rather than supplied as
new dialogue. The speaker map correctly withholds unstable student wording,
including the questions around state creation, the scalar-field assumption,
the first-order-unitarity exchange, and the final construction question.

The packet's speaker typography varies between `Yin` and `Xi Yin`. This is a
typographic inconsistency only. Use `Yin` consistently in the chapter.

## Chapter-versus-packet audit

The integrated `latex/chapters/253a/chapter01.tex` now has 198 begin markers,
198 matching end markers, and 198 unique source blocks. `T000317` is present
as its own source block and supplies the required closing word, `thing.` The
two sidecars contain 103 record-exclusion rows and 64 formula-ledger rows.

The strict trace now passes after the TeX-to-text normalizer gained balanced
`\ensuremath{...}` handling and numeric-script normalization, with two
regression fixtures for `T000221` and `T000237`. It reports all 6,542 contract
lexical words in source order, with full per-record recall and precision:

```text
eligible_records=198
excluded_scope_records=103
represented_words=6542
global_recall=1.0
formula_ledger_records=64
hidden_text_blocks=0
normalization_fixtures=2
status=PASS
```

A direct chapter scan also found zero uses of `\llap`, `\rlap`, `\phantom`,
`\hphantom`, and `\vphantom`. The formula records use visible mathematical
typesetting; no hidden-token layout workaround contributes to the trace.

Unresolved blockers: none.
