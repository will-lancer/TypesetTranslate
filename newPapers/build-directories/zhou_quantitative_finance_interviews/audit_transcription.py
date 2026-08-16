#!/usr/bin/env python3
"""Audit source-page fidelity for the native Zhou JHEP transcription.

The source is a 212-page scan whose OCR layer is only a comparison aid.  This
audit extracts that layer one physical page at a time, joins each native TeX
segment to its ``ZHOU-SOURCE-PAGE`` marker, and compares normalized prose.  TeX
math is removed from the comparison while text inside ``\text{...}`` remains
visible.  The audit also checks the page map, likely headings, repeated source
pages, and common OCR residue.

The default run is intentionally sequential.  It does not render or compile
the edition.  Use ``--strict`` when the transcription workers have stopped and
the complete native page set is expected.
"""

from __future__ import annotations

import argparse
import difflib
import re
import subprocess
import unicodedata
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
from statistics import mean, median
from typing import Sequence


ROOT = Path(__file__).resolve().parent
DEFAULT_SOURCE = Path("source") / "zhou-quantitative-finance-interviews.pdf"
DEFAULT_TRANSCRIPTION = Path("latex") / "transcription"
EXPECTED_PAGES = 212

# These dispositions mirror SOURCE_MAP.md.  Only INCLUDED pages are expected
# to have a native source-page marker and a page-level fidelity score.
INCLUDED_PAGES = (
    {5, 13, 14, 15}
    | set(range(17, 120))
    | set(range(121, 186))
    | set(range(187, 208))
    | set(range(209, 212))
)
REPLACED_PAGES = {1, 3, 7, 8, 9, 10, 11}
OMITTED_PAGES = {2, 4, 6, 12, 16, 120, 186, 208, 212}
FRONTMATTER_PAGES = {5, 13, 14, 15}

PAGE_MARKER = re.compile(
    r"^%\s*ZHOU-SOURCE-PAGE:\s*(?P<physical>\d+)\s+"
    r"PRINTED:\s*(?P<printed>FRONTMATTER|\d+)\s*$",
    re.MULTILINE,
)
WORD = re.compile(r"[A-Za-z0-9]+(?:['\u2019][A-Za-z0-9]+)*")

MATH_ENV = re.compile(
    r"\\begin\{(?P<env>equation\*?|align\*?|alignat\*?|gather\*?|"
    r"multline\*?|displaymath|math|array|matrix|pmatrix|bmatrix|cases)\}"
    r".*?\\end\{(?P=env)\}",
    re.DOTALL,
)
INLINE_DOLLAR = re.compile(
    r"(?<!\\)\$(?!\$).*?(?<!\\)\$(?!\$)", re.DOTALL
)
DISPLAY_DOLLAR = re.compile(
    r"(?<!\\)\$\$.*?(?<!\\)\$\$", re.DOTALL
)
INLINE_PAREN = re.compile(r"\\\(.*?\\\)", re.DOTALL)
DISPLAY_BRACKET = re.compile(r"\\\[.*?\\\]", re.DOTALL)

HEADING_COMMAND = re.compile(
    r"\\(?P<command>section|subsection|subsubsection|paragraph|"
    r"problem|hint|caption)\*?(?:\s*\[[^\]]*\])?\s*"
    r"\{(?P<body>[^{}\n]*)\}"
)
NO_ARGUMENT_HEADING = re.compile(r"\\(?P<command>solution|problem)\b")


@dataclass(frozen=True)
class Marker:
    physical: int
    printed: str
    path: Path
    line: int
    offset: int


@dataclass(frozen=True)
class Segment:
    marker: Marker
    text: str


@dataclass
class PageReport:
    physical: int
    source_tokens: list[str]
    native_tokens: list[str]
    matched: int
    recall: float | None

    @property
    def eligible(self) -> int:
        return len(self.source_tokens)


def resolve_path(root: Path, value: str | Path) -> Path:
    """Resolve a CLI path relative to the project root when needed."""

    path = Path(value)
    return path if path.is_absolute() else root / path


