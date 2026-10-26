# Decision log

## Decisions made while setting up the experiment

| # | Decision | Reason |
| --- | --- | --- |
| D1 | Use the migration **directory** as input, because no migration ZIP exists | It was the only artefact available. Its KU set was checked against `work/ku_index.json` (equal) |
| D2 | Use the frozen 43-question v2 benchmark, read from `pismo_retrieval_experiment_v2.zip`, as the **primary** set | It is the only frozen benchmark available as a file. Its IDs, texts and labels are preserved |
| D3 | Report the 59-question, 6-KU pilot as **historical only** | No files for it exist. It was not recreated, and its scores are not compared with this run |
| D4 | Map file-based labels to KU chunks by a fixed rule (`scripts/labels.py`) instead of rewriting labels | This preserves the gold labels while acknowledging where the evidence moved |
| D5 | Chunk by heading section and API operation, with a 4,000-character budget, repeated table headers and reopened fences | The KU structure called for this, and it matches the prior v2 budget |
| D6 | Use MiniLM-L6-v2 from the local cache, offline | It is the only genuine transformer embedder available without network access or paid APIs. `instructor-base` is cached but needs an uninstalled package |
| D7 | Score each chunk by its best window (1,000 characters, 800 stride) | MiniLM reads 256 word pieces. Without windows, most of a 4,000-character chunk would be invisible to the semantic method |
| D8 | Implement BM25 directly instead of installing `rank_bm25` | It avoids a new dependency. The formula is the same Okapi form with a non-negative idf, and it is unit-tested |
| D9 | Fix every parameter in advance and do no tuning | This removes any risk of fitting to the test set. Because nothing was tuned, no development subset was needed |
| D10 | Report the exact-identifier lookup as a separate enhancement | The request requires that its contribution not be hidden inside "BM25" |

## Does BM25-weighted hybrid remain the best candidate?

**Yes. It is the best candidate for the default configuration, with one qualification.**

On the primary set (n = 39), the BM25:semantic 2:1 hybrid:

- has the highest Recall@5 (0.720), Hit@5 (0.846), nDCG@5 and KU recall@5;
- is the only configuration whose Recall@5 gain over BM25 has a bootstrap interval that excludes zero (+0.122 [+0.019, +0.231]);
- also beats BM25 on Recall@10 (+0.109 [+0.032, +0.192]).

**The qualification:** the equal-weight hybrid cannot be distinguished from it.

- Recall@5: 2:1 minus equal is +0.064 [−0.026, +0.167].
- Recall@10: 2:1 minus equal is −0.026.
- The equal-weight hybrid is ahead on the extension set (MRR 0.695 vs 0.653) and on natural-language questions.

The 2:1 weighting is justified by the identifier-heavy questions, where semantic is very weak (exact-question Recall@5 is 0.167). It is not justified by a measured advantage overall.

Neither single method wins:

- **Semantic alone** is the weakest overall, and significantly worse than BM25 at Recall@10 (−0.201 [−0.368, −0.030]). Even so, it rescues the vocabulary-mismatch questions (E6, D4, G2, EXT-E02, EXT-G01, EXT-G03).
- **BM25 alone** misses those same questions and is beaten by both hybrids at Recall@10.

This reverses the raw-source experiment, where the hybrids did *worse* than BM25. The difference comes from a stronger embedder (MiniLM, which still fails some sanity checks) and from KU-structured chunks. It also matches the direction of the historical 6-KU pilot.

## Does exact identifier lookup add value?

**Yes, a small amount, confined to exact-identifier queries, with no measured harm.**

- Primary MRR rises from 0.552 to 0.581 for BM25 and from 0.571 to 0.603 for the 2:1 hybrid.
- On exact questions only: BM25 MRR goes from 0.721 to 0.847, and hybrid MRR from 0.713 to 0.852.
- The bootstrap lower bounds are 0, meaning that on these questions it never made a ranking worse.
- It changed the hybrid's recall not at all, and natural-language questions are unchanged by construction.
- Clearest case: C3 `WEAM0029`, from rank 9 to rank 1.

It is not a substitute for fusion. EXT-F04 `EHLD0016` stays at rank 26 with exact lookup, because 35 unlabelled API chunks contain the code; fusion ranks the catalogue row 1. **Keep it as a final promotion stage on top of the hybrid.**

## What to retest after the migration issues are addressed

| Fix | Questions to retest | Expected effect to verify |
| --- | --- | --- |
| Lifecycle warnings attached to every chunk of an affected KU, or inlined into the verbatim block's chunks (SC-01) | EXT-I01, G5, E2, EXT-H03 | A warning present in the top 10 for every method |
| Removal register and deprecation schedule as row-level chunks with headers | EXT-H01, E4, E5, EXT-H03, EXT-A05 | The dated row at rank ≤ 5 |
| KU navigation sections (topics covered, source references, related KUs) excluded from the index or merged into content | EXT-C01, D6, EXT-U02 | The content chunk outranks navigation |
| Operation → event relationship lookup | D1, D6 | The "Events emitted" table reached from the operation |
| Event catalogue "not documented" statements surfaced for payload questions (SG-01) | D6, EXT-U02 | The statement in the top 10 |
| Stronger embedder (more than 256 tokens; better at identifiers and paraphrase) | A7, S3–S5, error-code questions | The semantic and fusion gains reconfirmed |
| Migration MD-08: convert MDX/HTML | all; compare BM25 noise | Neutral or better |
| A second annotator for the extension set and the label mapping | all | The labels and diagnoses confirmed independently |

After each change:

1. rebuild the chunks;
2. re-verify and re-freeze the benchmark;
3. rerun all six configurations;
4. compare with the paired bootstrap against this run's `results/`.
