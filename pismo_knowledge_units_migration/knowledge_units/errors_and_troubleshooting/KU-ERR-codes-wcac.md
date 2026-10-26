---
ku_id: KU-ERR-codes-wcac
title: 'Error codes: WCAC'
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
- KU-API-banking-transaction-banking--dormancy
- KU-API-banking-transaction-banking--payments-part-01
- KU-API-banking-transaction-banking--payments-part-02
- KU-API-banking-transaction-banking--payments-part-03
- KU-API-banking-transaction-banking--payments-pismo-account-id
- KU-API-banking-transaction-banking--register-banking-account
- KU-API-banking-transaction-banking--transactions
- KU-CHG-2-october-2026
- KU-CHG-3-april-2026
- KU-CHG-5-december-2025
- KU-CHG-8-august-2025
error_codes:
- WCAC0001
- WCAC0002
- WCAC0004
- WCAC0005
- WCAC0006
- WCAC0009
- WCAC0010
- WCAC0011
- WCAC0012
- WCAC0013
- WCAC0014
- WCAC0016
- WCAC0018
- WCAC0019
- WCAC0020
- WCAC0021
- WCAC0023
- WCAC0026
- WCAC0027
- WCAC0028
- WCAC0029
- WCAC0031
- WCAC0032
- WCAC0033
- WCAC0034
- WCAC0035
- WCAC0036
- WCAC0037
- WCAC0038
- WCAC0040
- WCAC0041
- WCAC0042
- WCAC0043
- WCAC0045
---

# Error codes: WCAC

**KU ID:** `KU-ERR-codes-wcac` · **Category:** Errors and troubleshooting · **Type:** error-code catalogue (from reference table)

## Purpose and scope

