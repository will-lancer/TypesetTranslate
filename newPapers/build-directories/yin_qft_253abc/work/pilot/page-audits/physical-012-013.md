# Source audit: physical pages 12-13

Source: `/Users/wlancer/Desktop/IAS/phy/qft/qft_253abc_book.pdf`  
Verified SHA-256: `9e5e4d241fffffa56c1c3df6dce4b83178f75787dd5d794a18c5d0c087769f21`  
Scope: physical PDF pages 12-13, corresponding to Physics 253a handwritten note pages 7-8.  
Inspection: both pages were independently rendered from the verified PDF at 600 dpi (5100 by 6672 pixels), then checked as full pages and enlarged overlapping crops. The TeX below assumes `amsmath`, `amssymb`, and `xcolor`.

## Physical page 12 / 253a note page 7

### Exact TeX-ready transcription

```tex
% ===== BEGIN physical PDF page 12 / 253a note page 7 =====

\noindent Micro causality;

\[
\bigl[\hat\phi(x),\hat\phi(y)\bigr]=0
\qquad
\begin{gathered}
\text{whenever }x,y\\
\text{are spacelike}\\
\text{- separated.}
\end{gathered}
\]

\noindent i.e.

\[
\begin{aligned}
(x-y)^2
&\equiv -(x^0-y^0)^2+(\vec x-\vec y)^2\\
&>0.
\end{aligned}
\]

\medskip
\noindent $\bullet$\quad What about our model of\\
\hspace*{5em}free relativistic particles?

\[
H=\int d^{D-1}\vec p\,
\sqrt{\vec p^2+m^2}\,
a_{\vec p}^{+}a_{\vec p},
\]

\[
\vec P=\int d^{D-1}\vec p\,\vec p\,
a_{\vec p}^{+}a_{\vec p}.
\]

\[
\hat P^\mu=(H,\vec P).
\]

\noindent Does $\hat\phi(x)$ exist?\qquad Yes!

\[
\hat\phi(x)
=\int
\frac{d^{D-1}\vec p}
{\sqrt{(2\pi)^{D-1}\,2\omega_{\vec p}}}
\left(
a_{\vec p}e^{ip\cdot x}
+a_{\vec p}^{+}e^{-ip\cdot x}
\right)
\]

% [blue] An arrow begins beneath e^{ip\cdot x}, curves downward,
% and continues to the blue definitions at the top of physical page 13.

% ===== END physical PDF page 12 / 253a note page 7 =====
```

### Layout and annotation inventory

- The source splits “spacelike-separated” across two handwritten lines as “spacelike” and “- separated.”
- The radical in the scalar-field denominator extends over the complete factor `(2\pi)^{D-1}2\omega_{\vec p}`.
- The superscript on each creation operator is drawn as a literal plus sign. The exact layer therefore uses `a_{\vec p}^{+}`.
- The blue arrow under `e^{ip\cdot x}` crosses the page boundary conceptually. Its target is the blue phase and frequency convention at the top of physical page 13.
- Diagram inventory: the blue cross-page arrow only.

## Physical page 13 / 253a note page 8

### Exact TeX-ready transcription

```tex
% ===== BEGIN physical PDF page 13 / 253a note page 8 =====

% [blue] Continuation of the arrow from e^{ip\cdot x} on physical page 12.
% A separate opening curved stroke appears above and to the left.
\[
\textcolor{blue}{
\begin{aligned}
p\cdot x&\equiv \vec p\cdot\vec x-\omega_{\vec p}x^0.\\
\omega_{\vec p}&\equiv\sqrt{\vec p^2+m^2}.
\end{aligned}}
\]

\noindent Check micro causality;

\[
\begin{aligned}
\bigl[\hat\phi(x),\hat\phi(y)\bigr]
&=\int
\frac{d^{D-1}\vec p}{(2\pi)^{D-1}\,2\omega_{\vec p}}
\cdot
\left[
e^{ip\cdot(x-y)}-e^{-ip\cdot(x-y)}
\right]\\
&=\int
\textcolor{blue}{
\underbrace{
\textcolor{black}{
\frac{d^D p^\mu}{(2\pi)^{D-1}}
\theta(p^0)\delta(p^2+m^2)}
}_{\substack{\text{invariant under}\\
p^\mu\to\Lambda^\mu{}_{\nu}p^\nu.}}}
\textcolor{blue}{
\underbrace{
\textcolor{black}{
\left[e^{ip\cdot(x-y)}-e^{-ip\cdot(x-y)}\right]}
}_{\substack{\text{inv't under}\\
x\to\Lambda x,\ y\to\Lambda y.}}}
\end{aligned}
\]

\begin{center}
\textcolor{blue}{result a function of $(x-y)^2$ only.}
\end{center}

\noindent If $(x-y)^2>0$, WLOG can take $x^0-y^0=0$.

\[
\Rightarrow\quad \vec x-\vec y\ne 0.
\]

\noindent integrand odd under $\vec p\to-\vec p$,

\[
\text{thus}\qquad \int\cdots=0,
\]

\noindent i.e.

\[
\bigl[\hat\phi(x),\hat\phi(y)\bigr]=0
\qquad\text{for }(x-y)^2>0.
\]

\begin{flushright}
\textcolor{blue}{$\checkmark$}
\end{flushright}

% ===== END physical PDF page 13 / 253a note page 8 =====
```

### Layout and annotation inventory

