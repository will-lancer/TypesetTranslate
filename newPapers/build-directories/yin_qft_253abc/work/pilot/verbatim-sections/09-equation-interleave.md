# Exact-note equation and board interleave map

Frozen transcript: `work/pilot/transcript.cleaned.jsonl`, SHA-256 `5ac8ac5fb25a3235d8fa11b2b6be99b5f2bb9329d307c4045629544f4e43e9bd`. Record intervals use `[start,end)`. Every `notes-exact.tex:Lx-Ly` range below is inclusive and is the literal copy authority. Copy that source range rather than the abbreviated key in this map.

Actions: `states` means Yin says the content while writing or pointing; `derives` means he gives the displayed inference; `points silently` means the exact note supplies board material without a corresponding spoken derivation. Composite displays render once at the stated final insertion point.

Fragment keys: `F01=01-0502-1500.tex`, `F02=02-1500-2500.tex`, `F03=03-2500-3500.tex`, `F04=04-3500-4500.tex`, `F05=05-4500-5500.tex`, `F06=06-5500-6500.tex`, `F07=07-6500-7500.tex`, `F08=08-7500-8013.tex`.

Source rules:

- Keep every creator superscript literally as `a^+`, including indexed forms such as `a_{\vec p}^{+}`. Spoken `a^\dagger` remains in the transcript prose.
- Keep the printed covariant measure literally as `d^D p^\mu`.
- `PRINTED NORMALIZATION` identifies a coefficient or measure fixed by the handwritten page. The uncertain extra factor raised in `YIN-OY-T000141` is absent from the printed convention.

## Original note p. 1, physical PDF p. 6

The complete branching figure `notes-exact.tex:L43-L109` renders at `F02:L40`, after `YIN-OY-T000062` `[00:18:21.740,00:18:56.460)` and before `YIN-OY-T000063` `[00:18:56.460,00:19:14.400)`. This is figure placement 1. The rows inside the figure use the following acquisition anchors.

| Exact source unit | Speech or board anchor | Final insertion | Action |
|---|---|---|---|
| `notes-exact.tex:L39` `\YinLine{Q: What is QFT?}` | `T000016` `[00:05:02.580,00:05:13.500)` | `F01`, after `T000016` | states |
| `L51` `A: QM $+$ locality` | `T000017` `[00:05:13.500,00:05:33.360)` | inside figure 1 | states |
| `L52-L58` local/UV-complete and effective-field-theory branches, gray parenthesis, dashed divider | `T000018-T000020` `[00:05:33.360,00:06:42.900)` | inside figure 1 | states; dashed divider points silently |
| `L61-L63` Poincare symmetry and infinitely many degrees of freedom | `T000021-T000024` `[00:06:42.900,00:08:04.800)` | inside figure 1 | states |
| `L64-L65` local field operators and micro causality | `T000028-T000030` `[00:08:51.120,00:09:38.279)` | inside figure 1 | states |
| `L74-L80` perturbative path integral and long-distance/low-energy observables | `T000034-T000038` `[00:10:10.980,00:11:38.880)` | inside figure 1 | states |
| `L66-L67` Examples; `\phi^4` in `D=2,3` | `T000046-T000049` `[00:13:23.160,00:14:26.459)` | inside figure 1 | states |
| `L85-L87` `\phi^4` in `D=4`, QED, standard model | `T000050-T000053` `[00:14:26.459,00:15:15.899)` | inside figure 1 | states |
| `L71` Yang--Mills / QCD | `T000054-T000055` `[00:15:15.899,00:15:50.579)` | inside figure 1 | states |
| `L68-L70` statistical Ising model near criticality | `T000056-T000057` `[00:15:50.579,00:16:46.440)` | inside figure 1 | states |
| `L92-L97` chiral perturbation theory, GR, violet frame | `T000058-T000059` `[00:16:46.440,00:17:22.140)` | inside figure 1 | states; frame points silently |
| `L99-L107` blue `253a` arrows and violet `253b` arrows | `T000060` `[00:17:22.140,00:17:55.799)` | inside figure 1 | points silently; spoken allocation is partly inaudible |
| `L82-L90`, `L97` printed renormalizable and non-renormalizable labels and frames | `T000061-T000062` `[00:17:55.799,00:18:56.460)` | inside figure 1 | states; exact colors and frame membership point silently |

