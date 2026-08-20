# Transcription audit infrastructure

## Scope

`scripts/audit_transcription.py` audits the native PCT edition against the
221-page canonical scan. It reads `page-dispositions.jsonl`, follows the
ordered `latex/master.tex` assembly and nested figure inputs, joins every
included PDF page to its `% PCT-SOURCE` markers, and writes the machine-readable
result to `work/reviews/transcription_audit.json`.

The source PDF has a sparse text layer. The audit uses `pdftotext` where the
layer has enough prose and falls back to the matching 180-dpi JPEG with
Tesseract. Source-image paths, extraction methods, OCR residue findings,
marker kinds, native token counts, direct recall, and boundary-aware recall
are retained per page. TeX commands and mathematics are masked for prose
comparison. Text in `\text{...}` and related prose commands remains visible.

## Exact tests

```text
python3 -m py_compile scripts/audit_transcription.py
python3 scripts/audit_transcription.py --strict
```

The strict audit was rerun on 2026-08-20 against the current
`latex/master.tex`, page ledger, source-page images, and canonical source.
The repository JSON report was left unchanged; the rerun wrote to an
isolated report root with the canonical relative review paths. It exited with
status 0. The canonical source SHA-256 was
`44fadba731cafe7f009d4e561372febb3597e1f2a4819346ce2efd16befcb889`. Its
observed checks were:

- canonical source page count `221/221`;
- native assembly of 50 TeX files;
- included source markers `211/211`;
- 211 scored pages, mean direct prose recall `0.867`, median `0.895`;
- 36 possible heading findings retained as review data;
- 15 low-recall warning pages matched the reviewed disposition set and
  warning signature;
- 94 pages with OCR residue retained as review data;
- zero severe gaps after the adjacent-page boundary check;
- zero unresolved sparse-OCR exemptions.

`build_and_verify.sh` invokes the same script before `latexmk`; strict builds
pass `--strict`, while draft builds retain the findings in the JSON report.
The existing strict `master.log` warning audit remains in place, including
duplicate-destination and PDF-string token diagnostics.

Cross-checks against the current assembly report 36/36 native chunks and 211
distinct marked PDF pages from `audit_source.py`; `audit_project.py` passes in
draft mode with 36/36 expected chunks, 36 assembly inputs, and 438 native
labels. Immediately before this record refresh,
`audit_source.py --strict` and `check_transcription_review.py --strict` both
passed against the current provenance snapshot, with all 36 reviewed heading
candidates accounted for. This Markdown record is included in the
provenance aggregate. The release owner must refresh
`review-provenance.json` after this record change; that file is outside this
task's edit scope.

The direct transcription audit remains PASS. The final disposition below
applies to that audit's scope.

Unresolved blockers: none