- The two blue definitions at the page top complete the arrowed annotation begun beneath the positive-phase exponential on page 12. The isolated blue curve above them may be an opening parenthesis or the continued arrow stroke; no matching closing parenthesis is visible.
- A blue underbrace labels the covariant measure, theta function, and delta function “invariant under” `p^\mu\to\Lambda^\mu{}_{\nu}p^\nu`.
- A second blue underbrace labels the exponential difference “inv't under” `x\to\Lambda x, y\to\Lambda y`.
- The blue sentence “result a function of `(x-y)^2` only.” follows those braces. A blue check mark closes the page.
- Diagram inventory: the cross-page blue curve, two blue underbraces, and the final check mark.

## Critical source-fidelity readings

- The scalar-field normalization is exactly

  $$
  \frac{d^{D-1}\vec p}
  {\sqrt{(2\pi)^{D-1}2\omega_{\vec p}}}.
  $$

  The radical covers both `(2\pi)^{D-1}` and `2\omega_{\vec p}`. No factor lies outside it.
- The Fourier phases are exactly `e^{ip\cdot x}` on the annihilation term and `e^{-ip\cdot x}` on the creation term. The blue convention fixes

  $$
  p\cdot x\equiv\vec p\cdot\vec x-\omega_{\vec p}x^0.
  $$
- The commutator contains the ordered difference

  $$
  e^{ip\cdot(x-y)}-e^{-ip\cdot(x-y)}.
  $$

  There is no overall factor of `i` in the handwritten line.
- The first commutator line contains a visible centered multiplication dot between the on-shell spatial measure and the exponential bracket. It is transcribed literally as `\cdot`.
- The second commutator line literally writes the unusual numerator

  $$
  d^D p^\mu.
  $$

  This leaves a visible superscript `\mu` on `p` in the measure. The conventional Lorentz-invariant on-shell measure would use `d^D p`, but that is not the literal source. Preserve `d^D p^\mu` as `NOTES_EXACT` and record any later replacement as `SOURCE_CONFLICT` or `EQUATION_NORMALIZED` after video evidence or editorial review.
- The denominator of that covariant line is `(2\pi)^{D-1}`, followed by `\theta(p^0)\delta(p^2+m^2)`. The delta-function sign is a plus, consistent with the mostly-plus signature used here.
- The spacelike proof explicitly chooses `x^0-y^0=0`, then writes a leading implication arrow `\Rightarrow` before `\vec x-\vec y\ne0`. It invokes oddness under `\vec p\to-\vec p` and concludes that the integral vanishes.

## Uncertainties and competing readings

| Location | Adopted reading | Competing reading | Confidence | Disposition |
|---|---|---|---:|---|
| p. 12, creation-operator superscript | Literal `a_{\vec p}^{+}` | Semantic normalization to `a_{\vec p}^{\dagger}` | 0.995 for the ink; 0.99 for adjoint meaning | Keep `+` in the exact layer. A chapter-wide dagger conversion requires an explicit normalization record. |
| p. 12, scalar denominator | `\sqrt{(2\pi)^{D-1}2\omega_{\vec p}}` | Radical ending before `2\omega_{\vec p}` | 0.995 | The 600 dpi crop shows the radical bar extending over the complete product. |
| p. 13, covariant numerator | Literal `d^D p^\mu` | Conventional `d^D p` | 0.995 for the visible `\mu` | Preserve the literal measure and flag it. Seek a video frame or oral correction before normalization. |
| p. 13, top blue curve | Continuation/parenthetical curve attached to the page-12 phase annotation | A standalone opening parenthesis | 0.78 | Preserve it graphically as a curved annotation; do not insert an unmatched parenthesis into the mathematical line. |
| pp. 12-13, headings | “Micro causality;” and “Check micro causality;” | Colons | 0.98 | Enlarged crops show a dot with a descending comma stroke, so retain semicolons. |

No character-level ambiguity remains in the Fourier phases, radical coverage, theta function, mass-shell delta function, or the odd-integrand argument. The covariant measure remains a mathematical source issue rather than a handwriting uncertainty.

## Likely textbook and provenance units

All proposed records begin as `NOTES_EXACT`. The cross-page phase annotation belongs to the scalar-field formula and should not receive an independent prose disposition.

| Proposed ID | Source span | Unit for chapter assembly | Atomic source content |
|---|---|---|---|
| `yin-253a-n07-u01` | note 7 / PDF 12, upper third | Microcausality definition | Vanishing spacelike commutator and the mostly-plus expression for `(x-y)^2>0`. |
| `yin-253a-n07-u02` | note 7 / PDF 12, middle | Free relativistic Fock Hamiltonian and momentum | `H`, `\vec P`, and `\hat P^\mu=(H,\vec P)` with the literal `a^+a` notation. |
| `yin-253a-n07-u03` | note 7 / PDF 12, lower third through note 8 / PDF 13, top | Free scalar field | Existence question, normalized mode expansion, both Fourier phases, and the blue definitions of `p\cdot x` and `\omega_{\vec p}`. This is one source unit across the physical page break. |
| `yin-253a-n08-u01` | note 8 / PDF 13, upper and middle | Scalar commutator and covariant rewrite | Spatial momentum integral, exponential difference, literal `d^D p^\mu` rewrite, blue Lorentz-transformation annotations, and dependence on `(x-y)^2`. |
| `yin-253a-n08-u02` | note 8 / PDF 13, lower third | Spacelike vanishing argument | Equal-time frame choice, nonzero spatial separation, oddness under momentum reversal, vanishing integral, and checked microcausality conclusion. |
