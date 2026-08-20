# PCT, Spin and Statistics, and All That: native JHEP edition

This directory holds the source-faithful LaTeX edition of R. F. Streater and
A. S. Wightman's *PCT, Spin and Statistics, and All That*. The printed wording,
proof order, named results, footnotes, chapter bibliographies, appendix, and
index remain the content of the edition. The layout follows the local Weinberg
Volume I JHEP build. Mathematical notation uses the project's Dirac macros and
the conventions recorded in `NOTATION.md`.

The source baseline is the Princeton University Press paperback with revised
preface and corrections from 2000:

```text
TypesetTranslate/origPapers/pct_spin_statistics_all_that.pdf
SHA-256  44fadba731cafe7f009d4e561372febb3597e1f2a4819346ce2efd16befcb889
PDF pages 221
Printed main-text pages 1--207
```

The page images under `work/source-pages/` are review material. They are not
inputs to the native document. Every substantive native unit carries a
`% PCT-SOURCE:` marker with the physical PDF page, printed page, and object
kind. `SOURCE_MANIFEST.yaml`, `SOURCE_MAP.md`, `NOTATION.md`, `ERRATA.md`, and
the ledgers govern the final release audit.

The master assembles the book in source order through direct `\input` calls. A
missing chunk stops the build. Strict mode also requires every listed chunk,
complete source markers, resolved review work, native content, the adopted
notation, compiled-input evidence, and a clean PDF audit, so it cannot export a
partial assembly.

From this directory:

```sh
./build_and_verify.sh --draft
./build_and_verify.sh
```

After a review pass, regenerate its source-bound provenance with:

```sh
python3 scripts/generate_review_provenance.py
```

The command rerenders the complete source-page image set at the declared
`pdftoppm` settings and refuses to write provenance while the page reviews are
bound to a different native PDF.

The strict command writes the checked PDF to
`newPapers/pct-spin-statistics-all-that/pct-spin-statistics-all-that.pdf` after
the source, transcription, review-coverage, rendered-inspection, and release
evidence gates are complete.

The native assembly is organized as follows:

```text
latex/
  master.tex
  pct.sty
  jheppub.sty
  frontmatter/{copyright,preface,introduction}.tex
  chapters/chapter01/{opening,sec1_1,sec1_2,sec1_3,sec1_4,bibliography}.tex
  chapters/chapter02/{opening,sec2_1,sec2_2,sec2_3,sec2_4,sec2_5,sec2_6,bibliography}.tex
  chapters/chapter03/{opening,sec3_1,sec3_2,sec3_3,sec3_4,sec3_5,bibliography}.tex
  chapters/chapter04/{opening,sec4_1,sec4_2,sec4_3,sec4_4,sec4_5,sec4_6,bibliography}.tex
  appendix/{constructive,local-algebras,bibliography}.tex
  backmatter/index.tex
```

The section names follow the printed contents. The chunk files are native
transcription units, rather than facsimile pages or OCR imports.
