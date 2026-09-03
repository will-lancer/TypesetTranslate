#!/usr/bin/env python3
"""Reject definite regressions from the binding Wald notation policy."""

from __future__ import annotations

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


RULES = (
    Rule(
        "script-alphabet",
        re.compile(r"\\mathscr\b"),
        "use \\mathcal globally",
    ),
    Rule(
        "arrow-vector",
        re.compile(r"\\vec\b"),
        "use \\mathbf for Latin vectors or \\boldsymbol for Greek symbols",
    ),
    Rule(
        "pound-lie-derivative",
        re.compile(r"(?:\\pounds\b|£)"),
        "use \\mathcal L for Lie derivatives",
    ),
    Rule(
        "wald-tangent-space",
        re.compile(r"V\s*_\s*\{?\s*[A-Za-z]"),
        "use T_pM for tangent spaces",
    ),
    Rule(
        "wald-form-fiber",
        re.compile(r"\\Lambda\s*_\s*\{?\s*[A-Za-z]\s*\}?\s*\^"),
        "use \\Lambda^p T_x^\\vee M for p-forms at x",
    ),
    Rule(
        "star-cotangent-space",
        re.compile(
            r"T(?:\s*_\s*(?:\{[^}\n]+\}|[A-Za-z]))?\s*\^\s*"
            r"(?:\*|\{[^}\n]*\*[^}\n]*\})"
        ),
        "use a superscript \\vee for cotangent and algebraic dual spaces",
    ),
    Rule(
        "star-common-dual-space",
        re.compile(
            r"(?:\b[VW]|\\mathcal\s*\{?[HT]\}?|\\mathcal\s+T(?:_x)?)"
            r"\s*\^\s*(?:\*|\{[^}\n]*\*[^}\n]*\})"
        ),
        "use a superscript \\vee for algebraic dual spaces",
    ),
    Rule(
        "old-tangent-basis",
        re.compile(r"\{\s*v\s*_\s*\{?\s*\\mu\s*\}?\s*\}"),
        "use {e_\\mu} for a tangent-space basis",
    ),
    Rule(
        "old-dual-basis",
        re.compile(r"(?:v|Y)\s*\^\s*\{[^}\n]*\\mu[^}\n]*\*[^}\n]*\}"),
        "use {f^\\mu} for the dual cotangent-space basis",
    ),
    Rule(
        "dual-vector-term",
        re.compile(r"\bdual vector(?:s)?\b", re.IGNORECASE),
        "use covector or one-form",
    ),
    Rule(
        "lorentz-gauge",
        re.compile(r"\bLorentz (?:gauge|condition)\b"),
        "use Lorenz for electromagnetism and de Donder/harmonic for gravity",
    ),
    Rule(
        "metric-perturbation-gamma",
        re.compile(r"(?:\\bar\s*\{?\s*)?\\gamma\s*_\s*\{?\s*ab\b"),
        "use h_ab or barred h_ab for metric perturbations",
    ),
    Rule(
        "set-image-brackets",
        re.compile(r"(?<![A-Za-z-])[A-Za-z](?![A-Za-z-])\s*\[[A-Z]\]"),
        "write the image of a set as f(A)",
    ),
    Rule(
        "ambiguous-subset",
        re.compile(r"\\subset(?!eq|neq)\b"),
        "use subseteq or subsetneq according to meaning",
        fatal=False,
    ),
    Rule(
        "dotted-set-boundary",
        re.compile(r"\\dot\s*\{?\s*[A-Z]\s*\}?"),
        "verify that a dotted capital is a derivative, not a set boundary",
        fatal=False,
    ),
    Rule(
        "smooth-function-symbol",
        re.compile(r"\\mathcal\s*\{?F\}?[^\n]{0,80}smooth function", re.IGNORECASE),
        "use C^\\infty(M) for smooth functions",
        fatal=False,
    ),
)


def main() -> int:
    files = sorted(LATEX.rglob("*.tex")) if LATEX.exists() else []
    failures: list[str] = []
    reviews: list[str] = []

    for path in files:
        for line_number, line in enumerate(
            path.read_text(encoding="utf-8").splitlines(), start=1
        ):
            # Project metadata and editorial comments document source spellings
            # and modernization decisions; they are not typeset notation.
            if line.lstrip().startswith("%"):
                continue
            for rule in RULES:
                if not rule.pattern.search(line):
                    continue
                finding = (
                    f"{path.relative_to(ROOT)}:{line_number}: {rule.name}: "
                    f"{rule.explanation}"
                )
                (failures if rule.fatal else reviews).append(finding)

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
        return 1

    print("No definite notation regressions found.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
