# Pass 1 source capture: `vk_RlYUKUyM`

## Source identity

The recording is `GMT20220915 173014 Recording 640x360`, recorded on 2022-09-15 at 17:30:14 UTC. It is playlist position 10 in `work/pilot/playlist.jsonl`. The playlist metadata gives a duration of `01:23:27` and the URL `https://www.youtube.com/watch?v=vk_RlYUKUyM`.

The combined source is `/Users/wlancer/Desktop/IAS/phy/qft/qft_253abc_book.pdf`, physical pages 20-68 in this source packet. Its manifest SHA-256 is `9e5e4d241fffffa56c1c3df6dce4b83178f75787dd5d794a18c5d0c087769f21`. The rendered files `tmp/pdfs/253a-ch02-source/page-020.png` through `page-068.png` were inspected through the complete contact-sheet set. Pages 037-048 were inspected individually for this video span.

Caption inputs:

`work/253a-ch02/captions/20230504-vk_RlYUKUyM.en.json3`

SHA-256: `0b1a086f5babdf7e78c0bba97f00a61909231341106549195d256c30be9500b0`

`work/253a-ch02/captions/20230504-vk_RlYUKUyM.en.vtt`

SHA-256: `435d8b50e283ed3a2382a8066babac9f187a96ce8dfa527c14282c68afed913c`

The JSON3 file has 2,912 events, with one metadata event and 2,911 timed events. The VTT file has 2,911 cues. Their cue starts agree at every position. The JSON3 text contains 8,862 word-bearing ASR segments, including six `[Music]` events. The inventory below collapses rolling-caption repetition at the inventory level. Raw words remain in the order supplied by JSON3 and VTT. Equations are copied from the rendered notes when the caption track supplies only an equation recognition error.

## Exact boundaries

The first timed caption is `00:00:03.020-00:00:06.140`, raw text `thank you`. A 6.520 second gap follows. The first substantive Chapter 2 speech begins at `00:00:12.660`, raw text `um where we were again the last lecture`.

The final recoverable Chapter 2 content is the small-coupling qualification ending at the spoken event `01:20:16.460`, raw caption `explanation of that`. The rolling cue remains on screen through `01:20:36.790`; `01:20:36.800-01:20:40.040` carries `all right` as a classroom closure. A candidate room Q&A resumes at `01:21:38.460` with `absolutely` and `yeah`, ending at `01:21:42.260`. The later `right now`, `oh`, music, `differences`, and `I realize` fragments belong to the post-lecture tail.

Boundary dispositions:

`00:00:03.020-00:00:06.140`: opening acknowledgement, retained as logistics.

`00:00:12.660-01:20:16.460`: Chapter 2 lecture content, physical pages 37-48, with a short spoken revisit of material on physical pages 26-29.

`01:20:16.460-01:20:40.040`: explanation tail and classroom closure, retained as the end of the lecture interval.

`01:20:40.040-01:21:42.260`: candidate Q&A or room conversation. Its surviving captions are too sparse for a source-resolved claim. Keep the raw interval and mark its relation to Chapter 2 as provisional.

`01:21:42.260-01:23:28.159`: outside the source-resolved lecture. The caption track carries isolated post-class fragments and music.

## Chronological lecture order

Playlist order is a metadata order rather than recording-date order. The relevant 253a recordings sort as follows:

| Recording date | Playlist position | Video | Source-order role |
|---|---:|---|---|
| 2022-09-06 | 3 | `96lN2omwit4` | Lagrangian formalism begins after the Chapter 1 boundary. |
| 2022-09-08 | 9 | `uzixOflp0tY` | Lagrangian and path-integral continuation. |
| 2022-09-13 | 4 | `M0py5a4RWhE` | Gaussian functional-integral derivation reaches the operator and inverse kernel. |
| 2022-09-15 | 10 | `vk_RlYUKUyM` | Gaussian recap, anharmonic oscillator denominator, connected graphs, ground-state energy. |
| 2022-09-20 | 1 | `3VG2kDHso08` | Continues with the two-point numerator after Chapter 2 page 48. |
| 2022-09-22 | 6 | `TtMNnZ8__UU` | Later Chapter 2 material. |
| 2022-09-27 | 2 | `82__84nYd4I` | Later Chapter 2 material. |
| 2022-09-29 | 8 | `ph3wE8cFMmk` | Later Chapter 2 material and approach to the assignment boundary. |

## Topic-to-note-page alignment

Physical page numbers below refer to the rendered source packet. The parenthetical page is the corresponding handwritten lecture-note page in the `253a/lecture_notes.pdf` numbering shown on the chapter divider. Physical page 21 maps to lecture-note page 10, so physical page 37 maps to lecture-note page 26.

| Video interval | Physical pages | Lecture-note pages | Source material |
|---|---:|---:|---|
| `00:00:12.660-00:03:31.519` | 37, 39 | 26, 28 | Gaussian functional integral recap, inverse operator, Green function, Fourier representation. |
| `00:03:38.819-00:14:07.439` | 37-40, with a spoken cross-reference to 26-29 | 26-29 | Physical origin of the Gaussian expression, real-time and imaginary-time objects, spectral exponential, operator-order qualification. |
| `00:14:13.220-00:21:06.199` | 41 | 30 | Example 2, anharmonic oscillator, Euclidean action, spectral use of the two-point function, ground-state and excited-state overlaps. |
| `00:21:12.360-00:24:50.179` | 42 | 31 | Partition function denominator, expansion in `g`, free Wick contractions, interchange-of-sum-and-integral qualification. |
| `00:25:03.380-00:31:00.719` | 42 | 31 | `Z_g/Z_0`, Gaussian expectation values, integration variables, denominator normalization. |
| `00:31:00.720-00:43:57.779` | 42-43 | 31-32 | Order-by-order terms, quartic vertices, Wick pairings, connected and disconnected order-`g^2` graphs. |
| `00:44:31.160-01:07:07.798` | 44-45 | 33-34 | Connected-graph combinatorics, component counts `m_l`, symmetry factors, exponentiation. |
| `01:07:07.799-01:12:38.459` | 46-47 | 35-36 | Matrix-element interpretation of `Z`, ground-state projection, `log Z`, energy extraction, connected-graph sum. |
| `01:12:38.460-01:17:27.419` | 47-48 | 36-37 | First-order ground-state energy correction, Hamiltonian perturbation comparison, linear-divergence discussion. |
| `01:17:56.880-01:20:16.460` | 48 plus oral qualification | 37 plus oral qualification | Inaccessible-information remark, next-numerator preview, zero-radius-convergence qualification, small-`g` numerical remark. |

