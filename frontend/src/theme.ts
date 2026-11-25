// Colour theme (Green & Mint design system). The UI offers Light and Dark only. Until the user picks one, the theme
// follows the operating system (prefers-color-scheme) and updates live when that setting changes. A pick is stored in
// localStorage["ds-theme"] and wins from then on. index.html applies the same rule before first paint.
import { useEffect, useState } from 'react'

export type Theme = 'light' | 'dark'
export const THEME_KEY = 'ds-theme'

/** The stored choice, or null when there is none (or storage is unavailable / holds something else). */
export function readStored(storage: Pick<Storage, 'getItem'> | undefined): Theme | null {
  try {
    const v = storage?.getItem(THEME_KEY)
    return v === 'light' || v === 'dark' ? v : null
  } catch {
    return null
  }
}

/** The theme to show: the stored choice, otherwise the operating system's. */
export function resolveTheme(stored: Theme | null, systemPrefersLight: boolean): Theme {
  return stored ?? (systemPrefersLight ? 'light' : 'dark')
}

const lightQuery = () => window.matchMedia('(prefers-color-scheme: light)')
const storage = () => {
  try { return window.localStorage } catch { return undefined }
}
const current = (): Theme => resolveTheme(readStored(storage()), lightQuery().matches)

function apply(theme: Theme) {
  const root = document.documentElement
  if (root.getAttribute('data-theme') === theme) return
  root.classList.add('ds-theme-switching')            // swap every component at once
  root.setAttribute('data-theme', theme)
  requestAnimationFrame(() => requestAnimationFrame(() => root.classList.remove('ds-theme-switching')))
}

/** Current theme plus a setter. Follows the OS until the user picks, and picks made in other tabs. */
export function useTheme(): [Theme, (t: Theme) => void] {
  const [theme, setThemeState] = useState<Theme>(current)

  useEffect(() => {
    const sync = () => { const t = current(); apply(t); setThemeState(t) }
    sync()
    const media = lightQuery()
    const onStorage = (e: StorageEvent) => { if (e.key === THEME_KEY) sync() }
    media.addEventListener('change', sync)            // no effect once a choice is stored
    window.addEventListener('storage', onStorage)
    return () => { media.removeEventListener('change', sync); window.removeEventListener('storage', onStorage) }
  }, [])

  const setTheme = (t: Theme) => {
    try { storage()?.setItem(THEME_KEY, t) } catch { /* private mode: applies to this page only */ }
    apply(t)
    setThemeState(t)
  }
  return [theme, setTheme]
}
