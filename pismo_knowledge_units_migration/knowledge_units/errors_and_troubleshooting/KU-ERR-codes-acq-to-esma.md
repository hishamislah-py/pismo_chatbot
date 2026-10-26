---
ku_id: KU-ERR-codes-acq-to-esma
title: 'Error codes: ACQ to ESMA (32 prefixes)'
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
- KU-API-banking-authentication--provider-credentials
- KU-API-banking-ted-configuration--configurations
- KU-API-banking-transaction-banking--accounts
- KU-API-banking-transaction-banking--bank-statements-part-01
- KU-API-banking-transaction-banking--bulk-settlement
- KU-API-banking-transaction-banking--payments-part-03
- KU-API-banking-transaction-banking--payments-pismo-account-id
- KU-API-card-issuing-disputes--fees-v2
- KU-API-card-issuing-disputes--fraud-report
- KU-API-card-issuing-disputes--on-us
- KU-API-card-issuing-tokenization--card-lifecycle
- KU-API-control-center-audit-beta--audit
- KU-API-core-platform-accounts--accounts
- KU-API-core-platform-accounts--statuses-and-reasons
- KU-API-core-platform-balance-config-beta--balance-configurations
- KU-API-core-platform-balance-watcher--limit-acceptance-configurations
- KU-API-core-platform-balances-and-limits--account-limits
- KU-API-core-platform-ledger--account-limits
- KU-API-core-platform-payment-methods--force-operations
- KU-API-core-platform-payment-methods--payment-methods-part-01
- KU-API-core-platform-payment-methods--payments
- KU-API-core-platform-payment-methods-admin--simulation
- KU-API-instant-payments-pix-management--infraction-reports-part-01
- KU-API-revolving-credit-interest-accruals--accrual-type-post-configurations
- KU-API-revolving-credit-interest-accruals--post-interest-accruals
- KU-API-revolving-credit-statements--multivalue-program-parameters
- KU-API-revolving-credit-statements--statement-minimum-amount-due
- KU-CHG-7-november-2025
error_codes:
- ACQ0000
- ACQ0001
- AMON0000
- AMON0004
- BA00005
- BBLT0001
- BBLT0002
- BBLT0003
- BBLT0004
- BBLT0005
- BBLT0006
- BDPT0001
- BDPT0002
- BDPT0006
- BDPT0007
- BDPT0019
- BDPT0021
- BDPT0022
- BDPT0026
- BDPT0027
- BW0001
- BW0007
- BW0008
- BW0031
- BW0032
- CE0001
- CMN0002
- CMN9999
- DO0002
- EABL0001
- EACC0000
- EACC0003
- EACC0004
- EACC0005
- EACC0018
- EACC9999
- EACM0003
- EBAA0002
- EBAA0003
- EBAA0004
- EBAA0007
- EBAA0009
- EBAA0010
- EBAA0011
- EBAA0012
- EBAA0014
- EBCF0317
- EBCF0320
- EBCF0321
- EBLC9999
- EBLS9999
- EBLT0001
- EBLT0003
- EBLT0004
- EBLT0005
- EBLT0006
- EBLT0007
- EBLT0009
- EBLT9998
- EBLT9999
- EBS0009
- EBS0065
- ECAD0000
- ECAD0005
- ECAD0006
- ECAD0007
- ECM0001
- ECM0002
- ECM0003
- ECM0005
- ECMN9999
- EDPT0001
- EDPT0002
- EDPT0003
- EDPT0004
- EDPT0005
- EDPT0009
- EDPT9997
- EDPT9998
- EDPT9999
- EFCA0001
- EFCA0002
- EFCA0006
- EFCA0007
- EFCA0009
- EFCA0010
- EFCA0011
- EFCA0012
- EFCA0013
- EFCA0014
- EFCA0015
- EFCA0016
- EIAC0002
- EINS0004
- EINS0005
- EINS0006
- EINS0010
- EINS0011
- EINS0012
- EINS0015
- EINS0016
- ELDG500
- ELDG9999
- EPAE0001
- EPAE0002
- EPAE0004
- EPCG501
- EPT0303
- ERAT00001
- ERAT00002
- ERAT00003
- ERR4021
- ERR4091
- ERR4133
- ERR5446
- ERR93836
- ERR9786
- ERR9993
- ESMA5000
---

