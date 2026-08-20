#!/bin/sh
set -eu

edition_root=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
latex_dir="$edition_root/latex"
scripts_dir="$edition_root/scripts"

# Load the same fixed values used by the isolated reproducibility checker
# before either the draft or strict LaTeX build starts.
. "$edition_root/reproducible-build.env"
export SOURCE_DATE_EPOCH FORCE_SOURCE_DATE TZ LC_ALL

for dependency in python3 latexmk tesseract rg pdfinfo pdffonts pdftotext pdfimages pdftoppm gs shasum cmp mv cp
do
  if ! command -v "$dependency" >/dev/null 2>&1
  then
    echo "Missing required dependency: $dependency" >&2
    exit 1
  fi
done

case "${1-}" in
  "")
    strict=1
    ;;
  "--draft")
    strict=0
    ;;
  *)
    echo "Usage: ./build_and_verify.sh [--draft]" >&2
    exit 2
    ;;
esac

if [ "$strict" -eq 1 ]
then
  python3 "$scripts_dir/render_page_dispositions.py" --write --strict
  python3 "$scripts_dir/audit_source.py" --strict
  python3 "$scripts_dir/audit_notation.py" --strict
  python3 "$scripts_dir/audit_project.py" --strict
else
  python3 "$scripts_dir/render_page_dispositions.py" --write
  python3 "$scripts_dir/audit_source.py"
  python3 "$scripts_dir/audit_notation.py"
  python3 "$scripts_dir/audit_project.py"
fi

if [ "$strict" -eq 1 ]
then
  python3 "$scripts_dir/audit_transcription.py" --strict
  python3 "$scripts_dir/check_transcription_review.py" --strict
else
  python3 "$scripts_dir/audit_transcription.py"
fi

cd "$latex_dir"
latexmk -g -pdf -interaction=nonstopmode -halt-on-error master.tex

# A successful latexmk exit is not enough for release evidence. These files
# are required before any diagnostic scan can run, so a missing recorder or
# log cannot fall through an inverted grep condition.
for required_artifact in master.log master.fls master.pdf
do
  if [ ! -s "$required_artifact" ]
  then
    echo "Missing or empty required build artifact: $latex_dir/$required_artifact" >&2
    exit 1
  fi
done

if rg -n \
  'Undefined control sequence|LaTeX Error|Fatal error|Emergency stop|Runaway argument|Missing \\endgroup' \
  master.log
then
  echo "LaTeX compilation audit failed." >&2
  exit 1
fi

if rg -n \
  'facsimile|source-pages|origPapers|pct_spin_statistics_all_that\.pdf|pdfpages|includepdf' \
  master.fls
then
  echo "Build imported a source scan or facsimile artifact." >&2
  exit 1
fi

pdftotext master.pdf - >/dev/null
pdfinfo master.pdf >/dev/null

if [ "$strict" -eq 1 ]
then
  # This command writes reproducibility evidence only after two isolated
  # fixed-environment builds have identical PDF bytes. The finalizer checks
  # that evidence against the current input tree and master.pdf.
  python3 "$scripts_dir/check_reproducibility.py" check

  rendered_dir="$edition_root/work/rendered-output"
  rendered_manifest="$rendered_dir/manifest.jsonl"
  inspection_parts="$edition_root/work/reviews/page-inspection-parts"
  inspection_manifest="$edition_root/work/reviews/page-inspection.jsonl"
  python3 "$scripts_dir/render_release_evidence.py" render \
    --input "$latex_dir/master.pdf" \
    --output-dir "$rendered_dir" \
    --manifest "$rendered_manifest" \
    --dpi 180

  # Reviewers create one checksum-bound record per page-range file. The
  # assembler fails when any page is absent, duplicated, or still pending.
  python3 "$scripts_dir/assemble_page_inspections.py" \
    --input "$latex_dir/master.pdf" \
    --manifest "$rendered_manifest" \
    --parts-dir "$inspection_parts" \
    --output "$inspection_manifest"
  python3 "$scripts_dir/render_release_evidence.py" validate \
    --input "$latex_dir/master.pdf" \
    --output-dir "$rendered_dir" \
    --manifest "$rendered_manifest" \
    --inspection-manifest "$inspection_manifest" \
    --require-inspection

  # The finalizer owns the only export path. It runs the complete
  # fail-closed post-compile audit, stages and byte-checks the export, writes
  # the release record, closes Pass 4, and runs the final audit again.
  python3 "$scripts_dir/audit_release_pipeline.py" finalize
else
  echo "Draft build complete: $latex_dir/master.pdf"
fi
