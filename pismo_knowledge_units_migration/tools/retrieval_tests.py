"""Phase D retrieval-usability tests over the KU collection (no network, no extra packages).

Questions were written from the source corpus before evaluation (each cites its evidence). Ranking: KUs containing an exact
identifier from the question first (exact lookup), then BM25 (k1=1.5, b=0.75) over KU text with an identifier-preserving
tokenizer. Unanswerable questions pass when the identifier occurs in no KU, or when the named KU states the gap explicitly.
Usage: python -B -E -s retrieval_tests.py   -> work/retrieval_test_results.json; exit 1 if any test fails.
"""
import json, math, os, re, sys
from collections import Counter

MIG = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KUDIR = os.path.join(MIG, "knowledge_units")

Q = [  # id, type, question, expected KU ids (any), k, evidence
    ("X1", "exact", "post-payments-v1-hold-funds-unblock", ["KU-API-core-platform-payment-methods--hold-funds"], 5, "Core_platform_-_Payment_methods.yaml"),
    # X2 corrected after first run: WEAM0029 occurs only in changelog/2-october-2026.md (removed code); it is not in the
    # current specifications or error_code_index.csv, so the expected answer is the changelog record.
    ("X2", "exact", "What does WEAM0029 mean?", ["KU-CHG-2-october-2026"], 5, "changelog/2-october-2026.md only"),
    ("X7", "exact", "What does error WEAM0001 mean?", ["KU-ERR-codes-weam"], 5, "error_code_index.csv row WEAM0001"),
    ("X3", "exact", "POST /v1/migrations/cards-pci", ["KU-API-migrations--card-migration"], 5, "Migrations.yaml"),
    ("X4", "exact", "Can I still call postmarketplacesv2?", ["KU-LIFE-marketplace-endpoint-removal"], 5, "seller guides + api-endpoints-removed.md"),
    ("X5", "exact", "EIBACC0379", ["KU-ERR-codes-eibacc"], 5, "error_code_index.csv"),
    ("X6", "exact", "createMarketplaceMerchantsLink", ["KU-API-seller-management-sellers--marketplace-merchants-links"], 5, "Seller_management_-_Sellers.yaml"),
    ("N1", "natural", "How do I release funds that I previously held on an account?", ["KU-PAY-hold-funds"], 10, "docs/core-platform/hold-funds.md"),
    ("N2", "natural", "How do I cancel a transfer?", ["KU-PAY-transfers-make-and-cancel"], 10, "docs/core-platform/cancel-transfer.md"),
    ("N3", "natural", "How do I authenticate with OpenID Connect and obtain an access token?", ["KU-AUTH-authentication-methods"], 10, "authentication-with-openid.md"),
    ("N4", "natural", "How do I set up real-time event delivery and event filtering?", ["KU-EVT-real-time-event-delivery"], 10, "setting-up-real-time-event-delivery.md"),
    ("N5", "natural", "How do I verify that a webhook request was sent by Pismo?", ["KU-EVT-verifying-webhook-requests"], 10, "verifying-webhook-requests.md"),
    ("N6", "natural", "How does rate limiting work on the Pismo platform?", ["KU-SUP-rate-limiting"], 10, "api-get-started/rate-limiting.md"),
    ("N7", "natural", "How do I open a service request with the Pismo Service Desk?", ["KU-SUP-service-desk-requests"], 10, "opening-a-service-desk-ticket.md"),
    ("N8", "natural", "How is a dormant account reactivated and what is a dormancy reactivation exception?", ["KU-BANK-dormancy"], 10, "dormancy-*.md"),
    ("N9", "natural", "How do I create a Pix QR code?", ["KU-PAY-pix-and-qr-codes"], 10, "pix-and-qr-codes.md"),
    ("N10", "natural", "What calendar management strategies exist for cycle closing and due dates?", ["KU-CRED-calendar-management-strategies"], 10, "calendar-management-strategies.md"),
    ("N11", "natural", "How do I configure mTLS identity connectivity?", ["KU-AUTH-identity-connectivity-with-mtls"], 10, "identity-connectivity-with-mtls.md"),
    ("R1", "request_response", "Which request fields are required to block an amount with hold funds?", ["KU-API-core-platform-payment-methods--hold-funds", "KU-PAY-hold-funds"], 10, "HoldFundsRequest"),
    ("R2", "request_response", "Migrate PCI cards with encrypted_pan key_id and iv instead of pan", ["KU-API-migrations--card-migration"], 10, "PciCardsV1Request"),
    ("L1", "lifecycle", "Which marketplace endpoints were decommissioned and when were they removed?", ["KU-LIFE-marketplace-endpoint-removal", "KU-LIFE-api-endpoints-removed"], 10, "api-endpoints-removed.md; changelog 2 October 2026"),
    ("L2", "lifecycle", "What changed in the 2 October 2026 changelog?", ["KU-CHG-2-october-2026"], 10, "changelog/2-october-2026.md"),
    ("L3", "lifecycle", "Was the CRM API decommissioned and removed?", ["KU-LIFE-api-endpoints-removed", "KU-CHG-2-july-2026"], 10, "api-endpoints-removed.md; changelog 2 July 2026"),
    ("E1", "error", "What does error code WONP0001 mean?", ["@code:WONP0001"], 5, "error_code_index.csv"),
    ("E2", "error", "authorization validation code definitions for denied transactions", ["KU-ERR-validation-code-definitions"], 10, "validation-code-definitions.md"),
]
NOT_DOCUMENTED = [  # id, question, identifier that must not occur in any KU, or (KU id, required statement)
    ("U1", "How do I call the PCI card go-live endpoint cards-pci/go-live?", "cards-pci/go-live", None),
    ("U2", "What does error MIGR-0400 mean?", "MIGR-0400", None),
    ("U3", "Which payload fields does the authorization-authorization-event-1 event contain?", None, ("@event:authorization-authorization-event-1", "not documented in the available source corpus")),
    ("U4", "Which endpoint replaces the removed Create marketplace V2 endpoint?", None, ("KU-LIFE-marketplace-endpoint-removal", "Not documented in the available source corpus")),
]

