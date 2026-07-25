# Chapter 28 coverage manifest

## Source boundary

- Chapter: 28, *Supersymmetric Versions of the Standard Model*
- Source: `origPapers/weiberg_vol3.pdf`
- Physical PDF pages: 202--270 inclusive
- Printed pages: 179--247
- Chapter 29 begins on physical p. 271 and is excluded

Rendered source pages are authoritative. OCR is only an aid.

## Semantic ownership

| File | Content | Physical pages | Printed pages |
|---|---|---:|---:|
| `introduction.tex` | Chapter introduction before 28.1 | 202--203 | 179--180 |
| `sec281.tex` | 28.1 Superfields, Anomalies, and Conservation Laws | 203--211 | 180--188 |
| `sec282.tex` | 28.2 Supersymmetry and Strong-Electroweak Unification | 211--215 | 188--192 |
| `sec283.tex` | 28.3 Where is Supersymmetry Broken? | 215--221 | 192--198 |
| `sec284.tex` | 28.4 The Minimal Supersymmetric Standard Model | 221--232 | 198--209 |
| `sec285.tex` | 28.5 The Sector of Zero Baryon and Lepton Number | 232--243 | 209--220 |
| `sec286.tex` | 28.6 Gauge Mediation of Supersymmetry Breaking | 243--258 | 220--235 |
| `sec287.tex` | 28.7 Baryon and Lepton Non-Conservation | 258--263 | 235--240 |
| `backmatter.tex` | Problems and References | 263--270 | 240--247 |

Every physical page at a row boundary is read-only overlap for the
neighboring assignments. Text is owned by the visible heading boundary
and must occur exactly once.

## Expected numbered-equation coverage

- Section 28.1: (28.1.1)--(28.1.13)
- Section 28.2: (28.2.1)--(28.2.19)
- Section 28.3: (28.3.1)--(28.3.5)
- Section 28.4: (28.4.1)--(28.4.18)
- Section 28.5: (28.5.1)--(28.5.52)
- Section 28.6: (28.6.1)--(28.6.34)
- Section 28.7: (28.7.1)--(28.7.7)

Expected chapter total: 148 numbered equations. All unnumbered displays
must be inventoried during visual transcription.

## Expected visual inventory

- Table 28.1, physical p. 214, owned by section 28.2: electroweak mixing
  parameter and unification mass as functions of the number of minimal
  superfield doublets.
- Figure 28.1, physical p. 225, owned by section 28.4: one-loop
  supersymmetric contribution to a strangeness-changing effective
  interaction.
- Figure 28.2, physical p. 227, owned by section 28.4: corresponding
  one-loop standard-model weak contribution.
- Figure 28.3, physical p. 228, owned by section 28.4: the two one-loop
  diagrams for the charged-lepton radiative decay discussed in the
  surrounding text.
- Figure 28.4, physical p. 229, owned by section 28.4: one-loop
  contribution to the up-quark chromoelectric dipole moment.
- Figure 28.5, physical p. 244, owned by section 28.6: messenger-sector
  diagram that transmits supersymmetry breaking.
- Figure 28.6, physical p. 246, owned by section 28.6: the two diagram
  topologies communicating messenger-sector supersymmetry breaking to
  squarks and sleptons.
- Figure 28.7, physical p. 259, owned by section 28.7: tree-level
  exchange producing a four-fermion interaction among quarks and
  leptons.

All figures must be reconstructed as clean chapter-local TikZ/vector
graphics with the source topology, line styles, labels, panel order,
and complete captions. Expected numbered figures: seven. Expected
numbered tables: one.

## Other expected inventories

- Problems: 1--5, physical pp. 263--264.
- References: 1--45, physical pp. 264--270, including the lettered
  entries 1a, 1b, 4a--4d, 7a, 14a, 16a, 27a, 29a, 35a--35b, and 42a.
  Expected displayed reference entries: 59.
- Source footnotes: four, all converted to ordinary automatically
  numbered footnotes:
  - physical p. 203, the supersymmetry-breaking energy range and the
    photino/wino/bino mixing qualification;
  - physical p. 207, the value of
    \((-1)^{3(B-L)}\) for quark, lepton, and other superfields and the
    equivalence of the two definitions of \(R\) parity;
  - physical p. 236, the factor-of-two convention difference for the
    formula for \(m_Z^2\);
  - physical p. 245, the identification of the bino with the
    \(U(1)\) gauge field used in the standard model and the resulting
    effective-theory interpretation.
