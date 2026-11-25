import { useCallback, useEffect, useRef, useState } from 'react'
import { api, ApiError, SEND_TIMEOUT_MS, storedExchange, type Health, type MessageOut, type SessionOut } from './api'
import { applyStreamEvent, initialProgress, type StreamProgress } from './stream'
import { ChatView, type SendFailure } from './components/ChatView'
import { EvidenceDrawer } from './components/EvidenceDrawer'
import { PlusIcon, SidebarIcon } from './components/Icons'
import { Sidebar } from './components/Sidebar'
import { useTheme, type Theme } from './theme'
import { plural, shortWhen } from './util'

const errText = (e: unknown) => (e instanceof ApiError ? e.message : 'Unexpected error.')

function failureFor(e: unknown): SendFailure {
  if (e instanceof ApiError && e.code === 'timeout') {
    return {
      title: 'No response yet',
      message: `The backend did not reply within ${SEND_TIMEOUT_MS / 1000} s. The answer may still be saved; reload the conversation to check before asking again.`,
      action: 'reload',
    }
  }
  if (e instanceof ApiError && e.status === 409) {
    // backend per-session guard: another message for this session (e.g. from another tab) is still being answered
    return { title: 'Another question is still being answered', message: `${e.message} Nothing was saved for this question.`, action: 'reload' }
  }
  if (e instanceof ApiError && e.status === 422) return { title: 'The question was not accepted', message: e.message, action: 'retry' }
  if (e instanceof ApiError && e.code === 'incomplete_stream') {
    // the stream ended without a final answer: whatever draft text was shown is not an answer
    return { title: 'The answer did not finish', message: e.message, action: 'reload' }
  }
  if (e instanceof ApiError && (e.code === 'session_deleted' || e.code === 'session_not_found')) {
    return { title: 'This session no longer exists', message: e.message, action: 'reload' }
  }
  return { title: 'The question could not be sent', message: errText(e), action: 'retry' }
}

function HealthBadge({ health, error }: { health: Health | null; error: boolean }) {
  let tone = '', label = 'Checking backend…'
  if (error) [tone, label] = ['bad', 'Backend offline']
  else if (health) {
    if (health.database !== 'ok') [tone, label] = ['bad', 'Database unavailable']
    else if (health.assistant === 'error') [tone, label] = ['bad', 'Assistant failed to load']
    else if (health.assistant === 'not_loaded') [tone, label] = ['warn', 'Assistant loading…']
    else [tone, label] = ['ok', 'Connected']
  }
  return (
    <span className="health" title={label} role="status">
      <span className={`health-dot ${tone}`} /><span className="health-label">{label}</span>
    </span>
  )
}

/** Light / Dark switch. There is no "System" option: the theme follows the OS until one of these is chosen. */
function ThemeToggle() {
  const [theme, setTheme] = useTheme()
  const options: [Theme, string][] = [['light', 'Light'], ['dark', 'Dark']]
  return (
    <div className="theme-toggle" role="group" aria-label="Colour theme">
      {options.map(([value, label]) => (
        <button key={value} type="button" aria-pressed={theme === value} onClick={() => setTheme(value)}>{label}</button>
      ))}
    </div>
  )
}

