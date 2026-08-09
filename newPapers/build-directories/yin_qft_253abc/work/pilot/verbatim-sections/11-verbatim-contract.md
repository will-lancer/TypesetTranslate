# Near-verbatim transcript contract

## Frozen source

This contract applies to `work/pilot/transcript.cleaned.jsonl` with SHA-256
`5ac8ac5fb25a3235d8fa11b2b6be99b5f2bb9329d307c4045629544f4e43e9bd`.
Intervals use `[start,end)`.

The printed transcript scope is:

- core lecture: `00:05:02.580` through `01:19:47.090`;
- clear closing Q&A: `01:19:47.100` through `01:20:13.920`;
- one boundary-token exception: `T000317` contributes only `thing`, whose VTT onset is exactly `01:20:13.920` and which completes `T000316`.

The optional lead-in, earlier course administration, weak-room tail, candidate
post-class exchange, and outside-section tail sit outside the printed scope.

## Lexical baseline

A lexical word is a whitespace-independent alphanumeric token after lowercasing,
Unicode accent folding, and punctuation removal. Contractions remain single
tokens. Mathematics inside `$...$` or `\(...\)` is excluded from the lexical
denominator and passes through the formula gate below. Square-bracketed speaker
labels, uncertainty spans, sense glosses, and omission markers are also excluded.
For lexical comparison, TeX `U^{-1}` and canonical Unicode `U⁻¹` both
normalize to the token `u1`.

Two record-specific masks apply:

- `T000149`: the uncertain student prompt is excluded; counting begins after
  `[Yin:]`.
- `T000314`: the student sense gloss is excluded; only `For now, yes` contributes
  eligible lexical words.

The frozen pool contains 198 linked records and 6,542 eligible lexical words:

| Portion | Records | Eligible lexical words |
|---|---:|---:|
| Core | 194 | 6,493 |
| Clear Q&A | 3 | 48 |
| `T000317` boundary token | 1 | 1 |
| Total | 198 | 6,542 |

The final chapter-use labels classify 173 records as `included` and 24 as
`included_clear_portion_uncertainty_excluded`; `T000317` supplies the boundary
word. The 24 secure-portion records are `T000054`, `T000056`, `T000057`,
`T000059`, `T000077`, `T000119`, `T000121`, `T000127`, `T000135`, `T000141`,
`T000145`, `T000149`, `T000153`, `T000161`, `T000170`, `T000210`, `T000218`,
`T000225`, `T000232`, `T000253`, `T000257`, `T000267`, `T000272`, and
`T000314`. The uncertainty mask applies to bracketed spans in either chapter-use
class. Sixty-four eligible records contain mathematics that requires a
formula-source link.

All identifiers below carry the prefix `YIN-OY-`. The number in parentheses is
the eligible lexical-word count after the masks above.

- `00:05–00:15` (33 records, 963 words):
  `T000016`(12), `T000017`(18), `T000018`(41), `T000019`(37), `T000020`(16), `T000021`(22), `T000022`(53), `T000023`(18), `T000024`(34), `T000025`(38), `T000026`(23), `T000028`(24),
  `T000029`(19), `T000030`(35), `T000031`(7), `T000032`(34), `T000033`(13), `T000034`(7), `T000035`(51), `T000036`(18), `T000037`(35), `T000038`(19), `T000040`(40), `T000041`(22),
  `T000042`(27), `T000043`(35), `T000044`(89), `T000046`(41), `T000047`(24), `T000048`(36), `T000049`(23), `T000050`(24), `T000051`(28).
- `00:15–00:25` (28 records, 948 words):
  `T000053`(36), `T000054`(29), `T000055`(50), `T000056`(15), `T000057`(39), `T000058`(37), `T000059`(14), `T000061`(46), `T000064`(21), `T000065`(28), `T000066`(50), `T000067`(7),
  `T000068`(35), `T000069`(35), `T000070`(54), `T000071`(25), `T000072`(55), `T000073`(36), `T000074`(54), `T000075`(32), `T000076`(50), `T000077`(42), `T000078`(34), `T000079`(17),
  `T000080`(29), `T000081`(39), `T000082`(21), `T000083`(18).
