"""Independent validation of the KU collection against the authoritative corpus. Read-only on the corpus and the KUs.

Does not import the renderer (spec_model) or the builder; YAML is re-read and $refs are resolved here independently.
Usage: python -B -E -s validate.py [--pilot]      (--pilot: validate only the KUs present; skip whole-corpus coverage checks)
Writes work/validation_results.json and fills validation_status in MIGRATION_MANIFEST.csv and SOURCE_COVERAGE.csv.
Exit 0 when every check passes, 1 otherwise.
"""
import argparse, csv, hashlib, json, os, re, sys
from collections import Counter, defaultdict
import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
MIG = os.path.dirname(HERE)
PROJECT = os.path.dirname(MIG)
CORPUS = os.path.join(PROJECT, "pismo_kb_release_r2", "kb_corpus")
SMAP = os.path.join(PROJECT, "pismo_kb_release_r2", "internal", "provenance", "source_map.csv")
KUDIR = os.path.join(MIG, "knowledge_units")
WORK = os.path.join(MIG, "work")
ACCEPTED_P = "7080b549e8160a2bc555ae1c0646b4d9a807414cd12dbd1943e712f5031f0e62"
csv.field_size_limit(10 ** 9)
ap = argparse.ArgumentParser(); ap.add_argument("--pilot", action="store_true"); A = ap.parse_args()

R = {"checks": {}, "failures": defaultdict(list), "counts": {}}


def fail(check, msg):
    R["failures"][check].append(msg)


def done(check, n_checked, note=""):
    R["checks"][check] = {"checked": n_checked, "failures": len(R["failures"].get(check, [])), "note": note}


def sha(b):
    return hashlib.sha256(b).hexdigest()


def rb(p):
    with open(p, "rb") as fh:
        return fh.read()


def body_of(raw):
    m = re.match(r"\A---\r?\n.*?\r?\n---\r?\n", raw, re.S)
    return raw[m.end():] if m else raw


def cell(s):
    s = "" if s is None else str(s)
    return s.replace("\\", "\\\\").replace("|", "\\|").replace("\r\n", "\n").replace("\r", "\n").replace("\n", "<br>").strip()


def rows_csv(rel):
    with open(os.path.join(CORPUS, rel), encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh))


# ---------------- 1. corpus integrity ----------------
tree = {}
for r_, _, fs in os.walk(CORPUS):
    for f in fs:
        p = os.path.join(r_, f)
        b = rb(p)
        tree[os.path.relpath(p, CORPUS).replace(os.sep, "/")] = (len(b), sha(b))
P = sha("".join(f"{k}\t{v[0]}\t{v[1]}\n" for k, v in sorted(tree.items())).encode())
if P != ACCEPTED_P:
    fail("corpus_integrity", f"corpus fingerprint {P} != accepted {ACCEPTED_P}")
inv = {r["source_path"]: r for r in csv.DictReader(open(os.path.join(MIG, "archived_source_inventory", "SOURCE_INVENTORY.csv"), encoding="utf-8", newline=""))}
for p, (n, h) in tree.items():
    if p not in inv or inv[p]["sha256"] != h or int(inv[p]["bytes"]) != n:
        fail("corpus_integrity", f"inventory mismatch {p}")
if set(inv) != set(tree):
    fail("corpus_integrity", "inventory path set differs from corpus")
done("corpus_integrity", len(tree), f"fingerprint {P}")
smap = {r["corpus_path"][len("kb_corpus/"):]: r for r in csv.DictReader(open(SMAP, encoding="utf-8", newline=""))}

# ---------------- 2. KU files, front matter, coverage ----------------
kus, ku_text = {}, {}
for r_, _, fs in os.walk(KUDIR):
    for f in fs:
        p = os.path.join(r_, f)
        rel = os.path.relpath(p, KUDIR).replace(os.sep, "/")
        if f == ".generated_by_build_kus":
            continue
        if not f.endswith(".md"):
            fail("ku_files", f"non-Markdown file in knowledge_units: {rel}")
            continue
        raw = rb(p).decode("utf-8")
        m = re.match(r"\A---\n(.*?)\n---\n", raw, re.S)
        if not m:
            fail("ku_front_matter", f"{rel}: no front matter"); continue
        meta = yaml.safe_load(m.group(1))
        kid = meta.get("ku_id")
        if kid in kus:
            fail("ku_files", f"duplicate KU id {kid}")
        if f != f"{kid}.md":
            fail("ku_files", f"{rel}: file name does not match ku_id {kid}")
        if rel.split("/")[0] != meta.get("category"):
            fail("ku_files", f"{rel}: folder does not match category {meta.get('category')}")
        kus[kid] = dict(meta, _path=rel)
        ku_text[kid] = raw
