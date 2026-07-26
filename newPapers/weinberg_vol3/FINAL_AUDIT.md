# Weinberg Volume III final audit

Audit date: 2026-07-25

## Verdict

Complete. The modernized Volume III contains a new title page and generated
contents, followed by the complete Preface, Notation, Chapters 24--32, all
five chapter appendices, all Problems and References, the Author Index, and
the Subject Index.

The source scan's physical pp. 6 and 8--16 are represented by the new title
and contents matter. Physical pp. 17--442 are represented from the Preface
through the final Subject Index entry. Physical p. 443 is intentionally
blank. The publisher cover, promotional endorsements, and copyright
colophon on physical pp. 1--5 and 7 are deliberately not reproduced.

The stable full-volume export is `weinberg-vol3.pdf`, 373 A4 pages,
2,199,796 bytes, SHA-256
`5a69c9fbd0fa6f3ef570e88750762b71ce9f2980a634530d0356f9a823c68f3d`.
At export time it was byte-identical to `latex/master.pdf`; that duplicate
build artifact was removed during the final cleanup.

## Production inventory

- All 95 semantic production TeX files are reachable from the master include
  graph; there are no missing inputs or orphan semantic sources.
- The book contains 9 chapters, 49 numbered sections, 5 chapter appendices,
  9 problem sets, 9 chapter reference lists, and 2 indexes.
- All 1,433 numbered equations have unique, matching tags and labels in
  strict chapter/section order.
- The chapter back matter contains 39 problems and 167 displayed reference
  entries.
- Nine figures are reconstructed in TikZ and the single source table is
  native TeX.
- The Author Index contains 376 entries and 597 semantically italicized
  publication-page references.
- The Subject Index contains 168 top-level entries and 48 indented
  subentries.

Chapter totals are:

| Chapter | Equations | Problems | References |
|---:|---:|---:|---:|
| 24 | 61 | 3 | 16 |
| 25 | 119 | 4 | 3 |
| 26 | 247 | 6 | 10 |
| 27 | 218 | 5 | 21 |
| 28 | 148 | 5 | 59 |
| 29 | 209 | 3 | 13 |
| 30 | 33 | 3 | 2 |
| 31 | 289 | 6 | 28 |
| 32 | 109 | 4 | 15 |
| **Total** | **1,433** | **39** | **167** |

## Reference integrity

The final semantic include graph owns 1,640 unique labels, including 30
stable cross-volume anchors, with no duplicates. All 2,080 `ref`, `eqref`,
and `hyperref` occurrences resolve. All 167 chapter-reference targets are
used, and all 267 linked bibliography-marker occurrences point to the
correct chapter and displayed reference number.

The 30 fallback anchors preserve links to printed equations in Volumes I and
II:

- `eq:2.4.12`, `eq:2.4.13`, `eq:3.4.3`
- `eq:5.4.6`, `eq:5.4.35`, `eq:5.4.40`, `eq:5.5.23`, `eq:5.5.42`
- `eq:6.2.16`, `eq:9.5.40`
- `eq:17.5.33`, `eq:17.5.34`, `eq:17.5.35`, `eq:17.5.41`
- `eq:18.7.2`, `eq:19.7.2`
- `eq:21.1.17`, `eq:21.3.19`, `eq:21.3.30`, `eq:21.3.34`,
  `eq:21.5.15`, `eq:21.5.16`
- `eq:22.2.24`, `eq:22.2.26`
- `eq:23.5.4`, `eq:23.5.19`, `eq:23.5.20`, `eq:23.5.21`,
  `eq:23.5.23`, `eq:23.6.26`

## Build and source checks

The final build command was:

`cd latex && latexmk -g -pdf -interaction=nonstopmode -halt-on-error master.tex`

The final log has no TeX errors, fatal errors, undefined references,
multiply-defined labels, duplicate destinations, missing glyphs, or rerun
diagnostics. All fonts in the final PDF are embedded. The only package-level
notices are the inherited JHEP missing-email notice and the bundled style's
obsolete `hyperref` `pagecolor` option.

