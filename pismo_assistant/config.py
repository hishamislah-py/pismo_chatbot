"""Paths and settings for the Pismo assistant demo pipeline.

The retrieval index is the frozen output of pismo_full_corpus_retrieval_experiment/ (chunks + MiniLM window embeddings),
built only from the approved knowledge units in pismo_knowledge_units_migration/knowledge_units/. Nothing here writes to
those folders.
"""
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EXPERIMENT = os.path.join(ROOT, "pismo_full_corpus_retrieval_experiment")
EXPERIMENT_SCRIPTS = os.path.join(EXPERIMENT, "scripts")
RESULTS = os.path.join(EXPERIMENT, "results")
CHUNKS_PATH = os.path.join(RESULTS, "chunks.jsonl")
CORPUS_SUMMARY_PATH = os.path.join(RESULTS, "corpus_summary.json")
EMBEDDINGS_DIR = os.path.join(RESULTS, "embeddings")

# Retrieval configuration recommended by the experiment (RESULTS.md section 8): hybrid RRF, BM25:semantic = 2:1, k = 60,
# followed by exact-identifier promotion. Not re-tuned here.
RRF_WEIGHTS = (2.0, 1.0)
TOP_K = 6                 # retrieved chunks passed to the generator
# KU navigation sections hold no answer content (KU header, heading lists, source/URL tables, lists of other KU ids,
# heading-only boilerplate). They stay in the index but are skipped when filling the TOP_K evidence slots
# (audit 2026-10-21: they occupied evidence slots in 32 of 94 benchmark questions). Set False to restore old behaviour.
EXCLUDE_NAV_FROM_TOP_K = True
NAV_SECTIONS = ("Topics covered", "Source references", "Related knowledge units",
                "Current implementation guidance (source content, verbatim)", "Change record (source content, verbatim)")
MAX_LINKED_OPERATIONS = 3  # additive: operation chunks linked from retrieved guide chunks
ENABLE_ERROR_CATALOGUE_LOOKUP = True   # audit fix 2: error code in question -> its error-catalogue row
ENABLE_REMOVAL_REGISTER_LOOKUP = True  # audit fix 3: removed endpoint named in question -> its removal-register row
MAX_REGISTER_ROWS = 2      # removal-register rows added when the question names a removed endpoint or API
MAX_SUMMARY_OPERATIONS = 2 # operations matched by their exact spec summary phrase in the question
LINK_FROM_TOP = 3         # only the top-3 retrieved chunks (verbatim guide/changelog text) seed link expansion
MAX_EVENT_CHUNKS = 2       # additive: "Events emitted" chunks for operations already in the evidence
MAX_LIFECYCLE_CHUNKS = 3   # additive: lifecycle warnings of KUs already in the evidence
MAX_PROCEDURE_STEPS = 3    # additive: step sections of a retrieved procedure overview (only KUs that declare one)
# Questions about client webhooks only never receive data-platform event-delivery evidence (pismo_assistant/integrations.py;
# audit 2026-10-22: the data-platform production certificates URL was given as the webhook one). False restores old behaviour.
ENABLE_INTEGRATION_SCOPE = True
SCOPE_OVERFETCH = 6        # extra ranked hits fetched so that excluded chunks are replaced from the same ranking

ENV_FILE = os.path.join(ROOT, ".env")
try:  # settings from the project .env; real environment variables take precedence
    from dotenv import load_dotenv
    load_dotenv(ENV_FILE, override=False)
except ImportError:
    pass

OPENAI_MODEL = os.environ.get("OPENAI_MODEL") or "gpt-5-mini"
OPENAI_TIMEOUT_S = float(os.environ.get("OPENAI_TIMEOUT_S") or "60")


def ensure_experiment_on_path():
    if EXPERIMENT_SCRIPTS not in sys.path:
        sys.path.insert(0, EXPERIMENT_SCRIPTS)
