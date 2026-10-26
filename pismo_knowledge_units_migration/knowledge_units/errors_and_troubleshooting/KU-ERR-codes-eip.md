---
ku_id: KU-ERR-codes-eip
title: 'Error codes: EIP'
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
- KU-API-banking-integrated-payments--bank-slip
- KU-API-banking-integrated-payments--bank-slip-issuance
- KU-API-banking-integrated-payments--ebill-registration
- KU-API-banking-integrated-payments--transfer
- KU-CHG-2-july-2026
error_codes:
- EIP0002
- EIP0003
- EIP0004
- EIP0005
- EIP0006
- EIP0007
- EIP0008
- EIP0009
- EIP0010
- EIP0011
- EIP0012
- EIP0013
- EIP0014
- EIP0015
- EIP0016
- EIP0017
- EIP0018
- EIP0019
- EIP0020
- EIP0021
- EIP0022
- EIP0023
- EIP0024
- EIP0025
- EIP0028
- EIP0029
- EIP0030
- EIP0031
- EIP0041
- EIP0042
- EIP0043
- EIP0045
- EIP0046
- EIP0047
- EIP0049
- EIP0051
- EIP0053
- EIP0061
- EIP0062
- EIP0063
- EIP0065
- EIP0066
- EIP0067
- EIP0069
- EIP0070
- EIP0072
- EIP0073
- EIP0074
- EIP0076
- EIP0077
- EIP0088
- EIP0089
- EIP0090
- EIP0091
---

# Error codes: EIP

**KU ID:** `KU-ERR-codes-eip` · **Category:** Errors and troubleshooting · **Type:** error-code catalogue (from reference table)

## Purpose and scope

