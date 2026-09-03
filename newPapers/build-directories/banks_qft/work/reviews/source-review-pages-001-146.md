# Independent source review: physical PDF pages 1--146

## Basis and method

The authority was `/Users/wlancer/Coding_Projects/TypesetTranslate/newPapers/build-directories/banks_qft/banks-qft.pdf`, verified at 281 pages with SHA-256
`31de7827e7bc636feaa7028fe4dbb63a718b3926ee43ff3d96d91185a44eafe3`. I inspected all 146 source pages in the shared 150 dpi render at `/private/tmp/banks-qft-shared-01a063b0/source-render-150dpi/page-<n>.png`. I rebuilt the final native transcription in isolation from `latex/transcription-check.tex` at `/private/tmp/banks-final-re-review-3/transcription-check.pdf`, which has 266 A4 pages and SHA-256 `1b7129fab8c53ce9b20c3bc717753dc40f6608daf3a454e5b805bc2029e55ce4`. Text extraction located passages, and rendered source pages controlled readings of mathematics and figures. The changed contexts were re-rendered at native pages 7, 9, 14, 23, 62, 92, and 117.

The source body mapping is physical pages 11--146 to printed pages 1--136. Reflow makes the corresponding native body span 131 A4 pages, native pages 6--136. Source markers cover every body page: 136 unique pages in the range, with 466 chapter source markers. The range has 113 equation-kind markers, comprising 111 numbered equation markers and two intentionally idless equation markers. Editorial hooks were ignored as instructed.

`verify_source.py` and the non-strict base `audit_project.py` both pass. The page-level audit was supplemented by the per-equation marker count and the rendered checks below.

## Disposition and page coverage

All 146 physical pages were reviewed.

| Physical pages | Disposition or content | Result |
|---|---|---|
| 1--4, 6, 10 | Cover, blanks, publisher description, and imprint | Omitted as recorded |
| 5, 7--9 | Native title and regenerated contents | Generated |
| 11--17 | Chapter 1 | Native body present; native pages 6--11 |
| 18--26 | Chapter 2 | Native body present; native pages 12--20 |
| 27--47 | Chapter 3 | Native body present; native pages 21--40 |
| 48--53 | Chapter 4 | Native body present; native pages 41--45 |
| 54--71 | Chapter 5 | Native body present; native pages 46--63 |
| 72--85 | Chapter 6 | Native body present; native pages 64--77 |
| 86--102 | Chapter 7 | Native body present; native pages 78--94 |
| 103--146 | Chapter 8 | Native body present; native pages 95--136 |

The chapter, section, subsection, prose, problem, display, and page-boundary sequence follows the rendered source throughout the range. The corrected Chapter 2 boundary was rechecked on source p.20 and native p.14. References and both indices begin after this range. No reference or index page is included in physical pages 1--146.

## Inventory counts

- Numbered equations: 111, with complete labels `1.1`--`1.4`, `2.1`--`2.20`, `3.1`--`3.44`, `4.1`--`4.2`, `5.1`--`5.9`, `6.1`--`6.18`, `7.1`--`7.9`, and `8.1`--`8.5`. The labels are unique, and all 111 numbered labels now have source-unit markers. Two additional source-marked equation displays are intentionally idless.
- Unnumbered display environments in the chapter TeX inventory: 353. Rendered source comparison found no omitted mathematical display.
- Numbered figures: 12 of the 23 total inventory figures occur in this range. All are present: `1.1` (p.14), `1.2` (p.16), `3.1` (p.40), `6.1` (p.74), `6.2` and `6.3` (p.76), `6.4` (p.80), `7.1` and `7.2` (p.93), and `8.1` (p.110), `8.2` (p.116), `8.3` (p.119).
- Unnumbered diagram-like figures: three are visible in the source range, at p.52, p.69, and p.73. All three are now listed in `unnumbered-diagrams.json`; the full inventory count is 14. Their source markers and rendered figures were rechecked.
- Explicit problems: 65 statements, distributed as Ch. 2: 11, Ch. 3: 6, Ch. 4: 4, Ch. 5: 16, Ch. 6: 7, Ch. 7: 6, and Ch. 8: 15. Fifty are starred. The cross-page continuation of Problem 7.5 is marked at p.102. All problem IDs and star states agree with `explicit-problems.json`.
- Footnotes: 68 `\footnote` entries occur in Chapters 1--8. Their resets, text, and placement were checked in the rendered pages.
- Citations: 80 `\cite` commands reference 134 keys, with 110 unique keys. Every used key is defined in `latex/backmatter/references.tex`.

## Verdict

**PASS after re-review.** The source text and displayed mathematics are present across the declared range. All reviewed findings are resolved in the final source tree, and the changed contexts are present in the fresh native build.

## Re-review findings

### R-001 [RESOLVED] E-001 adopted correction

Source physical p.12, printed p.2, reads “Appendix G” in the introductory prose at `latex/chapters/chapter01/sec1_1.tex:85`. `ERRATA.md:4-7` adopts “Appendix E”. The final source uses the adopted form at that location and at the second source occurrence, physical p.14, printed p.4, at `latex/chapters/chapter01/sec1_2.tex:49`. Fresh native p.7 and p.9 render “Appendix E”. The source reading remains recorded as G; the E form is the intentional erratum, and the second occurrence is harmonized with the adopted destination.

### R-002 [RESOLVED] Chapter 2 heading boundary

