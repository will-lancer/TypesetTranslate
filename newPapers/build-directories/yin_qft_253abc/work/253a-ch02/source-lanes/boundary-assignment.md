# Pass 1 boundary assignment

## Binding basis

The six binding project documents were read in full:

1. SOURCE_MANIFEST.yaml
2. AGENT_POLICY.md
3. WRITING_STYLE.md
4. WORKFLOW.md
5. CHAPTER_PLAN.md
6. MASTER_PROMPT.md

Source PDF: /Users/wlancer/Desktop/IAS/phy/qft/qft_253abc_book.pdf
SHA-256: 9e5e4d241fffffa56c1c3df6dce4b83178f75787dd5d794a18c5d0c087769f21
Timestamp convention: JSON3 tStartMs and dDurationMs, written as half-open intervals [start,end).

The complete JSON3 and VTT tracks were read for all three requested recordings. The JSON3 audit spans are:

| Video | Recording date | JSON3 events | Nonempty caption events | Track span |
|---|---:|---:|---:|---:|
| TtMNnZ8__UU | 2022-09-22 | 3344 | 1672 | 00:00:00.179-01:19:57.620 |
| 82__84nYd4I | 2022-09-27 | 2926 | 1463 | 00:00:00.000-01:19:11.120 |
| ph3wE8cFMmk | 2022-09-29 | 3106 | 1553 | 00:00:00.120-01:17:04.440 |

## Boundary decision

Chapter 2 occupies physical pages 20-62. Physical pages 63-67 are the separate Problem Set 2 packet. Physical page 68 is the opening divider for Chapter 3, Relativistic Particles, Fields, and Green Functions.

The spoken handoff occurs inside TtMNnZ8__UU:

| Boundary role | Timestamp | Caption evidence | Reading and confidence |
|---|---|---|---|
| Chapter 2 close cue | 00:50:22.579-00:50:29.280 | "finally done with uh this quality times one and we're ready to actually do a field Theory" | The caption agrees on the handoff structure. "quality times one" is an ASR error or unresolved recognition of the preceding noun phrase. Confidence: high for the boundary, medium for the full wording. |
| Clear transition clause | 00:50:25.680-00:50:29.280 | "one and we're ready to actually do a field Theory" | The reliable spoken clause is "and we're ready to actually do a field theory." Confidence: high. |
| First sustained Chapter 3 topic | 00:51:15.660-00:51:20.579 | "a few words at least about a classical field Theory" | This is the first sustained new-topic statement after the short recap. Confidence: high. |
| Chapter 3 setup | 00:52:00.540-00:52:25.559 | Classical mechanics with a continuum of degrees of freedom, followed by a spacetime label | This supplies the first body-level field-theory material after the divider. Confidence: medium-high because the ASR is heavily corrupted while the topic sequence is clear. |

The phrase to use as the exact operational transition is the clear clause at 00:50:25.680-00:50:29.280. Preserve the raw caption in the evidence layer. A source-resolved noun phrase such as "quantum mechanics [one?]" remains provisional from these caption tracks alone.

## Physical-page audit

| Physical page | Visual identity | Extraction result | Caption alignment | Confidence | Pass 1 disposition |
|---:|---|---|---|---|---|
| 20 | Dark chapter divider: Lagrangian Quantum Mechanics, Path Integrals, and Perturbation Theory; source label 253a/lecture_notes.pdf, pages 10-51 | Title text recovered by pdftotext | TtMNnZ8__UU begins with the lecture opening at 00:00:00.179; the first topic-bearing caption begins at 00:00:24.539 with the Lagrangian for a one-degree-of-freedom mechanical system | High | Chapter 2 opening divider. Preserve as structural source evidence. |
| 62 | Final handwritten note page in the page-10-to-page-51 span. The visible close records the energy gap as an observable, the counterterm and regularization prescription as part of the path-integral definition, and the stronger QFT restrictions from Poincare symmetry and causality | Text extraction is blank because the page is handwritten | TtMNnZ8__UU evidence window 00:45:21.720-00:50:10.099; the finite-counterterm and QFT-constraint discussion ends immediately before the handoff bridge | High from the render; medium for caption-to-line matching | Chapter 2 closing note page. Capture the handwritten content in the Chapter 2 source packet. |
| 63 | Dark divider: Physics 253a Problem Set 2; Source PDF: 253a/pset2.pdf; tests Lagrangian QM, path integrals, diagrams, and counterterms | Cover text recovered by pdftotext | Thematically adjacent to the TtMNnZ8__UU counterterm discussion | High | Assignment material reserved for later exercise integration. |
| 64 | Problem Set 2, page 1. Problem 1 defines the anharmonic oscillator and its Euclidean Green function | Full problem text and equations recovered | The page is source material for the exercise packet | High | Assignment material reserved for later exercise integration. |
| 65 | Problem Set 2, page 2. Problem 1 continues with the self-energy and excited-state question | Full continuation and remark recovered | The page is source material for the exercise packet | High | Assignment material reserved for later exercise integration. |
| 66 | Problem Set 2, page 3. Problem 2 introduces scalar field theory, regularization, and the counterterm | Full problem text, equations, and footnote recovered | Thematic overlap with pages 62 and 68 is exercise-level source material | High | Assignment material reserved for later exercise integration. |
| 67 | Problem Set 2, page 4. Problem 2 continues with the Euclidean Green function, spectral decomposition, poles, and branch cuts | Full continuation and remark recovered | Thematic overlap with Chapter 3 Green functions | High | Assignment material reserved for later exercise integration. |
| 68 | Dark chapter divider: Relativistic Particles, Fields, and Green Functions; source label 253a/lecture_notes.pdf, pages 52-112 | Title text recovered by pdftotext | The TtMNnZ8__UU handoff at 00:50:25.680-00:50:29.280 and the new-topic statement at 00:51:15.660 establish the spoken start; later tracks continue the same chapter | High | Chapter 3 opening divider. Start the next chapter source packet here. |

