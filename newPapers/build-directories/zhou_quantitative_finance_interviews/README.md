# A Practical Guide to Quantitative Finance Interviews: JHEP edition

This project packages Xinfeng Zhou's first edition in the same LaTeX shape used
by the book editions in `TypesetTranslate`: an `article` master, the JHEP
publication package, small chapter assembly files, frozen source identity, and
a strict build script.

The supplied PDF is a 212-page raster scan with an imperfect text layer.  The
edition therefore treats the rendered source pages as authoritative.  It
replaces the original cover, title leaf, and static contents leaves with JHEP
front matter and a linked table of contents.  Every substantive source page is
included without OCR rewriting.  The source-page dispositions are recorded in
`SOURCE_MAP.md`.

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
