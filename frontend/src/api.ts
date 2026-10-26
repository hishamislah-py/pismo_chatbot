// Typed client for the FastAPI backend. Source of truth: backend/app/api/*.py and backend/app/schemas/*.py.
// All paths are relative (/api/...) and reach the backend through the Vite dev proxy.
// Imports use explicit .ts extensions so the pure modules also load under Node's test runner (npm test).
import { createSseParser, parseStreamEvent, type StreamEvent } from './stream.ts'

export type AssistantStatus = 'answered' | 'partial' | 'not_documented' | 'conflicting_sources' | 'no_evidence' | 'error'

export interface SessionOut {
  id: string
  title: string | null
  created_at: string
  updated_at: string
  message_count: number
}

export interface CitationSource {
  path: string
  url: string
}

export interface Citation {
  label: string
  ku_id: string
  title: string
  section: string
  chunk_id: string
  origin?: string | null
  sources: CitationSource[]
}

export interface RouteInfo {
  outcome: 'greeting' | 'social' | 'out_of_scope' | 'clarification' | 'pismo_question' | 'follow_up' | string
  reason: string
  /** "rule" | "classifier" | "fallback" (absent on older messages) */
  source?: string
  classifier_ms?: number
  /** why the classifier fallback was used: timeout | provider_error | invalid_output | unavailable */
  fallback?: string
}

/** Shape written by backend/app/services/conversation.py (_details). Every field may be absent on older rows. */
export interface MessageDetails {
  citations_valid?: boolean | null
  verification?: Record<string, unknown> | null
  warnings?: string[]
  missing_information?: string | null
  model?: string | null
  duration_ms?: number
  error?: { kind: string; message: string }
  /** "greeting" | "social" | "clarification": fixed reply that never searched the knowledge base (no citations). */
  response_kind?: string
  /** Routing decision (backend/app/services/router.py). */
  route?: RouteInfo
  /** Safe per-stage timing metadata (milliseconds); see backend/app/services/conversation.py. */
  timings?: Record<string, number | boolean | null>
  /** Index that served a pipeline answer; absent for greetings, timeouts and older messages. */
  index?: { chunk_set_hash: string | null }
  [key: string]: unknown
}

export interface MessageOut {
  id: string
  session_id: string
  seq: number
  role: 'user' | 'assistant'
  content: string
  status: AssistantStatus | null
  citations: Citation[] | null
  details: MessageDetails | null
  created_at: string
}

export interface ExchangeOut {
  session_id: string
  user_message: MessageOut
  assistant_message: MessageOut
}

export interface Health {
  status: 'ok' | 'degraded'
  app: string
  database: string
  assistant: 'loaded' | 'not_loaded' | 'error'
  /** Index held in memory; chunk_set_hash is null until it is loaded. Optional for older backends. */
  index?: { chunk_set_hash: string | null }
}

/** A request that did not produce a usable response. `status` is 0 for network failures and timeouts. */
export class ApiError extends Error {
  readonly status: number
  readonly code: string
  readonly body: unknown

  constructor(status: number, code: string, message: string, body: unknown = null) {
    super(message)
    this.name = 'ApiError'
    this.status = status
    this.code = code
    this.body = body
  }
}

const DEFAULT_TIMEOUT_MS = 15_000
// Timeout budget (backend/app/core/config.py): the backend answers within ASSISTANT_TIMEOUT_S (default 90 s) - its
// deadline covers lock wait, retrieval and every LLM attempt - or returns 504. 120 s leaves room for persistence and the
// proxy hop, so this only fires if the backend itself is unresponsive. The Vite proxy (130 s) outlasts it.
export const SEND_TIMEOUT_MS = 120_000

/** Turn any of the backend's error bodies into a message:
 *  {detail: {code, message}} (404, 413, 503), {detail: [...]} (FastAPI 422), {detail: "..."} or non-JSON. */
