# Source audit: physical pages 006-007

Source: `/Users/wlancer/Desktop/IAS/phy/qft/qft_253abc_book.pdf`

Verified SHA-256: `9e5e4d241fffffa56c1c3df6dce4b83178f75787dd5d794a18c5d0c087769f21`

The pages were inspected from 3400 by 4448 pixel RGB renders, corresponding to
400 dpi. The PDF has no usable text layer on either page. Physical page 006 is
original Physics 253a note page 1. Physical page 007 is original note page 2.

## Physical page 006, original note page 1

### Page boundary and visual structure

The page is self-contained. It begins with the question and answer
``Q: What is QFT?'' and ``A: QM + locality.'' A black fork below the answer
divides the page into local QFT on the left and effective field theory on the
right. Its two branches have no arrowheads. A dark blue dashed vertical line
runs downward between the columns, beginning below the fork and continuing
past both example boxes.

Black ink carries the main text. Gray ink supplies the parenthetical labels
``UV complete'' and ``and necessarily \(\infty\)-ly many d.o.f.'' Bright blue
marks `253a` and its three arrows. Magenta marks `253b` and another three
arrows. A pale blue box labeled `renormalizable` encloses the first effective
field theory group. A lavender box labeled `non-renormalizable` encloses the
second group.

The arrow endpoints are part of the source content:

- `253a` points to \(\phi^4\) theory in \(D=2,3\), \(\phi^4\) theory in
  \(D=4\), and QED.
- `253b` points to the statistical Ising model near criticality, Yang-Mills /
  QCD, and chiral perturbation theory.

No printed page number, footer, or continuation mark appears. The
`non-renormalizable` label is the final content on the page.

### Exact TeX-ready transcription

The following TikZ transcription preserves the lexical content, grouping,
fork, divider, boxes, course labels, and all six arrow relations. The color
values are rendering approximations; their semantic roles are exact.

