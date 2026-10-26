// Server-sent events from POST /api/sessions/{id}/messages/stream (backend/app/services/conversation.py stream_exchange).
// Pure functions only (no DOM, no fetch), so they can be tested with Node's built-in test runner.
import type { ExchangeOut, MessageOut, RouteInfo } from './api.ts'

export type StreamStage = 'sending' | 'routing' | 'accepted' | 'queued' | 'retrieving' | 'evidence_ready' | 'generating' | 'validating' | 'saving'

export type StreamEvent =
  | { type: 'status'; request_id: string; stage: string; evidence_count?: number; user_message?: MessageOut; route?: RouteInfo }
  | { type: 'delta'; request_id: string; text: string }
  | { type: 'validation'; request_id: string; status: string; citations_valid: boolean | null; citation_count: number; warning_count: number }
  | { type: 'final'; request_id: string; http_status: number; exchange: ExchangeOut }
  | { type: 'error'; request_id: string; code: string; message: string; http_status: number; exchange?: ExchangeOut }

/** Progress of one in-flight question. `draft` is provisional model output: never final, never stored. */
export interface StreamProgress {
  requestId: string | null
  stage: StreamStage
  evidenceCount: number | null
  draft: string
}

export const initialProgress = (): StreamProgress => ({ requestId: null, stage: 'sending', evidenceCount: null, draft: '' })

const STAGES = new Set<StreamStage>(['routing', 'accepted', 'queued', 'retrieving', 'evidence_ready', 'generating', 'validating', 'saving'])

export function stageLabel(p: StreamProgress): string {
  const n = p.evidenceCount
  const passages = n != null ? `${n} ${n === 1 ? 'passage' : 'passages'}` : ''
  switch (p.stage) {
    case 'sending': return 'Sending your question…'
    case 'routing': return 'Understanding your question…'
    case 'accepted': return 'Question received…'
    case 'queued': return 'Waiting for another answer to finish…'
    case 'retrieving': return 'Retrieving evidence from the knowledge base…'
    case 'evidence_ready': return `Evidence ready${passages ? ` (${passages})` : ''} · starting the answer…`
    // evidence_ready and generating arrive together, so the count is repeated here to stay visible
    case 'generating': return passages ? `Generating the answer from ${n} evidence ${n === 1 ? 'passage' : 'passages'}…` : 'Generating the answer…'
    case 'validating': return 'Checking citations against the evidence…'
    case 'saving': return 'Saving the answer…'
  }
}

/** Incremental SSE parser (https://html.spec.whatwg.org/multipage/server-sent-events.html#event-stream-interpretation).
 *  Lines end with \n or \r\n; comment lines (":") are ignored; an event is dispatched at a blank line. An event that is
 *  still incomplete when the stream ends is discarded, as the specification requires. */
export function createSseParser(onEvent: (name: string, data: string) => void) {
  let buf = ''
  let name = ''
  let data: string[] = []
  const line = (raw: string) => {
    const l = raw.endsWith('\r') ? raw.slice(0, -1) : raw
    if (l === '') {
      if (data.length) onEvent(name || 'message', data.join('\n'))
      name = ''
      data = []
      return
    }
    if (l.startsWith(':')) return
    const i = l.indexOf(':')
    const field = i < 0 ? l : l.slice(0, i)
    const value = i < 0 ? '' : l.slice(i + 1).replace(/^ /, '')
    if (field === 'event') name = value
    else if (field === 'data') data.push(value)
  }
  return {
    push(chunk: string) {
      buf += chunk
      let nl
      while ((nl = buf.indexOf('\n')) >= 0) {
        line(buf.slice(0, nl))
        buf = buf.slice(nl + 1)
      }
    },
    end() {
      buf = ''
      name = ''
      data = []
    },
  }
}

const isObj = (v: unknown): v is Record<string, unknown> => typeof v === 'object' && v !== null && !Array.isArray(v)

/** Validates one event; anything malformed returns null and is ignored by the caller. */
export function parseStreamEvent(name: string, data: string): StreamEvent | null {
  let d: unknown
  try {
    d = JSON.parse(data)
  } catch {
    return null
  }
  if (!isObj(d) || typeof d.request_id !== 'string') return null
  switch (name) {
    case 'status':
      return typeof d.stage === 'string' ? ({ type: 'status', ...d } as StreamEvent) : null
    case 'delta':
      return typeof d.text === 'string' ? ({ type: 'delta', ...d } as StreamEvent) : null
    case 'validation':
      return typeof d.status === 'string' ? ({ type: 'validation', ...d } as StreamEvent) : null
    case 'final': {
      const ex = d.exchange
      return isObj(ex) && isObj(ex.user_message) && isObj(ex.assistant_message) ? ({ type: 'final', ...d } as StreamEvent) : null
    }
    case 'error':
      return typeof d.code === 'string' ? ({ type: 'error', message: 'The request failed.', http_status: 0, ...d } as StreamEvent) : null
    default:
      return null
  }
}

/** Applies one event to the progress of the request it belongs to; events of any other request are ignored. */
export function applyStreamEvent(p: StreamProgress, ev: StreamEvent): StreamProgress {
  if (p.requestId !== null && ev.request_id !== p.requestId) return p
  const next = { ...p, requestId: ev.request_id }
  if (ev.type === 'status' && STAGES.has(ev.stage as StreamStage)) {
    next.stage = ev.stage as StreamStage
    if (typeof ev.evidence_count === 'number') next.evidenceCount = ev.evidence_count
  } else if (ev.type === 'delta') {
    next.draft = p.draft + ev.text
  }
  return next
}
