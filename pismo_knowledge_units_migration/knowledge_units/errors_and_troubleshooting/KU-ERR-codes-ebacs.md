---
ku_id: KU-ERR-codes-ebacs
title: 'Error codes: EBACS'
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
- KU-API-payment-rails-bacs-payments--bacs-direct-credit
- KU-API-payment-rails-bacs-payments--bacs-direct-debit
error_codes:
- EBACS0002
- EBACS0003
- EBACS0004
- EBACS0006
- EBACS0009
- EBACS0010
- EBACS0011
- EBACS0012
- EBACS0014
- EBACS0015
- EBACS0016
- EBACS0017
- EBACS0018
- EBACS0019
- EBACS0020
- EBACS0021
- EBACS0022
- EBACS0023
- EBACS0024
- EBACS0025
- EBACS0026
- EBACS0027
- EBACS0028
- EBACS0029
- EBACS0030
- EBACS0031
- EBACS0032
- EBACS0033
- EBACS0034
- EBACS0035
- EBACS0036
- EBACS0037
- EBACS0038
- EBACS0039
- EBACS0040
- EBACS0041
- EBACS0046
- EBACS0047
- EBACS0048
- EBACS0049
- EBACS0058
- EBACS0067
- EBACS0073
- EBACS0085
- EBACS0086
- EBACS0092
- EBACS0093
- EBACS0094
- EBACS0095
- EBACS0096
- EBACS0097
- EBACS0102
- EBACS0103
- EBACS0104
- EBACS0105
- EBACS0107
- EBACS0108
---

# Error codes: EBACS

**KU ID:** `KU-ERR-codes-ebacs` · **Category:** Errors and troubleshooting · **Type:** error-code catalogue (from reference table)

## Purpose and scope

