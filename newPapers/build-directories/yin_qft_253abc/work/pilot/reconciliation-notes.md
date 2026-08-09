# Pilot note-source reconciliation

Status: `notes-exact.tex` needs the corrections below before the source packet is frozen.

## Inspection record

- Source inspected: `/Users/wlancer/Desktop/IAS/phy/qft/qft_253abc_book.pdf`, physical pages 6--14, original Physics 253a note pages 1--9.
- Verified SHA-256: `9e5e4d241fffffa56c1c3df6dce4b83178f75787dd5d794a18c5d0c087769f21`.
- Visual evidence: all nine 3400 by 4448 Poppler renders in `work/pilot/note-pages/`, with targeted enlarged crops where the audits disagreed.
- Audit evidence: every file in `work/pilot/page-audits/`, covering physical pages 6--14.
- Compared features: page boundaries, wording, capitalization, punctuation, equations, signs, measures, indices, transformation arrows, connector arrows, diagrams, marginal notes, underbraces, hats, check marks, and semantic ink colors.

## Exact corrections required in `notes-exact.tex`

Line references describe the current file as inspected on 2026-08-08.

| ID | Note / PDF page | Current location | Required source-faithful change | Evidence and confidence |
|---|---|---|---|---|
| R06-01 | 1 / 6 | line 38 | Change `Q: what is QFT?` to `Q: What is QFT?`. | Full-page render and p. 6 audit, 1.00. |
| R06-02 | 1 / 6 | line 70 | Preserve the visible spacing in `Yang--Mills / QCD`. | Full-page render and p. 6 audit, 0.99. |
| R06-03 | 1 / 6 | line 77 | Change `Captures` to the source's lowercase `captures`. | Full-page render and p. 6 audit, 0.99. |
| R06-04 | 1 / 6 | line 87 | Change `Standard model.` to the source's lowercase `standard model.` | 400-dpi render and p. 6 audit, 0.98. |
| R06-05 | 1 / 6 | lines 81--88 | Place the pale-blue `renormalizable` label on or immediately above the box's top edge. It currently appears as the first line inside the box. | Diagram geometry in the source and p. 6 audit, 0.97. |
| R06-06 | 1 / 6 | lines 102--104 | Add the missing third magenta `253b` arrow to the `Statistical Ising model ... criticality` example. Keep the existing arrows to Yang--Mills / QCD and chiral perturbation theory. | The source contains three distinct magenta arrowheads; p. 6 audit, 0.98. |
| R07-01 | 2 / 7 | line 132 | Preserve the source wrap after `electron $g$-factor,` and put `Lamb shift.` on the next line. | Page layout and p. 7 audit, 0.99. |
| R08-09-01 | 3--4 / 8--9 | lines 161--167, 174--196, 205--209 | Preserve the handwritten creator superscript as literal `+` in the exact layer: `a_{\vec p}^{+}` and corresponding products. The same cross-shaped superscript recurs on pages 8, 9, and 12. A dagger conversion belongs in an `EQUATION_NORMALIZED` layer. | Page 12--13 audit gives 0.995 ink confidence; direct comparison shows the same glyph on pages 8--9. The p. 8--9 audit assigned dagger semantics, so this is also logged under inter-audit resolutions below. |
| R09-01 | 4 / 9 | lines 182--189 | End the nonzero commutator with a comma, as written. Remove the added period after the gray state-normalization line. | 800-dpi p. 9 audit and render, 0.99. |
| R09-02 | 4 / 9 | lines 198--199 | Put the blue check mark on its own centered line below `particles.` | Source geometry and p. 9 audit, 0.98. |
| R09-03 | 4 / 9 | lines 205--209 | Remove the typeset explanatory phrase `blue curved arrow from $H_{\mathrm{int}}$`. Draw only the blue U-shaped connector between `H_{\mathrm{int}}` and the blue monomials. Keep its terminal neutral until the arrowhead ambiguity is resolved. | The phrase is editorial metadata absent from the page. The connector is visible; its arrowhead is unresolved at 0.88 confidence. |
| R10-01 | 5 / 10 | lines 219--240 | Refine the causality figure: curve the upper-left green cone branch slightly; place visible purple and red arrowheads along their dashed trajectories while retaining the filled endpoint dots. | Full-page render and p. 10 audit, 0.97 for geometry and color roles. |
| R10-02 | 5 / 10 | line 243 | Encode the four visible terminal dots explicitly, for example with four `\ldotp` marks. | 600-dpi p. 10 audit, 0.97. |
| R10-03 | 5 / 10 | lines 248--255 | Reproduce the split-color field annotation: black `\phi(x)`, a blue added hat, a blue wavy underline under `operator`, and the blue curved arrow from the argument `x` to the blue coordinate note. The present comments describe these marks without rendering them. | Full-page render and p. 10 audit, 0.99 for the split color and 0.98 for the arrow. |
| R11-01 | 6 / 11 | lines 263--266 | Replace `\longmapsto` with the handwritten wavy transformation arrow `\rightsquigarrow`. | 600-dpi audit, 0.96. |
| R11-02 | 6 / 11 | lines 267--276 | Render the source's four diagonal entries `(-1,1,1,1)` in large parentheses, or equivalently `\operatorname{diag}(-1,1,1,1)`. Remove `\ldots`. Add the blue curved arrow from the metric condition to the preceding `\Lambda`. | Enlarged metric crop and p. 11 audit, 0.99. |
| R11-03 | 6 / 11 | line 285 | Preserve the literal sentence `It suffizes to study infinitesimal version`. Remove the added terminal `--`. | Enlarged crop and p. 11 audit, 0.98. |
| R11-04 | 6 / 11 | lines 286--293 | Draw both blue arrows from `\omega` and `\epsilon` to the blue note `small, keep only $1^{\mathrm{st}}$ order`. | Source geometry and p. 11 audit, 0.99. |
| R11-05 | 6 / 11 | lines 294--302 | Keep the generator expansion unchanged, then draw the two blue label arrows to `\hat P_\mu` and `\hat J^{\mu\nu}`. The labels alone do not preserve the source relations. | Source geometry and p. 11 audit, 0.99. |
| R12-01 | 7 / 12 | line 328 | Change the heading punctuation to the visible semicolon: `Micro causality;`. | 600-dpi p. 12 audit, 0.98. |
| R12-02 | 7 / 12 | lines 349--369 | Use the literal creator superscript `+` in the Hamiltonian, momentum, and scalar-field expansion. | 600-dpi crops and p. 12 audit, 0.995. |
| R12-03 | 7 / 12 | lines 353--356 | End the `\vec P` display with the source's terminal period. | p. 12 audit, 0.98. |
| R12-04 | 7 / 12 | lines 363--372 and p. 13 top | Remove the added period after the scalar-field expansion. Render the blue curved arrow from the positive-phase `p\cdot x` into the blue definitions on the next source page, including the separate opening blue curve visible at the top of p. 13. | Cross-page visual unit and p. 12--13 audit, 0.98 for the relation; 0.78 for the isolated top curve's exact shape. |
| R13-01 | 8 / 13 | line 382 | Change the heading punctuation to `Check micro causality;`. | 600-dpi p. 13 audit, 0.98. |
| R13-02 | 8 / 13 | lines 384--386 | Insert the visible centered multiplication dot between the spatial on-shell measure and the exponential bracket. | 600-dpi crop and p. 13 audit, 0.995. |
| R13-03 | 8 / 13 | lines 395--399 | Preserve the second blue label as `inv't under`; end the transformation line after `x\to\Lambda x,\ y\to\Lambda y.` Then place `result a function of $(x-y)^2$ only.` as a separate blue line below the brace. | Source layout and p. 13 audit, 0.98. |
| R13-04 | 8 / 13 | line 403 | Remove the leading `\longrightarrow` before `integrand odd under ...`. Enlarged direct inspection shows blank space before `integrand`; the source arrows on that proof line are the vector accents and the momentum-reversal arrow. | Direct 3400-pixel crop, 0.97. The p. 12--13 audit's proposed leading `\Rightarrow` before `\vec x-\vec y\ne0` appears to have mistaken the vector accent over `x` for an implication arrow. |
| R14-01 | 9 / 14 | lines 417--418 | Replace the plain rule with the hand-drawn horizontal divider ending in a right-pointing arrowhead, followed by the two small apostrophe-like marks. | 500-dpi p. 14 audit, 0.95 for the divider, 0.70 for the terminal shapes. |
| R14-02 | 9 / 14 | lines 424--427 | Preserve the handwritten forms `Poincar\'e - invt vacuum`, `Poincar\'e - covariance`, and `microcausality` as one word. | p. 14 audit, 0.98--0.99. |
| R14-03 | 9 / 14 | line 433 | Preserve the visible space before the question mark in `How to construct such theories~?`. | p. 14 audit, 0.99. |

