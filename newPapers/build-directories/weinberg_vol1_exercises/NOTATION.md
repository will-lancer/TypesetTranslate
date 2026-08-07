# QFT notation policy

This file is binding for editorial exercises and solutions. It summarizes the
modernized conventions printed in `latex/frontmatter/notation.tex`; that
frontmatter remains the primary mathematical reference.

## Spacetime and units

- Order coordinates as \(x^\mu=(x^0,\mathbf{x})\), with Greek spacetime
  indices \(0,1,2,3\) and Latin spatial indices \(1,2,3\).
- Use the mostly-plus metric
  \(\eta_{\mu\nu}=\operatorname{diag}(-1,+1,+1,+1)\). Thus \(p^2=-m^2\).
- Use \(\Box=\partial_\mu\partial^\mu=\nabla^2-\partial_t^2\).
- Use \(\epsilon^{0123}=+1\).
- Except in historical Chapter 1, set \(\hbar=c=1\). The electron has charge
  \(-e\), and \(\alpha=e^2/(4\pi)\).

## Internal and spacetime indices

- When a quantity carries both a gauge-adjoint index and spacetime indices,
  put the opposing scripts together: write
  `F^a_{\mu\nu}` and `A_a^\mu`, not
  `F^a{}_{\mu\nu}` or `A_a{}^\mu`.

## Product notation

- Use boldface rather than arrow accents for vectors: `\mathbf{x}` for Latin
  symbols and `\boldsymbol{\pi}` for Greek symbols. Do not use arrow accents.
- Use `\cdot` for ordinary or scalar multiplication and for inner products.
- Use `\times` for Cartesian and direct products, vector cross products and
  curls, and dimensions such as \(2\times2\).

## States and asymptotic labels

Use Dirac notation throughout:

```tex
\ket{p,\sigma}
\bra{p,\sigma}
\braket{\phi}{\psi}
```

Asymptotic labels belong outside the ket or bra, never inside its argument and
never as a superscript:

```tex
\InKet{\alpha}     % \ket{\alpha}_{\mathrm{in}}
\OutKet{\beta}    % \ket{\beta}_{\mathrm{out}}
\InBra{\alpha}    % {}_{\mathrm{in}}\!\bra{\alpha}
\OutBra{\beta}    % {}_{\mathrm{out}}\!\bra{\beta}
```

When one displayed identity applies to both choices at once, use the paired
helpers `\InOutKet`, `\OutInKet`, `\InOutBra`, and `\OutInBra`; these preserve
the same outside-label spacing without splitting a compact `in/out` formula.
When an in-state also carries an external-source qualifier, use
`\InKetWith{\alpha}{\epsilon}` so both `in` and `\epsilon` remain outside the
ket delimiter.

For example, write
\({}_{\mathrm{out}}\!\bra{\beta}S\ket{\alpha}_{\mathrm{in}}\), implemented as
`\OutBra{\beta}S\InKet{\alpha}`. Reserve superscripts \(+\) and \(-\) for
positive- and negative-frequency field pieces such as \(\psi^{(+)}\) and
\(\psi^{(-)}\).

## Momentum modes and internal gauge indices

- Write the on-shell energy of a momentum mode as `\omega_{\mathbf k}` (or
  `\omega_k` when the momentum variable is not bold), and likewise use
  `\omega_{\mathbf p}`, `\omega_{\mathbf q}`, and so on when the mode variable
  changes. Do not use `E_{\mathbf k}`, `E_k`, or the corresponding `E` notation
  for other individual momentum modes. This does not rename total energies,
  bound-state levels such as `E_n`, or scattering-state energies such as
  `E_\alpha`.
- Use lowercase Latin letters from the beginning of the alphabet for internal
  adjoint gauge indices: \(a,b,c,\ldots\), not
  \(\alpha,\beta,\gamma,\ldots\).
- Rename collision-safely. If \(a,b,c\) already label other objects in the same
  formula, continue with unused lowercase Latin letters such as \(d,e,f\) or
  \(r,s,t\), state the index range, and do not silently reuse spacetime,
  spatial, spinor, flavor, or particle-state labels.

## Spinors and operators

- Use \(\{\gamma^\mu,\gamma^\nu\}=2\eta^{\mu\nu}\),
  \(\gamma_5=i\gamma^0\gamma^1\gamma^2\gamma^3\),
  \(\beta=i\gamma^0\), and \(\bar u=u^\dagger\beta\).
- Write complex conjugation, transpose, and Hermitian conjugation as
  \(A^*\), \(A^{\mathsf T}\), and \(A^\dagger\).
- Use \(\mathbf{1}\) for the identity and \(+\mathrm{H.c.}\) or
  \(+\mathrm{c.c.}\) for appended conjugate terms.
- Write the interaction Hamiltonian as
  \(H_I(t)=\int d^3x\,\mathcal H_I(x)\), not bare \(V\).
- Operators normally remain unhatted when context is unambiguous.

## Editorial discipline

Do not import the GR project's curvature or action conventions. Do not
silently repair a suspected source error. Record any such issue in a comment
and keep the exercise statement and the editorial convention visibly
separate.
