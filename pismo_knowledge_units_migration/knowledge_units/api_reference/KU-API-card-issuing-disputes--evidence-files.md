---
ku_id: KU-API-card-issuing-disputes--evidence-files
title: 'API reference: Card issuing - Disputes — Evidence files'
category: api_reference
ku_type: api_reference
lifecycle: current
sources:
- path: api-specs/Card_issuing_-_Disputes.yaml
  sha256: 5c1d5513e1f3a4d1daa4d6bd654885c4edfeb5135eaa60b50f1a74d62031baad
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
operations:
- post-v1-disputes-disputeId-file
- get-v1-disputes-disputeId-files
- get-v1-disputes-disputeId-files-fileId
related_kus:
- KU-CARD-disputes-overview
- KU-CARD-visa-dispute-use-case
specification_version: 1.0.0
---

# API reference: Card issuing - Disputes — Evidence files

**KU ID:** `KU-API-card-issuing-disputes--evidence-files` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 3 operation(s) tagged `Evidence files` in `api-specs/Card_issuing_-_Disputes.yaml` (“Card issuing - Disputes”, version `1.0.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Endpoints to handle dispute evidence files

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `POST /v1/disputes/{disputeId}/file` | `post-v1-disputes-disputeId-file` | Upload evidence file | no |
| `GET /v1/disputes/{disputeId}/files` | `get-v1-disputes-disputeId-files` | Get dispute files | no |
| `GET /v1/disputes/{disputeId}/file/{fileId}` | `get-v1-disputes-disputeId-files-fileId` | Download dispute file | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"} — Account access token. Tokens can expire quickly, which can result in an "Unauthorized" error.

## Operation contracts

<!-- op: spec=api-specs/Card_issuing_-_Disputes.yaml method=POST path=/v1/disputes/{disputeId}/file operationId=post-v1-disputes-disputeId-file -->
### `POST /v1/disputes/{disputeId}/file` — Upload evidence file

- **operationId:** `post-v1-disputes-disputeId-file`
- **Specification:** `api-specs/Card_issuing_-_Disputes.yaml` (Card issuing - Disputes)
- **Server base URL(s):** `https://sandbox.pismolabs.io/disputes`
- **Tags:** `Evidence files`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Upload a file for the dispute process.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `disputeId` | path | yes | number | Dispute ID |  |

#### Request body

Required: yes

> File data.

**Content type `multipart/form-data`** — schema: object

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `name` | string | yes | File name.<br>VISA - Anything alphanumeric, no special characters, 20 chars maximum.<br>Mastercard - At least a number and a letter and no special characters. 9 chars maximum.<br> | maxLength: 20; example: "MyFile" |
| `category` | string (schema `DisputeFileCategory`) | yes | File category: <br>  `OTHERS` - Use to upload file on chargeback creation<br>  `PRE_ARBITRATION` - Use to upload files for pre-arbitration<br> | enum: ["OTHERS", "PRE_ARBITRATION"]; example: "PRE_ARBITRATION" |
| `file` | string | yes | Uploaded file. Max size = 14Mb. Must have one of these extensions: .jpg, .jpeg, .tif, .tiff and .pdf. | format: "binary" |
| `dispute_installment_id` | number | no | Dispute installment ID. If not passed, the first Installment is used. | format: "int64" |

Example `Dispute file sample data fields`:

```json
{
  "name": "A personal file",
  "category": "OTHERS",
  "file": "doc.pdf",
  "dispute_installment_id": 1
}
```

Example `Pre arbitration allocation / collaboration Visa`:

```json
{
  "name": "MyFile",
  "category": "PRE_ARBITRATION",
  "file": "doc.pdf",
  "dispute_installment_id": 1
}
```

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `DisputeFileResponse`) |
| 400 | Bad Request |  |
| 401 | Unauthorized. Invalid or missing access token. |  |
| 404 | Not found |  |
| 500 | Internal server error |  |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | number | no | Dispute file ID | example: 1 |
| `org_id` | string (schema `OrgID`) | no | Organization/tenant ID. | example: "TN-34778262-f4f0-464d-b4c6-a14exxxxxxxx" |
| `dispute_id` | number (schema `DisputeID`) | no | Dispute ID | example: 48670 |
| `dispute_installment_id` | integer (schema `DisputeInstallmentId`) | no | Dispute installment ID. | example: 8675309 |
| `installment` | number | no | Installment number |  |
| `path` | string | no | Organization file path | example: "/path/of/directory/" |
| `file_name` | string | no | File name | example: "doc.pdf" |
| `category` | string (schema `DisputeFileCategory2`) | no | File category<br> | enum: ["CARD", "OTHERS", "PRE_ARBITRATION"]; example: "PRE_ARBITRATION" |

