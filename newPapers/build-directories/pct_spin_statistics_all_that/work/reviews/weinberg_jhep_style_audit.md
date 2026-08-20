# Weinberg/JHEP style audit

Audit date: 2026-08-20

Scope: report-only review of the native PCT edition against the local Weinberg
Volume I edition. The checks cover the master shell, `pct.sty`, `NOTATION.md`,
`notation-map.jsonl`, headings, result environments, equations, Dirac states,
metric and Fourier phases, figure captions, bibliography treatment, Appendix
hierarchy, table of contents, page numbering, layout warnings, and the index.
This pass leaves manuscript and style files unchanged.

The audited edition is
`newPapers/build-directories/pct_spin_statistics_all_that`. The reference
edition is `newPapers/build-directories/weinberg_vol1`.

The final candidate artifact is `latex/master.pdf`, an A4 PDF with 180 pages.
Its SHA-256 is
`4741fe42fc72801e9b3bee2249eafcd0c013b52935f78827f646c3b1b6d05735`.
The report uses this artifact and the current log; it does not run a
compilation.

## Evidence surface

- Current shell: `latex/master.tex`, `latex/jheppub.sty`, and `latex/pct.sty`.
- Current policy and ledger: `NOTATION.md` and `notation-map.jsonl`.
- Reference shell: `weinberg_vol1/latex/master.tex` and
  `weinberg_vol1/latex/jheppub.sty`.
- Reference notation guide: `weinberg_vol1/latex/frontmatter/notation.tex`.
- Reference chapter style: `weinberg_vol1/latex/chapters/chapter02/sec21-23.tex`,
  `sec24-25.tex`, and `latex/figures/chapter06/fig61.tex`.
- Reference bibliography layout: `weinberg_vol1/latex/chapters/chapter01/backmatter.tex`.
- Existing focused checks: `work/reviews/audit_frontmatter.md`,
  `audit_appendix_constructive.md`, and `audit_appendix_local_algebras.md`.
- Current corpus inventory: 50 LaTeX files, 49 source-marked transcription
  packets, and 70 notation-map records.

Status terms have narrow meanings. `Pass` identifies a current source and
render check. `Authorized` identifies a source-specific PCT choice within the
requested reading edition. `Open` identifies a remaining audit or metadata
condition.

## Audit matrix