docs, meta = {}, {}
for r_, _, fs in os.walk(KUDIR):
    for f in fs:
        if f.endswith(".md"):
            t = open(os.path.join(r_, f), encoding="utf-8", newline="").read()
            m = re.match(r"\A---\n(.*?)\n---\n", t, re.S)
            kid = re.search(r"(?m)^ku_id: (\S+)", m.group(1)).group(1)
            docs[kid] = t
            meta[kid] = {"codes": re.findall(r"(?m)^- (\S+)$", m.group(1).split("error_codes:")[1]) if "error_codes:" in m.group(1) else [],
                         "events": re.findall(r"(?m)^- (\S+)$", m.group(1).split("events:")[1]) if "\nevents:" in "\n" + m.group(1) else []}
STOP = set("a an the of to in for on and or is are be do does i my we our how what which when why can should with from that this it as by at into was were".split())


def tok(s):
    s = s.lower()
    return [t for t in re.findall(r"[a-z0-9]+", s) + re.findall(r"[a-z0-9]+(?:[-_/.][a-z0-9]+)+", s) if t not in STOP]


ids = sorted(docs)
tf = {k: Counter(tok(docs[k])) for k in ids}
dl = {k: sum(tf[k].values()) for k in ids}
avg = sum(dl.values()) / len(ids)
df = Counter(t for k in ids for t in tf[k])
N = len(ids)


def bm25(q):
    qt = tok(q)
    sc = {}
    for k in ids:
        s = 0.0
        for t in qt:
            f = tf[k].get(t)
            if f:
                idf = math.log(1 + (N - df[t] + 0.5) / (df[t] + 0.5))
                s += idf * f * 2.5 / (f + 1.5 * (1 - 0.75 + 0.75 * dl[k] / avg))
        sc[k] = s
    return sorted(ids, key=lambda k: -sc[k])


ID_RX = re.compile(r"[A-Z][A-Z0-9]{1,9}[0-9]{3,6}|/[a-z0-9][A-Za-z0-9{}_\-/.]*|\b[a-z]+(?:-[a-z0-9]+){2,}\b|\b[a-z]+[A-Z][A-Za-z0-9]+\b|\b[a-z]{6,}v[0-9]\b")


def rank(q):
    idents = ID_RX.findall(q)
    exact = [k for k in ids if any(i in docs[k] for i in idents)] if idents else []
    b = bm25(q)
    exact.sort(key=b.index)
    return exact + [k for k in b if k not in exact], idents


res, fails = [], 0
for qid, typ, q, exp, k, ev in Q:
    exp2 = []
    for e in exp:
        if e.startswith("@code:"):
            exp2 += [x for x in ids if e[6:] in meta[x]["codes"]]
        else:
            exp2.append(e)
    missing = [e for e in exp2 if e not in docs]
    ranked, idents = rank(q)
    pos = min((ranked.index(e) + 1 for e in exp2 if e in docs), default=None)
    ok = pos is not None and pos <= k and not missing
    fails += not ok
    res.append({"id": qid, "type": typ, "question": q, "expected": exp2, "first_expected_rank": pos, "k": k, "pass": ok,
                "identifiers_detected": idents, "top5": ranked[:5], "evidence": ev, "missing_expected_kus": missing})
for qid, q, ident, need in NOT_DOCUMENTED:
    if ident:
        hits = [k for k in ids if ident in docs[k]]
        ok = not hits
        res.append({"id": qid, "type": "not_documented", "question": q, "identifier": ident, "kus_containing": hits, "pass": ok})
    else:
        target, stmt = need
        if target.startswith("@event:"):
            targets = [x for x in ids if target[7:] in meta[x]["events"] and x.startswith("KU-EVT-catalogue")]
        else:
            targets = [target]
        ok = bool(targets) and all(t in docs and stmt in docs[t] for t in targets)
        res.append({"id": qid, "type": "not_documented", "question": q, "kus": targets, "required_statement": stmt, "pass": ok})
    fails += not ok
json.dump(res, open(os.path.join(MIG, "work", "retrieval_test_results.json"), "w", encoding="utf-8"), indent=1, ensure_ascii=False)
for r in res:
    print(f"{'PASS' if r['pass'] else 'FAIL'}  {r['id']:<4} {r['type']:<17} rank {str(r.get('first_expected_rank', '-')):>4}  {r['question'][:70]}"
          + ("" if r["pass"] else f"  top5={r.get('top5') or r.get('kus_containing') or r.get('kus')}"))
print(f"{len(res) - fails}/{len(res)} passed")
sys.exit(1 if fails else 0)
