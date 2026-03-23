from __future__ import annotations

from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any, Literal

DocumentKind = Literal["paper", "book"]


@dataclass(slots=True)
class PaperConfig:
    slug: str
    source_pdf: str
    workspace_root: str
    style: str = "jhep"
    document_kind: DocumentKind = "paper"
    chunk_size: int | None = None
    transcription_workers: int = 3
    figure_workers: int = 1
    runner: str = "manifest"
    page_count: int | None = None
    title: str | None = None

    def effective_chunk_size(self) -> int:
        if self.chunk_size is not None:
            return self.chunk_size
        if self.document_kind == "book":
            return 3
        return 5

    def resolved_title(self) -> str:
        if self.title:
            return self.title
        return self.slug.replace("-", " ").title()

    def to_dict(self) -> dict[str, Any]:
        payload = asdict(self)
        payload["effective_chunk_size"] = self.effective_chunk_size()
        payload["resolved_title"] = self.resolved_title()
        return payload


@dataclass(slots=True)
class ChunkJob:
    job_id: str
    start_page: int
    end_page: int
    output_file: str
    prompt_file: str
    check_file: str
    status: str = "pending"
    notes: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(slots=True)
class FigureJob:
    job_id: str
    figure_label: str
    output_file: str
    prompt_file: str
    source_chunk_file: str | None = None
    source_page_hint: str | None = None
    placeholder_text: str | None = None
    status: str = "pending"
    notes: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(slots=True)
class WorkspaceStatus:
    workspace: str
    document_kind: DocumentKind
    page_images_ready: bool
    page_count_detected: bool
    runner: str
    chunk_size: int
    chunk_jobs: list[ChunkJob]
    figure_jobs: list[FigureJob]
    warnings: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return {
            "workspace": self.workspace,
            "document_kind": self.document_kind,
            "page_images_ready": self.page_images_ready,
            "page_count_detected": self.page_count_detected,
            "runner": self.runner,
            "chunk_size": self.chunk_size,
            "chunk_jobs": [job.to_dict() for job in self.chunk_jobs],
            "figure_jobs": [job.to_dict() for job in self.figure_jobs],
            "warnings": self.warnings,
        }


@dataclass(slots=True)
class VerificationFileFinding:
    path: str
    exists: bool
    verify_count: int = 0
    todo_figure_count: int = 0
    notes: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(slots=True)
class VerificationReport:
    workspace: str
    document_kind: DocumentKind
    master_exists: bool
    page_manifest_entries: int
    page_image_count: int
    planned_chunk_jobs: int
    existing_chunk_files: int
    missing_chunk_outputs: list[str]
    planned_figure_jobs: int
    existing_figure_files: int
    missing_figure_outputs: list[str]
    missing_check_wrappers: list[str]
    unresolved_verify_notes: int
    remaining_todo_figures: int
    chunk_findings: list[VerificationFileFinding]
    figure_findings: list[VerificationFileFinding]
    warnings: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return {
            "workspace": self.workspace,
            "document_kind": self.document_kind,
            "master_exists": self.master_exists,
            "page_manifest_entries": self.page_manifest_entries,
            "page_image_count": self.page_image_count,
            "planned_chunk_jobs": self.planned_chunk_jobs,
            "existing_chunk_files": self.existing_chunk_files,
            "missing_chunk_outputs": self.missing_chunk_outputs,
            "planned_figure_jobs": self.planned_figure_jobs,
            "existing_figure_files": self.existing_figure_files,
            "missing_figure_outputs": self.missing_figure_outputs,
            "missing_check_wrappers": self.missing_check_wrappers,
            "unresolved_verify_notes": self.unresolved_verify_notes,
            "remaining_todo_figures": self.remaining_todo_figures,
            "chunk_findings": [finding.to_dict() for finding in self.chunk_findings],
            "figure_findings": [finding.to_dict() for finding in self.figure_findings],
            "warnings": self.warnings,
        }


@dataclass(slots=True)
class WorkspacePaths:
    root: Path
    source_dir: Path
    artifacts_dir: Path
    output_dir: Path
    jobs_dir: Path
    manifests_dir: Path
    prompts_dir: Path
    logs_dir: Path
    reports_dir: Path
    state_dir: Path
    original_pdf: Path
    project_json: Path
    state_json: Path
    page_manifest_json: Path
    pages_dir: Path
    master_tex: Path
    chunks_dir: Path
    figures_dir: Path
    checks_dir: Path
    verification_json: Path
    verification_md: Path
