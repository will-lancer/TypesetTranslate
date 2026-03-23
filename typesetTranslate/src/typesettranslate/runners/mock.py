from __future__ import annotations

from ..models import WorkspaceStatus
from .base import Runner


class MockRunner(Runner):
    """Mark jobs as prepared without leaving the local machine."""

    def run(self, status: WorkspaceStatus) -> WorkspaceStatus:
        for job in status.chunk_jobs:
            if job.status == "pending":
                job.status = "mock-dispatched"
                job.notes.append("Mock runner prepared this chunk job.")
        for job in status.figure_jobs:
            if job.status == "pending":
                job.status = "mock-dispatched"
                job.notes.append("Mock runner prepared this figure job.")
        return status

