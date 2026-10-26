# Full retrieval and chunking audit: Pismo Client Implementation & Ramp-Up Assistant

Date: 21 October 2026. Retrieval and evidence assembly only: **no OpenAI calls were made** in this audit.

**Status: fully audited within the defined scope**, which is:

- the frozen 84-question benchmark (43 primary and 41 extension questions);
- 10 diagnostic questions;
- chunk construction statistics over all 11,026 chunks;
- end-to-end traces for representative questions.

It is **not** a claim that the system is defect-free. Thirteen questions still fail or pass only partially (§5), and answer quality was not re-measured here.

## 1. What was inspected

| Area | Location |
| --- | --- |
| Retrieval | `pismo_assistant/retrieval.py`: `HybridRetriever.ranked` (new; the logic is unchanged), `search`, `verify_index`. BM25 + MiniLM, RRF 2:1, exact-identifier promotion, reused from `pismo_full_corpus_retrieval_experiment/scripts/retrievers.py` |
| Evidence assembly | `pismo_assistant/evidence.py`: `assemble`, `OperationIndex`, `matched_operations` |
| Settings | `pismo_assistant/config.py` (TOP_K = 6) |
| Pipeline | `pismo_assistant/pipeline.py`, `generation.build_messages` |
| Chunking | `pismo_full_corpus_retrieval_experiment/scripts/corpus.py` (`parse_sections`, `chunk_ku`, `split_lines`) and `results/chunks.jsonl` |
| Benchmark | `pismo_full_corpus_retrieval_experiment/BENCHMARK.json`, its hash `ea20581c…` checked before every run, and label semantics in `scripts/labels.py` |
| KUs and source mapping | `pismo_knowledge_units_migration/knowledge_units/` (read only) and the chunk `source_refs` |

**Not modified:**

- the KUs and the source fingerprint `7080b549…`;
- the benchmark questions and labels;
- the chunk index and the embeddings;
- the experiment code.

Nothing was rebuilt or installed, and no files were deleted.

## 2. Method

`python -B -s -m pismo_assistant.audit_retrieval --tag <name> [--compare <json>]` runs every question through **the assistant's own code path**:

1. `retriever.ranked()`, the full hybrid ranking;
2. `retriever.search()`, the 6 evidence slots;
3. `evidence.assemble()`, the evidence the model receives.

It scores the frozen gold labels with the benchmark's own matching rule (`labels.py`), and reports:

- **Evidence label recall:** the share of a question's labels satisfied by the evidence actually sent to the model. This is the main measure.
- **All labels:** every required source present.
- **R@5, R@10 and MRR** over the raw ranking.
- **Navigation chunks** occupying evidence slots.
- **Near-matches:** the benchmark's distractor patterns.
- **Safety signals:** a lifecycle signal for lifecycle-sensitive questions, and the "not documented" statement for unanswerable ones.

The **diagnostic set** has 10 questions (DG01–DG10), written for this audit before any fix and labelled separately (`DIAGNOSTIC` in `audit_retrieval.py`). It covers natural-language operation names, operationIds, paths, required fields, operation→event, webhook troubleshooting, removed functionality, multi-KU workflows and an error code inside a sentence.

Every change was measured with the same command before and after (`docs/audit_runs/retrieval_*.json`).

## 3. Baseline findings

| Set | Scored | Pass | Partial | Fail | Evidence label recall | All labels | R@5 | MRR |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Primary | 39 | 26 | 9 | 4 | 0.801 | 0.667 | 0.720 | 0.603 |
| Extension | 37 | 30 | 4 | 3 | 0.860 | 0.811 | 0.806 | 0.667 |
| Diagnostic | 10 | 9 | 0 | 1 | 0.900 | 0.900 | 0.600 | 0.521 |

Unanswerable questions (G1, G3, G4, G7, EXT-U01–U04) are not scored. Their near-matches are listed in §6.

## 4. Defects found and fixed

