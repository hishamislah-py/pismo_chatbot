---
ku_id: KU-ERR-codes-wmlp
title: 'Error codes: WMLP'
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
- KU-API-banking-transaction-banking--payments-part-01
- KU-API-banking-transaction-banking--payments-part-02
- KU-API-banking-transaction-banking--payments-part-03
- KU-CHG-3-january-2025
- KU-CHG-7-february-2025
- KU-CHG-7-november-2025
- KU-CHG-9-january-2026
error_codes:
- WMLP0001
- WMLP0002
- WMLP0003
- WMLP0004
- WMLP0005
- WMLP0006
- WMLP0007
- WMLP0008
- WMLP0009
- WMLP1002
- WMLP1003
- WMLP1004
- WMLP1005
- WMLP1006
- WMLP1007
- WMLP1008
- WMLP1009
- WMLP1010
- WMLP1011
- WMLP1013
- WMLP1014
- WMLP1015
- WMLP1016
- WMLP1017
- WMLP1019
- WMLP1022
- WMLP1023
- WMLP1024
- WMLP1026
- WMLP1027
- WMLP1028
- WMLP1030
- WMLP1034
- WMLP1035
- WMLP1036
- WMLP1037
- WMLP1038
- WMLP1039
- WMLP1040
- WMLP1041
- WMLP1042
- WMLP1043
- WMLP1044
- WMLP1046
- WMLP1048
- WMLP1049
---

# Error codes: WMLP

**KU ID:** `KU-ERR-codes-wmlp` · **Category:** Errors and troubleshooting · **Type:** error-code catalogue (from reference table)

## Purpose and scope

