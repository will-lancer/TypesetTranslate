# Audit: Chapter 4 late packet

## Scope

- Canonical source: `origPapers/pct_spin_statistics_all_that.pdf`, SHA-256
  `44fadba731cafe7f009d4e561372febb3597e1f2a4819346ce2efd16befcb889`,
  221 physical pages.
- Source pages: PDF173--190, printed pages 161--178.
- Native files: `sec4_5.tex`, `sec4_6.tex`, and `bibliography.tex`.
- Rendered source images `work/source-pages/pdf-173.jpg` through
  `pdf-190.jpg` were inspected at original detail. The packet boundary at
  PDF173 begins with the continuation of Example 3 from Section 4-4. The
  boundary at PDF180 carries the final paragraph and equation of Section 4-5
  into the next source page before Section 4-6 begins.

## Coverage

The prose, displayed mathematics, equation tags, result statements, proof
steps, footnotes, and bibliography were checked in printed order.

- PDF173--180 contains the end of Example 3, Section 4-5, Theorems 4-14
  through 4-17, their displayed arguments, the unsmeared-fields footnote,
  the Jost-point footnote, and the Section 4-5 continuation through (4-89).
- The numbered equation sequence is complete and unique from (4-70) through
  (4-89). Unnumbered displays retain their unnumbered status.
- PDF180--186 contains the Section 4-6 opening, (4-90)--(4-93), Theorems
  4-18 through 4-22, the Borchers-class footnote, all proof displays, the
  corollary after Theorem 4-21, and (4-101). The numbered sequence is
  complete and unique from (4-90) through (4-101).
- The theorem environments are balanced for Theorems 4-14 through 4-22.
  Proof environments are balanced for Theorems 4-15 through 4-17 and
  4-18 through 4-21; the source's prose proof of Theorem 4-14 remains prose.
- PDF187--190 contains the single chapter bibliography heading, every prose
  introduction, references 1--29, and the intermediate printed entry 19a.

## Exact source fixes

- PDF173: restored the continuation of Example 3 before the Section 4-5
  heading, including the odd-subspace Klein transformation, its scalar
  products, the anti-hermitian transformed field, the sign relation for
  adjoints, and the paragraph on asymptotic normal statistics.
- PDF174: restored the theorem phrase `respectively, such that` before
  equation (4-71).
- PDF175: retained the source multiplication cross in the Jost--Schroer
  proof, while applying the bound notation's mass-sign conversion.
- PDF180: restored the Section 4-5 continuation and equation (4-89), then
  continued into the Section 4-6 heading in source order.
- PDF183: changed the dagger superscript after “the proof is in” to
  `\textsuperscript{\(\dagger\)}`, removing the math-only command from text.
- PDF183: changed the two Theorem 4-18 conclusions to the source labels
  `(a)` and `(b)`.
- PDF183--185: closed Theorem 4-18, 4-19, 4-20, and 4-21 before their proof
  environments. Theorem 4-22 was already correctly closed.
- PDF189: restored “It also appears in” before the Jordan--Wigner entry and
  gave reference 19a its own source marker.
- PDF187--190: replaced the repeated custom lists with native
  `thebibliography` environments. Each reopened native list sets natbib's
  numeric counter to the preceding global value, so the rendered labels run
  `[1]` through `[29]`, with `19a.` preserved between 19 and 20. The native
  list uses `\item[19a.]` for that alphanumeric source label because natbib's
  optional numeric label renders empty in this JHEP setup. Repeated natbib
  “References” headings are suppressed while the chapter's single
  “Bibliography” heading remains; the suppression is scoped to this packet.

## Notation audit

- Source Hilbert-space products in the restored PDF173 continuation use
  `\braket`; state equations throughout the packet use the project Dirac
  macros. Vacuum vectors retain the local `\Psi_0` state name where the
  source does so, while the source's `\Omega` notation remains `\Omega`.
- Operator adjoints use `^\dagger`. The scalar/test-function conjugate in
  `\widehat f(x)=f^*(-x)` remains a star, as required by the adjoint versus
  entrywise-conjugation distinction in `NOTATION.md`.
- The packet follows the bound mostly-plus metric. Source mass-shell and
  spacelike inequalities are rendered with `p^2=-m^2` and positive spacelike
  squares. The source free-field operators `(\Box+m^2)` become the local
  `\Box-m^2` form; the inhomogeneous uniqueness equations retain the
  established `-\Box+m^2` house form.
- Asymptotic states use the `\InKet` and `\OutKet` macros. The source's
  `\times` in the Jost--Schroer field equation is retained as a multiplication
  symbol.

## Marker and build checks

- Every packet source page is marked: `sec4_5.tex` covers PDF173--180,
  `sec4_6.tex` covers PDF180--186, and `bibliography.tex` covers PDF187--190.
  There are no missing page markers in those ranges.
- The native source environment counts are balanced: `sec4_5.tex` has four
  theorem ends for four theorem starts and three proof ends for three starts;
  `sec4_6.tex` has five theorem ends for five starts and four proof ends for
  four starts. The bibliography has no theorem or proof environments.
- `python3 scripts/audit_source.py --strict` passed with the canonical source
  hash, 221 pages, and 36/36 native chunks present.
- A two-pass JHEP harness containing these three files compiled with exit 0:
  `/tmp/pct-late-jhep4/pct-late-jhep4.pdf`. The output has 16 rendered pages,
  no overfull or underfull-box diagnostics, embedded fonts, and visible
  bibliography labels in source order. Rendered pages 1--16 were inspected
  through `/tmp/pct-late-jhep4/contact.png` and the page-level PNGs.

Packet disposition: PASS for all eighteen source pages.

Unresolved blockers: none
