# Errata and source-map audit

## Evidence

- Canonical source: `origPapers/pct_spin_statistics_all_that.pdf`.
- Inspected source images: PDF 008 / printed vi, PDF 085 / printed 73, PDF
  135 / printed 123, PDF 138 / printed 126, PDF 210 / printed 198, and PDF
  211 / printed 199.
- Compared native readings: `latex/figures/fig2_4.tex`,
  `latex/chapters/chapter03/sec3_5.tex`,
  `latex/chapters/chapter03/sec3_4.tex`, `SOURCE_MAP.md`,
  `SOURCE_MANIFEST.yaml`, and the page-disposition ledger.
- The source PDF has no usable text layer for these pages. Rendered images
  control each reading.

## Candidate checks

### Contents, Section 3-5

PDF 008 / printed vi visibly gives `3-5. Symmetries in a Field Theory 132`.
PDF 138 / printed 126 visibly carries the Section 3-5 heading, and PDF 144 /
printed 132 carries its closing prose. `sec3_5.tex` has the corresponding
markers and starts at PDF 138 / printed 126. The Contents pages are represented
by the generated native table of contents, so no fixed source folio is copied
into manuscript prose. This is recorded as a source-map note in `ERRATA.md`.

### Figure 2.4

PDF 085 / printed 73 visibly labels the caption `FIGURE 2.4`. The native
`fig2_4.tex` sets `\thefigure` to `2-4`, so the adopted caption reads
`FIGURE 2-4`. This is the one adopted source discrepancy recorded in
`ERRATA.md`; the figure's caption text and vector labels remain source-faithful.

### Appendix bibliography locator

PDF 008 / printed vi visibly gives `Bibliography 198`. PDF 210 / printed 198
still contains Figure A.3 and the closing `Local Algebras and Superselection
Sectors` prose. PDF 211 / printed 199 carries the running header `Bibliography
199` and the bibliography heading. The source map records PDF 211--216 /
printed 199--204, while the reading edition generates its own Contents. This
is recorded as a source-map note in `ERRATA.md`; there is no manuscript-level
source correction to adopt. The native appendix bibliography file was not
present at the time of this audit, so no unbuilt manuscript reading is treated
as evidence for a source correction.

### Inner-product limit on printed page 123

PDF 135 / printed 123 visibly uses lowercase `\chi` for the second limiting
vector: `\Psi_{f_n}\to\Phi` and `\Psi_{g_n}\to\chi`, followed by the
inner-product identity with `\chi` on both sides. `sec3_4.tex` keeps that
identity and applies the binding Dirac convention, writing the limits as
`\ket{\Psi_{f_n}}\to\ket{\Phi}` and
`\ket{\Psi_{g_n}}\to\ket{\chi}`, with the corresponding `\braket` identity.
This is an intentional notation conversion and is recorded as a source-map
note in `ERRATA.md`, not as a source defect.

## Result

One adopted discrepancy, Figure 2.4's period-to-hyphen label conversion, is
documented with PDF page, printed page, printed form, adopted form, and reason.
The two Contents locators and the page-123 `\chi` reading are documented as
source-map notes with their source forms and native treatment. No unrecorded
source defect remains in the assigned candidates.

Follow-up disposition: the native caption preserves the visible source form
`FIGURE 2.4`, while its semantic label remains `fig:2-4`. The ledger now
records this as a preserved source discrepancy.

Unresolved blockers: none
