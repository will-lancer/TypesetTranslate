# Weinberg, *The Quantum Theory of Fields*, Volume II

JHEP-article format outline for Weinberg Vol.~II, matching the
`article` + `jheppub` layout used for Volume I.

The project includes the structural scaffold for:

- Preface to Volume II and Notation headings
- Chapters 15--23
- every numbered section from 15.1 through 23.8
- all chapter appendices, Problems, and References headings
- Author Index and Subject Index headings

Chapter 15, “Non-Abelian Gauge Theories,” is fully transcribed and modernized
from physical source pages 24--85 (printed pages 1--62). It includes all 209
numbered equations through the two appendices, 23 unnumbered Cartan-catalog
displays, 21 ordinary footnotes, nine problems, and 28 linked references. The
chapter coverage and QA record is in `latex/chapters/chapter15/coverage.md`.

Chapter 16, “External Field Methods,” is fully transcribed and modernized from
physical source pages 86--102 (printed pages 63--79). It includes equations
(16.1.1)--(16.4.12), Figure 16.1 as TikZ, four problems, seven linked
references, and two ordinary footnotes. The chapter coverage and QA record is
in `latex/chapters/chapter16/COVERAGE.md`.

Chapter 17, “Renormalization of Gauge Theories,” is fully transcribed and
modernized from physical source pages 103--133 (printed pages 80--110). It
includes equations (17.1.1)--(17.5.44), Figure 17.1 as TikZ, 12 ordinary
footnotes, four problems, and five linked references. The chapter coverage and
QA record is in `latex/chapters/chapter17/coverage.md`.

Chapter 18, “Renormalization Group Methods,” is fully transcribed and
modernized from physical source pages 134--185 (printed pages 111--162). It
includes all 167 numbered equations, from (18.1.1) through (18.8.8), all four
figures redrawn in TikZ, 14 ordinary footnotes, six problems, and 32 linked
references. The chapter coverage and QA record is in
`latex/chapters/chapter18/COVERAGE.md`.

Stable PDF exports are written to:

- `weinberg-vol2-chapter16.pdf`
- `weinberg-vol2-chapter15.pdf`
- `weinberg-vol2-chapter17.pdf`
- `weinberg-vol2-chapter18.pdf`
- `weinberg-vol2.pdf`

```sh
cd latex && latexmk -pdf master.tex
```
