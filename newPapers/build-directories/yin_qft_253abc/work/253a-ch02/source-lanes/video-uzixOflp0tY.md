# Pass 1 source-capture lane: Xi Yin QFT Chapter 2

Video: `uzixOflp0tY`
Recorded: 2022-09-08, 17:30:02 UTC
Title: `GMT20220908 173002 Recording 640x360`
Channel: Xi Yin
Playlist position: 9
Video duration in `work/pilot/playlist.jsonl`: `01:25:28`
Sourcebook chapter: Chapter 2, pages 20-62, with pages 63-67 assigned as Problem Set 2 and page 68 opening Chapter 3.

This is a raw Pass 1 lane. `raw:` preserves caption wording, including `uh`, repeated words, `[Music]`, and recognition failures. An interpretation after `capture:` is a source-order or board-content note. It is not a cleaned transcript. `[ASR error; likely: ...]` marks an inference from the page render, the local lecture context, or the adjacent source. `[uncertain: ...]` marks speech that remains unresolved. `[board gap]` marks an interval in the caption track where the lecturer is writing, drawing, or otherwise producing no recoverable speech. Page numbers refer to the rendered handwritten pages in `tmp/pdfs/253a-ch02-source/`.

## Track audit

Files examined in full:

- `work/253a-ch02/captions/20230504-uzixOflp0tY.en.json3`
- `work/253a-ch02/captions/20230504-uzixOflp0tY.en.vtt`

The JSON3 contains 3,374 events, with 3,373 events carrying `segs`. The VTT has 3,373 cues. The JSON3 has 3,187 text-bearing events and 186 newline-only or blank roll cues. The first text-bearing event is `00:00:10.040-00:00:17.279`. The last text-bearing event is `01:24:57.239-01:25:00.620`. A leading `~` on a detailed inventory boundary marks a coarse grouping endpoint rounded to the nearby caption interval; the exact track-derived chapter boundaries and gap times are given without `~`. The JSON3 start times and VTT cue times agree, with small millisecond rounding differences at some cue boundaries. The VTT has no text after `01:25:00.620`; the metadata duration leaves approximately 27.380 seconds of unc captioned video.

The opening JSON3 event at `00:00:00.000` is a duration or metadata event with no text. The first captioned material is logistics. The lecture starts its Chapter 2 subject transition at `00:02:50.879` and its first recoverable Chapter 2 claim at `00:02:55.980`.

## Source order, page order, and boundary

The manifest identifies the combined source PDF as `/Users/wlancer/Desktop/IAS/phy/qft/qft_253abc_book.pdf` and the playlist as `PLAd5nTR2YCdoAkJnywB0B9f8cghPSLM9m`. The playlist record for this video gives a 5,128 second duration and the 2022-09-08 recording date. Playlist position is not chronological. The adjacent chronological records are:

| recording | video | duration | source-order evidence |
|---|---|---:|---|
| 2022-09-06 | `96lN2omwit4` | `01:30:12` | preceding lecture; its late material reaches the Lagrangian path integral, the time-slicing construction, the momentum integral, and the measure issue on pages 21-25 |
| 2022-09-08 | `uzixOflp0tY` | `01:25:28` | this lane; it starts with the ground-state correlator on page 26 and ends while diagonalizing the harmonic-oscillator Euclidean action on page 31 |
| 2022-09-13 | `M0py5a4RWhE` | `01:25:02` | following lecture; it opens by finishing the Fourier-basis calculation from this recording and continues with the Gaussian correlator calculation from page 32 |
| 2022-09-15 | `vk_RlYUKUyM` | `01:23:27` | later Chapter 2 source, after the Sep. 13 continuation |

The rendered page order is:

| rendered pages | page content and source-order use |
|---|---|
| 20 | Chapter 2 title page, “Lagrangian Quantum Mechanics, Path Integrals, and Perturbation Theory.” It is the chapter divider. |
| 21-25 | Lagrangian and Hamiltonian formalism, time slicing, insertion of momentum states, the phase-space path integral, momentum integration, the measure, and ordering or counter-term ambiguity. These pages belong primarily to `96lN2omwit4`, the immediately preceding lecture. |
| 26 | Ground-state two-point correlator, insertion of the energy basis, energy gaps, analytic continuation, and the lower-half-plane convergence statement. This is the first direct page match in `uzixOflp0tY`. |
| 27-29 | Wick rotation, Euclidean time, ground-state projection, the complex-time contour, the imaginary-time correlator, the path-integral insertion, and the Euclidean Lagrangian. These are the main middle pages of this video. |
| 30-31 | Harmonic oscillator, finite Euclidean interval, Dirichlet endpoints, Fourier sine basis, orthonormality, and the diagonal Euclidean action. This video reaches these pages and stops before evaluating the mode Gaussian. |
| 32-40 | Gaussian mode integrals, oscillator correlator, general Gaussian functional integrals, Green functions, Fourier transform, and Wick contractions. The Sep. 13 video picks up from the page 31 action and enters this range. |
| 41-62 | Anharmonic oscillator, perturbation theory, diagrams, self-energy, spectral continuation, derivative interaction, regulator dependence, and counterterms. These pages are later Chapter 2 source material and are not spoken in this recording. |
| 63-67 | Problem Set 2. The lecturer references the posted problem set, problem two, and an extra-credit Jacobian item. The problem pages themselves are not lecture exposition in this video. |
| 68 | Chapter 3 title page, “Relativistic Particles, Fields, and Green Functions.” This is the next chapter divider. No Chapter 3 transition is recoverable in this recording. |

### Exact Chapter 2 timestamps for this video

- Chapter 2 lecture opening transition: `00:02:50.879`, raw: `um so so let's start with uh uh with the`.
- First transition word: `00:02:53.940`, raw: `physics`.
- First recoverable Chapter 2 substantive claim: `00:02:55.980`, raw: `um so last time I uh introduced the time`.
- Chapter 2 subject coverage in this video therefore begins at `00:02:50.879`; the first claim-bearing timestamp is `00:02:55.980`.
- Last substantive lecture qualification: `01:24:51.600`, raw: `um` after the statement about a measure on a function space. The preceding caption at `01:24:42.530` ends with `organizations`, and `01:24:48.780` ends with `facing functions`. `[ASR error; likely: measure on some function space]`.
- Final recoverable Q and A interval: `01:24:57.239-01:25:00.620`, raw: `uh any other questions`.
- Last captioned Chapter 2 lecture timestamp: `01:25:00.620`. The video metadata runs to `01:25:28.000`, with no later caption. The inventory below treats `01:25:00.620` as the exact end of recoverable Chapter 2 lecture material and records the remaining unc captioned tail separately.

The best direct page interval for this video is pages 26-31, with the page 31 Fourier-action calculation overlapping the Sep. 13 handoff. Pages 21-25 overlap the preceding Sep. 6 lecture at the sourcebook level. Page 20 is the title divider, and page 68 is a later chapter divider.

## Continuous timestamped inventory

### `00:00:00.000-00:02:50.878` - opening logistics and homework interval

- `00:00:00.000-00:00:10.039`: no captioned speech. The JSON3 duration event has no text.
- `00:00:10.040-00:00:39.540`: raw: `uh first of all the second time has been decided to be Fridays uh 10 30 a.m in the same room here ... and also Alex will go to the office hour afterwards at two to three p.m on Fridays uh in uh Jefferson 453 the seven room upstairs`. `[uncertain: “the seven room upstairs”]`. Capture: Friday section time and room; Friday office hour, 2-3 p.m., Jefferson 453, with the room description unresolved.
- `00:00:44.520-00:00:53.879`: raw: `further questions after the section if you go uh Billy's office hour ... the first uh problem set has been posted is in the homework Channel um slack`. Capture: post-section questions, Billy's office hour, and the PSet announcement in the homework Slack channel.
- `00:00:55.980-00:01:08.939`: raw: `you don't need to look at now in fact some of the stuff will make more sense after today's lecture`. Capture: delayed reading instruction for the posted problem set.
- `00:01:10.320-00:01:33.000`: raw: `the problems look pretty long but it was mostly the statement that try to guide you through the problems so it's actually a lot longer the better because taking out the convention and explain what you need to do`. `[ASR error; likely: the statements are longer because they explain the convention and what to do]`. Capture: the long problem statements are intended as guidance.
- `00:01:18.840-00:01:33.000`: raw: `if you happen to be if event is scary and they don't know what to do it shouldn't worry ... once you understand the physics the actual problems are actually pretty trivial`. `[ASR error; likely: if the event is scary / if the problem looks scary]`. Capture: reassurance about problem difficulty after the physics is understood.
- `00:01:36.560-00:01:46.320`: raw: `like 90 of doing physics is to understand how is that the calculation ... most of the time once you understand exactly what they do the actual calculation is pretty easy`. Capture: colloquial explanation of the relationship between understanding the setup and doing the calculation.
- `00:01:46.320-00:02:16.040`: raw: `I do uh encourage you to look at it right away after the class ... don't wait till last minute ... also it's due on Tuesday ... this problem set is actually despite the land of the statements actually on the shorter side`. `[ASR error; likely: despite the length of the statements]`. Capture: start the homework after class; due Tuesday; lecturer describes this set as short in substance.
- `00:02:17.060-00:02:40.879`: student question and answer about source files and the PDF. Raw fragments: `the text source for the Primitive yeah`, `do you prefer looking in the attack than PDF`, `so we can like fight the solutions`, and lecturer: `the other thing everyone use paper ... it's not exactly the same ... maybe not inconvenient`. `[uncertain: “Primitive,” “attack,” and “fight the solutions”]`. Capture: a student asks about the text source and source/PDF preference; the lecturer says the paper version is not exactly identical.
- `00:02:45.840-00:02:50.879`: raw: `okay ... so uh` followed by `um so so let's start with uh uh with the`. Capture: transition from logistics to the Chapter 2 lecture.

