# Release verification

Status: **work in progress**

Canonical source: `../weinberg_vol2`

Verified errata export:
`../../weinberg-vol2-exercises.pdf`

## 2026-08-01 errata rebuild

The 55 shared corrections in `../weinberg_vol2/ERRATA.md` were mirrored into
this edition, together with one exercise-only determinant-expansion repair.

- Canonical PDF: 434 pages, SHA-256
  `facaa63bd5c9610969e43ae56933d913eb038af82d0e802147e6466dee84f279`.
- Exercise PDF: 679 pages, SHA-256
  `3a9c8e7e6b7ecfd5f2162191a0b7a4d5c0acd55f17888a47a81f634268b99066`.
- The 75-assertion errata regression passes.
- Both PDFs passed LaTeX error/reference checks, text extraction, Ghostscript
  interpretation, embedded/subset-font checks, and affected-page visual QA.
- The exercise PDF has zero overfull boxes.

The strict exercise-content gate remains blocked by unrelated pre-existing
editorial state: stale canonical and prompt hashes, stale source-fidelity
fields, 55 source-fidelity records not yet passed, and unused ledger entries.
Only hashes attributable to this errata work were refreshed. The physical PDF
checks pass, but the overall exercise edition remains work in progress.

The final strict-release record will include:

- chapter-by-chapter W/S exercise and solution counts;
- sources represented and any justified chapter count exceptions;
- full-volume page count;
- strict audit, LaTeX reference, layout, PDF parse, and font results;
- representative visual-QA pages from the beginning, middle, and end;
- a supplementary-solutions-to-original-references transition check;
- visual verification of both inherited-index pagination notices and the
  generated source/displayed-label/physical-PDF crosswalk;
- the series-wide supplementary duplication audit;
- build/export identity and SHA-256.

No strict-release hash is recorded until every strict gate passes; the verified
errata-build hash is recorded separately above.
