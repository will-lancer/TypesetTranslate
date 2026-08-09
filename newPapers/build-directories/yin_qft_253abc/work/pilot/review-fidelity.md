# Source-fidelity review

Review result: blocked.

## Counts

| Check | Count | Result |
|---|---:|---|
| Substantive chapter units | 95 | Every `YIN253A-C01-U001` through `U095` is present in both `chapter01.tex` and `provenance.jsonl`. |
| Clean unit traces | 80 | Source wording, order, scope, and source class are adequate. |
| Failed unit traces | 15 | Each failure is listed below. |
| Source classes | 95 | 40 `SPEECH_CLEAN`, 29 `SOURCE_COMPOSITE`, 24 `NOTES_EXACT`, 1 `EQUATION_NORMALIZED`, 1 `EDITORIAL_NOTE`. |
| Unit types | 95 | 69 paragraphs, 21 equations, 2 figures, 2 lists, 1 editorial note. |
| Note-page dispositions | 9 | All original pp. 1--9 have records. Five omitted elements are nonsemantic ink or layout marks with stated reasons. |
| Transcript dispositions | 382 | 174 included, 23 partly included with uncertainty excluded, 91 coverage separators, 31 outside section, and 63 other exclusions or special records. |
| Equation and diagram source failures | 0 | The note-governed formulas and both reconstructed diagrams preserve the source content. The `d^D p^\mu` to `d^D p` change is explicitly recorded as `EQUATION_NORMALIZED` in U086. |

The project audit reports 95 source comments, 95 provenance records, 95 substantive units, nine page alignments, nine page dispositions, continuous core transcript coverage, and no unfinished markers. Its only fidelity-related warning before this report existed was the missing review file.

## Full trace ledger

Pass: `U001--U006`, `U008--U012`, `U014--U018`, `U020--U028`, `U030--U035`, `U037--U040`, `U043--U046`, `U049--U052`, `U054`, `U056--U060`, `U062--U073`, `U075--U083`, `U085--U092`, `U094--U095`.

Fail: `U007`, `U013`, `U019`, `U029`, `U036`, `U041`, `U042`, `U047`, `U048`, `U053`, `U055`, `U061`, `U074`, `U084`, `U093`.

This partition covers all 95 IDs exactly once.

## B1: exact trace or source-class blockers

### U013: unresolved audio is represented as reviewed `SPEECH_CLEAN`

The printed sentence uses only the clear part of the interval. The provenance record still spans `00:17:55.799--00:18:56.460`, quotes the unresolved comparison, assigns confidence 0.94, and says it was reviewed against the frozen sources. The transcript disposition splits the interval: `00:17:55.799--00:18:21.740` is included, while `00:18:21.740--00:18:56.460` is `conflicted_audio_excluded`, with direct audio review required. Narrow U013 to the clear interval or retain a separate unresolved record. Evidence: `chapter01.tex:166-169`; `provenance.jsonl:13`; `transcript.cleaned.jsonl:63-64`; `transcript-dispositions.jsonl:62-63`.

### U042: the occupation-number sentence falls outside the cited interval

U042 ends at `00:43:48.530`. The source phrase begins at `00:43:48.540`, after a 10 ms coverage separator, and is assigned by the disposition ledger to U043. The claim itself is supported. Its paragraph-level trace is not. Extend or split the interval and update the disposition linkage. Evidence: `chapter01.tex:382-386`; `provenance.jsonl:42`; `transcript.cleaned.jsonl:162-163`; `transcript-dispositions.jsonl:161-162`; `segment-audits/00-35-00_to_00-45-00.md:23`.

### U047: resolved source conflict is labeled `SPEECH_CLEAN`

The last sentence is editorial source apparatus: it reports a spoken self-correction and says the displayed equation follows the handwritten order. The page disposition calls this an oral conflict resolved by the notes. The segment audit records medium confidence in the corrected spoken second monomial. Use `SOURCE_COMPOSITE` for the explanatory paragraph, or move the source-resolution sentence into an editorial note. Evidence: `chapter01.tex:414-419`; `provenance.jsonl:47`; `page-dispositions.jsonl:4`; `segment-audits/00-45-00_to_00-55-00.md:14,80`.

