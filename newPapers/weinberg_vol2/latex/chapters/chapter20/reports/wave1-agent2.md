# Chapter 20 Wave 1 Agent 2 Report

## Coverage

- `sec203.tex`: Section 20.3, physical PDF pages 286--288 (printed pages 263--265), from the section heading through the final paragraph immediately before Section 20.4.
- `sec204.tex`: Section 20.4, physical PDF pages 288--289 (printed pages 265--266), from the section heading through the final paragraph immediately before Section 20.5.
- `sec205.tex`: Section 20.5, physical PDF pages 289--295 (printed pages 266--272), from the section heading through the final paragraph immediately before Section 20.6.

## Inventory

- Section 20.3: equations (20.3.1)--(20.3.10), 1 unnumbered display, no footnotes, and no inline citations.
- Section 20.4: equations (20.4.1)--(20.4.8), no unnumbered displays or footnotes, and citation [4].
- Section 20.5: equations (20.5.1)--(20.5.19), 5 unnumbered displays, 2 footnotes, and citations [5] (twice), [6], [7], and [8].
- No figures or tables occur in this source range.

## Verification

- Compiled `checks/chapter20-wave1-agent2-check.tex` successfully with `latexmk`.
- The check PDF has 10 pages. Every page was rendered with Poppler and visually inspected; the first and last semantic boundaries were also checked against the source scans.
- No LaTeX errors, undefined references, duplicate labels, clipped text, equation-tag collisions, or unreadable glyphs were found.
- The log contains eight overfull hboxes (5.99022 pt, 2.17577 pt, 34.32455 pt, 61.46136 pt, 36.96535 pt, 12.32362 pt, 2.42854 pt, and 8.23389 pt) and one 0.14693 pt overfull vbox. All affected pages were visually checked; the material remains inside the physical page boundaries without clipping or collision.
- Equation-tag sequences are complete and consecutive: 1--10 for Section 20.3, 1--8 for Section 20.4, and 1--19 for Section 20.5.
- All 37 numbered equations have matching explicit tags and labels. No `VERIFY`, `TODO`, unresolved transcription markers, deprecated `\mathscr`, or multiplication `\times` remain.

## Source notes

- The source wording “a Greens function” on physical PDF page 286 is preserved as printed.
- The source footnote value \(F=F_\pi=184\) MeV on physical PDF page 294 is preserved.
- No unresolved source ambiguities remain.
