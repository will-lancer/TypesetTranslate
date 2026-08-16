# Zhou quantitative-finance JHEP release verification

Status: verified for release on 2026-08-15 PDT.

## Release artifact

- File: `../../zhou-quantitative-finance-interviews/zhou-quantitative-finance-interviews-jhep.pdf`
- SHA-256: `325b3a769c8d62787624a54273fd9cc5680684d488e0578a77e1cdcd5b192e6c`
- Extent: 176 A4 pages; 1,426,663 bytes; PDF 1.7; unencrypted
- Extracted text: 78,006 words
- Extracted-text SHA-256: `984551c01ecd558439a37269f85ccc7f1663bc2b0d72aa66423fa5ffaffb683c`
- Authoritative source: `source/zhou-quantitative-finance-interviews.pdf`
- Source SHA-256: `a31f318b4d017d9eab7887cd91b9f5ca65542e6b31bce541039e2ef24828d026`
- Source extent: 212 physical PDF pages
- `latex/master.pdf` and the stable export are byte-for-byte identical.

## Release gates

- [x] The frozen source checksum and 212-page extent pass verification.
- [x] The source map accounts for all leaves: 196 included pages, 7 replaced
      front-matter pages, and 9 omitted blank or cover leaves.
- [x] Forty-two native transcription chunks cover every included source page
      exactly once and compile in source order.
- [x] The strict transcription audit passes. Mean prose-token recall is 0.896,
      with median 0.924. Eleven low-recall warnings received source-image
      review; none is a severe gap.
- [x] All source footnotes use explicit source numbers. Display-level markers
      stay attached to their formulas.
- [x] The notation audit passes. Its two reported slash-abbreviation review
      candidates are the source terms `pmf/pdf`.
- [x] The edition contains 32 native figures and 8 native tables. The final PDF
      contains no raster image objects or imported source pages.
- [x] LaTeX reports no errors, unresolved references, duplicate references,
      rerun requests, or overfull boxes. Three underfull hboxes and five
      underfull vboxes are visually benign.
- [x] Ghostscript parses the complete PDF. Poppler extraction succeeds.
      All 49 listed fonts are embedded and subset.

## Visual QA

Every output page received visual inspection in non-overlapping page lanes.
The review covered text flow, equations, figures, tables, captions, footnotes,
code listings, margins, headers, and page continuations. Corrections from that
review include the rebuilt Figure 2.1 tree, separated Figure 5.4 arrows,
stable Chapter 4 and Chapter 6 table floats, native Figures 5.10 and 5.11,
formula-bound footnotes, and kept-together solution headings.

The exact release export received a final rendered check on physical PDF pages
54, 89--90, 107--109, 118, and 176. These pages cover the last footnote-anchor
change, repaired Dice-game break, Chapter 5 footnote sequence, dynamic-card
equation note, and closing index page. The rendered pages are clear and stay
inside the JHEP text block.
