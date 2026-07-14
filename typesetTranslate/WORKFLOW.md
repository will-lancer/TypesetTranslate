# typesetTranslate Workflow

## Goal

The purpose of `typesetTranslate` is to turn a scanned historical paper or book
into a modern LaTeX project that can be processed by multiple narrow agents in
parallel without those agents stepping on each other.

The workflow is built around one principle:

> agents coordinate through files and manifests, not through shared chat context.

That principle matters because transcription work is fragile. The wording,
mathematics, numbering, and note content must stay exact, while the LaTeX
implementation becomes modernized and modular. Presentation choices such as
citation markers, footnote symbols, and standard mathematical fonts may be
normalized when the project-specific notation guide explicitly requires it.

Two definitions are important throughout this document:

- **source page** means the physical PDF page, starting at `1`; it does not mean
  the printed roman or arabic page number visible in the scan
- **faithful** means that visible wording and mathematics are preserved; OCR is
  only an aid, and the rendered page image is authoritative

Modernizing LaTeX does not authorize paraphrasing, silent mathematical
correction, invented figure detail, or omission of front matter. It does allow
better environments, vector diagrams, and removal of scan-induced line-wrap
hyphenation.

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

### 0. Preflight

Do not initialize a large workspace until the input, tools, and execution
backend are understood.

Check:

1. the PDF opens, is not encrypted, and has a plausible physical page count
2. whether the source is a paper or a book
3. `pdfinfo`, `pdftoppm`, and either `latexmk` or `pdflatex` are available
4. enough disk space exists for 200-DPI PNGs and compile artifacts
5. the slug does not collide with an existing workspace or export
6. the selected runner can actually complete the work

Runner behavior matters:

- `manifest` writes contracts but does not submit jobs; external or local agents
  must write the output files, and `paperbot poll` discovers those files
- `mock` writes placeholders and is only for testing the orchestration
- `openai` requires rendered page images and `OPENAI_API_KEY`; verify credentials,
  model choice, network access, and expected image-token cost before dispatch

The `transcription_workers` and `figure_workers` settings describe the intended
worker pool; they do not themselves create local parallel workers.

### 1. Ingest

Command:

