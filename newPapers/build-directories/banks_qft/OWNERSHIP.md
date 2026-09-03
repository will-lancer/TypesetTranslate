# Ownership and handoff contract

The lead owns masters, styles, manifests, ledgers, release scripts, and final
integration. Workers edit only the files named in their assignment. Physical
page ranges stay disjoint during each wave. One boundary page on either side
may be read without editing another lane's content.

## Frozen pilot

| Lane | Physical pages | Owned file | Coverage |
| --- | ---: | --- | --- |
| pilot-prose | 11-13 | `latex/chapters/chapter01/sec1_1.tex` | Chapter opening, Sec. 1.1, prose, footnotes, displays |
| pilot-problems | 23-26 | `latex/chapters/chapter02/problems.tex`, `latex/solutions/chapter02-numbered.tex` | Problems 2.1-2.11 and solutions |
| pilot-figures | 261-265 | `latex/appendices/appendixD.tex`, `latex/figures/appendixD.tex` | Appendix D formulas and vector Feynman-rule figures |

## Handoff fields

Each handoff records source pages, source markers, displayed equations,
figures, footnotes, problem or exercise IDs, unresolved glyphs, and checks run.
The lead accepts a lane after direct diff review and a harness build.

## 2026-09-02 convention adaptation

Each chapter has one exclusive collaboration editor. The appendix closure has
its own editor. Shared policies, masters, manifests, audits, and release files
remain with the lead.

| Lane | Exclusive scope |
| --- | --- |
| chapter01 | Chapter 1 source and Chapter 1 figure annotations |
| chapter02 | Chapter 2 source, problems, numbered and implicit solutions, implicit exercises, figures |
| chapter03 | Chapter 3 source, problems, numbered and implicit solutions, implicit exercises, figures |
| chapter04 | Chapter 4 source, problems, numbered and implicit solutions, implicit exercises, figures |
| chapter05 | Chapter 5 source, problems, numbered and implicit solutions, implicit exercises, figures |
| chapter06 | Chapter 6 source, problems, numbered and implicit solutions, implicit exercises, figures |
| chapter07 | Chapter 7 source, problems, numbered and implicit solutions, implicit exercises, figures |
| chapter08 | Chapter 8 source, problems, numbered and implicit solutions, implicit exercises, figures |
| chapter09 | Chapter 9 source, problems, numbered and implicit solutions, implicit exercises, figures |
| chapter10 | Chapter 10 source, problems, numbered and implicit solutions, implicit exercises, figures |
| chapter11 | Chapter 11 source, implicit solution, and implicit exercise |
| appendices | Appendices A--F, appendix implicit material, and Appendix D figures |

Full builds are serialized after integration. Independent reviewers receive a
frozen native snapshot and disjoint source, solution, and rendered-page ranges.

## Production transcription

| Lane | Source scope | Owned files |
| --- | --- | --- |
| T1 | Chs. 1-3; Apps. A-C; references | matching chapter, appendix, figure, and backmatter files |
| T2 | Chs. 4-6; both indices | matching chapter, figure, and backmatter files |
| T3 | Ch. 7; Ch. 8 through Sec. 8.6; Apps. E-F | matching chapter, appendix, and figure files |
| T4 | Ch. 8 Secs. 8.7-8.10; Ch. 9 through Sec. 9.4; Ch. 11 | matching chapter and figure files |
| T5 | Ch. 9 Secs. 9.5-9.16 | matching chapter and figure files |
| T6 | Ch. 10 | matching chapter files |

Appendix D and Chapter 2 problems remain the accepted pilot files. Numbered
solutions outside Chapter 2 belong to the later solution wave.
