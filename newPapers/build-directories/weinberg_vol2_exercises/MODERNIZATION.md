# Modernization policy for exercise material

The canonical transcription has already modernized notation while preserving
Weinberg's content. This exercise edition follows that work; it does not
perform a second modernization pass on the book.

- Preserve Weinberg's extracted exercise wording and mathematical content.
- Write all new editorial solutions and supplementary material in the
  conventions of `NOTATION.md` and the chapter being extended.
- Replace cumbersome presentation only in editorial material: use Dirac
  states, compact derivatives, `\mathcal` rather than decorative `\mathscr`
  where the canonical edition does so, and `H_I` for the interaction
  Hamiltonian.
- Keep original equation, section, figure, bibliography, and reference
  numbering. Editorial displays should normally be unnumbered.
- Do not change physical assumptions to make a sourced problem fit. Adapt its
  presentation, or omit it.
- Mark third-party provenance exactly and write solutions independently.

Any mathematical correction to an original Weinberg problem must be handled
as an explicit editorial note, never as a silent rewrite of the prompt.

## Exercise-edition layout adjustments

Long displays in Sections 15.7 and 17.5 are broken across additional lines in
this independent copy. The adjustments remove inherited overfull boxes and
do not change their mathematical content, symbols, or equation numbers.

The inherited Author and Subject Index entries retain Weinberg's printed
source pagination. A visible note now distinguishes those source-page
references from this expanded PDF's live pages; `INDEX_PAGINATION.md` is
regenerated after every build as the navigation crosswalk.
