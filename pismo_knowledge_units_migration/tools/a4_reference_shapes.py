"""Planning probe (read-only): tag sizes, event domains, error prefixes, marketplace successor evidence."""
import re, sys
from collections import Counter, defaultdict
from common import *

sys.stdout.reconfigure(encoding="utf-8")
an = load_json(os.path.join(WORK, "analysis.json"))
tag_ops = Counter((o["spec"], (o["tags"] or ["(untagged)"])[0]) for o in an["operations"])
print("spec/tag groups:", len(tag_ops), "| groups with >25 ops:", [(k, v) for k, v in tag_ops.items() if v > 25])
print("ops with >1 tag:", sum(1 for o in an["operations"] if len(o["tags"]) > 1), "| untagged:", sum(1 for o in an["operations"] if not o["tags"]))
ev = read_csv_rel("api-reference-data/event_type_inventory.csv")
print("event domains:", len({r["domain_guess"] for r in ev}), dict(Counter(r["domain_guess"] for r in ev).most_common(60)))
err = read_csv_rel("api-reference-data/error_code_index.csv")
pre = Counter(re.match(r"[A-Za-z]+", r["code"]).group(0) if re.match(r"[A-Za-z]+", r["code"]) else "(non-alpha)" for r in err)
print("error prefixes:", len(pre), pre.most_common(80))
print("error codes non-standard sample:", [r["code"] for r in err if not re.fullmatch(r"[A-Z]{2,8}[0-9]{2,6}", r["code"])][:40])
ex = read_csv_rel("api-reference-data/request_response_examples.csv")
refrows = [r for r in ex if r["example_json"].strip().startswith('{"$ref"')]
print("example rows:", len(ex), "| $ref-only rows:", len(refrows), "| sample:", refrows[0]["example_json"][:120] if refrows else None)
print("example locations:", Counter(r["location"] for r in ex))
for needle in ("Link marketplace to merchants", "replaced by", "createMarketplaceMerchantsLink", "postlinkmerchanttomarketplacev1", "postmarketplacesv2",
               "getmerchantsbymarketplaceidv2", "putupdatemarketplacev1", "Create marketplace V3"):
    hits = [p for p in corpus_files() if p.endswith((".md", ".yaml", ".csv")) and needle.lower() in read_text(p).lower()]
    print(f"{needle!r}: {len(hits)} files: {hits[:12]}")
