---
ku_id: KU-ERR-codes-erul
title: 'Error codes: ERUL'
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
- KU-API-core-platform-payment-methods--installments-payments
- KU-API-core-platform-payment-methods--payments
error_codes:
- ERUL0001
- ERUL0002
- ERUL0003
- ERUL0004
- ERUL0005
- ERUL0101
- ERUL0102
- ERUL0204
- ERUL0404
- ERUL0701
- ERUL0702
- ERUL0703
- ERUL0704
- ERUL0706
- ERUL0707
- ERUL0801
- ERUL0802
- ERUL0803
- ERUL0804
- ERUL0805
- ERUL0806
- ERUL0901
- ERUL0902
- ERUL1001
- ERUL1002
- ERUL1003
- ERUL1004
- ERUL1005
- ERUL1006
- ERUL1007
- ERUL1101
- ERUL1102
- ERUL1105
- ERUL1106
- ERUL1201
- ERUL1202
- ERUL1203
- ERUL1204
- ERUL1205
- ERUL1301
- ERUL1302
- ERUL1401
- ERUL1402
- ERUL1403
- ERUL1406
- ERUL1501
---

# Error codes: ERUL

**KU ID:** `KU-ERR-codes-erul` · **Category:** Errors and troubleshooting · **Type:** error-code catalogue (from reference table)

## Purpose and scope