### `00:02:50.879-00:06:01.559` - ground-state correlator and energy-spectrum target, pages 26-27

- `00:02:50.879-00:03:00.599`: raw: `um so so let's start with uh uh with the physics ... um so last time I uh introduced the time in the world people can find the mechanics`. `[ASR error; likely: last time I introduced time evolution in quantum mechanics]`. Capture: the lecture resumes from the previous quantum-mechanics discussion.
- `00:03:00.599-00:03:08.400`: raw: `um and um now I'm going to discuss uh how you would use this probabilism`. `[ASR error; likely: formalism; possible “probability” is unresolved]`. Capture: use the preceding formalism to study observables.
- `00:03:08.400-00:03:16.640`: raw: `study some observables uh that uh captures uh you know physical quantities of Interest such as the energy spectrum of a quantum mechanical system`. Capture: energy spectrum is the first explicit target.
- `00:03:19.440-00:03:30.580`: raw: `we were considering it's on a simple funding mechanical models with uh finding many degrees freedom to begin with with some hamiltonian operator`. `[ASR error; likely: simple finite-degree mechanical models]`. Capture: finite-degree mechanical models with a Hamiltonian operator.
- `00:03:30.580-~00:03:35.000`: raw: `but sometimes you're telling me as a function that uh uh`. `[uncertain]`. The lecturer begins to specify the quantity to calculate.
- `00:03:35.270-00:03:38.640`: `[Music]`, followed by hesitation. Capture: audio transition before the energy-level formula.
- `00:03:42.780-00:03:54.770`: raw: `say we're interested in ... the uh energy levels of the hamiltonian ... I'm gonna probe that by studying the following quantity`.
- `00:03:54.780-00:04:05.159`: `[board gap]`. The caption has `performance` at `00:03:54.780` immediately before the gap. `[ASR error; likely: the displayed expression or a formula name was read incorrectly]`. Page match: p26 begins the ground-state correlator and its spectral decomposition.
- `00:04:05.159-00:04:38.400`: raw: `um so uh basically ... um uh observable uh of Interest which will be uh particularly convenient upon the filter even though this is not something that's often always discussing quantum mechanics ... correlation uh functions ... in the ground state`. `[ASR error; likely: particularly convenient in the field, although it is not always discussed in quantum mechanics]`. Capture: ground-state correlation functions are introduced as the useful observable.
- `00:04:38.400-00:04:55.020`: `[board gap]`. The preceding speech introduces the ground-state notation; no recoverable words occur in this interval.
- `00:04:55.020-00:05:10.500`: raw: `later uh it should be clear depending on whether I write Q if I write Q as an operator acting on the states sometimes I will drop the hat or forget to write the Hat it should be clear depending on the context whether it's an operator or a uh is a bear`. `[ASR error; likely: “a bare Q” or “a c-number”]`. Capture: hats may be omitted; context distinguishes the operator from the path-integral variable.
- `00:05:10.500-00:05:16.020`: raw: `so so now it's operator you have uh uh now uh as uh We've written in the last lecture`. Capture: switch to operator notation and recall the prior Heisenberg evolution convention.
- `00:05:16.020-00:05:32.556`: raw: `this Q has update uh the timely Evolution dictated by this ... relation uh into that I over R which has B into that minus the signal Base Bar which had a t that's how the operator evolved in either a picture`. `[ASR error; likely: “this Q has time evolution dictated by this relation ... e^{iHt/hbar} ... that's how the operator evolved in the Heisenberg picture”]`. Capture: Heisenberg-picture time evolution is written on the board.
- `00:05:37.139-00:05:53.039`: raw: `so the query function I'm going to be interested in is the following you've had a uh you had zero uh in the vacuum and take its overlap with the value so this thing uh because it's the two-point equation function in in the ground state ... so G of B ... right so that's the definition`. `[ASR errors; likely: “correlator,” “bra,” “vacuum,” and “two-point correlation function”]`. Page match: p26 equation `G(t)=<0|q(t)q(0)|0>`.
- `00:06:01.560-00:06:06.840`: raw: `uh any questions so far`. Q and A prompt.
- `00:06:06.840-00:06:27.240`: raw: `I think you had the time zero average if you had the time T again the things overlap with the vacuum notation always actually is in a hydrogen break picture ... the say does not involve`. `[ASR error; likely: time-zero operator, time-T operator, vacuum notation, and Heisenberg picture]`. Capture: lecturer restates the correlator and the picture convention in response to the prompt.

### `00:06:27.240-00:10:00.540` - spectral insertion and the first board derivation, page 26

- `00:06:27.240-00:06:35.240`: raw: `now uh why would we care about Central quantity`. `[ASR error; likely: “central quantity” is clear enough]`. Capture: motivation question for the correlator.
- `00:06:35.240-00:06:39.720`: raw: `well uh obviously uh if you have a uh what's a normal basis`. `[ASR error; likely: a normalized basis or energy basis]`.
- `00:06:46.280-00:07:04.680`: raw: `of energy ... and say ... this person said and in some en ends of ... the answer to that`. `[uncertain]`. Capture: lecturer sets up the energy eigenbasis and the spectral answer while writing.
- `00:07:04.680-00:07:17.529`: `[board gap]`; `00:07:17.539-00:07:24.180` resumes with `and so forth`. Capture: completion of the basis expansion on the board.
- `00:07:20.460-00:07:54.300`: raw: `um then uh we can write this G of D so we can insert a complete basis ... so basis ... United States ... is there a complete basis in uh here ... equivalently right there's two point for your function as the sun over energy`. `[ASR errors; likely: “insert a complete basis ... equivalently the two-point function is a sum over energy eigenstates”]`. Page match: p26 spectral decomposition.
- `00:07:54.300-00:08:11.710`: `[board gap]`. Capture: energy-basis expression is written.
- `00:08:11.720-00:08:33.170`: `[board gap]`, followed by `00:08:33.180-00:08:48.829` raw `so` and further board work. Capture: exponential factors and overlaps are being placed on the board.
- `00:08:48.829-00:08:59.180`: raw: `if it's okay is then not equal to sum over n and zero or two times zero and and uh zero zero sometimes the`. `[ASR error; likely: the student or lecturer reads the sum over n, matrix elements, and exponential factors]`. The exact spoken formula is not recoverable from captions; use p26 for the equation reference.
- `00:08:59.180-00:09:12.290`: `[board gap]`.
- `00:09:12.300-00:09:29.630`: `[board gap]`.
- `00:09:29.640-00:09:47.870`: `[board gap]`; `00:09:47.880-00:09:50.540` raw: `any questions`. Capture: lecturer pauses after the spectral sum.
- `00:09:55.080-00:10:00.040`: raw: `okay so this is going to be a basic Observer of interest because`. Capture: begins the interpretation of the spectral expression.

### `00:10:00.540-00:15:54.119` - energy gaps, inverse transform, and analytic continuation, pages 26-27

