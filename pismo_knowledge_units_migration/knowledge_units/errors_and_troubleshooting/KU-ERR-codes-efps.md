---
ku_id: KU-ERR-codes-efps
title: 'Error codes: EFPS'
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
- KU-API-instant-payments-uk-fps-beta--faster-payments
- KU-CHG-2-july-2026
- KU-CHG-7-august-2026
error_codes:
- EFPS0002
- EFPS0004
- EFPS0006
- EFPS0009
- EFPS0010
- EFPS0011
- EFPS0012
- EFPS0014
- EFPS0015
- EFPS0016
- EFPS0017
- EFPS0018
- EFPS0019
- EFPS0020
- EFPS0021
- EFPS0022
- EFPS0023
- EFPS0024
- EFPS0025
- EFPS0026
- EFPS0027
- EFPS0028
- EFPS0029
- EFPS0030
- EFPS0031
- EFPS0032
- EFPS0033
- EFPS0034
- EFPS0035
- EFPS0036
- EFPS0037
- EFPS0038
- EFPS0039
- EFPS0040
- EFPS0041
- EFPS0046
- EFPS0047
- EFPS0058
- EFPS0067
- EFPS0073
- EFPS0085
- EFPS0086
- EFPS0093
- EFPS0094
- EFPS0095
- EFPS0096
---

# Error codes: EFPS

**KU ID:** `KU-ERR-codes-efps` · **Category:** Errors and troubleshooting · **Type:** error-code catalogue (from reference table)

## Purpose and scope

