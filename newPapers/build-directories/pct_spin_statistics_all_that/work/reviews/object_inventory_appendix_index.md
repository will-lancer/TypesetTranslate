# Appendix and Index object inventory

PASS:

INPUT SNAPSHOT: `origPapers/pct_spin_statistics_all_that.pdf`, SHA-256 `44fadba731cafe7f009d4e561372febb3597e1f2a4819346ce2efd16befcb889`, 221 pages. The audit covers physical PDF pages 191--219, corresponding to printed pages 179--207. The inspected native inputs are `latex/appendix/constructive.tex`, `latex/appendix/local-algebras.tex`, `latex/appendix/bibliography.tex`, `latex/backmatter/index.tex`, and `latex/figures/figA1.tex`, `figA2.tex`, `figA3.tex`.

FULL SCOPE READ: Every source page in the Appendix, bibliography, and Index packet was read from the canonical rendered pages `work/source-pages/pdf-191.jpg` through `pdf-219.jpg`. Text, equations, displayed and inline mathematics, headings, footnotes, list continuations, proof or theorem endings, figure objects, bibliography items, index entries, subentries, and packet boundaries were compared against the native files.

## Appendix heading structure

PDF 191 prints an unlettered `APPENDIX`, followed by the centered title `SOME MORE RECENT DEVELOPMENTS IN QUANTUM FIELD THEORY`. The two internal headings are unnumbered all-capital source headings. The edition now preserves that visible structure:

* `constructive.tex` uses `\section*{APPENDIX}` and the centered title. A local `\refstepcounter{section}` supplies the internal Appendix A namespace for equation and hyperlink identity. It produces no visible section letter.
* The constructive and local-algebra headings use `\subsection*{...}`. They have no visible `A-1` or `A-2` labels.
* `\phantomsection` and `\addcontentsline` put `Appendix` at section level in the TOC. The two unnumbered subsection titles enter below it at subsection level. The bibliography enters as a subsection and the Index enters as a section.

This gives the source's unlettered printed page while preserving a clean JHEP hierarchy and usable TOC links. The equation namespace remains `A.1`, `A.2`, and the local hyperlink names remain stable.

## Constructive quantum field theory

The displayed-object inventory after the source display pass is:

| Source page | Printed page | Displays | Other objects and boundary evidence |
|---|---:|---:|---|
| PDF 191 | 179 | 0 | Appendix title, introduction, constructive heading |
| PDF 192 | 180 | 4 | Yukawa and total-Hamiltonian material begins |
| PDF 193 | 181 | 5 | Exact manually tagged equations `(A.1)` and `(A.2)` |
| PDF 194 | 182 | 3 | `$H_\kappa$`, `$N$`, and `$[H_\kappa,N]=0$`; the renormalized `$H_\infty$` limit and exponential remain inline as in the source |
| PDF 195 | 183 | 0 | The semigroup, `$H_{1,V}$`, and `$H_V$` formulas are inline source mathematics |
| PDF 196 | 184 | 5 | Figure A.1; list item (c) continues into item (d) |
| PDF 197 | 185 | 2 | Inner automorphism and inner time evolution displays; Euclidean semigroup is inline |
| PDF 198 | 186 | 3 | Constructive-field-theory continuation |
| PDF 199 | 187 | 3 | Continuation and list material |
| PDF 200 | 188 | 1 | Figure A.2 |
| PDF 201 | 189 | 0 | Questions and list continuation |
| PDF 202 | 190 | 2 | Gell--Mann--Low formula and kernel; continuation into local algebras |

Equations `(A.1)` and `(A.2)` are retained as explicit source tags in `constructive.tex`. Their vacuum expectation values, references in the surrounding prose, and equation labels agree. The source's unnumbered displayed formulas were checked separately from the two tagged equations. The list ending crosses PDF 195--197: item (c) starts on PDF 195, item (d) continues on PDF 196, and item (e) closes the list on PDF 197.

## Local algebras and superselection sectors

| Source page | Printed page | Displays | Other objects and boundary evidence |
|---|---:|---:|---|
| PDF 203 | 191 | 2 source displays | Axiom I and Axiom II; the multiline Axiom II display is represented by two aligned LaTeX blocks with one source continuation |
| PDF 204 | 192 | 8 | Local commutativity, state properties, additivity, positivity, normalization, invariance, and GNS equations (1) and (2); theorem starts here |
| PDF 205 | 193 | 3 | GNS equations (3) and (4), then the theorem's interpretation prose |
| PDF 206 | 194 | 6 | Massless field, currents, charges, direct-sum representation, massive Thirring model, and boson-fermion current; dagger footnote restored exactly |
| PDF 207 | 195 | 5 | Massive charge, direct sum, two automorphism limits, and the new state |
| PDF 208 | 196 | 2 | Soliton and anti-soliton limits; sentence continues to PDF 209 |
| PDF 209 | 197 | 3 | Vacuum sectors and the four-sector direct sum |
| PDF 210 | 198 | 0 | Figure A.3 |
| PDF 211 | 199 | 0 | Local-algebra closing prose resumes after Figure A.3, then bibliography begins |

The GNS theorem statement begins on PDF 204, carries equations (1) and (2), continues on PDF 205 with equations (3) and (4), and ends before the paragraph beginning `Thus, the GNS construction`. The source has no separately labelled proof ending. A search of both Appendix source files finds no `proof` environment. The dagger footnote on PDF 206 reads: “The currents of the Thirring model are obtained from the free currents, above, by an automorphism mixing $j$ and $j^5$.”

The sentence ending PDF 208 with `The iteration` resumes on PDF 209 with `of the automorphism associated ...`. The missing local-algebra closing prose after Figure A.3 was restored in `local-algebras.tex` at the PDF 211 boundary. It includes the three Hilbert-space choices, the gauge-transformation discussion, the generalized relativistic-QFT conclusion, and references [88]--[91].

