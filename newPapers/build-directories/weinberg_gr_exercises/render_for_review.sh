#!/bin/sh
set -eu

edition_root=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
pdf="$edition_root/latex/master.pdf"
first="${1-1}"
last="${2-}"
review_dir="${3-}"

case "$first" in
  *[!0-9]*|"")
    echo "First page must be a positive integer." >&2
    exit 2
    ;;
esac
if [ -n "$last" ]; then
  case "$last" in
    *[!0-9]*)
      echo "Last page must be a positive integer." >&2
      exit 2
      ;;
  esac
fi

if [ ! -f "$pdf" ]; then
  echo "Missing $pdf; run ./build_and_verify.sh --draft first." >&2
  exit 1
fi

if [ -z "$review_dir" ]; then
  review_dir=$(mktemp -d /private/tmp/weinberg-gr-review.XXXXXX)
else
  mkdir -p "$review_dir"
fi

if [ -n "$last" ]; then
  pdftoppm -png -r 160 -f "$first" -l "$last" \
    "$pdf" "$review_dir/page"
else
  pdftoppm -png -r 160 -f "$first" "$pdf" "$review_dir/page"
fi

echo "Rendered review pages to $review_dir"
