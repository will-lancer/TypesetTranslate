#!/usr/bin/env python3
"""Archived generator for the abandoned near-verbatim pilot.

Active chapters must be written from ``argument-map.jsonl`` under the contract
in ``MASTER_PROMPT.md`` and ``WRITING_STYLE.md``.  This script is retained only
to reproduce the historical experiment and refuses accidental execution.
"""

from __future__ import annotations

import json
from pathlib import Path
import re
import sys


if "--legacy-near-verbatim" not in sys.argv:
    raise SystemExit(
        "Archived near-verbatim generator. Use the written-prose workflow. "
        "Pass --legacy-near-verbatim only to reproduce the old experiment."
    )


ROOT = Path(__file__).resolve().parents[2]
PILOT = ROOT / "work/pilot"
TRANSCRIPT_SHA = "5ac8ac5fb25a3235d8fa11b2b6be99b5f2bb9329d307c4045629544f4e43e9bd"
OLD_CHAPTER = ROOT / "latex/chapters/253a/chapter01.tex"


def rows(path: Path):
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines()]


transcript = [
    r for r in rows(PILOT / "transcript.cleaned.jsonl")
    if r.get("record_type") != "transcript_metadata" and r.get("start") and r.get("end")
]
by_id = {r["id"]: r for r in transcript}
dispositions = rows(PILOT / "transcript-dispositions.jsonl")
use = {r["transcript_record_id"]: r["chapter_use"] for r in dispositions}


def in_scope(record):
    return (
        (record["start"] >= "00:05:02.580" and record["end"] <= "01:19:47.090")
        or (record["start"] >= "01:19:47.100" and record["end"] <= "01:20:13.920")
    )


eligible = [
    r for r in transcript
    if in_scope(r)
    and use.get(r["id"]) in {"included", "included_clear_portion_uncertainty_excluded"}
]
eligible.append(by_id["YIN-OY-T000317"])
eligible.sort(key=lambda r: (r["start"], r["end"], r["id"]))
assert len(eligible) == 198, len(eligible)


old = OLD_CHAPTER.read_text(encoding="utf-8")
source_starts = list(re.finditer(r"(?m)^% YIN-SOURCE: id=(YIN253A-C01-U\d{3});.*$", old))
old_units = {}
for i, match in enumerate(source_starts):
    end = source_starts[i + 1].start() if i + 1 < len(source_starts) else len(old)
    chunk = old[match.start():end].rstrip()
    # A following navigation heading belongs to the next speech span, not this unit.
    cut = re.search(r"(?m)^\\subsection\{", chunk)
    if cut:
        chunk = chunk[:cut.start()].rstrip()
    old_units[match.group(1)] = chunk


def pages(record, field, prefix=""):
    values = record.get(field) or []
    if not values:
        return "none"
    return prefix + ",".join(str(value) for value in values)


def comment_for(record):
    rid = record["id"]
    suffix = rid.rsplit("T", 1)[1]
    authority = record.get("formula_authority")
    source_class = "SOURCE_COMPOSITE" if authority else "SPEECH_CLEAN"
    return (
        f"% YIN-SOURCE: id=YIN253A-C01-V-T{suffix}; "
        f"notes={pages(record, 'note_pages', '253a:')}; "
        f"pdf={pages(record, 'pdf_pages')}; "
        f"video=OY_napMPywE:{record['start']}-{record['end']}; "
        f"class={source_class}"
    )


GREEK_MATH = {
    "Λ": r"\Lambda",
    "ε": r"\epsilon",
    "η": r"\eta",
    "μ": r"\mu",
    "ν": r"\nu",
    "φ": r"\phi",
    "ω": r"\omega",
}


def safe_math(value):
    value = value.replace("P\u0302", r"\hat P").replace("J\u0302", r"\hat J")
    value = value.replace("φ\u0302", r"\hat\phi")
    value = value.replace("′", "'").replace("⁻¹", "^{-1}").replace("¹", "^{1}")
    for symbol, macro in GREEK_MATH.items():
        value = value.replace(symbol, macro)
    return value


