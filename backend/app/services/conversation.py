"""Message exchange: persist the question, call the pipeline with session-scoped context, persist the outcome.

Transaction boundaries (two short transactions; none is open while the pipeline runs)
  1. one transaction: insert the user message, read the follow-up context, COMMIT. The session's connection goes back to
     the pool here, before any retrieval or LLM work;
  2. pipeline call (worker thread, timeout) - this step receives no database session at all;
  3. one transaction: re-check that the session still exists (it may have been deleted meanwhile), insert the assistant
     message + activity row, COMMIT. If the session is gone nothing is written and the caller gets 404.
Any exception in steps 1 or 3 rolls the transaction back before propagating. On a pipeline failure, step 3 stores an
assistant row with status "error", EMPTY content and the error kind/message in details - an accurate record of the
failure, never a fabricated answer. Each completed request writes exactly one user and one assistant row; if the request
itself is cancelled during step 2 (client disconnect), the committed question stays without an answer row.

Concurrency: send_message holds a per-session guard (session_guard.py) for the whole request, so a second message for
the same session gets SessionBusy (HTTP 409) instead of interleaving the history. Process-local; see that module.

Follow-up context (not long-term memory)
  Only prior USER questions of the SAME session are used, at most CONTEXT_MAX_PRIOR_QUESTIONS and CONTEXT_MAX_CHARS, and
  only for a referential follow-up: the message starts with a connective ("and", "what about", ...) or refers back with a
  pronoun ("it", "that", ...), AND names no API identifier of its own (error code, path, operationId). Message length
  alone never makes a follow-up. Offline retrieval checks showed contextualised retrieval is needed for real follow-ups
  ("What about events?", "Is it deprecated?": 0 relevant passages as typed) and harmful for self-contained short
  questions ("PCI card go-live steps?", "Rate limits?": the earlier topic's passages and operations were pulled in).
  Prior assistant answers are never passed. The context is appended to the question string given to the unchanged
  pipeline; the stored user message is always the text as typed. Greetings in the history are not used as context.

Routing (deterministic rules, decided before any retrieval; recorded in details.route = {outcome, reason})
  1. greeting / thanks       whole-message "hi", "thank you", ...           -> fixed reply  (response_kind "greeting")
  2. social / acknowledgement whole-message "how are you?", "got it", ...   -> fixed reply  (response_kind "social")
  3. own identifier          names an error code, path, header, snake_case/camelCase field or operationId
                                                                             -> RAG on the message as typed
  4. vague                   no content words ("yes explain more", "tell me more", "what do you mean?"):
                             asks for more AND a usable earlier topic exists -> RAG with that topic as context
                             otherwise                                       -> clarification (response_kind "clarification")
  5. referential cue         connective / pronoun / "the X part": with a usable topic -> RAG with context;
                             a bare pronoun with no topic ("Is it deprecated?")      -> clarification
  6. anything else           -> RAG on the message as typed
  Fixed replies and clarifications never search the knowledge base or call the LLM, never cite anything and carry no
  details.index. They are persisted exactly like any other exchange (status "answered" - the schema's statuses are
  answer statuses; response_kind says what it really is). A usable topic is an earlier USER question of the same session
  that is not a greeting, social message or vague continuation; only those are ever used as context. Offline checks on
  the real index: "yes explain more" as typed retrieved 6/6 unrelated incident-management chunks; resolved against an
  earlier webhook question it retrieved 4/6 webhook-verification chunks and no incident chunks.

Index version (details.index.chunk_set_hash)
  The chunk_set_hash of the in-memory index whose pipeline produced the result (null if that pipeline exposes none).
  Absent when the pipeline did not return (timeout, crash) and for fixed replies and clarifications, which never use it.

Timing (details.timings; safe numbers only, never question text)
  db_question_ms   transaction 1: insert of the user message, context read and commit
  db_context_ms    the context read inside transaction 1 (0 when the message is not a follow-up)
  pipeline_call_ms wall time of the pipeline call (= details.duration_ms); load_wait/lock_wait/pipeline and the
                   per-stage fields come from AssistantService (see timing.py)
  db_answer_ms     insert + flush of the assistant message and activity row; the final COMMIT is not included (it
                   cannot be stored in the rows it commits) and is logged instead
  total_ms         request handling up to the final commit
"""
import asyncio
import logging
import re
import time
import uuid
from collections.abc import AsyncIterator, Awaitable, Callable
from dataclasses import dataclass, field
from typing import Any

from sqlalchemy.orm import Session

from ..core.config import Settings
from ..models import Message
from ..repositories import store
from .assistant_service import AssistantService, AssistantTimeout
from .router import RouteDecision, Router
from .session_guard import SessionBusy, SessionGuard
from .streaming import CallObserver
from .timing import ms

log = logging.getLogger(__name__)

