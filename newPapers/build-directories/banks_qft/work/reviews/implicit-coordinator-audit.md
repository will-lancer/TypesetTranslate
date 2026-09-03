# Implicit-edition coordinator audit

Date: 2026-09-02

## Scope

This audit covers the editorial implicit exercises and worked solutions defined
by `implicit-exercises.json`. The canonical source is `banks-qft.pdf`, SHA-256
`31de7827e7bc636feaa7028fe4dbb63a718b3926ee43ff3d96d91185a44eafe3`.

## Exact coverage

| Unit | Exercise files | Solution entries | Independent report | Open in-scope findings |
|---|---:|---:|---|---:|
| Chapter 2 | 6 | 6 | `implicit-review-chapter02.md` | 0 |
| Chapter 3 | 16 | 16 | `implicit-review-chapter03.md` | 0 |
| Chapter 4 | 4 | 4 | `implicit-review-chapter04.md` | 0 |
| Chapter 5 | 4 | 4 | `implicit-review-chapter05.md` | 0 |
| Chapter 6 | 7 | 7 | `implicit-review-chapter06.md` | 0 |
| Chapter 7 | 5 | 5 | `implicit-review-chapter07.md` | 0 |
| Chapter 8 | 20 | 20 | `implicit-review-chapter08.md` | 0 |
| Chapter 9 | 23 | 23 | `implicit-review-chapter09.md` | 0 |
| Chapter 10 | 21 | 21 | `implicit-review-chapter10.md` | 0 |
| Chapter 11 | 1 | 1 | `implicit-review-chapter11.md` | 0 |
| Appendix C | 2 | 2 | `implicit-review-appendixC.md` | 0 |
| Appendix E | 1 | 1 | `implicit-review-appendixE.md` | 0 |
| **Total** | **110** | **110** | **12 reports** | **0** |

## Final static checks

- The inventory contains 110 records.
- `latex/implicit/` contains exactly 110 `I-*.tex` files.
- Every exercise file has one titled `exercise` wrapper whose ID matches its
  filename.
- The twelve unit solution files contain exactly 110
  `\BanksImplicitSolution` entries in inventory order.
- Exercise, solution, and hook ID sets are identical. Every set has 110 unique
  IDs.
- There are no missing, duplicate, or unexpected IDs.
- Placeholder, unfinished-marker, control-character, trailing-whitespace, and
  Unicode-dash scans are clean.
- Seven explicit labels occur across the implicit files. They are unique.
- The shortest solution contains 135 prose words after TeX commands and
  mathematics are removed from the count. Its derivation was independently
  reviewed.
- Each unit report records a PASS verdict with zero open in-scope findings.

## Files in this phase

- 110 files matching `latex/implicit/I-*.tex`
- 12 files matching `latex/solutions/*-implicit.tex`
- 12 files matching `work/reviews/implicit-review-*.md`
- this coordinator audit

The phase therefore contains 135 authored or reviewed files inside the stated
boundary.

## Source and base observations

The unit reports record source-sensitive qualifications and candidate base
errata. The main external items include Chapter 2 cross-reference mismatches,
the Chapter 3 placement order of `I-CH03-015` and `I-CH03-016`, Appendix C gamma
ordering and spin-label defects, and the overall normalization defects around
Banks's equations (6.8) and (6.9). This phase left chapter transcription,
ledgers, inventories, styles, masters, manifests, and release records unchanged.

## Build gate

`work/reviews/base-freeze.json` is absent at audit time. The serial
`master-implicit.tex` build, compiled-PDF inspection, and strict implicit release
remain gated. The requested coordinating-task message was attempted through the
app and blocked by its cross-task permission boundary. A direct user-authored
request is required before that message can be sent.
