# Notation and convention policy

This edition uses natural units with `\hbar=c=1` and the mostly-plus metric

```tex
\eta_{\mu\nu}=\operatorname{diag}(-,+,\ldots,+).
```

Greek spacetime indices run over `0,\ldots,D-1`; Latin spatial indices run over
`1,\ldots,D-1`. The symbol `D` always denotes the physical spacetime dimension.
Dimensional regularization uses `d_{\mathrm{reg}}=D-\varepsilon_{\mathrm{UV}}`,
with `d_{\mathrm{reg}}=4-\varepsilon_{\mathrm{UV}}` in the four-dimensional
applications.

## Lorentzian formulas

For `p^\mu=(E_{\mathbf p},\mathbf p)` and
`x^\mu=(t,\mathbf x)`,

```tex
p\mathbin{\cdot}x=-E_{\mathbf p}t+\mathbf p\mathbin{\cdot}\mathbf x,
\qquad
p^2=-m^2,
\qquad
E_{\mathbf p}=\sqrt{\mathbf p^2+m^2}.
```

The d'Alembertian is
`\Box=\partial_\mu\partial^\mu=-\partial_t^2+\boldsymbol\nabla^2`.
Positive-frequency plane waves use `\mathrm e^{\mathrm i p\cdot x}`. A free
real scalar has

```tex
\mathcal L_0=-\frac12\partial_\mu\phi\,\partial^\mu\phi
             -\frac12m^2\phi^2,
\qquad
(\Box-m^2)\phi=0,
```

and the Feynman factor is

```tex
\widetilde D_F(p)=\frac{-\mathrm i}{p^2+m^2-\mathrm i0}.
```

For a massive vector, physical polarizations have positive norm and obey

```tex
\sum_r\epsilon_{(r)}^\mu(p)\epsilon_{(r)}^{\nu *}(p)
=\eta^{\mu\nu}+\frac{p^\mu p^\nu}{m^2}.
```

The Proca mass term is `-m^2 A_\mu A^\mu/2`. Its covariant propagator is
`-\mathrm i(\eta_{\mu\nu}+p_\mu p_\nu/m^2)/(p^2+m^2-\mathrm i0)`.
The massless Feynman-gauge factor is
`-\mathrm i\eta_{\mu\nu}/(p^2-\mathrm i0)`.

## Spinors

The Clifford algebra and slash convention are

```tex
\{\gamma^\mu,\gamma^\nu\}=-2\eta^{\mu\nu},
\qquad
\slashed p=\gamma^\mu p_\mu.
```

This choice retains the displayed Weyl, Dirac, and Majorana matrices used in
Appendix C. With `\bar\psi=\psi^\dagger\gamma^0`, the compatible free
Lagrangian, equation, on-shell spinor equation, and propagator are

```tex
\mathcal L_D=-\bar\psi(\mathrm i\slashed\partial+m)\psi,
\qquad
(\mathrm i\slashed\partial+m)\psi=0,
\qquad
(\slashed p-m)u(p)=0,
```

```tex
S_F(p)=\frac{\mathrm i}{\slashed p-m+\mathrm i0}
=\frac{-\mathrm i(\slashed p+m)}{p^2+m^2-\mathrm i0}.
```

With the Appendix C state normalization, the spin sums are

```tex
\sum_s u(p,s)\bar u(p,s)=-(\slashed p+m),
\qquad
\sum_s v(p,s)\bar v(p,s)=-(\slashed p-m).
```

Writing `\mathcal D=-\mathrm i\slashed\partial-m`, the time-ordered
propagator satisfies
`\mathcal D_x S_F(x-y)=\mathrm i\delta^D(x-y)`. A PDE Green function
normalized by `\mathcal D_xG(x-y)=\delta^D(x-y)` differs by the stated
factor of `\mathrm i`.

Four-dimensional chirality formulas are labeled `D=4`. There
`\gamma_5=\mathrm i\gamma^0\gamma^1\gamma^2\gamma^3` and
`\epsilon^{0123}=+1`, hence `\epsilon_{0123}=-1`. More generally, the chosen
orientation is `\epsilon^{01\ldots D-1}=+1`.

## Wick rotation

The Lorentzian contour rotation uses

```tex
t=-\mathrm i\tau,
\qquad
p^0=\mathrm i p_4,
\qquad
p_0=-\mathrm i p_4,
\qquad
\dd p^0=\mathrm i\,\dd p_4.
```

Thus `p^2` continues to `p_E^2=p_4^2+\mathbf p^2`, and the positive-frequency
phase continues as

```tex
\mathrm e^{\mathrm i p\cdot x}
\longrightarrow
\mathrm e^{-\mathrm i p_4\tau+\mathrm i\mathbf p\cdot\mathbf x}.
```

For spinors, `\gamma_E^4=-\gamma^0` and `\gamma_E^i=\mathrm i\gamma^i`, so
`\{\gamma_E^A,\gamma_E^B\}=2\delta^{AB}`. Local Euclidean rules state whether
they invert the Euclidean differential operator or include the correlator
normalization.

## Measures, states, and typography

Spatial vectors are bold in text, states, phases, derivatives, figures, and
integration variables. Their energy labels are bold as well. The invariant
positive-shell measure is

```tex
\frac{\dd^{D-1}\mathbf p}{(2\pi)^{D-1}2E_{\mathbf p}},
```

and Banks's delta-function state normalization becomes

```tex
\langle \mathbf p,r\mid\mathbf q,s\rangle
=\delta_{rs}\delta^{D-1}(\mathbf p-\mathbf q).
```

Ordinary italic letters denote spacetime vectors. Adjacent lower and upper
tensor indices carry an empty group, as in `T^\mu{}_\nu`,
`R_\mu{}^\nu`, and `F_{\mu\rho}{}^\nu`. Compact Kronecker deltas such as
`\delta^\mu_\nu` remain permitted.

The edition keeps the van der Waerden dot convention for Weyl-spinor indices.
It uses `\mathrm i` for the imaginary unit and `\mathrm e` for an exponential
base. Source symbols with unrelated local meanings remain unchanged.

Systematic convention changes belong to this policy and the convention audit.
The `ERRATA.md` ledger remains reserved for defects in the printed source.
