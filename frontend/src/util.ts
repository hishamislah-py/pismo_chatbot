/** Only absolute http(s) links are followed; anything else is rendered as plain text. */
export function safeHref(url: string | null | undefined): string | null {
  if (!url) return null
  try {
    const u = new URL(url)
    return u.protocol === 'https:' || u.protocol === 'http:' ? u.href : null
  } catch {
    return null
  }
}

export type DayGroup = 'Today' | 'Yesterday' | 'Earlier'

function startOfDay(d: Date): number {
  return new Date(d.getFullYear(), d.getMonth(), d.getDate()).getTime()
}

export function dayGroup(iso: string, now = new Date()): DayGroup {
  const diffDays = Math.round((startOfDay(now) - startOfDay(new Date(iso))) / 86_400_000)
  return diffDays <= 0 ? 'Today' : diffDays === 1 ? 'Yesterday' : 'Earlier'
}

/** "Just now", "14:05", or "12 Oct" depending on age, in the viewer's locale. */
export function shortWhen(iso: string, now = new Date()): string {
  const d = new Date(iso)
  if (now.getTime() - d.getTime() < 60_000) return 'Just now'
  if (dayGroup(iso, now) === 'Earlier') return d.toLocaleDateString(undefined, { day: 'numeric', month: 'short' })
  return d.toLocaleTimeString(undefined, { hour: '2-digit', minute: '2-digit' })
}

/** Readable duration for a measured millisecond value ("850 ms", "12.4 s", "1 min 05 s"); null for anything that is not
 *  a finite positive number, so a missing or invalid measurement is never shown as a time. */
export function formatLatency(ms: unknown): string | null {
  if (typeof ms !== 'number' || !Number.isFinite(ms) || ms <= 0) return null
  if (ms < 1) return '<1 ms'
  if (ms < 999.5) return `${Math.round(ms)} ms`             // thresholds keep rounding from showing "1000 ms" / "60.0 s"
  if (ms < 59_950) return `${(ms / 1000).toFixed(1)} s`
  const s = Math.round(ms / 1000)
  return `${Math.floor(s / 60)} min ${String(s % 60).padStart(2, '0')} s`
}

export function plural(n: number, word: string): string {
  return `${n} ${word}${n === 1 ? '' : 's'}`
}
