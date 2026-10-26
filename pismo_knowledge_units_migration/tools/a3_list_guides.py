"""Print a compact guide listing per area for planning (read-only; uses work/analysis.json)."""
import sys
from common import *

an = load_json(os.path.join(WORK, "analysis.json"))
area = sys.argv[1] if len(sys.argv) > 1 else None
sys.stdout.reconfigure(encoding="utf-8")
for p, g in sorted(an["guides"].items()):
    if g["type"] != "guide_markdown":
        continue
    a = p.split("/")[1]
    if area and a != area:
        continue
    print(f"{a[:14]:<14} {os.path.basename(p)[:-3][:58]:<58} {g['chars']:>6} r{len(g['ref_resolved']):<3}u{len(g['ref_unresolved']):<2} d{len(g['doc_links_resolved']):<3} | {g['title'][:70]}")
