---
ku_id: KU-ERR-codes-wdiv
title: 'Error codes: WDIV'
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
- KU-API-banking-transaction-banking--accounts
- KU-API-banking-transaction-banking--divisions
- KU-CHG-4-april-2025
error_codes:
- WDIV0001
- WDIV0002
- WDIV0005
- WDIV0006
- WDIV0007
- WDIV0008
- WDIV0009
- WDIV0010
- WDIV0011
- WDIV0012
- WDIV0015
- WDIV0016
- WDIV0017
- WDIV0018
- WDIV0019
---

# Error codes: WDIV

**KU ID:** `KU-ERR-codes-wdiv` · **Category:** Errors and troubleshooting · **Type:** error-code catalogue (from reference table)

## Purpose and scope

15 error code(s) with prefix(es) WDIV from `api-reference-data/error_code_index.csv`, with the HTTP status, message and the operations whose response examples contain the code. The `operations_sample` column is a sample, not a complete list: the complete set of codes per operation is in the API-reference KUs (section “Error codes shown in this operation's response examples”). Conditions under which a code is returned are documented only where the message or the operation description states them.

## Error codes

| Code | HTTP status | Message | Specification files | Operation count | Operations (sample) |
| --- | --- | --- | --- | --- | --- |
| `WDIV0001` | 400 | Only hierarchy ID or level ID must be provided but not both | Banking_-_Transaction_banking | 1 | GET /corporate/v2/divisions |
| `WDIV0002` | 404 | Account division not found | Banking_-_Transaction_banking | 5 | GET /corporate/v1/corporate-accounts/{externalAccountId};GET /corporate/v2/divisions/{divisionCode};PATCH /corporate/v1/corporate-accounts/{externalAccountId} |
| `WDIV0005` | 400 | Invalid level | Banking_-_Transaction_banking | 2 | PATCH /corporate/v2/divisions/{divisionCode};POST /corporate/v2/divisions |
| `WDIV0006` | 400 | The parent division informed is at a level lower than or equal to the level | Banking_-_Transaction_banking | 2 | PATCH /corporate/v2/divisions/{divisionCode};POST /corporate/v2/divisions |
| `WDIV0007` | 400 | Parent level division not found for the given hierarchy | Banking_-_Transaction_banking | 2 | PATCH /corporate/v2/divisions/{divisionCode};POST /corporate/v2/divisions |
| `WDIV0008` | 400 | Cannot change Hierarchy ID because division has child divisions | Banking_-_Transaction_banking | 1 | PATCH /corporate/v2/divisions/{divisionCode} |
| `WDIV0009` | 400 | Child level division not found for the given hierarchy | Banking_-_Transaction_banking | 1 | PATCH /corporate/v2/divisions/{divisionCode} |
| `WDIV0010` | 400 | The level informed is at a level lower than or equal to the child divisions | Banking_-_Transaction_banking | 1 | PATCH /corporate/v2/divisions/{divisionCode} |
| `WDIV0011` | 400 | division_code must be a maximum of 36 characters in length | Banking_-_Transaction_banking | 3 | GET /corporate/v2/divisions;PATCH /corporate/v2/divisions/{divisionCode};POST /corporate/v2/divisions |
| `WDIV0012` | 400 | Program with program_id {programId} not found | Banking_-_Transaction_banking | 2 | PATCH /corporate/v2/divisions/{divisionCode};POST /corporate/v2/divisions |
| `WDIV0015` | 400 | Invalid JSON payload received: Error unmarshalling request | Banking_-_Transaction_banking | 2 | PATCH /corporate/v2/divisions/{divisionCode};POST /corporate/v2/divisions |
| `WDIV0016` | 409 | A division with the same code already exists | Banking_-_Transaction_banking | 1 | POST /corporate/v2/divisions |
| `WDIV0017` | 404 | Parent division not found | Banking_-_Transaction_banking | 3 | GET /corporate/v2/divisions/{divisionCode};PATCH /corporate/v2/divisions/{divisionCode};POST /corporate/v2/divisions |
| `WDIV0018` | 400 | Invalid hierarchy | Banking_-_Transaction_banking | 2 | PATCH /corporate/v2/divisions/{divisionCode};POST /corporate/v2/divisions |
| `WDIV0019` | 400 | Administrative division is misconfigured | Banking_-_Transaction_banking | 2 | PATCH /corporate/v2/divisions/{divisionCode};POST /corporate/v2/divisions |

## Lifecycle status

Codes in this unit that are mentioned in changelog posts (check the post: it may record that the code was added, changed or removed from some endpoints):

- `WDIV0018`: `KU-CHG-4-april-2025`

## Conflicts, caveats and evidence gaps

- Codes and messages come from response examples in the OpenAPI specifications; the conditions that trigger a code are documented only where the message or the operation description states them.
- The source table recognises only codes made of letters followed by digits; codes with mixed prefixes (for example `WP2P0000`) are not in the table but appear in the API-reference KUs.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-reference-data/error_code_index.csv` | rows with code prefix WDIV | https://github.com/PismoDevEx/pismo-api-specs | `76213ae93e90a725…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-API-banking-transaction-banking--accounts` — API reference: Banking - Transaction banking — Accounts
- `KU-API-banking-transaction-banking--divisions` — API reference: Banking - Transaction banking — Divisions
- `KU-CHG-4-april-2025` — Changelog: 4 April 2025
