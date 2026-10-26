---
ku_id: KU-ERR-codes-esmg-to-whis
title: 'Error codes: ESMG to WHIS (30 prefixes)'
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
- KU-API-banking-transaction-banking--bank-statements-part-01
- KU-API-banking-transaction-banking--bank-statements-part-02
- KU-API-banking-transaction-banking--bulk-payment-files
- KU-API-banking-transaction-banking--channels
- KU-API-banking-transaction-banking--check-posting
- KU-API-banking-transaction-banking--divisions
- KU-API-banking-transaction-banking--dormancy
- KU-API-banking-transaction-banking--earmarking-external-accounts
- KU-API-banking-transaction-banking--earmarking-pismo-account-id
- KU-API-banking-transaction-banking--hierarchies
- KU-API-banking-transaction-banking--payments-part-03
- KU-API-banking-transaction-banking--payments-pismo-account-id
- KU-API-banking-transaction-banking--register-banking-account
- KU-API-banking-transaction-banking--transactions
- KU-API-core-platform-accounts--accounts
- KU-API-core-platform-accounts--statuses-and-reasons
- KU-API-core-platform-balance-config-beta--balance-configurations
- KU-API-core-platform-payment-methods--installments-payments
- KU-API-core-platform-payment-methods-admin--simulation
- KU-API-core-platform-transactions--transaction-flows
- KU-API-core-platform-transactions--transaction-types
- KU-API-instant-payments-pix-management--anti-fraud
- KU-API-instant-payments-pix-management--infraction-reports-part-01
- KU-API-instant-payments-pix-management--infraction-reports-part-02
- KU-API-instant-payments-pix-management--keys-part-01
- KU-API-instant-payments-pix-management--keys-part-02
- KU-API-instant-payments-pix-payments--pix-part-01
- KU-API-revolving-credit-configurations--features-by-account-status
- KU-API-revolving-credit-delinquency--delinquency
- KU-API-seller-management-sellers--marketplace
- KU-CHG-2-may-2025
- KU-CHG-3-april-2026
- KU-CHG-4-april-2025
- KU-CHG-6-february-2026
- KU-CHG-6-march-2026
- KU-CHG-7-august-2026
- KU-CHG-7-july-2025
error_codes:
- ESMG0401
- ESMG0900
- ESMT0001
- ESMT0003
- ESPI00002
- ESPI00005
- ESPI00007
- ESPI00008
- ESPI00009
- ESPI00010
- ESPI00014
- ESPI00029
- ESPI00030
- ETRC00001
- ETRC03002
- ETRC04003
- ETRC04004
- ETRC04005
- ETRC04006
- ETRC05001
- GN0001
- ISMA1001
- ISMG0001
- MIGR00001
- MIGR00002
- PBE315
- PBE353
- PCE001
- RULVAL0409
- SI001
- SI003
- WABL0001
- WABL0002
- WABL0003
- WACC0011
- WACC0017
- WACM0001
- WACM0002
- WADC0002
- WADC0003
- WADC0004
- WBBT0001
- WBBT0002
- WBBT0003
- WBBT0004
- WBBT0005
- WBLC0020
- WBLC0022
- WBLS0001
- WBLS0002
- WBLS0003
- WBLS0004
- WBLS0005
- WBLS0006
- WBLS0007
- WBPK0001
- WBPK0002
- WBPK0004
- WBPK0005
- WBUP0001
- WBUP0003
- WBUP0004
- WBUP0005
- WBUP0006
- WBUP0007
- WBUP0008
- WBUP0009
- WBUP0010
- WCCC011
- WCCL0001
- WCCL0002
- WCCL0003
- WCCL0004
- WCCL0005
- WCDV0002
- WCFG0001
- WCFG0002
- WCFG0003
- WCFG0004
- WCFG0005
- WCFG0006
- WCFG0007
- WCFG0010
- WCFG0011
- WCMN0002
- WCMN0003
- WCMN0004
- WCMN0005
- WCMN0006
- WCTR0003
- WCTR0004
- WCTR0005
- WCTR0006
- WDOR0001
- WDOR0002
- WDOR0003
- WDOR0004
- WDOR0005
- WDOR0006
- WDOR0007
- WDOR0008
- WDOR0009
- WDOR0010
- WDOR0011
- WHIE0001
- WHIE0002
- WHIE0003
- WHIE0004
- WHIE0005
- WHIE0006
- WHIE0007
- WHIS0001
- WHIS0002
- WHIS0003
- WHIS0004
- WHIS0005
- WHIS0006
- WHIS0007
- WHIS0008
---

