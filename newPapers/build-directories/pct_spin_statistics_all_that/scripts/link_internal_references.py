#!/usr/bin/env python3
"""Replace printed cross-reference numbers with live LaTeX links.

The transcription keeps the source's printed numbers in ``\tag`` commands.
Every numbered display already has a label; this pass connects prose mentions
to those labels without changing the printed wording.
"""

from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LATEX = ROOT / "latex"
TEX_FILES = sorted((LATEX / "chapters").rglob("*.tex")) + sorted(
    (LATEX / "appendix").rglob("*.tex")
)


def split_comment(line: str) -> tuple[str, str]:
    for index, char in enumerate(line):
        if char != "%":
            continue
        slashes = 0
        cursor = index - 1
        while cursor >= 0 and line[cursor] == "\\":
            slashes += 1
            cursor -= 1
        if slashes % 2 == 0:
            return line[:index], line[index:]
    return line, ""


def aux_labels() -> dict[str, dict[str, str]]:
    maps = {"eq": {}, "thm": {}, "sec": {}, "fig": {}}
    aux = (LATEX / "master.aux").read_text(encoding="utf-8")
    pattern = re.compile(
        r"\\newlabel\{([^}]+)\}\{\{\{?([^{}]+)\}?\}\{"
    )
    for label, value in pattern.findall(aux):
        prefix = label.split(":", 1)[0]
        if prefix in maps:
            maps[prefix].setdefault(value, label)
    return maps


def equation_labels() -> dict[str, str]:
    mapping: dict[str, str] = {}
    pattern = re.compile(
        r"\\tag\{([^{}]+)\}\s*\\label\{(eq:[^{}]+)\}", re.MULTILINE
    )
    for path in TEX_FILES:
        for number, label in pattern.findall(path.read_text(encoding="utf-8")):
            number = number.strip()
            previous = mapping.setdefault(number, label)
            if previous != label:
                raise ValueError(f"duplicate equation number {number}: {previous}, {label}")
    return mapping


def linked_number(code: str, word: str, mapping: dict[str, str]) -> str:
    if word not in code or "\\begin{theorem}" in code:
        return code
    for number in sorted(mapping, key=len, reverse=True):
        label = mapping[number]
        escaped = re.escape(number)
        code = re.sub(
            rf"(?<=\bTheorem)\s*\({escaped}\)",
            rf"~\\ref{{{label}}}",
            code,
        )
        code = re.sub(
            rf"(?<![({{])\b{escaped}\b",
            rf"\\ref{{{label}}}",
            code,
        )
    return code


def replace_cross_references(code: str, maps: dict[str, dict[str, str]]) -> str:
    # Results are handled first so ``Theorem (4-11)`` links to the theorem
    # rather than to equation (4-11).
    if "Theorem" in code:
        for number in sorted(maps["thm"], key=len, reverse=True):
            label = maps["thm"][number]
            escaped = re.escape(number)
            code = re.sub(
                rf"(?<=Theorem)\s*\({escaped}\)",
                rf"~\\ref{{{label}}}",
                code,
            )
            if "\\begin{theorem}" not in code:
                code = re.sub(
                    rf"(?<![({{:A-Za-z0-9_-])\b{escaped}\b",
                    rf"\\ref{{{label}}}",
                    code,
                )

    if "Section" in code:
        for number in sorted(maps["sec"], key=len, reverse=True):
            if "-" not in number:
                continue
            code = re.sub(
                rf"(?<![({{:A-Za-z0-9_-])\b{re.escape(number)}\b",
                rf"\\ref{{{maps['sec'][number]}}}",
                code,
            )

    if "Chapter" in code:
        for number in ("1", "2", "3", "4"):
            label = maps["sec"].get(number)
            if label:
                code = re.sub(
                    rf"(?<=Chapter[~ ]){number}\b", rf"\\ref{{{label}}}", code
                )

    if "Figure" in code:
        for number in sorted(maps["fig"], key=len, reverse=True):
            code = re.sub(
                rf"(?<=Figure[~ ]){re.escape(number)}\b",
                rf"\\ref{{{maps['fig'][number]}}}",
                code,
            )

    for number in sorted(maps["eq"], key=len, reverse=True):
        label = maps["eq"][number]
        code = re.sub(
            rf"(?<!\\tag\{{)\({re.escape(number)}\)",
            rf"\\eqref{{{label}}}",
            code,
        )
    return code


def appendix_citations(code: str) -> str:
    def cite(match: re.Match[str]) -> str:
        raw = match.group(1)
        numbers: list[int] = []
        for part in raw.split(","):
            part = part.strip()
            range_match = re.fullmatch(r"(\d+)\s*--\s*(\d+)", part)
            if range_match:
                start, end = map(int, range_match.groups())
                numbers.extend(range(start, end + 1))
            elif part.isdigit():
                numbers.append(int(part))
            else:
                return match.group(0)
        keys = ",".join(f"pct-app-{number}" for number in numbers)
        return rf"\cite{{{keys}}}"

    return re.sub(r"\[([0-9][0-9,\s-]*)\]", cite, code)


def main() -> None:
    maps = aux_labels()
    maps["eq"] = {
        number: label
        for number, label in equation_labels().items()
        if "-" in number or "." in number
    }
    maps["sec"].update(
        {
            "1": "ch:relativistic-transformation-laws",
            "2-6": "sec:2-6",
            "4": "ch:general-theorems-relativistic-qft",
        }
    )
    maps["thm"].update(
        {
            "3-1": "thm:ch3-1-vacuum-transformation-laws",
            "2-12": "thm:ch2-12-jost",
            "3-2": "thm:ch3-2-translation-invariance",
            "3-3": "thm:ch3-3-positive-definiteness",
            "3-4": "thm:ch3-4-cluster-decomposition",
            "3-5": "thm:ch3-5-holomorphic-boundary-values",
            "3-6": "thm:ch3-6-free-field-wightman-functions",
        }
    )

    changed = 0
    for path in TEX_FILES:
        original = path.read_text(encoding="utf-8")
        output: list[str] = []
        for line in original.splitlines(keepends=True):
            code, comment = split_comment(line)
            code = replace_cross_references(code, maps)
            if path.parent.name == "appendix" and path.name != "bibliography.tex":
                code = appendix_citations(code)
            output.append(code + comment)
        revised = "".join(output)
        if revised != original:
            path.write_text(revised, encoding="utf-8")
            changed += 1
            print(path.relative_to(ROOT))
    print(f"linked references in {changed} TeX files")


if __name__ == "__main__":
    main()
