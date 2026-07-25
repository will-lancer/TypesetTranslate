# Weinberg Vol. III - Notation Modernization Guide

Binding notation policy for Steven Weinberg, *The Quantum Theory of Fields*,
Volume III (*Supersymmetry*).

The rendered scan is authoritative for wording, mathematics, equation
numbering, signs, and factor ordering. OCR is only an aid. This guide supplies
the deliberately modernized presentation layer inherited from Volumes I and II
and the additional spinor, superspace, and supergravity conventions required by
Volume III.

## House rules inherited from Volumes I and II

- Use `\mathbb{R}`, `\mathbb{C}`, `\mathbb{Z}`, `\mathbb{Z}_2`, and analogous
  blackboard-bold notation for standard number systems, spaces, and discrete
  groups. Keep generic groups such as `G` and `H` italic.
- Use `\mathbf{1}` for an identity matrix or operator, never `\mathbb{1}`.
- Use `\cdot`, never `\times`, for direct products, Cartesian products, and
  matrix dimensions in this edition.
- Use `\mathcal`, not `\mathscr`, for Lagrangian densities, Hamiltonian
  densities, superspace operators, and other applicable calligraphic symbols.
- Use the project command `\sl{p}` for Dirac slashes. Do not use `\not p`.
- Keep Weinberg's mostly-plus metric,
  `\eta_{\mu\nu}=\operatorname{diag}(-1,+1,+1,+1)`, with modern component
  order `(0,1,2,3)`. Thus `p^2=-m^2`,
  `\Box=\nabla^2-\partial_t^2`, and spacelike separations have nonnegative
  squared interval.
- Use boldface for three-vectors.
- Use Dirac notation for states, with double bars as in the existing project:
  `\ket{\Psi}`, `\bra{\Phi}`, and `\braket{\Phi}{\Psi}`. Use
  `\ket{\Omega}` for the vacuum.
- Put momentum, spin, species, and similar labels on creation and annihilation
  operators in subscripts.
- Use `\mathcal{P}` and `\mathcal{T}` only for spacetime inversion matrices,
  and `P=U(\mathcal{P},0)`, `T=U(\mathcal{T},0)` for Hilbert-space operators.
  Do not mechanically rewrite unrelated uses of `P`, `T`, or `R`.
- Convert superscript paper-reference markers to linked bracketed markers
  before terminal punctuation, for example `[1]`, `[3a]`, or `[4-7]`.
  Preserve chapter-local reference numbering exactly.
- Give every numbered equation and figure a stable label and use `\eqref` or
  `\ref` in prose. Give every displayed chapter reference a stable target.
- Use ordinary automatically numbered footnotes. Do not reproduce source
  `*`, `**`, or dagger footnote symbols and never rewind the counter.
  Section-title notes use an ordinary `\footnotemark`/`\footnotetext` pair and
  a clean optional table-of-contents title.
- Preserve source three-asterisk dividers as typographic section breaks; do
  not confuse them with footnote markers.
- Remove scan-induced line-wrap hyphenation, but do not paraphrase, summarize,
  silently correct, or omit source content.

## Volume III spinor conventions

Volume III uses four-component Dirac/Majorana notation almost everywhere.
Only the initial construction of the algebra and multiplets in Chapter 25 uses
two-component Weyl notation.

- Two-component spinor indices are `a,b,\ldots`.
- Four-component spinor indices are `\alpha,\beta,\ldots`.
- Uppercase `A,B,\ldots` label symmetry or gauge-algebra generators. This is an
  explicit departure from Volume II. Lowercase `t_A` denotes representation
  matrices.
- Preserve the source's deliberate typographic distinction between the
  two-component supercharges and the assembled four-component Majorana
  supercharges. Define separate macros in the owning chapter rather than
  relying on a visually ambiguous bare `Q`.
- The two-component antisymmetric matrix is
  `e=i\sigma_2`, with `e_{12}=+1`.
- The four-component Majorana matrix is a separate symbol,
  `\epsilon=\operatorname{diag}(e,e)`.
- Do not confuse either object with the Levi-Civita tensor
  `\epsilon^{\mu\nu\rho\sigma}` or the vierbein `e_\mu{}^a`.

## Clifford and chirality conventions

Keep the source's mostly-plus Clifford conventions exactly:

- `\{\gamma^\mu,\gamma^\nu\}=2\eta^{\mu\nu}`.
- `\epsilon^{0123}=+1`.
- `\beta=i\gamma^0=\gamma_4`.
- `\gamma_5` is diagonal with eigenvalues `(+1,+1,-1,-1)`.
- The chiral projectors are
  `P_L=(\mathbf{1}+\gamma_5)/2` and
  `P_R=(\mathbf{1}-\gamma_5)/2`.

The signs in these projectors are the reverse of conventions common in some
other QFT texts. Never flip them.

When explicit matrices are needed, preserve the source representation:

```tex
\gamma^0=-i\begin{pmatrix}0&\mathbf{1}\\ \mathbf{1}&0\end{pmatrix},
\qquad
\gamma^i=-i\begin{pmatrix}0&\sigma^i\\-\sigma^i&0\end{pmatrix}.
```

## Majorana conventions

For a two-component spinor `\chi`, the four-component Majorana spinor has the
source form

