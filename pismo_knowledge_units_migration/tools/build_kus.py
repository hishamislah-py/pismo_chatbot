"""Phase B/C: build the knowledge units (KUs) from the authoritative corpus. Read-only on the corpus.

Usage: python -B -E -s build_kus.py [--only KU-ID,KU-ID,...]
Writes knowledge_units/**, MIGRATION_MANIFEST.csv, SOURCE_COVERAGE.csv, work/ku_index.json, work/build_log.json.
With --only, all KUs are planned (so related links resolve) but only the listed KUs are written (pilot runs).
"""
import argparse, html, re, shutil, sys
from collections import Counter, defaultdict, OrderedDict
import yaml
from common import *
from ku_plan import CATEGORIES, AREA_DEFAULT, OVERRIDES, GROUPS, SPLIT_BYTES, PART_BYTES, API_SPLIT_BYTES
from spec_model import Spec, render_operation, render_named_schemas, cell, quote_block, jdump

ap = argparse.ArgumentParser()
ap.add_argument("--only", default="")
args = ap.parse_args()
ONLY = {x.strip() for x in args.only.split(",") if x.strip()}

an = load_json(os.path.join(WORK, "analysis.json"))
inv = {r["source_path"]: r for r in csv.DictReader(open(os.path.join(MIG, "archived_source_inventory", "SOURCE_INVENTORY.csv"), encoding="utf-8"))}
smap = load_source_map()
LOG = {"warnings": [], "unresolved_refs": [], "kind_mismatch_refs": []}

# link text may contain escaped characters such as \[beta\]
REF_LINK = re.compile(r"\[((?:\\.|[^\]\\])*)\]\((?:https?://developers\.pismo\.io)?/?(?:pismo-docs/)?reference(?:-link)?/([A-Za-z0-9_\-]+)[^)]*\)"
                      r"|\[((?:\\.|[^\]\\])*)\]\(ref:([A-Za-z0-9_\-]+)[^)]*\)")
DOC_LINK = re.compile(r"(?:https?://developers\.pismo\.io)?/pismo-docs/docs/([A-Za-z0-9_\-]+)|\(doc:([A-Za-z0-9_\-]+)")
EVENT_LINK = re.compile(r"developers\.pismo\.io/events/docs/([A-Za-z0-9_\-]+)")
EMPTY_LINK = re.compile(r"\[([^\]]+)\]\(\)")
HEAD = re.compile(r"^(\s{0,3})(#{1,6})\s+(.+?)\s*#*\s*$")


def norm_space(s):
    return re.sub(r"\s+", " ", s).strip()


def raw_cell(s):
    """Table cell for raw multi-line source text: line breaks shown as ' ⏎ ', nothing else changed."""
    return cell(re.sub(r"[ \t]*(?:\r\n|\r|\n)\s*", " ⏎ ", s.strip()))


def joined_paths(raw):
    """Join path fragments split by line breaks (the register uses bare CR inside paths). Used only for matching."""
    return re.sub(r"\s*(?:\r\n|\r|\n)\s*", "", raw.replace("\\", ""))


def key_to_path(k):
    return k + ".md" if k.startswith("api-specs/") else f"docs/{k}.md"


def headings(body):
    out, fence = [], False
    for i, l in enumerate(body.split("\n")):
        if re.match(r"^\s*(```|~~~)", l):
            fence = not fence
            continue
        m = None if fence else HEAD.match(l)
        if m:
            out.append((i, len(m.group(2)), m.group(3).strip()))
    return out


def first_paragraph(body):
    lines, fence, buf = body.split("\n"), False, []
    for l in lines:
        if re.match(r"^\s*(```|~~~)", l):
            fence = not fence
            if buf:
                break
            continue
        if fence:
            continue
        s = l.strip()
        if not s:
            if buf:
                break
            continue
        if s.startswith(("#", "<", "!", "|", ">", "[block:", "---")) or s.startswith("{"):
            if buf:
                break
            continue
        buf.append(l)
    return "\n".join(buf).strip()


# ---------------- specs, operations ----------------
SPECS = {p: Spec(p) for p in sorted(inv) if inv[p]["source_type"] == "openapi_yaml"}
OPS = []          # dicts: spec, method, path, op, item, opid, tag
for p, sp in SPECS.items():
    for path, m, op, item in sp.operations():
        OPS.append({"spec": p, "method": m, "path": path, "op": op, "item": item, "opid": op.get("operationId", ""),
                    "tag": (op.get("tags") or ["(untagged)"])[0], "summary": op.get("summary", "")})
OPS_BY_ID = defaultdict(list)
for o in OPS:
    OPS_BY_ID[o["opid"].lower()].append(o)
stem = lambda p: os.path.basename(p)[:-5]
EVENTS_BY_OP = defaultdict(list)
for r in read_csv_rel("api-reference-data/endpoint_event_map.csv"):
    EVENTS_BY_OP[(r["spec_file"], r["method"].upper(), r["path"])].append(r)
CATALOG = {(r["spec_file"], r["method"].upper(), r["path"]): r for r in read_csv_rel("api-reference-data/operations_catalog.csv")}
EVENT_INV = read_csv_rel("api-reference-data/event_type_inventory.csv")
ERRORS = read_csv_rel("api-reference-data/error_code_index.csv")

# ---------------- KU registry ----------------
KUS = OrderedDict()   # id -> dict
COVER = []            # source_path, ku_id, section, content_type, basis, notes


def cat_code(cat):
    return CATEGORIES[cat][0]


def add_ku(kid, **kw):
    if kid in KUS:
        raise SystemExit(f"duplicate KU id {kid}")
    kw.setdefault("related", set()); kw.setdefault("operations", []); kw.setdefault("events", []); kw.setdefault("codes", [])
    KUS[kid] = dict(id=kid, **kw)
    return KUS[kid]


def cover(src, kid, section, ctype, basis, notes=""):
    COVER.append({"source_path": src, "ku_id": kid, "source_section_or_operation": section, "content_type": ctype,
                  "mapping_basis": basis, "validation_status": "pending", "notes": notes})


# ---- API reference KU plan (spec x first tag), split later by size ----
API_GROUPS = OrderedDict()
for o in OPS:
    API_GROUPS.setdefault((o["spec"], o["tag"]), []).append(o)
OP_API_KU = {}
for (sp, tag), ops in API_GROUPS.items():
    base = f"KU-API-{slugify(stem(sp), 50)}--{slugify(tag, 40)}"
    for o in ops:
        OP_API_KU[id(o)] = base   # parts resolved after rendering (base id kept as group id)

# ---- guide KU plan ----
guide_paths = [p for p in inv if inv[p]["source_type"] in ("guide_markdown", "spec_repository_readme")]
assigned = {}
plan_guides = []   # (kid, category, title, [paths], rationale)
for cat, slug, title, keys, why in GROUPS:
    paths = [key_to_path(k) for k in keys]
    for p in paths:
        if p not in inv:
            raise SystemExit(f"GROUPS: unknown source {p}")
        if p in assigned:
            raise SystemExit(f"GROUPS: {p} assigned twice")
        assigned[p] = f"KU-{cat_code(cat)}-{slug}"
    plan_guides.append((f"KU-{cat_code(cat)}-{slug}", cat, title, paths, why))
for k in OVERRIDES:
    if key_to_path(k) not in inv:
        raise SystemExit(f"OVERRIDES: unknown source {k}")
for p in sorted(guide_paths):
    if p in assigned:
        continue
    area = p.split("/")[1]
    k = p[len("docs/"):-3]
    cat = OVERRIDES.get(k, AREA_DEFAULT[area])
    kid = f"KU-{cat_code(cat)}-{slugify(os.path.basename(p)[:-3])}"
    if kid in {x[0] for x in plan_guides}:
        kid = f"KU-{cat_code(cat)}-{slugify(area)}-{slugify(os.path.basename(p)[:-3])}"
    assigned[p] = kid
    plan_guides.append((kid, cat, smap[p]["title"], [p], "single source page"))
missing = [p for p in guide_paths if p not in assigned]
if missing:
    raise SystemExit(f"unassigned guides: {missing}")
GUIDE_KU = dict(assigned)        # path -> primary KU id (before splitting)

