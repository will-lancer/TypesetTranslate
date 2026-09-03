# Independent source review: physical PDF pages 147--281

## Basis and method

The authority was `/Users/wlancer/Coding_Projects/TypesetTranslate/newPapers/build-directories/banks_qft/banks-qft.pdf`, verified at 281 pages with SHA-256
`31de7827e7bc636feaa7028fe4dbb63a718b3926ee43ff3d96d91185a44eafe3`.
I reviewed every physical source page from 147 through 281 in the shared
150-DPI render at
`/private/tmp/banks-qft-shared-01a063b0/source-render-150dpi/page-<n>.png`.
The native transcription was checked in
`/Users/wlancer/Coding_Projects/TypesetTranslate/newPapers/build-directories/banks_qft/latex/transcription-check.pdf` and in its source tree. Text extraction located passages and source markers; rendered source pages controlled readings of mathematics and diagrams. High-resolution comparisons were made for the changed material on source pages 160, 192, 193, and 258. The current TeX was also compiled in the isolated scratch output
`/private/tmp/banks-qft-review-147-281/recheck-latest/build/transcription-check.pdf`
for visual re-review of the changed pages.

The target has 266 reflowed pages. Its page layout does not preserve source
page numbers. The ledger below therefore records physical source-page ranges,
their target files, and the inspected content. Chapter 10 was checked in this
pass; the earlier Chapter 10 report was supporting evidence only.

## Coverage ledger

All 135 physical pages in the assigned range have source markers and were
reviewed.

| Physical source pages | Content inspected | Target locations | Result |
|---|---|---|---|
| 147--152 | Chapter 9 opening, §§9.1--9.2, Figure 9.1, prose and displays | `chapters/chapter09/opening.tex`, `sec9_1.tex`, `sec9_2.tex`, `figures/figure9_1.tex` | Source-faithful |
| 153--158 | §§9.2--9.4, prose, equations, displays, section transitions | `chapters/chapter09/sec9_2.tex`--`sec9_4.tex` | Source-faithful |
| 159--163 | §9.4, Figure 9.2, Figure 9.3, equations and prose | `chapters/chapter09/sec9_4.tex`, `figures/figure9_2.tex`, `figures/figure9_3.tex` | Source-faithful after logged E-027 |
| 164--170 | §§9.5--9.6, Figures 9.4--9.5, equations, displays, footnote | `chapters/chapter09/sec9_5.tex`, `sec9_6.tex`, `figures/chapter09-fig94.tex`, `figures/chapter09-fig95.tex` | Source-faithful |
| 171--176 | §§9.7--9.8, Figure 9.6, equations and displays | `chapters/chapter09/sec9_7.tex`, `sec9_8.tex`, `figures/chapter09-fig96.tex` | Source-faithful |
| 177--182 | §9.8, Figure 9.7, equations, displays and prose | `chapters/chapter09/sec9_8.tex`, `figures/chapter09-fig97.tex` | Source-faithful |
| 183--190 | §§9.9--9.10, equations, displays and prose | `chapters/chapter09/sec9_9.tex`, `sec9_10.tex` | Source-faithful |
| 191--197 | §9.11, Figures 9.8--9.10, equations, displays and prose | `chapters/chapter09/sec9_11.tex`, `figures/chapter09-fig98.tex`, `figures/chapter09-fig99.tex`, `figures/chapter09-fig910.tex` | Source-faithful after figure rebuild |
| 198--202 | §§9.12--9.13, equations, displays and prose | `chapters/chapter09/sec9_12.tex`, `sec9_13.tex` | Source-faithful apart from E-024 |
| 203--210 | §9.14, equations, displays, prose and footnotes | `chapters/chapter09/sec9_14.tex` | Source-faithful apart from E-025 |
| 211--215 | §9.15 and Problems 9.1--9.10, including displays and citations | `chapters/chapter09/sec9_15.tex`, `problems.tex` | Source-faithful |
| 216--251 | Chapter 10 §§10.1--10.8, equations, displays, footnotes and Problems 10.1--10.5 | `chapters/chapter10/sec10_1.tex`--`sec10_8.tex`, `problems.tex` | Source-faithful after logged E-007--E-009 and prior structural corrections |
| 252--254 | Chapter 11 opening, prose and displays | `chapters/chapter11/chapter11.tex` | Source-faithful |
| 255--256 | Appendix A, prose, equations and footnote | `appendices/appendixA.tex` | Source-faithful |
| 257 | Appendix B, prose and displays | `appendices/appendixB.tex` | Source-faithful |
| 258--260 | Appendix C, prose, equations and displays | `appendices/appendixC.tex` | Source-faithful after logged E-022 and E-031 |
| 261--265 | Appendix D, all Feynman-rule diagrams, Figure D.1, prose and displays | `appendices/appendixD.tex`, `figures/appendixD.tex` | Source-faithful after logged E-002 |
| 266--269 | Appendix E, prose and displays | `appendices/appendixE.tex` | Source-faithful |
| 270--271 | Appendix F, prose and displays | `appendices/appendixF.tex` | Source-faithful |
| 272--277 | References 1--180, including source spellings and bibliographic punctuation | `backmatter/references.tex` | Source-faithful |
| 278 | Author index, names and page references | `backmatter/author-index.tex` | Source-faithful after logged E-015 |
| 279--281 | Subject index, entries and page references | `backmatter/subject-index.tex` | Source-faithful after logged E-016 |

## Findings

### F-001 [RESOLVED] Source page 160 has a logged `K` versus `K^{-1}` correction

Source physical p.160, printed p.150, in the paragraph immediately before
Figure 9.2, reads:

