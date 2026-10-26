import { useState } from 'react'
import type { SessionOut } from '../api'
import { dayGroup, plural, shortWhen, type DayGroup } from '../util'
import { DotsIcon, PlusIcon, SearchIcon, TrashIcon } from './Icons'

interface Props {
  sessions: SessionOut[]
  loading: boolean
  error: string | null
  activeId: string | null
  menuId: string | null
  deletingId: string | null
  /** Session with a question in flight; it cannot be deleted until the answer is stored. */
  lockedId: string | null
  onMenu: (id: string | null) => void
  onSelect: (id: string) => void
  onNew: () => void
  onDelete: (id: string) => void
  onReload: () => void
}

const GROUPS: DayGroup[] = ['Today', 'Yesterday', 'Earlier']

export function Sidebar({ sessions, loading, error, activeId, menuId, deletingId, lockedId, onMenu, onSelect, onNew, onDelete, onReload }: Props) {
  const [query, setQuery] = useState('')
  const q = query.trim().toLowerCase()
  const now = new Date()
  const visible = sessions.filter(s => !q || (s.title ?? '').toLowerCase().includes(q))
  const groups = GROUPS.map(label => ({ label, items: visible.filter(s => dayGroup(s.updated_at, now) === label) })).filter(g => g.items.length)

  return (
    <aside className="sidebar" aria-label="Sessions">
      <div className="sidebar-top">
        <button className="btn-primary" onClick={onNew}><PlusIcon />New session</button>
        <label className="search">
          <SearchIcon className="icon" />
          <input value={query} onChange={e => setQuery(e.target.value)} placeholder="Search sessions" aria-label="Search sessions" />
        </label>
      </div>
      <div className="session-list">
        <span className="eyebrow">RECENT SESSIONS</span>
        {loading && !sessions.length && <span className="sidebar-note">Loading sessions…</span>}
        {error && (
          <span className="sidebar-note">
            Could not load sessions. {error} <button className="link-btn" onClick={onReload}>Try again</button>
          </span>
        )}
        {!loading && !error && !sessions.length && <span className="sidebar-note">No saved sessions yet. Ask a question to start one.</span>}
        {!!sessions.length && !groups.length && <span className="sidebar-note">No sessions match “{query}”.</span>}
        {groups.map(g => (
          <div key={g.label} className="session-group">
            <span className="session-group-label">{g.label}</span>
            {g.items.map(s => (
              <div key={s.id} className={'session-item' + (s.id === activeId ? ' active' : '')}>
                <button className="session-select" onClick={() => onSelect(s.id)} aria-current={s.id === activeId ? 'true' : undefined}>
                  <span className="session-title">{s.title || 'Untitled session'}</span>
                  <span className="session-meta">{shortWhen(s.updated_at, now)} · {plural(s.message_count, 'message')}</span>
                </button>
                <button
                  className="session-menu-btn"
                  title="Session actions"
                  aria-label={`Actions for ${s.title || 'session'}`}
                  aria-expanded={menuId === s.id}
                  onClick={e => { e.stopPropagation(); onMenu(menuId === s.id ? null : s.id) }}
                >
                  <DotsIcon />
                </button>
                {menuId === s.id && (
                  <div className="session-menu" onClick={e => e.stopPropagation()}>
                    <button
                      className="menu-danger"
                      disabled={deletingId === s.id || lockedId === s.id}
                      title={lockedId === s.id ? 'Wait for the current answer before deleting' : undefined}
                      onClick={() => onDelete(s.id)}
                    >
                      <TrashIcon className="icon" />{deletingId === s.id ? 'Deleting…' : 'Delete'}
                    </button>
                  </div>
                )}
              </div>
            ))}
          </div>
        ))}
      </div>
      <div className="sidebar-foot">Sessions and messages are saved by the backend. Delete removes a session permanently.</div>
    </aside>
  )
}
