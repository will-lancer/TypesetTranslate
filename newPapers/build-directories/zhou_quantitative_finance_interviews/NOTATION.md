# Zhou quantitative finance notation policy

This policy is binding for the native JHEP transcription of Xinfeng Zhou's
*A Practical Guide to Quantitative Finance Interviews*. The rendered source is
the authority for symbols, capitalization, and meaning. LaTeX commands make
that source notation searchable and stable; they do not silently modernize a
formula.

## Page 15 notation

The source page headed ``Notations'' defines the following symbols. Keep these
meanings throughout the edition.

| Source meaning | LaTeX form |
|---|---|
| for each, for every, for all | `\forall` |
| there exists | `\exists` |
| therefore | `\therefore` |
| implication, whenever (A) is true, (B) is true | `A \Rightarrow B` |
| such that | `\textit{s.t.}` |
| minimum of two quantities | `a \wedge b` |
| maximum of two quantities | `a \vee b` |
| finite sum | `\sum_{i=1}^{n}x_i` |
| finite product | `\prod_{i=1}^{n}x_i` |
| factorial | `n!`, with `0!=1` |
| modulo | `x\%y`; `x\bmod y` may be used when the binary operation is named in prose |
| empty set | `\Phi` |
| indefinite integral | `\int f(x)\,dx` |
| definite integral | `\int_a^b f(x)\,dx` |
| positive part | `x^+ = \max(x,0)` |
| normal distribution | `N(\mu,\sigma^2)` |
| cumulative density function label | `\mathit{cdf}` |
| probability density function label | `\mathit{pdf}` |

The capital `\Phi` is a source convention for the empty set. Do not replace it
with `\varnothing` or `\emptyset` in a native transcription. The words
``minimum'' and ``maximum'' may also occur in ordinary prose or in an order
statistic; the page-15 binary operators retain their `\wedge` and `\vee`
meanings.

## Probability and expectation

Use `\Omega` for the sample space, `\omega` for an outcome, and capital Latin
letters such as `A`, `B`, and `E` for events. The source probability of an
outcome is `P(\omega)` and the probability of an event is `P(A)`. Preserve the
source's event-product shorthand in formulas such as `P(AB)` when the source
uses it. Write an explicit set intersection as `A\cap B`.

Conditional probability uses a semantic vertical bar:

$$
P(A\mid B)=\frac{P(A\cap B)}{P(B)}.
$$

Use `\mid` in conditional probability and conditional expectation. A raw `|`
inside a probability expression is an OCR or LaTeX formatting warning. Use
`A^c` for the complement and `\cup` for a union. Mutually exclusive events have
empty intersection `\Phi`.

For random variables, keep the author's capitalization and local meaning. The
usual distinction is an uppercase random variable and a lowercase realized
value:

$$
X\sim N(\mu,\sigma^2),\qquad
F(a)=P(X\leq a),\qquad
p(x)=P(X=x),\qquad
f(x)=\frac{d}{dx}F(x).
$$

Use `p(x)` for a discrete probability mass function and `f(x)` for a
continuous probability density. Use `F` for a cumulative distribution
function. The standard normal distribution is written `N(0,1)`, and its cdf is
written `N(x)` in the Black--Scholes material. In that local context `N'(x)`
is its pdf. A multivariate normal keeps the source form
`X\sim N(\mu,\Sigma)`.

Expected values use the source `E[...]` form:

$$
E[X],\qquad E[g(X)],\qquad E[X\mid Y=y].
$$

Do not introduce `\mathbb{E}`, `\operatorname{E}`, or `\mathrm{E}` as a second
expectation convention. Use semantic operator typography for moments and
dependence:

$$
\operatorname{var}(X),\quad
\operatorname{cov}(X,Y),\quad
\operatorname{corr}(X,Y),\quad
\operatorname{std}(X),\quad
\rho(X,Y)=
\frac{\operatorname{cov}(X,Y)}
{\sqrt{\operatorname{var}(X)\operatorname{var}(Y)}}.
$$

The source's `\mathit{var}` and `\mathit{std}` labels in a directly transcribed
table may remain with that table. Equations and prose definitions use the
operator forms above. `\rho` is correlation when its arguments are random
variables or when a correlation subscript is shown.

## Distributions and stochastic processes

Keep distribution parameters in the source order. In particular, the source
uses `N(\mu,\sigma^2)`, exponential rate `\lambda`, gamma parameters
`(\alpha,\lambda)`, and beta parameters `(\alpha,\beta)`. Do not turn a rate
into a mean or change `\sigma^2` into `\sigma`.

The source uses both `W(t)` and `B_t` for Brownian motion in different local
examples. Preserve that choice at the source boundary. An Itô process is
written in the source form

$$
dX(t)=\beta(t,X)\,dt+\gamma(t,X)\,dW(t).
$$

Here `\beta` is the drift coefficient and `\gamma` is the diffusion
coefficient. The stochastic differential convention is

