---
ku_id: KU-ERR-codes-elnd
title: 'Error codes: ELND'
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
- KU-API-lending--disbursements
- KU-API-lending--early-final-settlement
- KU-API-lending--loan-products
- KU-API-lending--loans
- KU-API-lending--prepayment
- KU-API-lending--repayment-hierarchy
- KU-API-lending--repayments
error_codes:
- ELND0001
- ELND0002
- ELND0003
- ELND0004
- ELND0005
- ELND0010
- ELND0011
- ELND0012
- ELND0320
- ELND0350
- ELND0351
- ELND0352
- ELND0353
- ELND0354
- ELND0355
- ELND0356
- ELND0357
- ELND0358
- ELND0359
- ELND0360
- ELND0361
- ELND0362
- ELND0363
- ELND0366
- ELND0369
- ELND0376
- ELND0379
- ELND0380
- ELND0400
- ELND0401
- ELND0402
- ELND0403
- ELND0404
- ELND0405
- ELND0406
- ELND0500
- ELND0504
- ELND0509
- ELND0511
- ELND0512
- ELND0513
- ELND0514
- ELND0515
- ELND0549
- ELND0550
- ELND0551
- ELND0601
- ELND0603
- ELND0605
- ELND0606
- ELND0607
- ELND0608
- ELND1501
- ELND1802
- ELND1803
- ELND1804
- ELND1807
- ELND1808
- ELND1809
- ELND2000
- ELND2106
- ELND2107
- ELND2300
- ELND2301
- ELND2302
- ELND2303
- ELND2304
- ELND2305
- ELND3000
---

# Error codes: ELND

**KU ID:** `KU-ERR-codes-elnd` · **Category:** Errors and troubleshooting · **Type:** error-code catalogue (from reference table)

## Purpose and scope

