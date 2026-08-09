#!/bin/sh
set -eu

edition_root=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
latex_dir="$edition_root/latex"
edition_name=$(basename "$edition_root")
export_dir="$edition_root/../.."

case "$edition_name" in
  weinberg_vol1_exercises)
    export_name="weinberg-vol1-exercises.pdf"
    ;;
  weinberg_vol2_exercises)
    export_name="weinberg-vol2-exercises.pdf"
    ;;
  weinberg_vol3_exercises)
    export_name="weinberg-vol3-exercises.pdf"
    ;;
  *)
    echo "Unsupported exercise-edition directory: $edition_name" >&2
    exit 2
    ;;
esac

for dependency in python3 latexmk rg pdfinfo pdffonts pdftotext gs shasum
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
  python3 "$edition_root/audit_exercises.py" --strict
else
  python3 "$edition_root/audit_exercises.py"
fi
python3 "$edition_root/render_inventory.py"
python3 "$edition_root/render_source_ledger.py"

cd "$latex_dir"
latexmk -g -pdf -interaction=nonstopmode -halt-on-error master.tex
python3 "$edition_root/render_index_pagination.py"

if rg -n \
  'Undefined control sequence|LaTeX Error|Fatal error|undefined on input line|There were undefined references|Citation .* undefined|Reference .* undefined|Hyper reference .* undefined|multiply defined|destination with the same identifier|Rerun to get cross-references right' \
  master.log
then
  echo "LaTeX error/reference audit failed." >&2
  exit 1
fi

pdftotext master.pdf - >/dev/null
pdfinfo master.pdf
gs -q -dNOPAUSE -dBATCH -sDEVICE=nullpage master.pdf

if pdffonts master.pdf | sed '1,2d' | rg -v ' yes +yes +'
then
  echo "Font audit failed: every font must be embedded and subset." >&2
  exit 1
fi

if [ "$strict" -eq 1 ]
then
  if rg -n 'Overfull \\[hv]box' master.log
  then
    echo "Layout audit failed: strict releases allow no overfull boxes." >&2
    exit 1
  fi
  mkdir -p "$export_dir"
  cp master.pdf "$export_dir/$export_name"
  build_hash=$(shasum -a 256 master.pdf | awk '{print $1}')
  export_hash=$(shasum -a 256 "$export_dir/$export_name" | awk '{print $1}')
  if [ "$build_hash" != "$export_hash" ]
  then
    echo "Export identity check failed." >&2
    exit 1
  fi
  echo "$export_hash  $export_name"
  echo "Exported verified exercise edition to $export_dir/$export_name"
else
  rg -n 'Overfull \\[hv]box|Underfull \\[hv]box' master.log || true
  echo "Draft build complete; no stable export was written."
fi