Physical page 20 is the Chapter 2 divider. Physical pages 49-62 continue the chapter after this recording. Physical pages 63-67 are Problem Set 2. Physical page 68 is the divider for Chapter 3, `Relativistic Particles, Fields, and Green Functions`.

## Equation reference layer

The caption track often renders mathematical speech as words such as `foreign`, `detailed Prime`, `Omega Square`, `permanent function`, or `kinetic graphs`. The following equation references come from the page images and retain note notation.

At `00:00:12.660-00:03:31.519`, page 37 supplies the functional replacement and Green-function setup:

`\vec q \rightsquigarrow g(\tau) \in \text{linear space of real functions}`

`\vec q\cdot\vec J \rightsquigarrow \int d\tau\,g(\tau)J(\tau)`

`A\cdot g(\tau):=(-\partial_\tau^2+\omega^2)g(\tau)`

`A^{-1}\cdot g(\tau)=\int d\tau'\,G(\tau,\tau')g(\tau')`

`(-\partial_\tau^2+\omega^2)G(\tau,\tau')=\delta(\tau-\tau')`

At `00:03:38.819-00:07:04.559`, the board discussion returns to the normalized two-point functional integral and its matrix-element origin. Page 37 visibly uses `Dg` in the numerator and `Dx` in the denominator. This page-local measure mismatch is retained as a source ambiguity.

At `00:08:21.840-00:13:59.339`, the spoken spectral discussion points back to the real-time and Wick-rotated expressions on pages 26-29. The source result repeated in the lecture is `G(\tau)=\frac{1}{2\omega}e^{-\omega|\tau|}` after the contour evaluation.

At `00:14:13.220-00:16:52.519`, page 41 introduces:

`H=\frac{p^2}{2}+\frac{q^2}{2}+\frac{g}{4!}q^4`

`L=\frac{1}{2}\dot q^2-\frac{q^2}{2}-\frac{g}{4!}q^4`

`L^E=\frac{1}{2}(\partial_\tau q)^2+\frac{q^2}{2}+\frac{g}{4!}q^4`

At `00:17:05.400-00:21:06.199`, page 41 gives the Euclidean two-point ratio and `Z=\int[Dq]e^{-\int d\tau L^E}`. The spectral expression for `\tau>0` is written as a sum of `|\langle n|\hat q(0)|0\rangle|^2 e^{-E_n\tau}`.

At `00:21:12.360-00:24:50.179`, page 42 gives the denominator expansion:

`Z=\int[Dq]e^{-\int d\tau(\frac12(\partial_\tau q)^2+\frac12q^2)}\sum_{n=0}^{\infty}\frac{1}{n!}(-\frac{g}{4!}\int d\tau' q^4(\tau'))^n`

`\frac{Z_g}{Z_0}=\sum_{n=0}^{\infty}\frac{1}{n!}(-\frac{g}{4!})^n\int d\tau_1\cdots d\tau_n\langle(q(\tau_1))^4\cdots(q(\tau_n))^4\rangle_0`

At `00:31:00.720-00:39:01.078`, pages 42-43 give the order-`g` term and its three pairings:

`-\frac{g}{4!}\int d\tau\,\langle(q(\tau))^4\rangle_0=-\frac{g}{8}\int d\tau\,(G_0(\tau,\tau))^2`

At `00:41:02.720-00:43:57.779`, page 43 gives the order-`g^2` term:

`\frac12(-\frac{g}{4!})^2\int d\tau_1d\tau_2\langle(q(\tau_1))^4(q(\tau_2))^4\rangle_0`

The board draws disconnected pairings and connected pairings. Each quartic insertion is drawn as a vertex with four legs, and each Wick contraction is drawn as a line carrying `G_0`.

At `00:44:31.160-01:07:07.798`, pages 44-45 give the connected-component count:

`\sum_{\ell\ge1}m_\ell=K`, `\sum_{\ell\ge1}m_\ell\ell=n`

`\frac{n!}{\prod_{\ell\ge1}(\ell!)^{m_\ell}m_\ell!}`

`\frac{Z_g}{Z_0}=\sum_{\{m_\ell\}}\prod_{\ell\ge1}\frac{1}{m_\ell!}(\frac{1}{\ell!}G^{(\ell)})^{m_\ell}=\exp(\sum_{\ell\ge1}\frac{1}{\ell!}G^{(\ell)})`

Here `G^{(\ell)}` is the contribution from connected Wick contractions of `\ell` quartic vertices. Page 45 gives the three-vertex connected example and records that the corresponding integral still diverges like `\int d\tau\,(\mathrm{const.})`.

At `01:07:07.799-01:12:38.459`, page 46 supplies:

`Z=\int[Dq]e^{-\int d\tau L^E}=\langle q_f|e^{-HT}|q_i\rangle`

`\log Z=-E_0T+O(1)`

`\log\frac{Z_g}{Z_0}=\sum_{\ell=1}^{\infty}\frac{1}{\ell!}G^{(\ell)}`

The boundary values of the imaginary-time path are left unspecified as `T\to\infty`; their role is ground-state projection.

At `01:12:38.460-01:15:03.299`, page 47 gives:

`G^{(1)}=3\,(-\frac{g}{4!})\int d\tau\,(G_0(\tau,\tau))^2=-\frac{g}{8}\int d\tau\,(G_0(\tau,\tau))^2`

`\Delta E_0=\frac{g}{8}(\frac{1}{2\omega})^2+O(g^2)`

The page annotation says `G_0(\tau_1,\tau_2)=\frac{1}{2\omega}e^{-\omega|\tau_1-\tau_2|}` and `G_0(\tau,\tau)=\frac{1}{2\omega}`. The note has set `\omega=1` in the displayed numerical comparison.

At `01:15:03.300-01:17:27.419`, page 48 compares Hamiltonian perturbation theory:

`H=\underbrace{\frac{\hat p^2}{2}+\frac{\hat q^2}{2}}_{H_0}+\underbrace{\frac{g}{4!}\hat q^4}_{H_1}`

`\Delta E_0\simeq\langle\psi_0|H_1|\psi_0\rangle=\frac{g}{4!}\langle\hat q^4\rangle_0=\frac{g}{32}`

The source-page comparison uses `\langle\hat q^4\rangle_0=3/4` after setting `\omega=1`.

## Continuous timestamped inventory

### `00:00:00.000-00:03:31.519` | opening and Gaussian recap | pages 37 and 39

`00:00:00.000-00:00:03.019`: room silence before the first caption. `00:00:03.020-00:00:06.140`: raw `thank you`. `00:00:06.140-00:00:12.660`: silence or room transition.

At `00:00:12.660`, raw: `um where we were again the last lecture`. Yin recaps a Gaussian-type functional integral, the general action form, the differential operator `A`, and the inverse object `G`. Raw caption fragments include `the main result would be right`, `this thing is equal`, and `G ... is ... the inverse of the operative a`. The caption phrase `so foreign` begins at `00:00:46.079`; it is an ASR failure around the operator discussion. The board source resolves `G` through the page-37 Green-function equation.

At `00:01:26.939`, raw: `uh and the main result would be right`. At `00:01:57.000`, raw: `for example uh it follows that the gene`. At `00:02:13.739`, he says he will carry the calculation one more step. At `00:02:38.580`, raw: `D is equal to integral ... over 2i` and the caption gives a damaged version of the Fourier kernel. The rendered page resolves the expression as the `k` integral with denominator `k^2+\omega^2`.

At `00:03:00.660-00:03:09.420`, raw: `you just pull down a k square plus Omega Square ... and the integral is just ...`. This is the verification that the differential operator acting on the Fourier integral produces the delta function. At `00:03:26.099`, raw `all right ... any questions about this so far`, followed by a board transition.

### `00:03:31.520-00:08:21.839` | physical interpretation, time variables, and board interval | pages 37-40, spoken recap of pages 26-29

`00:03:31.520-00:03:38.818` is a pause after `any questions about this so far`. At `00:03:38.819`, raw: `now let me just make a comment about this expression`. Yin distinguishes the Gaussian functional average from the physical matrix-element interpretation. Raw at `00:04:45.440`: `I hope you remember the physical origin of this ... some kind of statistical average ... this came from ... actual Matrix elements`. The words around `analyticulation` and `actual Matrix elements` are recognition errors.

At `00:05:55.340`, raw: `you missed that from our previous discussion okay so`. The captions then discuss the derivation of the matrix element, the convention for `q`, and the Wick-rotated time variable. At `00:06:24.919`, raw: `the way we derived this last time`. At `00:06:31.800`, raw: `in order to write this as a matrix elements`. Formula words around `anti Convention`, `time tab`, and `power too fantasy` are uncertain speech for operator ordering and imaginary time.

`00:07:04.560-00:07:20.159` contains damaged transition speech, including two `[ASR: foreign]` fragments. `00:07:20.160-00:07:43.569` is a board or room interval. JSON3 marks `[Music]` at `00:07:43.570-00:07:46.639`. A further quiet interval runs to `00:08:21.840`.

### `00:08:21.840-00:14:07.439` | real-time and imaginary-time objects, spectral content | pages 26-29 as a spoken cross-reference, pages 37-40 as the current board context

At `00:08:21.840`, raw: `and this is going to diverge exponentially`. Yin explains the convergence restriction after Wick rotation and the way the path-integral expression relates to a matrix element. Raw at `00:08:30.479`: `this right hand side would only be well defined`; raw at `00:08:40.440`: `generally you should understand this way`.

At `00:09:42.180`, raw: `the real time`. He marks the notation distinction between real time and imaginary time. Raw at `00:09:50.640`: `whenever I write ... it's real time ... it's the imaginary ... time`. The caption renders the equation words as `i h e u h` and `minus five`; the note pages supply the time-evolution and Wick-rotation expressions.

At `00:10:01.920-00:11:24.680`, Yin says that real-time quantum-mechanical matrix elements are well defined, while the related Euclidean objects require care. Raw: `these two lines often is not compute General`, `if you find this confusing ... always go back to the definition`, and `we have to be a little careful of the different objects`. These are direct oral qualifications. A long board interval occurs before `00:11:34.459`.

At `00:11:34.459`, raw: `the one we should look at ... there are Matrix elements ... evolved in real time ... and then there are ... computed from ... the pathway ... they're closely related but they're not exactly`. The final clause is caption-incomplete. At `00:11:42.600`, a question or response begins with `there's another thing`; at `00:11:47.600`, raw: `let's post on that discussion`. At `00:12:39.300`, Yin asks `any other questions about this`.

At `00:13:01.019`, raw: `make the additional remark that this quantity here ... this is actually using the ... formula`. The note-level result is the residue integral `1/(2\omega)e^{-\omega|\tau|}`. At `00:13:28.500`, he identifies `\omega` with the energy difference `E_1-E_0` in the single-exponential case. At `00:13:44.880`, raw: `if ... overlaps with the other excited states you have the sum of a bunch of exponential`. He names the spectral decomposition at `00:13:55.500`, with caption text `special decomposition`.

### `00:14:07.440-00:21:06.199` | Example 2 and the anharmonic oscillator | page 41

At `00:14:13.220`, Yin announces `example example two`. Raw at `00:14:19.079`: `the second example ... the N Harmony`; at `00:14:32.839`: `is not harmonic`. The intended heading on page 41 is `Example 2 "an harmonic oscillator"`, with the Hamiltonian containing the quartic coupling. The caption's `N Harmony`, `anthematic`, and `harmonic acid` readings are ASR errors.

At `00:14:43.980`, he sets `\omega=1` for the discussion. At `00:15:01.380-00:15:24.959`, raw: `Hamiltonian P Squared ... plus Q Square over two ... add a quartic potential ... Q to the fourth ... normalize ... G over four factorial ... coupling constants`. The page supplies `H=p^2/2+q^2/2+gq^4/4!` and `L=\dot q^2/2-q^2/2-gq^4/4!`.

