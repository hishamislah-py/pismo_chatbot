// The "Sources" block under every assistant answer (no JSX, so the Node tests render exactly what the app renders).
//
// Separation between the parts of a row must exist in the text itself, not only in the CSS layout: copy-paste, text
// extraction, reader views and some screen readers ignore flex gaps, and previously produced "Sources2",
// "1. 1Changelog: 2 October 2026" and "2Changelog: 2 October 2026passage 9". So:
//  - the heading is only "Sources" (the count is not part of it);
//  - the list is a <ul>, so the explicit source number (the same number as the in-text chip) is the only number;
//  - number, label, document title and passage marker are separate elements joined by visually hidden separators,
//    so text-only readings get "[2] Changelog: 2 October 2026 · passage 9".
import { createElement as h, type ReactNode } from 'react'
import type { Citation } from './api.ts'
import { plain, sectionTail, sourceLabels } from './sources.ts'

const hidden = (text: string) => h('span', { className: 'vh' }, text)

/** Removes a leading list number that only repeats the row's own number ("2. Foo" or "[2] Foo" in row 2). Numbers
 *  that are part of the title ("2 October 2026", "3DS", "v2 API", "2. Foo" in row 1) are kept. */
export function stripIndexPrefix(text: string, n: number): string {
  const m = /^\s*(?:\[(\d+)\]|(\d+)[.)])\s+(?=\S)/.exec(text)
  return m && Number(m[1] ?? m[2]) === n ? text.slice(m[0].length) : text
}

export interface SourceRow {
  label: string
  n: number
  /** Most specific readable name: the section when it adds to the title, otherwise the document title. */
  primary: string
  /** The document title, when `primary` is a section of it. */
  document: string | null
  /** Passage reference that separates otherwise identical rows of one answer ("passage 9"). */
  passage: string | null
}

/** One row per validated citation, in the order the backend validated them (the order the chips are numbered in). */
export function sourceRows(citations: Citation[], numbers: Map<string, number>): SourceRow[] {
  const labels = sourceLabels(citations)
  return citations.map((c, i) => {
    const n = numbers.get(c.label) ?? i + 1
    const title = stripIndexPrefix(plain(c.title), n)
    const section = stripIndexPrefix(sectionTail(c.section), n)
    const sectionAdds = !!section && !title.toLowerCase().includes(section.toLowerCase())
    return {
      label: c.label, n,
      primary: sectionAdds ? section : title,
      document: sectionAdds ? title : null,
      passage: labels.get(c.label)?.marker ?? null,
    }
  })
}

interface Props {
  citations: Citation[]
  numbers: Map<string, number>
  selectedLabel: string | null
  onOpen: (label: string) => void
}

export function sourceList({ citations, numbers, selectedLabel, onOpen }: Props): ReactNode {
  if (!citations.length) return null
  const byLabel = new Map(citations.map(c => [c.label, c]))
  return h('section', { className: 'sources', 'aria-label': 'Sources' },
    h('h3', { className: 'block-label' }, 'Sources'),
    h('ul', { className: 'source-list' }, sourceRows(citations, numbers).map(r => {
      const c = byLabel.get(r.label)!
      return h('li', { key: r.label },
        h('button', {
          className: 'source-row' + (selectedLabel === r.label ? ' on' : ''),
          onClick: () => onOpen(r.label),
          'aria-pressed': selectedLabel === r.label,
          title: `Show source details: ${c.title}${c.section ? ` — ${c.section}` : ''} (${c.chunk_id})`,
        },
        h('span', { className: 'src-num' }, hidden('['), String(r.n), hidden('] ')),
        h('span', { className: 'src-text' },
          h('span', { className: 'src-sec' }, r.primary),
          r.document && h('span', { className: 'src-doc' }, hidden(' — '), r.document)),
        r.passage && h('span', { className: 'src-marker' }, hidden(' · '), r.passage)))
    })))
}