## Equation, sign, measure, and index agreement

The following items agree with the source once the creator-superscript and punctuation changes above are applied.

| Note / PDF page | Checked source content | Result |
|---|---|---|
| 3 / 8 | `H|\vec p\rangle=\sqrt{\vec p^{\,2}+m^2}|\vec p\rangle`; the literal multiparticle shorthand `H=\sum_{i=1}^n\sqrt{\vec p_i^{\,2}+m^2}`; creation/annihilation brace; one-particle state | Energies, radical signs, momentum indices, vacuum ket, order, and page ending agree. The multiparticle line correctly remains a shorthand without an added ket. |
| 4 / 9 | two-particle state; `[a,a]=[a^+,a^+]=0`; `[a_{\vec p},a^+_{\vec p'}]=\delta^{(D-1)}(\vec p-\vec p')`; gray inner product; free Hamiltonian; `H=H_0+H_{\mathrm{int}}`; blue cubic monomials | The bare delta normalization agrees. The free measure is exactly `d^{D-1}\vec p`, with the displayed square-root energy and no added normalization factors. The second blue monomial has the creator mark on its third `a`. |
| 6 / 11 | scalar covariance; `\Lambda^\mu{}_\nu=\delta^\mu{}_\nu+\omega^\mu{}_\nu`, `a^\mu=\epsilon^\mu`; `U=1-i\epsilon^\mu\hat P_\mu+(i/2)\omega_{\mu\nu}\hat J^{\mu\nu}` | All generator signs, factors, upper and lower indices, and operator hats agree. |
| 6 / 11 | faint group law and Poincare algebra | `U(\Lambda',a')U(\Lambda,a)=U(\Lambda'\Lambda,\Lambda'a+a')`, `[P,P]=0`, `[P^\mu,J^{\rho\sigma}]=-i(\eta^{\mu\rho}P^\sigma-(\rho\leftrightarrow\sigma))`, and `[J^{\mu\nu},J^{\rho\sigma}]=-i(\eta^{\nu\rho}J^{\mu\sigma}-\eta^{\mu\rho}J^{\nu\sigma}-(\rho\leftrightarrow\sigma))` all agree. The source omits hats in these faint gray lines, as the transcription does. |
| 7 / 12 | spacelike commutator, mostly-plus interval, free `H`, `\vec P`, `\hat P^\mu=(H,\vec P)`, and free-scalar expansion | The minus sign on the time separation, plus sign on the spatial separation, measures, radical coverage, Fourier phases, and field hats agree. The scalar denominator radical covers the complete `(2\pi)^{D-1}2\omega_{\vec p}` product. |
| 8 / 13 | blue definitions of `p\cdot x` and `\omega_{\vec p}`; first commutator integral; covariant on-shell rewrite; odd-integrand proof | The phase signs and ordered exponential difference agree. The first denominator is `(2\pi)^{D-1}2\omega_{\vec p}`. The second denominator is `(2\pi)^{D-1}`, followed by `\theta(p^0)\delta(p^2+m^2)`; the mass-shell sign is plus for the mostly-plus metric. The literal numerator `d^D p^\mu` is preserved. The equal-time choice and conclusion for `(x-y)^2>0` agree after R13-04. |
| 9 / 14 | `U(\Lambda,a)\hat\phi(x)(U(\Lambda,a))^{-1}=\hat\phi(\Lambda x+a)` | Group parameters, inverse placement, transformed argument, hats, equality sign, and final period agree. |

