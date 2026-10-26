"""Evidence assembly: the retrieved chunks plus small, additive, deterministic expansions.

0. procedure steps   - when a retrieved chunk is the overview of a source-declared ordered procedure (chunk flag
                       procedure_overview, set only for KUs whose curated front matter declares one), the chunks holding
                       its detailed steps (flag procedure_step), in document order;
1. linked operations - API operation chunks that a retrieved guide chunk links to (author's /reference/<slug> links);
2. operation events  - the chunk holding the "Events emitted" table of an operation already in the evidence;
3. lifecycle notes   - the "Lifecycle status" chunk of a KU already in the evidence when it warns about removed or
                       unresolved endpoints.
Retrieved chunks keep their order and are never dropped. Each evidence item carries its exact chunk text.
"""
import re
from dataclasses import dataclass

from . import config
from .retrieval import Hit

REF_LINK = re.compile(r"\]\((?:https?://developers\.pismo\.io)?/?(?:pismo-docs/)?reference(?:-link)?/([A-Za-z0-9_\-]+)|\]\(ref:([A-Za-z0-9_\-]+)")
EVENTS_HEADING = "#### Events emitted"
REGISTER_KU = "KU-LIFE-api-endpoints-removed"
LIFECYCLE_INTENT = re.compile(r"remov|decommission|deprecat|\bstill\b|availab|retire|sunset|discontinu", re.I)
PATH_RX = re.compile(r"/[A-Za-z0-9{}'_\-.*]+(?:/[A-Za-z0-9{}'_\-.*]+)+")


def _norm_path(p):
    """Compare paths without escapes, MDX quoting or placeholder names: /a/{'{id}'}/b -> /a/{}/b."""
    p = re.sub(r"\{'?\{?([^}']*)\}?'?\}", "{}", p.replace("\\", ""))
    return p.lower().rstrip("/")


ERROR_CODE = re.compile(r"\b[A-Z][A-Z0-9]{1,9}[0-9]{3,6}\b")
ERROR_ROW = re.compile(r"^\| `([A-Z][A-Z0-9]{1,9}[0-9]{3,6})` \|", re.M)
OP_HEADING = re.compile(r"^### `([A-Z]+) ([^`]+)` — (.+)$", re.M)
LIFECYCLE_WARNING = re.compile(r"removed|not found in the current OpenAPI|conflicting sources|decommission", re.I)


@dataclass
class Evidence:
    label: str          # E1, E2, ... (what the generator cites)
    chunk_id: str
    ku_id: str
    ku_title: str
    section: str
    text: str           # exact chunk text passed to the generator
    source_refs: list   # [{path, url, sha256}]
    flags: list
    origin: str
    reason: str


class OperationIndex:
    """operationId (lower-case) -> chunks of that operation, built from chunk metadata."""

    def __init__(self, chunks):
        self.ops = {}
        for c in chunks:
            op = c.get("operation")
            if op:
                self.ops.setdefault(op.lower(), []).append(c)
        self.lifecycle = {c["ku_id"]: c for c in chunks if c["section_heading"] == "Lifecycle status"}
        # (KU, source file) -> chunks holding the detailed steps of a source-declared procedure, in document order
        self.procedure_steps = {}
        for c in chunks:
            if "procedure_step" in (c.get("flags") or []):
                self.procedure_steps.setdefault((c["ku_id"], c.get("source_path")), []).append(c)
        # removed endpoints: rows of the structured removal register (| n | API | section | names | URLs | date | in specs |)
        self.removed = []
        for c in chunks:
            if c["ku_id"] == REGISTER_KU and "::structured-removal-register" in c["chunk_id"]:
                for line in c["text"].split("\n"):
                    cells = [x.strip() for x in line.strip().strip("|").split("|")]
                    if len(cells) >= 6 and cells[0].isdigit():
                        self.removed.append({"row": int(cells[0]), "api": cells[1], "names": [n.strip() for n in cells[3].split(";")],
                                             "paths": [_norm_path(p) for p in PATH_RX.findall(cells[4].replace("\\", ""))], "chunk": c})
        # error code -> the error-catalogue chunk holding its row (rows look like "| `EIBA0005` | 400 | message | ...")
        self.error_rows = {}
        for c in chunks:
            if c["ku_type"] == "error_catalogue":
                for code in ERROR_ROW.findall(c["text"]):
                    self.error_rows.setdefault(code, c)
        # method, path and summary from each operation's heading: ### `POST /payment-methods/v2/transfers` — Create transfer
        self.meta = {}
        for op, cs in self.ops.items():
            for c in cs:
                m = OP_HEADING.search(c["text"])
                if m:
                    self.meta[op] = {"operation": c["operation"], "method": m.group(1), "path": m.group(2), "summary": m.group(3).strip()}
                    break

    def operation_chunks(self, op_id):
        return self.ops.get(op_id.lower(), [])

    def events_chunk(self, op_id):
        for c in self.operation_chunks(op_id):
            if EVENTS_HEADING in c["text"]:
                return c
        return None

    def events_for(self, op_id):
        """Event slugs listed in the operation's 'Events emitted' table (from endpoint_event_map.csv)."""
        c = self.events_chunk(op_id)
        if not c:
            return []
        part = c["text"].split(EVENTS_HEADING, 1)[1].split("\n#### ", 1)[0]
        return re.findall(r"^\| `([a-z0-9][a-z0-9\-]*)` \|", part, re.M)


