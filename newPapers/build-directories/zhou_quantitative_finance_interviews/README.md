# A Practical Guide to Quantitative Finance Interviews: JHEP edition

This project packages Xinfeng Zhou's first edition in the same LaTeX shape used
by the book editions in `TypesetTranslate`: an `article` master, the JHEP
publication package, small chapter assembly files, frozen source identity, and
a strict build script.

The supplied PDF is a 212-page raster scan with an imperfect text layer. The
rendered source pages govern the edition. Forty-two native transcription files
reproduce every included substantive page as searchable LaTeX, with equations,
tables, footnotes, code, and diagrams set in the JHEP layout. The original
cover, title leaf, and static contents leaves give way to JHEP front matter and
a linked table of contents. `SOURCE_MAP.md` records every source-page
disposition, while `CORRECTIONS.md` records visible source irregularities that
the transcription preserves.

The release gate checks the frozen source hash, page coverage, transcription
recall, notation, unresolved queries, compilation, embedded fonts, raster use,
and final page count. Page-by-page comparison against the rendered scan remains
the authority for wording and mathematics.

The JHEP package is resolved from the local TeX tree:

```sh
kpsewhich jheppub.sty
```

Build and verify from the project root:

```sh
./build_and_verify.sh
```

The verified PDF is exported to the paired release directory:

```text
newPapers/zhou-quantitative-finance-interviews/
  zhou-quantitative-finance-interviews-jhep.pdf
```