# Whole-message greetings and thanks only; matched after lower-casing, trimming surrounding punctuation/whitespace and
# collapsing inner whitespace. Kept deliberately narrow: anything that is not exactly one of these goes to the pipeline.
GREETING_RX = re.compile(r"(hi|hello|hey|hiya|good (morning|afternoon|evening))( there| all| everyone)?")
THANKS_RX = re.compile(r"(thanks|thank you|thanks a lot|thank you very much|many thanks)")
GREETING_REPLY = "Hi! I'm Pismo Assist. Ask me anything about Pismo APIs, webhooks, events or error codes."
THANKS_REPLY = "You're welcome! Let me know if you have another Pismo question."

# Whole-message social messages and acknowledgements (same normalisation as greetings). Deliberately narrow.
SOCIAL_RX = re.compile(r"how are (you|u)( doing)?( today)?|how('s| is) it going|how are things|how do you do|what'?s up"
                       r"|nice to meet you")
# The assistant's identity and purpose are application facts with fixed, approved answers - never searched in the KB.
IDENTITY_RX = re.compile(r"who are you|what are you|who am i (talking|speaking) (to|with)|what('s| is) your name|whats your name"
                         r"|introduce yourself|are you (a bot|an ai|a human|human|a person|real)|(what|who) is pismo assist")
CAPABILITY_RX = re.compile(r"what can you (help( me)? with|do)( for me)?|how can you help( me)?|what do you do"
                           r"|what can i ask( you)?|what are you able to do|what (kind|sort) of questions can i ask( you)?"
                           r"|what is this (tool|assistant|app) for")
ACK_RX = re.compile(r"(ok|okay|alright|all right|cool|great|nice|perfect|awesome|got it|understood|noted|sounds good"
                    r"|makes sense)( thanks| thank you)?")
SOCIAL_REPLY = "All good here, thanks for asking. What would you like to know about Pismo?"
IDENTITY_REPLY = ("I'm Pismo Assist, the client implementation and ramp-up assistant for Pismo. I answer questions about "
                  "Pismo APIs, integrations, webhooks, events and error codes using Pismo's approved developer "
                  "documentation, and I cite the sources behind each answer. What would you like to know?")
CAPABILITIES_REPLY = ("I can help you understand and implement Pismo: what an API operation does and which fields it needs, "
                      "what an error code means, how authentication, webhooks and events work, and how integration "
                      "workflows fit together. Answers come from Pismo's approved documentation with citations, and if "
                      "something isn't documented, I'll say so. What are you working on?")
ACK_REPLY = "Glad that helps! Let me know if you have another Pismo question."
CLARIFY_REPLY = ("What would you like me to explain more about? You can ask me about a Pismo API, integration workflow, "
                 "webhook, event, or error code.")
CLARIFY_REFERENCE_REPLY = ("I'm not sure what that refers to in this conversation. Which Pismo API, integration workflow, "
                           "webhook, event or error code do you mean?")

# ---- scope: the assistant is for Pismo implementation work only -----------------------------------------------------
# A message is out of scope when it names a clearly unrelated topic and is not substantively about Pismo work. Topic
# terms come in two tiers: STRONG terms are unambiguous (a dish, a sport, photosynthesis, a poem) and win unless the
# message also uses at least two distinct Pismo-domain terms ("Write a poem about Pismo webhooks" stays in scope, "make
# chicken biriyani for my API team lunch" does not); WEAK terms have technical uses too ("bake a signature", "cook up a
# test payment", "a recipe for retries") and only count when no domain term is present at all. A question without
# "Pismo" or "API" is never rejected for that alone ("How can I troubleshoot a failed transfer?"), an identifier on its
# own is not domain vocabulary, and context from earlier messages never rescues an unrelated request.
_OFF_TOPIC: dict[str, tuple[str, str]] = {   # topic -> (strong, weak)
    "recipes": (r"biri?yani|briyani|biryani|curry|pasta|pizza|lasagne?|omelett?e|dessert|mutton|paneer",
                r"recipes?|cook(?:ing|ed)?|bak(?:e|ing)|soup|marinate|chicken|ingredients"),
    "sports": (r"football|soccer|cricket|basketball|baseball|rugby|nba|nfl|ipl|premier league|world cup|olympics",
               r"tennis"),
    "entertainment": (r"netflix|celebrit(?:y|ies)|actors?|actress(?:es)?|lyrics",
                      r"movies?|films?|tv shows?|albums?|singers?"),
    "creative writing": (r"poems?|poetry|haiku|limerick", r"(?:write|tell) (?:me )?(?:a|an) (?:story|joke|song)|jokes?"),
    "personal or lifestyle topics": (r"horoscope|dating|girlfriend|boyfriend",
                                     r"diet|weight loss|workout|wedding|relationship advice|dogs?|puppy|kitten"),
    "general knowledge questions": (r"photosynthesis|mitochondria|dinosaurs?|volcano(?:es)?|solar system|world war|"
                                    r"theory of relativity|pythagoras",
                                    r"planets?|capital of|who invented|who won|homework|weather|climate change"),
}
_OFF_TOPIC_RX = {topic: (re.compile(rf"\b(?:{strong})\b", re.I), re.compile(rf"\b(?:{weak})\b", re.I))
                 for topic, (strong, weak) in _OFF_TOPIC.items()}