```tex
\psi=\begin{pmatrix}e\chi^*\\ \chi\end{pmatrix}.
```

Preserve the associated reality, adjoint, phase, and Fierz conventions,
including

```tex
s^*=-\beta\gamma_5\epsilon s,
\qquad
\bar{s}=s^\dagger\beta=s^T\epsilon\gamma_5.
```

The appendix to Chapter 26 is authoritative for all further Majorana
identities. Do not import phase conventions from another supersymmetry text.

## Conjugation, transpose, and adjoint

The scan overloads asterisks. Modernize semantically, never through global
replacement:

- `z^*` is complex conjugation of a number or c-number field.
- `A^T` is matrix transpose.
- `A^\dagger` is the Hermitian adjoint.
- Write operator adjoints with explicit indices when needed.
- Keep `s^*` in the Majorana reality condition.
- Keep `\Phi^*` for the complex-conjugate/right-chiral superfield where used.
- Keep `+\mathrm{H.c.}` distinct from `+\mathrm{c.c.}`.

Antighosts, antifields, complex conjugates, and Hermitian adjoints remain
different concepts. If BV antifields recur, retain the Volume II convention
`x_n^{\ddagger}`.

## Graded algebras and Grassmann variables

- Preserve the grading `\eta_A\in\{0,1\}` and all graded signs.
- Define a dedicated macro for the generalized bracket `[A,B\}` and use it
  consistently.
- Preserve every super-Jacobi sign and factor ordering.
- Grassmann conjugation reverses order:
  `(\alpha\beta)^*=\beta^*\alpha^*`.
- In Section 25.1, the normal repeated-index summation convention is
  explicitly suspended where the source says so. Do not silently sum.

## Superspace conventions

- `\theta_\alpha` is a four-component Majorana Grassmann c-number.
- All derivatives with respect to fermionic variables are left derivatives.
  Move the differentiated variable to the left before differentiating.
- Factor ordering is semantic and must not be rearranged cosmetically.
- Distinguish the supercharge `Q_\alpha`, the superspace differential operator
  `\mathcal{Q}_\alpha`, and the covariant superderivative
  `\mathcal{D}_\alpha`.
- Preserve `\mathcal{D}_L`, `\mathcal{D}_R`, their projections, and their
  anticommutators.

Weinberg's terminology is source-specific:

- A generic "chiral" superfield may be the sum of left- and right-chiral
  pieces.
- A left-chiral field `\Phi` satisfies `\mathcal{D}_R\Phi=0`.
- The right-chiral field `\Phi^*` satisfies
  `\mathcal{D}_L\Phi^*=0`.

Do not silently translate "chiral" into the convention of texts where it means
only left-chiral.

## Berezin integration and D/F terms

Preserve the source normalizations and ordering:

```tex
\int d^4x\,[S]_D
=-\frac12\int d^4x\,d^4\theta\,S,
```

```tex
\int d^4x\,[\Phi]_F
=+\frac12\int d^4x\,d^2\theta_L\,\Phi.
```

Grassmann integration selects the coefficient after all integrated theta
factors have been moved left. Fermionic changes of variables use the inverse
determinant. Do not substitute normalization conventions from another text.

## Collision map

Preserve these distinctions explicitly:

- `e`: the two-component antisymmetric spinor matrix.
- `\epsilon`: the four-component Majorana matrix.
- `\epsilon^{\mu\nu\rho\sigma}`: the Levi-Civita tensor.
- `e_\mu{}^a` and `e=\det(e_\mu{}^a)`: the vierbein and its determinant.
- `D`: dilation generator.
- `D_\mu`: spacetime/gauge covariant derivative.
- `\mathcal{D}_\alpha`: superspace covariant derivative.
- `D_A`: auxiliary gauge-multiplet field.
- `[\;]_D`: D-term projection.
- `F`: auxiliary chiral-multiplet field when so used.
- `[\;]_F`: F-term projection.
- `F_{\mu\nu}`: gauge-field strength.
- `\beta=i\gamma^0`: Dirac matrix.
- `\beta`: MSSM scalar-sector angle, only where context defines it.
- `R`: curvature scalar, R-symmetry generator, or other source-defined object;
  disambiguate locally without changing meaning.

## General covariance and higher dimensions

- In Chapter 31, use `\mu,\nu,\ldots` for general-coordinate indices and
  `a,b,\ldots` for local Lorentz indices.
- Where the source explicitly uses `i=1,\ldots,4` with `x^4=it`, preserve the
  derivation's meaning while applying the project-wide modern component order
  cautiously.
- The Chapter 32 appendix uses dimension-dependent gamma-matrix
  representations that are not the book's four-dimensional representation.
  Preserve all phases, definitions of `\gamma_{2n+1}`, real/pseudoreal
  classifications, and separate even/odd dimensional cases.

## Source-quality warning

The PDF is a crisp image scan with an unreliable invisible OCR layer. Common
OCR corruptions include:

- `SU` read as `517`;
- `U` read as `17`;
- `O` read as `0`;
- missing spaces;
- lost Greek or calligraphic glyphs;
- missing stars, daggers, exponents, matrix entries, and D/F-term notation.

Rendered pages, not extracted text, decide every uncertainty.
