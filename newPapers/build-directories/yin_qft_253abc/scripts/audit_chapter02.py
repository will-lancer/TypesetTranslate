#!/usr/bin/env python3
"""Audit the written and released Physics 253a Chapter 2 edition."""

from __future__ import annotations

import argparse
from dataclasses import dataclass, field
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / "work" / "253a-ch02"
CHAPTER = ROOT / "latex" / "chapters" / "253a" / "chapter02.tex"
CHAPTER1 = ROOT / "latex" / "chapters" / "253a" / "chapter01.tex"
MASTER = ROOT / "latex" / "master.tex"
TRANSCRIPT = WORK / "transcript.cleaned.jsonl"
ARGUMENT_MAP = WORK / "argument-map.jsonl"
PROVENANCE = WORK / "provenance.jsonl"
WRITTEN_TRANSCRIPT = WORK / "written-transcript-dispositions.jsonl"
WRITTEN_PAGES = WORK / "written-page-dispositions.jsonl"
VOICE_INVENTORY = WORK / "pass2-voice-cues.jsonl"
VOICE_RESTORATION = WORK / "voice-restoration.jsonl"
STYLE_EXCEPTIONS = WORK / "style-exceptions.jsonl"
PASS_LEDGER = WORK / "writing-style-pass-ledger.md"
REVIEW_FINAL = WORK / "review-final.md"
RENDER_REVIEW = WORK / "render-review.jsonl"
REPORT = WORK / "report.md"
PRESERVATION = WORK / "chapter1-preservation.json"
PASS2_VALIDATION = WORK / "pass2-validation.json"
SOURCE_PACKET = WORK / "source-packet-manifest.json"
RENDER_MANIFEST = ROOT / "work" / "release" / "render-manifest.json"
FINALIZE_PASS2 = WORK / "tools" / "finalize_pass2.py"
RENDER_ARTIFACTS = ROOT / "scripts" / "render_chapter02_artifacts.py"

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
SOURCE_ID_RE = re.compile(r"^YIN253A-C02-U\d{3}$")
ARGUMENT_ID_RE = re.compile(r"^YIN253A-C02-A\d{2}$")
TRANSCRIPT_ID_RE = re.compile(r"^YIN253A-C02-T(\d{6})$")
EQUATION_ID_RE = re.compile(r"^YIN253A-C02-EQ\d{3}$")
READER_UNCERTAINTY_RE = re.compile(
    r"\[(?:unclear|inaudible|unresolved|likely|uncertain|caption[^]]*)\]",
    re.IGNORECASE,
)
HIDDEN_TEX_RE = re.compile(
    r"\\(?:llap|rlap|clap|phantom|hphantom|vphantom|smash)\b"
)
HARD_FILLERS = {
    "okay": re.compile(r"\bokay\b", re.IGNORECASE),
    "all right": re.compile(r"\ball\s+right\b", re.IGNORECASE),
    "you know": re.compile(r"\byou\s+know\b", re.IGNORECASE),
    "sort of": re.compile(r"\bsort\s+of\b", re.IGNORECASE),
    "isolated uh": re.compile(r"\buh\b", re.IGNORECASE),
    "isolated um": re.compile(r"\bum\b", re.IGNORECASE),
    "question invitation": re.compile(
        r"\b(?:any|other)\s+questions?(?:\s+so\s+far)?\b", re.IGNORECASE
    ),
    "board narration": re.compile(
        r"\b(?:on\s+the\s+board|let\s+me\s+(?:write|draw)|"
        r"I(?:'m|\s+am)\s+going\s+to\s+(?:write|draw))\b",
        re.IGNORECASE,
    ),
}
REVIEW_PATTERNS = {
    "basically": re.compile(r"\bbasically\b", re.IGNORECASE),
    "kind_of": re.compile(r"\bkind\s+of\b", re.IGNORECASE),
    "i_mean": re.compile(r"\bI\s+mean\b"),
    "just": re.compile(r"\bjust\b", re.IGNORECASE),
    "let_me": re.compile(r"\blet\s+me\b", re.IGNORECASE),
    "for_the_moment": re.compile(r"\bfor\s+the\s+moment\b", re.IGNORECASE),
    "sentence_initial_so": re.compile(r"(?m)(?:^|[.!?]\s+)(So)(?:,|\s)"),
    "sentence_initial_now": re.compile(r"(?m)(?:^|[.!?]\s+)(Now)(?:,|\s)"),
}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def rel(path: Path) -> str:
    try:
        return path.relative_to(ROOT).as_posix()
    except ValueError:
        return str(path)


