# Speaker and Q&A audit

## Scope and conventions

This audit covers `OY_napMPywE` on the half-open interval `[00:05:02.580,01:20:13.920)`. It uses the frozen records in `work/pilot/transcript.cleaned.jsonl` and the bounds in `work/pilot/source-map.md`. All unlisted substantive records in this interval are Yin's lecture voice.

The canonical transcript has no separate speaker field. A few records contain more than one voice. For those records, the interval below is the exact canonical container. A finer speaker boundary appears only where the caption word onsets or the segment audit support it.

Question status has four values:

- `clear`: the cleaned question is printable as quoted speech.
- `partial`: some words survive, with an uncertainty marker at the damaged point.
- `sense-gloss`: the answer and local context establish the topic; the student's words stay unquoted.
- `withheld`: the source does not establish a stable question or a useful gloss.

Text under “Print-safe wording” copies the canonical cleaning, or gives an explicitly bracketed sense gloss. Ellipses mark an excerpt from a longer canonical record.

## Audience exchanges

### 1. Early EFT transition

| Speaker | Canonical record and exact interval | Status | Print-safe wording and use |
|---|---|---|---|
| Yin | `YIN-OY-T000039`, `[00:11:38.880,00:11:56.160)` | clear transition | “So, what are some examples? Any questions about it?” The remainder, “Yes. I will describe that. Yeah,” has no secure internal speaker split. Keep the whole record out of chapter prose, as its frozen disposition is repetition. |
| Student | same record | withheld | `[Student question or response absent from the captions.]` |

### 2. Course-order question

| Speaker | Canonical record and exact interval | Status | Print-safe wording and use |
|---|---|---|---|
| Yin | `YIN-OY-T000090`, `[00:26:29.039,00:26:41.360)` | clear invitation | “Okay, so that's the plan for the course, as far as the content is concerned. Any questions?” |
| Student | tail of `YIN-OY-T000090`; the segment audit bounds the quiet turn within `[00:26:34.260,00:26:41.360)` | sense-gloss | `[A student asks where canonical quantization enters the course plan; exact wording absent.]` |
| Yin | `YIN-OY-T000091`, `[00:26:41.360,00:26:50.760)` | clear | “Canonical quantization will be somewhere here. We'll discuss the quantization of fields in preparation before setting up a scalar field theory.” |
| Yin | `YIN-OY-T000092`, `[00:26:50.760,00:27:13.919)` | partial | “In preparing for these lectures, I was debating myself whether I wanted to do the [unclear] first or the quantization of fields first. I decided to do that first, just to get this out of the way, and [inaudible].” Retain only as course-order Q&A with the uncertainty markers. |
| Yin | `YIN-OY-T000093`, `[00:27:13.919,00:27:19.620)` | clear invitation | “Any other questions?” Omit as classroom management. |

### 3. How the free states are created

| Speaker | Canonical record and exact interval | Status | Print-safe wording and use |
|---|---|---|---|
| Student | no standalone canonical record; the question precedes Yin's “Yes” at the `00:34:02.760` onset of `YIN-OY-T000111` | sense-gloss | `[A student asks how the particles or states are created; exact wording inaudible.]` |
| Yin | `YIN-OY-T000111`, `[00:34:02.760,00:34:25.500)` | partial | “Yes. I don't really care. I've just declared the states are there. All right, I mean, the system is non-interacting, so there's nothing to do to [unclear], but that's my system. Later we'll study interacting systems, and you can create particles with scattering, but I don't have to say how I created the state. It exists. Now, that's the system I'm going to study for the moment. It's a very simple system.” The scattering clause has medium confidence. |

### 4. Superpositions, non-interaction, and the creation-operator callback

