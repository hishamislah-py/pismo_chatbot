# Validation report

This report covers what was verified before and after the retrieval runs. It keeps corpus and benchmark integrity separate from retrieval quality.

## 1. Artifact inspection

| Expected artifact | Found | Notes |
| --- | --- | --- |
| Migration ZIP | **No** | The migration exists only as the directory `pismo_knowledge_units_migration/`, which was used directly and read-only |
| `knowledge_units/` | Yes | 623 `.md` KUs plus one non-KU marker file (rejected) |
| `MIGRATION_MANIFEST.csv`, `SOURCE_COVERAGE.csv`, `VALIDATION_REPORT.md`, `ISSUES_AND_GAPS.md` | Yes | Read for the risk register; never indexed |
| `archived_source_inventory/SOURCE_INVENTORY.csv`, `tools/`, `work/` | Yes | `work/ku_index.json` was used to cross-check the KU ID set |
| Prior experiment `pismo_retrieval_experiment_v2.zip` (two identical copies in Downloads) | Yes | sha `061801cd…0f27`; contains the frozen benchmark v1 and v2, results, scripts and docs |
| 59-question, 6-KU, 117-chunk pilot | **No** | No files anywhere under the user profile; it is mentioned only in the request. Reported as historical and not recreated |

The **actual corpus counts** were measured, not taken from reports:

- 623 KU files, 623 unique KU IDs and 623 unique content hashes;
- the ID set equals the migration's `ku_index.json`;
- by type: api_reference 266, workflow_guide 284, changelog_history 22, event_catalogue 23, error_catalogue 27, lifecycle_reference 1.

The claim of 623 unique KUs is therefore **confirmed**.

## 2. KU-only isolation

Enforced in code by `scripts/corpus.py` and `scripts/run_experiment.py::verify_inputs`, and tested in `tests/test_corpus.py`:

- **Allowlist:** `knowledge_units/<category>/KU-*.md`, with YAML front matter, `ku_id` equal to the file name and `category` equal to the folder. Any file outside `knowledge_units/` (after resolving the real path) raises an error.
- **Rejected and recorded:** `knowledge_units/.generated_by_build_kus`.
- **Hard failures:** a duplicate KU ID; a KU without front matter; a KU byte-identical to any of the 503 original source files; a non-KU path in the chunk index at run time.
- **Tests:** these build fake KU folders containing `.yaml`, stray `.md` and `.csv` files, and check that they are rejected; they also check duplicate IDs and missing front matter.
- **Never indexed:** source guides, YAML, CSV, changelogs, inventories, manifests, reports and prior results. They were used only to verify gold labels (source corpus) and to build the risk register (migration reports).

**Integrity after the run:**

- the source corpus fingerprint is still `7080b549e8160a2bc555ae1c0646b4d9a807414cd12dbd1943e712f5031f0e62` (503 files);
- no file in `pismo_knowledge_units_migration/` or `pismo_kb_release_r2/` is newer than the start of this experiment;
- the prior experiment zip was read without extraction.

## 3. Risk register (migration issues → retrieval risk)

High-risk examples were inspected by hand; the full corpus was not audited by hand.

| Migration issue | Inspected example | Retrieval risk observed | Where measured |
| --- | --- | --- | --- |
| MD-07: 7 KUs over 100 KB | `KU-EVT-client-webhooks-part-09` (217,819 bytes, one fenced block) | Chunked into 66 chunks of at most 3,993 characters, with fences reopened; no oversized chunk remains. The large API KUs became 45–69 chunks each | `corpus_summary.json`; `test_split_code_fences_reopen` |
| SC-01: guides still reference removed marketplace endpoints | G5, E2, EXT-I01 | G5 and E2: warnings and the curated KU are in the hybrid top 10. **EXT-I01: no warning in the top 10** for the hybrids and semantic | §5 of `RESULTS.md` |
| SC-02: register lists 7 names, changelog lists 8 | E1 | Both sources are retrieved at ranks 1–2 by the hybrids, so the discrepancy is visible to a reader | `per_question_*.json` |
| SC-03: endpoint on the removal register and in the current spec | EXT-A05 | The register row is outside the top 10 for BM25 and the hybrids, but the top-1 operation chunk carries an inline lifecycle note | `FAILURE_ANALYSIS.md` |
| UR-01: 86 unresolved operation links | 84 chunks flagged `unresolved_operation_link` | The flag is metadata only; no ranking uses it. Unresolved links are **not** labelled as removed | `chunk_flags` |
| SG-01: no event payloads | D6, EXT-U02 | The "not documented" statements are never in the top 10 | `unanswerable_and_lifecycle.json` |
| SG-02 / SG-03: no successor endpoint; no PCI go-live | EXT-U01, G3, EXT-U03 | The successor statement ranks 1–2. **PCI go-live returns the accounts go-live near-match in every method** | same |
| SG-05: error codes only in examples | EXT-F02 (`WP2P0000`) | Retrieved at rank 1–4; the evidence is only the example message (partial) | same |
| SG-06: unresolved event links | EXT-H04, EXT-U04 | The changelog link is found (rank 1); the emitting operation is not documented and nothing says so | same |
| MD-08: unconverted MDX/HTML | 819 of 11,026 chunks contain MDX/HTML components | Indexed as-is. They add noise tokens for BM25 (for example `summary style`); no specific failure was traced to them | `chunks.jsonl` |

