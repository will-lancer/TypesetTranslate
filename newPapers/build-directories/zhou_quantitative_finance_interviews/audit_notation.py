#!/usr/bin/env python3
"""Audit Zhou's native LaTeX against the binding notation policy.

This is a static source check.  It deliberately does not invoke TeX, PDF
tools, OCR, extraction, or external programs.  The project audit remains the
authority for page coverage and environment balance; this script focuses on
notation and transcription hazards.
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parent
LATEX = ROOT / "latex"


@dataclass(frozen=True)
class Rule:
    name: str
    pattern: re.Pattern[str]
    explanation: str
    fatal: bool = True


# These rules operate on a line with comments removed.  The few source-era
# constructs that are intentional are documented in NOTATION.md and may be
# exempted locally with a preceding `% NOTATION EXCEPTION:` comment.
RULES = (
    Rule(
        "unicode-source-character",
        re.compile(r"[\u0080-\uffff]"),
        "use ASCII LaTeX commands for punctuation, dashes, quotes, and math glyphs",
    ),
    Rule(
        "forbidden-scan-package",
        re.compile(r"\\(?:usepackage|RequirePackage)\s*\{\s*pdfpages\s*\}"),
        "native transcription cannot load the pdfpages scan-import package",
    ),
    Rule(
        "forbidden-scan-command",
        re.compile(r"\\(?:includepdf|facsimilepages|frontmatterpages)\b"),
        "native transcription cannot import facsimile or scanned pages",
    ),
    Rule(
        "forbidden-source-input",
        re.compile(
            r"\\(?:input|include|includegraphics)\s*"
            r"(?:\[[^]]*\])?\s*\{[^}\n]*"
            r"(?:source(?:/|\\)|scan|facsimile|page[-_]?\d|\.pdf)"
        ),
        "do not import source scans or page images into the native LaTeX tree",
    ),
    Rule(
        "stray-control-space",
        re.compile(r"\\\s+[.!,;:?]"),
        "a control-space before punctuation is a common OCR-to-LaTeX corruption",
    ),
    Rule(
        "ellipsis-corruption",
        re.compile(r"(?:\\\.\s*){2,}|(?:\.\s*){3,}\\?"),
        "write ellipses as \\ldots or \\cdots, matching the source role",
    ),
    Rule(
        "frac-without-arguments",
        re.compile(r"\\(?:frac|dfrac|tfrac)\s*(?!\{)"),
        "\\frac, \\dfrac, and \\tfrac require braced numerator and denominator",
    ),
    Rule(
        "text-command-without-argument",
        re.compile(
            r"\\(?:operatorname|mathrm|mathit|text(?:bf|it)?)\b"
            r"\s*(?!\{)"
        ),
        "text and font commands require a braced argument",
    ),
    Rule(
        "sqrt-without-argument",
        re.compile(r"\\sqrt\s*(?!\{|\[)"),
        "\\sqrt requires a braced argument or an optional root index",
    ),
    Rule(
        "left-without-delimiter",
        re.compile(r"\\left(?![A-Za-z])\s*(?!\\|[.()\[\]{}|])"),
        "\\left must be followed by a LaTeX delimiter",
    ),
    Rule(
        "right-without-delimiter",
        re.compile(r"\\right(?![A-Za-z])\s*(?!\\|[.()\[\]{}|])"),
        "\\right must be followed by a LaTeX delimiter",
    ),
    Rule(
        "empty-set-alias",
        re.compile(r"\\(?:varnothing|emptyset)\b"),
        "page 15 binds the source empty-set symbol to \\Phi",
    ),
    Rule(
        "probability-alias",
        re.compile(r"\\(?:Pr\b|mathbb\s*\{?P\}?|operatorname\s*\{\s*P\s*\})"),
        "use the source probability function P(·)",
    ),
    Rule(
        "expectation-alias",
        re.compile(r"\\(?:mathbb\s*\{?E\}?|operatorname\s*\{\s*E\s*\}|mathrm\s*\{\s*E\s*\})"),
        "use the source expectation function E[·]",
    ),
    Rule(
        "raw-conditional-bar",
        re.compile(r"P\s*(?:\([^\n|)]*\|[^\n)]*\)|\{[^\n|}]*\|[^\n}]*\})"),
        "write conditional probability with \\mid, not a raw vertical bar",
    ),
    Rule(
        "unscoped-moment-operator",
        re.compile(
            r"(?<![\\A-Za-z])(?:Var|var|Cov|cov|Corr|corr|Std|std)\s*"
            r"(?:\(|\\left\s*\()"
        ),
        "use \\operatorname{var}, \\operatorname{cov}, \\operatorname{corr}, or \\operatorname{std}",
    ),
    Rule(
        "arrowed-vector",
        re.compile(r"\\(?:vec|overrightarrow|overleftarrow)\b"),
        "preserve the source's ordinary italic vector symbols",
    ),
    Rule(
        "logical-min-max-alias",
        re.compile(r"\\(?:land|lor)\b"),
        "page 15 uses \\wedge and \\vee for binary minimum and maximum",
    ),
    Rule(
        "legacy-cdf-pdf-font",
        re.compile(r"\\mathrm\s*\{\s*(?:cdf|pdf)\s*\}"),
        "page 15 uses italic cdf and pdf labels",
    ),
    Rule(
        "raw-percent-in-source",
        re.compile(r"(?<!\\)%"),
        "escape a percent sign as \\%; line comments are handled separately",
    ),
    Rule(
        "source-slash-abbreviation",
        re.compile(r"(?<![A-Za-z])/(?:pmf|pdf|cdf)\b"),
        "check that a slash abbreviation is source text, not a malformed LaTeX command",
        fatal=False,
    ),
    Rule(
        "bold-vector-restyling",
        re.compile(r"\\(?:mathbf|boldsymbol|bm)\b"),
        "review bold vector restyling against the source page",
        fatal=False,
    ),
    Rule(
        "upright-differential-restyling",
        re.compile(r"\\mathrm\s*\{\s*d(?:x|y|t|S|X|W)\s*\}"),
        "review differential typography against the source's d x, d t, and d W forms",
        fatal=False,
    ),
)


def strip_comment(line: str) -> str:
    """Return the part before the first unescaped TeX percent comment."""

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


def has_exception(previous_lines: list[str]) -> bool:
    return any("NOTATION EXCEPTION:" in line for line in previous_lines[-8:])


def check_brace_balance(path: Path, text: str, failures: list[str]) -> None:
    """Catch unmatched braces without trying to parse all of TeX."""

    depth = 0
    opening_line: int | None = None
    for line_number, raw_line in enumerate(text.splitlines(), start=1):
        line = strip_comment(raw_line)
        escaped = False
        for character in line:
            if character == "\\":
                escaped = not escaped
                continue
            if character == "{" and not escaped:
                if depth == 0:
                    opening_line = line_number
                depth += 1
            elif character == "}" and not escaped:
                depth -= 1
                if depth < 0:
                    failures.append(
                        f"{path.relative_to(ROOT)}:{line_number}: unmatched closing brace"
                    )
                    depth = 0
                    opening_line = None
            escaped = False
    if depth:
        failures.append(
            f"{path.relative_to(ROOT)}:{opening_line or 1}: "
            f"{depth} unmatched opening brace(s)"
        )


def check_delimiters(path: Path, text: str, failures: list[str]) -> None:
    r"""Check the cheap, high-signal \left/\right pairing invariant."""

    left = len(re.findall(r"\\left\b", text))
    right = len(re.findall(r"\\right\b", text))
    if left != right:
        failures.append(
            f"{path.relative_to(ROOT)}: \\left/\\right count mismatch "
            f"({left} left, {right} right)"
        )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "paths",
        nargs="*",
        type=Path,
        help="optional TeX paths relative to the Zhou project root",
    )
    args = parser.parse_args()

    if args.paths:
        files = [path if path.is_absolute() else ROOT / path for path in args.paths]
    else:
        files = (
            sorted(LATEX.rglob("*.tex")) + sorted(LATEX.rglob("*.sty"))
            if LATEX.exists()
            else []
        )

    failures: list[str] = []
    reviews: list[str] = []
    for path in files:
        if not path.is_file():
            failures.append(f"Missing LaTeX path: {path}")
            continue
        text = path.read_text(encoding="utf-8")
        check_brace_balance(path, text, failures)
        check_delimiters(path, text, failures)
        raw_lines = text.splitlines()
        literal_environment: str | None = None
        for line_number, raw_line in enumerate(raw_lines, start=1):
            begin_literal = re.search(r"\\begin\{(verbatim|lstlisting)\}", raw_line)
            if begin_literal:
                literal_environment = begin_literal.group(1)
                continue
            if literal_environment:
                if f"\\end{{{literal_environment}}}" in raw_line:
                    literal_environment = None
                continue
            code = strip_comment(raw_line)
            if not code.strip():
                continue
            exception = has_exception(raw_lines[max(0, line_number - 8) : line_number])

            # An unescaped percent in the middle of a source line starts a TeX
            # comment and can silently delete the rest of a formula.  A line
            # whose first non-space character is `%` is an ordinary metadata
            # comment and is intentionally ignored here.
            for index, character in enumerate(raw_line):
                if character != "%":
                    continue
                backslashes = 0
                cursor = index - 1
                while cursor >= 0 and raw_line[cursor] == "\\":
                    backslashes += 1
                    cursor -= 1
                if (
                    backslashes % 2 == 0
                    and raw_line[:index].strip()
                    and raw_line[index + 1 :].strip()
                ):
                    finding = (
                        f"{path.relative_to(ROOT)}:{line_number}: raw-percent-in-source: "
                        "escape a percent sign as \\%; line comments must begin a line "
                        f"[{character}]"
                    )
                    if exception:
                        reviews.append(finding + " (exception documented)")
                    else:
                        failures.append(finding)
                    break

            for rule in RULES:
                if rule.name == "ellipsis-corruption" and "\\foreach" in code:
                    continue
                match = rule.pattern.search(code)
                if not match:
                    continue
                finding = (
                    f"{path.relative_to(ROOT)}:{line_number}: {rule.name}: "
                    f"{rule.explanation} [{match.group(0)}]"
                )
                if exception:
                    reviews.append(finding + " (exception documented)")
                elif rule.fatal:
                    failures.append(finding)
                else:
                    reviews.append(finding)

    if reviews:
        print("NOTATION REVIEW CANDIDATES")
        for finding in reviews:
            print(f"  - {finding}")
    else:
        print("Notation review candidates: none.")

    if failures:
        print("\nDEFINITE NOTATION REGRESSIONS", file=sys.stderr)
        for finding in failures:
            print(f"  - {finding}", file=sys.stderr)
        print(
            "Use `% NOTATION EXCEPTION: reason` only for a deliberate, "
            "source-checked exception.",
            file=sys.stderr,
        )
        return 1

    print(f"Notation audit passed for {len(files)} LaTeX file(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
