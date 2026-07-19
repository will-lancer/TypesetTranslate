# Weinberg Vol. II — Notation Modernization Guide

Baseline catalog of recurring notational choices for Steven Weinberg, *The Quantum Theory of Fields*, Volume II (*Modern Applications*), inherited from the completed Volume I modernization and retained unless a Volume II-specific source convention requires an explicit exception.

This is a **pattern catalog**, not a line-by-line errata. The scan remains authoritative for wording, mathematics, and numbering. The house rules below are the approved modernization layer for this edition and therefore override the source's presentation where stated.

Baseline sources inspected in Volume I: Notation (pp. xxv–xxvi), Chs. 2–6 (states, S-matrix, creation/annihilation, fields, Dirac formalism, Feynman rules), plus spot checks through later chapters. Volume II-specific additions should be documented here during transcription.

---

## Weinberg-specific house rules

Apply these rules during transcription rather than saving them for an unbounded cleanup pass:

- **Blackboard bold:** Use `\mathbb{R}`, `\mathbb{C}`, `\mathbb{Z}`, `\mathbb{Z}_2`, and analogous notation for standard number systems, spaces, and discrete groups. Keep generic groups such as `G` and `H` in ordinary italic. Use `\mathbf{1}` for an identity operator or matrix; do not use `\mathbb{1}`.
- **Paper references:** Replace Weinberg's superscript reference markers with bracketed inline markers, placed before terminal punctuation: `Dirac~[1]`, `Wigner~[2]`, `Refs.~[4,5]`, `result~[3a]`. Preserve the chapter-local displayed numbering, give every reference-list item a stable label, and hyperlink every inline marker to its entry.
- **Footnotes:** Use ordinary automatically numbered `\footnote{...}` commands. Do not reproduce `*`, `**`, or `\dagger` markers, do not redefine `\thefootnote`, and never rewind the footnote counter. For a section-title note, use an ordinary numbered `\footnotemark` and matching `\footnotetext`, and give the section an optional table-of-contents title without the marker so the moving argument does not create a dangling footnote link.
- **Parity and time reversal:** Use `\mathcal{P}` and `\mathcal{T}` only for the spacetime inversion matrices acting on four-vectors. Use `P=U(\mathcal{P},0)` and `T=U(\mathcal{T},0)` for the corresponding Hilbert-space operators. Use different symbols for unrelated objects: `\Pi` and `\Theta` for internal multiplet matrices and `\gamma` for a path. Momentum `P^\mu` and generic symmetry transformations `T(\theta)` retain their established meanings.
- **Products:** Use `\cdot`, never `\times`, throughout the modernized chapters. This applies even to matrix dimensions and Cartesian products in this edition.
- **Creation and annihilation operators:** Put momentum, spin, species, and analogous operator labels in subscripts: `a(p,\sigma,n)\to a_{p,\sigma,n}` and `a^\dagger(\mathbf p,\sigma,n)\to a^\dagger_{\mathbf p,\sigma,n}`. Apply the same convention to other unambiguous creation or annihilation operators, but do not rewrite unrelated functions merely because they use the letter `a`.
- **Calligraphic symbols:** Use `\mathcal`, not `\mathscr`, for Lagrangian and Hamiltonian densities and for other applicable calligraphic symbols: `\mathcal L`, `\mathcal H`, `\mathcal F`, `\mathcal J`, and so on.
- **Dirac slash:** Use the project command `\sl{p}` (and similarly `\sl{k}`, `\sl{e}`, etc.), which is backed by the `slashed` package. Do not use `\not p` or `\not\!p`; `\notag` remains the ordinary `amsmath` line-number suppression command and must not be changed.
- **Cross-references:** Every numbered equation and figure must have a stable `\label`; prose must refer to them with `\eqref` and `\ref`. Every numbered chapter-reference entry must also have a stable label, and inline citation markers must hyperlink to the matching entry while retaining Weinberg's visible chapter-local numbering.
- **Display layout:** Keep a display on one line when it fits comfortably and reads clearly. Use multiple aligned lines only when line length, logical grouping, or legibility benefits from the break; do not preserve scan-induced line wrapping.
- **Batalin--Vilkovisky antifields (Chapter 15):** Write the antifield paired with a field `x^n` as `x_n^{\ddagger}`. Reserve `*` for complex conjugation and `\dagger` for Hermitian adjoints, exactly as the surrounding mathematics requires. Never use an antifield glyph as a footnote marker. State Grassmann parity and ghost number in prose or equations as in the source; this presentation change does not alter the BV grading conventions.