- `00:10:00.540-~00:10:28.000`: raw: `you see it captured the energy level ... so it has a difference between the energy of the ground state and any exciting State`. `[ASR error; likely: excited state]`. Capture: the correlator carries energy gaps `E_n-E_0`.
- `~00:10:28.000-00:10:31.279`: raw: `if you know GOP is the function P you can do the inverse polio transform and figure`. `[ASR error; likely: if you know G(tau), take an inverse Laplace transform]`.
- `00:10:31.279-~00:10:41.000`: raw: `out so captured all the information the product is that this overlap is not zero which genetically would be`. `[ASR error; likely: the correlator captures the information provided the overlap is nonzero]`.
- `~00:10:41.000-~00:10:48.000`: raw: `um now of course if you take the harmonic oscillator there's an accident if you take a common alternator actually this state only is non-trivial for n equals one`. `[ASR error; likely: in the harmonic oscillator, this matrix element is nonzero only for n=1]`. Page match: p26 discussion of the oscillator special case.
- `~00:10:48.000-~00:10:55.000`: raw: `but the more generic system this Q had on the vacuum I can come across that it will generally have none zero overlap with any excited States ... the two point function will capture all the energy Spectrum`. `[ASR errors; likely: a generic operator acting on the vacuum has nonzero overlap with excited states]`.
- `00:10:55.860-~00:11:01.000`: raw: `okay so so that's one reason why I would be interested in this but another reason I do speak swirly is that this is something that's relatively easy to calculate using the pattern more formative`. `[ASR error; likely: “another reason I do speak early / use it is that this is relatively easy to calculate using the path integral formalism”]`. Capture: the path integral gives a convenient calculation route.
- `00:10:55.860-~00:11:00.000`: `[board gap]` intervals are embedded in the transition to `E_n-E_0`.
- `00:10:55.860-~00:11:13.000`: raw: `um so uh my assumption uh e n minus e0 is uh is not negative because we're assuming the easier always`. `[ASR error; likely: `E_n-E_0` is nonnegative because the ground-state energy is the lowest]`.
- `00:11:13.260-~00:11:20.000`: raw: `um so one of the things we're going to do with this ... in field Theory ... is to ... not just as function of a real number T but ... as an energy function in C and ... G of T ... so complex values`. `[ASR errors; likely: extend G(t) from real t to complex t]`.
- `~00:11:31.000-~00:11:44.000`: raw: `okay so uh by the way uh how many people feel comfortable with the notion of another continuation of analytic function`. `[ASR error; likely: analytic continuation]`. Capture: audience check on analytic continuation.
- `~00:11:44.000-~00:12:09.000`: raw: `I think not everybody ... don't worry ... we will introduce these things gently ... the first thing or most important mathematical tool for Quantum field theory is complex analysis in one variable`. Capture: complex analysis is announced as a recurring QFT tool; lecturer promises a gentle introduction.
- `~00:12:09.000-~00:12:23.000`: raw: `if you're not familiar with at this point you will be familiar by the Android`. `[ASR error; likely: by the end]`.
- `~00:12:21.000-~00:12:46.000`: raw: `imagine you uh I'll take this pumpkin gft and extend the notion so April is defined for real number T real-time Devolution but we're gonna imagine uh we're gonna attempt to try to extend GOP uh as a function uh complex`. `[ASR errors; likely: “take this function G(t), defined for real-time evolution, and extend it as a function of complex t”]`.
- `~00:12:40.000-~00:12:50.000`: raw: `by the function of complex primary 13. now can we actually do that`. `[ASR error; likely: complex variable]`. Capture: extension question.
- `~00:12:50.000-~00:13:01.000`: raw: `if you look at the sum in terms by term obviously you can do that because you have this exponential you can replace the T from a real number to a complex number there's nothing wrong about that`. Capture: termwise replacement of real time by complex time is formally available.
- `~00:13:01.000-~00:13:15.000`: raw: `but there's a question that when the sun will converge ... the sound generated infinite sum ... there's a question of whether converges`. `[ASR errors; likely: whether the infinite sum converges]`. Capture: convergence is the actual issue.
- `~00:13:15.000-~00:13:32.000`: raw: `typically a quantity system you can take the harmonic oscillator ... how many ounces actually ... too trivial ... this state is actually equal to one of the sum ... but for generic system ... arbitrary ... arbitrary potential`. `[ASR errors; likely: the harmonic oscillator is too simple for this convergence issue; generic spectra require care]`.
- `~00:13:32.000-~00:13:46.000`: raw: `the sum could be evidence sound but in that situation uh you have to be a little hair because uh if you replace this T by complex parameter depending on the sign of this imaginary part`. `[ASR errors; likely: the sum could diverge; the sign of the imaginary part matters]`.
- `~00:13:46.000-~00:14:20.000`: raw: `if you want to have an I ... times T will have a real power ... positive sign or negative sign ... if the sign if minus i t has positive real part then they multiply this energy this will grow exponentially for higher difference and then typically the sum might diverge`. `[ASR errors; likely: one sign makes high-energy terms grow, while the other suppresses them]`.
- `~00:14:20.000-~00:14:39.000`: raw: `on the other hand if you ... analytically continue ... to complexity ... imaginary party Limited ... then ... the real part of this exponent will be some negative number times ... E_n minus e0 ... suppressed by high energy`. `[ASR errors; likely: continuation into the lower imaginary half-plane gives exponential suppression]`.
- `~00:14:39.000-~00:15:04.000`: raw: `so in that case the sum will tend to converge and indeed there's a mathematical theorem ... that will guarantee ... this sum ... makes sense`. Capture: a theorem is invoked for the convergence region.
- `~00:15:04.000-~00:15:31.000`: raw: `for this the sum of N converges ... P of T is a qualifying ... has some nice properties which I will not fully elaborate on ... this continuation through complex ... is well defined ... imaginary part ... we're going to be interested in studying this two-point ... not only for real T but ... negative imaginary parts`. `[ASR errors]`. Page match: p26 labels the convergence result with “Paley-Wiener theorem.” The theorem name is not clearly present in the caption speech, so this page label is a note-supported equation reference rather than a claimed exact spoken phrase.

### `00:15:54.120-00:20:00.069` - lower-half-plane question, Wick rotation, and a naming aside, pages 26-27

- `00:15:54.120-00:16:11.889`: `[board gap]` while the convergence region or axes are being drawn.
- `00:16:11.899-00:16:35.399`: student question, raw: `a few squares so effectively to be what zero is ... fine no not necessarily ... and gm0 is fine but that's not the what I'm worried about I'm worried about ... acquiring a positive imagine Fund`. `[ASR error; likely: the question asks what happens at or near the positive imaginary axis]`. Lecturer identifies the positive imaginary part as the concern.
- `00:16:35.399-00:16:45.170`: `[board gap]`.
- `00:16:45.180-~00:17:09.000`: raw: `no uh so far I haven't made any additional statement right all I'm saying is that let's go into contact ... but here it's a real axis this is the imaginary axis`. `[ASR error; likely: “let me draw the real and imaginary axes”]`. Capture: complex plane diagram, with real and imaginary axes.
- `~00:17:09.000-~00:17:25.000`: raw: `all we say is that ... I can't ... go down ... and I expect that ... cool`. `[uncertain]`. Capture: lecturer returns to the safe continuation direction.
- `00:17:25.180-~00:17:38.000`: raw: `um okay ... if you know what happens to the imaginary time ... oh yes absolutely`. `[uncertain; Q and A transition]`.
- `~00:17:38.000-~00:18:12.000`: raw: `so uh well that's the thing that about any continuation ... in particularly important case ... for example let's take C to be minus I now where now is a positive real number called the real number`. `[ASR errors; likely: set `t=-i tau` with positive real `tau`]`.
- `~00:18:12.000-~00:18:36.000`: raw: `commonly you know this is sometimes called the weak rotation`. `[ASR error; likely: Wick rotation]`. Capture: the continuation to negative imaginary time is named.
- `~00:18:36.000-~00:18:57.000`: raw: `I don't like this term rotation because uh it's not really we're not relatively anything it's really any configuration`. `[ASR error; likely: “we are not literally rotating anything; it is an analytic continuation”]`. This is a light terminology aside, with no separate joke recoverable.
- `~00:18:57.000-~00:19:10.000`: raw: `and you know this will become clear uh into examples ... in this case ... if we start with this this guy ... we think T to B minus`. `[ASR errors; likely: substitute `t=-i tau`]`.
- `~00:19:10.000-~00:19:35.000`: raw: `here we have a sum over n zero two zero and and two zero zero this is just one number and now and e to the minus one over H bar the N minus e0`. `[ASR errors; likely: spectral sum with matrix elements and `exp[-(E_n-E_0) tau/hbar]`]`.
- `~00:19:35.000-00:20:00.069`: raw: `as I said earlier you know these things are explodingly suppressed at higher energies and there's some typically convergence ... if you know the value of the ... on the negative axis ... analytically ... unambiguously ... back to real`. `[ASR errors; likely: lower-half-plane data determine the real-time function by analyticity]`.

### `00:20:00.070-~00:25:25.000` - analytic continuation construction and Q and A, pages 27-28

