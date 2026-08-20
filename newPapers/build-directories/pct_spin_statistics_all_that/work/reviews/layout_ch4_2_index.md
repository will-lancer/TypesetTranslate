# Layout audit: chapter 4 section 2 and index

Scope: `latex/chapters/chapter04/sec4_2.tex` and `latex/backmatter/index.tex`. The source comparison used `work/source-pages/pdf-150.jpg`, `pdf-151.jpg`, and `pdf-217.jpg` through `pdf-219.jpg`. The full manuscript target is `latex/master.tex`.

## Baseline warning record

The pre-edit full TeX build used:

```text
latexmk -g -pdf -interaction=nonstopmode -halt-on-error master.tex
```

The baseline `master.log` recorded the section warning:

```text
Overfull \hbox (3.21974pt too wide) in paragraph at lines 91--96
... Standard arguments ... show that the Fourier transform of F vanishes unless each four-momentum
```

The baseline index warning was:

```text
Underfull \hbox (badness 10000) in paragraph at lines 172--173
... Normal commutation relations ... 145,
```

The source page places the section sentence across two lines after “vanishes”. The source index places `Normal commutation relations, 145,` above `154, 156` in its column.

## Layout edits

In `sec4_2.tex`, `\newline` now follows “vanishes”. It creates the source-like sentence wrap while retaining every word, the footnote marker, the footnote text, and the source markers.

In `index.tex`, the Normal commutation entry remains inside a local `\raggedright` group and keeps the source-like `\linebreak` after 145. The entry retains both locators and its position in the alphabetic sequence. The local setting removes the underfull line warning without changing neighboring entries.

## Historical packet full manuscript rebuild

The release wrapper `./build_and_verify.sh` stopped during its project audit preflight. Its reported items concern existing notation-map statuses and review dispositions outside the two assigned TeX files. I therefore rebuilt the complete manuscript directly from `latex/` with the `latexmk` command above. The command exited with status 0 and wrote the historical packet's `master.pdf` with 185 pages.

The final log contains no `Overfull` or `Underfull` warning associated with `sec4_2.tex` or `backmatter/index.tex`. The remaining layout warnings identify existing content in `chapter03/sec3_3.tex` and an underfull vertical box on page 111. Those locations are outside this audit scope.

## Historical packet render inspection

I rendered the affected chapter pages and index pages at 180 dpi with `pdftoppm`:

```text
master.pdf pages 130--132 -> /private/tmp/pct-layout-after/sec4_2-130.png through sec4_2-132.png
master.pdf pages 183--185 -> /private/tmp/pct-layout-after/index-183.png through index-185.png
```

The section sentence on page 130 now ends its first line at “vanishes”. The second line begins “unless each four-momentum”, matching the source flow. The footnote rule and marker remain visible. Theorem 4-3 and the following equation tags retain their page positions and legibility on pages 131--132.

The index remains a three-page two-column block. The Normal commutation entry wraps at the source locator boundary on page 184. Main entries, subordinate entries, punctuation, and locators remain legible through page 185. The page frames contain all text, and the columns have continuous flow.

The edits affect line flow only. Source words, locators, equations, equation tags, footnote text, and `% PCT-SOURCE` markers remain intact.

## Current final-candidate evidence

The current `latex/master.pdf` is an A4, 180-page PDF with SHA-256
`4741fe42fc72801e9b3bee2249eafcd0c013b52935f78827f646c3b1b6d05735`. The
current rendered manifest and page-inspection manifest each contain 180
records, with 180/180 checksum-bound visual records validated against the
current PDF. The packet render paths and page numbers above are historical.

Unresolved blockers: none
