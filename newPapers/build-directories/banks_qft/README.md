# Banks QFT convention-adapted JHEP editions

This package builds two native A4 editions of Tom Banks's *Modern Quantum
Field Theory: A Concise Introduction* from the frozen 281-page source PDF. The
mathematics uses the mostly-plus metric, `D` spacetime dimensions where valid,
bold spatial vectors, and spaced adjacent mixed tensor indices. `NOTATION.md`
defines the dependent Fourier, propagator, spinor, epsilon, and Wick-rotation
conventions.

`latex/master.tex` builds the source transcription followed by solutions to
the 80 numbered problems. `latex/master-implicit.tex` enables 110 editorial
exercises at their source cues and collects their solutions at the end of each
chapter or appendix.

Run `./build_and_verify.sh --draft --edition base` while transcription is open.
Strict releases use `./build_and_verify.sh --strict --edition base` and
`./build_and_verify.sh --strict --edition implicit` after their ledgers and
checksum-bound review records close.

The source PDF remains the authority for content, numbering, captions,
footnotes, references, and index entries. The declared convention map governs
adapted formulas and their required wording. See `TRANSCRIPTION_CONTRACT.md`.
