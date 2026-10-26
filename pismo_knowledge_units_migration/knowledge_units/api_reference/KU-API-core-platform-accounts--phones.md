---
ku_id: KU-API-core-platform-accounts--phones
title: 'API reference: Core platform - Accounts — Phones'
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
- get-accounts-v1-accounts-accountId-phones
- post-accounts-v1-accounts-accountId-phones
- get-accounts-v1-accounts-accountId-phones-phoneId
- patch-accounts-v1-accounts-accountId-phones-phoneId
related_kus:
- KU-EVT-accounts-data-events
- KU-EVT-catalogue-audit
specification_version: 1.0.0
---

# API reference: Core platform - Accounts — Phones

**KU ID:** `KU-API-core-platform-accounts--phones` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 4 operation(s) tagged `Phones` in `api-specs/Core_platform_-_Accounts.yaml` (“Core platform - Accounts”, version `1.0.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Endpoints to manage phones

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `GET /accounts/v1/accounts/{accountId}/phones` | `get-accounts-v1-accounts-accountId-phones` | List phones | no |
| `POST /accounts/v1/accounts/{accountId}/phones` | `post-accounts-v1-accounts-accountId-phones` | Create phone | no |
| `GET /accounts/v1/accounts/{accountId}/phones/{phoneId}` | `get-accounts-v1-accounts-accountId-phones-phoneId` | Get phone | no |
| `PATCH /accounts/v1/accounts/{accountId}/phones/{phoneId}` | `patch-accounts-v1-accounts-accountId-phones-phoneId` | Update phone | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"}

## Operation contracts

<!-- op: spec=api-specs/Core_platform_-_Accounts.yaml method=GET path=/accounts/v1/accounts/{accountId}/phones operationId=get-accounts-v1-accounts-accountId-phones -->
### `GET /accounts/v1/accounts/{accountId}/phones` — List phones

- **operationId:** `get-accounts-v1-accounts-accountId-phones`
- **Specification:** `api-specs/Core_platform_-_Accounts.yaml` (Core platform - Accounts)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Phones`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> List an account's phone numbers with filtering options.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `accountId` | path | yes | integer | Account ID | format: "int64"; minimum: 1; example: 123 |
| `type` | query | no | string | Account phone type | enum: ["RESIDENTIAL", "MOBILE", "COMMERCIAL"]; example: "RESIDENTIAL" |
| `active` | query | no | boolean | Filter results based on whether the phone is active or not. | enum: [false, true]; example: true |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Phone numbers list | `application/json`: array of object (schema `PhoneItemResponse`) |
| 500 | Internal server error | `application/json`: object (schema `SimpleError`) |

##### Response 200

**200 `application/json` body fields:**

_No fields declared in the schema._

200 Example `Phone list`:

```json
[
  {
    "area_code": "11",
    "number": "912345678",
    "type": "MOBILE",
    "extension": "ext 123",
    "active": true,
    "country_code": "55",
    "creation_date": "2022-01-01T01:01:01Z",
    "last_update": "2022-02-02T02:02:02Z",
    "customer_id": 1
  }
]
```

##### Response 500

500 Example `Internal server error`:

```json
{
  "message": "Error retrieving phone list"
}
```


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;500`, has examples `True`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Core_platform_-_Accounts.yaml method=POST path=/accounts/v1/accounts/{accountId}/phones operationId=post-accounts-v1-accounts-accountId-phones -->
### `POST /accounts/v1/accounts/{accountId}/phones` — Create phone

- **operationId:** `post-accounts-v1-accounts-accountId-phones`
- **Specification:** `api-specs/Core_platform_-_Accounts.yaml` (Core platform - Accounts)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Phones`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Create a new phone number for the specified account.
>
> This event generates a [Phone created](https://developers.pismo.io/events/docs/audit-phone-creation-1) event.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `accountId` | path | yes | integer | Account ID | format: "int64"; minimum: 1; example: 123 |
| `x-customer-id` | header | no | integer |  | format: "int64"; example: 50624 |

#### Request body

Required: yes

> Phone entity

**Content type `application/json`** — schema: object (schema `PhoneRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `number` | string (schema `PhoneNumber`) | yes | Phone number | maxLength: 15; example: "11912345678" |
| `type` | string (schema `PhoneType`) | yes | Phone number type | enum: ["RESIDENTIAL", "COMMERCIAL", "MOBILE"]; example: "MOBILE" |
| `active` | boolean (schema `PhoneActive`) | no | Is phone active? Default is `true`. | example: false |
| `area_code` | integer (schema `AreaCode2`) | no | Phone number area code | format: "int32"; example: 11 |
| `country_code` | string (schema `PhoneCountryCode`) | no | Phone number's country code | maxLength: 5; example: "555" |
| `extension` | string (schema `PhoneExtension`) | no | Optional phone number extension | maxLength: 10; example: "ext. 9" |

Example `Phone number`:

```json
{
  "area_code": 11,
  "number": "91234-5678",
  "type": "MOBILE",
  "extension": "ext 123",
  "active": true
}
```

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | The phone was successfully created | `application/json`: object |
| 400 | Bad Request | `application/json`: object (schema `BadRequestError`) |
| 409 | Conflict | `application/json`: object (schema `SimpleError`) |
| 500 | Internal server error | `application/json`: object (schema `SimpleError`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | integer (schema `PhoneID`) | yes | Phone ID | format: "int64"; example: 8714 |

##### Response 409

409 Example `Duplicated phone number`:

```json
{
  "message": "Phone number already exists"
}
```

##### Response 500

500 Example `Internal server error`:

```json
{
  "message": "Error creating phone number"
}
```


#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `audit-phone-creation-1` | https://developers.pismo.io/events/docs/audit-phone-creation-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;409;500`, has examples `True`, emits events `1`, deprecated `False`.

Guides that link to this operation: `KU-EVT-accounts-data-events`.

<!-- op: spec=api-specs/Core_platform_-_Accounts.yaml method=GET path=/accounts/v1/accounts/{accountId}/phones/{phoneId} operationId=get-accounts-v1-accounts-accountId-phones-phoneId -->
### `GET /accounts/v1/accounts/{accountId}/phones/{phoneId}` — Get phone

- **operationId:** `get-accounts-v1-accounts-accountId-phones-phoneId`
- **Specification:** `api-specs/Core_platform_-_Accounts.yaml` (Core platform - Accounts)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Phones`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

>
> Get a phone number.
>
> To get a list of phone IDs, call [List phones](ref:get-accounts-v1-accounts-accountid-phones).

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `accountId` | path | yes | integer | Account ID | format: "int64"; minimum: 1; example: 123 |
| `phoneId` | path | yes | integer | Phone ID | format: "int64"; minimum: 1; example: 456 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Ok | `application/json`: object (schema `PhoneItemResponse`) |
| 500 | Internal server error | `application/json`: object (schema `SimpleError`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | integer (schema `PhoneID`) | no | Phone ID | format: "int64"; example: 8714 |
| `account_id` | integer (schema `AccountID`) | no | Account ID | format: "int64"; example: 1001 |
| `area_code` | string (schema `AreaCode`) | no | Phone number area code | maxLength: 2; example: "51" |
| `number` | string (schema `PhoneNumber`) | no | Phone number | maxLength: 15; example: "11912345678" |
| `type` | string (schema `PhoneType`) | no | Phone number type | enum: ["RESIDENTIAL", "COMMERCIAL", "MOBILE"]; example: "MOBILE" |
| `extension` | string (schema `PhoneExtension`) | no | Optional phone number extension | maxLength: 10; example: "ext. 9" |
| `active` | boolean (schema `PhoneActive`) | no | Is phone active? Default is `true`. | example: false |
| `org_id` | string (schema `OrganizationID`) | no | Organization ID | example: "TN-34778262-f4f0-464d-b4c6-a14e2dc6f4be" |
| `country_code` | string (schema `PhoneCountryCode`) | no | Phone number's country code | maxLength: 5; example: "555" |
| `creation_date` | string (schema `PhoneDate`) | no | Phone date creation. RFC 3339 format. | format: "date-time"; example: "2021-10-21T00:00:00Z" |
| `last_update` | string (schema `PhoneLastUpdate`) | no | Date of last phone update | format: "date-time"; example: "2021-10-21T00:00:00Z" |
| `customer_id` | integer (schema `CustomerID`) | no | Customer ID | format: "int64"; example: 100211299 |

200 Example `Phone number`:

```json
{
  "area_code": "11",
  "number": "91234-5678",
  "type": "MOBILE",
  "extension": "ext 123",
  "active": true,
  "country_code": "55",
  "creation_date": "2022-01-01T01:01:01Z",
  "last_update": "2022-02-02T02:02:02Z",
  "customer_id": 1
}
```

##### Response 500

500 Example `Internal server error`:

```json
{
  "message": "Error retrieving phone number"
}
```


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;500`, has examples `True`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Core_platform_-_Accounts.yaml method=PATCH path=/accounts/v1/accounts/{accountId}/phones/{phoneId} operationId=patch-accounts-v1-accounts-accountId-phones-phoneId -->
### `PATCH /accounts/v1/accounts/{accountId}/phones/{phoneId}` — Update phone

- **operationId:** `patch-accounts-v1-accounts-accountId-phones-phoneId`
- **Specification:** `api-specs/Core_platform_-_Accounts.yaml` (Core platform - Accounts)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Phones`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Update phone number.
>
> This event generates a [Phone updated](https://developers.pismo.io/events/docs/audit-phone-change-1) event.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `accountId` | path | yes | integer | Account ID | format: "int64"; minimum: 1; example: 123 |
| `phoneId` | path | yes | integer | Phone ID | format: "int64"; minimum: 1; example: 456 |

#### Request body

Required: yes

> Phone entity

**Content type `application/json`** — schema: object (schema `PhoneUpdateRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `area_code` | integer (schema `AreaCode2`) | no | Phone number area code | format: "int32"; example: 11 |
| `number` | string (schema `PhoneNumber`) | no | Phone number | maxLength: 15; example: "11912345678" |
| `type` | string (schema `PhoneType`) | no | Phone number type | enum: ["RESIDENTIAL", "COMMERCIAL", "MOBILE"]; example: "MOBILE" |
| `extension` | string (schema `PhoneExtension`) | no | Optional phone number extension | maxLength: 10; example: "ext. 9" |
| `active` | boolean (schema `PhoneActive`) | no | Is phone active? Default is `true`. | example: false |
| `country_code` | string (schema `PhoneCountryCode`) | no | Phone number's country code | maxLength: 5; example: "555" |

Example `Inactivate phone`:

```json
{
  "active": false
}
```

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Phone was successfully updated | `application/json`: object |
| 400 |  | `application/json`: object (schema `BadRequestError`) |
| 422 | Precondition failed | `application/json`: object (schema `SimpleError`) |
| 500 | Internal server error | `application/json`: object (schema `SimpleError`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | integer (schema `PhoneID`) | yes | Phone ID | format: "int64"; example: 8714 |

##### Response 422

422 Example `Inactive phone`:

```json
{
  "message": "Can't update an inactive phone number"
}
```

##### Response 500

500 Example `Internal server error`:

```json
{
  "message": "Error updating phone number"
}
```


#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `audit-phone-change-1` | https://developers.pismo.io/events/docs/audit-phone-change-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;422;500`, has examples `True`, emits events `1`, deprecated `False`.

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
| `api-specs/Core_platform_-_Accounts.yaml` | tag `Phones`: GET /accounts/v1/accounts/{accountId}/phones, POST /accounts/v1/accounts/{accountId}/phones, GET /accounts/v1/accounts/{accountId}/phones/{phoneId}, PATCH /accounts/v1/accounts/{accountId}/phones/{phoneId} | https://github.com/PismoDevEx/pismo-api-specs | `3c621106abf11d41…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-EVT-accounts-data-events` — Core platform - Accounts
- `KU-EVT-catalogue-audit` — Event catalogue: audit
