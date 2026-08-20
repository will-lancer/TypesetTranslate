# Independent front-matter audit

Source range: PDF pages 003--015. The canonical source is
`origPapers/pct_spin_statistics_all_that.pdf`. Pages 001--002 are outside this
audit and remain covered by the page-disposition ledger. The inspected source
images are `work/source-pages/pdf-003.jpg` through
`work/source-pages/pdf-015.jpg`.

Files checked: `latex/frontmatter/copyright.tex`,
`latex/frontmatter/preface.tex`, `latex/frontmatter/introduction.tex`, and
`latex/master.tex`.

## Pass 1: page and layout inventory

Every assigned page was inspected at full rendered resolution. The table gives
the native destination and the treatment used in the reading edition.

| PDF page | Printed label | Source material | Native treatment | Result |
| ---: | :--- | :--- | :--- | :--- |
| 003 | unpaginated | Stacked title leaf | JHEP title treatment in `master.tex` | checked |
| 004 | unpaginated | Blank title-leaf verso | omitted as a blank leaf | checked |
| 005 | unpaginated | Title, authors, affiliations, publisher imprint | JHEP title, author, affiliation, and imprint fields in `master.tex` | checked |
| 006 | unpaginated | Publication data, edition history, CIP data, copyright, paper statement, printer line | `frontmatter/copyright.tex` | checked |
| 007 | v | Contents, first page | generated native table of contents | checked |
| 008 | vi | Contents, second page | generated native table of contents | checked |
| 009 | vii | Preface opening, dagger note, signatures, 1978-edition paragraph | `frontmatter/preface.tex` | checked |
| 010 | viii | Preface continuation and signatures | `frontmatter/preface.tex` | checked |
| 011 | unpaginated | Repeated stacked title leaf before the Introduction | JHEP title treatment in `master.tex` | checked |
| 012 | unpaginated | Blank leaf | omitted as a blank leaf | checked |
| 013 | 1 | Introduction heading and three paragraphs | `frontmatter/introduction.tex` | checked |
| 014 | 2 | Five paragraphs and the Schweber dagger note | `frontmatter/introduction.tex` | checked |
| 015 | 3 | Two closing paragraphs and Halmos square | `frontmatter/introduction.tex` | checked |

The source has three visible title treatments across pages 003, 005, and 011.
The reading edition presents one JHEP title leaf, which carries the title,
authors, affiliations, and the publisher imprint once. The copyright file
retains the separate page-006 title line because it belongs to the CIP and
edition data printed there.

## Pass 2: source wording and metadata

The page images settle the following text.

- The title is `PCT, Spin and Statistics, and All That`.
- The authors are `R.F. Streater` and `A.S. Wightman`; the modern title field
  uses spaced initials, `R. F. Streater` and `A. S. Wightman`.
- The affiliations read `Kings College London` and `Princeton University`.
  The source spells `Kings` without an apostrophe.
- The publisher imprint reads `Princeton University Press` and `Princeton and
  Oxford`.
- Page 006 retains the addresses, the first paperback printing statement, the
  Cecelia Duray-Bito illustration acknowledgment, the 1964/1978/1980 printing
  history, all CIP lines, ISBN `0-691-07062-8`, classification codes, the
  copyright line, the ANSI/NISO paper statement, `ABCDEFGHIJ-AL-89`, the
  website, and the `10 9 8 7 6 5 4 3 2 1` printer sequence.
- The Preface reproduces the Bethe opening, the Sellar and Yeatman dagger
  note, both 1963 signatures, the 1978 Appendix paragraph, the Haag-Ruelle
  paragraph, the Bogolubov, Logunov, and Todorov reference, the Araki
  recommendation, and both signature blocks.
- The Introduction reproduces all ten prose units in printed order. The
  Schweber footnote remains attached to `Schweber's book` and the final
  paragraph keeps `Theorem 3-1`, `Halmos notation`, and the end-of-proof square.

The Contents inventory was checked against both source pages. It contains the
Preface, Chapters 1--4, each numbered section, chapter bibliographies, the
Appendix entries, and the Index. The source Contents has no Introduction entry,
so `introduction.tex` does not add one to the generated table of contents.

## Pass 3: notation and LaTeX audit

The title is emitted by the JHEP `\maketitle` block. The duplicated custom
title page was removed from `copyright.tex`. `master.tex` now carries the two
source affiliations and the publisher imprint through JHEP fields. The empty
`\abstract{}` declaration remains empty, and no abstract text was introduced.

The front matter contains no Hilbert-space vector or scalar-product formula,
so the Dirac state macros have no application in these pages. The only
mathematical glyph in the assigned prose is the Halmos square, rendered as
`\blacksquare`. TeX escapes preserve the source's apostrophes, quotation marks,
catalogue em dashes, copyright symbol, accented names, and italic book titles.

The title page, copyright page, Preface, and Introduction each retain source
markers with physical PDF pages and printed folios. Blank leaves have no native
body marker because the ledger classifies them as intentionally omitted.

## Pass 4: integration checks

The following checks were run after the edits.

1. The source images for all pages 003--015 were inspected directly.
2. `pdftotext -f 3 -l 15 -layout origPapers/pct_spin_statistics_all_that.pdf -`
   was used as a search aid, with the page images controlling every reading.
3. `rg` confirmed the front-matter source markers, the single JHEP title field,
   the two author fields, the affiliation field, the imprint field, and the
   absence of an Introduction table-of-contents entry.
4. The source and native page order was checked against `SOURCE_MAP.md` and
   `page-dispositions.jsonl`.

The front-matter source discrepancies found in this pass were the duplicate
custom title page and the unintended Introduction entry in the generated
Contents. Both are repaired in the assigned files. The remaining full-book
compile and rendered-page audit belongs to the integration pass.

Unresolved blockers: none
