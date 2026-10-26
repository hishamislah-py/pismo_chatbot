---
ku_id: KU-API-banking-bank-accounts--bank-accounts-part-01
title: 'API reference: Banking - Bank accounts — Bank accounts (part 1 of 2)'
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
- post-intl-bank-accounts-v2-accounts-account-id-bank-accounts-iban
- post-intl-bank-accounts-v2-accounts-account-id-bank-accounts-ach
- post-intl-bank-accounts-v2-accounts-account-id-bank-accounts-fedwire
- post-intl-bank-accounts-v2-accounts-account-id-bank-accounts-clabe
- post-intl-bank-accounts-v2-accounts-account-id-bank-accounts-uk-scan
- post-intl-bank-accounts-v2-accounts-account-id-bank-accounts-brazil
related_kus:
- KU-AUTH-account-and-external-id-tokens
- KU-BANK-banking-overview
- KU-ERR-codes-eiba
- KU-EVT-catalogue-other-domains
- KU-EVT-international-bank-accounts-data-events
- KU-PAY-bacs
- KU-PAY-faster-payment-system
specification_version: 1.0.0
---

# API reference: Banking - Bank accounts — Bank accounts (part 1 of 2)

**KU ID:** `KU-API-banking-bank-accounts--bank-accounts-part-01` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 6 operation(s) tagged `Bank accounts` in `api-specs/Banking_-_Bank_accounts.yaml` (“Banking - Bank accounts”, version `1.0.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Bank account management endpoints

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `POST /v2/accounts/{accountId}/bank-accounts/iban` | `post-intl-bank-accounts-v2-accounts-account-id-bank-accounts-iban` | Register IBAN account | no |
| `POST /v2/accounts/{accountId}/bank-accounts/ach` | `post-intl-bank-accounts-v2-accounts-account-id-bank-accounts-ach` | Register ACH account | no |
| `POST /v2/accounts/{accountId}/bank-accounts/fedwire` | `post-intl-bank-accounts-v2-accounts-account-id-bank-accounts-fedwire` | Register Fedwire account | no |
| `POST /v2/accounts/{accountId}/bank-accounts/clabe` | `post-intl-bank-accounts-v2-accounts-account-id-bank-accounts-clabe` | Register CLABE account | no |
| `POST /v2/accounts/{accountId}/bank-accounts/uk-scan` | `post-intl-bank-accounts-v2-accounts-account-id-bank-accounts-uk-scan` | Register UK bank account | no |
| `POST /v2/accounts/{accountId}/bank-accounts/brazil` | `post-intl-bank-accounts-v2-accounts-account-id-bank-accounts-brazil` | Register Brazilian bank account | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"} — Account token - token encoded with Pismo account ID. Tokens can expire quickly, which can result in an **401 Unauthorized** error.

## Operation contracts

<!-- op: spec=api-specs/Banking_-_Bank_accounts.yaml method=POST path=/v2/accounts/{accountId}/bank-accounts/iban operationId=post-intl-bank-accounts-v2-accounts-account-id-bank-accounts-iban -->
### `POST /v2/accounts/{accountId}/bank-accounts/iban` — Register IBAN account

- **operationId:** `post-intl-bank-accounts-v2-accounts-account-id-bank-accounts-iban`
- **Specification:** `api-specs/Banking_-_Bank_accounts.yaml` (Banking - Bank accounts)
- **Server base URL(s):** `https://sandbox.pismolabs.io/intl-bankaccounts`
- **Tags:** `Bank accounts`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Register a new International Bank Account Number (IBAN) bank account. 
>
> IBAN is a standardized international system developed to identify bank accounts when making international transactions. For more information, refer to <a href="https://www.investopedia.com/terms/i/iban.asp" target="_blank"> What Is an International Bank Account Number (IBAN) and How Does It Work</a>.
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

> Register IBAN request Body

**Content type `application/json`** — schema: object (schema `intlbankaccounts.IntlBankAccountIbanRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `scheme` | object (schema `intlbankaccounts.IbanScheme`) | yes |  |  |
| `metadata` | object (schema `metadata`) | no | A set of key-value pairs used to store custom data or additional information.<br><br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis).<br> |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | Response body | `application/json`: object (schema `intlbankaccounts.IntlBankAccountIbanResponse`) |
| 400 | Bad Request | `application/json`: object (schema `domain.Error`) |
| 403 | Forbidden | `application/json`: object (schema `domain.Error`) |
| 404 | Not Found | `application/json`: object (schema `domain.Error`) |
| 409 | Conflict | `application/json`: object (schema `domain.Error`) |
| 500 | Internal Server | `application/json`: object (schema `domain.Error`) |

##### Response 201

- Response header `x-cid`: Request tracking identifier. (string)
**201 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `account_id` | integer (schema `accountID`) | no | Account ID | example: 78123456 |
| `creation_datetime` | string (schema `creationDatetime`) | no | Account creation date time displayed in ISO 8601 format `2023-04-12T23:20:50.52Z`. | format: "date-time"; example: "2023-04-12T23:20:50.52Z" |
| `metadata` | object (schema `metadata`) | no | A set of key-value pairs used to store custom data or additional information.<br><br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis).<br> |  |
| `scheme` | object (schema `intlbankaccounts.IbanScheme`) | yes |  |  |

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

Guides that link to this operation: `KU-AUTH-account-and-external-id-tokens`, `KU-BANK-banking-overview`, `KU-EVT-international-bank-accounts-data-events`.

<!-- op: spec=api-specs/Banking_-_Bank_accounts.yaml method=POST path=/v2/accounts/{accountId}/bank-accounts/ach operationId=post-intl-bank-accounts-v2-accounts-account-id-bank-accounts-ach -->
### `POST /v2/accounts/{accountId}/bank-accounts/ach` — Register ACH account

- **operationId:** `post-intl-bank-accounts-v2-accounts-account-id-bank-accounts-ach`
- **Specification:** `api-specs/Banking_-_Bank_accounts.yaml` (Banking - Bank accounts)
- **Server base URL(s):** `https://sandbox.pismolabs.io/intl-bankaccounts`
- **Tags:** `Bank accounts`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Register a new Automated Clearing House (ACH) bank account. 
>
> ACH is an electronic network for financial transactions in the United States. ACH processes large volumes of credit and debit transactions in batches.
>
> To read about Pismo's banking offerings, see [Banking overview](doc:banking-overview).
>
> This endpoint generates a [Bank account registered](https://developers.pismo.io/events/docs/intl-bankaccounts-intl-bankaccount-register-1) event.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Account token - Token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a **401 Unauthorized** error. <br> | example: 1234 |
| `accountId` | path | yes | string | Pismo account ID | example: "78123456" |

#### Request body

Required: yes

> Register ACH request Body

**Content type `application/json`** — schema: object (schema `intlbankaccounts.IntlBankAccountAchRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `scheme` | object (schema `intlbankaccounts.AchScheme`) | yes |  |  |
| `metadata` | object (schema `metadata`) | no | A set of key-value pairs used to store custom data or additional information.<br><br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis).<br> |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | Response body | `application/json`: object (schema `intlbankaccounts.IntlBankAccountAchResponse`) |
| 400 | Bad Request | `application/json`: object (schema `domain.Error`) |
| 403 | Forbidden | `application/json`: object (schema `domain.Error`) |
| 404 | Not Found | `application/json`: object (schema `domain.Error`) |
| 409 | Conflict | `application/json`: object (schema `domain.Error`) |
| 500 | Internal Server | `application/json`: object (schema `domain.Error`) |

##### Response 201

- Response header `x-cid`: Request tracking identifier. (string)
**201 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `account_id` | integer (schema `accountID`) | no | Account ID | example: 78123456 |
| `creation_datetime` | string (schema `creationDatetime`) | no | Account creation date time displayed in ISO 8601 format `2023-04-12T23:20:50.52Z`. | format: "date-time"; example: "2023-04-12T23:20:50.52Z" |
| `metadata` | object (schema `metadata`) | no | A set of key-value pairs used to store custom data or additional information.<br><br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis).<br> |  |
| `scheme` | object (schema `intlbankaccounts.AchScheme`) | yes |  |  |

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

Guides that link to this operation: `KU-AUTH-account-and-external-id-tokens`.

<!-- op: spec=api-specs/Banking_-_Bank_accounts.yaml method=POST path=/v2/accounts/{accountId}/bank-accounts/fedwire operationId=post-intl-bank-accounts-v2-accounts-account-id-bank-accounts-fedwire -->
### `POST /v2/accounts/{accountId}/bank-accounts/fedwire` — Register Fedwire account

- **operationId:** `post-intl-bank-accounts-v2-accounts-account-id-bank-accounts-fedwire`
- **Specification:** `api-specs/Banking_-_Bank_accounts.yaml` (Banking - Bank accounts)
- **Server base URL(s):** `https://sandbox.pismolabs.io/intl-bankaccounts`
- **Tags:** `Bank accounts`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Register a new Fedwire bank account.
>
> Fedwire is a real-time gross settlement funds transfer system operated by the Federal Reserve Banks in the United States.
>
> To read about Pismo's banking offerings, see [Banking overview](doc:banking-overview).
>
> This endpoint generates a [Bank account registered](https://developers.pismo.io/events/docs/intl-bankaccounts-intl-bankaccount-register-1) event.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Account token - Token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a **401 Unauthorized** error. <br> | example: 1234 |
| `accountId` | path | yes | string | Pismo account ID | example: "78123456" |

#### Request body

Required: yes

> Register FedWire request Body

**Content type `application/json`** — schema: object (schema `intlbankaccounts.IntlBankAccountFedWireRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `scheme` | object (schema `intlbankaccounts.FedWireScheme`) | yes |  |  |
| `metadata` | object (schema `metadata`) | no | A set of key-value pairs used to store custom data or additional information.<br><br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis).<br> |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | Response body | `application/json`: object (schema `intlbankaccounts.IntlBankAccountFedWireResponse`) |
| 400 | Bad Request | `application/json`: object (schema `domain.Error`) |
| 403 | Forbidden | `application/json`: object (schema `domain.Error`) |
| 404 | Not Found | `application/json`: object (schema `domain.Error`) |
| 409 | Conflict | `application/json`: object (schema `domain.Error`) |
| 500 | Internal Server | `application/json`: object (schema `domain.Error`) |

##### Response 201

- Response header `x-cid`: Request tracking identifier. (string)
**201 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `account_id` | integer (schema `accountID`) | no | Account ID | example: 78123456 |
| `creation_datetime` | string (schema `creationDatetime`) | no | Account creation date time displayed in ISO 8601 format `2023-04-12T23:20:50.52Z`. | format: "date-time"; example: "2023-04-12T23:20:50.52Z" |
| `metadata` | object (schema `metadata`) | no | A set of key-value pairs used to store custom data or additional information.<br><br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis).<br> |  |
| `scheme` | object (schema `intlbankaccounts.FedWireScheme`) | yes |  |  |

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

Guides that link to this operation: `KU-AUTH-account-and-external-id-tokens`.

<!-- op: spec=api-specs/Banking_-_Bank_accounts.yaml method=POST path=/v2/accounts/{accountId}/bank-accounts/clabe operationId=post-intl-bank-accounts-v2-accounts-account-id-bank-accounts-clabe -->
### `POST /v2/accounts/{accountId}/bank-accounts/clabe` — Register CLABE account

- **operationId:** `post-intl-bank-accounts-v2-accounts-account-id-bank-accounts-clabe`
- **Specification:** `api-specs/Banking_-_Bank_accounts.yaml` (Banking - Bank accounts)
- **Server base URL(s):** `https://sandbox.pismolabs.io/intl-bankaccounts`
- **Tags:** `Bank accounts`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Register a new Clave Bancaria Estandarizada (CLABE) bank code for Mexican bank accounts. 
>
> A Clave Bancaria Estandarizada, commonly known as CLABE, is an 18-digit standardized banking code used in Mexico for domestic electronic fund transfers. It functions as a unique identifier for each bank account, similar to an International Bank Account Number (IBAN) in other countries. The CLABE is required for sending and receiving inter-bank transfers within Mexico. 
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

> Register CLABE request Body

**Content type `application/json`** — schema: object (schema `intlbankaccounts.IntlBankAccountClabeRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `scheme` | object (schema `intlbankaccounts.ClabeScheme`) | yes |  |  |
| `metadata` | object (schema `metadata`) | no | A set of key-value pairs used to store custom data or additional information.<br><br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis).<br> |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | Response body | `application/json`: object (schema `intlbankaccounts.IntlBankAccountClabeResponse`) |
| 400 | Bad Request | `application/json`: object (schema `domain.Error`) |
| 403 | Forbidden | `application/json`: object (schema `domain.Error`) |
| 404 | Not Found | `application/json`: object (schema `domain.Error`) |
| 409 | Conflict | `application/json`: object (schema `domain.Error`) |
| 500 | Internal Server | `application/json`: object (schema `domain.Error`) |

##### Response 201

- Response header `x-cid`: Request tracking identifier. (string)
**201 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `account_id` | integer (schema `accountID`) | no | Account ID | example: 78123456 |
| `creation_datetime` | string (schema `creationDatetime`) | no | Account creation date time displayed in ISO 8601 format `2023-04-12T23:20:50.52Z`. | format: "date-time"; example: "2023-04-12T23:20:50.52Z" |
| `metadata` | object (schema `metadata`) | no | A set of key-value pairs used to store custom data or additional information.<br><br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis).<br> |  |
| `scheme` | object (schema `intlbankaccounts.ClabeScheme`) | yes |  |  |

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

<!-- op: spec=api-specs/Banking_-_Bank_accounts.yaml method=POST path=/v2/accounts/{accountId}/bank-accounts/uk-scan operationId=post-intl-bank-accounts-v2-accounts-account-id-bank-accounts-uk-scan -->
### `POST /v2/accounts/{accountId}/bank-accounts/uk-scan` — Register UK bank account

- **operationId:** `post-intl-bank-accounts-v2-accounts-account-id-bank-accounts-uk-scan`
- **Specification:** `api-specs/Banking_-_Bank_accounts.yaml` (Banking - Bank accounts)
- **Server base URL(s):** `https://sandbox.pismolabs.io/intl-bankaccounts`
- **Tags:** `Bank accounts`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Register a new bank account with UK's sort code + account number (SCAN) scheme.
>
> In UK banking, a sort code is a unique identifier used to route money transfers between banks and financial institutions. Its similar to a routing number in the US. It is a six-digit number that identifies both the bank and the specific branch. Each bank and branch has its own unique sort code. The first two digits identify the bank and the remaining 4 digits identify the branch.
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

> Register UK bank account request body

**Content type `application/json`** — schema: object (schema `intlbankaccounts.IntlBankAccountUkScanRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `scheme` | object (schema `intlbankaccounts.UkScanScheme`) | yes |  |  |
| `metadata` | object (schema `metadata`) | no | A set of key-value pairs used to store custom data or additional information.<br><br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis).<br> |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | Response | `application/json`: object (schema `intlbankaccounts.IntlBankAccountUkScanResponse`) |
| 400 | Bad Request | `application/json`: object (schema `domain.Error`) |
| 403 | Forbidden | `application/json`: object (schema `domain.Error`) |
| 404 | Not Found | `application/json`: object (schema `domain.Error`) |
| 409 | Conflict | `application/json`: object (schema `domain.Error`) |
| 500 | Internal Server | `application/json`: object (schema `domain.Error`) |

##### Response 201

- Response header `x-cid`: Request tracking identifier. (string)
**201 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `account_id` | integer (schema `accountID`) | no | Account ID | example: 78123456 |
| `creation_datetime` | string (schema `creationDatetime`) | no | Account creation date time displayed in ISO 8601 format `2023-04-12T23:20:50.52Z`. | format: "date-time"; example: "2023-04-12T23:20:50.52Z" |
| `metadata` | object (schema `metadata`) | no | A set of key-value pairs used to store custom data or additional information.<br><br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis).<br> |  |
| `scheme` | object (schema `intlbankaccounts.UkScanScheme`) | yes |  |  |

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

Guides that link to this operation: `KU-AUTH-account-and-external-id-tokens`, `KU-EVT-international-bank-accounts-data-events`, `KU-PAY-bacs`, `KU-PAY-faster-payment-system`.

<!-- op: spec=api-specs/Banking_-_Bank_accounts.yaml method=POST path=/v2/accounts/{accountId}/bank-accounts/brazil operationId=post-intl-bank-accounts-v2-accounts-account-id-bank-accounts-brazil -->
### `POST /v2/accounts/{accountId}/bank-accounts/brazil` — Register Brazilian bank account

- **operationId:** `post-intl-bank-accounts-v2-accounts-account-id-bank-accounts-brazil`
- **Specification:** `api-specs/Banking_-_Bank_accounts.yaml` (Banking - Bank accounts)
- **Server base URL(s):** `https://sandbox.pismolabs.io/intl-bankaccounts`
- **Tags:** `Bank accounts`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Register a new bank account with Brazilian bank + branch + account number scheme.
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

> Register Brazilian bank account request body

**Content type `application/json`** — schema: object (schema `intlbankaccounts.IntlBankAccountBrazilRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `scheme` | object (schema `intlbankaccounts.BrazilScheme`) | yes |  |  |
| `metadata` | object (schema `metadata`) | no | A set of key-value pairs used to store custom data or additional information.<br><br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis).<br> |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | Register Brazilian bank account response body | `application/json`: object (schema `intlbankaccounts.IntlBankAccountBrazilResponse`) |
| 400 | Bad | `application/json`: object (schema `domain.Error`) |
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
| `scheme` | object (schema `intlbankaccounts.BrazilScheme`) | yes |  |  |

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

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/intlbankaccounts.IbanScheme -->
### Schema `intlbankaccounts.IbanScheme`

Pointer: `#/components/schemas/intlbankaccounts.IbanScheme`. Type: object (schema `intlbankaccounts.IbanScheme`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `iban` | string | yes | International Bank Account Number (IBAN).<br><br>IBAN structure varies by country, but typically includes a 2 letter country code, two check digits for error detection, a bank identifier and an account number.<br> | maxLength: 34; example: "GB29NWBK60161331926819" |

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
| `api-specs/Banking_-_Bank_accounts.yaml` | tag `Bank accounts`: POST /v2/accounts/{accountId}/bank-accounts/iban, POST /v2/accounts/{accountId}/bank-accounts/ach, POST /v2/accounts/{accountId}/bank-accounts/fedwire, POST /v2/accounts/{accountId}/bank-accounts/clabe, POST /v2/accounts/{accountId}/bank-accounts/uk-scan, POST /v2/accounts/{accountId}/bank-accounts/brazil | https://github.com/PismoDevEx/pismo-api-specs | `6245dc46ddfee395…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-AUTH-account-and-external-id-tokens` — Endpoints that require account-specific or external-ID tokens
- `KU-BANK-banking-overview` — Banking overview
- `KU-ERR-codes-eiba` — Error codes: EIBA
- `KU-EVT-catalogue-other-domains` — Event catalogue: other event domains (accounting, authorization, availables, average, bulletin, cash, delinquent, fraud, instantpay, intl, ledger, networktransactions, onboarding, orgs, payment, platform, programs, rules, savings, statement)
- `KU-EVT-international-bank-accounts-data-events` — Banking - Bank accounts
- `KU-PAY-bacs` — BACS: clearing, Direct Debit mandates and indemnity claims
- `KU-PAY-faster-payment-system` — Faster Payments (UK)
