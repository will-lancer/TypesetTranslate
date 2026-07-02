from __future__ import annotations

import re
import shutil
import subprocess
from pathlib import Path

from .models import CompileReport, CompileTargetReport
from .paths import resolve_workspace_paths
from .workspace import read_json, write_json, write_text

ERROR_PATTERNS = (
    re.compile(r"^! LaTeX Error: (.+)$", re.MULTILINE),
    re.compile(r"^! (.+)$", re.MULTILINE),
)
WARNING_PATTERN = re.compile(r"^(?:LaTeX|Package) .*Warning: (.+)$", re.MULTILINE)
MISSING_INPUT_PATTERN = re.compile(r"File `([^`]+)' not found")


def _select_compile_tool() -> str | None:
    if shutil.which("latexmk"):
        return "latexmk"
    if shutil.which("pdflatex"):
        return "pdflatex"
    return None


def _compile_command(tool: str, target: Path) -> list[str]:
    rel_target = target.as_posix()
    if tool == "latexmk":
        return ["latexmk", "-pdf", "-interaction=nonstopmode", "-halt-on-error", rel_target]
    return ["pdflatex", "-interaction=nonstopmode", "-halt-on-error", rel_target]


def _parse_log_text(text: str) -> tuple[list[str], list[str], list[str]]:
    errors: list[str] = []
    for pattern in ERROR_PATTERNS:
        for match in pattern.findall(text):
            message = match.strip()
            if message and message not in errors:
                errors.append(message)

    warnings = []
    for match in WARNING_PATTERN.findall(text):
        message = match.strip()
        if message and message not in warnings:
            warnings.append(message)

    missing_inputs = []
    for match in MISSING_INPUT_PATTERN.findall(text):
        if match not in missing_inputs:
            missing_inputs.append(match)

    return errors, warnings, missing_inputs


def _render_markdown(report: CompileReport) -> str:
    lines = [
        "# Compile Report",
        "",
        f"- Workspace: `{report.workspace}`",
        f"- Tool: `{report.tool or 'unavailable'}`",
        f"- Targets: `{len(report.targets)}`",
        "",
    ]

    if report.warnings:
        lines.append("## Warnings")
        lines.append("")
        lines.extend(f"- {warning}" for warning in report.warnings)
        lines.append("")

    for target in report.targets:
        lines.append(f"## `{target.target}`")
        lines.append("")
        lines.append(f"- Kind: `{target.kind}`")
        lines.append(f"- Success: `{target.success}`")
        lines.append(f"- Owner job: `{target.owner_job_id or 'n/a'}`")
        lines.append(f"- Log: `{target.log_path or 'n/a'}`")
        lines.append(f"- PDF: `{target.pdf_path or 'n/a'}`")
        if target.errors:
            lines.extend(f"- Error: {error}" for error in target.errors)
        if target.missing_inputs:
            lines.extend(f"- Missing input: {path}" for path in target.missing_inputs)
        if target.warnings:
            lines.extend(f"- Warning: {warning}" for warning in target.warnings)
        lines.append("")

    return "\n".join(lines)


def run_compile_verification(workspace: str | Path, scope: str = "all") -> CompileReport:
    workspace_root = Path(workspace).resolve()
    paths = resolve_workspace_paths(workspace_root)
    tool = _select_compile_tool()
    warnings: list[str] = []

    targets: list[tuple[str, Path, str | None]] = []
    if scope in {"all", "master"} and paths.master_tex.exists():
        targets.append(("master", paths.master_tex.relative_to(paths.root), None))

    if scope in {"all", "checks"} and paths.manifests_dir.exists():
        for manifest_path in sorted(paths.manifests_dir.glob("chunk-*.json")):
            payload = read_json(manifest_path)
            check_file = payload.get("check_file")
            if check_file:
                targets.append(("check", Path(check_file).resolve().relative_to(paths.root), payload["job_id"]))

    if tool is None:
        warnings.append("Neither latexmk nor pdflatex is available.")
        report = CompileReport(workspace=str(paths.root), tool=None, targets=[], warnings=warnings)
        write_json(paths.compile_json, report.to_dict())
        write_text(paths.compile_md, _render_markdown(report))
        return report

    target_reports: list[CompileTargetReport] = []
    for kind, rel_target, owner_job_id in targets:
        absolute_target = paths.root / rel_target
        command = _compile_command(tool, rel_target)
        result = subprocess.run(
            command,
            cwd=paths.root,
            check=False,
            capture_output=True,
            text=True,
        )

        raw_log_path = paths.compile_logs_dir / f"{rel_target.stem}.stdout.log"
        raw_log_path.write_text(result.stdout + ("\n" if result.stdout and result.stderr else "") + result.stderr)

        latex_log_path = absolute_target.with_suffix(".log")
        log_text = raw_log_path.read_text()
        if latex_log_path.exists():
            log_text += "\n" + latex_log_path.read_text()

        errors, target_warnings, missing_inputs = _parse_log_text(log_text)
        pdf_path = absolute_target.with_suffix(".pdf")
        success = result.returncode == 0 and pdf_path.exists()

        target_reports.append(
            CompileTargetReport(
                target=str(absolute_target),
                kind=kind,
                success=success,
                tool=tool,
                owner_job_id=owner_job_id,
                log_path=str(raw_log_path),
                pdf_path=str(pdf_path) if pdf_path.exists() else None,
                errors=errors,
                warnings=target_warnings,
                missing_inputs=missing_inputs,
            )
        )

    report = CompileReport(
        workspace=str(paths.root),
        tool=tool,
        targets=target_reports,
        warnings=warnings,
    )
    write_json(paths.compile_json, report.to_dict())
    write_text(paths.compile_md, _render_markdown(report))
    return report
