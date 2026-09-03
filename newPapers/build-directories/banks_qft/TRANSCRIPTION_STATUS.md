# Transcription status

The native transcription covers all 281 physical source pages under the
disposition ledger. Its 271 included source pages, four generated front-matter
pages, and six omitted blanks are fixed. The source review spans physical pages
1--281. Equation, figure, prose, problem, reference, and index checks are
recorded in the release evidence.

| Unit | Source pages | Native content | Review scope |
| --- | ---: | --- | --- |
| Chapters 1--11 | 11--254 | complete | equations, figures, prose, problems |
| Appendices A--F | 255--271 | complete | equations, diagrams, prose |
| References and indices | 272--281 | complete | entries and locators |
| 80 numbered solutions | source matched | complete | independent mathematical review |
| 110 implicit exercises | source matched | inventory and anchors frozen | edition audit and solution review |

The machine-readable release records under `work/` carry the current build,
review, render, and PDF hashes for each edition.

The complete native closure now uses the convention map in `NOTATION.md`.
Edition-specific convention audits scan the TeX closure and its supporting
records. Fresh source and solution reviews bind their verdicts to each native
snapshot. Strict release records then bind those reviews to deterministic
build inputs, rendered pages, and the released PDF bytes.