46 error code(s) with prefix(es) WMLP from `api-reference-data/error_code_index.csv`, with the HTTP status, message and the operations whose response examples contain the code. The `operations_sample` column is a sample, not a complete list: the complete set of codes per operation is in the API-reference KUs (section “Error codes shown in this operation's response examples”). Conditions under which a code is returned are documented only where the message or the operation description states them.

## Error codes

| Code | HTTP status | Message | Specification files | Operation count | Operations (sample) |
| --- | --- | --- | --- | --- | --- |
| `WMLP0001` | 400 | Invalid JSON payload received: Error unmarshalling request | Banking_-_Transaction_banking | 2 | POST /corporate/v2/payments/multileg;POST /corporate/v3/payments/multileg |
| `WMLP0002` | 400 | business_date 2025-05-32 should be formatted as yyyy-mm-dd and be a valid date | Banking_-_Transaction_banking | 2 | POST /corporate/v2/payments/multileg;POST /corporate/v3/payments/multileg |
| `WMLP0003` | 400 | Multi-leg payments must have up to 20 legs | Banking_-_Transaction_banking | 2 | POST /corporate/v2/payments/multileg;POST /corporate/v3/payments/multileg |
| `WMLP0004` | 400 | Multi-leg payments must have at least 2 legs | Banking_-_Transaction_banking | 2 | POST /corporate/v2/payments/multileg;POST /corporate/v3/payments/multileg |
| `WMLP0005` | 400 | Validation error: One or more legs did not pass validation. | Banking_-_Transaction_banking | 2 | POST /corporate/v2/payments/multileg;POST /corporate/v3/payments/multileg |
| `WMLP0006` | 400 | Multi-leg payments don't allow single transfers | Banking_-_Transaction_banking | 1 | POST /corporate/v2/payments/multileg |
| `WMLP0007` | 400;404 | multi leg not found | Banking_-_Transaction_banking | 2 | GET /corporate/v2/payments/multileg/{trackingId};GET /corporate/v3/payments/multileg/{multilegId} |
| `WMLP0008` | 400 | Cannot use primary and payment legs metadata fields together | Banking_-_Transaction_banking | 1 | POST /corporate/v3/payments/multileg |
| `WMLP0009` | 409 | multileg_id is already in use | Banking_-_Transaction_banking | 1 | POST /corporate/v3/payments/multileg |
| `WMLP1002` | 400 | Insufficient balance | Banking_-_Transaction_banking | 2 | POST /corporate/v2/payments/multileg;POST /corporate/v3/payments/multileg |
| `WMLP1003` | 400 | Invalid processing code | Banking_-_Transaction_banking | 2 | POST /corporate/v2/payments/multileg;POST /corporate/v3/payments/multileg |
| `WMLP1004` | 400 | Cannot perform conversion between account currency and provided currency | Banking_-_Transaction_banking | 2 | POST /corporate/v2/payments/multileg;POST /corporate/v3/payments/multileg |
| `WMLP1005` | 400 | Invalid account status | Banking_-_Transaction_banking | 2 | POST /corporate/v2/payments/multileg;POST /corporate/v3/payments/multileg |
| `WMLP1006` | 400 | Earmark is not active | Banking_-_Transaction_banking | 2 | POST /corporate/v2/payments/multileg;POST /corporate/v3/payments/multileg |
| `WMLP1007` | 400 | Cannot post transaction on weekends | Banking_-_Transaction_banking | 2 | POST /corporate/v2/payments/multileg;POST /corporate/v3/payments/multileg |
| `WMLP1008` | 400 | Cannot post transaction on holidays | Banking_-_Transaction_banking | 2 | POST /corporate/v2/payments/multileg;POST /corporate/v3/payments/multileg |
| `WMLP1009` | 400 | Account not found | Banking_-_Transaction_banking | 2 | POST /corporate/v2/payments/multileg;POST /corporate/v3/payments/multileg |
| `WMLP1010` | 400 | Earmark not found | Banking_-_Transaction_banking | 2 | POST /corporate/v2/payments/multileg;POST /corporate/v3/payments/multileg |
| `WMLP1011` | 400 | Processing code not found | Banking_-_Transaction_banking | 2 | POST /corporate/v2/payments/multileg;POST /corporate/v3/payments/multileg |
| `WMLP1013` | 400 | Tracking ID already exists | Banking_-_Transaction_banking | 2 | POST /corporate/v2/payments/multileg;POST /corporate/v3/payments/multileg |
| `WMLP1014` | 400 | Debit not permitted on a closed account | Banking_-_Transaction_banking | 2 | POST /corporate/v2/payments/multileg;POST /corporate/v3/payments/multileg |
| `WMLP1015` | 400 | Credit not permitted on a closed account | Banking_-_Transaction_banking | 2 | POST /corporate/v2/payments/multileg;POST /corporate/v3/payments/multileg |
| `WMLP1016` | 400 | Force debit not allowed by reason - Credit Only - No Force Debit Allowed | Banking_-_Transaction_banking | 2 | POST /corporate/v2/payments/multileg;POST /corporate/v3/payments/multileg |
| `WMLP1017` | 400 | Force credit not allowed by reason - {Reason} | Banking_-_Transaction_banking | 2 | POST /corporate/v2/payments/multileg;POST /corporate/v3/payments/multileg |
| `WMLP1019` | 400 | The payment date cannot be earlier than the account creation date | Banking_-_Transaction_banking | 2 | POST /corporate/v2/payments/multileg;POST /corporate/v3/payments/multileg |
| `WMLP1022` | 400 | There is insufficient balance in the earmark to complete this operation | Banking_-_Transaction_banking | 2 | POST /corporate/v2/payments/multileg;POST /corporate/v3/payments/multileg |
| `WMLP1023` | 400 | The maximum retroactive payment datetime allowed is [n] days | Banking_-_Transaction_banking | 2 | POST /corporate/v2/payments/multileg;POST /corporate/v3/payments/multileg |
| `WMLP1024` | 400 | Invalid business date for the current business day cycle | Banking_-_Transaction_banking | 2 | POST /corporate/v2/payments/multileg;POST /corporate/v3/payments/multileg |
| `WMLP1026` | 400 | Payment request with conflicting force parameters | Banking_-_Transaction_banking | 2 | POST /corporate/v2/payments/multileg;POST /corporate/v3/payments/multileg |
| `WMLP1027` | 400 | Invalid validation rule UNKNOWN | Banking_-_Transaction_banking | 2 | POST /corporate/v2/payments/multileg;POST /corporate/v3/payments/multileg |
| `WMLP1028` | 400 | Invalid params for validation rule ACCOUNT_STATUS | Banking_-_Transaction_banking | 2 | POST /corporate/v2/payments/multileg;POST /corporate/v3/payments/multileg |
| `WMLP1030` | 400 | Future dated payment datetime must be before date limit | Banking_-_Transaction_banking | 2 | POST /corporate/v2/payments/multileg;POST /corporate/v3/payments/multileg |
| `WMLP1034` | 400 | Back business dating is disabled | Banking_-_Transaction_banking | 2 | POST /corporate/v2/payments/multileg;POST /corporate/v3/payments/multileg |
| `WMLP1035` | 400 | Operations blocked for account | Banking_-_Transaction_banking | 2 | POST /corporate/v2/payments/multileg;POST /corporate/v3/payments/multileg |
| `WMLP1036` | 400 | Payment business date cannot be earlier than the earmark creation date | Banking_-_Transaction_banking | 2 | POST /corporate/v2/payments/multileg;POST /corporate/v3/payments/multileg |
| `WMLP1037` | 400 | Debit not allowed by reason - <reason> | Banking_-_Transaction_banking | 2 | POST /corporate/v2/payments/multileg;POST /corporate/v3/payments/multileg |
| `WMLP1038` | 400 | Credit not allowed by reason - <reason> | Banking_-_Transaction_banking | 2 | POST /corporate/v2/payments/multileg;POST /corporate/v3/payments/multileg |
| `WMLP1039` | 400 | Account has not finished onboarding | Banking_-_Transaction_banking | 2 | POST /corporate/v2/payments/multileg;POST /corporate/v3/payments/multileg |
| `WMLP1040` | 400 | Tracking ID already in use by another payment leg in the request | Banking_-_Transaction_banking | 1 | POST /corporate/v3/payments/multileg |
| `WMLP1041` | 400 | Cannot post back value-dated transaction for this division | Banking_-_Transaction_banking | 2 | POST /corporate/v2/payments/multileg;POST /corporate/v3/payments/multileg |
| `WMLP1042` | 400 | Cannot post future value-dated transaction for this division | Banking_-_Transaction_banking | 2 | POST /corporate/v2/payments/multileg;POST /corporate/v3/payments/multileg |
| `WMLP1043` | 400 | Invalid account currency code | Banking_-_Transaction_banking | 1 | POST /corporate/v3/payments/multileg |
| `WMLP1044` | 400 | Program not found | Banking_-_Transaction_banking | 1 | POST /corporate/v3/payments/multileg |
| `WMLP1046` | 400 | Channel not found | Banking_-_Transaction_banking | 1 | POST /corporate/v3/payments/multileg |
| `WMLP1048` | 400 | The payment date cannot be earlier than the account migration date | Banking_-_Transaction_banking | 2 | POST /corporate/v2/payments/multileg;POST /corporate/v3/payments/multileg |
| `WMLP1049` | 400 | Rates enforcement is not supported for operations with a fee deduction model (deductFromTransactionValue) | Banking_-_Transaction_banking | 1 | POST /corporate/v3/payments/multileg |

## Lifecycle status

Codes in this unit that are mentioned in changelog posts (check the post: it may record that the code was added, changed or removed from some endpoints):

- `WMLP0005`: `KU-CHG-3-january-2025`, `KU-CHG-7-february-2025`, `KU-CHG-7-november-2025`, `KU-CHG-9-january-2026`
- `WMLP1037`: `KU-CHG-7-february-2025`
- `WMLP1038`: `KU-CHG-7-february-2025`
- `WMLP1043`: `KU-CHG-9-january-2026`

## Conflicts, caveats and evidence gaps

- Codes and messages come from response examples in the OpenAPI specifications; the conditions that trigger a code are documented only where the message or the operation description states them.
- The source table recognises only codes made of letters followed by digits; codes with mixed prefixes (for example `WP2P0000`) are not in the table but appear in the API-reference KUs.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-reference-data/error_code_index.csv` | rows with code prefix WMLP | https://github.com/PismoDevEx/pismo-api-specs | `76213ae93e90a725…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-API-banking-transaction-banking--payments-part-01` — API reference: Banking - Transaction banking — Payments (part 1 of 3)
- `KU-API-banking-transaction-banking--payments-part-02` — API reference: Banking - Transaction banking — Payments (part 2 of 3)
- `KU-API-banking-transaction-banking--payments-part-03` — API reference: Banking - Transaction banking — Payments (part 3 of 3)
- `KU-CHG-3-january-2025` — Changelog: 3 January 2025
- `KU-CHG-7-february-2025` — Changelog: 7 February 2025
- `KU-CHG-7-november-2025` — Changelog: 7 November 2025
- `KU-CHG-9-january-2026` — Changelog: 9 January 2026
