# Failure analysis

**Scope.**

- Every scored question that missed Hit@5 in at least one of the four primary configurations.
- Every unanswerable, conflict and lifecycle-sensitive question.

The diagnoses were made by hand from the rankings, the gold chunk IDs and the chunk text. They were made by the same model that built the KUs (no independent reviewer). The machine-readable version, with a note for each question, is `results/failure_annotations.json` (45 questions).

| Category | Questions | Count |
| --- | --- | ---: |
| Retrieval ranking failure | A3, A4, A7, B2, B4, C1, C2, C3, C4, C5, D1, D4, E3, E4, E5, E6, F4, G2, EXT-A01, EXT-E02, EXT-F01, EXT-F03, EXT-G01, EXT-G03, EXT-H03, EXT-I06 | 26 |
| Missing evidence in KUs | D6 | 1 |
| Ambiguous or incorrect gold labels | B3, D5 (too broad); EXT-B03, EXT-F04 (too narrow) | 4 |
| Source contradictions | G5, E2, EXT-A05, EXT-I01 | 4 |
| Chunking or document structure | EXT-C01, EXT-H01 (and D6 secondarily) | 2 |
| Unanswerable | G1, G3, G4, G7, EXT-U01–U04 | 8 |

## 1. Retrieval ranking failures

The evidence is in a KU chunk and the label is sound, but the method ranks it below 5.

**Semantic misses identifiers.** This is the largest group: A4, B2, C1, C2, C5, EXT-A01 and EXT-F01, at semantic ranks 12–74.

- On the primary set, semantic Recall@5 is 0.167 for exact-identifier questions and **0.00 for error-code questions**.
- MiniLM's word-piece vocabulary splits `EIBACC0379` or `post-transfers-cancel` into fragments with little meaning, and the surrounding sentence dominates the embedding.
- Lexical methods rank these at 1–4, so fusion recovers them.

**BM25 misses vocabulary mismatches or falls into lexical traps.** Cases: D4, E6, G2, EXT-E02, EXT-G01 and EXT-G03, at BM25 ranks 7–90.

- E6: "notice" matches the `MaturityNotice` schema, so the deprecation-strategy guide falls to rank 44.
- G2: "transfers endpoint" pulls in transfer chunks.
- Semantic ranks all six at 1–5, and the hybrids at 1–4.
- **This is where fusion pays off.**

**Every method fails** on two questions:

- **A7.** "Moves money from one account to another" has no lexical overlap with "transfer", and MiniLM does not bridge it (rank 22). This persists from the raw-source experiment, so it is a property of the query, not of the migration.
- **D1.** "Which event is generated when I create a transfer" needs a relationship: the `post-transfers` operation, then its events. Lexically, "create a transfer" first matches transfer-*schedule* operations (rank 23). Similarity search will not reliably reach this; an operation → event lookup will.

**Long multi-topic chunks** affect B4 and E3. Each answer is one sentence in a 3,000–4,000-character changelog chunk (`x-account-id`, mTLS), and other chunks about the same topic outrank it. B4 improves from BM25 rank 8 to hybrid 2:1 rank 3.

**Exact lookup fixes identifier dilution.** For C3, `WEAM0029` inside a sentence moves from BM25 rank 9 to rank 1.

## 2. Missing evidence in KUs

**D6** asks for the payload fields of the account-status-change event. The source corpus does not document payloads (migration issue SG-01), and the KU states this ("not documented in the available source corpus"). This is a coverage gap in the source, not a retrieval failure.

It is aggravated by structure: every guide KU has a generated "Events" section, and those sections outrank the catalogue row (catalogue first relevant rank 28–54). The catalogue KU's statement is never in the top 10.

No other question failed because evidence was missing from or distorted in the KUs: every label resolved to KU evidence during benchmark verification.

## 3. Ambiguous or incorrect gold labels

| Q | Problem | Direction |
| --- | --- | --- |
| B3 | The inherited regex `202` matches `2026`, so any October 2026 changelog chunk counts | Over-credits every method |
| D5 | A label on a 14-KU guide, with no regex | Over-credits |
| EXT-B03 | `x-cid` is defined in 5 Pix KUs; the label names only `Pix_payments.yaml` | Under-credits the hybrids (rank 5–6) |
| EXT-F04 | `EHLD0016` appears in 35 Holidays API response-400 examples that answer the question, but only the catalogue row is labelled | Under-credits BM25 and semantic (rank 25–26); fusion ranks the row 1 |

