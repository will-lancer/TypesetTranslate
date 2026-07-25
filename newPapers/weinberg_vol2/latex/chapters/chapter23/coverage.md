# Chapter 23 coverage and QA

## Source boundary

Chapter 23, “Extended Field Configurations,” is transcribed from physical
pages 444--500 of `origPapers/weinberg_vol2.pdf` (printed pages 421--477).
The span begins with the chapter introduction on physical page 444 and ends
with Reference 40 on physical page 500. Appendix B ends and Problems begin on
physical page 496; that shared boundary was checked at high resolution.

## Content coverage

The chapter assembly includes:

- the introduction;
- Sections 23.1--23.8;
- Appendix A, “Euclidean Path Integrals”;
- Appendix B, “A List of Homotopy Groups”;
- six Problems; and
- forty linked References.

All 155 numbered equations and matching stable labels are present in strict
sequence:

- (23.1.1)--(23.1.10);
- (23.2.1)--(23.2.9);
- (23.3.1)--(23.3.25);
- (23.4.1)--(23.4.14);
- (23.5.1)--(23.5.26);
- (23.6.1)--(23.6.26);
- (23.7.1)--(23.7.4);
- (23.8.1)--(23.8.18); and
- (23.A.1)--(23.A.23).

The integrated inventory also contains 62 unnumbered display blocks, two
semantic footnotes, and two centered three-asterisk dividers. Chapter 23 has
no numbered figures or tables. Appendix B contains the complete unnumbered
homotopy-group catalog, and every reference entry owns a unique destination
from `ch23-ref-1` through `ch23-ref-40`.

## Integration and links

`latex/checks/chapter23.tex` supplies check-only destinations for the
twenty-four links that point outside Chapter 23. All chapter-internal section,
appendix, equation, and bibliography destinations resolve to their real
labels. Static comparison of the 162 used destinations against the 206 owned
destinations found exactly the expected twenty-four external links and no
missing internal target. No duplicate labels remain.

The isolated integrated build is:

```sh
cd newPapers/weinberg_vol2/latex
latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error \
  checks/chapter23.tex
```

The accepted build produces 49 A4 pages. Its final log contains no errors,
undefined or multiply defined references, duplicate destinations, overfull
boxes, or underfull boxes. The only package warning is the inherited
`hyperref` notice that the `pagecolor` option is no longer available.

## Rendered QA

Every one of the 49 output pages was rendered at 180 DPI in
`/private/tmp/ch23-integrated-qa.v6r2VQ/`. Six contact sheets covering pages
1--49 were inspected at original detail, including every section transition,
both appendix transitions, the Appendix B catalog, Problems, References, all
page edges, long displays, and both footnote regions. No clipping, collision,
overflow, blank content page, malformed glyph, or boundary leakage was found.

Mechanical audits confirmed the complete tag sequences, 155 matching
equation labels, 62 unnumbered displays, two footnotes, two dividers, six
Problems, forty References, and zero prohibited `\times` or `\mathscr`
commands in chapter content. `pdftotext -layout` confirmed every section
endpoint and both appendix/backmatter boundaries.

The stable export is `weinberg-vol2-chapter23.pdf`:

```text
SHA-256 06219afea3b0350517be2e12f4fbe29aa15aea75b6ee7d80d434a615a2a4ade8
```

The section-level reports in `reports/` record all scan-authoritative
typographical anomalies retained from the rendered source and the
high-resolution checks used to settle ambiguous readings.
