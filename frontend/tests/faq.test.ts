// The curated demo FAQ (src/faq.ts). Run with `npm test`.
import assert from 'node:assert/strict'
import { describe, it } from 'node:test'
import { FAQ } from '../src/faq.ts'

describe('demo FAQ', () => {
  it('no longer offers the undocumented PCI card go-live question', () => {
    assert.ok(!FAQ.some(f => /pci|go-live/i.test(f.question)), JSON.stringify(FAQ))
  })

  it('has unique, non-empty questions, each with a topic label', () => {
    assert.ok(FAQ.length > 0)
    assert.equal(new Set(FAQ.map(f => f.question)).size, FAQ.length)
    for (const f of FAQ) assert.ok(f.question.trim().endsWith('?') && f.topic.trim(), JSON.stringify(f))
  })
})
