---
ku_id: KU-ERR-codes-wpmt
title: 'Error codes: WPMT'
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
- KU-API-banking-transaction-banking--payments-part-01
- KU-API-banking-transaction-banking--payments-part-02
- KU-API-banking-transaction-banking--payments-part-03
- KU-API-banking-transaction-banking--payments-pismo-account-id
- KU-API-banking-transaction-banking--transactions
- KU-CHG-1-may-2026
- KU-CHG-3-april-2026
- KU-CHG-3-january-2025
- KU-CHG-4-april-2025
- KU-CHG-7-february-2025
- KU-CHG-7-november-2025
- KU-CHG-8-august-2025
- KU-CHG-9-january-2026
error_codes:
- WPMT0001
- WPMT0002
- WPMT0003
- WPMT0004
- WPMT0005
- WPMT0006
- WPMT0007
- WPMT0008
- WPMT0009
- WPMT0010
- WPMT0011
- WPMT0012
- WPMT0013
- WPMT0014
- WPMT0015
- WPMT0016
- WPMT0017
- WPMT0018
- WPMT0019
- WPMT0021
- WPMT0022
- WPMT0023
- WPMT0024
- WPMT0025
- WPMT0026
- WPMT0028
- WPMT0029
- WPMT0030
- WPMT0031
- WPMT0035
- WPMT0036
- WPMT0037
- WPMT0038
- WPMT0039
- WPMT0040
- WPMT0041
- WPMT0044
- WPMT0045
- WPMT0046
- WPMT0047
- WPMT0048
- WPMT0049
- WPMT0050
- WPMT0051
- WPMT0052
- WPMT0053
- WPMT0054
- WPMT0055
- WPMT0056
- WPMT0057
- WPMT0058
- WPMT0061
- WPMT0062
- WPMT0063
---

# Error codes: WPMT

**KU ID:** `KU-ERR-codes-wpmt` · **Category:** Errors and troubleshooting · **Type:** error-code catalogue (from reference table)

## Purpose and scope

