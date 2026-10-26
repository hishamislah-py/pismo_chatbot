---
ku_id: KU-API-banking-transaction-banking--accounts
title: 'API reference: Banking - Transaction banking — Accounts'
category: api_reference
ku_type: api_reference
lifecycle: current
sources:
- path: api-specs/Banking_-_Transaction_banking.yaml
  sha256: dec6c4900eb2db35c29c0f0380763da5ae0e1a18c4ad1e293216b2b6effdab56
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
- post-account
- post-accounts-accountId-close
- get-accounts
- patch-account
- patch-accounts-accountId-status-v2
- patch-accounts-accountId-entity
- patch-accounts-accountId-status-rollback-v2
- v1-get-account-status-reason
- post-accounts-accountId-force-close
related_kus:
- KU-AUTH-account-and-external-id-tokens
- KU-BANK-account-balance-definitions-for-transaction-banking
- KU-BANK-divisions-and-hierarchies
- KU-BANK-earmarks
- KU-BANK-get-started-demand-deposit-accounts
- KU-BANK-get-started-transaction-banking
- KU-BANK-managing-account-statuses
- KU-BANK-transaction-banking-accounts
- KU-ERR-codes-acq-to-esma
- KU-ERR-codes-esmg-to-whis
- KU-ERR-codes-wcac
- KU-ERR-codes-wdiv
- KU-EVT-catalogue-account
- KU-EVT-catalogue-corporate
- KU-EVT-catalogue-other-domains
- KU-EVT-corporate-banking-data-events
- KU-PAY-multi-leg-payments
specification_version: 0.9.0
---

# API reference: Banking - Transaction banking — Accounts

