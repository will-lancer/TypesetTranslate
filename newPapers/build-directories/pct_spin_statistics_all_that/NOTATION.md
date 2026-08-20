# Binding notation contract

This file binds the notation pass for the native edition of R. F. Streater and
A. S. Wightman's *PCT, Spin and Statistics, and All That*. It applies to the
front matter, Introduction, Chapters 1--4, Appendix, bibliographies, and index.
The printed source supplies the mathematical content. The Weinberg QFT style
supplies the presentation conventions recorded here.

The contract binds the source-faithful notation pass. It sets the Dirac
conversion for states and asymptotic labels and exposes every signature,
Fourier-phase, adjoint, conjugation, and script-letter decision for review.

LaTeX files follow this contract together with notation-map.jsonl. A formula
with a source-specific choice gets a map entry before the packet is marked
reviewed.

## Authority and reference set

The source image is the authority for glyphs, signs, accents, and layout. The
canonical file is
../../../origPapers/pct_spin_statistics_all_that.pdf, SHA-256
44fadba731cafe7f009d4e561372febb3597e1f2a4819346ce2efd16befcb889.
Rendered images under work/source-pages/ provide the page-level review
surface. Printed page 1 begins at PDF page 13.

The adopted style references are:

| Reference | Role in this edition |
| --- | --- |
| ../weinberg_vol1/latex/frontmatter/notation.tex | Primary QFT convention: mostly-plus metric, spatial boldface, Dirac states, adjoints, and mode energies. |
| ../weinberg_vol1_exercises/NOTATION.md | Operational audit rules for state products, asymptotic labels, indices, spinors, and equation references. |
| ../weinberg_vol1/latex/master.tex | Existing JHEP macros and title/layout context. |
| latex/pct.sty | PCT project helper names. Its macros are implementation points for the rules in this file. |
| PLAN.md and TRANSCRIPTION_CONTRACT.md | Source coverage, provenance, numbering, and review gates. |

The source pages inspected for this contract include PDF 016--040 (Chapter 1),
PDF 043--096 (Chapter 2), PDF 109--126 (the field axioms and Wightman
functions in Chapter 3), and PDF 146 onward (Chapter 4 and the PCT and
spin-statistics arguments). The images settle the source's old metric,
Hilbert-space tuple notation, script alphabets, field adjoints, spectral cones,
and Fourier phases.

## Fidelity rule

Transcribe the printed wording, definitions, hypotheses, conclusions, proof
steps, named results, footnotes, references, and index entries in printed
order. Reflow line endings and remove line-break hyphenation when a word
continues across the scan. A notation conversion is editorial typography when
the associated map entry identifies the source object and preserves its
mathematical role.

A source defect follows the procedure in ERRATA.md. A doubtful glyph stays
attached to a review item until the page image resolves it. The notation pass
does not repair a mathematical statement by intuition.

Each substantive native unit begins with a source marker, for example:

~~~tex
% PCT-SOURCE: pdf=109 print=99 kind=display id=3-6
~~~

The marker and the map entry use the physical PDF page, the printed folio, and
the printed equation or result number. A display spanning a source boundary
gets a marker at each boundary.

## Typography and macro discipline

Use the macros already provided by latex/pct.sty whenever they express a
semantic object. A new macro belongs in the style file only after its meaning
has been recorded here. The transcription files keep the source's symbols in
their semantic arguments. A macro name never changes meaning between chapters.

Use \mathcal for named spaces, algebras, tubes, and source script alphabets.
The Weinberg guide turns source mathscr letters into \mathcal letters. The
mathrsfs package may remain available for legacy compilation; \mathscr is not
the house form in new transcription. Use \mathbb for number fields and
coordinate spaces. Use \mathrm for labels such as in, out, PCT, and H.c. Use
\operatorname for named operations.

Boldface marks a spatial vector: \mathbf{x}, \mathbf{p}, and \mathbf{a}. A hat
marks a unit vector or a source-defined normalized object. An ordinary
four-vector has components such as x^\mu and is not bolded as a whole.
Operators are written without hats unless a source hat carries a mathematical
distinction that the map records.

The identity operator is \mathbf{1}. The symbol \mathcal P(O) denotes a
polynomial field algebra when that object occurs; the four-momentum remains
P^\mu. The scattering operator remains S; the Schwartz space remains
\mathcal S. Context and semantic macros keep the two uses separate.

