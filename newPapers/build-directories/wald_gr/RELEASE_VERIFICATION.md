# Wald GR release verification

Status: **verified for release** on 2026-08-07.

## Release artifact

- File: `../../wald-gr/wald-gr-modernized.pdf`
- SHA-256: `6c79b1dbdff2d60120ed6e518ddb78fb3908f30e8e481a0439d3a1869495b978`
- Extent: 483 A4 pages; 2,710,047 bytes
- Authoritative source: `../../../origPapers/wald_gr.pdf`
- Source SHA-256: `c0ca3f87d5dc8689ec89a2b9aef376a00670160b593e17dc533546f22b094599`
- Source extent: 505 physical PDF pages

## Release gates

- [x] Authoritative source checksum and page count verified by the build.
- [x] Every source leaf assigned and visually inspected; textual coverage is
      continuous across physical pages 8--12, 16--171, 174--433, and 436--504.
      Frontmatter, blank leaves, part/appendix dividers, and the publisher's
      advertisement on physical page 505 are explicitly accounted for in
      `SOURCE_MAP.md`.
- [x] All 95 planned transcription units are marked source-reviewed and
      compile-clean. Additional implementation subfiles are included within
      those units and carry the same reviewed status.
- [x] All 14 chapters, Appendices A--F, equations, statements, 72 figures,
      4 tables, problems, 336 references, and 434 source index entries are
      accounted for. Seventy-four figure/table objects have dedicated source
      files; Tables 7.1 and F.1 are inline with their surrounding text.
- [x] Binding notation audit has no definite regressions. Its nine review
      candidates were inspected and are genuine parameter/time derivatives,
      not obsolete dotted-boundary notation.
- [x] The 2026-08-07 notation revision replaced all 258 uses of `\vec`, uses
      `e_\mu` and `f^\mu` for tangent and cotangent bases, and uses `\vee` for
      algebraic duals. Pullback, Hodge, adjoint, and conjugation stars remain
      unchanged. The notation audit enforces the new rules.
- [x] The error review made 36 corrections in 19 classes. These include the
      sign in (7.2.50), the cross-reference in Section 7.4, and the displayed
      number (13.2.34). `CORRECTIONS.md` records each class and its basis.
      `audit_corrections.py` checks superseded forms, tag-label agreement,
      duplicate displayed numbers, and the reviewed mathematical repairs.
- [x] Full LaTeX build has no unresolved references or fatal warnings.
- [x] Layout audit records 0 overfull boxes and 5 benign underfull boxes.
- [x] Full PDF parses successfully with Poppler and Ghostscript.
- [x] Every font is embedded and subset.
- [x] All 483 output pages received visual review in ranges 1--160, 161--320,
      and 321--483. For the notation revision, all 83 affected pages were
      reviewed again. Eighty matched the reviewed candidate render
      byte-for-byte; the exact strict-release versions of pages 23, 35, and 36,
      which contain rebuilt TikZ diagrams, were inspected directly and are
      visually sound. The error pass changed 56 pages, all reviewed in raster
      contact sheets. Eighteen correction-bearing pages were also rendered at
      160 dpi, and their corrected text was checked through layout extraction.
      Pages 175, 180, 264, 366, and 406 received direct high-resolution inspection.
- [x] All 72 figures were compared directly with the authoritative source in
      chapter-grouped primary and independent second-pass audits. Forty-eight
      figure source files were repaired or redrawn. All 74 dedicated
      figure/table objects were recompiled into a canonical 74-page review PDF,
      and all 67 physical book pages containing figures were inspected in final
      placement. Nine top-edge clearance defects found in that placement pass
      were corrected and rechecked at high resolution.
- [x] Extracted layout-text SHA-256 for the final release is recorded:
      `12554ba20f8b6f7b8f17d80813e4a591e8a8cd0f27c5f28b3a401a7e3fc6813f`.
- [x] The sole blank output leaf is physical page 461, the intentional blank
      verso after Appendix F.
- [x] Final SHA-256 is recorded above.

The printed source's duplicated equation number `10.2.34` in Chapter 13 is
corrected to `13.2.34`. The correction audit verifies that every displayed
equation number is unique and agrees with its internal LaTeX label.
