import type { Citation } from './api'

/** Last segment of a section path: "Change record (source content, verbatim) > 2 October 2026" -> "2 October 2026". */
/** Plain text for a label: Markdown code ticks and bold markers in KB headings are not shown literally
 *  ("`POST /v1/credit-rights` — Register receivable" -> "POST /v1/credit-rights — Register receivable"). Underscores
 *  are kept: they are part of identifiers such as account_id. */
export function plain(s: string): string {
  return s.replace(/`|\*\*/g, '').replace(/\s+/g, ' ').trim()
}

export function sectionTail(section: string | null | undefined): string {
  const parts = (section ?? '').split(' > ').map(s => s.trim()).filter(Boolean)
  return parts.length ? plain(parts[parts.length - 1].replace(/:$/, '')) : ''
}

/** Passage marker from a chunk id ("KU-X::src-...::p08" -> "passage 8"), or the chunk's last id segment. */
function chunkMarker(chunkId: string): string {
  const tail = chunkId.split('::').pop() ?? chunkId
  const m = /^p0*(\d+)$/.exec(tail)
  return m ? `passage ${m[1]}` : tail
}

export interface SourceLabel {
  /** Title, plus the section when it adds something the title does not already say. May be truncated on screen. */
  text: string
  /** Shown in full: separates citations of one message that would otherwise look identical. */
  marker: string | null
}

export function sourceLabels(citations: Citation[]): Map<string, SourceLabel> {
  const text = new Map<string, string>()
  for (const c of citations) {
    const sec = sectionTail(c.section)
    const title = plain(c.title)
    text.set(c.label, sec && !title.toLowerCase().includes(sec.toLowerCase()) ? `${title} · ${sec}` : title)
  }
  const counts = new Map<string, number>()
  for (const v of text.values()) counts.set(v, (counts.get(v) ?? 0) + 1)
  const out = new Map<string, SourceLabel>()
  for (const c of citations) {
    const t = text.get(c.label)!
    out.set(c.label, { text: t, marker: (counts.get(t) ?? 0) > 1 ? chunkMarker(c.chunk_id) : null })
  }
  return out
}
