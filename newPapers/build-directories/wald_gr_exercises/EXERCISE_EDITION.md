# Exercise-edition policy

Each chapter retains Wald's original problem section.  Three editorial
sections follow it:

1. solutions to Wald's numbered problems;
2. supplementary problems;
3. solutions to the supplementary problems.

Wald solutions use labels of the form `W.<chapter>.<problem>`.  Supplementary
items use `S.<chapter>.<problem>`.  The added prose follows the book's
signature, curvature, abstract-index, and units conventions.

The supplementary set contains one problem per chapter.  Thirteen are adapted
from the repository's Weinberg GR exercise edition.  Their local source paths
and inherited source labels appear in `exercise-source-ledger.json`.  The
Chapter 14 problem is an editorial bridge from Bogoliubov transformations to
particle creation.

This edition does not alter files in the canonical `wald_gr` tree.  Run
`python3 audit_exercises.py` to check counts, IDs, credits, placeholders, and
the canonical-content guard.
