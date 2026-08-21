#!/usr/bin/env python3
"""Audit page-level prose coverage for the native PCT transcription.

The canonical PCT source is a 221-page scan.  Its embedded OCR is empty on
most pages, so this audit uses the page JPEGs as an OCR fallback.  It joins
assembled native TeX segments to ``PCT-SOURCE`` markers, compares visible
prose after masking TeX mathematics, records likely omissions and OCR residue,
and writes a JSON report.  Strict mode fails on structural evidence, severe
coverage gaps, and exemptions that have no source or native evidence.
"""

from __future__ import annotations

import argparse
import difflib
import hashlib
import json
import re
import shutil
import subprocess
import sys
import unicodedata
from collections import Counter, defaultdict
from dataclasses import asdict, dataclass
from pathlib import Path
from statistics import mean, median
from typing import Any, Sequence


ROOT = Path(__file__).resolve().parents[1]
LATEX = ROOT / "latex"
MASTER = LATEX / "master.tex"
SOURCE = ROOT.parents[2] / "origPapers" / "pct_spin_statistics_all_that.pdf"
DISPOSITIONS = ROOT / "page-dispositions.jsonl"
SOURCE_PAGES = ROOT / "work" / "source-pages"
DEFAULT_REPORT = ROOT / "work" / "reviews" / "transcription_audit.json"
DEFAULT_LOW_RECALL_DISPOSITIONS = ROOT / "work" / "reviews" / "transcription_low_recall_dispositions.json"
DEFAULT_LOW_RECALL_REVIEW = ROOT / "work" / "reviews" / "transcription_low_recall_audit.md"
EXPECTED_PAGES = 221
INCLUDED_STATUS = "transcribed"

PAGE_MARKER = re.compile(
    r"^[ \t]*%\s*PCT-SOURCE:\s*pdf=(?P<physical>\d+)\s+"
    r"print=(?P<printed>[^\s]+)\s+kind=(?P<kind>[^\s]+)"
    r"(?:\s+id=(?P<identifier>[^\s]+))?",
    re.MULTILINE,
)
ASSEMBLY_CALL = re.compile(r"\\(?:PCTInput|input)\s*\{([^{}]+)\}")
INPUT_CALL = re.compile(r"\\(?:input|include)\s*\{([^{}]+)\}")
WORD = re.compile(r"[A-Za-z0-9]+(?:['\u2019][A-Za-z0-9]+)*")

MATH_ENV = re.compile(
    r"\\begin\{(?P<env>equation\*?|align\*?|alignat\*?|gather\*?|"
    r"multline\*?|displaymath|math|array|matrix|pmatrix|bmatrix|cases)\}"
    r".*?\\end\{(?P=env)\}",
    re.DOTALL,
)
INLINE_DOLLAR = re.compile(r"(?<!\\)\$(?!\$).*?(?<!\\)\$(?!\$)", re.DOTALL)
DISPLAY_DOLLAR = re.compile(r"(?<!\\)\$\$.*?(?<!\\)\$\$", re.DOTALL)
INLINE_PAREN = re.compile(r"\\\(.*?\\\)", re.DOTALL)
DISPLAY_BRACKET = re.compile(r"\\\[.*?\\\]", re.DOTALL)
HEADING_COMMAND = re.compile(
    r"\\(?P<command>section|subsection|subsubsection|paragraph|"
    r"chapterbackmatter|chapterappendix|caption)\*?(?:\s*\[[^\]]*\])?\s*"
    r"\{(?P<body>[^{}\n]*)\}"
)

LAYOUT_ONLY_KINDS = {
    "display",
    "equation",
    "figure",
    "diagram",
    "title",
    "chapter-title",
}


@dataclass(frozen=True)
class Marker:
    physical: int
    printed: str
    kind: str
    identifier: str | None
    path: Path
    line: int


@dataclass(frozen=True)
class Segment:
    marker: Marker
    text: str


@dataclass
class SourcePage:
    physical: int
    text: str
    method: str
    image: str | None
    issue: str | None


@dataclass
class PageAudit:
    physical: int
    status: str
    printed_page: Any
    source_method: str
    source_chars: int
    source_tokens: int
    native_tokens: int
    matched_tokens: int
    recall: float | None
    marker_count: int
    marker_kinds: list[str]
    ocr_residue: list[str]
    exemption: str | None
    context_matched_tokens: int = 0
    context_recall: float | None = None


def resolve_path(root: Path, value: str | Path) -> Path:
    path = Path(value)
    return path if path.is_absolute() else root / path


def display_path(path: Path, root: Path) -> str:
    try:
        return str(path.relative_to(root))
    except ValueError:
        return str(path)


def strip_tex_comments(text: str) -> str:
    kept: list[str] = []
    for line in text.splitlines():
        result: list[str] = []
        backslashes = 0
        for character in line:
            if character == "%" and backslashes % 2 == 0:
                break
            result.append(character)
            if character == "\\":
                backslashes += 1
            else:
                backslashes = 0
        kept.append("".join(result))
    return "\n".join(kept)


