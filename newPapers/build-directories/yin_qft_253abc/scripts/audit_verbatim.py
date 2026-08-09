#!/usr/bin/env python3
"""Archived read-only audit for the abandoned near-verbatim pilot.

The active written textbook pipeline uses ``audit_written_prose.py``.  This
module remains only to reproduce the historical lexical-retention experiment.
It is not imported by ``audit_project.py`` and cannot approve a release.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass, field
import hashlib
import json
import math
from pathlib import Path
import re
import sys
import unicodedata
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
FROZEN_SHA = "5ac8ac5fb25a3235d8fa11b2b6be99b5f2bb9329d307c4045629544f4e43e9bd"
EXPECTED_ELIGIBLE_RECORDS = 198
EXPECTED_EXCLUDED_RECORDS = 103
EXPECTED_ELIGIBLE_WORDS = 6_542
MIN_REPRESENTED_WORDS = 6_215
MIN_GLOBAL_RECALL = 0.95
MIN_RECORD_RECALL = 0.80
MIN_RECORD_PRECISION = 0.90
EXPECTED_FORMULA_RECORDS = 64

ALLOWED_FORMULA_CLASSES = frozenset(
    {
        "NOTES_EXACT",
        "SPEECH_CLEAN",
        "SOURCE_COMPOSITE",
        "EQUATION_NORMALIZED",
        "EDITORIAL_NOTE",
        "SOURCE_CONFLICT",
    }
)
ELIGIBLE_CHAPTER_USES = frozenset(
    {"included", "included_clear_portion_uncertainty_excluded"}
)

TRANSCRIPT_REL = Path("work/pilot/transcript.cleaned.jsonl")
DISPOSITIONS_REL = Path("work/pilot/transcript-dispositions.jsonl")
CHAPTER_REL = Path("latex/chapters/253a/chapter01.tex")
OMISSIONS_REL = Path("work/pilot/verbatim-omissions.jsonl")
FORMULAS_REL = Path("work/pilot/verbatim-formulas.jsonl")

RECORD_ID_RE = re.compile(r"^YIN-OY-T\d{6}[AB]?$")
BEGIN_RE = re.compile(
    r"^\s*%\s*YIN-VERBATIM-BEGIN\s+(YIN-OY-T\d{6}[AB]?)\s*$"
)
END_RE = re.compile(
    r"^\s*%\s*YIN-VERBATIM-END\s+(YIN-OY-T\d{6}[AB]?)\s*$"
)
TIME_RE = re.compile(r"^(\d{2,}):([0-5]\d):([0-5]\d)\.(\d{3})$")
FORMULA_RE = re.compile(r"\$|\\\(")
HIDDEN_TEXT_COMMAND_RE = re.compile(
    r"\\(?:[hv]?phantom|[rlc]lap|math(?:llap|rlap|clap))\b"
)
ENSUREMATH_RE = re.compile(r"\\ensuremath\s*\{")
TEX_NUMERIC_SCRIPT_RE = re.compile(
    r"[\^_]\s*(?:"
    r"\{\s*(?P<braced>[+\-\u2212]?\s*(?:\\[,;:!]\s*)*\d+)\s*\}"
    r"|(?P<bare>[+\-\u2212]?\d+))"
)

NORMALIZATION_FIXTURES = (
    (
        "numeric inverse superscript",
        "U \u03c6\u0302(x) U\u207b\u00b9",
        r"\ensuremath{U\hat\phi(x)U^{-1}}",
        ["u", "x", "u1"],
    ),
    (
        "hatted-operator possessives",
        "P\u0302's and J\u0302's",
        r"\ensuremath{\hat P}'s and \ensuremath{\hat J}'s",
        ["p's", "and", "j's"],
    ),
)


@dataclass
class VerbatimAuditResult:
    strict: bool
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    stats: dict[str, int | float | str] = field(default_factory=dict)

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


def relative(path: Path, root: Path) -> str:
    try:
        return str(path.relative_to(root))
    except ValueError:
        return str(path)


def summarize(values: set[str] | list[str], limit: int = 10) -> str:
    ordered = sorted(values)
    if len(ordered) <= limit:
        return repr(ordered)
    return f"{ordered[:limit]!r} ... ({len(ordered)} total)"


def load_jsonl(
    path: Path,
    root: Path,
    result: VerbatimAuditResult,
) -> list[tuple[int, dict[str, Any]]]:
    if not path.is_file():
        return []
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError as exc:
        result.error(f"{relative(path, root)} is not valid UTF-8: {exc}")
        return []
    if not text:
        result.error(f"{relative(path, root)} is empty")
        return []
    records: list[tuple[int, dict[str, Any]]] = []
    for number, line in enumerate(text.splitlines(), 1):
        if not line.strip():
            result.error(
                f"{relative(path, root)}:{number}: blank line is not a JSONL record"
            )
            continue
        try:
            value = json.loads(line)
        except json.JSONDecodeError as exc:
            result.error(
                f"{relative(path, root)}:{number}: invalid JSON at column "
                f"{exc.colno}: {exc.msg}"
            )
            continue
        if not isinstance(value, dict):
            result.error(
                f"{relative(path, root)}:{number}: JSONL record must be an object"
            )
            continue
        records.append((number, value))
    return records


def millis(value: Any) -> int | None:
    if not isinstance(value, str):
        return None
    match = TIME_RE.fullmatch(value)
    if match is None:
        return None
    hour, minute, second, fraction = map(int, match.groups())
    return ((hour * 60 + minute) * 60 + second) * 1_000 + fraction


def in_scope(record: dict[str, Any]) -> bool:
    start = millis(record.get("start"))
    end = millis(record.get("end"))
    if start is None or end is None:
        return False
    core = start >= 302_580 and end <= 4_787_090
    clear_qa = start >= 4_787_100 and end <= 4_813_920
    return core or clear_qa


def strip_math(text: str) -> str:
    text = re.sub(
        r"\\begin\{(?:equation\*?|align\*?|gather\*?|multline\*?)\}.*?"
        r"\\end\{(?:equation\*?|align\*?|gather\*?|multline\*?)\}",
        " ",
        text,
        flags=re.S,
    )
    text = re.sub(r"\\\[.*?\\\]", " ", text, flags=re.S)
    text = re.sub(r"\\\(.*?\\\)", " ", text, flags=re.S)
    text = re.sub(r"\$\$.*?\$\$", " ", text, flags=re.S)
    return re.sub(r"\$[^$]*\$", " ", text, flags=re.S)


def secure_text(record: dict[str, Any]) -> str:
    text = record.get("cleaned_text") or ""
    record_id = record.get("id")
    if record_id == "YIN-OY-T000149" and "[Yin:]" in text:
        text = text.split("[Yin:]", 1)[1]
    elif record_id == "YIN-OY-T000314":
        text = "For now, yes."
    elif record_id == "YIN-OY-T000317":
        text = "thing."
    text = strip_math(text)
    return re.sub(r"\[[^\]]*\]", " ", text)


def unwrap_ensuremath(text: str) -> str:
    """Remove ensuremath wrappers while preserving their balanced contents."""
    search_from = 0
    while True:
        match = ENSUREMATH_RE.search(text, search_from)
        if match is None:
            return text
        group_start = match.end() - 1
        depth = 0
        group_end: int | None = None
        for index in range(group_start, len(text)):
            character = text[index]
            escaped = index > 0 and text[index - 1] == "\\"
            if character == "{" and not escaped:
                depth += 1
            elif character == "}" and not escaped:
                depth -= 1
                if depth == 0:
                    group_end = index
                    break
        if group_end is None:
            return text
        contents = text[group_start + 1 : group_end]
        text = text[: match.start()] + contents + text[group_end + 1 :]
        search_from = match.start()


def normalize_tex_numeric_scripts(text: str) -> str:
    """Fold TeX numeric scripts as NFKD folds Unicode script numerals."""

    def replace(match: re.Match[str]) -> str:
        value = match.group("braced") or match.group("bare") or ""
        return "".join(character for character in value if character.isdigit())

    return TEX_NUMERIC_SCRIPT_RE.sub(replace, text)


def tex_to_text(text: str) -> str:
    text = re.sub(r"(?m)%.*$", " ", text)
    text = strip_math(text)
    text = unwrap_ensuremath(text)
    text = normalize_tex_numeric_scripts(text)
    text = re.sub(
        r"\\['\"`^~=.uvHckbdtr]\s*\{?([A-Za-z])\}?", r"\1", text
    )
    text = re.sub(
        r"\\(?:textit|emph|textbf|textrm|textsf|texttt)\s*\{([^{}]*)\}",
        r"\1",
        text,
    )
    text = re.sub(r"\\[A-Za-z@]+\*?(?:\[[^\]]*\])?", " ", text)
    text = text.replace("{", " ").replace("}", " ").replace("~", " ")
    return re.sub(r"\[[^\]]*\]", " ", text)


def tokens(text: str) -> list[str]:
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    text = text.lower().replace("’", "'")
    return re.findall(r"[a-z0-9]+(?:'[a-z0-9]+)?", text)


def validate_normalization_fixtures(result: VerbatimAuditResult) -> None:
    for label, canonical, tex, expected in NORMALIZATION_FIXTURES:
        canonical_tokens = tokens(canonical)
        tex_tokens = tokens(tex_to_text(tex))
        if canonical_tokens != expected or tex_tokens != expected:
            result.error(
                f"normalization regression for {label}: canonical="
                f"{canonical_tokens!r}, TeX={tex_tokens!r}, expected={expected!r}"
            )
    result.stats["normalization_fixtures"] = len(NORMALIZATION_FIXTURES)


def lcs_length(left: list[str], right: list[str]) -> int:
    row = [0] * (len(right) + 1)
    for left_token in left:
        previous = 0
        for index, right_token in enumerate(right, 1):
            saved = row[index]
            if left_token == right_token:
                row[index] = previous + 1
            elif row[index - 1] > row[index]:
                row[index] = row[index - 1]
            previous = saved
    return row[-1]


def parse_blocks(
    text: str,
    path: Path,
    root: Path,
    result: VerbatimAuditResult,
) -> tuple[dict[str, str], list[str], int, int]:
    lines = text.splitlines(keepends=True)
    blocks: dict[str, str] = {}
    order: list[str] = []
    open_id: str | None = None
    open_line = 0
    body_start = 0
    begin_count = 0
    end_count = 0

    for index, line in enumerate(lines):
        number = index + 1
        stripped = line.rstrip("\r\n")
        begin = BEGIN_RE.fullmatch(stripped)
        end = END_RE.fullmatch(stripped)
        if "YIN-VERBATIM-BEGIN" in line and begin is None:
            result.error(
                f"{relative(path, root)}:{number}: malformed YIN-VERBATIM-BEGIN"
            )
        if "YIN-VERBATIM-END" in line and end is None:
            result.error(
                f"{relative(path, root)}:{number}: malformed YIN-VERBATIM-END"
            )
        if begin is not None:
            begin_count += 1
            record_id = begin.group(1)
            if open_id is not None:
                result.error(
                    f"{relative(path, root)}:{number}: nested verbatim block "
                    f"{record_id}; {open_id} began on line {open_line}"
                )
                continue
            open_id = record_id
            open_line = number
            body_start = index + 1
            continue
        if end is not None:
            end_count += 1
            record_id = end.group(1)
            if open_id is None:
                result.error(
                    f"{relative(path, root)}:{number}: orphan verbatim end {record_id}"
                )
                continue
            if record_id != open_id:
                result.error(
                    f"{relative(path, root)}:{number}: verbatim end {record_id} "
                    f"does not match {open_id} from line {open_line}"
                )
                open_id = None
                continue
            if record_id in blocks:
                result.error(
                    f"{relative(path, root)}:{number}: duplicate verbatim block "
                    f"for {record_id}"
                )
            else:
                blocks[record_id] = "".join(lines[body_start:index])
                order.append(record_id)
            open_id = None

    if open_id is not None:
        result.error(
            f"{relative(path, root)}:{open_line}: unclosed verbatim block {open_id}"
        )
    return blocks, order, begin_count, end_count


def has_uncertain_span(record: dict[str, Any]) -> bool:
    record_id = record.get("id")
    if record_id in {"YIN-OY-T000149", "YIN-OY-T000314"}:
        return True
    text = strip_math(record.get("cleaned_text") or "")
    spans = re.findall(r"\[([^\]]*)\]", text)
    speaker_labels = {"Yin:", "Student:", "Audience:", "Question:", "Q:", "A:"}
    for span in spans:
        if span.strip() in speaker_labels:
            continue
        return True
    return False


def validate_page_list(value: Any) -> bool:
    return (
        isinstance(value, list)
        and bool(value)
        and all(isinstance(item, int) and not isinstance(item, bool) and item > 0 for item in value)
    )


def run_audit(root: Path = ROOT, strict: bool = False) -> VerbatimAuditResult:
    result = VerbatimAuditResult(strict=strict)
    validate_normalization_fixtures(result)
    transcript_path = root / TRANSCRIPT_REL
    dispositions_path = root / DISPOSITIONS_REL
    chapter_path = root / CHAPTER_REL
    omissions_path = root / OMISSIONS_REL
    formulas_path = root / FORMULAS_REL

    for path, label in (
        (transcript_path, "canonical transcript"),
        (dispositions_path, "transcript dispositions"),
        (chapter_path, "chapter TeX"),
    ):
        if not path.is_file():
            result.error(f"missing {label}: {relative(path, root)}")
    if result.errors:
        return result

    digest = hashlib.sha256(transcript_path.read_bytes()).hexdigest()
    result.stats["transcript_sha256"] = digest
    if digest != FROZEN_SHA:
        result.error(
            f"transcript drift: expected {FROZEN_SHA}, found {digest}"
        )

    transcript_rows = load_jsonl(transcript_path, root, result)
    disposition_rows = load_jsonl(dispositions_path, root, result)
    records: list[dict[str, Any]] = []
    by_id: dict[str, dict[str, Any]] = {}
    for number, record in transcript_rows:
        if record.get("record_type") == "transcript_metadata":
            continue
        record_id = record.get("id")
        if not isinstance(record_id, str) or RECORD_ID_RE.fullmatch(record_id) is None:
            result.error(
                f"{relative(transcript_path, root)}:{number}: malformed record id "
                f"{record_id!r}"
            )
            continue
        if record_id in by_id:
            result.error(
                f"{relative(transcript_path, root)}:{number}: duplicate record id "
                f"{record_id}"
            )
            continue
        if millis(record.get("start")) is None or millis(record.get("end")) is None:
            result.error(
                f"{relative(transcript_path, root)}:{number}: malformed interval for "
                f"{record_id}"
            )
        records.append(record)
        by_id[record_id] = record

    use: dict[str, str] = {}
    for number, disposition in disposition_rows:
        reference_sha = disposition.get("transcript_sha256")
        if reference_sha != FROZEN_SHA:
            result.error(
                f"{relative(dispositions_path, root)}:{number}: "
                f"transcript_sha256={reference_sha!r}; expected {FROZEN_SHA}"
            )
        record_id = disposition.get("transcript_record_id")
        chapter_use = disposition.get("chapter_use")
        if not isinstance(record_id, str) or RECORD_ID_RE.fullmatch(record_id) is None:
            result.error(
                f"{relative(dispositions_path, root)}:{number}: malformed "
                f"transcript_record_id {record_id!r}"
            )
            continue
        if record_id in use:
            result.error(
                f"{relative(dispositions_path, root)}:{number}: duplicate disposition "
                f"for {record_id}"
            )
            continue
        if not isinstance(chapter_use, str) or not chapter_use:
            result.error(
                f"{relative(dispositions_path, root)}:{number}: missing chapter_use "
                f"for {record_id}"
            )
            continue
        use[record_id] = chapter_use

    scoped = {record["id"] for record in records if in_scope(record)}
    missing_dispositions = scoped - set(use)
    if missing_dispositions:
        result.error(
            "scope records missing transcript dispositions: "
            f"{summarize(missing_dispositions)}"
        )
    eligible = {
        record["id"]
        for record in records
        if in_scope(record) and use.get(record["id"]) in ELIGIBLE_CHAPTER_USES
    }
    boundary_id = "YIN-OY-T000317"
    if boundary_id not in by_id:
        result.error(f"missing boundary-token record {boundary_id}")
    else:
        eligible.add(boundary_id)
    excluded = scoped - eligible

    result.stats["eligible_records"] = len(eligible)
    result.stats["excluded_scope_records"] = len(excluded)
    if len(eligible) != EXPECTED_ELIGIBLE_RECORDS:
        result.error(
            f"eligible record baseline drift: expected {EXPECTED_ELIGIBLE_RECORDS}, "
            f"found {len(eligible)}"
        )
    if len(excluded) != EXPECTED_EXCLUDED_RECORDS:
        result.error(
            f"excluded record baseline drift: expected {EXPECTED_EXCLUDED_RECORDS}, "
            f"found {len(excluded)}"
        )

    source_tokens: dict[str, list[str]] = {}
    for record_id in eligible:
        record = by_id.get(record_id)
        if record is not None:
            source_tokens[record_id] = tokens(secure_text(record))
    eligible_word_count = sum(len(value) for value in source_tokens.values())
    result.stats["eligible_lexical_words"] = eligible_word_count
    if eligible_word_count != EXPECTED_ELIGIBLE_WORDS:
        result.error(
            f"eligible lexical baseline drift: expected {EXPECTED_ELIGIBLE_WORDS}, "
            f"found {eligible_word_count}"
        )
    empty_sources = {record_id for record_id, value in source_tokens.items() if not value}
    if empty_sources:
        result.error(
            f"eligible records with no secure lexical words: {summarize(empty_sources)}"
        )

    chapter_text = chapter_path.read_text(encoding="utf-8")
    blocks, block_order, begin_count, end_count = parse_blocks(
        chapter_text, chapter_path, root, result
    )
    result.stats["verbatim_begin_markers"] = begin_count
    result.stats["verbatim_end_markers"] = end_count
    result.stats["verbatim_blocks"] = len(blocks)
    hidden_text_blocks = {
        record_id
        for record_id, block in blocks.items()
        if HIDDEN_TEXT_COMMAND_RE.search(block)
    }
    if hidden_text_blocks:
        result.error(
            "verbatim blocks contain hidden or overlaid TeX text commands: "
            f"{summarize(hidden_text_blocks)}"
        )
    result.stats["hidden_text_blocks"] = len(hidden_text_blocks)
    if begin_count != EXPECTED_ELIGIBLE_RECORDS:
        result.gate(
            f"expected exactly {EXPECTED_ELIGIBLE_RECORDS} YIN-VERBATIM-BEGIN "
            f"markers, found {begin_count}"
        )
    if end_count != EXPECTED_ELIGIBLE_RECORDS:
        result.gate(
            f"expected exactly {EXPECTED_ELIGIBLE_RECORDS} YIN-VERBATIM-END "
            f"markers, found {end_count}"
        )
    missing_blocks = eligible - set(blocks)
    extra_blocks = set(blocks) - eligible
    if missing_blocks:
        result.gate(f"missing eligible verbatim blocks: {summarize(missing_blocks)}")
    if extra_blocks:
        result.gate(f"extra verbatim blocks: {summarize(extra_blocks)}")

    expected_order = sorted(
        eligible,
        key=lambda record_id: (
            millis(by_id[record_id].get("start")) or -1,
            millis(by_id[record_id].get("end")) or -1,
            record_id,
        ),
    )
    observed_eligible_order = [record_id for record_id in block_order if record_id in eligible]
    expected_present_order = [record_id for record_id in expected_order if record_id in blocks]
    if observed_eligible_order != expected_present_order:
        first_difference = next(
            (
                index
                for index, (observed, expected) in enumerate(
                    zip(observed_eligible_order, expected_present_order), 1
                )
                if observed != expected
            ),
            min(len(observed_eligible_order), len(expected_present_order)) + 1,
        )
        result.gate(
            "verbatim blocks are not in source order; first differing position "
            f"is {first_difference}"
        )

    omission_rows: list[tuple[int, dict[str, Any]]] = []
    if not omissions_path.is_file():
        result.gate(f"missing required sidecar: {relative(omissions_path, root)}")
    else:
        omission_rows = load_jsonl(omissions_path, root, result)
    record_exclusion_rows: dict[str, int] = {}
    span_omission_ids: set[str] = set()
    span_omission_row_count = 0
    for number, omission in omission_rows:
        kind = omission.get("record_type")
        record_id = omission.get("transcript_record_id")
        if kind not in {"record_exclusion", "span_omission"}:
            result.error(
                f"{relative(omissions_path, root)}:{number}: unsupported record_type "
                f"{kind!r}"
            )
            continue
        if not isinstance(record_id, str) or RECORD_ID_RE.fullmatch(record_id) is None:
            result.error(
                f"{relative(omissions_path, root)}:{number}: malformed "
                f"transcript_record_id {record_id!r}"
            )
            continue
        if kind == "record_exclusion":
            if record_id in record_exclusion_rows:
                result.error(
                    f"{relative(omissions_path, root)}:{number}: duplicate "
                    f"record_exclusion for {record_id}"
                )
                continue
            record_exclusion_rows[record_id] = number
        else:
            span_omission_row_count += 1
            span_omission_ids.add(record_id)
            for field_name in ("omitted_text", "reason_code", "detail"):
                value = omission.get(field_name)
                if not isinstance(value, str) or not value.strip():
                    result.error(
                        f"{relative(omissions_path, root)}:{number}: "
                        f"span_omission for {record_id} lacks nonempty {field_name}"
                    )

    record_exclusions = set(record_exclusion_rows)
    span_omissions = span_omission_ids
    result.stats["record_exclusions"] = len(record_exclusions)
    result.stats["span_omission_records"] = len(span_omissions)
    result.stats["span_omission_rows"] = span_omission_row_count
    if len(record_exclusions) != EXPECTED_EXCLUDED_RECORDS:
        result.gate(
            f"expected exactly {EXPECTED_EXCLUDED_RECORDS} record_exclusion rows, "
            f"found {len(record_exclusions)}"
        )
    missing_exclusions = excluded - record_exclusions
    extra_exclusions = record_exclusions - excluded
    if missing_exclusions:
        result.gate(f"missing record exclusions: {summarize(missing_exclusions)}")
    if extra_exclusions:
        result.gate(f"extra record exclusions: {summarize(extra_exclusions)}")

    represented = 0
    record_threshold_failures: list[str] = []
    unlisted_span_omissions: set[str] = set()
    for record_id in expected_order:
        if record_id not in blocks or record_id not in source_tokens:
            continue
        source = source_tokens[record_id]
        printed = tokens(tex_to_text(blocks[record_id]))
        common = lcs_length(source, printed)
        represented += common
        recall = common / len(source)
        precision = common / len(printed) if printed else 0.0
        required = max(1, math.ceil(MIN_RECORD_RECALL * len(source)))
        if common < required or precision < MIN_RECORD_PRECISION:
            record_threshold_failures.append(
                f"{record_id}(source={len(source)}, printed={len(printed)}, "
                f"matched={common}, recall={recall:.3f}, precision={precision:.3f})"
            )
        if common < len(source):
            if record_id not in span_omissions:
                unlisted_span_omissions.add(record_id)

    uncertain_span_ids = {
        record_id
        for record_id in eligible
        if record_id in by_id and has_uncertain_span(by_id[record_id])
    }
    unlisted_span_omissions.update(uncertain_span_ids - span_omissions)
    if record_threshold_failures:
        result.gate(
            f"{len(record_threshold_failures)} record block(s) fail the 80% recall "
            "or 90% precision gate: "
            + "; ".join(record_threshold_failures[:8])
            + (" ..." if len(record_threshold_failures) > 8 else "")
        )
    if unlisted_span_omissions:
        result.gate(
            "eligible records have unlisted lexical or uncertainty-span omissions: "
            f"{summarize(unlisted_span_omissions)}"
        )
    global_recall = represented / EXPECTED_ELIGIBLE_WORDS
    result.stats["represented_words"] = represented
    result.stats["global_recall"] = round(global_recall, 6)
    if represented < MIN_REPRESENTED_WORDS or global_recall < MIN_GLOBAL_RECALL:
        result.gate(
            f"global lexical retention is {represented}/{EXPECTED_ELIGIBLE_WORDS} "
            f"({global_recall:.3%}); require at least "
            f"{MIN_REPRESENTED_WORDS}/{EXPECTED_ELIGIBLE_WORDS} ({MIN_GLOBAL_RECALL:.0%})"
        )

    formula_records = {
        record_id
        for record_id in eligible
        if record_id in by_id
        and FORMULA_RE.search(by_id[record_id].get("cleaned_text") or "")
    }
    result.stats["formula_source_records"] = len(formula_records)
    if len(formula_records) != EXPECTED_FORMULA_RECORDS:
        result.error(
            f"formula-bearing source baseline drift: expected "
            f"{EXPECTED_FORMULA_RECORDS}, found {len(formula_records)}"
        )

    formula_rows: list[tuple[int, dict[str, Any]]] = []
    if not formulas_path.is_file():
        result.gate(f"missing required sidecar: {relative(formulas_path, root)}")
    else:
        formula_rows = load_jsonl(formulas_path, root, result)
    formula_by_record: dict[str, tuple[int, dict[str, Any]]] = {}
    for number, formula in formula_rows:
        record_id = formula.get("transcript_record_id")
        if not isinstance(record_id, str) or RECORD_ID_RE.fullmatch(record_id) is None:
            result.error(
                f"{relative(formulas_path, root)}:{number}: malformed "
                f"transcript_record_id {record_id!r}"
            )
            continue
        if record_id in formula_by_record:
            result.error(
                f"{relative(formulas_path, root)}:{number}: duplicate formula row "
                f"for {record_id}"
            )
            continue
        formula_by_record[record_id] = (number, formula)
        source_class = formula.get("source_class")
        if source_class not in ALLOWED_FORMULA_CLASSES:
            result.gate(
                f"{relative(formulas_path, root)}:{number}: invalid formula "
                f"source_class {source_class!r} for {record_id}"
            )
        if not validate_page_list(formula.get("note_pages")):
            result.gate(
                f"{relative(formulas_path, root)}:{number}: formula row for "
                f"{record_id} lacks note_pages"
            )
        if not validate_page_list(formula.get("pdf_pages")):
            result.gate(
                f"{relative(formulas_path, root)}:{number}: formula row for "
                f"{record_id} lacks pdf_pages"
            )
        if formula.get("review_status") != "math_reviewed":
            result.gate(
                f"{relative(formulas_path, root)}:{number}: formula row for "
                f"{record_id} is not math_reviewed"
            )

    formula_ids = set(formula_by_record)
    result.stats["formula_ledger_records"] = len(formula_ids)
    if len(formula_ids) != EXPECTED_FORMULA_RECORDS:
        result.gate(
            f"expected exactly {EXPECTED_FORMULA_RECORDS} formula-ledger rows, "
            f"found {len(formula_ids)}"
        )
    missing_formulas = formula_records - formula_ids
    extra_formulas = formula_ids - formula_records
    if missing_formulas:
        result.gate(f"missing formula-ledger records: {summarize(missing_formulas)}")
    if extra_formulas:
        result.gate(f"extra formula-ledger records: {summarize(extra_formulas)}")

    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--legacy",
        action="store_true",
        help="acknowledge that this is the archived near-verbatim audit",
    )
    parser.add_argument("--strict", action="store_true")
    args = parser.parse_args()
    if not args.legacy:
        parser.error(
            "archived audit; use scripts/audit_written_prose.py for active work "
            "or pass --legacy to reproduce the old experiment"
        )
    result = run_audit(ROOT, strict=args.strict)

    for warning in result.warnings:
        print(f"WARNING: {warning}")
    for error in result.errors:
        print(f"ERROR: {error}", file=sys.stderr)
    status = "PASS" if not result.errors and not result.warnings else (
        "DRAFT_INCOMPLETE" if not result.errors else "FAIL"
    )
    payload = dict(result.stats)
    payload.update(
        {
            "errors": len(result.errors),
            "warnings": len(result.warnings),
            "status": status,
        }
    )
    print(json.dumps(payload, indent=2, sort_keys=True))
    return result.exit_code


if __name__ == "__main__":
    raise SystemExit(main())
