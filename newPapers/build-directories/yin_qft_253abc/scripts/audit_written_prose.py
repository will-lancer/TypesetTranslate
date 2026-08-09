#!/usr/bin/env python3
"""Audit the Yin chapter as written exposition rather than retained speech.

The transcript remains a frozen evidence layer.  This audit checks source-span
coverage, the argument map, the six-pass ledger, deliberate conversational
phrases, TeX hygiene, and equation placement.  It never scores lexical overlap
with the transcript.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass, field
import hashlib
import json
from pathlib import Path
import re
import sys
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
PILOT = ROOT / "work" / "pilot"
CHAPTER = ROOT / "latex" / "chapters" / "253a" / "chapter01.tex"
STYLE = ROOT / "WRITING_STYLE.md"
PASS_LEDGER = PILOT / "writing-style-pass-ledger.md"
STYLE_EXCEPTIONS = PILOT / "style-exceptions.jsonl"
ARGUMENT_MAP = PILOT / "argument-map.jsonl"
VOICE_RESTORATION = PILOT / "voice-restoration.jsonl"
TRANSCRIPT = PILOT / "transcript.cleaned.jsonl"
DISPOSITIONS = PILOT / "transcript-dispositions.jsonl"

SPEECH_BEGIN_RE = re.compile(
    r"^\s*%\s*YIN-SPEECH-BEGIN\s+(YIN-OY-T\d{6}[AB]?)\s*$"
)
SPEECH_END_RE = re.compile(
    r"^\s*%\s*YIN-SPEECH-END\s+(YIN-OY-T\d{6}[AB]?)\s*$"
)
LEGACY_MARKER_RE = re.compile(r"YIN-VERBATIM-(?:BEGIN|END)")

HIDDEN_TEX_RE = re.compile(
    r"\\(?:llap|rlap|clap|phantom|hphantom|vphantom|smash)\b"
)
READER_UNCERTAINTY_RE = re.compile(
    r"\[(?:unclear|inaudible|unresolved|likely|uncertain)(?:[^]]*)\]",
    re.IGNORECASE,
)
HARD_FILLER_PATTERNS = {
    "okay": re.compile(r"\bokay\b", re.IGNORECASE),
    "all right": re.compile(r"\ball\s+right\b", re.IGNORECASE),
    "you know": re.compile(r"\byou\s+know\b", re.IGNORECASE),
    "sort of": re.compile(r"\bsort\s+of\b", re.IGNORECASE),
    "isolated uh": re.compile(r"\buh\b", re.IGNORECASE),
    "isolated um": re.compile(r"\bum\b", re.IGNORECASE),
    "question invitation": re.compile(
        r"\b(?:any|other)\s+questions?(?:\s+so\s+far)?\b", re.IGNORECASE
    ),
    "board instruction": re.compile(
        r"\b(?:take\s+(?:a|one|two|couple)\s+minutes?|"
        r"let\s+me\s+(?:write|draw)|I(?:'m|\s+am)\s+going\s+to\s+write|"
        r"write\s+down\s+this\s+line|on\s+the\s+board)\b",
        re.IGNORECASE,
    ),
}

REVIEW_PATTERNS = {
    "basically": re.compile(r"(?P<phrase>\bbasically\b)", re.IGNORECASE),
    "kind_of": re.compile(r"(?P<phrase>\bkind\s+of\b)", re.IGNORECASE),
    "i_mean": re.compile(r"(?P<phrase>\bI\s+mean\b)"),
    "just": re.compile(r"(?P<phrase>\bjust\b)", re.IGNORECASE),
    "let_me": re.compile(r"(?P<phrase>\blet\s+me\b)", re.IGNORECASE),
    "for_the_moment": re.compile(
        r"(?P<phrase>\bfor\s+the\s+moment\b)", re.IGNORECASE
    ),
    "sentence_initial_so": re.compile(
        r"(?P<phrase>\bSo(?:,|\s))"
    ),
    "sentence_initial_now": re.compile(
        r"(?P<phrase>\bNow(?:,|\s))"
    ),
}

DISPLAY_ENVS = (
    "equation",
    "equation*",
    "align",
    "align*",
    "alignat",
    "alignat*",
    "gather",
    "gather*",
    "multline",
    "multline*",
    "displaymath",
    "figure",
    "figure*",
    "tikzpicture",
    "table",
    "table*",
)

REQUIRED_PASSES = (
    "structure",
    "filler",
    "voice restoration",
    "logic and referents",
    "mathematics and notation",
    "build and render",
)

ACTIVE_CHAPTER_USES = frozenset(
    {
        "included",
        "included_clear_portion_uncertainty_excluded",
        "merged_into_preceding_written_answer",
    }
)
INACTIVE_CHAPTER_USES = frozenset(
    {
        "classroom_management_excluded",
        "classroom_setup_or_logistics_excluded",
        "coverage_only",
        "logistics_or_nonspeech_excluded",
        "optional_lead_in_excluded",
        "outside_section",
        "repetition_excluded",
        "repetition_or_context_excluded",
        "unresolved_excluded",
    }
)


@dataclass
class Result:
    strict: bool
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    stats: dict[str, Any] = field(default_factory=dict)

    def error(self, message: str) -> None:
        self.errors.append(message)

    def gate(self, message: str) -> None:
        if self.strict:
            self.errors.append(message)
        else:
            self.warnings.append(message)

    @property
    def exit_code(self) -> int:
        return 1 if self.errors else 0


def relative(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def load_jsonl(path: Path, result: Result) -> list[tuple[int, dict[str, Any]]]:
    if not path.is_file():
        result.gate(f"missing required written-prose artifact: {relative(path)}")
        return []
    rows: list[tuple[int, dict[str, Any]]] = []
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            result.error(f"{relative(path)}:{number}: blank JSONL line")
            continue
        try:
            value = json.loads(line)
        except json.JSONDecodeError as exc:
            result.error(
                f"{relative(path)}:{number}: invalid JSON at column {exc.colno}: "
                f"{exc.msg}"
            )
            continue
        if not isinstance(value, dict):
            result.error(f"{relative(path)}:{number}: JSONL row must be an object")
            continue
        rows.append((number, value))
    return rows


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


def visible_tex(text: str) -> str:
    return "\n".join(strip_tex_comment(line) for line in text.splitlines())


def remove_display_regions(text: str) -> str:
    for environment in DISPLAY_ENVS:
        escaped = re.escape(environment)
        text = re.sub(
            rf"\\begin\{{{escaped}\}}.*?\\end\{{{escaped}\}}",
            " ",
            text,
            flags=re.DOTALL,
        )
    text = re.sub(r"\\\[.*?\\\]", " ", text, flags=re.DOTALL)
    text = re.sub(r"\$\$.*?\$\$", " ", text, flags=re.DOTALL)
    return text


def oversized_inline_formulas(text: str) -> tuple[list[str], int]:
    inline_source = remove_display_regions(text)
    inline_math: list[str] = []
    inline_math.extend(
        match.group(1)
        for match in re.finditer(
            r"(?<!\$)\$(?!\$)(.+?)(?<!\$)\$(?!\$)", inline_source, re.DOTALL
        )
    )
    inline_math.extend(
        match.group(1)
        for match in re.finditer(r"\\\((.+?)\\\)", inline_source, re.DOTALL)
    )
    oversized: list[str] = []
    for formula in inline_math:
        compact = " ".join(formula.split())
        if len(compact) > 60 or re.search(r"\\(?:int|sum|prod)\b", compact):
            oversized.append(compact)
    return oversized, len(inline_math)


def parse_speech_blocks(
    lines: list[str], result: Result
) -> tuple[list[str], dict[str, tuple[int, int]]]:
    order: list[str] = []
    blocks: dict[str, tuple[int, int]] = {}
    open_id: str | None = None
    open_line = 0
    for number, line in enumerate(lines, 1):
        begin = SPEECH_BEGIN_RE.fullmatch(line)
        end = SPEECH_END_RE.fullmatch(line)
        if begin:
            record_id = begin.group(1)
            if open_id is not None:
                result.error(
                    f"{relative(CHAPTER)}:{number}: nested speech span {record_id} "
                    f"inside {open_id}"
                )
                continue
            if record_id in blocks or record_id in order:
                result.error(
                    f"{relative(CHAPTER)}:{number}: duplicate speech span {record_id}"
                )
            open_id = record_id
            open_line = number
            order.append(record_id)
            continue
        if end:
            record_id = end.group(1)
            if open_id is None:
                result.error(
                    f"{relative(CHAPTER)}:{number}: orphan speech end {record_id}"
                )
            elif record_id != open_id:
                result.error(
                    f"{relative(CHAPTER)}:{number}: speech end {record_id} does "
                    f"not match open span {open_id}"
                )
                open_id = None
            else:
                blocks[record_id] = (open_line, number)
                open_id = None
    if open_id is not None:
        result.error(
            f"{relative(CHAPTER)}:{open_line}: unclosed speech span {open_id}"
        )
    result.stats["speech_spans"] = len(blocks)
    return order, blocks


def validate_source_coverage(
    order: list[str], blocks: dict[str, tuple[int, int]], result: Result
) -> None:
    transcript_rows = load_jsonl(TRANSCRIPT, result)
    transcript_order: list[str] = []
    transcript_ids: set[str] = set()
    for _number, row in transcript_rows:
        if row.get("record_type") == "transcript_metadata":
            continue
        record_id = row.get("id")
        if isinstance(record_id, str):
            transcript_order.append(record_id)
            transcript_ids.add(record_id)

    unknown = sorted(set(blocks) - transcript_ids)
    if unknown:
        result.error(f"speech spans absent from the canonical transcript: {unknown}")

    positions = {record_id: index for index, record_id in enumerate(transcript_order)}
    observed_positions = [positions[record_id] for record_id in order if record_id in positions]
    if observed_positions != sorted(observed_positions):
        result.error("speech spans are not in canonical transcript order")

    disposition_rows = load_jsonl(DISPOSITIONS, result)
    dispositions: dict[str, dict[str, Any]] = {}
    for number, row in disposition_rows:
        record_id = row.get("transcript_record_id")
        if not isinstance(record_id, str):
            result.error(
                f"{relative(DISPOSITIONS)}:{number}: missing transcript_record_id"
            )
            continue
        dispositions[record_id] = row

    missing_dispositions = sorted(set(blocks) - set(dispositions))
    if missing_dispositions:
        result.error(
            "speech spans lack written-use dispositions: "
            f"{missing_dispositions}"
        )

    expected: set[str] = set()
    chapter_source_ids = set(
        re.findall(
            r"(?m)^\s*%\s*YIN-SOURCE:\s*id=([^;\s]+)",
            CHAPTER.read_text(encoding="utf-8"),
        )
    )
    chapter_hash = hashlib.sha256(CHAPTER.read_bytes()).hexdigest()
    for record_id, row in dispositions.items():
        chapter_use = row.get("chapter_use")
        if chapter_use in ACTIVE_CHAPTER_USES:
            expected.add(record_id)
        elif chapter_use not in INACTIVE_CHAPTER_USES:
            result.error(
                f"unknown chapter_use {chapter_use!r} for transcript record {record_id}"
            )
        links = row.get("included_unit_ids")
        if not isinstance(links, list):
            result.error(f"transcript record {record_id} has malformed included_unit_ids")
            links = []
        stale = [link for link in links if link not in chapter_source_ids]
        if stale:
            result.error(
                f"transcript record {record_id} links to absent chapter units: {stale}"
            )
        if chapter_use in ACTIVE_CHAPTER_USES:
            expected_source_id = "YIN253A-C01-V-" + record_id.removeprefix("YIN-OY-")
            if expected_source_id not in links:
                result.error(
                    f"active transcript record {record_id} lacks its current source "
                    f"link {expected_source_id}"
                )
        if row.get("chapter_sha256") != chapter_hash:
            result.gate(
                f"transcript disposition for {record_id} has a stale chapter_sha256"
            )
    missing_spans = sorted(expected - set(blocks))
    if missing_spans:
        result.gate(
            "written-use dispositions require missing speech spans: "
            f"{missing_spans}"
        )

    result.stats["speech_spans_with_dispositions"] = len(set(blocks) & set(dispositions))
    result.stats["active_transcript_dispositions"] = len(expected)


def validate_argument_map(result: Result) -> None:
    rows = load_jsonl(ARGUMENT_MAP, result)
    transcript_rows = load_jsonl(TRANSCRIPT, result)
    transcript_order = [
        row.get("id")
        for _number, row in transcript_rows
        if row.get("record_type") != "transcript_metadata"
        and isinstance(row.get("id"), str)
    ]
    positions = {record_id: index for index, record_id in enumerate(transcript_order)}
    required = {
        "id",
        "source_order",
        "title",
        "transcript_start_id",
        "transcript_end_id",
        "note_pages",
        "pdf_pages",
        "claims",
        "equation_source_ids",
        "voice_cues",
        "paragraph_plan",
        "status",
    }
    ids: set[str] = set()
    orders: list[int] = []
    previous_end = -1
    for number, row in rows:
        missing = sorted(required - set(row))
        if missing:
            result.gate(
                f"{relative(ARGUMENT_MAP)}:{number}: missing fields {missing}"
            )
        record_id = row.get("id")
        if not isinstance(record_id, str) or not record_id:
            result.error(f"{relative(ARGUMENT_MAP)}:{number}: missing id")
        elif record_id in ids:
            result.error(f"{relative(ARGUMENT_MAP)}:{number}: duplicate id {record_id}")
        else:
            ids.add(record_id)
        source_order = row.get("source_order")
        if not isinstance(source_order, int):
            result.error(
                f"{relative(ARGUMENT_MAP)}:{number}: source_order must be an integer"
            )
        else:
            orders.append(source_order)
        start_id = row.get("transcript_start_id")
        end_id = row.get("transcript_end_id")
        if start_id not in positions or end_id not in positions:
            result.error(
                f"{relative(ARGUMENT_MAP)}:{number}: transcript range is absent "
                "from the canonical transcript"
            )
        elif positions[start_id] > positions[end_id]:
            result.error(
                f"{relative(ARGUMENT_MAP)}:{number}: reversed transcript range"
            )
        elif positions[start_id] <= previous_end:
            result.error(
                f"{relative(ARGUMENT_MAP)}:{number}: argument ranges overlap or "
                "leave source order"
            )
        else:
            previous_end = positions[end_id]
        for key in ("claims", "voice_cues", "paragraph_plan"):
            value = row.get(key)
            if not isinstance(value, list) or not value:
                result.gate(
                    f"{relative(ARGUMENT_MAP)}:{number}: {key} must be nonempty"
                )
        if row.get("status") != "approved_for_drafting":
            result.gate(
                f"{relative(ARGUMENT_MAP)}:{number}: status is not "
                "approved_for_drafting"
            )
    if orders and sorted(orders) != list(range(1, len(orders) + 1)):
        result.error("argument-map source_order values must be contiguous from 1")
    result.stats["argument_units"] = len(rows)


def validate_voice_restoration(chapter_text: str, result: Result) -> None:
    argument_rows = load_jsonl(ARGUMENT_MAP, result)
    transcript_rows = load_jsonl(TRANSCRIPT, result)
    voice_rows = load_jsonl(VOICE_RESTORATION, result)

    arguments: dict[str, dict[str, Any]] = {}
    required_cues: set[tuple[str, str]] = set()
    for number, row in argument_rows:
        argument_id = row.get("id")
        cues = row.get("voice_cues")
        if not isinstance(argument_id, str) or not argument_id:
            continue
        arguments[argument_id] = row
        if not isinstance(cues, list):
            continue
        for cue in cues:
            if not isinstance(cue, str) or not cue.strip():
                result.error(
                    f"{relative(ARGUMENT_MAP)}:{number}: voice cue must be nonempty"
                )
                continue
            required_cues.add((argument_id, cue))

    transcript: dict[str, dict[str, Any]] = {}
    transcript_order: list[str] = []
    for _number, row in transcript_rows:
        if row.get("record_type") == "transcript_metadata":
            continue
        record_id = row.get("id")
        if isinstance(record_id, str):
            transcript[record_id] = row
            transcript_order.append(record_id)
    positions = {record_id: index for index, record_id in enumerate(transcript_order)}

    visible = visible_tex(chapter_text)
    normalized_visible = " ".join(visible.split())
    chapter_hash = hashlib.sha256(chapter_text.encode("utf-8")).hexdigest()
    required_fields = {
        "id",
        "argument_unit_id",
        "cue",
        "source_record_ids",
        "source_text",
        "treatment",
        "final_text",
        "voice_function",
        "reason",
        "status",
        "chapter_sha256",
    }
    allowed_treatments = {"retained_exact", "lightly_recast"}
    seen_ids: set[str] = set()
    covered_cues: set[tuple[str, str]] = set()
    for number, row in voice_rows:
        missing = sorted(required_fields - set(row))
        if missing:
            result.error(
                f"{relative(VOICE_RESTORATION)}:{number}: missing fields {missing}"
            )
            continue
        record_id = row.get("id")
        if not isinstance(record_id, str) or not record_id:
            result.error(f"{relative(VOICE_RESTORATION)}:{number}: missing id")
        elif record_id in seen_ids:
            result.error(
                f"{relative(VOICE_RESTORATION)}:{number}: duplicate id {record_id}"
            )
        else:
            seen_ids.add(record_id)

        argument_id = row.get("argument_unit_id")
        cue = row.get("cue")
        if argument_id not in arguments:
            result.error(
                f"{relative(VOICE_RESTORATION)}:{number}: unknown argument unit "
                f"{argument_id!r}"
            )
            continue
        if not isinstance(cue, str) or (argument_id, cue) not in required_cues:
            result.error(
                f"{relative(VOICE_RESTORATION)}:{number}: cue {cue!r} is not "
                f"approved for {argument_id}"
            )
            continue
        cue_key = (argument_id, cue)
        if cue_key in covered_cues:
            result.error(
                f"{relative(VOICE_RESTORATION)}:{number}: duplicate cue treatment "
                f"for {argument_id}: {cue!r}"
            )
        covered_cues.add(cue_key)

        source_ids = row.get("source_record_ids")
        if not isinstance(source_ids, list) or not source_ids:
            result.error(
                f"{relative(VOICE_RESTORATION)}:{number}: source_record_ids "
                "must be nonempty"
            )
            source_ids = []
        unknown = [source_id for source_id in source_ids if source_id not in transcript]
        if unknown:
            result.error(
                f"{relative(VOICE_RESTORATION)}:{number}: unknown transcript "
                f"records {unknown}"
            )
        argument = arguments[argument_id]
        start_id = argument.get("transcript_start_id")
        end_id = argument.get("transcript_end_id")
        if start_id in positions and end_id in positions:
            outside = [
                source_id
                for source_id in source_ids
                if source_id in positions
                and not positions[start_id] <= positions[source_id] <= positions[end_id]
            ]
            if outside:
                result.error(
                    f"{relative(VOICE_RESTORATION)}:{number}: source records "
                    f"outside {argument_id}: {outside}"
                )

        source_text = row.get("source_text")
        combined_source = " ".join(
            str(transcript.get(source_id, {}).get("cleaned_text") or "")
            for source_id in source_ids
        )
        if not isinstance(source_text, str) or not source_text.strip():
            result.error(
                f"{relative(VOICE_RESTORATION)}:{number}: source_text must be nonempty"
            )
        elif source_text not in combined_source:
            result.error(
                f"{relative(VOICE_RESTORATION)}:{number}: source_text is absent "
                "from the cited frozen transcript records"
            )

        treatment = row.get("treatment")
        if treatment not in allowed_treatments:
            result.error(
                f"{relative(VOICE_RESTORATION)}:{number}: treatment must be one "
                f"of {sorted(allowed_treatments)}"
            )
        final_text = row.get("final_text")
        if not isinstance(final_text, str) or not final_text.strip():
            result.error(
                f"{relative(VOICE_RESTORATION)}:{number}: final_text must be nonempty"
            )
        elif " ".join(final_text.split()) not in normalized_visible:
            result.gate(
                f"{relative(VOICE_RESTORATION)}:{number}: final_text is absent "
                "from the current chapter"
            )
        if not isinstance(row.get("voice_function"), str) or not row["voice_function"].strip():
            result.error(
                f"{relative(VOICE_RESTORATION)}:{number}: voice_function must be nonempty"
            )
        if not isinstance(row.get("reason"), str) or not row["reason"].strip():
            result.error(
                f"{relative(VOICE_RESTORATION)}:{number}: reason must be nonempty"
            )
        if row.get("status") != "approved":
            result.gate(
                f"{relative(VOICE_RESTORATION)}:{number}: status is not approved"
            )
        if row.get("chapter_sha256") != chapter_hash:
            result.gate(
                f"{relative(VOICE_RESTORATION)}:{number}: chapter_sha256 is stale"
            )

    missing_cues = sorted(required_cues - covered_cues)
    extra_cues = sorted(covered_cues - required_cues)
    if missing_cues:
        result.gate(f"voice-restoration ledger lacks approved cues: {missing_cues}")
    if extra_cues:
        result.error(f"voice-restoration ledger has unapproved cues: {extra_cues}")
    result.stats["voice_cues"] = len(required_cues)
    result.stats["voice_cues_verified"] = len(required_cues & covered_cues)


def validate_pass_ledger(result: Result) -> None:
    if not PASS_LEDGER.is_file():
        result.gate(f"missing required pass ledger: {relative(PASS_LEDGER)}")
        return
    text = PASS_LEDGER.read_text(encoding="utf-8")
    chapter_hash = hashlib.sha256(CHAPTER.read_bytes()).hexdigest()
    hash_match = re.search(r"Chapter SHA-256:\s*\n?`([0-9a-f]{64})`", text)
    if hash_match is None:
        result.gate("writing pass ledger lacks a chapter SHA-256")
    elif hash_match.group(1) != chapter_hash:
        result.gate("writing pass ledger cites a stale chapter SHA-256")
    completed = 0
    for number, name in enumerate(REQUIRED_PASSES, 1):
        pattern = re.compile(
            rf"(?ms)^##\s+Pass\s+{number}:\s*{re.escape(name)}\s*$"
            rf".*?^Status:\s*complete\s*$"
        )
        if pattern.search(text):
            completed += 1
        else:
            result.gate(f"writing pass {number} ({name}) is not complete")
    result.stats["completed_writing_passes"] = completed


def exception_spans(
    visible: str, rows: list[tuple[int, dict[str, Any]]], result: Result
) -> dict[str, set[tuple[int, int]]]:
    approved: dict[str, set[tuple[int, int]]] = {
        name: set() for name in REVIEW_PATTERNS
    }
    seen_ids: set[str] = set()
    for number, row in rows:
        exception_id = row.get("id")
        pattern_name = row.get("pattern")
        exact_text = row.get("exact_text")
        expected = row.get("expected_occurrences")
        source_ids = row.get("source_ids")
        if not isinstance(exception_id, str) or not exception_id:
            result.error(f"{relative(STYLE_EXCEPTIONS)}:{number}: missing id")
            continue
        if exception_id in seen_ids:
            result.error(
                f"{relative(STYLE_EXCEPTIONS)}:{number}: duplicate id {exception_id}"
            )
        seen_ids.add(exception_id)
        if pattern_name not in REVIEW_PATTERNS:
            result.error(
                f"{relative(STYLE_EXCEPTIONS)}:{number}: unknown pattern "
                f"{pattern_name!r}"
            )
            continue
        if not isinstance(exact_text, str) or not exact_text:
            result.error(
                f"{relative(STYLE_EXCEPTIONS)}:{number}: exact_text must be nonempty"
            )
            continue
        if not isinstance(expected, int) or expected < 1:
            result.error(
                f"{relative(STYLE_EXCEPTIONS)}:{number}: "
                "expected_occurrences must be a positive integer"
            )
            continue
        if not isinstance(source_ids, list) or not source_ids:
            result.gate(
                f"{relative(STYLE_EXCEPTIONS)}:{number}: source_ids must be nonempty"
            )
        if row.get("status") != "approved":
            result.gate(
                f"{relative(STYLE_EXCEPTIONS)}:{number}: exception is not approved"
            )

        starts = [match.start() for match in re.finditer(re.escape(exact_text), visible)]
        if len(starts) != expected:
            result.gate(
                f"{relative(STYLE_EXCEPTIONS)}:{number}: exact_text occurs "
                f"{len(starts)} time(s), expected {expected}"
            )
        local_matches = list(REVIEW_PATTERNS[pattern_name].finditer(exact_text))
        if not local_matches:
            result.error(
                f"{relative(STYLE_EXCEPTIONS)}:{number}: exact_text contains no "
                f"{pattern_name} occurrence"
            )
            continue
        for start in starts:
            for match in local_matches:
                approved[pattern_name].add(
                    (start + match.start("phrase"), start + match.end("phrase"))
                )
    result.stats["style_exceptions"] = len(seen_ids)
    return approved


def validate_style_and_tex(chapter_text: str, result: Result) -> None:
    if not STYLE.is_file():
        result.error(f"missing governing style ledger: {relative(STYLE)}")
    elif "54694a11d5b79ebf34003dcf62cc4d96c31fe27829019d9797344b0bc6fea635" not in STYLE.read_text(encoding="utf-8"):
        result.gate("WRITING_STYLE.md lacks the inspected Yin reference fingerprint")

    command_checks = {
        r"\\noindent\b": r"\noindent",
        r"\\ensuremath\b": r"\ensuremath",
        r"\\vec\b": r"\vec",
    }
    for pattern, label in command_checks.items():
        hits = len(re.findall(pattern, chapter_text))
        if hits:
            result.error(f"chapter contains {hits} forbidden {label} occurrence(s)")
    hidden = HIDDEN_TEX_RE.findall(chapter_text)
    if hidden:
        result.error(f"chapter contains hidden or overlaid TeX commands: {hidden}")
    legacy = LEGACY_MARKER_RE.findall(chapter_text)
    if legacy:
        result.error(
            f"chapter contains {len(legacy)} legacy near-verbatim marker(s); "
            "use YIN-SPEECH markers"
        )

    visible = visible_tex(chapter_text)
    scan_text = re.sub(r"\s+", " ", visible).strip()
    if "..." in visible or "…" in visible:
        result.error("chapter contains transcript ellipsis in visible text")
    uncertainty = READER_UNCERTAINTY_RE.findall(visible)
    if uncertainty:
        result.error(
            "chapter contains reader-facing uncertainty markers: "
            f"{uncertainty[:6]}"
        )
    for label, pattern in HARD_FILLER_PATTERNS.items():
        matches = list(pattern.finditer(scan_text))
        if matches:
            samples = [match.group(0) for match in matches[:4]]
            result.error(
                f"chapter contains {len(matches)} hard filler or classroom "
                f"occurrence(s) for {label}: {samples}"
            )

    exception_rows = load_jsonl(STYLE_EXCEPTIONS, result)
    approved = exception_spans(scan_text, exception_rows, result)
    review_hits = 0
    for pattern_name, pattern in REVIEW_PATTERNS.items():
        for match in pattern.finditer(scan_text):
            review_hits += 1
            span = match.span("phrase")
            if span not in approved[pattern_name]:
                context_start = max(0, span[0] - 55)
                context_end = min(len(scan_text), span[1] + 75)
                context = scan_text[context_start:context_end]
                result.error(
                    f"unapproved review-required phrase {pattern_name}: {context!r}"
                )
    result.stats["review_required_phrase_occurrences"] = review_hits

    oversized, inline_count = oversized_inline_formulas(visible)
    if oversized:
        result.error(
            "large formulas remain in inline math: "
            + "; ".join(repr(item) for item in oversized[:8])
        )
    result.stats["inline_math_expressions"] = inline_count
    result.stats["oversized_inline_math"] = len(oversized)


def run_audit(root: Path = ROOT, strict: bool = False) -> Result:
    if root != ROOT:
        raise ValueError("audit_written_prose currently supports its edition root only")
    result = Result(strict=strict)
    if not CHAPTER.is_file():
        result.error(f"missing chapter: {relative(CHAPTER)}")
        return result
    chapter_text = CHAPTER.read_text(encoding="utf-8")
    order, blocks = parse_speech_blocks(chapter_text.splitlines(), result)
    validate_source_coverage(order, blocks, result)
    validate_argument_map(result)
    validate_voice_restoration(chapter_text, result)
    validate_pass_ledger(result)
    validate_style_and_tex(chapter_text, result)
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--strict", action="store_true")
    args = parser.parse_args()
    result = run_audit(strict=args.strict)
    for warning in result.warnings:
        print(f"WARNING: {warning}")
    for error in result.errors:
        print(f"ERROR: {error}", file=sys.stderr)
    payload = dict(result.stats)
    payload.update(
        {
            "errors": len(result.errors),
            "warnings": len(result.warnings),
            "status": "PASS" if not result.errors and not result.warnings else (
                "DRAFT_INCOMPLETE" if not result.errors else "FAIL"
            ),
        }
    )
    print(json.dumps(payload, indent=2, sort_keys=True))
    return result.exit_code


if __name__ == "__main__":
    raise SystemExit(main())