## Original note p. 2, physical PDF p. 7

| Exact source unit | Canonical insertion point | Fragment marker | Action |
|---|---|---|---|
| `notes-exact.tex:L114-L116` `\underline{Plan of 253a}` | after `T000064` `[00:19:14.400,00:19:29.640)` | `F02`, after record | states |
| `L118` item (1), Lagrangian formulation of QM | after `T000067` `[00:20:05.039,00:20:16.080)` | collect into `F02:L87` | states |
| `L119` path integral, regularization | after `T000075` `[00:22:18.480,00:22:31.740)` | `F02:L87` | states |
| `L120` perturbation theory, Feynman diagrams | after `T000076` `[00:22:31.740,00:22:52.940)` | `F02:L87` | states |
| `L121` renormalization and counter terms | after `T000077` `[00:22:52.940,00:23:12.179)` | `F02:L87` | states |
| `L124-L125` item (2), relativistic particles and fields; `\phi^4` | after `T000079` `[00:23:27.900,00:23:45.419)` | collect into `F02:L104` | states |
| `L126-L127` Green functions; asymptotic states | after `T000080` `[00:23:45.419,00:24:04.980)` | `F02:L104` | states |
| `L128` S-matrix, LSZ reduction | after `T000081` `[00:24:04.980,00:24:21.900)` | `F02:L104` | states |
| `L131` item (3), particles and fields with spin | after `T000084` `[00:25:00.000,00:25:08.880)` | defer `F02:L109` across the fragment seam; render in `F03` after `T000084` | states |
| `L132` classification of relativistic particles | after `T000087` `[00:25:42.720,00:26:00.960)` | `F03`, after record | states |
| `L133-L134` fermions, gauge bosons, QED | after `T000088` `[00:26:00.960,00:26:11.400)` | `F03`, after record | states |
| `L135-L136` electron `g`-factor and Lamb shift | after `T000089` `[00:26:11.400,00:26:29.039)` | `F03`, before `T000090` | electron application states; Lamb shift points silently |

## Original note p. 3, physical PDF p. 8

| Exact source unit | Canonical insertion point | Fragment marker | Action |
|---|---|---|---|
| `notes-exact.tex:L141-L143` prelude question | after `T000096` `[00:28:09.799,00:28:32.100)` | `F03`, after record | states |
| `L146` Hilbert space `\mathcal H` | after `T000097` `[00:28:32.100,00:29:00.299)` | `F03`, after record | states |
| `L147` vacuum and `H\ket{\Omega}=0` | after `T000099` `[00:29:24.960,00:29:42.779)` | `F03:L54` | derives from Poincare-invariant vacuum; printed zero-energy convention |
| `L148-L150` one-particle state, gray `p^\mu\equiv(p^0,\vec p)`, gray `D`-dimensional marginalia | after `T000103` `[00:31:18.659,00:31:36.059)` | `F03:L61` follows the `p^\mu` statement; retain the full marginal block through `T000103` | states; gray placement points silently |
| `L151-L153` `H\ket{\vec p}=\sqrt{\vec p^{\,2}+m^2}\ket{\vec p}` | after `T000105` `[00:32:00.299,00:32:23.100)` | `F03:L74` | states |
| `L154-L159` multiparticle state, non-interacting qualification, summed energy | after `T000109` `[00:33:21.559,00:33:52.940)` | `F03:L87` | states |
| `L161-L169` creation/annihilation brace with literal `a_{\vec p}^{+}` and `a_{\vec p}` | after `T000123` `[00:36:25.579,00:36:58.190)` | `F04:L20` | states; retain `a^+` |
| `L170-L172` `\ket{\vec p}=a_{\vec p}^{+}\ket{\Omega}` | after `T000125` `[00:37:00.480,00:37:22.849)` | `F04:L24` | states; retain `a^+` |

## Original note p. 4, physical PDF p. 9

