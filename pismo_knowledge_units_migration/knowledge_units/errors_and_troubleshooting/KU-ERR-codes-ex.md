---
ku_id: KU-ERR-codes-ex
title: 'Error codes: EX'
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
- KU-API-revolving-credit-configurations--additional-accrual-type-configurations
- KU-API-revolving-credit-configurations--features-by-account-status
- KU-API-revolving-credit-delinquency--delinquency
- KU-API-revolving-credit-interest-accruals--accrual-types-minimum-value
- KU-API-revolving-credit-statements--multivalue-program-parameters
- KU-API-revolving-credit-statements--program-transaction-categories
- KU-API-revolving-credit-statements--transaction-types
error_codes:
- EX0001
- EX0002
- EX0004
- EX1101
- EX1102
- EX1103
- EX1104
- EX1105
- EX1106
- EX1107
- EX1108
- EX1109
- EX1110
- EX1200
- EX1201
- EX1203
- EX1301
- EX300
- EX301
- EX302
- EX303
- EX304
- EX305
- EX307
- EX308
---

# Error codes: EX

**KU ID:** `KU-ERR-codes-ex` · **Category:** Errors and troubleshooting · **Type:** error-code catalogue (from reference table)

## Purpose and scope

25 error code(s) with prefix(es) EX from `api-reference-data/error_code_index.csv`, with the HTTP status, message and the operations whose response examples contain the code. The `operations_sample` column is a sample, not a complete list: the complete set of codes per operation is in the API-reference KUs (section “Error codes shown in this operation's response examples”). Conditions under which a code is returned are documented only where the message or the operation description states them.

## Error codes

| Code | HTTP status | Message | Specification files | Operation count | Operations (sample) |
| --- | --- | --- | --- | --- | --- |
| `EX0001` | 400;404 | Validation Error. Details: Can't find [BalanceAccount] with params: [AccountID: XXXXXX, OrgID: TN-XXXXXXXXXXX-XXXX-XXXX-XXXXXXXXXX]. | Revolving_credit_-_Configurations;Revolving_credit_-_Interest_accruals;Revolving_credit_-_Statements | 14 | DELETE /v1/accrual-type-minimum-value;GET /statements-v2/v1/programs-transactions-types;GET /statements-v2/v1/transactions-categories |
| `EX0002` | 400 | Missing request header for method parameter of type String | Revolving_credit_-_Calendar_management;Revolving_credit_-_Configurations;Revolving_credit_-_Delinquency;Revolving_credit_-_Installment_management;Revolving_credit_-_Statement_refinancing_API;Revolving_credit_-_Statements | 5 | GET /statements-v2/v1/programs/{programId}/parameters/{parameterId};GET /v1/accounts/{accountId}/buckets;GET /v1/accounts/{accountId}/buckets/{delinquencyBucketId} |
| `EX0004` | 404 | Validation Error: The transaction category XXXXXXXX does not exist or does not belong to the provided program. | Revolving_credit_-_Configurations | 3 | DELETE /v1/programs/{programId}/transaction-category-id/{transactionCategoryId}/accrual-type/{accrualType}/period-to-calculate/{periodToCalculate}/configurations;GET /v1/features-by-account-status;POST /v1/programs/{programId}/transaction-category-id/{transactionCategoryId}/accrual-type/{accrualType}/period-to-calculate/{periodToCalculate}/configurations |
| `EX1101` | not stated | Field every_x_months must be between 1 and 12. | Revolving_credit_-_Calendar_management | 0 |  |
| `EX1102` | not stated | Fields cycle_closing_day and nth_specific_weekday are mutually exclusive. | Revolving_credit_-_Calendar_management | 0 |  |
| `EX1103` | not stated | Either cycle_closing_day or nth_specific_weekday must be provided. | Revolving_credit_-_Calendar_management | 0 |  |
| `EX1104` | not stated | Field day_of_week is required. | Revolving_credit_-_Calendar_management | 0 |  |
| `EX1105` | not stated | Field day_of_week must be a valid day of the week. | Revolving_credit_-_Calendar_management | 0 |  |
| `EX1106` | not stated | Field week_of_month is required. | Revolving_credit_-_Calendar_management | 0 |  |
| `EX1107` | not stated | Field week_of_month must be between 1 and 5. | Revolving_credit_-_Calendar_management | 0 |  |
| `EX1108` | not stated | Fields due_day and nth_specific_weekday are mutually exclusive. | Revolving_credit_-_Calendar_management | 0 |  |
| `EX1109` | not stated | Either due_day or nth_specific_weekday must be provided. | Revolving_credit_-_Calendar_management | 0 |  |
| `EX1110` | not stated | Field due_day must be between 1 and 28. | Revolving_credit_-_Calendar_management | 0 |  |
| `EX1200` | not stated | Field day_of_week is required. | Revolving_credit_-_Calendar_management | 0 |  |
| `EX1201` | not stated | Field day_of_week must be a valid day of the week (MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY). | Revolving_credit_-_Calendar_management | 0 |  |
| `EX1203` | not stated | Field every_x_weeks must be between 1 and 52. | Revolving_credit_-_Calendar_management | 0 |  |
| `EX1301` | not stated | Field every_x_days must be between 1 and 365. | Revolving_credit_-_Calendar_management | 0 |  |
| `EX300` | not stated | Another strategy has the same configuration. | Revolving_credit_-_Calendar_management | 0 |  |
| `EX301` | not stated | Calendar strategy not found. | Revolving_credit_-_Calendar_management | 0 |  |
| `EX302` | not stated | Field configuration is invalid. | Revolving_credit_-_Calendar_management | 0 |  |
| `EX303` | not stated | Field cycle_closing_day must be between 1 and 28. | Revolving_credit_-_Calendar_management | 0 |  |
| `EX304` | not stated | Field cycle_closing_day is required. | Revolving_credit_-_Calendar_management | 0 |  |
| `EX305` | not stated | Field days_between_cycle_closing_and_due_date is required. | Revolving_credit_-_Calendar_management | 0 |  |
| `EX307` | not stated | Field days_between_cycle_closing_and_due_date must be between 1 and 100. | Revolving_credit_-_Calendar_management;Revolving_credit_-_Installment_management | 0 |  |
| `EX308` | not stated | To proceed with this operation, please provide either the configuration update, the active flag, or both. | Revolving_credit_-_Calendar_management | 0 |  |

## Lifecycle status

- No code in this unit is mentioned in a changelog post.

## Conflicts, caveats and evidence gaps

- Codes and messages come from response examples in the OpenAPI specifications; the conditions that trigger a code are documented only where the message or the operation description states them.
- The source table recognises only codes made of letters followed by digits; codes with mixed prefixes (for example `WP2P0000`) are not in the table but appear in the API-reference KUs.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-reference-data/error_code_index.csv` | rows with code prefix EX | https://github.com/PismoDevEx/pismo-api-specs | `76213ae93e90a725…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-API-revolving-credit-configurations--additional-accrual-type-configurations` — API reference: Revolving credit - Configurations — Additional accrual type configurations
- `KU-API-revolving-credit-configurations--features-by-account-status` — API reference: Revolving credit - Configurations — Features by account status
- `KU-API-revolving-credit-delinquency--delinquency` — API reference: Revolving credit - Delinquency — Delinquency
- `KU-API-revolving-credit-interest-accruals--accrual-types-minimum-value` — API reference: Revolving credit - Interest accruals — Accrual types minimum value
- `KU-API-revolving-credit-statements--multivalue-program-parameters` — API reference: Revolving credit - Statements — Multivalue program parameters
- `KU-API-revolving-credit-statements--program-transaction-categories` — API reference: Revolving credit - Statements — Program transaction categories
- `KU-API-revolving-credit-statements--transaction-types` — API reference: Revolving credit - Statements — Transaction types
