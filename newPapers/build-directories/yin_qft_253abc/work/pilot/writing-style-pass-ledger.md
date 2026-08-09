# Written-prose pass ledger

Date: 2026-08-09

Governing rules: `WRITING_STYLE.md`

Chapter SHA-256:
`df431b6e60ee29d489a91eaa4beb9fc9c61ec198b0cdf5acd8d393996090ec82`

## Reference prose

The prose model is Xi Yin's *Foundations of String Theory*, taken from the
author's official repository. The downloaded reference PDF has 845 pages and
SHA-256
`54694a11d5b79ebf34003dcf62cc4d96c31fe27829019d9797344b0bc6fea635`.

The close-reading sample covered:

- the Preface and Prologue, physical PDF pages 18--40;
- Appendix D, "Local quantum field theories," physical PDF pages 676--684;
- technical exposition from the AdS chapters, physical PDF pages 458--474.

The reference prose usually begins a paragraph with the claim, places an
equation directly after its motivation, and uses a question only when the
question organizes the argument. It retains occasional dry humor and informal
phrases. Lecture-floor markers are nearly absent.

## Pass 1: structure

Status: complete

- Merged transcript-sized fragments into conceptual paragraphs while keeping
  every source marker in chronological order.
- Kept the course overview, the free-particle construction, causality,
  Poincare covariance, microcausality, and the free scalar construction as the
  seven governing subsections.
- Placed the coordinate transformation, commutators, Hamiltonians, covariance
  law, and field expansion in display environments at their point of use.
- The full free-field expansion remains displayed rather than embedded in a
  prose line.

## Pass 2: filler

Status: complete

The whole chapter was scanned for `okay`, `all right`, `you know`, `I mean`,
`well`, `actually`, `just`, `basically`, `kind of`, `sort of`, and `let me`.

- `okay`, `all right`, `you know`, and `actually`: zero visible occurrences.
- `basically`: two approved occurrences, in the rough opening answer and the
  intuitive statement of microcausality.
- `let me`: five approved occurrences recording a course map, provisional
  definition, normalization choice, causality transition, and move to the
  precise covariance law.
- `kind of`: three approved occurrences identifying a class of theories, the
  free model just solved, and the causal property under discussion.
- `I mean`: three approved definitions, for $D$, non-interaction, and the word
  field.
- `just`: six approved occurrences carrying comparison, restriction, or a
  precise backward reference.
- Sentence-initial `so`: four approved transitions, including "So, by
  contrast" and "So far, nothing, no big deal."

## Pass 3: voice restoration

Status: complete

The chapter was reread argument by argument against the minimally cleaned
transcript. The positive ledger contains 33 approved cues across all seven
argument units. Each cue cites exact frozen speech, records an exact or lightly
recast treatment, names its rhetorical function, and points to the current
printed phrase.

The pass restored or retained the following characteristic phrases and turns:

- "some folks" and the emphatic correction that QFT is a specialization of
  quantum mechanics;
- "good old nonrelativistic quantum mechanics";
- the observation that Feynman diagrams have everything to do with the
  perturbative expansion of a path integral;
- "if it smells like a particle, looks like a particle, it will be a
  particle";
- "I do not care" in the question about how free-particle states were created;
- "you can go home" after the free theory is solved;
- "what the heck is $\widehat\phi(x)$ in this model?"

It also restored quieter parts of Yin's voice: "This question is very easy to
answer," "you are probably not very impressed," "I will let you verify for
yourself," "you are welcome to try," "by inspection," and the arbitrary
rescaling "to the one-third power, or whatever." These phrases carry reader
address, pacing, understatement, or a concrete example.

Questions that merely invited classroom participation were removed. Student
questions about normalization, vacuum energy, locality, and the construction
of the field operator were folded into the exposition.

All 33 records in `voice-restoration.jsonl` were checked against the frozen
transcript and the chapter SHA above.

## Pass 4: logic and referents

Status: complete

- Removed the repeated threefold statement of why field theory is needed and
  replaced it with one general question followed by its precise relativistic
  form.
- Repaired the distinction between a one-particle sector and an entire Hilbert
  space.
- Made every occurrence of "this" and "it" refer to the immediately preceding
  model, transformation, condition, or operator.
- Kept contrasts only where the adjacent claims supply both sides.
- Replaced board narration with references to the displayed formula or figure.

## Pass 5: mathematics and notation

Status: complete

- Spatial vectors use `\mathbf`; the chapter contains no `\vec`.
- The chapter contains no `\noindent` or `\ensuremath`.
- There are no reader-facing uncertainty markers or hidden-text commands.
- All long transformation laws, commutators, generators, and field definitions
  are displayed.
- The reconciled signs, measures, metric convention, creator notation, and
  proper-orthochronous Lorentz qualifier remain unchanged.

## Pass 6: build and render

Status: complete

- The final chapter compiles to 13 A4 pages.
- The log contains no overfull boxes, underfull boxes, undefined references, or
  missing-glyph warnings.
- All 13 pages were rendered at 180 dpi in the directory named by the PDF hash
  and inspected. The two figures, long equations, field-operator definition,
  page breaks, and final problem-set note are readable and unclipped.
- Two forced builds are byte-identical. Their SHA-256 is
  `ae874ea093e48619a2c369ffe3be12b424ebaf69798ed1a2bd7ebcf69d355a14`.
- The render manifest SHA-256 is
  `935669ce833e2820c5c6d569ba2d11b9e6e37733827ef61d3c4f807aff5f1f8e`.
- The old near-verbatim retention gate is intentionally inapplicable to this
  written-prose edition; source comments, transcript IDs, and source artifacts
  remain available for traceability.
