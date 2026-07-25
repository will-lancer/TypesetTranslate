# Weinberg, *The Quantum Theory of Fields*, Volume III

JHEP-article format modernization of Volume III, *Supersymmetry*, matching
the structure and notation policy used for Volumes I and II.

Source:

- `../../origPapers/weiberg_vol3.pdf` (443 physical PDF pages)

Scope:

- Preface to Volume III
- Notation
- Chapters 24-32
- Every numbered section and chapter appendix
- Every problem set and chapter reference list
- Author Index and Subject Index

The authoritative book-wide structure and source-page map are recorded in
`OUTLINE.md`. Chapter-local transcription and QA records belong in
`latex/chapters/chapterNN/COVERAGE.md`.

The Preface (physical pp. 17--20, printed pp. xvi--xix) and Notation
(physical pp. 21--23, printed pp. xx--xxii) are fully transcribed. Each has
passed an isolated compile and full-page rendered inspection.

Chapter 24 is fully transcribed, structurally audited, compiled in isolation
and in the master, and exported as `weinberg-vol3-chapter24.pdf`.

Chapter 25, “Supersymmetry Algebras,” is fully transcribed from physical
source pages 48--77 (printed pages 25--54). It includes all 119 numbered
equations, nine ordinary footnotes, one typographic divider, four problems,
and three linked references. Its isolated and full-volume builds, complete
render review, and stable export `weinberg-vol3-chapter25.pdf` have passed.

Chapter 26, “Supersymmetric Field Theories,” is fully transcribed from
physical source pages 78--135 (printed pages 55--112). It includes all 247
numbered equations, 73 unnumbered display groups, ten ordinary footnotes,
four typographic dividers, six problems, and ten displayed reference entries
(References 1--9 plus 7a). Its isolated and full-volume builds, all-page
render reviews, and stable export `weinberg-vol3-chapter26.pdf` have passed.

Chapter 27, “Supersymmetric Gauge Theories,” is fully transcribed from
physical source pages 136--201 (printed pages 113--178). It includes all 218
numbered equations, one reconstructed figure, twelve ordinary footnotes, two
typographic dividers, five problems, and 21 displayed reference entries. Its
isolated and full-volume builds, complete 59-page rendered review, internal
link audit, and stable export `weinberg-vol3-chapter27.pdf` have passed.

Chapter 28, “Supersymmetric Versions of the Standard Model,” is fully
transcribed from physical source pages 202--270 (printed pages 179--247). It
includes all 148 numbered equations, 29 unnumbered display groups, seven
reconstructed figures, one table, four ordinary footnotes, two typographic
dividers, five problems, and 59 displayed reference entries. Its isolated and
full-volume builds, complete rendered review, internal-link audit, and stable
export `weinberg-vol3-chapter28.pdf` have passed.

Stable PDF exports will be written to:

- `weinberg-vol3-chapter24.pdf` through `weinberg-vol3-chapter32.pdf`
- `weinberg-vol3.pdf`

```sh
cd latex && latexmk -pdf master.tex
```
