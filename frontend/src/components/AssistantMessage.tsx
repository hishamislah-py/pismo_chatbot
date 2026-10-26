import { useMemo, useState } from 'react'
import type { Citation, MessageOut } from '../api'
import { citationNumbers, withoutMarkers } from '../citations'
import { sourceList } from '../sourceList'
import { formatLatency } from '../util'
import { CopyIcon, RetryIcon, WarnIcon } from './Icons'
import { Markdown } from './Markdown'

// Demo-facing view: the answer status (message.status) and the verification warnings (details.warnings,
// details.verification) are not shown. They are still returned by the API and stored unchanged.

// error kinds written by backend/app/services/conversation.py (HTTP_FOR_ERROR)
const ERROR_TEXT: Record<string, string> = {
  timeout: 'The assistant did not answer in time.',
  configuration: 'The assistant is not configured (for example, the OpenAI API key is missing).',
  api_error: 'The language model request failed.',
  malformed_output: 'The language model returned output that could not be used.',
  internal: 'The assistant failed with an internal error.',
}

export function AvatarMark() {
  return <div className="avatar" aria-hidden="true">PA</div>
}

interface ErrorCardProps {
  title: string
  message: string
  onRetry?: () => void
  retryDisabled?: boolean
  retryLabel?: string
}

export function ErrorCard({ title, message, onRetry, retryDisabled, retryLabel = 'Retry' }: ErrorCardProps) {
  return (
    <div className="asst" role="alert">
      <AvatarMark />
      <div className="err-card">
        <WarnIcon />
        <div className="err-text">
          <span className="err-title">{title}</span>
          <span className="err-msg">{message}</span>
        </div>
        {onRetry && (
          <button className="err-btn" onClick={onRetry} disabled={retryDisabled}><RetryIcon className="icon" />{retryLabel}</button>
        )}
      </div>
    </div>
  )
}

interface Props {
  message: MessageOut
  /** The label currently open in the evidence drawer, when it belongs to this message. */
  selectedLabel: string | null
  onCite: (label: string) => void
  /** Present only when a retry makes sense (latest failed message, nothing pending). */
  onRetry?: () => void
}

export function AssistantMessage({ message, selectedLabel, onCite, onRetry }: Props) {
  const [copied, setCopied] = useState(false)
  const byLabel = useMemo(() => new Map<string, Citation>((message.citations ?? []).map(c => [c.label, c])), [message.citations])
  // internal evidence labels (E1, E2) are shown to readers as per-answer source numbers in the Sources section
  const numbers = useMemo(() => citationNumbers([...byLabel.keys()]), [byLabel])
  const details = message.details ?? {}
  // fixed replies, clarifications and out-of-scope replies never search the knowledge base, so "no evidence cited"
  // would imply a search that did not happen
  const isDirect = ['greeting', 'social', 'clarification', 'out_of_scope'].includes(details.response_kind ?? '')

  if (message.status === 'error') {
    const err = details.error
    const text = (err && ERROR_TEXT[err.kind]) || 'No answer was generated.'
    return <ErrorCard title="The request failed" message={`${text} No answer is shown.${err?.kind ? ` (${err.kind})` : ''}`} onRetry={onRetry} />
  }

  // server-side total for this request (details.timings.total_ms); absent on older messages, so nothing is shown
  const latency = formatLatency(details.timings?.total_ms)

  const copy = async () => {
    try {
      await navigator.clipboard.writeText(withoutMarkers(message.content))
      setCopied(true)
      setTimeout(() => setCopied(false), 1500)
    } catch {
      /* clipboard unavailable (e.g. insecure context); nothing to do */
    }
  }

  return (
    <div className="asst">
      <AvatarMark />
      <div className="asst-body">
        <div className="asst-head">
          <span className="asst-name">Pismo Assist</span>
          {latency && (
            <span className="asst-latency" title="Measured on the server, from receiving the question until the answer was ready to save. Network time is not included.">
              Response time: {latency}
            </span>
          )}
        </div>
        <Markdown content={message.content} />
        {details.missing_information && (
          <div className="note note-missing">
            <span className="note-label">Missing information</span>
            <Markdown content={details.missing_information} />
          </div>
        )}
        {!byLabel.size && !isDirect && <div className="note">No supporting evidence cited · no citations</div>}
        {sourceList({ citations: [...byLabel.values()], numbers, selectedLabel, onOpen: onCite })}
        <div className="answer-foot">
          <button className="ghost-btn" onClick={copy} title="Copy answer (Markdown)"><CopyIcon />{copied ? 'Copied' : 'Copy'}</button>
        </div>
      </div>
    </div>
  )
}
