---
ku_id: KU-ERR-codes-wrfo
title: 'Error codes: WRFO'
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
- KU-API-banking-transaction-banking--restricted-funds
- KU-CHG-3-april-2026
- KU-CHG-5-december-2025
- KU-CHG-9-january-2026
error_codes:
- WRFO0001
- WRFO0003
- WRFO0004
- WRFO0005
- WRFO0006
- WRFO0007
- WRFO0008
- WRFO0009
- WRFO0010
- WRFO0011
- WRFO0012
- WRFO0013
- WRFO0014
- WRFO0015
- WRFO0016
- WRFO0017
- WRFO0019
---

# Error codes: WRFO

**KU ID:** `KU-ERR-codes-wrfo` · **Category:** Errors and troubleshooting · **Type:** error-code catalogue (from reference table)

## Purpose and scope

17 error code(s) with prefix(es) WRFO from `api-reference-data/error_code_index.csv`, with the HTTP status, message and the operations whose response examples contain the code. The `operations_sample` column is a sample, not a complete list: the complete set of codes per operation is in the API-reference KUs (section “Error codes shown in this operation's response examples”). Conditions under which a code is returned are documented only where the message or the operation description states them.

## Error codes

| Code | HTTP status | Message | Specification files | Operation count | Operations (sample) |
| --- | --- | --- | --- | --- | --- |
| `WRFO0001` | 400 | Invalid JSON payload received: Error unmarshalling request | Banking_-_Transaction_banking | 3 | PATCH /corporate/v1/restricted-funds/{restrictedFundsId};PATCH /corporate/v2/restricted-funds/{restrictedFundsId};POST /corporate/v1/restricted-funds |
| `WRFO0003` | 429 | Account is locked, please try again later | Banking_-_Transaction_banking | 3 | PATCH /corporate/v1/restricted-funds/{restrictedFundsId};PATCH /corporate/v2/restricted-funds/{restrictedFundsId};POST /corporate/v1/restricted-funds |
| `WRFO0004` | 409 | Restricted funds already exist | Banking_-_Transaction_banking | 1 | POST /corporate/v1/restricted-funds |
| `WRFO0005` | 409 | tracking_id is already in use | Banking_-_Transaction_banking | 3 | PATCH /corporate/v1/restricted-funds/{restrictedFundsId};PATCH /corporate/v2/restricted-funds/{restrictedFundsId};POST /corporate/v1/restricted-funds |
| `WRFO0006` | 400 | Insufficient funds | Banking_-_Transaction_banking | 2 | PATCH /corporate/v2/restricted-funds/{restrictedFundsId};POST /corporate/v1/restricted-funds |
| `WRFO0007` | 404 | Restricted funds not found | Banking_-_Transaction_banking | 2 | GET /corporate/v1/restricted-funds/{restrictedFundsId};PATCH /corporate/v2/restricted-funds/{restrictedFundsId} |
| `WRFO0008` | 400 | Requested amount exceeds the currently held amount | Banking_-_Transaction_banking | 2 | PATCH /corporate/v1/restricted-funds/{restrictedFundsId};PATCH /corporate/v2/restricted-funds/{restrictedFundsId} |
| `WRFO0009` | 400 | The number of decimal places is not compatible with the specified currency | Banking_-_Transaction_banking | 3 | PATCH /corporate/v1/restricted-funds/{restrictedFundsId};PATCH /corporate/v2/restricted-funds/{restrictedFundsId};POST /corporate/v1/restricted-funds |
| `WRFO0010` | 401 | Account not authorized | Banking_-_Transaction_banking | 2 | PATCH /corporate/v2/restricted-funds/{restrictedFundsId};POST /corporate/v1/restricted-funds |
| `WRFO0011` | 400 | Invalid account status | Banking_-_Transaction_banking | 3 | PATCH /corporate/v1/restricted-funds/{restrictedFundsId};PATCH /corporate/v2/restricted-funds/{restrictedFundsId};POST /corporate/v1/restricted-funds |
| `WRFO0012` | 400 | Account has not finished onboarding | Banking_-_Transaction_banking | 1 | POST /corporate/v1/restricted-funds |
| `WRFO0013` | 400 | Invalid account currency code: 999 | Banking_-_Transaction_banking | 1 | POST /corporate/v1/restricted-funds |
| `WRFO0014` | 400 | Invalid restricted funds processing code | Banking_-_Transaction_banking | 1 | POST /corporate/v1/restricted-funds |
| `WRFO0015` | 400 | increase_datetime_limit is only allowed when hold_method is RECURRENT | Banking_-_Transaction_banking | 1 | POST /corporate/v1/restricted-funds |
| `WRFO0016` | 400 | increase_datetime_limit cannot be in the past | Banking_-_Transaction_banking | 1 | POST /corporate/v1/restricted-funds |
| `WRFO0017` | 422 | Cannot increase a restriction with zero held amount | Banking_-_Transaction_banking | 1 | PATCH /corporate/v2/restricted-funds/{restrictedFundsId} |
| `WRFO0019` | 409 | Restricted funds was concurrently modified | Banking_-_Transaction_banking | 2 | PATCH /corporate/v1/restricted-funds/{restrictedFundsId};PATCH /corporate/v2/restricted-funds/{restrictedFundsId} |

## Lifecycle status

Codes in this unit that are mentioned in changelog posts (check the post: it may record that the code was added, changed or removed from some endpoints):

- `WRFO0003`: `KU-CHG-3-april-2026`
- `WRFO0012`: `KU-CHG-5-december-2025`
- `WRFO0013`: `KU-CHG-9-january-2026`
- `WRFO0014`: `KU-CHG-3-april-2026`

## Conflicts, caveats and evidence gaps

- Codes and messages come from response examples in the OpenAPI specifications; the conditions that trigger a code are documented only where the message or the operation description states them.
- The source table recognises only codes made of letters followed by digits; codes with mixed prefixes (for example `WP2P0000`) are not in the table but appear in the API-reference KUs.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-reference-data/error_code_index.csv` | rows with code prefix WRFO | https://github.com/PismoDevEx/pismo-api-specs | `76213ae93e90a725…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-API-banking-transaction-banking--restricted-funds` — API reference: Banking - Transaction banking — Restricted funds
- `KU-CHG-3-april-2026` — Changelog: 3 April 2026
- `KU-CHG-5-december-2025` — Changelog: 5 December 2025
- `KU-CHG-9-january-2026` — Changelog: 9 January 2026
