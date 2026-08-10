# Pass 2 global semantic audit

Audit date: 2026-08-10

## Audit basis

This read-only audit covers the current canonical transcript and all 45
current cleaned lanes. I reread the six video source reports,
`source-map.md`, `source-lanes/boundary-assignment.md`, `ambiguities.md`,
`notes-exact.tex`, the mapped note-source lanes, and the five completed video
audits (`audit-96-uz.md`, `audit-M0py5a4RWhE.md`, `audit-vk_RlYUKUyM.md`,
`audit-3VG2kDHso08.md`, and `audit-TtMNnZ8__UU.md`). The six binding documents
and the Pass 2 dispatcher contract were also used as the cleanup policy.

The semantic scan covered all 779 core records with non-null `cleaned_text`.
The review criteria were source commentary inserted into speech, unbracketed
ASR nonsense, silent mathematical completion, wrong variables, signs,
factorials, measures, dropped questions, jokes, qualifications, operations
that disagree with the cleaned claim, and source conflicts stated as certain.

## Current snapshot and deterministic checks

| artifact | current SHA-256 |
|---|---|
| `work/253a-ch02/transcript.cleaned.jsonl` | `c84a329bba04d3da2f2e5f6911b06919b2e358b0c4653a9a0e0f7e532859f112` |
| `work/253a-ch02/transcript-dispositions.jsonl` | `75b47e5e778b2933f1abdee5b02c56a6004fa534ceb8961b073fa97d44f7cd19` |

The current lane hashes were recomputed from all 45 expected-output files and
match the canonical metadata `inputs` rows. The manifest and lane pass report
9,693 raw events, 901 canonical segments, 802 non-null cleaned segments, and
779 core non-null segments. Every lane has one `lane_audit` with
`coverage_exact: true`; each ordered source-event sequence is complete and
unique. The lane-to-canonical comparison has zero field mismatches for lane,
video, times, source indices, raw text, cleaned text, disposition,
operations, pages, confidence, uncertainty, and formula authority.

The dispositions file has one row for each canonical segment, with matching
IDs, source spans, times, video, scope, and current transcript SHA. The six
frozen intervals and the half-open endpoint rule agree with the boundary
assignment. Tt's Chapter 2 bridge ends at `00:51:10.020`; the explicit
Chapter 3 topic starts at `00:51:15.660`.

Primary page arrays use the physical-to-handwritten mapping from pages 21-62
to notes 10-51. The vk prior-page references are marked as secondary source
references. Problem Set 2 pages 63-67 occur only in explicit secondary
assignment operations. Physical page 68 occurs only on the null Tt boundary
rows. No primary page-map violation remains.

## Formula, operation, and source-commentary checks

The scan covered 1,553 cleaned-text and formula-authority strings. Dollar,
`\\(` / `\\)`, and `\\[` / `\\]` delimiters are balanced, braces are balanced,
and there are zero doubled command backslashes or dangling backslashes. No
core cleaned record contains source-report, physical-page, handwritten-note,
formula-authority, lane, or page-map commentary.

The prior direct formula and operation defect at
`YIN253A-C02-T000077`, `96lN2omwit4`, `00:45:02.520-00:45:36.560`, is fixed.
The text now contains
`$\\prod_{n=1}^{N-1}d^Dq_n$` and
`$\\prod_{n=0}^{N-1}d^Dp_n/(2\\pi\\hbar)^D$`, including the spoken
p-versus-q count, and its operation record agrees with that text. The
finite-step exponential and error at T000072 use the source-exact
`$1-\\frac{i}{\\hbar}\\hat H T/N$`, its exponential replacement, and
`$O((T/N)^2)$`.

The source-sensitive formula families were reread against the exact notes:

- The M0 functional records T000445, T000446, T000449, and T000451 retain
  brackets around unrecoverable speech. The page-37 `Dg`/`Dx` disagreement and
  raw q/Q/g alternation remain explicit `SOURCE_CONFLICT` authority. The
  source-backed lower-case g formulas do not silently claim that the caption
  letters were settled.
- The vk expansion retains `-g/4!`, the three-pairing structure, the
  `\\ell`, `m_\\ell`, and `G^{(\\ell)}` notation, the grouping denominator,
  and the connected-graph exponential. The page source's divergence and
  finite-range qualifications remain in the speech.
- The 3VG graph and self-energy spans retain the `-g/4!` factor, the pole and
  `\\Sigma(k)` signs, and the source-qualified perturbative series. T000639 at
  `00:18:50.039` now says `Wick contraction` and renders the two external
  fields as `$q$`; its deictic tail remains `[unresolved]`.
- The Tt counterterm sequence is source-exact. T000831 at `00:39:37.740`
  contains `$\\Delta L^E=c\\cdot g\\hbar\\frac{q^2}{2}$`; T000834 at
  `00:41:32.460` contains `$\\frac{\\Lambda}{4\\pi}$`; T000837 carries the
  propagator and order-`\\hbar` qualification; T000844 and T000845 preserve
  the finite-`\\Sigma(k)` and operator-renormalization qualifications.

