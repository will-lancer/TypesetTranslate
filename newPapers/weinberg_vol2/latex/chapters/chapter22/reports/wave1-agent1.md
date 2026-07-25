# Chapter 22 wave 1 — agent 1 report

## Scope and source authority

- Transcribed Section 22.4 from physical PDF pages 406--411 (printed
  pages 383--388), beginning at the section heading and ending immediately
  before Section 22.5.
- Transcribed Section 22.5 from physical PDF pages 412--419 (printed
  pages 389--396), beginning at the section heading and ending immediately
  before Section 22.6.
- Used fresh 300-DPI renders from `origPapers/weinberg_vol2.pdf` as the
  authority. The inspected source render set is
  `tmp/pdfs/weinberg-vol2-ch22-wave1-agent1-source/source-405.png` through
  `source-420.png`; OCR was used only as an aid.
- The task's supplied section-title metadata was stale. The
  scan-authoritative titles used here are **Anomaly-Free Gauge Theories**
  and **Massless Bound States**.

## Content inventory

### Section 22.4

- 3 numbered equations: (22.4.1)--(22.4.3), each explicitly tagged and
  labeled.
- 15 unnumbered display blocks.
- 1 recreated LaTeX table: Table 22.1. No scan image was used.
- Unique linked chapter references: [11], [12], [13], [13a], [14], [15].
- No footnotes and no figures.

### Section 22.5

- 9 numbered equations: (22.5.1)--(22.5.9), each explicitly tagged and
  labeled.
- 3 unnumbered display blocks.
- 1 ordinary numbered section-title note and 4 ordinary numbered body
  footnotes.
- 1 centered three-asterisk divider.
- Representation lists (a)--(j) and (v)--(z).
- Unique linked chapter references: [16], [16a], [17].
- No tables and no figures.

## Preserved source anomalies

The following were checked directly against the scan and intentionally
left unchanged:

- Physical page 412 / printed page 389: “with the fact the observed
  masses” omits “that.”
- Physical page 415 / printed page 392: \(d_s\) is called the
  dimensionality of representation \(s\) of \(SU(N)\), although the
  surrounding flavor representations use \(SU(n)\).
- Physical page 415 / printed page 392: both complex-conjugate
  statements use \(SU(2)_L\cdot SU(2)_R\cdot U(1)_V\) inside a
  general-\(n\) discussion.
- Physical page 416 / printed page 393: the list footnote says
  “All \(SU(N)\) vectors and tensors...” while the list itself uses
  \(SU(n)\).
- Physical page 418 / printed page 395: item (x) says \(r'\) and \(s'\)
  are \(SU(n)\) vectors, although the surrounding subgroup is
  \(SU(n-1)\cdot SU(n-1)\).
- Physical page 419 / printed page 396: “three-fermion mass state” is
  retained verbatim.

## Integration dependencies

- External equation labels required by Section 22.4:
  `eq:22.3.3`, `eq:22.3.12`.
- External section destinations:
  `sec:12.3`, `sec:19.9`, `sec:22.3`, `sec:22.6`, `sec:23.5`.
- External chapter-reference destinations:
  `ch22-ref-11`, `ch22-ref-12`, `ch22-ref-13`, `ch22-ref-13a`,
  `ch22-ref-14`, `ch22-ref-15`, `ch22-ref-16`, `ch22-ref-16a`,
  `ch22-ref-17`.
- New local destinations:
  `sec:22.4`, `sec:22.5`, `eq:22.4.1`--`eq:22.4.3`,
  `eq:22.5.1`--`eq:22.5.9`, and `tab:22.1`.
- No external graphics or new package dependencies were introduced.

## Verification

- Isolated wrapper:
  `checks/chapter22-wave1-agent1-check.tex`.
- Build command, run from `newPapers/weinberg_vol2/latex`:
  `latexmk -pdf -interaction=nonstopmode -halt-on-error checks/chapter22-wave1-agent1-check.tex`.
- Result: success, 10 PDF pages.
- Final log diagnostics: no undefined or multiply defined references, no
  overfull or underfull boxes, and no section-content warnings. The only
  warning is the existing `jheppub`/`hyperref` warning that the
  `pagecolor` option is no longer available.
- Rendered all 10 pages at 180 DPI to
  `/tmp/chapter22-wave1-agent1-render/page-01.png` through
  `page-10.png` and visually inspected every page. Equations, Table 22.1,
  footnotes, links, and page edges are clear and unclipped.
- Two finishing cycles were used. The second corrected the source title's
  true hyphen in “Anomaly-Free” and recompiled/re-rendered cleanly.
