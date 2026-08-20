# Chapter 2 figure review

The seven native TikZ figures were compared against the full-resolution source
scans `pdf-070.jpg`, `pdf-077.jpg`, `pdf-084.jpg`, `pdf-085.jpg`,
`pdf-086.jpg`, `pdf-087.jpg`, and `pdf-091.jpg`.  Each figure is included at
the source position through its own file in `latex/figures/`.

- Figure 2-1, source PDF page 70: checked the vertical $z$ axis, three contour
  segments, arrow directions, intersections $a$ and $b$, and caption.
- Figure 2-2, source PDF page 77: checked the projected tube boundary, the
  paired endpoint configurations, dashed connecting path, transformed endpoint,
  labels, and full caption.
- Figure 2-3, source PDF page 84: checked the projected light-cone outlines,
  oblique planes $(\alpha)$ and $(\beta)$, three outgoing vectors, labels, and
  caption.
- Figure 2-4, source PDF page 85: checked the paired cones, vector orientations,
  primed and unprimed labels, and caption equations.
- Figure 2-5, source PDF page 86: checked the real-axis interval, domain
  boundaries, points $a$ and $b$, labels $D_1,D_2$, and caption punctuation.
- Figure 2-6, source PDF page 87: checked the nested upper and lower contour
  paths, arrow orientations, real-axis points, labels $C_1,C_2$, and caption.
- Figure 2-7, source PDF page 91: checked both axes and circles, mapped points,
  displayed mapping formula, labels, caption, and preserved the legacy reference
  label `fig:ch2-mobius-map`.

The isolated figure bundle compiled successfully with `pdflatex` and was
rendered to PNG for visual inspection.  The section files now input all seven
native reconstructions, and no pending figure placeholder remains.

Unresolved blockers: none
