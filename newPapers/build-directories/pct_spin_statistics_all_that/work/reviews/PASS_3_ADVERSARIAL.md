PASS: 3. Adversarial writing audit

INPUT SNAPSHOT:
- Canonical source: `../../../origPapers/pct_spin_statistics_all_that.pdf`, 221 physical pages, SHA-256 `44fadba731cafe7f009d4e561372febb3597e1f2a4819346ce2efd16befcb889`.
- Current candidate: `latex/master.pdf`, 180 A4 pages, 1,417,555 bytes, SHA-256 `4741fe42fc72801e9b3bee2249eafcd0c013b52935f78827f646c3b1b6d05735`.
- Current deterministic input-tree snapshot: SHA-256 `4a4b48934523e38f49533747917c12c6526911fb0f9551a417e256dc41ebcac8`.
- Current native-input digest: `1af48c57beaa4fe68bf7bf3f17bdebf56de614ac50e5d3b128ada2ea0264859a`.
- `review-provenance.json` binds the current source, native-input set, PDF, visual reviewer map, deterministic source renders, and the complete coverage-declared review set.

FULL SCOPE READ:
- Read the assembled `latex/master.tex` input order, all 36 native transcription chunks, all 13 native figure files, the source-marker and page-disposition records, `NOTATION.md`, the notation map, the errata and transcription ledgers, and the source-range audit packets.
- Read the release adversarial review, `build_and_verify.sh`, the post-compile audit and finalizer code, the release tests, the coverage contract, the current rendered-page manifest, and all ten page-inspection parts.
- Read all 180 checksum-bound page-inspection records. They cover PDF pages 1-180, each carries the current PDF hash, and each record has `inspected: true`.
- Checked the current PDF text and page evidence for Contents pages 3-4, the Chapter 1 bibliography on page 31, the bracketed display on output page 35, Chapter 3 locality formulas, Chapter 4 vacuum labels, Appendix references, and the Index.

FINDINGS:
- The corrected manuscript passes the Pass 3 adversarial scope. The canonical source identity, 36/36 native chunks, 211 marked source pages, strict transcription result, marker continuity, source-page authority, and packet order agree across the current ledgers.
- `work/reviews/transcription_audit.json` is strict `PASS`: 211 included pages, 211 marked pages, zero severe gaps, zero unresolved exemptions, 15 warning pages, and 36 reviewed heading candidates. The warning dispositions remain source-backed.
- Formula and notation checks found zero active unindexed `\\Psi_0` tokens. Eq. 3-46 carries `(x_j-x_{j+1})^2>0` on PDF page 108, the Chapter 3 support test uses `(x-y)^2\\leq0`, and indexed states remain present. The strict notation audit covers 49 transcription files and reports zero definite regressions. The object audit confirms the complete equation, theorem, figure, bibliography, and Index inventories.
- The 180-page inspection ledger passes against the current PDF. Rendered filenames use the padded `page-001.png` form through `page-180.png`. Contents rows and the Chapter 3 continuation appear on pages 3-4. Bibliography headings and entries remain present, including the Chapter 1 references on page 31. The closing bracket beside the display on output page 35 is present in the current extraction and page inspection.
- The release scripts preserve finalizer ownership. `audit_release_pipeline.py finalize` owns Pass 4, export staging, byte comparison, release-record writing, and the final audit. The adversarial release tests cover that ownership, padded render names, pending-coverage behavior, stale hashes, and fail-closed evidence checks.
- The strict source, transcription-review, and project commands pass against the sealed review provenance. The lower release gate still sees historical release-state records: `work/reviews/PASS_4_RELEASE.md`, `work/reviews/reproducibility.json`, and `RELEASE_VERIFICATION.md` describe the superseded PDF SHA-256 `aadf1ec4fd41cb3eabcbe8c11209b4c9ef345ecfbf1391f7abcbb649814b4d1a` and input-tree SHA-256 `48f009bbb2e9821390903cdb0e4c39e35ffe2891dc8a708659235999dde972aa`; the staged export has that same historical PDF hash. These are release-ledger refresh items. Stale packet evidence is explicitly historical and supplies zero manuscript defect.

EDITS MADE:
Only this `PASS_3_ADVERSARIAL.md` report was recreated. The manuscript, scripts, coverage, provenance, reproducibility, page evidence, export, and release records retain their existing content.

CHECKS RUN:
- `python3 scripts/audit_source.py --strict`: passed the source identity, native chunk set, marker pages, deterministic source-page rerender, and sealed review provenance.
- `python3 scripts/check_transcription_review.py --strict`: passed the strict transcription payload, all 36 reviewed dispositions, and sealed review provenance.
- `python3 scripts/audit_notation.py --strict`: passed across 49 files with the current notation map and zero definite regressions.
- `python3 scripts/audit_objects.py --strict`: passed equation ranges 1-1 through 4-101, theorem ranges, 13 figures, bibliography counts 10/25/17/30/91, and Index counts 205/24/20.
- `python3 scripts/audit_project.py --strict`: passed the 36/36 native chunk set and 438 native labels.
- `python3 scripts/render_release_evidence.py validate --input latex/master.pdf --require-inspection`: passed 180 rendered pages and 180 inspected pages. The ten inspection parts cover the same 180-page set.
- `python3 scripts/generate_review_provenance.py`: sealed the source pages, native inputs, current PDF, visual map, page evidence, and every coverage-declared review file. The strict source and transcription-review gates passed against the generated record.
- Direct `audit_pipeline(require_record=False, require_export=False, allow_pending_coverage={'pass-3-adversarial','pass-4-release','export-byte-identity'})`: manuscript and page evidence passed; remaining failures were the historical reproducibility record and historical export identity.
- `python3 tests/test_release_pipeline.py`, `python3 -m unittest discover -s tests -p 'test_*.py'`, `sh -n build_and_verify.sh`, and `python3 -m py_compile scripts/*.py tests/test_release_pipeline.py`: passed. The reproducibility checker produced two matching current-build hashes; its pre-existing historical evidence record remains the release-state item described above.
- `pdfinfo`, `pdftotext -layout`, the padded-render filename scan, source-marker scans, the PDF page-35 bracket check, and the Contents and bibliography spot checks completed against the current candidate.

UNRESOLVED:
Pass 3 has zero unresolved manuscript, formula, notation, marker, page-inspection, provenance, or adversarial-script blockers. The historical release hashes await the final release-record refresh outside this pass.

STATUS: PASS

Unresolved blockers: none
