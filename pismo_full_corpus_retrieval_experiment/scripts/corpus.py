"""KU-only corpus loading, isolation checks and structure-aware chunking.

Approved retrieval candidates are exactly the Markdown knowledge units under knowledge_units/<category>/KU-*.md whose
front matter carries a ku_id equal to the file name and a category equal to the folder. Everything else (marker files,
source corpus, manifests, reports, prior experiments) is rejected and the rejection is recorded.
"""
import os
import re

import yaml

from common import KU_DIR, MIG, SOURCE_CORPUS, sha_bytes

MAX_CHARS = 4000  # chunk body budget; same budget as the prior experiment's chunking v2 (a priori, not tuned)
FM_RX = re.compile(r"\A---\n(.*?)\n---\n", re.S)
FENCE_RX = re.compile(r"^\s{0,3}(```|~~~)")
HEAD_RX = re.compile(r"^(#{1,6})[ \t]+(.*?)[ \t#]*$")
SRC_BEGIN_RX = re.compile(r"^<!-- source:begin path=(\S+) part=(\S+) -->\s*$")
SRC_END = "<!-- source:end -->"
OP_RX = re.compile(r"^<!-- op: spec=(\S+) method=(\S+) path=(\S+) operationId=(\S*) -->\s*$")
SCHEMA_RX = re.compile(r"^<!-- schema: (\S+) -->\s*$")
REQUIRED_FM = ("ku_id", "title", "category", "ku_type", "lifecycle", "sources")


class IsolationError(Exception):
    pass


def approved_ku_files():
    """Return (approved relative paths, rejected [(path, reason)]). Raises IsolationError on a hard violation."""
    approved, rejected = [], []
    ku_root = os.path.realpath(KU_DIR)
    for root, dirs, files in os.walk(KU_DIR):
        dirs.sort()
        for f in sorted(files):
            full = os.path.join(root, f)
            rel = os.path.relpath(full, MIG).replace(os.sep, "/")
            real = os.path.realpath(full)
            if not real.startswith(ku_root + os.sep):
                raise IsolationError(f"{rel}: resolves outside knowledge_units ({real})")
            if not f.endswith(".md"):
                rejected.append((rel, "not a Markdown file"))
                continue
            if not f.startswith("KU-"):
                rejected.append((rel, "file name is not a KU id"))
                continue
            approved.append(rel)
    return approved, rejected


def load_ku(rel):
    with open(os.path.join(MIG, rel), "rb") as fh:
        raw = fh.read()
    text = raw.decode("utf-8")
    m = FM_RX.match(text)
    if not m:
        raise IsolationError(f"{rel}: no YAML front matter")
    fm = yaml.safe_load(m.group(1))
    for k in REQUIRED_FM:
        if k not in fm:
            raise IsolationError(f"{rel}: front matter lacks {k}")
    folder = rel.split("/")[1]
    if fm["category"] != folder:
        raise IsolationError(f"{rel}: category {fm['category']} != folder {folder}")
    if os.path.basename(rel) != fm["ku_id"] + ".md":
        raise IsolationError(f"{rel}: file name != ku_id {fm['ku_id']}")
    return {"ku_id": fm["ku_id"], "title": fm["title"], "category": fm["category"], "ku_type": fm["ku_type"],
            "lifecycle": fm["lifecycle"], "path": rel, "sha256": sha_bytes(raw), "bytes": len(raw),
            "sources": [{"path": s["path"], "url": s.get("url", ""), "sha256": s.get("sha256", ""), "role": s.get("role", "")}
                        for s in fm["sources"]],
            "operations": fm.get("operations") or [], "procedure": fm.get("procedure"), "body": text[m.end():]}


def source_corpus_hashes():
    hs = set()
    for root, _, files in os.walk(SOURCE_CORPUS):
        for f in files:
            with open(os.path.join(root, f), "rb") as fh:
                hs.add(sha_bytes(fh.read()))
    return hs


