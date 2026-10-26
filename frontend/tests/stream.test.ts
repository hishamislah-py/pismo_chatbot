// Run with `npm test` (Node's built-in test runner; Node >= 22.6 loads .ts files by stripping types).
import assert from 'node:assert/strict'
import { readdirSync, readFileSync, statSync } from 'node:fs'
import { join } from 'node:path'
import { afterEach, describe, it } from 'node:test'
import { api, ApiError, storedExchange } from '../src/api.ts'
import { applyStreamEvent, createSseParser, initialProgress, parseStreamEvent, stageLabel, type StreamEvent } from '../src/stream.ts'

const RID = 'req-1'
const msg = (id: string, role: 'user' | 'assistant', content: string, extra: Record<string, unknown> = {}) =>
  ({ id, session_id: 's1', seq: role === 'user' ? 1 : 2, role, content, status: role === 'user' ? null : 'answered', citations: [], details: null, created_at: '2026-10-21T10:00:00Z', ...extra })
const EXCHANGE = { session_id: 's1', user_message: msg('u1', 'user', 'How do I verify webhooks?'), assistant_message: msg('a1', 'assistant', 'Verified answer [E1].') }
const sse = (event: string, data: Record<string, unknown>, id = 1) => `id: ${id}\nevent: ${event}\ndata: ${JSON.stringify({ request_id: RID, ...data })}\n\n`

function mockFetch(body: string, init: { status?: number; contentType?: string; chunk?: number } = {}) {
  const enc = new TextEncoder().encode(body)
  const size = init.chunk ?? 5
  const stream = new ReadableStream<Uint8Array>({
    start(c) {
      for (let i = 0; i < enc.length; i += size) c.enqueue(enc.slice(i, i + size))   // splits lines and UTF-8 sequences
      c.close()
    },
  })
  globalThis.fetch = (async () => new Response(stream, {
    status: init.status ?? 200, headers: { 'content-type': init.contentType ?? 'text/event-stream' },
  })) as typeof fetch
}
const realFetch = globalThis.fetch
afterEach(() => { globalThis.fetch = realFetch })

describe('SSE parser', () => {
  it('handles events split across chunks, CRLF, comments and multi-line data', () => {
    const got: [string, string][] = []
    const p = createSseParser((n, d) => got.push([n, d]))
    const text = ': keep-alive\r\n\r\nevent: delta\r\ndata: {"a":\ndata: 1}\r\n\r\nevent: final\ndata: x\n\n'
    for (const ch of text) p.push(ch)
    p.end()
    assert.deepEqual(got, [['delta', '{"a":\n1}'], ['final', 'x']])
  })
  it('discards an incomplete event when the stream ends', () => {
    const got: string[] = []
    const p = createSseParser(n => got.push(n))
    p.push('event: final\ndata: {"request_id":"x"}\n')            // no blank line before EOF
    p.end()
    assert.deepEqual(got, [])
  })
})

describe('event validation and progress', () => {
  it('rejects malformed events', () => {
    assert.equal(parseStreamEvent('delta', '{not json'), null)
    assert.equal(parseStreamEvent('delta', '{"text":"no request id"}'), null)
    assert.equal(parseStreamEvent('final', '{"request_id":"r","exchange":{}}'), null)
    assert.equal(parseStreamEvent('mystery', '{"request_id":"r"}'), null)
  })
  it('shows progress stages, appends deltas in order and ignores other requests', () => {
    const evs = [
      { type: 'status', request_id: RID, stage: 'accepted' }, { type: 'status', request_id: RID, stage: 'retrieving' },
      { type: 'status', request_id: RID, stage: 'evidence_ready', evidence_count: 6 }, { type: 'status', request_id: RID, stage: 'generating' },
      { type: 'delta', request_id: RID, text: 'Each ' }, { type: 'delta', request_id: 'other-request', text: 'WRONG ' },
      { type: 'delta', request_id: RID, text: 'request' }, { type: 'status', request_id: RID, stage: 'not-a-stage' },
    ] as StreamEvent[]
    const seen: string[] = []
    let p = initialProgress()
    for (const ev of evs) { p = applyStreamEvent(p, ev); seen.push(stageLabel(p)) }
    assert.equal(p.draft, 'Each request')
    assert.equal(p.stage, 'generating')
    assert.ok(seen.includes('Evidence ready (6 passages) · starting the answer…'))
    assert.ok(seen.indexOf('Retrieving evidence from the knowledge base…') < seen.indexOf('Generating the answer from 6 evidence passages…'))
    assert.equal(stageLabel({ ...initialProgress(), stage: 'generating' }), 'Generating the answer…')   // count unknown
    const routed = applyStreamEvent(initialProgress(), { type: 'status', request_id: RID, stage: 'routing' } as StreamEvent)
    assert.equal(stageLabel(routed), 'Understanding your question…')                                   // classifier running
  })
})

