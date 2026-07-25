# Chapter 21 Wave 1 — Agent 1 report

## Coverage and boundaries

- Section 21.3, “The Electroweak Theory”: physical PDF pp. 328--341 (printed pp. 305--318).
- The transcription begins with the Section 21.3 heading on physical p. 328 and ends with the proton-decay paragraph immediately before the Section 21.4 heading on physical p. 341.
- Boundary and content verification used fresh 300-DPI renders of every source page in the span.

## File inventory

- `chapters/chapter21/sec213.tex`
- `checks/chapter21-wave1-agent1-check.tex`
- `chapters/chapter21/reports/wave1-agent1.md`

No other Chapter 21 content file, chapter assembly file, or master file was edited.

## Content inventory

- Eqs. (21.3.1)--(21.3.55), in strict sequence, plus six unnumbered displays.
- Every numbered equation has an explicit `\tag{21.3.N}` and matching `\label{eq:21.3.N}`.
- Five source footnotes and the centered `* * *` break are present.
- Citation markers present: [3], [6]--[20], [20a], [20b], [21]--[27], [27a], [27b], and [27c].
- Internal equation and section citations are linked; citation markers use `\hyperref[ch21-ref-ID]{[ID]}`.
- There are no figures or tables in the assigned span.
- Products, representations, matrices, conjugates, and other notation follow `NOTATION.md`.

## Verification

- Compile command, run from `newPapers/weinberg_vol2/latex`:

  `latexmk -g -pdf -interaction=nonstopmode -halt-on-error -outdir=../../../tmp/pdfs/weinberg-vol2-ch21-wave1-agent1-check checks/chapter21-wave1-agent1-check.tex`

- Result: success after the normal two LaTeX passes, producing a 12-page PDF with all references resolved.
- The final log contains no overfull boxes, underfull boxes, undefined references, multiply defined labels, missing files, or fatal errors.
- All 12 output pages were rendered at 180 DPI and inspected. A full contact-sheet pass was supplemented with original-resolution checks of the opening, the split Eq. (21.3.20), dense equation pages, footnote pages, and the closing boundary.
- Rendered pages: `tmp/pdfs/weinberg-vol2-ch21-wave1-agent1-check/render/page-01.png` through `page-12.png`.
- Contact sheet: `tmp/pdfs/weinberg-vol2-ch21-wave1-agent1-check/contact.png`.
- Static audits confirmed 55 strict-sequence tags, 55 matching strict-sequence labels, five source footnotes, no placeholders, no prohibited identity/mathematical-script macros, and a clean `git diff --check`.

## Warnings

- One inherited `hyperref` warning from `jheppub.sty`: option `pagecolor` is no longer available.
- No content or layout warning remains.

## Source anomalies preserved

- The footnote after the discussion of real two-generation quark mixing says “which can be eliminating”; the printed wording was verified and preserved.
- Historical numerical values and the source’s period-specific terminology were preserved without silent updating.

## Uncertainty

None. Prose, numbered and unnumbered mathematics, footnotes, citation markers, typography, paragraph structure, and both section boundaries were checked directly against the rendered source.