# ---- slug -> guide KU for doc links ----
DOC_SLUG = {os.path.basename(p)[:-3].lower(): p for p in inv if p.endswith(".md") and (p.startswith("docs/") or p.startswith("changelog/"))}

# ---- removal register parse (api-endpoints-removed.md) ----
REMOVED_PATH = "docs/resources/api-endpoints-removed.md"


def parse_removal_rows():
    t = read_text(REMOVED_PATH)
    rows = []
    for tr in re.findall(r"<tr>(.*?)</tr>", t, re.S):
        cells = re.findall(r"<td[^>]*?(?:/>|>(.*?)</td>)", tr, re.S)
        if len(cells) != 5:
            continue
        clean = [norm_space(re.sub(r"<br\s*/?>", " ", html.unescape(c or ""))) for c in cells]
        raw = [c or "" for c in cells]
        names = [norm_space(x) for x in re.split(r"\n\s*\n|<br\s*/?>", raw[2]) if norm_space(re.sub(r"<[^>]+>", "", x))]
        names = [re.sub(r"<[^>]+>", "", n).strip() for n in names]
        rows.append({"api": clean[0], "section": clean[1], "names": [n for n in names if n], "urls_raw": raw[3].strip(), "date_raw": clean[4]})
    return rows


REMOVED_ROWS = parse_removal_rows()
REMOVED_NAMES = defaultdict(list)
for r in REMOVED_ROWS:
    for n in r["names"]:
        REMOVED_NAMES[n.lower()].append(r)

# link texts used for each unresolved slug across the corpus
SLUG_TEXTS = defaultdict(set)
for p in inv:
    if p.endswith(".md"):
        for a, b, c, d in REF_LINK.findall(split_front_matter(read_text(p))[1]):
            SLUG_TEXTS[(b or d).lower()].add(norm_space(a or c))
SUMMARY_OPS = defaultdict(list)
for o in OPS:
    SUMMARY_OPS[norm_space(o["summary"]).lower()].append(o)


def slug_status(slug):
    """Classify an operation link slug. Returns (resolved_ops, note)."""
    ops = OPS_BY_ID.get(slug, [])
    if ops:
        note = "" if len(ops) == 1 else f"operationId `{ops[0]['opid']}` occurs in {len(ops)} specification files; the link does not say which one"
        return ops, note
    texts = sorted(SLUG_TEXTS.get(slug, []))
    hits = []
    for t in texts:
        for r in REMOVED_NAMES.get(t.lower(), []):
            hits.append(f"link text \"{t}\" equals the endpoint name \"{t}\" in the removed-endpoints list (row {r['api']} / {r['section']}, date removed `{r['date_raw']}`)")
    same = [f"`{o['opid']}` ({o['method'].upper()} {o['path']})" for t in texts for o in SUMMARY_OPS.get(t.lower(), [])]
    if hits:
        note = ("not found in the current OpenAPI specifications. Name-based inference: " + "; ".join(sorted(set(hits))) +
                ". This is a match on the endpoint name, not on an identifier.")
        if same:
            note += " A current operation has the same summary (" + ", ".join(sorted(set(same))) + "); no source states that it replaces the removed endpoint."
        return [], note
    return [], ("not found in the current OpenAPI specifications and not matched to any removed-endpoint entry; "
                "status unverified (possible rename, typo or undocumented removal)")


# ---------------- event catalogue plan ----------------
ev_by_domain = defaultdict(list)
for r in EVENT_INV:
    ev_by_domain[r["domain_guess"]].append(r)
EVENT_KU = {}
small = sorted(d for d, rs in ev_by_domain.items() if len(rs) < 3)
for d in sorted(ev_by_domain):
    kid = "KU-EVT-catalogue-" + (slugify(d) if d not in small else "other-domains")
    for r in ev_by_domain[d]:
        EVENT_KU[r["event_slug"]] = kid

# ---------------- error catalogue plan ----------------
def prefix(code):
    m = re.match(r"[A-Za-z]+", code)
    return m.group(0) if m else "other"


pref_count = Counter(prefix(r["code"]) for r in ERRORS)
ERR_KU = {}
minor = sorted(p for p, c in pref_count.items() if c < 15)
chunks, cur, n = [], [], 0
for p in minor:
    if n + pref_count[p] > 120 and cur:
        chunks.append(cur); cur, n = [], 0
    cur.append(p); n += pref_count[p]
if cur:
    chunks.append(cur)
for p, c in pref_count.items():
    if c >= 15:
        ERR_KU[p] = f"KU-ERR-codes-{slugify(p)}"
for ch in chunks:
    kid = f"KU-ERR-codes-{slugify(ch[0])}-to-{slugify(ch[-1])}"
    for p in ch:
        ERR_KU[p] = kid
CODE_KU = {r["code"]: ERR_KU[prefix(r["code"])] for r in ERRORS}

# ---------------- rendering helpers ----------------
def front(meta):
    return "---\n" + yaml.safe_dump(meta, sort_keys=False, allow_unicode=True, width=10_000) + "---\n"


def src_meta(p, role):
    r = inv[p]
    return {"path": p, "sha256": r["sha256"], "url": r["source_url"], "role": role, "updated_at": r["updated_at"]}


def refs_table(srcs, sections=None):
    out = ["| Source file | Section / operation | Source URL | SHA-256 | updatedAt |", "| --- | --- | --- | --- | --- |"]
    for s in srcs:
        sec = (sections or {}).get(s["path"], "whole document")
        out.append(f"| `{s['path']}` | {cell(sec)} | {s['url']} | `{s['sha256'][:16]}…` | {s['updated_at'] or 'not stated'} |")
    return "\n".join(out)


def op_essentials(o):
    sp = SPECS[o["spec"]]
    ctx = f"{o['spec']} {o['method'].upper()} {o['path']}"
    req = []
    rb = o["op"].get("requestBody")
    if rb is not None:
        res, _, _ = sp.deref(rb, "requestBodies", ctx)
        if isinstance(res, dict):
            for media in (res.get("content") or {}).values():
                sch = (media or {}).get("schema")
                if sch:
                    props, reqset, _ = sp.collect_props(sch, ctx)
                    req = [f"`{n}`" for n, _ in props if n in reqset]
                break
    params_req = [f"`{res.get('name')}` ({res.get('in')})" for res, _ in sp.params(o["item"], o["op"], ctx) if isinstance(res, dict) and res.get("required")]
    statuses = list((o["op"].get("responses") or {}).keys())
    codes = sp.error_codes(o["op"], ctx)
    evs = EVENTS_BY_OP.get((stem(o["spec"]), o["method"].upper(), o["path"]), [])
    sec = sp.security_names(o["op"])
    return {"required_params": params_req, "required_body": req, "statuses": [str(s) for s in statuses], "codes": codes, "events": evs, "security": sec}


def ops_section(ops_list, unresolved):
    if not ops_list and not unresolved:
        return []
    L = ["## API operations referenced", "",
         "Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the "
         "current OpenAPI specifications. Full contracts are in the linked API-reference KUs.", ""]
    if ops_list:
        L += ["| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |", "| --- | --- | --- | --- | --- | --- |"]
        for o, note in ops_list:
            L.append(f"| `{o['method'].upper()} {o['path']}` | `{o['opid']}` | {cell(o['summary'])} | `{o['spec']}` | "
                     f"{'**yes**' if o['op'].get('deprecated') else 'no'} | {OP_API_KU[id(o)]} |")
        if len(ops_list) > 25:
            L += ["", f"Operation essentials are not repeated here because the source links {len(ops_list)} operations; see the API-reference KUs listed in the table."]
        else:
            L += ["", "### Operation essentials", ""]
        for o, note in (ops_list if len(ops_list) <= 25 else []):
            e = op_essentials(o)
            L.append(f"- **`{o['method'].upper()} {o['path']}`** (`{o['opid']}`): "
                     f"security {('not declared' if e['security'] is None else ' OR '.join('`'+s+'`' for s in e['security']))}; "
                     f"required parameters {', '.join(e['required_params']) or 'none declared'}; "
                     f"required body fields {', '.join(e['required_body']) or 'none declared'}; "
                     f"response statuses {', '.join(e['statuses']) or 'none declared'}; "
                     f"error codes in examples {', '.join('`'+c+'`' for _, c, _ in e['codes']) or 'none'}; "
                     f"events {', '.join('`'+x['event_slug']+'`' for x in e['events']) or 'none listed'}"
                     + (f". Note: {note}" if note else "") + ".")
    if unresolved:
        L += ["", "### Operation links that do not resolve to a current specification", "",
              "| Link slug | Link text(s) in source | Status |", "| --- | --- | --- |"]
        for slug, texts, note in unresolved:
            L.append(f"| `{slug}` | {cell('; '.join(texts))} | {cell(note)} |")
    return L + [""]


