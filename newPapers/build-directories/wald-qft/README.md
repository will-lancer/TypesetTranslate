# Wald: Quantum Field Theory in Curved Spacetime and Black Hole Thermodynamics

A 159-page reading edition of Robert M. Wald’s 1994 book, with standardized
notation, clickable references, and seven figures drawn in TikZ.

[Read the PDF](../../wald-qft/wald-qft-jhep.pdf) or download the
[LaTeX and original-scan bundle](../../wald-qft/wald-qft-latex-and-source.zip).
The bundle also retains the raw OCR text and the detailed review notes.

## Build

From `latex/`, run:

```sh
latexmk -xelatex master.tex
```

Alternatively, run `xelatex -interaction=nonstopmode -halt-on-error master.tex`
twice. Keep `jheppub.sty` and the `figures/` directory beside `master.tex`.
The document uses Latin Modern fonts and the packages named in its preamble.

## Edition

Hilbert and Fock spaces use calligraphic notation. Vectors use bold letters,
and in/out subscripts are upright. Equation-reference numbers are blue;
their parentheses remain black. Simple expressions use ordinary-size
delimiters, with automatic sizing retained for tall contents.

The review checked the displayed equations throughout the book and compared
all seven diagrams against the scan. Targeted scan comparisons repaired OCR
damage in formulas and prose. This is a reviewed OCR edition; the original
scan is provided in the bundle for reference.

The final build has 356 equation labels and 1,229 internal links with valid
destinations. It reports no overfull boxes, undefined references, missing
characters, or font warnings. See `review-checks.json` for the recorded checks.

The original work is copyright 1994 by The University of Chicago.
