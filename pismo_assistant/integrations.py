"""Integration scoping: keep client-webhook questions from being answered with data-platform event-delivery evidence.

Two Pismo integrations document near-identical JWT verification with different configuration: client webhooks
(docs/get-started/verifying-webhook-requests.md: `https://<Production Domain>/v1/certs`) and the data-platform HTTP event
delivery (docs/data-and-reporting/pismo-data-platform-http-integration-guide-beta.md: `https://prod.pismo.io/v1/certs`).
Pismo itself calls the second an "HTTP webhook (beta)" (setting-up-real-time-event-delivery.md), so the word "webhook"
alone does not name an integration.

Evidence identity comes from chunk provenance (source_path / ku_sources), never from chunk text. Question scope comes
from the question text, and only narrows evidence when the question names client webhooks and nothing of the
data-platform delivery. The reverse direction is not filtered: the data-platform guide itself refers readers to the
webhook verification guide (line 100). Unknown or mixed sources are never excluded.
"""
import re

from . import config

CLIENT_WEBHOOKS = "client_webhooks"
DATA_PLATFORM_DELIVERY = "data_platform_event_delivery"

# Source files that document the data-platform event delivery only (reviewed 2026-10-22).
INTEGRATION_SOURCES = {
    "docs/data-and-reporting/pismo-data-platform-http-integration-guide-beta.md": DATA_PLATFORM_DELIVERY,
    "docs/data-and-reporting/setting-up-real-time-event-delivery.md": DATA_PLATFORM_DELIVERY,
}

DATA_PLATFORM_TERMS = re.compile(r"data[ -]?platform|event[ -]hub|event deliver(?:y|ies)|real[ -]?time events?|deliver(?:ed|s)? events?"
                                 r"|http (?:webhook|integration)|kafka|confluent|\bsqs\b|\bsns\b|eventbridge|event stream", re.I)
WEBHOOK = re.compile(r"\bweb[ -]?hooks?\b", re.I)


def question_scope(question):
    """The integrations a question names: {CLIENT_WEBHOOKS}, {DATA_PLATFORM_DELIVERY}, both, or none."""
    q = question or ""
    scope = set()
    if DATA_PLATFORM_TERMS.search(q):
        scope.add(DATA_PLATFORM_DELIVERY)
    if WEBHOOK.search(re.sub(r"http\s+web[ -]?hooks?", " ", q, flags=re.I)):
        scope.add(CLIENT_WEBHOOKS)
    return scope


def chunk_integration(chunk):
    """The integration a chunk documents, from its provenance; None when unknown or when its sources are mixed."""
    src = chunk.get("source_path")
    paths = [src] if src else list(chunk.get("ku_sources") or [])
    found = {INTEGRATION_SOURCES.get(p) for p in paths}
    return found.pop() if len(found) == 1 and None not in found else None


def evidence_integration(evidence):
    """Same as chunk_integration, for an Evidence item (its source_refs carry the paths)."""
    found = {INTEGRATION_SOURCES.get(r.get("path")) for r in evidence.source_refs or []}
    return found.pop() if len(found) == 1 and None not in found else None


def excluded_integrations(question):
    """Integrations whose evidence must not support an answer to this question (empty set = no narrowing)."""
    if not config.ENABLE_INTEGRATION_SCOPE:
        return set()
    return {DATA_PLATFORM_DELIVERY} if question_scope(question) == {CLIENT_WEBHOOKS} else set()
