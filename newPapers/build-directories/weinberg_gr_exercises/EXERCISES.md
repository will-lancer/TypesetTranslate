# Adding exercises

This build tree is independent of the canonical `weinberg_gr` edition. Its
strict build exports only to:

`../../weinberg-gr-exercises/weinberg-gr-exercises.pdf`

Each chapter has an insertion file:

`latex/exercises/chapter1.tex` through
`latex/exercises/chapter16.tex`.

The files are empty by default, so the initial compiled book is visually
identical to the canonical copyright-free edition. To add exercises to a
chapter, edit only that chapter's exercise file:

```tex
\begin{exercises}

\begin{exercise}[Weak-field limit]
Derive the requested result.
\label{ex:1.1}

\exercisesolution{A solution may be placed here.}
\end{exercise}

\end{exercises}
```

Exercises are numbered by chapter, such as `Exercise 1.1`. Labels and ordinary
LaTeX cross-references work normally.

Solutions are hidden by default. Change
`\printexercisesolutionsfalse` to `\printexercisesolutionstrue` in
`latex/exercises/setup.tex` to include them.

Run `./build_and_verify.sh --draft` while writing and
`./build_and_verify.sh` for a strict export.
