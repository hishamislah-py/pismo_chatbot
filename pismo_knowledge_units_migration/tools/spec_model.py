"""OpenAPI model and Markdown renderer for API-reference content.

$ref resolution follows the full JSON pointer inside the same document (e.g. #/components/schemas/X); it never matches by
the final name alone. Unresolvable or non-local pointers are recorded in Spec.unresolved and rendered as unresolved.
Examples are rendered only from concrete example values in the source (media-type `example`/`examples`, or
#/components/examples/* targets); no example is synthesised from a schema.
"""
import json, re
from urllib.parse import urlparse
import yaml
from common import *

METHODS = ("get", "put", "post", "delete", "patch", "head", "options", "trace")
# error codes such as WEAM0029, EIBACC0379 and also alphanumeric-prefix codes such as WP2P0000 / EP2P0010
CODE_RX = re.compile(r"^[A-Z][A-Z0-9]{1,9}[0-9]{3,6}$")
CONSTRAINT_KEYS = ("enum", "const", "default", "format", "pattern", "minimum", "maximum", "exclusiveMinimum", "exclusiveMaximum",
                   "minLength", "maxLength", "minItems", "maxItems", "uniqueItems", "multipleOf", "nullable", "readOnly", "writeOnly",
                   "deprecated", "example", "examples")
MAX_DEPTH = 6


def jdump(v):
    return json.dumps(v, ensure_ascii=False, default=str)


def cell(s):
    s = "" if s is None else str(s)
    return s.replace("\\", "\\\\").replace("|", "\\|").replace("\r\n", "\n").replace("\r", "\n").replace("\n", "<br>").strip()


def quote_block(text):
    text = str(text).replace("\r\n", "\n").rstrip("\n")
    return "\n".join("> " + l if l.strip() else ">" for l in text.split("\n"))