**KU ID:** `KU-API-banking-transaction-banking--accounts` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 9 operation(s) tagged `Accounts` in `api-specs/Banking_-_Transaction_banking.yaml` (“Banking - Transaction banking”, version `0.9.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Accounts endpoints

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `POST /corporate/v1/corporate-accounts` | `post-account` | Create transaction banking account | no |
| `POST /corporate/v1/corporate-accounts/{externalAccountId}/close` | `post-accounts-accountId-close` | Close transaction banking account | no |
| `GET /corporate/v1/corporate-accounts/{externalAccountId}` | `get-accounts` | Get transaction banking account information | no |
| `PATCH /corporate/v1/corporate-accounts/{externalAccountId}` | `patch-account` | Update transaction banking account | no |
| `PATCH /corporate/v2/corporate-accounts/{externalAccountId}/status` | `patch-accounts-accountId-status-v2` | Update transaction banking account status | no |
| `PATCH /corporate/v1/corporate-accounts/{externalAccountId}/entity` | `patch-accounts-accountId-entity` | Transfer transaction banking account ownership | no |
| `PATCH /corporate/v2/corporate-accounts/{externalAccountId}/status/rollback` | `patch-accounts-accountId-status-rollback-v2` | Roll back transaction banking account status | no |
| `GET /corporate/v1/corporate-account-status/reasons` | `v1-get-account-status-reason` | List transaction banking account status reasons | no |
| `POST /corporate/v1/corporate-accounts/{externalAccountId}/force-close` | `post-accounts-accountId-force-close` | Force close transaction banking account | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"}

## Operation contracts

<!-- op: spec=api-specs/Banking_-_Transaction_banking.yaml method=POST path=/corporate/v1/corporate-accounts operationId=post-account -->
### `POST /corporate/v1/corporate-accounts` — Create transaction banking account

- **operationId:** `post-account`
- **Specification:** `api-specs/Banking_-_Transaction_banking.yaml` (Banking - Transaction banking)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Accounts`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Creates a transaction banking account. For details, refer to [Transaction banking accounts](doc:corporate-accounts).
>
> This endpoint generates the following events:
>  - [Corporate account created](https://developers.pismo.io/events/docs/corporate-corporate-account-creation-1).
>  - [Account application created](https://developers.pismo.io/events/docs/onboarding-succeeded-1)
>
>  For more information about events and setting up event notifications, refer to the [Data and reporting overview](doc:data-reporting-overview) guide.

#### Request body

Required: yes

> Create account request body

**Content type `application/json`** — schema: object (schema `CreateAccountRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `division_code` | string (schema `DivisionCode`) | yes | Code used to identify your division within the organization. Division code should only contain letters, numbers, and hyphens.<br><br>This is a client-provided ID and can be changed.<br> | maxLength: 36; example: "US" |
| `program_id` | integer (schema `ProgramID`) | yes | Program ID. The program must belong to the organization. Use [List programs](https://developers.pismo.io/pismo-docs/reference/programs-1) to view a list of the program IDs for the organization.<br><br>This program must be bound to the division. You can attach the program with either of the following endpoints:<br>[Create division](ref:post-division-v2)<br>[Patch division](ref:patch-division-v2)<br> | format: "int64"; maximum: 18446744073709552000; example: 8674 |
| `applicant` | object | yes |  |  |
| `applicant.document_number` | string (schema `DocumentNumber`) | yes | Applicant's government document number. Once set, this value is immutable, which means that `document_number` can't be updated. This field only accepts alphanumeric characters.<br><br><b>Note</b>: `document_number` does not allow special characters.<br> | maxLength: 15; example: "812045147" |
| `applicant.name` | string (schema `ApplicantName`) | yes | Applicant name | maxLength: 60; example: "Chester Fields" |
| `applicant.external_id` | string (schema `ExternalID`) | no | Custom entity ID that uniquely identifies the entity within your organization. By default, `document_number` is used as the primary identifier. To set `external_id` as the primary identifier, contact a Pismo representative to enable the parameter `EXTERNAL ID AS MAIN KEY`. | maxLength: 60; example: "83bcde27-e049-4244-9dab-cfb4c88d70f8" |
| `applicant.custom_fields` | object (schema `CustomFields`) | no | Name-value fields for any account-related data your organization needs to store at Pismo. This field can have its values validated against the JSON schema stored at the division (referenced by the `division_code`) field `schema`. |  |
| `external_account_id` | string (schema `ExternalAccountID`) | yes | Custom account ID. Used as the key for all operations (manage accounts, transactions, etc.) on the corporate layer.<br><br>This field is:<br>- Unique within the Organization<br>- Immutable: The field cannot be updated.<br>- Not recyclable: You can't reuse an external account ID, even if the account that was using it has been canceled.<br> | pattern: "^[a-zA-Z0-9-]+$"; maxLength: 60; example: "b993ba96-b3e8-4ef7-9cf7-7eee5ddafdab" |
| `parent_account_id` | integer (schema `ParentAccountID`) | no | Parent account ID. If provided, the account is the child of the account referenced by `parent_account_id`. The account referenced by `parent_account_id` can be in another program or division. | format: "int64"; maximum: 18446744073709552000; example: 232 |
| `account_creation_datetime` | string (schema `AccountCreateDatetime`) | no | The datetime the account was created (in UTC). The datetime format follows the ISO 8601 standard: `yyyy-mm-ddThh:mm:ss.sssZ`.<br><br>`minLength: 24`<br>`maxLength: 24`<br> | format: "date-time"; minLength: 24; maxLength: 24; example: "2025-02-01T22:07:58.000Z" |
| `overdraft` | object (schema `Overdraft`) | no |  |  |
| `currency_code` | string (schema `CurrencyCode`) | no | Alphabetic or numeric code (ISO 4217) for the currency used by the program. (Use the same currency as the program, but this is only a temporary situation). | maxLength: 3; example: "986" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | Account created | `application/json`: object (schema `CreateAccountResponse`) |
| 400 | A Bad Request validation error.<br><br>Static Validations (mandatory field, max value, max length, etc) have the code `WCAC0005`.<br> | `application/json`: object (schema `ErrorResponse`) |
| 401 | Access token is missing or invalid |  |
| 403 | The request has been lost |  |
| 404 | Not Found | `application/json`: object (schema `ErrorResponse`) |
| 409 | Conflict.<br> | `application/json`: object (schema `ErrorResponse`) |
| 500 | Internal Server Error | `application/json`: object (schema `ErrorResponse`) |

##### Response 201

**201 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `account_id` | integer (schema `AccountID`) | yes | Account ID | format: "int64"; example: 1234 |
| `program_id` | integer (schema `ProgramID3`) | yes | Program ID. This is a client-provided ID. | format: "int64"; example: 2222 |
| `external_account_id` | string (schema `ExternalAccountID`) | no | Custom account ID. Used as the key for all operations (manage accounts, transactions, etc.) on the corporate layer.<br><br>This field is:<br>- Unique within the Organization<br>- Immutable: The field cannot be updated.<br>- Not recyclable: You can't reuse an external account ID, even if the account that was using it has been canceled.<br> | pattern: "^[a-zA-Z0-9-]+$"; maxLength: 60; example: "b993ba96-b3e8-4ef7-9cf7-7eee5ddafdab" |
| `division_code` | string (schema `DivisionCode`) | no | Code used to identify your division within the organization. Division code should only contain letters, numbers, and hyphens.<br><br>This is a client-provided ID and can be changed.<br> | maxLength: 36; example: "US" |

201 Example `Account created`:

```json
{
  "account_id": 178800,
  "external_account_id": "b993ba96-b3e8-4ef7-9cf7-7eee5ddafdab",
  "program_id": 8086,
  "division_code": "my-division"
}
```

##### Response 400

400 Example `Invalid JSON payload`:

```json
{
  "code": "WCAC0013",
  "message": "Invalid JSON payload received: Error unmarshalling request"
}
```

400 Example `division_code required`:

```json
{
  "code": "WCAC0005",
  "message": "division_code is a required field"
}
```

400 Example `division_code max length`:

```json
{
  "code": "WCAC0005",
  "message": "division_code must be a maximum of 36 characters in length"
}
```

400 Example `program_id required`:

```json
{
  "code": "WCAC0005",
  "message": "program_id is a required field"
}
```

400 Example `Program Id not bound to Division`:

```json
{
  "code": "WCAC0006",
  "message": "Program not bound to Division"
}
```

400 Example `applicant.document_number required`:

```json
{
  "code": "WCAC0005",
  "message": "document_number is a required field"
}
```

400 Example `applicant.document_number max length`:

```json
{
  "code": "WCAC0005",
  "message": "document_number must be a maximum of 15 characters in length"
}
```

400 Example `applicant.document_number alphanumeric only`:

```json
{
  "code": "WCAC0005",
  "message": "document_number can only contain alphanumeric characters"
}
```

400 Example `applicant.name required`:

```json
{
  "code": "WCAC0005",
  "message": "name is a required field"
}
```

400 Example `applicant.name max length`:

```json
{
  "code": "WCAC0005",
  "message": "name must be a maximum of 60 characters in length"
}
```

400 Example `applicant.external_id max length`:

```json
{
  "code": "WCAC0005",
  "message": "external_id must be a maximum of 60 characters in length"
}
```

400 Example `external_account_id required`:

```json
{
  "code": "WCAC0005",
  "message": "external_account_id is a required field"
}
```

400 Example `external_account_id max length`:

```json
{
  "code": "WCAC0005",
  "message": "external_account_id must be a maximum of 60 characters in length"
}
```

400 Example `overdraft.limit max value`:

```json
{
  "code": "WCAC0005",
  "message": "limit must be 100,000,000,000,000,000.00 or less"
}
```

400 Example `external_account_id contains character not permitted`:

```json
{
  "code": "WCAC0005",
  "message": "external_account_id contains character not permitted: [characters]"
}
```

400 Example `custom_fields don't match with the Division JSON schema`:

```json
{
  "code": "WCAC0004",
  "message": "schema validation error: [validation description]"
}
```

400 Example `parent_account_id invalid`:

```json
{
  "code": "WCAC0016",
  "message": "parent_account_id informed as Parent Account not exists"
}
```

400 Example `currency_numeric_code invalid`:

```json
{
  "code": "WCAC0016",
  "message": "currency_numeric_code: Invalid Currency Numeric Code"
}
```

400 Example `currency_code invalid`:

```json
{
  "code": "WCAC0005",
  "message": "currency_code: invalid currency code"
}
```

400 Example `Not mapped 400 error`:

```json
{
  "code": "WCAC0009",
  "message": "generic message"
}
```

400 Example `Invalid account creation date time format`:

```json
{
  "code": "WCAC0005",
  "message": "account_creation_datetime should be formatted as yyyy-mm-ddThh:mm:ss.sssZ and be a valid datetime"
}
```

400 Example `account creation datetime in the future`:

```json
{
  "code": "WCAC0005",
  "message": "account_creation_datetime cannot be a future date"
}
```

##### Response 404

404 Example `Division not found`:

```json
{
  "code": "WDIV0002",
  "message": "Division not found"
}
```

##### Response 409

409 Example `external_account_id duplicated`:

```json
{
  "code": "WCAC0011",
  "message": "Duplicated external_account_id"
}
```

409 Example `Account duplicated`:

```json
{
  "code": "WCAC0014",
  "message": "Duplicate corporate account"
}
```

##### Response 500

500 Example `Generic internal error`:

```json
{
  "code": "ECMN9999",
  "message": "Internal error"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `WCAC0013` | Invalid JSON payload received: Error unmarshalling request |
| 400 | `WCAC0005` | division_code is a required field |
| 400 | `WCAC0006` | Program not bound to Division |
| 400 | `WCAC0004` | schema validation error: [validation description] |
| 400 | `WCAC0016` | parent_account_id informed as Parent Account not exists |
| 400 | `WCAC0009` | generic message |
| 404 | `WDIV0002` | Division not found |
| 409 | `WCAC0011` | Duplicated external_account_id |
| 409 | `WCAC0014` | Duplicate corporate account |
| 500 | `ECMN9999` | Internal error |

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `corporate-corporate-account-creation-1` | https://developers.pismo.io/events/docs/corporate-corporate-account-creation-1 |
| `onboarding-succeeded-1` | https://developers.pismo.io/events/docs/onboarding-succeeded-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `201;400;401;403;404;409;500`, has examples `True`, emits events `2`, deprecated `False`.

Guides that link to this operation: `KU-AUTH-account-and-external-id-tokens`, `KU-BANK-divisions-and-hierarchies`, `KU-BANK-earmarks`, `KU-BANK-get-started-demand-deposit-accounts`, `KU-BANK-get-started-transaction-banking`, `KU-BANK-transaction-banking-accounts`, `KU-EVT-corporate-banking-data-events`.

<!-- op: spec=api-specs/Banking_-_Transaction_banking.yaml method=POST path=/corporate/v1/corporate-accounts/{externalAccountId}/close operationId=post-accounts-accountId-close -->
### `POST /corporate/v1/corporate-accounts/{externalAccountId}/close` — Close transaction banking account

- **operationId:** `post-accounts-accountId-close`
- **Specification:** `api-specs/Banking_-_Transaction_banking.yaml` (Banking - Transaction banking)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Accounts`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Close a transaction banking account and all of its children.
>
> Book balance and earmark balance must be zero.
>
> This endpoint generates an [Account status changed](https://developers.pismo.io/events/docs/account-status-change-2) event.
>
> **NOTE**: This endpoint requires an account token - an access token encoded with an external account ID. Tokens can expire quickly, which can result in a `401 Unauthorized` message.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `externalAccountId` | path | yes | string | External account ID | minLength: 1; maxLength: 60; example: "12345678901" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 204 | No Content |  |
| 400 | A Bad Request validation error. | `application/json`: object (schema `ErrorResponse`) |
| 401 | Access token is missing or invalid |  |
| 403 | The request has been lost |  |
| 422 | Unprocessable Entity. The account has not completed the onboarding process. | `application/json`: object (schema `ErrorResponse`) |
| 500 | Internal Server Error | `application/json`: object (schema `ErrorResponse`) |

##### Response 400

400 Example `Account not found`:

```json
{
  "code": "WCAC0012",
  "message": "Account not found"
}
```

400 Example `Scheduled transactions`:

```json
{
  "code": "WCAC0018",
  "message": "Account still has active scheduled payments"
}
```

400 Example `Remaining balance`:

```json
{
  "code": "WCAC0019",
  "message": "Make sure that the account has a zero balance before closing it"
}
```

400 Example `Earmark balance`:

```json
{
  "code": "WCAC0028",
  "message": "Account has active earmark"
}
```

400 Example `Account closed error`:

```json
{
  "code": "WCAC0029",
  "message": "Action not permitted on a closed account"
}
```

400 Example `Account is in final status`:

```json
{
  "code": "WCAC0035",
  "message": "Account is currently in the final status"
}
```

400 Example `Account balances pending creation`:

```json
{
  "code": "WCAC0040",
  "message": "Account balance is still being created. Please try again in a few minutes"
}
```

##### Response 422

422 Example `Account onboarding not completed`:

```json
{
  "code": "WCAC0045",
  "message": "Account onboarding has not been completed yet. The account cannot be closed."
}
```

##### Response 500

500 Example `Generic internal error`:

```json
{
  "code": "ECMN9999",
  "message": "Internal error"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `WCAC0012` | Account not found |
| 400 | `WCAC0018` | Account still has active scheduled payments |
| 400 | `WCAC0019` | Make sure that the account has a zero balance before closing it |
| 400 | `WCAC0028` | Account has active earmark |
| 400 | `WCAC0029` | Action not permitted on a closed account |
| 400 | `WCAC0035` | Account is currently in the final status |
| 400 | `WCAC0040` | Account balance is still being created. Please try again in a few minutes |
| 422 | `WCAC0045` | Account onboarding has not been completed yet. The account cannot be closed. |
| 500 | `ECMN9999` | Internal error |

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `account-status-change-2` | https://developers.pismo.io/events/docs/account-status-change-2 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `204;400;401;403;422;500`, has examples `True`, emits events `1`, deprecated `False`.

Guides that link to this operation: `KU-AUTH-account-and-external-id-tokens`, `KU-BANK-managing-account-statuses`, `KU-EVT-corporate-banking-data-events`.

<!-- op: spec=api-specs/Banking_-_Transaction_banking.yaml method=GET path=/corporate/v1/corporate-accounts/{externalAccountId} operationId=get-accounts -->
### `GET /corporate/v1/corporate-accounts/{externalAccountId}` — Get transaction banking account information

- **operationId:** `get-accounts`
- **Specification:** `api-specs/Banking_-_Transaction_banking.yaml` (Banking - Transaction banking)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Accounts`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Get the information for a transaction banking account.
>
> **NOTE**: This endpoint requires an account token - an access token encoded with an external account ID. Tokens can expire quickly, which can result in a `401 Unauthorized` message.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `externalAccountId` | path | yes | string | External account ID | minLength: 1; maxLength: 60; example: "12345678901" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `GetAccountResponse`) |
| 400 | A Bad Request validation error.<br> | `application/json`: object (schema `ErrorResponse`) |
| 401 | Access token is missing or invalid |  |
| 403 | The request has been lost |  |
| 404 | Not found | `application/json`: object (schema `ErrorResponse`) |
| 500 | Internal Server Error | `application/json`: object (schema `ErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `account_id` | integer (schema `AccountID2`) | yes | Account ID<br><br>`minimum: 1`<br> | format: "int64"; minimum: 1; example: 102778 |
| `account_creation_datetime` | string (schema `AccountCreationDatetime`) | yes | Datetime the account was created in the Pismo system (in UTC). The datetime format follows the ISO 8601 standard: `yyyy-mm-ddThh:mm:ss.sssZ`.<br><br>Note that milliseconds are represented as `000`, for example: `2024-02-22T16:51:49.000Z`.<br><br>This field accepts datetime values from the present or past. Future dates are not allowed.<br><br>`minLength: 24`<br>`maxLength: 24`<br> | format: "date-time"; minLength: 24; maxLength: 24; example: "2024-01-04T10:25:30.123Z" |
| `division_code` | string (schema `DivisionCode`) | yes | Code used to identify your division within the organization. Division code should only contain letters, numbers, and hyphens.<br><br>This is a client-provided ID and can be changed.<br> | maxLength: 36; example: "US" |
| `division_id` | string (schema `DivisionID`) | yes | The Pismo platform generates the division ID when you use the [Create division](ref:post-division-v2) endpoint.<br><br>This ID is immutable and cannot be changed.<br> | format: "uuid"; example: "6f8a456a-8b1a-4022-a2f8-7612595330b5" |
| `program_id` | integer (schema `ProgramID2`) | yes | Program ID<br><br>`minimum: 1`<br> | format: "int64"; minimum: 1; example: 492 |
| `future_dated_credits_balance` | number (schema `FutureDatedCreditsBalance`) | yes | Represents the account balance scheduled to be settled on a future date, after the original posting date. The account's `book_balance` is credited when the settlement occurs.<br><br>The `future_dated_credits_balance` increases when future-dated credits are posted using the [Post payment](ref:corporate-v2-post-payments) endpoint, and decreases when those payments are settled or canceled. This balance is always a positive value.<br><br>`minimum`: `-9223372036854775807`<br>`maximum`: `9223372036854775807`<br> | minimum: -9223372036854776000; maximum: 9223372036854776000; example: 70 |
| `future_dated_debits_balance` | number (schema `FutureDatedDebitsBalance`) | yes | Represents the account balance scheduled to be settled on a future date, after the initial posting date. The account’s `book_balance` is debited when the settlement occurs.<br><br>The `future_dated_debits_balance` increases when future-dated debits are posted using the [Post payment](ref:corporate-v2-post-payments) endpoint, and decreases when these payments are settled or canceled. This balance is always a positive value.<br><br>`minimum`: `-9223372036854775807`<br>`maximum`: `9223372036854775807`<br> | minimum: -9223372036854776000; maximum: 9223372036854776000; example: 70 |
| `parent_account_id` | integer (schema `ParentAccountID2`) | no | Parent account ID. The account retrieved is the child of the account referenced by `parent_account_id`. The account referenced by `parent_account_id` can be in another program or division.<br><br>`minimum: 1`<br> | format: "int64"; minimum: 1; example: 123 |
| `available_balance` | number (schema `AvailableBalance`) | no | Available balance.<br><br>Available balance is calculated as `credit_balance` - `debit_balance` + `overdraft_limit`.<br>`minimum: -9223372036854775807`<br>`maximum: 9223372036854775807`<br> | format: "float"; minimum: -9223372036854776000; maximum: 9223372036854776000; example: 123.45 |
| `earmarked_balance` | number (schema `EarmarkBalance`) | no | Earmark balance. Initially equal to the earmarked amount and decreases as the reserved funds are used up or decreased in a decrease operation. It can also increase if an increase operation is performed.<br><br>`minimum: 0`<br>`maximum: 18446744073709551617`<br> | minimum: 0; maximum: 18446744073709552000; example: 123.45 |
| `overdraft_limit` | number (schema `OverdraftLimit`) | no | Account overdraft limit<br><br>`minimum: 0`<br>`maximum: 18446744073709551617`<br> | format: "float"; minimum: 0; maximum: 18446744073709552000; example: 123.45 |
| `ledger_balance` | number (schema `LedgerBalance`) | no | Ledger balance.<br><br>Ledger balance is calculated as `book_balance` + `uncleared_funds`.<br>`minimum: -9223372036854775807`<br>`maximum: 9223372036854775807`<br> | format: "float"; minimum: -9223372036854776000; maximum: 9223372036854776000; example: 270.35 |
| `book_balance` | number (schema `BookBalance`) | no | Book balance.<br><br>Book balance is calculated as `credit_balance` - `debit_balance` + `earmarked_balance`.<br>`minimum: -9223372036854775807`<br>`maximum: 9223372036854775807`<br> | format: "float"; minimum: -9223372036854776000; maximum: 9223372036854776000; example: 146.9 |
| `value_dated_balance` | number (schema `ValueDatedBalance`) | no | The value dated balance results from recalculating credit or debit balance based on the back value date. Defaults to the book balance.<br><br>The value dated balance is included in the following events:<br>- [Account balance changed](https://developers.pismo.io/events/docs/account-balances-balance-change-1)<br>- [Account balance history generated](https://developers.pismo.io/events/docs/account-balances-balance-history-1)<br> | format: "float"; example: 123.45 |
| `uncleared_funds` | number (schema `UnclearedFunds`) | no | Uncleared funds amount<br><br>`minimum: -9223372036854775807`<br>`maximum: 9223372036854775807`<br> | format: "float"; minimum: -9223372036854776000; maximum: 9223372036854776000; example: 123.45 |
| `uncleared_checks_balance` | number (schema `UnclearedChecksBalance`) | no | The total value of checks that have been posted to the account but have not yet cleared.<br>`minimum: -9223372036854775807`<br>`maximum: 9223372036854775807`<br> | format: "float"; minimum: -9223372036854776000; maximum: 9223372036854776000 |
| `restricted_funds` | number (schema `RestrictedFundsBalance`) | no | The portion of an account balance held under regulatory or operational restrictions and not available for transactions.<br>`minimum`: 0<br>`maximum`: 9223372036854775807<br> | format: "float"; minimum: 0; maximum: 9223372036854776000 |
| `legal_holds` | number (schema `LegalHoldsBalance`) | no | The portion of an account balance held under legal holds (such as court-ordered restrictions) and unavailable for transactions.<br>`minimum`: 0<br>`maximum`: 9223372036854775807<br> | format: "float"; minimum: 0; maximum: 9223372036854776000 |
| `held_funds` | number (schema `HeldFunds`) | no | Funds that are temporarily restricted due to regulatory or operational requirements, unavailable for transactions, and representing the total amount of earmarked or otherwise restricted balances.<br>`minimum`: 0<br>`maximum`: 9223372036854775807<br> | format: "float"; minimum: 0; maximum: 9223372036854776000 |
| `held_checks_balance` | number (schema `HeldChecksBalance`) | no | The balance from checks that the bank considers available but holds to earn interest. It increases when check holds are applied and decreases when those holds are released or canceled.<br>`minimum`: 0<br>`maximum`: 9223372036854775807<br> | format: "float"; minimum: 0; maximum: 9223372036854776000 |
| `remunerative_interest_accrued` | number (schema `RemunerativeInterestAccrued`) | no | This balance reflects the total interest pending capitalization. It increases as interest accrues and decreases when the accrued interest is added to the principal balance.<br>`minimum`: 0<br>`maximum`: 9223372036854775807<br> | format: "float"; minimum: 0; maximum: 9223372036854776000 |
| `children` | array of integer (schema `Children`) | no | List of child account IDs | items.format: "int32" |
| `status` | string (schema `AccountStatus`) | no | Account status<br><br>`minLength: 1`<br>`maxLength: 9`<br> | minLength: 1; maxLength: 9; example: "DORMANT" |
| `external_account_id` | string (schema `ExternalAccountID`) | no | Custom account ID. Used as the key for all operations (manage accounts, transactions, etc.) on the corporate layer.<br><br>This field is:<br>- Unique within the Organization<br>- Immutable: The field cannot be updated.<br>- Not recyclable: You can't reuse an external account ID, even if the account that was using it has been canceled.<br> | pattern: "^[a-zA-Z0-9-]+$"; maxLength: 60; example: "b993ba96-b3e8-4ef7-9cf7-7eee5ddafdab" |
| `currency_numeric_code` | string (schema `CurrencyNumericCode`) | no | Numeric code (ISO 4217) for the currency used by the program.<br><br>`minLength: 3`<br>`maxLength: 3`<br> | minLength: 3; maxLength: 3; example: "840" |
| `currency_alphabetic_code` | string (schema `CurrencyAlphabeticCode`) | no | Alphabetic code (ISO 4217) for the currency used by the program.<br><br>`minLength: 3`<br>`maxLength: 3`<br> | minLength: 3; maxLength: 3; example: "USD" |
| `document_number` | string (schema `DocumentNumber2`) | no | Entity's government document number.<br><br>`minLength: 1`<br>`maxLength: 15`<br> | minLength: 1; maxLength: 15; example: "1122334455" |
| `status_reason_id` | integer (schema `AccountStatusReasonID`) | no | Account status reason ID<br><br>`minimum: 1`<br> | format: "int64"; minimum: 1; example: 1438 |
| `status_reason_description` | string (schema `AccountStatusReasonDescription`) | no | Account status reason description<br><br>`minLength: 1`<br>`maxLength: 500`<br> | minLength: 1; maxLength: 500; example: "CREDIT_ONLY" |
| `reason_external_id` | string (schema `AccountStatusReasonExternalID`) | no | External reason ID specifying account restrictions<br><br>`minimum: 1`<br>`maximum: 120`<br> | minLength: 1; maxLength: 120; example: "CREDIT_ONLY" |

200 Example `Account info`:

```json
{
  "account_id": 184034550,
  "division_code": "division-7",
  "division_id": "6f8a456a-8b1a-4022-a2f8-7612595330b5",
  "program_id": 10768,
  "children": [
    10983
  ],
  "future_dated_credits_balance": 0,
  "future_dated_debits_balance": 0,
  "status": "DORMANT",
  "external_account_id": "a4070788-bbe3-4127-8",
  "currency_numeric_code": "840",
  "currency_alphabetic_code": "USD",
  "document_number": "1879063",
  "status_reason_id": 1421,
  "reason_external_id": "DEBIT_ONLy",
  "status_reason_description": "Debit Only",
  "account_creation_datetime": "2024-07-11T14:58:33.000Z",
  "available_balance": 0,
  "earmarked_balance": 0,
  "overdraft_limit": 0,
  "ledger_balance": 0,
  "book_balance": 0,
  "value_dated_balance": 0,
  "uncleared_funds": 0,
  "uncleared_checks_balance": 0,
  "restricted_funds": 0,
  "legal_holds": 0,
  "remunerative_interest_accrued": 1.23
}
```

##### Response 400

400 Example `Account not found:`:

```json
{
  "code": "WCAC0012",
  "message": "Corporate account not found"
}
```

##### Response 404

404 Example `Account division not found`:

```json
{
  "code": "WDIV0002",
  "message": "Account division not found"
}
```

404 Example `Account balance not found`:

```json
{
  "code": "WCAC0023",
  "message": "Account balance not found"
}
```

##### Response 500

500 Example `Generic internal error`:

```json
{
  "code": "ECMN9999",
  "message": "Internal error"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `WCAC0012` | Corporate account not found |
| 404 | `WDIV0002` | Account division not found |
| 404 | `WCAC0023` | Account balance not found |
| 500 | `ECMN9999` | Internal error |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;403;404;500`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-BANK-account-balance-definitions-for-transaction-banking`, `KU-BANK-get-started-demand-deposit-accounts`, `KU-PAY-multi-leg-payments`.

<!-- op: spec=api-specs/Banking_-_Transaction_banking.yaml method=PATCH path=/corporate/v1/corporate-accounts/{externalAccountId} operationId=patch-account -->
### `PATCH /corporate/v1/corporate-accounts/{externalAccountId}` — Update transaction banking account

- **operationId:** `patch-account`
- **Specification:** `api-specs/Banking_-_Transaction_banking.yaml` (Banking - Transaction banking)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Accounts`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Update a transaction banking account.
>
> **NOTE**: This endpoint requires an account token - an access token encoded with an external account ID. Tokens can expire quickly, which can result in a `401 Unauthorized` message.
>
> This endpoint generates the following events:
> - [Corporate account updated](https://developers.pismo.io/events/docs/corporate-corporate-account-change-1)
> - [Account status changed](https://developers.pismo.io/events/docs/account-status-change-2)

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `externalAccountId` | path | yes | string | External account ID | minLength: 1; maxLength: 60; example: "12345678901" |

#### Request body

Required: yes

> Update account request body

**Content type `application/json`** — schema: object (schema `PatchAccountRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `division_code` | string (schema `DivisionCode`) | no | Code used to identify your division within the organization. Division code should only contain letters, numbers, and hyphens.<br><br>This is a client-provided ID and can be changed.<br> | maxLength: 36; example: "US" |
| `program_id` | integer (schema `ProgramID`) | no | Program ID. The program must belong to the organization. Use [List programs](https://developers.pismo.io/pismo-docs/reference/programs-1) to view a list of the program IDs for the organization.<br><br>This program must be bound to the division. You can attach the program with either of the following endpoints:<br>[Create division](ref:post-division-v2)<br>[Patch division](ref:patch-division-v2)<br> | format: "int64"; maximum: 18446744073709552000; example: 8674 |
| `applicant` | object | no |  |  |
| `applicant.custom_fields` | object (schema `CustomFields`) | no | Name-value fields for any account-related data your organization needs to store at Pismo. This field can have its values validated against the JSON schema stored at the division (referenced by the `division_code`) field `schema`. |  |

Example `Update account`:

```json
{
  "division_code": "my-division",
  "program_id": 8674,
  "applicant": {
    "custom_fields": {
      "product_id": 1
    }
  }
}
```

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 204 | No Content |  |
| 400 | A Bad Request validation error.<br><br>Static Validations (mandatory field, max value, max length, etc.) have the code `WCAC0005`.<br> | `application/json`: object (schema `ErrorResponse`) |
| 401 | Access token is missing or invalid |  |
| 403 | The request has been lost |  |
| 404 | Not Found | `application/json`: object (schema `ErrorResponse`) |
| 500 | Internal Server Error | `application/json`: object (schema `ErrorResponse`) |

##### Response 400

400 Example `Invalid JSON payload`:

```json
{
  "code": "WCAC0013",
  "message": "Invalid JSON payload received: Error unmarshalling request"
}
```

400 Example `Account not found:`:

```json
{
  "code": "WCAC0012",
  "message": "Corporate account not found"
}
```

400 Example `Program ID not bound to division`:

```json
{
  "code": "WCAC0006",
  "message": "Program not bound to Division"
}
```

400 Example `custom_fields don't match with the Division JSON schema`:

```json
{
  "code": "WCAC0004",
  "message": "schema validation error: [validation description]"
}
```

400 Example `division_code max length`:

```json
{
  "code": "WCAC0005",
  "message": "division_code must be a maximum of 36 characters in length"
}
```

400 Example `Programs with different currencies`:

```json
{
  "code": "WCAC0031",
  "message": "This program migration is not permitted. The programs currency must be the same type"
}
```

400 Example `Programs with different types`:

```json
{
  "code": "WCAC0032",
  "message": "This program migration is not permitted. The programs must be the same type"
}
```

400 Example `No attributes to update`:

```json
{
  "code": "WCAC0033",
  "message": "There are no attributes to update."
}
```

##### Response 404

404 Example `Division not found`:

```json
{
  "code": "WDIV0002",
  "message": "Division not found"
}
```

##### Response 500

500 Example `Generic internal error`:

```json
{
  "code": "ECMN9999",
  "message": "Internal error"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `WCAC0013` | Invalid JSON payload received: Error unmarshalling request |
| 400 | `WCAC0012` | Corporate account not found |
| 400 | `WCAC0006` | Program not bound to Division |
| 400 | `WCAC0004` | schema validation error: [validation description] |
| 400 | `WCAC0005` | division_code must be a maximum of 36 characters in length |
| 400 | `WCAC0031` | This program migration is not permitted. The programs currency must be the same type |
| 400 | `WCAC0032` | This program migration is not permitted. The programs must be the same type |
| 400 | `WCAC0033` | There are no attributes to update. |
| 404 | `WDIV0002` | Division not found |
| 500 | `ECMN9999` | Internal error |

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `account-status-change-2` | https://developers.pismo.io/events/docs/account-status-change-2 |
| `corporate-corporate-account-change-1` | https://developers.pismo.io/events/docs/corporate-corporate-account-change-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `204;400;401;403;404;500`, has examples `True`, emits events `2`, deprecated `False`.

Guides that link to this operation: `KU-AUTH-account-and-external-id-tokens`, `KU-EVT-corporate-banking-data-events`.

<!-- op: spec=api-specs/Banking_-_Transaction_banking.yaml method=PATCH path=/corporate/v2/corporate-accounts/{externalAccountId}/status operationId=patch-accounts-accountId-status-v2 -->
### `PATCH /corporate/v2/corporate-accounts/{externalAccountId}/status` — Update transaction banking account status

- **operationId:** `patch-accounts-accountId-status-v2`
- **Specification:** `api-specs/Banking_-_Transaction_banking.yaml` (Banking - Transaction banking)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Accounts`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Update the status of a transaction banking account and the statuses of all the account's children.
>
> This endpoint generates the following event:
>  - [Account status changed](https://developers.pismo.io/events/docs/account-status-change-2).
>
> For more information on account status and reasons, see [Manage account statuses](doc:managing-account-statuses).
>
> Note: This endpoint requires an account token — an access token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a `401 Unauthorized` message.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `externalAccountId` | path | yes | string | External account ID | minLength: 1; maxLength: 60; example: "12345678901" |

#### Request body

Required: yes

> Status to update

**Content type `application/json`** — schema: object (schema `PatchAccountStatusv2`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `status` | string (schema `NewAccountStatus`) | no | New status for the account.<br><br><b>Note</b>: When updating the account status, make sure the status is not a final status or a status in the dormancy configuration.<br> | pattern: "^[A-Z_]+$"; minLength: 1; maxLength: 9; example: "DORMANT" |
| `reason_external_id` | string (schema `AccountStatusReasonExternalID`) | no | External reason ID specifying account restrictions<br><br>`minimum: 1`<br>`maximum: 120`<br> | minLength: 1; maxLength: 120; example: "CREDIT_ONLY" |
| `update_children` | boolean (schema `UpdateChildren`) | no | Whether to update status of all account children linked through the attribute `parent_account_id` (`true`) or not (`false`). | example: true |
| `metadata` | object (schema `Metadata2`) | no | Key-value pair field that you can use to send any information relating to a status change. The information you send is propagated in the [Account status changed](https://developers.pismo.io/events/docs/account-status-change-2) event.<br><br>Note that data entered in this field is not saved.<br><br><b>Note</b>: If you include `external_account_id` in this field, the Pismo platform ignores it and only uses the one you sent in the path parameter.<br><br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis).<br> |  |

Example `Account blocked`:

```json
{
  "status": "BLOCKED"
}
```

Example `Reverse account blocked`:

```json
{
  "status": "NORMAL"
}
```

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 204 | OK |  |
| 400 | A Bad Request validation error.<br><br>Static Validations (mandatory field, max value, max length, etc) have the code `WCAC0005`.<br> | `application/json`: object (schema `ErrorResponse`) |
| 404 | Not found | `application/json`: object (schema `ErrorResponse`) |
| 422 | Unprocessable Entity | `application/json`: object (schema `ErrorResponse`) |
| 500 | Internal Server Error | `application/json`: object (schema `ErrorResponse`) |

##### Response 400

400 Example `Corporate account not found`:

```json
{
  "code": "WCAC0012",
  "message": "Corporate account not found"
}
```

400 Example `Invalid JSON payload`:

```json
{
  "code": "WCAC0013",
  "message": "Invalid JSON payload received: Error unmarshalling request."
}
```

400 Example `Account status is already in dormancy config`:

```json
{
  "code": "WCAC0034",
  "message": "status is specified in account's dormancy config"
}
```

400 Example `Account is in final status`:

```json
{
  "code": "WCAC0035",
  "message": "Account is currently in the final status"
}
```

400 Example `Status cannot be final`:

```json
{
  "code": "WCAC0036",
  "message": "status cannot be final"
}
```

400 Example `reason_external_id max length`:

```json
{
  "code": "WCAC0005",
  "message": "reason_external_id must be a maximum of 120 characters in length"
}
```

400 Example `status or reason_external_id must be provided`:

```json
{
  "code": "WCAC0005",
  "message": "status or reason_external_id must be provided"
}
```

400 Example `Status not found`:

```json
{
  "code": "WCAC0020",
  "message": "Status not found"
}
```

##### Response 404

404 Example `status not found`:

```json
{
  "code": "WCAC0020",
  "message": "Status not found"
}
```

404 Example `reason not found`:

```json
{
  "code": "WCAC0021",
  "message": "Reason not found"
}
```

##### Response 422

422 Example `status not found`:

```json
{
  "code": "WCAC0038",
  "message": "Account status update blocked: operation blocked for account."
}
```

##### Response 500

500 Example `Generic internal error`:

```json
{
  "code": "ECMN9999",
  "message": "Internal error"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `WCAC0012` | Corporate account not found |
| 400 | `WCAC0013` | Invalid JSON payload received: Error unmarshalling request. |
| 400 | `WCAC0034` | status is specified in account's dormancy config |
| 400 | `WCAC0035` | Account is currently in the final status |
| 400 | `WCAC0036` | status cannot be final |
| 400 | `WCAC0005` | reason_external_id must be a maximum of 120 characters in length |
| 400 | `WCAC0020` | Status not found |
| 404 | `WCAC0020` | Status not found |
| 404 | `WCAC0021` | Reason not found |
| 422 | `WCAC0038` | Account status update blocked: operation blocked for account. |
| 500 | `ECMN9999` | Internal error |

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `account-status-change-2` | https://developers.pismo.io/events/docs/account-status-change-2 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `204;400;404;422;500`, has examples `True`, emits events `1`, deprecated `False`.

Guides that link to this operation: `KU-AUTH-account-and-external-id-tokens`.

<!-- op: spec=api-specs/Banking_-_Transaction_banking.yaml method=PATCH path=/corporate/v1/corporate-accounts/{externalAccountId}/entity operationId=patch-accounts-accountId-entity -->
### `PATCH /corporate/v1/corporate-accounts/{externalAccountId}/entity` — Transfer transaction banking account ownership

- **operationId:** `patch-accounts-accountId-entity`
- **Specification:** `api-specs/Banking_-_Transaction_banking.yaml` (Banking - Transaction banking)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Accounts`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Assign a new owner to a transaction banking account. If the new owner already exists within the organization, it's linked to the account. If not, a new entity is created and linked to the account. The previous account owner and all other customers linked to the account are deactivated.
>
> This endpoint generates an [Account owner changed](https://developers.pismo.io/events/docs/account-account-owner-change-1) event.
>
> **NOTE**: This endpoint requires an account token - an access token encoded with an external account ID. Tokens can expire quickly, which can result in a `401 Unauthorized` message.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `externalAccountId` | path | yes | string | External account ID | minLength: 1; maxLength: 60; example: "12345678901" |

#### Request body

Required: yes

> The entity name and document number

**Content type `application/json`** — schema: object (schema `PatchAccountEntity`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `document_number` | string (schema `DocumentNumber`) | yes | Applicant's government document number. Once set, this value is immutable, which means that `document_number` can't be updated. This field only accepts alphanumeric characters.<br><br><b>Note</b>: `document_number` does not allow special characters.<br> | maxLength: 15; example: "812045147" |
| `name` | string (schema `EntityName`) | yes | Entity name | maxLength: 60; example: "Chester Fields" |

Example `Update Account Entity`:

```json
{
  "name": "Chester Fields",
  "document_number": "812045147"
}
```

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 204 | OK |  |
| 400 | A Bad Request validation error.<br><br>Static Validations (mandatory field, max value, max length, etc) have the code `WCAC0005`.<br> | `application/json`: object (schema `ErrorResponse`) |
| 401 | Access token is missing or invalid |  |
| 403 | The request has been lost |  |
| 409 | Entity conflict.<br> | `application/json`: object (schema `ErrorResponse`) |
| 500 | Internal Server Error | `application/json`: object (schema `ErrorResponse`) |

##### Response 400

400 Example `Account not found`:

```json
{
  "code": "WCAC0012",
  "message": "Corporate account not found"
}
```

400 Example `Invalid JSON payload`:

```json
{
  "code": "WCAC0013",
  "message": "Invalid JSON payload received: Error unmarshalling request."
}
```

400 Example `document_number required`:

```json
{
  "code": "WCAC0005",
  "message": "document_number is a required field"
}
```

400 Example `document_number max length`:

```json
{
  "code": "WCAC0005",
  "message": "document_number must be a maximum of 15 characters in length"
}
```

400 Example `document_number contains characters not permitted`:

```json
{
  "code": "WCAC0005",
  "message": "document_number contains character not permitted: {characters}"
}
```

400 Example `name required`:

```json
{
  "code": "WCAC0005",
  "message": "name is a required field"
}
```

400 Example `name max length`:

```json
{
  "code": "WCAC0005",
  "message": "name must be a maximum of 60 characters in length"
}
```

400 Example `name contains characters not permitted`:

```json
{
  "code": "WCAC0005",
  "message": "name contains character not permitted: {characters}"
}
```

400 Example `Account closed error`:

```json
{
  "code": "WCAC0029",
  "message": "Action not permitted on a closed account"
}
```

##### Response 409

409 Example `Customer already owns account`:

```json
{
  "code": "WCAC0026",
  "message": "This document number is already associated with the owner of this account"
}
```

409 Example `Inactive customer`:

```json
{
  "code": "WCAC0027",
  "message": "This document number is associated with an inactive customer"
}
```

##### Response 500

500 Example `Generic internal error`:

```json
{
  "code": "ECMN9999",
  "message": "Internal error"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `WCAC0012` | Corporate account not found |
| 400 | `WCAC0013` | Invalid JSON payload received: Error unmarshalling request. |
| 400 | `WCAC0005` | document_number is a required field |
| 400 | `WCAC0029` | Action not permitted on a closed account |
| 409 | `WCAC0026` | This document number is already associated with the owner of this account |
| 409 | `WCAC0027` | This document number is associated with an inactive customer |
| 500 | `ECMN9999` | Internal error |

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `account-account-owner-change-1` | https://developers.pismo.io/events/docs/account-account-owner-change-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `204;400;401;403;409;500`, has examples `True`, emits events `1`, deprecated `False`.

Guides that link to this operation: `KU-AUTH-account-and-external-id-tokens`.

<!-- op: spec=api-specs/Banking_-_Transaction_banking.yaml method=PATCH path=/corporate/v2/corporate-accounts/{externalAccountId}/status/rollback operationId=patch-accounts-accountId-status-rollback-v2 -->
### `PATCH /corporate/v2/corporate-accounts/{externalAccountId}/status/rollback` — Roll back transaction banking account status

- **operationId:** `patch-accounts-accountId-status-rollback-v2`
- **Specification:** `api-specs/Banking_-_Transaction_banking.yaml` (Banking - Transaction banking)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Accounts`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Roll back an account from its final status.
> <b>Note</b>: You can only change the account status from its final status to one that is both not final and not in a dormant state.
>
> This endpoint generates an [Account status changed](https://developers.pismo.io/events/docs/account-status-change-2) event.
>
> For more information on account statuses, refer to [Manage account statuses](doc:managing-account-statuses).
>
> **NOTE**: This endpoint requires an account token - an access token encoded with an external account ID. Tokens can expire quickly, which can result in a `401 Unauthorized` message.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `externalAccountId` | path | yes | string | External account ID | minLength: 1; maxLength: 60; example: "12345678901" |

#### Request body

Required: yes

> Status to update

**Content type `application/json`** — schema: object (schema `PatchAccountStatusRollbackv2`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `status` | string (schema `NewAccountStatus`) | no | New status for the account.<br><br><b>Note</b>: When updating the account status, make sure the status is not a final status or a status in the dormancy configuration.<br> | pattern: "^[A-Z_]+$"; minLength: 1; maxLength: 9; example: "DORMANT" |
| `reason_external_id` | string (schema `AccountStatusReasonExternalID`) | no | External reason ID specifying account restrictions<br><br>`minimum: 1`<br>`maximum: 120`<br> | minLength: 1; maxLength: 120; example: "CREDIT_ONLY" |
| `description` | string (schema `AccountStatusReasonDescription`) | no | Account status reason description<br><br>`minLength: 1`<br>`maxLength: 500`<br> | minLength: 1; maxLength: 500; example: "CREDIT_ONLY" |

Example `Reverse account cancelled`:

```json
{
  "status": "NORMAL"
}
```

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 204 | OK |  |
| 400 | A Bad Request validation error.<br><br>Static Validations (mandatory field, max value, max length, etc) have the code `WCAC0005`.<br> | `application/json`: object (schema `ErrorResponse`) |
| 404 | Not found | `application/json`: object (schema `ErrorResponse`) |
| 422 | Unprocessable Entity | `application/json`: object (schema `ErrorResponse`) |
| 500 | Internal Server Error | `application/json`: object (schema `ErrorResponse`) |

##### Response 400

400 Example `Corporate account not found`:

```json
{
  "code": "WCAC0012",
  "message": "Corporate account not found"
}
```

400 Example `Invalid JSON payload`:

```json
{
  "code": "WCAC0013",
  "message": "Invalid JSON payload received: Error unmarshalling request."
}
```

400 Example `status required`:

```json
{
  "code": "WCAC0005",
  "message": "status is a required field"
}
```

400 Example `Account status is already in dormancy config`:

```json
{
  "code": "WCAC0034",
  "message": "status is specified in account's dormancy config"
}
```

400 Example `Account is not in final status`:

```json
{
  "code": "WCAC0037",
  "message": "account is not currently in the final status"
}
```

400 Example `Status cannot be final`:

```json
{
  "code": "WCAC0036",
  "message": "status cannot be final"
}
```

400 Example `reason_external_id max length`:

```json
{
  "code": "WCAC0005",
  "message": "reason_external_id must be a maximum of 120 characters in length"
}
```

400 Example `Status not found`:

```json
{
  "code": "WCAC0020",
  "message": "Status not found"
}
```

##### Response 404

404 Example `status not found`:

```json
{
  "code": "WCAC0020",
  "message": "Status not found"
}
```

404 Example `reason not found`:

```json
{
  "code": "WCAC0021",
  "message": "Reason not found"
}
```

##### Response 422

422 Example `status not found`:

```json
{
  "code": "WCAC0038",
  "message": "Account status update blocked: operation blocked for account."
}
```

##### Response 500

500 Example `Generic internal error`:

```json
{
  "code": "ECMN9999",
  "message": "Internal error"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `WCAC0012` | Corporate account not found |
| 400 | `WCAC0013` | Invalid JSON payload received: Error unmarshalling request. |
| 400 | `WCAC0005` | status is a required field |
| 400 | `WCAC0034` | status is specified in account's dormancy config |
| 400 | `WCAC0037` | account is not currently in the final status |
| 400 | `WCAC0036` | status cannot be final |
| 400 | `WCAC0020` | Status not found |
| 404 | `WCAC0020` | Status not found |
| 404 | `WCAC0021` | Reason not found |
| 422 | `WCAC0038` | Account status update blocked: operation blocked for account. |
| 500 | `ECMN9999` | Internal error |

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `account-status-change-2` | https://developers.pismo.io/events/docs/account-status-change-2 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `204;400;404;422;500`, has examples `True`, emits events `1`, deprecated `False`.

Guides that link to this operation: `KU-AUTH-account-and-external-id-tokens`, `KU-BANK-managing-account-statuses`.

<!-- op: spec=api-specs/Banking_-_Transaction_banking.yaml method=GET path=/corporate/v1/corporate-account-status/reasons operationId=v1-get-account-status-reason -->
### `GET /corporate/v1/corporate-account-status/reasons` — List transaction banking account status reasons

- **operationId:** `v1-get-account-status-reason`
- **Specification:** `api-specs/Banking_-_Transaction_banking.yaml` (Banking - Transaction banking)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Accounts`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> List transaction banking account status reasons.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `nextCursor` | query | no | string | Cursor value used to get the next page | example: "MEgCQQCo9+BpMRYQ/dL3DS2CyJxRF+j6ctbT3/Qp84+KeFhnii7NT7fELilKUSnxS30WAvQCCo2yU1orfgqr41mM70MBAgMBAAE=" |
| `maxItems` | query | no | integer | Number of items on current page | format: "int32"; minimum: 1; maximum: 200; example: 100 |
| `page` | query | no | integer | Requested page | format: "int32"; minimum: 1; example: 1 |
| `perPage` | query | no | integer | Items per page | format: "int32"; minimum: 1; maximum: 100; example: 100; deprecated: true |
| `name` | query | no | string | Filter by reason name | example: "Unblocked" |
| `state` | query | no | array of string | Filter by `ACTIVE` or `INACTIVE`. Default is `ACTIVE``. | items.enum: ["ACTIVE", "INACTIVE"]; example: ["INACTIVE"] |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `StatusReasonsResponse`) |
| 400 | Bad request | `application/json`: object (schema `ListStatusMessageResponse`) |
| 500 | Internal server error | `application/json`: object (schema `ListStatusMessageResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `next_cursor` | string (schema `NextCursor`) | no | Cursor value for the next page | nullable: true; example: "MEgCQQCo9+BpMRYQ/dL3DS2CyJxRF+j6ctbT3/Qp84+KeFhnii7NT7fELilKUSnxS30WAvQCCo2yU1orfgqr41mM70MBAgMBAAE=" |
| `has_next` | boolean (schema `StatusCursorHasNext`) | no | If `true`, there are more items in the next request (retrieved using the `next_cursor` value). If `false`, this is the last page of the results. | example: true |
| `count` | integer (schema `CurrentPageCount`) | no | Number of items on the current page | format: "int32"; example: 100 |
| `current_page` | integer (schema `StatusCurrentPageDeprecated`) | no | Current page | format: "int32"; deprecated: true; example: 1 |
| `per_page` | integer (schema `StatusPerPageDeprecated`) | no | Maximum items per page | format: "int64"; deprecated: true; example: 100 |
| `pages` | integer (schema `StatusNumberOfPagesDeprecated`) | no | Total pages | format: "int32"; deprecated: true; example: 100 |
| `total_items` | integer (schema `StatusTotalItemsDeprecated`) | no | Total items | format: "int32"; deprecated: true; example: 500 |
| `items` | array of object (schema `ListStatusReasonResponse`) | no | List of result items |  |

200 Example `Default response`:

```json
{
  "next_cursor": null,
  "has_next": false,
  "count": 8,
  "current_page": 0,
  "per_page": 0,
  "pages": 0,
  "total_items": 0,
  "items": [
    {
      "reason_id": 17,
      "reason_external_id": "CREDIT_ONLY",
      "name": null,
      "description": "Credit only",
      "state": "ACTIVE"
    },
    {
      "reason_id": 18,
      "reason_external_id": "DEBIT_ONLY",
      "name": null,
      "description": "Debit only",
      "state": "ACTIVE"
    },
    {
      "reason_id": 19,
      "reason_external_id": "ALL",
      "name": null,
      "description": "Any",
      "state": "ACTIVE"
    },
    {
      "reason_id": 20,
      "reason_external_id": "NONE",
      "name": null,
      "description": "Manual",
      "state": "ACTIVE"
    },
    {
      "reason_id": 21,
      "reason_external_id": "CREDIT_ONLY_NO_FORCE_DEBIT_ALLOWED",
      "name": null,
      "description": "Credit Only - No Force Debit Allowed",
      "state": "ACTIVE"
    },
    {
      "reason_id": 22,
      "reason_external_id": "DEBIT_ONLY_NO_FORCE_CREDIT_ALLOWED",
      "name": null,
      "description": "Debit Only - No Force Credit Allowed",
      "state": "ACTIVE"
    },
    {
      "reason_id": 23,
      "reason_external_id": "ALL_NO_FORCE_ALLOWED",
      "name": null,
      "description": "Any - No Force Allowed",
      "state": "ACTIVE"
    },
    {
      "reason_id": 24,
      "reason_external_id": "NONE_NO_FORCE_ALLOWED",
      "name": null,
      "description": "Manual - No Force Allowed",
      "state": "ACTIVE"
    }
  ]
}
```

##### Response 400

400 Example `Invalid page parameter`:

```json
{
  "code": "EACC0005",
  "message": "One or more parameters with invalid format",
  "detail": {
    "payload": null,
    "parameters": [
      {
        "field": "page",
        "description": "invalid page parameters",
        "message": "Parameter with invalid format"
      }
    ],
    "external": null
  }
}
```

400 Example `Invalid per page parameter`:

```json
{
  "code": "EACC0005",
  "message": "One or more parameters with invalid format",
  "detail": {
    "parameters": [
      {
        "field": "perPage",
        "description": "Invalid per page parameter",
        "message": "Value is not a number"
      }
    ]
  }
}
```

400 Example `Invalid state parameter`:

```json
{
  "code": "EACC0018",
  "message": "One or more parameters with invalid format",
  "detail": {
    "parameters": [
      {
        "field": "state",
        "description": "Invalid state parameter",
        "message": "Value should be one of: ACTIVE, INACTIVE"
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
        "description": "Invalid maxItems parameter",
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
| 400 | `EACC0005` | One or more parameters with invalid format |
| 400 | `EACC0018` | One or more parameters with invalid format |
| 400 | `WACC0011` | Invalid cursor value |
| 500 | `EACC0000` | Timeout while executing the request |
| 500 | `EACC9999` | Something went wrong, please try again later |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;500`, has examples `True`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Banking_-_Transaction_banking.yaml method=POST path=/corporate/v1/corporate-accounts/{externalAccountId}/force-close operationId=post-accounts-accountId-force-close -->
### `POST /corporate/v1/corporate-accounts/{externalAccountId}/force-close` — Force close transaction banking account

- **operationId:** `post-accounts-accountId-force-close`
- **Specification:** `api-specs/Banking_-_Transaction_banking.yaml` (Banking - Transaction banking)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Accounts`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Initiates an asynchronous force‑closure of a transaction banking account by placing a closure instruction in the processing queue.
>
> All business rules, including balance checks, earmark verification, and status validation, are evaluated during asynchronous execution rather than when the request is submitted.
>
> **NOTE**:
>   * This endpoint requires an account token, an access token encoded with an external account ID. Tokens can expire quickly, which can result in a `401 Unauthorized` message.
>   * Calling this endpoint generates a [Force account closure succeeded](https://developers.pismo.io/events/docs/corporate-force-account-closure-1) event.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `externalAccountId` | path | yes | string | External account ID | minLength: 1; maxLength: 60; example: "12345678901" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 202 | Force close request accepted and enqueued for processing |  |
| 400 | Bad Request. The account ID is missing or has an invalid format | `application/json`: object (schema `ErrorResponse`) |
| 401 | Unauthorized | `application/json`: object (schema `ErrorResponse`) |
| 500 | Internal Server Error | `application/json`: object (schema `ErrorResponse`) |

##### Response 400

400 Example `Invalid account ID`:

```json
{
  "code": "WCAC0002",
  "message": "Invalid header account"
}
```

##### Response 401

401 Example `Account not authorized`:

```json
{
  "code": "WCAC0001",
  "message": "Account not authorized"
}
```

##### Response 500

500 Example `Generic internal error`:

```json
{
  "code": "ECMN9999",
  "message": "Internal error"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `WCAC0002` | Invalid header account |
| 401 | `WCAC0001` | Account not authorized |
| 500 | `ECMN9999` | Internal error |

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `corporate-force-account-closure-1` | https://developers.pismo.io/events/docs/corporate-force-account-closure-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `202;400;401;500`, has examples `True`, emits events `1`, deprecated `False`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/Overdraft -->
### Schema `Overdraft`

Pointer: `#/components/schemas/Overdraft`. Type: object (schema `Overdraft`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `limit` | number (schema `OverdraftLimit2`) | yes | Account overdraft limit | format: "float"; minimum: 0; maximum: 100000000000000000; example: 15680.45 |

<!-- schema: #/components/schemas/ErrorResponse -->
### Schema `ErrorResponse`

Pointer: `#/components/schemas/ErrorResponse`. Type: object (schema `ErrorResponse`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string (schema `ErrorCode`) | no | Error code<br>`minLength: 1`<br>`maxLength: 12`<br> | minLength: 1; maxLength: 12; example: "WPMT0017" |
| `message` | string (schema `ErrorMessage`) | no | Error message<br>`minLength: 1`<br>`maxLength: 1000`<br> | minLength: 1; maxLength: 1000; example: "Invalid JSON payload received: Error unmarshalling request" |

<!-- schema: #/components/schemas/ListStatusReasonResponse -->
### Schema `ListStatusReasonResponse`

Pointer: `#/components/schemas/ListStatusReasonResponse`. Type: object (schema `ListStatusReasonResponse`).

> Object response for account reason

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `reason_id` | integer (schema `ListStatusCreateAccountReasonID`) | no | Reason ID | format: "int64"; example: 1234567890 |
| `name` | string (schema `ListStatusCreateAccountReasonName`) | no | Reason name. The reason name is client-provided and created through [Create status reason](ref:v4-post-account-reason). | nullable: true; example: "Unblocked" |
| `description` | string (schema `ListStatusCreateAccountReasonDescription`) | no | Reason description | example: "Unblocked account after settling the account." |
| `state` | string (schema `ListStatusReasonState`) | no | Reason state | enum: ["ACTIVE", "INACTIVE"]; example: "ACTIVE" |
| `reason_external_id` | string (schema `ListStatusReasonExternalId`) | no | Client-generated ID that identifies a transaction from an external system. | maxLength: 60; example: "CREDIT_ONLY" |

<!-- schema: #/components/schemas/ListStatusMessageResponse -->
### Schema `ListStatusMessageResponse`

Pointer: `#/components/schemas/ListStatusMessageResponse`. Type: object (schema `ListStatusMessageResponse`).

> Object response for user message

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string (schema `ListStatusUserMessageCode`) | no | Code that identifies the user message | example: "EACC0000" |
| `message` | string (schema `ListStatusUserMessage`) | no | User message | example: "Timeout while executing the request" |
| `details` | object (schema `ListStatusMessageDetailsResponse`) | no | Object response for a user message |  |

<!-- schema: #/components/schemas/ListStatusMessageDetailsResponse -->
### Schema `ListStatusMessageDetailsResponse`

Pointer: `#/components/schemas/ListStatusMessageDetailsResponse`. Type: object (schema `ListStatusMessageDetailsResponse`).

> Object response for a user message

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `payload` | array of object (schema `ListStatusMessagePayloadResponse`) | no | Details for the request payload errors |  |
| `parameters` | array of object (schema `ListStatusMessageParameterResponse`) | no | Details for the query parameter errors |  |
| `external` | array of object (schema `ListStatusMessageExternalResponse`) | no | Details for the external service error |  |

<!-- schema: #/components/schemas/ListStatusMessagePayloadResponse -->
### Schema `ListStatusMessagePayloadResponse`

Pointer: `#/components/schemas/ListStatusMessagePayloadResponse`. Type: object (schema `ListStatusMessagePayloadResponse`).

> Object response for detailing request payload errors for a user message

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `field` | string (schema `ListStatusValidationErrorField`) | no | Field where validation returned error |  |
| `message` | string (schema `ListStatusValidationErrorMessage`) | no | Message description of the validation error |  |

<!-- schema: #/components/schemas/ListStatusMessageParameterResponse -->
### Schema `ListStatusMessageParameterResponse`

Pointer: `#/components/schemas/ListStatusMessageParameterResponse`. Type: object (schema `ListStatusMessageParameterResponse`).

> Object response for detailing query parameters errors for a user message

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `field` | string (schema `ListStatusValidationErrorField`) | no | Field where validation returned error |  |
| `message` | string (schema `ListStatusValidationErrorMessage`) | no | Message description of the validation error |  |

<!-- schema: #/components/schemas/ListStatusMessageExternalResponse -->
### Schema `ListStatusMessageExternalResponse`

Pointer: `#/components/schemas/ListStatusMessageExternalResponse`. Type: object (schema `ListStatusMessageExternalResponse`).

> Object response for detailing external errors for a user message

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string (schema `ListStatusExternalServiceCode`) | no | Code returned from the external service |  |
| `message` | string | no | Message description from the external service |  |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Banking_-_Transaction_banking.yaml` | tag `Accounts`: POST /corporate/v1/corporate-accounts, POST /corporate/v1/corporate-accounts/{externalAccountId}/close, GET /corporate/v1/corporate-accounts/{externalAccountId}, PATCH /corporate/v1/corporate-accounts/{externalAccountId}, PATCH /corporate/v2/corporate-accounts/{externalAccountId}/status, PATCH /corporate/v1/corporate-accounts/{externalAccountId}/entity, PATCH /corporate/v2/corporate-accounts/{externalAccountId}/status/rollback, GET /corporate/v1/corporate-account-status/reasons, POST /corporate/v1/corporate-accounts/{externalAccountId}/force-close | https://github.com/PismoDevEx/pismo-api-specs | `dec6c4900eb2db35…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-AUTH-account-and-external-id-tokens` — Endpoints that require account-specific or external-ID tokens
- `KU-BANK-account-balance-definitions-for-transaction-banking` — Account balance definitions for transaction banking
- `KU-BANK-divisions-and-hierarchies` — Divisions and hierarchies
- `KU-BANK-earmarks` — Earmarks
- `KU-BANK-get-started-demand-deposit-accounts` — Get started with demand deposit accounts (DDAs)
- `KU-BANK-get-started-transaction-banking` — Get started with transaction banking
- `KU-BANK-managing-account-statuses` — Manage account statuses
- `KU-BANK-transaction-banking-accounts` — Transaction banking and transaction banking accounts
- `KU-ERR-codes-acq-to-esma` — Error codes: ACQ to ESMA (32 prefixes)
- `KU-ERR-codes-esmg-to-whis` — Error codes: ESMG to WHIS (30 prefixes)
- `KU-ERR-codes-wcac` — Error codes: WCAC
- `KU-ERR-codes-wdiv` — Error codes: WDIV
- `KU-EVT-catalogue-account` — Event catalogue: account
- `KU-EVT-catalogue-corporate` — Event catalogue: corporate
- `KU-EVT-catalogue-other-domains` — Event catalogue: other event domains (accounting, authorization, availables, average, bulletin, cash, delinquent, fraud, instantpay, intl, ledger, networktransactions, onboarding, orgs, payment, platform, programs, rules, savings, statement)
- `KU-EVT-corporate-banking-data-events` — Banking - Transaction banking
- `KU-PAY-multi-leg-payments` — Multi-leg payments