# ---------------- guide KUs ----------------
def split_body(body):
    """Split a large body into parts at heading boundaries (H2, then H3/H4, then blank lines). Returns list of (start, end) line indexes."""
    lines = body.split("\n")
    fence, cand = False, {2: [], 3: [], 4: [], 0: []}
    for i, l in enumerate(lines):
        if re.match(r"^\s*(```|~~~)", l):
            fence = not fence
            continue
        if fence:
            continue
        m = HEAD.match(l)
        if m and len(m.group(2)) in (2, 3, 4):
            cand[len(m.group(2))].append(i)
        if not l.strip():
            cand[0].append(i + 1)
    size = [len(l.encode("utf-8")) + 1 for l in lines]

    def seg_bytes(a, b):
        return sum(size[a:b])

    def split_range(a, b, levels):
        if seg_bytes(a, b) <= PART_BYTES or not levels:
            return [(a, b)]
        cuts = [c for c in cand[levels[0]] if a < c < b]
        if not cuts:
            return split_range(a, b, levels[1:])
        pieces, start = [], a
        for c in cuts + [b]:
            pieces.append((start, c)); start = c
        out = []
        for x, y in pieces:
            out += split_range(x, y, levels[1:]) if seg_bytes(x, y) > PART_BYTES else [(x, y)]
        merged = []
        for x, y in out:   # pack consecutive pieces up to PART_BYTES
            if merged and seg_bytes(merged[-1][0], y) <= PART_BYTES:
                merged[-1] = (merged[-1][0], y)
            else:
                merged.append((x, y))
        return merged

    return split_range(0, len(lines), [2, 3, 4, 0])


GUIDE_PARTS = {}   # path -> list of (kid, start, end)
for kid, cat, title, paths, why in plan_guides:
    if len(paths) == 1:
        body = split_front_matter(read_text(paths[0]))[1]
        if len(body.encode("utf-8")) > SPLIT_BYTES:
            rngs = split_body(body)
            GUIDE_PARTS[paths[0]] = [(f"{kid}-part-{i:02d}", a, b) for i, (a, b) in enumerate(rngs, 1)]


def guide_ku_ids(path):
    return [x[0] for x in GUIDE_PARTS[path]] if path in GUIDE_PARTS else [GUIDE_KU[path]]


def render_guide_ku(kid, cat, title, paths, why, part=None):
    srcs, blocks, topics, prereq, ops_list, unresolved, ev_links, empties = [], [], [], [], [], [], set(), []
    seen_ops, related, lifecycle, caveats = set(), set(), [], []
    bodies = {}
    for p in paths:
        meta, body = split_front_matter(read_text(p))
        if part:
            lines = body.split("\n")
            body = "\n".join(lines[part[1]:part[2]]) + ("\n" if part[2] < len(lines) else "")
            bodies[p] = body
        else:
            bodies[p] = body
        srcs.append(src_meta(p, "primary_guide" if inv[p]["source_type"] == "guide_markdown" else "spec_repository_readme"))
        hs = headings(body)
        topics.append((p, [h for _, lvl, h in hs if lvl in (1, 2, 3)]))
        for _, lvl, h in hs:
            if re.search(r"(?i)prerequisite|before you (begin|start)|requirements?\b|what you need", h):
                prereq.append(f"`{p}` section \"{h}\"")
        for a, b, c, d in REF_LINK.findall(body):
            slug, text = (b or d).lower(), norm_space(a or c)
            ops, note = slug_status(slug)
            if ops:
                for o in ops:
                    if id(o) not in seen_ops:
                        seen_ops.add(id(o)); ops_list.append((o, note)); related.add(OP_API_KU[id(o)])
                        if o["op"].get("deprecated"):
                            lifecycle.append(f"Links to `{o['opid']}`, which is marked `deprecated: true` in `{o['spec']}`.")
            elif slug not in [u[0] for u in unresolved]:
                unresolved.append((slug, sorted(SLUG_TEXTS.get(slug, {text})), note))
        for a, b in DOC_LINK.findall(body):
            s = (a or b).lower()
            if s in DOC_SLUG and DOC_SLUG[s] in GUIDE_KU:
                related.update(guide_ku_ids(DOC_SLUG[s]))
            elif s in DOC_SLUG and DOC_SLUG[s].startswith("changelog/"):
                related.add("KU-CHG-" + slugify(os.path.basename(DOC_SLUG[s])[:-3]))
        ev_links |= set(EVENT_LINK.findall(body))
        fm_lines = len(read_text(p).split("\n")) - len(split_front_matter(read_text(p))[1].split("\n"))
        for i, l in enumerate(body.split("\n"), 1):
            for m in EMPTY_LINK.finditer(l):
                empties.append(f"`{p}` line {fm_lines + (part[1] if part else 0) + i}: `{m.group(0)}` (empty link target, kept as published)")
        if re.search(r"(?i)\(outdated\)", inv[p]["title"]):
            lifecycle.append(f"The source title marks the page as outdated: \"{inv[p]['title']}\".")
        if re.search(r"(?i)\bbeta\b", inv[p]["title"]):
            lifecycle.append(f"The source title marks the feature as beta: \"{inv[p]['title']}\".")
    for slug, texts, note in unresolved:
        if "removed-endpoints list" in note:
            lifecycle.append(f"Links to `{slug}`, which is not in the current specifications; {note}")
    related.discard(kid)
    related |= {EVENT_KU[e] for e in ev_links if e in EVENT_KU}
    for o, _ in ops_list:
        for e in EVENTS_BY_OP.get((stem(o["spec"]), o["method"].upper(), o["path"]), []):
            if e["event_slug"] in EVENT_KU:
                related.add(EVENT_KU[e["event_slug"]])
    is_dup = len(paths) > 1 and len({sha_bytes(norm_space(b).encode()) for b in bodies.values()}) == 1
    if is_dup:
        caveats.append("The grouped source pages have identical bodies (published twice under different URLs); both are kept verbatim for traceability.")
    if any("<HTMLBlock" in b or "<Table" in b or "<details" in b for b in bodies.values()):
        caveats.append("Source content contains MDX/HTML components (for example `<Table>`, `<HTMLBlock>`, `<Callout>`, `<details>`). They are preserved exactly as published; tables inside them were not converted to Markdown.")
    if ev_links:
        caveats.append(f"The source links to {len(ev_links)} event page(s) under `/events/`. Event payload definitions are not part of the corpus (robots.txt disallows `/events/`), so payload fields are not documented here.")
    caveats += empties
    for slug, texts, note in unresolved:
        if "removed-endpoints list" not in note:
            caveats.append(f"Operation link `{slug}` does not resolve: {note}")
    ttl = title if not part else f"{title} (part {part[3]} of {part[4]})"
    meta = {"ku_id": kid, "title": ttl, "category": cat, "ku_type": "workflow_guide", "lifecycle": "current",
            "sources": srcs, "operations": sorted({o["opid"] for o, _ in ops_list}), "related_kus": sorted(related),
            "grouping_rationale": why}
    L = [front(meta), f"# {ttl}", "", f"**KU ID:** `{kid}` · **Category:** {CATEGORIES[cat][1]} · **Type:** workflow / concept guide · **Status:** current documentation", ""]
    L += ["## Purpose and scope", ""]
    L.append(f"This unit migrates {len(paths)} Pismo source document(s) " + ("(one part of a large page) " if part else "") +
             f"into one implementation-oriented unit. Grouping rationale: {why}")
    for p in paths:
        fp = first_paragraph(bodies[p])
        L += ["", f"Scope as stated in `{p}`:" if fp else f"`{p}` has no introductory paragraph."]
        if fp:
            L += ["", quote_block(fp)]
    L += ["", "## Topics covered", "", "Headings of the source content (levels 1–3), which define the use cases this unit supports:", ""]
    for p, hs in topics:
        L.append(f"- `{p}`: " + ("; ".join(hs) if hs else "no headings"))
    if prereq or ops_list:
        L += ["", "## Prerequisites and dependencies", ""]
        L += [f"- Prerequisites are described in {x}." for x in prereq] or ["- No separate prerequisites section in the source."]
        if ops_list:
            L.append(f"- Depends on {len(ops_list)} API operation(s), listed under “API operations referenced”.")
    L += ["", "## Current implementation guidance (source content, verbatim)", "",
          "The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels."]
    for i, p in enumerate(paths, 1):
        rng = f" lines {part[1] + 1}–{part[2]} of the body" if part else ""
        L += ["", f"### Source {i}: `{p}`{rng}", "", f"Source URL: {inv[p]['source_url']} · updatedAt: {inv[p]['updated_at'] or 'not stated'}", "",
              f"<!-- source:begin path={p} part={part[1] if part else 0}-{part[2] if part else 'end'} -->", bodies[p].rstrip("\n"), "<!-- source:end -->"]
    L += [""] + ops_section(ops_list, unresolved)
    evrows = [r for r in EVENT_INV if r["event_slug"] in ev_links]
    op_events = sorted({(e["event_slug"], o["opid"]) for o, _ in ops_list for e in EVENTS_BY_OP.get((stem(o["spec"]), o["method"].upper(), o["path"]), [])})
    if evrows or op_events:
        L += ["## Events", ""]
        if op_events:
            L += ["Events emitted by the referenced operations (`api-reference-data/endpoint_event_map.csv`):", "", "| Operation | Event slug |", "| --- | --- |"]
            L += [f"| `{op}` | `{ev}` |" for ev, op in op_events] + [""]
        if evrows:
            L += ["Event types linked from the source text (`api-reference-data/event_type_inventory.csv`):", "",
                  "| Event slug | Domain (inventory guess) | Version (inventory guess) | Event page | Emitting operations | Catalogue KU |", "| --- | --- | --- | --- | --- | --- |"]
            L += [f"| `{r['event_slug']}` | {r['domain_guess']} | {r['version_guess']} | {r['event_url']} | {r['emitting_operations']} | {EVENT_KU.get(r['event_slug'], '')} |" for r in evrows] + [""]
        L += ["Event payload fields: not documented in the available source corpus.", ""]
    L += ["## Lifecycle status", ""]
    for p in paths:
        L.append(f"- `{p}`: updatedAt {inv[p]['updated_at'] or 'not stated in the source'}.")
    L += [f"- {x}" for x in lifecycle] or []
    if not lifecycle:
        L.append("- No deprecation, removal or beta marker was found in the source or its linked operations.")
    L += ["", "## Conflicts, caveats and evidence gaps", ""]
    L += [f"- {c}" for c in caveats] or ["- None identified by the migration checks."]
    L += ["", "## Source references", "", refs_table(srcs, {p: (f"body lines {part[1] + 1}–{part[2]}" if part else "whole document") for p in paths})]
    L += ["", "## Related knowledge units", ""] + ([f"- `{r}`" for r in sorted(related)] or ["- None."])
    k = add_ku(kid, category=cat, ku_type="workflow_guide", title=ttl, text="\n".join(L) + "\n", sources=paths,
               operations=[o["opid"] for o, _ in ops_list], related=related, events=sorted(ev_links))
    for p in paths:
        cover(p, kid, f"body lines {part[1] + 1}–{part[2]}" if part else "whole document", "guide_text_verbatim", "verbatim inclusion",
              "duplicate page grouped" if is_dup else "")
    for o, _ in ops_list:
        cover(o["spec"], kid, f"{o['method'].upper()} {o['path']} ({o['opid']}) essentials", "operation_summary", "guide link slug = operationId")
    return k


