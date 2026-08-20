# Notation ledger review

Scan date: 2026-08-20. The current native tree contains 50 TeX files: 49
transcription packets and `latex/master.tex`. The notation ledger contains 55
JSONL records. Twenty-two records carry exact `audit_candidate` keys for the
current review emissions. Every record has source notation, native notation,
rule, scope, semantic-invariance rationale, and verification metadata. The
manuscript TeX files were left unchanged by this audit.

The final frozen refresh follows restoration of the PDF 021 paragraph in
`chapter01/sec1_3.tex`. The candidate set remains 22 entries; the Chapter 1
locators below were checked against the post-restoration line numbers.

## Evidence set

The review read `NOTATION.md`, the Weinberg QFT notation file at
`../weinberg_vol1/latex/frontmatter/notation.tex`, the Weinberg exercise
notation contract, the Weinberg master files, all current native TeX packets,
and the page images under `work/source-pages/`. The inspected source-image
set covers the opening state pages, Chapter 1 spinor pages, Chapter 2 Fourier
and cone pages, Chapter 3 Fourier and spectral pages, the Chapter 4 PCT
packets, and the Appendix pages. Formula checks use
`work/source-pages/pdf-116.jpg`, `pdf-120.jpg`, `pdf-123.jpg`,
`pdf-125.jpg`, `pdf-126.jpg`, `pdf-128.jpg`, `pdf-138.jpg`, `pdf-175.jpg`,
`pdf-182.jpg`, `pdf-183.jpg`, `pdf-192.jpg`, `pdf-200.jpg`, `pdf-203.jpg`,
`pdf-204.jpg`, and `pdf-212.jpg`, together with the Chapter 1 and Chapter 2
star pages `pdf-027.jpg` through `pdf-035.jpg`, `pdf-078.jpg`, and
`pdf-079.jpg`.

The adopted rules are the Weinberg mostly-plus metric, explicit Dirac state
delimiters, source-order discrete-symmetry names, beta Dirac adjoints,
daggers for Hilbert-space operator adjoints, contextual stars, and explicit
source-page exceptions. The Fourier conversion tracks

\[
  p_{\mathrm{src}}\mathbin{\cdot}x=-p\mathbin{\cdot}x.
\]

## Current formula checks

| Subject | Current locator | Evidence and status |
| --- | --- | --- |
| PCT/CPT order | `chapter01/sec1_2.tex:32`; `chapter01/sec1_3.tex:552-555,611-618,1045-1064,1158-1164`; `chapter04/sec4_6.tex:145-165,187-188` | PDF 019 and PDF 025, 029, 033, 182, 183 retain CPT where the source says CPT and PCT where the source says PCT. The map carries order-preservation records. |
| Mostly-plus contraction | `chapter01/sec1_3.tex:eq:1-4` | PDF 021 shows the source mostly-minus contraction. The native display uses `eta` with `-x^0 y^0+\\mathbf{x}\\cdot\\mathbf{y}`. |
| Mass shells and cones | `chapter01/sec1_4.tex:37,94`; `chapter02/sec2_3.tex:957-962`; `chapter03/sec3_3.tex:541,671,919,937`; `chapter03/sec3_4.tex:839`; `chapter04/sec4_5.tex:232-253` | PDF 034, 071, 123, 125, 128, 138, and 175 support `p^2=-m^2`, `p^2<0`, `p^0>0`, `P^2\\leq-M^2`, and `\\delta(p^2+m^2)`. Chapter 1 retains the source spacelike sector `p^2>0` for the separate representation class. |
| Fourier and translation phases | `chapter03/sec3_2.tex:102-122`; `chapter03/sec3_3.tex:248-262,773-783` | PDF 116, 120, and 126 show the source phases. Native equations 3-15, 3-16, 3-29, 3-30, and the Laplace transform use the converted signs under the house contraction. |
| Dirac states | `chapter01/opening.tex:23-47`; `chapter01/sec1_1.tex:58-62`; `chapter01/sec1_4.tex:41-50`; `figures/figA2.tex:27` | Scalar products use `\\braket`, operator products use bra-kets or `\\matrixel`, and asymptotic labels use the project helpers. The raw Hilbert-product scan emits zero tuple candidates. |
| Beta and daggers | `chapter01/sec1_4.tex:151-154`; `chapter03/sec3_1.tex:86-106`; `appendix/constructive.tex:68-82` | PDF 035, 109, and 192 support `A^\\dagger`, field operator daggers, and `\\bar\\psi=\\psi^\\dagger\\beta`. The Appendix beta record is current at line 82. |
| Contextual stars | all 22 candidate rows below | Matrix, spinor-component, test-function, bibliography, and C*-algebra stars retain their source meanings. Each emitted candidate has one reviewed classification. |
| Tuple exceptions | `chapter04/sec4_3.tex:12-20`; `chapter04/sec4_4.tex:783-818` | The tuples name operator sets or membership cases. They do not denote Hilbert-space scalar products, so they remain tuples under the explicit exception record. |
| Undefined controls | full active-code scan | Active `\\Chi`, `\\mathscr`, vector-arrow commands, raw inner-product bars, legacy metric signatures, and source `g_{\\mu\\nu}` candidates count zero. The lower-case `\\chi` state in `chapter03/sec3_4.tex:553-563` uses a defined control sequence. |