_DOMAIN_RX = re.compile(
    r"\b(?:pismo|apis?|endpoints?|webhooks?|events?|transfers?|payments?|accounts?|cards?|authenticat\w*|auth|"
    r"authori[sz]ation|tokens?|tokeni[sz]ation|jwt|oauth|headers?|requests?|responses?|errors?|transactions?|ledgers?|"
    r"balances?|onboarding|integrat\w*|sandbox|postman|statements?|loans?|credit|debit|pix|customers?|wallets?|"
    r"disputes?|chargebacks?|merchants?|issuers?|acquirers?|kyc|sdk|schemas?|payloads?|fields?|json|https?|"
    r"idempoten\w*|rate limits?|banking|bank|fees?|installments?|clearing|settlements?|3ds|mastercard|visa|"
    r"control center|earmarks?|programs? id|developer docs?|documentation)\b", re.I)
OUT_OF_SCOPE_REPLY = ("I'm designed to help with Pismo APIs, developer documentation, integrations, events, webhooks, and "
                      "related implementation questions. I can't help with {topic} or unrelated topics. What Pismo "
                      "integration question can I help you with?")


def out_of_scope_topic(text: str) -> str | None:
    """The unrelated topic a message is clearly about (e.g. "recipes"), or None. A message that stays in scope is
    answered (or abstained on) from the evidence as usual."""
    domain_terms = {m.lower() for m in _DOMAIN_RX.findall(text)}
    for topic, (strong, weak) in _OFF_TOPIC_RX.items():
        if strong.search(text) and len(domain_terms) < 2:
            return topic
    if not domain_terms:
        for topic, (_strong, weak) in _OFF_TOPIC_RX.items():
            if weak.search(text):
                return topic
    return None


CONNECTIVE_RX = re.compile(r"^\s*(and|also|what about|how about|what if|then|so|but|ok|okay)\b", re.I)
PRONOUN_RX = re.compile(
    r"\b(it|its|it's|they|them|their|the same|same one|above|previous|earlier|mentioned)\b"
    # demonstratives refer back only at the start or after a verb/preposition ("what does that mean?", "is this
    # deprecated?", "which of these"); after a noun they are relative pronouns ("funds that I previously held")
    r"|(^\s*|\b(is|are|was|were|does|do|did|can|could|should|will|would|about|for|with|of|on|in|to|from|use|call|"
    r"explain|mean|has|have|and|or)\s+)(that|this|those|these)\b", re.I)
# definite reference to part of an earlier topic: "the JWT part", "the second endpoint", "the last step"
DEFINITE_RX = re.compile(r"\bthe\s+(?:[\w-]+\s+){0,3}?(part|parts|step|steps|bit|section|one)\b"
                         r"|\bthe\s+(first|second|third|fourth|last|other|next|previous|former|latter)\b", re.I)
FOLLOWUP_RX = re.compile(f"{CONNECTIVE_RX.pattern}|{PRONOUN_RX.pattern}|{DEFINITE_RX.pattern}", re.I)

# An API identifier in the message itself makes it self-contained. The patterns mirror the retriever's exact-identifier
# detection (pismo_full_corpus_retrieval_experiment/scripts/retrievers.py ID_PATTERNS / NOT_IDENTIFIERS; copied, because
# importing pismo_assistant loads the project .env). Deliberate difference: a hyphenated slug counts only when it is a
# verb-prefixed operationId (post-transfers) or contains a digit (event slugs such as transfer-created-1), so English
# words like "step-by-step" do not make a vague message look self-contained.
_ID_PATTERNS = [re.compile(r"\b[A-Z][A-Z0-9]{1,9}[0-9]{3,6}\b"),                                  # error code
                re.compile(r"(?<![\w/])/[A-Za-z0-9{}_\-.]+(?:/[A-Za-z0-9{}_\-.]+)+"),             # path
                re.compile(r"\bx-[a-z0-9]+(?:-[a-z0-9]+)*\b", re.I),                                # header
                re.compile(r"\b[a-z][a-z0-9]*(?:_[a-z0-9]+)+\b"),                                   # snake_case
                re.compile(r"\b[a-z]+[A-Z][A-Za-z0-9]*[a-z0-9][A-Za-z0-9]*\b"),                    # camelCase
                re.compile(r"\b(?:get|post|put|patch|delete)-[a-z0-9][a-z0-9-]*\b", re.I),          # operationId
                re.compile(r"\b(?=[a-z0-9-]*\d)[a-z0-9]+(?:-[a-z0-9]+)+\b")]                        # slug with a digit
_NOT_IDENTIFIERS = {"mTLS", "eCommerce", "iOS", "macOS"}