At `00:15:37.800`, he situates the example in ordinary quantum mechanics and says the energy levels can be obtained from the Schrodinger equation. Raw: `you can solve the energy levels ... by ... equation ... normalizable`. He then returns to the path integral. At `00:16:16.019`, raw: `now again we're going to study this using the path integral`. At `00:16:22.680`, he writes the Lagrangian; at `00:16:35.699`, he says `week rotated`, an ASR rendering of Wick rotation. The Euclidean Lagrangian is the page-41 expression.

`00:16:52.520-00:17:05.399` is a question interval followed by a board transition. At `00:17:05.400`, raw: `any question about the system ... we are considering`. Yin says the two-point function can be computed by the same path-integral method. Raw at `00:17:31.260`: `starting the pattern go exactly the same`. He erases and recycles the board. The captions contain `I'm gonna erase`, `everything on this board ... still holds`, and a long `[ASR: foreign]` segment.

At `00:18:12.480`, raw: `if you are actually able to calculate ... this two point expression value ... read out information about the energy spectrum`. At `00:18:24.780`, he asks for the energy eigenvalue in terms of `g`. This is a live question interval. At `00:18:49.860`, raw: `the potential is like this`; at `00:19:04.460`, raw: `the potential ... looks like this`. The board draws the quartic potential and energy levels.

At `00:19:18.679`, raw: `the good news is ... perturbation Theory values ... it doesn't converge`. The caption renders `perturbation Theory` as `provision Theory` in the surrounding span. Yin says the Hamiltonian method is available, while the lecture will use the Lagrangian version. At `00:19:48.380`, raw: `if you know the exact answer to this two-point query function ... a sequence of exponential`. At `00:20:05.100`, he says the anharmonic oscillator has overlap with the first excited state and an infinite tower of further excited states.

### `00:21:06.200-00:25:03.379` | denominator, expansion in `g`, and the convergence qualification | page 42

`00:21:06.200-00:21:12.359` is a board interval. At `00:21:12.360`, Yin introduces the denominator, calls it `Z`, and notes an ambiguous normalization. Raw: `certainly speaking ... ambiguous normalization`, `whatever ambiguity there is ... gonna cancel out in the final answer`, and `not enough worry too much about the ambiguity in doing this stage of computation`.

At `00:21:48.000-00:22:19.919`, he separates the harmonic action from the quartic term. The caption gives `G over 400 ... to the fourth`; page 42 resolves `g/4!` and `q^4`. At `00:22:27.059`, raw: `the only thing ... is to just expand exponential`. He writes the sum over `n` with `1/n!` and `(-g/4!)^n`.

At `00:23:01.020`, raw: `if you assume that you can't exchange the order on functional integral with the sum over little n`. He explains that every coefficient is a Gaussian expectation of quartic insertions and invokes the Wick contraction rule from the previous lecture. Raw at `00:23:29.400`: `we knew how to do this last time`; raw at `00:23:45.720`: `any questions so far`.

At `00:23:48.780-00:24:50.179`, he qualifies the formal manipulation. Raw: `you cannot quite do that`, `the sum actually will not actually converge`, and `we'll have zero radius converters in G`. The source-resolved claim is that the perturbative series generally has zero radius of convergence while still furnishing the formal expansion used in the calculation. The caption renders `convergence` as `converters` and gives several clipped restarts.

`00:24:50.180-00:25:03.379` is a room or board interval. At `00:25:03.380`, Yin says the issue can be partially cured later and proceeds with the formal expansion.

### `00:25:03.380-00:31:00.719` | `Z_g/Z_0`, Gaussian averages, and normalization questions | page 42

At `00:25:03.380-00:25:58.260`, Yin defines `Z_g`, compares it with `Z_0`, and identifies the ratio as a Gaussian expectation. Raw: `if I compare this ... at zero coupling ... harmonic oscillator`, followed by `then ... equal to the expression value`. The caption repeatedly renders `partition function` as `primary function`, `party function`, or `permanent function`.

At `00:26:40.020`, the caption gives the insertion sequence as `Q of Tau one ... Q of Tau n`. Yin explains that the integration variables are separately named `\tau_1,\ldots,\tau_n`. At `00:27:01.799`, raw: `I'm just writing this out ... I have this integral to n power ... change in my variable ... renaming the variable`.

At `00:27:29.340`, he explicitly acknowledges the hidden exchange of the sum and the functional integral. Raw: `I have secretly exchanged the song with the integral`, followed by `these things are actually more subtle than you might have thought`. The words `song` and `management` are caption errors around `sum` and the formal continuation. He proceeds under the stated assumption.

At `00:28:34.340`, a student asks how the integral can be pulled out as a factor. Raw: `how are we able to write ... as a factor`. Yin answers that the `\tau_i` are independent integration variables and that the bracket denotes the Gaussian expectation for those variables. At `00:29:23.520`, raw: `why am I allowed to pull this integral outside of the expression value`; at `00:29:31.500`, he answers `I can because ... by definition this is just a sum of different variables`.

At `00:29:41.640`, the question continues about the definition of the expectation. Raw at `00:29:48.200`: `yes that is by definition`. At `00:29:58.460-00:30:11.039`, he writes the integral over `q(\tau_1)^4 ... q(\tau_n)^4`. `00:30:11.039-00:30:40.019` is a board interval with low-confidence captions.

At `00:30:47.580`, raw: `we just ... learned from the last lecture ... Wick contractions`. He begins the order-by-order evaluation of the denominator.

### `00:31:00.720-00:34:00.000` | order-by-order expansion and quartic vertex | pages 42-43

At `00:31:00.720`, Yin says he will move through the expansion by order. Raw: `at the living water is this one ... term angle angle zero`, an ASR-damaged version of the `n=0` term. At `00:31:27.740`, the caption recovers `minus G over four factorial`; the note equation is the order-`g` integral. At `00:31:48.960`, he writes the order-`g^2` coefficient `1/2(-g/4!)^2` with two time integrations.

