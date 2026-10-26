// Plain-language explanations for the verification warnings built in pismo_assistant/pipeline.py (Assistant.answer).
// Only those exact prefixes are explained; any other warning is shown as-is, without an invented meaning.

export interface ExplainedWarning {
  /** Plain-language explanation, or null for an unrecognised warning. */
  summary: string | null
  /** The warning exactly as the backend stored it, for diagnostics. */
  raw: string
}

const KNOWN: [prefix: string, summary: string][] = [
  ['answer cites labels that were not supplied', 'The answer refers to evidence labels that were not given to the model. Those labels are not linked to sources.'],
  ['cited evidence lacks source metadata', 'Some cited evidence is missing source details (knowledge unit, title, or source path and link).'],
  ['API details not found in the passages cited by the same claim', 'A sentence mentions API details (such as a path, field or code) that were not found in the passages it cites.'],
  ['claims with API details but no citation', 'A sentence mentions an API detail (such as an error code, path or field) without citing a source.'],
  ['answer does not name the operation the question identified', 'The answer does not name the API operation the question referred to.'],
  ['requirement stated for several operations but not documented for each', 'A sentence states a requirement (such as a header or field) for several API operations, but the cited documentation shows it for only some of them.'],
  ['claims cite documentation of another integration than the question asks about', 'A statement cites documentation of a different integration than the one the question asks about (for example, data-platform event delivery instead of client webhooks).'],
  ['claims supported only by historical changelog passages are not marked as historical', 'A statement relies only on historical changelog entries but is not described as historical or changed.'],
  ['answer contains no inline citations', 'The answer contains no inline citations.'],
]

/** True for entries that carry no information: empty, whitespace, dashes, or an empty list/str representation. */
function isBlank(w: string): boolean {
  return /^[\s\-–—_.[\]'"(){}]*$/.test(w) || /^(none|null|undefined)$/i.test(w.trim())
}

export function explainWarnings(warnings: unknown): ExplainedWarning[] {
  if (!Array.isArray(warnings)) return []
  return warnings
    .filter((w): w is string => typeof w === 'string' && !isBlank(w))
    .map(raw => {
      const hit = KNOWN.find(([prefix]) => raw.trim().startsWith(prefix))
      return { summary: hit ? hit[1] : null, raw: raw.trim() }
    })
}
