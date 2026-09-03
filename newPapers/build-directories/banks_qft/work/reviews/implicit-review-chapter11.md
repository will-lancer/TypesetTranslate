# Independent implicit-exercise review: Chapter 11

Date: 2026-09-02

Result: **PASS**

## Scope and source basis

Reviewed I-CH11-001 in `implicit-exercises.json`, its exercise unit,
`latex/solutions/chapter11-implicit.tex`, the native hook context, and printed
page 243 / PDF page 253.  The hook follows the paragraph continuing onto
printed page 244 / PDF page 254.  Banks's Euclidean conventions on printed
pages 23–24 / PDF pages 33–34 supplied the continuation and source signs.

## Coverage

| Requested part | Reviewed content | Status |
|---|---|---|
| (a) | Common complexification, Lorentzian and Euclidean slices, definite metric, full action continuation | PASS |
| (b) | Regulated normalized functional integral, Schwinger derivatives, vacuum and thermal boundary data | PASS |
| (c) | Spectral representation, ordered holomorphy domain, arbitrary time ordering, explicit regulator | PASS |
| (d) | Geometric regularity, global hyperbolicity, ellipticity, state selection, reflection positivity | PASS |
| (e) | Flat free-field position-space and momentum-space Feynman propagators | PASS |

## Findings and dispositions

### F11-01: P1, fixed

The exercise and solution used signature `(-,+,...)`, conflicting with Banks's
frozen mostly-minus convention.  The final momentum-space propagator already
used the mostly-minus denominator, creating an internal convention mismatch.

Repair: `latex/implicit/I-CH11-001.tex` and
`latex/solutions/chapter11-implicit.tex` now use `(+,-,...)`.  The complex
static metric is `N^2 dz^2-h_ij dx^i dx^j`; its Euclidean restriction is real
negative definite, with the positive metric defined by `g_E=-g_C|_{M_E}`.
The minimally coupled scalar action was retained, removing an unnecessary
curvature-sign branch from this source obligation.

Disposition: resolved.  Direct substitution gives `S_L|=i S_E`, hence
`exp(i S_L)` continues to `exp(-S_E)`.

### F11-02: P1, fixed

The Euclidean source term used `+ integral J phi`, while Banks's equation 3.24
uses the analytically continued source `+ i integral J phi`.  The derivative
formula consequently lacked the compensating powers of `i`.

Repair: `latex/implicit/I-CH11-001.tex` now requests Banks's source convention.
`latex/solutions/chapter11-implicit.tex` uses
`+i integral sqrt(g_E) J phi` and defines the normalized n-point function with
the factor `1/i^n`.

Disposition: resolved.  The functional derivatives reproduce the Schwinger
functions with the source convention stated in the book.

### F11-03: P2, fixed

The ordered complex Euclidean times supplied damping, while their equivalent
Lorentzian `i epsilon` displacement remained unstated.  The vacuum boundary
condition was also described as decay of fields at both Euclidean ends.

Repair: `latex/solutions/chapter11-implicit.tex` now gives
`t_{pi(a)} -> t_{pi(a)}-i(n-a) epsilon` and identifies it as the ordered
prescription.  Semi-infinite Euclidean evolution with regular finite-action
boundary data now states the vacuum projection accurately.

Disposition: resolved.  The spectral factors have positive real gaps and the
flat-space limit yields `i/(p^2-m^2+i0)`.

### F11-04: P3, fixed

Static lint found one space before punctuation inside the boxed continuation
formula.

Repair: removed the space from
`latex/solutions/chapter11-implicit.tex`.

Disposition: resolved.

## Static checks

- Inventory coverage returned exactly I-CH11-001 at printed page 243 / PDF
  page 253.
- The exercise ID and solution ID each occur once.
- A convention scan found no residual `(-,+,...)` signature, curvature term,
  or source functional lacking the continued-source factor.
- `lacheck` returned exit 0 for the exercise and solution files.
- The assigned TeX files contain no trailing whitespace.
- Compilation was omitted as instructed.

Final status: **PASS. No unresolved finding remains.**
