#!/usr/bin/env python3
"""Check the frozen manuscript's source-object inventory.

This gate is intentionally source-shaped.  It checks the native TeX against
the object ledgers produced from the canonical scan, rather than inferring
coverage from the generated PDF.  Draft mode prints findings; ``--strict``
returns a failure for every mismatch.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LATEX = ROOT / "latex"


CHAPTER_FILES: dict[int, tuple[str, ...]] = {
    1: (
        "chapters/chapter01/sec1_1.tex",
        "chapters/chapter01/sec1_2.tex",
        "chapters/chapter01/sec1_3.tex",
        "chapters/chapter01/sec1_4.tex",
    ),
    2: (
        "chapters/chapter02/sec2_1.tex",
        "chapters/chapter02/sec2_2.tex",
        "chapters/chapter02/sec2_3.tex",
        "chapters/chapter02/sec2_4.tex",
        "chapters/chapter02/sec2_5.tex",
        "chapters/chapter02/sec2_6.tex",
    ),
    3: (
        "chapters/chapter03/sec3_1.tex",
        "chapters/chapter03/sec3_2.tex",
        "chapters/chapter03/sec3_3.tex",
        "chapters/chapter03/sec3_4.tex",
        "chapters/chapter03/sec3_5.tex",
    ),
    4: (
        "chapters/chapter04/sec4_1.tex",
        "chapters/chapter04/sec4_2.tex",
        "chapters/chapter04/sec4_3.tex",
        "chapters/chapter04/sec4_4.tex",
        "chapters/chapter04/sec4_5.tex",
        "chapters/chapter04/sec4_6.tex",
    ),
}

EQUATION_COUNTS = {1: 60, 2: 114, 3: 67, 4: 101}
THEOREM_COUNTS = {1: 2, 2: 17, 3: 9, 4: 22}
THEOREM_ENV_COUNTS = {1: 1, 2: 15, 3: 9, 4: 13}
PROOF_ENV_COUNTS = {1: 0, 2: 15, 3: 9, 4: 11}

# Manual theorem headings are source objects too.  The remaining numbered
# results are carried by theorem environments or by the explicit Jost slot in
# Chapter 2.  The parser below reconstructs the shared theorem counter and
# checks the resulting visible sequence.
MANUAL_THEOREM_IDS = {
    1: ("1-1",),
    2: ("2-1",),
    3: (),
    4: ("4-1", "4-6", "4-7", "4-8", "4-9", "4-10", "4-11", "4-12", "4-13"),
}
THEOREM_LABELS = {
    1: {
        "thm:ch1-symmetry",
        "thm:1-2",
    },
    2: {
        "thm:ch2-nuclear",
        "thm:ch2-fourier-distribution-inverse",
        "thm:ch2-fourier-fast-decrease",
        "thm:ch2-separate-holomorphy",
        "thm:ch2-laplace-convexity",
        "thm:ch2-laplace-holomorphy",
        "thm:ch2-laplace-halfspace",
        "thm:ch2-laplace-forward-cone",
        "thm:ch2-laplace-boundary-value",
        "thm:ch2-laplace-tempered-bound",
        "thm:ch2-11",
        "thm:edge-of-wedge-one-variable",
        "thm:edge-of-wedge-product-half-planes",
        "thm:edge-of-wedge-cone",
        "thm:edge-of-wedge-distributional",
        "thm:edge-of-wedge-zero-boundary",
    },
    3: {
        "thm:ch3-reconstruction",
        "thm:ch3-symmetry-uniqueness",
        "thm:ch3-pct",
    },
    4: {
        "thm:ch4-global-locality",
        "thm:ch4-2-reeh-schlieder",
        "thm:ch4-3-separating",
        "thm:ch4-4-adjoined-projection",
        "thm:ch4-5-smeared-fields",
        "thm:ch4-6-neutral-scalar-pct",
        "thm:ch4-7-general-spin-pct",
        "thm:ch4-8",
        "thm:ch4-9-scalar-spin-statistics",
        "thm:ch4-10-general-spin-statistics",
        "thm:ch4-11",
        "thm:ch4-12",
        "thm:ch4-13",
        "thm:ch4-14-unitary-equivalence",
        "thm:ch4-15-jost-schroer",
        "thm:ch4-16-haag",
        "thm:ch4-17-generalized-haag",
        "thm:ch4-18-weak-local-relative",
        "thm:ch4-19-transitivity",
        "thm:ch4-20-asymptotic-fields",
        "thm:ch4-21-relative-locality-transitive",
        "thm:ch4-22-unique-local-solution",
    },
}

LEMMA_MARKER_COUNTS = {1: 0, 2: 2, 3: 0, 4: 0}
COROLLARY_MARKER_COUNTS = {1: 0, 2: 0, 3: 0, 4: 3}
EXAMPLE_MARKER_COUNTS = {1: 0, 2: 0, 3: 3, 4: 3}

BIB_LABELS: dict[int, tuple[str, ...]] = {
    1: tuple(f"ref:1.{index}" for index in range(1, 11)),
    2: tuple(f"pct-{index}" for index in range(1, 26)),
    3: tuple(f"pct-ch3-{index}" for index in range(1, 18)),
    4: tuple(f"ch4-{index}" for index in range(1, 30)),
}

FIGURE_LABELS: dict[str, tuple[str, ...]] = {
    "fig1_1.tex": ("fig:ch1-lorentz-components",),
    "fig1_2.tex": ("fig:ch1-complex-lorentz-components",),
    "fig1_3.tex": ("fig:1-3",),
    "fig2_1.tex": ("fig:2-1", "fig:ch2-contour"),
    "fig2_2.tex": ("fig:2-2",),
    "fig2_3.tex": ("fig:2-3",),
    "fig2_4.tex": ("fig:2-4",),
    "fig2_5.tex": ("fig:2-5", "fig:ch2-edge-wedge-domains"),
    "fig2_6.tex": ("fig:2-6", "fig:ch2-edge-wedge-contours"),
    "fig2_7.tex": ("fig:2-7", "fig:ch2-mobius-map"),
    "figA1.tex": ("fig:A-1",),
    "figA2.tex": ("fig:A-2",),
    "figA3.tex": ("fig:A-3",),
}

EXPECTED_FIGURE_INPUTS = tuple(
    f"figures/{name[:-4]}" for name in FIGURE_LABELS
)


TAG = re.compile(r"\\tag\s*\{([^{}\n]+)\}")
LABEL = re.compile(r"\\label\s*\{([^{}\n]+)\}")
BIBITEM = re.compile(r"\\bibitem(?:\s*\[[^\]]*\])?\s*\{([^{}\n]+)\}")
SPECIAL_BIBITEM = re.compile(r"^\s*\\item\s*\[([^\]]+)\]", re.MULTILINE)
THEOREM_ENV = re.compile(r"\\begin\s*\{theorem\}(?:\[([^\]\n]*)\])?")
MANUAL_THEOREM = re.compile(r"\\textbf\s*\{Theorem\s+([1-4]-\d+)")
SOURCE_KIND = re.compile(r"^\s*%\s*PCT-SOURCE:.*?\bkind=([^\s]+)")
FIGURE_INPUT = re.compile(r"\\input\s*\{([^{}\n]+)")


def uncommented(text: str) -> str:
    """Remove TeX comments while preserving line boundaries."""

    return "\n".join(re.split(r"(?<!\\)%", line, maxsplit=1)[0] for line in text.splitlines())


def read(relative: str) -> str:
    path = LATEX / relative
    return path.read_text(encoding="utf-8") if path.is_file() else ""


def chapter_text(chapter: int) -> str:
    return "\n".join(read(relative) for relative in CHAPTER_FILES[chapter])


def expected_range(chapter: int, count: int) -> list[str]:
    return [f"{chapter}-{index}" for index in range(1, count + 1)]


def check_exact(
    failures: list[str], label: str, actual: object, expected: object
) -> None:
    if actual != expected:
        failures.append(f"{label}: expected {expected!r}, got {actual!r}")


def source_object_markers(text: str, kind: str) -> list[str]:
    result: list[str] = []
    for line in text.splitlines():
        match = SOURCE_KIND.match(line)
        if match and match.group(1) == kind:
            result.append(line)
    return result


def check_equations(failures: list[str]) -> None:
    for chapter, expected_count in EQUATION_COUNTS.items():
        tags = TAG.findall(uncommented(chapter_text(chapter)))
        expected = expected_range(chapter, expected_count)
        check_exact(failures, f"Chapter {chapter} numbered equations", tags, expected)

    constructive = TAG.findall(uncommented(read("appendix/constructive.tex")))
    local = TAG.findall(uncommented(read("appendix/local-algebras.tex")))
    check_exact(failures, "Appendix constructive equation tags", constructive, ["A.1", "A.2"])
    check_exact(failures, "Appendix local-algebra equation tags", local, ["1", "2", "3", "4"])


def infer_theorem_sequence(chapter: int, failures: list[str]) -> list[str]:
    """Reconstruct the visible theorem counter from source-order TeX tokens."""

    text = uncommented(chapter_text(chapter))
    token = re.compile(
        r"(?P<set>\\setcounter\s*\{theorem\}\s*\{(?P<set_n>\d+)\})"
        r"|(?P<ref>\\refstepcounter\s*\{theorem\})"
        r"|(?P<step>\\stepcounter\s*\{theorem\})"
        r"|(?P<manual>\\textbf\s*\{Theorem\s+(?P<manual_id>[1-4]-\d+))"
        r"|(?P<env>\\begin\s*\{theorem\}(?:\[(?P<env_option>[^\]\n]*)\])?)"
    )
    counter = 0
    sequence: list[str] = []
    manual: list[str] = []
    env_count = 0
    for match in token.finditer(text):
        if match.group("set"):
            counter = int(match.group("set_n"))
        elif match.group("ref"):
            counter += 1
        elif match.group("step"):
            counter += 1
            # Chapter 2's Jost theorem is a source result slot introduced in
            # prose.  The explicit counter step is its native identity hook.
            sequence.append(f"{chapter}-{counter}")
        elif match.group("manual"):
            identifier = match.group("manual_id")
            manual.append(identifier)
            sequence.append(identifier)
            expected_number = int(identifier.split("-")[1])
            if expected_number not in (counter, counter + 1):
                failures.append(
                    f"Chapter {chapter} manual theorem {identifier}: "
                    f"counter is {counter}"
                )
            # Manual source headings do not execute amsthm's counter step.
            counter = expected_number
        elif match.group("env"):
            env_count += 1
            option = match.group("env_option")
            if option:
                number_match = re.match(r"\s*([1-4]-\d+)", option)
                if number_match is None:
                    failures.append(
                        f"Chapter {chapter} theorem option has no numeric identifier: {option!r}"
                    )
                    continue
                identifier = number_match.group(1)
                expected_number = int(identifier.split("-")[1])
                if expected_number != counter + 1:
                    failures.append(
                        f"Chapter {chapter} theorem environment {identifier}: "
                        f"counter is {counter}, expected {counter + 1}"
                    )
                counter = expected_number
            else:
                counter += 1
                identifier = f"{chapter}-{counter}"
            sequence.append(identifier)

    expected = expected_range(chapter, THEOREM_COUNTS[chapter])
    check_exact(failures, f"Chapter {chapter} theorem sequence", sequence, expected)
    check_exact(failures, f"Chapter {chapter} manual theorem headings", manual, list(MANUAL_THEOREM_IDS[chapter]))
    check_exact(failures, f"Chapter {chapter} theorem environments", env_count, THEOREM_ENV_COUNTS[chapter])
    return sequence


def check_results(failures: list[str]) -> None:
    for chapter in CHAPTER_FILES:
        text = chapter_text(chapter)
        code = uncommented(text)
        infer_theorem_sequence(chapter, failures)
        theorem_labels = {label for label in LABEL.findall(code) if label.startswith("thm:")}
        check_exact(failures, f"Chapter {chapter} theorem labels", theorem_labels, THEOREM_LABELS[chapter])
        check_exact(
            failures,
            f"Chapter {chapter} proof environments",
            len(re.findall(r"\\begin\s*\{proof\}", code)),
            PROOF_ENV_COUNTS[chapter],
        )
        check_exact(
            failures,
            f"Chapter {chapter} source proof markers",
            len(source_object_markers(text, "proof")),
            {1: 0, 2: 17, 3: 9, 4: 21}[chapter],
        )
        check_exact(
            failures,
            f"Chapter {chapter} lemma markers",
            len(source_object_markers(text, "lemma")),
            LEMMA_MARKER_COUNTS[chapter],
        )
        check_exact(
            failures,
            f"Chapter {chapter} corollary markers",
            len(source_object_markers(text, "corollary")),
            COROLLARY_MARKER_COUNTS[chapter],
        )
        check_exact(
            failures,
            f"Chapter {chapter} example markers",
            len(source_object_markers(text, "example")),
            EXAMPLE_MARKER_COUNTS[chapter],
        )


def check_bibliographies(failures: list[str]) -> None:
    for chapter, expected_tuple in BIB_LABELS.items():
        relative = f"chapters/chapter0{chapter}/bibliography.tex"
        code = uncommented(read(relative))
        labels = BIBITEM.findall(code)
        check_exact(failures, f"Chapter {chapter} bibliography labels", labels, list(expected_tuple))
        check_exact(failures, f"Chapter {chapter} bibliography count", len(labels), len(expected_tuple))
        if chapter == 4:
            special = SPECIAL_BIBITEM.findall(code)
            check_exact(failures, "Chapter 4 special bibliography labels", special, ["19a."])

    appendix_code = uncommented(read("appendix/bibliography.tex"))
    appendix_labels = BIBITEM.findall(appendix_code)
    expected_appendix = [f"pct-app-{index}" for index in range(1, 92)]
    check_exact(failures, "Appendix bibliography labels", appendix_labels, expected_appendix)
    check_exact(failures, "Appendix bibliography count", len(appendix_labels), 91)
    optional = re.findall(r"\\bibitem\s*\[([^\]]+)\]", appendix_code)
    check_exact(failures, "Appendix visible bibliography labels", optional, [str(index) for index in range(1, 92)])


def check_figures(failures: list[str]) -> None:
    figure_dir = LATEX / "figures"
    actual_files = sorted(path.name for path in figure_dir.glob("*.tex")) if figure_dir.is_dir() else []
    expected_files = sorted(FIGURE_LABELS)
    check_exact(failures, "Native figure files", actual_files, expected_files)
    for filename, expected_labels in FIGURE_LABELS.items():
        code = uncommented(read(f"figures/{filename}"))
        labels = LABEL.findall(code)
        check_exact(failures, f"{filename} labels", labels, list(expected_labels))
        check_exact(failures, f"{filename} figure environments", code.count(r"\begin{figure}"), 1)
        check_exact(failures, f"{filename} captions", len(re.findall(r"\\caption\s*\{", code)), 1)

    input_text = "\n".join(
        uncommented(read(relative))
        for files in (CHAPTER_FILES, {0: ("appendix/constructive.tex", "appendix/local-algebras.tex")})
        for group in files.values()
        for relative in group
    )
    actual_inputs: list[str] = []
    for value in FIGURE_INPUT.findall(input_text):
        if not value.startswith("figures/"):
            continue
        normalized = value[:-4] if value.endswith(".tex") else value
        actual_inputs.append(normalized)
    check_exact(failures, "Figure input hooks", sorted(actual_inputs), sorted(EXPECTED_FIGURE_INPUTS))


def check_appendix_and_index(failures: list[str]) -> None:
    constructive = uncommented(read("appendix/constructive.tex"))
    local = uncommented(read("appendix/local-algebras.tex"))
    check_exact(failures, "Appendix visible section headings", re.findall(r"\\section\*\s*\{([^}]+)\}", constructive), ["APPENDIX"])
    check_exact(
        failures,
        "Appendix visible subsection headings",
        re.findall(r"\\subsection\*\s*\{([^}]+)\}", constructive + "\n" + local),
        [
            "Constructive Quantum Field Theory and the Existence of Non-Trivial Theories of Interacting Fields",
            "Local Algebras and Superselection Sectors",
        ],
    )
    for name, code in (("constructive.tex", constructive), ("local-algebras.tex", local)):
        if re.search(r"\\section(?!\*)\s*\{", code):
            failures.append(f"Appendix {name}: numbered section heading found")
        if re.search(r"\\subsection(?!\*)\s*\{", code):
            failures.append(f"Appendix {name}: numbered subsection heading found")
    check_exact(failures, "Appendix internal section counter step", constructive.count(r"\refstepcounter{section}"), 1)
    check_exact(failures, "Appendix theorem paragraphs", len(re.findall(r"\\paragraph\s*\{\\textbf\{Theorem\}\}", local)), 1)
    check_exact(failures, "Appendix proof environments", len(re.findall(r"\\begin\s*\{proof\}", constructive + local)), 0)

    index = uncommented(read("backmatter/index.tex"))
    check_exact(failures, "Index environments", (index.count(r"\begin{theindex}"), index.count(r"\end{theindex}")), (1, 1))
    main_items = len(re.findall(r"^\s*\\item(?![A-Za-z])", index, re.MULTILINE))
    subitems = len(re.findall(r"^\s*\\subitem(?![A-Za-z])", index, re.MULTILINE))
    indexspaces = len(re.findall(r"^\s*\\indexspace\b", index, re.MULTILINE))
    check_exact(failures, "Index main entries", main_items, 205)
    check_exact(failures, "Index subentries", subitems, 24)
    check_exact(failures, "Index item lines", main_items + subitems, 229)
    check_exact(failures, "Index space divisions", indexspaces, 20)


def check_master_assembly(failures: list[str]) -> None:
    master = read("master.tex")
    inputs = re.findall(r"\\PCTInput\s*\{([^}\n]+)\}", uncommented(master))
    expected = [
        "frontmatter/copyright.tex",
        "frontmatter/preface.tex",
        "frontmatter/introduction.tex",
        "chapters/chapter01/opening.tex",
        *CHAPTER_FILES[1],
        "chapters/chapter01/bibliography.tex",
        "chapters/chapter02/opening.tex",
        *CHAPTER_FILES[2],
        "chapters/chapter02/bibliography.tex",
        "chapters/chapter03/opening.tex",
        *CHAPTER_FILES[3],
        "chapters/chapter03/bibliography.tex",
        "chapters/chapter04/opening.tex",
        *CHAPTER_FILES[4],
        "chapters/chapter04/bibliography.tex",
        "appendix/constructive.tex",
        "appendix/local-algebras.tex",
        "appendix/bibliography.tex",
        "backmatter/index.tex",
    ]
    check_exact(failures, "Master PCTInput assembly", inputs, expected)
    check_exact(failures, "Master appendix command", uncommented(master).count(r"\appendix"), 1)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--strict", action="store_true", help="return failure on any inventory mismatch")
    args = parser.parse_args()
    failures: list[str] = []

    check_master_assembly(failures)
    check_equations(failures)
    check_results(failures)
    check_bibliographies(failures)
    check_figures(failures)
    check_appendix_and_index(failures)

    print("Object inventory gate")
    print(f"  Chapters checked: {', '.join(str(chapter) for chapter in CHAPTER_FILES)}")
    print("  Equation ranges: 1-1..1-60, 2-1..2-114, 3-1..3-67, 4-1..4-101")
    print("  Theorem ranges: 1-1..1-2, 2-1..2-17, 3-1..3-9, 4-1..4-22")
    print("  Figure files checked: 13")
    print("  Bibliography counts: chapters 10/25/17/30, Appendix 91")
    print("  Index counts: 205 main, 24 subentries, 20 divisions")
    if failures:
        print("OBJECT INVENTORY FAILURES", file=sys.stderr)
        for failure in failures:
            print(f"  - {failure}", file=sys.stderr)
        if args.strict:
            return 1
        print("Draft mode: inventory findings are reported and do not stop the pilot build.")
    else:
        print("Object inventory gate passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
