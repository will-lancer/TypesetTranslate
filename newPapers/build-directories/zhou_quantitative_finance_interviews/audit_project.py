#!/usr/bin/env python3
"""Audit native Zhou coverage, float metadata, and style-policy contracts."""

from __future__ import annotations

import argparse
import re
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parent
LATEX = ROOT / "latex"
TRANSCRIPTION = LATEX / "transcription"

EXPECTED_CHUNKS = [
    "pp0005-0015.tex",
    "pp0017-0018.tex",
    "pp0019-0023.tex",
    "pp0024-0028.tex",
    "pp0029-0033.tex",
    "pp0034-0038.tex",
    "pp0039-0043.tex",
    "pp0044-0048.tex",
    "pp0049-0053.tex",
    "pp0054-0058.tex",
    "pp0059-0063.tex",
    "pp0064-0068.tex",
    "pp0069-0074.tex",
    "pp0075-0079.tex",
    "pp0080-0084.tex",
    "pp0085-0089.tex",
    "pp0090-0094.tex",
    "pp0095-0099.tex",
    "pp0100-0104.tex",
    "pp0105-0109.tex",
    "pp0110-0114.tex",
    "pp0115-0119.tex",
    "pp0121-0125.tex",
    "pp0126-0130.tex",
    "pp0131-0135.tex",
    "pp0136-0140.tex",
    "pp0141-0145.tex",
    "pp0146-0150.tex",
    "pp0151-0152.tex",
    "pp0153-0157.tex",
    "pp0158-0162.tex",
    "pp0163-0167.tex",
    "pp0168-0172.tex",
    "pp0173-0177.tex",
    "pp0178-0182.tex",
    "pp0183-0185.tex",
    "pp0187-0191.tex",
    "pp0192-0196.tex",
    "pp0197-0201.tex",
    "pp0202-0206.tex",
    "pp0207-0207.tex",
    "pp0209-0211.tex",
]

ASSEMBLY_FILES = [
    "frontmatter/frontmatter.tex",
    "chapters/chapter01.tex",
    "chapters/chapter02.tex",
    "chapters/chapter03.tex",
    "chapters/chapter04.tex",
    "chapters/chapter05.tex",
    "chapters/chapter06.tex",
    "chapters/chapter07.tex",
    "backmatter/index.tex",
]

INCLUDED = {5, 13, 14, 15}
INCLUDED.update(range(17, 120))
INCLUDED.update(range(121, 186))
INCLUDED.update(range(187, 208))
INCLUDED.update(range(209, 212))
REPLACED = {1, 3, 7, 8, 9, 10, 11}
OMITTED = {2, 4, 6, 12, 16, 120, 186, 208, 212}
FRONTMATTER_PAGES = {5, 13, 14, 15}

PAGE_MARKER = re.compile(
    r"^% ZHOU-SOURCE-PAGE: (?P<physical>\d+) PRINTED: "
    r"(?P<printed>FRONTMATTER|\d+)\s*$",
    re.MULTILINE,
)
INPUT = re.compile(r"\\input\{transcription/([^}]+)\}")
BEGIN = re.compile(r"\\begin\{([^}]+)\}")
END = re.compile(r"\\end\{([^}]+)\}")
FLOAT_TOKEN = re.compile(
    r"\\(?P<command>begin|end)\{(?P<kind>figure|table)(?P<star>\*)?\}"
    r"(?:\[(?P<placement>[^]]*)\])?"
)
CAPTION_START = re.compile(r"\\caption(?:\s*\[[^]]*\])?\s*\{")
LABEL_COMMAND = re.compile(r"\\label\s*\{(?P<label>[^}\n]+)\}")
MANUAL_FLOAT_CAPTION = re.compile(
    r"\\(?:noindent\s*)?\\textbf\{\s*(?:Figure|Table)\s+[0-9]"
)
UNNUMBERED_SOURCE_NOTE = re.compile(
    r"\\footnote\s*\{|"
    r"\\footnotemark(?!\s*\[)|"
    r"\\footnotetext(?!\s*\[)"
)


