#!/usr/bin/env python3
"""Create the modular exercise scaffolding inside the three copied QFT trees.

The script is intentionally strict: it only operates on the independent
``*_exercises`` directories, requires the copied backmatter to have the
expected canonical structure, and refuses to run twice.
"""

from __future__ import annotations

import hashlib
import json
import re
from dataclasses import dataclass
from pathlib import Path


HERE = Path(__file__).resolve().parent


@dataclass(frozen=True)
class Edition:
    name: str
    canonical_name: str
    first_chapter: int
    last_chapter: int
    volume_title: str

    @property
    def root(self) -> Path:
        return HERE / self.name

    @property
    def canonical_root(self) -> Path:
        return HERE / self.canonical_name


EDITIONS = (
    Edition(
        "weinberg_vol1_exercises",
        "weinberg_vol1",
        1,
        14,
        "Volume I: Foundations",
    ),
    Edition(
        "weinberg_vol2_exercises",
        "weinberg_vol2",
        15,
        23,
        "Volume II: Modern Applications",
    ),
    Edition(
        "weinberg_vol3_exercises",
        "weinberg_vol3",
        24,
        32,
        "Volume III: Supersymmetry",
    ),
)

SOURCE_PRINTED_PAGES = {
    15: (1, 62),
    16: (63, 79),
    17: (80, 110),
    18: (111, 162),
    19: (163, 251),
    20: (252, 294),
    21: (295, 358),
    22: (359, 420),
    23: (421, 477),
    24: (1, 24),
    25: (25, 54),
    26: (55, 112),
    27: (113, 178),
    28: (179, 247),
    29: (248, 306),
    30: (307, 317),
    31: (318, 381),
    32: (382, 410),
}


STYLE = r"""\NeedsTeXFormat{LaTeX2e}
\ProvidesPackage{exercise-edition}[2026/07/30 Weinberg QFT exercise-edition helpers]

\setlength{\emergencystretch}{3em}

\newcommand{\ExerciseEditorialNote}{%
  \noindent\emph{These editorial solutions were added by Codex and are not
  part of Weinberg's original text.}\par\medskip
}

\newcommand{\ExerciseIndexPaginationNote}{%
  \par\begingroup\small\itshape
  \noindent Pagination note: the numbers in this inherited index reproduce
  Weinberg's printed-source pagination. They are source-page references, not
  page numbers in this expanded, reflowed exercise PDF. Use the table of
  contents or \texttt{INDEX\_PAGINATION.md} for live navigation.\par
  \endgroup\medskip
}

\newcommand{\InKet}[1]{\ket{#1}_{\mathrm{in}}}
\newcommand{\OutKet}[1]{\ket{#1}_{\mathrm{out}}}
\newcommand{\InBra}[1]{{}_{\mathrm{in}}\!\bra{#1}}
\newcommand{\OutBra}[1]{{}_{\mathrm{out}}\!\bra{#1}}

\newcommand{\chapterexercisehook}[1]{%
  \input{exercises/chapter#1/weinberg-exercises.tex}%
  \input{exercises/chapter#1/weinberg-solutions.tex}%
  \input{exercises/chapter#1/supplementary-exercises.tex}%
  \input{exercises/chapter#1/supplementary-solutions.tex}%
}

\newcommand{\WeinbergExercise}[1]{%
  \item[\textbf{W.\thesection.#1.}]%
  \phantomsection\label{exercise:W:\thesection:#1}%
}

\newcommand{\WeinbergSolution}[1]{%
  \item[\textbf{W.\thesection.#1.}]%
  \phantomsection\label{solution:W:\thesection:#1}%
}

\newcommand{\SupplementaryExercise}[4]{%
  \item[\textbf{S.\thesection.#1.}]%
  \phantomsection\label{exercise:S:\thesection:#1}%
  \textbf{#2}\par
  \noindent{\small\itshape #3}\par\smallskip
  \expandafter\def\csname exercise@source@\thesection @#1\endcsname{#4}%
}

\newcommand{\SupplementarySolution}[2]{%
  \item[\textbf{S.\thesection.#1.}]%
  \phantomsection\label{solution:S:\thesection:#1}%
  \textbf{#2}\par\smallskip
}
"""


WEINBERG_SOLUTIONS = r"""\chapterbackmatter{Solutions to Weinberg Exercises}
\ExerciseEditorialNote

% Editorial solutions are inserted here with \WeinbergSolution{N}.
"""


SUPPLEMENTARY_EXERCISES = r"""\chapterbackmatter{Supplementary Exercises}

% Use \SupplementaryExercise{N}{Title}{(Source credit)}{source-ledger-id}.
"""


SUPPLEMENTARY_SOLUTIONS = r"""\chapterbackmatter{Solutions to Supplementary Exercises}

% Editorial solutions are inserted here with \SupplementarySolution{N}{Title}.
"""