- `00:20:00.070-~00:20:22.000`: raw: `uh to agree about your teeth uh maybe just as a as as a a kind of a brief mathematical aside how does this work in general`. `[ASR error; likely: “to clarify this, as a brief mathematical aside, how does this work in general?”]`. Capture: transition to a Taylor-series construction.
- `~00:20:22.000-~00:20:47.000`: raw: `you have some function ... a functional real value ... imagine trying to define the function on the complex ... with the real axis here ... a plus R i this function would be defined anywhere along the real axis`. `[ASR errors; likely: a real-valued function on the real axis is extended to a complex plane]`.
- `~00:20:47.000-~00:21:15.000`: raw: `suppose the function is analytic at one point which means that the Taylor series of the function ... to the function itself in a neighborhood of that point ... over here you can write the paper series sum over ...`. `[ASR errors; likely: write the Taylor series about a point]`.
- `~00:21:15.000-~00:21:43.000`: raw: `where this point is the mineral ... get suppressed by some number to Npower ... every term in the sum ... converge ... radius ... this is the radius convergence`. `[ASR errors; likely: terms are suppressed by powers of the displacement and the series has a radius of convergence]`.
- `~00:21:43.000-~00:22:04.000`: raw: `it always will also converge if you replace ... by the complex number in this little disk ... the series will converge on this disk ... defines anywhere inside of this as an under function ... defines unambiguously the element integration the function`. `[ASR errors; likely: the Taylor series defines the analytic continuation inside its disk]`.
- `~00:22:04.000-~00:22:17.000`: raw: `any questions` and a student acknowledgment. Q and A interval begins.
- `~00:22:05.000-~00:22:35.000`: student question, raw: `I this is the definition of beneficiation ... I'm saying that I sort of function with reality I can associate and move the function of one context here`. `[ASR errors; likely: question asks for the definition of analytic continuation]`.
- `~00:22:35.000-~00:23:08.000`: lecturer answer, raw: `the way this functional complex variable is constructed by taking the pillar Series ... starting with ... around a point on the real axis ... any random data series ... if you find the radius convergence it will also converge ... replace ... by a complex number inside this disk`. `[ASR errors; likely: construct a complex analytic function from Taylor series centered on a real-axis point]`.
- `~00:23:08.000-~00:23:35.000`: raw: `inside the disk ... complex analytic function ... defined ... start at another point ... do the same procedure provided that you still have some radius`. Capture: continue by re-expanding in overlapping disks.
- `~00:23:35.000-~00:24:03.000`: raw: `you know I invite you to ... I'll try the example of uh like one over one minus D over something`. `[ASR error; likely: example `1/(1-z)`; exact denominator speech is unclear]`.
- `~00:24:03.000-~00:24:28.000`: raw: `if you take the function the one over ... start at the origin ... there's already convergence ... if you just do the Taylor series you're stuck on this disk but if you re-expand over here you can go around this ... cover the ... singularities`. `[ASR errors; likely: the singularity limits the first disk; overlapping expansions continue around it where possible]`.
- `~00:24:28.000-~00:24:39.000`: raw: `okay uh any other questions`. Q and A prompt.
- `~00:24:39.000-~00:25:08.000`: student question, raw: `actually yeah when you're you're in the initial Circle ... are you using the same particular Series`. `[ASR errors; likely: whether the same Taylor series is used in the next circle]`.
- `~00:25:08.000-~00:25:25.000`: lecturer answer, raw: `because I'm really expanding the function uh at that point and so I need to use the average derivative of in order to function at that point ... anyway ... we'll go into the section`. `[ASR error; likely: re-expand at the new point using derivatives there]`.

### `~00:25:25.000-00:32:35.269` - ground-state projection and the complex-time contour, page 27

- `~00:25:25.000-~00:25:36.000`: raw: `um so ... another thing ...` followed by the assumption of a gap. Capture: transition back from the mathematical aside to the correlator.
- `~00:25:36.000-~00:26:04.000`: raw: `assuming gap ... E1 minus E0 ...` with the energy gap and nondegenerate-ground-state condition on the board. `[ASR error; exact speech about the gap is incomplete]`. Page match: p27 projection argument.
- `~00:26:04.000-00:26:26.640`: raw: `if you take a generic state psi ... e to the minus ... H ... T is very large ... positive ... pick up the contribution from the ground state`. `[ASR errors; likely: imaginary-time evolution projects a generic state with nonzero vacuum overlap onto the ground state]`.
- `00:26:26.640-00:26:46.310`: `[board gap]` while the projection formula is written.
- `00:26:46.320-00:28:07.320`: raw: `when I say divided sorry now we're going to say ... possibility ... e to the minus 1 over H bar Capital H ... at ... T is very large because it's going to be positive ... Q 0`. `[ASR errors; likely: write the correlator as a ratio with `exp[-(H-E_0)T/hbar]` on the two sides and a generic state]`.
- `00:28:07.320-00:28:16.430`: `[board gap]`.
- `00:28:16.430-~00:28:27.000`: student question, raw: `last time I never had this group had research ... so last time ...` `[uncertain; likely asks where the `E_0` or the large-T factor went]`.
- `~00:28:27.000-~00:28:43.000`: lecturer clarification, raw: `this is something new compared to last time ... where did the E not go ...` `[ASR errors; likely: the `E_0` factors cancel between numerator and denominator]`.
- `~00:28:43.000-00:29:50.940`: raw: `you can think of this whole thing as ... operator variable in this path in complex time ... at some point ... insert ... q hats ... evolve ...`. `[ASR errors; likely: draw a contour with imaginary-time evolution to project the endpoints and a real-time segment between operator insertions]`.
- `00:29:50.940-00:30:00.070`: `[board gap]` while the contour is drawn.
- `00:30:00.080-00:32:22.919`: raw: `we are a contour here ... work with a negative imagery T ... consider this rotation ... take ... to be minus ... when there's no room for confusion ... still write this as Q of Tau ... Q at Tau is actually a different function`. `[ASR errors; likely: the contour can be replaced by a path along negative imaginary time; write `q(tau)` by convention]`. Page match: p27 contour and p28 notation.
- `00:32:22.919-00:32:35.269`: `[board gap]` before the alternative imaginary-time expression.

### `00:32:35.269-~00:36:15.000` - imaginary-time correlator and inverse Laplace statement, pages 28-29

- `00:32:35.269-00:33:14.940`: raw: `it's really ... minus ital ... probably will be clear depending on the context what I actually need`. `[ASR errors; likely: the continued correlator is being written with `t=-i tau`]`.
- `00:33:14.940-00:33:52.730`: `[board gap]`.
- `00:33:52.730-~00:34:37.000`: raw: `so this is ... same expression ... replace ... Q hat ...` and the continuation to imaginary time. `[ASR errors]`. Capture: alternative formula for `G(-i tau)`.
- `~00:34:37.000-~00:35:14.000`: raw: `this is another way to rewrite this two point function with imaginary negative ... this also captures the energy spectrum`. `[ASR errors; likely: the imaginary-time correlator contains the same spectral information]`.
- `~00:35:14.000-~00:35:47.000`: raw: `for example if you know this function for Tau you can just do the inverse ... transform and recover the energy exactly`. `[ASR errors; likely: inverse Laplace transform recovers the energies]`.
- `~00:35:47.000-~00:36:15.000`: raw: `so ... we're going to now investigate how to access this observable using the path ...` `[ASR error; likely: path integral]`. Capture: transition to path-integral evaluation.

### `~00:36:15.000-00:38:11.270` - path-integral motivation and scope

- `~00:36:15.000-00:36:34.910`: raw: `the path integral is a better Behavior ... so what critical information ...`. `[ASR errors; likely: path integral is a convenient way to calculate the correlator]`.
- `00:36:34.910-00:37:35.820`: raw: `the only intuition ... some Matrix elements of operators ... at this point I don't need to give any interpretation this is just something I can study ... capture the energy spectrum and some other information about metric settlement`. `[ASR errors; likely: the object is a matrix element; no further physical interpretation is needed at this stage]`.
- `00:37:35.820-00:38:11.270`: `[board gap]`, then transition: `the real reason ... natural thing to cover using pattern ... if you want to probe any observable using ... this is sort of the ... thing to start with`. `[ASR errors; likely: path integrals are the natural starting point for probing observables]`.
- `00:38:11.270-~00:38:21.000`: raw: `um any other questions` followed by a student acknowledgment. Q and A interval.

### `00:38:11.270-~00:43:29.000` - inserting operators into the path integral, pages 28-29

- `00:38:11.270-~00:38:28.000`: raw: `okay so uh ... how do we continue such a thing ... here's a nice thing about it`. Capture: lecturer answers how to continue from the ordinary path-integral matrix element.
- `~00:38:28.000-~00:39:00.000`: raw: `in the past integral ... this two-point assumption ... you can follow the same logic as the way we derive the Matrix element of operator last time`. `[ASR errors; likely: use the same complete-basis and time-slicing derivation as in the previous lecture]`.
- `~00:39:00.000-~00:39:31.000`: raw: `start doing a complete basis at small steps of time ... get rid of the conjugate momentum ... produce some kind of integration over this path of Q going to some range of time`. `[ASR errors; likely: insert complete position and momentum bases, integrate out momentum, and obtain an integral over q(tau)]`.
- `~00:39:31.000-~00:40:08.000`: raw: `what happens if you have this additional insertion of Q hats ... if you get to the point where you have time zero you just insert the ... and then ... another two hats`. `[ASR errors; likely: operator insertions are placed at their time slices]`.
- `~00:40:08.000-00:40:42.420`: raw: `if you calculate the Matrix element ... because this p's and q's ... States ... you'll just pick up qn at that step`. `[ASR errors; likely: a q-operator insertion contributes the q eigenvalue at the corresponding slice]`.
- `00:40:42.420-00:40:59.829`: `[board gap]`.
- `00:40:59.839-00:41:55.380`: raw: `the result ... inserting a q t and q0 into the ... but no longer as operator but just as variables ... write integral DQ this measure factor ... we don't have to carefully interpret this in value of computations ... e to the I over degrees power and action`. `[ASR errors; likely: the operator correlator becomes a path integral with c-number factors `q(tau)q(0)` in the integrand]`.
- `00:41:55.380-00:42:12.109`: `[board gap]`.
- `00:42:12.119-~00:42:39.000`: raw: `convolutional time to some kind of time ... specify that in moment so lagrangian ... I can give you that DT ... not same material Prime`. `[ASR errors; likely: write the action and time interval in the Euclidean path integral]`.
- `~00:42:40.000-~00:42:49.000`: raw: `and this is going to insert QT and uh zero in here`. Capture: displayed path integral has the two insertions.
- `~00:42:49.000-~00:43:29.000`: raw: `now this is not quite the left hand side yet because if you recall our generation last time ... first of all you have to specify some boundary condition`. `[ASR errors; likely: the path integral still needs endpoint boundary conditions]`.