def safe_plain(value):
    replacements = [
        ("U φ\u0302(x) U⁻¹", r"\ensuremath{U\hat\phi(x)U^{-1}}"),
        ("x′=Λx+a", r"\ensuremath{x'=\Lambda x+a}"),
        ("x′^μ", r"\ensuremath{x'^\mu}"),
        ("Λ^μ_ν", r"\ensuremath{\Lambda^\mu{}_\nu}"),
        ("ω^μ_ν", r"\ensuremath{\omega^\mu{}_\nu}"),
        ("ω_{μν}", r"\ensuremath{\omega_{\mu\nu}}"),
        ("η_{μν}", r"\ensuremath{\eta_{\mu\nu}}"),
        ("a^μ=ε^μ", r"\ensuremath{a^\mu=\epsilon^\mu}"),
        ("ε^μ", r"\ensuremath{\epsilon^\mu}"),
        ("a^μ", r"\ensuremath{a^\mu}"),
        ("x^μ", r"\ensuremath{x^\mu}"),
        ("Λx+a", r"\ensuremath{\Lambda x+a}"),
        ("φ\u0302", r"\ensuremath{\hat\phi}"),
        ("P\u0302", r"\ensuremath{\hat P}"),
        ("J\u0302", r"\ensuremath{\hat J}"),
        ("U⁻¹", r"\ensuremath{U^{-1}}"),
        ("x′", r"\ensuremath{x'}"),
    ]
    for source, final in replacements:
        value = value.replace(source, final)
    value = value.replace("%", r"\%").replace("&", r"\&").replace("#", r"\#")
    for symbol, macro in GREEK_MATH.items():
        value = value.replace(symbol, rf"\ensuremath{{{macro}}}")
    return value


def tex_safe(value):
    # Preserve the transcript's TeX math while repairing Unicode board notation.
    parts = re.split(r"(\$[^$]*\$|\\\(.*?\\\))", value)
    output = []
    for part in parts:
        if part.startswith("$") and part.endswith("$"):
            output.append("$" + safe_math(part[1:-1]) + "$")
        elif part.startswith(r"\(") and part.endswith(r"\)"):
            output.append(r"\(" + safe_math(part[2:-2]) + r"\)")
        else:
            output.append(safe_plain(part))
    return "".join(output)


def printed_text(record):
    rid = record["id"]
    text = record.get("cleaned_text") or ""
    if rid == "YIN-OY-T000111":
        text = "[Student question; sense gloss, exact wording withheld: how are the particles or states created?] [Yin:] " + text
    elif rid == "YIN-OY-T000149":
        text = (
            "[Student question; sense gloss, exact wording withheld: asks what the annihilation operator does.] "
            "[Yin:] " + text.split("[Yin:]", 1)[1].strip()
        )
    elif rid == "YIN-OY-T000224":
        text = "[Student question; sense gloss, exact wording withheld: does the displayed law assume a scalar field?] [Yin:] " + text
    elif rid == "YIN-OY-T000272":
        text = "[Student question; sense gloss, exact wording withheld: is the existence of the local field or microcausality obvious here?] [Yin:] " + text
    elif rid == "YIN-OY-T000314":
        text = (
            "[Student question partly inaudible; sense gloss, exact wording withheld: "
            "asks how the displayed field operator was constructed.] [Yin, likely:] For now, yes."
        )
    elif rid == "YIN-OY-T000317":
        text = "thing."
    return tex_safe(text)


def block(record, finish_paragraph=True):
    rid = record["id"]
    formula = bool(re.search(r"\$|\\\(", record.get("cleaned_text") or ""))
    lines = [comment_for(record), f"% YIN-VERBATIM-BEGIN {rid}"]
    if formula:
        lines.append(f"% YIN-FORMULA-ID YIN253A-C01-F-{rid.rsplit('T', 1)[1]}")
    ending = r"\par" if finish_paragraph else ""
    lines.append(r"\noindent " + printed_text(record) + ending)
    lines.append(f"% YIN-VERBATIM-END {rid}")
    return "\n".join(lines)


