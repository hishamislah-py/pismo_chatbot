# Pismo knowledge units (KB r2 migration)

This directory holds the Pismo KB release r2 corpus (`../pismo_kb_release_r2/kb_corpus/`, 503 files), migrated into **623 implementation-oriented Markdown knowledge units (KUs)**. Every source file is accounted for. Every KU traces back to its source files by path, SHA-256 and published URL.

The source corpus was only read, never changed. Its fingerprint P is still `7080b549e8160a2bc555ae1c0646b4d9a807414cd12dbd1943e712f5031f0e62`.

## Layout

| Path | Contents |
| --- | --- |
| `knowledge_units/<category>/KU-*.md` | The knowledge units: 17 category folders, one KU per file, with YAML front matter. **This is the only folder a retrieval system should index.** |
| `MIGRATION_PLAN.md` | Taxonomy, KU types, method, batch strategy, validation strategy and deviations from the requested structure. |
| `MIGRATION_MANIFEST.csv` | One row per source file (503): the KUs it went into, its migration status, its validation status and its issue IDs. |
| `SOURCE_COVERAGE.csv` | One row per source unit (6,226): each guide body, changelog body, operation, named schema, CSV row and README, mapped to the KU and anchor that carries it. |
| `VALIDATION_REPORT.md` | Pilot results, full-corpus results, retrieval tests and limitations. |
| `ISSUES_AND_GAPS.md` | Source contradictions, source gaps, unresolved relationships, migration defects and validation limitations, with IDs (`SC-`, `SG-`, `UR-`, `MD-`, `VL-`). |
| `archived_source_inventory/SOURCE_INVENTORY.csv` | An inventory of the 503 source files (path, type, size, SHA-256, URL, updated date). The files themselves are not copied. |
| `tools/` | The scripts that build and validate the collection. They use only the standard library plus PyYAML, which was already installed. |
| `work/` | Machine-readable intermediate results and evidence: analysis, the KU index, the build log, validation and retrieval results, and issue data. |

## KU format

Each KU starts with front matter containing these fields:

- `ku_id`, `title`, `category`, `ku_type`, `lifecycle`;
- `sources`: path, sha256, url, role, updated_at;
- `operations`, `events`, `error_codes`, `related_kus`.

The body then has a header line, a purpose and scope section and the content. The content depends on the KU type:

- **workflow_guide** and **changelog_history:** the source body, copied byte for byte with its front matter removed, between `<!-- source:begin path=… part=… -->` and `<!-- source:end -->` markers. Before it come a navigation section and a table of linked operations. That table states, for each link, whether the target exists in the current specifications. Changelog KUs carry a **HISTORICAL RECORD** banner.
- **api_reference:** one KU per specification tag, with large tags split into `-part-NN`. These KUs are rendered from the OpenAPI YAML: parameters, request and response field tables with fully resolved `$ref`s, concrete examples only, the error codes found in the examples, the events and the operation catalogue line.
- **event_catalogue**, **error_catalogue:** rendered from `api-reference-data/*.csv`.
- **lifecycle_reference:** one curated KU, `KU-LIFE-marketplace-endpoint-removal`, built only from quoted evidence.

## Retrieval rule

Index `knowledge_units/` only. Do not index `work/`, `tools/` or the CSVs. They contain identifiers but no answers, and they would compete with the KUs.

Two rules apply to answers built from changelog KUs:

- treat them as historical records;
- check what an endpoint does today against the `KU-API-*` KUs and the `KU-LIFE-*` KUs.

## Rebuild and validate

Run these commands from `tools/`. They make no network calls.

```powershell
cd C:\Users\artlptp263user\Downloads\pismo_claude_code_handoff\pismo_knowledge_units_migration\tools
python -B -E -s a1_inventory.py        # corpus integrity + SOURCE_INVENTORY.csv
python -B -E -s a2_analyse.py          # work/analysis.json
python -B -E -s build_kus.py           # knowledge_units/, MIGRATION_MANIFEST.csv, SOURCE_COVERAGE.csv
python -B -E -s issues_data.py         # work/issues_data.json
python -B -E -s annotate_manifest.py   # issue IDs into the manifest
python -B -E -s validate.py            # 22 deterministic checks; exit 1 on any failure
python -B -E -s retrieval_tests.py     # 29 retrieval / not-documented tests; exit 1 on any failure
```

To validate without rebuilding, run only the last two commands.

Use `-B -E -s` and not `-I`: the `-I` flag blocks the scripts' local `common` import.

`build_kus.py` writes only into a `knowledge_units/` folder that carries its own `.generated_by_build_kus` marker. It refuses to overwrite any other folder.
