# Wald GR modernization policy

The target is Wald's text, reasoning, and mathematical content with the
specific notation changes in `NOTATION.md`. It is not a rewritten GR textbook.

## Permitted changes

- Apply the binding notation conversions in `NOTATION.md`.
- Remove scan-induced line-break hyphenation.
- Normalize LaTeX typography, spacing, quotation marks, and cross-references.
- Correct “Lorentz gauge” to “Lorenz gauge” and use de Donder or harmonic
  gauge for the gravitational condition.
- Recreate geometric line figures in TikZ when their content is unambiguous.
- Correct an actual source error only after explicit review; retain a nearby
  `% SOURCE ERRATUM:` comment recording the printed form.

## Prohibited silent changes

- Do not replace abstract indices by component notation.
- Do not change Wald's Riemann tensor convention or index order.
- Do not remove the Chapter 13 signature change.
- Do not change the meaning of (\partial_a).
- Do not change the pushforward/pullback convention.
- Do not replace Wald's proofs with more recent proofs.
- Do not update historical claims, experimental data, or bibliographic
  judgments without a separately authorized editor's note.
- Do not silently alter extrinsic-curvature or ADM signs.

Suspected source errors retained after checking the printed page are marked
`% SOURCE VERIFIED:`. Any unresolved modernization question would be marked
`% MODERNIZATION CHECK:` and would block release.
