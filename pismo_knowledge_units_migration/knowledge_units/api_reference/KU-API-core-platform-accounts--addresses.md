---
ku_id: KU-API-core-platform-accounts--addresses
title: 'API reference: Core platform - Accounts — Addresses'
category: api_reference
ku_type: api_reference
lifecycle: current
sources:
- path: api-specs/Core_platform_-_Accounts.yaml
  sha256: 3c621106abf11d41435170a356ae695e023a5d963bdb0b1e8772209bf0b88c49
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
- get-accounts-v1-accounts-accountId-addresses
- post-accounts-v1-accounts-accountId-addresses
- get-accounts-v1-accounts-accountId-addresses-addressId
- patch-accounts-v1-accounts-accountId-addresses-addressId
related_kus:
- KU-EVT-accounts-data-events
- KU-EVT-catalogue-audit
specification_version: 1.0.0
---

# API reference: Core platform - Accounts — Addresses

**KU ID:** `KU-API-core-platform-accounts--addresses` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 4 operation(s) tagged `Addresses` in `api-specs/Core_platform_-_Accounts.yaml` (“Core platform - Accounts”, version `1.0.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Endpoints to manage addresses

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `GET /accounts/v1/accounts/{accountId}/addresses` | `get-accounts-v1-accounts-accountId-addresses` | List addresses | no |
| `POST /accounts/v1/accounts/{accountId}/addresses` | `post-accounts-v1-accounts-accountId-addresses` | Create address | no |
| `GET /accounts/v1/accounts/{accountId}/addresses/{addressId}` | `get-accounts-v1-accounts-accountId-addresses-addressId` | Get address | no |
| `PATCH /accounts/v1/accounts/{accountId}/addresses/{addressId}` | `patch-accounts-v1-accounts-accountId-addresses-addressId` | Update address | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"}

## Operation contracts

<!-- op: spec=api-specs/Core_platform_-_Accounts.yaml method=GET path=/accounts/v1/accounts/{accountId}/addresses operationId=get-accounts-v1-accounts-accountId-addresses -->
### `GET /accounts/v1/accounts/{accountId}/addresses` — List addresses

- **operationId:** `get-accounts-v1-accounts-accountId-addresses`
- **Specification:** `api-specs/Core_platform_-_Accounts.yaml` (Core platform - Accounts)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Addresses`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> List addresses defined for the specified account.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `accountId` | path | yes | integer | Account ID | format: "int64"; minimum: 1; example: 123 |
| `active` | query | no | boolean | Filter results based on whether the address is active or inactive. | enum: [false, true]; example: true |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Ok | `application/json`: array of object (schema `AddressItemResponse`) |
| 500 | Internal server error | `application/json`: object (schema `SimpleError`) |

##### Response 200

**200 `application/json` body fields:**

_No fields declared in the schema._

200 Example `Address list`:

```json
[
  {
    "zip_code": "18047620",
    "country": "BRA",
    "address": "Avenida Antônio Carlos Comitre",
    "city": "Sorocaba",
    "address_type": "COMMERCIAL",
    "active": true,
    "creation_date": "2023-04-06T20:24:49Z",
    "org_id": "TN-02b1acbb-9fe3-45e4-8b20-f3afaf0b2970",
    "number": 1393,
    "account_id": 115203987,
    "complementary_address": "null",
    "mailing_address": true,
    "last_update": "2019-07-22T14:35:00.000Z",
    "customer_ids": "null",
    "id": 32670165,
    "neighborhood": "Faraway Creek",
    "state": "SP"
  }
]
```

##### Response 500

500 Example `Internal server error`:

```json
{
  "message": "Not possible to find all addresses"
}
```


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;500`, has examples `True`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Core_platform_-_Accounts.yaml method=POST path=/accounts/v1/accounts/{accountId}/addresses operationId=post-accounts-v1-accounts-accountId-addresses -->
### `POST /accounts/v1/accounts/{accountId}/addresses` — Create address

- **operationId:** `post-accounts-v1-accounts-accountId-addresses`
- **Specification:** `api-specs/Core_platform_-_Accounts.yaml` (Core platform - Accounts)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Addresses`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Create a new address for the specified account.
>
> This endpoint generates an [Address created](https://developers.pismo.io/events/docs/audit-address-creation-1) event.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `accountId` | path | yes | integer | Account ID | format: "int64"; minimum: 1; example: 123 |

#### Request body

Required: yes

> Address entity

**Content type `application/json`** — schema: object (schema `AddressItemRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `type` | string (schema `AddressType`) | yes | Address type | enum: ["RESIDENTIAL", "COMMERCIAL", "OTHER"]; example: "RESIDENTIAL" |
| `address` | string (schema `Address`) | yes | Street, avenue, road, and so on, name. | maxLength: 300; example: "Mulholland Drive" |
| `number` | string (schema `AddressNumberInput`) | yes | Address number as string or integer.<br><br>If you enter numeric characters, they are saved in the `number` address object field.<br><br>If you enter any non-numeric characters, all characters are saved in the `extended_number` address object field.<br><br>For example, if you enter "12 A", it gets saved as follows:<br>  *  `number` = 12<br>  *  `extended_number` = "12 A"<br> | maxLength: 9 |
| `zip_code` | string (schema `ZipCode`) | yes | Zip/postal code | maxLength: 16; example: "12345-678" |
| `city` | string (schema `City`) | yes | Address city | maxLength: 100; example: "San Diego" |
| `state` | string (schema `State`) | yes | Address state | maxLength: 30; example: "California" |
| `country` | string (schema `Country`) | yes | Address country | maxLength: 30; example: "Brazil" |
| `neighborhood` | string (schema `Neighborhood`) | yes | Address neighborhood. Some countries use neighborhood in addresses. | maxLength: 100; example: "Shady Pines" |
| `active` | boolean (schema `AddressActive`) | no | Is address active? Default is `false`. | default: false; example: true |
| `complementary_address` | string (schema `ComplementaryAddress`) | no | Any additional information such as suite, apt., and so on. | maxLength: 100; example: "Apt 1408" |
| `custom_fields` | object (schema `CustomFields`) | no | Key/value field for custom information. (Limited to 1014 bytes.) | example: {"field_01": "value01", "field_02": "value02"} |
| `mailing_address` | boolean (schema `MailingAddress`) | no | Is this address the mailing address?<br><br>Only one address can have this field set to `true`.<br> | example: true |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | The address was successfully created | `application/json`: object |
| 400 | Bad request | `application/json`: object (schema `BadRequestError`) |
| 500 | Internal server error | `application/json`: object (schema `SimpleError`) |

##### Response 201

**201 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | integer | no |  | format: "int64"; example: 1472162 |

##### Response 400

400 Example `Bad payload`:

```json
{
  "message": "Field should be boolean",
  "field": "mailing_address"
}
```

##### Response 500

500 Example `Internal server error`:

```json
{
  "message": "Not possible to create the address"
}
```


#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `audit-address-creation-1` | https://developers.pismo.io/events/docs/audit-address-creation-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `201;400;500`, has examples `True`, emits events `1`, deprecated `False`.

Guides that link to this operation: `KU-EVT-accounts-data-events`.

<!-- op: spec=api-specs/Core_platform_-_Accounts.yaml method=GET path=/accounts/v1/accounts/{accountId}/addresses/{addressId} operationId=get-accounts-v1-accounts-accountId-addresses-addressId -->
### `GET /accounts/v1/accounts/{accountId}/addresses/{addressId}` — Get address

- **operationId:** `get-accounts-v1-accounts-accountId-addresses-addressId`
- **Specification:** `api-specs/Core_platform_-_Accounts.yaml` (Core platform - Accounts)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Addresses`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Get address information using an account ID and address ID.
>
> To get a list of address IDs, call [List addresses](ref:get-accounts-v1-accounts-accountid-addresses).

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `accountId` | path | yes | integer | Account ID | format: "int64"; minimum: 1; example: 123 |
| `addressId` | path | yes | integer | Address ID | format: "int64"; minimum: 1; example: 456 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `AddressResponse`) |
| 400 | Bad request | `application/json`: object (schema `SimpleError`) |
| 404 | Address not found or inactive for the given account. | `application/json`: object (schema `SimpleError`) |
| 500 | Internal server error | `application/json`: object (schema `SimpleError`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | integer (schema `AddressID`) | no | Address ID | format: "int32"; example: 456 |
| `address_type` | string (schema `AddressType`) | no | Address type | enum: ["RESIDENTIAL", "COMMERCIAL", "OTHER"]; example: "RESIDENTIAL" |
| `address` | string (schema `Address`) | no | Street, avenue, road, and so on, name. | maxLength: 300; example: "Mulholland Drive" |
| `number` | integer (schema `AddressNumber`) | no | Address number with numeric characters only | format: "int32"; example: 456 |
| `extended_number` | string (schema `AddressExtendedNumber`) | no | Address number with numeric and non-numeric characters | example: "456 B" |
| `complementary_address` | string (schema `ComplementaryAddress`) | no | Any additional information such as suite, apt., and so on. | maxLength: 100; example: "Apt 1408" |
| `neighborhood` | string (schema `Neighborhood`) | no | Address neighborhood. Some countries use neighborhood in addresses. | maxLength: 100; example: "Shady Pines" |
| `zip_code` | string (schema `ZipCode`) | no | Zip/postal code | maxLength: 16; example: "12345-678" |
| `city` | string (schema `City`) | no | Address city | maxLength: 100; example: "San Diego" |
| `state` | string (schema `State`) | no | Address state | maxLength: 30; example: "California" |
| `country` | string (schema `Country`) | no | Address country | maxLength: 30; example: "Brazil" |
| `creation_date` | string (schema `CustomerAddressDate`) | no | Date customer first acquired this address. Format = dd/mm/yyyy. | example: "15/05/2022" |
| `mailing_address` | boolean (schema `MailingAddress`) | no | Is this address the mailing address?<br><br>Only one address can have this field set to `true`.<br> | example: true |
| `active` | boolean (schema `AddressActive`) | no | Is address active? Default is `false`. | default: false; example: true |
| `org_id` | string (schema `OrganizationID`) | no | Organization ID | example: "TN-34778262-f4f0-464d-b4c6-a14e2dc6f4be" |
| `account_id` | integer (schema `AccountID`) | no | Account ID | format: "int64"; example: 1001 |
| `last_update` | string (schema `AddressLastUpdate`) | no | UTC date/time when address was last updated. Format = yyyy-mm-dd:hr:mm:ss. | format: "date-time"; example: "2019-07-22T14:35:00.000Z" |
| `custom_fields` | object (schema `CustomFields`) | no | Key/value field for custom information. (Limited to 1014 bytes.) | example: {"field_01": "value01", "field_02": "value02"} |
| `customer_ids` | array of integer (schema `CustomerID`) | no | Customer IDs linked to this address. | items.format: "int64" |

##### Response 400

400 Example `Invalid path parameter`:

```json
{
  "message": "Invalid request"
}
```

##### Response 404

404 Example `Not found`:

```json
{
  "message": "Address not found for this account"
}
```

##### Response 500

500 Example `Invalid path parameter`:

```json
{
  "message": "Invalid request"
}
```


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;404;500`, has examples `True`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Core_platform_-_Accounts.yaml method=PATCH path=/accounts/v1/accounts/{accountId}/addresses/{addressId} operationId=patch-accounts-v1-accounts-accountId-addresses-addressId -->
### `PATCH /accounts/v1/accounts/{accountId}/addresses/{addressId}` — Update address

- **operationId:** `patch-accounts-v1-accounts-accountId-addresses-addressId`
- **Specification:** `api-specs/Core_platform_-_Accounts.yaml` (Core platform - Accounts)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Addresses`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Update an address.
>
> This endpoint generates an [Address updated](https://developers.pismo.io/events/docs/audit-address-change-1) event.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `accountId` | path | yes | integer | Account ID | format: "int64"; minimum: 1; example: 123 |
| `addressId` | path | yes | integer | Address ID | format: "int64"; minimum: 1; example: 456 |

#### Request body

Required: yes

> Address entity

**Content type `application/json`** — schema: object (schema `AddressUpdateRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `type` | string (schema `AddressType`) | no | Address type | enum: ["RESIDENTIAL", "COMMERCIAL", "OTHER"]; example: "RESIDENTIAL" |
| `address` | string (schema `Address`) | no | Street, avenue, road, and so on, name. | maxLength: 300; example: "Mulholland Drive" |
| `number` | string (schema `AddressNumberInput`) | no | Address number as string or integer.<br><br>If you enter numeric characters, they are saved in the `number` address object field.<br><br>If you enter any non-numeric characters, all characters are saved in the `extended_number` address object field.<br><br>For example, if you enter "12 A", it gets saved as follows:<br>  *  `number` = 12<br>  *  `extended_number` = "12 A"<br> | maxLength: 9 |
| `neighborhood` | string (schema `Neighborhood`) | no | Address neighborhood. Some countries use neighborhood in addresses. | maxLength: 100; example: "Shady Pines" |
| `zip_code` | string (schema `ZipCode`) | no | Zip/postal code | maxLength: 16; example: "12345-678" |
| `city` | string (schema `City`) | no | Address city | maxLength: 100; example: "San Diego" |
| `state` | string (schema `State`) | no | Address state | maxLength: 30; example: "California" |
| `country` | string (schema `Country`) | no | Address country | maxLength: 30; example: "Brazil" |
| `active` | boolean (schema `AddressActive`) | no | Is address active? Default is `false`. | default: false; example: true |
| `mailing_address` | boolean (schema `MailingAddress`) | no | Is this address the mailing address?<br><br>Only one address can have this field set to `true`.<br> | example: true |
| `complementary_address` | string (schema `ComplementaryAddress`) | no | Any additional information such as suite, apt., and so on. | maxLength: 100; example: "Apt 1408" |
| `custom_fields` | object (schema `CustomFields`) | no | Key/value field for custom information. (Limited to 1014 bytes.) | example: {"field_01": "value01", "field_02": "value02"} |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | The address was successfully updated | `application/json`: object |
| 500 | Internal server error | `application/json`: object (schema `SimpleError`) |

##### Response 201

**201 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | integer (schema `AddressID`) | no | Address ID | format: "int32"; example: 456 |

##### Response 500

500 Example `Internal server error`:

```json
{
  "message": "Error updating address"
}
```


#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `audit-address-change-1` | https://developers.pismo.io/events/docs/audit-address-change-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `201;500`, has examples `True`, emits events `1`, deprecated `False`.

Guides that link to this operation: `KU-EVT-accounts-data-events`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/SimpleError -->
### Schema `SimpleError`

Pointer: `#/components/schemas/SimpleError`. Type: object (schema `SimpleError`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `message` | string | yes | Error message |  |

<!-- schema: #/components/schemas/BadRequestError -->
### Schema `BadRequestError`

Pointer: `#/components/schemas/BadRequestError`. Type: object (schema `BadRequestError`).

> Bad request error

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `message` | string | yes | Message describing the error |  |
| `field` | string | yes | Text identifying the ill-formatted field |  |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Core_platform_-_Accounts.yaml` | tag `Addresses`: GET /accounts/v1/accounts/{accountId}/addresses, POST /accounts/v1/accounts/{accountId}/addresses, GET /accounts/v1/accounts/{accountId}/addresses/{addressId}, PATCH /accounts/v1/accounts/{accountId}/addresses/{addressId} | https://github.com/PismoDevEx/pismo-api-specs | `3c621106abf11d41…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-EVT-accounts-data-events` — Core platform - Accounts
- `KU-EVT-catalogue-audit` — Event catalogue: audit