for kid, cat, title, paths, why in plan_guides:
    if len(paths) == 1 and paths[0] in GUIDE_PARTS:
        parts = GUIDE_PARTS[paths[0]]
        for i, (pk, a, b) in enumerate(parts, 1):
            render_guide_ku(pk, cat, title, paths, why + "; split into parts because the page is very large", part=(pk, a, b, i, len(parts)))
    else:
        render_guide_ku(kid, cat, title, paths, why)

# ---------------- changelog KUs ----------------
for p in sorted(x for x in inv if inv[x]["source_type"] == "changelog_markdown"):
    meta, body = split_front_matter(read_text(p))
    kid = "KU-CHG-" + slugify(os.path.basename(p)[:-3])
    h1 = next((h for _, lvl, h in headings(body) if lvl == 1), inv[p]["title"])
    window = re.search(r"Changes between ([^\n]+)", body)
    mentions, unresolved, seen = [], [], set()
    for a, b, c, d in REF_LINK.findall(body):
        slug = (b or d).lower()
        if slug in seen:
            continue
        seen.add(slug)
        ops, note = slug_status(slug)
        if ops:
            mentions += [(o, note) for o in ops]
        else:
            unresolved.append((slug, sorted(SLUG_TEXTS.get(slug, {norm_space(a or c)})), note))
    lif_sections = [h for _, lvl, h in headings(body) if re.search(r"(?i)deprecat|remov|decommission|breaking", h)]
    srcs = [src_meta(p, "changelog_post")]
    related = {OP_API_KU[id(o)] for o, _ in mentions} | {"KU-LIFE-api-endpoints-removed", "KU-LIFE-marketplace-endpoint-removal"}
    m = {"ku_id": kid, "title": f"Changelog: {h1}", "category": "changelog_history", "ku_type": "changelog_history", "lifecycle": "historical",
         "sources": srcs, "operations": sorted({o["opid"] for o, _ in mentions}), "related_kus": sorted(related),
         "title_date": h1, "coverage_window": window.group(1).strip() if window else ""}
    L = [front(m), f"# Changelog: {h1}", "", f"**KU ID:** `{kid}` · **Category:** Changelog history · **Type:** historical record", "",
         f"> **HISTORICAL RECORD.** This post records changes published by Pismo on **{h1}** "
         f"({'changes between ' + window.group(1).strip() if window else 'coverage window not stated'}). It describes what changed at that time. "
         "It is not, by itself, a description of current behaviour: check the current API-reference and guide KUs, and the removed-endpoints register, before relying on any statement here.",
         "", "## Purpose and scope", "",
         "Dated record of platform changes. The title date is the publication date of record (the RSS `pubDate` is not used). The post has no `updatedAt`.", ""]
    if lif_sections:
        L += ["Sections of this post about deprecations, removals or decommissioning: " + "; ".join(f"\"{h}\"" for h in lif_sections) + ".", ""]
    L += ["## Topics covered", "", "; ".join(h for _, lvl, h in headings(body) if lvl in (2, 3)) or "no headings", ""]
    L += ["## Change record (source content, verbatim)", "", f"Source URL: {inv[p]['source_url']}", "",
          f"<!-- source:begin path={p} part=0-end -->", body.rstrip("\n"), "<!-- source:end -->", ""]
    if mentions or unresolved:
        L += ["## Current status of operations mentioned in this post", "",
              "Checked against the current OpenAPI specifications (snapshot in the corpus). Presence in the specifications means the operation is documented today; it does not confirm that a change described above is still in effect.", ""]
        if mentions:
            L += ["| Operation | Current specification | Deprecated in spec | API-reference KU |", "| --- | --- | --- | --- |"]
            L += [f"| `{o['method'].upper()} {o['path']}` (`{o['opid']}`) | `{o['spec']}` | {'**yes**' if o['op'].get('deprecated') else 'no'} | {OP_API_KU[id(o)]} |" for o, _ in mentions]
        if unresolved:
            L += ["", "| Link slug | Link text(s) | Status |", "| --- | --- | --- |"]
            L += [f"| `{s}` | {cell('; '.join(t))} | {cell(n)} |" for s, t, n in unresolved]
        L.append("")
    L += ["## Source references", "", refs_table(srcs), "", "## Related knowledge units", ""] + [f"- `{r}`" for r in sorted(related)]
    add_ku(kid, category="changelog_history", ku_type="changelog_history", title=f"Changelog: {h1}", text="\n".join(L) + "\n", sources=[p],
           operations=[o["opid"] for o, _ in mentions], related=related)
    cover(p, kid, "whole document", "changelog_text_verbatim", "verbatim inclusion", "historical")

