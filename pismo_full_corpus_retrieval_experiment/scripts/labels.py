"""Gold-label semantics shared by the benchmark builder, the scorer and the tests.

A label is {file, match?} (carried over from the frozen benchmark) or {ku, match?} (KU-generated content).
A chunk satisfies a {file} label when:
  * the chunk's KU was built from `file` (front-matter sources; a trailing '/' means any file under that folder), and
  * the chunk is not inside the verbatim block of a different source file, and
  * for guide/changelog files without a regex, the chunk is inside that file's verbatim block (generated navigation
    sections such as 'Related knowledge units' do not count as evidence), and
  * its body matches the case-insensitive regex `match`, when given.
A chunk satisfies a {ku} label when it belongs to that KU and matches `match`, when given.
"""
import re
from functools import lru_cache


@lru_cache(maxsize=None)
def _rx(pattern):
    return re.compile(pattern, re.I)


def _file_hit(path, f):
    return path == f or (f.endswith("/") and path.startswith(f))


def chunk_satisfies(chunk, label):
    if "ku" in label:
        if chunk["ku_id"] != label["ku"]:
            return False
    else:
        f = label["file"]
        if not any(_file_hit(s, f) for s in chunk["ku_sources"]):
            return False
        src = chunk.get("source_path")
        if src is not None and not _file_hit(src, f):
            return False
        verbatim_kind = f.startswith(("docs/", "changelog/")) or f.endswith(".md")
        if verbatim_kind and not label.get("match") and src is None:
            return False
    m = label.get("match")
    return bool(_rx(m).search(chunk["text"])) if m else True


def label_key(label):
    return ("ku:" + label["ku"] if "ku" in label else label["file"]) + ("|" + label["match"] if label.get("match") else "")
