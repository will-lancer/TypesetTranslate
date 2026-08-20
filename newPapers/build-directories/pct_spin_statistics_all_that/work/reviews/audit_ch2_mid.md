# Independent Chapter 2 mid-section audit

PASS:

INPUT SNAPSHOT:

- Canonical source: `../../../origPapers/pct_spin_statistics_all_that.pdf`, SHA-256 `44fadba731cafe7f009d4e561372febb3597e1f2a4819346ce2efd16befcb889`.
- Source images checked at original resolution: `work/source-pages/pdf-059.jpg` through `work/source-pages/pdf-095.jpg`.
- Native section files: `latex/chapters/chapter02/sec2_3.tex`, `latex/chapters/chapter02/sec2_4.tex`, and `latex/chapters/chapter02/sec2_5.tex`.
- Native figure files: `latex/figures/fig2_1.tex` through `latex/figures/fig2_7.tex`.
- Printed pages 47 to 83 correspond to PDF pages 059 to 095. The audit covered all 37 pages.
- The binding rules are `NOTATION.md`, `SOURCE_MAP.md`, and the Weinberg guide named there. The source image controls printed wording, signs, glyphs, labels, captions, and placement. Authorized notation changes follow the house mostly-plus metric and script-letter rules.

FULL SCOPE READ:

Every page was compared against the native transcription. The comparison included prose, section boundaries, equation tags, unnumbered displays, theorem and proof text, remarks, lemma text, footnotes, citations, source markers, figure captions, figure labels, and figure placement.

| PDF | Print | Scope checked |
|---:|---:|---|
| 059 | 47 | Section 2-2 tail, equations (2-49) through (2-52), Theorem 2-3, Section 2-3 opening, equations (2-53) and (2-54). |
| 060 | 48 | Holomorphic definition, dagger footnote, equations (2-55) through (2-57). |
| 061 | 49 | Equations (2-58) and (2-59), surrounding prose. |
| 062 | 50 | Equation (2-60), Lorentz representations, matrix and antisymmetry displays. |
| 063 | 51 | Theorem 2-4, unnumbered Remark, proof opening. |
| 064 | 52 | Equation (2-61), Cauchy smearing, equations (2-62) and (2-63). |
| 065 | 53 | Theorem 2-5, proof, equation (2-64), Theorem 2-6 opening. |
| 066 | 54 | Theorem 2-6 continuation, equations (2-65) through (2-67), unnumbered Remark, proof opening. |
| 067 | 55 | Equations (2-68) through (2-70). |
| 068 | 56 | Strict inequality in equation (2-71), Cauchy-Riemann calculation. |
| 069 | 57 | Equations (2-73) through (2-75), Figure 2-1 lead-in. |
| 070 | 58 | Figure 2-1, proof continuation, equation (2-76). |
| 071 | 59 | Theorem 2-7, equation (2-77), future-cone definition and closure. |
| 072 | 60 | Theorem 2-8, equation (2-78), proof and Reed--Simon citation. |
| 073 | 61 | Theorem 2-9, equation (2-79), Theorem 2-10 opening. |
| 074 | 62 | Equations (2-80) through (2-83). |
| 075 | 63 | Theorem 2-10 proof end, Section 2-4 heading, equation (2-84). |
| 076 | 64 | Equation (2-85), transformation-law continuation. |
| 077 | 65 | Equation (2-86), unnumbered Lemma, Figure 2-2. |
| 078 | 66 | Lemma continuation, Theorem 2-11, proof. |
| 079 | 67 | Jordan forms, equations (2-87) through (2-90), Halmos dagger footnote. |
| 080 | 68 | Cone criterion, matrix calculation, component formulas. |
| 081 | 69 | Completion of the matrix argument and positivity of the two components. |
| 082 | 70 | Real points, equation (2-91), Jost-point criterion and equation (2-92). |
| 083 | 71 | Jost proof, convex-separation dagger footnote, Figure 2-3 lead-in. |
| 084 | 72 | Figure 2-3, non-continuation example, permuted-tube setup. |
| 085 | 73 | Equation (2-93), common real environment, Figure 2.4. |
| 086 | 74 | Section 2-5 heading, Theorem 2-13, equations (2-94) and (2-95), boundary match, Remark, Figure 2-5. |
| 087 | 75 | Figure 2-6 and Theorem 2-13 proof. |
| 088 | 76 | Theorem 2-13 proof end, Theorem 2-14 opening, equations (2-96) and (2-97). |
| 089 | 77 | Equations (2-98) and (2-99), Theorem 2-14 conclusion, Remarks 1 through 4, primitives. |
| 090 | 78 | Theorem 2-14 proof, equations (2-100) through (2-102). |
| 091 | 79 | Figure 2-7, mapping equation, dagger footnote after the boundary-value assumption, equation (2-103). |
| 092 | 80 | Equation (2-103) continuation, Theorem 2-15 and equations (2-104) through (2-107). |
| 093 | 81 | Theorem 2-15 proof, distributional setup, Theorem 2-16 opening. |
| 094 | 82 | Theorem 2-16 proof, equations (2-108) and (2-109). |
| 095 | 83 | Theorem 2-16 proof continuation, nuclearity displays, Theorem 2-17 opening and equation (2-110). |