def display_path(path: Path, root: Path) -> str:
    try:
        return str(path.relative_to(root))
    except ValueError:
        return str(path)


def strip_tex_comments(text: str) -> str:
    """Remove unescaped TeX comments while preserving escaped percent signs."""

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
    """Normalize scan and TeX typography before tokenization."""

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
    # A hyphen at a scan line break is a word continuation.  Other hyphens
    # remain separators and therefore yield two comparable prose tokens.
    text = re.sub(r"(?<=[A-Za-z])-\s*\n\s*(?=[A-Za-z])", "", text)
    return text.replace("\f", "\n")


def _save_text_commands(text: str) -> tuple[str, list[str]]:
    """Protect prose commands before masking math regions."""

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
    """Mask TeX math while retaining text fragments embedded in math."""

    text, fragments = _save_text_commands(text)

    def mask_match(match: re.Match[str]) -> str:
        body = match.group(0)
        kept: list[str] = []
        for index in re.findall(r"\ue000(\d+)\ue001", body):
            kept.append(fragments[int(index)])
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
    """Return visible prose from a native TeX segment.

    Commands are removed after math is masked.  Their braced text remains, so
    headings, captions, footnotes, and problem statements participate in the
    source comparison.  Cross-reference arguments are removed because their
    generated numbers are not prose from the scanned page.
    """

    text = normalize_unicode(strip_tex_comments(text))
    text = mask_tex_math(text)
    text = re.sub(
        r"\\(?:label|ref|eqref|pageref|autoref|cite|footnotemark)"
        r"(?:\s*\[[^\]]*\])?\s*\{[^{}]*\}",
        " ",
        text,
    )
    text = re.sub(r"\\(?:begin|end)\s*\{[^{}]*\}", " ", text)
    # TeX command names and optional arguments are presentation instructions.
    text = re.sub(r"\\[A-Za-z@]+\*?(?:\s*\[[^\]]*\])?", " ", text)
    text = re.sub(r"\\(?:[,;:!]|\s)", " ", text)
    text = re.sub(r"\\([%$&#_{}])", r"\1", text)
    return text.replace("{", " ").replace("}", " ").replace("~", " ")


def prose_tokens(text: str) -> list[str]:
    """Normalize visible prose into comparable alphabetic tokens.

    Single-character words are excluded because they are overwhelmingly
    variables or diagram labels in this source.  Numeric and mixed numeric
    tokens never enter the denominator, which is the math exemption used by
    the page recall score.
    """

    text = normalize_unicode(text)
    tokens: list[str] = []
    for raw in WORD.findall(text):
        token = raw.casefold().strip("'")
        if len(token) < 2 or any(character.isdigit() for character in token):
            continue
        tokens.append(token)
    return tokens


def expected_printed(physical: int) -> str:
    return "FRONTMATTER" if physical in FRONTMATTER_PAGES else str(physical - 16)


def collect_segments(transcription: Path) -> tuple[list[Segment], list[str]]:
    """Read native chunks and split each at its page marker."""

    segments: list[Segment] = []
    issues: list[str] = []
    if not transcription.is_dir():
        return [], [f"missing transcription directory: {transcription}"]

    for path in sorted(transcription.glob("*.tex")):
        try:
            text = path.read_text(encoding="utf-8")
        except OSError as error:
            issues.append(f"cannot read {path}: {error}")
            continue
        matches = list(PAGE_MARKER.finditer(text))
        for index, match in enumerate(matches):
            physical = int(match.group("physical"))
            printed = match.group("printed")
            line = text.count("\n", 0, match.start()) + 1
            end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
            marker = Marker(physical, printed, path, line, match.start())
            segments.append(Segment(marker, text[match.end() : end]))
    return segments, issues


def source_text_file_candidates(directory: Path, physical: int) -> list[Path]:
    return [
        directory / f"page-{physical:04d}.txt",
        directory / f"page-{physical:03d}.txt",
        directory / f"{physical:04d}.txt",
        directory / f"{physical:03d}.txt",
        directory / f"{physical}.txt",
    ]


