#!/bin/sh
set -eu

edition_root=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
latex_dir="$edition_root/latex"
export_dir="$edition_root/../../weinberg-qft-two-component"

python3 "$edition_root/verify_spinor_conventions.py"
python3 "$edition_root/verify_superspace_conventions.py"
python3 "$edition_root/audit_two_component.py" --strict
python3 "$edition_root/audit_semantic_hotspots.py"

cd "$latex_dir"
latexmk -g -pdf -interaction=nonstopmode -halt-on-error master.tex

if rg -n \
  'Undefined control sequence|LaTeX Error|Fatal error|undefined on input line|There were undefined references|Citation .* undefined|Reference .* undefined|Hyper reference .* undefined|multiply defined|Rerun to get cross-references right' \
  master.log
then
  echo "LaTeX reference audit failed." >&2
  exit 1
fi

python3 "$edition_root/audit_layout.py"
pdftotext master.pdf - >/dev/null
mkdir -p "$export_dir"
cp master.pdf "$export_dir/weinberg-vol3-two-component.pdf"
pdfinfo "$export_dir/weinberg-vol3-two-component.pdf"