### `~00:43:29.000-~00:47:56.000` - endpoint conditions, insertion meaning, and real versus imaginary contour

- `~00:43:29.000-~00:43:50.000`: `[board gap]`, then raw: `we do not want to specify conditions of your final ... we don't have to specify because ... this side here is arbitrary`. `[ASR errors; likely: endpoint values are arbitrary for the ground-state projection]`.
- `~00:43:50.000-~00:44:25.000`: raw: `I could have replaced this side by side ... this doesn't actually matter ... that dependence will drop out ... if I evolve in this specific way I'm only going to pick up the contribution from the ground state`. Capture: arbitrary endpoint dependence drops out as the imaginary-time interval becomes large.
- `~00:44:25.000-~00:44:44.000`: raw: `and indeed that's the procedure we're going to follow ... take this and divide by the passenger row ... same path ... without this Q insertion ... then you take a limit ... imaginary part of T`. `[ASR errors; likely: divide the inserted path integral by the no-insertion path integral and take the large-imaginary-time limit]`.
- `~00:44:44.000-~00:45:00.000`: raw: `okay so so this is going to be the empathic representation of the two point correlation function of our interest`. `[ASR error; likely: “path-integral representation”]`.
- `~00:45:00.000-~00:45:42.000`: raw: `if I take T to be real ... interpret with action ... as a contour ... on a complex plane ... if I just ... the continued version ... if interested in that ... moving in imaginary time ... don't have to do this weird thing ... more straightforward`. `[ASR errors; likely: real-time evolution follows a complex contour, while the imaginary-time correlator follows a simple straight path]`.
- `~00:45:42.000-~00:45:45.000`: raw: `uh any question about this formula here`.
- `~00:45:45.000-~00:46:08.000`: student question, raw: `yes just to make sure ... so the q i and Q final can be any right`. Capture: student asks whether `q_i` and `q_f` can be arbitrary.
- `~00:46:08.000-~00:46:26.000`: lecturer answer, raw: `that's good that's correct so here I don't even need to specify the boundary condition because that depends on the market will drop out in this limit`. `[ASR errors; likely: endpoint dependence drops out]`.
- `~00:46:26.000-~00:46:45.000`: raw: `that's why I introduced that whole Gadget video ... I mean I could have kept track of the final condition but it'll make things more Counting`. `[ASR errors; likely: the device of the large-time projection avoids carrying endpoint data through the calculation]`.
- `~00:46:45.000-~00:47:04.000`: raw: `okay uh any other questions` followed by a student question. Q and A interval.
- `~00:47:04.000-~00:47:40.000`: student question, raw: `in this case we're taking ... states ... q0 ... equals the same QR`. `[ASR errors; likely: student asks whether the initial and final position values are set equal]`.
- `~00:47:40.000-~00:47:56.000`: lecturer correction, raw: `no no no no no no no ... Qi plays the role of this side primary and the qf will play the row of the side here ... I don't have to specify them because ... dependence ... will drop out`. `[ASR error in “side primary” and “row”]`. Capture: `q_i` and `q_f` are separate endpoint variables; equality is not imposed.

### `~00:47:56.000-~00:50:02.000` - why the insertion is new and numerical continuation question

- `~00:47:56.000-00:48:13.619`: raw: `so then how did we go from what because last time I never had this ...`. `[uncertain]`. Student asks how the inserted-operator expression differs from the preceding lecture's expression.
- `00:48:13.619-00:48:24.069`: `[board gap]`.
- `00:48:24.079-00:49:35.520`: raw: `last time ... this is something new compared to last time ... discretizing ... two hats ... enter in that computation in this Matrix element between ... basis ... q and P basis ... the Q hat on the q basis just picks up this argument eigen value ... qn ... this qn turns into Q of t or Q of zero ... variable of the integration`. `[ASR errors; likely: the operator is inserted between time-slice basis states, and its q eigenvalue becomes the path variable]`.
- `00:49:35.520-00:49:54.050`: `[board gap]`.
- `00:49:54.060-~00:50:17.000`: raw: `this is kind of a basically but very important point ... on the left-hand side this is an operator ... integrating over the space of functions Q ... q0 is one of these ... q at t is another ... insert that into the integral ... part of the integrand`. Capture: operator on the Hilbert-space side becomes a c-number factor in the functional integrand.
- `~00:50:17.000-~00:50:30.000`: raw: `the claim is that this pattern ... reproduce that answer provided that you regularize this measure correctly`. `[ASR error; likely: path integral reproduces the operator answer only with a correctly regularized measure]`.
- `~00:50:30.000-~00:50:43.000`: raw: `imaginary ... all throughout ... still taking the key to be real ... action as defined by following this path`. `[ASR errors; likely: the real-time expression still needs contour interpretation]`.
- `~00:50:43.000-~00:51:26.000`: raw: `if I instead ... work with ... imaginary ... drive this red point down here ... don't have to worry about this ... convenient to work with G at the negative imagery`. `[ASR errors; likely: use the lower-half-plane continuation to avoid the contour complication]`.
- `~00:51:26.000-~00:51:38.000`: raw: `yes but the whole point is that acceleration is unambiguous if you have ... know the function for imagery`. `[ASR error; likely: analytic continuation is unambiguous when the imaginary-time function is known]`.
- `~00:51:38.000-~00:52:14.000`: raw: `it is analytic on this lower half complexity plane then that has all the information to determine the function and reality`. `[ASR errors; likely: analyticity on the lower half-plane determines the real-time function]`.
- `~00:52:14.000-~00:52:43.000`: raw: `I'm not sure what do you mean by can do analytic ... when we prove ... calculus for a reason`. `[uncertain]`. A follow-up question about what can be done analytically.
- `~00:52:43.000-~00:53:15.000`: raw: `I didn't say ... we can launch into a lengthy discussion of how you numerically and continue ... very interesting subject but it will take us a bit far from the theme`. `[ASR error; likely: numerical analytic continuation is a lengthy topic outside this lecture]`.
- `~00:53:15.000-~00:53:32.000`: raw: `but numerically ... this procedure ... repeated ... not a multiplication way calculation ... order in the Taylor series ... this you can do on the computer`. `[ASR errors; likely: repeated Taylor re-expansion can be implemented numerically]`.
- `~00:53:32.000-~00:53:56.000`: raw: `okay uh any uh other questions ... um so uh let's see`. Q and A closes and the lecture returns to Euclidean notation.
- `~00:53:56.000-~00:55:00.000`: raw: `as I ... I don't want to keep ...` and the notation transition. `[ASR errors]`.

### `~00:50:02.000-00:58:52.129` - Euclidean Lagrangian and the convergence advantage, pages 28-29

