# Author Index transcription report

## Scope and source

- Transcribed the complete Author Index from
  `origPapers/weinberg_vol2.pdf`, physical PDF pages 501--506
  (printed pages 478--483).
- Treated the scan as authoritative. OCR and XML extraction were used only as
  navigation aids and were reconciled against fresh rasterizations.
- Fresh 300-DPI full-page source renders:
  `tmp/pdfs/weinberg-vol2-author-index-source.GKEQM7/`
  (`source-501.png` through `source-506.png`, 2480 x 3505 pixels).
- Fresh 600-DPI source-column crops:
  `tmp/pdfs/weinberg-vol2-author-index-crops.2g8P6n/`
  (`page-501-left.png` through `page-506-right.png`, 2150 x 6500 pixels).

## Delivered files

- `latex/backmatter/author-index.tex`
- `latex/checks/author-index-check.tex`
- `latex/backmatter/reports/author-index.md`

No subject-index, index-loader, master, chapter, or other source file was
edited for this task.

## Fidelity inventory

- 468 author entries.
- 25 alphabet groups: A--W, Y, and Z (the scan has no X group).
- 6 source pages and 12 source columns, preserved with explicit
  `multicols*` column and page boundaries.
- Source-column entry counts:

  | Physical page | Left | Right |
  | --- | ---: | ---: |
  | 501 | 33 | 32 |
  | 502 | 44 | 42 |
  | 503 | 42 | 43 |
  | 504 | 45 | 44 |
  | 505 | 44 | 44 |
  | 506 | 28 | 27 |

- 413 page-number tokens are italic in the scan and are encoded with
  `\aidxbib`.
- An independent second scan audit checked all entries and all retained
  italics. It also asserted 275 visually roman page-number tokens that could
  otherwise be mistaken for italics merely because the same page value occurs
  in a reference-list page range; all 275 are bare/roman in the final source.
- The opening note is preserved verbatim:
  “Where page numbers are given in italics, they refer to publications cited
  in lists of references.”
- Hanging continuation indentation, alphabet-group spacing, name punctuation,
  entry order, and all source page/column breaks were checked against the scan.

## Scan-sensitive readings retained

The scan, rather than modern bibliographic normalization, controls the text.
Notable retained readings include `Fanchotti`, `Iliopoulis`,
`Leites-Lopes`, `Moshhin, P. Yu` (double `h`, no period after `Yu`),
`Oleson`, `París J.` (accent and no comma after the surname), `Renk`,
`Rubako`, `Riazuddin`, and `Fayyazuddin`. Maximum-zoom checks also established
`Fürstmann, H.` with the umlaut and `Teplitz, V. I.` with a capital `I`.
Accents in `Alvarez-Gaumé`, `Brézin`, `Fröhlich`, `Lévy`, `Mañes`,
`Ordóñez`, and `Zappalà` were verified directly.

Two especially easy mixed-style cases were independently rechecked:
`Rebbi, C.` has italic 60, roman 475, italic 476; `Voronov, B. L.` has
roman 62 and italic 110.

## Build and visual QA

- Isolated build command, run from `newPapers/weinberg_vol2/latex`:

  `latexmk -g -pdf -interaction=nonstopmode -halt-on-error checks/author-index-check.tex`

- Final artifact: `latex/author-index-check.pdf`, 6 A4 pages, 86,721 bytes.
- Final 180-DPI QA render:
  `/private/tmp/author-index-final-render.tc7hWW/`
  (`page-1.png` through `page-6.png`).
- Every final rendered page was inspected individually. No clipping,
  collisions, malformed continuation lines, missing groups, or column/page
  spill was found.
- The two allowed finishing cycles were used: the first established the
  six-page layout; the second followed the exhaustive scan-style correction
  and is the final build.
- Final log scan found no overfull/underfull boxes, undefined references,
  duplicate destinations, fatal errors, or LaTeX errors. The sole warning is
  the inherited `hyperref` warning that the obsolete `pagecolor` option is no
  longer available.
- Mechanical checks passed: 468 entries, 413 italic tokens, 25 groups,
  6 explicit column breaks, 6 source pages, no conflict markers, and no
  trailing whitespace.