At `00:32:14.580`, he recalls the Wick rule using four variables. Raw: `last time I wrote this I wrote u n q m q r q s`. The page-36 and page-42 source notation resolves this as a four-field Gaussian expectation with all distinct pairings. At `00:32:35.039`, raw: `the Wick contraction tells us`. A gap runs from `00:32:44.299` to `00:32:58.640` while the board is updated.

At `00:32:58.640`, Yin introduces a diagram for each quartic insertion. Raw: `every time I put down a ... G I get the insertion of four q's`, with `G` in this span an ASR error for `g`. At `00:33:20.279`, he draws a vertex and says the coefficient is `minus g over four factorial`. Each line leaving the vertex represents a `q` insertion.

At `00:34:00.000-00:34:36.839`, he says the four lines meet at one Euclidean time and that a Wick contraction ties lines together with the Green function. Raw: `all the cues are at the same value of euclidean time`; the caption's `white lines`, `bird boxes`, and `Galaxy integral` are recognition failures. At `00:34:39.179`, he states that there are three distinct ways to contract the four legs.

### `00:34:00.000-00:41:02.719` | three pairings, order `g`, and the first divergence | pages 42-43

At `00:35:01.859`, Yin draws the remaining contraction and says the three diagrams are identical. Raw: `they are actually all identical so you have three copies`. At `00:35:33.000`, he identifies the purple line as `G` between Euclidean times. The caption renders `q(\tau)` as `cute Tau` and the Green function as `G of power and how two`; the page diagrams settle the line meaning.

At `00:36:33.599`, a question asks how the contraction relates to the earlier finite-dimensional matrix calculation. Raw: `when we didn't work with children now the contraction ... e to the q some Matrix`; Yin answers by pointing back to the inverse matrix and the Gaussian result. At `00:37:36.980`, another low-confidence span begins `speak of this Matrix`; at `00:37:53.339`, he says `convince yourself`. This is a Q&A and board interval around the contraction rule.

At `00:38:00.480`, Yin assembles the order-`g` contribution. Raw: `the order G term ... is just ... minus G over 34 times 3`; the caption has `34` for `4!` and `G` for `g`. The page-43 equation resolves the coefficient to `-g/8`.

At `00:39:01.079`, raw: `this appears to be Divergent because you're integrating ... in Tau`. Yin says the divergence will be interpreted and handled later, then says `it's a feature another bug` at `00:39:36.660-00:39:43.700`. This phrase is a recoverable joke or informal qualification. A student asks what is being integrated at `00:39:43.700`; the response distinguishes the quartic interaction insertion from the time integration.

At `00:40:00.480`, raw: `in action there was no difference ... they're all just power`; the word `County` at `00:40:02.280` is an ASR error. At `00:40:32.040`, a question asks how the time variable is treated. Raw: `a towel is a ... like an index`; the likely source meaning is that `\tau` labels the integration variable. Yin closes with `we'll revisit this Divergence later` at `00:40:51.720`.

### `00:41:02.720-00:44:31.159` | order `g^2` Wick contractions | page 43

At `00:41:02.720`, Yin writes the order-`g^2` term with `\tau_1` and `\tau_2`, each carrying a quartic insertion. Raw: `minus G over four factorial squared ... q a one to the fourth ... q now two to the fourth`. He turns the expression into a diagram.

At `00:41:45.200`, he invokes the Wick rule. At `00:42:09.780`, raw: `sum over all the possible weak contractions of the eight cubes`; `weak contractions` and `cubes` are ASR readings of Wick contractions and `q` fields. He draws several possible pairings and says the diagrams must be added.

At `00:43:01.319`, he explains that each line is a `G(\tau_i,\tau_j)` factor and that the numerical coefficients multiply with the Green-function factors. Raw: `this is G Taiwan ... this is g l one l two ... just multiply this together and multiply the coefficients`. The page resolves the time labels and product structure.

At `00:43:27.660`, raw: `I have the integrator which is Divergence but don't worry about that`. The class asks a follow-up at `00:43:39.300`; `00:43:57.780-00:44:31.159` is a long board or room interval. The final caption before the gap is `foreign`.

### `00:44:31.160-00:47:01.499` | connected and disconnected graphs | pages 43-45

At `00:44:31.160`, Yin returns to the finite integration range and normalization. Raw: `function would only be well defined if you do this integration in finite range`. He says the normalization drops out in a ratio and mentions a homework problem with a related normalization issue. The word `bonification` is an ASR error for normalization.

At `00:45:12.660`, he says the diagram organization will clarify the physical interpretation. At `00:45:34.800`, he distinguishes connected graphs from disconnected graphs. Raw: `some of them ... these are connected graphs ... these graphs are disconnected`; at `00:45:52.140`, he explains that a disconnected graph is a product of connected graph contributions.

At `00:46:06.060`, Yin says the partition function can be expressed using connected graphs. Raw: `trying to express this whole party function in terms of just the connected graphs`. At `00:46:28.140`, he generalizes to order `g^n` and says every set of Wick contractions is represented by a graph. The caption renders `Wick interactions` as `weak interactions`.

### `00:47:01.500-00:50:02.219` | connected components and the `m_l` labels | page 44

At `00:47:01.500`, Yin defines a graph with `K` connected components. Raw: `a bunch of these coordinate vertices ... connect the legs with the purple lines`. At `00:47:17.460`, he introduces `K connected components`; at `00:47:39.420`, he says that for each `l` there are `m_l` connected graphs containing `l` vertices.

The note equations are `\sum_{l\ge1}m_l=K` and `\sum_{l\ge1}m_l l=n`. A short `[Music]` marker appears at `00:47:26.900-00:47:31.560` while the component classification continues across the rolling captions.

At `00:48:01.020`, Yin draws a component with `l` vertices and another component. Raw: `the total member of this would be m_l minus one`; the word `member` is the caption's uncertain rendering of the component count. At `00:48:42.300`, he clarifies that the whole disconnected object is one graph for the purpose of the sum and asks about the total number of vertices.

At `00:49:29.940`, a student asks about `K` and `n`. Raw: `I don't understand the K is the sum of an L`; Yin answers with `K` as the sum of the `m_l` and `n` as the weighted sum. The exact formulas are supplied by page 44.

### `00:50:02.220-00:53:01.279` | grouping count and combinatorial weight | page 44

