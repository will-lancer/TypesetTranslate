from __future__ import annotations

import json
from pathlib import Path

from .models import ChunkJob, FigureJob, PaperConfig, WorkspacePaths, WorkspaceStatus
from .paths import build_workspace_paths, resolve_workspace_paths
from .pdf_tools import build_page_manifest, collect_page_images, detect_page_count, render_pages
from .planner import build_chunk_jobs, build_figure_jobs, build_master_inputs
from .prompts import render_figure_prompt, render_transcription_prompt
from .runners import ManifestRunner, MockRunner, Runner
from .workspace import (
    append_job_log,
    copy_source_pdf,
    initialize_workspace,
    manifest_path_for_job,
    read_json,
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
    if name == "openai":
        from .runners.openai import OpenAIRunner

        return OpenAIRunner()
    raise ValueError(f"Unknown runner: {name}")


def _status_for(
    config: PaperConfig,
    paths: WorkspacePaths,
    chunk_jobs: list[ChunkJob],
    figure_jobs: list[FigureJob],
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


def _job_output_exists(job: ChunkJob | FigureJob) -> bool:
    return Path(job.output_file).exists()


def _sync_job_with_existing(
    job: ChunkJob | FigureJob,
    existing_job: ChunkJob | FigureJob | None,
) -> None:
    if existing_job is None:
        if _job_output_exists(job):
            job.status = "completed"
        return

    job.status = existing_job.status
    job.backend = existing_job.backend
    job.attempt_count = existing_job.attempt_count
    job.remote_job_id = existing_job.remote_job_id
    job.submitted_at = existing_job.submitted_at
    job.completed_at = existing_job.completed_at
    job.last_error = existing_job.last_error
    job.result_summary = existing_job.result_summary
    job.notes = list(existing_job.notes)

    if _job_output_exists(job):
        job.status = "completed"
    elif existing_job.status == "completed":
        job.status = "ready"
        job.completed_at = None


def _write_chunk_manifests(paths: WorkspacePaths, chunk_jobs: list[ChunkJob]) -> None:
    for job in chunk_jobs:
        payload = job.to_dict()
        payload["job_type"] = "transcription"
        write_job_manifest(manifest_path_for_job(paths, job.job_id), payload)


def _write_figure_manifests(paths: WorkspacePaths, figure_jobs: list[FigureJob]) -> None:
    for job in figure_jobs:
        payload = job.to_dict()
        payload["job_type"] = "figure"
        write_job_manifest(manifest_path_for_job(paths, job.job_id), payload)


def _load_jobs(paths: WorkspacePaths) -> tuple[list[ChunkJob], list[FigureJob]]:
    chunk_jobs: list[ChunkJob] = []
    figure_jobs: list[FigureJob] = []

    if not paths.manifests_dir.exists():
        return chunk_jobs, figure_jobs

    for manifest_path in sorted(paths.manifests_dir.glob("*.json")):
        payload = read_json(manifest_path)
        job_type = payload.pop("job_type", None)
        if job_type == "transcription":
            chunk_jobs.append(ChunkJob.from_dict(payload))
        elif job_type == "figure":
            figure_jobs.append(FigureJob.from_dict(payload))

    return chunk_jobs, figure_jobs


def _persist_runtime_state(
    paths: WorkspacePaths,
    config: PaperConfig,
    chunk_jobs: list[ChunkJob],
    figure_jobs: list[FigureJob],
    warnings: list[str],
) -> WorkspaceStatus:
    _write_chunk_manifests(paths, chunk_jobs)
    _write_figure_manifests(paths, figure_jobs)
    status = _status_for(
        config=config,
        paths=paths,
        chunk_jobs=chunk_jobs,
        figure_jobs=figure_jobs,
        warnings=warnings,
        page_images_ready=bool(collect_page_images(paths.pages_dir)),
    )
    write_state(paths, status)
    return status


def load_project_config(paths: WorkspacePaths) -> PaperConfig:
    payload = json.loads(paths.project_json.read_text())
    payload.pop("effective_chunk_size", None)
    payload.pop("resolved_title", None)
    return PaperConfig(**payload)


def load_existing_state(paths: WorkspacePaths) -> WorkspaceStatus | None:
    if not paths.state_json.exists():
        return None
    return WorkspaceStatus.from_dict(json.loads(paths.state_json.read_text()))


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
    existing_chunk_jobs, existing_figure_jobs = _load_jobs(paths)
    existing_chunk_map = {job.job_id: job for job in existing_chunk_jobs}
    existing_figure_map = {job.job_id: job for job in existing_figure_jobs}

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
        _sync_job_with_existing(job, existing_chunk_map.get(job.job_id))
        prompt_text = render_transcription_prompt(config, paths, job)
        write_chunk_prompt(job, prompt_text)
        write_check_wrapper(paths, job, config.resolved_title())

    figure_jobs = build_figure_jobs(paths)
    for job in figure_jobs:
        _sync_job_with_existing(job, existing_figure_map.get(job.job_id))
        prompt_text = render_figure_prompt(config, paths, job)
        write_figure_prompt(job, prompt_text)

    write_project_config(paths, config)
    _write_chunk_manifests(paths, chunk_jobs)
    _write_figure_manifests(paths, figure_jobs)

    master_inputs = build_master_inputs(chunk_jobs, paths.root)
    write_master_tex(paths, config.resolved_title(), master_inputs)

    status = _status_for(
        config=config,
        paths=paths,
        chunk_jobs=chunk_jobs,
        figure_jobs=figure_jobs,
        warnings=warnings,
        page_images_ready=page_images_created and bool(page_manifest),
    )
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
    existing_chunk_jobs, existing_figure_jobs = _load_jobs(paths)
    existing_figure_map = {job.job_id: job for job in existing_figure_jobs}
    warnings = list(existing_state.warnings) if existing_state else []

    figure_jobs = build_figure_jobs(paths)
    for job in figure_jobs:
        _sync_job_with_existing(job, existing_figure_map.get(job.job_id))
        prompt_text = render_figure_prompt(config, paths, job)
        write_figure_prompt(job, prompt_text)

    chunk_jobs = build_chunk_jobs(config, paths)
    existing_chunk_map = {job.job_id: job for job in existing_chunk_jobs}
    for job in chunk_jobs:
        _sync_job_with_existing(job, existing_chunk_map.get(job.job_id))

    return _persist_runtime_state(paths, config, chunk_jobs, figure_jobs, warnings)


def dispatch_jobs(
    workspace: str | Path,
    *,
    job_type: str = "all",
    limit: int | None = None,
) -> WorkspaceStatus:
    workspace_root = Path(workspace).resolve()
    paths = resolve_workspace_paths(workspace_root)
    config = load_project_config(paths)
    existing_state = load_existing_state(paths)
    warnings = list(existing_state.warnings) if existing_state else []
    chunk_jobs, figure_jobs = _load_jobs(paths)
    runner = _select_runner(config.runner)

    dispatched = 0
    for job in chunk_jobs:
        if job_type not in {"all", "transcription"}:
            continue
        if job.status != "ready":
            continue
        try:
            runner.dispatch_job(job, paths)
        except Exception as exc:
            job.status = "failed"
            job.last_error = str(exc)
            job.result_summary = "Dispatch failed."
        append_job_log(paths, job.job_id, "dispatch", job.to_dict())
        dispatched += 1
        if limit is not None and dispatched >= limit:
            return _persist_runtime_state(paths, config, chunk_jobs, figure_jobs, warnings)

    for job in figure_jobs:
        if job_type not in {"all", "figure"}:
            continue
        if job.status != "ready":
            continue
        try:
            runner.dispatch_job(job, paths)
        except Exception as exc:
            job.status = "failed"
            job.last_error = str(exc)
            job.result_summary = "Dispatch failed."
        append_job_log(paths, job.job_id, "dispatch", job.to_dict())
        dispatched += 1
        if limit is not None and dispatched >= limit:
            break

    return _persist_runtime_state(paths, config, chunk_jobs, figure_jobs, warnings)


def poll_jobs(
    workspace: str | Path,
    *,
    job_type: str = "all",
) -> WorkspaceStatus:
    workspace_root = Path(workspace).resolve()
    paths = resolve_workspace_paths(workspace_root)
    config = load_project_config(paths)
    existing_state = load_existing_state(paths)
    warnings = list(existing_state.warnings) if existing_state else []
    chunk_jobs, figure_jobs = _load_jobs(paths)
    runner = _select_runner(config.runner)

    for job in chunk_jobs:
        if job_type not in {"all", "transcription"}:
            continue
        try:
            runner.poll_job(job, paths)
        except Exception as exc:
            job.status = "failed"
            job.last_error = str(exc)
            job.result_summary = "Polling failed."
        append_job_log(paths, job.job_id, "poll", job.to_dict())

    for job in figure_jobs:
        if job_type not in {"all", "figure"}:
            continue
        try:
            runner.poll_job(job, paths)
        except Exception as exc:
            job.status = "failed"
            job.last_error = str(exc)
            job.result_summary = "Polling failed."
        append_job_log(paths, job.job_id, "poll", job.to_dict())

    return _persist_runtime_state(paths, config, chunk_jobs, figure_jobs, warnings)
