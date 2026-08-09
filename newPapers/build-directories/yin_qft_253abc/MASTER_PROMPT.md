# Master prompt: Xi Yin Physics 253abc textbook

You are the lead agent for a source-faithful textbook project. Work inside:

```text
/Users/wlancer/Coding_Projects/TypesetTranslate/newPapers/build-directories/yin_qft_253abc
```

Read `README.md`, `WORKFLOW.md`, `CHAPTER_PLAN.md`, and
`SOURCE_MANIFEST.yaml` before acting. Inspect git status and preserve unrelated
changes.

## Goal

Create a coherent JHEP-format textbook from Xi Yin's Physics 253a, 253b, and
253c handwritten notes, problem sets, and lecture videos. The book has three
parts in that order. Keep the source's topic order and use Yin's written and
spoken wording as closely as readable textbook prose permits.

This run is a pilot. Produce only Chapter 1, "Basic Generalities of Quantum
Field Theory," then stop for review.

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

The playlist had 79 items when this scaffold was made. Inventory it again and
record the observed count. Use the date order to nominate candidate lectures.
Confirm matches from transcript content, visible equations, displayed note
pages, and the boundary with the next section.

## Fixed pilot scope

- Physics 253a handwritten pages 1--9.
- Combined PDF physical pages 6--14.
- Problem Set 1 is on physical pages 15--19. During the pilot, give it an
  appendix pointer and preserve it for later exercise integration.
- Physical page 20 begins Lagrangian quantum mechanics and provides the end
  boundary for video alignment.

The source pages cover the opening definition of QFT, the 253a course plan,
relativistic multiparticle states, the free Hamiltonian, locality and
causality, Poincare covariance, microcausality, the free scalar field, and the
postulates leading into a manifestly Poincare-invariant formulation.

## Source rules

The handwritten pages govern equations, notation, diagrams, and mathematical
order. Lecture audio governs exposition, motivation, examples, qualifications,
and oral corrections. Video frames resolve references such as "this term" or
"the expression here." Problem-set pages govern exercise wording.

Keep these source layers separate:

1. rendered note pages;
2. exact note transcription;
3. raw timestamped captions or ASR;
4. minimally cleaned timestamped transcript;
5. video-to-page alignment;
6. textbook chapter.

Models may draft from transcripts once the note pages and targeted frames are
available. Treat captions and ASR as fallible around formulas. Establish every
equation from the handwritten page or a clear video frame.

Allowed transcript cleaning consists of punctuation, capitalization, removal
of isolated fillers and immediate false starts, repair of caption errors from
source evidence, conversion of spoken mathematics to LaTeX, and removal of
classroom logistics. Preserve Yin's vocabulary, examples, qualifications, and
derivation order. Mark any newly written transition as `EDITORIAL_NOTE`.

Record every uncertain reading or note-video disagreement. Include its note
page, video ID, timestamps, competing readings, decision, and confidence. Keep
the source form until evidence settles the issue.

Use the mostly-plus signature visible in the opening notes. Preserve the
source's measures, state normalizations, hats, generator signs, Fourier
conventions, and equation order. A reviewer must check any proposed
normalization or sign change.

## Provenance

Put a compact source comment before every substantive paragraph and displayed
equation:

```tex
% YIN-SOURCE: notes=253a:1; pdf=6; video=VIDEO_ID:00:01:20-00:02:15; class=SPEECH_CLEAN
```

Also write `work/pilot/provenance.jsonl`, one record per paragraph, equation,
figure, and problem. Each record contains a stable ID, TeX target, source
class, note page, PDF page, video ID and interval, source excerpt, final text,
cleaning operations, confidence, and review status.

Allowed source classes are `NOTES_EXACT`, `SPEECH_CLEAN`,
`SOURCE_COMPOSITE`, `EQUATION_NORMALIZED`, `EDITORIAL_NOTE`, and
`SOURCE_CONFLICT`. Unsupported prose and unresolved source conflicts block the
strict build.

Give every pilot note page and every relevant transcript interval a recorded
disposition such as included, repetition, logistics, outside section,
corrected orally, or unresolved.

## Swarm

Follow the waves and exclusive writable paths in `WORKFLOW.md`. Use up to three
workers at a time.

- Source mapper: inventories the playlist and finds exact pilot video bounds.
- Note transcriber: creates a page-faithful transcription of PDF pages 6--14.
- Transcript worker: preserves raw captions, cleans them minimally, and aligns
  timestamps with note pages.
- Chapter editor: writes the chapter from the frozen source packet.
- Reviewers: independently check the mathematics, source fidelity, and
  rendered PDF. They write reports and leave the chapter unchanged.
- Lead agent: freezes inputs, resolves review findings, edits canonical files,
  runs verification, and writes the pilot report.

## Pilot outputs

```text
work/pilot/
  playlist.jsonl
  notes-exact.tex
  transcript.raw.vtt
  transcript.cleaned.jsonl
  alignment.jsonl
  provenance.jsonl
  ambiguities.md
  review-math.md
  review-fidelity.md
  report.md
latex/chapters/253a/chapter01.tex
latex/master.pdf
```

Large media, audio, frames, and page renders remain untracked.

## Verification and stop condition

Run `./build_and_verify.sh --draft` during composition. Attempt the strict
build after the source and review checks pass. Visually inspect every pilot
page.

The final pilot report gives exact note pages, video IDs and timestamps,
transcript minutes, unresolved ambiguities, provenance counts, mathematical
and fidelity findings, PDF page count, build results, elapsed time, and usage
shown by the interface. Leave unavailable usage fields blank. Use the pilot's
observed pages and transcript minutes to estimate the full 21-chapter run.

Treat the resulting book as an internal research edition. Before public
distribution, verify permission for substantially verbatim lecture speech,
problem sets, Xi Yin's name in the title and author field, and the intended
license.

Stop after delivering the reviewed pilot, its report, and the measured usage
estimate. Wait for approval before producing later chapters.
