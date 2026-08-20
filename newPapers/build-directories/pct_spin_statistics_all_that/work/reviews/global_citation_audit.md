# Global citation and bibliography audit

## Scope

This report covers the citation callouts in Chapters 1 through 4 and the
Appendix, together with the chapter bibliographies and the Appendix
bibliography. Source pages were compared as rendered images against the
current TeX. The source bibliography ranges are PDF page 42 for Chapter 1,
PDF pages 105--107 for Chapter 2, PDF pages 144--145 for Chapter 3, PDF pages
187--190 for Chapter 4, and PDF pages 211--216 for the Appendix.

The comparison included names, titles, initials, journal and book data,
volumes, years, page ranges, punctuation, visible numbering, lettered item
19a, and bibliography continuations. Bracketed theorem labels and equation
labels were excluded from the citation list. The Appendix bibliography's
internal visible callout `[47, 48]` in item 68 was checked as source content.

## Resolved implementation finding

Source PDF 42, printed page 30, presents Chapter 1 bibliography entries 1
through 10 as one continuous numbered list. The source-preserving TeX keeps
the two bibliography blocks at
`latex/chapters/chapter01/bibliography.tex:9-32` and
`latex/chapters/chapter01/bibliography.tex:38-68`.

The exact repair at line 41 was:

```diff
-\setcounter{enumiv}{4}
+\setcounter{NAT@ctr}{4}
```

The project loads natbib through `jheppub.sty`. Natbib's bibliography list
uses `NAT@ctr`, so the second block now renders entries 5 through 10 with the
source labels. Two forced `latexmk -g -pdf -interaction=nonstopmode
-halt-on-error master.tex` builds completed with exit status 0. The final
`master.aux:91-100` records refs 1.1 through 1.10 as labels 1 through 10.
Rendered PDF pages 31 and 32 show labels `[1]` through `[10]`, matching PDF
42. The bibliography TOC entry remains linked to page 26 through
`master.aux:89-90`, and the corresponding `section*.149` bookmark remains in
`master.out`.

## Bibliography comparison

| Section | Source range | TeX bibliography | Result |
|---|---|---|---|
| Chapter 1 | PDF 42, printed 30 | `chapters/chapter01/bibliography.tex` | Entries 1--10 and visible numbering match after the `NAT@ctr` repair. |
| Chapter 2 | PDF 105--107, printed 93--95 | `chapters/chapter02/bibliography.tex` | Entries 1--25 match in full. |
| Chapter 3 | PDF 144--145, printed 132--133 | `chapters/chapter03/bibliography.tex` | Entries 1--17 match in full. |
| Chapter 4 | PDF 187--190, printed 175--178 | `chapters/chapter04/bibliography.tex` | Entries 1--29 and lettered item 19a match in full. |
| Appendix | PDF 211--216, printed 199--204 | `appendix/bibliography.tex` | Entries 1--91 match in full. Items 21 and 76 continue across pages as in the source. |

The Appendix comparison includes the visible source oddity `221--136` in
item 66. It was retained because it is printed source content. Item 68's
internal `[47, 48]` agrees with the source. The Appendix uses explicit
optional labels `[1]` through `[91]`.

## Chapter 1 callouts

| Source page | TeX locator | Source callout | Finding |
|---|---|---|---|
| PDF 19, printed 7 | `chapters/chapter01/sec1_2.tex:39` | Ref. 1 | Matches. |
| PDF 23, printed 11 | `chapters/chapter01/sec1_3.tex:165` | Ref. 7 | Matches. |
| PDF 27, printed 15 | `chapters/chapter01/sec1_3.tex:493` | Refs. 9 and 10; Ref. 7 | Matches. |
| PDF 39, printed 27 | `chapters/chapter01/sec1_4.tex:369` | Refs. 5, 6, and 7 | Matches. |

Proposed correction for these callouts: none.

## Chapter 2 callouts

| Source page | TeX locator | Source callout | Finding |
|---|---|---|---|
| PDF 48, printed 36 | `chapters/chapter02/sec2_1.tex:371` | Refs. 1, 2, and 3 | Matches. |
| PDF 48, printed 36 | `chapters/chapter02/sec2_1.tex:383` | Ref. 24, p. 373 | Matches. |
| PDF 49, printed 37 | `chapters/chapter02/sec2_1.tex:415` | Ref. 1, p. 74 | Matches. |
| PDF 52, printed 40 | `chapters/chapter02/sec2_1.tex:694` | Ref. 1, Chapter 5 | Matches. |
| PDF 52, printed 40 | `chapters/chapter02/sec2_1.tex:742` | Ref. 1, Chapter 4 | Matches. |
| PDF 54, printed 42 | `chapters/chapter02/sec2_1.tex:858` | Ref. 1, Vol. II, p. 102 | Matches. |
| PDF 55, printed 43 | `chapters/chapter02/sec2_1.tex:929` | Ref. 5 | Matches. |
| PDF 97, printed 85 | `chapters/chapter02/sec2_6.tex:116` | Ref. 20 | Matches. |
| PDF 100, printed 88 | `chapters/chapter02/sec2_6.tex:333` | Ref. 20 | Matches. |
| PDF 101, printed 89 | `chapters/chapter02/sec2_6.tex:389` | Ref. 21 | Matches. |
| PDF 102, printed 90 | `chapters/chapter02/sec2_6.tex:404` | Ref. 20 | Matches. |
| PDF 103, printed 91 | `chapters/chapter02/sec2_6.tex:448` | Ref. 23 | Matches. |
| PDF 103, printed 91 | `chapters/chapter02/sec2_6.tex:516` | Ref. 22 | Matches. |
| PDF 104, printed 92 | `chapters/chapter02/sec2_6.tex:520` | Ref. 22 | Matches. |

