# Chapter 20 Wave 1 — Agent 1 report

## Coverage and boundaries

- Introduction: physical PDF pp. 275--276 (printed pp. 252--253), from the Chapter 20 opening through immediately before Section 20.1.
- Section 20.1: physical PDF pp. 276--278 (printed pp. 253--255), complete through immediately before Section 20.2.
- Section 20.2: physical PDF pp. 278--285 (printed pp. 255--262), complete through immediately before the Section 20.3 heading on physical p. 286.
- Source boundary verification included fresh 300-DPI renders of physical PDF pp. 275--286.

## File inventory

- `chapters/chapter20/introduction.tex`
- `chapters/chapter20/sec201.tex`
- `chapters/chapter20/sec202.tex`
- `chapters/chapter20/figures/fig20-01.tex`
- `chapters/chapter20/figures/fig20-02.tex`
- `checks/chapter20-wave1-agent1-check.tex`
- `chapters/chapter20/reports/wave1-agent1.md`

No other Chapter 20 content file, chapter assembly file, or master file was edited.

## Content inventory

- Introduction: one unnumbered display and citation markers [1]--[2].
- Section 20.1: Eqs. (20.1.1)--(20.1.9), citation [1], and one automatic footnote.
- Section 20.2: Eqs. (20.2.1)--(20.2.20), citation [3], the automatic optional-reading note, three additional automatic footnotes, and Figures 20.1--20.2.
- All numbered equations have explicit `\tag{...}` and `\label{eq:...}` pairs.
- Citation markers use `\hyperref[ch20-ref-ID]{[ID]}`.
- States, products, calligraphic letters, and other notation were modernized according to `NOTATION.md`.

## Figures

- Figure 20.1 is native TikZ and includes all three diagrammatic terms, the equality and plus signs, four cross-hatched disks, both vertical kernel dividers, every momentum-flow line and arrow, all momentum labels, the `I`/`\Gamma` labels, and the complete caption.
- Figure 20.2 is native TikZ and includes the divided cross-hatched kernel disk, equality sign, tree graph, both one-loop channels, plus signs, continuation ellipsis, and the complete caption.
- Both figures were visually compared with the 300-DPI source render on physical p. 281.

## Verification

- Compile command, run from `newPapers/weinberg_vol2/latex`:

  `latexmk -g -pdf -interaction=nonstopmode -halt-on-error checks/chapter20-wave1-agent1-check.tex`

- Result: success, 10-page PDF, with all references resolved.
- Every output page was rendered at 150 DPI and inspected. The final rendered set is in `/private/tmp/ch20-wave1-agent1-handoff-render.YhZOtM/`.
- The final log contains no undefined references, duplicate labels, missing files, or fatal errors.

## Warnings

- One inherited `hyperref` warning from `jheppub.sty`: option `pagecolor` is no longer available.
- Two visually harmless overfull boxes remain:
  - 3.09525 pt in the introduction's opening paragraph.
  - 0.69559 pt in the prose preceding Eq. (20.2.13).
- The original 79.11383 pt display overflow at Eq. (20.2.13) was removed by a source-faithful line reflow; the final display is within the text block.

## Source anomalies preserved

- The introduction says “renormalization group expansions”; this was verified against the rendered source and preserved.
- Eq. (20.2.1) has an `O(k^{-5})` remainder, verified from the rendered source.
- Figure 20.1's caption ends with “external lines,” even though the nearby prose discusses cutting internal lines; the printed caption was preserved exactly.
- Eq. (20.2.18) uses the kernel ordering `I(k',k,p)` in its second integral; this was verified visually and preserved.

## Uncertainty

None. Dense formulas, captions, footnotes, citation markers, figure labels, and the Section 20.3 boundary were all checked directly against the rendered source.
