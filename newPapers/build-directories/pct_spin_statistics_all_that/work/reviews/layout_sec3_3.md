# Section 3-3 layout review

Scope: `latex/chapters/chapter03/sec3_3.tex` only. The edits preserve the
source markers, equation tags, and mathematical statements. They add display
line breaks, paragraph break opportunities inside long inline products, and
the required unnumbered display structure for the long norm identity.

## Baseline warning evidence

The isolated section wrapper compiled before the layout pass with `RC=0`, but
reported these 16 overfull boxes in
`/tmp/pdfs/pct-sec3-3/layout-before.log`:

```text
Overfull \hbox (61.71793pt too wide) detected at line 127
Overfull \hbox (0.64839pt too wide) detected at line 147
Overfull \hbox (37.53693pt too wide) in paragraph at lines 159--163
Overfull \hbox (10.85497pt too wide) in paragraph at lines 159--163
Overfull \hbox (32.58655pt too wide) in paragraph at lines 207--209
Overfull \hbox (10.58919pt too wide) detected at line 347
Overfull \hbox (0.2764pt too wide) detected at line 420
Overfull \hbox (25.28337pt too wide) detected at line 466
Overfull \hbox (7.03094pt too wide) detected at line 505
Overfull \hbox (61.43887pt too wide) detected at line 527
Overfull \hbox (31.2489pt too wide) detected at line 560
Overfull \hbox (95.29465pt too wide) detected at line 596
Overfull \hbox (9.95164pt too wide) detected at line 685
Overfull \hbox (17.07674pt too wide) detected at line 746
Overfull \hbox (0.74924pt too wide) detected at line 782
Overfull \hbox (11.24432pt too wide) detected at line 920
```

The first full-manuscript draft build also exposed two paragraph boxes that
the isolated article wrapper did not reproduce:

```text
Overfull \hbox (55.66617pt too wide) in paragraph at lines 383--385
Overfull \hbox (36.75566pt too wide) in paragraph at lines 531--541
```

Those boxes came from unbreakable inline products in the hermiticity prose and
the cluster-decomposition proof. `\allowbreak` was added between the factors.

## Layout changes

- The norm identity was moved into a centered `gathered` display. Its inner
  products, integration factors, and measures now occupy short rows.
- Long theorem headings and the spectral-conditions heading are separated from
  their following prose paragraphs.
- Displays (3-36), (3-37), (3-39), and (3-41), the spectral-support integral,
  the cluster proof identities, the metric estimate, the absolute-value
  estimate, the Laplace transform, and the complex-Lorentz continuation use
  internal line breaks.
- The two long inline products noted above have explicit legal break points.
- The final partition prose after (3-41) has legal breaks between adjacent
  pair factors, preventing a full-build paragraph box.
- The section opening uses `\enlargethispage{4\baselineskip}` as a local page
  adjustment so the manuscript page reaches its flush-bottom target.

## Verification

The isolated wrapper was compiled twice after the edits:

```text
pdflatex -interaction=nonstopmode -halt-on-error ... main.tex
RC=0
```

The second final log, `/tmp/pdfs/pct-sec3-3/layout-final-3-2.log`, contains no
`Overfull`, `Underfull`, `Fatal`, `Undefined`, `Missing`, or unresolved-label
diagnostics. The rendered standalone pages
`final3-page-02.jpg` through `final3-page-12.jpg` were inspected. They contain
no clipped display material, and all affected equation tags remain visible.

The full manuscript was rebuilt in the historical packet with:

```text
./build_and_verify.sh --draft
```

It completed with `RC=0` and produced a historical `latex/master.pdf` with
185 pages. The final `latex/master.log` contains no `Underfull` or `Overfull`
diagnostics.
The local `\enlargethispage{4\baselineskip}` adjustment at the start of the
section removes the prior page-97 warning while preserving the source text,
mathematics, equation tags, and source markers. The additional `\allowbreak`
opportunities in the prose following (3-41) remove the final full-build
paragraph box.

The final full-PDF renders for pages 96--109 were inspected, including page 97
and its neighbors 96 and 98. These pages cover the section-opening break and
the complete section in the manuscript build; the changed displays fit the
text block, and the final incomplete source sentence remains at the end of the
section.

`python3 scripts/audit_source.py` passes with all 36 native chunks present and
211 distinct marked PDF pages.

## Current final-candidate evidence

The current `latex/master.pdf` is an A4, 180-page PDF with SHA-256
`4741fe42fc72801e9b3bee2249eafcd0c013b52935f78827f646c3b1b6d05735`. The
rendered and inspection manifests each contain 180 records, and render
validation passed for 180/180 pages.

Unresolved blockers: none
