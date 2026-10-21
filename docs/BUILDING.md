# Working on an edition

[Repository](../README.md) · [Book catalogue](../newPapers/README.md)

Choose an edition from the catalogue and open its source directory. Read its
README and notation policy before editing. Chapters usually live under
`latex/`, alongside the master document and local style files.

## Build commands

Projects with `build_and_verify.sh` document their options in their README.
Run the script from the project directory. These scripts combine compilation
with the project's review checks and export rules.

For example, a Wald integration build is:

```sh
cd newPapers/build-directories/wald_gr
./build_and_verify.sh --draft
```

Banks selects an edition explicitly:

```sh
cd newPapers/build-directories/banks_qft
./build_and_verify.sh --draft --edition base
```

Its release command uses `--strict`; see the
[Banks README](../newPapers/build-directories/banks_qft/README.md) for both
editions. Other scripts have their own defaults.

For projects without a build script, compile from their `latex/` directory:

```sh
cd newPapers/build-directories/milnorTopFromDiffView/latex
latexmk -pdf -interaction=nonstopmode -halt-on-error master.tex
```

Witten's entry point is `wittenSUSYintro.tex`. Keep the bundled `.sty` files
beside the master. Projects can also require packages installed in the TeX
distribution, as described in their notes.

Wald's QFT edition requires XeLaTeX. From its `latex/` directory, run:

```sh
cd newPapers/build-directories/wald-qft/latex
latexmk -xelatex master.tex
```

Build scripts list required tools near the top. Common dependencies include
Python 3, `latexmk`, and Poppler utilities; some projects also use Ghostscript
or OCR tools. Full books and page-rendering audits can require substantial
computation. Run those workloads on a suitable remote runner unless the user
has explicitly approved that workload on this Mac.

## Where files belong

| Material | Location |
| --- | --- |
| Exported PDFs | The book's folder directly under `newPapers/` |
| LaTeX and local styles | The edition's `latex/` directory |
| Project scripts and review records | The edition's build workspace |
| Original scans | `origPapers/`, or the source location recorded by the project |
| New temporary renderings | An ignored project output directory or `/private/tmp` |

For a new edition, use a descriptive folder name and add a catalogue row
linking its PDF and source. Document the master filename and export destination
in its README. Existing build-directory names are used by scripts and
cross-edition checks.

When moving an export, update the build destination and every manifest or guard
that resolves its path. Preserve the recorded content hashes. Existing release
records describe the builds they checked; a new release needs its own checks.

For editions built directly with `latexmk`, copy the reviewed PDF into the
catalogue's destination after completing the applicable checks.
