from __future__ import annotations

from ..models import ChunkJob, FigureJob, WorkspacePaths
from .base import Runner


class ManifestRunner(Runner):
    """Emit job manifests only; do not dispatch anything."""

    def dispatch_job(self, job: ChunkJob | FigureJob, paths: WorkspacePaths) -> None:
        job.backend = "manifest"
        job.result_summary = "Manifest backend does not submit jobs automatically."
        note = "Dispatch skipped by manifest backend."
        if note not in job.notes:
            job.notes.append(note)

    def poll_job(self, job: ChunkJob | FigureJob, paths: WorkspacePaths) -> None:
        if job.status != "completed" and job.output_file:
            from pathlib import Path

            if Path(job.output_file).exists():
                job.status = "completed"
                job.result_summary = "Output file exists."
