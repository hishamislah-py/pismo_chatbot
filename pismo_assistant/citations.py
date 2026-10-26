"""Citation validation.

What IS checked (deterministic):
  1. source mapping     - every cited label exists in the supplied evidence and that evidence has a KU id, title and
                          source path + URL;
  2. claim-level tokens - the answer is split into claim units (a line/bullet plus any code block that follows it).
                          Every API-looking token in a unit (path, operationId/event slug, snake_case field, error
                          code, back-ticked text) must occur in a passage cited *by that unit*; a unit with such tokens
                          and no citation is flagged;
  3. operation alignment - when the question identified an operation (by operationId or exact summary phrase), an
                          answer that names other operations' paths but never that operation is flagged;
  4. history marking    - a unit supported only by historical changelog passages must describe the item as
                          historical/removed/changed, or it is flagged.

  5. integration scope  - when the question is about one integration only (integrations.excluded_integrations), a unit
                          citing a passage whose provenance is an excluded integration is flagged, even if the cited
                          text contains the claim (e.g. the data-platform production URL given for client webhooks).
  6. operation scope    - a generalized requirement ("both", "all", "each", ...) cited to passages of two or more
                          different operations must be supported by each operation's own passage (or by a cited general
                          guide passage); one operation's header or field does not establish it for another.
  7. abstentions        - a token is exempt from checks 2 only when the user's question contains it verbatim, every
                          sentence using it says it is not documented, and no supplied passage contains it (recorded in
                          abstained_identifiers). Other tokens in that sentence are checked as usual.
What is NOT checked: whether a cited passage semantically supports the claim (e.g. that an endpoint really performs the
requested action). `semantic_support_verified` is always False in this version.
"""
import re
from dataclasses import dataclass, field

from .integrations import evidence_integration as integration_of

LABEL_GROUP_RX = re.compile(r"\[\s*(E\d+(?:\s*[,;]\s*E\d+)*)\s*\]")
FENCE_RX = re.compile(r"^\s*(```|~~~)")
API_TOKEN_RX = re.compile(
    r"`([^`\n]{2,120})`"                                          # back-ticked text
    r"|(?<![\w/])(/[A-Za-z0-9{}_\-.]+(?:/[A-Za-z0-9{}_\-.]+)+)"     # API path
    r"|\b([A-Z][A-Z0-9]{1,9}[0-9]{3,6})\b"                         # error code
    r"|\b([a-z0-9]+(?:-[a-z0-9]+){2,})\b"                          # operationId / event slug (2+ hyphens)
    r"|\b([a-z][a-z0-9]*(?:_[a-z0-9]+)+)\b")                       # snake_case field name
HISTORY_WORDS = re.compile(r"removed|no longer|deprecated|decommission|historical|changelog|previously|originally|formerly"
                           r"|\bwas\b|\bwere\b|\bhad\b|used to|has been|changed|as of|replaced", re.I)
# operation scope (check 6)
OPERATION_OF_RX = re.compile(r"::op-([a-z0-9-]+?)(?:\.|::|$)")          # chunk ids of operation passages (corpus.section_key)
CITATION_RUN_RX = re.compile(r"(?:\[\s*E\d+(?:\s*[,;]\s*E\d+)*\s*\]\s*)+")  # adjacent label groups: "[E4][E7]"
GENERALIZING_RX = re.compile(r"\b(both|all|each|every|either|these (?:operations|endpoints)|"
                             r"the (?:two|three) (?:operations|endpoints))\b", re.I)
ERROR_CODE_TOKEN_RX = re.compile(r"^[A-Z][A-Z0-9]{1,9}[0-9]{3,6}$")
EVENT_SLUG_RX = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)+-\d+$")
# abstentions (check 7): a sentence that explicitly says something is not documented
NOT_DOCUMENTED_RX = re.compile(r"\b(?:is|are) not documented\b|\bnot documented\b|\bdoes not (?:specify|document|describe)\b|"
                               r"\bdo not (?:specify|document|describe)\b|\bis not (?:specified|described)\b", re.I)
SENTENCE_RX = re.compile(r"(?<=[.!?])\s+")


