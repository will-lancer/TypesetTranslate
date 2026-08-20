# Global object inventory audit for Chapters 1 and 2

## Scope and evidence

This audit covers physical PDF pages 016 through 107, printed pages 4 through
95, in `origPapers/pct_spin_statistics_all_that.pdf`. The source SHA-256 is
`44fadba731cafe7f009d4e561372febb3597e1f2a4819346ce2efd16befcb889`.

The native comparison surface is:

- `latex/chapters/chapter01/opening.tex`, `sec1_1.tex`, `sec1_2.tex`,
  `sec1_3.tex`, `sec1_4.tex`, and `bibliography.tex`;
- `latex/chapters/chapter02/opening.tex`, `sec2_1.tex`, `sec2_2.tex`,
  `sec2_3.tex`, `sec2_4.tex`, `sec2_5.tex`, `sec2_6.tex`, and
  `bibliography.tex`;
- `latex/figures/fig1_1.tex` through `fig1_3.tex` and `fig2_1.tex` through
  `fig2_7.tex`.

I read the source page images at original stored resolution. The page audits
`audit_ch1_early.md`, `audit_ch1_late.md`, `audit_ch2_early.md`,
`audit_ch2_mid.md`, and `audit_ch2_late.md` supplied the prose and boundary
records. This pass rebuilt the object sequence from the current TeX, checked
each source marker against its page, and checked the rendered packet after the
counter correction recorded below.

## Inventory totals

| Chapter | Printed equations | Numbered theorem slots | Named theorem headings | Lemma headings | Remark blocks | Figures | Footnotes | Bibliography entries |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 60 | 2 | 2 | 0 | 0 | 3 | 7 | 10 |
| 2 | 114 | 17 | 16 | 2 | 5 | 7 | 7 | 25 |

Chapter 1 has no printed Lemma, Corollary, Example, or Remark heading. Chapter
2 has no printed Corollary or Example heading. The source's prose use of
“corollary” after Theorem 2-13 and its prose examples remain in the checked
paragraph inventory.

Every printed equation identifier occurs once. Chapter 1 runs from `(1-1)` to
`(1-60)`. Chapter 2 runs from `(2-1)` to `(2-114)`. Each displayed body was
checked as a complete object, including aligned lines, bounds, signs,
delimiters, superscripts, punctuation, and the printed tag.

## Chapter 1 equation ledger

The table gives the source page, printed page, complete tag set on that page,
and the native file. It also records pages whose source text contains a
display without a printed tag in the result and boundary checks below.

| Source PDF / print | Printed equation tags | Native file |
|---:|---|---|
| 019 / 7 | `(1-1)`, `(1-2)` | `chapter01/sec1_2.tex` |
| 020 / 8 | `(1-3)` | `chapter01/sec1_2.tex` |
| 021 / 9 | `(1-4)` through `(1-6)` | `chapter01/sec1_3.tex` |
| 022 / 10 | `(1-7)` through `(1-9)` | `chapter01/sec1_3.tex` |
| 023 / 11 | `(1-10)` | `chapter01/sec1_3.tex` |
| 024 / 12 | `(1-11)` through `(1-17)` | `chapter01/sec1_3.tex` |
| 025 / 13 | `(1-18)` | `chapter01/sec1_3.tex` |
| 026 / 14 | `(1-19)` through `(1-23)` | `chapter01/sec1_3.tex` |
| 027 / 15 | `(1-24)` through `(1-26)` | `chapter01/sec1_3.tex` |
| 028 / 16 | `(1-27)` through `(1-29)` | `chapter01/sec1_3.tex` |
| 029 / 17 | `(1-30)` through `(1-36)` | `chapter01/sec1_3.tex` |
| 030 / 18 | `(1-37)` through `(1-43)` | `chapter01/sec1_3.tex` |
| 031 / 19 | `(1-44)` through `(1-46)` | `chapter01/sec1_3.tex` |
| 032 / 20 | `(1-47)` through `(1-50)` | `chapter01/sec1_3.tex` |
| 033 / 21 | `(1-51)` through `(1-53)` | `chapter01/sec1_3.tex` |
| 034 / 22 | `(1-54)` through `(1-56)` | `chapter01/sec1_4.tex` |
| 035 / 23 | `(1-57)` through `(1-59)` | `chapter01/sec1_4.tex` |
| 040 / 28 | `(1-60)` | `chapter01/sec1_4.tex` |