class Spec:
    def __init__(self, rel):
        self.rel = rel
        self.doc = yaml.safe_load(read_text(rel))
        info = self.doc.get("info") or {}
        self.title = info.get("title") or os.path.basename(rel)
        self.version = info.get("version")
        self.servers = [s.get("url") for s in self.doc.get("servers") or [] if isinstance(s, dict)]
        bp = {urlparse(u).path.rstrip("/") for u in self.servers if u}
        self.base_paths = sorted(bp)
        self.unresolved = []          # (pointer, context)
        self.kind_mismatch = []       # (pointer, expected component type, context)
        self.tag_desc = {t.get("name"): t.get("description", "") for t in self.doc.get("tags") or [] if isinstance(t, dict)}
        self.schemes = (self.doc.get("components") or {}).get("securitySchemes") or {}

    # ---------- $ref ----------
    def pointer(self, ref):
        if not isinstance(ref, str) or not ref.startswith("#/"):
            return None
        node = self.doc
        for part in ref[2:].split("/"):
            part = part.replace("~1", "/").replace("~0", "~")
            if isinstance(node, dict) and part in node:
                node = node[part]
            elif isinstance(node, list) and part.isdigit() and int(part) < len(node):
                node = node[int(part)]
            else:
                return None
        return node

    def deref(self, node, expect=None, ctx=""):
        """Follow a $ref chain by full pointer. Returns (resolved_node_or_None, [pointers], sibling_keys)."""
        chain, siblings = [], {}
        while isinstance(node, dict) and "$ref" in node:
            ref = node["$ref"]
            if not chain:
                siblings = {k: v for k, v in node.items() if k != "$ref"}
            if ref in chain:
                self.unresolved.append((ref, ctx + " (reference cycle)"))
                return None, chain + [ref], siblings
            chain.append(ref)
            if expect and isinstance(ref, str) and ref.startswith("#/components/") and not ref.startswith(f"#/components/{expect}/"):
                self.kind_mismatch.append((ref, expect, ctx))
            tgt = self.pointer(ref)
            if tgt is None:
                self.unresolved.append((ref, ctx))
                return None, chain, siblings
            node = tgt
        return node, chain, siblings

    @staticmethod
    def ref_name(ptr):
        return ptr.rsplit("/", 1)[-1] if ptr else ""

    # ---------- schema description ----------
    def type_label(self, sch, ctx):
        res, chain, _ = self.deref(sch, "schemas", ctx)
        named = f" (schema `{self.ref_name(chain[-1])}`)" if chain else ""
        if res is None:
            return f"unresolved reference `{chain[-1] if chain else sch}`"
        if not isinstance(res, dict):
            return "(non-object schema)"
        t = res.get("type")
        if isinstance(t, list):
            t = " \\| ".join(map(str, t))
        if res.get("type") == "array" or (t is None and "items" in res):
            return "array of " + self.type_label(res.get("items") or {}, ctx) + named
        for comb in ("oneOf", "anyOf"):
            if comb in res:
                return f"{comb}: " + ", ".join(self.type_label(x, ctx) for x in res[comb]) + named
        if t is None and ("properties" in res or "allOf" in res):
            t = "object"
        if t == "object" and not res.get("properties") and isinstance(res.get("additionalProperties"), dict):
            return "object (map of " + self.type_label(res["additionalProperties"], ctx) + ")" + named
        return (t or "(type not declared)") + named

    def constraints(self, sch, ctx):
        res, chain, sib = self.deref(sch, "schemas", ctx)
        out = []
        for src in (res if isinstance(res, dict) else {}, sib):
            for k in CONSTRAINT_KEYS:
                if k in src:
                    item = f"{k}: {jdump(src[k])}"
                    if item not in out:
                        out.append(item)
        if isinstance(res, dict) and res.get("type") == "array" and isinstance(res.get("items"), dict):
            ires, _, _ = self.deref(res["items"], "schemas", ctx)
            if isinstance(ires, dict):
                for k in ("enum", "format", "pattern", "minLength", "maxLength"):
                    if k in ires:
                        out.append(f"items.{k}: {jdump(ires[k])}")
        return "; ".join(out)

    def description(self, sch, ctx):
        res, chain, sib = self.deref(sch, "schemas", ctx)
        if "description" in sib:
            return sib["description"]
        return res.get("description", "") if isinstance(res, dict) else ""

    def collect_props(self, sch, ctx, seen=None):
        """Properties (ordered) and required names of an object schema, merging allOf parts."""
        seen = seen or set()
        res, chain, _ = self.deref(sch, "schemas", ctx)
        if not isinstance(res, dict) or id(res) in seen:
            return [], set(), []
        seen = seen | {id(res)}
        props, req, notes = [], set(res.get("required") or []), []
        for part in res.get("allOf") or []:
            p2, r2, n2 = self.collect_props(part, ctx, seen)
            _, pch, _ = self.deref(part, "schemas", ctx)
            if pch:
                notes.append(f"includes the fields of schema `{self.ref_name(pch[-1])}` (allOf)")
            props += p2; req |= r2; notes += n2
        for name, sub in (res.get("properties") or {}).items():
            props.append((name, sub))
        return props, req, notes

    def field_rows(self, sch, ctx, named, prefix="", depth=0, stack=()):
        props, req, _ = self.collect_props(sch, ctx)
        rows = []
        for name, sub in props:
            full = prefix + name
            rows.append({"field": full, "type": self.type_label(sub, ctx), "required": "yes" if name in req else "no",
                         "description": self.description(sub, ctx), "constraints": self.constraints(sub, ctx)})
            res, chain, _ = self.deref(sub, "schemas", ctx)
            target, tchain, arr = res, chain, False
            if isinstance(res, dict) and (res.get("type") == "array" or "items" in res):
                target, tchain, _ = self.deref(res.get("items") or {}, "schemas", ctx)
                arr = True
            if not isinstance(target, dict):
                continue
            if tchain:  # named schema: documented once in the Schemas section
                if self._is_structured(target):
                    named.append(tchain[-1])
                continue
            for comb in ("oneOf", "anyOf"):
                for k, opt in enumerate(target.get(comb) or [], 1):
                    ores, och, _ = self.deref(opt, "schemas", ctx)
                    if och and self._is_structured(ores):
                        named.append(och[-1])
                    elif isinstance(ores, dict) and self._is_structured(ores) and depth < MAX_DEPTH:
                        rows += self.field_rows(opt, ctx, named, f"{full}{'[]' if arr else ''} ({comb} option {k}).", depth + 1, stack)
            if (target.get("properties") or target.get("allOf")) and depth < MAX_DEPTH and id(target) not in stack:
                rows += self.field_rows(target, ctx, named, full + ("[]." if arr else "."), depth + 1, stack + (id(target),))
            elif (target.get("properties") or target.get("allOf")) and depth >= MAX_DEPTH:
                rows.append({"field": full + ("[]" if arr else "") + ".…", "type": "nested object not expanded (depth limit)",
                             "required": "", "description": "", "constraints": ""})
        return rows

    @staticmethod
    def _is_structured(s):
        return isinstance(s, dict) and bool(s.get("properties") or s.get("allOf") or s.get("oneOf") or s.get("anyOf")
                                            or (s.get("type") == "object" and s.get("additionalProperties")))

    # ---------- operations ----------
    def operations(self):
        out = []
        for path, item in (self.doc.get("paths") or {}).items():
            if not isinstance(item, dict):
                continue
            for m in METHODS:
                op = item.get(m)
                if isinstance(op, dict):
                    out.append((path, m, op, item))
        return out

    def params(self, item, op, ctx):
        merged = {}
        for src in (item.get("parameters") or [], op.get("parameters") or []):
            for p in src:
                res, chain, _ = self.deref(p, "parameters", ctx)
                if isinstance(res, dict):
                    merged[(res.get("name"), res.get("in"))] = (res, chain)
                else:
                    merged[(f"unresolved {chain[-1] if chain else p}", "?")] = (None, chain)
        return list(merged.values())

    def examples_of(self, media, ctx):
        out = []
        if not isinstance(media, dict):
            return out
        if "example" in media:
            out.append(("example", "", media["example"], None))
        for name, ex in (media.get("examples") or {}).items():
            res, chain, sib = self.deref(ex, "examples", ctx)
            if res is None:
                out.append((name, "", None, chain[-1] if chain else "unresolved"))
                continue
            summ = sib.get("summary") or (res.get("summary") if isinstance(res, dict) else "") or ""
            if isinstance(res, dict) and "value" in res:
                out.append((name, summ, res["value"], chain[-1] if chain else None))
            elif isinstance(res, dict) and "externalValue" in res:
                out.append((name, summ, None, f"externalValue {res['externalValue']}"))
            else:
                out.append((name, summ, None, "example object without a value"))
        return out

    def error_codes(self, op, ctx):
        """(status, code, message) found in concrete response examples of this operation."""
        found = []

        def walk(n, status, depth=0):
            if depth > 14:
                return
            if isinstance(n, dict):
                for key in ("code", "error_code"):
                    c = n.get(key)
                    if isinstance(c, str) and CODE_RX.match(c):
                        found.append((status, c, str(n.get("message") or n.get("description") or "")))
                for v in n.values():
                    walk(v, status, depth + 1)
            elif isinstance(n, list):
                for v in n:
                    walk(v, status, depth + 1)

        for st, r in (op.get("responses") or {}).items():
            res, _, _ = self.deref(r, "responses", ctx)
            if not isinstance(res, dict):
                continue
            for media in (res.get("content") or {}).values():
                for _, _, val, _ in self.examples_of(media, ctx):
                    if val is not None:
                        walk(val, str(st))
        seen, out = set(), []
        for t in found:
            if (t[0], t[1]) not in seen:
                seen.add((t[0], t[1])); out.append(t)
        return out

    def security_names(self, op):
        sec = op.get("security", self.doc.get("security"))
        if sec is None:
            return None
        return [", ".join(req.keys()) if req else "(none: anonymous allowed)" for req in sec]


