# Xi Yin prose ledger

This ledger governs the conversion of the Physics 253abc lectures into written exposition. The prose model is Xi Yin's *Foundations of String Theory*, especially the Prologue and Appendix D, "Local quantum field theories." The inspected reference PDF has 845 pages and SHA-256 `54694a11d5b79ebf34003dcf62cc4d96c31fe27829019d9797344b0bc6fea635`. The lecture remains the source of content, emphasis, examples, and personality.

## Governing principle

Write what Yin would plausibly have written after teaching the lecture. Preserve his line of thought and his characteristic turns of phrase. Remove the machinery of live speech.

The default is preservation. Ordinary connective language, qualifications,
questions, and first-person remarks also carry voice; the memorable jokes are
only the most visible part of it. Before removing or replacing a phrase, decide
whether it performs mathematical, rhetorical, interpersonal, or purely
classroom work. Preserve the first three functions. Remove only the classroom
mechanics.

Begin from Yin's minimally cleaned sentences within each argument unit. Join
adjacent fragments, repair syntax and referents, and make the smallest changes
that produce good written prose. Generic synonyms are not improvements. A
sentence that already reads well after its false start or caption seam is
removed should keep Yin's vocabulary and order.

The cleaned transcript is never the paragraph skeleton. Build the paragraph
from the argument first, then attach the supporting transcript spans. A draft
that follows caption boundaries has failed the structural pass even when every
word is accurate.

## Preserve

- Conceptual questions that organize the discussion, such as "Why do particle physicists need field theory?"
- Memorable informal phrases that sharpen a point, such as "what the heck," "some folks," "you can go home," and "if it smells like a particle, looks like a particle, it will be a particle."
- Self-corrections that change the mathematical statement or prevent a misconception.
- First-person guidance when it records a convention or a deliberate choice: "We work in units with (c=1)," "I use the mostly-plus signature," or "We will return to this point."
- Repetition when it carries emphasis, especially a deliberate correction such as "QFT is not a generalization of quantum mechanics; it is a specialization."
- The lecture's order of ideas, examples, caveats, and jokes.
- Ordinary authorial contact with the reader: "you might ask," "you can verify
  for yourself," "I would say," and similar phrases when they guide the
  argument.
- Rhetorical pacing such as "But that is not all," "So far, nothing, no big
  deal," or "It is not obvious" when it marks the pressure point of an
  argument.

## Remove or rewrite

- Pure floor-holding: "okay," "all right," "well," "you know," "I mean," and sentence-initial "so."
- Narration of board work: "let me write," "I am going to draw," "take a couple minutes," and "here is the equation," unless the act itself matters.
- Empty temporal markers: "now," "at this point," "for the moment," and "later on" when the sentence already fixes the order.
- Softening that adds no meaning: "kind of," "sort of," "basically" when it merely delays the claim, "perhaps" when no uncertainty is intended, and repeated "actually."
- Repeated previews and recaps. State a result once near the equation or argument it governs.
- Transcript seams, clipped phrases, invitations for questions, acknowledgments, and classroom management.
- Speaker labels when the mathematical question can be incorporated directly into the exposition.

## Written syntax

- Begin a paragraph with its subject or claim. Use "We begin," "We consider," "Let us," "It follows," and "In particular" when they describe a real logical move.
- Keep one conceptual job per paragraph. Merge short transcript fragments that belong to the same argument.
- Put a displayed equation immediately after the sentence that defines or motivates it. Explain notation after the display only when the explanation is not already clear.
- Prefer direct definitions: "A local field operator obeys..." rather than "What I want to say is that there is some operator that is supposed to..."
- Prefer explicit logical relations over spoken sequencing. Use "therefore," "however," "for instance," and "in contrast" only when the relation is present.
- Use questions sparingly. A retained question must open a problem, expose a misconception, or carry Yin's personality.
- Avoid consecutive paragraphs beginning with the same transition.

## Binding examples

These examples set the allowed degree of editing.

Preserve the full correction and its voice:

> This kind of fundamental theory, first of all, is a quantum-mechanical
> system. Some folks might have the slight misconception that quantum field
> theory, going beyond quantum mechanics, is a generalization of quantum
> mechanics: no, quantum field theory is not a generalization of quantum
> mechanics. Quantum field theory is a specialization of quantum mechanics.

