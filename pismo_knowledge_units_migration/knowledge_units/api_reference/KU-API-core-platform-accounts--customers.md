---
ku_id: KU-API-core-platform-accounts--customers
title: 'API reference: Core platform - Accounts — Customers'
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
- customerV2Post
- customersV2Get
- customerV2Get
- customerV2Put
- customerV1patch
related_kus:
- KU-BANK-banking-as-a-service
- KU-CARD-implementation-steps
- KU-CORE-accounts-overview
- KU-EVT-accounts-data-events
- KU-EVT-catalogue-account
- KU-EVT-catalogue-audit
- KU-GS-program-types
- KU-GS-setup-overview
specification_version: 1.0.0
---

# API reference: Core platform - Accounts — Customers

**KU ID:** `KU-API-core-platform-accounts--customers` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 5 operation(s) tagged `Customers` in `api-specs/Core_platform_-_Accounts.yaml` (“Core platform - Accounts”, version `1.0.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Endpoints to manage customers

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `POST /accounts/v2/customers` | `customerV2Post` | Create customer | no |
| `GET /accounts/v2/accounts/{accountId}/customers` | `customersV2Get` | List customers | no |
| `GET /accounts/v2/customers/{customerId}` | `customerV2Get` | Get customer | no |
| `PUT /accounts/v2/customers/{customerId}` | `customerV2Put` | Overwrite customer | no |
| `PATCH /accounts/v1/accounts/{accountId}/customers/{customerId}/detail` | `customerV1patch` | Update person or company customer | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"}

## Operation contracts

<!-- op: spec=api-specs/Core_platform_-_Accounts.yaml method=POST path=/accounts/v2/customers operationId=customerV2Post -->
### `POST /accounts/v2/customers` — Create customer

- **operationId:** `customerV2Post`
- **Specification:** `api-specs/Core_platform_-_Accounts.yaml` (Core platform - Accounts)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Customers`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Create a new account customer.
>
> There are 3 customer types you can create with this endpoint: a `company` customer, a `person` customer, or a person customer with less informational fields (`customer` object).
>
> Each account contains at least one customer. You can add multiple customers to an account but only one can be the account owner. Other customers can have their own individual cards, but the balances on those cards must be shared with the account owner.
>
> This endpoint generates a [Customer created](https://developers.pismo.io/events/docs/account-customer-creation-1) event.
>
> If the `customer.is_owner` property is set to `true`:
>
> * The account owner is changed to this new customer, and all existing customers remain active in the account.
> * This endpoint generates an [Account owner changed](https://developers.pismo.io/events/docs/account-account-owner-change-1) event.
>
> If the `customer.is_active` = `true`, and the `Maximum number of card holders` program parameter is set, this customer is counted in the limit of maximum number of card holders for an account.
>
> Each customer has an associated entity object. If one isn't passed in the request, a default one is created using their document number.
>
> Refer to the [Core objects](doc:setup-overview) guide for more information.

#### Request body

Required: yes

> Additional customer

**Content type `application/json`** — schema: object (schema `CustomerV2Request`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `account_id` | integer (schema `AccountID`) | yes | Account ID | format: "int64"; example: 1001 |
| `entity` | object | yes |  |  |
| `entity.name` | string (schema `EntityName`) | yes | Entity name | example: "Sam Smith" |
| `entity.document_number` | string (schema `DocumentNumber`) | yes | Document number, such as a government tax ID. | maxLength: 15; example: "31457828046" |
| `entity.birth_date` | string (schema `EntityBirthDate2`) | no | Entity birth date. Format = dd/MM/yyyy.<br><br>For individuals, this is their birth date. For companies, this is the business registration date.<br> | example: "15/01/1990" |
| `entity.gender` | string (schema `Gender`) | no | Gender | enum: ["F", "M", ""]; maxLength: 1; example: "M" |
| `entity.marital_status` | string (schema `MaritalStatus`) | no | Marital status | enum: ["SINGLE", "MARRIED", "DIVORCED", "WIDOWER"]; example: "MARRIED" |
| `entity.mothers_name` | string (schema `MothersName`) | no | Mother's name | maxLength: 60; example: "Kay Sadilla" |
| `entity.registration` | string (schema `EntityRegistration`) | no | Entity registration | example: "55555555" |
| `entity.pep` | boolean (schema `PEP`) | no | Is this person a Politically Exposed Person (PEP)? Pismo doesn't do anything differently for a PEP, this is just additional account information. Default is `false`.<br> | example: false |
| `entity.external_id` | string (schema `AccountExternalId`) | no | <br>Client-created ID from an external system or application. **REQUIRED** for `VIRTUAL` accounts.<br> | maxLength: 60; example: "8c8a4dd7-e48f-4c15-85b7-9d12f401057f" |
| `entity.person` | object (schema `Person2`) | no | Either this or the `company` object is **REQUIRED**. Pass one or the other but not both. |  |
| `entity.company` | object (schema `Company2`) | no |  |  |
| `customer` | object | yes |  |  |
| `customer.is_owner` | boolean (schema `IsOwner`) | yes | Is the customer the account owner? | example: false |
| `customer.email` | string (schema `IndividualsEmailAddress`) | no | Email address. | format: "email"; maxLength: 100; example: "jenna.flect@email.com" |
| `customer.printed_name` | string (schema `PrintedName`) | no | <br>This field is **DEPRECATED**.<br><br>Name to be printed on the card.<br><br>Punctuation, special characters, and connectors (da/das/de/do/dos/e) are always removed.<br><br>This field's maximum length is 25, but you can set it to a lower value at the program level with the `Max name length on physical card` program parameter.<br><br>If `printed_name` is null, the Pismo platform uses `social_name`. If `social_name` is null, the Pismo platform uses the customer's entity name. For more information on the customer object, refer to [Core objects](doc:setup-overview#customer).<br><br>The Pismo platform gets the name for program parameter `TAMANHO MAX NOME EMBOSSADO` (max size name embossed).<br> | maxLength: 25; deprecated: true; example: "Jack Williams" |
| `customer.social_name` | string (schema `SocialName`) | no | Social name. | maxLength: 64; example: "Jack" |
| `customer.nickname` | string (schema `Nickname`) | no | Nickname. | maxLength: 128; example: "Pinto" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | Account additional registration | `application/json`: oneOf: object (schema `CustomerV2Response`) |
| 400 | Bad request | `application/json`: object |
| 409 | Conflict | `application/json`: object |
| 500 | Internal server error | `application/json`: object |

##### Response 201

**201 `application/json` body fields:**

_No fields declared in the schema._

##### Response 400

400 Example `Empty is_owner`:

```json
{
  "message": "is_owner must not be empty",
  "field": "is_owner"
}
```

400 Example `Inactive_owner`:

```json
{
  "message": "New customer owner must not be inactive"
}
```

400 Example `Maximum Additional Customers`:

```json
{
  "message": "Exceeded maximum value of additional customers"
}
```


#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `account-account-owner-change-1` | https://developers.pismo.io/events/docs/account-account-owner-change-1 |
| `account-customer-creation-1` | https://developers.pismo.io/events/docs/account-customer-creation-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `201;400;409;500`, has examples `True`, emits events `2`, deprecated `False`.

Guides that link to this operation: `KU-BANK-banking-as-a-service`, `KU-CARD-implementation-steps`, `KU-CORE-accounts-overview`, `KU-EVT-accounts-data-events`, `KU-GS-program-types`, `KU-GS-setup-overview`.

<!-- op: spec=api-specs/Core_platform_-_Accounts.yaml method=GET path=/accounts/v2/accounts/{accountId}/customers operationId=customersV2Get -->
### `GET /accounts/v2/accounts/{accountId}/customers` — List customers

- **operationId:** `customersV2Get`
- **Specification:** `api-specs/Core_platform_-_Accounts.yaml` (Core platform - Accounts)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Customers`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> List account customers with filtering options.
>
> For each customer, the shorter `customer` object is returned. This object does not contain the additional informational fields provided for person or company customers.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `accountId` | path | yes | integer | Account ID | format: "int64"; minimum: 1; example: 123 |
| `page` | query | no | integer | Page number. | default: 1; format: "int32" |
| `perPage` | query | no | integer | Items per page | default: 10; format: "int32"; minimum: 1; maximum: 200 |
| `isOwner` | query | no | boolean | Is customer the account owner? | example: false |
| `entityId` | query | no | integer | ID of entity associated with the customer's information | format: "int64"; example: 12345 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Customer information associated with the given account | `application/json`: object |
| 404 | Not found | `application/json`: object (schema `SimpleError`) |
| 500 | Internal server error | `application/json`: object (schema `SimpleError`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `current_page` | integer (schema `CurrentPage`) | no | Current page | format: "int32"; example: 1 |
| `per_page` | integer (schema `PerPage`) | no | Maximum items per page. 100 maximum. | format: "int64"; example: 100 |
| `items` | array of object | no |  |  |
| `items[].account_id` | integer (schema `AccountID`) | no | Account ID | format: "int64"; example: 1001 |
| `items[].customer` | object | no |  |  |
| `items[].customer.id` | integer (schema `CustomerID`) | no | Customer ID | format: "int64"; example: 100211299 |
| `items[].customer.printed_name` | string (schema `PrintedName`) | no | <br>This field is **DEPRECATED**.<br><br>Name to be printed on the card.<br><br>Punctuation, special characters, and connectors (da/das/de/do/dos/e) are always removed.<br><br>This field's maximum length is 25, but you can set it to a lower value at the program level with the `Max name length on physical card` program parameter.<br><br>If `printed_name` is null, the Pismo platform uses `social_name`. If `social_name` is null, the Pismo platform uses the customer's entity name. For more information on the customer object, refer to [Core objects](doc:setup-overview#customer).<br><br>The Pismo platform gets the name for program parameter `TAMANHO MAX NOME EMBOSSADO` (max size name embossed).<br> | maxLength: 25; deprecated: true; example: "Jack Williams" |
| `items[].customer.social_name` | string (schema `SocialName`) | no | Social name. | maxLength: 64; example: "Jack" |
| `items[].customer.nickname` | string (schema `Nickname`) | no | Nickname. | maxLength: 128; example: "Pinto" |
| `items[].customer.is_owner` | boolean (schema `IsOwner`) | no | Is the customer the account owner? | example: false |
| `items[].customer.is_active` | boolean (schema `CustomerIsActive`) | no | Is customer active or not active? If `is_active` is null in this request, the Pismo platform doesn't overwrite the existing value. | example: true |

##### Response 404

404 Example `Account not found`:

```json
{
  "message": "Account not found"
}
```

##### Response 500

500 Example `Internal server error`:

```json
{
  "message": "Internal server error"
}
```


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;404;500`, has examples `True`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Core_platform_-_Accounts.yaml method=GET path=/accounts/v2/customers/{customerId} operationId=customerV2Get -->
### `GET /accounts/v2/customers/{customerId}` — Get customer

- **operationId:** `customerV2Get`
- **Specification:** `api-specs/Core_platform_-_Accounts.yaml` (Core platform - Accounts)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Customers`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Use the customer ID to get customer and associated entity details.
>
> To get a list of customer IDs, call [List account customers](ref:customersv2get).
>
> Depending on customer, either the `person`, `company`, or `customer` (less informational fields than `person`) object is returned.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `customerId` | path | yes | integer | Customer ID | format: "int64"; example: 12345 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Detailed customer and entity information associated with the given customer ID. | `application/json`: object |
| 404 | Not found | `application/json`: object (schema `SimpleError`) |
| 500 | Internal server error | `application/json`: object (schema `SimpleError`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `program_id` | integer (schema `ProgramID`) | no | Program ID | format: "int64"; example: 12345 |
| `account_id` | integer (schema `AccountID`) | no | Account ID | format: "int64"; example: 1001 |
| `entity` | object | no |  |  |
| `entity.id` | integer (schema `EntityID`) | no | Entity ID | format: "int64"; minimum: 1; example: 1234567891 |
| `entity.name` | string (schema `EntityName`) | no | Entity name | example: "Sam Smith" |
| `entity.document_number` | string (schema `DocumentNumber`) | no | Document number, such as a government tax ID. | maxLength: 15; example: "31457828046" |
| `entity.registration` | string (schema `EntityRegistration`) | no | Entity registration | example: "55555555" |
| `entity.birth_date` | string (schema `EntityBirthDate`) | no | Entity birth date. Format = yyyy-mm-dd.<br><br>For individuals, this is their birth date. For companies, this is the business registration date.<br> | format: "date"; example: "1990-12-31" |
| `entity.gender` | string (schema `Gender`) | no | Gender | enum: ["F", "M", ""]; maxLength: 1; example: "M" |
| `entity.mothers_name` | string (schema `MothersName`) | no | Mother's name | maxLength: 60; example: "Kay Sadilla" |
| `entity.marital_status` | string (schema `MaritalStatus`) | no | Marital status | enum: ["SINGLE", "MARRIED", "DIVORCED", "WIDOWER"]; example: "MARRIED" |
| `entity.pep` | boolean (schema `PEP`) | no | Is this person a Politically Exposed Person (PEP)? Pismo doesn't do anything differently for a PEP, this is just additional account information. Default is `false`.<br> | example: false |
| `entity.person` | object (schema `Person2`) | no | Either this or the `company` object is **REQUIRED**. Pass one or the other but not both. |  |
| `entity.company` | object (schema `Company2`) | no |  |  |
| `customer` | object | no |  |  |
| `customer.id` | integer (schema `CustomerID`) | no | Customer ID | format: "int64"; example: 100211299 |
| `customer.printed_name` | string (schema `PrintedName`) | no | <br>This field is **DEPRECATED**.<br><br>Name to be printed on the card.<br><br>Punctuation, special characters, and connectors (da/das/de/do/dos/e) are always removed.<br><br>This field's maximum length is 25, but you can set it to a lower value at the program level with the `Max name length on physical card` program parameter.<br><br>If `printed_name` is null, the Pismo platform uses `social_name`. If `social_name` is null, the Pismo platform uses the customer's entity name. For more information on the customer object, refer to [Core objects](doc:setup-overview#customer).<br><br>The Pismo platform gets the name for program parameter `TAMANHO MAX NOME EMBOSSADO` (max size name embossed).<br> | maxLength: 25; deprecated: true; example: "Jack Williams" |
| `customer.social_name` | string (schema `SocialName`) | no | Social name. | maxLength: 64; example: "Jack" |
| `customer.nickname` | string (schema `Nickname`) | no | Nickname. | maxLength: 128; example: "Pinto" |
| `customer.is_owner` | boolean (schema `IsOwner`) | no | Is the customer the account owner? | example: false |
| `customer.is_active` | boolean (schema `CustomerIsActive`) | no | Is customer active or not active? If `is_active` is null in this request, the Pismo platform doesn't overwrite the existing value. | example: true |
| `customer.email` | string (schema `IndividualsEmailAddress`) | no | Email address. | format: "email"; maxLength: 100; example: "jenna.flect@email.com" |
| `customer.addresses` | array of object | no |  |  |
| `customer.addresses[].address_id` | integer (schema `AddressID`) | no | Address ID | format: "int32"; example: 456 |
| `customer.addresses[].type` | string (schema `AddressType`) | no | Address type | enum: ["RESIDENTIAL", "COMMERCIAL", "OTHER"]; example: "RESIDENTIAL" |
| `customer.phones` | array of object | no |  |  |
| `customer.phones[].phone_id` | integer (schema `PhoneID`) | no | Phone ID | format: "int64"; example: 8714 |
| `customer.phones[].type` | string | no | Phone type. | enum: ["MOBILE", "RESIDENTIAL", "COMMERCIAL"]; example: "MOBILE" |

##### Response 404

404 Example `Account not found`:

```json
{
  "message": "Account not found"
}
```

404 Example `Customer not found`:

```json
{
  "message": "Customer not found."
}
```

404 Example `Person details not found`:

```json
{
  "message": "Person details not found."
}
```

404 Example `Company details not found`:

```json
{
  "message": "Company details not found."
}
```

##### Response 500

500 Example `Internal server error`:

```json
{
  "message": "Internal server error"
}
```


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;404;500`, has examples `True`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Core_platform_-_Accounts.yaml method=PUT path=/accounts/v2/customers/{customerId} operationId=customerV2Put -->
### `PUT /accounts/v2/customers/{customerId}` — Overwrite customer

- **operationId:** `customerV2Put`
- **Specification:** `api-specs/Core_platform_-_Accounts.yaml` (Core platform - Accounts)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Customers`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Overwrite some customer information. This endpoint allows you to mark the customer on the account as active or inactive using the `is_active` field. This field is informative only. There are no restrictions that prevent inactive customers from performing any actions.
>
> If `customer.is_active` = `true`, and the `Maximum number of card holders` program parameter is set, this customer is counted in the account's maximum number of card holders limit.
>
> If the `customerId` parameter is not set, the server returns "Cannot get property `customerId` on null object".
>
> **Note:** If `social_name` and `nickname` are not passed, their values are overwritten as null.
>
> This endpoint generates a [Customer changed](https://developers.pismo.io/events/docs/account-customer-change-2) event.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `customerId` | path | yes | integer | Customer ID | format: "int64"; example: 12345 |

#### Request body

Required: yes

> Customer data to overwrite

**Content type `application/json`** — schema: object (schema `OverwriteCustomerInformationRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `customer` | object | no |  |  |
| `customer.printed_name` | string (schema `PrintedName`) | no | <br>This field is **DEPRECATED**.<br><br>Name to be printed on the card.<br><br>Punctuation, special characters, and connectors (da/das/de/do/dos/e) are always removed.<br><br>This field's maximum length is 25, but you can set it to a lower value at the program level with the `Max name length on physical card` program parameter.<br><br>If `printed_name` is null, the Pismo platform uses `social_name`. If `social_name` is null, the Pismo platform uses the customer's entity name. For more information on the customer object, refer to [Core objects](doc:setup-overview#customer).<br><br>The Pismo platform gets the name for program parameter `TAMANHO MAX NOME EMBOSSADO` (max size name embossed).<br> | maxLength: 25; deprecated: true; example: "Jack Williams" |
| `customer.social_name` | string (schema `SocialName`) | no | Social name. | maxLength: 64; example: "Jack" |
| `customer.nickname` | string (schema `Nickname`) | no | Nickname. | maxLength: 128; example: "Pinto" |
| `customer.is_active` | boolean (schema `CustomerIsActive`) | no | Is customer active or not active? If `is_active` is null in this request, the Pismo platform doesn't overwrite the existing value. | example: true |
| `customer.email` | string (schema `IndividualsEmailAddress`) | no | Email address. | format: "email"; maxLength: 100; example: "jenna.flect@email.com" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK |  |
| 400 | Bad request | `application/json`: object |
| 404 | Customer {customerId} not found |  |
| 500 | Internal server error | `application/json`: object (schema `SimpleError`) |

##### Response 400

400 Example `Maximum Additional Customers`:

```json
{
  "message": "Exceeded maximum value of additional customers"
}
```

##### Response 500

500 Example `Internal server error`:

```json
{
  "message": "Internal server error"
}
```


#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `account-customer-change-2` | https://developers.pismo.io/events/docs/account-customer-change-2 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;404;500`, has examples `True`, emits events `1`, deprecated `False`.

Guides that link to this operation: `KU-EVT-accounts-data-events`.

<!-- op: spec=api-specs/Core_platform_-_Accounts.yaml method=PATCH path=/accounts/v1/accounts/{accountId}/customers/{customerId}/detail operationId=customerV1patch -->
### `PATCH /accounts/v1/accounts/{accountId}/customers/{customerId}/detail` — Update person or company customer

- **operationId:** `customerV1patch`
- **Specification:** `api-specs/Core_platform_-_Accounts.yaml` (Core platform - Accounts)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Customers`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Update the account's person or company customer information.
>
> Fields not passed are not updated.
>
> This endpoint generates an [Account entity updated](https://developers.pismo.io/events/docs/audit-entity-change-1) event.
>
> If the `customer.is_owner` property is set to `true`:
>   - The account owner is changed to this new customer, and all existing customers remain active in the account.
>   - This endpoint generates an [Account owner changed](https://developers.pismo.io/events/docs/account-owner-change-1) event.
>
> If `customer.is_active = true`, and the **Maximum number of card holders** program parameter is set, this customer is counted in the limit of maximum number of card holders for an account.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `x-cid` | header | no | string | The Correlation IDentifier field is used to link related API requests and events. The `x-cid` can help the Pismo engineering team track everything related to a call. You can find the x-cid field in the response header from an API endpoint call.<br><br>If this field isn't passed, one is automatically generated.<br> | example: "5bb05174-4e80-11ea-b77f-2e728ce88125" |
| `x-tenant` | header | yes | string | Organization ID | example: "TN-34778262-f4f0-464d-b4c6-a14e2dc6f4be" |
| `accountId` | path | yes | integer | Account ID | format: "int64"; minimum: 1; example: 123 |
| `customerId` | path | yes | integer | Customer ID | format: "int64"; example: 12345 |

#### Request body

Required: no

> Customer properties to update

**Content type `application/json`** — schema: oneOf: object (schema `PersonRequest`), object (schema `CompanyRequest`)

_oneOf option 1: schema `PersonRequest`_

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `name` | string (schema `IndividualsName`) | no | Name - person or company name | example: "Hyman Roth" |
| `nickname` | string (schema `Nickname`) | no | Nickname. | maxLength: 128; example: "Pinto" |
| `printed_name` | string (schema `PrintedName3`) | no | <br>This field is **DEPRECATED**. Cards is now responsible for this field.<br><br>Person's name to be printed on the card. If the field is null, `name` or `social_name` is used.<br><br>Punctuation, special characters, and connectors (da/das/de/do/dos/e) are always removed.<br><br>This field's maximum lengh of this field is 25, but you can set it to a lower value on the program level with the `Max name length on physical card` program parameter.<br> | maxLength: 25; deprecated: true; example: "Luce Lyons" |
| `social_name` | string (schema `SocialName`) | no | Social name. | maxLength: 64; example: "Jack" |
| `email` | string (schema `IndividualsEmailAddress`) | no | Email address. | format: "email"; maxLength: 100; example: "jenna.flect@email.com" |
| `pep` | boolean (schema `PEP`) | no | Is this person a Politically Exposed Person (PEP)? Pismo doesn't do anything differently for a PEP, this is just additional account information. Default is `false`.<br> | example: false |
| `gender` | string (schema `Gender`) | no | Gender | enum: ["F", "M", ""]; maxLength: 1; example: "M" |
| `marital_status` | string (schema `MaritalStatus`) | no | Marital status | enum: ["SINGLE", "MARRIED", "DIVORCED", "WIDOWER"]; example: "MARRIED" |
| `mothers_name` | string (schema `MothersName`) | no | Mother's name | maxLength: 60; example: "Kay Sadilla" |
| `nationality` | string (schema `Nationality`) | no | Nationality | maxLength: 60; example: "Australian" |
| `city_of_birth` | string (schema `CityOfBirth`) | no | Birth city | maxLength: 60; example: "San Diego" |
| `state_of_birth` | string (schema `StateOfBirth`) | no | Birth state | maxLength: 60; example: "California" |
| `country_of_birth` | string (schema `CountryOfBirth`) | no | Birth country | maxLength: 60; example: "India" |
| `other_id_number` | string (schema `OtherIdNumber`) | no | Another ID number | example: "29000000" |
| `document_type` | string (schema `DocumentType`) | no | Document type. Free-form field, not an enum. | maxLength: 30 |
| `document_issued_by` | string (schema `DocumentIssuedBy`) | no | Document issuer | maxLength: 30 |
| `document_issued_at` | string (schema `DocumentIssuedAt`) | no | Document issuer location. This is a free-form field, not an ISO standard. | maxLength: 30; example: "Brazil" |
| `document_issued_date` | string (schema `DocumentIssuedDate`) | no | Date document was issued. Format = dd/mm/yyyy. | example: "01/31/1970" |
| `fathers_name` | string (schema `FathersName`) | no | Father's name | maxLength: 60; example: "Steven Douglas" |
| `occupation` | string (schema `PersonOccupation`) | no | Person's occupation | maxLength: 60; example: "Programmer" |
| `assets` | number (schema `Assets`) | no | Assets | format: "float"; example: 40000 |
| `income` | number (schema `PersonIncome`) | no | Person's income | format: "float"; example: 2000 |
| `net_worth` | number (schema `PersonNetWorth`) | no | Person's net worth | format: "float"; example: 50000 |
| `birth_date` | string (schema `BirthDate`) | no | Birth date. Format = dd/mm/yyyy. | example: "31/12/1980" |
| `document_issued_date` | string (schema `DocumentIssuedDate`) | no | Date document was issued. Format = dd/mm/yyyy. | example: "01/31/1970" |
| `is_owner` | boolean | no | Is customer the account owner? | example: false |
| `is_active` | boolean | no | Is customer active? | example: true |

_oneOf option 2: schema `CompanyRequest`_

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `name` | string (schema `CompanyRepresentativeName`) | no | Company representative name | example: "Sam Houston" |
| `nickname` | string (schema `CompanyRepresentativeNickname`) | no | Company representative nickname | example: "Curveball" |
| `printed_name` | string (schema `PrintedName3`) | no | <br>This field is **DEPRECATED**. Cards is now responsible for this field.<br><br>Person's name to be printed on the card. If the field is null, `name` or `social_name` is used.<br><br>Punctuation, special characters, and connectors (da/das/de/do/dos/e) are always removed.<br><br>This field's maximum lengh of this field is 25, but you can set it to a lower value on the program level with the `Max name length on physical card` program parameter.<br> | maxLength: 25; deprecated: true; example: "Luce Lyons" |
| `social_name` | string (schema `CompanyRepresentativeSocialName`) | no | Company representative's social name | example: "Otter" |
| `pep` | boolean (schema `PEP`) | no | Is this person a Politically Exposed Person (PEP)? Pismo doesn't do anything differently for a PEP, this is just additional account information. Default is `false`.<br> | example: false |
| `company_name` | string (schema `CompanyName`) | no | Company's legal name | maxLength: 150; example: "Acme Inc." |
| `registration_number` | string (schema `RegistrationNumber`) | no | Company's registration number with local authorities | maxLength: 30; example: "ACM10004" |
| `activity` | string (schema `Activity`) | no | Company's general field of activity | maxLength: 30; example: "Manufacturing" |
| `company_type` | string (schema `CompanyType`) | no | Company type | maxLength: 60; example: "Retailer" |
| `company_format` | string (schema `CompanyFormat`) | no | Company social type | maxLength: 60; example: "ME" |
| `occupation` | string (schema `RepresentativeOccupation`) | no | Company representative's occupation | maxLength: 60; example: "CEO" |
| `income` | number (schema `CompanyIncome2`) | no | Company's income | format: "float"; example: 10000 |
| `net_worth` | number (schema `CompanyNetWorth2`) | no | Company's net worth. | format: "float"; example: 20000 |
| `annual_revenues` | number (schema `CompanyAnnualRevenues`) | no | Company annual revenues (monthly billing average) | format: "float"; example: 33000 |
| `type` | string (schema `CompanyBusinessRelationsType`) | no | Company's business relations type | maxLength: 60; example: "B2C" |
| `number_of_partners` | integer (schema `NumberOfPartners`) | no | Number of company partners | format: "int32"; example: 3 |
| `perc_ownership` | number (schema `PercOwnership`) | no | Company percentage ownership | format: "float"; example: 50 |
| `fiscal_situation` | string (schema `FiscalSituation`) | no | Company's fiscal situation. | maxLength: 60; example: "Good" |
| `debt` | number (schema `CompanyDebt2`) | no | Company's debt | format: "float"; example: 18000 |
| `email` | string (schema `CompanyEmail`) | no | Company's registered email | maxLength: 100; example: "acme@acmemail.com" |
| `partners` | array of object (schema `Partner`) | no | Company partners |  |
| `company_constitution_date` | string (schema `CompanyConstitutionDate2`) | no | Company constitution date. Format = dd/MM/yyyy. | example: "01/01/2019" |
| `is_owner` | boolean | no | Is the customer the account owner (`true`) or an additional customer (`false`). | example: false |
| `is_active` | boolean | no | Is the customer active (`true`) or not (`false`). | example: true |


#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Customer details were successfully updated | `application/json`: oneOf: object (schema `PersonResponse`), object (schema `CompanyResponse`) |
| 404 | Not found | `application/json`: object |
| 500 | Internal server error | `application/json`: object (schema `SimpleError`) |

##### Response 200

**200 `application/json` body fields:**

_No fields declared in the schema._

##### Response 500

500 Example `Internal server error`:

```json
{
  "message": "Internal server error"
}
```


#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `account-owner-change-1` | https://developers.pismo.io/events/docs/account-owner-change-1 |
| `audit-entity-change-1` | https://developers.pismo.io/events/docs/audit-entity-change-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;404;500`, has examples `True`, emits events `2`, deprecated `False`.

Guides that link to this operation: `KU-EVT-accounts-data-events`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/Person2 -->
### Schema `Person2`

Pointer: `#/components/schemas/Person2`. Type: object (schema `Person2`).

> Either this or the `company` object is **REQUIRED**. Pass one or the other but not both.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `nationality` | string (schema `Nationality`) | no | Nationality | maxLength: 60; example: "Australian" |
| `city_of_birth` | string (schema `CityOfBirth`) | no | Birth city | maxLength: 60; example: "San Diego" |
| `state_of_birth` | string (schema `StateOfBirth`) | no | Birth state | maxLength: 60; example: "California" |
| `country_of_birth` | string (schema `CountryOfBirth`) | no | Birth country | maxLength: 60; example: "India" |
| `other_id_number` | string (schema `OtherIdNumber`) | no | Another ID number | example: "29000000" |
| `document_type` | string (schema `DocumentType`) | no | Document type. Free-form field, not an enum. | maxLength: 30 |
| `document_issued_by` | string (schema `DocumentIssuedBy`) | no | Document issuer | maxLength: 30 |
| `document_issued_at` | string (schema `DocumentIssuedAt`) | no | Document issuer location. This is a free-form field, not an ISO standard. | maxLength: 30; example: "Brazil" |
| `document_issued_date` | string (schema `DocumentIssuedDate`) | no | Date document was issued. Format = dd/mm/yyyy. | example: "01/31/1970" |
| `fathers_name` | string (schema `FathersName`) | no | Father's name | maxLength: 60; example: "Steven Douglas" |
| `occupation` | string (schema `PersonOccupation`) | no | Person's occupation | maxLength: 60; example: "Programmer" |
| `assets` | number (schema `Assets`) | no | Assets | format: "float"; example: 40000 |
| `income` | number (schema `PersonIncome`) | no | Person's income | format: "float"; example: 2000 |
| `net_worth` | number (schema `PersonNetWorth`) | no | Person's net worth | format: "float"; example: 50000 |

<!-- schema: #/components/schemas/Company2 -->
### Schema `Company2`

Pointer: `#/components/schemas/Company2`. Type: object (schema `Company2`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `company_name` | string (schema `CompanyName`) | no | Company's legal name | maxLength: 150; example: "Acme Inc." |
| `registration_number` | string (schema `RegistrationNumber`) | no | Company's registration number with local authorities | maxLength: 30; example: "ACM10004" |
| `activity` | string (schema `Activity`) | no | Company's general field of activity | maxLength: 30; example: "Manufacturing" |
| `company_type` | string (schema `CompanyType`) | no | Company type | maxLength: 60; example: "Retailer" |
| `company_format` | string (schema `CompanyFormat`) | no | Company social type | maxLength: 60; example: "ME" |
| `company_constitution_date` | string (schema `CompanyConstitutionDate2`) | no | Company constitution date. Format = dd/MM/yyyy. | example: "01/01/2019" |
| `occupation` | string (schema `RepresentativeOccupation`) | no | Company representative's occupation | maxLength: 60; example: "CEO" |
| `annual_revenues` | number (schema `CompanyAnnualRevenues`) | no | Company annual revenues (monthly billing average) | format: "float"; example: 33000 |
| `type` | string (schema `CompanyBusinessRelationsType`) | no | Company's business relations type | maxLength: 60; example: "B2C" |
| `number_of_partners` | integer (schema `NumberOfPartners`) | no | Number of company partners | format: "int32"; example: 3 |
| `perc_ownership` | number (schema `PercOwnership`) | no | Company percentage ownership | format: "float"; example: 50 |
| `fiscal_situation` | string (schema `FiscalSituation`) | no | Company's fiscal situation. | maxLength: 60; example: "Good" |
| `debt` | number (schema `CompanyDebt2`) | no | Company's debt | format: "float"; example: 18000 |
| `income` | integer (schema `CompanyIncome`) | no | Company's income | format: "int64"; example: 10000 |
| `net_worth` | integer (schema `CompanyNetWorth`) | no | Company's net worth | format: "int64"; example: 20000 |
| `partners` | array of object (schema `Partner`) | no | Company partners |  |

<!-- schema: #/components/schemas/SimpleError -->
### Schema `SimpleError`

Pointer: `#/components/schemas/SimpleError`. Type: object (schema `SimpleError`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `message` | string | yes | Error message |  |

<!-- schema: #/components/schemas/Partner -->
### Schema `Partner`

Pointer: `#/components/schemas/Partner`. Type: object (schema `Partner`).

> Applicant's personal information

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `name` | string (schema `IndividualsName`) | no | Name - person or company name | example: "Hyman Roth" |
| `nickname` | string (schema `Nickname`) | no | Nickname. | maxLength: 128; example: "Pinto" |
| `printed_name` | string (schema `PrintedName`) | no | <br>This field is **DEPRECATED**.<br><br>Name to be printed on the card.<br><br>Punctuation, special characters, and connectors (da/das/de/do/dos/e) are always removed.<br><br>This field's maximum length is 25, but you can set it to a lower value at the program level with the `Max name length on physical card` program parameter.<br><br>If `printed_name` is null, the Pismo platform uses `social_name`. If `social_name` is null, the Pismo platform uses the customer's entity name. For more information on the customer object, refer to [Core objects](doc:setup-overview#customer).<br><br>The Pismo platform gets the name for program parameter `TAMANHO MAX NOME EMBOSSADO` (max size name embossed).<br> | maxLength: 25; deprecated: true; example: "Jack Williams" |
| `social_name` | string (schema `SocialName`) | no | Social name. | maxLength: 64; example: "Jack" |
| `email` | string (schema `IndividualsEmailAddress`) | no | Email address. | format: "email"; maxLength: 100; example: "jenna.flect@email.com" |
| `document_number` | string (schema `DocumentNumber`) | no | Document number, such as a government tax ID. | maxLength: 15; example: "31457828046" |
| `mothers_name` | string (schema `MothersName`) | no | Mother's name | maxLength: 60; example: "Kay Sadilla" |
| `gender` | string (schema `Gender`) | no | Gender | enum: ["F", "M", ""]; maxLength: 1; example: "M" |
| `birth_date` | string (schema `BirthDate`) | no | Birth date. Format = dd/mm/yyyy. | example: "31/12/1980" |
| `city_of_birth` | string (schema `CityOfBirth`) | no | Birth city | maxLength: 60; example: "San Diego" |
| `state_of_birth` | string (schema `StateOfBirth`) | no | Birth state | maxLength: 60; example: "California" |
| `country_of_birth` | string (schema `CountryOfBirth`) | no | Birth country | maxLength: 60; example: "India" |
| `fathers_name` | string (schema `FathersName`) | no | Father's name | maxLength: 60; example: "Steven Douglas" |
| `marital_status` | string (schema `MaritalStatus`) | no | Marital status | enum: ["SINGLE", "MARRIED", "DIVORCED", "WIDOWER"]; example: "MARRIED" |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Core_platform_-_Accounts.yaml` | tag `Customers`: POST /accounts/v2/customers, GET /accounts/v2/accounts/{accountId}/customers, GET /accounts/v2/customers/{customerId}, PUT /accounts/v2/customers/{customerId}, PATCH /accounts/v1/accounts/{accountId}/customers/{customerId}/detail | https://github.com/PismoDevEx/pismo-api-specs | `3c621106abf11d41…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-BANK-banking-as-a-service` — Banking as a Service
- `KU-CARD-implementation-steps` — Card issuing implementation steps 1 to 7
- `KU-CORE-accounts-overview` — Accounts
- `KU-EVT-accounts-data-events` — Core platform - Accounts
- `KU-EVT-catalogue-account` — Event catalogue: account
- `KU-EVT-catalogue-audit` — Event catalogue: audit
- `KU-GS-program-types` — Program types
- `KU-GS-setup-overview` — Core objects
