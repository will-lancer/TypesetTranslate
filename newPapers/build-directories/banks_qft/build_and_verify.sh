#!/bin/sh
set -eu

root=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
latex_dir="$root/latex"
scripts_dir="$root/scripts"
release_dir=$(CDPATH= cd -- "$root/../.." && pwd)/banks-qft

strict=0
edition=base
while [ "$#" -gt 0 ]
do
  case "$1" in
    --draft)
      strict=0
      shift
      ;;
    --strict)
      strict=1
      shift
      ;;
    --edition)
      edition=${2-}
      shift 2
      ;;
    *)
      echo "Usage: ./build_and_verify.sh [--draft|--strict] [--edition base|implicit]" >&2
      exit 2
      ;;
  esac
done
if [ "$edition" != base ] && [ "$edition" != implicit ]
then
  echo "Edition must be base or implicit" >&2
  exit 2
fi

. "$root/reproducible-build.env"
export SOURCE_DATE_EPOCH FORCE_SOURCE_DATE TZ LC_ALL

for dependency in python3 latexmk pdflatex kpsewhich pdfinfo pdffonts pdftotext pdfimages pdftoppm gs cmp
do
  command -v "$dependency" >/dev/null 2>&1 || {
    echo "Missing dependency: $dependency" >&2
    exit 1
  }
done

python3 "$scripts_dir/verify_source.py"
python3 "$scripts_dir/render_page_dispositions.py"
if [ "$strict" -eq 1 ]
then
  python3 "$scripts_dir/verify_source_render.py" \
    --manifest "$root/SOURCE_MANIFEST.yaml" \
    --output "$root/work/reviews/source-render-provenance.json"
fi

if [ "$edition" = implicit ] && [ "$strict" -eq 1 ]
then
  if [ ! -s "$root/work/reviews/base-freeze.json" ]
  then
    echo "The base edition has no frozen release record" >&2
    exit 1
  fi
  (cd "$latex_dir" && latexmk -g -pdf -interaction=nonstopmode -halt-on-error master.tex)
  python3 "$scripts_dir/verify_base_freeze.py" \
    --pdf "$latex_dir/master.pdf" \
    --fls "$latex_dir/master.fls" \
    --release-record "$root/work/reviews/base-freeze.json"
fi

convention_audit="$root/work/reviews/convention-audit-$edition.json"
if [ "$strict" -eq 1 ]
then
  python3 "$scripts_dir/audit_conventions.py" \
    --edition "$edition" --strict --output "$convention_audit"
fi

if [ "$strict" -eq 1 ]
then
  python3 "$scripts_dir/audit_project.py" --strict --edition "$edition"
else
  python3 "$scripts_dir/audit_project.py" --edition "$edition"
fi

if [ "$edition" = base ]
then
  stem=master
  release_name=banks-qft-exercise-edition.pdf
else
  stem=master-implicit
  release_name=banks-qft-implicit-exercise-edition.pdf
fi

(cd "$latex_dir" && latexmk -g -pdf -interaction=nonstopmode -halt-on-error "$stem.tex")

check_args=
if [ "$strict" -eq 1 ]
then
  check_args=--strict
fi
python3 "$scripts_dir/check_pdf.py" \
  "$latex_dir/$stem.pdf" \
  --log "$latex_dir/$stem.log" \
  --fls "$latex_dir/$stem.fls" \
  $check_args

input_manifest="$root/work/build-input-$edition.json"
python3 "$scripts_dir/build_input_manifest.py" \
  --edition "$edition" \
  --fls "$latex_dir/$stem.fls" \
  --pdf "$latex_dir/$stem.pdf" \
  --output "$input_manifest"
python3 "$scripts_dir/audit_compiled_dependencies.py" \
  --edition "$edition" --manifest "$input_manifest" --pdf "$latex_dir/$stem.pdf"

text_recall="$root/work/reviews/text-recall-$edition.json"
if [ "$strict" -eq 1 ]
then
  python3 "$scripts_dir/audit_text_recall.py" \
    --edition "$edition" --pdf "$latex_dir/$stem.pdf" --output "$text_recall" --strict
else
  python3 "$scripts_dir/audit_text_recall.py" \
    --edition "$edition" --pdf "$latex_dir/$stem.pdf" --output "$text_recall"
fi

if [ "$strict" -eq 0 ]
then
  echo "Draft build complete: $latex_dir/$stem.pdf"
  exit 0
fi

reproducibility="$root/work/reviews/reproducibility-$edition.json"
python3 "$scripts_dir/check_reproducibility.py" \
  --edition "$edition" \
  --current-pdf "$latex_dir/$stem.pdf" \
  --input-manifest "$input_manifest" \
  --output "$reproducibility"

render_dir="$root/work/rendered-$edition"
render_manifest="$render_dir/manifest.jsonl"
python3 "$scripts_dir/render_release.py" render \
  --pdf "$latex_dir/$stem.pdf" \
  --output-dir "$render_dir" \
  --manifest "$render_manifest"

reviews_dir="$root/work/reviews/page-inspection-$edition"
visual_review="$root/work/reviews/visual-review-$edition.json"
set -- "$reviews_dir"/*.jsonl
if [ ! -f "$1" ]
then
  echo "Missing visual-review records under $reviews_dir" >&2
  exit 1
fi
python3 "$scripts_dir/render_release.py" validate \
  --pdf "$latex_dir/$stem.pdf" \
  --output-dir "$render_dir" \
  --manifest "$render_manifest" \
  --reviews "$@" \
  --summary "$visual_review"

python3 "$scripts_dir/finalize_release.py" \
  --edition "$edition" \
  --compiled "$latex_dir/$stem.pdf" \
  --release "$release_dir/$release_name" \
  --input-manifest "$input_manifest" \
  --reproducibility "$reproducibility" \
  --render-manifest "$render_manifest" \
  --review-coverage "$root/review-coverage-$edition.json" \
  --solution-review "$root/solution-review-$edition.json" \
  --source-render "$root/work/reviews/source-render-provenance.json" \
  --visual-review "$visual_review" \
  --text-recall "$text_recall" \
  --convention-audit "$convention_audit" \
  --output-record "$root/work/release-$edition.json"

python3 "$scripts_dir/verify_source.py"
python3 "$scripts_dir/audit_project.py" --strict --edition "$edition"
python3 "$scripts_dir/check_pdf.py" \
  "$release_dir/$release_name" \
  --log "$latex_dir/$stem.log" \
  --fls "$latex_dir/$stem.fls" \
  --strict
cmp "$latex_dir/$stem.pdf" "$release_dir/$release_name"
python3 "$scripts_dir/audit_conventions.py" \
  --edition "$edition" --strict --output "$convention_audit"
python3 - "$root/work/release-$edition.json" "$convention_audit" <<'PY'
import hashlib
import json
import sys
from pathlib import Path


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


record_path = Path(sys.argv[1])
audit_path = Path(sys.argv[2])
record = json.loads(record_path.read_text(encoding="utf-8"))
audit = json.loads(audit_path.read_text(encoding="utf-8"))
if record.get("convention_audit_sha256") != sha256(audit_path):
    raise SystemExit("Post-final convention audit differs from the release record")
if record.get("audits", {}).get("convention_audit") != "pass":
    raise SystemExit("Release record has no passing convention-audit status")
if audit.get("status") != "pass" or audit.get("findings_count") != 0:
    raise SystemExit("Post-final convention audit did not pass")
PY
if [ "$edition" = implicit ]
then
  python3 "$scripts_dir/write_release_verification.py"
fi
echo "Strict release complete: $release_dir/$release_name"
