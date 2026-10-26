---
ku_id: KU-PAY-file-based-check-processing-and-bulk-settlement
title: File-based check processing and bulk settlement
category: transfers_and_payments
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/core-banking/file-based-check-processing-and-bulk-settlement.md
  sha256: 3d231789f22c062b55c87e254e64b8d37b7c1f5a871bd139fbb7b69f922ce486
  url: https://developers.pismo.io/pismo-docs/docs/file-based-check-processing-and-bulk-settlement
  role: primary_guide
  updated_at: '2026-03-18T15:18:05.000Z'
operations:
- corporate-post-v1-checks
- post-bulk-settlement
- post-corporate-v1-checks-release
related_kus:
- KU-API-banking-transaction-banking--bulk-settlement
- KU-API-banking-transaction-banking--check-posting
- KU-EVT-catalogue-other-domains
grouping_rationale: single source page
---

# File-based check processing and bulk settlement

**KU ID:** `KU-PAY-file-based-check-processing-and-bulk-settlement` · **Category:** Transfers and payments · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/core-banking/file-based-check-processing-and-bulk-settlement.md`:

> The Pismo platform includes an extensible, AWS‑based bulk processing framework that ingests and executes large‑scale, file‑based operational workflows using a plugin‑driven architecture. This infrastructure supports high‑volume batch operations such as bulk check posting and bulk check releases, and also powers the bulk‑settlements API, which allows multiple settlement operations to be executed simultaneously by specifying a division code and settlement date.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/core-banking/file-based-check-processing-and-bulk-settlement.md`: File-based check processing and bulk settlement; Check posting; File format; Input format; Sample check posting bulk request; Check posting field definitions; Sample check release bulk request; Header; Rows; Check release field definitions; Output format; Output header example; Header status fields; Row examples; Bulk settlement API; Request example; Field definitions

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 3 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/core-banking/file-based-check-processing-and-bulk-settlement.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/file-based-check-processing-and-bulk-settlement · updatedAt: 2026-03-18T15:18:05.000Z

<!-- source:begin path=docs/core-banking/file-based-check-processing-and-bulk-settlement.md part=0-end -->

# File-based check processing and bulk settlement

The Pismo platform includes an extensible, AWS‑based bulk processing framework that ingests and executes large‑scale, file‑based operational workflows using a plugin‑driven architecture. This infrastructure supports high‑volume batch operations such as bulk check posting and bulk check releases, and also powers the bulk‑settlements API, which allows multiple settlement operations to be executed simultaneously by specifying a division code and settlement date.

# Check posting

The enhanced bulk processing platform supports these functions.