def fields_table(rows):
    if not rows:
        return "_No fields declared in the schema._"
    out = ["| Field | Type | Required | Description | Constraints |", "| --- | --- | --- | --- | --- |"]
    for r in rows:
        out.append(f"| `{r['field']}` | {cell(r['type'])} | {r['required']} | {cell(r['description'])} | {cell(r['constraints'])} |")
    return "\n".join(out)


def render_example(name, summ, val, ptr):
    head = f"Example `{name}`" + (f" ({summ})" if summ else "") + (f" — from `{ptr}`" if ptr and val is not None else "")
    if val is None:
        return f"{head}: **not rendered** — {ptr} (no concrete value in the source)."
    if isinstance(val, (dict, list)):
        body = json.dumps(val, indent=2, ensure_ascii=False, default=str)
        return f"{head}:\n\n```json\n{body}\n```"
    return f"{head}:\n\n```text\n{val}\n```"


def render_operation(spec, path, method, op, item, ctx_extra):
    """Markdown for one operation. ctx_extra: events, catalogue row, guide KU ids, lifecycle notes. Returns (md, named_schemas, facts)."""
    ctx = f"{spec.rel} {method.upper()} {path}"
    named = []
    opid = op.get("operationId", "")
    L = [f"<!-- op: spec={spec.rel} method={method.upper()} path={path} operationId={opid} -->",
         f"### `{method.upper()} {path}` — {op.get('summary', '')}", "",
         f"- **operationId:** `{opid}`" if opid else "- **operationId:** not declared in the source",
         f"- **Specification:** `{spec.rel}` ({spec.title})",
         f"- **Server base URL(s):** " + (", ".join(f"`{u}`" for u in spec.servers) if spec.servers else "not declared")]
    if op.get("tags"):
        L.append("- **Tags:** " + ", ".join(f"`{t}`" for t in op["tags"]))
    L.append("- **Deprecated in specification:** " + ("**yes**" if op.get("deprecated") else "no"))
    sec = spec.security_names(op)
    L.append("- **Security requirement:** " + ("not declared" if sec is None else " OR ".join(f"`{s}`" for s in sec)))
    for note in ctx_extra.get("lifecycle", []):
        L.append(f"- **Lifecycle note:** {note}")
    if op.get("description"):
        L += ["", "**Description (from the specification):**", "", quote_block(op["description"])]
    # parameters
    params = spec.params(item, op, ctx)
    if params:
        L += ["", "#### Parameters", "", "| Name | In | Required | Type | Description | Constraints |", "| --- | --- | --- | --- | --- | --- |"]
        for res, chain in params:
            if res is None:
                L.append(f"| unresolved `{chain[-1] if chain else ''}` | ? | ? | ? | | |")
                continue
            sch = res.get("schema") or {}
            cons = spec.constraints(sch, ctx) if sch else ""
            if "example" in res:
                cons = (cons + "; " if cons else "") + f"example: {jdump(res['example'])}"
            if res.get("deprecated"):
                cons = (cons + "; " if cons else "") + "deprecated: true"
            L.append(f"| `{res.get('name')}` | {res.get('in')} | {'yes' if res.get('required') else 'no'} | "
                     f"{cell(spec.type_label(sch, ctx) if sch else '')} | {cell(res.get('description', ''))} | {cell(cons)} |")
    # request body
    rb = op.get("requestBody")
    if rb is not None:
        res, chain, _ = spec.deref(rb, "requestBodies", ctx)
        L += ["", "#### Request body", ""]
        if res is None:
            L.append(f"Request body reference `{chain[-1] if chain else ''}` could not be resolved.")
        else:
            L.append(f"Required: {'yes' if res.get('required') else 'no'}" + (f" (from `{chain[-1]}`)" if chain else ""))
            if res.get("description"):
                L += ["", quote_block(res["description"])]
            for mt, media in (res.get("content") or {}).items():
                sch = (media or {}).get("schema")
                L += ["", f"**Content type `{mt}`** — schema: {cell(spec.type_label(sch, ctx)) if sch else 'not declared'}", ""]
                if sch:
                    sres, sch_chain, _ = spec.deref(sch, "schemas", ctx)
                    if isinstance(sres, dict) and (sres.get("oneOf") or sres.get("anyOf")) and not sres.get("properties"):
                        for comb in ("oneOf", "anyOf"):
                            for k, opt in enumerate(sres.get(comb) or [], 1):
                                ores, och, _ = spec.deref(opt, "schemas", ctx)
                                lbl = f"schema `{spec.ref_name(och[-1])}`" if och else "inline schema"
                                L += [f"_{comb} option {k}: {lbl}_", "", fields_table(spec.field_rows(opt, ctx, named)), ""]
                    else:
                        L.append(fields_table(spec.field_rows(sch, ctx, named)))
                exs = spec.examples_of(media, ctx)
                for name, summ, val, ptr in exs:
                    L += ["", render_example(name, summ, val, ptr)]
    # responses
    resps = op.get("responses") or {}
    if resps:
        L += ["", "#### Responses", "", "| Status | Description | Body |", "| --- | --- | --- |"]
        details = []
        for st, r in resps.items():
            res, chain, _ = spec.deref(r, "responses", ctx)
            if res is None:
                L.append(f"| {st} | unresolved `{chain[-1] if chain else ''}` | |")
                continue
            bodies = []
            for mt, media in (res.get("content") or {}).items():
                sch = (media or {}).get("schema")
                bodies.append(f"`{mt}`: " + (spec.type_label(sch, ctx) if sch else "no schema"))
            L.append(f"| {st} | {cell(res.get('description', ''))} | {cell('; '.join(bodies))} |")
            sub = []
            for hn, h in (res.get("headers") or {}).items():
                hres, _, _ = spec.deref(h, "headers", ctx)
                if isinstance(hres, dict):
                    sub.append(f"- Response header `{hn}`: {cell(hres.get('description', ''))} ({cell(spec.type_label(hres.get('schema') or {}, ctx))})")
            for mt, media in (res.get("content") or {}).items():
                sch = (media or {}).get("schema")
                if sch and str(st).startswith("2"):
                    sub += [f"**{st} `{mt}` body fields:**", "", fields_table(spec.field_rows(sch, ctx, named)), ""]
                elif sch:
                    sres, sch_chain, _ = spec.deref(sch, "schemas", ctx)
                    if sch_chain:
                        named.append(sch_chain[-1])
                    elif isinstance(sres, dict):
                        for comb in ("oneOf", "anyOf", "allOf"):
                            for opt in sres.get(comb) or []:
                                _, och, _ = spec.deref(opt, "schemas", ctx)
                                if och:
                                    named.append(och[-1])
                for name, summ, val, ptr in spec.examples_of(media, ctx):
                    sub += [f"{st} " + render_example(name, summ, val, ptr), ""]
            if sub:
                details += [f"##### Response {st}", ""] + sub
        L += [""] + details
    codes = spec.error_codes(op, ctx)
    if codes:
        L += ["", "#### Error codes shown in this operation's response examples", "", "| HTTP status | Code | Message |", "| --- | --- | --- |"]
        L += [f"| {s} | `{c}` | {cell(m)} |" for s, c, m in codes]
    ev = ctx_extra.get("events") or []
    if ev:
        L += ["", "#### Events emitted (api-reference-data/endpoint_event_map.csv)", "", "| Event slug | Event page |", "| --- | --- |"]
        L += [f"| `{e['event_slug']}` | {e['event_url']} |" for e in ev]
    cat = ctx_extra.get("catalogue")
    if cat:
        L += ["", f"Catalogue row (api-reference-data/operations_catalog.csv): response codes `{cat['response_codes']}`, "
                  f"has examples `{cat['has_examples']}`, emits events `{cat['emits_events']}`, deprecated `{cat['deprecated']}`."]
    guides = ctx_extra.get("guides") or []
    if guides:
        L += ["", "Guides that link to this operation: " + ", ".join(f"`{g}`" for g in guides) + "."]
    facts = {"opid": opid, "method": method.upper(), "path": path, "codes": codes, "security": sec}
    return "\n".join(L), named, facts


