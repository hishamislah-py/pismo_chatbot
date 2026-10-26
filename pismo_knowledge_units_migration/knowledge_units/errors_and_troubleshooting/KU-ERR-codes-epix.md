---
ku_id: KU-ERR-codes-epix
title: 'Error codes: EPIX'
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
- KU-API-instant-payments-pix-payments--pix-part-01
- KU-API-instant-payments-pix-payments--pix-part-02
- KU-API-instant-payments-pix-payments--scheduled-transfers
error_codes:
- EPIX0003
- EPIX0004
- EPIX0005
- EPIX0007
- EPIX0008
- EPIX0009
- EPIX0010
- EPIX0014
- EPIX0015
- EPIX0017
- EPIX0018
- EPIX0019
- EPIX0020
- EPIX0022
- EPIX0030
- EPIX0031
- EPIX0032
- EPIX0041
- EPIX0042
- EPIX0043
- EPIX0045
- EPIX0046
- EPIX0049
- EPIX0050
- EPIX0051
- EPIX0053
- EPIX0058
- EPIX0059
- EPIX0060
- EPIX0061
- EPIX0062
- EPIX0063
- EPIX0065
- EPIX0067
- EPIX0068
- EPIX0069
- EPIX0070
- EPIX0071
- EPIX0073
- EPIX0074
- EPIX0075
- EPIX0076
- EPIX0077
- EPIX0083
- EPIX0084
- EPIX0085
- EPIX0086
- EPIX0087
- EPIX0089
- EPIX0091
- EPIX0092
- EPIX0095
- EPIX0096
- EPIX0097
- EPIX0098
- EPIX0099
- EPIX0100
- EPIX0101
- EPIX0102
- EPIX0103
- EPIX0108
- EPIX0109
- EPIX0110
- EPIX0111
- EPIX0112
- EPIX0113
- EPIX0114
- EPIX0115
- EPIX0120
- EPIX0122
- EPIX0123
- EPIX0124
- EPIX0125
- EPIX0126
- EPIX0127
- EPIX0128
- EPIX0129
- EPIX0130
- EPIX0131
- EPIX0132
- EPIX0134
- EPIX0135
- EPIX0136
- EPIX0137
- EPIX0138
- EPIX0139
- EPIX0141
- EPIX0142
- EPIX0143
- EPIX0144
- EPIX0146
- EPIX0160
- EPIX0226
- EPIX0227
- EPIX0228
---

# Error codes: EPIX

**KU ID:** `KU-ERR-codes-epix` · **Category:** Errors and troubleshooting · **Type:** error-code catalogue (from reference table)

## Purpose and scope

