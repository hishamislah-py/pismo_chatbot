---
ku_id: KU-ERR-codes-wcpt
title: 'Error codes: WCPT'
category: errors_and_troubleshooting
ku_type: error_catalogue
lifecycle: current
sources:
- path: api-reference-data/error_code_index.csv
  sha256: 76213ae93e90a725287cb34455be25ec9526ab12b34f02d7707b11a206bbcb35
  url: https://github.com/PismoDevEx/pismo-api-specs
  role: reference_table
  updated_at: '2026-10-13T20:51:51+00:00'
related_kus:
- KU-API-banking-transaction-banking--check-posting
- KU-CHG-3-april-2026
- KU-CHG-4-september-2026
error_codes:
- WCPT0001
- WCPT0002
- WCPT0003
- WCPT0004
- WCPT0005
- WCPT0006
- WCPT0007
- WCPT0008
- WCPT0009
- WCPT0010
- WCPT0011
- WCPT0012
- WCPT0013
- WCPT0014
- WCPT0015
- WCPT0016
- WCPT0017
- WCPT0018
- WCPT0019
---

# Error codes: WCPT

**KU ID:** `KU-ERR-codes-wcpt` · **Category:** Errors and troubleshooting · **Type:** error-code catalogue (from reference table)

## Purpose and scope

19 error code(s) with prefix(es) WCPT from `api-reference-data/error_code_index.csv`, with the HTTP status, message and the operations whose response examples contain the code. The `operations_sample` column is a sample, not a complete list: the complete set of codes per operation is in the API-reference KUs (section “Error codes shown in this operation's response examples”). Conditions under which a code is returned are documented only where the message or the operation description states them.

## Error codes

| Code | HTTP status | Message | Specification files | Operation count | Operations (sample) |
| --- | --- | --- | --- | --- | --- |
| `WCPT0001` | 400 | Invalid JSON payload received: Error unmarshalling request | Banking_-_Transaction_banking | 2 | POST /corporate/v1/checks;POST /corporate/v1/checks/release |
| `WCPT0002` | 400 | settlements.settlement_date cannot surpass current_business_date by more than 30 calendar days when settlements.type is PENDING | Banking_-_Transaction_banking | 4 | GET /corporate/v1/checks/{checkId}/settlement-operations;POST /corporate/v1/checks;POST /corporate/v1/checks/release |
| `WCPT0003` | 404 | Check posting not found | Banking_-_Transaction_banking | 4 | GET /corporate/v1/checks/{checkId};GET /corporate/v1/checks/{checkId}/settlement-operations;POST /corporate/v1/checks/release |
| `WCPT0004` | 400 | Corporate account not found | Banking_-_Transaction_banking | 3 | POST /corporate/v1/checks;POST /corporate/v1/checks/release;POST /corporate/v1/checks/{checkId}/cancel |
| `WCPT0005` | 409 | check_id [...] is already in use | Banking_-_Transaction_banking | 1 | POST /corporate/v1/checks |
| `WCPT0006` | 400 | Cannot post checks on holiday | Banking_-_Transaction_banking | 1 | POST /corporate/v1/checks |
| `WCPT0007` | 400 | Cannot post checks on a weekend | Banking_-_Transaction_banking | 1 | POST /corporate/v1/checks |
| `WCPT0008` | 400 | Invalid business date for the current business day cycle | Banking_-_Transaction_banking | 1 | POST /corporate/v1/checks |
| `WCPT0009` | 400 | Action not permitted on a closed account | Banking_-_Transaction_banking | 1 | POST /corporate/v1/checks |
| `WCPT0010` | 400 | Invalid check processing code | Banking_-_Transaction_banking | 1 | POST /corporate/v1/checks |
| `WCPT0011` | 400 | Check status is invalid for this operation | Banking_-_Transaction_banking | 3 | POST /corporate/v1/checks;POST /corporate/v1/checks/release;POST /corporate/v1/checks/{checkId}/cancel |
| `WCPT0012` | 400 | The account cannot be credited. Credit function is not active | Banking_-_Transaction_banking | 1 | POST /corporate/v1/checks |
| `WCPT0013` | 409 | Tracking ID already exists for another operation | Banking_-_Transaction_banking | 3 | POST /corporate/v1/checks;POST /corporate/v1/checks/release;POST /corporate/v1/checks/{checkId}/cancel |
| `WCPT0014` | 400 | Invalid account currency code: 999 | Banking_-_Transaction_banking | 1 | POST /corporate/v1/checks |
| `WCPT0015` | 400 | No releasable settlements found | Banking_-_Transaction_banking | 1 | POST /corporate/v1/checks/release |
| `WCPT0016` | 400 | The payment date cannot be earlier than the account creation date | Banking_-_Transaction_banking | 1 | POST /corporate/v1/checks |
| `WCPT0017` | 400 | The payment date cannot be earlier than the account migration date | Banking_-_Transaction_banking | 1 | POST /corporate/v1/checks |
| `WCPT0018` | 400 | Account has not finished onboarding | Banking_-_Transaction_banking | 3 | POST /corporate/v1/checks;POST /corporate/v1/checks/release;POST /corporate/v1/checks/{checkId}/cancel |
| `WCPT0019` | 409 | Check posting was concurrently modified | Banking_-_Transaction_banking | 2 | POST /corporate/v1/checks/release;POST /corporate/v1/checks/{checkId}/cancel |

## Lifecycle status

Codes in this unit that are mentioned in changelog posts (check the post: it may record that the code was added, changed or removed from some endpoints):

- `WCPT0014`: `KU-CHG-3-april-2026`
- `WCPT0018`: `KU-CHG-4-september-2026`

## Conflicts, caveats and evidence gaps

- Codes and messages come from response examples in the OpenAPI specifications; the conditions that trigger a code are documented only where the message or the operation description states them.
- The source table recognises only codes made of letters followed by digits; codes with mixed prefixes (for example `WP2P0000`) are not in the table but appear in the API-reference KUs.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-reference-data/error_code_index.csv` | rows with code prefix WCPT | https://github.com/PismoDevEx/pismo-api-specs | `76213ae93e90a725…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-API-banking-transaction-banking--check-posting` — API reference: Banking - Transaction banking — Check posting
- `KU-CHG-3-april-2026` — Changelog: 3 April 2026
- `KU-CHG-4-september-2026` — Changelog: 4 September 2026