def load_corpus(check_source_copies=True):
    """Load every approved KU and run the isolation checks. Returns (kus, report)."""
    approved, rejected = approved_ku_files()
    kus, ids = [], {}
    for rel in approved:
        ku = load_ku(rel)
        if ku["ku_id"] in ids:
            raise IsolationError(f"duplicate KU id {ku['ku_id']} in {rel} and {ids[ku['ku_id']]}")
        ids[ku["ku_id"]] = rel
        kus.append(ku)
    if check_source_copies:
        src = source_corpus_hashes()
        for ku in kus:
            if ku["sha256"] in src:
                raise IsolationError(f"{ku['path']}: byte-identical to an original source file")
    report = {"approved": len(kus), "rejected": [{"path": p, "reason": r} for p, r in rejected],
              "unique_ku_ids": len(ids), "unique_content_hashes": len({k["sha256"] for k in kus})}
    return kus, report


# ---------------------------------------------------------------- chunking
def slug(s, n=60):
    s = re.sub(r"[`*_\[\]()<>{}'\"]", "", s.lower())
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s[:n].strip("-") or "section"


def parse_sections(ku):
    """Split a KU body into heading-delimited sections, tracking heading path, source block and API operation."""
    title = ku["title"]
    outer = []  # (level, text) for KU-generated headings
    inner = []  # headings inside a verbatim source block
    sections = []
    cur = {"path": [title], "lines": [], "src": None, "op": None}
    in_fence = False
    src = None
    src_outer = None
    pending_op = None
    op = None

    carry = []  # heading-only sections are carried into the next section instead of becoming empty chunks

    def new_section(path):
        nonlocal cur, carry
        content = [l for l in cur["lines"] if l.strip() and not HEAD_RX.match(l)]
        if content:
            sections.append(cur)
        elif cur["lines"] and cur["src"] == src:
            carry = carry + [l for l in cur["lines"] if l.strip()] + [""]
        cur = {"path": path, "lines": list(carry) if cur["src"] == src else [], "src": src, "op": op}
        carry = []

    for line in ku["body"].split("\n"):
        if FENCE_RX.match(line):
            in_fence = not in_fence
            cur["lines"].append(line)
            continue
        if not in_fence:
            mb = SRC_BEGIN_RX.match(line)
            if mb:  # provenance marker: recorded as chunk metadata (source_path), not indexed
                src, src_outer, inner = mb.group(1), [t for _, t in outer], []
                new_section([title] + src_outer)
                continue
            if line.strip() == SRC_END and src is not None:
                src = None
                new_section([title] + [t for _, t in outer])
                continue
            mo = OP_RX.match(line)
            if mo:
                pending_op = mo.group(4) or f"{mo.group(2)} {mo.group(3)}"
                continue  # marker is provenance metadata; kept on the chunk, not in the indexed text
            if SCHEMA_RX.match(line):
                continue
            mh = HEAD_RX.match(line)
            if mh:
                lvl, txt = len(mh.group(1)), mh.group(2).strip()
                if src is not None:
                    inner = [(l, t) for l, t in inner if l < lvl] + [(lvl, txt)]
                    path = [title] + src_outer + [t for _, t in inner]
                else:
                    if lvl == 1:
                        outer = []
                        path = [title]
                    else:
                        outer = [(l, t) for l, t in outer if l < lvl] + [(lvl, txt)]
                        path = [title] + [t for _, t in outer]
                    if pending_op is not None:
                        op, pending_op = pending_op, None
                    elif lvl <= 3:
                        op = None
                new_section(path)
                cur["lines"].append(line)
                continue
        cur["lines"].append(line)
    if cur["lines"] and any(l.strip() for l in cur["lines"]):
        sections.append(cur)
    return sections


def group_key(sec):
    """Sections sharing a key may be packed together: one API operation, or one top-level section of a source block / KU."""
    if sec["op"]:
        return ("op", sec["op"])
    p = sec["path"]
    return ("sec", sec["src"], tuple(p[:3] if sec["src"] else p[:2]))


