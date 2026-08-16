#!/bin/sh
set -eu

edition_root=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
latex_dir="$edition_root/latex"
export_dir="$edition_root/../../zhou-quantitative-finance-interviews"
export_pdf="$export_dir/zhou-quantitative-finance-interviews-jhep.pdf"

for dependency in python3 latexmk rg kpsewhich pdfinfo pdffonts pdftotext pdftoppm gs shasum
do
  if ! command -v "$dependency" >/dev/null 2>&1
  then
    echo "Missing required dependency: $dependency" >&2
    exit 1
  fi
done

python3 "$edition_root/verify_source.py"
python3 "$edition_root/audit_project.py"

cd "$latex_dir"
latexmk -g -pdf -interaction=nonstopmode -halt-on-error master.tex

if rg -n \
  'Undefined control sequence|LaTeX Error|Fatal error|undefined on input line|There were undefined references|multiply defined|Rerun to get cross-references right|Overfull \\hbox|Overfull \\vbox' \
  master.log
then
  echo "LaTeX log audit failed." >&2
  exit 1
fi

pdftotext master.pdf - >/dev/null
gs -q -dNOPAUSE -dBATCH -sDEVICE=nullpage master.pdf

if pdffonts master.pdf | sed '1,2d' | rg -v ' yes +yes +'
then
  echo "Font audit failed: every font must be embedded and subset." >&2
  exit 1
fi

pages=$(pdfinfo master.pdf | awk '/^Pages:/ {print $2}')
if [ "$pages" -ne 199 ]
then
  echo "Output page-count mismatch: expected 199, found $pages." >&2
  exit 1
fi

mkdir -p "$export_dir"
cp master.pdf "$export_pdf"

pdfinfo "$export_pdf"
shasum -a 256 "$export_pdf"
echo "Exported verified edition to $export_pdf"