# ---------------- API reference KUs ----------------
GUIDES_BY_OP = defaultdict(set)
for k in list(KUS.values()):
    if k["ku_type"] == "workflow_guide":
        for opid in k["operations"]:
            GUIDES_BY_OP[opid.lower()].add(k["id"])
REMOVED_FULL = set()
for r in REMOVED_ROWS:
    for m_ in re.finditer(r"\b(GET|POST|PUT|PATCH|DELETE)\s+(/?[^\s<]+)", joined_paths(r["urls_raw"])):
        REMOVED_FULL.add((m_.group(1), re.sub(r"\{[^}]*\}|:[A-Za-z_]+", "{}", "/" + m_.group(2).lstrip("/")).rstrip("/")))


def api_lifecycle_notes(o):
    notes = []
    sp = SPECS[o["spec"]]
    for bp in sp.base_paths or [""]:
        full = re.sub(r"\{[^}]*\}", "{}", bp + o["path"]).rstrip("/")
        if (o["method"].upper(), full) in REMOVED_FULL:
            notes.append(f"`{o['method'].upper()} {bp + o['path']}` also appears in the removed-endpoints list (`{REMOVED_PATH}`). "
                         "The current specification still contains it: conflicting sources (see ISSUES_AND_GAPS.md).")
    return notes