46 error code(s) with prefix(es) ERUL from `api-reference-data/error_code_index.csv`, with the HTTP status, message and the operations whose response examples contain the code. The `operations_sample` column is a sample, not a complete list: the complete set of codes per operation is in the API-reference KUs (section “Error codes shown in this operation's response examples”). Conditions under which a code is returned are documented only where the message or the operation description states them.

## Error codes

| Code | HTTP status | Message | Specification files | Operation count | Operations (sample) |
| --- | --- | --- | --- | --- | --- |
| `ERUL0001` | not stated | internal server error | Core_platform_-_Flex_controls | 0 |  |
| `ERUL0002` | not stated | operation not allowed | Core_platform_-_Flex_controls | 0 |  |
| `ERUL0003` | not stated | spending limit not found | Core_platform_-_Flex_controls | 0 |  |
| `ERUL0004` | not stated | spending limit does not exist in override controls | Core_platform_-_Flex_controls | 0 |  |
| `ERUL0005` | not stated | Error getting info from Account | Core_platform_-_Flex_controls | 0 |  |
| `ERUL0101` | not stated | error validating request header | Core_platform_-_Flex_controls | 0 |  |
| `ERUL0102` | not stated | error validating request parameter | Core_platform_-_Flex_controls | 0 |  |
| `ERUL0204` | not stated | Flex Controls not found for the specified program | Core_platform_-_Flex_controls | 0 |  |
| `ERUL0404` | 400 | Restriction rule [max_value_authorized_device_unique_transaction] does not pass. | Core_platform_-_Payment_methods | 2 | POST /payments/v1/payments;POST /payments/v1/payments/installments |
| `ERUL0701` | not stated | error parsing payload | Core_platform_-_Flex_controls | 0 |  |
| `ERUL0702` | not stated | error validating request path | Core_platform_-_Flex_controls | 0 |  |
| `ERUL0703` | not stated | error validating request header | Core_platform_-_Flex_controls | 0 |  |
| `ERUL0704` | not stated | error building new spending limit from request payload | Core_platform_-_Flex_controls | 0 |  |
| `ERUL0706` | not stated | spending limit already exists | Core_platform_-_Flex_controls | 0 |  |
| `ERUL0707` | not stated | Attribute group already exists | Core_platform_-_Flex_controls | 0 |  |
| `ERUL0801` | not stated | error validating request header | Core_platform_-_Flex_controls | 0 |  |
| `ERUL0802` | not stated | error validating request path | Core_platform_-_Flex_controls | 0 |  |
| `ERUL0803` | not stated | spending limit not found for account | Core_platform_-_Flex_controls | 0 |  |
| `ERUL0804` | not stated | Customer's spending limits not found for account | Core_platform_-_Flex_controls | 0 |  |
| `ERUL0805` | not stated | attribute group not found | Core_platform_-_Flex_controls | 0 |  |
| `ERUL0806` | not stated | The 'value' field is the only one that can be updated. | Core_platform_-_Flex_controls | 0 |  |
| `ERUL0901` | not stated | error validating request header | Core_platform_-_Flex_controls | 0 |  |
| `ERUL0902` | not stated | error validating request path | Core_platform_-_Flex_controls | 0 |  |
| `ERUL1001` | not stated | error parsing payload | Core_platform_-_Flex_controls | 0 |  |
| `ERUL1002` | not stated | error validating request header | Core_platform_-_Flex_controls | 0 |  |
| `ERUL1003` | not stated | error validating request path | Core_platform_-_Flex_controls | 0 |  |
| `ERUL1004` | not stated | no information to patch | Core_platform_-_Flex_controls | 0 |  |
| `ERUL1005` | not stated | error validating spending limit from request payload | Core_platform_-_Flex_controls | 0 |  |
| `ERUL1006` | not stated | error validating request payload | Core_platform_-_Flex_controls | 0 |  |
| `ERUL1007` | not stated | spending limit created by template | Core_platform_-_Flex_controls | 0 |  |
| `ERUL1101` | not stated | invalid request | Core_platform_-_Flex_controls | 0 |  |
| `ERUL1102` | not stated | error building new spending limit from request payload | Core_platform_-_Flex_controls | 0 |  |
| `ERUL1105` | not stated | Error on repository | Core_platform_-_Flex_controls | 0 |  |
| `ERUL1106` | not stated | Customer spending limit already exists. | Core_platform_-_Flex_controls | 0 |  |
| `ERUL1201` | not stated | Invalid request | Core_platform_-_Flex_controls | 0 |  |
| `ERUL1202` | not stated | Error validating request payload to GetCustomerSpendingLimitRules | Core_platform_-_Flex_controls | 0 |  |
| `ERUL1203` | not stated | Error on repository | Core_platform_-_Flex_controls | 0 |  |
| `ERUL1204` | not stated | Rules for customerID not found | Core_platform_-_Flex_controls | 0 |  |
| `ERUL1205` | not stated | Customer spending limit rules not found. | Core_platform_-_Flex_controls | 0 |  |
| `ERUL1301` | not stated | Invalid request | Core_platform_-_Flex_controls | 0 |  |
| `ERUL1302` | not stated | Error validating request payload to GetCustomerSpendingLimitRule | Core_platform_-_Flex_controls | 0 |  |
| `ERUL1401` | not stated | Invalid request | Core_platform_-_Flex_controls | 0 |  |
| `ERUL1402` | not stated | Error parsing payload. | Core_platform_-_Flex_controls | 0 |  |
| `ERUL1403` | not stated | Error validating request payload to PatchCustomerSpendingLimitRule | Core_platform_-_Flex_controls | 0 |  |
| `ERUL1406` | not stated | Error building new spending limit from request payload | Core_platform_-_Flex_controls | 0 |  |
| `ERUL1501` | not stated | error validating request parameters | Core_platform_-_Flex_controls | 0 |  |

## Lifecycle status

- No code in this unit is mentioned in a changelog post.

## Conflicts, caveats and evidence gaps

- Codes and messages come from response examples in the OpenAPI specifications; the conditions that trigger a code are documented only where the message or the operation description states them.
- The source table recognises only codes made of letters followed by digits; codes with mixed prefixes (for example `WP2P0000`) are not in the table but appear in the API-reference KUs.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-reference-data/error_code_index.csv` | rows with code prefix ERUL | https://github.com/PismoDevEx/pismo-api-specs | `76213ae93e90a725…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-API-core-platform-payment-methods--installments-payments` — API reference: Core platform - Payment methods — Installments payments
- `KU-API-core-platform-payment-methods--payments` — API reference: Core platform - Payment methods — Payments