```tex
% Physical PDF page 006; Physics 253a original note page 1.
% Source class: NOTES_EXACT.
% Requires \usepackage{xcolor,tikz}
%          \usetikzlibrary{arrows.meta,fit}
\definecolor{YinGray}{HTML}{A7A7A7}
\definecolor{YinDivider}{HTML}{28278A}
\definecolor{Yin253a}{HTML}{087BFA}
\definecolor{Yin253b}{HTML}{B000D5}
\definecolor{YinRenorm}{HTML}{A9C7E1}
\definecolor{YinNonrenorm}{HTML}{A68CFA}

\begin{center}
\begin{tikzpicture}[
  x=1cm,
  y=1cm,
  >=Latex,
  every node/.style={font=\normalsize,align=left},
  coursearrow/.style={-{Latex[length=2.2mm]},line width=0.8mm}
]
  \node (question) at (7.5,19.0) {Q: What is QFT?};
  \node (answer)   at (7.5,17.5) {A: QM + locality};

  % The black fork has no arrowheads.
  \coordinate (fork) at (7.5,16.8);
  \draw[line width=0.45mm] (fork) -- (3.0,15.2);
  \draw[line width=0.45mm] (fork) -- (12.0,15.2);

  \node[anchor=north,align=center] (localhead) at (3.0,14.8) {%
    local {\color{YinGray}(``UV complete'')}\\
    QFT};
  \node[anchor=north] (efthead) at (11.8,14.8) {Effective field Theory};

  \draw[YinDivider,dashed,line width=0.45mm]
    (7.5,14.6) -- (7.5,0.2);

  \node[anchor=north west,text width=6.3cm] at (0.0,12.9) {%
    $\bullet$ QM w/ Poincar\'e sym\\
    {\color{YinGray}\hspace*{0.9em}(and necessarily $\infty$-ly\\
    \hspace*{3.0em}many d.o.f.)}\\[0.7em]
    $\bullet$ local ``field'' operators\\[0.7em]
    $\bullet$ micro causality};

  \node[anchor=north west,text width=7.0cm] at (8.2,12.9) {%
    $\bullet$ defined perturbatively\\
    \hspace*{1.0em}based on a path integral\\
    \hspace*{1.0em}over space of fields\\[0.7em]
    $\bullet$ captures long-distance\\
    \hspace*{1.0em}low-energy observables};

  \node[anchor=west] at (0.0,7.8) {Examples:};
  \node[anchor=west] (phi23) at (0.7,6.7)
    {$\bullet$ $\phi^4$ theory in $D=2,3$};
  \node[anchor=north west,align=center] (ising) at (0.7,5.6) {%
    $\bullet$ Statistical Ising model\\
    \hspace*{1.2em}in $D=2,3$ near\\
    \hspace*{1.2em}criticality};
  \node[anchor=west] (ymqcd) at (0.7,2.2)
    {$\bullet$ Yang-Mills / QCD};

  \node[anchor=west] (phi4d4) at (9.0,6.7)
    {$\bullet$ $\phi^4$ theory in $D=4$};
  \node[anchor=west] (qed) at (9.0,5.5) {$\bullet$ QED};
  \node[anchor=west] (standardmodel) at (9.0,4.3)
    {$\bullet$ standard model.};
  \node[
    draw=YinRenorm,
    line width=0.6mm,
    fit=(phi4d4)(qed)(standardmodel),
    inner xsep=4mm,
    inner ysep=4mm,
    label={[YinRenorm]above:renormalizable}
  ] (renormbox) {};

  \node[anchor=west] (chiral) at (9.0,2.2)
    {$\bullet$ chiral perturbation theory};
  \node[anchor=west] (gr) at (9.0,1.0) {$\bullet$ GR};
  \node[
    draw=YinNonrenorm,
    line width=0.6mm,
    fit=(chiral)(gr),
    inner xsep=4mm,
    inner ysep=4mm,
    label={[YinNonrenorm]below:non-renormalizable}
  ] (nonrenormbox) {};

  \node[Yin253a] (coursea) at (6.2,7.4) {253a};
  \draw[Yin253a,coursearrow]
    (coursea.south west) to[out=235,in=25] (phi23.east);
  \draw[Yin253a,coursearrow]
    (coursea.east) to[out=0,in=170] (phi4d4.west);
  \draw[Yin253a,coursearrow]
    (coursea.south east) to[out=300,in=170] (qed.west);

  \node[Yin253b] (courseb) at (6.2,3.2) {253b};
  \draw[Yin253b,coursearrow]
    (courseb.west) to[out=165,in=0] (ising.east);
  \draw[Yin253b,coursearrow]
    (courseb.south west) to[out=235,in=35] (ymqcd.east);
  \draw[Yin253b,coursearrow]
    (courseb.east) to[out=0,in=175] (chiral.west);
\end{tikzpicture}
\end{center}
```

### Reading uncertainties

| Location | Adopted reading | Competing reading | Confidence | Evidence |
|---|---|---|---:|---|
| Gray text beside `local` | `(``UV complete'')` | `(``UV-complete'')` | 0.99 | The source has a visible space and no hyphen between `UV` and `complete`. |
| Gray parenthesis below Poincare symmetry | `(and necessarily $\infty$-ly many d.o.f.)` | `(and necessarily infinitely many d.o.f.)` | 0.98 | The literal source form uses the infinity glyph followed by `-ly`; expansion belongs only in edited prose. |
| Left property | `micro causality` | `microcausality` | 0.99 | The handwriting leaves a word gap. |
| Right heading | `Effective field Theory` | `Effective field theory` | 0.96 | The final word begins with a visibly large capital form. Capitalization has no mathematical effect. |
| Pale blue label | `renormalizable` | `renormalizeable` | 0.99 | The letter sequence is clear at 400 dpi and matches the paired label below. |
| Course arrows | 253a to \(\phi^4_{D=2,3}\), \(\phi^4_{D=4}\), QED; 253b to Ising criticality, Yang-Mills/QCD, chiral perturbation theory | An arrow could be read as assigning an entire box rather than its nearest bullet | 0.98 | Each arrowhead lands beside the named bullet. The upper magenta arrow lands beside `criticality`. |
| Color values | Semantic gray, blue, magenta, pale blue, lavender | Exact RGB values | 0.90 | Color roles are unambiguous. The numeric values above are visual approximations and should not serve as source measurements. |

No mathematical symbol remains unresolved on this page.

## Physical page 007, original note page 2

### Page boundary and visual structure

