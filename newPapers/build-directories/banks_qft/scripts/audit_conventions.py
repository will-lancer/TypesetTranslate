#!/usr/bin/env python3
"""Audit the mathematical convention closure used by a Banks QFT edition.

The project audit checks structure and inventory.  This audit checks the small
set of convention changes which can alter the meaning of an otherwise faithful
transcription.  It deliberately reports source-preservation prose separately
from active TeX and reads the exact native input closure selected by
``audit_project.edition_sources``.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Iterable

from audit_project import edition_sources, native_snapshot_sha256


ROOT = Path(__file__).resolve().parents[1]

# These are the package records which describe or index adapted mathematics.
# Review reports under work/ are intentionally excluded: they are historical
# evidence and often quote the source convention while explaining a repair.
CONVENTION_DOCS = (
    "AUTHORING_CONVENTIONS.md",
    "ERRATA.md",
    "IMPLICIT_EXERCISES.md",
    "IMPLICIT_INVENTORY_DECISIONS.md",
    "NOTATION.md",
    "README.md",
    "SOURCE_MANIFEST.yaml",
    "SOURCE_MAP.md",
    "TRANSCRIPTION_CONTRACT.md",
    "TRANSCRIPTION_STATUS.md",
    "figures.json",
    "implicit-exercises.json",
    "numbered-equations.json",
    "unnumbered-diagrams.json",
)

SCOPE_MARKER_RE = re.compile(
    r"CONVENTION[-_ ]SCOPE\s*:\s*(?:fixed[-_ ]?)?D\s*=\s*4(?:\s+reason\s*=\s*(?P<reason>[^\n%]+))?",
    re.IGNORECASE,
)

HISTORICAL_RE = re.compile(
    # Keep this contextual rather than treating every use of "source",
    # "original", or "Banks" as a historical-convention escape hatch.  A
    # nearby source-form sentence should protect the source formula it is
    # describing, while ordinary phrases such as "source term" remain live.
    r"(?:\b(?:source|printed|old|historical|original|adopted)\s+"
    r"(?:convention|form|notation|formula|expression|metric|sign|kernel|"
    r"denominator|equation|version|text|dimension|phase)\b|"
    r"\b(?:mostly[- ]minus|west\s+coast)\b|"
    r"\b(?:in|under|from)\s+(?:the\s+)?(?:source|printed|old|original)\b|"
    r"\bBanks(?:['’]s)?\s+(?:source|original|printed)\b)",
    re.IGNORECASE,
)

# The package uses d_{\\mathrm{reg}} for dimensional regularization.  These
# labels are common source-style aliases and need explicit review.  The
# matcher is deliberately limited to labels that unambiguously mean
# dimensional regularization, so legitimate labels such as d_R (a group
# representation dimension) and d_s (a static spatial dimension) remain
# untouched.
DIMREG_ALIAS_RE = re.compile(
    r"(?<![A-Za-z\\])d\s*_\s*"
    r"(?P<body>\{(?:[^{}]|\{[^{}]*\})*\}|"
    r"\\(?:rm|mathrm|text)\s*(?:\{[^{}]*\}|[A-Za-z]+)|"
    r"[A-Za-z]+)",
    re.IGNORECASE,
)
NONCANONICAL_DIMREG_LABELS = frozenset(
    {
        "dr",
        "dimreg",
        "dimensionalreg",
        "dimensionalregularization",
    }
)

# These atom patterns are shared by shell, pole, and propagator checks.  An
# indexed mass is still one mass token: m_0, m_A, m_{\\rm vector}, M_i, and
# \\mu_V all need the same mostly-plus sign audit as bare m and M.
MASS_INDEX = (
    r"(?:m|M|\\mu)"
    r"(?:\s*_\s*(?:\{(?:[^{}]|\{[^{}]*\})*\}|\\[A-Za-z]+|[A-Za-z0-9]))?"
)
MASS_SQUARED = rf"{MASS_INDEX}\s*\^\s*\{{?2\}}?"

# A Levi--Civita object with an explicitly dimension-labelled Lorentz index
# is only ambiguous in the dimensional-regularization discussion.  The
# direct \\mu_d form is unambiguous; the broader raw-d fallback is gated by a
# nearby dimensional-regularization cue below.
EPSILON_INDEX_RE = re.compile(
    r"\\(?:epsilon|varepsilon)\s*[_^]\s*"
    r"(?P<body>\{[^{}\n]*\}|[A-Za-z0-9])",
    re.IGNORECASE,
)
DIMENSION_INDEX_RE = re.compile(
    r"\\(?:mu|nu|rho|sigma|alpha|beta|lambda|kappa|ell)\s*_\s*"
    r"\{?\s*d\s*\}?\b",
    re.IGNORECASE,
)

# A bare d^D w in native TikZ/text is a differential measure, not an
# exponentiated variable.  Restrict this check to a likely measure context
# or a figure so ordinary uses of d as a variable stay untouched.
BARE_DIFFERENTIAL_MEASURE_RE = re.compile(
    r"(?<![A-Za-z\\])d\s*\^\s*"
    r"(?P<dimension>\{\s*(?:D|d)\s*\}|D|d)"
    r"(?P<tail>(?:\s|\\[,;:!~ ]|\\!|\\;|\\,|\\:)*"
    r"(?:\\(?:mathrm|text)\s*)?(?:\{?[A-Za-z]\}?|"
    r"\\(?:mathbf|boldsymbol)\s*(?:\{[^{}]*\}|[A-Za-z])))",
    re.IGNORECASE,
)

FIXED_DIMENSION_CUE_RE = re.compile(
    r"\b(?:D\s*=\s*4|4\s*[- ]?dimensional|four[- ]dimensional|four\s+dimensions?|"
    r"three\s+spatial|instanton|anomal(?:y|ies)|Hodge|chirality|gamma[_ ]?5|"
    r"4[- ]index(?:ed)?\s+(?:epsilon|Levi[- ]Civita)|fixed\s+physical\s+dimension)\b",
    re.IGNORECASE,
)

DIMREG_CUE_RE = re.compile(
    r"\b(?:dimensional\s+regulari[sz]ation|dimreg|loop\s+dimension|"
    r"d[_ ]?reg|\varepsilon[_ ]?UV|epsilon[_ ]?UV)\b",
    re.IGNORECASE,
)

SPATIAL_NAMES = frozenset("pqkrlxyPQRKRLXY")

# A compact mixed-index delta is explicitly allowed by NOTATION.md.  The
# remaining command names are tensor-like; ordinary operator commands are
# excluded before the candidate is recorded.
TENSOR_COMMANDS = frozenset(
    {
        "eta",
        "epsilon",
        "varepsilon",
        "gamma",
        "sigma",
        "Pi",
        "Gamma",
        "Lambda",
        "Omega",
        "Phi",
        "Psi",
        "Theta",
        "Delta",
        "Sigma",
        "Xi",
        "Upsilon",
        "rho",
        "tau",
        "kappa",
        "chi",
        "varphi",
        "varpi",
        "varrho",
        "vartheta",
        "ell",
    }
)
OPERATOR_COMMANDS = frozenset(
    {
        "above",
        "acute",
        "bar",
        "begin",
        "bigl",
        "bigr",
        "braket",
        "caption",
        "cdot",
        "centering",
        "DeclareMathOperator",
        "dd",
        "det",
        "displaybreak",
        "end",
        "exp",
        "frac",
        "hbox",
        "hspace",
        "includegraphics",
        "input",
        "int",
        "item",
        "label",
        "left",
        "mathbb",
        "mathbf",
        "mathcal",
        "mathrm",
        "mathsf",
        "operatorname",
        "overline",
        "partial",
        "prod",
        "ref",
        "right",
        "sqrt",
        "sum",
        "text",
        "textbf",
        "textit",
        "texttt",
        "tilde",
        "underbrace",
        "underline",
        "url",
        "vec",
        "widehat",
        "widetilde",
    }
)

HEADING_RE = re.compile(r"(?:\\(?:sub)*section\*?|^#{1,6})")

MIXED_INDEX_RE = re.compile(
    rf"(?P<base>\\[A-Za-z]+(?:\s*\{{[A-Za-z]\}})?|[A-Za-z])"
    rf"(?P<first_kind>[\^_])\s*(?P<first_body>\{{[^{{}}\n]*\}}|\\[A-Za-z]+|[A-Za-z0-9])"
    rf"(?P<second_kind>[\^_])\s*(?P<second_body>\{{[^{{}}\n]*\}}|\\[A-Za-z]+|[A-Za-z0-9])"
)


def relpath(path: Path) -> str:
    """Return a stable package-relative path."""

    return path.resolve().relative_to(ROOT.resolve()).as_posix()


def strip_tex_comment(line: str) -> str:
    """Drop an unescaped TeX comment without changing line numbering."""

    for index, char in enumerate(line):
        if char != "%":
            continue
        backslashes = 0
        cursor = index - 1
        while cursor >= 0 and line[cursor] == "\\":
            backslashes += 1
            cursor -= 1
        if backslashes % 2 == 0:
            # A scope marker is an intentional part of the live audit
            # contract.  Retain just that marker when it occurs in a TeX
            # comment so numeric D=4 formulas can be scoped locally without
            # reintroducing historical commented-out formulas.
            marker = SCOPE_MARKER_RE.search(line[index:])
            if marker:
                return f"{line[:index]} {marker.group(0)}"
            return line[:index]
    return line


def source_lines(path: Path, text: str) -> list[str]:
    """Return scanable lines for TeX or package metadata."""

    if path.suffix == ".tex" or path.suffix == ".sty":
        return [strip_tex_comment(line) for line in text.splitlines()]
    return text.splitlines()


def errata_lines(text: str) -> list[str]:
    """Keep only adopted forms in ERRATA.md.

    Source forms are preserved as evidence and may intentionally use the
    original metric.  The adopted-form field is part of the live package
    contract and is therefore audited.
    """

    selected: list[str] = []
    active = False
    for line in text.splitlines():
        if re.match(r"\s*-\s*Adopted form\s*:", line, re.IGNORECASE):
            active = True
            selected.append(line)
            continue
        if active and re.match(r"\s*-\s*[A-Za-z][A-Za-z _-]*\s*:", line):
            active = False
        if active:
            selected.append(line)
    return selected


def package_doc_inputs() -> dict[Path, list[str]]:
    """Load existing convention-bearing docs in a deterministic order."""

    result: dict[Path, list[str]] = {}
    for name in CONVENTION_DOCS:
        path = ROOT / name
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        if name == "ERRATA.md":
            result[path] = errata_lines(text)
        else:
            result[path] = source_lines(path, text)
    return dict(sorted(result.items(), key=lambda item: relpath(item[0])))


def line_context(lines: list[str], index: int, radius: int = 4) -> str:
    """Return nearby text plus the current section's heading context."""

    start = max(0, index - radius)
    end = min(len(lines), index + radius + 1)
    chunks = lines[start:end]
    section_start = None
    for position in range(index, -1, -1):
        if HEADING_RE.search(lines[position]):
            section_start = position
            break
    if section_start is not None:
        chunks.extend(lines[section_start : index + 1])
    return "\n".join(chunks)


