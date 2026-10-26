# Benchmark provenance

`BENCHMARK.json` holds two sets that are never mixed in reporting:

- the **primary** set: 43 frozen questions;
- the **extension** set: 41 new questions.

The content hash, a canonical JSON hash of both sets, is `ea20581c88fe163fcc484d86ecc9468b55c5488554378e8c57859f6f4d5c1cfc`. It is stored in `BENCHMARK.sha256`, and `run_experiment.py` refuses to run if the hash differs.

The benchmark was frozen against chunk set `8db472c5…7826`, because every gold label is resolved to concrete chunk IDs.

## Primary set: preserved from the earlier experiment

- **Source:** `pismo_retrieval_experiment_v2.zip` (sha256 `061801cd9d573aff025a200fcbf98cf44abc87a3f3f62b25d020aebfaad60f27`), member `benchmark/benchmark_questions_v2.json` (sha256 `71a969f3d180f6f9f8156e335328eddf43eea3dc21bf5ee5bc975c2a994c04da`). The file is read straight from the zip and is never extracted or edited.
- **Original authorship** (from its `_meta`): "Expected sources chosen by Claude web after grep/inspection of the corpus", label version v2 (C1, C2 and E4 were revised after pooled inspection).
- **Preserved:** all 43 IDs, question texts, categories, types and answerability values, and every `{file, match}` label. `tests/test_evaluation.py::test_primary_ids_and_labels_preserved` checks this against the zip.
- **Added annotations** (`PRIMARY_ANNOTATIONS` in `scripts/build_benchmark.py`). These change no question and no label:
  - lifecycle-sensitivity flags (B3–B5, C3, E1–E7, G5);
  - the migration issue each question exercises;
  - `absent_identifier` for G3 (`cards-pci/go-live`) and G7 (`MIGR-0400`);
  - the near-match distractors that the original notes name (G1 `99.999`, G3 go-live, G4 "Ordering dimensions", G7 `MIGR0000[12]`);
  - for D6, the catalogue statement that the payload is not documented.

### How file-based labels were mapped to KUs

A label `{file, match}` is satisfied by a chunk when all of the following hold (see `scripts/labels.py`):

- the chunk's KU lists `file` among its front-matter sources;
- the chunk is not inside the verbatim block of a different source;
- for guide or changelog files given without a regex, the chunk is inside that file's verbatim block, so generated navigation does not count as evidence;
- the chunk text matches the case-insensitive `match` regex.

The mapping never edits a label. It only resolves where the evidence now lives:

- guide and changelog text → the verbatim block in the guide or changelog KU;
- OpenAPI files → the API-reference KUs;
- `error_code_index.csv` → the error catalogue KUs;
- `event_type_inventory.csv` → the event catalogue KUs;
- `operations_catalog.csv`, `request_response_examples.csv` and `endpoint_event_map.csv` → the API KUs, plus the event catalogue for the map;
- quotations of the register and changelog in `KU-LIFE-marketplace-endpoint-removal` → that KU, which lists those files as sources.

### Verification (separate from retrieval)

Each label was checked twice before any retrieval run:

1. **Against the original source file:** the file exists and the regex occurs in it.
2. **Against the KU chunks:** at least one chunk satisfies the label.

| Set | Labels | valid | ku_coverage_gap | chunking_split | invalid_label |
| --- | ---: | ---: | ---: | ---: | ---: |
| Primary | 69 | **69** | 0 | 0 | 0 |
| Extension | 50 | **50** | 0 | 0 | 0 |

Every label of the 39 answerable primary questions resolves to KU evidence, so no primary question was dropped or rewritten. The four `none` questions (G1, G3, G4, G7) have no labels by design. Their checks also pass: `cards-pci/go-live` and `MIGR-0400` occur in no KU, and the D6 catalogue KU carries its "not documented" statement.

### Labels recorded as ambiguous (kept unchanged)

| Question | Issue | Effect |
| --- | --- | --- |
| B3 | The regex `202` also matches `2026`, so any chunk of the October 2026 changelog qualifies | B3 scores are lenient |
| D5 | A label on `client-webhooks.md` with no regex covers 235 chunks in 14 KUs | D5 scores are lenient |
| A4 | `Seller_management_-_Sellers.yaml` + `createMarketplace\b` is also satisfied by the curated lifecycle KU's table of current operations, which renders spec rows | Legitimate, but broader than the original single-file intent |
| A5, EXT-I03, EXT-I05 | Spec-wide labels covering 46–95 chunks | Lenient |
| EXT-B03, EXT-F04 | Narrower than the evidence: the same answer appears in unlabelled chunks (other Pix KUs; the Holidays API 400 examples for `EHLD0016`) | These questions under-report retrieval quality |

## Extension set: new, reported separately

- **Source:** `benchmark_inputs/extension_questions_v1.json`, written in this session **before any retrieval run on the full corpus**, by Claude Opus 5.5, the same model that built the KUs.
- **Method:** each question came from a specific source passage found by grep in the r2 corpus, and its `created_from` field cites that passage. Labels use the same `{file, match}` format, plus `{ku, match}` for KU-generated content (the curated lifecycle KU and the structured removal register).
- **Coverage:**
  - endpoint discovery (4), request and response fields (3), authentication and security (3), transfers and payments (3), events and webhooks (4), errors (4), rate limits and support (3), lifecycle and changelog (7), cross-KU workflows (6);
  - unanswerable (4), covering the marketplace successor, the event payload, PCI card go-live, and an unresolved event link;
  - migration-issue questions: SC-01, SC-03, SC-08, SG-01, SG-02, SG-03, SG-05, SG-06 and SG-07.
- **No label was changed after a retrieval ranking was seen.**

## Limitations

- **No independent annotator.** The primary labels were authored by "Claude web" in the earlier experiment. The extension labels, the label mapping and the diagnoses were made by the model that built the KUs. All agreement checks are mechanical (regex against source and KU).
- **Gold labels say where evidence is, not whether it is sufficient.** A retrieved relevant chunk does not prove a question is answerable; the answerability field records the intent.
- **The 59-question consolidated-KU pilot benchmark could not be reused.** Its files are not present, so it could not be preserved or remapped.
