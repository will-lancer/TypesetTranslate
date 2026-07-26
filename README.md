# README

Typesetting old, beautiful physics and math books and papers into modern LaTeX.
The typesetting is done almost entirely via coding agents.
Please email me at will.m.lancer@gmail.com if you find any errors.

The repository has one canonical content tree:

- `newPapers/*.pdf`: polished delivery PDFs
- `newPapers/**/latex/`: the LaTeX source needed to reproduce them

Compile `master.tex` from the relevant `latex/` directory with `latexmk -pdf`;
the Witten project uses `wittenSUSYintro.tex` instead. The local `.sty` files
are required source dependencies and should remain beside the corresponding
documents.

Completed:
* Witten's *Introduction to Supersymmetry*
* Milnor's *Topology from the Differentiable Viewpoint*
    * Note on the above: I moved the exercises to immediately follow the chapter
      that tests their content instead of having them all at the end.
* Atiyah and MacDonald's *Introduction to Commutative Algebra*
    * I have an edited copy and an unedited one in the repo. The edited
      one adds more examples and pedagogy to the text.
* Weinberg's QFT: volumes I - III