def pdf_page_count(pdfinfo: str, source: Path) -> tuple[int | None, str | None]:
    try:
        completed = subprocess.run(
            [pdfinfo, str(source)],
            check=False,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=60,
        )
    except (FileNotFoundError, subprocess.TimeoutExpired) as error:
        return None, f"could not run {pdfinfo}: {error}"
    if completed.returncode != 0:
        detail = completed.stderr.strip() or "no diagnostic"
        return None, f"{pdfinfo} failed for {source}: {detail}"
    match = re.search(r"^Pages:\s*(\d+)\s*$", completed.stdout, re.MULTILINE)
    if not match:
        return None, f"{pdfinfo} output did not contain a page count for {source}"
    return int(match.group(1)), None


def extract_source_pages(
    source_pdf: Path,
    source_text_dir: Path | None,
    pdftotext: str,
    pdfinfo: str,
    expected_pages: int,
) -> tuple[dict[int, str], list[str], int | None]:
    """Load text for every physical page, one page per pdftotext call."""

    pages: dict[int, str] = {}
    issues: list[str] = []
    actual_count: int | None = None

    if source_text_dir is None:
        if not source_pdf.is_file():
            return {}, [f"missing source PDF: {source_pdf}"], None
        actual_count, count_issue = pdf_page_count(pdfinfo, source_pdf)
        if count_issue:
            issues.append(count_issue)
        elif actual_count != expected_pages:
            issues.append(
                f"source PDF page count is {actual_count}, expected {expected_pages}"
            )
    elif not source_text_dir.is_dir():
        issues.append(f"missing source text directory: {source_text_dir}")

    for physical in range(1, expected_pages + 1):
        if source_text_dir is not None:
            candidates = source_text_file_candidates(source_text_dir, physical)
            path = next((candidate for candidate in candidates if candidate.is_file()), None)
            if path is None:
                issues.append(
                    f"missing extracted source text for physical page {physical}"
                )
                continue
            try:
                pages[physical] = path.read_text(encoding="utf-8", errors="replace")
            except OSError as error:
                issues.append(f"cannot read {path}: {error}")
            continue

        try:
            completed = subprocess.run(
                [
                    pdftotext,
                    "-layout",
                    "-f",
                    str(physical),
                    "-l",
                    str(physical),
                    str(source_pdf),
                    "-",
                ],
                check=False,
                capture_output=True,
                text=True,
                encoding="utf-8",
                errors="replace",
                timeout=60,
            )
        except (FileNotFoundError, subprocess.TimeoutExpired) as error:
            issues.append(f"could not extract source page {physical}: {error}")
            continue
        if completed.returncode != 0:
            detail = completed.stderr.strip() or "no diagnostic"
            issues.append(f"pdftotext failed on source page {physical}: {detail}")
            continue
        pages[physical] = completed.stdout

    return pages, issues, actual_count


def heading_candidates(source_text: str, minimum_tokens: int) -> list[str]:
    """Find short source lines that have the shape of printed headings."""

    candidates: list[str] = []
    seen: set[tuple[str, ...]] = set()
    known_single = {
        "solution",
        "hint",
        "preface",
        "notations",
        "contents",
        "references",
        "index",
    }
    known_prefix = re.compile(
        r"(?i)^(?:chapter|section|part|problem|solution|hint|exercise|"
        r"question|appendix|figure|table|[a-z]\.)\b"
    )
    for raw_line in normalize_unicode(source_text).splitlines():
        line = re.sub(r"\s+", " ", raw_line).strip()
        if not line or len(line) > 120 or re.fullmatch(r"[\d\s-]+", line):
            continue
        tokens = prose_tokens(line)
        if not tokens:
            continue
        lower = line.casefold().rstrip(" .:")
        known = bool(known_prefix.match(line)) or lower in known_single
        if len(tokens) < minimum_tokens and not known:
            continue
        if len(tokens) > 14:
            continue
        first = next((character for character in line if character.isalpha()), "")
        title_case_ratio = sum(
            token[0].isupper() for token in re.findall(r"[A-Za-z]+", line)
        ) / max(1, len(re.findall(r"[A-Za-z]+", line)))
        all_caps = any(character.isalpha() for character in line) and line.upper() == line
        terminal_sentence = line.endswith((".", ",", ";", ":", "?", "!"))
        looks_like_heading = (
            known
            or all_caps
            or (first.isupper() and not terminal_sentence and title_case_ratio >= 0.35)
        )
        if not looks_like_heading:
            continue
        key = tuple(tokens)
        if key in seen:
            continue
        seen.add(key)
        candidates.append(line)
    return candidates


