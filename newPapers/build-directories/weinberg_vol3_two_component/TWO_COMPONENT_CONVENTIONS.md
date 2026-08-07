# Binding Two-Component Conventions

This file is authoritative for the two-component edition.  Do not import
phases or metric-dependent identities from another source without reducing
them to these definitions.

## Scope

Chapters 24–31 use two-component spinors in every four-dimensional formula.
Chapter 32 retains the irreducible spinors and Clifford matrices appropriate
to its stated spacetime dimension.  References there to the strictly
four-dimensional algebra point back to its two-component form.  Congruence
classes such as `d=4 mod 8`, which also cover higher dimensions, retain the
dimension-independent Clifford notation.

## Lorentz representations and indices

- Undotted Greek indices `alpha,beta,...` label `(1/2,0)` spinors.
- Dotted indices `dotalpha,dotbeta,...` label `(0,1/2)` spinors.
- A Majorana field is represented by one Weyl field `psi_alpha` and its
  complex conjugate `bar psi_dotalpha`; the two are not independent.
- Weinberg's original two-component `Q_a` transforms as `(0,1/2)`.  After
  lowering the standard dotted index with `epsilon_dot alpha dot beta`, it is
  written `bar Q_dotalpha` in this edition.  Its Hermitian adjoint is
  `Q_alpha`; Eq. (25.2.34) gives the component map explicitly.
- In the portions of Chapter 25 that were already derived entirely with
  two-component spinors, the original Roman component label `a` may be
  retained to avoid a gratuitous rewrite of the representation-theory
  argument.  Equation (25.2.34) gives the explicit bridge to
  `Q_alpha,bar Q_dotalpha`; no four-component generator is introduced.
- For an ordinary commuting test spinor `u_alpha`, the Hermitian contraction
  is `Q(u)=u^alpha Q_alpha-bar u_dotalpha bar Q^dotalpha`, and hence
  `Q(u)^2=-2(u sigma^mu bar u)P_mu`.  This differs in appearance from the
  plus sign used with anticommuting supersymmetry-transformation parameters,
  where reordering the Grassmann-odd factors supplies the extra sign.
- Latin `a,b,...` remain available for local Lorentz vector indices in
  supergravity.

## Metric and sigma matrices

The metric remains

```tex
\eta_{\mu\nu}=\operatorname{diag}(-1,+1,+1,+1).
```

Define

```tex
\sigma^\mu_{\alpha\dot\alpha}
  =(\mathbf 1,\sigma^1,\sigma^2,\sigma^3),
\qquad
\bar\sigma^{\mu\,\dot\alpha\alpha}
  =(\mathbf 1,-\sigma^1,-\sigma^2,-\sigma^3).
```

Consequently,

```tex
\sigma^\mu\bar\sigma^\nu+\sigma^\nu\bar\sigma^\mu
  =-2\eta^{\mu\nu}\mathbf 1,
\qquad
\bar\sigma^\mu\sigma^\nu+\bar\sigma^\nu\sigma^\mu
  =-2\eta^{\mu\nu}\mathbf 1.
```

These definitions reproduce Weinberg's matrices through

```tex
\gamma^\mu=-i
\begin{pmatrix}
0&\sigma^\mu\\
\bar\sigma^\mu&0
\end{pmatrix}.
```

They are the sign authority for every conversion.

Weinberg's explicit chirality matrix and projectors are

```tex
\gamma_5=\operatorname{diag}(+1,+1,-1,-1),
\qquad
P_L=\frac{1+\gamma_5}{2},
\qquad
P_R=\frac{1-\gamma_5}{2}.
```

With the explicit gamma matrices displayed above, this matrix equals
`-i gamma^0 gamma^1 gamma^2 gamma^3`.  A transcription of the Notation
section gives the opposite `+i` product; that product is inconsistent with
both the displayed matrix and every subsequent projector assignment.  For
this edition the explicit diagonal matrix and the `P_L/P_R` assignments are
authoritative.

## Four-to-two-component comparison dictionary

For checking a translation only, assemble two Weyl fields as

