---
ku_id: KU-API-banking-bank-accounts--beneficiaries
title: 'API reference: Banking - Bank accounts — Beneficiaries'
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
operations:
- get-intl-bank-accounts-v1-bank-accounts-beneficiaries
- post-intl-bank-accounts-v1-bank-accounts-beneficiaries
- post-intl-bank-accounts-v1-bank-accounts-beneficiaries-beneficiary-id-activate
- get-intl-bank-accounts-v1-bank-accounts-beneficiaries-beneficiary-id
- delete-intl-bank-accounts-v1-beneficiaries-beneficiary-id
- patch-intl-bank-accounts-v1-beneficiaries-beneficiary-id
related_kus:
- KU-AUTH-account-and-external-id-tokens
- KU-ERR-codes-eiba
specification_version: 1.0.0
---

# API reference: Banking - Bank accounts — Beneficiaries

**KU ID:** `KU-API-banking-bank-accounts--beneficiaries` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 6 operation(s) tagged `Beneficiaries` in `api-specs/Banking_-_Bank_accounts.yaml` (“Banking - Bank accounts”, version `1.0.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Beneficiaries management endpoints

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `GET /v1/beneficiaries` | `get-intl-bank-accounts-v1-bank-accounts-beneficiaries` | List beneficiaries | no |
| `POST /v1/beneficiaries` | `post-intl-bank-accounts-v1-bank-accounts-beneficiaries` | Register beneficiary | no |
| `POST /v1/beneficiaries/{beneficiaryId}/activate` | `post-intl-bank-accounts-v1-bank-accounts-beneficiaries-beneficiary-id-activate` | Activate beneficiary | no |
| `GET /v1/beneficiaries/{beneficiaryId}` | `get-intl-bank-accounts-v1-bank-accounts-beneficiaries-beneficiary-id` | Get beneficiary | no |
| `DELETE /v1/beneficiaries/{beneficiaryId}` | `delete-intl-bank-accounts-v1-beneficiaries-beneficiary-id` | Delete beneficiary | no |
| `PATCH /v1/beneficiaries/{beneficiaryId}` | `patch-intl-bank-accounts-v1-beneficiaries-beneficiary-id` | Update beneficiary | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"} — Account token - token encoded with Pismo account ID. Tokens can expire quickly, which can result in an **401 Unauthorized** error.

## Operation contracts

<!-- op: spec=api-specs/Banking_-_Bank_accounts.yaml method=GET path=/v1/beneficiaries operationId=get-intl-bank-accounts-v1-bank-accounts-beneficiaries -->
### `GET /v1/beneficiaries` — List beneficiaries

- **operationId:** `get-intl-bank-accounts-v1-bank-accounts-beneficiaries`
- **Specification:** `api-specs/Banking_-_Bank_accounts.yaml` (Banking - Bank accounts)
- **Server base URL(s):** `https://sandbox.pismolabs.io/intl-bankaccounts`
- **Tags:** `Beneficiaries`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> List registered beneficiaries with query filtering options.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Account token - Token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a **401 Unauthorized** error. <br> | example: 1234 |
| `lastEvaluatedCreationDatetime` | query | no | string | This is the `last_evaluated_creation_datetime` field from the response. You can use it to get the next page of results on a subsequent call.<br> |  |
| `perPage` | query | no | string | Number of items per page, min=1, max=100, default=20. |  |
| `order` | query | no | string | Sort order. Results are ordered on the `created_datetime` field. Default=`DESC`. | enum: ["DESC", "ASC"] |
| `name` | query | no | string | Beneficiary name | maxLength: 50 |
| `alias` | query | no | string | Beneficiary alias | maxLength: 20 |
| `enabled` | query | no | boolean | Return only active or non-active beneficiaries flag. If not passed, all beneficiares are returned. |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Response Body | `application/json`: object (schema `beneficiaries.SearchBeneficiaryResponse`) |
| 400 | Bad Request | `application/json`: object (schema `domain.Error`) |
| 403 | Forbidden | `application/json`: object (schema `domain.Error`) |
| 404 | Not Found | `application/json`: object (schema `domain.Error`) |
| 500 | Internal Server Error | `application/json`: object (schema `domain.Error`) |

##### Response 200

- Response header `x-cid`: Request tracking identifier. (string)
**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `items` | array of object (schema `beneficiaries.Beneficiary`) | no |  |  |
| `last_evaluated_creation_datetime` | string | no | Use this field to get next results |  |
| `per_page` | integer | no | Items per page. | example: 10 |
| `total_items` | integer | no | Total items | example: 100 |

##### Response 400

- Response header `x-cid`: Request tracking identifier. (string)
400 Example `EIBA0012` (Accounts API invalid request):

```json
{
  "code": "EIBA0012",
  "message": "Accounts - API returned 4xx error"
}
```

400 Example `EIBA0018` (Invalid perPage Query Parameter):

```json
{
  "code": "EIBA0018",
  "message": "Invalid value for query param 'perPage'"
}
```

400 Example `EIBA0019` (Invalid Datetime Query Parameter):

```json
{
  "code": "EIBA0019",
  "message": "Invalid value for datetime query parameter. RFC3339 format must be used"
}
```

400 Example `EIBA0020` (Invalid Boolean Query Parameter):

```json
{
  "code": "EIBA0020",
  "message": "Invalid value for boolean query parameter"
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
| 400 | `EIBA0018` | Invalid value for query param 'perPage' |
| 400 | `EIBA0019` | Invalid value for datetime query parameter. RFC3339 format must be used |
| 400 | `EIBA0020` | Invalid value for boolean query parameter |
| 403 | `EIBA0006` | Missing required header: 'x-tenant' |
| 403 | `EIBA0007` | Invalid account ID header: 'x-account-id' |
| 403 | `EIBA0023` | Account status not NORMAL |
| 404 | `EIBA0010` | Account not found |
| 500 | `EIBA0005` | HTTP error |
| 500 | `EIBA0011` | Accounts - API returned 5xx error |
| 500 | `EIBA0013` | Accounts - API timeout |
| 500 | `EIBA0015` | Database internal error |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;403;404;500`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-AUTH-account-and-external-id-tokens`.

<!-- op: spec=api-specs/Banking_-_Bank_accounts.yaml method=POST path=/v1/beneficiaries operationId=post-intl-bank-accounts-v1-bank-accounts-beneficiaries -->
### `POST /v1/beneficiaries` — Register beneficiary

- **operationId:** `post-intl-bank-accounts-v1-bank-accounts-beneficiaries`
- **Specification:** `api-specs/Banking_-_Bank_accounts.yaml` (Banking - Bank accounts)
- **Server base URL(s):** `https://sandbox.pismolabs.io/intl-bankaccounts`
- **Tags:** `Beneficiaries`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Register a new beneficiary with Pismo.
>
> A newly-registerd beneficiary is not initially enabled and must be <a href="https://developers.pismo.io/pismo-docs/reference/post-intl-bank-accounts-v1-bank-accounts-beneficiaries-beneficiary-id-activate">activated</a> before use in transactions.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Account token - Token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a **401 Unauthorized** error. <br> | example: 1234 |

#### Request body

Required: yes

> Register beneficiary request body

**Content type `application/json`** — schema: object (schema `beneficiaries.RegisterBeneficiaryRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `account_code` | string (schema `beneAccountCode`) | yes | Beneficiary account code. | maxLength: 50; example: "7654321" |
| `account_id` | integer (schema `accountID`) | yes | Account ID | example: 78123456 |
| `name` | string (schema `beneName`) | yes | Beneficiary's first and last name. | maxLength: 50; example: "Al Freydough" |
| `region` | string (schema `regionCode`) | yes | ISO-3166 two letter country code. For example, BR=Brazil. | example: "BR" |
| `schema` | string (schema `beneSchema`) | yes | Beneficiary schema validation: <br><br>  `BANKACCOUNT` -  `account_code` contains a Brazilian account number (used in junction with the `bank_code` and `branch` fields)<br><br>  `PIX` - `account_code` contains a valid Pix key. For more information, see <a href="https://developers.pismo.io/pismo-docs/docs/pix-instant-payments" target="_blank">Pix instant payments</a><br><br> `DOCUMENTNUMBER` - `account_code` contains a valid Brazilian document number. This is government document number, such as Cadastro de Pessoas Físicas number - a Brazilian tax registry number, similar to a Social Security number in the US. <br> | enum: ["BANKACCOUNT", "PIX", "DOCUMENTNUMBER"]; example: "PIX" |
| `account_type` | string (schema `brazilAccountType`) | no | Account type:  <br>  `CACC` - Checking/current account. Known as "conta corrente" in Portuguese, this is a bank account type designed for everyday financial transactions and is the most common type individuals and businesses use for day-to-day banking.<br>  `SVGS` - Savings account<br>  `TRAN` - Payment account. Payment institutions offer payment accounts to move funds and make payments, while banks offer checking accounts that include full financial services such as credit and investments.<br>  `SLRY` - Salary account. Employer deposits a fixed amount every month.<br> | enum: ["CACC", "SLRY", "SVGS", "TRAN"]; maxLength: 4; example: "TRAN" |
| `alias` | string (schema `beneAlias`) | no | Beneficiary alias. | maxLength: 20; example: "Curveball" |
| `bank_code` | string (schema `beneBankCode`) | no | Beneficiary bank code. | maxLength: 20; example: "1086" |
| `branch` | string (schema `beneBranch`) | no | Beneficiary branch. | maxLength: 50; example: "5555555" |
| `document_number` | string (schema `beneDocNumber`) | no | A government document number, such as a Social Security number (US) or Cadastro de Pessoas Físicas number (Brazil). <br> | maxLength: 20; example: "123412341234" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | Register beneficiary response body | `application/json`: object (schema `beneficiaries.Beneficiary`) |
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
| `account_code` | string (schema `beneAccountCode`) | no | Beneficiary account code. | maxLength: 50; example: "7654321" |
| `account_id` | integer (schema `accountID`) | no | Account ID | example: 78123456 |
| `account_type` | string (schema `brazilAccountType`) | no | Account type:  <br>  `CACC` - Checking/current account. Known as "conta corrente" in Portuguese, this is a bank account type designed for everyday financial transactions and is the most common type individuals and businesses use for day-to-day banking.<br>  `SVGS` - Savings account<br>  `TRAN` - Payment account. Payment institutions offer payment accounts to move funds and make payments, while banks offer checking accounts that include full financial services such as credit and investments.<br>  `SLRY` - Salary account. Employer deposits a fixed amount every month.<br> | enum: ["CACC", "SLRY", "SVGS", "TRAN"]; maxLength: 4; example: "TRAN" |
| `alias` | string (schema `beneAlias`) | no | Beneficiary alias. | maxLength: 20; example: "Curveball" |
| `bank_code` | string (schema `beneBankCode`) | no | Beneficiary bank code. | maxLength: 20; example: "1086" |
| `beneficiary_id` | string (schema `beneID`) | no | UUID identifying beneficiary. | maxLength: 32; example: "123e4567-e89b-12d3-a456-42661417" |
| `branch` | string (schema `beneBranch`) | no | Beneficiary branch. | maxLength: 50; example: "5555555" |
| `creation_datetime` | string (schema `creationDatetime`) | no | Account creation date time displayed in ISO 8601 format `2023-04-12T23:20:50.52Z`. | format: "date-time"; example: "2023-04-12T23:20:50.52Z" |
| `document_number` | string (schema `beneDocNumber`) | no | A government document number, such as a Social Security number (US) or Cadastro de Pessoas Físicas number (Brazil). <br> | maxLength: 20; example: "123412341234" |
| `enabled` | boolean (schema `beneEnabled`) | no | Is beneficiary active flag. | example: true |
| `name` | string (schema `beneName`) | no | Beneficiary's first and last name. | maxLength: 50; example: "Al Freydough" |
| `region` | string (schema `regionCode`) | no | ISO-3166 two letter country code. For example, BR=Brazil. | example: "BR" |
| `schema` | string (schema `beneSchema`) | no | Beneficiary schema validation: <br><br>  `BANKACCOUNT` -  `account_code` contains a Brazilian account number (used in junction with the `bank_code` and `branch` fields)<br><br>  `PIX` - `account_code` contains a valid Pix key. For more information, see <a href="https://developers.pismo.io/pismo-docs/docs/pix-instant-payments" target="_blank">Pix instant payments</a><br><br> `DOCUMENTNUMBER` - `account_code` contains a valid Brazilian document number. This is government document number, such as Cadastro de Pessoas Físicas number - a Brazilian tax registry number, similar to a Social Security number in the US. <br> | enum: ["BANKACCOUNT", "PIX", "DOCUMENTNUMBER"]; example: "PIX" |
| `updated_datetime` | string (schema `updatedDatetime`) | no | Updated date time. A RFC 3339 value, i.e., "2023-04-12T23:20:50.52Z". | format: "date-time"; example: "2023-04-12T23:20:50.52Z" |

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

##### Response 409

- Response header `x-cid`: Request tracking identifier. (string)
409 Example `EIBA0017` (Beneficiary Already Exists):

```json
{
  "code": "EIBA0017",
  "message": "Beneficiary - Already Exists"
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
| 400 | `EIBA0016` | Account ID in header does not match account ID in request body |
| 403 | `EIBA0006` | Missing required header: 'x-tenant' |
| 403 | `EIBA0007` | Invalid account ID header: 'x-account-id' |
| 403 | `EIBA0023` | Account status not NORMAL |
| 404 | `EIBA0010` | Account not found |
| 409 | `EIBA0017` | Beneficiary - Already Exists |
| 500 | `EIBA0005` | HTTP error |
| 500 | `EIBA0011` | Accounts - API returned 5xx error |
| 500 | `EIBA0013` | Accounts - API timeout |
| 500 | `EIBA0015` | Database internal error |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `201;400;403;404;409;500`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-AUTH-account-and-external-id-tokens`.

<!-- op: spec=api-specs/Banking_-_Bank_accounts.yaml method=POST path=/v1/beneficiaries/{beneficiaryId}/activate operationId=post-intl-bank-accounts-v1-bank-accounts-beneficiaries-beneficiary-id-activate -->
### `POST /v1/beneficiaries/{beneficiaryId}/activate` — Activate beneficiary

- **operationId:** `post-intl-bank-accounts-v1-bank-accounts-beneficiaries-beneficiary-id-activate`
- **Specification:** `api-specs/Banking_-_Bank_accounts.yaml` (Banking - Bank accounts)
- **Server base URL(s):** `https://sandbox.pismolabs.io/intl-bankaccounts`
- **Tags:** `Beneficiaries`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Activate a beneficiary. 
>
> Activating a beneficiary authorizes or confirms a particular individual, organization, or account can receive frunds from another account. This is usually required before initiating transactions, especially fund transfers, to ensure that the recipient is approved to receive money.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Account token - Token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a **401 Unauthorized** error. <br> | example: 1234 |
| `beneficiaryId` | path | yes | string | Beneficiary identifier (UUID). This field is returned from the <a href="https://developers.pismo.io/pismo-docs/reference/post-intl-bank-accounts-v1-bank-accounts-beneficiaries">Register beneficiary</a> endpoint.<br> | example: 3456 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Response Body | `application/json`: object (schema `beneficiaries.Beneficiary`) |
| 400 | Bad Request | `application/json`: object (schema `domain.Error`) |
| 403 | Forbidden | `application/json`: object (schema `domain.Error`) |
| 404 | Not Found | `application/json`: object (schema `domain.Error`) |
| 500 | Internal Server Error | `application/json`: object (schema `domain.Error`) |

##### Response 200

- Response header `x-cid`: Request tracking identifier. (string)
**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `account_code` | string (schema `beneAccountCode`) | no | Beneficiary account code. | maxLength: 50; example: "7654321" |
| `account_id` | integer (schema `accountID`) | no | Account ID | example: 78123456 |
| `account_type` | string (schema `brazilAccountType`) | no | Account type:  <br>  `CACC` - Checking/current account. Known as "conta corrente" in Portuguese, this is a bank account type designed for everyday financial transactions and is the most common type individuals and businesses use for day-to-day banking.<br>  `SVGS` - Savings account<br>  `TRAN` - Payment account. Payment institutions offer payment accounts to move funds and make payments, while banks offer checking accounts that include full financial services such as credit and investments.<br>  `SLRY` - Salary account. Employer deposits a fixed amount every month.<br> | enum: ["CACC", "SLRY", "SVGS", "TRAN"]; maxLength: 4; example: "TRAN" |
| `alias` | string (schema `beneAlias`) | no | Beneficiary alias. | maxLength: 20; example: "Curveball" |
| `bank_code` | string (schema `beneBankCode`) | no | Beneficiary bank code. | maxLength: 20; example: "1086" |
| `beneficiary_id` | string (schema `beneID`) | no | UUID identifying beneficiary. | maxLength: 32; example: "123e4567-e89b-12d3-a456-42661417" |
| `branch` | string (schema `beneBranch`) | no | Beneficiary branch. | maxLength: 50; example: "5555555" |
| `creation_datetime` | string (schema `creationDatetime`) | no | Account creation date time displayed in ISO 8601 format `2023-04-12T23:20:50.52Z`. | format: "date-time"; example: "2023-04-12T23:20:50.52Z" |
| `document_number` | string (schema `beneDocNumber`) | no | A government document number, such as a Social Security number (US) or Cadastro de Pessoas Físicas number (Brazil). <br> | maxLength: 20; example: "123412341234" |
| `enabled` | boolean (schema `beneEnabled`) | no | Is beneficiary active flag. | example: true |
| `name` | string (schema `beneName`) | no | Beneficiary's first and last name. | maxLength: 50; example: "Al Freydough" |
| `region` | string (schema `regionCode`) | no | ISO-3166 two letter country code. For example, BR=Brazil. | example: "BR" |
| `schema` | string (schema `beneSchema`) | no | Beneficiary schema validation: <br><br>  `BANKACCOUNT` -  `account_code` contains a Brazilian account number (used in junction with the `bank_code` and `branch` fields)<br><br>  `PIX` - `account_code` contains a valid Pix key. For more information, see <a href="https://developers.pismo.io/pismo-docs/docs/pix-instant-payments" target="_blank">Pix instant payments</a><br><br> `DOCUMENTNUMBER` - `account_code` contains a valid Brazilian document number. This is government document number, such as Cadastro de Pessoas Físicas number - a Brazilian tax registry number, similar to a Social Security number in the US. <br> | enum: ["BANKACCOUNT", "PIX", "DOCUMENTNUMBER"]; example: "PIX" |
| `updated_datetime` | string (schema `updatedDatetime`) | no | Updated date time. A RFC 3339 value, i.e., "2023-04-12T23:20:50.52Z". | format: "date-time"; example: "2023-04-12T23:20:50.52Z" |

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

400 Example `EIBA0021` (Invalid UUID Path Parameter):

```json
{
  "code": "EIBA0021",
  "message": "Invalid value for UUID path parameter"
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

404 Example `EIBA0022` (Beneficiary Not Found):

```json
{
  "code": "EIBA0022",
  "message": "Beneficiary not found"
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
| 400 | `EIBA0021` | Invalid value for UUID path parameter |
| 403 | `EIBA0006` | Missing required header: 'x-tenant' |
| 403 | `EIBA0007` | Invalid account ID header: 'x-account-id' |
| 403 | `EIBA0023` | Account status not NORMAL |
| 404 | `EIBA0010` | Account not found |
| 404 | `EIBA0022` | Beneficiary not found |
| 500 | `EIBA0005` | HTTP error |
| 500 | `EIBA0011` | Accounts - API returned 5xx error |
| 500 | `EIBA0013` | Accounts - API timeout |
| 500 | `EIBA0015` | Database internal error |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;403;404;500`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-AUTH-account-and-external-id-tokens`.

<!-- op: spec=api-specs/Banking_-_Bank_accounts.yaml method=GET path=/v1/beneficiaries/{beneficiaryId} operationId=get-intl-bank-accounts-v1-bank-accounts-beneficiaries-beneficiary-id -->
### `GET /v1/beneficiaries/{beneficiaryId}` — Get beneficiary

- **operationId:** `get-intl-bank-accounts-v1-bank-accounts-beneficiaries-beneficiary-id`
- **Specification:** `api-specs/Banking_-_Bank_accounts.yaml` (Banking - Bank accounts)
- **Server base URL(s):** `https://sandbox.pismolabs.io/intl-bankaccounts`
- **Tags:** `Beneficiaries`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Get a beneficiary's information given its ID in the path.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Account token - Token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a **401 Unauthorized** error. <br> | example: 1234 |
| `beneficiaryId` | path | yes | string | Beneficiary identifier (UUID). This field is returned from the <a href="https://developers.pismo.io/pismo-docs/reference/post-intl-bank-accounts-v1-bank-accounts-beneficiaries">Register beneficiary</a> endpoint.<br> | example: 3456 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Get beneficiary response body | `application/json`: object (schema `beneficiaries.Beneficiary`) |
| 400 | Bad Request | `application/json`: object (schema `domain.Error`) |
| 403 | Forbidden | `application/json`: object (schema `domain.Error`) |
| 404 | Not Found | `application/json`: object (schema `domain.Error`) |
| 500 | Internal Server | `application/json`: object (schema `domain.Error`) |

##### Response 200

- Response header `x-cid`: Request tracking identifier. (string)
**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `account_code` | string (schema `beneAccountCode`) | no | Beneficiary account code. | maxLength: 50; example: "7654321" |
| `account_id` | integer (schema `accountID`) | no | Account ID | example: 78123456 |
| `account_type` | string (schema `brazilAccountType`) | no | Account type:  <br>  `CACC` - Checking/current account. Known as "conta corrente" in Portuguese, this is a bank account type designed for everyday financial transactions and is the most common type individuals and businesses use for day-to-day banking.<br>  `SVGS` - Savings account<br>  `TRAN` - Payment account. Payment institutions offer payment accounts to move funds and make payments, while banks offer checking accounts that include full financial services such as credit and investments.<br>  `SLRY` - Salary account. Employer deposits a fixed amount every month.<br> | enum: ["CACC", "SLRY", "SVGS", "TRAN"]; maxLength: 4; example: "TRAN" |
| `alias` | string (schema `beneAlias`) | no | Beneficiary alias. | maxLength: 20; example: "Curveball" |
| `bank_code` | string (schema `beneBankCode`) | no | Beneficiary bank code. | maxLength: 20; example: "1086" |
| `beneficiary_id` | string (schema `beneID`) | no | UUID identifying beneficiary. | maxLength: 32; example: "123e4567-e89b-12d3-a456-42661417" |
| `branch` | string (schema `beneBranch`) | no | Beneficiary branch. | maxLength: 50; example: "5555555" |
| `creation_datetime` | string (schema `creationDatetime`) | no | Account creation date time displayed in ISO 8601 format `2023-04-12T23:20:50.52Z`. | format: "date-time"; example: "2023-04-12T23:20:50.52Z" |
| `document_number` | string (schema `beneDocNumber`) | no | A government document number, such as a Social Security number (US) or Cadastro de Pessoas Físicas number (Brazil). <br> | maxLength: 20; example: "123412341234" |
| `enabled` | boolean (schema `beneEnabled`) | no | Is beneficiary active flag. | example: true |
| `name` | string (schema `beneName`) | no | Beneficiary's first and last name. | maxLength: 50; example: "Al Freydough" |
| `region` | string (schema `regionCode`) | no | ISO-3166 two letter country code. For example, BR=Brazil. | example: "BR" |
| `schema` | string (schema `beneSchema`) | no | Beneficiary schema validation: <br><br>  `BANKACCOUNT` -  `account_code` contains a Brazilian account number (used in junction with the `bank_code` and `branch` fields)<br><br>  `PIX` - `account_code` contains a valid Pix key. For more information, see <a href="https://developers.pismo.io/pismo-docs/docs/pix-instant-payments" target="_blank">Pix instant payments</a><br><br> `DOCUMENTNUMBER` - `account_code` contains a valid Brazilian document number. This is government document number, such as Cadastro de Pessoas Físicas number - a Brazilian tax registry number, similar to a Social Security number in the US. <br> | enum: ["BANKACCOUNT", "PIX", "DOCUMENTNUMBER"]; example: "PIX" |
| `updated_datetime` | string (schema `updatedDatetime`) | no | Updated date time. A RFC 3339 value, i.e., "2023-04-12T23:20:50.52Z". | format: "date-time"; example: "2023-04-12T23:20:50.52Z" |

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

400 Example `EIBA0021` (Invalid UUID Path Parameter):

```json
{
  "code": "EIBA0021",
  "message": "Invalid value for UUID path parameter"
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

404 Example `EIBA0022` (Beneficiary Not Found):

```json
{
  "code": "EIBA0022",
  "message": "Beneficiary not found"
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
| 400 | `EIBA0021` | Invalid value for UUID path parameter |
| 403 | `EIBA0006` | Missing required header: 'x-tenant' |
| 403 | `EIBA0007` | Invalid account ID header: 'x-account-id' |
| 403 | `EIBA0023` | Account status not NORMAL |
| 404 | `EIBA0010` | Account not found |
| 404 | `EIBA0022` | Beneficiary not found |
| 500 | `EIBA0005` | HTTP error |
| 500 | `EIBA0011` | Accounts - API returned 5xx error |
| 500 | `EIBA0013` | Accounts - API timeout |
| 500 | `EIBA0015` | Database internal error |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;403;404;500`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-AUTH-account-and-external-id-tokens`.

<!-- op: spec=api-specs/Banking_-_Bank_accounts.yaml method=DELETE path=/v1/beneficiaries/{beneficiaryId} operationId=delete-intl-bank-accounts-v1-beneficiaries-beneficiary-id -->
### `DELETE /v1/beneficiaries/{beneficiaryId}` — Delete beneficiary

- **operationId:** `delete-intl-bank-accounts-v1-beneficiaries-beneficiary-id`
- **Specification:** `api-specs/Banking_-_Bank_accounts.yaml` (Banking - Bank accounts)
- **Server base URL(s):** `https://sandbox.pismolabs.io/intl-bankaccounts`
- **Tags:** `Beneficiaries`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Delete a beneficiary given its ID in the path.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Account token - Token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a **401 Unauthorized** error. <br> | example: 1234 |
| `beneficiaryId` | path | yes | string | Beneficiary identifier (UUID). This field is returned from the <a href="https://developers.pismo.io/pismo-docs/reference/post-intl-bank-accounts-v1-bank-accounts-beneficiaries">Register beneficiary</a> endpoint.<br> | example: 3456 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 204 | No Content |  |
| 400 | Bad Request | `application/json`: object (schema `domain.Error`) |
| 403 | Forbidden | `application/json`: object (schema `domain.Error`) |
| 404 | Not Found | `application/json`: object (schema `domain.Error`) |
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

400 Example `EIBA0021` (Invalid UUID Path Parameter):

```json
{
  "code": "EIBA0021",
  "message": "Invalid value for UUID path parameter"
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

404 Example `EIBA0022` (Beneficiary Not Found):

```json
{
  "code": "EIBA0022",
  "message": "Beneficiary not found"
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
| 400 | `EIBA0021` | Invalid value for UUID path parameter |
| 403 | `EIBA0006` | Missing required header: 'x-tenant' |
| 403 | `EIBA0007` | Invalid account ID header: 'x-account-id' |
| 403 | `EIBA0023` | Account status not NORMAL |
| 404 | `EIBA0010` | Account not found |
| 404 | `EIBA0022` | Beneficiary not found |
| 500 | `EIBA0005` | HTTP error |
| 500 | `EIBA0011` | Accounts - API returned 5xx error |
| 500 | `EIBA0013` | Accounts - API timeout |
| 500 | `EIBA0015` | Database internal error |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `204;400;403;404;500`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-AUTH-account-and-external-id-tokens`.

<!-- op: spec=api-specs/Banking_-_Bank_accounts.yaml method=PATCH path=/v1/beneficiaries/{beneficiaryId} operationId=patch-intl-bank-accounts-v1-beneficiaries-beneficiary-id -->
### `PATCH /v1/beneficiaries/{beneficiaryId}` — Update beneficiary

- **operationId:** `patch-intl-bank-accounts-v1-beneficiaries-beneficiary-id`
- **Specification:** `api-specs/Banking_-_Bank_accounts.yaml` (Banking - Bank accounts)
- **Server base URL(s):** `https://sandbox.pismolabs.io/intl-bankaccounts`
- **Tags:** `Beneficiaries`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Update a beneficiary given its ID in the path.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Account token - Token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a **401 Unauthorized** error. <br> | example: 1234 |
| `beneficiaryId` | path | yes | string | Beneficiary identifier (UUID). This field is returned from the <a href="https://developers.pismo.io/pismo-docs/reference/post-intl-bank-accounts-v1-bank-accounts-beneficiaries">Register beneficiary</a> endpoint.<br> | example: 3456 |

#### Request body

Required: yes

> Request Body

**Content type `application/json`** — schema: object (schema `beneficiaries.UpdateBeneficiaryRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `alias` | string (schema `beneAlias`) | no | Beneficiary alias. | maxLength: 20; example: "Curveball" |
| `name` | string (schema `beneName`) | no | Beneficiary's first and last name. | maxLength: 50; example: "Al Freydough" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Response | `application/json`: object (schema `beneficiaries.Beneficiary`) |
| 400 | Bad | `application/json`: object (schema `domain.Error`) |
| 403 | Forbidden | `application/json`: object (schema `domain.Error`) |
| 404 | Not Found | `application/json`: object (schema `domain.Error`) |
| 500 | Internal Server Error | `application/json`: object (schema `domain.Error`) |

##### Response 200

- Response header `x-cid`: Request tracking identifier. (string)
**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `account_code` | string (schema `beneAccountCode`) | no | Beneficiary account code. | maxLength: 50; example: "7654321" |
| `account_id` | integer (schema `accountID`) | no | Account ID | example: 78123456 |
| `account_type` | string (schema `brazilAccountType`) | no | Account type:  <br>  `CACC` - Checking/current account. Known as "conta corrente" in Portuguese, this is a bank account type designed for everyday financial transactions and is the most common type individuals and businesses use for day-to-day banking.<br>  `SVGS` - Savings account<br>  `TRAN` - Payment account. Payment institutions offer payment accounts to move funds and make payments, while banks offer checking accounts that include full financial services such as credit and investments.<br>  `SLRY` - Salary account. Employer deposits a fixed amount every month.<br> | enum: ["CACC", "SLRY", "SVGS", "TRAN"]; maxLength: 4; example: "TRAN" |
| `alias` | string (schema `beneAlias`) | no | Beneficiary alias. | maxLength: 20; example: "Curveball" |
| `bank_code` | string (schema `beneBankCode`) | no | Beneficiary bank code. | maxLength: 20; example: "1086" |
| `beneficiary_id` | string (schema `beneID`) | no | UUID identifying beneficiary. | maxLength: 32; example: "123e4567-e89b-12d3-a456-42661417" |
| `branch` | string (schema `beneBranch`) | no | Beneficiary branch. | maxLength: 50; example: "5555555" |
| `creation_datetime` | string (schema `creationDatetime`) | no | Account creation date time displayed in ISO 8601 format `2023-04-12T23:20:50.52Z`. | format: "date-time"; example: "2023-04-12T23:20:50.52Z" |
| `document_number` | string (schema `beneDocNumber`) | no | A government document number, such as a Social Security number (US) or Cadastro de Pessoas Físicas number (Brazil). <br> | maxLength: 20; example: "123412341234" |
| `enabled` | boolean (schema `beneEnabled`) | no | Is beneficiary active flag. | example: true |
| `name` | string (schema `beneName`) | no | Beneficiary's first and last name. | maxLength: 50; example: "Al Freydough" |
| `region` | string (schema `regionCode`) | no | ISO-3166 two letter country code. For example, BR=Brazil. | example: "BR" |
| `schema` | string (schema `beneSchema`) | no | Beneficiary schema validation: <br><br>  `BANKACCOUNT` -  `account_code` contains a Brazilian account number (used in junction with the `bank_code` and `branch` fields)<br><br>  `PIX` - `account_code` contains a valid Pix key. For more information, see <a href="https://developers.pismo.io/pismo-docs/docs/pix-instant-payments" target="_blank">Pix instant payments</a><br><br> `DOCUMENTNUMBER` - `account_code` contains a valid Brazilian document number. This is government document number, such as Cadastro de Pessoas Físicas number - a Brazilian tax registry number, similar to a Social Security number in the US. <br> | enum: ["BANKACCOUNT", "PIX", "DOCUMENTNUMBER"]; example: "PIX" |
| `updated_datetime` | string (schema `updatedDatetime`) | no | Updated date time. A RFC 3339 value, i.e., "2023-04-12T23:20:50.52Z". | format: "date-time"; example: "2023-04-12T23:20:50.52Z" |

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

400 Example `EIBA0016` (Account ID mismatch):

```json
{
  "code": "EIBA0016",
  "message": "Account ID in header does not match account ID in request body"
}
```

400 Example `EIBA0021` (Invalid UUID Path Parameter):

```json
{
  "code": "EIBA0021",
  "message": "Invalid value for UUID path parameter"
}
```

400 Example `EIBA0024` (No Updatable Fields):

```json
{
  "code": "EIBA0024",
  "message": "Request body contains no fields that can be updated"
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

404 Example `EIBA0022` (beneficiary Not Found):

```json
{
  "code": "EIBA0022",
  "message": "Beneficiary not found"
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
| 400 | `EIBA0016` | Account ID in header does not match account ID in request body |
| 400 | `EIBA0021` | Invalid value for UUID path parameter |
| 400 | `EIBA0024` | Request body contains no fields that can be updated |
| 403 | `EIBA0006` | Missing required header: 'x-tenant' |
| 403 | `EIBA0007` | Invalid account ID header: 'x-account-id' |
| 403 | `EIBA0023` | Account status not NORMAL |
| 404 | `EIBA0010` | Account not found |
| 404 | `EIBA0022` | Beneficiary not found |
| 500 | `EIBA0005` | HTTP error |
| 500 | `EIBA0011` | Accounts - API returned 5xx error |
| 500 | `EIBA0013` | Accounts - API timeout |
| 500 | `EIBA0015` | Database internal error |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;403;404;500`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-AUTH-account-and-external-id-tokens`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/beneficiaries.Beneficiary -->
### Schema `beneficiaries.Beneficiary`

Pointer: `#/components/schemas/beneficiaries.Beneficiary`. Type: object (schema `beneficiaries.Beneficiary`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `account_code` | string (schema `beneAccountCode`) | no | Beneficiary account code. | maxLength: 50; example: "7654321" |
| `account_id` | integer (schema `accountID`) | no | Account ID | example: 78123456 |
| `account_type` | string (schema `brazilAccountType`) | no | Account type:  <br>  `CACC` - Checking/current account. Known as "conta corrente" in Portuguese, this is a bank account type designed for everyday financial transactions and is the most common type individuals and businesses use for day-to-day banking.<br>  `SVGS` - Savings account<br>  `TRAN` - Payment account. Payment institutions offer payment accounts to move funds and make payments, while banks offer checking accounts that include full financial services such as credit and investments.<br>  `SLRY` - Salary account. Employer deposits a fixed amount every month.<br> | enum: ["CACC", "SLRY", "SVGS", "TRAN"]; maxLength: 4; example: "TRAN" |
| `alias` | string (schema `beneAlias`) | no | Beneficiary alias. | maxLength: 20; example: "Curveball" |
| `bank_code` | string (schema `beneBankCode`) | no | Beneficiary bank code. | maxLength: 20; example: "1086" |
| `beneficiary_id` | string (schema `beneID`) | no | UUID identifying beneficiary. | maxLength: 32; example: "123e4567-e89b-12d3-a456-42661417" |
| `branch` | string (schema `beneBranch`) | no | Beneficiary branch. | maxLength: 50; example: "5555555" |
| `creation_datetime` | string (schema `creationDatetime`) | no | Account creation date time displayed in ISO 8601 format `2023-04-12T23:20:50.52Z`. | format: "date-time"; example: "2023-04-12T23:20:50.52Z" |
| `document_number` | string (schema `beneDocNumber`) | no | A government document number, such as a Social Security number (US) or Cadastro de Pessoas Físicas number (Brazil). <br> | maxLength: 20; example: "123412341234" |
| `enabled` | boolean (schema `beneEnabled`) | no | Is beneficiary active flag. | example: true |
| `name` | string (schema `beneName`) | no | Beneficiary's first and last name. | maxLength: 50; example: "Al Freydough" |
| `region` | string (schema `regionCode`) | no | ISO-3166 two letter country code. For example, BR=Brazil. | example: "BR" |
| `schema` | string (schema `beneSchema`) | no | Beneficiary schema validation: <br><br>  `BANKACCOUNT` -  `account_code` contains a Brazilian account number (used in junction with the `bank_code` and `branch` fields)<br><br>  `PIX` - `account_code` contains a valid Pix key. For more information, see <a href="https://developers.pismo.io/pismo-docs/docs/pix-instant-payments" target="_blank">Pix instant payments</a><br><br> `DOCUMENTNUMBER` - `account_code` contains a valid Brazilian document number. This is government document number, such as Cadastro de Pessoas Físicas number - a Brazilian tax registry number, similar to a Social Security number in the US. <br> | enum: ["BANKACCOUNT", "PIX", "DOCUMENTNUMBER"]; example: "PIX" |
| `updated_datetime` | string (schema `updatedDatetime`) | no | Updated date time. A RFC 3339 value, i.e., "2023-04-12T23:20:50.52Z". | format: "date-time"; example: "2023-04-12T23:20:50.52Z" |

<!-- schema: #/components/schemas/domain.Error -->
### Schema `domain.Error`

Pointer: `#/components/schemas/domain.Error`. Type: object (schema `domain.Error`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string | no | Error type code | example: "EIBA0001" |
| `details` | string | no | Error details | example: "Key not found" |
| `message` | string | no | Error message | example: "Key not found" |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Banking_-_Bank_accounts.yaml` | tag `Beneficiaries`: GET /v1/beneficiaries, POST /v1/beneficiaries, POST /v1/beneficiaries/{beneficiaryId}/activate, GET /v1/beneficiaries/{beneficiaryId}, DELETE /v1/beneficiaries/{beneficiaryId}, PATCH /v1/beneficiaries/{beneficiaryId} | https://github.com/PismoDevEx/pismo-api-specs | `6245dc46ddfee395…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-AUTH-account-and-external-id-tokens` — Endpoints that require account-specific or external-ID tokens
- `KU-ERR-codes-eiba` — Error codes: EIBA
