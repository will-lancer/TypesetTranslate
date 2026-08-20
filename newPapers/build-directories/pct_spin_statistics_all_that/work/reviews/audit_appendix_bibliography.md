# Independent audit: Appendix bibliography, printed pages 199--204

Source scope: PDF pages 211--216 of
`origPapers/pct_spin_statistics_all_that.pdf`.  Native scope:
`latex/appendix/bibliography.tex`.

I inspected the six rendered source pages, including the top continuation of
reference 21 on PDF page 213 and the top continuation of reference 76 on PDF
page 216.  I checked every entry for author names and initials, title text,
accents, mathematical symbols, journal or book data, volume, page range, year,
editor data, punctuation, and entry boundaries.  The native file contains 91
`\\bibitem` entries, numbered 1 through 91.

## Complete entry pass record

| Source PDF page | Entries checked | Result |
|---|---:|---|
| 211 | 1, 2, 3 | pass |
| 212 | 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21 | pass |
| 213 | continuation of 21; 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39 | pass |
| 214 | 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58 | pass |
| 215 | 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76 | pass |
| 216 | continuation of 76; 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91 | pass |

The six rows account for all 91 entries.  Entries 1--91 were checked
individually, with the source-page mapping in the table preserving the two
entries that cross a page boundary.

## Source discrepancies corrected

Reference 22 follows the source typography `Fortschr. Physik 21`, with no
comma between the journal title and volume.  The native entry now preserves
that punctuation.

Reference 39 ends at `(1974)` on the source page.  The native entry no longer
adds a terminal period.

Reference 66 ends at `(1977)` on the source page.  The native entry no longer
adds a terminal period.  The source's apparent page-range typo `221--136` is
retained verbatim.

All other author strings, initials, accents, titles, mathematical notation,
publication data, punctuation, and years match the inspected source pages.
Source-visible apparent errors remain as printed, including the `1390--139`
page range in reference 18, the `221--136` range in reference 66, and the
missing page data for reference 53.

## Compilation check

The bibliography was compiled independently with pdfTeX using an article
harness that inputs the native file:

```text
pdflatex -interaction=nonstopmode -halt-on-error -jobname=pct-appendix-bibliography
```

The command exited with status 0 and produced a seven-page PDF.  The only
diagnostic was an underfull box in reference 9.  The full draft master build
reached Chapter 4 before stopping at an unrelated missing-math-delimiter
error in `chapters/chapter04/sec4_4.tex`.

Unresolved blockers: none