def native_heading_tokens(text: str) -> list[str]:
    """Return structural heading labels that are not present as prose."""

    labels: list[str] = []
    for match in HEADING_COMMAND.finditer(text):
        labels.extend(prose_tokens(match.group("body")))
    for match in NO_ARGUMENT_HEADING.finditer(text):
        if match.group("command") == "solution":
            labels.append("solution")
        elif match.group("command") == "problem":
            labels.append("problem")
    return labels


def phrase_in_tokens(phrase: Sequence[str], tokens: Sequence[str]) -> bool:
    if not phrase or len(phrase) > len(tokens):
        return False
    width = len(phrase)
    return any(list(tokens[index : index + width]) == list(phrase) for index in range(len(tokens) - width + 1))


def detect_missing_headings(
    source_text: str,
    native_text: str,
    minimum_tokens: int,
) -> list[str]:
    native_text_tokens = prose_tokens(visible_tex_prose(native_text))
    native_text_tokens.extend(native_heading_tokens(native_text))
    missing: list[str] = []
    for candidate in heading_candidates(source_text, minimum_tokens):
        phrase = prose_tokens(candidate)
        if phrase and not phrase_in_tokens(phrase, native_text_tokens):
            missing.append(candidate)
    return missing


def coverage_report(
    physical: int,
    source_text: str,
    native_text: str,
    minimum_tokens: int,
) -> PageReport:
    source_tokens = prose_tokens(source_text)
    native_tokens = prose_tokens(visible_tex_prose(native_text))
    native_counts = Counter(native_tokens)
    matched = sum(
        min(count, native_counts[token])
        for token, count in Counter(source_tokens).items()
    )
    recall = matched / len(source_tokens) if len(source_tokens) >= minimum_tokens else None
    return PageReport(physical, source_tokens, native_tokens, matched, recall)


def repeated_page_pairs(
    page_tokens: dict[int, Sequence[str]],
    minimum_tokens: int,
    threshold: float,
) -> list[tuple[int, int, float, str]]:
    """Find exact or near-identical nontrivial page text."""

    eligible = {
        page: list(tokens)
        for page, tokens in page_tokens.items()
        if len(tokens) >= minimum_tokens
    }
    pairs: list[tuple[int, int, float, str]] = []
    fingerprints: dict[tuple[str, ...], list[int]] = defaultdict(list)
    for page, tokens in eligible.items():
        fingerprints[tuple(tokens)].append(page)
    seen: set[tuple[int, int]] = set()
    for pages in fingerprints.values():
        for left_index, left in enumerate(pages):
            for right in pages[left_index + 1 :]:
                pair = (min(left, right), max(left, right))
                seen.add(pair)
                pairs.append((pair[0], pair[1], 1.0, "exact"))

    ordered = sorted(eligible)
    for left_index, left in enumerate(ordered):
        for right in ordered[left_index + 1 :]:
            pair = (left, right)
            if pair in seen:
                continue
            ratio = difflib.SequenceMatcher(
                None, eligible[left], eligible[right], autojunk=False
            ).ratio()
            if ratio >= threshold:
                seen.add(pair)
                pairs.append((left, right, ratio, "near"))
    return sorted(pairs, key=lambda item: (-item[2], item[0], item[1]))


