---
ku_id: KU-ERR-codes-epda
title: 'Error codes: EPDA'
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
- KU-API-instant-payments-pix-management--anti-fraud
- KU-API-instant-payments-pix-management--funds-recovery
- KU-API-instant-payments-pix-management--infraction-reports-part-01
- KU-API-instant-payments-pix-management--infraction-reports-part-02
- KU-API-instant-payments-pix-management--keys-part-01
- KU-API-instant-payments-pix-management--keys-part-02
- KU-API-instant-payments-pix-management--participants
error_codes:
- EPDA0000
- EPDA0001
- EPDA0002
- EPDA0003
- EPDA0004
- EPDA0008
- EPDA0009
- EPDA0010
- EPDA0011
- EPDA0018
- EPDA0023
- EPDA0024
- EPDA0025
- EPDA0026
- EPDA0027
- EPDA0028
- EPDA0029
- EPDA0030
- EPDA0038
- EPDA0039
- EPDA0040
- EPDA0041
- EPDA0042
- EPDA0043
- EPDA0049
- EPDA0070
- EPDA0073
- EPDA0075
- EPDA0079
- EPDA0139
- EPDA0148
- EPDA0149
- EPDA0152
- EPDA0160
- EPDA0161
- EPDA0162
- EPDA0166
- EPDA0167
- EPDA0169
- EPDA0174
- EPDA0180
- EPDA01815
- EPDA0187
- EPDA0190
- EPDA0191
- EPDA0192
---

# Error codes: EPDA

**KU ID:** `KU-ERR-codes-epda` · **Category:** Errors and troubleshooting · **Type:** error-code catalogue (from reference table)

## Purpose and scope

