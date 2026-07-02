from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path

from ..models import ChunkJob, FigureJob, WorkspacePaths
from .base import Runner


class MockRunner(Runner):
    """Mark jobs as prepared without leaving the local machine."""

    def dispatch_job(self, job: ChunkJob | FigureJob, paths: WorkspacePaths) -> None:
        if job.status != "ready":
            return
        job.backend = "mock"
        job.attempt_count += 1
        job.submitted_at = datetime.now(timezone.utc).isoformat()
        job.status = "dispatched"
        job.last_error = None
        job.result_summary = "Mock runner marked this job as dispatched."

    def poll_job(self, job: ChunkJob | FigureJob, paths: WorkspacePaths) -> None:
        if job.status not in {"dispatched", "ready"}:
            return

        output_path = Path(job.output_file)
        if not output_path.exists():
            if isinstance(job, ChunkJob):
                output_path.write_text(
                    "\n".join(
                        [
                            f"% Mock transcription output for {job.job_id}.",
                            f"% Original pages: {job.start_page}-{job.end_page}",
                            "% Replace this file with real transcription output.",
                            "",
                        ]
                    )
                )
            else:
                output_path.write_text(
                    "\n".join(
                        [
                            f"% Mock figure output for {job.job_id}.",
                            "% Replace this file with real figure output.",
                            "",
                        ]
                    )
                )

        job.status = "completed"
        job.completed_at = datetime.now(timezone.utc).isoformat()
        job.last_error = None
        job.result_summary = "Mock runner wrote a placeholder output file."