@dataclass
class Audit:
    strict: bool
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    stats: dict[str, Any] = field(default_factory=dict)

    def error(self, message: str) -> None:
        self.errors.append(message)

    def gate(self, message: str) -> None:
        (self.errors if self.strict else self.warnings).append(message)

    def finish(self) -> int:
        for message in self.warnings:
            print(f"WARNING: {message}")
        for message in self.errors:
            print(f"ERROR: {message}", file=sys.stderr)
        mode = "strict" if self.strict else "draft"
        details = ", ".join(f"{key}={value}" for key, value in sorted(self.stats.items()))
        if self.errors:
            print(
                f"Chapter 2 {mode} audit failed: {len(self.errors)} error(s), "
                f"{len(self.warnings)} warning(s); {details}",
                file=sys.stderr,
            )
            return 1
        print(
            f"Chapter 2 {mode} audit passed: {len(self.warnings)} warning(s); {details}"
        )
        return 0


def load_json(path: Path, audit: Audit) -> dict[str, Any]:
    if not path.is_file():
        audit.gate(f"missing required artifact: {rel(path)}")
        return {}
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        audit.error(f"{rel(path)} is invalid JSON: {exc}")
        return {}
    if not isinstance(value, dict):
        audit.error(f"{rel(path)} must contain a JSON object")
        return {}
    return value


def load_jsonl(path: Path, audit: Audit, *, required: bool = True) -> list[dict[str, Any]]:
    if not path.is_file():
        if required:
            audit.gate(f"missing required artifact: {rel(path)}")
        return []
    rows: list[dict[str, Any]] = []
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            audit.error(f"{rel(path)}:{number}: blank JSONL line")
            continue
        try:
            value = json.loads(line)
        except json.JSONDecodeError as exc:
            audit.error(f"{rel(path)}:{number}: invalid JSON: {exc.msg}")
            continue
        if not isinstance(value, dict):
            audit.error(f"{rel(path)}:{number}: row must be an object")
            continue
        rows.append(value)
    return rows


def run_check(command: list[str], audit: Audit, label: str, *, gated: bool = False) -> None:
    result = subprocess.run(
        command, cwd=ROOT, text=True, capture_output=True, check=False
    )
    if result.returncode:
        detail = (result.stderr or result.stdout).strip().splitlines()
        message = f"{label} failed: {detail[-1] if detail else 'unknown error'}"
        if gated:
            audit.gate(message)
        else:
            audit.error(message)


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


def validate_frozen_packet(audit: Audit) -> None:
    validation = load_json(PASS2_VALIDATION, audit)
    if validation and validation.get("status") != "pass":
        audit.error("Pass 2 validation does not pass")
    if validation and validation.get("source_packet_sha256") != (
        "6e64705ecbd5a91d651c461a8689bfc37c29600da2be9736b79ef4c3adee310d"
    ):
        audit.error("Pass 2 source-packet digest changed")
    run_check(
        [sys.executable, str(FINALIZE_PASS2), "--check"],
        audit,
        "frozen Pass 2 packet check",
    )
    audit.stats["frozen_transcript_sha256"] = validation.get("transcript_sha256", "missing")


def validate_preservation(audit: Audit) -> None:
    contract = load_json(PRESERVATION, audit)
    if not contract or not CHAPTER1.is_file() or not MASTER.is_file():
        return
    expected_chapter = contract.get("protected_chapter_sha256")
    actual_chapter = digest(CHAPTER1)
    if actual_chapter != expected_chapter:
        audit.error(
            f"Chapter 1 changed during Chapter 2 work: {actual_chapter} != {expected_chapter}"
        )
    insertion = "\\input{chapters/253a/chapter02.tex}\n"
    master_text = MASTER.read_text(encoding="utf-8")
    if master_text.count(insertion) != 1:
        audit.error("master.tex must contain exactly one Chapter 2 input line")
        return
    if master_text.index(insertion) < master_text.index("\\input{chapters/253a/chapter01.tex}"):
        audit.error("Chapter 2 is not included after Chapter 1")
    if "\\part{Physics 253b" in master_text and master_text.index(insertion) > master_text.index("\\part{Physics 253b"):
        audit.error("Chapter 2 input appears after the Physics 253b boundary")
    before = master_text.replace(insertion, "", 1).encode("utf-8")
    base_hash = hashlib.sha256(before).hexdigest()
    if base_hash != contract.get("protected_master_before_chapter2_sha256"):
        audit.error("master.tex contains edits beyond the permitted Chapter 2 insertion")
    audit.stats["chapter1_sha256"] = actual_chapter


