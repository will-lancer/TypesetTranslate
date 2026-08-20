# Low-recall warning-page audit

## Scope and input snapshot

This review covers every page below the 0.70 warning threshold in the source
report that was supplied for this pass:

`005, 021, 031, 032, 056, 074, 080, 091, 109, 119, 120, 121, 124, 131, 134, 136`.

The canonical source is `origPapers/pct_spin_statistics_all_that.pdf`, SHA-256
`44fadba731cafe7f009d4e561372febb3597e1f2a4819346ce2efd16befcb889`, with 221
pages. I inspected the full JPEG for every listed page in
`work/source-pages/`. I read each native marker segment and the adjacent
source markers in the ordered `master.tex` assembly. The initial report had 16
warning pages. The page-021 repair below leaves 15 active warnings in the
refreshed report; page 021 remains in this review as a resolved item from the
initial set.

## PASS 1: source images and page boundaries

The source images were inspected at high detail. Running headers, folios, page
rules, equation glyphs, figure lines, captions, footnote symbols, and body
prose were included in the visual comparison. The source extraction methods in
the report were checked against the visible pages. Pages 021, 031, 032, 056,
074, 080, 091, 109, 120, 121, 124, 131, 134, and 136 use the Tesseract fallback;
page 005 uses the sparse title extraction path; page 119 uses Tesseract in the
current report. The JPEG remains authoritative for mathematical glyphs.

## PASS 2: native segments and adjacent markers

The following record gives the direct recall from the refreshed report. The
boundary-aware value includes the neighboring native page markers. A `real
omission` value of `false` means that the source content is represented in the
native assembly or in the authorized title treatment. Page 021 records the
single source correction.

| PDF page | Printed page | Direct / boundary recall | Native and boundary evidence | Cause disposition | Real omission |
| --- | --- | --- | --- | --- | --- |
| 005 | unpaginated | 0.000 / 0.700 | The source title leaf is represented by `master.tex:65-74`; the layout marker is in `frontmatter/copyright.tex:7`. | Title material in master. | false |
| 021 | 9 | 0.826 / 0.861 | `chapter01/sec1_2.tex` ends the page-20 sentence at “observables of”. The added `p9-boundary` marker in `chapter01/sec1_3.tex` supplies the page-21 continuation before section 1-3. | Real omission, repaired. | true in the initial report |
| 031 | 19 | 0.689 / 0.720 | `chapter01/sec1_3.tex` markers cover the spinor transformation, equations 1-44 through 1-46, gamma matrices, PCT rules, and the footnote. | Notation conversion with OCR corruption in mathematical tokens. | false |
| 032 | 20 | 0.529 / 0.721 | The page-31 marker carries the preceding two-component sentence tail. PDF-032 markers cover equations 1-47 through 1-50 and the adjoining prose. | Page reflow, notation conversion, OCR corruption. | false |
| 056 | 44 | 0.628 / 0.767 | The page-55 prose marker carries the sentence ending in “with a few integrations by parts”. PDF-056 markers cover equations 2-35 through 2-40 and the Fourier proof. | Page reflow and notation conversion. | false |
| 074 | 62 | 0.675 / 0.701 | The page-73 theorem marker owns the opening through equation 2-80. PDF-074 markers cover its continuation, proof, and equations 2-81 through 2-83. | Page reflow, notation conversion, OCR corruption. | false |
| 080 | 68 | 0.608 / 0.657 | The page-79 marker carries the cone criterion through the source boundary. PDF-080 markers cover the light-cone argument and the four eta-component calculations. | Page reflow, notation conversion, OCR corruption. | false |
| 091 | 79 | 0.561 / 0.735 | PDF-091 markers cover the mapped-circle display, `fig2_7.tex`, its caption, the dagger note, and equation 2-103. | Notation conversion and OCR corruption in figure and display material. | false |
| 109 | 97 | 0.417 / 0.962 | The page-108 opening marker owns the first field paragraph through the source boundary. PDF-109 begins at “The assumptions we make fall into four groups” and carries axiom O through the vacuum statement. | Page reflow, notation conversion, OCR corruption. | false |
| 119 | 107 | 0.685 / 0.718 | The page-118 proof marker owns the test-function setup through the source boundary. PDF-119 markers cover equations 3-24 and 3-48 through 3-51 with the reconstruction prose. | Page reflow and notation conversion. | false |
| 120 | 108 | 0.643 / 0.683 | PDF-120 markers cover the proof of Theorem 3-1, Theorem 3-2, equations 3-27 through 3-33, and the spectral and hermiticity text. | Notation conversion and OCR corruption. | false |
| 121 | 109 | 0.610 / 0.655 | PDF-121 markers cover equation 3-34, its local-commutativity condition, the proof, spectral support, and the hermiticity continuation. | Notation conversion and OCR corruption. | false |
| 124 | 112 | 0.691 / 0.731 | PDF-124 markers cover the polynomial bound, the R0 estimate, local commutativity, and the polar-coordinate integral. | Notation conversion and OCR corruption. | false |
| 131 | 119 | 0.654 / 0.764 | The page-130 proof marker owns the “test functions f_k=0” boundary sentence. PDF-131 markers cover vector addition, the scalar product, U(a,Lambda), the vacuum vector, and phi(h). | Page reflow and notation conversion. | false |
| 134 | 122 | 0.646 / 0.874 | The page-133 inner-product marker owns the setup ending with the equivalence-class construction. PDF-134 markers cover the Cauchy classes, diagonal choice, limit, and Hilbert-space summary. | Page reflow and notation conversion. | false |
| 136 | 124 | 0.545 / 0.627 | The page-135 invariant-vector marker owns the opening sequence phrase. PDF-136 markers cover the vacuum-uniqueness proof and cluster-decomposition displays. | Page reflow and notation conversion. | false |