46 error code(s) with prefix(es) EFPS from `api-reference-data/error_code_index.csv`, with the HTTP status, message and the operations whose response examples contain the code. The `operations_sample` column is a sample, not a complete list: the complete set of codes per operation is in the API-reference KUs (section “Error codes shown in this operation's response examples”). Conditions under which a code is returned are documented only where the message or the operation description states them.

## Error codes

| Code | HTTP status | Message | Specification files | Operation count | Operations (sample) |
| --- | --- | --- | --- | --- | --- |
| `EFPS0002` | 403 | Missing required header: 'x-tenant' | Instant_payments_-_UK_FPS_beta | 6 | GET /v1/payments/fps/{endToEndId};POST /v1/payments/fps/cancel/{endToEndId};POST /v1/payments/fps/cop |
| `EFPS0004` | 400 | Validation error | Instant_payments_-_UK_FPS_beta | 6 | GET /v1/payments/fps/{endToEndId};POST /v1/payments/fps/cancel/{endToEndId};POST /v1/payments/fps/cop |
| `EFPS0006` | 500 | HTTP request error | Instant_payments_-_UK_FPS_beta | 6 | GET /v1/payments/fps/{endToEndId};POST /v1/payments/fps/cancel/{endToEndId};POST /v1/payments/fps/cop |
| `EFPS0009` | 500 | IntlBankAccounts API timeout error | Instant_payments_-_UK_FPS_beta | 4 | GET /v1/payments/fps/{endToEndId};POST /v1/payments/fps/cancel/{endToEndId};POST /v1/payments/fps/out |
| `EFPS0010` | 404 | Sort Code not found | Instant_payments_-_UK_FPS_beta | 4 | GET /v1/payments/fps/{endToEndId};POST /v1/payments/fps/cancel/{endToEndId};POST /v1/payments/fps/out |
| `EFPS0011` | 500 | IntlBankAccounts API Internal Server error | Instant_payments_-_UK_FPS_beta | 4 | GET /v1/payments/fps/{endToEndId};POST /v1/payments/fps/cancel/{endToEndId};POST /v1/payments/fps/out |
| `EFPS0012` | 500;504 | PSPGateway API timeout error | Instant_payments_-_UK_FPS_beta | 6 | GET /v1/payments/fps/{endToEndId};POST /v1/payments/fps/cancel/{endToEndId};POST /v1/payments/fps/cop |
| `EFPS0014` | 502 | PSPGateway API Bad Gateway | Instant_payments_-_UK_FPS_beta | 6 | GET /v1/payments/fps/{endToEndId};POST /v1/payments/fps/cancel/{endToEndId};POST /v1/payments/fps/cop |
| `EFPS0015` | 429 | PSPGateway API Rate Limit exceeded | Instant_payments_-_UK_FPS_beta | 6 | GET /v1/payments/fps/{endToEndId};POST /v1/payments/fps/cancel/{endToEndId};POST /v1/payments/fps/cop |
| `EFPS0016` | 400 | Unmarshal error | Instant_payments_-_UK_FPS_beta | 6 | GET /v1/payments/fps/{endToEndId};POST /v1/payments/fps/cancel/{endToEndId};POST /v1/payments/fps/cop |
| `EFPS0017` | 500 | Accounts API timeout error | Instant_payments_-_UK_FPS_beta | 4 | GET /v1/payments/fps/{endToEndId};POST /v1/payments/fps/cancel/{endToEndId};POST /v1/payments/fps/out |
| `EFPS0018` | 404 | Accounts - Not found | Instant_payments_-_UK_FPS_beta | 4 | GET /v1/payments/fps/{endToEndId};POST /v1/payments/fps/cancel/{endToEndId};POST /v1/payments/fps/out |
| `EFPS0019` | 400 | Accounts - API returned 4xx error | Instant_payments_-_UK_FPS_beta | 4 | GET /v1/payments/fps/{endToEndId};POST /v1/payments/fps/cancel/{endToEndId};POST /v1/payments/fps/out |
| `EFPS0020` | 500 | Accounts - API returned 5xx error | Instant_payments_-_UK_FPS_beta | 4 | GET /v1/payments/fps/{endToEndId};POST /v1/payments/fps/cancel/{endToEndId};POST /v1/payments/fps/out |
| `EFPS0021` | 403 | Account blocked or cancelled | Instant_payments_-_UK_FPS_beta | 4 | GET /v1/payments/fps/{endToEndId};POST /v1/payments/fps/cancel/{endToEndId};POST /v1/payments/fps/out |
| `EFPS0022` | 409 | A transaction with the specified idempotency key and end_to_end_id already exists | Instant_payments_-_UK_FPS_beta | 4 | GET /v1/payments/fps/{endToEndId};POST /v1/payments/fps/cancel/{endToEndId};POST /v1/payments/fps/out |
| `EFPS0023` | 500 | Transaction database error | Instant_payments_-_UK_FPS_beta | 6 | GET /v1/payments/fps/{endToEndId};POST /v1/payments/fps/cancel/{endToEndId};POST /v1/payments/fps/cop |
| `EFPS0024` | 500 | P2p - API timeout error | Instant_payments_-_UK_FPS_beta | 4 | GET /v1/payments/fps/{endToEndId};POST /v1/payments/fps/cancel/{endToEndId};POST /v1/payments/fps/out |
| `EFPS0025` | 400 | P2p - API returned 4xx error | Instant_payments_-_UK_FPS_beta | 4 | GET /v1/payments/fps/{endToEndId};POST /v1/payments/fps/cancel/{endToEndId};POST /v1/payments/fps/out |
| `EFPS0026` | 500 | P2p - API returned 5xx error | Instant_payments_-_UK_FPS_beta | 4 | GET /v1/payments/fps/{endToEndId};POST /v1/payments/fps/cancel/{endToEndId};POST /v1/payments/fps/out |
| `EFPS0027` | 500 | Ledger API timeout error | Instant_payments_-_UK_FPS_beta | 4 | GET /v1/payments/fps/{endToEndId};POST /v1/payments/fps/cancel/{endToEndId};POST /v1/payments/fps/out |
| `EFPS0028` | 404 | Ledger - Not found | Instant_payments_-_UK_FPS_beta | 4 | GET /v1/payments/fps/{endToEndId};POST /v1/payments/fps/cancel/{endToEndId};POST /v1/payments/fps/out |
| `EFPS0029` | 400 | Ledger - API returned 4xx error | Instant_payments_-_UK_FPS_beta | 4 | GET /v1/payments/fps/{endToEndId};POST /v1/payments/fps/cancel/{endToEndId};POST /v1/payments/fps/out |
| `EFPS0030` | 500 | Ledger - API returned 5xx error | Instant_payments_-_UK_FPS_beta | 4 | GET /v1/payments/fps/{endToEndId};POST /v1/payments/fps/cancel/{endToEndId};POST /v1/payments/fps/out |
| `EFPS0031` | 404 | IntlBankAccounts - Not found | Instant_payments_-_UK_FPS_beta | 4 | GET /v1/payments/fps/{endToEndId};POST /v1/payments/fps/cancel/{endToEndId};POST /v1/payments/fps/out |
| `EFPS0032` | 500 | IntlBankAccounts - API returned 5xx error | Instant_payments_-_UK_FPS_beta | 4 | GET /v1/payments/fps/{endToEndId};POST /v1/payments/fps/cancel/{endToEndId};POST /v1/payments/fps/out |
| `EFPS0033` | 403 | Invalid account id header: 'x-account-id' | Instant_payments_-_UK_FPS_beta | 4 | GET /v1/payments/fps/{endToEndId};POST /v1/payments/fps/cancel/{endToEndId};POST /v1/payments/fps/out |
| `EFPS0034` | 403 | Missing required header: 'x-idempotency-key' | Instant_payments_-_UK_FPS_beta | 4 | GET /v1/payments/fps/{endToEndId};POST /v1/payments/fps/cancel/{endToEndId};POST /v1/payments/fps/out |
| `EFPS0035` | 403 | Account has no active addresses | Instant_payments_-_UK_FPS_beta | 4 | GET /v1/payments/fps/{endToEndId};POST /v1/payments/fps/cancel/{endToEndId};POST /v1/payments/fps/out |
| `EFPS0036` | 409 | The provided currency does not match with the account's configured currency | Instant_payments_-_UK_FPS_beta | 4 | GET /v1/payments/fps/{endToEndId};POST /v1/payments/fps/cancel/{endToEndId};POST /v1/payments/fps/out |
| `EFPS0037` | 400 | Invalid creditor sort code/account number | Instant_payments_-_UK_FPS_beta | 4 | GET /v1/payments/fps/{endToEndId};POST /v1/payments/fps/cancel/{endToEndId};POST /v1/payments/fps/out |
| `EFPS0038` | 400 | Invalid creditor IBAN | Instant_payments_-_UK_FPS_beta | 4 | GET /v1/payments/fps/{endToEndId};POST /v1/payments/fps/cancel/{endToEndId};POST /v1/payments/fps/out |
| `EFPS0039` | 400 | Invalid creditor BBAN | Instant_payments_-_UK_FPS_beta | 4 | GET /v1/payments/fps/{endToEndId};POST /v1/payments/fps/cancel/{endToEndId};POST /v1/payments/fps/out |
| `EFPS0040` | 403 | FPS is not enabled for the creditor sort code | Instant_payments_-_UK_FPS_beta | 4 | GET /v1/payments/fps/{endToEndId};POST /v1/payments/fps/cancel/{endToEndId};POST /v1/payments/fps/out |
| `EFPS0041` | 403 | Failed to execute account number modulus check | Instant_payments_-_UK_FPS_beta | 4 | GET /v1/payments/fps/{endToEndId};POST /v1/payments/fps/cancel/{endToEndId};POST /v1/payments/fps/out |
| `EFPS0046` | 400 | IntlBankAccounts - API returned 4xx error | Instant_payments_-_UK_FPS_beta | 4 | GET /v1/payments/fps/{endToEndId};POST /v1/payments/fps/cancel/{endToEndId};POST /v1/payments/fps/out |
| `EFPS0047` | 400 | Invalid FPS Request. Check error details for more information. | Instant_payments_-_UK_FPS_beta | 4 | GET /v1/payments/fps/{endToEndId};POST /v1/payments/fps/cancel/{endToEndId};POST /v1/payments/fps/out |
| `EFPS0058` | 409 | Record already exists | Instant_payments_-_UK_FPS_beta | 2 | POST /v1/payments/fps/cop;POST /v1/payments/fps/return/{endToEndId} |
| `EFPS0067` | 404 | Transaction API not found error | Instant_payments_-_UK_FPS_beta | 1 | POST /v1/payments/fps/return/{endToEndId} |
| `EFPS0073` | 400 | The amount passed is greater than the current balance | Instant_payments_-_UK_FPS_beta | 1 | POST /v1/payments/fps/out |
| `EFPS0085` | 403 | Missing required account-id | Instant_payments_-_UK_FPS_beta | 1 | POST /v1/payments/fps/return/{endToEndId} |
| `EFPS0086` | 403 | Missing required header: 'Idempotency-Key' | Instant_payments_-_UK_FPS_beta | 2 | POST /v1/payments/fps/cop;POST /v1/payments/fps/return/{endToEndId} |
| `EFPS0093` | 422 | Payment is not eligible for return | Instant_payments_-_UK_FPS_beta | 1 | POST /v1/payments/fps/return/{endToEndId} |
| `EFPS0094` | 409 | Transaction status is not HOLD, release is not allowed | Instant_payments_-_UK_FPS_beta | 1 | POST /v1/payments/fps/release/{endToEndId} |
| `EFPS0095` | 409 | Transaction status is not HOLD, cancel is not allowed | Instant_payments_-_UK_FPS_beta | 1 | POST /v1/payments/fps/cancel/{endToEndId} |
| `EFPS0096` | 400 | Partial returns are not allowed. Return amount must match the original transaction amount | Instant_payments_-_UK_FPS_beta | 1 | POST /v1/payments/fps/return/{endToEndId} |

## Lifecycle status

Codes in this unit that are mentioned in changelog posts (check the post: it may record that the code was added, changed or removed from some endpoints):

- `EFPS0094`: `KU-CHG-7-august-2026`
- `EFPS0096`: `KU-CHG-2-july-2026`

## Conflicts, caveats and evidence gaps

- Codes and messages come from response examples in the OpenAPI specifications; the conditions that trigger a code are documented only where the message or the operation description states them.
- The source table recognises only codes made of letters followed by digits; codes with mixed prefixes (for example `WP2P0000`) are not in the table but appear in the API-reference KUs.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-reference-data/error_code_index.csv` | rows with code prefix EFPS | https://github.com/PismoDevEx/pismo-api-specs | `76213ae93e90a725…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-API-instant-payments-uk-fps-beta--faster-payments` — API reference: Instant payments - Faster payments — Faster payments
- `KU-CHG-2-july-2026` — Changelog: 2 July 2026
- `KU-CHG-7-august-2026` — Changelog: 7 August 2026
