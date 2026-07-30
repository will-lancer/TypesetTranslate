# Modernization handoff

The target is not a facsimile transcription. It is Weinberg's text and argument
with modern, internally consistent notation.

## High-priority conversions

1. Convert the entire book from \((+,+,+,-)\) with time listed last to
   \((-+++)\) with \(x^0=t\) listed first.
2. Use \(G_{\mu\nu}+\Lambda g_{\mu\nu}=8\pi G T_{\mu\nu}\) with the curvature
   convention fixed in `NOTATION.md`. At fixed slot order, Weinberg's source
   \(R^\rho{}_{\sigma\mu\nu}\), \(R_{\mu\nu}\), \(R\), and \(G_{\mu\nu}\)
   are each the negative of the target object; the time-first conversion
   reorders metric components rather than multiplying the metric by \(-1\).
3. Use `\partial_\mu` and `\nabla_\mu` in long derivations instead of repeated
   full partial-derivative fractions.
4. Replace comma and semicolon derivative notation with explicit operators.
5. Use one Greek spacetime-index family; reserve Latin \(a,b,\ldots\) for
   orthonormal-frame indices.
6. Rename the cosmological scale factor \(R(t)\) to \(a(t)\), avoiding collision
   with the Ricci scalar.
7. Keep Weinberg's cheeky \(I\)-notation for actions: \(I\), \(I_M\), and
   \(I_G\). Convert the sign and invariant measure of \(I_G\) consistently with
   the target metric and curvature conventions.
8. Keep Weinberg's \(D/D\tau\)-notation for covariant differentiation along a
   worldline, defining \(DV^\mu/D\tau=u^\nu\nabla_\nu V^\mu\) when introduced.
9. Use \(\mathcal L_\xi\) for Lie derivatives and \(e^a{}_\mu\) for tetrads.
10. Distinguish the permutation symbol/density
    \(\tilde\epsilon^{0123}=+1\) from the Levi--Civita tensor
    \(\varepsilon^{0123}=+1/\sqrt{-g}\), so lowering all four indices gives
    \(\varepsilon_{0123}=-\sqrt{-g}\).
11. Use the correctly attributed modern name “Lorenz gauge/condition” for
    electromagnetism; reserve “Lorentz” for transformations and the spacetime
    group.

## Signature conversion examples

Source-style flat interval:

\[
  d\tau^2=dt^2-d\mathbf{x}^2.
\]

Modern spacetime interval:

\[
  ds^2=-dt^2+d\mathbf{x}^2,
  \qquad d\tau^2=-ds^2
\]

for a timelike worldline.

Source-style static spherical line element:

\[
  d\tau^2=B(r)\,dt^2-A(r)\,dr^2-r^2d\Omega^2.
\]

Modern form:

\[
  ds^2=-B(r)\,dt^2+A(r)\,dr^2+r^2d\Omega^2.
\]

The perfect-fluid tensor remains

\[
  T^{\mu\nu}=(\rho+p)u^\mu u^\nu+p\,g^{\mu\nu}
\]

with \(u^\mu u_\mu=-1\). This illustrates why conversions must be derived
equation by equation rather than implemented as a global minus sign.

## Editorial boundary

Modernize notation aggressively when it shortens or clarifies the calculation.
Do not modernize the physics historically: do not insert later discoveries,
replace Weinberg's arguments with textbook-standard proofs, or silently update
1971 observational values. Such additions belong in clearly labeled editor's
notes, if separately authorized.
