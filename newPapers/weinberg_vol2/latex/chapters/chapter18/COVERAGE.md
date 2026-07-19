# Chapter 18 Coverage Manifest

## Source boundary

- Source: `origPapers/weinberg_vol2.pdf`.
- Physical PDF pages: 134--185 inclusive.
- Printed book pages: 111--162 inclusive.
- Starts with the Chapter 18 title and introduction on physical p. 134.
- Ends after the Chapter 18 references on physical p. 185.
- Excludes all Chapter 17 material before p. 134 and all Chapter 19 material beginning on p. 186.
- Authoritative review basis: fresh renders of physical pages 134--185 from the source PDF. The temporary page images were removed after final visual QA.
- OCR was used only as a navigation aid and was checked against the rendered pages; its temporary output was removed after QA.

## Semantic ownership and equation coverage

| Output | Physical pages | Printed pages | Semantic coverage | Numbered equations |
|---|---:|---:|---|---|
| `introduction.tex` | 134--135 | 111--112 | Chapter title and introduction, ending before the 18.1 heading on p. 135 | none |
| `sec181.tex` | 135--142 | 112--119 | 18.1 through its final paragraph above the 18.2 heading, including Figs. 18.1--18.3 | (18.1.1)--(18.1.19) |
| `sec182.tex` | 142--153 | 119--130 | 18.2, including its two-paragraph continuation above the 18.3 heading on p. 153 | (18.2.1)--(18.2.50) |
| `sec183.tex` | 153--162 | 130--139 | 18.3 from its heading on p. 153 through the final paragraphs above 18.4, including Fig. 18.4 | (18.3.1)--(18.3.30) |
| `sec184.tex` | 162--167 | 139--144 | 18.4 | (18.4.1)--(18.4.20) |
| `sec185.tex` | 168--171 | 145--148 | 18.5, optional reading; ends at the semantic section boundary on p. 171 | (18.5.1)--(18.5.13) |
| `sec186.tex` | 171--174 | 148--151 | 18.6, beginning at its heading on p. 171 | (18.6.1)--(18.6.15) |
| `sec187.tex` | 175--180 | 152--157 | 18.7 through its final paragraph above the 18.8 heading | (18.7.1)--(18.7.12) |
| `sec188.tex` | 180--181 | 157--158 | 18.8, optional reading; ends before Problems on p. 181 | (18.8.1)--(18.8.8) |
| `backmatter.tex` | 181--185 | 158--162 | Problems 1--6 and all References | none |

All unnumbered displayed equations within these boundaries are required in source order.

## Visual inventory

1. Figure 18.1, physical p. 139: momentum-space Feynman diagrams for a matrix element containing a $\phi^2$ operator insertion; `figures/fig18-01.tex`.
2. Figure 18.2, physical p. 139: class of diagrams exhibiting an ultraviolet divergence; `figures/fig18-02.tex`.
3. Figure 18.3, physical p. 140: divergent part of the Figure 18.2 diagram to one-loop order, including separate contributions and plus sign; `figures/fig18-03.tex`.
4. Figure 18.4, physical p. 154: four schematic beta-function curves (a)--(d), axes, signs, crossings, and marked fixed point $g_*$; `figures/fig18-04.tex`.

Expected figures: 4. Expected tables: 0.

## Problems and references

- Problems: 6, spanning physical pp. 181--182.
- Reference list: 32 displayed entries on physical pp. 182--185.
- Visible identifiers, preserved exactly and each assigned a stable label: 1, 2, 3, 3a, 4, 4a, 4b, 4c, 4d, 5, 6, 7, 8, 8a, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26.
- Unique superscript paper-reference markers to inventory and convert to linked inline markers: [1], [2], [3], [3a], [4], [4a], [4b], [4c], [4d], [5], [6], [7], [8], [8a], [9], [10], [11], [12], [13], [14], [15], [16], [17], [18], [19], [20], [21], [22], [23], [24], [25], and [26], including any source combinations or ranges such as [4a--4d] and [12,13]. Every occurrence must be checked against the rendered page and placed before terminal punctuation.

## Footnotes and optional reading

