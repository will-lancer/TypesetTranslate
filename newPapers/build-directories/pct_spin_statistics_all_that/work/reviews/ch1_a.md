# Chapter 1, pages 4--8 review

Source pages inspected at original image detail:

- PDF 016, printed 4: chapter title, Wigner epigraph, opening Heisenberg-picture discussion, unit-ray discussion, and the state footnote.
- PDF 017, printed 5: Section 1-1 through the projection-operator footnote and the sentence ending ``commute with all the''.
- PDF 018, printed 6: continuation of that sentence through the commutative-super-selection assumption and its Dirac-terminology footnote.
- PDF 019, printed 7: closing paragraph of Section 1-1, Section 1-2, transition-probability equation, symmetry discussion, and Theorem 1-1.
- PDF 020, printed 8: theorem explanation, linear/anti-linear displays, parity examples, and the sentence ending ``observables of''.

## Notation decisions

The source writes Hilbert-space vectors as upright Greek letters and scalar
products as `(Phi, Psi)`. The transcription uses `\ket{\Phi}` and
`\braket{\Phi}{\Psi}` throughout, as required by the PCT Weinberg-style
notation pass. The anti-unitary identity on printed page 7 is rendered as
`\braket{\Theta\Phi}{\Theta\Psi}=\overline{\braket{\Phi}{\Psi}}`; this is the
Dirac form of the source's `(Theta Phi, Theta Psi)=(overline{Phi},overline{Psi})`.

The set of observables is the lowercase Greek `\theta`, with commutant
`\theta'`. The original scan is clear at PDF 017 and PDF 018; OCR often turns
this glyph into `6`. The univalence operator is `(-1)^F`, with `F` even for
integer spin and odd for half odd integer spin. The projection footnote uses
`E_{\Phi}\ket{\Psi}=\braket{\Phi}{\Psi}[\braket{\Phi}{\Phi}]^{-1}\ket{\Phi}`.

The source's scalar-product norm was converted to a Dirac norm. The displayed
equations printed as (1-1), (1-2), and (1-3) carry semantic LaTeX labels and
the requested `\tag{1-n}` forms. The two linearity tests on printed page 8
are unnumbered in the source and remain unnumbered.

## Boundary and unresolved items

The last sentence on printed page 8 ends mid-sentence at ``the observables of'';
the next packet must continue with the following source page. The theorem is
typeset as a labeled bold theorem heading so that the printed wording and
number remain visible while the parent style file can control spacing.

No source glyph remained unresolved after the original-detail inspection. The
anti-unitary overbar is recorded above because its printed placement is part
of the notation modernization rather than a change to the theorem's content.

## Later-audit disposition

`audit_ch1_early.md` independently checked PDF 016--020 against the source
images and the three native files. Its page ledger marks every assigned page
pass, including the final fragment on PDF 020, the three printed equation tags,
both unnumbered linearity displays, the theorem, and the footnotes. The source
boundary at the words ``observables of'' remains explicit. The following
PDF 021 handoff is checked in `audit_ch1_late.md`, whose page ledger begins
with the Section 1-3 continuation. The Dirac conversion and anti-unitary
overbar have matching entries in that audit's notation pass.

Unresolved blockers: none
