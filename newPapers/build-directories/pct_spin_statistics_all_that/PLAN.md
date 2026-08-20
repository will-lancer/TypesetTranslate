# Typesetting plan: PCT, Spin and Statistics, and All That

## Target

Create a native LaTeX edition of R. F. Streater and A. S. Wightman's *PCT,
Spin and Statistics, and All That*. The edition will follow the printed text
closely while applying the QFT notation used in the repository's Weinberg
edition. The final PDF should read as a careful re-typesetting of the book.

The source prose, chapter order, theorem sequence, proofs, epigraphs,
footnotes, bibliographies, appendix, and index all belong in the new edition.
The notation policy below governs mathematical presentation. `ERRATA.md` will
record every accepted correction to the printed source.

## Source baseline

The canonical oldpaper is
`../../../origPapers/pct_spin_statistics_all_that.pdf`.

| Property | Verified value |
| --- | --- |
| Edition | Princeton University Press paperback, 2000, with revised preface and corrections |
| Physical PDF pages | 221 |
| Printed main-text span | 1-207 |
| SHA-256 | `44fadba731cafe7f009d4e561372febb3597e1f2a4819346ce2efd16befcb889` |
| PDF page size | 431 x 657 pt |
| Source type | Scanned pages with a sparse OCR layer |

Printed page 1 appears on PDF page 13. The useful page anchors are:

| Material | Printed page | PDF page |
| --- | ---: | ---: |
| Contents | v | 7 |
| Preface | vii | 9 |
| Introduction | 1 | 13 |
| Chapter 1 | 4 | 16 |
| Chapter 2 | 31 | 43 |
| Chapter 3 | 96 | 108 |
| Chapter 4 | 134 | 146 |
| Appendix | 179 | 191 |
| Index | 205 | 217 |

The OCR layer can seed searches in the front matter. Page images remain the
authority for words, symbols, accents, equation layout, footnotes, and page
boundaries.

## Local references

Use these files as the house style:

- `../weinberg_vol1/latex/master.tex` supplies the JHEP layout, title-page
  treatment, links, chapter breaks, and reusable state macros.
- `../weinberg_vol1/latex/frontmatter/notation.tex` gives the primary QFT
  convention.
- `../weinberg_vol1_exercises/NOTATION.md` gives the audit-friendly version of
  that convention.

The PCT project will keep its own `NOTATION.md`. It should quote each adopted
rule in operational form and list every book-specific decision.

## Editorial contract

Transcribe the printed wording sentence by sentence. Preserve spelling,
capitalization with mathematical meaning, named results, examples, quotations,
and authorial asides. Reflow line breaks and hyphenation for native LaTeX.

Clear print defects go into `ERRATA.md` with the PDF page, printed page, source
reading, adopted reading, and reason. A doubtful reading stays tied to a
review item until the page image settles it.

Place a source marker before each substantive paragraph, display, theorem,
footnote, bibliography block, and index block:

```tex
% PCT-SOURCE: pdf=146 print=134 kind=prose
% PCT-SOURCE: pdf=146 print=134 kind=theorem id=4-1
```

Build a page-disposition ledger that covers all 221 PDF pages, including
covers and blanks. The ledger will classify each page as transcribed,
represented elsewhere, intentionally omitted from the reading edition, or
pending review. Each classification needs a short reason.

## Notation policy

Adopt the Weinberg QFT conventions where the conversion preserves the stated
mathematics. Record conversions in `notation-map.jsonl`, keyed by source page
and formula or prose locator.

| Topic | House form | Required check |
| --- | --- | --- |
| State vector | `\ket{\Psi}` | Distinguish states from test functions and field components. |
| Hilbert product | `\braket{\Phi}{\Psi}` | Confirm the source's argument order before conversion. |
| Matrix element | `\bra{\Phi}A\ket{\Psi}` | Check domains whenever an unbounded operator appears. |
| In/out state | `\InKet{\alpha}`, `\OutBra{\beta}` | Keep asymptotic labels outside delimiters. |
| Spacetime metric | `\eta=\operatorname{diag}(-1,+1,+1,+1)` | Audit cones, spectral support, Fourier phases, and every use of `x^2`. |
| Spatial vector | `\mathbf{x}` | Reserve hats for unit vectors. |
| Mode energy | `\omega_{\mathbf p}` | Preserve total-energy symbols and spectral variables according to role. |
| Adjoint | `A^\dagger` | Classify source stars as adjoint, conjugate, or dual before changing them. |
| Complex conjugate | `A^*` | Check anti-linear maps and analytic continuations separately. |
| Identity | `\mathbf{1}` | Keep identity representations distinct through subscripts. |
| Script alphabet | `\mathcal{H}`, `\mathcal{P}(O)` | Give each space and algebra one stable macro. |
| PCT terminology | `PCT` | Preserve the authors' theorem name and ordering. |

