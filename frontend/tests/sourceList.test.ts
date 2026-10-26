// The Sources block (src/sourceList.ts), shared by every assistant answer. Its text must read correctly without CSS:
// copy-paste, text extraction and some screen readers see only the text. Run with `npm test`.
import assert from 'node:assert/strict'
import { describe, it } from 'node:test'
import { renderToStaticMarkup } from 'react-dom/server'
import type { Citation } from '../src/api.ts'
import { citationNumbers } from '../src/citations.ts'
import { sourceList, sourceRows, stripIndexPrefix } from '../src/sourceList.ts'

const cite = (label: string, title: string, section: string | null, chunk_id: string): Citation =>
  ({ label, ku_id: chunk_id.split('::')[0], title, section, chunk_id, origin: 'retrieved', sources: [] })

// shapes taken from stored answers: two passages of one changelog, an API reference operation and its response,
// and an implementation guide
const CHANGELOG = [
  cite('E1', 'Changelog: 2 October 2026', 'Change record (source content, verbatim) > 2 October 2026', 'KU-CHG-2-october-2026::src-x::p08'),
  cite('E2', 'Changelog: 2 October 2026', 'Change record (source content, verbatim) > 2 October 2026', 'KU-CHG-2-october-2026::src-x::p09'),
]
const API = [
  cite('E7', 'API reference: Core platform - Payment methods — Payment methods (part 2 of 3)',
    'Operation contracts > `POST /payment-methods/v2/transfers` — Create transfer', 'KU-API-pm::op-post-transfers'),
  cite('E9', 'API reference: Core platform - Payment methods — Payment methods (part 2 of 3)',
    'Operation contracts > `POST /payment-methods/v2/transfers` — Create transfer > Responses > Response 400', 'KU-API-pm::op-post-transfers::resp-400'),
]
const GUIDE = [cite('E1', 'Verifying webhook requests', 'Verifying webhook requests > Retrieving a list of public keys', 'KU-EVT-v::src-v.retrieving')]