def fail(message: str) -> None:
    raise SystemExit(message)


def strip_comments(text: str) -> str:
    return "\n".join(
        re.split(r"(?<!\\)%", line, maxsplit=1)[0] for line in text.splitlines()
    )


def audit_environment_nesting(text: str) -> None:
    """Validate environments across the assembled transcription stream."""

    stack: list[tuple[str, int]] = []
    for token in re.finditer(r"\\(?P<command>begin|end)\{(?P<name>[^}]+)\}", text):
        command = token.group("command")
        name = token.group("name")
        line_number = text.count("\n", 0, token.start()) + 1
        if command == "begin":
            stack.append((name, line_number))
            continue
        if not stack:
            fail(f"Environment {name} closes at assembled line {line_number} without opening")
        opened, opened_line = stack.pop()
        if opened != name:
            fail(
                f"Environment {name} closes at assembled line {line_number} while "
                f"{opened} from line {opened_line} is open"
            )
    if stack:
        name, line_number = stack[-1]
        fail(f"Environment {name} opened at assembled line {line_number} is not closed")


def audit_float_metadata(
    path: Path,
    text: str,
    issues: list[str],
    labels: dict[str, str],
) -> None:
    """Check native floats without inventing metadata absent from the source."""

    active = None
    for line_number, raw_line in enumerate(text.splitlines(), start=1):
        code = strip_comments(raw_line)
        if not code.strip():
            continue

        manual = MANUAL_FLOAT_CAPTION.search(code)
        if manual:
            issues.append(
                f"{path.relative_to(ROOT)}:{line_number}: manual Figure/Table caption "
                "prefix; use the environment counter and \\caption"
            )

        if active is not None:
            active["captions"] += len(CAPTION_START.findall(code))
            for label_match in LABEL_COMMAND.finditer(code):
                label = label_match.group("label")
                active["labels"].append((label, line_number))

        for token in FLOAT_TOKEN.finditer(code):
            command = token.group("command")
            kind = token.group("kind")
            if command == "begin":
                if active is not None:
                    issues.append(
                        f"{path.relative_to(ROOT)}:{line_number}: nested {kind} inside "
                        f"{active['kind']}"
                    )
                    continue
                placement = token.group("placement")
                if placement is None:
                    issues.append(
                        f"{path.relative_to(ROOT)}:{line_number}: {kind} has no explicit "
                        "placement spec"
                    )
                elif any(character not in "htbp!H" for character in placement):
                    issues.append(
                        f"{path.relative_to(ROOT)}:{line_number}: unsupported {kind} "
                        f"placement spec [{placement}]"
                    )
                active = {
                    "kind": kind,
                    "line": line_number,
                    "captions": 0,
                    "labels": [],
                }
                continue

            if active is None:
                issues.append(
                    f"{path.relative_to(ROOT)}:{line_number}: closing {kind} without "
                    "an open float"
                )
                continue
            if active["kind"] != kind:
                issues.append(
                    f"{path.relative_to(ROOT)}:{line_number}: closed {kind} while "
                    f"{active['kind']} from line {active['line']} is open"
                )
                active = None
                continue

            if active["captions"] > 1:
                issues.append(
                    f"{path.relative_to(ROOT)}:{active['line']}: {kind} has "
                    f"{active['captions']} captions; expected at most one"
                )
            expected_prefix = "fig:zhou-" if kind == "figure" else "tab:zhou-"
            float_labels = active["labels"]
            if len(float_labels) > 1:
                issues.append(
                    f"{path.relative_to(ROOT)}:{active['line']}: {kind} has "
                    f"{len(float_labels)} labels; expected at most one"
                )
            for label, label_line in float_labels:
                if not label.startswith(expected_prefix):
                    issues.append(
                        f"{path.relative_to(ROOT)}:{label_line}: {kind} label "
                        f"{label!r} should start with {expected_prefix!r}"
                    )
                prior = labels.get(label)
                if prior is not None:
                    issues.append(
                        f"{path.relative_to(ROOT)}:{label_line}: duplicate float label "
                        f"{label!r}; first used at {prior}"
                    )
                else:
                    labels[label] = f"{path.relative_to(ROOT)}:{label_line}"
            active = None

    if active is not None:
        issues.append(
            f"{path.relative_to(ROOT)}:{active['line']}: unclosed {active['kind']} "
            "environment"
        )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--allow-queries",
        action="store_true",
        help="allow ZHOU-QUERY markers during active transcription",
    )
    args = parser.parse_args()

    expected_paths = {TRANSCRIPTION / name for name in EXPECTED_CHUNKS}
    actual_paths = set(TRANSCRIPTION.glob("*.tex"))
    missing = sorted(path.name for path in expected_paths - actual_paths)
    extra = sorted(path.name for path in actual_paths - expected_paths)
    if missing or extra:
        fail(f"Chunk set mismatch; missing={missing}, extra={extra}")

    assembly_inputs: list[str] = []
    for relative in ASSEMBLY_FILES:
        path = LATEX / relative
        if not path.is_file():
            fail(f"Missing assembly file: {relative}")
        assembly_inputs.extend(INPUT.findall(path.read_text(encoding="utf-8")))
    if assembly_inputs != EXPECTED_CHUNKS:
        fail(
            "Assembly order mismatch; "
            f"expected={EXPECTED_CHUNKS}, actual={assembly_inputs}"
        )

    master = (LATEX / "master.tex").read_text(encoding="utf-8")
    style = (LATEX / "quantguide.sty").read_text(encoding="utf-8")
    for relative in ASSEMBLY_FILES:
        if f"\\input{{{relative}}}" not in master:
            fail(f"master.tex omits {relative}")
    if "\\usepackage{quantguide}" not in master:
        fail("master.tex does not load quantguide")
    if "\\title{" not in master or "\\author{" not in master:
        fail("master.tex must retain title and author metadata")
    if "\\subheader{First edition}" not in master:
        fail("master.tex must retain the first-edition identity")
    if "\\affiliation{" in master or re.search(r"edited by\b", master, re.IGNORECASE):
        fail("master.tex contains retired affiliation or editor-banner metadata")
    if not re.search(r"\\maketitle\s*\\clearpage", master):
        fail("master.tex must clear the title page before frontmatter")

    required_style_macros = (r"\dd", r"\E", r"\PDF", r"\CDF")
    for macro in required_style_macros:
        if not re.search(
            rf"\\(?:newcommand|DeclareRobustCommand)\s*\{{{re.escape(macro)}\}}",
            style,
        ):
            fail(f"quantguide.sty does not define canonical macro {macro}")
    for environment in ("problem", "solution", "concept"):
        if not re.search(rf"\\newenvironment\s*\{{{environment}\}}", style):
            fail(f"quantguide.sty does not define breakable {environment} environment")
    if r"\renewcommand{\qedsymbol}{\ensuremath{\square}}" not in style:
        fail("quantguide.sty does not define the solution QED square")
    if r"\begin{proof}[Solution]" not in style or r"\end{proof}" not in style:
        fail("quantguide.sty solution environment does not use proof/QED machinery")
    if r"\renewcommand{\underline}[1]{#1}" not in style:
        fail("quantguide.sty does not neutralize legacy underline styling")

    marker_records: list[tuple[int, str, str]] = []
    all_tex = [LATEX / "master.tex", LATEX / "quantguide.sty"]
    all_tex.extend(LATEX / relative for relative in ASSEMBLY_FILES)
    all_tex.extend(TRANSCRIPTION / name for name in EXPECTED_CHUNKS)

    forbidden = re.compile(
        r"\\(?:includepdf|facsimilepages|frontmatterpages)|"
        r"\\RequirePackage\{pdfpages\}|sourcepdf"
    )
    unresolved = re.compile(r"ZHOU-QUERY|\bTODO\b|\bTBD\b|\bFIXME\b")
    non_ascii: list[str] = []
    float_issues: list[str] = []
    float_labels: dict[str, str] = {}

    for path in all_tex:
        text = path.read_text(encoding="utf-8")
        match = forbidden.search(text)
        if match:
            fail(f"Forbidden facsimile command in {path}: {match.group(0)}")
        if not args.allow_queries:
            match = unresolved.search(text)
            if match:
                fail(f"Unresolved marker in {path}: {match.group(0)}")
        for line_number, line in enumerate(text.splitlines(), start=1):
            if any(ord(character) > 127 for character in line):
                non_ascii.append(f"{path}:{line_number}")

        if path.parent == TRANSCRIPTION:
            if path.stat().st_size < 80:
                fail(f"Suspiciously short transcription chunk: {path.name}")
            match = UNNUMBERED_SOURCE_NOTE.search(text)
            if match:
                fail(
                    f"Source footnote lacks an explicit source number in "
                    f"{path.name}: {match.group(0)}"
                )
            for match in PAGE_MARKER.finditer(text):
                marker_records.append(
                    (int(match.group("physical")), match.group("printed"), path.name)
                )
            audit_float_metadata(path, text, float_issues, float_labels)

    if float_issues:
        fail("Float metadata audit failed:\n" + "\n".join(float_issues))

    if non_ascii:
        fail(f"Non-ASCII source remains in TeX: {non_ascii}")

    assembled_visible = "\n".join(
        strip_comments((TRANSCRIPTION / name).read_text(encoding="utf-8"))
        for name in EXPECTED_CHUNKS
    )
    audit_environment_nesting(assembled_visible)

    page_counts = Counter(physical for physical, _, _ in marker_records)
    duplicated = sorted(page for page, count in page_counts.items() if count != 1)
    seen_pages = set(page_counts)
    if seen_pages != INCLUDED or duplicated:
        fail(
            "Source marker coverage mismatch; "
            f"missing={sorted(INCLUDED - seen_pages)}, "
            f"extra={sorted(seen_pages - INCLUDED)}, duplicated={duplicated}"
        )

    for physical, printed, chunk in marker_records:
        expected_printed = "FRONTMATTER" if physical in FRONTMATTER_PAGES else str(physical - 16)
        if printed != expected_printed:
            fail(
                f"Printed folio mismatch in {chunk}: physical {physical} "
                f"has {printed}, expected {expected_printed}"
            )

    dispositions = INCLUDED | REPLACED | OMITTED
    if dispositions != set(range(1, 213)):
        fail("Disposition map does not cover physical pages 1-212")
    if (INCLUDED & REPLACED) or (INCLUDED & OMITTED) or (REPLACED & OMITTED):
        fail("Disposition sets overlap")

    required_sections = [
        "General Principles",
        "Brain Teasers",
        "Calculus and Linear Algebra",
        "Probability Theory",
        "Stochastic Process and Stochastic Calculus",
        "Finance",
        "Algorithms and Numerical Methods",
    ]
    combined = "\n".join(
        (TRANSCRIPTION / name).read_text(encoding="utf-8") for name in EXPECTED_CHUNKS
    )
    for heading in required_sections:
        if combined.count(f"\\section{{{heading}}}") != 1:
            fail(f"Required chapter section is missing or duplicated: {heading}")

    print(
        "Project audit passed: "
        f"{len(EXPECTED_CHUNKS)} native chunks, {len(INCLUDED)} source pages, "
        f"{len(REPLACED)} replaced pages, {len(OMITTED)} omitted leaves"
    )


if __name__ == "__main__":
    main()
