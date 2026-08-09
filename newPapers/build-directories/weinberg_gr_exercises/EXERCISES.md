# Exercise edition

This tree is independent of the canonical `weinberg_gr` edition. Its strict
build exports only to:

`../../weinberg-gr-exercises.pdf`

Chapter 1 is the historical introduction and intentionally has no exercises.
Chapters 2--16 each load one file:

`latex/exercises/chapter2.tex` through
`latex/exercises/chapter16.tex`.

Each file prints an Exercises section followed by a Solutions section. The
chapter's original bibliography or references follow both sections.

The inherited positional environments and the fragments under
`latex/exercises/additional/` are provisional.  The release collection must
contain 10--30 audited exercises and matching solutions in each Chapter 2--16.
Empty fragments may remain as stable include points, but no legacy
`exercise`/`solution` environment may survive the strict audit.

## Authoring interface

Use the audited interfaces.  Their arguments are stable ID, chapter-local
display number, title, and exact printed source credit for a prompt; a solution
repeats the same ID, number, and title:

```tex
\begin{exercises}

\begin{sourceexercise}{GR-10-01}{1}{Weak-field radiation}{%
  University of Cambridge, Part III General Relativity, 2025,
  Paper 309, Question 3, printed p. 2 (PDF p. 2)}
State every definition, formula, connected subpart, and retained hint needed
to make the complete adapted parent independently usable in signature
\((-+++)\).
\end{sourceexercise}

\end{exercises}

\begin{solutions}

\begin{sourcesolution}{GR-10-01}{1}{Weak-field radiation}
Give a complete independent derivation, checking every requested subpart,
sign, limit, and interpretation rather than merely quoting the target result.
\end{sourcesolution}

\end{solutions}
```

The environment supplies labels `exercise:<ID>` and `solution:<ID>`.
Prompt/solution ID sets, titles, numbers, counts, and order must match.
Solutions are always printed in this edition.

Use the edition conventions throughout: signature \((-+++)\), compact
derivatives in long calculations, action \(I\), and worldline derivative
\(D/D\tau\). Source problems are adapted into those conventions rather than
preserving incompatible notation.

For each prompt, add one exact entry to `exercise-ledger.json` containing the
selected `source_parent_id`, chapter/number/title/printed credit, use mode,
explicit departures, and prompt/solution file paths.  The parent must already
be `selected` in `exercise-source-inventory.json`.  After drafting, add two
distinct passed reviews with the current prompt and solution hashes to
`source-fidelity-audit.json`; the required checklist is enforced by the audit.

The source policy and inventory entry points are recorded in
`EXERCISE_SOURCES.md`. During editing run:

```bash
python3 audit_exercises.py
./build_and_verify.sh --draft
```

Only `python3 audit_exercises.py --strict` and then
`./build_and_verify.sh` constitute the strict release gate and export.
