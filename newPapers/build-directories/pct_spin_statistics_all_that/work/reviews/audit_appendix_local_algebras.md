# Appendix Local Algebras audit

## PASS: source, transcription, and rendering

INPUT SNAPSHOT: Canonical source `origPapers/pct_spin_statistics_all_that.pdf`, SHA-256 `44fadba731cafe7f009d4e561372febb3597e1f2a4819346ce2efd16befcb889`. The packet covers physical PDF pages 203--210, printed pages 191--198. The assigned native files are `latex/appendix/local-algebras.tex` and `latex/figures/figA3.tex`. The source rasters are `work/source-pages/pdf-203.jpg` through `pdf-210.jpg`.

FULL SCOPE READ: Each source raster was read at original detail in page order. The native text was checked line by line against the source reading order. The comparison included prose, displayed mathematics, punctuation, equation tags and labels, theorem text, the dagger footnote, citations, section boundaries, figure labels, figure arrows, figure profiles, the Figure A.3 caption, notation conversions required by `NOTATION.md`, and `% PCT-SOURCE` markers. The final article and JHEP-like renders were inspected after the last source edit.

### Page pass record

| Source page | Printed page | Checked units | Result |
| --- | ---: | --- | --- |
| PDF 203 | 191 | Continuation of the constructive-QFT discussion; citations [61, 62, 60] and [63, 64]; the local-algebra heading; the introduction to local algebras; net axiom I; covariance axiom II | PASS |
| PDF 204 | 192 | Quasilocal algebra and its norm closure; local commutativity axiom III; state linearity, additivity, positivity, normalization, and invariance; GNS theorem and equations (1) and (2) | PASS |
| PDF 205 | 193 | GNS theorem continuation; equations (3) and (4); invariant and covariant states; superselection discussion; citations [65], [69--71], [72], and [73]; sine-Gordon equation and its continuation | PASS |
| PDF 206 | 194 | Massless scalar equation; infrared test-function condition; currents and charges; integer-charge representations; direct-sum Hilbert space; massless Thirring discussion; dagger footnote; massive Thirring equation; boson-fermion relations; beta relation; citations [74], [75], and [77] | PASS |
| PDF 207 | 195 | Massive charge; direct-sum sector decomposition; sine-Gordon vacuum sector; beta range; automorphism limits; normalized state; vacuum ket; kink construction; topological-charge introduction; citations [78--82] | PASS |
| PDF 208 | 196 | Continuation of the topological-charge paragraph; asymptotic completeness; sine-Gordon and $(\varphi^4)_2$ comparison; sector questions; vacuum, soliton, and anti-soliton sectors; limiting equations; citations [83--86] | PASS |
| PDF 209 | 197 | Automorphism iteration; Figure A.3 pointer; four-sector alternatives; Haag--Ruelle statement; parity; weakened-locality fields; all-four-sector direct sum; sector-product paragraph; citation [87] | PASS |
| PDF 210 | 198 | Figure A.3 native reconstruction, all state-profile labels, wavy arrows, axes, expectation-value labels, and the complete caption | PASS |

The physical-page boundary from PDF 203 follows the preceding constructive appendix material. The PDF 205 continuation begins with “of $\mathcal A$”. The PDF 206 continuation begins with “What was done in [72]”. The PDF 208 continuation begins with “a number of non-trivial mathematical problems”. PDF 209 begins with the continuation of the automorphism paragraph. The PDF 210 figure follows the Figure A.3 pointer at the end of PDF 209.

### FINDINGS

| Locator | Defect or evidence | Claim affected | Resolution |
| --- | --- | --- | --- |
| `local-algebras.tex:62--78` | The first native render put the long covariance axiom display beyond the narrow article text block. | The statement of Poincare covariance and its locality image | Split the statement into two `aligned` displays. The words, map, algebra membership, and source markers remain unchanged. |
| `local-algebras.tex:261--281` | The integer-charge set phrase produced a narrow-column overfull line in the JHEP-like harness. | The construction of the integer-charge direct-sum representation | Added a local line-breaking group, split the inline math into adjacent chunks, and retained the source words and symbols. The visible space before `\mathcal H_{n_1,n_2}` is explicit. |
| `figA3.tex:7--109` | The first native figure render was too wide for the target text block. The upper-right prose and middle-right `\langle\varphi\rangle` label also approached each other in the narrow render. | Figure A.3 layout and readability | Added a text-width resize wrapper, reduced the native TikZ scale, and raised the upper-right prose block. All source profiles, arrows, labels, and caption content remain present. The final article and JHEP-like renders have separated text and labels. |
| `local-algebras.tex:114` | `A^*A` is the C-star algebra involution recorded in `NOTATION.md`. | Positivity of a state | Retained the source star. It is not an operator-adjoint conversion. |
| `local-algebras.tex:291--294` and `306--321` | The source uses the older `\psi^+` Dirac-adjoint notation. | Thirring equations, current, density, and charge | Applied the authorized conversion to `\bar\psi=\psi^\dagger\beta`. The equations retain their source order and meaning. |

No missing prose, display, equation tag, citation, footnote, caption sentence, figure label, or page-boundary continuation was found in the eight-page packet. Equation labels `(1)` through `(4)` occur in source order. The source dagger footnote appears after the massless Thirring sentence and is present in the native output. Citations `[61, 62, 60]`, `[63, 64]`, `[65]`, `[69--71]`, `[72]`, `[73]`, `[74, 75]`, `[77]`, `[78--82]`, `[83--86]`, and `[87]` match the source locations.

