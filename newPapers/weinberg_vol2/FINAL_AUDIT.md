# Weinberg Volume II final audit

Audit date: 2026-07-25

## Verdict

Complete. The modernized Volume II represents every content-bearing source
page from physical PDF pages 18--512 exactly once: Preface, Notation, the
dedication represented in the title matter, Chapters 15--23, all appendices,
Problems, References, the Author Index, and the Subject Index. Physical page
513 is blank and page 514 is the publisher's back cover; both are
intentionally excluded.

The stable full-volume export is `weinberg-vol2.pdf`, 434 A4 pages, SHA-256
`395af2912ec6fedbf330add5914410a85b6f083099d61eeede33604badbaf679`.
It is byte-identical to `latex/master.pdf`.

## Production inventory

- 118 of 118 production TeX files are reachable from the master include
  graph; there are no missing or orphaned production files.
- 1,665 of 1,665 numbered equations are present in strict chapter/section
  order, with continuous numbering, no duplicate equation labels or tags, and
  no tagged equation lacking a label.
- 50 problems and 284 reference entries match the chapter coverage manifests.
- 14 figures are redrawn in TikZ and the single source table is native TeX.
- The Author Index contains 468 entries and 413 scan-matched italic page
  tokens.
- The Subject Index contains 308 top-level entries and 71 subentries, for 379
  entries total.

Numbered-equation totals by chapter are:

| Chapter | Equations | Problems | References |
|---:|---:|---:|---:|
| 15 | 209 | 9 | 28 |
| 16 | 64 | 4 | 7 |
| 17 | 145 | 4 | 5 |
| 18 | 167 | 6 | 32 |
| 19 | 323 | 6 | 56 |
| 20 | 160 | 5 | 22 |
| 21 | 252 | 6 | 57 |
| 22 | 190 | 4 | 37 |
| 23 | 155 | 6 | 40 |
| **Total** | **1,665** | **50** | **284** |

## Reference integrity

The final include graph owns 2,033 unique labels and has no duplicates. It
contains 2,357 reference-use occurrences targeting 1,271 unique labels, with
zero missing targets.

Eighteen references explicitly point back to Volume I. The master defines
stable fallback anchors for all of them so their printed labels and links
remain valid:

- `app:9`
- `eq:5.2.7`, `eq:8.7.7`, `eq:8.7.38`, `eq:10.7.4`, `eq:10.8.16`
- `sec:2.7`, `sec:3.3`, `sec:5.4`, `sec:5.5`, `sec:7.3`, `sec:8.8`,
  `sec:9.1`, `sec:9.2`, `sec:10.4`, `sec:10.7`, `sec:12.3`, `sec:12.4`

All 18 fallbacks are used, in 26 reference occurrences. Of the 284 source
bibliography entries, 282 have inbound citations. The two uncited entries,
`ch15-ref-16` and `ch17-ref-2`, are legitimate source entries and are
therefore retained.

## Build and source checks

The final build command was:

`cd latex && latexmk -g -pdf master.tex`

The master log has no TeX errors, fatal errors, undefined references,
multiply-defined labels, duplicate destinations, or font warnings. All fonts
in the final PDF are embedded. Two inherited package-level notices are
intentional: JHEP reports that no contact e-mail was supplied, and the bundled
style requests the obsolete `hyperref` `pagecolor` option.

Nineteen bounded overfull line warnings remain in Chapters 15--20. Their
largest values by affected chapter are 17.36 pt (15), 10.03 pt (16), 9.74 pt
(17), 8.44 pt (18), and 10.99 pt (20). Each affected rendered line was checked
and remains inside the printable page without clipping or collision. Eight
underfull vertical boxes are harmless page balancing, and four underfull
horizontal boxes occur in narrow Subject Index entries.

The production TeX tree has zero uses of forbidden `\times`, `\mathscr`, or
`\mathbb{1}` notation; zero placeholders or conflict markers; and zero
trailing whitespace, tab, CRLF, missing-EOF-newline, or nonbreaking-space
defects. `git diff --check -- newPapers/weinberg_vol2` passes.

## Rendered-page QA

Every page of the 434-page integrated master was rasterized. Contact sheets
covering pages 1--422 were inspected for blank pages, clipping, collisions,
malformed figures/tables, broken chapter transitions, and page-boundary
defects. Final master pages 423--434 were rerendered after the independent
Author Index style audit and inspected at 180 DPI.

The final QA render locations were:

- `/private/tmp/weinberg-vol2-full-qa.TgzZTx/` for the complete pre-index
  sweep and chapter-by-chapter contacts.
- `/private/tmp/weinberg-vol2-final-index-qa.ubV6n2/` for the final integrated
  Author and Subject Index pages.

These raster and contact-sheet directories were temporary verification
artifacts and were removed during the final cleanup.

Chapter-level coverage files record the higher-resolution isolated visual
checks. Index-specific checks are recorded in
`latex/backmatter/reports/author-index.md`,
`latex/backmatter/reports/subject-index.md`, and
`latex/backmatter/reports/indexes-integrated.md`.

## Verification PDF manifest

The chapter-only PDFs below were generated and hash-verified during the final
audit, then removed as intermediate artifacts during repository cleanup. The
retained PDFs are the full-volume `weinberg-vol2.pdf` and its byte-identical
build artifact, `latex/master.pdf`.

| Artifact | Pages | SHA-256 |
|---|---:|---|
| `weinberg-vol2-chapter15.pdf` | 54 | `b95ac1004aa8093907ad9f3b94c92fe75582a0d8374004f4cf461c9e06e5f412` |
| `weinberg-vol2-chapter16.pdf` | 16 | `6f5c3093cf270339461134d2dac9a416beb9257ccf5b5d6b04fcdc4b16d1bed8` |
| `weinberg-vol2-chapter17.pdf` | 28 | `fd5789eb4468fb1cdfcf47e255ebba4341668cd9a086e3309d25c77bdd6ae11b` |
| `weinberg-vol2-chapter18.pdf` | 45 | `e4ec23b84afdf387ebaacf4dfed6970f2b452965d3c9c93685a9a07df1c2b88d` |
| `weinberg-vol2-chapter19.pdf` | 78 | `d8ab85c0ebd81b43023dfd8c15a21423b100ec33643d81dfc581f9f87ff524be` |
| `weinberg-vol2-chapter20.pdf` | 38 | `65971e69d8c712791f5be811fff8fa2c90cbaffe65f8151c3b05779bcba12339` |
| `weinberg-vol2-chapter21.pdf` | 56 | `e90e61804ce2beac92b978794ca6a130d2dc344341868dce0980053a24eab822` |
| `weinberg-vol2-chapter22.pdf` | 53 | `e9dd7ad4082e93ed065fd69679930e494e810117e5c146d5844a387e5c93239e` |
| `weinberg-vol2-chapter23.pdf` | 49 | `06219afea3b0350517be2e12f4fbe29aa15aea75b6ee7d80d434a615a2a4ade8` |
| `weinberg-vol2.pdf` | 434 | `395af2912ec6fedbf330add5914410a85b6f083099d61eeede33604badbaf679` |

All acceptance gates in `COMPLETION_PLAN.md` are satisfied.