| Surface | Current locators | Weinberg reference locators | Finding | Status |
| --- | --- | --- | --- | --- |
| JHEP document shell | `latex/master.tex:1-50,65-75` | `weinberg_vol1/latex/master.tex:1-46,85-87` | The article shell, 11pt A4 geometry, blue links, compressed spacing, fresh section pages, and `\flushbottom` follow the local Weinberg edition. | Pass |
| JHEP package behavior | `latex/jheppub.sty:38-48,266-275` | `weinberg_vol1/latex/jheppub.sty:38-49,267-276` | The reading edition keeps the JHEP link treatment and suppresses the submission banner and missing-email warning. The white page field suits the historical book edition. | Authorized |
| Title metadata and publisher placement | `latex/master.tex:65-71`; `latex/frontmatter/copyright.tex:1-76` | `weinberg_vol1/latex/master.tex:75-83` | Title, authors, affiliations, and the publisher imprint are carried by the JHEP title fields. The copyright leaf preserves the source CIP and edition data. The imprint occurs once in the title treatment, with the separate source title line retained on the copyright leaf. | Authorized |
| Headings and subsection numbering | `latex/pct.sty:79-106`; `latex/chapters/chapter02/sec2_1.tex:2`; `sec2_5.tex:11` | `weinberg_vol1/latex/chapters/chapter02/sec21-23.tex:11,105`; `sec24-25.tex:5` | `\thesubsection` now produces source-style hyphenated labels such as `2-1`. The rendered contents page and body headings use that form. | Pass and source-authorized |
| TOC and page sequence | `latex/master.tex:44-46`; `latex/jheppub.sty:216-217,287-297` | `weinberg_vol1/latex/master.tex:31-46,85-87` | The TOC uses roman page numbering, the Arabic body sequence resumes after the TOC, and the added `\clearpage` places the source copyright leaf after the TOC. The rendered contents page shows `1-1`, `2-1`, `3-1`, and `4-1`. | Pass |
| Equations and result numbers | `latex/pct.sty:79-106`; sampled displays in `chapter03/sec3_2.tex:102-123` and `sec3_3.tex:245-269` | `weinberg_vol1/latex/chapters/chapter02/sec24-25.tex:12-17` | PCT equation and theorem labels retain the printed hyphen form, including `(2-1)` and `Theorem 4-1`. Weinberg's dotted tags such as `2.4.1` supply the shell comparison. | Authorized source choice |
| Theorem and proof styling | `latex/pct.sty:85-173`; `chapter02/sec2_1.tex:933-940`; `sec2_5.tex:18-48` | `weinberg_vol1/latex/master.tex:1-13`; `sec24-25.tex:12-17` | The result parser accepts source identifiers, source titles, and proof headings while retaining the JHEP article spacing. | Authorized |
| Dirac states | `latex/pct.sty:16-37`; `NOTATION.md:171-236,269-304`; `chapter03/sec3_3.tex:853-864` | `weinberg_vol1/latex/master.tex:48-60`; `frontmatter/notation.tex:45-55` | Kets, bras, inner products, matrix elements, vacuum states, and in/out labels follow the Weinberg guide. The current corpus has zero active calls to Weinberg's short `\sl` alias; `\slashedvector` remains the local helper. | Pass |
| Metric and spinors | `latex/pct.sty:39-71`; `NOTATION.md:91-143,407-442` | `weinberg_vol1/latex/frontmatter/notation.tex:9-43` | Mostly-plus `\eta`, `p^2=-m^2`, `\beta=i\gamma^0`, `\bar u=u^\dagger\beta`, bold spatial vectors, script letters, and star/transpose/dagger distinctions follow the guide. | Pass |
| Fourier and Laplace phases | `NOTATION.md:306-376`; `chapter03/sec3_2.tex:102-123`; `chapter03/sec3_3.tex:245-259,768-783` | `weinberg_vol1/latex/chapters/chapter02/sec24-25.tex:233-240,315-316` | Current displays use the source conversion recorded in the policy. The Laplace proof uses the current positive house phase, and the formula-level ledger records the current source locators. | Pass |
| Notation ledger synchronization | `notation-map.jsonl:1-70`; `scripts/audit_notation.py --strict` | `weinberg_vol1/latex/frontmatter/notation.tex:14-55` | The refreshed map has 70 records, with statuses `reviewed`, `reviewed-current-corpus`, or `resolved`. Every current raw-star candidate has an exact reviewed classification, and the strict audit reports no definite notation regressions. | Pass |
| Figures and captions | `latex/figures/fig2_1.tex:9-35`, `fig2_2.tex:8-53`, `fig2_3.tex:6-49`, `fig2_4.tex:6-48`, `fig2_5.tex:6-30`, `fig2_6.tex:6-47`, `fig2_7.tex:6-33` | `weinberg_vol1/latex/figures/chapter06/fig61.tex:1-10` | Native TikZ geometry is placed in figure environments with source captions and labels. The rendered captions use the source numbering, including the recorded source-specific `FIGURE 2.4`. | Pass and authorized |
| Bibliography | `latex/chapters/chapter01/bibliography.tex:1-68`; `chapter02/bibliography.tex:3-45`; `appendix/bibliography.tex:3-16` | `weinberg_vol1/latex/chapters/chapter01/backmatter.tex:6-8,88-90` | PCT's interleaved printed bibliography is represented with numbered `thebibliography` blocks and source labels. Weinberg's split Bibliography and References layout supplies the comparison pattern. | Authorized source choice |
| Appendix hierarchy | `latex/master.tex:121-125`; `latex/appendix/constructive.tex:1-31`; `local-algebras.tex:1-32`; `bibliography.tex:1-6` | `weinberg_vol1/latex/master.tex:61-72`; `frontmatter/notation.tex:1-7` | The source-faithful Appendix heading is unlettered in print. Its two unlettered subsection titles and Bibliography entry appear under one Appendix TOC node. Internal equation and hyperlink namespaces retain Appendix A. | Pass and source-authorized |
| Index | `latex/master.tex:47,127-128`; `latex/backmatter/index.tex:1-30` | Reference package layer and the source bibliography/backmatter pattern | The current index is native LaTeX, two-column, and source ordered. Main entries are bold, subentries are indented, and the rendered index occupies pages 178-180. | Pass and authorized |
| Layout warnings | `latex/master.log` | `weinberg_vol1/latex/master.log` and rendered artifact conventions | The current log scan has zero `Overfull`, `Underfull`, undefined-reference, multiply-defined-label, rerun, or `PackageWarning` records. The lone `rerunfilecheck` match is package metadata. | Pass |