def validate_argument_map(audit: Audit) -> tuple[list[dict[str, Any]], set[str]]:
    rows = load_jsonl(ARGUMENT_MAP, audit)
    units = [row for row in rows if row.get("record_type") == "conceptual_unit"]
    if len(units) != 15:
        audit.error(f"argument map must contain 15 conceptual units, found {len(units)}")
    ids = [str(row.get("id")) for row in rows]
    if len(ids) != len(set(ids)):
        audit.error("argument map IDs are duplicated")
    notes = [int(page) for row in units for page in row.get("note_pages", [])]
    pdfs = [int(page) for row in units for page in row.get("pdf_pages", []) if int(page) != 20]
    if sorted(notes) != list(range(10, 52)):
        audit.error("argument map does not partition note pages 10-51 exactly")
    if sorted(pdfs) != list(range(21, 63)):
        audit.error("argument map does not partition PDF pages 21-62 exactly")
    equations = [str(value) for row in units for value in row.get("equation_source_ids", [])]
    expected_equations = {f"YIN253A-C02-EQ{number:03d}" for number in range(1, 24)}
    if set(equations) != expected_equations or len(equations) != 23:
        audit.error("argument map does not allocate EQ001-EQ023 exactly once")
    selected_cues = {
        str(value) for row in units for value in row.get("selected_voice_cue_ids", [])
    }
    audit_rows = [row for row in rows if row.get("record_type") == "coverage_audit"]
    if len(audit_rows) != 1 or audit_rows[0].get("audit", {}).get("coverage_exact") is not True:
        audit.error("argument map lacks its exact coverage audit")
    audit.stats["argument_units"] = len(units)
    audit.stats["selected_voice_cues"] = len(selected_cues)
    return units, selected_cues