The resulting set has 60 entries, in numeric order, with 60 distinct tags.
The unnumbered linearity displays, parity-exchange display, center-of-mass
display, tensor-product displays, scattering display, and momentum-class
display were matched to their source pages and did not advance the equation
counter.

## Chapter 2 equation ledger

| Source PDF / print | Printed equation tags | Native file |
|---:|---|---|
| 043 / 31 | `(2-1)` | `chapter02/sec2_1.tex` |
| 044 / 32 | `(2-2)`, `(2-3)` | `chapter02/sec2_1.tex` |
| 045 / 33 | `(2-4)` through `(2-7)` | `chapter02/sec2_1.tex` |
| 046 / 34 | `(2-8)` through `(2-12)` | `chapter02/sec2_1.tex` |
| 047 / 35 | `(2-13)` | `chapter02/sec2_1.tex` |
| 049 / 37 | `(2-14)` through `(2-16)` | `chapter02/sec2_1.tex` |
| 050 / 38 | `(2-17)` | `chapter02/sec2_1.tex` |
| 051 / 39 | `(2-18)` through `(2-23)` | `chapter02/sec2_1.tex` |
| 052 / 40 | `(2-24)` through `(2-26)` | `chapter02/sec2_1.tex` |
| 053 / 41 | `(2-27)` through `(2-31)` | `chapter02/sec2_1.tex` |
| 054 / 42 | `(2-32)` | `chapter02/sec2_1.tex` |
| 055 / 43 | `(2-33)`, `(2-34)` | `chapter02/sec2_2.tex` |
| 056 / 44 | `(2-35)` through `(2-40)` | `chapter02/sec2_2.tex` |
| 057 / 45 | `(2-41)` through `(2-46)` | `chapter02/sec2_2.tex` |
| 058 / 46 | `(2-47)`, `(2-48)` | `chapter02/sec2_2.tex` |
| 059 / 47 | `(2-49)` through `(2-54)` | `chapter02/sec2_3.tex` |
| 060 / 48 | `(2-55)` through `(2-57)` | `chapter02/sec2_3.tex` |
| 061 / 49 | `(2-58)`, `(2-59)` | `chapter02/sec2_3.tex` |
| 062 / 50 | `(2-60)` | `chapter02/sec2_3.tex` |
| 064 / 52 | `(2-61)` through `(2-63)` | `chapter02/sec2_3.tex` |
| 065 / 53 | `(2-64)` | `chapter02/sec2_3.tex` |
| 066 / 54 | `(2-65)` through `(2-67)` | `chapter02/sec2_3.tex` |
| 067 / 55 | `(2-68)` through `(2-70)` | `chapter02/sec2_3.tex` |
| 068 / 56 | `(2-71)`, `(2-72)` | `chapter02/sec2_3.tex` |
| 069 / 57 | `(2-73)` through `(2-75)` | `chapter02/sec2_3.tex` |
| 070 / 58 | `(2-76)` | `chapter02/sec2_3.tex` |
| 071 / 59 | `(2-77)` | `chapter02/sec2_3.tex` |
| 072 / 60 | `(2-78)` | `chapter02/sec2_3.tex` |
| 073 / 61 | `(2-79)`, `(2-80)` | `chapter02/sec2_3.tex` |
| 074 / 62 | `(2-81)` through `(2-83)` | `chapter02/sec2_3.tex` |
| 075 / 63 | `(2-84)` | `chapter02/sec2_4.tex` |
| 076 / 64 | `(2-85)` | `chapter02/sec2_4.tex` |
| 077 / 65 | `(2-86)` | `chapter02/sec2_4.tex` |
| 079 / 67 | `(2-87)` through `(2-90)` | `chapter02/sec2_4.tex` |
| 082 / 70 | `(2-91)`, `(2-92)` | `chapter02/sec2_4.tex` |
| 085 / 73 | `(2-93)` | `chapter02/sec2_4.tex` |
| 086 / 74 | `(2-94)`, `(2-95)` | `chapter02/sec2_5.tex` |
| 088 / 76 | `(2-96)`, `(2-97)` | `chapter02/sec2_5.tex` |
| 089 / 77 | `(2-98)`, `(2-99)` | `chapter02/sec2_5.tex` |
| 090 / 78 | `(2-100)` through `(2-102)` | `chapter02/sec2_5.tex` |
| 091 / 79 | `(2-103)` | `chapter02/sec2_5.tex` |
| 092 / 80 | `(2-104)` through `(2-107)` | `chapter02/sec2_5.tex` |
| 094 / 82 | `(2-108)`, `(2-109)` | `chapter02/sec2_5.tex` |
| 095 / 83 | `(2-110)` | `chapter02/sec2_5.tex` |
| 096 / 84 | `(2-111)`, `(2-112)` | `chapter02/sec2_6.tex` |
| 103 / 91 | `(2-113)`, `(2-114)` | `chapter02/sec2_6.tex` |