| Exact source unit | Canonical insertion point | Fragment marker | Action |
|---|---|---|---|
| `notes-exact.tex:L177-L181` two-particle state with two `a^+` operators | after `T000127` `[00:37:22.859,00:37:38.510)` | `F04:L28` | states; retain both `a^+` marks |
| `L182-L184` `[a,a]=[a^{+},a^{+}]=0` | after `T000131` `[00:38:00.260,00:38:19.849)` | `F04:L36` | states; retain `a^+` |
| `L185-L188` `[a_{\vec p},a_{\vec p'}^{+}]=\delta^{(D-1)}(\vec p-\vec p')` | after `T000133` `[00:38:22.140,00:38:51.890)` | `F04:L40` | states; **PRINTED NORMALIZATION:** unit delta coefficient, with no extra factor |
| `L189-L194` gray `\braket{\vec p}{\vec p'}=\delta^{(D-1)}(\vec p-\vec p')` | after `T000139` `[00:39:40.760,00:39:53.930)`, before `T000141` | `F04:L48-L56` | derives in `T000135-T000139`; **PRINTED NORMALIZATION:** delta only; gray ink retained |
| `L196-L201` Hamiltonian integral with `a_{\vec p}^{+}a_{\vec p}` | after `T000159` `[00:43:21.319,00:43:48.530)` | `F04:L97`; occupation label at `F04:L101` | states; **PRINTED NORMALIZATION:** measure is exactly `d^{D-1}\vec p`, with no added `(2\pi)` or `2\omega` factor |
| `L202-L206` free-relativistic-particle statement and blue checkmark | after `T000170` `[00:45:07.500,00:45:31.800)` | `F05`, after record | statement states; checkmark points silently |
| `L208` interacting-particles question | after `T000174` `[00:45:34.440,00:46:08.030)` | `F05`, after record | states |
| `L209-L220` `H=H_0+H_{\mathrm{int}}` with literal `a^{+}a^{+}a,\;aaa^{+},\;\ldots` and blue brace | after `T000178` `[00:46:31.380,00:47:15.170)` | source keys `F05:L26-L27`; render after `T000178` | derives the particle-number change; retain every `a^+` and the blue brace |
| `L221-L222` difficulty preserving relativistic symmetry | after `T000182` `[00:47:23.040,00:48:05.390)` | `F05`, after record | states |

## Original note p. 5, physical PDF p. 10

| Exact source unit | Canonical insertion point | Fragment marker | Action |
|---|---|---|---|
| `notes-exact.tex:L227` `Issue: \qquad Causality` | after `T000184` `[00:48:05.400,00:48:21.000)` | `F05`, before `T000185` | states |
| `L229-L253` complete spacetime/lightcone TikZ figure | after `T000189` `[00:49:57.900,00:50:23.890)` and before `T000191` `[00:50:23.900,00:51:05.270)` | `F05:L47-L48` is the asset manifest; render at the completed-figure point after `T000189` | derives during `T000185-T000189`; axes, rays, colors, arrowheads, and label are stated or pointed to. This is figure placement 2 |
| `L255-L257` generic-QM instantaneous propagation | after `T000191` `[00:50:23.900,00:51:05.270)` | `F05`, after record | states |
| `L260-L261` relativistic local disturbance | after `T000195` `[00:51:19.319,00:52:17.630)` | `F05`, after record | states |
| `L262-L283` annotated field-operator display, `\phi(x)`, blue arrows, and `x^\mu=(x^0,\vec x)` parameter note | after `T000200` `[00:53:15.000,00:53:39.470)` | source key `F05:L83`; render after `T000200` | states in `T000197-T000200`; arrows and underlines point silently |
| `L285-L286` `\hat\phi(x)` and `\hat\phi(x')` related by Poincare symmetry | after `T000209` `[00:55:00.000,00:55:20.000)` | `F06`, after `T000209` | states across the `F05/F06` seam |

## Original note p. 6, physical PDF p. 11

