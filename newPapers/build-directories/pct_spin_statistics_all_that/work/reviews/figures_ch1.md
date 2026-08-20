# Chapter 1 figure review

Source pages checked against the rendered canonical scan:

- PDF 23, printed page 11: Figure 1-1, Lorentz-group components, subgroup
  dashed regions, four component circles, labels, and source caption.
- PDF 25, printed page 13: Figure 1-2, four complex-Lorentz components,
  solid and dashed diagonal connectors, leader lines, labels, and source
  caption.
- PDF 38, printed page 26: Figure 1-3, spectral axes, vacuum point, mass
  curves, continuum hatching, legend, state labels, and source caption.

Native files:

- `latex/figures/fig1_1.tex`
- `latex/figures/fig1_2.tex`
- `latex/figures/fig1_3.tex`

Integration points:

- `chapters/chapter01/sec1_3.tex` inputs Figures 1-1 and 1-2 at the source
  positions following the relevant paragraphs.
- `chapters/chapter01/sec1_4.tex` inputs Figure 1-3 between the source
  paragraph that introduces the spectrum and its continuation.
- The Figure 1-3 reference and label both use `fig:1-3`.

Verification:

- A figure-only `pdflatex` build completed successfully.
- The resulting page was rendered with Poppler and inspected visually.
- All three captions remain source-faithful, with the metric notation in
  Figure 1-3 following the project Weinberg convention.

Unresolved blockers: none