EMPTY_WEINBERG_EXERCISES = r"""\chapterbackmatter{Weinberg Exercises}

\noindent\emph{Weinberg's original Chapter 1 contains no end-of-chapter
exercises.}
"""


EMPTY_WEINBERG_SOLUTIONS = r"""\chapterbackmatter{Solutions to Weinberg Exercises}
\ExerciseEditorialNote

\noindent\emph{There are no original Weinberg exercises to solve in this
chapter.}
"""


def strip_comments(line: str) -> str:
    escaped = False
    for index, char in enumerate(line):
        if char == "%" and not escaped:
            return line[:index]
        escaped = char == "\\" and not escaped
        if char != "\\":
            escaped = False
    return line


def label_top_level_items(problem_block: str) -> tuple[str, int]:
    """Replace only the outer problem-list items with stable W macros."""

    output: list[str] = []
    depth = 0
    count = 0
    for raw_line in problem_block.splitlines(keepends=True):
        code = strip_comments(raw_line)
        begins = code.count(r"\begin{enumerate}")
        ends = code.count(r"\end{enumerate}")
        depth += begins
        if depth == 1 and re.match(r"^\s*\\item(?:\s|$)", code):
            count += 1
            raw_line = re.sub(
                r"^(\s*)\\item(?:\s*)",
                lambda match: (
                    f"{match.group(1)}\\WeinbergExercise{{{count}}} "
                ),
                raw_line,
                count=1,
            )
        output.append(raw_line)
        depth -= ends
        if depth < 0:
            raise ValueError("Unbalanced enumerate environment in Problems block")
    if depth != 0:
        raise ValueError("Unbalanced enumerate environment in Problems block")
    return "".join(output), count


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def canonical_manifest(edition: Edition) -> dict[str, str]:
    result: dict[str, str] = {}
    for path in sorted(edition.canonical_root.rglob("*")):
        if path.is_file() and not any(
            path.name.endswith(suffix)
            for suffix in (
                ".aux",
                ".fdb_latexmk",
                ".fls",
                ".log",
                ".out",
                ".pdf",
                ".toc",
            )
        ):
            result[str(path.relative_to(edition.canonical_root))] = sha256(path)
    return result


def chapter_title(wrapper: Path) -> str:
    text = wrapper.read_text()
    short_match = re.search(r"\\section\[([^\]]+)\]", text)
    if short_match:
        return short_match.group(1)
    match = re.search(r"\\section\{([^}]+)\}", text)
    if not match:
        raise ValueError(f"Could not find chapter title in {wrapper}")
    return match.group(1)


def update_master(edition: Edition) -> None:
    master = edition.root / "latex" / "master.tex"
    text = master.read_text()
    if r"\usepackage{exercise-edition}" in text:
        raise RuntimeError(f"{master} is already scaffolded")
    insertion = r"\usepackage{float}" + "\n" + r"\usepackage{exercise-edition}"
    if r"\usepackage{float}" not in text:
        raise ValueError(f"Missing expected float package in {master}")
    text = text.replace(r"\usepackage{float}", insertion, 1)
    text = text.replace(
        edition.volume_title + "}",
        edition.volume_title + " -- Exercise Edition}",
        1,
    )
    text = text.replace(
        r"\subheader{" + edition.volume_title + "}",
        r"\subheader{" + edition.volume_title + r" -- Exercise Edition}",
        1,
    )
    master.write_text(text)


