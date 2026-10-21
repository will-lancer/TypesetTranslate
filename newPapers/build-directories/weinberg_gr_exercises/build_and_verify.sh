#!/bin/sh
set -eu

edition_root=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
latex_dir="$edition_root/latex"
export_dir="$edition_root/../../weinberg-gr-exercises"
export_pdf="$export_dir/weinberg-gr-exercises.pdf"

for dependency in python3 latexmk rg pdfinfo pdffonts pdftotext pdftoppm gs
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

python3 "$edition_root/canonical_guard.py"
python3 "$edition_root/verify_source.py"
python3 "$edition_root/source_corpus.py"
python3 "$edition_root/provisional_dispositions.py"

if [ "$strict" -eq 1 ]; then
  python3 "$edition_root/source_inventory.py" --strict
  python3 "$edition_root/audit_transcription.py" --strict
  python3 "$edition_root/source_manifest.py" --check
  python3 "$edition_root/audit_notation.py" --strict
  python3 "$edition_root/audit_exercises.py" --strict
else
  python3 "$edition_root/source_inventory.py"
  python3 "$edition_root/audit_transcription.py"
  python3 "$edition_root/source_manifest.py" --check || true
  python3 "$edition_root/audit_notation.py"
  python3 "$edition_root/audit_exercises.py"
fi
python3 "$edition_root/audit_index.py"

cd "$latex_dir"
latexmk -g -pdf -interaction=nonstopmode -halt-on-error master.tex

if [ "$strict" -eq 1 ]; then
  if rg -n \
    'Undefined control sequence|LaTeX Error|Fatal error|undefined on input line|There were undefined references|Citation .* undefined|Reference .* undefined|Hyper reference .* undefined|multiply defined|Rerun to get cross-references right' \
    master.log
  then
    echo "LaTeX reference audit failed." >&2
    exit 1
  fi
  python3 "$edition_root/audit_layout.py"
else
  python3 "$edition_root/audit_layout.py" --report-only
  rg -n \
    'undefined on input line|There were undefined references|Citation .* undefined|Reference .* undefined|Overfull \\hbox|Underfull \\hbox' \
    master.log || true
fi

pdftotext master.pdf - >/dev/null
pdfinfo master.pdf

if [ "$strict" -eq 1 ]; then
  python3 "$edition_root/canonical_guard.py"
  gs -q -dNOPAUSE -dBATCH -sDEVICE=nullpage master.pdf
  if pdffonts master.pdf | sed '1,2d' | rg -v ' yes +yes +'
  then
    echo "Font audit failed: every font must be embedded and subset." >&2
    exit 1
  fi
  mkdir -p "$export_dir"
  cp master.pdf "$export_pdf"
  shasum -a 256 "$export_pdf"
  echo "Exported verified edition to $export_pdf"
fi
