# Yin QFT 253abc textbook

This is a small handoff package for another agent or agent swarm. Its job is to
turn Xi Yin's handwritten Physics 253abc notes and recorded lectures into a
source-faithful JHEP-format textbook.

Start here:

```text
MASTER_PROMPT.md
```

The first run covers only "Basic Generalities of Quantum Field Theory."
Production agents determine the corresponding video IDs and timestamps, draft
the chapter, review it, build the PDF, record usage, and stop for approval.

## Files

- `MASTER_PROMPT.md`: complete task prompt, source rules, and swarm roles.
- `WORKFLOW.md`: wave order, writable paths, outputs, and acceptance checks.
- `CHAPTER_PLAN.md`: the three-part book map.
- `SOURCE_MANIFEST.yaml`: verified source locations and pilot page range.
- `latex/`: minimal JHEP scaffold.
- `build_and_verify.sh`: draft and strict checks.

## Build

```sh
./build_and_verify.sh --draft
./build_and_verify.sh
```

Draft mode permits declared unfinished markers. Strict mode exports a stable
PDF only after those markers have been resolved.
