---
ku_id: KU-API-banking-integrated-payments--bank-slip-issuance
title: 'API reference: Banking - Integrated payments — Bank slip issuance'
category: api_reference
ku_type: api_reference
lifecycle: current
sources:
- path: api-specs/Banking_-_Integrated_payments.yaml
  sha256: 8696ddecc6a5182f219956d7bbba779e4dfa8c9d4b356ef282e9e96c407d1716
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
- get-integrated-payments-api-v1-bankslips-issue
- post-integrated-payments-api-v1-bankslips-issue
- get-integrated-payments-api-v1-bankslips-issue-retrieve
- delete-integrated-payments-api-v1-bankslips-issue
related_kus:
- KU-AUTH-account-and-external-id-tokens
- KU-BANK-banking-overview
- KU-ERR-codes-eip
- KU-EVT-catalogue-integrated
- KU-PAY-bank-slips
specification_version: '1.0'
---

# API reference: Banking - Integrated payments — Bank slip issuance

**KU ID:** `KU-API-banking-integrated-payments--bank-slip-issuance` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 4 operation(s) tagged `Bank slip issuance` in `api-specs/Banking_-_Integrated_payments.yaml` (“Banking - Integrated payments”, version `1.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Operations related to issue and cancel issued bank slips

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `GET /v1/bankslips-issue` | `get-integrated-payments-api-v1-bankslips-issue` | List issued bank slips | no |
| `POST /v1/bankslips-issue` | `post-integrated-payments-api-v1-bankslips-issue` | Issue bank slip | no |
| `GET /v1/bankslips-issue/client-requests/{clientRequestId}` | `get-integrated-payments-api-v1-bankslips-issue-retrieve` | Get issued bank slip | no |
| `DELETE /v1/bankslips-issue/client-requests/{clientRequestId}` | `delete-integrated-payments-api-v1-bankslips-issue` | Delete issued bank slip | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"}

## Operation contracts

<!-- op: spec=api-specs/Banking_-_Integrated_payments.yaml method=GET path=/v1/bankslips-issue operationId=get-integrated-payments-api-v1-bankslips-issue -->
### `GET /v1/bankslips-issue` — List issued bank slips

- **operationId:** `get-integrated-payments-api-v1-bankslips-issue`
- **Specification:** `api-specs/Banking_-_Integrated_payments.yaml` (Banking - Integrated payments)
- **Server base URL(s):** `https://sandbox.pismolabs.io/integrated-payments`
- **Tags:** `Bank slip issuance`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Retrieve a list of issued bank slips.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `perPage` | query | no | string | Receipts per page. Min=1, max=100, default=20. | default: "20"; minLength: 1; maxLength: 100; example: "100" |
| `page` | query | no | string | Current page. min=1 default=1 | default: "1"; minLength: 1; example: "1" |
| `order` | query | no | string | Result ordering is done on bank slip creation datetime. Default is `desc`. | enum: ["asc", "desc"]; example: "desc" |
| `beginDatetime` | query | no | string | Begin datetime filter. ISO 8601 format - `yyyy-MM-ddTHH:mm:ss.SSSSSSSSSZ`.<br> | format: "datetime"; example: "2024-09-11T18:01:44Z" |
| `endDatetime` | query | no | string | End datetime filter. ISO 8601 format - `syyyy-MM-ddTHH:mm:ss.SSSSSSSSSZ`.<br> | format: "datetime"; example: "2024-09-11T18:01:44.000Z" |
| `status` | query | no | string | Status of issued bank slip. | example: "REGISTERED" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Response Body | `application/json`: object (schema `bankslips_issue.ListIssueResponse`) |
| 400 | Bad Request | `application/json`: object (schema `domain.Error`) |
| 403 | Forbidden | `application/json`: object (schema `domain.Error`) |
| 500 | Internal Server Error | `application/json`: object (schema `domain.Error`) |

##### Response 200

- Response header `x-cid`: Request tracking identifier. (string)
**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `items` | array of object (schema `bankslips_issue.ListIssueItem`) | no |  |  |
| `pagination` | object (schema `bankslips_issue.OffsetPagination`) | no |  |  |

##### Response 400

- Response header `x-cid`: Request tracking identifier. (string)
400 Example `EIP0045` (Invalid per_page query param):

```json
{
  "code": "EIP0045",
  "message": "Invalid value for query param 'per_page'"
}
```

400 Example `EIP0046` (Invalid datetime query param):

```json
{
  "code": "EIP0046",
  "message": "Invalid value for datetime query parameter. RFC3339 format must be used"
}
```

400 Example `EIP0066` (Invalid status query param):

```json
{
  "code": "EIP0066",
  "message": "Invalid query param status"
}
```

400 Example `EIP0012` (Account not found):

```json
{
  "code": "EIP0012",
  "message": "Account not found"
}
```

400 Example `EIP0013` (Accounts - API returned 4xx error):

```json
{
  "code": "EIP0013",
  "message": "Accounts - API returned 4xx error"
}
```

400 Example `EIP0067` (Invalid page query param):

```json
{
  "code": "EIP0067",
  "message": "Invalid query param page"
}
```

##### Response 403

- Response header `x-cid`: Request tracking identifier. (string)
403 Example `EIP0005` (Missing required header x-tenant):

```json
{
  "code": "EIP0005",
  "message": "Missing required header: 'x-tenant'"
}
```

403 Example `EIP0006` (Invalid account ID header x-account-id):

```json
{
  "code": "EIP0006",
  "message": "Invalid account id header: 'x-account-id'"
}
```

403 Example `EIP0029` (Account blocked or cancelled):

```json
{
  "code": "EIP0029",
  "message": "Account blocked or cancelled"
}
```

##### Response 500

- Response header `x-cid`: Request tracking identifier. (string)
500 Example `EIP0007` (Internal error):

```json
{
  "code": "EIP0007",
  "message": "Internal error"
}
```

500 Example `EIP0011` (Accounts API timeout error):

```json
{
  "code": "EIP0011",
  "message": "Accounts API timeout error"
}
```

500 Example `EIP0014` (Accounts - API returned 5xx error):

```json
{
  "code": "EIP0014",
  "message": "Accounts - API returned 5xx error"
}
```

500 Example `EIP0074` (Bankslip issue database error):

```json
{
  "code": "EIP0074",
  "message": "Bankslip issue database error"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `EIP0045` | Invalid value for query param 'per_page' |
| 400 | `EIP0046` | Invalid value for datetime query parameter. RFC3339 format must be used |
| 400 | `EIP0066` | Invalid query param status |
| 400 | `EIP0012` | Account not found |
| 400 | `EIP0013` | Accounts - API returned 4xx error |
| 400 | `EIP0067` | Invalid query param page |
| 403 | `EIP0005` | Missing required header: 'x-tenant' |
| 403 | `EIP0006` | Invalid account id header: 'x-account-id' |
| 403 | `EIP0029` | Account blocked or cancelled |
| 500 | `EIP0007` | Internal error |
| 500 | `EIP0011` | Accounts API timeout error |
| 500 | `EIP0014` | Accounts - API returned 5xx error |
| 500 | `EIP0074` | Bankslip issue database error |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;403;500`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-AUTH-account-and-external-id-tokens`.

<!-- op: spec=api-specs/Banking_-_Integrated_payments.yaml method=POST path=/v1/bankslips-issue operationId=post-integrated-payments-api-v1-bankslips-issue -->
### `POST /v1/bankslips-issue` — Issue bank slip

- **operationId:** `post-integrated-payments-api-v1-bankslips-issue`
- **Specification:** `api-specs/Banking_-_Integrated_payments.yaml` (Banking - Integrated payments)
- **Server base URL(s):** `https://sandbox.pismolabs.io/integrated-payments`
- **Tags:** `Bank slip issuance`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Create a bank slip and issue it to the provider. See [Bank slips](doc:bank-slips) for more information.<br>
> This endpoint generates the [Bank slip issuance registered](https://developers.pismo.io/events/docs/integrated-payments-bankslip-issue-register-1) event.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `x-idempotency-key` | header | yes | string | Unique identifier (UUID) to ensure the operation remains idempotent, allowing for operation repitition without causing unintended effects or duplication. An idempotent operation is one that can be applied multiple times, yet the outcome remains the same. it ensures that network errors, retries, or failures can occur without introducing inconsistencies.<br> | example: "6a17f82d-7365-4451-a83d-09403f05c1ec" |

#### Request body

Required: yes

> Request Body

**Content type `application/json`** — schema: object (schema `bankslips_issue.IssueRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `amount` | number | yes | bank slip amount. | example: 100 |
| `due_date` | string | yes | bank slip payment due date. | format: "date"; example: "2024-07-25T00:00:00.000Z" |
| `debtor` | object (schema `bankslips_issue.IssueDebtor`) | no |  |  |
| `description` | string | no | Description about the bank slip. | example: "Long description." |
| `instructions` | object (schema `bankslips_issue.IssueInstructions`) | no |  |  |
| `maximum_amount` | number | no | Maximum amount accepted when paying the bank slip. | example: 100 |
| `minimum_amount` | number | no | Minimum amount accepted when paying the bank slip. | example: 10 |
| `over_due_date` | string | no | Last day to accept bank slip payments. After this date, the bank slip is not paid. | format: "date"; example: "2024-08-25T00:00:00.000Z" |
| `pix_key` | string | no | PIX key related to the bank slip. | example: "pixkey@pix.com.br" |
| `issuer` | string | no | The name of the provider that issues the bank slip. | example: "PISMO" |
| `transaction_id` | string | no | Transaction ID related to the bank slip issue. This is the ID that links the bank slip to the specific transaction performed in the payments API. It can be used for tracking, reconciliation, and reference purposes when managing bank slips and their associated transactions. | example: "550e8400-e29b-41d4-a716-446655440000" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 202 | Accepted | `application/json`: object (schema `bankslips_issue.IssueResponse`) |
| 400 | Bad Request | `application/json`: object (schema `domain.Error`) |
| 403 | Forbidden | `application/json`: object (schema `domain.Error`) |
| 409 | Conflict | `application/json`: object (schema `domain.Error`) |
| 500 | Internal Server Error | `application/json`: object (schema `domain.Error`) |
| 502 | Bad Gateway | `application/json`: object (schema `domain.Error`) |

##### Response 202

- Response header `x-cid`: Request tracking ID. (string)
**202 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `client_request_id` | string | no | Unique identifier of the request controlled by the client. | example: "6d6bdd2c-9980-4cf1-87ff-c99dc9ce6ef4456" |
| `external_id` | string | no | Unique identifier of the request controlled by the provider. | example: "6d6bdd2c-9980-4cf1-87ff-c99dc9ce6ef4123" |
| `status` | string | no | bank slip status. Possible values are `CREATED`, `CANCELLED`, `REGISTERED`, and `ERROR`. | example: "CREATED" |

##### Response 400

- Response header `x-cid`: Request tracking ID. (string)
400 Example `EIP0010` (Unmarshal error):

```json
{
  "code": "EIP0010",
  "message": "Unmarshal error"
}
```

400 Example `EIP0012` (Account not found):

```json
{
  "code": "EIP0012",
  "message": "Account not found"
}
```

400 Example `EIP0013` (Accounts - API returned 4xx error):

```json
{
  "code": "EIP0013",
  "message": "Accounts - API returned 4xx error"
}
```

400 Example `EIP0016` (IntlBankAccounts - API Account not found):

```json
{
  "code": "EIP0016",
  "message": "IntlBankAccounts - API Account not found"
}
```

400 Example `EIP0017` (IntlBankAccounts - API returned 4xx error):

```json
{
  "code": "EIP0017",
  "message": "IntlBankAccounts - API returned 4xx error"
}
```

400 Example `EIP0023` (BankingGatewayAPI - API returned 4xx error):

```json
{
  "code": "EIP0023",
  "message": "BankingGatewayAPI - API returned 4xx error"
}
```

400 Example `EIP0077` (Address not found for this Account):

```json
{
  "code": "EIP0077",
  "message": "Address not found for this Account"
}
```

##### Response 403

- Response header `x-cid`: Request tracking ID. (string)
403 Example `EIP0005` (Missing required header x-tenant):

```json
{
  "code": "EIP0005",
  "message": "Missing required header: 'x-tenant'"
}
```

403 Example `EIP0006` (Invalid account ID header x-account-id):

```json
{
  "code": "EIP0006",
  "message": "Invalid account id header: 'x-account-id'"
}
```

403 Example `EIP0009` (Missing required header x-idempotency-key):

```json
{
  "code": "EIP0009",
  "message": "Missing required header: 'x-idempotency-key'"
}
```

403 Example `EIP0029` (Account blocked or canceled):

```json
{
  "code": "EIP0029",
  "message": "Account blocked or cancelled"
}
```

##### Response 409

- Response header `x-cid`: Request tracking ID. (string)
409 Example `EIP0042` (Client request ID already exists):

```json
{
  "code": "EIP0042",
  "message": "client request id already exists"
}
```

409 Example `EIP0065` (BankingGatewayAPI returned 409 provider error):

```json
{
  "code": "EIP0065",
  "message": "BankingGatewayAPI - API returned 409 provider error"
}
```

##### Response 500

- Response header `x-cid`: Request tracking ID. (string)
500 Example `EIP0015` (IntlBankAccounts - API timeout error):

```json
{
  "code": "EIP0015",
  "message": "IntlBankAccounts - API timeout error"
}
```

500 Example `EIP0014` (Accounts - API returned 5xx error):

```json
{
  "code": "EIP0014",
  "message": "Accounts - API returned 5xx error"
}
```

500 Example `EIP0007` (Internal error):

```json
{
  "code": "EIP0007",
  "message": "Internal error"
}
```

500 Example `EIP0004` (HTTP request error):

```json
{
  "code": "EIP0004",
  "message": "HTTP request error"
}
```

500 Example `EIP0011` (Accounts API timeout error):

```json
{
  "code": "EIP0011",
  "message": "Accounts API timeout error"
}
```

500 Example `EIP0028` (Transaction database error):

```json
{
  "code": "EIP0028",
  "message": "Transaction database error"
}
```

500 Example `EIP0022` (BankingGatewayAPI - API timeout error):

```json
{
  "code": "EIP0022",
  "message": "BankingGatewayAPI - API timeout error"
}
```

500 Example `EIP0070` (BankingGateway API - Failed to unmarshal error response):

```json
{
  "code": "EIP0070",
  "message": "BankingGateway API - Failed to unmarshal error response body"
}
```

500 Example `EIP0074` (Bankslip issue database error):

```json
{
  "code": "EIP0074",
  "message": "Bankslip issue database error"
}
```

##### Response 502

- Response header `x-cid`: Request tracking ID. (string)
502 Example `EIP0018` (IntlBankAccounts - API returned 5xx error):

```json
{
  "code": "EIP0018",
  "message": "IntlBankAccounts - API returned 5xx error"
}
```

502 Example `EIP0024` (BankingGatewayAPI - API returned 5xx error):

```json
{
  "code": "EIP0024",
  "message": "BankingGatewayAPI - API returned 5xx error"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `EIP0010` | Unmarshal error |
| 400 | `EIP0012` | Account not found |
| 400 | `EIP0013` | Accounts - API returned 4xx error |
| 400 | `EIP0016` | IntlBankAccounts - API Account not found |
| 400 | `EIP0017` | IntlBankAccounts - API returned 4xx error |
| 400 | `EIP0023` | BankingGatewayAPI - API returned 4xx error |
| 400 | `EIP0077` | Address not found for this Account |
| 403 | `EIP0005` | Missing required header: 'x-tenant' |
| 403 | `EIP0006` | Invalid account id header: 'x-account-id' |
| 403 | `EIP0009` | Missing required header: 'x-idempotency-key' |
| 403 | `EIP0029` | Account blocked or cancelled |
| 409 | `EIP0042` | client request id already exists |
| 409 | `EIP0065` | BankingGatewayAPI - API returned 409 provider error |
| 500 | `EIP0015` | IntlBankAccounts - API timeout error |
| 500 | `EIP0014` | Accounts - API returned 5xx error |
| 500 | `EIP0007` | Internal error |
| 500 | `EIP0004` | HTTP request error |
| 500 | `EIP0011` | Accounts API timeout error |
| 500 | `EIP0028` | Transaction database error |
| 500 | `EIP0022` | BankingGatewayAPI - API timeout error |
| 500 | `EIP0070` | BankingGateway API - Failed to unmarshal error response body |
| 500 | `EIP0074` | Bankslip issue database error |
| 502 | `EIP0018` | IntlBankAccounts - API returned 5xx error |
| 502 | `EIP0024` | BankingGatewayAPI - API returned 5xx error |

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `integrated-payments-bankslip-issue-register-1` | https://developers.pismo.io/events/docs/integrated-payments-bankslip-issue-register-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `202;400;403;409;500;502`, has examples `True`, emits events `1`, deprecated `False`.

Guides that link to this operation: `KU-AUTH-account-and-external-id-tokens`, `KU-BANK-banking-overview`, `KU-PAY-bank-slips`.

<!-- op: spec=api-specs/Banking_-_Integrated_payments.yaml method=GET path=/v1/bankslips-issue/client-requests/{clientRequestId} operationId=get-integrated-payments-api-v1-bankslips-issue-retrieve -->
### `GET /v1/bankslips-issue/client-requests/{clientRequestId}` — Get issued bank slip

- **operationId:** `get-integrated-payments-api-v1-bankslips-issue-retrieve`
- **Specification:** `api-specs/Banking_-_Integrated_payments.yaml` (Banking - Integrated payments)
- **Server base URL(s):** `https://sandbox.pismolabs.io/integrated-payments`
- **Tags:** `Bank slip issuance`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Retrieve a previously issued bank slip from the provider. This endpoint only returns one bank slip at a time.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `clientRequestId` | path | yes | string | Client request ID returned using the bank slip issue endpoint. | example: "6d6bdd2c-9980-4cf1-87ff-c99dc9ce6ef4" |
| `x-idempotency-key` | header | yes | string | Unique identifier (UUID) to ensure the operation remains idempotent, allowing for operation repitition without causing unintended effects or duplication. An idempotent operation is one that can be applied multiple times, yet the outcome remains the same. it ensures that network errors, retries, or failures can occur without introducing inconsistencies.<br> | example: "6a17f82d-7365-4451-a83d-09403f05c1ec" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Response Body | `application/json`: object (schema `bankslips_issue.GetIssueResponse`) |
| 400 | Bad Request | `application/json`: object (schema `domain.Error`) |
| 403 | Forbidden | `application/json`: object (schema `domain.Error`) |
| 404 | Not Found | `application/json`: object (schema `domain.Error`) |
| 409 | Conflict | `application/json`: object (schema `domain.Error`) |
| 500 | Internal Server Error | `application/json`: object (schema `domain.Error`) |
| 502 | Bad Gateway | `application/json`: object (schema `domain.Error`) |

##### Response 200

- Response header `x-cid`: Request tracking identifier. (string)
**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `account_id` | integer | no | Pismo Platform Account ID. | example: 123 |
| `amount` | number | no | Bank slip amount. | example: 100 |
| `bar_code` | string | no | Bar code encoding bank slip information such as the bank code, currency code, check digit, due date, amount, and beneficiary information.<br> | example: "6049000117010051039060004359977819483000015380998174912864" |
| `client_request_id` | string | no | Client request ID. | example: "6d6bdd2c-9980-4cf1-87ff-123" |
| `correlation_id` | string | no | Correlation ID. | example: "c537939d-5442-48b6-8b84-66465ba68880" |
| `created_at` | string | no | Date on which the resource was created. | example: "2024-07-24T00:00:00Z" |
| `debtor` | object (schema `bankslips_issue.IssueDebtor`) | no |  |  |
| `description` | string | no | Description detailing the bank slip. | example: "Long description." |
| `digitable_line` | string | no | Digitable line.<br><br>For example on a Brazilian bank slip, the digitable line contains numerical payment information encoding details like the payment amount, due date, beneficiary information, and other transaction-specific data.<br> | example: "60490001170100510390600043599778194830000153809" |
| `due_date` | string | no | Bank slip due date in ISO 8601 format. | example: "2024-07-25T00:00:00Z" |
| `external_id` | string | no | External ID. | example: "6d6bdd2c-9980-4cf1-87ff-456" |
| `id` | string | no | Bank slip ID. | example: "050d8e9b-586e-4419-af13-d7c6be012fb2" |
| `instructions` | object (schema `bankslips_issue.IssueInstructions`) | no |  |  |
| `org_id` | string | no | Organization ID. | example: "TN-000000000-00000-00000-0000-00000000000000" |
| `over_due_date` | string | no | Last day to accept bank slip payments. After this date, the bank slip is not paid. | example: "2024-07-25T00:00:00Z" |
| `paid_amount` | number | no | Bank slip paid amount. | example: 100 |
| `pix_emv` | string | no | The emv string that is used to pay (Pix Copia e Cola). Can be used to generate the QRCode image representation. | example: "00020101021226980014br.gov.bcb.pix2576qrcode-h.pix.provider.com.br/pixqrcode/v2/cobv/cf8aebf27395133f638ca19870a5ef5204000053039865802BR5916" |
| `pix_key` | string | no | PIX key related to the bank slip. | example: "pixkey@pix.com.br" |
| `provider` | string | no | The name of the provvider that issues the bank slip. | example: "BTG" |
| `issuer` | string | no | The name of the provider that issues the bank slip. | example: "PISMO" |
| `transaction_id` | string | no | Transaction ID related to the bank slip issue. This is the ID that links the bank slip to the specific transaction performed in the payments API. It can be used for tracking, reconciliation, and reference purposes when managing bank slips and their associated transactions. | example: "550e8400-e29b-41d4-a716-446655440000" |
| `receiver` | object (schema `bankslips_issue.IssueReceiver`) | no |  |  |
| `status` | string | no | status of issued bankslip | example: "REGISTERED" |
| `updated_at` | string | no | Date on which the bank slip is updated. | example: "2024-07-25T00:00:00Z" |

##### Response 400

- Response header `x-cid`: Request tracking identifier. (string)
400 Example `EIP0072` (Missing required path parameter {client_request_id}):

```json
{
  "code": "EIP0072",
  "message": "Missing required path parameter {client_request_id}"
}
```

400 Example `EIP0010` (Unmarshal error):

```json
{
  "code": "EIP0010",
  "message": "Unmarshal error"
}
```

400 Example `EIP0023` (BankingGatewayAPI - API returned 4xx error):

```json
{
  "code": "EIP0023",
  "message": "BankingGatewayAPI - API returned 4xx error"
}
```

##### Response 403

- Response header `x-cid`: Request tracking identifier. (string)
403 Example `EIP0005` (Missing required header {x-tenant}):

```json
{
  "code": "EIP0005",
  "message": "Missing required header {x-tenant}"
}
```

403 Example `EIP0006` (Invalid account id header {x-account-id}):

```json
{
  "code": "EIP0006",
  "message": "Invalid account id header {x-account-id}"
}
```

##### Response 404

- Response header `x-cid`: Request tracking identifier. (string)
404 Example `EIP0073` (Bank slip issue not found):

```json
{
  "code": "EIP0073",
  "message": "Bank slip issue not found"
}
```

404 Example `EIP0062` (BankingGatewayAPI - Register not found in provider):

```json
{
  "code": "EIP0062",
  "message": "BankingGatewayAPI - Register not found in provider"
}
```

##### Response 409

- Response header `x-cid`: Request tracking identifier. (string)
409 Example `EIP0065` (BankingGatewayAPI - API returned 409 provider error):

```json
{
  "code": "EIP0065",
  "message": "BankingGatewayAPI - API returned 409 provider error"
}
```

##### Response 500

- Response header `x-cid`: Request tracking identifier. (string)
500 Example `EIP0004` (HTTP request error):

```json
{
  "code": "EIP0004",
  "message": "HTTP request error"
}
```

500 Example `EIP0007` (Internal error):

```json
{
  "code": "EIP0007",
  "message": "Internal error"
}
```

500 Example `EIP0022` (BankingGatewayAPI - API timeout error):

```json
{
  "code": "EIP0022",
  "message": "BankingGatewayAPI - API timeout error"
}
```

500 Example `EIP0074` (Bankslip issue database error):

```json
{
  "code": "EIP0074",
  "message": "Bankslip issue database error"
}
```

500 Example `EIP0070` (BankingGateway API - Failed to unmarshal error response body):

```json
{
  "code": "EIP0070",
  "message": "BankingGateway API - Failed to unmarshal error response body"
}
```

##### Response 502

- Response header `x-cid`: Request tracking identifier. (string)
502 Example `EIP0024` (BankingGatewayAPI - API returned 5xx error):

```json
{
  "code": "EIP0024",
  "message": "BankingGatewayAPI - API returned 5xx error"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `EIP0072` | Missing required path parameter {client_request_id} |
| 400 | `EIP0010` | Unmarshal error |
| 400 | `EIP0023` | BankingGatewayAPI - API returned 4xx error |
| 403 | `EIP0005` | Missing required header {x-tenant} |
| 403 | `EIP0006` | Invalid account id header {x-account-id} |
| 404 | `EIP0073` | Bank slip issue not found |
| 404 | `EIP0062` | BankingGatewayAPI - Register not found in provider |
| 409 | `EIP0065` | BankingGatewayAPI - API returned 409 provider error |
| 500 | `EIP0004` | HTTP request error |
| 500 | `EIP0007` | Internal error |
| 500 | `EIP0022` | BankingGatewayAPI - API timeout error |
| 500 | `EIP0074` | Bankslip issue database error |
| 500 | `EIP0070` | BankingGateway API - Failed to unmarshal error response body |
| 502 | `EIP0024` | BankingGatewayAPI - API returned 5xx error |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;403;404;409;500;502`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-AUTH-account-and-external-id-tokens`, `KU-PAY-bank-slips`.

<!-- op: spec=api-specs/Banking_-_Integrated_payments.yaml method=DELETE path=/v1/bankslips-issue/client-requests/{clientRequestId} operationId=delete-integrated-payments-api-v1-bankslips-issue -->
### `DELETE /v1/bankslips-issue/client-requests/{clientRequestId}` — Delete issued bank slip

- **operationId:** `delete-integrated-payments-api-v1-bankslips-issue`
- **Specification:** `api-specs/Banking_-_Integrated_payments.yaml` (Banking - Integrated payments)
- **Server base URL(s):** `https://sandbox.pismolabs.io/integrated-payments`
- **Tags:** `Bank slip issuance`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Delete a previously issued bank slip and cancel it for the provider.<br>
> This endpoint produces the [Bank slip issuance canceled](https://developers.pismo.io/events/docs/integrated-payments-bankslip-issue-cancel-1) event.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `clientRequestId` | path | yes | string | Client request ID returned using the bank slip issue endpoint. | example: "6d6bdd2c-9980-4cf1-87ff-c99dc9ce6ef4" |

#### Request body

Required: yes

> Request Body

**Content type `application/json`** — schema: object (schema `bankslips_issue.DeleteIssueRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `reason` | string | no | bank slip delete reason. | example: "Cancellation of client contract." |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 204 | accepted |  |
| 400 | Bad Request | `application/json`: object (schema `domain.Error`) |
| 403 | Forbidden | `application/json`: object (schema `domain.Error`) |
| 404 | Not Found | `application/json`: object (schema `domain.Error`) |
| 409 | Conflict | `application/json`: object (schema `domain.Error`) |
| 422 | Unprocessable Entity | `application/json`: object (schema `domain.Error`) |
| 500 | Internal Server Error | `application/json`: object (schema `domain.Error`) |
| 502 | Bad Gateway | `application/json`: object (schema `domain.Error`) |
| 504 | Gateway Timeout | `application/json`: object (schema `domain.Error`) |

##### Response 204

- Response header `x-cid`: Request tracking identifier. (string)
##### Response 400

- Response header `x-cid`: Request tracking identifier. (string)
400 Example `EIP0025` (Error unmarshalling request body):

```json
{
  "code": "EIP0025",
  "message": "Error unmarshalling request body"
}
```

400 Example `EIP0010` (Unmarshal error):

```json
{
  "code": "EIP0010",
  "message": "Unmarshal error"
}
```

400 Example `EIP0023` (BankingGatewayAPI - API returned 4xx error):

```json
{
  "code": "EIP0023",
  "message": "BankingGatewayAPI - API returned 4xx error"
}
```

400 Example `EIP0003` (Bad Request):

```json
{
  "code": "EIP0003",
  "message": "Bad Request"
}
```

##### Response 403

- Response header `x-cid`: Request tracking identifier. (string)
403 Example `EIP0005` (Missing required header {x-tenant}):

```json
{
  "code": "EIP0005",
  "message": "Missing required header {x-tenant}"
}
```

403 Example `EIP0006` (Invalid account id header {x-account-id}):

```json
{
  "code": "EIP0006",
  "message": "Invalid account id header {x-account-id}"
}
```

##### Response 404

- Response header `x-cid`: Request tracking identifier. (string)
404 Example `EIP0043` (Bank slip not found):

```json
{
  "code": "EIP0043",
  "message": "Bankslips not found"
}
```

404 Example `EIP0062` (BankingGatewayAPI - Register not found in provider):

```json
{
  "code": "EIP0062",
  "message": "BankingGatewayAPI - Register data not found in provider"
}
```

##### Response 409

- Response header `x-cid`: Request tracking identifier. (string)
409 Example `EIP0065` (BankingGatewayAPI - API returned 409 provider error):

```json
{
  "code": "EIP0065",
  "message": "BankingGatewayAPI - API returned 409 provider error"
}
```

##### Response 422

- Response header `x-cid`: Request tracking identifier. (string)
422 Example `EIP0076` (Bankslip issue ExternalID invalid):

```json
{
  "code": "EIP0076",
  "message": "Bankslips issue ExternalID invalid"
}
```

##### Response 500

- Response header `x-cid`: Request tracking identifier. (string)
500 Example `EIP0007` (Internal error):

```json
{
  "code": "EIP0007",
  "message": "Internal error"
}
```

500 Example `EIP0041` (Bank slip database error):

```json
{
  "code": "EIP0041",
  "message": "Bankslips database error"
}
```

500 Example `EIP0004` (HTTP request error):

```json
{
  "code": "EIP0004",
  "message": "HTTP request error"
}
```

500 Example `EIP0022` (BankingGatewayAPI - API timeout error):

```json
{
  "code": "EIP0022",
  "message": "BankingGatewayAPI - API timeout error"
}
```

500 Example `EIP0070` (BankingGateway API - Failed to unmarshal error response body):

```json
{
  "code": "EIP0070",
  "message": "BankingGateway API - Failed to unmarshal error response body"
}
```

500 Example `EIP0053` (Send integrity message error):

```json
{
  "code": "EIP0053",
  "message": "Send integrity message error"
}
```

500 Example `EIP0074` (Bankslip issue database error):

```json
{
  "code": "EIP0074",
  "message": "Bankslip issue database error"
}
```

##### Response 502

- Response header `x-cid`: Request tracking identifier. (string)
502 Example `EIP0024` (Bad Gateway):

```json
{
  "code": "EIP0024",
  "message": "BankingGatewayAPI - API returned 5xx error"
}
```

##### Response 504

- Response header `x-cid`: Request tracking identifier. (string)
504 Example `EIP0024` (BankingGatewayAPI - API returned 5xx error):

```json
{
  "code": "EIP0024",
  "message": "BankingGatewayAPI - API returned 5xx error"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `EIP0025` | Error unmarshalling request body |
| 400 | `EIP0010` | Unmarshal error |
| 400 | `EIP0023` | BankingGatewayAPI - API returned 4xx error |
| 400 | `EIP0003` | Bad Request |
| 403 | `EIP0005` | Missing required header {x-tenant} |
| 403 | `EIP0006` | Invalid account id header {x-account-id} |
| 404 | `EIP0043` | Bankslips not found |
| 404 | `EIP0062` | BankingGatewayAPI - Register data not found in provider |
| 409 | `EIP0065` | BankingGatewayAPI - API returned 409 provider error |
| 422 | `EIP0076` | Bankslips issue ExternalID invalid |
| 500 | `EIP0007` | Internal error |
| 500 | `EIP0041` | Bankslips database error |
| 500 | `EIP0004` | HTTP request error |
| 500 | `EIP0022` | BankingGatewayAPI - API timeout error |
| 500 | `EIP0070` | BankingGateway API - Failed to unmarshal error response body |
| 500 | `EIP0053` | Send integrity message error |
| 500 | `EIP0074` | Bankslip issue database error |
| 502 | `EIP0024` | BankingGatewayAPI - API returned 5xx error |
| 504 | `EIP0024` | BankingGatewayAPI - API returned 5xx error |

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `integrated-payments-bankslip-issue-cancel-1` | https://developers.pismo.io/events/docs/integrated-payments-bankslip-issue-cancel-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `204;400;403;404;409;422;500;502;504`, has examples `True`, emits events `1`, deprecated `False`.

Guides that link to this operation: `KU-AUTH-account-and-external-id-tokens`, `KU-PAY-bank-slips`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/bankslips_issue.ListIssueItem -->
### Schema `bankslips_issue.ListIssueItem`

Pointer: `#/components/schemas/bankslips_issue.ListIssueItem`. Type: object (schema `bankslips_issue.ListIssueItem`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `account_id` | integer | no | Pismo Platform Account ID. | example: 123 |
| `client_request_id` | string | no | Client request ID. | example: "6d6bdd2c-9980-4cf1-87ff-123" |
| `correlation_id` | string | no | Correlation ID. | example: "c537939d-5442-48b6-8b84-66465ba68880" |
| `created_at` | string | no | Date on which the resource was created. | example: "2024-07-24T00:00:00Z" |
| `due_date` | string | no | Bank slip due date in ISO 8601 format. | example: "2024-07-25T00:00:00Z" |
| `external_id` | string | no | External ID. | example: "6d6bdd2c-9980-4cf1-87ff-456" |
| `id` | string | no | Bank slip ID. | example: "050d8e9b-586e-4419-af13-d7c6be012fb2" |
| `org_id` | string | no | Organization ID. | example: "TN-000000000-00000-00000-0000-00000000000000" |
| `over_due_date` | string | no | Last day to accept bank slip payments. After this date, the bank slip is not paid. | example: "2024-07-25T00:00:00Z" |
| `provider` | string | no | The name of the provvider that issues the bank slip. | example: "BTG" |
| `issuer` | string | no | The name of the provider that issues the bank slip. | example: "PISMO" |
| `transaction_id` | string | no | Transaction ID related to the bank slip issue. This is the ID that links the bank slip to the specific transaction performed in the payments API. It can be used for tracking, reconciliation, and reference purposes when managing bank slips and their associated transactions. | example: "550e8400-e29b-41d4-a716-446655440000" |
| `status` | string | no | status of issued bankslip | example: "REGISTERED" |
| `updated_at` | string | no | Date on which the bank slip is updated. | example: "2024-07-25T00:00:00Z" |

<!-- schema: #/components/schemas/bankslips_issue.OffsetPagination -->
### Schema `bankslips_issue.OffsetPagination`

Pointer: `#/components/schemas/bankslips_issue.OffsetPagination`. Type: object (schema `bankslips_issue.OffsetPagination`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `current_page` | integer | no | Current page. | example: 1 |
| `per_page` | integer | no | Number per page. | example: 10 |
| `total_items` | integer | no | Total items listed on the page. | example: 100 |
| `total_pages` | integer | no | Total pages. | example: 10 |

<!-- schema: #/components/schemas/domain.Error -->
### Schema `domain.Error`

Pointer: `#/components/schemas/domain.Error`. Type: object (schema `domain.Error`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string | no | Error type code. | example: "EIP0001" |
| `details` | string | no | Error details. | example: "Error details" |
| `message` | string | no | Error message describing the error. | example: "error" |

<!-- schema: #/components/schemas/bankslips_issue.IssueDebtor -->
### Schema `bankslips_issue.IssueDebtor`

Pointer: `#/components/schemas/bankslips_issue.IssueDebtor`. Type: object (schema `bankslips_issue.IssueDebtor`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `city` | string | no | City where the debtor resides. | example: "New York" |
| `complement` | string | no | Additional address. | example: "Complement" |
| `document_number` | string | no | A government document number, such as a CPF (Brazil) - Cadastro de Pessoas Fisicas (Indiviual Taxpayer Registry) number, CNPJ (Brazil) - Cadastro Nacional de Pessoa Juridica (National Registry of Legal Entities) number - unique ID for legal entities, such as companies and organizations.<br> | example: "00000000000" |
| `name` | string | no | Debtor's full name. | example: "John Doe" |
| `neighborhood` | string | no | Neighborhood name where the debtor resides. | example: "Neighborhood" |
| `number` | string | no | Street number. | example: "123" |
| `state` | string | no | The name of the state. | example: "UF" |
| `street` | string | no | The name of the street where the debtor resides. | example: "Street" |
| `zip_code` | string | no | Zip code. | example: "00000000" |

<!-- schema: #/components/schemas/bankslips_issue.IssueInstructions -->
### Schema `bankslips_issue.IssueInstructions`

Pointer: `#/components/schemas/bankslips_issue.IssueInstructions`. Type: object (schema `bankslips_issue.IssueInstructions`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `fine` | number | yes | Fine to be applied to the bank slip amount if overdue. | example: 5 |
| `interest` | number | yes | Interest to be applied to the bank slips amount when overdue. | example: 10 |
| `discount` | object (schema `bankslips_issue.IssueDiscount`) | no |  |  |

<!-- schema: #/components/schemas/bankslips_issue.IssueReceiver -->
### Schema `bankslips_issue.IssueReceiver`

Pointer: `#/components/schemas/bankslips_issue.IssueReceiver`. Type: object (schema `bankslips_issue.IssueReceiver`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `document_number` | string | no | Recipient 's document number. |  |
| `name` | string | no | Recipient name. |  |

<!-- schema: #/components/schemas/bankslips_issue.IssueDiscount -->
### Schema `bankslips_issue.IssueDiscount`

Pointer: `#/components/schemas/bankslips_issue.IssueDiscount`. Type: object (schema `bankslips_issue.IssueDiscount`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `amount` | number | no | Discounted amount to be applied to the bank slip amount if paid before or on the deadline. | example: 10 |
| `deadline` | string | no | Discount deadline. | example: "2024-09-25T00:00:00.000Z" |
| `type` | string | no | Fixed bank slip type | example: "fixed" |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Banking_-_Integrated_payments.yaml` | tag `Bank slip issuance`: GET /v1/bankslips-issue, POST /v1/bankslips-issue, GET /v1/bankslips-issue/client-requests/{clientRequestId}, DELETE /v1/bankslips-issue/client-requests/{clientRequestId} | https://github.com/PismoDevEx/pismo-api-specs | `8696ddecc6a5182f…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-AUTH-account-and-external-id-tokens` — Endpoints that require account-specific or external-ID tokens
- `KU-BANK-banking-overview` — Banking overview
- `KU-ERR-codes-eip` — Error codes: EIP
- `KU-EVT-catalogue-integrated` — Event catalogue: integrated
- `KU-PAY-bank-slips` — Bank slips
