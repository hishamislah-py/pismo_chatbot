---
ku_id: KU-API-core-platform-accounts--accounts
title: 'API reference: Core platform - Accounts — Accounts'
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
- post-acquisitions-v3-s2s-applications
- GetApplicationByApplicationId
- patch-acquisitions-v2-s2s-applications
- get-acquisitions-v2-programs-programId-channels
- post-accounts-v5-accounts-search
- post-accounts-v3-accounts-search
- get-accounts-v1-accounts
- patch-accounts-v1-accounts
- post-acquisitions-v2-s2s-applications
- get-accounts-v4-accounts-accountId-hierarchy-ascendants
related_kus:
- KU-AUTH-pismo-platform-security-guide
- KU-BANK-banking-as-a-service
- KU-BANK-banking-overview
- KU-BANK-get-started-core-banking
- KU-CARD-card-issuing-basics
- KU-CARD-implementation-steps
- KU-CARD-physical-card-embossing
- KU-CC-accounts
- KU-CORE-accounts-overview
- KU-CORE-commercial-cards
- KU-CORE-legal-blocks
- KU-CORE-program-limits
- KU-CORE-working-with-limits-objects
- KU-CRED-agreements
- KU-CRED-holidays-in-credit-card-accounts
- KU-ERR-codes-acq-to-esma
- KU-ERR-codes-esmg-to-whis
- KU-ERR-validation-code-definitions
- KU-EVT-accounts-data-events
- KU-EVT-catalogue-account
- KU-EVT-catalogue-other-domains
- KU-GS-get-started-with-pismo-apis
- KU-GS-program-types
- KU-GS-setup-overview
- KU-PAY-bacs
- KU-PAY-faster-payment-system
specification_version: 1.0.0
---

# API reference: Core platform - Accounts — Accounts

