# Independent source review: Chapter 10 (re-review)

## Basis and coverage

I reviewed `banks-qft.pdf`, physical PDF pages 216--251, corresponding to printed pages 206--241. Each page was inspected in the 300 dpi source render at `/private/tmp/ch10-review/render-300/page-<n>.png`. Text extraction served as a locator; the rendered source controlled glyph readings.

All 36 physical pages were examined. The review covered chapter and section headings, prose, 23 numbered equations, 110 unnumbered display blocks, footnotes 1--10, citations, and Problems 10.1--10.5. Equation labels 10.1--10.23 are all present in the chapter files. The problems, their displays, source citations, and numbering are present. The source spelling differences listed below remain recorded as editorial changes.

## Verdict

**PASS after re-review.** The page-246 insertion and equation 10.16 correction now match the rendered source. The three spelling changes below are editorial corrections, not transcription failures.

## Findings

### P1: page 246 body of section 10.8, resolved

Source physical page 246, printed page 236, contains the opening body of “10.8 ’t Hooft--Polyakov monopoles.” It begins “We now skip to the case of most interest, the static ’t Hooft--Polyakov solutions...” and continues through the construction on the square, ending “With this definition, $g=1$ on the left, top, and”. It includes these three unnumbered displays:

```tex
\phi(t_1,t_2)=g(t_1,t_2)\phi_0,
D_i\phi=0,
g(t_1,t_2)=P e^{i\int_C A}.
```

The corrected transcription now includes the body at `newPapers/build-directories/banks_qft/latex/chapters/chapter10/sec10_7.tex:261-302`. The three display markers are at lines 269, 287, and 295. `sec10_8.tex:1-2` continues with “bottom boundaries of the square...”, matching the source page break. A fresh visual comparison confirms the prose and all three displays.

### P2: equation 10.16 derivative index, resolved

On source physical page 238, printed page 228, equation 10.16 visibly reads
`A_\mu=g_1^{-1}(\hat x)\partial_i g_1(\hat x)f(x^2).`
The corrected transcription has `\partial_i` at `newPapers/build-directories/banks_qft/latex/chapters/chapter10/sec10_6.tex:159-163`. The source glyph is a lower-case `i`, and the re-rendered source comparison agrees.

### Source spelling differences recorded for editorial review

- Source page 216 says “purse”; the transcription says “pursue” at `newPapers/build-directories/banks_qft/latex/chapters/chapter10/sec10_1.tex:10-12`.
- Source page 250 says “arbitary”; the transcription says “arbitrary” at `newPapers/build-directories/banks_qft/latex/chapters/chapter10/problems.tex:35`.
- Source page 251 says “Abrikosov--Nielson--Olesen”; the transcription says “Abrikosov--Nielsen--Olesen” at `newPapers/build-directories/banks_qft/latex/chapters/chapter10/problems.tex:93`.

The 300 dpi inspection left no unresolved glyph ambiguity. No source corrections were made during this review.
