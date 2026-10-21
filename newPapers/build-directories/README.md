# Build workspaces

[Book catalogue](../README.md) · [Build guide](../../docs/BUILDING.md)

Each edition has its own directory. The catalogue maps readable book titles
to these source directories, including the unedited Atiyah and Macdonald
edition under `unedited/`.

Within a project, `latex/` holds the document and local styles. Its README
explains the build entry point. Files such as `NOTATION.md`, `SOURCE_MAP.md`,
and `RELEASE_VERIFICATION.md` record that project's conventions and review
evidence.

The files directly in this directory support the Weinberg QFT exercise series:

| Files | Purpose |
| --- | --- |
| [build_all_weinberg_qft_exercise_editions.sh](build_all_weinberg_qft_exercise_editions.sh) | Build and check all volumes, then export the series |
| [build_weinberg_qft_exercise_edition.sh](build_weinberg_qft_exercise_edition.sh) | Template copied into each edition as `build_and_verify.sh` |
| [scaffold_weinberg_exercise_editions.py](scaffold_weinberg_exercise_editions.py) | Create the initial exercise structure and supporting files |
| [audit_weinberg_qft_exercises.py](audit_weinberg_qft_exercises.py) | Audit an edition's exercises |
| [audit_weinberg_qft_cross_volume.py](audit_weinberg_qft_cross_volume.py) | Check supplementary material across volumes |
| [fingerprint_weinberg_qft_release_inputs.py](fingerprint_weinberg_qft_release_inputs.py) | Detect changes to inputs during a release build |
| `render_weinberg_qft_*.py` | Generate inventories, source ledgers, pagination crosswalks, and release manifests |
| [WEINBERG_QFT_SOURCE_PRIORITY.md](WEINBERG_QFT_SOURCE_PRIORITY.md) | Define the source policy for supplementary exercises |
| [WEINBERG_QFT_EXERCISE_SOURCE_INVENTORY.md](WEINBERG_QFT_EXERCISE_SOURCE_INVENTORY.md) | Catalogue candidate exercise sources |

Use an edition's own build script when working on that edition. The shared
scaffold and template are used to create project files and depend on this
directory layout.