- `00:25–00:35` (25 records, 950 words):
  `T000084`(4), `T000085`(62), `T000086`(42), `T000087`(36), `T000088`(14), `T000089`(28), `T000091`(21), `T000094`(24), `T000095`(54), `T000096`(15), `T000097`(42), `T000098`(46),
  `T000099`(32), `T000100`(58), `T000101`(35), `T000102`(55), `T000103`(31), `T000104`(35), `T000105`(43), `T000107`(39), `T000108`(57), `T000109`(24), `T000110`(35), `T000111`(72),
  `T000113`(46).
- `00:35–00:45` (22 records, 902 words):
  `T000117`(36), `T000119`(40), `T000121`(4), `T000123`(67), `T000125`(43), `T000127`(25), `T000129`(42), `T000131`(18), `T000133`(49), `T000135`(33), `T000137`(37), `T000139`(30),
  `T000141`(45), `T000143`(50), `T000145`(40), `T000149`(39), `T000151`(73), `T000153`(64), `T000157`(43), `T000159`(20), `T000161`(31), `T000165`(73).
- `00:45–00:55` (18 records, 953 words):
  `T000170`(21), `T000174`(59), `T000176`(48), `T000178`(87), `T000180`(11), `T000182`(50), `T000185`(98), `T000187`(51), `T000189`(64), `T000191`(79), `T000193`(16), `T000195`(75),
  `T000197`(74), `T000199`(60), `T000200`(52), `T000204`(26), `T000206`(25), `T000208`(57).
- `00:55–01:05` (26 records, 783 words):
  `T000209`(31), `T000210`(20), `T000211`(32), `T000212`(25), `T000214`(26), `T000215`(42), `T000216`(39), `T000217`(11), `T000218`(37), `T000219`(11), `T000220`(26), `T000221`(7),
  `T000222`(40), `T000223`(21), `T000224`(28), `T000225`(60), `T000227`(36), `T000228`(45), `T000229`(25), `T000230`(17), `T000231`(36), `T000232`(16), `T000234`(35), `T000235`(40),
  `T000236`(37), `T000237`(40).
- `01:05–01:15` (26 records, 504 words):
  `T000243`(13), `T000244`(14), `T000247`(6), `T000248`(21), `T000249`(11), `T000250`(12), `T000251`(45), `T000253`(19), `T000254`(21), `T000256`(33), `T000257`(20), `T000262`(35),
  `T000263`(18), `T000264`(27), `T000265`(15), `T000266`(7), `T000267`(27), `T000268`(6), `T000269`(21), `T000270`(15), `T000272`(39), `T000273`(2), `T000274`(37), `T000275`(13),
  `T000276`(15), `T000277`(12).
- `01:15–01:20` (20 records, 539 words):
  `T000279`(38), `T000281`(51), `T000283`(44), `T000285`(28), `T000287`(11), `T000289`(17), `T000291`(25), `T000293`(14), `T000295`(27), `T000297`(4), `T000299`(17), `T000301`(35),
  `T000303`(39), `T000306`(46), `T000308`(48), `T000310`(46), `T000312`(8), `T000314`(3), `T000316`(37), `T000317`(1).

## Excluded records

Within the core and clear-Q&A intervals, 103 records are excluded. Their
canonical `cleaned_word_count` fields sum to 417 before this contract's math and
uncertainty masks. Every excluded record still requires an omission-ledger
entry. Zero-word coverage and silence records remain listed because they prove
complete interval disposition.

