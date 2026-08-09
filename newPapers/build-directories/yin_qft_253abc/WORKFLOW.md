# Pilot workflow

## Wave 1: map and transcribe

Run these workers concurrently:

| Worker | Writable outputs |
|---|---|
| Source mapper | `work/pilot/playlist.jsonl`, `work/pilot/source-map.md` |
| Note transcriber | `work/pilot/notes-exact.tex`, `work/pilot/note-pages/`, `work/pilot/ambiguities.md` |
| Transcript worker | `work/pilot/transcript.raw.vtt`, `work/pilot/transcript.cleaned.jsonl`, `work/pilot/alignment.jsonl`, `work/pilot/keyframes/` |

The source mapper inventories every observed playlist item and nominates
opening lectures. The transcript worker may start from those candidates and
must record every video examined. The note transcriber covers combined PDF
pages 6--14 line by line, including equations, arrows, diagrams, marginalia,
and meaningful color.

The lead checks the three outputs together. It resolves the exact lecture
boundaries through topics, visible equations, page images, and the transition
to Lagrangian quantum mechanics. It then freezes the source packet.

## Wave 2: write

One chapter editor owns:

```text
latex/chapters/253a/chapter01.tex
work/pilot/provenance.jsonl
work/pilot/page-dispositions.jsonl
work/pilot/transcript-dispositions.jsonl
```

The editor uses only the frozen packet. It follows the handwritten order,
selects minimally cleaned lecture explanations, and adds provenance while
writing. Source conflicts remain marked.

## Wave 3: review

Run these reviewers concurrently after the draft compiles:

| Reviewer | Writable output |
|---|---|
| Mathematical reviewer | `work/pilot/review-math.md` |
| Fidelity reviewer | `work/pilot/review-fidelity.md` |
| Render reviewer | `work/pilot/review-render.md` |

The mathematical reviewer checks signs, measures, state normalization,
commutators, Poincare transformations, the scalar-field expansion, and the
causality argument. Every proposed correction cites a note page or video
interval.

The fidelity reviewer traces every substantive unit to its source record and
flags changed terminology, missing qualifications, unsupported bridges,
reordering, or omitted material.

The render reviewer inspects every PDF page for JHEP formatting, page breaks,
equation layout, diagrams, links, clipping, and readable typography.

Reviewers propose changes in their reports. The lead applies accepted changes.

## Acceptance checks

The pilot is ready for strict verification when:

- note pages 1--9 have complete transcription and dispositions;
- matched lectures have exact video IDs and start/end timestamps;
- raw captions remain preserved;
- transcript repairs have recorded reasons;
- every printed paragraph, equation, and figure has provenance;
- mathematical and fidelity reviews have no unresolved blockers;
- all `TODO`, `VERIFY`, `SOURCE_CONFLICT`, and unfinished-status markers are
  resolved;
- the JHEP PDF compiles, parses, embeds its fonts, and passes visual review.

Run:

```sh
./build_and_verify.sh --draft
./build_and_verify.sh
```

The lead writes `work/pilot/report.md` and stops for approval.