The equation inventory contains each printed tag `(2-49)` through `(2-110)` exactly once. The result sequence is Theorems 2-3 through 2-11, the unheaded Jost result occupying the source's 2-12 counter position, and Theorems 2-13 through 2-17. The source's Remark environments on PDF 063 and PDF 066 and the Lemma on PDF 077 are unnumbered. All theorem, lemma, remark, and proof environments are closed.

The seven figures were checked against their source pages and against the rendered harness:

| Figure | Source | Native file | Render check |
|---|---:|---|---|
| 2-1 | PDF 070, print 58 | `fig2_1.tex` | Contour segments, vertical axis, arrows, labels, and caption checked on harness page 25. |
| 2-2 | PDF 077, print 65 | `fig2_2.tex` | Tube boundary, dashed path, endpoint marks, arrows, labels, and caption checked on harness page 32. |
| 2-3 | PDF 084, print 72 | `fig2_3.tex` | Light-cone projection, separating planes, vectors, labels, and caption checked on harness page 37. |
| 2.4 | PDF 085, print 73 | `fig2_4.tex` | Two cone configurations, primed vectors, caption, and visible decimal figure label checked on harness page 38. |
| 2-5 | PDF 086, print 74 | `fig2_5.tex` | Upper and lower domains, labels, caption, and placement checked on harness page 39. |
| 2-6 | PDF 087, print 75 | `fig2_6.tex` | Contours, labels, caption, and placement checked on harness page 39. |
| 2-7 | PDF 091, print 79 | `fig2_7.tex` | z-plane and w-plane circles, axes, marked points, labels, caption, and placement checked on harness page 43. |

FINDINGS:

| Locator | Defect found | Evidence and effect |
|---|---|---|
| `sec2_3.tex:135` | The source footnote after “holomorphic” is a dagger footnote. | The transcription used a local dagger-form footnote group, preserving the printed marker and keeping later footnote destinations independent. |
| `sec2_3.tex:272-280` | The representation label used plain `D`. | Converted to `\mathcal D` under the binding Weinberg script rule. |
| `sec2_3.tex:323,562` | Two source Remarks were entering the shared theorem counter. | Changed them to `remark*`; the visible word “Remark” remains and the theorem sequence stays aligned. |
| `sec2_3.tex:735` | Equation (2-71) used a non-strict inequality in the working transcription. | Restored the strict `<` visible on PDF 068. |
| `sec2_4.tex:160` | The source Lemma before Theorem 2-11 is unnumbered. | Changed it to `lemma*`. |
| `sec2_4.tex:183` | The displayed theorem identifier needed explicit source control. | The theorem uses the source identifier `[2-11]` while retaining the shared counter for later results. |
| `sec2_4.tex:248-306` | Source matrix notation used a non-house script and old-signature expressions. | Applied the authorized `\mathcal D` conversion and retained the matrix calculation with the project notation contract. |
| `sec2_4.tex:259,656` | The Halmos and convex-separation footnotes were printed with daggers. | Each footnote now uses a local dagger group. |
| `sec2_4.tex:338,563-604,710` | Jost-point cone expressions required the house mostly-plus signature, and the source prose introduces the unheaded 2-12 result. | Converted the scalar-product and spacelike inequalities consistently, then advanced the theorem counter at the end of the Jost proof so Theorems 2-13 through 2-17 keep their printed identifiers. |
| `sec2_5.tex:343-347` | The Figure 2-7 footnote used `\footnotetext` without advancing the footnote counter. | Replaced it with a local dagger `\footnote`; the printed dagger remains and the duplicate `Hfootnote.360` destination disappears in the fresh two-pass build. |
| `fig2_4.tex:4` | The source visibly prints `FIGURE 2.4`. The project ERRATA entry uses `FIGURE 2-4`. | Kept the visible source decimal as `2.4` and retained the semantic label `fig:2-4`. The ERRATA punctuation change was not applied because the unchanged-content requirement and the source image control the figure caption, and the notation contract does not authorize figure-label punctuation changes. |
| `fig2_7.tex:1-34` and `sec2_5.tex:325-331` | The native figure and the section each carried the mapping formula, producing two rendered copies. | Kept the source display in Section 2-5 and removed the duplicate formula node from the native figure. The legacy label `fig:ch2-mobius-map` remains alongside `fig:2-7`, so the section reference resolves. |

