---
ku_id: KU-ERR-codes-wiac-to-wstm
title: 'Error codes: WIAC to WSTM (9 prefixes)'
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
- KU-API-banking-transaction-banking--bulk-settlement
- KU-API-banking-transaction-banking--earmarking-pismo-account-id
- KU-API-banking-transaction-banking--operations-blocks
- KU-API-banking-transaction-banking--payments-part-02
- KU-API-banking-transaction-banking--restricted-funds
- KU-API-core-platform-balances-and-limits--account-limits
- KU-API-core-platform-ledger--account-limits
- KU-API-core-platform-payment-methods--force-operations
- KU-API-core-platform-payment-methods--installments-payments
- KU-API-core-platform-payment-methods--payment-methods-part-01
- KU-API-core-platform-payment-methods--payment-methods-part-02
- KU-API-core-platform-payment-methods--payments
- KU-API-lending--repayment-hierarchy
- KU-API-revolving-credit-interest-accruals--post-interest-accruals
- KU-CHG-8-august-2025
- KU-CHG-9-january-2026
error_codes:
- WIAC0002
- WIAC0003
- WIAC0005
- WLDG0004
- WLDG0005
- WLDG0006
- WLDG0010
- WLDG0019
- WLDG0020
- WLDG0021
- WLDG0022
- WLDG0025
- WLND0001
- WOBK0001
- WOBK0002
- WOBK0003
- WOBK0004
- WOBK0005
- WOBK0006
- WOBK0007
- WOBK0008
- WOBK0009
- WONB0001
- WONP0001
- WONP0010
- WRAT00001
- WRUL0707
- WRUL1207
- WSTM0001
- WSTM0002
- WSTM0003
- WSTM0004
- WSTM0005
- WSTM0006
- WSTM0007
- WSTM0008
- WSTM0009
- WSTM0010
- WSTM0011
---

# Error codes: WIAC to WSTM (9 prefixes)

**KU ID:** `KU-ERR-codes-wiac-to-wstm` · **Category:** Errors and troubleshooting · **Type:** error-code catalogue (from reference table)

## Purpose and scope

