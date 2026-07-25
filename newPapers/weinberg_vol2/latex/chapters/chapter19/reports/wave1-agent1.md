# Chapter 19 Wave 1 Agent 1 Report

## Coverage

- `introduction.tex`: Chapter 19 opening, physical PDF page 186 (printed page 163), through immediately before Section 19.1.
- `sec191.tex`: complete Section 19.1, physical PDF pages 186-190 (printed pages 163-167).
- `sec192.tex`: complete Section 19.2, physical PDF pages 190-200 (printed pages 167-177), including the continuation at the top of physical page 200 and stopping before the Section 19.3 heading.

## Inventory

- Section 19.1: equations (19.1.1)-(19.1.9), citations [1]-[2], and one source footnote.
- Section 19.2: equations (19.2.1)-(19.2.56), citations [3]-[6], and one source footnote.
- Figures 19.1 and 19.2, reconstructed as TikZ in `fig19-01.tex` and `fig19-02.tex`, with the complete source captions.

## Verification

- Compiled `checks/chapter19-wave1-agent1-check.tex` successfully with `latexmk`.
- The isolated check PDF has 13 pages. Every page was rendered to PNG and visually inspected; Figure 19.2 also received a high-resolution inspection after label-spacing refinements.
- No LaTeX errors, undefined references, overfull or underfull boxes, clipped text, equation-tag collisions, or unreadable glyphs remain. The only log warning is the existing `jheppub`/`hyperref` deprecation warning for the removed `pagecolor` option.
- Equation-tag and label sequences are complete and consecutive: 1-9 for Section 19.1 and 1-56 for Section 19.2.
- All six citation markers resolve in the isolated wrapper, both source footnotes are ordinary numbered `\footnote`s, and no `VERIFY`, `TODO`, `FIXME`, or unresolved transcription markers remain.

## Source-fidelity notes

- Preserved the identical exponent \(e^{ip\cdot(y-x)}\) in both terms of Eq. (19.2.18), exactly as printed.
- Preserved the printed \(i\int\rho_n(\mu^2)\) in Eq. (19.2.32), which has no visible differential.
- Preserved the uppercase subscript in the prose reference to \(\rho_N(\mu^2)\).
- Preserved the printed factors of \(i\) in the unnumbered derivation after Eq. (19.2.35), including their absence on its second line.
- Preserved the source's use of \(q^\mu\) in the prose before Eq. (19.2.34) and \(p_B\) in Eqs. (19.2.34)-(19.2.39).
- No unresolved source uncertainty remains.