def historical_context(context: str) -> bool:
    """Whether nearby prose is explicitly describing source/history."""

    return HISTORICAL_RE.search(context) is not None


def normalise_tex_label(value: str) -> str:
    """Strip the small set of TeX wrappers used for dimension labels."""

    value = re.sub(r"\\(?:rm|mathrm|text|operatorname)\s*", "", value)
    return re.sub(r"[{}\\\s]", "", value).lower()


def figure_path(path: Path) -> bool:
    """Whether a package-relative input is a native figure source."""

    return "figures" in path.resolve().parts


def euclidean_context(context: str) -> bool:
    """Whether nearby prose marks a formula as Euclidean/heat-kernel data."""

    return bool(
        re.search(
            r"(?:\bEuclidean\b|heat[- ]kernel|proper[- ]time|Schwinger|"
            r"elliptic|Euclidean\s+continuation|Wick\s+rotation)",
            context,
            re.IGNORECASE,
        )
    )


def fixed_dimension_context(path: Path, lines: list[str], index: int) -> bool:
    """Whether a numeric four-dimensional formula is locally scoped."""

    context = line_context(lines, index, radius=6)
    return bool(SCOPE_MARKER_RE.search(context) or FIXED_DIMENSION_CUE_RE.search(context))


def dimreg_context(lines: list[str], index: int) -> bool:
    return bool(DIMREG_CUE_RE.search(line_context(lines, index, radius=6)))


def normalise_index_body(body: str) -> str:
    body = re.sub(r"[{}\\,;!~ ]", "", body)
    return body


def has_spacetime_index(body: str) -> bool:
    return spacetime_index_count(body) > 0


def spacetime_index_count(body: str) -> int:
    """Count explicit Lorentz-index commands in one TeX script."""

    names = (
        "mu",
        "nu",
        "rho",
        "sigma",
        "lambda",
        "kappa",
        "alpha",
        "beta",
        "gamma",
        "delta",
        "ell",
    )
    return sum(len(re.findall(rf"\\{name}(?![A-Za-z])", body)) for name in names)