index = json.load(open(os.path.join(WORK, "ku_index.json"), encoding="utf-8"))
if not A.pilot:
    for k in index:
        if k not in kus:
            fail("ku_files", f"indexed KU missing on disk: {k}")
for k in kus:
    if k not in index:
        fail("ku_files", f"KU on disk not in index (orphan): {k}")
done("ku_files", len(kus))

# operationIds in specs (independent parse)
SPECS, OPS = {}, []
for p in tree:
    if p.startswith("api-specs/") and p.endswith(".yaml"):
        d = yaml.safe_load(rb(os.path.join(CORPUS, p)).decode("utf-8"))
        SPECS[p] = d
        for path, item in (d.get("paths") or {}).items():
            for mth in ("get", "put", "post", "delete", "patch", "head", "options", "trace"):
                op = (item or {}).get(mth) if isinstance(item, dict) else None
                if isinstance(op, dict):
                    OPS.append((p, mth.upper(), path, op, item))
OPIDS = {o[3].get("operationId", "") for o in OPS}
REQ_FM = ("ku_id", "title", "category", "ku_type", "lifecycle", "sources", "related_kus")
n = 0
for k, meta in kus.items():
    for key in REQ_FM:
        if key not in meta:
            fail("ku_front_matter", f"{k}: missing {key}")
    for s in meta.get("sources") or []:
        n += 1
        p = s.get("path")
        if p not in tree:
            fail("traceability_sources", f"{k}: source {p} not in corpus"); continue
        if s.get("sha256") != tree[p][1]:
            fail("traceability_sources", f"{k}: sha256 of {p} differs from corpus")
        if s.get("url") != smap[p]["source_url"]:
            fail("traceability_sources", f"{k}: url of {p} differs from source_map ({s.get('url')} vs {smap[p]['source_url']})")
    for r in meta.get("related_kus") or []:
        if r not in kus and (not A.pilot or r not in index):
            fail("traceability_related", f"{k}: related {r} does not exist")
    for o in meta.get("operations") or []:
        if o not in OPIDS:
            fail("traceability_operations", f"{k}: operation {o} not in any specification")
    for line in re.findall(r"Source URL: (\S+)", ku_text[k]):
        if line not in {x["source_url"] for x in smap.values()}:
            fail("traceability_sources", f"{k}: Source URL {line} not in source_map")
for c in ("ku_front_matter", "traceability_sources", "traceability_related", "traceability_operations"):
    done(c, n if c == "traceability_sources" else len(kus))

# ---------------- 3. verbatim fidelity ----------------
BLOCK = re.compile(r"<!-- source:begin path=(\S+) part=(\d+)-(\S+) -->\n(.*?)\n<!-- source:end -->", re.S)
seen_parts = defaultdict(list)
nb = 0
for k, t in ku_text.items():
    for p, a, b, content in BLOCK.findall(t):
        nb += 1
        if p not in tree:
            fail("verbatim_fidelity", f"{k}: block for unknown source {p}"); continue
        body = body_of(rb(os.path.join(CORPUS, p)).decode("utf-8"))
        lines = body.split("\n")
        a = int(a); b2 = len(lines) if b == "end" else int(b)
        expect = "\n".join(lines[a:b2]).rstrip("\n")
        if content != expect:
            i = next((i for i, (x, y) in enumerate(zip(content, expect)) if x != y), min(len(content), len(expect)))
            fail("verbatim_fidelity", f"{k}: block {p} [{a}:{b}] differs at char {i}")
        seen_parts[p].append((a, b2, k))
for p, parts in seen_parts.items():
    parts.sort()
    total = len(body_of(rb(os.path.join(CORPUS, p)).decode("utf-8")).split("\n"))
    pos = 0
    for a, b2, k in parts:
        if a != pos:
            fail("verbatim_completeness", f"{p}: gap or overlap at line {pos} (next part starts {a} in {k})")
        pos = b2
    if pos != total:
        fail("verbatim_completeness", f"{p}: parts end at line {pos} of {total}")
md_sources = [p for p in tree if p.endswith(".md")]
if not A.pilot:
    for p in md_sources:
        if p not in seen_parts:
            fail("verbatim_completeness", f"{p}: no verbatim block in any KU")
