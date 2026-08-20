# Source errata

This ledger records changes to clear defects in the printed 2000 Princeton
paperback. Each entry requires a PDF page, printed page, source reading,
adopted reading, and reason.

Adopted corrections passed review: 0. Recorded source discrepancies: 2.

## Preserved source discrepancy

### Figure label punctuation

- PDF page: 085.
- Printed page: 73.
- Printed form: `FIGURE 2.4`.
- Native form: the visible caption remains `FIGURE 2.4`; the semantic LaTeX
  label is `fig:2-4`. The preceding source prose remains `Figure 2-4`.
- Reason: the source visibly uses both forms on the same page. Preserving each
  occurrence keeps the printed discrepancy while the semantic label follows
  the chapter-local figure sequence.

### Automorphism names in the fourth panel of Figure A.3

- PDF page: 210.
- Printed page: 198.
- Printed form: the $\mathcal H_{\bar s}$ block reads `obtained from \Psi_{0+}
  by applying the automorphism, s,` and closes `It is also obtained by
  applying \bar s to \Psi_{0-}`.
- Native form: the same two names, unchanged.
- Reason: the third panel names $s$ acting on $\Psi_{0-}$ and $\bar s$ acting
  on $\Psi_{0+}$, so the fourth panel's pairing reads as the source's own
  inconsistency rather than a scan defect. The printed reading is preserved
  and recorded here instead of being silently exchanged.

## Source-map notes with no adopted source correction

### Contents locator for Section 3-5

- PDF page: 008.
- Printed page: vi.
- Printed form: `3-5. Symmetries in a Field Theory 132`.
- Adopted form: the native section begins from the source marker at PDF 138 /
  printed page 126 and runs through PDF 144 / printed page 132; the source
  Contents folio is retained in the map while the reading edition generates its
  own table of contents.
- Reason: the source heading is visibly on printed page 126, while the printed
  Contents gives 132 beside the section title. No fixed source folio is copied
  into manuscript prose.

### Contents locator for the Appendix bibliography

- PDF page: 008.
- Printed page: vi.
- Printed form: `Bibliography 198`.
- Adopted form: the source map places the bibliography at PDF 211 / printed
  page 199 and the reading edition generates its own table of contents.
- Reason: the source header on PDF 211 reads `Bibliography 199`; PDF 210 is
  printed page 198 and still contains Figure A.3 and the closing prose of
  `Local Algebras and Superselection Sectors`.

### Inner-product limit on printed page 123

- PDF page: 135.
- Printed page: 123.
- Printed form: the limiting vectors are `\Psi_{f_n}\to\Phi` and
  `\Psi_{g_n}\to\chi`, followed by
  `(U(a,\Lambda)\Phi,U(a,\Lambda)\chi)=(\Phi,\chi)`.
- Adopted form: the native Dirac reading uses
  `\ket{\Psi_{f_n}}\to\ket{\Phi}`,
  `\ket{\Psi_{g_n}}\to\ket{\chi}`, and
  `\braket{U(a,\Lambda)\Phi}{U(a,\Lambda)\chi}
  =\braket{\Phi}{\chi}`.
- Reason: the source image clearly uses lowercase `\chi` for the second limit
  vector. The native delimiters implement the binding Dirac-notation contract
  and preserve the source's vector identity and inner-product order.
