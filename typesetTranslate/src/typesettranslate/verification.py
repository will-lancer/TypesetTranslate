from __future__ import annotations

import json
import re
from pathlib import Path

from .models import VerificationFileFinding, VerificationReport
from .paths import resolve_workspace_paths
from .pdf_tools import collect_page_images
from .planner import FIGURE_PLACEHOLDER_PATTERN
from .workflow import load_project_config
from .workspace import write_json, write_text

VERIFY_PATTERN = re.compile(r"VERIFY\s*:", re.IGNORECASE)


def _load_page_manifest_count(page_manifest_path: Path) -> int:
    if not page_manifest_path.exists():
        return 0
    payload = json.loads(page_manifest_path.read_text())
    return len(payload.get("pages", []))


def _scan_file(path: Path) -> VerificationFileFinding:
    if not path.exists():
        return VerificationFileFinding(
            path=str(path),
            exists=False,
            notes=["Missing file."],
        )

    text = path.read_text()
    verify_count = len(VERIFY_PATTERN.findall(text))
    todo_figure_count = len(FIGURE_PLACEHOLDER_PATTERN.findall(text))
    notes: list[str] = []
    if verify_count:
        notes.append(f"{verify_count} unresolved VERIFY note(s).")
    if todo_figure_count:
        notes.append(f"{todo_figure_count} TODO figure placeholder(s) remain.")

    return VerificationFileFinding(
        path=str(path),
        exists=True,
        verify_count=verify_count,
        todo_figure_count=todo_figure_count,
        notes=notes,
    )


def _render_markdown(report: VerificationReport) -> str:
    lines = [
        "# Verification Report",
        "",
        f"- Workspace: `{report.workspace}`",
        f"- Document kind: `{report.document_kind}`",
        f"- Master exists: `{report.master_exists}`",
        f"- Page manifest entries: `{report.page_manifest_entries}`",
        f"- Page images: `{report.page_image_count}`",
        f"- Planned chunk jobs: `{report.planned_chunk_jobs}`",
        f"- Existing chunk files: `{report.existing_chunk_files}`",
        f"- Planned figure jobs: `{report.planned_figure_jobs}`",
        f"- Existing figure files: `{report.existing_figure_files}`",
        f"- Unresolved VERIFY notes: `{report.unresolved_verify_notes}`",
        f"- Remaining TODO figure placeholders: `{report.remaining_todo_figures}`",
        "",
        "## Missing Outputs",
        "",
    ]

    if report.missing_chunk_outputs:
        lines.append("### Missing chunk outputs")
        lines.extend(f"- `{path}`" for path in report.missing_chunk_outputs)
        lines.append("")

    if report.missing_figure_outputs:
        lines.append("### Missing figure outputs")
        lines.extend(f"- `{path}`" for path in report.missing_figure_outputs)
        lines.append("")

    if report.missing_check_wrappers:
        lines.append("### Missing check wrappers")
        lines.extend(f"- `{path}`" for path in report.missing_check_wrappers)
        lines.append("")

    lines.extend(
        [
            "## Chunk Findings",
            "",
        ]
    )
    if report.chunk_findings:
        for finding in report.chunk_findings:
            lines.append(f"### `{finding.path}`")
            lines.append(f"- Exists: `{finding.exists}`")
            lines.append(f"- VERIFY notes: `{finding.verify_count}`")
            lines.append(f"- TODO figures: `{finding.todo_figure_count}`")
            if finding.notes:
                lines.extend(f"- {note}" for note in finding.notes)
            lines.append("")
    else:
        lines.append("No chunk findings.")
        lines.append("")

    lines.extend(
        [
            "## Figure Findings",
            "",
        ]
    )
    if report.figure_findings:
        for finding in report.figure_findings:
            lines.append(f"### `{finding.path}`")
            lines.append(f"- Exists: `{finding.exists}`")
            lines.append(f"- VERIFY notes: `{finding.verify_count}`")
            lines.append(f"- TODO figures: `{finding.todo_figure_count}`")
            if finding.notes:
                lines.extend(f"- {note}" for note in finding.notes)
            lines.append("")
    else:
        lines.append("No figure findings.")
        lines.append("")

    if report.warnings:
        lines.extend(["## Warnings", ""])
        lines.extend(f"- {warning}" for warning in report.warnings)
        lines.append("")

    return "\n".join(lines)


def verify_workspace(workspace: str | Path) -> VerificationReport:
    workspace_root = Path(workspace).resolve()
    paths = resolve_workspace_paths(workspace_root)
    config = load_project_config(paths)

    chunk_jobs = []
    if paths.manifests_dir.exists():
        for manifest_path in sorted(paths.manifests_dir.glob("chunk-*.json")):
            chunk_jobs.append(json.loads(manifest_path.read_text()))

    figure_jobs = []
    if paths.manifests_dir.exists():
        for manifest_path in sorted(paths.manifests_dir.glob("figure-*.json")):
            figure_jobs.append(json.loads(manifest_path.read_text()))

    chunk_findings = [_scan_file(Path(job["output_file"])) for job in chunk_jobs]
    figure_findings = [_scan_file(Path(job["output_file"])) for job in figure_jobs]

    missing_chunk_outputs = [finding.path for finding in chunk_findings if not finding.exists]
    missing_figure_outputs = [finding.path for finding in figure_findings if not finding.exists]
    missing_check_wrappers = [
        job["check_file"]
        for job in chunk_jobs
        if not Path(job["check_file"]).exists()
    ]

    unresolved_verify_notes = sum(finding.verify_count for finding in chunk_findings + figure_findings)
    remaining_todo_figures = sum(finding.todo_figure_count for finding in chunk_findings + figure_findings)
    page_manifest_entries = _load_page_manifest_count(paths.page_manifest_json)
    page_image_count = len(collect_page_images(paths.pages_dir))

    warnings: list[str] = []
    if not paths.master_tex.exists():
        warnings.append("master.tex is missing.")
    if page_manifest_entries == 0:
        warnings.append("Page manifest is empty.")
    if config.page_count and page_manifest_entries and page_manifest_entries != config.page_count:
        warnings.append(
            f"Project page_count is {config.page_count}, but page-manifest.json has {page_manifest_entries} entries."
        )

    report = VerificationReport(
        workspace=str(paths.root),
        document_kind=config.document_kind,
        master_exists=paths.master_tex.exists(),
        page_manifest_entries=page_manifest_entries,
        page_image_count=page_image_count,
        planned_chunk_jobs=len(chunk_jobs),
        existing_chunk_files=sum(1 for finding in chunk_findings if finding.exists),
        missing_chunk_outputs=missing_chunk_outputs,
        planned_figure_jobs=len(figure_jobs),
        existing_figure_files=sum(1 for finding in figure_findings if finding.exists),
        missing_figure_outputs=missing_figure_outputs,
        missing_check_wrappers=missing_check_wrappers,
        unresolved_verify_notes=unresolved_verify_notes,
        remaining_todo_figures=remaining_todo_figures,
        chunk_findings=chunk_findings,
        figure_findings=figure_findings,
        warnings=warnings,
    )

    write_json(paths.verification_json, report.to_dict())
    write_text(paths.verification_md, _render_markdown(report))
    return report