| Final disposition | Records | Cleaned words | Record IDs, prefix `YIN-OY-` |
|---|---:|---:|---|
| `board_writing_silence` | 1 | 0 | `T000213` |
| `classroom_logistics` | 3 | 0 | `T000255`, `T000261`, `T000271` |
| `classroom_q_and_a` | 2 | 6 | `T000147`, `T000155` |
| `classroom_question_pause` | 2 | 8 | `T000168`, `T000202` |
| `classroom_question_transition` | 3 | 25 | `T000090`, `T000093`, `T000106` |
| `course_order_q_and_a_unresolved` | 1 | 39 | `T000092` |
| `included_question_management` | 1 | 11 | `T000241` |
| `included_then_question_pause` | 1 | 6 | `T000226` |
| `included_transition` | 1 | 21 | `T000233` |
| `included_transition_with_uncertain_word` | 1 | 13 | `T000184` |
| `included_with_unresolved_audio` | 2 | 49 | `T000240`, `T000258` |
| `logistics` | 2 | 30 | `T000027`, `T000045` |
| `repetition` | 1 | 15 | `T000039` |
| `repetition_or_question` | 1 | 17 | `T000063` |
| `rolling_caption_carryover` | 1 | 0 | `T000278` |
| `rolling_caption_separator_no_new_tokens` | 51 | 0 | `T000052`, `T000116`, `T000118`, `T000122`, `T000126`, `T000128`, `T000136`, `T000138`, `T000140`, `T000142`, `T000144`, `T000146`, `T000150`, `T000154`, `T000156`, `T000158`, `T000160`, `T000162`, `T000164`, `T000167`, `T000169`, `T000171`, `T000173`, `T000175`, `T000177`, `T000179`, `T000181`, `T000183`, `T000186`, `T000188`, `T000190`, `T000192`, `T000194`, `T000196`, `T000198`, `T000201`, `T000203`, `T000205`, `T000207`, `T000280`, `T000282`, `T000284`, `T000294`, `T000296`, `T000300`, `T000302`, `T000304`, `T000307`, `T000309`, `T000313`, `T000315` |
| `rolling_caption_tail_no_new_speech` | 1 | 0 | `T000166` |
| `source_conflict_audio_review` | 2 | 71 | `T000060`, `T000062` |
| `spurious_nonspeech_caption` | 1 | 0 | `T000172` |
| `student_question_unresolved` | 2 | 22 | `T000242`, `T000259` |
| `uncaptioned_interval_unresolved` | 7 | 0 | `T000120`, `T000124`, `T000130`, `T000132`, `T000134`, `T000148`, `T000152` |
| `unresolved` | 2 | 10 | `T000115`, `T000163` |
| `unresolved_audio` | 4 | 41 | `T000239`, `T000245`, `T000246`, `T000252` |
| `unresolved_boundary_fragment` | 1 | 6 | `T000114` |
| `unresolved_boundary_qa` | 1 | 20 | `T000238` |
| `unresolved_student_question` | 1 | 7 | `T000112` |
| `unresolved_weak_room_audio` | 1 | 0 | `T000260` |
| `writing_pause` | 6 | 0 | `T000286`, `T000288`, `T000290`, `T000292`, `T000298`, `T000305` |

The record `T000314` remains eligible only for the secure reply `For now, yes`.
Its student-question sense gloss is an omission. The record `T000149` excludes
the uncertain student prompt. All other square-bracketed uncertain spans are
omissions even when their surrounding record is eligible.

## Printed-text contract

The printed result follows the cleaned speech closely. These transformations are
allowed:

1. Change punctuation, capitalization, quotation marks, apostrophe style,
   paragraph boundaries, and speaker-label typography.
2. Join adjacent records, including recorded continuation links, while retaining
   the eligible word order. A source marker may sit between two words without
   forcing a printed break.
3. Replace an uncertain span with one of the audit's short bracketed markers,
   such as `[inaudible]`, `[question partly inaudible]`, or `[unclear formula]`.
   The complete accepted marker vocabulary appears in the audit constants.
4. Omit records listed in the exclusion table and log each omission.
5. Typeset spoken mathematics from the note layer or a clear frame. Follow an
   explicit `EQUATION_NORMALIZED`, `SOURCE_COMPOSITE`, or `SOURCE_CONFLICT`
   authority when the canonical record records one.
