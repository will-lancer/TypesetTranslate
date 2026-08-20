# Adversarial release-pipeline audit

This review covers the strict build wrapper, the post-compile auditor, the
review-coverage contract, and the release evidence path. It does not alter
manuscript TeX or review-coverage statuses. The frozen source authority is
`origPapers/pct_spin_statistics_all_that.pdf`, SHA-256
`44fadba731cafe7f009d4e561372febb3597e1f2a4819346ce2efd16befcb889`, with 221
physical pages.

## Reproducible checks

The following checks are the repeatable pipeline checks. The first three are
tooling checks that can run while coverage is pending. The finalizer is
expected to stop until the human review records and page inspection are
complete.

| Command | Required result | Current evidence |
| --- | --- | --- |
| `sh -n build_and_verify.sh` | Exit 0 | The strict wrapper parses. |
| `python3 -m py_compile scripts/*.py tests/test_release_pipeline.py` | Exit 0 | All release tools and tests compile. |
| `python3 tests/test_release_pipeline.py` | Exit 0 | Unit tests cover the deterministic tree hash, pending coverage, warning allowlisting, FLS parsing, fixed environment, and fail-closed evidence checks. |
| `python3 scripts/check_reproducibility.py check` | Exit 0 | Two isolated fixed-environment builds must have identical bytes; the evidence records the current input-tree hash and PDF hash. |
| `python3 scripts/audit_release_pipeline.py finalize` | Exit 0 only at release closeout | It must stop on any pending coverage record, missing inspection record, warning, raster object, missing FLS input, or incomplete release evidence. |

## Findings and implemented patches

The prior audit found a positional call that passed the evidence dictionary as
the release-record path. `audit_pipeline` now calls
`release_record_failures(evidence=evidence)`, so the failure is reported as a
controlled audit result.

`build_and_verify.sh` now sources `reproducible-build.env` before compilation
and requires `python3`, `latexmk`, `tesseract`, Poppler tools, Ghostscript,
`rg`, and byte-comparison utilities. It checks that `master.log`,
`master.fls`, and `master.pdf` are nonempty before scanning them. This closes
the missing-diagnostic path that previously treated an `rg` status 2 as a
clean scan.

The strict wrapper runs the two-build reproducibility check, renders every
compiled page at 180 dpi, assembles only checksum-bound inspection parts, and
validates the complete page set. It has no independent copy or export block.
`audit_release_pipeline.py finalize` owns staging, byte comparison, release
record creation, Pass 4 creation, and the final audit. Its font parser rejects
command failure, empty output, unparseable rows, and any non-embedded or
non-subset row. Its image parser rejects every raster row; the native figure
allowlist is empty.

The finalizer also checks every expected manuscript, figure, and style path in
`master.fls`, rejects all unallowlisted compiler diagnostics, runs
Ghostscript and text extraction, rejects native placeholders and forbidden
imports, and binds the PDF, render, inspection, and export hashes. The
deterministic input-tree hash excludes generated `work/` output, TeX
auxiliaries, PDFs, and `RELEASE_VERIFICATION.md`. Coverage status values are
normalized to `pending` in that hash, which keeps the Pass 4 closeout from
creating a circular evidence dependency.

`review-coverage.json` now names the 17 disjoint source ranges, 13 figures,
four global audits, four writing-audit pass records, and four release-evidence
requirements. Each writing-audit record requires the exact fields `PASS:`,
`INPUT SNAPSHOT:`, `FULL SCOPE READ:`, `FINDINGS:`, `EDITS MADE:`,
`CHECKS RUN:`, `UNRESOLVED:`, `STATUS: PASS`, and
`Unresolved blockers: none`. The generated Pass 4 record uses that schema.
The finalizer permits only Pass 4 to remain pending during preflight, then
writes the record and closes only that status before its final audit.

## Risks and proposed operational patches

| Risk | Guard | Required follow-up |
| --- | --- | --- |
| A stale render or inspection record could describe a different PDF. | Render checksums, render-manifest checksum, compiled-PDF checksum, reviewer, timestamp, and observation are required for every page. | Re-render after the final manuscript build, then assemble all inspection parts from that manifest. |
| A partial review ledger could be mistaken for a release. | The canonical coverage manifest requires exact counts and passing statuses; only Pass 4 has a preflight exception. | Complete the 17 source ranges, 13 figures, four global audits, and four writing-audit records. |
| Environment drift could change the compiled bytes. | The wrapper sources fixed values and the double-build checker compares isolated PDFs and input-tree hashes. | Re-run the checker after the last manuscript or tooling change. |

## Remaining release conditions

The tooling has no unresolved fail-open path in the audited release sequence.
The project still requires the source-range, figure, global-audit, and pass
records to reach `pass`, together with a human-generated inspection part for
every rendered page. Those records are intentionally outside this tooling
patch and their statuses remain unchanged.

The final handoff should run the checks above again after the review records
and inspection parts are complete. A successful `finalize` run is the only
condition under which the export path is exercised.

Unresolved blockers: none
