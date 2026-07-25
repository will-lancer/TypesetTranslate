# Chapter 19 Wave 2 Agent 2 Report

## Coverage

- `sec197.tex`: Section 19.7, physical PDF pages 248--257 (printed pages 225--234), beginning exactly at the Section 19.7 heading and ending immediately before the Section 19.8 heading.
- `backmatter.tex`: physical PDF pages 269--274 (printed pages 246--251), beginning at the Problems heading after Section 19.10 and continuing through the complete chapter reference list.

## Inventory

- Section 19.7: equations (19.7.1)--(19.7.32), all unnumbered displays, 2 ordinary numbered footnotes, and linked citations [33], [34], [35], [36], [37], [38], [38a], [38b], [39], [40], and [41].
- Back matter: Problems 1--6 and 56 displayed reference entries: 1--52 plus 30a, 32a, 38a, and 38b.
- Every reference entry has a stable `ch19-ref-*` label, and cross-references within the reference list are linked.
- No numbered figures or tables occur in either source range.

## Verification

- Compiled `checks/chapter19-wave2-agent2-check.tex` successfully with `latexmk`.
- The isolated check PDF has 14 pages. All 14 pages were rendered to PNG at 160 dpi and visually inspected, both in contact sheets and at full-page scale where dense mathematics or references required it.
- No LaTeX errors, undefined references, duplicate destinations, clipped text, equation-tag collisions, missing reference entries, or unreadable glyphs were found.
- The final check log contains seven overfull boxes (2.66457--38.64276 pt). The two larger prose cases arise from linked equation-number runs in the deliberately narrow A4 article wrapper; every occurrence was visually checked and remains inside the physical page margins without clipping or collision. The four reference-list cases are long identifiers or titles.
- Equation tags are complete and consecutive from 1 through 32. The reference labels are complete in visible order, including all four lettered identifiers.
- The backmatter contains exactly 6 problem items and 56 reference items.
- No `VERIFY`, `TODO`, scaffold text, or unresolved transcription markers remain.

## Source notes

- Reference 38a visibly prints the unusual identifier `hep-ph/-9602366`; this was preserved rather than silently normalized.
- Reference 11 visibly gives *Phys. Rev.* **111**, 354 as `(1966)`, despite the historically expected year being 1958; the printed source was preserved.
- The source's symbolic footnote markers in Section 19.7 were modernized to ordinary automatically numbered footnotes, and all direct-product signs were modernized to `\cdot` in accordance with `NOTATION.md`.
