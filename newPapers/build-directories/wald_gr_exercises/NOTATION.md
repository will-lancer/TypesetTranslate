# Wald GR notation policy

This file is binding. The edition preserves Wald's abstract-index method and
mathematical conventions while applying only the changes authorized below.
Do not import the Weinberg GR notation policy into this project.

## Conventions retained from Wald

### Abstract indices

Lowercase Latin indices

\[
  a,b,c,d,\ldots
\]

remain abstract tensor indices. They label tensor slots and do not denote
basis components. Greek indices

\[
  \mu,\nu,\rho,\sigma,\ldots
\]

remain component indices. Preserve the semantic distinction explained in
Section 2.4.

### Metric signatures

Preserve Wald's mostly-plus signature

\[
  (-+++)
\]

throughout the book except Chapter 13. Preserve Wald's deliberate Chapter 13
spinor convention

\[
  (+---).
\]

Do not silently carry formulas between Chapter 13 and the rest of the book.
Every such use must be checked with the source's stated sign rules.

### Curvature

Preserve Wald's Riemann tensor notation and definition:

\[
  (\nabla_a\nabla_b-\nabla_b\nabla_a)\omega_c
  =R_{abc}{}^{d}\omega_d.
\]

Preserve the index order \(R_{abc}{}^d\), the Ricci contraction

\[
  R_{ac}=R_{abc}{}^b,
\]

and all associated signs. Do not convert these objects to an output-first
curvature convention.

### Derivative operators

Preserve Wald's use of \(\partial_a\) for an ordinary derivative operator and
\(\nabla_a\) for a general derivative operator. This notation is intentional
and is not a modernization target.

### Other retained systems

- Preserve Wald's pushforward and pullback conventions from Appendix C.
- Preserve the cosmological notation of Chapter 5.
- Preserve \(h_{ab}\), \(K_{ab}\), Wald's extrinsic-curvature sign, and the ADM
  conventions of Sections 9.3 and 10.2 and Appendix E.
- Preserve the exterior derivative \(d\), wedge product \(\wedge\), and Hodge
  dual.
- Preserve geometrized units and restore constants only where the source does.
- Preserve \(e\) for Kerr--Newman charge and Wald's spinor curvature scalar
  notation unless a later explicit project decision changes them.

## Required modernizations

### Tangent and cotangent spaces

Replace

\[
  V_p\longrightarrow T_pM,
  \qquad
  V_p^*\longrightarrow T_p^\vee M.
\]

Use *covector* or *one-form* for an element of \(T_p^\vee M\), rather than
*dual vector*. The term *dual space* remains appropriate for \(T_p^\vee M\).

Use \(\vee\), not \(*\), for every algebraic dual-space symbol:

\[
  V^\vee,\qquad V^{\vee\vee},\qquad T_p^\vee M.
\]

This rule does not alter stars with other meanings, such as Wald's maps
\(\phi^*\), Hodge duality, adjoints, or complex conjugation.

For a basis of \(T_pM\), use

\[
  \{e_\mu\}.
\]

Write its dual basis in \(T_p^\vee M\) as \(\{f^\mu\}\), normalized by

\[
  f^\mu(e_\nu)=\delta^\mu{}_{\nu}.
\]

Do not use \(v_\mu\) and \(v^{\mu *}\) for these basis elements.

### Smooth functions and tensor spaces

Write the smooth real-valued functions on \(M\) as

\[
  C^\infty(M)
\]

unless the codomain must be shown explicitly, in which case use
\(C^\infty(M,\mathbb R)\).

Preserve Wald's tensor-space notation but use calligraphic typography:

\[
  \mathcal T(k,l).
\]

### Differential-form spaces

Wald's abbreviated pointwise notation is replaced by the explicit exterior
power of the cotangent space:

\[
  \Lambda_x^p\longrightarrow\Lambda^pT_x^\vee M.
\]

The space of smooth \(p\)-form fields is written

\[
  \Lambda^p\longrightarrow\Omega^p(M)
  =\Gamma\!\left(\Lambda^pT^\vee M\right).
\]

This conversion changes only the names of the spaces. It does not change an
individual form, the wedge product, \(d\), integration, orientation, or Hodge
duality.

### Spatial-vector typography

