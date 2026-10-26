---
ku_id: KU-ERR-codes-wona
title: 'Error codes: WONA'
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
- KU-API-core-platform-payment-methods--payment-methods-part-01
- KU-CHG-7-november-2025
error_codes:
- WONA0001
- WONA0004
- WONA0005
- WONA0006
- WONA0011
- WONA0012
- WONA0013
- WONA0015
- WONA0016
- WONA0018
- WONA0019
- WONA0020
- WONA0032
- WONA0033
- WONA0036
- WONA039
- WONA040
- WONA041
- WONA042
- WONA043
---

# Error codes: WONA

**KU ID:** `KU-ERR-codes-wona` · **Category:** Errors and troubleshooting · **Type:** error-code catalogue (from reference table)

## Purpose and scope

20 error code(s) with prefix(es) WONA from `api-reference-data/error_code_index.csv`, with the HTTP status, message and the operations whose response examples contain the code. The `operations_sample` column is a sample, not a complete list: the complete set of codes per operation is in the API-reference KUs (section “Error codes shown in this operation's response examples”). Conditions under which a code is returned are documented only where the message or the operation description states them.

## Error codes

| Code | HTTP status | Message | Specification files | Operation count | Operations (sample) |
| --- | --- | --- | --- | --- | --- |
| `WONA0001` | 400 | Authorization Payload is invalid. It must be a valid JSON. | Core_platform_-_Payment_methods | 1 | POST /payment-methods/v1/authorization |
| `WONA0004` | 400 | MTI is required. | Core_platform_-_Payment_methods | 1 | POST /payment-methods/v1/authorization |
| `WONA0005` | 400 | Entry mode is required. | Core_platform_-_Payment_methods | 1 | POST /payment-methods/v1/authorization |
| `WONA0006` | 400 | Processing code is required. | Core_platform_-_Payment_methods | 1 | POST /payment-methods/v1/authorization |
| `WONA0011` | 400 | Number of installments is required and must be greater than 0. | Core_platform_-_Payment_methods | 1 | POST /payment-methods/v1/authorization |
| `WONA0012` | 400 | Amount is required. | Core_platform_-_Payment_methods | 1 | POST /payment-methods/v1/authorization |
| `WONA0013` | 400 | Amount can't be negative. | Core_platform_-_Payment_methods | 1 | POST /payment-methods/v1/authorization |
| `WONA0015` | 400 | Card ID, card number, document number, bank account, bank branch, or account ID is required to identify the account holder." | Core_platform_-_Payment_methods | 1 | POST /payment-methods/v1/authorization |
| `WONA0016` | 400 | Network is required. | Core_platform_-_Payment_methods | 1 | POST /payment-methods/v1/authorization |
| `WONA0018` | 400 | Invalid MTI. | Core_platform_-_Payment_methods | 1 | POST /payment-methods/v1/authorization |
| `WONA0019` | 400 | Entry mode is invalid. It should have two or three characters. | Core_platform_-_Payment_methods | 1 | POST /payment-methods/v1/authorization |
| `WONA0020` | 400 | Original tracking ID or original authorization ID is required to identify the authorization. | Core_platform_-_Payment_methods | 1 | POST /payment-methods/v1/authorization |
| `WONA0032` | 400 | Amount must be greater than zero. | Core_platform_-_Payment_methods | 1 | POST /payment-methods/v1/authorization |
| `WONA0033` | 400 | Beneficiary_id must be a valid UUID. | Core_platform_-_Payment_methods | 1 | POST /payment-methods/v1/authorization |
| `WONA0036` | 400 | Invalid Clearing Type. It must be ONLINE or OFFLINE. | Core_platform_-_Payment_methods | 1 | POST /payment-methods/v1/authorization |
| `WONA039` | 400 | A maximum of 20 digits including two decimals is allowed for the amount field. | Core_platform_-_Payment_methods | 1 | POST /payment-methods/v1/authorization |
| `WONA040` | 400 | The amount must have a maximum of two decimal places. | Core_platform_-_Payment_methods | 1 | POST /payment-methods/v1/authorization |
| `WONA041` | 400 | Tracking ID must not have more than 50 characters. | Core_platform_-_Payment_methods | 1 | POST /payment-methods/v1/authorization |
| `WONA042` | 400 | Authorization date time must be in the UTC-0 RFC3339 format. | Core_platform_-_Payment_methods | 1 | POST /payment-methods/v1/authorization |
| `WONA043` | 400 | Authorization posting date must be in the YYYY-MM-DD format. | Core_platform_-_Payment_methods | 1 | POST /payment-methods/v1/authorization |

## Lifecycle status

Codes in this unit that are mentioned in changelog posts (check the post: it may record that the code was added, changed or removed from some endpoints):

- `WONA0004`: `KU-CHG-7-november-2025`
- `WONA0013`: `KU-CHG-7-november-2025`
- `WONA0015`: `KU-CHG-7-november-2025`
- `WONA0016`: `KU-CHG-7-november-2025`
- `WONA0018`: `KU-CHG-7-november-2025`
- `WONA0019`: `KU-CHG-7-november-2025`
- `WONA0032`: `KU-CHG-7-november-2025`
- `WONA0033`: `KU-CHG-7-november-2025`
- `WONA0036`: `KU-CHG-7-november-2025`
- `WONA039`: `KU-CHG-7-november-2025`
- `WONA040`: `KU-CHG-7-november-2025`
- `WONA041`: `KU-CHG-7-november-2025`
- `WONA042`: `KU-CHG-7-november-2025`
- `WONA043`: `KU-CHG-7-november-2025`

## Conflicts, caveats and evidence gaps

- Codes and messages come from response examples in the OpenAPI specifications; the conditions that trigger a code are documented only where the message or the operation description states them.
- The source table recognises only codes made of letters followed by digits; codes with mixed prefixes (for example `WP2P0000`) are not in the table but appear in the API-reference KUs.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-reference-data/error_code_index.csv` | rows with code prefix WONA | https://github.com/PismoDevEx/pismo-api-specs | `76213ae93e90a725…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-API-core-platform-payment-methods--payment-methods-part-01` — API reference: Core platform - Payment methods — Payment methods (part 1 of 3)
- `KU-CHG-7-november-2025` — Changelog: 7 November 2025
