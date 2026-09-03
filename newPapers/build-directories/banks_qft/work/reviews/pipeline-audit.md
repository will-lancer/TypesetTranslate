# Pipeline audit

> Historical pre-adaptation audit. The 2026-09-02 convention release replaces
> its authorization state with current checksum-bound release records. The
> findings below remain the design provenance for the strengthened scripts.

Audit date: 2026-09-02. Scope: the pasted Banks QFT release plan and the
current `banks_qft` package. The source hash and pinned JHEP style checks pass.
The shell and Python entry points parse successfully. A complete release build
was not available during this audit because the solution and review waves were
still open.

## Findings

### P1. The strict audit does not enforce the master input closure

`scripts/audit_project.py:60-73` reads every `.tex` file below `latex`, while
`scripts/audit_project.py:119-133` checks only the paths currently named by
`book.tex`. `scripts/audit_compiled_dependencies.py:19-42` requires the common
styles and the expanded exercise files, but it has no exact expected native
input set for either master.

An input can be removed from `book.tex` while its orphaned file still supplies
source markers, problems, solutions, labels, figures, or bibliography entries
to the recursive lexical audits. The compiled dependency manifest records what
was reached, yet no strict check compares that closure with the required source
map. A chapter or solution can therefore disappear from the PDF while the
structural audit remains green.

The strict gate needs an expected closure for each entry point. Inventory,
marker, object, and solution checks should run on that closure, with every
required native file and nested figure input required to be reachable from the
selected master.

### P1. Text recall is global and prose-only

In `scripts/audit_text_recall.py:49-62`, all output words are merged into one
`output_words` sequence and every source-page shingle is searched in that global
set. The page number does not constrain the match. The token expression at
`scripts/audit_text_recall.py:28-32` also drops Greek letters, operators,
mathematical symbols, and most display structure.

An omitted or misplaced source page can pass when its prose appears elsewhere in
the output. Missing or altered mathematics receives no recall penalty. The
strict invocation in `build_and_verify.sh:104-112` uses this same evidence.
Page-local comparison, source-marker order checks, and an equation/display
inventory are needed for the transcription gate.

### P1. Source and solution review ledgers are self-attested

`scripts/audit_project.py:278-320` accepts `review-coverage-<edition>.json`
after checking a source hash, counts, ranges, and reviewer-name strings.
`scripts/audit_project.py:321-335` accepts the solution ledger from an edition
field, an `80/80` string, and two distinct names. Neither path requires the
review files named by the ledger, a review-file checksum, a passing status, or a
problem/equation record set.

A hand-written JSON object can claim two reviewers and complete coverage without
evidence from either reader. The strict gate needs a versioned schema with
required report paths, hashes, statuses, and coverage IDs, followed by checks
that those reports bind to the current native input snapshot.

### P1. Visual review records can be generated as passes, with no reviewer-count gate

`scripts/render_release.py:114-140` writes `status: "pass"` for every requested
page. `scripts/render_release.py:169-200` checks checksums and page coverage,
but it accepts one reviewer for the whole output and does not require a
non-empty observation in a manually supplied record. `build_and_verify.sh:134-147`
only collects JSONL files and invokes that validator.

One call to the `record` subcommand can produce a passing record for every page
under an arbitrary reviewer string. The plan calls for disjoint visual-review
lanes. The strict validator should require assigned reviewer ranges, at least
the planned independent reviewer identities, and structured observations tied
to each inspected page.

### P1. The base-freeze boundary trusts two mutable hashes

`build_and_verify.sh:52-64` checks only that `base-freeze.json` is non-empty
before the implicit build. `scripts/verify_base_freeze.py:19-24` compares the
current rebuild with `output_sha256` and `build_input_sha256`, without checking
the frozen record's schema, status, canonical source hash, release path, page
count, or release-copy identity.

An edited or incomplete freeze record can authorize implicit work. The verifier
should require a passing record with all expected identity fields and compare
the frozen release PDF at `newPapers/banks-qft/banks-qft-exercise-edition.pdf`
as well as the rebuilt base output.

### P2. The build-input hash silently omits classes, configuration, and external inputs

`scripts/build_input_manifest.py:24-41` ignores every recorded input outside
the package root, silently skips missing paths, and hashes only `.tex`, `.sty`,
and `.bib` files. `scripts/check_reproducibility.py:49-57` copies that same
subset into its isolated builds. A local `.cls`, `.cfg`, `.fd`, or other
build-relevant file is outside the hash; a system package can change without
appearing in the manifest. A generated `.tex` file is admitted whenever the
master reaches it.

The manifest should fail on unexpected or missing local inputs, record all
build-relevant extensions, and state the TeX engine/package identity used by
the isolated rebuild.

### P2. The declared source render has no strict provenance check

`SOURCE_MANIFEST.yaml:12-22` declares the shared 150-DPI render and extracted
assets authoritative. `scripts/verify_source.py:19-35` verifies only the source
PDF hash, page count, page size, and local JHEP style hash. No strict step
checks that the shared render exists, contains 281 pages, uses the declared
crop box and DPI, or matches the frozen source. The source-review report also
refers to a temporary 300-DPI directory without an image hash.

The review evidence should include a deterministic source-render digest and a
rerender check before a source-review ledger can pass.

### P2. Text-recall evidence is not bound to the PDF it describes

`scripts/audit_text_recall.py:76-85` writes edition, page records, thresholds,
and status, but no source-PDF or output-PDF hash. `scripts/finalize_release.py:64-74`
checks only the edition and passing status for this evidence. The build script
regenerates it immediately before finalization, which narrows the operational
risk, yet a stale record remains acceptable to the finalizer interface.

The evidence schema should carry both hashes, and finalization should compare
the output hash with the compiled PDF.

### P2. Query-ledger closure is a substring test

`scripts/audit_project.py:278-280` passes whenever the text
`No unresolved readings.` appears anywhere in `QUERY_LEDGER.md`. It does not
parse entries or reject unresolved material below that line. The strict gate
therefore cannot establish the plan's zero-unresolved-query requirement.

Use a structured query ledger with explicit entry statuses and require every
entry to be closed before release.

### P2. The contract, notation, errata, and status ledgers are not release inputs

The package documents these requirements in `TRANSCRIPTION_CONTRACT.md` and
`AUTHORING_CONVENTIONS.md`, while `TRANSCRIPTION_STATUS.md:3-15` still reports
production as open. No strict script validates those files or requires the
status ledger to state a completed release. `finalize_release.py:106-115`
hard-codes several audit summaries instead of deriving them from the ledgers.

The release record should bind the contract/notation/errata/status snapshots,
or the strict pipeline should validate their required fields directly.

## Checks run

- `python3 scripts/verify_source.py`: pass, 281 pages and the expected source
  and JHEP hashes.
- `python3 scripts/render_page_dispositions.py`: pass, 281/281 records with
  271 native, 4 generated, and 6 omitted pages.
- `sh -n build_and_verify.sh`: pass.
- `python3 -m compileall -q scripts`: pass.
- Draft structural audits ran with the expected in-progress warnings for the
  unfinished Chapter 9 solution and implicit solution files. Strict review
  ledgers and final PDFs were not yet present.

## Verdict

The current pipeline has release-blocking fail-open paths in master closure,
text recall, review provenance, visual review, and base-freeze verification.
The source identity, page-disposition, pinned-style, and command-syntax checks
are sound for the current package snapshot.