AQFT-specific symbols need a project glossary. It should cover test-function
spaces, tempered distributions, tubes and extended tubes, Wightman functions,
polynomial algebras of open sets, Borchers classes, spectral supports, and
superselection sectors. Each macro gets one meaning throughout the book.

Use chapter-based source numbering. Equations should render as `(2-1)`,
`(2-2)`, and so on, while theorem labels should render as `Theorem 4-1`.
LaTeX labels will carry semantic names such as
`eq:ch2-delta-derivative` and `thm:global-locality`.

## Planned project tree

```text
pct_spin_statistics_all_that/
  PLAN.md
  README.md
  SOURCE_MANIFEST.yaml
  SOURCE_MAP.md
  NOTATION.md
  ERRATA.md
  TRANSCRIPTION_STATUS.md
  notation-map.jsonl
  page-dispositions.jsonl
  build_and_verify.sh
  scripts/
    audit_source.py
    audit_notation.py
    audit_project.py
    render_source_map.py
  latex/
    jheppub.sty
    master.tex
    pct.sty
    frontmatter/
    chapters/
      chapter01/
      chapter02/
      chapter03/
      chapter04/
    appendix/
    backmatter/
  work/
    source-pages/
    reviews/
```

The source PDF stays in `origPapers`. Rendered source pages and review images
belong under `work/`, and build artifacts stay out of the content tree.

## Execution sequence

### 1. Freeze and map the source

Write `SOURCE_MANIFEST.yaml` with the source path, hash, edition statement,
page count, and page offset. Render every page once at review resolution.
Create `SOURCE_MAP.md` from the printed contents, then enumerate front matter,
sections, theorem ranges, equation ranges, figures, notes, bibliography pages,
and index pages.

### 2. Build the native scaffold

Copy the local `jheppub.sty` from the Weinberg Volume I project. Create an A4,
11 pt `master.tex` with the same link treatment and title-page spacing. Add
`pct.sty` for state notation, AQFT spaces, theorem environments, source-style
numbering, and repeated analytic-domain symbols.

Compile a short pilot containing the title, contents, the Introduction, and
the opening two pages of Chapter 1. Compare the pilot with the source at normal
reading size before fixing the page geometry and display spacing.

### 3. Transcribe in proof-sized packets

Work through contiguous packets of roughly five printed pages. Extend a packet
when a theorem or proof crosses its boundary. Every packet receives page
markers, an equation inventory, a notation-map update, and a focused visual
review.

The reading order is front matter, Introduction, Chapters 1 through 4,
Appendix, chapter bibliographies, and Index. Preserve the source's section
boundaries. Typeset equations from the scan while using OCR only as a locator.

### 4. Apply the notation pass

Review each completed chapter against `NOTATION.md` and
`notation-map.jsonl`. Trace every metric-signature change through related
definitions and proofs. Inspect state vectors, scalar products, adjoints,
anti-unitary operators, Fourier transforms, spectral cones, PCT formulas, and
spin-statistics signs in mathematical context.

Run `audit_notation.py` after each chapter. Its checks should find raw Hilbert
space tuple notation used for state inner products, state labels inside
asymptotic delimiters, unclassified source stars, inconsistent script macros,
and formulas that still carry the source metric without a recorded exception.

### 5. Rebuild figures and back matter

Inventory each mathematical figure from the rendered source pages. Recreate
line art and domain diagrams in TikZ or another vector form, then record the
source page and geometry check. Preserve chapter-local bibliographies with
linked citations. Rebuild the printed index as structured LaTeX entries whose
page links follow the new pagination.

### 6. Run fidelity review and release gates

For every chapter, compare the complete native text with its source pages.
Check each displayed equation and named theorem directly against the scan.
Resolve the page-disposition ledger, notation map, figure inventory, references,
and errata records.

`./build_and_verify.sh --draft` should run during transcription. The strict
command should require full page coverage, resolved review items, complete
source markers, clean notation scans, valid cross-references, zero unexpected
overfull boxes, parseable PDF text, embedded fonts, and a successful
Ghostscript check.

Render every final page to PNG and inspect it for broken symbols, crowded
displays, bad theorem breaks, footnote collisions, figure drift, and weak scan
readings. Write the checked build hash and source hash to
`RELEASE_VERIFICATION.md`. Export the verified artifact to
`../../pct-spin-statistics-all-that/pct-spin-statistics-all-that.pdf`.

## Completion test

The project is complete when all 221 source pages have dispositions, every
printed paragraph and mathematical object in the reading edition has source
provenance, each notation change has been checked in context, the appendix and
index are native LaTeX, the strict build passes, every output page has a visual
review record, and the exported PDF matches the verified build byte for byte.
