# PASS 4 RELEASE

PASS: 4
INPUT SNAPSHOT: Source SHA-256 `44fadba731cafe7f009d4e561372febb3597e1f2a4819346ce2efd16befcb889`; input-tree SHA-256 `86ebe90b5d4d0b1c746d9591a67df9e3cc7552d43a6ea21b6f0e18688accc499`; verified PDF SHA-256 `4741fe42fc72801e9b3bee2249eafcd0c013b52935f78827f646c3b1b6d05735`; exported PDF SHA-256 `4741fe42fc72801e9b3bee2249eafcd0c013b52935f78827f646c3b1b6d05735`; compiled page count 180.
FULL SCOPE READ: `RELEASE_VERIFICATION.md`, reproducibility evidence, the rendered-page manifest, the page-inspection manifest, the recorder file, diagnostics, fonts, images, export bytes, and all 180 rendered pages were checked.
FINDINGS: The native PDF and staged export are byte-identical, reproducibility evidence matches the compiled PDF, and 180 of 180 rendered pages carry checksum-bound inspection records.
EDITS MADE: Wrote the populated release verification record and this Pass 4 record; closed the Pass 4 and export-byte coverage statuses after the export audit.
CHECKS RUN: `python3 scripts/check_reproducibility.py check`, rendered-page checksum validation, page-inspection validation, `python3 scripts/audit_release_pipeline.py finalize`, and the final release-record audit.
UNRESOLVED: none
STATUS: PASS
Unresolved blockers: none