### U048: the Hermitian-operator premise lies outside the cited interval

The final paragraph says quantum mechanics permits arbitrary Hermitian operators. Its cited interval begins at `00:47:23.040`. Yin states the Hermitian-operator premise at `00:46:08.040--00:46:31.370`, which the disposition ledger assigns to U046. U048's own excerpt contains only the difficulty of preserving relativistic symmetry. Expand the composite provenance or remove the premise from U048. Evidence: `chapter01.tex:421-424`; `provenance.jsonl:48`; `segment-audits/00-45-00_to_00-55-00.md:13-15`; `transcript-dispositions.jsonl:177`.

### U053: the operator, Hermiticity, and observable claims lie in U054's interval

U053 cites `00:51:19.319--00:52:17.630`, which supports the local-disturbance motivation. The statements that the field acts on Hilbert space, may be Hermitian, and has an observable expectation value begin at `00:52:17.640`; the disposition ledger assigns them to U054. Move those sentences to U054 or extend U053 and repair both records. Evidence: `chapter01.tex:485-495`; `provenance.jsonl:53`; `segment-audits/00-45-00_to_00-55-00.md:20-21`; `transcript-dispositions.jsonl:197-198`.

### U061: the first-order qualification is sourced from the wrong time

The cited `01:01:00--01:01:40` speech says that a finite transformation is composed of infinitesimal transformations and that the infinitesimal version suffices. The words about small parameters and expanding to first order occur at `01:05:14.579--01:05:37.380`, after the displayed generator expansion. That later interval is currently classified as excluded repetition and linked to no chapter unit. The note annotation also supports first order, which would require a composite or note-backed trace. Repair the interval, class, and lecture-order placement together. Evidence: `chapter01.tex:544-547`; `provenance.jsonl:61`; `transcript.cleaned.jsonl:229-230,242`; `transcript-dispositions.jsonl:241`; `segment-audits/01-05-00_to_01-15-00.md:15-19`.

### U074: an unresolved adjective is printed as settled speech

The cleaned source marks two words around “constraint” unresolved. The final prose supplies “nontrivial,” and provenance still labels the unit `SPEECH_CLEAN`. The segment audit permits that adjective only as a marked sense gloss. Keep the recoverable wording, mark the gloss editorially, or supply new audio evidence. Evidence: `chapter01.tex:629-633`; `provenance.jsonl:74`; `transcript-dispositions.jsonl:273`; `segment-audits/01-05-00_to_01-15-00.md:132-138`.

### U084: editorial connective is labeled `NOTES_EXACT`

The note reads “Check micro causality;”. It does not say “The handwritten notes check the second claim. First,”. That sentence is a useful editorial bridge, with an invented deictic relation to the preceding prose. Classify it as `EDITORIAL_NOTE` or replace it with the exact heading. Evidence: `chapter01.tex:698-704`; `provenance.jsonl:84`; `notes-exact.tex:445-451`; `page-audits/physical-012-013.md:100,207`.

### U093: a lecture transition is rewritten as a chapter transition without an editorial class

Yin says, “Next time we'll discuss how to formulate quantum mechanics using the Lagrangian language.” The chapter says, “The next chapter formulates quantum mechanics in Lagrangian language.” The master prompt requires newly written transitions to carry `EDITORIAL_NOTE`. Retain “next lecture” or split the chapter-facing sentence into an editorial unit. Evidence: `chapter01.tex:770-773`; `provenance.jsonl:93`; `transcript.cleaned.jsonl:312`; `segment-audits/01-15-00_to_01-22-00.md:78-80`.

## B2: wording, qualification, and mechanism blockers

### U007: two effective-field-theory qualifications are dropped

Yin says that a path integral may or may not make nonperturbative sense, and that an EFT captures long-distance or low-energy observables “and not necessarily beyond that.” The printed paragraph removes both boundaries. Restore them in Yin's order. Evidence: `chapter01.tex:49-53`; `provenance.jsonl:7`; `transcript.cleaned.jsonl:38-40`; `segment-audits/00-04-45_to_00-15-00.md:61-63`.