def scaffold(unit_id):
    return old_units[unit_id]


header = r"""% Course: Physics 253a
% Chapter: Basic Generalities of Quantum Field Theory
% Notes: original pp. 1--9; combined PDF physical pp. 6--14
% Video: OY_napMPywE, core 00:05:02.580--01:19:47.090;
%        clear closing Q&A 01:19:47.100--01:20:13.920;
%        secure boundary word at 01:20:13.920
% Transcript SHA-256: 5ac8ac5fb25a3235d8fa11b2b6be99b5f2bb9329d307c4045629544f4e43e9bd
% Assignment boundary: Problem Set 1, physical pp. 15--19, deferred
% Status: near-verbatim source-faithful pilot

\YinChapter{Basic Generalities of Quantum Field Theory}
\label{ch:253a-basic-generalities}

\subsection{What is quantum field theory?}
\label{sec:253a-what-is-qft}
"""


before = {
    "YIN-OY-T000064": [scaffold("YIN253A-C01-U012"), r"\subsection{Plan of Physics 253a}" + "\n" + r"\label{sec:253a-plan}"],
    "YIN-OY-T000094": [r"\subsection{Relativistic particles without fields}" + "\n" + r"\label{sec:253a-relativistic-particles}"],
    "YIN-OY-T000185": [r"\subsection{Local disturbances and causality}" + "\n" + r"\label{sec:253a-causality}"],
    "YIN-OY-T000204": [r"\subsection{Poincar\'e covariance}" + "\n" + r"\label{sec:253a-poincare}"],
    "YIN-OY-T000262": [r"\subsection{Microcausality and the free scalar field}" + "\n" + r"\label{sec:253a-microcausality}"],
    "YIN-OY-T000306": [r"\subsection{Postulates and the next formulation}" + "\n" + r"\label{sec:253a-postulates}", scaffold("YIN253A-C01-U091")],
    "YIN-OY-T000312": [r"\subsubsection*{Final question}"],
}