200 Example `File Uploaded`:

```json
{
  "id": 1,
  "org_id": "TN:123...456789",
  "dispute_id": 1,
  "path": "/path/of/directory/",
  "file_name": "doc.pdf",
  "category": "OTHERS"
}
```


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;404;500`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-CARD-disputes-overview`, `KU-CARD-visa-dispute-use-case`.

<!-- op: spec=api-specs/Card_issuing_-_Disputes.yaml method=GET path=/v1/disputes/{disputeId}/files operationId=get-v1-disputes-disputeId-files -->
### `GET /v1/disputes/{disputeId}/files` — Get dispute files

- **operationId:** `get-v1-disputes-disputeId-files`
- **Specification:** `api-specs/Card_issuing_-_Disputes.yaml` (Card issuing - Disputes)
- **Server base URL(s):** `https://sandbox.pismolabs.io/disputes`
- **Tags:** `Evidence files`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Get files related to a specific dispute.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `disputeId` | path | yes | number | Dispute ID |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: array of object (schema `DisputeFileResponse`) |
| 400 | Bad Request |  |
| 401 | Unauthorized. Invalid or missing access token. |  |
| 404 | Not found |  |
| 500 | Internal server error |  |

##### Response 200

**200 `application/json` body fields:**

_No fields declared in the schema._

200 Example `List Files`:

```json
[
  {
    "id": 1,
    "org_id": "TN:12...3456789",
    "dispute_id": 1,
    "dispute_installment_id": 1,
    "installment": 1,
    "path": "/path/of/directory/",
    "file_name": "doc.pdf",
    "category": "OTHERS"
  }
]
```


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;404;500`, has examples `True`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Card_issuing_-_Disputes.yaml method=GET path=/v1/disputes/{disputeId}/file/{fileId} operationId=get-v1-disputes-disputeId-files-fileId -->
### `GET /v1/disputes/{disputeId}/file/{fileId}` — Download dispute file

- **operationId:** `get-v1-disputes-disputeId-files-fileId`
- **Specification:** `api-specs/Card_issuing_-_Disputes.yaml` (Card issuing - Disputes)
- **Server base URL(s):** `https://sandbox.pismolabs.io/disputes`
- **Tags:** `Evidence files`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Download an uploaded dispute file

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `disputeId` | path | yes | number | Dispute ID |  |
| `fileId` | path | yes | number | Dispute file ID |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `image/*`: string; `application/pdf`: string |
| 400 | Bad Request |  |
| 404 | Not found |  |
| 500 | Internal server error |  |

##### Response 200

**200 `image/*` body fields:**

_No fields declared in the schema._

**200 `application/pdf` body fields:**

_No fields declared in the schema._


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;404;500`, has examples `False`, emits events `0`, deprecated `False`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.


## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Card_issuing_-_Disputes.yaml` | tag `Evidence files`: POST /v1/disputes/{disputeId}/file, GET /v1/disputes/{disputeId}/files, GET /v1/disputes/{disputeId}/file/{fileId} | https://github.com/PismoDevEx/pismo-api-specs | `5c1d5513e1f3a4d1…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-CARD-disputes-overview` — Disputes overview
- `KU-CARD-visa-dispute-use-case` — Visa dispute use case
