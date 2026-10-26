// Evidence markers ([E1], [E1][E2], ...) are not shown in answer prose: each answer's Sources section lists its
// citations. Renders through the app's own Markdown configuration (src/markdownConfig.ts). Run with `npm test`.
import assert from 'node:assert/strict'
import { describe, it } from 'node:test'
import { createElement } from 'react'
import { renderToStaticMarkup } from 'react-dom/server'
import ReactMarkdown from 'react-markdown'
import type { Citation } from '../src/api.ts'
import { citationNumbers, draftDisplay, withoutMarkers } from '../src/citations.ts'
import { rehypePlugins, remarkPlugins } from '../src/markdownConfig.ts'
import { sourceList } from '../src/sourceList.ts'
import { plain, sourceLabels } from '../src/sources.ts'

const cite = (label: string, title: string): Citation =>
  ({ label, ku_id: `KU-${label}`, title, section: 'Section', chunk_id: `KU-${label}::p01`, origin: 'retrieved', sources: [] })

/** Renders an answer exactly as AssistantMessage does; returns the HTML and its visible text. */
function render(markdown: string) {
  const html = renderToStaticMarkup(createElement(ReactMarkdown, { remarkPlugins, rehypePlugins }, markdown))
  const text = html.replace(/<[^>]+>/g, '').replace(/&quot;/g, '"').replace(/&#x27;/g, "'").replace(/&lt;/g, '<')
    .replace(/&gt;/g, '>').replace(/&amp;/g, '&')
  return { html, text }
}

const WEAM = 'WEAM0029 was an error code used when earmark payments with back value dates were rejected; back-dated earmark payments are supported by default [E1][E2].'

describe('answer prose shows no citation markers', () => {
  it('reported case: "... supported by default [E1][E2]." reads "... supported by default."', () => {
    const { text, html } = render(WEAM)
    assert.equal(text, WEAM.replace(' [E1][E2]', ''))
    assert.ok(!/\[\d\]|\[E\d|<cite|chip/.test(html), html)
  })

  it('every marker form disappears together with the space before it', () => {
    for (const md of ['Claim [E1].', 'Claim [E1][E2].', 'Claim [E1, E3].', 'Claim [E1; E2].', 'Claim [ E1 ].', 'Claim [E1 E2].',
      'Claim [E1E2].', 'Claim [E1] [E2].', 'Claim [E7].']) {
      assert.equal(render(md).text, 'Claim.', md)
    }
    assert.equal(render('One [E1]. Two [E2]. Both [E1, E3], then more.').text, 'One. Two. Both, then more.')
    assert.equal(render('See [E1]below.').text, 'See below.')                    // never glues two words together
  })

  it('numbered steps keep their numbering, including steps separated by code blocks', () => {
    const md = '1. Extract the JWT [E1]\n2. Look up the `kid` [E2]\n\n```json\n{ "a": 1 }\n```\n\n3) Verify the signature [E1].'
    const { html, text } = render(md)
    assert.ok(html.includes('<ol>') && html.includes('<ol start="3">'), html)
    assert.ok(html.includes('<li>Extract the JWT</li>') && html.includes('<li>Look up the <code>kid</code></li>'), html)
    assert.ok(text.includes('Verify the signature.') && !/\[E|\[\d\]/.test(text), text)
  })

  it('inline code and fenced code stay exactly as written', () => {
    const md = 'Use `[E1]` and `items[1]` literally [E2].\n\n```text\nheader: [E3]\nvalues[0] = [1]\n```'
    const { html } = render(md)
    assert.ok(html.includes('<code>[E1]</code>') && html.includes('<code>items[1]</code>'), html)
    assert.ok(html.includes('<pre><code class="language-text">header: [E3]\nvalues[0] = [1]\n</code></pre>'), html)
    assert.ok(html.includes('literally.</p>'), html)
  })

  it('legitimate brackets, links, status codes and identifiers are untouched', () => {
    const md = 'WEAM0029, E1 alone, [Note], [E], array[2], HTTP 400 and [docs](https://developers.pismo.io/x) stay [E1].'
    const { text, html } = render(md)
    assert.equal(text, md.replace('[docs](https://developers.pismo.io/x)', 'docs').replace(' [E1]', ''))
    assert.ok(html.includes('<a href="https://developers.pismo.io/x">docs</a>'), html)
  })

  it('markers in tables, list items and headings are removed; a marker-only paragraph leaves nothing behind', () => {
    const { html, text } = render('## Fields [E1]\n\n| Field | Required |\n| --- | --- |\n| `amount` | yes [E2] |\n\n- item [E3]\n\n[E1][E2]\n\nEnd.')
    assert.ok(!/\[E\d|\[\d\]/.test(text), text)
    assert.ok(html.includes('<h2>Fields</h2>') && html.includes('<td>yes</td>') && html.includes('<li>item</li>'), html)
    assert.ok(!/<p>\s*<\/p>/.test(html), html)
  })

  it('placeholders next to markers stay intact', () => {
    assert.equal(render('Use https://<Production Domain>/v1/certs [E1].').text, 'Use https://<Production Domain>/v1/certs.')
  })
})

describe('the Sources section is unchanged and stays the place to inspect citations', () => {
  it('numbers sources in validated order and opens the right one', () => {
    const cs = [cite('E5', 'Five'), cite('E2', 'Two')]
    const opened: string[] = []
    const numbers = citationNumbers(cs.map(c => c.label))
    const html = renderToStaticMarkup(sourceList({ citations: cs, numbers, selectedLabel: null, onOpen: l => opened.push(l) }) as never)
    assert.ok(html.includes('<span class="vh">[</span>1<span class="vh">] </span>') && html.includes('Five'), html)
    const tree = sourceList({ citations: cs, numbers, selectedLabel: null, onOpen: l => opened.push(l) }) as
      { props: { children: [unknown, { props: { children: { props: { children: { props: { onClick: () => void } } } }[] } }] } }
    tree.props.children[1].props.children.forEach(li => li.props.children.props.onClick())
    assert.deepEqual(opened, ['E5', 'E2'])
  })

  it('source labels show titles without Markdown, keeping identifiers intact', () => {
    const labels = sourceLabels([cite('E1', 'API reference: Banking - Credit receivables — Receivable')].map(c =>
      ({ ...c, section: 'Operation contracts > `POST /v1/credit-rights` — Register receivable' })))
    assert.equal(labels.get('E1')?.text, 'API reference: Banking - Credit receivables — Receivable · POST /v1/credit-rights — Register receivable')
    assert.equal(plain('Fields > **account_id** and `program_id`'), 'Fields > account_id and program_id')
  })
})

describe('copy text and streaming drafts', () => {
  it('copy leaves the markers out, code untouched', () => {
    assert.equal(withoutMarkers(WEAM), WEAM.replace(' [E1][E2]', ''))
    assert.equal(withoutMarkers('Ok [E1, E9]. Code `[E1]`.\n\n```\n[E2]\n```'), 'Ok. Code `[E1]`.\n\n```\n[E2]\n```')
    assert.equal(withoutMarkers('1. Extract the JWT [E1]\n2. Verify [E2]'), '1. Extract the JWT\n2. Verify')
  })

  it('drafts hide complete and half-typed markers, keep identifiers', () => {
    assert.equal(draftDisplay(WEAM), WEAM.replace(' [E1][E2]', ''))
    for (const raw of ['Done [E1E2]', 'Done [E1; E2]', 'Done [ E1 ]', 'Done [E1 E', 'Done [ E']) assert.equal(draftDisplay(raw), 'Done', raw)
    for (const partial of ['supported by default [', 'supported by default [E', 'supported by default [E1',
      'supported by default [E1][E', 'supported by default [E1, E']) {
      assert.equal(draftDisplay(partial), 'supported by default', partial)
    }
    assert.equal(draftDisplay('WEAM0029 and `[E1]` in code [E2]'), 'WEAM0029 and `[E1]` in code')
  })

  it('draft and final answer read the same, without markers', () => {
    const chunks = ['WEAM0029 was ', 'removed [E', '1][E2', '] earlier.']
    let raw = ''
    for (const c of chunks) {
      raw += c
      assert.ok(!/\[E|E\d/.test(draftDisplay(raw).replace('WEAM0029', '')), draftDisplay(raw))
    }
    assert.equal(render(raw).text, 'WEAM0029 was removed earlier.')
  })
})