57 error code(s) with prefix(es) EBACS from `api-reference-data/error_code_index.csv`, with the HTTP status, message and the operations whose response examples contain the code. The `operations_sample` column is a sample, not a complete list: the complete set of codes per operation is in the API-reference KUs (section “Error codes shown in this operation's response examples”). Conditions under which a code is returned are documented only where the message or the operation description states them.

## Error codes

| Code | HTTP status | Message | Specification files | Operation count | Operations (sample) |
| --- | --- | --- | --- | --- | --- |
| `EBACS0002` | 403 | Missing required header: 'x-tenant' | Payment_rails_-_BACS_payments | 15 | GET /v1/payments/bacs/directcredit;GET /v1/payments/bacs/directcredit/{id};GET /v1/payments/bacs/directdebit |
| `EBACS0003` | 500 | Internal error | Payment_rails_-_BACS_payments | 5 | GET /v1/payments/bacs/directdebit/claims;PATCH /v1/payments/bacs/directdebit/mandates/{id};POST /v1/payments/bacs/directdebit/claims |
| `EBACS0004` | 400 | Validation error | Payment_rails_-_BACS_payments | 15 | GET /v1/payments/bacs/directcredit;GET /v1/payments/bacs/directcredit/{id};GET /v1/payments/bacs/directdebit |
| `EBACS0006` | 500 | HTTP request error | Payment_rails_-_BACS_payments | 6 | GET /v1/payments/bacs/directcredit/{id};POST /v1/payments/bacs/directcredit/cancel/{id};POST /v1/payments/bacs/directcredit/out |
| `EBACS0009` | 500 | IntlBankAccounts API timeout error | Payment_rails_-_BACS_payments | 4 | GET /v1/payments/bacs/directcredit/{id};POST /v1/payments/bacs/directcredit/cancel/{id};POST /v1/payments/bacs/directcredit/out |
| `EBACS0010` | 404 | Transaction not found | Payment_rails_-_BACS_payments | 5 | GET /v1/payments/bacs/directcredit/{id};POST /v1/payments/bacs/directcredit/cancel/{id};POST /v1/payments/bacs/directcredit/out |
| `EBACS0011` | 500 | IntlBankAccounts API Internal Server error | Payment_rails_-_BACS_payments | 4 | GET /v1/payments/bacs/directcredit/{id};POST /v1/payments/bacs/directcredit/cancel/{id};POST /v1/payments/bacs/directcredit/out |
| `EBACS0012` | 500 | PSPGateway API timeout error | Payment_rails_-_BACS_payments | 6 | GET /v1/payments/bacs/directcredit/{id};POST /v1/payments/bacs/directcredit/cancel/{id};POST /v1/payments/bacs/directcredit/out |
| `EBACS0014` | 502 | PSPGateway API Bad Gateway | Payment_rails_-_BACS_payments | 6 | GET /v1/payments/bacs/directcredit/{id};POST /v1/payments/bacs/directcredit/cancel/{id};POST /v1/payments/bacs/directcredit/out |
| `EBACS0015` | 429 | PSPGateway API Rate Limit exceeded | Payment_rails_-_BACS_payments | 6 | GET /v1/payments/bacs/directcredit/{id};POST /v1/payments/bacs/directcredit/cancel/{id};POST /v1/payments/bacs/directcredit/out |
| `EBACS0016` | 400 | Unmarshal error | Payment_rails_-_BACS_payments | 8 | GET /v1/payments/bacs/directcredit/{id};PATCH /v1/payments/bacs/directdebit/mandates/{id};POST /v1/payments/bacs/directcredit/cancel/{id} |
| `EBACS0017` | 500 | Accounts API timeout error | Payment_rails_-_BACS_payments | 4 | GET /v1/payments/bacs/directcredit/{id};POST /v1/payments/bacs/directcredit/cancel/{id};POST /v1/payments/bacs/directcredit/out |
| `EBACS0018` | 404 | Accounts - Not found | Payment_rails_-_BACS_payments | 4 | GET /v1/payments/bacs/directcredit/{id};POST /v1/payments/bacs/directcredit/cancel/{id};POST /v1/payments/bacs/directcredit/out |
| `EBACS0019` | 400 | Accounts - API returned 4xx error | Payment_rails_-_BACS_payments | 4 | GET /v1/payments/bacs/directcredit/{id};POST /v1/payments/bacs/directcredit/cancel/{id};POST /v1/payments/bacs/directcredit/out |
| `EBACS0020` | 500 | Accounts - API returned 5xx error | Payment_rails_-_BACS_payments | 4 | GET /v1/payments/bacs/directcredit/{id};POST /v1/payments/bacs/directcredit/cancel/{id};POST /v1/payments/bacs/directcredit/out |
| `EBACS0021` | 403 | Account blocked or cancelled | Payment_rails_-_BACS_payments | 7 | GET /v1/payments/bacs/directcredit/{id};POST /v1/payments/bacs/directcredit/cancel/{id};POST /v1/payments/bacs/directcredit/out |
| `EBACS0022` | 409 | A transaction with the specified idempotency key and id already exists | Payment_rails_-_BACS_payments | 4 | GET /v1/payments/bacs/directcredit/{id};POST /v1/payments/bacs/directcredit/cancel/{id};POST /v1/payments/bacs/directcredit/out |
| `EBACS0023` | 500 | Transaction database error | Payment_rails_-_BACS_payments | 10 | GET /v1/payments/bacs/directcredit;GET /v1/payments/bacs/directcredit/{id};GET /v1/payments/bacs/directdebit |
| `EBACS0024` | 500 | P2p - API timeout error | Payment_rails_-_BACS_payments | 4 | GET /v1/payments/bacs/directcredit/{id};POST /v1/payments/bacs/directcredit/cancel/{id};POST /v1/payments/bacs/directcredit/out |
| `EBACS0025` | 400 | P2p - API returned 4xx error | Payment_rails_-_BACS_payments | 4 | GET /v1/payments/bacs/directcredit/{id};POST /v1/payments/bacs/directcredit/cancel/{id};POST /v1/payments/bacs/directcredit/out |
| `EBACS0026` | 500 | P2p - API returned 5xx error | Payment_rails_-_BACS_payments | 4 | GET /v1/payments/bacs/directcredit/{id};POST /v1/payments/bacs/directcredit/cancel/{id};POST /v1/payments/bacs/directcredit/out |
| `EBACS0027` | 500 | Ledger API timeout error | Payment_rails_-_BACS_payments | 4 | GET /v1/payments/bacs/directcredit/{id};POST /v1/payments/bacs/directcredit/cancel/{id};POST /v1/payments/bacs/directcredit/out |
| `EBACS0028` | 404 | Ledger - Not found | Payment_rails_-_BACS_payments | 4 | GET /v1/payments/bacs/directcredit/{id};POST /v1/payments/bacs/directcredit/cancel/{id};POST /v1/payments/bacs/directcredit/out |
| `EBACS0029` | 400 | Ledger - API returned 4xx error | Payment_rails_-_BACS_payments | 4 | GET /v1/payments/bacs/directcredit/{id};POST /v1/payments/bacs/directcredit/cancel/{id};POST /v1/payments/bacs/directcredit/out |
| `EBACS0030` | 500 | Ledger - API returned 5xx error | Payment_rails_-_BACS_payments | 4 | GET /v1/payments/bacs/directcredit/{id};POST /v1/payments/bacs/directcredit/cancel/{id};POST /v1/payments/bacs/directcredit/out |
| `EBACS0031` | 404 | IntlBankAccounts - Not found | Payment_rails_-_BACS_payments | 4 | GET /v1/payments/bacs/directcredit/{id};POST /v1/payments/bacs/directcredit/cancel/{id};POST /v1/payments/bacs/directcredit/out |
| `EBACS0032` | 500 | IntlBankAccounts - API returned 5xx error | Payment_rails_-_BACS_payments | 4 | GET /v1/payments/bacs/directcredit/{id};POST /v1/payments/bacs/directcredit/cancel/{id};POST /v1/payments/bacs/directcredit/out |
| `EBACS0033` | 403 | Invalid account id header: 'x-account-id' | Payment_rails_-_BACS_payments | 6 | GET /v1/payments/bacs/directcredit/{id};POST /v1/payments/bacs/directcredit/cancel/{id};POST /v1/payments/bacs/directcredit/out |
| `EBACS0034` | 403 | Missing required header: 'x-idempotency-key' | Payment_rails_-_BACS_payments | 6 | GET /v1/payments/bacs/directcredit/{id};POST /v1/payments/bacs/directcredit/cancel/{id};POST /v1/payments/bacs/directcredit/out |
| `EBACS0035` | 403 | Account has no active addresses | Payment_rails_-_BACS_payments | 4 | GET /v1/payments/bacs/directcredit/{id};POST /v1/payments/bacs/directcredit/cancel/{id};POST /v1/payments/bacs/directcredit/out |
| `EBACS0036` | 409 | The provided currency does not match with the account's configured currency | Payment_rails_-_BACS_payments | 4 | GET /v1/payments/bacs/directcredit/{id};POST /v1/payments/bacs/directcredit/cancel/{id};POST /v1/payments/bacs/directcredit/out |
| `EBACS0037` | 400 | Invalid creditor sort code/account number | Payment_rails_-_BACS_payments | 4 | GET /v1/payments/bacs/directcredit/{id};POST /v1/payments/bacs/directcredit/cancel/{id};POST /v1/payments/bacs/directcredit/out |
| `EBACS0038` | 400 | Invalid creditor IBAN | Payment_rails_-_BACS_payments | 4 | GET /v1/payments/bacs/directcredit/{id};POST /v1/payments/bacs/directcredit/cancel/{id};POST /v1/payments/bacs/directcredit/out |
| `EBACS0039` | 400 | Invalid creditor BBAN | Payment_rails_-_BACS_payments | 4 | GET /v1/payments/bacs/directcredit/{id};POST /v1/payments/bacs/directcredit/cancel/{id};POST /v1/payments/bacs/directcredit/out |
| `EBACS0040` | 403 | BACS is not enabled for the creditor sort code | Payment_rails_-_BACS_payments | 4 | GET /v1/payments/bacs/directcredit/{id};POST /v1/payments/bacs/directcredit/cancel/{id};POST /v1/payments/bacs/directcredit/out |
| `EBACS0041` | 403 | Failed to execute account number modulus check | Payment_rails_-_BACS_payments | 4 | GET /v1/payments/bacs/directcredit/{id};POST /v1/payments/bacs/directcredit/cancel/{id};POST /v1/payments/bacs/directcredit/out |
| `EBACS0046` | 400 | IntlBankAccounts - API returned 4xx error | Payment_rails_-_BACS_payments | 4 | GET /v1/payments/bacs/directcredit/{id};POST /v1/payments/bacs/directcredit/cancel/{id};POST /v1/payments/bacs/directcredit/out |
| `EBACS0047` | 400 | Invalid BACS Request. Check error details for more information. | Payment_rails_-_BACS_payments | 6 | GET /v1/payments/bacs/directcredit/{id};POST /v1/payments/bacs/directcredit/cancel/{id};POST /v1/payments/bacs/directcredit/out |
| `EBACS0048` | 500 | PSPGateway API returned 4xx error | Payment_rails_-_BACS_payments | 1 | POST /v1/payments/bacs/directcredit/return/{id} |
| `EBACS0049` | 500 | PSPGateway API returned 5xx error | Payment_rails_-_BACS_payments | 1 | POST /v1/payments/bacs/directcredit/return/{id} |
| `EBACS0058` | 409 | Record already exists | Payment_rails_-_BACS_payments | 2 | POST /v1/payments/bacs/directdebit/claims;POST /v1/payments/bacs/directdebit/paper-mandates |
| `EBACS0067` | 404 | Transaction not found | Payment_rails_-_BACS_payments | 1 | POST /v1/payments/bacs/directcredit/return/{id} |
| `EBACS0073` | 400 | The amount passed is greater than the current balance | Payment_rails_-_BACS_payments | 1 | POST /v1/payments/bacs/directcredit/out |
| `EBACS0085` | 403 | Missing required account-id | Payment_rails_-_BACS_payments | 9 | GET /v1/payments/bacs/directcredit;GET /v1/payments/bacs/directdebit;GET /v1/payments/bacs/directdebit/claims |
| `EBACS0086` | 403 | Missing required header: 'Idempotency-Key' | Payment_rails_-_BACS_payments | 3 | POST /v1/payments/bacs/directcredit/return/{id};POST /v1/payments/bacs/directdebit/claims;POST /v1/payments/bacs/directdebit/claims/reversal/{id} |
| `EBACS0092` | 404 | PSPGateway API Not found | Payment_rails_-_BACS_payments | 1 | POST /v1/payments/bacs/directcredit/{id}/reversal |
| `EBACS0093` | 400 | Reversal not allowed: payment must be OUTBOUND with HOLD status | Payment_rails_-_BACS_payments | 1 | POST /v1/payments/bacs/directcredit/{id}/reversal |
| `EBACS0094` | 400 | Reversal not allowed: current time is past the payment creation day | Payment_rails_-_BACS_payments | 1 | POST /v1/payments/bacs/directcredit/{id}/reversal |
| `EBACS0095` | 400 | Partial returns are not allowed | Payment_rails_-_BACS_payments | 1 | POST /v1/payments/bacs/directcredit/return/{id} |
| `EBACS0096` | 409 | Cancel not allowed: transaction is already finalised | Payment_rails_-_BACS_payments | 1 | POST /v1/payments/bacs/directcredit/cancel/{id} |
| `EBACS0097` | 409 | Release not allowed: transaction is already finalised | Payment_rails_-_BACS_payments | 1 | POST /v1/payments/bacs/directcredit/release/{id} |
| `EBACS0102` | 404 | Mandate not found | Payment_rails_-_BACS_payments | 2 | PATCH /v1/payments/bacs/directdebit/mandates/{id};POST /v1/payments/bacs/directdebit/mandates/{id}/cancel |
| `EBACS0103` | 409 | Mandate cannot perform the requested operation in its current status | Payment_rails_-_BACS_payments | 2 | PATCH /v1/payments/bacs/directdebit/mandates/{id};POST /v1/payments/bacs/directdebit/mandates/{id}/cancel |
| `EBACS0104` | 409 | Mandate version does not match the current version | Payment_rails_-_BACS_payments | 2 | PATCH /v1/payments/bacs/directdebit/mandates/{id};POST /v1/payments/bacs/directdebit/mandates/{id}/cancel |
| `EBACS0105` | 403 | BACS mandates are not enabled for the account | Payment_rails_-_BACS_payments | 1 | POST /v1/payments/bacs/directdebit/paper-mandates |
| `EBACS0107` | 404 | Claim not found | Payment_rails_-_BACS_payments | 1 | POST /v1/payments/bacs/directdebit/claims/reversal/{id} |
| `EBACS0108` | 409 | Claim reversal not allowed: claim must be CONFIRMED (delivery confirmed) | Payment_rails_-_BACS_payments | 1 | POST /v1/payments/bacs/directdebit/claims/reversal/{id} |

## Lifecycle status

- No code in this unit is mentioned in a changelog post.

## Conflicts, caveats and evidence gaps

- Codes and messages come from response examples in the OpenAPI specifications; the conditions that trigger a code are documented only where the message or the operation description states them.
- The source table recognises only codes made of letters followed by digits; codes with mixed prefixes (for example `WP2P0000`) are not in the table but appear in the API-reference KUs.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-reference-data/error_code_index.csv` | rows with code prefix EBACS | https://github.com/PismoDevEx/pismo-api-specs | `76213ae93e90a725…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-API-payment-rails-bacs-payments--bacs-direct-credit` — API reference: Payment rails - BACS payments — BACS direct credit
- `KU-API-payment-rails-bacs-payments--bacs-direct-debit` — API reference: Payment rails - BACS payments — BACS direct debit
