"""Part 2 - end-to-end arm comparison through the FULL application in-process (FastAPI app, router with its LLM
classifier, persistence, pipeline), on an isolated scratch SQLite database. The running backend, its configuration and the
development database are not touched. The arm only changes the answer call's reasoning_effort ("low" or not sent);
the router classifier keeps its own settings. Sequential requests; arm order alternates per question.

Usage: python -B -E -s e2e_effort.py <out.json> [--repeats N]
"""
import argparse
import json
import os
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
DB = os.path.join(HERE, "e2e_scratch.db").replace("\\", "/")
os.environ.update(DATABASE_URL="sqlite:///" + DB, ASSISTANT_PRELOAD="false", ROUTER_ENABLED="true",
                  HF_HUB_OFFLINE="1", TRANSFORMERS_OFFLINE="1")
sys.path.insert(0, ROOT)
from fastapi.testclient import TestClient  # noqa: E402
from backend.app import models  # noqa: E402,F401
from backend.app.core.config import get_settings  # noqa: E402
from backend.app.db import session as db_session  # noqa: E402
from backend.app.db.base import Base  # noqa: E402
from backend.app.main import create_app  # noqa: E402
from backend.app.services.assistant_service import get_assistant_service  # noqa: E402

# (label, [messages in one session]); follow-ups share the session of their first message
QUESTIONS = [
    ("create transfer", ["How do I create a transfer?"]), ("WEAM0029", ["What does WEAM0029 mean?"]),
    ("webhook auth", ["How does webhook authentication work?"]),
    ("webhook cert URL", ["What certificate URL do I use to verify webhooks in production?"]),
    ("data-platform JWT", ["How do I verify the JWT on Pismo data platform HTTP event deliveries?"]),
    ("release held funds", ["How do I release funds that I previously held on an account?"]),
    ("post-transfers event", ["Which event does post-transfers emit?"]), ("PCI go-live", ["How do I perform PCI card go-live?"]),
    ("rate limit", ["What is the rate limit for Pismo APIs?"]), ("OAuth2", ["How do I get an access token with OAuth2?"]),
    ("cancel transfer", ["How do I cancel a transfer?"]), ("EIBA0005", ["What does EIBA0005 mean?"]),
    ("mTLS webhooks", ["How do I configure mTLS for webhook requests?"]), ("body-hash", ["How do I calculate the webhook body-hash?"]),
    ("marketplace V2 still usable", ["Can I still use the Create marketplace V2 endpoint?"]),
    ("marketplace successor (unanswerable)", ["Which endpoint replaces the removed Create marketplace V2 endpoint?"]),
    ("webhook IPs (unanswerable)", ["Which IP addresses do Pismo webhooks come from?"]),
    ("migrate then go live", ["How do I migrate cards and then make the migrated accounts go live?"]),
    ("transfer required fields", ["Which fields are required to create a transfer?"]),
    ("anti-fraud", ["How does the anti-fraud integration work?"]), ("tokenization", ["How does card tokenization work?"]),
    ("3DS", ["What is 3DS authentication?"]), ("SNS delivery", ["How do I configure real-time event delivery to AWS SNS?"]),
    ("follow-up: hold -> events", ["How do I create a hold on an account?", "Which events does that emit?"]),
    ("follow-up: webhook -> JWT", ["How do I verify webhook requests?", "Can you explain the JWT part?"]),
    ("out of scope", ["What is the capital of France?"]), ("greeting", ["hi"]),
]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("out")
    ap.add_argument("--repeats", type=int, default=2)
    a = ap.parse_args()
    if os.path.exists(DB):
        os.remove(DB)
    get_settings.cache_clear()
    s = get_settings()
    assert s.database_url.startswith("sqlite:///") and DB in s.database_url, "must use the scratch database"
    db_session.configure(s.database_url)
    Base.metadata.create_all(db_session.get_engine())
    service = get_assistant_service()
    t = time.perf_counter()
    service.preload()
    load_s = round(time.perf_counter() - t, 1)
    gen = service._pipeline.generator._inner
    state = {"arm": None, "call": None}
    original = gen.client.chat.completions.create

    def create(**kw):
        if state["arm"] == "low":
            kw["reasoning_effort"] = "low"              # the ONLY difference between the arms
        t0 = time.perf_counter()
        r = original(**kw)
        u = getattr(r, "usage", None)
        det = getattr(u, "completion_tokens_details", None) if u else None
        state["call"] = {"ms": round((time.perf_counter() - t0) * 1000), "completion_tokens": getattr(u, "completion_tokens", None),
                         "reasoning_tokens": getattr(det, "reasoning_tokens", None) if det else None}
        return r
    gen.client.chat.completions.create = create
    print(f"index {service.index_version[:12]} loaded in {load_s}s; answer model {gen.model}; router enabled {s.router_enabled}")
    rows = []
    with TestClient(create_app()) as c:
        for rep in range(a.repeats):
            for i, (label, msgs) in enumerate(QUESTIONS):
                arms = ("default", "low") if (i + rep) % 2 == 0 else ("low", "default")
                for arm in arms:
                    state["arm"] = arm
                    sid = c.post("/api/sessions").json()["id"]
                    for turn, m in enumerate(msgs):
                        state["call"] = None
                        t0 = time.perf_counter()
                        r = c.post(f"/api/sessions/{sid}/messages", json={"content": m})
                        wall = round((time.perf_counter() - t0) * 1000, 1)
                        am = r.json()["assistant_message"]
                        d = am.get("details") or {}
                        rows.append({"label": label, "turn": turn, "rep": rep, "arm": arm, "question": m, "http": r.status_code,
                                     "e2e_ms": wall, "timings": d.get("timings"), "route": d.get("route"), "status": am["status"],
                                     "citations_valid": d.get("citations_valid"), "warnings": d.get("warnings"),
                                     "verification": d.get("verification"), "error": d.get("error"), "call": state["call"],
                                     "evidence": [e["chunk_id"] for e in d.get("evidence") or []],
                                     "citations": [x["chunk_id"] for x in am.get("citations") or []], "answer": am["content"]})
                        x = rows[-1]
                        print(f"r{rep} {arm:7} {label[:30]:30} t{turn} http={x['http']} {wall:7.0f}ms status={x['status']} "
                              f"valid={x['citations_valid']} route={(x['route'] or {}).get('outcome')}")
    json.dump({"load_s": load_s, "rows": rows}, open(a.out, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    os.remove(DB)


if __name__ == "__main__":
    main()
