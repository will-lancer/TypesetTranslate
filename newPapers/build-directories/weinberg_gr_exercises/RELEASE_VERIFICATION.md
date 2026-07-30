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
  `37dc345cff69e638e1ace1e1f9ab5adf37d6f27aa7984cd8ac8d9ee660c3c069`
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
- The exercise audit reports 162 exercises, 162 one-for-one solutions, and 69
  credited source labels. Chapter 1 has none; each of Chapters 2--16 has at
  least ten.
- The exercise audit excludes Cambridge Part II, covers every available
  Cambridge Part III General Relativity exam year from 2001 through 2025
  (except 2020, for which the archive has no paper), and represents all four
  Tong sheets, McGreevy problem sets 1--9, and MIT 8.962.
- The index audit reports 1,207 main entries, 269 subentries, and 17
  source-page markers, with no common OCR-structure failures.
- LaTeX completes without errors, undefined references, duplicate labels or
  anchors, multiply defined references, or rerun requests.
- The layout audit reports zero overfull hboxes and one harmless underfull
  hbox.
- Text extraction succeeds; Ghostscript parses the complete PDF without
  error; every listed font is embedded and subset.
- The stable export is 4,577,603 bytes, PDF 1.7, unencrypted, and has 650 A4
  pages. `pdfinfo` reports `Suspects: no`.
- Extracted text contains no copyright-acknowledgement, rights-reservation,
  Library of Congress, or ISBN leaf text. It also confirms fifteen complete
  Exercises--Solutions sequences before the corresponding original
  bibliographies or references.

## Visual QA

The unchanged book transcription and figures inherit the canonical edition's
completed visual review. The exercise additions were separately sampled at the
beginning, middle, and end of the book, including exercise openings, source
credits, multi-page solutions, and the transition into the original
bibliography/reference matter.

The final review included the expanded Chapter 4 Cambridge exercises and
solutions, a middle-book exercise/solution/bibliography sequence, and the
complete Chapter 16 ending. Long source credits were moved to a dedicated line
below each title after an earlier render exposed an awkward wrap. The rebuilt
pages were re-rendered and inspected at full size. No clipping, overlap,
orphaned source fragments, malformed equations, bad margins, or broken
chapter-end transitions were observed.

## Exercise infrastructure

Chapter 1 is historical and has no exercise hook. Chapters 2--16 contain 162
newly edited, source-credited exercises and 162 worked solutions. Numbering is
chapter-scoped, solutions are always printed, and every applicable chapter
orders its material as original text, Exercises, Solutions, then the original
bibliography or references.

`EXERCISE_SOURCES.md` records the graduate-source ledger and Cambridge Part III
exam-year coverage. `audit_exercises.py` enforces Chapter 1 exclusion, per-
chapter minima, one-for-one solutions, nonempty adjacent credits, Part II
exclusion, and the declared coverage. The strict build exports only to
`../../weinberg-gr-exercises/weinberg-gr-exercises.pdf` and cannot overwrite
the canonical PDF. A source scan of the sibling `weinberg_gr` tree confirms it
contains no exercise hooks or exercise environment.

## Editorial scope

The edition uses signature `(-+++)`, time-first coordinates, compact partial
and covariant derivatives, and the notation documented in `NOTATION.md` and
`MODERNIZATION.md`.  Weinberg's action notation \(I\), \(I_M\), and \(I_G\),
and his worldline derivative \(D/D\tau\), are deliberately retained.