The source images and native segments show a complete content path for every
row. The low direct values track display-heavy pages, source-page sentence
boundaries, and OCR damage to symbols. Page 021 was the sole source omission.

## PASS 3: source-proven repair

I added the following native text before the page-21 section heading in
`latex/chapters/chapter01/sec1_3.tex`:

```text
The system. In the remaining sections of this chapter it will be assumed that
some such specification has been made for relativity transformations. In
Chapter 3 the specification will be made explicit in terms of fields.
```

The block carries `% PCT-SOURCE: pdf=021 print=9 kind=prose id=p9-boundary`.
The wording follows the scan. The adjacent page-20 marker retains the source
sentence prefix, so the paragraph occurs once in the ordered assembly. No
other source correction was warranted by the 16-page comparison.

## PASS 4: linkage and verification

The machine disposition file is
`work/reviews/transcription_low_recall_dispositions.json`. It records all 16
initial warning pages, source-image paths, native and adjacent marker paths,
cause categories, evidence, and the page-021 repair. Its active warning set
matches the refreshed report:

`005, 031, 032, 056, 074, 080, 091, 109, 119, 120, 121, 124, 131, 134, 136`.

The refreshed warning signature is
`772a210bd44c50f0bd430bd5aff9f66e6218eba27a410a21988ab2c79de22316`.

`scripts/audit_transcription.py` now checks, in strict mode, the disposition
schema, report path, review path, source SHA-256, warning threshold, active
warning set, page status, category, evidence, and warning signature. It also
requires this review to contain the resolved-blocker line. The report stores
the check under `low_recall_dispositions` and stores any failed checks under
`findings.low_recall_disposition_issues`.

Checks run for this pass:

- `python3 -m py_compile scripts/audit_transcription.py` passed.
- The refreshed audit found 211/211 included markers, zero severe gaps, and 15 active warning pages after the page-021 repair.
- The strict audit was run after the disposition JSON and this review were installed. Its result and linkage fields were inspected in `work/reviews/transcription_audit.json`.
- Historical packet build: `latexmk -g -pdf -interaction=nonstopmode -halt-on-error master.tex` completed with exit code 0 after the source repair; that rebuilt manuscript was 186 pages.
- Rendered pages 12 and 13 were inspected. The repaired paragraph is legible at the bottom of page 12, and section 1-3 begins cleanly on page 13.

Current final-candidate evidence:

The current `latex/master.pdf` is an A4, 180-page PDF with SHA-256
`4741fe42fc72801e9b3bee2249eafcd0c013b52935f78827f646c3b1b6d05735`. The
current rendered manifest and page-inspection manifest each contain 180
records, and render validation passed for 180/180 visually inspected pages.

Unresolved blockers: none
