"""Phase A2: analyse the corpus (read-only) for planning: guide metadata and links, spec operations/tags/$refs, CSV keys.

Writes work/analysis.json.
"""
import os, re, sys
from collections import Counter, defaultdict
import yaml
from common import *

files = corpus_files()
smap = load_source_map()
REF_LINK = re.compile(r"(?:https?://developers\.pismo\.io)?/?(?:pismo-docs/)?reference(?:-link)?/([A-Za-z0-9_\-]+)|\(ref:([A-Za-z0-9_\-]+)")
DOC_LINK = re.compile(r"(?:https?://developers\.pismo\.io)?/pismo-docs/docs/([A-Za-z0-9_\-]+)|\(doc:([A-Za-z0-9_\-]+)")
EVENT_LINK = re.compile(r"developers\.pismo\.io/events/docs/([A-Za-z0-9_\-]+)")
HEAD = re.compile(r"^\s{0,3}(#{1,6})\s+(.+?)\s*#*\s*$")
METHODS = ("get", "post", "put", "patch", "delete", "head", "options")

# ---------- specs ----------
specs, ops, refs_external, dup_opids = {}, [], Counter(), defaultdict(list)
for p in files:
    if source_type(p) != "openapi_yaml":
        continue
    d = yaml.safe_load(read_text(p))
    comps = d.get("components") or {}
    text = read_text(p)
    ref_targets = Counter(m.split("/")[2] if m.startswith("#/") and m.count("/") >= 3 else "EXTERNAL" for m in re.findall(r"\$ref['\"]?\s*:\s*['\"]?([^'\"\s}]+)", text))
    tags_decl = [t.get("name") for t in d.get("tags") or []]
    sp_ops = []
    for path, item in (d.get("paths") or {}).items():
        for m, op in (item or {}).items():
            if m not in METHODS or not isinstance(op, dict):
                continue
            o = {"spec": p, "method": m.upper(), "path": path, "operationId": op.get("operationId", ""), "summary": op.get("summary", ""),
                 "tags": op.get("tags") or [], "deprecated": bool(op.get("deprecated"))}
            sp_ops.append(o); ops.append(o)
            dup_opids[o["operationId"].lower()].append(f"{p}:{o['method']} {path}")
    specs[p] = {"title": (d.get("info") or {}).get("title"), "openapi": d.get("openapi"), "operations": len(sp_ops),
                "tags_declared": tags_decl, "tags_used": dict(Counter(t for o in sp_ops for t in (o["tags"] or ["(untagged)"]))),
                "component_types": {k: len(v or {}) for k, v in comps.items()}, "ref_target_types": dict(ref_targets),
                "security_schemes": list((comps.get("securitySchemes") or {}).keys()), "global_security": d.get("security"),
                "servers": [s.get("url") for s in d.get("servers") or []]}
opid_index = {k: v for k, v in dup_opids.items()}
dups = {k: v for k, v in dup_opids.items() if len(v) > 1}

# ---------- guides & changelogs ----------
slug_to_file = {}
for p in files:
    if p.endswith(".md") and (p.startswith("docs/") or p.startswith("changelog/")):
        slug_to_file.setdefault(os.path.basename(p)[:-3].lower(), []).append(p)
guides = {}
for p in files:
    t = source_type(p)
    if t not in ("guide_markdown", "changelog_markdown", "spec_repository_readme"):
        continue
    raw = read_text(p)
    meta, body = split_front_matter(raw)
    heads = [(len(m.group(1)), m.group(2)) for m in (HEAD.match(l) for l in body.splitlines()) if m]
    h1 = next((h for lvl, h in heads if lvl == 1), smap[p]["title"])
    ref_slugs = sorted({(a or b).lower() for a, b in REF_LINK.findall(body)})
    doc_slugs = sorted({(a or b).lower() for a, b in DOC_LINK.findall(body)})
    guides[p] = {"type": t, "title": smap[p]["title"], "h1": h1, "updated_at": meta.get("updatedAt", ""), "chars": len(body),
                 "headings": heads, "ref_slugs": ref_slugs,
                 "ref_resolved": [s for s in ref_slugs if s in opid_index], "ref_unresolved": [s for s in ref_slugs if s not in opid_index],
                 "doc_slugs": doc_slugs, "doc_links_resolved": sorted({f for s in doc_slugs for f in slug_to_file.get(s, [])}),
                 "doc_links_unresolved": [s for s in doc_slugs if s not in slug_to_file],
                 "event_slugs": sorted(set(EVENT_LINK.findall(body))),
                 "mdx": dict(Counter(re.findall(r"<(HTMLBlock|Callout|Table|Image|Anchor|Tabs?|Embed|Cards?|Accordion|details|summary)\b", body))),
                 "body_sha": sha_bytes(re.sub(r"\s+", " ", body).strip().encode("utf-8"))}
dup_bodies = defaultdict(list)
for p, g in guides.items():
    dup_bodies[g["body_sha"]].append(p)
title_dups = defaultdict(list)
for p, g in guides.items():
    if g["type"] == "guide_markdown":
        title_dups[g["title"].strip().lower()].append(p)

# ---------- csv ----------
csvs = {}
for p in files:
    if source_type(p) == "reference_table_csv":
        rows = read_csv_rel(p)
        csvs[p] = {"rows": len(rows), "columns": list(rows[0].keys()) if rows else []}

an = {"specs": specs, "operations": ops, "operation_count": len(ops), "duplicate_operation_ids": dups,
      "guides": guides, "identical_bodies": [v for v in dup_bodies.values() if len(v) > 1],
      "same_title_guides": {k: v for k, v in title_dups.items() if len(v) > 1}, "csvs": csvs,
      "slug_to_file_collisions": {k: v for k, v in slug_to_file.items() if len(v) > 1}}
dump_json(os.path.join(WORK, "analysis.json"), an)
g_only = {p: g for p, g in guides.items() if g["type"] == "guide_markdown"}
print("operations", len(ops), "| distinct opIds", len(opid_index), "| duplicated opIds", len(dups))
print("guide->op links: guides with links", sum(1 for g in g_only.values() if g["ref_slugs"]),
      "| distinct slugs", len({s for g in g_only.values() for s in g["ref_slugs"]}),
      "| resolved", len({s for g in g_only.values() for s in g["ref_resolved"]}),
      "| unresolved", len({s for g in g_only.values() for s in g["ref_unresolved"]}))
print("identical guide bodies:", an["identical_bodies"])
print("same-title guides:", an["same_title_guides"])
print("slug collisions:", an["slug_to_file_collisions"])
print("ref target types (all specs):", dict(sum((Counter(s["ref_target_types"]) for s in specs.values()), Counter())))
print("security schemes:", sorted({x for s in specs.values() for x in s["security_schemes"]}))
print("mdx totals:", dict(sum((Counter(g["mdx"]) for g in guides.values()), Counter())))
print("csvs:", csvs)