- Expected ordinary automatically numbered footnotes after modernization: 14.
- Source-page inventory: p. 140 (1), 141 (1), 151 (1), 152 (1), 163 (1), 167 (1), 168 (1), 169 (2), 170 (1), 175 (1), 176 (1), 178 (1), 180 (1).
- Sections 18.5 and 18.8 are optional reading. Each title uses an ordinary numbered footnote with a clean optional TOC argument; no literal star, duplicate note, or dangling TOC hyperlink is permitted.

## Page-boundary continuations

- Physical p. 171 transitions from the end of 18.5 to the 18.6 heading. `sec185.tex` owns only the former; `sec186.tex` owns the latter and following text.
- Physical p. 153 transitions from the final two paragraphs of 18.2 to the 18.3 heading. `sec182.tex` owns the continuation; `sec183.tex` starts at the heading.
- Physical p. 142 transitions from the final part of 18.1 (including Eqs. 18.1.17--18.1.19) to the 18.2 heading. `sec181.tex` owns the former; `sec182.tex` starts at the heading.
- Physical p. 162 transitions from the final part of 18.3 (including Eq. 18.3.30 and its closing paragraphs) to the 18.4 heading. `sec183.tex` owns the former; `sec184.tex` starts at the heading.
- Physical p. 181 transitions from the end of 18.8 to Problems. `sec188.tex` owns only 18.8; `backmatter.tex` owns Problems.
- Physical p. 180 transitions from the final part of 18.7 to the optional 18.8 heading. `sec187.tex` owns the former; `sec188.tex` starts at the heading.
- Physical p. 182 transitions from Problems to References. `backmatter.tex` owns both and must include the passage exactly once.
- Other prose, display, footnote, and reference continuations across adjacent physical pages remain with the semantic section/backmatter owner.

## Initial source-review uncertainties

These are verification targets, not permission to guess or alter the source:

- Exact signs and coefficients of every beta-function and anomalous dimension.
- Distinguishing $\beta$, $\phi$, $\mu$, $\nu$, $\Lambda$, $\Gamma$, $F$, $n_f$, $Z_2$, $Z_3$, and $\alpha_s$ from OCR substitutions.
- Factors of $i$, 2, $4\pi$, $16\pi^2$, measures, $i\epsilon$ prescriptions, logarithm arguments and powers, and all $O(\cdot)$ orders.
- Bare, conventionally renormalized, and sliding-scale couplings; renormalization scales versus cutoffs, masses, external scales, and integration constants.
- Fixed-point eigenvalue signs, eigenvectors, relevant/irrelevant directions, flavor thresholds, group-theory factors, and historical numerical values/uncertainties.
- The rendered source confirms that section 18.4 ends with Eq. (18.4.20) on physical p. 167; the initial request's provisional endpoint (18.4.19) was one equation short.
- The rendered source confirms that section 18.1 ends with Eq. (18.1.19) on physical p. 142; the initial request's provisional endpoint (18.1.17) was two equations short.
- The rendered source confirms that section 18.6 ends with Eq. (18.6.15); the initial request's provisional endpoint (18.6.14) was one equation short.
- Complete wording and punctuation of all captions, notes, problems, reference entries, and lettered citation markers.
- Figure connectivity, cross-hatching, external-line count, relative sizing/spacing, curve slopes/crossings, and the location of $g_*$.

Each owning worker must resolve these from rendered pages, compile an isolated check, render it, and report any remaining concrete uncertainty.

## Final verification

- Completed in two transcription waves, with each section checked against the rendered source pages rather than OCR alone.
- Verified totals: 167 numbered equations, 4 TikZ figures, 14 ordinary footnotes, 6 problems, and 32 linked reference entries.
- The chapter-only check compiled to 45 pages with no LaTeX errors or undefined references; all pages were rendered and visually reviewed.
- The full volume compiled to 153 pages with no LaTeX errors or undefined references; the complete Chapter 18 span was rendered and visually reviewed.
- Three small, non-clipping overfull-box warnings remain in Chapter 18 (maximum 8.44 pt). They are visually harmless and were left unchanged to preserve faithful mathematical setting.
