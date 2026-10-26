# Dense retrieval backends: NumPy vs FAISS vs Chroma

Date: 26 October 2026. Scope: the dense-search step of the Pismo Assist hybrid retriever. Everything below was measured on this machine; nothing is estimated. Machine-readable results are in `out/`, with `out/executive_summary.csv` as the entry point.

## Recommendation

**Keep the current NumPy exact search. Neither FAISS nor Chroma justifies a migration for this workload.**

- **FAISS exact (IndexFlatIP)** gives byte-identical results: the same top-6 and evidence on all 132 questions. It is no faster at full depth (dense median 13.9 ms vs 13.0 ms, measured interleaved), and it adds a native dependency.
- **Chroma at full depth** gives identical results but is about 7.5× slower on dense search (98 ms vs 13 ms). It also takes 1.4 s to open cold, uses 2.8× the index memory and 1.7× the disk, and needs its own environment: the global install is broken and its newest `grpcio` DLL is blocked by Windows Application Control. It also threw a reproducible `KeyError` under 10-thread load (3 of 840 calls).
- **Truncated dense lists** (top-100/500/2,000 windows, the practical way to make either library fast) change the hybrid ranking, because production RRF ranks *all* 11,026 chunks.
  - With exact truncation (FAISS), labelled metrics stayed flat at @2,000 windows, but 10 of 132 top-6 sets still changed.
  - With Chroma's HNSW, truncation also lost relevant evidence at every depth tested: −1.3 points of label Recall@6 at @2,000.
- **Retrieval is not where the time goes.** Retrieval plus evidence assembly takes about 50–70 ms of a 4–12 s answer. Inside the dense step, the NumPy matrix product takes 4.9 ms; most of the remaining ~16 ms is Python sorting of the 11,026-chunk ranking. A vector library would not remove that cost.

Revisit the decision if the corpus grows by an order of magnitude (exact search over 25,325 × 384 float32 vectors is 39 MB), or if metadata-filtered search or multi-process index sharing becomes a requirement.

## Executive comparison

Labelled benchmark: 76 scored questions (39 primary + 37 extension; the 8 unanswerable questions are excluded from metrics). Quality rows use the **final top-6**, meaning the six chunks production actually selects after identifier promotion, navigation exclusion and webhook scoping. The extra columns show the practical truncated configurations.

| Metric | NumPy baseline | FAISS exact | Chroma (full depth) | Chroma top-2,000 windows | FAISS exact top-2,000 windows |
|---|---:|---:|---:|---:|---:|
| Label Recall@6 | 0.8213 | 0.8213 | 0.8213 | 0.8081 | 0.8213 |
| Chunk Precision@6 (supplementary) | 0.3421 | 0.3421 | 0.3421 | 0.3399 | 0.3421 |
| MRR | 0.6425 | 0.6425 | 0.6425 | 0.6393 | 0.6425 |
| nDCG@6 (label gain) | 0.6601 | 0.6601 | 0.6601 | 0.6544 | 0.6601 |
| Hit rate@6 | 0.9211 | 0.9211 | 0.9211 | 0.9079 | 0.9211 |
| Evidence label recall (what the model receives) | 0.8914 | 0.8914 | 0.8914 | 0.8783 | 0.8914 |
| Final top-6 identical to baseline (of 132) | 132 | 132 | 132 | 122 | 122 |
| Dense-search median latency (ms, interleaved) | 13.0 | 13.9 | 98.4 | 10.8 | 3.4 |
| Dense-search p90 latency (ms, interleaved) | 20.6 | 22.2 | 120.9 | 16.0 | 5.1 |
| Hybrid ranking median (ms, interleaved) | 47.1 | 48.0 | 130.6 | 32.2 | 24.4 |
| Hybrid ranking p90 (ms, interleaved) | 65.8 | 65.7 | 160.4 | 47.4 | 38.8 |
| Retrieval + evidence assembly median / p90 (ms, per-process run) | 68.1 / 94.2 | 98.7 / 142.7 | 152.3 / 223.0 | 49.8 / 73.8 | 49.1 / 70.7 |
| Index build/import time | 0 s (existing `.npy`) | 0.075 s | 8.54 s | 8.54 s | 0.075 s |
| Cold open + first query (fresh process) | 0.047 s | 0.159 s | 1.409 s | 1.409 s | 0.159 s |
| Index memory (RSS delta, clean process) | 37.7 MB | 45.9 MB | 104.8 MB | 104.8 MB | 45.9 MB |
| Persistent index size | 39.1 MB | 39.1 MB | 67.1 MB | 67.1 MB | 39.1 MB |
| Failed checks (of 113 recorded; see §8) | 0 | 0 | 0 | 0 | 0 |
| Concurrency, 10 threads: failed calls | 0 / 840 | 0 / 840 | 0 / 840 | **3 / 840** | 0 / 840 |
| End-to-end demo: evidence checks / answer checks passed (of 6) | 6 / 6 | 6 / 4 ¹ | 6 / 6 | 6 / 6 | not run |