function describeError(status: number, body: unknown): { code: string; message: string } {
  const detail = (body as { detail?: unknown } | null)?.detail
  if (detail && typeof detail === 'object' && !Array.isArray(detail)) {
    const d = detail as { code?: unknown; message?: unknown }
    return { code: String(d.code ?? `http_${status}`), message: String(d.message ?? `Request failed (HTTP ${status})`) }
  }
  if (Array.isArray(detail)) {
    const msgs = detail.map(e => (e as { msg?: unknown })?.msg).filter(Boolean).map(String)
    return { code: 'validation_error', message: msgs.join('; ') || 'The request was not valid.' }
  }
  if (typeof detail === 'string') return { code: `http_${status}`, message: detail }
  return { code: `http_${status}`, message: `Request failed (HTTP ${status})` }
}

async function request(method: string, path: string, body?: unknown, timeoutMs = DEFAULT_TIMEOUT_MS): Promise<{ status: number; data: unknown }> {
  const ctrl = new AbortController()
  const timer = setTimeout(() => ctrl.abort(), timeoutMs)
  let res: Response
  try {
    res = await fetch(path, {
      method,
      headers: body === undefined ? undefined : { 'Content-Type': 'application/json' },
      body: body === undefined ? undefined : JSON.stringify(body),
      signal: ctrl.signal,
    })
  } catch (e) {
    if (ctrl.signal.aborted) throw new ApiError(0, 'timeout', `No response within ${Math.round(timeoutMs / 1000)} s.`)
    throw new ApiError(0, 'network', 'Could not reach the backend. Check that it is running on port 8000.', e)
  } finally {
    clearTimeout(timer)
  }
  if (res.status === 204) return { status: 204, data: null }
  const text = await res.text()
  let data: unknown = null
  try {
    data = text ? JSON.parse(text) : null
  } catch {
    data = text // e.g. an HTML error page from the proxy when the backend is down
  }
  // The dev proxy answers with an empty/plain-text 5xx when the backend is down; the API itself always sends JSON.
  if (res.status >= 500 && (data === null || typeof data === 'string')) {
    throw new ApiError(res.status, 'unreachable', `The backend did not respond normally (HTTP ${res.status}). It may be stopped or restarting.`, data)
  }
  return { status: res.status, data }
}

async function json<T>(method: string, path: string, body?: unknown, timeoutMs?: number): Promise<T> {
  const { status, data } = await request(method, path, body, timeoutMs)
  if (status < 200 || status >= 300) {
    const { code, message } = describeError(status, data)
    throw new ApiError(status, code, message, data)
  }
  return data as T
}

function isExchange(data: unknown): data is ExchangeOut {
  const d = data as Partial<ExchangeOut> | null
  return !!d && typeof d === 'object' && !!d.user_message && !!d.assistant_message
}

/** The stored question + failure record carried by a stream `error` event, if the backend stored one. */
export function storedExchange(e: unknown): ExchangeOut | null {
  const ex = e instanceof ApiError ? (e.body as { exchange?: unknown } | null)?.exchange : undefined
  return isExchange(ex) ? ex : null
}

const INCOMPLETE = 'The connection closed before the answer was complete. Nothing was confirmed; reload the conversation to see what was saved.'

/** POST a question to the streaming endpoint. `onEvent` receives every valid event of this request (progress,
 *  provisional deltas, validation). Resolves only with the `final` event's stored exchange. Rejects with ApiError on a
 *  pre-stream HTTP error (404/409/413/422/5xx, same handling as sendMessage), on an `error` event (body = the event,
 *  including any stored failure record), or with code "incomplete_stream" if the stream ends without a terminal event. */