def validate_generated_artifacts(
    audit: Audit, units: list[dict[str, Any]]
) -> list[dict[str, Any]]:
    if not CHAPTER.is_file():
        audit.gate(f"missing canonical chapter: {rel(CHAPTER)}")
        return []
    run_check(
        [sys.executable, str(RENDER_ARTIFACTS), "--check"],
        audit,
        "Chapter 2 generated-artifact check",
        gated=True,
    )
    provenance = load_jsonl(PROVENANCE, audit)
    written_transcript = load_jsonl(WRITTEN_TRANSCRIPT, audit)
    written_pages = load_jsonl(WRITTEN_PAGES, audit)
    if len(written_transcript) != 901:
        audit.gate(f"written transcript dispositions must have 901 rows, found {len(written_transcript)}")
    if [row.get("physical_pdf_page") for row in written_pages] != list(range(20, 69)):
        audit.gate("written page dispositions must cover physical pages 20-68 in order")
    chapter_hash = digest(CHAPTER)
    unit_ids: set[str] = set()
    argument_refs: set[str] = set()
    equation_refs: set[str] = set()
    note_refs: set[int] = set()
    pdf_refs: set[int] = set()
    for number, row in enumerate(provenance, 1):
        source_id = str(row.get("id", ""))
        if SOURCE_ID_RE.fullmatch(source_id) is None:
            audit.error(f"{rel(PROVENANCE)}:{number}: malformed source ID")
        if source_id in unit_ids:
            audit.error(f"{rel(PROVENANCE)}:{number}: duplicate source ID {source_id}")
        unit_ids.add(source_id)
        source_class = str(row.get("source_class", ""))
        if source_class not in ALLOWED_SOURCE_CLASSES:
            audit.error(f"{rel(PROVENANCE)}:{number}: invalid source class {source_class}")
        if row.get("chapter_sha256") != chapter_hash:
            audit.gate(f"{rel(PROVENANCE)}:{number}: stale chapter hash")
        argument_refs.update(map(str, row.get("argument_unit_ids", [])))
        equation_refs.update(map(str, row.get("equation_source_ids", [])))
        note_refs.update(int(page) for page in row.get("note_pages", []))
        pdf_refs.update(int(page) for page in row.get("pdf_pages", []))
        body = str(row.get("final_text", ""))
        blocks = [block for block in re.split(r"\n\s*\n", body) if block.strip()]
        if len(blocks) != 1:
            audit.error(
                f"{source_id} contains {len(blocks)} printed blocks; each paragraph/display/figure needs its own source comment"
            )
        if any(63 <= int(page) <= 67 for page in row.get("pdf_pages", [])):
            if source_class != "EDITORIAL_NOTE" or row.get("equation_source_ids") or row.get("transcript_record_ids"):
                audit.error(f"{source_id} imports assignment evidence into chapter prose")
        if 68 in [int(page) for page in row.get("pdf_pages", [])]:
            if source_class != "EDITORIAL_NOTE" or row.get("equation_source_ids") or row.get("transcript_record_ids"):
                audit.error(f"{source_id} uses physical page 68 as Chapter 2 content")
    expected_arguments = {str(row["id"]) for row in units}
    if not expected_arguments <= argument_refs:
        audit.gate(f"chapter provenance misses arguments {sorted(expected_arguments - argument_refs)}")
    expected_equations = {f"YIN253A-C02-EQ{number:03d}" for number in range(1, 24)}
    if not expected_equations <= equation_refs:
        audit.gate(f"chapter provenance misses equations {sorted(expected_equations - equation_refs)}")
    if not set(range(10, 52)) <= note_refs:
        audit.gate(f"chapter provenance misses note pages {sorted(set(range(10, 52)) - note_refs)}")
    if not set(range(21, 63)) <= pdf_refs:
        audit.gate(f"chapter provenance misses PDF pages {sorted(set(range(21, 63)) - pdf_refs)}")
    audit.stats["provenance_records"] = len(provenance)
    audit.stats["written_transcript_dispositions"] = len(written_transcript)
    audit.stats["written_page_dispositions"] = len(written_pages)
    return provenance


def validate_chapter_text(audit: Audit) -> str:
    if not CHAPTER.is_file():
        return ""
    text = CHAPTER.read_text(encoding="utf-8")
    visible = visible_tex(text)
    normalized_visible = " ".join(visible.split())
    if text.count("\\YinChapter{Lagrangian Quantum Mechanics, Path Integrals, and Perturbation Theory}") != 1:
        audit.error("Chapter 2 title is missing or duplicated")
    if text.count("\\label{ch:253a-lagrangian-qm}") != 1:
        audit.error("Chapter 2 start label is missing or duplicated")
    if text.count("\\label{ch:253a-lagrangian-qm-end}") != 1:
        audit.error("Chapter 2 end label is missing or duplicated")
    if READER_UNCERTAINTY_RE.search(visible):
        audit.error("reader-facing uncertainty marker remains in Chapter 2")
    if HIDDEN_TEX_RE.search(visible):
        audit.error("hidden-text TeX command remains in Chapter 2")
    for token in ("\\noindent", "\\ensuremath", "\\vec"):
        if token in visible:
            audit.error(f"forbidden TeX token remains in Chapter 2: {token}")
    if "..." in visible:
        audit.error("literal transcript ellipsis remains in Chapter 2")
    for name, pattern in HARD_FILLERS.items():
        matches = list(pattern.finditer(normalized_visible))
        if matches:
            audit.error(f"hard filler or classroom phrase {name!r} occurs {len(matches)} time(s)")
    inline = re.sub(
        r"\\begin\{(?:equation\*?|align\*?|gather\*?|multline\*?|figure|figure\*)\}.*?"
        r"\\end\{(?:equation\*?|align\*?|gather\*?|multline\*?|figure|figure\*)\}",
        " ",
        visible,
        flags=re.DOTALL,
    )
    formulas = re.findall(r"(?<!\$)\$(?!\$)(.+?)(?<!\$)\$(?!\$)", inline, flags=re.DOTALL)
    formulas += re.findall(r"\\\((.+?)\\\)", inline, flags=re.DOTALL)
    oversized = [
        " ".join(formula.split())
        for formula in formulas
        if len(" ".join(formula.split())) > 70
        or re.search(r"\\(?:int|sum|prod)\b", formula)
    ]
    if oversized:
        audit.error(f"oversized inline mathematics remains: {oversized[:5]}")
    audit.stats["inline_math_expressions"] = len(formulas)
    audit.stats["chapter_sha256"] = digest(CHAPTER)
    return visible


