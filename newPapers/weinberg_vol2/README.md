# Weinberg, *The Quantum Theory of Fields*, Volume II

JHEP-article format outline for Weinberg Vol.~II, matching the
`article` + `jheppub` layout used for Volume I.

The project includes:

- the complete Preface to Volume II and Notation
- Chapters 15--23
- every numbered section from 15.1 through 23.8
- all chapter appendices, Problems, and References
- the Author Index and Subject Index

The finished volume represents physical source pages 18--512. Physical page
513 is blank and page 514 is the publisher's back cover, so both are
intentionally excluded. The integrated 434-page PDF contains 1,665
sequentially audited numbered equations, 50 problems, 284 reference entries,
14 redrawn figures, one native table, a 468-entry Author Index, and a
379-entry Subject Index. All 118 production TeX files are reachable from the
master include graph, and every internal reference resolves.

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

Chapter 19, “Spontaneously Broken Global Symmetries,” is fully transcribed and
modernized from physical source pages 186--274 (printed pages 163--251). It
includes all 323 numbered equations, three TikZ figures, 25 automatic
footnotes, six problems, and 56 displayed reference entries. The chapter
coverage and QA record is in `latex/chapters/chapter19/coverage.md`.

Chapter 20, “Operator Product Expansions,” is fully transcribed and modernized
from physical source pages 275--317 (printed pages 252--294). It includes all
160 numbered equations, three TikZ figures, 15 semantic footnotes, five
problems, and 22 linked references. The chapter coverage and QA record is in
`latex/chapters/chapter20/coverage.md`.

Chapter 21, “Spontaneously Broken Gauge Symmetries,” is fully transcribed and
modernized from physical source pages 318--381 (printed pages 295--358). It
includes all 252 numbered equations, 17 semantic footnotes, 31 unnumbered
displays, three centered dividers, six problems, and 57 linked references.
The chapter coverage and QA record is in
`latex/chapters/chapter21/coverage.md`.

Chapter 22, “Anomalies,” is fully transcribed and modernized from physical
source pages 382--443 (printed pages 359--420). It includes all 190 numbered
equations, 62 unnumbered displays, 13 semantic notes, five centered dividers,
two TikZ figures, one native table, four problems, and 37 linked references.
The chapter coverage and QA record is in
`latex/chapters/chapter22/coverage.md`.

Chapter 23, “Extended Field Configurations,” is fully transcribed and
modernized from physical source pages 444--500 (printed pages 421--477). It
includes all 155 numbered equations, 62 unnumbered displays, two semantic
footnotes, two centered dividers, both appendices, six problems, and 40 linked
references. The chapter coverage and QA record is in
`latex/chapters/chapter23/coverage.md`.

The retained PDF deliverables are:

- `weinberg-vol2.pdf`, the user-facing final volume
- `latex/master.pdf`, the byte-identical build artifact

The final full-volume export is 434 A4 pages with SHA-256
`395af2912ec6fedbf330add5914410a85b6f083099d61eeede33604badbaf679`.
The complete acceptance record and historical verification manifest are in
`FINAL_AUDIT.md`; index-specific source audits are in
`latex/backmatter/reports/`.

Chapter-only PDFs, isolated check wrappers, LaTeX auxiliaries, rendered-page
caches, and agent-wave reports were removed after final verification.

```sh
cd latex && latexmk -g -pdf master.tex
```
