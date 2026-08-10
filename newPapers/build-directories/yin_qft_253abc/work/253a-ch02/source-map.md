# Source map: Physics 253a, Chapter 2

Status: Pass 1 reconciled; transcript freeze pending

## Scope

Chapter 2 is “Lagrangian Quantum Mechanics, Path Integrals, and Perturbation
Theory.” The combined source is
`/Users/wlancer/Desktop/IAS/phy/qft/qft_253abc_book.pdf`, SHA-256
`9e5e4d241fffffa56c1c3df6dce4b83178f75787dd5d794a18c5d0c087769f21`.
Physical page 20 is the chapter divider. Original handwritten note pages 10
through 51 occupy physical pages 21 through 62.

Physical pages 63 through 67 are Problem Set 2. They are reserved for later
assignment integration. Physical page 68 is the divider for “Relativistic
Particles, Fields, and Green Functions.”

Timestamp intervals use the half-open convention `[start,end)`. The times below
come from JSON3 cue starts, checked against the VTT tracks and targeted source
video frames.

## Exact lecture set

The playlist order is not chronological. Recording dates establish the six
lectures that cover the chapter.

| Order | Date | Video | Chapter 2 interval | Notes | Physical pages |
|---:|---|---|---|---:|---:|
| 1 | 2022-09-06 | `96lN2omwit4` | `[00:01:26.700, 01:20:25.500)` | 10--14 | 21--25 |
| 2 | 2022-09-08 | `uzixOflp0tY` | `[00:02:50.879, 01:19:02.520)` | 15--20 | 26--31 |
| 3 | 2022-09-13 | `M0py5a4RWhE` | `[00:00:02.340, 01:23:02.640)` | 21--28 | 32--39 |
| 4 | 2022-09-15 | `vk_RlYUKUyM` | `[00:00:12.660, 01:18:28.140)` | 29--37 | 40--48 |
| 5 | 2022-09-20 | `3VG2kDHso08` | `[00:01:10.080, 01:18:54.780)` | 38--44 | 49--55 |
| 6 | 2022-09-22 | `TtMNnZ8__UU` | `[00:00:14.179, 00:51:10.020)` | 45--51 | 56--62 |

The first interval begins when Yin says that the lecture and the next couple of
lectures concern the Lagrangian formalism for quantum mechanics. The board title
“Lagrangian formulation for QM” is visible during the same opening sequence.

The intervals record the main chapter-bearing run in each lecture. Full caption
tracks remain in the source packet. Logistics, closing questions, caption tails,
and post-class fragments receive explicit transcript dispositions in Pass 2.

## Lecture transitions

`96lN2omwit4` develops the Lagrangian and Hamiltonian descriptions, quantum time
evolution, the transition kernel, time slicing, the phase-space path integral,
and the measure obtained by integrating the momenta. Its late caption tail
contains further discussion of the same Gaussian momentum integral. That tail
is retained as supplemental evidence outside the main classroom interval.

`uzixOflp0tY` starts the ground-state two-point function at `00:02:50.879`.
It gives the spectral decomposition, analytic continuation, Wick rotation,
ground-state projection, the Euclidean path integral, and the harmonic
oscillator Fourier basis. At `01:18:59.699`, Yin says the calculation will be
finished next time.

`M0py5a4RWhE` opens by finishing that oscillator calculation. It then derives
finite-dimensional Gaussian identities, Wick contractions, the functional
Gaussian integral, and the inverse differential operator that defines the
Green function.

`vk_RlYUKUyM` recalls the functional Gaussian calculation at `00:00:12.660`.
It introduces the anharmonic oscillator, expands the partition function,
organizes Wick contractions into graphs, proves connected-graph exponentiation,
and extracts the ground-state energy. Its next-lecture cue reaches
`01:18:28.140`.