done("verbatim_fidelity", nb); done("verbatim_completeness", len(seen_parts))

# ---------------- 4. API fidelity (independent resolver) ----------------
def ptr(doc, ref):
    if not isinstance(ref, str) or not ref.startswith("#/"):
        return None
    node = doc
    for part in ref[2:].split("/"):
        part = part.replace("~1", "/").replace("~0", "~")
        if isinstance(node, dict) and part in node:
            node = node[part]
        else:
            return None
    return node


def deref(doc, node, depth=0):
    while isinstance(node, dict) and "$ref" in node and depth < 20:
        node = ptr(doc, node["$ref"]); depth += 1
    return node


def top_props(doc, sch, seen=()):
    s = deref(doc, sch)
    if not isinstance(s, dict) or id(s) in seen:
        return [], set()
    props, req = [], set(s.get("required") or [])
    for part in s.get("allOf") or []:
        p2, r2 = top_props(doc, part, seen + (id(s),))
        props += p2; req |= r2
    props += list((s.get("properties") or {}).items())
    return props, req


op_sections = {}
for k, t in ku_text.items():
    if kus[k].get("ku_type") != "api_reference":
        continue
    parts = re.split(r"(?=<!-- op: spec=)", t)
    for sec in parts[1:]:
        m = re.match(r"<!-- op: spec=(\S+) method=(\S+) path=(\S+) operationId=(\S*) -->", sec)
        sec = sec.split("\n## Schemas referenced")[0]
        key = (m.group(1), m.group(2), m.group(3))
        if key in op_sections:
            fail("api_fidelity", f"operation {key} rendered in two KUs ({op_sections[key][0]}, {k})")
        op_sections[key] = (k, sec, m.group(4))
napi = 0
for spec, mth, path, op, item in OPS:
    key = (spec, mth, path)
    if key not in op_sections:
        if not A.pilot:
            fail("api_coverage", f"operation {mth} {path} in {spec} not rendered")
        continue
    napi += 1
    k, sec, opid = op_sections[key]
    doc = SPECS[spec]
    if opid != op.get("operationId", ""):
        fail("api_fidelity", f"{k}: {mth} {path} operationId {opid} != {op.get('operationId')}")
    if f"### `{mth} {path}`" not in sec:
        fail("api_fidelity", f"{k}: heading for {mth} {path} missing")
    if op.get("operationId") and f"- **operationId:** `{op['operationId']}`" not in sec:
        fail("api_fidelity", f"{k}: operationId line missing for {mth} {path}")
    dep = "**yes**" if op.get("deprecated") else "no"
    if f"- **Deprecated in specification:** {dep}" not in sec:
        fail("api_fidelity", f"{k}: deprecated flag wrong for {mth} {path}")
    params = {}
    for src in ((item or {}).get("parameters") or [], op.get("parameters") or []):
        for prm in src:
            r = deref(doc, prm)
            if isinstance(r, dict):
                params[(r.get("name"), r.get("in"))] = r
    for (nm, where), r in params.items():
        row = f"| `{nm}` | {where} | {'yes' if r.get('required') else 'no'} |"
        if row not in sec:
            fail("api_fidelity", f"{k}: parameter row missing/wrong {row} for {mth} {path}")
    rbody = deref(doc, op.get("requestBody")) if op.get("requestBody") is not None else None
    if isinstance(rbody, dict):
        for mt, media in (rbody.get("content") or {}).items():
            s = deref(doc, (media or {}).get("schema"))
            if not isinstance(s, dict) or ((s.get("oneOf") or s.get("anyOf")) and not s.get("properties")):
                continue
            props, req = top_props(doc, (media or {}).get("schema"))
            for nm, sub in props:
                row = re.compile(r"^\| `" + re.escape(nm) + r"` \| [^\n]*? \| " + ("yes" if nm in req else "no") + r" \|", re.M)
                if not row.search(sec):
                    fail("api_fidelity", f"{k}: request field `{nm}` (required={nm in req}) missing/wrong for {mth} {path} {mt}")
                ds = deref(doc, sub)
                if isinstance(ds, dict) and "enum" in ds:
                    if ("enum: " + cell(json.dumps(ds["enum"], ensure_ascii=False, default=str))) not in sec:
                        fail("api_fidelity", f"{k}: enum of `{nm}` not rendered exactly for {mth} {path}")
    for st in (op.get("responses") or {}):
        if not re.search(r"^\| " + re.escape(str(st)) + r" \|", sec, re.M):
            fail("api_fidelity", f"{k}: response {st} missing for {mth} {path}")