> The two contributions to the variation of `S_I` have an interpretation in terms of Feynman diagrams (Figure 9.2), one a loop diagram and one a tree. Note that the internal lines in these diagrams are proportional to `\partial_t K`, which is non-zero only for momenta near the cut-off.

The rendered source reading is also visible in
`/private/tmp/banks-qft-review-147-281/source-147-281.txt` and the source
render for page 160. The target at
`/Users/wlancer/Coding_Projects/TypesetTranslate/newPapers/build-directories/banks_qft/latex/chapters/chapter09/sec9_4.tex:132-138`, specifically line 135, reads
`$\partial_tK^{-1}$`.

The preceding source equations use `\partial_tK^{-1}`, so the target form
is the mathematically intended correction to a source typo. E-027 now records
source form `\partial_t K`, adopted form `\partial_t K^{-1}`, with the
equation-based reason. The target retains the adopted form at line 135, so
the source discrepancy is accounted for as a logged editorial erratum.

### F-002 [RESOLVED] Figure 9.9 reconstruction

Source physical p.192, printed p.182, shows seven one-loop contributions to
the potential. The source has seven separately bounded Wilson-loop panels
labelled (a)--(g), horizontal wavy gluon lines, the curved loop topologies
for (b), (c), (e), and (f), the two-line configuration in (d), a shaded oval
in (g), and plus signs between the contributions. The source crop is
`/private/tmp/banks-qft-review-147-281/source300-192-fig.png`.

The rebuilt target at
`/Users/wlancer/Coding_Projects/TypesetTranslate/newPapers/build-directories/banks_qft/latex/figures/chapter09-fig99.tex:10-144`
implements the seven source panels in source order. The isolated rebuild at
`/private/tmp/banks-qft-review-147-281/recheck-latest/target-rebuilt-178.png`
shows the Wilson-loop walls, horizontal propagator lines, curved loop
connections, panel (g) insertion, labels, and plus separators. The previous
cross-panel arcs and rearranged topologies are absent. Source and target now
agree at the semantic diagram level; the native coil glyph has minor stroke
variation from the scanned source.

### F-003 [RESOLVED] Figure 9.10 equation components and loop labels

Source physical p.193, printed p.183, presents the gluon vacuum polarization
as a diagrammatic equation. It contains a shaded oval on the left, an equals
sign, then six one-loop diagrams labelled (a)--(f) joined by plus signs. The
fermion loop in (d) carries `R_F` labels. The scalar loops in (e) and (f)
carry `R_S` labels. The fermion and scalar loops also have the source
arrowheads indicating orientation. The source crop is
`/private/tmp/banks-qft-review-147-281/source300-193-top.png`.

The rebuilt target at
`/Users/wlancer/Coding_Projects/TypesetTranslate/newPapers/build-directories/banks_qft/latex/figures/chapter09-fig910.tex:72-120`
implements the leading oval, equality, plus signs, six oriented loops,
`R_F` under (d), and `R_S` under (e) and (f). The isolated rebuild at
`/private/tmp/banks-qft-review-147-281/recheck-latest/target-rebuilt-179.png`
matches the source equation components and loop orientations on p.193. The
figure discrepancy is resolved.

### F-004 [RESOLVED] Appendix C Majorana transformation, E-031

Source physical p.258, printed p.248, displays
`S_M=2^{-1/2}(\sigma_3+\sigma_2)\otimes1` before stating that the Majorana
Dirac equation is satisfied separately by the real and imaginary parts of the
field. E-031 records this source matrix as the faulty source form.

The target at
`/Users/wlancer/Coding_Projects/TypesetTranslate/newPapers/build-directories/banks_qft/latex/appendices/appendixC.tex:57-67`
uses the adopted block matrix
`S_M=2^{-1/2}[[\mathbf 1,\sigma_2],[\sigma_2,-\mathbf 1]]`.
An independent 4x4 calculation with the displayed Weyl and Dirac
conventions gives `S_M^\dagger S_M=1` for the adopted matrix, preserves the
Clifford anticommutator, and makes the real parts of all four transformed
`\gamma_M^\mu` matrices vanish to numerical roundoff. The source matrix
leaves `\gamma_M^2` real. E-031 therefore supplies the needed mathematical
correction and the target claim is valid.

## Logged errata confirmed in this range

The following existing entries were checked against the rendered source and
the target. They are recorded editorial changes rather than new findings:

- E-002, circular-polarization basis in Appendix D, source p.264.
- E-007, “purse” to “pursue” on p.216.
- E-008, “arbitary” to “arbitrary” in Problem 10.2 on p.250.
- E-009, “Nielson” to “Nielsen” in Problem 10.4 on p.251.
- E-010, the heat-flow sentence on p.161.
- E-015, “Nielson” to “Nielsen” in the author index on p.278.
- E-016, “Nielson--Olesen” to “Nielsen--Olesen” in the subject index on p.280.
- E-022, the contracted metric index in Appendix C on p.260.
- E-023, the free Lorentz index in equation (9.8) on p.196.
- E-024, “forseeable” to “foreseeable” on p.200.
- E-025, the one-particle-reducible terminology in Section 9.14 on p.206.
- E-027, the cutoff-kernel derivative before Figure 9.2 on p.160.
- E-031, the Majorana-basis transformation in Appendix C on p.258.

The references and indices retain source bibliographic spellings and page
references, including entries that look unusual in isolation. No additional
prose, equation, footnote, problem, reference, or index omission was found in
the assigned pages.

## Final review

The three initial findings are resolved by E-027 and the rebuilt figures.
Appendix C now carries the verified E-031 matrix. The complete physical
page range, including Chapter 10, the appendices, references, and both
indices, passes source and mathematical review. The report remains
work-only; no transcription, style, inventory, or solution files were edited.

FINAL STATUS: PASS
