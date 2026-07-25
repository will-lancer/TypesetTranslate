# Chapter 23 wave 2, agent 3 report

## Scope and boundary

- Transcribed Section 23.8, “Vacuum Decay,” from physical PDF pages
  487--491 (printed pages 464--468), beginning at the Section 23.8 heading
  and ending immediately before Appendix A.
- Transcribed Appendix A, “Euclidean Path Integrals,” from physical PDF
  pages 491--495 (printed pages 468--472), beginning at the Appendix A
  heading and ending immediately before Appendix B.
- Used fresh 300-DPI source renders in
  `tmp/pdfs/weinberg-vol2-ch23-sec238-appa-source/`; physical pages 486 and
  496 were also rendered to verify both outer boundaries. Ambiguous
  formulas and markers were checked against 600-DPI renders in
  `tmp/pdfs/weinberg-vol2-ch23-sec238-appa-hires/`.
- Did not edit the Chapter 23 assembly or any other chapter-content file.

## Structural inventory

- Section 23.8: eighteen numbered equations with exact tags and labels
  (23.8.1)--(23.8.18), no unnumbered displays, four citation occurrences
  linking entries [6], [37], [38], and [39], and one ordinary footnote.
- Appendix A: twenty-three numbered equations with exact tags and labels
  (23.A.1)--(23.A.23), five unnumbered displays, and no citations or
  footnotes.
- Neither source span contains a figure or table.

## Scan-authoritative readings retained

The following potentially surprising readings were checked against the
600-DPI source and retained rather than silently corrected:

- Eq. (23.8.14), and the prose immediately before it, print `M^{-4}`.
- The prose before Eq. (23.8.8) calls Eq. (23.8.2) the Euclidean action,
  although the explicit action is Eq. (23.8.3).
- Eq. (23.A.21) explicitly imposes `q(0)=q` and `q(T)=q'`, while the
  neighboring formulas and the action in Eqs. (23.A.22)--(23.A.23) use
  the interval from `-T/2` to `T/2`.
- The prose after Eq. (23.A.12) calls the bras right-eigenstates and the
  kets left-eigenstates. This wording is preserved.
- High-resolution review also confirmed the determinant
  `Det[2 i pi A(q)]` in Eqs. (23.A.17) and (23.A.21), all indices and
  signs in Eq. (23.A.22), and the full continuous-symmetry footnote in
  Section 23.8.

## Integration dependencies

The isolated check supplies check-only destinations for links that the
integrated volume must provide:

- Earlier appendix and sections: `app:9`, `sec:9.1`, `sec:19.5`,
  `sec:23.1`, and `sec:23.7`.
- Earlier equation: `eq:23.1.4`.
- Bibliography anchors: `ch23-ref-6`, `ch23-ref-37`, `ch23-ref-38`, and
  `ch23-ref-39`.

The links from Section 23.8 to Appendix A and to Eqs. (23.A.6),
(23.A.21), and (23.A.23) resolve internally in the combined isolated
check.

## Verification

- Combined isolated build command, run from
  `newPapers/weinberg_vol2/latex`:
  `latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error
  checks/chapter23-wave2-agent3-check.tex`
- Result: successful seven-page PDF. All equation, section, appendix, and
  bibliography links resolve.
- Final log audit found no overfull boxes, underfull boxes, undefined
  references, multiply defined labels, LaTeX errors, or fatal errors. The
  inherited `hyperref` notice about the removed `pagecolor` option is the
  only package warning.
- Rendered every final page at 180 DPI in
  `/private/tmp/weinberg-vol2-ch23-wave2-agent3-render/` and visually
  inspected all seven pages. No clipping, collision, overflow, missing
  content, or Appendix B leakage was found.
- Mechanical audit confirmed 18 + 23 sequential equation tags and matching
  unique labels, five unnumbered displays, four citation occurrences, one
  footnote, and no forbidden `\times`, `\mathscr`, or `\mathbb{1}`
  notation.
- `pdftotext` confirmed the visible endpoint tags (23.8.18) and
  (23.A.23), and `git diff --check` passes for both content files and the
  isolated check wrapper.
- Two layout-finishing cycles were used to eliminate a 1.43-point
  overfull line; the final source and render audits then passed cleanly.
