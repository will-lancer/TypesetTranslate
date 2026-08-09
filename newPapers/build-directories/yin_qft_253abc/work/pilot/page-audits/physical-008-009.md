# Source audit: physical pages 8-9

Source: `/Users/wlancer/Desktop/IAS/phy/qft/qft_253abc_book.pdf`  
Verified SHA-256: `9e5e4d241fffffa56c1c3df6dce4b83178f75787dd5d794a18c5d0c087769f21`  
Scope: physical PDF pages 8-9, corresponding to Physics 253a handwritten note pages 3-4.  
Inspection: both pages were rendered from the source PDF at 400 dpi and 800 dpi. The 800 dpi renders were checked as full pages and as overlapping crops.

The principal handwriting is black. Later or secondary annotations on these pages use light gray and blue. The transcription marks those colors explicitly. The TeX below assumes `amsmath`, `amssymb`, and `xcolor`.

## Physical page 8 / 253a note page 3

### Exact TeX-ready transcription

```tex
% ===== BEGIN physical PDF page 8 / 253a note page 3 =====

\noindent Prelude: why do we need\\
\hspace*{2em}``field theory'' to describe QM of\\
\hspace*{3em}particles with relativistic symmetry?

\medskip
\noindent $\bullet$\quad Hilbert space $\mathcal H$

\medskip
\noindent\hspace*{2em}$-$\quad vacuum $|\Omega\rangle$,
\qquad $H|\Omega\rangle=0$.

\medskip
\noindent\hspace*{2em}$\bullet$\quad single particle
\qquad $|\vec p\rangle$
\hfill
\textcolor{gray}{$p^\mu\equiv(p^0,\vec p)$}\\
\hfill\textcolor{gray}{$D$-dimensional}

\[
H|\vec p\rangle
=\sqrt{\vec p^{\,2}+m^2}\,|\vec p\rangle.
\]

\medskip
\noindent\hspace*{2em}$\bullet$\quad multi-particle
\qquad $|\vec p_1,\ldots,\vec p_n\rangle$

\noindent\hspace*{8em}(non-interacting)

\[
H=\sum_{i=1}^{n}\sqrt{\vec p_i^{\,2}+m^2}\,.
\]

\noindent Equivalently, we can introduce

\[
\left.
\begin{array}{rl}
\text{creation} & a_{\vec p}^{\dagger}\\
\text{annihilation} & a_{\vec p}
\end{array}
\right\}
\quad \text{operators.}
\]

\[
|\vec p\rangle=a_{\vec p}^{\dagger}|\Omega\rangle
\]

% ===== END physical PDF page 8 / 253a note page 3 =====
```

### Layout and annotation inventory

- The heading/question occupies three centered-left lines. Quotation marks occur only around “field theory.”
- The gray note sits to the right of the single-particle ket. It reads \(p^\mu\equiv(p^0,\vec p)\), with “\(D\)-dimensional” directly below it.
- A right brace groups the creation and annihilation rows with the word “operators.”
- The page ends immediately after \(|\vec p\rangle=a_{\vec p}^{\dagger}|\Omega\rangle\). The next physical page continues the same construction with a two-particle state.
- Diagram inventory: empty.

## Physical page 9 / 253a note page 4

### Exact TeX-ready transcription

```tex
% ===== BEGIN physical PDF page 9 / 253a note page 4 =====

\[
|\vec p_1,\vec p_2\rangle
=a_{\vec p_1}^{\dagger}a_{\vec p_2}^{\dagger}|\Omega\rangle,
\qquad \text{etc.}
\]

\[
[a,a]=[a^{\dagger},a^{\dagger}]=0,
\]

\[
[a_{\vec p},a_{\vec p'}^{\dagger}]
=\delta^{(D-1)}(\vec p-\vec p'),
\]

\[
\textcolor{gray}{
\text{so that}\qquad
\langle\vec p|\vec p'\rangle
=\delta^{(D-1)}(\vec p-\vec p')
}
\]

\noindent We can then express the Hamiltonian as

\[
H=\int d^{D-1}\vec p\,
\sqrt{\vec p^{\,2}+m^2}\,
a_{\vec p}^{\dagger}a_{\vec p}\,.
\]

\noindent $-$\quad a QM system of free relativistic\\
\hspace*{7em}particles.

\begin{center}
\textcolor{blue}{$\checkmark$}
\end{center}

\noindent $-$\quad What about interacting particles?

\[
H=H_0+H_{\mathrm{int}}.
\]

% [blue] A handwritten U-shaped connector below H_int links it to
% the following blue monomial examples. Arrowhead status: unresolved.
\[
\textcolor{blue}{
a^{\dagger}a^{\dagger}a,
\qquad aaa^{\dagger},
\qquad \cdots
}
\]

\noindent $-$\quad not easy to find $H_{\mathrm{int}}$ that\\
\hspace*{5em}respects relativistic symmetry!

% ===== END physical PDF page 9 / 253a note page 4 =====
```

### Layout and annotation inventory

- The first line begins at the top margin and continues the operator construction from physical page 8.
- The normalization line beginning “so that” is entirely light gray and sits between the momentum-space commutator and the Hamiltonian sentence.
- The blue check mark is centered below “particles.” in the free-particle bullet.
- A blue U-shaped curved connector is drawn directly below \(H_{\mathrm{int}}\). It links that term to the blue examples \(a^\dagger a^\dagger a,\,aaa^\dagger,\,\ldots\) on the next line. The handwritten examples consist of these unlabelled monomials and the ellipsis.
- The page ends after the exclamation mark in “respects relativistic symmetry!” Physical page 10 begins a new unit headed “Issue: causality.”
- Diagram inventory: empty.