* Uploading files containing check posting and fund release instructions through a bulk upload endpoint.
* Running the same operations available in these endpoints.
  * [Create check posting](https://developers.pismo.io/pismo-docs/reference/corporate-post-v1-checks)
  * [Release check](https://developers.pismo.io/pismo-docs/reference/post-corporate-v1-checks-release)
* Processing fund releases in bulk using the [Request bulk settlement](https://developers.pismo.io/pismo-docs/reference/post-bulk-settlement) endpoint, which settles all pending operations for a given division and settlement date.

## File format

Bulk operations are processed from a UTF‑8 encoded file consisting of:

* a header line
* n-lines of NDJSON entries, each representing a single operation matching the schema for the chosen operation type

### Input format

#### Header example

```json
{
  "bulk_id": "UniqueID",
  "org_id": "tn-0000-0001",
  "header_version": "1.0.0",
  "operation_type": "CHECK_POST",
  "n_entries": 10000
}
```

#### Header field definitions

| Field            | Type   | Required | Description                                                                                              |
| ---------------- | ------ | -------- | -------------------------------------------------------------------------------------------------------- |
| `bulk_id`        | string | yes      | Unique ID for the batch. Alphanumeric + hyphens only, maximum 50 characters. Must be unique per `org_id` |
| `org_id`         | string | yes      | Organization ID                                                                                          |
| `header_version` | string | yes      | Must be `1.0.0`                                                                                          |
| `operation_type` | string | yes      | `CHECK_POST`, `CHECK_RELEASE`. Identifies the type of check operation you perform                        |
| `n_entries`      | number | yes      | Number of NDJSON entries that follow                                                                     |

Each row is a JSON payload matching the schema for the specified `operation_type`.

## Sample check posting bulk request

```json
{"operation_type":"CHECK_POST","n_entries":1,"bulk_id":"16dfc4c4-c7eb-4002-baca-05098b15166e","header_version":"1.0.0","org_id":"TN-16dfc4c4-c7eb-4002-ANTEC-05098b15166e"}
```

```json
{
  "external_account_id": "6b6e32c3-6f67-453e-8221-bafa8993e113",
  "check_id": "c462b2f3-55cc-42b4-ae9a-7614df3e8e72",
  "check_amount": { "value": 2000, "currency": "USD" },
  "description": "Check posting",
  "settlement_type": "BEGINNING",
  "settlements": [
    { "type": "HOLD", "tracking_id": "e219459f-9a7e-48ec-9c2b-1a40a62d5ca3", "settlement_date": "2025-01-10", "amount": 800 },
    { "type": "HOLD", "tracking_id": "e219459f-9a7e-48ec-9c2b-1a40a62d5ca3", "settlement_date": "2025-01-20", "amount": 1000 },
    { "type": "HOLD", "tracking_id": "e219459f-9a7e-48ec-9c2b-1a40a62d5ca3", "settlement_date": "2025-01-30", "amount": 200 }
  ]
}
```

### Check posting field definitions

| Field                         | Type    | Required | Description                                                   |
| ----------------------------- | ------- | -------- | ------------------------------------------------------------- |
| `external_account_id`         | string  | yes      | Custom account ID used as the corporate‑layer reference key.  |
| `check_id`                    | string  | yes      | Check ID. Identifies your check posting or settlement request |
| `check_amount.value`          | decimal | yes      | Total transaction amount                                      |
| `check_amount.currency`       | string  | no       | Currency code                                                 |
| `description`                 | string  | no       | Transaction description                                       |
| `business_date`               | string  | no       | Posting business date. Defaults to current business date      |
| `settlement_type`             | string  | yes      | When funds become available (`BEGINNING`, `END`)              |
| `settlements.type`            | string  | yes      | `DEPOSIT`, `PENDING`, or `HOLD`                               |
| `settlements.tracking_id`     | string  | yes      | Tracking ID                                                   |
| `settlements.settlement_date` | string  | yes      | Expected settlement date                                      |
| `settlements.amount`          | decimal | yes      | Amount to settle                                              |

## Sample check release bulk request

### Header

```json
{
  "bulk_id":"bf4695d5-c53c-4da3-9255-e88485337aa9",
  "org_id":"TN-097d9c0e-0331-492a-93e2-95c8c2019fd1",
  "header_version":"1.0.0",
  "operation_type":"CHECK_RELEASE",
  "n_entries":2
}
```

### Rows

```json
{"external_account_id":"acc1","check_id":"963ae9db-b841-4fa3-8eb7-454602ca7d3d"}
```

```json
{"external_account_id":"acc1","check_id":"98211b85-ae48-4c01-8e3a-d52720b24c94","tracking_id":"1e87d288-c82a-4858-8e02-96634de21002","settlement_date":"2025-10-31"}
```

### Check release field definitions

| Field                 | Required | Description                                                            |
| --------------------- | -------- | ---------------------------------------------------------------------- |
| `external_account_id` | yes      | Custom account ID                                                      |
| `check_id`            | yes      | Check ID                                                               |
| `tracking_id`         | no       | Tracking ID for the release. Auto-generated if omitted                 |
| `settlement_date`     | no       | Specific settlement date to release. If empty, full amount is released |

## Output format

After processing, two output files are generated.

| File Type   | Description                                  |
| ----------- | -------------------------------------------- |
| `.original` | Contains line‑by‑line processing results     |
| `.sign`     | Signature file for authenticity verification |

### Output header example

```json
{
  "bulk_id": "blk-0001",
  "org_id": "tn-0000-0001",
  "header_version": "1.0.0",
  "operation_type": "CHECK_POST",
  "n_entries": 10000,
  "status": {
    "description": "FAILED",
    "error": {
      "code": "WBLK-0001",
      "message": "Malformatted input file"
    }
  }
}
```

### Header status fields

| Field                  | Description                      |
| ---------------------- | -------------------------------- |
| `status.description`   | `FAILED` or `FINISHED`           |
| `status.error.code`    | Error code if failure            |
| `status.error.message` | Human‑readable error description |

**Note**: A `FAILED` header means **no rows were processed**.

### Row examples

#### Success

```json
{
  "response_status": 202,
  "tracking_id": "9d15bfd1-5db9-4e96-b846-8d8707454430",
  "cid": "ex-cid-1",
  "data": {
    "check_id": "4a4060d5-3649-46e8-8d64-93949b212918"
  }
}
```

#### Failure

```json
{
  "response_status": 400,
  "tracking_id": "9d15bfd1-5db9-4e96-b846-8d8707454430",
  "cid": "ex-cid-1",
  "error": {
    "code": "ERR9999",
    "message": "Error while executing operation"
  }
}
```

# Bulk settlement API

[Bulk settlement API](https://developers.pismo.io/pismo-docs/reference/post-bulk-settlement) allows all pending check operations for a division and settlement date to be executed at once.

### Request example

```json
{
  "operation_type": "check-release",
  "settlement_date": "2024-07-03",
  "bulk_id": "74f8e8df",
  "division_code": "74f8e8df-2c2b-412f-8d35-abdf17d896ec"
}
```

### Field definitions

| Field             | Description                                                              |
| ----------------- | ------------------------------------------------------------------------ |
| `operation_type`  | Must be `check-release`                                                  |
| `settlement_date` | Original pending settlement date (must be current or past business date) |
| `bulk_id`         | ID of the generated bulk file                                            |
| `division_code`   | Division used to query settlement events                                 |

Once the bulk settlement request is processed, the Pismo platform generates these events to indicate status.

* [Bulk payment processing status changed](https://developers.pismo.io/events/docs/corporate-bulk-status-changed-1)
* [Bulk settlement processing status changed](https://developers.pismo.io/events/docs/corporate-bulk-settlement-1)
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `POST /corporate/v1/checks` | `corporate-post-v1-checks` | Create check posting | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--check-posting |
| `POST /corporate/v1/checks/release` | `post-corporate-v1-checks-release` | Release check | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--check-posting |
| `POST /corporate/v1/bulk-settlement` | `post-bulk-settlement` | Request bulk settlement | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--bulk-settlement |

### Operation essentials

- **`POST /corporate/v1/checks`** (`corporate-post-v1-checks`): security `BearerAuth`; required parameters none declared; required body fields `check_id`, `check_amount`, `settlement_type`, `settlements`; response statuses 202, 400, 401, 403, 409, 500; error codes in examples `WCPT0001`, `WCPT0002`, `WCMN0002`, `WCPT0006`, `WCPT0007`, `WCPT0008`, `WCPT0010`, `WCPT0011`, `WCPT0004`, `WCPT0018`, `WCPT0009`, `WCPT0012`, `WCPT0014`, `WCPT0016`, `WCPT0017`, `WCAC0001`, `WCPT0005`, `WCPT0013`, `ECMN9999`; events `cash-management-check-status-change-1`, `platform-authorization-platform-authorization-1`.
- **`POST /corporate/v1/checks/release`** (`post-corporate-v1-checks-release`): security `BearerAuth`; required parameters none declared; required body fields `check_id`; response statuses 202, 400, 401, 403, 404, 409, 500; error codes in examples `WCPT0001`, `WCPT0002`, `WCPT0004`, `WCPT0018`, `WOBK0007`, `WCPT0011`, `WCPT0015`, `WCPT0003`, `WCPT0013`, `WCPT0019`, `ECMN9999`; events `cash-management-check-status-change-1`, `platform-authorization-platform-authorization-1`.
- **`POST /corporate/v1/bulk-settlement`** (`post-bulk-settlement`): security `BearerAuth`; required parameters none declared; required body fields `operation_type`, `settlement_date`, `division_code`, `bulk_id`; response statuses 202, 400, 401, 403, 409, 429, 500; error codes in examples `WSTM0001`, `WSTM0002`, `WSTM0003`, `WSTM0004`, `WSTM0005`, `WSTM0006`, `WSTM0010`, `WSTM0011`, `WSTM0007`, `WSTM0009`, `WSTM0008`, `ECMN9999`; events none listed.

## Events

Events emitted by the referenced operations (`api-reference-data/endpoint_event_map.csv`):

| Operation | Event slug |
| --- | --- |
| `corporate-post-v1-checks` | `cash-management-check-status-change-1` |
| `post-corporate-v1-checks-release` | `cash-management-check-status-change-1` |
| `corporate-post-v1-checks` | `platform-authorization-platform-authorization-1` |
| `post-corporate-v1-checks-release` | `platform-authorization-platform-authorization-1` |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/core-banking/file-based-check-processing-and-bulk-settlement.md`: updatedAt 2026-03-18T15:18:05.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- The source links to 2 event page(s) under `/events/`. Event payload definitions are not part of the corpus (robots.txt disallows `/events/`), so payload fields are not documented here.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/core-banking/file-based-check-processing-and-bulk-settlement.md` | whole document | https://developers.pismo.io/pismo-docs/docs/file-based-check-processing-and-bulk-settlement | `3d231789f22c062b…` | 2026-03-18T15:18:05.000Z |

## Related knowledge units

- `KU-API-banking-transaction-banking--bulk-settlement` — API reference: Banking - Transaction banking — Bulk settlement
- `KU-API-banking-transaction-banking--check-posting` — API reference: Banking - Transaction banking — Check posting
- `KU-EVT-catalogue-other-domains` — Event catalogue: other event domains (accounting, authorization, availables, average, bulletin, cash, delinquent, fraud, instantpay, intl, ledger, networktransactions, onboarding, orgs, payment, platform, programs, rules, savings, statement)