def validate_style_exceptions(audit: Audit, visible: str) -> None:
    rows = load_jsonl(STYLE_EXCEPTIONS, audit)
    chapter_hash = digest(CHAPTER) if CHAPTER.is_file() else None
    normalized_visible = " ".join(visible.split())
    expected_by_pattern: dict[str, int] = {name: 0 for name in REVIEW_PATTERNS}
    for number, row in enumerate(rows, 1):
        pattern_name = str(row.get("pattern", ""))
        if pattern_name not in REVIEW_PATTERNS:
            audit.error(f"{rel(STYLE_EXCEPTIONS)}:{number}: unknown pattern {pattern_name}")
            continue
        exact_text = str(row.get("exact_text", ""))
        expected = row.get("expected_occurrences")
        if not isinstance(expected, int) or expected < 1:
            audit.error(f"{rel(STYLE_EXCEPTIONS)}:{number}: invalid expected_occurrences")
            continue
        normalized_exact = " ".join(exact_text.split())
        actual_exact = normalized_visible.count(normalized_exact)
        if actual_exact != expected:
            audit.gate(
                f"{rel(STYLE_EXCEPTIONS)}:{number}: exact_text occurs {actual_exact} time(s), expected {expected}"
            )
        expected_by_pattern[pattern_name] += expected
        if row.get("status") != "approved" or not row.get("reason"):
            audit.gate(f"{rel(STYLE_EXCEPTIONS)}:{number}: exception is not approved and justified")
        if row.get("chapter_sha256") != chapter_hash:
            audit.gate(f"{rel(STYLE_EXCEPTIONS)}:{number}: stale chapter hash")
    for name, pattern in REVIEW_PATTERNS.items():
        actual = len(list(pattern.finditer(normalized_visible)))
        if actual != expected_by_pattern[name]:
            audit.gate(
                f"review-required phrase {name}: chapter has {actual}, ledger approves {expected_by_pattern[name]}"
            )
    audit.stats["style_exceptions"] = len(rows)


def validate_voice(
    audit: Audit, visible: str, selected_cues: set[str]
) -> None:
    inventory = {str(row.get("id")): row for row in load_jsonl(VOICE_INVENTORY, audit)}
    rows = load_jsonl(VOICE_RESTORATION, audit)
    by_id = {str(row.get("id")): row for row in rows}
    if set(by_id) != selected_cues:
        audit.gate(
            f"voice restoration IDs differ from selected argument-map cues: "
            f"missing={sorted(selected_cues - set(by_id))}, extra={sorted(set(by_id) - selected_cues)}"
        )
    chapter_hash = digest(CHAPTER) if CHAPTER.is_file() else None
    transcript_hash = digest(TRANSCRIPT) if TRANSCRIPT.is_file() else None
    normalized_visible = " ".join(visible.split())
    for cue_id, row in by_id.items():
        source = inventory.get(cue_id)
        if source is None:
            audit.error(f"voice restoration cue {cue_id} is absent from Pass 2 inventory")
            continue
        source_text = str(row.get("source_text", ""))
        if source_text != source.get("exact_or_minimally_cleaned_cue"):
            audit.error(f"voice restoration cue {cue_id} changes its frozen source phrase")
        final_text = str(row.get("final_text", ""))
        normalized_final = " ".join(final_text.split())
        if not normalized_final or normalized_visible.count(normalized_final) != 1:
            audit.gate(f"voice restoration cue {cue_id} printed phrase is absent or duplicated")
        if row.get("treatment") not in {"retained_exact", "lightly_recast"}:
            audit.error(f"voice restoration cue {cue_id} has invalid treatment")
        if row.get("status") != "approved" or not row.get("reason") or not row.get("voice_function"):
            audit.gate(f"voice restoration cue {cue_id} is not approved and justified")
        if row.get("chapter_sha256") != chapter_hash or row.get("transcript_sha256") != transcript_hash:
            audit.gate(f"voice restoration cue {cue_id} has stale hashes")
    audit.stats["voice_cues_verified"] = len(rows)