## Appendix figures

| Source | Native file | Inventory result |
|---|---|---|
| PDF 196, Figure A.1 | `latex/figures/figA1.tex` | Native TikZ dependence diamond, axes, light-cone boundary, arrows, labels, and exact caption. |
| PDF 200, Figure A.2 | `latex/figures/figA2.tex` | Native TikZ Ising phase diagram with axes, phases, critical line, labels, and exact caption. |
| PDF 210, Figure A.3 | `latex/figures/figA3.tex` | Native TikZ five profile plots, source arrows and labels, and exact caption. |

The three figure files were inspected against source pages PDF 196, 200, and 210. Their captions and referenced figure numbers agree with the surrounding prose. The output uses vector TikZ geometry and the JHEP figure float, while retaining the source objects and labels.

## Bibliography

`bibliography.tex` contains 91 source `\bibitem` records, numbered 1 through 91 in source order. The packet map is:

| Source page | Entries |
|---|---|
| PDF 211 | heading and 1--3 |
| PDF 212 | 4--21 |
| PDF 213 | continuation of 21, then 22--39 |
| PDF 214 | 40--58 |
| PDF 215 | 59--76 |
| PDF 216 | continuation of 76, then 77--91 |

The source's numerical optional arguments are consumed by a local `\bibitem` wrapper because natbib's numerical mode otherwise treats them as author-year labels and renders empty labels. The wrapper lets the bibliography counter typeset `[1]` through `[91]`; the final standalone extraction confirms the complete sequence. Source wording, punctuation, ordering, and the two packet continuations were retained. The bibliography heading has a TOC anchor and appears below the Appendix subsections.

## Index

`backmatter/index.tex` contains 205 main entries, 24 subentries, 229 item or subitem lines in total, and 20 `\indexspace` divisions. The source entries and subentries were checked in order across all three pages:

* PDF 217 begins the index packet and contains the first 76 item or subitem lines.
* PDF 218 continues after the source packet marker and contains the next 73 lines.
* PDF 219 continues after the second marker and contains the final 80 lines.

The native output keeps the source's two-column presentation, bold main entries, indented roman subentries, and page references. The index heading is `INDEX`. Its section-level TOC entry is anchored with `\phantomsection`. A local plain-page-style definition keeps the continuous reading-edition page counter, so the standalone index pages carry pages 24--26 rather than restarting at 1.

## Boundary audit

The following cross-page and cross-file continuations were checked explicitly:

* constructive list items (c), (d), and (e), across PDF 195--197;
* constructive closing prose on PDF 202 into the local-algebra heading on PDF 203;
* GNS theorem and equations (1)--(4), across PDF 204--205;
* the soliton sentence, across PDF 208--209;
* Figure A.3 into the restored local closing prose on PDF 210--211;
* bibliography item 21, across PDF 212--213;
* bibliography item 76, across PDF 215--216;
* Index packet markers and entry order, across PDF 217--219.

## Edits made

FINDINGS: PDF 191 | the previous JHEP hierarchy exposed generated Appendix labels | the source visibly uses unlettered `APPENDIX` and unnumbered subsection headings | heading identity and TOC claim.

EDITS MADE: `latex/appendix/constructive.tex` and `latex/appendix/local-algebras.tex` | starred visible headings, internal Appendix section step, and explicit TOC anchors | visible source structure and clean internal links.

FINDINGS: PDF 194--197 | several formulas had been promoted to display math | source pages set those formulas inline | display inventory and page rhythm.

EDITS MADE: `latex/appendix/constructive.tex` | restored inline treatment for the `$H_\infty$` limit, exponential, semigroup, `$H_{1,V}$`, `$H_V$`, and Euclidean semigroup formulas | source display status.

FINDINGS: PDF 211 | local-algebra closing prose was absent after Figure A.3 | source continues through the generalized-QFT conclusion and citations [88]--[91] | prose completeness.

EDITS MADE: `latex/appendix/local-algebras.tex` | restored the PDF 211 continuation verbatim in the house notation | boundary continuity.

FINDINGS: PDF 211--216 | optional source labels rendered as empty bibliography labels under natbib | the source requires numerical labels 1--91 | bibliography object identity.

EDITS MADE: `latex/appendix/bibliography.tex` | local numerical-label wrapper and bibliography TOC anchor | rendered labels and TOC navigation.

FINDINGS: PDF 217--219 | JHEP plain style restarted the index page counter and lacked a TOC anchor | the reading edition has continuous backmatter pagination and a Contents entry | backmatter identity.

EDITS MADE: `latex/backmatter/index.tex` | local page-style override and Index TOC anchor | continuous pages and TOC navigation.

## Checks run

* `python3 scripts/audit_source.py` passed: canonical source hash matched, native chunks present 36/36, and 211 distinct marked source pages were found.
* `python3 scripts/audit_project.py` passed: native chunk set 36/36, 36 assembly inputs, and 438 native labels.
* An Appendix/index-only JHEP harness was compiled twice with the master-compatible `\hypersetup{hypertexnames=false}` setting. `/tmp/appcheck_hyperfalse.pdf` is 26 pages. The second pass exited successfully with no undefined or multiply-defined labels, duplicate destinations, or overfull boxes.
* `pdftotext` extraction from the final harness found bibliography labels `[1]` through `[91]` in order.
* Rendered output pages containing the Appendix opening, Figures A.1--A.3, late bibliography entries, and the first and last Index pages were inspected. The shared master compile remains deferred to the parent agent's serialized final build.

STATUS: PASS

Unresolved blockers: none
