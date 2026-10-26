---
ku_id: KU-API-banking-assets--quotas
title: 'API reference: Banking - Assets — Quotas'
category: api_reference
ku_type: api_reference
lifecycle: current
sources:
- path: api-specs/Banking_-_Assets.yaml
  sha256: 4571af460975f34c49953e1f6b989175441ee84e84142cca7450503fba10458b
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
- UpdateQuota
- AssetQuotas
related_kus:
- KU-EVT-assets-data-events
- KU-EVT-catalogue-assets
specification_version: 1.0.0
---

# API reference: Banking - Assets — Quotas

**KU ID:** `KU-API-banking-assets--quotas` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 2 operation(s) tagged `Quotas` in `api-specs/Banking_-_Assets.yaml` (“Banking - Assets”, version `1.0.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Quota endpoints

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `PATCH /v1/issuer/{issuer_id}/assets/{asset_id}/quotas/{quota_id}` | `UpdateQuota` | Update quota | no |
| `GET /v1/issuer/{issuer_id}/assets/{asset_id}/quotas` | `AssetQuotas` | List asset quotas | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"}

## Operation contracts

<!-- op: spec=api-specs/Banking_-_Assets.yaml method=PATCH path=/v1/issuer/{issuer_id}/assets/{asset_id}/quotas/{quota_id} operationId=UpdateQuota -->
### `PATCH /v1/issuer/{issuer_id}/assets/{asset_id}/quotas/{quota_id}` — Update quota

- **operationId:** `UpdateQuota`
- **Specification:** `api-specs/Banking_-_Assets.yaml` (Banking - Assets)
- **Server base URL(s):** `https://sandbox.pismolabs.io/assets-accrual`, `https://sandbox.pismolabs.io/assets-accrual`, `https://api.pismolabs.io/assets-accrual`
- **Tags:** `Quotas`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Updates a quota by its ID.
>
> A quota is the number of asset shares. One asset can consist of a single share or multiple shares. 
>
> You can get quota IDs with the <a href="https://developers.pismo.io/pismo-docs/reference/assetquotas" target="_blank">List asset quotas</a> endpoint.
>
> This endpoint generates a [Quota updated](https://developers.pismo.io/events/docs/assets-quota-update-1) event.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `x-cid` | header | no | string | The Correlation IDentifier field is used to link related API requests and events.  The x-cid can help the Pismo engineering team track everything related to a call. You can find the x-cid field in the response header from an API endpoint call.<br><br>If this field isn't passed, one is automatically generated.<br> | example: "5bb05174-4e80-11ea-b77f-2e728ce88125" |
| `issuer_id` | path | yes | string | Issuer ID. For more information, refer to [issuer identification number](https://www.investopedia.com/terms/i/issuer-identification-number-iin.asp) | example: "24" |
| `asset_id` | path | yes | string | Client assigned asset ID. Must consist of the characters [a-z,A-Z,0-9,-,:] with a range from 1 to 128.<br> | example: "2345" |
| `quota_id` | path | yes | string | Quota ID | example: "3456" |

#### Request body

Required: yes

> Request body

**Content type `application/json`** — schema: object (schema `UpdateQuota`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `operation_type` | string (schema `OperationType`) | yes | Quota operation type. Must be `amendment` (update quota). | enum: ["amendment"] |
| `purchased_units` | integer (schema `PurchasedUnits`) | no | Number of purchased units | format: "int32"; example: 20 |
| `customer_name` | string (schema `CustomerName`) | no | Customer name - max length is 128 chars | minLength: 1; maxLength: 128; example: "Bud Whyser" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `UpdateQuotaResponse`) |
| 400 | Bad Request |  |
| 401 | Unauthorized |  |
| 404 | Not found |  |
| 500 | Internal server error |  |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `asset_id` | string (schema `AssetID`) | no | Asset ID. This ID is client-generated. It must be between 1 and 128 characters long and consist of only the characters [a-z,A-Z,0-9,-,:]. | minLength: 1; maxLength: 128; example: "6ea8094b-73ba-4737-93ad-370c27c54813" |
| `quota_id` | string (schema `QuotaID`) | no | Quota ID | example: "c2d581cb-5c9c-40ab-8783-724feb372132" |
| `issuer_id` | string (schema `IssuerID`) | no | Issuer ID. For more information, see [issuer identification number](https://www.investopedia.com/terms/i/issuer-identification-number-iin.asp)<br> | example: "98400-0-0d" |
| `units` | integer (schema `Units`) | no | Number of asset units | format: "int32"; example: 20 |
| `created_at` | string (schema `CreatedAt`) | no | Date/time (UTC) asset registered on Pismo platform | example: "2023-03-30T12:26:41" |
| `customer_type` | string (schema `CustomerType`) | no | Customer type - `natural` or `legal`. A `natural` customer is an individual, a `legal` customer is a corporation or other legal entitiy type. | enum: ["natural", "legal"]; example: "natural" |
| `document_number` | string (schema `DocumentNumber`) | no | A government document number, such as a social security number (US). Must be numeric with 11-14 digits.<br> | minLength: 1; maxLength: 14; example: "123412341234" |
| `customer_name` | string (schema `CustomerName`) | no | Customer name - max length is 128 chars | minLength: 1; maxLength: 128; example: "Bud Whyser" |
| `deposit_number` | string (schema `DocumentNumber`) | no | A government document number, such as a social security number (US). Must be numeric with 11-14 digits.<br> | minLength: 1; maxLength: 14; example: "123412341234" |


#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `assets-quota-update-1` | https://developers.pismo.io/events/docs/assets-quota-update-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;404;500`, has examples `False`, emits events `1`, deprecated `False`.

Guides that link to this operation: `KU-EVT-assets-data-events`.

<!-- op: spec=api-specs/Banking_-_Assets.yaml method=GET path=/v1/issuer/{issuer_id}/assets/{asset_id}/quotas operationId=AssetQuotas -->
### `GET /v1/issuer/{issuer_id}/assets/{asset_id}/quotas` — List asset quotas

- **operationId:** `AssetQuotas`
- **Specification:** `api-specs/Banking_-_Assets.yaml` (Banking - Assets)
- **Server base URL(s):** `https://sandbox.pismolabs.io/assets-accrual`, `https://sandbox.pismolabs.io/assets-accrual`, `https://api.pismolabs.io/assets-accrual`
- **Tags:** `Quotas`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Retrieves asset quotas by asset ID. 
> A quota is the number of asset shares. One asset can consist of a single share or multiple shares. 

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `x-cid` | header | no | string | The Correlation IDentifier field is used to link related API requests and events.  The x-cid can help the Pismo engineering team track everything related to a call. You can find the x-cid field in the response header from an API endpoint call.<br><br>If this field isn't passed, one is automatically generated.<br> | example: "5bb05174-4e80-11ea-b77f-2e728ce88125" |
| `issuer_id` | path | yes | string | Issuer ID. For more information, refer to [issuer identification number](https://www.investopedia.com/terms/i/issuer-identification-number-iin.asp) | example: "24" |
| `page` | query | yes | integer | Page number, default is 1. | format: "int32"; example: 1 |
| `perPage` | query | yes | integer | Number of items per page, default is 10. | format: "int32"; example: 10 |
| `asset_id` | path | yes | string | Client assigned asset ID. Must consist of the characters [a-z,A-Z,0-9,-,:] with a range from 1 to 128.<br> | example: "2345" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `AssetQuotasResponse`) |
| 400 | Bad Request |  |
| 401 | Unauthorized |  |
| 404 | Not found |  |
| 500 | Internal server error |  |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `current_page` | number (schema `CurrentPage`) | no | Current page | example: 1 |
| `per_page` | integer (schema `PerPage`) | no | Number of items per page, default is 10. | format: "Int32"; example: 1 |
| `pages` | integer (schema `Pages`) | no | Total number of pages, default is 1. | format: "Int32"; example: 1 |
| `total_items` | number (schema `TotalItems`) | no | Total number of items | example: 1 |
| `items` | array of object | no |  |  |
| `items[].asset_id` | string (schema `AssetID`) | no | Asset ID. This ID is client-generated. It must be between 1 and 128 characters long and consist of only the characters [a-z,A-Z,0-9,-,:]. | minLength: 1; maxLength: 128; example: "6ea8094b-73ba-4737-93ad-370c27c54813" |
| `items[].quota_id` | string (schema `QuotaID`) | no | Quota ID | example: "c2d581cb-5c9c-40ab-8783-724feb372132" |
| `items[].issuer_id` | string (schema `IssuerID`) | no | Issuer ID. For more information, see [issuer identification number](https://www.investopedia.com/terms/i/issuer-identification-number-iin.asp)<br> | example: "98400-0-0d" |
| `items[].units` | integer (schema `Units`) | no | Number of asset units | format: "int32"; example: 20 |
| `items[].redeemed_units` | number (schema `RedeemedUnits`) | no | Number of redeemed units | example: 10 |
| `items[].created_at` | string (schema `CreatedAt`) | no | Date/time (UTC) asset registered on Pismo platform | example: "2023-03-30T12:26:41" |
| `items[].customer_type` | string (schema `CustomerType`) | no | Customer type - `natural` or `legal`. A `natural` customer is an individual, a `legal` customer is a corporation or other legal entitiy type. | enum: ["natural", "legal"]; example: "natural" |
| `items[].document_number` | string (schema `DocumentNumber`) | no | A government document number, such as a social security number (US). Must be numeric with 11-14 digits.<br> | minLength: 1; maxLength: 14; example: "123412341234" |
| `items[].deposit_number` | integer (schema `DepositNumber`) | no | Deposit number | format: "int32"; example: 567339022 |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;404;500`, has examples `False`, emits events `0`, deprecated `False`.

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
| `api-specs/Banking_-_Assets.yaml` | tag `Quotas`: PATCH /v1/issuer/{issuer_id}/assets/{asset_id}/quotas/{quota_id}, GET /v1/issuer/{issuer_id}/assets/{asset_id}/quotas | https://github.com/PismoDevEx/pismo-api-specs | `4571af460975f34c…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-EVT-assets-data-events` — Banking - Assets
- `KU-EVT-catalogue-assets` — Event catalogue: assets
