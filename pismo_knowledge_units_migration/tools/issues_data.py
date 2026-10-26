"""Collect measured facts for ISSUES_AND_GAPS.md and VALIDATION_REPORT.md (read-only). Writes work/issues_data.json."""
import re, sys
from collections import Counter, defaultdict
import yaml
from common import *

sys.stdout.reconfigure(encoding="utf-8")
an = load_json(os.path.join(WORK, "analysis.json"))
ix = load_json(os.path.join(WORK, "ku_index.json"))
blog = load_json(os.path.join(WORK, "build_log.json"))
D = {}
kutext = {}
for k, v in ix.items():
    with open(os.path.join(MIG, v["path"]), encoding="utf-8", newline="") as fh:
        kutext[k] = fh.read()

# unresolved operation links (guides + changelogs), with classification taken from the KU tables
unres = defaultdict(lambda: {"sources": set(), "status": ""})
for k, t in kutext.items():
    for m in re.finditer(r"^\| `([a-z0-9_\-]+)` \| (.*?) \| (not found in the current OpenAPI.*?) \|$", t, re.M):
        u = unres[m.group(1)]
        u["sources"] |= {s for s in ix[k]["sources"] if s.endswith(".md")}
        u["status"] = "name-matched to removed endpoint" if "removed-endpoints list" in m.group(3) else "unverified"
# attribute each slug to the exact source files that link it (a KU table may cover several grouped sources)
src_of = defaultdict(set)
for p, g in an["guides"].items():
    for s in g["ref_unresolved"]:
        src_of[s.lower()].add(p)
D["unresolved_links"] = {s: {"sources": sorted(src_of.get(s) or v["sources"]), "status": v["status"]} for s, v in sorted(unres.items())}
D["unresolved_counts"] = dict(Counter(v["status"] for v in unres.values()))

# removal-register rows whose path is still in current specs
reg = kutext["KU-LIFE-api-endpoints-removed"].split("## Structured removal register", 1)[1].split("\n## ", 1)[0]
D["removal_rows_still_in_specs"] = [l for l in reg.splitlines() if re.match(r"^\| \d+ \|", l) and "| yes:" in l]
D["removal_rows_blank_date"] = [l for l in reg.splitlines() if "`(blank)`" in l]
D["removal_date_formats"] = sorted({m for m in re.findall(r"\| `([0-9/]+)` \|", reg)})

# empty links in sources
empt = []
for p in corpus_files():
    if p.endswith(".md"):
        for i, l in enumerate(read_text(p).split("\n"), 1):
            for m in re.finditer(r"\[([^\]]+)\]\(\)", l):
                empt.append(f"{p}:{i} {m.group(0)}")
D["empty_links"] = empt

# bare CR characters in sources
D["bare_cr_sources"] = [p for p in corpus_files() if b"\r" in read_bytes(p).replace(b"\r\n", b"")]

# error codes in YAML examples absent from error_code_index.csv
idx_codes = {r["code"] for r in read_csv_rel("api-reference-data/error_code_index.csv")}
yaml_codes = set()
for k, t in kutext.items():
    if ix[k]["ku_type"] == "api_reference":
        for sec in t.split("#### Error codes shown in this operation's response examples")[1:]:
            yaml_codes |= set(re.findall(r"^\| \S+ \| `([A-Z0-9]+)` \|", sec.split("\n#### ")[0], re.M))
missing = sorted(yaml_codes - idx_codes)
D["codes_in_examples_not_in_index"] = {"count": len(missing), "sample": missing[:40],
                                       "pattern_letters_then_digits": sum(1 for c in missing if re.fullmatch(r"[A-Z]{2,8}[0-9]{2,6}", c))}

# oversized KUs, depth-limit truncation, not-rendered examples
D["kus_over_100KB"] = sorted(((len(t.encode()), k) for k, t in kutext.items() if len(t.encode()) > 100_000), reverse=True)
D["depth_limit_rows"] = sum(t.count("nested object not expanded (depth limit)") for t in kutext.values())
D["examples_not_rendered"] = sum(t.count("**not rendered**") for t in kutext.values())
D["kind_mismatch_refs"] = blog["kind_mismatch_refs"]
D["unresolved_refs"] = blog["unresolved_refs"]
D["split_guides"] = blog["split_guides"]
D["identical_bodies"] = an["identical_bodies"]
D["duplicate_operation_ids"] = an["duplicate_operation_ids"]
D["event_links_not_in_inventory"] = sorted({e for g in an["guides"].values() for e in g["event_slugs"]} -
                                           {r["event_slug"] for r in read_csv_rel("api-reference-data/event_type_inventory.csv")})
D["outdated_or_beta_titles"] = sorted(p for p, g in an["guides"].items() if re.search(r"(?i)\(outdated\)|\bbeta\b", g["title"]))
D["ku_counts"] = {"total": len(ix), "by_category": dict(Counter(v["category"] for v in ix.values())), "by_type": dict(Counter(v["ku_type"] for v in ix.values()))}
D["ku_bytes_total"] = sum(len(t.encode()) for t in kutext.values())
D["deprecated_ops"] = sum(1 for k, t in kutext.items() if ix[k]["ku_type"] == "api_reference" for _ in re.finditer(r"- \*\*Deprecated in specification:\*\* \*\*yes\*\*", t))
D["multi_source_guide_kus"] = sum(1 for v in ix.values() if v["ku_type"] == "workflow_guide" and len([s for s in v["sources"] if s.endswith(".md")]) > 1)
dump_json(os.path.join(WORK, "issues_data.json"), D)
for k, v in D.items():
    s = json.dumps(v, ensure_ascii=False, default=str)
    print(f"{k}: {s[:600]}")