## Spacetime and signature

The edition uses the Weinberg mostly-plus metric:

\[
  \eta_{\mu\nu}=\operatorname{diag}(-1,+1,+1,+1),\qquad
  x^\mu=(x^0,\mathbf{x}),\qquad x^0=t.
\]

Raising and lowering use \eta:

\[
  x_\mu=\eta_{\mu\nu}x^\nu=(-x^0,\mathbf{x}),\qquad
  x\mathbin{\cdot}y=x_\mu y^\mu=-x^0y^0+\mathbf{x}\mathbin{\cdot}\mathbf{y},
  \qquad x^2=x\mathbin{\cdot}x.
\]

Thus timelike vectors have x^2<0, spacelike vectors have x^2>0, and null
vectors have x^2=0. The d'Alembertian is

\[
  \Box=\partial_\mu\partial^\mu=\nabla^2-\partial_t^2.
\]

The Levi-Civita convention is \epsilon^{0123}=+1; lowering indices uses
\eta. A source formula written with
g_{\mu\nu}=\operatorname{diag}(+1,-1,-1,-1) is converted by the rule

\[
  g^{\mathrm{src}}_{\mu\nu}=-\eta_{\mu\nu},\qquad
  (x\mathbin{\cdot}y)_{\mathrm{src}}=-x\mathbin{\cdot}y.
\]

The conversion is recorded once for every source formula that uses the
signature. The audit follows its effect through x^2, mass shells, cones,
gamma matrices, Fourier phases, and analytic domains.

For a massive positive-energy mode, use

\[
  p^\mu=(\omega_{\mathbf p},\mathbf p),\qquad
  \omega_{\mathbf p}=\sqrt{\mathbf p^2+m^2},\qquad
  p^2=-m^2,\qquad p^0>0,
\]

and, when the source uses the invariant mass-shell measure,

\[
  \dd\Omega_m(p)=\frac{\dd^3\mathbf p}{\omega_{\mathbf p}}.
\]

The source's symbol p^2=m^2 on the old mostly-minus convention maps to the
last mass-shell equation. Every source occurrence is checked in context.

## Indices, coordinates, and representations

Greek spacetime indices \mu,\nu,\rho,\sigma range over 0,1,2,3. Latin
spatial indices i,j,k range over 1,2,3. The labels a^\mu and A retain the
source roles of a translation four-vector and a Lorentz or complex-Lorentz
matrix. Particle or field-component labels use r,s or the Greek labels chosen
by the source. A permutation is \pi.

Undotted two-spinor indices use \alpha,\beta,\gamma; dotted indices use
\dot\alpha,\dot\beta,\dot\gamma. Their positions and dottedness carry the
representation information. Internal adjoint or multiplet indices stay
lowercase Latin unless the source fixes another alphabet. Repeated indices are
contracted only where the source uses Einstein summation; an explicit finite
sum remains explicit when it is part of the source statement.

For n spacetime arguments, use x_1,\ldots,x_n with components x_j^\mu.
Relative coordinates in the translation-invariant Wightman distributions are

\[
  \xi_j=x_j-x_{j+1},\qquad j=1,\ldots,n-1.
\]

Complex coordinates use the same bilinear extension of \eta; complex
conjugation is applied to components only when a star or an explicitly defined
conjugate representation requires it.

## States, products, and domains

### Dirac state notation

Every source Hilbert-space vector that participates in a scalar product or an
operator equation becomes a ket. The direct translations are:

| Source role | House form |
| --- | --- |
| vector \Phi | \ket{\Phi} |
| vector \Psi | \ket{\Psi} |
| vacuum vector \Psi_0 | \ket{\Omega} |
| scalar product (\Phi,\Psi) | \braket{\Phi}{\Psi} |
| norm (\Phi,\Phi) | \braket{\Phi}{\Phi}=\lVert\ket{\Phi}\rVert^2 |
| matrix element (\Phi,A\Psi) | \matrixel{\Phi}{A}{\Psi} |

The product is antilinear in the bra and linear in the ket, matching the
source's scalar-product order. A source formula whose argument order carries a
special convention keeps that order and receives a map entry. Transition
probabilities use the modulus of the Dirac product, for example
\abs{\braket{\Phi'}{\Psi'}}^2.