$$
(dW(t))^2=dt,\qquad dt\,dW(t)=0,\qquad (dt)^2=0,
$$

when those identities are invoked. Use `\partial` for ordinary partial
derivatives in Itô's lemma and keep the source's function arguments visible:

$$
df=\left(\frac{\partial f}{\partial t}
 +\beta(t,X)\frac{\partial f}{\partial x}
 +\frac12\gamma^2(t,X)\frac{\partial^2 f}{\partial x^2}\right)dt
 +\gamma(t,X)\frac{\partial f}{\partial x}\,dW(t).
$$

The drift term is the coefficient of `dt`. A martingale claim requires that
coefficient to vanish under the measure stated by the source.

## Finance and option Greeks

The option-pricing notation introduced on source page 153 is binding:

| Symbol | Source meaning |
|---|---|
| `T` | maturity date |
| `t` | current time |
| `\tau=T-t` | time to maturity |
| `S` | stock price at time `t` |
| `r` | continuous risk-free interest rate |
| `y` | continuous dividend yield |
| `\sigma` | annualized asset volatility |
| `c`, `p` | European call and put prices |
| `C`, `P` | American call and put prices |
| `D` | present value at `t` of future dividends |
| `K` | strike price |
| `PV` | present value at `t` |

For an option value `V(S,t)` or a price `c`, use the source Greek symbols:

$$
\Delta=\frac{\partial V}{\partial S},\qquad
\Gamma=\frac{\partial^2 V}{\partial S^2},\qquad
\Theta=\frac{\partial V}{\partial t},\qquad
\nu=\frac{\partial V}{\partial\sigma}.
$$

The source writes vega as the Greek `\nu`, not the Latin word `Vega` inside a
formula. Use `\rho` for an option's interest-rate sensitivity only in an
option-Greek context. Keep correlation as `\rho(X,Y)` or `\rho_{AB}` when the
surrounding formula is probabilistic. `\Delta x` remains a finite increment in
calculus and is not silently changed to an option delta.

European call and put payoffs use the source positive-part/max notation:

$$
\max(S_T-K,0),\qquad \max(K-S_T,0).
$$

The Black--Scholes normal cdf notation is `N(d_1)` and `N(d_2)`, with
`N'(d_i)` for the standard normal pdf. Keep `d_1`, `d_2`, `r`, `y`, `\sigma`,
and `\tau` in those formulas. Do not substitute `\Phi` for the normal cdf,
because `\Phi` is reserved by page 15 for the empty set in this edition.

## Vectors and matrices

The source uses ordinary italic Latin symbols for vectors in linear algebra:
`x`, `y`, `z`, and `X` are not automatically bolded. A column vector is
written in source order, for example

$$
x=[x_1,x_2,\ldots,x_n]^T,
\qquad x^Ty,
\qquad \lVert x\rVert.
$$

Matrices use uppercase symbols such as `A`, `X`, `P`, `R`, and `\Sigma` and
native LaTeX matrix environments such as `bmatrix` or `pmatrix`. Preserve
transposes as `^T`, determinants as `\det(A)`, and traces as
`\operatorname{trace}(A)`. Do not introduce `\vec`, `\overrightarrow`,
`\mathbf`, or `\boldsymbol` merely to restyle a source vector. A vector or
matrix may be bold only when the rendered source itself uses that distinction.

## Modulo, extrema, and factorials

Use `x\%y` for the page-15 modulo operation. The percent sign must be escaped
inside and outside mathematical mode. Use `x\bmod y` when the prose names the
operation or when ordinary modular arithmetic notation is clearer. Keep the
source's positive part `x^+` and binary minimum/maximum `a\wedge b` and
`a\vee b`. Use `\min` and `\max` for an explicit optimization or an order
statistic, such as `\min(X_1,\ldots,X_n)` and `\max(X_1,\ldots,X_n)`.

## Differentials and derivative operators

Keep ordinary differentials attached to their variables as `dx`, `dy`, `dt`,
`dS`, `dX(t)`, and `dW(t)`, with a thin mathematical space before an integral
differential when the source layout permits it:

$$
\int f(x)\,dx,\qquad
\frac{d f}{dx},\qquad
\frac{\partial f}{\partial x}.
$$

`d` is a differential, `\frac{d}{dx}` is an ordinary derivative, and
`\partial` denotes a partial derivative. Keep the source's explicit variable
in a derivative. Do not replace `dW` with `DW`, and do not turn a differential
into a probability symbol.

## Static release checks

`audit_notation.py` scans the native LaTeX tree. It reports Unicode punctuation
and mathematical glyphs, stray control-space punctuation, malformed argument
commands, unescaped percent signs, source-scan imports, and notation aliases
that violate this policy. A deliberate source exception must be documented on
the preceding line as `% NOTATION EXCEPTION: reason`; the exception is still
subject to source review.

The notation audit complements `audit_project.py`. It does not replace a
rendered-page inspection, a source-page coverage audit, or a compilation check.
