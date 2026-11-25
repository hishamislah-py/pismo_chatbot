// Theme selection (src/theme.ts) and the Green & Mint token rules (src/theme.css). Run with `npm test`.
import assert from 'node:assert/strict'
import { readFileSync } from 'node:fs'
import { describe, it } from 'node:test'
import { readStored, resolveTheme, THEME_KEY } from '../src/theme.ts'

const store = (v: string | null) => ({ getItem: (k: string) => (k === THEME_KEY ? v : null) })

describe('theme selection', () => {
  it('follows the operating system when nothing is stored', () => {
    assert.equal(resolveTheme(readStored(store(null)), true), 'light')
    assert.equal(resolveTheme(readStored(store(null)), false), 'dark')
  })

  it('a stored Light or Dark choice wins over the operating system', () => {
    assert.equal(resolveTheme(readStored(store('dark')), true), 'dark')
    assert.equal(resolveTheme(readStored(store('light')), false), 'light')
  })

  it('ignores anything else, including a legacy "system" value, and unavailable storage', () => {
    assert.equal(readStored(store('system')), null)
    assert.equal(readStored(store('blue')), null)
    assert.equal(readStored(undefined), null)
    assert.equal(readStored({ getItem: () => { throw new Error('blocked') } }), null)
  })
})

describe('Green & Mint tokens', () => {
  const css = readFileSync(new URL('../src/theme.css', import.meta.url), 'utf8')
  const block = (selector: string) => {
    const start = css.indexOf(selector)
    return css.slice(start, css.indexOf('}', start))
  }
  const names = (s: string) => new Set([...s.matchAll(/(--ds-[\w-]+)\s*:/g)].map(m => m[1]))

  it('defines every colour token for both themes', () => {
    const dark = names(block(':root, [data-theme="dark"]'))
    const light = names(block('[data-theme="light"]'))
    assert.ok(dark.size > 50)
    assert.deepEqual([...dark].filter(n => !light.has(n)), [])
    assert.deepEqual([...light].filter(n => !dark.has(n)), [])
  })

  it('component styles use tokens, not raw colours or literal font weights', () => {
    const styles = readFileSync(new URL('../src/styles.css', import.meta.url), 'utf8')
    assert.deepEqual(styles.match(/#[0-9a-fA-F]{3,8}\b|rgba?\(/g) ?? [], [])
    assert.deepEqual(styles.match(/font-weight:\s*\d/g) ?? [], [])
  })
})
