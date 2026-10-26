---
ku_id: KU-ERR-codes-wtrc
title: 'Error codes: WTRC'
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
- KU-API-core-platform-transactions--transaction-flows
- KU-API-core-platform-transactions--transaction-types
- KU-API-core-platform-transactions--transactions
- KU-CHG-3-april-2026
- KU-CHG-6-march-2026
error_codes:
- WTRC00001
- WTRC00002
- WTRC00003
- WTRC00005
- WTRC01001
- WTRC01003
- WTRC03001
- WTRC04001
- WTRC04002
- WTRC04003
- WTRC04004
- WTRC04005
- WTRC04006
- WTRC05001
- WTRC05003
- WTRC05004
- WTRC05005
- WTRC05007
- WTRC07001
- WTRC08001
---

# Error codes: WTRC

**KU ID:** `KU-ERR-codes-wtrc` · **Category:** Errors and troubleshooting · **Type:** error-code catalogue (from reference table)

## Purpose and scope

20 error code(s) with prefix(es) WTRC from `api-reference-data/error_code_index.csv`, with the HTTP status, message and the operations whose response examples contain the code. The `operations_sample` column is a sample, not a complete list: the complete set of codes per operation is in the API-reference KUs (section “Error codes shown in this operation's response examples”). Conditions under which a code is returned are documented only where the message or the operation description states them.

## Error codes

| Code | HTTP status | Message | Specification files | Operation count | Operations (sample) |
| --- | --- | --- | --- | --- | --- |
| `WTRC00001` | 400 | invalid time range: difference between eventDateStart and eventDateEnd cannot be greater than 90 days | Core_platform_-_Transactions | 4 | GET /v1/transaction-flow;GET /v1/transaction-types;GET /v2/transactions |
| `WTRC00002` | 400 | Invalid request headers | Core_platform_-_Transactions | 3 | GET /v2/transactions;GET /v2/transactions/total-items;GET /v2/transactions/{transactionId} |
| `WTRC00003` | 400 | Invalid request parameters | Core_platform_-_Transactions | 5 | GET /v2/transactions;GET /v2/transactions/total-items;GET /v2/transactions/{transactionId} |
| `WTRC00005` | 400 | Invalid request body | Core_platform_-_Transactions | 5 | PATCH /v1/programs/{programId}/transaction-types/{transactionTypeId};PATCH /v1/transaction-flow/processing-code/{processingCode}/transaction-type/{transactionTypeId};PATCH /v1/transaction-types/{transactionTypeId} |
| `WTRC01001` | 404 | Transaction not found | Core_platform_-_Transactions | 1 | GET /v2/transactions/{transactionId} |
| `WTRC01003` | 400 | Transaction ID not provided | Core_platform_-_Transactions | 1 | GET /v2/transactions/{transactionId} |
| `WTRC03001` | 404 | Program transaction type not found | Core_platform_-_Transactions | 1 | PATCH /v1/programs/{programId}/transaction-types/{transactionTypeId} |
| `WTRC04001` | 409 | Relationship between transaction type and processing code already exists | Core_platform_-_Transactions | 1 | POST /v1/transaction-flow |
| `WTRC04002` | 400 | The transaction flow mapping configuration between this processing code and transaction type doesn't exist | Core_platform_-_Transactions | 1 | PATCH /v1/transaction-flow/processing-code/{processingCode}/transaction-type/{transactionTypeId} |
| `WTRC04003` | 400 | Key should be PRINCIPAL, INSTALLMENT, CONTRACT, or OTHER | Core_platform_-_Transactions | 2 | PATCH /v1/transaction-flow/processing-code/{processingCode}/transaction-type/{transactionTypeId};POST /v1/transaction-flow |
| `WTRC04004` | 400 | custom_key is mandatory when key is OTHER | Core_platform_-_Transactions | 2 | PATCH /v1/transaction-flow/processing-code/{processingCode}/transaction-type/{transactionTypeId};POST /v1/transaction-flow |
| `WTRC04005` | 400 | custom_key should not be empty when key is OTHER | Core_platform_-_Transactions | 2 | PATCH /v1/transaction-flow/processing-code/{processingCode}/transaction-type/{transactionTypeId};POST /v1/transaction-flow |
| `WTRC04006` | 400 | custom_key should only be provided when key is OTHER | Core_platform_-_Transactions | 2 | PATCH /v1/transaction-flow/processing-code/{processingCode}/transaction-type/{transactionTypeId};POST /v1/transaction-flow |
| `WTRC05001` | 409 | Transaction type ID already exists | Core_platform_-_Transactions | 2 | PATCH /v1/transaction-types/{transactionTypeId};POST /v1/transaction-types |
| `WTRC05003` | 400 | Transaction type doesn't exist | Core_platform_-_Transactions | 2 | PATCH /v1/transaction-flow/processing-code/{processingCode}/transaction-type/{transactionTypeId};POST /v1/transaction-flow |
| `WTRC05004` | 400 | Transaction type ID not provided | Core_platform_-_Transactions | 1 | GET /v1/transaction-type/{transactionTypeId} |
| `WTRC05005` | 404 | Transaction type not found | Core_platform_-_Transactions | 1 | GET /v1/transaction-type/{transactionTypeId} |
| `WTRC05007` | 400 | Transaction type ID is not a number | Core_platform_-_Transactions | 1 | PATCH /v1/transaction-flow/processing-code/{processingCode}/transaction-type/{transactionTypeId} |
| `WTRC07001` | 400 | Processing code doesn't exist | Core_platform_-_Transactions | 1 | POST /v1/transaction-flow |
| `WTRC08001` | 409 | The provided transaction_type_id is reserved by the platform and cannot be used | Core_platform_-_Transactions | 2 | POST /v1/transaction-flow;POST /v1/transaction-types |

## Lifecycle status

Codes in this unit that are mentioned in changelog posts (check the post: it may record that the code was added, changed or removed from some endpoints):

- `WTRC00001`: `KU-CHG-6-march-2026`
- `WTRC05003`: `KU-CHG-6-march-2026`
- `WTRC08001`: `KU-CHG-3-april-2026`

## Conflicts, caveats and evidence gaps

- Codes and messages come from response examples in the OpenAPI specifications; the conditions that trigger a code are documented only where the message or the operation description states them.
- The source table recognises only codes made of letters followed by digits; codes with mixed prefixes (for example `WP2P0000`) are not in the table but appear in the API-reference KUs.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-reference-data/error_code_index.csv` | rows with code prefix WTRC | https://github.com/PismoDevEx/pismo-api-specs | `76213ae93e90a725…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-API-core-platform-transactions--transaction-flows` — API reference: Core platform - Transactions — Transaction flows
- `KU-API-core-platform-transactions--transaction-types` — API reference: Core platform - Transactions — Transaction types
- `KU-API-core-platform-transactions--transactions` — API reference: Core platform - Transactions — Transactions
- `KU-CHG-3-april-2026` — Changelog: 3 April 2026
- `KU-CHG-6-march-2026` — Changelog: 6 March 2026
