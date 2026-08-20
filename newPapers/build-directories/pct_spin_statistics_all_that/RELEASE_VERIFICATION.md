# Release verification record

This record was written by `scripts/audit_release_pipeline.py finalize` after
the strict post-compile checks completed. The source PDF remains the authority
named in `SOURCE_MANIFEST.yaml`.

## Identity

- Source PDF: `../../../origPapers/pct_spin_statistics_all_that.pdf`
- Source SHA-256: `44fadba731cafe7f009d4e561372febb3597e1f2a4819346ce2efd16befcb889`
- Input-tree definition: deterministic SHA-256 over sorted relative paths and
  file-content hashes, excluding generated files under `work/`, TeX auxiliary
  output, PDFs, and this release record. Mutable `status` values in
  `review-coverage.json` are normalized to `pending`.
- Input-tree SHA-256: `86ebe90b5d4d0b1c746d9591a67df9e3cc7552d43a6ea21b6f0e18688accc499`
- Verified build PDF: `latex/master.pdf`
- Verified PDF SHA-256: `4741fe42fc72801e9b3bee2249eafcd0c013b52935f78827f646c3b1b6d05735`
- Exported PDF: `../../pct-spin-statistics-all-that/pct-spin-statistics-all-that.pdf`
- Exported PDF SHA-256: `4741fe42fc72801e9b3bee2249eafcd0c013b52935f78827f646c3b1b6d05735`
- Byte identity: PASS (staged export and verified build compared byte-for-byte)

## Build

- Build command: `./build_and_verify.sh`
- Fixed build environment: `SOURCE_DATE_EPOCH=946684800`, `FORCE_SOURCE_DATE=1`, `TZ=UTC`, `LC_ALL=C`
- Build date: `2026-08-20T21:51:51+00:00`
- Native PDF page count: `180`
- Double-build reproducibility: PASS (two isolated builds have the same PDF SHA-256)
- Ghostscript parse check: PASS
- Extracted text check: PASS (421110 characters)
- Warning disposition: PASS (none)

## Fonts and native inputs

- Font embedding and subsetting: PASS (50 font rows; every row is embedded and subset)
- Full-page raster check: PASS (0 embedded raster objects)
- Facsimile or source-PDF import check: PASS (all expected local inputs appear in master.fls)
- Native chunk audit: PASS (review-coverage source and figure records are complete)
- Notation audit: PASS (review-coverage notation record is complete)
- Reference audit: PASS (review-coverage citation record is complete)

## Rendered-page inspection

- Render command: `python3 scripts/render_release_evidence.py render --input latex/master.pdf`
- Rendered output directory: `work/rendered-output/`
- Page manifest: `work/rendered-output/manifest.jsonl`
- Inspection manifest: `work/reviews/page-inspection.jsonl`
- Render DPI: `180`
- Pages rendered: `180`
- Pages visually inspected: `180`
- Inspection result: PASS
- Inspection notes: none recorded by the page reviewers

## Sign-off

- Reviewer: visual_pages_001_019, visual_pages_020_038, visual_pages_039_057, visual_pages_058_076, visual_pages_077_095, visual_pages_096_114, visual_pages_115_133, visual_pages_134_152, visual_pages_153_170, visual_pages_171_186
- Review date: 2026-08-20
- Release disposition: PASS
