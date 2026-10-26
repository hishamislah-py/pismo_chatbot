---
ku_id: KU-ERR-codes-weam
title: 'Error codes: WEAM'
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
- KU-API-banking-transaction-banking--earmarking-external-accounts
- KU-API-banking-transaction-banking--earmarking-pismo-account-id
- KU-API-banking-transaction-banking--payments-pismo-account-id
- KU-CHG-1-may-2026
- KU-CHG-3-april-2026
- KU-CHG-3-january-2025
- KU-CHG-4-april-2025
- KU-CHG-5-september-2025
- KU-CHG-8-august-2025
- KU-CHG-9-january-2026
error_codes:
- WEAM0001
- WEAM0005
- WEAM0006
- WEAM0007
- WEAM0008
- WEAM0009
- WEAM0014
- WEAM0015
- WEAM0016
- WEAM0017
- WEAM0018
- WEAM0019
- WEAM0020
- WEAM0022
- WEAM0023
- WEAM0024
- WEAM0025
- WEAM0026
- WEAM0027
- WEAM0030
- WEAM0031
- WEAM0033
- WEAM0034
- WEAM0036
- WEAM0037
- WEAM0038
- WEAM0039
- WEAM0040
- WEAM0041
- WEAM0042
- WEAM0043
- WEAM0044
- WEAM0045
- WEAM0046
- WEAM0047
- WEAM0048
- WEAM0049
---

# Error codes: WEAM

**KU ID:** `KU-ERR-codes-weam` · **Category:** Errors and troubleshooting · **Type:** error-code catalogue (from reference table)

## Purpose and scope

