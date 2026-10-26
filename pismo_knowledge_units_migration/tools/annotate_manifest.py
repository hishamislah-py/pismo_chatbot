"""Write issue IDs (defined in ISSUES_AND_GAPS.md) into the `issues` column of MIGRATION_MANIFEST.csv, from measured data.

Run after build_kus.py and issues_data.py, before validate.py.
"""
from collections import defaultdict
from common import *

D = load_json(os.path.join(WORK, "issues_data.json"))
ix = load_json(os.path.join(WORK, "ku_index.json"))
tag = defaultdict(set)
for slug, v in D["unresolved_links"].items():
    if "marketplace" in slug and v["status"] != "unverified":
        for p in v["sources"]:
            tag[p].add("SC-01")
for p in ("docs/resources/api-endpoints-removed.md", "changelog/2-october-2026.md"):
    tag[p] |= {"SC-02", "SG-02"}
tag["docs/resources/api-endpoints-removed.md"] |= {"SC-03", "SC-08", "SG-07"}
tag["api-specs/Card_issuing_-_Cards_on_file.yaml"].add("SC-03")
for ref, _, ctx in D["kind_mismatch_refs"]:
    tag[ctx.split(" ")[0]].add("SC-04")
for pair in D["identical_bodies"]:
    for p in pair:
        tag[p].add("SC-05")
for p in ("docs/control-center/get-started-with-control-center.md", "docs/get-started/get-started-building-control-center.md",
          "docs/card-issuing/transaction-category-structure.md", "docs/control-center/cc-manage-transaction-categories.md"):
    tag[p].add("SC-05")
for opid, locs in D["duplicate_operation_ids"].items():
    for l in locs:
        tag[l.split(":")[0]].add("SC-06")
for e in D["empty_links"]:
    tag[e.split(":")[0]].add("SC-07")
for p in D["bare_cr_sources"]:
    tag[p].add("SC-08")
for p in D["outdated_or_beta_titles"]:
    tag[p].add("SC-09")
for slug, v in D["unresolved_links"].items():
    for p in v["sources"]:
        tag[p].add("UR-01")
tag["api-reference-data/error_code_index.csv"].add("SG-05")
tag["api-reference-data/event_type_inventory.csv"] |= {"SG-01", "SG-06"}
tag["api-reference-data/endpoint_event_map.csv"].add("SG-01")
tag["api-specs/Migrations.yaml"].add("SG-03")
for p in (x for x in corpus_files() if x.startswith("changelog/")):
    tag[p].add("SG-04")
big = {k for _, k in D["kus_over_100KB"]}
for k in big:
    for s in ix[k]["sources"]:
        if not s.startswith("api-reference-data/"):
            tag[s].add("MD-07")
path = os.path.join(MIG, "MIGRATION_MANIFEST.csv")
rows = list(csv.DictReader(open(path, encoding="utf-8", newline="")))
for r in rows:
    r["issues"] = ";".join(sorted(tag.get(r["source_path"], set())))
write_csv(path, list(rows[0]), rows)
print("sources tagged:", sum(1 for r in rows if r["issues"]), "of", len(rows))
