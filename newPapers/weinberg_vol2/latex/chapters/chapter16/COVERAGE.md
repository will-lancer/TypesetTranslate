# Chapter 16 coverage manifest

- Source: `origPapers/weinberg_vol2.pdf`; rendered physical PDF pages 86--102 are authoritative.
- Printed-page span: 63--79. Physical p. 86 begins Chapter 16; physical p. 103 begins Chapter 17 and is excluded.
- Introduction: physical p. 86 (printed p. 63), ending immediately before section 16.1.
- Section 16.1, “The Quantum Effective Action”: physical pp. 86--91 (printed pp. 63--68); equations (16.1.1)--(16.1.21), plus all unnumbered displays.
- Section 16.2, “Calculation of the Effective Potential”: physical pp. 91--95 (printed pp. 68--72); equations (16.2.1)--(16.2.16), plus all unnumbered displays.
- Section 16.3, “Energy Interpretation”: physical pp. 95--97 (printed pp. 72--74); equations (16.3.1)--(16.3.15), plus the unnumbered convexity display and other unnumbered displays.
- Section 16.4, “Symmetries of the Effective Action”: physical pp. 98--100 (printed pp. 75--77); equations (16.4.1)--(16.4.12), plus all unnumbered displays.
- Back matter: Problems 1--4 on physical p. 101 (printed p. 78); References 1--7 on physical pp. 101--102 (printed pp. 78--79). Reference 6 continues across the p. 101/102 boundary.
- Figure inventory: Figure 16.1 on physical p. 92 (printed p. 69), four diagrams in order: point-like zero-loop, one-loop circle, two-loop circle with internal chord, two-loop figure eight. One complete caption; no tables.
- Footnotes: two source symbolic notes, on physical pp. 87 and 92, to become ordinary automatically numbered footnotes.
- Superscript paper-reference markers found/expected: 1 (definition/history of the effective action), 2 (tree-graph argument), 3 (Coleman--Weinberg calculation), 4 (energy interpretation), 5 and 6 (convexity/effective-potential discussion), and 7 (Slavnov--Taylor identities). Convert each to a linked bracketed marker targeting reference labels `ch16-ref-1` through `ch16-ref-7`.
- Section-transition ownership: on physical p. 91, section 16.1 owns through the paragraph ending with the comparison to Eq. (10.3.15), and section 16.2 begins at its heading; on physical p. 95, section 16.2 owns through the paragraph explaining the fermionic determinant/sign, and section 16.3 begins at its heading.
- Page-boundary continuations to verify: Eq. (16.1.1) into p. 87 prose; connected-component discussion p. 87/88; effective-action discussion p. 88/89; loop-counting argument p. 89/90; shifted-action discussion p. 90/91; constant-field setup p. 91/92; one-loop determinant derivation p. 92/93; renormalization calculation p. 93/94; fermion contribution p. 94/95; constrained-energy derivation p. 95/96; convexity discussion p. 96/97; symmetry-measure derivation p. 98/99; linear/nonlinear and fermionic symmetry discussion p. 99/100; Reference 6 p. 101/102.
- Initial uncertainties requiring rendered-page inspection: exact signs and normalization in (16.1.1)--(16.1.21); whether the source uses `g` or another glyph for the loop-counting parameter; determinant powers and `i\epsilon` signs in (16.2.7)--(16.2.16); the contour-rotation direction; exact inequality sign in the convexity display and the following prose; chiral matrix in the section 16.4 fermion example; left/right derivative order and Grassmann signs in (16.4.10)--(16.4.12); Figure 16.1 line geometry; author spellings and journal data, especially Jona-Lasinio, Symanzik, Iliopoulos, O'Raifeartaigh, and the p. 102 continuation of Reference 6.

## Completion record

- All physical pages 86--102 are represented exactly once; the p. 91 and p. 95 section transitions were checked directly against the rendered source.
- Equation labels verified: 21 in section 16.1, 16 in section 16.2, 15 in section 16.3, and 12 in section 16.4; all unnumbered displays retained.
- Inventory verified: one TikZ figure, zero tables, four problems, seven linked inline citations, seven labeled references, and two ordinary footnotes.
- Chapter-only build: 16 pages, compiled with no unresolved references or duplicate anchors; every page rendered and visually inspected.
- Full-volume build: 71 pages at integration time; Chapter 16 occupies PDF pages 49--62 and every one of those pages was rendered and visually inspected.
- No Chapter 15 passage precedes the Chapter 16 opening and no Chapter 17 passage appears before the end of Chapter 16 references.
- Source-specific decisions: the visibly unsquared `\mu(\phi_0)` in (16.2.11) and the later literal word “nonpositive” in section 16.3 are preserved; the logical reference to the inverse relation is linked to (16.1.21).
- Deferred under the 98% stop rule: three chapter-only overfull-box warnings (26.0 pt, 4.2 pt, and 1.1 pt) have no visible clipping, collision, or unreadable content. The wider full-volume layout has only two small Chapter 16 warnings (10.0 pt and 4.6 pt), also visually harmless.
