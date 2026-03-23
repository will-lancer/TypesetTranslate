from __future__ import annotations

import json
from pathlib import Path

from .models import FigureJob, PaperConfig, WorkspacePaths, WorkspaceStatus
from .paths import build_workspace_paths, resolve_workspace_paths
from .pdf_tools import build_page_manifest, collect_page_images, detect_page_count, render_pages
from .planner import build_chunk_jobs, build_figure_jobs, build_master_inputs
from .prompts import render_figure_prompt, render_transcription_prompt
from .runners import ManifestRunner, MockRunner, Runner
from .workspace import (
    copy_source_pdf,
    initialize_workspace,
    write_check_wrapper,
    write_chunk_prompt,
    write_figure_prompt,
    write_job_manifest,
    write_master_tex,
    write_page_manifest,
    write_project_config,
    write_state,
)


def _select_runner(name: str) -> Runner:
    if name == "manifest":
        return ManifestRunner()
    if name == "mock":
        return MockRunner()
    raise ValueError(f"Unknown runner: {name}")


def _status_for(
    config: PaperConfig,
    paths: WorkspacePaths,
    chunk_jobs,
    figure_jobs,
    warnings: list[str],
    page_images_ready: bool,
) -> WorkspaceStatus:
    return WorkspaceStatus(
        workspace=str(paths.root),
        document_kind=config.document_kind,
        page_images_ready=page_images_ready,
        page_count_detected=config.page_count is not None,
        runner=config.runner,
        chunk_size=config.effective_chunk_size(),
        chunk_jobs=chunk_jobs,
        figure_jobs=figure_jobs,
        warnings=warnings,
    )


def _write_chunk_manifests(paths: WorkspacePaths, chunk_jobs) -> None:
    for job in chunk_jobs:
        manifest_path = paths.manifests_dir / f"{job.job_id}.json"
        write_job_manifest(
            manifest_path,
            {
                "job_type": "transcription",
                "job_id": job.job_id,
                "start_page": job.start_page,
                "end_page": job.end_page,
                "output_file": job.output_file,
                "prompt_file": job.prompt_file,
                "check_file": job.check_file,
                "status": job.status,
                "notes": job.notes,
            },
        )


def _write_figure_manifests(paths: WorkspacePaths, figure_jobs: list[FigureJob]) -> None:
    for job in figure_jobs:
        manifest_path = paths.manifests_dir / f"{job.job_id}.json"
        write_job_manifest(
            manifest_path,
            {
                "job_type": "figure",
                "job_id": job.job_id,
                "figure_label": job.figure_label,
                "output_file": job.output_file,
                "prompt_file": job.prompt_file,
                "source_chunk_file": job.source_chunk_file,
                "source_page_hint": job.source_page_hint,
                "placeholder_text": job.placeholder_text,
                "status": job.status,
                "notes": job.notes,
            },
        )


def load_project_config(paths: WorkspacePaths) -> PaperConfig:
    payload = json.loads(paths.project_json.read_text())
    payload.pop("effective_chunk_size", None)
    payload.pop("resolved_title", None)
    return PaperConfig(**payload)


def load_existing_state(paths: WorkspacePaths) -> WorkspaceStatus | None:
    if not paths.state_json.exists():
        return None
    payload = json.loads(paths.state_json.read_text())
    return WorkspaceStatus(
        workspace=payload["workspace"],
        document_kind=payload["document_kind"],
        page_images_ready=payload["page_images_ready"],
        page_count_detected=payload["page_count_detected"],
        runner=payload["runner"],
        chunk_size=payload["chunk_size"],
        chunk_jobs=[],
        figure_jobs=[],
        warnings=payload.get("warnings", []),
    )


def initialize_project(config: PaperConfig) -> WorkspaceStatus:
    workspace_root = Path(config.workspace_root).resolve()
    source_pdf = Path(config.source_pdf).resolve()
    paths = build_workspace_paths(workspace_root, config.slug)
    initialize_workspace(paths)
    copy_source_pdf(source_pdf, paths.original_pdf)
    write_project_config(paths, config)

    status = _status_for(
        config=config,
        paths=paths,
        chunk_jobs=[],
        figure_jobs=[],
        warnings=[],
        page_images_ready=bool(collect_page_images(paths.pages_dir)),
    )
    write_state(paths, status)
    return status


def plan_project(
    workspace: str | Path,
    *,
    page_count_override: int | None = None,
    runner_override: str | None = None,
) -> WorkspaceStatus:
    workspace_root = Path(workspace).resolve()
    paths = resolve_workspace_paths(workspace_root)
    config = load_project_config(paths)
    if page_count_override is not None:
        config.page_count = page_count_override
    if runner_override is not None:
        config.runner = runner_override

    warnings: list[str] = []
    if config.page_count is None:
        detected_page_count, page_count_warning = detect_page_count(paths.original_pdf)
        config.page_count = detected_page_count
        if page_count_warning:
            warnings.append(page_count_warning)

    page_images_created, render_warning = render_pages(paths.original_pdf, paths.pages_dir)
    if render_warning:
        warnings.append(render_warning)

    page_manifest = build_page_manifest(config.page_count, paths.pages_dir)
    write_page_manifest(paths, page_manifest)

    chunk_jobs = build_chunk_jobs(config, paths)
    for job in chunk_jobs:
        prompt_text = render_transcription_prompt(config, paths, job)
        write_chunk_prompt(job, prompt_text)
        write_check_wrapper(paths, job, config.resolved_title())

    figure_jobs = build_figure_jobs(paths)
    for job in figure_jobs:
        prompt_text = render_figure_prompt(config, paths, job)
        write_figure_prompt(job, prompt_text)

    write_project_config(paths, config)

    status = _status_for(
        config=config,
        paths=paths,
        chunk_jobs=chunk_jobs,
        figure_jobs=figure_jobs,
        warnings=warnings,
        page_images_ready=page_images_created and bool(page_manifest),
    )

    runner = _select_runner(config.runner)
    status = runner.run(status)

    _write_chunk_manifests(paths, status.chunk_jobs)
    _write_figure_manifests(paths, status.figure_jobs)

    master_inputs = build_master_inputs(status.chunk_jobs, paths.root)
    write_master_tex(paths, config.resolved_title(), master_inputs)
    write_state(paths, status)
    return status


def run_pipeline(config: PaperConfig) -> WorkspaceStatus:
    initialize_project(config)
    paths = build_workspace_paths(Path(config.workspace_root).resolve(), config.slug)
    return plan_project(paths.root)


def refresh_figure_pipeline(workspace: str | Path) -> WorkspaceStatus:
    workspace_root = Path(workspace).resolve()
    paths = resolve_workspace_paths(workspace_root)
    config = load_project_config(paths)
    existing_state = load_existing_state(paths)
    warnings = list(existing_state.warnings) if existing_state else []

    figure_jobs = build_figure_jobs(paths)
    for job in figure_jobs:
        prompt_text = render_figure_prompt(config, paths, job)
        write_figure_prompt(job, prompt_text)

    status = _status_for(
        config=config,
        paths=paths,
        chunk_jobs=build_chunk_jobs(config, paths),
        figure_jobs=figure_jobs,
        warnings=warnings,
        page_images_ready=bool(collect_page_images(paths.pages_dir)),
    )

    runner = _select_runner(config.runner)
    status = runner.run(status)
    _write_chunk_manifests(paths, status.chunk_jobs)
    _write_figure_manifests(paths, status.figure_jobs)
    write_state(paths, status)
    return status