# Words that carry no subject on their own. A message made only of these (and punctuation) is "vague".
_FILLER = frozenset("""
a about above again all also am an and any anything are as at be been bit but by can could did didn't do does doesn't
doing don't done dont else further give go going got have help here how i i'd i'm im in info information is isn't it
it's its just keep kindly know let let's lets like little lot lots me mean meant more much my need no not now of ok okay
on one or our part please pls plz point previous provide really said say saying see show so some something still sure
tell than that that's thats the them then there these they thing things this those to try understand up us very want
wanted was we well were what what's whats when where which why will with would yeah yep yes yup you your
explain explained explaining elaborate expand clarify continue detail details detailed deeper deep depth example
examples earlier last answer response
""".split())
# a vague message that asks to continue the earlier topic (as opposed to a bare "yes" / "no")
CONTINUE_RX = re.compile(r"\b(explain\w*|elaborate|expand|more|details?|detailed|continue|go on|deeper|clarify|mean|meant"
                         r"|understand|example|examples|why|how)\b", re.I)
_WORD_RX = re.compile(r"[a-z0-9]+(?:['’][a-z]+)?")

ANSWER_STATUSES = {"answered", "partial", "not_documented", "conflicting_sources", "no_evidence"}
HTTP_FOR_ERROR = {"timeout": 504, "configuration": 503, "api_error": 502, "malformed_output": 502, "internal": 500}


def _normalise(text: str) -> str:
    """Lower-case, curly apostrophes straightened, surrounding punctuation trimmed, inner , ; : ! ? . treated as spaces,
    whitespace collapsed ("Got it, thanks!" -> "got it thanks"). Used only for whole-message matches."""
    t = re.sub(r"^[\W_]+|[\W_]+$", "", text.strip().lower().replace("’", "'"))
    return " ".join(re.sub(r"[,;:!?.]+", " ", t).split())


def greeting_kind(text: str) -> str | None:
    """"greeting" / "thanks" when the whole message is just that, else None."""
    t = _normalise(text)
    if GREETING_RX.fullmatch(t):
        return "greeting"
    if THANKS_RX.fullmatch(t):
        return "thanks"
    return None


def social_kind(text: str) -> str | None:
    """"identity" ("who are you?"), "capabilities" ("what can you help me with?"), "social" ("how are you?") or
    "acknowledgement" ("got it") when the whole message is just that, else None."""
    t = _normalise(text)
    if IDENTITY_RX.fullmatch(t):
        return "identity"
    if CAPABILITY_RX.fullmatch(t):
        return "capabilities"
    if SOCIAL_RX.fullmatch(t):
        return "social"
    if ACK_RX.fullmatch(t):
        return "acknowledgement"
    return None


# a greeting or thanks at the START of a longer message ("hi who are you", "Hi, how do I verify webhooks?")
_LEADING_PLEASANTRY_RX = re.compile(
    r"^\s*(?:hiya|hello|hey|hi|good (?:morning|afternoon|evening)|thanks|thank you)(?: there| all| everyone| again)?"
    r"(?=[\s,!.:;]|$)[\s,!.:;]*", re.I)


def core_message(text: str) -> str:
    """The message without a leading greeting or thanks, when something substantive follows it. The greeting never
    causes the question to be dropped: "hi who are you" is routed as "who are you", "Hi, how do I verify webhooks?" as
    the question itself. A message that is only a greeting is returned unchanged (and routed as a greeting)."""
    rest = _LEADING_PLEASANTRY_RX.sub("", text, count=1).strip()
    return rest if re.search(r"\w", rest) else text


def own_identifiers(text: str) -> list[str]:
    """API identifiers written in the message (see _ID_PATTERNS)."""
    found: list[str] = []
    for rx in _ID_PATTERNS:
        for m in rx.findall(text):
            m = m if isinstance(m, str) else m[0]
            if m and m not in _NOT_IDENTIFIERS and m not in found and not (rx is _ID_PATTERNS[4] and m[1:].isupper()):
                found.append(m)
    return found


def is_vague(text: str) -> bool:
    """True when the message names no subject: no identifier and no word outside _FILLER ("yes explain more")."""
    if own_identifiers(text):
        return False
    return not [w for w in _WORD_RX.findall(text.lower().replace("’", "'")) if w not in _FILLER]


def follow_up_rule(question: str) -> str:
    """Why a message is or is not treated as a follow-up (recorded in details.context.rule)."""
    if own_identifiers(question):
        return "own_identifier"
    return "referential_cue" if FOLLOWUP_RX.search(question) else "standalone"


def is_follow_up(question: str) -> bool:
    return follow_up_rule(question) == "referential_cue"


def is_usable_topic(question: str) -> bool:
    """Whether an earlier user message can serve as follow-up context (greetings, social, out-of-scope and vague
    messages cannot)."""
    question = core_message(question)
    return (greeting_kind(question) is None and social_kind(question) is None and out_of_scope_topic(question) is None
            and not is_vague(question))


@dataclass(frozen=True)
class Route:
    outcome: str            # "greeting" | "social" | "out_of_scope" | "clarification" | "rag"
    reason: str             # greeting, thanks, social, acknowledgement, <out-of-scope topic>, no_topic, no_subject,
                            # unresolved_reference, continuation, referential_cue, own_identifier, standalone
    use_context: bool = False