def linked_operation_ids(text):
    return [a or b for a, b in REF_LINK.findall(text)]


OP_TOKEN = re.compile(r"[A-Za-z][A-Za-z0-9_\-]{4,}")
ARTICLES = {"a", "an", "the"}


def named_operation_ids(question, op_index):
    """operationIds written verbatim in the question (exact, case-insensitive token match against the spec ids)."""
    return [t for t in dict.fromkeys(OP_TOKEN.findall(question or ""))
            if t.lower() in op_index.ops and ("-" in t or "_" in t or any(ch.isupper() for ch in t[1:]))]


def _words(text):
    return [w for w in re.findall(r"[a-z0-9]+", (text or "").lower()) if w not in ARTICLES]


def summary_operation_ids(question, op_index, max_ops=config.MAX_SUMMARY_OPERATIONS):
    """Operations whose spec summary (at least two words, e.g. 'Create transfer') occurs as a whole phrase in the
    question, ignoring case, punctuation and articles. Only the longest matching phrases are kept, so 'create a transfer
    schedule' matches 'Create transfer schedule' and not also 'Create transfer'. Operations sharing one summary are
    ambiguous beyond max_ops and are then skipped."""
    q = " " + " ".join(_words(question)) + " "
    found = {}
    for op, m in op_index.meta.items():
        s = _words(m["summary"])
        if len(s) >= 2 and f" {' '.join(s)} " in q:
            found.setdefault(" ".join(s), []).append(m["operation"])
    phrases = [p for p in found if not any(p != o and f" {p} " in f" {o} " for o in found)]
    out = []
    for p in sorted(phrases, key=lambda p: (-len(p), p)):
        ops = sorted(found[p])
        if len(ops) <= max_ops:
            out.extend(ops)
    return out[:max_ops]


def removed_endpoint_rows(question, op_index):
    """Removal-register rows the question identifies: an endpoint name of 2+ words as a whole phrase, an endpoint path
    (escapes and placeholder names ignored), or '<API name> API'. Deterministic; returns rows with the match reason."""
    q = " " + " ".join(_words(question)) + " "
    q_paths = {_norm_path(p) for p in PATH_RX.findall(question or "")}
    out = []
    for r in getattr(op_index, "removed", []):
        why = None
        for n in r["names"]:
            w = _words(n)
            if len(w) >= 2 and f" {' '.join(w)} " in q:
                why = f"names '{n}'"
                break
        if not why and q_paths & set(r["paths"]):
            why = "names its path"
        api = _words(r["api"])
        if not why and api and f" {' '.join(api)} api " in q and LIFECYCLE_INTENT.search(question or ""):
            why = f"names the {r['api']} API"
        if why:
            out.append(dict(r, why=why))
    return out


def matched_operations(question, op_index):
    """Operations the question identifies deterministically: by operationId, then by exact summary phrase."""
    out = []
    for op in named_operation_ids(question, op_index):
        out.append((op, "operationId"))
    for op in summary_operation_ids(question, op_index):
        if op.lower() not in {o.lower() for o, _ in out}:
            out.append((op, "summary"))
    return [dict(op_index.meta.get(op.lower(), {"operation": op}), matched_by=how) for op, how in out]


