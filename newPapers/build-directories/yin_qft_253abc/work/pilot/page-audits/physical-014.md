# Physical page 014 audit

## Source and inspection record

- Combined source: `/Users/wlancer/Desktop/IAS/phy/qft/qft_253abc_book.pdf`
- Combined physical page: 14
- Original note page: Physics 253a, page 9
- SHA-256 checked: `9e5e4d241fffffa56c1c3df6dce4b83178f75787dd5d794a18c5d0c087769f21`
- Visual inspection: Poppler render at 500 dpi, 4250 by 5560 pixels
- Context checked: physical pages 13 and 15
- Ink: black on white. The rendered page is exactly grayscale, with zero RGB-channel spread.
- Overall transcription confidence: 0.99

## Exact TeX-ready transcription

The source abbreviations, capitalization, singular nouns, spaces around hyphens, quotation marks, and punctuation remain unchanged.

```tex
% YIN-SOURCE: notes=253a:9; pdf=14; class=NOTES_EXACT
\begin{itemize}
  \item Can also verify that
  \[
    U(\Lambda,a)\,\hat{\phi}(x)\,
    \bigl(U(\Lambda,a)\bigr)^{-1}
    = \hat{\phi}(\Lambda x+a).
  \]
\end{itemize}

% Graphical divider in the source: a long horizontal line ending in a
% right-pointing arrowhead, followed by two small apostrophe-like ink marks.
% The final {}'' is a shape-preserving placeholder, not assigned prose meaning.
\noindent\makebox[\linewidth][l]{%
  \rule[0.5ex]{0.90\linewidth}{0.4pt}%
  \(\mkern-5mu>\mkern4mu{}''\)%
}

\medskip
\noindent Postulate that the properties
\begin{itemize}
  \item Hilbert space \(\mathcal{H}\)
  \item Poincar\'e sym \(U(\Lambda,a)\)
  \item Poincar\'e - invt vacuum \(\lvert\Omega\rangle\)
  \item local ``field'' operators \(\hat{\phi}(x)\)\\
        that obey Poincar\'e - covariance and\\
        microcausality.
\end{itemize}

\noindent hold for system of interacting\\
relativistic particles as well!

\begin{itemize}
  \item[-] How to construct such theories ?
  \item[-] useful to work with a formalism in\\
           which Poincar\'e sym is manifest.
\end{itemize}
```

## Page geometry and marks

- The opening dot bullet continues the preceding free-field discussion. Its displayed equation occupies the upper third of the page.
- A hand-drawn horizontal divider begins near the left margin and ends near the right margin in a right-pointing arrowhead.
- Two small black ink marks sit immediately to the right of that arrowhead. Their shapes resemble a pair of apostrophe strokes. They carry no clear textual meaning.
- The postulate heading has no colon or terminal punctuation.
- Four round bullets introduce the postulates. The two closing transitions use dash bullets.
- No page number, header, footer, diagram, or colored annotation appears on this page.

## Uncertainties and retained readings

| Location | Retained reading | Competing reading or issue | Decision | Confidence |
|---|---|---|---|---:|
| Divider, far right | two apostrophe-like ink marks after the arrowhead | stray pen taps; an unidentified punctuation mark | Preserve both graphically and leave them semantically unassigned. | 0.70 shape, 0.20 meaning |
| Third postulate | `Poincar\'e - invt vacuum` | `invt` expands to `invariant` | Retain the abbreviation in the exact transcript. Any textbook expansion must be logged as a cleaning operation. | 0.99 |
| Fourth postulate | `Poincar\'e - covariance` | conventional typography would use `Poincar\'e covariance` or `Poincar\'e-covariance` | Retain the visible spaces around the handwritten hyphen. | 0.98 |
| Scope sentence | `hold for system of interacting` | grammar might invite `a system` or plural `systems` | Retain the source's singular `system` and omitted article. | 0.99 |
| Closing question | `theories ?` | conventional typesetting removes the space before `?` | Retain the source spacing in this diplomatic transcript. | 0.99 |
| Closing transition | `Poincar\'e sym` | `sym` expands to `symmetry` | Retain the abbreviation here. | 0.99 |

## Likely textbook and provenance units

Every unit below has `notes=253a:9`, `pdf=14`, and source class `NOTES_EXACT` unless the chapter editor combines it with lecture speech.

| Stable unit | Source content | Likely chapter use | Confidence |
|---|---|---|---:|
| `253a-09-p014-u01` | `Can also verify that` | Short lead-in to the covariance check; attach it to the displayed equation or keep it as its own sentence record. | 0.99 |
| `253a-09-p014-u02` | \(U(\Lambda,a)\hat\phi(x)(U(\Lambda,a))^{-1}=\hat\phi(\Lambda x+a)\) | Displayed Poincar\'e-covariance equation. Preserve the hats, group parameters, inverse placement, transformed argument, and final period. | 1.00 |
| `253a-09-p014-g01` | ruled arrow divider plus two terminal marks | Page-layout artifact. Record a disposition even if the textbook replaces it with a section break. | 0.95 divider, 0.70 terminal marks |
| `253a-09-p014-u03` | `Postulate that the properties` | Opening line of a postulate or axiom block. Its grammatical continuation runs through unit `u08`. | 0.99 |
| `253a-09-p014-u04` | Hilbert space \(\mathcal H\) | First postulate-list item. | 1.00 |
| `253a-09-p014-u05` | Poincar\'e symmetry \(U(\Lambda,a)\) | Second postulate-list item. Record expansion of `sym` if expanded. | 1.00 |
| `253a-09-p014-u06` | Poincar\'e-invariant vacuum \(\lvert\Omega\rangle\) | Third postulate-list item. Record expansion of `invt` if expanded. | 1.00 |
| `253a-09-p014-u07` | local “field” operators \(\hat\phi(x)\) obeying Poincar\'e covariance and microcausality | Fourth postulate-list item. Preserve the quotation marks around `field`. | 1.00 |
| `253a-09-p014-u08` | the properties hold for interacting relativistic particles as well | Scope statement completing the postulate heading. Keep its link to the list explicit. | 0.99 |
| `253a-09-p014-u09` | `How to construct such theories ?` | Transition question from the postulates to a constructive formalism. | 1.00 |
| `253a-09-p014-u10` | a formalism in which Poincar\'e symmetry is manifest | Final transition into the manifestly Poincar\'e-invariant formulation developed next. | 1.00 |

## Boundary note

Physical page 13 ends the free scalar microcausality check. Physical page 14 first verifies field covariance, then elevates the Hilbert-space, symmetry, vacuum, locality, covariance, and microcausality properties to postulates for interacting relativistic systems. Its final two dash bullets pose the construction problem and motivate a manifestly Poincar\'e-symmetric formalism. Physical page 15 begins Problem Set 1, so the last bullet is the chapter's source-page endpoint and forward transition.
