---
ku_id: KU-ERR-codes-eibacc
title: 'Error codes: EIBACC'
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
- KU-API-banking-interest-bearing-accounts--account-attachment
- KU-API-banking-interest-bearing-accounts--deposit-account-open
- KU-API-banking-interest-bearing-accounts--penalty
- KU-API-banking-interest-bearing-accounts--product
- KU-API-banking-interest-bearing-accounts--program-attachment
- KU-CHG-2-october-2026
- KU-CHG-4-september-2026
- KU-CHG-5-december-2025
error_codes:
- EIBACC0005
- EIBACC0007
- EIBACC0008
- EIBACC0015
- EIBACC0018
- EIBACC0064
- EIBACC0065
- EIBACC0066
- EIBACC0103
- EIBACC0104
- EIBACC0106
- EIBACC0107
- EIBACC0108
- EIBACC0109
- EIBACC0110
- EIBACC0113
- EIBACC0114
- EIBACC0204
- EIBACC0226
- EIBACC0236
- EIBACC0284
- EIBACC0294
- EIBACC0295
- EIBACC0296
- EIBACC0297
- EIBACC0298
- EIBACC0299
- EIBACC0301
- EIBACC0302
- EIBACC0303
- EIBACC0304
- EIBACC0305
- EIBACC0306
- EIBACC0307
- EIBACC0308
- EIBACC0309
- EIBACC0310
- EIBACC0311
- EIBACC0312
- EIBACC0314
- EIBACC0315
- EIBACC0316
- EIBACC0317
- EIBACC0318
- EIBACC0319
- EIBACC0320
- EIBACC0321
- EIBACC0322
- EIBACC0324
- EIBACC0325
- EIBACC0328
- EIBACC0329
- EIBACC0330
- EIBACC0331
- EIBACC0338
- EIBACC0379
- EIBACC0380
- EIBACC0393
- EIBACC0396
---

# Error codes: EIBACC

**KU ID:** `KU-ERR-codes-eibacc` · **Category:** Errors and troubleshooting · **Type:** error-code catalogue (from reference table)

## Purpose and scope