def scaffold_chapter(edition: Edition, chapter: int) -> dict[str, object]:
    chapter_id = f"{chapter:02d}"
    chapter_dir = edition.root / "latex" / "chapters" / f"chapter{chapter_id}"
    wrapper = edition.root / "latex" / "chapters" / f"chapter{chapter_id}.tex"
    backmatter = chapter_dir / "backmatter.tex"
    if chapter == 2 and not backmatter.exists():
        backmatter = chapter_dir / "appC-backmatter.tex"
    if not backmatter.exists():
        raise FileNotFoundError(backmatter)

    exercise_dir = edition.root / "latex" / "exercises" / f"chapter{chapter_id}"
    if exercise_dir.exists():
        raise RuntimeError(f"{exercise_dir} already exists")
    exercise_dir.mkdir(parents=True)

    text = backmatter.read_text()
    problem_marker = r"\chapterbackmatter{Problems}"
    reference_marker = r"\chapterbackmatter{References}"
    bibliography_marker = r"\chapterbackmatter{Bibliography}"
    hook = rf"\chapterexercisehook{{{chapter_id}}}" + "\n\n"

    if problem_marker in text:
        if text.count(problem_marker) != 1 or text.count(reference_marker) != 1:
            raise ValueError(f"Unexpected Problems/References markers in {backmatter}")
        start = text.index(problem_marker)
        end = text.index(reference_marker, start)
        original_problem_block = text[start:end].rstrip() + "\n"
        generated, count = label_top_level_items(
            original_problem_block.replace(
                problem_marker,
                r"\chapterbackmatter{Weinberg Exercises}",
                1,
            )
        )
        text = text[:start] + hook + text[end:]
    else:
        if chapter != 1:
            raise ValueError(f"No Problems marker in {backmatter}")
        marker = bibliography_marker if bibliography_marker in text else reference_marker
        if marker not in text:
            raise ValueError(f"No Bibliography/References marker in {backmatter}")
        start = text.index(marker)
        text = text[:start] + hook + text[start:]
        generated = EMPTY_WEINBERG_EXERCISES
        count = 0

    backmatter.write_text(text)
    (exercise_dir / "weinberg-exercises.tex").write_text(generated)
    (exercise_dir / "weinberg-solutions.tex").write_text(
        EMPTY_WEINBERG_SOLUTIONS if count == 0 else WEINBERG_SOLUTIONS
    )
    (exercise_dir / "supplementary-exercises.tex").write_text(
        SUPPLEMENTARY_EXERCISES
    )
    (exercise_dir / "supplementary-solutions.tex").write_text(
        SUPPLEMENTARY_SOLUTIONS
    )

    title = chapter_title(wrapper)
    historical = title == "Historical Introduction"
    result = {
        "chapter": chapter,
        "title": title,
        "weinberg_exercises": count,
        "supplementary_target": 0 if historical else 30,
        "count_exception": (
            "Historical chapter: supplementary exercises are intentionally "
            "omitted at the user's direction."
            if historical
            else None
        ),
        "backmatter": str(backmatter.relative_to(edition.root)),
    }
    if chapter in SOURCE_PRINTED_PAGES:
        result["source_printed_pages"] = list(SOURCE_PRINTED_PAGES[chapter])
    return result


def scaffold_edition(edition: Edition) -> None:
    if not edition.root.exists():
        raise FileNotFoundError(
            f"Copy the canonical tree to {edition.root} before scaffolding"
        )
    if (edition.root / "exercise-edition.json").exists():
        raise RuntimeError(f"{edition.root} is already scaffolded")

    update_master(edition)
    (edition.root / "latex" / "exercise-edition.sty").write_text(STYLE)
    chapters = [
        scaffold_chapter(edition, chapter)
        for chapter in range(edition.first_chapter, edition.last_chapter + 1)
    ]

    metadata = {
        "edition": edition.name,
        "canonical_source": edition.canonical_name,
        "selected_variant_note": (
            "The conventional four-component Volume III is the authoritative "
            "base; the two-component tree is a specialized derived edition."
            if edition.name == "weinberg_vol3_exercises"
            else None
        ),
        "source_index": edition.name != "weinberg_vol1_exercises",
        "pdf_arabic_page_offset": (
            6 if edition.name == "weinberg_vol1_exercises" else 4
        ),
        "chapter_range": [edition.first_chapter, edition.last_chapter],
        "chapters": chapters,
    }
    (edition.root / "exercise-edition.json").write_text(
        json.dumps(metadata, indent=2) + "\n"
    )
    (edition.root / "canonical-source-sha256.json").write_text(
        json.dumps(canonical_manifest(edition), indent=2, sort_keys=True) + "\n"
    )
    exercise_hashes = {
        str(path.relative_to(edition.root)): sha256(path)
        for path in sorted(
            (edition.root / "latex" / "exercises").glob(
                "chapter*/weinberg-exercises.tex"
            )
        )
    }
    (edition.root / "weinberg-exercise-source-sha256.json").write_text(
        json.dumps(exercise_hashes, indent=2, sort_keys=True) + "\n"
    )
    volume_number = re.search(r"vol([123])", edition.name)
    if volume_number:
        relative_export = (
            f"../../weinberg-qft/weinberg-vol{volume_number.group(1)}.pdf"
        )
        canonical_export = (edition.root / relative_export).resolve()
        if canonical_export.is_file():
            (edition.root / "canonical-export-sha256.json").write_text(
                json.dumps(
                    {relative_export: sha256(canonical_export)},
                    indent=2,
                    sort_keys=True,
                )
                + "\n"
            )

    script_copies = {
        "audit_weinberg_qft_exercises.py": "audit_exercises.py",
        "build_weinberg_qft_exercise_edition.sh": "build_and_verify.sh",
        "render_weinberg_qft_index_crosswalk.py": "render_index_pagination.py",
        "render_weinberg_qft_inventory.py": "render_inventory.py",
        "render_weinberg_qft_source_ledger.py": "render_source_ledger.py",
    }
    for source_name, destination_name in script_copies.items():
        source = HERE / source_name
        if not source.is_file():
            raise FileNotFoundError(source)
        (edition.root / destination_name).write_bytes(source.read_bytes())


def main() -> None:
    for edition in EDITIONS:
        scaffold_edition(edition)
        print(f"Scaffolded {edition.name}")


if __name__ == "__main__":
    main()
