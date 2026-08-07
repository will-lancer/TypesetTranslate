# Transcription conventions

## Ownership and assembly

- Use one writable content file per section or appendix subdivision.
- Chapter assembly files contain only the chapter heading and `\\input` lines.
- Put chapter-opening prose in `introduction.tex` and chapter problems in
  `problems.tex`.
- Put each figure in its own file under `latex/figures/chapterNN/`.
- Do not edit another section as a side effect of transcription.

## Required content-file header

```tex
% Source: Wald GR, physical PDF pp. TODO--TODO
%         (printed pp. TODO--TODO).
% Coverage: Section X.Y, TITLE; equations (X.Y.1)--(X.Y.N).
% Figures/tables/footnotes: TODO.
% Status: not started | transcribed | source-reviewed and compile-clean.
% Uncertainties: none | concise list of VERIFY items.
```

Physical PDF pages define assignments. Printed pages are included for human
orientation.

## Equations and references

Preserve source equation numbers explicitly:

```tex
\begin{equation}
  \cdots
  \tag{3.2.3}\label{eq:3.2.3}
\end{equation}
```

Use `Eq.~\\eqref{eq:3.2.3}` and stable prefixes `eq:`, `sec:`, `fig:`,
`tab:`, `thm:`, `prop:`, and `lem:`. Preserve theorem, proposition, lemma,
definition, figure, table, and problem numbers.

## Figures

- Prefer TikZ for line diagrams and causal or geometric constructions.
- Keep source-dependent artwork as a separate asset where vector recreation
  would be speculative.
- Use `TODO FIGURE:` rather than guessing an unclear figure.

## Completion gate

A file is complete only when its source pages have been viewed at readable
resolution; prose, mathematics, footnotes, figures, and transitions are
accounted for; all notation conversions are applied; all uncertainty markers
are resolved or reported; the containing unit compiles; and the output has
been visually inspected.