## Critical source-fidelity readings

- The vanishing commutators are exactly

  $$
  [a,a]=[a^\dagger,a^\dagger]=0.
  $$

  The first bracket is \([a,a]\).
- The nonzero commutator and the gray state normalization both use the same bare spatial delta function,

  $$
  \delta^{(D-1)}(\vec p-\vec p').
  $$

  Extra normalization factors in this line: zero. In particular, \(2E_{\vec p}\) and \((2\pi)^{D-1}\) are absent.
- The free-Hamiltonian measure is exactly \(d^{D-1}\vec p\). Denominators, \(2\pi\) factors, and covariant phase-space factors are absent.
- On physical page 8, the non-interacting multiparticle line visibly reads

  $$
  H=\sum_{i=1}^{n}\sqrt{\vec p_i^{\,2}+m^2}.
  $$

  The handwritten line is a bare equality. It functions as an energy shorthand in context. A conversion to \(H|\vec p_1,\ldots,\vec p_n\rangle=(\sum_i E_{\vec p_i})|\vec p_1,\ldots,\vec p_n\rangle\) would be an editorial normalization and should receive a separate source class.
- The interaction examples are ordered \(a^\dagger a^\dagger a\) and \(aaa^\dagger\). The dagger in the second example is attached to the third \(a\).
- The source sets \(H|\Omega\rangle=0\). Vacuum-state normalization lies outside these two pages.

## Uncertainties and competing readings

| Location | Adopted reading | Competing reading | Confidence | Disposition |
|---|---|---|---:|---|
| p. 8, gray momentum note | \(p^\mu\equiv(p^0,\vec p)\) | \(p^\mu=(p^0,\vec p)\) | 0.97 | Three horizontal strokes are visible in the relation symbol; retain `\equiv`. |
| p. 8, multiparticle \(H\) line | Literal ink: \(H=\sum_i\sqrt{\vec p_i^2+m^2}\) | An implied eigenvalue equation acting on the displayed multiparticle ket | 1.00 for ink; 0.80 for implied meaning | Keep the literal line in exact transcription. Record a later normalized equation as `EQUATION_NORMALIZED` if the editor supplies the ket. |
| p. 9, first commutator | \([a,a]=[a^\dagger,a^\dagger]=0\) | \([a,a^\dagger]=[a^\dagger,a^\dagger]=0\) | 0.995 | The enlarged render shows no dagger on the second \(a\) in the first bracket. The next line separately gives \([a_{\vec p},a_{\vec p'}^\dagger]\). |
| p. 9, blue connector | U-shaped curved connector with no resolved arrowhead | Downward curved arrow | 0.88 | Preserve it as a connector in the exact layer. A diagrammatic redraw may use an arrow only if a video frame resolves an arrowhead. |
| p. 9, second blue monomial | \(aaa^\dagger\) | \(aa^\dagger a\) | 0.99 | The dagger is visibly above the third \(a\). |

Character-level readings in the black equations are resolved. The blue connector shape remains the sole graphical uncertainty.

## Likely textbook and provenance units

All proposed records below start as `NOTES_EXACT`. Spoken motivation or an oral correction can later turn a composed paragraph into `SOURCE_COMPOSITE` or `SOURCE_CONFLICT`.

| Proposed ID | Source span | Unit for chapter assembly | Atomic source content |
|---|---|---|---|
| `yin-253a-n03-u01` | note 3 / PDF 8, heading | Prelude question | Why field theory is needed for relativistic particle quantum mechanics. |
| `yin-253a-n03-u02` | note 3 / PDF 8 | Hilbert space and vacuum | \(\mathcal H\), \(\lvert\Omega\rangle\), and \(H\lvert\Omega\rangle=0\). |
| `yin-253a-n03-u03` | note 3 / PDF 8 | One-particle energy eigenstate | \(\lvert\vec p\rangle\), the gray \(D\)-dimensional momentum convention, and \(E_{\vec p}=\sqrt{\vec p^2+m^2}\). |
| `yin-253a-n03-u04` | note 3 / PDF 8 | Non-interacting multiparticle states | \(\lvert\vec p_1,\ldots,\vec p_n\rangle\) and the summed energy shorthand. |
| `yin-253a-n03-u05` | note 3 / PDF 8 through note 4 / PDF 9, first line | Creation and annihilation construction | Operator brace, one-particle state, and two-particle state. This is one source unit across the physical page break. |
| `yin-253a-n04-u01` | note 4 / PDF 9, upper third | Bosonic algebra and state normalization | Vanishing commutators, delta-function commutator, and gray inner product. |
| `yin-253a-n04-u02` | note 4 / PDF 9, middle | Free Fock-space Hamiltonian | Momentum integral and the free-relativistic-particle interpretation with blue check mark. |
| `yin-253a-n04-u03` | note 4 / PDF 9, lower middle | Interaction Hamiltonian examples | Question, \(H=H_0+H_{\mathrm{int}}\), blue connector, and the two cubic operator monomials. |
| `yin-253a-n04-u04` | note 4 / PDF 9, final lines | Relativistic-symmetry obstruction | Difficulty of finding \(H_{\mathrm{int}}\) compatible with relativistic symmetry; this leads into the causality unit on PDF 10. |
