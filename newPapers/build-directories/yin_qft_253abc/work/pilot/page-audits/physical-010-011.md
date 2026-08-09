# Yin Physics 253a source audit: physical pages 010--011

Source: `/Users/wlancer/Desktop/IAS/phy/qft/qft_253abc_book.pdf`

Source SHA-256: `9e5e4d241fffffa56c1c3df6dce4b83178f75787dd5d794a18c5d0c087769f21` (verified)

Page mapping:

| Combined-PDF physical page | Original handwritten page | Main content |
|---:|---:|---|
| 010 | 5 | Causality, light-cone figure, local field operators |
| 011 | 6 | Poincare transformations, unitary implementation, infinitesimal generators, Poincare algebra |

The pages were inspected as complete 450-dpi renders. Six overlapping 600-dpi crops checked the handwriting and color. A 1200-dpi crop resolved the faint gray algebra on physical page 011. PDF text extraction returned blank pages, as expected for image-only handwritten material.

## Transcription conventions

- Line breaks in the prose blocks follow the handwriting.
- Spelling and punctuation stay literal. In particular, page 011 writes `suffizes`.
- `yinblue`, `yingreen`, `yinpurple`, `yinred`, and `yinfaintgray` name ink colors. The exact RGB values are not semantically significant; their separation is.
- Comments beginning `% VISUAL:` record arrows, underlining, placement, or a color split that ordinary LaTeX cannot reproduce inline.
- The source uses hats on the field and on the generators in the black formulas. The faint gray algebra omits hats.
- The shorthand `-(\rho\leftrightarrow\sigma)` is copied as written. It applies the exchange to the preceding terms inside the same parentheses.

Suggested preamble for the color-faithful snippets:

```tex
\usepackage{xcolor}
\usepackage{tikz}
\usetikzlibrary{arrows.meta}
\definecolor{yinblue}{RGB}{0,100,220}
\definecolor{yingreen}{RGB}{0,125,70}
\definecolor{yinpurple}{RGB}{165,0,205}
\definecolor{yinred}{RGB}{245,50,30}
\definecolor{yinfaintgray}{RGB}{165,165,165}
```

## Physical page 010 / original note page 5

### Exact TeX-ready transcription

```tex
% YIN-NOTE-PAGE: course=253a; note=5; pdf=10

\noindent Issue: Causality

% VISUAL: The following figure occupies the upper half of the page.
% VISUAL: The black coordinate-axis intersection lies well to the left of the
% light-cone vertex. The cone vertex is a blue filled point on the horizontal
% axis. The cone and its label are green. A purple dashed future-directed path
% lies inside the future cone. A red dashed future-directed path lies outside
% its right edge. Each dashed path has an arrow in the same color and ends in
% a filled point. The red path is the one labeled forbidden.
\begin{center}
\begin{tikzpicture}[>=Stealth, line cap=round, line join=round]
  \coordinate (event) at (0,0);

  \draw[black,->,thick] (-4.0,0) -- (4.7,0)
    node[right] {space $\vec{x}$};
  \draw[black,->,thick] (-3.0,-1.3) -- (-3.0,3.0)
    node[above] {time $x^0$};

  \draw[yingreen,thick] (event) -- (-2.15,2.6);
  \draw[yingreen,thick] (event) -- ( 2.05,2.6)
    node[above right] {lightcone};
  \draw[yingreen,thick] (event) -- (-2.05,-2.1);
  \draw[yingreen,thick] (event) -- ( 2.25,-2.1);

  \fill[yinblue] (event) circle (2.2pt);

  \draw[yinpurple,dashed,thick,->] (event) -- (0.55,2.05);
  \fill[yinpurple] (0.55,2.05) circle (3.0pt);

  \draw[yinred,dashed,thick,->] (event) -- (2.55,1.55);
  \fill[yinred] (2.55,1.55) circle (3.0pt);
  \node[black,align=left,anchor=west] at (2.85,1.35)
    {super-luminal\\propagation forbidden!};
\end{tikzpicture}
\end{center}

\noindent In a generic QM system,\\
signal propagation can be instantaneous\ldotp\ldotp\ldotp\ldotp

\bigskip

\noindent In a relativistic system, expect\\
\hspace*{1.4em}local disturbance to be represented by\\
\hspace*{4.4em}``field operator''\hspace{5em}$\widehat{\phi}(x)$

% VISUAL: ``operator'' has a blue wavy underline. The phi and its argument are
% black, while the caret making the hat was added in blue. A blue curved arrow
% descends from the argument x to the following blue marginal annotation.
\begin{flushright}
\color{yinblue}
$x^\mu=(x^0,\vec{x})$\\
$x^\mu$ are merely parameters,\\
not themselves operators.
\end{flushright}

\noindent $\bullet$ $\widehat{\phi}(x)$ and $\widehat{\phi}(x')$ are related\\
\hspace*{3.2em}by Poincar\'e symmetry.
```