¹ The prompts sent to the model were **byte-identical** across all four configurations for all six questions (same SHA-256), so the two FAISS answer misses are LLM run-to-run variance, not a retrieval effect. See §6.

**Notes on the latency rows:**
- The "interleaved" rows alternate backends query by query inside one process (84 questions × 7 rounds). This is the fair comparison.
- The "per-process" rows come from separate runs. BM25 and RRF are the same code in every backend, yet their medians ranged from 12 to 22 ms between those runs. Treat cross-process differences below about ±40% as noise.
- Query embedding is identical for all backends: median 14.6 ms, p90 19.3 ms, p95 22.3 ms (127 questions × 5 reps). It is reported separately and not included above.
- Memory: the per-process runs showed a NumPy delta of 76 MB because the harness held a duplicate copy of the vectors. The clean probe (`latency_interleaved.py --memory`) loads exactly what `HybridRetriever` keeps.

## 1. Phase 1 audit: what production actually does

| Item | Finding |
|---|---|
| Production retriever | `pismo_assistant/retrieval.py` `HybridRetriever`. It imports `BM25`, `Dense`, `rrf`, `exact_rerank`, `detect_identifiers` and `rank_by_score` unchanged from the experiment's `scripts/retrievers.py`, so the production and experiment retrievers are the same code. The backend (`backend/app/services/assistant_service.py`) wraps the same `Assistant(HybridRetriever())` with timing proxies. |
| Index on disk | `pismo_full_corpus_retrieval_experiment/results/`: `chunks.jsonl` (11,026 chunks, chunk-set hash `8db472c5…7826`), `embeddings/window_vectors.npy` (25,325 × 384 float32, sha `9c8b2516…`), `window_chunk.npy` (sha `5ead2ab9…`). The live backend (:8000) reports the same chunk-set hash. The `candidates/ku_v1_1` and `ku_v1_2` indexes are **not** used by production. |
| Embedding model | `sentence-transformers/all-MiniLM-L6-v2` at revision `1110a243…`, offline, CPU. Query = raw text, `normalize_embeddings=True`, one question per call. |
| Windows | 1,000 characters with a stride of 800, prefixed by the KU title and heading path. Up to 5 windows per chunk; every chunk has at least 1. The mapping is monotone. All vectors are unit-norm (0.9999999–1.0000001). 175 windows have duplicate vectors. |
| Similarity | Cosine as a dot product on L2-normalised vectors. Chunk score = max over its windows. The dense ranking covers **all 11,026 chunks** (ties broken by chunk id). |
| BM25 | Okapi, k1 = 1.5, b = 0.75. Tokens are words plus whole compound identifiers. Only chunks with a positive score are ranked. |
| Fusion | Weighted RRF, BM25 : dense = 2 : 1, k = 60, over the full lists, then stable exact-identifier promotion. |
| Final selection | Top 6 (`TOP_K`), skipping navigation sections. Webhook scoping over-fetches 6 extra chunks and drops data-platform chunks for client-webhook questions. Evidence expansion adds named operations, linked operations, events, lifecycle notes, the error catalogue, the removal register and procedure steps. |
| Environment | Windows 11 Enterprise 10.0.26300; Intel i5-1135G7 (4 cores / 8 threads); 16.9 GB RAM (about 2.9 GB free during the runs: the backend, database and frontend dev server were running); Python 3.11.0; numpy 1.26.4; faiss-cpu 1.13.1 (8 OpenMP threads; no `*_NUM_THREADS` variables set); sentence-transformers 5.1.2; torch 2.2.1+cpu. |
| Chroma | chromadb 1.3.5 was installed globally but fails to import (`opentelemetry-exporter-otlp-proto-grpc` 1.38.0 vs `opentelemetry-sdk` 1.39.1). The global install was not touched. |

