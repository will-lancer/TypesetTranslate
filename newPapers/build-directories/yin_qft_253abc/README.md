# Yin QFT 253abc textbook

This project turns Xi Yin's handwritten Physics 253abc notes and recorded
lectures into a source-faithful textbook written in Yin's prose style.

Start in this order:

```text
SOURCE_MANIFEST.yaml
AGENT_POLICY.md
WRITING_STYLE.md
MASTER_PROMPT.md
WORKFLOW.md
CHAPTER_PLAN.md
```

The cleaned transcript preserves evidence. The argument map organizes that
evidence into conceptual units. The chapter editor writes continuous textbook
prose from the map, exact notes, targeted lecture spans, and video frames.
The voice-restoration ledger then checks every approved voice cue against the
frozen transcript and the current chapter.

The first complete draft must pass the written-prose audit:

```sh
python3 scripts/render_written_provenance.py --write
python3 scripts/render_written_dispositions.py --write
python3 scripts/audit_written_prose.py
```

Project builds run the same audit automatically:

```sh
./build_and_verify.sh --draft
./build_and_verify.sh
```

Draft mode reports incomplete ledgers and reviews. Strict mode exports a stable
PDF only after the source, prose, mathematics, provenance, and render checks
pass.

## Active files

- `MASTER_PROMPT.md`: source hierarchy and drafting contract.
- `AGENT_POLICY.md`: binding five-pass model, scope, and ownership policy.
- `WRITING_STYLE.md`: binding prose ledger and examples.
- `WORKFLOW.md`: source, argument-map, writing, review, and release sequence.
- `templates/WRITING_PASS_LEDGER.md`: required five-pass record for each chapter.
- `work/pilot/voice-restoration.jsonl`: positive, hash-pinned voice cues.
- `scripts/audit_written_prose.py`: mechanical written-prose gate.
- `scripts/render_written_provenance.py`: deterministic provenance renderer and
  stale-ledger check.
- `scripts/render_written_dispositions.py`: deterministic current-chapter links
  for every frozen transcript disposition.
- `scripts/render_render_manifest.py`: PDF and rendered-page identity manifest.
- `scripts/audit_project.py`: source, provenance, disposition, and review gate.
- `build_and_verify.sh`: integrated build and PDF verification.

Files named `verbatim-*`, the `verbatim-sections/` directory, and
`scripts/audit_verbatim.py` preserve the abandoned near-verbatim experiment.
They are outside the active writing and release pipeline.