```tex
\Psi=
\begin{pmatrix}
\psi_\alpha\\
\bar\psi^{\dot\alpha}
\end{pmatrix},
\qquad
\overline\Psi
=\bigl(\psi^\alpha,\bar\psi_{\dot\alpha}\bigr).
```

For another such field
`X=(chi_alpha,bar chi^dotalpha)^{\mathsf T}`, direct block multiplication gives

```tex
\overline\Psi X
  =\psi\chi+\bar\psi\bar\chi,
```

```tex
\overline\Psi\gamma_5X
  =\psi\chi-\bar\psi\bar\chi,
```

```tex
\overline\Psi\gamma^\mu X
  =-i\left(
    \psi\sigma^\mu\bar\chi
    +\bar\psi\bar\sigma^\mu\chi
  \right),
```

```tex
\overline\Psi\gamma_5\gamma^\mu X
  =-i\left(
    \psi\sigma^\mu\bar\chi
    -\bar\psi\bar\sigma^\mu\chi
\right).
```

With the Lorentz-generator definitions above,

```tex
[\gamma^\mu,\gamma^\nu]
  =-4
  \begin{pmatrix}
    \sigma^{\mu\nu}&0\\
    0&\bar\sigma^{\mu\nu}
  \end{pmatrix},
```

and hence

```tex
\overline\Psi[\gamma^\mu,\gamma^\nu]X
  =-4\left(
    \psi\sigma^{\mu\nu}\chi
    +\bar\psi\bar\sigma^{\mu\nu}\bar\chi
  \right),
```

```tex
\overline\Psi\gamma_5[\gamma^\mu,\gamma^\nu]X
  =-4\left(
    \psi\sigma^{\mu\nu}\chi
    -\bar\psi\bar\sigma^{\mu\nu}\bar\chi
  \right).
```

In particular, Weinberg's four-component Lorentz generator
`\mathcal J^{\mu\nu}=-i[\gamma^\mu,\gamma^\nu]/4` reduces to
`i\sigma^{\mu\nu}` and `i\bar\sigma^{\mu\nu}` on the undotted and dotted
blocks.

These are ordered Grassmann expressions.  Do not swap the two spinors without
applying the appropriate anticommutation sign.  For a kinetic term, perform
integration by parts only after applying this ordered dictionary.

The same block ordering fixes discrete-symmetry signs.  In particular,

```tex
i\beta
=
\begin{pmatrix}
0&i\mathbf 1\\
i\mathbf 1&0
\end{pmatrix}
```

maps an assembled column `(psi_alpha,bar psi^dotalpha)^{\mathsf T}` to
`(i bar psi,i psi)^{\mathsf T}`.  This block check must be made before simplifying
any parity formula.

The four-component algebra

```tex
\{Q,\overline Q\}=-2iP_\mu\gamma^\mu
```

therefore has the undotted/dotted block

```tex
\{Q_\alpha,\bar Q_{\dot\beta}\}
  =-2\sigma^\mu_{\alpha\dot\beta}P_\mu
```

with the metric and momentum-index placement used in this edition.  Equivalent
forms with a raised momentum index must be obtained by applying
`eta=(-,+,+,+)`, not by dropping this sign.

## Antisymmetric spinor metric

Use

```tex
\epsilon_{12}=+1,
\qquad
\epsilon^{12}=-1,
\qquad
\epsilon_{\alpha\beta}\epsilon^{\beta\gamma}
  =\delta_\alpha{}^\gamma,
```

and the identical dotted convention.  Raise and lower indices northwest to
southeast:

```tex
\psi^\alpha=\epsilon^{\alpha\beta}\psi_\beta,
\qquad
\psi_\alpha=\epsilon_{\alpha\beta}\psi^\beta.
```

Spinor contractions are

```tex
\psi\chi=\psi^\alpha\chi_\alpha,
\qquad
\bar\psi\bar\chi
  =\bar\psi_{\dot\alpha}\bar\chi^{\dot\alpha}.
```

Factor ordering is semantic for Grassmann quantities and must not be
rearranged cosmetically.

## Lorentz generators

Unless an equation explicitly defines a different normalization, use

