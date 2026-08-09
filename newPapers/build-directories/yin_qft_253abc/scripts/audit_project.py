#!/usr/bin/env python3
"""Structural and provenance audit for the Yin QFT pilot.

Draft mode keeps the scaffold buildable while production files are being
written.  Missing or incomplete production artifacts are warnings there.
Malformed files, duplicate identifiers, invalid source classes, and
contradictory frozen-source metadata are errors in both modes.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
import hashlib
import json
from pathlib import Path
import re
import sys
from typing import Any, Iterable

try:
    from audit_verbatim import run_audit as run_verbatim_audit
except ModuleNotFoundError:  # Support `python -m scripts.audit_project`.
    from .audit_verbatim import run_audit as run_verbatim_audit


ROOT = Path(__file__).resolve().parents[1]
PILOT = ROOT / "work" / "pilot"
CHAPTER = ROOT / "latex" / "chapters" / "253a" / "chapter01.tex"

SCAFFOLD_REQUIRED = (
    "README.md",
    "MASTER_PROMPT.md",
    "WORKFLOW.md",
    "CHAPTER_PLAN.md",
    "SOURCE_MANIFEST.yaml",
    "latex/master.tex",
    "latex/yinqft.sty",
    "latex/chapters/253a/chapter01.tex",
)

SOURCE_PACKET_REQUIRED = (
    "work/pilot/playlist.jsonl",
    "work/pilot/source-map.md",
    "work/pilot/notes-exact.tex",
    "work/pilot/transcript.raw.vtt",
    "work/pilot/transcript.cleaned.jsonl",
    "work/pilot/alignment.jsonl",
    "work/pilot/ambiguities.md",
)

EDITOR_OUTPUT_REQUIRED = (
    "work/pilot/provenance.jsonl",
    "work/pilot/page-dispositions.jsonl",
    "work/pilot/transcript-dispositions.jsonl",
)

REVIEW_REPORTS = (
    "work/pilot/review-math.md",
    "work/pilot/review-fidelity.md",
    "work/pilot/review-render.md",
)

FINAL_REPORT = "work/pilot/report.md"

ALLOWED_SOURCE_CLASSES = frozenset(
    {
        "NOTES_EXACT",
        "SPEECH_CLEAN",
        "SOURCE_COMPOSITE",
        "EQUATION_NORMALIZED",
        "EDITORIAL_NOTE",
        "SOURCE_CONFLICT",
    }
)

EXPECTED_PAGE_PAIRS = {(note_page, note_page + 5) for note_page in range(1, 10)}

TIME_RE = re.compile(
    r"(?P<hours>\d{2,}):(?P<minutes>[0-5]\d):(?P<seconds>[0-5]\d)"
    r"(?:\.(?P<fraction>\d{1,3}))?"
)
TIME_TOKEN_RE = re.compile(
    r"(?<!\d)(\d{2,}:[0-5]\d:[0-5]\d(?:\.\d{1,3})?)(?!\d)"
)
STABLE_ID_RE = re.compile(r"^[A-Za-z][A-Za-z0-9]*(?:[-_.:][A-Za-z0-9]+)*$")
YIN_SOURCE_RE = re.compile(r"^\s*%\s*YIN-SOURCE:\s*(.*?)\s*$")

DISPLAY_ENVIRONMENTS = frozenset(
    {
        "displaymath",
        "equation",
        "equation*",
        "align",
        "align*",
        "alignat",
        "alignat*",
        "flalign",
        "flalign*",
        "gather",
        "gather*",
        "multline",
        "multline*",
        "split",
        "figure",
        "figure*",
        "table",
        "table*",
        "tikzpicture",
    }
)
FIGURE_ENVIRONMENTS = frozenset(
    {"figure", "figure*", "table", "table*", "tikzpicture"}
)
CONTAINER_ENVIRONMENTS = frozenset(
    {
        "document",
        "itemize",
        "enumerate",
        "description",
        "quote",
        "quotation",
        "center",
        "flushleft",
        "flushright",
        "minipage",
        "theorem",
        "lemma",
        "proposition",
        "corollary",
        "definition",
        "remark",
        "proof",
    }
)

STRUCTURAL_LINE_RE = re.compile(
    r"^\\(?:"
    r"YinChapter|chapter|part|section|subsection|subsubsection|paragraph|"
    r"label|index|hypertarget|phantomsection|input|include|"
    r"vspace\*?|hspace\*?|smallskip|medskip|bigskip|newpage|clearpage|"
    r"pagebreak|nopagebreak|linebreak|nolinebreak|goodbreak|smallbreak|bigbreak|"
    r"enlargethispage|needspace|allowdisplaybreaks|displaybreak|"
    r"raggedbottom|flushbottom|sloppy|fussy|"
    r"centering|raggedright|raggedleft|noindent"
    r")\b"
)

HARD_MARKER_RE = re.compile(
    r"\b(?:TODO|VERIFY|UNSUPPORTED|SOURCE_CONFLICT)\b|"
    r"(?i:Status:\s*(?:not started|pending|unfinished|incomplete)|pending source)"
)
UNRESOLVED_VALUE_RE = re.compile(
    r'"(?:review_status|status|disposition)"\s*:\s*'
    r'"(?:unresolved|unsupported|pending|needs[_ -]?review|todo|blocked)"',
    re.IGNORECASE,
)
UNRESOLVED_TEXT_RE = re.compile(
    r"(?:\[\s*UNRESOLVED\s*\]|\bUNRESOLVED\s*:|^\s*#+\s*Unresolved\b)",
    re.IGNORECASE,
)
VERBATIM_BEGIN_RE = re.compile(
    r"^\s*%\s*YIN-VERBATIM-BEGIN\s+(YIN-OY-T\d{6}[AB]?)\s*$"
)
VERBATIM_END_RE = re.compile(
    r"^\s*%\s*YIN-VERBATIM-END\s+(YIN-OY-T\d{6}[AB]?)\s*$"
)
BRACKETED_UNRESOLVED_RE = re.compile(r"\[\s*unresolved\s*\]", re.IGNORECASE)
SAFE_NONE_RE = re.compile(
    r"\bunresolved(?:\s+[A-Za-z_-]+){0,4}\s*:\s*(?:none|0|no)\b",
    re.IGNORECASE,
)

UNRESOLVED_REVIEW_STATUS_RE = re.compile(
    r"(?:unresolved|unsupported|pending|needs[_ -]?review|not[_ -]?reviewed|"
    r"todo|blocked|draft|open)",
    re.IGNORECASE,
)


@dataclass(frozen=True)
class SourceComment:
    line: int
    source_id: str
    source_class: str
    fields: dict[str, str]


class Audit:
    def __init__(self, strict: bool) -> None:
        self.strict = strict
        self.errors: list[str] = []
        self.warnings: list[str] = []
        self.stats: dict[str, int] = {}

    def error(self, message: str) -> None:
        self.errors.append(message)

    def warning(self, message: str) -> None:
        self.warnings.append(message)

    def gate(self, message: str) -> None:
        """A release requirement: error in strict mode, warning in draft."""
        if self.strict:
            self.error(message)
        else:
            self.warning(message)

    def finish(self) -> int:
        for message in self.warnings:
            print(f"WARNING: {message}")
        for message in self.errors:
            print(f"ERROR: {message}", file=sys.stderr)

        mode = "strict" if self.strict else "draft"
        detail = ", ".join(
            f"{name}={value}" for name, value in sorted(self.stats.items())
        )
        if detail:
            detail = f"; {detail}"
        if self.errors:
            print(
                f"Yin pilot {mode} audit failed: {len(self.errors)} error(s), "
                f"{len(self.warnings)} warning(s){detail}",
                file=sys.stderr,
            )
            return 1
        print(
            f"Yin pilot {mode} audit passed: {len(self.warnings)} warning(s){detail}"
        )
        return 0


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def is_nonempty_file(path: Path) -> bool:
    return path.is_file() and path.stat().st_size > 0


def validate_required_files(audit: Audit) -> None:
    for name in SCAFFOLD_REQUIRED:
        path = ROOT / name
        if not is_nonempty_file(path):
            audit.error(f"missing or empty scaffold file: {name}")

    for name in SOURCE_PACKET_REQUIRED:
        path = ROOT / name
        if not is_nonempty_file(path):
            audit.gate(f"missing or empty pilot source-packet file: {name}")

    for name in EDITOR_OUTPUT_REQUIRED:
        path = ROOT / name
        if not is_nonempty_file(path):
            audit.gate(f"missing or empty canonical editor output: {name}")

    for name in REVIEW_REPORTS:
        path = ROOT / name
        if not is_nonempty_file(path):
            audit.gate(f"missing or empty required review report: {name}")

    report = ROOT / FINAL_REPORT
    if not is_nonempty_file(report):
        audit.gate(f"missing or empty pilot report: {FINAL_REPORT}")


def load_jsonl(path: Path, audit: Audit) -> list[tuple[int, dict[str, Any]]]:
    if not path.is_file():
        return []

    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError as exc:
        audit.error(f"{rel(path)} is not valid UTF-8: {exc}")
        return []

    if not text:
        audit.error(f"{rel(path)} is empty")
        return []

    records: list[tuple[int, dict[str, Any]]] = []
    for number, line in enumerate(text.splitlines(), 1):
        if not line.strip():
            audit.error(f"{rel(path)}:{number}: blank lines are not valid JSONL records")
            continue
        try:
            value = json.loads(line)
        except json.JSONDecodeError as exc:
            audit.error(
                f"{rel(path)}:{number}: invalid JSON: {exc.msg} at column {exc.colno}"
            )
            continue
        if not isinstance(value, dict):
            audit.error(f"{rel(path)}:{number}: each JSONL record must be an object")
            continue
        records.append((number, value))
    return records


def load_all_jsonl(audit: Audit) -> dict[Path, list[tuple[int, dict[str, Any]]]]:
    loaded: dict[Path, list[tuple[int, dict[str, Any]]]] = {}
    if not PILOT.is_dir():
        return loaded
    for path in sorted(PILOT.rglob("*.jsonl")):
        loaded[path] = load_jsonl(path, audit)
    audit.stats["jsonl_files"] = len(loaded)
    audit.stats["jsonl_records"] = sum(len(records) for records in loaded.values())
    return loaded


def parse_time(value: Any, context: str, audit: Audit) -> int | None:
    if not isinstance(value, str):
        audit.error(f"{context}: timestamp must be a string")
        return None
    match = TIME_RE.fullmatch(value)
    if match is None:
        audit.error(f"{context}: malformed timestamp {value!r}; expected HH:MM:SS[.mmm]")
        return None
    fraction = (match.group("fraction") or "").ljust(3, "0")
    milliseconds = int(fraction) if fraction else 0
    return (
        int(match.group("hours")) * 3_600_000
        + int(match.group("minutes")) * 60_000
        + int(match.group("seconds")) * 1_000
        + milliseconds
    )


def format_time(milliseconds: int) -> str:
    hours, remainder = divmod(milliseconds, 3_600_000)
    minutes, remainder = divmod(remainder, 60_000)
    seconds, millis = divmod(remainder, 1_000)
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}.{millis:03d}"


def validate_interval_record(
    path: Path,
    number: int,
    record: dict[str, Any],
    audit: Audit,
) -> tuple[int, int] | None:
    has_start = "start" in record
    has_end = "end" in record
    if not has_start and not has_end:
        return None
    if has_start != has_end:
        audit.error(f"{rel(path)}:{number}: interval must contain both start and end")
        return None
    start = parse_time(record["start"], f"{rel(path)}:{number}:start", audit)
    end = parse_time(record["end"], f"{rel(path)}:{number}:end", audit)
    if start is None or end is None:
        return None
    if start >= end:
        audit.error(
            f"{rel(path)}:{number}: malformed interval "
            f"{record['start']!r}--{record['end']!r}; start must precede end"
        )
        return None
    return start, end


def validate_jsonl_intervals(
    loaded: dict[Path, list[tuple[int, dict[str, Any]]]], audit: Audit
) -> None:
    for path, records in loaded.items():
        for number, record in records:
            validate_interval_record(path, number, record, audit)


def record_type(record: dict[str, Any]) -> str:
    value = record.get("record_type", "")
    return value.strip().lower() if isinstance(value, str) else ""


def is_metadata_record(record: dict[str, Any]) -> bool:
    kind = record_type(record)
    return kind == "metadata" or kind.endswith("_metadata")


def extract_single_page(value: Any, kind: str) -> int | None:
    if isinstance(value, list):
        if len(value) != 1:
            return None
        value = value[0]
    if isinstance(value, bool):
        return None
    if isinstance(value, int):
        return value
    if not isinstance(value, str):
        return None
    text = value.strip()
    if kind == "note":
        match = re.fullmatch(r"(?:253a:)?(\d+)", text, re.IGNORECASE)
    else:
        match = re.fullmatch(r"(?:pdf:?)?(\d+)", text, re.IGNORECASE)
    return int(match.group(1)) if match else None


def first_present(record: dict[str, Any], names: Iterable[str]) -> Any:
    for name in names:
        if name in record:
            return record[name]
    return None


def validate_note_source_boundaries(audit: Audit) -> None:
    path = PILOT / "notes-exact.tex"
    if not path.is_file():
        return
    text = path.read_text(encoding="utf-8")
    pairs = [
        (int(note), int(pdf))
        for note, pdf in re.findall(r"\\YinPageBoundary\{(\d+)\}\{(\d+)\}", text)
    ]
    duplicates = sorted({pair for pair in pairs if pairs.count(pair) > 1})
    if duplicates:
        audit.error(f"{rel(path)} has duplicate page boundaries: {duplicates}")
    actual = set(pairs)
    missing = sorted(EXPECTED_PAGE_PAIRS - actual)
    extra = sorted(actual - EXPECTED_PAGE_PAIRS)
    if missing:
        audit.gate(f"{rel(path)} is missing note/PDF page boundaries: {missing}")
    if extra:
        audit.error(f"{rel(path)} has out-of-scope note/PDF page boundaries: {extra}")
    audit.stats["note_boundaries"] = len(actual & EXPECTED_PAGE_PAIRS)


def validate_page_dispositions(
    records: list[tuple[int, dict[str, Any]]], audit: Audit
) -> None:
    path = PILOT / "page-dispositions.jsonl"
    if not path.is_file():
        return

    pairs: list[tuple[int, int]] = []
    ids: dict[str, int] = {}
    for number, record in records:
        if is_metadata_record(record):
            continue
        note_value = first_present(record, ("note_page", "note_pages", "notes"))
        pdf_value = first_present(record, ("pdf_page", "pdf_pages", "pdf"))
        note_page = extract_single_page(note_value, "note")
        pdf_page = extract_single_page(pdf_value, "pdf")
        if note_page is None or pdf_page is None:
            audit.error(
                f"{rel(path)}:{number}: each disposition must name one note page "
                "and one PDF page"
            )
            continue
        disposition = record.get("disposition")
        if not isinstance(disposition, str) or not disposition.strip():
            audit.error(f"{rel(path)}:{number}: missing nonempty disposition")
        source_id = record.get("id")
        if source_id is not None:
            validate_unique_id(source_id, path, number, ids, audit)
        pairs.append((note_page, pdf_page))

    duplicate_pairs = sorted({pair for pair in pairs if pairs.count(pair) > 1})
    if duplicate_pairs:
        audit.error(f"{rel(path)} has duplicate page dispositions: {duplicate_pairs}")
    actual = set(pairs)
    missing = sorted(EXPECTED_PAGE_PAIRS - actual)
    extra = sorted(actual - EXPECTED_PAGE_PAIRS)
    if missing:
        audit.gate(f"{rel(path)} is missing page dispositions: {missing}")
    if extra:
        audit.error(f"{rel(path)} has invalid or out-of-scope page dispositions: {extra}")
    audit.stats["page_dispositions"] = len(actual & EXPECTED_PAGE_PAIRS)


def validate_unique_id(
    value: Any,
    path: Path,
    number: int,
    seen: dict[str, int],
    audit: Audit,
) -> str | None:
    if not isinstance(value, str) or not value.strip():
        audit.error(f"{rel(path)}:{number}: missing stable id")
        return None
    source_id = value.strip()
    if STABLE_ID_RE.fullmatch(source_id) is None:
        audit.error(f"{rel(path)}:{number}: malformed stable id {source_id!r}")
        return None
    if source_id in seen:
        audit.error(
            f"{rel(path)}:{number}: duplicate id {source_id!r}; "
            f"first used on line {seen[source_id]}"
        )
        return None
    seen[source_id] = number
    return source_id


def find_metadata(
    path: Path,
    records: list[tuple[int, dict[str, Any]]],
    kind: str,
    audit: Audit,
) -> tuple[int, dict[str, Any]] | None:
    matches = [(number, record) for number, record in records if record_type(record) == kind]
    if not matches:
        audit.gate(f"{rel(path)} is missing its {kind!r} record")
        return None
    if len(matches) > 1:
        audit.error(f"{rel(path)} contains {len(matches)} {kind!r} records")
    return matches[0]


def extract_source_map_core(audit: Audit) -> tuple[str, str, str] | None:
    path = PILOT / "source-map.md"
    if not path.is_file():
        return None
    text = path.read_text(encoding="utf-8")
    video_match = re.search(
        r"The Chapter 1 lecture is \[`([^`]+)`\]", text, re.IGNORECASE
    )
    core_lines = [
        (number, line)
        for number, line in enumerate(text.splitlines(), 1)
        if "core Chapter 1 transcript interval" in line
    ]
    if not video_match:
        audit.gate(f"{rel(path)} does not state the frozen Chapter 1 video ID")
        return None
    if len(core_lines) != 1:
        audit.gate(
            f"{rel(path)} must contain one frozen core-interval row; found {len(core_lines)}"
        )
        return None
    number, line = core_lines[0]
    times = TIME_TOKEN_RE.findall(line)
    if len(times) != 2:
        audit.error(
            f"{rel(path)}:{number}: frozen core row must contain exactly two timestamps"
        )
        return None
    start = parse_time(times[0], f"{rel(path)}:{number}:core start", audit)
    end = parse_time(times[1], f"{rel(path)}:{number}:core end", audit)
    if start is not None and end is not None and start >= end:
        audit.error(f"{rel(path)}:{number}: frozen core start must precede its end")
    return video_match.group(1), times[0], times[1]


def metadata_core(
    path: Path,
    number: int,
    record: dict[str, Any],
    video_key: str,
    audit: Audit,
) -> tuple[str, str, str, int, int] | None:
    def validate_candidate(
        label: str,
        video: Any,
        start_value: Any,
        end_value: Any,
        duration: Any,
    ) -> tuple[str, str, str, int, int] | None:
        if not isinstance(video, str) or not video.strip():
            audit.error(
                f"{rel(path)}:{number}:{label}: expected a nonempty video ID"
            )
            return None
        start = parse_time(
            start_value, f"{rel(path)}:{number}:{label}.core_start", audit
        )
        end = parse_time(
            end_value, f"{rel(path)}:{number}:{label}.core_end", audit
        )
        if start is None or end is None:
            return None
        if start >= end:
            audit.error(
                f"{rel(path)}:{number}:{label}: core start must precede core end"
            )
            return None
        if duration is not None:
            duration_name = (
                "section_boundaries.core.duration_seconds"
                if label == "schema-v2"
                else "core_duration_seconds"
            )
            if isinstance(duration, bool) or not isinstance(duration, (int, float)):
                audit.error(
                    f"{rel(path)}:{number}:{duration_name} must be numeric"
                )
            elif abs(float(duration) - (end - start) / 1000) > 0.001:
                audit.error(
                    f"{rel(path)}:{number}:{duration_name}={duration} disagrees "
                    f"with timestamps ({(end - start) / 1000:.3f})"
                )
        return video.strip(), str(start_value), str(end_value), start, end

    candidates: list[tuple[str, tuple[str, str, str, int, int]]] = []

    flat_keys = (video_key, "core_start", "core_end")
    flat_present = any(key in record for key in flat_keys)
    if flat_present:
        missing = [key for key in flat_keys if key not in record]
        if missing:
            audit.error(
                f"{rel(path)}:{number}: incomplete legacy core metadata; missing {missing}"
            )
        else:
            flat = validate_candidate(
                "legacy",
                record.get(video_key),
                record.get("core_start"),
                record.get("core_end"),
                record.get("core_duration_seconds"),
            )
            if flat is not None:
                candidates.append(("legacy", flat))

    schema_version = record.get("schema_version")
    nested_present = "matched_video" in record or "section_boundaries" in record
    if nested_present or schema_version == 2:
        matched_video = record.get("matched_video")
        section_boundaries = record.get("section_boundaries")
        if not isinstance(matched_video, dict):
            audit.error(
                f"{rel(path)}:{number}: schema-v2 matched_video must be an object"
            )
            matched_video = {}
        if not isinstance(section_boundaries, dict):
            audit.error(
                f"{rel(path)}:{number}: schema-v2 section_boundaries must be an object"
            )
            section_boundaries = {}
        core = section_boundaries.get("core")
        if not isinstance(core, dict):
            audit.error(
                f"{rel(path)}:{number}: schema-v2 section_boundaries.core "
                "must be an object"
            )
            core = {}
        nested_missing = []
        if "video_id" not in matched_video:
            nested_missing.append("matched_video.video_id")
        if "start" not in core:
            nested_missing.append("section_boundaries.core.start")
        if "end" not in core:
            nested_missing.append("section_boundaries.core.end")
        if nested_missing:
            audit.error(
                f"{rel(path)}:{number}: incomplete schema-v2 core metadata; "
                f"missing {nested_missing}"
            )
        else:
            nested = validate_candidate(
                "schema-v2",
                matched_video.get("video_id"),
                core.get("start"),
                core.get("end"),
                core.get("duration_seconds"),
            )
            if nested is not None:
                candidates.append(("schema-v2", nested))

    if not candidates:
        audit.error(
            f"{rel(path)}:{number}: core metadata contains neither a complete "
            "legacy layout nor a complete schema-v2 layout"
        )
        return None

    baseline_label, baseline = candidates[0]
    for candidate_label, candidate in candidates[1:]:
        if candidate[0] != baseline[0] or candidate[3:] != baseline[3:]:
            audit.error(
                f"{rel(path)}:{number}: {baseline_label} core metadata has "
                f"{baseline[0]} {baseline[1]}--{baseline[2]}, while "
                f"{candidate_label} has {candidate[0]} "
                f"{candidate[1]}--{candidate[2]}"
            )
    return baseline


def validate_source_core(
    loaded: dict[Path, list[tuple[int, dict[str, Any]]]], audit: Audit
) -> tuple[str, int, int] | None:
    alignment_path = PILOT / "alignment.jsonl"
    transcript_path = PILOT / "transcript.cleaned.jsonl"
    alignment_records = loaded.get(alignment_path, [])
    transcript_records = loaded.get(transcript_path, [])

    alignment_meta = find_metadata(
        alignment_path, alignment_records, "alignment_metadata", audit
    ) if alignment_path.is_file() else None
    transcript_meta = find_metadata(
        transcript_path, transcript_records, "transcript_metadata", audit
    ) if transcript_path.is_file() else None

    cores: list[tuple[str, str, str, str, int, int]] = []
    if alignment_meta:
        number, record = alignment_meta
        value = metadata_core(
            alignment_path, number, record, "matched_video_id", audit
        )
        if value:
            video, start_text, end_text, start, end = value
            cores.append(("alignment metadata", video, start_text, end_text, start, end))
    if transcript_meta:
        number, record = transcript_meta
        value = metadata_core(transcript_path, number, record, "video_id", audit)
        if value:
            video, start_text, end_text, start, end = value
            cores.append(("transcript metadata", video, start_text, end_text, start, end))

    source_map = extract_source_map_core(audit)
    if source_map:
        video, start_text, end_text = source_map
        start = parse_time(start_text, "work/pilot/source-map.md:core start", audit)
        end = parse_time(end_text, "work/pilot/source-map.md:core end", audit)
        if start is not None and end is not None:
            cores.append(("source map", video, start_text, end_text, start, end))

    if not cores:
        return None
    baseline = cores[0]
    for candidate in cores[1:]:
        if candidate[1] != baseline[1] or candidate[4:] != baseline[4:]:
            audit.error(
                "frozen core mismatch: "
                f"{baseline[0]} has {baseline[1]} {baseline[2]}--{baseline[3]}, "
                f"while {candidate[0]} has {candidate[1]} "
                f"{candidate[2]}--{candidate[3]}"
            )
    audit.stats["core_metadata_sources"] = len(cores)
    return baseline[1], baseline[4], baseline[5]


def validate_alignment_pages(
    records: list[tuple[int, dict[str, Any]]], audit: Audit
) -> None:
    path = PILOT / "alignment.jsonl"
    if not path.is_file():
        return
    pairs: list[tuple[int, int]] = []
    ids: dict[str, int] = {}
    for number, record in records:
        if record_type(record) != "alignment":
            continue
        note_page = extract_single_page(record.get("note_pages"), "note")
        pdf_page = extract_single_page(record.get("pdf_pages"), "pdf")
        if note_page is None or pdf_page is None:
            audit.error(
                f"{rel(path)}:{number}: pilot alignment must name one note and PDF page"
            )
            continue
        pairs.append((note_page, pdf_page))
        validate_unique_id(record.get("id"), path, number, ids, audit)
    actual = set(pairs)
    missing = sorted(EXPECTED_PAGE_PAIRS - actual)
    extra = sorted(actual - EXPECTED_PAGE_PAIRS)
    if missing:
        audit.gate(f"{rel(path)} is missing pilot page alignments: {missing}")
    if extra:
        audit.error(f"{rel(path)} has out-of-scope pilot page alignments: {extra}")
    if len(pairs) != len(actual):
        audit.error(f"{rel(path)} has duplicate pilot page alignments")
    audit.stats["page_alignments"] = len(actual & EXPECTED_PAGE_PAIRS)


def validate_raw_transcript_hashes(
    loaded: dict[Path, list[tuple[int, dict[str, Any]]]], audit: Audit
) -> None:
    raw_path = PILOT / "transcript.raw.vtt"
    if not raw_path.is_file():
        return
    raw = raw_path.read_bytes()
    if b"-->" not in raw:
        audit.error(f"{rel(raw_path)} contains no VTT timestamp cues")
    digest = hashlib.sha256(raw).hexdigest()
    checked = 0
    for path in (PILOT / "alignment.jsonl", PILOT / "transcript.cleaned.jsonl"):
        for number, record in loaded.get(path, []):
            for key in ("raw_caption_sha256", "raw_vtt_sha256"):
                if key not in record:
                    continue
                checked += 1
                expected = record[key]
                if expected != digest:
                    audit.error(
                        f"{rel(path)}:{number}:{key}={expected!r} does not match "
                        f"{rel(raw_path)} ({digest})"
                    )
            raw_vtt = record.get("raw_vtt")
            if isinstance(raw_vtt, dict) and "sha256" in raw_vtt:
                checked += 1
                expected = raw_vtt["sha256"]
                if expected != digest:
                    audit.error(
                        f"{rel(path)}:{number}:raw_vtt.sha256={expected!r} does "
                        f"not match {rel(raw_path)} ({digest})"
                    )
    if checked == 0:
        audit.gate("no source metadata records the raw transcript SHA-256")
    audit.stats["raw_hash_references"] = checked


def validate_canonical_transcript_hashes(
    loaded: dict[Path, list[tuple[int, dict[str, Any]]]], audit: Audit
) -> None:
    transcript_path = PILOT / "transcript.cleaned.jsonl"
    if not transcript_path.is_file():
        return
    digest = hashlib.sha256(transcript_path.read_bytes()).hexdigest()
    canonical_paths = (
        PILOT / "provenance.jsonl",
        PILOT / "transcript-dispositions.jsonl",
    )
    references = 0
    matches = 0
    for path in canonical_paths:
        stale: dict[str, list[int]] = {}
        malformed: list[int] = []
        for number, record in loaded.get(path, []):
            value = record.get("transcript_sha256")
            if value in (None, ""):
                continue
            references += 1
            if not isinstance(value, str) or re.fullmatch(r"[0-9a-fA-F]{64}", value) is None:
                malformed.append(number)
                continue
            normalized = value.lower()
            if normalized == digest:
                matches += 1
            else:
                stale.setdefault(normalized, []).append(number)
        if malformed:
            sample = ", ".join(str(number) for number in malformed[:8])
            suffix = "..." if len(malformed) > 8 else ""
            audit.error(
                f"{rel(path)} has {len(malformed)} malformed nonempty "
                f"transcript_sha256 value(s), at line(s) {sample}{suffix}"
            )
        for stale_digest, lines in sorted(stale.items()):
            sample = ", ".join(str(number) for number in lines[:8])
            suffix = "..." if len(lines) > 8 else ""
            audit.error(
                f"{rel(path)} has {len(lines)} stale transcript_sha256 value(s) "
                f"at line(s) {sample}{suffix}: {stale_digest}; canonical "
                f"{rel(transcript_path)} is {digest}"
            )
    audit.stats["transcript_hash_matches"] = matches
    audit.stats["transcript_hash_references"] = references


def validate_transcript_dispositions(
    records: list[tuple[int, dict[str, Any]]],
    core: tuple[str, int, int] | None,
    audit: Audit,
) -> None:
    path = PILOT / "transcript-dispositions.jsonl"
    if not path.is_file():
        return

    ids: dict[str, int] = {}
    by_video: dict[str, list[tuple[int, int, int]]] = {}
    for number, record in records:
        if is_metadata_record(record):
            continue
        source_id = validate_unique_id(record.get("id"), path, number, ids, audit)
        video_id = record.get("video_id")
        disposition = record.get("disposition")
        if not isinstance(video_id, str) or not video_id.strip():
            audit.error(f"{rel(path)}:{number}: missing nonempty video_id")
        if not isinstance(disposition, str) or not disposition.strip():
            audit.error(f"{rel(path)}:{number}: missing nonempty disposition")
        interval = validate_interval_record(path, number, record, audit)
        if (
            source_id is not None
            and isinstance(video_id, str)
            and video_id.strip()
            and interval is not None
        ):
            by_video.setdefault(video_id.strip(), []).append(
                (interval[0], interval[1], number)
            )

    for video_id, intervals in by_video.items():
        ordered = sorted(intervals)
        for previous, current in zip(ordered, ordered[1:]):
            if current[0] < previous[1]:
                audit.error(
                    f"{rel(path)}:{current[2]} overlaps line {previous[2]} for "
                    f"video {video_id}: {format_time(current[0])} precedes "
                    f"{format_time(previous[1])}"
                )

    if core is None:
        audit.gate(f"cannot check {rel(path)} coverage without frozen core metadata")
        return
    video_id, core_start, core_end = core
    intervals = sorted(by_video.get(video_id, []))
    if not intervals:
        audit.gate(f"{rel(path)} has no dispositions for frozen video {video_id}")
        return

    gaps: list[tuple[int, int]] = []
    cursor = core_start
    for start, end, _number in intervals:
        if end <= core_start or start >= core_end:
            continue
        clipped_start = max(start, core_start)
        clipped_end = min(end, core_end)
        if clipped_start > cursor:
            gaps.append((cursor, clipped_start))
        cursor = max(cursor, clipped_end)
        if cursor >= core_end:
            break
    if cursor < core_end:
        gaps.append((cursor, core_end))
    if gaps:
        rendered = ", ".join(
            f"{format_time(start)}--{format_time(end)}" for start, end in gaps
        )
        audit.gate(f"{rel(path)} does not cover the frozen core; gaps: {rendered}")
    else:
        audit.stats["transcript_core_covered"] = 1
    audit.stats["transcript_dispositions"] = len(ids)


def strip_tex_comment(line: str) -> str:
    for index, character in enumerate(line):
        if character != "%":
            continue
        backslashes = 0
        cursor = index - 1
        while cursor >= 0 and line[cursor] == "\\":
            backslashes += 1
            cursor -= 1
        if backslashes % 2 == 0:
            return line[:index]
    return line


def parse_source_comment(
    payload: str, path: Path, number: int, audit: Audit
) -> SourceComment | None:
    fields: dict[str, str] = {}
    for field in payload.split(";"):
        field = field.strip()
        if not field:
            continue
        if "=" not in field:
            audit.error(
                f"{rel(path)}:{number}: malformed YIN-SOURCE field {field!r}"
            )
            return None
        key, value = field.split("=", 1)
        key = key.strip().lower()
        value = value.strip()
        if not key or not value:
            audit.error(f"{rel(path)}:{number}: empty YIN-SOURCE key or value")
            return None
        if key in fields:
            audit.error(f"{rel(path)}:{number}: duplicate YIN-SOURCE key {key!r}")
            return None
        fields[key] = value

    missing = sorted({"id", "notes", "pdf", "video", "class"} - fields.keys())
    if missing:
        audit.error(f"{rel(path)}:{number}: YIN-SOURCE comment is missing {missing}")
        return None
    source_id = fields["id"]
    source_class = fields["class"].upper()
    if STABLE_ID_RE.fullmatch(source_id) is None:
        audit.error(f"{rel(path)}:{number}: malformed stable id {source_id!r}")
        return None
    if source_class not in ALLOWED_SOURCE_CLASSES:
        audit.error(
            f"{rel(path)}:{number}: invalid source class {fields['class']!r}; "
            f"allowed: {', '.join(sorted(ALLOWED_SOURCE_CLASSES))}"
        )
        return None
    fields["class"] = source_class
    return SourceComment(number, source_id, source_class, fields)


def begin_environment(line: str) -> str | None:
    match = re.match(r"^\\begin\{([^}]+)\}", line)
    return match.group(1) if match else None


def source_unit_kind(line: str) -> tuple[str, str | None] | None:
    environment = begin_environment(line)
    if environment in DISPLAY_ENVIRONMENTS:
        kind = "figure" if environment in FIGURE_ENVIRONMENTS else "display"
        return kind, environment
    if line.startswith("\\[") or line.startswith("$$"):
        return "display", "\\[" if line.startswith("\\[") else "$$"
    if re.match(r"^\\includegraphics(?:\[[^]]*\])?\{", line):
        return "figure", None
    return None


def is_structural_line(line: str) -> bool:
    environment = begin_environment(line)
    if environment in CONTAINER_ENVIRONMENTS:
        return True
    if line.startswith("\\end{"):
        return True
    if STRUCTURAL_LINE_RE.match(line):
        if line.startswith("\\noindent"):
            return not bool(line[len("\\noindent") :].strip())
        return True
    return False


def scan_chapter_sources(
    path: Path, audit: Audit
) -> tuple[dict[str, SourceComment], set[str]]:
    if not path.is_file():
        return {}, set()
    lines = path.read_text(encoding="utf-8").splitlines()
    comments: dict[str, SourceComment] = {}
    used: set[str] = set()
    pending: SourceComment | None = None
    in_prose = False
    skip_environment: str | None = None
    bracket_display: str | None = None
    list_context: list[bool] = []
    unit_count = 0

    def consume_unit(number: int, kind: str) -> None:
        nonlocal pending, unit_count
        unit_count += 1
        if pending is None:
            audit.gate(
                f"{rel(path)}:{number}: substantive {kind} lacks a preceding "
                "YIN-SOURCE comment"
            )
            return
        used.add(pending.source_id)
        pending = None

    for number, raw_line in enumerate(lines, 1):
        source_match = YIN_SOURCE_RE.match(raw_line)
        if source_match:
            if pending is not None:
                audit.gate(
                    f"{rel(path)}:{pending.line}: YIN-SOURCE {pending.source_id!r} "
                    f"is superseded by another source comment on line {number}"
                )
            parsed = parse_source_comment(source_match.group(1), path, number, audit)
            if parsed is not None:
                if parsed.source_id in comments:
                    audit.error(
                        f"{rel(path)}:{number}: duplicate YIN-SOURCE id "
                        f"{parsed.source_id!r}; first used on line "
                        f"{comments[parsed.source_id].line}"
                    )
                else:
                    comments[parsed.source_id] = parsed
                pending = parsed
            in_prose = False
            continue

        line = strip_tex_comment(raw_line).strip()
        if skip_environment is not None:
            if f"\\end{{{skip_environment}}}" in line:
                skip_environment = None
                in_prose = False
            continue
        if bracket_display is not None:
            closer = "\\]" if bracket_display == "\\[" else "$$"
            if closer in line:
                bracket_display = None
                in_prose = False
            continue
        if not line:
            in_prose = False
            continue

        environment = begin_environment(line)
        if environment in {"itemize", "enumerate", "description"}:
            covered = in_prose or (bool(list_context) and list_context[-1])
            if not covered and pending is not None:
                consume_unit(number, "list")
                covered = True
            list_context.append(covered)
            in_prose = covered
            continue
        if re.match(r"^\\end\{(?:itemize|enumerate|description)\}", line):
            covered = list_context.pop() if list_context else False
            in_prose = covered
            continue

        unit = source_unit_kind(line)
        if unit is not None:
            kind, environment = unit
            consume_unit(number, kind)
            in_prose = False
            if environment in DISPLAY_ENVIRONMENTS:
                if f"\\end{{{environment}}}" not in line:
                    skip_environment = environment
            elif environment in {"\\[", "$$"}:
                closer = "\\]" if environment == "\\[" else "$$"
                if line.count(closer) < 2 if closer == "$$" else closer not in line[2:]:
                    bracket_display = environment
            continue

        if line.startswith("\\item"):
            covered = bool(list_context) and list_context[-1]
            if not covered:
                consume_unit(number, "list")
                if list_context:
                    list_context[-1] = True
            in_prose = True
            continue
        if is_structural_line(line):
            in_prose = False
            continue
        if not in_prose:
            consume_unit(number, "paragraph")
            in_prose = True

    if pending is not None:
        audit.gate(
            f"{rel(path)}:{pending.line}: YIN-SOURCE {pending.source_id!r} is orphaned"
        )
    audit.stats["source_comments"] = len(comments)
    audit.stats["substantive_units"] = unit_count
    audit.stats["sourced_units"] = len(used)
    return comments, used


def normalize_page_values(value: Any, kind: str) -> set[int] | None:
    if value is None:
        return set()
    values = value if isinstance(value, list) else [value]
    result: set[int] = set()
    for item in values:
        page = extract_single_page(item, kind)
        if page is None:
            return None
        result.add(page)
    return result


def parse_comment_page_spec(value: str, kind: str) -> set[int] | None:
    if value.strip().lower() in {"none", "n/a", "na", "-"}:
        return set()
    result: set[int] = set()
    for token in value.split(","):
        token = token.strip()
        if kind == "note":
            token = re.sub(r"^253a:", "", token, flags=re.IGNORECASE)
        else:
            token = re.sub(r"^pdf:?", "", token, flags=re.IGNORECASE)
        match = re.fullmatch(r"(\d+)(?:-(\d+))?", token)
        if not match:
            return None
        start = int(match.group(1))
        end = int(match.group(2) or start)
        if start > end:
            return None
        result.update(range(start, end + 1))
    return result


def parse_comment_video(
    value: str, context: str, audit: Audit
) -> tuple[str | None, int | None, int | None] | None:
    if value.strip().lower() in {"none", "n/a", "na", "-"}:
        return None, None, None
    match = re.match(r"^([^:;\s]+):", value)
    if match is None:
        audit.error(f"{context}: malformed video source {value!r}")
        return None
    video_id = match.group(1)
    time_tokens = TIME_TOKEN_RE.findall(value)
    if len(time_tokens) != 2:
        audit.error(f"{context}: malformed video interval {value!r}")
        return None
    prefix = value[: match.end()]
    interval_text = value[match.end() :]
    expected_interval = re.fullmatch(
        r"\d{2,}:[0-5]\d:[0-5]\d(?:\.\d{1,3})?\s*(?:--|-)\s*"
        r"\d{2,}:[0-5]\d:[0-5]\d(?:\.\d{1,3})?",
        interval_text,
    )
    if expected_interval is None or prefix != f"{video_id}:":
        audit.error(f"{context}: malformed video interval {value!r}")
        return None
    start = parse_time(time_tokens[0], f"{context}:video start", audit)
    end = parse_time(time_tokens[1], f"{context}:video end", audit)
    if start is None or end is None:
        return None
    if start >= end:
        audit.error(f"{context}: video source start must precede its end")
        return None
    return video_id, start, end


def validate_provenance(
    records: list[tuple[int, dict[str, Any]]],
    comments: dict[str, SourceComment],
    audit: Audit,
) -> None:
    path = PILOT / "provenance.jsonl"
    if not path.is_file():
        return

    required_fields = {
        "id",
        "tex_target",
        "unit_type",
        "source_class",
        "note_pages",
        "pdf_pages",
        "video_id",
        "video_start",
        "video_end",
        "source_excerpt",
        "final_text",
        "cleaning_operations",
        "confidence",
        "review_status",
    }
    ids: dict[str, int] = {}
    provenance: dict[str, tuple[int, dict[str, Any]]] = {}
    for number, record in records:
        if is_metadata_record(record):
            continue
        missing = sorted(required_fields - record.keys())
        if missing:
            audit.gate(f"{rel(path)}:{number}: provenance record is missing {missing}")
        source_id = validate_unique_id(record.get("id"), path, number, ids, audit)
        if source_id is None:
            continue
        provenance[source_id] = (number, record)

        source_class = record.get("source_class")
        if not isinstance(source_class, str) or source_class.upper() not in ALLOWED_SOURCE_CLASSES:
            audit.error(
                f"{rel(path)}:{number}: invalid source_class {source_class!r}; "
                f"allowed: {', '.join(sorted(ALLOWED_SOURCE_CLASSES))}"
            )

        status = record.get("review_status")
        if not isinstance(status, str) or not status.strip():
            audit.gate(f"{rel(path)}:{number}: missing provenance review_status")
        elif UNRESOLVED_REVIEW_STATUS_RE.search(status):
            audit.gate(
                f"{rel(path)}:{number}: unresolved provenance review_status "
                f"{status!r} for {source_id}"
            )

        has_video = any(record.get(key) not in (None, "", "none", "n/a") for key in (
            "video_id", "video_start", "video_end"
        ))
        if has_video:
            if not isinstance(record.get("video_id"), str) or not record["video_id"].strip():
                audit.error(f"{rel(path)}:{number}: video interval lacks video_id")
            start = parse_time(
                record.get("video_start"), f"{rel(path)}:{number}:video_start", audit
            )
            end = parse_time(
                record.get("video_end"), f"{rel(path)}:{number}:video_end", audit
            )
            if start is not None and end is not None and start >= end:
                audit.error(f"{rel(path)}:{number}: video_start must precede video_end")

        note_pages = normalize_page_values(record.get("note_pages"), "note")
        pdf_pages = normalize_page_values(record.get("pdf_pages"), "pdf")
        if note_pages is None:
            audit.error(f"{rel(path)}:{number}: malformed note_pages")
        if pdf_pages is None:
            audit.error(f"{rel(path)}:{number}: malformed pdf_pages")
        if note_pages is not None and pdf_pages is not None and note_pages and pdf_pages:
            expected_pdf = {page + 5 for page in note_pages}
            if pdf_pages != expected_pdf:
                audit.error(
                    f"{rel(path)}:{number}: note_pages {sorted(note_pages)} do not map "
                    f"to pdf_pages {sorted(pdf_pages)}"
                )

    tex_ids = set(comments)
    provenance_ids = set(provenance)
    missing_records = sorted(tex_ids - provenance_ids)
    orphan_records = sorted(provenance_ids - tex_ids)
    if missing_records:
        audit.gate(f"provenance.jsonl lacks TeX source IDs: {missing_records}")
    if orphan_records:
        audit.gate(f"provenance.jsonl has IDs absent from TeX: {orphan_records}")

    for source_id in sorted(tex_ids & provenance_ids):
        comment = comments[source_id]
        number, record = provenance[source_id]
        source_class = record.get("source_class")
        if isinstance(source_class, str) and source_class.upper() != comment.source_class:
            audit.error(
                f"source class mismatch for {source_id}: TeX line {comment.line} has "
                f"{comment.source_class}, provenance line {number} has {source_class}"
            )

        comment_notes = parse_comment_page_spec(comment.fields["notes"], "note")
        comment_pdfs = parse_comment_page_spec(comment.fields["pdf"], "pdf")
        provenance_notes = normalize_page_values(record.get("note_pages"), "note")
        provenance_pdfs = normalize_page_values(record.get("pdf_pages"), "pdf")
        if comment_notes is None:
            audit.error(
                f"{rel(CHAPTER)}:{comment.line}: malformed notes page specification"
            )
        elif provenance_notes is not None and comment_notes != provenance_notes:
            audit.error(
                f"page mismatch for {source_id}: TeX notes={comment.fields['notes']!r}, "
                f"provenance note_pages={record.get('note_pages')!r}"
            )
        if comment_pdfs is None:
            audit.error(
                f"{rel(CHAPTER)}:{comment.line}: malformed PDF page specification"
            )
        elif provenance_pdfs is not None and comment_pdfs != provenance_pdfs:
            audit.error(
                f"page mismatch for {source_id}: TeX pdf={comment.fields['pdf']!r}, "
                f"provenance pdf_pages={record.get('pdf_pages')!r}"
            )

        comment_video = parse_comment_video(
            comment.fields["video"],
            f"{rel(CHAPTER)}:{comment.line}",
            audit,
        )
        if comment_video is not None:
            comment_video_id, comment_start, comment_end = comment_video
            provenance_video_id = record.get("video_id")
            if comment_video_id != provenance_video_id:
                audit.error(
                    f"video mismatch for {source_id}: TeX has {comment_video_id!r}, "
                    f"provenance has {provenance_video_id!r}"
                )
            if comment_start is not None and comment_end is not None:
                provenance_start = parse_time(
                    record.get("video_start"),
                    f"{rel(path)}:{number}:video_start",
                    audit,
                )
                provenance_end = parse_time(
                    record.get("video_end"),
                    f"{rel(path)}:{number}:video_end",
                    audit,
                )
                if (provenance_start, provenance_end) != (comment_start, comment_end):
                    audit.error(
                        f"video interval mismatch for {source_id}: TeX has "
                        f"{comment.fields['video']!r}, provenance has "
                        f"{record.get('video_start')!r}--{record.get('video_end')!r}"
                    )

    audit.stats["provenance_records"] = len(provenance)


def line_has_unfinished_marker(line: str) -> bool:
    if HARD_MARKER_RE.search(line) or UNRESOLVED_VALUE_RE.search(line):
        return True
    if UNRESOLVED_TEXT_RE.search(line) and not SAFE_NONE_RE.search(line):
        return True
    return False


def valid_verbatim_line_records(lines: list[str]) -> dict[int, str]:
    """Map body lines only for closed, exactly matched verbatim blocks."""
    mapped: dict[int, str] = {}
    open_id: str | None = None
    body_lines: list[int] = []
    valid = True

    for number, line in enumerate(lines, 1):
        stripped = line.rstrip("\r\n")
        begin = VERBATIM_BEGIN_RE.fullmatch(stripped)
        end = VERBATIM_END_RE.fullmatch(stripped)
        if begin is not None:
            if open_id is not None:
                valid = False
            else:
                open_id = begin.group(1)
                body_lines = []
                valid = True
            continue
        if end is not None:
            if open_id is not None and valid and end.group(1) == open_id:
                mapped.update({line_number: open_id for line_number in body_lines})
            open_id = None
            body_lines = []
            valid = True
            continue
        if open_id is not None:
            body_lines.append(number)
    return mapped


def logged_unresolved_allowances(
    omission_rows: list[tuple[int, dict[str, Any]]],
) -> dict[str, int]:
    allowances: dict[str, int] = {}
    for _number, record in omission_rows:
        if record.get("record_type") != "span_omission":
            continue
        if record.get("scope") != "prebaseline_uncertainty":
            continue
        if record.get("reason_code") != "uncertain_or_sense_gloss_span":
            continue
        omitted_text = record.get("omitted_text")
        record_id = record.get("transcript_record_id")
        if not isinstance(omitted_text, str) or not isinstance(record_id, str):
            continue
        marker_text = omitted_text.strip()
        if marker_text.startswith("[") and marker_text.endswith("]"):
            marker_text = marker_text[1:-1].strip()
        if marker_text.casefold() != "unresolved":
            continue
        allowances[record_id] = allowances.get(record_id, 0) + 1
    return allowances


def chapter_unfinished_marker_hits(
    lines: list[str],
    omission_rows: list[tuple[int, dict[str, Any]]],
) -> list[tuple[int, str]]:
    line_records = valid_verbatim_line_records(lines)
    allowances = logged_unresolved_allowances(omission_rows)
    hits: list[tuple[int, str]] = []

    for number, line in enumerate(lines, 1):
        record_id = line_records.get(number)
        scan_line = line
        if record_id is not None and allowances.get(record_id, 0) > 0:
            remaining = allowances[record_id]

            def remove_logged_marker(match: re.Match[str]) -> str:
                nonlocal remaining
                if remaining <= 0:
                    return match.group(0)
                remaining -= 1
                return " "

            scan_line = BRACKETED_UNRESOLVED_RE.sub(remove_logged_marker, scan_line)
            allowances[record_id] = remaining
        if line_has_unfinished_marker(scan_line):
            hits.append((number, line))
    return hits


def validate_unfinished_marker_fixtures(audit: Audit) -> None:
    approved_one = "YIN-OY-T000001"
    unlogged = "YIN-OY-T000002"
    approved_hard = "YIN-OY-T000003"
    underlogged = "YIN-OY-T000004"
    lines = [
        f"% YIN-VERBATIM-BEGIN {approved_one}",
        r"\noindent [unresolved] source-faithful text.\par",
        f"% YIN-VERBATIM-END {approved_one}",
        f"% YIN-VERBATIM-BEGIN {unlogged}",
        r"\noindent [unresolved] unlogged text.\par",
        f"% YIN-VERBATIM-END {unlogged}",
        f"% YIN-VERBATIM-BEGIN {approved_hard}",
        r"\noindent [unresolved] TODO\par",
        f"% YIN-VERBATIM-END {approved_hard}",
        r"\noindent [unresolved] outside a block.\par",
        f"% YIN-VERBATIM-BEGIN {underlogged}",
        r"\noindent [unresolved] and [unresolved].\par",
        f"% YIN-VERBATIM-END {underlogged}",
    ]
    omission_rows = [
        (
            1,
            {
                "record_type": "span_omission",
                "transcript_record_id": approved_one,
                "scope": "prebaseline_uncertainty",
                "omitted_text": "unresolved",
                "reason_code": "uncertain_or_sense_gloss_span",
            },
        ),
        (
            2,
            {
                "record_type": "span_omission",
                "transcript_record_id": approved_hard,
                "scope": "prebaseline_uncertainty",
                "omitted_text": "unresolved",
                "reason_code": "uncertain_or_sense_gloss_span",
            },
        ),
        (
            3,
            {
                "record_type": "span_omission",
                "transcript_record_id": underlogged,
                "scope": "prebaseline_uncertainty",
                "omitted_text": "unresolved",
                "reason_code": "uncertain_or_sense_gloss_span",
            },
        ),
    ]
    observed = [
        number for number, _line in chapter_unfinished_marker_hits(lines, omission_rows)
    ]
    expected = [5, 8, 10, 12]
    if observed != expected:
        audit.error(
            "unfinished-marker regression failed: "
            f"expected hit lines {expected}, found {observed}"
        )
    audit.stats["unfinished_marker_fixtures"] = len(expected)


def validate_unfinished_markers(
    loaded: dict[Path, list[tuple[int, dict[str, Any]]]], audit: Audit
) -> None:
    validate_unfinished_marker_fixtures(audit)
    hits: list[str] = []
    if CHAPTER.is_file():
        chapter_lines = CHAPTER.read_text(encoding="utf-8").splitlines()
        omission_path = PILOT / "verbatim-omissions.jsonl"
        for number, line in chapter_unfinished_marker_hits(
            chapter_lines, loaded.get(omission_path, [])
        ):
            hits.append(f"{rel(CHAPTER)}:{number}:{line.strip()}")

    canonical_paths = (
        PILOT / "provenance.jsonl",
        PILOT / "page-dispositions.jsonl",
        PILOT / "transcript-dispositions.jsonl",
    )
    unresolved_values = re.compile(
        r"(?:unresolved|unsupported|pending|needs[_ -]?review|not[_ -]?reviewed|"
        r"todo|blocked|draft|open)",
        re.IGNORECASE,
    )
    for path in canonical_paths:
        for number, record in loaded.get(path, []):
            source_class = record.get("source_class")
            if isinstance(source_class, str) and source_class.upper() == "SOURCE_CONFLICT":
                hits.append(f"{rel(path)}:{number}:source_class=SOURCE_CONFLICT")
            for key in ("review_status", "status", "disposition"):
                value = record.get(key)
                if isinstance(value, str) and unresolved_values.search(value):
                    hits.append(f"{rel(path)}:{number}:{key}={value}")
            final_text = record.get("final_text")
            if isinstance(final_text, str) and line_has_unfinished_marker(final_text):
                hits.append(f"{rel(path)}:{number}:final_text contains a marker")
            if record.get("unsupported") is True:
                hits.append(f"{rel(path)}:{number}:unsupported=true")
    for hit in hits:
        audit.gate(f"unfinished or unsupported marker: {hit}")
    audit.stats["unfinished_markers"] = len(hits)


def review_has_clear_attestation(text: str) -> bool:
    patterns = (
        r"(?:unresolved\s+)?blockers?\s*(?::|=|\n)\s*(?:none|0|no\b|clear\b)",
        r"blockers?\s+(?:found\s*)?(?::|=)?\s*0\b",
        r"(?:review\s+)?status\s*:\s*(?:pass(?:ed)?|approved|clear|complete)\b",
    )
    return any(re.search(pattern, text, re.IGNORECASE) for pattern in patterns)


def review_has_explicit_blocker(text: str) -> bool:
    if re.search(r"\[\s*BLOCKER\s*\]", text, re.IGNORECASE):
        return True
    if re.search(r"(?:review\s+)?status\s*:\s*(?:fail(?:ed)?|blocked)\b", text, re.IGNORECASE):
        return True
    for line in text.splitlines():
        match = re.search(r"(?:unresolved\s+)?blockers?\s*:\s*(.+)", line, re.IGNORECASE)
        if match and not re.match(r"(?:none|0|no\b|clear\b|resolved\b)", match.group(1).strip(), re.IGNORECASE):
            return True
    return False


def validate_review_reports(audit: Audit) -> None:
    clear = 0
    for name in REVIEW_REPORTS:
        path = ROOT / name
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        if review_has_explicit_blocker(text):
            audit.gate(f"{name} declares an unresolved blocker")
        elif not review_has_clear_attestation(text):
            audit.gate(
                f"{name} lacks an explicit no-blockers attestation "
                "(for example, 'Unresolved blockers: none')"
            )
        else:
            clear += 1
    audit.stats["clear_review_reports"] = clear


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--strict", action="store_true")
    strict = parser.parse_args().strict
    audit = Audit(strict)

    validate_required_files(audit)
    loaded = load_all_jsonl(audit)
    validate_jsonl_intervals(loaded, audit)
    validate_note_source_boundaries(audit)

    alignment_path = PILOT / "alignment.jsonl"
    validate_alignment_pages(loaded.get(alignment_path, []), audit)
    core = validate_source_core(loaded, audit)
    validate_raw_transcript_hashes(loaded, audit)
    validate_canonical_transcript_hashes(loaded, audit)

    page_dispositions_path = PILOT / "page-dispositions.jsonl"
    validate_page_dispositions(loaded.get(page_dispositions_path, []), audit)

    transcript_dispositions_path = PILOT / "transcript-dispositions.jsonl"
    validate_transcript_dispositions(
        loaded.get(transcript_dispositions_path, []), core, audit
    )

    comments, _used = scan_chapter_sources(CHAPTER, audit)
    provenance_path = PILOT / "provenance.jsonl"
    validate_provenance(loaded.get(provenance_path, []), comments, audit)

    verbatim = run_verbatim_audit(ROOT, strict=strict)
    audit.errors.extend(f"near-verbatim: {message}" for message in verbatim.errors)
    audit.warnings.extend(
        f"near-verbatim: {message}" for message in verbatim.warnings
    )
    for name, value in verbatim.stats.items():
        if name == "transcript_sha256":
            continue
        stat_name = name if name.startswith("verbatim_") else f"verbatim_{name}"
        audit.stats[stat_name] = value

    validate_unfinished_markers(loaded, audit)
    validate_review_reports(audit)
    return audit.finish()


if __name__ == "__main__":
    raise SystemExit(main())
