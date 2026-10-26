---
ku_id: KU-API-seller-management-marketplace--marketplace
title: 'API reference: Seller management - Marketplace — Marketplace'
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
- GetMarketPlaceByIdV2
- GetMarketplacesV1
related_kus:
- KU-SELL-managing-merchant-transactions
specification_version: 1.0.0
---

# API reference: Seller management - Marketplace — Marketplace

**KU ID:** `KU-API-seller-management-marketplace--marketplace` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 2 operation(s) tagged `Marketplace` in `api-specs/Seller_management_-_Marketplace.yaml` (“Seller management - Marketplace”, version `1.0.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Endpoints for marketplaces and operations including split transaction scheduler

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `GET /v2/marketplaces/{marketplaceId}` | `GetMarketPlaceByIdV2` | Get marketplace V2 (deprecated) | **yes** |
| `GET /v1/marketplaces` | `GetMarketplacesV1` | List marketplaces V1 (deprecated) | **yes** |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"}

## Operation contracts

<!-- op: spec=api-specs/Seller_management_-_Marketplace.yaml method=GET path=/v2/marketplaces/{marketplaceId} operationId=GetMarketPlaceByIdV2 -->
### `GET /v2/marketplaces/{marketplaceId}` — Get marketplace V2 (deprecated)

- **operationId:** `GetMarketPlaceByIdV2`
- **Specification:** `api-specs/Seller_management_-_Marketplace.yaml` (Seller management - Marketplace)
- **Server base URL(s):** `https://sandbox.pismolabs.io/marketplace`
- **Tags:** `Marketplace`
- **Deprecated in specification:** **yes**
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Get marketplace given its ID in the path. This endpoint is **deprecated**. It is replaced by [Get marketplace](https://developers.pismo.io/pismo-docs/reference/getmarketplacebyid).

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `marketplaceId` | path | yes | integer | Marketplace ID | format: "int64"; example: 1 |
| `Content-Type` | header | no | string | Content type | example: "application/json" |
| `Authorization` | header | no | string | Authorization token. This is a regular access token, which does not need to include an account ID. | example: "Bearer 1JI12J39182H39182JDIOAWJ%=" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `GETMarketplaceResponseV2`) |
| 400 | Bad Request |  |
| 401 | Access token is missing or invalid |  |
| 500 | Internal server error |  |
| 502 | Bad gateway (unexpected internal error) |  |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `address` | object (schema `MarketplaceAddress`) | no |  |  |
| `brand_name` | string (schema `MarketplaceBrandName`) | no | Marketplace brand name. A secondary name for the marketplace that is <b>not</b> the legal registered name.<br> | minLength: 1; maxLength: 50; example: "Acme" |
| `contact` | object (schema `ContactObject`) | no |  |  |
| `document_number` | string (schema `DocumentNumber`) | no | Marketplace document number. This is the government document code, such as a government-issued tax ID | minLength: 1; maxLength: 14; example: "20166135000139" |
| `external_id` | string (schema `ExternalMarketplaceID`) | no | Marketplace ID used on client's system | minLength: 1; maxLength: 50; example: "1123" |
| `id` | integer (schema `MarketplaceID`) | no | Marketplace ID<br> | format: "int64"; example: 20 |
| `marketplace_name` | string (schema `MarketplaceName`) | no | Registered, legal marketplace name. | minLength: 1; maxLength: 100; example: "Acme Products, LLC" |
| `registration` | string (schema `Registration`) | no | Municipal registration number. In some countries the municipal registration is called a business license. | minLength: 1; maxLength: 15; example: "123.456.789" |
| `registration2` | string (schema `Registration2`) | no | Additional municipal registration number. In some countries, two munipal registration numbers are required — one for the country and another for the state. | minLength: 1; maxLength: 15; example: "123.456.790" |
| `schedule_id` | integer (schema `ScheduleID`) | no | Schedule ID for marketplace | format: "int64"; example: 9 |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;500;502`, has examples `False`, emits events `0`, deprecated `True`.

Guides that link to this operation: `KU-SELL-managing-merchant-transactions`.

<!-- op: spec=api-specs/Seller_management_-_Marketplace.yaml method=GET path=/v1/marketplaces operationId=GetMarketplacesV1 -->
### `GET /v1/marketplaces` — List marketplaces V1 (deprecated)

- **operationId:** `GetMarketplacesV1`
- **Specification:** `api-specs/Seller_management_-_Marketplace.yaml` (Seller management - Marketplace)
- **Server base URL(s):** `https://sandbox.pismolabs.io/marketplace`
- **Tags:** `Marketplace`
- **Deprecated in specification:** **yes**
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> List marketplaces using query parameters. This endpoint is **deprecated**. It is replaced by [List marketplaces](https://developers.pismo.io/pismo-docs/reference/getmarketplaces).

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `merchant` | query | no | number | Merchant ID. List all the marketplaces the merchant belongs to. | format: "int64"; example: 54 |
| `search` | query | no | string | If a value is provided for this field, the Pismo platform searches for that value in the `document_number`, `registration`, `brand_name`, and `marketplace_name` fields of the marketplace records. It also searches for it in the `name` and `email` fields of the `contact` object for each record.<br><br>For example, if the value provided is "acme", and a marketplace has `marketplace_name` = "The Acme Market", that record is returned. If another record has "acme" in the `email` field in it's `contact` object, that record is also returned.<br> | example: "acme" |
| `page` | query | no | number | Current page number | format: "int64"; example: 2 |
| `perPage` | query | no | number | Number of items per page | format: "int64"; example: 10 |
| `Authorization` | header | no | string | Authorization token. This is a regular access token, which does not need to include an account ID. | example: "Bearer 1JI12J39182H39182JDIOAWJ%=" |
| `Content-Type` | header | no | string | Content type | example: "application/json" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `GETMarketplacesResponse`) |
| 400 | Bad Request |  |
| 401 | Access token is missing or invalid |  |
| 500 | Internal server error |  |
| 502 | Bad gateway (unexpected internal error) |  |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `pages` | integer (schema `TotalPages`) | no | Total number of pages | format: "int32"; example: 2 |
| `per_page` | integer (schema `PerPage`) | no | Number of result items per page | default: 10; format: "int32"; example: 50 |
| `total_items` | integer (schema `TotalItems`) | no | Total number of items | format: "int32"; example: 24 |
| `current_page` | integer (schema `CurrentPage`) | no | Current page number | default: 1; format: "int32"; example: 2 |
| `items` | array of object | no | Found marketplaces |  |
| `items[].id` | integer (schema `MarketplaceID`) | no | Marketplace ID<br> | format: "int64"; example: 20 |
| `items[].name` | string (schema `MarketplaceName`) | no | Registered, legal marketplace name. | minLength: 1; maxLength: 100; example: "Acme Products, LLC" |
| `items[].brand_name` | string (schema `MarketplaceBrandName`) | no | Marketplace brand name. A secondary name for the marketplace that is <b>not</b> the legal registered name.<br> | minLength: 1; maxLength: 50; example: "Acme" |
| `items[].document_number` | string (schema `DocumentNumber`) | no | Marketplace document number. This is the government document code, such as a government-issued tax ID | minLength: 1; maxLength: 14; example: "20166135000139" |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;500;502`, has examples `False`, emits events `0`, deprecated `True`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/MarketplaceAddress -->
### Schema `MarketplaceAddress`

Pointer: `#/components/schemas/MarketplaceAddress`. Type: object (schema `MarketplaceAddress`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `number` | integer (schema `StreetNumber`) | no | Numerical identifier for the specific location within a street or avenue | format: "int32"; minimum: 0; maximum: 2147483647; example: 22 |
| `street` | string (schema `Street`) | no | Name of the street, avenue, or primary thoroughfare of the address | minLength: 1; maxLength: 80; example: "Maple Avenue" |
| `complementary_address` | string (schema `ComplementaryAddress`) | no | Additional address details that help pinpoint the exact location, such as building, apartment, or floor | minLength: 1; maxLength: 50; example: "Suite 2" |
| `neighborhood` | string (schema `Neighborhood`) | no | Name of the neighborhood or administrative region where the address is located | minLength: 1; maxLength: 50; example: "West End" |
| `city` | string (schema `City`) | no | Name of the city or municipality | minLength: 1; maxLength: 60; example: "San Diego" |
| `state` | string (schema `State`) | no | Abbreviation or full name of the state, province, or administrative division | minLength: 2; maxLength: 2; example: "CA" |
| `zip_code` | string (schema `ZipCode`) | no | Postal code. This is called a zip code in the United States, but you can use other types of postal codes. | minLength: 1; maxLength: 9; example: "91941" |
| `country` | string (schema `Country`) | no | Full name of the country according to international standards or local registry | minLength: 1; maxLength: 30; example: "United States" |

<!-- schema: #/components/schemas/ContactObject -->
### Schema `ContactObject`

Pointer: `#/components/schemas/ContactObject`. Type: object (schema `ContactObject`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `email` | string (schema `EmailAddress`) | yes | Marketplace contact e-mail address. Its format must be a valid email address | minLength: 1; maxLength: 255; example: "email@email.com" |
| `name` | string | no | Contact name | minLength: 1; maxLength: 50; example: "John Doe" |
| `phone_number` | string (schema `PhoneNumber`) | no | Phone number. Dashes and parentheses are optional. | minLength: 1; maxLength: 25; example: "5558739452" |
| `additional_phone_number` | string (schema `AdditionalPhoneNumber`) | no | Additional phone number. Dashes and parentheses are optional. | minLength: 1; maxLength: 25; example: "5558739453" |

## Lifecycle status

- `GET /v2/marketplaces/{marketplaceId}` (`GetMarketPlaceByIdV2`) is marked `deprecated: true` in the specification.
- `GET /v1/marketplaces` (`GetMarketplacesV1`) is marked `deprecated: true` in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Seller_management_-_Marketplace.yaml` | tag `Marketplace`: GET /v2/marketplaces/{marketplaceId}, GET /v1/marketplaces | https://github.com/PismoDevEx/pismo-api-specs | `8ffe617b35e772cc…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-SELL-managing-merchant-transactions` — Managing merchant transactions
