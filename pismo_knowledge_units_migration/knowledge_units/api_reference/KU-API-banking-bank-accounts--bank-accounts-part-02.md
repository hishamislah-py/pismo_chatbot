---
ku_id: KU-API-banking-bank-accounts--bank-accounts-part-02
title: 'API reference: Banking - Bank accounts — Bank accounts (part 2 of 2)'
category: api_reference
ku_type: api_reference
lifecycle: current
sources:
- path: api-specs/Banking_-_Bank_accounts.yaml
  sha256: 6245dc46ddfee395dbd8cb136682c7447bf07e0571419be697d65229bf6d77c7
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
- post-intl-bank-accounts-v2-accounts-account-id-bank-accounts-bban
- get-intl-bank-accounts-v2-bank-accounts-account-id-bank-accounts-scheme-name
- delete-intl-bank-accounts-v2-accounts-account-id-bank-accounts-scheme-name
- update-intl-bank-accounts-v2-accounts-account-id-bank-accounts-scheme-name
- get-intl-bank-accounts-v1-sort-codes-sort-code
- post-intl-bank-accounts-v3-bank-accounts-scheme-name-search
related_kus:
- KU-AUTH-account-and-external-id-tokens
- KU-ERR-codes-eiba
- KU-EVT-catalogue-other-domains
- KU-EVT-international-bank-accounts-data-events
- KU-PAY-faster-payment-system
specification_version: 1.0.0
---

# API reference: Banking - Bank accounts — Bank accounts (part 2 of 2)

