# Independent audit: Chapter 1 bibliography

## Packet and evidence

- Source: `origPapers/pct_spin_statistics_all_that.pdf`, physical PDF page 42,
  printed page 30.
- Native file: `latex/chapters/chapter01/bibliography.tex`.
- Source image: `work/source-pages/pdf-042.jpg`, inspected at original detail.
- The source PDF has no usable text layer for this page; the rendered image is
  the authority for wording, accents, punctuation, and printed numbering.

## Coverage

The page contains the `BIBLIOGRAPHY` heading, the opening paragraph, references
1--4, the intervening paragraph, references 5--10, and the closing paragraph.
Every unit has a physical-page provenance marker. References 1--4 and 5--10
are represented in native `thebibliography` environments, with the second
environment continuing the printed sequence at 5.

## Item-by-item comparison

| Printed item | Source data checked | Native result |
| ---: | --- | --- |
| 1 | E. P. Wigner; German title; Friedr. Vieweg Braunschweig, 1931; English translation title; Academic, New York, 1959; explanatory sentence about the rotation group | Present with the same authors, titles, publication data, and sentence. |
| 2 | E. P. Wigner; `Über die Operation der Zeitumkehr in der Quantenmechanik`; `Gött. Nach.`; 546--559 (1931); anti-unitary sentence | Present with TeX accents and the same journal, pages, year, and sentence. |
| 3 | E. P. Wigner; `Unitary Representations of the Inhomogeneous Lorentz Group`; `Ann. Math.`; 40, 149 (1939) | Present with the same title and publication data. |
| 4 | G. C. Wick, E. P. Wigner, A. S. Wightman; `Intrinsic Parity of Elementary Particles`; `Phys. Rev.`; 88, 101 (1952); superselection sentence | Present with the same authors, title, publication data, and sentence. |
| 5 | A. S. Wightman; French title; pp. 6--11 in the CNRS volume; 1959 | Present with the same title, page range, book title, institution, and year. |
| 6 | A. Barut and A. S. Wightman; `Relativistic Invariance and Quantum Mechanics`; `Nuovo Cimento Suppl.`; 14, 81--94 (1959) | Present with the same authors, title, journal, volume, pages, and year. |
| 7 | A. S. Wightman; `L'Invariance dans la mécanique quantique relativiste`; pp. 161--226 in *Dispersion Relations and Elementary Particles*; Wiley, New York, 1960 | Present with the same title, pages, book data, and year. |
| 8 | S. Schweber; *An Introduction to Relativistic Quantum Field Theory*, Part One; Harper and Row, New York, 1961 | Present with the same title, part, publisher, place, and year. |
| 9 | B. L. van der Waerden; *Die gruppentheoretische Methode in der Quantenmechanik*; Springer, Berlin, 1932 | Present with the same title and publication data. |
| 10 | G. Ya. Liubarskii; *The Application of Group Theory in Physics*; translated by S. Dedijer; Pergamon, New York, 1960 | Present with the same title, translator, publisher, place, and year. |

The opening and closing prose matches the scan, including “Wignerism,” the
sentence introducing the application to relativistic quantum mechanics, and
the reference to exercises in Ref. 7.

## House-style changes

The source's numbered enumerations are native `thebibliography` environments.
The JHEP bibliography treatment supplies bracketed labels and bold journal
volumes. Diacritics are written with TeX accent commands. These changes affect
typesetting only; the bibliographic content remains source-faithful.

## Local audit result

All ten entries, both prose transitions, the heading, and the closing note were
compared against the source image. No author, title, page range, publication
field, year, punctuation-bearing phrase, or printed item number remains
unresolved.

Unresolved blockers: none