## 4. Benchmark verification

`BENCHMARK_PROVENANCE.md` has the full account. In brief:

- all 69 primary and all 50 extension labels are valid against **both** the original source file and at least one KU chunk;
- the four unanswerable primary questions keep zero labels, and their absent-identifier and statement checks pass;
- the frozen hash is verified by `run_experiment.py` and by `tests/test_evaluation.py::test_benchmark_frozen_hash`.

## 5. Semantic model sanity checks (`results/semantic_sanity.json`)

The criteria were fixed before the run.

| Check | Query | Result |
| --- | --- | --- |
| Self-similarity | the same text twice | cosine 1.000: **pass** |
| S1 exact operationId | `post-payments-v1-hold-funds-unblock` | first acceptable KU at rank 1: **pass** |
| S2 error code | `WEAM0001` | rank 1: **pass** |
| S3 field name | `encrypted_pan` | rank 16; criterion ≤ 10: **fail** (3DS PAN-encryption KUs rank first) |
| S4 paraphrase | "move money from one customer account to another account" | rank 22: **fail** |
| S5 paraphrase | "freeze part of a balance … because a judge ordered it" | rank 43: **fail** |
| P1 confusable concepts | earmark versus hold funds for "set money aside until a scheduled release date" | 0.525 vs 0.383: **pass** |
| P2 confusable concepts | PCI card migration versus accounts go-live for "make migrated PCI cards go live" | 0.646 vs 0.399: **pass** |
| P3 confusable concepts | webhook verification versus rate limiting | 0.685 vs 0.217: **pass** |

This is genuine dense retrieval, not lexical retrieval relabelled. It handles short, distinctive identifiers when the query is the identifier alone (S1, S2). It is weak on paraphrase over the full corpus (S4, S5) and on common field names (S3), and these weaknesses show up in the benchmark results.

## 6. Automated tests

`python -B -s -m pytest tests -q -p no:cacheprovider` → **38 passed, 0 failed** (executed after the final run).

**Determinism:** a second run of `run_experiment.py` gave byte-identical `per_question_*.json` and `aggregate_metrics.json`.

| File | Covers |
| --- | --- |
| `tests/test_corpus.py` (13) | KU-only isolation (real corpus plus synthetic rejects); duplicate KU IDs; missing front matter; unique and stable chunk IDs (rebuild equality, identity-based not positional); provenance fields and source refs; verbatim markers not indexed; operation kept with its tables; table header repetition; code-fence reopening; reproducible manifest and chunk-set hashes |
| `tests/test_retrieval.py` (13) | Identifier-preserving tokenizer; identifier detection (including the `mTLS` exclusion); exact-lookup promotion; BM25 ranking on a known example; non-negative idf; score tie-breaking; dense max-over-windows; windowing; RRF formula and weights; items missing from one list; deterministic RRF tie-breaks; sanity-check artefact; embedding provenance (model, revision, dimension, unit norm) |
| `tests/test_evaluation.py` (12) | Metrics on hand-computed examples (recall, MRR, hit, all-labels, KU recall); top-K cutoffs; label-level nDCG; multi-KU coverage; label semantics; classification of missing gold evidence (`invalid_label`, `source_file_missing`); frozen benchmark hash; primary IDs and labels preserved against the zip; unanswerable questions unscored, with absent identifiers and statements checked; extension set kept separate; lifecycle flags and diagnostics present; results cover every question and configuration |

## 7. What this validation does not establish

- **Answer correctness.** Retrieval is measured; answer correctness is not judged. Relevant evidence in the top k does not mean an answer would be correct.
- **Independent review.** No independent human or model annotator was available. The KUs, the extension questions, the label mapping, the failure diagnoses and this report all come from the same model. The primary questions came from an earlier session (Claude web), so they are not independent of Claude either.
- **Statistical power.** The samples are small (39 and 37 scored questions; 3–7 per workflow). Only the differences whose bootstrap intervals exclude zero should be treated as findings.