## Chapter 3 refresh

The previous Chapter 3 `needs-correction` rows were refreshed after formula
inspection. The current rows carry `reviewed-current-corpus` status.

| Source image | Current TeX | Verified conversion |
| --- | --- | --- |
| PDF 116, printed 104 | `chapter03/sec3_2.tex:105` and `:116` | Source `e^{-i p_{src}\\cdot x}` becomes native `e^{+i p\\cdot x}`. The source positive translation character becomes the native negative `\\exp[-i(\\sum p_j)\\cdot a]`. |
| PDF 120, printed 108 | `chapter03/sec3_3.tex:251,259` | Source Wightman Fourier phases are positive in the source convention. Native phases are negative with the house contraction. |
| PDF 123, printed 111 | `chapter03/sec3_3.tex:541` | Source `P_{src}^2\\geq M^2` becomes native `P^2\\leq-M^2`. |
| PDF 125, printed 113 | `chapter03/sec3_3.tex:671` | The cutoff uses native `P^2\\leq-M^2` and `P^0>0`. |
| PDF 126, printed 114 | `chapter03/sec3_3.tex:779-780` | Source Laplace phase is negative. Native phase is positive after the same contraction conversion. |
| PDF 128, printed 116 | `chapter03/sec3_3.tex:919,937` | Source `\\delta(p_{src}^2-m^2)` becomes native `\\delta(p^2+m^2)`. |
| PDF 138, printed 126 | `chapter03/sec3_4.tex:839` | Source isolated representation `p_{src}^2=m^2` becomes native `p^2=-m^2`. |

The Chapter 4 mass-shell row was also refreshed at
`chapter04/sec4_5.tex:232-253`, where the native field equation and frequency
cutoff use the house sign. The Appendix beta row now points to
`appendix/constructive.tex:82`. The Figure A.2 matrix-element row remains at
`figures/figA2.tex:27`.

## Current `audit_notation` candidates

The strict audit emits the following 22 keys. The right column is the exact
classification read from `notation-map.jsonl`.