54 error code(s) with prefix(es) WPMT from `api-reference-data/error_code_index.csv`, with the HTTP status, message and the operations whose response examples contain the code. The `operations_sample` column is a sample, not a complete list: the complete set of codes per operation is in the API-reference KUs (section “Error codes shown in this operation's response examples”). Conditions under which a code is returned are documented only where the message or the operation description states them.

## Error codes

| Code | HTTP status | Message | Specification files | Operation count | Operations (sample) |
| --- | --- | --- | --- | --- | --- |
| `WPMT0001` | 400 | The payment date cannot be earlier than the account creation date | Banking_-_Transaction_banking | 6 | POST /cash-management/v2/payments;POST /cash-management/v2/payments/cancel;POST /cash-management/v2/payments/confirm |
| `WPMT0002` | 400 | Invalid timezone {invalid} | Banking_-_Transaction_banking | 2 | POST /cash-management/v2/payments;POST /corporate/v2/payments |
| `WPMT0003` | 400 | Cannot post transaction on holidays | Banking_-_Transaction_banking | 6 | POST /cash-management/v2/payments;POST /cash-management/v2/payments/cancel;POST /cash-management/v2/payments/confirm |
| `WPMT0004` | 400 | Cannot post transaction on weekends | Banking_-_Transaction_banking | 6 | POST /cash-management/v2/payments;POST /cash-management/v2/payments/cancel;POST /cash-management/v2/payments/confirm |
| `WPMT0005` | 400 | Future dated payments only supports default debit processing code | Banking_-_Transaction_banking | 4 | POST /cash-management/v2/payments;POST /cash-management/v2/scheduled-payments;POST /corporate/v2/payments |
| `WPMT0006` | 400 | Future dated payments only supports default credit processing code | Banking_-_Transaction_banking | 4 | POST /cash-management/v2/payments;POST /cash-management/v2/scheduled-payments;POST /corporate/v2/payments |
| `WPMT0007` | 409 | tracking_id is already in use | Banking_-_Transaction_banking | 6 | POST /cash-management/v2/payments;POST /cash-management/v2/payments/cancel;POST /cash-management/v2/payments/confirm |
| `WPMT0008` | 400 | Invalid processing code | Banking_-_Transaction_banking | 2 | POST /cash-management/v2/payments;POST /corporate/v2/payments |
| `WPMT0009` | 400 | Invalid account status | Banking_-_Transaction_banking | 2 | POST /cash-management/v2/payments;POST /corporate/v2/payments |
| `WPMT0010` | 200;400 | Insufficient funds | Banking_-_Transaction_banking | 4 | GET /corporate/v1/corporate-transactions/status/{trackingId};GET /corporate/v3/payments/multileg/{multilegId};POST /cash-management/v2/payments |
| `WPMT0011` | 400 | Corporate account not found | Banking_-_Transaction_banking | 2 | POST /cash-management/v2/payments;POST /corporate/v2/payments |
| `WPMT0012` | 400 | Scheduled payment not found | Banking_-_Transaction_banking | 1 | DELETE /corporate/v2/scheduled-payments/{scheduledPaymentId} |
| `WPMT0013` | 400 | Scheduled payment not active | Banking_-_Transaction_banking | 1 | DELETE /corporate/v2/scheduled-payments/{scheduledPaymentId} |
| `WPMT0014` | 400 | Action not permitted on a closed account | Banking_-_Transaction_banking | 4 | POST /cash-management/v2/payments;POST /cash-management/v2/scheduled-payments;POST /corporate/v2/payments |
| `WPMT0015` | 400 | Invalid currency | Banking_-_Transaction_banking | 2 | POST /cash-management/v2/payments;POST /corporate/v2/payments |
| `WPMT0016` | 400 | Cannot perform conversion between account currency and provided currency | Banking_-_Transaction_banking | 2 | POST /cash-management/v2/payments;POST /corporate/v2/payments |
| `WPMT0017` | 400 | Invalid JSON payload received: Error unmarshalling request | Banking_-_Transaction_banking | 8 | POST /cash-management/v2/payments;POST /cash-management/v2/payments/cancel;POST /cash-management/v2/payments/confirm |
| `WPMT0018` | 400 | business_date 24-05-2024 should be formatted as yyyy-mm-dd and be a valid date | Banking_-_Transaction_banking | 9 | GET /corporate/v2/scheduled-payments;POST /cash-management/v2/payments;POST /cash-management/v2/payments/cancel |
| `WPMT0019` | 400 | Cannot use same account for credit and debit | Banking_-_Transaction_banking | 2 | POST /cash-management/v2/payments;POST /corporate/v2/payments |
| `WPMT0021` | 400 | Invalid debit earmark processing code | Banking_-_Transaction_banking | 2 | POST /cash-management/v2/payments;POST /corporate/v2/payments |
| `WPMT0022` | 400 | The account cannot be credited, credit earmark function is not active | Banking_-_Transaction_banking | 2 | POST /cash-management/v2/payments;POST /corporate/v2/payments |
| `WPMT0023` | 400 | The account cannot be debited. Debit earmark function is not active | Banking_-_Transaction_banking | 2 | POST /cash-management/v2/payments;POST /corporate/v2/payments |
| `WPMT0024` | 400 | Force operation not allowed by reason: {reason_description} | Banking_-_Transaction_banking | 2 | POST /cash-management/v2/payments;POST /corporate/v2/payments |
| `WPMT0025` | 400 | Debit not permitted on a closed account | Banking_-_Transaction_banking | 2 | POST /cash-management/v2/payments;POST /corporate/v2/payments |
| `WPMT0026` | 400 | Credit not permitted on a closed account | Banking_-_Transaction_banking | 2 | POST /cash-management/v2/payments;POST /corporate/v2/payments |
| `WPMT0028` | 400 | Invalid business date for the current business day cycle | Banking_-_Transaction_banking | 6 | POST /cash-management/v2/payments;POST /cash-management/v2/payments/cancel;POST /cash-management/v2/payments/confirm |
| `WPMT0029` | 400 | Payment request with conflicting force parameters | Banking_-_Transaction_banking | 2 | POST /cash-management/v2/payments;POST /corporate/v2/payments |
| `WPMT0030` | 400 | Invalid validation rule {validation rule} | Banking_-_Transaction_banking | 2 | POST /cash-management/v2/payments;POST /corporate/v2/payments |
| `WPMT0031` | 400 | Invalid params for validation rule {validation rule} | Banking_-_Transaction_banking | 2 | POST /cash-management/v2/payments;POST /corporate/v2/payments |
| `WPMT0035` | 400 | Future dated payment datetime must be before date limit | Banking_-_Transaction_banking | 2 | POST /cash-management/v2/payments;POST /corporate/v2/payments |
| `WPMT0036` | 400 | Future dated earmark payments are not allowed | Banking_-_Transaction_banking | 2 | POST /cash-management/v2/payments;POST /corporate/v2/payments |
| `WPMT0037` | 404 | original_tracking_id not found | Banking_-_Transaction_banking | 4 | POST /cash-management/v2/payments/cancel;POST /cash-management/v2/payments/confirm;POST /corporate/v2/payments/cancel |
| `WPMT0038` | 400 | transaction is owned by another account | Banking_-_Transaction_banking | 4 | POST /cash-management/v2/payments/cancel;POST /cash-management/v2/payments/confirm;POST /corporate/v2/payments/cancel |
| `WPMT0039` | 400 | transaction cannot be confirmed | Banking_-_Transaction_banking | 4 | POST /cash-management/v2/payments/cancel;POST /cash-management/v2/payments/confirm;POST /corporate/v2/payments/cancel |
| `WPMT0040` | 400 | transaction cannot be canceled | Banking_-_Transaction_banking | 2 | POST /cash-management/v2/payments/cancel;POST /corporate/v2/payments/cancel |
| `WPMT0041` | 400 | earmark internal_operation cannot be canceled | Banking_-_Transaction_banking | 2 | POST /cash-management/v2/payments/cancel;POST /corporate/v2/payments/cancel |
| `WPMT0044` | 400 | Back business dating is disabled | Banking_-_Transaction_banking | 6 | POST /cash-management/v2/payments;POST /cash-management/v2/payments/cancel;POST /cash-management/v2/payments/confirm |
| `WPMT0045` | 400 | Administrative division is misconfigured | Banking_-_Transaction_banking | 2 | POST /cash-management/v2/payments;POST /corporate/v2/payments |
| `WPMT0046` | 400 | The maximum retroactive payment datetime allowed is <days_limit> days | Banking_-_Transaction_banking | 4 | POST /cash-management/v2/payments;POST /cash-management/v2/payments/cancel;POST /corporate/v2/payments |
| `WPMT0047` | 423 | transaction using this tracking_id is in progress, please try again later | Banking_-_Transaction_banking | 6 | POST /cash-management/v2/payments;POST /cash-management/v2/payments/cancel;POST /cash-management/v2/payments/confirm |
| `WPMT0048` | 423 | transaction using this original_tracking_id is in progress, please try again later | Banking_-_Transaction_banking | 4 | POST /cash-management/v2/payments/cancel;POST /cash-management/v2/payments/confirm;POST /corporate/v2/payments/cancel |
| `WPMT0049` | 400 | Transfer operations must be sent by the debit account | Banking_-_Transaction_banking | 6 | POST /cash-management/v2/payments;POST /cash-management/v2/payments/cancel;POST /cash-management/v2/payments/confirm |
| `WPMT0050` | 400 | Payment business date cannot be earlier than the earmark creation date | Banking_-_Transaction_banking | 2 | POST /cash-management/v2/payments;POST /corporate/v2/payments |
| `WPMT0051` | 400 | Operation not allowed by reason: <reason> | Banking_-_Transaction_banking | 2 | POST /cash-management/v2/payments;POST /corporate/v2/payments |
| `WPMT0052` | 409 | tracking_id is already in use | Banking_-_Transaction_banking | 6 | POST /cash-management/v2/payments;POST /cash-management/v2/payments/cancel;POST /cash-management/v2/payments/confirm |
| `WPMT0053` | 400 | Account has not finished onboarding | Banking_-_Transaction_banking | 4 | POST /cash-management/v2/payments;POST /cash-management/v2/scheduled-payments;POST /corporate/v2/payments |
| `WPMT0054` | 400 | Cannot post back value-dated transaction for this division | Banking_-_Transaction_banking | 2 | POST /cash-management/v2/payments;POST /corporate/v2/payments |
| `WPMT0055` | 400 | Cannot post future value-dated transaction for this division | Banking_-_Transaction_banking | 2 | POST /cash-management/v2/payments;POST /corporate/v2/payments |
| `WPMT0056` | 400 | Invalid account currency code: 999 | Banking_-_Transaction_banking | 2 | POST /cash-management/v2/payments;POST /corporate/v2/payments |
| `WPMT0057` | 400 | Cannot instantly cancel when original business date is after the current date | Banking_-_Transaction_banking | 2 | POST /cash-management/v2/payments/cancel;POST /corporate/v2/payments/cancel |
| `WPMT0058` | 400 | Channel not found | Banking_-_Transaction_banking | 2 | POST /cash-management/v2/payments;POST /corporate/v2/payments |
| `WPMT0061` | 400 | The payment date cannot be earlier than the account migration date | Banking_-_Transaction_banking | 6 | POST /cash-management/v2/payments;POST /cash-management/v2/payments/cancel;POST /cash-management/v2/payments/confirm |
| `WPMT0062` | 400 | Authorization failed flex control evaluation | Banking_-_Transaction_banking | 2 | POST /cash-management/v2/payments;POST /corporate/v2/payments |
| `WPMT0063` | 400 | Rates enforcement is not supported for operations with a fee deduction model (deductFromTransactionValue) | Banking_-_Transaction_banking | 2 | POST /cash-management/v2/payments;POST /corporate/v2/payments |

## Lifecycle status

Codes in this unit that are mentioned in changelog posts (check the post: it may record that the code was added, changed or removed from some endpoints):

- `WPMT0001`: `KU-CHG-1-may-2026`
- `WPMT0002`: `KU-CHG-3-april-2026`
- `WPMT0005`: `KU-CHG-3-january-2025`
- `WPMT0006`: `KU-CHG-3-january-2025`
- `WPMT0008`: `KU-CHG-3-april-2026`
- `WPMT0014`: `KU-CHG-3-april-2026`
- `WPMT0018`: `KU-CHG-4-april-2025`
- `WPMT0019`: `KU-CHG-3-april-2026`
- `WPMT0025`: `KU-CHG-3-january-2025`
- `WPMT0026`: `KU-CHG-3-january-2025`
- `WPMT0036`: `KU-CHG-3-january-2025`
- `WPMT0044`: `KU-CHG-7-february-2025`
- `WPMT0045`: `KU-CHG-8-august-2025`
- `WPMT0050`: `KU-CHG-3-january-2025`
- `WPMT0051`: `KU-CHG-7-february-2025`
- `WPMT0054`: `KU-CHG-7-november-2025`
- `WPMT0056`: `KU-CHG-9-january-2026`
- `WPMT0057`: `KU-CHG-9-january-2026`

## Conflicts, caveats and evidence gaps

- Codes and messages come from response examples in the OpenAPI specifications; the conditions that trigger a code are documented only where the message or the operation description states them.
- The source table recognises only codes made of letters followed by digits; codes with mixed prefixes (for example `WP2P0000`) are not in the table but appear in the API-reference KUs.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-reference-data/error_code_index.csv` | rows with code prefix WPMT | https://github.com/PismoDevEx/pismo-api-specs | `76213ae93e90a725…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-API-banking-transaction-banking--payments-part-01` — API reference: Banking - Transaction banking — Payments (part 1 of 3)
- `KU-API-banking-transaction-banking--payments-part-02` — API reference: Banking - Transaction banking — Payments (part 2 of 3)
- `KU-API-banking-transaction-banking--payments-part-03` — API reference: Banking - Transaction banking — Payments (part 3 of 3)
- `KU-API-banking-transaction-banking--payments-pismo-account-id` — API reference: Banking - Transaction banking — Payments (Pismo account ID)
- `KU-API-banking-transaction-banking--transactions` — API reference: Banking - Transaction banking — Transactions
- `KU-CHG-1-may-2026` — Changelog: 1 May 2026
- `KU-CHG-3-april-2026` — Changelog: 3 April 2026
- `KU-CHG-3-january-2025` — Changelog: 3 January 2025
- `KU-CHG-4-april-2025` — Changelog: 4 April 2025
- `KU-CHG-7-february-2025` — Changelog: 7 February 2025
- `KU-CHG-7-november-2025` — Changelog: 7 November 2025
- `KU-CHG-8-august-2025` — Changelog: 8 August 2025
- `KU-CHG-9-january-2026` — Changelog: 9 January 2026
