#!/bin/sh
set -eu

build_root=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
export_root="$build_root/../weinberg-qft-exercises"

for edition in \
  weinberg_vol1_exercises \
  weinberg_vol2_exercises \
  weinberg_vol3_exercises
do
  "$build_root/$edition/build_and_verify.sh" --draft
done

for edition in \
  weinberg_vol1_exercises \
  weinberg_vol2_exercises \
  weinberg_vol3_exercises
do
  python3 "$build_root/$edition/audit_exercises.py" --strict
  if rg -n 'Overfull \\[hv]box' "$build_root/$edition/latex/master.log"
  then
    echo "Layout audit failed for $edition." >&2
    exit 1
  fi
done

python3 "$build_root/audit_weinberg_qft_cross_volume.py"

mkdir -p "$export_root"
for volume in 1 2 3
do
  edition="weinberg_vol${volume}_exercises"
  export_name="weinberg-vol${volume}-exercises.pdf"
  staged_export="$export_root/.${export_name}.stage.$$"
  cp "$build_root/$edition/latex/master.pdf" "$staged_export"
  build_hash=$(shasum -a 256 "$build_root/$edition/latex/master.pdf" | awk '{print $1}')
  export_hash=$(shasum -a 256 "$staged_export" | awk '{print $1}')
  if [ "$build_hash" != "$export_hash" ]
  then
    echo "Export identity check failed for $edition." >&2
    exit 1
  fi
done

for volume in 1 2 3
do
  export_name="weinberg-vol${volume}-exercises.pdf"
  staged_export="$export_root/.${export_name}.stage.$$"
  mv "$staged_export" "$export_root/$export_name"
done

python3 "$build_root/render_weinberg_qft_release_manifest.py"

echo "All three Weinberg QFT exercise editions passed the release pipeline."
