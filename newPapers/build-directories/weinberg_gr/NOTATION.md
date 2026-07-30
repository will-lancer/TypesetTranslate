# Weinberg GR modernization policy

This transcription preserves Weinberg's content while deliberately modernizing
notation. This file is binding. Do not copy the source notation mechanically,
and do not import conventions from the Weinberg QFT projects without checking
them here.

## Core spacetime convention

- Coordinates are ordered
  \[
    x^\mu=(x^0,x^1,x^2,x^3)=(t,\mathbf{x}).
  \]
- Greek indices \(\mu,\nu,\rho,\sigma,\ldots\) are spacetime indices.
- Latin indices \(i,j,k,\ldots\) are spatial indices.
- Latin indices \(a,b,c,\ldots\) from the beginning of the alphabet are local
  Lorentz/tetrad indices when needed.
- The metric signature is
  \[
    \eta_{\mu\nu}=\operatorname{diag}(-1,+1,+1,+1).
  \]
- Timelike four-velocities obey \(u^\mu u_\mu=-1\).
- Proper time is defined by
  \[
    d\tau^2=-g_{\mu\nu}\,dx^\mu dx^\nu.
  \]
- The speed of light is set to one. Keep \(\hbar\) explicit in the quantum
  sections unless a chapter-level note explicitly changes that choice.

The source uses the ordering \((1,2,3,0)\) and signature \((+,+,+,-)\).
Every converted equation must be checked for induced signs; changing only the
displayed metric convention is not sufficient.

## Curvature convention

Use

\[
  [\nabla_\mu,\nabla_\nu]V^\rho
  =R^\rho{}_{\sigma\mu\nu}V^\sigma,
\]

\[
  R^\rho{}_{\sigma\mu\nu}
  =
  \partial_\mu\Gamma^\rho{}_{\nu\sigma}
  -\partial_\nu\Gamma^\rho{}_{\mu\sigma}
  +\Gamma^\rho{}_{\mu\lambda}\Gamma^\lambda{}_{\nu\sigma}
  -\Gamma^\rho{}_{\nu\lambda}\Gamma^\lambda{}_{\mu\sigma},
\]

\[
  R_{\mu\nu}=R^\rho{}_{\mu\rho\nu},
  \qquad
  G_{\mu\nu}=R_{\mu\nu}-\frac12 g_{\mu\nu}R.
\]

With these conventions, write Einstein's equation as

\[
  G_{\mu\nu}+\Lambda g_{\mu\nu}=8\pi G\,T_{\mu\nu}.
\]

At the same index-slot order, the target curvature objects are the negatives
of Weinberg's source objects:

\[
  R^\rho{}_{\sigma\mu\nu}\big|_{\mathrm{target}}
  =-R^\rho{}_{\sigma\mu\nu}\big|_{\mathrm{source}},
  \qquad
  R_{\mu\nu}\big|_{\mathrm{target}}
  =-R_{\mu\nu}\big|_{\mathrm{source}},
\]
\[
  R\big|_{\mathrm{target}}=-R\big|_{\mathrm{source}},
  \qquad
  G_{\mu\nu}\big|_{\mathrm{target}}
  =-G_{\mu\nu}\big|_{\mathrm{source}}.
\]

The passage from Weinberg's displayed \((1,2,3,0)\) order to
\((0,1,2,3)\) merely reorders the metric components; it does not multiply
the metric by \(-1\). Apply the curvature sign map before rearranging index
slots, and check the Newtonian limit after any chapter-wide conversion.

Keep Weinberg's \(I\)-notation for the action, but convert its sign and measure
consistently:

\[
  I=I_M+I_G,
  \qquad
  I_G=\frac{1}{16\pi G}\int d^4x\,\sqrt{-g}\,(R-2\Lambda).
\]

Here \(g=\det(g_{\mu\nu})<0\). Define

\[
  T_{\mu\nu}
  =-\frac{2}{\sqrt{-g}}\frac{\delta I_M}{\delta g^{\mu\nu}}.
\]

## Derivatives

Prefer compact indexed notation:

\[
  \partial_\mu\phi,\qquad
  \nabla_\mu V^\nu,\qquad
  \Box\phi\equiv\nabla_\mu\nabla^\mu\phi.
\]

Do not repeatedly write
`\frac{\partial}{\partial x^\mu}` in long calculations when `\partial_\mu`
is unambiguous. Retain a full derivative fraction when:

- defining a Jacobian,
- differentiating with respect to a non-coordinate parameter,
- the differentiated variable would otherwise be ambiguous, or
- the expanded form is pedagogically important at that step.

Replace source comma/semicolon notation by explicit operators:

\[
  T^{\mu\nu}{}_{,\rho}\longrightarrow\partial_\rho T^{\mu\nu},
  \qquad
  T^{\mu\nu}{}_{;\rho}\longrightarrow\nabla_\rho T^{\mu\nu}.
\]

Keep Weinberg's covariant worldline derivative:

\[
  \frac{D V^\mu}{D\tau}
  \equiv
  u^\nu\nabla_\nu V^\mu.
\]

Define this equivalence when the operator is introduced, then prefer
\(D/D\tau\) in worldline equations. The expanded form
\(u^\nu\nabla_\nu\) may still be used when deriving the operator or when the
directional-derivative structure is itself important.