@dataclass
class CitationReport:
    valid: list = field(default_factory=list)              # cited labels that map to evidence with complete metadata
    unknown: list = field(default_factory=list)            # cited labels that were not supplied
    missing_metadata: list = field(default_factory=list)   # cited labels whose evidence lacks KU id/title/source path/URL
    unsupported_tokens: list = field(default_factory=list)  # (token, unit labels) not found in the unit's cited passages
    uncited_claims: list = field(default_factory=list)     # claim units containing API tokens but no citation
    operation_mismatch: list = field(default_factory=list)  # expected operations never named while other paths are
    unmarked_historical: list = field(default_factory=list)  # units supported only by changelogs, not marked historical
    integration_mismatch: list = field(default_factory=list)  # units citing documentation of an integration the question excludes
    cross_operation_claims: list = field(default_factory=list)  # generalized requirements missing from a cited operation
    abstained_identifiers: list = field(default_factory=list)  # informational: requested tokens named only as undocumented
    uncited_answer: bool = False
    semantic_support_verified: bool = False                # never claimed in this version

    @property
    def source_mapping_ok(self):
        return bool(self.valid) and not (self.unknown or self.missing_metadata)

    @property
    def ok(self):
        return self.source_mapping_ok and not (self.unsupported_tokens or self.uncited_claims or self.operation_mismatch
                                               or self.unmarked_historical or self.integration_mismatch
                                               or self.cross_operation_claims)

    def checks(self):
        return {"source_mapping": self.source_mapping_ok, "claim_token_support": not (self.unsupported_tokens or self.uncited_claims),
                "operation_alignment": not self.operation_mismatch, "historical_marking": not self.unmarked_historical,
                "integration_scope": not self.integration_mismatch, "operation_scope": not self.cross_operation_claims,
                "semantic_support_verified": False}


def has_metadata(e):
    return bool(e.ku_id and e.ku_title and e.source_refs and all(r.get("path") and r.get("url") for r in e.source_refs))


def labels_in(text):
    return [l for g in LABEL_GROUP_RX.findall(text or "") for l in re.findall(r"E\d+", g)]


def claim_units(answer):
    """Split an answer into claim units: each non-empty line, with a following code block (fenced, or an unfenced JSON
    object/array) attached to the line that introduces it."""
    units, in_code, depth = [], False, 0
    for line in (answer or "").split("\n"):
        s = line.strip()
        if FENCE_RX.match(line):
            in_code = not in_code
            if units:
                units[-1] += "\n" + line
            continue
        if (in_code or depth > 0) and units:
            units[-1] += "\n" + line
            depth = max(0, depth + s.count("{") + s.count("[") - s.count("}") - s.count("]")) if not in_code else depth
        elif s.startswith(("{", "[")) and not LABEL_GROUP_RX.match(s) and units:
            units[-1] += "\n" + line
            depth = max(0, s.count("{") + s.count("[") - s.count("}") - s.count("]"))
        elif s:
            units.append(line)
    return units


def api_tokens(text, known_identifiers=None):
    """API-like tokens in text. A bare hyphenated word counts as an identifier only when it contains a digit (event
    slugs end in -<version>) or is a known spec operationId, so English words like 'step-by-step' are not checked."""
    out = []
    for m in API_TOKEN_RX.finditer(LABEL_GROUP_RX.sub(" ", text)):
        tok = next(g for g in m.groups() if g).strip().rstrip(".,;:)")  # sentence punctuation is not part of a token
        if m.group(4) and not (re.search(r"\d", tok) or tok.lower() in (known_identifiers or ())):
            continue
        if tok and tok not in out:
            out.append(tok)
    return out


def operation_of(evidence_item):
    """operationId slug of an operation passage (from its chunk id), or None for guide and other passages."""
    m = OPERATION_OF_RX.search(evidence_item.chunk_id or "")
    return m.group(1) if m else None


def _requirement_like(tok, operation_ids):
    """Headers, fields, parameters, auth schemes...; not paths, method+path, error codes, event slugs or operationIds."""
    return not (tok.startswith("/") or re.match(r"^[A-Z]+ /", tok) or ERROR_CODE_TOKEN_RX.match(tok)
                or EVENT_SLUG_RX.match(tok) or " " in tok.strip() or tok.lower() in operation_ids)


