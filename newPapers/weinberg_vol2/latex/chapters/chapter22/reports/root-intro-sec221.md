# Chapter 22 opening and Section 22.1 — root report

## Coverage

- Chapter introduction: physical PDF p. 382 (printed p. 359), from the
  chapter heading through immediately before Section 22.1.
- Section 22.1, “The pi-zero Decay Problem”: physical PDF pp. 382--384
  (printed pp. 359--361), through the final paragraph immediately before
  Section 22.2.

## Inventory

- Numbered equations: (22.1.1)--(22.1.9), consecutive, with matching explicit
  tags and labels.
- Citations: [1]--[6], linked to the Chapter 22 reference destinations.
- No figures, tables, footnotes, or unnumbered displays occur in this range.

## Verification

- Source wording, mathematical notation, equation endpoints, and the
  Section 22.2 boundary were checked against the existing high-resolution
  renders of physical pp. 382--384.
- `checks/chapter22-root-sec221-check.tex` compiles successfully with
  `latexmk` to a three-page A4 PDF.
- The final log has no undefined references, duplicate labels, overfull
  boxes, or errors. The only warning is the inherited `hyperref` `pagecolor`
  warning from `jheppub.sty`.
- All three pages were rendered at 180 DPI to
  `/private/tmp/ch22-root-sec221-qa/` and inspected at full resolution; no
  clipping, collisions, missing material, or boundary leakage was found.
- The notation finishing pass normalized the source's multiplication signs
  in \(U(1)\cdot U(1)\) and the three scientific-notation factors to the
  project-standard `\cdot`. The section was then rebuilt and all three pages
  were rerendered and reinspected cleanly.

## Fidelity notes

- The source uses \(SU(2)\otimes SU(2)\), rather than the centered-dot
  notation used elsewhere in the volume; the printed notation is preserved.
- The pre-QCD pion--nucleon interaction retains the printed factor
  \(2\vec t\).
- The source punctuation “with little change in our results).” is preserved.

No unresolved ambiguity remains.