- `~00:50:02.000-~00:50:20.000`: raw: `often ... consider this rotation ... take ... to be minus ... when there's no room for confusion I'm still going to write this as Q of Tau ... Q of Tau is actually a different function`. `[ASR errors; likely: use `q(tau)` as shorthand after setting `t=-i tau`]`.
- `~00:50:20.000-~00:50:38.000`: raw: `right it's an integration of this two at least now ... it's really ... minus ...`. `[uncertain]`. Capture: notation and the continuation are being fixed.
- `00:50:40.400-00:50:57.059`: raw: `okay so this is by a slide uh notation ... if I apply that to this actually on the lagrangian I would kind of derivative of q ... by dT of Q ... become`. `[ASR errors; likely: apply the substitution to the Lagrangian and transform the time derivative]`.
- `00:50:57.059-00:51:16.920`: raw: `[Music] ... so ... typically ... for example this Lagrangian ... suppose this lagrangian is in the form ... potential term is a potential term`. `[ASR errors]`. Capture: board work on the generic Lagrangian.
- `00:51:16.920-00:51:26.750`: `[board gap]`.
- `00:51:26.760-00:52:12.720`: raw: `if I do this replacement it goes to a minus I ... replace these two dots with I times ... by the time of Q so this becomes minus one half ... and of course if I integrate also this measure DT ... replaced by minus I`. `[ASR errors; likely: `dt=-i d tau` and `dq/dt=i dq/dtau`]`.
- `00:52:12.720-00:52:32.329`: `[board gap]`.
- `00:52:32.339-~00:53:14.000`: raw: `e to the I over H bar integral L ... under this weak rotation ... what does it become ... this T is going to become ... Define this thing ... what we usually call the euclidean version of lagrangian`. `[ASR errors; likely: define `L_E` so the oscillatory weight becomes `exp(-S_E/hbar)`]`.
- `~00:53:14.000-~00:53:46.000`: raw: `the wick rotating version is a function of Q and Tau ... my convention is always going to be such that this ... is defined to be minus ...`. `[ASR errors; likely: `L(q,qdot) = - L_E(q, partial_tau q)` under the convention shown on p29]`.
- `~00:53:46.000-~00:54:03.000`: raw: `for example if the usual lagrangian is one half q dot squared minus V of Q then this euclidean version ... now it becomes plus one half d by d p q square plus ...`. `[ASR errors; likely: `L_E=1/2 (partial_tau q)^2+V(q)`]`.
- `~00:54:03.000-~00:54:23.000`: raw: `the reason for this assignment is just that I want to make this L euclidean ... positive ... potential is bounded from below`. `[ASR errors; likely: Euclidean action is positive or bounded below]`.
- `~00:54:23.000-~00:54:45.000`: raw: `this ... function as a functional ... bounded below`. Capture: positivity or lower boundedness is the reason for the sign convention.
- `~00:54:45.000-~00:55:06.000`: raw: `in this wick rotation procedure replacing T by minus I Tau and this exponential ... becomes e to the minus one over H bar the integral of the euclidean lagrangian`. `[ASR errors; likely: the weight is `e^{-S_E/hbar}`]`.
- `~00:55:06.000-00:55:32.880`: raw: `typically this guy ... positive or bounded From Below ... unlike the original ... for the real path ... phase oscillatory ... numerically important ... wildly fluctuating paths`. `[ASR errors; likely: real-time weights oscillate; Euclidean weights suppress]`.
- `00:55:32.880-00:55:45.549`: `[board gap]`.
- `00:55:45.559-00:55:59.339`: raw: `once you do this wick rotation it looks much better because now this guy here is going to be exponentially suppressed for wildly fluctuating paths ... dominated by the path that really have small values of the euclidean action`. Capture: Euclidean weighting suppresses high-action paths.
- `00:55:59.339-00:56:22.510`: `[board gap]`.
- `00:56:22.520-~00:56:39.000`: student question, raw: `like minus like if it's the magnets like ... the sign is correct`. `[ASR errors; likely: asks about the sign in `L_E` or the exponent]`.
- `~00:56:39.000-~00:56:59.000`: lecturer answer, raw: `this side here is important ... I have to find the sign ... this L is minus L e ... this one is ... so the sign is correct`. `[ASR errors]`.
- `~00:56:59.000-~00:57:13.000`: raw: `euclidean action it differs from the usual connection of the action Better Sound ... I don't listen`. `[uncertain: a follow-up clarification about how the Euclidean action differs from the ordinary action]`.
- `~00:57:13.000-~00:57:30.000`: raw: `all right so um ... with that ... if you want to calculate this ... version related version of this two-point function`. `[ASR errors; likely: calculate the Euclidean correlator]`.
- `~00:57:30.000-~00:58:14.000`: raw: `we can just use the nuclear version ... replace ... integration range ... from minus T ... then take limit ... to Infinity ... result ... well defined ... actual ... two-point functions`. `[ASR errors; likely: integrate over `[-T,T]` and take `T` to infinity]`.
- `~00:58:14.000-~00:58:27.000`: raw: `okay ... any questions yeah`. Q and A prompt.
- `~00:58:27.000-00:58:52.129`: student question, raw: `in general we're going to perform a work rotation ... path integral ... in order to get back to our actual measurable ... find ... analytic ... equals`. `[ASR errors; likely: asks how to recover real-time measurable correlators from Euclidean data]`.

### `00:58:52.130-~01:01:44.000` - recovery of real-time data, QFT scope, and operator ordering, pages 28-29

- `00:58:52.130-~00:59:20.000`: lecturer answer, raw: `you can extract this identity levels ... without having to explicit ... information ... easier ... actual energy levels`. `[ASR errors; likely: Euclidean data can yield energy levels without directly reconstructing every real-time detail]`.
- `~00:59:20.000-00:59:38.160`: raw: `this is not just ... abstract mathematics ... computations of actual energy levels`. Capture: the analytic continuation and Euclidean calculation have a computational interpretation.
- `00:59:38.160-01:00:17.040`: raw: `but in both ... simple model but also later in actual ... Theory ... these kind of quality functions are expected to have a nice energy property ... provided ... filtering is actually defined ... in a non-portrait defined Financial Theory such as Quantum ... Dimension or 5433 Dimension ... QED it will not quite be well defined ... only defined ... perturbation theory ... pathologies`. `[ASR errors; likely: nonperturbatively defined field theories have well-behaved correlators; QED is treated perturbatively here and has associated pathologies]`.
- `01:00:17.040-01:00:28.390`: `[board gap]`; then raw: `any other questions`.
- `01:00:28.390-~01:00:46.000`: student question, raw: `what if the two operators ...`. Capture: asks about changing the ordering of the two operators.
- `~01:00:46.000-~01:01:03.000`: lecturer answer, raw: `you see ... this is ... you don't get to choose the water okay so so the water is specified`. `[ASR errors; likely: the ordering is specified by the written expression]`.
- `~01:01:03.000-01:01:14.400`: raw: `so far ... I'm always going to be in a specific ordering ... in fact for this euclidean version`. `[ASR errors]`. Capture: fixes the ordering for the current derivation.
- `01:01:14.400-01:01:23.930`: `[board gap]`.
- `01:01:23.940-~01:01:37.000`: raw: `if you switch q0 and Q on one side now ... You Might be in trouble because that's like negative ...`. `[ASR errors; likely: reversing the order corresponds to negative Euclidean time or a different correlator]`.
- `~01:01:37.000-~01:01:47.000`: raw: `what we'll discuss later ... recover ... functions with arbitrary ordering but for now the order is as expected`. `[ASR errors; likely: other orderings will be treated later]`.
- `~01:01:47.000-~01:02:00.000`: raw: `any other questions ...` followed by a question about the variation step. `[ASR errors; Q and A interval]`.
- `~01:02:00.000-~01:02:50.000`: raw: `in this case it's always ...` `[uncertain]`. The track returns to the path-integral calculation.

### `~01:02:50.000-01:07:17.280` - evaluating the measure by mode expansion, pages 29-30

- `~01:02:50.000-~01:03:10.000`: raw: `um all right ... next we're going to discuss how to actually evaluate the pathway ... writing this ... are we just pulling ourselves or does this actually ... useful for computation`. `[ASR errors; likely: asks whether the path-integral expression is useful for calculation]`.
- `~01:03:10.000-~01:03:30.000`: lecturer answer, raw: `you can always go back to this ... real ... version like last lecture ... just do that and then ... not really gain anything ... somehow like to do a little better`. `[ASR errors; likely: returning to the real-time formulation gives no computational gain; the Euclidean or mode formulation is sought]`.
- `~01:03:30.000-~01:03:46.000`: raw: `once we decide this integration is supposed to be integration over path ... in time or imaginary time ... different ways to parametrize the space of functions`. `[ASR errors; likely: choose coordinates on the space of paths]`.
- `~01:03:46.000-~01:04:11.000`: raw: `like last time ... discretizing time ... every time we have one variable ... better things ... Fourier transform in time ... Fourier expansion of Q of T`. Capture: use Fourier modes instead of time-slice variables.
- `~01:04:11.000-~01:04:38.000`: raw: `instead of working Q at a longer time you go to frequency space ... instead of integration Q at every time integrate over the Fourier modes of every frequency ... much more convenient for computations`. `[ASR errors; likely: mode variables make the functional integral more convenient]`.
- `~01:04:38.000-~01:05:12.000`: raw: `this way of thinking about the path ... integration of the Fourier modes is much more convenient for doing ... preservation Theory`. `[ASR error; likely: perturbation theory]`. Page match: p29 mode expansion and p30 example setup.
- `~01:05:12.000-~01:05:31.000`: `[board gap]`, then `so to evaluate ... key ... find a convenient and also regularized expression of the measure let's DQ`. `[ASR errors; likely: need a convenient regularized expression for `[Dq]`]`.
- `~01:05:31.000-~01:05:49.000`: raw: `okay so ... work in some kind of a frequency space ... expand this on some ... bases or functions ... q_n and f_n`. `[ASR errors; likely: expand `q(tau)` in basis functions `f_n(tau)` with coefficients `q_n`]`.
- `~01:05:49.000-~01:06:28.000`: raw: `the naive ... you might imagine that you can replace this integration in the function field ... by the integration in the ... conditions ... functions ... modes`. `[ASR errors; likely: naive measure `[Dq] = product dq_n` is being proposed]`.
- `~01:06:28.000-~01:06:42.000`: raw: `now of course this will still be ... integral ... imagine not getting this on a large ...`. `[uncertain]`; `[board gap]` near the cutoff discussion.
- `~01:06:42.000-~01:07:00.000`: raw: `okay so that's something that one might attempt to do ... any questions`. Q and A prompt about the measure.
- `~01:07:00.000-01:07:17.280`: raw: `well that is this question mark here ... you don't know that ... [Music]`. Capture: the naive mode measure is explicitly left with a question mark; a normalization or Jacobian is not automatic.

### `01:07:17.280-01:10:03.299` - measure qualification and harmonic-oscillator example, pages 29-30

