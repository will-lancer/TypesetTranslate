# Master prompt: Xi Yin Physics 253abc textbook

You are the lead editor for a source-faithful textbook project. Work inside:

```text
/Users/wlancer/Coding_Projects/TypesetTranslate/newPapers/build-directories/yin_qft_253abc
```

Read these files in order before acting:

1. `SOURCE_MANIFEST.yaml`
2. `AGENT_POLICY.md`
3. `WRITING_STYLE.md`
4. `WORKFLOW.md`
5. `CHAPTER_PLAN.md`

Inspect git status and preserve unrelated changes.

## Agent execution

`AGENT_POLICY.md` is binding. Use Luna Max Fast, the default subagent, for
full source capture and literal transcript cleanup. Use only `gpt-5.6-sol`
at `xhigh` for chapter drafting, editorial balance, and fidelity and release.

Passes 1 and 2 may be divided into bounded source lanes. Passes 3 through 5
are large-context work whose agents read the whole lecture or chapter under
review. One editor owns the canonical chapter. Parallel editorial agents write
separate reports or proposed patches.

During passes 1 and 2, Luna Max Fast may use up to 50 simultaneous subagents.
Use as many independent lanes as the work supports, without imposing a smaller
fixed cap or treating 50 as a quota. During passes 3 through 5, enforce a hard
limit of eight simultaneous `gpt-5.6-sol` `xhigh` agents across the complete
task tree.

## Goal

Create a coherent JHEP-format textbook from Xi Yin's Physics 253a, 253b, and
253c handwritten notes, problem sets, and lecture videos. The result must read
like written Xi Yin. His book *Foundations of String Theory* is the prose model.
The lecture supplies the content, argument, examples, emphasis, and personality.

The first draft is written exposition. A cleaned transcript is an evidence
layer, not a prose template. The task goal names the chapter to produce. Keep
the work inside that chapter and its boundary evidence.

## Sources

Combined notes and assignments:

```text
/Users/wlancer/Desktop/IAS/phy/qft/qft_253abc_book.pdf
```

Expected SHA-256:

```text
9e5e4d241fffffa56c1c3df6dce4b83178f75787dd5d794a18c5d0c087769f21
```

Lecture playlist:

```text
https://www.youtube.com/playlist?list=PLAd5nTR2YCdoAkJnywB0B9f8cghPSLM9m
```

Written-prose reference:

```text
https://github.com/xiyin137/stringbook
```

Use the reference passages and fingerprint recorded in `SOURCE_MANIFEST.yaml`.
They establish cadence and paragraph construction. They do not add QFT content
to the lecture chapter.

## Chapter 1 reference scope

- Physics 253a handwritten pages 1--9.
- Combined PDF physical pages 6--14.
- Problem Set 1 is on physical pages 15--19. Give it an appendix pointer and
  preserve it for later exercise integration.
- Physical page 20 begins Lagrangian quantum mechanics and supplies the end
  boundary for video alignment.

The completed Chapter 1 source pages cover the opening definition of QFT, the 253a course plan,
relativistic multiparticle states, the free Hamiltonian, locality and
causality, Poincare covariance, microcausality, the free scalar field, and the
postulates leading into a manifestly Poincare-invariant formulation.

## Source hierarchy

The handwritten pages govern equations, notation, diagrams, and mathematical
order. Lecture audio governs exposition, motivation, examples, qualifications,
oral corrections, and characteristic phrasing. Video frames settle deictic
references such as "this term." Problem-set pages govern exercise wording.

Keep the evidence layers separate and immutable after freeze:

1. rendered note pages;
2. exact note transcription;
3. raw timestamped captions or ASR;
4. minimally cleaned timestamped transcript;
5. video-to-page alignment;
6. argument map;
7. written chapter and provenance.

Transcript cleaning remains minimal. It repairs the evidence layer without
turning speech into polished prose. Allowed operations are punctuation,
capitalization, isolated-filler removal, immediate false-start removal,
source-backed caption repair, spoken-math conversion, and removal of classroom
logistics.

## Written-prose drafting contract

Do not assemble the chapter by concatenating transcript records. Do not use a
lexical-retention target. Do not make one printed paragraph for each caption
interval.

Before writing TeX, create `work/<chapter>/argument-map.jsonl`. Each record groups a
continuous run of lecture and note material into one conceptual job. Record the
claim, supporting transcript span, note pages, equations, examples, caveats,
and any phrase or joke that carries Yin's voice.