export default function App() {
  const [sessions, setSessions] = useState<SessionOut[]>([])
  const [sessionsLoading, setSessionsLoading] = useState(true)
  const [sessionsError, setSessionsError] = useState<string | null>(null)

  // null = a new, not-yet-saved session (created on the first send)
  const [activeId, setActiveId] = useState<string | null>(null)
  const activeRef = useRef<string | null>(null)
  const [messages, setMessages] = useState<MessageOut[]>([])
  const [messagesLoading, setMessagesLoading] = useState(false)
  const [messagesError, setMessagesError] = useState<string | null>(null)

  const [pending, setPending] = useState<{ token: number; sessionId: string | null; question: string; progress: StreamProgress } | null>(null)
  const sendSeq = useRef(0)
  const [failure, setFailure] = useState<(SendFailure & { sessionId: string | null; question: string }) | null>(null)
  const [drawer, setDrawer] = useState<{ messageId: string; label: string } | null>(null)
  const [menuId, setMenuId] = useState<string | null>(null)
  const [deletingId, setDeletingId] = useState<string | null>(null)
  const [collapsed, setCollapsed] = useState(() => window.innerWidth < 900)
  const [health, setHealth] = useState<Health | null>(null)
  const [healthError, setHealthError] = useState(false)

  const activate = (id: string | null) => {
    activeRef.current = id
    setActiveId(id)
  }

  const applySessions = useCallback((p: Promise<SessionOut[]>, live: () => boolean = () => true) =>
    p.then(
      list => { if (live()) { setSessions(list); setSessionsError(null) } },
      e => { if (live()) setSessionsError(errText(e)) },
    ).finally(() => { if (live()) setSessionsLoading(false) }), [])

  const loadSessions = useCallback(() => applySessions(api.listSessions()), [applySessions])

  const loadMessages = useCallback(async (id: string) => {
    setMessagesLoading(true)
    setMessagesError(null)
    try {
      const list = await api.listMessages(id)
      if (activeRef.current === id) setMessages(list) // ignore responses for a session the user has left
    } catch (e) {
      if (activeRef.current !== id) return
      if (e instanceof ApiError && e.status === 404) {
        setMessagesError('This session no longer exists. It may have been deleted.')
        setSessions(prev => prev.filter(s => s.id !== id))
      } else setMessagesError(errText(e))
    } finally {
      if (activeRef.current === id) setMessagesLoading(false)
    }
  }, [])

  useEffect(() => {
    let live = true
    void applySessions(api.listSessions(), () => live)
    return () => { live = false }
  }, [applySessions])

  const reloadSessions = () => {
    setSessionsLoading(true)
    setSessionsError(null)
    void loadSessions()
  }

  useEffect(() => {
    let stop = false
    let timer: ReturnType<typeof setTimeout>
    const tick = async () => {
      let next = 60_000
      try {
        const h = await api.health()
        if (stop) return
        setHealth(h)
        setHealthError(false)
        if (h.assistant !== 'loaded' || h.database !== 'ok') next = 5_000 // poll faster while the model loads
      } catch {
        if (stop) return
        setHealthError(true)
        next = 10_000
      }
      timer = setTimeout(tick, next)
    }
    void tick()
    return () => { stop = true; clearTimeout(timer) }
  }, [])

  useEffect(() => {
    const onKey = (e: KeyboardEvent) => {
      if (e.key === 'Escape') { setDrawer(null); setMenuId(null) }
    }
    window.addEventListener('keydown', onKey)
    return () => window.removeEventListener('keydown', onKey)
  }, [])

  const select = (id: string) => {
    setMenuId(null)
    setDrawer(null)
    if (window.innerWidth < 900) setCollapsed(true)
    if (id === activeRef.current) return
    activate(id)
    setMessages([])
    void loadMessages(id)
  }

  const newSession = () => {
    setMenuId(null)
    setDrawer(null)
    if (window.innerWidth < 900) setCollapsed(true)
    activate(null)
    setMessages([])
    setMessagesError(null)
    setMessagesLoading(false)
  }

  const send = async (question: string) => {
    const q = question.trim()
    if (!q || pending) return
    setFailure(null)
    setDrawer(null)
    let sid = activeRef.current
    const token = ++sendSeq.current       // events of this request may only update this request's pending state
    setPending({ token, sessionId: sid, question: q, progress: initialProgress() })
    try {
      if (!sid) {
        const created = await api.createSession()
        sid = created.id
        setSessions(prev => [created, ...prev])
        if (activeRef.current === null) activate(sid) // still on the new-session screen
        setPending(p => (p && p.token === token ? { ...p, sessionId: created.id } : p))
      }
      const ex = await api.sendMessageStream(sid, q, ev =>
        setPending(p => (p && p.token === token ? { ...p, progress: applyStreamEvent(p.progress, ev) } : p)))
      // only the validated, stored answer from the `final` event ever enters the conversation
      if (activeRef.current === sid) setMessages(prev => [...prev, ex.user_message, ex.assistant_message])
    } catch (e) {
      const stored = storedExchange(e)
      if (stored) {
        // generation failed and the backend stored the question with a failure record: show them like history does
        if (activeRef.current === sid) setMessages(prev => [...prev, stored.user_message, stored.assistant_message])
      } else if (activeRef.current === sid) {
        setFailure({ ...failureFor(e), sessionId: sid, question: q })
        // the backend commits the question before generating, so re-read what was actually stored
        if (sid) void loadMessages(sid)
      }
    } finally {
      setPending(p => (p && p.token === token ? null : p))
      void loadSessions()
    }
  }

  const askFaq = (question: string) => {
    if (pending) return
    if (activeRef.current !== null || messages.length) newSession() // a standalone question, never a follow-up
    void send(question)
  }

  const retryMessage = (assistantIndex: number) => {
    const prevUser = messages.slice(0, assistantIndex).reverse().find(m => m.role === 'user')
    if (prevUser) void send(prevUser.content)
  }

  const onFailureAction = () => {
    if (!failure) return
    if (failure.action === 'reload') {
      setFailure(null)
      if (failure.sessionId) void loadMessages(failure.sessionId)
    } else void send(failure.question)
  }

  const remove = async (id: string) => {
    if (!window.confirm('Delete this session and all of its messages? This cannot be undone.')) return
    setDeletingId(id)
    try {
      await api.deleteSession(id)
    } catch (e) {
      if (!(e instanceof ApiError && e.status === 404)) { // already gone counts as deleted
        window.alert(`The session could not be deleted. ${errText(e)}`)
        return
      }
    } finally {
      setDeletingId(null)
      setMenuId(null)
    }
    setSessions(prev => prev.filter(s => s.id !== id))
    if (activeRef.current === id) newSession()
    if (failure?.sessionId === id) setFailure(null)
  }

  const onCite = useCallback((messageId: string, label: string) => {
    setMenuId(null)
    setDrawer(d => (d && d.messageId === messageId && d.label === label ? null : { messageId, label }))
  }, [])

  const active = sessions.find(s => s.id === activeId)
  const title = activeId ? active?.title || 'Untitled session' : 'New session'
  const meta = !activeId
    ? 'Not saved yet · the session is created when you send the first question'
    : messages.length
      ? `${active ? `Updated ${shortWhen(active.updated_at).toLowerCase()} · ` : ''}${plural(messages.length, 'message')}`
      : messagesLoading ? 'Loading…' : 'No messages yet'
  const pendingHere = pending && pending.sessionId === activeId ? pending : null
  const failureHere = failure && failure.sessionId === activeId ? failure : null
  const drawerMsg = drawer ? messages.find(m => m.id === drawer.messageId) : undefined

  return (
    <div className="app" onClick={() => menuId && setMenuId(null)}>
      <header className="topbar">
        <button className="icon-btn-dark" onClick={() => setCollapsed(c => !c)} title="Toggle sidebar" aria-label="Toggle sidebar" aria-expanded={!collapsed}>
          <SidebarIcon className="icon" />
        </button>
        <div className="brand">
          <div className="brand-mark" aria-hidden="true">PA</div>
          <span className="brand-name">Pismo Assist</span>
          <span className="brand-sub">Client implementation &amp; ramp-up assistant</span>
        </div>
        <div className="topbar-end">
          <ThemeToggle />
          <HealthBadge health={health} error={healthError} />
        </div>
      </header>

      <div className="body">
        {collapsed ? (
          <aside className="rail" aria-label="Sessions (collapsed)">
            <button className="btn-primary" onClick={newSession} title="New session" aria-label="New session"><PlusIcon /></button>
          </aside>
        ) : (
          <Sidebar
            sessions={sessions}
            loading={sessionsLoading}
            error={sessionsError}
            activeId={activeId}
            menuId={menuId}
            deletingId={deletingId}
            lockedId={pending?.sessionId ?? null}
            onMenu={setMenuId}
            onSelect={select}
            onNew={newSession}
            onDelete={id => void remove(id)}
            onReload={reloadSessions}
          />
        )}

        <ChatView
          title={title}
          meta={meta}
          messages={messages}
          loading={messagesLoading}
          loadError={messagesError}
          pendingQuestion={pendingHere?.question ?? null}
          pendingProgress={pendingHere?.progress ?? null}
          busy={!!pending}
          failure={failureHere}
          drawer={drawer}
          onSend={q => void send(q)}
          onAskFaq={askFaq}
          onCite={onCite}
          onRetryMessage={retryMessage}
          onFailureAction={onFailureAction}
          onReload={() => activeId && void loadMessages(activeId)}
        />

        {drawer && drawerMsg?.citations && (
          <EvidenceDrawer
            citations={drawerMsg.citations}
            label={drawer.label}
            onSelect={label => setDrawer({ messageId: drawerMsg.id, label })}
            onClose={() => setDrawer(null)}
          />
        )}
      </div>
    </div>
  )
}
