# Chapter 21 root wave-1 integration report

## Scope

This check integrates the chapter introduction and Sections 21.1--21.3:
physical source pages 318--341, printed pages 295--318. It verifies the
shared 21.2/21.3 transition on physical page 328 without taking ownership of
Sections 21.4--21.6 or the chapter backmatter.

## Inventory

- 103 numbered equations: 21.1.1--21.1.25, 21.2.1--21.2.23, and
  21.3.1--21.3.55.
- 103 matching stable equation labels.
- Six automatic footnotes, seven unnumbered displays, and two centered
  three-asterisk dividers.
- No figures or tables.

## Build and visual verification

- Wrapper:
  `latex/checks/chapter21-root-wave1-integrated-check.tex`
- Output:
  `latex/chapter21-root-wave1-integrated-check.pdf`
- Result: successful 21-page A4 build with all local and check-only external
  references resolved.
- Render directory:
  `tmp/pdfs/weinberg-vol2-ch21-root-wave1-integrated/rendered`
- Contact sheets:
  `tmp/pdfs/weinberg-vol2-ch21-root-wave1-integrated/contact-sheets`

All 21 pages were reviewed in two complete contact sheets. The shared
Section 21.2/21.3 transition page was also inspected at full resolution.
There is no clipping, overlap, malformed math, missing content, blank-content
loss, or bad section boundary.

The final log has no LaTeX errors, undefined references, duplicate
destinations, or underfull boxes. It retains one 6.09952 pt overfull box in
the long inline kinetic-gauge formula in Section 21.1; the line remains
inside the readable page area with no clipping or collision.