59 error code(s) with prefix(es) EIBACC from `api-reference-data/error_code_index.csv`, with the HTTP status, message and the operations whose response examples contain the code. The `operations_sample` column is a sample, not a complete list: the complete set of codes per operation is in the API-reference KUs (section “Error codes shown in this operation's response examples”). Conditions under which a code is returned are documented only where the message or the operation description states them.

## Error codes

| Code | HTTP status | Message | Specification files | Operation count | Operations (sample) |
| --- | --- | --- | --- | --- | --- |
| `EIBACC0005` | 403 | Missing required header: 'x-tenant' | Banking_-_Interest-bearing_accounts | 2 | POST /v1/deposits/accounts/open;POST /v1/deposits/accounts/{accountId}/penalty-simulation |
| `EIBACC0007` | 500 | Internal error | Banking_-_Interest-bearing_accounts | 6 | PATCH /v1/deposits/accounts/{accountId}/attachment;PATCH /v1/deposits/programs/{programId}/attachment;POST /v1/deposits/accounts/open |
| `EIBACC0008` | 400 | Validation error | Banking_-_Interest-bearing_accounts | 4 | POST /v1/deposits/accounts/open;POST /v1/deposits/accounts/{accountId}/attach;POST /v1/deposits/accounts/{accountId}/penalty-simulation |
| `EIBACC0015` | 400 | Invalid accountId path param | Banking_-_Interest-bearing_accounts | 1 | POST /v1/deposits/accounts/{accountId}/penalty-simulation |
| `EIBACC0018` | 400 | Accounts API - Request returned error 4xx | Banking_-_Interest-bearing_accounts | 1 | POST /v1/deposits/accounts/open |
| `EIBACC0064` | 404 | Product not found | Banking_-_Interest-bearing_accounts | 2 | POST /v1/deposits/accounts/open;POST /v1/deposits/accounts/{accountId}/penalty-simulation |
| `EIBACC0065` | 400 | Product Type is not valid | Banking_-_Interest-bearing_accounts | 1 | POST /v1/deposits/accounts/open |
| `EIBACC0066` | 500 | Failed on get product | Banking_-_Interest-bearing_accounts | 1 | POST /v1/deposits/accounts/open |
| `EIBACC0103` | 400 | Programs API - Request returned error 4xx | Banking_-_Interest-bearing_accounts | 1 | POST /v1/deposits/accounts/open |
| `EIBACC0104` | 403 | Account status isn't NORMAL | Banking_-_Interest-bearing_accounts | 1 | POST /v1/deposits/accounts/open |
| `EIBACC0106` | 409 | The product ID provided is already attached | Banking_-_Interest-bearing_accounts | 2 | POST /v1/deposits/accounts/open;POST /v1/deposits/programs/{programId}/attach |
| `EIBACC0107` | 400 | Informed program or account already has an attached product | Banking_-_Interest-bearing_accounts | 1 | POST /v1/deposits/accounts/open |
| `EIBACC0108` | 400 | Product isn't ACTIVE. Activate to proceed with the attachment | Banking_-_Interest-bearing_accounts | 1 | POST /v1/deposits/accounts/open |
| `EIBACC0109` | 400 | Maturity period is below the configured MinTerm of the product | Banking_-_Interest-bearing_accounts | 2 | PATCH /v1/deposits/accounts/{accountId}/attachment;POST /v1/deposits/accounts/open |
| `EIBACC0110` | 400 | Maturity period is above the configured MaxTerm of the product | Banking_-_Interest-bearing_accounts | 2 | PATCH /v1/deposits/accounts/{accountId}/attachment;POST /v1/deposits/accounts/open |
| `EIBACC0113` | 404 | Product attachment not found | Banking_-_Interest-bearing_accounts | 2 | PATCH /v1/deposits/accounts/{accountId}/attachment;PATCH /v1/deposits/programs/{programId}/attachment |
| `EIBACC0114` | 409 | Product is already detached | Banking_-_Interest-bearing_accounts | 2 | POST /v1/deposits/accounts/{accountId}/detach;POST /v1/savings-accounts/accounts/{accountId}/detach |
| `EIBACC0204` | 500 | Get Penalty error | Banking_-_Interest-bearing_accounts | 1 | POST /v1/deposits/accounts/{accountId}/penalty-simulation |
| `EIBACC0226` | 404 | Account not found | Banking_-_Interest-bearing_accounts | 1 | POST /v1/deposits/accounts/{accountId}/penalty-simulation |
| `EIBACC0236` | 400 | Product cannot be attached before its start date | Banking_-_Interest-bearing_accounts | 1 | POST /v1/deposits/accounts/open |
| `EIBACC0284` | 400 | Payout account is configured but is invalid | Banking_-_Interest-bearing_accounts | 1 | POST /v1/deposits/accounts/open |
| `EIBACC0294` | 422 | withdrawalDate must not be in the past | Banking_-_Interest-bearing_accounts | 1 | POST /v1/deposits/accounts/{accountId}/penalty-simulation |
| `EIBACC0295` | 422 | Penalty simulation is only available for deposit accounts | Banking_-_Interest-bearing_accounts | 1 | POST /v1/deposits/accounts/{accountId}/penalty-simulation |
| `EIBACC0296` | 422 | No penalty is configured for the product attached to this account | Banking_-_Interest-bearing_accounts | 1 | POST /v1/deposits/accounts/{accountId}/penalty-simulation |
| `EIBACC0297` | 422 | Program is not valid for attachment. Program must be DEBIT type and ACTIVE status | Banking_-_Interest-bearing_accounts | 1 | POST /v1/deposits/accounts/open |
| `EIBACC0298` | 400 | Validation error | Banking_-_Interest-bearing_accounts | 2 | PATCH /v1/deposits/accounts/{accountId}/attachment;POST /v1/deposits/accounts/open |
| `EIBACC0299` | 400 | Validation error | Banking_-_Interest-bearing_accounts | 2 | PATCH /v1/deposits/accounts/{accountId}/attachment;POST /v1/deposits/accounts/open |
| `EIBACC0301` | 409 | Product attachment is not active | Banking_-_Interest-bearing_accounts | 2 | PATCH /v1/deposits/accounts/{accountId}/attachment;PATCH /v1/deposits/programs/{programId}/attachment |
| `EIBACC0302` | 422 | Internal payout account validation failed. Account does not exist | Banking_-_Interest-bearing_accounts | 2 | PATCH /v1/deposits/accounts/{accountId};PATCH /v1/savings-accounts/accounts/{accountId} |
| `EIBACC0303` | 400 | New attachments are not allowed after the deposit product end_date. | Banking_-_Interest-bearing_accounts | 1 | POST /v1/deposits/accounts/open |
| `EIBACC0304` | 500 | Failed to schedule override expiration | Banking_-_Interest-bearing_accounts | 2 | POST /v1/deposits/accounts/{accountId}/attach;POST /v1/deposits/programs/{programId}/attach |
| `EIBACC0305` | 400 | Validation error | Banking_-_Interest-bearing_accounts | 2 | PATCH /v1/deposits/accounts/{accountId}/attachment;POST /v1/deposits/accounts/open |
| `EIBACC0306` | 400 | Validation error | Banking_-_Interest-bearing_accounts | 2 | PATCH /v1/deposits/accounts/{accountId}/attachment;POST /v1/deposits/accounts/open |
| `EIBACC0307` | 400 | Validation error | Banking_-_Interest-bearing_accounts | 2 | PATCH /v1/deposits/accounts/{accountId}/attachment;POST /v1/deposits/accounts/open |
| `EIBACC0308` | 400 | valid_until must be a future datetime | Banking_-_Interest-bearing_accounts | 4 | PATCH /v1/deposits/accounts/{accountId}/attachment;POST /v1/deposits/accounts/open;POST /v1/deposits/accounts/{accountId}/attach |
| `EIBACC0309` | 400 | Validation error | Banking_-_Interest-bearing_accounts | 2 | POST /v1/deposits/accounts/{accountId}/attach;POST /v1/deposits/programs/{programId}/attach |
| `EIBACC0310` | 400 | Validation error | Banking_-_Interest-bearing_accounts | 4 | PATCH /v1/deposits/accounts/{accountId}/attachment;PATCH /v1/deposits/programs/{programId}/attachment;POST /v1/deposits/accounts/{accountId}/attach |
| `EIBACC0311` | 400 | Validation error | Banking_-_Interest-bearing_accounts | 2 | POST /v1/deposits/accounts/{accountId}/attach;POST /v1/deposits/programs/{programId}/attach |
| `EIBACC0312` | 400 | Validation error | Banking_-_Interest-bearing_accounts | 2 | POST /v1/deposits/accounts/{accountId}/attach;POST /v1/deposits/programs/{programId}/attach |
| `EIBACC0314` | 409 | Product attachment was modified concurrently; retry with the latest state | Banking_-_Interest-bearing_accounts | 2 | PATCH /v1/deposits/accounts/{accountId}/attachment;PATCH /v1/deposits/programs/{programId}/attachment |
| `EIBACC0315` | 400 | deposit_configs.overrides must contain at least one field | Banking_-_Interest-bearing_accounts | 2 | PATCH /v1/deposits/accounts/{accountId}/attachment;PATCH /v1/deposits/programs/{programId}/attachment |
| `EIBACC0316` | 500 | Failed to update attachment overrides | Banking_-_Interest-bearing_accounts | 2 | PATCH /v1/deposits/accounts/{accountId}/attachment;PATCH /v1/deposits/programs/{programId}/attachment |
| `EIBACC0317` | 400 | deposit_configs.overrides.penalties is not supported at program-level; apply per-account instead | Banking_-_Interest-bearing_accounts | 2 | PATCH /v1/deposits/programs/{programId}/attachment;POST /v1/deposits/programs/{programId}/attach |
| `EIBACC0318` | 400 | deposit_configs.overrides.maturity_instructions is not supported at program-level; apply per-account instead | Banking_-_Interest-bearing_accounts | 2 | PATCH /v1/deposits/programs/{programId}/attachment;POST /v1/deposits/programs/{programId}/attach |
| `EIBACC0319` | 400 | Effective date exceeds maximum backdating limit | Banking_-_Interest-bearing_accounts | 1 | POST /v1/deposits/accounts/open |
| `EIBACC0320` | 400 | Invalid effective date format. Expected YYYY-MM-DD | Banking_-_Interest-bearing_accounts | 1 | POST /v1/deposits/accounts/open |
| `EIBACC0321` | 400 | Effective date cannot be in the future | Banking_-_Interest-bearing_accounts | 1 | POST /v1/deposits/accounts/open |
| `EIBACC0322` | 502 | Corporate API unavailable | Banking_-_Interest-bearing_accounts | 1 | POST /v1/deposits/accounts/open |
| `EIBACC0324` | 500 | Failed to unmarshal Corporate API response | Banking_-_Interest-bearing_accounts | 1 | POST /v1/deposits/accounts/open |
| `EIBACC0325` | 400 | Field 'account_creation' is required when 'account_id' is not provided | Banking_-_Interest-bearing_accounts | 1 | POST /v1/deposits/accounts/open |
| `EIBACC0328` | 500 | Corporate API request error | Banking_-_Interest-bearing_accounts | 1 | POST /v1/deposits/accounts/open |
| `EIBACC0329` | 504 | Corporate API timeout | Banking_-_Interest-bearing_accounts | 1 | POST /v1/deposits/accounts/open |
| `EIBACC0330` | 400 | Corporate API validation error | Banking_-_Interest-bearing_accounts | 1 | POST /v1/deposits/accounts/open |
| `EIBACC0331` | 400 | Provided account_id does not match the resolved external_account_id | Banking_-_Interest-bearing_accounts | 1 | POST /v1/deposits/accounts/open |
| `EIBACC0338` | 400 | withdrawal_amount cannot be greater than the account balance | Banking_-_Interest-bearing_accounts | 1 | POST /v1/deposits/accounts/{accountId}/penalty-simulation |
| `EIBACC0379` | 400 | interest_capitalization_mode PAYOUT requires a fully resolved payout_account | Banking_-_Interest-bearing_accounts | 3 | POST /v1/deposits/accounts/open;POST /v1/deposits/accounts/{accountId}/attach;POST /v1/deposits/programs/{programId}/attach |
| `EIBACC0380` | 400 | Invalid account_creation_datetime format. Expected RFC3339 | Banking_-_Interest-bearing_accounts | 1 | POST /v1/deposits/accounts/open |
| `EIBACC0393` | 409 | Penalty processing code has a balance‑config that conflicts with the required penalty configuration | Banking_-_Interest-bearing_accounts | 1 | POST /v1/deposits |
| `EIBACC0396` | 409 | Account already exists but could not be attached, status is not "NORMAL" | Banking_-_Interest-bearing_accounts | 1 | POST /v1/deposits/accounts/open |

## Lifecycle status

Codes in this unit that are mentioned in changelog posts (check the post: it may record that the code was added, changed or removed from some endpoints):

- `EIBACC0007`: `KU-CHG-5-december-2025`
- `EIBACC0008`: `KU-CHG-5-december-2025`
- `EIBACC0018`: `KU-CHG-4-september-2026`
- `EIBACC0065`: `KU-CHG-4-september-2026`
- `EIBACC0103`: `KU-CHG-4-september-2026`
- `EIBACC0107`: `KU-CHG-4-september-2026`
- `EIBACC0109`: `KU-CHG-4-september-2026`
- `EIBACC0110`: `KU-CHG-4-september-2026`
- `EIBACC0236`: `KU-CHG-4-september-2026`
- `EIBACC0284`: `KU-CHG-4-september-2026`
- `EIBACC0297`: `KU-CHG-4-september-2026`
- `EIBACC0298`: `KU-CHG-4-september-2026`
- `EIBACC0299`: `KU-CHG-4-september-2026`
- `EIBACC0303`: `KU-CHG-4-september-2026`
- `EIBACC0305`: `KU-CHG-2-october-2026`, `KU-CHG-4-september-2026`
- `EIBACC0306`: `KU-CHG-2-october-2026`, `KU-CHG-4-september-2026`
- `EIBACC0307`: `KU-CHG-2-october-2026`, `KU-CHG-4-september-2026`
- `EIBACC0308`: `KU-CHG-4-september-2026`
- `EIBACC0318`: `KU-CHG-4-september-2026`
- `EIBACC0319`: `KU-CHG-2-october-2026`, `KU-CHG-4-september-2026`
- `EIBACC0320`: `KU-CHG-2-october-2026`, `KU-CHG-4-september-2026`
- `EIBACC0321`: `KU-CHG-2-october-2026`, `KU-CHG-4-september-2026`
- `EIBACC0324`: `KU-CHG-4-september-2026`
- `EIBACC0328`: `KU-CHG-4-september-2026`
- `EIBACC0329`: `KU-CHG-4-september-2026`
- `EIBACC0330`: `KU-CHG-4-september-2026`
- `EIBACC0331`: `KU-CHG-4-september-2026`
- `EIBACC0379`: `KU-CHG-2-october-2026`

## Conflicts, caveats and evidence gaps

- Codes and messages come from response examples in the OpenAPI specifications; the conditions that trigger a code are documented only where the message or the operation description states them.
- The source table recognises only codes made of letters followed by digits; codes with mixed prefixes (for example `WP2P0000`) are not in the table but appear in the API-reference KUs.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-reference-data/error_code_index.csv` | rows with code prefix EIBACC | https://github.com/PismoDevEx/pismo-api-specs | `76213ae93e90a725…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-API-banking-interest-bearing-accounts--account-attachment` — API reference: Banking - Interest-bearing accounts — Account attachment
- `KU-API-banking-interest-bearing-accounts--deposit-account-open` — API reference: Banking - Interest-bearing accounts — Deposit account open
- `KU-API-banking-interest-bearing-accounts--penalty` — API reference: Banking - Interest-bearing accounts — Penalty
- `KU-API-banking-interest-bearing-accounts--product` — API reference: Banking - Interest-bearing accounts — Product
- `KU-API-banking-interest-bearing-accounts--program-attachment` — API reference: Banking - Interest-bearing accounts — Program attachment
- `KU-CHG-2-october-2026` — Changelog: 2 October 2026
- `KU-CHG-4-september-2026` — Changelog: 4 September 2026
- `KU-CHG-5-december-2025` — Changelog: 5 December 2025