### U019: Yin's particle-versus-field vocabulary is compressed into generic prose

The segment audit explicitly says this lecture-only distinction should remain in Yin's terminology. The source says particles and fields are “really, really different,” gives “if it smells like a particle, looks like a particle,” and says their spins “have nothing to do with each other.” The chapter reduces this to “different concepts” and “different meanings.” Restore the characteristic explanation with light cleanup. Evidence: `chapter01.tex:238-241`; `provenance.jsonl:19`; `transcript.cleaned.jsonl:87-88`; `segment-audits/00-25-00_to_00-35-00.md:10`.

### U029: a tentative identical-particle choice becomes an assumption

Yin says the particles “could be identical” and later “perhaps they're identical”; his stated assumption is that they are noninteracting, with a same-mass example. The chapter says they are identical, have the same mass, and do not interact. Preserve the tentative status of identity and same mass. Evidence: `chapter01.tex:297-301`; `provenance.jsonl:29`; `transcript.cleaned.jsonl:109-111`.

### U036: “identical bosons” is an unsupported classification

The notes and speech give commuting creation and annihilation operators and a chosen delta-function normalization. Neither source names the particles as bosons in this passage. The classification is an inference from the algebra. Remove it or mark it as an editorial explanation. Evidence: `chapter01.tex:342-355`; `provenance.jsonl:36`; `transcript.cleaned.jsonl:131`; `notes-exact.tex:241-252`.

### U041: vacuum nonuniqueness is omitted

Yin qualifies the symmetry-invariant vacuum as “not even necessarily unique,” and the segment audit directs the editor to preserve that phrase. The printed paragraph covers the additive energy convention and generator action while dropping the qualification. Restore it without asserting a unique vacuum. Evidence: `chapter01.tex:376-380`; `provenance.jsonl:41`; `transcript.cleaned.jsonl:155`; `segment-audits/00-35-00_to_00-45-00.md:20-21,75`.

### U055: the Poincare-map mechanism loses its nonuniqueness qualification

Yin explains that any two Minkowski points can be related, a translation already suffices, and the choice is highly nonunique. The final paragraph keeps only the abstract covariance requirement. Restore the example and its nonuniqueness qualification, since they explain how the operator family is tied to spacetime. Evidence: `chapter01.tex:501-505`; `provenance.jsonl:55`; `transcript.cleaned.jsonl:210`; `segment-audits/00-45-00_to_00-55-00.md:23-25`.

## Order, equations, diagrams, omissions, and Q&A

The printed topic order follows handwritten pp. 1--9. The scalar expansion precedes its definitions because the handwritten order governs, even though Yin orally defines $\omega_{\vec p}$ while writing the expression. This is documented and faithful.

All 21 displayed-equation units preserve the note formulas and conventions. U086 visibly normalizes the handwritten `d^D p^\mu` to `d^D p`, and its provenance supplies the literal source form and reason. The scalar-field expansion, Fourier signs, mostly-plus interval, free generators, commutator, and odd-integrand proof match `notes-exact.tex:402-472`.

The opening QFT map retains both branches, every listed example, the renormalizable and non-renormalizable enclosures, and all six course arrows. The light-cone figure retains the causal geometry and gains only speech-supported labels. The five omitted graphic elements recorded in page dispositions are the completion check mark, emphasis marks, faint-ink styling, an unattached curve, and divider marks. None carries settled mathematical content.

The clear Q&A used in the chapter stays within Chapter 1: canonical-quantization order, normalization and wave packets, annihilation and vacuum energy, scalar-field covariance, local-field existence, and the final construction question. Low-audibility exchanges remain excluded. U041 still needs the vacuum-nonuniqueness qualification, and U061 currently attaches a later clarification to an earlier interval. The post-class fragment at `01:21:03.980--01:21:26.350` remains correctly unresolved and outside printed prose.

Unresolved blockers: U007, U013, U019, U029, U036, U041, U042, U047, U048, U053, U055, U061, U074, U084, U093