The state space is \Hilbert, rendered as \mathcal H. Dense operator domains
retain the source names D, D_0, and D_1. They are sets of vectors, with
\ket{\Omega}\in D when the source axiom says so. A direct sum is written
\bigoplus_n\mathcal H^{(n)}. A projection onto a normalized ray is written in
operator form, for example

\[
  E_\Phi\ket{\Psi}
  =\ket{\Phi}\,\braket{\Phi}{\Psi},
  \qquad \braket{\Phi}{\Phi}=1,
\]

and the source normalization factor is retained when the source does not
assume a unit vector.

Test functions, distributions, field components, and wavefunctions remain
ordinary mathematical objects. The symbols f, g, T, \phi_j, and \psi_\alpha do
not become kets merely because they occur inside a Hilbert space formula. A
smeared field such as \phi_j(f) is an operator. Its action on a state is
\phi_j(f)\ket{\Psi}.

The source often writes a vector \Psi in a component Hilbert space as a
wavefunction \Psi^{(n)}(p_1,\ldots,p_n). That object remains a function and
does not receive ket delimiters. The source vacuum symbol \Psi_0 is a state
vector and becomes \ket{\Omega}. A packet review checks every occurrence where
the same Greek letter could denote a vector or a function.

### Operators and products

Operators use the source's upright or italic letter without a hat. Products
and matrix elements use

\[
  AB,\qquad A\ket{\Psi},\qquad
  \bra{\Phi}A\ket{\Psi},\qquad
  \braket{\Phi}{A\Psi}
\]

with the last form used only when the source explicitly treats A\Psi as the
ket argument. The unambiguous matrix-element macro is
\matrixel{\Phi}{A}{\Psi}. The identity is \mathbf 1; a
representation-specific identity keeps its subscript or representation label.
Hermiticity, self-adjointness, and domain statements retain the source's
distinctions between a symmetric operator and a self-adjoint extension.

### Adjoint, conjugate, transpose

The source uses a star for several operations. The transcription classifies
each star before typesetting it:

| Source meaning | House form | Typical PCT occurrence |
| --- | --- | --- |
| Hilbert-space adjoint of an operator | A^\dagger | \phi_j(f)^\dagger, B^\dagger |
| Entrywise complex conjugate of a scalar, matrix, or test function | A^* | f^*, S(A)^*, \gamma^{\mu *} |
| Hermitian-conjugate field at a point | \phi^\dagger(x) | local commutativity and hermiticity formulas |
| Transpose of a matrix | A^{\mathsf T} | two-spinor and representation identities |
| Complex conjugate of a spinor component | \psi^* | source passages that define a bar as componentwise conjugation |

The bar is semantic. \bar u=u^\dagger\beta is the Weinberg Dirac adjoint
when the source is using Dirac spinors in that role. A source footnote that
defines \bar\psi as ordinary complex conjugation is rendered with \psi^*.
The spinor and matrix context is checked at every bar. Entrywise conjugation
does not change an operator into its Hilbert adjoint.

For an antiunitary map \Theta,

\[
  \Theta(c\ket{\Psi})=c^*\Theta\ket{\Psi},\qquad
  \braket{\Theta\Phi}{\Theta\Psi}=\braket{\Phi}{\Psi}^*.
\]

The source's order of factors under an antiunitary transformation is preserved.
An operator relation is written with \dagger, *, or an explicit antiunitary
conjugation according to its source definition. The notation pass does not
infer an operator adjoint from an isolated star.

## In and out states

Asymptotic labels sit outside ket and bra delimiters. Use the project macros:

~~~tex
\InKet{\alpha}       % \ket{\alpha}_{\mathrm{in}}
\OutKet{\beta}       % \ket{\beta}_{\mathrm{out}}
\InBra{\alpha}       % {}_{\mathrm{in}}\!\bra{\alpha}
\OutBra{\beta}       % {}_{\mathrm{out}}\!\bra{\beta}
~~~

The paired helpers \InOutKet, \OutInKet, \InOutBra, and \OutInBra apply when
the source writes a statement for both asymptotic choices. A secondary label
remains outside the delimiters as in \InKetWith{\alpha}{\epsilon} when that
helper is available.

