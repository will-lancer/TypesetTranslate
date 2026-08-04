#!/usr/bin/env python3
"""Reject definite regressions to the source-era GR notation."""

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
    chapters: frozenset[int] | None = None
    fatal: bool = True


RULES = (
    Rule(
        "old-signature",
        re.compile(
            r"\(\s*(?:\+?1|\+)\s*,\s*(?:\+?1|\+)\s*,"
            r"\s*(?:\+?1|\+)\s*,\s*(?:-1|-)\s*\)"
        ),
        "convert (+,+,+,-) to (-,+,+,+)",
    ),
    Rule(
        "old-four-velocity-normalization",
        re.compile(
            r"(?:"
            r"u\s*\^\s*\{?\\mu\}?\s*u\s*_\s*\{?\\mu\}?"
            r"|"
            r"u\s*_\s*\{?\\mu\}?\s*u\s*\^\s*\{?\\mu\}?"
            r")\s*=\s*\+?\s*1(?![\d.])"
        ),
        "timelike four-velocities obey u^mu u_mu = -1 in the target signature",
    ),
    Rule(
        "time-last-order",
        re.compile(r"\(\s*1\s*,\s*2\s*,\s*3\s*,\s*0\s*\)"),
        "use the coordinate order (0,1,2,3)",
    ),
    Rule(
        "comma-semicolon-derivative",
        re.compile(
            r"_\{?\s*[,;]\s*\\(?:mu|nu|rho|sigma|alpha|beta|gamma|"
            r"lambda|kappa|tau)\b"
        ),
        "use explicit partial or covariant derivatives",
    ),
    Rule(
        "lorentz-gauge-misnomer",
        re.compile(r"\bLorentz (?:gauge|condition)\b"),
        "use Lorenz gauge/condition; reserve Lorentz for the spacetime group",
    ),
    Rule(
        "squared-box-symbol",
        re.compile(r"\\(?:Box|square)\s*\^\s*\{?2\}?"),
        "use \\Box for the d'Alembertian unless an actual iterated operator is intended",
    ),
    Rule(
        "legacy-tex-rm",
        re.compile(r"\\rm\b"),
        "use scoped \\mathrm{...} rather than the legacy \\rm font switch",
    ),
    Rule(
        "cosmological-R-of-t",
        re.compile(r"\bR\s*\(\s*t\s*\)"),
        "use a(t) for the cosmological scale factor",
        chapters=frozenset({14, 15, 16}),
    ),
    Rule(
        "cosmological-R-derivatives",
        re.compile(
            r"(?:\\(?:dot|ddot)\s*\{\s*R\s*\}"
            r"|\\(?:dot|ddot)\s+R\b"
            r"|\bR\s*_\s*\{?\s*0\s*\}?)"
        ),
        "use a, dot a, ddot a, and a_0 for the cosmological scale factor",
        chapters=frozenset({14, 15, 16}),
    ),
    Rule(
        "radiation-constant-a",
        re.compile(
            r"(?:"
            r"(?<![A-Za-z\\])a\s*(?:\\[,;!]|~|\s)*"
            r"T(?:_\{?(?:\\gamma[A-Za-z0-9]*|[A-Za-z0-9]+)\}?)?"
            r"\s*\^\s*\{?[34]\}?"
            r"|(?<![A-Za-z0-9_\\])a\s*\\equiv"
            r")"
        ),
        "use a_{\\mathrm{rad}} for the radiation constant beside scale factor a(t)",
        chapters=frozenset({15, 16}),
    ),
    Rule(
        "radiation-constant-legacy-rm",
        re.compile(r"a_\{\s*\\rm\s+rad\s*\}"),
        "write the binding radiation-constant symbol as a_{\\mathrm{rad}}",
        chapters=frozenset({15, 16}),
    ),
    Rule(
        "deacceleration-spelling",
        re.compile(r"\b[Dd]eacceleration\b"),
        "use the standard term deceleration",
    ),
    Rule(
        "cosmic-scale-index-R",
        re.compile(
            r"Cosmic\s+scale\s+factor[^\n]{0,32}"
            r"(?:\\\(\s*R\s*\\\)|\(\s*R\s*\))"
        ),
        "write the modernized index heading with scale factor a",
    ),
    Rule(
        "chapter16-brans-dicke-phi",
        re.compile(r"\\phi\b"),
        "use \\Phi_{\\mathrm{BD}} for the Brans--Dicke scalar",
        chapters=frozenset({16}),
    ),
    Rule(
        "chapter16-lowercase-lambda",
        re.compile(r"\\lambda\b"),
        "verify that a lowercase lambda is a genuine dummy variable; "
        "the cosmological constant is \\Lambda",
        chapters=frozenset({16}),
        fatal=False,
    ),
    Rule(
        "long-coordinate-derivative",
        re.compile(
            r"\\(?:d?frac)\s*\{\s*\\partial\s*\}\s*"
            r"\{\s*\\partial\s+x(?:\^|_)"
        ),
        "prefer compact indexed derivatives in long calculations",
        fatal=False,
    ),
    Rule(
        "ambiguous-indexed-epsilon",
        re.compile(
            r"(?<!\\tilde)\\epsilon\s*(?:\^|_)\s*\{?"
            r"(?:\\(?:mu|nu|rho|sigma|alpha|beta|gamma|delta|"
            r"lambda|kappa)|[ijk0123])"
        ),
        "use \\tilde\\epsilon for the permutation symbol/density or "
        "\\varepsilon for the Levi-Civita tensor",
        fatal=False,
    ),
)


def chapter_number(path: Path) -> int | None:
    match = re.search(r"chapter0?(\d{1,2})", str(path))
    return int(match.group(1)) if match else None


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--strict",
        action="store_true",
        help="make exercise-edition notation regressions release-blocking",
    )
    args = parser.parse_args()
    scopes = (
        LATEX / "chapters",
        LATEX / "backmatter",
        LATEX / "figures",
        LATEX / "exercises",
    )
    files = sorted(
        path
        for scope in scopes
        if scope.exists()
        for path in scope.rglob("*.tex")
    )
    failures: list[str] = []
    reviews: list[str] = []

    for path in files:
        lines = path.read_text(encoding="utf-8").splitlines()
        chapter = chapter_number(path)
        for line_number, line in enumerate(lines, start=1):
            # An exception comment normally precedes the display as a whole,
            # so retain enough nearby context to span \[...\] or an equation
            # opening plus a short explanatory continuation.
            context = "\n".join(lines[max(0, line_number - 9) : line_number])
            excepted = "NOTATION EXCEPTION" in context
            for rule in RULES:
                if rule.chapters is not None and chapter not in rule.chapters:
                    continue
                if not rule.pattern.search(line):
                    continue
                finding = (
                    f"{path.relative_to(ROOT)}:{line_number}: {rule.name}: "
                    f"{rule.explanation}"
                )
                is_provisional_exercise = (
                    not args.strict and (LATEX / "exercises") in path.parents
                )
                if rule.fatal and not excepted and not is_provisional_exercise:
                    failures.append(finding)
                elif not excepted:
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

    print("No definite source-era notation regressions found.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