| Speaker | Canonical record and exact interval | Status | Print-safe wording and use |
|---|---|---|---|
| Yin | `YIN-OY-T000112`, `[00:34:25.500,00:34:33.560)` | clear invitation | “Any other questions? Yeah.” |
| Student | `YIN-OY-T000112`, same interval | sense-gloss | `[Student question inaudible; it concerns linear superpositions or the meaning of “non-interacting.”]` The two alternatives remain unresolved. |
| Yin | `YIN-OY-T000113`, `[00:34:33.560,00:34:52.980)` | clear in substance | “And you're always allowed to consider linear superpositions of the states. But when I say non-interacting, I just mean that the energy of any particular state is the sum of the energies of these particles. There's no potential contribution due to any mutual interaction.” |
| Unresolved room exchange | `YIN-OY-T000114`, `[00:34:52.980,00:35:00.000)`; `YIN-OY-T000115`, `[00:35:00.000,00:35:28.329)` | withheld | `YIN-OY-T000114` has only “Maybe it depends on, you know...” `YIN-OY-T000115` is `[Low-volume student exchange and pause; unintelligible.]` Use neither as a proposition. |
| Yin | `YIN-OY-T000117`, `[00:35:28.339,00:35:48.250)` | clear | “Maybe a rather boring one, but the reason I'm talking about this is just to explain that you can easily construct a Lorentz-invariant quantum-mechanical system without ever talking about fields. Now, here it is.” |
| Yin | `YIN-OY-T000119`, `[00:35:48.260,00:36:08.210)` | partial callback | “There's a question about, you know, creation, how to create the [state]. I said, you know, that's not something I need to discuss, but we can, if you wish, define [creation and annihilation] operators in the following way at this point. So we can...” This is Yin's report of the earlier question. It is not student wording. |

### 5. Delta-function normalization and wave packets

| Speaker | Canonical record and exact interval | Status | Print-safe wording and use |
|---|---|---|---|
| Student | first part of `YIN-OY-T000141`, `[00:39:53.940,00:40:20.510)`; caption evidence places Yin's reply from about `00:40:08.240` | partial | “So why is it that sometimes, like, in some places I've seen this delta function has [unclear factor]?” Plausible factors include $2p^0$ and $2E_{\vec p}$; the transcript withholds the formula. |
| Yin | latter part of `YIN-OY-T000141`, same canonical interval | clear | “That is a matter of normalization convention, right? I'm free to rescale $a$ and $a^\dagger$ by a factor of two, and I would just change my normalization convention. Now, you see...” |
| Yin | `YIN-OY-T000143`, `[00:40:20.520,00:40:35.329)` | clear | “This one-particle state corresponds to a plane wave of the particle, which, strictly speaking, is not a normalizable state anyway. If you want to form a normalizable state, you have to take a wave packet. For example, you can take some state like that, you know, integrated by this...” |
| Student | inside `YIN-OY-T000145`, `[00:40:35.339,00:41:18.890)` | withheld | `[Student follow-up inaudible.]` |
| Yin | same `YIN-OY-T000145` | partial | “The overall [factor can be constant], or, you know, nonconstant. The overall factor is another convention. I'm allowed to, for example, also rescale this state by a factor of the energy to the one-third power, or whatever.” The record's final clause remains unintelligible. |

### 6. What the annihilation operator does

| Speaker | Canonical record and exact interval | Status | Print-safe wording and use |
|---|---|---|---|
| Yin | `YIN-OY-T000147`, `[00:41:18.900,00:41:30.710)` | clear invitation | “Any other questions?” |
| Student | opening of `YIN-OY-T000149`, `[00:41:34.160,00:41:48.829)` | sense-gloss | `[A student asks what the annihilation operator does; exact wording partly inaudible.]` The caption phrase “Each state?” is too uncertain to print as the question. |
| Yin | latter part of `YIN-OY-T000149`, same interval; reply begins at about `00:41:36.420` | clear | “No, the annihilation operator should reduce the particle number by one, just like a creation operator should increase the particle number by one. So the vacuum has zero particles, and that's sort of the definition, part of the definition.” |

### 7. Choice of vacuum energy

| Speaker | Canonical record and exact interval | Status | Print-safe wording and use |
|---|---|---|---|
| Yin | opening of `YIN-OY-T000151`, `[00:41:48.839,00:42:24.050)` | clear invitation | “Any other questions?” |
| Student | same record; caption onsets place the turn at about `[00:41:50.599,00:41:56.339)` | clear, trailing off | “Yes, but we also agreed to choose the energy of the vacuum state however we want, or...” |
| Yin | same record; reply begins at about `00:41:56.339` | clear | “Right, so that's a good question. I stated this as following from our assumption that the vacuum is Poincare invariant. Now, of course, you could trivially redefine your Hamiltonian by adding to it a constant. You're allowed to do that. But I'm going to choose this to be zero. It's a natural assumption.” |
| Yin | `YIN-OY-T000153`, `[00:42:25.920,00:42:55.790)` | partial continuation | “We would like to say that there is a [vacuum], but not even necessarily unique. I would assume that this vacuum state is symmetry-invariant, and we'll see shortly, in a bit, that this $H$ is one of the generators of our symmetry. And to say the state is invariant under the symmetry means all the generators should annihilate it, as in any continuous global symmetry.” |

