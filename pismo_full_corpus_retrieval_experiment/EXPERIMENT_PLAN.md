# Experiment plan

## Objective

Determine which of three approaches retrieves best when the only searchable corpus is the finalised `knowledge_units/` directory (623 KUs from the r2 migration):

- BM25 keyword retrieval;
- dense semantic retrieval;
- hybrid reciprocal rank fusion (RRF).

This is an evaluation only. It builds no chatbot, UI or answer generation, and it uses no LLM reranker.

## Inputs (all read-only)

| Input | Used for | Verification |
| --- | --- | --- |
| `../pismo_knowledge_units_migration/knowledge_units/` | The only retrieval corpus | 623 KU files; IDs equal `work/ku_index.json`; the corpus manifest hash is recorded |
| `../pismo_knowledge_units_migration/` reports, manifest and `work/` | Risk register and context only (never indexed) | Read only |
| `../pismo_kb_release_r2/kb_corpus/` | Verifying gold-label evidence against the original sources (never indexed) | Fingerprint `7080b549…f0e62` checked unchanged at the end |
| `~/Downloads/pismo_retrieval_experiment_v2.zip` | The frozen 43-question benchmark (`benchmark_questions_v2.json`), read straight from the zip | zip sha `061801cd…0f27`; member sha `71a969f3…04da` |
| `~/Downloads/RETRIEVAL_EXPERIMENTS.md`, `SCENARIO_TEST_MATRIX.md`, `TECHNICAL_LEARNINGS.md` | Prior results and lessons (historical) | Same byte sizes as the copies in the zip's `docs/`; content identity not separately hashed |
| The local Hugging Face cache, `all-MiniLM-L6-v2` | The dense embedder | Pinned revision `1110a243…`; offline (`HF_HUB_OFFLINE=1`) |

Two requested inputs were **not found**:

- **The migration ZIP.** The migration exists only as a directory, which was verified directly.
- **The 59-question, 6-KU, 117-chunk pilot.** No benchmark, chunk or result files for it exist on this machine; its figures appear only in the request. It is reported as historical and was not recreated.

## Steps

1. **Corpus build** (`scripts/build_corpus.py`). Enforce the allowlist: only `knowledge_units/<category>/KU-*.md` files with valid front matter, `ku_id` equal to the file name and `category` equal to the folder. Reject everything else. Fail on duplicate IDs, on non-KU paths and on any KU byte-identical to a source file. Then chunk, and write `CORPUS_MANIFEST.csv`, `results/chunks.jsonl` and `results/corpus_summary.json`.
2. **Benchmark** (`scripts/build_benchmark.py`). Load the frozen questions unchanged, and verify every gold label twice: against the source file and against the KU chunks. Map each label to relevant KU IDs and evidence sections. Add the separate extension set (`benchmark_inputs/extension_questions_v1.json`). Freeze `BENCHMARK.json` and its hash in `BENCHMARK.sha256`.
3. **Embeddings** (`scripts/embed_corpus.py`) and **sanity checks** (`scripts/semantic_sanity.py`).
4. **Runs** (`scripts/run_experiment.py`). These start by verifying the chunk-set hash and the frozen benchmark hash, then run every configuration on every question.
5. **Tests** (`pytest tests`), then the analysis and reports.

## Chunking policy

The same chunks are used by every method. The policy was chosen by inspecting the KU structure, not by benchmark results.

- **Unit:** a heading section (outside code fences). An API operation (the `<!-- op -->` marker, its `###` heading and its `####` subsections) is kept together while it fits. A verbatim source block keeps its own internal headings.
- **Packing:** adjacent sections with the same key (the same operation, or the same top-level section of a source block or KU) are merged up to 4,000 body characters. This is the prior experiment's v2 budget.
- **Oversized blocks:** tables are split by rows with the header repeated; code fences are split by lines and reopened; paragraphs are split at blank lines.
- **Removed and kept text:** provenance comments (`source:begin`, `op:`, `schema:`) are removed from the indexed text and kept as metadata. Heading-only sections are carried into the next section.
- **Indexed text:** the KU title, the heading path and the body.
- **Chunk ID:** `KU-ID::<section identity>`, where the identity is the operationId for an operation, the source stem plus inner headings for verbatim content, or the heading path for generated sections. `::pNN` marks a split part and `~n` breaks a tie (only 2 of 11,026 chunks need one).
- **Metadata per chunk:** KU ID, title, path, category, type and lifecycle; heading path, section heading and parent heading; the source path of the verbatim block; source references (path, URL, sha256); the operation; and flags (`historical_changelog`, `deprecated_operation`, `unresolved_operation_link`, `removal_register`, `not_documented_statement`).

## Methods

| Configuration | Definition |
| --- | --- |
| `bm25` | Okapi BM25 (k1 1.5, b 0.75, non-negative idf). The tokenizer keeps both words and whole compound identifiers (`x-account-id`, `encrypted_pan`, `v1/migrations/cards-pci`). Ties are broken by chunk ID |
| `semantic` | MiniLM cosine. A chunk's score is the maximum over its 1,000-character windows. The query is the raw question text. Ties are broken by chunk ID |
| `rrf_equal` | Σ 1/(60 + rank) over the BM25 list (chunks with a positive score) and the semantic list (all chunks) |
| `rrf_bm25_2to1` | Σ w/(60 + rank) with w = 2 for BM25 and 1 for semantic |
| `bm25_exact`, `rrf_bm25_2to1_exact` | **Optional lexical enhancement, reported separately.** Detected identifiers (error codes, paths, headers, hyphen/snake/camel identifiers; `mTLS` excluded) promote the chunks that contain all of them, then those containing any of them, in base order |

RRF ties are broken by the fused score (rounded to 1e-12), then the best single-method rank, then the BM25 rank, then the chunk ID.

## Evaluation

The evaluation follows the gold-label rule in `scripts/labels.py`. The primary metrics are Recall@5 and Recall@10, MRR (depth 100), and label-level nDCG@5 and nDCG@10. Also reported:

- Hit@5 and Hit@10;
- KU-level recall;
- all-required-labels coverage at 5 and 10 for multi-label questions;
- breakdowns by query type, workflow, answerability, migration issue and lifecycle sensitivity;
- paired bootstrap 95% intervals for the key differences.

Unanswerable questions are not scored for recall. Their top results are inspected for misleading near-matches, for the KU's own "not documented" statements and for score separation.

**No tuning.** Every parameter (chunk budget, window size, BM25 k1 and b, RRF k, weights) was fixed before the first retrieval run, so no development subset was needed and the final benchmark was never used for tuning. The weights 1:1 and 2:1 are the ones the request specified.

## Known limitations planned for

- A single author and judge (this model) for the KUs, the extension questions and the diagnoses.
- Small samples: 39 and 37 scored questions, with per-workflow n of 3–7.
- One small embedder (MiniLM, 256 word pieces).
