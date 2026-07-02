from __future__ import annotations

import base64
import json
import os
import re
from datetime import datetime, timezone
from pathlib import Path
from urllib import error, request

from ..models import ChunkJob, FigureJob, WorkspacePaths
from ..workspace import read_json
from .base import Runner

CHUNK_RANGE_PATTERN = re.compile(r"pp(\d+)-(\d+)")


def _strip_markdown_fences(text: str) -> str:
    stripped = text.strip()
    if stripped.startswith("```") and stripped.endswith("```"):
        lines = stripped.splitlines()
        if len(lines) >= 2:
            return "\n".join(lines[1:-1]).strip()
    return text


class OpenAIRunner(Runner):
    def _base_url(self) -> str:
        return os.environ.get("OPENAI_BASE_URL", "https://api.openai.com/v1").rstrip("/")

    def _api_key(self) -> str:
        api_key = os.environ.get("OPENAI_API_KEY")
        if not api_key:
            raise RuntimeError("OPENAI_API_KEY is required for the openai runner.")
        return api_key

    def _model(self, paths: WorkspacePaths) -> str:
        config = read_json(paths.project_json)
        return config.get("runner_model") or os.environ.get("TYPESETTRANSLATE_OPENAI_MODEL") or "gpt-5"

    def _request(self, method: str, path: str, payload: dict | None = None) -> dict:
        body = None
        if payload is not None:
            body = json.dumps(payload).encode()
        req = request.Request(
            url=f"{self._base_url()}/{path.lstrip('/')}",
            data=body,
            method=method,
            headers={
                "Authorization": f"Bearer {self._api_key()}",
                "Content-Type": "application/json",
            },
        )
        try:
            with request.urlopen(req, timeout=60) as response:
                return json.loads(response.read().decode())
        except error.HTTPError as exc:
            detail = exc.read().decode()
            raise RuntimeError(f"OpenAI API request failed: HTTP {exc.code}: {detail}") from exc

    def _image_input(self, image_path: Path) -> dict:
        encoded = base64.b64encode(image_path.read_bytes()).decode()
        return {
            "type": "input_image",
            "image_url": f"data:image/png;base64,{encoded}",
        }

    def _chunk_page_paths(self, job: ChunkJob, paths: WorkspacePaths) -> list[Path]:
        page_paths = []
        for page_number in range(job.start_page, job.end_page + 1):
            page_path = paths.pages_dir / f"page-{page_number:04d}.png"
            if page_path.exists():
                page_paths.append(page_path)
        return page_paths

    def _figure_page_paths(self, job: FigureJob, paths: WorkspacePaths) -> list[Path]:
        page_numbers: list[int] = []
        if job.source_page_hint and job.source_page_hint.isdigit():
            page_numbers.append(int(job.source_page_hint))
        elif job.source_chunk_file:
            match = CHUNK_RANGE_PATTERN.search(Path(job.source_chunk_file).stem)
            if match:
                start_page = int(match.group(1))
                end_page = int(match.group(2))
                page_numbers.extend(range(start_page, end_page + 1))

        page_paths = []
        for page_number in page_numbers:
            page_path = paths.pages_dir / f"page-{page_number:04d}.png"
            if page_path.exists():
                page_paths.append(page_path)
        return page_paths

    def _build_input(self, job: ChunkJob | FigureJob, paths: WorkspacePaths) -> list[dict]:
        prompt_text = Path(job.prompt_file).read_text()
        content: list[dict] = [
            {"type": "input_text", "text": prompt_text},
            {
                "type": "input_text",
                "text": "Return only the full file contents for the assigned output file. Do not use Markdown fences.",
            },
        ]

        if isinstance(job, ChunkJob):
            page_paths = self._chunk_page_paths(job, paths)
        else:
            page_paths = self._figure_page_paths(job, paths)
            if job.source_chunk_file and Path(job.source_chunk_file).exists():
                content.append(
                    {
                        "type": "input_text",
                        "text": "Source chunk context:\n" + Path(job.source_chunk_file).read_text(),
                    }
                )

        if not page_paths:
            raise RuntimeError("The openai runner requires rendered page images for the assigned job.")

        for page_path in page_paths:
            content.append(self._image_input(page_path))

        return [
            {
                "role": "developer",
                "content": [
                    {
                        "type": "input_text",
                        "text": "You are a narrow LaTeX transcription agent. Output only raw file contents for the assigned file.",
                    }
                ],
            },
            {
                "role": "user",
                "content": content,
            },
        ]

    def _extract_output_text(self, payload: dict) -> str:
        output_text = payload.get("output_text")
        if isinstance(output_text, str) and output_text.strip():
            return output_text

        parts: list[str] = []
        for item in payload.get("output", []):
            if item.get("type") != "message":
                continue
            for content in item.get("content", []):
                if content.get("type") == "output_text" and content.get("text"):
                    parts.append(content["text"])
        return "\n".join(parts).strip()

    def _extract_error(self, payload: dict) -> str:
        if payload.get("error"):
            return json.dumps(payload["error"], sort_keys=True)
        if payload.get("incomplete_details"):
            return json.dumps(payload["incomplete_details"], sort_keys=True)
        return f"Remote job ended with status {payload.get('status', 'unknown')}"

    def dispatch_job(self, job: ChunkJob | FigureJob, paths: WorkspacePaths) -> None:
        if job.status != "ready":
            return

        response = self._request(
            "POST",
            "responses",
            {
                "model": self._model(paths),
                "background": True,
                "store": True,
                "metadata": {"job_id": job.job_id, "workspace": paths.root.name},
                "input": self._build_input(job, paths),
            },
        )

        job.backend = "openai"
        job.attempt_count += 1
        job.remote_job_id = response.get("id")
        job.submitted_at = datetime.now(timezone.utc).isoformat()
        job.last_error = None
        job.result_summary = f"Submitted to OpenAI with remote status {response.get('status', 'unknown')}."
        job.status = "dispatched"

    def poll_job(self, job: ChunkJob | FigureJob, paths: WorkspacePaths) -> None:
        if not job.remote_job_id:
            return

        response = self._request("GET", f"responses/{job.remote_job_id}")
        remote_status = response.get("status")
        if remote_status in {"queued", "in_progress"}:
            job.status = "dispatched"
            job.result_summary = f"Remote status: {remote_status}."
            return

        if remote_status == "completed":
            output_text = _strip_markdown_fences(self._extract_output_text(response))
            if not output_text.strip():
                raise RuntimeError("OpenAI response completed without any output text.")
            Path(job.output_file).write_text(output_text)
            job.status = "completed"
            job.completed_at = datetime.now(timezone.utc).isoformat()
            job.last_error = None
            job.result_summary = "OpenAI response completed and wrote the output file."
            return

        job.status = "failed"
        job.last_error = self._extract_error(response)
        job.result_summary = f"OpenAI response ended with status {remote_status}."