6. Apply TeX typography that leaves the lexical wording unchanged, including
   accent commands, nonbreaking spaces, and display environments.

Reject synonym substitution, summary prose, compressed explanations, reordered
clauses, silent removal of discourse content, newly supplied transitions, and
unlabeled reconstructions. Isolated fillers and false starts have already been
handled in the canonical cleaned transcript. A second editorial cleaning pass
falls outside this contract.

The following acceptance gates all apply:

- The canonical SHA matches the frozen hash above.
- Every one of the 198 eligible records has exactly one source-linked printed
  block, and those blocks occur in transcript order.
- Every one of the 103 excluded scope records has a `record_exclusion` entry.
- Every excluded bracketed uncertainty or sense span has a `span_omission`
  entry. Any eligible lexical-word loss has one as well.
- At least 95 percent of the 6,542 eligible lexical words are represented in
  source order. This requires at least 6,215 represented words.
- Each eligible record represents at least 80 percent of its eligible words,
  rounded up, and at least one word. The one-word boundary record therefore
  requires `thing`.
- Every lexical word inside a source-linked printed block aligns to that record
  in source order. Editorial prose belongs outside the source block.
- The student sense gloss in `T000314`, all bracketed uncertain reconstructions,
  and all unresolved-audio records contribute no invented dialogue.
- Every one of the 64 formula-bearing eligible records has a formula-ledger
  entry tied to note pages, PDF pages, and an allowed source class.
- Mathematical review confirms the formulas independently of lexical recall.

## Required source markers and sidecars

Wrap each eligible source contribution in the chapter TeX with comments:

```tex
% YIN-VERBATIM-BEGIN YIN-OY-T000016
What is quantum field theory? This question is very easy to answer.
% YIN-VERBATIM-END YIN-OY-T000016
```

Comments permit consecutive records to form one printed paragraph. Each eligible
ID appears in one begin/end pair.

Use `work/pilot/verbatim-omissions.jsonl` with either of these forms:

```json
{"record_type":"record_exclusion","transcript_record_id":"YIN-OY-T000027","reason_code":"classroom_management","detail":"Question-management interval omitted from printed exposition."}
{"record_type":"span_omission","transcript_record_id":"YIN-OY-T000054","scope":"prebaseline_uncertainty","omitted_text":"[inaudible]","reason_code":"inaudible_or_uncertain","detail":"Unknown theory name replaced by an inaudible marker."}
```

Use one `span_omission` row per distinct omitted span. When identical markers
recur in one record, add a one-based `occurrence` field. The `detail` field must
state whether the loss precedes the lexical baseline or removes eligible words.
Use `scope=prebaseline_uncertainty` for the former and
`scope=eligible_lexical_loss` for the latter.

Use `work/pilot/verbatim-formulas.jsonl` for all 64 formula-bearing eligible
records:

```json
{"transcript_record_id":"YIN-OY-T000297","source_class":"EQUATION_NORMALIZED","note_pages":[7,8],"pdf_pages":[12,13],"printed_formula_ids":["YIN253A-C01-N07-EQ-PHI"],"review_status":"math_reviewed"}
```

Each formula row uses the canonical record's note pages and their PDF `n+5`
counterparts. Local authority labels `NOTES_EXACT_AND_FRAME` and
`NOTES_EXACT_FOR_SYMBOLS` map to the allowed ledger class `NOTES_EXACT`. Other
explicit canonical formula-authority classes carry over unchanged. Every
printed formula ID is unique.

Allowed formula source classes are `NOTES_EXACT`, `SPEECH_CLEAN`,
`SOURCE_COMPOSITE`, `EQUATION_NORMALIZED`, `EDITORIAL_NOTE`, and
`SOURCE_CONFLICT`. Caption text alone cannot authorize an equation.

## Read-only lexical audit

Run this from the build-directory root after creating the marked chapter and the
two sidecars. It reads the canonical files and exits nonzero on hash drift,
missing links, unlisted omissions, compression, or paraphrase-like token drift.
It writes nothing.