describe('sendMessageStream', () => {
  it('delivers progress and provisional deltas before resolving with the final, stored answer', async () => {
    mockFetch(sse('status', { stage: 'accepted' }) + sse('status', { stage: 'retrieving' }) + sse('delta', { text: 'Draft ' }) +
      sse('delta', { text: 'text “é”' }) + sse('validation', { status: 'answered', citations_valid: true, citation_count: 1, warning_count: 0 }) +
      sse('final', { http_status: 201, exchange: EXCHANGE }))
    const order: string[] = []
    let progress = initialProgress()
    const ex = await api.sendMessageStream('s1', 'q', ev => { order.push(ev.type); progress = applyStreamEvent(progress, ev) })
    assert.deepEqual(order, ['status', 'status', 'delta', 'delta', 'validation', 'final'])
    assert.equal(progress.draft, 'Draft text “é”')                       // multibyte text split across chunks
    assert.equal(ex.assistant_message.content, 'Verified answer [E1].')   // the final, not the draft
  })

  it('rejects on an error event and keeps the stored failure record', async () => {
    const failed = { ...EXCHANGE, assistant_message: msg('a1', 'assistant', '', { status: 'error' }) }
    mockFetch(sse('delta', { text: 'partial' }) + sse('error', { code: 'malformed_output', message: 'Unusable output.', http_status: 502, exchange: failed }))
    await assert.rejects(api.sendMessageStream('s1', 'q', () => {}), (e: unknown) => {
      assert.ok(e instanceof ApiError && e.code === 'malformed_output' && e.status === 502)
      assert.equal(storedExchange(e)?.assistant_message.content, '')        // the stored record, not the partial draft
      return true
    })
  })

  it('treats a stream that ends without a final event as incomplete, never as an answer', async () => {
    mockFetch(sse('status', { stage: 'generating' }) + sse('delta', { text: 'Looks like an answer' }))
    await assert.rejects(api.sendMessageStream('s1', 'q', () => {}), (e: unknown) =>
      e instanceof ApiError && e.code === 'incomplete_stream' && storedExchange(e) === null)
  })

  it('keeps HTTP errors before the stream (409 busy, 404, 422) as before', async () => {
    mockFetch(JSON.stringify({ detail: { code: 'session_busy', message: 'Still processing.' } }), { status: 409, contentType: 'application/json' })
    await assert.rejects(api.sendMessageStream('s1', 'q', () => {}), (e: unknown) => e instanceof ApiError && e.status === 409 && e.code === 'session_busy')
    mockFetch(JSON.stringify({ detail: [{ msg: 'content must not be blank' }] }), { status: 422, contentType: 'application/json' })
    await assert.rejects(api.sendMessageStream('s1', 'q', () => {}), (e: unknown) => e instanceof ApiError && e.status === 422)
  })

  it('ignores malformed events and events of another request', async () => {
    const foreign = `event: final\ndata: ${JSON.stringify({ request_id: 'someone-else', http_status: 201, exchange: { ...EXCHANGE, assistant_message: msg('x', 'assistant', 'WRONG') } })}\n\n`
    mockFetch(sse('status', { stage: 'accepted' }) + 'event: delta\ndata: {broken\n\n' + foreign + sse('final', { http_status: 201, exchange: EXCHANGE }))
    const ex = await api.sendMessageStream('s1', 'q', () => {})
    assert.equal(ex.assistant_message.content, 'Verified answer [E1].')
  })
})

describe('static latency estimate', () => {
  it('appears nowhere in the frontend source', () => {
    const files: string[] = []
    const walk = (dir: string) => readdirSync(dir).forEach(f => {
      const p = join(dir, f)
      if (statSync(p).isDirectory()) walk(p); else files.push(p)
    })
    walk(join(import.meta.dirname, '..', 'src'))
    files.push(join(import.meta.dirname, '..', 'index.html'))
    for (const f of files) {
      const text = readFileSync(f, 'utf8')
      assert.ok(!/Responses often take|10.20 seconds|few seconds and can take/.test(text), f)
    }
  })
})
