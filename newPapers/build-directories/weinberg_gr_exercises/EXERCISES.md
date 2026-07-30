# Exercise edition

This tree is independent of the canonical `weinberg_gr` edition. Its strict
build exports only to:

`../../weinberg-gr-exercises/weinberg-gr-exercises.pdf`

Chapter 1 is the historical introduction and intentionally has no exercises.
Chapters 2--16 each load one file:

`latex/exercises/chapter2.tex` through
`latex/exercises/chapter16.tex`.

Each file prints an Exercises section followed by a Solutions section. The
chapter's original bibliography or references follow both sections.

The curated expansion is kept in modular fragments under
`latex/exercises/additional/`. Each applicable chapter has one exercise
fragment and one matching solution fragment. The chapter file inputs them
inside the corresponding section, preserving continuous chapter numbering.
There are currently 20 exercises and 20 solutions in each of Chapters 2--16.

## Authoring interface

Keep every source credit in the required second argument so it appears
immediately below the exercise title:

```tex
\begin{exercises}

\begin{exercise}[Weak-field limit]{Cambridge Part III, 2025 exam, Question 3}
Derive the requested result using signature \((-+++)\).
\label{ex:weak-field-limit}
\end{exercise}

\end{exercises}

\begin{solutions}

\begin{solution}
Give the corresponding worked solution here.
\end{solution}

\end{solutions}
```

Exercises and solutions are both numbered by chapter. Their counts and order
must match. Solutions are always printed in this edition.

Use the edition conventions throughout: signature \((-+++)\), compact
derivatives in long calculations, action \(I\), and worldline derivative
\(D/D\tau\). Source problems are adapted into those conventions rather than
preserving incompatible notation.

The source inventory and Cambridge archive coverage are recorded in
`EXERCISE_SOURCES.md`. Run:

```bash
python3 audit_exercises.py
./build_and_verify.sh --draft
```

Use `./build_and_verify.sh` for the strict release and export.
