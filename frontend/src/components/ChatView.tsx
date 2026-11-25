import { useEffect, useRef, useState } from 'react'
import { MAX_QUESTION_CHARS, type MessageOut } from '../api'
import { FAQ } from '../faq'
import { draftDisplay } from '../citations'
import { stageLabel, type StreamProgress } from '../stream'
import { AssistantMessage, AvatarMark, ErrorCard } from './AssistantMessage'
import { ArrowOutIcon, ChatIcon, SendIcon } from './Icons'

export interface SendFailure {
  title: string
  message: string
  /** "retry" re-sends the question; "reload" re-reads the session (used after a timeout, when the answer may still land). */
  action: 'retry' | 'reload'
}

interface Props {
  title: string
  meta: string
  messages: MessageOut[]
  loading: boolean
  loadError: string | null
  pendingQuestion: string | null
  /** Live progress of the pending question (stage and provisional draft text), from the streaming endpoint. */
  pendingProgress: StreamProgress | null
  /** True while any question is in flight, in any session (the backend serialises pipeline calls). */
  busy: boolean
  failure: SendFailure | null
  drawer: { messageId: string; label: string } | null
  onSend: (question: string) => void
  /** Asks a frequently asked question in a new session, so it is never read as a follow-up of another conversation. */
  onAskFaq: (question: string) => void
  onCite: (messageId: string, label: string) => void
  onRetryMessage: (assistantIndex: number) => void
  onFailureAction: () => void
  onReload: () => void
}

