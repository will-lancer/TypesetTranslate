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

Chapter 29, “Beyond Perturbation Theory,” is fully transcribed from physical
source pages 271--329 (printed pages 248--306). It includes all 209 numbered
equations, 33 unnumbered display groups, twelve ordinary footnotes, one
typographic divider, one reconstructed figure, three problems, and thirteen
displayed reference entries. Its integrated build, complete rendered review,
internal-link audit, and stable export `weinberg-vol3-chapter29.pdf` have
passed.

Chapter 30, “Supergraphs,” is fully transcribed from physical source pages
330--340 (printed pages 307--317). It includes all 33 numbered equations,
nine unnumbered display groups, three problems, and two displayed reference
entries, with no footnotes, figures, tables, or typographic dividers. Its
integrated build, complete rendered review, internal-link audit, and stable
export `weinberg-vol3-chapter30.pdf` have passed.

Chapter 31, “Supergravity,” is fully transcribed from physical source pages
341--404 (printed pages 318--381). It includes all 289 numbered equations,
36 unnumbered display groups, five ordinary footnotes, three typographic
dividers, six problems, and 28 displayed reference entries, with no figures
or tables. Its integrated 58-page build, complete rendered review,
internal-link audit, and stable export `weinberg-vol3-chapter31.pdf` have
passed.

Chapter 32, “Supersymmetry Algebras in Higher Dimensions,” is fully
transcribed from physical source pages 405--433 (printed pages 382--410),
including the intentionally blank final chapter page. It includes all 109
numbered equations, twelve unnumbered display groups, two ordinary footnotes,
four problems, and fifteen displayed reference entries, with no figures,
tables, or typographic dividers. Its integrated 25-page build, complete
rendered review, internal-link audit, and stable export
`weinberg-vol3-chapter32.pdf` have passed.

The Author and Subject Indexes are fully transcribed from physical source
pages 434--442; physical page 443 is intentionally blank. Their isolated
nine-page build and complete rendered review have passed, preserving the
two-column layout, semantic italics, entry hierarchy, and source-visible
wording.

The complete 373-page master has passed its reference audit, clean build,
all-page rendered review, warning-page inspection, embedded-font check, and
byte-identical stable export. Full production details and artifact hashes are
recorded in `FINAL_AUDIT.md`.

The retained stable PDF export is:

- `weinberg-vol3.pdf`

The chapter-only PDFs, isolated checks, build auxiliaries, and rendered QA
artifacts were removed after their hashes and results were recorded in
`FINAL_AUDIT.md`.

```sh
cd latex && latexmk -pdf master.tex
```
