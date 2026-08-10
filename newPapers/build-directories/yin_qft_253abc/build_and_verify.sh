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
python3 "$edition_root/work/253a-ch02/tools/finalize_pass2.py" --check
python3 "$edition_root/scripts/render_chapter02_artifacts.py" --check
python3 "$edition_root/scripts/audit_chapter02.py"

build_once() {
  cd "$latex_dir"
  SOURCE_DATE_EPOCH=1786233600 FORCE_SOURCE_DATE=1 TZ=UTC \
  TEXINPUTS="$reference_style_dir:$latex_dir:${TEXINPUTS-}" \
    latexmk -g -pdf -interaction=nonstopmode -halt-on-error master.tex
}

audit_pdf() {
  cd "$latex_dir"
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

  if [ "$strict" -eq 1 ] && rg -n 'Overfull \\[hv]box' master.log
  then
    echo "Layout audit failed: strict releases allow no overfull boxes." >&2
    exit 1
  fi
}

render_pdf() {
  cd "$latex_dir"
  current_hash=$(shasum -a 256 master.pdf | awk '{print $1}')
  render_dir="$edition_root/qa/rendered/$current_hash"
  mkdir -p "$render_dir"
  pdftoppm -r 180 -png master.pdf "$render_dir/page" >/dev/null 2>&1
  echo "$current_hash"
}

build_once
audit_pdf
first_hash=$(render_pdf)

if [ "$strict" -eq 0 ]
then
  python3 "$edition_root/scripts/render_release_manifest.py" --write
  rg -n 'Overfull \\[hv]box|Underfull \\[hv]box' "$latex_dir/master.log" || true
  echo "Draft build complete at $first_hash; no stable export was written."
  exit 0
fi

python3 "$edition_root/scripts/render_release_manifest.py" --check
python3 "$edition_root/scripts/audit_chapter02.py" --strict

build_once
audit_pdf
second_hash=$(render_pdf)
if [ "$first_hash" != "$second_hash" ]
then
  echo "Deterministic rebuild failed: $first_hash != $second_hash" >&2
  exit 1
fi
python3 "$edition_root/scripts/render_release_manifest.py" --check
python3 "$edition_root/scripts/audit_chapter02.py" --strict

mkdir -p "$export_dir"
temporary_export="$export_dir/.yin-qft-253abc.pdf.tmp.$$"
cp "$latex_dir/master.pdf" "$temporary_export"
mv "$temporary_export" "$export_pdf"
export_hash=$(shasum -a 256 "$export_pdf" | awk '{print $1}')
if [ "$second_hash" != "$export_hash" ]
then
  echo "Export identity check failed." >&2
  exit 1
fi

echo "$export_hash  $(basename "$export_pdf")"
echo "Exported verified edition to $export_pdf"