EDITS MADE:

- `latex/chapters/chapter02/sec2_3.tex`: corrected the dagger footnote, `\mathcal D` representation labels, unnumbered Remarks, and the strict inequality in (2-71).
- `latex/chapters/chapter02/sec2_4.tex`: corrected `\mathcal D`, the unnumbered Lemma, theorem identifier handling, local dagger footnotes, house-signature Jost expressions, and the implicit 2-12 theorem counter position.
- `latex/chapters/chapter02/sec2_5.tex`: preserved the source dagger while giving the Figure 2-7 footnote a unique hyperlink destination.
- `latex/figures/fig2_4.tex`: preserved the visible decimal caption label `FIGURE 2.4` with semantic label `fig:2-4`.
- `latex/figures/fig2_7.tex`: retained both figure labels, removed the duplicated mapping formula, and preserved the source geometry and caption.

CHECKS RUN:

- Original-resolution visual inspection of all 37 source pages, PDF 059 through PDF 095.
- Original-resolution comparison of Figures 2-1 through 2-7 with the rendered native TikZ figures.
- Two-pass `pdflatex -interaction=nonstopmode -halt-on-error -jobname=ch2_mid_harness /private/tmp/ch2_mid_harness.tex` from `latex/`; the current output is `latex/ch2_mid_harness.pdf` with 46 pages.
- The final log `latex/ch2_mid_harness.log` has no undefined-reference, duplicate-destination, rerun, or LaTeX warning messages. The existing overfull box is in the earlier Section 2-2 harness material, outside this audit packet.
- `pdftotext latex/ch2_mid_harness.pdf /private/tmp/ch2_mid_final.txt`; the extracted text shows Theorems 2-3 through 2-17, the dagger markers, `FIGURE 2.4`, and one Figure 2-7 mapping caption.
- Equation-tag inventory: 62 tags, 62 unique tags, no missing tag in `(2-49)` through `(2-110)`, and no duplicate tag.
- Environment stack audit: no unmatched theorem, lemma, remark, or proof begin/end pair. The section files contain 14 numbered theorem environments, one unnumbered Lemma, two unnumbered Remarks, and 13 closed proofs.
- `chktex -q -Wall latex/chapters/chapter02/sec2_3.tex latex/chapters/chapter02/sec2_4.tex latex/chapters/chapter02/sec2_5.tex`: clean.
- `python3 scripts/audit_notation.py --strict`: no definite notation regressions. The remaining raw-star review candidates are pre-existing files outside this packet.

UNRESOLVED:

The page, equation, theorem, proof, footnote, citation, caption, label, figure, and placement checks are complete for PDF 059 through PDF 095. The Figure 2.4 decimal decision is recorded above. The legacy Figure 2-7 identifier resolves. The duplicate footnote destination is gone.

STATUS: PASS

Unresolved blockers: none
