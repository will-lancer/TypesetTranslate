#!/usr/bin/env python3
"""Regression audit for translation-sensitive equations.

The general source audit protects structure and references.  This companion
gate protects the algebraic hotspots found during independent equation-level
review, where a syntactically valid edit can still lose a sign, factor,
index position, or conjugate block.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent
CHAPTERS = ROOT / "latex" / "chapters"


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


def compact(text: str) -> str:
    uncommented = re.sub(r"(?<!\\)%.*", "", text)
    return re.sub(r"\s+", "", uncommented).replace("&", "")


def tagged_equation(relative: str, tag: str) -> str:
    text = read(relative)
    marker = rf"\tag{{{tag}}}"
    marker_index = text.find(marker)
    if marker_index < 0:
        raise AssertionError(f"{relative}: missing tag {tag}")

    begin_markers = (
        r"\begin{equation}",
        r"\begin{align}",
        r"\begin{multline}",
    )
    starts = [text.rfind(begin, 0, marker_index) for begin in begin_markers]
    start = max(starts)
    if start < 0:
        raise AssertionError(f"{relative}: cannot locate start of {tag}")

    end_match = re.search(
        r"\\end\{(?:equation|align|multline)\}",
        text[marker_index:],
    )
    if end_match is None:
        raise AssertionError(f"{relative}: cannot locate end of {tag}")
    end = marker_index + end_match.end()
    return compact(text[start:end])


def require_contains(
    name: str,
    actual: str,
    expected: str,
) -> None:
    if expected not in actual:
        print(f"FAIL: {name}")
        print("missing:", expected)
        raise AssertionError(name)
    print(f"OK: {name}")


def require_absent(
    name: str,
    actual: str,
    forbidden: str,
) -> None:
    if forbidden in actual:
        print(f"FAIL: {name}")
        print("unexpected:", forbidden)
        raise AssertionError(name)
    print(f"OK: {name}")


def main() -> int:
    chapter24_appendix = compact(
        read("latex/chapters/chapter24/appendixA.tex")
    )
    require_contains(
        "Chapter 24 supersymmetry-algebra cross-reference",
        chapter24_appendix,
        "Sections25.2and32.1",
    )
    require_absent(
        "no stale Chapter 24 supersymmetry-algebra cross-reference",
        chapter24_appendix,
        "Sections25.1and31.1",
    )

    chapter24 = tagged_equation(
        "latex/chapters/chapter24/sec242.tex",
        "24.2.8",
    )
    require_contains(
        "published Wess-Zumino chiral combination",
        chapter24,
        r"\partial_\mu(A+iB)",
    )

    projection = tagged_equation(
        "latex/chapters/chapter26/sec263.tex",
        "26.3.31",
    )
    require_contains(
        "two-component F-to-D projection sign",
        projection,
        r"=-2\intd^4x\,[h]_D",
    )

    grassmann_derivatives = tagged_equation(
        "latex/chapters/chapter26/sec262.tex",
        "26.2.9",
    )
    require_contains(
        "barred left derivative of bar theta squared",
        grassmann_derivatives,
        r"\bar\partial_{\dot\alpha}(\bar\theta\bar\theta)"
        r"=-2\bar\theta_{\dot\alpha}",
    )

    commuting_generator = tagged_equation(
        "latex/chapters/chapter26/sec262.tex",
        "26.2.37",
    )
    require_contains(
        "Hermitian commuting-spinor generator contraction",
        commuting_generator,
        r"u^\alphaQ_\alpha-\baru_{\dot\alpha}\barQ^{\dot\alpha}",
    )
    chapter262 = compact(read("latex/chapters/chapter26/sec262.tex"))
    require_contains(
        "commuting-spinor generator square",
        chapter262,
        r"Q^2(u)=-2(u\sigma^\mu\baru)P_\mu",
    )

    potential_conjugate = tagged_equation(
        "latex/chapters/chapter26/sec266.tex",
        "26.6.11",
    )
    require_contains(
        "potential-superfield squared-derivative conjugation",
        potential_conjugate,
        r"\Phi_n^*=D^2S_n^*",
    )
    for tag in ("26.6.15", "26.6.16"):
        equation = tagged_equation(
            "latex/chapters/chapter26/sec266.tex",
            tag,
        )
        require_contains(
            f"canonical chiral equation coefficient {tag}",
            equation,
            r"=4",
        )

    appendix_conjugation = tagged_equation(
        "latex/chapters/chapter26/appendix.tex",
        "26.A.21",
    )
    require_contains(
        "Appendix 26.A ordered squared-derivative rule",
        appendix_conjugation,
        r"\left(\barD_{\dot\alpha}\barD^{\dot\alpha}S\right)^*"
        r"=D^\alphaD_\alphaS^*",
    )
    chapter26_appendix = compact(
        read("latex/chapters/chapter26/appendix.tex")
    )
    require_contains(
        "Appendix 26.A distinct Lorentz indices",
        chapter26_appendix,
        r"\sigma^{\mu\nu}",
    )
    require_absent(
        "no repeated Lorentz index in Appendix 26.A tensor",
        chapter26_appendix,
        r"\sigma^{\mu\mu}",
    )

    chapter266 = compact(
        read("latex/chapters/chapter26/sec266.tex")
    )
    require_contains(
        "superspace variation factor and spacetime measure",
        chapter266,
        r"=-\frac14\sum_n\intd^4x\intd^2\theta\,d^2\bar\theta\,"
        r"\deltaS_n\barD^2",
    )

    current_algebra = tagged_equation(
        "latex/chapters/chapter26/sec267.tex",
        "26.7.45",
    )
    for block in (
        r"\{S_{\mathrm{new}\,\alpha}^\mu,\barQ_{\dot\alpha}\}",
        r"\{\barS_{\mathrm{new}\,\dot\alpha}^\mu,Q_\alpha\}",
        r"\{S_{\mathrm{new}\,\alpha}^\mu,Q_\beta\}",
        r"\{\barS_{\mathrm{new}\,\dot\alpha}^\mu,"
        r"\barQ_{\dot\beta}\}",
    ):
        require_contains(
            f"complete current-algebra block {block}",
            current_algebra,
            block,
        )

    chapter272 = compact(
        read("latex/chapters/chapter27/sec272.tex")
    )
    require_contains(
        "raised Grassmann dyad sign",
        chapter272,
        r"\theta^\alpha\theta^\beta"
        r"=-\frac12\epsilon^{\alpha\beta}\theta^2",
    )
    require_contains(
        "gauge-superderivative commutator sign",
        chapter272,
        r"[\barD^2,D_\alpha]"
        r"=-4i\sigma^\mu_{\alpha\dot\alpha}"
        r"\partial_\mu\barD^{\dot\alpha}",
    )

    nonabelian_strength = tagged_equation(
        "latex/chapters/chapter27/sec273.tex",
        "27.3.12",
    )
    require_contains(
        "non-Abelian field-strength normalization",
        nonabelian_strength,
        r"\equiv{}\frac{i}{4}\barD^2",
    )

    gauge_kinetic_components = tagged_equation(
        "latex/chapters/chapter27/sec274.tex",
        "27.4.42",
    )
    require_contains(
        "gauge-kinetic lambda-lambda-scalar block",
        gauge_kinetic_components,
        r"\left(\lambda_B\sigma^\mu\bar\sigma^\nu\psi_n\right)"
        r"f_{A\mu\nu}",
    )

    chapter274 = compact(
        read("latex/chapters/chapter27/sec274.tex")
    )
    require_contains(
        "post-27.4.19 mass-matrix input carries free B index",
        chapter274,
        r"M_0^2\begin{bmatrix}t_B\phi_0\\"
        r"\mathord{\pm}(t_B\phi_0)^*\end{bmatrix}=\sum_A",
    )
    require_contains(
        "post-27.4.19 mass-matrix output carries summed A index",
        chapter274,
        r"\left(\phi_0^\dagger[t_At_B\mathord{\pm}t_Bt_A]\phi_0\right)"
        r"\begin{bmatrix}t_A\phi_0\\"
        r"\mathord{\pm}(t_A\phi_0)^*\end{bmatrix}",
    )

    external_superfields = tagged_equation(
        "latex/chapters/chapter27/sec276.tex",
        "27.6.4",
    )
    require_contains(
        "external-superfield canonical D-term normalization",
        external_superfields,
        r"=\left[\Phi^\daggere^{-V}\Phi\right]_D",
    )

    extended_beta = tagged_equation(
        "latex/chapters/chapter27/sec279.tex",
        "27.9.50",
    )
    require_contains(
        "N=2 beta-function coupling power",
        extended_beta,
        r"\beta(g)=-\frac{g^3}{8\pi^2}",
    )

    gauge_chapters = compact(
        "\n".join(
            path.read_text(encoding="utf-8")
            for chapter in ("chapter27", "chapter28")
            for path in sorted((CHAPTERS / chapter).rglob("*.tex"))
        )
    )
    require_absent(
        "legacy projected field-strength suffix",
        gauge_chapters,
        r"W_{A\alphaL}",
    )
    require_absent(
        "legacy lower-epsilon field-strength contraction",
        gauge_chapters,
        r"\epsilon_{\alpha\beta}W_\alphaW_\beta",
    )

    chapter292 = compact(
        read("latex/chapters/chapter29/sec292.tex")
    )
    require_contains(
        "goldstino spectral trace overall sign and block sum",
        chapter292,
        r"4\rho_{\mathrm{VAC}}"
        r"=-\frac{\lvertF\rvert^2}{2p^0}"
        r"\operatorname{tr}_2\left("
        r"\sigma^0p_\mu\bar\sigma^\mu"
        r"+\bar\sigma^0p_\mu\sigma^\mu\right)",
    )

    chapter293 = compact(
        read("latex/chapters/chapter29/sec293.tex")
    )
    require_contains(
        "Chapter 29 field-strength spinor contraction",
        chapter293,
        r"\sum_{AB}W_A^\alphaW_{B\alpha}",
    )

    higgs_bound = tagged_equation(
        "latex/chapters/chapter28/sec285.tex",
        "28.5.43",
    )
    require_contains(
        "dimensionally consistent light-Higgs bound",
        higgs_bound,
        r"m_h^2\leqm_h^2(m_A\longrightarrow\infty)",
    )

    higgs_soft_mass = tagged_equation(
        "latex/chapters/chapter28/sec286.tex",
        "28.6.23",
    )
    require_contains(
        "gauge-mediated Higgs soft-mass normalization",
        higgs_soft_mass,
        r"=2\sum_nM_{sn}^2",
    )
    require_absent(
        "no spurious square of gauge-mediated loop bracket",
        higgs_soft_mass,
        r"\right]^2",
    )

    action_d_term = tagged_equation(
        "latex/chapters/chapter30/sec301.tex",
        "30.1.8",
    )
    require_contains(
        "potential-superfield D-term interaction factor",
        action_d_term,
        r"-4\operatorname{Re}",
    )
    action_integral = tagged_equation(
        "latex/chapters/chapter30/sec301.tex",
        "30.1.9",
    )
    require_contains(
        "potential-superfield superspace interaction factor",
        action_integral,
        r"+2\operatorname{Re}",
    )

    chapter30 = compact(
        "\n".join(
            path.read_text(encoding="utf-8")
            for path in sorted(
                (CHAPTERS / "chapter30").rglob("*.tex")
            )
        )
    )
    for daggered in (
        r"S^\dagger",
        r"S_n^\dagger",
        r"\Phi^\dagger",
        r"\Phi_n^\dagger",
    ):
        require_absent(
            f"minimal Chapter 30 conjugate notation {daggered}",
            chapter30,
            daggered,
        )

    gravitino_numerator = tagged_equation(
        "latex/chapters/chapter31/sec313.tex",
        "31.3.7",
    )
    require_contains(
        "gravitino same-chirality leading sign",
        gravitino_numerator,
        r"={}+m_g\left(",
    )
    require_contains(
        "gravitino mixed-chirality leading sign",
        gravitino_numerator,
        r"={}-\left(",
    )

    exchange_amplitude = tagged_equation(
        "latex/chapters/chapter31/sec313.tex",
        "31.3.14",
    )
    if exchange_amplitude.count(r"\Delta^{") != 4:
        print("FAIL: explicit four-block gravitino exchange amplitude")
        print("Delta block count:", exchange_amplitude.count(r"\Delta^{"))
        raise AssertionError("31.3.14 block count")
    print("OK: explicit four-block gravitino exchange amplitude")

    gravitino_mass = tagged_equation(
        "latex/chapters/chapter31/sec316.tex",
        "31.6.44",
    )
    require_contains(
        "gravitino mass undotted block",
        gravitino_mass,
        r"\psi_\mu\sigma^{\mu\nu}\psi_\nu",
    )
    require_contains(
        "gravitino mass dotted conjugate block",
        gravitino_mass,
        r"\bar\psi_\mu\bar\sigma^{\mu\nu}\bar\psi_\nu",
    )

    weyl_metric = tagged_equation(
        "latex/chapters/chapter31/sec316.tex",
        "31.6.63",
    )
    require_contains(
        "supergravity Weyl-rescaling power",
        weyl_metric,
        r"=(1-\kappa^2K/3)g_{\mu\nu}",
    )

    even_dimensional_reality = tagged_equation(
        "latex/chapters/chapter32/sec321.tex",
        "32.1.26",
    )
    require_contains(
        "even-dimensional spinor reality sign",
        even_dimensional_reality,
        r"\mathcalS^{\pm*}\mathcalS^{\mp(-1)^{d/2}}",
    )

    chapter31_bibliography = compact(
        read("latex/chapters/chapter31/backmatter.tex")
    )
    for expected in (
        r"\textit{PhysicaA}\textbf{96},141(1979)",
        r"L.~Ib\'a\~nez",
        r"\textbf{123B},214(1983)",
    ):
        require_contains(
            f"corrected Chapter 31 bibliography entry {expected}",
            chapter31_bibliography,
            expected,
        )

    chapter32_bibliography = compact(
        read("latex/chapters/chapter32/backmatter.tex")
    )
    author_index = compact(read("latex/backmatter/indexes.tex"))
    for name in ("Aitken", r"G\"uven"):
        require_contains(
            f"corrected Chapter 32 bibliography name {name}",
            chapter32_bibliography,
            name,
        )
    require_contains(
        "corrected Aitken author-index spelling",
        author_index,
        "Aitken,A.C.",
    )
    require_contains(
        "corrected Güven author-index spelling",
        author_index,
        "Güven,R.",
    )

    print("All translation-sensitive semantic hotspot checks passed.")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except AssertionError:
        sys.exit(1)