This page contains the black-ink, underlined heading `Plan of 253a`, followed
by three numbered blocks. Bullets are indented under each block. The final
application wraps after `electron g-factor,` and ends with `Lamb shift.` No
diagram, marginal annotation, or meaningful color appears. Physical page 008
starts a new `Prelude`, so the plan ends at this page boundary.

### Exact TeX-ready transcription

```tex
% Physical PDF page 007; Physics 253a original note page 2.
% Source class: NOTES_EXACT.
\begin{center}
  \underline{Plan of 253a}
\end{center}

\begin{itemize}
  \item[(1)] Lagrangian formulation of QM
    \begin{itemize}
      \item path integral, regularization
      \item perturbation theory, Feynman diagrams
      \item renormalization and counter terms
    \end{itemize}

  \item[(2)] Relativistic particles and fields
    \begin{itemize}
      \item $\phi^4$ theory
      \item Green functions
      \item asymptotic states
      \item S-matrix, LSZ reduction
    \end{itemize}

  \item[(3)] Particles and fields with spin
    \begin{itemize}
      \item classification of relativistic particles
      \item fermions and gauge bosons
      \item QED
      \item Applications: electron $g$-factor,\\
        Lamb shift.
    \end{itemize}
\end{itemize}
```

### Reading uncertainties

| Location | Adopted reading | Competing reading | Confidence | Evidence |
|---|---|---|---:|---|
| Block (1), third bullet | `counter terms` | `counterterms` | 0.99 | A clear word gap separates `counter` and `terms`. |
| Block (2), second bullet | `Green functions` | `Green's functions` | 0.99 | No apostrophe or possessive `s` follows `Green`. |
| Block (2), fourth bullet | `LSZ reduction` | `LS2 reduction` | 0.995 | The final glyph is a handwritten capital Z; the standard technical phrase fixes the reading. |
| Block (3), final bullet | `electron $g$-factor` | `electron $g$ factor` | 0.99 | A short hyphen is visible between `g` and `factor`. |
| Heading style | Underline spans the full heading | Underline applies only to `253a` | 0.995 | The continuous line starts below `Plan` and ends after `253a`. |

No unresolved reading blocks transcription of this page.

## Likely textbook and provenance units

| Stable candidate ID | Page | Kind | Exact source scope | Source class | Likely placement or disposition |
|---|---:|---|---|---|---|
| `YIN-253A-N01-P006-U01` | 006 | displayed definition | `Q: What is QFT?` through `A: QM + locality` and the black fork | `NOTES_EXACT` | Chapter-opening display or lead sentence with the fork retained in the page figure. |
| `YIN-253A-N01-P006-U02` | 006 | definition list | local QFT heading, `UV complete` annotation, and its three properties | `NOTES_EXACT` | Opening comparison of local QFT and effective field theory. |
| `YIN-253A-N01-P006-U03` | 006 | definition list | effective field theory heading and its two properties | `NOTES_EXACT` | Same comparison, kept adjacent to U02. |
| `YIN-253A-N01-P006-U04` | 006 | figure | all examples, the dashed divider, both boxes, both course labels, and six arrows | `NOTES_EXACT` | Reconstructed overview figure. Record the figure as one provenance unit while retaining every internal label in its source excerpt. |
| `YIN-253A-N02-P007-U01` | 007 | roadmap heading | underlined `Plan of 253a` | `NOTES_EXACT` | Source-authored course roadmap heading. |
| `YIN-253A-N02-P007-U02` | 007 | roadmap block | item (1) and its three bullets | `NOTES_EXACT` | Introductory roadmap or recorded page disposition if the chapter omits course logistics. |
| `YIN-253A-N02-P007-U03` | 007 | roadmap block | item (2) and its four bullets | `NOTES_EXACT` | Introductory roadmap for the relativistic-particles sequence. |
| `YIN-253A-N02-P007-U04` | 007 | roadmap block | item (3) and its four bullets | `NOTES_EXACT` | Introductory roadmap for spin, fermions, gauge bosons, and QED applications. |

For page-level dispositions, page 006 is substantive opening material. Page
007 is a source-authored roadmap whose placement needs an editorial decision;
its complete transcription should remain in the frozen source packet either
way.