Proposed correction for these callouts: none.

## Chapter 3 callouts

| Source page | TeX locator | Source callout | Finding |
|---|---|---|---|
| PDF 110, printed 98 | `chapters/chapter03/sec3_1.tex:121` | Ref. 20 of the Bibliography of Chapter 2 | Matches. |
| PDF 110, printed 98 | `chapters/chapter03/sec3_1.tex:133` | Refs. 5 and 15 | Matches. |
| PDF 113, printed 101 | `chapters/chapter03/sec3_1.tex:315` | Ref. 5 | Matches. |
| PDF 113, printed 101 | `chapters/chapter03/sec3_1.tex:334` | Ref. 25 of Chapter II, pp. 301--303 | Matches. |
| PDF 117, printed 105 | `chapters/chapter03/sec3_2.tex:192` | Ref. 4 | Matches. |
| PDF 117, printed 105 | `chapters/chapter03/sec3_2.tex:201` | Ref. 15 | Matches. |
| PDF 117, printed 105 | `chapters/chapter03/sec3_2.tex:226` | Ref. 3 | Matches. |
| PDF 123, printed 111 | `chapters/chapter03/sec3_3.tex:503` | Refs. 5, 7, 9, 10, and 11 | Matches. |
| PDF 128, printed 116 | `chapters/chapter03/sec3_3.tex:964` | Ref. 12 | Matches. |

Proposed correction for these callouts: none.

## Chapter 4 callouts

| Source page | TeX locator | Source callout | Finding |
|---|---|---|---|
| PDF 148, printed 136 | `chapters/chapter04/sec4_1.tex:158` | Ref. 1 | Matches. |
| PDF 151, printed 139 | `chapters/chapter04/sec4_2.tex:114` | Ref. 4 | Matches. |
| PDF 154, printed 142 | `chapters/chapter04/sec4_3.tex:39` | Ref. 3 of Chapter 3 | Matches. |
| PDF 158, printed 146 | `chapters/chapter04/sec4_4.tex:72` | Ref. 28 | Matches. |
| PDF 173, printed 161 | `chapters/chapter04/sec4_5.tex:35` | Ref. 6 | Matches. |
| PDF 181, printed 169 | `chapters/chapter04/sec4_6.tex:58` | Ref. 27 | Matches. |

Proposed correction for these callouts: none.

## Appendix callouts

| Source page | TeX locator | Source callouts | Finding |
|---|---|---|---|
| PDF 191, printed 179 | `appendix/constructive.tex:10-11` | [1], [2] | Matches. |
| PDF 192, printed 180 | `appendix/constructive.tex:42,45,47-48,76` | [3], [4], [5], [6], [7], [8, 9] | Matches. |
| PDF 193, printed 181 | `appendix/constructive.tex:107,142,179` | [10], [11], [12] | Matches. |
| PDF 194, printed 182 | `appendix/constructive.tex:255-256` | [13], [14] | Matches. |
| PDF 195, printed 183 | `appendix/constructive.tex:270,282,318,326,328,331,334,337-338` | [15--19], [15], [16, 17, 19], [20], [21], [22], [15--22], [23, 18, 24] | Matches. |
| PDF 197, printed 185 | `appendix/constructive.tex:434,446,450,470-471` | [67], [25, 26], [18, 27], [28, 29], [30--32] | Matches. |
| PDF 198, printed 186 | `appendix/constructive.tex:508,526,535` | [33], [34], [35] | Matches. |
| PDF 199, printed 187 | `appendix/constructive.tex:570,591,595` | [36], [37, 38], [39] | Matches. |
| PDF 200, printed 188 | `appendix/constructive.tex:614,622,635,645,647` | [40, 41], [42], [43, 44], [45], [37, 38, 44] | Matches. |
| PDF 201, printed 189 | `appendix/constructive.tex:652,676,683,690,695,697` | [46, 47], [45], [48, 49], [50], [51], [52--54] | Matches. |
| PDF 202, printed 190 | `appendix/constructive.tex:715,717,719,751,755-756` | [55], [25, 26], [57], [57], [58, 59], [60] | Matches. |
| PDF 203, printed 191 | `appendix/local-algebras.tex:6,21,34,39,43` | [61, 62, 60], [63, 64], [65], [66], [67] | Matches. |
| PDF 204, printed 192 | `appendix/local-algebras.tex:135` | [68] | Matches. |
| PDF 205, printed 193 | `appendix/local-algebras.tex:196,202-203,209,212` | [65], [69--71], [72], [73] | Matches. |
| PDF 206, printed 194 | `appendix/local-algebras.tex:229,295,297,300` | [72], [74], [74, 75], [77] | Matches. |
| PDF 207, printed 195 | `appendix/local-algebras.tex:353-354,392` | [78--82], [72], [78--81] | Matches. |
| PDF 208, printed 196 | `appendix/local-algebras.tex:414,421` | [83--85], [86] | Matches. |
| PDF 209, printed 197 | `appendix/local-algebras.tex:479,524` | [87], [79] | Matches. |

Proposed correction for the Appendix callouts: none.

## Audit status

All source citation callouts, bibliography content, visible bibliography
labels, and the bibliography link destination in the audited range match the
source scans after the counter repair.

Unresolved blockers: none
