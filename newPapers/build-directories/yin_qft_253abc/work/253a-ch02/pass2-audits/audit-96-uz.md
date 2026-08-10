# Pass 2 independent audit: `96lN2omwit4` and `uzixOflp0tY`

## Audit basis

This refresh covers all sixteen current raw lanes and cleaned outputs for
`96lN2omwit4` and `uzixOflp0tY`. I read their video reports, the mapped note
source lanes, `playlist-chronology.md`, `boundary-assignment.md`,
`chapter-metadata.json`, `source-map.md`, the lane manifest, and the merge
contract. The canonical transcript was remerged before this audit with
current SHA-256
`c84a329bba04d3da2f2e5f6911b06919b2e358b0c4653a9a0e0f7e532859f112`.

The frozen intervals are:

- `96lN2omwit4`: `[00:01:26.700,01:20:25.500)`, handwritten notes 10--14,
  physical pages 21--25.
- `uzixOflp0tY`: `[00:02:50.879,01:19:02.520)`, handwritten notes 15--20,
  physical pages 26--31.

## Exact lane coverage

| lane | raw events | segments | non-null/null | source-event span | cue-start scope | raw SHA-256 | cleaned SHA-256 |
|---|---:|---:|---|---|---|---|---|
| `96lN2omwit4-000000-001200` | 191 | 24 | 22/2 | 1--381 | 2 pre, 22 core | `1dc34e6f1b4d14e5ad6d594462f1bb5751b5f168ef498b4621247a67a0c3f6fe` | `79147505267c2925259c395a6019a82997965b6a06c1ed4d8eee876440f5bd7c` |
| `96lN2omwit4-001200-002400` | 266 | 16 | 16/0 | 383--913 | core | `2bb98af4d3e977740f76543584f3911161a4ef87459bfc0a9459b8c1ade4b64f` | `6dd11c509ecff4e2fdd756c219572a58185ce0fbed13d83be0745a4c2f6b0694` |
| `96lN2omwit4-002400-003600` | 199 | 20 | 18/2 | 915--1311 | core | `6cb9c2196495e4e86837283e31015d5073a32c208ab6ab78a401163fa2c3dd61` | `a0dfbe4fa501ff9b90928dfac9f8db5d0350afc4408c16b37f378021f13fe7b0` |
| `96lN2omwit4-003600-004800` | 224 | 21 | 21/0 | 1313--1759 | core | `4683daf8deaf58af618fa7beb8126d28c6a61a3212810b5710756ec863f94bcc` | `3d60b23fd069887cfd0dab6bd2d51e6d3f499d636034dce995a7df76ea434647` |
| `96lN2omwit4-004800-010000` | 276 | 23 | 23/0 | 1761--2311 | core | `54c675d262b76b92006847ef2b90c62017741d18ce1307f642d166ef3b38381b` | `11d3ee9481f2bac98df6534941c3f00adaef32ca9f10145e4e884772dac38afc` |
| `96lN2omwit4-010000-011200` | 231 | 21 | 21/0 | 2313--2773 | core | `92286f06f8078761465175c9a41512056b38799bbbbbae20d79dff846f31146d` | `3eccc239ad73c738b547036057f7ab6a815100ab6f264e61988bfd9eef33485f` |
| `96lN2omwit4-011200-012400` | 179 | 19 | 13/6 | 2775--3131 | 14 core, 5 post | `2a5334e6cdf28ff62442381584fc8d6812686a9233beb4435e02ad8a8ea604f1` | `d35b052c7e9b5968ec219dce374def76b1d7a3c0056916a044e08d055e294acf` |
| `96lN2omwit4-012400-013012` | 23 | 6 | 1/5 | 3133--3177 | post | `08807232449361eba043d1eba6fa5d5d656343e7d0590fb70c66085093d576a6` | `976792c3be3345a0af8d3a6f70924693a027cc9d2ef68f37cd2b2e30d105ab14` |
| `uzixOflp0tY-000000-001200` | 225 | 23 | 15/8 | 1--449 | 7 pre, 16 core | `03737d380bbe2d71be8128439361c9783bb7d86e0a21fdd145ba14ffad94f041` | `c1c84f89b70081990d3aba9563dcff03a307eb9a4694a7bef08bc970ac42da2c` |
| `uzixOflp0tY-001200-002400` | 279 | 18 | 18/0 | 451--1007 | core | `1d59436bd8d3725c5993e0d1d9235e96ebed03fca95c375286aa313e4e09fcbd` | `ebb2109af2d61cc8029e1323f8d084b17a90e23d17a703f9d5c58500f4acd3d0` |
| `uzixOflp0tY-002400-003600` | 214 | 22 | 22/0 | 1009--1435 | core | `a9028e4de1c5b8a62f00e4019ac704ca82b7651c4f9d2bbbde13d473bcc48754` | `bdd671ff17a9ad3f4614db6b57e5618a9a0967abb61136105daa9e08a1d14756` |
| `uzixOflp0tY-003600-004800` | 245 | 27 | 26/1 | 1437--1925 | core | `c9d01949828009d074182d60b390dc757cb7e78b4686b0ba1fe01bcb3c7235a0` | `abaa8c0b0c2900d6c4c63f93c53ca09a614eba51df9c5804875a5032583ee449` |
| `uzixOflp0tY-004800-010000` | 226 | 27 | 27/0 | 1927--2377 | core | `f8640ed8e4ebaba72afae60dfcbce7a6e59488dd649b7ba010e5a232c008f7f6` | `55b25c65360b2bdee3ba638b29344f95b573e3690ba2f2a4b86c4086629991bf` |
| `uzixOflp0tY-010000-011200` | 237 | 23 | 23/0 | 2379--2851 | core | `dd5364e472597dbdec86d989a3e51614d1e2bf131bdbd6afd9fac10d44ccd5cb` | `d62e9505ab60769376ad000de3d6c38d02c848df252753e201170a1f3765d000` |
| `uzixOflp0tY-011200-012400` | 243 | 27 | 26/1 | 2853--3337 | 14 core, 13 post | `cb6c2b006778b34141be862acf8358b34d4c8dfa20648a66ee95707963f53cdd` | `63f04d77a29d938721f9daf6c6a9be2016edd5675fcf0749539d9d7c1c8fd2df` |
| `uzixOflp0tY-012400-012528` | 18 | 3 | 3/0 | 3339--3373 | post | `dbc7b2f1a5a9137975a450128d0385b4818f69a3253d85d98265d63fd31d8c5e` | `985abb4ce06015657400fca580e6642e93e3a543a12cfb703d442eb474de147d` |
| **total** | **3,276** | **320** | **295/25** | | | | |

