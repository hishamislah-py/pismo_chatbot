---
ku_id: KU-API-core-platform-accounting--accounting-entry-types
title: 'API reference: Core platform - Accounting — Accounting entry types'
category: api_reference
ku_type: api_reference
lifecycle: current
sources:
- path: api-specs/Core_platform_-_Accounting.yaml
  sha256: f0272a891eaca0fedca4fa47cc760ff7fd676f50c94a22aa19ac665fa7017451
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
- SearchEntryTypesV2
- CreateEntryTypeV2
- GetEntryTypeByIdV2
- DeleteEntryTypeV2
- UpdateEntryTypeV2
- SearchEntryTypes
- GetEntryTypeById
related_kus:
- KU-CORE-accounting-accounts-and-entries
- KU-CORE-accounting-overview
specification_version: 1.0.0
---

# API reference: Core platform - Accounting — Accounting entry types

**KU ID:** `KU-API-core-platform-accounting--accounting-entry-types` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 7 operation(s) tagged `Accounting entry types` in `api-specs/Core_platform_-_Accounting.yaml` (“Core platform - Accounting”, version `1.0.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Endpoints to manage accounting entry types.

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `GET /v2/entry-types` | `SearchEntryTypesV2` | List accounting entry types | no |
| `POST /v2/entry-types` | `CreateEntryTypeV2` | Create accounting entry types | no |
| `GET /v2/entry-types/{entryTypeId}` | `GetEntryTypeByIdV2` | Get accounting entry type | no |
| `DELETE /v2/entry-types/{entryTypeId}` | `DeleteEntryTypeV2` | Delete accounting entry type | no |
| `PATCH /v2/entry-types/{entryTypeId}` | `UpdateEntryTypeV2` | Update accounting entry type | no |
| `GET /v1/entry-types` | `SearchEntryTypes` | List accounting entry types (outdated) | no |
| `GET /v1/entry-types/{entryTypeId}` | `GetEntryTypeById` | Get accounting entry type (outdated) | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"} — Account access token. Tokens can expire quickly, which can result in an "Unauthorized" error.

## Operation contracts

<!-- op: spec=api-specs/Core_platform_-_Accounting.yaml method=GET path=/v2/entry-types operationId=SearchEntryTypesV2 -->
### `GET /v2/entry-types` — List accounting entry types

- **operationId:** `SearchEntryTypesV2`
- **Specification:** `api-specs/Core_platform_-_Accounting.yaml` (Core platform - Accounting)
- **Server base URL(s):** `https://sandbox.pismolabs.io/accounting`
- **Tags:** `Accounting entry types`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> List accounting entry types with their latest history from your organization.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `pageSize` | query | no | integer | Maximum number of accounting event types per page. |  |
| `pageOffset` | query | no | integer | Number to offset page resuts. For example, value `2` returns the third page. Defaults to `0`, which returns the first page. |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object |
| 400 | Bad request when a provided parameter is invalid |  |
| 404 | Entry type not found |  |
| 500 | Internal server error |  |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `has_next` | boolean | no | Indicates if there are more items to be retrieved. |  |
| `items` | array of object | no | Items retrieved from a given request. |  |
| `items` | array of object (schema `EntryType`) | no |  |  |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;404;500`, has examples `False`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Core_platform_-_Accounting.yaml method=POST path=/v2/entry-types operationId=CreateEntryTypeV2 -->
### `POST /v2/entry-types` — Create accounting entry types

- **operationId:** `CreateEntryTypeV2`
- **Specification:** `api-specs/Core_platform_-_Accounting.yaml` (Core platform - Accounting)
- **Server base URL(s):** `https://sandbox.pismolabs.io/accounting`
- **Tags:** `Accounting entry types`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Create accounting entry type for your organization.

#### Request body

Required: no

**Content type `application/json`** — schema: object (schema `EntryTypePost`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | integer (schema `EntryTypeID`) | yes | Entry type ID | format: "int64"; example: 101 |
| `description` | string (schema `EntryTypeDescription`) | yes | Entry type description. | maxLength: 250; example: "CREDIT" |
| `type` | string (schema `EntryTypeType`) | yes | Set the entry type:<br><br>* `CREATION`: Default value for new entries. Also, this value is assumed when type is not provided.<br>* `DUE_DATE`: Used only with a credit program to indicate a due date entry.<br> | enum: ["DUE_DATE", "CREATION"]; maxLength: 100; example: "DUE_DATE" |
| `reason` | string (schema `HistoryReason`) | yes | Reason for the operation. | maxLength: 250; example: "Creation of a new entry type configuration." |
| `responsible` | string (schema `HistoryResponsible`) | no | User name or ID of the person performing the operation. | maxLength: 100; example: "John Doe" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | Ok | `application/json`: array of object (schema `EntryType`) |
| 400 | Bad request when a provided parameter is invalid |  |
| 409 | Bad request (conflict) when ID already exists |  |
| 500 | Internal server error |  |

##### Response 201

**201 `application/json` body fields:**

_No fields declared in the schema._


Catalogue row (api-reference-data/operations_catalog.csv): response codes `201;400;409;500`, has examples `False`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Core_platform_-_Accounting.yaml method=GET path=/v2/entry-types/{entryTypeId} operationId=GetEntryTypeByIdV2 -->
### `GET /v2/entry-types/{entryTypeId}` — Get accounting entry type

- **operationId:** `GetEntryTypeByIdV2`
- **Specification:** `api-specs/Core_platform_-_Accounting.yaml` (Core platform - Accounting)
- **Server base URL(s):** `https://sandbox.pismolabs.io/accounting`
- **Tags:** `Accounting entry types`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Get a specific accounting entry type by its ID with its historic information.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `entryTypeId` | path | yes | integer | Numeric entry type ID | format: "int64" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `EntryTypeGetById`) |
| 400 | Bad request when a provided parameter is invalid |  |
| 404 | Entry type not found |  |
| 500 | Internal server error |  |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | integer (schema `EntryTypeID`) | no | Entry type ID | format: "int64"; example: 101 |
| `description` | string (schema `EntryTypeDescription`) | no | Entry type description. | maxLength: 250; example: "CREDIT" |
| `type` | string (schema `EntryTypeType`) | no | Set the entry type:<br><br>* `CREATION`: Default value for new entries. Also, this value is assumed when type is not provided.<br>* `DUE_DATE`: Used only with a credit program to indicate a due date entry.<br> | enum: ["DUE_DATE", "CREATION"]; maxLength: 100; example: "DUE_DATE" |
| `reason` | string (schema `HistoryReason`) | no | Reason for the operation. | maxLength: 250; example: "Creation of a new entry type configuration." |
| `responsible` | string (schema `HistoryResponsible`) | no | User name or ID of the person performing the operation. | maxLength: 100; example: "John Doe" |
| `history` | array of object (schema `History`) | no |  |  |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;404;500`, has examples `False`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Core_platform_-_Accounting.yaml method=DELETE path=/v2/entry-types/{entryTypeId} operationId=DeleteEntryTypeV2 -->
### `DELETE /v2/entry-types/{entryTypeId}` — Delete accounting entry type

- **operationId:** `DeleteEntryTypeV2`
- **Specification:** `api-specs/Core_platform_-_Accounting.yaml` (Core platform - Accounting)
- **Server base URL(s):** `https://sandbox.pismolabs.io/accounting`
- **Tags:** `Accounting entry types`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Delete a specific accounting entry type by its ID.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `entryTypeId` | path | yes | integer | Numeric entry type ID | format: "int64" |

#### Request body

Required: no

**Content type `application/json`** — schema: object (schema `EntryTypeDelete`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `reason` | string (schema `HistoryReason`) | yes | Reason for the operation. | maxLength: 250; example: "Creation of a new entry type configuration." |
| `responsible` | string (schema `HistoryResponsible`) | no | User name or ID of the person performing the operation. | maxLength: 100; example: "John Doe" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK |  |
| 400 | Bad request when a provided parameter is invalid |  |
| 404 | Entry type not found |  |
| 500 | Internal server error |  |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;404;500`, has examples `False`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Core_platform_-_Accounting.yaml method=PATCH path=/v2/entry-types/{entryTypeId} operationId=UpdateEntryTypeV2 -->
### `PATCH /v2/entry-types/{entryTypeId}` — Update accounting entry type

- **operationId:** `UpdateEntryTypeV2`
- **Specification:** `api-specs/Core_platform_-_Accounting.yaml` (Core platform - Accounting)
- **Server base URL(s):** `https://sandbox.pismolabs.io/accounting`
- **Tags:** `Accounting entry types`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Update a specific accounting entry type by its ID.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `entryTypeId` | path | yes | integer | Numeric entry type ID | format: "int64" |

#### Request body

Required: no

**Content type `application/json`** — schema: object (schema `EntryTypePatch`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `description` | string (schema `EntryTypeDescription`) | no | Entry type description. | maxLength: 250; example: "CREDIT" |
| `type` | string (schema `EntryTypeType`) | no | Set the entry type:<br><br>* `CREATION`: Default value for new entries. Also, this value is assumed when type is not provided.<br>* `DUE_DATE`: Used only with a credit program to indicate a due date entry.<br> | enum: ["DUE_DATE", "CREATION"]; maxLength: 100; example: "DUE_DATE" |
| `reason` | string (schema `HistoryReason`) | yes | Reason for the operation. | maxLength: 250; example: "Creation of a new entry type configuration." |
| `responsible` | string (schema `HistoryResponsible`) | no | User name or ID of the person performing the operation. | maxLength: 100; example: "John Doe" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Ok | `application/json`: array of object (schema `EntryType`) |
| 400 | Bad request when a provided parameter is invalid |  |
| 404 | Entry type not found |  |
| 500 | Internal server error |  |

##### Response 200

**200 `application/json` body fields:**

_No fields declared in the schema._


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;404;500`, has examples `False`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Core_platform_-_Accounting.yaml method=GET path=/v1/entry-types operationId=SearchEntryTypes -->
### `GET /v1/entry-types` — List accounting entry types (outdated)

- **operationId:** `SearchEntryTypes`
- **Specification:** `api-specs/Core_platform_-_Accounting.yaml` (Core platform - Accounting)
- **Server base URL(s):** `https://sandbox.pismolabs.io/accounting`
- **Tags:** `Accounting entry types`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> List accounting entry types from your organization.
>
> This endpoint is outdated and new endpoint is available: [List accounting entry types](ref:searchentrytypesv2).
>
> Refer to [Search for accounting entry types](doc:create-accounting-entries#search-for-accounting-entry-types) for more information.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `pageSize` | query | no | integer | Maximum number of accounting event types per page. |  |
| `pageOffset` | query | no | integer | Number to offset page resuts. For example, value `2` returns the third page. Defaults to `0`, which returns the first page. |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object |
| 400 | Bad request |  |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `has_next` | boolean | no | Indicates if there are more items to be retrieved. |  |
| `items` | array of object | no | Items retrieved from a given request. |  |
| `items` | array of object (schema `EntryType`) | no |  |  |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400`, has examples `False`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Core_platform_-_Accounting.yaml method=GET path=/v1/entry-types/{entryTypeId} operationId=GetEntryTypeById -->
### `GET /v1/entry-types/{entryTypeId}` — Get accounting entry type (outdated)

- **operationId:** `GetEntryTypeById`
- **Specification:** `api-specs/Core_platform_-_Accounting.yaml` (Core platform - Accounting)
- **Server base URL(s):** `https://sandbox.pismolabs.io/accounting`
- **Tags:** `Accounting entry types`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Get a specific accounting entry type by its ID.
>
> This endpoint is outdated and new endpoint is available: [Get accounting entry type](ref:getentrytypebyidv2).
>
> Refer to [Search for accounting entry types](doc:create-accounting-entries#search-for-accounting-entry-types) for more information.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `entryTypeId` | path | yes | integer | Entry type ID | format: "int64" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `EntryType`) |
| 404 | Entry type not found |  |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | integer (schema `EntryTypeID`) | no | Entry type ID | format: "int64"; example: 101 |
| `description` | string (schema `EntryTypeDescription`) | no | Entry type description. | maxLength: 250; example: "CREDIT" |
| `type` | string (schema `EntryTypeType`) | no | Set the entry type:<br><br>* `CREATION`: Default value for new entries. Also, this value is assumed when type is not provided.<br>* `DUE_DATE`: Used only with a credit program to indicate a due date entry.<br> | enum: ["DUE_DATE", "CREATION"]; maxLength: 100; example: "DUE_DATE" |
| `org_id` | string (schema `OrgID`) | no | Organization ID | example: "TN-XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX" |
| `history` | object (schema `History`) | no | Historical information for auditing the entity. |  |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;404`, has examples `False`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-CORE-accounting-accounts-and-entries`, `KU-CORE-accounting-overview`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/EntryType -->
### Schema `EntryType`

Pointer: `#/components/schemas/EntryType`. Type: object (schema `EntryType`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | integer (schema `EntryTypeID`) | no | Entry type ID | format: "int64"; example: 101 |
| `description` | string (schema `EntryTypeDescription`) | no | Entry type description. | maxLength: 250; example: "CREDIT" |
| `type` | string (schema `EntryTypeType`) | no | Set the entry type:<br><br>* `CREATION`: Default value for new entries. Also, this value is assumed when type is not provided.<br>* `DUE_DATE`: Used only with a credit program to indicate a due date entry.<br> | enum: ["DUE_DATE", "CREATION"]; maxLength: 100; example: "DUE_DATE" |
| `org_id` | string (schema `OrgID`) | no | Organization ID | example: "TN-XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX" |
| `history` | object (schema `History`) | no | Historical information for auditing the entity. |  |

<!-- schema: #/components/schemas/History -->
### Schema `History`

Pointer: `#/components/schemas/History`. Type: object (schema `History`).

> Historical information for auditing the entity.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `org_id` | string (schema `OrgID`) | no | Organization ID | example: "TN-XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX" |
| `action` | string | no | Action performed on the entity. | example: "Created" |
| `reason` | string (schema `HistoryReason`) | no | Reason for the operation. | maxLength: 250; example: "Creation of a new entry type configuration." |
| `responsible` | string (schema `HistoryResponsible`) | no | User name or ID of the person performing the operation. | maxLength: 100; example: "John Doe" |
| `version` | integer | no | Entity version. | format: "int64"; example: 1 |
| `jsonb` | string | no | JSON representation of the request body. | example: "{\\"id\\": 101, \\"description\\": \\"CREDIT\\", \\"type\\": \\"DUE_DATE\\", \\"reason\\": \\"Creation of a new entry type configuration.\\", \\"responsible\\": \\"John Doe\\", \\"created_at\\": \\"2021-10-10T10:10:00Z\\"}" |
| `created_at` | string | no | Date and time when the history was created (ISO 8601). Format: YYYY-MM-DDThh:mm:ssZ. | format: "date-time"; example: "2021-10-10T10:10:00Z" |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Core_platform_-_Accounting.yaml` | tag `Accounting entry types`: GET /v2/entry-types, POST /v2/entry-types, GET /v2/entry-types/{entryTypeId}, DELETE /v2/entry-types/{entryTypeId}, PATCH /v2/entry-types/{entryTypeId}, GET /v1/entry-types, GET /v1/entry-types/{entryTypeId} | https://github.com/PismoDevEx/pismo-api-specs | `f0272a891eaca0fe…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-CORE-accounting-accounts-and-entries` — Creating accounting accounts and accounting entries
- `KU-CORE-accounting-overview` — Accounting overview and accounting event types
