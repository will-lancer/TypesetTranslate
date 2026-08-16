# Source-faithfulness corrections ledger

This ledger records visible source irregularities that remain in the native
transcription. The source wording, notation, code, and index entries are kept
where the scan is legible. No silent mathematical or editorial repair is made.

| Source location | Visible source irregularity | Treatment |
| --- | --- | --- |
| Physical p. 55, printed p. 39 | The displayed equation reads `T^2-T+1=0`, while the following root solves `T^2+T-1=0`. | The displayed equation is preserved. The chunk carries a `ZHOU-SOURCE-ERROR` comment. |
| Physical p. 185, printed p. 169 | The Cox-Ingersoll-Ross diffusion term and its following sentence use `R(u)` rather than `R(t)`. | `R(u)` is preserved. The chunk uncertainty log records the visible notation. |
| Physical p. 189, printed p. 173 | The prose says “A mathematic approach” and the footnote says “It is not recommend, though”. | Both source wordings are preserved. |
| Physical p. 189, printed p. 173 | The C++ comment reads `reserver to avoid reallocation`. | The code comment is preserved verbatim. |
| Physical p. 190, printed p. 174 | The moving-average definition uses `B_{n-1}=NA`. | The source notation is preserved. |
| Physical p. 191, printed p. 175 | The insertion-sort prose says “and increases i step by step”. The pseudocode identifiers are printed as `beginindex`, `endindex`, `centerindex`, `merge1`, and `merge2`. | The wording and identifiers are preserved. |
| Physical p. 207, printed p. 191 | The finite-difference discussion uses `\Delta t` in `\alpha=\Delta t/(\Delta x)^2` while the surrounding grid uses `\Delta\tau`, and states the strict condition `1-2\alpha>0`. | The visible source formulas are preserved. |
| Physical pp. 209--211, printed pp. 193--195 | The index contains `homogenous linear equation`, `module`, and `orting algorithm`. | The spellings are preserved. |
| Physical p. 210, printed p. 194 | `Poisson process, 90` appears twice. | Both entries are preserved. |
| Physical p. 210, printed p. 194 | The index contains `product rule.; 33`. | The punctuation is preserved. |
| Physical p. 211, printed p. 195 | The index contains lowercase `european call`. | The capitalization is preserved. |