def needs_history(text: str) -> bool:
    """Whether routing depends on the session's earlier questions (only then are they read)."""
    text = core_message(text)
    if greeting_kind(text) or social_kind(text) or out_of_scope_topic(text) or own_identifiers(text):
        return False
    return is_vague(text) or is_follow_up(text)


def route(text: str, has_topic: bool) -> Route:
    """The routing decision. `has_topic`: the session has a usable earlier question (see is_usable_topic).
    A leading greeting is set aside first, so "hi who are you" is decided as "who are you"."""
    text = core_message(text)
    if kind := greeting_kind(text):
        return Route("greeting", kind)
    if kind := social_kind(text):
        return Route("social", kind)
    if topic := out_of_scope_topic(text):           # before identifiers and context: neither can make it in scope
        return Route("out_of_scope", topic)
    rule = follow_up_rule(text)
    if rule == "own_identifier":
        return Route("rag", rule)
    if is_vague(text):
        if has_topic and (CONTINUE_RX.search(text) or rule == "referential_cue"):
            return Route("rag", "continuation", use_context=True)
        return Route("clarification", "no_subject" if has_topic else "no_topic")
    if rule == "referential_cue":
        if has_topic:
            return Route("rag", rule, use_context=True)
        pronoun = PRONOUN_RX.search(text)
        if pronoun and not has_own_antecedent(text[:pronoun.start()]):
            return Route("clarification", "unresolved_reference")   # "Is it deprecated?" with nothing for "it"
    return Route("rag", "standalone")


def has_own_antecedent(before_pronoun: str) -> bool:
    """Whether the message names a subject before its pronoun ("which signature header ... and its format?"), so the
    pronoun refers inside the message. "Pismo" alone is not such a subject ("Does Pismo support it?")."""
    return any(m.group(0).lower() != "pismo" for m in _DOMAIN_RX.finditer(before_pronoun))


def build_pipeline_question(question: str, prior_questions: list[str], max_chars: int,
                            follow_up: bool | None = None) -> tuple[str, bool]:
    """Return (question passed to the pipeline, whether context was added). `follow_up` overrides the cue check
    (the router decides; a continuation such as "yes explain more" has no cue but does use context)."""
    if not prior_questions or max_chars <= 0 or not (is_follow_up(question) if follow_up is None else follow_up):
        return question, False
    kept, used = [], 0
    for q in reversed(prior_questions):          # most recent first, until the budget is spent
        q = " ".join(q.split())
        if used + len(q) > max_chars:
            q = q[: max(0, max_chars - used)].rstrip()
            if not q:
                break
        kept.insert(0, q)
        used += len(q)
        if used >= max_chars:
            break
    if not kept:
        return question, False
    ctx = "; ".join(f'"{q}"' for q in kept)
    return f"{question}\n\n(Follow-up in the same conversation. Earlier questions, for context only: {ctx})", True


@dataclass
class Exchange:
    user_message: Message
    assistant_message: Message
    http_status: int


def _citations(result: dict) -> list[dict]:
    keep = ("label", "ku_id", "title", "section", "chunk_id", "origin", "sources")
    return [{k: c.get(k) for k in keep if k in c} for c in (result.get("citations") or [])]


def _details(result: dict, context: dict, duration_ms: int) -> dict:
    return {
        "citations_valid": result.get("citations_valid"),
        "verification": result.get("verification"),
        "warnings": result.get("warnings") or [],
        "missing_information": result.get("missing_information"),
        "model": result.get("model"),
        "matched_operations": [{k: m.get(k) for k in ("operation", "method", "path", "summary", "matched_by")}
                               for m in result.get("matched_operations") or []],
        "evidence": [{k: e.get(k) for k in ("label", "chunk_id", "ku_id", "origin")} for e in result.get("evidence") or []],
        "context": context,
        "duration_ms": duration_ms,
    }


@dataclass
class Outcome:
    """What step 3 persists: the assistant message and its activity row."""
    status: str
    http_status: int
    content: str
    citations: list
    details: dict
    event: str = "message.answer"
    duration_ms: int = 0
    evidence_count: int | None = None
    model: str | None = None
    error_kind: str | None = None
    timings: dict[str, Any] = field(default_factory=dict)


CLARIFY_SCOPE_REPLY = ("I'm not sure what you'd like to know. Which Pismo API, integration workflow, webhook, event or "
                       "error code is your question about?")
OUT_OF_SCOPE_GENERIC_REPLY = ("I'm designed to help with Pismo APIs, developer documentation, integrations, events, "
                              "webhooks, and related implementation questions. I can't help with unrelated topics. What "
                              "Pismo integration question can I help you with?")
# out-of-scope reasons from the classifier -> the topic named in the reply (None: generic reply)
CLASSIFIER_TOPICS = {"general_knowledge": "general knowledge questions", "unrelated_software": "unrelated software projects",
                     "creative_or_personal": "personal or creative requests", "unrelated_topic": None}