done("api_fidelity", napi); done("api_coverage", len(OPS))

# examples (request_response_examples.csv)
ex_checked = ex_ref = ex_unparsable = 0
stem_to_spec = {os.path.basename(p)[:-5]: p for p in SPECS}
for r in rows_csv("api-reference-data/request_response_examples.csv"):
    key = (stem_to_spec.get(r["spec_file"]), r["method"].upper(), r["path"])
    if key not in op_sections:
        if not A.pilot:
            fail("examples", f"example row for unrendered op {key}")
        continue
    k, sec, _ = op_sections[key]
    try:
        val = json.loads(r["example_json"])
    except Exception:
        ex_unparsable += 1
        continue
    if isinstance(val, dict) and set(val) == {"$ref"}:
        ex_ref += 1
        tgt = ptr(SPECS[key[0]], val["$ref"])
        if isinstance(tgt, dict) and "value" in tgt:
            val = tgt["value"]
        else:
            if "**not rendered**" not in sec:
                fail("examples", f"{k}: unresolvable example pointer {val['$ref']} without a 'not rendered' note")
            continue
    ex_checked += 1
    rendered = json.dumps(val, indent=2, ensure_ascii=False, default=str) if isinstance(val, (dict, list)) else str(val)
    if rendered not in sec:
        fail("examples", f"{k}: example {r['example_name']} ({r['location']} {r['http_status']}) of {key[1]} {key[2]} not found verbatim")
done("examples", ex_checked, f"{ex_ref} $ref-only rows resolved by full pointer; {ex_unparsable} rows not JSON-parsable (not compared)")

# ---------------- 5. CSV rows ----------------
alltext = "\n".join(ku_text.values())
nerr = 0
for r in rows_csv("api-reference-data/error_code_index.csv"):
    row = f"| `{r['code']}` | {r['http_status'] or 'not stated'} | {cell(r['message'])} | {cell(r['spec_files'])} | {r['operation_count']} | {cell(r['operations_sample'])} |"
    hit = [k for k, t in ku_text.items() if kus[k].get("ku_type") == "error_catalogue" and row in t]
    if not A.pilot or any(kus[k].get("ku_type") == "error_catalogue" and f"`{r['code']}`" in t for k, t in ku_text.items()):
        nerr += 1
        if len(hit) != 1:
            fail("csv_error_codes", f"error code {r['code']}: row found in {len(hit)} error KUs")
done("csv_error_codes", nerr)
nev = 0
for r in rows_csv("api-reference-data/event_type_inventory.csv"):
    row = f"| `{r['event_slug']}` | {r['domain_guess']} | {r['version_guess']} | {r['event_url']} | {r['emitting_operations']} | {cell(r['spec_files'])} |"
    hit = [k for k, t in ku_text.items() if kus[k].get("ku_type") == "event_catalogue" and row in t]
    if not A.pilot or hit:
        nev += 1
        if len(hit) != 1:
            fail("csv_event_types", f"event {r['event_slug']}: row found in {len(hit)} event KUs")
done("csv_event_types", nev)
nmap = 0
for r in rows_csv("api-reference-data/endpoint_event_map.csv"):
    key = (stem_to_spec.get(r["spec_file"]), r["method"].upper(), r["path"])
    in_api = key in op_sections and f"| `{r['event_slug']}` | {r['event_url']} |" in op_sections[key][1]
    in_cat = f"| `{r['event_slug']}` | `{r['method']} {r['path']}` | `{r['operation_id']}` | `{r['spec_file']}` |" in alltext
    cat_written = any(r["event_slug"] in (index[k].get("events") or []) and index[k]["ku_type"] == "event_catalogue" for k in kus)
    if not A.pilot or (key in op_sections and cat_written):
        nmap += 1
        if not (in_api and in_cat):
            fail("csv_endpoint_event_map", f"{r['operation_id']} -> {r['event_slug']}: in API KU {in_api}, in catalogue {in_cat}")
