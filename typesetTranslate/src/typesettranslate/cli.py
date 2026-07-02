from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from .compile_tools import run_compile_verification
from .export import export_workspace
from .models import PaperConfig
from .verification import verify_workspace
from .workflow import (
    dispatch_jobs,
    initialize_project,
    plan_project,
    poll_jobs,
    refresh_figure_pipeline,
    run_pipeline,
)


def _add_project_args(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("source_pdf", help="Path to the source PDF.")
    parser.add_argument("--slug", required=True, help="Workspace slug for this paper or book.")
    parser.add_argument(
        "--workspace-root",
        default="./dirs",
        help="Root directory under which workspace directories are created.",
    )
    parser.add_argument("--style", default="jhep", help="Target LaTeX style.")
    parser.add_argument(
        "--document-kind",
        default="paper",
        choices=["paper", "book"],
        help="Choose planning defaults for a paper or a book.",
    )
    parser.add_argument(
        "--chunk-size",
        type=int,
        default=None,
        help="Pages per chunk. Defaults to 5 for papers and 3 for books.",
    )
    parser.add_argument(
        "--transcription-workers",
        type=int,
        default=3,
        help="Planned number of transcription workers.",
    )
    parser.add_argument(
        "--figure-workers",
        type=int,
        default=1,
        help="Planned number of figure workers.",
    )
    parser.add_argument(
        "--runner",
        default="manifest",
        choices=["manifest", "mock", "openai"],
        help="Runner backend.",
    )
    parser.add_argument(
        "--runner-model",
        default=None,
        help="Optional model name for the selected runner backend.",
    )
    parser.add_argument(
        "--page-count",
        type=int,
        default=None,
        help="Override page count if PDF tooling is unavailable.",
    )
    parser.add_argument(
        "--title",
        default=None,
        help="Optional document title for the generated master.tex.",
    )


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="paperbot")
    subparsers = parser.add_subparsers(dest="command", required=True)

    init_parser = subparsers.add_parser("init", help="Initialize a workspace and write project metadata.")
    _add_project_args(init_parser)

    plan_parser = subparsers.add_parser(
        "plan",
        help="Render pages when possible and plan chunk jobs for an existing workspace.",
    )
    plan_parser.add_argument("workspace", help="Path to an existing paper workspace.")
    plan_parser.add_argument(
        "--page-count",
        type=int,
        default=None,
        help="Override page count for this planning pass.",
    )
    plan_parser.add_argument(
        "--runner",
        default=None,
        choices=["manifest", "mock", "openai"],
        help="Override the stored runner for this planning pass.",
    )

    run_parser = subparsers.add_parser("run", help="Initialize and plan a workspace in one command.")
    _add_project_args(run_parser)

    inspect_parser = subparsers.add_parser("inspect", help="Print the current workspace state.")
    inspect_parser.add_argument("workspace", help="Path to an existing paper workspace.")

    refresh_parser = subparsers.add_parser(
        "refresh-figures",
        help="Scan chunk placeholders and regenerate figure jobs and prompts.",
    )
    refresh_parser.add_argument("workspace", help="Path to an existing paper workspace.")

    dispatch_parser = subparsers.add_parser(
        "dispatch",
        help="Submit ready jobs for the configured runner backend.",
    )
    dispatch_parser.add_argument("workspace", help="Path to an existing paper workspace.")
    dispatch_parser.add_argument(
        "--job-type",
        default="all",
        choices=["all", "transcription", "figure"],
        help="Limit dispatch to one job class.",
    )
    dispatch_parser.add_argument(
        "--limit",
        type=int,
        default=None,
        help="Maximum number of jobs to dispatch.",
    )

    poll_parser = subparsers.add_parser(
        "poll",
        help="Refresh remote job state for the configured runner backend.",
    )
    poll_parser.add_argument("workspace", help="Path to an existing paper workspace.")
    poll_parser.add_argument(
        "--job-type",
        default="all",
        choices=["all", "transcription", "figure"],
        help="Limit polling to one job class.",
    )

    verify_parser = subparsers.add_parser(
        "verify",
        help="Run structural verification and write reports/verification.{json,md}.",
    )
    verify_parser.add_argument("workspace", help="Path to an existing paper workspace.")

    compile_parser = subparsers.add_parser(
        "verify-compile",
        help="Compile master/check targets and write reports/compile.{json,md}.",
    )
    compile_parser.add_argument("workspace", help="Path to an existing paper workspace.")
    compile_parser.add_argument(
        "--scope",
        default="all",
        choices=["all", "master", "checks"],
        help="Choose which LaTeX targets to compile.",
    )

    export_parser = subparsers.add_parser(
        "export",
        help="Export the current workspace into newPapers-style output.",
    )
    export_parser.add_argument("workspace", help="Path to an existing paper workspace.")
    export_parser.add_argument(
        "--dest-root",
        default="./newPapers",
        help="Destination root for exported workspaces.",
    )
    export_parser.add_argument(
        "--include-pdf",
        action="store_true",
        help="Include output/master.pdf if it exists.",
    )

    return parser