def tensor_base(base: str) -> tuple[str, str]:
    """Return raw base and control-sequence name."""

    raw = base.strip()
    match = re.fullmatch(r"\\([A-Za-z]+)(?:\s*\{([A-Za-z])\})?", raw)
    if match:
        command, qualifier = match.groups()
        return raw, command if qualifier is None else f"{command}{{{qualifier}}}"
    return raw, raw


def is_credible_mixed_candidate(base: str, upper: str, lower: str) -> bool:
    """Filter operator scripts and representation labels from mixed indices."""

    raw, name = tensor_base(base)
    if name in OPERATOR_COMMANDS:
        return False
    if name in {"delta", "Delta"}:
        return False
    # Parenthesized labels, textual qualifiers, and a numeric component label
    # are not tensor scripts.  They occur frequently on polarization vectors,
    # representation matrices, and named sources.
    def label_script(body: str) -> bool:
        if re.fullmatch(
            r"\s*\{?\s*\\(?:dagger|ddagger|ast|star|prime|doubleprime|"
            r"infty|top|bot)\s*\}?\s*",
            body,
            re.IGNORECASE,
        ):
            return True
        if re.search(r"\\(?:rm|mathrm|text|operatorname)\b", body):
            return True
        if re.search(r"[()]", body):
            return True
        cleaned = re.sub(r"\\(?:[,;:!~]|\s)", "", body)
        cleaned = re.sub(r"[{}\s]", "", cleaned)
        if re.fullmatch(r"[0-9,+-]+", cleaned or ""):
            return True
        if re.fullmatch(r"[A-Z](?:,[A-Z])+(?:,[A-Z])*", cleaned or ""):
            return True
        if re.fullmatch(r"[A-Z]", cleaned or "") and not has_spacetime_index(body):
            return True
        return False

    upper_is_label = label_script(upper)
    lower_is_label = label_script(lower)
    if upper_is_label or lower_is_label:
        # A representation, polarization, or component label is adjacent to
        # a Lorentz script in many source formulas.  It is not the tensor
        # upper/lower pair covered by this audit.  A genuinely mixed pair on
        # both sides remains eligible even when one side carries a qualifier.
        if re.search(r"[()]", upper) or re.search(r"[()]", lower):
            return False
        if not (has_spacetime_index(upper) and has_spacetime_index(lower)):
            return False
    upper_count = spacetime_index_count(upper)
    lower_count = spacetime_index_count(lower)
    if upper_count + lower_count == 1:
        one_script = upper if upper_count == 0 else lower
        other_script = lower if upper_count == 0 else upper
        if (
            re.fullmatch(r"\s*\{?\s*[a-z]\s*\}?\s*", one_script)
            and spacetime_index_count(other_script) == 1
        ):
            # A lone Latin subscript/superscript next to one Lorentz index is
            # normally a polarization or species label, as in epsilon_r^mu.
            return False
    if name == "D" and normalise_index_body(upper).lower() in {"j", "j1", "j2"}:
        # D^j_{kl} is the standard representation-matrix label used in the
        # Lorentz-group discussion, rather than a mixed tensor index.
        if not has_spacetime_index(upper) and not has_spacetime_index(lower):
            return False
    if name.startswith("math"):
        return True
    if name in TENSOR_COMMANDS:
        return True
    if raw.startswith("\\"):
        return False
    if not raw.isalpha():
        return False
    if upper_count and lower_count:
        return True
    # A single Lorentz script adjacent to an internal or representation label
    # is ordinary field notation such as A_mu^a.  A block with two or more
    # Lorentz scripts is a tensor expression and needs the explicit group.
    if max(upper_count, lower_count) >= 2:
        return True
    return False


def add_record(
    records: list[dict[str, object]],
    *,
    category: str,
    path: Path,
    line: int,
    message: str,
    snippet: str,
    severity: str = "error",
) -> None:
    records.append(
        {
            "category": category,
            "file": relpath(path),
            "line": line,
            "message": message,
            "severity": severity,
            "snippet": " ".join(snippet.strip().split()),
        }
    )


def add_candidate(
    candidates: list[dict[str, object]],
    *,
    category: str,
    path: Path,
    line: int,
    reason: str,
    snippet: str,
) -> None:
    candidates.append(
        {
            "category": category,
            "file": relpath(path),
            "line": line,
            "reason": reason,
            "snippet": " ".join(snippet.strip().split()),
            "status": "reviewed",
        }
    )


def delta_argument(tail: str) -> str:
    """Return the first balanced parenthesized delta argument."""

    start = tail.find("(")
    if start < 0:
        return ""
    depth = 0
    for index in range(start, len(tail)):
        char = tail[index]
        if char == "(":
            depth += 1
        elif char == ")":
            depth -= 1
            if depth == 0:
                return tail[start + 1 : index]
    return tail[start + 1 :]