DIRECT_REPLIES = {"greeting": GREETING_REPLY, "thanks": THANKS_REPLY, "social": SOCIAL_REPLY, "acknowledgement": ACK_REPLY,
                  "identity": IDENTITY_REPLY, "capabilities": CAPABILITIES_REPLY,
                  "no_topic": CLARIFY_REPLY, "no_subject": CLARIFY_REPLY, "unresolved_reference": CLARIFY_REFERENCE_REPLY,
                  # classifier clarifications and the fallback's unclear scope
                  "no_clear_subject": CLARIFY_SCOPE_REPLY, "ambiguous_reference": CLARIFY_REFERENCE_REPLY,
                  "follow_up_without_topic": CLARIFY_REFERENCE_REPLY, "unclear_scope": CLARIFY_SCOPE_REPLY}


def _direct_reply(d: RouteDecision) -> str:
    if d.outcome == "out_of_scope":
        topic = CLASSIFIER_TOPICS.get(d.reason, d.reason) if d.source == "classifier" else d.reason
        return OUT_OF_SCOPE_REPLY.format(topic=topic) if topic else OUT_OF_SCOPE_GENERIC_REPLY
    return DIRECT_REPLIES[d.reason]


def _direct_outcome(d: RouteDecision) -> Outcome:
    """Fixed reply or clarification: no retrieval, answer generation, citation validation or context, and no
    details.index - the knowledge base was not searched. The text is always one of the fixed replies above (the
    classifier only picks a route). Same detail keys as a pipeline answer, nothing invented."""
    details = _details({}, {"used": False, "prior_message_ids": [], "pipeline_question": None}, 0)
    details["response_kind"] = d.outcome                 # "greeting" | "social" | "clarification" | "out_of_scope"
    details["route"] = d.as_details()
    return Outcome(status="answered", http_status=201, content=_direct_reply(d), citations=[], details=details,
                   event=f"message.{d.outcome}", evidence_count=0)


async def _pipeline_outcome(settings: Settings, service: AssistantService, content: str, prior: list[Message],
                            r: RouteDecision, observer: CallObserver | None = None) -> Outcome:
    """Step 2. Deliberately takes no database session: nothing here may touch the database."""
    # retrieval and the model get the question without a leading greeting; earlier questions likewise
    pipeline_q, used = build_pipeline_question(core_message(content), [core_message(m.content) for m in prior],
                                               settings.context_max_chars,
                                               follow_up=r.use_context)
    context = {"used": used, "prior_message_ids": [str(m.id) for m in prior] if used else [], "pipeline_question": pipeline_q,
               "rule": r.reason}
    timings: dict[str, Any] = {}

    t0 = time.perf_counter()
    result, error, index_hash = None, None, None
    try:
        result, service_timings, index_hash = await service.answer_with_timings(pipeline_q, observer=observer)
        timings.update(service_timings)
    except AssistantTimeout as e:
        error = {"kind": "timeout", "message": str(e), "worker_still_running": e.still_running}
    except Exception as e:  # unexpected pipeline failure: record it, do not invent an answer
        error = {"kind": "internal", "message": f"{type(e).__name__}"}
    t1 = time.perf_counter()
    duration_ms = int((t1 - t0) * 1000)
    timings["pipeline_call_ms"] = ms(t0, t1)
    if result is not None and result.get("status") == "generation_error":
        err = result.get("error") or {}
        error = {"kind": err.get("kind") or "api_error", "message": err.get("message") or "generation failed"}

    common = {"duration_ms": duration_ms, "timings": timings, "model": (result or {}).get("model"),
              "evidence_count": len((result or {}).get("evidence") or []) if result else None}
    # the index that served this call; only known when the pipeline returned (not on timeout or crash)
    extra: dict[str, Any] = {"index": {"chunk_set_hash": index_hash}} if result is not None else {}
    extra["route"] = r.as_details()
    if error is None and result.get("status") in ANSWER_STATUSES:
        return Outcome(status=result["status"], http_status=201, content=result.get("answer") or "",
                       citations=_citations(result), details={**_details(result, context, duration_ms), **extra}, **common)
    if error is None:
        error = {"kind": "internal", "message": f"unexpected pipeline status {result.get('status')!r}"}
    details = {**_details(result or {}, context, duration_ms), **extra}
    details["error"] = error
    return Outcome(status="error", http_status=HTTP_FOR_ERROR.get(error["kind"], 502), content="", citations=[],
                   details=details, error_kind=error["kind"], **common)


async def send_message(db: Session, settings: Settings, service: AssistantService, session_id: uuid.UUID,
                       content: str, guard: SessionGuard, router: Router | None = None) -> Exchange | None:
    """Returns None if the session does not exist (or was deleted while the answer was generated).
    Raises SessionBusy if another message for this session is still being processed. `router` None: rules only."""
    with guard.hold(session_id):
        return await _exchange(db, settings, service, session_id, content, router or Router())


