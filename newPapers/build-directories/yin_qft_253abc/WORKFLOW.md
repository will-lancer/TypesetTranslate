# Written-prose-first workflow

The pipeline keeps source recovery separate from textbook writing. Raw captions
and exact notes remain available for audit. The chapter is organized by
arguments rather than caption intervals.

## Gate 0: calibrate the prose

Read `WRITING_STYLE.md` and the reference passages named in
`SOURCE_MANIFEST.yaml`. Record any chapter-specific additions before drafting.
This gate is complete only when the editor can state which spoken habits will
be removed and which characteristic phrases must survive.

## Wave 1: map and transcribe

| Output lane | Writable outputs |
|---|---|
| Source map | `work/pilot/playlist.jsonl`, `work/pilot/source-map.md` |
| Exact notes | `work/pilot/notes-exact.tex`, `work/pilot/note-pages/`, `work/pilot/ambiguities.md` |
| Transcript evidence | `work/pilot/transcript.raw.vtt`, `work/pilot/transcript.cleaned.jsonl`, `work/pilot/alignment.jsonl`, `work/pilot/keyframes/` |

The source map fixes the lecture bounds. The note transcription covers every
source mark, equation, arrow, diagram, marginal note, and meaningful color.
The transcript lane repairs captions minimally and records each operation.

The lead compares all three lanes, resolves source identity and boundaries,
then freezes the evidence packet. No later editorial pass rewrites the cleaned
transcript.

## Wave 2: construct the argument map

Create `work/pilot/argument-map.jsonl` before chapter prose. Each entry must
contain:

- one conceptual job;
- a continuous transcript range;
- note and physical PDF pages;
- the claims, derivation steps, examples, and caveats to preserve;
- equation source IDs and figure placements;
- voice cues worth retaining;
- the intended paragraph structure.

The map must cover the chapter in source order. A transcript record may be
merged into a neighboring argument or omitted with a reason. The map must not
contain polished prose copied from the transcript.

## Wave 3: write the chapter

One editor owns the chapter and its ledgers:

```text
latex/chapters/253a/chapter01.tex
work/pilot/provenance.jsonl
work/pilot/page-dispositions.jsonl
work/pilot/transcript-dispositions.jsonl
work/pilot/style-exceptions.jsonl
work/pilot/writing-style-pass-ledger.md
```

The editor writes from the argument map, exact notes, targeted transcript
spans, and frames. Several source spans normally become one paragraph. Source
comments can occur inside a paragraph without forcing a paragraph break.

The first draft must already satisfy these conditions:

- no `\noindent`, `\ensuremath`, or `\vec`;
- no transcript ellipses or reader-facing uncertainty labels;
- no classroom floor-holding or board narration;
- no large formula in inline math;
- equations appear beside the prose that motivates them;
- characteristic phrases and deliberate corrections remain;
- every source span has a recorded written-use disposition.

Run `python3 scripts/audit_written_prose.py` after the first complete draft.
The audit is a drafting tool. It is not a cleanup step postponed until release.
Before that audit, run
`python3 scripts/render_written_provenance.py --write`. Strict builds rerun the
renderer in check-only mode and fail if the chapter changed afterward.

## Wave 4: make the six passes

Use `templates/WRITING_PASS_LEDGER.md`. Complete the passes in order:

1. structure;
2. filler;
3. voice;
4. logic and referents;
5. mathematics and notation;
6. build and render.

The filler pass records every approved occurrence of a review-required phrase
in `style-exceptions.jsonl`. The voice pass compares the chapter with the voice
cues in the argument map. The math pass checks every display against the exact
note layer.

## Wave 5: review

| Review | Writable output |
|---|---|
| Mathematics | `work/pilot/review-math.md` |
| Source and prose fidelity | `work/pilot/review-fidelity.md` |
| Render | `work/pilot/review-render.md` |

The mathematical review checks signs, measures, normalization, commutators,
Poincare transformations, the scalar-field expansion, and the causality
argument.

The fidelity review checks semantic coverage, source order, terminology,
qualifications, examples, and retained voice. It also looks for transcript
seams, over-compression, invented transitions, and residual classroom speech.

The render review inspects every PDF page for paragraph flow, equation layout,
figures, links, clipping, and readable typography.

Each review ends with `Unresolved blockers: none` or an explicit blocker list.
The lead applies accepted changes and reruns all affected checks.

## Acceptance checks

Strict verification requires:

- exact notes and transcript evidence frozen with hashes;
- a complete argument map in source order;
- complete page and transcript dispositions;
- one provenance record for every `YIN-SOURCE` comment;
- every writing-style pass marked complete;
- every review-required phrase covered by an approved style exception;
- no mechanical prose or notation violations;
- no unresolved source, mathematics, fidelity, or render blockers;
- a compiling PDF with embedded fonts and no overfull boxes;
- page-by-page visual inspection and an export identity check.

Run:

```sh
./build_and_verify.sh --draft
./build_and_verify.sh
```

The old near-verbatim contract and its sidecars are archival evidence from the
pilot. They must never be used to generate or approve a written chapter.
