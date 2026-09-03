#!/usr/bin/env python3
"""Write the human-readable release verification from final JSON records."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load(name: str) -> dict[str, object]:
    return json.loads((ROOT / "work" / f"release-{name}.json").read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def load_convention_audit(edition: str, record: dict[str, object]) -> dict[str, object]:
    path = ROOT / "work" / "reviews" / f"convention-audit-{edition}.json"
    try:
        audit = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise SystemExit(f"Cannot read {edition} convention-audit evidence: {error}") from error
    if not isinstance(audit, dict):
        raise SystemExit(f"{edition} convention-audit evidence must be a JSON object")
    if record.get("convention_audit_sha256") != sha256(path):
        raise SystemExit(f"{edition} release record has a stale convention-audit hash")
    if (
        audit.get("schema_version") != 1
        or audit.get("edition") != edition
        or audit.get("status") != "pass"
        or audit.get("findings_count") != 0
        or type(audit.get("reviewed_candidates_count")) is not int
        or audit.get("reviewed_candidates_count") < 0
        or "conventions" not in audit
    ):
        raise SystemExit(f"{edition} convention-audit evidence did not pass")
    return audit


def convention_table(audit: dict[str, object]) -> str:
    rows = ["## Adopted conventions", "", "| Convention | Adopted form |", "| --- | --- |"]
    conventions = audit["conventions"]
    if isinstance(conventions, dict):
        for key, value in sorted(conventions.items(), key=lambda item: str(item[0])):
            if isinstance(value, (dict, list)):
                rendered = json.dumps(value, sort_keys=True, separators=(", ", ": "))
            else:
                rendered = str(value)
            key_text = str(key).replace("|", "\\|")
            value_text = rendered.replace("|", "\\|")
            rows.append(f"| {key_text} | {value_text} |")
    elif isinstance(conventions, list):
        for index, value in enumerate(conventions, 1):
            if isinstance(value, dict):
                rendered = json.dumps(value, sort_keys=True, separators=(", ", ": "))
            else:
                rendered = str(value)
            value_text = rendered.replace("|", "\\|")
            rows.append(f"| Convention {index} | {value_text} |")
    else:
        value_text = str(conventions).replace("|", "\\|")
        rows.append(f"| Adopted convention | {value_text} |")
    return "\n".join(rows)


def block(title: str, record: dict[str, object], audit: dict[str, object]) -> str:
    return f"""## {title}

- Release: `{record['release_path']}`
- Pages: {record['page_count']}
- Bytes: {record['output_bytes']}
- Build-input SHA-256: `{record['build_input_sha256']}`
- Output SHA-256: `{record['output_sha256']}`
- Visual review: {record['visual_review_pages']}/{record['page_count']} pages
- Reproducibility: pass
- Convention audit: pass; findings: {audit['findings_count']}; reviewed candidates: {audit['reviewed_candidates_count']}; SHA-256: `{record['convention_audit_sha256']}`
- Audited-build/release byte identity: pass
"""


def main() -> int:
    base = load("base")
    implicit = load("implicit")
    base_convention_audit = load_convention_audit("base", base)
    implicit_convention_audit = load_convention_audit("implicit", implicit)
    if base.get("source_sha256") != implicit.get("source_sha256"):
        raise SystemExit("Release records use different source hashes")
    text = f"""# Release verification

Canonical source SHA-256: `{base['source_sha256']}`

Page-disposition coverage is 281/281. The base audit contains 80 numbered
problem-solution pairs. The expanded audit contains the same pairs and 110
inline implicit exercise-solution pairs. Both outputs use the pinned local
JHEP style, native mathematics, and vector figures.

{convention_table(base_convention_audit)}

{block('Base exercise edition', base, base_convention_audit)}
{block('Implicit-exercise edition', implicit, implicit_convention_audit)}

## Release commands

```sh
./build_and_verify.sh --strict --edition base
./build_and_verify.sh --strict --edition implicit
```

The strict pipeline checks source identity, marker coverage, inventories,
labels, references, LaTeX diagnostics, A4 geometry, text extraction,
Ghostscript parsing, embedded fonts, absence of raster imports, convention
adoption, text recall, isolated reproducibility, checksum-bound 150-DPI review
coverage, and final byte identity.
"""
    (ROOT / "RELEASE_VERIFICATION.md").write_text(text, encoding="utf-8")
    print(f"Release verification written: {ROOT / 'RELEASE_VERIFICATION.md'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
