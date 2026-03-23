from __future__ import annotations

from pathlib import Path

from .models import ChunkJob, FigureJob, PaperConfig, WorkspacePaths


TRANSCRIBE_TEMPLATE = """You are helping faithfully re-typeset a historical {document_kind} in modern LaTeX.

Project root:
`{workspace_root}`

Source scan:
`{source_pdf}`

Paper workspace:
`{paper_root}`

Master file:
`{master_tex}`

Page image directory:
`{pages_dir}`

Chunk directory:
`{chunks_dir}`

Figure directory:
`{figures_dir}`

Assigned original pages:
`{start_page}-{end_page}`

Output file:
`{output_file}`

Hard constraints:
- Preserve the wording exactly.
- Preserve equations exactly.
- Preserve figure numbering, captions, footnotes, and references exactly.
- Do not paraphrase, summarize, modernize wording, or silently correct the source.
- Modernize only the LaTeX implementation and figure drawing.
- Do not preserve original page breaks or original page numbering.
- Remove line-wrap hyphenation introduced by the scan.
- Keep true compound hyphens.
- If any character, symbol, or word is uncertain, mark it explicitly with a clear `VERIFY:` comment rather than guessing.
- Keep figure placeholders as explicit `TODO` blocks rather than guessing figure content.
- Work only on the assigned original pages.
- Do not edit the master file.

Workflow constraints:
- Write only the body-content chunk for the assigned pages.
- Start the chunk with:
  `% Original pages: ...`
  `% Figures: ...`
  `% Uncertainty log: ...`
- Preserve original equation numbers via `\\tag{{...}}`.
- Preserve footnotes exactly.
- If a figure appears, insert a clear placeholder comment at the correct location.

Task:
1. Read only the assigned original pages from the source PDF or page images.
2. Transcribe them exactly into the assigned chunk file.
3. Do not modify unrelated files.
"""


FIGURE_TEMPLATE = """You are helping render figures for a historical {document_kind} being re-typeset in modern LaTeX.

Project root:
`{workspace_root}`

Paper workspace:
`{paper_root}`

Master file:
`{master_tex}`

Page image directory:
`{pages_dir}`

Figure directory:
`{figures_dir}`

Target figure job:
`{figure_label}`

Source chunk:
`{source_chunk_file}`

Source page hint:
`{source_page_hint}`

Placeholder text:
`{placeholder_text}`

Output file:
`{output_file}`

Hard constraints:
- Work only on figures.
- Do not alter wording, equations, captions, numbering, references, or footnotes.
- Prefer TikZ/PGF when feasible.
- Preserve figure numbering and caption text exactly.
- If any figure detail is uncertain, mark it with a `VERIFY:` comment rather than guessing.
- Keep outputs standalone and auditable.
- Do not edit the master file.

Task:
1. Read the relevant source page image(s) and chunk placeholders.
2. Create a standalone LaTeX figure file.
3. Preserve the figure number and associated caption contract.
"""


def render_transcription_prompt(
    config: PaperConfig,
    paths: WorkspacePaths,
    job: ChunkJob,
) -> str:
    return TRANSCRIBE_TEMPLATE.format(
        document_kind=config.document_kind,
        workspace_root=Path(config.workspace_root).resolve(),
        source_pdf=Path(config.source_pdf).resolve(),
        paper_root=paths.root.resolve(),
        master_tex=paths.master_tex.resolve(),
        pages_dir=paths.pages_dir.resolve(),
        chunks_dir=paths.chunks_dir.resolve(),
        figures_dir=paths.figures_dir.resolve(),
        start_page=job.start_page,
        end_page=job.end_page,
        output_file=Path(job.output_file).resolve(),
    )


def render_figure_prompt(
    config: PaperConfig,
    paths: WorkspacePaths,
    job: FigureJob,
) -> str:
    return FIGURE_TEMPLATE.format(
        document_kind=config.document_kind,
        workspace_root=Path(config.workspace_root).resolve(),
        paper_root=paths.root.resolve(),
        master_tex=paths.master_tex.resolve(),
        pages_dir=paths.pages_dir.resolve(),
        figures_dir=paths.figures_dir.resolve(),
        figure_label=job.figure_label,
        source_chunk_file=job.source_chunk_file or "unknown",
        source_page_hint=job.source_page_hint or "unknown",
        placeholder_text=job.placeholder_text or "unknown",
        output_file=Path(job.output_file).resolve(),
    )
