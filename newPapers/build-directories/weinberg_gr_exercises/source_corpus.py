#!/usr/bin/env python3
"""Generate and verify the cached supplementary-source document corpus."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parent
CACHE = ROOT / "tmp" / "source-audit"
MANIFEST = ROOT / "source-corpus.json"

CAMBRIDGE_COURSES = (
    "Gravitational Waves and Numerical Relativity",
    "Formation, Structure and Evolution of Stars",
    "Structure and Evolution of Stars",
    "Field Theory in Cosmology",
    "Early Universe Cosmology",
    "Relativistic Astrophysics",
    "Astrophysical Fluid Dynamics",
    "Astrophysical Black Holes",
    "Advanced Cosmology",
    "Physical Cosmology",
    "Quantum Cosmology",
    "General Relativity",
    "Black Holes",
    "Cosmology",
)

CENTRAL_EXAMPLES: dict[str, tuple[str, int]] = {
    "3A1a": ("Astrophysical Fluid Dynamics", 2021),
    "3A1b": ("Astrophysical Fluid Dynamics", 2021),
    "3A1c": ("Astrophysical Fluid Dynamics", 2021),
    "3A1d": ("Astrophysical Fluid Dynamics", 2021),
    "3A2a": ("Structure and Evolution of Stars", 2025),
    "3A2b": ("Structure and Evolution of Stars", 2025),
    "3A2c": ("Structure and Evolution of Stars", 2025),
    "3A2d": ("Structure and Evolution of Stars", 2025),
    "3A7a": ("Dynamics of Astrophysical Discs", 2023),
    "3A7b": ("Dynamics of Astrophysical Discs", 2023),
    "3A7c": ("Dynamics of Astrophysical Discs", 2023),
    "3A10a": ("Binary Stars", 2022),
    "3A10b": ("Binary Stars", 2022),
    "3A10c": ("Binary Stars", 2022),
    "3R1a": ("General Relativity", 2019),
    "3R1b": ("General Relativity", 2019),
    "3R1c": ("General Relativity", 2019),
    "3R1d": ("General Relativity", 2019),
    "3R2a": ("Cosmology", 2015),
    "3R2b": ("Cosmology", 2015),
    "3R2c": ("Cosmology", 2017),
    "3R2d": ("Cosmology", 2015),
    "3R3a": ("Black Holes", 2025),
    "3R3b": ("Black Holes", 2025),
    "3R3c": ("Black Holes", 2025),
    "3R3d": ("Black Holes", 2025),
    "3R6a": ("Applications of Differential Geometry to Physics", 2020),
    "3R6b": ("Applications of Differential Geometry to Physics", 2020),
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def pdf_pages(path: Path) -> int:
    result = subprocess.run(
        ["pdfinfo", str(path)],
        check=True,
        capture_output=True,
        text=True,
    )
    for line in result.stdout.splitlines():
        if line.startswith("Pages:"):
            return int(line.split(":", 1)[1].strip())
    raise ValueError(f"pdfinfo did not report a page count for {path}")


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def exam_course(text: str) -> str:
    # Examination covers can be followed by questions mentioning another
    # course name (for example, a Black Holes question may say "general
    # relativity").  Restrict identification to the cover page.
    normalized = " ".join(text.split("\f", 1)[0].split()).upper()
    for course in CAMBRIDGE_COURSES:
        if course.upper() in normalized:
            return course
    raise ValueError("Cannot identify Cambridge examination course")


def record_for(pdf: Path) -> dict[str, object]:
    relative = pdf.relative_to(ROOT).as_posix()
    text_path = pdf.with_suffix(".txt")
    if not text_path.is_file():
        raise FileNotFoundError(f"Missing layout-preserving extraction: {text_path}")
    text = text_path.read_text(encoding="utf-8", errors="replace")
    group = pdf.parent.name
    name = pdf.stem
    ancillary = False

    if group == "cambridge-exams":
        match = re.fullmatch(r"(\d{4})-(.+)", pdf.name)
        if match is None:
            raise ValueError(f"Unexpected Cambridge exam filename: {pdf.name}")
        year = int(match.group(1))
        original_name = match.group(2)
        paper_match = re.search(r"paper_?(\d+)", original_name, re.IGNORECASE)
        if paper_match is None:
            raise ValueError(f"Cannot read paper number from {pdf.name}")
        paper = int(paper_match.group(1))
        ancillary = "correction" in original_name.lower()
        course = "Black Holes" if ancillary else exam_course(text)
        document_id = f"cambridge-partiii-{year}-paper{paper}"
        if ancillary:
            document_id += "-correction"
        url = (
            "https://www.maths.cam.ac.uk/postgrad/part-iii/files/"
            f"pastpapers/{year}/{original_name}"
        )
        source_family = "cambridge-part-iii"
        institution = "University of Cambridge"
        kind = "correction" if ancillary else "examination"
        locator = f"Mathematical Tripos Part III, {year}, Paper {paper}"
    elif group == "tong-gr":
        sheet = int(re.search(r"(\d+)", name).group(1))
        year = 2019
        course = "General Relativity"
        document_id = f"tong-gr-2019-sheet{sheet}"
        url = f"https://davidtong.org/pdfs/teaching/general-relativity/idk{sheet}.pdf"
        source_family = "tong"
        institution = "David Tong, University of Cambridge"
        kind = "example-sheet"
        locator = f"General Relativity, Example Sheet {sheet}"
    elif group == "tong-cosmology":
        letter = name.rsplit("-", 1)[-1]
        sheet = ord(letter) - ord("a") + 1
        year = 2019
        course = "Cosmology"
        document_id = f"tong-cosmology-2019-sheet{sheet}"
        url = f"https://davidtong.org/pdfs/teaching/cosmology/fls{letter}.pdf"
        source_family = "tong"
        institution = "David Tong, University of Cambridge"
        kind = "example-sheet"
        locator = f"Cosmology, Example Sheet {sheet}"
    elif group == "mit-8.962":
        number = int(re.search(r"ps(\d+)", name).group(1))
        year = 2018
        course = "8.962 General Relativity"
        document_id = f"mit-8.962-2018-ps{number:02d}"
        url = f"https://web.mit.edu/8.962/www/probsets/ps{number:02d}-grs18.pdf"
        source_family = "mit-8.962"
        institution = "Alan Guth, Massachusetts Institute of Technology"
        kind = "problem-set"
        locator = f"Physics 8.962, Spring 2018, Problem Set {number}"
    elif group == "mcgreevy-225a":
        number = int(re.search(r"pset(\d+)", name).group(1))
        year = 2013
        course = "Physics 225A General Relativity"
        document_id = f"mcgreevy-225a-2013-ps{number:02d}"
        url = f"https://mcgreevy.physics.ucsd.edu/f13/225A-pset{number:02d}.pdf"
        source_family = "mcgreevy"
        institution = "John McGreevy, University of California San Diego"
        kind = "problem-set"
        locator = f"Physics 225A, Fall 2013, Assignment {number}"
    elif group == "cambridge-example-sheets":
        if name not in CENTRAL_EXAMPLES:
            raise ValueError(f"Unknown Cambridge example-sheet code: {name}")
        course, year = CENTRAL_EXAMPLES[name]
        document_id = f"cambridge-partiii-{slug(course)}-{year}-{name.lower()}"
        url = f"https://www.damtp.cam.ac.uk/user/examples/{name}.pdf"
        source_family = "cambridge-part-iii"
        institution = "University of Cambridge"
        kind = "example-sheet"
        locator = f"Part III {course}, sheet code {name}"
    elif group == "cambridge-special-sheets":
        match = re.search(r"(\d+)$", name)
        if match is None:
            raise ValueError(f"Cannot identify sheet number from {name}")
        sheet = int(match.group(1))
        year = 2026
        source_family = "cambridge-part-iii"
        institution = "University of Cambridge"
        kind = "example-sheet"
        if name.startswith("field-theory"):
            course = "Field Theory in Cosmology"
            document_id = f"cambridge-partiii-ftc-2026-sheet{sheet}"
            url = (
                "https://www.damtp.cam.ac.uk/user/ep551/"
                f"example_sheet_{sheet}_FT_in_Cosmo.pdf"
            )
        else:
            course = "Gravitational Waves and Numerical Relativity"
            document_id = f"cambridge-partiii-gwnr-2026-sheet{sheet}"
            url = (
                "https://www.damtp.cam.ac.uk/user/us248/Lectures/"
                f"Examples/GWNR/exgwnr{sheet}.pdf"
            )
        locator = f"Part III {course}, Example Sheet {sheet}"
    else:
        raise ValueError(f"Unknown source-cache group: {group}")

    return {
        "document_id": document_id,
        "source_family": source_family,
        "institution_or_author": institution,
        "course": course,
        "year": year,
        "kind": kind,
        "document_locator": locator,
        "stable_url": url,
        "local_pdf": relative,
        "local_text": text_path.relative_to(ROOT).as_posix(),
        "source_sha256": sha256(pdf),
        "text_sha256": sha256(text_path),
        "pdf_pages": pdf_pages(pdf),
        "ancillary": ancillary,
    }


def generate() -> dict[str, object]:
    pdfs = sorted(CACHE.glob("*/*.pdf"))
    documents = [record_for(pdf) for pdf in pdfs]
    ids = [str(record["document_id"]) for record in documents]
    duplicate_ids = sorted(key for key, count in Counter(ids).items() if count > 1)
    if duplicate_ids:
        raise ValueError(f"Duplicate document ids: {duplicate_ids}")
    return {
        "schema_version": 1,
        "scope": (
            "Public author- or institution-posted graduate relativity, gravitation, "
            "cosmology, black-hole, gravitational-wave, and stellar-astrophysics "
            "problem sources inspected for the Weinberg GR exercise edition."
        ),
        "documents": documents,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    try:
        generated = generate()
    except (OSError, ValueError, subprocess.CalledProcessError) as error:
        print(f"Source corpus error: {error}", file=sys.stderr)
        return 1
    rendered = json.dumps(generated, indent=2, ensure_ascii=True) + "\n"
    if args.write:
        MANIFEST.write_text(rendered, encoding="utf-8")
        print(f"Wrote {MANIFEST} with {len(generated['documents'])} documents.")
        return 0
    if not MANIFEST.is_file():
        print(f"Missing source corpus manifest: {MANIFEST}", file=sys.stderr)
        return 1
    if MANIFEST.read_text(encoding="utf-8") != rendered:
        print("Source corpus manifest is stale or the cached corpus changed.", file=sys.stderr)
        return 1
    documents = generated["documents"]
    families = Counter(item["source_family"] for item in documents)
    print(
        "Source corpus: "
        f"{len(documents)} hashed documents; "
        + ", ".join(f"{family}={count}" for family, count in sorted(families.items()))
        + "."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
