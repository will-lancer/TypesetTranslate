# Agent execution policy

The project uses five passes. Checks performed inside a pass do not become
additional passes.

| Pass | Work | Required subagent model | Scope |
|---|---|---|---|
| 1 | Full source capture | Luna Max Fast | Parallel lecture and note lanes |
| 2 | Literal transcript cleanup | Luna Max Fast | Parallel lecture lanes |
| 3 | Chapter drafting | `gpt-5.6-sol` at `xhigh` | Whole chapter |
| 4 | Editorial balance | `gpt-5.6-sol` at `xhigh` | Whole chapter |
| 5 | Fidelity and release | `gpt-5.6-sol` at `xhigh`, lead editor, and scripts | Whole chapter and rendered PDF |

Luna Max Fast is the default subagent for passes 1 and 2. Omit a model
override when spawning those lanes.

Luna Max Fast work may use up to 50 simultaneous subagents. Use however many
independent source and audit lanes are useful. Do not impose an arbitrary lower
cap. Fifty is a ceiling rather than a quota, so do not create artificial lanes
merely to occupy every slot.

Every subagent that organizes arguments, writes or edits chapter prose,
restores Yin's voice, or judges mathematical and source fidelity must use
`gpt-5.6-sol` at `xhigh`. Leave the work pending if that model is unavailable.

At most eight agents running `gpt-5.6-sol` at `xhigh` may be active at once
across the complete task tree. Count the lead when it uses that configuration,
direct subagents, and nested subagents toward the same limit.

Passes 1 and 2 may divide videos, note pages, boundary checks, caption audits,
and reconciliation checks among agents with nonoverlapping writable outputs
and short source-boundary overlaps. Passes 3 through 5 are chapter-scale work.
Their agents read the complete chapter and the relevant source packet.

One editor owns the canonical chapter at a time. Parallel editorial agents
write findings or proposed patches in separate files. The lead editor applies
accepted changes.

## Pass 1: full source capture

Capture every recoverable spoken word, question, joke, example,
qualification, equation, diagram, and note mark. Preserve raw source identity,
timestamps, pages, and frames. Do not polish the language.

## Pass 2: literal transcript cleanup

Remove caption duplication, clipped seams, ellipsis artifacts, broken
restarts, and source-resolvable recognition errors. Preserve meaningful
repetition and characteristic wording. Record repairs and freeze the minimally
cleaned transcript.

## Pass 3: chapter drafting

Build a compact argument map, interleave equations, and write the complete
chapter. Merge transcript fragments into coherent paragraphs. Remove classroom
mechanics and place large mathematics in displays. Begin from Yin's vocabulary
and make the smallest useful edit.

## Pass 4: editorial balance

A fresh whole-chapter reader removes remaining spoken debris and restores voice
lost during drafting. Check filler, cadence, qualifications, reader address,
questions, jokes, repetition, paragraph flow, connectives, and referents.
Record the positive voice cues that must survive.

## Pass 5: fidelity and release

Check source coverage, mathematics, notation, provenance, and the rendered PDF
inside one final pass. Read every affected page. Run deterministic audits and
verify the exported PDF against the build. A content change invalidates the
affected checks and requires them to be rerun before release.