These are deliberate semantic distinctions, not a mechanical replacement of every letter `P` or `T`.

---

## 1. No Dirac bra–ket notation (the biggest pattern)

Weinberg treats Hilbert-space vectors as ordinary mathematical vectors. States are bare symbols with labels as subscripts; inner products use parentheses.

| Weinberg | Modern replacement |
|---|---|
| $\Psi$, $\Phi$ (state-vectors) | $\|\Psi\rangle$, $\|\Phi\rangle$ |
| $\Psi_{p,\sigma}$ | $\|p,\sigma\rangle$ |
| $\Psi_{p_1\sigma_1 n_1;\,p_2\sigma_2 n_2;\,\ldots}$ | $\|p_1,\sigma_1,n_1;\,p_2,\sigma_2,n_2;\,\ldots\rangle$ |
| $\Phi_{q_1\cdots q_N}$ | $\|q_1,\ldots,q_N\rangle$ |
| $\Phi_0$ (vacuum) | $\|\Omega\rangle$ |
| $(\Phi,\Psi)$ | $\langle\Phi\|\Psi\rangle$ |
| $(\Psi_{p',\sigma'},\Psi_{p,\sigma})=\delta^3(\mathbf{p}'-\mathbf{p})\,\delta_{\sigma'\sigma}$ | $\langle p',\sigma'\|p,\sigma\rangle=\delta^3(\mathbf{p}'-\mathbf{p})\,\delta_{\sigma'\sigma}$ |
| $O\Psi$ | $O\|\Psi\rangle$ |
| $(\Psi,O\Phi)$ | $\langle\Psi\|O\|\Phi\rangle$ |

He footnotes that one *may* write $\langle 1\|2\rangle$ for $(\Psi_1,\Psi_2)$, but the book almost never does. Prefer Dirac notation throughout a modernized edition.

**Worked examples**