54 error code(s) with prefix(es) EIP from `api-reference-data/error_code_index.csv`, with the HTTP status, message and the operations whose response examples contain the code. The `operations_sample` column is a sample, not a complete list: the complete set of codes per operation is in the API-reference KUs (section “Error codes shown in this operation's response examples”). Conditions under which a code is returned are documented only where the message or the operation description states them.

## Error codes

| Code | HTTP status | Message | Specification files | Operation count | Operations (sample) |
| --- | --- | --- | --- | --- | --- |
| `EIP0002` | 504 | API request timeout | Banking_-_Integrated_payments | 2 | POST /v1/bankslips/pay;POST /v1/transfers/cashout |
| `EIP0003` | 400 | Bad Request | Banking_-_Integrated_payments | 2 | DELETE /v1/bankslips-issue/client-requests/{clientRequestId};POST /v1/transfers/cashout |
| `EIP0004` | 500 | HTTP request error | Banking_-_Integrated_payments | 10 | DELETE /v1/bankslips-issue/client-requests/{clientRequestId};DELETE /v1/ebill-registration/accounts/{accountId};GET /v1/bankslips-issue/client-requests/{clientRequestId} |
| `EIP0005` | 400;403 | Missing required header: 'x-tenant' | Banking_-_Integrated_payments | 12 | DELETE /v1/bankslips-issue/client-requests/{clientRequestId};DELETE /v1/ebill-registration/accounts/{accountId};GET /v1/bankslips-issue |
| `EIP0006` | 400;403 | Invalid account id header: 'x-account-id' | Banking_-_Integrated_payments | 12 | DELETE /v1/bankslips-issue/client-requests/{clientRequestId};DELETE /v1/ebill-registration/accounts/{accountId};GET /v1/bankslips-issue |
| `EIP0007` | 500 | Internal error | Banking_-_Integrated_payments | 11 | DELETE /v1/bankslips-issue/client-requests/{clientRequestId};DELETE /v1/ebill-registration/accounts/{accountId};GET /v1/bankslips-issue |
| `EIP0008` | 400 | Validation error | Banking_-_Integrated_payments | 4 | POST /v1/bankslips/pay;POST /v1/bankslips/validate;POST /v1/ebill-registration/accounts/{accountId} |
| `EIP0009` | 403 | Missing required header: 'x-idempotency-key' | Banking_-_Integrated_payments | 3 | POST /v1/bankslips-issue;POST /v1/bankslips/pay;POST /v1/transfers/cashout |
| `EIP0010` | 400 | Unmarshal error | Banking_-_Integrated_payments | 8 | DELETE /v1/bankslips-issue/client-requests/{clientRequestId};GET /v1/bankslips-issue/client-requests/{clientRequestId};GET /v1/bankslips/receipts |
| `EIP0011` | 500 | Accounts API timeout error | Banking_-_Integrated_payments | 8 | DELETE /v1/ebill-registration/accounts/{accountId};GET /v1/bankslips-issue;GET /v1/bankslips/receipts |
| `EIP0012` | 400 | Account not found | Banking_-_Integrated_payments | 8 | DELETE /v1/ebill-registration/accounts/{accountId};GET /v1/bankslips-issue;GET /v1/bankslips/receipts |
| `EIP0013` | 400 | Accounts - API returned 4xx error | Banking_-_Integrated_payments | 8 | DELETE /v1/ebill-registration/accounts/{accountId};GET /v1/bankslips-issue;GET /v1/bankslips/receipts |
| `EIP0014` | 500 | Accounts - API returned 5xx error | Banking_-_Integrated_payments | 6 | DELETE /v1/ebill-registration/accounts/{accountId};GET /v1/bankslips-issue;GET /v1/bankslips/receipts |
| `EIP0015` | 500 | IntlBankAccounts - API timeout error | Banking_-_Integrated_payments | 3 | POST /v1/bankslips-issue;POST /v1/bankslips/pay;POST /v1/transfers/cashout |
| `EIP0016` | 400 | IntlBankAccounts - API Account not found | Banking_-_Integrated_payments | 2 | POST /v1/bankslips-issue;POST /v1/transfers/cashout |
| `EIP0017` | 400 | IntlBankAccounts - API returned 4xx error | Banking_-_Integrated_payments | 3 | POST /v1/bankslips-issue;POST /v1/bankslips/pay;POST /v1/transfers/cashout |
| `EIP0018` | 502 | IntlBankAccounts - API returned 5xx error | Banking_-_Integrated_payments | 3 | POST /v1/bankslips-issue;POST /v1/bankslips/pay;POST /v1/transfers/cashout |
| `EIP0019` | 500 | P2p - API timeout error | Banking_-_Integrated_payments | 2 | POST /v1/bankslips/pay;POST /v1/transfers/cashout |
| `EIP0020` | 400 | P2p - API returned 4xx error | Banking_-_Integrated_payments | 2 | POST /v1/bankslips/pay;POST /v1/transfers/cashout |
| `EIP0021` | 502 | P2p - API returned 5xx error | Banking_-_Integrated_payments | 2 | POST /v1/bankslips/pay;POST /v1/transfers/cashout |
| `EIP0022` | 500 | BankingGatewayAPI - API timeout error | Banking_-_Integrated_payments | 8 | DELETE /v1/bankslips-issue/client-requests/{clientRequestId};DELETE /v1/ebill-registration/accounts/{accountId};GET /v1/bankslips-issue/client-requests/{clientRequestId} |
| `EIP0023` | 400 | BankingGatewayAPI - API returned 4xx error | Banking_-_Integrated_payments | 7 | DELETE /v1/bankslips-issue/client-requests/{clientRequestId};DELETE /v1/ebill-registration/accounts/{accountId};GET /v1/bankslips-issue/client-requests/{clientRequestId} |
| `EIP0024` | 502;504 | BankingGatewayAPI - API returned 5xx error | Banking_-_Integrated_payments | 8 | DELETE /v1/bankslips-issue/client-requests/{clientRequestId};DELETE /v1/ebill-registration/accounts/{accountId};GET /v1/bankslips-issue/client-requests/{clientRequestId} |
| `EIP0025` | 400 | Error unmarshalling request body | Banking_-_Integrated_payments | 1 | DELETE /v1/bankslips-issue/client-requests/{clientRequestId} |
| `EIP0028` | 500 | Transaction database error | Banking_-_Integrated_payments | 4 | GET /v1/transfers;POST /v1/bankslips-issue;POST /v1/bankslips/pay |
| `EIP0029` | 403 | Account blocked or cancelled | Banking_-_Integrated_payments | 5 | GET /v1/bankslips-issue;GET /v1/bankslips/receipts;GET /v1/transfers |
| `EIP0030` | 403 | Entity's account id does not match {x-account-id} header | Banking_-_Integrated_payments | 2 | POST /v1/bankslips/pay;POST /v1/transfers/cashout |
| `EIP0031` | 409 | {x-idempotency-key} already exists | Banking_-_Integrated_payments | 1 | POST /v1/transfers/cashout |
| `EIP0041` | 500 | Bankslips database error | Banking_-_Integrated_payments | 3 | DELETE /v1/bankslips-issue/client-requests/{clientRequestId};GET /v1/bankslips/receipts;POST /v1/bankslips/pay |
| `EIP0042` | 409 | client request id already exists | Banking_-_Integrated_payments | 1 | POST /v1/bankslips-issue |
| `EIP0043` | 404 | Bankslips not found | Banking_-_Integrated_payments | 1 | DELETE /v1/bankslips-issue/client-requests/{clientRequestId} |
| `EIP0045` | 400 | Invalid value for query param 'per_page' | Banking_-_Integrated_payments | 3 | GET /v1/bankslips-issue;GET /v1/bankslips/receipts;GET /v1/transfers |
| `EIP0046` | 400 | Invalid value for datetime query parameter. RFC3339 format must be used | Banking_-_Integrated_payments | 3 | GET /v1/bankslips-issue;GET /v1/bankslips/receipts;GET /v1/transfers |
| `EIP0047` | 400 | Invalid value for query param 'authorization_id' | Banking_-_Integrated_payments | 2 | GET /v1/bankslips/receipts;GET /v1/transfers |
| `EIP0049` | 404 | Convert barcode to digitable line failed | Banking_-_Integrated_payments | 2 | POST /v1/bankslips/pay;POST /v1/bankslips/validate |
| `EIP0051` | 500 | Schedule conciliation error | Banking_-_Integrated_payments | 1 | POST /v1/bankslips/pay |
| `EIP0053` | 500 | Send integrity message error | Banking_-_Integrated_payments | 3 | DELETE /v1/bankslips-issue/client-requests/{clientRequestId};POST /v1/bankslips/pay;POST /v1/transfers/cashout |
| `EIP0061` | 400 | BankingGatewayAPI - Invalid bill for payment | Banking_-_Integrated_payments | 1 | POST /v1/bankslips/pay |
| `EIP0062` | 404 | BankingGatewayAPI - Register data not found in provider | Banking_-_Integrated_payments | 3 | DELETE /v1/bankslips-issue/client-requests/{clientRequestId};DELETE /v1/ebill-registration/accounts/{accountId};GET /v1/bankslips-issue/client-requests/{clientRequestId} |
| `EIP0063` | 409 | Bankslips is already in processing or paid | Banking_-_Integrated_payments | 1 | POST /v1/bankslips/pay |
| `EIP0065` | 409 | BankingGatewayAPI - API returned 409 provider error | Banking_-_Integrated_payments | 8 | DELETE /v1/bankslips-issue/client-requests/{clientRequestId};DELETE /v1/ebill-registration/accounts/{accountId};GET /v1/bankslips-issue/client-requests/{clientRequestId} |
| `EIP0066` | 400 | Invalid query param status | Banking_-_Integrated_payments | 1 | GET /v1/bankslips-issue |
| `EIP0067` | 400 | Invalid query param page | Banking_-_Integrated_payments | 1 | GET /v1/bankslips-issue |
| `EIP0069` | 500 | P2P API - Failed to unmarshal error response body | Banking_-_Integrated_payments | 2 | POST /v1/bankslips/pay;POST /v1/transfers/cashout |
| `EIP0070` | 500 | BankingGateway API - Failed to unmarshal error response body | Banking_-_Integrated_payments | 8 | DELETE /v1/bankslips-issue/client-requests/{clientRequestId};DELETE /v1/ebill-registration/accounts/{accountId};GET /v1/bankslips-issue/client-requests/{clientRequestId} |
| `EIP0072` | 400 | Missing required path parameter {client_request_id} | Banking_-_Integrated_payments | 1 | GET /v1/bankslips-issue/client-requests/{clientRequestId} |
| `EIP0073` | 404 | Bank slip issue not found | Banking_-_Integrated_payments | 1 | GET /v1/bankslips-issue/client-requests/{clientRequestId} |
| `EIP0074` | 500 | Bankslip issue database error | Banking_-_Integrated_payments | 4 | DELETE /v1/bankslips-issue/client-requests/{clientRequestId};GET /v1/bankslips-issue;GET /v1/bankslips-issue/client-requests/{clientRequestId} |
| `EIP0076` | 422 | Bankslips issue ExternalID invalid | Banking_-_Integrated_payments | 1 | DELETE /v1/bankslips-issue/client-requests/{clientRequestId} |
| `EIP0077` | 400 | Address not found for this Account | Banking_-_Integrated_payments | 1 | POST /v1/bankslips-issue |
| `EIP0088` | 404 | Ebill registration not found | Banking_-_Integrated_payments | 2 | DELETE /v1/ebill-registration/accounts/{accountId};GET /v1/ebill-registration/accounts/{accountId} |
| `EIP0089` | 500 | Ebill database error | Banking_-_Integrated_payments | 3 | DELETE /v1/ebill-registration/accounts/{accountId};GET /v1/ebill-registration/accounts/{accountId};POST /v1/ebill-registration/accounts/{accountId} |
| `EIP0090` | 409 | Ebill registration is already being processed | Banking_-_Integrated_payments | 1 | POST /v1/ebill-registration/accounts/{accountId} |
| `EIP0091` | 400 | Ebill registration is not deletable | Banking_-_Integrated_payments | 1 | DELETE /v1/ebill-registration/accounts/{accountId} |

## Lifecycle status

Codes in this unit that are mentioned in changelog posts (check the post: it may record that the code was added, changed or removed from some endpoints):

- `EIP0002`: `KU-CHG-2-july-2026`
- `EIP0004`: `KU-CHG-2-july-2026`
- `EIP0005`: `KU-CHG-2-july-2026`
- `EIP0006`: `KU-CHG-2-july-2026`
- `EIP0007`: `KU-CHG-2-july-2026`
- `EIP0009`: `KU-CHG-2-july-2026`
- `EIP0010`: `KU-CHG-2-july-2026`
- `EIP0011`: `KU-CHG-2-july-2026`
- `EIP0012`: `KU-CHG-2-july-2026`
- `EIP0013`: `KU-CHG-2-july-2026`
- `EIP0014`: `KU-CHG-2-july-2026`
- `EIP0018`: `KU-CHG-2-july-2026`
- `EIP0019`: `KU-CHG-2-july-2026`
- `EIP0020`: `KU-CHG-2-july-2026`
- `EIP0021`: `KU-CHG-2-july-2026`
- `EIP0023`: `KU-CHG-2-july-2026`
- `EIP0024`: `KU-CHG-2-july-2026`
- `EIP0028`: `KU-CHG-2-july-2026`
- `EIP0029`: `KU-CHG-2-july-2026`
- `EIP0030`: `KU-CHG-2-july-2026`
- `EIP0042`: `KU-CHG-2-july-2026`
- `EIP0045`: `KU-CHG-2-july-2026`
- `EIP0046`: `KU-CHG-2-july-2026`
- `EIP0047`: `KU-CHG-2-july-2026`
- `EIP0049`: `KU-CHG-2-july-2026`
- `EIP0053`: `KU-CHG-2-july-2026`
- `EIP0061`: `KU-CHG-2-july-2026`
- `EIP0062`: `KU-CHG-2-july-2026`
- `EIP0063`: `KU-CHG-2-july-2026`
- `EIP0065`: `KU-CHG-2-july-2026`
- `EIP0069`: `KU-CHG-2-july-2026`
- `EIP0070`: `KU-CHG-2-july-2026`
- `EIP0074`: `KU-CHG-2-july-2026`
- `EIP0076`: `KU-CHG-2-july-2026`
- `EIP0077`: `KU-CHG-2-july-2026`
- `EIP0088`: `KU-CHG-2-july-2026`
- `EIP0089`: `KU-CHG-2-july-2026`
- `EIP0090`: `KU-CHG-2-july-2026`
- `EIP0091`: `KU-CHG-2-july-2026`

## Conflicts, caveats and evidence gaps

- Codes and messages come from response examples in the OpenAPI specifications; the conditions that trigger a code are documented only where the message or the operation description states them.
- The source table recognises only codes made of letters followed by digits; codes with mixed prefixes (for example `WP2P0000`) are not in the table but appear in the API-reference KUs.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-reference-data/error_code_index.csv` | rows with code prefix EIP | https://github.com/PismoDevEx/pismo-api-specs | `76213ae93e90a725…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-API-banking-integrated-payments--bank-slip` — API reference: Banking - Integrated payments — Bank slip
- `KU-API-banking-integrated-payments--bank-slip-issuance` — API reference: Banking - Integrated payments — Bank slip issuance
- `KU-API-banking-integrated-payments--ebill-registration` — API reference: Banking - Integrated payments — eBill registration
- `KU-API-banking-integrated-payments--transfer` — API reference: Banking - Integrated payments — Transfer
- `KU-CHG-2-july-2026` — Changelog: 2 July 2026
