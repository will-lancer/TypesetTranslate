# Release verification

Status: **work in progress (2026-08-01 errata rebuild complete)**

Canonical source: `../weinberg_vol1`

Verified errata export:
`../../weinberg-vol1-exercises.pdf`

## 2026-08-01 errata rebuild

Five confirmed corrections in `../weinberg_vol1/ERRATA.md` were mirrored into
this edition and protected by `audit_errata.py`.

- Canonical PDF: 528 pages, SHA-256
  `e65469e0822c64cccdddfd08c09554e84dd7df27f0021bd736763ea86ff04dd2`.
- Exercise PDF: 844 pages, SHA-256
  `1c45800449cf2f347fc2cf132c4a63083e552574135fa6ae6da40d08583c7f3d`.
- Both PDFs passed LaTeX error/reference checks, text extraction, Ghostscript
  interpretation, embedded/subset-font checks, and affected-page visual QA.
- The exercise PDF has zero overfull boxes.

The strict exercise-content gate remains blocked by pre-existing editorial
state outside this errata port: stale canonical-source hashes, Chapter 10
inventory/source-ID issues, and incomplete source-fidelity approval records.
Those findings were preserved rather than reset. The errata regression and
physical PDF checks pass, but this rebuild is not represented as a strict-gate
release.

The historical release record below is retained for provenance and does not
describe the current strict-audit state.

## Historical corpus record

The released volume contains 70 Weinberg exercises with 70 solutions and
177 supplementary parent exercises with 177 solutions.  The supplementary
ledger has 177 exact parent records drawn from 68 source documents:

- 51 parents use a first-choice source family;
- 60 parents are adaptations of one exact editorial parent;
- 117 parents are original syntheses inspired by broader source sections.

| Chapter | W ex./sol. | S ex./sol. | Adapted | Original-inspired |
|---:|---:|---:|---:|---:|
| 1 | 0/0 | 0/0 | 0 | 0 |
| 2 | 6/6 | 14/14 | 3 | 11 |
| 3 | 7/7 | 17/17 | 10 | 7 |
| 4 | 3/3 | 10/10 | 5 | 5 |
| 5 | 7/7 | 16/16 | 11 | 5 |
| 6 | 5/5 | 15/15 | 3 | 12 |
| 7 | 7/7 | 11/11 | 2 | 9 |
| 8 | 5/5 | 12/12 | 5 | 7 |
| 9 | 4/4 | 19/19 | 12 | 7 |
| 10 | 8/8 | 13/13 | 0 | 13 |
| 11 | 4/4 | 14/14 | 8 | 6 |
| 12 | 4/4 | 14/14 | 1 | 13 |
| 13 | 5/5 | 12/12 | 0 | 12 |
| 14 | 5/5 | 10/10 | 0 | 10 |

Chapter 1 is the sole count exception: exercises are intentionally omitted
from the historical introduction.  Chapters 4 and 14 meet the lower bound
with ten complete parents rather than inflating the count by splitting
dependent calculations.  Chapter-specific curation notes in
`EXERCISE_INVENTORY.md` document the same editorial decisions for every
nonhistorical chapter.

## Historical automated verification

- `audit_exercises.py --strict`: passed with zero warnings and zero failures.
- Inventory and ledger agreement: 70/70 W, 177/177 S, and 177/177 exact
  supplementary parent records.
- Volume-local source-ID and exact-parent-root duplication gates: passed.
- Full strict build and export: passed.
- LaTeX references: no undefined references or citations.
- Layout: no overfull boxes.
- PDF parsing and Ghostscript integrity checks: passed.
- Fonts: all embedded or subset.
- Completed page count: 756 A4 pages.

Series-wide cross-volume duplication remains a release-driver responsibility;
this record certifies the Volume I gates and does not represent a standalone
series-wide result.

## Historical pagination and visual QA

The generated pagination crosswalk was verified against the completed PDF.
Physical PDF pages equal the displayed Arabic page label plus six, accounting
for the title and Roman-numbered front matter.

Representative rendered pages inspected:

- physical 45: Chapter 1 historical no-supplement boundary;
- physical 106 and 111: Chapter 2 supplementary exercises and solutions;
- physical 506 and 517: Chapter 9 McGreevy Gaussian prompts and solutions;
- physical 660 and 672: Chapter 12 scale-symmetry prompt and solution;
- physical 743 and 747: Chapter 14 supplementary exercises and solutions;
- physical 755: supplementary-solutions-to-original-references transition.

## Historical release identity

- Stable export:
  `../../weinberg-vol1-exercises.pdf`
- SHA-256:
  `e619982622dedda8e1e5313263a602b12b95f43fdd0a06ac92660f3f4c54a304`
