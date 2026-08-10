# Pass 2 global mechanical audit

## Audit basis

This final read-only audit uses the stable merged snapshot
`transcript.cleaned.jsonl` SHA-256
`c84a329bba04d3da2f2e5f6911b06919b2e358b0c4653a9a0e0f7e532859f112`.
It covers all 45 manifest lanes, all 45 raw-caption lane files, all 45
cleaned outputs, `chapter-metadata.json`,
`raw-caption-lane-manifest.jsonl`, `transcript.cleaned.jsonl`,
`transcript-dispositions.jsonl`, and the full
`tools/merge_cleaned_transcript.py` implementation.

I read the five completed video audits:

- `pass2-audits/audit-96-uz.md`
- `pass2-audits/audit-M0py5a4RWhE.md`
- `pass2-audits/audit-vk_RlYUKUyM.md`
- `pass2-audits/audit-3VG2kDHso08.md`
- `pass2-audits/audit-TtMNnZ8__UU.md`

The source and contract basis was `dispatch_luna_pass2.sh`,
`source-map.md`, `source-lanes/playlist-chronology.md`,
`source-lanes/boundary-assignment.md`, the six binding documents named by
the dispatcher, and the video and note source lanes cited by those audits.

## Commands

The checks ran from `/Users/wlancer/Coding_Projects/TypesetTranslate`.
The inline Python validator loaded every JSONL line, rejected blank lines and
non-object rows, reconstructed each `raw_text` from its ordered raw events,
checked timestamps and positive intervals, checked one lane audit per lane,
checked per-video global raw ordering, and compared every canonical row to
its source lane row. It then checked canonical IDs and source-span IDs,
merged metadata hashes and counts, page-map pairs, assignment references,
page-68 boundary evidence, disposition one-to-one links, null-operation
accounting, and balanced math delimiters.

```sh
cd /Users/wlancer/Coding_Projects/TypesetTranslate
sed -n '1,240p' newPapers/build-directories/yin_qft_253abc/work/253a-ch02/dispatch_luna_pass2.sh
sed -n '1,560p' newPapers/build-directories/yin_qft_253abc/work/253a-ch02/tools/merge_cleaned_transcript.py
for f in newPapers/build-directories/yin_qft_253abc/work/253a-ch02/pass2-audits/audit-{96-uz,M0py5a4RWhE,vk_RlYUKUyM,3VG2kDHso08,TtMNnZ8__UU}.md; do sed -n '1,99999p' "$f"; done
python3 - <<'PY'
# read-only global JSONL, coverage, provenance, page, disposition, and delimiter checks
PY
sha256sum newPapers/build-directories/yin_qft_253abc/work/253a-ch02/transcript.cleaned.jsonl \
  newPapers/build-directories/yin_qft_253abc/work/253a-ch02/transcript-dispositions.jsonl
```

## Counts and exact coverage

| video | lanes | raw events | source-event range | segments | cleaned non-null | cleaned null | cue-start scopes |
|---|---:|---:|---|---:|---:|---:|---|
| `96lN2omwit4` | 8 | 1,589 | 1--3,177 | 150 | 135 | 15 | 2 pre, 137 core, 11 post |
| `uzixOflp0tY` | 8 | 1,687 | 1--3,373 | 170 | 160 | 10 | 7 pre, 147 core, 16 post |
| `M0py5a4RWhE` | 8 | 1,682 | 1--3,363 | 139 | 136 | 3 | 135 core, 4 post |
| `vk_RlYUKUyM` | 7 | 1,456 | 1--2,911 | 145 | 133 | 12 | 1 pre, 136 core, 8 post |
| `3VG2kDHso08` | 7 | 1,607 | 1--3,213 | 143 | 137 | 6 | 3 pre, 137 core, 3 post |
| `TtMNnZ8__UU` | 7 | 1,672 | 1--3,343 | 154 | 101 | 53 | 1 pre, 103 core, 50 next |
| **total** | **45** | **9,693** | | **901** | **802** | **99** | **14 pre, 795 core, 42 post, 50 next** |

Every raw caption event is consumed exactly once. Within each video, the
source indices are the complete odd sequence from 1 through the listed
endpoint. Each lane has exactly one `lane_audit` row with matching input and
consumed counts, first and last indices, and `coverage_exact: true`. Every
segment has the required cleanup, provenance, page, confidence, uncertainty,
and authority fields. No segment crosses a cue-start scope boundary.

The merged file contains one metadata row and 901 canonical transcript rows.
IDs run from `YIN253A-C02-T000001` through `YIN253A-C02-T000901`; source-span
IDs run in the same order. The disposition file contains 901 rows with a
one-to-one transcript-record and source-span mapping. Scope, chapter use,
source disposition, confidence, and current transcript hash all agree.

