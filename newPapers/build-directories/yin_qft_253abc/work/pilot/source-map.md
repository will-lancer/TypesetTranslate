# Pilot source map

Observed on 2026-08-08 in America/Los_Angeles.

## Source checks

- The combined source is `/Users/wlancer/Desktop/IAS/phy/qft/qft_253abc_book.pdf`.
- Its SHA-256 is `9e5e4d241fffffa56c1c3df6dce4b83178f75787dd5d794a18c5d0c087769f21`, which matches `SOURCE_MANIFEST.yaml`.
- `pdfinfo` reports 786 physical pages.
- Physical pages 6--14 render as original Physics 253a note pages 1--9. Physical page 20 renders as the section divider “Lagrangian Quantum Mechanics, Path Integrals, and Perturbation Theory.”
- The playlist query returned 79 positions and 78 unique video IDs. Video `1CDPLddV8B0` occurs at positions 13 and 42.
- The observed playlist title is “QFT lectures.” YouTube reports the playlist as unlisted, with Xi Yin as channel owner and 2023-12-22 as the playlist modified date.
- `work/pilot/playlist.jsonl` contains one observation record followed by 79 item records. Each item includes playlist position, video ID, recording-title timestamp, title resolution, flat-playlist duration, observed view count, channel metadata, URL, and access result.

## Frozen pilot decision