Source superscripts on fields, operators, and Hilbert spaces remain ordinary
superscripts: \phi^{\mathrm{in}}, \phi^{\mathrm{out}},
\mathcal H_{\mathrm{in}}, and \mathcal H_{\mathrm{out}}. Source superscripts
on state vectors become the matching helpers. A source expression such as

\[
  (\Phi^{\mathrm{out}},\Psi^{\mathrm{out}})
  =(\Phi^{\mathrm{in}},S\Psi^{\mathrm{in}})
\]

is typeset as

\[
  \OutBra{\Phi}\OutKet{\Psi}
  =\InBra{\Phi}\,S\InKet{\Psi},
\]

with the printed product order preserved. The surrounding prose controls the
author's direction for the S-operator. A map entry records any explicit
operator action introduced for readability.

## Fourier and distribution conventions

### Euclidean test-function spaces

In Chapter 2, formulas on \mathbb R^n use the Euclidean dot product
p\mathbin{\cdot_E}x=\sum_{j=1}^n p_jx_j. Source \mathscr S and
\mathscr D become \mathcal S and \mathcal D:

\[
  \mathcal S(\mathbb R^n),\qquad
  \mathcal D(\mathbb R^n),\qquad
  \mathcal S'(\mathbb R^n),\qquad
  \mathcal D'(\mathbb R^n).
\]

The normalized Fourier pair keeps the authors' symbols while making each sign
visible in the definition:

\[
  (\mathcal Ff)(p)
  =(2\pi)^{-n/2}\int e^{-\ii p\cdot_E x}f(x)\,\dd^nx,
  \qquad
  (\overline{\mathcal F}f)(p)
  =(2\pi)^{-n/2}\int e^{+\ii p\cdot_E x}f(x)\,\dd^nx.
\]

Inversion, derivative, convolution, delta, and duality formulas retain the
source's symbols and normalization. A packet review checks the sign against
the displayed definition.

### Minkowski phases

The source uses the old mostly-minus contraction in Chapter 3 and in the
analytic-domain arguments. With the house metric,

\[
  p\mathbin{\cdot_{\rm src}}x=-p\mathbin{\cdot}x.
\]

Therefore a source phase is translated by the operational rule

\[
  e^{\sigma\,\ii p\cdot_{\rm src}x}
  \longmapsto e^{-\sigma\,\ii p\cdot x},
  \qquad \sigma\in\{+1,-1\}.
\]

Minkowski transforms retain the source's names. Their house-metric definitions
show the converted sign explicitly, and each source-specific phase receives a
notation-map entry.

\[
  (\mathcal FF)(p)=\int e^{-\ii p\cdot x}F(x)\,\dd^4x,
  \qquad
  (\overline{\mathcal F}F)(p)=\int e^{+\ii p\cdot x}F(x)\,\dd^4x.
\]

The source normalization, the number of variables, and any delta factor stay
as printed. A source display chooses the matching transform sign through the
phase rule. Important checked examples are:

| Source display or role | House phase |
| --- | --- |
| source e^{-\ii p\cdot_{\rm src}x} in the test-function transform, such as printed (3-15) | e^{+\ii p\cdot x} |
| source e^{+\ii\sum_j p_j\cdot_{\rm src}x_j} in the Wightman transform, such as printed (3-29) | e^{-\ii\sum_j p_j\cdot x_j} |
| source e^{+\ii\sum_j q_j\cdot_{\rm src}\xi_j} in the relative-coordinate transform, such as printed (3-30) | e^{-\ii\sum_j q_j\cdot\xi_j} |
| source e^{-\ii\sum_j(\zeta_j-\ii\eta_j)\cdot_{\rm src}q_j} in the Laplace proof | e^{+\ii\sum_j(\zeta_j-\ii\eta_j)\cdot q_j} |

The table records source-specific sign decisions. It does not authorize a
global phase replacement. Every display containing e^{\pm\ii p\cdot x},
\Box, spectral support, or a cone receives a map entry.

## Spectral cones and analytic domains

The future cone in house signature is

\[
  V_+=\{p\in\mathbb R^{1,3}:p^2<0,\ p^0>0\},
  \qquad V_-=-V_+,
\]

