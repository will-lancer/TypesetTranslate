# Exercise source policy and entry points

The inherited exercise layer is provisional and is not a source ledger.  Its
300 item-level decisions are frozen in
`provisional-exercise-dispositions.json`; the twelve question-resolvable
rebuild candidates have side-by-side completeness findings in
`provisional-exact-parent-comparisons.json`.  The replacement edition accepts an
exercise only when one complete parent problem has been inspected, selected in
`exercise-source-inventory.json`, bound to one stable exercise ID in
`exercise-ledger.json`, and passed both source-fidelity and independent-solution
review in `source-fidelity-audit.json`.  Each final exercise prints an exact
document/question/page credit; any adaptation or convention departure is
recorded explicitly.  Cambridge undergraduate Part II material is excluded.

The comprehensive human-readable inventory is
`EXERCISE_SOURCE_INVENTORY.md`; its machine source is assembled from the
independently reviewable files under `source-inventory-fragments/`.  The cache
manifest `source-corpus.json` records the official URL, page count, local PDF
and layout-preserving text derivative, and SHA-256 hashes for every document.

## Cambridge Part III General Relativity

The collection represents every available General Relativity exam year in the
Cambridge Part III archive from 2001 through 2025. Cambridge states that the
archive has no 2020 examination papers.

- [Official Part III past-examination archive](https://www.maths.cam.ac.uk/postgrad/part-iii/node/91)

| Year | Official paper |
|---:|---|
| 2001 | [Paper 68](https://www.maths.cam.ac.uk/postgrad/part-iii/files/pastpapers/2001/Paper68.pdf) |
| 2002 | [Paper 72](https://www.maths.cam.ac.uk/postgrad/part-iii/files/pastpapers/2002/Paper72.pdf) |
| 2003 | [Paper 54](https://www.maths.cam.ac.uk/postgrad/part-iii/files/pastpapers/2003/Paper54.pdf) |
| 2004 | [Paper 55](https://www.maths.cam.ac.uk/postgrad/part-iii/files/pastpapers/2004/Paper55.pdf) |
| 2005 | [Paper 60](https://www.maths.cam.ac.uk/postgrad/part-iii/files/pastpapers/2005/Paper60.pdf) |
| 2006 | [Paper 61](https://www.maths.cam.ac.uk/postgrad/part-iii/files/pastpapers/2006/Paper61.pdf) |
| 2007 | [Paper 61](https://www.maths.cam.ac.uk/postgrad/part-iii/files/pastpapers/2007/Paper61.pdf) |
| 2008 | [Paper 63](https://www.maths.cam.ac.uk/postgrad/part-iii/files/pastpapers/2008/Paper63.pdf) |
| 2009 | [Paper 54](https://www.maths.cam.ac.uk/postgrad/part-iii/files/pastpapers/2009/Paper54.pdf) |
| 2010 | [Paper 52](https://www.maths.cam.ac.uk/postgrad/part-iii/files/pastpapers/2010/Paper52.pdf) |
| 2011 | [Paper 52](https://www.maths.cam.ac.uk/postgrad/part-iii/files/pastpapers/2011/Paper52.pdf) |
| 2012 | [Paper 56](https://www.maths.cam.ac.uk/postgrad/part-iii/files/pastpapers/2012/Paper56.pdf) |
| 2013 | [Paper 49](https://www.maths.cam.ac.uk/postgrad/part-iii/files/pastpapers/2013/Paper49.pdf) |
| 2014 | [Paper 50](https://www.maths.cam.ac.uk/postgrad/part-iii/files/pastpapers/2014/Paper50.pdf) |
| 2015 | [Paper 52](https://www.maths.cam.ac.uk/postgrad/part-iii/files/pastpapers/2015/Paper52.pdf) |
| 2016 | [Paper 309](https://www.maths.cam.ac.uk/postgrad/part-iii/files/pastpapers/2016/paper_309.pdf) |
| 2017 | [Paper 309](https://www.maths.cam.ac.uk/postgrad/part-iii/files/pastpapers/2017/paper_309.pdf) |
| 2018 | [Paper 309](https://www.maths.cam.ac.uk/postgrad/part-iii/files/pastpapers/2018/paper_309.pdf) |
| 2019 | [Paper 309](https://www.maths.cam.ac.uk/postgrad/part-iii/files/pastpapers/2019/paper_309.pdf) |
| 2021 | [Paper 309](https://www.maths.cam.ac.uk/postgrad/part-iii/files/pastpapers/2021/paper_309.pdf) |
| 2022 | [Paper 309](https://www.maths.cam.ac.uk/postgrad/part-iii/files/pastpapers/2022/paper_309.pdf) |
| 2023 | [Paper 309](https://www.maths.cam.ac.uk/postgrad/part-iii/files/pastpapers/2023/Paper_309.pdf) |
| 2024 | [Paper 309](https://www.maths.cam.ac.uk/postgrad/part-iii/files/pastpapers/2024/Paper_309.pdf) |
| 2025 | [Paper 309](https://www.maths.cam.ac.uk/postgrad/part-iii/files/pastpapers/2025/III_Paper_309.pdf) |

The current David Tong Part III course's four General Relativity example
sheets are also represented:

- [General Relativity course and Sheets 1--4](https://davidtong.org/teaching/general-relativity/)
- [Cambridge Part III Relativity and Gravitation courses](https://www.maths.cam.ac.uk/postgrad/part-iii/relativity-and-gravitation-courses)

Part III Cosmology, Field Theory in Cosmology, and Structure and Evolution of
Stars sources are used only where they directly support Weinberg's cosmology
or stellar-structure chapters.

## Other graduate courses

- [John McGreevy, Physics 225A, Problem Sets 1--9](https://mcgreevy.physics.ucsd.edu/f13/hw.html)
- [MIT 8.962 General Relativity problem sets](https://web.mit.edu/8.962/www/psets.html)
- [Rutgers Physics 617 General Relativity](https://www.physics.rutgers.edu/grad/617/)

The inspected corpus is deliberately broader than the final selection:
nonselected parents remain visible with `duplicate`, `too_dependent`,
`unsuitable_for_weinberg`, or `outside_scope` dispositions and a substantive
rationale.  `source_inventory.py --strict` requires complete document
coverage.  `audit_exercises.py --strict` then enforces 10--30 final exercises
per Chapter 2--16, none in Chapter 1, one complete parent per number,
one-for-one full solutions, exact printed credits/departures, and two current
content-hash-bound review passes.