## 2. How the requirements were met

No benchmark harness existed before this run, so every item below was implemented here (in this folder). Existing assets were reused rather than duplicated: no question or label was written or changed. The only new inputs are five unlabelled edge-case queries (`EDGE_QUESTIONS` in `bench_lib.py`), used for behaviour checks only.

| # | Requirement | Status |
|---|---|---|
| 1 | Production retriever reproduces its existing rankings | **Implemented, passed.** `step0_reproduce.py` matched the stored top-20 for all 84 questions in `results/per_question_rrf_bm25_2to1_exact.json` and the stored top-10 for all 94 questions in `docs/audit_runs/retrieval_final.json`. The run stops on any mismatch. One evidence set (D2) differs from the 21 Oct audit, as expected: the 22 Oct integration scoping now removes a data-platform chunk from that client-webhook question. |
| 2 | Reuse existing evaluation assets, keep labelled and unlabelled separate | **Implemented.** Labelled: `BENCHMARK.json` 43 + 41 (hash `ea20581c…` checked), the audit's DG01–DG10 (via `audit_retrieval.resolve_diagnostic`), and `regression_webhook_auth_v2.json` (15 questions, file sha checked; 13 scored, because RW2-X02 and RW2-X08 carry no labels by design). Unlabelled: 12 probe questions, the 6 `verify_demo.QUESTIONS` (scored only by their own evidence and answer predicates) and the 8 unanswerable benchmark questions. Unlabelled questions get overlap and behaviour checks, never metrics. |
| 3 | Reuse `metrics.py`, `labels.py`, paired bootstrap | **Implemented.** `label_hits`, `label_recall_at`, `ndcg_at` and `mrr` from `scripts/metrics.py` (with k = 6); `chunk_satisfies` and `label_key` from `scripts/labels.py`; `bootstrap_diff` from `scripts/run_experiment.py` (2,000 paired resamples, seed 20261021). |
| 4 | Use the project's label definitions; don't call label recall "passage recall" | **Implemented.** Reported as *label* Recall@6, MRR and label-gain nDCG@6. Chunk Precision@6 is reported separately as a supplementary binary measure. Chunk-level recall is **not** reported: several labels legitimately match very broad chunk sets (D5's label matches 235 chunks), so "share of relevant chunks in the top 6" would be meaningless. Graded relevance does not exist in these assets, so nDCG uses the project's label-gain definition. |
| 5 | Chroma full ranking vs top-100/500/2,000, and the effect on RRF | **Implemented** (§4). Exact FAISS at the same depths was added as a control, to separate truncation effects from HNSW approximation. |
| 6 | Reuse vectors and mapping; validate Chroma and FAISS scores against NumPy | **Implemented.** Neither index was re-embedded. Window id `w%05d` = row of `window_vectors.npy`; the Chroma metadata carries `chunk_id`, `chunk_index` and `window_ordinal`. For identical window ids, the largest score difference against `V @ q` was 1.19e-7 for FAISS and 5.96e-7 for Chroma. Stored vectors matched exactly for FAISS and to within 1e-6 for Chroma. The window→chunk mapping matched for all 25,325 Chroma windows. |
| 7 | Same top-6, navigation exclusion, promotion, scoping and expansion for every method | **Implemented by construction.** `BackendRetriever` subclasses production `HybridRetriever` and replaces only the dense-ranking line; evidence comes from production `Assistant.evidence`. The NumPy adapter reproduced production's full ranking and evidence on all 127 questions. Per-question invariants are checked for every configuration (§8). |
| 8 | Report the transfer/balance coverage gap | **Reported** (§7). No labels were added, so nothing needed freezing. |
| 9 | Chroma in a separate venv; no shared changes | **Implemented** at `%USERPROFILE%\.venvs\pismo_chroma_bench`. The first attempt inside this folder failed on the Windows 260-character path limit; that partial venv (created by this run) was deleted. Windows Application Control blocked the venv's `grpcio` 1.84.1 DLL, so the venv pins `grpcio==1.76.0`, the build the global environment already loads under the same policy. Packages: `venv_freeze.txt` (this folder), `pip check` clean. |

## 3. Retrieval quality

### Dense-only, BM25-only and hybrid (benchmark, n = 76)

| List | Label R@6 | MRR (depth 100) | nDCG@6 | Hit@6 |
|---|---:|---:|---:|---:|
| BM25 only (identical for every backend) | 0.6996 | 0.5672 | 0.5616 | 0.8158 |
| Dense only: NumPy = FAISS exact (all depths) = Chroma full | 0.5965 | 0.5167 | 0.4940 | 0.6974 |
| Dense only: Chroma @500 / @2000 | 0.5965 / 0.5965 | 0.5165 / 0.5167 | 0.4940 / 0.4940 | 0.6974 / 0.6974 |
| Dense only: Chroma @100 | 0.5636 | 0.4864 | 0.4642 | 0.6579 |
| Hybrid ranking (before navigation exclusion): NumPy = FAISS = Chroma full | 0.8015 | 0.6340 | 0.6459 | 0.8947 |
| Hybrid ranking: Chroma @2000 | 0.7884 | 0.6326 | 0.6403 | 0.8816 |
| **Final top-6: NumPy = FAISS = Chroma full** | **0.8213** | **0.6425** | **0.6601** | **0.9211** |

Dense-only quality survives truncation (Chroma @500 and @2000 are almost unchanged), yet the hybrid ranking still drops. The losses come from fusion: chunks lose their dense term in RRF (§4).

Every metric for every list type and configuration, overall and per question, is in `out/aggregate_metrics.csv` and `out/per_query_metrics.csv`.

### Per set (final top-6: label R@6 / MRR / nDCG@6 / evidence label recall)

| Config | primary (n=39) | extension (n=37) | diagnostic (n=10) | webhook v2 (n=13) |
|---|---|---|---|---|
| numpy = faiss_flat = chroma_full | 0.7842 / 0.6175 / 0.644 / 0.844 | 0.8604 / 0.6689 / 0.6771 / 0.9414 | 0.6 / 0.5167 / 0.5084 / 0.9 | 0.6923 / 0.4936 / 0.5544 / 0.6923 |
| faiss_flat@100 | 0.7714 / 0.6154 / 0.6406 / 0.8312 | 0.8739 / 0.6689 / 0.683 / 0.9414 | unchanged | 0.6154 / 0.4808 / 0.527 / 0.6154 |
| faiss_flat@500 | 0.7842 / 0.6162 / 0.6429 / 0.844 | unchanged | unchanged | unchanged |
| faiss_flat@2000 | unchanged | unchanged | unchanged | unchanged |
| chroma@100 | 0.7201 / 0.5855 / 0.6116 / 0.7799 | 0.8739 / 0.6464 / 0.6723 / 0.955 | 0.5 / 0.4167 / 0.4084 / 0.9 | 0.6154 / 0.5192 / 0.5554 / 0.6154 |
| chroma@500 | 0.7585 / 0.6077 / 0.63 / 0.8184 | unchanged | unchanged | 0.6154 / 0.4679 / 0.517 / 0.6154 |
| chroma@2000 | 0.7585 / 0.6111 / 0.6329 / 0.8184 | unchanged | unchanged | unchanged |

### Per category (benchmark, final top-6 label Recall@6)

| Category | n | NumPy / FAISS / Chroma full | FAISS @100 | Chroma @100 | Chroma @500 | Chroma @2000 |
|---|---:|---:|---:|---:|---:|---:|
| Authentication and security | 3 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 |
| Cross-KU workflows | 12 | 0.819 | 0.819 | 0.861 | 0.819 | 0.819 |
| Endpoint discovery | 11 | 0.773 | 0.727 | 0.727 | 0.773 | 0.773 |
| Errors and troubleshooting | 9 | 0.898 | 0.898 | 0.898 | 0.898 | **0.787** |
| Events and webhooks | 10 | 0.65 | 0.65 | 0.65 | 0.65 | 0.65 |
| Lifecycle and changelog | 14 | 0.714 | 0.75 | 0.714 | 0.714 | 0.714 |
| Missing or ambiguous | 3 | 0.833 | 0.833 | **0.5** | 0.833 | 0.833 |
| Rate limits and support | 3 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 |
| Request and response fields | 8 | 1.0 | 1.0 | 0.875 | 0.875 | 1.0 |
| Transfers and payments | 3 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 |

FAISS @500 and @2000 match the baseline in every category. Categories have 3–14 questions, so a single question moves a category by 0.07–0.33.

### Paired bootstrap vs NumPy (benchmark, n = 76): difference [95% CI]

| Config | final R@6 | final MRR | final nDCG@6 | evidence label recall |
|---|---|---|---|---|
| faiss_flat | 0 [0, 0] | 0 [0, 0] | 0 [0, 0] | 0 [0, 0] |
| chroma_full | 0 [0, 0] | 0 [0, 0] | 0 [0, 0] | 0 [0, 0] |
| faiss_flat@100 | 0 [−0.020, +0.020] | −0.001 [−0.010, +0.007] | +0.001 [−0.009, +0.010] | −0.007 [−0.020, 0] |
| faiss_flat@500 | 0 [0, 0] | −0.001 [−0.002, 0] | −0.001 [−0.002, 0] | 0 [0, 0] |
| faiss_flat@2000 | 0 [0, 0] | 0 [0, 0] | 0 [0, 0] | 0 [0, 0] |
| chroma@100 | −0.026 [−0.072, +0.007] | **−0.027 [−0.060, −0.003]** | −0.019 [−0.046, +0.004] | −0.026 [−0.072, +0.007] |
| chroma@500 | −0.013 [−0.040, 0] | −0.005 [−0.015, 0] | −0.007 [−0.021, 0] | −0.013 [−0.040, 0] |
| chroma@2000 | −0.013 [−0.040, 0] | −0.003 [−0.010, 0] | −0.006 [−0.017, 0] | −0.013 [−0.040, 0] |

No configuration improves meaningfully on the baseline (the largest point gain is FAISS @100's nDCG +0.001). The only interval that excludes zero is Chroma @100's MRR, which is a regression. With n = 76, an interval touching zero still means "a few questions lost evidence": see §5.

### Unlabelled questions (probes, demo, unanswerable; n = 28)

Mean top-6 overlap with the baseline: FAISS exact and Chroma full 1.0 (28 of 28 identical); @2000 0.994 (27 of 28) for both libraries; FAISS @500 0.946; Chroma @500 0.941; FAISS @100 0.941; Chroma @100 0.917 (17 of 28 identical). All 6 `verify_demo` evidence checks pass for every configuration.

## 4. Why truncated dense lists change the hybrid ranking

Production fuses two complete rankings: BM25 over every chunk with a positive score, and dense over **all 11,026 chunks**. Each chunk's score is

score = 2 / (60 + BM25 rank) + 1 / (60 + dense rank)

A store queried for its top-N windows returns only some chunks: about 78 chunks for 100 windows, 349 for 500, and 1,298 for 2,000. Every chunk outside that list loses its dense term entirely. That term is worth less than 1/(60 + N_chunks): up to 0.0072 at @100 and 0.00074 at @2,000. The top-6 fused scores lie around 0.03–0.05 and are often separated by less than that, so chunks reorder. Chunks with no BM25 match and no dense hit drop out of the fused list altogether: its mean length falls from 11,026 to about 4,200–4,550. Identifier promotion is unaffected except for one question at @100, where the promoted set shrank because a matching chunk was no longer in the fused list.

Measured effect with exact truncation (FAISS), isolating truncation alone:

- **@100:** 41 of 132 top-6 sets changed. Two relevant chunks were lost (A3 lost its hold-funds evidence; RW2-04 lost `parsing-the-jwt`) and two were gained (EXT-H02, E6). Net label recall is unchanged; evidence label recall −0.007.
- **@500:** 28 top-6 sets changed, with one MRR change (C4: 0.25 → 0.20).
- **@2000:** 10 top-6 sets changed, with no label-metric change.

Chroma adds HNSW approximation on top of truncation. With default `ef_search = 100` (`ef_construction = 100`, `max_neighbors = 16`), its top-N window lists recalled 93.2% (min 64%) of the exact top-100, 96.8% (min 88.4%) of the top-500 and 98.6% (min 95.8%) of the top-2,000. A full-depth query (`n_results = 25,325`) returned every window with exact scores, which is why `chroma_full` is identical to NumPy. Larger `ef_search` values were not tested.

## 5. Every quality change, explained

Each change below is a labelled question whose final top-6 or evidence metrics changed against the baseline. "Exact twin" means FAISS at the same depth: if it matches Chroma, truncation is the cause; if not, HNSW approximation is. All 177 changed (configuration, question) pairs, including unlabelled ones, are in `out/differences.csv`.

| Config | Question | Change (baseline → config) | Cause |
|---|---|---|---|
| chroma@2000 | C4 "requests rejected with HTTP 429" | R@6 1.0 → 0; lost `KU-SUP-rate-limiting` (replaced by an EIP error-code chunk) | HNSW miss; exact @2000 keeps it |
| chroma@500 | B4 "body field must match x-…" | R@6 1.0 → 0; lost the 2 October 2026 changelog part | HNSW miss |
| chroma@500 | RW2-04 "What does the kid claim mean?" | R@6 1.0 → 0; lost `verifying-webhook-requests … parsing-the-jwt`; Pix and BACS "claim" operations took its place | HNSW miss (exact @500 keeps it; exact @100 loses it) |
| chroma@500 | RW2-06 "webhook body-hash" | MRR 0.5 → 0.33 | HNSW |
| chroma@500 / faiss@500 | C4 | MRR 0.25 → 0.20 | Truncation (exact twin identical) |
| chroma@100 | A3, B4, G2, DG10, RW2-04 | R@6 → 0 each: hold-funds, changelog, rate-limiting, EHLD error catalogue, JWT parsing lost | Truncation and HNSW (A3 and RW2-04 also fail at exact @100) |
| chroma@100 | C2, EXT-H02 | MRR drops (1.0 → 0.5; 1.0 → 0.17) | HNSW |
| chroma@100 | C1, E6, EXT-I04, RW2-06 | Gains: nDCG up; EXT-I04 R@6 0.5 → 1.0 | Same reordering, in the favourable direction |
| faiss@100 | A3, RW2-04 losses; E6, EXT-H02 gains | as above | Truncation |

Every loss traces to the dense list losing a chunk ranked between about 100 and 2,000. None comes from a scoring, mapping, navigation, scoping or promotion error: all those invariants passed (§8).

## 6. End-to-end (live OpenAI)

**Setup.** Run in-process through the production `Assistant.answer`: model `gpt-5-mini`, reasoning effort `low` (the `OPENAI_REASONING_EFFORT` the backend sends), the production prompt and citation validation. The 6 demo questions were sent once each per configuration, sequentially. The HTTP API was **not** used, because it writes sessions and messages to the development PostgreSQL database.

The prompt hash (SHA-256 of the messages) was identical across all configurations for every question. For example, Q1 = `79762c72…` and Q6 = `9cdf5a7b…` in every configuration.

| Config | Q1 | Q2 | Q3 | Q4 | Q5 | Q6 | Answer time per question (s) |
|---|---|---|---|---|---|---|---|
| numpy | answered ✔ (citation warning: historical claim not marked) | answered ✔ | answered ✔ | answered ✔ | answered ✔ | not_documented ✔ | 5.3–11.0 |
| faiss_flat | answered ✘ (did not mark WEAM0029 as removed) | ✔ | ✔ | ✔ | ✔ | partial ✘ (presented accounts go-live as the PCI procedure; unsupported `migration_status` warning) | 5.8–11.9 |
| chroma_full | ✔ | ✔ | ✔ | ✔ | ✔ | partial ✔ | 4.0–10.4 |
| chroma@2000 | ✔ | ✔ | ✔ | ✔ | ✔ | not_documented ✔ | 4.3–8.2 |

Retrieval took 24–250 ms of each call; generation took the rest. Because the inputs were identical, the FAISS misses show **generation variance on byte-identical evidence**. They are worth tracking for Q1 (historical marking) and Q6 (the go-live near-match) independently of this decision. The live calls are not used as retrieval ground truth.

The NumPy configuration ran twice: the first run's output was hidden by a log filter, so it was re-run, which overwrote the first result file. `out/e2e_numpy.json` holds the second run. In total, 30 live answer calls were made: 6 + 6 for NumPy, 6 for FAISS and 12 for Chroma.

## 7. Limitations

- **Transfer and balance discrepancy coverage is thin.** The benchmark has 3 labelled "Transfers and payments" questions (all from the extension set), plus balance-related F3 (available vs book balance) and F4 (authorization → transaction → balance) among the cross-KU workflows. No labelled question covers transfer or balance *discrepancy troubleshooting* (for example, "the transfer succeeded but the balance did not change"), and none of the probes covers it either. The "no difference" result for that scenario rests on very few questions. Adding such questions requires labels written and hashed before any comparison run; that was not done here.
- **Small samples.** The benchmark has 76 scored questions, with 3–14 per category. Diagnostic n = 10; webhook v2 n = 13.
- **Labels from a single annotator.** The labels come from the existing frozen assets and were authored by Claude models; no independent annotator was used (see `BENCHMARK_PROVENANCE.md`). Some labels are lenient (B3, D5, A5) and some narrower than the evidence (EXT-B03, EXT-F04).
- **No graded relevance.** nDCG uses the project's label-gain definition. Chunk Precision@6 is low (0.34) partly because labels name few chunks; unlabelled chunks can still be relevant.
- **Cold-start numbers include warm OS file caches.** Flushing the cache needs admin rights.
- **Latency noise.** Measured on a laptop with the backend, database and frontend dev server running. Use the interleaved figures.
- **Not tested:** approximate FAISS indexes (HNSW, IVF; exact truncation was used as the control instead); Chroma `ef_search` tuning; Chroma client/server mode; multi-process serving; corpora larger than the current one.

## 8. Tests: what ran and the outcome

All of these ran; none was skipped silently.

| Test | Scope | Result |
|---|---|---|
| Production ranking reproduces stored rankings (requirement 1) | 84 + 94 questions | **Passed** |
| NumPy adapter = production `ranked()` (full list) and `evidence()` | 127 questions | **Passed** |
| FAISS: ntotal/d, built-from-current-vectors sha, stored vectors == production | index | **Passed** (3 checks) |
| Chroma: count, built-from sha, cosine space, window→chunk mapping (all 25,325), stored embeddings (2,000 sampled) | collection | **Passed** (5 checks) |
| Similarity == NumPy cosine for identical window ids | 84 queries × every depth | **Passed** (FAISS 1.19e-7, Chroma 5.96e-7) |
| Full-depth query returns all 25,325 windows | FAISS, Chroma | **Passed** |
| Per configuration (9 configurations × 132 questions): no navigation in the final top-6; evidence deduplicated; evidence text, KU and source refs map to the source chunk; citation labels E1…En sequential; webhook scope respected; promoted chunks contain the identifier; 6 slots filled; deterministic across 5 reps; no exceptions; empty/blank query returns no evidence | 9 × 10 checks | **Passed** (90) |
| `verify_demo` evidence checks | 9 configurations × 6 | **Passed** |
| Unknown error code, unknown operationId, unknown path | 5 edge queries × 9 configurations | No exceptions; deterministic |
| Concurrency, 10 threads (5 trials × 168 calls) | numpy, faiss_flat, faiss@2000, chroma_full, chroma@2000 | **Chroma @2000 failed 3 of 840 calls** (`KeyError: '<uuid>CollectionQueryEvent'`, raised inside Chroma's query-event telemetry even with `anonymized_telemetry=False`). All others: 0 failures. The earlier per-process concurrency run also hit this error at 10 threads. |
| Existing suites, re-run unchanged | `pismo_assistant/tests`; experiment `tests/` | **171 passed**; **95 passed** |
| End-to-end, live OpenAI (§6) | 4 configurations × 6 questions | Ran; 0 generation errors |
| End-to-end through the HTTP API | — | **Not run** (would write to the dev PostgreSQL database) |

The recorded checks are listed in `out/checks.csv` (113 rows, all passed). The concurrency failure is recorded in `out/latency_interleaved_chroma.json` and `out/run_chroma.json`.

## 9. Safety record

- **Production untouched.** No production code, configuration, `.env`, embeddings, chunk index, BM25 index or database was modified, and the backend was not restarted. After the run, `window_vectors.npy`, `window_chunk.npy` and `chunks.jsonl` still have their audited hashes, and `/api/health` reports the same index.
- **Writes confined.** All writes went to this folder (`out/`, including `out/faiss/` and `out/chroma_db/`) and to `%USERPROFILE%\.venvs\pismo_chroma_bench`. The only files modified today outside this folder are `frontend/package-lock.json` and `frontend/node_modules/.package-lock.json`, at 09:51, before this run began; they were not touched by this benchmark.
- **No secrets logged.** The OpenAI key was read by the production code and is never logged or stored.
- **Removing the benchmark.** Delete this folder's `out/` and `%USERPROFILE%\.venvs\pismo_chroma_bench`. Both were created by this run only.

## 10. Reproduce

From this folder (`CH` = `%USERPROFILE%\.venvs\pismo_chroma_bench\Scripts\python`):

```powershell
$env:HF_HUB_OFFLINE='1'; $env:TRANSFORMERS_OFFLINE='1'
python -B -s step0_reproduce.py                     # requirement 1, query vectors, embedding latency (~90 s)
python -B -s build_indexes.py --backend faiss       # out/faiss/flat_ip.index (refuses to overwrite)
& $CH -B -s build_indexes.py --backend chroma       # out/chroma_db (refuses to overwrite)
python -B -s run_backend.py --backend numpy         # ~2 min
python -B -s run_backend.py --backend faiss         # ~6 min
& $CH -B -s run_backend.py --backend chroma         # ~9 min
python -B -s latency_interleaved.py --backend faiss
& $CH -B -s latency_interleaved.py --backend chroma
python -B -s latency_interleaved.py --backend numpy --memory; python -B -s latency_interleaved.py --backend faiss --memory
& $CH -B -s latency_interleaved.py --backend chroma --memory
python -B -s analyze.py
python -B -s report_tables.py > out/report_tables.md
python -B -s e2e.py --backend numpy                 # live OpenAI calls
python -B -s e2e.py --backend faiss --configs faiss_flat
& $CH -B -s e2e.py --backend chroma --configs chroma_full chroma@2000
```

Venv: `python -m venv %USERPROFILE%\.venvs\pismo_chroma_bench`, then `pip install chromadb==1.3.5 numpy==1.26.4 psutil pyyaml python-dotenv openai==2.51.0 grpcio==1.76.0` (full list in `venv_freeze.txt`).

Outputs in `out/`:

| File | Contents |
|---|---|
| `executive_summary.csv` | Executive comparison table |
| `aggregate_metrics.csv` | Every metric by configuration and set |
| `per_query_metrics.csv` | Per configuration and question: metrics and final top-6 chunk ids |
| `per_category_metrics.csv` | Metrics by benchmark category |
| `bootstrap_vs_numpy.csv` | Paired bootstrap differences against the baseline |
| `differences.csv` | Every configuration/question pair that differs from the baseline |
| `latency.csv`, `latency_interleaved_*.json` | Latency by stage and the interleaved comparison |
| `checks.csv` | All recorded checks |
| `run_*.json` | Full rankings (top-100 dense, BM25 and hybrid), evidence, timings per repetition, concurrency |
| `e2e_*.json` | Answers, citations and warnings from the live runs |
| `step0_reproduce.json`, `memory_*.json`, `analysis.json` | Reproduction check, memory probes, combined analysis |