34 error code(s) with prefix(es) WCAC from `api-reference-data/error_code_index.csv`, with the HTTP status, message and the operations whose response examples contain the code. The `operations_sample` column is a sample, not a complete list: the complete set of codes per operation is in the API-reference KUs (section “Error codes shown in this operation's response examples”). Conditions under which a code is returned are documented only where the message or the operation description states them.

## Error codes

| Code | HTTP status | Message | Specification files | Operation count | Operations (sample) |
| --- | --- | --- | --- | --- | --- |
| `WCAC0001` | 400;401 | Account not authorized | Banking_-_Transaction_banking | 15 | DELETE /corporate/v2/scheduled-payments/{scheduledPaymentId};GET /corporate/v1/account-dormancy/{externalAccountId};GET /corporate/v1/corporate-transactions |
| `WCAC0002` | 400 | Invalid header account | Banking_-_Transaction_banking | 4 | GET /corporate/v1/account-dormancy/{externalAccountId};POST /cash-management/v2/payments;POST /corporate/v1/corporate-accounts/{externalAccountId}/force-close |
| `WCAC0004` | 400 | schema validation error: [validation description] | Banking_-_Transaction_banking | 2 | PATCH /corporate/v1/corporate-accounts/{externalAccountId};POST /corporate/v1/corporate-accounts |
| `WCAC0005` | 400 | account_creation_datetime should be formatted as yyyy-mm-ddThh:mm:ss.sssZ and be a valid datetime | Banking_-_Transaction_banking | 5 | PATCH /corporate/v1/corporate-accounts/{externalAccountId};PATCH /corporate/v1/corporate-accounts/{externalAccountId}/entity;PATCH /corporate/v2/corporate-accounts/{externalAccountId}/status |
| `WCAC0006` | 400 | Program not bound to Division | Banking_-_Transaction_banking | 3 | PATCH /corporate/v1/corporate-accounts/{externalAccountId};POST /corporate/v1/corporate-accounts;POST /corporate/v2/corporate-accounts/register |
| `WCAC0009` | 400 | generic message | Banking_-_Transaction_banking | 1 | POST /corporate/v1/corporate-accounts |
| `WCAC0010` | 400 | Token contains an unrecognized account ID type | Banking_-_Transaction_banking | 3 | DELETE /corporate/v2/scheduled-payments/{scheduledPaymentId};POST /corporate/v2/payments;POST /corporate/v2/scheduled-payments |
| `WCAC0011` | 409 | Duplicated external_account_id | Banking_-_Transaction_banking | 2 | POST /corporate/v1/corporate-accounts;POST /corporate/v2/corporate-accounts/register |
| `WCAC0012` | 400 | Corporate account not found | Banking_-_Transaction_banking | 10 | GET /corporate/v1/corporate-accounts/{externalAccountId};PATCH /corporate/v1/corporate-accounts/{externalAccountId};PATCH /corporate/v1/corporate-accounts/{externalAccountId}/entity |
| `WCAC0013` | 400 | Invalid JSON payload received: Error unmarshalling request. | Banking_-_Transaction_banking | 5 | PATCH /corporate/v1/corporate-accounts/{externalAccountId};PATCH /corporate/v1/corporate-accounts/{externalAccountId}/entity;PATCH /corporate/v2/corporate-accounts/{externalAccountId}/status |
| `WCAC0014` | 409 | Duplicate corporate account | Banking_-_Transaction_banking | 1 | POST /corporate/v1/corporate-accounts |
| `WCAC0016` | 400 | parent_account_id informed as Parent Account not exists | Banking_-_Transaction_banking | 1 | POST /corporate/v1/corporate-accounts |
| `WCAC0018` | 400 | Account still has active scheduled payments | Banking_-_Transaction_banking | 1 | POST /corporate/v1/corporate-accounts/{externalAccountId}/close |
| `WCAC0019` | 400 | Make sure that the account has a zero balance before closing it | Banking_-_Transaction_banking | 1 | POST /corporate/v1/corporate-accounts/{externalAccountId}/close |
| `WCAC0020` | 400;404 | Status not found | Banking_-_Transaction_banking | 2 | PATCH /corporate/v2/corporate-accounts/{externalAccountId}/status;PATCH /corporate/v2/corporate-accounts/{externalAccountId}/status/rollback |
| `WCAC0021` | 404 | Reason not found | Banking_-_Transaction_banking | 2 | PATCH /corporate/v2/corporate-accounts/{externalAccountId}/status;PATCH /corporate/v2/corporate-accounts/{externalAccountId}/status/rollback |
| `WCAC0023` | 404 | Account balance not found | Banking_-_Transaction_banking | 1 | GET /corporate/v1/corporate-accounts/{externalAccountId} |
| `WCAC0026` | 409 | This document number is already associated with the owner of this account | Banking_-_Transaction_banking | 1 | PATCH /corporate/v1/corporate-accounts/{externalAccountId}/entity |
| `WCAC0027` | 409 | This document number is associated with an inactive customer | Banking_-_Transaction_banking | 1 | PATCH /corporate/v1/corporate-accounts/{externalAccountId}/entity |
| `WCAC0028` | 400 | Account has active earmark | Banking_-_Transaction_banking | 1 | POST /corporate/v1/corporate-accounts/{externalAccountId}/close |
| `WCAC0029` | 400 | Action not permitted on a closed account | Banking_-_Transaction_banking | 2 | PATCH /corporate/v1/corporate-accounts/{externalAccountId}/entity;POST /corporate/v1/corporate-accounts/{externalAccountId}/close |
| `WCAC0031` | 400 | This program migration is not permitted. The programs currency must be the same type | Banking_-_Transaction_banking | 1 | PATCH /corporate/v1/corporate-accounts/{externalAccountId} |
| `WCAC0032` | 400 | This program migration is not permitted. The programs must be the same type | Banking_-_Transaction_banking | 1 | PATCH /corporate/v1/corporate-accounts/{externalAccountId} |
| `WCAC0033` | 400 | There are no attributes to update. | Banking_-_Transaction_banking | 1 | PATCH /corporate/v1/corporate-accounts/{externalAccountId} |
| `WCAC0034` | 400 | status is specified in account's dormancy config | Banking_-_Transaction_banking | 2 | PATCH /corporate/v2/corporate-accounts/{externalAccountId}/status;PATCH /corporate/v2/corporate-accounts/{externalAccountId}/status/rollback |
| `WCAC0035` | 400 | Account is currently in the final status | Banking_-_Transaction_banking | 2 | PATCH /corporate/v2/corporate-accounts/{externalAccountId}/status;POST /corporate/v1/corporate-accounts/{externalAccountId}/close |
| `WCAC0036` | 400 | status cannot be final | Banking_-_Transaction_banking | 2 | PATCH /corporate/v2/corporate-accounts/{externalAccountId}/status;PATCH /corporate/v2/corporate-accounts/{externalAccountId}/status/rollback |
| `WCAC0037` | 400 | account is not currently in the final status | Banking_-_Transaction_banking | 1 | PATCH /corporate/v2/corporate-accounts/{externalAccountId}/status/rollback |
| `WCAC0038` | 422 | Account status update blocked: operation blocked for account. | Banking_-_Transaction_banking | 2 | PATCH /corporate/v2/corporate-accounts/{externalAccountId}/status;PATCH /corporate/v2/corporate-accounts/{externalAccountId}/status/rollback |
| `WCAC0040` | 400 | Account balance is still being created. Please try again in a few minutes | Banking_-_Transaction_banking | 1 | POST /corporate/v1/corporate-accounts/{externalAccountId}/close |
| `WCAC0041` | 404 | Account not found in accounts-core | Banking_-_Transaction_banking | 1 | POST /corporate/v2/corporate-accounts/register |
| `WCAC0042` | 422 | Account has not completed the creation process | Banking_-_Transaction_banking | 1 | POST /corporate/v2/corporate-accounts/register |
| `WCAC0043` | 422 | Program type CREDITO cannot be registered | Banking_-_Transaction_banking | 1 | POST /corporate/v2/corporate-accounts/register |
| `WCAC0045` | 422 | Account onboarding has not been completed yet. The account cannot be closed. | Banking_-_Transaction_banking | 1 | POST /corporate/v1/corporate-accounts/{externalAccountId}/close |

## Lifecycle status

Codes in this unit that are mentioned in changelog posts (check the post: it may record that the code was added, changed or removed from some endpoints):

- `WCAC0002`: `KU-CHG-3-april-2026`
- `WCAC0005`: `KU-CHG-2-october-2026`
- `WCAC0012`: `KU-CHG-3-april-2026`
- `WCAC0035`: `KU-CHG-8-august-2025`
- `WCAC0040`: `KU-CHG-5-december-2025`

## Conflicts, caveats and evidence gaps

- Codes and messages come from response examples in the OpenAPI specifications; the conditions that trigger a code are documented only where the message or the operation description states them.
- The source table recognises only codes made of letters followed by digits; codes with mixed prefixes (for example `WP2P0000`) are not in the table but appear in the API-reference KUs.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-reference-data/error_code_index.csv` | rows with code prefix WCAC | https://github.com/PismoDevEx/pismo-api-specs | `76213ae93e90a725…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-API-banking-transaction-banking--accounts` — API reference: Banking - Transaction banking — Accounts
- `KU-API-banking-transaction-banking--dormancy` — API reference: Banking - Transaction banking — Dormancy
- `KU-API-banking-transaction-banking--payments-part-01` — API reference: Banking - Transaction banking — Payments (part 1 of 3)
- `KU-API-banking-transaction-banking--payments-part-02` — API reference: Banking - Transaction banking — Payments (part 2 of 3)
- `KU-API-banking-transaction-banking--payments-part-03` — API reference: Banking - Transaction banking — Payments (part 3 of 3)
- `KU-API-banking-transaction-banking--payments-pismo-account-id` — API reference: Banking - Transaction banking — Payments (Pismo account ID)
- `KU-API-banking-transaction-banking--register-banking-account` — API reference: Banking - Transaction banking — Register banking account
- `KU-API-banking-transaction-banking--transactions` — API reference: Banking - Transaction banking — Transactions
- `KU-CHG-2-october-2026` — Changelog: 2 October 2026
- `KU-CHG-3-april-2026` — Changelog: 3 April 2026
- `KU-CHG-5-december-2025` — Changelog: 5 December 2025
- `KU-CHG-8-august-2025` — Changelog: 8 August 2025