The labels were left unchanged, because the frozen benchmark is preserved and the extension labels were frozen before the run.

## 4. Source contradictions

- **G5** (should I use `postmarketplacesv2`?).
  - The prior raw-source experiment failed this one: the conflicting removal row was not retrieved.
  - **On the KU corpus** the curated `KU-LIFE-marketplace-endpoint-removal` chunk is rank 1 for BM25 and both hybrids, and four guide lifecycle-status warnings are in the hybrid top 10.
  - The register-row *label* itself ranks 12 for the 2:1 hybrid, but the curated KU already contains that evidence.
- **E2** (successor of Link merchant).
  - BM25's top 5 are seller-guide chunks that still link the removed endpoint.
  - The hybrids put the curated KU and the lifecycle warnings at ranks 4–10.
  - No successor is documented (SG-02).
- **EXT-A05** (an endpoint both on the removal register and in the current spec, SC-03).
  - Every method ranks the spec operation 1; BM25 and the hybrids miss the register row in the top 10.
  - **The KU mitigates this:** the operation chunk includes "Lifecycle note: … also appears in the removed-endpoints list … conflicting sources", so the top-1 chunk carries both sides.
- **EXT-I01** (steps to plan and create a seller marketplace). **This is the open risk.**
  - The hybrid and semantic top 10 are all seller-guide chunks. Neither the curated KU nor any guide lifecycle-status chunk appears; BM25 reaches the curated KU at rank 10.
  - The guides' verbatim steps still instruct `postmarketplacesv2`.
  - A generator given these chunks would present removed behaviour as current.
  - **Cause:** the KU puts its warning in a separate "Lifecycle status" section, which becomes its own chunk.

## 5. Chunking and document-structure problems

- **EXT-C01** (which endpoints need an account-specific token).
  - Every method ranks the right KU first (KU recall 1.0).
  - But the KU's generated navigation chunks ("Topics covered", "Source references", the intro) match the question's words better than the long verbatim endpoint lists, so the content chunks fall to rank 6–10.
  - Navigation sections act as decoys.
- **EXT-H01** (when will the installment advancement endpoints be removed).
  - The dated row sits in a 3,808-character schedule table chunk that also contains about 25 other rows.
  - The same KU's detailed per-API section (`::p05`) matches the query better but has no date.
  - Right KU at rank 1, wrong chunk.
  - Row-level chunks with the header repeated would fix this.
- **Large KUs (MD-07).** No failure was traced to the seven KUs over 100 KB. They were cut into 34–69 chunks of at most 4,000 characters, and no chunk exceeds the budget.
- **Generated "Events" sections** decoy event questions (D6, EXT-U02).

## 6. Unanswerable questions

| Q | Retrieved | Risk for a future generator |
| --- | --- | --- |
| G3, EXT-U03 (PCI card go-live) | The accounts go-live operation is in the top 5 for **every** method. BM25's top-1 score (64.6 for G3) is far above the answerable median (25.8) | **High:** a confident near-match |
| G7 (`MIGR-0400`) | `MIGR00001`/`MIGR00002` look-alikes in the semantic and hybrid top 5 | Medium |
| G4 (event ordering) | "Ordering dimensions" (debt discharge) | Medium |
| G1 (uptime SLA) | Operations-status and security pages; "99.999%" not in the top 5 | Medium |
| EXT-U01 (marketplace successor) | The curated KU's "Not documented" statement at rank 1–2 | Low, provided the generator uses the statement |
| EXT-U02 (event payload) | Payment guides; the catalogue statement is not retrieved | Medium |
| EXT-U04 (operation emitting `apex-entry-creation-1`) | Accounting guides plus the changelog; nothing states the gap | Medium |

In both BM25 and semantic, the top-1 scores of unanswerable questions fall inside the answerable range. No score threshold separates them.

## 7. What to re-test after the fixes

- **Lifecycle warnings as chunk metadata or inline text:** EXT-I01, G5, E2, EXT-A05 and EXT-H03.
- **Row-level chunks for the register and schedule:** EXT-H01, E4, E5 and EXT-H03.
- **Navigation sections handled differently:** EXT-C01.
- **Operation → event lookup:** D1, D6 and EXT-U02.
- **A stronger embedder:** A7, S3, S4, S5 and the semantic identifier misses.