async function sendMessageStream(sessionId: string, content: string, onEvent: (ev: StreamEvent) => void): Promise<ExchangeOut> {
  const ctrl = new AbortController()
  const timer = setTimeout(() => ctrl.abort(), SEND_TIMEOUT_MS)
  const timeoutError = () => new ApiError(0, 'timeout', `No response within ${SEND_TIMEOUT_MS / 1000} s.`)
  let reader: ReadableStreamDefaultReader<Uint8Array> | undefined
  try {
    let res: Response
    try {
      res = await fetch(`/api/sessions/${encodeURIComponent(sessionId)}/messages/stream`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', Accept: 'text/event-stream' },
        body: JSON.stringify({ content }),
        signal: ctrl.signal,
      })
    } catch (e) {
      if (ctrl.signal.aborted) throw timeoutError()
      throw new ApiError(0, 'network', 'Could not reach the backend. Check that it is running on port 8000.', e)
    }
    if (!res.ok || !(res.headers.get('content-type') ?? '').includes('text/event-stream')) {
      const text = await res.text()
      let data: unknown = text
      try { data = text ? JSON.parse(text) : null } catch { /* plain-text proxy error */ }
      if (res.status >= 500 && (data === null || typeof data === 'string')) {
        throw new ApiError(res.status, 'unreachable', `The backend did not respond normally (HTTP ${res.status}). It may be stopped or restarting.`, data)
      }
      const { code, message } = describeError(res.status, data)
      throw new ApiError(res.status, code, message, data)
    }
    if (!res.body) throw new ApiError(0, 'stream_unsupported', 'This browser cannot read streamed responses.')

    reader = res.body.getReader()
    const decoder = new TextDecoder()
    let requestId: string | null = null
    let terminal: StreamEvent | null = null
    const parser = createSseParser((name, data) => {
      if (terminal) return
      const ev = parseStreamEvent(name, data)
      if (!ev || (requestId !== null && ev.request_id !== requestId)) return     // malformed or foreign: ignored
      requestId = ev.request_id
      onEvent(ev)
      if (ev.type === 'final' || ev.type === 'error') terminal = ev
    })
    try {
      for (;;) {
        const { value, done } = await reader.read()
        if (done) break
        parser.push(decoder.decode(value, { stream: true }))
        if (terminal) break
      }
      if (!terminal) parser.push(decoder.decode())
      parser.end()
    } catch (e) {
      if (ctrl.signal.aborted) throw timeoutError()
      throw new ApiError(0, 'incomplete_stream', INCOMPLETE, e)
    }
    const t = terminal as StreamEvent | null
    if (t?.type === 'final') return t.exchange
    if (t?.type === 'error') throw new ApiError(t.http_status, t.code, t.message, t)
    throw new ApiError(0, 'incomplete_stream', INCOMPLETE)
  } finally {
    clearTimeout(timer)
    reader?.cancel().catch(() => {})
  }
}

export const api = {
  health: () => json<Health>('GET', '/api/health'),

  listSessions: (limit = 100) => json<{ sessions: SessionOut[] }>('GET', `/api/sessions?limit=${limit}`).then(r => r.sessions),
  createSession: () => json<SessionOut>('POST', '/api/sessions', {}),
  deleteSession: (id: string) => json<null>('DELETE', `/api/sessions/${encodeURIComponent(id)}`),

  listMessages: (sessionId: string) =>
    json<{ session_id: string; messages: MessageOut[] }>('GET', `/api/sessions/${encodeURIComponent(sessionId)}/messages`).then(r => r.messages),

  /** POST a question. Generation failures (500/502/503/504) still return an ExchangeOut whose assistant message has
   *  status "error"; those are returned, not thrown. Anything else non-2xx throws ApiError. */
  async sendMessage(sessionId: string, content: string): Promise<ExchangeOut> {
    const { status, data } = await request('POST', `/api/sessions/${encodeURIComponent(sessionId)}/messages`, { content }, SEND_TIMEOUT_MS)
    if (isExchange(data)) return data
    const { code, message } = describeError(status, data)
    throw new ApiError(status, code, message, data)
  },

  sendMessageStream,
}

/** Mirrors MAX_QUESTION_CHARS (backend default 2000). The backend remains the authority and returns 422 beyond its limit. */
export const MAX_QUESTION_CHARS = 2000
