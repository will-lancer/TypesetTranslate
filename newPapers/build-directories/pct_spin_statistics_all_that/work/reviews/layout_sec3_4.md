# Layout review: Chapter 3, Section 3-4

PASS: focused overfull-box cleanup

INPUT SNAPSHOT: `latex/chapters/chapter03/sec3_4.tex`, SHA-256 `4d67b807977afb841fafb7d3980bc55e1a5c42e469d7ded125b016915b7e3ef1`, inspected 2026-08-20; controlling source pages are PDF129-138, print pages 117-126.

FULL SCOPE READ: The complete 829-line section source was read. The source-to-section boundary from `sec3_3.tex` was checked. The rebuilt section occupies rendered PDF pages 109-117, with printed page labels 105-113 in the native build. Each of those nine rendered pages was inspected at 150 dpi.

FINDINGS:

- The initial master log reported a 53.23882pt overfull paragraph at lines 923--2. The paragraph began in `sec3_3.tex` and ended at the Section 3-4 heading.
- The initial master log reported a 13.70242pt overfull display at `sec3_4.tex` line 95, equation (3-47).
- The initial master log reported a 100.80429pt overfull display at `sec3_4.tex` line 205, equation (3-49).
- The initial master log reported a 148.90929pt overfull display at `sec3_4.tex` line 630, the cluster-decomposition inner-product display.

EDITS MADE:

- Scoped `\emergencystretch` to the Section 3-4 heading boundary. The preceding paragraph now breaks within the available measure while its prose remains unchanged.
- Put equation (3-47) into an `aligned` display with explicit rows for the integral measure, conjugated test function, and remaining product.
- Put equation (3-49) into an `aligned` display with one row for the group action and one row for its component action.
- Split the two long rows in the cluster-decomposition display into aligned rows that fit the text measure. Equation tags, mathematical symbols, prose, and all `PCT-SOURCE` markers remain present.

CHECKS RUN:

- Historical packet build: `latexmk -g -pdf -interaction=nonstopmode -halt-on-error master.tex` from `latex/` exited with status 0. That packet's `latex/master.pdf` contained 185 pages and had SHA-256 `44ac9dd804e8e70682cb61bf46945c2d9110936e7803f1051a9249411ec57201`.
- The final `master.log` segment from `sec3_4.tex` through `sec3_5.tex` contains zero `Overfull \\hbox` and zero `Overfull \\vbox` records. The boundary warning and the three section warnings listed above are absent.
- The final segment contains one `Underfull \\vbox (badness 2205)` output-balancing diagnostic. It produces no overfull box, and the rendered page inspection shows complete text, intact equations, and no clipping. The diagnostic is retained as a vertical balancing notice outside this focused overfull-box certification.
- Rendered pages 109-117 were inspected after the final build. The Section 3-4 heading, equations (3-47), (3-49), and the cluster display fit inside the text measure. The proof continuation at the section file boundary remains continuous through page 113.

UNRESOLVED: none within the declared overfull-box scope.

STATUS: PASS

CURRENT FINAL-CANDIDATE EVIDENCE:

The current `latex/master.pdf` is an A4, 180-page PDF with SHA-256
`4741fe42fc72801e9b3bee2249eafcd0c013b52935f78827f646c3b1b6d05735`. The
rendered manifest and page-inspection manifest each contain 180 records; the
visual records are 180/180, and render validation passed for all pages.

Unresolved blockers: none