At `00:50:02.220`, Yin explains that the `n` vertices are grouped into subsets specified by the `m_l`. Raw: `I separate ... into subsets of groups of L ... specified by the MLS`. He asks for the number of ways to group the vertices in the specified pattern.

At `00:51:00.780`, he gives the count as `n!` divided by `\prod_{l\ge1}(l!)^{m_l}m_l!`. Raw: `number of ways of grouping the n vertices in this matter`. The caption renders `m_l` as `Alpha`, `meters`, and `film`; the page equation governs the symbols.

At `00:51:38.880`, he describes first choosing the groups and then accounting for their internal permutations. At `00:52:08.640`, he gives the example `m_1=1`, `m_2=0` in raw form. At `00:52:31.920`, he says the integers are arbitrary and must satisfy the vertex-count equation. The phrase `Ten Perfect` at `00:52:36.420` is an ASR error around the total count.

### `00:53:01.280-00:56:38.039` | connected-graph sum and symmetry factor | pages 44-45

At `00:53:01.280`, raw: `so what do we have in order to do to the n to the end order`. Yin collects the `1/n!` from the exponential, the grouping count, and the product over connected graph contributions. At `00:53:47.040`, he defines `G^{(l)}` as the sum of all connected graphs with `l` vertices.

At `00:54:01.500`, raw: `all connected ... with contraction ... of all ... graphs ... of L vertices`. The caption renders `connected` as `kinetic` in this span. At `00:54:53.000`, Yin says the expression rewrites the order-`g^n` contribution using connected graphs and explains that a disconnected graph is built from connected graph pieces.

At `00:55:24.240`, he gives a three-vertex example. Connected contributions enter `G^{(3)}`; disconnected products are omitted from that connected contribution. At `00:56:03.780`, he says the symmetry factors count the different ways that give the same contraction pattern. Raw: `the spirit factors are just different different ways that are given the same company`.

At `00:56:27.630-00:56:32.700`, JSON3 marks `[Music]`. At `00:56:38.040`, Yin accepts the combinatorial formula and begins the sum over all `m_l`.

### `00:56:38.040-01:00:04.078` | exponentiation and the logarithm of `Z` | pages 45-46

At `00:57:03.660`, Yin sums over all assignments of `m_l`. Raw: `the n factor of cancer right`, an ASR failure for cancellation of the factorial structure. He rewrites the sum as a product over `l`, with `1/m_l!` and `(G^{(l)}/l!)^{m_l}`.

At `00:58:00.839`, he identifies the independent sum over each `m_l` with an exponential. The page equation is `Z_g/Z_0=\exp(\sum_{l\ge1}G^{(l)}/l!)`. At `00:58:21.180`, raw: `if I had taken the log of z ... only keep track of the kinetic wraps`. The recoverable claim is that `\log Z` retains connected graphs.

At `00:58:47.359`, a question asks whether the exponentiation is a general characteristic of the construction. Yin says the rule follows from expanding the exponential and reproduces all disconnected products with their combinatorial positions. Raw at `00:59:23.400`: `when you expand this exponential you get a product of those G's`.

`00:59:44.359-01:00:04.078` is a board interval before the next question.

### `01:00:04.079-01:03:30.339` | graph factors, examples, and the sum over `m_l` | pages 44-45

At `01:00:04.079`, Yin says the connected-graph interpretation supplies a way to compute the partition function. A student asks where the factor of `g` enters. At `01:00:34.160`, raw: `where does it evolve oh gee it's included in the graph itself`. Yin answers that each vertex carries `-g/4!`.

At `01:01:00.180`, a follow-up asks whether the Green functions are multiplied inside each graph. Yin confirms this and distinguishes a single connected graph from the product of several graphs. At `01:01:42.660`, raw: `all of the possible ways to contract the three vertices ... as long as the whole thing remain connected`.

At `01:02:03.960`, Yin corrects or completes the written formula. Raw: `thank you` at `01:02:04.940`, followed by `here I'm summing over all the possible decompositions`. He explains that the sum over `{m_l}` ranges over all integer sequences with the required vertex count.

At `01:03:01.740`, he gives the ranges `m_1` from zero to infinity, `m_2` from zero to infinity, and so on. The caption renders `infinity` as `Fitness`. `[Music]` occurs at `01:03:27.230-01:03:30.339`.

### `01:03:30.340-01:07:07.798` | integer partitions, connectedness, and the three pairings | pages 45 and 36-42 cross-reference

At `01:03:32.359`, Yin distinguishes summing over an entire sequence from summing over one integer. Raw: `this bracket means that I'm summing over this entire sequence of integers m one and m two and m three`. At `01:03:50.040`, he notes that only finitely many `m_l` are nonzero in a fixed order.

At `01:04:02.280`, he says the construction ranges over every partition of the integer `n`. Raw: `every ... graph ... will be labeled by some ... m_l`. At `01:04:48.619`, he suggests doing the construction through `n` equal to five as practice.

At `01:05:04.940`, Yin clarifies that `G^{(l)}` means the sum of all connected graphs with `l` vertices. He contrasts the connected-graph sum with the combinatorial partition count. At `01:05:50.760`, a student asks why the quartic insertion gives three pairings. Raw: `where do we derive ... if it's Q to the four then it's like one x`.

At `01:06:18.900`, Yin identifies the four-field Gaussian calculation with the earlier `q_n q_m q_r q_s` rule. He says it can be derived by time discretization or by the integration-by-parts trick. The caption renders `Wick contraction` as `weak attraction` and `discretize` as `discriminize`.

`01:06:52.220-01:07:07.798` is a transition interval before the interpretation of `Z`.

### `01:07:07.799-01:10:41.279` | interpretation of `Z` and ground-state projection | page 46

At `01:07:07.799`, Yin says the graph expression looks unphysical until it is interpreted carefully. Raw: `now let's interpret the meaning of this ... not quite physical ... in fact it is ... provide that you interpret it carefully`. The page-46 equation identifies the Euclidean path integral with `\langle q_f|e^{-HT}|q_i\rangle`.

At `01:07:46.859`, he takes a finite imaginary-time interval and explains the boundary condition at its endpoints. Raw: `this is supposed to be actually ... Matrix element of the ... rotated in time evolution`. The caption phrase `this cube is subjective` is unresolved speech about the path boundary values.