done("csv_endpoint_event_map", nmap)
ncat = 0
for r in rows_csv("api-reference-data/operations_catalog.csv"):
    key = (stem_to_spec.get(r["spec_file"]), r["method"].upper(), r["path"])
    if key not in op_sections:
        continue
    ncat += 1
    line = (f"response codes `{r['response_codes']}`, has examples `{r['has_examples']}`, emits events `{r['emits_events']}`, deprecated `{r['deprecated']}`")
    if line not in op_sections[key][1]:
        fail("csv_operations_catalog", f"{key}: catalogue line missing or different")
    spec_dep = bool(next(o[3] for o in OPS if (o[0], o[1], o[2]) == key).get("deprecated"))
    if (r["deprecated"] == "True") != spec_dep:
        fail("source_conflict_catalog_vs_spec", f"{key}: catalogue deprecated={r['deprecated']} but spec deprecated={spec_dep}")
done("csv_operations_catalog", ncat)

# ---------------- 6. lifecycle and curated content ----------------
REMOVED_SLUGS = ["postmarketplacesv2", "postlinkmerchanttomarketplacev1", "getmerchantsbymarketplaceidv2", "putupdatemarketplacev1"]
nl = 0
for k, t in ku_text.items():
    typ = kus[k].get("ku_type")
    if typ == "changelog_history":
        nl += 1
        if "**HISTORICAL RECORD.**" not in t or kus[k].get("lifecycle") != "historical":
            fail("lifecycle", f"{k}: changelog KU without historical banner/status")
    if typ == "workflow_guide" and any(s in t.lower() for s in REMOVED_SLUGS):
        nl += 1
        life = t.split("## Lifecycle status", 1)[1].split("\n## ", 1)[0] if "## Lifecycle status" in t else ""
        for s in REMOVED_SLUGS:
            if s in t.split("<!-- source:end -->")[0].lower() and s not in life:
                fail("lifecycle", f"{k}: links removed slug {s} without a lifecycle warning")
mk = ku_text.get("KU-LIFE-marketplace-endpoint-removal")
if mk:
    nl += 1
    if "Not documented in the available source corpus" not in mk:
        fail("lifecycle", "marketplace KU lacks the explicit 'successor not documented' statement")
    outside = re.sub(r"(?m)^>.*$", "", mk)
    for phrase in ("use instead", "has been replaced by", "successor is", "replaced by the"):
        if phrase in outside.lower():
            fail("lifecycle", f"marketplace KU contains unsupported successor wording: {phrase}")
    cited = [p for p in re.findall(r"`(changelog/[^`]+\.md)`", mk)]
    srcs_text = " ".join(re.sub(r"\s+", " ", body_of(rb(os.path.join(CORPUS, p)).decode("utf-8"))) for p in set(cited))
    for q in re.findall(r"(?m)^> (?:- )?(.+)$", mk):
        if re.sub(r"\s+", " ", q).strip() not in srcs_text:
            fail("quote_fidelity", f"marketplace KU quote not found in cited changelog sources: {q[:80]}")
rem = ku_text.get("KU-LIFE-api-endpoints-removed")
if rem:
    nl += 1
    t = rb(os.path.join(CORPUS, "docs/resources/api-endpoints-removed.md")).decode("utf-8")
    nrows = len([tr for tr in re.findall(r"<tr>(.*?)</tr>", t, re.S) if len(re.findall(r"<td", tr)) == 5])
    got = len(re.findall(r"(?m)^\| \d+ \| ", rem.split("## Structured removal register", 1)[-1]))
    if got != nrows:
        fail("lifecycle", f"removal register: {got} structured rows vs {nrows} in source")
done("lifecycle", nl); done("quote_fidelity", 1 if mk else 0)

# ---------------- 6b. link accounting: every operation/event link in a guide body is handled outside the verbatim block ----------------
REFL = re.compile(r"\]\((?:https?://developers\.pismo\.io)?/?(?:pismo-docs/)?reference(?:-link)?/([A-Za-z0-9_\-]+)|\]\(ref:([A-Za-z0-9_\-]+)")
EVL = re.compile(r"developers\.pismo\.io/events/docs/([A-Za-z0-9_\-]+)")
inv_events = {r["event_slug"] for r in rows_csv("api-reference-data/event_type_inventory.csv")}
opid_lower = {o.lower() for o in OPIDS}
nlinks = 0
for k, t in ku_text.items():
    if kus[k].get("ku_type") not in ("workflow_guide", "changelog_history"):
        continue
    verb = "\n".join(c for _, _, _, c in BLOCK.findall(t))
    outside = BLOCK.sub("", t)
    for a, b in REFL.findall(verb):
        s = (a or b).lower()
        nlinks += 1
        if s in opid_lower:
            if not re.search(r"`" + re.escape(s) + r"`", outside, re.I):
                fail("link_accounting", f"{k}: operation link {s} not listed in the operations section")
        elif f"`{s}`" not in outside:
            fail("link_accounting", f"{k}: unresolved operation link {s} not listed with a status")
    if kus[k].get("ku_type") == "workflow_guide":
        for e in set(EVL.findall(verb)):
            nlinks += 1
            if e in inv_events and f"| `{e}` |" not in outside:
                fail("link_accounting", f"{k}: event link {e} (in inventory) not listed in the Events section")
