# Written-prose-first workflow

Read `SOURCE_MANIFEST.yaml`, `AGENT_POLICY.md`, `WRITING_STYLE.md`, and
`CHAPTER_PLAN.md` before starting a chapter. The project uses five passes.

## Pass 1: full source capture

Use Luna Max Fast, the default subagent. Divide the notes and candidate lecture
videos into bounded lanes with nonoverlapping writable outputs. Use short
overlaps at video boundaries. Use as many useful lanes as the source supports,
up to 50 simultaneous subagents. Do not impose a smaller fixed cap or create
artificial work to reach the ceiling.

Produce a source map, exact note transcription, raw transcript, alignment,
keyframes, ambiguities, and page dispositions. Capture every recoverable word,
question, joke, example, qualification, equation, diagram, and meaningful note
mark. Preserve the raw material without polishing it.

The lead reconciles lane boundaries and confirms complete source coverage.

## Pass 2: literal transcript cleanup

Use Luna Max Fast, the default subagent. Repair the raw transcript from the
audio, exact notes, and frames. Remove caption duplication, clipped seams,
ellipsis artifacts, broken restarts, and recognition errors settled by source
evidence. Preserve meaningful repetition and Yin's characteristic wording.

Repair, boundary, formula, and independent transcript-audit lanes may run in
parallel up to the same 50-subagent ceiling whenever the work divides cleanly.

Record each repair and its evidence. Produce transcript dispositions, verify
continuous coverage, and freeze the minimally cleaned transcript. Later passes
do not rewrite it.

## Pass 3: chapter drafting

Use only `gpt-5.6-sol` at `xhigh`. The editor and any reviewing subagent read
the whole chapter source packet. Across passes 3 through 5, no more than eight
agents running at this model and reasoning level may be active at once across
the complete task tree.

Create a compact argument map. Each unit records its conceptual job, source
span, notes, equations, examples, caveats, voice cues, and intended paragraph
structure. Preserve source order unless an exception is recorded.

Write the complete chapter from the argument map, exact notes, transcript, and
frames. Merge transcript fragments into coherent paragraphs. Remove classroom
mechanics and place long mathematics in displays. Maintain source comments,
provenance, and page and transcript dispositions while drafting.

The draft already satisfies the mechanical rules in `WRITING_STYLE.md`.

## Pass 4: editorial balance

Use a fresh `gpt-5.6-sol` `xhigh` reader on the complete draft and source
packet. This is one large prose pass.

Remove remaining floor holding, board narration, transcript seams, empty
repetition, and spoken syntax that does not work in print. Restore vocabulary,
cadence, qualifications, reader address, questions, jokes, and deliberate
repetition lost during drafting. Check paragraph structure, connectives, and
referents at the same time.

Update `style-exceptions.jsonl` and `voice-restoration.jsonl`. Record the pass
in the writing ledger.

## Pass 5: fidelity and release

Use `gpt-5.6-sol` at `xhigh` for chapter-scale source and mathematical
judgment. The lead editor owns the final build and release decision.

Inside this single pass:

- compare every equation with the notes and clear frames;
- check source coverage, examples, caveats, terminology, and retained voice;
- verify provenance and dispositions;
- build the book and inspect every affected rendered page;
- run strict mechanical, source, math, layout, font, and artifact-identity
  checks.

Record the findings in one `review-final.md`. End it with
`Unresolved blockers: none` or a precise blocker list. A content change requires
the affected checks to be rerun before release.

## Canonical ownership

One editor modifies the canonical chapter at a time. Parallel agents in passes
3 through 5 write separate findings or proposed patches. Source agents in
passes 1 and 2 may write concurrently only when their outputs do not overlap.

## Acceptance

A chapter is complete when:

- the source packet and cleaned transcript are frozen with hashes;
- the argument map covers the chapter;
- every source page and transcript interval has a disposition;
- every substantive paragraph, equation, and figure has provenance;
- the editorial balance pass is recorded and every required voice cue survives;
- `review-final.md` has no unresolved blockers;
- the strict build passes and every affected PDF page has been inspected;
- the exported PDF is byte-identical to the verified build.

Run:

```sh
./build_and_verify.sh --draft
./build_and_verify.sh
```

The Chapter 1 pilot retains its earlier separate review and pass ledgers as
historical evidence. New chapters use this five-pass workflow.