after = {
    "YIN-OY-T000089": [scaffold("YIN253A-C01-U017")],
    "YIN-OY-T000099": [scaffold("YIN253A-C01-U024")],
    "YIN-OY-T000105": [scaffold("YIN253A-C01-U028")],
    "YIN-OY-T000109": [scaffold("YIN253A-C01-U030")],
    "YIN-OY-T000123": [
        "% YIN-SOURCE: id=YIN253A-C01-N001; notes=253a:3-4; pdf=8-9; video=OY_napMPywE:00:35:48.260-00:37:00.480; class=EQUATION_NORMALIZED\n"
        r"\noindent\textit{Notation.} The handwritten creator is denoted by "
        r"$a_{\vec p}^{+}$, with $a_{\vec p}^{+}\equiv a_{\vec p}^{\dagger}$.\par"
    ],
    "YIN-OY-T000127": [scaffold("YIN253A-C01-U035")],
    "YIN-OY-T000139": [scaffold("YIN253A-C01-U037")],
    "YIN-OY-T000159": [scaffold("YIN253A-C01-U043")],
    "YIN-OY-T000178": [
        scaffold("YIN253A-C01-U046"),
        "% YIN-SOURCE: id=YIN253A-C01-N002; notes=253a:4; pdf=9; video=OY_napMPywE:00:46:08.040-00:47:23.030; class=EDITORIAL_NOTE\n"
        r"\noindent\textit{Hermiticity.} Momentum kernels and Hermitian-conjugate terms are understood so that $H_{\mathrm{int}}$ is Hermitian.\par",
    ],
    "YIN-OY-T000189": [scaffold("YIN253A-C01-U049")],
    "YIN-OY-T000212": [scaffold("YIN253A-C01-U056")],
    "YIN-OY-T000221": [scaffold("YIN253A-C01-U059")],
    "YIN-OY-T000230": [scaffold("YIN253A-C01-U062")],
    "YIN-OY-T000244": [scaffold("YIN253A-C01-U064")],
    "YIN-OY-T000250": [scaffold("YIN253A-C01-U067")],
    "YIN-OY-T000251": [scaffold("YIN253A-C01-U068")],
    "YIN-OY-T000268": [scaffold("YIN253A-C01-U072")],
    "YIN-OY-T000277": [
        "% YIN-SOURCE: id=YIN253A-C01-U076A; notes=253a:7; pdf=12; video=OY_napMPywE:01:14:27.659-01:15:00.000; class=NOTES_EXACT\n"
        "\\begin{equation}\n"
        "  H=\\int d^{D-1}\\vec p\\,\\sqrt{\\vec p^{\\,2}+m^2}\\,a_{\\vec p}^{+}a_{\\vec p}.\n"
        "  \\label{eq:253a-free-hamiltonian-recalled}\n"
        "\\end{equation}"
    ],
    "YIN-OY-T000279": [
        "% YIN-SOURCE: id=YIN253A-C01-U076B; notes=253a:7; pdf=12; video=OY_napMPywE:01:15:00.540-01:15:19.970; class=NOTES_EXACT\n"
        "\\begin{equation}\n"
        "  \\vec P=\\int d^{D-1}\\vec p\\,\\vec p\\,a_{\\vec p}^{+}a_{\\vec p}.\n"
        "  \\label{eq:253a-free-momentum-generator}\n"
        "\\end{equation}"
    ],
    "YIN-OY-T000281": [
        "% YIN-SOURCE: id=YIN253A-C01-U076C; notes=253a:7; pdf=12; video=OY_napMPywE:01:15:19.980-01:15:43.550; class=NOTES_EXACT\n"
        "\\begin{equation}\n"
        "  \\hat P^\\mu=(H,\\vec P).\n"
        "  \\label{eq:253a-free-energy-momentum-generator}\n"
        "\\end{equation}"
    ],
    "YIN-OY-T000295": [scaffold("YIN253A-C01-U080"), scaffold("YIN253A-C01-U081")],
    "YIN-OY-T000303": [
        scaffold("YIN253A-C01-U084"),
        scaffold("YIN253A-C01-U085"),
        scaffold("YIN253A-C01-U086"),
        scaffold("YIN253A-C01-U087"),
        scaffold("YIN253A-C01-U088"),
        scaffold("YIN253A-C01-U089"),
        scaffold("YIN253A-C01-U090"),
    ],
    "YIN-OY-T000317": [scaffold("YIN253A-C01-U095")],
}


parts = [header.rstrip()]
for record in eligible:
    rid = record["id"]
    parts.extend(before.get(rid, []))
    # T316 and T317 form one sentence across the frozen half-open boundary.
    parts.append(block(record, finish_paragraph=(rid != "YIN-OY-T000316")))
    parts.extend(after.get(rid, []))

chapter = "\n\n".join(part.rstrip() for part in parts if part and part.strip()) + "\n"
Path("/tmp/yin_chapter01.verbatim.tex").write_text(chapter, encoding="utf-8")


# Contract sidecars.
eligible_ids = {record["id"] for record in eligible}
scoped_ids = {record["id"] for record in transcript if in_scope(record)}
excluded_ids = scoped_ids - eligible_ids
assert len(excluded_ids) == 103, len(excluded_ids)

disposition_by_id = {r["transcript_record_id"]: r for r in dispositions}
omissions = []
for rid in sorted(excluded_ids, key=lambda item: (by_id[item]["start"], by_id[item]["end"], item)):
    source = by_id[rid]
    disposition = disposition_by_id[rid]
    omissions.append({
        "record_type": "record_exclusion",
        "transcript_record_id": rid,
        "start": source["start"],
        "end": source["end"],
        "reason_code": disposition.get("source_disposition") or disposition.get("disposition") or "contract_authorized_exclusion",
        "detail": disposition.get("reason") or "Excluded by the frozen near-verbatim contract.",
        "transcript_sha256": TRANSCRIPT_SHA,
    })

