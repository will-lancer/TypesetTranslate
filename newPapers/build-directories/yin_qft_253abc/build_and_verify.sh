#!/bin/sh
set -eu

edition_root=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
latex_dir="$edition_root/latex"
reference_style_dir="$edition_root/../wittenSUSYintro/latex"
export_dir="$edition_root/../.."
export_pdf="$export_dir/yin-qft-253abc.pdf"

for dependency in python3 latexmk rg pdfinfo pdffonts pdftotext pdftoppm gs shasum
do
  if ! command -v "$dependency" >/dev/null 2>&1
  then
    echo "Missing required dependency: $dependency" >&2
    exit 1
  fi
done

case "${1-}" in
  "") strict=1 ;;
  "--draft") strict=0 ;;
  *) echo "Usage: ./build_and_verify.sh [--draft]" >&2; exit 2 ;;
esac

python3 "$edition_root/scripts/verify_source.py"
python3 "$edition_root/scripts/test_written_prose_audit.py"
if [ "$strict" -eq 1 ]
then
  python3 "$edition_root/scripts/render_written_provenance.py" --check
  python3 "$edition_root/scripts/audit_project.py" --strict
else
  python3 "$edition_root/scripts/audit_project.py"
fi

cd "$latex_dir"
TEXINPUTS="$reference_style_dir:$latex_dir:${TEXINPUTS-}" \
  latexmk -g -pdf -interaction=nonstopmode -halt-on-error master.tex

if rg -n \
  'Undefined control sequence|LaTeX Error|Fatal error|Missing character|undefined on input line|There were undefined references|Citation .* undefined|Reference .* undefined|Hyper reference .* undefined|multiply defined|destination with the same identifier|Rerun to get cross-references right' \
  master.log
then
  echo "LaTeX error or reference audit failed." >&2
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

mkdir -p "$edition_root/qa/rendered"
pdftoppm -r 180 -png master.pdf "$edition_root/qa/rendered/pilot" >/dev/null 2>&1

if [ "$strict" -eq 1 ]
then
  if rg -n 'Overfull \\[hv]box' master.log
  then
    echo "Layout audit failed: strict releases allow no overfull boxes." >&2
    exit 1
  fi
  mkdir -p "$export_dir"
  cp master.pdf "$export_pdf"
  build_hash=$(shasum -a 256 master.pdf | awk '{print $1}')
  export_hash=$(shasum -a 256 "$export_pdf" | awk '{print $1}')
  if [ "$build_hash" != "$export_hash" ]
  then
    echo "Export identity check failed." >&2
    exit 1
  fi
  echo "$export_hash  $(basename "$export_pdf")"
  echo "Exported verified edition to $export_pdf"
else
  rg -n 'Overfull \\[hv]box|Underfull \\[hv]box' master.log || true
  echo "Draft build complete; no stable export was written."
fi