def render_named_schemas(spec, names, ctx):
    """Render each referenced named schema once, following nested named references transitively."""
    out, done, queue = [], set(), list(dict.fromkeys(names))
    while queue:
        ptr = queue.pop(0)
        if ptr in done:
            continue
        done.add(ptr)
        res = spec.pointer(ptr)
        if res is None:
            out += [f"### Schema `{spec.ref_name(ptr)}`", "", f"Unresolved reference `{ptr}`.", ""]
            continue
        more = []
        rows = spec.field_rows({"$ref": ptr}, ctx, more)
        _, _, notes = spec.collect_props({"$ref": ptr}, ctx)
        out += [f"<!-- schema: {ptr} -->", f"### Schema `{spec.ref_name(ptr)}`", "", f"Pointer: `{ptr}`. Type: {cell(spec.type_label({'$ref': ptr}, ctx))}."]
        if isinstance(res, dict) and res.get("description"):
            out += ["", quote_block(res["description"])]
        if notes:
            out += ["", "Composition: " + "; ".join(notes) + "."]
        if isinstance(res, dict):
            for comb in ("oneOf", "anyOf"):
                if res.get(comb):
                    labels = []
                    for opt in res[comb]:
                        ores, och, _ = spec.deref(opt, "schemas", ctx)
                        labels.append(f"`{spec.ref_name(och[-1])}`" if och else "inline schema")
                        if och and Spec._is_structured(ores):
                            more.append(och[-1])
                    out += ["", f"{comb}: " + ", ".join(labels)]
            enum = res.get("enum")
            if enum is not None:
                out += ["", f"Enum: {cell(jdump(enum))}"]
        if rows:
            out += ["", fields_table(rows)]
        out.append("")
        queue += [m for m in more if m not in done]
    return "\n".join(out), sorted(done)