All sixteen lanes parse as strict JSONL with no blank lines. Their source
indices are ordered, non-overlapping, and consume the complete per-video
sequences `1,3,...,3177` and `1,3,...,3373`. Every lane has one final
`lane_audit`; normalized raw text, start, and end match the raw events. No
segment crosses a frozen cue-start boundary.

The late boundary allocations are explicit. The 96 recording has 14 core and
5 post-core segments in its `01:12:00` lane, followed by six post-core
segments. The uzix recording has 14 core and 13 post-core segments in its
late lane, followed by three post-core segments. The post-core material stays
coverage-only.

## Source-fidelity and page checks

The source-retained `LeBron James` wording at `96lN2omwit4 00:09:40.260` is
present with `[likely: Legendre transform]` as an uncertainty cue. The
recoverable `Any other questions?` prompt at `96lN2omwit4 00:10:05.480` is
retained with a classroom-question disposition, and the prompt at
`uzixOflp0tY 01:24:57.239` is retained as `Any other questions?`. All null
rows carry complete raw omission accounting, including the repaired late-Q&A
and foreign-marker records.

Primary page fields use handwritten pages 10--14 / physical 21--25 for 96 and
handwritten pages 15--20 / physical 26--31 for uzix. The three verbal Problem
Set 2 references in the uzix late lane carry physical pages 63--67 only in
explicit `secondary_assignment_reference` operations. No assignment page is
present in primary segment or formula-authority provenance.

All formula-authority page pairs and all cleaned-text delimiters pass the
chapter map and balanced-math checks. The current 96/uz source repairs leave
raw text, timestamps, event indices, and lane audits unchanged.

Unresolved blockers: none
