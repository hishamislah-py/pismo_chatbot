# Pismo assistant: retrieval-to-answer pipeline (demo)

The pipeline answers a question in five stages. Each stage lives in its own module and can be tested on its own.

| Stage | Module | What it does |
| --- | --- | --- |
| Retrieval | `retrieval.py` | Hybrid RRF (BM25 2:1 MiniLM, k = 60) plus exact-identifier promotion, over the frozen KU chunk index in `pismo_full_corpus_retrieval_experiment/results/`. On start-up it verifies that the index contains KU chunks only and that `knowledge_units/` is unchanged (corpus manifest hash) |
| Evidence assembly | `evidence.py` | Takes the top 6 retrieved chunks and adds, in order: <ul><li>operations the question names;</li><li>operations linked from the top 3 guide passages;</li><li>each operation's "Events emitted" table;</li><li>lifecycle warnings</li></ul>Every evidence item carries its exact chunk text and its source references |
| Generation | `generation.py` | Calls OpenAI Chat Completions in JSON mode. The system prompt requires answers from the evidence only, no invented API details, `[E#]` citations, and explicit `not_documented`, `partial` or `conflicting_sources` statuses |
| Citation validation | `citations.py` | Checks that every cited label exists and has a KU ID, a title and source paths with URLs. Flags API-like tokens that are not found in the cited passages |
| Orchestration and CLI | `pipeline.py`, `__main__.py` | Returns a result dict: status, answer, citations (KU, section, source path and URL), warnings, and the evidence list |

## Run

From the project root (`Downloads\pismo_claude_code_handoff`), with Python 3.11. Everything needed is already installed: openai 2.51.0, sentence-transformers, numpy and PyYAML.

```powershell
$env:HF_HUB_OFFLINE='1'; $env:TRANSFORMERS_OFFLINE='1'
# The OpenAI key and model are read from the project-root .env file (python-dotenv): OPENAI_API_KEY, OPENAI_MODEL
# (default gpt-5-mini). Keep the key only in .env; never paste it into code, docs, the terminal history or chat.
python -B -s -m pismo_assistant "How do I release funds that I previously held on an account?"
python -B -s -m pismo_assistant --evidence-only "What does WEAM0029 mean?"   # no OpenAI call
python -B -s -m pismo_assistant --json "..."                                 # machine-readable result
```

Exit codes: 0 means OK; 2 means a generation error (configuration, API or malformed output). The status and error appear in the output.

## Test

```powershell
$env:HF_HUB_OFFLINE='1'; $env:TRANSFORMERS_OFFLINE='1'
python -B -s -m pytest pismo_assistant/tests -q -p no:cacheprovider -rxX
```

The tests use a fake OpenAI client and make no network calls.

## Demo verification

`python -B -s -m pismo_assistant.verify_demo` does four things:

1. runs both test suites;
2. runs the six demo questions (live if `.env` holds a key, otherwise mocked);
3. prints a terminal summary;
4. refreshes `docs/DEMO_READINESS_VERIFICATION.md`.

## Known limitations

- **No answerability judge.** Abstention relies on the model following the prompt. `test_pci_go_live_limitation_model_can_answer_from_near_match` shows that a wrong answer drawn from the accounts go-live near-match would pass every deterministic check.
- **Citation checks are deterministic only.** They cover source mapping, claim-level API tokens, operation alignment and historical marking. `semantic_support_verified` is always `False`.
- **Operation matching needs exact names.** An operation is identified by its operationId or by its exact summary phrase ("create a transfer" → "Create transfer"). Paraphrases still depend on retrieval rank.
- **Retrieval is unchanged from the experiment.** Low-ranked passages can be off-topic (for example the WEAM0029 results 3–6).