export function ChatView(p: Props) {
  const scrollRef = useRef<HTMLDivElement>(null)
  // whether the reader is at (or near) the bottom; streamed updates only follow along while they are
  const atEnd = useRef(true)

  const hasContent = !!(p.messages.length || p.pendingQuestion || p.failure)
  const draftLength = p.pendingProgress?.draft.length ?? 0
  const stage = p.pendingProgress?.stage

  // new session shown, or a question just sent: jump to the latest content (the welcome screen starts at the top)
  useEffect(() => {
    const el = scrollRef.current
    if (!el) return
    atEnd.current = true
    requestAnimationFrame(() => { el.scrollTop = hasContent ? el.scrollHeight : 0 })
  }, [hasContent, p.title, p.pendingQuestion])

  // progress, draft text, answers and failures arriving: follow only if the reader has not scrolled away (never on the
  // welcome screen, which starts at the top even when it is taller than the viewport)
  useEffect(() => {
    const el = scrollRef.current
    if (el && hasContent && atEnd.current) requestAnimationFrame(() => { el.scrollTop = el.scrollHeight })
  }, [hasContent, p.messages.length, p.failure, draftLength, stage])

  const onScroll = () => {
    const el = scrollRef.current
    if (el) atEnd.current = el.scrollHeight - el.scrollTop - el.clientHeight < 80
  }

  const showWelcome = !p.loading && !p.loadError && !p.messages.length && !p.pendingQuestion && !p.failure
  const last = p.messages[p.messages.length - 1]

  return (
    <main className="main">
      <div className="chat-scroll" ref={scrollRef} onScroll={onScroll}>
        <div className="chat-col">
          <div className="session-header">
            <span className="eyebrow">CURRENT SESSION</span>
            <span className="session-header-title">{p.title}</span>
            <span className="session-header-meta">{p.meta}</span>
          </div>

          {showWelcome && (
            <div className="welcome">
              <div className="welcome-intro">
                <h1>Hi, I'm Pismo Assist.</h1>
                <p>I'm here to help with your Pismo integration. Ask me about API operations, required fields, authentication, transfers, webhooks, events, and error codes—or choose a frequently asked question below.</p>
              </div>
              <div className="faq">
                <span className="faq-label">Frequently asked questions</span>
                <div className="faq-grid">
                  {FAQ.map(f => (
                    <button key={f.question} className="faq-item" onClick={() => p.onAskFaq(f.question)} disabled={p.busy}>
                      <ChatIcon />
                      <span className="faq-text">
                        <span className="faq-topic">{f.topic}</span>
                        <span className="faq-q">{f.question}</span>
                      </span>
                      <ArrowOutIcon />
                    </button>
                  ))}
                </div>
              </div>
            </div>
          )}

          {p.loading && !p.messages.length && <div className="center-state"><span className="spinner spinner-accent" />Loading conversation…</div>}
          {p.loadError && (
            <ErrorCard title="Could not load this conversation" message={p.loadError} onRetry={p.onReload} retryLabel="Try again" />
          )}

          {p.messages.map((m, i) =>
            m.role === 'user'
              ? <div key={m.id} className="user-msg"><div className="user-bubble">{m.content}</div></div>
              : (
                <AssistantMessage
                  key={m.id}
                  message={m}
                  selectedLabel={p.drawer?.messageId === m.id ? p.drawer.label : null}
                  onCite={label => p.onCite(m.id, label)}
                  onRetry={m === last && m.status === 'error' && !p.busy ? () => p.onRetryMessage(i) : undefined}
                />
              ),
          )}

          {p.pendingQuestion && (
            <>
              {/* optimistic: the saved user message arrives together with the answer */}
              <div className="user-msg"><div className="user-bubble">{p.pendingQuestion}</div></div>
              <div className="asst">
                <AvatarMark />
                <div className="pending">
                  <div className="pending-title" role="status" aria-live="polite">
                    <span className="spinner" />
                    <span>{p.pendingProgress ? stageLabel(p.pendingProgress) : 'Sending your question…'}</span>
                  </div>
                  {!!p.pendingProgress?.draft && (
                    // provisional model output: plain text, visibly marked, replaced by the validated answer when it arrives
                    <div className="draft">
                      <span className="draft-badge">Draft · not yet verified</span>
                      <div className="draft-text" aria-live="off">{draftDisplay(p.pendingProgress.draft)}</div>
                    </div>
                  )}
                </div>
              </div>
            </>
          )}

          {p.failure && (
            <ErrorCard
              title={p.failure.title}
              message={p.failure.message}
              onRetry={p.onFailureAction}
              retryDisabled={p.busy}
              retryLabel={p.failure.action === 'reload' ? 'Reload' : 'Retry'}
            />
          )}
        </div>
      </div>
      <Composer busy={p.busy} onSend={p.onSend} />
    </main>
  )
}

function Composer({ busy, onSend }: { busy: boolean; onSend: (q: string) => void }) {
  const [draft, setDraft] = useState('')
  const text = draft.trim()
  const over = text.length > MAX_QUESTION_CHARS
  const canSend = !!text && !over && !busy

  const submit = () => {
    if (!canSend) return
    onSend(text)
    setDraft('')
  }

  return (
    <div className="composer">
      <div className="composer-inner">
        <div className={'composer-box' + (busy ? ' busy' : '')}>
          <textarea
            value={draft}
            onChange={e => setDraft(e.target.value)}
            onKeyDown={e => {
              if (e.key === 'Enter' && !e.shiftKey && !e.nativeEvent.isComposing) {
                e.preventDefault()
                submit()
              }
            }}
            rows={2}
            placeholder="Ask a question about Pismo APIs, events or errors"
            aria-label="Question"
          />
          <button className={'send-btn' + (busy ? ' busy' : '')} onClick={submit} disabled={!canSend} title="Send" aria-label="Send">
            {busy ? <span className="spinner" /> : <SendIcon />}
          </button>
        </div>
        <div className="composer-hint">
          <span>Enter to send · Shift + Enter for a new line</span>
          {over
            ? <span className="over">{text.length} / {MAX_QUESTION_CHARS} characters — shorten the question</span>
            : <span>Answers come from the approved Pismo knowledge base. Check the cited sources.</span>}
        </div>
      </div>
    </div>
  )
}
