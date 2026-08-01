# Weinberg QFT Volume III - Two-Component Spinor Edition

This directory is a parallel edition of Steven Weinberg's *The Quantum
Theory of Fields, Volume III: Supersymmetry*.  It is derived from the
completed source in `../weinberg_vol3` and rewrites the four-dimensional
spinor formalism in standard dotted/undotted two-component notation.

The editorial invariants are:

- preserve Weinberg's prose except where it explicitly describes
  four-component packaging or notation;
- preserve physical content, signs, normalizations, factor ordering,
  equation tags, labels, cross-references, section structure, problems,
  references, figures, and indexes, except for independently verified source
  errors recorded in `ERRATA.md`;
- retain the mostly-plus metric
  `eta = diag(-1,+1,+1,+1)`;
- use two-component notation throughout the four-dimensional material in
  Chapters 24–31;
- retain dimension-dependent Clifford-spinor notation in Chapter 32, where
  a four-dimensional Weyl decomposition is not generally available, while
  writing its four-dimensional specializations in the edition's
  two-component notation.

The binding convention and QA policy are in
`TWO_COMPONENT_CONVENTIONS.md`.

Build and run the algebraic convention checks, source-parity audit,
semantic-hotspot audit, reference checks, layout comparison, PDF metadata
checks, text extraction, and stable export:

```sh
./build_and_verify.sh
```

The stable exported PDF is
`../../weinberg-qft-two-component/weinberg-vol3-two-component.pdf`.

The convention checks are split between
`verify_spinor_conventions.py`, which verifies the sigma/gamma dictionary,
and `verify_superspace_conventions.py`, which verifies the Grassmann
operator signs independently with an exterior algebra.  The final release
record is `RELEASE_VERIFICATION.md`; corrected errors are listed in
`ERRATA.md`.