Formula-bearing operations that describe spoken prose or source alternatives
were checked in context. The only earlier operation/text mismatch was T000077;
no current operation asserts a contradictory mathematical value. Source
conflicts stay visible through `SOURCE_CONFLICT`, bracketed text, or an
explicit uncertainty field.

## Recheck of the dispatched semantic findings

### 96lN2omwit4

The former G1 IDs T000003 (`00:01:26.700`), T000029 (`00:14:59.220`), T000061
(`00:36:00.660`), T000071 (`00:41:33.079`), T000072 (`00:42:07.520`), T000074
(`00:43:26.220`), T000076 (`00:44:27.140`), T000077 (`00:45:02.520`), T000079
(`00:46:33.480`), T000080 (`00:46:55.680`), and T000081 (`00:47:20.819`)
now bracket every unresolved caption phrase. The late Q&A IDs T000105-T000112,
T000114, T000116-T000118, and T000120-T000124 likewise bracket the ASR
residuals or use source-backed repairs with uncertainty fields. Recoverable
content such as the finite-N error, generalized-coordinate measure,
regularization qualification, and Legendre/path-integral transitions remains
in the text.

The two LeBron James jokes at T000017 (`00:09:40.260`) and T000124
(`01:10:46.440`) are retained with `[likely: Legendre transform]`. The
question prompts at T000018, T000029, T000047, T000072, T000074, and the
later measure Q&A remain visible. No source commentary was added to these
records.

### M0py5a4RWhE

T000445 (`01:17:01.199`), T000446 (`01:17:35.159`), T000449
(`01:18:31.260`), and T000451 (`01:19:46.500`) now bracket the unresolved
spoken fragments. The exact page-38 functional derivative and inverse-kernel
claims remain source-backed, with q/Q/g and Dg/Dx conflicts stated as
conflicts. T000452 and T000457 retain their unresolved measure and deictic
tokens in caption-unclear brackets. The M0 question, pain, overkill, and
functional-integration qualifications remain in the cleaned voice.

### vk_RlYUKUyM

All seven lanes recheck clean. The former null-omission defect at T000508,
`00:22:57.480`, now records the complete raw text `uh and uh um no um if you
assume`. The connected-graph notation, factorials, finite-range warning,
student questions, and small-coupling convergence qualification remain
source-aligned across the lane seams.

### 3VG2kDHso08

The former G3 residual T000639 is source-repaired as described above. The
unresolved endpoint is explicitly bracketed. The `-g/4!` seam and the
Hamiltonian-versus-Lagrangian qualification remain intact, with no changed
raw events or timestamps.

### TtMNnZ8__UU

The former G4 records T000828 (`00:37:57.300`), T000830 (`00:39:00.720`),
T000831 (`00:39:37.740`), T000834 (`00:41:32.460`), T000837
(`00:43:01.800`), T000844 (`00:46:33.900`), and T000845 (`00:47:26.599`)
now use bracketed nouns or clipped markers wherever the captions are not
recoverable. The counterterm definition, coefficient and hbar bookkeeping,
finite self-energy part, physical-energy qualification, and possible operator
renormalization remain in Xi's wording. The boundary overlap and page-60 to
page-61 seam remain exact.

## Questions, jokes, qualifications, and uncertainty

Recoverable questions are retained throughout the 215 core records containing
question marks, including questions about measures, operator ordering, Wick
rotation, convergence, graph counting, counterterms, and operator
renormalization. Classroom jokes and voice markers remain, including the
elephant-in-the-room line, the trivial-trivia aside, the Mathematica and
overkill remarks, the pain remark, the `Go home` exchange, and the LeBron
wording. Finite-N, hbar, regularization, cutoff, source-normalization, and
finite-part qualifications are not flattened into certainty.

Every remaining low-confidence speech fragment is either bracketed, marked
`[unclear]`, marked `[likely: ...]`, retained as an explicit ellipsis, or
excluded with complete lane-local omission metadata when no Chapter 2 claim is
recoverable. The current cleaned output contains no unbracketed residual from
the former G1-G4 dispatch list.

## Lecture seams and residual scan

Source indices advance through every lane and every video seam. Rolling-cue
time overlaps at the 12, 24, 36, and 48 minute lane boundaries are retained
without merging events across frozen scope changes. The Tt Chapter 2 close,
the next-chapter null rows, and the page-68 divider are separated by the
frozen cue-start rule. Raw text and times are unchanged by the semantic
repairs.

The final residual scan found zero source-commentary hits, zero formula
delimiter or slash defects, zero canonical/lane field mismatches, zero
page-map violations, and zero material formula or operation conflicts. The
remaining uncertainty markers are intentional source-fidelity markers rather
than unresolved blockers.

Unresolved blockers: none