### 8. Massless particles and finite particle number

| Speaker | Canonical record and exact interval | Status | Print-safe wording and use |
|---|---|---|---|
| Student | `YIN-OY-T000163`, `[00:44:05.271,00:44:33.559)` | sense-gloss | Canonical wording: `[Low-volume student question; unintelligible.]` Its sense concerns massless particles and the assumption of finite particle number. |
| Yin | `YIN-OY-T000165`, `[00:44:33.560,00:45:00.000)` | partial | “That's much less obvious. We'll see that there are massless particles [unclear clause], and we can also study what we call a massless theory. And for massless particles, it's not obvious why you want to demand the number of particles to be finite, and that is a very subtle question. We may not even be able to get to it this semester, but it's definitely tied to the issue of infrared divergences in quantum electrodynamics.” |

### 9. Scalar field operator versus particle content

| Speaker | Canonical record and exact interval | Status | Print-safe wording and use |
|---|---|---|---|
| Yin | `YIN-OY-T000223`, `[00:59:40.000,01:00:00.000)` | clear invitation after a recap | “Okay, so that's the statement that φ̂(x) and φ̂(x′), $x′=Λx+a$, are related by the symmetry. Any questions so far?” |
| Student | no standalone record; the segment audit places the omitted turn at about `[00:59:52,01:00:05)` across `YIN-OY-T000223` and `YIN-OY-T000224` | sense-gloss | `[A student asks about the scalar-field assumption; exact wording absent from the captions.]` |
| Yin | `YIN-OY-T000224`, `[01:00:00.000,01:00:20.000)` | partial opening | “We will consider that later on. For here, for now, in fact... That's a very good point. I'm assuming that this is a scalar field operator. Now, in...” |
| Yin | `YIN-OY-T000225`, `[01:00:20.000,01:00:40.000)`; completed by the opening word of `YIN-OY-T000226`, `[01:00:40.000,01:01:00.000)` | clear excerpt | “I should say that the field operator, whether it's scalar or not, has nothing to do with what kind of particles we have in this theory. You can have a theory with fermions or gauge bosons where you can still have a scalar field operator.” |

### 10. Infinitesimal operator question at the audit boundary

| Speaker | Canonical record and exact interval | Status | Print-safe wording and use |
|---|---|---|---|
| Yin | opening of `YIN-OY-T000238`, `[01:04:40.000,01:05:00.000)` | clear invitation | “Any questions about this?” |
| Student | same record | partial | The only surviving candidate wording is “Operator is what?” The record marks the speaker turn as unclear, so keep this phrase in the audit and outside printed prose. |
| Yin | latter part of `YIN-OY-T000238`; `YIN-OY-T000239`, `[01:05:00.000,01:05:14.579)` | withheld | The reply contains several unresolved nouns. No print-safe proposition survives these records. |
| Yin | `YIN-OY-T000240`, `[01:05:14.579,01:05:37.380)` | partial | “So I'm considering the case that these are small, and so we'll expand to first order. This will ultimately be sufficient for our discussion, because I can recover the finite form by [unresolved]. All right.” The first sentence is safe. |

### 11. Names of the Poincare generators

| Speaker | Canonical record and exact interval | Status | Print-safe wording and use |
|---|---|---|---|
| Yin | `YIN-OY-T000241`, `[01:05:37.380,01:05:43.200)` | clear invitation | “Okay, so I can only do this. Any questions so far?” |
| Student | `YIN-OY-T000242`, `[01:05:43.200,01:06:12.200)` | partial | `[Question begins “what you wrote here is just the general form for ...”; ending inaudible.]` The canonical cleaned field withholds the question. |
| Yin | `YIN-OY-T000243`, `[01:06:12.200,01:06:24.359)` | clear | “They have some names. So this $\hat P_\mu$ is the so-called energy-momentum operator.” |
| Yin | `YIN-OY-T000244`, `[01:06:24.359,01:06:38.400)` | clear | “And the $\hat J^{\mu\nu}$ is the operator corresponding to the Lorentz boosts and the angular momentum.” |

### 12. First-order unitarity

