from __future__ import annotations

import re
from pathlib import Path

from .models import ChunkJob, FigureJob, PaperConfig, WorkspacePaths

FIGURE_PLACEHOLDER_PATTERN = re.compile(
    r"%\s*TODO FIGURE:\s*Original Fig\.?\s*(\d+)\s*appears here(?: on p\.?\s*([0-9A-Za-z-]+))?",
    re.IGNORECASE,
)


def build_chunk_jobs(config: PaperConfig, paths: WorkspacePaths) -> list[ChunkJob]:
    if not config.page_count:
        return []

    chunk_size = config.effective_chunk_size()
    jobs: list[ChunkJob] = []
    start = 1
    chunk_index = 1
    while start <= config.page_count:
        end = min(start + chunk_size - 1, config.page_count)
        stem = f"pp{start:04d}-{end:04d}"
        jobs.append(
            ChunkJob(
                job_id=f"chunk-{chunk_index:03d}",
                start_page=start,
                end_page=end,
                output_file=str(paths.chunks_dir / f"{stem}.tex"),
                prompt_file=str(paths.prompts_dir / f"{stem}.txt"),
                check_file=str(paths.checks_dir / f"check-{stem}.tex"),
            )
        )
        start = end + 1
        chunk_index += 1

    return jobs


def build_figure_jobs(paths: WorkspacePaths) -> list[FigureJob]:
    jobs: list[FigureJob] = []
    seen_numbers: set[int] = set()

    for chunk_file in sorted(paths.chunks_dir.glob("pp*.tex")):
        text = chunk_file.read_text()
        for match in FIGURE_PLACEHOLDER_PATTERN.finditer(text):
            figure_number = int(match.group(1))
            if figure_number in seen_numbers:
                continue
            seen_numbers.add(figure_number)

            figure_stem = f"fig{figure_number:02d}"
            source_page_hint = match.group(2)
            jobs.append(
                FigureJob(
                    job_id=f"figure-{figure_number:03d}",
                    figure_label=f"Figure {figure_number}",
                    output_file=str(paths.figures_dir / f"{figure_stem}.tex"),
                    prompt_file=str(paths.prompts_dir / f"{figure_stem}.txt"),
                    source_chunk_file=str(chunk_file),
                    source_page_hint=source_page_hint,
                    placeholder_text=match.group(0),
                )
            )

    return jobs


def build_master_inputs(chunk_jobs: list[ChunkJob], workspace_root: Path) -> list[str]:
    lines: list[str] = []
    for job in chunk_jobs:
        chunk_path = Path(job.output_file)
        rel = chunk_path.relative_to(workspace_root)
        lines.append(f"\\input{{{rel.as_posix()}}}")
    return lines