def scan_metric_and_propagators(
    path: Path,
    lines: list[str],
    findings: list[dict[str, object]],
    candidates: list[dict[str, object]],
) -> None:
    """Check signature, shells, propagator signs, and field conventions."""

    metric_old_re = re.compile(
        r"(?:(?:\\(?:operatorname|mathrm|text)\s*\{\s*)?diag\s*(?:\}\s*)?\(\s*(?:\+|1)\s*,\s*-|"
        r"(?:\\eta|(?<![A-Za-z])g)\s*(?:[_^]\s*\{[^{}]*\}\s*)?(?:=|:)\s*"
        r"\(?\s*(?:\+|1)\s*,\s*-|"
        r"(?:signature|metric)\s*(?:[=:]\s*)?\(?\s*\+\s*,\s*-)",
        re.IGNORECASE,
    )
    metric_object_re = re.compile(
        r"(?:\\eta(?![A-Za-z])|(?<![A-Za-z])g\s*(?:[_^=])|\b(?:signature|metric)\b)",
        re.IGNORECASE,
    )
    spacelike_old_re = re.compile(
        r"spacelike[^\n]{0,100}(?:\^\s*\{?2\}?|squared)[^\n]{0,30}<\s*0",
        re.IGNORECASE,
    )
    timelike_old_re = re.compile(
        r"timelike[^\n]{0,100}(?:\^\s*\{?2\}?|squared)[^\n]{0,30}>\s*0",
        re.IGNORECASE,
    )
    old_norm_formula_re = re.compile(
        r"(?<![A-Za-z])(?:x|p|q|k)\s*\^\s*\{?2\}?\s*=\s*"
        r"[^=\n]{0,60}-\s*(?:\\mathbf|\\vec)\b",
    )
    old_dot_formula_re = re.compile(
        r"(?<![A-Za-z])(?:p|q|k|x)\s*"
        r"(?:\\cdot|\\mathbin\s*\{?\\cdot\}?)\s*"
        r"(?:p|q|k|x)\s*=\s*[^=()\n]{0,80}-\s*(?:\\mathbf|\\vec)\b",
    )
    shell_old_re = re.compile(
        r"(?<![A-Za-z])(?:p|q|k|r|l|\\ell)\s*\^\s*\{?2\}?\s*=\s*"
        rf"{MASS_SQUARED}(?![A-Za-z])",
    )
    contracted_shell_old_re = re.compile(
        r"(?<![A-Za-z])(?:p|q|k|r|l|\\ell)\s*_\s*\{?\\(?:mu|nu|rho|sigma|alpha|beta)\}?\s*"
        r"(?:p|q|k|r|l|\\ell)\s*\^\s*\{?\\(?:mu|nu|rho|sigma|alpha|beta)\}?\s*=\s*"
        rf"{MASS_SQUARED}(?![A-Za-z])",
    )
    mass_difference_re = re.compile(
        r"(?<![A-Za-z])(?:p|q|k|r|l|\\ell)\s*\^\s*\{?2\}?\s*-\s*"
        rf"{MASS_SQUARED}(?![A-Za-z])",
    )
    propagator_denominator_re = re.compile(
        r"(?:/|\\frac\s*(?:\{[^{}\n]*\}|[^\s{])\s*\{|\bdenominator\b)[^\n]{0,80}"
        r"(?<![A-Za-z])(?:p|q|k|r|l|\\ell)\s*\^\s*\{?2\}?\s*-\s*"
        rf"{MASS_SQUARED}(?![A-Za-z])",
        re.IGNORECASE,
    )
    scalar_operator_old_re = re.compile(
        r"(?:\\Box|\\partial\s*\^\s*2|\\partial_\{?\\mu\}?"
        rf"\s*\\partial\s*\^\s*\\mu)[^\n]{{0,40}}\+\s*{MASS_SQUARED}",
    )
    scalar_kinetic_old_re = re.compile(
        r"(?:\\mathcal\s*\{?L\}?\s*(?:[_^]\s*\{?[^}\n]*\}?)?|\bL)\s*=.{0,180}"
        r"\+\s*\\frac\s*\{?1\}?\s*\{?2\}?[^\n]{0,80}"
        r"(?:\\partial|\\nabla)[^\n]{0,50}(?:phi|varphi|\\phi|\\varphi)",
        re.IGNORECASE,
    )
    dirac_lagrangian_old_re = re.compile(
        r"\\bar\s*\\psi\s*\(\s*(?:\\ii|i)\s*"
        r"(?:\\slashed\s*\\partial|\\gamma\s*\^|\\gamma)"
        r"[^\n]{0,80}-\s*m\b",
    )
    dirac_equation_old_re = re.compile(
        r"\(\s*(?:\\ii|i)\s*(?:\\slashed\s*\\partial|\\gamma\s*\^|\\gamma)"
        r"[^\n]{0,60}-\s*m\s*\)\s*\\?(?:psi|Psi)\s*=\s*0",
    )
    proca_mass_old_re = re.compile(
        r"\+\s*\\frac\s*\{?1\}?\s*\{?2\}?[^\n]{0,45}"
        rf"{MASS_SQUARED}[^\n]{{0,45}}A\s*[_\^]",
    )
    proca_polarization_old_re = re.compile(
        r"\\eta\s*\^?\s*\{[^{}]*\}\s*-\s*"
        r"p\s*\^?\s*\{?[^{}]*\}?\s*p\s*\^?\s*\{?[^{}]*\}?\s*/\s*m",
    )
    proca_polarization_fraction_old_re = re.compile(
        r"\\eta\s*\^?\s*\{[^{}]*\}\s*-\s*"
        r"\\frac\s*\{[^{}\n]*p\s*\^?\s*\{?[^{}]*\}?\s*p\s*\^?\s*\{?[^{}]*\}?\s*\}"
        r"\s*\{[^{}\n]*m\s*\^?\s*\{?2\}?\s*\}",
    )
    clifford_old_re = re.compile(
        r"(?:\[\s*\\gamma[^\n]*\]_\+|\{\s*\\gamma[^\n]*\})"
        r"\s*=\s*\+?2\s*\\eta",
    )
    expanded_clifford_old_re = re.compile(
        r"\\gamma\s*\^\s*\{?\\[A-Za-z]+\}?[^\n]{0,20}"
        r"\+\s*\\gamma\s*\^\s*\{?\\[A-Za-z]+\}?[^\n]{0,20}"
        r"=\s*\+?2\s*\\eta",
    )
    trace_old_re = re.compile(
        r"(?:tr|operatorname\s*\{?tr\}?)[^\n]*\\gamma\s*\^?\s*\{?\\mu\}?"
        r"[^\n]*\\gamma\s*\^?\s*\{?\\nu\}?[^\n]*=\s*4\s*\\eta",
        re.IGNORECASE,
    )
    contraction_old_re = re.compile(
        r"\\gamma\s*\^\s*\{?\\lambda\}?\s*"
        r"\\gamma\s*_\s*\{?\\(?:mu|nu|rho|sigma|alpha|beta|kappa)\}?\s*"
        r"\\gamma\s*_\s*\{?\\lambda\}?\s*=\s*-\s*2\s*\\gamma",
    )
    epsilon_orientation_old_re = re.compile(
        r"(?:\\epsilon|epsilon)\s*_\s*\{?\s*0\s*1\s*2\s*3\s*\}?\s*=\s*\+\s*1",
        re.IGNORECASE,
    )
    gamma5_orientation_old_re = re.compile(
        r"\\gamma\s*_\s*\{?5\}?\s*(?:=|\\equiv)\s*-\s*(?:\\ii|i)\s*\\gamma",
        re.IGNORECASE,
    )

    for index, line in enumerate(lines):
        # Convention qualifiers often sit in the prose line immediately
        # before a displayed formula.  Keep the context local, but wide
        # enough to include that lead-in and the display's continuation.
        context = line_context(lines, index, radius=6)
        historical = historical_context(context)
        euclidean_operator = euclidean_context(context)

        for alias in DIMREG_ALIAS_RE.finditer(line):
            label = normalise_tex_label(alias.group("body"))
            if label in NONCANONICAL_DIMREG_LABELS and not historical:
                add_record(
                    findings,
                    category="dimreg-symbol",
                    path=path,
                    line=index + 1,
                    message="Dimensional regularization uses a noncanonical dimension alias; use d_reg.",
                    snippet=line,
                )

        for epsilon in EPSILON_INDEX_RE.finditer(line):
            body = epsilon.group("body")
            regulator_context = dimreg_context(lines, index)
            enumerated_dimension_indices = bool(
                re.search(
                    r"\\(?:mu|nu|rho|sigma|alpha|beta|lambda|kappa|ell)"
                    r"\s*_\s*\{?\s*[0-9]+\s*\}?",
                    body,
                    re.IGNORECASE,
                )
            )
            raw_dimension_index = bool(
                (
                    DIMENSION_INDEX_RE.search(body)
                    and (regulator_context or enumerated_dimension_indices)
                )
                or (
                    re.search(r"(?<![A-Za-z\\])d(?![A-Za-z])", body)
                    and regulator_context
                )
            )
            if raw_dimension_index and not historical:
                add_record(
                    findings,
                    category="raw-dimensional-regularization",
                    path=path,
                    line=index + 1,
                    message="Levi--Civita index uses raw d; use d_reg for a regulator-dimensional index.",
                    snippet=line,
                )

        if (
            metric_old_re.search(line)
            and metric_object_re.search(line)
            and not historical
        ):
            add_record(
                findings,
                category="mostly-minus-metric",
                path=path,
                line=index + 1,
                message="Metric signature has a positive time entry and negative spatial entries.",
                snippet=line,
            )
        if (spacelike_old_re.search(line) or timelike_old_re.search(line)) and not historical:
            add_record(
                findings,
                category="interval-sign",
                path=path,
                line=index + 1,
                message="Timelike/spacelike interval sign conflicts with the mostly-plus metric.",
                snippet=line,
            )
        if (old_norm_formula_re.search(line) or old_dot_formula_re.search(line)) and not historical:
            add_record(
                findings,
                category="interval-sign",
                path=path,
                line=index + 1,
                message="Lorentzian scalar product has a positive time and negative spatial form.",
                snippet=line,
            )

        if (shell_old_re.search(line) or contracted_shell_old_re.search(line)) and not historical:
            add_record(
                findings,
                category="old-mass-shell",
                path=path,
                line=index + 1,
                message="Lorentzian massive shell must use p^2=-m^2.",
                snippet=line,
            )

        if (
            (mass_difference_re.search(line) or propagator_denominator_re.search(line))
            and not historical
            and not euclidean_operator
        ):
            relevant = re.search(
                r"(?:propagator|Feynman|Green|Fourier|on[- ]?shell|mass[- ]?shell|"
                r"pole|resolvent|D_F|S_F|G_2|\\widetilde)",
                context,
                re.IGNORECASE,
            )
            prescription = re.search(r"(?:\\ii|\\mathrm\s*\{i\}|\bi\b)\s*(?:0|epsilon|varepsilon)", line, re.I)
            if relevant or prescription or propagator_denominator_re.search(line):
                add_record(
                    findings,
                    category="old-mass-propagator",
                    path=path,
                    line=index + 1,
                    message="Lorentzian propagator or pole uses p^2-m^2 instead of p^2+m^2.",
                    snippet=line,
                )

        if scalar_operator_old_re.search(line) and re.search(
            r"(?:scalar|D_F|Green|K\b|equation|\\phi)", context, re.I
        ) and not historical and not euclidean_operator:
            add_record(
                findings,
                category="scalar-equation-sign",
                path=path,
                line=index + 1,
                message="Scalar Lorentzian operator has the mostly-minus mass sign.",
                snippet=line,
            )
        if scalar_kinetic_old_re.search(line) and not historical:
            add_record(
                findings,
                category="scalar-lagrangian-sign",
                path=path,
                line=index + 1,
                message="Scalar kinetic term has a positive Lorentzian sign.",
                snippet=line,
            )
        if dirac_lagrangian_old_re.search(line) and not historical:
            add_record(
                findings,
                category="dirac-lagrangian-sign",
                path=path,
                line=index + 1,
                message="Dirac Lagrangian has the opposite sign/mass combination.",
                snippet=line,
            )
        if dirac_equation_old_re.search(line) and not historical:
            add_record(
                findings,
                category="dirac-equation-sign",
                path=path,
                line=index + 1,
                message="Dirac equation has the old mostly-minus mass sign.",
                snippet=line,
            )
        if proca_mass_old_re.search(line) and re.search(
            r"(?:Proca|massive\s+vector|vector|A_\w*\s*A)", context, re.I
        ) and not historical:
            add_record(
                findings,
                category="proca-mass-sign",
                path=path,
                line=index + 1,
                message="Proca mass term has the opposite mostly-plus sign.",
                snippet=line,
            )
        if (
            proca_polarization_old_re.search(line)
            or proca_polarization_fraction_old_re.search(line)
        ) and not historical:
            add_record(
                findings,
                category="proca-polarization-sign",
                path=path,
                line=index + 1,
                message="Massive-vector polarization sum has a negative pp/m^2 term.",
                snippet=line,
            )
        if clifford_old_re.search(line) and not historical:
            add_record(
                findings,
                category="clifford-sign",
                path=path,
                line=index + 1,
                message="Clifford anticommutator uses +2 eta instead of -2 eta.",
                snippet=line,
            )
        if expanded_clifford_old_re.search(line) and not historical:
            add_record(
                findings,
                category="clifford-sign",
                path=path,
                line=index + 1,
                message="Expanded Clifford anticommutator uses +2 eta instead of -2 eta.",
                snippet=line,
            )
        if trace_old_re.search(line) and not historical:
            add_record(
                findings,
                category="gamma-trace-sign",
                path=path,
                line=index + 1,
                message="Two-gamma trace has the old positive coefficient.",
                snippet=line,
            )
        if contraction_old_re.search(line) and not historical:
            add_record(
                findings,
                category="gamma-contraction-sign",
                path=path,
                line=index + 1,
                message="Gamma contraction has the old mostly-minus coefficient.",
                snippet=line,
            )
        if epsilon_orientation_old_re.search(line) and not historical:
            if not re.search(r"\bEuclidean\b|heat[- ]kernel|proper[- ]time", context, re.I):
                add_record(
                    findings,
                    category="epsilon-orientation",
                    path=path,
                    line=index + 1,
                    message="Lower epsilon orientation must be epsilon_{0123}=-1 for the mostly-plus metric.",
                    snippet=line,
                )
        if gamma5_orientation_old_re.search(line) and not historical:
            if not re.search(r"\bEuclidean\b|heat[- ]kernel|proper[- ]time", context, re.I):
                add_record(
                    findings,
                    category="gamma5-sign",
                    path=path,
                    line=index + 1,
                    message="The D=4 gamma_5 definition has the opposite orientation sign.",
                    snippet=line,
                )


