#!/bin/sh
set -eu

edition_root=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
latex_dir="$edition_root/latex"
reference_style_dir="$edition_root/../wittenSUSYintro/latex"
export_dir="$edition_root/../../zhou-quantitative-finance-interviews"
export_pdf="$export_dir/zhou-quantitative-finance-interviews-jhep.pdf"

for dependency in python3 latexmk rg kpsewhich pdfinfo pdffonts pdftotext pdfimages gs shasum
do
  if ! command -v "$dependency" >/dev/null 2>&1
  then
    echo "Missing required dependency: $dependency" >&2
    exit 1
  fi
done

for audit in audit_project.py audit_notation.py audit_transcription.py
do
  if [ ! -f "$edition_root/$audit" ]
  then
    echo "Missing required release audit: $audit" >&2
    exit 1
  fi
done

python3 "$edition_root/verify_source.py"
python3 "$edition_root/audit_project.py"
python3 "$edition_root/audit_notation.py"
python3 "$edition_root/audit_transcription.py" --strict

cd "$latex_dir"
TEXINPUTS="$reference_style_dir:$latex_dir:${TEXINPUTS-}" \
  latexmk -g -pdf -interaction=nonstopmode -halt-on-error master.tex

if rg -n \
  'Undefined control sequence|LaTeX Error|Fatal error|undefined on input line|There were undefined references|multiply defined|Rerun to get cross-references right|Overfull \\hbox|Overfull \\vbox' \
  master.log
then
  echo "LaTeX log audit failed." >&2
  exit 1
fi

if rg -n \
  'zhou-quantitative-finance-interviews\.pdf|zhou-source-preview|facsimile' \
  master.fls
then
  echo "Build imported a source scan or facsimile artifact." >&2
  exit 1
fi

words=$(pdftotext master.pdf - | wc -w | tr -d ' ')
if [ "$words" -lt 45000 ]
then
  echo "Output text is suspiciously short: $words words." >&2
  exit 1
fi

gs -q -dNOPAUSE -dBATCH -sDEVICE=nullpage master.pdf

if pdffonts master.pdf | sed '1,2d' | rg -v ' yes +yes +'
then
  echo "Font audit failed: every font must be embedded and subset." >&2
  exit 1
fi

pages=$(pdfinfo master.pdf | awk '/^Pages:/ {print $2}')
if [ "$pages" -lt 120 ] || [ "$pages" -gt 400 ]
then
  echo "Output page count is outside the native-edition range: $pages." >&2
  exit 1
fi

if pdfimages -list master.pdf | awk 'NR > 2 && $4 >= 1800 && $5 >= 2200 {print; found=1} END {exit !found}'
then
  echo "Full-page raster image detected in native edition." >&2
  exit 1
fi

mkdir -p "$export_dir"
cp master.pdf "$export_pdf"

pdfinfo "$export_pdf"
shasum -a 256 "$export_pdf"
echo "Exported verified native edition to $export_pdf"