37 error code(s) with prefix(es) WEAM from `api-reference-data/error_code_index.csv`, with the HTTP status, message and the operations whose response examples contain the code. The `operations_sample` column is a sample, not a complete list: the complete set of codes per operation is in the API-reference KUs (section “Error codes shown in this operation's response examples”). Conditions under which a code is returned are documented only where the message or the operation description states them.

## Error codes

| Code | HTTP status | Message | Specification files | Operation count | Operations (sample) |
| --- | --- | --- | --- | --- | --- |
| `WEAM0001` | 409 | earmark_id [{earmark_id}] is already in use | Banking_-_Transaction_banking | 2 | POST /cash-management/v2/earmarks;POST /corporate/v2/earmarks |
| `WEAM0005` | 400 | Invalid account status | Banking_-_Transaction_banking | 2 | POST /cash-management/v2/earmarks;POST /corporate/v2/earmarks |
| `WEAM0006` | 400 | Earmark does not have sufficient balance to complete this operation. Balance: `earmark_balance` | Banking_-_Transaction_banking | 4 | POST /cash-management/v2/earmarks;POST /cash-management/v2/payments;POST /corporate/v2/earmarks |
| `WEAM0007` | 404 | Earmark with ID `earmark_id` not found | Banking_-_Transaction_banking | 4 | POST /cash-management/v2/earmarks/{earmarkId}/cancel;POST /cash-management/v2/payments;POST /corporate/v2/earmarks/{earmarkId}/cancel |
| `WEAM0008` | 400 | Earmark ID `earmark_id` not active | Banking_-_Transaction_banking | 4 | POST /cash-management/v2/earmarks/{earmarkId}/cancel;POST /cash-management/v2/payments;POST /corporate/v2/earmarks/{earmarkId}/cancel |
| `WEAM0009` | 401 | Account not authorized | Banking_-_Transaction_banking | 2 | POST /cash-management/v2/earmarks;POST /corporate/v2/earmarks |
| `WEAM0014` | 400 | Invalid JSON payload received: Error unmarshalling request | Banking_-_Transaction_banking | 6 | PATCH /cash-management/v2/earmarks/{earmarkId};PATCH /corporate/v2/earmarks/{earmarkId};POST /cash-management/v2/earmarks |
| `WEAM0015` | 400 | The number of decimal places is not compatible with the specified currency | Banking_-_Transaction_banking | 6 | PATCH /cash-management/v2/earmarks/{earmarkId};PATCH /corporate/v2/earmarks/{earmarkId};POST /cash-management/v2/earmarks |
| `WEAM0016` | 400 | Invalid header account | Banking_-_Transaction_banking | 4 | PATCH /cash-management/v2/earmarks/{earmarkId};PATCH /corporate/v2/earmarks/{earmarkId};POST /cash-management/v2/earmarks |
| `WEAM0017` | 400 | Orgs operations not found or parameters are incorrect or invalid | Banking_-_Transaction_banking | 8 | PATCH /cash-management/v2/earmarks/{earmarkId};PATCH /corporate/v2/earmarks/{earmarkId};POST /cash-management/v2/earmarks |
| `WEAM0018` | 400 | operation already made | Banking_-_Transaction_banking | 6 | PATCH /cash-management/v2/earmarks/{earmarkId};PATCH /corporate/v2/earmarks/{earmarkId};POST /cash-management/v2/earmarks |
| `WEAM0019` | 400 | The account's program type is invalid | Banking_-_Transaction_banking | 8 | PATCH /cash-management/v2/earmarks/{earmarkId};PATCH /corporate/v2/earmarks/{earmarkId};POST /cash-management/v2/earmarks |
| `WEAM0020` | 401 | Use of a valid token for a valid account is required | Banking_-_Transaction_banking | 2 | POST /cash-management/v2/earmarks;POST /corporate/v2/earmarks |
| `WEAM0022` | 400 | Earmark with ID {earmarkId} has zero balance | Banking_-_Transaction_banking | 2 | POST /cash-management/v2/earmarks/{earmarkId}/cancel;POST /corporate/v2/earmarks/{earmarkId}/cancel |
| `WEAM0023` | 401 | The account cannot be debited. Debit function is not active | Banking_-_Transaction_banking | 4 | PATCH /cash-management/v2/earmarks/{earmarkId};PATCH /corporate/v2/earmarks/{earmarkId};POST /cash-management/v2/earmarks |
| `WEAM0024` | 401 | The account cannot be credited. Credit function is not active | Banking_-_Transaction_banking | 6 | PATCH /cash-management/v2/earmarks/{earmarkId};PATCH /corporate/v2/earmarks/{earmarkId};POST /cash-management/v2/earmarks |
| `WEAM0025` | 409 | Tracking ID is already in use | Banking_-_Transaction_banking | 6 | PATCH /cash-management/v2/earmarks/{earmarkId};PATCH /corporate/v2/earmarks/{earmarkId};POST /cash-management/v2/earmarks |
| `WEAM0026` | 400 | Action not permitted on a closed account | Banking_-_Transaction_banking | 4 | PATCH /cash-management/v2/earmarks/{earmarkId};PATCH /corporate/v2/earmarks/{earmarkId};POST /cash-management/v2/earmarks |
| `WEAM0027` | 400 | You cannot force a release that results in the decrease of the earmark balance | Banking_-_Transaction_banking | 2 | PATCH /cash-management/v2/earmarks/{earmarkId};PATCH /corporate/v2/earmarks/{earmarkId} |
| `WEAM0030` | 400 | Maximum number of internal operations reached [limit] | Banking_-_Transaction_banking | 2 | PATCH /cash-management/v2/earmarks/{earmarkId};PATCH /corporate/v2/earmarks/{earmarkId} |
| `WEAM0031` | 400 | Balance cannot be reduced to zero as a result of this operation | Banking_-_Transaction_banking | 2 | PATCH /cash-management/v2/earmarks/{earmarkId};PATCH /corporate/v2/earmarks/{earmarkId} |
| `WEAM0033` | 423 | transaction using this tracking_id is in progress, please try again later | Banking_-_Transaction_banking | 2 | POST /cash-management/v2/earmarks;POST /corporate/v2/earmarks |
| `WEAM0034` | 409 | Tracking ID is already in use | Banking_-_Transaction_banking | 6 | PATCH /cash-management/v2/earmarks/{earmarkId};PATCH /corporate/v2/earmarks/{earmarkId};POST /cash-management/v2/earmarks |
| `WEAM0036` | 400 | Administrative division is misconfigured | Banking_-_Transaction_banking | 6 | PATCH /cash-management/v2/earmarks/{earmarkId};PATCH /corporate/v2/earmarks/{earmarkId};POST /cash-management/v2/earmarks |
| `WEAM0037` | 400 | Account has not finished onboarding | Banking_-_Transaction_banking | 2 | POST /cash-management/v2/earmarks;POST /corporate/v2/earmarks |
| `WEAM0038` | 400 | Earmark balance is unchanged | Banking_-_Transaction_banking | 2 | PATCH /cash-management/v2/earmarks/{earmarkId};PATCH /corporate/v2/earmarks/{earmarkId} |
| `WEAM0039` | 400 | Invalid business date for the current business day cycle | Banking_-_Transaction_banking | 6 | PATCH /cash-management/v2/earmarks/{earmarkId};PATCH /corporate/v2/earmarks/{earmarkId};POST /cash-management/v2/earmarks |
| `WEAM0040` | 400 | The payment date cannot be earlier than the account creation date | Banking_-_Transaction_banking | 6 | PATCH /cash-management/v2/earmarks/{earmarkId};PATCH /corporate/v2/earmarks/{earmarkId};POST /cash-management/v2/earmarks |
| `WEAM0041` | 400 | Business date cannot be earlier than the earmark creation date | Banking_-_Transaction_banking | 4 | PATCH /cash-management/v2/earmarks/{earmarkId};PATCH /corporate/v2/earmarks/{earmarkId};POST /cash-management/v2/earmarks/{earmarkId}/cancel |
| `WEAM0042` | 400 | Future dated earmark operations are not allowed | Banking_-_Transaction_banking | 6 | PATCH /cash-management/v2/earmarks/{earmarkId};PATCH /corporate/v2/earmarks/{earmarkId};POST /cash-management/v2/earmarks |
| `WEAM0043` | 400 | Cannot post transaction on holidays | Banking_-_Transaction_banking | 6 | PATCH /cash-management/v2/earmarks/{earmarkId};PATCH /corporate/v2/earmarks/{earmarkId};POST /cash-management/v2/earmarks |
| `WEAM0044` | 400 | Cannot post transaction on weekends | Banking_-_Transaction_banking | 6 | PATCH /cash-management/v2/earmarks/{earmarkId};PATCH /corporate/v2/earmarks/{earmarkId};POST /cash-management/v2/earmarks |
| `WEAM0045` | 400 | Back business dating is disabled | Banking_-_Transaction_banking | 6 | PATCH /cash-management/v2/earmarks/{earmarkId};PATCH /corporate/v2/earmarks/{earmarkId};POST /cash-management/v2/earmarks |
| `WEAM0046` | 400 | Invalid account currency code: 999 | Banking_-_Transaction_banking | 6 | PATCH /cash-management/v2/earmarks/{earmarkId};PATCH /corporate/v2/earmarks/{earmarkId};POST /cash-management/v2/earmarks |
| `WEAM0047` | 400 | The payment date cannot be earlier than the account migration date | Banking_-_Transaction_banking | 6 | PATCH /cash-management/v2/earmarks/{earmarkId};PATCH /corporate/v2/earmarks/{earmarkId};POST /cash-management/v2/earmarks |
| `WEAM0048` | 423 | Earmark locked by a concurrent operation | Banking_-_Transaction_banking | 8 | PATCH /cash-management/v2/earmarks/{earmarkId};PATCH /corporate/v2/earmarks/{earmarkId};POST /cash-management/v2/earmarks |
| `WEAM0049` | 409 | Earmark was concurrently modified | Banking_-_Transaction_banking | 6 | PATCH /cash-management/v2/earmarks/{earmarkId};PATCH /corporate/v2/earmarks/{earmarkId};POST /cash-management/v2/earmarks/{earmarkId}/cancel |

## Lifecycle status

Codes in this unit that are mentioned in changelog posts (check the post: it may record that the code was added, changed or removed from some endpoints):

- `WEAM0001`: `KU-CHG-4-april-2025`
- `WEAM0015`: `KU-CHG-3-january-2025`
- `WEAM0016`: `KU-CHG-3-april-2026`
- `WEAM0024`: `KU-CHG-3-april-2026`
- `WEAM0025`: `KU-CHG-4-april-2025`
- `WEAM0033`: `KU-CHG-4-april-2025`
- `WEAM0039`: `KU-CHG-8-august-2025`
- `WEAM0040`: `KU-CHG-5-september-2025`
- `WEAM0041`: `KU-CHG-8-august-2025`
- `WEAM0042`: `KU-CHG-8-august-2025`
- `WEAM0043`: `KU-CHG-8-august-2025`
- `WEAM0044`: `KU-CHG-8-august-2025`
- `WEAM0046`: `KU-CHG-9-january-2026`
- `WEAM0047`: `KU-CHG-1-may-2026`

## Conflicts, caveats and evidence gaps

- Codes and messages come from response examples in the OpenAPI specifications; the conditions that trigger a code are documented only where the message or the operation description states them.
- The source table recognises only codes made of letters followed by digits; codes with mixed prefixes (for example `WP2P0000`) are not in the table but appear in the API-reference KUs.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-reference-data/error_code_index.csv` | rows with code prefix WEAM | https://github.com/PismoDevEx/pismo-api-specs | `76213ae93e90a725…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-API-banking-transaction-banking--earmarking-external-accounts` — API reference: Banking - Transaction banking — Earmarking (external accounts)
- `KU-API-banking-transaction-banking--earmarking-pismo-account-id` — API reference: Banking - Transaction banking — Earmarking (Pismo account ID)
- `KU-API-banking-transaction-banking--payments-pismo-account-id` — API reference: Banking - Transaction banking — Payments (Pismo account ID)
- `KU-CHG-1-may-2026` — Changelog: 1 May 2026
- `KU-CHG-3-april-2026` — Changelog: 3 April 2026
- `KU-CHG-3-january-2025` — Changelog: 3 January 2025
- `KU-CHG-4-april-2025` — Changelog: 4 April 2025
- `KU-CHG-5-september-2025` — Changelog: 5 September 2025
- `KU-CHG-8-august-2025` — Changelog: 8 August 2025
- `KU-CHG-9-january-2026` — Changelog: 9 January 2026
