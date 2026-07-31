# Weinberg QFT supplementary-source priority

## Selection rule

Each substantive chapter contains 10--30 complete parent problems. Preserve a
problem's connected subparts under one number. The upper limit is not a quota:
retain fewer problems when that produces a stronger, less fragmented set.

The unordered first-choice pool is:

- John McGreevy's graduate QFT homework and examinations;
- Daniel Harlow's QFT I--III problem sections;
- official Cambridge Part III examinations and example sheets for QFT,
  Advanced QFT, Applications of QFT, the Standard Model, gauge theory,
  solitons, and supersymmetry; and
- Kevin Zhou's QFT notes and course problem sets.

There is no ranking within this pool. Select the strongest complete,
chapter-appropriate problem available among the four, then draw from other
strong author-posted books, notes, examinations, and graduate homework.

Quality and chapter fit remain decisive. Membership in the first-choice pool
is never a reason to include a weaker problem or to misclassify a source.

## Verified source hubs

- McGreevy course index:
  <https://mcgreevy.physics.ucsd.edu/>
- McGreevy Physics 215A, Fall 2023 homework:
  <https://mcgreevy.physics.ucsd.edu/f23/hw.html>
- McGreevy Physics 215C, Spring 2025 homework:
  <https://mcgreevy.physics.ucsd.edu/s25/hw.html>
- Harlow QFT I:
  <https://www.mit.edu/~harlow/HarlowQFT1.pdf>
- Harlow QFT II:
  <https://www.mit.edu/~harlow/HarlowQFT2.pdf>
- Harlow QFT III:
  <https://www.mit.edu/~harlow/HarlowQFT3.pdf>
- Cambridge Part III examination archive:
  <https://www.maths.cam.ac.uk/postgrad/part-iii/node/91>
- Cambridge Part III example-sheet index:
  <https://www.damtp.cam.ac.uk/user/examples/indexP3.html>
- Kevin Zhou:
  <https://knzhou.github.io/>

Cambridge's examination archive states that its papers are copyrighted and
may not be reproduced without permission. Public availability alone is not a
reuse license. Cambridge problems therefore use `adapted` or
`original-inspired` mode unless a concrete permission record is present.
Apply the same rule to other sources lacking an explicit reuse grant.

## Exact-parent ledger discipline

Every supplementary exercise has one unique source-ledger record. Required
fields beyond the bibliographic metadata are:

```json
{
  "source_family": "cambridge-part-iii",
  "document_id": "cambridge-part-iii-aqft-2019-exam",
  "parent_problem": "Question 3, parts (a)--(d)",
  "use_mode": "adapted"
}
```

Allowed source families are `mcgreevy`, `harlow`, `cambridge-part-iii`,
`knzhou`, and `other`. Allowed use modes are `adapted`,
`original-inspired`, and `verbatim-permitted`. The last requires a
`reproduction_basis` identifying workspace-supplied text or an explicit reuse
license or permission.

One ledger parent ID may appear in exactly one exercise. If two old items came
from connected parts of the same parent, merge them and their solutions.

An exact problem number may be recorded as `adapted` only after direct
comparison with the primary source confirms that the edition retains the
parent's complete connected conceptual and subpart arc. Topic overlap or a
shared final formula is insufficient. If the local problem has a genuinely
different architecture, either restore the whole parent or use
`original-inspired` with an accurate broad locator. This source-fidelity
review is a manual release gate in addition to the automated uniqueness
checks.