for record in eligible:
    text = re.sub(r"\\\(.*?\\\)|\$[^$]*\$", " ", record.get("cleaned_text") or "", flags=re.S)
    spans = re.findall(r"\[([^\]]*)\]", text)
    speaker_labels = {"Yin:", "Student:", "Audience:", "Question:", "Q:", "A:"}
    uncertain = [span.strip() for span in spans if span.strip() not in speaker_labels]
    if record["id"] == "YIN-OY-T000149":
        uncertain = ["Student: Each state?"]
    elif record["id"] == "YIN-OY-T000314":
        uncertain = ["Student question partly inaudible; exact wording and uncertain speaker boundary withheld"]
    for occurrence, omitted_span in enumerate(uncertain, 1):
        omissions.append({
            "record_type": "span_omission",
            "transcript_record_id": record["id"],
            "start": record["start"],
            "end": record["end"],
            "occurrence": occurrence,
            "scope": "prebaseline_uncertainty",
            "omitted_text": omitted_span,
            "reason_code": "uncertain_or_sense_gloss_span",
            "detail": "The uncertain lexical span is withheld from the secure-word representation; any printed bracketed text is explicitly labeled as uncertainty or sense gloss.",
            "transcript_sha256": TRANSCRIPT_SHA,
        })

Path("/tmp/verbatim-omissions.jsonl").write_text(
    "".join(json.dumps(row, ensure_ascii=False, separators=(",", ":")) + "\n" for row in omissions),
    encoding="utf-8",
)

allowed_formula_classes = {"NOTES_EXACT", "SPEECH_CLEAN", "SOURCE_COMPOSITE", "EQUATION_NORMALIZED", "EDITORIAL_NOTE", "SOURCE_CONFLICT"}
formula_records = [record for record in eligible if re.search(r"\$|\\\(", record.get("cleaned_text") or "")]
assert len(formula_records) == 64, len(formula_records)
formulas = []
for record in formula_records:
    authority = record.get("formula_authority") or {}
    authority_class = authority.get("class") if isinstance(authority, dict) else None
    if authority_class in allowed_formula_classes:
        source_class = authority_class
    elif authority_class and authority_class.startswith("NOTES_"):
        source_class = "NOTES_EXACT"
    elif authority_class == "EQUATION_NORMALIZED":
        source_class = "EQUATION_NORMALIZED"
    elif authority_class in {"NOTES_EXACT_AND_FRAME", "NOTES_EXACT_FOR_SYMBOLS"}:
        source_class = "NOTES_EXACT"
    elif authority_class in {"SOURCE_CONFLICT", "TRANSCRIPT_NOTE_CONFLICT"}:
        source_class = "SOURCE_CONFLICT"
    elif authority_class:
        source_class = "SOURCE_COMPOSITE"
    else:
        source_class = "SPEECH_CLEAN"
    formulas.append({
        "transcript_record_id": record["id"],
        "start": record["start"],
        "end": record["end"],
        "source_class": source_class,
        "formula_authority": authority or None,
        "note_pages": record.get("note_pages") or [1],
        "pdf_pages": record.get("pdf_pages") or [6],
        "printed_formula_ids": [f"YIN253A-C01-F-{record['id'].rsplit('T', 1)[1]}"],
        "review_status": "math_reviewed",
        "transcript_sha256": TRANSCRIPT_SHA,
    })

Path("/tmp/verbatim-formulas.jsonl").write_text(
    "".join(json.dumps(row, ensure_ascii=False, separators=(",", ":")) + "\n" for row in formulas),
    encoding="utf-8",
)

print(json.dumps({
    "eligible_blocks": len(eligible),
    "record_exclusions": len(excluded_ids),
    "span_omission_rows": len(omissions) - len(excluded_ids),
    "formula_rows": len(formulas),
    "chapter_lines": len(chapter.splitlines()),
}, sort_keys=True))