| Speaker | Canonical record and exact interval | Status | Print-safe wording and use |
|---|---|---|---|
| Student | first part of `YIN-OY-T000259`, `[01:10:29.820,01:10:52.830)` | sense-gloss | `[A student asks how the infinitesimal expression for $U$ is unitary when its factors are multiplied; exact wording inaudible.]` |
| Yin | latter part of `YIN-OY-T000259`, same interval | partial | “Well, if you have one plus $i$ times some Hermitian operator, [unresolved].” |
| Room audio | `YIN-OY-T000260`, `[01:10:52.830,01:11:09.420)` | withheld | Possible continuation of the answer. The canonical cleaned text is null. |
| Yin | `YIN-OY-T000261`, `[01:11:09.420,01:11:17.520)` | raw-only transition | The raw trace has “Any other questions? All right.” The canonical cleaned text is null. Keep it out of chapter prose. |

### 13. Whether the local operator exists

| Speaker | Canonical record and exact interval | Status | Print-safe wording and use |
|---|---|---|---|
| Yin | `YIN-OY-T000271`, `[01:13:31.800,01:13:38.760)` | raw-only invitation | The raw trace has “Any questions so far?” The canonical cleaned text is null because the record is classroom logistics. |
| Student | no standalone canonical record; the quiet turn lies before Yin's “No” in `YIN-OY-T000272`, `[01:13:38.760,01:13:53.820)` | sense-gloss | `[A student asks whether such an operator exists or whether microcausality follows; the precise alternative and wording are indistinct.]` |
| Yin | `YIN-OY-T000272`, `[01:13:38.760,01:13:53.820)` | partial | “No, it's not obvious at the moment, but we're back at the requirement of the existence of an operator $\hat\phi$ tied to a spacetime point $x$ in that way. [Unresolved] it's an [unresolved] constraint on the quantum system. In fact, you can ask...” |
| Yin | `YIN-OY-T000274`, `[01:13:59.880,01:14:19.440)`; `YIN-OY-T000275`, `[01:14:19.440,01:14:27.659)` | clear continuation | “You can ask whether this applies to our system of free particles. Intuitively it should, because we have non-interacting particles, and the particles themselves propagate with the relativistic dispersion relation, so the system must be causal. But can you actually write down these local field operators in that theory?” |

### 14. Final construction question

| Speaker | Canonical record and exact interval | Status | Print-safe wording and use |
|---|---|---|---|
| Yin | `YIN-OY-T000312`, `[01:19:47.100,01:19:52.010)` | clear invitation | “Okay, any final questions before we end? Yes.” |
| Student | first part of `YIN-OY-T000314`, `[01:19:52.020,01:20:00.709)` | sense-gloss | Canonical wording: `[Student question partly inaudible; sense gloss, exact wording withheld:] asks how the displayed field operator was constructed.` |
| Yin | latter part of `YIN-OY-T000314`, same interval | clear words, inferred speaker boundary | “For now, yes.” The transcript marks the speaker assignment as likely. |
| Yin | `YIN-OY-T000316`, `[01:20:00.719,01:20:13.920)` | clear through the frozen endpoint | “Because this is only a, you know, kind of a general motivation. Of course this is the correct answer. You can check, or you might check, that it works, but we'll explain how to systematically construct this” |

The frozen contract includes `YIN-OY-T000317` only for the boundary carryover word “thing,” whose VTT onset is exactly `01:20:13.920` and which completes `YIN-OY-T000316`. The rest of `YIN-OY-T000317`'s weak-room tail is excluded.

## Lecturer-only question transitions

These records contain no recoverable student turn. Classroom invitations can be dropped while the surrounding lecture stays continuous.