def scan_dimensions_and_vectors(
    path: Path,
    lines: list[str],
    findings: list[dict[str, object]],
    candidates: list[dict[str, object]],
) -> None:
    """Check D/d_reg dimensions and bold spatial variables."""

    measure_re = re.compile(
        r"\\dd\s*\^\s*(?:\{\s*(?P<braced>D\s*-\s*1|d\s*-\s*1|3|4)\s*\}"
        r"|(?P<plain>D\s*-\s*1|d\s*-\s*1|3|4))"
        r"(?P<tail>[^\n]*)",
    )
    delta_re = re.compile(
        r"\\delta\s*\^\s*(?:\{\s*(?P<braced>D\s*-\s*1|d\s*-\s*1|3|4|D)\s*\}"
        r"|(?P<plain>D\s*-\s*1|d\s*-\s*1|3|4|D))"
        r"\s*(?P<tail>[^\n]*)",
    )
    raw_dimensional_measure_re = re.compile(
        r"\\dd\s*\^\s*(?:\{\s*d\s*\}|d)(?![_A-Za-z])",
    )
    raw_dimensional_delta_re = re.compile(
        r"\\delta\s*\^\s*(?:\{\s*d\s*\}|d)(?![_A-Za-z])",
    )
    dimreg_definition_re = re.compile(
        r"(?<![A-Za-z])d\s*=\s*(?:D\s*-\s*|4\s*-\s*)"
        r"(?:\\epsilon|epsilon|\\varepsilon|varepsilon|e)(?![A-Za-z])",
    )
    dimreg_power_re = re.compile(
        r"(?:\\mu|mu)\s*\^\s*\{?[^{}\n]*\b(?:d\s*-\s*4|4\s*-\s*d)\b[^{}\n]*\}?",
    )
    raw_dimensional_text_re = re.compile(
        r"(?<![A-Za-z_])d\s*[- ]dimensional(?![A-Za-z])|"
        r"(?<![A-Za-z_])d\s*[-+]\s*(?:1|2|4)\b|"
        r"(?<![A-Za-z_])d\s*/\s*2\b",
    )
    energy_re = re.compile(
        r"(?P<name>\\omega|omega|E)\s*_\s*(?:\{(?P<brace>[^{}\n]*)\}|(?P<plain>[A-Za-z]))",
    )

    for index, line in enumerate(lines):
        context = line_context(lines, index, radius=6)
        historical = historical_context(context)
        fixed = fixed_dimension_context(path, lines, index)

        for bare_measure in BARE_DIFFERENTIAL_MEASURE_RE.finditer(line):
            dimension = normalise_tex_label(bare_measure.group("dimension"))
            likely_measure = bool(
                figure_path(path)
                or re.search(r"\\int|integration|measure|volume", context, re.IGNORECASE)
            )
            if likely_measure and not historical:
                if dimension == "d":
                    category = "raw-dimensional-regularization"
                    message = "Differential measure uses raw d; use \\dd^{d_reg} in regulator-dimensional integration."
                else:
                    category = "noncanonical-differential-measure"
                    message = "Differential measure uses bare d^D; use the package \\dd^D notation."
                add_record(
                    findings,
                    category=category,
                    path=path,
                    line=index + 1,
                    message=message,
                    snippet=line,
                )

        if raw_dimensional_measure_re.search(line) or raw_dimensional_delta_re.search(line):
            add_record(
                findings,
                category="raw-dimensional-regularization",
                path=path,
                line=index + 1,
                message="Loop or delta dimension uses raw d; use d_reg for dimensional regularization.",
                snippet=line,
            )
        if dimreg_definition_re.search(line) and not historical:
            add_record(
                findings,
                category="dimreg-symbol",
                path=path,
                line=index + 1,
                message="Dimensional-regularization definition uses d instead of d_reg.",
                snippet=line,
            )
        if dimreg_power_re.search(line) and not historical:
            add_record(
                findings,
                category="dimreg-symbol",
                path=path,
                line=index + 1,
                message="Renormalization power uses raw d instead of d_reg.",
                snippet=line,
            )
        if raw_dimensional_text_re.search(line) and not historical:
            add_record(
                findings,
                category="raw-dimensional-regularization",
                path=path,
                line=index + 1,
                message="Dimension arithmetic uses raw d outside an explicit d_reg context.",
                snippet=line,
            )

        for match in measure_re.finditer(line):
            exponent = (match.group("braced") or match.group("plain") or "").replace(" ", "")
            tail = match.group("tail")
            if exponent.lower() == "d":
                continue
            if exponent == "d-1":
                add_record(
                    findings,
                    category="raw-dimensional-regularization",
                    path=path,
                    line=index + 1,
                    message="Spatial measure uses raw d-1; use D-1 or d_reg-1 as appropriate.",
                    snippet=line,
                )
            if exponent in {"D-1", "d-1", "3"}:
                # The first vector token after the exponent is the integration
                # variable.  TeX spacing commands can occur in between.
                vector_match = re.match(
                    r"(?:\s|\\[,;:! ]|\\!|\\;|\\,|\\:)*"
                    r"(?P<vector>\\(?:mathbf|boldsymbol)\s*(?:\{[^{}]*\}|[A-Za-z])|"
                    r"(?P<bare>[A-Za-z]))",
                    tail,
                )
                if vector_match and vector_match.group("bare"):
                    add_record(
                        findings,
                        category="unbold-spatial-vector",
                        path=path,
                        line=index + 1,
                        message="Spatial integration variable must be bold.",
                        snippet=line,
                    )
                if exponent == "3" and not fixed and not historical:
                    add_record(
                        findings,
                        category="fixed-dimension-formula",
                        path=path,
                        line=index + 1,
                        message="Numeric spatial measure lacks a local fixed-D=4 scope.",
                        snippet=line,
                    )
                elif exponent == "3" and fixed:
                    add_candidate(
                        candidates,
                        category="fixed-dimension-formula",
                        path=path,
                        line=index + 1,
                        reason="Numeric spatial measure is locally scoped to fixed physical D=4.",
                        snippet=line,
                    )
            elif exponent == "4" and not fixed and not historical:
                add_record(
                    findings,
                    category="fixed-dimension-formula",
                    path=path,
                    line=index + 1,
                    message="Numeric spacetime measure lacks a local fixed-D=4 scope.",
                    snippet=line,
                )
            elif exponent == "4" and fixed:
                add_candidate(
                    candidates,
                    category="fixed-dimension-formula",
                    path=path,
                    line=index + 1,
                    reason="Numeric spacetime measure is locally scoped to fixed physical D=4.",
                    snippet=line,
                )
        for match in delta_re.finditer(line):
            exponent = (match.group("braced") or match.group("plain") or "").replace(" ", "")
            tail = match.group("tail")
            if exponent == "d-1":
                add_record(
                    findings,
                    category="raw-dimensional-regularization",
                    path=path,
                    line=index + 1,
                    message="Spatial delta uses raw d-1; use D-1 or a declared d_reg context.",
                    snippet=line,
                )
            if exponent in {"3", "D-1"}:
                argument = delta_argument(tail)
                # A superscript on W, Gamma, or another functional is a
                # derivative order, not the dimension of a delta function.
                # A genuine delta function has its argument immediately
                # after optional TeX spacing (and an optional \left).
                if not re.match(
                    r"(?:\s|\\[,;:! ]|\\!|\\;|\\,|\\:)*"
                    r"(?:\\left\s*)?\(",
                    tail,
                ):
                    # For example, \delta^3 W is a third functional
                    # derivative, not a three-dimensional delta function.
                    continue
                protected = re.sub(
                    r"\\(?:mathbf|boldsymbol)\s*(?:\{([^{}]*)\}|([A-Za-z]))",
                    " PROTECTED ",
                    argument,
                )
                bare_vectors = re.findall(
                    r"(?<![A-Za-z\\])([pqkrlxyPQRKRLXY])(?![A-Za-z])",
                    protected,
                )
                if bare_vectors:
                    add_record(
                        findings,
                        category="unbold-spatial-vector",
                        path=path,
                        line=index + 1,
                        message="Spatial delta arguments must use bold vectors.",
                        snippet=line,
                    )
                if exponent == "3" and not fixed and not historical:
                    add_record(
                        findings,
                        category="fixed-dimension-formula",
                        path=path,
                        line=index + 1,
                        message="Numeric delta dimension lacks a local fixed-D=4 scope.",
                        snippet=line,
                    )
                elif exponent == "3" and fixed:
                    add_candidate(
                        candidates,
                        category="fixed-dimension-formula",
                        path=path,
                        line=index + 1,
                        reason="Numeric spatial delta is locally scoped to fixed physical D=4.",
                        snippet=line,
                    )
            elif exponent == "4" and not fixed and not historical:
                add_record(
                    findings,
                    category="fixed-dimension-formula",
                    path=path,
                    line=index + 1,
                    message="Numeric spacetime delta dimension lacks a local fixed-D=4 scope.",
                    snippet=line,
                )
            elif exponent == "4" and fixed:
                add_candidate(
                    candidates,
                    category="fixed-dimension-formula",
                    path=path,
                    line=index + 1,
                    reason="Numeric spacetime delta is locally scoped to fixed physical D=4.",
                    snippet=line,
                )

        for match in energy_re.finditer(line):
            subscript = match.group("brace") or match.group("plain") or ""
            protected = re.sub(
                r"\\(?:mathbf|boldsymbol)\s*(?:\{([^{}]*)\}|([A-Za-z]))",
                " PROTECTED ",
                subscript,
            )
            # E_k in a spectral sum and omega_L/R in helicity-labelled
            # amplitudes are labels, not spatial momenta.  Momentum energy
            # labels use p, q, k, r, x, or y (with uppercase variants).
            names = "pqklPQKL" if match.group("name") == "E" else "pqkrlxyPQKXY"
            if match.group("name") == "E":
                first_label = re.match(r"[A-Za-z]", subscript)
                if first_label and re.search(
                    rf"\\sum\s*_\s*(?:\{{[^{{}}]*\b{first_label.group(0)}\b[^{{}}]*\}}|"
                    rf"{first_label.group(0)})",
                    line,
                ):
                    continue
            if re.search(rf"(?<![A-Za-z\\])(?:[{names}])(?![A-Za-z])", protected):
                add_record(
                    findings,
                    category="unbold-spatial-vector",
                    path=path,
                    line=index + 1,
                    message="Energy label must carry a bold spatial momentum.",
                    snippet=line,
                )