**KU ID:** `KU-API-banking-bank-accounts--bank-accounts-part-02` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 6 operation(s) tagged `Bank accounts` in `api-specs/Banking_-_Bank_accounts.yaml` (“Banking - Bank accounts”, version `1.0.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Bank account management endpoints

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `POST /v2/accounts/{accountId}/bank-accounts/bban` | `post-intl-bank-accounts-v2-accounts-account-id-bank-accounts-bban` | Register BBAN account | no |
| `GET /v2/accounts/{accountId}/bank-accounts/{schemeName}` | `get-intl-bank-accounts-v2-bank-accounts-account-id-bank-accounts-scheme-name` | Get bank account | no |
| `DELETE /v2/accounts/{accountId}/bank-accounts/{schemeName}` | `delete-intl-bank-accounts-v2-accounts-account-id-bank-accounts-scheme-name` | Delete bank account | no |
| `PATCH /v2/accounts/{accountId}/bank-accounts/{schemeName}` | `update-intl-bank-accounts-v2-accounts-account-id-bank-accounts-scheme-name` | Update bank account | no |
| `GET /v1/sortcodes/{sortCode}` | `get-intl-bank-accounts-v1-sort-codes-sort-code` | Get UK bank branch info | no |
| `POST /v3/bank-accounts/{schemeName}/search` | `post-intl-bank-accounts-v3-bank-accounts-scheme-name-search` | Search bank account | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"} — Account token - token encoded with Pismo account ID. Tokens can expire quickly, which can result in an **401 Unauthorized** error.

## Operation contracts

<!-- op: spec=api-specs/Banking_-_Bank_accounts.yaml method=POST path=/v2/accounts/{accountId}/bank-accounts/bban operationId=post-intl-bank-accounts-v2-accounts-account-id-bank-accounts-bban -->
### `POST /v2/accounts/{accountId}/bank-accounts/bban` — Register BBAN account

- **operationId:** `post-intl-bank-accounts-v2-accounts-account-id-bank-accounts-bban`
- **Specification:** `api-specs/Banking_-_Bank_accounts.yaml` (Banking - Bank accounts)
- **Server base URL(s):** `https://sandbox.pismolabs.io/intl-bankaccounts`
- **Tags:** `Bank accounts`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Register a new Basic Bank Account Number (BBAN) bank account.
>
> BBAN is a bank account numbering system used in many countries, especially in Europe. For international transactions, the BBAN is combined with the country code and a checksum to create an IBAN (International Bank Account Number).
>
> To read about Pismo's banking offerings, see [Banking overview](doc:banking-overview).
>
> This endpoint generates a <a href="https://developers.pismo.io/events/docs/intl-bankaccounts-intl-bankaccount-register-1">Bank account registered</a> event.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Account token - Token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a **401 Unauthorized** error. <br> | example: 1234 |
| `accountId` | path | yes | string | Pismo account ID | example: "78123456" |

#### Request body

Required: yes

> Request Body

**Content type `application/json`** — schema: object (schema `intlbankaccounts.IntlBankAccountBbanRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `scheme` | object (schema `intlbankaccounts.BbanScheme`) | yes |  |  |
| `metadata` | object (schema `metadata`) | no | A set of key-value pairs used to store custom data or additional information.<br><br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis).<br> |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | Response Body | `application/json`: object (schema `intlbankaccounts.IntlBankAccountBbanResponse`) |
| 400 | Bad Request | `application/json`: object (schema `domain.Error`) |
| 403 | Forbidden | `application/json`: object (schema `domain.Error`) |
| 404 | Not Found | `application/json`: object (schema `domain.Error`) |
| 409 | Conflict | `application/json`: object (schema `domain.Error`) |
| 500 | Internal Server Error | `application/json`: object (schema `domain.Error`) |

##### Response 201

- Response header `x-cid`: Request tracking identifier. (string)
**201 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `account_id` | integer (schema `accountID`) | no | Account ID | example: 78123456 |
| `creation_datetime` | string (schema `creationDatetime`) | no | Account creation date time displayed in ISO 8601 format `2023-04-12T23:20:50.52Z`. | format: "date-time"; example: "2023-04-12T23:20:50.52Z" |
| `metadata` | object (schema `metadata`) | no | A set of key-value pairs used to store custom data or additional information.<br><br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis).<br> |  |
| `scheme` | object (schema `intlbankaccounts.BbanScheme`) | yes |  |  |

##### Response 400

- Response header `x-cid`: Request tracking identifier. (string)
400 Example `EIBA0009` (Validation Error):

```json
{
  "code": "EIBA0009",
  "message": "Validation error"
}
```

400 Example `EIBA0012` (Accounts API invalid request):

```json
{
  "code": "EIBA0012",
  "message": "Accounts - API returned 4xx error"
}
```

##### Response 403

- Response header `x-cid`: Request tracking identifier. (string)
403 Example `EIBA0006` (Missing tenant header):

```json
{
  "code": "EIBA0006",
  "message": "Missing required header: 'x-tenant'"
}
```

403 Example `EIBA0007` (Invalid account ID header):

```json
{
  "code": "EIBA0007",
  "message": "Invalid account ID header: 'x-account-id'"
}
```

403 Example `EIBA0023` (Account status not NORMAL):

```json
{
  "code": "EIBA0023",
  "message": "Account status not NORMAL"
}
```

##### Response 404

- Response header `x-cid`: Request tracking identifier. (string)
404 Example `EIBA0010` (Account not found):

```json
{
  "code": "EIBA0010",
  "message": "Account not found"
}
```

##### Response 409

- Response header `x-cid`: Request tracking identifier. (string)
409 Example `EIBA0028` (IntlBankAccount Already Exists):

```json
{
  "code": "EIBA0028",
  "message": "IntlBankAccount - Already Exists"
}
```

##### Response 500

- Response header `x-cid`: Request tracking identifier. (string)
500 Example `EIBA0005` (HTTP error):

```json
{
  "code": "EIBA0005",
  "message": "HTTP error"
}
```

500 Example `EIBA0011` (Accounts API server error):

```json
{
  "code": "EIBA0011",
  "message": "Accounts - API returned 5xx error"
}
```

500 Example `EIBA0013` (Accounts API timeout):

```json
{
  "code": "EIBA0013",
  "message": "Accounts - API timeout"
}
```

500 Example `EIBA0015` (Database error):

```json
{
  "code": "EIBA0015",
  "message": "Database internal error"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `EIBA0009` | Validation error |
| 400 | `EIBA0012` | Accounts - API returned 4xx error |
| 403 | `EIBA0006` | Missing required header: 'x-tenant' |
| 403 | `EIBA0007` | Invalid account ID header: 'x-account-id' |
| 403 | `EIBA0023` | Account status not NORMAL |
| 404 | `EIBA0010` | Account not found |
| 409 | `EIBA0028` | IntlBankAccount - Already Exists |
| 500 | `EIBA0005` | HTTP error |
| 500 | `EIBA0011` | Accounts - API returned 5xx error |
| 500 | `EIBA0013` | Accounts - API timeout |
| 500 | `EIBA0015` | Database internal error |

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `intl-bankaccounts-intl-bankaccount-register-1` | https://developers.pismo.io/events/docs/intl-bankaccounts-intl-bankaccount-register-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `201;400;403;404;409;500`, has examples `True`, emits events `1`, deprecated `False`.

Guides that link to this operation: `KU-AUTH-account-and-external-id-tokens`, `KU-EVT-international-bank-accounts-data-events`.

<!-- op: spec=api-specs/Banking_-_Bank_accounts.yaml method=GET path=/v2/accounts/{accountId}/bank-accounts/{schemeName} operationId=get-intl-bank-accounts-v2-bank-accounts-account-id-bank-accounts-scheme-name -->
### `GET /v2/accounts/{accountId}/bank-accounts/{schemeName}` — Get bank account

- **operationId:** `get-intl-bank-accounts-v2-bank-accounts-account-id-bank-accounts-scheme-name`
- **Specification:** `api-specs/Banking_-_Bank_accounts.yaml` (Banking - Bank accounts)
- **Server base URL(s):** `https://sandbox.pismolabs.io/intl-bankaccounts`
- **Tags:** `Bank accounts`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Get a bank account given its Pismo account ID and scheme name in the path.
>
> To read about Pismo's banking offerings, see [Banking overview](doc:banking-overview).

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Account token - Token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a **401 Unauthorized** error. <br> | example: 1234 |
| `accountId` | path | yes | string | Pismo account ID | example: "78123456" |
| `schemeName` | path | yes | string | Bank account's scheme (account type): <br>`IBAN` - International Bank Account Number  <br>`UK-SCAN` - UK bank account - sort code + account number (SCAN)<br>`BRAZIL` - Brazilian bank account <br>`BBAN` - Basic Bank Account Number<br>`ACH` - Automated Clearing House for US Account<br>`FEDWIRE` - US Account scheme<br>`CLABE` - Mexico bank account scheme<br> | enum: ["IBAN", "UK-SCAN", "BRAZIL", "BBAN", "ACH", "FEDWIRE", "CLABE"]; example: "IBAN" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Response | `application/json`: object (schema `intlbankaccounts.IntlBankAccountExternal`) |
| 400 | Bad | `application/json`: object (schema `domain.Error`) |
| 403 | Forbidden | `application/json`: object (schema `domain.Error`) |
| 404 | Not Found | `application/json`: object (schema `domain.Error`) |
| 500 | Internal Server Error | `application/json`: object (schema `domain.Error`) |

##### Response 200

- Response header `x-cid`: Request tracking identifier. (string)
**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `account_id` | integer (schema `accountID`) | no | Account ID | example: 78123456 |
| `creation_datetime` | string (schema `creationDatetime`) | no | Account creation date time displayed in ISO 8601 format `2023-04-12T23:20:50.52Z`. | format: "date-time"; example: "2023-04-12T23:20:50.52Z" |
| `updated_datetime` | string (schema `updatedDatetime`) | no | Updated date time. A RFC 3339 value, i.e., "2023-04-12T23:20:50.52Z". | format: "date-time"; example: "2023-04-12T23:20:50.52Z" |
| `metadata` | object (schema `metadata`) | no | A set of key-value pairs used to store custom data or additional information.<br><br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis).<br> |  |
| `scheme` | oneOf: object (schema `intlbankaccounts.IbanScheme`), object (schema `intlbankaccounts.UkScanScheme`), object (schema `intlbankaccounts.BrazilScheme`), object (schema `intlbankaccounts.BbanScheme`), object (schema `intlbankaccounts.AchScheme`), object (schema `intlbankaccounts.FedWireScheme`), object (schema `intlbankaccounts.ClabeScheme`) | no |  |  |

##### Response 400

- Response header `x-cid`: Request tracking identifier. (string)
400 Example `EIBA0012` (Accounts API invalid request):

```json
{
  "code": "EIBA0012",
  "message": "Accounts - API returned 4xx error"
}
```

400 Example `EIBA0016` (Account ID mismatch):

```json
{
  "code": "EIBA0016",
  "message": "Account ID in header does not match account ID in request body"
}
```

400 Example `EIBA0030` (Invalid Value for Scheme Name):

```json
{
  "code": "EIBA0030",
  "message": "Invalid value for scheme_name"
}
```

##### Response 403

- Response header `x-cid`: Request tracking identifier. (string)
403 Example `EIBA0006` (Missing tenant header):

```json
{
  "code": "EIBA0006",
  "message": "Missing required header: 'x-tenant'"
}
```

403 Example `EIBA0007` (Invalid account ID header):

```json
{
  "code": "EIBA0007",
  "message": "Invalid account ID header: 'x-account-id'"
}
```

403 Example `EIBA0023` (Account status not NORMAL):

```json
{
  "code": "EIBA0023",
  "message": "Account status not NORMAL"
}
```

##### Response 404

- Response header `x-cid`: Request tracking identifier. (string)
404 Example `EIBA0010` (Account not found):

```json
{
  "code": "EIBA0010",
  "message": "Account not found"
}
```

404 Example `EIBA0029` (IntlBankAccount not found):

```json
{
  "code": "EIBA0022",
  "message": "IntlBankAccount not found"
}
```

##### Response 500

- Response header `x-cid`: Request tracking identifier. (string)
500 Example `EIBA0005` (HTTP error):

```json
{
  "code": "EIBA0005",
  "message": "HTTP error"
}
```

500 Example `EIBA0011` (Accounts API server error):

```json
{
  "code": "EIBA0011",
  "message": "Accounts - API returned 5xx error"
}
```

500 Example `EIBA0013` (Accounts API timeout):

```json
{
  "code": "EIBA0013",
  "message": "Accounts - API timeout"
}
```

500 Example `EIBA0015` (Database error):

```json
{
  "code": "EIBA0015",
  "message": "Database internal error"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `EIBA0012` | Accounts - API returned 4xx error |
| 400 | `EIBA0016` | Account ID in header does not match account ID in request body |
| 400 | `EIBA0030` | Invalid value for scheme_name |
| 403 | `EIBA0006` | Missing required header: 'x-tenant' |
| 403 | `EIBA0007` | Invalid account ID header: 'x-account-id' |
| 403 | `EIBA0023` | Account status not NORMAL |
| 404 | `EIBA0010` | Account not found |
| 404 | `EIBA0022` | IntlBankAccount not found |
| 500 | `EIBA0005` | HTTP error |
| 500 | `EIBA0011` | Accounts - API returned 5xx error |
| 500 | `EIBA0013` | Accounts - API timeout |
| 500 | `EIBA0015` | Database internal error |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;403;404;500`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-AUTH-account-and-external-id-tokens`.

<!-- op: spec=api-specs/Banking_-_Bank_accounts.yaml method=DELETE path=/v2/accounts/{accountId}/bank-accounts/{schemeName} operationId=delete-intl-bank-accounts-v2-accounts-account-id-bank-accounts-scheme-name -->
### `DELETE /v2/accounts/{accountId}/bank-accounts/{schemeName}` — Delete bank account

- **operationId:** `delete-intl-bank-accounts-v2-accounts-account-id-bank-accounts-scheme-name`
- **Specification:** `api-specs/Banking_-_Bank_accounts.yaml` (Banking - Bank accounts)
- **Server base URL(s):** `https://sandbox.pismolabs.io/intl-bankaccounts`
- **Tags:** `Bank accounts`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Delete a bank account given its Pismo account ID and scheme name in the path.
>
> To read about Pismo's banking offerings, see [Banking overview](doc:banking-overview).
>
> This endpoint generates a <a href="https://developers.pismo.io/events/docs/intl-bankaccounts-intl-bankaccount-update-1">Bank account updated</a> event.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Account token - Token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a **401 Unauthorized** error. <br> | example: 1234 |
| `accountId` | path | yes | string | Pismo account ID | example: "78123456" |
| `schemeName` | path | yes | string | Bank account's scheme (account type): <br>`IBAN` - International Bank Account Number  <br>`UK-SCAN` - UK bank account - sort code + account number (SCAN)<br>`BRAZIL` - Brazilian bank account <br>`BBAN` - Basic Bank Account Number<br>`ACH` - Automated Clearing House for US Account<br>`FEDWIRE` - US Account scheme<br>`CLABE` - Mexico bank account scheme<br> | enum: ["IBAN", "UK-SCAN", "BRAZIL", "BBAN", "ACH", "FEDWIRE", "CLABE"]; example: "IBAN" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 204 | Response does not contain a body in case of successful deletion |  |
| 400 | Bad Request | `application/json`: object (schema `domain.Error`) |
| 403 | Forbidden | `application/json`: object (schema `domain.Error`) |
| 404 | Not | `application/json`: object (schema `domain.Error`) |
| 500 | Internal Server | `application/json`: object (schema `domain.Error`) |

##### Response 400

- Response header `x-cid`: Request tracking identifier. (string)
400 Example `EIBA0012` (Accounts API invalid request):

```json
{
  "code": "EIBA0012",
  "message": "Accounts - API returned 4xx error"
}
```

400 Example `EIBA0016` (Account ID mismatch):

```json
{
  "code": "EIBA0016",
  "message": "Account ID in header does not match account ID in request body"
}
```

##### Response 403

- Response header `x-cid`: Request tracking identifier. (string)
403 Example `EIBA0006` (Missing tenant header):

```json
{
  "code": "EIBA0006",
  "message": "Missing required header: 'x-tenant'"
}
```

403 Example `EIBA0007` (Invalid account ID header):

```json
{
  "code": "EIBA0007",
  "message": "Invalid account ID header: 'x-account-id'"
}
```

403 Example `EIBA0023` (Account status not NORMAL):

```json
{
  "code": "EIBA0023",
  "message": "Account status not NORMAL"
}
```

##### Response 404

- Response header `x-cid`: Request tracking identifier. (string)
404 Example `EIBA0010` (Account not found):

```json
{
  "code": "EIBA0010",
  "message": "Account not found"
}
```

##### Response 500

- Response header `x-cid`: Request tracking identifier. (string)
500 Example `EIBA0005` (HTTP error):

```json
{
  "code": "EIBA0005",
  "message": "HTTP error"
}
```

500 Example `EIBA0011` (Accounts API server error):

```json
{
  "code": "EIBA0011",
  "message": "Accounts - API returned 5xx error"
}
```

500 Example `EIBA0013` (Accounts API timeout):

```json
{
  "code": "EIBA0013",
  "message": "Accounts - API timeout"
}
```

500 Example `EIBA0015` (Database error):

```json
{
  "code": "EIBA0015",
  "message": "Database internal error"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `EIBA0012` | Accounts - API returned 4xx error |
| 400 | `EIBA0016` | Account ID in header does not match account ID in request body |
| 403 | `EIBA0006` | Missing required header: 'x-tenant' |
| 403 | `EIBA0007` | Invalid account ID header: 'x-account-id' |
| 403 | `EIBA0023` | Account status not NORMAL |
| 404 | `EIBA0010` | Account not found |
| 500 | `EIBA0005` | HTTP error |
| 500 | `EIBA0011` | Accounts - API returned 5xx error |
| 500 | `EIBA0013` | Accounts - API timeout |
| 500 | `EIBA0015` | Database internal error |

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `intl-bankaccounts-intl-bankaccount-update-1` | https://developers.pismo.io/events/docs/intl-bankaccounts-intl-bankaccount-update-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `204;400;403;404;500`, has examples `True`, emits events `1`, deprecated `False`.

Guides that link to this operation: `KU-AUTH-account-and-external-id-tokens`, `KU-EVT-international-bank-accounts-data-events`, `KU-PAY-faster-payment-system`.

<!-- op: spec=api-specs/Banking_-_Bank_accounts.yaml method=PATCH path=/v2/accounts/{accountId}/bank-accounts/{schemeName} operationId=update-intl-bank-accounts-v2-accounts-account-id-bank-accounts-scheme-name -->
### `PATCH /v2/accounts/{accountId}/bank-accounts/{schemeName}` — Update bank account

- **operationId:** `update-intl-bank-accounts-v2-accounts-account-id-bank-accounts-scheme-name`
- **Specification:** `api-specs/Banking_-_Bank_accounts.yaml` (Banking - Bank accounts)
- **Server base URL(s):** `https://sandbox.pismolabs.io/intl-bankaccounts`
- **Tags:** `Bank accounts`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Update a bank account given its Pismo account ID and scheme name in the path.
>
> To read about Pismo's banking offerings, see [Banking overview](doc:banking-overview).
>
> This endpoint generates a <a href="https://developers.pismo.io/events/docs/intl-bankaccounts-intl-bankaccount-update-1">Bank account updated</a> event.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Account token - Token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a **401 Unauthorized** error. <br> | example: 1234 |
| `accountId` | path | yes | string | Pismo account ID | example: "78123456" |
| `schemeName` | path | yes | string | Bank account's scheme (account type): <br>`IBAN` - International Bank Account Number  <br>`UK-SCAN` - UK bank account - sort code + account number (SCAN)<br>`BRAZIL` - Brazilian bank account <br>`BBAN` - Basic Bank Account Number<br>`ACH` - Automated Clearing House for US Account<br>`FEDWIRE` - US Account scheme<br>`CLABE` - Mexico bank account scheme<br> | enum: ["IBAN", "UK-SCAN", "BRAZIL", "BBAN", "ACH", "FEDWIRE", "CLABE"]; example: "IBAN" |

#### Request body

Required: yes

> Request Body

**Content type `application/json`** — schema: object (schema `intlbankaccounts.UpdateIntlBankAccountRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `metadata` | object (schema `metadata`) | no | A set of key-value pairs used to store custom data or additional information.<br><br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis).<br> |  |
| `scheme` | object | yes | Scheme-specific fields |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 204 | Response does not contain a body in case of successful update |  |
| 400 | Bad Request | `application/json`: object (schema `domain.Error`) |
| 403 | Forbidden | `application/json`: object (schema `domain.Error`) |
| 404 | Not | `application/json`: object (schema `domain.Error`) |
| 500 | Internal Server | `application/json`: object (schema `domain.Error`) |

##### Response 400

- Response header `x-cid`: Request tracking identifier. (string)
400 Example `EIBA0012` (Accounts API invalid request):

```json
{
  "code": "EIBA0012",
  "message": "Accounts - API returned 4xx error"
}
```

400 Example `EIBA0016` (Account ID mismatch):

```json
{
  "code": "EIBA0016",
  "message": "Account ID in header does not match account ID in request body"
}
```

##### Response 403

- Response header `x-cid`: Request tracking identifier. (string)
403 Example `EIBA0006` (Missing tenant header):

```json
{
  "code": "EIBA0006",
  "message": "Missing required header: 'x-tenant'"
}
```

403 Example `EIBA0007` (Invalid account ID header):

```json
{
  "code": "EIBA0007",
  "message": "Invalid account ID header: 'x-account-id'"
}
```

403 Example `EIBA0023` (Account status not NORMAL):

```json
{
  "code": "EIBA0023",
  "message": "Account status not NORMAL"
}
```

##### Response 404

- Response header `x-cid`: Request tracking identifier. (string)
404 Example `EIBA0010` (Account not found):

```json
{
  "code": "EIBA0010",
  "message": "Account not found"
}
```

##### Response 500

- Response header `x-cid`: Request tracking identifier. (string)
500 Example `EIBA0005` (HTTP error):

```json
{
  "code": "EIBA0005",
  "message": "HTTP error"
}
```

500 Example `EIBA0011` (Accounts API server error):

```json
{
  "code": "EIBA0011",
  "message": "Accounts - API returned 5xx error"
}
```

500 Example `EIBA0013` (Accounts API timeout):

```json
{
  "code": "EIBA0013",
  "message": "Accounts - API timeout"
}
```

500 Example `EIBA0015` (Database error):

```json
{
  "code": "EIBA0015",
  "message": "Database internal error"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `EIBA0012` | Accounts - API returned 4xx error |
| 400 | `EIBA0016` | Account ID in header does not match account ID in request body |
| 403 | `EIBA0006` | Missing required header: 'x-tenant' |
| 403 | `EIBA0007` | Invalid account ID header: 'x-account-id' |
| 403 | `EIBA0023` | Account status not NORMAL |
| 404 | `EIBA0010` | Account not found |
| 500 | `EIBA0005` | HTTP error |
| 500 | `EIBA0011` | Accounts - API returned 5xx error |
| 500 | `EIBA0013` | Accounts - API timeout |
| 500 | `EIBA0015` | Database internal error |

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `intl-bankaccounts-intl-bankaccount-update-1` | https://developers.pismo.io/events/docs/intl-bankaccounts-intl-bankaccount-update-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `204;400;403;404;500`, has examples `True`, emits events `1`, deprecated `False`.

Guides that link to this operation: `KU-AUTH-account-and-external-id-tokens`.

<!-- op: spec=api-specs/Banking_-_Bank_accounts.yaml method=GET path=/v1/sortcodes/{sortCode} operationId=get-intl-bank-accounts-v1-sort-codes-sort-code -->
### `GET /v1/sortcodes/{sortCode}` — Get UK bank branch info

- **operationId:** `get-intl-bank-accounts-v1-sort-codes-sort-code`
- **Specification:** `api-specs/Banking_-_Bank_accounts.yaml` (Banking - Bank accounts)
- **Server base URL(s):** `https://sandbox.pismolabs.io/intl-bankaccounts`
- **Tags:** `Bank accounts`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Get information for a United Kingdom (UK) bank-branch given its *sort code* in the path.
>
> To read about Pismo's banking offerings, see [Banking overview](doc:banking-overview).
>
> In UK banking, a sort code is a unique identification code used to route money transfers between banks and financial institutions. Its similar to a routing number in the US. It is a six-digit number that identifies both the bank and the specific branch. Each bank and branch has its own unique sort code. The first two digits identity the bank and the remaining 4 digits identify the branch.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Account token - Token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a **401 Unauthorized** error. <br> | example: 1234 |
| `sortCode` | path | yes | string | Sort code. Used to identify a UK bank-branch. The UK bank branch sort code is a six-digit code that is split into pairs with dashes in between. | example: "12-34-56" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Get UK bank-branch office info response | `application/json`: object (schema `sortcodes.GetSortCodeResponse`) |
| 400 | Bad | `application/json`: object (schema `domain.Error`) |
| 403 | Forbidden | `application/json`: object (schema `domain.Error`) |
| 404 | Not Found | `application/json`: object (schema `domain.Error`) |
| 500 | Internal Server | `application/json`: object (schema `domain.Error`) |

##### Response 200

- Response header `x-cid`: Request tracking identifier. (string)
**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `address_line_1` | string | no | Bank office address line 1. | minLength: 0; maxLength: 35; example: "Bolton Customer Service Centre" |
| `address_line_2` | string | no | Bank office address line 2. | minLength: 0; maxLength: 35; example: "PO Box 2027 Parklands" |
| `address_line_3` | string | no | Bank office address line 3. | minLength: 0; maxLength: 35; example: "De Havilland Way" |
| `address_line_4` | string | no | Bank office address line 4. | minLength: 0; maxLength: 35; example: "Horwich" |
| `bank_full_name` | string | no | Bankers' Automated Clearing Services (BACS) approved name. | minLength: 1; maxLength: 71; example: "NATIONAL WESTMINSTER BANK PLC" |
| `bank_short_name` | string | no | Bankers' Automated Clearing Services (BACS) approved short name. | minLength: 1; maxLength: 20; example: "NAT WEST BANK PLC" |
| `city` | string | no | Bank office's town/city. | minLength: 0; maxLength: 30; example: "Bolton" |
| `payment_schemes` | object (schema `sortcodes.PaymentSchemes`) | no |  |  |
| `sort_code` | string (schema `sortCode`) | no | In UK banking, a sort code is a unique identifier used to route money transfers between banks and financial institutions. Similar to a routing number in the US. It is a six-digit number that identifies both the bank and the specific branch office. Each bank branch office has its own unique sort code. The first two digits identity the bank and the remaining 4 digits identify the branch.<br> | minLength: 6; maxLength: 6; example: "123456" |
| `zip_code` | string | no | Bank office's postal code. | minLength: 0; maxLength: 9; example: "BL6 BL6" |

##### Response 400

- Response header `x-cid`: Request tracking identifier. (string)
400 Example `EIBA0031` (Invalid Sort Code):

```json
{
  "code": "EIBA0005",
  "message": "Invalid sort code path parameter, expected 6-digit number"
}
```

##### Response 403

- Response header `x-cid`: Request tracking identifier. (string)
##### Response 404

- Response header `x-cid`: Request tracking identifier. (string)
404 Example `EIBA0031` (Sort Code Not Found):

```json
{
  "code": "EIBA0005",
  "message": "Sort Code not found"
}
```

##### Response 500

- Response header `x-cid`: Request tracking identifier. (string)
500 Example `EIBA0005` (HTTP error):

```json
{
  "code": "EIBA0005",
  "message": "HTTP error"
}
```

500 Example `EIBA0011` (Accounts API server error):

```json
{
  "code": "EIBA0011",
  "message": "Accounts - API returned 5xx error"
}
```

500 Example `EIBA0015` (Database error):

```json
{
  "code": "EIBA0015",
  "message": "Database internal error"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `EIBA0005` | Invalid sort code path parameter, expected 6-digit number |
| 404 | `EIBA0005` | Sort Code not found |
| 500 | `EIBA0005` | HTTP error |
| 500 | `EIBA0011` | Accounts - API returned 5xx error |
| 500 | `EIBA0015` | Database internal error |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;403;404;500`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-AUTH-account-and-external-id-tokens`.

<!-- op: spec=api-specs/Banking_-_Bank_accounts.yaml method=POST path=/v3/bank-accounts/{schemeName}/search operationId=post-intl-bank-accounts-v3-bank-accounts-scheme-name-search -->
### `POST /v3/bank-accounts/{schemeName}/search` — Search bank account

- **operationId:** `post-intl-bank-accounts-v3-bank-accounts-scheme-name-search`
- **Specification:** `api-specs/Banking_-_Bank_accounts.yaml` (Banking - Bank accounts)
- **Server base URL(s):** `https://sandbox.pismolabs.io/intl-bankaccounts`
- **Tags:** `Bank accounts`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Search for a bank account using various account schemes.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `schemeName` | path | yes | string | Bank account's scheme (account type): <br>`IBAN` - International Bank Account Number  <br>`UK-SCAN` - UK bank account - sort code + account number (SCAN)<br>`BRAZIL` - Brazilian bank account <br>`BBAN` - Basic Bank Account Number<br>`ACH` - Automated Clearing House for US Account<br>`FEDWIRE` - US Account scheme<br>`CLABE` - Mexico bank account scheme<br> | enum: ["IBAN", "UK-SCAN", "BRAZIL", "BBAN", "ACH", "FEDWIRE", "CLABE"]; example: "IBAN" |

#### Request body

Required: yes

> Request body matching the scheme specified in the path parameter.

**Content type `application/json`** — schema: object (schema `intlbankaccounts.IntlBankAccountSearchRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `scheme` | oneOf: object (schema `intlbankaccounts.IbanScheme`), object (schema `intlbankaccounts.UkScanScheme`), object (schema `intlbankaccounts.BrazilScheme`), object (schema `intlbankaccounts.BbanScheme`), object (schema `intlbankaccounts.AchScheme`), object (schema `intlbankaccounts.FedWireScheme`), object (schema `intlbankaccounts.ClabeScheme`) | yes |  |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Success | `application/json`: object (schema `intlbankaccounts.IntlBankAccountExternal`) |
| 400 | Bad Request | `application/json`: object (schema `domain.Error`) |
| 403 | Forbidden | `application/json`: object (schema `domain.Error`) |
| 404 | Not Found | `application/json`: object (schema `domain.Error`) |
| 500 | Internal Server | `application/json`: object (schema `domain.Error`) |

##### Response 200

- Response header `x-cid`: Request tracking identifier. (string)
**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `account_id` | integer (schema `accountID`) | no | Account ID | example: 78123456 |
| `creation_datetime` | string (schema `creationDatetime`) | no | Account creation date time displayed in ISO 8601 format `2023-04-12T23:20:50.52Z`. | format: "date-time"; example: "2023-04-12T23:20:50.52Z" |
| `updated_datetime` | string (schema `updatedDatetime`) | no | Updated date time. A RFC 3339 value, i.e., "2023-04-12T23:20:50.52Z". | format: "date-time"; example: "2023-04-12T23:20:50.52Z" |
| `metadata` | object (schema `metadata`) | no | A set of key-value pairs used to store custom data or additional information.<br><br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis).<br> |  |
| `scheme` | oneOf: object (schema `intlbankaccounts.IbanScheme`), object (schema `intlbankaccounts.UkScanScheme`), object (schema `intlbankaccounts.BrazilScheme`), object (schema `intlbankaccounts.BbanScheme`), object (schema `intlbankaccounts.AchScheme`), object (schema `intlbankaccounts.FedWireScheme`), object (schema `intlbankaccounts.ClabeScheme`) | no |  |  |

##### Response 400

- Response header `x-cid`: Request tracking identifier. (string)
400 Example `EIBA0009` (Validation Error):

```json
{
  "code": "EIBA0009",
  "message": "Validation error"
}
```

400 Example `EIBA0012` (Accounts API invalid request):

```json
{
  "code": "EIBA0012",
  "message": "Accounts - API returned 4xx error"
}
```

##### Response 403

- Response header `x-cid`: Request tracking identifier. (string)
403 Example `EIBA0006` (Missing tenant header):

```json
{
  "code": "EIBA0006",
  "message": "Missing required header: 'x-tenant'"
}
```

##### Response 404

- Response header `x-cid`: Request tracking identifier. (string)
404 Example `EIBA0029` (Intl Bank Account not found):

```json
{
  "code": "EIBA0029",
  "message": "IntlBankAccount not found"
}
```

##### Response 500

- Response header `x-cid`: Request tracking identifier. (string)
500 Example `EIBA0005` (HTTP error):

```json
{
  "code": "EIBA0005",
  "message": "HTTP error"
}
```

500 Example `EIBA0011` (Accounts API server error):

```json
{
  "code": "EIBA0011",
  "message": "Accounts - API returned 5xx error"
}
```

500 Example `EIBA0013` (Accounts API timeout):

```json
{
  "code": "EIBA0013",
  "message": "Accounts - API timeout"
}
```

500 Example `EIBA0015` (Database error):

```json
{
  "code": "EIBA0015",
  "message": "Database internal error"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `EIBA0009` | Validation error |
| 400 | `EIBA0012` | Accounts - API returned 4xx error |
| 403 | `EIBA0006` | Missing required header: 'x-tenant' |
| 404 | `EIBA0029` | IntlBankAccount not found |
| 500 | `EIBA0005` | HTTP error |
| 500 | `EIBA0011` | Accounts - API returned 5xx error |
| 500 | `EIBA0013` | Accounts - API timeout |
| 500 | `EIBA0015` | Database internal error |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;403;404;500`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-AUTH-account-and-external-id-tokens`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/intlbankaccounts.BbanScheme -->
### Schema `intlbankaccounts.BbanScheme`

Pointer: `#/components/schemas/intlbankaccounts.BbanScheme`. Type: object (schema `intlbankaccounts.BbanScheme`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `bban` | string | yes | Basic Bank Account Number (BBAN). BBAN is a bank account numbering system used in many countries, especially in Europe. | maxLength: 30; example: "GB539007547034" |

<!-- schema: #/components/schemas/metadata -->
### Schema `metadata`

Pointer: `#/components/schemas/metadata`. Type: object (schema `metadata`).

> A set of key-value pairs used to store custom data or additional information.<br>
>
> **Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis).

<!-- schema: #/components/schemas/domain.Error -->
### Schema `domain.Error`

Pointer: `#/components/schemas/domain.Error`. Type: object (schema `domain.Error`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string | no | Error type code | example: "EIBA0001" |
| `details` | string | no | Error details | example: "Key not found" |
| `message` | string | no | Error message | example: "Key not found" |

<!-- schema: #/components/schemas/intlbankaccounts.IbanScheme -->
### Schema `intlbankaccounts.IbanScheme`

Pointer: `#/components/schemas/intlbankaccounts.IbanScheme`. Type: object (schema `intlbankaccounts.IbanScheme`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `iban` | string | yes | International Bank Account Number (IBAN).<br><br>IBAN structure varies by country, but typically includes a 2 letter country code, two check digits for error detection, a bank identifier and an account number.<br> | maxLength: 34; example: "GB29NWBK60161331926819" |

<!-- schema: #/components/schemas/intlbankaccounts.UkScanScheme -->
### Schema `intlbankaccounts.UkScanScheme`

Pointer: `#/components/schemas/intlbankaccounts.UkScanScheme`. Type: object (schema `intlbankaccounts.UkScanScheme`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `account_number` | string | yes | Account number | maxLength: 8 |
| `sort_code` | string (schema `sortCode`) | yes | In UK banking, a sort code is a unique identifier used to route money transfers between banks and financial institutions. Similar to a routing number in the US. It is a six-digit number that identifies both the bank and the specific branch office. Each bank branch office has its own unique sort code. The first two digits identity the bank and the remaining 4 digits identify the branch.<br> | minLength: 6; maxLength: 6; example: "123456" |

<!-- schema: #/components/schemas/intlbankaccounts.BrazilScheme -->
### Schema `intlbankaccounts.BrazilScheme`

Pointer: `#/components/schemas/intlbankaccounts.BrazilScheme`. Type: object (schema `intlbankaccounts.BrazilScheme`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `bank` | string (schema `brazilBank`) | yes | <a href="https://bank.codes/numero-do-banco/bank/banco-central-do-brasil/" target="_blank">ISPB (Identificador do Sistema de Pagamento Brazil)</a> - the Brazilian payment system bank ID, the value is eight alphanumeric characters. | minLength: 8; maxLength: 8; example: "76523A28" |
| `branch` | string (schema `brazilBranch`) | yes | Branch code, a four-digit value. Values under four digits are left-padded with zeroes. | minLength: 1; maxLength: 4; example: "0186" |
| `account_number` | string (schema `brazilAccountNumber`) | yes | Account number. Cannot contain leading zeroes. | minLength: 1; maxLength: 13; example: "1773065291" |
| `supplementary_data` | object (schema `intlbankaccounts.BrazilSupplementaryData`) | yes |  |  |

<!-- schema: #/components/schemas/intlbankaccounts.AchScheme -->
### Schema `intlbankaccounts.AchScheme`

Pointer: `#/components/schemas/intlbankaccounts.AchScheme`. Type: object (schema `intlbankaccounts.AchScheme`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `account_number` | string (schema `usaAccountNumber`) | yes | Account number | minLength: 17; maxLength: 17; example: "12345678901234567" |
| `routing_number` | string (schema `usaRoutingNumber`) | yes | A routing number is a nine-digit number used to identify a financial institution in the United States. It is also known as an ABA (American Bankers Association) number.<br> | minLength: 9; maxLength: 9; example: "123456789" |

<!-- schema: #/components/schemas/intlbankaccounts.FedWireScheme -->
### Schema `intlbankaccounts.FedWireScheme`

Pointer: `#/components/schemas/intlbankaccounts.FedWireScheme`. Type: object (schema `intlbankaccounts.FedWireScheme`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `account_number` | string (schema `usaAccountNumber`) | yes | Account number | minLength: 17; maxLength: 17; example: "12345678901234567" |
| `routing_number` | string (schema `usaRoutingNumber`) | yes | A routing number is a nine-digit number used to identify a financial institution in the United States. It is also known as an ABA (American Bankers Association) number.<br> | minLength: 9; maxLength: 9; example: "123456789" |

<!-- schema: #/components/schemas/intlbankaccounts.ClabeScheme -->
### Schema `intlbankaccounts.ClabeScheme`

Pointer: `#/components/schemas/intlbankaccounts.ClabeScheme`. Type: object (schema `intlbankaccounts.ClabeScheme`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `clabe` | string | yes | The Clave Bancaria Estandarizada (CLABE) is an 18-digit standardized bank code used for identifying bank accounts in Mexico.<br> | minLength: 18; example: "003290103581700922" |

<!-- schema: #/components/schemas/sortcodes.PaymentSchemes -->
### Schema `sortcodes.PaymentSchemes`

Pointer: `#/components/schemas/sortcodes.PaymentSchemes`. Type: object (schema `sortcodes.PaymentSchemes`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `bacs` | boolean | no | Does the bank/branch participate in the Banker's Automated Clearing Service (BACS) payment system?<br> | example: true |
| `chaps` | boolean | no | Does the bank/branch participate in the Clearing House Automated Payment System (CHAPS)?<br> | example: true |
| `fps` | boolean | no | Does the bank/branch participate in the Faster Payment System (FPS)?<br> | example: true |
| `ics` | boolean | no | Does the bank/branch participate in the Image Clearing System (ICS) used for processing cheques in the UK?<br> | example: true |

<!-- schema: #/components/schemas/intlbankaccounts.BrazilSupplementaryData -->
### Schema `intlbankaccounts.BrazilSupplementaryData`

Pointer: `#/components/schemas/intlbankaccounts.BrazilSupplementaryData`. Type: object (schema `intlbankaccounts.BrazilSupplementaryData`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `account_type` | string (schema `brazilAccountType`) | yes | Account type:  <br>  `CACC` - Checking/current account. Known as "conta corrente" in Portuguese, this is a bank account type designed for everyday financial transactions and is the most common type individuals and businesses use for day-to-day banking.<br>  `SVGS` - Savings account<br>  `TRAN` - Payment account. Payment institutions offer payment accounts to move funds and make payments, while banks offer checking accounts that include full financial services such as credit and investments.<br>  `SLRY` - Salary account. Employer deposits a fixed amount every month.<br> | enum: ["CACC", "SLRY", "SVGS", "TRAN"]; maxLength: 4; example: "TRAN" |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Banking_-_Bank_accounts.yaml` | tag `Bank accounts`: POST /v2/accounts/{accountId}/bank-accounts/bban, GET /v2/accounts/{accountId}/bank-accounts/{schemeName}, DELETE /v2/accounts/{accountId}/bank-accounts/{schemeName}, PATCH /v2/accounts/{accountId}/bank-accounts/{schemeName}, GET /v1/sortcodes/{sortCode}, POST /v3/bank-accounts/{schemeName}/search | https://github.com/PismoDevEx/pismo-api-specs | `6245dc46ddfee395…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-AUTH-account-and-external-id-tokens` — Endpoints that require account-specific or external-ID tokens
- `KU-ERR-codes-eiba` — Error codes: EIBA
- `KU-EVT-catalogue-other-domains` — Event catalogue: other event domains (accounting, authorization, availables, average, bulletin, cash, delinquent, fraud, instantpay, intl, ledger, networktransactions, onboarding, orgs, payment, platform, programs, rules, savings, statement)
- `KU-EVT-international-bank-accounts-data-events` — Banking - Bank accounts
- `KU-PAY-faster-payment-system` — Faster Payments (UK)