### Visual inventory

The light cone has four green branches. Its upper-left branch is slightly curved by the handwriting, while the upper-right branch is nearly straight. The purple trajectory reaches a point inside the future cone. The red trajectory reaches a spacelike-separated point to the right of the future cone. Both trajectories start at the same blue event.

Black ink carries the heading, axes, prose, field symbols, and the warning text. Blue ink marks the cone vertex, underlines `operator`, supplies the hat over `\phi`, and gives the coordinate-parameter note. Green, purple, and red distinguish the causal geometry in the figure.

### Page boundary

The final bullet begins the Poincare-covariance discussion. Physical page 011 supplies the explicit transformation and its quantum implementation. This is one continuous source unit across the page break.

## Physical page 011 / original note page 6

### Exact TeX-ready transcription

```tex
% YIN-NOTE-PAGE: course=253a; note=6; pdf=11

\[
x^\mu \rightsquigarrow x'{}^\mu
=\Lambda^\mu{}_{\nu}x^\nu+a^\mu.
\]

% VISUAL: This entire metric condition is blue. A blue curved arrow points
% upward from it to the Lambda in the preceding black transformation.
\begingroup
\color{yinblue}
\[
\eta^{\alpha\beta}\Lambda^\mu{}_{\alpha}\Lambda^\nu{}_{\beta}
=\eta^{\mu\nu},
\qquad
\eta^{\mu\nu}
=
\begin{pmatrix}
-1&0&0&0\\
0&1&0&0\\
0&0&1&0\\
0&0&0&1
\end{pmatrix}.
\]
\endgroup

\noindent In QM, represented by a\\
\hspace*{1.3em}unitary operator $U(\Lambda,a)$.\qquad such that

\[
\widehat{\phi}(\Lambda x+a)
=U(\Lambda,a)\widehat{\phi}(x)\bigl(U(\Lambda,a)\bigr)^{-1}
\]

\noindent It suffizes to study infinitesimal version

\[
\Lambda^\mu{}_{\nu}=\delta^\mu{}_{\nu}+\omega^\mu{}_{\nu},
\qquad
a^\mu=\epsilon^\mu.
\]

% VISUAL: Blue curved arrows point from omega and epsilon to the shared note
% below them: ``small, keep / only 1st order''.
\begin{center}
{\color{yinblue}small, keep\\only $1^{\mathrm{st}}$ order}
\end{center}

\[
U(\Lambda,a)
=1-i\epsilon^\mu\widehat{P}_{\mu}
+\frac{i}{2}\omega_{\mu\nu}\widehat{J}^{\mu\nu}
\]

% VISUAL: A blue arrow points to P-hat with the label ``energy-momentum''.
% Another blue arrow points to J-hat with the stacked label
% ``boost / + angular / momentum''.
\begin{center}
{\color{yinblue}
$\widehat P_\mu$: energy-momentum
\qquad
$\widehat J^{\mu\nu}$: boost $+$ angular momentum}
\end{center}

% VISUAL: Every remaining line is written faintly in light gray.
\begingroup
\color{yinfaintgray}
\[
U(\Lambda',a')U(\Lambda,a)
=U(\Lambda'\Lambda,\Lambda'a+a')
\]
\[
[P,P]=0.
\]
\[
[P^\mu,J^{\rho\sigma}]
=-i\bigl(\eta^{\mu\rho}P^\sigma-(\rho\leftrightarrow\sigma)\bigr)
\]
\[
[J^{\mu\nu},J^{\rho\sigma}]
=-i\bigl(
\eta^{\nu\rho}J^{\mu\sigma}
-\eta^{\mu\rho}J^{\nu\sigma}
-(\rho\leftrightarrow\sigma)
\bigr)
\]
\endgroup
```