The resulting set has 114 entries, in numeric order, with 114 distinct tags.
Unnumbered Cauchy, Fourier, cone, boundary-value, proof, and spectral-measure
displays were checked in source order. They retain `equation*` or bracketed
display treatment and leave the printed counter unchanged.

## Theorem, lemma, and remark inventory

The statement text, hypotheses, displayed conditions, proof start, proof end,
and source-page continuation were checked for every row. The native locators
give the complete statement span.

### Chapter 1

| Source | Object | Native statement |
|---:|---|---|
| PDF 019, print 7 | Theorem 1-1: a symmetry satisfying the commutative super-selection hypothesis is induced on an invariant coherent subspace by a unitary or anti-unitary operator, unique up to phase; a moved coherent subspace is mapped one-to-one with the same uniqueness | `sec1_2.tex:42-64` |
| PDF 040, print 28 | Theorem 1-2: every continuous unitary representation up to a phase factor of \(\mathcal P^{\uparrow}_{+}\) can be put into a continuous representation \(\{a,A\}\mapsto U(a,A)\) of the inhomogeneous \(SL(2,\mathbb C)\) | `sec1_4.tex:450-459` |

Theorem 1-1 is manually printed because its source statement precedes the
native theorem environment used for Theorem 1-2. The counter step added in
this pass gives `thm:ch1-symmetry` the native identifier `1-1`; the visible
heading remains exactly “Theorem 1-1”. Theorem 1-2 retains the explicit
`\setcounter{theorem}{1}` source control.

### Chapter 2

