# Results: full-corpus retrieval over the Pismo knowledge units

Run date: 21 October 2026. All numbers come from files in `results/`: `aggregate_metrics.json`, `per_question_*.json`, `unanswerable_and_lifecycle.json` and `semantic_sanity.json`. Every run was deterministic and single-pass, and the parameters were fixed before any retrieval run (see `DECISION_LOG.md`).

## 1. Corpus, benchmark and model

| Item | Value |
| --- | --- |
| Searchable corpus | `pismo_knowledge_units_migration/knowledge_units/` only |
| KU files indexed | **623** (623 unique KU IDs, 623 unique content hashes, identical to the migration's KU index) |
| Files rejected by the isolation check | 1 (`knowledge_units/.generated_by_build_kus`, not Markdown) |
| Chunks | **11,026** (median 758 characters, p90 3,826, maximum 4,000; 2,142 chunks are parts of a split section) |
| Corpus manifest hash | `91b18ec7f7072ec19d76fba4b286622b43321f6683bf8a8030411e71c393e2cf` |
| Chunk-set hash | `8db472c58e43022e7a4c8b6240c836476bad08a809cc5a76ee406efaa9a77826` |
| Benchmark content hash (`BENCHMARK.sha256`) | `ea20581c88fe163fcc484d86ecc9468b55c5488554378e8c57859f6f4d5c1cfc` |
| Primary benchmark | 43 frozen questions from `pismo_retrieval_experiment_v2.zip` (`benchmark_questions_v2.json`, sha `71a969f3…04da`): 39 scored, 4 unanswerable |
| Extension set | 41 new questions (`EXT-*`): 37 scored, 4 unanswerable; always reported separately |
| Embedding model | `sentence-transformers/all-MiniLM-L6-v2`, revision `1110a243fdf4706b3f48f1d95db1a4f5529b4d41`, safetensors sha `53aa5117…d9db` |
| Embedding details | 384 dimensions; cosine similarity on L2-normalised vectors; maximum 256 word pieces per window |
| Windowing | 1,000-character windows with an 800-character stride, each prefixed with the KU title and heading path; 25,325 windows; a chunk's score is its best window. Encoding took 1,786 s on CPU, offline, from the local Hugging Face cache |
| BM25 | Okapi, k1 = 1.5, b = 0.75, idf ln(1 + (N − df + 0.5)/(df + 0.5)); the tokenizer keeps compound identifiers |
| RRF | k = 60; score = Σ w_m/(60 + rank_m); weights 1:1 and 2:1 (BM25:semantic) |
| Tests | 38 passed, 0 failed (`pytest tests`) |

The 6-KU, 117-chunk, 59-question pilot is **not available** as files anywhere on this machine, so its results appear in §7 as historical figures only.

## 2. Primary benchmark (39 scored questions)

| Method | Recall@5 | Recall@10 | MRR | nDCG@5 | nDCG@10 | Hit@5 | KU recall@5 | KU recall@10 | All-required@5 | All-required@10 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| BM25 | 0.598 | 0.701 | 0.552 | 0.525 | 0.561 | 0.769 | 0.727 | 0.829 | 0.32 | 0.44 |
| Semantic (MiniLM) | 0.474 | 0.500 | 0.424 | 0.396 | 0.406 | 0.590 | 0.605 | 0.694 | 0.24 | 0.28 |
| Hybrid RRF, equal | 0.656 | **0.836** | 0.577 | 0.554 | **0.620** | 0.795 | 0.793 | **0.883** | 0.40 | **0.64** |
| Hybrid RRF, BM25 2:1 | **0.720** | 0.810 | 0.571 | **0.579** | 0.617 | **0.846** | **0.836** | 0.855 | **0.44** | 0.60 |
| *Enhancement:* BM25 + exact lookup | 0.624 | 0.707 | 0.581 | 0.557 | 0.588 | 0.795 | 0.752 | 0.846 | 0.32 | 0.44 |
| *Enhancement:* RRF 2:1 + exact lookup | 0.720 | 0.810 | **0.603** | **0.605** | **0.644** | 0.846 | 0.844 | 0.872 | 0.44 | 0.60 |

How to read the columns:

- **Recall@k:** the share of a question's gold labels satisfied by a chunk in the top k.
- **MRR:** reciprocal rank of the first relevant chunk, measured to depth 100.
- **nDCG:** label-level; each chunk earns gain only for labels not already covered.
- **KU recall:** the same as Recall@k but measured over distinct KUs.
- **All-required:** every gold label covered. It applies to the 25 multi-label questions only.

**Paired bootstrap** on the primary set (2,000 resamples, seed 20261021). Each cell gives the difference followed by its 95% interval.

| Comparison | Recall@5 | Recall@10 | MRR |
| --- | --- | --- | --- |
| RRF 2:1 − BM25 | **+0.122** [+0.019, +0.231] | **+0.109** [+0.032, +0.192] | +0.020 [−0.052, +0.091] |
| RRF equal − BM25 | +0.058 [−0.071, +0.186] | **+0.135** [+0.051, +0.231] | +0.025 [−0.074, +0.125] |
| Semantic − BM25 | −0.124 [−0.286, +0.051] | **−0.201** [−0.368, −0.030] | −0.128 [−0.282, +0.029] |
| RRF 2:1 − RRF equal | +0.064 [−0.026, +0.167] | −0.026 [−0.103, +0.039] | −0.006 [−0.059, +0.044] |
| BM25 + exact − BM25 | +0.026 [0, +0.077] | +0.006 [0, +0.019] | +0.029 [0, +0.081] |
| RRF 2:1 + exact − RRF 2:1 | 0 | 0 | +0.032 [0, +0.083] |

With n = 39, the conclusions the data supports are these:

- Both hybrids beat BM25 on Recall@10. The 2:1 hybrid also beats it on Recall@5.
- Semantic alone is worse than BM25 at Recall@10.
- The two hybrids cannot be told apart.
- No method differs from another on MRR.

## 3. Extension set (37 scored questions, reported separately)

| Method | Recall@5 | Recall@10 | MRR | nDCG@10 | Hit@5 | KU recall@10 | All-required@10 (n = 12) |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| BM25 | 0.752 | 0.842 | 0.584 | 0.612 | 0.838 | 1.000 | 0.667 |
| Semantic | 0.685 | 0.779 | 0.615 | 0.615 | 0.784 | 0.923 | 0.500 |
| RRF equal | **0.820** | 0.869 | **0.695** | **0.696** | **0.919** | 0.964 | 0.500 |
| RRF 2:1 | 0.806 | **0.887** | 0.653 | 0.674 | 0.892 | 1.000 | 0.667 |
| *BM25 + exact* | 0.752 | 0.842 | 0.590 | 0.618 | 0.838 | 1.000 | 0.667 |
| *RRF 2:1 + exact* | 0.806 | 0.887 | 0.667 | 0.684 | 0.892 | 1.000 | 0.667 |

The extension set is easier than the primary set: its questions name topics that are close to KU titles. It was also written by the same model that built the KUs, so it measures coverage of the corpus, not independent difficulty.

## 4. Breakdown by query type and workflow

**By query type** (primary set; Recall@5 / MRR):

| Method | Exact identifiers (n = 9) | Natural language (n = 30) |
| --- | --- | --- |
| BM25 | 0.648 / 0.721 | 0.583 / 0.501 |
| Semantic | **0.167 / 0.256** | 0.567 / 0.474 |
| RRF equal | 0.731 / 0.630 | 0.633 / **0.561** |
| RRF 2:1 | 0.843 / 0.713 | **0.683** / 0.529 |
| BM25 + exact | 0.759 / 0.847 | 0.583 / 0.501 (unchanged) |
| RRF 2:1 + exact | **0.843 / 0.852** | 0.683 / 0.529 (unchanged) |

The extension set shows the same pattern. On exact-identifier questions (n = 9), semantic reaches only 0.556 / 0.503, while RRF 2:1 + exact reaches 0.833 / 0.741. On natural-language questions (n = 28), the equal-weight hybrid is best at 0.798 / 0.703.

**By workflow** (Recall@5; columns are BM25 / semantic / RRF equal / RRF 2:1):

| Workflow | Primary | Extension |
| --- | --- | --- |
| Endpoint discovery | 0.64 / 0.43 / 0.57 / **0.71** (n = 7) | 0.88 / 0.50 / 0.88 / 0.88 (n = 4) |
| Request and response fields | 0.70 / 0.40 / 0.70 / **0.90** (n = 5) | 0.83 / 1.00 / 1.00 / 0.67 (n = 3) |
| Errors and troubleshooting | 0.57 / **0.00** / 0.52 / 0.72 (n = 5) | 0.75 / 0.25 / 1.00 / 1.00 (n = 4) |
| Events and webhooks | 0.42 / 0.58 / 0.42 / 0.50 (n = 6) | 0.75 / 0.88 / 0.88 / 1.00 (n = 4) |
| Lifecycle and changelog | 0.57 / 0.57 / **0.79** / 0.64 (n = 7) | **0.71** / 0.57 / 0.50 / 0.50 (n = 7) |
| Cross-KU workflows | 0.75 / 0.58 / 0.83 / 0.83 (n = 6) | 0.81 / 0.64 / 0.81 / 0.81 (n = 6) |
| Missing or ambiguous (scored subset) | 0.50 / 0.83 / 0.83 / 0.83 (n = 3) | — |
| Authentication and security | — | 0.67 for all methods (n = 3) |
| Transfers and payments | — | 1.00 for all methods (n = 3) |
| Rate limits and support | — | 0.33 / 1.00 / 1.00 / 1.00 (n = 3) |

Two further patterns:

- **Errors and troubleshooting:** with exact lookup, the primary set reaches 0.77 for BM25 + exact, and MRR reaches 0.85 for RRF 2:1 + exact.
- **Lifecycle-sensitive questions:** on the primary set (n = 12), Recall@10 is 0.75 for BM25, 0.54 for semantic and 0.96 for both hybrids. On the extension set (n = 7), BM25 leads with Recall@5 0.62, against 0.41 for both hybrids, because dated register and changelog rows are lexical matches.
- **Questions touching a known migration issue:** n = 4 on the primary set and 6 on the extension set. The numbers are too small to rank methods (see `aggregate_metrics.json`).

## 5. Unanswerable questions and lifecycle safety

Here retrieval is judged only on what evidence it returns. Whether a generated answer would be correct is not scored.

| Question | What the corpus lacks | What retrieval returned (all four primary methods unless stated) |
| --- | --- | --- |
| G3, EXT-U03 | PCI card go-live | The **accounts go-live operation in the top 5** for every method, a misleading near-match. BM25's top-1 score for G3 is 64.6, against a median of 25.8 for answerable questions |
| G7 | `MIGR-0400` | Semantic and both hybrids put the look-alike codes `MIGR00001`/`MIGR00002` in the top 5 |
| G4 | An event-ordering guarantee | Lexical methods return "Ordering dimensions" (debt discharge) |
| G1 | An uptime SLA | Operations-status and security pages; the "99.999%" design goal is not in the top 5 |
| EXT-U01 | A marketplace successor | The curated KU stating "Not documented in the available source corpus" ranks 1–2 for every method. Current marketplace operations also appear in the BM25 and 2:1 top 5 |
| EXT-U02, D6 | Event payload fields | The catalogue KU that states the payload is not documented is **never in the top 10**. The top results are guides' "Events" sections |
| EXT-U04 | The operation that emits `apex-entry-creation-1` | Accounting guides and the changelog; nothing states the gap |

**Scores do not separate answerable from unanswerable questions.**

- BM25: unanswerable top-1 scores range from 13.3 to 64.6, against an answerable median of 25.8.
- Semantic: unanswerable top-1 cosines range from 0.555 to 0.798, against an answerable median of 0.663.

Abstention therefore has to come from checking the evidence, not from a score threshold.

Lifecycle and conflict questions, inspected by hand in `FAILURE_ANALYSIS.md`:

- **G5** (use `postmarketplacesv2`?): this is an improvement on the raw-source experiment. The curated `KU-LIFE-marketplace-endpoint-removal` chunk is **rank 1** for BM25 and both hybrids, and the guides' lifecycle-status warnings are in the top 10.
- **E2** (successor of "Link merchant"): BM25's top 5 are seller guides that still link the removed endpoint. The hybrids bring the register and the warnings into the top 6.
- **EXT-A05** (an endpoint that is both on the removal register and in the current spec): the spec operation is rank 1. The register row is outside the top 10 for BM25 and both hybrids. **The KU mitigates this:** the operation chunk carries an inline lifecycle note naming the conflict.
- **EXT-I01** (plain "steps to create a seller marketplace"): **risk confirmed.** For both hybrids and for semantic, every top-10 result is a seller-guide chunk. Neither the curated removal KU nor any guide lifecycle-status chunk appears, so a generator would see instructions for removed endpoints with no warning. BM25 reaches the curated KU only at rank 10.
- **EXT-H03** (Create combo card removal): the top results for semantic and the hybrids are current Cards API chunks. The register row ranks 5 for BM25 and 14–21 for the others.

## 6. Most informative successes and failures

Successes:

- **Exact identifiers with fusion or exact lookup.** C3 `WEAM0029` moves from rank 9 (BM25) to rank 1 with exact lookup. EXT-F04 `EHLD0016` moves from 26 to 1 with fusion. The other identifier questions (A1, A4, B5, C2, C5, EXT-A01, EXT-B02) are at rank 1 for BM25 or hybrid.
- **Fusion rescues vocabulary mismatches.** E6 ("notice before removing a deprecated API") goes from BM25 rank 44 to hybrid rank 2–3. G2, EXT-E02, EXT-G01 and EXT-G03 also go from BM25 rank 7–20 to hybrid rank 1–4.
- **The curated lifecycle KU works for direct lifecycle questions.** This covers G5, E1 and EXT-U01.

Failures:

- **A7, "moves money" versus "transfer".** Every method misses (BM25 not in the top 100; semantic 22; hybrids 27 and 58). This vocabulary gap persists from the raw-source experiment, and the small embedder does not close it.
- **D1, "which event is generated when I create a transfer".** Rank 23 or worse for every method. The answer is a relationship (the operation's "Events emitted" table), not a similar passage.
- **EXT-H01, the installment-advancement removal date.** The right KU is rank 1, but the dated row sits inside a 3,800-character schedule table chunk (a chunking problem).
- **EXT-C01, endpoints requiring an account token.** The right KU is rank 1 for every method, but its navigation chunks outrank the verbatim endpoint lists (a document-structure problem).
- **Semantic on identifiers.** Primary error-code Recall@5 is 0.00. Sanity check S3 (`encrypted_pan`) put the first acceptable KU at rank 16.

## 7. Comparison with earlier experiments (limitations)

| Source | Corpus and chunks | Questions and labels | BM25 R@5 / R@10 / MRR | Semantic | RRF 1:1 | RRF 2:1 |
| --- | --- | --- | --- | --- | --- | --- |
| **This run (primary)** | 623 KUs, 11,026 chunks | 39 scored of the frozen 43; labels mapped to KU chunks | 0.598 / 0.701 / 0.552 | 0.474 / 0.500 / 0.424 (MiniLM) | 0.656 / 0.836 / 0.577 | 0.720 / 0.810 / 0.571 |
| Raw-source experiment v2 (`RETRIEVAL_EXPERIMENTS.md`) | 503 raw files, chunking v2 | the same 39 questions; labels on raw files | 0.526 / 0.660 / 0.524 | 0.284 / 0.395 / 0.341 (WordLlama, 256-dim) | 0.421 / 0.502 / 0.417 | 0.462 / 0.592 / 0.494 |
| 6-KU pilot (historical, **files not available**) | 6 KUs, 117 chunks | 59 questions | 0.744 / 0.901 / 0.712 | 0.699 / 0.872 / 0.629 | 0.802 / 0.907 / 0.720 | 0.812 / 0.937 / 0.762 |

The question IDs and texts in the first two rows are the same. The corpus, the chunker, the embedder and the label-matching rule all differ (`labels.py` adapts file-based labels to KU chunks). The differences are therefore directional, not controlled.

The pilot searched 6 KUs, not 623. Its figures were not used to estimate anything here, and it should not be compared with this run.

## 8. Recommendation for the next implementation step

1. **Retriever.** Adopt **hybrid RRF (BM25:semantic 2:1, k = 60) over the KU chunks, with an exact-identifier promotion stage.** It is best or tied on Recall@5, nDCG and MRR for the primary set, and its gain over BM25 on Recall@5 and Recall@10 is significant. Equal weights are statistically indistinguishable and slightly better on natural-language questions, so keep the weight configurable and re-test.
2. **Lifecycle signal on content chunks.** Attach the KU's lifecycle warnings (removed or unresolved endpoints, the register-versus-spec conflict) as metadata to *every* chunk of an affected KU, or inline them, so that a generator receives them with the guide text. EXT-I01 shows that a separate "Lifecycle status" chunk is not reliably retrieved.
3. **Relationship lookups.** Add relationship lookups: operation → events (D1), event → catalogue row including its "not documented" statement (D6, EXT-U02), and removed endpoint → register row (EXT-A05, EXT-H03).
4. **Chunking fixes.** Make row-level chunks, with headers repeated, for the removal schedule and the register (EXT-H01). Down-weight or exclude KU navigation sections (topics covered, source references, related KUs) from the index, or attach them to the content they describe (EXT-C01).
5. **Embedder.** Re-test a stronger embedder before giving semantic retrieval more weight. MiniLM reads only 256 word pieces and handles identifiers poorly.
6. **Generation.** Generation must cite chunks and abstain when they do not contain the answer. Scores cannot detect unanswerable questions.