- `01:07:17.280-~01:07:35.000`: raw: `by this gaussian ... all right so so that will become contributed to this measure now in some people situation this will actually be true after some constant normalization`. `[ASR errors; likely: a Gaussian calculation can justify the product measure up to a constant in some cases]`.
- `~01:07:35.000-~01:07:54.000`: raw: `but that may not always be the case ... this will come back ... one example ...`. Capture: the measure issue is model-dependent.
- `~01:07:54.000-~01:08:06.000`: raw: `the ... reason ... locality ... as I emphasize in the first lecture ... specializer in quantum mechanics ... ambiguities ... resolved`. `[ASR errors; likely: locality or the structure of quantum field theory constrains some ambiguities]`.
- `~01:08:06.000-01:08:15.480`: raw: `one of the simplest examples of one mechanical models with the increasing level of sophistication ... okay so we're gonna first discuss the harmonic acid`. `[ASR error; likely: harmonic oscillator]`. Capture: transition to the explicit oscillator example.
- `01:08:15.480-01:08:17.359`: raw: `um okay so`.
- `01:08:17.359-~01:08:35.000`: raw: `example one is just the harmonic the quantum harmonic oscillator ... the hamiltonian is ... p squared plus Omega squared q squared over two`. `[ASR errors; likely: `H=(p^2+omega^2 q^2)/2`]`. Page match: p30.
- `~01:08:35.000-~01:08:54.000`: raw: `and then ... at the classical level ... lagrangian ... one half q dot squared minus the potential ... omega squared Q squared`. `[ASR errors; likely: `L=1/2 qdot^2-1/2 omega^2 q^2`]`.
- `~01:08:54.000-~01:09:17.000`: raw: `we are going to investigate this kind of a two point ... function of Interest ... from the undergrad ... ground state ... Q is just a position operator ... calculate this explicit but we're going to go through this painful process using path people`. `[ASR errors; likely: the oscillator correlator is familiar from undergraduate quantum mechanics; the lecture computes it through the path integral]`.
- `~01:09:17.000-01:10:03.299`: raw: `and to do that ... consider the wick rotating version ... starting with ... calculating things like integral DQ of e to the minus one ... action with some insertion into this ... if you're interested in two point`. `[ASR errors; likely: use the Euclidean path integral with insertions]`.

### `01:10:03.300-01:13:47.228` - finite interval and Fourier sine basis, pages 30-31

- `01:10:03.300-~01:10:41.000`: raw: `so in fact I want to do this example as explicitly impossible and so we're actually going to choose boundary condition ... take this action to be the integral of this euclidean version of lagrangian from ... minus T to T`. `[ASR error; likely: “as explicitly as possible”]`. Capture: finite interval `[-T,T]` is introduced.
- `~01:10:41.000-~01:11:06.000`: raw: `the boundary ... is not going to actually matter in the limit T to Infinity but it will be a step for now ... start by taking ... finite`. `[ASR errors; likely: endpoints are a temporary finite-interval device; their effect drops out as `T -> infinity`]`.
- `~01:11:06.000-~01:11:22.000`: raw: `we do want ... choose some boundary condition ... choose ... the boundary condition ... and imaginary time`. `[ASR errors]`.
- `~01:11:22.000-01:11:44.649`: raw: `with Q ... remember this now is rotated ... so ... Q of minus T is equal to zero and the Q of T is also zero`. `[ASR errors; likely: Dirichlet conditions `q(-T)=q(T)=0`]`. Page match: p30.
- `01:11:44.659-01:12:04.020`: raw: `now we're evolving ... in imaginary time ... from minus ... to ...` followed by the boundary drawing. `[ASR errors]`; `[board gap]` around the path sketch.
- `01:12:04.020-01:12:24.480`: raw: `given this constraint we can expand a general function on the four-year basis subject to this ... frame`. `[ASR errors; likely: Fourier basis subject to the Dirichlet endpoints]`.
- `01:12:24.480-01:12:45.679`: raw: `if you're now on the foyer basis in this case because of the boundary condition ... q and f n l and from one to Infinity ... choose this at ends ... proportional to the sign of n i Tau plus ...`. `[ASR errors; likely: sine basis satisfying the endpoints]`.
- `01:12:45.679-~01:13:01.000`: raw: `and so forth ... this is a complete basis of functions ... advantage ... hope you can distinguish my handwriting this is two which is not to be confused with now uh in this Tau`. `[ASR errors; likely: `T` and `tau` are visually distinct and must not be confused]`.
- `~01:13:01.000-01:13:12.199`: raw: `know this is a complete basis ... useful to normalize this ... one over square root T factor`. `[ASR errors; likely: normalize `f_n` with `1/sqrt(T)`]`.
- `01:13:12.199-01:13:47.228`: raw: `so far is a bit ad hoc ... let me tell you this a bit more precisely ... basis functions ... prescribed the boundary condition ... and orthonormal ... inner product ... integral from minus T to T ... f_n star f_m ...`. `[ASR errors; likely: state boundary conditions and orthonormality]`. Page match: p31.

### `01:13:47.229-~01:17:40.000` - orthonormality and diagonal Euclidean action, page 31

- `01:13:47.229-01:14:16.039`: raw: `for example ... inner product ... integral from ... and star ... this should be ...`. `[ASR errors]`. Capture: orthonormality is written as an inner product.
- `01:14:16.040-01:14:23.040`: raw: `prescribed the boundary condition ... and uh orthonormal`. Capture: the two properties of the basis are restated.
- `01:14:23.040-~01:14:40.000`: raw: `for the normal ... with respect to ... a ... it defines inner products ... functions`. `[ASR errors; likely: define the inner product on functions]`.
- `~01:14:40.000-01:15:10.560`: raw: `for example ... inner part ... integral from ... and star ...`. `[ASR errors]`; `[board gap]` around the normalization equation.
- `01:15:10.560-01:15:14.880`: raw: `any questions about this`. Q and A prompt before substituting into the action.
- `01:15:14.880-~01:15:35.000`: raw: `I'm just expanding ... in terms of this ... we can then write this ... include an action`. `[ASR errors; likely: substitute the mode expansion into `S_E`]`.
- `~01:15:35.000-01:15:52.219`: raw: `what's the equation in this example the integral from minus T to T one half ... squared plus one half Omega squared Q squared comes out right`. `[ASR errors; likely: `S_E=integral[-T,T] d tau [1/2 (partial_tau q)^2 + 1/2 omega^2 q^2]`]`.
- `01:15:52.219-~01:16:06.000`: raw: `remember ... go through your procedure and flip the overall sign this is our euclidean lagrangian`. `[ASR errors]`.
- `~01:16:06.000-01:16:25.080`: raw: `now you take that extension and plug it into here ... re-extend this action in terms of the q ... in terms of the q_n`. `[ASR errors; likely: express the Euclidean action in mode coefficients]`.
- `01:16:25.080-~01:16:35.000`: `[board gap]`.
- `~01:16:35.000-~01:16:57.000`: raw: `what is the action ... all the time ... let me just quickly state this ... I'll finish this next time`. `[ASR errors]`; capture: lecturer flags the calculation as the next continuation.
- `~01:16:57.000-~01:17:28.000`: raw: `it's very important ... plug it into the integral ... take this and stick into this entire ... multiply by another ... qn times qm ... integral ... non-zero only if n is equal to M`. `[ASR errors; likely: orthonormality makes the mode action diagonal, with `delta_nm`]`.
- `~01:17:28.000-~01:17:40.000`: raw: `the result ... sum over n ... q_n squared ... one half ... plus one half omega squared ... first term ... second term`. `[ASR errors; likely: `S_E = sum_n q_n^2/2 [(n pi/2T)^2+omega^2]`]`. Page match: p31 equation.

### `~01:17:40.000-01:20:30.799` - Gaussian factorization, next-lecture seam, and Euclidean interpretation

- `~01:17:40.000-~01:18:18.000`: raw: `right so ... whatever it is that you want ... something to start which you can study ... next time when I insert like some cues and from that we'll extract this quantity function`. `[ASR errors; likely: use the diagonal action to compute the correlator after inserting `q(tau)` and `q(0)`]`.
- `~01:18:18.000-01:18:48.300`: raw: `we're gonna compute by ... course integration over ... q_n ... product ... from one to Infinity ... action is just minus one over H bar sum ... one half of ... plus omega squared ... with whatever ... insertions that you want to put in`. `[ASR errors; likely: the functional integral factorizes into independent Gaussian mode integrals]`.
- `01:18:48.300-01:18:51.780`: raw: `gaussian integrals ... interested in insertion of additional cues`. `[ASR error; likely: additional q insertions]`.
- `01:18:51.780-01:18:59.699`: raw: `and unfortunately I don't have time now I will finish that calculation ... next time`. This is the explicit lecture handoff.
- `01:18:59.699-~01:19:10.000`: raw: `next time yes so let's give this away because we can follow each`. `[uncertain; likely: closes the board calculation]`.
- `01:19:10.580-~01:19:24.000`: raw: `that's correct that's correct so far ... this is the Ukrainian government now you see ... yeah that's correct`. `[ASR error; likely: student Q and A about the Euclidean construction; “Ukrainian government” is a caption failure]`.
- `~01:19:24.000-01:20:00.000`: raw: `if you might imagine ... in time ... worry ... instead of expanding ... positive base ... set up ... real-time ... weird time ... most of it is still in imaginary time Direction`. `[ASR errors; likely: the mode expansion remains well behaved because the contour has been arranged around imaginary time]`.
- `01:20:00.000-~01:20:20.000`: raw: `in a sense that this kind of a path ... in mechanics is always ... should always be viewed as ... imaginary time ... mathematically`. `[ASR errors; likely: for this calculation, regard the path integral mathematically as an imaginary-time path integral]`.
- `~01:20:20.000-01:20:30.799`: raw: `it's sort of the path people that this ... mathematically ... yes`. `[ASR errors]`; Q and A interval.

### `01:20:30.800-~01:22:43.000` - normalization, measure dependence, and Problem Set 2