function render(citations: Citation[]) {
  const numbers = citationNumbers(citations.map(c => c.label))
  const html = renderToStaticMarkup(sourceList({ citations, numbers, selectedLabel: null, onOpen: () => {} }) as never)
  const rows = [...html.matchAll(/<button[^>]*>([\s\S]*?)<\/button>/g)].map(m => text(m[1]))
  return { html, rows, heading: text(/<h3[^>]*>([\s\S]*?)<\/h3>/.exec(html)![1]) }
}
// what text-only readers get: tags dropped, nothing from the stylesheet
const text = (h: string) => h.replace(/<[^>]+>/g, '').replace(/&amp;/g, '&').replace(/&#x27;/g, "'").replace(/&quot;/g, '"')

describe('Sources heading', () => {
  for (const [name, cs] of [['one source', GUIDE], ['two sources', CHANGELOG], ['API reference', API]] as const) {
    it(`is exactly "Sources" (${name}), never with the count appended`, () => {
      const { heading, html } = render([...cs])
      assert.equal(heading, 'Sources')
      assert.ok(!/Sources\s*\d/.test(text(html)), text(html))
    })
  }
  it('renders nothing when there are no citations', () => {
    assert.equal(sourceList({ citations: [], numbers: new Map(), selectedLabel: null, onOpen: () => {} }), null)
  })
})

describe('source rows', () => {
  it('changelog passages: one number each, title and passage separated (was "1. 1Changelog…", "2Changelog…passage 9")', () => {
    const { rows, html } = render(CHANGELOG)
    assert.deepEqual(rows, ['[1] Changelog: 2 October 2026 · passage 8', '[2] Changelog: 2 October 2026 · passage 9'])
    assert.ok(!html.includes('<ol'), 'a numbered <ol> would add a second number when pasted')
  })

  it('API reference: section first, document title as a separate element', () => {
    const { rows, html } = render(API)
    assert.deepEqual(rows, [
      '[1] POST /payment-methods/v2/transfers — Create transfer — API reference: Core platform - Payment methods — Payment methods (part 2 of 3)',
      '[2] Response 400 — API reference: Core platform - Payment methods — Payment methods (part 2 of 3)',
    ])
    assert.equal((html.match(/class="src-sec"/g) ?? []).length, 2)
    assert.equal((html.match(/class="src-doc"/g) ?? []).length, 2)
  })

  it('guide: section and title readable, no passage marker when rows are distinct', () => {
    assert.deepEqual(render(GUIDE).rows, ['[1] Retrieving a list of public keys — Verifying webhook requests'])
  })

  it('every row shows its number exactly once, in citation order, matching the in-text chip numbers', () => {
    const cs = [...API, ...GUIDE.map(c => ({ ...c, label: 'E3' })), ...CHANGELOG.map(c => ({ ...c, label: c.label === 'E1' ? 'E4' : 'E5' }))]
    const { rows } = render(cs)
    rows.forEach((r, i) => {
      assert.ok(r.startsWith(`[${i + 1}] `), r)
      assert.ok(!new RegExp(`^\\[${i + 1}\\] \\[?${i + 1}\\b`).test(r), r)
    })
    assert.deepEqual(sourceRows(cs, citationNumbers(cs.map(c => c.label))).map(r => r.label), ['E7', 'E9', 'E3', 'E4', 'E5'])
  })

  it('keeps the citation mapping: each row opens its own label', () => {
    const opened: string[] = []
    const cs = API
    const tree = sourceList({ citations: cs, numbers: citationNumbers(cs.map(c => c.label)), selectedLabel: 'E9', onOpen: l => opened.push(l) }) as
      { props: { children: [unknown, { props: { children: { props: { children: { props: { onClick: () => void; className: string } } } }[] } }] } }
    const buttons = tree.props.children[1].props.children.map(li => li.props.children.props)
    buttons.forEach(b => b.onClick())
    assert.deepEqual(opened, ['E7', 'E9'])
    assert.deepEqual(buttons.map(b => b.className), ['source-row', 'source-row on'])
  })
})

describe('duplicate leading numbers', () => {
  it('a leading number that repeats the row number is removed once', () => {
    assert.equal(stripIndexPrefix('2. Changelog', 2), 'Changelog')
    assert.equal(stripIndexPrefix('2) Changelog', 2), 'Changelog')
    assert.equal(stripIndexPrefix('[2] Changelog', 2), 'Changelog')
    const cs = [cite('E1', 'Guide', '1. Create the account', 'KU-G::s1'), cite('E2', '2. Payments overview', null, 'KU-P::s')]
    assert.deepEqual(render(cs).rows, ['[1] Create the account — Guide', '[2] Payments overview'])
  })

  it('legitimate numbers in titles, dates, paths and identifiers are kept', () => {
    assert.equal(stripIndexPrefix('2 October 2026', 2), '2 October 2026')          // a date, not a list number
    assert.equal(stripIndexPrefix('2. Changelog', 1), '2. Changelog')              // not this row's number
    assert.equal(stripIndexPrefix('3DS authentication', 3), '3DS authentication')
    assert.equal(stripIndexPrefix('2.1 Settlement', 2), '2.1 Settlement')
    assert.equal(stripIndexPrefix('1', 1), '1')
    const cs = [cite('E1', 'Changelog: 1 October 2026', 'Change record > 1 October 2026', 'KU-C1::p01'),
      cite('E2', 'API reference: Core platform — Payments (part 2 of 3)', 'Operation contracts > `GET /v2/accounts/{id}` — Get account', 'KU-A::op')]
    assert.deepEqual(render(cs).rows, [
      '[1] Changelog: 1 October 2026',
      '[2] GET /v2/accounts/{id} — Get account — API reference: Core platform — Payments (part 2 of 3)',
    ])
  })
})