| File and line | Rule | Classification |
| --- | --- | --- |
| `latex/appendix/bibliography.tex:113` | `raw-source-star` | `algebraic-involution.cstar-bibliography` |
| `latex/appendix/bibliography.tex:114` | `raw-source-star` | `algebraic-involution.cstar-bibliography` |
| `latex/appendix/local-algebras.tex:49` | `raw-source-star` | `algebraic-involution.cstar-local-algebra` |
| `latex/appendix/local-algebras.tex:116` | `raw-source-star` | `algebraic-involution.state-positivity` |
| `latex/appendix/local-algebras.tex:126` | `raw-source-star` | `algebraic-involution.cstar-local-algebra` |
| `latex/appendix/local-algebras.tex:141` | `raw-source-star` | `algebraic-involution.cstar-local-algebra` |
| `latex/chapters/chapter01/sec1_3.tex:472` | `raw-source-star` | `conjugate.matrix-dotted-spinor` |
| `latex/chapters/chapter01/sec1_3.tex:473` | `raw-source-star` | `conjugate.matrix-dotted-spinor` |
| `latex/chapters/chapter01/sec1_3.tex:480` | `raw-source-star` | `conjugate.matrix-dotted-spinor` |
| `latex/chapters/chapter01/sec1_3.tex:522` | `raw-source-star` | `conjugate.matrix-analytic-continuation` |
| `latex/chapters/chapter01/sec1_3.tex:641` | `raw-source-star` | `conjugate.matrix-dotted-spinor` |
| `latex/chapters/chapter01/sec1_3.tex:890` | `raw-source-star` | `conjugate.matrix-spinor-representation` |
| `latex/chapters/chapter01/sec1_3.tex:1018` | `raw-source-star` | `conjugate.componentwise-charge` |
| `latex/chapters/chapter01/sec1_3.tex:1019` | `raw-source-star` | `conjugate.componentwise-charge` |
| `latex/chapters/chapter01/sec1_3.tex:1106` | `raw-source-star` | `conjugate.componentwise-charge` |
| `latex/chapters/chapter01/sec1_3.tex:1107` | `raw-source-star` | `conjugate.componentwise-charge` |
| `latex/chapters/chapter01/sec1_3.tex:1150` | `raw-source-star` | `conjugate.componentwise-pct` |
| `latex/chapters/chapter01/sec1_3.tex:1151` | `raw-source-star` | `conjugate.componentwise-pct` |
| `latex/chapters/chapter02/sec2_4.tex:248` | `raw-source-star` | `conjugate.matrix-lorentz-factorization` |
| `latex/chapters/chapter02/sec2_4.tex:249` | `raw-source-star` | `conjugate.matrix-lorentz-factorization` |
| `latex/chapters/chapter02/sec2_4.tex:254` | `raw-source-star` | `conjugate.matrix-jordan-argument` |
| `latex/chapters/chapter04/sec4_6.tex:156` | `raw-source-star` | `conjugate.test-function` |

The Chapter 1 lines 1106, 1107, 1150, and 1151 are the newly added component
star records. Source PDF 033, printed page 21, was checked for each pair. The
matrix and dotted-spinor rows use source PDFs 027 through 031. The Chapter 2
rows use PDFs 078 and 079. The Appendix rows use PDFs 203, 204, and 212. The
test-function row uses PDF 182.

## Strict coverage enforcement

`scripts/audit_notation.py` now loads `notation-map.jsonl` as a candidate
index. Strict mode validates JSON records, accepts only reviewed statuses,
requires a nonempty classification, matches the exact `(file, line, rule)`
triple for every emitted candidate, detects duplicate classifications, and
reports stale ledger candidates. Draft mode prints the same coverage issues
as review items.

The command

```text
python3 scripts/audit_notation.py --strict
```

Fresh frozen-corpus output reports:

```text
Notation policy: present
Transcription files scanned: 49
No definite notation regressions found.
```

The command emits 22 reviewed candidates, prints 22 exact map
classifications, and exits with code 0. The active-code control scan also
reports zero definite notation regressions. The source audit passes with the
recorded PDF hash and 36/36 native chunks. `audit_project.py --strict`
continues to report separate review-file disposition failures elsewhere in
the project; those records sit outside this notation audit.

The source corpus is present at the current scan. No transcription-arrival
file remains unresolved.

Unresolved blockers: none