```sh
python3 - \
  work/pilot/transcript.cleaned.jsonl \
  work/pilot/transcript-dispositions.jsonl \
  latex/chapters/253a/chapter01.tex \
  work/pilot/verbatim-omissions.jsonl \
  work/pilot/verbatim-formulas.jsonl <<'PY'
from pathlib import Path
from collections import Counter
import hashlib, json, math, re, sys, unicodedata

TRANSCRIPT, DISPOSITIONS, TEX, OMISSIONS, FORMULAS = map(Path, sys.argv[1:])
FROZEN_SHA = "5ac8ac5fb25a3235d8fa11b2b6be99b5f2bb9329d307c4045629544f4e43e9bd"
ALLOWED_FORMULA_CLASSES = {
    "NOTES_EXACT", "SPEECH_CLEAN", "SOURCE_COMPOSITE",
    "EQUATION_NORMALIZED", "EDITORIAL_NOTE", "SOURCE_CONFLICT",
}
SPEAKER_LABELS = {"Yin:", "Student:", "Audience:", "Question:", "Q:", "A:"}
ALLOWED_BRACKET_MARKERS = {
    "inaudible", "unclear", "question partly inaudible",
    "student question partly inaudible", "partly inaudible question",
    "unclear formula", "unclear word", "unclear phrase",
    "inaudible word", "inaudible phrase", "inaudible speech",
    "speaker unclear",
}

def load_jsonl(path):
    return [json.loads(line) for line in path.read_text().splitlines() if line.strip()]

def millis(value):
    hour, minute, second = value.split(":")
    whole, fraction = second.split(".")
    return ((int(hour) * 60 + int(minute)) * 60 + int(whole)) * 1000 + int(fraction)

def in_scope(record):
    start, end = millis(record["start"]), millis(record["end"])
    core = start >= 302_580 and end <= 4_787_090
    clear_qa = start >= 4_787_100 and end <= 4_813_920
    return core or clear_qa

def strip_math(text):
    text = re.sub(r"\\begin\{(?:equation\*?|align\*?|gather\*?|multline\*?)\}.*?"
                  r"\\end\{(?:equation\*?|align\*?|gather\*?|multline\*?)\}",
                  " ", text, flags=re.S)
    text = re.sub(r"\\\[.*?\\\]", " ", text, flags=re.S)
    text = re.sub(r"\\\(.*?\\\)", " ", text, flags=re.S)
    text = re.sub(r"\$\$.*?\$\$", " ", text, flags=re.S)
    return re.sub(r"\$[^$]*\$", " ", text, flags=re.S)

def secure_text(record):
    text = record.get("cleaned_text") or ""
    if record["id"] == "YIN-OY-T000149" and "[Yin:]" in text:
        text = text.split("[Yin:]", 1)[1]
    elif record["id"] == "YIN-OY-T000314":
        text = "For now, yes."
    elif record["id"] == "YIN-OY-T000317":
        text = "thing."
    text = strip_math(text)
    return re.sub(r"\[[^\]]*\]", " ", text)

def tex_to_text(text):
    text = re.sub(r"(?m)%.*$", " ", text)
    text = strip_math(text)
    text = re.sub(r"([A-Za-z])\s*\^\s*\{\s*-\s*1\s*\}", r"\g<1>1", text)
    text = re.sub(r"\\['\"`^~=.uvHckbdtr]\s*\{?([A-Za-z])\}?", r"\1", text)
    text = re.sub(r"\\(?:textit|emph|textbf|textrm|textsf|texttt)\s*\{([^{}]*)\}", r"\1", text)
    text = re.sub(r"\\[A-Za-z@]+\*?(?:\[[^\]]*\])?", " ", text)
    text = text.replace("{", "").replace("}", "").replace("~", " ")
    text = re.sub(
        r"(?im)^\s*(?:Yin|Student|Audience|Question|Q|A)\s*:\s*", " ", text
    )
    return re.sub(r"\[[^\]]*\]", " ", text)