- $P^\mu\Psi_{p,\sigma}=p^\mu\Psi_{p,\sigma}$ → $P^\mu\|p,\sigma\rangle=p^\mu\|p,\sigma\rangle$
- $U(\Lambda)\Psi_{p,\sigma}=\cdots\sum_{\sigma'}D_{\sigma'\sigma}(W)\Psi_{\Lambda p,\sigma'}$ → $U(\Lambda)\|p,\sigma\rangle=\cdots\sum_{\sigma'}D_{\sigma'\sigma}(W)\|\Lambda p,\sigma'\rangle$
- $a^\dagger(q)\Phi_{q_1\cdots q_N}=\Phi_{q\,q_1\cdots q_N}$ → $a^\dagger_q\|q_1,\ldots,q_N\rangle=\|q,q_1,\ldots,q_N\rangle$
- $a^\dagger(q_1)\cdots a^\dagger(q_N)\Phi_0=\Phi_{q_1\cdots q_N}$ → $a^\dagger_{q_1}\cdots a^\dagger_{q_N}\|\Omega\rangle=\|q_1,\ldots,q_N\rangle$

---

## 2. In/out states labeled $+$ / $-$ (admittedly backwards)

| Weinberg | Modern replacement |
|---|---|
| $\Psi_\alpha^+$ (‘in’ state) | $\|\alpha\rangle_{\mathrm{in}}$ or $\|\alpha;\,\mathrm{in}\rangle$ |
| $\Psi_\beta^-$ (‘out’ state) | $\|\beta\rangle_{\mathrm{out}}$ or $\|\beta;\,\mathrm{out}\rangle$ |
| $S_{\beta\alpha}=(\Psi_\beta^-,\Psi_\alpha^+)$ | $S_{\beta\alpha}=\langle\beta;\,\mathrm{out}\|\alpha;\,\mathrm{in}\rangle$ |

Weinberg himself notes (Ch. 3) that the $+$ / $-$ labels “may seem backward.” They come from the $\pm i\epsilon$ in the Lippmann–Schwinger equation, not from any intuitive early/late-time labeling. Prefer explicit `in` / `out` tags.

Related free-particle / asymptotic notation:

| Weinberg | Modern |
|---|---|
| $\Phi_\alpha$ (free multi-particle state) | $\|\alpha\rangle_0$ or $\|\alpha\rangle$ (free) |
| $a_{\mathrm{in}}(p)$, $a_{\mathrm{out}}(p)$ | $a_{p,\mathrm{in}}$, $a_{p,\mathrm{out}}$ |

---

## 3. Metric signature and index order

**Keep Weinberg’s mostly-plus metric.** Do not flip to mostly-minus.

From the Notation pages and §2.3:

- Spacetime indices run over **$1,2,3,0$** (time listed last).
- Metric: $\eta_{11}=\eta_{22}=\eta_{33}=+1$, $\eta_{00}=-1$ (mostly-plus).
- d’Alembertian: $\Box=\nabla^2-\partial_t^2$.
- Mass shell: $p^2+M^2=0$, i.e. $p^2=-M^2$.
- Standard rest momentum written as $k^\mu=(0,0,0,M)$ (time component in the *last* slot).

| Weinberg | Modern replacement |
|---|---|
| Index order $1,2,3,0$ | Index order $0,1,2,3$ |
| $\eta_{\mu\nu}=\mathrm{diag}(+1,+1,+1,-1)$ | Keep mostly-plus: $\eta_{\mu\nu}=\mathrm{diag}(-1,+1,+1,+1)$ with order $(0,1,2,3)$ |
| $p^2=-M^2$ | Keep $p^2=-m^2$ |
| $k^\mu=(0,0,0,M)$ | $k^\mu=(M,\mathbf{0})=(m,0,0,0)$ |
| $(x-x')^2\ge 0$ for spacelike | Keep $(x-x')^2\ge 0$ for spacelike |
| $\Box=\nabla^2-\partial_t^2$ | Keep $\Box=\nabla^2-\partial_t^2$ (equiv. $\Box=\partial_\mu\partial^\mu$ with mostly-plus) |

**Recommendation:** Keep mostly-plus $(-+++)$. The only index cleanup is listing components as $(0,1,2,3)$ and writing rest-frame four-vectors as $(m,\mathbf{0})$ instead of Weinberg’s $(0,0,0,M)$ slotting. On-shell conditions stay $p^2=-m^2$; spacelike separation stays $(x-x')^2\ge 0$. Document this once in Notation frontmatter and never mix with mostly-minus formulas from Peskin-style notes.

---

## 4. Dirac / Clifford conventions tied to the metric

| Weinberg | Modern replacement |
|---|---|
| $\{\gamma_\mu,\gamma_\nu\}=2\eta_{\mu\nu}$ | Keep $\{\gamma^\mu,\gamma^\nu\}=2\eta^{\mu\nu}$ with mostly-plus $\eta$ |
| $\gamma_5=i\gamma_0\gamma_1\gamma_2\gamma_3$ | $\gamma^5=i\gamma^0\gamma^1\gamma^2\gamma^3$ (keep; consistent with mostly-plus) |
| $\beta=i\gamma^0$ | Keep $\beta=i\gamma^0$, or write adjoints with $\beta$ explicitly once and then use $\bar{u}$ |
| $\bar{u}=u^\dagger\beta$ | Keep $\bar{u}=u^\dagger\beta$ (with $\beta=i\gamma^0$), or define $\bar{u}=u^\dagger i\gamma^0$ and drop the name $\beta$ |
| $\epsilon^{0123}=+1$ | Keep $\epsilon^{0123}=+1$ |
| Historical $\alpha_4$ (Ch. 1) for what is usually $\beta$ | $\beta$ (or $i\gamma^0$) |
| $\gamma^i=-i\alpha^i\alpha_4$, $\gamma^0=-i\alpha_4$ (Ch. 1) | Keep the mostly-plus dictionary; prefer stating $\beta=i\gamma^0$ up front |

Because we keep mostly-plus, Weinberg’s $\beta=i\gamma^0$ and $\bar{u}=u^\dagger\beta$ are the consistent Dirac-adjoint convention—do not replace them with the mostly-minus $\bar{u}=u^\dagger\gamma^0$. Optionally retire the letter $\beta$ and always write $i\gamma^0$, but do not change the factor of $i$.

---

## 5. Creation / annihilation and multi-particle states

| Weinberg | Modern replacement |
|---|---|
| $\Phi_0$ | $\|\Omega\rangle$ |
| $a^\dagger(q)\Phi_{q_1\cdots q_N}=\Phi_{q\,q_1\cdots q_N}$ | $a^\dagger_q\|q_1,\ldots,q_N\rangle=\|q,q_1,\ldots,q_N\rangle$ |
| $a(q)\Phi_{q_1\cdots q_N}=\sum_r(\pm)^{r+1}\delta(q-q_r)\Phi_{\ldots\hat{q}_r\ldots}$ | $a_q\|q_1,\ldots,q_N\rangle=\sum_r(\pm)^{r+1}\delta(q-q_r)\|\ldots,\hat q_r,\ldots\rangle$ |
| $(\pm)$ upper = bosons, lower = fermions | Keep the $\pm$ convention, or write $(-1)^F$ / explicit Bose/Fermi cases |
| $a^\dagger(\mathbf{p},\sigma,n)$ | $a^\dagger_{\mathbf{p},\sigma,n}$ |
| Measure often $d^3p$ with factors absorbed into $u,v,a$ | Prefer relativistic measure $\dfrac{d^3p}{(2\pi)^3 2E_{\mathbf{p}}}$ with correspondingly normalized $a_{\mathbf p}$, as in Peskin |

Weinberg’s $N(p)=\sqrt{p^0}$ state normalization (§2.5) is standard relativistically covariant normalization; **keep it**, but express overlaps in Dirac notation:

$$
\langle p',\sigma'|p,\sigma\rangle=2p^0\,\delta^3(\mathbf{p}'-\mathbf{p})\,\delta_{\sigma'\sigma}
$$

(or whatever overall $2\pi$ convention you adopt—state it once and stick to it).

---

## 6. Fields: $\psi^+$ annihilates, $\psi^-$ creates

| Weinberg | Modern replacement |
|---|---|
| $\psi^+_\ell(x)=\sum\int d^3p\,u_\ell(x;\mathbf{p},\sigma,n)\,a(\mathbf{p},\sigma,n)$ | $\psi^{(+)}_\ell(x)=\sum\int d^3p\,u_\ell(x;\mathbf p,\sigma,n)\,a_{\mathbf p,\sigma,n}$ |
| $\psi^-_\ell(x)=\sum\int d^3p\,v_\ell(x;\mathbf{p},\sigma,n)\,a^\dagger(\mathbf{p},\sigma,n)$ | $\psi^{(-)}_\ell(x)=\sum\int d^3p\,v_\ell(x;\mathbf p,\sigma,n)\,a^\dagger_{\mathbf p,\sigma,n}$ |
| Full causal field $\psi=\psi^++\psi^-$ (schematically) | $\psi=\psi^{(+)}+\psi^{(-)}$ with a one-line glossary |
| Coefficient args $u_\ell(x;\mathbf{p},\sigma,n)$ | $u_\ell(\mathbf{p},\sigma)\,e^{-ip\cdot x}$ (factor plane wave out explicitly when possible) |
| Catch-all component index $\ell$ | Split into Lorentz/spinor index + species when clarity helps: $\psi^n_\alpha(x)$ |

The $+$ / $-$ on fields means **positive / negative frequency**, which matches annihilation / creation for particle operators—but collides with the $+$ / $-$ on **in/out states**. In a modernized text, never overload both meanings. Prefer:

- states: $\|\alpha\rangle_{\mathrm{in}}$, $\|\beta\rangle_{\mathrm{out}}$
- fields: $\psi^{(+)}$, $\psi^{(-)}$ (frequency) or just write $\psi=\int(u\,a+v\,a^\dagger)$ without $\pm$ labels

Also: Weinberg uses **$\Psi$ for states** and **$\psi$ for fields**. That distinction is good—**keep it**—but once states become kets, the capital/lowercase split matters less; still useful for field operators vs. c-number wavefunctions.

---

## 7. Hamiltonians, interactions, and densities

| Weinberg | Modern replacement |
|---|---|
| $H=H_0+V$ | $H=H_0+H_{\mathrm{int}}$ (or $H_I$) |
| $V(t)=e^{iH_0 t}Ve^{-iH_0 t}$ | $H_I(t)$ (interaction picture) |
| $V(t)=\int d^3x\,\mathcal{H}(\mathbf{x},t)$ | $H_I(t)=\int d^3x\,\mathcal{H}_I(\mathbf{x},t)$ |
| $\mathcal{H}(x)$ (Hamiltonian density) | $\mathcal{H}_I(x)$ |
| Calligraphic $\mathcal{H}$ vs $H$ | Keep density vs. integrated distinction; avoid bare $V$ |

$V$ for “interaction” is old-fashioned QM scattering language. In QFT it constantly collides with potential, volume, and vertex. Prefer $H_{\mathrm{int}}$ / $\mathcal{H}_I$.

---

## 9. Poincaré / Lorentz packaging

| Weinberg | Modern replacement |
|---|---|
| “Inhomogeneous Lorentz group” | Poincaré group (applied throughout) |
| $T(\Lambda,a)$ (classical transformation) | $(\Lambda,a)$ or $\mathcal{P}(\Lambda,a)$ |
| $U(\Lambda,a)$ | $U(\Lambda,a)$ (fine) or $U(\Lambda,a)$ with ket: $U(\Lambda,a)\|p,\sigma\rangle$ |
| $U_0(\Lambda,a)$ (free) | $U_0(\Lambda,a)$ or $U^{(0)}(\Lambda,a)$ |
| Generators $J^{\mu\nu}$, $P^\mu$ | Keep (standard) |
| Field-rep generators $\mathcal{J}^{\mu\nu}=-\frac{i}{4}[\gamma^\mu,\gamma^\nu]$ | $S^{\mu\nu}$ or $\Sigma^{\mu\nu}$ (common in particle texts) |
| Wigner rotation $W(\Lambda,p)=L^{-1}(\Lambda p)\Lambda L(p)$ | Keep (this is already the standard modern name) |

---

## 10. S-matrix / T-matrix packaging

| Weinberg | Modern replacement |
|---|---|
| $S_{\beta\alpha}=(\Psi_\beta^-,\Psi_\alpha^+)$ | $S_{\beta\alpha}=\langle\beta;\,\mathrm{out}\|\alpha;\,\mathrm{in}\rangle$ |
| $S_{\beta\alpha}=\delta(\beta-\alpha)-2\pi i\,\delta(E_\beta-E_\alpha)\,T_{\beta\alpha}$ (schematic) | Keep structure; write $T_{\beta\alpha}=\langle\beta\|T\|\alpha\rangle$ |
| Operator $S$ with free-state matrix elements equal to $S_{\beta\alpha}$ | Keep; $\langle\beta\|S\|\alpha\rangle=S_{\beta\alpha}$ |
| Connected part $S^c$ / cluster partitions | Keep the idea; write $S^c_{\beta\alpha}$ or $C_{\beta\alpha}$ with a clear definition (Weinberg’s recursive partition sum is good physics, dense notation) |

Completeness written as $\int d\beta\,(\Psi_\gamma^+,\Psi_\beta^-)(\Psi_\beta^-,\Psi_\alpha^+)$ → $\int d\beta\,|\beta\rangle_{\mathrm{out}}\langle\beta|_{\mathrm{out}}=1$ (on the appropriate subspace).

---

## 11. Operators without hats; matrices as “1”

| Weinberg | Modern |
|---|---|
| Operators and their eigenvalues share glyphs: $P^\mu\Psi=p^\mu\Psi$ | Prefer $P^\mu\|p\rangle=p^\mu\|p\rangle$ (ket already disambiguates); optional $\hat{P}^\mu$ if needed |
| Identity matrix written $1$ | $\mathbf{1}$ or $\mathbb{1}$ or $I$ |
| No hats on $a,a^\dagger,H,V,\ldots$ | Optional hats; not required if Dirac notation is in place |

---

## 12. Levi-Civita, boldface, and miscellaneous Notation-page items

These are mostly fine; only small cleanups:

| Weinberg | Note / replacement |
|---|---|
| Boldface = 3-vectors | Keep |
| $\hat{\mathbf{v}}=\mathbf{v}/\|\mathbf{v}\|$ | Keep |
| \vec{p} | Replace with \mathbf{p} |
| Dot = time derivative | Keep, or use $\partial_t$ in dense QFT passages |
| $+\,\mathrm{H.c.}$ / $+\,\mathrm{c.c.}$ | Keep |
| Asterisk on operator matrices “not transposed” | Prefer explicit $\mathcal{O}^*$ vs $\mathcal{O}^\dagger$ explanation once; avoid silent dual use |
| $-e$ = rationalized electron charge, $\alpha=e^2/4\pi$ | Keep Heaviside–Lorentz; state it |
| $\hbar=c=1$ except Ch. 1 | Keep |

---

## 13. Pattern summary (cheat sheet)

Use this as the default rewrite map when modernizing chunks:

1. **States:** $\Psi_{p,\sigma}\to\|p,\sigma\rangle$, $\Phi_0\to\|\Omega\rangle$, $(\Psi,\Phi)\to\langle\Psi\|\Phi\rangle$.
2. **Asymptotics:** $\Psi^\pm\to\|\cdot\rangle_{\mathrm{in/out}}$.
3. **Metric:** keep mostly-plus; only clean index order to $(0,1,2,3)$ and write rest frames as $(m,\mathbf{0})$. Keep $p^2=-m^2$ and spacelike $(x-x')^2\ge 0$.
4. **Spinors:** keep $\beta=i\gamma^0$ and $\bar{u}=u^\dagger\beta$ (or write $\bar{u}=u^\dagger i\gamma^0$).
5. **Vacuum:** always $\|\Omega\rangle$ — never $\|0\rangle$ or $\|\mathrm{vac}\rangle$.
6. **Interaction:** $V$, $V(t)$, $\mathcal{H}$ → $H_{\mathrm{int}}$, $H_I(t)$, $\mathcal{H}_I$.
7. **Fields:** $\psi^\pm$ frequency pieces → $\psi^{(\pm)}$ or expanded $u\,a+v\,a^\dagger$; don’t reuse $\pm$ for in/out.
8. **Disambiguate** $T$, $P$, $S$ overloads with subscripts or alternate glyphs.
9. **Keep** Wigner rotations, little groups, cluster decomposition, and $N(p)=\sqrt{p^0}$ normalization—these are strengths, not defects.

---

## 14. What *not* to “fix”

These look idiosyncratic but are deliberate and modernize poorly if altered casually:

- Particle-first → field-later logical order (architectural, not notational).
- Induced representations / little-group construction of one-particle states.
- Cluster decomposition as the principle selecting creation/annihilation polynomials.
- Causality ⇒ antiparticles and spin-statistics derivations.
- Explicit ISO(2) matrix forms for massless little groups.
- $(A,B)$ classification of Lorentz irreps (standard; keep).

Modernize **symbols and conventions**, not the logical spine of the book.

---

## 15. Suggested frontmatter blurb for a modernized edition

> **Notation (modernized).** We use Dirac notation: states $\|p,\sigma\rangle$, vacuum $\|\Omega\rangle$, inner products $\langle\phi\|\psi\rangle$. The metric is mostly-plus, $\eta_{\mu\nu}=\mathrm{diag}(-1,+1,+1,+1)$, so $p^2=-m^2$ on shell and spacelike separations satisfy $(x-x')^2\ge 0$. Dirac adjoints use $\bar{u}=u^\dagger\beta$ with $\beta=i\gamma^0$. The interaction Hamiltonian is $H_I(t)=\int d^3x\,\mathcal{H}_I(x)$. Creation and annihilation labels are written as subscripts, calligraphic symbols with `\mathcal`, products with `\cdot`, and Dirac slashes with `\sl{p}`. Numbered equations, figures, and chapter references carry stable hyperlinks. Asymptotic states are labeled $\|\alpha\rangle_{\mathrm{in}}$ and $\|\beta\rangle_{\mathrm{out}}$. Positive- and negative-frequency field pieces are $\psi^{(\pm)}$. Weinberg’s index order $(1,2,3,0)$, parenthesis inner products, $\Phi_0$ vacuum, and $V$-for-interaction notation are translated according to `NOTATION.md`.
