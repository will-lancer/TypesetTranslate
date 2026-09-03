# Independent review: Chapter 7 implicit exercises

**Status: PASS**

All five inventory records, their native hooks, the cited source pages, the
exercise files, and the combined solution file were reviewed.  Every in-scope
finding was repaired.  No compilation was run.

## Coverage and sources

| ID | Printed pages | PDF pages | Native hook | Audited scope |
|---|---:|---:|---|---|
| I-CH07-001 | 77 | 87 | `opening.tex:94` | $Z$, $W$, mean field, $\Gamma$, infinitesimal identities, failure terms |
| I-CH07-002 | 78 | 88 | `opening.tex:119` | Lehmann pole data, LSZ tensor basis, crossing, channel projectors, $SO(n)$ cases |
| I-CH07-003 | 78--81 | 88--91 | `sec7_2.tex:35` | All eight tasks assigned by footnote 4 |
| I-CH07-004 | 87 | 97 | `sec7_4.tex:132` | $G/H$, pion field, two-derivative action, expansion, currents, scattering, weak and soft limits |
| I-CH07-005 | 89 | 99 | `sec7_4.tex:235` | Projected Maurer--Cartan form, connection law, components, covariant checks, normalization |

The authoritative inventory was `implicit-exercises.json`.  Source claims were
checked against short layout-preserving extracts from `banks-qft.pdf`.  The
native transcription fixed the PDF page 99 global-action typo to
$g\mapsto g_1g$; the reviewed exercise uses only the local right action
$g\mapsto gh$.

## Findings and disposition

| Severity | ID | Finding | Disposition |
|---|---|---|---|
| High | I-CH07-004 | The authored pion coordinate used $\Sigma\mapsto L\Sigma R^\dagger$, opposite to Banks's displayed $L^\dagger\Sigma R$ convention.  The order parameter and current signs followed the former choice. | **Resolved.** The prompt and solution now use Banks's orientation.  The Noether currents were rederived as $J_L=2if^2\operatorname{Tr}(t^a\partial\Sigma\Sigma^\dagger)$ and $J_R=-2if^2\operatorname{Tr}(t^a\Sigma^\dagger\partial\Sigma)$, giving $V^{a\mu}=\epsilon^{abc}\pi^b\partial^\mu\pi^c+O(\pi^4)$ and $A^{a\mu}=-2f\partial^\mu\pi^a+O(\pi^3)$.  The matrix elements retain $F_\pi=2f$. |
| Medium | I-CH07-003 | The solution omitted Banks's explicit reason that a conserved boost charge can fail to commute with $H$. | **Resolved.** It now displays $K^i=tP^i-\int x^iT^{00}$, $\partial_tK^i=P^i$, and $[H,K^i]=iP^i$. |
| Medium | I-CH07-003 | Banks's displayed metric derivative lacks the factor and sign required by the standard Hilbert definition used in the exercise.  Calling this only a convention hid the normalization needed for translation charges. | **Resolved.** The solution states $T_{\rm source}^{\mu\nu}=-T_{\rm H}^{\mu\nu}/2$ and keeps the standard Hilbert tensor throughout the proof. |
| Medium | I-CH07-002 | The $SO(n)$ discussion named $SO(4)$ but left the other rank-four cases vague.  The source also calls a single epsilon tensor $O(n)$ invariant, which fails under reflections. | **Resolved.** The answer now identifies the extra $SO(2)$ epsilon-delta tensors, the $SO(4)$ epsilon tensor, and the absence of a new single-epsilon rank-four tensor for $n=3$ or $n>4$. |
| Medium | I-CH07-005 | The prompt used a positive orthonormal trace while the component derivation silently switched to anti-Hermitian generators. | **Resolved.** The invariant bilinear form and its possible matrix-trace sign are explicit.  Component indices and structure constants now use one anti-Hermitian convention, and the curvature conjugation check is shown. |
| Medium | I-CH07-001 | The claim that every zero-source vertex is invariant lacked the broken-vacuum qualification needed by the following section. | **Resolved.** The text distinguishes a symmetry-invariant zero-source state from an infinite-volume limit that selects one vacuum on a group orbit. |
| Low | all | The exercise files and solution blocks lacked stable source locators.  Four compound prompts lacked lettered boundaries. | **Resolved.** Exact `BANKS-SOURCE` markers were added.  The exercise item counts are 3, 4, 8, 4, and 3, with matching solution headings. |
| Low | I-CH07-002/003/004 | Four `\qquad` commands had lost their backslash, and one singlet projector read `P_{mathbf1}`. | **Resolved.** All five TeX defects were corrected. |

## Mathematical checks

- The $O(3)$ projectors are complete and idempotent, and reconstruct the
  crossed amplitude with residual $2.22\times10^{-16}$.
- Banks's special-conformal vector obeys the four-dimensional conformal
  Killing equation with zero numerical residual.
- A finite $SU(2)$ differentiation check reproduces the pion Lagrangian
  through quartic order with residual $4.01\times10^{-11}$.  The current
  residual falls by a factor $8.02$ when the fields are halved, matching the
  displayed $O(\pi^3)$ remainder.
- An explicit reductive $SU(2)/U(1)$ example verifies the finite connection
  law and $D_\mu g$ covariance with residuals below $3.5\times10^{-17}$.

## Static checks

- Braces and LaTeX environment stacks balance in all six TeX files.
- Each exercise ID and each `\BanksImplicitSolution` occurs exactly once.
- Source-marker counts are five exercise markers plus one section and five
  solution markers.
- Scans found no malformed `\qquad`, `P_{mathbf1}`, stale equation-(1)
  reference, `TODO`, `FIXME`, or trailing whitespace.
- `chktex` found no warning outside its inspected categories 3, 8, 25, and 36.
  Those categories flag intentional IDs, TeX dashes, enum labels, and harmless
  multiplication or parenthesis forms here.

## Files repaired

- `latex/implicit/I-CH07-001.tex`
- `latex/implicit/I-CH07-002.tex`
- `latex/implicit/I-CH07-003.tex`
- `latex/implicit/I-CH07-004.tex`
- `latex/implicit/I-CH07-005.tex`
- `latex/solutions/chapter07-implicit.tex`

**PASS: no in-scope mathematical, source, structural, or static issue remains.**
