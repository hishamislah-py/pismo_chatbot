"""Command-line entry point.

    python -m pismo_assistant "How do I release funds that I previously held?"
    python -m pismo_assistant --evidence-only "What does WEAM0029 mean?"   (no OpenAI call)
    python -m pismo_assistant --json "..."
"""
import argparse
import json
import sys

from .pipeline import Assistant


def render(result):
    out = [f"Status: {result['status']}"]
    if result.get("error"):
        out.append(f"Error: {result['error']['kind']}: {result['error']['message']}")
    if result.get("answer"):
        out += ["", result["answer"]]
    if result.get("citations"):
        out += ["", "Sources:"]
        for c in result["citations"]:
            srcs = "; ".join(f"{s['path']} <{s['url']}>" for s in c["sources"])
            out.append(f"  [{c['label']}] {c['ku_id']} - {c['title']} / {c['section']} - {srcs}")
    for w in result.get("warnings", []):
        out.append(f"WARNING: {w}")
    out += ["", "Evidence passed to the generator:"]
    for e in result["evidence"]:
        out.append(f"  {e['label']} {e['chunk_id']} ({e['origin']}: {e['reason']})")
    return "\n".join(out)


def main(argv=None):
    p = argparse.ArgumentParser(prog="pismo_assistant")
    p.add_argument("question")
    p.add_argument("--evidence-only", action="store_true", help="retrieve and assemble evidence without calling OpenAI")
    p.add_argument("--json", action="store_true")
    a = p.parse_args(argv)
    sys.stdout.reconfigure(encoding="utf-8")
    result = Assistant().answer(a.question, generate=not a.evidence_only)
    print(json.dumps(result, ensure_ascii=False, indent=1) if a.json else render(result))
    return 0 if result["status"] not in ("generation_error",) else 2


if __name__ == "__main__":
    sys.exit(main())