Draft one argument at a time from that map. Merge adjacent transcript fragments
into paragraphs. Remove floor-holding, classroom questions, board narration,
repeated previews, clipped clauses, and empty sequencing. Repair pronouns and
deictic language from the note or frame evidence. Preserve technical content,
qualifications, derivation order, characteristic language, and deliberate
emphasis.

Begin from Yin's minimally cleaned sentences inside the chosen argument unit.
Keep his vocabulary, cadence, qualifications, reader address, and ordinary
connective language whenever they survive the move to written prose. The voice
is distributed throughout the explanation; it is not confined to jokes or
catchphrases. Prefer the smallest edit that removes a speech artifact. Do not
replace a serviceable Yin sentence with generic textbook prose.

Read `WRITING_STYLE.md` before the first paragraph and again before each
required pass. Its examples are binding. Every conversational phrase listed as
review-required must be justified in `work/<chapter>/style-exceptions.jsonl`.
Every argument-map voice cue must be accounted for in
`work/<chapter>/voice-restoration.jsonl` and present in the hash-pinned chapter.

## Mathematics

Establish every equation from the handwritten page or a clear video frame.
Use the mostly-plus signature visible in the opening notes. Preserve measures,
state normalizations, hats, generator signs, Fourier conventions, and equation
order unless a reviewed `EQUATION_NORMALIZED` record states the change.

Use `\mathbf` for spatial vectors. Reserve inline math for short expressions.
Definitions, transformations, commutators, integrals, field expansions, and
multi-part identities belong in display environments.

## Provenance

Put a compact source comment before every substantive paragraph, displayed
equation, and figure:

```tex
% YIN-SOURCE: id=YIN253A-C01-U001; notes=253a:1; pdf=6; video=VIDEO_ID:00:01:20-00:02:15; class=SOURCE_COMPOSITE
```

Speech-span comments may sit inside a written paragraph. They identify the
evidence absorbed into that paragraph and do not create paragraph breaks.

Write `work/<chapter>/provenance.jsonl`, one record per `YIN-SOURCE` comment. Each
record contains the stable ID, TeX target, source class, note and PDF pages,
video interval, transcript record IDs when applicable, source excerpt, printed
TeX span, editorial operations, confidence, and review status.

Generate the ledger with
`python3 scripts/render_written_provenance.py --write` after each chapter edit.
The strict build checks the generated artifact byte for byte and rejects stale
chapter hashes or printed spans.

Allowed source classes are `NOTES_EXACT`, `SPEECH_CLEAN`,
`SOURCE_COMPOSITE`, `EQUATION_NORMALIZED`, `EDITORIAL_NOTE`, and
`SOURCE_CONFLICT`. Ordinary written transitions derived from adjacent source
sentences remain `SOURCE_COMPOSITE`. Use `EDITORIAL_NOTE` only for content not
present in the lecture or notes.

Give every source page and transcript interval a disposition. The permitted
written-use outcomes are included directly, merged into an adjacent argument,
repetition removed, classroom material removed, uncertainty withheld, outside
the section, and source conflict.

## Required editorial passes

Run the five passes in `WORKFLOW.md`: source capture, literal transcript
cleanup, chapter drafting, editorial balance, and fidelity and release. The
style checks in `WRITING_STYLE.md` belong inside passes 3 through 5. They are
checks rather than additional passes.

## Chapter 1 historical outputs

```text
work/pilot/
  playlist.jsonl
  notes-exact.tex
  transcript.raw.vtt
  transcript.cleaned.jsonl
  alignment.jsonl
  argument-map.jsonl
  voice-restoration.jsonl
  style-exceptions.jsonl
  provenance.jsonl
  page-dispositions.jsonl
  transcript-dispositions.jsonl
  ambiguities.md
  writing-style-pass-ledger.md
  review-math.md
  review-fidelity.md
  review-render.md
  report.md
latex/chapters/253a/chapter01.tex
latex/master.pdf
```

Files under `work/pilot/verbatim-sections/`, `verbatim-omissions.jsonl`, and
`verbatim-formulas.jsonl` belong to the archived pilot experiment. They are not
drafting inputs or release gates.

## Verification and stop condition

Run `./build_and_verify.sh --draft` during composition. Run
`./build_and_verify.sh` only after all five passes and the final review are
complete. Visually inspect every affected rendered page.

The final pilot report records exact note pages, video IDs and timestamps,
transcript minutes, unresolved ambiguities, provenance counts, mathematical
and fidelity findings, PDF page count, build results, elapsed time, and usage
shown by the interface. Leave unavailable usage fields blank.

Treat the book as an internal research edition. Verify permissions before
public distribution for lecture-derived prose, problem sets, Xi Yin's name in
the title and author field, and the intended license.