def tokens(text):
    text = text.lower().replace("’", "'").replace("‘", "'")
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    return re.findall(r"[a-z0-9]+(?:'[a-z0-9]+)?", text)

def lcs_length(left, right):
    row = [0] * (len(right) + 1)
    for a in left:
        previous = 0
        for index, b in enumerate(right, 1):
            saved = row[index]
            if a == b:
                row[index] = previous + 1
            elif row[index - 1] > row[index]:
                row[index] = row[index - 1]
            previous = saved
    return row[-1]

digest = hashlib.sha256(TRANSCRIPT.read_bytes()).hexdigest()
assert digest == FROZEN_SHA, f"transcript drift: {digest}"
objects = load_jsonl(TRANSCRIPT)
records = [item for item in objects if item.get("record_type") != "transcript_metadata"]
by_id = {item["id"]: item for item in records}
assert len(by_id) == len(records)

dispositions = load_jsonl(DISPOSITIONS)
assert all(item.get("transcript_sha256") == FROZEN_SHA for item in dispositions)
use = {item["transcript_record_id"]: item["chapter_use"] for item in dispositions}
eligible = {
    item["id"] for item in records
    if in_scope(item) and use.get(item["id"]) in {
        "included", "included_clear_portion_uncertainty_excluded"
    }
}
eligible.add("YIN-OY-T000317")
excluded = {item["id"] for item in records if in_scope(item)} - eligible
assert len(eligible) == 198, len(eligible)
assert len(excluded) == 103, len(excluded)

source_tokens = {rid: tokens(secure_text(by_id[rid])) for rid in eligible}
assert sum(map(len, source_tokens.values())) == 6_542

tex = TEX.read_text()
begin_ids = re.findall(
    r"(?m)^%\s*YIN-VERBATIM-BEGIN\s+(YIN-OY-T\d{6}[AB]?)\s*$", tex
)
end_ids = re.findall(
    r"(?m)^%\s*YIN-VERBATIM-END\s+(YIN-OY-T\d{6}[AB]?)\s*$", tex
)
assert Counter(begin_ids) == Counter(end_ids)
assert begin_ids == end_ids
assert len(begin_ids) == len(set(begin_ids)) == 198
ordered_eligible = sorted(eligible, key=lambda rid: millis(by_id[rid]["start"]))
assert begin_ids == ordered_eligible, "source blocks are not in transcript order"
block_re = re.compile(
    r"(?ms)^%\s*YIN-VERBATIM-BEGIN\s+(YIN-OY-T\d{6}[AB]?)\s*$\n"
    r"(.*?)^%\s*YIN-VERBATIM-END\s+\1\s*$"
)
blocks = {}
for match in block_re.finditer(tex):
    rid = match.group(1)
    assert rid not in blocks, f"duplicate source block: {rid}"
    blocks[rid] = match.group(2)
assert set(blocks) == eligible, (
    f"missing blocks={sorted(eligible-set(blocks))}; "
    f"extra blocks={sorted(set(blocks)-eligible)}"
)
for rid, block in blocks.items():
    prose = strip_math(block)
    for marker in re.findall(r"\[([^\]]*)\]", prose):
        normalized = " ".join(marker.lower().split())
        assert marker.strip() in SPEAKER_LABELS or normalized in ALLOWED_BRACKET_MARKERS, (
            rid, "unapproved bracketed reconstruction", marker
        )