with \overline V_+ and \overline V_- denoting the closures. The source phrase
“plus cone” and source condition p^2>0, p^0>0 use the old mostly-minus
signature and map to this definition. The spectral condition is checked in the
momentum variables used by each theorem.

For relative coordinates, the forward tube uses

\[
  \mathcal T_{n-1}
  =\{(\zeta_1,\ldots,\zeta_{n-1}):
      \zeta_j=\xi_j-\ii\eta_j,\ \eta_j\in V_+\}.
\]

The extended tube is \mathcal T'_{n-1}. Boundary values are distributional
limits as all \eta_j\to0 through V_+. A complex dot product is bilinear with
respect to \eta; it is not a Hermitian product. Jost-point and permutation
statements keep the source's real spacelike inequalities after the signature
conversion. A source \zeta^2<0 spacelike condition becomes \zeta^2>0 in the
house metric.

## Spinors, gamma matrices, and PCT symbols

The Clifford convention follows Weinberg:

\[
  \{\gamma^\mu,\gamma^\nu\}=2\eta^{\mu\nu},
  \qquad \beta=\ii\gamma^0,
  \qquad \bar u=u^\dagger\beta.
\]

The source gamma relation is checked through g_{\rm src}=-\eta; a source
factor already tied to its Dirac equation receives a formula-level map entry.
The source's charge-conjugation matrix is written with entrywise conjugation,
for example

\[
  C\gamma^\mu C^{-1}=-\gamma^{\mu *},
\]

when that is the relation printed in the relevant representation. A transpose
is \mathsf T, and a Hermitian adjoint is \dagger.

Two-spinor matrices retain the source's A, Pauli matrices, dotted and
undotted indices, and tensor-representation labels such as
D^{(j/2,k/2)}. A source A^* in an SL(2,\mathbb C) representation is entrywise
conjugation. A source A^{\mathsf T} is transpose. The notation map keeps these
operations distinct.

The theorem name and prose use the source's exact discrete-symmetry ordering.
Occurrences printed as CPT remain CPT. Occurrences printed as PCT remain PCT.
The project title and the later PCT theorem retain PCT. CPT and PCT remain
exactly as printed at each occurrence. Discrete transformations retain the source symbols
P, C, T, I_s, I_t, U(I_s), U(C), U(I_t), and \Theta when those symbols occur.
The product order and phase choices in a discrete-symmetry formula are
source-specific. The operator \Theta is antiunitary wherever the source states
that property, with the rule in the adjoint section.

## AQFT and field-theory glossary

The following meanings are stable across all chapters. A symbol enters the
glossary when the source introduces it; the list does not add assumptions to
the source axioms.

| Object | House rendering and meaning |
| --- | --- |
| Hilbert state space | \Hilbert=\mathcal H |
| Vacuum | \ket{\Omega} |
| Operator domains | D, D_0, D_1, as source-defined dense domains |
| Test functions | \TestFunctions=\mathcal D, with \mathcal D(O) for compact support in O |
| Schwartz space | \Schwartz=\mathcal S; its continuous dual is \mathcal S' |
| Distribution space | \mathcal D' for the dual of \mathcal D |
| Polynomial local algebra | \PolynomialAlgebra(O)=\mathcal P(O) |
| Observable/local algebra | \Algebra(O)=\mathcal A(O) only where the source defines it |
| Full vacuum expectation distribution | \mathcal W_n(x_1,\ldots,x_n) |
| Translation-invariant relative distribution | W_n(\xi_1,\ldots,\xi_{n-1}) |
| Permuted Wightman distribution | W_{n,\pi} or the source's explicit W_\pi |
| Forward tube | \Tube_{n-1}=\mathcal T_{n-1} |
| Extended tube | \ExtendedTube_{n-1}=\mathcal T'_{n-1} |
| Borchers class | \BorchersClass=\mathcal B |
| Spectrum and support | \Spectrum and \supp |
| Field components | \phi_j, \psi_\alpha, or the source's component symbols |
| Smeared field | \phi_j(f) |
| Fermion parity | (-1)^F, with the source's integer and half-odd-integer spin assignment |

The semantic helper \Wightman anchors the full vacuum expectation object in
the LaTeX source. Its visual alphabet follows this glossary: the full object
is \mathcal W_n, while a plain W_n denotes the relative-coordinate
distribution. The helper's implementation may supply the visual \mathcal
styling without changing its meaning.