for (sp_path, tag), ops in API_GROUPS.items():
    sp = SPECS[sp_path]
    base = f"KU-API-{slugify(stem(sp_path), 50)}--{slugify(tag, 40)}"
    rendered = []
    for o in ops:
        ctx_extra = {"events": EVENTS_BY_OP.get((stem(sp_path), o["method"].upper(), o["path"]), []),
                     "catalogue": CATALOG.get((stem(sp_path), o["method"].upper(), o["path"])),
                     "guides": sorted(GUIDES_BY_OP.get(o["opid"].lower(), [])), "lifecycle": api_lifecycle_notes(o)}
        md, named, facts = render_operation(sp, o["path"], o["method"], o["op"], o["item"], ctx_extra)
        rendered.append((o, md, named, facts))
    total = sum(len(x[1].encode()) for x in rendered)
    nparts = max(1, -(-total // API_SPLIT_BYTES))
    per = -(-len(rendered) // nparts)
    groups = [rendered[i:i + per] for i in range(0, len(rendered), per)]
    for gi, grp in enumerate(groups, 1):
        kid = base if len(groups) == 1 else f"{base}-part-{gi:02d}"
        for o, *_ in grp:
            OP_API_KU[id(o)] = kid
    for gi, grp in enumerate(groups, 1):
        kid = base if len(groups) == 1 else f"{base}-part-{gi:02d}"
        names = [n for _, _, nm, _ in grp for n in nm]
        schemas_md, schema_list = render_named_schemas(sp, names, f"{sp_path} schemas")
        title = f"API reference: {sp.title} — {tag}" + (f" (part {gi} of {len(groups)})" if len(groups) > 1 else "")
        srcs = [src_meta(sp_path, "openapi_specification")]
        csv_srcs = ["api-reference-data/operations_catalog.csv", "api-reference-data/request_response_examples.csv"]
        if any(EVENTS_BY_OP.get((stem(sp_path), o["method"].upper(), o["path"])) for o, *_ in grp):
            csv_srcs.append("api-reference-data/endpoint_event_map.csv")
        srcs += [src_meta(c, "reference_table") for c in csv_srcs]
        related = set()
        for o, *_ in grp:
            related |= GUIDES_BY_OP.get(o["opid"].lower(), set())
            related |= {EVENT_KU[e["event_slug"]] for e in EVENTS_BY_OP.get((stem(sp_path), o["method"].upper(), o["path"]), []) if e["event_slug"] in EVENT_KU}
        related |= {CODE_KU[c] for x in grp for _, c, _ in x[3]["codes"] if c in CODE_KU}
        sec_used = sorted({s for *_, f in grp for s in (f["security"] or []) for s in s.split(", ")})
        m = {"ku_id": kid, "title": title, "category": "api_reference", "ku_type": "api_reference", "lifecycle": "current",
             "sources": srcs, "operations": [o["opid"] for o, *_ in grp], "related_kus": sorted(related),
             "specification_version": str(sp.version)}
        L = [front(m), f"# {title}", "", f"**KU ID:** `{kid}` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification", "",
             "## Purpose and scope", "",
             f"Contracts of {len(grp)} operation(s) tagged `{tag}` in `{sp_path}` (“{sp.title}”, version `{sp.version}`), generated from the OpenAPI document. "
             "Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; "
             "examples are shown only where the specification contains a concrete example value.", ""]
        if sp.tag_desc.get(tag):
            L += [f"Tag description (from the specification):", "", quote_block(sp.tag_desc[tag]), ""]
        L += ["## Operations in this unit", "", "| Method and path | operationId | Summary | Deprecated |", "| --- | --- | --- | --- |"]
        L += [f"| `{o['method'].upper()} {o['path']}` | `{o['opid']}` | {cell(o['summary'])} | {'**yes**' if o['op'].get('deprecated') else 'no'} |" for o, *_ in grp]
        if sec_used:
            L += ["", "## Authentication", ""]
            for s in sec_used:
                sch = sp.schemes.get(s)
                L.append(f"- `{s}`: " + (cell(jdump({k: v for k, v in sch.items() if k != 'description'})) + (f" — {cell(sch.get('description'))}" if sch.get("description") else "") if isinstance(sch, dict) else "scheme not defined in this specification"))
        L += ["", "## Operation contracts", ""]
        for o, md, named, facts in grp:
            L += [md, ""]
        L += ["## Schemas referenced", "", "Each named schema used by the operations above is listed once, with nested named schemas.", "", schemas_md]
        lifecycle = [n for o, *_ in grp for n in api_lifecycle_notes(o)]
        dep = [o for o, *_ in grp if o["op"].get("deprecated")]
        L += ["## Lifecycle status", ""]
        L += [f"- `{o['method'].upper()} {o['path']}` (`{o['opid']}`) is marked `deprecated: true` in the specification." for o in dep]
        L += [f"- {n}" for n in lifecycle]
        if not dep and not lifecycle:
            L.append("- No operation in this unit is marked deprecated in the specification.")
        L += ["", "## Conflicts, caveats and evidence gaps", "",
              "- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.",
              "- Event payload fields are not documented in the corpus (event pages are not collected)."]
        unres = [u for u in sp.unresolved if any(u[1].startswith(f"{sp_path} {o['method'].upper()} {o['path']}") for o, *_ in grp)]
        if unres:
            L += [f"- Unresolved `$ref` pointer `{u[0]}` in {u[1]}." for u in sorted(set(unres))]
        L += ["", "## Source references", "", refs_table(srcs, {sp_path: f"tag `{tag}`: " + ", ".join(f"{o['method'].upper()} {o['path']}" for o, *_ in grp)}),
              "", "## Related knowledge units", ""] + ([f"- `{r}`" for r in sorted(related)] or ["- None."])
        add_ku(kid, category="api_reference", ku_type="api_reference", title=title, text="\n".join(L) + "\n", sources=[s["path"] for s in srcs],
               operations=[o["opid"] for o, *_ in grp], related=related, schemas=schema_list)
        for o, *_ in grp:
            cover(sp_path, kid, f"{o['method'].upper()} {o['path']} ({o['opid']})", "operation_contract", "generated from OpenAPI")
            if CATALOG.get((stem(sp_path), o["method"].upper(), o["path"])):
                cover("api-reference-data/operations_catalog.csv", kid, f"row {stem(sp_path)} {o['method'].upper()} {o['path']}", "csv_row", "spec_file+method+path key")
            for e in EVENTS_BY_OP.get((stem(sp_path), o["method"].upper(), o["path"]), []):
                cover("api-reference-data/endpoint_event_map.csv", kid, f"row {o['opid']} -> {e['event_slug']}", "csv_row", "spec_file+method+path key")
        cover("api-reference-data/request_response_examples.csv", kid, f"rows for {stem(sp_path)} tag {tag}", "csv_rows_cross_check",
              "examples rendered from the YAML; CSV rows used as a cross-check")
    for u in sp.unresolved:
        LOG["unresolved_refs"].append(u)
    for u in sp.kind_mismatch:
        LOG["kind_mismatch_refs"].append(u)

# re-point guide KU related links and operation tables to final API part ids: re-render guides (cheap) so OP_API_KU part ids are used
guide_ids = [k for k, v in KUS.items() if v["ku_type"] == "workflow_guide"]
for k in guide_ids:
    del KUS[k]
COVER[:] = [c for c in COVER if c["content_type"] not in ("guide_text_verbatim", "operation_summary")]
for kid, cat, title, paths, why in plan_guides:
    if len(paths) == 1 and paths[0] in GUIDE_PARTS:
        parts = GUIDE_PARTS[paths[0]]
        for i, (pk, a, b) in enumerate(parts, 1):
            render_guide_ku(pk, cat, title, paths, why + "; split into parts because the page is very large", part=(pk, a, b, i, len(parts)))
    else:
        render_guide_ku(kid, cat, title, paths, why)
# changelog KU related links also used base API ids: rebuild their related sets textually
for k in [x for x in KUS.values() if x["ku_type"] == "changelog_history"]:
    pass  # changelog KUs reference API KUs via OP_API_KU at render time above; parts are re-resolved below

# ---------------- event catalogue KUs ----------------
by_ku = defaultdict(list)
for r in EVENT_INV:
    by_ku[EVENT_KU[r["event_slug"]]].append(r)
GUIDES_BY_EVENT = defaultdict(set)
for k in KUS.values():
    for e in k.get("events", []):
        GUIDES_BY_EVENT[e].add(k["id"])
EMIT = defaultdict(list)
for r in read_csv_rel("api-reference-data/endpoint_event_map.csv"):
    EMIT[r["event_slug"]].append(r)
for kid, rows in sorted(by_ku.items()):
    doms = sorted({r["domain_guess"] for r in rows})
    title = "Event catalogue: " + (", ".join(doms) if len(doms) <= 3 else f"other event domains ({', '.join(doms)})")
    srcs = [src_meta("api-reference-data/event_type_inventory.csv", "reference_table"), src_meta("api-reference-data/endpoint_event_map.csv", "reference_table")]
    related = set()
    L = ["## Event types", "", "| Event slug | Domain (guess) | Version (guess) | Event page | Emitting operations (count in inventory) | Specification files |", "| --- | --- | --- | --- | --- | --- |"]
    for r in sorted(rows, key=lambda x: x["event_slug"]):
        L.append(f"| `{r['event_slug']}` | {r['domain_guess']} | {r['version_guess']} | {r['event_url']} | {r['emitting_operations']} | {cell(r['spec_files'])} |")
    L += ["", "## Operations that emit these events", "", "From `api-reference-data/endpoint_event_map.csv`.", "", "| Event slug | Method and path | operationId | Specification | API-reference KU |", "| --- | --- | --- | --- | --- |"]
    for r in sorted(rows, key=lambda x: x["event_slug"]):
        for e in EMIT.get(r["event_slug"], []):
            o = next((o for o in OPS if stem(o["spec"]) == e["spec_file"] and o["method"].upper() == e["method"].upper() and o["path"] == e["path"]), None)
            akid = OP_API_KU[id(o)] if o else "operation not found in specifications"
            if o:
                related.add(akid)
            L.append(f"| `{e['event_slug']}` | `{e['method']} {e['path']}` | `{e['operation_id']}` | `{e['spec_file']}` | {akid} |")
        related |= GUIDES_BY_EVENT.get(r["event_slug"], set())
    guide_lines = []
    for r in sorted(rows, key=lambda x: x["event_slug"]):
        g = sorted(GUIDES_BY_EVENT.get(r["event_slug"], set()))
        if g:
            guide_lines.append(f"- `{r['event_slug']}`: " + ", ".join(f"`{x}`" for x in g))
    m = {"ku_id": kid, "title": title, "category": "events_and_webhooks", "ku_type": "event_catalogue", "lifecycle": "current",
         "sources": srcs, "operations": sorted({e["operation_id"] for r in rows for e in EMIT.get(r["event_slug"], [])}),
         "related_kus": sorted(related), "events": sorted(r["event_slug"] for r in rows)}
    H = [front(m), f"# {title}", "", f"**KU ID:** `{kid}` · **Category:** Events and webhooks · **Type:** event catalogue (from reference tables)", "",
         "## Purpose and scope", "",
         f"Catalogue of {len(rows)} event type(s) whose inventory domain is {', '.join(doms)}, with the operations that emit them. "
         "The domain and version columns are guesses recorded in the inventory table itself (`domain_guess`, `version_guess`), not Pismo classifications.", "",
         "**Payload fields, delivery guarantees and ordering for these events are not documented in the available source corpus**: the event pages under `/events/` were not collected (robots.txt disallows them). "
         "For delivery mechanics see the event-delivery guide KUs.", ""]
    H += L + ["", "## Guides that link to these events", ""] + (guide_lines or ["- No guide in the corpus links to these event pages."])
    H += ["", "## Source references", "", refs_table(srcs, {"api-reference-data/event_type_inventory.csv": "rows: " + ", ".join(sorted(r["event_slug"] for r in rows)),
                                                         "api-reference-data/endpoint_event_map.csv": "rows for these event slugs"}),
          "", "## Related knowledge units", ""] + ([f"- `{x}`" for x in sorted(related)] or ["- None."])
    add_ku(kid, category="events_and_webhooks", ku_type="event_catalogue", title=title, text="\n".join(H) + "\n",
           sources=[s["path"] for s in srcs], related=related, events=sorted(r["event_slug"] for r in rows))
    for r in rows:
        cover("api-reference-data/event_type_inventory.csv", kid, f"row {r['event_slug']}", "csv_row", "event_slug key")
        for e in EMIT.get(r["event_slug"], []):
            cover("api-reference-data/endpoint_event_map.csv", kid, f"row {e['operation_id']} -> {e['event_slug']}", "csv_row", "event_slug key")

# ---------------- error catalogue KUs ----------------
CHANGELOG_TEXT = {p: split_front_matter(read_text(p))[1] for p in inv if inv[p]["source_type"] == "changelog_markdown"}
OPS_BY_MP = defaultdict(list)
for o in OPS:
    OPS_BY_MP[(o["method"].upper(), o["path"])].append(o)
    for bp in SPECS[o["spec"]].base_paths:
        OPS_BY_MP[(o["method"].upper(), bp + o["path"])].append(o)
by_err = defaultdict(list)
for r in ERRORS:
    by_err[CODE_KU[r["code"]]].append(r)
for kid, rows in sorted(by_err.items()):
    prefs = sorted({prefix(r["code"]) for r in rows})
    title = "Error codes: " + (", ".join(prefs) if len(prefs) <= 4 else f"{prefs[0]} to {prefs[-1]} ({len(prefs)} prefixes)")
    srcs = [src_meta("api-reference-data/error_code_index.csv", "reference_table")]
    related = set()
    L = ["| Code | HTTP status | Message | Specification files | Operation count | Operations (sample) |", "| --- | --- | --- | --- | --- | --- |"]
    for r in sorted(rows, key=lambda x: x["code"]):
        samp = [s.strip() for s in r["operations_sample"].split(";") if s.strip()]
        for s in samp:   # samples are "METHOD path" (path as in the spec, or with the server base path)
            mm = re.match(r"(GET|POST|PUT|PATCH|DELETE|HEAD|OPTIONS)\s+(\S+)", s)
            for o in (OPS_BY_MP.get((mm.group(1), mm.group(2)), []) if mm else OPS_BY_ID.get(s.lower(), [])):
                related.add(OP_API_KU[id(o)])
        L.append(f"| `{r['code']}` | {r['http_status'] or 'not stated'} | {cell(r['message'])} | {cell(r['spec_files'])} | {r['operation_count']} | {cell(r['operations_sample'])} |")
    m = {"ku_id": kid, "title": title, "category": "errors_and_troubleshooting", "ku_type": "error_catalogue", "lifecycle": "current",
         "sources": srcs, "related_kus": sorted(related), "error_codes": sorted(r["code"] for r in rows)}
    H = [front(m), f"# {title}", "", f"**KU ID:** `{kid}` · **Category:** Errors and troubleshooting · **Type:** error-code catalogue (from reference table)", "",
         "## Purpose and scope", "",
         f"{len(rows)} error code(s) with prefix(es) {', '.join(prefs)} from `api-reference-data/error_code_index.csv`, with the HTTP status, message and the operations "
         "whose response examples contain the code. The `operations_sample` column is a sample, not a complete list: the complete set of codes per operation is in the API-reference KUs "
         "(section “Error codes shown in this operation's response examples”). Conditions under which a code is returned are documented only where the message or the operation description states them.", "",
         "## Error codes", ""] + L
    in_chg = []
    for r in sorted(rows, key=lambda x: x["code"]):
        posts = [p for p, txt in CHANGELOG_TEXT.items() if re.search(r"(?<![A-Z0-9])" + re.escape(r["code"]) + r"(?![0-9])", txt)]
        if posts:
            in_chg.append(f"`{r['code']}`: " + ", ".join(f"`KU-CHG-{slugify(os.path.basename(p)[:-3])}`" for p in posts))
            related.update(f"KU-CHG-{slugify(os.path.basename(p)[:-3])}" for p in posts)
    H += ["", "## Lifecycle status", ""]
    H += (["Codes in this unit that are mentioned in changelog posts (check the post: it may record that the code was added, changed or removed from some endpoints):", ""]
          + [f"- {x}" for x in in_chg]) if in_chg else ["- No code in this unit is mentioned in a changelog post."]
    H += ["", "## Conflicts, caveats and evidence gaps", "",
          "- Codes and messages come from response examples in the OpenAPI specifications; the conditions that trigger a code are documented only where the message or the operation description states them.",
          "- The source table recognises only codes made of letters followed by digits; codes with mixed prefixes (for example `WP2P0000`) are not in the table but appear in the API-reference KUs.",
          "", "## Source references", "", refs_table(srcs, {"api-reference-data/error_code_index.csv": "rows with code prefix " + ", ".join(prefs)}),
          "", "## Related knowledge units", ""] + ([f"- `{x}`" for x in sorted(related)] or ["- None."])
    add_ku(kid, category="errors_and_troubleshooting", ku_type="error_catalogue", title=title, text="\n".join(H) + "\n",
           sources=["api-reference-data/error_code_index.csv"], related=related, codes=sorted(r["code"] for r in rows))
    for r in rows:
        cover("api-reference-data/error_code_index.csv", kid, f"row {r['code']}", "csv_row", "code key")

# ---------------- curated lifecycle KU: marketplace endpoint removal ----------------
MKT = "KU-LIFE-marketplace-endpoint-removal"
mrows = [r for r in REMOVED_ROWS if "marketplace" in (r["api"] + r["section"]).lower()]
ch_lines = []
for p in sorted(x for x in inv if inv[x]["source_type"] == "changelog_markdown"):
    lines = split_front_matter(read_text(p))[1].split("\n")
    for i, l in enumerate(lines):
        if re.search(r"(?i)decommissioned", l) and re.search(r"(?i)api-endpoints-removed", l):
            items = []
            for l2 in lines[i + 1:]:
                if re.match(r"^\s*\*\s+", l2):
                    items.append(l2.strip()[2:].strip())
                elif l2.strip() and items:
                    break
            if any("marketplace" in x.lower() for x in items):
                ch_lines.append((p, norm_space(l), items))
mkt_slugs = ["postmarketplacesv2", "postlinkmerchanttomarketplacev1", "getmerchantsbymarketplaceidv2", "putupdatemarketplacev1"]
uses = []
for p in sorted(inv):
    if not p.endswith(".md"):
        continue
    full = read_text(p).split("\n")
    for i, l in enumerate(full, 1):
        for a, b, c, d in REF_LINK.findall(l):
            if (b or d).lower() in mkt_slugs:
                uses.append((p, i, norm_space(a or c), (b or d).lower()))
cur_ops = [o for o in OPS if o["spec"].startswith("api-specs/Seller_management_-_") and "marketplace" in o["path"].lower()]
srcs = [src_meta(REMOVED_PATH, "removal_register")] + [src_meta(p, "changelog_post") for p in sorted({x[0] for x in ch_lines})] + \
       [src_meta(p, "guide_reference") for p in sorted({u[0] for u in uses if u[0] != REMOVED_PATH})] + \
       [src_meta(p, "openapi_specification") for p in sorted({o["spec"] for o in cur_ops})]
related = {"KU-LIFE-api-endpoints-removed"} | {GUIDE_KU[u[0]] for u in uses if u[0] in GUIDE_KU} | {"KU-CHG-" + slugify(os.path.basename(p)[:-3]) for p, _, _ in ch_lines} | {OP_API_KU[id(o)] for o in cur_ops}
m = {"ku_id": MKT, "title": "Marketplace endpoints removed on 10/6/26 and guides that still reference them", "category": "api_lifecycle",
     "ku_type": "lifecycle_reference", "lifecycle": "lifecycle_reference", "sources": srcs, "operations": sorted({o["opid"] for o in cur_ops}),
     "related_kus": sorted(related)}
L = [front(m), f"# {m['title']}", "", f"**KU ID:** `{MKT}` · **Category:** API lifecycle · **Type:** lifecycle reference (assembled from quoted evidence)", "",
     "## Purpose and scope", "",
     "Answers: which marketplace endpoints were removed, when, which guides still instruct their use, and what the corpus says about replacements. "
     "Every statement below is a quotation or a structured extract of the cited source; nothing is inferred beyond what is labelled as inference.", "",
     "## Removal evidence", "", f"### Removed-endpoints register (`{REMOVED_PATH}`)", "",
     "| API | API section | Endpoint names (as published) | Endpoint URLs (as published; line breaks inside the source cell kept as ` ⏎ `) | Date removed (raw) |",
     "| --- | --- | --- | --- | --- |"]
for r in mrows:
    L.append(f"| {cell(r['api'])} | {cell(r['section'])} | {cell('; '.join(r['names']))} | {raw_cell(r['urls_raw'])} | `{r['date_raw']}` |")
L += ["", "Date format: the register mixes formats (`10/6/26`, `7/24/2026`, `9/2025`). Rows such as `7/24/2026` and `6/30/2025` show month/day order, so `10/6/26` is read as 6 October 2026. "
      "This reading is a migration inference from the register itself; the raw value is kept above.", "", "### Changelog record", ""]
for p, line, items in ch_lines:
    post_title = next((h for _, lvl, h in headings(split_front_matter(read_text(p))[1]) if lvl == 1), inv[p]["title"])
    L += [f"`{p}` (post dated “{post_title}”):", "", quote_block(line), ""] + [f"> - {x}" for x in items] + [""]
L += ["Count conflict: the register lists the endpoint names `" + "`, `".join(n for r in mrows if r['date_raw'] == '10/6/26' for n in r['names']) +
      "` for the 10/6/26 row, while the changelog lists " + str(sum(len(i) for _, _, i in ch_lines)) + " names (it separates “Create marketplace V1” and “Create marketplace V2”). Both are kept; see ISSUES_AND_GAPS.md.", "",
      "## Guides and pages that still link to these endpoints", "",
      "These links are to operation slugs that are not in the current OpenAPI specifications. The match between a slug and a removed endpoint is by the link text equal to the published endpoint name (inference, not an identifier match).", "",
      "| Source file | Line | Link text | Slug | Knowledge unit |", "| --- | --- | --- | --- | --- |"]
for p, i, t, s in uses:
    L.append(f"| `{p}` | {i} | {cell(t)} | `{s}` | {', '.join(guide_ku_ids(p)) if p in GUIDE_KU else 'KU-CHG-' + slugify(os.path.basename(p)[:-3])} |")
L += ["", "**Implementation guidance:** do not use these links as current instructions. The guides above are migrated verbatim and still describe the removed calls; their KUs carry a lifecycle warning.", "",
      "## Current marketplace operations in the specifications", "",
      "Operations whose path contains `marketplace` in the current Seller management specifications. **No source in the corpus states that any of them replaces a removed endpoint.** Similar names are not evidence of replacement.", "",
      "| Method and path | operationId | Summary | Specification | Deprecated | API-reference KU |", "| --- | --- | --- | --- | --- | --- |"]
L += [f"| `{o['method'].upper()} {o['path']}` | `{o['opid']}` | {cell(o['summary'])} | `{o['spec']}` | {'**yes**' if o['op'].get('deprecated') else 'no'} | {OP_API_KU[id(o)]} |" for o in cur_ops]
L += ["", "## Successor or replacement", "", "Not documented in the available source corpus. The corpus contains no statement that a removed marketplace endpoint is replaced by another endpoint.", "",
      "## Source references", "", refs_table(srcs), "", "## Related knowledge units", ""] + [f"- `{r}`" for r in sorted(related)]
add_ku(MKT, category="api_lifecycle", ku_type="lifecycle_reference", title=m["title"], text="\n".join(L) + "\n", sources=[s["path"] for s in srcs],
       operations=[o["opid"] for o in cur_ops], related=related)
cover(REMOVED_PATH, MKT, "Marketplace rows of the removal table", "structured_extract", "curated: marketplace rows")
for p, _, _ in ch_lines:
    cover(p, MKT, "decommissioned-endpoint list", "quoted_extract", "curated: 'decommissioned' paragraph linking api-endpoints-removed")
for p in sorted({u[0] for u in uses}):
    cover(p, MKT, "lines linking removed marketplace slugs", "reference_list", "curated: link slug occurrence")

# structured register appended to the api-endpoints-removed KU
rk = KUS["KU-LIFE-api-endpoints-removed"]
reg = ["", "## Structured removal register (migration extract)", "",
       "Each row of the published table, extracted from the MDX source. Cell text is shown with line breaks inside a cell replaced by ` ⏎ `; no path was repaired. "
       "“In current specs?” checks each `METHOD path` in the URL cell against current operations (server base path + path, placeholders normalised).", "",
       "| # | API | API section | Endpoint names | Endpoint URLs (raw) | Date removed (raw) | In current specs? |", "| --- | --- | --- | --- | --- | --- | --- |"]
cur_full = {}
for o in OPS:
    for bp in SPECS[o["spec"]].base_paths or [""]:
        cur_full[(o["method"].upper(), re.sub(r"\{[^}]*\}", "{}", bp + o["path"]).rstrip("/"))] = o
for i, r in enumerate(REMOVED_ROWS, 1):
    found = []
    for m_ in re.finditer(r"\b(GET|POST|PUT|PATCH|DELETE)\s+(/?[^\s<]+)", joined_paths(r["urls_raw"])):
        k = (m_.group(1), re.sub(r"\{[^}]*\}|:[A-Za-z_]+", "{}", "/" + m_.group(2).lstrip("/")).rstrip("/"))
        if k in cur_full:
            found.append(f"yes: `{cur_full[k]['opid']}` in `{cur_full[k]['spec']}`")
    reg.append(f"| {i} | {cell(r['api'])} | {cell(r['section'])} | {cell('; '.join(r['names']))} | {raw_cell(r['urls_raw'])} | `{r['date_raw'] or '(blank)'}` | "
               f"{'; '.join(found) if found else 'no match'} |")
txt = rk["text"]
anchor = "\n## API operations referenced" if "\n## API operations referenced" in txt else "\n## Lifecycle status"
rk["text"] = txt.replace(anchor, "\n".join(reg) + "\n" + anchor, 1)
rk["related"].add(MKT)
cover(REMOVED_PATH, "KU-LIFE-api-endpoints-removed", "removal table rows (structured extract)", "structured_extract", "MDX table parse")

# ---------------- related-link resolution to final ids, writing ----------------
api_base_to_parts = defaultdict(list)
for k in KUS:
    if k.startswith("KU-API-"):
        api_base_to_parts[re.sub(r"-part-\d+$", "", k)].append(k)
for k in KUS.values():
    fixed = set()
    for r in k["related"]:
        fixed |= set(api_base_to_parts.get(r, [r])) if r not in KUS else {r}
    fixed.discard(k["id"])
    k["related"] = fixed
    for r in list(fixed):
        if r not in KUS:
            LOG["warnings"].append(f"{k['id']}: related {r} does not exist")

out_dir = KU_ROOT
marker = os.path.join(out_dir, ".generated_by_build_kus")
if os.path.exists(out_dir) and not os.path.exists(marker):
    raise SystemExit(f"{out_dir} exists and was not generated by this tool; refusing to overwrite")
if os.path.exists(out_dir) and not ONLY:
    shutil.rmtree(out_dir)
os.makedirs(out_dir, exist_ok=True)
open(marker, "w").write("generated by tools/build_kus.py; safe to regenerate\n")
written = []
for k in KUS.values():
    if ONLY and k["id"] not in ONLY:
        continue
    text = k["text"]
    # rewrite the related_kus front-matter list and the Related section with final ids
    fm_end = text.index("\n---\n", 4) + 5
    meta = yaml.safe_load(text[4:fm_end - 5])
    meta["related_kus"] = sorted(k["related"])
    body = text[fm_end:]
    body = re.sub(r"## Related knowledge units\n\n(?:- .*\n?)*", "## Related knowledge units\n\n" + ("\n".join(f"- `{r}` — {KUS[r]['title']}" for r in sorted(k["related"]) if r in KUS) or "- None.") + "\n", body)
    for base, parts in api_base_to_parts.items():
        if len(parts) > 1 or parts[0] != base:
            body = body.replace(f"| {base} |", "| " + ", ".join(parts) + " |")
    final = front(meta) + body
    path = os.path.join(out_dir, k["category"], f"{k['id']}.md")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(final)
    k["path"] = os.path.relpath(path, MIG).replace(os.sep, "/")
    written.append(k["id"])

# ---------------- manifest, coverage, index ----------------
by_src = defaultdict(set)
for c in COVER:
    by_src[c["source_path"]].add(c["ku_id"])
man = []
for p, r in sorted(inv.items()):
    kus = sorted(by_src.get(p, set()))
    man.append({"source_path": p, "source_sha256": r["sha256"], "source_type": r["source_type"],
                "migration_status": "migrated" if kus else "not_migrated", "ku_ids": ";".join(kus), "validation_status": "pending",
                "issues": "", "exclusion_reason": "" if kus else "NO MAPPING (defect)"})
write_csv(os.path.join(MIG, "MIGRATION_MANIFEST.csv"), list(man[0]), man)
write_csv(os.path.join(MIG, "SOURCE_COVERAGE.csv"), list(COVER[0]), COVER)
index = {k["id"]: {"category": k["category"], "ku_type": k["ku_type"], "title": k["title"], "path": k.get("path"),
                   "sources": k["sources"], "operations": k["operations"], "related": sorted(k["related"]),
                   "events": k.get("events", []), "codes": k.get("codes", []), "schemas": k.get("schemas", [])} for k in KUS.values()}
dump_json(os.path.join(WORK, "ku_index.json"), index)
LOG.update(kus_planned=len(KUS), kus_written=len(written), by_category=dict(Counter(k["category"] for k in KUS.values())),
           by_type=dict(Counter(k["ku_type"] for k in KUS.values())), sources_unmapped=[m_["source_path"] for m_ in man if not m_["ku_ids"]],
           unresolved_refs=sorted(set(map(tuple, LOG["unresolved_refs"]))), kind_mismatch_refs=sorted(set(map(tuple, LOG["kind_mismatch_refs"]))),
           split_guides={p: [x[0] for x in v] for p, v in GUIDE_PARTS.items()}, removal_rows=len(REMOVED_ROWS))
dump_json(os.path.join(WORK, "build_log.json"), LOG)
sizes = sorted(((len(k["text"].encode()), k["id"]) for k in KUS.values()), reverse=True)
print(json.dumps({k: LOG[k] for k in ("kus_planned", "kus_written", "by_category", "by_type", "sources_unmapped", "removal_rows")}, indent=1))
print("unresolved $refs:", len(LOG["unresolved_refs"]), "| kind-mismatch $refs:", len(LOG["kind_mismatch_refs"]), "| warnings:", len(LOG["warnings"]))
print("largest KUs (bytes):", sizes[:8])
print("total KU bytes:", sum(s for s, _ in sizes))