Twenty-two bounded overfull horizontal-box warnings remain: 2 in Chapter 24,
5 in Chapter 26, 9 in Chapter 27, and 6 in Chapter 28. Their chapter maxima
are 25.70 pt, 41.26 pt, 29.56 pt, and 4.59 pt, respectively. One 1.09 pt
overfull vertical box remains in Chapter 29. Every affected page was
inspected at full resolution; all content remains inside the printable page
without clipping or collision. Eleven underfull vertical boxes are harmless
page balancing. Seven underfull horizontal boxes are one prose line and six
narrow Subject Index entries.

The production tree has no active TODOs, placeholders, conflict markers, or
missing semantic files. `git diff --check -- newPapers/weinberg_vol3`
passes.

## Rendered-page QA

Every page of the 373-page integrated master was rasterized at 120 dpi.
Twenty-five contact sheets were inspected for blank pages, clipping,
collisions, malformed equations, broken figures/tables, damaged chapter
transitions, and page-boundary defects.

Independent audits covered master pp. 1--120, 121--240, and 241--373. They
also inspected at full resolution the title and contents, every chapter
opening, section/appendix/Problems/References boundaries, every known layout
warning page, Table 28.1, Figures 27.1, 28.1--28.7, and 29.1, and all nine
integrated index pages. The complete final render was generated under
`/private/tmp/weinberg-vol3-final.VMTyij/` and removed after the audit.

All chapter-local coverage files record their higher-resolution isolated
checks. The final integrated sweep found no missing page, unexpected blank,
clipping, overlap, malformed display, broken caption, bad page number, or
release-blocking layout defect.

## Verification PDF manifest

The chapter-only PDFs below were generated and hash-verified during the final
audit, then removed with the isolated checks and build auxiliaries. The sole
retained PDF is the complete `weinberg-vol3.pdf`.

| Artifact | Pages | SHA-256 |
|---|---:|---|
| `weinberg-vol3-chapter24.pdf` | 20 | `19db1729062aa60d6260e769fd8c5ad1cde9acdb371c572140763a57ac6c922b` |
| `weinberg-vol3-chapter25.pdf` | 26 | `ee868e62a502bb7589140ae7f36bc2dfa3c8d5793ff279f4e1c30e775cb4f993` |
| `weinberg-vol3-chapter26.pdf` | 54 | `16101d7fd261df485a5784555ee4541ac3c78b119f0227304738b8a6a0a45556` |
| `weinberg-vol3-chapter27.pdf` | 59 | `088aa971eaf468cea5ae9be7b0771ae824e05d0b40cb9900176487414fd4bf64` |
| `weinberg-vol3-chapter28.pdf` | 60 | `755e0264f4c22e7602c99e9fbdb2a52b0744d6e0633603b6a90ef483e9ea3516` |
| `weinberg-vol3-chapter29.pdf` | 52 | `0bcaf5fa56ac3f76c33f0e0cb291f165b8931d7efcf069e2923a834ccda13f35` |
| `weinberg-vol3-chapter30.pdf` | 10 | `340898a95be605e74b6685a18e406fc2bf454e7b5b5764dcd65c581016e503d6` |
| `weinberg-vol3-chapter31.pdf` | 58 | `10e12df8502244892c08de7bb9e0dc1b53e7188fe79155f7306d02c9a4220e10` |
| `weinberg-vol3-chapter32.pdf` | 25 | `d6f975ae964a7059c978e4dcc50c2a899927ccd30e63d7cbedf32f22c0e33c59` |
| `weinberg-vol3.pdf` | 373 | `5a69c9fbd0fa6f3ef570e88750762b71ce9f2980a634530d0356f9a823c68f3d` |

All acceptance gates in `COMPLETION_PLAN.md` are satisfied.