At `01:08:15.720`, he says the boundary values become irrelevant when `T` tends to infinity, with a qualification that the final answer requires tracking them during the finite-`T` calculation. At `01:08:46.219`, he writes the spectral sum in an energy-eigenstate basis.

At `01:09:03.600`, raw: `dominated ... by the ground state`. At `01:09:18.859`, he assumes a unique ground state for the moment. The captions render this as `unique advantage point`; page 46 and the surrounding speech resolve the intended ground-state assumption.

At `01:09:45.719`, Yin explains that `\log Z` is `-E_0 T` plus an order-one term. Raw: `log of G ... minus e0 ... whatever that overlap is ... just going to be some one number`. The page equation gives `\log Z=-E_0T+O(1)`.

### `01:10:41.280-01:13:00.299` | energy difference and connected graphs in `log Z` | pages 46-47

At `01:10:41.280`, Yin compares `Z_g` with `Z_0`. Raw: `the difference between ground energy of the ... anharmonic oscillator and the harmonic oscillator ... correction energy due to the interaction term ... q to the fourth`.

At `01:11:10.560`, a question asks about the gap. Yin distinguishes the partition-function calculation from an excited-state gap calculation and says the two-point function will carry that information later. Raw: `the Gap will be ... if we look at the ... q q ... we're not doing that right`.

At `01:11:38.159`, he says `log` has a linear divergence in the time interval and calls this the divergence under discussion. At `01:11:57.239`, he returns to the result that `\log Z` is the sum over connected graphs and that the linear term gives the ground-state energy.

At `01:12:38.460`, he begins the explicit order-`g` calculation. Raw: `at the order G ... G l equals one ... this was three times this graph`. The caption uses `G` for the coupling and `kinetic wraps` for connected graphs. Page 47 supplies `G^{(1)}`.

### `01:13:00.300-01:16:20.639` | first-order ground-state energy and Hamiltonian comparison | pages 47-48

At `01:13:00.300`, Yin says he will stop drawing the purple graph and write the formula. Raw: `three times ... minus G over four factorial ... integral ... G ... TaoTao to the fourth`. The page equation gives `-g/8\int d\tau (G_0(\tau,\tau))^2`.

At `01:13:43.380`, he restores the oscillator frequency notation. Raw: `the harmonic oscillator ... one over two Omega e to the minus Omega ... absolute value`. The caption's `word to only` at `01:14:00.480` is a low-confidence fragment in the same formula explanation.

At `01:14:25.020`, he states the ground-state energy correction. Raw: `the ground state energy ... following form ... linear Divergence in time ... G over eight ... one over two Omega squared ... some other G squared term`. Page 47 resolves the result as `\Delta E_0=g/8(1/(2\omega))^2+O(g^2)`.

At `01:15:03.300`, Yin says the result is physical and can be recovered from Hamiltonian perturbation theory. Raw: `you could recover this from hamiltonian perturbation Theory ... the resulting should be equivalent`. Page 48 labels `H_0` and `H_1` and evaluates `\Delta E_0=g/32` after setting `\omega=1`.

At `01:15:37.860`, a student asks whether a quadratic-time divergence appears at order `g^2`. Yin says disconnected diagrams would produce the higher power, while the connected-graph sum retains a single linear divergence. The caption renders `connected` as `delay` and `diagrams` as `diagrams` with several clipped words.

### `01:16:20.640-01:18:33.979` | linear divergence, first-order question, and next numerator | pages 47-48

At `01:16:20.640`, Yin gives the reason for the single linear divergence. Raw: `these two points in the ... time cannot be very far separated otherwise this whole thing is suppressed exponential`. The source meaning is that the Euclidean Green functions suppress large relative-time separation.

At `01:17:02.760`, a student asks `is this the first order Corrections`. Yin answers `yes`, then says he can check it with Hamiltonian perturbation theory. At `01:17:24.420-01:17:56.879`, captions become fragmentary and a room question begins.

At `01:18:00.120`, the surviving exchange includes `is that interesting oh yes`. Yin says the information is inaccessible from the denominator alone. At `01:18:15.900`, he previews the next recording: `next lecture we'll discuss the QQ ... we started by talking about the particular value I only covered the ...` The source-page transition is to physical page 49, where the numerator `\langle0|\hat q(\tau)\hat q(0)|0\rangle` begins.

At `01:18:26.179`, raw: `we're going to set a numerator next time`. This is the final clear bridge from page 48 to page 49.

### `01:18:33.980-01:20:16.460` | perturbative-series qualification and small-`g` remark | page 48 plus oral material

At `01:18:33.980`, a student asks about the series. Raw: `what is it oh ... this series`. Yin says the perturbative expansion generally has zero radius of convergence. At `01:18:48.000`, the caption gives `serious expansion generally were not ... zero radius convergence`.

At `01:19:00.239`, he explains that a Taylor series can fail to converge to the function it formally represents. Raw: `this Taylor series ... doesn't actually convert to the function itself`. He gives the elementary example `minus 1 over X` and says the zero Taylor series on the positive side fails to reproduce the function. The caption renders `Taylor series` as `Taylor Swift`; this is a recognition error, with the mathematical example recoverable.

At `01:19:32.400`, Yin says the lecture will leave this issue aside for the semester's main perturbative applications. At `01:19:50.520`, raw: `the number three aspects is the major topic`; the number is an ASR artifact and the surrounding sentence is unresolved.

At `01:20:01.500-01:20:16.460`, Yin says numerical perturbation can work for sufficiently small coupling. Raw: `numerically approximately it's still going to work as long as it's too small there's a reason for that and uh let me post one explanation of that`. `too small` is the caption's raw wording; source context indicates a small-`g` qualification. The phrase `explanation of that` is the last spoken Chapter 2 content.

### `01:20:16.460-01:21:42.260` | closure and candidate room Q&A

`01:20:16.460-01:20:36.799` is a quiet interval after the small-`g` remark, with the rolling caption extending through `01:20:36.790`. At `01:20:36.800-01:20:40.040`, raw: `all right`. This is a classroom closure.

