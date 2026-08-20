# Independent audit: Chapter 4, Section 4-4

PASS: 1, source reconstruction and page continuity

INPUT SNAPSHOT: `origPapers/pct_spin_statistics_all_that.pdf`, source SHA-256 `44fadba731cafe7f009d4e561372febb3597e1f2a4819346ce2efd16befcb889`; `latex/chapters/chapter04/sec4_4.tex`, snapshot SHA-256 `469d1f162cfb7c4f2a6ae5e2c34232f023436845002d1799846ae8eabffc96a3`; source raster pages `work/source-pages/pdf-158.jpg` through `work/source-pages/pdf-172.jpg`.

FULL SCOPE READ: I read each source page in order and compared its prose, theorem and example boundaries, proof endings, footnote, cross-references, displayed mathematics, and source-page continuations with `sec4_4.tex`. The page map is: PDF 158, the end of the general-spin PCT proof and Theorem 4-7; PDF 159, the section opening and Theorem 4-8; PDF 160, the end of that proof, its corollary, and Theorem 4-9; PDF 161, the holomorphic proof through (4-47); PDF 162, the end of Theorem 4-9 and Theorem 4-10 through (4-52); PDF 163, Example 1 through the first view; PDF 164, the first-view continuation and Example 2 through Theorem 4-11; PDF 165, the Theorem 4-11 proof and Example 2 through (4-56); PDF 166, the second example, its Klein transformation, and Theorem 4-12; PDF 167, the general even-odd construction and the Klein case analysis; PDF 168, the case-analysis continuation, (4-58), and the monomial setup; PDF 169, (4-59) through (4-62); PDF 170, Theorem 4-13, both proof headings, and (4-64); PDF 171, (4-65) through the symmetric matrix relation; PDF 172, the decomposition proof, the abnormal PCT display, and the opening of Example 3. Every source page from 158 through 172 has a corresponding `PCT-SOURCE` marker.

FINDINGS: The source packet has one sentence crossing PDF 163 and PDF 164 without a marker before `say F(\varphi,\psi)`. The vertical choice in (4-59), its following even/odd sentence, the parenthesized choice in (4-60), and the vertical choices in the statement preceding (4-63) had been reflowed as `cases` or had lost the intervening source prose. Equation (4-62) had the second scalar product in the commuted source order. Equation (4-69) had folded the two-case factor into the exponent and omitted the source factor `(-1)^J`.

EDITS MADE: None in this pass.

CHECKS RUN: Visual comparison of all fifteen source page images; page-boundary scan for `pdf=158` through `pdf=172`; cross-reference check for (4-34), (4-35), and (4-36) in `latex/chapters/chapter04/sec4_3.tex`.

UNRESOLVED: None in the source reconstruction pass.

STATUS: PASS

PASS: 2, technical and equation audit

INPUT SNAPSHOT: Same source and native snapshot as Pass 1, with the repaired file read from disk after the edits below.

FULL SCOPE READ: I checked the printed equation sequence (4-37) through (4-69), including signs, phases, exponents, indices, mod-2 statements, hypotheses, proof conclusions, and unnumbered displays. References to (4-34) through (4-36) were checked against their definitions in `sec4_3.tex`; those displays are not duplicated in Section 4-4. The source footnote on parity at PDF 168 is present. Ref. 28, Ref. 6, Theorems 3-4 and 4-3, Theorem 4-10, Theorem 4-11, and the source cross-references to (4-30), (4-57), (4-58), (4-59), (4-60), (4-61), (4-64), and (4-65) remain present and attached to the same claims.

FINDINGS: The equation and prose-shape findings recorded in Pass 1 were the only source discrepancies. The source image for (4-69) shows `(-1)^J` followed by the stacked factor with upper entry `i` and lower entry `1`; the surrounding prose assigns the upper choice to half-odd integer spin and the lower choice to integer spin.

EDITS MADE: At the PDF 163/164 boundary, split the sentence after `If a certain function,` and added the PDF 164 continuation marker. Restored the stacked factor and intervening prose after (4-59), the source parenthesized two-row display for (4-60), and the stacked choices in the statement before (4-63). Reordered the second product in (4-62) to `t_j(\alpha)t_i(\beta)`. Repaired (4-69) to `(-1)^J\left(\begin{smallmatrix}\ii\\1\end{smallmatrix}\right)\varphi_i^{\prime\dagger}(\widehat f)`, preserving the source choice factor while applying the authorized Dirac-adjoint notation.

