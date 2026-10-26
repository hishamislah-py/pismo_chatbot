---
ku_id: KU-API-card-issuing-cards--embossing-data
title: 'API reference: Card issuing - Cards — Embossing data'
category: api_reference
ku_type: api_reference
lifecycle: current
sources:
- path: api-specs/Card_issuing_-_Cards.yaml
  sha256: 687df76f123e41a762721ae0b3fe344c701d22f47bdd929d033b1ad2d14ca406
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
- get-embossing-info
- get-noname-embossing-info
- get-embossing-file-info
- get-embossing-download-file
- get-embossing-configurations-info
- get-embossing-history
related_kus:
- KU-CARD-physical-card-embossing
- KU-EVT-catalogue-cards
specification_version: 1.4.6
---

# API reference: Card issuing - Cards — Embossing data

**KU ID:** `KU-API-card-issuing-cards--embossing-data` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 6 operation(s) tagged `Embossing data` in `api-specs/Card_issuing_-_Cards.yaml` (“Card issuing - Cards”, version `1.4.6`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Embossing data endpoints

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `GET /embossing/v1/cards/{cardId}` | `get-embossing-info` | Get nominal card embossing info | no |
| `GET /embossing/v1/cards/noname/{cardId}` | `get-noname-embossing-info` | Get noname card embossing info | no |
| `GET /embossing/v1/file-info` | `get-embossing-file-info` | List embossing files info | no |
| `GET /embossing/v1/download-file` | `get-embossing-download-file` | Get embossing file | no |
| `GET /embossing/v1/configurations/info` | `get-embossing-configurations-info` | Get org embosser info | no |
| `GET /embossing/v1/cards/{cardId}/history` | `get-embossing-history` | Get card embossing history | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"} — Account token - an access token encoded with a Pismo account ID. Tokens can expire quickly, which can result in an "Unauthorized" error.

## Operation contracts

<!-- op: spec=api-specs/Card_issuing_-_Cards.yaml method=GET path=/embossing/v1/cards/{cardId} operationId=get-embossing-info -->
### `GET /embossing/v1/cards/{cardId}` — Get nominal card embossing info

- **operationId:** `get-embossing-info`
- **Specification:** `api-specs/Card_issuing_-_Cards.yaml` (Card issuing - Cards)
- **Server base URL(s):** `https://sandbox.pismolabs.io`, `https://gw-pci.pismolabs.io`
- **Tags:** `Embossing data`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Get nominal card embossing information.<br>
>
> For more information on embossing, refer to the [Physical card embossing](doc:physical-card-embossing) guide.
>
> **Notes:** 
>   * This is a PCI endpoint, use the https://gw-pci.pismolabs.io environment.
>   * This endpoint requires an account token - an access token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a **401 Unauthorized** error message. 

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `cardId` | path | yes | string | Pismo card ID | example: "12345" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Nominal card embossing information response object | `application/json`: object (schema `GetNominalCardEmbossingInfoResponse`) |
| 400 | Bad Request | `application/json`: object |
| 404 | Not Found | `application/json`: object |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `org_id` | string (schema `OrgID`) | no | Organization/tenant ID | example: "TN-f878e4a1-2879-48ba-be16-821e73ac98db" |
| `program_id` | integer (schema `ProgramID`) | no | Pismo program ID | example: 7654 |
| `customer_id` | integer (schema `CustomerID`) | no | Pismo customer ID | example: 765476676 |
| `account_id` | integer (schema `AccountID`) | no | Pismo account ID | example: 7654776 |
| `card_id` | integer (schema `CardID2`) | no | Pismo card ID | example: 123456 |
| `filename` | string | no | File name | example: "embossing_filename.pgp" |
| `created_datetime` | string | no | File created date/time. RFC 3339 value. | example: "2022-05-31T17:45:23Z" |
| `updated_datetime` | string | no | File updated date/time. RFC 3339 value. | example: "2022-06-03T08:32:46Z" |
| `embossing_group` | string (schema `EmbossingGroup`) | no | Embossing group name. Clients can work with multi-embossers. You can use this field to notify an embosser about a card request. If this parameter is not passed, and you work with multi-embossers, the default embosser is used. For more information, refer to the [Physical card embossing](doc:physical-card-embossing) guide.<br> | minLength: 2; maxLength: 32; example: "EM1-embosser" |
| `address_id` | integer | no | Address object ID | example: 12345678 |

##### Response 400

400 Example `example-bad-request`:

```json
{
  "message": "Invalid card ID",
  "error": "bad_request",
  "status": 400,
  "error_code": ""
}
```

##### Response 404

404 Example `example-not-found`:

```json
{
  "message": "Card not found",
  "error": "not_found",
  "status": 404,
  "error_code": ""
}
```


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;404`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-CARD-physical-card-embossing`.

<!-- op: spec=api-specs/Card_issuing_-_Cards.yaml method=GET path=/embossing/v1/cards/noname/{cardId} operationId=get-noname-embossing-info -->
### `GET /embossing/v1/cards/noname/{cardId}` — Get noname card embossing info

- **operationId:** `get-noname-embossing-info`
- **Specification:** `api-specs/Card_issuing_-_Cards.yaml` (Card issuing - Cards)
- **Server base URL(s):** `https://sandbox.pismolabs.io`, `https://gw-pci.pismolabs.io`
- **Tags:** `Embossing data`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Get noname card embossing group information.
>
> Noname cards are batch-generated and not initially associated with customers, which occurs later.
>
> Contact your Pismo representative to set up your embossing configuration and process. For more information on embossing, refer to the [Physical card embossing](doc:physical-card-embossing) guide.
>
> **Note:** This is a PCI endpoint, use the https://gw-pci.pismolabs.io environment.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `cardId` | path | yes | string | Pismo card ID | example: "12345" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Get noname card embossing information response | `application/json`: object (schema `GetNonameEmbossingInfoResponse`) |
| 400 | Bad Request | `application/json`: object |
| 404 | Not Found | `application/json`: object |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `program_id` | integer (schema `ProgramID`) | no | Pismo program ID | example: 7654 |
| `card_id` | integer (schema `CardID2`) | no | Pismo card ID | example: 123456 |
| `embossing_group` | string (schema `EmbossingGroup`) | no | Embossing group name. Clients can work with multi-embossers. You can use this field to notify an embosser about a card request. If this parameter is not passed, and you work with multi-embossers, the default embosser is used. For more information, refer to the [Physical card embossing](doc:physical-card-embossing) guide.<br> | minLength: 2; maxLength: 32; example: "EM1-embosser" |

200 Example `example`:

```json
{
  "program_id": 0,
  "card_id": 0,
  "embossing_group": "embosser-1"
}
```

##### Response 400

400 Example `example-bad-request`:

```json
{
  "message": "the param cardId is invalid",
  "error": "bad_request",
  "status": 400,
  "error_code": ""
}
```

##### Response 404

404 Example `example-not-found`:

```json
{
  "message": "card not found",
  "error": "not_found",
  "status": 404,
  "error_code": ""
}
```


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;404`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-CARD-physical-card-embossing`.

<!-- op: spec=api-specs/Card_issuing_-_Cards.yaml method=GET path=/embossing/v1/file-info operationId=get-embossing-file-info -->
### `GET /embossing/v1/file-info` — List embossing files info

- **operationId:** `get-embossing-file-info`
- **Specification:** `api-specs/Card_issuing_-_Cards.yaml` (Card issuing - Cards)
- **Server base URL(s):** `https://sandbox.pismolabs.io`, `https://gw-pci.pismolabs.io`
- **Tags:** `Embossing data`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> List embossing file information with date, program, and configuration filters. 
>
> For more information about embossing, refer to the [Physical card embossing](doc:physical-card-embossing) guide.
>
> For detailed information about embossing flows, refer to [Embossing flows](doc:physical-card-embossing#embossing-flows).
>
> **Note:** This is a PCI endpoint, use the https://gw-pci.pismolabs.io environment.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `beginDate` | query | yes | string | Beginning date filter, format = yyyy-mm-dd | format: "date"; example: "2022-08-27" |
| `endDate` | query | yes | string | End date filter, format = yyyy-mm-dd | format: "date"; example: "2022-08-27" |
| `programs` | query | no | array of string | Organization program ID array | example: ["1", "2", "3"] |
| `configId` | query | no | string | Embossing configuration/group ID.<br><br>You can call [Get nominal card embossing info](https://developers.pismo.io/pismo-docs/reference/get-embossing-info) to get a card's embossing details.<br><br>You can also call [Get org embosser info](https://developers.pismo.io/pismo-docs/reference/get-embossing-configurations-info) to get details about an Org's embossing settings. <br> | format: "uuid"; example: "6dacfdde-64bd-4a17-bbdf-3be627b271e6" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Embossing files info array. | `application/json`: object |
| 204 | No Content |  |
| 400 | Bad Request | `application/json`: object |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `embossing_files` | array of object (schema `EmbosserFileInfo`) | no |  |  |

200 Example `example`:

```json
{
  "embossing_files": [
    {
      "org_id": "tn-123",
      "file_id": "6dacfdde-64bd-4a17-bbdf-3be627b271e6",
      "file_name": "EMBOSSERFILE.pgp",
      "config_id": "6dacfdde-64bd-4a17-bbdf-3be627b271e6",
      "program_id": 0,
      "generation_date": "2022-08-24T20:13:24Z",
      "total_embossed_cards": 1000,
      "total_unembossed_cards": 20
    }
  ]
}
```

##### Response 400

400 Example `example-bad-request`:

```json
{
  "message": "start date is required",
  "error": "bad_request",
  "status": 400
}
```


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;204;400`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-CARD-physical-card-embossing`.

<!-- op: spec=api-specs/Card_issuing_-_Cards.yaml method=GET path=/embossing/v1/download-file operationId=get-embossing-download-file -->
### `GET /embossing/v1/download-file` — Get embossing file

- **operationId:** `get-embossing-download-file`
- **Specification:** `api-specs/Card_issuing_-_Cards.yaml` (Card issuing - Cards)
- **Server base URL(s):** `https://sandbox.pismolabs.io`, `https://gw-pci.pismolabs.io`
- **Tags:** `Embossing data`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Download embossing file sent from Pismo to an embosser. Only available in the EXT environment.
>
> You can call the [List embossing files info](ref:get-embossing-file-info) endpoint to get embossing file names and configuration IDs.
>
> Embossing file names are also available via two events: [Card embossing notification received](https://developers.pismo.io/events/docs/cards-embossing-1) (`tracking` field) and the [Embossing summary received](https://developers.pismo.io/events/docs/cards-embossing-summary-1) event (`file-name` field).
>
> For more information about embossing, refer to the [Physical card embossing](doc:physical-card-embossing) guide.
>
> For detailed information about embossing flows, refer to [Embossing flows](doc:physical-card-embossing#embossing-flows).
>
> **Note:** This is a PCI endpoint, use the https://gw-pci.pismolabs.io environment.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `configId` | query | no | string | Embossing configuration/group ID.<br><br>You can call [Get nominal card embossing info](https://developers.pismo.io/pismo-docs/reference/get-embossing-info) to get a card's embossing details.<br><br>You can also call [Get org embosser info](https://developers.pismo.io/pismo-docs/reference/get-embossing-configurations-info) to get details about an Org's embossing settings. <br> | format: "uuid"; example: "6dacfdde-64bd-4a17-bbdf-3be627b271e6" |
| `fileName` | query | yes | string | Embossing file to download | example: "myEmbossFile.pdf" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Embossing content to download. |  |
| 400 | Bad Request | `application/json`: object |

##### Response 400

400 Example `example-bad-request`:

```json
{
  "message": "X-tenant, configid, and filename are required",
  "error": "bad_request",
  "status": 400
}
```


#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `cards-embossing-1` | https://developers.pismo.io/events/docs/cards-embossing-1 |
| `cards-embossing-summary-1` | https://developers.pismo.io/events/docs/cards-embossing-summary-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400`, has examples `True`, emits events `2`, deprecated `False`.

Guides that link to this operation: `KU-CARD-physical-card-embossing`.

<!-- op: spec=api-specs/Card_issuing_-_Cards.yaml method=GET path=/embossing/v1/configurations/info operationId=get-embossing-configurations-info -->
### `GET /embossing/v1/configurations/info` — Get org embosser info

- **operationId:** `get-embossing-configurations-info`
- **Specification:** `api-specs/Card_issuing_-_Cards.yaml` (Card issuing - Cards)
- **Server base URL(s):** `https://sandbox.pismolabs.io`, `https://gw-pci.pismolabs.io`
- **Tags:** `Embossing data`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Get detailed information about an organization's embossing configurations.
>
> The organization/tenant ID is derived from the access token.
>
> For more information about embossing, refer to the [Physical card embossing](doc:physical-card-embossing) guide.
>
> For detailed information about embossing flows, refer to [Embossing flows](doc:physical-card-embossing#embossing-flows).
>
> **Notes:** 
>
>  * This endpoint requires an account token - an access token encoded with a Pismo account ID. 
>
>  * This is a PCI endpoint, use the https://gw-pci.pismolabs.io environment.

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Embosser objects. | `application/json`: object |
| 404 | Not Found | `application/json`: object |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `configurations` | array of object (schema `EmbosserObject`) | no |  |  |

200 Example `example`:

```json
{
  "configurations": [
    {
      "config_id": "6dacfdde-64bd-4a17-bbdf-3be627b271e6",
      "config_name": "name-1",
      "embosser_name": "Embosser-1",
      "programs": [
        1226,
        1225
      ],
      "type": "nominal",
      "enable": true
    },
    {
      "config_id": "6dacfdde-64bd-4a17-bbdf-3be627b271e6",
      "config_name": "name-2",
      "embosser_name": "Embosser-2",
      "programs": [
        1226,
        1225
      ],
      "type": "nominal",
      "enable": true
    }
  ]
}
```

##### Response 404

404 Example `example-not-found`:

```json
{
  "message": "not found configurations to org",
  "error": "not_found",
  "status": 404
}
```


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;404`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-CARD-physical-card-embossing`.

<!-- op: spec=api-specs/Card_issuing_-_Cards.yaml method=GET path=/embossing/v1/cards/{cardId}/history operationId=get-embossing-history -->
### `GET /embossing/v1/cards/{cardId}/history` — Get card embossing history

- **operationId:** `get-embossing-history`
- **Specification:** `api-specs/Card_issuing_-_Cards.yaml` (Card issuing - Cards)
- **Server base URL(s):** `https://sandbox.pismolabs.io`, `https://gw-pci.pismolabs.io`
- **Tags:** `Embossing data`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Retrieve a card's embossing history information.
>
>  **Notes:** 
>
>  * This endpoint requires an account token - an access token encoded with a Pismo account ID. 
>
>  * This is a PCI endpoint, use the https://gw-pci.pismolabs.io environment.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `cardId` | path | yes | string | Pismo card ID | example: "12345" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Embossing history response | `application/json`: array of object (schema `EmbossingHistoryResponse`) |
| 204 | No content - card has no embossing history |  |
| 400 | Bad Request | `application/json`: object |
| 401 | Access token is missing or invalid |  |
| 404 | Not Found | `application/json`: object |
| 500 | Internal server error |  |

##### Response 200

**200 `application/json` body fields:**

_No fields declared in the schema._

##### Response 400

400 Example `example-bad-request`:

```json
{
  "message": "The param cardId is invalid",
  "error": "bad_request",
  "status": 400,
  "error_code": ""
}
```

##### Response 404

404 Example `example-not-found`:

```json
{
  "message": "card not found",
  "error": "not_found",
  "status": 404,
  "error_code": ""
}
```


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;204;400;401;404;500`, has examples `True`, emits events `0`, deprecated `False`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/EmbosserFileInfo -->
### Schema `EmbosserFileInfo`

Pointer: `#/components/schemas/EmbosserFileInfo`. Type: object (schema `EmbosserFileInfo`).

> Embossing files info object

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `org_id` | string (schema `OrgID`) | no | Organization/tenant ID | example: "TN-f878e4a1-2879-48ba-be16-821e73ac98db" |
| `file_id` | string | no | File ID | example: "6dacfdde-64bd-4a17-bbdf-3be627b271e6" |
| `file_name` | string (schema `EmbossingFileName`) | no | Embossing file name | example: "EMBOSSERFILE.pgp" |
| `config_id` | string (schema `ConfigID`) | no | Embosser configuration/group ID. <br><br>You can call [Get nominal card embossing info](https://developers.pismo.io/pismo-docs/reference/get-embossing-info)  to get a card's embossing group.<br><br>You can also call [Get org embosser info](https://developers.pismo.io/pismo-docs/reference/get-embossing-configurations-info) to get an embossing group's configuration ID. <br> | format: "uuid"; example: "acde070d-8c4c-4f0d-9d8a-162843c10333" |
| `program_id` | integer (schema `ProgramID`) | no | Pismo program ID | example: 7654 |
| `generation_date` | string | no | File generation date, format = yyyy-mm-ddThh:mm:ssZ | example: "2022-08-24T20:13:24Z" |
| `total_embossed_cards` | integer | no | Total number of embossed cards | example: 1000 |
| `total_unembossed_cards` | integer | no | Total number of cards that did not get embossed | example: 20 |

<!-- schema: #/components/schemas/EmbosserObject -->
### Schema `EmbosserObject`

Pointer: `#/components/schemas/EmbosserObject`. Type: object (schema `EmbosserObject`).

> Embosser object

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `config_id` | string (schema `ConfigID`) | no | Embosser configuration/group ID. <br><br>You can call [Get nominal card embossing info](https://developers.pismo.io/pismo-docs/reference/get-embossing-info)  to get a card's embossing group.<br><br>You can also call [Get org embosser info](https://developers.pismo.io/pismo-docs/reference/get-embossing-configurations-info) to get an embossing group's configuration ID. <br> | format: "uuid"; example: "acde070d-8c4c-4f0d-9d8a-162843c10333" |
| `config_name` | string | no | Configuration name | example: "Config-1" |
| `embosser_name` | string | no | Embosser name | example: "Embosser-1" |
| `programs` | array of integer | no | Program IDs |  |
| `type` | string | no | Type - `nominal` or `noname` | enum: ["noname", "nominal"]; example: "nominal" |
| `enable` | boolean | no | Is this configuration enabled? | example: true |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Card_issuing_-_Cards.yaml` | tag `Embossing data`: GET /embossing/v1/cards/{cardId}, GET /embossing/v1/cards/noname/{cardId}, GET /embossing/v1/file-info, GET /embossing/v1/download-file, GET /embossing/v1/configurations/info, GET /embossing/v1/cards/{cardId}/history | https://github.com/PismoDevEx/pismo-api-specs | `687df76f123e41a7…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-CARD-physical-card-embossing` — Physical card embossing
- `KU-EVT-catalogue-cards` — Event catalogue: cards
