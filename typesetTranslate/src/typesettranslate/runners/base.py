from __future__ import annotations

from abc import ABC, abstractmethod

from ..models import WorkspaceStatus


class Runner(ABC):
    @abstractmethod
    def run(self, status: WorkspaceStatus) -> WorkspaceStatus:
        raise NotImplementedError

