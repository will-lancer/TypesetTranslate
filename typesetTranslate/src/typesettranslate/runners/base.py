from __future__ import annotations

from abc import ABC, abstractmethod

from ..models import ChunkJob, FigureJob, WorkspacePaths


class Runner(ABC):
    @abstractmethod
    def dispatch_job(self, job: ChunkJob | FigureJob, paths: WorkspacePaths) -> None:
        raise NotImplementedError

    @abstractmethod
    def poll_job(self, job: ChunkJob | FigureJob, paths: WorkspacePaths) -> None:
        raise NotImplementedError