## Detailed checks

### Shell, title treatment, and source rationale

The shell at `latex/master.tex:1-14` uses the same article class and core
mathematics stack as `weinberg_vol1/latex/master.tex:1-13`. The local additions
keep the JHEP links, compact title spacing, chapter page breaks, and PCT helper
macros. `jheppub.sty` supplies the title, TOC, footer, and page geometry layer.

The title block at `master.tex:65-71` uses JHEP author and affiliation commands.
The publisher imprint is carried in `\dedicated` at line 70. The source
copyright file retains the separate title line and CIP material printed on that
leaf. The focused frontmatter review records this as the accepted
source-preserving placement. This is a shell adaptation with the source
publisher information intact.

The local package differences remain deliberate reading-edition choices. The
current JHEP package omits the blue page-field option and replaces the missing
email warning with a historical-edition comment. The rendered PDF has a white
page field, blue links, and zero email-warning records.

### Headings, TOC, equations, and results

`pct.sty:79-84` defines the PCT number surface directly:

```tex
\renewcommand{\thesubsection}{\thesection-\arabic{subsection}}
\numberwithin{equation}{section}
\renewcommand{\theequation}{\thesection-\arabic{equation}}
```

Theorem-family counters at `pct.sty:86-106` use the same chapter-result form.
The current contents page contains `1-1`, `2-1`, `3-1`, and `4-1`, and the
body contains source-style equation and theorem labels. The Weinberg edition
uses dotted subsection and equation tags in the inspected Chapter 2 files. The
PCT source contract governs the visible hyphenated labels; the Weinberg
contribution is the surrounding JHEP shell and notation treatment.

The `\pretocmd{\section}{\clearpage}` hook at `master.tex:45` keeps printed
chapters on fresh pages. The TOC depth is two at line 46, which exposes the
source subsection and chapter bibliography entries.

The parser at `pct.sty:120-173` accepts source identifiers such as `4-14`,
keeps optional source titles, and preserves the amsthm spacing surface. This
supports source result labels within the JHEP article structure.

### Front matter, roman TOC, and Appendix hierarchy

The JHEP hook at `jheppub.sty:216-217` switches the TOC page sequence to roman
numerals. The `\maketitle` flow at `jheppub.sty:287-297` emits the TOC and
restores Arabic numbering after it. `master.tex:44` adds a clear page after the
TOC rule. The final candidate PDF extraction shows the title leaf, roman
markers `-i-`, `-ii-`, and `-iii-`, the three-page Contents sequence, and the
source copyright leaf before the Arabic Preface page 1.

The Appendix input order at `master.tex:121-125` follows the source. The first
packet advances the internal section counter, sets the equation hyperlink
namespace to `A.` and prints `\section*{APPENDIX}` at
`appendix/constructive.tex:1-9`. Its subsection title is unlettered at lines
28-31. `appendix/local-algebras.tex:1,29-32` continues with the second
unlettered subsection. `appendix/bibliography.tex:3-6` adds the source
Bibliography entry. The rendered Contents page shows one Appendix node followed
by the two source headings and Bibliography. The body keeps the printed
unlettered hierarchy while Appendix equations retain A.1 and A.2 anchors.