def ocr_residue(text: str) -> list[str]:
    """Return high-signal OCR artifacts, with short human-readable snippets."""

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
        if (
            len(token) >= 6
            and re.search(r"[A-Za-z]", token)
            and len(re.findall(r"\d", token)) >= 2
        ):
            mixed.append(token[:32])
    if mixed:
        findings.append("mixed alphanumeric token(s): " + ", ".join(mixed[:3]))

    for line in text.replace("\f", " ").splitlines():
        compact = re.sub(r"\s+", "", line)
        if len(compact) >= 16:
            punctuation = sum(
                not character.isalnum() for character in compact
            ) / len(compact)
            if punctuation >= 0.72:
                snippet = re.sub(r"\s+", " ", line).strip()[:70]
                findings.append(f"punctuation-heavy OCR line: {snippet}")
                break
    return findings


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    epilog = """Audit semantics and default thresholds:

  Native prose is compared page by page after TeX commands and math are
  removed.  Single-letter, numeric, and mixed numeric tokens are math/layout
  exemptions.  Warning recall is below 0.70.  A severe coverage gap is below
  0.45 on a page with at least 20 eligible source tokens.  Strict mode fails
  missing included-page markers, source extraction failures, empty included
  source pages, and severe coverage gaps.  Repeated source/native page text is
  reported at sequence similarity 0.98 or higher when each page has at least
  25 eligible tokens.  Heading candidates are short title-shaped source lines
  with at least two eligible tokens, with known one-word headings exempted.

The default source extraction invokes pdftotext once for each of the 212
physical pages.  --source-text-dir can supply page-####.txt files from a later
run when that text layer has already been extracted.
"""
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=epilog,
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="fail on missing included pages and severe page-level recall gaps",
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=ROOT,
        help="Zhou project root (default: script directory)",
    )
    parser.add_argument(
        "--source-pdf",
        type=Path,
        default=None,
        help="source PDF relative to --root (default: source/zhou-quantitative-finance-interviews.pdf)",
    )
    parser.add_argument(
        "--transcription-dir",
        type=Path,
        default=None,
        help="native chunk directory relative to --root (default: latex/transcription)",
    )
    parser.add_argument(
        "--source-text-dir",
        type=Path,
        default=None,
        help="optional pre-extracted page text directory; accepts page-####.txt",
    )
    parser.add_argument(
        "--pdftotext",
        default="pdftotext",
        help="pdftotext executable used for page-by-page extraction",
    )
    parser.add_argument(
        "--pdfinfo",
        default="pdfinfo",
        help="pdfinfo executable used to verify the 212-page source",
    )
    parser.add_argument(
        "--expected-pages",
        type=int,
        default=EXPECTED_PAGES,
        help=f"expected physical source pages (default: {EXPECTED_PAGES})",
    )
    parser.add_argument(
        "--warn-recall",
        type=float,
        default=0.70,
        help="warn below this page token recall (default: 0.70)",
    )
    parser.add_argument(
        "--severe-recall",
        type=float,
        default=0.45,
        help="strict-fail below this recall when enough prose exists (default: 0.45)",
    )
    parser.add_argument(
        "--minimum-eligible-tokens",
        type=int,
        default=20,
        help="minimum source prose tokens for a recall score (default: 20)",
    )
    parser.add_argument(
        "--heading-min-tokens",
        type=int,
        default=2,
        help="minimum tokens for a non-special heading candidate (default: 2)",
    )
    parser.add_argument(
        "--repeat-similarity",
        type=float,
        default=0.98,
        help="sequence similarity threshold for repeated pages (default: 0.98)",
    )
    parser.add_argument(
        "--repeat-min-tokens",
        type=int,
        default=25,
        help="minimum tokens for repeated-page detection (default: 25)",
    )
    parser.add_argument(
        "--worst-pages",
        type=int,
        default=10,
        help="number of lowest-recall pages to print (default: 10)",
    )
    args = parser.parse_args(argv)
    if not 0 <= args.severe_recall <= args.warn_recall <= 1:
        parser.error("require 0 <= severe-recall <= warn-recall <= 1")
    if args.minimum_eligible_tokens < 1 or args.repeat_min_tokens < 1:
        parser.error("token thresholds must be positive")
    if not 0 <= args.repeat_similarity <= 1:
        parser.error("repeat-similarity must lie in [0, 1]")
    if args.expected_pages < 1 or args.worst_pages < 1:
        parser.error("expected-pages and worst-pages must be positive")
    return args


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_args(argv)
    root = args.root.resolve()
    source_pdf = resolve_path(root, args.source_pdf or DEFAULT_SOURCE)
    transcription = resolve_path(root, args.transcription_dir or DEFAULT_TRANSCRIPTION)
    source_text_dir = (
        resolve_path(root, args.source_text_dir) if args.source_text_dir else None
    )

    structural_issues: list[str] = []
    strict_issues: list[str] = []
    segments, segment_issues = collect_segments(transcription)
    structural_issues.extend(segment_issues)

    by_page: dict[int, list[Segment]] = defaultdict(list)
    marker_sequence: list[int] = []
    for segment in segments:
        by_page[segment.marker.physical].append(segment)
        marker_sequence.append(segment.marker.physical)
        if not 1 <= segment.marker.physical <= args.expected_pages:
            structural_issues.append(
                f"marker page {segment.marker.physical} is outside 1-{args.expected_pages} "
                f"at {display_path(segment.marker.path, root)}:{segment.marker.line}"
            )
        if segment.marker.physical in INCLUDED_PAGES:
            expected = expected_printed(segment.marker.physical)
            if segment.marker.printed != expected:
                structural_issues.append(
                    f"printed folio mismatch on physical page {segment.marker.physical}: "
                    f"got {segment.marker.printed}, expected {expected}"
                )

    duplicate_pages = sorted(page for page, items in by_page.items() if len(items) > 1)
    if duplicate_pages:
        structural_issues.append(
            "duplicate native page markers: " + ", ".join(map(str, duplicate_pages))
        )
    actual_pages = set(by_page)
    missing_pages = sorted(INCLUDED_PAGES - actual_pages)
    extra_pages = sorted(actual_pages - INCLUDED_PAGES)
    if missing_pages:
        structural_issues.append(
            "missing native markers for included physical pages: "
            + ", ".join(map(str, missing_pages))
        )
        strict_issues.append(
            "strict page coverage failure; missing included pages: "
            + ", ".join(map(str, missing_pages))
        )
    if extra_pages:
        structural_issues.append(
            "native markers appear on replaced/omitted or invalid pages: "
            + ", ".join(map(str, extra_pages))
        )
    if marker_sequence != sorted(marker_sequence):
        structural_issues.append("native page markers are out of source order")

    source_pages, extraction_issues, actual_pdf_pages = extract_source_pages(
        source_pdf,
        source_text_dir,
        args.pdftotext,
        args.pdfinfo,
        args.expected_pages,
    )
    structural_issues.extend(extraction_issues)
    if source_text_dir is None and actual_pdf_pages is not None:
        print(f"Source PDF page count: {actual_pdf_pages}")

    expected_sets = INCLUDED_PAGES | REPLACED_PAGES | OMITTED_PAGES
    disposition_issue = expected_sets != set(range(1, EXPECTED_PAGES + 1))
    if args.expected_pages == EXPECTED_PAGES and disposition_issue:
        structural_issues.append("source disposition sets do not cover physical pages 1-212")

    reports: list[PageReport] = []
    missing_headings: list[tuple[int, str]] = []
    source_residue: dict[int, list[str]] = {}
    native_token_pages: dict[int, list[str]] = {}

    for physical in range(1, args.expected_pages + 1):
        source_text = source_pages.get(physical, "")
        source_residue[physical] = ocr_residue(source_text)
        if physical in INCLUDED_PAGES and not source_text.strip():
            strict_issues.append(
                f"source OCR text is empty on included physical page {physical}"
            )
        if physical not in INCLUDED_PAGES or physical not in by_page or not source_text:
            continue
        native_text = by_page[physical][0].text
        report = coverage_report(
            physical,
            source_text,
            native_text,
            args.minimum_eligible_tokens,
        )
        reports.append(report)
        native_token_pages[physical] = report.native_tokens
        missing_headings.extend(
            (physical, heading)
            for heading in detect_missing_headings(
                source_text,
                native_text,
                args.heading_min_tokens,
            )
        )
        if report.recall is not None and report.recall < args.severe_recall:
            strict_issues.append(
                f"physical page {physical} recall {report.recall:.3f} "
                f"({report.matched}/{report.eligible} eligible tokens)"
            )

    source_repeats = repeated_page_pairs(
        {page: prose_tokens(text) for page, text in source_pages.items()},
        args.repeat_min_tokens,
        args.repeat_similarity,
    )
    native_repeats = repeated_page_pairs(
        native_token_pages,
        args.repeat_min_tokens,
        args.repeat_similarity,
    )

    scored = [report for report in reports if report.recall is not None]
    warnings = [report for report in scored if report.recall is not None and report.recall < args.warn_recall]
    worst = sorted(scored, key=lambda report: (report.recall or 0, report.physical))

    print(f"Native page markers: {len(actual_pages & INCLUDED_PAGES)}/{len(INCLUDED_PAGES)} included pages")
    print(
        "Thresholds: "
        f"warning recall < {args.warn_recall:.2f}; "
        f"severe recall < {args.severe_recall:.2f} with >= {args.minimum_eligible_tokens} "
        f"eligible tokens; repeated text >= {args.repeat_similarity:.2f} with >= "
        f"{args.repeat_min_tokens} tokens"
    )
    if scored:
        values = [report.recall for report in scored if report.recall is not None]
        print(
            f"Page recall: {len(scored)} scored; mean {mean(values):.3f}; "
            f"median {median(values):.3f}; warnings {len(warnings)}"
        )
    else:
        print("Page recall: no pages reached the eligible-token threshold")

    if worst:
        print("Worst pages by prose-token recall:")
        for report in worst[: args.worst_pages]:
            print(
                f"  p{report.physical:03d}: {report.recall:.3f} "
                f"({report.matched}/{report.eligible})"
            )
    if missing_headings:
        print("Possible missing headings:")
        for physical, heading in missing_headings[:30]:
            print(f"  p{physical:03d}: {heading}")
        if len(missing_headings) > 30:
            print(f"  ... {len(missing_headings) - 30} more")
    if source_repeats:
        print("Repeated source page text:")
        for left, right, ratio, kind in source_repeats[:20]:
            print(f"  p{left:03d} / p{right:03d}: {kind}, similarity {ratio:.3f}")
    if native_repeats:
        print("Repeated native page text:")
        for left, right, ratio, kind in native_repeats[:20]:
            print(f"  p{left:03d} / p{right:03d}: {kind}, similarity {ratio:.3f}")
    residue_pages = [(page, findings) for page, findings in source_residue.items() if findings]
    if residue_pages:
        print("Possible OCR residue:")
        for physical, findings in residue_pages[:30]:
            print(f"  p{physical:03d}: " + "; ".join(findings))
        if len(residue_pages) > 30:
            print(f"  ... {len(residue_pages) - 30} more")

    if structural_issues:
        print("Structural failures:")
        for issue in structural_issues[:40]:
            print(f"  - {issue}")
        if len(structural_issues) > 40:
            print(f"  ... {len(structural_issues) - 40} more")
    if args.strict and strict_issues:
        print("Strict coverage failures:")
        for issue in strict_issues[:40]:
            print(f"  - {issue}")
        if len(strict_issues) > 40:
            print(f"  ... {len(strict_issues) - 40} more")
    elif strict_issues:
        print(
            f"Strict-mode findings: {len(strict_issues)}; rerun with --strict to fail on them"
        )

    failures = list(structural_issues)
    if args.strict:
        failures.extend(strict_issues)
    if failures:
        print(f"RESULT: FAIL ({len(failures)} failure(s))")
        return 1
    print("RESULT: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