# Error codes: ACQ to ESMA (32 prefixes)

**KU ID:** `KU-ERR-codes-acq-to-esma` · **Category:** Errors and troubleshooting · **Type:** error-code catalogue (from reference table)

## Purpose and scope

119 error code(s) with prefix(es) ACQ, AMON, BA, BBLT, BDPT, BW, CE, CMN, DO, EABL, EACC, EACM, EBAA, EBCF, EBLC, EBLS, EBLT, EBS, ECAD, ECM, ECMN, EDPT, EFCA, EIAC, EINS, ELDG, EPAE, EPCG, EPT, ERAT, ERR, ESMA from `api-reference-data/error_code_index.csv`, with the HTTP status, message and the operations whose response examples contain the code. The `operations_sample` column is a sample, not a complete list: the complete set of codes per operation is in the API-reference KUs (section “Error codes shown in this operation's response examples”). Conditions under which a code is returned are documented only where the message or the operation description states them.

## Error codes

| Code | HTTP status | Message | Specification files | Operation count | Operations (sample) |
| --- | --- | --- | --- | --- | --- |
| `ACQ0000` | 500 | Unknown error | Core_platform_-_Payment_methods | 1 | POST /payments/v2/cancel |
| `ACQ0001` | 500 | Internal server error | Core_platform_-_Payment_methods | 1 | POST /payments/v2/cancel |
| `AMON0000` | 400 | The amount passed 51 is greater than the current balance 50 | Core_platform_-_Payment_methods | 1 | POST /payments/v2/cancel |
| `AMON0004` | 208;409 | Authorization was already refunded/reversed. | Core_platform_-_Payment_methods | 1 | POST /payments/v2/cancel |
| `BA00005` | 400 | Invalid payload. Required fields: [fields] | Banking_-_Authentication | 1 | POST /banking-auth/v1/credentials |
| `BBLT0001` | not stated | Error while validating fields | Card_issuing_-_Protection_Bulletin | 0 |  |
| `BBLT0002` | not stated | Bulletin card not found | Card_issuing_-_Protection_Bulletin | 0 |  |
| `BBLT0003` | not stated | Bulletin card has an ongoing event in the network brand. | Card_issuing_-_Protection_Bulletin | 0 |  |
| `BBLT0004` | not stated | Bulletin card is already BLOCKED | Card_issuing_-_Protection_Bulletin | 0 |  |
| `BBLT0005` | not stated | The card with ID 123 does not have a network brand. | Card_issuing_-_Protection_Bulletin | 0 |  |
| `BBLT0006` | not stated | The program with ID 123 does not have a network brand. | Card_issuing_-_Protection_Bulletin | 0 |  |
| `BDPT0001` | 422 | Error while validating fields | Card_issuing_-_Disputes | 4 | POST /v1/on-us-dispute;POST /v2/fee;POST /v2/fraud-report |
| `BDPT0002` | 422 | Fraud Report cannot be edited while in PENDING status. | Card_issuing_-_Disputes | 2 | POST /v2/fraud-report;PUT /v2/fraud-report/{fraudReportId} |
| `BDPT0006` | 404 | Fraud Report [123] not found | Card_issuing_-_Disputes | 6 | GET /v1/fraud-report/{fraudReportId}/logs;GET /v2/fee/{fee_id};GET /v2/fraud-report/{fraudReportId} |
| `BDPT0007` | 409 | Fraud Report already created using transaction_id [123] | Card_issuing_-_Disputes | 2 | POST /v2/fraud-report;PUT /v2/fraud-report/{fraudReportId} |
| `BDPT0019` | 400 | Unsupported Fee brand type | Card_issuing_-_Disputes | 1 | POST /v2/fee |
| `BDPT0021` | 422 | Authorized Account is different from request | Card_issuing_-_Disputes | 2 | GET /v2/fee/{fee_id};POST /v2/fee |
| `BDPT0022` | 422 | The 'network_brand_type' [Visa] of the request does not match the 'network' [Mastercard] associated with the Transaction | Card_issuing_-_Disputes | 1 | POST /v2/fee |
| `BDPT0026` | 422 | Unable to retrieve program_id from account_id [1234] | Card_issuing_-_Disputes | 1 | POST /v1/on-us-dispute |
| `BDPT0027` | 422 | Program [1010] is not configured to create an On Us Dispute | Card_issuing_-_Disputes | 1 | POST /v1/on-us-dispute |
| `BW0001` | 404 | No configuration was found. | Core_platform_-_Balance_watcher | 12 | GET /v1/acceptance/processing-code/{processingCode};GET /v1/acceptance/processing-code/{processingCode}/account/{accountId};GET /v1/acceptance/processing-code/{processingCode}/program/{programId} |
| `BW0007` | 500 | An unexpected error happened. | Core_platform_-_Balance_watcher | 18 | GET /v1/acceptance/processing-code/{processingCode};GET /v1/acceptance/processing-code/{processingCode}/account/{accountId};GET /v1/acceptance/processing-code/{processingCode}/program/{programId} |
| `BW0008` | 400 | Invalid request. | Core_platform_-_Balance_watcher | 18 | GET /v1/acceptance/processing-code/{processingCode};GET /v1/acceptance/processing-code/{processingCode}/account/{accountId};GET /v1/acceptance/processing-code/{processingCode}/program/{programId} |
| `BW0031` | 401 | Config creation by account unauthorized. | Core_platform_-_Balance_watcher | 18 | GET /v1/acceptance/processing-code/{processingCode};GET /v1/acceptance/processing-code/{processingCode}/account/{accountId};GET /v1/acceptance/processing-code/{processingCode}/program/{programId} |
| `BW0032` | 409 | Config already exists. | Core_platform_-_Balance_watcher | 6 | POST /v1/acceptance/processing-code/{processingCode};POST /v1/acceptance/processing-code/{processingCode}/account/{accountId};POST /v1/acceptance/processing-code/{processingCode}/program/{programId} |
| `CE0001` | 400;404;409 | Settings not found for Program with id {program_id} and Parameter with id {parameter_id} | Revolving_credit_-_Statements | 8 | DELETE /statements-v2/v1/accounts/{accountId}/minimum-amount-due;DELETE /statements-v2/v1/programs/{programId}/parameters/{parameterId};GET /statements-v2/v1/accounts/{accountId}/minimum-amount-due |
| `CMN0002` | 400 | external_account_id must be a maximum of 60 characters in length | Banking_-_Transaction_banking | 2 | GET /bank-statements/v1/account-balances/{externalAccountId};GET /bank-statements/v1/account-balances/{externalAccountId}/history |
| `CMN9999` | not stated | Internal error | Banking_-_Transaction_banking | 0 |  |
| `DO0002` | 400 | Invalid Request. | Core_platform_-_Payment_methods_admin | 1 | POST /v1/simulations |
| `EABL0001` | not stated | Account balance unknown | Banking_-_Transaction_banking | 0 |  |
| `EACC0000` | 500 | Timeout while executing the request | Banking_-_Transaction_banking;Core_platform_-_Accounts | 7 | GET /accounts/v4/accounts/{accountId}/hierarchy/ascendants;GET /accounts/v4/reasons;GET /accounts/v4/statuses |
| `EACC0003` | 500 | Failed to parse request payload | Core_platform_-_Accounts | 2 | POST /accounts/v4/reasons;POST /accounts/v4/statuses |
| `EACC0004` | 400 | Failed during validation of request payload | Core_platform_-_Accounts | 3 | POST /accounts/v4/reasons;POST /accounts/v4/statuses;POST /accounts/v5/accounts/search |
| `EACC0005` | 400 | One or more parameters with invalid format | Banking_-_Transaction_banking;Core_platform_-_Accounts | 5 | GET /accounts/v4/accounts/{accountId}/hierarchy/ascendants;GET /accounts/v4/reasons;GET /accounts/v4/statuses |
| `EACC0018` | 400;409 | Account reason already exists with key(s): 'Unblocked' | Banking_-_Transaction_banking;Core_platform_-_Accounts | 5 | GET /accounts/v4/reasons;GET /accounts/v4/statuses;GET /corporate/v1/corporate-account-status/reasons |
| `EACC9999` | 500 | Something went wrong, please try again later | Banking_-_Transaction_banking;Core_platform_-_Accounts | 7 | GET /accounts/v4/accounts/{accountId}/hierarchy/ascendants;GET /accounts/v4/reasons;GET /accounts/v4/statuses |
| `EACM0003` | not stated | Configuration not found | Core_platform_-_Accumulator | 0 |  |
| `EBAA0002` | 502 | Bad Gateway Error | Banking_-_Authentication | 1 | POST /banking-auth/v1/credentials |
| `EBAA0003` | 504 | Gateway Timeout | Banking_-_Authentication | 1 | POST /banking-auth/v1/credentials |
| `EBAA0004` | 400 | Invalid payload | Banking_-_Authentication | 1 | POST /banking-auth/v1/credentials |
| `EBAA0007` | 400 | Unsupported Type: (TYPE) and Provider (PROVIDER) | Banking_-_Authentication | 1 | POST /banking-auth/v1/credentials |
| `EBAA0009` | 500 | Encrypted value error. Decrypt returned different value | Banking_-_Authentication | 1 | POST /banking-auth/v1/credentials |
| `EBAA0010` | 500 | Cryptography Decrypt error. Check logs for more details | Banking_-_Authentication | 1 | POST /banking-auth/v1/credentials |
| `EBAA0011` | 500 | Credential Repository Save config error. Check logs for more details | Banking_-_Authentication | 1 | POST /banking-auth/v1/credentials |
| `EBAA0012` | 500 | Credential Repository Get config error. Check logs for more details | Banking_-_Authentication | 1 | POST /banking-auth/v1/credentials |
| `EBAA0014` | 500 | BTG - API configuration not found | Banking_-_Authentication | 1 | POST /banking-auth/v1/credentials |
| `EBCF0317` | 404 | Filter template with ID test-1 not found | Core_platform_-_Balance_config_Beta | 1 | POST /v1/balances-config |
| `EBCF0320` | 400 | Configuration at index 0 must have either filter_template_id or filters.processing_codes | Core_platform_-_Balance_config_Beta | 1 | POST /v1/balances-config |
| `EBCF0321` | 400 | Cannot provide both filters and filter_template_id in the same configuration | Core_platform_-_Balance_config_Beta | 1 | POST /v1/balances-config |
| `EBLC9999` | 500 | An Internal Server Error found, please contact the administrator | Core_platform_-_Balance_config_Beta | 4 | GET /v1/balances-config;GET /v1/balances-config/{configId};POST /v1/balances-config |
| `EBLS9999` | not stated | Internal error found, please contact the administrator | Core_platform_-_Balances_and_limits | 0 |  |
| `EBLT0001` | not stated | Request timeout | Card_issuing_-_Protection_Bulletin | 0 |  |
| `EBLT0003` | not stated | Failed to parse request payload | Card_issuing_-_Protection_Bulletin | 0 |  |
| `EBLT0004` | not stated | Invalid program_id param | Card_issuing_-_Protection_Bulletin | 0 |  |
| `EBLT0005` | not stated | Missing or invalid Authorization header | Card_issuing_-_Protection_Bulletin | 0 |  |
| `EBLT0006` | not stated | Invalid Authorization header, missing account-id | Card_issuing_-_Protection_Bulletin | 0 |  |
| `EBLT0007` | not stated | Invalid Authorization header, missing tenant | Card_issuing_-_Protection_Bulletin | 0 |  |
| `EBLT0009` | not stated | Programs API returned [Not found] using ID: {program_id} | Card_issuing_-_Protection_Bulletin | 0 |  |
| `EBLT9998` | not stated | Something went wrong when try to process a request in Programs API using ID: 123 | Card_issuing_-_Protection_Bulletin | 0 |  |
| `EBLT9999` | not stated | Something went wrong, please try again later | Card_issuing_-_Protection_Bulletin | 0 |  |
| `EBS0009` | 400 | (Field 'code' is required) | Banking_-_TED_configuration | 1 | POST /v1/provider-configuration |
| `EBS0065` | 500 | Error on save configuration | Banking_-_TED_configuration | 1 | POST /v1/provider-configuration |
| `ECAD0000` | 500 | Something went wrong, please try again later | Control_Center_audit_beta | 1 | GET /v1/audit |
| `ECAD0005` | 400 | Key: 'SearchAuditParams.Page' Error:Field validation for 'Page' failed on the 'min' tag | Control_Center_audit_beta | 1 | GET /v1/audit |
| `ECAD0006` | 400 | beginDate must be before or equal to endDate | Control_Center_audit_beta | 1 | GET /v1/audit |
| `ECAD0007` | 400 | Error binding request | Control_Center_audit_beta | 1 | GET /v1/audit |
| `ECM0001` | not stated | Internal error while accessing an external resource | Instant_payments_-_Pix_management | 0 |  |
| `ECM0002` | 400 | Bad request while accessing an external resource | Instant_payments_-_Pix_management | 1 | POST /v2/pix/infraction-reports/{id}/close |
| `ECM0003` | 400 | Received response status %d was not expected | Instant_payments_-_Pix_management | 1 | POST /v2/pix/infraction-reports/{id}/close |
| `ECM0005` | 400 | Failed to marshal request | Instant_payments_-_Pix_management | 1 | POST /v2/pix/infraction-reports/{id}/close |
| `ECMN9999` | 500 | Internal error | Banking_-_Transaction_banking | 5 | DELETE /corporate/v2/scheduled-payments/{scheduledPaymentId};POST /cash-management/v2/payments/confirm;POST /corporate/v1/bulk-settlement |
| `EDPT0001` | 504 | Request timeout | Card_issuing_-_Disputes | 7 | GET /v1/fraud-report/{fraudReportId}/logs;GET /v2/fee/{fee_id};GET /v2/fraud-report/{fraudReportId} |
| `EDPT0002` | 400 | Failed during validation of request payload | Card_issuing_-_Disputes | 2 | POST /v2/fraud-report;PUT /v2/fraud-report/{fraudReportId} |
| `EDPT0003` | 400 | Failed to parse request payload | Card_issuing_-_Disputes | 1 | POST /v2/fee |
| `EDPT0004` | 400 | Failed to parse request payload | Card_issuing_-_Disputes | 4 | GET /v1/fraud-report/{fraudReportId}/logs;GET /v2/fee/{fee_id};GET /v2/fraud-report/{fraudReportId} |
| `EDPT0005` | 401 | Missing or invalid Authorization header | Card_issuing_-_Disputes | 7 | GET /v1/fraud-report/{fraudReportId}/logs;GET /v2/fee/{fee_id};GET /v2/fraud-report/{fraudReportId} |
| `EDPT0009` | 404 | TransactionById returned [Not found] using ID: 1234567890 | Card_issuing_-_Disputes | 2 | POST /v1/on-us-dispute;POST /v2/fee |
| `EDPT9997` | 500 | Something went wrong when try to process a request in Authorizations using ID: 1234 | Card_issuing_-_Disputes | 1 | POST /v1/on-us-dispute |
| `EDPT9998` | 500 | Something went wrong, please try again later | Card_issuing_-_Disputes | 3 | GET /v2/fee/{fee_id};POST /v1/on-us-dispute;POST /v2/fee |
| `EDPT9999` | 500 | Something went wrong, please try again later | Card_issuing_-_Disputes | 5 | GET /v1/fraud-report/{fraudReportId}/logs;GET /v2/fraud-report/{fraudReportId};POST /v1/on-us-dispute |
| `EFCA0001` | not stated | Bad Request | Banking_-_Funds_coverage | 0 |  |
| `EFCA0002` | not stated | Validation error | Banking_-_Funds_coverage | 0 |  |
| `EFCA0006` | not stated | Internal error | Banking_-_Funds_coverage | 0 |  |
| `EFCA0007` | not stated | HTTP request error | Banking_-_Funds_coverage | 0 |  |
| `EFCA0009` | not stated | Resource not found | Banking_-_Funds_coverage | 0 |  |
| `EFCA0010` | not stated | Resource already exists | Banking_-_Funds_coverage | 0 |  |
| `EFCA0011` | not stated | Organization API request error | Banking_-_Funds_coverage | 0 |  |
| `EFCA0012` | not stated | Organization API unmarshal response error | Banking_-_Funds_coverage | 0 |  |
| `EFCA0013` | not stated | Organization API unmapped response code error | Banking_-_Funds_coverage | 0 |  |
| `EFCA0014` | not stated | Organization API 5xx error | Banking_-_Funds_coverage | 0 |  |
| `EFCA0015` | not stated | Organization API 4xx error | Banking_-_Funds_coverage | 0 |  |
| `EFCA0016` | not stated | Organizations API resource not found | Banking_-_Funds_coverage | 0 |  |
| `EIAC0002` | 400 | The header {HeaderName} is required \| The property {PropertyName} is required. \| Can't find [BalanceAccount] with params: [AccountID: XXX, OrgID: XXX]. | Revolving_credit_-_Interest_accruals | 4 | GET /v1/programs/{programId}/accrual-type-post-config;PATCH /v1/programs/{programId}/accrual-type-post-config/{accrualTypePostConfigId};POST /v1/accounts/{accountId}/interest-accruals |
| `EINS0004` | 400 | Contract amount cannot be negative and must contain at most 2 decimal places. | Core_platform_-_Payment_methods | 1 | POST /payment-methods/v1/authorization |
| `EINS0005` | 400 | Principal amount cannot be negative and must contain at most 2 decimal places. | Core_platform_-_Payment_methods | 1 | POST /payment-methods/v1/authorization |
| `EINS0006` | 400 | Principal amount cannot be greater than contract amount. | Core_platform_-_Payment_methods | 1 | POST /payment-methods/v1/authorization |
| `EINS0010` | 400 | Number of installments should be greater than 0. | Core_platform_-_Payment_methods | 1 | POST /payment-methods/v1/authorization |
| `EINS0011` | 400 | Number of installments must be equal to the installments details provided. | Core_platform_-_Payment_methods | 1 | POST /payment-methods/v1/authorization |
| `EINS0012` | 400 | All installments amounts must be greater than 0 and must contain at most 2 decimal places. | Core_platform_-_Payment_methods | 1 | POST /payment-methods/v1/authorization |
| `EINS0015` | 400 | Added installment amounts don't match the contract amount. | Core_platform_-_Payment_methods | 1 | POST /payment-methods/v1/authorization |
| `EINS0016` | 400 | First payment date in the additional financial details is invalid. | Core_platform_-_Payment_methods | 1 | POST /payment-methods/v1/authorization |
| `ELDG500` | 500 | Internal server error | Core_platform_-_Payment_methods | 2 | POST /payments/v1/payments;POST /payments/v2/cancel |
| `ELDG9999` | 500 | An Internal Server Error found, please contact the administrator passing the code | Core_platform_-_Ledger | 2 | GET /v1/accounts/{accountId}/limits;PATCH /v1/accounts/{accountId}/limits |
| `EPAE0001` | 500 | Unexpected error while processing the call to the authentication system. | Core_platform_-_Payment_methods | 7 | POST /payment-methods/v1/authorization;POST /payment-methods/v2/payments;POST /payment-methods/v2/payments/cancel |
| `EPAE0002` | 500 | Timeout error while processing the call to the authentication system. | Core_platform_-_Payment_methods | 7 | POST /payment-methods/v1/authorization;POST /payment-methods/v2/payments;POST /payment-methods/v2/payments/cancel |
| `EPAE0004` | 422 | The method provided in the payload does not exist. | Core_platform_-_Payment_methods | 7 | POST /payment-methods/v1/authorization;POST /payment-methods/v2/payments;POST /payment-methods/v2/payments/cancel |
| `EPCG501` | 500 | Internal server error | Core_platform_-_Payment_methods | 1 | POST /payments/v1/payments |
| `EPT0303` | not stated | Failed during validation of request payload | Seller_management_-_Merchant_advance | 0 |  |
| `ERAT00001` | 500 | Error on request calculations | Core_platform_-_Payment_methods | 1 | POST /payments/v1/payments/force |
| `ERAT00002` | 500 | Failed when transforming data | Core_platform_-_Payment_methods | 1 | POST /payments/v1/payments/force |
| `ERAT00003` | 500 | An Internal Error has occurred. Please try again | Core_platform_-_Payment_methods | 1 | POST /payments/v1/payments/force |
| `ERR4021` | 400 | network respond bad request error | Card_issuing_-_Tokenization | 1 | POST /v1/cards/{card_id} |
| `ERR4091` | 400 | Token not found | Card_issuing_-_Tokenization | 1 | POST /v1/cards/{card_id} |
| `ERR4133` | not stated | Token not found | Card_issuing_-_Tokenization;Card_issuing_-_Visa_Flexible_Credentials | 0 |  |
| `ERR5446` | not stated | Internal server error | Card_issuing_-_Tokenization;Card_issuing_-_Visa_Flexible_Credentials | 0 |  |
| `ERR93836` | not stated | Card profile can't be null | Card_issuing_-_Tokenization | 0 |  |
| `ERR9786` | not stated | Access token is missing or invalid | Card_issuing_-_Tokenization;Card_issuing_-_Visa_Flexible_Credentials | 0 |  |
| `ERR9993` | not stated | card not found | Card_issuing_-_Visa_Flexible_Credentials | 0 |  |
| `ESMA5000` | not stated | Config does not exists | Seller_management_-_Sellers | 0 |  |

## Lifecycle status

Codes in this unit that are mentioned in changelog posts (check the post: it may record that the code was added, changed or removed from some endpoints):

- `EINS0004`: `KU-CHG-7-november-2025`
- `EINS0005`: `KU-CHG-7-november-2025`
- `EINS0006`: `KU-CHG-7-november-2025`
- `EINS0010`: `KU-CHG-7-november-2025`
- `EINS0011`: `KU-CHG-7-november-2025`
- `EINS0012`: `KU-CHG-7-november-2025`
- `EINS0015`: `KU-CHG-7-november-2025`
- `EINS0016`: `KU-CHG-7-november-2025`

## Conflicts, caveats and evidence gaps

- Codes and messages come from response examples in the OpenAPI specifications; the conditions that trigger a code are documented only where the message or the operation description states them.
- The source table recognises only codes made of letters followed by digits; codes with mixed prefixes (for example `WP2P0000`) are not in the table but appear in the API-reference KUs.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-reference-data/error_code_index.csv` | rows with code prefix ACQ, AMON, BA, BBLT, BDPT, BW, CE, CMN, DO, EABL, EACC, EACM, EBAA, EBCF, EBLC, EBLS, EBLT, EBS, ECAD, ECM, ECMN, EDPT, EFCA, EIAC, EINS, ELDG, EPAE, EPCG, EPT, ERAT, ERR, ESMA | https://github.com/PismoDevEx/pismo-api-specs | `76213ae93e90a725…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-API-banking-authentication--provider-credentials` — API reference: Banking - Authentication — Provider credentials
- `KU-API-banking-ted-configuration--configurations` — API reference: Banking - TED configuration — Configurations
- `KU-API-banking-transaction-banking--accounts` — API reference: Banking - Transaction banking — Accounts
- `KU-API-banking-transaction-banking--bank-statements-part-01` — API reference: Banking - Transaction banking — Bank statements (part 1 of 2)
- `KU-API-banking-transaction-banking--bulk-settlement` — API reference: Banking - Transaction banking — Bulk settlement
- `KU-API-banking-transaction-banking--payments-part-03` — API reference: Banking - Transaction banking — Payments (part 3 of 3)
- `KU-API-banking-transaction-banking--payments-pismo-account-id` — API reference: Banking - Transaction banking — Payments (Pismo account ID)
- `KU-API-card-issuing-disputes--fees-v2` — API reference: Card issuing - Disputes — Fees V2
- `KU-API-card-issuing-disputes--fraud-report` — API reference: Card issuing - Disputes — Fraud report
- `KU-API-card-issuing-disputes--on-us` — API reference: Card issuing - Disputes — On-Us
- `KU-API-card-issuing-tokenization--card-lifecycle` — API reference: Card issuing - Tokenization — Card lifecycle
- `KU-API-control-center-audit-beta--audit` — API reference: Control Center — Audit
- `KU-API-core-platform-accounts--accounts` — API reference: Core platform - Accounts — Accounts
- `KU-API-core-platform-accounts--statuses-and-reasons` — API reference: Core platform - Accounts — Statuses and reasons
- `KU-API-core-platform-balance-config-beta--balance-configurations` — API reference: Core platform - Balance configurations — Balance configurations
- `KU-API-core-platform-balance-watcher--limit-acceptance-configurations` — API reference: Core platform - Balance watcher — Limit acceptance configurations
- `KU-API-core-platform-balances-and-limits--account-limits` — API reference: Core platform - Balances and limits — Account limits
- `KU-API-core-platform-ledger--account-limits` — API reference: Core platform - Ledger — Account limits
- `KU-API-core-platform-payment-methods--force-operations` — API reference: Core platform - Payment methods — Force operations
- `KU-API-core-platform-payment-methods--payment-methods-part-01` — API reference: Core platform - Payment methods — Payment methods (part 1 of 3)
- `KU-API-core-platform-payment-methods--payments` — API reference: Core platform - Payment methods — Payments
- `KU-API-core-platform-payment-methods-admin--simulation` — API reference: Core platform - Payment methods admin — Simulation
- `KU-API-instant-payments-pix-management--infraction-reports-part-01` — API reference: Instant payments - Pix management — Infraction reports (part 1 of 2)
- `KU-API-revolving-credit-interest-accruals--accrual-type-post-configurations` — API reference: Revolving credit - Interest accruals — Accrual type post configurations
- `KU-API-revolving-credit-interest-accruals--post-interest-accruals` — API reference: Revolving credit - Interest accruals — Post interest accruals
- `KU-API-revolving-credit-statements--multivalue-program-parameters` — API reference: Revolving credit - Statements — Multivalue program parameters
- `KU-API-revolving-credit-statements--statement-minimum-amount-due` — API reference: Revolving credit - Statements — Statement minimum amount due
- `KU-CHG-7-november-2025` — Changelog: 7 November 2025
