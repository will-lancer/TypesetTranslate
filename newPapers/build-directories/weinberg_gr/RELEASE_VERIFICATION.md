# Release Verification

Release date: 2026-08-01 PDT

## Artifacts

- Source scan:
  `../../../origPapers/weinberg_gr.pdf`
- Restored source leaves:
  `source-supplements/`
- Modernized edition:
  `../../weinberg-gr/weinberg-gr-modernized.pdf`
- Source PDF SHA-256:
  `da6fca5e44d31417e0d370108a622f9444602d68fb5768ec8edbc5b8ce5a78f9`
- Modernized PDF SHA-256:
  `c4a0aaf00ea9b32ab934c92b603b3bff49b49203cebd7d7d323be5fa32cb5d64`
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
- The stable export is 4,389,162 bytes, PDF 1.7, unencrypted, and has 587 A4
  pages. `pdfinfo` reports `Suspects: no`.

## Visual QA

The 2026-07-30 release completed the all-page visual review and remains the
baseline for unchanged matter. For this errata update, every affected content
location in the final export was rendered at 144 dpi and inspected at full
size: physical PDF pages 107, 178--179, 265--267, 412, 433, 511, 519--520,
523, 567, and 569. These pages cover the corrected electromagnetic equation
and current, table reference, stellar thermodynamics and volume measure,
bibliographic year, horizon, Jeans inequalities, relativistic perturbation
signs, early-universe factors, galaxy datum, and index locator.

No clipping, overlap, malformed equations, broken tables, bad margins, or
pagination discontinuities were observed on the rebuilt pages. The strict
layout gate independently reports zero overfull boxes.

## Editorial scope

The edition uses signature `(-+++)`, time-first coordinates, compact partial
and covariant derivatives, and the notation documented in `NOTATION.md` and
`MODERNIZATION.md`.  Weinberg's action notation \(I\), \(I_M\), and \(I_G\),
and his worldline derivative \(D/D\tau\), are deliberately retained.
At the user's direction, the reviewed timelike-geodesic wording following
Eq. (3.3.10) remains unchanged from the source.
