# Chapter 4 bibliography packet review

## Source range

- Source: `pct_spin_statistics_all_that.pdf`
- Physical PDF pages: 187--190
- Printed pages: 175--178
- Native file: `latex/chapters/chapter04/bibliography.tex`
- Source type: rendered page images; the PDF text layer is empty for this range

## Coverage

The packet contains the Chapter 4 heading, every introductory prose block, and
the complete reference sequence 1--29, including the source's intermediate
entry 19a. The page allocation is:

| PDF page | Printed page | Native material |
| ---: | ---: | --- |
| 187 | 175 | Heading, introductory blocks, references 1--9 |
| 188 | 176 | Introductory blocks, references 10--18 |
| 189 | 177 | Introductory blocks, references 19, 19a, and 20--28 |
| 190 | 178 | Introductory sentence and reference 29 |

Each native prose or bibliography block begins with a `% PCT-SOURCE:` marker.
The list labels preserve the printed numbering, including `19a.`. No source
footnotes occur on these four pages.

## Image checks

- The page 175 header reads `Bibliography 175`; page 176 begins with the
  running title and folio `176`; pages 177 and 178 retain the printed running
  headers.
- Item 10 reads `Eine Bemerkung zum CTP Theorem` in the scan. The transcription
  keeps `CTP` rather than silently normalizing it to `PCT`.
- Item 2 retains the French title `Discussion des 'Axiomes' et des propriétés
  asymptotiques d'une théorie des champs locale avec particules composées`.
- Item 3 retains the German word `Unitäräquivalenz`; item 13 retains
  `kräftefreier`; item 19a retains `Über das Paulische Äquivalenzverbot`; item
  25 retains `Über die Mannigfaltigkeit ... zu einer kausalen S-Matrix`.
- Item 22 reads `Mat. Fys. Medd. Dan. Vid. Selsk.` in the scan.
- Item 28 ends with the page/article identifier `B248`, with a capital `B`.
- Item 29 retains the parenthetical publication description, including
  `Lectures in Applied Mathematics IV`, `Boulder, Colorado, 1960`, and
  `Providence, R.I., 1965`.

## Native presentation

The original prose remains prose. Each numbered bibliography block uses a
native list with the original label, while journal names and book titles use
semantic emphasis. Scanned pages, OCR imports, and invented citation keys are
absent. TeX accent commands carry the visible diacritics without introducing
Unicode source characters.

## Local QA

The packet compiles in a standalone JHEP harness. The three-page test PDF has
no overfull or underfull boxes, passes Ghostscript parsing, and embeds every
font as a subset. The rendered pages were inspected at reading size; list
labels, accents, quotation marks, and the 19a label remain legible.

## Independent reconciliation

`audit_ch4_late.md` independently checked PDF 187--190 in source order. It
confirms the single chapter bibliography heading, introductory prose, every
reference from 1 through 29, the intermediate 19a entry, the restored phrase
“It also appears in,” source markers on all four pages, and the scoped native
`thebibliography` lists. The source-page image audit agrees with the packet's
readings of CTP, `Unitäräquivalenz`, `kräftefreier`, `B248`, and the final
publication parenthetical.

Unresolved blockers: none