| # | Defect, with evidence | Root cause (category) | Fix | Measured effect |
| --- | --- | --- | --- | --- |
| 1 | **KU navigation chunks took evidence slots in 32 of 94 questions.** These are the KU header, "Topics covered", "Source references", "Related knowledge units" and heading-only "source content, verbatim" chunks. EXT-C01: 4 of 6 slots, with the endpoint list at rank 7. E3: 3 of 6, with the mTLS guide at rank 10. Inspection confirmed these sections contain only boilerplate, heading lists, URL/hash tables or KU-ID lists | **Evidence assembly / top-k selection (5).** The generated KU sections are indexed like content and rank well because they repeat the KU's key terms | `config.EXCLUDE_NAV_FROM_TOP_K = True` with `config.NAV_SECTIONS`. `retrieval.search` skips these chunks when filling the 6 slots. They **stay in the index**, so no rebuild was needed, and the flag restores the old behaviour. "Purpose and scope", "Operations in this unit", "API operations referenced", "Events" and "Lifecycle status" remain eligible | E3 and EXT-C01 go from fail to pass. Navigation chunks in evidence go from 0.58 to 0 per question. 0 regressions |
| 2 | **Error-code questions lacked the code's catalogue row.** Exact lookup promotes every chunk containing the code, so dozens of API response examples outrank the one catalogue row (C2: rank 22; C5: rank 12) | **Missing relationship (6)** | `evidence.assemble` step 0b: an error code in the question adds its row chunk from the error catalogue (`OperationIndex.error_rows`). Deterministic and additive | C2 and C5 go from partial to pass. 0 regressions |
| 3 | **Questions naming a removed endpoint lacked the removal-register row** (ranks 7–15). EXT-H03's evidence held only current Cards API content: a lifecycle-safety risk | **Missing relationship (6)** | Step 0c: `removed_endpoint_rows` matches the 24 parsed register rows on: <ul><li>an endpoint name of 2+ words as a whole phrase;</li><li>a path, with escapes and placeholder names ignored;</li><li>"<API> API", only with a lifecycle word in the question.</li></ul>Up to 2 rows are added (`config.MAX_REGISTER_ROWS`) | G5, EXT-A05, EXT-H02 and EXT-H03 go to pass. EXT-H03's lifecycle signal goes from absent to present. 0 regressions |

**Rejected change (experiment only, code removed):** a per-KU cap on the 6 slots.

- Cap 2: 4 regressions (E3, F1, F2, EXT-C01) for 1 gain.
- Cap 3: 1 regression (F1), 0 gains.

Many questions legitimately need several chunks from one KU.

**Final results** (`docs/audit_runs/retrieval_final.json`):

| Set | Pass | Partial | Fail | Evidence label recall | All labels | Change from baseline |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| Primary | **30** | 6 | 3 | **0.857** | **0.769** | +4 pass, recall +0.056 |
| Extension | **34** | 2 | 1 | **0.941** | **0.919** | +4 pass, recall +0.081 |
| Diagnostic | 9 | 0 | 1 | 0.900 | 0.900 | unchanged |

R@5, R@10 and MRR over the raw ranking are unchanged by design: no ranking code changed, only slot selection and assembly. No question regressed against the baseline.

## 5. Remaining failures and root causes

These were not fixed; they are recommendations. Details are in `docs/audit_runs/failure_classification.json`.