46 error code(s) with prefix(es) EPDA from `api-reference-data/error_code_index.csv`, with the HTTP status, message and the operations whose response examples contain the code. The `operations_sample` column is a sample, not a complete list: the complete set of codes per operation is in the API-reference KUs (section “Error codes shown in this operation's response examples”). Conditions under which a code is returned are documented only where the message or the operation description states them.

## Error codes

| Code | HTTP status | Message | Specification files | Operation count | Operations (sample) |
| --- | --- | --- | --- | --- | --- |
| `EPDA0000` | 202;400;403;404;409;504 | Refund deadline expired. Must initiate refund within 72 hours after ANALYSED status | Instant_payments_-_Pix_management | 8 | GET /v1/pix/funds-recoveries;GET /v1/pix/funds-recoveries/{funds_recovery_id};GET /v1/pix/funds-recoveries/{funds_recovery_id}/infractions |
| `EPDA0001` | 400 | root_transaction_id must be 32 characters long | Instant_payments_-_Pix_management | 7 | GET /v2/pix/infraction-reports;GET /v2/pix/infraction-reports/search;GET /v2/pix/infraction-reports/{id} |
| `EPDA0002` | 400 | Failed to unmarshal request body | Instant_payments_-_Pix_management | 10 | GET /v2/pix/infraction-reports;GET /v2/pix/infraction-reports/search;PATCH /v2/pix/keys |
| `EPDA0003` | 400 | There are invalid fields when trying to validate request body. | Instant_payments_-_Pix_management | 9 | GET /v2/pix/infraction-reports;GET /v2/pix/infraction-reports/search;PATCH /v2/pix/keys |
| `EPDA0004` | 500 | Internal error | Instant_payments_-_Pix_management | 3 | GET /v2/pix/dict/participants;GET /v2/pix/statistics;POST /v2/pix/keys/validate |
| `EPDA0008` | 409 | Account blocked or cancelled | Instant_payments_-_Pix_management | 1 | POST /v2/pix/keys/validate |
| `EPDA0009` | 403 | Missing required header 'x-tenant' | Instant_payments_-_Pix_management | 1 | GET /v2/pix/dict/participants |
| `EPDA0010` | not stated | Missing required header 'x-account-id' | Instant_payments_-_Pix_management | 0 |  |
| `EPDA0011` | 400 | Missing required header: 'x-account-id' | Instant_payments_-_Pix_management | 1 | POST /v2/pix/keys/validate |
| `EPDA0018` | 502 | SPI Gateway - API returned error | Instant_payments_-_Pix_management | 2 | GET /v2/pix/dict/participants;POST /v2/pix/keys/validate |
| `EPDA0023` | 404 | Participant not found for org {orgId} | Instant_payments_-_Pix_management | 1 | POST /v2/pix/keys |
| `EPDA0024` | 404 | Account not found for ID {account_id} | Instant_payments_-_Pix_management | 5 | GET /v2/pix/keys;PATCH /v2/pix/keys;POST /v2/pix/keys |
| `EPDA0025` | 409 | Key already exists in database | Instant_payments_-_Pix_management | 1 | POST /v2/pix/keys |
| `EPDA0026` | 404 | Key not found | Instant_payments_-_Pix_management | 3 | PATCH /v2/pix/keys;POST /v2/pix/keys/delete;POST /v2/pix/keys/search |
| `EPDA0027` | 409 | Key has open claim | Instant_payments_-_Pix_management | 1 | POST /v2/pix/keys/delete |
| `EPDA0028` | 409 | Account status blocked or cancelled | Instant_payments_-_Pix_management | 6 | GET /v2/pix/keys;PATCH /v2/pix/keys;POST /v2/pix/keys |
| `EPDA0029` | 500 | Internal errors while attempting to communicate with the provider service | Instant_payments_-_Pix_management | 17 | GET /v2/pix/fraud-markers/{id};GET /v2/pix/infraction-reports;GET /v2/pix/infraction-reports/search |
| `EPDA0030` | 504 | SPI Gateway - API returned a timeout error | Instant_payments_-_Pix_management | 2 | GET /v2/pix/dict/participants;POST /v2/pix/keys/validate |
| `EPDA0038` | 400 | Invalid Key Type | Instant_payments_-_Pix_management | 3 | GET /v2/pix/keys;POST /v2/pix/keys;POST /v2/pix/keys/delete |
| `EPDA0039` | 400 | Invalid CPF | Instant_payments_-_Pix_management | 2 | POST /v2/pix/keys;POST /v2/pix/keys/delete |
| `EPDA0040` | 400 | Invalid CNPJ | Instant_payments_-_Pix_management | 2 | POST /v2/pix/keys;POST /v2/pix/keys/delete |
| `EPDA0041` | 400 | Invalid PHONE | Instant_payments_-_Pix_management | 2 | POST /v2/pix/keys;POST /v2/pix/keys/delete |
| `EPDA0042` | 400 | Invalid EMAIL | Instant_payments_-_Pix_management | 2 | POST /v2/pix/keys;POST /v2/pix/keys/delete |
| `EPDA0043` | 400 | Invalid EVP | Instant_payments_-_Pix_management | 2 | POST /v2/pix/keys;POST /v2/pix/keys/delete |
| `EPDA0049` | 400;404 | Infraction report not found | Instant_payments_-_Pix_management | 3 | POST /v2/pix/infraction-reports/{id}/cancel;POST /v2/pix/infraction-reports/{id}/close;POST /v2/pix/keys/validate |
| `EPDA0070` | 400 | Invalid request infraction report id | Instant_payments_-_Pix_management | 4 | GET /v2/pix/infraction-reports/{id};PATCH /v2/pix/infraction-reports/{id};POST /v2/pix/infraction-reports/{id}/cancel |
| `EPDA0073` | 400 | Infraction cannot be cancel it is possible to only close the infraction | Instant_payments_-_Pix_management | 1 | POST /v2/pix/infraction-reports/{id}/cancel |
| `EPDA0075` | 400 | Invalid document number | Instant_payments_-_Pix_management | 2 | POST /v2/pix/statistics/keys;POST /v2/pix/statistics/persons |
| `EPDA0079` | 404 | Transaction not found | Instant_payments_-_Pix_management | 1 | POST /v1/pix/funds-recoveries |
| `EPDA0139` | 400;404 | Participant not found for organization | Instant_payments_-_Pix_management | 1 | POST /v2/pix/keys/validate |
| `EPDA0148` | not stated | Infraction registration will continue asynchronously | Instant_payments_-_Pix_management | 0 |  |
| `EPDA0149` | not stated | Infraction cancel will continue asynchronously | Instant_payments_-_Pix_management | 0 |  |
| `EPDA0152` | not stated | Missing required param 'id' | Instant_payments_-_Pix_management | 0 |  |
| `EPDA0160` | not stated | Claim cancel will continue asynchronously | Instant_payments_-_Pix_management | 0 |  |
| `EPDA0161` | not stated | Claim complete will continue asynchronously | Instant_payments_-_Pix_management | 0 |  |
| `EPDA0162` | not stated | Claim confirmation will continue asynchronously | Instant_payments_-_Pix_management | 0 |  |
| `EPDA0166` | 409 | Fraud marker already registered with different values for the idempotency key | Instant_payments_-_Pix_management | 1 | POST /v2/pix/fraud-markers |
| `EPDA0167` | 404 | Fraud marker not found | Instant_payments_-_Pix_management | 3 | GET /v2/pix/fraud-markers/{id};POST /v2/pix/fraud-markers/list;POST /v2/pix/fraud-markers/{id}/cancel |
| `EPDA0169` | 202 | Funds recovery creation will continue asynchronously. Monitor events for completion. | Instant_payments_-_Pix_management | 1 | POST /v1/pix/funds-recoveries |
| `EPDA0174` | not stated | Refund flow will continue asynchronously | Instant_payments_-_Pix_management | 0 |  |
| `EPDA0180` | not stated | Claim creation will continue asynchronously | Instant_payments_-_Pix_management | 0 |  |
| `EPDA01815` | 400 | Entity's account customer id is null | Instant_payments_-_Pix_management | 1 | POST /v2/pix/keys/validate |
| `EPDA0187` | 404 | SPI Dict Gateway - Not found | Instant_payments_-_Pix_management | 1 | GET /v2/pix/dict/participants |
| `EPDA0190` | 409 | An active funds recovery already exists for the given root transaction | Instant_payments_-_Pix_management | 1 | POST /v1/pix/funds-recoveries |
| `EPDA0191` | 422 | Transaction is outside the 80-day eligibility period for funds recovery | Instant_payments_-_Pix_management | 1 | POST /v1/pix/funds-recoveries |
| `EPDA0192` | 400;422 | Funds recovery cannot be initiated for this transaction due to its current status | Instant_payments_-_Pix_management | 1 | POST /v1/pix/funds-recoveries |

## Lifecycle status

- No code in this unit is mentioned in a changelog post.

## Conflicts, caveats and evidence gaps

- Codes and messages come from response examples in the OpenAPI specifications; the conditions that trigger a code are documented only where the message or the operation description states them.
- The source table recognises only codes made of letters followed by digits; codes with mixed prefixes (for example `WP2P0000`) are not in the table but appear in the API-reference KUs.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-reference-data/error_code_index.csv` | rows with code prefix EPDA | https://github.com/PismoDevEx/pismo-api-specs | `76213ae93e90a725…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-API-instant-payments-pix-management--anti-fraud` — API reference: Instant payments - Pix management — Anti-fraud
- `KU-API-instant-payments-pix-management--funds-recovery` — API reference: Instant payments - Pix management — Funds recovery
- `KU-API-instant-payments-pix-management--infraction-reports-part-01` — API reference: Instant payments - Pix management — Infraction reports (part 1 of 2)
- `KU-API-instant-payments-pix-management--infraction-reports-part-02` — API reference: Instant payments - Pix management — Infraction reports (part 2 of 2)
- `KU-API-instant-payments-pix-management--keys-part-01` — API reference: Instant payments - Pix management — Keys (part 1 of 2)
- `KU-API-instant-payments-pix-management--keys-part-02` — API reference: Instant payments - Pix management — Keys (part 2 of 2)
- `KU-API-instant-payments-pix-management--participants` — API reference: Instant payments - Pix management — Participants
