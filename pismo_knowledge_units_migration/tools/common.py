"""Shared helpers for the Pismo KB r2 -> knowledge-unit migration. Read-only on the corpus; standard library + PyYAML only."""
import csv, hashlib, json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
MIG = os.path.dirname(HERE)                                   # pismo_knowledge_units_migration/
PROJECT = os.path.dirname(MIG)
RELEASE = os.path.join(PROJECT, "pismo_kb_release_r2")
CORPUS = os.path.join(RELEASE, "kb_corpus")
SOURCE_MAP = os.path.join(RELEASE, "internal", "provenance", "source_map.csv")
ALLOWLIST = os.path.join(RELEASE, "internal", "kb_corpus_allowlist.json")
WORK = os.path.join(MIG, "work")                              # intermediate, reproducible artefacts
KU_ROOT = os.path.join(MIG, "knowledge_units")
# Accepted fingerprints of KB r2 (project README, 2026-10-19)
CORPUS_P = "7080b549e8160a2bc555ae1c0646b4d9a807414cd12dbd1943e712f5031f0e62"

csv.field_size_limit(10 ** 9)


def sha_bytes(b):
    return hashlib.sha256(b).hexdigest()


def read_bytes(rel):
    with open(os.path.join(CORPUS, rel), "rb") as fh:
        return fh.read()


def read_text(rel):
    return read_bytes(rel).decode("utf-8")


def corpus_files():
    out = []
    for r, _, fs in os.walk(CORPUS):
        for f in fs:
            out.append(os.path.relpath(os.path.join(r, f), CORPUS).replace(os.sep, "/"))
    return sorted(out)


def corpus_tree():
    return {p: (len(b), sha_bytes(b)) for p in corpus_files() for b in [read_bytes(p)]}


def fp_P(tree):
    return sha_bytes("".join(f"{k}\t{v[0]}\t{v[1]}\n" for k, v in sorted(tree.items())).encode("utf-8"))


def source_type(rel):
    if rel.startswith("changelog/"):
        return "changelog_markdown"
    if rel.startswith("docs/"):
        return "guide_markdown"
    if rel.startswith("api-specs/") and rel.endswith(".yaml"):
        return "openapi_yaml"
    if rel.startswith("api-specs/") and rel.endswith(".md"):
        return "spec_repository_readme"
    if rel.startswith("api-reference-data/") and rel.endswith(".csv"):
        return "reference_table_csv"
    return "other"


def load_source_map():
    with open(SOURCE_MAP, encoding="utf-8", newline="") as fh:
        rows = list(csv.DictReader(fh))
    return {r["corpus_path"][len("kb_corpus/"):]: r for r in rows}


def read_csv_rel(rel):
    with open(os.path.join(CORPUS, rel), encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh))


def write_csv(path, fields, rows):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=fields, extrasaction="raise")
        w.writeheader()
        w.writerows(rows)


def dump_json(path, obj):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(obj, fh, indent=1, ensure_ascii=False)


def load_json(path):
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


FRONT = re.compile(r"\A---\r?\n(.*?)\r?\n---\r?\n", re.S)


def split_front_matter(text):
    m = FRONT.match(text)
    if not m:
        return {}, text
    meta = {}
    for line in m.group(1).splitlines():
        mm = re.match(r"^([A-Za-z_]+):\s*(.*)$", line)
        if mm and mm.group(2).strip():
            meta[mm.group(1)] = mm.group(2).strip()
    return meta, text[m.end():]


def slugify(s, maxlen=60):
    s = re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")
    return s[:maxlen].rstrip("-") or "x"
