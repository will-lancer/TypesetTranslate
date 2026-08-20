# Transcription contract

## Scope

The reading edition reproduces the 2000 Princeton paperback of R. F. Streater
and A. S. Wightman's *PCT, Spin and Statistics, and All That*. It includes the
revised preface, Introduction, four chapters, chapter bibliographies, Appendix,
Appendix bibliography, and index.

Every sentence, displayed formula, theorem, definition, proof, quotation,
footnote, reference, and index entry carries its source meaning into the native
LaTeX edition. The printed order controls the reading order.

## Source authority

`../../../origPapers/pct_spin_statistics_all_that.pdf` is the canonical source.
Its SHA-256 is
`44fadba731cafe7f009d4e561372febb3597e1f2a4819346ce2efd16befcb889`.
Rendered page images settle wording and mathematical symbols because the PDF's
OCR layer covers only part of the front matter.

Each substantive LaTeX unit starts with a marker such as:

```tex
% PCT-SOURCE: pdf=146 print=134 kind=prose
```

The `pdf` field uses the physical PDF page. The `print` field records the
printed folio, including Roman front-matter folios. A unit spanning pages gets
one marker for each source boundary.

## Content fidelity

Preserve the authors' prose, theorem hypotheses, conclusions, proof steps,
examples, terminology, historical remarks, humor, and bibliography data.
Reflow printed line endings and remove end-of-line hyphenation when a word
continues on the next source line.

Record a clear source defect in `ERRATA.md` before changing its reading. The
record gives both page locators, the printed form, the adopted form, and the
mathematical or grammatical reason. An uncertain scan reading remains listed
in the relevant review file until direct image inspection resolves it.

## Modern notation

`NOTATION.md` controls presentation. State vectors use Dirac notation, scalar
products use bras and kets, and asymptotic labels sit outside their delimiters.
The Weinberg QFT convention supplies spacetime signature, spatial boldface,
adjoints, conjugation, identity operators, and mode energies.

Each convention change preserves the formula's mathematical statement. Metric
conversion therefore propagates through quadratic forms, Fourier phases,
spectral cones, gamma-matrix identities, and analytic continuations as one
checked system. `notation-map.jsonl` records source-specific conversions and
approved exceptions.

The authors' term `PCT` remains in theorem names and prose. AQFT objects retain
stable project macros whose meanings match the source definitions.

## Native typesetting

Body prose and mathematics use native LaTeX. Mathematical diagrams use vector
source. Raster material may represent cover art in a clearly separated
facsimile component, while the reading edition uses a native title page.

Printed equation and theorem numbers remain usable source locators. Cross
references use semantic LaTeX labels. Chapter bibliographies preserve their
local numbering, and the rebuilt index links to the new pagination.

## Review record

Each source packet produces a review file under `work/reviews/` with its page
range, completed files, notation conversions, unresolved readings, figures,
and continuity notes. Packet boundaries extend through a theorem, proof,
footnote, or sentence that crosses a page boundary.

A second reader checks every displayed formula and named result against the
rendered scan. Prose review compares each paragraph in reading order. The page
disposition ledger covers all 221 physical pages.

## Release evidence

The strict build requires the canonical source hash, complete page
dispositions, source markers, resolved review items, clean notation audits,
valid references, embedded fonts, parseable text, Ghostscript validation, and
native coverage. It rejects transcription placeholders and facsimile body
pages.

Every output page receives visual inspection after the strict build. The
release record pins the source hash, build-input hash, verified PDF hash, page
count, font report, and rendered-page manifest. The exported PDF must match the
verified build byte for byte.