def scan_mixed_indices(
    path: Path,
    lines: list[str],
    findings: list[dict[str, object]],
    candidates: list[dict[str, object]],
) -> None:
    """Find credible adjacent upper/lower tensor scripts without ``{}``."""

    for index, line in enumerate(lines):
        for match in MIXED_INDEX_RE.finditer(line):
            first_kind = match.group("first_kind")
            second_kind = match.group("second_kind")
            if first_kind == second_kind:
                continue
            base = match.group("base")
            upper = match.group("first_body") if first_kind == "^" else match.group("second_body")
            lower = match.group("second_body") if first_kind == "^" else match.group("first_body")
            raw_base, base_name = tensor_base(base)
            if base_name in {"delta", "Delta"}:
                add_candidate(
                    candidates,
                    category="compact-kronecker-index",
                    path=path,
                    line=index + 1,
                    reason="Compact mixed indices are explicitly permitted for Kronecker deltas.",
                    snippet=line,
                )
                continue
            if base_name == "D" and normalise_index_body(upper).lower() in {"j", "j1", "j2"}:
                if not has_spacetime_index(upper) and not has_spacetime_index(lower):
                    add_candidate(
                        candidates,
                        category="representation-label",
                        path=path,
                        line=index + 1,
                        reason="D^j_{kl} is a representation-matrix label, not a mixed tensor index.",
                        snippet=line,
                    )
                    continue
            if not is_credible_mixed_candidate(base, upper, lower):
                continue
            add_record(
                findings,
                category="adjacent-mixed-indices",
                path=path,
                line=index + 1,
                message="Adjacent upper/lower tensor indices require an empty TeX group.",
                snippet=line,
            )