def assemble(hits, op_index, max_linked=config.MAX_LINKED_OPERATIONS, max_events=config.MAX_EVENT_CHUNKS,
             max_lifecycle=config.MAX_LIFECYCLE_CHUNKS, link_from_top=config.LINK_FROM_TOP, question=None,
             max_procedure=config.MAX_PROCEDURE_STEPS, exclude=None):
    """`exclude(chunk) -> bool` (integration scoping, pipeline.Assistant.evidence) also applies to every expansion."""
    items = list(hits)
    seen = {h.chunk_id for h in items}

    def add(chunk, origin, reason):
        if chunk["chunk_id"] in seen or (exclude is not None and exclude(chunk)):
            return False
        seen.add(chunk["chunk_id"])
        items.append(Hit(chunk, len(items) + 1, origin, reason))
        return True

    # 0. operations the question identifies explicitly - by operationId ("which event does post-transfers emit?") or by
    #    the operation's exact summary phrase ("... when I create a transfer?" -> Create transfer / post-transfers)
    matched = matched_operations(question, op_index)
    for m in matched:
        why = (f"question names operationId {m['operation']}" if m["matched_by"] == "operationId"
               else f"question contains the operation summary '{m.get('summary')}' ({m['operation']})")
        add(op_index.operation_chunks(m["operation"])[0], "named_operation", why)
    # 0b. error codes in the question -> their error-catalogue row (code, HTTP status, message, operations), which
    #     otherwise ranks below the many API response examples that merely quote the code
    for code in dict.fromkeys(ERROR_CODE.findall(question or "") if config.ENABLE_ERROR_CATALOGUE_LOOKUP else []):
        row = op_index.error_rows.get(code)
        if row:
            add(row, "error_catalogue", f"catalogue entry for error code {code}")
    # 0c. removed endpoints the question names (by endpoint name, path or "<API> API") -> their removal-register row
    for r in (removed_endpoint_rows(question, op_index) if config.ENABLE_REMOVAL_REGISTER_LOOKUP else [])[:config.MAX_REGISTER_ROWS]:
        add(r["chunk"], "removal_register", f"removal register row {r['row']} ({r['why']})")
    # 0d. a retrieved overview of a source-declared procedure -> its detailed step sections (the source says the
    #     following sections explain the steps; ranking alone leaves the long step sections out of the top-k)
    n = 0
    for h in hits:
        if "procedure_overview" in (h.chunk.get("flags") or []):
            for c in op_index.procedure_steps.get((h.chunk["ku_id"], h.chunk.get("source_path")), []):
                if n < max_procedure and add(c, "procedure_step", f"detailed step of the procedure in {h.chunk_id}"):
                    n += 1

    # 1. operations linked from the top retrieved guide source text (not KU navigation sections, and not changelogs,
    #    which link many unrelated operations)
    n = 0
    for h in hits[:link_from_top]:
        if h.chunk["ku_type"] != "workflow_guide" or not h.chunk.get("source_path"):
            continue
        for slug in linked_operation_ids(h.chunk["text"]):
            ops = op_index.operation_chunks(slug)
            if ops and n < max_linked and add(ops[0], "linked_operation", f"linked from {h.chunk_id} ({slug})"):
                n += 1
    # 2. "Events emitted" tables: operations the question identified come first, then other operations in the evidence
    n = 0
    explicit = [h for h in items if h.origin == "named_operation"]
    for h in explicit + [h for h in list(items) if h.origin != "named_operation"]:
        op = h.chunk.get("operation")
        if op and n < max_events:
            ev = op_index.events_chunk(op)
            if ev and add(ev, "operation_events", f"events emitted by {op}"):
                n += 1
    # 3. lifecycle warnings of KUs present in the evidence
    n = 0
    for ku in dict.fromkeys(h.chunk["ku_id"] for h in list(items)):
        lc = op_index.lifecycle.get(ku)
        if lc and n < max_lifecycle and LIFECYCLE_WARNING.search(lc["text"]) and add(lc, "lifecycle", f"lifecycle warning for {ku}"):
            n += 1
    return [to_evidence(h, i) for i, h in enumerate(items, 1)]


def to_evidence(hit, i):
    c = hit.chunk
    return Evidence(label=f"E{i}", chunk_id=c["chunk_id"], ku_id=c.get("ku_id", ""), ku_title=c.get("ku_title", ""),
                    section=" > ".join(c.get("heading_path", [])[1:]) or c.get("section_heading", ""), text=c.get("text", ""),
                    source_refs=c.get("source_refs") or [], flags=c.get("flags") or [], origin=hit.origin, reason=hit.reason)