```tex
(\sigma^{\mu\nu})_\alpha{}^\beta
 =\frac14
  (\sigma^\mu\bar\sigma^\nu-\sigma^\nu\bar\sigma^\mu)_\alpha{}^\beta,
```

```tex
(\bar\sigma^{\mu\nu})^{\dot\alpha}{}_{\dot\beta}
 =\frac14
  (\bar\sigma^\mu\sigma^\nu-\bar\sigma^\nu\sigma^\mu)
    ^{\dot\alpha}{}_{\dot\beta}.
```

If Weinberg's original `-i[\gamma^\mu,\gamma^\nu]/4` convention introduces
an additional phase in a particular generator, show the reduction explicitly
in a source comment and preserve the original transformation law.

## Supersymmetry and superspace

Use

```tex
Q_\alpha,\quad \bar Q_{\dot\alpha},\qquad
\theta^\alpha,\quad\bar\theta^{\dot\alpha},\qquad
\mathcal Q_\alpha,\quad\bar{\mathcal Q}_{\dot\alpha},\qquad
D_\alpha,\quad\bar D_{\dot\alpha}.
```

The algebra is written in the form obtained by reducing Weinberg's
four-component algebra with the sigma matrices above.  All fermionic
derivatives remain left derivatives.  A left-chiral superfield satisfies
`\bar D_{\dot\alpha}\Phi=0`; its complex conjugate satisfies
`D_\alpha\Phi^\dagger=0`.

Use `d^2\theta`, `d^2\bar\theta`, and
`d^4\theta=d^2\theta\,d^2\bar\theta`, with coefficients fixed by
Weinberg's original D- and F-term normalizations rather than by convention
from another text.

With the epsilon convention above and left fermionic derivatives, the ordered
squares used in Chapters 26 and 30 are

```tex
\bar D^2\equiv\bar D_{\dot\alpha}\bar D^{\dot\alpha}
  =-2\bar D_{\dot1}\bar D_{\dot2},
\qquad
D^2\equiv D^\alpha D_\alpha=+2D_1D_2.
```

For a Grassmann-even superfield `S`, complex conjugation reverses the two odd
derivatives and therefore gives

```tex
(\bar D^2S)^*=D^2S^*.
```

In the component expansion used here,
`\bar D^2\bar\theta^2=D^2\theta^2=-4`.  Consequently the projection and
canonical chiral-field equations have the binding signs

```tex
[\bar D^2h]_{\mathcal F}=-2[h]_D,
\qquad
\bar D^2K_\Phi=+4f_\Phi,
\qquad
D^2K_{\Phi^*}=+4f_\Phi^*.
```

## Editorial conversion rules

1. Translate equation by equation; never globally replace `gamma`, bars, or
   chiral projectors.
2. Preserve every original equation tag and `\label`.  Pure four-component
   packaging equations may remain only as an explicitly marked comparison
   dictionary, or be replaced by an equivalent two-component identity under
   the same tag.
3. Preserve bosonic expressions verbatim unless combining real fields into
   complex fields is already part of Weinberg's own definition.
4. Replace prose only when it says that a field or calculation is
   four-component, Majorana, Dirac, left/right projected, or uses a Dirac
   adjoint.
5. In the four-dimensional chapters, `\bar\psi` means a dotted conjugate
   Weyl spinor, never a Dirac adjoint.
6. Descriptions such as "Majorana gaugino" may remain when they identify the
   physical reality condition, but the displayed field must be a Weyl
   spinor plus its conjugate.
7. Do not translate ordinary uses of Greek `\gamma` as an index, Euler's
   constant, anomalous dimensions, or dimension-dependent gamma matrices in
   Chapter 32.

## Verification gates

For every converted section:

- it compiles in the integrated master;
- its original equation-label set is unchanged unless an exception is
  documented;
- forbidden four-dimensional constructs are absent or explicitly justified:
  `\gamma^\mu`, `\gamma_5`, `P_L`, `P_R`, Dirac adjoints, four-component
  `\theta`, and `\mathcal D_L/\mathcal D_R`;
- sigma-matrix signs and factors are checked by reassembly into Weinberg's
  explicit gamma representation;
- rendered pages contain no clipped equations, collisions, black boxes, or
  broken links.
