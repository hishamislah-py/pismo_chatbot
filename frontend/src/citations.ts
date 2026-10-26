// Evidence markers such as [E1], [E2] or [E1, E3] in answer text are not shown to readers: each answer lists its
// validated citations in its Sources section instead (numbered in validated-citation order; see citationNumbers).
// The stored answer text and the citation data are unchanged; only the rendered prose, the copied text and the
// streaming draft leave the markers out.
//
// Only the bracketed marker grammar below is recognised. Code spans, code blocks and link text are separate node types
// and are never touched, and identifiers such as WEAM0029, a bare "E1", [Note], array indexes like items[1], status
// codes and list numbers never match.

interface MdNode {
  type: string
  value?: string
  children?: MdNode[]
}

// The validator's grammar ([E1], [E1, E2], [E1; E2], [ E1 ]) plus forms models sometimes emit anyway: [E1 E2] and the
// concatenated [E1E2]. Only bracketed groups made entirely of E-labels match. The whitespace before a marker goes with
// it, so "default [E1][E2]." reads "default." rather than "default .".
const MARKERS = /\s*\[\s*E\d+(?:\s*[,;]?\s*E\d+)*\s*\](?:\s*\[\s*E\d+(?:\s*[,;]?\s*E\d+)*\s*\])*/g
const SKIP = new Set(['link', 'linkReference', 'code', 'inlineCode', 'html'])

/** Removes markers from one piece of prose. A marker between two words ("see [E1]below") leaves a single space. */
function dropMarkers(prose: string): string {
  return prose.replace(MARKERS, (m, offset: number, s: string) => {
    const before = s[offset - 1], after = s[offset + m.length]
    return before !== undefined && /\w/.test(before) && after !== undefined && /\w/.test(after) ? ' ' : ''
  })
}

const isBlank = (n: MdNode) => n.type === 'text' && !(n.value ?? '').trim()

function walk(node: MdNode): void {
  if (!node.children || SKIP.has(node.type)) return
  for (const child of node.children) {
    if (child.type === 'text' && child.value) child.value = dropMarkers(child.value)
    else walk(child)
  }
  // a paragraph that held nothing but markers would otherwise leave an empty block behind
  node.children = node.children.filter(c => !(c.type === 'paragraph' && (c.children ?? []).every(isBlank)))
}

/** remark plugin: removes evidence markers from the prose of a rendered answer. */
export function remarkHideCitations() {
  return (tree: MdNode) => walk(tree)
}

/** Per-answer display number for each validated citation label, in the order the backend validated them. */
export function citationNumbers(validLabels: readonly string[]): Map<string, number> {
  const out = new Map<string, number>()
  for (const l of validLabels) if (!out.has(l)) out.set(l, out.size + 1)
  return out
}

// fenced blocks and inline code spans are left exactly as written
const CODE = /(```[\s\S]*?(?:```|$)|`[^`\n]*`)/

function outsideCode(text: string, f: (prose: string) => string): string {
  return text.split(CODE).map((part, i) => (i % 2 ? part : f(part))).join('')
}

/** Markdown of an answer without its evidence markers (code left as written), as the reader sees it; used for Copy. */
export function withoutMarkers(markdown: string): string {
  return outsideCode(markdown, dropMarkers)
}

const PARTIAL_MARKER_AT_END = /\s*\[\s*(?:E\d*(?:\s*[,;]?\s*E?\d*)*)?\s*$/

/** Provisional draft text for display while streaming: complete markers and a marker still being typed at the end
 *  are hidden. */
export function draftDisplay(raw: string): string {
  return withoutMarkers(raw).replace(PARTIAL_MARKER_AT_END, '')
}
