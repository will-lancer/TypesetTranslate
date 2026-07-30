# Source map

The original scan is `origPapers/weinberg_gr.pdf`. It contains 681 physical PDF
pages. Printed page numbers do not have a constant offset from physical PDF
pages because unnumbered and omitted leaves occur in the scan. Agent assignments
must therefore state physical PDF page ranges.

A complete page-sequence comparison against the matching Internet Archive scan
found eight content omissions. They are restored under `source-supplements/`:

| Missing source page | Position in local PDF | Transcription owner |
|---|---|---|
| Contents xxii | between physical pp. 19 and 20 | front matter |
| printed 306 | between physical pp. 328 and 329 | Section 11.2 |
| printed 390 | between physical pp. 413 and 414 | Section 13.3 |
| printed 392 | between physical pp. 414 and 415 | Sections 13.3--13.4 |
| printed 418 | between physical pp. 438 and 439 | Sections 14.3--14.4 |
| printed 440 | between physical pp. 463 and 464 | Section 14.5 |
| printed 594 | between physical pp. 621 and 622 | Section 15.11 |
| printed 602 | between physical pp. 628 and 629 | Chapter 15 references |

Each PNG comes from the matching edition and has an adjacent provenance file
recording the exact Internet Archive item, page mapping, extraction command,
dimensions, and SHA-256 checksum. `verify_source.py` checks the 681-page local
scan and all eight supplements.

For the combined index, the same Internet Archive item's ABBYY XML is a useful
drafting aid because its `<formatting italic="true">` spans retain the source's
selective italic publication locators. Index physical pp. 665--681 correspond
to ABBYY/DjVu objects 668--684 (zero-based), or Internet Archive PDF
pp. 669--685 (one-based). This metadata is not authoritative: every entry,
indentation level, spelling, locator, and italic span must still be checked
against the rendered source pages.

The same comparison found the following repeated local leaves. These are source
scan defects, not extra book content; transcribe each printed page once.

| Physical PDF pages | Repeated content |
|---|---|
| 2 and 4 | copyright page |
| 3 and 5 | dedication |
| 43 and 45; 44 and 46 | printed pp. 18--19 |
| 153 and 155 | printed p. 128 |
| 310 and 312; 311 and 313 | printed pp. 288--289 |
| 402 and 404; 403 and 405 | printed pp. 382--383 |
| 406 and 408; 407 and 409 | printed pp. 384--385 |
| 442 and 444; 443 and 445 | printed pp. 422--423 |
| 460 and 462; 461 and 463 | printed pp. 438--439 |
| 491 and 492 | printed p. 468 |
| 526 and 528; 527 and 529 | printed pp. 502--503 |
| 538 and 540; 539 and 541 | printed pp. 512--513 |
| 636 and 637 | Chapter 16 opening, printed p. 611 |

All discontinuities in the monotone page sequence were visually classified as
one of the eight restored content leaves, one of the repeated leaves above, or
an intentionally blank/divider leaf.

The table below records the book's printed-page starts from the contents pages.
It is an orientation aid, not a physical-page manifest.

| Chapter | Title | Printed start |
|---:|---|---:|
| 1 | Historical Introduction | 3 |
| 2 | Special Relativity | 25 |
| 3 | The Principle of Equivalence | 67 |
| 4 | Tensor Analysis | 91 |
| 5 | Effects of Gravitation | 121 |
| 6 | Curvature | 131 |
| 7 | Einstein's Field Equations | 151 |
| 8 | Classic Tests of Einstein's Theory | 175 |
| 9 | Post-Newtonian Celestial Mechanics | 211 |
| 10 | Gravitational Radiation | 251 |
| 11 | Stellar Equilibrium and Collapse | 297 |
| 12 | The Action Principle | 357 |
| 13 | Symmetric Spaces | 375 |
| 14 | Cosmography | 407 |
| 15 | Cosmology: The Standard Model | 469 |
| 16 | Cosmology: Other Models | 611 |
| Appendix | Some Useful Numbers | 635 |
| Index | Index | 641 |

Front matter includes the title page, dedication, preface, notation, contents,
and copyright acknowledgements. The main text is divided into:

1. Preliminaries
2. The General Theory of Relativity
3. Applications of General Relativity
4. Formal Developments
5. Cosmology

Before dispatching transcription, render the source at a consistent resolution
and create a physical-page manifest. A typical command is:

```bash
mkdir -p artifacts/pages
pdftoppm -png -r 200 ../../../origPapers/weinberg_gr.pdf artifacts/pages/page
```

Do not commit the rendered page images unless explicitly desired; they will be
large and are derived from the immutable source PDF.
