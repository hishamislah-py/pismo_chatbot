---
ku_id: KU-ERR-codes-eoa
title: 'Error codes: EOA'
category: errors_and_troubleshooting
ku_type: error_catalogue
lifecycle: current
sources:
- path: api-reference-data/error_code_index.csv
  sha256: 76213ae93e90a725287cb34455be25ec9526ab12b34f02d7707b11a206bbcb35
  url: https://github.com/PismoDevEx/pismo-api-specs
  role: reference_table
  updated_at: '2026-10-13T20:51:51+00:00'
related_kus: []
error_codes:
- EOA0001
- EOA0008
- EOA0009
- EOA0010
- EOA0011
- EOA0015
- EOA0016
- EOA0017
- EOA0018
- EOA0020
- EOA0021
- EOA0022
- EOA0029
- EOA0030
- EOA0031
- EOA0033
- EOA0034
- EOA0035
- EOA0036
- EOA0037
- EOA0038
- EOA0039
- EOA0040
- EOA0054
- EOA0055
- EOA0058
- EOA0059
- EOA0063
- EOA0064
- EOA0072
- EOA0073
- EOA0080
- EOA0082
- EOA0085
- EOA0086
- EOA0090
- EOA0091
- EOA0092
- EOA0100
---

# Error codes: EOA

**KU ID:** `KU-ERR-codes-eoa` · **Category:** Errors and troubleshooting · **Type:** error-code catalogue (from reference table)

## Purpose and scope

39 error code(s) with prefix(es) EOA from `api-reference-data/error_code_index.csv`, with the HTTP status, message and the operations whose response examples contain the code. The `operations_sample` column is a sample, not a complete list: the complete set of codes per operation is in the API-reference KUs (section “Error codes shown in this operation's response examples”). Conditions under which a code is returned are documented only where the message or the operation description states them.

## Error codes

| Code | HTTP status | Message | Specification files | Operation count | Operations (sample) |
| --- | --- | --- | --- | --- | --- |
| `EOA0001` | not stated | Something went wrong, please try again later | Platform_setup_-_Organizations | 0 |  |
| `EOA0008` | not stated | Error parsing utils body with message: | Platform_setup_-_Programs | 0 |  |
| `EOA0009` | not stated | Connection failed with message: | Platform_setup_-_Programs | 0 |  |
| `EOA0010` | not stated | Connection failed with message: | Platform_setup_-_Programs | 0 |  |
| `EOA0011` | not stated | Error parsing utils body with message: | Platform_setup_-_Programs | 0 |  |
| `EOA0015` | not stated | Something went wrong, please try again later | Platform_setup_-_Programs | 0 |  |
| `EOA0016` | not stated | Something went wrong, please try again later | Platform_setup_-_Programs | 0 |  |
| `EOA0017` | not stated | Missing x-tenant header | Platform_setup_-_Programs | 0 |  |
| `EOA0018` | not stated | Error to Binder | Platform_setup_-_Programs | 0 |  |
| `EOA0020` | not stated | Program x not found | Platform_setup_-_Programs | 0 |  |
| `EOA0021` | not stated | Invalid channel name: xxx | Platform_setup_-_Programs | 0 |  |
| `EOA0022` | not stated | Failed to create program channel | Platform_setup_-_Programs | 0 |  |
| `EOA0029` | not stated | Invalid timezone: xxx | Platform_setup_-_Programs | 0 |  |
| `EOA0030` | not stated | Missing x-tenant header | Platform_setup_-_Organizations;Platform_setup_-_Programs | 0 |  |
| `EOA0031` | not stated | Program type not found | Platform_setup_-_Programs | 0 |  |
| `EOA0033` | not stated | Invalid currency_numeric_code: xxx | Platform_setup_-_Programs | 0 |  |
| `EOA0034` | not stated | Failed to create program due dates | Platform_setup_-_Programs | 0 |  |
| `EOA0035` | not stated | X-Tenant header and request are different | Platform_setup_-_Organizations;Platform_setup_-_Programs | 0 |  |
| `EOA0036` | not stated | Failed to find a transaction category by description | Platform_setup_-_Programs | 0 |  |
| `EOA0037` | not stated | Bin must be 6 or 8 digits | Platform_setup_-_Programs | 0 |  |
| `EOA0038` | not stated | When a BIN is 6, the range can be up to 9 digits | Platform_setup_-_Programs | 0 |  |
| `EOA0039` | not stated | When a BIN is 8, the range can be up to 7 digits | Platform_setup_-_Programs | 0 |  |
| `EOA0040` | not stated | bin.start_range is not a valid number | Platform_setup_-_Programs | 0 |  |
| `EOA0054` | not stated | Card information is required (Bin, Brand and DueDate) | Platform_setup_-_Programs | 0 |  |
| `EOA0055` | not stated | Should not contain card information (Bin, Brand and DueDate) | Platform_setup_-_Programs | 0 |  |
| `EOA0058` | not stated | Failed to create corporate configuration | Platform_setup_-_Programs | 0 |  |
| `EOA0059` | not stated | It is not possible to update the Brand value, the value is already filled | Platform_setup_-_Programs | 0 |  |
| `EOA0063` | not stated | Invalid country_code: xxx | Platform_setup_-_Programs | 0 |  |
| `EOA0064` | not stated | Brand not found | Platform_setup_-_Programs | 0 |  |
| `EOA0072` | not stated | Program export xxx not found | Platform_setup_-_Programs | 0 |  |
| `EOA0073` | not stated | Card information is required (Bin and Brand) | Platform_setup_-_Programs | 0 |  |
| `EOA0080` | not stated | Invalid request | Platform_setup_-_Programs | 0 |  |
| `EOA0082` | not stated | Due dates need at least one active day | Platform_setup_-_Programs | 0 |  |
| `EOA0085` | not stated | Program xxx isn't operational | Platform_setup_-_Programs | 0 |  |
| `EOA0086` | not stated | fieldName' field is required | Platform_setup_-_Programs | 0 |  |
| `EOA0090` | not stated | Steps for program export xxx not found | Platform_setup_-_Programs | 0 |  |
| `EOA0091` | not stated | Program import xxx not found | Platform_setup_-_Programs | 0 |  |
| `EOA0092` | not stated | Steps for program import xxx not found | Platform_setup_-_Programs | 0 |  |
| `EOA0100` | not stated | Org TN-00000000000001 was not found | Platform_setup_-_Organizations | 0 |  |

## Lifecycle status

- No code in this unit is mentioned in a changelog post.

## Conflicts, caveats and evidence gaps

- Codes and messages come from response examples in the OpenAPI specifications; the conditions that trigger a code are documented only where the message or the operation description states them.
- The source table recognises only codes made of letters followed by digits; codes with mixed prefixes (for example `WP2P0000`) are not in the table but appear in the API-reference KUs.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-reference-data/error_code_index.csv` | rows with code prefix EOA | https://github.com/PismoDevEx/pismo-api-specs | `76213ae93e90a725…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- None.