| Q | Outcome | Cause | Detail |
| --- | --- | --- | --- |
| A7 | fail | 4 ranking (vocabulary) | "moves money" vs "transfer": guide at rank 58, operation at rank 764. Same failure as the raw-source experiment |
| DG02 | fail | 3+4 | Paraphrase "send money … to another": `post-transfers` is not in the top 100. Summary matching is phrase-exact by design |
| D4 | fail | 4 | "Same event twice / duplicates" vs `event_id` delivery semantics: guide at rank 23 |
| D6 | fail | 1+4 | Payload fields are not documented (SG-01). The catalogue row is at rank 36, behind guides' generated "Events" sections |
| EXT-H01 | fail | **2 chunk construction** | Right KU at rank 1, but the dated row sits in a 3,808-character schedule-table chunk (`::p01`). The KU's detailed section (`::p05`) matches better and lacks the date |
| A2 | partial | 4 | The PCI card migration operation is at rank 54; the non-PCI one is retrieved ("card number" vs "pan") |
| A3 | partial | 4+6 | "Set aside / court order" vocabulary. The hold-funds guide is at rank 4, but link expansion reads only the top 3, so the block operation (rank 381) is not attached |
| C1, E4, F2, D1, EXT-I01, EXT-I04 | partial | 4 | A second required source ranks 7–23 (changelog mentions, a sibling section of the same KU, a second guide) |

**Cause tally across the 13 remaining failures:** ranking/vocabulary 11; chunk construction 1 (EXT-H01); missing source content 1 (D6, together with ranking); missing relationship 1 (A3, together with ranking).

## 6. Chunking quality (Audit B)

The measurements below cover all 11,026 chunks. An observation is counted as a defect only where it has a demonstrated impact.

| Observation | Measurement | Impact | Verdict |
| --- | --- | --- | --- |
| Operation contracts split | 564 of 999 operations span more than one chunk (105 span more than 5; maximum 23) | — | Observation |
| Events table separate from the operation | In 251 of the 321 operations with an events table, the table is not in the operation's first chunk; it often sits inside an error-example chunk | D1/Q4 (the transfer event) | **Defect, mitigated in assembly** by summary/operationId matching and events-table attachment (earlier fix). Not rechunked |
| Request-body chunks without method/path in their text | 300 of 301 | None: all 301 carry the operation heading in `heading_path`, which reaches the model as the `Section:` line | Not a defect |
| Tables split with the header repeated | 704 split parts begin with a repeated table header | None observed | Working as designed |
| Large table chunk dilutes a single row | Removal-schedule chunk of 3,808 characters | EXT-H01 | **Defect, not fixed** (needs row-level chunking and an index rebuild; see recommendations) |
| Tiny chunks (<100 characters) | 771, mostly "Lifecycle status", "Authentication", "Response 200" | None in the evidence of failing questions | Observation |
| Duplicate boilerplate text | 339 groups, 2,238 chunks | 6 evidence slots across 2 questions, both passing | Observation |
| Deprecation flags | 45 deprecated-operation chunks flagged inline | — | OK |
| Guide lifecycle warnings in separate chunks | 25 "Lifecycle status" chunks carry warnings | Attached by assembly step 3 when their KU is in the evidence. EXT-I01 has a lifecycle signal | OK in the cases tested |
| Historical content | All 411 changelog chunks are flagged `historical_changelog` | — | OK |

**Unanswerable near-matches still in evidence** (benchmark distractors):

- G3 and EXT-U03: accounts go-live;
- G4: "Ordering dimensions";
- G7: `MIGR00001`/`MIGR00002`;
- EXT-U01: `GetMarketPlaceByIdV2`, alongside the curated "Not documented" statement;
- EXT-U04: the changelog link.

The "not documented" statements for D6 and EXT-U02 are not retrieved. Retrieval cannot resolve these cases; they depend on answer-time behaviour.

## 7. Retrieval-to-evidence integration (Audit D)

Traces are in `docs/audit_runs/traces.json`. For each case: query → full ranking → 6 slots → assembled evidence → the exact prompt from `generation.build_messages`.

| Case | Result |
| --- | --- |
| C3 (success: `WEAM0029` in a sentence) | 2 exact-identifier promotions put the October 2026 changelog at E1–E2 |
| EXT-C01 (fixed: navigation) | The endpoint list is now E3, with the listed operations attached by link expansion |
| C2 (fixed: error catalogue) | 25 chunks contain `EIBA0005`; the catalogue row is now added as E7 |
| D1 (fixed earlier) | Operation and events table at E7–E8; the payments-data-events guide is still missing (ranking) |
| A7, EXT-H01 (remaining) | Failures upstream, in ranking and chunk construction |