The Chapter 1 lecture is [`OY_napMPywE`](https://www.youtube.com/watch?v=OY_napMPywE), titled `GMT20220901 172926 Recording 640x360`.

| Use | Exact interval | Disposition |
|---|---:|---|
| Section lead-in | `00:04:52.520--00:05:02.579` | Yin says “so let’s get started.” Keep as optional lead-in. |
| Combined PDF pp. 6--14, original note pp. 1--9 | `00:05:02.580--01:19:47.090` | Freeze as the core Chapter 1 transcript interval. The final words are “using the Lagrangian language.” |
| Clear construction Q&A | `01:19:47.100--01:20:13.920` | Preserve as relevant Q&A for the scalar field operator and its later systematic construction. |
| Weak room audio | `01:20:13.920--01:20:35.999` | Preserve raw and leave unresolved pending listening review. |
| Candidate post-class Q&A | `01:20:36.000--01:21:26.360` | Preserve provisionally. Audio and frame review must settle its content and disposition. |
| Post-lecture tail | after `01:21:26.360` | Outside the section. The recording contains teardown, room noise, and isolated caption fragments. |

Item-level YouTube metadata gives `OY_napMPywE` a duration of 5494 seconds, displayed as 1:31:34, an upload date of 2023-05-04, and unlisted availability. The downloaded format-18 file has duration 5494.282449 seconds. The flat playlist rounded the duration to 5495 seconds.

The next lecture is [`96lN2omwit4`](https://www.youtube.com/watch?v=96lN2omwit4), titled `GMT20220906 173002 Recording 640x360`. After logistics, Yin says at `00:01:26.700` that this lecture and the next couple of lectures concern the Lagrangian formalism for quantum mechanics. At about `00:01:40`, the board visibly reads “Lagrangian formulation for QM.” This matches the physical-page-20 divider and fixes the external end boundary for Chapter 1.

## Page and topic alignment

All timestamps in this table refer to `OY_napMPywE`. Caption wording supplies the oral cue. Rendered note pages and sampled video frames supply the equation and board evidence.

| PDF page | Note page | Best aligned interval | Source evidence | Confidence |
|---:|---:|---:|---|---|
| 6 | 1 | `00:05:02.580--00:19:14.418` | At `00:05:02.580`, Yin asks “What is quantum field theory?” He answers with quantum mechanics plus locality, then distinguishes local or UV-complete QFT from effective field theory. A `00:05:15` frame shows “What is QFT?” and “A: QM + locality.” Later speech and the board cover local field operators, microcausality, effective-field-theory examples, and renormalizability. | high |
| 7 | 2 | `00:19:14.419--00:27:19.619` | Yin announces the course plan at `00:19:14.419`. He covers Lagrangian quantum mechanics, path integrals, regularization, perturbation theory, Feynman diagrams, renormalization and counterterms, relativistic particles and fields, Green functions, asymptotic states, the S-matrix, LSZ, spin, QED, and applications. A `00:27:39` frame displays the relativistic-particles-and-fields list and the start of the Hilbert-space prelude. | high |
| 8 | 3 | `00:27:19.620--00:37:24.779` | Yin motivates the question “why do we need field theory to describe the quantum mechanics of particles with relativistic symmetry?” He introduces the Hilbert space, vacuum, one-particle momentum states, the relativistic dispersion relation, noninteracting multiparticle states, and creation and annihilation operators. At `00:37:24`, the board shows the Hilbert-space and relativistic-particle equations. | high |
| 9 | 4 | `00:37:24.780--00:48:12.899` | Yin constructs multiparticle states with creation operators, fixes the commutator and delta-function normalization, writes the free Hamiltonian with the occupation-number operator, and adds candidate interaction monomials. The closing board line reads “Issue: not easy to find `H_int` that respects relativistic sym.” A `00:48:13` frame captures this line together with `H=H_0+H_{int}`. | high |
| 10 | 5 | `00:48:12.900--00:55:29.999` | Yin names causality as the issue, draws the light cone, excludes superluminal propagation, and represents a local disturbance by `\hat\phi(x)`. He stresses that `x^\mu` labels operators and remains a parameter. He then requires field operators at transformed spacetime points to be related by Poincare symmetry. A `00:55:30` frame shows the light-cone diagram and the `\hat\phi(x)` board text. | high |
| 11 | 6 | `00:55:30.000--01:11:54.178` | Yin writes `x'^\mu=\Lambda^\mu{}_{\nu}x^\nu+a^\mu`, uses the mostly-plus metric, realizes the symmetry by `U(\Lambda,a)`, and gives `U\hat\phi(x)U^{-1}=\hat\phi(\Lambda x+a)`. He expands the infinitesimal transformation in `\hat P_\mu` and `\hat J^{\mu\nu}`, identifies their meanings, and discusses the Poincare commutators. Frames at `01:11:54` show the transformation law, infinitesimal generators, and commutator algebra on the board. | high |
| 12 | 7 | `01:11:54.179--01:18:04.738` | Yin introduces microcausality at `01:11:54.179`, states the spacelike-separation condition, writes the free `H` and `\vec P`, and asks for a local field operator in the free-particle model. He then writes the free scalar expansion in creation and annihilation operators. Frames at `01:17:00` and `01:19:26` show the momentum generators and scalar-field expansion. | high |
| 13 | 8 | `01:18:04.739--01:18:43.999` | Yin says that he lacks time to explain the displayed scalar construction, invites the class to think about it, and states that it transforms correctly and obeys microcausality. The final seconds contain a pause and board transition. The note page supplies the invariant on-shell integral and the odd-integrand proof. The recording omits that written derivation. | medium for topic; notes-only for the displayed derivation |
| 14 | 9 | `01:18:44.000--01:19:47.090` | Yin returns to interacting systems with microcausality. He explains that Hamiltonian language singles out time, which obscures Poincare symmetry, then asks for a formulation where the symmetry is manifest. At `01:19:37.860`, he says the Lagrangian formalism will be useful. At `01:19:39.480`, he announces that the next lecture will formulate quantum mechanics in Lagrangian language. His final phrase ends immediately before the Q&A preamble at `01:19:47.100`. The note page supplies the compact postulate list. | high for the closing bridge; notes-only for the compact list |

The page intervals meet at topic changes in the speech. Chalkboard contents persist across adjacent intervals, so a sampled frame can display material from the preceding board while Yin begins the next topic.

The JSON3 captions use rolling cues. The value `01:19:43.920` is the start of the final cue, while the next speech cue begins at `01:19:47.100`. The core endpoint is therefore `01:19:47.090`. The 10 ms separator carries no speech. The p. 12 endpoint similarly meets the p. 13 cue at `01:18:04.739`. The pause from the end of the p. 13 statement through `01:18:43.999` stays with p. 13 as a board transition.

## Final Q&A disposition

| Interval | Evidence | Required handling |
|---:|---|---|
| `01:19:47.100--01:20:13.920` | A student asks how to construct the scalar operator. Yin says he has produced it “out of the hat” for the motivation, that one can check it, and that later lectures will construct it systematically. | Include as relevant Q&A for note pp. 7--9. |
| `01:20:13.920--01:20:35.999` | The room audio and autogenerated captions are weak; the captions emit music markers. | Preserve raw audio/captions and mark unresolved until listening review. |
| `01:20:36.000--01:21:26.360` | The surviving captions mention many operators with similar properties, consistent with a possible follow-up about nonuniqueness. | Keep as candidate post-class Q&A. Clean and include only after audio and frame review. |
| after `01:21:26.360` | Classroom teardown and isolated caption fragments. | Mark outside section. |

## Candidate and access log

Playlist order differs from recording-title chronology. The first five 2022 dates were nominated before content matching. The 2023 restart was checked because it begins a later playlist block.

| Video ID | Recording title date | Material examined | Result |
|---|---:|---|---|
| `OY_napMPywE` | 2022-09-01 | Flat and item metadata, English VTT and JSON3 autogenerated captions, full 640x360 video, timestamped frames | Exact Chapter 1 match. |
| `96lN2omwit4` | 2022-09-06 | Flat and item metadata, English VTT and JSON3 captions, 00:01:20--00:03:00 video segment, timestamped frames | External boundary. It opens Lagrangian quantum mechanics. |
| `uzixOflp0tY` | 2022-09-08 | Flat metadata, English VTT and JSON3 captions | Later lecture. At `00:02:50.879`, Yin says he is continuing the prior Lagrangian-formalism discussion and moves to ground-state correlation functions. |
| `M0py5a4RWhE` | 2022-09-13 | Flat metadata, English VTT and JSON3 captions | Later lecture. It opens by finishing a prior path-integral calculation and discusses the oscillator functional integral. |
| `vk_RlYUKUyM` | 2022-09-15 | Flat metadata, English VTT and JSON3 captions | Later lecture. It continues a Gaussian path-integral calculation and its Green function. |
| `8CEATsoohDk` | 2023-09-05 | Flat and item metadata, English JSON3 captions | Different course block. Yin calls it QFT 3 at the opening and addresses students from his QFT 1 and 2 courses in the previous academic year. |

The first sandboxed playlist request failed because DNS could not resolve `www.youtube.com`. The approved network retry succeeded. All six item queries in the table succeeded. YouTube supplied autogenerated English captions for each queried item.

## Residual source issues

- Original note page 8, combined PDF page 13, contains a complete microcausality integral that the matched lecture only asserts and assigns for thought. The equation must come from the rendered note.
- Original note page 9, combined PDF page 14, compacts the Hilbert-space, Poincare, vacuum, field-operator, covariance, and microcausality assumptions into a postulate list. The lecture develops these assumptions across earlier intervals and omits a final list recitation.
- Formula-bearing autogenerated captions contain recognition errors such as “microcontality,” “Conqueror symmetry,” and “lagrangian populism.” Timestamps remain useful. Equations require the notes or clear frames.
- Flat-playlist view counts are observation-time metadata. Several positions returned a null view count.