def _blocks(lines):
    """Split lines into atomic blocks: fenced code, table, or paragraph."""
    blocks, i, n = [], 0, len(lines)
    while i < n:
        l = lines[i]
        if FENCE_RX.match(l):
            j = i + 1
            while j < n and not FENCE_RX.match(lines[j]):
                j += 1
            blocks.append(("code", lines[i:j + 1]))
            i = j + 1
        elif l.lstrip().startswith("|"):
            j = i
            while j < n and lines[j].lstrip().startswith("|"):
                j += 1
            blocks.append(("table", lines[i:j]))
            i = j
        else:
            j = i
            while j < n and lines[j].strip() and not FENCE_RX.match(lines[j]) and not lines[j].lstrip().startswith("|"):
                j += 1
            if j == i:
                j = i + 1
            blocks.append(("para", lines[i:j]))
            i = j
    return blocks


def _hard_lines(lines, budget):
    out = []
    for l in lines:
        while len(l) > budget:
            out.append(l[:budget])
            l = l[budget:]
        out.append(l)
    return out


def _split_block(kind, lines, budget):
    """Split one oversized block, repeating table headers and reopening code fences."""
    if kind == "table" and len(lines) > 2 and re.match(r"^\s*\|[\s:\-|]+\|\s*$", lines[1]):
        head, rows = lines[:2], lines[2:]
        hb = sum(len(x) + 1 for x in head)
        parts, cur, size = [], [], hb
        for r in _hard_lines(rows, max(200, budget - hb)):
            if cur and size + len(r) + 1 > budget:
                parts.append(head + cur)
                cur, size = [], hb
            cur.append(r)
            size += len(r) + 1
        if cur:
            parts.append(head + cur)
        return parts
    if kind == "code":
        opener = lines[0]
        closer = lines[-1] if len(lines) > 1 and FENCE_RX.match(lines[-1]) else "```"
        body = lines[1:-1] if len(lines) > 1 and FENCE_RX.match(lines[-1]) else lines[1:]
        ob = len(opener) + len(closer) + 2
        parts, cur, size = [], [], ob
        for r in _hard_lines(body, max(200, budget - ob)):
            if cur and size + len(r) + 1 > budget:
                parts.append([opener] + cur + [closer])
                cur, size = [], ob
            cur.append(r)
            size += len(r) + 1
        if cur:
            parts.append([opener] + cur + [closer])
        return parts
    parts, cur, size = [], [], 0
    for r in _hard_lines(lines, budget):
        if cur and size + len(r) + 1 > budget:
            parts.append(cur)
            cur, size = [], 0
        cur.append(r)
        size += len(r) + 1
    if cur:
        parts.append(cur)
    return parts


def split_lines(lines, budget=MAX_CHARS):
    """Pack blocks into pieces of at most `budget` characters, splitting only oversized blocks."""
    if sum(len(l) + 1 for l in lines) <= budget:
        return [lines]
    pieces, cur, size = [], [], 0
    for kind, bl in _blocks(lines):
        bsize = sum(len(l) + 1 for l in bl)
        if bsize > budget:
            if cur:
                pieces.append(cur)
                cur, size = [], 0
            pieces.extend(_split_block(kind, bl, budget))
            continue
        if cur and size + bsize > budget:
            pieces.append(cur)
            cur, size = [], 0
        cur.extend(bl)
        size += bsize
    if cur:
        pieces.append(cur)
    return pieces


def _procedure_role(ku, t, role):
    """True when the chunk holds a source heading that the KU's curated `procedure` front matter lists for `role`
    (the overview, or one of the detailed steps). KUs without that field never get these flags."""
    pr = ku.get("procedure")
    if not pr:
        return False
    want = {pr["overview"]} if role == "overview" else set(pr["steps"])
    return any((m := HEAD_RX.match(l)) and m.group(2).strip() in want for l in t.split("\n"))