## Caption reconciliation across the three recordings

### TtMNnZ8__UU, 2022-09-22

The final page-62 discussion runs through the counterterm prescription, the energy-level ambiguity, and the restriction supplied by QFT principles. The decisive bridge is:

    00:50:22.579  finally done with uh this quality times one
    00:50:25.680  one and we're ready to actually do a
    00:50:28.200  field Theory

The caption text "quality times one" carries the recognition uncertainty. The field-theory clause remains clear. Yin then says "a few words at least about a classical field Theory" at 00:51:15.660, followed by the continuum-of-degrees-of-freedom setup. This recording therefore contains the spoken Chapter 2 to Chapter 3 handoff and the first Chapter 3 setup.

Disposition: retain the full raw interval in the boundary ledger. Assign the counterterm and finite-part discussion to the Chapter 2 close. Assign the classical-field-theory setup from 00:51:15.660 forward to Chapter 3.

### 82__84nYd4I, 2022-09-27

The first topic-bearing caption appears at 00:00:26.119:

    action that is of the form ... the integral ... of some Lagrangian ... a function of scalar fields

The track continues the field-theory material after the Chapter 3 divider. Later portions discuss free-particle interpretation, creation and annihilation operators, path-integral correlators, and local-field ordering. The closing lecture seam is explicit at 01:15:52.380-01:16:08.820:

    I guess next time I'm going to explain ... mechanical example ...
    I'll discuss this systematically next time.

Disposition: Chapter 3 continuation evidence. The track corroborates the established Chapter 3 boundary. Its opening caption begins after a recording and caption seam, so the first 26 seconds carry transition context rather than a new page assignment.

### ph3wE8cFMmk, 2022-09-29

The first caption is the fragment "of" at 00:00:00.120. The first coherent topic-bearing caption begins at 00:00:23.279:

    the products, a bunch of field operators

The lecture develops the general field-operator and Green-function discussion. The later close at 01:15:42.980-01:16:22.980 says:

    I guess I'll just stop here ... the interpretation of the results of that later.
    Next lecture I'm going to discuss these kind of Green functions in a general ...

Disposition: Chapter 3 continuation evidence. The opening fragment belongs to the same Green-function sequence. The late forward-looking language marks a lecture seam within Chapter 3.

## Working source dispositions

| Source unit | Disposition |
|---|---|
| Physical page 20 and the opening TtMNnZ8__UU topic cue | Include as the Chapter 2 structural opening. |
| Physical page 62 and TtMNnZ8__UU 00:45:21.720-00:50:10.099 | Include as the Chapter 2 closing source interval. Preserve the visual note wording and the caption uncertainty. |
| TtMNnZ8__UU 00:50:22.579-00:50:29.280 | Include as the spoken boundary record. Use the clear field-theory clause for the exact handoff. |
| TtMNnZ8__UU from 00:51:15.660 forward | Assign to Chapter 3 source capture. |
| Physical pages 63-67 | Keep in the assignment packet for later exercise integration. |
| Physical page 68 | Include as the Chapter 3 structural opening. |
| 82__84nYd4I and ph3wE8cFMmk | Assign to Chapter 3 continuation evidence, with their recording seams retained in the boundary ledger. |
