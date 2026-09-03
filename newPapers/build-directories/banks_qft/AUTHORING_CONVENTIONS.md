# Frozen authoring conventions

The 2026-09-02 convention-adaptation pass supersedes the pilot's mathematical
conventions while retaining its structural interface. The lead places
`\BanksImplicitHook{I-...}` anchors after transcription and before the base
freeze. Their external exercise files remain outside the base edition's
recorded TeX inputs.

## Editorial convention adaptation

Every source formula is expressed with the mostly-plus metric and the physical
spacetime dimension `D` when its argument is dimension-independent. Lorentzian
positive-frequency phases use `\ee^{\ii p\cdot x}`. The scalar mass shell is
`p^2=-m^2`, and its Feynman denominator is `p^2+m^2-\ii0`.

Spatial vectors and their energy labels are bold. Spatial measures, delta
functions, and state normalizations carry `D-1`; spacetime measures carry `D`.
Four-dimensional chirality, `\gamma_5`, four-index Levi-Civita, Hodge-duality,
anomaly, and fixed trace formulas carry a local `D=4` statement.

The Clifford convention is
`\{\gamma^\mu,\gamma^\nu\}=-2\eta^{\mu\nu}` with
`\slashed p=\gamma^\mu p_\mu`. Dimensional regularization uses
`d_{\mathrm{reg}}` and `\varepsilon_{\mathrm{UV}}`, leaving `D` for physical
spacetime dimension.

Wick rotation uses `t=-\mathrm i\tau` and `p^0=\mathrm i p_4`. The continued
positive-frequency phase is
`\ee^{-\mathrm i p_4\tau+\mathrm i\mathbf p\cdot\mathbf x}`. Euclidean
spinor formulas define their Euclidean gamma matrices and propagator
normalization locally.

Adjacent lower and upper tensor indices contain an empty group. Authors inspect
each occurrence semantically because ordinary subscripts and powers share the
same TeX syntax. Kronecker deltas may retain compact mixed indices.

These systematic changes are recorded in the convention audit. `ERRATA.md`
continues to contain source defects alone.

## Structure

- `\BanksChapter{N}{Title}` opens a numbered chapter.
- A source section uses `\subsection{Title}`. Lower headings follow the source.
- `banksproblems` opens the source problem section.
- Appendices use `\BanksAppendix{Title}` after the master calls `\appendix`.
- Source-numbered displays use `equation` and `\label{eq:N.m}`. Other displays use
  unnumbered environments.
- Figures use native TikZ, source captions, and labels of the form `fig:N.m`.
- References use keys `banks-ref-1` through `banks-ref-180` in source order.

## Provenance

Place a `BANKS-SOURCE` marker at every source-page boundary and before each
equation, figure, problem, reference block, or index block. Use physical and
printed page numbers. A numbered object carries its source ID.

## Text and mathematics

The cropped source render is authoritative for content and locators. Join words
split by source line breaks. Preserve punctuation, emphasis, footnotes, equation
numbers, and problem stars. Apply the declared convention transformation to
mathematics and its dependent wording. Use `\footnote[n]{...}` for source
footnote numbers. Shared notation comes from `banks.sty`.

Workers preserve a suspected source defect and report it in their handoff. The
lead decides any correction and edits `ERRATA.md`. An unresolved glyph enters
`QUERY_LEDGER.md` before release.

## Editorial material

Source problems use `\BanksProblem{N.m}{*}` or an empty second argument.
Solutions use `\BanksSolution{N.m}` inside `bankssolutions`. The expanded edition
uses `exercise` with a stable `I-...` ID and `\BanksImplicitSolution{I-...}`.
Every solution supplies a derivation, checks the requested subparts, and states
the relevant assumptions.

## Handoff

Each lane reports pages, markers, numbered displays, figures, footnotes, problem
IDs, uncertain readings, and its compile command. Workers edit only assigned
content files. Shared styles, masters, manifests, ledgers, and scripts belong to
the lead.
