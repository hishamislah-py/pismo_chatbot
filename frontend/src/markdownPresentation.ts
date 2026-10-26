// Presentation-only Markdown plugins. None of them adds, removes or reorders answer text.
//
// remarkLiteralHtml: answers often contain documented placeholders such as https://<Production Domain>/v1/certs.
// CommonMark parses `<Production Domain>` as a raw HTML tag, and raw HTML is never rendered here, so the placeholder
// used to vanish ("https:///v1/certs"). Raw HTML is now kept as literal text instead (still never interpreted as HTML).
//
// rehypePresentation (runs after sanitizing, so the classes it adds are the app's own):
//  - a short paragraph that only introduces what follows ("Field constraints and important fields:") gets class
//    md-lead and reads as a sub-heading;
//  - a short lead-in label at the start of a paragraph or list item ("Required headers: ...") is shown in bold;
//  - inline code holding an HTTP method and a path (`POST /payments/v2/cancel`) gets the method styled separately.

interface Node {
  type: string
  value?: string
  tagName?: string
  properties?: Record<string, unknown>
  children?: Node[]
}

// ---------------- remark (mdast) ----------------

const FLOW_PARENTS = new Set(['root', 'blockquote', 'listItem', 'footnoteDefinition'])
const BREAK_TAG = /^<br\s*\/?>$/i

function literal(node: Node, parentType: string): Node {
  const value = node.value ?? ''
  if (BREAK_TAG.test(value.trim())) return { type: 'break' }
  const text = { type: 'text', value }
  return FLOW_PARENTS.has(parentType) ? { type: 'paragraph', children: [text] } : text
}

function mergeTexts(children: Node[]): Node[] {
  const out: Node[] = []
  for (const c of children) {
    const prev = out[out.length - 1]
    if (c.type === 'text' && prev?.type === 'text') out[out.length - 1] = { type: 'text', value: (prev.value ?? '') + (c.value ?? '') }
    else out.push(c)
  }
  return out
}

function keepHtmlAsText(node: Node): void {
  if (!node.children) return
  let changed = false
  node.children = node.children.map(c => {
    if (c.type !== 'html') {
      keepHtmlAsText(c)
      return c
    }
    changed = true
    return literal(c, node.type)
  })
  if (changed) node.children = mergeTexts(node.children)
}

export function remarkLiteralHtml() {
  return (tree: Node) => keepHtmlAsText(tree)
}

// ---------------- rehype (hast) ----------------

const METHOD_PATH = /^(GET|POST|PUT|PATCH|DELETE|HEAD|OPTIONS)\s+(\/\S*)$/
// up to six words starting with a capital letter, then a colon and a space; never a URL scheme ("https: //")
const LEAD_LABEL = /^([A-Z][\w'’()/&+-]*(?: [\w'’()/&+-]+){0,5}):[ \t]+(?=[^\s/]|$)/
const LEAD_MAX = 60
const INTRO_MAX = 80

const el = (tagName: string, className: string, children: Node[]): Node =>
  ({ type: 'element', tagName, properties: { className: [className] }, children })

function addClass(node: Node, cls: string): void {
  const props = (node.properties ??= {})
  const cur = props.className
  props.className = Array.isArray(cur) ? [...cur, cls] : cur ? [String(cur), cls] : [cls]
}

/** A paragraph made only of text that ends with a colon, e.g. "Required request fields:". */
function isIntro(p: Node): boolean {
  const kids = p.children ?? []
  if (!kids.length || kids.some(k => k.type !== 'text')) return false
  const text = kids.map(k => k.value ?? '').join('').trim()
  return text.length <= INTRO_MAX && text.endsWith(':') && !text.slice(0, -1).includes(':')
}

/** Bold the "Label:" that opens a paragraph or list item. */
function boldLeadLabel(container: Node): void {
  const kids = container.children ?? []
  const first = kids[0]
  if (first?.type !== 'text' || !first.value) return
  const m = LEAD_LABEL.exec(first.value)
  if (!m || m[1].length > LEAD_MAX || /https?$/i.test(m[1])) return
  const label = m[0].slice(0, m[1].length + 1)                 // "Required headers:"
  const rest = first.value.slice(label.length)
  container.children = [el('strong', 'md-label', [{ type: 'text', value: label }]), { type: 'text', value: rest }, ...kids.slice(1)]
}

function endpointCode(code: Node): void {
  const kids = code.children ?? []
  if (kids.length !== 1 || kids[0].type !== 'text') return
  const m = METHOD_PATH.exec(kids[0].value ?? '')
  if (!m) return
  addClass(code, 'md-endpoint')
  code.children = [el('span', 'md-method', [{ type: 'text', value: m[1] }]), { type: 'text', value: ' ' + m[2] }]
}

function present(node: Node, parent: Node | null): void {
  if (node.type === 'element') {
    if (node.tagName === 'p') {
      if (isIntro(node)) addClass(node, 'md-lead')
      else boldLeadLabel(node)
    } else if (node.tagName === 'li') boldLeadLabel(node)
    else if (node.tagName === 'code' && parent?.tagName !== 'pre') endpointCode(node)
  }
  for (const c of node.children ?? []) present(c, node)
}

export function rehypePresentation() {
  return (tree: Node) => present(tree, null)
}
