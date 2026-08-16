# Zhou transcription contract

The rendered source PDF is authoritative. Transcribe every visible word, formula,
list item, table entry, figure label, footnote, and heading in the assigned physical
page range. The OCR layer supplies a draft only. Resolve doubtful text and symbols
from a rendered page.

Write one native LaTeX chunk at the assigned path under `latex/transcription/`.
Do not include a preamble or an `\input` command. Keep each chunk independently
readable and safe to assemble in source order.

At the first visible content from every physical PDF page, add a line of this form:

```tex
% ZHOU-SOURCE-PAGE: 17 PRINTED: 1
```

Use `FRONTMATTER` when a source page has no printed Arabic folio. A page marker may
sit between words when the source page breaks inside a sentence. Keep the TeX prose
continuous around that marker.

Use these structural forms:

```tex
\section{General Principles}
\subsection{Problem Simplification}
\problem{Screwy pirates}
\solution
\hint{The source hint text.}
```

The project style defines `\problem`, `\solution`, and `\hint`. Use ordinary
paragraphs after each command, since prose may continue into another chunk. Use
`enumerate`, `itemize`, `description`, `tabular`, `align`, and `equation` where the
source structure calls for them. Preserve source equation numbers when present.

Write mathematics as LaTeX. Check subscripts, superscripts, accents, delimiters,
probability notation, expectation notation, inequalities, matrix entries, bounds,
and differentials against the scan. Keep source variables and capitalization.

Recreate simple diagrams with TikZ or native LaTeX. Put a blocked complex graphic in
`latex/figures/` as a tightly cropped source-derived image and record its physical
page in a nearby comment. Report every such crop in the handoff. Tables must remain
native LaTeX.

Preserve the author's wording and ordering. Repair OCR artifacts during
transcription. Keep visible source spelling and punctuation. Add a `% ZHOU-QUERY:`
comment when the scan leaves a character unresolved after close inspection. Do not
invent missing prose or silently omit unclear material.

Before finishing, run these checks on the chunk:

```sh
rg -n 'ZHOU-QUERY|TODO|TBD|facsimilepages|includepdf' PATH_TO_CHUNK
```

Return the written path, covered physical pages, any query markers, and any graphics
that need an integration review.