def _cross_operation_claims(unit, by_label, known_identifiers):
    """Check 6: generalized requirements whose citation group spans two or more operations."""
    out, pos = [], 0
    known = {k.lower() for k in (known_identifiers or ())}
    for m in CITATION_RUN_RX.finditer(unit):
        segment, pos = unit[pos:m.start()], m.end()
        if not GENERALIZING_RX.search(segment):
            continue
        by_op, general = {}, []
        for lab in re.findall(r"E\d+", m.group(0)):
            e = by_label.get(lab)
            if e is not None:
                op = operation_of(e)
                (by_op.setdefault(op, []) if op else general).append(e)
        if len(by_op) < 2:
            continue
        for tok in api_tokens(segment, known_identifiers):
            t = tok.lower()
            if not _requirement_like(tok, known | set(by_op)) or any(t in e.text.lower() for e in general):
                continue
            missing = sorted(op for op, es in by_op.items() if not any(t in e.text.lower() for e in es))
            if missing:
                out.append({"token": tok, "operations": sorted(by_op), "not_documented_for": missing})
    return out


def _abstained(unit, toks, question, evidence_text):
    """Check 7: tokens the user asked about that the unit only names as undocumented."""
    if not question:
        return set()
    sentences = SENTENCE_RX.split(LABEL_GROUP_RX.sub(" ", unit))
    out = set()
    for tok in toks:
        using = [s for s in sentences if tok in s]
        if tok in question and tok.lower() not in evidence_text and using and all(NOT_DOCUMENTED_RX.search(s) for s in using):
            out.add(tok)
    return out


def validate(answer, cited_labels, evidence, expected_operations=None, status=None, known_identifiers=None,
             excluded_integrations=(), question=None):
    by_label = {e.label: e for e in evidence}
    evidence_text = "\n".join(e.text for e in evidence).lower()
    labels = list(dict.fromkeys(labels_in(answer) + list(cited_labels or [])))
    rep = CitationReport()
    for lab in labels:
        e = by_label.get(lab)
        if e is None:
            rep.unknown.append(lab)
        elif not has_metadata(e):
            rep.missing_metadata.append(lab)
        else:
            rep.valid.append(lab)
    rep.uncited_answer = not labels_in(answer)
    # claim-level token support and history marking
    units = claim_units(answer)
    for i, unit in enumerate(units):
        own = labels_in(unit)
        if not own and "\n" in unit and i + 1 < len(units):
            # a code block without its own citation may be cited on the line right after it ("This example ... [E4]");
            # its tokens are still checked against those passages
            own = labels_in(units[i + 1])
        unit_labels = [l for l in own if l in by_label]
        toks = api_tokens(unit, known_identifiers)
        abstained = _abstained(unit, toks, question, evidence_text)
        rep.abstained_identifiers.extend(t for t in abstained if t not in rep.abstained_identifiers)
        toks = [t for t in toks if t not in abstained]
        if toks and not own:
            rep.uncited_claims.append(unit.strip()[:160])
            continue
        text = "\n".join(by_label[l].text for l in unit_labels).lower()
        for tok in toks:
            if tok.lower() not in text:
                rep.unsupported_tokens.append({"token": tok, "cited": unit_labels})
        rep.cross_operation_claims.extend(_cross_operation_claims(unit, by_label, known_identifiers))
        # textual support is not enough when the passage documents another integration than the question asks about
        if excluded_integrations and any(integration_of(by_label[l]) in excluded_integrations for l in unit_labels):
            rep.integration_mismatch.append(unit.strip()[:160])
        if unit_labels and all("historical_changelog" in by_label[l].flags for l in unit_labels) \
                and status in ("answered", "partial") and not HISTORY_WORDS.search(unit):
            rep.unmarked_historical.append(unit.strip()[:160])
    # operation alignment (only when the question identified operations deterministically)
    exp = [o for o in (expected_operations or []) if o.get("path")]
    if exp and status in ("answered", "partial"):
        low = (answer or "").lower()
        named = any(o["path"].lower() in low or o["operation"].lower() in low for o in exp)
        other_paths = [t for t in api_tokens(answer, known_identifiers) if t.startswith("/") or re.match(r"^[A-Z]+ /", t)]
        if not named and other_paths:
            rep.operation_mismatch.append({"expected": [f"{o['method']} {o['path']} ({o['operation']})" for o in exp],
                                           "answer_names": other_paths[:5]})
    return rep


def sources_for(labels, evidence):
    """Citation list for display: one entry per valid label, with KU id, title, section and source path/URL."""
    by_label = {e.label: e for e in evidence}
    out = []
    for lab in labels:
        e = by_label[lab]
        out.append({"label": lab, "ku_id": e.ku_id, "title": e.ku_title, "section": e.section, "chunk_id": e.chunk_id,
                    "origin": e.origin, "sources": [{"path": r["path"], "url": r["url"]} for r in e.source_refs]})
    return out