- `01:20:30.800-~01:20:43.000`: raw: `good so uh first of all a first comment is that ... you could of course imagine ... normalization measure`. `[ASR errors; likely: comment on the normalization of the measure]`.
- `~01:20:43.000-~01:21:03.000`: raw: `that's one constant if you change by some constant ... ultimately I don't care about ... this it's going to cancel between the numerator and ... if I'm interested in the ... functions`. `[ASR errors; likely: an overall measure normalization cancels in normalized correlators]`.
- `~01:21:03.000-~01:21:13.000`: raw: `you might worry about the dependence ... it depends on ... that could be bad`. `[ASR errors; likely: a nonconstant Jacobian or measure dependence could affect the result]`.
- `01:21:13.860-~01:21:38.000`: raw: `that now did not happen in this example ... the purpose of a problem Set ... problem two ... just posted is precisely to let you study this ... similar but actually even simpler ... example`. `[ASR errors; likely: Problem 2 studies measure or Jacobian dependence in a simpler example]`. Page match: Problem Set 2, p64 onward.
- `~01:21:38.000-~01:21:50.000`: raw: `if you use ... time regularization as we had ... last time ... when we derived from Hamilton ... no ambiguity`. `[ASR errors; likely: time-lattice regularization fixes the measure inherited from the Hamiltonian derivation]`.
- `~01:21:50.000-~01:22:12.000`: raw: `in this case ... we don't know what the matter is ... going from this q_n to those Q ... different variables ... factor`. `[ASR errors; likely: a change of variables can bring a Jacobian]`.
- `~01:22:12.000-~01:22:29.000`: raw: `I'm not going to discuss that right now ... that Jacobian factor even was a remark at the end of the P set ... extra credit part ... not even required`. Capture: Jacobian factor is extra credit on Problem Set 2.
- `~01:22:29.000-~01:22:43.000`: raw: `it's really some aspects of ... you'll see that it's not always trivial sometimes you have to keep track ... but in this example ... no actual non-trivial dependence`. `[ASR errors; likely: Jacobians can be nontrivial, though this example has no nontrivial dependence]`.

### `~01:22:43.000-01:25:00.620` - all functions, rigor of the measure, and final Q and A

- `~01:22:43.000-~01:22:55.000`: student question, raw: `well the limits ... put it ... you're integrating over all possible functions here`. `[ASR errors; likely: asks what the integration symbol means and whether it ranges over all functions]`.
- `~01:22:55.000-~01:23:10.000`: lecturer answer, raw: `I'm sorry I mean these four amounts are under strength ... in this case real errors is`. `[ASR errors; likely: finite cutoff or finite-mode regularization is understood before taking the continuum limit]`.
- `~01:23:10.000-01:23:28.080`: `[board gap]` followed by a second question.
- `01:23:28.080-~01:24:17.000`: student question, raw: `that depends on what you want to get out of it ... regularization I did last time is a way to make it rigorous ... may not preserve all the problems ... the ... that we've been talking about is that like a well-defined ... space on the space of the path ... actual space of the functions`. `[ASR errors; likely: asks whether the functional measure can be defined rigorously on a space of functions]`.
- `~01:24:17.000-01:24:39.360`: lecturer answer, raw: `that depends I believe a simple cases at least in the gaussian case if it actually can be made ... rigorous on the space of functions ... this is not something I will get into in this class ... in practice ... almost never used in physics`. `[ASR errors; likely: Gaussian cases can be made mathematically precise; the general measure-theoretic construction is outside the course and is rarely used explicitly in physics]`.
- `01:24:39.360-01:24:51.600`: raw: `applications but for these are very simple models it can be made precise ... but for our purpose we're always going to think about this ... as defined through regularization we're not going to try to ... consider some ... measure on some organizations facing functions`. `[ASR error; likely: “measure on some function space”]`. Capture: the working definition throughout the course is through regularization.
- `01:24:57.239-01:25:00.620`: raw: `uh any other questions`. Final Q and A prompt. No answer is captioned after it.
- `01:25:00.620-01:25:28.000`: no recoverable caption. Video metadata continues for approximately 27.380 seconds.

## Caption-gap and board-transition register

The following are all start-to-start gaps longer than eight seconds in the JSON3 text-event sequence. They identify board writing, diagrams, pauses, or audio loss. A gap is not treated as proof of a particular board action unless the neighboring captions and page render support it.

| interval | source-capture note |
|---|---|
| `00:03:54.780-00:04:05.159` | energy-level or correlator formula; preceding raw cue is `performance` |
| `00:04:38.400-00:04:55.020` | ground-state correlator and notation board |
| `00:07:04.680-00:07:17.529` | energy-basis derivation |
| `00:07:54.300-00:08:11.710` | spectral sum |
| `00:08:11.720-00:08:33.170` | spectral sum and exponential factors |
| `00:08:33.180-00:08:48.829` | spectral sum; raw speech resumes with `if it's okay is then not equal to sum` |
| `00:08:59.180-00:09:12.290` | spectral expression |
| `00:09:12.300-00:09:29.630` | spectral expression |
| `00:09:29.640-00:09:47.870` | final spectral board before question |
| `00:15:54.120-00:16:11.889` | convergence or complex-plane diagram |
| `00:16:35.399-00:16:45.170` | complex-plane board |
| `00:26:26.640-00:26:46.310` | ground-state projection formula |
| `00:28:07.320-00:28:16.430` | projection or normalization board |
| `00:29:50.940-00:30:00.070` | complex-time contour |
| `00:32:22.919-00:32:35.269` | transition from contour to imaginary-time formula |
| `00:33:14.940-00:33:52.730` | imaginary-time correlator formula |
| `00:36:23.400-00:36:34.910` | path-integral motivation board |
| `00:37:35.820-00:38:11.270` | path-integral representation and Q prompt |
| `00:40:42.420-00:40:59.829` | inserted path integral |
| `00:41:55.380-00:42:12.109` | action and insertion notation |
| `00:48:13.619-00:48:24.069` | inserted-operator derivation |
| `00:49:35.520-00:49:54.050` | operator versus c-number distinction |
| `00:51:16.920-00:51:26.750` | Wick-rotation derivative substitution |
| `00:52:12.720-00:52:32.329` | Euclidean action sign |
| `00:55:32.880-00:55:45.549` | Euclidean-weight discussion |
| `00:55:59.339-00:56:22.510` | sign question and board |
| `00:58:38.160-00:58:52.129` | QFT-scope transition |
| `01:00:17.040-01:00:28.390` | operator-ordering Q prompt |
| `01:01:14.400-01:01:23.930` | ordering board |
| `01:04:32.880-01:04:42.170` | Fourier or measure board |
| `01:05:36.299-01:05:49.250` | mode-measure question |
| `01:05:53.690-01:06:04.569` | mode-measure board |
| `01:07:17.280-01:07:26.170` | Gaussian measure qualification |
| `01:07:42.000-01:07:53.589` | locality or ambiguity qualification |
| `01:07:57.900-01:08:15.470` | transition to oscillator example |
| `01:11:22.500-01:11:44.649` | endpoint drawing and Dirichlet condition |
| `01:12:35.699-01:12:45.669` | Fourier sine basis |
| `01:13:33.600-01:13:47.229` | basis normalization and orthonormality |
| `01:18:33.179-01:18:44.830` | action coefficient or Gaussian setup |
| `01:19:15.780-01:19:26.290` | Q and A after the handoff |
| `01:20:20.820-01:20:29.169` | Euclidean interpretation |
| `01:22:58.199-01:23:26.510` | all-functions measure question |
| `01:24:21.380-01:24:31.630` | rigor question |

## Adjacent-lecture overlap notes

- The Sep. 6 recording `96lN2omwit4` is the source-order predecessor. Its late captions discuss the Lagrangian path integral, integration over momentum, regularization, and measure ambiguity. Those topics correspond to rendered pages 21-25. The Sep. 8 recording begins after that derivation, with the spectral correlator on p26. The title page p20 is a divider rather than a spoken opening in this video.
- The Sep. 13 recording `M0py5a4RWhE` is the source-order successor. Its opening says it will finish the previous calculation and returns to the Fourier basis, Euclidean action, mode coefficients, and Gaussian integrals. That is a direct handoff at p31. The Sep. 8 recording's final mode action is therefore a possible overlap point, while the actual Gaussian correlator calculation belongs to the next recording.
- The homework references at `01:05-01:07` and `01:20-01:22` point to Problem Set 2, rendered pages 63-67. They are logistics and qualification references, not evidence that the problem-set pages were lectured in this recording.
- Page 68 starts Chapter 3. The Sep. 8 caption track contains no recoverable “Relativistic Particles,” field, or Green-function chapter transition. The recorded subject ends inside the Chapter 2 harmonic-oscillator path-integral calculation.

## Capture status

The target lane contains the complete caption-track audit, the sourcebook page-order map for pages 20-68, the exact recoverable Chapter 2 boundary, the full chronological inventory through the final Q prompt, raw wording with recognition flags, page-linked equation references, Q and A intervals, logistics, board gaps, and adjacent-lecture overlap evidence. No caption text was polished or rewritten in the source tracks. No canonical LaTeX or existing project file was edited.