95 error code(s) with prefix(es) EPIX from `api-reference-data/error_code_index.csv`, with the HTTP status, message and the operations whose response examples contain the code. The `operations_sample` column is a sample, not a complete list: the complete set of codes per operation is in the API-reference KUs (section “Error codes shown in this operation's response examples”). Conditions under which a code is returned are documented only where the message or the operation description states them.

## Error codes

| Code | HTTP status | Message | Specification files | Operation count | Operations (sample) |
| --- | --- | --- | --- | --- | --- |
| `EPIX0003` | 400;404 | Account not found | Instant_payments_-_Pix_payments | 4 | POST /pix/v1/pix/in/reversal;POST /pix/v1/pix/out/schedule;POST /pix/v1/pix/out/transfer |
| `EPIX0004` | 500 | Internal server error | Instant_payments_-_Pix_payments | 9 | DELETE /pix/v1/pix/out/schedule/{scheduler_id};GET /pix/v1/pix/end-to-end/{end_to_end_id}/transaction;GET /pix/v1/pix/out/accounts/{account_id}/schedules |
| `EPIX0005` | 400;500 | Error unmarshalling object | Banking_-_Authentication;Instant_payments_-_Pix_payments | 5 | POST /banking-auth/v1/credentials;POST /pix/v1/pix/in/reversal;POST /pix/v1/pix/out/schedule |
| `EPIX0007` | 500 | HTTP error | Instant_payments_-_Pix_payments | 4 | POST /pix/v1/pix/in/reversal;POST /pix/v1/pix/out/schedule;POST /pix/v1/pix/out/transfer |
| `EPIX0008` | 400;409 | Account blocked or cancelled | Instant_payments_-_Pix_payments | 4 | POST /pix/v1/pix/in/reversal;POST /pix/v1/pix/out/schedule;POST /pix/v1/pix/out/transfer |
| `EPIX0009` | 403 | Missing required header: "x-tenant" | Instant_payments_-_Pix_payments | 9 | DELETE /pix/v1/pix/out/schedule/{scheduler_id};GET /pix/v1/pix/end-to-end/{end_to_end_id}/transaction;GET /pix/v1/pix/out/accounts/{account_id}/schedules |
| `EPIX0010` | 403 | Invalid account id header: "x-account-id" | Instant_payments_-_Pix_payments | 9 | DELETE /pix/v1/pix/out/schedule/{scheduler_id};GET /pix/v1/pix/end-to-end/{end_to_end_id}/transaction;GET /pix/v1/pix/out/accounts/{account_id}/schedules |
| `EPIX0014` | 500 | Database internal Error | Instant_payments_-_Pix_payments | 4 | DELETE /pix/v1/pix/out/schedule/{scheduler_id};POST /pix/v1/pix/in/reversal;POST /pix/v1/pix/out/transfer |
| `EPIX0015` | 400 | x-account-id is not a valid number | Instant_payments_-_Pix_payments | 1 | POST /pix/v1/pix/qrcode/validate |
| `EPIX0017` | 500 | Accounts - API returned 5xx error | Instant_payments_-_Pix_payments | 3 | POST /pix/v1/pix/out/schedule;POST /pix/v1/pix/out/transfer;POST /pix/v1/pix/qrcode/validate |
| `EPIX0018` | 502 | SPI Gateway - API returned error | Instant_payments_-_Pix_payments | 4 | POST /pix/v1/pix/in/reversal;POST /pix/v1/pix/out/schedule;POST /pix/v1/pix/out/transfer |
| `EPIX0019` | 400 | Accounts - API returned 4xx error | Instant_payments_-_Pix_payments | 3 | POST /pix/v1/pix/out/schedule;POST /pix/v1/pix/out/transfer;POST /pix/v1/pix/qrcode/validate |
| `EPIX0020` | 400 | SPI Gateway - API returned 4xx error | Instant_payments_-_Pix_payments | 4 | POST /pix/v1/pix/in/reversal;POST /pix/v1/pix/out/schedule;POST /pix/v1/pix/out/transfer |
| `EPIX0022` | 400 | Invalid CNPJ | Instant_payments_-_Pix_payments | 1 | POST /pix/v1/pix/out/transfer |
| `EPIX0030` | 504 | SPI Gateway - API returned a timeout error | Instant_payments_-_Pix_payments | 4 | POST /pix/v1/pix/in/reversal;POST /pix/v1/pix/out/schedule;POST /pix/v1/pix/out/transfer |
| `EPIX0031` | 429 | SPI Gateway - API returned a rate limit error | Instant_payments_-_Pix_payments | 4 | POST /pix/v1/pix/in/reversal;POST /pix/v1/pix/out/schedule;POST /pix/v1/pix/out/transfer |
| `EPIX0032` | 400 | Error unmarshalling request body | Instant_payments_-_Pix_payments | 4 | POST /pix/v1/pix/out/schedule;POST /pix/v1/pix/out/transfer;POST /pix/v1/pix/qrcode/validate |
| `EPIX0041` | 404 | SPI Gateway - Not found error. Check details | Instant_payments_-_Pix_payments | 4 | POST /pix/v1/pix/in/reversal;POST /pix/v1/pix/out/schedule;POST /pix/v1/pix/out/transfer |
| `EPIX0042` | 500 | Accounts API timeout error | Instant_payments_-_Pix_payments | 3 | POST /pix/v1/pix/out/schedule;POST /pix/v1/pix/out/transfer;POST /pix/v1/pix/qrcode/validate |
| `EPIX0043` | 500 | P2P API timeout error | Instant_payments_-_Pix_payments | 2 | POST /pix/v1/pix/in/reversal;POST /pix/v1/pix/out/transfer |
| `EPIX0045` | 400 | P2P API returned 4xx error | Instant_payments_-_Pix_payments | 2 | POST /pix/v1/pix/in/reversal;POST /pix/v1/pix/out/transfer |
| `EPIX0046` | 500 | P2P API returned 5xx error | Instant_payments_-_Pix_payments | 1 | POST /pix/v1/pix/out/transfer |
| `EPIX0049` | 400 | Validation error | Instant_payments_-_Pix_payments | 4 | POST /pix/v1/pix/in/reversal;POST /pix/v1/pix/out/schedule;POST /pix/v1/pix/out/transfer |
| `EPIX0050` | 504 | IntlBankAccounts - API timeout | Instant_payments_-_Pix_payments | 1 | POST /pix/v1/pix/out/transfer |
| `EPIX0051` | 404;502 | IntlBankAccounts - API returned 5xx error | Instant_payments_-_Pix_payments | 1 | POST /pix/v1/pix/out/transfer |
| `EPIX0053` | 400 | IntlBankAccounts - API returned 4xx error | Instant_payments_-_Pix_payments | 1 | POST /pix/v1/pix/out/transfer |
| `EPIX0058` | 504 | PixDict - API timeout | Instant_payments_-_Pix_payments | 2 | POST /pix/v1/pix/out/transfer;POST /pix/v1/pix/qrcode/validate |
| `EPIX0059` | 404 | PixDict - Not found | Instant_payments_-_Pix_payments | 1 | POST /pix/v1/pix/qrcode/validate |
| `EPIX0060` | 502 | PixDict - API returned 5xx error | Instant_payments_-_Pix_payments | 2 | POST /pix/v1/pix/out/transfer;POST /pix/v1/pix/qrcode/validate |
| `EPIX0061` | 400 | PixDict - API returned 4xx error | Instant_payments_-_Pix_payments | 4 | GET /pix/v1/pix/out/accounts/{account_id}/schedules;GET /pix/v1/pix/receipts;POST /pix/v1/pix/out/transfer |
| `EPIX0062` | 400 | Invalid value for query param. Date must be RFC3339 format | Instant_payments_-_Pix_payments | 1 | GET /pix/v1/pix/receipts |
| `EPIX0063` | 400 | Invalid value for query param. Date must be RFC3339 format | Instant_payments_-_Pix_payments | 1 | GET /pix/v1/pix/receipts |
| `EPIX0065` | 400 | ? must be greater than ? | Instant_payments_-_Pix_payments | 1 | GET /pix/v1/pix/receipts |
| `EPIX0067` | 400 | Requester account id does not match with body account_id | Instant_payments_-_Pix_payments | 1 | POST /pix/v1/pix/out/transfer |
| `EPIX0068` | 400 | Invalid EndToEndID | Instant_payments_-_Pix_payments | 1 | POST /pix/v1/pix/out/transfer |
| `EPIX0069` | 403 | Missing required header: "Idempotency-Key" | Instant_payments_-_Pix_payments | 3 | POST /pix/v1/pix/in/reversal;POST /pix/v1/pix/out/schedule;POST /pix/v1/pix/out/transfer |
| `EPIX0070` | 400;500 | QRCPS API do returned a merchant information without key and url | Instant_payments_-_Pix_payments | 2 | POST /pix/v1/pix/out/transfer;POST /pix/v1/pix/qrcode/validate |
| `EPIX0071` | 409 | Pix transaction already exists | Instant_payments_-_Pix_payments | 2 | POST /pix/v1/pix/in/reversal;POST /pix/v1/pix/out/transfer |
| `EPIX0073` | 504 | QRCPS API timeout error | Instant_payments_-_Pix_payments | 1 | POST /pix/v1/pix/qrcode/validate |
| `EPIX0074` | 400 | QRCPS API returned 4xx error | Instant_payments_-_Pix_payments | 1 | POST /pix/v1/pix/qrcode/validate |
| `EPIX0075` | 502 | QRCPS API returned 5xx error | Instant_payments_-_Pix_payments | 1 | POST /pix/v1/pix/qrcode/validate |
| `EPIX0076` | 400 | QRCPS API do not returned a merchant information | Instant_payments_-_Pix_payments | 1 | POST /pix/v1/pix/qrcode/validate |
| `EPIX0077` | 400 | query parameter is invalid. Should use the last value of "last_id" field | Instant_payments_-_Pix_payments | 1 | GET /pix/v1/pix/receipts |
| `EPIX0083` | 409 | P2P API returned 409 error - Authorization was already refunded/reversed | Instant_payments_-_Pix_payments | 1 | POST /pix/v1/pix/in/reversal |
| `EPIX0084` | 400 | P2P API returned 400 error - Amount cannot exceed the original transaction amount | Instant_payments_-_Pix_payments | 1 | POST /pix/v1/pix/in/reversal |
| `EPIX0085` | 409 | P2P API returned 409 error - Duplicated CorrelationId | Instant_payments_-_Pix_payments | 2 | POST /pix/v1/pix/in/reversal;POST /pix/v1/pix/out/transfer |
| `EPIX0086` | 404;409 | Pix Transaction not found | Instant_payments_-_Pix_payments | 3 | GET /pix/v1/pix/end-to-end/{end_to_end_id}/transaction;POST /pix/v1/pix/in/reversal;POST /pix/v1/pix/transactions/search |
| `EPIX0087` | 404 | Pix TransactionDetail is not found | Instant_payments_-_Pix_payments | 2 | GET /pix/v1/pix/end-to-end/{end_to_end_id}/transaction;POST /pix/v1/pix/transactions/search |
| `EPIX0089` | 500 | P2P returned invalid event date | Instant_payments_-_Pix_payments | 1 | POST /pix/v1/pix/out/transfer |
| `EPIX0091` | 400 | Pix Schedule - schedule date is invalid | Instant_payments_-_Pix_payments | 1 | POST /pix/v1/pix/out/schedule |
| `EPIX0092` | 400 | Pix Schedule - EndToEndId should be provided | Instant_payments_-_Pix_payments | 1 | POST /pix/v1/pix/out/schedule |
| `EPIX0095` | 500 | Pix Schedule - Error marshalling schedule transfer | Instant_payments_-_Pix_payments | 1 | POST /pix/v1/pix/out/schedule |
| `EPIX0096` | 500 | Pix Schedule - Error on start queue scheduler | Instant_payments_-_Pix_payments | 1 | POST /pix/v1/pix/out/schedule |
| `EPIX0097` | 500 | Pix Schedule - Error persisting transaction | Instant_payments_-_Pix_payments | 1 | POST /pix/v1/pix/out/schedule |
| `EPIX0098` | 500 | Pix Schedule - Error persisting scheduled transfers | Instant_payments_-_Pix_payments | 1 | POST /pix/v1/pix/out/schedule |
| `EPIX0099` | 400 | Account id header does not match request body | Instant_payments_-_Pix_payments | 1 | POST /pix/v1/pix/out/schedule |
| `EPIX0100` | 400 | Invalid account id in parameter | Instant_payments_-_Pix_payments | 1 | GET /pix/v1/pix/out/accounts/{account_id}/schedules |
| `EPIX0101` | 404 | Pix Schedule - Error scheduled transfers not found | Instant_payments_-_Pix_payments | 2 | DELETE /pix/v1/pix/out/schedule/{scheduler_id};GET /pix/v1/pix/out/accounts/{account_id}/schedules |
| `EPIX0102` | 403 | Entity"s account id does not match x-account-id header | Instant_payments_-_Pix_payments | 2 | DELETE /pix/v1/pix/out/schedule/{scheduler_id};GET /pix/v1/pix/out/accounts/{account_id}/schedules |
| `EPIX0103` | 400 | Invalid value for datetime query parameter. RFC3339 format must be used | Instant_payments_-_Pix_payments | 1 | GET /pix/v1/pix/out/accounts/{account_id}/schedules |
| `EPIX0108` | 500 | Fail to find banking configs | Instant_payments_-_Pix_payments | 1 | POST /pix/v1/pix/out/transfer |
| `EPIX0109` | 500 | Invalid type for banking config parameter value | Instant_payments_-_Pix_payments | 1 | POST /pix/v1/pix/out/transfer |
| `EPIX0110` | 400 | The amount passed is greater than the current balance | Instant_payments_-_Pix_payments | 1 | POST /pix/v1/pix/out/transfer |
| `EPIX0111` | 403 | Anti fraud API error | Instant_payments_-_Pix_payments | 1 | POST /pix/v1/pix/out/transfer |
| `EPIX0112` | 403 | Rejected by Anti fraud API | Instant_payments_-_Pix_payments | 1 | POST /pix/v1/pix/out/transfer |
| `EPIX0113` | 400 | Beneficiary is not enabled | Instant_payments_-_Pix_payments | 1 | POST /pix/v1/pix/out/transfer |
| `EPIX0114` | 400 | Beneficiary information does not match Payee's information | Instant_payments_-_Pix_payments | 1 | POST /pix/v1/pix/out/transfer |
| `EPIX0115` | 400 | Missing required transaction identification | Instant_payments_-_Pix_payments | 1 | POST /pix/v1/pix/out/transfer |
| `EPIX0120` | 400 | Missing required purchase amount | Instant_payments_-_Pix_payments | 1 | POST /pix/v1/pix/out/transfer |
| `EPIX0122` | 400 | Invalid withdraw amount | Instant_payments_-_Pix_payments | 1 | POST /pix/v1/pix/out/transfer |
| `EPIX0123` | 400 | Required withdrawal | Instant_payments_-_Pix_payments | 1 | POST /pix/v1/pix/out/transfer |
| `EPIX0124` | 400 | Invalid amount | Instant_payments_-_Pix_payments | 1 | POST /pix/v1/pix/out/transfer |
| `EPIX0125` | 400 | Key cannot be sent when `initiation_type` is `MANUAL` | Instant_payments_-_Pix_payments | 1 | POST /pix/v1/pix/out/schedule |
| `EPIX0126` | 400 | Required Key | Instant_payments_-_Pix_payments | 2 | POST /pix/v1/pix/out/schedule;POST /pix/v1/pix/out/transfer |
| `EPIX0127` | 400 | Invalid field size for merchant category code | Instant_payments_-_Pix_payments | 1 | POST /pix/v1/pix/qrcode/validate |
| `EPIX0128` | 400 | Invalid value for transaction currency. Local currency must be used | Instant_payments_-_Pix_payments | 1 | POST /pix/v1/pix/qrcode/validate |
| `EPIX0129` | 400 | Invalid value for transaction amount. Transaction amount must be greater than zero | Instant_payments_-_Pix_payments | 1 | POST /pix/v1/pix/qrcode/validate |
| `EPIX0130` | 400 | Transaction type not found | Instant_payments_-_Pix_payments | 1 | POST /pix/v1/pix/out/transfer |
| `EPIX0131` | 400 | Invalid QR Code, the payload format indicator is invalid | Instant_payments_-_Pix_payments | 1 | POST /pix/v1/pix/qrcode/validate |
| `EPIX0132` | 400;403 | Invalid field size for Idempotency-Key | Instant_payments_-_Pix_payments | 3 | POST /pix/v1/pix/in/reversal;POST /pix/v1/pix/out/schedule;POST /pix/v1/pix/out/transfer |
| `EPIX0134` | 400 | Invalid QR Code, a merchant information cannot contain key and url filled in | Instant_payments_-_Pix_payments | 1 | POST /pix/v1/pix/qrcode/validate |
| `EPIX0135` | 404 | Receipt not found | Instant_payments_-_Pix_payments | 1 | GET /pix/v1/pix/receipts |
| `EPIX0136` | 400 | Missing required initiator document number | Instant_payments_-_Pix_payments | 1 | POST /pix/v1/pix/out/transfer |
| `EPIX0137` | 400 | Invalid value for urgency field. Value must be 'HIGH' | Instant_payments_-_Pix_payments | 1 | POST /pix/v1/pix/out/transfer |
| `EPIX0138` | 400 | Invalid value for transaction type. Value must be 'TRANSFER' | Instant_payments_-_Pix_payments | 1 | POST /pix/v1/pix/out/transfer |
| `EPIX0139` | 400 | Invalid field size for Cid | Instant_payments_-_Pix_payments | 1 | POST /pix/v1/pix/out/transfer |
| `EPIX0141` | 400 | It's not allow transaction to the same AccountID | Instant_payments_-_Pix_payments | 1 | POST /pix/v1/pix/out/transfer |
| `EPIX0142` | 409 | Already exist a transaction with this EndToEnd | Instant_payments_-_Pix_payments | 1 | POST /pix/v1/pix/out/transfer |
| `EPIX0143` | 400 | Invalid country code on QR Code. Must be `BR` | Instant_payments_-_Pix_payments | 1 | POST /pix/v1/pix/qrcode/validate |
| `EPIX0144` | 409 | Error recording the idempotency | Instant_payments_-_Pix_payments | 1 | POST /pix/v1/pix/out/transfer |
| `EPIX0146` | 400 | No Orgs operation found | Instant_payments_-_Pix_payments | 1 | POST /pix/v1/pix/out/transfer |
| `EPIX0160` | 400 | Field transaction_identification can not be filled when initiation_type is MANUAL or DICT | Instant_payments_-_Pix_payments | 1 | POST /pix/v1/pix/out/transfer |
| `EPIX0226` | 400 | Transaction identification not allowed with initiator document number | Instant_payments_-_Pix_payments | 1 | POST /pix/v1/pix/out/transfer |
| `EPIX0227` | 400 | Invalid transaction identification length for payment initiator | Instant_payments_-_Pix_payments | 1 | POST /pix/v1/pix/out/transfer |
| `EPIX0228` | 400 | Invalid transaction identification length for automatic pix | Instant_payments_-_Pix_payments | 1 | POST /pix/v1/pix/out/transfer |

## Lifecycle status

- No code in this unit is mentioned in a changelog post.

## Conflicts, caveats and evidence gaps

- Codes and messages come from response examples in the OpenAPI specifications; the conditions that trigger a code are documented only where the message or the operation description states them.
- The source table recognises only codes made of letters followed by digits; codes with mixed prefixes (for example `WP2P0000`) are not in the table but appear in the API-reference KUs.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-reference-data/error_code_index.csv` | rows with code prefix EPIX | https://github.com/PismoDevEx/pismo-api-specs | `76213ae93e90a725…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-API-banking-authentication--provider-credentials` — API reference: Banking - Authentication — Provider credentials
- `KU-API-instant-payments-pix-payments--pix-part-01` — API reference: Instant payments - Pix payments — Pix (part 1 of 2)
- `KU-API-instant-payments-pix-payments--pix-part-02` — API reference: Instant payments - Pix payments — Pix (part 2 of 2)
- `KU-API-instant-payments-pix-payments--scheduled-transfers` — API reference: Instant payments - Pix payments — Scheduled transfers
