# Transcription contract

## Authority

`banks-qft.pdf` is the sole textual authority. Its SHA-256 is
`31de7827e7bc636feaa7028fe4dbb63a718b3926ee43ff3d96d91185a44eafe3`.
Rendered source pages settle every symbol and line reading. The extracted text
layer serves as a search aid.

## Coverage

The native transcription contains Chapters 1 through 11, Appendices A through
F, references, the author index, and the subject index. `SOURCE_MAP.md` assigns
an explicit disposition to all 281 physical pages. The generated title and
contents represent source pages 5 and 7 through 9.

## Fidelity

Preserve prose, equation labels, numbering, stars, footnotes, captions,
bibliography data, and index entries in printed order. Reflow source line
endings. Join words split only by a source line break. Express every equation
and dependent phrase through the convention map in `NOTATION.md`. Record each
adopted source correction in `ERRATA.md`. Put an uncertain reading in
`QUERY_LEDGER.md` until page inspection settles it.

Each substantive unit starts with `% BANKS-SOURCE: pdf=<n> print=<n>
kind=<type>`. Equation, figure, problem, reference, and index units add a stable
`id` field.

## Native form

Body text and mathematics use native LaTeX. Mathematical figures use TikZ.
The reading editions never import source PDF pages. Equation numbers and
problem numbers remain source locators.

## Convention map

The native editions use `\eta_{\mu\nu}=\operatorname{diag}(-,+,\ldots,+)`.
Arguments valid in general spacetime dimension use `D`; dimensional
regularization uses `d_{\mathrm{reg}}`. Spatial vectors are bold. Adjacent
lower and upper tensor indices include an empty TeX group, apart from compact
Kronecker deltas. Four-dimensional structures carry an explicit local
specialization.

This map is an editorial transformation of the complete mathematical closure.
It covers chapters, appendices, figures, problems, added exercises, and every
solution. The transformation record stays separate from `ERRATA.md`, whose
entries describe source defects.

## Editorial exercises

`\BanksProblem`, `\BanksSolution`, and the `exercise` environment form the
frozen authoring interface. The base edition contains all 80 source problems
and their editorial solutions. The expanded edition also contains 110 inline
editorial exercises and their collected solutions.

An implicit cue produces one exercise. A compound assignment uses lettered
subparts inside that exercise. Every added solution begins with the printed
label `Editorial solution`.

At chapter end, the order is source problems, numbered-problem solutions, then
implicit-exercise solutions. Inline exercises appear immediately after their
recorded source cue.

## Release evidence

Strict release requires complete page dispositions, closed ledgers, exact
exercise-solution pairing, unique labels, complete master inclusion, and clean
LaTeX diagnostics. Both PDFs must pass text extraction, Ghostscript parsing,
embedded-font checks, reproducibility checks, and byte comparison with their
release copies.

Every output page is rendered at 150 DPI. Review records cover all rendered
pages exactly once and bind each decision to the rendered-file checksum. Fresh
mathematical reviews also bind the converted equations and solutions to the
current native snapshot hash.
