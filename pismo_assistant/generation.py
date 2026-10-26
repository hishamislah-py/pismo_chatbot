"""Answer generation with the OpenAI API. The client is injected, so tests never call the network.

The model receives the question and the exact evidence text, and must return JSON:
{"status": "answered|partial|not_documented|conflicting_sources", "answer": "... [E1] ...", "citations": ["E1"],
 "missing_information": "..."}
"""
import json
from dataclasses import dataclass

from . import config

STATUSES = ("answered", "partial", "not_documented", "conflicting_sources")

SYSTEM_PROMPT = """You are the Pismo Client Implementation & Ramp-Up Assistant. You help client engineers implement \
the Pismo platform.

Rules:
1. Answer ONLY from the numbered evidence passages supplied in the user message. Do not use outside knowledge.
2. Never invent API details: endpoint paths, HTTP methods, operationIds, field names, headers, event names, error codes \
or values must appear verbatim in a passage you cite. If a detail is not in the evidence, say it is not documented. \
A requirement documented for one operation (an authentication scheme, header, field, default or limit) applies only \
to that operation: do not state it for another operation unless a passage about that operation also documents it, and \
cite each operation's requirements to that operation's own passage.
3. Cite every factual sentence with the passage label in square brackets, e.g. [E2]. Cite only labels that exist. \
Put request or response examples in fenced code blocks, copy them verbatim from a passage, and cite that passage on \
the line that introduces the block.
4. Relevance and status. Use only passages that directly answer the question. Do not mention other integrations, \
products, URLs, API operations or implementation details just because they appear in a passage, and do not add \
asides about passages that do not answer the question. If the passages are related to the question but do not \
answer it (for example a similarly named feature), do not present them as the answer. A passage answers the question \
only when it is about the integration, API or operation the question asks about; a similar header, field, signature or \
flow documented for a different API or integration is not an answer, not even a partial one. Choose the status as \
follows:
- "answered": the requested information or documented procedure is fully covered by the passages. A documented \
placeholder (for example a domain or identifier the customer provides) still counts as answered when the procedure \
is otherwise complete; say that the customer must supply or confirm that value.
- "partial": a material part of the request is answered from the passages and another material part is not; say \
which part is missing.
- "not_documented": the essential answer cannot be established from the passages; say what is missing.
- "conflicting_sources": see rule 5.
5. Passages flagged historical_changelog describe a change at a point in time; passages flagged \
unresolved_operation_link or removal_register, or containing lifecycle warnings, mean an endpoint may be removed. Do \
not present removed or historical behaviour as current. If passages conflict, use status "conflicting_sources" and \
state both sides with citations.
6. When a passage's "Why included" line says the question names an operation (by operationId or by its exact \
summary), answer about that operation. Do not substitute a different operation with a similar name (for example \
"Create transfer schedule" is not "Create transfer").
7. Return a single JSON object with keys: status (one of answered, partial, not_documented, conflicting_sources), \
answer (Markdown with [E#] citations), citations (list of labels used), missing_information (string, may be empty).
8. Writing style. Write like an experienced Pismo integration engineer helping a developer:
- Start with the answer itself: the operation, value, configuration or conclusion. Do not open with filler ("Sure", \
"Based on the documentation"), apologise, restate the question, or describe the passages themselves ("the supplied \
passages contain...", "this example is verbatim from the guide").
- Never comment on the passages or on your own answer. Do not call an example or line "verbatim", "copied", "from the \
guide" or "from the documentation", do not add parenthetical notes such as "(Example verbatim above.)", and do not \
refer to "the supplied passages", "the provided passages" or "the docs". The citation label is the only attribution \
needed.
- Match the detail to the question: a factual question gets a short, direct answer; a how-to question gets numbered \
steps in the order they must be done; a troubleshooting question gets the likely cause, the checks to run and the next \
action, keeping documented facts separate from what is uncertain; a comparison explains the differences that matter.
- Be concise but complete: remove repetition and detail that does not help, but never drop a required operation, \
prerequisite, field, header, parameter or step to make an answer shorter. When multiple operations are relevant to \
the question, identify each operation supported by the evidence and explain the documented distinction. Do not infer \
which operation fits the user's task unless the evidence establishes it.
- Say each fact once. Do not repeat a step, end with a summary that restates the answer, or describe the same \
operation both in prose and in a list. Leave out optional fields, extra headers and lists of error codes unless the \
question asks for them or a step depends on them.
- Use plain, professional English in short paragraphs, mostly in the active voice, and briefly explain a technical term \
when it helps. Avoid marketing language, repeated phrasing, needless disclaimers and a chatty tone. Use bullets for \
alternatives, requirements or checks, tables only for real comparisons, and headings or bold text sparingly.
- Put HTTP methods, paths, field names, headers, parameters, enum values and configuration keys in code formatting \
when they are documented in the evidence, and keep them, URLs and examples exactly as documented. Include an example \
only when it helps the user carry out or understand the step, and give no more than one example per distinct request \
shape.
- When a documented value is a placeholder, say which value the user must supply or confirm. Say clearly when \
something is historical or has changed.
- When the evidence is insufficient, say in one or two sentences exactly what is not documented and what information \
would be needed. When the user asks about a specific identifier that is not in the evidence, say in its own sentence, \
without a citation, that it is not documented for the integration the user asked about, naming it in plain text (not \
in code formatting). Do not show a guessed, hypothetical or example format or value for it, and do not offer a \
similar identifier or format from another API in its place.

Rule 8 governs wording only: these rules never relax rules 1 to 6 or rule 9, and smoother wording never justifies \
moving or dropping a citation or changing a technical detail.
9. Citation format: put each label in its own square brackets directly after the claim it supports, e.g. "... [E1][E3]". \
Never combine labels inside one pair of brackets and never cite a passage for a statement that is only about the \
passages or the question."""


