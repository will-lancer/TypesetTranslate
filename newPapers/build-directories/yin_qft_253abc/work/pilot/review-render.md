# Render review: Yin Physics 253a pilot

Reviewed the rebuilt `latex/master.pdf` and the current native-resolution
render set `qa/rendered/pilot-01.png` through `pilot-11.png`, generated at
2026-08-08 20:56. The PDF has eleven A4 pages.

## Page review

| PDF page | Rendered content | Result |
|---:|---|---|
| 1 | Title page | The JHEP title block, author line, rule, and revised abstract are clean. |
| 2 | Contents and Part I opener | Hierarchy is clear. Contents links are visible and destinations are present. |
| 3 | Section 1.1 | The added effective-theory qualification fits the text block with readable density and clean hyphenation. |
| 4 | Figure 1 and start of Section 1.2 | Diagram, caption, heading transition, and source-plan list are readable without clipping or collisions. |
| 5 | Plan, Section 1.3 opening | List hierarchy, equation (1.1), and page break are clean. |
| 6 | Relativistic-particle discussion | Expanded equations (1.2)--(1.5) fit within the text block; long commutators and number labels remain clear. |
| 7 | Equations (1.6)--(1.7) and Figure 2 | The revised interaction discussion remains balanced. Figure labels, arrows, and caption are clear. |
| 8 | Locality and Poincare covariance | The general-D metric display in (1.8) and equations (1.9)--(1.10) are complete and legible. |
| 9 | Generators and free scalar field | Equations (1.11)--(1.15) have clean display spacing, with no collision between the algebra and Section 1.6. |
| 10 | Free-field construction and Section 1.7 opening | Equations (1.16)--(1.21), including both underbrace labels in (1.19), are legible and unclipped. The Section 1.7 heading is run into the opening sentence on one line. |
| 11 | End of Section 1.7 and Problem Set note | The closing prose and required Problem Set 1 note are readable. Most of the page is empty because the preceding heading and list occupy the end of PDF page 10. |

## Figure comparison

- Figure 1 on PDF page 4 matches the source-note render on combined-PDF physical page 6: the fork, divider, course labels, colored arrows, example allocation, and paired classification boxes are present. Regularized typography introduces no visual defect.
- Figure 2 on PDF page 7 matches the source-note render on combined-PDF physical page 10: the offset time axis, shared blue event, four green cone branches, interior purple response, exterior red forbidden path, and labels are retained. Nothing is clipped or collides.

## PDF and log checks

- Ghostscript processed all eleven pages with `-dPDFSTOPONERROR`. All listed fonts are embedded and subsetted.
- Named destinations cover the contents, sections, figures, and equations. No external URL object appears.
- `latex/master.log` has no overfull-box warning, underfull-box warning, undefined reference, undefined citation, or fatal error. It retains the JHEP missing-email warning, which is metadata debt for a full JHEP submission and does not affect this pilot render.

## Required reflow

Move Section 1.7 as a unit to the top of PDF page 11, or otherwise reflow the end of PDF page 10. Its heading must occupy its own line, and the final page should carry a proportionate share of the section. Keep the Problem Set 1 note at the chapter end after reflow.

## Cleanup debt

`qa/rendered/pilot-1.png` through `pilot-8.png` are legacy unpadded renders. Segregate or remove them before packaging so the current eleven-page set is unambiguous.

Unresolved blockers: Reflow PDF pages 10--11 so Section 1.7 has a standalone heading and PDF page 11 is no longer mostly blank.
