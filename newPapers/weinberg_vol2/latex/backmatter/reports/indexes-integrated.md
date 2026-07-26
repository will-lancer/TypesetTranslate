# Integrated indexes report

## Scope

The integrated back matter represents the complete Author Index and Subject
Index from physical source pages 501--512 (printed pages 478--489).
`latex/backmatter/indexes.tex` loads the two source files in source order with
an explicit page boundary between them.

## Inventory

- Author Index: 468 entries, 25 alphabet groups, 413 exact italic-reference
  tokens, 275 independently asserted roman tokens, 12 scan-matched columns
  across six pages.
- Subject Index: 308 top-level entries plus 71 subentries, 26 `see`
  references, 17 `also see` references, 23 alphabetic gaps, and 12
  scan-matched columns across six pages.
- Integrated output: 12 A4 pages. In the final volume these are PDF pages
  423--434.

Detailed scan reconciliations are recorded in `author-index.md` and
`subject-index.md`.

## Build and log audit

The final isolated build was run from `newPapers/weinberg_vol2/latex`:

`latexmk -g -pdf checks/indexes-check.tex`

The result is `latex/indexes-check.pdf`, 12 pages and 196,736 bytes, SHA-256
`98ea130de4f0b1f0fffd9d3ad1bbe6254fc833372ff60926df5e72bd37ded23f`.
The log contains no TeX errors, fatal errors, undefined references, duplicate
destinations, font warnings, or overfull boxes. Four benign underfull
paragraphs remain in narrow Subject Index columns and were visually checked.
The inherited `hyperref` warning about the removed `pagecolor` option is
unrelated to index content.

## Visual QA

Every Author Index page was inspected individually at 180--200 DPI, including
the independent source-scan audit of roman and italic page-number styles.
Every Subject Index page was inspected individually at 180 DPI. The final
integrated master pages 423--434 were rendered at 180 DPI in
`/private/tmp/weinberg-vol2-final-index-qa.ubV6n2/` and inspected together for
ordering, page boundaries, clipping, collision, continuation indentation, and
column drift. No visual defects were found.

## Boundary decision

Physical source page 513 is blank and physical page 514 is the publisher's
back cover. They contain no book content and are intentionally excluded.