In **all six traces every evidence passage reached the prompt verbatim** (`all_evidence_text_verbatim_in_prompt = true`). Evidence size across the 94 questions: median 8 items and 18.5k characters; maximum 13 items and 33.5k characters.

## 8. Tests

| Suite | Result |
| --- | --- |
| `pismo_assistant/tests` | **58 passed**, 0 failed, 0 skipped (49 before this audit; 9 regression tests added) |
| `pismo_full_corpus_retrieval_experiment/tests` | **38 passed** |
| Demo evidence (`verify_demo --mock`) | All six demo questions keep their expected evidence, with the full text in the prompt. This was a mocked run with no generation; the saved live verification record was kept unchanged |

Regression tests added:

- **Fix 1:** `test_search_skips_navigation_chunks` (also tests the off-switch and rank preservation), `test_search_keeps_relationship_sections`, `test_navigation_chunks_do_not_take_evidence_slots` (EXT-C01, E3).
- **Fix 2:** `test_error_code_lookup_adds_catalogue_row`, `test_error_code_question_includes_catalogue_row` (C2, C5).
- **Fix 3:** `test_removed_endpoint_lookup_by_name_path_and_api` (including the lifecycle-intent gate and negative cases), `test_removed_endpoint_questions_include_register_row` (EXT-H03, EXT-A05, EXT-H02, G5).

Four kinds of check, kept distinct:

- the **frozen benchmark**, with labels unchanged;
- the **diagnostic set**, authored for this audit;
- **unit tests**, with synthetic data;
- **live answer tests**, which were not run: no OpenAI calls were made.

## 9. Recommendations (not implemented)

1. **Vocabulary gap** (A7, DG02, D4, A2, A3): add domain synonym expansion (money movement → transfer; set aside/freeze → hold funds) or evaluate a stronger embedder on the same frozen benchmark.
2. **Row-level chunks for the removal schedule and register** (EXT-H01). This needs a documented rebuild of `chunks.jsonl` and the embeddings, then a re-frozen benchmark mapping, which is out of scope here.
3. **Link expansion depth:** allow the top 5 instead of the top 3 for guide chunks (A3). Measure for noise first.
4. **Event questions:** attach the event catalogue row (and its "not documented" statement) when the question names an event slug or asks about an event payload (D6, EXT-U02).
5. **Prompt size:** evidence reaches 33k characters. Consider trimming large API-reference chunks to their relevant subsections if latency or cost matters.

## 10. Reproduce

```powershell
cd C:\Users\artlptp263user\Downloads\pismo_claude_code_handoff
$env:HF_HUB_OFFLINE='1'; $env:TRANSFORMERS_OFFLINE='1'
python -B -s -m pismo_assistant.audit_retrieval --tag final --compare docs/audit_runs/retrieval_baseline.json
python -B -s -m pytest pismo_assistant/tests -q -p no:cacheprovider
cd pismo_full_corpus_retrieval_experiment; python -B -s -m pytest tests -q -p no:cacheprovider; cd ..
```

**To reproduce the baseline:** set these three flags in `pismo_assistant/config.py` to `False`, then run the audit with `--tag baseline_check`:

- `EXCLUDE_NAV_FROM_TOP_K` (fix 1);
- `ENABLE_ERROR_CATALOGUE_LOOKUP` (fix 2);
- `ENABLE_REMOVAL_REGISTER_LOOKUP` (fix 3).

Each fix can also be switched off on its own.

**Machine-readable results** (no secrets):

- `docs/audit_runs/retrieval_{baseline,fix1_nav,fix2_errors,fix3_register,final}.json`: per question, the top-10 ranking with titles and relevance, the evidence set, per-label recall, rank, the safety signals and the outcome;
- `docs/audit_runs/retrieval_exp_cap{2,3}.json`: the rejected experiments;
- `docs/audit_runs/failure_classification.json`;
- `docs/audit_runs/traces.json`.