**KU ID:** `KU-API-core-platform-accounts--accounts` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 10 operation(s) tagged `Accounts` in `api-specs/Core_platform_-_Accounts.yaml` (“Core platform - Accounts”, version `1.0.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Endpoints to manage accounts

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `POST /acquisitions/v3/s2s/applications` | `post-acquisitions-v3-s2s-applications` | Create account application | no |
| `GET /acquisitions/v2/s2s/applications/{applicationId}` | `GetApplicationByApplicationId` | Get account application | no |
| `PATCH /acquisitions/v2/s2s/applications/{applicationId}` | `patch-acquisitions-v2-s2s-applications` | Update account application | no |
| `GET /acquisitions/v2/programs/{programId}/channels` | `get-acquisitions-v2-programs-programId-channels` | List acquisition channels | no |
| `POST /accounts/v5/accounts/search` | `post-accounts-v5-accounts-search` | List accounts by phone number | no |
| `POST /accounts/v3/accounts/search` | `post-accounts-v3-accounts-search` | List accounts by document number | no |
| `GET /accounts/v1/accounts/{accountId}` | `get-accounts-v1-accounts` | Get account | no |
| `PATCH /accounts/v1/accounts/{accountId}` | `patch-accounts-v1-accounts` | Update account | no |
| `POST /acquisitions/v2/s2s/applications` | `post-acquisitions-v2-s2s-applications` | Create account application (deprecated) | **yes** |
| `GET /accounts/v4/accounts/{accountId}/hierarchy/ascendants` | `get-accounts-v4-accounts-accountId-hierarchy-ascendants` | Get account hierarchy ascendants | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"}

## Operation contracts

<!-- op: spec=api-specs/Core_platform_-_Accounts.yaml method=POST path=/acquisitions/v3/s2s/applications operationId=post-acquisitions-v3-s2s-applications -->
### `POST /acquisitions/v3/s2s/applications` — Create account application

- **operationId:** `post-acquisitions-v3-s2s-applications`
- **Specification:** `api-specs/Core_platform_-_Accounts.yaml` (Core platform - Accounts)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Accounts`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Create a new account application.
>
> If `submit` is set to `false`:
>
> - The application is not sent for processing and can be further modified  with incremental changes via [Update account application](ref:patch-acquisitions-v2-s2s-applications).
>
> - This endpoint generates an [Account application prospect created](https://developers.pismo.io/events/docs/onboarding-prospect-1) event.
>
> If `submit` flag is set to `true`:
>
> - No further updates can be made and the account application is sent out for processing, which creates an account and its associated structures.
>
> - This endpoint generates an [Account application created](https://developers.pismo.io/events/docs/onboarding-succeeded-1) event.
>
>
> **Warning**&mdash;Some of the account's elements are created asynchronously and you should refrain from accessing the account via other endpoints until the events this endpoint generates are received.
>
> **Notes:**
>   * Either the `personal` object or `company` object is **REQUIRED**. Pass one or the other but not both.
>   * This endpoint creates a default `entity` object for the account owner based on document ID.
>
> Refer to the [Core objects](doc:setup-overview) and the [Accounts](doc:accounts-overview) guides for more information.

#### Request body

Required: yes

> Application details

**Content type `application/json`** — schema: object

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `application` | object (schema `AcquisitionRequestV3`) | yes | Application form |  |

Example `Application form`:

```json
{
  "application": {
    "submit": true,
    "due_date": 4638,
    "program_id": 1226,
    "applicant": {
      "document_number": "695-32-3317",
      "birth_date": "1980-01-31",
      "account": {
        "external_id": "de84c0b2-6d9e-49b3-ae97-acbd9944f62a",
        "currency_numeric_code": "986",
        "account_type": "PHYSICAL",
        "account_name": "Account cash management",
        "granted_limit": 1000,
        "limit": 500
      },
      "personal": {
        "name": "John Doe",
        "email": "john.doe@email.com"
      },
      "addresses": [
        {
          "address": "Nowhere St.",
          "number": "222",
          "address1": "10",
          "country": "USA",
          "complementary_address": "Suite B",
          "neighborhood": "Faraway Creek",
          "city": "Smallville",
          "state": "KS",
          "zip_code": "01234",
          "mailing_address": true,
          "address_type": "RESIDENTIAL"
        }
      ],
      "phones": [
        {
          "phone": "555-1234",
          "phone_type": "MOBILE",
          "country_code": "55",
          "area_code": 11
        }
      ]
    }
  }
}
```

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | Created | `application/json`: object (schema `AcquisitionResponse`) |
| 400 | Bad request | `application/json`: object (schema `SimpleError`) |
| 409 | Conflict | `application/json`: object (schema `SimpleError`) |
| 500 | Internal server error | `application/json`: object (schema `SimpleError`) |

##### Response 201

**201 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `application_id` | integer (schema `ApplicationIdNonchecking`) | yes | Application form ID (non-checking accounts only) | format: "int64"; example: 1234 |
| `status` | integer (schema `ApplicationStatusIdNonchecking`) | yes | Application status ID | format: "int64"; example: 4 |
| `status_name` | string (schema `ApplicationStatusNameNonchecking`) | yes | Application status. Most likely to be<br>* `REGISTERED` - Application was saved, but not started processing yet.<br>* `APPROVED` - Application has finished processing.<br>* `PROSPECT` - Application was created with `submit` = `false`.<br> | example: "APPROVED" |
| `account_id` | integer (schema `AccountIdNonchecking`) | yes | Created account ID. `null` if the application has not been proccessed yet (non-checking accounts only). | format: "int64"; example: 123 |
| `customer_id` | integer (schema `CustomerIdNonchecking`) | yes | Created customer ID. `null` if the application has not yet been proccessed (non-checking accounts only). | format: "int64"; example: 123 |
| `entity_id` | integer (schema `EntityID2`) | yes | Created entity ID. `null` if the application has not yet been proccessed (non-checking accounts only). | format: "int64"; example: 123 |
| `program_id` | integer (schema `ProgramID`) | yes | Program ID | format: "int64"; example: 12345 |

201 Example `Application created`:

```json
{
  "application_id": 23942777,
  "status": 4,
  "status_name": "APPROVED",
  "account_id": 123,
  "customer_id": 456,
  "entity_id": 789,
  "program_id": 100
}
```

##### Response 400

400 Example `Bad channel`:

```json
{
  "message": "Invalid acquisition channel"
}
```

400 Example `Program restriction`:

```json
{
  "message": "Account cannot be created due to program restrictions"
}
```

##### Response 409

409 Example `Account conflict`:

```json
{
  "message": "Account already created"
}
```

##### Response 500

500 Example `Internal server error`:

```json
{
  "message": "Error registering application"
}
```


#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `onboarding-prospect-1` | https://developers.pismo.io/events/docs/onboarding-prospect-1 |
| `onboarding-succeeded-1` | https://developers.pismo.io/events/docs/onboarding-succeeded-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `201;400;409;500`, has examples `True`, emits events `2`, deprecated `False`.

Guides that link to this operation: `KU-AUTH-pismo-platform-security-guide`, `KU-BANK-banking-as-a-service`, `KU-BANK-banking-overview`, `KU-BANK-get-started-core-banking`, `KU-CARD-card-issuing-basics`, `KU-CARD-implementation-steps`, `KU-CARD-physical-card-embossing`, `KU-CC-accounts`, `KU-CORE-accounts-overview`, `KU-CORE-commercial-cards`, `KU-CORE-program-limits`, `KU-CORE-working-with-limits-objects`, `KU-CRED-holidays-in-credit-card-accounts`, `KU-ERR-validation-code-definitions`, `KU-EVT-accounts-data-events`, `KU-GS-get-started-with-pismo-apis`, `KU-GS-program-types`, `KU-GS-setup-overview`, `KU-PAY-bacs`, `KU-PAY-faster-payment-system`.

<!-- op: spec=api-specs/Core_platform_-_Accounts.yaml method=GET path=/acquisitions/v2/s2s/applications/{applicationId} operationId=GetApplicationByApplicationId -->
### `GET /acquisitions/v2/s2s/applications/{applicationId}` — Get account application

- **operationId:** `GetApplicationByApplicationId`
- **Specification:** `api-specs/Core_platform_-_Accounts.yaml` (Core platform - Accounts)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Accounts`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Get account application given application ID in the path.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `applicationId` | path | yes | integer | Application ID | format: "int64"; example: 12345 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `ApplicationsResponse`) |
| 404 | Not found | `application/json`: object |
| 500 | 500 | `text/plain`: no schema |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `application_id` | integer (schema `ApplicationIdNonchecking`) | yes | Application form ID (non-checking accounts only) | format: "int64"; example: 1234 |
| `program_due_date_id` | integer (schema `ProgramDueDateID`) | yes | ID of Program due date | format: "int64"; example: 1234 |
| `program_id` | integer (schema `ProgramID`) | yes | Program ID | format: "int64"; example: 12345 |
| `acquisition_channel_id` | integer (schema `AcquisitionChannelID`) | yes | Application's acquisition channel ID. An acquisition channel is how a customer was referred to the site, such as through a web app or mobile app.<br><br>You can call [List acquistion channels](ref:get-acquisitions-v2-programs-programid-channels) to find channels registered for your account.<br> | format: "int64"; example: 111 |
| `created_at` | string (schema `CreatedAt`) | yes | Date application was created. RFC 3339 format. | example: "2021-06-08T10:46:54.000Z" |
| `application_status` | number (schema `ApplicationStatusNonchecking`) | yes | Application status, according to the status mapping (non-checking accounts only). | example: 4 |
| `application_status_name` | string (schema `ApplicationStatusNameNonchecking`) | yes | Application status. Most likely to be<br>* `REGISTERED` - Application was saved, but not started processing yet.<br>* `APPROVED` - Application has finished processing.<br>* `PROSPECT` - Application was created with `submit` = `false`.<br> | example: "APPROVED" |
| `application_form` | object (schema `ApplicationForm`) | yes | Key/value field that contains all fields from the application form.<br>This data can be used to verify the application form during onboarding. It should not be used to obtain data after the account is approved.<br>After the final status of the application form (such as `APPROVED` or `CANCELLED`), this data is kept as read-only and is not updated.<br> | example: {"id": 1234, "submit": true, "applicant": {"entity": {"name": "John Doe", "entity_type": "PERSON", "document_number": "31384509038"}, "account": {"email": "johndoe@test.com", "limit": 50000}, "customer": {"nickname": "John", "social_name": "John Doe", "printed_name": "John Doe"}}} |

##### Response 500

500 Example `Result`:

```text
Internal server error
```


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;404;500`, has examples `True`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Core_platform_-_Accounts.yaml method=PATCH path=/acquisitions/v2/s2s/applications/{applicationId} operationId=patch-acquisitions-v2-s2s-applications -->
### `PATCH /acquisitions/v2/s2s/applications/{applicationId}` — Update account application

- **operationId:** `patch-acquisitions-v2-s2s-applications`
- **Specification:** `api-specs/Core_platform_-_Accounts.yaml` (Core platform - Accounts)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Accounts`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Update a previously-created account application, only if the account application's `submit` field is `false`.
>
> If `submit` is set to `false`:
>
> - The application is not sent for processing and can be further modified  with incremental changes via this endpoint.
>
> If `submit` flag is set to `true`:
>
> - No further updates can be made and the account application is sent out for processing, which creates an account and its associated structures.
>
> - This endpoint generates an [Account application created](https://developers.pismo.io/events/docs/onboarding-succeeded-1) event.
>
> **Warning**&mdash;Some of the account's elements are created asynchronously and you should refrain from accessing the account via other endpoints until the events this endpoint generates are received.
>
> **Notes:**
>
> * By default, `prospect_cancel` is `false`. If you set `prospect_cancel` to `true`, the account application is canceled and no further updates can be made.
>
> * You **cannot** update a previously-entered address. All addresses entered are considered new.  The main address is the last one passed with `mailing_address` = `true`.
>
> * You **cannot** update a previously-entered `partner` object. All partner information entered is considered new.
>
> * For all other objects and fields, anything not passed is not updated.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `applicationId` | path | yes | integer | Application ID | format: "int64"; example: 12345 |

#### Request body

Required: no

**Content type `application/json`** — schema: object

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `application` | object (schema `AcquisitionRequestUpdate`) | no | Application form |  |

Example `Application Form`:

```json
{
  "application": {
    "submit": true,
    "prospect_cancel": false
  }
}
```

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `AcquisitionResponse`) |
| 400 | Bad request | `application/json`: object (schema `SimpleError`) |
| 409 | Conflict | `application/json`: object (schema `SimpleError`) |
| 500 | Internal server error | `application/json`: object (schema `SimpleError`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `application_id` | integer (schema `ApplicationIdNonchecking`) | yes | Application form ID (non-checking accounts only) | format: "int64"; example: 1234 |
| `status` | integer (schema `ApplicationStatusIdNonchecking`) | yes | Application status ID | format: "int64"; example: 4 |
| `status_name` | string (schema `ApplicationStatusNameNonchecking`) | yes | Application status. Most likely to be<br>* `REGISTERED` - Application was saved, but not started processing yet.<br>* `APPROVED` - Application has finished processing.<br>* `PROSPECT` - Application was created with `submit` = `false`.<br> | example: "APPROVED" |
| `account_id` | integer (schema `AccountIdNonchecking`) | yes | Created account ID. `null` if the application has not been proccessed yet (non-checking accounts only). | format: "int64"; example: 123 |
| `customer_id` | integer (schema `CustomerIdNonchecking`) | yes | Created customer ID. `null` if the application has not yet been proccessed (non-checking accounts only). | format: "int64"; example: 123 |
| `entity_id` | integer (schema `EntityID2`) | yes | Created entity ID. `null` if the application has not yet been proccessed (non-checking accounts only). | format: "int64"; example: 123 |
| `program_id` | integer (schema `ProgramID`) | yes | Program ID | format: "int64"; example: 12345 |

200 Example `Processed application`:

```json
{
  "application_id": 23942777,
  "status": 4,
  "status_name": "APPROVED",
  "account_id": 35426,
  "customer_id": 3569,
  "entity_id": 123,
  "program_id": 100
}
```

##### Response 400

400 Example `Bad channel`:

```json
{
  "message": "Invalid acquisition channel"
}
```

##### Response 409

409 Example `Account conflict`:

```json
{
  "message": "Account already created"
}
```

##### Response 500

500 Example `Internal server error`:

```json
{
  "message": "Error registering application"
}
```


#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `onboarding-succeeded-1` | https://developers.pismo.io/events/docs/onboarding-succeeded-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;409;500`, has examples `True`, emits events `1`, deprecated `False`.

Guides that link to this operation: `KU-CORE-accounts-overview`.

<!-- op: spec=api-specs/Core_platform_-_Accounts.yaml method=GET path=/acquisitions/v2/programs/{programId}/channels operationId=get-acquisitions-v2-programs-programId-channels -->
### `GET /acquisitions/v2/programs/{programId}/channels` — List acquisition channels

- **operationId:** `get-acquisitions-v2-programs-programId-channels`
- **Specification:** `api-specs/Core_platform_-_Accounts.yaml` (Core platform - Accounts)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Accounts`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> List acquisition channels registered for a specific program.
>
> The acquisition channel is the unique ID of the original source of your customer (such as a referring web page or mobile app). Acquisition channels are configured at the program level.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `programId` | path | yes | integer | Program ID | format: "int64"; minimum: 1; example: 123 |
| `page` | query | no | integer | Page number. | default: 1; format: "int32" |
| `perPage` | query | no | integer | Items per page. | default: 10; format: "int32"; minimum: 1; maximum: 100; example: 100 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `AcquisitionChannelsResponse`) |
| 500 | Internal server error | `application/json`: object (schema `SimpleError`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `pages` | integer (schema `NumberOfPages`) | no | Total pages | format: "int32"; example: 100 |
| `per_page` | integer (schema `PerPage`) | no | Maximum items per page. 100 maximum. | format: "int64"; example: 100 |
| `current_page` | integer (schema `CurrentPage`) | no | Current page | format: "int32"; example: 1 |
| `total_items` | integer (schema `TotalItems`) | no | Total items | format: "int32"; example: 500 |
| `items` | array of object (schema `AcquisitionChannelItemResponse`) | no | List of result items |  |

200 Example `Channel list`:

```json
{
  "total_items": 1,
  "per_page": 10,
  "pages": 1,
  "current_page": 1,
  "items": [
    {
      "id": 123,
      "type": "Webapp",
      "name": "eStore form"
    }
  ]
}
```

##### Response 500

500 Example `Internal server error`:

```json
{
  "message": "Error retrieving acquisition channels"
}
```


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;500`, has examples `True`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Core_platform_-_Accounts.yaml method=POST path=/accounts/v5/accounts/search operationId=post-accounts-v5-accounts-search -->
### `POST /accounts/v5/accounts/search` — List accounts by phone number

- **operationId:** `post-accounts-v5-accounts-search`
- **Specification:** `api-specs/Core_platform_-_Accounts.yaml` (Core platform - Accounts)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Accounts`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> List accounts by phone number.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `nextCursor` | query | no | string | Cursor value used to get the next page. This is the `next_cursor` value returned in the response. | example: "MEgCQQCo9..." |
| `maxItems` | query | no | integer | Number of items on current page. `200` maximum. Default is `200`. | format: "int32"; minimum: 1; maximum: 200; example: 100 |

#### Request body

Required: yes

> Account search fields

**Content type `application/json`** — schema: object (schema `AccountsV5Request`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `phone` | object | yes | Filter by phone number, area code, and/or country code. Phone number is required. |  |
| `phone.number` | string (schema `PhoneNumber`) | yes | Phone number | maxLength: 15; example: "11912345678" |
| `phone.area_code` | string (schema `AreaCode`) | no | Phone number area code | maxLength: 2; example: "51" |
| `phone.country_code` | string (schema `PhoneCountryCode`) | no | Phone number's country code | maxLength: 5; example: "555" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | List of accounts returned | `application/json`: object |
| 400 | Bad request | `application/json`: object (schema `MessageResponse`) |
| 500 | Internal server error | `application/json`: object (schema `MessageResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `next_cursor` | string (schema `NextCursor`) | no | Cursor value for the next page | example: "MEgCQQCo9+BpMRYQ/dL3DS2CyJxRF+j6ctbT3/Qp84+KeFhnii7NT7fELilKUSnxS30WAvQCCo2yU1orfgqr41mM70MBAgMBAAE=" |
| `has_next` | boolean (schema `HasNext`) | no | Are there more results (retrieved using the `next_cursor` value)? | example: true |
| `count` | integer (schema `CurrentPageCount`) | no | Number of items on the current page | format: "int32"; example: 100 |
| `items` | array of object (schema `AccountsV5Response`) | no | List of result items |  |

##### Response 400

400 Example `Invalid payload`:

```json
{
  "code": "EACC0004",
  "message": "Failed during validation of request payload",
  "detail": {
    "payload": [
      {
        "field": "phone",
        "message": "Field is required"
      }
    ]
  }
}
```

400 Example `Invalid next_cursor parameter`:

```json
{
  "code": "WACC0011",
  "message": "Invalid cursor value"
}
```

400 Example `Invalid maxItems parameter`:

```json
{
  "code": "EACC0005",
  "message": "One or more parameters with invalid format",
  "detail": {
    "parameters": [
      {
        "field": "maxItems",
        "message": "Value must be greater than zero"
      }
    ]
  }
}
```

##### Response 500

500 Example `Timeout execution`:

```json
{
  "code": "EACC0000",
  "message": "Timeout while executing the request"
}
```

500 Example `Generic message`:

```json
{
  "code": "EACC9999",
  "message": "Something went wrong, please try again later"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `EACC0004` | Failed during validation of request payload |
| 400 | `WACC0011` | Invalid cursor value |
| 400 | `EACC0005` | One or more parameters with invalid format |
| 500 | `EACC0000` | Timeout while executing the request |
| 500 | `EACC9999` | Something went wrong, please try again later |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;500`, has examples `True`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Core_platform_-_Accounts.yaml method=POST path=/accounts/v3/accounts/search operationId=post-accounts-v3-accounts-search -->
### `POST /accounts/v3/accounts/search` — List accounts by document number

- **operationId:** `post-accounts-v3-accounts-search`
- **Specification:** `api-specs/Core_platform_-_Accounts.yaml` (Core platform - Accounts)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Accounts`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Search for accounts by `document_number`. You can also optionally specify `program_ID` or `account_status`.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `page` | query | no | integer | Page number. | default: 1; format: "int32" |
| `perPage` | query | no | integer | Items per page. | default: 10; format: "int32"; minimum: 1; maximum: 100; example: 100 |

#### Request body

Required: yes

> Account sensible search fields

**Content type `application/json`** — schema: object (schema `AccountsV3Request`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `document_number` | string (schema `DocumentNumber`) | yes | Document number, such as a government tax ID. | maxLength: 15; example: "31457828046" |
| `program_id` | integer (schema `ProgramID`) | no | Program ID | format: "int64"; example: 12345 |
| `account_status` | string (schema `AccountStatus3`) | no | Account status. The pre-defined account statuses are `DEBIT_ONLY`, `NORMAL`, `BLOCKED`, and `CANCELLED`. You can create your own account statuses with the [Create status](ref:v4-post-account-status) endpoint.<br> | pattern: "^[A-Z_-]+$"; maxLength: 200; example: "NORMAL" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Account returned | `application/json`: array of object (schema `AccountsV3Response`) |
| 404 | Not found | `application/json`: object (schema `SimpleError`) |
| 500 | Internal server error | `application/json`: object |

##### Response 200

**200 `application/json` body fields:**

_No fields declared in the schema._

##### Response 404

404 Example `Account not found`:

```json
{
  "message": "Account not found"
}
```


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;404;500`, has examples `True`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Core_platform_-_Accounts.yaml method=GET path=/accounts/v1/accounts/{accountId} operationId=get-accounts-v1-accounts -->
### `GET /accounts/v1/accounts/{accountId}` — Get account

- **operationId:** `get-accounts-v1-accounts`
- **Specification:** `api-specs/Core_platform_-_Accounts.yaml` (Core platform - Accounts)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Accounts`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Get a summary of registration information related to a specific account, as well as some financial data such as its current balance.
>
> **Notes**
>
> * Some of the fields returned vary depending on whether the account was created with a `person` or `company` object as the account owner.  The `entity_type` (`INDIVIDUAL`, `COMPANY`) identifies this.
>
> * The fields `name`, `email_address`, `customer_id`, and `document_number` are either person- or company-related.
>
> * The field  `social_name` is only specific to a person.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `accountId` | path | yes | integer | Account ID | format: "int64"; minimum: 1; example: 123 |
| `show_children` | query | no | boolean | Should the response list up to 3 levels of descendant account numbers (children, grandchildren, and great-grandchildren) in the `children` array? Default is `false`.<br><br>Refer to the [Related accounts](doc:accounts-overview#related-accounts) guide section for information about the parent and child relationship between Pismo platform accounts.<br> | example: true |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `AccountDataResponse`) |
| 404 | Not found | `application/json`: object (schema `SimpleError`) |
| 500 | Internal server error | `application/json`: object (schema `SimpleError`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `account_id` | integer (schema `AccountID`) | yes | Account ID | format: "int64"; example: 1001 |
| `account_type` | string (schema `AccountType`) | no | <br>Account type:<br><br>- `PHYSICAL`&mdash;Default. A parent account is always physical. A child account can be physical or virtual.<br><br>  A *physical* card is a plastic or metal embossed card. "Physical" here means an account that represents an actual client entity (person or company). A physical account supports full operations&mdash; transfers, payments, cards, interest, statements, and so on.<br><br>- `VIRTUAL`&mdash;Always a child account.<br><br>  `parent_account_id` and `external_id` are **REQUIRED** for virtual accounts.<br><br>  Virtual accounts can have a many to one mapping to a physical account where the balance lives at the parent account.<br><br>While a `document_number` is **REQUIRED** for a virtual account, it is ignored since it shares a parent account's entity and `document_number`.<br><br>**Key difference summary**<br><br>\| Feature                        \| Physical           \| Virtual                    \|<br>\| ------------------------------ \| ------------------ \| -------------------------- \|<br>\| Fund ownership                 \| Yes                \| No (parent owns funds)     \|<br>\| Independent balance            \| Usually            \| Typically parent balance   \|<br>\| Persistent ID                  \| One account        \| Can be many to one parent  \|<br>\| Regulatory/KYC link            \| Direct             \| Inherited/indirect         \|<br>\| Primary use                    \| Real account       \| Segmentation & routing     \|<br> | enum: ["PHYSICAL", "VIRTUAL"]; example: "PHYSICAL" |
| `account_name` | string (schema `AccountName`) | no | Account name | minLength: 1; maxLength: 60; example: "Expenses account" |
| `creation_date` | string (schema `AccountCreationDate`) | yes | Date of account creation in ISO 8601 format (yyyy-mm-dd). | format: "date"; example: "2021-10-21" |
| `is_centralizer` | boolean (schema `IsCentralizer`) | no | Is this a centralizer account? A centralizer account, within the account hierarchy, is the account responsible for invoice billing. Defaults to `false`. | default: false; example: false |
| `external_id` | string (schema `AccountExternalId`) | yes | <br>Client-created ID from an external system or application. **REQUIRED** for `VIRTUAL` accounts.<br> | maxLength: 60; example: "8c8a4dd7-e48f-4c15-85b7-9d12f401057f" |
| `division_id` | integer (schema `DivisionID`) | no | Account's administrative division ID | format: "int64"; example: 2856813 |
| `customer_id` | integer (schema `CustomerID`) | yes | Customer ID | format: "int64"; example: 100211299 |
| `parent_account_id` | integer (schema `ParentAccountID`) | yes | Parent account ID. **REQUIRED** for `VIRTUAL` accounts. | format: "int64"; example: 8675309 |
| `children` | array of integer (schema `Children`) | no | Array of up to 3 levels of descendant account numbers (children, grandchildren, and great-grandchildren) | example: [121, 122, 123]; items.format: "int64" |
| `status` | string (schema `AccountStatus`) | yes | Account status. The pre-defined account statuses are `DEBIT_ONLY`, `NORMAL`, `BLOCKED`, and `CANCELLED`. You can create your own account statuses with the [Create status](ref:v4-post-account-status) endpoint.<br> | maxLength: 200; example: "NORMAL" |
| `status_reason_id` | integer (schema `StatusReasonID`) | yes | ID of the reason why the account is in its current status. You can create reasons with the [Create status reason](ref:v4-post-account-reason) endpoint.<br> | format: "int64"; minimum: 1; example: 123 |
| `status_reason_description` | string (schema `StatusReasonDescription`) | yes | Description of why the account is in its current status | maxLength: 80; example: "Registration restriction" |
| `account_status_date` | string (schema `AccountStatusDate`) | yes | Account status date. Format = yyyy-mm-dd:hr:mm:ss. | format: "date-time"; example: "2021-10-21T18:41:26.000Z" |
| `program_name` | string (schema `ProgramName`) | yes | Program name | example: "Digital wallet program" |
| `program_type` | string (schema `ProgramType`) | yes | Program type:<br>  * `CREDITO` — Full balance credit accounts<br>  * `PRE-PAGO` — Full balance prepaid accounts<br>  * `DEBITO` — Full balance debit accounts<br>  * `MERCHANT` — Merchant accounts<br>  * `CREDITO ZERO-BALANCE` — Zero balance credit accounts<br>  * `PRE-PAGO ZERO-BALANCE` — Zero balance prepaid accounts<br>  * `DEBITO ZERO-BALANCE` — Zero balance debit accounts<br>  * `CURRENT ACCOUNTS` — Current accounts<br>  * `INTERNAL ACCOUNTS` — Internal accounts<br>  * `CORRESPONDENT ACCOUNTS` — Correspondent accounts<br><br>For more information, refer to the [Program types](doc:program-types) guide.<br> | enum: ["CREDITO", "DEBITO", "PRE-PAGO", "MERCHANT", "CREDITO ZERO-BALANCE", "PRE-PAGO ZERO BALANCE", "DEBITO ZERO-BALAMCE", "CURRENT ACCOUNTS", "INTERNAL ACCOUNTS", "CORRESPONDENT ACCOUNTS"]; example: "DEBITO" |
| `program_id` | integer (schema `ProgramID`) | yes | Program ID | format: "int64"; example: 12345 |
| `org` | string (schema `OrganizationID`) | yes | Organization ID | example: "TN-34778262-f4f0-464d-b4c6-a14e2dc6f4be" |
| `entity_type` | string (schema `EntityType`) | yes | Entity type | enum: ["INDIVIDUAL", "COMPANY"]; maxLength: 10; example: "INDIVIDUAL" |
| `name` | string (schema `IndividualsName`) | yes | Name - person or company name | example: "Hyman Roth" |
| `social_name` | string (schema `SocialName`) | yes | Social name. | maxLength: 64; example: "Jack" |
| `email` | string (schema `IndividualsEmailAddress`) | yes | Email address. | format: "email"; maxLength: 100; example: "jenna.flect@email.com" |
| `document_number` | string (schema `DocumentNumber`) | yes | Document number, such as a government tax ID. | maxLength: 15; example: "31457828046" |
| `postal_address_type` | integer (schema `PostalAddressType`) | yes | ID of the mailing address registered for this account.<br> | format: "int64"; example: 1 |
| `acquisition_id` | integer (schema `AcquisitionIdOfApplicationForm`) | yes | ID of the application form that originated the account | format: "int64"; minimum: 1; example: 1234 |
| `currency_numeric_code` | string (schema `CurrencyNumericCode`) | no | ISO 4217 code for account's currency. If not defined, the Pismo platform uses the program currency code. If not defined at the program level, the platform uses the currency code defined at the organization level.<br> | maxLength: 3; example: "986" |
| `collections_status` | string (schema `CollectionStatus`) | yes | Account's financial status for credit programs | enum: ["NORMAL", "OVERDUE"]; example: "NORMAL" |
| `open_due_date` | string (schema `OpenDueDate`) | yes | Due date of currently open statement. Format = yyyy-mm-dd. | format: "date"; example: "2022-07-03" |
| `current_cicle` | integer (schema `CurrentCycle`) | yes | Current statement cycle. Every cycle is numbered sequentially starting at `1` when the account is opened.<br> | format: "int32"; example: 3 |
| `current_balance` | number (schema `CurrentBalance`) | yes | Current balance = previous balance + credits - debits. | format: "float"; example: 100.43 |
| `available_withdrawal_credit` | number (schema `AvailableWithdrawalCredit`) | yes | Amount available for withdrawal in credit programs | format: "float"; example: 100.43 |
| `available_monthly_credit` | number (schema `AvailableMonthlyCredit`) | yes | Monthly amount available in credit programs. This field is **DEPRECATED**. | format: "float"; deprecated: true; example: 100.43 |
| `available_total_installment_credit` | number (schema `AvailableTotalInstallmentCredit`) | yes | Amount available for installments in credit programs | format: "float"; example: 100.43 |
| `withdrawal_credit_limit` | number (schema `WithdrawalCreditLimit`) | yes | Amount limit for withdrawal in credit programs | format: "float"; example: 100.43 |
| `monthly_credit_limit` | number (schema `MonthlyCreditLimit`) | yes | Monthly credit limit for credit programs. This field is **DEPRECATED**. | format: "float"; deprecated: true; example: 100.43 |
| `total_installment_credit_limit` | number (schema `TotalInstallmentCreditLimit`) | yes | Amount limit for installments in credit programs | format: "float"; example: 100.43 |
| `total_credit_limit` | number (schema `TotalCreditLimit`) | yes | User-set total credit limit. This can be any value up to `max_credit_limit`. | format: "float"; example: 100.43 |
| `max_credit_limit` | number (schema `MaxCreditLimit`) | yes | Maximum credit amount approved for this account | format: "float"; example: 100.43 |
| `available_limit` | number (schema `AvailableLimit`) | yes | Amount available for this account | format: "float"; example: 100.43 |
| `blocked_amount` | number (schema `BlockedAmount`) | yes | Amount blocked in this account | format: "float"; example: 100.43 |
| `exchange_mode` | string (schema `ExchangeMode`) | yes | When a foreign transaction is charged the exchange rate:<br><br>* `SAME_DAY` - Day the transaction occurred<br>* `CLOSING` - Statement's closing date<br><br>This field is valid for credit [programs](doc:program-types) **only**.<br> | enum: ["SAME_DAY", "CLOSING"]; example: "SAME_DAY" |
| `program_due_date_id` | integer (schema `ProgramDueDateID`) | yes | ID of Program due date | format: "int64"; example: 1234 |
| `custom_fields` | string (schema `CustomFieldsString`) | yes | Key/value field for custom information. (Limited to 1014 bytes.) | example: "{\\"field_01\\": \\"value01\\", \\"field_02\\": \\"value02\\" }" |

200 Example `Account data`:

```json
{
  "acquisition_id": 123,
  "document_number": "514-08-3862",
  "entity_type": "INDIVIDUAL",
  "name": "John Doe",
  "email": "john.doe@email.com",
  "org": "TN-34778262-f4f0-464d-b4c6-a14e2dc6f4be",
  "program_name": "Digital wallet program",
  "program_type": "CREDITO",
  "status": "CANCELLED",
  "status_reason_id": 36,
  "status_reason_description": "FRAUD SUSPECTED",
  "collections_status": "NORMAL",
  "open_due_date": "2018-01-01",
  "current_cicle": 3,
  "current_balance": 100.43,
  "available_withdrawal_credit": 0,
  "available_monthly_credit": 0,
  "available_total_installment_credit": 0,
  "withdrawal_credit_limit": 0,
  "monthly_credit_limit": 0,
  "total_installment_credit_limit": 0,
  "total_credit_limit": 0,
  "max_credit_limit": 1000,
  "available_limit": 2270,
  "blocked_amount": 0.04,
  "postal_address_type": 123,
  "social_name": "John Doe",
  "exchange_mode": "SAME_DAY",
  "customer_id": 123,
  "external_id": "3ed4f6d4-ad35-4857-b1e3-dbf5d5bd4148",
  "creation_date": "2021-10-21",
  "program_due_date_id": 123,
  "account_id": 123,
  "account_status_date": "2021-10-21T18:41:26.000Z",
  "program_id": 123,
  "parent_account_id": 122,
  "custom_fields": "{ \"some_key\": \"1\" }",
  "children": [
    121,
    122,
    123
  ],
  "currency_numeric_code": "986",
  "account_type": "PHYSICAL",
  "account_name": "Account cash management"
}
```

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
  "message": "Not possible to get the account"
}
```


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;404;500`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-CORE-legal-blocks`, `KU-CRED-agreements`.

<!-- op: spec=api-specs/Core_platform_-_Accounts.yaml method=PATCH path=/accounts/v1/accounts/{accountId} operationId=patch-accounts-v1-accounts -->
### `PATCH /accounts/v1/accounts/{accountId}` — Update account

- **operationId:** `patch-accounts-v1-accounts`
- **Specification:** `api-specs/Core_platform_-_Accounts.yaml` (Core platform - Accounts)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Accounts`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Update some account information. Fields not passed are not updated.
>
> This endpoint generates an [Account information changed](https://developers.pismo.io/events/docs/account-account-change-2) event.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `accountId` | path | yes | integer | Account ID | format: "int64"; minimum: 1; example: 123 |

#### Request body

Required: no

**Content type `application/json`** — schema: object (schema `UpdateAccountInformationRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `custom_fields` | object (schema `CustomFields`) | no | Key/value field for custom information. (Limited to 1014 bytes.) | example: {"field_01": "value01", "field_02": "value02"} |
| `division_id` | integer (schema `DivisionID`) | no | Account's administrative division ID | format: "int64"; example: 2856813 |
| `account_name` | string (schema `AccountName`) | no | Account name | minLength: 1; maxLength: 60; example: "Expenses account" |
| `parent_account_id` | integer (schema `ParentAccountID2`) | no | Parent account ID. Enter `null` to unlink an account. | format: "int64"; example: 1 |
| `external_id` | string (schema `ExternalId`) | no | Customer-provided external ID field for customer monitoring and tracking. | maxLength: 60; example: "9erqwerncsodignlkd80we4ty" |
| `centralizer` | boolean (schema `IsCentralizer`) | no | Is this a centralizer account? A centralizer account, within the account hierarchy, is the account responsible for invoice billing. Defaults to `false`. | default: false; example: false |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK |  |
| 401 | Unauthorized access | `application/json`: object |
| 404 | Not found | `application/json`: object |
| 500 | Internal server error | `application/json`: object (schema `SimpleError`) |

##### Response 500

500 Example `Internal server error`:

```json
{
  "message": "Not possible to update custom fields."
}
```


#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `account-account-change-2` | https://developers.pismo.io/events/docs/account-account-change-2 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;401;404;500`, has examples `True`, emits events `1`, deprecated `False`.

Guides that link to this operation: `KU-CORE-accounts-overview`, `KU-CORE-commercial-cards`, `KU-CRED-holidays-in-credit-card-accounts`, `KU-EVT-accounts-data-events`, `KU-PAY-bacs`.

<!-- op: spec=api-specs/Core_platform_-_Accounts.yaml method=POST path=/acquisitions/v2/s2s/applications operationId=post-acquisitions-v2-s2s-applications -->
### `POST /acquisitions/v2/s2s/applications` — Create account application (deprecated)

- **operationId:** `post-acquisitions-v2-s2s-applications`
- **Specification:** `api-specs/Core_platform_-_Accounts.yaml` (Core platform - Accounts)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Accounts`
- **Deprecated in specification:** **yes**
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> This endpoint is **DEPRECATED**. Use the new [Create account application](ref:post-acquisitions-v3-s2s-applications) instead.
>
> Create a new account application.
>
> If the `submit` property is set to `false`:
> - The application is not sent for processing and can be further PATCH-ed with incremental changes.
> - This endpoint generates an [Account application prospect created](https://developers.pismo.io/events/docs/onboarding-prospect-1) event.
>
> If the `submit` flag is set to `true`:
> - No further updates can be made and the account application is sent out for processing, which creates an account and its associated structures.
> - This endpoint generates an [Account application created](https://developers.pismo.io/events/docs/onboarding-succeeded-1) event.

#### Request body

Required: yes

> Application details

**Content type `application/json`** — schema: object

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `application` | object (schema `AcquisitionRequestOutdated`) | no | Application form |  |

Example `Application Form`:

```json
{
  "application": {
    "submit": true,
    "program_id": 1,
    "due_date": 123,
    "applicant": {
      "document_number": "228-88-7742",
      "personal": {
        "name": "John Doe",
        "email": "john.doe@email.com"
      },
      "birth_date": "31/01/1980",
      "addresses": [
        {
          "address": "228-88-7742",
          "number": "12A",
          "address1": "123",
          "neighborhood": "Faraway Creek",
          "complementary_address": "Apt. 10A",
          "city": "Smallville",
          "state": "KS",
          "country": "USA",
          "zip_code": "66080",
          "address_type": "RESIDENTIAL",
          "mailing_address": true,
          "phones": [
            {
              "phone_type": "MOBILE",
              "phone": "555-1234",
              "area_code": 11,
              "country_code": 55
            }
          ]
        }
      ],
      "account": {
        "external_id": "b9215aa7-4f88-4154-9d86-52b3662f28ac"
      }
    }
  }
}
```

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | Created | `application/json`: object (schema `AcquisitionResponse`) |
| 400 | Bad request | `application/json`: object (schema `AccountDuplicityByExternalIdError`) |
| 409 | Conflict | `application/json`: object (schema `SimpleError`) |
| 500 | Internal server error | `application/json`: object (schema `SimpleError`) |

##### Response 201

**201 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `application_id` | integer (schema `ApplicationIdNonchecking`) | yes | Application form ID (non-checking accounts only) | format: "int64"; example: 1234 |
| `status` | integer (schema `ApplicationStatusIdNonchecking`) | yes | Application status ID | format: "int64"; example: 4 |
| `status_name` | string (schema `ApplicationStatusNameNonchecking`) | yes | Application status. Most likely to be<br>* `REGISTERED` - Application was saved, but not started processing yet.<br>* `APPROVED` - Application has finished processing.<br>* `PROSPECT` - Application was created with `submit` = `false`.<br> | example: "APPROVED" |
| `account_id` | integer (schema `AccountIdNonchecking`) | yes | Created account ID. `null` if the application has not been proccessed yet (non-checking accounts only). | format: "int64"; example: 123 |
| `customer_id` | integer (schema `CustomerIdNonchecking`) | yes | Created customer ID. `null` if the application has not yet been proccessed (non-checking accounts only). | format: "int64"; example: 123 |
| `entity_id` | integer (schema `EntityID2`) | yes | Created entity ID. `null` if the application has not yet been proccessed (non-checking accounts only). | format: "int64"; example: 123 |
| `program_id` | integer (schema `ProgramID`) | yes | Program ID | format: "int64"; example: 12345 |

201 Example `Application created`:

```json
{
  "application_id": 23942777,
  "status": 4,
  "status_name": "APPROVED",
  "account_id": 123,
  "customer_id": 456,
  "entity_id": 789,
  "program_id": 100
}
```

##### Response 400

400 Example `Bad channel`:

```json
{
  "message": "Invalid acquisition channel"
}
```

400 Example `Duplicity By External Id`:

```json
{
  "message": "Account with same external id already registered",
  "org_id": "TN-34778262-f4f0-464d-b4c6-a14e2dc6f4be",
  "account_id": 123,
  "application_id": 23942777,
  "customer_id": 456,
  "entity_id": 789,
  "program_id": 100
}
```

##### Response 409

409 Example `Account conflict`:

```json
{
  "message": "Account already created"
}
```

##### Response 500

500 Example `Internal server error`:

```json
{
  "message": "Error registering application"
}
```


#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `onboarding-prospect-1` | https://developers.pismo.io/events/docs/onboarding-prospect-1 |
| `onboarding-succeeded-1` | https://developers.pismo.io/events/docs/onboarding-succeeded-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `201;400;409;500`, has examples `True`, emits events `2`, deprecated `True`.

Guides that link to this operation: `KU-EVT-accounts-data-events`.

<!-- op: spec=api-specs/Core_platform_-_Accounts.yaml method=GET path=/accounts/v4/accounts/{accountId}/hierarchy/ascendants operationId=get-accounts-v4-accounts-accountId-hierarchy-ascendants -->
### `GET /accounts/v4/accounts/{accountId}/hierarchy/ascendants` — Get account hierarchy ascendants

- **operationId:** `get-accounts-v4-accounts-accountId-hierarchy-ascendants`
- **Specification:** `api-specs/Core_platform_-_Accounts.yaml` (Core platform - Accounts)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Accounts`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Get account hierarchy information including all parent/ancestor accounts.
>
> This endpoint returns the account details along with an array of all parent accounts in the hierarchy, with each parent containing information about its level, centralizer status, and relationship to other accounts in the hierarchy.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `accountId` | path | yes | integer | Account ID | format: "int64"; minimum: 1; example: 123 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `AccountHierarchyResponse`) |
| 400 | Bad request | `application/json`: object (schema `MessageResponse`) |
| 404 | Not found | `application/json`: object (schema `MessageResponse`) |
| 500 | Internal server error | `application/json`: object (schema `MessageResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `account_id` | integer (schema `AccountID`) | no | Account ID | format: "int64"; example: 1001 |
| `name` | string (schema `IndividualsName`) | no | Name - person or company name | example: "Hyman Roth" |
| `document_number` | string (schema `DocumentNumber`) | no | Document number, such as a government tax ID. | maxLength: 15; example: "31457828046" |
| `customer_id` | integer (schema `CustomerID`) | no | Customer ID | format: "int64"; example: 100211299 |
| `social_name` | string (schema `SocialName`) | no | Social name. | maxLength: 64; example: "Jack" |
| `entity_id` | integer (schema `EntityID`) | no | Entity ID | format: "int64"; minimum: 1; example: 1234567891 |
| `program_id` | integer (schema `ProgramID`) | no | Program ID | format: "int64"; example: 12345 |
| `status` | string (schema `AccountStatus`) | no | Account status. The pre-defined account statuses are `DEBIT_ONLY`, `NORMAL`, `BLOCKED`, and `CANCELLED`. You can create your own account statuses with the [Create status](ref:v4-post-account-status) endpoint.<br> | maxLength: 200; example: "NORMAL" |
| `postal_address_id` | integer (schema `PostalAddressID`) | no | Postal address ID | format: "int64"; example: 456 |
| `creation_datetime` | string (schema `AccountCreationDatetime`) | no | Account creation date/time in UTC. Format = yyyy-mm-dd:hr:mm:ss. | format: "date-time"; example: "2017-07-21T17:32:28Z" |
| `external_id` | string (schema `AccountExternalId`) | no | <br>Client-created ID from an external system or application. **REQUIRED** for `VIRTUAL` accounts.<br> | maxLength: 60; example: "8c8a4dd7-e48f-4c15-85b7-9d12f401057f" |
| `account_type` | string (schema `AccountType`) | no | <br>Account type:<br><br>- `PHYSICAL`&mdash;Default. A parent account is always physical. A child account can be physical or virtual.<br><br>  A *physical* card is a plastic or metal embossed card. "Physical" here means an account that represents an actual client entity (person or company). A physical account supports full operations&mdash; transfers, payments, cards, interest, statements, and so on.<br><br>- `VIRTUAL`&mdash;Always a child account.<br><br>  `parent_account_id` and `external_id` are **REQUIRED** for virtual accounts.<br><br>  Virtual accounts can have a many to one mapping to a physical account where the balance lives at the parent account.<br><br>While a `document_number` is **REQUIRED** for a virtual account, it is ignored since it shares a parent account's entity and `document_number`.<br><br>**Key difference summary**<br><br>\| Feature                        \| Physical           \| Virtual                    \|<br>\| ------------------------------ \| ------------------ \| -------------------------- \|<br>\| Fund ownership                 \| Yes                \| No (parent owns funds)     \|<br>\| Independent balance            \| Usually            \| Typically parent balance   \|<br>\| Persistent ID                  \| One account        \| Can be many to one parent  \|<br>\| Regulatory/KYC link            \| Direct             \| Inherited/indirect         \|<br>\| Primary use                    \| Real account       \| Segmentation & routing     \|<br> | enum: ["PHYSICAL", "VIRTUAL"]; example: "PHYSICAL" |
| `account_name` | string (schema `AccountName`) | no | Account name | minLength: 1; maxLength: 60; example: "Expenses account" |
| `division_id` | integer (schema `DivisionID`) | no | Account's administrative division ID | format: "int64"; example: 2856813 |
| `currency_numeric_code` | string (schema `CurrencyNumericCode`) | no | ISO 4217 code for account's currency. If not defined, the Pismo platform uses the program currency code. If not defined at the program level, the platform uses the currency code defined at the organization level.<br> | maxLength: 3; example: "986" |
| `parents` | array of object (schema `HierarchyParent`) (schema `HierarchyParents`) | no | Array of parent accounts in the hierarchy |  |

200 Example `Account with hierarchy`:

```json
{
  "account_id": 123,
  "name": "John Doe",
  "document_number": "31457828046",
  "customer_id": 456,
  "social_name": "Johnny",
  "entity_id": 789,
  "program_id": 100,
  "status": "NORMAL",
  "postal_address_id": 111,
  "creation_datetime": "2021-07-21T17:32:28Z",
  "external_id": "8c8a4dd7-e48f-4c15-85b7-9d12f401057f",
  "account_type": "PHYSICAL",
  "account_name": "Main Account",
  "division_id": 222,
  "currency_numeric_code": "986",
  "parents": [
    {
      "account_id": 124,
      "is_centralizer": false,
      "level": 1,
      "parent_account_id": 125,
      "currency_numeric_code": "986",
      "program_id": 100,
      "division_id": 222
    },
    {
      "account_id": 125,
      "is_centralizer": true,
      "level": 2,
      "parent_account_id": 8675309,
      "currency_numeric_code": "986",
      "program_id": 100,
      "division_id": 222
    }
  ]
}
```

##### Response 400

400 Example `Invalid account ID`:

```json
{
  "code": "EACC0005",
  "message": "One or more parameters with invalid format",
  "detail": {
    "parameters": [
      {
        "field": "accountId",
        "message": "Value must be a valid integer"
      }
    ]
  }
}
```

##### Response 404

404 Example `Account not found`:

```json
{
  "code": "WACC0017",
  "message": "Account not found"
}
```

##### Response 500

500 Example `Timeout execution`:

```json
{
  "code": "EACC0000",
  "message": "Timeout while executing the request"
}
```

500 Example `Generic message`:

```json
{
  "code": "EACC9999",
  "message": "Something went wrong, please try again later"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `EACC0005` | One or more parameters with invalid format |
| 404 | `WACC0017` | Account not found |
| 500 | `EACC0000` | Timeout while executing the request |
| 500 | `EACC9999` | Something went wrong, please try again later |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;404;500`, has examples `True`, emits events `0`, deprecated `False`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/AcquisitionRequestV3 -->
### Schema `AcquisitionRequestV3`

Pointer: `#/components/schemas/AcquisitionRequestV3`. Type: object (schema `AcquisitionRequestV3`).

> Application form

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `submit` | boolean (schema `Submit`) | yes | Should form be processed now (`true`), or later after adding more information (`false`). | example: true |
| `applicant` | object (schema `Applicant`) | yes | Applicant's details |  |
| `acquisition_channel` | integer (schema `AcquisitionChannelID`) | no | Application's acquisition channel ID. An acquisition channel is how a customer was referred to the site, such as through a web app or mobile app.<br><br>You can call [List acquistion channels](ref:get-acquisitions-v2-programs-programid-channels) to find channels registered for your account.<br> | format: "int64"; example: 111 |
| `program_id` | integer (schema `ProgramID2`) | no | Program ID. **REQUIRED** when `acquisition_channel` is not passed. | format: "int64"; example: 111 |
| `due_date` | integer (schema `AccountDueDateID`) | no | Program due date ID. This field is **REQUIRED** only for Full balance credit programs.<br><br>Program due dates and their IDs are set when you [create a program](ref:createprogrambasedontemplate).<br> | format: "int64"; example: 222 |
| `program_calendar_strategy_id` | number (schema `ProgramCalendarStrategyID`) | no | Program calendar strategy ID.<br><br>The program calendar strategy determines how program calendars are created.<br><br>For more information, refer to the [Create program calendar strategy](ref:createprogramcalendarstrategy) endpoint. This endpoint returns an ID you can pass here.<br> | example: 8675309 |

<!-- schema: #/components/schemas/SimpleError -->
### Schema `SimpleError`

Pointer: `#/components/schemas/SimpleError`. Type: object (schema `SimpleError`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `message` | string | yes | Error message |  |

<!-- schema: #/components/schemas/AcquisitionRequestUpdate -->
### Schema `AcquisitionRequestUpdate`

Pointer: `#/components/schemas/AcquisitionRequestUpdate`. Type: object (schema `AcquisitionRequestUpdate`).

> Application form

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `submit` | boolean (schema `Submit`) | no | Should form be processed now (`true`), or later after adding more information (`false`). | example: true |
| `prospect_cancel` | boolean (schema `ProspectCancel`) | no | Should prospect be canceled (`true`), or can more information be added later (`false`).<br> | example: true |
| `applicant` | object (schema `Applicant2`) | no | Applicant's details |  |

<!-- schema: #/components/schemas/AcquisitionChannelItemResponse -->
### Schema `AcquisitionChannelItemResponse`

Pointer: `#/components/schemas/AcquisitionChannelItemResponse`. Type: object (schema `AcquisitionChannelItemResponse`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | integer (schema `AcquisitionChannelID`) | yes | Application's acquisition channel ID. An acquisition channel is how a customer was referred to the site, such as through a web app or mobile app.<br><br>You can call [List acquistion channels](ref:get-acquisitions-v2-programs-programid-channels) to find channels registered for your account.<br> | format: "int64"; example: 111 |
| `type` | string (schema `AcquisitionChannelType`) | yes | Acquisition channel type | example: "Mobile app" |
| `name` | string (schema `AcquisitionChannelName`) | yes | Acquisition channel name | example: "Android app" |

<!-- schema: #/components/schemas/AccountsV5Response -->
### Schema `AccountsV5Response`

Pointer: `#/components/schemas/AccountsV5Response`. Type: object (schema `AccountsV5Response`).

> Object response for account

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `account_id` | integer (schema `AccountID`) | no | Account ID | format: "int64"; example: 1001 |
| `account_external_id` | string (schema `AccountExternalId`) | no | <br>Client-created ID from an external system or application. **REQUIRED** for `VIRTUAL` accounts.<br> | maxLength: 60; example: "8c8a4dd7-e48f-4c15-85b7-9d12f401057f" |
| `is_centralizer` | boolean (schema `IsCentralizer`) | no | Is this a centralizer account? A centralizer account, within the account hierarchy, is the account responsible for invoice billing. Defaults to `false`. | default: false; example: false |
| `entities` | array of object (schema `AccountEntityResponseV5`) | no | List of account's entities |  |

<!-- schema: #/components/schemas/MessageResponse -->
### Schema `MessageResponse`

Pointer: `#/components/schemas/MessageResponse`. Type: object (schema `MessageResponse`).

> Object response for user message

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string (schema `UserMessageCode`) | no | Code that identifies the user message | example: "EACC0000" |
| `message` | string (schema `UserMessage`) | no | User message | example: "Timeout while executing the request" |
| `details` | object (schema `MessageDetailsResponse`) | no | Object response for a user message |  |

<!-- schema: #/components/schemas/AcquisitionRequestOutdated -->
### Schema `AcquisitionRequestOutdated`

Pointer: `#/components/schemas/AcquisitionRequestOutdated`. Type: object (schema `AcquisitionRequestOutdated`).

> Application form

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `submit` | boolean (schema `Submit`) | yes | Should form be processed now (`true`), or later after adding more information (`false`). | example: true |
| `acquisition_channel` | integer (schema `AcquisitionChannelID`) | no | Application's acquisition channel ID. An acquisition channel is how a customer was referred to the site, such as through a web app or mobile app.<br><br>You can call [List acquistion channels](ref:get-acquisitions-v2-programs-programid-channels) to find channels registered for your account.<br> | format: "int64"; example: 111 |
| `program_id` | integer (schema `ProgramID2`) | no | Program ID. **REQUIRED** when `acquisition_channel` is not passed. | format: "int64"; example: 111 |
| `due_date` | integer (schema `AccountDueDateID`) | no | Program due date ID. This field is **REQUIRED** only for Full balance credit programs.<br><br>Program due dates and their IDs are set when you [create a program](ref:createprogrambasedontemplate).<br> | format: "int64"; example: 222 |
| `applicant` | object (schema `Applicant2`) | yes | Applicant's details |  |

<!-- schema: #/components/schemas/AccountDuplicityByExternalIdError -->
### Schema `AccountDuplicityByExternalIdError`

Pointer: `#/components/schemas/AccountDuplicityByExternalIdError`. Type: object (schema `AccountDuplicityByExternalIdError`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `message` | string | yes | Message describing the error |  |
| `org_id` | string (schema `OrganizationID`) | no | Organization ID | example: "TN-34778262-f4f0-464d-b4c6-a14e2dc6f4be" |
| `account_id` | integer (schema `AccountID`) | no | Account ID | format: "int64"; example: 1001 |
| `application_id` | integer (schema `ApplicationID`) | no | Application ID | format: "int64" |
| `customer_id` | integer (schema `CustomerID`) | no | Customer ID | format: "int64"; example: 100211299 |
| `entity_id` | integer (schema `EntityID`) | no | Entity ID | format: "int64"; minimum: 1; example: 1234567891 |
| `program_id` | integer (schema `ProgramID`) | no | Program ID | format: "int64"; example: 12345 |

<!-- schema: #/components/schemas/HierarchyParent -->
### Schema `HierarchyParent`

Pointer: `#/components/schemas/HierarchyParent`. Type: object (schema `HierarchyParent`).

> Parent account information in the hierarchy

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `account_id` | integer (schema `AccountID`) | no | Account ID | format: "int64"; example: 1001 |
| `is_centralizer` | boolean (schema `IsCentralizer`) | no | Is this a centralizer account? A centralizer account, within the account hierarchy, is the account responsible for invoice billing. Defaults to `false`. | default: false; example: false |
| `level` | integer | no | Hierarchy level (`1` = direct parent, `2` = grandparent, and so on.) | format: "int32"; example: 1 |
| `parent_account_id` | integer (schema `AccountID`) | no | Account ID | format: "int64"; example: 1001 |
| `currency_numeric_code` | string (schema `CurrencyNumericCode`) | no | ISO 4217 code for account's currency. If not defined, the Pismo platform uses the program currency code. If not defined at the program level, the platform uses the currency code defined at the organization level.<br> | maxLength: 3; example: "986" |
| `program_id` | integer (schema `ProgramID`) | no | Program ID | format: "int64"; example: 12345 |
| `division_id` | integer (schema `DivisionID`) | no | Account's administrative division ID | format: "int64"; example: 2856813 |
| `external_account_id` | string (schema `AccountExternalId`) | no | <br>Client-created ID from an external system or application. **REQUIRED** for `VIRTUAL` accounts.<br> | maxLength: 60; example: "8c8a4dd7-e48f-4c15-85b7-9d12f401057f" |

<!-- schema: #/components/schemas/Applicant -->
### Schema `Applicant`

Pointer: `#/components/schemas/Applicant`. Type: object (schema `Applicant`).

> Applicant's details

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `document_number` | string (schema `DocumentNumberSetOnce`) | yes | Applicant's document number (such as a government tax ID).<br><br>For a company, this can be something like its tax or business registration number.<br><br>**Important**: Once passed, this value **CANNOT** be changed, even if `submit` is `false`.<br> | maxLength: 15; example: "12345678910" |
| `birth_date` | string (schema `BirthDate2`) | no | Birth date. Format = yyyy-mm-dd.<br><br>For a company, this can be the company creation date.<br> | format: "date"; example: "1991-11-27" |
| `personal` | object (schema `ApplicantPersonal`) | no | Applicant's personal information. Either this or the `company` object is **REQUIRED**. Pass one or the other but not both. |  |
| `company` | object (schema `ApplicantCompany`) | no | Applicant's company information. Either this or the `personal` object is **REQUIRED**. Pass one or the other but not both. |  |
| `account` | object (schema `ApplicantAccount`) | no | Applicant's account options |  |
| `addresses` | array of object (schema `ApplicantAddresses`) | no | List of addresses |  |
| `addresses[].address` | string (schema `Address`) | yes | Street, avenue, road, and so on, name. | maxLength: 300; example: "Mulholland Drive" |
| `addresses[].number` | string (schema `AddressNumberInput`) | no | Address number as string or integer.<br><br>If you enter numeric characters, they are saved in the `number` address object field.<br><br>If you enter any non-numeric characters, all characters are saved in the `extended_number` address object field.<br><br>For example, if you enter "12 A", it gets saved as follows:<br>  *  `number` = 12<br>  *  `extended_number` = "12 A"<br> | maxLength: 9 |
| `addresses[].city` | string (schema `City`) | yes | Address city | maxLength: 100; example: "San Diego" |
| `addresses[].state` | string (schema `State2`) | yes | Address state | maxLength: 30; example: "California" |
| `addresses[].country` | string (schema `Country`) | yes | Address country | maxLength: 30; example: "Brazil" |
| `addresses[].address_type` | string (schema `AddressType`) | yes | Address type | enum: ["RESIDENTIAL", "COMMERCIAL", "OTHER"]; example: "RESIDENTIAL" |
| `addresses[].zip_code` | string (schema `ZipCode`) | yes | Zip/postal code | maxLength: 16; example: "12345-678" |
| `addresses[].neighborhood` | string (schema `Neighborhood`) | yes | Address neighborhood. Some countries use neighborhood in addresses. | maxLength: 100; example: "Shady Pines" |
| `addresses[].complementary_address` | string (schema `ComplementaryAddress`) | no | Any additional information such as suite, apt., and so on. | maxLength: 100; example: "Apt 1408" |
| `addresses[].mailing_address` | boolean (schema `MailingAddress`) | no | Is this address the mailing address?<br><br>Only one address can have this field set to `true`.<br> | example: true |
| `addresses[].custom_fields` | object (schema `CustomFields`) | no | Key/value field for custom information. (Limited to 1014 bytes.) | example: {"field_01": "value01", "field_02": "value02"} |
| `phones` | array of object (schema `ApplicantPhonesV3`) | no | List of phone numbers |  |
| `phones[].phone` | string (schema `PhoneNumber`) | yes | Phone number | maxLength: 15; example: "11912345678" |
| `phones[].phone_type` | string (schema `PhoneType`) | yes | Phone number type | enum: ["RESIDENTIAL", "COMMERCIAL", "MOBILE"]; example: "MOBILE" |
| `phones[].country_code` | string (schema `PhoneCountryCode`) | yes | Phone number's country code | maxLength: 5; example: "555" |
| `phones[].area_code` | integer (schema `AreaCode2`) | no | Phone number area code | format: "int32"; example: 11 |
| `phones[].extension` | string (schema `PhoneExtension`) | no | Optional phone number extension | maxLength: 10; example: "ext. 9" |
| `custom_fields` | object (schema `CustomFields`) | no | Key/value field for custom information. (Limited to 1014 bytes.) | example: {"field_01": "value01", "field_02": "value02"} |

<!-- schema: #/components/schemas/Applicant2 -->
### Schema `Applicant2`

Pointer: `#/components/schemas/Applicant2`. Type: object (schema `Applicant2`).

> Applicant's details

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `document_number` | string (schema `DocumentNumberSetOnce`) | yes | Applicant's document number (such as a government tax ID).<br><br>For a company, this can be something like its tax or business registration number.<br><br>**Important**: Once passed, this value **CANNOT** be changed, even if `submit` is `false`.<br> | maxLength: 15; example: "12345678910" |
| `birth_date` | string (schema `BirthDate`) | no | Birth date. Format = dd/mm/yyyy. | example: "31/12/1980" |
| `personal` | object (schema `ApplicantPersonal`) | no | Applicant's personal information. Either this or the `company` object is **REQUIRED**. Pass one or the other but not both. |  |
| `company` | object (schema `ApplicantCompany`) | no | Applicant's company information. Either this or the `personal` object is **REQUIRED**. Pass one or the other but not both. |  |
| `account` | object (schema `ApplicantAccount`) | no | Applicant's account options |  |
| `addresses` | array of object (schema `ApplicantAddresses`) | no | List of addresses |  |
| `addresses[].address` | string (schema `Address`) | yes | Street, avenue, road, and so on, name. | maxLength: 300; example: "Mulholland Drive" |
| `addresses[].number` | string (schema `AddressNumberInput`) | no | Address number as string or integer.<br><br>If you enter numeric characters, they are saved in the `number` address object field.<br><br>If you enter any non-numeric characters, all characters are saved in the `extended_number` address object field.<br><br>For example, if you enter "12 A", it gets saved as follows:<br>  *  `number` = 12<br>  *  `extended_number` = "12 A"<br> | maxLength: 9 |
| `addresses[].city` | string (schema `City`) | yes | Address city | maxLength: 100; example: "San Diego" |
| `addresses[].state` | string (schema `State2`) | yes | Address state | maxLength: 30; example: "California" |
| `addresses[].country` | string (schema `Country`) | yes | Address country | maxLength: 30; example: "Brazil" |
| `addresses[].address_type` | string (schema `AddressType`) | yes | Address type | enum: ["RESIDENTIAL", "COMMERCIAL", "OTHER"]; example: "RESIDENTIAL" |
| `addresses[].zip_code` | string (schema `ZipCode`) | yes | Zip/postal code | maxLength: 16; example: "12345-678" |
| `addresses[].neighborhood` | string (schema `Neighborhood`) | yes | Address neighborhood. Some countries use neighborhood in addresses. | maxLength: 100; example: "Shady Pines" |
| `addresses[].complementary_address` | string (schema `ComplementaryAddress`) | no | Any additional information such as suite, apt., and so on. | maxLength: 100; example: "Apt 1408" |
| `addresses[].mailing_address` | boolean (schema `MailingAddress`) | no | Is this address the mailing address?<br><br>Only one address can have this field set to `true`.<br> | example: true |
| `addresses[].custom_fields` | object (schema `CustomFields`) | no | Key/value field for custom information. (Limited to 1014 bytes.) | example: {"field_01": "value01", "field_02": "value02"} |
| `custom_fields` | object (schema `CustomFields`) | no | Key/value field for custom information. (Limited to 1014 bytes.) | example: {"field_01": "value01", "field_02": "value02"} |

<!-- schema: #/components/schemas/AccountEntityResponseV5 -->
### Schema `AccountEntityResponseV5`

Pointer: `#/components/schemas/AccountEntityResponseV5`. Type: object (schema `AccountEntityResponseV5`).

> Account entity

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `entity_id` | integer (schema `EntityID`) | no | Entity ID | format: "int64"; minimum: 1; example: 1234567891 |
| `entity_external_id` | string (schema `AccountExternalId`) | no | <br>Client-created ID from an external system or application. **REQUIRED** for `VIRTUAL` accounts.<br> | maxLength: 60; example: "8c8a4dd7-e48f-4c15-85b7-9d12f401057f" |

<!-- schema: #/components/schemas/MessageDetailsResponse -->
### Schema `MessageDetailsResponse`

Pointer: `#/components/schemas/MessageDetailsResponse`. Type: object (schema `MessageDetailsResponse`).

> Object response for a user message

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `payload` | array of object (schema `MessagePayloadResponse`) | no | Details for the request payload errors |  |
| `parameters` | array of object (schema `MessageParameterResponse`) | no | Details for the query parameter errors |  |
| `external` | array of object (schema `MessageExternalResponse`) | no | Details for the external service error |  |

<!-- schema: #/components/schemas/ApplicantPersonal -->
### Schema `ApplicantPersonal`

Pointer: `#/components/schemas/ApplicantPersonal`. Type: object (schema `ApplicantPersonal`).

> Applicant's personal information. Either this or the `company` object is **REQUIRED**. Pass one or the other but not both.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `external_id` | string (schema `PersonalExternalId`) | no | Client-supplied personal ID from an external system or application. | maxLength: 60; example: "8c8a4dd7-e48f-4c15-85b7-9d12f401057f" |
| `name` | string (schema `IndividualsName2`) | no | Name. **REQUIRED** if `social_name` is not provided. | maxLength: 150; example: "Hyman Roth" |
| `email` | string (schema `IndividualsEmailAddress`) | no | Email address. | format: "email"; maxLength: 100; example: "jenna.flect@email.com" |
| `gender` | string (schema `Gender`) | no | Gender | enum: ["F", "M", ""]; maxLength: 1; example: "M" |
| `printed_name` | string (schema `PrintedName2`) | no | <br>This field is **DEPRECATED**. Cards is now responsible for this field.<br><br>Name to be printed on the card. **REQUIRED** if `name` and `social_name` are not provided.<br><br>Punctuation, special characters, and connectors (da/das/de/do/dos/e) are always removed.<br><br>This field's maximum length is 25, but you can set it to a lower value at the program level with the `Max name length on physical card` program parameter.<br> | maxLength: 25; deprecated: true; example: "John Doe" |
| `nickname` | string (schema `Nickname`) | no | Nickname. | maxLength: 128; example: "Pinto" |
| `social_name` | string (schema `SocialName2`) | no | Social name. **REQUIRED** if `name` is not provided. | maxLength: 64; example: "Terminator" |
| `country_of_birth` | string (schema `CountryOfBirth`) | no | Birth country | maxLength: 60; example: "India" |
| `state_of_birth` | string (schema `StateOfBirth`) | no | Birth state | maxLength: 60; example: "California" |
| `city_of_birth` | string (schema `CityOfBirth`) | no | Birth city | maxLength: 60; example: "San Diego" |
| `registration` | object (schema `ApplicantRegistration`) | no | Applicant's document information |  |
| `education_degree` | string (schema `EducationDegree`) | no | Education degree | maxLength: 30 |
| `marital_status` | string (schema `MaritalStatus`) | no | Marital status | enum: ["SINGLE", "MARRIED", "DIVORCED", "WIDOWER"]; example: "MARRIED" |
| `fathers_name` | string (schema `FathersName`) | no | Father's name | maxLength: 60; example: "Steven Douglas" |
| `mothers_name` | string (schema `MothersName`) | no | Mother's name | maxLength: 60; example: "Kay Sadilla" |
| `nationality` | string (schema `Nationality`) | no | Nationality | maxLength: 60; example: "Australian" |
| `other_id_number` | string (schema `OtherIdNumber`) | no | Another ID number | example: "29000000" |
| `document_type` | string (schema `DocumentType`) | no | Document type. Free-form field, not an enum. | maxLength: 30 |
| `document_issued_by` | string (schema `DocumentIssuedBy`) | no | Document issuer | maxLength: 30 |
| `document_issued_at` | string (schema `DocumentIssuedAt`) | no | Document issuer location. This is a free-form field, not an ISO standard. | maxLength: 30; example: "Brazil" |
| `document_issued_date` | string (schema `DocumentIssuedDate`) | no | Date document was issued. Format = dd/mm/yyyy. | example: "01/31/1970" |
| `occupation` | string (schema `ApplicantOccupation`) | no | Applicant's occupation | maxLength: 60; example: "Creative Accountant" |
| `assets` | number (schema `Assets`) | no | Assets | format: "float"; example: 40000 |
| `income` | integer (schema `ApplicantIncome2`) | no | Applicant's income | format: "int64"; example: 4000 |
| `net_worth` | integer (schema `ApplicantNetWorth`) | no | Applicant's net worth | format: "int64"; example: 20000 |
| `pep` | boolean (schema `PEP`) | no | Is this person a Politically Exposed Person (PEP)? Pismo doesn't do anything differently for a PEP, this is just additional account information. Default is `false`.<br> | example: false |
| `statutory` | boolean (schema `Statutory`) | no | Is person statutory? A statutory employee is defined as an employee by law under a specific statute. Pismo doesn't do anything differently in this case, it is simply additional account information. Default is `false`.<br> | example: false |

<!-- schema: #/components/schemas/ApplicantCompany -->
### Schema `ApplicantCompany`

Pointer: `#/components/schemas/ApplicantCompany`. Type: object (schema `ApplicantCompany`).

> Applicant's company information. Either this or the `personal` object is **REQUIRED**. Pass one or the other but not both.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `external_id` | string (schema `CompanyExternalId`) | no | Client-provided company ID from an external system. | maxLength: 60; example: "8c8a4dd7-e48f-4c15-85b7-9d12f401057f" |
| `name` | string (schema `CompanyName`) | yes | Company's legal name | maxLength: 150; example: "Acme Inc." |
| `email` | string (schema `CompanyEmail`) | no | Company's registered email | maxLength: 100; example: "acme@acmemail.com" |
| `company_name` | string (schema `CompanyBrandName`) | no | Company's brand name | maxLength: 60; example: "Acme General Products" |
| `registration_number` | string (schema `RegistrationNumber`) | no | Company's registration number with local authorities | maxLength: 30; example: "ACM10004" |
| `activity` | string (schema `Activity`) | no | Company's general field of activity | maxLength: 30; example: "Manufacturing" |
| `company_type` | string (schema `CompanyType`) | no | Company type | maxLength: 60; example: "Retailer" |
| `company_format` | string (schema `CompanyFormat`) | no | Company social type | maxLength: 60; example: "ME" |
| `company_constitution_date` | string (schema `CompanyConstitutionDate`) | no | Company's operational start date. Format = yyyy-mm-dd. | format: "date"; example: "2004-01-20" |
| `occupation` | string (schema `CompanyOccupation`) | no | Company's main occupation | maxLength: 60; example: "Online retail" |
| `income` | integer (schema `CompanyIncome`) | no | Company's income | format: "int64"; example: 10000 |
| `net_worth` | integer (schema `CompanyNetWorth`) | no | Company's net worth | format: "int64"; example: 20000 |
| `annual_revenues` | integer (schema `AverageMonthlyRevenue`) | no | Average monthly revenue for the last 12 months | format: "int64"; example: 33000 |
| `type` | string (schema `CompanyBusinessRelationsType`) | no | Company's business relations type | maxLength: 60; example: "B2C" |
| `number_of_partners` | integer (schema `NumberOfPartners`) | no | Number of company partners | format: "int32"; example: 3 |
| `perc_ownership` | integer (schema `PercOwnership2`) | no | Company percentage ownership | format: "int64"; example: 50 |
| `fiscal_situation` | string (schema `FiscalSituation`) | no | Company's fiscal situation. | maxLength: 60; example: "Good" |
| `debt` | integer (schema `CompanyDebt`) | no | Company's debt | format: "int64"; example: 18000 |
| `partners` | array of object (schema `Partner`) | no | Company partners |  |

<!-- schema: #/components/schemas/ApplicantAccount -->
### Schema `ApplicantAccount`

Pointer: `#/components/schemas/ApplicantAccount`. Type: object (schema `ApplicantAccount`).

> Applicant's account options

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `currency_numeric_code` | string (schema `CurrencyNumericCode`) | no | ISO 4217 code for account's currency. If not defined, the Pismo platform uses the program currency code. If not defined at the program level, the platform uses the currency code defined at the organization level.<br> | maxLength: 3; example: "986" |
| `granted_limit` | number (schema `GrantedLimit`) | no | Account's credit limit.<br><br>**REQUIRED** for credit programs.<br><br>This field is called  `max_credit_limit` in the [Update account limits](https://developers.pismo.io/pismo-docs/reference/patch-v1-account-limit) endpoint and the [Account limits](https://developers.pismo.io/pismo-docs/docs/working-with-limits-objects) guide.<br> | format: "float"; example: 1500 |
| `limit` | number (schema `AccountLimit`) | no | <br>Client-defined account limit. Must be between 0 and the `granted_limit` (aka `max_credit_limit`).<br><br>Defaults to zero (0) if not passed.<br><br> This field is called  `total_credit_limit` in the [Update account limits](https://developers.pismo.io/pismo-docs/reference/patch-v1-account-limit) endpoint and the [Account limits](https://developers.pismo.io/pismo-docs/docs/working-with-limits-objects) guide.<br> | format: "float"; example: 750 |
| `exchange_mode` | string (schema `ExchangeMode`) | no | When a foreign transaction is charged the exchange rate:<br><br>* `SAME_DAY` - Day the transaction occurred<br>* `CLOSING` - Statement's closing date<br><br>This field is valid for credit [programs](doc:program-types) **only**.<br> | enum: ["SAME_DAY", "CLOSING"]; example: "SAME_DAY" |
| `external_id` | string (schema `AccountExternalId`) | no | <br>Client-created ID from an external system or application. **REQUIRED** for `VIRTUAL` accounts.<br> | maxLength: 60; example: "8c8a4dd7-e48f-4c15-85b7-9d12f401057f" |
| `parent_account_id` | integer (schema `ParentAccountID`) | no | Parent account ID. **REQUIRED** for `VIRTUAL` accounts. | format: "int64"; example: 8675309 |
| `overdraft_limit` | number (schema `OverdraftLimit`) | no | Maximum issuer-granted limit for overdraft spending on debit accounts | format: "float"; example: 750 |
| `account_type` | string (schema `AccountType`) | no | <br>Account type:<br><br>- `PHYSICAL`&mdash;Default. A parent account is always physical. A child account can be physical or virtual.<br><br>  A *physical* card is a plastic or metal embossed card. "Physical" here means an account that represents an actual client entity (person or company). A physical account supports full operations&mdash; transfers, payments, cards, interest, statements, and so on.<br><br>- `VIRTUAL`&mdash;Always a child account.<br><br>  `parent_account_id` and `external_id` are **REQUIRED** for virtual accounts.<br><br>  Virtual accounts can have a many to one mapping to a physical account where the balance lives at the parent account.<br><br>While a `document_number` is **REQUIRED** for a virtual account, it is ignored since it shares a parent account's entity and `document_number`.<br><br>**Key difference summary**<br><br>\| Feature                        \| Physical           \| Virtual                    \|<br>\| ------------------------------ \| ------------------ \| -------------------------- \|<br>\| Fund ownership                 \| Yes                \| No (parent owns funds)     \|<br>\| Independent balance            \| Usually            \| Typically parent balance   \|<br>\| Persistent ID                  \| One account        \| Can be many to one parent  \|<br>\| Regulatory/KYC link            \| Direct             \| Inherited/indirect         \|<br>\| Primary use                    \| Real account       \| Segmentation & routing     \|<br> | enum: ["PHYSICAL", "VIRTUAL"]; example: "PHYSICAL" |
| `division_id` | integer (schema `DivisionID`) | no | Account's administrative division ID | format: "int64"; example: 2856813 |
| `centralizer` | boolean (schema `IsCentralizer`) | no | Is this a centralizer account? A centralizer account, within the account hierarchy, is the account responsible for invoice billing. Defaults to `false`. | default: false; example: false |

<!-- schema: #/components/schemas/MessagePayloadResponse -->
### Schema `MessagePayloadResponse`

Pointer: `#/components/schemas/MessagePayloadResponse`. Type: object (schema `MessagePayloadResponse`).

> Object response for detailing request payload errors for a user message

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `field` | string (schema `ValidationErrorField`) | no | Non-valid field |  |
| `message` | string (schema `ValidationErrorMessage`) | no | Validation error description |  |

<!-- schema: #/components/schemas/MessageParameterResponse -->
### Schema `MessageParameterResponse`

Pointer: `#/components/schemas/MessageParameterResponse`. Type: object (schema `MessageParameterResponse`).

> Object response for detailing query parameters errors for a user message

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `field` | string (schema `ValidationErrorField`) | no | Non-valid field |  |
| `message` | string (schema `ValidationErrorMessage`) | no | Validation error description |  |

<!-- schema: #/components/schemas/MessageExternalResponse -->
### Schema `MessageExternalResponse`

Pointer: `#/components/schemas/MessageExternalResponse`. Type: object (schema `MessageExternalResponse`).

> Object response for detailing external errors for a user message

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string (schema `ExternalServiceCode`) | no | Code returned from the external service |  |
| `message` | string | no | Message description from the external service |  |

<!-- schema: #/components/schemas/ApplicantRegistration -->
### Schema `ApplicantRegistration`

Pointer: `#/components/schemas/ApplicantRegistration`. Type: object (schema `ApplicantRegistration`).

> Applicant's document information

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `number` | string | no | Document number, such as a tax ID. | maxLength: 15; example: "1234567890" |

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

- `POST /acquisitions/v2/s2s/applications` (`post-acquisitions-v2-s2s-applications`) is marked `deprecated: true` in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Core_platform_-_Accounts.yaml` | tag `Accounts`: POST /acquisitions/v3/s2s/applications, GET /acquisitions/v2/s2s/applications/{applicationId}, PATCH /acquisitions/v2/s2s/applications/{applicationId}, GET /acquisitions/v2/programs/{programId}/channels, POST /accounts/v5/accounts/search, POST /accounts/v3/accounts/search, GET /accounts/v1/accounts/{accountId}, PATCH /accounts/v1/accounts/{accountId}, POST /acquisitions/v2/s2s/applications, GET /accounts/v4/accounts/{accountId}/hierarchy/ascendants | https://github.com/PismoDevEx/pismo-api-specs | `3c621106abf11d41…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-AUTH-pismo-platform-security-guide` — Security guide for Pismo platform
- `KU-BANK-banking-as-a-service` — Banking as a Service
- `KU-BANK-banking-overview` — Banking overview
- `KU-BANK-get-started-core-banking` — Get started with core banking
- `KU-CARD-card-issuing-basics` — Card issuing reference
- `KU-CARD-implementation-steps` — Card issuing implementation steps 1 to 7
- `KU-CARD-physical-card-embossing` — Physical card embossing
- `KU-CC-accounts` — Control Center accounts: overview, management, actions and configurations
- `KU-CORE-accounts-overview` — Accounts
- `KU-CORE-commercial-cards` — Commercial cards programs
- `KU-CORE-legal-blocks` — Legal blocks (outdated)
- `KU-CORE-program-limits` — Program limits
- `KU-CORE-working-with-limits-objects` — Account limits
- `KU-CRED-agreements` — Agreements: compulsory, statement, installment and payment agreements
- `KU-CRED-holidays-in-credit-card-accounts` — Holidays in credit card accounts
- `KU-ERR-codes-acq-to-esma` — Error codes: ACQ to ESMA (32 prefixes)
- `KU-ERR-codes-esmg-to-whis` — Error codes: ESMG to WHIS (30 prefixes)
- `KU-ERR-validation-code-definitions` — Validation code definitions
- `KU-EVT-accounts-data-events` — Core platform - Accounts
- `KU-EVT-catalogue-account` — Event catalogue: account
- `KU-EVT-catalogue-other-domains` — Event catalogue: other event domains (accounting, authorization, availables, average, bulletin, cash, delinquent, fraud, instantpay, intl, ledger, networktransactions, onboarding, orgs, payment, platform, programs, rules, savings, statement)
- `KU-GS-get-started-with-pismo-apis` — Get started with Pismo APIs
- `KU-GS-program-types` — Program types
- `KU-GS-setup-overview` — Core objects
- `KU-PAY-bacs` — BACS: clearing, Direct Debit mandates and indemnity claims
- `KU-PAY-faster-payment-system` — Faster Payments (UK)