```bash
paperbot init origPapers/<file>.pdf \
  --slug <slug> \
  --workspace-root dirs \
  --document-kind <paper-or-book> \
  --runner <manifest-or-openai> \
  --title "<title>"
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

#### Page-completeness gate

Planning is not complete until all of the following numbers agree:

- the `pdfinfo` page count
- the configured `page_count`
- entries in `artifacts/page-manifest.json`
- `artifacts/pages/page-*.png` files

This is a hard gate. The renderer currently skips rendering when it finds any
existing page PNG, so an interrupted partial render can otherwise look ready.
If counts differ, treat the page set as incomplete and regenerate it before
transcription. Do not rely only on the `page_images_ready` boolean.

### 3. Chunk Planning

Chunk jobs are the core transcription unit. Page counts are a planning aid, not
the final ownership boundary: prefer a complete section, appendix, problem set,
or bibliography whenever a heading begins mid-page. Give neighboring agents a
small read-only overlap for context, but assign every source passage to exactly
one writable chunk.

Defaults:

- papers: `5` pages per chunk
- books: `3` pages per chunk

Why the defaults differ:

- papers often have more whitespace and fewer continuous paragraphs
- books are denser and accumulate uncertainty faster

These are conservative implementation defaults, not universal targets. In
practice, use `5` pages for very dense mathematics, about `8` for a typical
clean book scan, and up to `10` for sparse prose or front matter. Larger chunks
reduce boundary risk and orchestration overhead; smaller chunks reduce agent
fatigue and make uncertainty easier to isolate. Choose the size after inspecting
representative pages, then pass it explicitly with `--chunk-size`.

If the chunk size changes after planning, regenerate prompts, manifests, check
wrappers, state, and `master.tex` before any transcription starts. Do not leave
stale job files for the old ranges in place.

Outputs:

- `output/chunks/pp0001-0005.tex`
- `output/checks/check-pp0001-0005.tex`
- `jobs/prompts/pp0001-0005.txt`
- `jobs/manifests/chunk-001.json`

The chunk file itself is not written by the orchestrator. It is the output
contract for a transcription agent.

#### Project notation policy

Before dispatch, read or create the project's `NOTATION.md`. It is the binding
style layer for deliberate modernization and should settle recurring choices
before several agents encode them differently. Record at least:

- state-vector and operator conventions
- identity, number-set, group, and representation fonts
- discrete-symmetry notation
- citation-marker and bibliography style
- footnote numbering and symbols
- source-specific conventions that must remain unchanged

The source remains authoritative for content. The project notation guide is
authoritative for explicitly approved presentation changes. If a strange
formula may be a source error, preserve it and log it unless a separate errata
pass has been authorized; do not spend the finishing pass trying to prove or
silently repair it.

### 4. Transcription

Each transcription agent should have exactly one writable target:

- one chunk file in `output/chunks/`

The agent prompt requires:

- exact wording
- exact equations
- exact reference and footnote content, styled according to `NOTATION.md`
- explicit `VERIFY:` comments for uncertainty
- explicit `TODO FIGURE:` placeholders instead of guessed figures

The agent should use the source OCR layer only for speed. It must inspect the
page image for equations, accents, German letters, subscripts, superscripts,
punctuation, diagrams, and words that OCR commonly corrupts.

No transcription agent should edit:

- `master.tex`
- any figure file
- another chunk

When a runner or local agent finishes a chunk:

1. verify that the assigned output file exists and starts with the required
   page/figure/uncertainty header
2. compile its check wrapper
3. render the check PDF and inspect it for clipping, overlaps, and bad glyphs
4. fix only that chunk's syntax or record a `VERIFY:` uncertainty
5. run `paperbot poll ... --job-type transcription` to synchronize state

Do not mark a chunk complete merely because a file appeared while its writer is
still editing or validating it.

Each completion report should state the physical source-page range, semantic
start and end points, equation-number interval, table/figure/problem/reference
counts where applicable, footnote count, and compile/render status. Once a
writer declares a chunk source-reviewed and compile-clean, freeze that chunk;
the integrator owns later cross-chunk corrections.

### 5. Cross-boundary QA

Chunk compilation cannot detect dropped or duplicated prose at a chunk join.
After transcription, compare every adjacent pair against the source, especially
joins that split a sentence, proof, equation, exercise, footnote, or chapter.

The boundary pass is read-only by default. It should report:

- missing or duplicated words
- broken continuations
- a display or diagram divided incorrectly across files
- repeated scan hyphenation
- inconsistent notation introduced by different agents

Only the owner or orchestrator should apply a reported correction, and the
affected check wrapper must then be recompiled.

### 6. Figure Discovery

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

#### Unnumbered figures and diagrams

Automatic discovery currently recognizes only the numbered contract above.
Logos and unnumbered commutative diagrams will not produce jobs. Never invent a
figure number just to satisfy the parser.

For an unnumbered visual, either typeset it directly in the owning chunk or use
an explicit figure-only assignment:

1. the figure agent writes exactly one file in `output/figures/`
2. it compiles and visually checks that fragment against the source page
3. the orchestrator replaces the placeholder with an `\input{}` at the original
   position
4. the owning chunk check is compiled again

Before moving on, search all chunks for both `TODO FIGURE` and more general
`TODO` comments. Structural verification only counts placeholders matching the
numbered parser contract.

### 7. Master Assembly

The master document is assembled by `\input{}` lines rather than by copying all
chunk text into one file.

That is important because:

- it removes merge conflicts
- it makes chunk outputs auditable
- it lets the orchestrator rebuild the master deterministically

Current location:

- `output/master.tex`

The generated master is a starting point, not proof of a polished title page.
Inspect it for generic `TODO` metadata, an inappropriate document style, and a
generated `\maketitle` that duplicates transcribed historical front matter.
Use the source's real title and authors, and avoid showing the same title page
twice. Re-run planning only before these deliberate master edits, because
planning deterministically regenerates `master.tex`.

### 8. Definition Of Done And The 98% Stop Rule

“98% good” is a stopping policy, not a claim that fidelity can be measured to
two decimal places. The work is done when all material acceptance gates pass:

1. every assigned source passage is present exactly once
2. equations, tables, figures, problems, references, and note content are
   complete and correctly numbered
3. project notation rules have been applied consistently
4. chunk checks and the assembled master compile with no missing inputs or
   LaTeX errors
5. an all-page visual coverage pass finds no clipping, overlap, broken table,
   unreadable glyph, or visible placeholder
6. no unresolved fidelity uncertainty can change wording, mathematics, or
   meaning

After the first successful full compile and all-page coverage pass, allow at
most **two bounded correction cycles**. Every cycle must begin with a concrete
defect tied to a failed gate or source page. Re-render only affected pages and
joins unless pagination changed. Do not start another search, rebuild, or
full-document inspection merely to look for something else to polish.

Material blockers include omitted or duplicated source, wrong mathematics,
wrong numbering, missing back matter, semantic uncertainty, clipping,
illegibility, and visible placeholders. Deferable polish includes microscopic
spacing differences, harmless line or page-break changes, benign package or
PDF-anchor warnings with no visible effect, and speculative corrections to the
source. Record deferable items briefly for a later pass and stop. If the same
non-material warning survives two attempts, stop trying to eliminate it.

This rule applies especially to autonomous agents: once the acceptance gates
pass, they must hand off the result instead of consuming more time on
open-ended micro-polish.

### 9. Verification

The verification stage has three layers:

- structural verification
- compile verification
- full-document visual verification

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

Structural verification does not compare the transcription with the scan. It
also scans the text `VERIFY:` case-insensitively anywhere in a file, so ordinary
source prose such as "easy to verify:" can be a false positive. Inspect every
match; preserve the visible source wording while distinguishing it from an
actual uncertainty marker.

Compile verification command:

```bash
paperbot verify-compile dirs/<slug>
```

Outputs:

- `reports/compile.json`
- `reports/compile.md`

This stage compiles:

1. `output/master.tex`
2. chunk check wrappers in `output/checks/`

The compile report records missing files, extracted LaTeX errors, warnings, and
which chunk check wrapper failed.

A compile pass is complete when the master and every planned chunk check report
success, with no missing inputs. Classify warnings by visible or semantic
impact instead of requiring a warning-free log. Duplicate PDF anchors can
result from faithfully preserved source numbering; an overfull box is a blocker
only when it clips, collides, or makes the page unreadable.

#### Visual verification

After the final meaningful edit:

1. render the latest `output/master.pdf` to PNGs
2. inspect every page, using contact sheets for coverage and full-resolution
   pages for suspected defects
3. check the title/front matter, section transitions, diagrams, dense equations,
   page numbers, final index, and first/last pages
4. reject clipped text, overlaps, broken tables, black replacement glyphs,
   malformed diagrams, visible `TODO` text, and unreadable type

Use one all-page contact-sheet pass for coverage and full resolution for
suspected defects. After a localized correction, inspect the affected pages and
their joins; repeat the complete visual pass only if pagination changed. Do not
treat successful LaTeX compilation as visual approval, and do not turn visual
approval into an unlimited typography-polish loop.

### 10. Export And Portability Check

Command:

```bash
paperbot export dirs/<slug> --dest-root newPapers --include-pdf
```

Export replaces `newPapers/<slug>` if it already exists. Confirm that this is
intended before running it.

The export is not finished until the exported copy is self-contained:

1. inspect `export-manifest.json` for warnings
2. confirm `latex/master.tex` uses exported `chunks/` and `figures/` paths
3. compile `newPapers/<slug>/latex/master.tex` from the exported `latex/`
   directory, preferably writing test artifacts to a temporary directory
4. compare the exported PDF with the verified workspace PDF when both are
   expected to be identical

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
- explicit dispatch and poll commands
- manifest, mock, and OpenAI runner backends
- master generation by `\input{}`
- structural verification reports
- compile verification reports
- export into `newPapers/`

What still needs to be built:

- bibliography and table-specialized agents
- richer book-specific heuristics for adaptive chunking
- automated repair passes from compile findings
- automatic recovery from partial page rendering
- first-class jobs for unnumbered figures and chapter-local figure numbering
- automated scan-to-transcription and cross-boundary fidelity checks
- document-kind-aware master templates and title-page handling

## Recommended operating procedure

For a new project:

1. put the source PDF in `origPapers/` and run the preflight checks
2. initialize with explicit document kind, runner, slug, and title
3. plan with an inspected, explicit chunk size
4. confirm page-count and rendered-image completeness
5. dispatch jobs, or assign manifest jobs to isolated local agents
6. poll until every transcription job has finished its check/render pass
7. perform read-only QA across every chunk boundary
8. refresh numbered figure jobs and explicitly handle unnumbered visuals
9. inspect and finalize `master.tex`
10. resolve every material uncertainty and placeholder; record genuinely
    undecidable, non-material items in a concise deferred-issues report
11. compile the master and every chunk check successfully
12. render and visually inspect the complete final PDF
13. export with the PDF into `newPapers/`
14. compile the exported copy from its destination
15. remove temporary render and compile artifacts
16. stop when the Definition of Done passes; schedule optional micro-polish as
    a separate later task

For best results:

- keep chunk agents narrow
- keep figure agents separate
- never allow multiple agents to edit the same file
- use `VERIFY:` comments instead of guessing
- compile early and often
- treat page images, not OCR, as the source of truth
- verify boundaries and exported portability explicitly
- require a concrete failed gate before any late-stage correction cycle
- stop after two bounded finishing cycles

That is the workflow the current codebase is trying to formalize.