| Exact source unit | Canonical insertion point | Fragment marker | Action |
|---|---|---|---|
| `notes-exact.tex:L291-L306` coordinate map and Lorentz-metric annotation, including `\eta^{\mu\nu}=\operatorname{diag}(-1,1,1,1)` | during silent `T000213` `[00:56:20.000,00:56:40.000)`, before `T000214` | `F06:L16-L28` | coordinate map states in `T000210-T000212`; displayed metric condition points silently; mostly-plus signature states in `T000214` |
| `L308-L309` unitary representation `U(\Lambda,a)` | after `T000218` `[00:58:00.000,00:58:20.000)` | `F06`, before `T000219` | states |
| `L310-L313` `\hat\phi(\Lambda x+a)=U(\Lambda,a)\hat\phi(x)(U(\Lambda,a))^{-1}` | after `T000221` `[00:59:00.000,00:59:20.000)` and before `T000222` | `F06:L48-L52` | derives the conjugation rule in `T000219-T000223` |
| `L315-L332` infinitesimal heading, `\Lambda=\delta+\omega`, `a=\epsilon`, blue first-order note and arrows | after `T000230` `[01:02:00.000,01:02:20.000)` | `F06:L80-L90` | states; first-order expansion is used to derive antisymmetry in `T000231-T000232`; blue arrows point silently |
| `L334-L353` full `U(\Lambda,a)=1-i\epsilon^\mu\hat P_\mu+\frac{i}{2}\omega_{\mu\nu}\hat J^{\mu\nu}` generator display and blue labels | after `T000244` `[01:06:24.359,01:06:38.400)` and before `T000245` | `F06:L106-L111` is the formula asset marker; final labeled display belongs in `F07` after `T000244` | states in `T000234-T000237` and names the generators in `T000243-T000244`; printed factor `1/2` retained |
| `L355-L360` faint-gray Poincare group law | after `T000250` `[01:08:18.960,01:08:28.920)` | use `F07:L50`; `F06:L117` is the earlier cross-lane asset marker | derives by composing the two transformations |
| `L361-L367` faint-gray `[P,P]=0` and `[P^\mu,J^{\rho\sigma}]` | after `T000251` `[01:08:28.920,01:08:47.880)` | `F07:L57` | points silently; Yin assigns the derivation to the listener |
| `L368-L374` faint-gray `[J^{\mu\nu},J^{\rho\sigma}]` | immediately after the preceding algebra block, still after `T000251` | `F07:L57` | points silently; preserve faint gray and literal antisymmetrization shorthand |

## Original note p. 7, physical PDF p. 12

| Exact source unit | Canonical insertion point | Fragment marker | Action |
|---|---|---|---|
| `notes-exact.tex:L379-L388` microcausality commutator and spacelike qualification | after `T000266` `[01:12:25.380,01:12:38.480)` | `F07:L117` as part of its combined marker | states |
| `L389-L395` mostly-plus interval and `>0` | after `T000268` `[01:12:57.900,01:13:08.699)` | `F07:L117` | derives the spacelike criterion |
| `L397-L398` free-relativistic-particle question | after `T000276` `[01:14:27.659,01:14:44.760)` | `F07`, before `T000277` | states |
| `L399-L403` free Hamiltonian with `a_{\vec p}^{+}a_{\vec p}` | after `T000277` `[01:14:44.760,01:15:00.000)` | `F07:L151` | states; **PRINTED NORMALIZATION:** exact measure `d^{D-1}\vec p`; retain `a^+` |
| `L404-L407` `\vec P=\int d^{D-1}\vec p\,\vec p\,a_{\vec p}^{+}a_{\vec p}` | immediately before `T000279` `[01:15:00.540,01:15:19.970)` | `F08:L7` | states while pointing; **SOURCE/BOARD DISTINCTION:** printed `\vec P` has no hat, while speech and board use `\widehat{\vec P}`; retain printed form and `a^+` |
| `L408-L410` `\hat P^\mu=(H,\vec P)` | immediately before `T000281` `[01:15:19.980,01:15:43.550)` | `F08:L13` | states while pointing; **SOURCE/BOARD DISTINCTION:** printed components are exactly `(H,\vec P)` |
| `L412` existence question and `Yes!` | after `T000291` `[01:16:42.120,01:16:51.900)` | `F08`, before silent `T000292` | states; the written answer lands during `T000292` |
| `L413-L426` free scalar field integral | after `T000295` `[01:17:04.560,01:17:19.689)`, immediately before `T000297` | `F08:L55` | states in `T000297`; **PRINTED NORMALIZATION:** denominator is exactly `\sqrt{(2\pi)^{D-1}2\omega_{\vec p}}`; retain literal `a_{\vec p}^{+}` and both phases |