`01:20:40.040-01:21:38.459` is a long quiet interval. At `01:21:38.460-01:21:42.260`, raw: `absolutely` and `yeah`. The question that prompted these responses is absent from the caption track. Keep this as candidate Q&A with unresolved topic and source disposition.

### `01:21:42.260-01:23:28.159` | post-lecture tail

`01:21:42.260-01:22:00.079` is quiet. At `01:22:00.080-01:22:04.219`, raw: `right now` and `oh`; the material is too fragmentary for a claim. JSON3 marks `[Music]` at `01:22:07.250-01:22:10.359` and again at `01:22:37.390-01:22:41.540`.

At `01:22:41.540-01:23:10.499`, the surviving raw caption is `um`. At `01:23:10.500-01:23:24.919`, it is `differences`. At `01:23:24.920-01:23:28.159`, it is `I realize`. These fragments are outside the source-resolved lecture and remain raw tail material.

## Recognition and uncertainty ledger

The JSON3 confidence field contains 72 text segments below `160/255` and 192 between `160/255` and `189/255`. The following errors affect source interpretation and require the note layer or audio in a later pass:

At `00:00:27.900`, `variable was this appeal of this week` is unresolved. At `00:00:46.079` and `00:07:17.160`, `foreign` marks low-confidence speech. At `00:01:35.040`, `the nuclear internal the appear in` is unresolved mathematical wording.

At `00:02:38.580`, the words for `d\tau`, `dk`, `\omega`, and the denominator are unreliable. Page 39 supplies the Fourier equation. At `00:09:42.180-00:10:01.920`, `real time`, `imaginary time`, and `time evolution` are recoverable while the operator formula is caption-damaged.

At `00:14:19.079-00:16:52.519`, `N Harmony`, `harmonic acid`, and `practical language` are ASR errors around anharmonic oscillator, harmonic oscillator, and path-integral language. Page 41 supplies the exact Hamiltonian and Lagrangians.

At `00:21:48.000-00:22:51.380`, `permanent function`, `primary function`, `G over 400`, and `the board` are recognition errors around partition function, coupling normalization, and the quartic term.

At `00:31:00.720-00:36:10.619`, `living water`, `angle angle zero`, `white lines`, `bird boxes`, and `Galaxy integral` are raw caption failures. The recoverable content is the order expansion, the quartic vertex, the three Wick pairings, and the Green-function line factor.

At `00:38:19.820-00:40:02.280`, `minus G over 34`, `County`, and `compels` are damaged versions of the order-`g` coefficient, coupling, and power-counting discussion. Page 43 resolves the order-`g` formula.

At `00:44:31.160-00:59:41.520`, `bonification`, `kinetic graphs`, `weak interactions`, `spirit factors`, and `commentatorical positions` are recurring errors. The page equations and diagrams resolve normalization, connected graphs, Wick contractions, symmetry factors, and combinatorial positions.

At `01:00:34.160-01:06:55.940`, raw `where does it evolve oh gee`, `GG values`, `kinetic Rock`, and `weak attraction formula` preserve the sound sequence while the mathematical wording stays uncertain. The note layer supplies the vertex factor, `G^{(l)}`, and the three pairings.

At `01:07:39.180-01:10:34.020`, `this cube is subjective`, `people continue limits`, `United States`, and `granted energy` are caption errors around path boundary values, the `T\to\infty` limit, energy eigenstates, and ground-state energy.

At `01:13:20.820-01:15:00.480`, `G TaoTao`, `word to only`, and the damaged `E_0` sentence are equation-bearing speech. Page 47 supplies the exact factors and the `\omega` dependence.

At `01:15:34.080-01:17:17.360`, `equivalent`, `delay diagrams`, `Constitutional constant`, and `constant resistible` are low-confidence fragments in the Hamiltonian-comparison and connected-graph discussion. Retain the raw sequence and use page 48 for the equation.

At `01:18:33.980-01:20:16.460`, `number three`, `Taylor Swift`, `textures itself`, `applications`, and `too small` require source-context marking. The convergence qualification and the small-`g` numerical remark are recoverable; the exact surrounding wording remains caption-level uncertain.

The page-37 denominator visibly reads `Dx` while the numerator reads `Dg`. The page-38 calculation uses `[Dg]`. This is a source-page ambiguity rather than a caption repair. The caption layer also alternates among `q`, `g`, `G`, and spoken equation words. No notation normalization belongs in this lane.

## Adjacent-lecture overlap and boundary evidence

The 2022-09-13 recording `M0py5a4RWhE` is the preceding chronological lecture. Its interval around `01:07:04-01:15:18` introduces the Gaussian functional-integral generalization, treats the function as a vector in a function space, defines the linear operator `A`, and asks for its inverse kernel `G`. The target opens at `00:00:12.660` with a recap of that material. Physical pages 37-40 therefore have a deliberate overlap between the preceding lecture's derivation and this lecture's recap and continuation.

The 2022-09-20 recording `3VG2kDHso08` is the next chronological lecture. Its opening contains course logistics through approximately `00:01:08`. The first substantive continuation begins at `00:01:14.340` with the Euclidean two-point function and the numerator calculation. Its raw opening says `let's continue ... the euclidean two point function ... harmonic ...` and then returns to the quartic expansion and external insertions. This matches physical page 49, immediately after the page-48 Hamiltonian comparison in the target recording.

The remaining September 22, September 27, and September 29 recordings continue the Chapter 2 source span toward physical pages 62 and the Problem Set 2 boundary. Pages 63-67 contain the assignment. Page 68 begins Chapter 3. Those recordings supply adjacent source evidence rather than additional content for this video lane.

## Page dispositions for this video

Physical pages 20-36 establish the earlier Chapter 2 order and remain outside the target video span, with the exception of the spoken spectral recap tied to pages 26-29. Physical pages 37-48 are included in this video lane. Physical pages 49-62 are the later Chapter 2 continuation. Physical pages 63-67 are reserved Problem Set 2 material. Physical page 68 is the next-chapter divider.

The lecture source packet should preserve the raw caption track, the exact page equations, the low-confidence ASR fragments, the unresolved measure mismatch on page 37, the board intervals, the music intervals, and the candidate room Q&A. The artifact remains a Pass 1 evidence layer.
