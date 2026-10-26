---
ku_id: KU-ERR-codes-eupi
title: 'Error codes: EUPI'
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
- KU-API-instant-payments-rupay-on-upi--upi
error_codes:
- EUPI0001
- EUPI0002
- EUPI0003
- EUPI0004
- EUPI0007
- EUPI0014
- EUPI0020
- EUPI0023
- EUPI0024
- EUPI0028
- EUPI0031
- EUPI0032
- EUPI0033
- EUPI0034
- EUPI0035
- EUPI0036
- EUPI0038
- EUPI0039
- EUPI0040
- EUPI0041
- EUPI0042
- EUPI0100
- EUPI0101
- EUPI0103
- EUPI0104
- EUPI0105
- EUPI0106
- EUPI0108
- EUPI0109
- EUPI0110
- EUPI0112
- EUPI0113
- EUPI0114
- EUPI0120
- EUPI0121
---

# Error codes: EUPI

**KU ID:** `KU-ERR-codes-eupi` · **Category:** Errors and troubleshooting · **Type:** error-code catalogue (from reference table)

## Purpose and scope

35 error code(s) with prefix(es) EUPI from `api-reference-data/error_code_index.csv`, with the HTTP status, message and the operations whose response examples contain the code. The `operations_sample` column is a sample, not a complete list: the complete set of codes per operation is in the API-reference KUs (section “Error codes shown in this operation's response examples”). Conditions under which a code is returned are documented only where the message or the operation description states them.

## Error codes

| Code | HTTP status | Message | Specification files | Operation count | Operations (sample) |
| --- | --- | --- | --- | --- | --- |
| `EUPI0001` | 500 | An unexpected error happened | Instant_payments_-_RuPay_on_UPI | 6 | POST /v1/cards/balance;POST /v1/cards/credit-card-bill;POST /v1/cards/emi-select |
| `EUPI0002` | 400 | Validation error | Instant_payments_-_RuPay_on_UPI | 6 | POST /v1/cards/balance;POST /v1/cards/credit-card-bill;POST /v1/cards/emi-select |
| `EUPI0003` | 400 | Bad Request | Instant_payments_-_RuPay_on_UPI | 6 | POST /v1/cards/balance;POST /v1/cards/credit-card-bill;POST /v1/cards/emi-select |
| `EUPI0004` | 403 | Missing required header 'x-tenant' | Instant_payments_-_RuPay_on_UPI | 7 | GET /v1/transactions/inquiry/account-reference-number/{account_reference_number}/external-transaction-id/{external_transaction_id};POST /v1/cards/balance;POST /v1/cards/credit-card-bill |
| `EUPI0007` | 404 | Account not found. | Instant_payments_-_RuPay_on_UPI | 3 | POST /v1/cards/balance;POST /v1/cards/credit-card-bill;POST /v1/cards/list |
| `EUPI0014` | 409 | Not unique owner for the phone number | Instant_payments_-_RuPay_on_UPI | 1 | POST /v1/cards/list |
| `EUPI0020` | 408 | Upi - API returned a timeout error | Instant_payments_-_RuPay_on_UPI | 3 | GET /v1/transactions/inquiry/account-reference-number/{account_reference_number}/external-transaction-id/{external_transaction_id};POST /v1/cards/emi-select;POST /v1/cards/transfer |
| `EUPI0023` | 400 | number is a required field | Instant_payments_-_RuPay_on_UPI | 2 | POST /v1/cards/credit-card-bill;POST /v1/cards/list |
| `EUPI0024` | 409 | card type invalid | Instant_payments_-_RuPay_on_UPI | 1 | POST /v1/cards/list |
| `EUPI0028` | 404 | Cards not found. | Instant_payments_-_RuPay_on_UPI | 4 | POST /v1/cards/balance;POST /v1/cards/credit-card-bill;POST /v1/cards/list |
| `EUPI0031` | 404 | An unexpected error has occurred while fetching Ledger information. | Instant_payments_-_RuPay_on_UPI | 1 | POST /v1/cards/balance |
| `EUPI0032` | 404 | Not found. | Instant_payments_-_RuPay_on_UPI | 4 | POST /v1/cards/balance;POST /v1/cards/credit-card-bill;POST /v1/cards/list |
| `EUPI0033` | 409 | Card with SUSPENDED status | Instant_payments_-_RuPay_on_UPI | 1 | POST /v1/cards/validate |
| `EUPI0034` | 409 | last_six_digits sent is not equal as original card data | Instant_payments_-_RuPay_on_UPI | 1 | POST /v1/cards/validate |
| `EUPI0035` | 409 | card_expiration sent is not equal as original card data | Instant_payments_-_RuPay_on_UPI | 1 | POST /v1/cards/validate |
| `EUPI0036` | 409 | pinblock sent is not equal as original card pinblock | Instant_payments_-_RuPay_on_UPI | 1 | POST /v1/cards/validate |
| `EUPI0038` | 400 | pin is a required field | Instant_payments_-_RuPay_on_UPI | 1 | POST /v1/cards/validate |
| `EUPI0039` | 400 | card_expiration is a required field | Instant_payments_-_RuPay_on_UPI | 1 | POST /v1/cards/validate |
| `EUPI0040` | 400 | cvv is a required field | Instant_payments_-_RuPay_on_UPI | 1 | POST /v1/cards/validate |
| `EUPI0041` | 400 | last_six_digits is a required field | Instant_payments_-_RuPay_on_UPI | 1 | POST /v1/cards/validate |
| `EUPI0042` | 422 | An unexpected error has occurred | Instant_payments_-_RuPay_on_UPI | 4 | POST /v1/cards/balance;POST /v1/cards/credit-card-bill;POST /v1/cards/list |
| `EUPI0100` | 409 | Transaction already exists with the external_transaction_id | Instant_payments_-_RuPay_on_UPI | 2 | POST /v1/cards/emi-select;POST /v1/cards/transfer |
| `EUPI0101` | 400 | The transaction was cancelled due authorization request validation error | Instant_payments_-_RuPay_on_UPI | 2 | POST /v1/cards/emi-select;POST /v1/cards/transfer |
| `EUPI0103` | 404 | Transaction not found | Instant_payments_-_RuPay_on_UPI | 1 | GET /v1/transactions/inquiry/account-reference-number/{account_reference_number}/external-transaction-id/{external_transaction_id} |
| `EUPI0104` | 400 | Invalid transaction type | Instant_payments_-_RuPay_on_UPI | 2 | POST /v1/cards/emi-select;POST /v1/cards/transfer |
| `EUPI0105` | 500 | The transaction will be cancelled due to internal error | Instant_payments_-_RuPay_on_UPI | 2 | POST /v1/cards/emi-select;POST /v1/cards/transfer |
| `EUPI0106` | 500 | The transaction was authorized but will be canceled due to internal error | Instant_payments_-_RuPay_on_UPI | 2 | POST /v1/cards/emi-select;POST /v1/cards/transfer |
| `EUPI0108` | 400 | The transaction was cancelled due to an authorization error | Instant_payments_-_RuPay_on_UPI | 2 | POST /v1/cards/emi-select;POST /v1/cards/transfer |
| `EUPI0109` | 502 | The transaction will be cancelled due to authorization error | Instant_payments_-_RuPay_on_UPI | 2 | POST /v1/cards/emi-select;POST /v1/cards/transfer |
| `EUPI0110` | 404 | Original transaction not found on reversal operation | Instant_payments_-_RuPay_on_UPI | 2 | POST /v1/cards/emi-select;POST /v1/cards/transfer |
| `EUPI0112` | 409 | Original transaction is still being processed | Instant_payments_-_RuPay_on_UPI | 2 | POST /v1/cards/emi-select;POST /v1/cards/transfer |
| `EUPI0113` | 409 | Original transaction is not accepted, then it can't be reverted | Instant_payments_-_RuPay_on_UPI | 2 | POST /v1/cards/emi-select;POST /v1/cards/transfer |
| `EUPI0114` | 409 | Reversal transaction amount must be equals to the original transaction | Instant_payments_-_RuPay_on_UPI | 2 | POST /v1/cards/emi-select;POST /v1/cards/transfer |
| `EUPI0120` | 200;401 | Transfer amount is greater than the account available limits | Instant_payments_-_RuPay_on_UPI | 3 | GET /v1/transactions/inquiry/account-reference-number/{account_reference_number}/external-transaction-id/{external_transaction_id};POST /v1/cards/emi-select;POST /v1/cards/transfer |
| `EUPI0121` | 409 | Invalid card status | Instant_payments_-_RuPay_on_UPI | 2 | POST /v1/cards/emi-select;POST /v1/cards/transfer |

## Lifecycle status

- No code in this unit is mentioned in a changelog post.

## Conflicts, caveats and evidence gaps

- Codes and messages come from response examples in the OpenAPI specifications; the conditions that trigger a code are documented only where the message or the operation description states them.
- The source table recognises only codes made of letters followed by digits; codes with mixed prefixes (for example `WP2P0000`) are not in the table but appear in the API-reference KUs.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-reference-data/error_code_index.csv` | rows with code prefix EUPI | https://github.com/PismoDevEx/pismo-api-specs | `76213ae93e90a725…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-API-instant-payments-rupay-on-upi--upi` — API reference: Instant payments - RuPay on UPI — UPI
