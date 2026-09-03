# Source map

The canonical PDF has 281 physical pages. Printed page 1 is physical PDF page
11. Throughout the numbered body, `printed = pdf - 10`.

| Material | Physical PDF pages | Printed pages | Disposition |
| --- | ---: | ---: | --- |
| Front cover | 1 | unnumbered | Omit cover |
| Intentional blank | 2 | unnumbered | Omit blank |
| Publisher description | 3 | unnumbered | Omit publisher-only page |
| Blank verso | 4 | unnumbered | Omit blank |
| Title page | 5 | unnumbered | Native title treatment |
| Copyright and imprint | 6 | unnumbered | Omit publisher-only page |
| Contents | 7-9 | v-vii | Regenerate from native structure |
| Blank leaf | 10 | unnumbered | Omit blank |
| Chapter 1 | 11-17 | 1-7 | Transcribe |
| Chapter 2 | 18-26 | 8-16 | Transcribe |
| Chapter 3 | 27-47 | 17-37 | Transcribe |
| Chapter 4 | 48-53 | 38-43 | Transcribe |
| Chapter 5 | 54-71 | 44-61 | Transcribe |
| Chapter 6 | 72-85 | 62-75 | Transcribe |
| Chapter 7 | 86-102 | 76-92 | Transcribe |
| Chapter 8 | 103-146 | 93-136 | Transcribe |
| Chapter 9 | 147-215 | 137-205 | Transcribe |
| Chapter 10 | 216-251 | 206-241 | Transcribe |
| Chapter 11 | 252-254 | 242-244 | Transcribe |
| Appendices A-F | 255-271 | 245-261 | Transcribe |
| References | 272-277 | 262-267 | Transcribe |
| Author index | 278 | 268 | Transcribe |
| Subject index | 279-281 | 269-271 | Transcribe |

Each substantive source unit begins with a marker of this form:

```tex
% BANKS-SOURCE: pdf=18 print=8 kind=prose
```

Displays add `id=<source equation number>`. Figures add `id=<source figure
number>`. A unit crossing a physical-page boundary receives another marker.

The section boundaries follow the printed Contents. Where a heading starts
partway down a page, the marker chooses the heading as the content boundary.
Reviewers inspect the whole boundary page.

