# Review of `missing_headings`

This review covers every item in `work/reviews/transcription_audit.json` at
the time of the audit. Each candidate was checked against the rendered source
image in `work/source-pages/` and the assembled native segment carrying the
same PDF-page marker. The OCR output supplies candidate text. The image
supplies the reading.

The dispositions use four classes: title metadata represented in `master.tex`,
present native heading or caption, formula OCR noise, and bibliography macro.
The review found zero source-proven omissions. The decimal punctuation on
Figure 2.4 remains a recorded source-map detail in `ERRATA.md`.

## Candidate dispositions

1. PDF 005, candidate `R.R STREATER`. The title-page image reads `R.F. STREATER`. The native title treatment in `latex/master.tex` uses `R. F. Streater`, and `latex/frontmatter/copyright.tex` retains the title-page initials. Classification: title metadata represented in `master.tex`; the `R.R` form is OCR noise.

2. PDF 005, candidate `A.S. WIGHTMAN`. The title-page image reads `A.S. WIGHTMAN`. The native title treatment in `latex/master.tex` uses `A. S. Wightman`, with the affiliation `Princeton University`. Classification: title metadata represented in `master.tex`.

3. PDF 009, candidate `Preface`. The source image carries the Preface heading and opening text. `latex/frontmatter/preface.tex` has `\section*{Preface}` and the PDF 009 source markers. Classification: present native heading.

4. PDF 021, candidate `1-8. THE LORENTZ AND POINCARE GROUPS`. The source image reads `1-3. THE LORENTZ AND POINCARÉ GROUPS`. `latex/chapters/chapter01/sec1_3.tex` begins with the PDF 021 marker and `\subsection{The Lorentz and Poincaré Groups}`. Classification: present native heading; the number and accent in the candidate are OCR noise.

5. PDF 021, candidate `(AM), = AMM,`. The source image places this fragment in the displayed Lorentz-group product relation (1-6). The display and the following equations are carried by the PDF 021 segments in `latex/chapters/chapter01/sec1_3.tex`. Classification: formula OCR noise.

6. PDF 023, candidate `FIGURE I-!. Connectivity properties of the Lorentz group, L, and its`. The source image shows Figure 1-1 and its caption beginning `Connectivity properties of the Lorentz group, L, and its subgroups`. `latex/figures/fig1_1.tex` contains the PDF 023 marker, native artwork, caption, and label. Classification: present native caption; `I-!` and truncation are OCR noise.

7. PDF 025, candidate `FIGURE I-2. Connectivity properties of the complex Lorentz group, L(C).` The source image shows Figure 1-2 with the complex Lorentz-group caption. `latex/figures/fig1_2.tex` contains the PDF 025 marker, caption, and label. Classification: present native caption; the Roman `I` is OCR noise.

8. PDF 029, candidate `(6,48) = (UG,AU®) = (8,0-*AU®) = (G,(U-*AU)*6),`. The source image shows the anti-unitary inner-product calculation immediately before (1-30). `latex/chapters/chapter01/sec1_3.tex` carries the PDF 029 display and the adjacent equation marker `id=1-30`. Classification: formula OCR noise.

9. PDF 029, candidate `AB= (U-!ABU)* = (U-1BU)*(U-1AU)* = BA, (1-31)`. The source image shows the anti-unitary product identity (1-31). The native display with `\widehat A\widehat B` and tag (1-31) is in `latex/chapters/chapter01/sec1_3.tex` under the PDF 029 marker. Classification: formula OCR noise.

10. PDF 038, candidate `FIGURE I-3. The spectrum of a theory of neutral scalar mesons of mass m`. The source image shows Figure 1-3 and the neutral-scalar-meson spectrum caption. `latex/figures/fig1_3.tex` contains the PDF 038 marker and the complete caption. Classification: present native caption; the figure-number glyph is OCR noise.

11. PDF 039, candidate `RELATION TO THE GENERAL ANALYSIS OF RELATIVISTIC INVARIANCET`. The source image shows the subheading `Relation to the General Analysis of Relativistic Invariance` with a dagger marker. `latex/chapters/chapter01/sec1_4.tex` has the PDF 039 heading marker, native `\subsubsection`, and footnote marker. Classification: present native heading; the trailing `T` is OCR noise.

