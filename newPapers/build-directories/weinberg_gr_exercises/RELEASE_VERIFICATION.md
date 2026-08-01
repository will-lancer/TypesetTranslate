# Release Verification

Release date: 2026-08-01 PDT

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
  `d6023f924ef32dbe0b95cf910839b6d441f646692ea38b1b9b359f6475df5b6f`
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
- The exercise audit reports 300 exercises, 300 one-for-one solutions, and 79
  credited source labels. Chapter 1 has none; each of Chapters 2--16 has
  exactly twenty.
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
- The stable export is 4,719,540 bytes, PDF 1.7, unencrypted, and has 694 A4
  pages. `pdfinfo` reports `Suspects: no`.
- Extracted text contains no copyright-acknowledgement, rights-reservation,
  Library of Congress, or ISBN leaf text. It also confirms fifteen complete
  Exercises--Solutions sequences before the corresponding original
  bibliographies or references.

## Visual QA

The exercise additions retain their completed release review. For this errata
update, every affected book-content location in the final exercise export was
rendered at 144 dpi and inspected at full size: physical PDF pages 121,
220--222, 331--333, 505, 527, 605, 613--614, 617, 674, and 676. These pages
cover the same corrections as the canonical edition while accounting for the
exercise edition's expanded pagination.

No clipping, overlap, malformed equations, broken tables, bad margins, or
exercise/book transition defects were observed on the rebuilt pages. The
strict exercise and layout gates both pass, with zero overfull boxes.

## Exercise infrastructure

Chapter 1 is historical and has no exercise hook. Chapters 2--16 each contain
20 newly edited, source-credited exercises and 20 worked solutions, for 300 of
each overall. Numbering is chapter-scoped, solutions are always printed, and
every applicable chapter orders its material as original text, Exercises,
Solutions, then the original bibliography or references. The second curated
set is kept in reviewable fragments under `latex/exercises/additional/`.

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
At the user's direction, the reviewed timelike-geodesic wording following
Eq. (3.3.10) remains unchanged from the source.
