# typesetTranslate Workflow

## Goal

The purpose of `typesetTranslate` is to turn a scanned historical paper or book
into a modern LaTeX project that can be processed by multiple narrow agents in
parallel without those agents stepping on each other.

The workflow is built around one principle:

> agents coordinate through files and manifests, not through shared chat context.

That principle matters because transcription work is fragile. The wording,
equations, figure numbering, and footnotes must stay exact, while the LaTeX
implementation becomes modernized and modular.

## Repository-level layout

At the repository root:

```text
origPapers/        immutable source PDFs
dirs/              active workspaces under transcription
newPapers/         polished or exported final PDFs
typesetTranslate/  the orchestration package
```

This split lets you keep source input, active work, and final outputs separate.
That becomes especially important for books, where rendered page images and
intermediate chunks can become very large.

## Workspace-level layout

Each workspace is created under `dirs/<slug>/` and now uses a staged layout:

```text
dirs/<slug>/
  source/
    original.pdf
  artifacts/
    page-manifest.json
    pages/
  output/
    master.tex
    chunks/
    figures/
    checks/
  jobs/
    manifests/
    prompts/
    logs/
  reports/
  state/
    project.json
    state.json
```

### Why this is better than a flat layout

- `source/` is immutable input.
- `artifacts/` holds derived machine-readable material such as page images.
- `output/` contains actual LaTeX deliverables.
- `jobs/` holds what agents consume: prompts, manifests, and later logs.
- `state/` holds the orchestrator's current understanding of the workspace.
- `reports/` is reserved for verification summaries and merge notes.

This structure scales much better from short papers to full books because the
number of temporary files grows quickly once you have hundreds of pages.

## Stages

The workflow is intentionally split into stages.

### 1. Ingest

Command:

```bash
paperbot init origPapers/<file>.pdf --slug <slug> --workspace-root dirs
```

What happens:

1. The workspace is created.
2. The source PDF is copied into `source/original.pdf`.
3. The project config is written to `state/project.json`.

### 2. Planning And Page Discovery

The orchestrator tries to:

- count pages with `pdfinfo`
- render PNG page images with `pdftoppm`

Outputs:

- `artifacts/pages/page-0001.png`, `page-0002.png`, ...
- `artifacts/page-manifest.json`

If these tools are unavailable, the workspace is still usable. In that case the
operator should provide `--page-count` and later run the workflow on a machine
with Poppler installed.

Command:

```bash
paperbot plan dirs/<slug>
```

### 3. Chunk Planning

Chunk jobs are the core transcription unit.

Defaults:

- papers: `5` pages per chunk
- books: `3` pages per chunk

Why the defaults differ:

- papers often have more whitespace and fewer continuous paragraphs
- books are denser and accumulate uncertainty faster

Outputs:

- `output/chunks/pp0001-0005.tex`
- `output/checks/check-pp0001-0005.tex`
- `jobs/prompts/pp0001-0005.txt`
- `jobs/manifests/chunk-001.json`

The chunk file itself is not written by the orchestrator. It is the output
contract for a transcription agent.

### 4. Transcription

Each transcription agent should have exactly one writable target:

- one chunk file in `output/chunks/`

The agent prompt requires:

- exact wording
- exact equations
- exact references and footnotes
- explicit `VERIFY:` comments for uncertainty
- explicit `TODO FIGURE:` placeholders instead of guessed figures

No transcription agent should edit:

- `master.tex`
- any figure file
- another chunk

### 5. Figure Discovery

Once chunk files exist, the orchestrator can scan them for figure placeholders.

Current contract:

```text
% TODO FIGURE: Original Fig. 15 appears here on p. 343.
```

The command:

```bash
paperbot refresh-figures dirs/<slug>
```

parses chunk files and emits figure jobs:

- `output/figures/fig15.tex`
- `jobs/prompts/fig15.txt`
- `jobs/manifests/figure-015.json`

This keeps figure work downstream from transcription, which is safer than
trying to do prose, equations, and figures in one pass across the whole work.

### 6. Master Assembly

The master document is assembled by `\input{}` lines rather than by copying all
chunk text into one file.

That is important because:

- it removes merge conflicts
- it makes chunk outputs auditable
- it lets the orchestrator rebuild the master deterministically

Current location:

- `output/master.tex`

### 7. Verification

The verification stage is now implemented as a structural audit.

Command:

```bash
paperbot verify dirs/<slug>
```

Outputs:

- `reports/verification.json`
- `reports/verification.md`

The report currently checks:

1. whether planned chunk outputs exist
2. whether planned figure outputs exist
3. whether chunk check wrappers exist
4. how many `VERIFY:` notes remain
5. how many `% TODO FIGURE:` placeholders remain
6. whether `master.tex` exists
7. whether page-manifest entries match the configured page count

For historical documents, this narrow verification model is much safer than
telling one large agent to "fix the project."

## State files

### `state/project.json`

This records the workspace configuration:

- slug
- source PDF
- document kind
- chunk-size policy
- runner choice
- title override

### `state/state.json`

This records the current derived state:

- whether page images are ready
- whether page count was detected
- chunk jobs
- figure jobs
- warnings

The point of `state.json` is not to be perfect forever. It is there so the
orchestrator and human operator can quickly see what exists and what remains.

## Prompts and manifests

Prompts and manifests are separate on purpose.

### Prompts

Prompt files in `jobs/prompts/` are human-readable instructions for an agent.

### Manifests

Manifest files in `jobs/manifests/` are machine-readable job contracts.

That separation is useful because:

- prompts change often
- manifests are consumed by tooling
- you may want several runners to use the same manifest format

## Why this workflow is good for books as well as papers

Books differ from papers mainly in scale, not in correctness constraints.

What changes at book scale:

- more pages
- more front matter
- more figures and tables
- more need for resumability
- more need to keep intermediate artifacts organized

The staged workspace layout and chunk-based job model are what make the same
system usable for both.

## Current limitations

What is implemented now:

- workspace creation
- page counting and rendering when system tools are installed
- chunk planning
- figure discovery from chunk placeholders
- prompt and manifest generation
- master generation by `\input{}`
- structural verification reports

What still needs to be built:

- real Codex/API dispatch
- compile-aware verification and repair passes
- merge/export into `newPapers/`
- bibliography and table-specialized agents
- richer book-specific heuristics for adaptive chunking

## Recommended operating procedure

For a new project:

1. put the source PDF in `origPapers/`
2. run `paperbot init ...`
3. run `paperbot plan dirs/<slug>`
4. dispatch transcription jobs from `jobs/manifests/`
5. refresh figure jobs after chunk files start appearing
6. run `paperbot verify dirs/<slug>`
7. export the cleaned result into `newPapers/`

For best results:

- keep chunk agents narrow
- keep figure agents separate
- never allow multiple agents to edit the same file
- use `VERIFY:` comments instead of guessing
- compile early and often

That is the workflow the current codebase is trying to formalize.
