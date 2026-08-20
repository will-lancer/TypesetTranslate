# Provenance and strict-release audit

This review covers the release scripts and ledgers for the native PCT edition.
It does not alter manuscript TeX.

## Checks

- `SOURCE_MANIFEST.yaml` retains the frozen SHA-256
  `44fadba731cafe7f009d4e561372febb3597e1f2a4819346ce2efd16befcb889` and the
  221-page source count. `audit_source.py` checks both values against the
  canonical PDF and against the manifest.
- `render_page_dispositions.py --strict` validates one record for each physical
  source page, rejects duplicate or out-of-range pages, requires a status and a
  reason, and rejects `pending` and `review` statuses.
- `audit_source.py --strict` requires every path in `EXPECTED_CHUNKS`, native
  source markers, valid marker pages, and non-empty content. It scans native
  chunks for facsimile imports and transcription placeholders.
- `audit_project.py --strict` checks ordered assembly, environment nesting,
  labels, static references, bibliography entries, the notation map, the page
  ledger, and every Markdown review record.
- The required-author audit now checks the source-specific keyed forms
  `\\author[a]{R. F. Streater}` and `\\author[b]{A. S. Wightman}`.
- The static label and reference census includes every native `latex/figures/*.tex`
  support file while leaving the ordered `EXPECTED_CHUNKS` assembly ledger
  unchanged.
- Every notation-map record must carry a verification status. Strict mode
  rejects `needs-correction`, `pending`, `unresolved`, and standalone `review`
  statuses.
- Review records under `work/reviews/` must contain the exact disposition line
  `Unresolved blockers: none` before strict release.
- Native figure support files under `latex/figures/` are allowed as auxiliary
  TeX inputs. Unexpected TeX elsewhere remains a release failure.
- `build_and_verify.sh` loads `reproducible-build.env` before compilation,
  requires nonempty `master.log`, `master.fls`, and `master.pdf`, and runs the
  strict evidence tools after compilation. The only export path is
  `audit_release_pipeline.py finalize`; its preflight checks the compiler log,
  recorder inputs, warnings, fonts, images, rendered pages, review coverage,
  and reproducibility evidence before it stages byte-identity checks. It
  writes the release record and closes Pass 4 only after the final audit.
- `scripts/render_release_evidence.py render` uses `pdftoppm` at 180 dpi and
  writes one PNG plus one JSONL record for every compiled-PDF page. The record
  stores pixel dimensions and a PNG checksum. Its `validate` command checks the
  page count, filenames, dimensions, checksums, and rendered-page set.
- Strict validation also requires
  `work/reviews/page-inspection.jsonl`. That file must be created after visual
  review and must carry one `inspected: true` record per rendered page, with the
  matching rendered checksum. No page is marked inspected by the tooling.
- `review-coverage.json` names the 17 source ranges, 13 figures, four global
  audits, four writing-audit pass files, and four separate release-evidence
  requirements. Required review files must contain the exact disposition line
  `Unresolved blockers: none`; every status begins as `pending`.
- `scripts/audit_release_pipeline.py` adds recorder-input, warning-allowlist,
  font, raster, deterministic-tree-hash, release-record, rendered-inspection,
  and byte-identity checks. Its dependency gate includes `tesseract` for the
  strict source transcription path. Its `finalize` command stages the export
  only after the preflight audit. The tree hash normalizes mutable review
  statuses so the final Pass 4 closeout does not invalidate recorded hashes.
- `reproducible-build.env` fixes the TeX date and locale inputs. The paired
  `scripts/check_reproducibility.py` command builds two isolated copies and
  writes evidence only when their PDF hashes agree. The strict release audit
  binds that evidence to the current tree and compiled PDF.

## Historical packet evidence

The fixed environment is recorded in `reproducible-build.env`. The packet-time
`work/reviews/reproducibility.json` record describes two matching 186-page
isolated builds, 1,419,694 bytes each, with SHA-256
`d90b8f10f7826c27a691b66139e31e5529b66e56022cf52b33c71b0d339728c2`. Those
values belong to that earlier packet build and are not the current candidate.

## Current final-candidate evidence

The current `latex/master.pdf` is an A4, 180-page PDF with SHA-256
`4741fe42fc72801e9b3bee2249eafcd0c013b52935f78827f646c3b1b6d05735`.
`work/rendered-output/manifest.jsonl` contains 180 rendered-page records and
`work/reviews/page-inspection.jsonl` contains 180/180 checksum-bound visual
records. Render validation passed against this PDF. The source identity
remains the frozen 221-page authority, and strict project audit remains
coupled to packet completion, the notation map, the page ledger, review
records, and the visual-inspection manifest.

Unresolved blockers: none