69 error code(s) with prefix(es) ELND from `api-reference-data/error_code_index.csv`, with the HTTP status, message and the operations whose response examples contain the code. The `operations_sample` column is a sample, not a complete list: the complete set of codes per operation is in the API-reference KUs (section “Error codes shown in this operation's response examples”). Conditions under which a code is returned are documented only where the message or the operation description states them.

## Error codes

| Code | HTTP status | Message | Specification files | Operation count | Operations (sample) |
| --- | --- | --- | --- | --- | --- |
| `ELND0001` | 500 | Unexpected error | Lending | 18 | DELETE /v2/loan-products/{productId};GET /v2/loan-products;GET /v2/loan-products/{productId} |
| `ELND0002` | 400;403 | Unauthorized access. Invalid credentials. | Lending | 7 | DELETE /v2/loan-products/{productId};GET /v2/loan-products;GET /v2/loan-products/{productId} |
| `ELND0003` | 400 | disbursement_account.account_type not valid | Lending | 4 | GET /v2/loans/{loanId};POST /v2/loans/{loanId}/disburse;POST /v2/loans/{loanId}/repayment |
| `ELND0004` | 400 | Authorization failed | Lending | 4 | POST /v2/loans;POST /v2/loans/{loanId}/cancel;POST /v2/loans/{loanId}/disburse |
| `ELND0005` | 400;404 | Repayment hierarchy not found | Lending | 10 | DELETE /v2/loan-products/{productId};GET /v2/loan-products;GET /v2/loan-products/{productId} |
| `ELND0010` | 400 | Header idempotency-key not passed | Lending | 2 | POST /v2/accounts/{accountId}/loans/cancel;POST /v2/loans/{loanId}/cancel |
| `ELND0011` | 400 | %s %s not valid for Disbursement Method %s | Lending | 1 | POST /v2/loan-products |
| `ELND0012` | 400 | %s %s not valid. Allowed values : %s | Lending | 1 | POST /v2/loan-products |
| `ELND0320` | 400 | product_id contains invalid characters | Lending | 1 | DELETE /v2/loan-products/{productId} |
| `ELND0350` | 400 | Field processing_codes not passed | Lending | 1 | POST /v2/loan-products |
| `ELND0351` | 400 | Field processing_codes.booking not passed | Lending | 1 | POST /v2/loan-products |
| `ELND0352` | 400 | Field processing_codes.booking must be defined between 2 and 6 | Lending | 2 | PATCH /v2/loan-products/{productId};POST /v2/loan-products |
| `ELND0353` | 400 | Field processing_codes.repayment not passed | Lending | 1 | POST /v2/loan-products |
| `ELND0354` | 400 | Field processing_codes.repayment must be defined between 2 and 6 | Lending | 2 | PATCH /v2/loan-products/{productId};POST /v2/loan-products |
| `ELND0355` | 400 | Field processing_codes.prepayment_discount must be defined between 2 and 6 | Lending | 1 | POST /v2/loan-products |
| `ELND0356` | 400 | Field processing_codes.penalty_accruals must be defined between 2 and 6 | Lending | 1 | POST /v2/loan-products |
| `ELND0357` | 400 | Field processing_codes.penalty_waiver must be defined between 2 and 6 | Lending | 1 | POST /v2/loan-products |
| `ELND0358` | 400 | Field processing_codes.insurance.booking must be defined between 2 and 6 | Lending | 1 | POST /v2/loan-products |
| `ELND0359` | 400 | Field processing_codes.insurance.repayment must be defined between 2 and 6 | Lending | 1 | POST /v2/loan-products |
| `ELND0360` | 400 | Processing code PC_BOOKING already in use by product id 5770c974-dcd5-4a53-b19e-08078a8cb65d, and operation Booking | Lending | 2 | PATCH /v2/loan-products/{productId};POST /v2/loan-products |
| `ELND0361` | 400 | The processing code must be unique for each operation. | Lending | 1 | POST /v2/loan-products |
| `ELND0362` | 400 | Processing code %s is not linked to transactions types. | Lending | 1 | POST /v2/loan-products |
| `ELND0363` | 400 | Processing code %s is invalid or does not exist. | Lending | 1 | POST /v2/loan-products |
| `ELND0366` | 400 | Interest plan PLAN1 not found | Lending | 1 | PATCH /v2/loan-products/{productId} |
| `ELND0369` | 400 | Processing codes list must have at most 20 items. | Lending | 1 | PATCH /v2/loan-products/{productId} |
| `ELND0376` | 400 | Field minimum_total_payment must be positive | Lending | 1 | PATCH /v2/loan-products/{productId} |
| `ELND0379` | 400 | Field max_backdating_window_days can only be set when backdating_enabled is true | Lending | 2 | PATCH /v2/loan-products/{productId};POST /v2/loan-products |
| `ELND0380` | 400 | Field processing_codes.present_value_discount is required when bring_to_present_value_on_delinquency is true. | Lending | 2 | PATCH /v2/loan-products/{productId};POST /v2/loan-products |
| `ELND0400` | 400 | Loan must be active to perform this action. | Lending | 2 | POST /v2/loans/{loanId}/early-settlement/simulate;POST /v2/loans/{loanId}/early-settlement/{efsId}/register |
| `ELND0401` | 400 | Loan product does not support early final settlement. | Lending | 1 | POST /v2/loans/{loanId}/early-settlement/simulate |
| `ELND0402` | 400 | Lock In period defined in the current loan product did not meet the number of installments paid. | Lending | 1 | POST /v2/loans/{loanId}/early-settlement/simulate |
| `ELND0403` | 400 | Early final settlement ID must be a UUID | Lending | 1 | POST /v2/loans/{loanId}/early-settlement/{efsId}/register |
| `ELND0404` | 400 | This EFS simulation is not valid anymore because the outstanding balance changed after the simulation was requested. | Lending | 1 | POST /v2/loans/{loanId}/early-settlement/{efsId}/register |
| `ELND0405` | 400 | Field reference_date must be equal to or greater than today. | Lending | 1 | POST /v2/loans/{loanId}/early-settlement/simulate |
| `ELND0406` | 400 | Field waive_penalty is true but no penalty is configured for this product. | Lending | 1 | POST /v2/loans/{loanId}/early-settlement/simulate |
| `ELND0500` | 400 | simulationId must be an UUID | Lending | 1 | POST /v2/loans/{loanId}/prepayment/{simulationId}/register |
| `ELND0504` | 400 | Field amount_paid not passed. | Lending | 1 | POST /v2/loans/{loanId}/prepayment/simulate |
| `ELND0509` | 400 | This Prepayment simulation is no longer valid because the outstanding balance changed after the simulation was requested. | Lending | 1 | POST /v2/loans/{loanId}/prepayment/{simulationId}/register |
| `ELND0511` | 400 | The calculated penalty would be greater than the amount being paid. | Lending | 1 | POST /v2/loans/{loanId}/prepayment/simulate |
| `ELND0512` | 400 | Field reduce_option not passed. | Lending | 1 | POST /v2/loans/{loanId}/prepayment/simulate |
| `ELND0513` | 400 | Loan product does not permit the reduce_option passed in the request. | Lending | 1 | POST /v2/loans/{loanId}/prepayment/simulate |
| `ELND0514` | 400 | Failed to calculate the new loan with the provided parameters. | Lending | 1 | POST /v2/loans/{loanId}/prepayment/simulate |
| `ELND0515` | 400 | Simulation config not found. | Lending | 1 | POST /v2/loans/{loanId}/prepayment/simulate |
| `ELND0549` | 400 | Prepayment processing code length must be between 2 and 6. | Lending | 1 | POST /v2/loans/{loanId}/prepayment/{simulationId}/register |
| `ELND0550` | 400 | Penalty processing code length must be between 2 and 6. | Lending | 1 | POST /v2/loans/{loanId}/prepayment/{simulationId}/register |
| `ELND0551` | 400 | Insurance processing code length must be between 2 and 6. | Lending | 1 | POST /v2/loans/{loanId}/prepayment/{simulationId}/register |
| `ELND0601` | 400 | Field hierarchy_code not passed | Lending | 2 | GET /v2/repayment-hierarchies/{hierarchyCode};POST /v2/repayment-hierarchies |
| `ELND0603` | 400 | Field hierarchy not passed | Lending | 1 | POST /v2/repayment-hierarchies |
| `ELND0605` | 400 | Field hierarchy_code length must be lower or equal to 80 | Lending | 1 | POST /v2/repayment-hierarchies |
| `ELND0606` | 400 | Field hierarchy size must be equal to 7 | Lending | 1 | POST /v2/repayment-hierarchies |
| `ELND0607` | 400 | Field hierarchy_code contains invalid characters | Lending | 2 | GET /v2/repayment-hierarchies/{hierarchyCode};POST /v2/repayment-hierarchies |
| `ELND0608` | 400 | Invalid hierarchy type provided | Lending | 1 | POST /v2/repayment-hierarchies |
| `ELND1501` | 202 | idempotency-key is already in use | Lending | 2 | PATCH /v2/loan-products/{productId};POST /v2/loan-products |
| `ELND1802` | 400 | Field fromCreatedDate must be before or equal to toCreatedDate. | Lending | 1 | GET /v2/accounts/{accountId}/loans |
| `ELND1803` | 400 | Field fromStartDate must be before or equal to toStartDate. | Lending | 1 | GET /v2/accounts/{accountId}/loans |
| `ELND1804` | 400 | summarizeLoans must be a valid boolean value. | Lending | 1 | GET /v2/accounts/{accountId}/loans |
| `ELND1807` | 400 | includeInsuranceHistory must be a valid boolean value. | Lending | 2 | GET /v2/accounts/{accountId}/loans;GET /v2/loans/{loanId} |
| `ELND1808` | 400 | Field fromStartDate and toStartDate date range must not exceed 12 months. | Lending | 1 | GET /v2/accounts/{accountId}/loans |
| `ELND1809` | 400 | Field fromCreatedDate and toCreatedDate date range must not exceed 12 months. | Lending | 1 | GET /v2/accounts/{accountId}/loans |
| `ELND2000` | 404 | Loan not found | Lending | 2 | POST /v2/loans/{loanId}/early-settlement/simulate;POST /v2/loans/{loanId}/early-settlement/{efsId}/register |
| `ELND2106` | 400 | No active loans found for the account. | Lending | 1 | POST /v2/accounts/{accountId}/loans/cancel |
| `ELND2107` | 400 | Invalid account ID | Lending | 1 | POST /v2/accounts/{accountId}/loans/cancel |
| `ELND2300` | 400 | repayment_date must be less than or equal to current date. | Lending | 1 | POST /v2/loans/{loanId}/repayment |
| `ELND2301` | 400 | Backdating is not enabled for this product. | Lending | 1 | POST /v2/loans/{loanId}/repayment |
| `ELND2302` | 400 | repayment_date is older than the maximum backdating window. | Lending | 1 | POST /v2/loans/{loanId}/repayment |
| `ELND2303` | 400 | Backdating reason is required when the operation is backdated. | Lending | 1 | POST /v2/loans/{loanId}/repayment |
| `ELND2304` | 400 | Invalid backdating reason. | Lending | 1 | POST /v2/loans/{loanId}/repayment |
| `ELND2305` | 400 | repayment_date must not be before the loan creation date. | Lending | 1 | POST /v2/loans/{loanId}/repayment |
| `ELND3000` | 404 | Loan product not found. | Lending | 1 | POST /v2/loans/{loanId}/early-settlement/simulate |

## Lifecycle status

- No code in this unit is mentioned in a changelog post.

## Conflicts, caveats and evidence gaps

- Codes and messages come from response examples in the OpenAPI specifications; the conditions that trigger a code are documented only where the message or the operation description states them.
- The source table recognises only codes made of letters followed by digits; codes with mixed prefixes (for example `WP2P0000`) are not in the table but appear in the API-reference KUs.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-reference-data/error_code_index.csv` | rows with code prefix ELND | https://github.com/PismoDevEx/pismo-api-specs | `76213ae93e90a725…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-API-lending--disbursements` — API reference: Lending — Disbursements
- `KU-API-lending--early-final-settlement` — API reference: Lending — Early final settlement
- `KU-API-lending--loan-products` — API reference: Lending — Loan products
- `KU-API-lending--loans` — API reference: Lending — Loans
- `KU-API-lending--prepayment` — API reference: Lending — Prepayment
- `KU-API-lending--repayment-hierarchy` — API reference: Lending — Repayment hierarchy
- `KU-API-lending--repayments` — API reference: Lending — Repayments
