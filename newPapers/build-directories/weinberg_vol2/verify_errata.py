#!/usr/bin/env python3
"""Regression checks for corrected Volume II source and exercise copies."""

from pathlib import Path


ROOT = Path(__file__).resolve().parent
EXERCISE = ROOT.parent / "weinberg_vol2_exercises"

CHECKS = (
    ("chapter15/sec157.tex", "Greens functions", "Green's functions"),
    ("chapter16/sec161.tex", "vacuum vacuum amplitude", "vacuum amplitude"),
    ("chapter16/sec161.tex", r"\Phi^r(x)\ket{\Omega}_{\mathrm{in},J=0}", r"\Phi^r(y)\ket{\Omega}_{\mathrm{in},J=0}"),
    ("chapter16/sec162.tex", r"p^2+\mu(\phi_0)", r"p^2+\mu^2(\phi_0)"),
    ("chapter16/sec163.tex", "nonpositive second derivative", "nonnegative second derivative"),
    ("chapter17/sec173.tex", r"F(t)=gtF_1", r"F(t)=\hbar tF_1"),
    ("chapter18/sec185.tex", r"T-T_0", r"T-T_c"),
    ("chapter18/sec185.tex", r"O\bigl(g_4(\mu)\bigr)", r"O\bigl(g_4^2(\mu)\bigr)"),
    ("chapter18/sec185.tex", "powers of 1", r"powers of $\epsilon$"),
    ("chapter18/sec187.tex", "it for the first time opened", "for the first time it opened"),
    ("chapter19/sec194.tex", "This symmetry if exact", "This symmetry, if exact"),
    ("chapter19/sec196.tex", r"\sum_a\mathcal D_{ab}(h)\xi_b", r"\sum_b\mathcal D_{ab}(h)\xi_b"),
    ("chapter19/sec196.tex", r"h\bigl(\xi(x)\bigr)", r"h\bigl(\xi(x),g\bigr)"),
    ("chapter19/sec196.tex", "a linear combinations", "a linear combination"),
    ("chapter19/sec198.tex", r"0\geq s\geq1", r"0\leq s\leq1"),
    ("chapter19/backmatter.tex", "hep-ph/-9602366", "hep-ph/9602366"),
    ("chapter20/sec206.tex", "yielding a electron", "yielding an electron"),
    ("chapter20/backmatter.tex", "B126}, 298 (1972)", "B126}, 298 (1977)"),
    ("chapter21/sec213.tex", "an hadronic current", "a hadronic current"),
    ("chapter21/sec214.tex", r"\hyperref[sec:19.5]{Section 19.5}, in this case", r"\hyperref[sec:19.6]{Section 19.6}, in this case"),
    ("chapter21/sec215.tex", "couplings is measured", "couplings are measured"),
    ("chapter21/sec215.tex", "As emphasized in Chapter 19", "As emphasized in Chapter 18"),
    ("chapter21/appendix.tex", r"\sum_i\phi_ax_a", r"\sum_a\phi_ax_a"),
    ("chapter22/sec222.tex", r"\hyperref[eq:22.2.1]{Eq.~(22.2.1)}", r"\hyperref[eq:22.1.1]{Eq.~(22.1.1)}"),
    ("chapter22/sec222.tex", "(22.12.13)", "(22.2.13)"),
    ("chapter22/sec222.tex", "orthornormal", "orthonormal"),
    ("chapter22/sec222.tex", "Eq.~(2.2.44)", "Eq.~(22.2.44)"),
    ("chapter22/sec222.tex", r"\varphi_u^\dagger(x)\varphi_v(x)", r"\varphi_v^\dagger(x)\varphi_v(x)"),
    ("chapter22/sec227.tex", r"\int_0^t dt", r"\int_0^1 dt"),
    ("chapter22/sec227.tex", "form.We", "form. We"),
    ("chapter22/sec227.tex", "zerofor", "zero for"),
    ("chapter22/sec227.tex", "0$and", "0$ and"),
    ("chapter22/sec227.tex", r"z^\mu$of", r"z^\mu$ of"),
    ("chapter22/sec227.tex", "haveshown", "have shown"),
    ("chapter23/introduction.tex", "such as as magnetic", "such as magnetic"),
    ("chapter23/sec232.tex", "the the homotopy", "the homotopy"),
)


def read(edition: Path, relative: str) -> str:
    source = (edition / "latex" / "chapters" / relative).read_text(encoding="utf-8")
    return "\n".join(
        line for line in source.splitlines() if not line.lstrip().startswith("%")
    )


failures: list[str] = []
for relative, bad, good in CHECKS:
    for edition in (ROOT, EXERCISE):
        text = read(edition, relative)
        if bad in text:
            failures.append(f"stale text in {edition.name}/{relative}: {bad}")
        if good not in text:
            failures.append(f"missing correction in {edition.name}/{relative}: {good}")

prompt = (
    EXERCISE / "latex/exercises/chapter20/weinberg-exercises.tex"
).read_text(encoding="utf-8")
for required in (r"\sum_N\delta^4(p-p_N)", r"\ket{N}"):
    if required not in prompt:
        failures.append(f"missing Chapter 20 exercise correction: {required}")

exercise_175 = read(EXERCISE, "chapter17/sec175.tex")
corrupt = r"\cdot\mathcal M_0^A(q)^{-1}\mathcal M_2^A(q)"
restored = r"-\mathcal M_0^A(q)^{-1}\mathcal M_2^A(q)"
if corrupt in exercise_175 or restored not in exercise_175:
    failures.append("Chapter 17.5 exercise determinant expansion is not restored")

if failures:
    raise SystemExit("\n".join(failures))

print(f"Volume II errata regression checks passed ({len(CHECKS) * 2 + 3} assertions).")
