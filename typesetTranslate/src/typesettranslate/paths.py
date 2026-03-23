from __future__ import annotations

from pathlib import Path

from .models import WorkspacePaths


def build_workspace_paths(workspace_root: Path, slug: str) -> WorkspacePaths:
    root = workspace_root / slug
    source_dir = root / "source"
    artifacts_dir = root / "artifacts"
    output_dir = root / "output"
    jobs_dir = root / "jobs"
    state_dir = root / "state"

    return WorkspacePaths(
        root=root,
        source_dir=source_dir,
        artifacts_dir=artifacts_dir,
        output_dir=output_dir,
        jobs_dir=jobs_dir,
        manifests_dir=jobs_dir / "manifests",
        prompts_dir=jobs_dir / "prompts",
        logs_dir=jobs_dir / "logs",
        reports_dir=root / "reports",
        state_dir=state_dir,
        original_pdf=source_dir / "original.pdf",
        project_json=state_dir / "project.json",
        state_json=state_dir / "state.json",
        page_manifest_json=artifacts_dir / "page-manifest.json",
        pages_dir=artifacts_dir / "pages",
        master_tex=output_dir / "master.tex",
        chunks_dir=output_dir / "chunks",
        figures_dir=output_dir / "figures",
        checks_dir=output_dir / "checks",
        verification_json=root / "reports" / "verification.json",
        verification_md=root / "reports" / "verification.md",
    )


def resolve_workspace_paths(root: Path) -> WorkspacePaths:
    return build_workspace_paths(root.parent, root.name)


def ensure_workspace_dirs(paths: WorkspacePaths) -> None:
    for directory in (
        paths.root,
        paths.source_dir,
        paths.artifacts_dir,
        paths.pages_dir,
        paths.output_dir,
        paths.chunks_dir,
        paths.figures_dir,
        paths.checks_dir,
        paths.jobs_dir,
        paths.manifests_dir,
        paths.prompts_dir,
        paths.logs_dir,
        paths.reports_dir,
        paths.state_dir,
    ):
        directory.mkdir(parents=True, exist_ok=True)