### Notation audit

| Source role | Native form | Decision |
| --- | --- | --- |
| Script local algebras and Hilbert spaces | `\mathcal A`, `\mathcal A(\mathcal O)`, `\mathcal H` | House script-alphabet form from `NOTATION.md` |
| GNS state vector | `\ket{\Psi_\rho}` | Dirac ket conversion |
| GNS matrix element | `\matrixel{\Psi_\rho}{\pi_\rho(A)}{\Psi_\rho}` | Dirac matrix-element conversion |
| Vacuum state | `\ket{\Omega}` and `\ket{\Omega_{0+}}` | Dirac ket conversion with house vacuum labels |
| C-star involution | `A^*A` | Star retained for the C-star algebra operation |
| Spinor adjoint | `\bar\psi=\psi^\dagger\beta` | Authorized Dirac-adjoint conversion |
| Identity | `\mathbf 1` | House identity form |
| Charge integration | `\dd x` | House differential form |
| Figure expectation values | `\langle\varphi(x)\rangle_s` and related labels | Expectation brackets retained as source observables, rather than state inner products |
| Infinite sector sums | `n_1,n_2\in\mathbb Z` and `(n_1,n_2)\in\mathbb Z^2` | Compact native notation for the source's infinite direct sums |

The direct-sum Hilbert-space formulas preserve the two charge indices. The sector labels `\mathcal H_s`, `\mathcal H_{\bar s}`, `\mathcal H_{0+}`, and `\mathcal H_{0-}` retain their source roles. The Figure A.3 expectation-value brackets remain distinct from the Dirac matrix elements in the GNS formulas.

### Figure audit

PDF 210 contains the two vacuum profiles, the two two-soliton profiles, the soliton profile, and the anti-soliton profile. The native figure includes each horizontal space axis, vertical expectation-value axis, profile curve, state label, four small-panel descriptions, central wavy arrows, and the caption's three automorphism actions. The reconstruction is vector TikZ artwork. It does not import the source raster. The final rendered figure is fully contained in the float and has no text collision in either scoped harness.

## EDITS MADE

| Locator | Change |
| --- | --- |
| `latex/appendix/local-algebras.tex:62--78` | Reflowed covariance axiom II into two aligned displays to fit the text block. |
| `latex/appendix/local-algebras.tex:261--274` | Reflowed the integer-charge prose and inline set notation inside a local emergency-stretch group. |
| `latex/figures/figA3.tex:7--109` | Added `\resizebox`, adjusted TikZ scale and central profile placement, and raised the upper-right explanatory node after rendered inspection. |
| `work/reviews/audit_appendix_local_algebras.md` | Added this page-level audit record. |

## CHECKS RUN

1. Article harness, two passes:

   `TEXINPUTS=.../latex: pdflatex -interaction=nonstopmode -halt-on-error -output-directory=/tmp/pct-audit -jobname=pct-appendix-local /tmp/pct-audit-appendix-local.tex`

   Result: exit 0 on both passes, 9 pages, letter paper. The only remaining LaTeX warning is the harness's absolute-path package-name warning for `pct.sty`. No overfull, underfull, float-size, undefined-reference, or changed-label warning remains.

2. JHEP-like harness, two passes:

   `TEXINPUTS=.../latex: pdflatex -interaction=nonstopmode -halt-on-error -output-directory=/tmp/pct-audit -jobname=pct-appendix-jhep /tmp/pct-audit-jhep.tex`

   Result: exit 0 on both passes, 8 pages, A4 paper. The layout, float, reference, and box-warning scan is clean. The `rerunfilecheck` package line is package metadata, not a rerun warning.

3. Render checks:

   `pdftoppm -r 150 -png` rendered all 9 article pages and all 8 JHEP-like pages. Every final page was inspected in page order. Article page 4 and page 9, and JHEP-like page 4 and page 8, were revisited after the last layout edits. The figure page was checked at original raster detail after the upper-right node adjustment.

4. Marker scan:

   `rg -n -e 'PCT-SOURCE: pdf=(203|204|205|206|207|208|209|210)' latex/appendix/local-algebras.tex latex/figures/figA3.tex`

   Counts by physical page are PDF 203: 10, PDF 204: 13, PDF 205: 9, PDF 206: 14, PDF 207: 12, PDF 208: 8, PDF 209: 9, and PDF 210: 2. The PDF 210 count includes the local-file hook and the figure source marker.

5. Final scoped artifact hashes:

   `6b2cdeea809b1956f4699205c55de233a3e49e73cad21e4051a50bd8e150051a` for `/tmp/pct-audit/pct-appendix-jhep.pdf`.

   `e344af3eb77e17dc0ac476e62a512bada91e8b30774cc07b8714d2888d3eab83` for `/tmp/pct-audit/pct-appendix-local.pdf`.

6. Text extraction smoke check:

   `pdftotext -layout /tmp/pct-audit/pct-appendix-jhep.pdf /tmp/pct-audit/pct-appendix-jhep.txt` followed by searches for `Theorem`, `Figure A.3`, `Thirring`, `topological`, `[87]`, and `Poincar`. All six tokens were present. Superscript automorphism labels were checked in the rendered page and in the extracted `s2` form.

## UNRESOLVED

The full master-document build was outside this assigned packet. The scoped article and JHEP-like harnesses cover both assigned source files and the Figure A.3 inclusion path. No source comparison, notation, marker, equation, citation, footnote, caption, or rendered-layout issue remains in PDF 203--210.

STATUS: PASS

Unresolved blockers: none