@dataclass
class _Begun:
    """State after transaction 1."""
    chat: Any
    user_msg: Message
    prior: list[Message]
    route: Route
    t_start: float
    t_saved: float
    t_ctx: float
    t_ctx_end: float


def _begin(db: Session, settings: Settings, session_id: uuid.UUID, content: str) -> _Begun | None:
    """Transaction 1: store the question (kept even if generation later fails) and, only when the routing decision
    depends on it, read the session's usable earlier questions. None if the session does not exist."""
    t_start = time.perf_counter()
    try:
        chat = store.get_session(db, session_id)
        if chat is None:
            db.rollback()
            return None
        user_msg = store.add_message(db, session_id, "user", content)
        store.touch_session(db, chat, first_question=content)
        t_ctx = time.perf_counter()
        prior = store.prior_user_questions(db, session_id, user_msg.seq, settings.context_max_prior_questions,
                                           skip=lambda q: not is_usable_topic(q)) if needs_history(content) else []
        t_ctx_end = time.perf_counter()
        db.commit()                                 # ends the transaction and returns the connection to the pool
    except BaseException:
        db.rollback()
        raise
    return _Begun(chat, user_msg, prior, route(content, has_topic=bool(prior)), t_start, time.perf_counter(), t_ctx,
                  t_ctx_end)


async def _decide(router: Router, content: str, b: _Begun) -> tuple[RouteDecision, float]:
    """First-stage routing (rules, then the classifier where needed) - after transaction 1, so no transaction or
    connection is held while a classifier call runs."""
    t0 = time.perf_counter()
    d = await router.decide(core_message(content), [core_message(m.content) for m in b.prior], b.route)
    return d, ms(t0, time.perf_counter())


async def _produce(settings: Settings, service: AssistantService, content: str, b: _Begun, d: RouteDecision,
                   routing_ms: float, observer: CallObserver | None = None) -> Outcome:
    """Step 2: fixed reply / clarification, or the unchanged pipeline - no transaction or connection is held meanwhile."""
    if d.outcome not in ("pismo_question", "follow_up"):
        out = _direct_outcome(d)
    else:
        out = await _pipeline_outcome(settings, service, content, b.prior if d.use_context else [], d, observer)
        out.timings["db_context_ms"] = ms(b.t_ctx, b.t_ctx_end)
    out.timings["routing_ms"] = routing_ms
    return out


def _finish(db: Session, session_id: uuid.UUID, b: _Begun, out: Outcome) -> Message | None:
    """Transaction 2: the answer and its activity row, committed together. None (nothing written) if the session was
    deleted while the answer was generated."""
    t_db = time.perf_counter()
    try:
        if not store.session_exists(db, session_id):
            db.rollback()
            log.info("%s session=%s deleted during processing; answer not stored", out.event, session_id)
            return None
        asst = store.add_message(db, session_id, "assistant", out.content, status=out.status, citations=out.citations,
                                 details=out.details)
        store.touch_session(db, b.chat)
        store.add_activity(db, session_id=session_id, event=out.event,
                           status=out.status if out.status != "error" else out.error_kind,
                           http_status=out.http_status, duration_ms=out.duration_ms, evidence_count=out.evidence_count,
                           citation_count=len(out.citations), model=out.model, error_kind=out.error_kind)
        db.flush()
        t_end = time.perf_counter()
        asst.details = {**out.details, "timings": {"db_question_ms": ms(b.t_start, b.t_saved), **out.timings,
                                                  "db_answer_ms": ms(t_db, t_end), "total_ms": ms(b.t_start, t_end)}}
        db.commit()
    except BaseException:
        db.rollback()
        raise
    log.info("%s session=%s status=%s timings=%s commit_ms=%.1f", out.event, session_id, out.status,
             asst.details["timings"], ms(t_end, time.perf_counter()))
    return asst


async def _exchange(db: Session, settings: Settings, service: AssistantService, session_id: uuid.UUID,
                    content: str, router: Router) -> Exchange | None:
    b = _begin(db, settings, session_id, content)
    if b is None:
        return None
    d, routing_ms = await _decide(router, content, b)
    out = await _produce(settings, service, content, b, d, routing_ms)
    asst = _finish(db, session_id, b, out)
    return None if asst is None else Exchange(b.user_msg, asst, out.http_status)


# ---- streaming (POST /api/sessions/{id}/messages/stream) -------------------------------------------------------------

STREAM_ERROR_MESSAGES = {
    "timeout": "The assistant did not answer in time.",
    "configuration": "The assistant is not configured (for example, the OpenAI API key is missing).",
    "api_error": "The language model request failed.",
    "malformed_output": "The language model returned output that could not be used.",
    "cancelled": "Generation was stopped.",
    "internal": "The assistant failed with an internal error.",
    "session_busy": "A message for this session is still being processed. Wait for its answer, then try again.",
    "session_not_found": "This session no longer exists.",
    "session_deleted": "The session was deleted while the answer was being generated. Nothing was saved.",
}
_DONE = object()