def _print_payload(payload: dict) -> None:
    print(json.dumps(payload, indent=2))


def _config_from_args(args: argparse.Namespace) -> PaperConfig:
    return PaperConfig(
        slug=args.slug,
        source_pdf=args.source_pdf,
        workspace_root=args.workspace_root,
        style=args.style,
        document_kind=args.document_kind,
        chunk_size=args.chunk_size,
        transcription_workers=args.transcription_workers,
        figure_workers=args.figure_workers,
        runner=args.runner,
        runner_model=args.runner_model,
        page_count=args.page_count,
        title=args.title,
    )


def _cmd_init(args: argparse.Namespace) -> int:
    status = initialize_project(_config_from_args(args))
    _print_payload(status.to_dict())
    return 0


def _cmd_plan(args: argparse.Namespace) -> int:
    status = plan_project(
        args.workspace,
        page_count_override=args.page_count,
        runner_override=args.runner,
    )
    _print_payload(status.to_dict())
    return 0


def _cmd_run(args: argparse.Namespace) -> int:
    status = run_pipeline(_config_from_args(args))
    _print_payload(status.to_dict())
    return 0


def _find_state_path(workspace: Path) -> Path | None:
    candidates = [
        workspace / "state" / "state.json",
        workspace / "state.json",
    ]
    for candidate in candidates:
        if candidate.exists():
            return candidate
    return None


def _cmd_inspect(args: argparse.Namespace) -> int:
    state_path = _find_state_path(Path(args.workspace))
    if state_path is None:
        print(f"state.json not found in {args.workspace}", file=sys.stderr)
        return 1
    print(state_path.read_text())
    return 0


def _cmd_refresh_figures(args: argparse.Namespace) -> int:
    status = refresh_figure_pipeline(args.workspace)
    _print_payload(status.to_dict())
    return 0


def _cmd_dispatch(args: argparse.Namespace) -> int:
    status = dispatch_jobs(args.workspace, job_type=args.job_type, limit=args.limit)
    _print_payload(status.to_dict())
    return 0


def _cmd_poll(args: argparse.Namespace) -> int:
    status = poll_jobs(args.workspace, job_type=args.job_type)
    _print_payload(status.to_dict())
    return 0


def _cmd_verify(args: argparse.Namespace) -> int:
    report = verify_workspace(args.workspace)
    _print_payload(report.to_dict())
    return 0


def _cmd_verify_compile(args: argparse.Namespace) -> int:
    report = run_compile_verification(args.workspace, scope=args.scope)
    _print_payload(report.to_dict())
    return 0


def _cmd_export(args: argparse.Namespace) -> int:
    report = export_workspace(
        args.workspace,
        destination_root=args.dest_root,
        include_pdf=args.include_pdf,
    )
    _print_payload(report.to_dict())
    return 0


def main() -> int:
    parser = _build_parser()
    args = parser.parse_args()
    if args.command == "init":
        return _cmd_init(args)
    if args.command == "plan":
        return _cmd_plan(args)
    if args.command == "run":
        return _cmd_run(args)
    if args.command == "inspect":
        return _cmd_inspect(args)
    if args.command == "refresh-figures":
        return _cmd_refresh_figures(args)
    if args.command == "dispatch":
        return _cmd_dispatch(args)
    if args.command == "poll":
        return _cmd_poll(args)
    if args.command == "verify":
        return _cmd_verify(args)
    if args.command == "verify-compile":
        return _cmd_verify_compile(args)
    if args.command == "export":
        return _cmd_export(args)
    parser.error(f"Unknown command: {args.command}")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
