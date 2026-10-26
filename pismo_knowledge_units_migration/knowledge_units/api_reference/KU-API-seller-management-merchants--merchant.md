---
ku_id: KU-API-seller-management-merchants--merchant
title: 'API reference: Seller management - Merchants — Merchant'
category: api_reference
ku_type: api_reference
lifecycle: current
sources:
- path: api-specs/Seller_management_-_Merchants.yaml
  sha256: ebc9f3fadda7001c7ad8d607cd3fe07461f96c39c6ca15baccef307dd27f67bb
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
- listMerchants
- createMerchant
- getMerchant
- updateMerchant
- listStatusTransitions
- updateMerchantStatus
related_kus:
- KU-EVT-catalogue-merchants
- KU-GS-get-started-with-pismo-apis
- KU-SELL-get-started-seller-management
- KU-SELL-managing-merchant-transactions
- KU-SELL-seller-management-overview-and-onboarding
- KU-SELL-seller-marketplace-implementation-steps
specification_version: 1.0.0
---

# API reference: Seller management - Merchants — Merchant

**KU ID:** `KU-API-seller-management-merchants--merchant` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 6 operation(s) tagged `Merchant` in `api-specs/Seller_management_-_Merchants.yaml` (“Seller management - Merchants”, version `1.0.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Endpoints for merchant operations

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `GET /v1/merchants` | `listMerchants` | List merchants | no |
| `POST /v1/merchants` | `createMerchant` | Create merchant | no |
| `GET /v1/merchants/{merchantId}` | `getMerchant` | Get merchant | no |
| `PUT /v1/merchants/{merchantId}` | `updateMerchant` | Update merchant | no |
| `GET /v1/merchants/{merchantId}/workflow/statuses` | `listStatusTransitions` | List status transitions | no |
| `PUT /v1/merchants/{merchantId}/workflow/status` | `updateMerchantStatus` | Update merchant status | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"}

## Operation contracts

<!-- op: spec=api-specs/Seller_management_-_Merchants.yaml method=GET path=/v1/merchants operationId=listMerchants -->
### `GET /v1/merchants` — List merchants

- **operationId:** `listMerchants`
- **Specification:** `api-specs/Seller_management_-_Merchants.yaml` (Seller management - Merchants)
- **Server base URL(s):** `https://sandbox.pismolabs.io/merchants`
- **Tags:** `Merchant`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Find merchants using query parameters.
>
> For more information about merchants, see the <a href="https://developers.pismo.io/pismo-docs/docs/seller-management-overview" target="blank">Seller management overview</a> guide.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | no | string | Authorization token. This is a regular access token, which does not need to include an account ID. | example: "Bearer 1JI12J39182H39182JDIOAWJ%=" |
| `x-marketplace-id` | header | no | integer | Marketplace ID | format: "int64"; example: 123456 |
| `documentNumber` | query | no | string | Merchant document number | minLength: 1; maxLength: 128; example: "73399909000114" |
| `status` | query | no | string | Merchant status. This is a string, not an enum, so any string value is allowed, but the most commonly used values are: 'ACTIVE', 'ANALYSING', 'APPROVED', 'CANCELLED', 'PENDING', 'REJECTED' | example: "ACTIVE" |
| `name` | query | no | string | Merchant name | minLength: 1; maxLength: 128; example: "Acme Store" |
| `externalId` | query | no | string | ID used by client to reference a merchant in their domain. | minLength: 1; maxLength: 50; example: "5321" |
| `page` | query | no | integer | Page number. Default is 1. | format: "int32"; example: 1 |
| `perPage` | query | no | integer | Items per page. Default is 10. | format: "int32"; example: 10 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `FindMerchantsResponse`) |
| 401 | Access token is missing or invalid |  |
| 500 | Internal server error |  |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | integer (schema `MerchantID`) | no | Merchant ID | format: "int64"; example: 1 |
| `document_number` | string (schema `MerchantDocumentNumber`) | no | Merchant document number. This is the government document code, such as a government-issued tax ID.<br> | minLength: 1; maxLength: 14; example: "40533164000107" |
| `municipal_registration` | string (schema `MunicipalRegistration`) | no | Merchant's municipal registration number<br> | minLength: 1; maxLength: 128; example: "737.326.648.860" |
| `contact` | string (schema `ContactName`) | no | Name of contact | minLength: 1; maxLength: 128; example: "John Doe" |
| `email` | string (schema `EmailAddress`) | no | Email address | example: "test@acmecorp.com" |
| `zip_code` | string (schema `PostalCode`) | no | Postal code. This is called a zip code in the United States, but you can use other types of postal codes. | minLength: 1; maxLength: 9; example: "12345" |
| `address` | string (schema `AddressLine`) | no | Name of the street, avenue, or primary thoroughfare of the address | minLength: 1; maxLength: 80; example: "Maple Street" |
| `complementary_address` | string (schema `ComplementaryAddress`) | no | Additional address details that help pinpoint the exact location, such as building, apartment, or floor | minLength: 1; maxLength: 50; example: "Suite 100" |
| `neighborhood` | string (schema `Neighborhood`) | no | Name of the neighborhood or administrative region where the address is located | minLength: 1; maxLength: 50; example: "Canary Wharf" |
| `state` | string (schema `State`) | no | Abbreviation or full name of the state, province, or administrative division | minLength: 1; maxLength: 2; example: "CA" |
| `city` | string (schema `City`) | no | Name of the city or municipality | minLength: 1; maxLength: 60; example: "San Diego" |
| `city_code` | string (schema `CityCode`) | no | Official seven-digit numeric code of the city according to the IBGE (Brazilian Institute of Geography and Statistics) code table. Used only for cities in Brazil; this code is unique per city. | minLength: 1; maxLength: 50; example: "3550308" |
| `country` | string (schema `Country`) | no | Full name of the country according to international standards or local registry | minLength: 1; maxLength: 30; example: "United States" |
| `number` | integer (schema `AddressNumber`) | no | Numerical identifier for the specific location within a street or avenue | format: "int64"; example: 45 |
| `area_code` | string (schema `AreaCode`) | no | Area code. The US, Canada, and certain other countries divide their telephone service into regions, which are identified by numbers called area codes.<br>In the US, for example, area codes are 3-digit numbers.<br> | example: "555" |
| `phone` | string (schema `Phone`) | no | Phone number. Parentheses and dashes are optional. | maxLength: 25; example: "1231234" |
| `additional_area_code` | string (schema `AdditionalAreaCode`) | no | Additional area code (for `additional_phone`) | example: "11" |
| `additional_phone` | string (schema `AdditionalPhone`) | no | Number for an additional phone. Parentheses and dashes are optional. | example: "2342345" |
| `marketplace_category` | number (schema `MarketplaceCategoryID`) | no | Marketplace category ID. The category is the type of business. | deprecated: true; example: 123 |
| `status` | string (schema `MerchantStatus`) | no | Merchant status. This is a string, not an enum, so any string value is allowed, but the most commonly used values are: 'ACTIVE', 'ANALYSING', 'APPROVED', 'CANCELLED', 'PENDING', 'REJECTED' | minLength: 1; maxLength: 128; example: "APPROVED" |
| `program_id` | integer (schema `MerchantProgramID`) | no | Program ID for merchant account | format: "int64"; example: 123 |
| `external_id` | string (schema `ExternalID`) | no | Internal ID used by client to reference a merchant in their domain. | example: "5321" |
| `business_category` | object | no | Type of business |  |
| `business_category.external_code` | string (schema `ExternalCode`) | no | Code for merchant category. The category is the type of business. You can use the endpoint <a href="https://developers.pismo.io/pismo-docs/reference/get_v1-businesscategories">Retrieves business categories corresponding to query parameters</a> to get a list of business categories and their external codes.<br> | minLength: 1; maxLength: 128 |
| `business_category.category` | string (schema `BusinessCategoryName`) | no | Business category name | minLength: 1; maxLength: 128 |
| `business_category.description` | string (schema `BusinessCategoryDescription`) | no | Business category description | minLength: 1; maxLength: 128 |
| `creditor_id` | integer (schema `CreditorID`) | no | Creditor ID | format: "int64"; example: 1 |
| `name` | string (schema `MerchantBrandName`) | no | Merchant brand name. Note that this is different from a merchant's legal registered name. For example, <i>Great Company</i> as opposed to <i>Great Company, LLC</i> (legal entity name).<br> | minLength: 1; maxLength: 128; example: "Acme Corporation" |
| `merchant_name` | string (schema `MerchantName`) | no | Merchant name | minLength: 1; maxLength: 100; example: "Acme Store" |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;401;500`, has examples `False`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Seller_management_-_Merchants.yaml method=POST path=/v1/merchants operationId=createMerchant -->
### `POST /v1/merchants` — Create merchant

- **operationId:** `createMerchant`
- **Specification:** `api-specs/Seller_management_-_Merchants.yaml` (Seller management - Merchants)
- **Server base URL(s):** `https://sandbox.pismolabs.io/merchants`
- **Tags:** `Merchant`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Create merchant. You use this endpoint to register a merchant (store) in a marketplace using the information the merchant provides.
>
> <b>Note:</b> Before you create merchants, you must create a Merchant program, using the [Create program based on template](ref:createprogrambasedontemplate) endpoint with `type` set to `MERCHANT`. If a program of type `MERCHANT` is not provided, the request returns an error.
> By default, when a merchant is created, the Pismo platform assigns it to the first existing program of type `MERCHANT` in the Org. However, you have the option of specifying a program by providing its ID in the `program_id` field.
>
> <b>Note:</b> When a `x-marketplace-id` header is provided, the merchant is automatically linked to the provided marketplace after creation.
>
> For more information about merchants, refer to the <a href="https://developers.pismo.io/pismo-docs/docs/seller-management-overview" target="blank">Seller management overview</a> guide.<br>
>
> This endpoint generates a [Merchant created](https://developers.pismo.io/events/docs/merchants-merchant-created-1) event.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Content-Type` | header | no | string | Content type | example: "application/json" |
| `Authorization` | header | no | string | Authorization token. This is a regular access token, which does not need to include an account ID. | example: "Bearer 1JI12J39182H39182JDIOAWJ%=" |
| `x-marketplace-id` | header | no | integer | Marketplace ID | format: "int64"; example: 123456 |

#### Request body

Required: yes

> Request body

**Content type `application/json`** — schema: object (schema `POSTMerchantRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `document_number` | string (schema `MerchantDocumentNumber`) | yes | Merchant document number. This is the government document code, such as a government-issued tax ID.<br> | minLength: 1; maxLength: 14; example: "40533164000107" |
| `name` | string (schema `MerchantName`) | yes | Merchant name | minLength: 1; maxLength: 100; example: "Acme Store" |
| `email` | string (schema `EmailAddress`) | yes | Email address | example: "test@acmecorp.com" |
| `brand_name` | string (schema `MerchantBrandName`) | no | Merchant brand name. Note that this is different from a merchant's legal registered name. For example, <i>Great Company</i> as opposed to <i>Great Company, LLC</i> (legal entity name).<br> | minLength: 1; maxLength: 128; example: "Acme Corporation" |
| `municipal_registration` | string (schema `MunicipalRegistration`) | no | Merchant's municipal registration number<br> | minLength: 1; maxLength: 128; example: "737.326.648.860" |
| `contact` | string (schema `ContactName`) | no | Name of contact | minLength: 1; maxLength: 128; example: "John Doe" |
| `zip_code` | string (schema `PostalCode`) | no | Postal code. This is called a zip code in the United States, but you can use other types of postal codes. | minLength: 1; maxLength: 9; example: "12345" |
| `number` | integer (schema `AddressNumber`) | no | Numerical identifier for the specific location within a street or avenue | format: "int64"; example: 45 |
| `address` | string (schema `AddressLine`) | no | Name of the street, avenue, or primary thoroughfare of the address | minLength: 1; maxLength: 80; example: "Maple Street" |
| `complementary_address` | string (schema `ComplementaryAddress`) | no | Additional address details that help pinpoint the exact location, such as building, apartment, or floor | minLength: 1; maxLength: 50; example: "Suite 100" |
| `neighborhood` | string (schema `Neighborhood`) | no | Name of the neighborhood or administrative region where the address is located | minLength: 1; maxLength: 50; example: "Canary Wharf" |
| `state` | string (schema `State`) | no | Abbreviation or full name of the state, province, or administrative division | minLength: 1; maxLength: 2; example: "CA" |
| `city` | string (schema `City`) | no | Name of the city or municipality | minLength: 1; maxLength: 60; example: "San Diego" |
| `country` | string (schema `Country`) | no | Full name of the country according to international standards or local registry | minLength: 1; maxLength: 30; example: "United States" |
| `area_code` | string (schema `AreaCode`) | no | Area code. The US, Canada, and certain other countries divide their telephone service into regions, which are identified by numbers called area codes.<br>In the US, for example, area codes are 3-digit numbers.<br> | example: "555" |
| `phone` | string (schema `Phone`) | no | Phone number. Parentheses and dashes are optional. | maxLength: 25; example: "1231234" |
| `additional_area_code` | string (schema `AdditionalAreaCode`) | no | Additional area code (for `additional_phone`) | example: "11" |
| `additional_phone` | string (schema `AdditionalPhone`) | no | Number for an additional phone. Parentheses and dashes are optional. | example: "2342345" |
| `program_id` | integer (schema `MerchantProgramID`) | no | Program ID for merchant account | format: "int64"; example: 123 |
| `external_code` | string (schema `ExternalCode`) | no | Code for merchant category. The category is the type of business. You can use the endpoint <a href="https://developers.pismo.io/pismo-docs/reference/get_v1-businesscategories">Retrieves business categories corresponding to query parameters</a> to get a list of business categories and their external codes.<br> | minLength: 1; maxLength: 128 |
| `external_id` | string (schema `ExternalID`) | no | Internal ID used by client to reference a merchant in their domain. | example: "5321" |
| `creditor` | object (schema `POSTMerchantCreditorRequest`) | no | This is the entity from which the merchant receives money when a transaction is settled.<br>It should be a Pismo account.<br><br>You can either provide an `id` to create a merchant with an already existing creditor, or fill in the creditor fields to create a new creditor for the created merchant.<br> |  |
| `city_code` | string (schema `CityCode`) | no | Official seven-digit numeric code of the city according to the IBGE (Brazilian Institute of Geography and Statistics) code table. Used only for cities in Brazil; this code is unique per city. | minLength: 1; maxLength: 50; example: "3550308" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | Created | `application/json`: object (schema `POSTMerchantResponse`) |
| 400 | Bad Request |  |
| 401 | Access token is missing or invalid |  |
| 500 | Internal server error |  |

##### Response 201

**201 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | integer (schema `MerchantID`) | no | Merchant ID | format: "int64"; example: 1 |
| `document_number` | string (schema `MerchantDocumentNumber`) | no | Merchant document number. This is the government document code, such as a government-issued tax ID.<br> | minLength: 1; maxLength: 14; example: "40533164000107" |
| `name` | string (schema `MerchantName`) | no | Merchant name | minLength: 1; maxLength: 100; example: "Acme Store" |
| `brand_name` | string (schema `MerchantBrandName`) | no | Merchant brand name. Note that this is different from a merchant's legal registered name. For example, <i>Great Company</i> as opposed to <i>Great Company, LLC</i> (legal entity name).<br> | minLength: 1; maxLength: 128; example: "Acme Corporation" |
| `municipal_registration` | string (schema `MunicipalRegistration`) | no | Merchant's municipal registration number<br> | minLength: 1; maxLength: 128; example: "737.326.648.860" |
| `category` | string (schema `MerchantCategory`) | no | Code name for merchant category. The category is the type of business. | minLength: 1; maxLength: 128; deprecated: true; example: "abc-123" |
| `contact` | string (schema `ContactName`) | no | Name of contact | minLength: 1; maxLength: 128; example: "John Doe" |
| `email` | string (schema `EmailAddress`) | no | Email address | example: "test@acmecorp.com" |
| `zip_code` | string (schema `PostalCode`) | no | Postal code. This is called a zip code in the United States, but you can use other types of postal codes. | minLength: 1; maxLength: 9; example: "12345" |
| `address` | string (schema `AddressLine`) | no | Name of the street, avenue, or primary thoroughfare of the address | minLength: 1; maxLength: 80; example: "Maple Street" |
| `complementary_address` | string (schema `ComplementaryAddress`) | no | Additional address details that help pinpoint the exact location, such as building, apartment, or floor | minLength: 1; maxLength: 50; example: "Suite 100" |
| `neighborhood` | string (schema `Neighborhood`) | no | Name of the neighborhood or administrative region where the address is located | minLength: 1; maxLength: 50; example: "Canary Wharf" |
| `state` | string (schema `State`) | no | Abbreviation or full name of the state, province, or administrative division | minLength: 1; maxLength: 2; example: "CA" |
| `city` | string (schema `City`) | no | Name of the city or municipality | minLength: 1; maxLength: 60; example: "San Diego" |
| `country` | string (schema `Country`) | no | Full name of the country according to international standards or local registry | minLength: 1; maxLength: 30; example: "United States" |
| `number` | integer (schema `AddressNumber`) | no | Numerical identifier for the specific location within a street or avenue | format: "int64"; example: 45 |
| `area_code` | string (schema `AreaCode`) | no | Area code. The US, Canada, and certain other countries divide their telephone service into regions, which are identified by numbers called area codes.<br>In the US, for example, area codes are 3-digit numbers.<br> | example: "555" |
| `phone` | string (schema `Phone`) | no | Phone number. Parentheses and dashes are optional. | maxLength: 25; example: "1231234" |
| `additional_area_code` | string (schema `AdditionalAreaCode`) | no | Additional area code (for `additional_phone`) | example: "11" |
| `additional_phone` | string (schema `AdditionalPhone`) | no | Number for an additional phone. Parentheses and dashes are optional. | example: "2342345" |
| `program_id` | integer (schema `MerchantProgramID`) | no | Program ID for merchant account | format: "int64"; example: 123 |
| `external_code` | string (schema `ExternalCode`) | no | Code for merchant category. The category is the type of business. You can use the endpoint <a href="https://developers.pismo.io/pismo-docs/reference/get_v1-businesscategories">Retrieves business categories corresponding to query parameters</a> to get a list of business categories and their external codes.<br> | minLength: 1; maxLength: 128 |
| `external_id` | string (schema `ExternalID`) | no | Internal ID used by client to reference a merchant in their domain. | example: "5321" |
| `creditor` | object (schema `MerchantCreditorResponse`) | no | Get response from merchant creditor.<br> | example: {"id": 7611, "name": "Acme Corporation", "crediting_method": "ACCOUNT", "account": {"id": 2}, "advancement_fee": "3.00", "discount_rate": "0.025", "maximum_advancement_percentage": "0.80"} |


#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `merchants-merchant-created-1` | https://developers.pismo.io/events/docs/merchants-merchant-created-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `201;400;401;500`, has examples `False`, emits events `1`, deprecated `False`.

Guides that link to this operation: `KU-GS-get-started-with-pismo-apis`, `KU-SELL-get-started-seller-management`, `KU-SELL-managing-merchant-transactions`, `KU-SELL-seller-management-overview-and-onboarding`, `KU-SELL-seller-marketplace-implementation-steps`.

<!-- op: spec=api-specs/Seller_management_-_Merchants.yaml method=GET path=/v1/merchants/{merchantId} operationId=getMerchant -->
### `GET /v1/merchants/{merchantId}` — Get merchant

- **operationId:** `getMerchant`
- **Specification:** `api-specs/Seller_management_-_Merchants.yaml` (Seller management - Merchants)
- **Server base URL(s):** `https://sandbox.pismolabs.io/merchants`
- **Tags:** `Merchant`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Get merchant by ID.
>
> For more information about merchants, see the <a href="https://developers.pismo.io/pismo-docs/docs/seller-management-overview" target="blank">Seller management overview</a> guide.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Content-Type` | header | no | string | Content type | example: "application/json" |
| `Authorization` | header | no | string | Authorization token. This is a regular access token, which does not need to include an account ID. | example: "Bearer 1JI12J39182H39182JDIOAWJ%=" |
| `merchantId` | path | yes | integer | Merchant ID | format: "int64"; example: 1 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `GETMerchantResponse`) |
| 400 | Bad Request |  |
| 401 | Access token is missing or invalid |  |
| 500 | Internal server error |  |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | integer (schema `MerchantID`) | no | Merchant ID | format: "int64"; example: 1 |
| `document_number` | string (schema `MerchantDocumentNumber`) | no | Merchant document number. This is the government document code, such as a government-issued tax ID.<br> | minLength: 1; maxLength: 14; example: "40533164000107" |
| `municipal_registration` | string (schema `MunicipalRegistration`) | no | Merchant's municipal registration number<br> | minLength: 1; maxLength: 128; example: "737.326.648.860" |
| `contact` | string (schema `ContactName`) | no | Name of contact | minLength: 1; maxLength: 128; example: "John Doe" |
| `email` | string (schema `EmailAddress`) | no | Email address | example: "test@acmecorp.com" |
| `zip_code` | string (schema `PostalCode`) | no | Postal code. This is called a zip code in the United States, but you can use other types of postal codes. | minLength: 1; maxLength: 9; example: "12345" |
| `address` | string (schema `AddressLine`) | no | Name of the street, avenue, or primary thoroughfare of the address | minLength: 1; maxLength: 80; example: "Maple Street" |
| `complementary_address` | string (schema `ComplementaryAddress`) | no | Additional address details that help pinpoint the exact location, such as building, apartment, or floor | minLength: 1; maxLength: 50; example: "Suite 100" |
| `neighborhood` | string (schema `Neighborhood`) | no | Name of the neighborhood or administrative region where the address is located | minLength: 1; maxLength: 50; example: "Canary Wharf" |
| `state` | string (schema `State`) | no | Abbreviation or full name of the state, province, or administrative division | minLength: 1; maxLength: 2; example: "CA" |
| `city` | string (schema `City`) | no | Name of the city or municipality | minLength: 1; maxLength: 60; example: "San Diego" |
| `city_code` | string (schema `CityCode`) | no | Official seven-digit numeric code of the city according to the IBGE (Brazilian Institute of Geography and Statistics) code table. Used only for cities in Brazil; this code is unique per city. | minLength: 1; maxLength: 50; example: "3550308" |
| `country` | string (schema `Country`) | no | Full name of the country according to international standards or local registry | minLength: 1; maxLength: 30; example: "United States" |
| `number` | integer (schema `AddressNumber`) | no | Numerical identifier for the specific location within a street or avenue | format: "int64"; example: 45 |
| `area_code` | string (schema `AreaCode`) | no | Area code. The US, Canada, and certain other countries divide their telephone service into regions, which are identified by numbers called area codes.<br>In the US, for example, area codes are 3-digit numbers.<br> | example: "555" |
| `phone` | string (schema `Phone`) | no | Phone number. Parentheses and dashes are optional. | maxLength: 25; example: "1231234" |
| `additional_area_code` | string (schema `AdditionalAreaCode`) | no | Additional area code (for `additional_phone`) | example: "11" |
| `additional_phone` | string (schema `AdditionalPhone`) | no | Number for an additional phone. Parentheses and dashes are optional. | example: "2342345" |
| `marketplace_category` | number (schema `MarketplaceCategoryID`) | no | Marketplace category ID. The category is the type of business. | deprecated: true; example: 123 |
| `status` | string (schema `MerchantStatus`) | no | Merchant status. This is a string, not an enum, so any string value is allowed, but the most commonly used values are: 'ACTIVE', 'ANALYSING', 'APPROVED', 'CANCELLED', 'PENDING', 'REJECTED' | minLength: 1; maxLength: 128; example: "APPROVED" |
| `program_id` | integer (schema `MerchantProgramID`) | no | Program ID for merchant account | format: "int64"; example: 123 |
| `external_id` | string (schema `ExternalID`) | no | Internal ID used by client to reference a merchant in their domain. | example: "5321" |
| `business_category` | object | no | Type of business |  |
| `business_category.external_code` | string (schema `ExternalCode`) | no | Code for merchant category. The category is the type of business. You can use the endpoint <a href="https://developers.pismo.io/pismo-docs/reference/get_v1-businesscategories">Retrieves business categories corresponding to query parameters</a> to get a list of business categories and their external codes.<br> | minLength: 1; maxLength: 128 |
| `business_category.category` | string (schema `BusinessCategoryName`) | no | Business category name | minLength: 1; maxLength: 128 |
| `business_category.description` | string (schema `BusinessCategoryDescription`) | no | Business category description | minLength: 1; maxLength: 128 |
| `name` | string (schema `MerchantName`) | no | Merchant name | minLength: 1; maxLength: 100; example: "Acme Store" |
| `brand_name` | string (schema `MerchantBrandName`) | no | Merchant brand name. Note that this is different from a merchant's legal registered name. For example, <i>Great Company</i> as opposed to <i>Great Company, LLC</i> (legal entity name).<br> | minLength: 1; maxLength: 128; example: "Acme Corporation" |
| `creditor` | object (schema `MerchantCreditorResponse`) | no | Get response from merchant creditor.<br> | example: {"id": 7611, "name": "Acme Corporation", "crediting_method": "ACCOUNT", "account": {"id": 2}, "advancement_fee": "3.00", "discount_rate": "0.025", "maximum_advancement_percentage": "0.80"} |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;500`, has examples `False`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Seller_management_-_Merchants.yaml method=PUT path=/v1/merchants/{merchantId} operationId=updateMerchant -->
### `PUT /v1/merchants/{merchantId}` — Update merchant

- **operationId:** `updateMerchant`
- **Specification:** `api-specs/Seller_management_-_Merchants.yaml` (Seller management - Merchants)
- **Server base URL(s):** `https://sandbox.pismolabs.io/merchants`
- **Tags:** `Merchant`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Update merchant by ID.
>
> For more information about merchants, see the <a href="https://developers.pismo.io/pismo-docs/docs/seller-management-overview" target="blank">Seller management overview</a> guide.<br>
> This endpoint generates a [Merchant updated](https://developers.pismo.io/events/docs/merchants-merchant-updated-1) event.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Content-Type` | header | no | string | Content type | example: "application/json" |
| `Authorization` | header | no | string | Authorization token. This is a regular access token, which does not need to include an account ID. | example: "Bearer 1JI12J39182H39182JDIOAWJ%=" |
| `merchantId` | path | yes | integer | Merchant ID | format: "int64"; example: 1 |

#### Request body

Required: yes

> Request body

**Content type `application/json`** — schema: object (schema `PUTMerchantRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `document_number` | string (schema `MerchantDocumentNumber`) | no | Merchant document number. This is the government document code, such as a government-issued tax ID.<br> | minLength: 1; maxLength: 14; example: "40533164000107" |
| `name` | string (schema `MerchantName`) | yes | Merchant name | minLength: 1; maxLength: 100; example: "Acme Store" |
| `brand_name` | string (schema `MerchantBrandName`) | no | Merchant brand name. Note that this is different from a merchant's legal registered name. For example, <i>Great Company</i> as opposed to <i>Great Company, LLC</i> (legal entity name).<br> | minLength: 1; maxLength: 128; example: "Acme Corporation" |
| `municipal_registration` | string (schema `MunicipalRegistration`) | no | Merchant's municipal registration number<br> | minLength: 1; maxLength: 128; example: "737.326.648.860" |
| `contact` | string (schema `ContactName`) | no | Name of contact | minLength: 1; maxLength: 128; example: "John Doe" |
| `email` | string (schema `EmailAddress`) | yes | Email address | example: "test@acmecorp.com" |
| `zip_code` | string (schema `PostalCode`) | no | Postal code. This is called a zip code in the United States, but you can use other types of postal codes. | minLength: 1; maxLength: 9; example: "12345" |
| `address` | string (schema `AddressLine`) | no | Name of the street, avenue, or primary thoroughfare of the address | minLength: 1; maxLength: 80; example: "Maple Street" |
| `complementary_address` | string (schema `ComplementaryAddress`) | no | Additional address details that help pinpoint the exact location, such as building, apartment, or floor | minLength: 1; maxLength: 50; example: "Suite 100" |
| `neighborhood` | string (schema `Neighborhood`) | no | Name of the neighborhood or administrative region where the address is located | minLength: 1; maxLength: 50; example: "Canary Wharf" |
| `state` | string (schema `State`) | no | Abbreviation or full name of the state, province, or administrative division | minLength: 1; maxLength: 2; example: "CA" |
| `city` | string (schema `City`) | no | Name of the city or municipality | minLength: 1; maxLength: 60; example: "San Diego" |
| `country` | string (schema `Country`) | no | Full name of the country according to international standards or local registry | minLength: 1; maxLength: 30; example: "United States" |
| `number` | integer (schema `AddressNumber`) | no | Numerical identifier for the specific location within a street or avenue | format: "int64"; example: 45 |
| `area_code` | string (schema `AreaCode`) | no | Area code. The US, Canada, and certain other countries divide their telephone service into regions, which are identified by numbers called area codes.<br>In the US, for example, area codes are 3-digit numbers.<br> | example: "555" |
| `phone` | string (schema `Phone`) | no | Phone number. Parentheses and dashes are optional. | maxLength: 25; example: "1231234" |
| `additional_area_code` | string (schema `AdditionalAreaCode`) | no | Additional area code (for `additional_phone`) | example: "11" |
| `additional_phone` | string (schema `AdditionalPhone`) | no | Number for an additional phone. Parentheses and dashes are optional. | example: "2342345" |
| `external_code` | string (schema `ExternalCode`) | no | Code for merchant category. The category is the type of business. You can use the endpoint <a href="https://developers.pismo.io/pismo-docs/reference/get_v1-businesscategories">Retrieves business categories corresponding to query parameters</a> to get a list of business categories and their external codes.<br> | minLength: 1; maxLength: 128 |
| `creditor` | object (schema `PUTMerchantCreditorRequest`) | no | This is the entity from which the merchant receives money when a transaction is settled.<br>It should be a Pismo account.<br> |  |
| `city_code` | string (schema `CityCode`) | no | Official seven-digit numeric code of the city according to the IBGE (Brazilian Institute of Geography and Statistics) code table. Used only for cities in Brazil; this code is unique per city. | minLength: 1; maxLength: 50; example: "3550308" |
| `external_id` | string (schema `ExternalID`) | no | Internal ID used by client to reference a merchant in their domain. | example: "5321" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK |  |
| 400 | Bad Request |  |
| 401 | Access token is missing or invalid |  |
| 500 | Internal server error |  |


#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `merchants-merchant-updated-1` | https://developers.pismo.io/events/docs/merchants-merchant-updated-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;500`, has examples `False`, emits events `1`, deprecated `False`.

<!-- op: spec=api-specs/Seller_management_-_Merchants.yaml method=GET path=/v1/merchants/{merchantId}/workflow/statuses operationId=listStatusTransitions -->
### `GET /v1/merchants/{merchantId}/workflow/statuses` — List status transitions

- **operationId:** `listStatusTransitions`
- **Specification:** `api-specs/Seller_management_-_Merchants.yaml` (Seller management - Merchants)
- **Server base URL(s):** `https://sandbox.pismolabs.io/merchants`
- **Tags:** `Merchant`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> List the status transitions using the merchant ID.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Content-Type` | header | no | string | Content type | example: "application/json" |
| `Authorization` | header | no | string | Authorization token. This is a regular access token, which does not need to include an account ID. | example: "Bearer 1JI12J39182H39182JDIOAWJ%=" |
| `merchantId` | path | yes | integer | Merchant ID | format: "int64"; example: 1 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: array of string (schema `MerchantWorkflowStatus`) |
| 400 | Bad Request |  |
| 401 | Access token is missing or invalid |  |
| 500 | Internal server error |  |

##### Response 200

**200 `application/json` body fields:**

_No fields declared in the schema._


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;500`, has examples `False`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Seller_management_-_Merchants.yaml method=PUT path=/v1/merchants/{merchantId}/workflow/status operationId=updateMerchantStatus -->
### `PUT /v1/merchants/{merchantId}/workflow/status` — Update merchant status

- **operationId:** `updateMerchantStatus`
- **Specification:** `api-specs/Seller_management_-_Merchants.yaml` (Seller management - Merchants)
- **Server base URL(s):** `https://sandbox.pismolabs.io/merchants`
- **Tags:** `Merchant`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Update merchant status using the merchant ID.
>
> To find all available merchant status transitions, use [List status transitions](ref:liststatustransitions).
>
> This endpoint generates a [Merchant updated](https://developers.pismo.io/events/docs/merchants-merchant-updated-1) event.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Content-Type` | header | no | string | Content type | example: "application/json" |
| `Authorization` | header | no | string | Authorization token. This is a regular access token, which does not need to include an account ID. | example: "Bearer 1JI12J39182H39182JDIOAWJ%=" |
| `merchantId` | path | yes | integer | Merchant ID | format: "int64"; example: 1 |

#### Request body

Required: yes

> Request body

**Content type `application/json`** — schema: object

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `status` | string (schema `MerchantStatus`) | yes | Merchant status. This is a string, not an enum, so any string value is allowed, but the most commonly used values are: 'ACTIVE', 'ANALYSING', 'APPROVED', 'CANCELLED', 'PENDING', 'REJECTED' | minLength: 1; maxLength: 128; example: "APPROVED" |
| `notes` | string (schema `OperationNotes`) | no | Notes about the operation.<br><br><b>Note</b>: This field is <b>deprecated</b> and scheduled for removal.<br> | deprecated: true; example: "This is a status change." |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK |  |
| 400 | Bad Request |  |
| 401 | Access token is missing or invalid |  |
| 500 | Internal server error |  |


#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `merchants-merchant-updated-1` | https://developers.pismo.io/events/docs/merchants-merchant-updated-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;500`, has examples `False`, emits events `1`, deprecated `False`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/POSTMerchantCreditorRequest -->
### Schema `POSTMerchantCreditorRequest`

Pointer: `#/components/schemas/POSTMerchantCreditorRequest`. Type: object (schema `POSTMerchantCreditorRequest`).

> This is the entity from which the merchant receives money when a transaction is settled.
> It should be a Pismo account.
>
> You can either provide an `id` to create a merchant with an already existing creditor, or fill in the creditor fields to create a new creditor for the created merchant.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `name` | string (schema `CreditorName`) | yes | Creditor name | minLength: 1; maxLength: 100; example: "Acme Corporation" |
| `id` | integer (schema `CreditorID`) | no | Creditor ID | format: "int64"; example: 1 |
| `crediting_method` | string (schema `CreditingMethod`) | no | Crediting method. Must be set to `ACCOUNT`.<br> | enum: ["ACCOUNT"]; example: "ACCOUNT" |
| `advancement_fee` | string (schema `AdvancementFeeInRequestMerchant`) | no | Advancement fee for creditor. If you don't specify a value for this field, the server tries to retrieve the value from the <b>Fixed fee applied to the<br>advancement transaction</b> parameter for the provided `program_id` in the Pismo console. If the `program_id` is not provided or the parameter is disabled,<br>the server uses the default value of `10`.<br> | default: "10"; example: "30.00" |
| `discount_rate` | string (schema `CreditorDiscountRateMerchant`) | no | Advancement discount rate for creditor. If the client doesn't provide a value for this field, the server tries to retrieve the value from the <b>Percentage rate over the anticipated gross amount</b> parameter for the provided `program_id` in the Pismo console.<br>If the `program_id` of the merchant is not found or the parameter is disabled, the server uses the default value of `0.025`.<br> | default: "0.025"; example: "0.03" |
| `maximum_advancement_percentage` | string (schema `MaximumAdvancementPercentageMerchant`) | no | Maximum advancement percentage for creditor. If the client didn't provide a value for this field, the server tries to retrieve the value from the <b>Max percentage that can be anticipated</b> parameter for the provided `program_id` in the Pismo console.<br>  If the `program_id` of the merchant is not found or the parameter is disabled, the server uses the default value of `1`.<br> | default: "1"; example: "0.80" |

<!-- schema: #/components/schemas/MerchantCreditorResponse -->
### Schema `MerchantCreditorResponse`

Pointer: `#/components/schemas/MerchantCreditorResponse`. Type: object (schema `MerchantCreditorResponse`).

> Get response from merchant creditor.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | integer (schema `CreditorID`) | no | Creditor ID | format: "int64"; example: 1 |
| `name` | string (schema `CreditorName`) | no | Creditor name | minLength: 1; maxLength: 100; example: "Acme Corporation" |
| `crediting_method` | string (schema `CreditingMethod`) | no | Crediting method. Must be set to `ACCOUNT`.<br> | enum: ["ACCOUNT"]; example: "ACCOUNT" |
| `account` | object | no | Pismo platform account |  |
| `account.id` | integer (schema `PismoAccountID`) | no | Pismo account ID | format: "int64"; example: 8675309 |
| `advancement_fee` | string (schema `AdvancementFeeInRequest`) | no | Advancement fee for creditor.<br> | default: "10"; example: "30.00" |
| `discount_rate` | string (schema `CreditorDiscountRate`) | no | Advancement discount rate for creditor.<br> | default: "0.025"; example: "0.03" |
| `maximum_advancement_percentage` | string (schema `MaximumAdvancementPercentage`) | no | Maximum advancement percentage for creditor.<br> | default: "1"; example: "0.80" |

<!-- schema: #/components/schemas/PUTMerchantCreditorRequest -->
### Schema `PUTMerchantCreditorRequest`

Pointer: `#/components/schemas/PUTMerchantCreditorRequest`. Type: object (schema `PUTMerchantCreditorRequest`).

> This is the entity from which the merchant receives money when a transaction is settled.
> It should be a Pismo account.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | integer (schema `CreditorID`) | no | Creditor ID | format: "int64"; example: 1 |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Seller_management_-_Merchants.yaml` | tag `Merchant`: GET /v1/merchants, POST /v1/merchants, GET /v1/merchants/{merchantId}, PUT /v1/merchants/{merchantId}, GET /v1/merchants/{merchantId}/workflow/statuses, PUT /v1/merchants/{merchantId}/workflow/status | https://github.com/PismoDevEx/pismo-api-specs | `ebc9f3fadda7001c…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-EVT-catalogue-merchants` — Event catalogue: merchants
- `KU-GS-get-started-with-pismo-apis` — Get started with Pismo APIs
- `KU-SELL-get-started-seller-management` — Get started with seller management
- `KU-SELL-managing-merchant-transactions` — Managing merchant transactions
- `KU-SELL-seller-management-overview-and-onboarding` — Seller management overview and onboarding
- `KU-SELL-seller-marketplace-implementation-steps` — Seller marketplace implementation steps 1 to 6
