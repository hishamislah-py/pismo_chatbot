---
ku_id: KU-ERR-codes-eiba
title: 'Error codes: EIBA'
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
- KU-API-banking-bank-accounts--bank-accounts-part-01
- KU-API-banking-bank-accounts--bank-accounts-part-02
- KU-API-banking-bank-accounts--beneficiaries
- KU-CHG-5-december-2025
error_codes:
- EIBA0005
- EIBA0006
- EIBA0007
- EIBA0009
- EIBA0010
- EIBA0011
- EIBA0012
- EIBA0013
- EIBA0015
- EIBA0016
- EIBA0017
- EIBA0018
- EIBA0019
- EIBA0020
- EIBA0021
- EIBA0022
- EIBA0023
- EIBA0024
- EIBA0028
- EIBA0029
- EIBA0030
---

# Error codes: EIBA

**KU ID:** `KU-ERR-codes-eiba` · **Category:** Errors and troubleshooting · **Type:** error-code catalogue (from reference table)

## Purpose and scope

21 error code(s) with prefix(es) EIBA from `api-reference-data/error_code_index.csv`, with the HTTP status, message and the operations whose response examples contain the code. The `operations_sample` column is a sample, not a complete list: the complete set of codes per operation is in the API-reference KUs (section “Error codes shown in this operation's response examples”). Conditions under which a code is returned are documented only where the message or the operation description states them.

## Error codes

| Code | HTTP status | Message | Specification files | Operation count | Operations (sample) |
| --- | --- | --- | --- | --- | --- |
| `EIBA0005` | 400;404;500 | Invalid sort code path parameter, expected 6-digit number | Banking_-_Bank_accounts | 18 | DELETE /v1/beneficiaries/{beneficiaryId};DELETE /v2/accounts/{accountId}/bank-accounts/{schemeName};GET /v1/beneficiaries |
| `EIBA0006` | 403 | Missing required header: 'x-tenant' | Banking_-_Bank_accounts | 17 | DELETE /v1/beneficiaries/{beneficiaryId};DELETE /v2/accounts/{accountId}/bank-accounts/{schemeName};GET /v1/beneficiaries |
| `EIBA0007` | 403 | Invalid account ID header: 'x-account-id' | Banking_-_Bank_accounts | 16 | DELETE /v1/beneficiaries/{beneficiaryId};DELETE /v2/accounts/{accountId}/bank-accounts/{schemeName};GET /v1/beneficiaries |
| `EIBA0009` | 400 | Validation error | Banking_-_Bank_accounts | 10 | PATCH /v1/beneficiaries/{beneficiaryId};POST /v1/beneficiaries;POST /v2/accounts/{accountId}/bank-accounts/ach |
| `EIBA0010` | 404 | Account not found | Banking_-_Bank_accounts | 16 | DELETE /v1/beneficiaries/{beneficiaryId};DELETE /v2/accounts/{accountId}/bank-accounts/{schemeName};GET /v1/beneficiaries |
| `EIBA0011` | 500 | Accounts - API returned 5xx error | Banking_-_Bank_accounts | 18 | DELETE /v1/beneficiaries/{beneficiaryId};DELETE /v2/accounts/{accountId}/bank-accounts/{schemeName};GET /v1/beneficiaries |
| `EIBA0012` | 400 | Accounts - API returned 4xx error | Banking_-_Bank_accounts | 17 | DELETE /v1/beneficiaries/{beneficiaryId};DELETE /v2/accounts/{accountId}/bank-accounts/{schemeName};GET /v1/beneficiaries |
| `EIBA0013` | 500 | Accounts - API timeout | Banking_-_Bank_accounts | 17 | DELETE /v1/beneficiaries/{beneficiaryId};DELETE /v2/accounts/{accountId}/bank-accounts/{schemeName};GET /v1/beneficiaries |
| `EIBA0015` | 500 | Database internal error | Banking_-_Bank_accounts | 18 | DELETE /v1/beneficiaries/{beneficiaryId};DELETE /v2/accounts/{accountId}/bank-accounts/{schemeName};GET /v1/beneficiaries |
| `EIBA0016` | 400 | Account ID in header does not match account ID in request body | Banking_-_Bank_accounts | 8 | DELETE /v1/beneficiaries/{beneficiaryId};DELETE /v2/accounts/{accountId}/bank-accounts/{schemeName};GET /v1/beneficiaries/{beneficiaryId} |
| `EIBA0017` | 409 | Beneficiary - Already Exists | Banking_-_Bank_accounts | 1 | POST /v1/beneficiaries |
| `EIBA0018` | 400 | Invalid value for query param 'perPage' | Banking_-_Bank_accounts | 1 | GET /v1/beneficiaries |
| `EIBA0019` | 400 | Invalid value for datetime query parameter. RFC3339 format must be used | Banking_-_Bank_accounts | 1 | GET /v1/beneficiaries |
| `EIBA0020` | 400 | Invalid value for boolean query parameter | Banking_-_Bank_accounts | 1 | GET /v1/beneficiaries |
| `EIBA0021` | 400 | Invalid value for UUID path parameter | Banking_-_Bank_accounts | 4 | DELETE /v1/beneficiaries/{beneficiaryId};GET /v1/beneficiaries/{beneficiaryId};PATCH /v1/beneficiaries/{beneficiaryId} |
| `EIBA0022` | 404 | IntlBankAccount not found | Banking_-_Bank_accounts | 5 | DELETE /v1/beneficiaries/{beneficiaryId};GET /v1/beneficiaries/{beneficiaryId};GET /v2/accounts/{accountId}/bank-accounts/{schemeName} |
| `EIBA0023` | 403 | Account status not NORMAL | Banking_-_Bank_accounts | 16 | DELETE /v1/beneficiaries/{beneficiaryId};DELETE /v2/accounts/{accountId}/bank-accounts/{schemeName};GET /v1/beneficiaries |
| `EIBA0024` | 400 | Request body contains no fields that can be updated | Banking_-_Bank_accounts | 1 | PATCH /v1/beneficiaries/{beneficiaryId} |
| `EIBA0028` | 409 | IntlBankAccount - Already Exists | Banking_-_Bank_accounts | 7 | POST /v2/accounts/{accountId}/bank-accounts/ach;POST /v2/accounts/{accountId}/bank-accounts/bban;POST /v2/accounts/{accountId}/bank-accounts/brazil |
| `EIBA0029` | 404 | IntlBankAccount not found | Banking_-_Bank_accounts | 1 | POST /v3/bank-accounts/{schemeName}/search |
| `EIBA0030` | 400 | Invalid value for scheme_name | Banking_-_Bank_accounts | 1 | GET /v2/accounts/{accountId}/bank-accounts/{schemeName} |

## Lifecycle status

Codes in this unit that are mentioned in changelog posts (check the post: it may record that the code was added, changed or removed from some endpoints):

- `EIBA0007`: `KU-CHG-5-december-2025`

## Conflicts, caveats and evidence gaps

- Codes and messages come from response examples in the OpenAPI specifications; the conditions that trigger a code are documented only where the message or the operation description states them.
- The source table recognises only codes made of letters followed by digits; codes with mixed prefixes (for example `WP2P0000`) are not in the table but appear in the API-reference KUs.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-reference-data/error_code_index.csv` | rows with code prefix EIBA | https://github.com/PismoDevEx/pismo-api-specs | `76213ae93e90a725…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-API-banking-bank-accounts--bank-accounts-part-01` — API reference: Banking - Bank accounts — Bank accounts (part 1 of 2)
- `KU-API-banking-bank-accounts--bank-accounts-part-02` — API reference: Banking - Bank accounts — Bank accounts (part 2 of 2)
- `KU-API-banking-bank-accounts--beneficiaries` — API reference: Banking - Bank accounts — Beneficiaries
- `KU-CHG-5-december-2025` — Changelog: 5 December 2025