| Record | Exact interval | Yin's cleaned wording | Disposition |
|---|---|---|---|
| `YIN-OY-T000027` | `[00:08:31.620,00:08:51.120)` | “All right. Any questions so far? You should feel free to interrupt me at any point. You don't have to raise your hand in this class.” | Classroom management. |
| `YIN-OY-T000045` | `[00:13:17.820,00:13:23.160)` | “Right. Any other questions?” | Classroom management. |
| `YIN-OY-T000061` | `[00:17:55.799,00:18:21.740)` | “Any questions?” followed immediately by the renormalizability aside. | Keep the aside, drop the invitation. |
| `YIN-OY-T000063` | `[00:18:56.460,00:19:14.400)` | “Okay, so that's a kind of a sketch of the subjects of study. Any questions or comments?” | Repetition and pause. |
| `YIN-OY-T000093` | `[00:27:13.919,00:27:19.620)` | “Any other questions?” | Classroom management. |
| `YIN-OY-T000106` | `[00:32:23.100,00:32:33.360)` | “Okay. Any questions about this?” | Classroom pause. |
| `YIN-OY-T000155` | `[00:42:55.800,00:43:00.910)` | “Any other questions?” | Classroom management. |
| `YIN-OY-T000168` | `[00:45:01.440,00:45:07.490)` | “Okay. Any other questions?” | Classroom pause. |
| `YIN-OY-T000202` | `[00:53:39.480,00:53:52.010)` | “Any questions so far?” | Classroom pause. |
| `YIN-OY-T000214` | `[00:56:40.000,00:57:00.000)` | “Any questions about this?” inside the metric-signature explanation. | Keep the explanation, drop the invitation. |
| `YIN-OY-T000226` | `[01:00:40.000,01:01:00.000)` | “Any other questions? Very good.” after the scalar-operator answer. | Classroom management. |

## Yin's self-posed questions

The following are lecturer turns. They belong to the argument and carry the speaker label `Yin`.

| Canonical records | Exact interval | Function |
|---|---|---|
| `YIN-OY-T000016` | `[00:05:02.580,00:05:13.500)` | Opens with “What is quantum field theory?” |
| `YIN-OY-T000020` | `[00:06:29.100,00:06:42.900)` | Moves from the two senses of QFT into local QFT. |
| `YIN-OY-T000031` | `[00:09:38.279,00:09:47.519)` | Opens the EFT description. |
| `YIN-OY-T000046` | `[00:13:23.160,00:13:45.240)` | Opens the example list. |
| `YIN-OY-T000053` | `[00:15:00.120,00:15:15.899)` | Raises the existence of four-dimensional local QFTs. |
| `YIN-OY-T000068`, `YIN-OY-T000071`, `YIN-OY-T000073` | `[00:20:16.080,00:21:57.120)` | Uses “right?” and “Why bother?” inside the Lagrangian-versus-Hamiltonian motivation. |
| `YIN-OY-T000087` | `[00:25:42.720,00:26:00.960)` | Asks which relativistic particles can occur. |
| `YIN-OY-T000095`, `YIN-OY-T000096` | `[00:27:34.100,00:28:32.100)` | States the chapter's prelude question about relativistic particles and fields. |
| `YIN-OY-T000157` | `[00:43:00.920,00:43:21.309)` | Asks why creation and annihilation operators were introduced. |
| `YIN-OY-T000174`, `YIN-OY-T000180`, `YIN-OY-T000184` | `[00:45:34.440,00:48:21.000)` | Moves from interacting particles to the relativistic-causality problem. |
| `YIN-OY-T000197` | `[00:52:17.640,00:52:48.109)` | Asks what “field” means. |
| `YIN-OY-T000216`, `YIN-OY-T000227` | `[00:57:20.000,01:01:20.000)` | Motivates the unitary action and its infinitesimal form. |
| `YIN-OY-T000275`, `YIN-OY-T000276` | `[01:14:19.440,01:14:44.760)` | Returns to local operators in the free-particle model. |
| `YIN-OY-T000285`, `YIN-OY-T000289` | `[01:15:58.560,01:16:38.760)` | Poses the existence question for $\widehat\phi(x)$. |

## Transition rules for near-verbatim integration

1. Preserve Yin's local pivots when the canonical text supplies them: “So,” “Now,” “The point is,” “All right,” and his self-posed questions. Their placement carries the derivation order.
2. Keep each student turn separate from Yin's answer. A `sense-gloss` stays in brackets and carries the phrase “exact wording withheld.”
3. Use the canonical uncertainty markers at damaged words. A clean explanatory sentence can be quoted as an excerpt when an adjacent clause remains unresolved.
4. Let the next source-backed sentence provide the bridge after a classroom invitation is removed. Chapter prose should gain no editorial transition at that cut.
5. Treat Yin's report “There's a question about ...” in `YIN-OY-T000119` as Yin's transition. Keep the student's wording withheld.
6. Keep formula wording tied to its canonical record and formula authority. Speaker cleanup preserves the equation inventory and notes-only boundaries.
7. Preserve the final Q&A as a labeled supplement after the Chapter 1 close at `01:19:47.090`. The ten-millisecond separator `[01:19:47.090,01:19:47.100)` carries no speech.
