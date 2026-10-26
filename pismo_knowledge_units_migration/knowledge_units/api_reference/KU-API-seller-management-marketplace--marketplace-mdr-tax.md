---
ku_id: KU-API-seller-management-marketplace--marketplace-mdr-tax
title: 'API reference: Seller management - Marketplace — Marketplace MDR tax'
category: api_reference
ku_type: api_reference
lifecycle: current
sources:
- path: api-specs/Seller_management_-_Marketplace.yaml
  sha256: 8ffe617b35e772cca857f195c1384b6d7287d6e8bcbf553ed99c3eed14924d2b
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
- GetMdrTaxByIdV1
- PostMdrTaxV1
- DeleteMdrTaxV1
related_kus: []
specification_version: 1.0.0
---

# API reference: Seller management - Marketplace — Marketplace MDR tax

**KU ID:** `KU-API-seller-management-marketplace--marketplace-mdr-tax` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 3 operation(s) tagged `Marketplace MDR tax` in `api-specs/Seller_management_-_Marketplace.yaml` (“Seller management - Marketplace”, version `1.0.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Endpoints for Merchant Discount Rate (MDR) tax

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `GET /v1/marketplaces/{marketplaceId}/mdrtax` | `GetMdrTaxByIdV1` | Get MDR tax information | no |
| `POST /v1/marketplaces/{marketplaceId}/mdrtax` | `PostMdrTaxV1` | Create MDR tax information | no |
| `DELETE /v1/marketplaces/{marketplaceId}/mdrtax` | `DeleteMdrTaxV1` | Delete MDR tax information | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"}

## Operation contracts

<!-- op: spec=api-specs/Seller_management_-_Marketplace.yaml method=GET path=/v1/marketplaces/{marketplaceId}/mdrtax operationId=GetMdrTaxByIdV1 -->
### `GET /v1/marketplaces/{marketplaceId}/mdrtax` — Get MDR tax information

- **operationId:** `GetMdrTaxByIdV1`
- **Specification:** `api-specs/Seller_management_-_Marketplace.yaml` (Seller management - Marketplace)
- **Server base URL(s):** `https://sandbox.pismolabs.io/marketplace`
- **Tags:** `Marketplace MDR tax`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Get Merchant Discount Rate (MDR) tax information using marketplace ID.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `marketplaceId` | path | yes | integer | Marketplace ID | format: "int64"; example: 1 |
| `Authorization` | header | no | string | Authorization token. This is a regular access token, which does not need to include an account ID. | example: "Bearer 1JI12J39182H39182JDIOAWJ%=" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `GETMDRTaxResponse`) |
| 400 | Bad Request |  |
| 401 | Access token is missing or invalid |  |
| 500 | Internal server error |  |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `items` | array of object | no | Merchant Discount Rate (MDR) tax List |  |
| `items[].fixed_tax` | number (schema `FixedTax`) | no | Fixed tax | format: "float"; example: 1.5 |
| `items[].maximum_transaction_amount` | number (schema `MaximumTransactionAmount`) | no | Maximum transaction amount | format: "float"; example: 1.5 |
| `items[].minimum_transaction_amount` | number (schema `MinimumTransactionAmount`) | no | Minimum transaction amount | format: "float"; example: 1.5 |
| `items[].percentage_tax` | number (schema `PercentageTax`) | no | Tax rate (percentage) | format: "float"; example: 0.05 |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;500`, has examples `False`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Seller_management_-_Marketplace.yaml method=POST path=/v1/marketplaces/{marketplaceId}/mdrtax operationId=PostMdrTaxV1 -->
### `POST /v1/marketplaces/{marketplaceId}/mdrtax` — Create MDR tax information

- **operationId:** `PostMdrTaxV1`
- **Specification:** `api-specs/Seller_management_-_Marketplace.yaml` (Seller management - Marketplace)
- **Server base URL(s):** `https://sandbox.pismolabs.io/marketplace`
- **Tags:** `Marketplace MDR tax`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Store information about Merchant Discount Rate (MDR) tax using marketplace ID. The MDR is the rate charged to a merchant for payment processing services on debit and credit card transactions. The merchant must set up this service and agree to the rate before accepting debit and credit cards as payment.
>
> For information about MDR, refer to the <a href="https://www.investopedia.com/terms/m/merchant-discount-rate.asp" target="_blank">Merchant Discount Rate</a>.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `marketplaceId` | path | yes | integer | Marketplace ID | format: "int64"; example: 1 |
| `Authorization` | header | no | string | Authorization token. This is a regular access token, which does not need to include an account ID. | example: "Bearer 1JI12J39182H39182JDIOAWJ%=" |
| `Content-Type` | header | no | string | Content type | example: "application/json" |

#### Request body

Required: yes

> Request body

**Content type `application/json`** — schema: object (schema `POSTMDRTaxRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `ranges` | array of object | no |  |  |
| `ranges[].fixed_tax` | number (schema `FixedTax`) | no | Fixed tax | format: "float"; example: 1.5 |
| `ranges[].maximum_transaction_amount` | number (schema `MaximumTransactionAmount`) | no | Maximum transaction amount | format: "float"; example: 1.5 |
| `ranges[].minimum_transaction_amount` | number (schema `MinimumTransactionAmount`) | no | Minimum transaction amount | format: "float"; example: 1.5 |
| `ranges[].percentage_tax` | number (schema `PercentageTax`) | no | Tax rate (percentage) | format: "float"; example: 0.05 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object |
| 400 | Bad Request |  |
| 401 | Access token is missing or invalid |  |
| 500 | Internal server error |  |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `success` | boolean | no | Indicates whether the MDR tax information was successfully stored. | example: true |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;500`, has examples `True`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Seller_management_-_Marketplace.yaml method=DELETE path=/v1/marketplaces/{marketplaceId}/mdrtax operationId=DeleteMdrTaxV1 -->
### `DELETE /v1/marketplaces/{marketplaceId}/mdrtax` — Delete MDR tax information

- **operationId:** `DeleteMdrTaxV1`
- **Specification:** `api-specs/Seller_management_-_Marketplace.yaml` (Seller management - Marketplace)
- **Server base URL(s):** `https://sandbox.pismolabs.io/marketplace`
- **Tags:** `Marketplace MDR tax`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Delete Merchant Discount Rate (MDR) tax information using marketplace ID.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `marketplaceId` | path | yes | integer | Marketplace ID | format: "int64"; example: 1 |
| `Authorization` | header | no | string | Authorization token. This is a regular access token, which does not need to include an account ID. | example: "Bearer 1JI12J39182H39182JDIOAWJ%=" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object |
| 400 | Bad Request |  |
| 401 | Access token is missing or invalid |  |
| 500 | Internal server error |  |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `success` | boolean | no | Indicates whether MDR tax information was successfully deleted. | example: true |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;500`, has examples `True`, emits events `0`, deprecated `False`.

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
| `api-specs/Seller_management_-_Marketplace.yaml` | tag `Marketplace MDR tax`: GET /v1/marketplaces/{marketplaceId}/mdrtax, POST /v1/marketplaces/{marketplaceId}/mdrtax, DELETE /v1/marketplaces/{marketplaceId}/mdrtax | https://github.com/PismoDevEx/pismo-api-specs | `8ffe617b35e772cc…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- None.
