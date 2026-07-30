# Modernization policy for exercise material

The canonical transcription has already modernized notation while preserving
Weinberg's content. This exercise edition follows that work; it does not
perform a second modernization pass on the book.

- Preserve Weinberg's extracted exercise wording and mathematical content.
- Write all new editorial solutions and supplementary material in the
  conventions of `NOTATION.md` and the chapter being extended.
- Replace cumbersome presentation only in editorial material: use Dirac
  states, compact derivatives, `\mathcal` rather than decorative `\mathscr`
  where the canonical edition does so, and `H_I` for the interaction
  Hamiltonian.
- Keep original equation, section, figure, bibliography, and reference
  numbering. Editorial displays should normally be unnumbered.
- Do not change physical assumptions to make a sourced problem fit. Adapt its
  presentation, or omit it.
- Mark third-party provenance exactly and write solutions independently.

Any mathematical correction to an original Weinberg problem must be handled
as an explicit editorial note, never as a silent rewrite of the prompt.

## Recorded transcription correction

The independent exercise edition corrects one internally demonstrable sign
error in the surrounding transcribed text; the canonical edition remains
unchanged.

- In Eqs. (24.2.9) and (26.1.22), the auxiliary-field interaction is
  \(gF(A^2-B^2)\), not \(gF(A^2+B^2)\).
- Consequently Eq. (24.2.10) reads
  \(F=-mA-g(A^2-B^2)\).
- In Eq. (24.2.8), the derivative term in \(\delta\psi\) is
  \(\partial_\mu(A+i\gamma_5B)\gamma^\mu\alpha\), as in the equivalent
  four-component derivation in Eq. (26.1.21), not the transcribed minus-sign
  version.

With these signs, eliminating \(F\) and \(G\) gives Eq. (24.2.11), including
the terms \(-gmA(A^2+B^2)\) and
\(-\tfrac12g^2(A^2+B^2)^2\). The plus-sign transcription cannot yield either
term. This correction is also the conventional Wess--Zumino auxiliary-field
coupling and is needed for the supersymmetry check in Exercise W.24.3.
