# Pismo full-corpus retrieval experiment

This experiment compares BM25, dense semantic retrieval (MiniLM) and hybrid RRF retrieval over the **complete Pismo knowledge-unit collection**: 623 KUs, split into 11,026 chunks. Only `../pismo_knowledge_units_migration/knowledge_units/` is searchable. Every other artefact is used only for verification.

**Headline (primary benchmark, 39 scored questions):**

| Method | Recall@5 | Recall@10 | MRR |
| --- | ---: | ---: | ---: |
| BM25 | 0.598 | 0.701 | 0.552 |
| Semantic (all-MiniLM-L6-v2) | 0.474 | 0.500 | 0.424 |
| Hybrid RRF, equal | 0.656 | 0.836 | 0.577 |
| Hybrid RRF, BM25 2:1 | 0.720 | 0.810 | 0.571 |
| *RRF 2:1 + exact lookup (enhancement)* | 0.720 | 0.810 | 0.603 |

`RESULTS.md` covers everything else: extension-set results, breakdowns, significance tests, unanswerable and lifecycle findings, and the recommendation.

## Contents

| Path | What it is |
| --- | --- |
| `EXPERIMENT_PLAN.md` | Inputs, isolation, chunking, methods and evaluation rules |
| `CORPUS_MANIFEST.csv` | One row per indexed KU: path, sha256, type, lifecycle, chunk count |
| `BENCHMARK.json`, `BENCHMARK.sha256` | The frozen benchmark: the 43-question primary set and the 41-question extension set, with verified KU mappings |
| `BENCHMARK_PROVENANCE.md` | Where each question and label came from, how labels were mapped and checked, and ambiguous labels |
| `benchmark_inputs/extension_questions_v1.json` | The authored extension questions (input to `build_benchmark.py`) |
| `RESULTS.md` | The results |
| `VALIDATION_REPORT.md` | Artefact inspection, isolation, risk register, sanity checks, tests |
| `FAILURE_ANALYSIS.md` | Failures by cause: retrieval, missing evidence, labels, contradictions, chunking, unanswerable |
| `DECISION_LOG.md` | Decisions, the hybrid verdict, the value of exact lookup, what to retest |
| `scripts/` | The pipeline (standard library plus numpy, PyYAML and sentence-transformers, all already installed; nothing was installed) |
| `tests/` | 38 pytest tests |
| `results/` | `chunks.jsonl`, `corpus_summary.json`, `embeddings/`, `per_question_<config>.json` (6 configurations), `aggregate_metrics.json`, `unanswerable_and_lifecycle.json`, `semantic_sanity.json`, `failure_annotations.json`, `run_log.json` |

## Reproduce

Run these commands from this directory. There are no network calls; the embedder loads from the local Hugging Face cache, `sentence-transformers/all-MiniLM-L6-v2` at revision `1110a243fdf4706b3f48f1d95db1a4f5529b4d41`.

```powershell
cd C:\Users\artlptp263user\Downloads\pismo_claude_code_handoff\pismo_full_corpus_retrieval_experiment
$env:HF_HUB_OFFLINE='1'; $env:TRANSFORMERS_OFFLINE='1'
python -B -s scripts/build_corpus.py        # isolation checks, CORPUS_MANIFEST.csv, chunks (~30 s)
python -B -s scripts/build_benchmark.py     # verify labels, freeze BENCHMARK.json (~1 min)
python -B -s scripts/embed_corpus.py        # 25,325 windows; ~30 min on CPU; reuses cache if current
python -B -s scripts/semantic_sanity.py     # embedder sanity checks
python -B -s scripts/run_experiment.py      # 6 configs x 84 questions (~15 s with cached embeddings)
python -B -s -m pytest tests -q -p no:cacheprovider
```

**Expected values:**

| Item | Expected |
| --- | --- |
| Corpus manifest hash | `91b18ec7…e2cf` |
| Chunk-set hash | `8db472c5…7826` |
| Benchmark hash | `ea20581c…1cfc` |
| Tests | 38 passed |

`run_experiment.py` stops if the chunk set or the benchmark differs from the frozen hashes. If you change the chunking, run `build_benchmark.py` again so that the gold chunk IDs are resolved anew; that produces a new benchmark hash, which is expected.

The scripts read `../pismo_knowledge_units_migration/`, `../pismo_kb_release_r2/kb_corpus/` (label verification only) and `~/Downloads/pismo_retrieval_experiment_v2.zip`. They never write to any of them.

## Limitations

- **A single model** built the KUs, wrote the extension questions, mapped the labels and diagnosed the failures. There was no independent annotator.
- **Small samples** limit the conclusions: n = 39 and 37, with 3–7 questions per workflow.
- **One small embedder.** MiniLM reads at most 256 word pieces.
- **Missing pilot data.** The 59-question, 6-KU pilot was not available, so its figures are historical only.
- **Retrieval only.** Answer correctness was not measured.