def scan_content(
    path: Path,
    lines: list[str],
    findings: list[dict[str, object]],
    candidates: list[dict[str, object]],
) -> None:
    scan_metric_and_propagators(path, lines, findings, candidates)
    scan_dimensions_and_vectors(path, lines, findings, candidates)
    scan_mixed_indices(path, lines, findings, candidates)


def canonical_checks(
    sources: dict[Path, str],
    docs: dict[Path, list[str]],
    findings: list[dict[str, object]],
) -> None:
    """Require the adopted convention table to be present in the closure."""

    chunks = ["\n".join(source_lines(path, text)) for path, text in sources.items()]
    chunks.extend("\n".join(lines) for lines in docs.values())
    blob = "\n".join(chunks)
    requirements: tuple[tuple[str, str, str], ...] = (
        (
            "metric",
            r"diag\s*\(\s*-\s*,\s*\+",
            "The convention table must state eta=diag(-,+,...,+).",
        ),
        (
            "mass_shell",
            r"p\s*\^\s*\{?2\}?\s*=\s*-\s*m\s*\^\s*\{?2\}?",
            "The convention table must state p^2=-m^2.",
        ),
        (
            "clifford",
            r"(?:\{|\[)\s*\\gamma[^\n]*(?:\}|\]_\+)\s*=\s*-\s*2\s*\\eta",
            "The convention table must state the -2 eta Clifford algebra.",
        ),
        (
            "slash",
            r"\\slashed\s*p\s*=\s*\\gamma\s*\^\s*\\mu\s*p\s*_\s*\\?mu",
            "The convention table must define slash(p)=gamma^mu p_mu.",
        ),
        (
            "gamma5",
            r"\\gamma\s*_\s*\{?5\}?\s*(?:=|\\equiv)\s*"
            r"(?:\\ii|\\mathrm\s*\{\s*i\s*\}|i)\s*"
            r"\\gamma\s*\^\s*\{?0\}?.{0,24}"
            r"\\gamma\s*\^\s*\{?1\}?.{0,24}"
            r"\\gamma\s*\^\s*\{?2\}?.{0,24}"
            r"\\gamma\s*\^\s*\{?3\}?",
            "The convention table must state the D=4 gamma_5 orientation.",
        ),
        (
            "epsilon_orientation",
            r"\\epsilon\s*\^\s*\{?\s*0\s*1\s*2\s*3\s*\}?\s*=\s*\+\s*1",
            "The convention table must state epsilon^{0123}=+1.",
        ),
        (
            "d_reg",
            r"d[_\s{]*(?:\\mathrm\s*\{\s*reg\s*\}|reg)",
            "The convention table must distinguish d_reg from physical D.",
        ),
        (
            "positive_phase",
            r"(?:\\ee|\\mathrm\s*e|\\text\s*\{?e\}?)[^\n]{0,40}"
            r"(?:\\ii|\\mathrm\s*\{\s*i\s*\})[^\n]{0,40}p[^\n]*x",
            "The convention table must state the positive-frequency phase.",
        ),
        (
            "scalar_propagator",
            r"-\s*(?:\\ii|\\mathrm\s*\{\s*i\s*\})[^\n]{0,40}"
            r"p\s*\^\s*\{?2\}?\s*\+\s*m\s*\^\s*\{?2\}?[^\n]*"
            r"-\s*(?:\\ii|\\mathrm\s*\{\s*i\s*\})",
            "The convention table must state the mostly-plus scalar propagator.",
        ),
        (
            "mixed_spacing",
            r"T\s*\^\s*\\?mu\s*\{\}\s*_\s*\\?nu",
            "The convention table must show empty-group spacing for mixed indices.",
        ),
    )
    for category, pattern, message in requirements:
        if re.search(pattern, blob, re.IGNORECASE | re.DOTALL):
            continue
        add_record(
            findings,
            category="missing-canonical-convention",
            path=ROOT / "NOTATION.md",
            line=1,
            message=message,
            snippet=category,
        )


