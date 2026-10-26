// Answer presentation: literal placeholders survive rendering, raw HTML is never interpreted, and the presentation-only
// plugins (src/markdownPresentation.ts) add structure without changing the answer text. Run with `npm test`.
import assert from 'node:assert/strict'
import { describe, it } from 'node:test'
import { createElement } from 'react'
import { renderToStaticMarkup } from 'react-dom/server'
import ReactMarkdown from 'react-markdown'
import { rehypePlugins, remarkPlugins } from '../src/markdownConfig.ts'
import { explainWarnings } from '../src/warnings.ts'

const html = (md: string) => renderToStaticMarkup(createElement(ReactMarkdown, { remarkPlugins, rehypePlugins }, md))
const text = (h: string) => h.replace(/<[^>]+>/g, '').replace(/&lt;/g, '<').replace(/&gt;/g, '>').replace(/&quot;/g, '"')
  .replace(/&#x27;/g, "'").replace(/&amp;/g, '&')

// stored answer of 2026-10-23 (session "What certificate URL should I use to verify Pismo webhooks in production ...")
const CERT = 'Use the production public-keys endpoint: https://<Production Domain>/v1/certs. Replace the placeholder ' +
  '<Production Domain> with the domain for your production environment. [E1]\n\n```shell Public key request\n' +
  'Production: curl -i https://<Production Domain>/v1/certs\n```'

describe('literal placeholders and raw HTML', () => {
  it('keeps <Production Domain> in prose and in code (was rendered as "https:///v1/certs")', () => {
    const h = html(CERT)
    const t = text(h)
    assert.ok(t.includes('https://<Production Domain>/v1/certs.'), t)
    assert.ok(t.includes('Replace the placeholder <Production Domain> with'), t)
    assert.ok(t.includes('curl -i https://<Production Domain>/v1/certs'), t)
    assert.ok(!t.includes('https:///v1/certs'), t)
    assert.ok(h.includes('&lt;Production Domain&gt;') && !h.includes('<production'), h)   // escaped, never an element
  })

  it('raw HTML is shown as text, never rendered; <br> stays a line break', () => {
    const h = html('Header <script>alert(1)</script> and <img src=x onerror=alert(1)> and <jwt>.\n\n<div>block</div>\n\nA<br>B')
    assert.ok(!/<script|<img|<div/i.test(h), h)
    const t = text(h)
    assert.ok(t.includes('<script>alert(1)</script>') && t.includes('<jwt>.') && t.includes('<div>block</div>'), t)
    assert.ok(h.includes('<p>A<br/>\nB</p>'), h)
  })

  it('citation markers next to placeholders are left out, the placeholder stays', () => {
    const h = html('Use https://<Production Domain>/v1/certs [E1].')
    assert.equal(text(h), 'Use https://<Production Domain>/v1/certs.')
  })
})

describe('presentation-only structure', () => {
  it('a short "Label:" paragraph reads as a sub-heading, text unchanged', () => {
    const md = 'Field constraints and important fields:\n- `amount`: numeric, format `float`. [E1]'
    const h = html(md)
    assert.ok(h.includes('<p class="md-lead">Field constraints and important fields:</p>'), h)
  })

  it('a lead-in label is bolded; URLs, long sentences and code-first lines are left alone', () => {
    assert.ok(html('Required headers: `x-tenant` is required.').includes('<strong class="md-label">Required headers:</strong> '))
    assert.ok(html('- Security requirement: `BearerAuth` is required.').includes('<strong class="md-label">Security requirement:</strong>'))
    assert.ok(!html('See https://sandbox.pismolabs.io for details.').includes('md-label'))
    assert.ok(!html('Send it to https: //x').includes('md-label'))
    assert.ok(!html('This is a long sentence with more than six words before: the colon.').includes('md-label'))
    assert.ok(!html('- `amount`: numeric').includes('md-label'))
  })

  it('inline endpoint code styles the method; fenced code and other code are untouched', () => {
    const h = html('Call `POST /payments/v2/cancel` or `x-tenant`.\n\n```\nPOST /payments/v2/cancel\n```')
    assert.ok(h.includes('<code class="md-endpoint"><span class="md-method">POST</span> /payments/v2/cancel</code>'), h)
    assert.ok(h.includes('<code>x-tenant</code>'), h)
    assert.ok(h.includes('<pre><code>POST /payments/v2/cancel\n</code></pre>'), h)
  })

  it('ordered steps split by code blocks keep their numbers', () => {
    const h = html('1) One.\n\n```json\n{}\n```\n\n5) Five.')
    assert.ok(h.includes('<ol start="5">'), h)
  })

  it('rendered text is the answer text: presentation never adds or drops words', () => {
    const md = 'Operation: Create transfer.\n\nRequired request fields:\n\n- Security requirement: `BearerAuth`.'
    assert.equal(text(html(md)).replace(/\s+/g, ' ').trim(), 'Operation: Create transfer. Required request fields: Security requirement: BearerAuth.')
  })
})

describe('verification warnings', () => {
  it('the operation-scope and integration-scope warnings are explained, raw text kept', () => {
    const raw = ["requirement stated for several operations but not documented for each: [{'token': 'x-tenant'}]",
      "claims cite documentation of another integration than the question asks about: [{'line': 'x'}]", 'something new']
    const w = explainWarnings(raw)
    assert.ok(w[0].summary?.startsWith('A sentence states a requirement'))
    assert.ok(w[1].summary?.startsWith('A statement cites documentation of a different integration'))
    assert.equal(w[2].summary, null)
    assert.deepEqual(w.map(x => x.raw), raw)
  })
})
