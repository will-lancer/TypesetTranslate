# Wald GR correction record

This record covers reviewed corrections to the printed source and to the
edition's transcription. Each source correction also carries a nearby
`% SOURCE ERRATUM:` comment in the LaTeX. The one transcription correction is
marked `% TRANSCRIPTION CORRECTION:`.

The pass made 36 individual changes in 19 classes. Eighteen of those changes
standardize the source's variant spelling `Leibnitz` to `Leibniz`.

| Location | Printed or transcribed form | Corrected form | Basis |
|---|---|---|---|
| 2.1 | `is they were` | `if they were` | Grammar |
| 2.2, 2 problems, 3.1--3.3, 13.2, C.2 | `Leibnitz` | `Leibniz` | Standard spelling |
| 3.2 | `trace tree part` | `trace-free part` | Tensor decomposition |
| 4.2 | `spacial` | `spatial` | Spelling |
| 6.2 | `nonstatic` | `nonstationary` | Verified against the source PDF |
| 7.2 | `satisying` | `satisfying` | Spelling |
| (7.2.50) | plus sign on the second line | minus sign | Follows from the preceding line and yields (7.2.51) |
| 7.4 | reference to (7.2.12) | reference to (7.4.12) | Local transformation number |
| Chapter 8 introduction | `artifical` | `artificial` | Spelling |
| 9.5 | `past direct timelike` | `past directed timelike` | Grammar and standard terminology |
| Chapter 10 introduction | `contraints` | `constraints` | Spelling |
| Chapter 10, problem 1(c) | `Schwartz inequality` | `Cauchy--Schwarz inequality` | Name of the inequality |
| (13.2.34) | displayed as (10.2.34) | displayed as (13.2.34) | Chapter and section sequence |
| 14.3 | `Boltzman's constant` | `Boltzmann's constant` | Name spelling |
| 14.3 | `await to complete theory` | `await a complete theory` | Grammar |
| E.1 | `wih respect` | `with respect` | Spelling |
| Eisenhart reference | `Univerity Press` | `University Press` | Publisher name |
| Weinberg reference | `Centennary Survey` | `Centenary Survey` | Book title |
| Index | `Gauss-Codacci` | `Gauss--Codazzi` | Name spelling and consistency with 10.2 |

`audit_corrections.py` rejects every superseded form in active TeX. It also
checks tag-label agreement, duplicate displayed equation numbers, the sign in
(7.2.50), and the corrected 7.4 cross-references.