CHECKS RUN: `rg -o 'tag\\{4-[0-9]+\\}' latex/chapters/chapter04/sec4_4.tex` returns every tag from 4-37 through 4-69 exactly once. The source equation images for PDFs 159 through 172 were re-read after each repair, with special attention to (4-59), (4-60), (4-62), (4-63), and (4-69).

UNRESOLVED: None in the technical record.

STATUS: PASS

PASS: 3, notation and source-authorized native form

INPUT SNAPSHOT: Current `sec4_4.tex`; `NOTATION.md`; `notation-map.jsonl`, entries for the PCT and general-spin packet, including the `discrete-symmetry.order-and-dirac-adjoint` rule scoped to `sec4_4.tex`.

FULL SCOPE READ: The source vacuum products use `\bra{\Omega}` and `\ket{\Omega}` in the native packet. Field operator adjoints use `\dagger`; scalar and test-function conjugation retain their source roles. The mostly-plus Weinberg metric maps the source spacelike condition to `(x-y)^2>0`. `\PCT`, `\mathcal H`, `\mathcal P_+^\uparrow`, `\mathcal T'_1`, `\C`, and `\ii` follow the authorized project notation. The source star in (4-69) is represented by the authorized field Dirac adjoint, while the spin-choice factor remains explicit.

FINDINGS: No notation outside the authorized map remains in the assigned packet after the technical repairs.

EDITS MADE: The notation changes were limited to the authorized native forms described above. No notation-map entry was changed.

CHECKS RUN: `python3 scripts/audit_notation.py` completed with no definite notation regressions. The packet was checked for `\PCT`, explicit bra-kets, `\dagger`, `\ii`, and the source marker scope.

UNRESOLVED: None in the notation audit.

STATUS: PASS

PASS: 4, build and rendered-page inspection

INPUT SNAPSHOT: Repaired `sec4_4.tex`, current full manuscript assembly, and source SHA-256 `44fadba731cafe7f009d4e561372febb3597e1f2a4819346ce2efd16befcb889`.

FULL SCOPE READ: The native section renders on manuscript PDF pages 136 through 147. I inspected all twelve rendered pages at 180 dpi after the final repair. The page containing (4-69) shows the explicit `(-1)^J` factor and the stacked `i/1` choice. The rendered page containing (4-59) and (4-60) shows both stacked choices and the intervening prose. Theorem 4-13 displays the source normal/abnormal choice. Equations and proof endings remain visible, with the final sentence on PDF 172 continuing into the next source packet as expected.

FINDINGS: The full draft log contains an unrelated underfull page warning outside this packet. The assigned section introduces no fatal error, undefined reference, or layout warning in its twelve rendered pages.

EDITS MADE: None after the final render inspection.

CHECKS RUN: Historical packet checks from `newPapers/build-directories/pct_spin_statistics_all_that`: `./build_and_verify.sh --draft` exited 0; the source, notation, and project audits passed; `latexmk -g -pdf -interaction=nonstopmode -halt-on-error master.tex` produced a 185-page native PDF; a fatal/reference scan of `latex/master.log` was clean; and `pdftoppm -f 136 -l 147 -r 180 -jpeg latex/master.pdf /tmp/pct-audit/rendered-ch4/rebuild-page` produced the twelve inspected page images. The historical packet PDF SHA-256 was `f3d3fd02de9f5896c08f64fcaa6f50fb33fb2149384aa03fd37d176c6091ca6e`.

CURRENT FINAL-CANDIDATE EVIDENCE: The current `latex/master.pdf` is an A4,
180-page PDF with SHA-256
`4741fe42fc72801e9b3bee2249eafcd0c013b52935f78827f646c3b1b6d05735`. The
current rendered evidence contains 180 rendered-page records and 180/180
checksum-bound visual inspection records; render validation passed for all
180 pages. The packet's twelve inspected pages remain within this final
candidate's 180-page render.

UNRESOLVED: The focused Section 4-4 packet has no unresolved source, notation, build, or rendering blocker. The unrelated global warning remains outside this assigned scope.

STATUS: PASS

Unresolved blockers: none
