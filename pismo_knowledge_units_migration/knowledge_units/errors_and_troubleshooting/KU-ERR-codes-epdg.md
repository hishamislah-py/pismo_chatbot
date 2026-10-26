---
ku_id: KU-ERR-codes-epdg
title: 'Error codes: EPDG'
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
- KU-API-instant-payments-pix-management--infraction-reports-part-01
- KU-API-instant-payments-pix-management--infraction-reports-part-02
- KU-API-instant-payments-pix-management--keys-part-01
error_codes:
- EPDG0000
- EPDG0001
- EPDG0005
- EPDG0006
- EPDG0007
- EPDG0010
- EPDG0011
- EPDG0013
- EPDG0014
- EPDG0016
- EPDG0017
- EPDG0018
- EPDG0019
- EPDG0020
- EPDG0021
- EPDG0035
- EPDG0036
---

# Error codes: EPDG

**KU ID:** `KU-ERR-codes-epdg` · **Category:** Errors and troubleshooting · **Type:** error-code catalogue (from reference table)

## Purpose and scope

17 error code(s) with prefix(es) EPDG from `api-reference-data/error_code_index.csv`, with the HTTP status, message and the operations whose response examples contain the code. The `operations_sample` column is a sample, not a complete list: the complete set of codes per operation is in the API-reference KUs (section “Error codes shown in this operation's response examples”). Conditions under which a code is returned are documented only where the message or the operation description states them.

## Error codes

| Code | HTTP status | Message | Specification files | Operation count | Operations (sample) |
| --- | --- | --- | --- | --- | --- |
| `EPDG0000` | not stated | Timeout while executing the request | Instant_payments_-_Pix_management | 0 |  |
| `EPDG0001` | 400 | Missing x-tenant header | Instant_payments_-_Pix_management | 3 | PATCH /v2/pix/keys;POST /v2/pix/keys;POST /v2/pix/keys/delete |
| `EPDG0005` | 500 | Invalid Pix provider '{provider_name}' | Instant_payments_-_Pix_management | 17 | GET /v2/pix/fraud-markers/{id};GET /v2/pix/infraction-reports;GET /v2/pix/infraction-reports/search |
| `EPDG0006` | 500 | Failed to marshal JSON object | Instant_payments_-_Pix_management | 20 | GET /v2/pix/fraud-markers/{id};GET /v2/pix/infraction-reports;GET /v2/pix/infraction-reports/search |
| `EPDG0007` | 500 | Failed to unmarshal JSON object | Instant_payments_-_Pix_management | 20 | GET /v2/pix/fraud-markers/{id};GET /v2/pix/infraction-reports;GET /v2/pix/infraction-reports/search |
| `EPDG0010` | 500 | I/O error while reading response data: '{details}' | Instant_payments_-_Pix_management | 20 | GET /v2/pix/fraud-markers/{id};GET /v2/pix/infraction-reports;GET /v2/pix/infraction-reports/search |
| `EPDG0011` | 400 | Bad request while accessing the provider service | Instant_payments_-_Pix_management | 3 | PATCH /v2/pix/keys;POST /v2/pix/keys;POST /v2/pix/keys/delete |
| `EPDG0013` | not stated | Unauthorized access to the provider service | Instant_payments_-_Pix_management | 0 |  |
| `EPDG0014` | 404 | Resource not found on the provider service | Instant_payments_-_Pix_management | 6 | GET /v2/pix/keys;PATCH /v2/pix/keys;POST /v2/pix/keys |
| `EPDG0016` | 500 | Provider service returned an internal error while trying to access the resource | Instant_payments_-_Pix_management | 17 | GET /v2/pix/fraud-markers/{id};GET /v2/pix/infraction-reports;GET /v2/pix/infraction-reports/search |
| `EPDG0017` | 503 | Provider service resource is unavailable | Instant_payments_-_Pix_management | 16 | GET /v2/pix/fraud-markers/{id};GET /v2/pix/infraction-reports;GET /v2/pix/infraction-reports/search |
| `EPDG0018` | 400 | Provider service returned a status {http_status} which was not expected | Instant_payments_-_Pix_management | 3 | PATCH /v2/pix/keys;POST /v2/pix/keys;POST /v2/pix/keys/delete |
| `EPDG0019` | 400 | Provider authentication service rejected request due to a client payload misconfiguration | Instant_payments_-_Pix_management | 3 | PATCH /v2/pix/keys;POST /v2/pix/keys;POST /v2/pix/keys/delete |
| `EPDG0020` | not stated | Provider authentication service is unable to complete the request | Instant_payments_-_Pix_management | 0 |  |
| `EPDG0021` | 503 | Provider authentication service is unavailable | Instant_payments_-_Pix_management | 16 | GET /v2/pix/fraud-markers/{id};GET /v2/pix/infraction-reports;GET /v2/pix/infraction-reports/search |
| `EPDG0035` | 400 | Entry owned by different person | Instant_payments_-_Pix_management | 1 | POST /v2/pix/keys |
| `EPDG0036` | 400 | Entry owned by same person, but with different participant | Instant_payments_-_Pix_management | 1 | POST /v2/pix/keys |

## Lifecycle status

- No code in this unit is mentioned in a changelog post.

## Conflicts, caveats and evidence gaps

- Codes and messages come from response examples in the OpenAPI specifications; the conditions that trigger a code are documented only where the message or the operation description states them.
- The source table recognises only codes made of letters followed by digits; codes with mixed prefixes (for example `WP2P0000`) are not in the table but appear in the API-reference KUs.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-reference-data/error_code_index.csv` | rows with code prefix EPDG | https://github.com/PismoDevEx/pismo-api-specs | `76213ae93e90a725…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-API-instant-payments-pix-management--anti-fraud` — API reference: Instant payments - Pix management — Anti-fraud
- `KU-API-instant-payments-pix-management--infraction-reports-part-01` — API reference: Instant payments - Pix management — Infraction reports (part 1 of 2)
- `KU-API-instant-payments-pix-management--infraction-reports-part-02` — API reference: Instant payments - Pix management — Infraction reports (part 2 of 2)
- `KU-API-instant-payments-pix-management--keys-part-01` — API reference: Instant payments - Pix management — Keys (part 1 of 2)
