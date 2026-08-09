# Written-prose pass ledger

Date: 2026-08-09

Governing rules: `WRITING_STYLE.md`

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
- `basically`: retained once in the user's approved microcausality sentence.
- `let me`: retained once in the user's approved transition into the precise
  covariance statement.
- `kind of`: occurs only inside "this kind of fundamental theory."
- `I mean`: occurs only inside the definition "By a field I generally mean."
- `just`: occurs in meaningful constructions such as "just as" and in the
  user's approved line "I'll just write down the answer."
- Sentence-initial `so` survives only where it carries Yin's emphasis, such as
  "So, by contrast" and "So far, nothing surprising."

## Pass 3: voice

Status: complete

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

Questions that merely invited classroom participation were removed. Student
questions about normalization, vacuum energy, locality, and the construction
of the field operator were folded into the exposition.

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
- All 13 pages were rendered at 180 dpi and inspected. The two figures, long
  equations, field-operator definition, page breaks, and final problem-set note
  are readable and unclipped.
- The exported PDF and the built master are byte-identical. Their SHA-256 is
  `008e7367998b4c889816929d0f6caf643daec53814d920309a64ea087cdcb49f`.
- The old near-verbatim retention gate is intentionally inapplicable to this
  written-prose edition; source comments, transcript IDs, and source artifacts
  remain available for traceability.
