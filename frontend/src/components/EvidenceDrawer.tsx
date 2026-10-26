import type { Citation } from '../api'
import { citationNumbers } from '../citations'
import { safeHref } from '../util'
import { CloseIcon, ExternalIcon } from './Icons'

interface Props {
  citations: Citation[]
  label: string
  onSelect: (label: string) => void
  onClose: () => void
}

/** Shows the citation metadata the API returns for one assistant message. Excerpt text is not exposed by the
 *  backend yet, so it is not shown. */
export function EvidenceDrawer({ citations, label, onSelect, onClose }: Props) {
  const c = citations.find(x => x.label === label)
  const numbers = citationNumbers(citations.map(x => x.label))   // same numbering as the answer's Sources list
  if (!c) return null
  return (
    <>
      <div className="scrim" onClick={onClose} aria-hidden="true" />
      <aside className="drawer" aria-label="Source evidence">
        <div className="drawer-head">
          <div>
            <span className="eyebrow">SOURCE EVIDENCE</span>
            <span className="drawer-head-sub">Details for source {numbers.get(label)}</span>
          </div>
          <button className="icon-btn" onClick={onClose} title="Close (Esc)" aria-label="Close evidence panel"><CloseIcon /></button>
        </div>
        <div className="drawer-tabs" role="tablist">
          {citations.map(x => (
            <button key={x.label} role="tab" aria-selected={x.label === label} className={'drawer-tab' + (x.label === label ? ' on' : '')}
              onClick={() => onSelect(x.label)} aria-label={`Source ${numbers.get(x.label)}: ${x.title}`}>
              {numbers.get(x.label)}
            </button>
          ))}
        </div>
        <div className="drawer-body">
          {c.origin && <span className="tag" title="Why this passage was included">{c.origin}</span>}
          <div className="field">
            <span className="drawer-title">{c.title}</span>
            <span className="field-code">{c.ku_id}</span>
          </div>
          <div className="field">
            <span className="field-label">Section</span>
            <span className="field-value">{c.section || '—'}</span>
          </div>
          <div className="field">
            <span className="field-label">Chunk</span>
            <code className="field-code">{c.chunk_id}</code>
          </div>
          <div className="field">
            <span className="field-label">{c.sources.length === 1 ? 'Source' : 'Sources'}</span>
            {c.sources.length === 0 && <span className="drawer-head-sub">No source reference recorded for this citation.</span>}
            {c.sources.map(s => {
              const href = safeHref(s.url)
              return (
                <div key={s.path + s.url} className="field">
                  <code className="field-code">{s.path}</code>
                  {href
                    ? <a className="source-link" href={href} target="_blank" rel="noopener noreferrer"><ExternalIcon className="icon" /><span>Open source</span></a>
                    : <span className="drawer-head-sub">No usable source URL for this reference.</span>}
                </div>
              )
            })}
          </div>
        </div>
        <div className="drawer-foot">Citations are validated against the evidence supplied to the model. Supporting excerpt text is not available from the API yet.</div>
      </aside>
    </>
  )
}
