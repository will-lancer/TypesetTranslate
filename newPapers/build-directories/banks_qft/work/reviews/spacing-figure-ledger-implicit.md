# Banks QFT implicit edition — spacing/figure defect ledger

Working ledger for the implicit-first layout pass (2026-09-02).
Status: **closed** after rebuild and targeted re-render.

## Summary

| Status | Count |
|--------|------:|
| Closed | 18 |
| Open   | 0 |

## Defects

| ID | Page(s) | Class | File | Issue | Fix | Status |
|----|---------|-------|------|-------|-----|--------|
| D-001 | 8–12 | exercise-chrome | `latex/banks.sty` | Stacked `\medskip\hrule` on consecutive hooks; orphan rules | Lighter 0.4pt rules, `\smallskip`, `\Needspace{7\baselineskip}`, `\nobreak` | closed |
| D-002 | ~56 | hook-float | `sec3_5.tex` | I-CH03-014 immediately before Fig. 3.1 | Moved hook after figure | closed |
| D-003 | ~56 | tikz-scale | `chapter03-fig-3-1.tex` | Slight left overflow | `x=0.97cm` scale | closed |
| D-004 | ~35–36 | hook-itemize | `sec3_3.tex` | I-CH03-009–012 inside `\itemize` | Moved hooks after each list | closed |
| D-005 | ~44 | hook-midpara | `sec3_7.tex` | I-CH03-015/016 split prose | Moved to sentence boundaries | closed |
| D-006 | ~52 | hook-inline | `sec4_3.tex` | I-CH04-002/003 before propagator | Moved after diagram + source note | closed |
| D-007 | ~52 | tikz-overflow | `chapter04-massive-photon-propagator.tex` | Propagator wider than `\textwidth` | `\resizebox{\linewidth}{!}` in center | closed |
| D-008 | ~69 | tikz-overflow | `chapter05-dirac-propagator.tex` | Dirac row overflow | `\resizebox{\linewidth}{!}` in center | closed |
| D-009 | ~94 | float-drift | `sec7_2.tex` | Figs. 7.1/7.2 mid-sentence | Floats after NGB paragraph; 10.5cm scale | closed |
| D-010 | ~119 | float-drift | `sec8_5.tex` | Fig. 8.3 between display and “where” | Figure before continuation prose | closed |
| D-011 | ~125 | hook-eof | `sec8_6.tex` | I-CH08-009 orphaned at EOF | Moved into closing paragraph | closed |
| D-012 | ~131 | pagebreak | `sec8_8.tex` | `\pagebreak[4]` near I-CH08-013 | Removed forced break | closed |
| D-013 | ~168 | hook-float | `sec9_6.tex` | I-CH09-009 vs footnote + Fig. 9.5 | Hook after Fig. 9.5 | closed |
| D-014 | ~192 | float-drift | `sec9_11.tex` | Fig. 9.9 between cue and eq. 9.3 | Figure before “Its value is” | closed |
| D-015 | ~193 | tikz-scale | `chapter09-fig910.tex` | Multi-panel coil figure overflow | `\resizebox{11cm}{!}` | closed |
| D-016 | ~247 | hook-midpara | `sec10_8.tex` | I-CH10-020 splits sentence | Moved after Dirac paragraph | closed |
| D-017 | ~510+ | tikz-overflow | `figures/appendixD.tex` | Wide propagator rows | `\resizebox{0.92\textwidth}{!}` on propagators | closed |
| D-018 | — | figproof-gap | `figproof.tex` | Appendix D macros not in harness | Added `appendixD-figproof.tex` | closed |

## Hotspot re-check (implicit, post-fix)

Pages from prior caption scan re-inspected at 150 DPI after rebuild:

| Page | Result |
|------|--------|
| 8, 10 | Exercise boxes tighter; no orphan rules |
| 56 | Fig. 3.1 fits; hook follows figure |
| 153–160 | Ch. 4 propagator inline diagram fits |
| 189 | Dirac propagator fits |
| 228–238 | Ch. 7 NGB figures follow prose |
| 309–358 | Ch. 9 floats and Fig. 9.10 scaled |
| 510 | Appendix D propagators fit column |

## Base edition spot-check

Shared figure/chapter edits verified on base draft build; no new holes at hook sites (hooks inert in base).
