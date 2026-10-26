---
ku_id: KU-ERR-codes-ehld
title: 'Error codes: EHLD'
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
- EHLD0001
- EHLD0016
- EHLD0026
- EHLD0027
- EHLD0028
- EHLD0030
- EHLD0031
- EHLD0032
- EHLD0034
- EHLD0039
- EHLD0041
- EHLD0046
- EHLD0047
- EHLD0048
- EHLD0049
- EHLD0050
- EHLD0052
---

# Error codes: EHLD

**KU ID:** `KU-ERR-codes-ehld` · **Category:** Errors and troubleshooting · **Type:** error-code catalogue (from reference table)

## Purpose and scope

17 error code(s) with prefix(es) EHLD from `api-reference-data/error_code_index.csv`, with the HTTP status, message and the operations whose response examples contain the code. The `operations_sample` column is a sample, not a complete list: the complete set of codes per operation is in the API-reference KUs (section “Error codes shown in this operation's response examples”). Conditions under which a code is returned are documented only where the message or the operation description states them.

## Error codes

| Code | HTTP status | Message | Specification files | Operation count | Operations (sample) |
| --- | --- | --- | --- | --- | --- |
| `EHLD0001` | not stated | Something went wrong - please try again | Platform_setup_-_Holidays | 0 |  |
| `EHLD0016` | not stated | Missing x-tenant header | Platform_setup_-_Holidays | 0 |  |
| `EHLD0026` | not stated | Administrative division not found | Platform_setup_-_Holidays | 0 |  |
| `EHLD0027` | not stated | Holiday calendar already exists | Platform_setup_-_Holidays | 0 |  |
| `EHLD0028` | not stated | Holiday date with the wrong format | Platform_setup_-_Holidays | 0 |  |
| `EHLD0030` | not stated | Working date with the wrong format | Platform_setup_-_Holidays | 0 |  |
| `EHLD0031` | not stated | Working date less than the current date | Platform_setup_-_Holidays | 0 |  |
| `EHLD0032` | not stated | Working date before holiday date | Platform_setup_-_Holidays | 0 |  |
| `EHLD0034` | not stated | Holiday not found | Platform_setup_-_Holidays | 0 |  |
| `EHLD0039` | not stated | Invalid 'perPage' query param with value '10A'. PerPage must be > 0. | Platform_setup_-_Holidays | 0 |  |
| `EHLD0041` | not stated | Invalid 'order' query param with value 'ascaa'. Order must be asc or desc. | Platform_setup_-_Holidays | 0 |  |
| `EHLD0046` | not stated | End date before Begin date | Platform_setup_-_Holidays | 0 |  |
| `EHLD0047` | not stated | Begin date with the wrong format | Platform_setup_-_Holidays | 0 |  |
| `EHLD0048` | not stated | End date with the wrong format | Platform_setup_-_Holidays | 0 |  |
| `EHLD0049` | not stated | Invalid metadata | Platform_setup_-_Holidays | 0 |  |
| `EHLD0050` | not stated | Missing required fields | Platform_setup_-_Holidays | 0 |  |
| `EHLD0052` | not stated | Holiday calendar not found | Platform_setup_-_Holidays | 0 |  |

## Lifecycle status

- No code in this unit is mentioned in a changelog post.

## Conflicts, caveats and evidence gaps

- Codes and messages come from response examples in the OpenAPI specifications; the conditions that trigger a code are documented only where the message or the operation description states them.
- The source table recognises only codes made of letters followed by digits; codes with mixed prefixes (for example `WP2P0000`) are not in the table but appear in the API-reference KUs.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-reference-data/error_code_index.csv` | rows with code prefix EHLD | https://github.com/PismoDevEx/pismo-api-specs | `76213ae93e90a725…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- None.
