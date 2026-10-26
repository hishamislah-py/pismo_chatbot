---
ku_id: KU-API-banking-integrated-payments--ebill-registration
title: 'API reference: Banking - Integrated payments — eBill registration'
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
- get-integrated-payments-api-v1-ebill-registration-accounts-accountId
- post-integrated-payments-api-v1-ebill-registration-accounts-accountId
- delete-integrated-payments-api-v1-ebill-registration-accounts-accountId
related_kus:
- KU-BANK-banking-overview
- KU-ERR-codes-eip
- KU-EVT-catalogue-integrated
specification_version: '1.0'
---

# API reference: Banking - Integrated payments — eBill registration

**KU ID:** `KU-API-banking-integrated-payments--ebill-registration` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 3 operation(s) tagged `eBill registration` in `api-specs/Banking_-_Integrated_payments.yaml` (“Banking - Integrated payments”, version `1.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `GET /v1/ebill-registration/accounts/{accountId}` | `get-integrated-payments-api-v1-ebill-registration-accounts-accountId` | Get eBill registration | no |
| `POST /v1/ebill-registration/accounts/{accountId}` | `post-integrated-payments-api-v1-ebill-registration-accounts-accountId` | Register eBill | no |
| `DELETE /v1/ebill-registration/accounts/{accountId}` | `delete-integrated-payments-api-v1-ebill-registration-accounts-accountId` | Delete eBill registration | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"}

## Operation contracts

<!-- op: spec=api-specs/Banking_-_Integrated_payments.yaml method=GET path=/v1/ebill-registration/accounts/{accountId} operationId=get-integrated-payments-api-v1-ebill-registration-accounts-accountId -->
### `GET /v1/ebill-registration/accounts/{accountId}` — Get eBill registration

- **operationId:** `get-integrated-payments-api-v1-ebill-registration-accounts-accountId`
- **Specification:** `api-specs/Banking_-_Integrated_payments.yaml` (Banking - Integrated payments)
- **Server base URL(s):** `https://sandbox.pismolabs.io/integrated-payments`
- **Tags:** `eBill registration`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Retrieve eBill registration information.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `accountId` | path | yes | string | Your Pismo account ID. | example: "78123456" |
| `x-idempotency-key` | header | yes | string | Unique identifier (UUID) to ensure the operation remains idempotent, allowing for operation repitition without causing unintended effects or duplication. An idempotent operation is one that can be applied multiple times, yet the outcome remains the same. it ensures that network errors, retries, or failures can occur without introducing inconsistencies.<br> | example: "6a17f82d-7365-4451-a83d-09403f05c1ec" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Response Body | `application/json`: object (schema `ebill.GetEbillResponse`) |
| 403 | Forbidden | `application/json`: object (schema `domain.Error`) |
| 404 | Not Found | `application/json`: object (schema `domain.Error`) |
| 500 | Internal Server Error | `application/json`: object (schema `domain.Error`) |

##### Response 200

- Response header `x-cid`: Request tracking identifier. (string)
**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | string | no | Registration ID. |  |
| `client_request_id` | string | no | Client request ID. |  |
| `external_id` | string | no | Provider's external ID. |  |
| `status` | string | no | Registration status. |  |
| `document_number` | string | no | Document number. |  |

##### Response 403

- Response header `x-cid`: Request tracking ID. (string)
403 Example `EIP0005` (Missing required header {x-tenant}):

```json
{
  "code": "EIP0005",
  "message": "Missing required header: 'x-tenant'"
}
```

403 Example `EIP0006` (Invalid account id header {x-account-id}):

```json
{
  "code": "EIP0006",
  "message": "Invalid account id header: 'x-account-id'"
}
```

##### Response 404

- Response header `x-cid`: Request tracking ID. (string)
404 Example `EIP0088` (eBill registration not found):

```json
{
  "code": "EIP0088",
  "message": "Ebill registration not found"
}
```

##### Response 500

- Response header `x-cid`: Request tracking ID. (string)
500 Example `EIP0007` (Internal error):

```json
{
  "code": "EIP0007",
  "message": "Internal error"
}
```

500 Example `EIP0089` (eBill database error):

```json
{
  "code": "EIP0089",
  "message": "Ebill database error"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 403 | `EIP0005` | Missing required header: 'x-tenant' |
| 403 | `EIP0006` | Invalid account id header: 'x-account-id' |
| 404 | `EIP0088` | Ebill registration not found |
| 500 | `EIP0007` | Internal error |
| 500 | `EIP0089` | Ebill database error |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;403;404;500`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-BANK-banking-overview`.

<!-- op: spec=api-specs/Banking_-_Integrated_payments.yaml method=POST path=/v1/ebill-registration/accounts/{accountId} operationId=post-integrated-payments-api-v1-ebill-registration-accounts-accountId -->
### `POST /v1/ebill-registration/accounts/{accountId}` — Register eBill

- **operationId:** `post-integrated-payments-api-v1-ebill-registration-accounts-accountId`
- **Specification:** `api-specs/Banking_-_Integrated_payments.yaml` (Banking - Integrated payments)
- **Server base URL(s):** `https://sandbox.pismolabs.io/integrated-payments`
- **Tags:** `eBill registration`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Register eBill for an account.<br>
> eBill offers an electronic view of bank slips linked to your document number, simplifying daily use without paper documents. You can pay slips via internet banking or a banking app, minimizing barcode errors, and track all accounts under your document number. For more details, refer to the [eBill](doc:banking-overview#ebill) section in the *Banking overview* guide.<br>
> This endpoint generates an [eBill registration status updated](https://developers.pismo.io/events/docs/integrated-payments-ebill-status-change-1) event.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `accountId` | path | yes | string | Your Pismo account ID. | example: "78123456" |
| `x-idempotency-key` | header | yes | string | Unique identifier (UUID) to ensure the operation remains idempotent, allowing for operation repitition without causing unintended effects or duplication. An idempotent operation is one that can be applied multiple times, yet the outcome remains the same. it ensures that network errors, retries, or failures can occur without introducing inconsistencies.<br> | example: "6a17f82d-7365-4451-a83d-09403f05c1ec" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | Response Body | `application/json`: object (schema `ebill.RegistrationResponse`) |
| 400 | Bad Request | `application/json`: object (schema `domain.Error`) |
| 403 | Forbidden | `application/json`: object (schema `domain.Error`) |
| 409 | Conflict | `application/json`: object (schema `domain.Error`) |
| 500 | Internal Server Error | `application/json`: object (schema `domain.Error`) |
| 502 | Bad Gateway | `application/json`: object (schema `domain.Error`) |

##### Response 201

- Response header `x-cid`: Request tracking ID. (string)
**201 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | string | no | Registration ID. |  |
| `external_id` | string | no | Provider's external ID. |  |
| `status` | string | no | Registration status. |  |

##### Response 400

- Response header `x-cid`: Request tracking ID. (string)
400 Example `EIP0005` (Missing required header {x-tenant}):

```json
{
  "code": "EIP0005",
  "message": "Missing required header {x-tenant}"
}
```

400 Example `EIP0006` (Missing required header {x-account-id}):

```json
{
  "code": "EIP0006",
  "message": "Missing required header {x-account-id}"
}
```

400 Example `EIP0008` (Validation error):

```json
{
  "code": "EIP0008",
  "message": "Validation error"
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

400 Example `EIP0023` (BankingGatewayAPI - API returned 4xx error):

```json
{
  "code": "EIP0023",
  "message": "BankingGatewayAPI - API returned 4xx error"
}
```

##### Response 403

- Response header `x-cid`: Request tracking ID. (string)
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
  "message": "Invalid account id header: 'x-account-id'"
}
```

##### Response 409

- Response header `x-cid`: Request tracking ID. (string)
409 Example `EIP0065` (BankingGatewayAPI - API returned 409 provider error):

```json
{
  "code": "EIP0065",
  "message": "BankingGatewayAPI - API returned 409 provider error"
}
```

409 Example `EIP0090` (eBill registration already processing):

```json
{
  "code": "EIP0090",
  "message": "Ebill registration is already being processed"
}
```

##### Response 500

- Response header `x-cid`: Request tracking ID. (string)
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

500 Example `EIP0022` (BankingGatewayAPI - API timeout error):

```json
{
  "code": "EIP0022",
  "message": "BankingGatewayAPI - API timeout error"
}
```

500 Example `EIP0089` (eBill database error):

```json
{
  "code": "EIP0089",
  "message": "Ebill database error"
}
```

500 Example `EIP0070` (BankingGateway API - Failed to unmarshal error response):

```json
{
  "code": "EIP0070",
  "message": "BankingGateway API - Failed to unmarshal error response body"
}
```

##### Response 502

- Response header `x-cid`: Request tracking ID. (string)
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
| 400 | `EIP0005` | Missing required header {x-tenant} |
| 400 | `EIP0006` | Missing required header {x-account-id} |
| 400 | `EIP0008` | Validation error |
| 400 | `EIP0012` | Account not found |
| 400 | `EIP0013` | Accounts - API returned 4xx error |
| 400 | `EIP0023` | BankingGatewayAPI - API returned 4xx error |
| 403 | `EIP0005` | Missing required header {x-tenant} |
| 403 | `EIP0006` | Invalid account id header: 'x-account-id' |
| 409 | `EIP0065` | BankingGatewayAPI - API returned 409 provider error |
| 409 | `EIP0090` | Ebill registration is already being processed |
| 500 | `EIP0004` | HTTP request error |
| 500 | `EIP0007` | Internal error |
| 500 | `EIP0011` | Accounts API timeout error |
| 500 | `EIP0014` | Accounts - API returned 5xx error |
| 500 | `EIP0022` | BankingGatewayAPI - API timeout error |
| 500 | `EIP0089` | Ebill database error |
| 500 | `EIP0070` | BankingGateway API - Failed to unmarshal error response body |
| 502 | `EIP0024` | BankingGatewayAPI - API returned 5xx error |

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `integrated-payments-ebill-status-change-1` | https://developers.pismo.io/events/docs/integrated-payments-ebill-status-change-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `201;400;403;409;500;502`, has examples `True`, emits events `1`, deprecated `False`.

Guides that link to this operation: `KU-BANK-banking-overview`.

<!-- op: spec=api-specs/Banking_-_Integrated_payments.yaml method=DELETE path=/v1/ebill-registration/accounts/{accountId} operationId=delete-integrated-payments-api-v1-ebill-registration-accounts-accountId -->
### `DELETE /v1/ebill-registration/accounts/{accountId}` — Delete eBill registration

- **operationId:** `delete-integrated-payments-api-v1-ebill-registration-accounts-accountId`
- **Specification:** `api-specs/Banking_-_Integrated_payments.yaml` (Banking - Integrated payments)
- **Server base URL(s):** `https://sandbox.pismolabs.io/integrated-payments`
- **Tags:** `eBill registration`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Delete eBill registration.<br>
> This endpoint produces an [eBill registration status updated](https://developers.pismo.io/events/docs/integrated-payments-ebill-status-change-1) event.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `accountId` | path | yes | string | Your Pismo account ID. | example: "78123456" |
| `x-idempotency-key` | header | yes | string | Unique identifier (UUID) to ensure the operation remains idempotent, allowing for operation repitition without causing unintended effects or duplication. An idempotent operation is one that can be applied multiple times, yet the outcome remains the same. it ensures that network errors, retries, or failures can occur without introducing inconsistencies.<br> | example: "6a17f82d-7365-4451-a83d-09403f05c1ec" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 204 | No Content |  |
| 400 | Bad Request | `application/json`: object (schema `domain.Error`) |
| 403 | Forbidden | `application/json`: object (schema `domain.Error`) |
| 404 | Not Found | `application/json`: object (schema `domain.Error`) |
| 409 | Conflict | `application/json`: object (schema `domain.Error`) |
| 500 | Internal Server Error | `application/json`: object (schema `domain.Error`) |
| 502 | Bad Gateway | `application/json`: object (schema `domain.Error`) |

##### Response 204

- Response header `x-cid`: Request tracking ID. (string)
##### Response 400

- Response header `x-cid`: Request tracking ID. (string)
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

400 Example `EIP0023` (BankingGatewayAPI - API returned 4xx error):

```json
{
  "code": "EIP0023",
  "message": "BankingGatewayAPI - API returned 4xx error"
}
```

400 Example `EIP0091` (eBill registration is not deletable):

```json
{
  "code": "EIP0091",
  "message": "Ebill registration is not deletable"
}
```

##### Response 403

- Response header `x-cid`: Request tracking ID. (string)
403 Example `EIP0005` (Missing required header {x-tenant}):

```json
{
  "code": "EIP0005",
  "message": "Missing required header: 'x-tenant'"
}
```

403 Example `EIP0006` (Invalid account id header {x-account-id}):

```json
{
  "code": "EIP0006",
  "message": "Invalid account id header: 'x-account-id'"
}
```

##### Response 404

- Response header `x-cid`: Request tracking ID. (string)
404 Example `EIP0088` (eBill registration not found):

```json
{
  "code": "EIP0088",
  "message": "Ebill registration not found"
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

- Response header `x-cid`: Request tracking ID. (string)
409 Example `EIP0065` (BankingGatewayAPI - API returned 409 provider error):

```json
{
  "code": "EIP0065",
  "message": "BankingGatewayAPI - API returned 409 provider error"
}
```

##### Response 500

- Response header `x-cid`: Request tracking ID. (string)
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

500 Example `EIP0022` (BankingGatewayAPI - API timeout error):

```json
{
  "code": "EIP0022",
  "message": "BankingGatewayAPI - API timeout error"
}
```

500 Example `EIP0089` (eBill database error):

```json
{
  "code": "EIP0089",
  "message": "Ebill database error"
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

- Response header `x-cid`: Request tracking ID. (string)
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
| 400 | `EIP0012` | Account not found |
| 400 | `EIP0013` | Accounts - API returned 4xx error |
| 400 | `EIP0023` | BankingGatewayAPI - API returned 4xx error |
| 400 | `EIP0091` | Ebill registration is not deletable |
| 403 | `EIP0005` | Missing required header: 'x-tenant' |
| 403 | `EIP0006` | Invalid account id header: 'x-account-id' |
| 404 | `EIP0088` | Ebill registration not found |
| 404 | `EIP0062` | BankingGatewayAPI - Register data not found in provider |
| 409 | `EIP0065` | BankingGatewayAPI - API returned 409 provider error |
| 500 | `EIP0004` | HTTP request error |
| 500 | `EIP0007` | Internal error |
| 500 | `EIP0011` | Accounts API timeout error |
| 500 | `EIP0014` | Accounts - API returned 5xx error |
| 500 | `EIP0022` | BankingGatewayAPI - API timeout error |
| 500 | `EIP0089` | Ebill database error |
| 500 | `EIP0070` | BankingGateway API - Failed to unmarshal error response body |
| 502 | `EIP0024` | BankingGatewayAPI - API returned 5xx error |

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `integrated-payments-ebill-status-change-1` | https://developers.pismo.io/events/docs/integrated-payments-ebill-status-change-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `204;400;403;404;409;500;502`, has examples `True`, emits events `1`, deprecated `False`.

Guides that link to this operation: `KU-BANK-banking-overview`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/domain.Error -->
### Schema `domain.Error`

Pointer: `#/components/schemas/domain.Error`. Type: object (schema `domain.Error`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string | no | Error type code. | example: "EIP0001" |
| `details` | string | no | Error details. | example: "Error details" |
| `message` | string | no | Error message describing the error. | example: "error" |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Banking_-_Integrated_payments.yaml` | tag `eBill registration`: GET /v1/ebill-registration/accounts/{accountId}, POST /v1/ebill-registration/accounts/{accountId}, DELETE /v1/ebill-registration/accounts/{accountId} | https://github.com/PismoDevEx/pismo-api-specs | `8696ddecc6a5182f…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-BANK-banking-overview` — Banking overview
- `KU-ERR-codes-eip` — Error codes: EIP
- `KU-EVT-catalogue-integrated` — Event catalogue: integrated
