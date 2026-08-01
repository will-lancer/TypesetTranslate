# Release verification

Status: **work in progress**

Canonical source: `../weinberg_vol3`

Verified errata export:
`../../weinberg-qft-exercises/weinberg-vol3-exercises.pdf`

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
errata-build hash is recorded separately below.

## 2026-08-01 errata rebuild

The inherited four-component text was synchronized with the correction set in
`../weinberg_vol3/ERRATA.md` and rebuilt successfully.

- Canonical PDF: 373 pages, SHA-256
  `e031856555caaca5425dd7c4539652a95f6f129b5998b4344871b7f6b3db84e2`.
- Exercise PDF: 541 pages, SHA-256
  `7da395ae65c738bc13bc03b52ece291e797315c64d0a5cce482b2e27c66a19ff`.
- Both PDFs passed LaTeX error/reference checks, text extraction, Ghostscript
  interpretation, embedded/subset-font checks, and affected-page visual QA.
- The exercise PDF also has zero overfull boxes.
- The final integration check corrected the free/summed gauge-index flow in
  the post-(27.4.19) mass-matrix relation and visually rechecked that page in
  the canonical and exercise PDFs.

The strict exercise-content gate still fails on pre-existing editorial audit
state outside this errata port: one stale Weinberg-prompt hash, five unknown
source IDs, incomplete/obsolete source-fidelity records (including 59 records
not yet passed), and unused ledger entries. Canonical-source and canonical-PDF
isolation hashes are current and pass. A stable exercise PDF was refreshed for
the requested errata port, but the overall edition remains work in progress.