- Centered three-asterisk dividers: two. The physical p. 209 divider is
  owned by section 28.1 and separates the naturalness discussion from
  the relic-particle discussion. The physical p. 219 divider is owned
  by section 28.3 and separates the gravitino-mass discussion from the
  cosmological constraint.

## Continuity and high-risk checks

- Check all physical-page transitions listed in the ownership table,
  especially pp. 203, 211, 215, 221, 232, 243, 258, 263, and 264.
- Preserve every distinction among quarks, antiquarks, leptons,
  sleptons, squarks, gauginos, winos, binos, higgsinos, gluinos, and
  gravitinos; preserve all handedness, charge, color, flavor,
  generation, and superfield labels.
- Verify \(R\)-parity and \(B-L\) exponents, beta-function
  coefficients, unification normalizations, threshold scales,
  supersymmetry-breaking scales, mass matrices, mixing angles,
  eigenvalues, Yukawa and gauge couplings, CP phases, loop factors,
  group-theory traces, messenger indices, soft terms, and baryon- and
  lepton-number assignments directly from rendered pages.
- Preserve every dagger, star, transpose, bar, prime, sign, factor of
  \(i\), power of \(2\pi\), numerical bound, experimental value, unit,
  and confidence-level statement.
- OCR missed visible equation labels (28.1.1), (28.1.8), (28.1.9),
  (28.2.14), (28.2.15), (28.4.18), (28.5.1), (28.5.46),
  (28.5.51), and (28.6.29). Inspect the rendered source rather than
  inferring these equations from neighboring text.
- Every superscript source citation becomes a linked bracketed marker;
  none may be confused with the four source footnotes or the two
  typographic dividers.

## Completion record

- Complete transcription now covers every source passage on physical
  pp. 202--270 exactly once, from the chapter introduction through
  References. All seven section files, all seven chapter-local TikZ figures,
  Table 28.1, Problems 1--5, and all 59 displayed reference entries are
  present.
- The numbered-equation audit found exactly 148 `\tag` commands and 148
  matching stable labels: 13 equations in Section 28.1, 19 in 28.2, 5 in
  28.3, 18 in 28.4, 52 in 28.5, 34 in 28.6, and 7 in 28.7. The chapter also
  contains 29 source-faithful unnumbered display groups.
- Structural inventories agree with the rendered source: seven figures, one
  table, four ordinary numbered footnotes, two typographic dividers, five
  problems, and 59 displayed reference entries.
- Problems 1--5 and all 59 displayed reference entries (base
  References 1--45 and every lettered entry) are transcribed from
  physical pp. 263--270 with stable chapter-local labels and linked
  internal reference mentions. The eight-page isolated check compiled
  without undefined links or errors, and every content page passed
  full-resolution rendered inspection. Two harmless overfull boxes,
  at most 2.05 pt, remain under the 98-percent stop rule.
- Visibly printed source anomalies in the bibliography, including
  “E. Dudea” in Reference 1, “Phys. Rev. Lett. B436” in Reference 1,
  the period between B309 and 337 in Reference 12, the missing comma
  between B243 and 250 in Reference 24, and “R. Rattazi” in Reference
  32, are preserved rather than silently emended.
- The visibly printed Section 28.7 cross-reference to Eqs. (28.1.2) and
  (28.1.3), rather than the apparently intended Eqs. (28.1.4) and
  (28.1.5), is also preserved and recorded instead of silently corrected.
- The integrated chapter-only check compiled to 60 A4 pages including its
  check title page. All Chapter 28 labels and links resolve; six harmless
  overfull boxes remain, with a maximum excess of 4.59 pt. Every page was
  covered by contact-sheet inspection, and the corrected Section 28.7 and
  both of its joins were additionally inspected at full resolution. No
  clipping, overlap, malformed diagram, missing glyph, or visible placeholder
  was found.
- The complete-volume build also compiles with every Chapter 28-local link
  resolved. Its remaining undefined links are deliberate references to
  Volumes I and II or forward references in chapters still under
  transcription, not Chapter 28 defects.
