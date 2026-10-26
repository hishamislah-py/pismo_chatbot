---
ku_id: KU-API-core-platform-payment-methods--force-operations
title: 'API reference: Core platform - Payment methods — Force operations'
category: api_reference
ku_type: api_reference
lifecycle: current
sources:
- path: api-specs/Core_platform_-_Payment_methods.yaml
  sha256: 9b02c87b6e39a1c803b8361362aa5beb50c098580d9549c8f58475df0d91a80e
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
- post-payments-v1-force
- post-payments-v1-force-cancel
related_kus:
- KU-CARD-full-balance-versus-zero-balance
- KU-ERR-codes-acq-to-esma
- KU-ERR-codes-wiac-to-wstm
- KU-EVT-catalogue-other-domains
- KU-EVT-payments-data-events
- KU-PAY-force-operation
- KU-PAY-installments-payment
specification_version: 1.0.0
---

# API reference: Core platform - Payment methods — Force operations

**KU ID:** `KU-API-core-platform-payment-methods--force-operations` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 2 operation(s) tagged `Force operations` in `api-specs/Core_platform_-_Payment_methods.yaml` (“Core platform - Payment methods”, version `1.0.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> APIs to manage force operations.

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `POST /payments/v1/payments/force` | `post-payments-v1-force` | Force operation | no |
| `POST /payments/v1/payments/force/cancel` | `post-payments-v1-force-cancel` | Cancel forced operation | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"} — Account access token. Tokens can expire quickly, which can result in an "Unauthorized" error.

## Operation contracts

<!-- op: spec=api-specs/Core_platform_-_Payment_methods.yaml method=POST path=/payments/v1/payments/force operationId=post-payments-v1-force -->
### `POST /payments/v1/payments/force` — Force operation

- **operationId:** `post-payments-v1-force`
- **Specification:** `api-specs/Core_platform_-_Payment_methods.yaml` (Core platform - Payment methods)
- **Server base URL(s):** `https://sandbox.pismolabs.io`, `https://gw-pci.pismolabs.io`
- **Tags:** `Force operations`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Force a credit or debit operation in the specified account using the `account_id`, the `processing_code`, and the `amount` provided.
> This operation directly impacts the balance but does not perform any of the validations that are done in the [Transfer funds](ref:post-payments-v1-payments) endpoint, such as validating the account status, account balance, and flex controls.
>
> This endpoint generates an [Authorization created](https://developers.pismo.io/events/docs/authorization-authorization-event-1) event with authorization > type "FORCE".
>
> For additional information, see the [Force operation](doc:force-operation) guide. 
>
> ## Forced credit example
>
> Assuming that  `processing_code` "090907" is defined as credit type, the following payload executes a forced credit operation:
>
> ```json  
> {
>   "amount": 12.34,
>   "account_id": 2417,
>   "processing_code": "090907",
>   "descriptor": "Cashback credit",
>   "original_authorization": {
>     "id": 123,
>     "type": "PLATFORM"
>   },
>   "metadata": {
>     "my-custom-key": "my-custom-info"
>   }
> }
> ```

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `x-tenant` | header | yes | string | Unique Org ID | pattern: "TN\\\\-[0-9a-fA-F]{8}\\\\b-[0-9a-fA-F]{4}\\\\b-[0-9a-fA-F]{4}\\\\b-[0-9a-fA-F]{4}\\\\b-[0-9a-fA-F]{12}"; minLength: 39; maxLength: 39; example: "TN-c0e4c660-9059-404c-ab22-761aa431766c" |
| `x-cid` | header | no | string | Related correlation identifier. If none is provided, a random one is generated. | example: "c737895c-8159-4c0c-a92a-a4f8600bff37" |
| `x-account-id` | header | no | number | Optional account identifier. | example: 1 |
| `x-skip-timeline` | header | no | string | If set to `true`, this will prevent the generation of timeline events in the customer timeline. | example: "true" |

#### Request body

Required: yes

**Content type `application/json`** — schema: object (schema `ForceRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `tracking_id` | string | no | Unique tracking ID of the forced operation. If you don't provide one, the Pismo platform generates it randomly. | pattern: "^[0-9a-fA-F]{8}\\\\b-[0-9a-fA-F]{4}\\\\b-[0-9a-fA-F]{4}\\\\b-[0-9a-fA-F]{4}\\\\b-[0-9a-fA-F]{12}$"; minLength: 36; maxLength: 50; example: "be68db6e-8da0-4761-8632-6a51857bd123" |
| `account_id` | integer | no | Unique identifier of an account in the Pismo platform. | example: 101 |
| `amount` | number | no | Credit or debit amount | format: "float"; example: 12.13 |
| `processing_code` | string | no | Unique 6-character processing code that identifies the credit or debit operation. | pattern: "^[0-9]{6}$"; example: "004000" |
| `currency` | string (schema `Currency`) | no | ISO-4217 alphabetic or numeric (3 characters) operation currency code. For example, either BRL or 986 for Brazilian real. | example: "BRL" |
| `descriptor` | string | no | Optional text that describes the created operation. The platform supports only letters and numbers in this field and removes any special characters or emojis. | example: "Single credit adjustment" |
| `metadata` | object (schema `Metadata`) | no | This optional user-defined key-value object field can be used with external operations to provide additional context or supplementary custom information for the operation. <br><br>The Pismo platform does not perform any validation or processing on this field but passes this object to the acquirer in transactions involving calls to the acquirer and sends it in the events related to the stream of data produced at the end of the request.<br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis#metadata).<br> | example: {"any-key": "any-value"} |
| `original_authorization` | object | no | This optional field identifies the original authorization to be forced. <br>When this object is provided, both the `id` and `type` fields need to be filled.<br> |  |
| `original_authorization.id` | number | yes | Original authorization ID in the Pismo plataform. | example: 101 |
| `original_authorization.type` | string | yes | Original authorization type. | enum: ["NETWORK", "PLATFORM"]; example: "NETWORK" |
| `payment_datetime` | string | no | Value date (effective date) of the payment in UTC-0 (RFC3339) format. <br>Payments can be backdated but future dates are not allowed.<br>example: '2020-01-02T15:14:00.218Z'    <br> | format: "date-time" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | Created | `application/json`: object (schema `ForceResponse`) |
| 202 | Accepted | `application/json`: object (schema `AcceptedResponse`) |
| 400 | Bad request | `application/json`: object (schema `ErrorModel`) |
| 409 | Conflict | `application/json`: object (schema `TrackingIdAlreadyInUseResponse`) |
| 500 | Internal server error | `application/json`: object (schema `ErrorModel`) |

##### Response 201

**201 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `authorization_id` | integer | no | Generated authorization ID | format: "int64"; example: 15301234 |
| `event_date` | string | no | Date and time of the authorization, in the UTC-0 (RFC3339) format. | format: "date-time"; example: "2020-01-02T15:14:00.218Z" |
| `tracking_id` | string | no | Unique tracking ID of the forced operation. If you don't provide one, the Pismo platform generates it randomly. | minLength: 36; maxLength: 50; example: "82766158-514c-42f0-87e2-1bb3250c6dee" |

##### Response 202

**202 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `error_code` | string | no | Error code | deprecated: true; example: "EP2P0010" |
| `code` | string | no | Error code | example: "EP2P0010" |
| `message` | string | no | Message that the request is processing and will finish asynchronously. | example: "Request is processing and will finish asynchronously" |

##### Response 400

400 Example `Invalid payload`:

```json
{
  "error_code": "WP2P0000",
  "code": "WP2P0000",
  "message": "Invalid payload"
}
```

400 Example `Invalid amount`:

```json
{
  "error_code": "WP2P0000",
  "code": "WP2P0000",
  "message": "The amount must have a maximum of two decimal places."
}
```

400 Example `Negative amount`:

```json
{
  "error_code": "WP2P1005",
  "code": "WP2P1005",
  "message": "The amount cannot be negative or zero."
}
```

400 Example `Cannot perform calculations`:

```json
{
  "error_code": "WRAT00001",
  "code": "WRAT00001",
  "message": "Cannot perform calculations"
}
```

400 Example `Program not found`:

```json
{
  "error_code": "WP2P0022",
  "code": "WP2P0022",
  "message": "Program not found"
}
```

400 Example `Account not found`:

```json
{
  "error_code": "WP2P0023",
  "code": "WP2P0023",
  "message": "Account not found"
}
```

400 Example `Invalid currency`:

```json
{
  "error_code": "WP2P0000",
  "code": "WP2P0000",
  "message": "The currency sent is invalid."
}
```

400 Example `AccountID is doesn't match the original authorization`:

```json
{
  "error_code": "WP2P0000",
  "code": "WP2P0000",
  "message": "Account ID in this request doesn't match the account ID of the original authorization."
}
```

400 Example `Original authorization id was not provided`:

```json
{
  "error_code": "WP2P0000",
  "code": "WP2P0000",
  "message": "Original authorization id was not provided."
}
```

400 Example `Original authorization type was not provided`:

```json
{
  "error_code": "WP2P0000",
  "code": "WP2P0000",
  "message": "Original authorization type was not provided."
}
```

400 Example `Limit of two decimal places`:

```json
{
  "error_code": "WP2P0000",
  "code": "WP2P0000",
  "message": "The amount must have a maximum of two decimal places."
}
```

400 Example `Exceed amount limit`:

```json
{
  "error_code": "WP2P0000",
  "code": "WP2P0000",
  "message": "A maximum of 20 digits, including two decimals, is allowed for the amount field."
}
```

##### Response 500

500 Example `Database connection error`:

```json
{
  "error_code": "WP2P0000",
  "code": "WP2P0000",
  "message": "Database connection error"
}
```

500 Example `Error on request calculations`:

```json
{
  "error_code": "ERAT00001",
  "code": "ERAT00001",
  "message": "Error on request calculations"
}
```

500 Example `Marshalling Error`:

```json
{
  "error_code": "ERAT00002",
  "code": "ERAT00002",
  "message": "Failed when transforming data"
}
```

500 Example `Internal Error`:

```json
{
  "error_code": "ERAT00003",
  "code": "ERAT00003",
  "message": "An Internal Error has occurred. Please try again"
}
```

500 Example `Accounts api with troubles`:

```json
{
  "error_code": "EP2P0012",
  "code": "EP2P0012",
  "message": "Accounts API with troubles"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `WP2P0000` | Invalid payload |
| 400 | `WP2P1005` | The amount cannot be negative or zero. |
| 400 | `WRAT00001` | Cannot perform calculations |
| 400 | `WP2P0022` | Program not found |
| 400 | `WP2P0023` | Account not found |
| 500 | `WP2P0000` | Database connection error |
| 500 | `ERAT00001` | Error on request calculations |
| 500 | `ERAT00002` | Failed when transforming data |
| 500 | `ERAT00003` | An Internal Error has occurred. Please try again |
| 500 | `EP2P0012` | Accounts API with troubles |

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `authorization-authorization-event-1` | https://developers.pismo.io/events/docs/authorization-authorization-event-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `201;202;400;409;500`, has examples `True`, emits events `1`, deprecated `False`.

Guides that link to this operation: `KU-CARD-full-balance-versus-zero-balance`, `KU-EVT-payments-data-events`, `KU-PAY-force-operation`, `KU-PAY-installments-payment`.

<!-- op: spec=api-specs/Core_platform_-_Payment_methods.yaml method=POST path=/payments/v1/payments/force/cancel operationId=post-payments-v1-force-cancel -->
### `POST /payments/v1/payments/force/cancel` — Cancel forced operation

- **operationId:** `post-payments-v1-force-cancel`
- **Specification:** `api-specs/Core_platform_-_Payment_methods.yaml` (Core platform - Payment methods)
- **Server base URL(s):** `https://sandbox.pismolabs.io`, `https://gw-pci.pismolabs.io`
- **Tags:** `Force operations`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Cancel forced operation. Only works with forced operations and with the total amount.
>
> This endpoint generates an [Authorization cancelled](https://developers.pismo.io/events/docs/authorization-authorization-cancellation-event-1) event with authorization > type "FORCE".

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `x-skip-timeline` | header | no | string | If set to `true`, this will prevent the generation of timeline events in the customer timeline. | example: "true" |

#### Request body

Required: yes

**Content type `application/json`** — schema: object (schema `ForceCancelRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `authorization_id` | integer | no |  | format: "int64"; minimum: 1; example: 15301234 |
| `tracking_id` | string | no | Unique tracking ID of the cancellation. If you don't provide one, the Pismo platform generates it randomly. | pattern: "^[0-9a-fA-F]{8}\\\\b-[0-9a-fA-F]{4}\\\\b-[0-9a-fA-F]{4}\\\\b-[0-9a-fA-F]{4}\\\\b-[0-9a-fA-F]{12}$"; minLength: 36; maxLength: 50; example: "1ff51e99-3a05-448a-bc19-7b5c05274174" |
| `amount` | number | no | Optional full or partial amount to cancel, which cannot be more than the original transaction amount. Maximum of two decimal places. | format: "float" |
| `original_tracking_id` | string | no | Either this field or `authorization_id` is **REQUIRED**. Unique tracking ID of the original operation to be canceled. Returned from the force request (`v1/payments/force`) as `tracking_id`. | pattern: "^[0-9a-fA-F]{8}\\\\b-[0-9a-fA-F]{4}\\\\b-[0-9a-fA-F]{4}\\\\b-[0-9a-fA-F]{4}\\\\b-[0-9a-fA-F]{12}$"; minLength: 36; maxLength: 50; example: "0d240226-d03e-47eb-ab3f-6d57c7d5feeb" |
| `cancel_fees` | boolean | no | Indicates whether to cancel associated fees when canceling a forced operation. Default value is `false`.<br>- If set to `true`, when the cancel forced operation is performed, the associated fees on the original forced operation are cancelled also.<br>- If set to `false`, when the cancel forced operation is performed, the associated fees on the original forced operation are not cancelled.<br> | example: false |
| `descriptor` | string | no | Optional text that describes the created authorization. The platform supports only letters and numbers in this field and removes any special characters or emojis. | example: "Single credit adjustment" |
| `metadata` | object (schema `Metadata`) | no | This optional user-defined key-value object field can be used with external operations to provide additional context or supplementary custom information for the operation. <br><br>The Pismo platform does not perform any validation or processing on this field but passes this object to the acquirer in transactions involving calls to the acquirer and sends it in the events related to the stream of data produced at the end of the request.<br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis#metadata).<br> | example: {"any-key": "any-value"} |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `ForceCancelResponse`) |
| 202 | Accepted | `application/json`: object (schema `AcceptedResponse`) |
| 400 | Bad request | `application/json`: object (schema `ErrorModel`) |
| 404 | Not found | `application/json`: object (schema `ErrorModel`) |
| 409 | Conflict | `application/json`: object (schema `CancelForceTrackingIdAlreadyInUseResponse`) |
| 500 | Internal server error | `application/json`: object (schema `ErrorModel`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `authorization_id` | integer | yes | Generated cancellation authorization ID | format: "int64"; example: 15301234 |
| `event_date` | string | yes | Date and time of the cancellation authorization, in the UTC-0 (RFC3339) format. | format: "date-time"; example: "2020-01-02T15:14:00.218Z" |
| `tracking_id` | string | yes | Unique 36-character identifier for the forced cancellation operation. If you didn't provide an identifier, then the Pismo platform automatically generates and includes one in the response. | example: "82766158-514c-42f0-87e2-1bb3250c6dee" |

##### Response 202

**202 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `error_code` | string | no | Error code | deprecated: true; example: "EP2P0010" |
| `code` | string | no | Error code | example: "EP2P0010" |
| `message` | string | no | Message that the request is processing and will finish asynchronously. | example: "Request is processing and will finish asynchronously" |

##### Response 400

400 Example `Invalid payload`:

```json
{
  "error_code": "WP2P0000",
  "code": "WP2P0000",
  "message": "Invalid payload"
}
```

400 Example `Authorization is not Force`:

```json
{
  "error_code": "WP2P0022",
  "code": "WP2P0022",
  "message": "Only allowed to cancel force authorizations"
}
```

400 Example `Orgs operation not found`:

```json
{
  "error_code": "WP2P0003",
  "code": "WP2P0003",
  "message": "No Orgs Operation Found"
}
```

400 Example `The amount cannot be negative or zero`:

```json
{
  "error_code": "WP2P1005",
  "code": "WP2P1005",
  "message": "The amount cannot be negative or zero."
}
```

400 Example `Amount should be less than or equal to the amount of the original transaction, and greater than 0`:

```json
{
  "error_code": "EP2P0005",
  "code": "EP2P0005",
  "message": "Amount should be less than or equal to the amount of the original transaction, and greater than 0."
}
```

400 Example `Partial cancellation with the associated fees was already made`:

```json
{
  "error_code": "EP2P0014",
  "code": "EP2P0014",
  "message": "Partial cancellation with the associated fees was already made."
}
```

400 Example `Limit of two decimal places`:

```json
{
  "error_code": "WP2P0000",
  "code": "WP2P0000",
  "message": "The amount must have a maximum of two decimal places."
}
```

400 Example `Exceed amount limit`:

```json
{
  "error_code": "WP2P0000",
  "code": "WP2P0000",
  "message": "A maximum of 20 digits, including two decimals, is allowed for the amount field."
}
```

##### Response 404

404 Example `Authorization not found`:

```json
{
  "error_code": "WP2P0008",
  "code": "WP2P0008",
  "message": "Authorization not found"
}
```

##### Response 500

500 Example `Database connection error`:

```json
{
  "error_code": "WP2P0000"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `WP2P0000` | Invalid payload |
| 400 | `WP2P0022` | Only allowed to cancel force authorizations |
| 400 | `WP2P0003` | No Orgs Operation Found |
| 400 | `WP2P1005` | The amount cannot be negative or zero. |
| 400 | `EP2P0005` | Amount should be less than or equal to the amount of the original transaction, and greater than 0. |
| 400 | `EP2P0014` | Partial cancellation with the associated fees was already made. |
| 404 | `WP2P0008` | Authorization not found |
| 500 | `WP2P0000` |  |

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `authorization-authorization-cancellation-event-1` | https://developers.pismo.io/events/docs/authorization-authorization-cancellation-event-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;202;400;404;409;500`, has examples `True`, emits events `1`, deprecated `False`.

Guides that link to this operation: `KU-EVT-payments-data-events`, `KU-PAY-force-operation`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/ErrorModel -->
### Schema `ErrorModel`

Pointer: `#/components/schemas/ErrorModel`. Type: object (schema `ErrorModel`).

> API generic returned error.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `error_code` | string | no | Error code. | deprecated: true |
| `code` | string | no | Error code. |  |
| `message` | string | no | Error description. |  |

<!-- schema: #/components/schemas/TrackingIdAlreadyInUseResponse -->
### Schema `TrackingIdAlreadyInUseResponse`

Pointer: `#/components/schemas/TrackingIdAlreadyInUseResponse`. Type: object (schema `TrackingIdAlreadyInUseResponse`).

> Tracking ID already in use error object.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `error_code` | string | no | Error code. | deprecated: true; example: "WP2P0010" |
| `code` | string | no | Error code. | example: "WP2P0010" |
| `message` | string | no | Error description. | example: "Tracking ID already in use" |
| `authorizations` | array of object (schema `Authorization`) | no |  |  |

<!-- schema: #/components/schemas/CancelForceTrackingIdAlreadyInUseResponse -->
### Schema `CancelForceTrackingIdAlreadyInUseResponse`

Pointer: `#/components/schemas/CancelForceTrackingIdAlreadyInUseResponse`. Type: object (schema `CancelForceTrackingIdAlreadyInUseResponse`).

> Tracking ID has already in use error object.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `authorization_id` | integer | no | Authorization ID of the previously generated cancellation operation. | format: "int64"; example: 15301234 |
| `event_date` | string | no | Date and time of the previous cancellation authorization, in the UTC-0 (RFC3339) format. | format: "date-time"; example: "2020-01-02T15:14:00.218Z" |
| `tracking_id` | string | no | Unique identifier for the previous cancellation authorization. | example: "82766158-514c-42f0-87e2-1bb3250c6dee" |

<!-- schema: #/components/schemas/Authorization -->
### Schema `Authorization`

Pointer: `#/components/schemas/Authorization`. Type: object (schema `Authorization`).

> Authorization object.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `authorization_id` | integer | no | Generated authorization ID. | format: "int64"; example: 16397984 |
| `response_code` | string | no | Operation status code. | example: "00" |
| `amount` | number | no | Credited or debited amount. | format: "float"; example: 12.13 |
| `date` | string | no | Authorization date/time in UTC-0 (RFC3339) format. | format: "date-time"; example: "2020-01-02T15:14:00.218Z" |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Core_platform_-_Payment_methods.yaml` | tag `Force operations`: POST /payments/v1/payments/force, POST /payments/v1/payments/force/cancel | https://github.com/PismoDevEx/pismo-api-specs | `9b02c87b6e39a1c8…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-CARD-full-balance-versus-zero-balance` — Full balance versus Zero balance integration
- `KU-ERR-codes-acq-to-esma` — Error codes: ACQ to ESMA (32 prefixes)
- `KU-ERR-codes-wiac-to-wstm` — Error codes: WIAC to WSTM (9 prefixes)
- `KU-EVT-catalogue-other-domains` — Event catalogue: other event domains (accounting, authorization, availables, average, bulletin, cash, delinquent, fraud, instantpay, intl, ledger, networktransactions, onboarding, orgs, payment, platform, programs, rules, savings, statement)
- `KU-EVT-payments-data-events` — Core platform - Payments
- `KU-PAY-force-operation` — Force operation
- `KU-PAY-installments-payment` — Installments payment