Do not use `\vec`. Use `\mathbf` for Latin spatial vectors and `\boldsymbol`
for Greek spatial vectors or operators. For example,

\[
  \mathbf E,\quad \mathbf A,\quad \mathbf x,
  \qquad
  \boldsymbol{\nabla},\quad \boldsymbol{\pi},\quad
  \boldsymbol{\omega}.
\]

### Sets and topology

Replace Wald's dotted boundary notation by

\[
  \dot S\longrightarrow\partial S.
\]

This rule applies only when the dot denotes a set boundary. A genuine time or
parameter derivative remains dotted.

Write the image of a set as \(f(A)\), rather than \(f[A]\). Replace ambiguous
\(\subset\) with \(\subseteq\) or \(\subsetneq\), according to the source's
meaning. Preserve \(\overline S\), \(\operatorname{int}(S)\), unions, and
intersections.

### Lie derivatives

Use

\[
  \mathcal L_v
\]

for the Lie derivative with respect to \(v^a\). Do not use a pound sign or
`\pounds`.

### Metric perturbations

Replace Wald's metric perturbation and its trace reverse by

\[
  \gamma_{ab}\longrightarrow h_{ab},
  \qquad
  \overline\gamma_{ab}\longrightarrow\overline h_{ab}.
\]

The induced spatial metric also remains \(h_{ab}\). If both meanings occur in
one local discussion, use \(\delta g_{ab}\) for the perturbation or state the
distinction explicitly. Never leave an ambiguous \(h_{ab}\).

### Gauge names

Use *Lorenz gauge* for electromagnetism. Reserve *Lorentz* for the spacetime
group and transformations. Call the corresponding gravitational condition
the *de Donder gauge* or *harmonic gauge*, according to context.

### Calligraphic typography

All source script letters are typeset with `\mathcal`, not `\mathscr`.
This applies globally, including null infinity, function and tensor spaces,
Hilbert and Fock spaces, trapped-region symbols, and Lagrangian or Hamiltonian
densities. The semantic symbol may change separately under another binding
rule; for example, Wald's smooth-function symbol becomes \(C^\infty(M)\), not
\(\mathcal F\).

No `\mathscr` command may appear in the LaTeX tree.

## Standard replacement table

| Source | Target |
|---|---|
| \(V_p\) | \(T_pM\) |
| \(V_p^*\) | \(T_p^\vee M\) |
| algebraic dual \(V^*\) | \(V^\vee\) |
| double dual \(V^{**}\) | \(V^{\vee\vee}\) |
| tangent-space basis \(\{v_\mu\}\) | \(\{e_\mu\}\) |
| dual basis \(\{v^{\mu *}\}\) | \(\{f^\mu\}\) |
| dual vector | covector or one-form |
| script smooth-function symbol | \(C^\infty(M)\) |
| script tensor space | \(\mathcal T(k,l)\) |
| \(\Lambda_x^p\) | \(\Lambda^pT_x^\vee M\) |
| \(\Lambda^p\), space of smooth form fields | \(\Omega^p(M)\) |
| arrowed Latin vector \(\vec X\) | \(\mathbf X\) |
| arrowed Greek vector/operator \(\vec\omega\) | \(\boldsymbol\omega\) |
| \(\dot S\), boundary | \(\partial S\) |
| \(f[A]\) | \(f(A)\) |
| ambiguous \(\subset\) | \(\subseteq\) or \(\subsetneq\) |
| pound-sign Lie derivative | \(\mathcal L_v\) |
| \(\gamma_{ab}\), metric perturbation | \(h_{ab}\) |
| \(\overline\gamma_{ab}\) | \(\overline h_{ab}\) |
| Lorentz gauge | Lorenz gauge |
| gravitational Lorenz analogue | de Donder or harmonic gauge |
| any script alphabet | corresponding \(\mathcal{...}\) form |

## Section completion check

For every completed section:

1. Verify every Latin tensor index is still abstract and every Greek index is
   genuinely a component index.
2. Verify Wald's curvature order and sign were preserved.
3. Verify Chapter 13 uses its source signature and other chapters do not.
4. Apply every required modernization above consistently in prose, displays,
   figures, problems, and index entries.
5. Run `audit_notation.py` and review all nonfatal candidates.
6. Compile and compare the rendered mathematics with the source page.