Do not compress this to a generic statement that drops "first of all," "some
folks," or the explicit correction.

Keep a useful informal transition when it carries the speaker's emphasis:

> Basically, this is a precise quantum-mechanical statement that captures the
> idea that signals cannot propagate faster than the speed of light in a
> relativistic theory.

Remove filler without flattening the cadence:

> So, by contrast, there are plenty of examples of quantum field theories that
> are completely well-defined at strong coupling. These effective field
> theories are typically only defined as a formal perturbative series in the
> coupling constant, and it may not have a well-defined limit. In particular,
> it may or may not converge.

Merge repeated questions and board instructions into the argument:

> But the key question you might ask is: what the heck is
> $\widehat{\phi}(x)$ in this model? Does it even exist? That is, does an
> operator $\widehat{\phi}(x)$ exist that satisfies all of the nice properties
> we just demanded?
>
> The answer is yes, but it's not totally obvious. We'll have a different way
> to understand this later, but for now I'll just write down the answer.

When a spoken explanation introduces a long formula, finish the motivation and
place the formula in a display. Continue with the interpretation afterward.
The coordinate transformation, metric-preserving condition, and free-field
expansion are separate displays.

## Mathematical presentation

- Use \\mathbf for spatial vectors.
- Reserve inline math for short expressions. Definitions, transformation laws, commutators, field expansions, and multi-part identities belong in display environments.
- Keep the notation and sign conventions fixed by the handwritten notes and the reconciled equation layer.
- Preserve a source ambiguity in a comment or ledger rather than turning it into awkward reader-facing prose.

## Editorial checks

These checks belong inside the five passes in `WORKFLOW.md`. They do not create
additional passes.

During chapter drafting:

- merge transcript-sized fragments into arguments;
- place equations at the point of use;
- keep source order, examples, caveats, and voice cues visible in the draft.

During editorial balance:

- inspect `okay`, `so`, `well`, `you know`, `all right`, `I mean`, `just`,
  `actually`, `basically`, `kind of`, and `let me`;
- reread the complete chapter against the minimally cleaned transcript;
- restore characteristic vocabulary, cadence, qualifications, reader address,
  jokes, corrections, and conceptual questions lost during drafting;
- verify connectives, pronouns, and paragraph flow;
- update `work/<chapter>/voice-restoration.jsonl` and the style exceptions.

During fidelity and release:

- compare every displayed formula with the reconciled note layer;
- inspect long inline mathematics and notation;
- build the PDF and inspect every affected page.

## Voice-restoration ledger

Every `voice_cues` entry in the argument map is a positive drafting
requirement. `work/<chapter>/voice-restoration.jsonl` records:

- the argument and transcript record supplying the cue;
- a short exact source phrase;
- the treatment, either `retained_exact` or `lightly_recast`;
- the exact printed phrase;
- the function served by the phrase;
- the current chapter SHA-256 and an approval status.

The printed phrase must occur in the current chapter. The source phrase must
occur in the frozen minimally cleaned transcript. A cue cannot be satisfied by
an omitted phrase. When a cue turns out to be classroom mechanics, remove it
from the approved argument map and replace it with a genuine voice cue before
drafting.

## Conversational-phrase ledger

The following expressions require an explicit record in
`work/<chapter>/style-exceptions.jsonl` whenever they survive into print:

- `basically`;
- `kind of`;
- `I mean`;
- `just`;
- `let me`;
- sentence-initial `So` or `Now`;
- `for the moment`.

Each exception names the exact printed sentence, source IDs, expected
occurrence count, and reason the phrase carries conceptual or stylistic work.
Unlisted occurrences fail the written-prose audit.

## Mechanical checks

- No `\\noindent`, `\\ensuremath`, `\\vec`, transcript ellipses, or reader-facing uncertainty markers.
- No hidden text used to satisfy an audit.
- No large formula embedded in a prose line.
- Every retained conversational phrase must do conceptual or stylistic work.
- The chapter must compile without overfull boxes, undefined references, or malformed glyphs.
- Runs of caption-sized paragraphs fail the structural pass even when the
  individual sentences are grammatical.