Source physical p.18, printed p.8, continues the Fock-space discussion without a subsection heading. Source p.20, printed p.10, begins the single heading “2.1 Local fields”. The final transcription has prose at `latex/chapters/chapter02/sec2_1.tex:1-7` and the sole section marker and heading at `latex/chapters/chapter02/sec2_1.tex:134-135`. Fresh native p.12 has no premature heading, and fresh native p.14 has one `2.1 Local fields` heading.

### R-003 [RESOLVED] Equation (8.5) source-unit marker

Source physical p.126, printed p.116, contains numbered equation (8.5) immediately after the opening prose of Section 8.7. The final transcription places `% BANKS-SOURCE: pdf=126 print=116 kind=equation id=8.5` at `latex/chapters/chapter08/sec8_7.tex:8`, followed by the equation and label at lines 9--12. Fresh native p.117 renders the equation as (8.5). All 111 numbered equation labels now have markers.

### R-004 [RESOLVED] Unnumbered diagram inventory

The source p.52 massive-photon-propagator figure is present through `latex/chapters/chapter04/sec4_3.tex:109-115` and `latex/figures/chapter04-massive-photon-propagator.tex:1-7`. The matching inventory entry is now at `unnumbered-diagrams.json:3-8`. The range entries at p.69 and p.73 remain present, giving three source-range entries and 14 total entries.

### R-005 [RESOLVED] E-028 adopted correction to Equation (3.9)

Source physical p.30, printed p.20, shows `+[J(x)]` inside the source equation's outer minus sign. `ERRATA.md:235-243` adopts the sign `-[V'(delta/(i delta J)) - J] Z[J]` for the `+i` source functional. The final source at `latex/chapters/chapter03/opening.tex:195-200` uses the adopted `-J(x)` form, and fresh native p.23 renders Equation (3.9) with that form. This is an intentional adopted erratum.

### R-006 [RESOLVED] E-029 adopted correction to Problem 5.3

Source physical p.69, printed p.59, shows the time-reversal image of `a^dagger(p,s)` as undaggered `a(-p,-s)`. `ERRATA.md:245-252` adopts `a^dagger(-p,-s)`. The final source at `latex/chapters/chapter05/problems.tex:29-39` and fresh native p.62 use the adopted creation operator. This is an intentional adopted erratum.

### R-007 [RESOLVED] E-030 adopted correction to Problem 7.2

Source physical p.100, printed p.90, shows `1/sqrt(-g)` in the Hilbert stress-tensor definition. `ERRATA.md:254-262` adopts `2/sqrt(-g)`. The final source marker is at `latex/chapters/chapter07/problems.tex:21`, with the adopted factor 2 at line 41, and fresh native p.92 renders `2/sqrt(-g)` in Problem 7.2. This is an intentional adopted erratum.

## Corrected errata confirmed in this range

The following adopted forms agree with the rendered source context and the current TeX. E-001 is an intentional adopted correction whose source page retains the original “Appendix G” wording.

- E-001: adopted `Appendix E` at `latex/chapters/chapter01/sec1_1.tex:85` for source physical p.12, with the harmonized second occurrence at `latex/chapters/chapter01/sec1_2.tex:49` on source p.14; the source wording is `Appendix G`.

- E-003: `\ee^{\ii H_0t}...\ee^{-\ii H_0t_0}` at `latex/chapters/chapter02/problems.tex:16`.
- E-004: “four or greater” at `latex/chapters/chapter02/problems.tex:40`.
- E-005: the `-\ii/2` source-functional exponent at `latex/chapters/chapter02/problems.tex:115-119`.
- E-006: spatial `\delta^3` source profile at `latex/chapters/chapter02/problems.tex:123-125`.
- E-011 and E-012: `Lagrangian` at `latex/chapters/chapter07/problems.tex:7` and `(\partial_\mu G)^2` in equation (7.3) at `latex/chapters/chapter07/sec7_4.tex:55-60`.
- E-013 and E-014: `D(x-y)` at `latex/chapters/chapter08/sec8_5.tex:103-106` and `Froggatt--Nielsen` at `latex/chapters/chapter08/sec8_6.tex:147`.
- E-017 and E-018: `Problem 2.8` at `latex/chapters/chapter04/sec4_1.tex:9` and “general complex symmetric matrix” at `latex/chapters/chapter05/sec5_1.tex:246`.
- E-019 and E-020: the positive spatial components for `K_+` at `latex/figures/chapter06-fig6.3.tex:4-5`, and `unambiguous` at `latex/chapters/chapter06/sec6_4.tex:134`.
- E-021: the final outgoing-field index `\Phi(y_n)` at `latex/chapters/chapter03/sec3_7.tex:151-154`.
- E-028: adopted `-J(x)` in Equation (3.9) at `latex/chapters/chapter03/opening.tex:195-200`; source p.30 has `+J(x)`.
- E-029: adopted `a^\dagger(-p,-s)` in Problem 5.3 at `latex/chapters/chapter05/problems.tex:29-39`; source p.69 has undaggered `a(-p,-s)`.
- E-030: adopted `2/\sqrt{-g}` in Problem 7.2 at `latex/chapters/chapter07/problems.tex:41` under the marker at line 21; source p.100 has `1/\sqrt{-g}`.

## Remaining ambiguity

The source PDF's text layer corrupts some custom mathematical glyphs and ligatures. The rendered source pages resolved the readings used here. Native page reflow changes physical-page correspondence after transcription, so the native page ranges above are coverage ranges rather than page-for-page facsimiles. The isolated build emitted inherited underfull-box, hyperref PDF-string, and one 0.7366pt overfull-vbox diagnostic on later pages; the changed pages rendered cleanly, and these diagnostics do not affect this source-faithfulness scope. No unresolved content reading remains in physical pages 1--146.

FINAL STATUS: PASS
