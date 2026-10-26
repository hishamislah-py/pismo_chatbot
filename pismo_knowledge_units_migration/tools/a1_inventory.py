"""Phase A1: inventory the authoritative corpus (read-only) and record it.

Writes archived_source_inventory/SOURCE_INVENTORY.csv and work/inventory_check.json.
Stops (exit 2) if the corpus differs from the accepted fingerprint or from its allowlist.
"""
import json, os, sys
from collections import Counter
from common import *

tree = corpus_tree()
allow = load_json(ALLOWLIST)
am = {a["path"][len("kb_corpus/"):]: (a["bytes"], a["sha256"]) for a in allow["allowlist"]}
smap = load_source_map()
check = {
    "corpus_files": len(tree),
    "corpus_fingerprint_P": fp_P(tree),
    "fingerprint_matches_accepted": fp_P(tree) == CORPUS_P,
    "allowlist_files": allow["files"],
    "allowlist_equals_corpus": am == tree,
    "source_map_rows": len(smap),
    "source_map_covers_corpus": set(smap) == set(tree),
    "source_map_hash_mismatches": sorted(p for p in tree if smap.get(p, {}).get("corpus_sha256") != tree[p][1]),
    "by_type": dict(Counter(source_type(p) for p in tree)),
    "by_top_folder": dict(Counter(p.split("/")[0] for p in tree)),
    "by_extension": dict(Counter(os.path.splitext(p)[1] for p in tree)),
    "guide_areas": dict(Counter(p.split("/")[1] for p in tree if p.startswith("docs/"))),
}
rows = []
for p, (size, h) in sorted(tree.items()):
    s = smap[p]
    rows.append({"source_path": p, "source_type": source_type(p), "bytes": size, "sha256": h,
                 "source_url": s["source_url"], "source_markdown_url": s["source_markdown_url"], "title": s["title"],
                 "product_area": s["product_area"], "updated_at": s["updated_at"], "retrieved_at": s["retrieved_at"],
                 "openapi_commit": s["openapi_commit"], "source_map_kind": s["kind"]})
write_csv(os.path.join(MIG, "archived_source_inventory", "SOURCE_INVENTORY.csv"), list(rows[0]), rows)
dump_json(os.path.join(WORK, "inventory_check.json"), check)
print(json.dumps(check, indent=1))
ok = check["fingerprint_matches_accepted"] and check["allowlist_equals_corpus"] and check["source_map_covers_corpus"] \
     and not check["source_map_hash_mismatches"]
sys.exit(0 if ok else 2)
