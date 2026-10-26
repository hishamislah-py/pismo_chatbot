---
ku_id: KU-PAY-bulk-file-based-payment-processing
title: Bulk file-based payment processing
category: transfers_and_payments
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/core-banking/bulk-file-based-payment-processing.md
  sha256: 5e179137aca7c34e7222e66d64bb7afed46dbc4e9b673a5baadabb9cfd56affa
  url: https://developers.pismo.io/pismo-docs/docs/bulk-file-based-payment-processing
  role: primary_guide
  updated_at: '2026-04-24T21:57:56.000Z'
operations:
- corporate-put-bulk-file
- corporate-v2-post-payments
related_kus:
- KU-API-banking-transaction-banking--bulk-payment-files
- KU-API-banking-transaction-banking--payments-part-01
- KU-EVT-catalogue-account
- KU-EVT-catalogue-other-domains
grouping_rationale: single source page
---

# Bulk file-based payment processing

**KU ID:** `KU-PAY-bulk-file-based-payment-processing` · **Category:** Transfers and payments · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/core-banking/bulk-file-based-payment-processing.md`:

> Bulk file-based payment processing, common among banks and large corporations, is a result of managing multiple accounts with high daily transaction volumes. This is in stark contrast to families and small businesses, where one or two individuals typically manage a single account with significantly fewer transactions. Despite the arrival of faster payment methods, such as same-day and instant payments, file-based payment processing is still widely used. It’s particularly vital for banks with legacy systems, where it’s used to manage high-volume transactions efficiently.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/core-banking/bulk-file-based-payment-processing.md`: Bulk file-based payment processing; Understanding file-based payment processing; Feature restrictions; Security configuration; File format; Naming convention; Input file; Sample input file; Header; Output file; Sample output file; Header; Error response; Common error messages

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 2 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/core-banking/bulk-file-based-payment-processing.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/bulk-file-based-payment-processing · updatedAt: 2026-04-24T21:57:56.000Z

<!-- source:begin path=docs/core-banking/bulk-file-based-payment-processing.md part=0-end -->

# Bulk file-based payment processing

Bulk file-based payment processing, common among banks and large corporations, is a result of managing multiple accounts with high daily transaction volumes. This is in stark contrast to families and small businesses, where one or two individuals typically manage a single account with significantly fewer transactions. Despite the arrival of faster payment methods, such as same-day and instant payments, file-based payment processing is still widely used. It’s particularly vital for banks with legacy systems, where it’s used to manage high-volume transactions efficiently.

With the trend pointing towards a reduction in reliance on bulk processing, Pismo is introducing a new solution that leverages AWS S3 bucket cross-account replication to bridge the gap between traditional bulk processing and fast payment methods. This strategy replicates an S3 object (a file and its associated metadata) uploaded manually by clients to their designated bucket on the Pismo platform, enhancing consumption and processing. This development, along with companies sending daily transaction files to banks, reflects the evolving landscape of transaction management.

In addition to manual uploads, you can also use Pismo's [Upload bulk file](https://developers.pismo.io/pismo-docs/reference/corporate-put-bulk-file) API to upload your files.

# Understanding file-based payment processing

Pismo’s bulk file-based payment processing includes the following features:

* Payments are ingested from a designated AWS S3 bucket, with each file capable of containing up to 500,000 payments.
* Supports all workflows available through the [Post payment](https://developers.pismo.io/pismo-docs/reference/corporate-v2-post-payments) API. The following transaction types are supported:
  * Regular transactions, applies to:
    * Debit
    * Credit
    * Transfer
  * Forced transactions, applies to:
    * Debit
    * Credit
    * Transfer
  * Earmarks
    * Debit and transfer with earmark execution
  * Time-influenced transactions
    * Backdated debit and credit
    * Back business debits and credits
  * Clients can upload more than one per day, as long as they upload them to the specified AWS S3 bucket.
  * Files are processed in parallel.
  * Should any payment within a bulk file fail, the processing of the remaining payments continues independently.
  * Details of both successful and failed payments are provided in a response file.

# Feature restrictions

* Pismo does not provide endpoints for progress tracking. File changes can be monitored by checking the output file in the AWS S3 Bucket.
* Float and Earmark operations fall outside the scope of this project.
* Once a file has been posted and confirmed as received, a feature to cancel its processing is not available.

# Security configuration

Reach out to your Pismo representative for guidance on how to configure security measures for sending and receiving files.

# File format

The Pismo platform handles bulk payment processing by ingesting a UTF-8 encoded input file containing the list of transactions to be processed. The file consists of a header line followed by n-lines, each representing an operation entry in pre-formatted JSON schema. The name of the file must adhere to the naming convention rules detailed in the next section.

## Naming convention

* File names must have the format `{creation-datetime}-{bulk-id}`, where `creation-datetime` is in the UTC timezone and is formatted as `YYYY-MM-DD-hh-mm-ss`.
* `bulk-id` includes only digits, letters, hyphens, and underscores, and has a maximum length of 60 characters. For example: `2023-06-23-11-07-23-a_09BM-001-53`.
* A file extension is not mandatory.
* Upon processing, an output file is generated following the naming convention `{original-input-filename}-out.original`. For example: `2023-06-23-11-07-23-a_09BM-001-53-out.original`.

## Input file

The following sample illustrates how your input files should be structured. The parts of the sample file are explained in detail below it.

### Sample input file

```json
{"bulk_id": "c5a5f9cf-07ab-45c5-a7c5-43d101484aca", "org_id": "TN-097d9c0e-0331-492a-93e2-95c8c2019fd1", "header_version": "1.0.0", "operation_type": "PAYMENT", "n_entries": 5}
{"credit": {"external_account_id": "3c075273-1a56-439b-963b-efff1ae347be", "processing_code": "220035"}, "amount": {"value": 1, "currency": "USD"}, "soft_descriptor": "cash-in", "tracking_id": "8607a074-dcdc-4ae6-bc3e-c227865b6e50"}
{"credit": {"external_account_id": "3c075273-1a56-439b-963b-efff1ae347be", "processing_code": "220035"}, "amount": {"value": 1, "currency": "USD"}, "soft_descriptor": "cash-in", "tracking_id": "5a97fc1f-9f08-43e8-a500-6c450af5d4f5"}
{"credit": {"external_account_id": "3c075273-1a56-439b-963b-efff1ae347be", "processing_code": "220035"}, "amount": {"value": 1, "currency": "USD"}, "soft_descriptor": "cash-in", "tracking_id": "3f2d3619-9a2f-42a2-8746-fe0fe1aef401"}
{"credit": {"external_account_id": "3c075273-1a56-439b-963b-efff1ae347be", "processing_code": "220035"}, "amount": {"value": 1, "currency": "USD"}, "soft_descriptor": "cash-in", "tracking_id": "ba491e35-fb11-4975-9cd4-2b0fc71b0678"}
{"credit": {"external_account_id": "3c075273-1a56-439b-963b-efff1ae347be", "processing_code": "220035"}, "amount": {"value": 1, "currency": "USD"}, "soft_descriptor": "cash-in", "tracking_id": "78dabe62-495a-4f85-b728-c532c57d761d"}
```

### Header

The header of an input file is crucial as it holds specific information about the transaction. It includes details about the originator of the bulk payment processing request, the type of operation, and the count of transactions awaiting processing.

#### Example header

```json
{
  "bulk_id": "c5a5f9cf-07ab-45c5-a7c5-43d101484aca",
  "org_id": "TN-097d9c0e-0331-492a-93e2-95c8c2019fd1",
  "header_version": "1.0.0",
  "operation_type": "PAYMENT",
  "n_entries": 5
}
```

The fields in the example are defined as follows.

* `bulk_id`\
  The ID of the bulk payment request. Only digits, letters, hyphens, and underscores are allowed. Maximum length is 60 characters. `bulk_id` is client-generated.
* `org_id`\
  ID that represents the organization sending the file. This is a client-generated ID.
* `header_version`\
  The version of the header. Must be `1.0.0`.
* `operation_type`\
  The type of the operation to be executed, only `PAYMENT` is supported.
* `n_entries`\
  The number of entries contained in the file. `n_entries` is used to check the number of rows in the file against the value of `n_entries`. The maximum number of rows per file is 500,000.

## Output file

An output file presents the outcomes of a bulk payment processing. The following sample illustrates how output files are structured. The parts of the sample file are explained in detail below it.

### Sample output file

```json
{"bulk_id": "c5a5f9cf-07ab-45c5-a7c5-43d101484aca", "org_id": "TN-097d9c0e-0331-492a-93e2-95c8c2019fd1", "header_version": "1.0.0", "operation_type": "PAYMENT", "n_entries": 5, "status": {"description": "FINISHED"}}
{"response_status": 201, "cid": "ex-cid-1","tracking_id": "5a50d3a3-9ab2-463b-9bfb-7c5044489f95"}
{"response_status": 201, "cid": "ex-cid-2","tracking_id": "5a50d3a3-9ab2-463b-9bfb-7c5044489f96"}
{"response_status": 201, "cid": "ex-cid-3","tracking_id": "5a50d3a3-9ab2-463b-9bfb-7c5044489f97"}
{"response_status": 201, "cid": "ex-cid-4","tracking_id": "5a50d3a3-9ab2-463b-9bfb-7c5044489f98"}
{"response_status": 400, "cid": "ex-cid-5", "error": {"code": "WPMT-0010", "message": "Insufficient funds"},"tracking_id": "5a50d3a3-9ab2-463b-9bfb-7c5044489f99"}
```

### Header

```json
{
  "bulk_id": "blk-0001",
	"org_id": "tn-0000-0001",
	"header_version": "1.0.0",
	"operation_type": "PAYMENT",
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

* `bulk_id`\
  ID of the bulk payment request. Only digits, letters, hyphens, and underscores are allowed. Maximum character length allowed is 60. This ID is client-generated.
* `org_id`\
  A client-generated ID that represents the organization sending the file.
* `header_version`\
  The version of the header. It must be `1.0.0`.
* `operation_type`\
  The type of the operation to be executed.  Only `PAYMENT` is supported.
* `n_entries`\
  The number of entries contained in the file.
* `status`\
  Details about the result of payment processing:
  * `description`\
    Status name. It can be `CREATED`, `FAILED`, or `FINISHED`.
  * `error`\
    This field is populated with an error code and a corresponding message in case an error occurs while processing the input file:
    * `code`\
      Error code that represents the error.
    * `message`\
      Message that describes the error.

### Error response

In the event of a processing error, the output file (response file) includes the unsuccessful transaction, along with its corresponding error code and message. Refer to the sample in [Output file](#output-file), where an unsuccessful transaction does not prevent Pismo from processing other transactions in the file.

Example of a JSON object for a failed transaction:

```json
{
  "response_status": 400,
  "error": {
    "code": "WPMT-0010",
    "message": "Insufficient funds"
  },
  "cid": "ex-cid-5",
  "tracking_id": "5a50d3a3-9ab2-463b-9bfb-7c5044489f99"
}
```

The fields in the above example are defined as follows.

* `response_status`\
  HTTP status code returned for the specific operation.
* `error`\
  This attribute is populated in case of an error:
  * `code`\
    Error code.
  * `message`\
    Error message.
  * `cid`\
    Correlation ID for the operation.
  * `tracking_id`\
    ID that identifies the payment transaction encountering error.

### Common error messages

Here is a list of common error messages contained in the response file.

| Code     | Message                                         | Cause                                                                                                               |
| -------- | ----------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| WBLK1001 | Entry count mismatch                            | The number of entries in the file is different from that provided in the header.                                    |
| WBLK1002 | Entry limit exceeded                            | The number of entries in the file exceeds the maximum limit of 500,000.                                             |
| WBLK1005 | Validation error: `HeaderVersion` not supported | The provided header version is not supported. The only supported version is `1.0.0`.                                |
| WBLK1005 | Validation error: `OperationType` not supported | The provided operation type is not supported. The allowed types are `PAYMENT`, `FLOAT_PAYMENT`, and `FUTURE_DATED`. |
| WBLK1006 | Duplicate bulk ID                               | Bulk ID is already in use by a different file.                                                                      |
| WBLK1007 | Quota exceeded                                  | This error occurs when you exceed the daily limit of 10 successful input file uploads.                              |
| WBLK1008 | Invalid signature                               | Signature provided is not valid.                                                                                    |
| WBLK1009 | Key expired                                     | Public key has expired.                                                                                             |
| WBLK1010 | Key not found                                   | Public key is not found.                                                                                            |
| WBLK1011 | Invalid JSON input                              | Header from the original file is not in valid JSON format.                                                          |
| WBLK1012 | Invalid encryption key                          | Encryption keys are not found.                                                                                      |
| WBLK1012 | Invalid encryption key                          | An invalid UTF-8 file is generated after decryption using the provided key.                                         |
| WBLK1013 | Invalid JSON signature                          | Signature file is missing or contains JSON syntax errors.                                                           |
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `PUT /corporate/v1/bulk-payments/{bulkId}` | `corporate-put-bulk-file` | Upload bulk file | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--bulk-payment-files |
| `POST /corporate/v2/payments` | `corporate-v2-post-payments` | Post payment | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--payments-part-01 |

### Operation essentials

- **`PUT /corporate/v1/bulk-payments/{bulkId}`** (`corporate-put-bulk-file`): security `BearerAuth`; required parameters `bulkId` (path), `signature` (header); required body fields none declared; response statuses 200, 400, 401, 403, 409, 500; error codes in examples `WBUP0001`, `WBUP0004`, `WBUP0005`, `WBUP0006`, `WBUP0007`, `WBUP0008`, `WBUP0009`, `WBUP0010`, `WBUP0003`, `ECMN9999`; events none listed.
- **`POST /corporate/v2/payments`** (`corporate-v2-post-payments`): security `BearerAuth`; required parameters none declared; required body fields `amount`, `tracking_id`; response statuses 201, 400, 401, 403, 404, 409, 423, 500; error codes in examples `WOBK0007`, `WPMT0017`, `WPMT0011`, `WPMT0053`, `WPMT0018`, `WPMT0029`, `WPMT0030`, `WPMT0031`, `WPMT0062`, `WPMT0063`, `WCAC0010`, `WPMT0001`, `WPMT0061`, `WPMT0015`, `WPMT0016`, `WPMT0003`, `WPMT0004`, `WPMT0005`, `WPMT0006`, `WPMT0009`, `WPMT0010`, `WPMT0021`, `WEAM0008`, `WEAM0006`, `WPMT0050`, `WEAM0017`, `WEAM0019`, `WPMT0022`, `WPMT0023`, `WPMT0024`, `WPMT0025`, `WPMT0026`, `WCMN0002`, `WPMT0028`, `WPMT0045`, `WPMT0049`, `WPMT0036`, `WPMT0044`, `WPMT0051`, `WPMT0035`, `WPMT0046`, `WPMT0054`, `WPMT0055`, `WPMT0056`, `WPMT0058`, `WPMT0008`, `WPMT0014`, `WPMT0019`, `WCAC0002`, `WCAC0012`, `WPMT0002`, `WCAC0001`, `WEAM0007`, `WPMT0007`, `WPMT0052`, `WEAM0049`, `WPMT0047`, `WEAM0048`, `ECMN9999`; events `account-balances-balance-change-1`, `accounting-entry-creation-1`, `availables-change-available-1`, `platform-authorization-platform-authorization-1`, `rules-evaluation-requested-1`.

## Events

Events emitted by the referenced operations (`api-reference-data/endpoint_event_map.csv`):

| Operation | Event slug |
| --- | --- |
| `corporate-v2-post-payments` | `account-balances-balance-change-1` |
| `corporate-v2-post-payments` | `accounting-entry-creation-1` |
| `corporate-v2-post-payments` | `availables-change-available-1` |
| `corporate-v2-post-payments` | `platform-authorization-platform-authorization-1` |
| `corporate-v2-post-payments` | `rules-evaluation-requested-1` |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/core-banking/bulk-file-based-payment-processing.md`: updatedAt 2026-04-24T21:57:56.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- None identified by the migration checks.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/core-banking/bulk-file-based-payment-processing.md` | whole document | https://developers.pismo.io/pismo-docs/docs/bulk-file-based-payment-processing | `5e179137aca7c34e…` | 2026-04-24T21:57:56.000Z |

## Related knowledge units

- `KU-API-banking-transaction-banking--bulk-payment-files` — API reference: Banking - Transaction banking — Bulk payment files
- `KU-API-banking-transaction-banking--payments-part-01` — API reference: Banking - Transaction banking — Payments (part 1 of 3)
- `KU-EVT-catalogue-account` — Event catalogue: account
- `KU-EVT-catalogue-other-domains` — Event catalogue: other event domains (accounting, authorization, availables, average, bulletin, cash, delinquent, fraud, instantpay, intl, ledger, networktransactions, onboarding, orgs, payment, platform, programs, rules, savings, statement)