done("link_accounting", nlinks)

# ---------------- 7. contamination and separation ----------------
bad = re.compile(r"pismo_kb_release/|pismo_kb_release\\|corrected_release_candidate|corrected_dataset|pismo_validation|pismo_dataset_final/")
for k, t in ku_text.items():
    if bad.search(t):
        fail("no_r1_or_candidates", f"{k}: references r1/candidate material")
done("no_r1_or_candidates", len(ku_text))
src_hashes = {h for _, h in tree.values()}
for k, t in ku_text.items():
    if sha(t.encode("utf-8")) in src_hashes:
        fail("no_source_copies_in_ku_dir", f"{k}: identical to an original corpus file")
done("no_source_copies_in_ku_dir", len(ku_text))

# ---------------- 8. manifest + coverage tables ----------------
man = list(csv.DictReader(open(os.path.join(MIG, "MIGRATION_MANIFEST.csv"), encoding="utf-8", newline="")))
cov = list(csv.DictReader(open(os.path.join(MIG, "SOURCE_COVERAGE.csv"), encoding="utf-8", newline="")))
if not A.pilot:
    if len(man) != len(tree) or {m["source_path"] for m in man} != set(tree):
        fail("manifest", "manifest rows do not match the corpus file set")
    for m in man:
        if not m["ku_ids"] and not m["exclusion_reason"]:
            fail("manifest", f"{m['source_path']}: no KU and no exclusion reason")
        for k in filter(None, m["ku_ids"].split(";")):
            if k not in kus:
                fail("manifest", f"{m['source_path']}: KU {k} does not exist")
        if m["source_sha256"] != tree[m["source_path"]][1]:
            fail("manifest", f"{m['source_path']}: sha differs")
    for c in cov:
        if c["ku_id"] not in kus:
            fail("coverage", f"coverage row references missing KU {c['ku_id']}")
        if c["source_path"] not in tree:
            fail("coverage", f"coverage row references missing source {c['source_path']}")
    ku_in_cov = {c["ku_id"] for c in cov}
    for k in kus:
        if k not in ku_in_cov:
            fail("coverage", f"KU {k} has no source coverage row")
done("manifest", len(man)); done("coverage", len(cov))

# ---------------- summary + status write-back ----------------
total_fail = sum(len(v) for v in R["failures"].values())
R["counts"] = {"kus_validated": len(kus), "operations_checked": napi, "total_failures": total_fail}
R["failures"] = {k: v[:200] for k, v in R["failures"].items()}
R["failure_totals"] = {k: len(v) for k, v in R["failures"].items()}
out = os.path.join(WORK, "validation_results_pilot.json" if A.pilot else "validation_results.json")
json.dump(R, open(out, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
if not A.pilot:
    failing_kus = {m.split(":")[0] for v in R["failures"].values() for m in v if m.startswith("KU-")}
    for m in man:
        ks = list(filter(None, m["ku_ids"].split(";")))
        bad_src = any(m["source_path"] in x for v in R["failures"].values() for x in v)
        m["validation_status"] = "fail" if bad_src or any(k in failing_kus for k in ks) else "pass"
    with open(os.path.join(MIG, "MIGRATION_MANIFEST.csv"), "w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(man[0])); w.writeheader(); w.writerows(man)
    for c in cov:
        c["validation_status"] = "fail" if c["ku_id"] in failing_kus else "pass"
    with open(os.path.join(MIG, "SOURCE_COVERAGE.csv"), "w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(cov[0])); w.writeheader(); w.writerows(cov)
for k, v in R["checks"].items():
    print(f"{'PASS' if v['failures'] == 0 else 'FAIL'}  {k:<34} checked {v['checked']:>6}  failures {v['failures']:>5}  {v['note']}")
for k, v in R["failures"].items():
    for x in v[:5]:
        print("   ", k, "::", x[:220])
print("TOTAL FAILURES:", total_fail)
sys.exit(0 if total_fail == 0 else 1)