FLAG_RULES = {
    "historical_changelog": lambda ku, t: ku["ku_type"] == "changelog_history",
    "procedure_overview": lambda ku, t: _procedure_role(ku, t, "overview"),
    "procedure_step": lambda ku, t: _procedure_role(ku, t, "steps"),
    "deprecated_operation": lambda ku, t: "**Deprecated in specification:** **yes**" in t,
    "unresolved_operation_link": lambda ku, t: "not found in the current OpenAPI" in t,
    "removal_register": lambda ku, t: ku["ku_id"] in ("KU-LIFE-api-endpoints-removed", "KU-LIFE-marketplace-endpoint-removal"),
    "not_documented_statement": lambda ku, t: "not documented in the available source corpus" in t.lower(),
}


def chunk_ku(ku, budget=MAX_CHARS):
    sections = parse_sections(ku)
    groups = []
    for sec in sections:
        size = sum(len(l) + 1 for l in sec["lines"])
        if groups and group_key(groups[-1][-1]) == group_key(sec) and \
                sum(len(l) + 1 for s in groups[-1] for l in s["lines"]) + size <= budget:
            groups[-1].append(sec)
        else:
            groups.append([sec])
    chunks, seen = [], {}
    for g in groups:
        lines = [l for s in g for l in s["lines"]]
        path = g[0]["path"]  # heading path of the first section in the group; later subsections are in the body
        pieces = split_lines(lines, budget)
        base = f"{ku['ku_id']}::{section_key(g[0], len(path))}"
        n = seen.get(base, 0) + 1
        seen[base] = n
        if n > 1:
            base += f"~{n}"
        for i, piece in enumerate(pieces, 1):
            body = "\n".join(piece).strip("\n")
            if not body.strip():
                continue
            cid = base if len(pieces) == 1 else f"{base}::p{i:02d}"
            heading_path = path
            chunks.append({
                "chunk_id": cid, "ku_id": ku["ku_id"], "ku_title": ku["title"], "ku_path": ku["path"],
                "category": ku["category"], "ku_type": ku["ku_type"], "lifecycle": ku["lifecycle"],
                "heading_path": heading_path, "section_heading": heading_path[-1],
                "parent_heading": heading_path[-2] if len(heading_path) > 1 else "",
                "part": i, "parts": len(pieces), "source_path": g[0]["src"], "operation": g[0]["op"],
                "ku_sources": [s["path"] for s in ku["sources"]],
                "source_refs": [{"path": s["path"], "url": s["url"], "sha256": s["sha256"]} for s in ku["sources"]
                                if g[0]["src"] in (None, s["path"])],
                "flags": sorted(f for f, rule in FLAG_RULES.items() if rule(ku, body)),
                "text": body, "chars": len(body), "sha256": sha_bytes(body.encode("utf-8")),
            })
    return chunks


def section_key(sec, _n=None):
    """Readable, stable section identity: operationId for API operations, source stem + inner headings for verbatim
    source content, heading path for generated KU sections. Positional suffixes are used only to break ties."""
    p = sec["path"]
    if sec["op"]:
        tail = [] if p[-1].startswith("`") else [slug(p[-1], 40)]
        return ".".join(["op-" + slug(sec["op"], 80)] + tail)
    if sec["src"]:
        stem = os.path.splitext(os.path.basename(sec["src"]))[0]
        n_outer = 0
        for i, h in enumerate(p):
            if h.startswith("Source ") and "`" in h:
                n_outer = i + 1
        inner = p[n_outer:] if n_outer else p[1:]
        return ".".join(["src-" + slug(stem, 50)] + [slug(h, 40) for h in inner])
    return ".".join(slug(h, 40) for h in p[1:]) or "intro"


def index_text(ch):
    """The exact text every method indexes: context header (KU title and heading path) + chunk body."""
    return f"{ch['ku_title']}\n{' > '.join(ch['heading_path'][1:])}\n{ch['text']}"