## Diagram, marginal-note, color, and boundary agreement

| Note / PDF page | Agreement after listed corrections |
|---|---|
| 1 / 6 | The black answer fork has two branches without arrowheads. The dark-blue dashed divider, gray parenthetical notes, pale-blue renormalizable box, lavender non-renormalizable box, blue `253a`, magenta `253b`, and the example groupings are present. The three `253a` endpoints already agree. |
| 2 / 7 | The full-width underlined course-plan heading, numbered blocks, bullet order, spelling `counter terms`, `Green functions`, `S-matrix, LSZ reduction`, and final page boundary agree. The page carries black ink only. |
| 3 / 8 | The gray momentum marginal note and its `D`-dimensional line agree. The operator brace agrees. The page ends after the one-particle creator equation, and p. 9 continues with the two-particle state. |
| 4 / 9 | The gray normalization line, blue interaction examples, and blue check mark are all represented. The page ends after the relativistic-symmetry warning; p. 10 begins the causality unit. |
| 5 / 10 | The black offset axes, green four-branch light cone, blue event, purple timelike trajectory, red superluminal trajectory, endpoint dots, warning label, and blue coordinate marginal note agree in semantic content. The last bullet continues directly onto p. 11. |
| 6 / 11 | The blue Lorentz-condition annotation, blue small-parameter note, blue generator labels, and four faint gray marginal lines all have the correct semantic colors. P. 12 starts a new microcausality unit. |
| 7--8 / 12--13 | The field expansion and its blue phase/frequency note form one cross-page unit. Both blue underbraces and the final blue check mark are present. P. 13 ends the microcausality proof; p. 14 continues with the covariance check. |
| 9 / 14 | The opening bullet continues the free-field discussion. The postulate block uses four round bullets, followed by two dash bullets. The page is grayscale. Its final line is the pilot endpoint; physical p. 15 begins Problem Set 1. |

