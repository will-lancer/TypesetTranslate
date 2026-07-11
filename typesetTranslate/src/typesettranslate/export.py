from __future__ import annotations

import shutil
from pathlib import Path

from .models import ExportReport
from .paths import resolve_workspace_paths
from .workspace import write_json


def _copy_if_exists(source: Path, destination: Path, exported_files: list[str]) -> None:
    if not source.exists():
        return
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, destination)
    exported_files.append(str(destination))


def _copy_tree_if_exists(source: Path, destination: Path, exported_files: list[str]) -> None:
    if not source.exists():
        return
    if destination.exists():
        shutil.rmtree(destination)
    shutil.copytree(source, destination)
    for path in sorted(destination.rglob("*")):
        if path.is_file():
            exported_files.append(str(path))


def _rewrite_exported_latex_paths(latex_root: Path) -> None:
    for tex_path in latex_root.rglob("*.tex"):
        text = tex_path.read_text()
        rewritten = text.replace("{output/chunks/", "{chunks/")
        rewritten = rewritten.replace("{output/figures/", "{figures/")
        if rewritten != text:
            tex_path.write_text(rewritten)


def export_workspace(
    workspace: str | Path,
    *,
    destination_root: str | Path = "./newPapers",
    include_pdf: bool = False,
) -> ExportReport:
    workspace_root = Path(workspace).resolve()
    paths = resolve_workspace_paths(workspace_root)
    destination = Path(destination_root).resolve() / paths.root.name
    if destination.exists():
        shutil.rmtree(destination)
    destination.mkdir(parents=True, exist_ok=True)

    exported_files: list[str] = []
    warnings: list[str] = []

    _copy_if_exists(paths.master_tex, destination / "latex" / "master.tex", exported_files)
    _copy_tree_if_exists(paths.chunks_dir, destination / "latex" / "chunks", exported_files)
    _copy_tree_if_exists(paths.figures_dir, destination / "latex" / "figures", exported_files)
    _copy_if_exists(paths.project_json, destination / "state" / "project.json", exported_files)
    _copy_if_exists(paths.state_json, destination / "state" / "state.json", exported_files)
    _copy_if_exists(paths.verification_json, destination / "reports" / "verification.json", exported_files)
    _copy_if_exists(paths.verification_md, destination / "reports" / "verification.md", exported_files)
    _copy_if_exists(paths.compile_json, destination / "reports" / "compile.json", exported_files)
    _copy_if_exists(paths.compile_md, destination / "reports" / "compile.md", exported_files)

    _rewrite_exported_latex_paths(destination / "latex")

    if include_pdf:
        master_pdf = paths.master_tex.with_suffix(".pdf")
        if master_pdf.exists():
            _copy_if_exists(master_pdf, destination / "latex" / master_pdf.name, exported_files)
        else:
            warnings.append("include_pdf was requested but output/master.pdf does not exist.")

    if not exported_files:
        warnings.append("No exportable files were found.")

    report = ExportReport(
        workspace=str(paths.root),
        destination=str(destination),
        exported_files=exported_files,
        warnings=warnings,
    )
    write_json(destination / "export-manifest.json", report.to_dict())
    return report