`3VG2kDHso08` resumes the Euclidean two-point function at `00:01:10.080`.
Disconnected factors cancel against the denominator. The remaining graphs lead
to self-energy, one-particle-irreducible insertions, the pole of the exact
propagator, and the energy gap. Its closing material introduces a coordinate
redefinition and the associated ordering ambiguity.

`TtMNnZ8__UU` begins the derivative-interaction example at `00:00:14.179`.
The lecture traces a divergent derivative contraction through momentum cutoff
regularization, a counterterm, the finite counterterm ambiguity, and the
physical energy gap. Page 62 closes with the stronger restrictions supplied by
Poincare symmetry and microcausality in QFT.

## Chapter 2 end boundary

The final lecture contains both the Chapter 2 close and the first Chapter 3
prelude.

| Role | Interval or cue | Evidence |
|---|---|---|
| Final page-62 claim | through `00:50:15.599` | Finite counterterms in QFT are restricted by Poincare symmetry and microcausality. |
| Oral close cue | `[00:50:22.579, 00:50:29.280)` | Yin says that the quantum-mechanics material is finished and that the class is ready to do field theory. |
| Closing recap | `[00:50:29.280, 00:51:10.020)` | Regularization, counterterms, and the field-theory continuation are recapped. |
| Chapter 3 bridge begins | `00:51:10.020` | “But before that” begins the move to classical field theory. |
| First explicit Chapter 3 topic | `00:51:15.660` | “A few words at least about classical field theory.” |

The operational Chapter 2 endpoint is therefore `TtMNnZ8__UU:00:51:10.020`.
It retains the closing recap and excludes the sentence that opens the classical
field-theory prelude. Physical page 68 supplies the matching written divider.

The next recording, `82__84nYd4I`, begins sustained Chapter 3 material at
`00:00:26.119` with a spacetime action for fields. `ph3wE8cFMmk` continues the
same chapter. Both tracks are retained only as boundary evidence for this
packet.

## Page allocation

| Physical pages | Original note pages | Primary source sequence |
|---:|---:|---|
| 20 | none | Chapter divider |
| 21--25 | 10--14 | Lagrangian and Hamiltonian mechanics; transition kernel; phase-space path integral; measure |
| 26--31 | 15--20 | Spectral correlator; Wick rotation; Euclidean formulation; oscillator modes |
| 32--39 | 21--28 | Oscillator Green function; Gaussian identities; functional integral |
| 40--48 | 29--37 | Anharmonic oscillator; diagrams; connected graphs; vacuum energy |
| 49--55 | 38--44 | Two-point function; self-energy; one-particle irreducibility; exact pole |
| 56--62 | 45--51 | Derivative interaction; cutoff; counterterm; energy gap; finite ambiguity |
| 63--67 | none | Problem Set 2, deferred |
| 68 | none | Chapter 3 divider, boundary evidence only |

Every handwritten page has a dedicated source-capture report under
`work/253a-ch02/source-lanes/`. The exact page map is stored in
`work/253a-ch02/chapter-metadata.json`.

## Evidence ledger

- Playlist inventory: `work/253a-ch02/playlist.jsonl`
- Machine-readable chapter identity: `work/253a-ch02/chapter-metadata.json`
- Chronology reconciliation: `work/253a-ch02/source-lanes/playlist-chronology.md`
- End-boundary reconciliation: `work/253a-ch02/source-lanes/boundary-assignment.md`
- Complete lecture inventories: `work/253a-ch02/source-lanes/video-*.md`
- Exact page captures: `work/253a-ch02/source-lanes/notes-*.md`
- Raw caption tracks: `work/253a-ch02/captions/`
- Raw six-lecture anthology: `work/253a-ch02/transcript.raw.vtt`
- Targeted boundary frames: `tmp/pdfs/253a-ch02-video-boundary/`

The two outside-scope continuation videos and physical pages 63 through 68 have
no Chapter 2 drafting disposition. They establish the assignment and next-
chapter boundaries.