Use \(\mathcal L_\xi\) for a Lie derivative. Use parentheses and brackets for
normalized symmetrization and antisymmetrization:

\[
  A_{(\mu\nu)}=\frac12(A_{\mu\nu}+A_{\nu\mu}),\qquad
  A_{[\mu\nu]}=\frac12(A_{\mu\nu}-A_{\nu\mu}).
\]

Distinguish the numerical permutation symbol from the Levi--Civita tensor.
Use \(\tilde\epsilon\) for the symbol/tensor density and \(\varepsilon\) for
the tensor:

\[
  \tilde\epsilon^{0123}=+1,
  \qquad
  \varepsilon^{\mu\nu\rho\sigma}
  =\frac{1}{\sqrt{-g}}\tilde\epsilon^{\mu\nu\rho\sigma},
  \qquad
  \varepsilon_{\mu\nu\rho\sigma}
  =-\sqrt{-g}\,\tilde\epsilon_{\mu\nu\rho\sigma}.
\]

Here the upper- and lower-index permutation symbols are separately normalized
to \(+1\) on \(0123\). Thus
\(\varepsilon^{0123}=+1/\sqrt{-g}\) and
\(\varepsilon_{0123}=-\sqrt{-g}\) for the mostly-plus metric. Formulas written
with a fixed orientation assume orientation-preserving coordinate changes;
under an orientation reversal the Levi--Civita object has the usual
pseudotensor behavior. Use \(\varepsilon^{ijk}\), with
\(\varepsilon^{123}=+1\), for the Euclidean spatial Levi--Civita tensor.

## Standard replacements

| Source habit | Modern form |
|---|---|
| inertial indices \(\alpha,\beta,\ldots\), general indices \(\mu,\nu,\ldots\) | one spacetime family \(\mu,\nu,\rho,\sigma,\ldots\) |
| coordinate list \(1,2,3,0\) | \(0,1,2,3\) |
| signature \(+,+,+,-\) | signature \(-,+,+,+\) |
| \(I\), \(I_M\), \(I_G\) for actions | keep Weinberg's \(I\)-notation |
| \(R(t)\) for the cosmic scale factor | \(a(t)\) |
| \(\lambda\) for the cosmological constant | \(\Lambda\) |
| radiation constant \(a\), where the scale factor is also \(a(t)\) | \(a_{\mathrm{rad}}\) |
| long repeated \(\partial/\partial x^\mu\) | \(\partial_\mu\) |
| comma and semicolon derivatives | \(\partial_\mu\) and \(\nabla_\mu\) |
| “Lorentz gauge/condition” | Lorenz gauge/condition |
| \(D/D\tau\) along a worldline | keep Weinberg's \(D/D\tau\)-notation |
| infinitesimal coordinate/gauge displacement \(\epsilon^\mu\) | \(\xi^\mu\) |
| Brans--Dicke scalar \(\phi\), where it could be confused with the Newtonian potential | \(\Phi_{\mathrm{BD}}\) |
| an ad hoc symbol for infinitesimal tensor change | \(\mathcal L_\xi\) |
| expanded symmetric/antisymmetric sums | \(A_{(\mu\nu)}\), \(A_{[\mu\nu]}\) |
| \(\sqrt{-\det g}\) written inconsistently | \(\sqrt{-g}\), with \(g=\det g_{\mu\nu}\) |
| one \(\epsilon\) for both symbol/density and tensor | \(\tilde\epsilon\) for the symbol/density; \(\varepsilon\) for the tensor |

Use

\[
  H=\frac{\dot a}{a},
  \qquad
  q=-\frac{a\ddot a}{\dot a^2}
\]

in cosmology once defined. Use \(k\in\{-1,0,+1\}\) for normalized spatial
curvature, reserving \(R\) for curvature tensors and scalars. Write the
black-body radiation constant as \(a_{\mathrm{rad}}\), so products such as
\(\rho_\gamma=a_{\mathrm{rad}}T_\gamma^4\) cannot be mistaken for powers of
the scale factor.

For weak-field gravity, use

\[
  g_{\mu\nu}=\eta_{\mu\nu}+h_{\mu\nu},
  \qquad
  \bar h_{\mu\nu}=h_{\mu\nu}-\frac12\eta_{\mu\nu}h,
\]

and state the gauge condition as \(\partial^\mu\bar h_{\mu\nu}=0\).

For tetrads, use \(e^a{}_\mu\) and its inverse \(e_a{}^\mu\). Do not reuse the
metric perturbation \(h_{\mu\nu}\) as a tetrad symbol.

## What is not automatically changed

- Equation, section, figure, table, bibliography, and reference numbering.
- Physical units appearing in data or observational formulas.
- Definitions whose alteration would change the substance rather than the
  notation.
- Historical terminology inside quotations.

Do not silently repair a suspected mathematical error. Preserve the source
content, add `% VERIFY SOURCE:` and `% MODERNIZATION CHECK:` comments, and
separate source errata from notation conversion.

## Required conversion check

For every completed section:

1. compare the modernized equation with the source equation;
2. check all raised/lowered time indices for sign changes;
3. check contractions, traces, and determinants;
4. check the flat-space and Newtonian limits where applicable;
5. compile and visually inspect the rendered mathematics;
6. leave no mixed \(+,+,+,-\) and \(-,+,+,+\) conventions.