12. PDF 052, candidate `T.N= T, (sco | dy 904X..%..%, ny)`. The source image shows the distribution formula (2-25) and its surrounding explanation. `latex/chapters/chapter02/sec2_1.tex` carries `PCT-SOURCE: pdf=52` with `id=2-25`. Classification: formula OCR noise.

13. PDF 056, candidate `FF = FF =1. (2-38)`. The source image shows the Fourier inverse identity (2-38). `latex/chapters/chapter02/sec2_2.tex` carries the PDF 056 display with `id=2-38`, tag (2-38), and the native identity. Classification: formula OCR noise.

14. PDF 057, candidate `(FA)G) = MF] (2-45)`. The source image shows the distributional pairing equation (2-45). `latex/chapters/chapter02/sec2_2.tex` carries the PDF 057 display with `id=2-45` and the native pairing formula. Classification: formula OCR noise.

15. PDF 058, candidate `FF =FF =\ (2-48)`. The source image shows the inverse-isomorphism identity (2-48) in Theorem 2-2. `latex/chapters/chapter02/sec2_2.tex` carries the PDF 058 display with `id=2-48`, tag (2-48), and the proof continuation. Classification: formula OCR noise.

16. PDF 070, candidate `FIGURE 2-1. The contour C in the plane of z = ¢ - iy.` The source image shows Figure 2-1, the contour, and the complex-plane caption. `latex/figures/fig2_1.tex` contains the PDF 070 marker, native contour drawing, caption, and label. Classification: present native caption; OCR substituted symbols in the formula.

17. PDF 077, candidate `FIGURE 2-2, The single-valuedness of the functions as defined throughout`. The source image shows Figure 2-2 and the caption beginning `The single-valuedness of the functions as defined throughout the extended tube`. `latex/figures/fig2_2.tex` contains the PDF 077 marker and full caption. Classification: present native caption; the comma and truncation are OCR noise.

18. PDF 084, candidate `FIGURE 2-3. The cone of space-like vectors corresponding to a Jost`. The source image shows Figure 2-3 and its Jost-point cone caption. `latex/figures/fig2_3.tex` contains the PDF 084 marker and complete native caption. Classification: present native caption; the candidate is a truncated OCR line.

19. PDF 085, candidate `FIGURE 2.4 A configuration of vectors f,-1, £5. )+1 appearing for a Jost`. The source image shows `FIGURE 2.4` and the configuration of the three Jost-point vectors. `latex/figures/fig2_4.tex` carries the PDF 085 marker, native drawing, visible decimal figure number, caption, and semantic label `fig:2-4`. Classification: present native caption; OCR substituted vector glyphs and dropped punctuation. The source-specific decimal is recorded in `ERRATA.md`.

20. PDF 086, candidate `FIGURE 2-5. Domains D, and Dz, of definition of F, and F2, respectively.` The source image shows Figure 2-5 with domains (D_1,D_2) and functions (F_1,F_2). `latex/figures/fig2_5.tex` contains the PDF 086 marker and complete caption. Classification: present native caption; subscripts are OCR noise.

21. PDF 087, candidate `FIGURE 2-6. The contours C, and C2.` The source image shows Figure 2-6 with contours (C_1) and (C_2). `latex/figures/fig2_6.tex` contains the PDF 087 marker and caption. Classification: present native caption; subscript loss is OCR noise.

22. PDF 091, candidate `FIGURE 2-7. Illustration of the mapping w = (u + z)/(1 + uz). Aszruns`. The source image shows Figure 2-7 and the mapping caption continuing with the unit-circle description. `latex/figures/fig2_7.tex` contains the PDF 091 marker and complete caption. Classification: present native caption; the missing word space and truncation are OCR noise.

23. PDF 100, candidate `KO, P},{P,, AD,}) = (®, ®,) + (¥, AD) = 0`. The source image shows the first graph-orthogonality condition in the adjoint-operator discussion. `latex/chapters/chapter02/sec2_6.tex` carries the PDF 100 display marker `id=2-6-orthogonal-condition-one` and its companion condition. Classification: formula OCR noise.

24. PDF 105, candidate `BIBLIOGRAPHY`. The source image shows the Chapter 2 bibliography heading and entries. `latex/chapters/chapter02/bibliography.tex` carries the PDF 105 bibliography-heading marker, `\chapterbibliography`, and the native `thebibliography` list. Classification: bibliography macro.