| Source | Object | Native statement |
|---:|---|---|
| PDF 055, print 43 | Theorem 2-1, Nuclear Theorem: a separately continuous multilinear functional on \(\mathcal S\) or \(\mathcal D\) has a unique distribution \(G\) in all variables with \(T(f_1,\ldots,f_k)=G(f_1\cdots f_k)\) | `sec2_1.tex:933-972` |
| PDF 056, print 44 | Lemma: \(\mathcal F\) and \(\overline{\mathcal F}\) are inverse continuous isomorphisms of \(\mathcal S\), with `(2-38)` | `sec2_2.tex:95-110` |
| PDF 058, print 46 | Theorem 2-2: the two transforms defined on \(\mathcal S'\) are inverse continuous linear bijections, with `(2-48)` | `sec2_2.tex:253-268` |
| PDF 059, print 47 | Theorem 2-3: the transform of a tempered distribution of fast decrease is infinitely differentiable and polynomially bounded | `sec2_3.tex:65-69` |
| PDF 063, print 51 | Theorem 2-4: continuity jointly in all variables plus separate holomorphy is equivalent to holomorphy on an open subset of \(\mathbb C^n\) | `sec2_3.tex:314-320` |
| PDF 065, print 53 | Theorem 2-5: the set of \(\eta\) for which \(e^{-p\cdot\eta}T\) is tempered is convex | `sec2_3.tex:486-490` |
| PDF 065-066, print 53-54 | Theorem 2-6: the Laplace transform is holomorphic on \(\mathbb R^n-i\Gamma\) with the polynomial bound `(2-65)`; the converse recovers a unique distribution | `sec2_3.tex:533-559` |
| PDF 071, print 59 | Theorem 2-7: support in a half-space forces \(\eta+ta\) into the Laplace domain for \(t\geq0\) | `sec2_3.tex:911-918` |
| PDF 072, print 60 | Theorem 2-8: forward-cone support gives the polynomial estimate `(2-78)` and the converse Laplace representation | `sec2_3.tex:978-1001` |
| PDF 073-074, print 61-62 | Theorem 2-9: the Laplace boundary value tends to the Fourier transform in \(\mathcal S'\), with the converse temperedness claim | `sec2_3.tex:1063-1081` |
| PDF 073-075, print 61-63 | Theorem 2-10: the tempered Laplace transform obeys `(2-80)` on compact cone subsets, with the converse | `sec2_3.tex:1114-1132` |
| PDF 077-078, print 65-66 | Lemma: a proper complex Lorentz transformation path from \(\mathbf 1\) to \(\Lambda\) remains in the tube; Theorem 2-11 gives the single-valued analytic continuation to \(\mathcal T'_n\) | `sec2_4.tex:159-169`, `182-226` |
| PDF 082-084, print 70-72 | The Jost theorem, called “Theorem 2-12” in the following prose, states that a real point lies in the extended tube exactly when every nonzero nonnegative combination of the \(\zeta_j\) is space-like, with `(2-92)` and its proof | `sec2_4.tex:587-704` |
| PDF 086-088, print 74-76 | Theorem 2-13: matching uniform continuous boundary values on an interval give a common holomorphic continuation | `sec2_5.tex:18-48`, `62-124` |
| PDF 088-092, print 76-80 | Theorem 2-14: matching limits from products of upper and lower half-planes extend to a neighborhood of the real environment | `sec2_5.tex:155-202`, `260-385` |
| PDF 092-093, print 80-81 | Theorem 2-15: the same edge-of-wedge conclusion holds for an open convex cone | `sec2_5.tex:391-436`, `438-457` |
| PDF 093-095, print 81-83 | Theorem 2-16: distributional boundary values in the cone give the Theorem 2-15 continuation | `sec2_5.tex:490-511`, `513-621` |
| PDF 095-096, print 83-84 | Theorem 2-17: a holomorphic function on \(\mathcal B=(\mathbb R^n+i\mathcal C)\cap\mathcal O\) with zero boundary value on \(E\) vanishes by the edge-of-wedge conclusion | `sec2_5.tex:627-647`, proof continuation in `sec2_6.tex:10-31` |

The Jost theorem has an explicit source result slot and a prose identifier,
with no bold theorem heading in the scan. The native `\stepcounter{theorem}`
at `sec2_4.tex:710` preserves the subsequent Theorem 2-13 through 2-17
sequence. The Fourier Lemma and the tube Lemma are unnumbered in the source.

The unnumbered Remark inventory is:

| Source | Native object |
|---:|---|
| PDF 063, print 51 | Remark after Theorem 2-4, `sec2_3.tex:322-329` |
| PDF 066, print 54 | Remarks 1 and 2 after Theorem 2-6, `sec2_3.tex:561-578` |
| PDF 086, print 74 | Remark after Theorem 2-13, `sec2_5.tex:50-56` |
| PDF 089, print 77 | Remarks 1 through 4 after Theorem 2-14, `sec2_5.tex:204-258` |

The native starred remark environments preserve the source's unnumbered
status. The source's prose “A corollary of this theorem” after Theorem 2-13
remains prose and does not enter the theorem counter.

## Footnote inventory

Each printed footnote was matched by marker, destination, content, and source
page. PDF 039 uses one printed footnote implemented as a mark and text pair.

| Chapter | Source page / print | Subject | Native locator |
|---|---:|---|---|
| 1 | 016 / 4 | pure versus mixed state | `opening.tex:50` |
| 1 | 017 / 5 | projection operator and observability | `sec1_1.tex:56` |
| 1 | 018 / 6 | complete commuting set and maximal Abelian terminology | `sec1_1.tex:98` |
| 1 | 027 / 15 | finite-dimensional \(SL(2,\mathbb C)\) representations | `sec1_3.tex:490` |
| 1 | 031 / 19 | componentwise spinor conjugation versus Dirac adjoint | `sec1_3.tex:834` |
| 1 | 034 / 22 | Dirac formalism and continuum normalization | `sec1_4.tex:38-53` |
| 1 | 039 / 27 | references for the general relativistic-invariance analysis | `sec1_4.tex:367-369` |
| 2 | 044 / 32 | `Supp T` and `sup T` notation | `sec2_1.tex:94` |
| 2 | 047 / 35 | compact sets and convergence in \(\mathcal D\) | `sec2_1.tex:318-323` |
| 2 | 060 / 48 | “analytic” as a term for holomorphic | `sec2_3.tex:137` |
| 2 | 079 / 67 | Halmos reference for the matrix lemma | `sec2_4.tex:260` |
| 2 | 083 / 71 | direct convex-separation argument | `sec2_4.tex:654-669` |
| 2 | 091 / 79 | continuity of the \(F_j\) in all variables | `sec2_5.tex:345-347` |
| 2 | 096 / 84 | real Hilbert spaces | `sec2_6.tex:38` |

## Figure inventory

The source has three Chapter 1 figures and seven Chapter 2 figures. The figure
file owns the physical-page marker. A section marker immediately before an
`\input` may identify the preceding prose page, as with Figure 1-3 on PDF 038
and Figure 2-1 on PDF 070; those leads were checked against the figure-file
markers and preserve the source boundary.

| Figure | Source PDF / print | Native file and labels | Caption or subject check |
|---|---:|---|---|
| Figure 1-1 | 023 / 11 | `fig1_1.tex`, `fig:ch1-lorentz-components` | Lorentz-group connectivity, four components, subgroup regions, and component labels |
| Figure 1-2 | 025 / 13 | `fig1_2.tex`, `fig:ch1-complex-lorentz-components` | Complex Lorentz connectivity, two components, solid and dashed paths |
| Figure 1-3 | 038 / 26 | `fig1_3.tex`, `fig:1-3` | Neutral scalar meson spectrum, one-particle shell, two-particle vertical hatch, three-particle cross hatch, and vacuum |
| Figure 2-1 | 070 / 58 | `fig2_1.tex`, `fig:2-1`, `fig:ch2-contour` | Contour \(C\), the \(z\)-axis, arrows, and points \(a,b\) |
| Figure 2-2 | 077 / 65 | `fig2_2.tex`, `fig:2-2` | Single-valuedness path through the extended tube and endpoint labels |
| Figure 2-3 | 084 / 72 | `fig2_3.tex`, `fig:2-3` | Space-like cone, planes \((\alpha),(\beta)\), and \(\zeta_1,\zeta_2,\zeta_3\) |
| Figure 2.4 | 085 / 73 | `fig2_4.tex`, `fig:2-4` | Source-visible decimal caption, primed and unprimed Jost vectors, and two cone configurations |
| Figure 2-5 | 086 / 74 | `fig2_5.tex`, `fig:2-5`, `fig:ch2-edge-wedge-domains` | Domains \(D_1,D_2\), real interval, and endpoints \(a,b\) |
| Figure 2-6 | 087 / 75 | `fig2_6.tex`, `fig:2-6`, `fig:ch2-edge-wedge-contours` | Contours \(C_1,C_2\), slit, endpoints, and arrow orientation |
| Figure 2-7 | 091 / 79 | `fig2_7.tex`, `fig:2-7`, `fig:ch2-mobius-map` | Mapped unit circles, \(z\)- and \(w\)-planes, marked points, and caption formula |

Figure 2.4 keeps the visible decimal `FIGURE 2.4`. Figure 2-7 has one
mapping formula in the section prose and one caption formula. The native
figure contains the caption formula once, while the section contains the
source display once.

## Bibliography inventory

Chapter 1 bibliography PDF 042 / print 30 contains entries `ref:1.1` through
`ref:1.10`. The two native `thebibliography` blocks are source-ordered as
entries 1 through 4 and 5 through 10; `\setcounter{NAT@ctr}{4}` preserves the
printed sequence.

Chapter 2 bibliography PDF 105 through 107 / print 93 through 95 contains
`pct-1` through `pct-25` in one native environment. Items 1 through 11 occupy
PDF 105, items 12 through 19 occupy PDF 106, and items 20 through 25 occupy
PDF 107. Names, accents, titles, journal data, book data, page data, years,
and the source prose between items were checked. The bibliographies add 0
equation, theorem, lemma, corollary, example, remark, figure, or footnote
objects.

## Boundary and counter audit

| Boundary | Source continuation checked | Native handling |
|---|---|---|
| PDF 020 to 021 | Section 1-2 closes in the middle of the space-inversion discussion | `sec1_2.tex` ends with the source fragment; `sec1_3.tex` begins the continuation and Section 1-3 |
| PDF 032 to 033 | General-spinor PCT material continues with `(1-51)` through `(1-53)` | `sec1_3.tex` carries all three tags and the index definitions |
| PDF 033 to 034 | Section 1-3 ends before Section 1-4 begins | `sec1_3.tex` closes before `sec1_4.tex` |
| PDF 041 to 042 | Restriction (3) continues into the Chapter 1 bibliography page | `sec1_4.tex` carries the continuation marker; bibliography starts once |
| PDF 042 to 043 | Chapter 1 bibliography ends before Chapter 2 opening | Separate bibliography and chapter-opening files |
| PDF 054 to 055 | Nuclear-theorem lead, statement, example, and evaluations continue | `sec2_1.tex` has the PDF 054 lead and PDF 055 theorem block; `refstepcounter{theorem}` prints 2-1 |
| PDF 055 to 056 | Fourier definitions begin before the Fourier Lemma and proof | `sec2_2.tex` retains `(2-33)` through `(2-40)` and an unnumbered Lemma |
| PDF 058 to 059 | Theorem 2-2 proof closes before the Laplace section and Theorem 2-3 | `sec2_2.tex` closes before `sec2_3.tex` |
| PDF 074 to 075 | Theorem 2-10 proof closes before Section 2-4 and `(2-84)` | `sec2_3.tex` and `sec2_4.tex` preserve the section boundary |
| PDF 077 to 078 | Tube Lemma text continues; Theorem 2-11 starts on the next page | `lemma*`, then Theorem 2-11 with its proof and Lemma proof |
| PDF 083 to 084 | Jost proof closes; the example and Figure 2-3 follow | `stepcounter{theorem}` occurs after the unheaded Theorem 2-12 proof |
| PDF 085 to 086 | Section 2-4 closes before the edge-of-wedge heading | `sec2_5.tex` begins Theorem 2-13 at 2-13 |
| PDF 095 to 096 | Theorem 2-17 proof continues before Section 2-6 | `sec2_6.tex` begins with that continuation, then `(2-111)` and `(2-112)` |
| PDF 104 to 105 | Section 2-6 closes before the 25-item bibliography | Separate section and bibliography files |

The native equation counters are explicit tags rather than automatic source
equation numbering. Result counters use the manual Theorem 1-1 step, the
Theorem 1-2 reset, the Theorem 2-1 step, and the Jost Theorem 2-12 step. The
auxiliary label scan after the fix reports `thm:ch1-symmetry` as `1-1`,
`thm:1-2` as `1-2`, `thm:ch2-nuclear` as `2-1`, `thm:ch2-fourier-distribution-inverse`
as `2-2`, `thm:ch2-11` as `2-11`, and the edge-of-wedge sequence as `2-13`
through `2-17`.

## Source-marker validation

The Chapter 1 file and figure marker scan contains 237 marker entries and all
27 source pages PDF 016 through PDF 042. The Chapter 2 scan contains 712
marker entries and all 65 source pages PDF 043 through PDF 107. Repeated
markers identify separate source units on the same page. The union has every
page in the assigned range, with page numbers matching the printed offset in
`SOURCE_MAP.md`.

## Corrections applied

This global pass applied one source-proven structural correction:

- `latex/chapters/chapter01/sec1_2.tex`: inserted `\refstepcounter{theorem}`
  immediately before the manually printed Theorem 1-1. The visible theorem
  text and source order remain unchanged. The auxiliary label now carries
  `1-1`, and the next printed result remains Theorem 1-2.

The current files also contain the source-proven corrections recorded in the
dedicated page audits, including the restored `(1-51)` through `(1-53)` block,
the Chapter 2 nuclear-theorem continuation, `(2-35)` multi-index notation,
the unnumbered result environments, the Jost counter slot, Figure 2.4's
decimal caption, and the single Figure 2-7 mapping display in each source
location.

## Build and rendered inspection

The temporary packet wrapper `/tmp/pct-ch1-ch2-inventory.tex` included all
Chapter 1 and Chapter 2 native files, all ten figures, and both bibliographies.
Two consecutive runs of

```text
pdflatex -interaction=nonstopmode -halt-on-error \
  -jobname=pct-ch1-ch2-inventory \
  -output-directory=/tmp/pct-ch1-ch2-build \
  /tmp/pct-ch1-ch2-inventory.tex
```

completed successfully. The final packet is an 82-page PDF. The final log has
zero undefined-reference, duplicate-destination, rerun, overfull, underfull,
or LaTeX error messages. The final auxiliary scan has all result and figure
labels listed above.

Rendered packet pages inspected after the correction include the Chapter 1
opening and Theorem 1-1 page, Lorentz and spectrum figures, the nuclear theorem
and Fourier boundary pages, Figures 2-1 through 2-7, Theorem 2-11 and the Jost
boundary, Theorems 2-13 through 2-17, the Section 2-6 continuation, and both
bibliography regions. The source figures and the native render agree in
caption, label, object order, and visible counter.

`python3 scripts/audit_notation.py --strict` reports the notation policy as
present and finds zero definite notation regressions. Its contextual raw-star
review candidates lie outside the assigned correction surface or are source
complex-conjugation uses already checked in the Chapter 1 and Chapter 2 pages.

STATUS: PASS

Unresolved blockers: none
