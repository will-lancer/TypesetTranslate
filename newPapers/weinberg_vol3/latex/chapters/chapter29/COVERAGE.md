# Chapter 29 coverage manifest

## Source boundary

- Chapter: 29, *Beyond Perturbation Theory*
- Source: `origPapers/weiberg_vol3.pdf`
- Physical PDF pages: 271--329 inclusive
- Printed pages: 248--306
- Chapter 30 begins on physical p. 330 and is excluded

Rendered source pages are authoritative. OCR is only an aid.

## Semantic ownership

| File | Content | Physical pages | Printed pages |
|---|---|---:|---:|
| `introduction.tex` | Chapter introduction before 29.1 | 271 | 248 |
| `sec291.tex` | 29.1 General Aspects of Supersymmetry Breaking | 271--279 | 248--256 |
| `sec292.tex` | 29.2 Supersymmetry Current Sum Rules | 279--289 | 256--266 |
| `sec293.tex` | 29.3 Non-Perturbative Corrections to the Superpotential | 289--299 | 266--276 |
| `sec294.tex` | 29.4 Supersymmetry Breaking in Gauge Theories | 299--310 | 276--287 |
| `sec295.tex` | 29.5 The Seiberg-Witten Solution | 310--328 | 287--305 |
| `backmatter.tex` | Problems and References | 328--329 | 305--306 |

Every physical page at a row boundary is read-only overlap for the
neighboring assignments. Text is owned by the visible heading boundary
and must occur exactly once.

## Expected numbered-equation coverage

- Section 29.1: (29.1.1)--(29.1.10)
- Section 29.2: (29.2.1)--(29.2.51)
- Section 29.3: (29.3.1)--(29.3.38)
- Section 29.4: (29.4.1)--(29.4.23)
- Section 29.5: (29.5.1)--(29.5.87)

Expected chapter total: 209 numbered equations. All unnumbered displays
must be inventoried during visual transcription.

## Expected visual inventory

- Figure 29.1, physical p. 323, owned by section 29.5: deformation of
  a counterclockwise contour at large \(\lvert u\rvert\) into a contour
  based at \(P\) that circles the singularities at \(-u_0\) and
  \(+u_0\), in that order. Preserve both singularity points, the base
  point, the large outer contour, the narrow return paths, every
  orientation arrow, all labels, and the complete caption.

The figure must be reconstructed as a clean chapter-local TikZ/vector
graphic. Expected numbered figures: one. Expected numbered tables:
zero.

## Other expected inventories

- Problems: 1--3, physical p. 328.
- References: 1--12 plus 1a, thirteen displayed entries on physical
  pp. 328--329.
- Source footnotes: twelve, all converted to ordinary automatically
  numbered footnotes:
  - physical p. 281, the Lorentz-invariant goldstino-current matrix
    element and the CPT relations among its left- and right-handed
    coefficient functions;
  - physical p. 282, possible external-line poles in the non-goldstino
    part of a soft-goldstino emission amplitude;
  - physical p. 285, the corresponding Lorentz- and CPT-based relation
    between the coefficients \(N_L\) and \(N_R\);
  - physical p. 290, the factor 32 in Eq. (29.3.4), Majorana-gaugino
    state counting, and the gauge-generator normalization convention;
  - physical p. 297, the distinction among the several quantities
    denoted by \(C_2\) in the gauge and matter representations;
  - physical pp. 303 and 305--306, respectively, the definition and
    \(SU(3)\) example of a Cartan subalgebra, and Witten's observation
    about Weyl-invariant physical states with its continued invariant-
    tensor argument;
  - physical p. 310, the section 29.5 optional-reading note;
  - physical p. 314, the \(1/4\pi i\) normalization and the
    Seiberg--Witten prepotential;
  - physical p. 316, the meaning of the subscript \(D\) as “dual,” not
    a superfield \(D\)-term;
  - physical p. 321, the harmless additive constant in integrating
    \(h'(a)\) and its fixing by the \(Z_8\) symmetry;
  - physical p. 321, instanton-generated non-perturbative
    contributions to \(\beta(e)\).
- Centered three-asterisk dividers: one, on physical p. 287 in section
  29.2, after Eq. (29.2.39) and before the alternative derivation of
  the vacuum-energy relation.

## Continuity and high-risk checks

- Check all physical-page transitions listed in the ownership table,
  especially pp. 271, 279, 289, 299, 310, and 328.
- Section 29.5 is optional reading; its title asterisk must become an
  ordinary numbered section-title footnote with a safe moving
  argument.
- Verify supersymmetry-current normalization, vacuum-energy factors,
  box normalization, goldstino matrix elements, CPT phases, spectral
  functions, delta functions, current sum rules, and all one-particle
  state normalizations directly from rendered pages.
- Preserve every Witten-index sign and weight, regulator, anomaly
  coefficient, Wilsonian coupling, instanton factor, representation
  index, determinant, superpotential exponent, and group-theory
  normalization.
- Check the distinction between bare, running, and effective
  couplings; all \(R\)- and chiral-symmetry charges; dynamical scales;
  conditions for supersymmetry breaking; Cartan and Weyl group
  statements; and the continuation of the long Weyl-invariance
  footnote across physical pp. 305--306.
- In section 29.5 verify the \(N=2\) effective action, prepotential,
  duality transformations, electric and magnetic charges, central
  charge, monodromy matrices and their order, branch cuts, logarithms,
  singular points, asymptotic expansions, contour orientations, and
  all signs of square roots and imaginary parts. Preserve the
  distinctions among \(a\), \(a_D=h(a)\), \(u\), \(h\), and their
  Seiberg--Witten comparison functions.
- Preserve every dagger, star, transpose, bar, prime, sign, factor of
  \(i\), power of \(2\pi\), integration contour, branch choice,
  numerical coefficient, and exponent.
- OCR missed visible equation labels (29.2.29), (29.3.20),
  (29.3.22), (29.3.28)--(29.3.30), (29.4.3), (29.4.6),
  (29.4.10), (29.4.21), (29.5.61), (29.5.65), (29.5.81), and
  (29.5.82). Inspect the rendered source rather than inferring these
  equations from neighboring text.
- Every superscript source citation becomes a linked bracketed marker;
  none may be confused with the twelve source footnotes or the
  typographic divider.

## Completion record

- Problems 1--3 and References 1--12 plus 1a are transcribed from
  physical pp. 328--329, with thirteen stable chapter-local reference
  labels and linked internal reference mentions.
- The isolated backmatter check compiled in three passes without
  errors, unresolved links, or box warnings. Its two content pages
  passed full-resolution rendered inspection without clipping,
  overlap, malformed mathematics, or bad glyphs.
- The visibly printed forms “Nucl. Phys. B52, 1677 (1984)” in
  Reference 3 and “K. Intrilligator” in Reference 10 are preserved
  rather than silently emended.
- The chapter remains incomplete until sections 29.1--29.5, Figure
  29.1, and the complete integrated chapter are transcribed and
  verified.
