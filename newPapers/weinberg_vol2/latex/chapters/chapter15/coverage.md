# Chapter 15 coverage manifest

Source: `origPapers/weinberg_vol2.pdf`, physical PDF pages 24--85 inclusive,
printed pages 1--62. Chapter 15 starts on physical page 24. Chapter 16 starts
on physical page 86 and is excluded. Rendered pages are authoritative; OCR is
only an aid.

## Semantic ownership and expected numbered equations

| File | Material | Physical pages | Printed pages | Expected equations |
|---|---|---:|---:|---|
| `introduction.tex` | Chapter introduction | 24--25 | 1--2 | none |
| `sec151.tex` | 15.1 Gauge Invariance | 25--29 | 2--6 | 15.1.1--15.1.19 |
| `sec152.tex` | 15.2 Gauge Theory Lagrangians and Simple Lie Groups | 30--35 | 7--12 | 15.2.1--15.2.9 |
| `sec153.tex` | 15.3 Field Equations and Conservation Laws | 35--37 | 12--14 | 15.3.1--15.3.10 |
| `sec154.tex` | 15.4 Quantization | 37--41 | 14--18 | 15.4.1--15.4.17 |
| `sec155.tex` | 15.5 The De Witt--Faddeev--Popov Method | 42--47 | 19--24 | 15.5.1--15.5.27 |
| `sec156.tex` | 15.6 Ghosts | 47--50 | 24--27 | 15.6.1--15.6.16 |
| `sec157.tex` | 15.7 BRST Symmetry | 50--59 | 27--36 | 15.7.1--15.7.40 |
| `sec158.tex` | 15.8 Generalizations of BRST Symmetry | 59--64 | 36--41 | 15.8.1--15.8.21 |
| `sec159.tex` | 15.9 The Batalin--Vilkovisky Formalism | 65--73 | 42--50 | 15.9.1--15.9.36 |
| `appendixA.tex` | Appendix A: A Theorem Regarding Lie Algebras | 73--77 | 50--54 | 15.A.1--15.A.14 |
| `appendixB.tex` | Appendix B: The Cartan Catalog | 77--81 | 54--58 | all unnumbered displays |
| `backmatter.tex` | Problems and References | 81--85 | 58--62 | Problems 1--9; references 1--26 plus 11a and 13a |

## Shared transition pages and semantic ownership

- Physical 35 / printed 12: Section 15.2 ends at (15.2.9); Section 15.3 owns its heading and all following material.
- Physical 37 / printed 14: Section 15.3 ends at (15.3.10); Section 15.4 owns its heading and all following material.
- Physical 47 / printed 24: Section 15.5 ends at (15.5.27); Section 15.6 owns its heading and all following material.
- Physical 50 / printed 27: Section 15.6 ends at (15.6.16); Section 15.7 owns its heading and all following material.
- Physical 59 / printed 36: Section 15.7 ends at (15.7.40); Section 15.8 owns its heading, numbered optional-reading footnote, and all following material.
- Physical 73 / printed 50: Section 15.9 ends at (15.9.36) and its final footnote; Appendix A owns its heading and statements a--c onward.
- Physical 77 / printed 54: Appendix A ends at (15.A.14); Appendix B owns its heading and the Cartan catalog onward.
- Physical 81 / printed 58: Appendix B ends after the catalog/isomorphism discussion; back matter owns `Problems` and everything following.
- Physical 82 / printed 59: Problem 9 ends before the `References` heading; the reference list owns the heading and all following material.

## Required inventories

- Figures: 0. Numbered tables: 0. Appendices: 2.
- Problems: 9.
- References: 28 displayed entries: 1--26, including 11a and 13a.
- Section-title optional-reading notes: Section 15.8 (physical 59) and Section 15.9 (physical 65), both converted to ordinary numbered footnotes.
- Footnotes: 21 ordinary automatic footnotes: 4 across the introduction and
  Sections 15.1--15.3; 1 in Section 15.4; 4 each in Sections 15.7 and 15.8;
  6 in Section 15.9; and 2 in Appendix A. This count includes the optional-reading
  notes in the titles of Sections 15.8 and 15.9.
- Three-asterisk internal dividers: 3, on physical pages 29, 41, and 59. They
  are centered typographic breaks, not footnote markers.

## Page-boundary continuity ledger

Every boundary 24/25 through 84/85 requires a direct rendered-page join check.
The shared semantic transitions are listed above. All other boundaries are
continuations owned by the same semantic file, except 41/42 (15.4/15.5), 64/65
(15.8/15.9), and 82's Problems/References transition, which begin on a new
physical page or at the explicit heading. Owners record split sentences,
equations, footnotes, lists, and reference entries in their completion notes;
the integrator checks every adjacent join exactly once.

## Initial uncertainties to resolve from rendered pages

- OCR corrupts many Greek letters, calligraphic symbols, fractions, primes,
  left/right functional derivatives, and equation punctuation.
- Physical 28 contains a badly interleaved OCR rendering around (15.1.18).
- Physical 63 contains an OCR artifact resembling `*A 6`; verify the actual
  mathematical symbol from the image.
- Physical 67 onward requires strict separation of BV antifields
  (`\ddagger`) from complex conjugation (`*`) and Hermitian adjoints
  (`\dagger`).
- Appendix B's catalog displays are unnumbered and must be inventoried from
  the rendered pages rather than inferred from extracted text.
- Reference typography and page ranges on physical 82--85 require image-level
  verification, especially 11a, 13a, and the long entries spanning pages.

## Completion record

Completed 2026-07-19.

- Agent assignment 1: introduction and Sections 15.1--15.3 (physical 24--37),
  followed by Appendix B (physical 77--81).
- Agent assignment 2: Sections 15.4--15.6 (physical 37--50), followed by an
  independent scan-to-LaTeX QA pass over Sections 15.7--15.9 and both appendices.
- Agent assignment 3: Sections 15.7--15.8 (physical 50--64), Appendix A
  (physical 73--77), and Problems/References (physical 81--85), followed by an
  independent QA pass over the introduction and Sections 15.1--15.6.
- The integrator transcribed Section 15.9 (physical 65--73), assembled the
  chapter, reconciled notation, and performed structural and visual QA.

All equation ranges in the ownership table are present exactly once, with
explicit tags and stable labels. Appendix B contains 23 unnumbered displays.
The final inventories are 21 footnotes, 3 internal dividers, 9 problems, and
28 displayed references. Every adjacent source-page join from 24/25 through
84/85 was checked, including all shared transition pages listed above.

Each semantic file compiled and rendered independently. Two cross-assignment
QA passes compared the complete chapter to the source scans. The integrated
chapter check builds as a 54-page A4 PDF and was inspected in full; no material
clipping, overlap, malformed glyphs, missing text, unresolved references, or
equation-number defects remain. Four small line-width warnings are visually
harmless and do not clip content.

Source anomalies deliberately preserved rather than silently corrected:

- Section 15.8 refers to the general BRST-invariant action as (15.8.3).
- Problem 9 prints `(O,S)=i\Delta S`.
- Problem 3 uses `f_\alpha f_\alpha` in its electrodynamics parenthesis.
- Reference 26 ends its title with “Continue.”
