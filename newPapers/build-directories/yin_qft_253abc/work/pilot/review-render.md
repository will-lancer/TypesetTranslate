# Render review: Chapter 1 written edition

Review status: PASS

Chapter SHA-256:
`df431b6e60ee29d489a91eaa4beb9fc9c61ec198b0cdf5acd8d393996090ec82`

PDF SHA-256:
`ae874ea093e48619a2c369ffe3be12b424ebaf69798ed1a2bd7ebcf69d355a14`

Render manifest SHA-256:
`935669ce833e2820c5c6d569ba2d11b9e6e37733827ef61d3c4f807aff5f1f8e`

The written edition compiles reproducibly to 13 A4 pages. Every page in the
hash-addressed render directory recorded by `render-manifest.json` was
inspected at 180 dpi. Paragraph flow, section breaks, equation placement,
figures, captions, links, and the final problem-set note are readable and
unclipped.

The QFT concept map remains legible at its first point of use. The light-cone
figure retains the source geometry and color distinctions. Long equations are
displayed, including the coordinate transformation, Lorentz metric condition,
generator formulas, free Hamiltonians, scalar-field expansion, and commutator
integrals.

The build log contains no overfull boxes, underfull boxes, undefined
references, missing glyphs, or fatal errors. All fonts are embedded and
subset. Ghostscript and `pdftotext` process the PDF successfully. Two forced
builds produced the same PDF hash recorded above.

Unresolved blockers: none