def hash_in_text(path: Path, value: str) -> bool:
    return value in path.read_text(encoding="utf-8") if path.is_file() else False


def validate_ledgers_and_reviews(audit: Audit) -> None:
    chapter_hash = digest(CHAPTER) if CHAPTER.is_file() else "missing"
    transcript_hash = digest(TRANSCRIPT) if TRANSCRIPT.is_file() else "missing"
    source_packet_hash = load_json(SOURCE_PACKET, audit).get("source_packet_sha256", "missing")
    if not PASS_LEDGER.is_file():
        audit.gate(f"missing required artifact: {rel(PASS_LEDGER)}")
    else:
        text = PASS_LEDGER.read_text(encoding="utf-8")
        for required in (
            "Pass 3: chapter drafting",
            "Pass 4: editorial balance",
            "Pass 5: fidelity and release",
            chapter_hash,
            transcript_hash,
            source_packet_hash,
        ):
            if required not in text:
                audit.gate(f"writing ledger lacks current marker {required!r}")
        if audit.strict and len(re.findall(r"Status:\s*complete", text, re.IGNORECASE)) < 3:
            audit.error("writing ledger does not mark Passes 3-5 complete")
    if not REVIEW_FINAL.is_file():
        audit.gate(f"missing required artifact: {rel(REVIEW_FINAL)}")
    else:
        text = REVIEW_FINAL.read_text(encoding="utf-8")
        for required in (chapter_hash, transcript_hash, source_packet_hash):
            if required not in text:
                audit.gate(f"final review lacks current hash {required}")
        if text.rstrip().splitlines()[-1] != "Unresolved blockers: none":
            audit.gate("final review does not end with the exact zero-blocker line")
    for path in (REPORT,):
        if not path.is_file():
            audit.gate(f"missing required artifact: {rel(path)}")
        elif not hash_in_text(path, chapter_hash):
            audit.gate(f"{rel(path)} lacks the current chapter hash")


def validate_render_review(audit: Audit) -> None:
    if not audit.strict:
        return
    manifest = load_json(RENDER_MANIFEST, audit)
    rows = load_jsonl(RENDER_REVIEW, audit)
    chapters = manifest.get("chapters", []) if manifest else []
    target = next(
        (row for row in chapters if row.get("chapter_id") == "253a-ch02"), None
    )
    if target is None:
        audit.error("release render manifest lacks the Chapter 2 range")
        return
    images = target.get("images", [])
    by_page = {row.get("pdf_page"): row for row in rows}
    expected_pages = [image.get("page") for image in images]
    if sorted(by_page) != expected_pages:
        audit.error("render review does not cover every affected Chapter 2 PDF page")
    for image in images:
        page = image.get("page")
        review = by_page.get(page, {})
        if review.get("image_sha256") != image.get("sha256"):
            audit.error(f"render review page {page} has a stale image hash")
        if review.get("status") != "inspected" or review.get("blockers") not in ([], None):
            audit.error(f"render review page {page} is not cleanly inspected")
    if manifest.get("pdf_sha256") and not all(
        row.get("pdf_sha256") == manifest.get("pdf_sha256") for row in rows
    ):
        audit.error("render review cites a stale PDF hash")
    audit.stats["rendered_pages_inspected"] = len(rows)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--strict", action="store_true")
    args = parser.parse_args()
    audit = Audit(strict=args.strict)
    validate_frozen_packet(audit)
    validate_preservation(audit)
    units, selected_cues = validate_argument_map(audit)
    visible = validate_chapter_text(audit)
    validate_generated_artifacts(audit, units)
    validate_style_exceptions(audit, visible)
    validate_voice(audit, visible, selected_cues)
    validate_ledgers_and_reviews(audit)
    validate_render_review(audit)
    return audit.finish()


if __name__ == "__main__":
    raise SystemExit(main())
