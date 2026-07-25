# Chapter 22 wave 1 — agent 2 report

## Scope and source boundary

- Transcribed complete Section 22.3, “Direct Calculation of Anomalies: The
  General Case,” from physical PDF pages 393--406 (printed pages 370--383).
- The transcription begins at the Section 22.3 heading on physical page 393
  and ends after the Witten \(SU(2)\) global-anomaly paragraph on physical
  page 406, immediately before the centered Section 22.4 heading.
- The running head on physical page 406 already says “22.4 Anomaly-Free Gauge
  Theories,” although the upper body of that page is still Section 22.3. The
  actual centered Section 22.4 heading, and all content below it, are
  excluded.
- Fresh 300-DPI renders
  `tmp/pdfs/ch22-wave1-agent2/source-300/page-393.png` through
  `page-406.png` were the authority. Every source page was inspected
  individually at full resolution; OCR was used only as an aid.
- No Chapter 22 assembly file or content outside Section 22.3 was edited.

## Delivered files

- `latex/chapters/chapter22/sec223.tex`
- `latex/chapters/chapter22/figures/fig22-01.tex`
- `latex/chapters/chapter22/figures/fig22-02.tex`
- `latex/checks/chapter22-wave1-agent2-check.tex`
- `latex/chapters/chapter22/reports/wave1-agent2.md`

## Exact content inventory

- 47 numbered equations, (22.3.1)--(22.3.47), in strict sequence. Every
  equation has an explicit `\tag{22.3.N}` and matching
  `\label{eq:22.3.N}`.
- 14 unnumbered mathematical displays.
- 2 recreated TikZ figures: Figures 22.1 and 22.2. No scan images were used.
- 2 automatic semantic body footnotes.
- 1 centered three-asterisk divider.
- Unique linked Chapter 22 citations: [7], [7a], [8], [8a], [9], [10],
  [10a], and [10b].
- No tables or section-title notes.
- Equation, figure, section, and citation references are linked. Notation
  follows `NOTATION.md`, including `\mathcal`, `\gamma^5`, `\sl{}`, and
  `\cdot` in place of printed multiplication signs.

## Source anomalies and normalization

- Physical page 394 / printed page 371 has a diagonal overprint or scan
  corruption across the charge-conjugation identity. The obscured identity
  was reconstructed from the visible remnants and the convention in
  Volume I, Section 5.4 as
  \(\mathcal C\gamma^{\mu *}\mathcal C^{-1}=\gamma_\mu\). This
  reconstruction is documented in the source-file header.
- Physical page 405 / printed page 382 visibly omits the sentence space in
  “(for \(r\ne r'\)).The anomalies”. Ordinary sentence spacing was
  normalized in the transcription.
- Physical page 405 / printed page 382 says “in additional to”; this wording
  was confirmed in the rendered source and intentionally preserved.
- Physical page 406 / printed page 383 has the premature Section 22.4
  running head described above. The semantic body boundary, not the running
  head, governs the transcription.

## Integration dependencies

- External equation destinations:
  `eq:19.7.2`, `eq:22.2.26`.
- External section destinations:
  `sec:5.4`, `sec:5.5`, `sec:10.4`, `sec:22.2`, `sec:22.6`, and
  `sec:22.7`.
- External chapter-reference destinations:
  `ch22-ref-7`, `ch22-ref-7a`, `ch22-ref-8`, `ch22-ref-8a`,
  `ch22-ref-9`, `ch22-ref-10`, `ch22-ref-10a`, and `ch22-ref-10b`.
- New local destinations:
  `sec:22.3`, `eq:22.3.1`--`eq:22.3.47`, `fig:22.1`, and `fig:22.2`.
- The two figures use the existing TikZ support and require the
  `decorations.pathmorphing`, `arrows.meta`, and `calc` TikZ libraries.

## Build and visual QA

- Isolated wrapper:
  `checks/chapter22-wave1-agent2-check.tex`.
- Build command, run from `newPapers/weinberg_vol2/latex`:
  `latexmk -pdf -interaction=nonstopmode -halt-on-error
  checks/chapter22-wave1-agent2-check.tex`.
- Result: successful 12-page A4 PDF,
  `latex/chapter22-wave1-agent2-check.pdf`.
- The initial full build was rendered at 220 DPI to
  `tmp/pdfs/ch22-wave1-agent2/render-cycle0/page-01.png` through
  `page-12.png`; every page was inspected individually at full resolution.
- Both permitted correction cycles were used:
  - Cycle 1 split Eq. (22.3.10) into source-faithful rows and separated the
    middle and right diagrams in Figure 22.2.
  - Cycle 2 removed the final small Eq. (22.3.10) overflow and applied a
    tightly scoped sentence-space adjustment near Eqs. (22.3.11)--(22.3.13).
- The accepted build was rendered at 220 DPI to
  `tmp/pdfs/ch22-wave1-agent2/render-cycle2/page-01.png` through
  `page-12.png`. All 12 pages were again inspected individually at full
  resolution. Equations and tags, both figures, links, footnotes, page
  edges, and the final Section 22.3 boundary are clear and unclipped.
- Static audits confirmed 47 strict-sequence tags, 47 matching
  strict-sequence labels, 14 unnumbered displays, 2 figures, 2 footnotes,
  zero tables, and no prohibited `\times` or `\mathscr` notation.
- The final log has no undefined or multiply defined references, overfull
  or underfull boxes, missing files, or content warnings. Its sole warning
  is the inherited `jheppub`/`hyperref` warning that option `pagecolor` is
  no longer available.

## Uncertainty

None beyond the explicitly documented reconstruction of the obscured
charge-conjugation identity on physical page 394.
