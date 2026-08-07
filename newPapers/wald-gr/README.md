# Wald GR — notation-modernized edition

The verified delivery PDF for Robert M. Wald's *General Relativity* is
`wald-gr-modernized.pdf`.

- Extent: 483 A4 pages
- SHA-256: `6c79b1dbdff2d60120ed6e518ddb78fb3908f30e8e481a0439d3a1869495b978`
- Contents: all 14 chapters, Appendices A--F, 336 references, and 434 source
  index entries
- Notation: algebraic duals use `\vee`; tangent/cotangent bases use `e_\mu`
  and `f^\mu`; spatial vectors use `\mathbf` or `\boldsymbol`, never `\vec`
- Corrections: 36 reviewed changes in 19 classes, recorded in
  `../build-directories/wald_gr/CORRECTIONS.md`
- Figures: all 72 figures were compared with the authoritative source; 48
  figure source files were repaired and every figure-bearing book page was
  checked in final placement

The reproducible LaTeX source, source map, binding notation policy, and QA
tools live in `../build-directories/wald_gr`. The authoritative 505-page
source PDF is kept separately at `../../origPapers/wald_gr.pdf`.

The edition was exported by the strict verification command:

```sh
../build-directories/wald_gr/build_and_verify.sh
```

See `../build-directories/wald_gr/RELEASE_VERIFICATION.md` for the complete
release record.
