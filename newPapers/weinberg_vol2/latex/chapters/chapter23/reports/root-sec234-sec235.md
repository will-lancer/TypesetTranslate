# Chapter 23 root wave — Sections 23.4--23.5 report

## Scope and source boundary

- Transcribed complete Section 23.4, “The Cartan--Maurer Integral
  Invariant,” from physical PDF pages 468--473 (printed pages 445--450).
  The file ends immediately before the Section 23.5 heading.
- Transcribed complete Section 23.5, “Instantons,” from physical PDF pages
  473--478 (printed pages 450--455). The file ends immediately before the
  Section 23.6 heading.
- Fresh 240-DPI renders
  `/private/tmp/ch23-root-sec234-235.Lm72YE/source-468.png` through
  `source-478.png` were the authority. Every source page was inspected;
  OCR was used only as a navigation aid.
- No Chapter 23 assembly file or content outside Sections 23.4--23.5 was
  edited during this wave.

## Delivered files

- `latex/chapters/chapter23/sec234.tex`
- `latex/chapters/chapter23/sec235.tex`
- `latex/checks/chapter23-root-sec234-sec235-check.tex`
- `latex/chapters/chapter23/reports/root-sec234-sec235.md`

## Exact content inventory

- Section 23.4 contains 14 numbered equations,
  (23.4.1)--(23.4.14), in strict sequence, with 14 matching stable labels.
- Section 23.5 contains 26 numbered equations,
  (23.5.1)--(23.5.26), in strict sequence, with 26 matching stable labels.
- Section 23.4 contains 13 unnumbered displays; Section 23.5 contains 3.
- Section 23.5 contains one centered three-asterisk divider.
- Unique linked Chapter 23 citations are [1], [10], and [22]--[27].
- Neither section contains a numbered figure, table, or footnote.
- Equation, section, appendix, and citation references are linked.
  Modernized notation includes `\mathbb{Z}`, `\mathbf{1}`, `\mathcal`,
  and `\cdot`; no prohibited `\times` or `\mathscr` remains.

## Source anomalies retained

- Physical page 476 / printed page 453 explicitly refers twice to
  Eq. (23.5.14) where the surrounding argument appears to concern the
  action and topological-integral results. Both printed references were
  retained and linked to (23.5.14).
- Physical page 477 / printed page 454 says that “the integral (23.5.15)
  does not vanish,” although (23.5.15) is the displayed instanton action.
  The printed equation reference was retained.
- The printed phrase “A solution with \(\nu=-1\) negative” was confirmed
  in the rendered source and retained.
- Products printed with multiplication signs, plain \(Z\) for the integer
  group, and the identity matrix printed as \(1\) were normalized according
  to `NOTATION.md`.

## Integration dependencies

- External equation destinations:
  `eq:18.7.7`, `eq:22.2.10`, `eq:22.2.29`, `eq:22.2.45`, and
  `eq:23.1.7`.
- External section destinations:
  `sec:2.7`, `sec:18.2`, `sec:19.8`, `sec:19.10`, `sec:22.4`,
  `sec:22.7`, `sec:23.1`, and `sec:23.7`.
- External appendix destination: `app:23.B`.
- External chapter-reference destinations:
  `ch23-ref-1`, `ch23-ref-10`, and `ch23-ref-22`--`ch23-ref-27`.
- New local destinations:
  `sec:23.4`, `sec:23.5`, `eq:23.4.1`--`eq:23.4.14`, and
  `eq:23.5.1`--`eq:23.5.26`.

## Build and visual QA

- Isolated wrapper:
  `checks/chapter23-root-sec234-sec235-check.tex`.
- Build command, run from `newPapers/weinberg_vol2/latex`:
  `latexmk -pdf -interaction=nonstopmode -halt-on-error
  -file-line-error checks/chapter23-root-sec234-sec235-check.tex`.
- Result: successful 9-page A4 PDF,
  `latex/chapter23-root-sec234-sec235-check.pdf`.
- The accepted build was rendered at 180 DPI to
  `/private/tmp/ch23-root-sec234-235.Lm72YE/final3-page-1.png` through
  `final3-page-9.png`. Every page was inspected. Equations, tags, links,
  the divider, page edges, and both semantic section boundaries are clear
  and unclipped.
- Two bounded finishing cycles were used: the first normalized three
  remaining printed multiplication signs to `\cdot`; the second applied
  the required `\mathbb{Z}` and `\mathbf{1}` modernization.
- Static audits confirmed both strict tag sequences, 40 matching equation
  labels, 16 unnumbered displays, one divider, zero figures, zero tables,
  zero footnotes, no placeholders, and no prohibited `\times` or
  `\mathscr`.
- The final log has no undefined or multiply defined references, overfull
  or underfull boxes, missing files, or content warnings. Its sole warning
  is the inherited `jheppub`/`hyperref` warning that option `pagecolor` is
  no longer available.

## Uncertainty

None beyond the explicitly recorded source anomalies.