This separation follows the source surface. It also keeps internal references
stable for the native transcription.

### Dirac notation, metric, and phases

The state macros at `pct.sty:16-37` implement the forms documented by the
Weinberg notation guide at `frontmatter/notation.tex:45-55`. The local policy
at `NOTATION.md:171-236,269-304` converts Hilbert-space products to explicit
bra-ket or matrix-element notation, keeps in/out qualifiers outside the state
delimiters, and uses `\ket{\Omega}` for the vacuum. The tuple
`(\psi_p,\psi_n)` remains a field-operator set in the context recorded at
`notation-map.jsonl:23`.

The metric contract at `NOTATION.md:91-143` is visible in current Chapter 3
formulas. The spectral support records at `notation-map.jsonl:16-19` point to
the current `sec3_3.tex` and `sec3_4.tex` lines and carry the expected
mostly-plus forms `P^2\leq-M^2`, `\delta(p^2+m^2)`, and `p^2=-m^2`.

The phase records at `notation-map.jsonl:12-15` are current-corpus entries.
Equations (3-15), (3-16), (3-29), and (3-30) use the declared converted
phases. The Laplace proof at `sec3_3.tex:768-783` uses the positive house phase
required by `NOTATION.md:367-372`. Weinberg's translation and one-particle
phases at `sec24-25.tex:233-240,315-316` provide the comparison convention.

The formula checks pass. The current frozen-corpus `audit_notation.py --strict`
run emits 22 raw-star candidates and assigns an exact reviewed classification
to every candidate. The classifications preserve the local meanings, including
entrywise matrix conjugation, componentwise conjugation, test-function
conjugation, and the C*-algebra involution. The strict run ends with `No
definite notation regressions found.`

### Figures, bibliography, and index

The seven Chapter 2 figure files use native TikZ geometry and source insertion
points. Their captions and labels are checked in the figure review. The
Weinberg figure at `figures/chapter06/fig61.tex:1-10` supplies the native TikZ
comparison. Current captions preserve the source uppercase form and numbering.

PCT chapter bibliography files use local numbered lists because the source
interleaves bibliography blocks with the chapter text. Weinberg's
`chapter01/backmatter.tex:6-8,88-90` separates a square-bullet Bibliography from
an enumerated References list. The PCT arrangement preserves the source reading
order and reference labels.

The index packet at `backmatter/index.tex:1-30` owns the native `theindex`
content. The JHEP package supplies the two-column page surface. The final
candidate render preserves the source ordering and page range on pages 178-180.

## Automated and rendered checks

The following read-only checks were run against the current checkout or current
artifact.

1. `python3 scripts/audit_project.py` reported 36/36 native chunks, 36 assembly
   inputs, 438 native labels, and a passed project audit.
2. `python3 scripts/audit_notation.py --strict` found the binding policy, scanned
   49 transcription files, emitted 22 contextual star candidates, classified
   every candidate through the refreshed map, and ended with `No definite
   notation regressions found.`
3. `sha256sum latex/master.pdf` reports
   `4741fe42fc72801e9b3bee2249eafcd0c013b52935f78827f646c3b1b6d05735`, and
   `pdfinfo latex/master.pdf` reports 180 A4 pages. `pdftotext -layout` shows
   hyphenated subsection labels, roman TOC numbering, the source Appendix
   hierarchy, source-style figure captions, and the two-column index.
4. The current `latex/master.log` scan has zero `Overfull`, `Underfull`,
   undefined-reference, multiply-defined-label, rerun, or `PackageWarning`
   records. Its only `rerunfilecheck` match is package metadata at line 655.

## Audit closure

The title placement, hyphenated subsection numbering, refreshed formula-level
notation records, source-preserving bibliography placement, layout warning
scan, roman TOC/page break, and unlettered Appendix hierarchy are closed by
the current source and artifact evidence. The frozen-corpus strict notation
audit passes with current `audit_candidate` locators and reviewed classifications.

Unresolved blockers: none