Primary page arrays use the `chapter_metadata.page_map` mapping from physical
pages 21--62 to handwritten pages 10--51. The three Problem Set 2 mentions
use explicit `secondary_assignment_reference` operations for physical pages
63--67, and those pages occur in no primary segment or formula authority.
Physical page 68 occurs only on the two TtMNnZ8__UU next-chapter rows beginning
at `00:51:10.020` and `00:51:15.660`; both are null-cleaned. The nested
authority at TtMNnZ8__UU `00:32:58.500` now uses note pages `[44,49]` for
physical pages `[55,60]`, matching the frozen map.

The delimiter scan found no unbalanced dollar, `\\(` / `\\)`, or `\\[` /
`\\]` pair and no unbalanced braces in cleaned text or formula-authority
items and equations. JSONL parsing found no blanks or malformed rows.

## Current lane hashes

| lane | raw lane SHA-256 | cleaned lane SHA-256 |
|---|---|---|
| `96lN2omwit4-000000-001200` | `1dc34e6f1b4d14e5ad6d594462f1bb5751b5f168ef498b4621247a67a0c3f6fe` | `79147505267c2925259c395a6019a82997965b6a06c1ed4d8eee876440f5bd7c` |
| `96lN2omwit4-001200-002400` | `2bb98af4d3e977740f76543584f3911161a4ef87459bfc0a9459b8c1ade4b64f` | `6dd11c509ecff4e2fdd756c219572a58185ce0fbed13d83be0745a4c2f6b0694` |
| `96lN2omwit4-002400-003600` | `6cb9c2196495e4e86837283e31015d5073a32c208ab6ab78a401163fa2c3dd61` | `a0dfbe4fa501ff9b90928dfac9f8db5d0350afc4408c16b37f378021f13fe7b0` |
| `96lN2omwit4-003600-004800` | `4683daf8deaf58af618fa7beb8126d28c6a61a3212810b5710756ec863f94bcc` | `3d60b23fd069887cfd0dab6bd2d51e6d3f499d636034dce995a7df76ea434647` |
| `96lN2omwit4-004800-010000` | `54c675d262b76b92006847ef2b90c62017741d18ce1307f642d166ef3b38381b` | `11d3ee9481f2bac98df6534941c3f00adaef32ca9f10145e4e884772dac38afc` |
| `96lN2omwit4-010000-011200` | `92286f06f8078761465175c9a41512056b38799bbbbbae20d79dff846f31146d` | `3eccc239ad73c738b547036057f7ab6a815100ab6f264e61988bfd9eef33485f` |
| `96lN2omwit4-011200-012400` | `2a5334e6cdf28ff62442381584fc8d6812686a9233beb4435e02ad8a8ea604f1` | `d35b052c7e9b5968ec219dce374def76b1d7a3c0056916a044e08d055e294acf` |
| `96lN2omwit4-012400-013012` | `08807232449361eba043d1eba6fa5d5d656343e7d0590fb70c66085093d576a6` | `976792c3be3345a0af8d3a6f70924693a027cc9d2ef68f37cd2b2e30d105ab14` |
| `uzixOflp0tY-000000-001200` | `03737d380bbe2d71be8128439361c9783bb7d86e0a21fdd145ba14ffad94f041` | `c1c84f89b70081990d3aba9563dcff03a307eb9a4694a7bef08bc970ac42da2c` |
| `uzixOflp0tY-001200-002400` | `1d59436bd8d3725c5993e0d1d9235e96ebed03fca95c375286aa313e4e09fcbd` | `ebb2109af2d61cc8029e1323f8d084b17a90e23d17a703f9d5c58500f4acd3d0` |
| `uzixOflp0tY-002400-003600` | `a9028e4de1c5b8a62f00e4019ac704ca82b7651c4f9d2bbbde13d473bcc48754` | `bdd671ff17a9ad3f4614db6b57e5618a9a0967abb61136105daa9e08a1d14756` |
| `uzixOflp0tY-003600-004800` | `c9d01949828009d074182d60b390dc757cb7e78b4686b0ba1fe01bcb3c7235a0` | `abaa8c0b0c2900d6c4c63f93c53ca09a614eba51df9c5804875a5032583ee449` |
| `uzixOflp0tY-004800-010000` | `f8640ed8e4ebaba72afae60dfcbce7a6e59488dd649b7ba010e5a232c008f7f6` | `55b25c65360b2bdee3ba638b29344f95b573e3690ba2f2a4b86c4086629991bf` |
| `uzixOflp0tY-010000-011200` | `dd5364e472597dbdec86d989a3e51614d1e2bf131bdbd6afd9fac10d44ccd5cb` | `d62e9505ab60769376ad000de3d6c38d02c848df252753e201170a1f3765d000` |
| `uzixOflp0tY-011200-012400` | `cb6c2b006778b34141be862acf8358b34d4c8dfa20648a66ee95707963f53cdd` | `63f04d77a29d938721f9daf6c6a9be2016edd5675fcf0749539d9d7c1c8fd2df` |
| `uzixOflp0tY-012400-012528` | `dbc7b2f1a5a9137975a450128d0385b4818f69a3253d85d98265d63fd31d8c5e` | `985abb4ce06015657400fca580e6642e93e3a543a12cfb703d442eb474de147d` |
| `M0py5a4RWhE-000000-001200` | `29f57c42133fe47ff84fa12a8bc13fea58663bd26f23eb9ee2eb7532cb56bd4e` | `fd9d5236d35b87a69b37ec69b8d8e988bd49b5fd595b895867f71d7593127449` |
| `M0py5a4RWhE-001200-002400` | `dfe61b3ad48d5f744f45a54ff4fc811985f65e89108bc3c7d78fff848dbc8377` | `55baa79e19dfa52a2c23ba56069a5ccdf42b91cc026e24c3154c6ea3221f304b` |
| `M0py5a4RWhE-002400-003600` | `9215816289f14b9e73096c904f5998c9b23663e916563f32556e472cd9d980d5` | `87145b1728958dbf2e274df8938c6afe21862252628c1bf0eb1f2e13132960f5` |
| `M0py5a4RWhE-003600-004800` | `1f671a45ba1562600d63a31a5f643efd3f202470ed4192513dea0a86301cf8a5` | `7d55d6361d61732231c9352d85f7042f394207ec079d3e8264345d3e8c29e5d8` |
| `M0py5a4RWhE-004800-010000` | `f7515e061fdeb2be5d76a80bc965ef064e422e8c09a1b3683d35c8acbc8cb0ba` | `594e046a301d435302aaf7245345cd91dffeb789054db638feb000f38c660d69` |
| `M0py5a4RWhE-010000-011200` | `c0daa759df4cdd96a0a01662b533340f946e6457623c1a7a1187339c29941ef1` | `42632de5e5ed3de687b65b03eed17e3d9e19a99dde696678c59d6a182ce18195` |
| `M0py5a4RWhE-011200-012400` | `0b69090a07805d698a4f25ec89fe54de54acc3d5c1c9a6f38b98dac03684bd9f` | `f51cfcbb38205dbfcec624141c99b3aa28f8731a3f5971e035f1aa6d133eb31d` |
| `M0py5a4RWhE-012400-012502` | `4f47220454793ff75c95f0e09a1b4c90a9aae4e409b8391d6ff9a011db731de8` | `facede55c3e0c27fb9b924f81131099550027e772b91007ed2b687c8135b6b2b` |
| `vk_RlYUKUyM-000000-001200` | `b12b7dc6b79301eb33614c7638a5ca68aa49780af37adcd59ac8d8a236cbab2f` | `7fa18d4394793407ceaec5c9f437d5bf963ad8dabe162d5583412f972476bc3c` |
| `vk_RlYUKUyM-001200-002400` | `bdd19042ab06b1331b71ede5098ace5be7015b0a0625fc9f1b455a4e0427be83` | `ca30b6234458a700089f99529fc827e16dc5892bd55e61a659b5a780821f18c3` |
| `vk_RlYUKUyM-002400-003600` | `585258a7009a595c2b17b301276c24ff7f3c5e49d6b9231eb282825296ea9ae7` | `243a0d73dc5e75d57d1043b4cdb8cbd09bc9b498fc1b2888f9f68032f4b10bb0` |
| `vk_RlYUKUyM-003600-004800` | `9bcf10f505e10a805178392af7efb86c52f21a7f5324ce6a70625d6ea4f35e84` | `8732d9eb2d709171db7235299c77366543be2013442148f995d7a5d9e63bb97d` |
| `vk_RlYUKUyM-004800-010000` | `044e21cd811aa2df64d13ed3f99207c197bf0d77baac30e2fa32f71771b942bc` | `f595460dc52030483ca1b28cf60b75044ee99576cd9f5eda825c3f3d3805ccfe` |
| `vk_RlYUKUyM-010000-011200` | `61213d2d020d74199ae28a14b900dc9202acda5ca2676016dececf174707803d` | `c89605384ae1a64b8ae40a9d05b8d0ee70c7b14332f676608b8ab8bbdb4d1b62` |
| `vk_RlYUKUyM-011200-012327` | `a9efc9f62b2c1f4f140f79cf5b614a3a3430d3d65201657532548de151eaab4d` | `b1895bb72c10f823407b63a283edd32a43347cfa446c3cb5b6cc67d20d404867` |
| `3VG2kDHso08-000000-001200` | `c1730c48064e84846a61136fcf2379221e5fddb8aa57b6a3cc0f09df002085e6` | `fbf80d189aa804502c5961247c38fb80aa0cbb942bd62a7093f1aabb54acd9b4` |
| `3VG2kDHso08-001200-002400` | `6bfb241c82783730822f7362b0e9a84cf4c21aee604b436fa04e4947b676a3fb` | `042bfd8f375cb89ce8878b66f55199cb2720e1714a47904f6f61475d81d0bb95` |
| `3VG2kDHso08-002400-003600` | `c63df29b9c1a44101051d07303b0b893edc2dd2f58f2e3735d412cd12ab38bde` | `e9328024e989895979f1c39ace904ebaad9c8c6d84986a745801c3c555209871` |
| `3VG2kDHso08-003600-004800` | `8b2cfabbbbb549936b29823bc7e76ad06dc9d6a3c161b738cda9999e8e511209` | `0a1025689c6a8b60aa4682ab7f6567584e581accb6e3d4a12467c2d7acdbfa6c` |
| `3VG2kDHso08-004800-010000` | `7ad9d4ba33c9f895858f0b7267c2cc70919c8a230f31671f0f57b23472ed4bb3` | `ca4129126dc0b44b5ac44fc0ea0b688bdaf5936a670258e746a067c739cc0d0b` |
| `3VG2kDHso08-010000-011200` | `713218a85d675566645855799adfa3997c35eceb17656a07bbcc7f568f91910b` | `65e210d808305a65a5c02327eb2af269fcf5ab6ccce421e92dcdb2e59abe543b` |
| `3VG2kDHso08-011200-011922` | `a1c42c1da17326459f5f78da4e6bbbadf7aed4a851e8d17b6791149f85a90188` | `ef1f63f83564f48401887aa7f57fcfd509b9a4a7163f45f0419508b83f1b3f03` |
| `TtMNnZ8__UU-000000-001200` | `54b90e1f1e41fc29b863ed8d057e7b3907343a1c0568da711ce025dcdacacf7e` | `e69ba7298da16338ef639c5ddfe191746c511cf96c62aaccd0a6d799b19ac0fa` |
| `TtMNnZ8__UU-001200-002400` | `1e30084b4b8d9cee51aa79594beffe6ad6560af591dad627a5e2814c9ac30331` | `2852f7a862e215b284a08a768c51a80988ab5a0069e4bab7354968cd4212885f` |
| `TtMNnZ8__UU-002400-003600` | `0e53135610fe91ff364f845e85d0ac209004108f6b5805c78a92fdeda643edfa` | `e1001265bc33cfca075182bc740a7e44aa5d036e640aa2c73a2beba85b535591` |
| `TtMNnZ8__UU-003600-004800` | `952074d366de9b14bdf4d264491a22b7439dc46ad8990d5c552c65b7c7eb152b` | `ea51f5ffd6f57d42fe5707b77dd9d1b0669f249ff15e7b780681a560c10d086f` |
| `TtMNnZ8__UU-004800-010000` | `e517516fd0b3c88b0725e641848e1034920af2ddf7f3cb6662b7a6e136fc4b3c` | `2a527802b68c14108f5c5223ef0e0c9121951d6b04c173cdd18789548e0d424c` |
| `TtMNnZ8__UU-010000-011200` | `2fdabef2e1776f79914ab35d6a7e922de0dba3029b3eb0acce6bd31dd1e5499b` | `ff4634693392fb412af0174eed6b7bfb2a631c38dbdd9b48d439def745d2f3fc` |
| `TtMNnZ8__UU-011200-011956` | `ec92f55d41172d8ead11b71d9089c2f5af8ded3a8c2f1b1c2002021428a9ef25` | `695f6d5b02a54b41db5ff1df5ff2b103d0b7d5afb28a4de3f8e7879b0c81cf08` |

The merged-file hashes are:

```text
transcript.cleaned.jsonl       c84a329bba04d3da2f2e5f6911b06919b2e358b0c4653a9a0e0f7e532859f112
transcript-dispositions.jsonl  75b47e5e778b2933f1abdee5b02c56a6004fa534ceb8961b073fa97d44f7cd19
```

All mechanical checks pass in this stable snapshot.

Unresolved blockers: none
