# Transcription conventions

These conventions match the successful Weinberg QFT build directories where
they are useful for this book.

## Ownership and assembly

- One agent owns one writable section file at a time.
- Chapter assembly files contain only the chapter heading and `\input` lines.
- Put chapter-opening prose and epigraphs in `introduction.tex`.
- Put bibliography and references in `backmatter.tex`.
- Put each figure in its own file under `latex/figures/chapterNN/`.
- Do not make unrelated edits to `master.tex`, `jheppub.sty`, or another
  section while transcribing.

Use the stable filenames in `SECTION_PLAN.md`.

## Required file header

Begin every section file with:

```tex
% Source: Weinberg GR, physical PDF pp. TODO--TODO
%         (printed pp. TODO--TODO).
% Coverage: Section X.Y, TITLE; equations (X.Y.1)--(X.Y.N).
% Figures/tables/footnotes: TODO.
% Status: not started | transcribed | source-reviewed and compile-clean.
% Uncertainties: none | concise list of VERIFY items.
```

Physical PDF pages are the assignment boundary. Printed pages are recorded for
human orientation only. Eight pages absent from the local PDF are preserved as
hashed supplemental sources documented in `SOURCE_MAP.md`: Contents xxii and
printed pages 306, 390, 392, 418, 440, 594, and 602. Their exact insertion points
and transcription owners are binding; a physical-page range that crosses one
of those positions does not by itself provide complete source coverage.

## Headings and optional sections

Use:

```tex
\subsection{Section Title}
```

For sections marked with an asterisk in the source contents:

```tex
\subsection{Section Title\optionalreading}
```

The star indicates optional first-reading material; it is not a footnote.

## Equations and cross-references

Preserve source equation numbers explicitly:

```tex
\begin{equation}
  G_{\mu\nu}=8\pi G\,T_{\mu\nu}.
  \tag{7.1.13}\label{eq:7.1.13}
\end{equation}
```

Refer to it with:

```tex
Eq.~\eqref{eq:7.1.13}
```

Use stable prefixes:

- equations: `eq:7.1.13`;
- sections: `sec:7.1`;
- figures: `fig:7.1`;
- tables: `tab:15.1`;
- chapter references: `ch7-ref-1`.

Do not rely on automatic equation numbering: explicit tags prevent numbering
drift when section files are assembled or revised.

## Bibliography and references

Weinberg distinguishes chapter bibliographies from numbered references.
Preserve both headings and their order in `chapters/chapterNN/backmatter.tex`.

Use:

```tex
\chapterbackmatter{Bibliography}
...
\chapterbackmatter{References}
\begin{enumerate}
  \item \phantomsection\label{ch7-ref-1} ...
\end{enumerate}
```

Link source markers with `\hyperref[ch7-ref-1]{[1]}`. Do not create a global
BibTeX database unless the project is deliberately redesigned later.

## Figures and tables

- Prefer TikZ for line diagrams and geometric constructions.
- Keep photographs or scan-dependent artwork as separate image assets when
  faithful vector reconstruction is inappropriate.
- Put figure code in `latex/figures/chapterNN/figNN-NN.tex`.
- Add source physical-page information in every figure file header.
- Use `TODO FIGURE:` rather than inventing unclear content.

## Combined index

The source has one combined author-and-subject index on physical PDF
pp. 665--681 (printed pp. 641--657). Preserve the entry order, cross-references,
subentries, continuation indentation, and every page-number range. The source
uses italics selectively for page numbers that point to publications in
bibliographies, reference lists, and tables; reproduce those italics rather
than inferring that every number on a bibliography page is italic. Apply the
edition's binding notation conversions inside index headings as well—for
example, “Cosmic scale factor (\(R\))” becomes “Cosmic scale factor
(\(a\))”—but do not silently update historical names, data, or page locators.

## Modernization QA

For every numbered and unnumbered displayed equation:

1. transcribe the source equation before converting it;
2. apply `NOTATION.md`;
3. check the metric, curvature, determinant, and raised-time-index signs;
4. check the flat-space or Newtonian limit where applicable;
5. retain \(I\) for actions and \(D/D\tau\) along worldlines;
6. ensure no source \((+,+,+,-)\) convention survives accidentally;
7. compare every multiline display with the rendered source for missing binary
   operators. In particular, a literal `+` at the start of a line can be
   swallowed while an added file is represented as a patch, leaving valid TeX
   with a mathematically incorrect concatenation.

## Completion gate

A section is complete only when:

- its physical source range has been inspected at readable resolution;
- text, equations, footnotes, figures, tables, bibliography markers, and
  transitions are accounted for;
- all `VERIFY:` and `TODO FIGURE:` comments are resolved or reported;
- the chapter or a small check wrapper compiles;
- the rendered PDF has been inspected for clipping, overlaps, missing glyphs,
  bad page breaks, and malformed equations.
