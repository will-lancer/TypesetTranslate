# Result-environment audit

## Scope

This pass covers the shared result definitions in
`latex/pct.sty` and every theorem-like environment call in the native
transcription. Chapter files were read for the call-site inventory and were
left unchanged.

The scan found 41 numbered result-environment openings across the chapter
files. Twenty-five carry an optional source identifier. Sixteen use the
ordinary no-argument form. The optional forms are all `theorem` environments;
they include identifiers from `2-3` through `2-10`, `3-7` through `3-9`,
`4-2` through `4-5`, and `4-14` through `4-22`, together with the
source-named form `[Theorem 2-11]` and the titled form
`[4-16 \emph{(Haag's Theorem)}]`.

## Defect reproduced

Before the style change, amsthm treated a source identifier as a parenthetical
note after its automatic counter. A minimal file therefore extracted as:

```text
Theorem 1-1 (4-14). Explicit identifier.
Theorem 1-2 (4-16 (Haag's Theorem)). Named identifier.
Theorem 1-3 (Theorem 2-11). Named prefix.
```

The source identifier was visually duplicated or displaced into the note
position. Labels still carried the automatic counter.

## Repair

`pct.sty` now recognizes an optional result argument containing a chapter-
result identifier. It accepts a bare identifier, a standard result-name
prefix, and a source title after the identifier. The identifier is placed in
the main result-number slot, with any title retained after it. The amsthm
head builder remains responsible for JHEP spacing and typography. The shared
automatic counter still advances, so later unnamed results keep a consistent
sequence.

The style also exposes starred unnumbered forms for theorem, lemma,
proposition, corollary, claim, definition, example, remark, and observation.
Ordinary non-identifier optional notes retain amsthm's parenthetical form.
The explicit identifier is copied into `\@currentlabel` after the amsthm head
is assembled, which makes a following `\label` resolve to the printed source
number. The hyperref label name is set to the corresponding result heading.

The Weinberg helper required by `NOTATION.md` is now present:

```tex
\newcommand{\InKetWith}[2]{\ket{#1}_{\mathrm{in},#2}}
```

## Minimal compile

The test harness was `/private/tmp/pct-result-env.tex`. It exercised:

- `theorem[4-14]`;
- `theorem[4-16 \emph{(Haag's Theorem)}]`;
- `theorem[Theorem 2-11]`;
- an ordinary theorem with no optional argument;
- an ordinary remark note;
- `theorem*` and `lemma*` with names;
- an automatic lemma;
- `\InKetWith{\alpha}{\epsilon}` in math mode;
- labels and cross-references for every numbered theorem case.

The command was run twice for cross-reference resolution:

```text
TEXINPUTS=.../pct_spin_statistics_all_that/latex: \
  pdflatex -interaction=nonstopmode -halt-on-error \
  -output-directory=/private/tmp /private/tmp/pct-result-env.tex
```

Both passes returned exit code 0. The extracted result headings were:

```text
Theorem 4-14. Explicit identifier.
Theorem 4-16 (Haag's Theorem). Named identifier.
Theorem 2-11. Named prefix.
Theorem 1-4. Automatic identifier.
Remark 1-5 (Ordinary note). Ordinary note.
Theorem (Unnumbered named). Unnumbered result.
Lemma 1-6. Automatic lemma.
Lemma (Unnumbered lemma). Unnumbered lemma.
States: |α⟩in,ϵ .
```

The resolved references in the extracted PDF were `4-14`, `4-16`, `2-11`,
and `1-4`. The auxiliary labels recorded the same values and retained the
standard theorem anchors. The log contained no LaTeX errors, undefined
control sequences, missing-dollar diagnostics, overfull boxes, underfull
boxes, or multiply-defined-label warnings.

A second two-pass harness loaded the local `jheppub.sty` before `pct.sty`.
It returned exit code 0 and extracted `Theorem 4-14`, `Theorem 2-11`, and
`Theorem 1-3`, with resolved references `4-14`, `2-11`, and `1-3`. Its log had
no theorem-environment or layout diagnostics.

## Files changed

- `latex/pct.sty`: result-head parser, starred result environments, and
  `\InKetWith`.
- `work/reviews/result_environment.md`: this audit record.

Unresolved blockers: none
