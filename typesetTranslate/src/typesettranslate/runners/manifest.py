from __future__ import annotations

from ..models import WorkspaceStatus
from .base import Runner


class ManifestRunner(Runner):
    """Emit job manifests only; do not dispatch anything."""

    def run(self, status: WorkspaceStatus) -> WorkspaceStatus:
        for job in status.chunk_jobs:
            if job.status == "pending":
                job.status = "ready"
        for job in status.figure_jobs:
            if job.status == "pending":
                job.status = "queued"
        return status