# Error codes: ESMG to WHIS (30 prefixes)

**KU ID:** `KU-ERR-codes-esmg-to-whis` · **Category:** Errors and troubleshooting · **Type:** error-code catalogue (from reference table)

## Purpose and scope

119 error code(s) with prefix(es) ESMG, ESMT, ESPI, ETRC, GN, ISMA, ISMG, MIGR, PBE, PCE, RULVAL, SI, WABL, WACC, WACM, WADC, WBBT, WBLC, WBLS, WBPK, WBUP, WCCC, WCCL, WCDV, WCFG, WCMN, WCTR, WDOR, WHIE, WHIS from `api-reference-data/error_code_index.csv`, with the HTTP status, message and the operations whose response examples contain the code. The `operations_sample` column is a sample, not a complete list: the complete set of codes per operation is in the API-reference KUs (section “Error codes shown in this operation's response examples”). Conditions under which a code is returned are documented only where the message or the operation description states them.

## Error codes

| Code | HTTP status | Message | Specification files | Operation count | Operations (sample) |
| --- | --- | --- | --- | --- | --- |
| `ESMG0401` | 401 | Unauthorized | Seller_management_-_Sellers | 1 | GET /v3/marketplaces |
| `ESMG0900` | not stated | Failed during validation of request payload | Seller_management_-_Sellers | 0 |  |
| `ESMT0001` | not stated | Failed during validation of request payload | Seller_management_-_Transactions | 0 |  |
| `ESMT0003` | not stated | Merchant not found | Seller_management_-_Transactions | 0 |  |
| `ESPI00002` | 500 | Internal error | Instant_payments_-_Pix_management | 1 | POST /v2/pix/keys/validate |
| `ESPI00005` | 502 | HTTP error | Instant_payments_-_Pix_management | 1 | POST /v2/pix/keys/validate |
| `ESPI00007` | 500 | Auth - API returned 5xx error | Instant_payments_-_Pix_management | 1 | POST /v2/pix/keys/validate |
| `ESPI00008` | 400 | Auth - API returned 4xx error | Instant_payments_-_Pix_management | 1 | POST /v2/pix/keys/validate |
| `ESPI00009` | 502 | Dict - API returned 5xx error | Instant_payments_-_Pix_management | 1 | POST /v2/pix/keys/validate |
| `ESPI00010` | 400 | Dict - API returned 4xx error | Instant_payments_-_Pix_management | 1 | POST /v2/pix/keys/validate |
| `ESPI00014` | 404 | Dict - API key not found | Instant_payments_-_Pix_management | 1 | POST /v2/pix/keys/validate |
| `ESPI00029` | 409 | Provider timeout | Instant_payments_-_Pix_management | 1 | POST /v2/pix/keys/validate |
| `ESPI00030` | 409 | Dict - API returned 5xx error | Instant_payments_-_Pix_management | 1 | POST /v2/pix/keys/validate |
| `ETRC00001` | 500 | Internal processing error | Core_platform_-_Transactions | 10 | GET /v1/transaction-flow;GET /v1/transaction-type/{transactionTypeId};GET /v1/transaction-types |
| `ETRC03002` | 500 | Could not perform program transaction type operation | Core_platform_-_Transactions | 1 | PATCH /v1/programs/{programId}/transaction-types/{transactionTypeId} |
| `ETRC04003` | 409 | The provided amount type is already configured for the processing code | Core_platform_-_Transactions | 2 | PATCH /v1/transaction-flow/processing-code/{processingCode}/transaction-type/{transactionTypeId};POST /v1/transaction-flow |
| `ETRC04004` | 409 | The provided transaction type is already configured for the processing code | Core_platform_-_Transactions | 2 | PATCH /v1/transaction-flow/processing-code/{processingCode}/transaction-type/{transactionTypeId};POST /v1/transaction-flow |
| `ETRC04005` | 409 | The provided amount type conflicts with an existing configured amount type for the processing code. Please select either Principal or Contract | Core_platform_-_Transactions | 2 | PATCH /v1/transaction-flow/processing-code/{processingCode}/transaction-type/{transactionTypeId};POST /v1/transaction-flow |
| `ETRC04006` | 409 | Transaction Type isCredit does not correspond to the processing code balance impact | Core_platform_-_Transactions | 2 | PATCH /v1/transaction-flow/processing-code/{processingCode}/transaction-type/{transactionTypeId};POST /v1/transaction-flow |
| `ETRC05001` | 500 | Failed to get transaction type | Core_platform_-_Transactions | 1 | GET /v1/transaction-types |
| `GN0001` | 500 | Service is unavailable | Revolving_credit_-_Calendar_management;Revolving_credit_-_Configurations;Revolving_credit_-_Delinquency;Revolving_credit_-_Installment_management;Revolving_credit_-_Interest_accruals;Revolving_credit_-_Statement_refinancing_API;Revolving_credit_-_Statements | 6 | GET /v1/accounts/{accountId}/buckets;GET /v1/accounts/{accountId}/buckets/{delinquencyBucketId};GET /v1/features-by-account-status |
| `ISMA1001` | not stated | Not found. | Seller_management_-_Sellers | 0 |  |
| `ISMG0001` | not stated | Success. | Seller_management_-_Sellers | 0 |  |
| `MIGR00001` | not stated | Something went wrong | Migrations | 0 |  |
| `MIGR00002` | not stated | Field required | Migrations | 0 |  |
| `PBE315` | 500 | Generic error | Instant_payments_-_Pix_management | 17 | GET /v2/pix/fraud-markers/{id};GET /v2/pix/infraction-reports;GET /v2/pix/infraction-reports/search |
| `PBE353` | 400;404 | Entity not found | Instant_payments_-_Pix_management | 6 | GET /v2/pix/keys;PATCH /v2/pix/keys;POST /v2/pix/keys |
| `PCE001` | 400 | The value "000000012345" is invalid for PI-PayerId. The value must match "((^[0-9]11$)\|(^[0-9]14$))" | Instant_payments_-_Pix_payments | 2 | POST /pix/v1/pix/in/reversal;POST /pix/v1/pix/qrcode/validate |
| `RULVAL0409` | 409 | Evaluation already exists for CID. | Core_platform_-_Payment_methods | 1 | POST /payments/v1/payments/installments |
| `SI001` | 422 | An unexpected error happened. | Core_platform_-_Payment_methods_admin | 1 | POST /v1/simulations |
| `SI003` | 422 | Card doesn't have authorization mode created. | Core_platform_-_Payment_methods_admin | 1 | POST /v1/simulations |
| `WABL0001` | 404 | Account balance not found | Banking_-_Transaction_banking | 1 | GET /bank-statements/v1/account-balances/{externalAccountId} |
| `WABL0002` | 401 | Account not authorized | Banking_-_Transaction_banking | 1 | GET /bank-statements/v1/account-balances/{externalAccountId} |
| `WABL0003` | 400 | Invalid header account | Banking_-_Transaction_banking | 1 | GET /bank-statements/v1/account-balances/{externalAccountId} |
| `WACC0011` | 400 | Invalid cursor value | Banking_-_Transaction_banking;Core_platform_-_Accounts | 4 | GET /accounts/v4/reasons;GET /accounts/v4/statuses;GET /corporate/v1/corporate-account-status/reasons |
| `WACC0017` | 404 | Account not found | Core_platform_-_Accounts | 1 | GET /accounts/v4/accounts/{accountId}/hierarchy/ascendants |
| `WACM0001` | not stated | Error validating input | Core_platform_-_Accumulator | 0 |  |
| `WACM0002` | not stated | identifier gmf123 already exists | Core_platform_-_Accumulator | 0 |  |
| `WADC0002` | 404 | Account Dormancy Control not found: {externalAccountId} | Banking_-_Transaction_banking | 1 | GET /corporate/v1/account-dormancy/{externalAccountId} |
| `WADC0003` | 404 | Corporate account not found | Banking_-_Transaction_banking | 1 | GET /corporate/v1/account-dormancy/{externalAccountId} |
| `WADC0004` | 404 | Division with division_code {%s} not found | Banking_-_Transaction_banking | 1 | GET /corporate/v1/account-dormancy/{externalAccountId} |
| `WBBT0001` | 400 | Invalid JSON payload received: Error unmarshalling request | Banking_-_Transaction_banking | 1 | PUT /corporate/v1/feature/back-business/toggle |
| `WBBT0002` | 400 | business_date {business_date} should be formatted as yyyy-mm-dd and be a valid date | Banking_-_Transaction_banking | 1 | PUT /corporate/v1/feature/back-business/toggle |
| `WBBT0003` | 400 | Business date must fall within a past business cycle | Banking_-_Transaction_banking | 1 | PUT /corporate/v1/feature/back-business/toggle |
| `WBBT0004` | 400 | Division not found | Banking_-_Transaction_banking | 1 | PUT /corporate/v1/feature/back-business/toggle |
| `WBBT0005` | 400 | Channel '{channel}' not found | Banking_-_Transaction_banking | 1 | PUT /corporate/v1/feature/back-business/toggle |
| `WBLC0020` | 400 | Error parsing program ID to integer number. | Core_platform_-_Balance_config_Beta | 2 | GET /v1/balances-config;GET /v1/balances-config/{configId} |
| `WBLC0022` | 404 | Balance configuration not found. | Core_platform_-_Balance_config_Beta | 2 | GET /v1/balances-config/{configId};PUT /v1/balances-config/{configId} |
| `WBLS0001` | not stated | Some required headers are missing | Core_platform_-_Balances_and_limits | 0 |  |
| `WBLS0002` | not stated | Invalid input | Core_platform_-_Balances_and_limits | 0 |  |
| `WBLS0003` | not stated | Invalid syntax input | Core_platform_-_Balances_and_limits | 0 |  |
| `WBLS0004` | not stated | Invalid account id | Core_platform_-_Balances_and_limits | 0 |  |
| `WBLS0005` | not stated | Error validating input | Core_platform_-_Balances_and_limits | 0 |  |
| `WBLS0006` | not stated | Account not found | Core_platform_-_Balances_and_limits | 0 |  |
| `WBLS0007` | not stated | Global configuration not found | Core_platform_-_Balances_and_limits | 0 |  |
| `WBPK0001` | 400 | Invalid JSON payload received: Error unmarshalling request | Banking_-_Transaction_banking | 1 | POST /corporate/v1/bulk-payments/keys |
| `WBPK0002` | 400 | key_material must be encoded in DER and a Base64 format string | Banking_-_Transaction_banking | 1 | POST /corporate/v1/bulk-payments/keys |
| `WBPK0004` | 400 | expires_at must not be in the past | Banking_-_Transaction_banking | 1 | POST /corporate/v1/bulk-payments/keys |
| `WBPK0005` | 400 | Key with id {id} already registered | Banking_-_Transaction_banking | 1 | POST /corporate/v1/bulk-payments/keys |
| `WBUP0001` | 400 | 'signature' header: attribute must be a valid base64 encoded string | Banking_-_Transaction_banking | 1 | PUT /corporate/v1/bulk-payments/{bulkId} |
| `WBUP0003` | 409 | Duplicate bulk file uploaded | Banking_-_Transaction_banking | 1 | PUT /corporate/v1/bulk-payments/{bulkId} |
| `WBUP0004` | 400 | Invalid request header | Banking_-_Transaction_banking | 1 | PUT /corporate/v1/bulk-payments/{bulkId} |
| `WBUP0005` | 400 | Invalid JSON data in bulk header | Banking_-_Transaction_banking | 1 | PUT /corporate/v1/bulk-payments/{bulkId} |
| `WBUP0006` | 400 | Authentication OrgID does not match Bulk Header | Banking_-_Transaction_banking | 1 | PUT /corporate/v1/bulk-payments/{bulkId} |
| `WBUP0007` | 400 | BulkID in URL does not match Bulk Header | Banking_-_Transaction_banking | 1 | PUT /corporate/v1/bulk-payments/{bulkId} |
| `WBUP0008` | 400 | Invalid operation_type in Bulk Header | Banking_-_Transaction_banking | 1 | PUT /corporate/v1/bulk-payments/{bulkId} |
| `WBUP0009` | 400 | Invalid bulkId format | Banking_-_Transaction_banking | 1 | PUT /corporate/v1/bulk-payments/{bulkId} |
| `WBUP0010` | 400 | Bulk header line exceeds maximum allowed length | Banking_-_Transaction_banking | 1 | PUT /corporate/v1/bulk-payments/{bulkId} |
| `WCCC011` | 400 | Validation Error: The "FULL_CANCELLATION" account status was not found for this organization. | Revolving_credit_-_Configurations | 2 | PATCH /v1/features-by-account-status;POST /v1/features-by-account-status |
| `WCCL0001` | 400 | Invalid JSON payload received: Error unmarshalling request | Banking_-_Transaction_banking | 2 | PATCH /corporate/v1/channels/{channel};POST /corporate/v1/channels |
| `WCCL0002` | 400 | CreatedAtStart 10-12-2026 should be formatted as yyyy-mm-dd and be a valid date | Banking_-_Transaction_banking | 3 | GET /corporate/v1/channels;PATCH /corporate/v1/channels/{channel};POST /corporate/v1/channels |
| `WCCL0003` | 409 | Channel 'GDP' already exists | Banking_-_Transaction_banking | 1 | POST /corporate/v1/channels |
| `WCCL0004` | 404 | Channel not found | Banking_-_Transaction_banking | 3 | DELETE /corporate/v1/channels/{channel};GET /corporate/v1/channels/{channel};PATCH /corporate/v1/channels/{channel} |
| `WCCL0005` | 400 | Channel not active | Banking_-_Transaction_banking | 2 | DELETE /corporate/v1/channels/{channel};PATCH /corporate/v1/channels/{channel} |
| `WCDV0002` | 404 | Division not found | Banking_-_Transaction_banking | 1 | POST /corporate/v2/corporate-accounts/register |
| `WCFG0001` | 400 | Invalid JSON payload received: Error unmarshalling request | Banking_-_Transaction_banking | 5 | GET /bank-statements/v2/account-balances/history/config;PATCH /bank-statements/v1/account-balances/history/config/{divisionCode};PATCH /bank-statements/v2/account-balances/history/config/{balanceHistoryConfigId} |
| `WCFG0002` | 400 | cycle_closing_time has an invalid time format: {cycle_closing_time} | Banking_-_Transaction_banking | 8 | GET /bank-statements/v1/account-balances/history/config/{divisionCode};GET /bank-statements/v2/account-balances/history/config;GET /bank-statements/v2/account-balances/history/config/{balanceHistoryConfigId} |
| `WCFG0003` | 404 | Division [divisionCode] not found | Banking_-_Transaction_banking | 7 | GET /bank-statements/v1/account-balances/history/config/{divisionCode};GET /bank-statements/v2/account-balances/history/config;GET /bank-statements/v2/account-balances/history/config/{balanceHistoryConfigId} |
| `WCFG0004` | 409 | Division is already configured | Banking_-_Transaction_banking | 3 | GET /bank-statements/v2/account-balances/history/config;POST /bank-statements/v1/account-balances/history/config;POST /bank-statements/v2/account-balances/history/config |
| `WCFG0005` | 404 | Account balance history config not found | Banking_-_Transaction_banking | 5 | GET /bank-statements/v1/account-balances/history/config/{divisionCode};GET /bank-statements/v2/account-balances/history/config/{balanceHistoryConfigId};GET /bank-statements/v2/account-balances/history/config/{targetType}/{targetId} |
| `WCFG0006` | 404 | Program not found | Banking_-_Transaction_banking | 2 | PATCH /bank-statements/v2/account-balances/history/config/{balanceHistoryConfigId};POST /bank-statements/v2/account-balances/history/config |
| `WCFG0007` | 404 | Organization not found | Banking_-_Transaction_banking | 2 | PATCH /bank-statements/v2/account-balances/history/config/{balanceHistoryConfigId};POST /bank-statements/v2/account-balances/history/config |
| `WCFG0010` | 400 | Invalid target type: must be ORGANIZATION, PROGRAM, or DIVISION | Banking_-_Transaction_banking | 3 | GET /bank-statements/v2/account-balances/history/config/{targetType}/{targetId};PATCH /bank-statements/v2/account-balances/history/config/{balanceHistoryConfigId};POST /bank-statements/v2/account-balances/history/config |
| `WCFG0011` | 400 | Invalid target ID | Banking_-_Transaction_banking | 2 | PATCH /bank-statements/v2/account-balances/history/config/{balanceHistoryConfigId};POST /bank-statements/v2/account-balances/history/config |
| `WCMN0002` | 400 | scheduleDatetime: The scheduled datetime is too close to the current datetime | Banking_-_Transaction_banking | 5 | POST /cash-management/v2/payments;POST /cash-management/v2/scheduled-payments;POST /corporate/v1/checks |
| `WCMN0003` | 400 | Missing HTTP parameters | Banking_-_Transaction_banking | 1 | GET /corporate/v1/dormancy-config/{dormancyConfigId} |
| `WCMN0004` | 400 | Invalid cursor | Banking_-_Transaction_banking | 5 | GET /corporate/v1/channels;GET /corporate/v1/dormancy-config;GET /corporate/v1/hierarchies |
| `WCMN0005` | 400 | Invalid query parameter | Banking_-_Transaction_banking | 2 | GET /cash-management/v1/earmarks;GET /corporate/v1/earmarks |
| `WCMN0006` | 400 | Limit must be less than or equal to 100 | Banking_-_Transaction_banking | 3 | GET /corporate/v1/dormancy-config;GET /corporate/v1/hierarchies;GET /corporate/v2/divisions |
| `WCTR0003` | 400 | authorization type should be PLATFORM or NETWORK | Banking_-_Transaction_banking | 1 | GET /corporate/v1/corporate-transactions |
| `WCTR0004` | 400 | Invalid request parameters | Banking_-_Transaction_banking | 1 | GET /corporate/v1/corporate-transactions |
| `WCTR0005` | 400 | transactionId is invalid | Banking_-_Transaction_banking | 1 | GET /corporate/v1/corporate-transactions/{transactionId} |
| `WCTR0006` | 404 | Transaction not found | Banking_-_Transaction_banking | 2 | GET /corporate/v1/corporate-transactions/status/{trackingId};GET /corporate/v1/corporate-transactions/{transactionId} |
| `WDOR0001` | 400 | Invalid JSON payload received: Error unmarshalling request | Banking_-_Transaction_banking | 2 | PATCH /corporate/v2/dormancy-config/{dormancyConfigId};POST /corporate/v2/dormancy-config |
| `WDOR0002` | 400 | target_id is a required field. If the target_type is DIVISION the target_id is the division code. If target_type is PROGRAM the target_id will be the program ID. | Banking_-_Transaction_banking | 4 | GET /corporate/v1/dormancy-config;PATCH /corporate/v2/dormancy-config/{dormancyConfigId};POST /corporate/v2/dormancy-config |
| `WDOR0003` | 404 | Division with division_code {targetID} not found | Banking_-_Transaction_banking | 1 | POST /corporate/v2/dormancy-config |
| `WDOR0004` | 404 | Program with program_id {targetID} not found | Banking_-_Transaction_banking | 1 | POST /corporate/v2/dormancy-config |
| `WDOR0005` | 400 | Invalid status {status} | Banking_-_Transaction_banking | 2 | PATCH /corporate/v2/dormancy-config/{dormancyConfigId};POST /corporate/v2/dormancy-config |
| `WDOR0006` | 400 | Invalid reason_external_id {reason_id} | Banking_-_Transaction_banking | 2 | PATCH /corporate/v2/dormancy-config/{dormancyConfigId};POST /corporate/v2/dormancy-config |
| `WDOR0007` | 404 | Dormancy configuration with ID {dormancyConfigId} not found | Banking_-_Transaction_banking | 2 | GET /corporate/v1/dormancy-config/{dormancyConfigId};PATCH /corporate/v2/dormancy-config/{dormancyConfigId} |
| `WDOR0008` | 400 | Dormancy configuration with ID {dormancyID} already exists | Banking_-_Transaction_banking | 1 | POST /corporate/v2/dormancy-config |
| `WDOR0009` | 400 | Invalid dormant processing code [{dormant_processing_code}] | Banking_-_Transaction_banking | 2 | PATCH /corporate/v2/dormancy-config/{dormancyConfigId};POST /corporate/v2/dormancy-config |
| `WDOR0010` | 400 | Invalid current_reason_external_id, the current_reason_external_id you entered does not exist. | Banking_-_Transaction_banking | 2 | PATCH /corporate/v2/dormancy-config/{dormancyConfigId};POST /corporate/v2/dormancy-config |
| `WDOR0011` | 400 | Invalid new_reason_external_id, the new_reason_external_id you entered does not exist. | Banking_-_Transaction_banking | 2 | PATCH /corporate/v2/dormancy-config/{dormancyConfigId};POST /corporate/v2/dormancy-config |
| `WHIE0001` | 400 | Invalid JSON payload received: Error unmarshalling request | Banking_-_Transaction_banking | 2 | PATCH /corporate/v1/hierarchies/{hierarchyId};POST /corporate/v1/hierarchies |
| `WHIE0002` | 400 | description must be a maximum of 80 characters in length | Banking_-_Transaction_banking | 2 | PATCH /corporate/v1/hierarchies/{hierarchyId};POST /corporate/v1/hierarchies |
| `WHIE0003` | 400 | First Level index must be 0 | Banking_-_Transaction_banking | 1 | POST /corporate/v1/hierarchies |
| `WHIE0004` | 400 | Levels must have different index values | Banking_-_Transaction_banking | 1 | POST /corporate/v1/hierarchies |
| `WHIE0005` | 400 | Levels index values must be in a sequential order | Banking_-_Transaction_banking | 1 | POST /corporate/v1/hierarchies |
| `WHIE0006` | 404 | Hierarchy with ID {hierarchyId} not found | Banking_-_Transaction_banking | 1 | PATCH /corporate/v1/hierarchies/{hierarchyId} |
| `WHIE0007` | 400 | levels should have at least 1 item | Banking_-_Transaction_banking | 1 | POST /corporate/v1/hierarchies |
| `WHIS0001` | 401 | Account not authorized | Banking_-_Transaction_banking | 1 | GET /bank-statements/v1/account-balances/{externalAccountId}/history |
| `WHIS0002` | 400 | Invalid header account | Banking_-_Transaction_banking | 1 | GET /bank-statements/v1/account-balances/{externalAccountId}/history |
| `WHIS0003` | 400 | Invalid date format | Banking_-_Transaction_banking | 1 | GET /bank-statements/v1/account-balances/{externalAccountId}/history |
| `WHIS0004` | 400 | Invalid date interval | Banking_-_Transaction_banking | 1 | GET /bank-statements/v1/account-balances/{externalAccountId}/history |
| `WHIS0005` | 404 | No account balance history found | Banking_-_Transaction_banking | 1 | GET /bank-statements/v1/account-balances/{externalAccountId}/history |
| `WHIS0006` | 400 | Max page limit exceeded | Banking_-_Transaction_banking | 1 | GET /bank-statements/v1/account-balances/{externalAccountId}/history |
| `WHIS0007` | 400 | Max query range exceeded | Banking_-_Transaction_banking | 1 | GET /bank-statements/v1/account-balances/{externalAccountId}/history |
| `WHIS0008` | 400 | Cursor is invalid | Banking_-_Transaction_banking | 1 | GET /bank-statements/v1/account-balances/{externalAccountId}/history |

## Lifecycle status

Codes in this unit that are mentioned in changelog posts (check the post: it may record that the code was added, changed or removed from some endpoints):

- `ETRC04003`: `KU-CHG-2-may-2025`
- `ETRC04004`: `KU-CHG-2-may-2025`, `KU-CHG-6-march-2026`
- `ETRC04005`: `KU-CHG-2-may-2025`, `KU-CHG-6-march-2026`
- `WBUP0004`: `KU-CHG-3-april-2026`
- `WBUP0005`: `KU-CHG-3-april-2026`
- `WBUP0006`: `KU-CHG-3-april-2026`
- `WBUP0007`: `KU-CHG-3-april-2026`
- `WBUP0008`: `KU-CHG-3-april-2026`
- `WBUP0009`: `KU-CHG-7-august-2026`
- `WBUP0010`: `KU-CHG-7-august-2026`
- `WCFG0002`: `KU-CHG-7-july-2025`
- `WCMN0004`: `KU-CHG-4-april-2025`
- `WCMN0006`: `KU-CHG-6-february-2026`
- `WDOR0002`: `KU-CHG-7-july-2025`
- `WHIE0007`: `KU-CHG-4-april-2025`

## Conflicts, caveats and evidence gaps

- Codes and messages come from response examples in the OpenAPI specifications; the conditions that trigger a code are documented only where the message or the operation description states them.
- The source table recognises only codes made of letters followed by digits; codes with mixed prefixes (for example `WP2P0000`) are not in the table but appear in the API-reference KUs.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-reference-data/error_code_index.csv` | rows with code prefix ESMG, ESMT, ESPI, ETRC, GN, ISMA, ISMG, MIGR, PBE, PCE, RULVAL, SI, WABL, WACC, WACM, WADC, WBBT, WBLC, WBLS, WBPK, WBUP, WCCC, WCCL, WCDV, WCFG, WCMN, WCTR, WDOR, WHIE, WHIS | https://github.com/PismoDevEx/pismo-api-specs | `76213ae93e90a725…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-API-banking-transaction-banking--accounts` — API reference: Banking - Transaction banking — Accounts
- `KU-API-banking-transaction-banking--bank-statements-part-01` — API reference: Banking - Transaction banking — Bank statements (part 1 of 2)
- `KU-API-banking-transaction-banking--bank-statements-part-02` — API reference: Banking - Transaction banking — Bank statements (part 2 of 2)
- `KU-API-banking-transaction-banking--bulk-payment-files` — API reference: Banking - Transaction banking — Bulk payment files
- `KU-API-banking-transaction-banking--channels` — API reference: Banking - Transaction banking — Channels
- `KU-API-banking-transaction-banking--check-posting` — API reference: Banking - Transaction banking — Check posting
- `KU-API-banking-transaction-banking--divisions` — API reference: Banking - Transaction banking — Divisions
- `KU-API-banking-transaction-banking--dormancy` — API reference: Banking - Transaction banking — Dormancy
- `KU-API-banking-transaction-banking--earmarking-external-accounts` — API reference: Banking - Transaction banking — Earmarking (external accounts)
- `KU-API-banking-transaction-banking--earmarking-pismo-account-id` — API reference: Banking - Transaction banking — Earmarking (Pismo account ID)
- `KU-API-banking-transaction-banking--hierarchies` — API reference: Banking - Transaction banking — Hierarchies
- `KU-API-banking-transaction-banking--payments-part-03` — API reference: Banking - Transaction banking — Payments (part 3 of 3)
- `KU-API-banking-transaction-banking--payments-pismo-account-id` — API reference: Banking - Transaction banking — Payments (Pismo account ID)
- `KU-API-banking-transaction-banking--register-banking-account` — API reference: Banking - Transaction banking — Register banking account
- `KU-API-banking-transaction-banking--transactions` — API reference: Banking - Transaction banking — Transactions
- `KU-API-core-platform-accounts--accounts` — API reference: Core platform - Accounts — Accounts
- `KU-API-core-platform-accounts--statuses-and-reasons` — API reference: Core platform - Accounts — Statuses and reasons
- `KU-API-core-platform-balance-config-beta--balance-configurations` — API reference: Core platform - Balance configurations — Balance configurations
- `KU-API-core-platform-payment-methods--installments-payments` — API reference: Core platform - Payment methods — Installments payments
- `KU-API-core-platform-payment-methods-admin--simulation` — API reference: Core platform - Payment methods admin — Simulation
- `KU-API-core-platform-transactions--transaction-flows` — API reference: Core platform - Transactions — Transaction flows
- `KU-API-core-platform-transactions--transaction-types` — API reference: Core platform - Transactions — Transaction types
- `KU-API-instant-payments-pix-management--anti-fraud` — API reference: Instant payments - Pix management — Anti-fraud
- `KU-API-instant-payments-pix-management--infraction-reports-part-01` — API reference: Instant payments - Pix management — Infraction reports (part 1 of 2)
- `KU-API-instant-payments-pix-management--infraction-reports-part-02` — API reference: Instant payments - Pix management — Infraction reports (part 2 of 2)
- `KU-API-instant-payments-pix-management--keys-part-01` — API reference: Instant payments - Pix management — Keys (part 1 of 2)
- `KU-API-instant-payments-pix-management--keys-part-02` — API reference: Instant payments - Pix management — Keys (part 2 of 2)
- `KU-API-instant-payments-pix-payments--pix-part-01` — API reference: Instant payments - Pix payments — Pix (part 1 of 2)
- `KU-API-revolving-credit-configurations--features-by-account-status` — API reference: Revolving credit - Configurations — Features by account status
- `KU-API-revolving-credit-delinquency--delinquency` — API reference: Revolving credit - Delinquency — Delinquency
- `KU-API-seller-management-sellers--marketplace` — API reference: Seller management - Sellers — Marketplace
- `KU-CHG-2-may-2025` — Changelog: 2 May 2025
- `KU-CHG-3-april-2026` — Changelog: 3 April 2026
- `KU-CHG-4-april-2025` — Changelog: 4 April 2025
- `KU-CHG-6-february-2026` — Changelog: 6 February 2026
- `KU-CHG-6-march-2026` — Changelog: 6 March 2026
- `KU-CHG-7-august-2026` — Changelog: 7 August 2026
- `KU-CHG-7-july-2025` — Changelog: 7 July 2025