def conventions_table() -> dict[str, str]:
    return {
        "metric": "eta_{mu nu}=diag(-,+,...,+)",
        "physical_spacetime_dimension": "D",
        "spatial_dimension": "D-1",
        "dimensional_regularization_dimension": "d_reg=D-epsilon_UV",
        "positive_frequency_phase": "exp(+i p dot x)",
        "scalar_mass_shell": "p^2=-m^2",
        "scalar_lagrangian": "L_0=-1/2 (partial phi)^2-1/2 m^2 phi^2",
        "scalar_propagator": "-i/(p^2+m^2-i0)",
        "proca_polarization_sum": "eta^{mu nu}+p^mu p^nu/m^2",
        "proca_mass_term": "-m^2 A_mu A^mu/2",
        "proca_propagator": "-i(eta_{mu nu}+p_mu p_nu/m^2)/(p^2+m^2-i0)",
        "clifford_algebra": "{gamma^mu,gamma^nu}=-2 eta^{mu nu}",
        "slash_definition": "slash(p)=gamma^mu p_mu",
        "gamma5_definition": "gamma_5=i gamma^0 gamma^1 gamma^2 gamma^3 in D=4",
        "epsilon_orientation": "epsilon^{01...D-1}=+1; epsilon_{0123}=-1 in D=4",
        "dirac_lagrangian": "-bar(psi)(i slash(partial)+m) psi",
        "dirac_equation": "(i slash(partial)+m) psi=0",
        "mixed_index_spacing": "empty TeX group between adjacent lower and upper tensor indices",
    }


def sorted_unique(records: Iterable[dict[str, object]]) -> list[dict[str, object]]:
    seen: set[tuple[object, ...]] = set()
    result: list[dict[str, object]] = []
    for item in sorted(
        records,
        key=lambda row: (
            str(row.get("file", "")),
            int(row.get("line", 0)),
            str(row.get("category", "")),
            str(row.get("message", "")),
            str(row.get("snippet", "")),
        ),
    ):
        key = tuple(item.get(field) for field in ("category", "file", "line", "message", "snippet"))
        if key in seen:
            continue
        seen.add(key)
        result.append(item)
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--edition", choices=("base", "implicit"), required=True)
    parser.add_argument("--strict", action="store_true")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    findings: list[dict[str, object]] = []
    candidates: list[dict[str, object]] = []
    sources, missing = edition_sources(args.edition)
    for path in missing:
        add_record(
            findings,
            category="missing-native-input",
            path=path,
            line=1,
            message="Edition source closure contains a missing input.",
            snippet=str(path),
        )

    for path, text in sources.items():
        scan_content(path, source_lines(path, text), findings, candidates)
    docs = package_doc_inputs()
    for path, lines in docs.items():
        scan_content(path, lines, findings, candidates)
    canonical_checks(sources, docs, findings)

    final_findings = sorted_unique(findings)
    final_candidates = sorted_unique(candidates)
    result = {
        "schema_version": 1,
        "edition": args.edition,
        "status": "pass" if not final_findings else "fail",
        "native_snapshot_sha256": native_snapshot_sha256(args.edition),
        "findings_count": len(final_findings),
        "reviewed_candidates_count": len(final_candidates),
        "conventions": conventions_table(),
        "findings": final_findings,
        "reviewed_candidates": final_candidates,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    for finding in final_findings:
        print(
            f"FAIL: {finding['file']}:{finding['line']} "
            f"[{finding['category']}] {finding['message']}",
            file=sys.stderr,
        )
    if final_findings and args.strict:
        print(f"convention audit failed: {len(final_findings)} finding(s)", file=sys.stderr)
        return 1
    print(
        f"convention audit {result['status']}: edition={args.edition}; "
        f"findings={len(final_findings)}; reviewed_candidates={len(final_candidates)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