All nine `\YinPageBoundary` declarations map original note pages 1--9 to physical PDF pages 6--14 correctly. The source unit that crosses each boundary should remain linked in provenance: creator construction across pp. 8--9, Poincare covariance across pp. 10--11, and phase convention across pp. 12--13.

## Ambiguity reconciliation

### Resolved entries

- `A6-1`: resolve to the explicit four-entry mostly-plus signature `\operatorname{diag}(-1,1,1,1)`. The staggered entries occupy a diagonal matrix layout. Confidence 0.99. Update `ambiguities.md`; this is no longer an open reading.
- `A6-2`: retain `\eta^{\nu\rho}J^{\mu\sigma}-\eta^{\mu\rho}J^{\nu\sigma}-(\rho\leftrightarrow\sigma)`. A 1200-dpi crop resolves the indices and both displayed minus signs. Confidence 0.99. Mark resolved.
- Creator superscripts: the source draws `+`; use `a^+` in `NOTES_EXACT`. The symbol has adjoint meaning, and a dagger rendering is an explicit notation normalization. Confidence 0.995 on p. 12 and 0.95 across the matching glyphs on pp. 8--9.
- Equal-time proof arrows on p. 13: direct crop inspection shows vector accents over `\vec x,\vec y,\vec p` and the arrow in `\vec p\to-\vec p`. It shows no leading implication arrow before either proof line. Remove the current added arrow before `integrand`. Confidence 0.97.

### Unresolved entries retained in the source layer

| ID | Location | Competing readings | Source-layer disposition | Evidence / confidence |
|---|---|---|---|---|
| U09-1 | note 4 / PDF 9, blue connector below `H_{\mathrm{int}}` | U-shaped connector; curved arrow | Draw the visible U-shaped stroke without an arrowhead. Seek a lecture frame before assigning direction. | Connector shape 0.99; absence or presence of arrowhead 0.88. |
| A8-1 | note 8 / PDF 13, covariant measure numerator | literal `d^D p^\mu`; conventional `d^D p` | Keep literal `d^D p^\mu` in `NOTES_EXACT`. Any replacement needs video evidence or the class `SOURCE_CONFLICT` / `EQUATION_NORMALIZED`. | Superscript `\mu` visible at 600--800 dpi, 0.995; mathematical intent unresolved. |
| U13-1 | note 8 / PDF 13, isolated blue curve at the page top | continuation of the p. 12 arrow; parenthetical opening stroke | Preserve it as an unlabelled curved annotation connected to the phase note. | Shape visible, 0.99; interpretation 0.78. |
| U14-1 | note 9 / PDF 14, marks after divider arrow | two apostrophe-like marks; stray pen taps; unidentified punctuation | Preserve both shapes graphically and assign no prose meaning. | Shape 0.70; meaning 0.20. |

Exact RGB values remain approximate. The semantic color assignments are resolved: gray marginalia, blue annotations and `253a`, magenta `253b`, pale-blue renormalizable grouping, lavender non-renormalizable grouping, green light cone, purple timelike path, and red forbidden path.

## Freeze gate

The note-source layer can be frozen after every `R..` item is applied, `A6-1` and `A6-2` are marked resolved in `ambiguities.md`, and the four unresolved graphical or mathematical readings remain recorded with the dispositions above. A compilation check alone will not establish source fidelity because several present defects are comments standing in for visible source marks.