def normalize_unicode(text: str) -> str:
    text = unicodedata.normalize("NFKC", text)
    replacements = {
        "\u2018": "'",
        "\u2019": "'",
        "\u201b": "'",
        "\u201c": '"',
        "\u201d": '"',
        "\u201f": '"',
        "\u00a0": " ",
        "\u00ad": "",
        "\u200b": "",
        "\u200c": "",
        "\u200d": "",
        "\u2026": "...",
        "\u2013": "-",
        "\u2014": "-",
        "\u2212": "-",
        "\ufb00": "ff",
        "\ufb01": "fi",
        "\ufb02": "fl",
        "\ufb03": "ffi",
        "\ufb04": "ffl",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    text = re.sub(r"(?<=[A-Za-z])-\s*\n\s*(?=[A-Za-z])", "", text)
    return text.replace("\f", "\n")


def _save_text_commands(text: str) -> tuple[str, list[str]]:
    fragments: list[str] = []
    pattern = re.compile(
        r"\\(?:text|mbox|textrm|textit|textbf|textsf|emph|underline|"
        r"operatorname)\s*\{([^{}]*)\}"
    )

    def replace(match: re.Match[str]) -> str:
        index = len(fragments)
        fragments.append(match.group(1))
        return f"\ue000{index}\ue001"

    return pattern.sub(replace, text), fragments


def mask_tex_math(text: str) -> str:
    text, fragments = _save_text_commands(text)

    def mask_match(match: re.Match[str]) -> str:
        body = match.group(0)
        kept = [fragments[int(index)] for index in re.findall(r"\ue000(\d+)\ue001", body)]
        return (" " + " ".join(kept) + " ") if kept else " "

    for pattern in (
        MATH_ENV,
        DISPLAY_DOLLAR,
        DISPLAY_BRACKET,
        INLINE_DOLLAR,
        INLINE_PAREN,
    ):
        text = pattern.sub(mask_match, text)
    for index, fragment in enumerate(fragments):
        text = text.replace(f"\ue000{index}\ue001", f" {fragment} ")
    return text


def visible_tex_prose(text: str) -> str:
    text = normalize_unicode(strip_tex_comments(text))
    text = mask_tex_math(text)
    text = re.sub(
        r"\\(?:label|ref|eqref|pageref|autoref|cite|footnotemark)"
        r"(?:\s*\[[^\]]*\])?\s*\{[^{}]*\}",
        " ",
        text,
    )
    text = re.sub(r"\\(?:begin|end)\s*\{[^{}]*\}", " ", text)
    text = re.sub(r"\\[A-Za-z@]+\*?(?:\s*\[[^\]]*\])?", " ", text)
    text = re.sub(r"\\(?:[,;:!]|\s)", " ", text)
    text = re.sub(r"\\([%$&#_{}])", r"\1", text)
    return text.replace("{", " ").replace("}", " ").replace("~", " ")


def prose_tokens(text: str) -> list[str]:
    tokens: list[str] = []
    for raw in WORD.findall(normalize_unicode(text)):
        token = raw.casefold().strip("'")
        if len(token) < 2 or any(character.isdigit() for character in token):
            continue
        tokens.append(token)
    return tokens


def normalize_printed(value: Any) -> str | None:
    if value is None:
        return None
    if isinstance(value, list):
        return ",".join(sorted(item for item in (normalize_printed(v) for v in value) if item))
    value = str(value).strip()
    if not value:
        return None
    if value.isdigit():
        return str(int(value))
    return value.casefold()


def load_dispositions(path: Path, expected: int) -> tuple[dict[int, dict[str, Any]], list[str]]:
    issues: list[str] = []
    records: dict[int, dict[str, Any]] = {}
    if not path.is_file():
        return {}, [f"missing page disposition ledger: {path}"]
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except OSError as error:
        return {}, [f"cannot read page disposition ledger {path}: {error}"]
    for index, line in enumerate(lines, start=1):
        if not line.strip():
            continue
        try:
            record = json.loads(line)
        except json.JSONDecodeError as error:
            issues.append(f"ledger line {index} is not JSON: {error}")
            continue
        try:
            page = int(record["pdf_page"])
        except (KeyError, TypeError, ValueError):
            issues.append(f"ledger line {index} has no integer pdf_page")
            continue
        if page in records:
            issues.append(f"duplicate disposition for PDF page {page}")
        records[page] = record
    expected_pages = set(range(1, expected + 1))
    missing = sorted(expected_pages - set(records))
    extra = sorted(set(records) - expected_pages)
    if missing:
        issues.append("ledger missing PDF pages: " + ", ".join(map(str, missing)))
    if extra:
        issues.append("ledger has out-of-range PDF pages: " + ", ".join(map(str, extra)))
    if len(records) != expected:
        issues.append(f"ledger has {len(records)} records; expected {expected}")
    for page, record in records.items():
        status = str(record.get("status", "")).strip()
        if not status:
            issues.append(f"ledger PDF page {page} has no status")
        if not str(record.get("reason", "")).strip():
            issues.append(f"ledger PDF page {page} has no reason")
    return records, issues


def resolve_tex_target(value: str, latex: Path) -> Path:
    value = value.strip()
    path = Path(value)
    if path.suffix == "":
        path = path.with_suffix(".tex")
    return latex / path


def collect_assembled_files(master: Path, latex: Path) -> tuple[list[Path], list[str]]:
    ordered: list[Path] = []
    missing: list[str] = []
    queue = [master]
    seen: set[Path] = set()
    while queue:
        path = queue.pop(0).resolve()
        if path in seen:
            continue
        seen.add(path)
        if not path.is_file():
            missing.append(display_path(path, ROOT))
            continue
        ordered.append(path)
        try:
            text = strip_tex_comments(path.read_text(encoding="utf-8"))
        except OSError as error:
            missing.append(f"{display_path(path, ROOT)}: {error}")
            continue
        calls = ASSEMBLY_CALL.findall(text) if path == master.resolve() else INPUT_CALL.findall(text)
        for value in calls:
            target = resolve_tex_target(value, latex).resolve()
            if target not in seen:
                queue.append(target)
    return ordered, missing


def find_marker_files(latex: Path) -> set[Path]:
    found: set[Path] = set()
    for path in latex.rglob("*.tex"):
        try:
            if PAGE_MARKER.search(path.read_text(encoding="utf-8")):
                found.add(path.resolve())
        except OSError:
            continue
    return found


def collect_segments(paths: Sequence[Path]) -> tuple[list[Segment], list[str]]:
    segments: list[Segment] = []
    issues: list[str] = []
    for path in paths:
        try:
            text = path.read_text(encoding="utf-8")
        except OSError as error:
            issues.append(f"cannot read assembled TeX {display_path(path, ROOT)}: {error}")
            continue
        matches = list(PAGE_MARKER.finditer(text))
        for index, match in enumerate(matches):
            end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
            marker = Marker(
                physical=int(match.group("physical")),
                printed=match.group("printed"),
                kind=match.group("kind"),
                identifier=match.group("identifier"),
                path=path,
                line=text.count("\n", 0, match.start()) + 1,
            )
            segments.append(Segment(marker, text[match.end() : end]))
    return segments, issues


def pdf_page_count(path: Path) -> tuple[int | None, str | None]:
    try:
        result = subprocess.run(
            ["pdfinfo", str(path)],
            check=False,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=60,
        )
    except (FileNotFoundError, subprocess.TimeoutExpired) as error:
        return None, f"could not run pdfinfo: {error}"
    if result.returncode:
        return None, result.stderr.strip() or "pdfinfo failed"
    match = re.search(r"^Pages:\s*(\d+)\s*$", result.stdout, re.MULTILINE)
    return (int(match.group(1)), None) if match else (None, "pdfinfo returned no page count")


def sha256(path: Path) -> str | None:
    if not path.is_file():
        return None
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def text_sha256(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def warning_signature(pages: Sequence[PageAudit]) -> str:
    payload = [
        {
            "pdf_page": page.physical,
            "printed_page": page.printed_page,
            "source_method": page.source_method,
            "source_tokens": page.source_tokens,
            "native_tokens": page.native_tokens,
            "matched_tokens": page.matched_tokens,
            "recall": page.recall,
            "context_matched_tokens": page.context_matched_tokens,
            "context_recall": page.context_recall,
            "marker_count": page.marker_count,
            "marker_kinds": page.marker_kinds,
            "ocr_residue": page.ocr_residue,
            "exemption": page.exemption,
        }
        for page in pages
    ]
    serialized = json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return text_sha256(serialized)


def check_low_recall_dispositions(
    path: Path,
    review_path: Path,
    report_path: Path,
    source_hash: str | None,
    warning_pages: Sequence[PageAudit],
    warning_recall: float,
    root: Path,
) -> tuple[dict[str, Any], list[str]]:
    """Check the reviewed warning pages against the current audit state."""
    issues: list[str] = []
    current_pages = [page.physical for page in warning_pages]
    current_signature = warning_signature(warning_pages)
    checked: dict[str, Any] = {
        "path": display_path(path, root),
        "review": display_path(review_path, root),
        "report": display_path(report_path, root),
        "warning_pages": current_pages,
        "warning_signature": current_signature,
        "checked": False,
    }
    if not path.is_file():
        issues.append(f"missing low-recall disposition file: {display_path(path, root)}")
        return checked, issues
    try:
        record = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        issues.append(f"cannot read low-recall disposition file {display_path(path, root)}: {error}")
        return checked, issues
    if not isinstance(record, dict):
        issues.append("low-recall disposition file must contain a JSON object")
        return checked, issues
    if record.get("schema") != "pct-transcription-low-recall/v1":
        issues.append("low-recall disposition schema is missing or unsupported")
    if record.get("report") != display_path(report_path, root):
        issues.append("low-recall dispositions do not identify the current report")
    if record.get("review") != display_path(review_path, root):
        issues.append("low-recall dispositions do not identify the required review")
    if record.get("source_sha256") != source_hash:
        issues.append("low-recall dispositions have a stale source SHA-256")
    recorded_threshold = record.get("warning_recall")
    if recorded_threshold != warning_recall:
        issues.append(
            f"low-recall disposition threshold {recorded_threshold!r} differs from current {warning_recall!r}"
        )
    if record.get("warning_signature") != current_signature:
        issues.append("low-recall dispositions do not match the current warning-page report")
    entries = record.get("pages")
    if not isinstance(entries, list):
        issues.append("low-recall disposition pages must be a list")
        entries = []
    entry_pages: list[int] = []
    active_entry_pages: list[int] = []
    for index, entry in enumerate(entries, start=1):
        if not isinstance(entry, dict):
            issues.append(f"low-recall disposition entry {index} is not an object")
            continue
        try:
            page = int(entry["pdf_page"])
        except (KeyError, TypeError, ValueError):
            issues.append(f"low-recall disposition entry {index} has no integer pdf_page")
            continue
        entry_pages.append(page)
        if entry.get("current_warning", True):
            active_entry_pages.append(page)
        if entry.get("status") != "resolved":
            issues.append(f"low-recall disposition PDF page {page} is not resolved")
        if not str(entry.get("category", "")).strip():
            issues.append(f"low-recall disposition PDF page {page} has no category")
        if not str(entry.get("evidence", "")).strip():
            issues.append(f"low-recall disposition PDF page {page} has no evidence")
    if len(entry_pages) != len(set(entry_pages)):
        issues.append("low-recall disposition pages contain duplicates")
    if sorted(active_entry_pages) != current_pages:
        issues.append(
            "low-recall active disposition pages differ from current warnings: "
            f"recorded {sorted(active_entry_pages)}, current {current_pages}"
        )
    if not review_path.is_file():
        issues.append(f"missing low-recall audit review: {display_path(review_path, root)}")
    else:
        try:
            review_text = review_path.read_text(encoding="utf-8")
        except OSError as error:
            issues.append(f"cannot read low-recall audit review {display_path(review_path, root)}: {error}")
        else:
            if "Unresolved blockers: none" not in review_text:
                issues.append("low-recall audit review has no resolved-blocker disposition")
    checked["checked"] = not issues
    checked["issues"] = issues
    return checked, issues


def source_text_candidates(directory: Path, page: int) -> list[Path]:
    return [
        directory / f"page-{page:04d}.txt",
        directory / f"page-{page:03d}.txt",
        directory / f"{page:04d}.txt",
        directory / f"{page:03d}.txt",
        directory / f"{page}.txt",
    ]


def source_image_candidates(directory: Path, page: int) -> list[Path]:
    return [
        directory / f"pdf-{page:03d}.jpg",
        directory / f"pdf-{page:03d}.jpeg",
        directory / f"pdf-{page:03d}.png",
        directory / f"page-{page:03d}.jpg",
    ]


def run_text_command(command: list[str], timeout: int = 60) -> tuple[str, str | None]:
    try:
        result = subprocess.run(
            command,
            check=False,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=timeout,
        )
    except (FileNotFoundError, subprocess.TimeoutExpired) as error:
        return "", str(error)
    if result.returncode:
        return result.stdout, result.stderr.strip() or f"command failed with status {result.returncode}"
    return result.stdout, None


def extract_source_page(
    page: int,
    source_pdf: Path,
    source_text_dir: Path | None,
    source_pages_dir: Path,
    pdftotext: str,
    tesseract: str | None,
    min_layer_tokens: int,
) -> SourcePage:
    image = next((candidate for candidate in source_image_candidates(source_pages_dir, page) if candidate.is_file()), None)
    if source_text_dir is not None:
        candidate = next((path for path in source_text_candidates(source_text_dir, page) if path.is_file()), None)
        if candidate is None:
            text, issue = "", f"missing extracted source text for PDF page {page}"
        else:
            try:
                text, issue = candidate.read_text(encoding="utf-8", errors="replace"), None
            except OSError as error:
                text, issue = "", f"cannot read {candidate}: {error}"
        method = "text-dir"
    else:
        text, issue = run_text_command(
            [pdftotext, "-layout", "-f", str(page), "-l", str(page), str(source_pdf), "-"],
            timeout=60,
        )
        method = "pdftotext"

    if len(prose_tokens(text)) < min_layer_tokens and tesseract and image is not None:
        ocr_text, ocr_issue = run_text_command(
            [tesseract, str(image), "stdout", "--psm", "3"],
            timeout=45,
        )
        if ocr_text.strip() or not text.strip():
            text, method = ocr_text, "tesseract"
            issue = ocr_issue
    if not text.strip() and issue is None:
        issue = f"source text is empty for PDF page {page}"
    return SourcePage(page, text, method if text.strip() else "empty", str(image) if image else None, issue)


def ocr_residue(text: str) -> list[str]:
    findings: list[str] = []
    if re.search(r"[\ufffd\u25a1\u25a3]", text):
        findings.append("replacement or missing-glyph character")
    if re.search(r"\(cid:\s*\d+\)|<0x[0-9A-Fa-f]+>", text):
        findings.append("embedded character-code artifact")
    if re.search(r"[\x00-\x08\x0b\x0e-\x1f\x7f]", text):
        findings.append("control character")
    if re.search(r"([^\w\s])\1{4,}", text):
        findings.append("repeated punctuation run")
    mixed = []
    for token in re.findall(r"\S+", text):
        if len(token) >= 6 and re.search(r"[A-Za-z]", token) and len(re.findall(r"\d", token)) >= 2:
            mixed.append(token[:32])
    if mixed:
        findings.append("mixed alphanumeric token(s): " + ", ".join(mixed[:3]))
    for line in text.replace("\f", " ").splitlines():
        compact = re.sub(r"\s+", "", line)
        if len(compact) >= 16:
            punctuation = sum(not character.isalnum() for character in compact) / len(compact)
            if punctuation >= 0.72:
                findings.append("punctuation-heavy OCR line: " + re.sub(r"\s+", " ", line).strip()[:70])
                break
    return findings


def heading_candidates(source_text: str, minimum_tokens: int) -> list[str]:
    candidates: list[str] = []
    seen: set[tuple[str, ...]] = set()
    known_single = {"solution", "hint", "preface", "contents", "references", "index", "bibliography"}
    known_prefix = re.compile(
        r"(?i)^(?:chapter|section|part|problem|solution|hint|exercise|question|appendix|figure|table|[a-z]\.)\b"
    )
    for raw_line in normalize_unicode(source_text).splitlines():
        line = re.sub(r"\s+", " ", raw_line).strip()
        if not line or len(line) > 120 or re.fullmatch(r"[\d\s-]+", line):
            continue
        tokens = prose_tokens(line)
        lower = line.casefold().rstrip(" .:")
        known = bool(known_prefix.match(line)) or lower in known_single
        if not tokens or (len(tokens) < minimum_tokens and not known) or len(tokens) > 14:
            continue
        letters = re.findall(r"[A-Za-z]+", line)
        first = next((character for character in line if character.isalpha()), "")
        title_case_ratio = sum(token[0].isupper() for token in letters) / max(1, len(letters))
        all_caps = bool(letters) and line.upper() == line
        terminal_sentence = line.endswith((".", ",", ";", ":", "?", "!"))
        # OCR line breaks are unreliable on this scan.  Restrict the report to
        # unmistakable structural headings instead of treating ordinary
        # sentence fragments as missing headings.
        if not (known or all_caps):
            continue
        key = tuple(tokens)
        if key not in seen:
            seen.add(key)
            candidates.append(line)
    return candidates


def detect_missing_headings(source_text: str, native_text: str, minimum_tokens: int) -> list[str]:
    native = prose_tokens(visible_tex_prose(native_text))
    for match in HEADING_COMMAND.finditer(native_text):
        native.extend(prose_tokens(match.group("body")))
    missing: list[str] = []
    for candidate in heading_candidates(source_text, minimum_tokens):
        phrase = prose_tokens(candidate)
        if phrase and not any(native[index : index + len(phrase)] == phrase for index in range(len(native) - len(phrase) + 1)):
            missing.append(candidate)
    return missing


def coverage(source_text: str, native_text: str, minimum_tokens: int) -> tuple[list[str], list[str], int, float | None]:
    source_tokens = prose_tokens(source_text)
    native_tokens = prose_tokens(visible_tex_prose(native_text))
    native_counts = Counter(native_tokens)
    matched = sum(min(count, native_counts[token]) for token, count in Counter(source_tokens).items())
    recall = matched / len(source_tokens) if len(source_tokens) >= minimum_tokens else None
    return source_tokens, native_tokens, matched, recall


def repeated_page_pairs(page_tokens: dict[int, Sequence[str]], minimum_tokens: int, threshold: float) -> list[dict[str, Any]]:
    eligible = {page: list(tokens) for page, tokens in page_tokens.items() if len(tokens) >= minimum_tokens}
    pairs: list[dict[str, Any]] = []
    fingerprints: dict[tuple[str, ...], list[int]] = defaultdict(list)
    for page, tokens in eligible.items():
        fingerprints[tuple(tokens)].append(page)
    seen: set[tuple[int, int]] = set()
    for pages in fingerprints.values():
        for left_index, left in enumerate(pages):
            for right in pages[left_index + 1 :]:
                pair = (min(left, right), max(left, right))
                seen.add(pair)
                pairs.append({"left": pair[0], "right": pair[1], "similarity": 1.0, "kind": "exact"})
    ordered = sorted(eligible)
    for left_index, left in enumerate(ordered):
        for right in ordered[left_index + 1 :]:
            pair = (left, right)
            if pair in seen:
                continue
            ratio = difflib.SequenceMatcher(None, eligible[left], eligible[right], autojunk=False).ratio()
            if ratio >= threshold:
                seen.add(pair)
                pairs.append({"left": left, "right": right, "similarity": round(ratio, 6), "kind": "near"})
    return sorted(pairs, key=lambda item: (-item["similarity"], item["left"], item["right"]))


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--strict", action="store_true", help="fail on evidence-backed severe gaps or unresolved exemptions")
    parser.add_argument("--root", type=Path, default=ROOT, help="PCT project root")
    parser.add_argument("--source-pdf", type=Path, default=None)
    parser.add_argument("--source-text-dir", type=Path, default=None)
    parser.add_argument("--source-pages-dir", type=Path, default=None)
    parser.add_argument("--dispositions", type=Path, default=None)
    parser.add_argument("--master", type=Path, default=None)
    parser.add_argument("--report", type=Path, default=None)
    parser.add_argument("--low-recall-dispositions", type=Path, default=None)
    parser.add_argument("--low-recall-review", type=Path, default=None)
    parser.add_argument("--pdftotext", default="pdftotext")
    parser.add_argument("--tesseract", default="tesseract")
    parser.add_argument("--expected-pages", type=int, default=EXPECTED_PAGES)
    parser.add_argument("--warn-recall", type=float, default=0.70)
    parser.add_argument("--severe-recall", type=float, default=0.45)
    parser.add_argument("--minimum-eligible-tokens", type=int, default=20)
    parser.add_argument("--minimum-layer-tokens", type=int, default=8)
    parser.add_argument("--heading-min-tokens", type=int, default=2)
    parser.add_argument("--repeat-similarity", type=float, default=0.98)
    parser.add_argument("--repeat-min-tokens", type=int, default=25)
    parser.add_argument("--worst-pages", type=int, default=10)
    args = parser.parse_args(argv)
    if not 0 <= args.severe_recall <= args.warn_recall <= 1:
        parser.error("require 0 <= severe-recall <= warn-recall <= 1")
    if args.minimum_eligible_tokens < 1 or args.minimum_layer_tokens < 1 or args.repeat_min_tokens < 1:
        parser.error("token thresholds must be positive")
    return args


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_args(argv)
    root = args.root.resolve()
    source_pdf = resolve_path(root, args.source_pdf or SOURCE)
    source_text_dir = resolve_path(root, args.source_text_dir) if args.source_text_dir else None
    source_pages_dir = resolve_path(root, args.source_pages_dir or SOURCE_PAGES)
    dispositions_path = resolve_path(root, args.dispositions or DISPOSITIONS)
    master = resolve_path(root, args.master or MASTER)
    report_path = resolve_path(root, args.report or DEFAULT_REPORT)
    low_recall_dispositions_path = resolve_path(
        root, args.low_recall_dispositions or DEFAULT_LOW_RECALL_DISPOSITIONS
    )
    low_recall_review_path = resolve_path(root, args.low_recall_review or DEFAULT_LOW_RECALL_REVIEW)
    pdftotext = args.pdftotext
    tesseract = shutil.which(args.tesseract)

    structural: list[str] = []
    records, disposition_issues = load_dispositions(dispositions_path, args.expected_pages)
    structural.extend(disposition_issues)
    included = {page for page, record in records.items() if record.get("status") == INCLUDED_STATUS}
    if not included and not disposition_issues:
        structural.append("page disposition ledger has no transcribed pages")

    actual_pages, page_issue = pdf_page_count(source_pdf)
    if page_issue:
        structural.append(f"source PDF page count unavailable: {page_issue}")
    elif actual_pages != args.expected_pages:
        structural.append(f"source PDF page count is {actual_pages}; expected {args.expected_pages}")

    assembled, assembly_issues = collect_assembled_files(master, LATEX)
    structural.extend(f"assembly: {issue}" for issue in assembly_issues)
    marker_files = find_marker_files(LATEX)
    assembled_set = set(assembled)
    unassembled_marker_files = sorted(marker_files - assembled_set)
    if unassembled_marker_files:
        structural.append(
            "PCT-SOURCE markers occur outside master assembly: "
            + ", ".join(display_path(path, root) for path in unassembled_marker_files)
        )

    segments, segment_issues = collect_segments(assembled)
    structural.extend(segment_issues)
    by_page: dict[int, list[Segment]] = defaultdict(list)
    for segment in segments:
        page = segment.marker.physical
        by_page[page].append(segment)
        if not 1 <= page <= args.expected_pages:
            structural.append(
                f"marker page {page} is outside 1-{args.expected_pages} at "
                f"{display_path(segment.marker.path, root)}:{segment.marker.line}"
            )
        record = records.get(page)
        if record and record.get("status") == INCLUDED_STATUS:
            expected_prints = record.get("printed_page")
            accepted = {normalize_printed(expected_prints)} if not isinstance(expected_prints, list) else {normalize_printed(item) for item in expected_prints}
            if accepted and normalize_printed(segment.marker.printed) not in accepted:
                structural.append(
                    f"printed folio mismatch on PDF page {page}: marker {segment.marker.printed!r}, "
                    f"ledger {expected_prints!r} at {display_path(segment.marker.path, root)}:{segment.marker.line}"
                )

    missing_markers = sorted(included - set(by_page))
    if missing_markers and by_page:
        structural.append("missing native markers for transcribed PDF pages: " + ", ".join(map(str, missing_markers)))
    invalid_markers = sorted(set(by_page) - set(records))
    if invalid_markers:
        structural.append("native markers have no disposition: " + ", ".join(map(str, invalid_markers)))

    source_pages: dict[int, SourcePage] = {}
    extraction_issues: list[str] = []
    if not source_pdf.is_file():
        extraction_issues.append(f"missing canonical source PDF: {source_pdf}")
    for page in sorted(included):
        result = extract_source_page(
            page,
            source_pdf,
            source_text_dir,
            source_pages_dir,
            pdftotext,
            tesseract,
            args.minimum_layer_tokens,
        )
        source_pages[page] = result
        if result.issue and not result.text.strip():
            extraction_issues.append(result.issue)
    structural.extend(extraction_issues)

    if not by_page:
        print("No inline PCT-SOURCE markers; skipping page-token coverage against the scan.")
        report_path.parent.mkdir(parents=True, exist_ok=True)
        report_path.write_text(
            json.dumps(
                {
                    "schema": "pct-transcription-audit/v1",
                    "mode": "strict" if args.strict else "draft",
                    "result": "PASS" if not structural else "FAIL",
                    "inline_markers": 0,
                    "structural_issues": structural,
                },
                indent=2,
            )
            + "\n",
            encoding="utf-8",
        )
        if structural:
            print("STRUCTURAL ISSUES")
            for issue in structural[:40]:
                print(f"  - {issue}")
        if args.strict and structural:
            print(f"RESULT: FAIL ({len(structural)} failure(s))")
            return 1
        print("RESULT: PASS")
        return 0

    page_audits: list[PageAudit] = []
    severe: list[dict[str, Any]] = []
    unresolved: list[dict[str, Any]] = []
    missing_headings: list[dict[str, Any]] = []
    source_tokens_by_page: dict[int, list[str]] = {}
    native_tokens_by_page: dict[int, list[str]] = {}

    for page in sorted(included):
        source = source_pages.get(page, SourcePage(page, "", "empty", None, "source page was not extracted"))
        page_segments = by_page.get(page, [])
        native_text = "\n".join(segment.text for segment in page_segments)
        source_tokens, native_tokens, matched, recall = coverage(source.text, native_text, args.minimum_eligible_tokens)
        source_tokens_by_page[page] = source_tokens
        native_tokens_by_page[page] = native_tokens
        kinds = sorted({segment.marker.kind for segment in page_segments})
        exemption: str | None = None
        if not source.text.strip() or len(source_tokens) < args.minimum_eligible_tokens:
            if source.image and page_segments and (native_tokens or set(kinds) <= LAYOUT_ONLY_KINDS):
                exemption = "sparse OCR resolved by source image and native marker content"
            else:
                exemption = "sparse OCR has no sufficient native or source evidence"
                unresolved.append(
                    {
                        "pdf_page": page,
                        "reason": exemption,
                        "source_method": source.method,
                        "source_image": source.image,
                        "marker_kinds": kinds,
                    }
                )
        title_exemption = "title" in kinds and not native_tokens
        if title_exemption:
            exemption = "title treatment is assembled in master.tex outside the page marker"
            unresolved[:] = [item for item in unresolved if item["pdf_page"] != page]
        missing_headings.extend(
            {"pdf_page": page, "heading": heading}
            for heading in detect_missing_headings(source.text, native_text, args.heading_min_tokens)
        )
        page_audits.append(
            PageAudit(
                physical=page,
                status=str(records.get(page, {}).get("status", "")),
                printed_page=records.get(page, {}).get("printed_page"),
                source_method=source.method,
                source_chars=len(source.text),
                source_tokens=len(source_tokens),
                native_tokens=len(native_tokens),
                matched_tokens=matched,
                recall=round(recall, 6) if recall is not None else None,
                marker_count=len(page_segments),
                marker_kinds=kinds,
                ocr_residue=ocr_residue(source.text),
                exemption=exemption,
            )
        )

    # Reflow can move the tail of a source paragraph across a native page
    # marker.  Use adjacent native pages as corroborating evidence before
    # calling a low direct recall a likely omission.  A genuine omission stays
    # low after this boundary-aware check.
    for index, page in enumerate(page_audits):
        context_tokens: list[str] = []
        for neighbor in page_audits[max(0, index - 1) : min(len(page_audits), index + 2)]:
            context_tokens.extend(native_tokens_by_page.get(neighbor.physical, []))
        source_tokens = source_tokens_by_page.get(page.physical, [])
        context_counts = Counter(context_tokens)
        context_matched = sum(
            min(count, context_counts[token]) for token, count in Counter(source_tokens).items()
        )
        context_recall = (
            context_matched / len(source_tokens)
            if len(source_tokens) >= args.minimum_eligible_tokens
            else None
        )
        page.context_matched_tokens = context_matched
        page.context_recall = round(context_recall, 6) if context_recall is not None else None
        title_exemption = bool(page.exemption and page.exemption.startswith("title treatment"))
        if (
            not title_exemption
            and page.recall is not None
            and page.recall < args.severe_recall
            and context_recall is not None
            and context_recall < args.severe_recall
        ):
            context_ratio = len(context_tokens) / max(1, len(source_tokens))
            if context_ratio < 0.65 or context_recall < 0.30:
                severe.append(
                    {
                        "pdf_page": page.physical,
                        "recall": page.recall,
                        "context_recall": round(context_recall, 6),
                        "matched_tokens": page.matched_tokens,
                        "context_matched_tokens": context_matched,
                        "source_tokens": len(source_tokens),
                        "native_tokens": page.native_tokens,
                        "context_native_ratio": round(context_ratio, 6),
                        "evidence": "source OCR has enough prose and adjacent native pages do not recover the direct coverage gap",
                    }
                )

    source_repeats = repeated_page_pairs(source_tokens_by_page, args.repeat_min_tokens, args.repeat_similarity)
    native_repeats = repeated_page_pairs(native_tokens_by_page, args.repeat_min_tokens, args.repeat_similarity)
    scored = [page for page in page_audits if page.recall is not None]
    warnings = [page for page in scored if page.recall is not None and page.recall < args.warn_recall]
    low_recall_checked, low_recall_issues = check_low_recall_dispositions(
        low_recall_dispositions_path,
        low_recall_review_path,
        report_path,
        sha256(source_pdf),
        warnings,
        args.warn_recall,
        root,
    )
    strict_failures = list(structural)
    strict_failures.extend(
        f"severe prose coverage gap on PDF page {item['pdf_page']}: direct recall {item['recall']:.3f}, "
        f"boundary-aware recall {item['context_recall']:.3f} "
        f"({item['matched_tokens']}/{item['source_tokens']} direct; "
        f"{item['context_matched_tokens']} boundary-aware)"
        for item in severe
    )
    strict_failures.extend(
        f"unresolved sparse-OCR exemption on PDF page {item['pdf_page']}: {item['reason']}"
        for item in unresolved
    )
    if args.strict:
        strict_failures.extend(f"low-recall disposition: {issue}" for issue in low_recall_issues)

    report: dict[str, Any] = {
        "schema": "pct-transcription-audit/v1",
        "mode": "strict" if args.strict else "draft",
        "result": "PASS" if not strict_failures else "FAIL",
        "source": {
            "path": display_path(source_pdf, root),
            "sha256": sha256(source_pdf),
            "expected_pages": args.expected_pages,
            "actual_pages": actual_pages,
            "source_pages_dir": display_path(source_pages_dir, root),
        },
        "dispositions": {
            "path": display_path(dispositions_path, root),
            "records": len(records),
            "included_pages": sorted(included),
            "status_counts": dict(Counter(str(record.get("status", "")) for record in records.values())),
        },
        "assembly": {
            "master": display_path(master, root),
            "files": [display_path(path, root) for path in assembled],
            "missing": assembly_issues,
            "unassembled_marker_files": [display_path(path, root) for path in unassembled_marker_files],
        },
        "thresholds": {
            "warning_recall": args.warn_recall,
            "severe_recall": args.severe_recall,
            "minimum_eligible_tokens": args.minimum_eligible_tokens,
            "minimum_layer_tokens": args.minimum_layer_tokens,
            "repeat_similarity": args.repeat_similarity,
            "repeat_min_tokens": args.repeat_min_tokens,
        },
        "summary": {
            "included_pages": len(included),
            "pages_with_markers": len(set(by_page) & included),
            "pages_scored": len(scored),
            "warning_pages": len(warnings),
            "mean_recall": round(mean(page.recall for page in scored if page.recall is not None), 6) if scored else None,
            "median_recall": round(median(page.recall for page in scored if page.recall is not None), 6) if scored else None,
            "severe_gaps": len(severe),
            "unresolved_exemptions": len(unresolved),
            "ocr_residue_pages": sum(bool(page.ocr_residue) for page in page_audits),
        },
        "low_recall_dispositions": low_recall_checked,
        "pages": [asdict(page) for page in page_audits],
        "findings": {
            "structural_issues": structural,
            "severe_gaps": severe,
            "unresolved_exemptions": unresolved,
            "missing_headings": missing_headings,
            "source_repeated_pages": source_repeats,
            "native_repeated_pages": native_repeats,
            "low_recall_disposition_issues": low_recall_issues,
            "strict_failures": strict_failures,
        },
    }
    try:
        report_path.parent.mkdir(parents=True, exist_ok=True)
        report_path.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    except OSError as error:
        print(f"Could not write machine-readable report {report_path}: {error}", file=sys.stderr)
        return 1

    print(f"Canonical source pages: {actual_pages if actual_pages is not None else 'unknown'} (expected {args.expected_pages})")
    print(f"Native assembly: {len(assembled)} files; included page markers {len(set(by_page) & included)}/{len(included)}")
    if scored:
        print(
            f"Page recall: {len(scored)} scored; mean {mean(page.recall for page in scored if page.recall is not None):.3f}; "
            f"median {median(page.recall for page in scored if page.recall is not None):.3f}; warnings {len(warnings)}"
        )
        print("Worst pages by prose-token recall:")
        for page in sorted(scored, key=lambda item: (item.recall or 0, item.physical))[: args.worst_pages]:
            print(f"  p{page.physical:03d}: {page.recall:.3f} ({page.matched_tokens}/{page.source_tokens})")
    else:
        print("Page recall: no pages reached the eligible-token threshold")
    if severe:
        print(f"Severe likely omissions: {len(severe)}")
    if unresolved:
        print(f"Unresolved exemptions: {len(unresolved)}")
    if missing_headings:
        print(f"Possible missing headings: {len(missing_headings)}")
    residue_pages = [page for page in page_audits if page.ocr_residue]
    if residue_pages:
        print(f"Pages with detected OCR residue: {len(residue_pages)} (reported, source images remain the authority)")
    if structural:
        print("Structural findings:")
        for issue in structural[:40]:
            print(f"  - {issue}")
    if args.strict and strict_failures:
        print("Strict audit failures:")
        for issue in strict_failures[:40]:
            print(f"  - {issue}")
    elif strict_failures:
        print(f"Strict-mode findings: {len(strict_failures)}; rerun with --strict to fail on them")
    if args.strict and strict_failures:
        print(f"RESULT: FAIL ({len(strict_failures)} failure(s))")
        return 1
    print("RESULT: PASS" if not args.strict else "RESULT: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
