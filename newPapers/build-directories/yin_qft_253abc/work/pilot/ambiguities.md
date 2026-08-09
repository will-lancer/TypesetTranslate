# Note-transcription ambiguities

Source: `qft_253abc_book.pdf`, physical pages 6--14, original Physics 253a
note pages 1--9. The source hash matches `SOURCE_MANIFEST.yaml`.

Every open entry records the visual reading kept in `notes-exact.tex`.
Resolved readings and possible printed-layer normalizations are recorded in
separate sections so that neither changes the exact source layer.

## Open source-layer ambiguities

| ID | Note p. | PDF p. | Location / ink | Competing readings | Exact-layer disposition | Confidence | Basis |
|---|---:|---:|---|---|---|---:|---|
| U09-1 | 4 | 9 | Blue stroke between `H_{\mathrm{int}}` and the blue monomials | U-shaped connector; curved arrow | Draw the visible U-shaped stroke without an arrowhead. | 0.99 shape; 0.88 terminal | The enlarged page fixes the U shape. A lecture frame is needed to assign an arrowhead and direction. |
| A8-1 | 8 | 13 | Numerator of the covariant momentum measure | Literal `d^D p^\mu`; conventional `d^D p` | Keep literal `d^D p^\mu`. | 0.995 ink | The raised `\mu` after `p` is distinct at 600--800 dpi. Its mathematical intent remains unresolved. |
| U13-1 | 8 | 13 | Isolated blue curve at the page top | Continuation of the page-12 phase arrow; parenthetical opening stroke | Preserve an unlabelled curved annotation beside the phase definitions. | 0.99 shape; 0.78 interpretation | The stroke is clear and has no matching closing parenthesis. |
| U14-1 | 9 | 14 | Two marks after the horizontal divider arrow | Apostrophe-like marks; stray pen taps; unidentified punctuation | Preserve both shapes graphically and assign no prose meaning. | 0.70 shape; 0.20 meaning | The two small terminal marks remain visible in the 500-dpi render. |

## Resolved readings

- `A6-1`: the blue metric signature is the explicit four-entry diagonal
  signature `\operatorname{diag}(-1,1,1,1)`. The staggered entries form a
  diagonal layout inside large parentheses. Confidence 0.99.
- `A6-2`: the faint final algebra line reads
  `-i(\eta^{\nu\rho}J^{\mu\sigma}-\eta^{\mu\rho}J^{\nu\sigma}
  -(\rho\leftrightarrow\sigma))`. Both metric indices and both displayed
  minus signs resolve at 1200 dpi. Confidence 0.99.
- Creator superscripts on note pages 3, 4, and 7 are literal `+` marks. The
  exact layer uses `a^+` in every corresponding operator and product.
  Confidence 0.995 on note page 7 and 0.95 across the matching earlier glyphs.
- The equal-time proof on note page 8 contains vector accents over
  `\vec x`, `\vec y`, and `\vec p`, plus the momentum-reversal arrow in
  `\vec p\to-\vec p`. Blank space precedes both proof lines. A leading
  implication arrow is absent. Confidence 0.97.

## Printed-layer normalization recommendations

These recommendations do not authorize a change to `notes-exact.tex`.

- The creator mark has adjoint meaning. A printed or canonical layer may
  render each literal `a^+` as `a^\dagger` when the change is recorded as
  `EQUATION_NORMALIZED`.
- The covariant measure would conventionally read `d^D p`. Replacing the
  literal `d^D p^\mu` requires video evidence or an explicit
  `SOURCE_CONFLICT` or `EQUATION_NORMALIZED` record.

## Resolved zoom checks

- Note p. 4 / PDF p. 9: the first equal-time relation reads
  `[a,a]=[a^+,a^+]=0`, confidence 0.99 for the full reading and 0.95 for the
  literal creator glyph.
- Note p. 4 / PDF p. 9: the blue examples below `H_{\mathrm{int}}` read
  `a^+a^+a,\ aaa^+,\ldots`, confidence 0.98 for the products and 0.95 for the
  literal creator glyph.
- Note p. 6 / PDF p. 11: the faint gray mixed commutator reads
  `[P^\mu,J^{\rho\sigma}]=-i(\eta^{\mu\rho}P^\sigma-(\rho\leftrightarrow\sigma))`,
  confidence 0.97.
