# Chapter 22 Section 22.6 — root report

## Coverage and boundaries

- Section 22.6, “Consistency Conditions”: physical PDF pp. 419--430
  (printed pp. 396--407).
- The transcription begins at the Section 22.6 heading on physical p. 419,
  after the closing Section 22.5 paragraph. It ends with the final sentence
  on physical p. 430. The Section 22.7 heading and all subsequent text on
  physical p. 431 are excluded.
- All twelve source pages and the p. 431 closing boundary were inspected from
  fresh 240-DPI renders. Ambiguous formulas on physical pp. 425 and 427 were
  additionally checked in fresh 600-DPI renders.

## Inventory

- Eqs. (22.6.1)--(22.6.35), consecutive, with matching explicit tags and
  labels.
- Twenty-one unnumbered mathematical displays.
- Four automatic semantic footnotes and one centered `* * *` divider.
- Linked Chapter 22 citations 8, 18, 18a--18c, 19, 19a, and 20--23.
- Linked external section and equation references required from Chapters 8,
  15--17, and Section 22.3; the isolated wrapper supplies check-only
  destinations for them.
- No figures or tables.

## Build and visual QA

- `checks/chapter22-root-sec226-check.tex` compiles successfully with
  `latexmk` to an 11-page A4 PDF.
- The final log has no LaTeX errors, unresolved links, duplicate labels,
  overfull boxes, or underfull boxes. The inherited `hyperref` `pagecolor`
  notice is the only package warning.
- All 11 pages were rendered at 180 DPI and inspected in
  `/private/tmp/ch22-root-sec226-qa/`. Full-resolution checks covered the
  long BRST variations, the descent equations, the Schwinger-term
  construction, the all-orders antibracket calculation, all four footnotes,
  and the closing boundary. The corrected lowercase generator in
  Eq. (22.6.21) was recompiled, rerendered at 220 DPI, and reinspected.
- Static checks confirm 35 strict-sequence tags, 35 matching labels, four
  footnotes, 21 unnumbered displays, one divider, no placeholders, and a
  clean scoped `git diff --check`.
- A final notation pass normalized the source's two multiplication signs to
  the project-standard `\cdot`; the section was rebuilt, the affected pages
  were rerendered and reinspected, and the log remained clean.
- Correction cycles used: two of the permitted two.

## Source anomalies preserved

- Eq. (22.6.21) prints lowercase \(t_\alpha\), although the surrounding
  general-representation formulas use uppercase \(T_\alpha\).
- Eq. (22.6.24) explicitly prints
  \(\operatorname{Tr}\{F^{2n+2}\}=d\Omega_{2n+1}\), although the immediately
  preceding and following formulas use \(F^{n+1}\).
- The paragraph before Eq. (22.6.29) prints
  \(d\Omega_{2n+1}=\operatorname{Tr}\{F^3\}\) while discussing general
  \(2n\)-dimensional spacetime.
- The prose before Eq. (22.6.28) says “It follows than that.”
- The Schwinger-term derivation contracts the third current
  \(J^0_\gamma(\mathbf z)\) with a printed
  \(\omega_\alpha(\mathbf z)\), repeating the \(\alpha\) index; both the
  prose and the following unnumbered display were checked at 600 DPI and
  preserved.
- The candidate-anomaly paragraph says that the local \(F_1\) excluded from
  the cohomology has ghost number unity, despite the earlier statement that
  an exact counterterm functional has ghost number zero.
- The closing theorem discussion prints “terms of the of the form” and “any
  menu of fermion fields.” Both wordings were preserved.

No unresolved transcription uncertainty remains.