25. PDF 114, candidate `KH = SH = Z%,`. The source image shows the Asymptotic Completeness display under axiom IV, followed by the Section 3-2 heading. `latex/chapters/chapter03/sec3_1.tex` carries the PDF 114 axiom and display markers, while `sec3_2.tex` carries the native Section 3-2 heading on the same PDF page. Classification: formula OCR noise.

26. PDF 115, candidate `{GO, GYD, GH, } (3-10)`. The source image shows the sequence of (n)-particle components in equation (3-10). `latex/chapters/chapter03/sec3_2.tex` carries the PDF 115 marker `id=3-10`, tag (3-10), and the native sequence. Classification: formula OCR noise.

27. PDF 144, candidate `BIBLIOGRAPHY`. The source image shows the Chapter 3 bibliography heading and entries. `latex/chapters/chapter03/bibliography.tex` carries the PDF 144 bibliography-heading marker, `\chapterbibliography`, and the native reference list. Classification: bibliography macro.

28. PDF 151, candidate `(Y, T*®) = (TY, ©) = (TP, &) = (P'T%, ®) = 0 (4-12)`. The source image shows equation (4-12) in the proof of Theorem 4-3. `latex/chapters/chapter04/sec4_2.tex` carries the PDF 151 display marker `id=eq-ch4-12`, the native inner products, and tag (4-12). Classification: formula OCR noise.

29. PDF 152, candidate `CE, = EC. (4-14)`. The source image shows the commutation relation (CE_0=E_0C) as equation (4-14). `latex/chapters/chapter04/sec4_2.tex` carries the PDF 152 display marker `id=eq-ch4-14` and tag (4-14). Classification: formula OCR noise.

30. PDF 187, candidate `BIBLIOGRAPHY`. The source image shows the Chapter 4 bibliography heading and its interleaved prose and entries. `latex/chapters/chapter04/bibliography.tex` carries the PDF 187 heading marker and `\chapterbibliography`. Classification: bibliography macro.

31. PDF 196, candidate `Figure A.1. The dependence domain of the region where g = 1.` The source image shows Figure A.1 and the dependence-domain caption. `latex/figures/figA1.tex` carries the PDF 196 marker, native diagram, caption, and label. Classification: present native caption.

32. PDF 200, candidate `Figure A.2. Phase diagram of the Ising ferromagnet (nearest-neighbor interaction).` The source image shows Figure A.2 and the phase-diagram caption. `latex/figures/figA2.tex` carries the PDF 200 marker, native diagram, caption, and label. Classification: present native caption.

33. PDF 200, candidate `BE(ATY")`. The source image places this OCR fragment in the Ising and λ\(\varphi^4\) formula discussion around Figure A.2. `latex/appendix/constructive.tex` carries the corresponding native prose and formula at the PDF 200 markers, including the β--B and \(\mathcal{P}(\varphi)\) expressions. Classification: formula OCR noise.

34. PDF 210, candidate `Figure A.3, Behavior of (p(z)) as a function of space coordinate for some typical states`. The source image shows Figure A.3 and its state-profile caption. `latex/figures/figA3.tex` carries the native figure, full caption, and PDF 210 marker through `latex/appendix/local-algebras.tex`. Classification: present native caption; punctuation and symbol substitutions are OCR noise.

35. PDF 211, candidate `BIBLIOGRAPHY`. The source image shows the Appendix bibliography heading followed by its first entries. `latex/appendix/bibliography.tex` carries the PDF 211 heading marker, `\chapterbibliography`, and the native reference list. Classification: bibliography macro.

36. PDF 212, candidate `U.S.A., 57, 1178-1183 (1967); IIT: "Properties of the C* Dynamics for`. The source image shows a continuation of bibliography item 18. `latex/appendix/bibliography.tex` carries the PDF 212 bibliography markers and the complete item, including `Proc. Nat. Acad. Sci. U.S.A.`, pages 1178--1183, and the `C^*` title. Classification: bibliography macro; the candidate is OCR residue from an entry continuation.

## Review result

All 36 candidates have an image-backed disposition. Native headings, captions,
formula displays, title metadata, and bibliography blocks are present in the
assembled source files. The strict companion manifest at
`work/reviews/transcription_audit_reviewed.json` records the exact candidate
set and requires each item to carry a resolved disposition. A strict audit
fails when the machine-produced candidate set changes without a corresponding
review update.

Unresolved blockers: none