## Original note p. 8, physical PDF p. 13

| Exact source unit | Canonical insertion point | Fragment marker | Action |
|---|---|---|---|
| `notes-exact.tex:L431-L443` blue annotated definitions `p\cdot x\equiv\vec p\cdot\vec x-\omega_{\vec p}x^0` and `\omega_{\vec p}\equiv\sqrt{\vec p^{\,2}+m^2}` | after the p.7 field display and before `T000297` `[01:17:19.699,01:17:42.360)` | `F08:L56`, immediately after the `F08:L55` field display | omega states in `T000295`; phase states in `T000297`; opening curve and arrows point silently |
| `L445-L451` first microcausality commutator integral | after `T000303` `[01:18:19.080,01:18:35.390)` | rehome `F08:L73` into the notes-only packet after `T000303` | points silently; **PRINTED NORMALIZATION:** exactly `(2\pi)^{D-1}2\omega_{\vec p}` in the denominator and the centered multiplication dot |
| `L452-L463` covariant mass-shell rewrite with two blue underbraces | immediately after the preceding integral | same notes-only packet | points silently; **PRINTED NORMALIZATION:** preserve literal `\frac{d^D p^\mu}{(2\pi)^{D-1}}\theta(p^0)\delta(p^2+m^2)`; keep `d^D p^\mu` unchanged |
| `L464-L466` blue result: function of `(x-y)^2` only | immediately after the covariant rewrite | same notes-only packet | points silently |
| `L468-L469` spacelike WLOG frame with equal times | immediately after the invariant-function line | same notes-only packet | points silently |
| `L470-L473` odd-integrand argument and vanishing commutator with blue checkmark | immediately after the WLOG lines, before the p.9 covariance check | same notes-only packet | points silently; the complete derivation is notes-only, as forecast by `T000301` `[01:18:04.739,01:18:19.070)` |

## Original note p. 9, physical PDF p. 14

| Exact source unit | Canonical insertion point | Fragment marker | Action |
|---|---|---|---|
| `notes-exact.tex:L478-L482` scalar-field Poincare covariance equation | after the p.8 notes-only proof, still after `T000303` and before `T000305` `[01:18:35.400,01:18:44.000)` | rehome `F08:L72` after the p.8 packet | states as a claim in `T000303`; displayed verification points silently |
| `L484-L491` terminal horizontal arrow and two quote-like marks | immediately after the covariance equation | `F08`, before the postulate block | points silently; preserve as graphics without assigning prose meaning |
| `L493-L500` postulate heading and exact list: Hilbert space, Poincare symmetry, invariant vacuum, local field operators, covariance, microcausality | during/after silent `T000305` `[01:18:35.400,01:18:44.000)`, before `T000306` | `F08`, before `T000306` | points silently; this compact list is notes-only |
| `L502-L503` properties hold for interacting relativistic particles | immediately before `T000306` `[01:18:44.000,01:19:07.669)` | append to the postulate block | states in `T000306` |
| `L505-L508` construction question and formalism with manifest Poincare symmetry | after `T000310` `[01:19:26.460,01:19:47.090)` | `F08:L91`, before `T000312` | states across `T000306-T000310`; this is the Chapter 1 close |

## Integration order at the final cross-page seam

After `T000303`, preserve source order as one packet: p.8 commutator integral, covariant rewrite with literal `d^D p^\mu`, invariant-function statement, equal-time/oddness derivation, p.9 covariance equation, graphical divider. Place the postulate list in the `T000305` writing interval. Continue with `T000306-T000310`, then insert the closing construction/manifest-formalism lines. This keeps the notes-only derivation and list visible without attributing spoken words to Yin.
