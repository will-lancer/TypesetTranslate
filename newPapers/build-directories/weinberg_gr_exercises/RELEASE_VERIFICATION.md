# Release Verification

Release date: 2026-07-30 PDT

## Artifacts

- Source scan:
  `../../../origPapers/weinberg_gr.pdf`
- Restored source leaves:
  `source-supplements/`
- Exercise-ready edition:
  `../../weinberg-gr-exercises/weinberg-gr-exercises.pdf`
- Source PDF SHA-256:
  `da6fca5e44d31417e0d370108a622f9444602d68fb5768ec8edbc5b8ce5a78f9`
- Exercise-ready PDF SHA-256:
  `8646d3c2fd8336cecf4742953f85ae6698fd019ecc61e5ed21efcb437e3c2cff`
- The build master and stable export are byte-for-byte identical.
- The publisher publication-data leaf and the separate copyright-
  acknowledgements leaf are intentionally omitted from the compiled edition.

## Automated gates

The final strict execution of `./build_and_verify.sh` passed.

- The pinned 681-page source scan and all eight restored source leaves match
  their recorded SHA-256 hashes.
- All 160/160 planned content files are source-reviewed and compile-clean.
  The inventory contains 2,116 equation tags and 2,789 labels.
- `SOURCE_MANIFEST.tsv` and `TRANSCRIPTION_STATUS.md` are current.
- The notation audit reports no candidates and no definite source-era
  notation regressions.
- The index audit reports 1,207 main entries, 269 subentries, and 17
  source-page markers, with no common OCR-structure failures.
- LaTeX completes without errors, undefined references, duplicate labels or
  anchors, multiply defined references, or rerun requests.
- The layout audit reports zero overfull hboxes and one harmless underfull
  hbox.
- Text extraction succeeds; Ghostscript parses the complete PDF without
  error; every listed font is embedded and subset.
- The stable export is 4,382,524 bytes, PDF 1.7, unencrypted, and has 586 A4
  pages. `pdfinfo` reports `Suspects: no`.

## Visual QA

Every page of the exercise-ready baseline was verified pixel-for-pixel against
the fully reviewed canonical copyright-free edition. Both rendered books
contain 586 pages, with identical filenames and zero pixel mismatches.

Three extraction/crop defects found during review were corrected before
release: the missing lower labels in Figure 11.1 and retained scan prose above
Figures 14.5 and 14.9. The repaired pages and all Chapter 14 pages affected by
float repacking were re-inspected at full size. The exact final raster differs
from the previously inspected raster only on pages 10, 265, and 382--416; all
37 changed pages were separately inspected, while every other final page is
pixel-identical to its inspected predecessor.

There are no blank pages. The deliberately low-density leaves are the five
Part dividers on physical pages 10, 67, 157, 315, and 357; sparse
bibliography/reference tails and chapter-end whitespace were also checked
against their surrounding page flow.

The exercise-ready export was rendered at 110 dpi and compared with the
independently verified canonical render. No clipping, overlap, malformed text
or equations, broken figures, missing matter, bad margins, or pagination
discontinuities remain.

## Exercise infrastructure

The empty chapter hooks under `latex/exercises/` emit no material, so this
baseline remains visually identical to the canonical edition. Exercises can be
added independently for Chapters 1--16, with chapter-scoped numbering and
optional solutions as documented in `EXERCISES.md`. The strict build exports
only to `../../weinberg-gr-exercises/weinberg-gr-exercises.pdf` and cannot
overwrite the canonical PDF.

## Editorial scope

The edition uses signature `(-+++)`, time-first coordinates, compact partial
and covariant derivatives, and the notation documented in `NOTATION.md` and
`MODERNIZATION.md`.  Weinberg's action notation \(I\), \(I_M\), and \(I_G\),
and his worldline derivative \(D/D\tau\), are deliberately retained.
