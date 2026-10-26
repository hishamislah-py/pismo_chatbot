---
ku_id: KU-API-seller-management-sellers--marketplace
title: 'API reference: Seller management - Sellers — Marketplace'
category: api_reference
ku_type: api_reference
lifecycle: current
sources:
- path: api-specs/Seller_management_-_Sellers.yaml
  sha256: eb5d18c21f5848fe7db87917b88dfe2d23206e9b68f8382dc8c41745d518c00d
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
- getMarketplaces
- createMarketplace
- getMarketplaceById
- updateMarketplace
related_kus:
- KU-ERR-codes-esmg-to-whis
- KU-EVT-catalogue-marketplace
specification_version: 1.0.0
---

# API reference: Seller management - Sellers — Marketplace

**KU ID:** `KU-API-seller-management-sellers--marketplace` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 4 operation(s) tagged `Marketplace` in `api-specs/Seller_management_-_Sellers.yaml` (“Seller management - Sellers”, version `1.0.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Endpoints for marketplace management

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `GET /v3/marketplaces` | `getMarketplaces` | List marketplaces | no |
| `POST /v3/marketplaces` | `createMarketplace` | Create marketplace V3 | no |
| `GET /v3/marketplaces/{marketplaceId}` | `getMarketplaceById` | Get marketplace by ID | no |
| `PATCH /v1/marketplaces/{marketplaceId}` | `updateMarketplace` | Update marketplace | no |

## Operation contracts

<!-- op: spec=api-specs/Seller_management_-_Sellers.yaml method=GET path=/v3/marketplaces operationId=getMarketplaces -->
### `GET /v3/marketplaces` — List marketplaces

- **operationId:** `getMarketplaces`
- **Specification:** `api-specs/Seller_management_-_Sellers.yaml` (Seller management - Sellers)
- **Server base URL(s):** `https://sandbox.pismolabs.io/sellers`
- **Tags:** `Marketplace`
- **Deprecated in specification:** no
- **Security requirement:** not declared

**Description (from the specification):**

> Retrieve a paginated list of marketplaces with optional filtering and sorting capabilities.
>
> ## Filtering
>
> Filters are provided as individual query parameters. Multiple filters can be combined — each additional parameter further restricts the result set (AND logic).
>
> | Parameter | Field Filtered | Match Type | Case Sensitive |
> |---|---|---|---|
> | `documentNumber` | `document_number` | Exact | Yes |
> | `externalId` | `external_id` | Exact | Yes |
> | `brandName` | `brand_name` | Partial (LIKE) | No |
> | `marketplaceName` | `marketplace_name` | Partial (LIKE) | No |
>
> **Examples:**
> - `?documentNumber=12345678901234` — exact document number match
> - `?brandName=Acme` — brand name containing "Acme"
> - `?brandName=Acme&marketplaceName=Store` — brand name containing "Acme" AND marketplace name containing "Store"
>
> ## Sorting
>
> Use `order` and `orderBy` to control result ordering.
> Supported `orderBy` values: `marketplace_id`, `document_number`, `brand_name`, `marketplace_name`, `external_id`.
> Default sort: `marketplace_id ASC`.
>
> ## Empty Results
>
> Empty result sets return **HTTP 200** with an empty `items` array (not 404).

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `page` | query | no | integer | Current page number | format: "int32"; minimum: 1; example: 1; example: 12 |
| `perPage` | query | no | integer | Number of items per page | format: "int32"; minimum: 1; example: 100 |
| `order` | query | no | string | Sort order direction (case-insensitive) | enum: ["asc", "desc"]; default: "asc"; example: "asc" |
| `orderBy` | query | no | string | Field name to sort by. Supported fields:<br>- `marketplace_id`<br>- `document_number`<br>- `brand_name`<br>- `marketplace_name`<br>- `external_id`<br> | maxLength: 50; example: "brand_name" |
| `documentNumber` | query | no | string | Filter by marketplace document number (exact match, case-sensitive) | minLength: 1; maxLength: 14; example: "12345678901234" |
| `externalId` | query | no | string | Filter by external system identifier (exact match, case-sensitive) | minLength: 1; maxLength: 50; example: "EXT-123" |
| `brandName` | query | no | string | Filter by brand name (partial match, case-insensitive) | minLength: 1; maxLength: 50; example: "Acme" |
| `marketplaceName` | query | no | string | Filter by marketplace name (partial match, case-insensitive) | minLength: 1; maxLength: 100; example: "Store" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK - Paginated list of marketplaces | `application/json`: object (schema `GetMarketplacesResponse`) |
| 400 | Bad request - Invalid query parameters | `application/json`: object (schema `ErrorRequestResponse`) |
| 401 | Unauthorized | `application/json`: object (schema `ErrorRequestResponse`) |
| 500 | Internal server error | `application/json`: object (schema `InternalServerErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `has_next` | boolean | yes | Is a next page available? | example: true |
| `items` | array of object (schema `MarketplaceListItem`) | yes | Array of marketplace objects. Returns empty array if no results found (HTTP 200, not 404) |  |
| `page` | integer | yes | Current page number (starts at 1) | format: "int32"; minimum: 1; example: 1 |
| `per_page` | integer | yes | Number of items per page | format: "int32"; minimum: 1; maximum: 100; example: 10 |

200 Example `marketplaces-list-success` (List marketplaces with pagination) — from `#/components/examples/GetMarketplacesResponseExample`:

```json
{
  "page": 1,
  "per_page": 10,
  "has_next": true,
  "items": [
    {
      "id": 123,
      "document_number": "12345678901234",
      "brand_name": "Acme Corporation",
      "marketplace_name": "Acme Store",
      "external_id": "EXT-123"
    },
    {
      "id": 124,
      "document_number": "98765432109876",
      "brand_name": "Beta Industries",
      "marketplace_name": "Beta Marketplace",
      "external_id": null
    }
  ]
}
```

200 Example `marketplaces-list-empty` (Empty list response (HTTP 200, not 404)) — from `#/components/examples/GetMarketplacesEmptyResponseExample`:

```json
{
  "page": 1,
  "per_page": 10,
  "has_next": false,
  "items": []
}
```

200 Example `marketplaces-list-filtered` (Filtered list combining brandName and marketplaceName) — from `#/components/examples/GetMarketplacesFilteredResponseExample`:

```json
{
  "page": 1,
  "per_page": 20,
  "has_next": false,
  "items": [
    {
      "id": 1,
      "document_number": "12345678901234",
      "brand_name": "Acme Corporation",
      "marketplace_name": "Acme Store",
      "external_id": "EXT-001"
    },
    {
      "id": 15,
      "document_number": "98765432109876",
      "brand_name": "Acme Industries",
      "marketplace_name": "Acme Marketplace",
      "external_id": null
    }
  ]
}
```

200 Example `marketplaces-list-last-page` (Last page where `has_next` is `false`) — from `#/components/examples/GetMarketplacesLastPageExample`:

```json
{
  "page": 5,
  "per_page": 10,
  "has_next": false,
  "items": [
    {
      "id": 200,
      "document_number": "11122233344455",
      "brand_name": "Last Marketplace",
      "marketplace_name": "Final Store",
      "external_id": "EXT-200"
    }
  ]
}
```

##### Response 400

400 Example `invalid-page` (Invalid page parameter error) — from `#/components/examples/GetMarketplacesInvalidPageExample`:

```json
{
  "code": "ESMG0900",
  "message": "Validation failed",
  "details": {
    "payload": [
      {
        "field": "page",
        "message": "Invalid page parameter: must be greater than 0"
      }
    ]
  }
}
```

400 Example `invalid-perPage` (Invalid perPage parameter error) — from `#/components/examples/GetMarketplacesInvalidPerPageExample`:

```json
{
  "code": "ESMG0900",
  "message": "Validation failed",
  "details": {
    "payload": [
      {
        "field": "perPage",
        "message": "Invalid perPage parameter: maximum value is 100"
      }
    ]
  }
}
```

400 Example `invalid-order` (Invalid order parameter error) — from `#/components/examples/GetMarketplacesInvalidOrderExample`:

```json
{
  "code": "ESMG0900",
  "message": "Validation failed",
  "details": {
    "payload": [
      {
        "field": "order",
        "message": "Invalid order parameter: must be 'asc' or 'desc'"
      }
    ]
  }
}
```

##### Response 401

401 Example `unauthorized` (Unauthorized error):

```json
{
  "code": "ESMG0401",
  "message": "Unauthorized",
  "details": {
    "payload": [
      {
        "field": "Authorization",
        "message": "Invalid or missing authorization token"
      }
    ]
  }
}
```

##### Response 500

500 Example `merchant-transactions-response-success` (Internal server error response) — from `#/components/examples/InternalServerErrorResponseExample`:

```json
{
  "message": "Internal Server Error"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `ESMG0900` | Validation failed |
| 401 | `ESMG0401` | Unauthorized |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;500`, has examples `True`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Seller_management_-_Sellers.yaml method=POST path=/v3/marketplaces operationId=createMarketplace -->
### `POST /v3/marketplaces` — Create marketplace V3

- **operationId:** `createMarketplace`
- **Specification:** `api-specs/Seller_management_-_Sellers.yaml` (Seller management - Sellers)
- **Server base URL(s):** `https://sandbox.pismolabs.io/sellers`
- **Tags:** `Marketplace`
- **Deprecated in specification:** no
- **Security requirement:** not declared

**Description (from the specification):**

> This endpoint creates a new marketplace.
> This endpoint generates a <a href="https://developers.pismo.io/events/docs/marketplace-marketplace-created-2">Marketplace created</a> event.

#### Request body

Required: no

**Content type `application/json`** — schema: object (schema `CreateMarketplaceRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `brand_name` | string (schema `BrandName`) | yes | Marketplace brand name. A secondary name for the marketplace that is **not** the legal registered name<br> | minLength: 1; maxLength: 50; example: "Acme" |
| `document_number` | string (schema `DocumentNumber`) | yes | Marketplace document number. This is the government document code, such as a government-issued tax ID | minLength: 1; maxLength: 14; example: "20166135000139" |
| `marketplace_name` | string (schema `MarketplaceName`) | yes | Registered, legal marketplace name | minLength: 1; maxLength: 100; example: "Acme Products, LLC" |
| `registration` | string (schema `Registration`) | no | Municipal registration number. In some countries the municipal registration is called a business license | minLength: 1; maxLength: 15; example: "123.456.789" |
| `registration2` | string (schema `Registration2`) | no | Additional municipal registration number. In some countries, two munipal registration numbers are required — one for the country and another for the state | minLength: 1; maxLength: 15; example: "123.456.790" |
| `external_id` | string (schema `ExternalId`) | no | Marketplace ID used on client's system | minLength: 1; maxLength: 50; example: "1123" |
| `address` | object | no | Marketplace address information |  |
| `address.number` | integer (schema `Number`) | no | Numerical identifier for the specific location within a street or avenue | format: "int32"; minimum: 0; maximum: 2147483647; example: 22 |
| `address.street` | string (schema `Street`) | no | Name of the street, avenue, or primary thoroughfare of the address | minLength: 1; maxLength: 80; example: "Maple Avenue" |
| `address.complementary_address` | string (schema `ComplementaryAddress`) | no | Additional address details that help pinpoint the exact location, such as building, apartment, or floor | minLength: 1; maxLength: 50; example: "Suite 2" |
| `address.neighborhood` | string (schema `Neighborhood`) | no | Name of the neighborhood or administrative region where the address is located | minLength: 1; maxLength: 50; example: "West End" |
| `address.zip_code` | string (schema `ZipCode`) | no | Postal code. This is called a zip code in the United States, but you can use other types of postal codes | minLength: 1; maxLength: 9; example: "91941" |
| `address.city` | string (schema `City`) | no | Name of the city or municipality | minLength: 1; maxLength: 60; example: "San Diego" |
| `address.state` | string (schema `State`) | no | Abbreviation or full name of the state, province, or administrative division | minLength: 2; maxLength: 2; example: "CA" |
| `address.country` | string (schema `Country`) | no | Full name of the country according to international standards or local registry | minLength: 1; maxLength: 30; example: "United States" |
| `contact` | object | no | Contact information |  |
| `contact.name` | string (schema `Name`) | no | Contact name for the marketplace | minLength: 1; maxLength: 50; example: "Jane Doe" |
| `contact.email` | string (schema `Email`) | no | Marketplace contact email address. Its format must be a valid email address | minLength: 1; maxLength: 255; example: "email@email.com" |
| `contact.phone_number` | string (schema `PhoneNumber`) | no | Phone number. Dashes and parentheses are optional | minLength: 1; maxLength: 25; example: "5558739452" |
| `contact.additional_phone_number` | string (schema `AdditionalPhoneNumber`) | no | Additional phone number. Dashes and parentheses are optional | minLength: 1; maxLength: 25; example: "5558739453" |

Example `marketplace-request-success` (Create marketplace payload) — from `#/components/examples/CreateMarketplaceRequestExample`:

```json
{
  "document_number": "99419954904000",
  "registration": "REG123456",
  "registration2": "REG654321",
  "brand_name": "Natalia",
  "marketplace_name": "Test Marketplace",
  "external_id": "EXT-40790",
  "address": {
    "street": "Main Street",
    "number": 100,
    "complementary_address": "Suite 10",
    "neighborhood": "Downtown",
    "zip_code": "22345-477",
    "city": "Test City",
    "state": "SP",
    "country": "BR"
  },
  "contact": {
    "name": "John Doe",
    "email": "alexmiller@example.com",
    "phone_number": "4155551234",
    "additional_phone_number": "4155555678"
  }
}
```

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | Create marketplace | `application/json`: object (schema `CreateMarketplaceResponse`) |
| 400 | Bad request | `application/json`: object (schema `ErrorRequestResponse`) |
| 500 | Internal server error | `application/json`: object (schema `InternalServerErrorResponse`) |

##### Response 201

**201 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | integer (schema `MarketplaceId`) | no | Marketplace ID | format: "int64"; minimum: 1; maximum: 18446744073709552000; example: 51148 |

201 Example `marketplace-response-success` (Create marketplace payload response) — from `#/components/examples/CreateMarketplaceResponseExample`:

```json
{
  "id": 99
}
```

##### Response 400

400 Example `merchant-transactions-response-success` (Bad request response) — from `#/components/examples/BadRequestResponse`:

```json
{
  "code": "ESMG0900",
  "message": "Failed during validation of request payload",
  "details": {
    "payload": [
      {
        "field": "field_name",
        "message": "validation message"
      }
    ]
  }
}
```

##### Response 500

500 Example `merchant-transactions-response-success` (Internal server error response) — from `#/components/examples/InternalServerErrorResponseExample`:

```json
{
  "message": "Internal Server Error"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `ESMG0900` | Failed during validation of request payload |

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `marketplace-marketplace-created-2` | https://developers.pismo.io/events/docs/marketplace-marketplace-created-2 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `201;400;500`, has examples `True`, emits events `1`, deprecated `False`.

<!-- op: spec=api-specs/Seller_management_-_Sellers.yaml method=GET path=/v3/marketplaces/{marketplaceId} operationId=getMarketplaceById -->
### `GET /v3/marketplaces/{marketplaceId}` — Get marketplace by ID

- **operationId:** `getMarketplaceById`
- **Specification:** `api-specs/Seller_management_-_Sellers.yaml` (Seller management - Sellers)
- **Server base URL(s):** `https://sandbox.pismolabs.io/sellers`
- **Tags:** `Marketplace`
- **Deprecated in specification:** no
- **Security requirement:** not declared

**Description (from the specification):**

> Retrieve marketplace information by its ID.
>
> Returns detailed information about a specific marketplace including its configuration, contact details, and address information.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `marketplaceId` | path | yes | integer | Marketplace ID | format: "int64"; minimum: 1; maximum: 18446744073709552000; example: 1654 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Ok | `application/json`: object (schema `GetMarketplaceByIdResponse`) |
| 400 | Bad request | `application/json`: object (schema `ErrorRequestResponse`) |
| 404 | Not found | `application/json`: object (schema `ErrorRequestResponse`) |
| 500 | Internal server error | `application/json`: object (schema `InternalServerErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | integer (schema `MarketplaceId`) | no | Marketplace ID | format: "int64"; minimum: 1; maximum: 18446744073709552000; example: 51148 |
| `document_number` | string | no | Marketplace document number | example: "12345678901234" |
| `brand_name` | string | no | Marketplace brand name | example: "Tech Store Brasil" |
| `marketplace_name` | string | no | Marketplace name | example: "TechStore Marketplace" |
| `registration` | string | no | Official company registration with the local municipality | minLength: 1; maxLength: 15 |
| `registration2` | string | no | Complementary registration number issued by local authorities. In certain countries, businesses may be required to hold multiple municipal registrations at national, state, or regional levels. | minLength: 1; maxLength: 15 |
| `external_id` | string | no | Marketplace external identifier | example: "EXT-MP-001" |
| `address` | object | no | Marketplace address information |  |
| `address.street` | string | no | Street address | example: "Rua das Flores, 123" |
| `address.number` | integer | no | Address number | format: "int32"; example: 123 |
| `address.neighborhood` | string | no | Field intended for entering the neighborhood name | maximum: 50 |
| `address.zip_code` | string | no | ZIP/postal code | example: "01234-567" |
| `address.city` | string | no | City name | example: "São Paulo" |
| `address.state` | string | no | State/province | example: "SP" |
| `address.country` | string | no | Country name | example: "Brasil" |
| `contact` | object | no | Contact information |  |
| `contact.name` | string | no | Contact person name | example: "João Silva" |
| `contact.email` | string | no | Contact email | format: "email"; example: "joao.silva@techstore.com" |
| `contact.phone_number` | string | no | Primary phone number | example: "+55 11 99999-9999" |
| `contact.additional_phone_number` | string | no | Secondary phone number | example: "+55 11 88888-8888" |

200 Example `marketplace-details` (Get marketplace by ID response) — from `#/components/examples/GetMarketplaceByIdExample`:

```json
{
  "id": 1654,
  "document_number": "12345678901234",
  "brand_name": "Tech Store Brasil",
  "marketplace_name": "TechStore Marketplace",
  "registration": "REG123456",
  "registration2": "REG654321",
  "external_id": "EXT-MP-001",
  "address": {
    "street": "Rua das Flores, 123",
    "number": 123,
    "neighborhood": "Jardim das Acácias",
    "zip_code": "01234-567",
    "city": "São Paulo",
    "state": "SP",
    "country": "Brasil"
  },
  "contact": {
    "name": "João Silva",
    "email": "joao.silva@techstore.com",
    "phone_number": "+55 11 99999-9999",
    "additional_phone_number": "+55 11 88888-8888"
  }
}
```

##### Response 400

400 Example `merchant-transactions-response-success` (Bad request response) — from `#/components/examples/BadRequestResponse`:

```json
{
  "code": "ESMG0900",
  "message": "Failed during validation of request payload",
  "details": {
    "payload": [
      {
        "field": "field_name",
        "message": "validation message"
      }
    ]
  }
}
```

##### Response 404

404 Example `generic-not-found-response` (Not Found Response) — from `#/components/examples/NotFoundResponse`:

```json
{
  "code": "ISMA1001",
  "message": "Not found.",
  "details": {
    "payload": [
      {
        "field": "field_name",
        "description": "not found message"
      }
    ]
  }
}
```

##### Response 500

500 Example `merchant-transactions-response-success` (Internal server error response) — from `#/components/examples/InternalServerErrorResponseExample`:

```json
{
  "message": "Internal Server Error"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `ESMG0900` | Failed during validation of request payload |
| 404 | `ISMA1001` | Not found. |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;404;500`, has examples `True`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Seller_management_-_Sellers.yaml method=PATCH path=/v1/marketplaces/{marketplaceId} operationId=updateMarketplace -->
### `PATCH /v1/marketplaces/{marketplaceId}` — Update marketplace

- **operationId:** `updateMarketplace`
- **Specification:** `api-specs/Seller_management_-_Sellers.yaml` (Seller management - Sellers)
- **Server base URL(s):** `https://sandbox.pismolabs.io/sellers`
- **Tags:** `Marketplace`
- **Deprecated in specification:** no
- **Security requirement:** not declared

**Description (from the specification):**

> This endpoint updates the marketplace information.
> This endpoint generates a <a href="https://developers.pismo.io/events/docs/marketplace-marketplace-updated-2">Marketplace updated</a> event.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `marketplaceId` | path | yes | integer | Marketplace ID | format: "int64"; minimum: 1; maximum: 18446744073709552000; example: 1654 |

#### Request body

Required: no

**Content type `application/json`** — schema: object (schema `UpdateMarketplaceRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `marketplace_name` | string (schema `MarketplaceName`) | no | Registered, legal marketplace name | minLength: 1; maxLength: 100; example: "Acme Products, LLC" |
| `brand_name` | string (schema `BrandName`) | no | Marketplace brand name. A secondary name for the marketplace that is **not** the legal registered name<br> | minLength: 1; maxLength: 50; example: "Acme" |
| `document_number` | string (schema `DocumentNumber`) | no | Marketplace document number. This is the government document code, such as a government-issued tax ID | minLength: 1; maxLength: 14; example: "20166135000139" |
| `registration` | string (schema `Registration`) | no | Municipal registration number. In some countries the municipal registration is called a business license | minLength: 1; maxLength: 15; example: "123.456.789" |
| `registration2` | string (schema `Registration2`) | no | Additional municipal registration number. In some countries, two munipal registration numbers are required — one for the country and another for the state | minLength: 1; maxLength: 15; example: "123.456.790" |
| `external_id` | string (schema `ExternalId`) | no | Marketplace ID used on client's system | minLength: 1; maxLength: 50; example: "1123" |
| `address` | object | no |  |  |
| `address.number` | integer (schema `Number`) | no | Numerical identifier for the specific location within a street or avenue | format: "int32"; minimum: 0; maximum: 2147483647; example: 22 |
| `address.street` | string (schema `Street`) | no | Name of the street, avenue, or primary thoroughfare of the address | minLength: 1; maxLength: 80; example: "Maple Avenue" |
| `address.complementary_address` | string (schema `ComplementaryAddress`) | no | Additional address details that help pinpoint the exact location, such as building, apartment, or floor | minLength: 1; maxLength: 50; example: "Suite 2" |
| `address.neighborhood` | string (schema `Neighborhood`) | no | Name of the neighborhood or administrative region where the address is located | minLength: 1; maxLength: 50; example: "West End" |
| `address.zip_code` | string (schema `ZipCode`) | no | Postal code. This is called a zip code in the United States, but you can use other types of postal codes | minLength: 1; maxLength: 9; example: "91941" |
| `address.city` | string (schema `City`) | no | Name of the city or municipality | minLength: 1; maxLength: 60; example: "San Diego" |
| `address.state` | string (schema `State`) | no | Abbreviation or full name of the state, province, or administrative division | minLength: 2; maxLength: 2; example: "CA" |
| `address.country` | string (schema `Country`) | no | Full name of the country according to international standards or local registry | minLength: 1; maxLength: 30; example: "United States" |
| `contact` | object | no |  |  |
| `contact.name` | string (schema `Name`) | no | Contact name for the marketplace | minLength: 1; maxLength: 50; example: "Jane Doe" |
| `contact.email` | string (schema `Email`) | no | Marketplace contact email address. Its format must be a valid email address | minLength: 1; maxLength: 255; example: "email@email.com" |
| `contact.phone_number` | string (schema `PhoneNumber`) | no | Phone number. Dashes and parentheses are optional | minLength: 1; maxLength: 25; example: "5558739452" |
| `contact.additional_phone_number` | string (schema `AdditionalPhoneNumber`) | no | Additional phone number. Dashes and parentheses are optional | minLength: 1; maxLength: 25; example: "5558739453" |

Example `marketplace-request-success` (Update marketplace payload) — from `#/components/examples/UpdateMarketplaceRequestExample`:

```json
{
  "document_number": "99419954904000",
  "registration": "REG123456",
  "registration2": "REG654321",
  "brand_name": "Natalia",
  "marketplace_name": "Test Marketplace",
  "external_id": "EXT-40790",
  "address": {
    "street": "Main Street",
    "number": 100,
    "complementary_address": "Suite 10",
    "neighborhood": "Downtown",
    "zip_code": "22345-477",
    "city": "San Francisco",
    "state": "CA",
    "country": "US"
  },
  "contact": {
    "name": "Alex Miller",
    "email": "marketplace@teste.com",
    "phone_number": "4155551234",
    "additional_phone_number": "4155555678"
  }
}
```

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Ok | `application/json`: object (schema `GetMarketplaceByIdResponse`) |
| 400 | Bad request | `application/json`: object (schema `ErrorRequestResponse`) |
| 404 | Not found | `application/json`: object (schema `ErrorRequestResponse`) |
| 500 | Internal server error | `application/json`: object (schema `InternalServerErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | integer (schema `MarketplaceId`) | no | Marketplace ID | format: "int64"; minimum: 1; maximum: 18446744073709552000; example: 51148 |
| `document_number` | string | no | Marketplace document number | example: "12345678901234" |
| `brand_name` | string | no | Marketplace brand name | example: "Tech Store Brasil" |
| `marketplace_name` | string | no | Marketplace name | example: "TechStore Marketplace" |
| `registration` | string | no | Official company registration with the local municipality | minLength: 1; maxLength: 15 |
| `registration2` | string | no | Complementary registration number issued by local authorities. In certain countries, businesses may be required to hold multiple municipal registrations at national, state, or regional levels. | minLength: 1; maxLength: 15 |
| `external_id` | string | no | Marketplace external identifier | example: "EXT-MP-001" |
| `address` | object | no | Marketplace address information |  |
| `address.street` | string | no | Street address | example: "Rua das Flores, 123" |
| `address.number` | integer | no | Address number | format: "int32"; example: 123 |
| `address.neighborhood` | string | no | Field intended for entering the neighborhood name | maximum: 50 |
| `address.zip_code` | string | no | ZIP/postal code | example: "01234-567" |
| `address.city` | string | no | City name | example: "São Paulo" |
| `address.state` | string | no | State/province | example: "SP" |
| `address.country` | string | no | Country name | example: "Brasil" |
| `contact` | object | no | Contact information |  |
| `contact.name` | string | no | Contact person name | example: "João Silva" |
| `contact.email` | string | no | Contact email | format: "email"; example: "joao.silva@techstore.com" |
| `contact.phone_number` | string | no | Primary phone number | example: "+55 11 99999-9999" |
| `contact.additional_phone_number` | string | no | Secondary phone number | example: "+55 11 88888-8888" |

200 Example `marketplace-details` (Get marketplace by ID response) — from `#/components/examples/GetMarketplaceByIdExample`:

```json
{
  "id": 1654,
  "document_number": "12345678901234",
  "brand_name": "Tech Store Brasil",
  "marketplace_name": "TechStore Marketplace",
  "registration": "REG123456",
  "registration2": "REG654321",
  "external_id": "EXT-MP-001",
  "address": {
    "street": "Rua das Flores, 123",
    "number": 123,
    "neighborhood": "Jardim das Acácias",
    "zip_code": "01234-567",
    "city": "São Paulo",
    "state": "SP",
    "country": "Brasil"
  },
  "contact": {
    "name": "João Silva",
    "email": "joao.silva@techstore.com",
    "phone_number": "+55 11 99999-9999",
    "additional_phone_number": "+55 11 88888-8888"
  }
}
```

##### Response 400

400 Example `merchant-transactions-response-success` (Bad request response) — from `#/components/examples/BadRequestResponse`:

```json
{
  "code": "ESMG0900",
  "message": "Failed during validation of request payload",
  "details": {
    "payload": [
      {
        "field": "field_name",
        "message": "validation message"
      }
    ]
  }
}
```

##### Response 404

404 Example `generic-not-found-response` (Not Found Response) — from `#/components/examples/NotFoundResponse`:

```json
{
  "code": "ISMA1001",
  "message": "Not found.",
  "details": {
    "payload": [
      {
        "field": "field_name",
        "description": "not found message"
      }
    ]
  }
}
```

##### Response 500

500 Example `merchant-transactions-response-success` (Internal server error response) — from `#/components/examples/InternalServerErrorResponseExample`:

```json
{
  "message": "Internal Server Error"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `ESMG0900` | Failed during validation of request payload |
| 404 | `ISMA1001` | Not found. |

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `marketplace-marketplace-updated-2` | https://developers.pismo.io/events/docs/marketplace-marketplace-updated-2 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;404;500`, has examples `True`, emits events `1`, deprecated `False`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/MarketplaceListItem -->
### Schema `MarketplaceListItem`

Pointer: `#/components/schemas/MarketplaceListItem`. Type: object (schema `MarketplaceListItem`).

> Marketplace information in paginated list response

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `brand_name` | string | yes | Brand name of the marketplace | example: "Acme Corporation" |
| `document_number` | string | yes | Marketplace document number | example: "12345678901234" |
| `id` | integer (schema `MarketplaceId`) | yes | Marketplace ID | format: "int64"; minimum: 1; maximum: 18446744073709552000; example: 51148 |
| `marketplace_name` | string | yes | Registered marketplace name | example: "Acme Store" |
| `external_id` | string \\\| null | no | External system identifier | example: "EXT-123" |

<!-- schema: #/components/schemas/ErrorRequestResponse -->
### Schema `ErrorRequestResponse`

Pointer: `#/components/schemas/ErrorRequestResponse`. Type: object (schema `ErrorRequestResponse`).

> Error payload returned by the API

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string | no | Pismo internal error code |  |
| `message` | string | no | Error message |  |
| `details` | object | no | If necessary, this field shows which fields failed validation |  |
| `details.payload` | array of object | no | Array of fields with error |  |
| `details.payload[].field` | string | no | Name of field with error |  |
| `details.payload[].message` | string | no | Error message referring to the field |  |

<!-- schema: #/components/schemas/InternalServerErrorResponse -->
### Schema `InternalServerErrorResponse`

Pointer: `#/components/schemas/InternalServerErrorResponse`. Type: object (schema `InternalServerErrorResponse`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `message` | string | no | Message |  |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Seller_management_-_Sellers.yaml` | tag `Marketplace`: GET /v3/marketplaces, POST /v3/marketplaces, GET /v3/marketplaces/{marketplaceId}, PATCH /v1/marketplaces/{marketplaceId} | https://github.com/PismoDevEx/pismo-api-specs | `eb5d18c21f5848fe…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-ERR-codes-esmg-to-whis` — Error codes: ESMG to WHIS (30 prefixes)
- `KU-EVT-catalogue-marketplace` — Event catalogue: marketplace
