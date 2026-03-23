# typesetTranslate

`typesetTranslate` is the local orchestration layer for converting historical
papers and books into modern LaTeX with many narrow coding-agent jobs.

The core design is file-oriented:

- transcription agents write chunk files only
- figure agents write figure files only
- the master document assembles chunks via `\input{}`
- project state lives on disk

## Repository shape

From the repository root:

```text
origPapers/        source PDFs
dirs/              active paper or book workspaces
newPapers/         final polished outputs
typesetTranslate/  orchestration package
```

## Workspace shape

Each generated workspace now follows a stage-oriented layout:

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

This split matters because books and papers produce different kinds of files:
raw source files, rendered page images, agent job contracts, generated LaTeX,
and workflow state should not be mixed together in one flat directory.

## Installation

From this directory:

```bash
python3 -m pip install -e .
```

## Main commands

### `paperbot init`

Create the workspace and write project metadata.

```bash
paperbot init origPapers/wittenSUSYintroOrig.pdf \
  --slug witten-susy-intro \
  --workspace-root dirs \
  --document-kind paper
```

### `paperbot plan`

Plan chunk jobs for an existing workspace, render page images when possible,
write prompts/manifests, and build `output/master.tex`.

```bash
paperbot plan dirs/witten-susy-intro
```

### `paperbot run`

Convenience command for `init` followed by `plan`.

For a paper:

```bash
paperbot run origPapers/wittenSUSYintroOrig.pdf \
  --slug witten-susy-intro \
  --workspace-root dirs \
  --document-kind paper \
  --runner manifest
```

For a book:

```bash
paperbot run origPapers/milnorTopFromDiffView.pdf \
  --slug milnor-topology \
  --workspace-root dirs \
  --document-kind book \
  --runner manifest
```

Chunk sizes default to:

- `5` pages for papers
- `3` pages for books

Use `--chunk-size` to override.

### `paperbot refresh-figures`

Scan existing chunk files for `% TODO FIGURE:` placeholders and generate figure
job manifests and prompts.

```bash
paperbot refresh-figures dirs/witten-susy-intro
```

### `paperbot verify`

Run structural verification and write:

- `reports/verification.json`
- `reports/verification.md`

```bash
paperbot verify dirs/witten-susy-intro
```

### `paperbot inspect`

Print the current serialized workspace state.

```bash
paperbot inspect dirs/witten-susy-intro
```

## PDF tooling

The package uses these external tools when present:

- `pdfinfo` for page counting
- `pdftoppm` for page image rendering

If they are missing, the workspace still initializes correctly. In that case,
pass `--page-count` manually and add page rendering later on a machine with
Poppler installed.

## Detailed workflow

See [`WORKFLOW.md`](/Users/wlancer/Coding_Projects/TypesetTranslate/typesetTranslate/WORKFLOW.md) for the full process and rationale.

## Current boundaries

The current package is good at:

- setting up a clean workspace
- planning chunk jobs
- generating prompts and manifests
- keeping transcription and figure work separated

The next useful steps are:

- a real Codex/API runner
- chunk verification and compile repair passes
- bibliography/reference normalization
- automatic final export into `newPapers/`