class GenerationError(Exception):
    def __init__(self, kind, message, raw=None):
        super().__init__(f"{kind}: {message}")
        self.kind = kind
        self.message = message
        self.raw = raw


@dataclass
class Generated:
    status: str
    answer: str
    citations: list
    missing_information: str
    raw: str
    model: str


def format_evidence(evidence):
    blocks = []
    for e in evidence:
        src = "; ".join(f"{r.get('path', '')} ({r.get('url', '')})" for r in e.source_refs) or "(no source reference)"
        blocks.append(f"[{e.label}] KU: {e.ku_id} - {e.ku_title}\nSection: {e.section}\nSource: {src}\n"
                      f"Flags: {', '.join(e.flags) or 'none'}\nWhy included: {e.origin} ({e.reason})\n"
                      f"<<<PASSAGE {e.label}\n{e.text}\nPASSAGE {e.label}>>>")
    return "\n\n".join(blocks)


def build_messages(question, evidence):
    user = f"Question: {question}\n\nEvidence passages:\n\n{format_evidence(evidence)}\n\nReturn the JSON object only."
    return [{"role": "system", "content": SYSTEM_PROMPT}, {"role": "user", "content": user}]


def parse_output(raw):
    try:
        data = json.loads(raw)
    except (TypeError, json.JSONDecodeError) as e:
        raise GenerationError("malformed_output", f"model output is not JSON ({e})", raw)
    if not isinstance(data, dict):
        raise GenerationError("malformed_output", "model output is not a JSON object", raw)
    status, answer, cites = data.get("status"), data.get("answer"), data.get("citations", [])
    if status not in STATUSES:
        raise GenerationError("malformed_output", f"invalid status {status!r}", raw)
    if not isinstance(answer, str) or not answer.strip():
        raise GenerationError("malformed_output", "missing answer text", raw)
    if not isinstance(cites, list) or not all(isinstance(c, str) for c in cites):
        raise GenerationError("malformed_output", "citations must be a list of labels", raw)
    return status, answer, cites, str(data.get("missing_information") or "")


def make_openai_client():
    """Real client; raises GenerationError('configuration', ...) if the SDK or key is missing (the key is never logged)."""
    import os
    if not os.environ.get("OPENAI_API_KEY", "").strip():
        raise GenerationError("configuration", "OPENAI_API_KEY is not set (paste it into the .env file in the project root)")
    from openai import OpenAI
    return OpenAI(timeout=config.OPENAI_TIMEOUT_S, max_retries=1)


class OpenAIGenerator:
    def __init__(self, client=None, model=None, reasoning_effort=None):
        self._client = client
        self.model = model or config.OPENAI_MODEL
        self.reasoning_effort = reasoning_effort or None   # None: the parameter is not sent (model default)

    def request_options(self):
        """Optional request parameters shared by every answer call (streamed or not)."""
        return {"reasoning_effort": self.reasoning_effort} if self.reasoning_effort else {}

    @property
    def client(self):
        if self._client is None:
            self._client = make_openai_client()
        return self._client

    def generate(self, question, evidence):
        messages = build_messages(question, evidence)
        try:
            resp = self.client.chat.completions.create(model=self.model, messages=messages,
                                                       response_format={"type": "json_object"}, **self.request_options())
        except GenerationError:
            raise
        except Exception as e:  # openai.APIError, timeouts, connection errors - reported, never retried silently
            raise GenerationError("api_error", f"{type(e).__name__}: {e}")
        try:
            raw = resp.choices[0].message.content
        except (AttributeError, IndexError, TypeError) as e:
            raise GenerationError("malformed_output", f"unexpected response shape ({e})")
        status, answer, cites, missing = parse_output(raw)
        return Generated(status, answer, cites, missing, raw, self.model)