39 error code(s) with prefix(es) WIAC, WLDG, WLND, WOBK, WONB, WONP, WRAT, WRUL, WSTM from `api-reference-data/error_code_index.csv`, with the HTTP status, message and the operations whose response examples contain the code. The `operations_sample` column is a sample, not a complete list: the complete set of codes per operation is in the API-reference KUs (section “Error codes shown in this operation's response examples”). Conditions under which a code is returned are documented only where the message or the operation description states them.

## Error codes

| Code | HTTP status | Message | Specification files | Operation count | Operations (sample) |
| --- | --- | --- | --- | --- | --- |
| `WIAC0002` | 404 | There are no accruals to be posted. | Revolving_credit_-_Interest_accruals | 1 | POST /v1/accounts/{accountId}/interest-accruals |
| `WIAC0003` | 422 | There are no processing codes configured to post the accrual types [XXXX, YYYYY, ZZZZZ]. | Revolving_credit_-_Interest_accruals | 1 | POST /v1/accounts/{accountId}/interest-accruals |
| `WIAC0005` | 403 | The use of processing_code_fine is only allowed for accrual_type OVERDUE | Revolving_credit_-_Interest_accruals | 1 | POST /v1/accounts/{accountId}/interest-accruals |
| `WLDG0004` | 404 | No AvailableIntegrity found | Core_platform_-_Payment_methods | 1 | POST /payments/v2/cancel |
| `WLDG0005` | 404 | No Available Entries found | Core_platform_-_Payment_methods | 1 | POST /payments/v2/cancel |
| `WLDG0006` | 400;404 | No AvailableCreditLimit to complete the transaction - amount: 15, availableCreditLimit: -121.07 | Core_platform_-_Payment_methods | 3 | POST /payments/v1/payments;POST /payments/v1/payments/installments;POST /payments/v2/cancel |
| `WLDG0010` | 400 | Error when binding request body: code=400, message=error decoding string 'asd': can't convert asd to decimal | Core_platform_-_Ledger | 1 | PATCH /v1/accounts/{accountId}/limits |
| `WLDG0019` | 400;404 | No Accounts authorization found. | Core_platform_-_Payment_methods | 3 | POST /payments/v1/payments;POST /payments/v1/payments/installments;POST /payments/v2/cancel |
| `WLDG0020` | 400 | Error parsing accountID to integer number | Core_platform_-_Ledger | 1 | GET /v1/accounts/{accountId}/limits |
| `WLDG0021` | 400 | Error when parsing the beginDate and/or endDate | Core_platform_-_Balances_and_limits;Core_platform_-_Ledger | 1 | PATCH /v1/accounts/{accountId}/limits |
| `WLDG0022` | 404 | No account limits found | Core_platform_-_Ledger | 2 | GET /v1/accounts/{accountId}/limits;PATCH /v1/accounts/{accountId}/limits |
| `WLDG0025` | 400 | Max credit limit 9000 must be greater than total credit limit 10000 | Core_platform_-_Ledger | 1 | PATCH /v1/accounts/{accountId}/limits |
| `WLND0001` | 202 | idempotency-key already in use | Lending | 1 | POST /v2/repayment-hierarchies |
| `WOBK0001` | 400 | Invalid JSON payload received: Error unmarshalling request | Banking_-_Transaction_banking | 1 | POST /corporate/v2/operations-blocks |
| `WOBK0002` | 400 | description or allowed_operations must be provided | Banking_-_Transaction_banking | 1 | PATCH /corporate/v2/operations-blocks/{operationsBlockId} |
| `WOBK0003` | 400 | Division not found | Banking_-_Transaction_banking | 1 | POST /corporate/v2/operations-blocks |
| `WOBK0004` | 400 | Program not found | Banking_-_Transaction_banking | 1 | POST /corporate/v2/operations-blocks |
| `WOBK0005` | 400 | Invalid id parameter | Banking_-_Transaction_banking | 2 | DELETE /corporate/v2/operations-blocks/{operationsBlockId};PATCH /corporate/v2/operations-blocks/{operationsBlockId} |
| `WOBK0006` | 404 | Operation block not found | Banking_-_Transaction_banking | 3 | DELETE /corporate/v2/operations-blocks/{operationsBlockId};GET /corporate/v2/operations-blocks/{operationsBlockId};PATCH /corporate/v2/operations-blocks/{operationsBlockId} |
| `WOBK0007` | 200;400 | Operations blocked for account | Banking_-_Transaction_banking | 18 | GET /corporate/v3/payments/multileg/{multilegId};PATCH /cash-management/v2/earmarks/{earmarkId};PATCH /corporate/v1/restricted-funds/{restrictedFundsId} |
| `WOBK0008` | 409 | Operations block already exists | Banking_-_Transaction_banking | 1 | POST /corporate/v2/operations-blocks |
| `WOBK0009` | 400 | Operation block is not active | Banking_-_Transaction_banking | 2 | DELETE /corporate/v2/operations-blocks/{operationsBlockId};PATCH /corporate/v2/operations-blocks/{operationsBlockId} |
| `WONB0001` | 400 | Authorized account is different from the request. | Core_platform_-_Payment_methods | 2 | POST /payment-methods/v2/payments;POST /payment-methods/v2/transfers |
| `WONP0001` | 400 | Payload is invalid. It must be a valid JSON. | Core_platform_-_Payment_methods | 4 | POST /payment-methods/v2/payments;POST /payment-methods/v2/payments/cancel;POST /payment-methods/v2/transfers |
| `WONP0010` | 400 | Original authorization cannot be confirmed. | Core_platform_-_Payment_methods | 1 | POST /payment-methods/v2/payments/confirm |
| `WRAT00001` | 400 | Cannot perform calculations | Core_platform_-_Payment_methods | 1 | POST /payments/v1/payments/force |
| `WRUL0707` | not stated | Maximum number of account flex controls reached - 200. | Core_platform_-_Flex_controls | 0 |  |
| `WRUL1207` | not stated | Maximum number of customer flex controls reached - 200. | Core_platform_-_Flex_controls | 0 |  |
| `WSTM0001` | 400 | Invalid JSON payload received: Error unmarshalling request | Banking_-_Transaction_banking | 1 | POST /corporate/v1/bulk-settlement |
| `WSTM0002` | 400 | settlement_date 07/15/2024 should be formatted as yyyy-mm-dd and be a valid date | Banking_-_Transaction_banking | 1 | POST /corporate/v1/bulk-settlement |
| `WSTM0003` | 400 | Settlement date cannot be a future date | Banking_-_Transaction_banking | 1 | POST /corporate/v1/bulk-settlement |
| `WSTM0004` | 400 | Current date can be the same as settlement date only after 00:15 in the division's time zone | Banking_-_Transaction_banking | 1 | POST /corporate/v1/bulk-settlement |
| `WSTM0005` | 400 | Division not found | Banking_-_Transaction_banking | 1 | POST /corporate/v1/bulk-settlement |
| `WSTM0006` | 400 | Settlement date must be a valid date in ISO 8601 format | Banking_-_Transaction_banking | 1 | POST /corporate/v1/bulk-settlement |
| `WSTM0007` | 409 | Bulk settlement already posted with parameters division code [division], settlement date [date] and type [type] | Banking_-_Transaction_banking | 1 | POST /corporate/v1/bulk-settlement |
| `WSTM0008` | 429 | You cannot post more than 10 daily bulk settlements | Banking_-_Transaction_banking | 1 | POST /corporate/v1/bulk-settlement |
| `WSTM0009` | 409 | Bulk id [id] is already in use | Banking_-_Transaction_banking | 1 | POST /corporate/v1/bulk-settlement |
| `WSTM0010` | 400 | Bulk settlement for the current date is allowed only after {hour}:{minute}, according to the division’s time zone | Banking_-_Transaction_banking | 1 | POST /corporate/v1/bulk-settlement |
| `WSTM0011` | 400 | Administrative division is misconfigured | Banking_-_Transaction_banking | 1 | POST /corporate/v1/bulk-settlement |

## Lifecycle status

Codes in this unit that are mentioned in changelog posts (check the post: it may record that the code was added, changed or removed from some endpoints):

- `WOBK0009`: `KU-CHG-9-january-2026`
- `WSTM0010`: `KU-CHG-8-august-2025`
- `WSTM0011`: `KU-CHG-8-august-2025`

## Conflicts, caveats and evidence gaps

- Codes and messages come from response examples in the OpenAPI specifications; the conditions that trigger a code are documented only where the message or the operation description states them.
- The source table recognises only codes made of letters followed by digits; codes with mixed prefixes (for example `WP2P0000`) are not in the table but appear in the API-reference KUs.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-reference-data/error_code_index.csv` | rows with code prefix WIAC, WLDG, WLND, WOBK, WONB, WONP, WRAT, WRUL, WSTM | https://github.com/PismoDevEx/pismo-api-specs | `76213ae93e90a725…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-API-banking-transaction-banking--bulk-settlement` — API reference: Banking - Transaction banking — Bulk settlement
- `KU-API-banking-transaction-banking--earmarking-pismo-account-id` — API reference: Banking - Transaction banking — Earmarking (Pismo account ID)
- `KU-API-banking-transaction-banking--operations-blocks` — API reference: Banking - Transaction banking — Operations blocks
- `KU-API-banking-transaction-banking--payments-part-02` — API reference: Banking - Transaction banking — Payments (part 2 of 3)
- `KU-API-banking-transaction-banking--restricted-funds` — API reference: Banking - Transaction banking — Restricted funds
- `KU-API-core-platform-balances-and-limits--account-limits` — API reference: Core platform - Balances and limits — Account limits
- `KU-API-core-platform-ledger--account-limits` — API reference: Core platform - Ledger — Account limits
- `KU-API-core-platform-payment-methods--force-operations` — API reference: Core platform - Payment methods — Force operations
- `KU-API-core-platform-payment-methods--installments-payments` — API reference: Core platform - Payment methods — Installments payments
- `KU-API-core-platform-payment-methods--payment-methods-part-01` — API reference: Core platform - Payment methods — Payment methods (part 1 of 3)
- `KU-API-core-platform-payment-methods--payment-methods-part-02` — API reference: Core platform - Payment methods — Payment methods (part 2 of 3)
- `KU-API-core-platform-payment-methods--payments` — API reference: Core platform - Payment methods — Payments
- `KU-API-lending--repayment-hierarchy` — API reference: Lending — Repayment hierarchy
- `KU-API-revolving-credit-interest-accruals--post-interest-accruals` — API reference: Revolving credit - Interest accruals — Post interest accruals
- `KU-CHG-8-august-2025` — Changelog: 8 August 2025
- `KU-CHG-9-january-2026` — Changelog: 9 January 2026
