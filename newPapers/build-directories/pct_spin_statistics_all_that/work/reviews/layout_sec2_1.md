# Layout review: Chapter 2, Section 2-1

## Scope

- File reviewed: `latex/chapters/chapter02/sec2_1.tex`
- Affected source marker: PDF 52, printed page 40, prose after Eq. (2-25)
- Affected native paragraph: lines 685--689 after the final reflow
- Affected rendered page: physical PDF page 41, native footer 37
- Source page inspected: `work/source-pages/pdf-052.jpg`

## Before

The full-build log recorded this warning in the paragraph containing the inline
identity `T(x_1,\ldots,x_n)=T(\xi_1,\ldots,\xi_{n-1})`:

```text
Overfull \\hbox (10.14317pt too wide) in paragraph at lines 685--689
```

The pre-edit rendered page placed the complete identity on one line. The right
edge extended past the text block by the amount reported in the log.

## Edit

The paragraph is enclosed in a local `sloppypar` environment. Every source
word, mathematical token, punctuation mark, equation tag, and `% PCT-SOURCE`
marker remains present. TeX now reflows the inline identity across the equality
sign when the line width requires it.

## After

The full manuscript draft was rebuilt with:

```text
./build_and_verify.sh --draft
```

The command exited with status 0 and produced `latex/master.pdf`. The log
segment from `sec2_1.tex` through the next chapter file contains no `Overfull
\\hbox` or `Underfull \\hbox` entry. The source and project audits passed.

The post-edit extraction from physical page 41 reads the identity as

```text
the equation T (x1 , . . . , xn ) =
T (ξ1 , . . . , ξn−1 ) and have solved the problem of finding all distributions
```

The rendered page keeps the paragraph inside the text block, retains Eq. (2-24),
Eq. (2-25), and Eq. (2-26), and carries the following prose without clipping.
The formula remains inline, as on the source page, while the discretionary
reflow keeps the equality and its two sides legible.

Unresolved blockers: none
