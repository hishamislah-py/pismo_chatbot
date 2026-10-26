---
ku_id: KU-API-banking-credit-receivables--invoices
title: 'API reference: Banking - Credit receivables — Invoices'
category: api_reference
ku_type: api_reference
lifecycle: current
sources:
- path: api-specs/Banking_-_Credit_receivables.yaml
  sha256: eb38b8a710548b184944b0c66db4d4e7de1065f7b76aebc6eb5d1985647e0759
  url: https://github.com/PismoDevEx/pismo-api-specs
  role: openapi_specification
  updated_at: '2026-10-13T20:51:51+00:00'
- path: api-reference-data/operations_catalog.csv
  sha256: b218bf75940b0c374ca9e3a48fe92fb615b559e3192f263aff99b738b50a71cf
  url: https://github.com/PismoDevEx/pismo-api-specs
  role: reference_table
  updated_at: '2026-10-13T20:51:51+00:00'
- path: api-reference-data/request_response_examples.csv
  sha256: ac921f2e8d0d154511b4550462e609cf6bebe3e6ce05dada157e0ed645a80856
  url: https://github.com/PismoDevEx/pismo-api-specs
  role: reference_table
  updated_at: '2026-10-13T20:51:51+00:00'
- path: api-reference-data/endpoint_event_map.csv
  sha256: 34649b6033098e514ab0440f13d45a56ec7fd2b476137de7f9fa6867034655c2
  url: https://github.com/PismoDevEx/pismo-api-specs
  role: reference_table
  updated_at: '2026-10-13T20:51:51+00:00'
operations:
- findByAccessKey
related_kus:
- KU-EVT-catalogue-depositary
- KU-EVT-depositary-data-events
specification_version: v1
---

# API reference: Banking - Credit receivables — Invoices

**KU ID:** `KU-API-banking-credit-receivables--invoices` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 1 operation(s) tagged `Invoices` in `api-specs/Banking_-_Credit_receivables.yaml` (“Banking - Credit receivables”, version `v1`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Endpoints to create and manage invoices

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `GET /v1/invoices/{access_key}` | `findByAccessKey` | Get invoice | no |

## Authentication

- `bearerAuth`: {"bearerFormat": "JWT", "scheme": "bearer", "type": "http"}

## Operation contracts

<!-- op: spec=api-specs/Banking_-_Credit_receivables.yaml method=GET path=/v1/invoices/{access_key} operationId=findByAccessKey -->
### `GET /v1/invoices/{access_key}` — Get invoice

- **operationId:** `findByAccessKey`
- **Specification:** `api-specs/Banking_-_Credit_receivables.yaml` (Banking - Credit receivables)
- **Server base URL(s):** `https://api-sandbox.pismolabs.io/credit-rights-receivable`
- **Tags:** `Invoices`
- **Deprecated in specification:** no
- **Security requirement:** `bearerAuth`

**Description (from the specification):**

> Get and validate invoice given access key in path. The access key is created via the [Register receivable](create-receivable) endpoint.
>
> Pismo works with a third-party (B3) who registers the invoices.
>
> This endpoint generates 4 possible events:
>
> 1. Request to third-party fails - <a href="https://developers.pismo.io/events/docs/depositary-invoice-validation-request-failure-1" target="_blank">invoice_validation_request_failure-1</a>
> 2. Request to third-party succeeds - <a href="https://developers.pismo.io/events/docs/depositary-invoice-validation-request-success-1" target="_blank">invoice_validation_request_success-1</a>
> 3. Third-party validation fails- <a href="https://developers.pismo.io/events/docs/depositary-invoice-validation-failure-1" target="_blank">invoice_validation_failure-1</a>
> 4. Third-party validation succeeds - <a href="https://developers.pismo.io/events/docs/depositary-invoice-validation-success-1" target="_blank">invoice_validation_success-1</a>

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `access_key` | path | yes | string | Client-generated identifier. Must be 44 characters. Created via the [Register receivable](ref:create-receivable) endpoint. | minLength: 44; maxLength: 44 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 202 | Success message is sent to the client while an invoice validation is processed asynchronously,<br> | `application/json`: object (schema `GetInvoiceResponse`) |
| 400 | Bad Request | `application/json`: object (schema `GlobalErrorResponse`) |
| 401 | Missing or invalid access token | `application/json`: object (schema `GlobalErrorResponse`) |
| 500 | Internal Server Error | `application/json`: object (schema `GlobalErrorResponse`) |

##### Response 202

**202 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `access_key` | string (schema `AccessKey`) | no | Client-generated identifier. This field is used for the [Get invoice](ref:findbyaccesskey) endpoint. | minLength: 1; maxLength: 44; example: "KAB6J8903CNMH01892749JKSNOAXMCA7199382ABCERL" |
| `message` | string (schema `Message`) | no | Message | maxLength: 500; example: "Credit rights update request is being processed" |


#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `depositary-invoice-validation-failure-1` | https://developers.pismo.io/events/docs/depositary-invoice-validation-failure-1 |
| `depositary-invoice-validation-request-failure-1` | https://developers.pismo.io/events/docs/depositary-invoice-validation-request-failure-1 |
| `depositary-invoice-validation-request-success-1` | https://developers.pismo.io/events/docs/depositary-invoice-validation-request-success-1 |
| `depositary-invoice-validation-success-1` | https://developers.pismo.io/events/docs/depositary-invoice-validation-success-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `202;400;401;500`, has examples `False`, emits events `4`, deprecated `False`.

Guides that link to this operation: `KU-EVT-depositary-data-events`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/GlobalErrorResponse -->
### Schema `GlobalErrorResponse`

Pointer: `#/components/schemas/GlobalErrorResponse`. Type: object (schema `GlobalErrorResponse`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `correlationId` | string (schema `CorrelationID`) | no | Correlation ID (CID). This field is used to link related API requests and events. The CID can help the Pismo engineering team track everything related to a call. If one isn't passed, one is automatically generated. You can find the CID in a response header. <br> | example: "88474990237-94940" |
| `errors` | array of string (schema `Errors`) | no |  |  |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Banking_-_Credit_receivables.yaml` | tag `Invoices`: GET /v1/invoices/{access_key} | https://github.com/PismoDevEx/pismo-api-specs | `eb38b8a710548b18…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-EVT-catalogue-depositary` — Event catalogue: depositary
- `KU-EVT-depositary-data-events` — Banking - Credit receivables
