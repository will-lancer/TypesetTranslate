# Independent audit: Chapter 3, printed pages 117--133

Scope: source PDF pages 129--145, covering Section 3-4, the continuation on
source page 138, Section 3-5, and the Chapter 3 bibliography.  The comparison
used the rendered source pages `pdf-129.jpg` through `pdf-145.jpg`, the source
page markers in the native files, and a second pass over every displayed
equation, proof continuation, footnote, citation, and bibliography entry.

Files reviewed:

- `latex/chapters/chapter03/sec3_4.tex`
- `latex/chapters/chapter03/sec3_5.tex`
- `latex/chapters/chapter03/bibliography.tex`

## Findings and patches

The reconstruction proof continues at the top of source page 138 after
equation (3-57).  The native transcription had stopped at the end of source
page 137.  The continuation now includes the well-definedness and unitarity
of (V), the three-line intertwining calculation, the identities
(Varphi(h)V^{-1}=arphi_1(h)) and
(U_1(a,Lambda)=VU(a,Lambda)V^{-1}), and the closing proof boundary.  The
following source-page-138 remark about denumerable fields, asymptotic
completeness, and the isolated (p^2=m^2) representation is present before
Section 3-5 begins.

Equation (3-46) now preserves the source condition
((x_j-x_{j+1})^2<0) for spacelike separation.  This was a transcription
direction error in the draft.

The source page 123 inner-product limit uses a lower-case chi.  The native
text retains `\chi` in both occurrences of
(\ket{\Psi_{g_n}}\to\ket{\chi}) and
(\braket{U(a,\Lambda)\Phi}{U(a,\Lambda)\chi}).

The Chapter 3 references are now inside a native `thebibliography` environment
with all seventeen entries in source order.  The source's introductory prose,
numbered references, publication data, accents, and cross-references remain
present.  Empty-label items carry the source's prose transitions inside the
native list environment.

## Coverage check

Every source page 129--145 has at least one `PCT-SOURCE` marker.  The source
page-138 continuation is marked independently from the Section 3-5 material.
The reconstruction proof environment closes at the end of the continuation;
Section 3-5 and the PCT proof each have balanced proof environments.  The
draft build reached the converted Chapter 3 bibliography successfully after
these edits.  The remaining draft build failure occurred in Chapter 4 and is
outside this audit scope.

Unresolved blockers: none