### Literal layout and color notes

The metric is drawn as four diagonal entries enclosed by large parentheses. The explicit zeroes in the TeX matrix above encode that diagonal layout; the page itself writes only `-1,1,1,1` along the diagonal.

The blue phrase `small, keep only 1st order` sits below and between the `\omega` and `\epsilon` parameters. Two arrows connect the phrase to those parameters. Generator labels sit directly below their respective terms. The final group law and commutators are materially fainter than all preceding writing and remain part of the source.

## Uncertainties and competing readings

| Page | Location | Adopted reading | Competing reading | Confidence | Disposition |
|---:|---|---|---|---:|---|
| 010 | End of `instantaneous` line | Four visible dots, encoded as `\ldotp` four times | An ordinary three-dot ellipsis preceded by sentence punctuation | 0.97 | Preserve the four marks in exact transcription; textbook prose may use a standard ellipsis. |
| 010 | Field-operator symbol | Black `\phi(x)` with a blue caret, yielding `\widehat\phi(x)` | Entire hatted symbol written in one color | 0.99 | Preserve the split-color construction in the visual record. |
| 011 | Transformation arrow | A hand-drawn wavy transformation arrow, encoded `\rightsquigarrow` | Ordinary `\to` drawn loosely | 0.96 | Keep `\rightsquigarrow` in the exact layer; either arrow has the same mathematical role in edited prose. |
| 011 | Metric display | `\operatorname{diag}(-1,1,1,1)` | A parenthesized tuple rather than a matrix | 0.99 | The diagonal placement establishes the mostly-plus metric. |
| 011 | Prose before infinitesimal expansion | Literal source spelling `suffizes` | Intended English `suffices` | 0.98 | Exact layer keeps `suffizes`; an edited chapter may silently correct the spelling under a recorded cleaning operation. |
| 011 | Faint group law | `\Lambda'a+a'` in the translation slot | `\Lambda'a'+a` | 0.99 | High-resolution inspection supports the adopted reading, which also agrees with the displayed order of group composition. |
| 011 | Faint algebra typography | Unhatted `P,J` throughout | Hats lost because the ink is faint | 0.99 | The letter tops are fully visible at 1200 dpi and carry no hats. Preserve the omission. |
| 011 | Second faint commutator | `\eta^{\mu\rho}P^\sigma-(\rho\leftrightarrow\sigma)` | Fully expanded second term | 1.00 | Keep the source shorthand. |
| 011 | Third faint commutator | `\eta^{\nu\rho}J^{\mu\sigma}-\eta^{\mu\rho}J^{\nu\sigma}-(\rho\leftrightarrow\sigma)` | A sign change in the second displayed term | 0.99 | The minus sign is visible. Keep both source signs. |

## Likely textbook and provenance units

| Suggested stable unit | Kind | Source locator | Scope |
|---|---|---|---|
| `253a-n05-causality-figure` | figure | note 5; PDF 10 | Heading, axes, light cone, allowed timelike path, forbidden super-luminal path, and all color labels |
| `253a-n05-local-fields` | paragraph plus annotation | note 5; PDF 10 | Generic-QM instantaneous propagation, relativistic locality, `\widehat\phi(x)`, and the parameter status of `x^\mu` |
| `253a-n05-n06-poincare-bridge` | cross-page paragraph | notes 5--6; PDFs 10--11 | Statement that fields at transformed points are related, followed by the explicit Poincare coordinate map |
| `253a-n06-lorentz-condition` | equation | note 6; PDF 11 | Lorentz metric condition and mostly-plus signature |
| `253a-n06-unitary-covariance` | paragraph plus equation | note 6; PDF 11 | Unitary representation `U(\Lambda,a)` and scalar-field covariance formula |
| `253a-n06-infinitesimal-generators` | paragraph plus two equations | note 6; PDF 11 | Infinitesimal `\omega,\epsilon` expansion, first-order instruction, and the signs of `\widehat P,\widehat J` |
| `253a-n06-poincare-algebra` | equation group | note 6; PDF 11 | Faint group-composition law and the three Poincare commutator lines |

Each row should receive its own `NOTES_EXACT` provenance record until video alignment supplies a timestamped composite source. The cross-page bridge should remain one textual unit even if the final TeX places a page break between its sentences. Physical page 012 starts the separately headed `Micro causality:` unit.