omission_rows = load_jsonl(OMISSIONS)
record_exclusion_rows = [
    item for item in omission_rows
    if item.get("record_type") == "record_exclusion"
]
record_exclusions = {item["transcript_record_id"] for item in record_exclusion_rows}
assert len(record_exclusion_rows) == len(record_exclusions) == 103
assert record_exclusions == excluded, (
    f"missing exclusions={sorted(excluded-record_exclusions)}; "
    f"extra exclusions={sorted(record_exclusions-excluded)}"
)
span_omission_rows = [
    item for item in omission_rows
    if item.get("record_type") == "span_omission"
]
assert all(
    item.get("scope") in {"prebaseline_uncertainty", "eligible_lexical_loss"}
    and item.get("omitted_text") and item.get("reason_code") and item.get("detail")
    for item in span_omission_rows
)
prebaseline_rows = {
    item["transcript_record_id"] for item in span_omission_rows
    if item["scope"] == "prebaseline_uncertainty"
}
lexical_loss_rows = {
    item["transcript_record_id"] for item in span_omission_rows
    if item["scope"] == "eligible_lexical_loss"
}
prebaseline_omissions = {"YIN-OY-T000149", "YIN-OY-T000314"}
for rid in eligible:
    prose = strip_math(by_id[rid].get("cleaned_text") or "")
    spans = [value.strip() for value in re.findall(r"\[([^\]]*)\]", prose)]
    if any(value not in SPEAKER_LABELS for value in spans):
        prebaseline_omissions.add(rid)
assert prebaseline_omissions <= prebaseline_rows, (
    "missing prebaseline omissions", sorted(prebaseline_omissions - prebaseline_rows)
)

represented = 0
failures = []
for rid in sorted(eligible, key=lambda value: millis(by_id[value]["start"])):
    source = source_tokens[rid]
    printed = tokens(tex_to_text(blocks[rid]))
    common = lcs_length(source, printed)
    represented += common
    recall = common / len(source)
    precision = common / len(printed) if printed else 0.0
    required = max(1, math.ceil(0.80 * len(source)))
    if common < required or common != len(printed):
        failures.append((rid, len(source), len(printed), common, recall, precision))
    if common < len(source) and rid not in lexical_loss_rows:
        failures.append((rid, "unlisted span omission"))

global_recall = represented / 6_542
assert represented >= 6_215 and global_recall >= 0.95, (
    represented, global_recall
)
assert not failures, failures

formula_rows = load_jsonl(FORMULAS)
formula_by_record = {item["transcript_record_id"]: item for item in formula_rows}
formula_records = {
    rid for rid in eligible
    if re.search(r"\$|\\\(", by_id[rid].get("cleaned_text") or "")
}
assert len(formula_records) == 64, len(formula_records)
assert len(formula_rows) == len(formula_by_record) == 64
assert set(formula_by_record) == formula_records
for rid, item in formula_by_record.items():
    assert item.get("source_class") in ALLOWED_FORMULA_CLASSES, (rid, item)
    assert item.get("note_pages") and item.get("pdf_pages"), (rid, item)
    record = by_id[rid]
    assert set(item["note_pages"]) <= set(record.get("note_pages") or []), (rid, item)
    assert set(item["pdf_pages"]) == {page + 5 for page in item["note_pages"]}, (rid, item)
    authority = record.get("formula_authority") or {}
    canonical_class = authority.get("class")
    if canonical_class in {"NOTES_EXACT_AND_FRAME", "NOTES_EXACT_FOR_SYMBOLS"}:
        canonical_class = "NOTES_EXACT"
    if canonical_class:
        assert item["source_class"] == canonical_class, (rid, canonical_class, item)
    assert item.get("printed_formula_ids"), (rid, item)
    assert item.get("review_status") == "math_reviewed", (rid, item)
formula_ids = [
    formula_id
    for item in formula_rows
    for formula_id in item["printed_formula_ids"]
]
assert len(formula_ids) == len(set(formula_ids)), "duplicate printed formula ID"

print(json.dumps({
    "transcript_sha256": digest,
    "eligible_records": len(eligible),
    "excluded_scope_records": len(excluded),
    "eligible_lexical_words": 6_542,
    "represented_words": represented,
    "global_recall": round(global_recall, 6),
    "formula_records": len(formula_records),
    "status": "PASS",
}, indent=2))
PY
```

The lexical audit measures fidelity to cleaned speech. The formula ledger and
mathematical review establish equation fidelity. Both gates must pass.