async def stream_exchange(db: Session, settings: Settings, service: AssistantService, session_id: uuid.UUID,
                          content: str, guard: SessionGuard, is_disconnected: Callable[[], Awaitable[bool]],
                          poll_s: float = 1.0, heartbeat_s: float = 15.0,
                          router: Router | None = None) -> AsyncIterator[tuple[str, dict[str, Any]]]:
    """The same exchange as send_message, reported as (event, data) pairs while it happens:

      status      {"stage": "routing"}                              question stored; the routing classifier is running
                                                                    (only when the rules leave the decision to it)
                  {"stage": "accepted", "user_message", "route"}   question stored and routed (route: see router.py)
                  {"stage": "queued" | "retrieving" | "evidence_ready" (+ evidence_count) | "generating" | "validating"}
                                                                    emitted by the pipeline when the stage really starts
                  {"stage": "saving"}                               transaction 2 starts
      delta       {"text"}                                          PROVISIONAL answer text from the streamed model output;
                                                                    never stored, never final
      validation  {"status", "citations_valid", "citation_count", "warning_count"}   after citation validation
      final       {"http_status", "exchange"}                       the stored, validated answer (same as the regular API)
      error       {"code", "message", "http_status", ["exchange"]}  terminal failure; "exchange" when a failure record
                                                                    was stored (as the regular API does)
      comment     {}                                                keep-alive while nothing else happens

    Exactly one terminal event (final or error) ends a completed stream. If the client disconnects, the stream ends
    without one: the model stream is told to stop at its next chunk, the pipeline task is cancelled, nothing is stored
    for the answer (the question stays, as with the regular API) and the session guard is released."""
    router = router or Router()                      # None: rules only
    observer = CallObserver(asyncio.get_running_loop())
    task: asyncio.Task | None = None
    routing: asyncio.Task | None = None
    try:
        with guard.hold(session_id):
            b = _begin(db, settings, session_id, content)
            if b is None:
                yield "error", _stream_error("session_not_found", 404)
                return
            if router.needs_classifier(b.route):
                yield "status", {"stage": "routing"}       # the classifier is deciding how to handle the message
                routing = asyncio.create_task(_decide(router, content, b))
                while not routing.done():
                    await asyncio.wait({routing}, timeout=poll_s)
                    if not routing.done() and await is_disconnected():
                        log.info("stream session=%s: client disconnected during routing; nothing stored", session_id)
                        return
                d, routing_ms = routing.result()
            else:
                d, routing_ms = await _decide(router, content, b)
            yield "status", {"stage": "accepted", "user_message": b.user_msg, "route": d.as_details()}
            if d.outcome in ("pismo_question", "follow_up"):
                task = asyncio.create_task(_produce(settings, service, content, b, d, routing_ms, observer))
                task.add_done_callback(lambda _t: observer.queue.put_nowait((_DONE, {})))
                idle = 0.0
                while True:
                    try:
                        event, data = await asyncio.wait_for(observer.queue.get(), timeout=poll_s)
                    except asyncio.TimeoutError:
                        if await is_disconnected():
                            log.info("stream session=%s: client disconnected; generation stopped, nothing stored",
                                     session_id)
                            return
                        idle += poll_s
                        if idle >= heartbeat_s:
                            idle = 0.0
                            yield "comment", {}
                        continue
                    if event is _DONE:
                        break
                    idle = 0.0
                    yield event, data
                out = task.result()
                if out.status != "error":
                    d = out.details
                    yield "validation", {"status": out.status, "citations_valid": d.get("citations_valid"),
                                         "citation_count": len(out.citations), "warning_count": len(d.get("warnings") or [])}
            else:
                out = await _produce(settings, service, content, b, d, routing_ms)   # fixed reply: no RAG, no model
            yield "status", {"stage": "saving"}
            asst = _finish(db, session_id, b, out)
            if asst is None:
                yield "error", _stream_error("session_deleted", 404)
                return
            exchange = {"session_id": session_id, "user_message": b.user_msg, "assistant_message": asst}
            if out.status == "error":
                yield "error", {**_stream_error(out.error_kind or "internal", out.http_status), "exchange": exchange}
            else:
                yield "final", {"http_status": out.http_status, "exchange": exchange}
    except SessionBusy:
        yield "error", _stream_error("session_busy", 409)
    except Exception:                                # e.g. a database failure after the stream started
        log.exception("stream session=%s failed", session_id)
        yield "error", _stream_error("internal", 500)
    finally:
        observer.stop()                              # a streamed model response stops at its next chunk
        if task is not None and not task.done():
            task.cancel()                            # its result is never stored
        if routing is not None and not routing.done():
            routing.cancel()                         # an abandoned classification is discarded


def _stream_error(code: str, http_status: int) -> dict[str, Any]:
    return {"code": code, "message": STREAM_ERROR_MESSAGES.get(code, "The request failed."), "http_status": http_status}