The source's \mathcal H^{\rm in} and \mathcal H^{\rm out} become
\mathcal H_{\mathrm{in}} and \mathcal H_{\mathrm{out}} when they denote the
asymptotic spaces. The source's script \mathcal P remains distinct from
momentum P^\mu. A script symbol with a new local definition receives a project
glossary entry before use.

Field products are read as operator products. A vacuum expectation is written
in Dirac order:

\[
  \mathcal W_n(x_1,\ldots,x_n)
  =\bra{\Omega}\phi_1(x_1)\cdots\phi_n(x_n)\ket{\Omega}.
\]

The source's \phi_j^*(x) in a hermiticity or locality statement becomes
\phi_j^\dagger(x) when it denotes the adjoint field. The source's scalar or
matrix stars in the same theorem retain *. This distinction is central to the
spectral and local-commutativity formulas.

## Printed numbering and cross-references

Printed chapter equation numbers remain visible as (1-1), (2-1), (3-1), and so
on. Use \tag{3-29} or the project equation machinery when the source number is
fixed, and assign a semantic label such as \label{eq:ch3-wightman-fourier}.
The label name is implementation metadata; the printed number is the source
locator.

Theorem, lemma, proposition, definition, example, and remark headings preserve
the printed chapter number, such as Theorem 4-1. A named result that is
unnumbered in the scan remains unnumbered. Section labels preserve forms such
as 3-3. Source references to an equation or theorem use the printed form in
prose, with a linked semantic reference in LaTeX.

An equation that is split across source pages remains one equation. A display
that has no printed number does not receive a new number for visual symmetry.
The source marker records every page boundary.

## Source-specific exception workflow

The notation map is JSON Lines. Each line describes one source formula or one
short, tightly related prose decision. The fields are:

~~~json
{
  "source_page": {"pdf": 109, "print": 99},
  "locator": "eq:3-4",
  "source_form": "g=diag(+1,-1,-1,-1); (Phi,Psi)",
  "house_form": "eta=diag(-1,+1,+1,+1); braket{Phi}{Psi}",
  "class": "metric|state|adjoint|conjugate|fourier|script|inout|cone|spinor",
  "reason": "house convention with source meaning preserved",
  "verification": "image checked",
  "status": "reviewed"
}
~~~

The actual file uses valid escaped JSON strings and one object per line. The
following decisions always need entries:

1. a source scalar-product tuple converted to a bra-ket;
2. a source state superscript converted to an in/out delimiter helper;
3. a source star, bar, or overbar classified as an adjoint or conjugate;
4. an old-metric quadratic form, mass shell, gamma identity, or cone;
5. a Minkowski Fourier, Laplace, or mode phase;
6. a source script alphabet converted to a \mathcal macro;
7. a source operator or space whose symbol could collide with a house macro;
8. a source-specific PCT phase, representation convention, or spinor identity.

The packet reviewer checks the source image, the native formula, the map entry,
and the neighboring prose. A semantic ambiguity is placed in
work/reviews/notation-source-findings.md with both page locators. The
transcription stays pending until the review file records a decision. An
accepted correction also gets the ERRATA.md record required by the project
contract.

## Audit checklist

Run the notation audit after each chapter packet and before the strict build.
The audit and visual review cover:

- every state product, norm, transition probability, projection, and matrix
  element;
- every vacuum vector, dense domain, in/out state, field superscript, and
  collision-state relation;
- every *, bar, transpose, dagger, antiunitary map, and Dirac adjoint;
- every source script letter, Schwartz or test-function space, algebra, tube,
  Wightman distribution, and Borchers class;
- every occurrence of x^2, p^2, a cone, a spectral-support statement,
  \Box, \epsilon^{0123}, or a mass-shell measure;
- every Fourier or Laplace phase and its normalization;
- every dotted or undotted index, gamma identity, charge-conjugation relation,
  discrete-symmetry product, and spin-statistics sign;
- printed equation and theorem numbers, source markers, semantic labels, and
  page-boundary continuity.

The scan should find no raw Hilbert-space tuple used as a state product, no
asymptotic label inside a ket or bra argument, no unclassified star, no source
metric without a map entry, no source \mathscr letter in new material, and no
cone or Fourier phase whose signature decision is implicit.
