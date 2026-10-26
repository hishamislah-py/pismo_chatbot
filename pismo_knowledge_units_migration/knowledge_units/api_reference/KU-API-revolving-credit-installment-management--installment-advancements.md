---
ku_id: KU-API-revolving-credit-installment-management--installment-advancements
title: 'API reference: Revolving credit - Installment management — Installment advancements'
category: api_reference
ku_type: api_reference
lifecycle: current
sources:
- path: api-specs/Revolving_credit_-_Installment_management.yaml
  sha256: 1a735b324f2927f966984801891fd29894e1fe67abeeebc38d0bb02eb465ab9c
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
- CreateInstallmentAdvancementV2
- GetInstallmentAdvancementV2ById
- cancelInstallmentAdvanceV2
- CreateInstallmentAdvancement
- GetIntallmentAdvancementById
- CancelInstallmentAdvancement
related_kus:
- KU-CRED-installment-advancements-guide
- KU-ERR-codes-esmg-to-whis
- KU-ERR-codes-ex
- KU-EVT-catalogue-balance
- KU-LIFE-api-endpoint-deprecation-and-removal-schedule
specification_version: 1.0.0
---

# API reference: Revolving credit - Installment management — Installment advancements

**KU ID:** `KU-API-revolving-credit-installment-management--installment-advancements` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 6 operation(s) tagged `Installment advancements` in `api-specs/Revolving_credit_-_Installment_management.yaml` (“Revolving credit - Installment management”, version `1.0.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Endpoints to manage installment advancements

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `POST /v2/accounts/{accountId}/installment-advance` | `CreateInstallmentAdvancementV2` | Create installment advancement | no |
| `GET /v2/accounts/{accountId}/installment-advance/{advancementId}` | `GetInstallmentAdvancementV2ById` | Get installment advancement | no |
| `DELETE /v2/accounts/{accountId}/installment-advance/{advancementId}` | `cancelInstallmentAdvanceV2` | Cancel installment advancement | no |
| `POST /v1/accounts/{accountId}/installment-advance` | `CreateInstallmentAdvancement` | Create installment advancement (deprecated) | **yes** |
| `GET /v1/accounts/{accountId}/installment-advance/{advancementId}` | `GetIntallmentAdvancementById` | Get installment advancement (deprecated) | **yes** |
| `DELETE /v1/accounts/{accountId}/installment-advance/{advancementId}` | `CancelInstallmentAdvancement` | Cancel installment advancement (deprecated) | **yes** |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"} — Account access token. Tokens can expire quickly, which can result in an "Unauthorized" error.

## Operation contracts

<!-- op: spec=api-specs/Revolving_credit_-_Installment_management.yaml method=POST path=/v2/accounts/{accountId}/installment-advance operationId=CreateInstallmentAdvancementV2 -->
### `POST /v2/accounts/{accountId}/installment-advance` — Create installment advancement

- **operationId:** `CreateInstallmentAdvancementV2`
- **Specification:** `api-specs/Revolving_credit_-_Installment_management.yaml` (Revolving credit - Installment management)
- **Server base URL(s):** `https://sandbox.pismolabs.io/installment-management`
- **Tags:** `Installment advancements`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Creates an installment advancement for an account. An installment advancement moves one or more future installments to the current cycle.
>
> This version supports two advancement modes:
>
> **ALL_CONTRACTS mode**: Advances all future installments for all installment agreements in the account. When using this mode:
> - Set `condition` to `ALL_CONTRACTS`.
> - The `calculator`, `reschedule`, and `remove_interest_from_current` fields are required at the root level.
> - The `contracts` array should <i>not</i> be passed.
>
> **MULTIPLE_CONTRACTS mode**: Advances installments for specific contracts with individual configurations. When using this mode:
> - Set `condition` to `MULTIPLE_CONTRACTS`.
> - Provide a `contracts` array with individual contract configurations.
> - Root-level `calculator`, `reschedule`, and `remove_interest_from_current` fields must not be passed.
>
> When you advance installments, you must specify what to do with the interest. You have three options:
> 1. To remove 100% of the interest on the advanced installment(s), set the `remove_interest_from_current` field to `true` and the `calculator` field to `REMOVE_ALL_INTEREST`.
> 2. To advance 100% of the interest on the advanced installment(s), set `remove_interest_from_current` to `false` and set `calculator` to `NONE`.
> 3. To recalculate the interest applied to the advanced installment(s), set `calculator` to `PRESENT_VALUE`. You can set the `remove_interest_from_current` field  to either `true` or `false`. If `true`, the system recalculates interest on installments that were already in the current cycle (and did not need to be advanced). Otherwise, interest on those installments remains unchanged.
> For more information, refer to [Installment advancements](doc:installment-management#installment-advancements) and [Creating an installment advancment](doc:installment-management#creating-an-installment-advancement).
>
> This endpoint triggers an async process in which the transactions are advanced as requested.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `accountId` | path | yes | integer | Account ID | format: "int64"; example: 6912345 |
| `x-cid` | header | no | string | The Correlation Identifier field is used to link related API requests and events. The x-cid can help the Pismo engineering team track everything related to a call. You can find the x-cid field in the response header from an API endpoint call. If this field isn't passed, one is automatically generated. | example: "5bb05174-4e80-11ea-b77f-2e728ce88125" |

#### Request body

Required: yes

**Content type `application/json`** — schema: object (schema `CreateInstallmentAdvancedV2RequestDto`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `condition` | string (schema `ConditionV2`) | yes | Installments should be advanced for all the contracts for an account (`ALL_CONTRACTS`) or for multiple specific contracts (`MULTIPLE_CONTRACTS`).<br> | enum: ["MULTIPLE_CONTRACTS", "ALL_CONTRACTS"]; example: "MULTIPLE_CONTRACTS" |
| `tracking_id` | string (schema `TrackingIdForPost`) | yes | Tracking ID. A client-supplied tracking ID that can be used to keep track of an advancement. Must consist of the characters [a-z,A-Z,0-9,-,:] with a range from 1 to 128.<br><br>**Note:** For a given account ID, the tracking ID must be unique. You cannot reuse the same tracking ID in another call to this endpoint, even if the earlier call returned an error, unless you use a different account ID.<br> | example: "3ea22692-a209-11eb-89a2-f73e179dcbc2" |
| `calculator` | string (schema `Calculator`) | no | Type of calculation to apply. Default is `NONE`.<br> | enum: ["PRESENT_VALUE", "REMOVE_ALL_INTEREST", "NONE"]; example: "PRESENT_VALUE" |
| `reschedule` | string (schema `Reschedule`) | no | Reschedule mode to apply. Must be `ADVANCEMENT`.<br> | enum: ["ADVANCEMENT"]; example: "ADVANCEMENT" |
| `remove_interest_from_current` | boolean (schema `RemoveInterestFromCurrent`) | no | Whether interest should be removed when an installment is advanced. | default: false; example: false |
| `interest_removal_end_date` | string (schema `InterestRemovalEndDate`) | no | Cutoff date used for interest recalculation when `calculator` is `PRESENT_VALUE`.<br>Reflects the value passed in the request. `null` if not passed. Format = yyyy-mm-dd.<br> | format: "date"; example: "2021-04-14" |
| `contracts` | array of object (schema `ContractAdvancementDto`) | no | Array of contract advancement configurations (required for `MULTIPLE_CONTRACTS` condition) |  |

Example `all_contracts` (Advance all contracts):

```json
{
  "condition": "ALL_CONTRACTS",
  "tracking_id": "3ea22692-a209-11eb-89a2-f73e179dcbc2",
  "calculator": "PRESENT_VALUE",
  "reschedule": "ADVANCEMENT",
  "remove_interest_from_current": false
}
```

Example `multiple_contracts` (Advance multiple specific contracts):

```json
{
  "condition": "MULTIPLE_CONTRACTS",
  "tracking_id": "3ea22692-a209-11eb-89a2-f73e179dcbc2",
  "contracts": [
    {
      "remove_interest_from_current": false,
      "authorization_id": 12345,
      "number_of_installments": 3,
      "calculator": "PRESENT_VALUE",
      "reschedule": "ADVANCEMENT"
    },
    {
      "remove_interest_from_current": true,
      "authorization_id": 67890,
      "number_of_installments": 2,
      "calculator": "NONE",
      "reschedule": "ADVANCEMENT"
    }
  ]
}
```

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 202 | Accepted | `application/json`: object (schema `CreateInstallmentAdvancedV2ResponseDto`) |
| 400 | Bad request | `application/json`: object (schema `StandardErrorResponse`) |
| 409 | Conflict | `application/json`: object (schema `StandardErrorResponse`) |
| 500 | Internal server error | `application/json`: object (schema `StandardErrorResponse`) |

##### Response 202

**202 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | integer (schema `AdvancementId`) | no | Advancement ID | format: "int64"; example: 67854328 |
| `condition` | string (schema `ConditionV2`) | no | Installments should be advanced for all the contracts for an account (`ALL_CONTRACTS`) or for multiple specific contracts (`MULTIPLE_CONTRACTS`).<br> | enum: ["MULTIPLE_CONTRACTS", "ALL_CONTRACTS"]; example: "MULTIPLE_CONTRACTS" |
| `tracking_id` | string (schema `TrackingID`) | no | Tracking ID. A client-supplied tracking ID that can be used to keep track of an advancement. Must consist of the characters [a-z,A-Z,0-9,-,:] with a range from 1 to 128. | example: "3ea22692-a209-11eb-89a2-f73e179dcbc2" |
| `calculator` | string (schema `Calculator`) | no | Type of calculation to apply. Default is `NONE`.<br> | enum: ["PRESENT_VALUE", "REMOVE_ALL_INTEREST", "NONE"]; example: "PRESENT_VALUE" |
| `reschedule` | string (schema `Reschedule`) | no | Reschedule mode to apply. Must be `ADVANCEMENT`.<br> | enum: ["ADVANCEMENT"]; example: "ADVANCEMENT" |
| `remove_interest_from_current` | boolean (schema `RemoveInterestFromCurrent`) | no | Whether interest should be removed when an installment is advanced. | default: false; example: false |
| `number_of_installments` | integer (schema `NumberOfInstallmentsToAdvance`) | no | Number of installments to advance<br><br>This field is **REQUIRED** if `contract_condition` is set to `SPECIFIC_NUMBER_OF_INSTALLMENTS`. If `contract_condition` is set to `ALL_CONTRACTS`, this field is ignored.<br> | format: "int32"; example: 3 |
| `created_at` | string (schema `CreatedAt`) | no | Date/time advancement was created. Format = yyyy-mm-dd:hr:mm:ss. | format: "date-time"; example: "2021-04-14T12:00:00-03:00" |
| `updated_at` | string (schema `UpdatedAt`) | no | Date/time advancement was last updated. Format = yyyy-mm-dd:hr:mm:ss. | format: "date-time"; example: "2025-09-01T10:05:00" |
| `cancelled_at` | string (schema `CanceledAt`) | no | Date/time advancement was canceled. Format = yyyy-mm-dd:hr:mm:ss. | format: "date-time"; example: "2021-04-14T12:00:00-03:00" |
| `contracts` | array of object (schema `ContractAdvancementResponseDto`) | no | Array of contract advancement configurations (present for `MULTIPLE_CONTRACTS` condition) |  |
| `installments` | array of object (schema `InstallmentResponseDto`) | no | Array of installment details |  |
| `error_message` | string (schema `AdvancementErrorMessage`) | no | Error message if advancement failed | example: "Operation error" |
| `status` | string (schema `AdvancementStatus`) | no | Current status of the advancement | enum: ["CREATED", "PROCESSED", "CANCELLED", "ERROR", "CANCELLATION_ERROR"]; example: "PROCESSED" |

##### Response 400

400 Example `Missing request header`:

```json
{
  "code": "EX0002",
  "message": "Missing request header for method parameter of type String"
}
```

##### Response 409

409 Example `Account conflict`:

```json
{
  "message": "Installment advance already exists with this Account_ID and Tracking_ID."
}
```

##### Response 500

500 Example `Internal Server Error`:

```json
{
  "code": "GN0001",
  "message": "Service is unavailable"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `EX0002` | Missing request header for method parameter of type String |
| 500 | `GN0001` | Service is unavailable |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `202;400;409;500`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-CRED-installment-advancements-guide`, `KU-LIFE-api-endpoint-deprecation-and-removal-schedule`.

<!-- op: spec=api-specs/Revolving_credit_-_Installment_management.yaml method=GET path=/v2/accounts/{accountId}/installment-advance/{advancementId} operationId=GetInstallmentAdvancementV2ById -->
### `GET /v2/accounts/{accountId}/installment-advance/{advancementId}` — Get installment advancement

- **operationId:** `GetInstallmentAdvancementV2ById`
- **Specification:** `api-specs/Revolving_credit_-_Installment_management.yaml` (Revolving credit - Installment management)
- **Server base URL(s):** `https://sandbox.pismolabs.io/installment-management`
- **Tags:** `Installment advancements`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Retrieves an installment advancement by its ID. This endpoint provides enhanced response data including:
>
> - Detailed advancement information with status tracking
> - Contract-specific configurations for MULTIPLE_CONTRACTS mode
> - Enhanced metadata including creation, update, and cancellation timestamps
> - Error messages when applicable
>
> The response format differs based on the advancement condition.
> - **ALL_CONTRACTS**: Returns root-level calculator, reschedule settings, and no contracts array.
> - **MULTIPLE_CONTRACTS**: Returns individual contract configurations in the contracts array.
>
> This endpoint includes additional fields like `cancelled_at`, `error_message`, `status`, and `contracts`.
>
> <BetaComponent />

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `accountId` | path | yes | integer | Account ID | format: "int64"; example: 6912345 |
| `x-cid` | header | no | string | The Correlation Identifier field is used to link related API requests and events. The x-cid can help the Pismo engineering team track everything related to a call. You can find the x-cid field in the response header from an API endpoint call. If this field isn't passed, one is automatically generated. | example: "5bb05174-4e80-11ea-b77f-2e728ce88125" |
| `advancementId` | path | yes | integer | Advancement ID | format: "int64"; example: 6912345 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `GetInstallmentAdvanceV2ResponseDto`) |
| 400 | Bad request | `application/json`: object (schema `StandardErrorResponse`) |
| 404 | Not Found | `application/json`: object (schema `StandardErrorResponse`) |
| 500 | Internal server error | `application/json`: object (schema `StandardErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | integer (schema `AdvancementId`) | no | Advancement ID | format: "int64"; example: 67854328 |
| `condition` | string (schema `ConditionV2`) | no | Installments should be advanced for all the contracts for an account (`ALL_CONTRACTS`) or for multiple specific contracts (`MULTIPLE_CONTRACTS`).<br> | enum: ["MULTIPLE_CONTRACTS", "ALL_CONTRACTS"]; example: "MULTIPLE_CONTRACTS" |
| `tracking_id` | string (schema `TrackingID`) | no | Tracking ID. A client-supplied tracking ID that can be used to keep track of an advancement. Must consist of the characters [a-z,A-Z,0-9,-,:] with a range from 1 to 128. | example: "3ea22692-a209-11eb-89a2-f73e179dcbc2" |
| `calculator` | string (schema `Calculator`) | no | Type of calculation to apply. Default is `NONE`.<br> | enum: ["PRESENT_VALUE", "REMOVE_ALL_INTEREST", "NONE"]; example: "PRESENT_VALUE" |
| `reschedule` | string (schema `Reschedule`) | no | Reschedule mode to apply. Must be `ADVANCEMENT`.<br> | enum: ["ADVANCEMENT"]; example: "ADVANCEMENT" |
| `remove_interest_from_current` | boolean (schema `RemoveInterestFromCurrent`) | no | Whether interest should be removed when an installment is advanced. | default: false; example: false |
| `number_of_installments` | integer (schema `NumberOfInstallmentsToAdvance`) | no | Number of installments to advance<br><br>This field is **REQUIRED** if `contract_condition` is set to `SPECIFIC_NUMBER_OF_INSTALLMENTS`. If `contract_condition` is set to `ALL_CONTRACTS`, this field is ignored.<br> | format: "int32"; example: 3 |
| `created_at` | string (schema `CreatedAt`) | no | Date/time advancement was created. Format = yyyy-mm-dd:hr:mm:ss. | format: "date-time"; example: "2021-04-14T12:00:00-03:00" |
| `updated_at` | string (schema `UpdatedAt`) | no | Date/time advancement was last updated. Format = yyyy-mm-dd:hr:mm:ss. | format: "date-time"; example: "2025-09-01T10:05:00" |
| `cancelled_at` | string (schema `CanceledAt`) | no | Date/time advancement was canceled. Format = yyyy-mm-dd:hr:mm:ss. | format: "date-time"; example: "2021-04-14T12:00:00-03:00" |
| `contracts` | array of object (schema `ContractAdvancementResponseDto`) | no | Array of contract advancement configurations (present for `MULTIPLE_CONTRACTS` condition) |  |
| `installments` | array of object (schema `InstallmentResponseDto`) | no | Array of installment details |  |
| `error_message` | string (schema `AdvancementErrorMessage`) | no | Error message if advancement failed | example: "Operation error" |
| `status` | string (schema `AdvancementStatus`) | no | Current status of the advancement | enum: ["CREATED", "PROCESSED", "CANCELLED", "ERROR", "CANCELLATION_ERROR"]; example: "PROCESSED" |

200 Example `all_contracts_processed` (ALL_CONTRACTS advancement (processed)):

```json
{
  "id": 1,
  "condition": "ALL_CONTRACTS",
  "tracking_id": "3ea22692-a209-11eb-89a2-f73e179dcbc2",
  "calculator": "PRESENT_VALUE",
  "reschedule": "ADVANCEMENT",
  "remove_interest_from_current": false,
  "number_of_installments": 5,
  "created_at": "2025-09-01T10:00:00",
  "updated_at": "2025-09-01T10:05:00",
  "status": "PROCESSED",
  "installments": [
    {
      "id": 12345,
      "new_amount": 150,
      "old_amount": 155,
      "new_interest_amount": 15,
      "old_interest_amount": 17.5,
      "new_statement_id": 1,
      "old_statement_id": 3
    }
  ]
}
```

200 Example `multiple_contracts_processed` (MULTIPLE_CONTRACTS advancement (processed)):

```json
{
  "id": 2,
  "condition": "MULTIPLE_CONTRACTS",
  "tracking_id": "3ea22692-a209-11eb-89a2-f73e179dcbc2",
  "remove_interest_from_current": false,
  "created_at": "2025-09-01T11:00:00",
  "updated_at": "2025-09-01T11:05:00",
  "status": "PROCESSED",
  "contracts": [
    {
      "remove_interest_from_current": false,
      "authorization_id": 12345,
      "number_of_installments": 3,
      "calculator": "PRESENT_VALUE",
      "reschedule": "ADVANCEMENT"
    },
    {
      "remove_interest_from_current": true,
      "authorization_id": 67890,
      "number_of_installments": 2,
      "calculator": "NONE",
      "reschedule": "ADVANCEMENT"
    }
  ],
  "installments": [
    {
      "id": 12346,
      "new_amount": 200,
      "old_amount": 210,
      "new_interest_amount": 20,
      "old_interest_amount": 25,
      "new_statement_id": 1,
      "old_statement_id": 4
    },
    {
      "id": 12347,
      "new_amount": 100,
      "old_amount": 100,
      "new_interest_amount": 0,
      "old_interest_amount": 10,
      "new_statement_id": 1,
      "old_statement_id": 5
    }
  ]
}
```

200 Example `cancelled_advancement` (Cancelled advancement):

```json
{
  "id": 3,
  "condition": "ALL_CONTRACTS",
  "tracking_id": "3ea22692-a209-11eb-89a2-f73e179dcbc2",
  "calculator": "PRESENT_VALUE",
  "reschedule": "ADVANCEMENT",
  "remove_interest_from_current": false,
  "number_of_installments": 2,
  "created_at": "2025-09-01T12:00:00",
  "updated_at": "2025-09-01T12:30:00",
  "cancelled_at": "2025-09-01T12:30:00",
  "status": "CANCELLED",
  "error_message": "Operation error"
}
```

##### Response 400

400 Example `Missing request header`:

```json
{
  "code": "EX0002",
  "message": "Missing request header for method parameter of type String"
}
```

##### Response 404

404 Example `Installment advance not found`:

```json
{
  "code": "EX307",
  "message": "Installment advancement AdvancementID for account accountID not found."
}
```

##### Response 500

500 Example `Internal Server Error`:

```json
{
  "code": "GN0001",
  "message": "Service is unavailable"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `EX0002` | Missing request header for method parameter of type String |
| 404 | `EX307` | Installment advancement AdvancementID for account accountID not found. |
| 500 | `GN0001` | Service is unavailable |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;404;500`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-LIFE-api-endpoint-deprecation-and-removal-schedule`.

<!-- op: spec=api-specs/Revolving_credit_-_Installment_management.yaml method=DELETE path=/v2/accounts/{accountId}/installment-advance/{advancementId} operationId=cancelInstallmentAdvanceV2 -->
### `DELETE /v2/accounts/{accountId}/installment-advance/{advancementId}` — Cancel installment advancement

- **operationId:** `cancelInstallmentAdvanceV2`
- **Specification:** `api-specs/Revolving_credit_-_Installment_management.yaml` (Revolving credit - Installment management)
- **Server base URL(s):** `https://sandbox.pismolabs.io/installment-management`
- **Tags:** `Installment advancements`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Cancel an installment advancement.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `accountId` | path | yes | integer | Account ID | format: "int64"; example: 6912345 |
| `advancementId` | path | yes | integer | Advancement ID | format: "int64"; example: 6912345 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Installment advance canceled successfully | `application/json`: object (schema `CancellationInstallmentAdvancedV2ResponseDto`) |
| 400 | Bad request | `application/json`: object (schema `StandardErrorResponse`) |
| 404 | Not Found | `application/json`: object (schema `StandardErrorResponse`) |
| 500 | Internal server error | `application/json`: object (schema `StandardErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | integer (schema `AdvancementId`) | no | Unique identifier for the installment advancement cancellation. | format: "int64"; example: 67854328 |
| `condition` | string (schema `ConditionV2`) | no | The condition of the installment advancement | enum: ["MULTIPLE_CONTRACTS", "ALL_CONTRACTS"]; example: "MULTIPLE_CONTRACTS" |
| `tracking_id` | string (schema `TrackingID`) | no | Identifier used to track the cancellation request. | example: "3ea22692-a209-11eb-89a2-f73e179dcbc2" |
| `calculator` | string (schema `Calculator`) | no | Details about the calculation performed for the cancellation. | enum: ["PRESENT_VALUE", "REMOVE_ALL_INTEREST", "NONE"]; example: "PRESENT_VALUE" |
| `reschedule` | string (schema `Reschedule`) | no | Information about any rescheduling related to the cancellation. | enum: ["ADVANCEMENT"]; example: "ADVANCEMENT" |
| `remove_interest_from_current` | boolean (schema `RemoveInterestFromCurrent`) | no | Indicates whether interest should be removed from the current statement as part of the cancellation. | default: false; example: false |
| `contracts` | array of object (schema `ContractAdvancementResponseDto`) | no | List of contract details affected by the installment advancement cancellation. |  |

##### Response 400

400 Example `Missing request header`:

```json
{
  "code": "EX0002",
  "message": "Missing request header for method parameter of type String"
}
```

##### Response 404

404 Example `Installment advance not found`:

```json
{
  "code": "EX307",
  "message": "Installment advancement AdvancementID for account accountID not found."
}
```

##### Response 500

500 Example `Internal Server Error`:

```json
{
  "code": "GN0001",
  "message": "Service is unavailable"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `EX0002` | Missing request header for method parameter of type String |
| 404 | `EX307` | Installment advancement AdvancementID for account accountID not found. |
| 500 | `GN0001` | Service is unavailable |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;404;500`, has examples `False`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-LIFE-api-endpoint-deprecation-and-removal-schedule`.

<!-- op: spec=api-specs/Revolving_credit_-_Installment_management.yaml method=POST path=/v1/accounts/{accountId}/installment-advance operationId=CreateInstallmentAdvancement -->
### `POST /v1/accounts/{accountId}/installment-advance` — Create installment advancement (deprecated)

- **operationId:** `CreateInstallmentAdvancement`
- **Specification:** `api-specs/Revolving_credit_-_Installment_management.yaml` (Revolving credit - Installment management)
- **Server base URL(s):** `https://sandbox.pismolabs.io/installment-management`
- **Tags:** `Installment advancements`
- **Deprecated in specification:** **yes**
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Create an installment advancement for an account. This is a DEPRECATED endpoint. Use the non-deprecated [Create installment advancement](ref:createinstallmentadvancementv2) endpoint instead.<br>
> An installment advancement moves one or more future installments to the current cycle.
>
> To advance installments for a specific installment agreement (contract), set the `condition` field to `SINGLE_CONTRACT`, and set the `transaction_id` field to the transaction ID of any of the installments in the installment agreement. Specify the number of installments to advance in the `number_of_installments_to_advance` field. Installments are advanced starting with the last scheduled installment in the agreement and working backwards from there.
>
> To advance <b>all</b> future installments for <b>all</b> installment agreements in the account, set the `condition` field to `ALL_CONTRACTS`. (In this case, the `number_of_installments_to_advance` field is ignored.)
>
> When you advance installments, you must specify what to do with the interest. You have three options:
> 1. To remove 100% of the interest on the advanced installment(s), set the `remove_interest_from_current` field to `true` and the `calculator` field to `REMOVE_ALL_INTEREST`.
> 2. To advance 100% of the interest on the advanced installment(s), set `remove_interest_from_current` to `false` and set `calculator` to `NONE`.
> 3. To recalculate the interest applied to the advanced installment(s), set `calculator` to `PRESENT_VALUE`. You can set the `remove_interest_from_current` field  to either `true` or `false`. If `true`, the system recalculates interest on installments that were already in the current cycle (and did not need to be advanced). Otherwise, interest on those installments remains unchanged.
> For more information, refer to [Installment advancements](doc:installment-management#installment-advancements) and [Creating an installment advancment](doc:installment-management#creating-an-installment-advancement).
>
> This endpoint generates an <a href='https://developers.pismo.io/events/docs/balance-installment-advancement-1'>Installment advanced</a> event.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `accountId` | path | yes | integer | Account ID | format: "int64"; example: 6912345 |
| `x-cid` | header | no | string | The Correlation Identifier field is used to link related API requests and events. The x-cid can help the Pismo engineering team track everything related to a call. You can find the x-cid field in the response header from an API endpoint call. If this field isn't passed, one is automatically generated. | example: "5bb05174-4e80-11ea-b77f-2e728ce88125" |

#### Request body

Required: yes

**Content type `application/json`** — schema: object (schema `CreateInstallmentAdvancedRequestDto`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `transaction_id` | integer (schema `TransactionID`) | no | Transaction ID | format: "int64"; example: 98457355 |
| `tracking_id` | string (schema `TrackingIdForPost`) | no | Tracking ID. A client-supplied tracking ID that can be used to keep track of an advancement. Must consist of the characters [a-z,A-Z,0-9,-,:] with a range from 1 to 128.<br><br>**Note:** For a given account ID, the tracking ID must be unique. You cannot reuse the same tracking ID in another call to this endpoint, even if the earlier call returned an error, unless you use a different account ID.<br> | example: "3ea22692-a209-11eb-89a2-f73e179dcbc2" |
| `condition` | string (schema `Condition`) | no | Installments should be advanced for all the contracts for an account (`ALL_CONTRACTS`) or for a specific contract (`SINGLE_CONTRACT`).<br>If `condition` is set to `SINGLE_CONTRACT`, then the `transaction_id` field must be set to the transaction ID of the specific contract.<br> | enum: ["SINGLE_CONTRACT", "ALL_CONTRACTS"]; example: "SINGLE_CONTRACT" |
| `remove_interest_from_current` | boolean (schema `RemoveInterestFromCurrent`) | no | Whether interest should be removed when an installment is advanced. | default: false; example: false |
| `calculator` | string (schema `Calculator`) | no | Type of calculation to apply. Default is `NONE`.<br> | enum: ["PRESENT_VALUE", "REMOVE_ALL_INTEREST", "NONE"]; example: "PRESENT_VALUE" |
| `reschedule` | string (schema `Reschedule`) | no | Reschedule mode to apply. Must be `ADVANCEMENT`.<br> | enum: ["ADVANCEMENT"]; example: "ADVANCEMENT" |
| `number_of_installments_to_advance` | integer (schema `NumberOfInstallmentsToAdvance`) | no | Number of installments to advance<br><br>This field is **REQUIRED** if `contract_condition` is set to `SPECIFIC_NUMBER_OF_INSTALLMENTS`. If `contract_condition` is set to `ALL_CONTRACTS`, this field is ignored.<br> | format: "int32"; example: 3 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 202 | OK | `application/json`: object (schema `CreateInstallmentAdvancedResponseDto`) |
| 400 | Bad request | `application/json`: object (schema `StandardErrorResponse`) |
| 409 | Conflict | `application/json`: object (schema `StandardErrorResponse`) |
| 500 | Internal server error | `application/json`: object (schema `StandardErrorResponse`) |

##### Response 202

**202 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `advancement_id` | integer (schema `AdvancementId`) | no | Advancement ID | format: "int64"; example: 67854328 |
| `tracking_id` | string (schema `TrackingID`) | no | Tracking ID. A client-supplied tracking ID that can be used to keep track of an advancement. Must consist of the characters [a-z,A-Z,0-9,-,:] with a range from 1 to 128. | example: "3ea22692-a209-11eb-89a2-f73e179dcbc2" |
| `created_at` | string (schema `CreatedAt`) | no | Date/time advancement was created. Format = yyyy-mm-dd:hr:mm:ss. | format: "date-time"; example: "2021-04-14T12:00:00-03:00" |
| `accountId` | integer (schema `AccountID`) | no | Account ID | format: "int64"; example: 67854328 |
| `condition` | string (schema `Condition`) | no | Installments should be advanced for all the contracts for an account (`ALL_CONTRACTS`) or for a specific contract (`SINGLE_CONTRACT`).<br>If `condition` is set to `SINGLE_CONTRACT`, then the `transaction_id` field must be set to the transaction ID of the specific contract.<br> | enum: ["SINGLE_CONTRACT", "ALL_CONTRACTS"]; example: "SINGLE_CONTRACT" |
| `calculator` | string (schema `Calculator`) | no | Type of calculation to apply. Default is `NONE`.<br> | enum: ["PRESENT_VALUE", "REMOVE_ALL_INTEREST", "NONE"]; example: "PRESENT_VALUE" |
| `reschedule` | string (schema `Reschedule`) | no | Reschedule mode to apply. Must be `ADVANCEMENT`.<br> | enum: ["ADVANCEMENT"]; example: "ADVANCEMENT" |
| `installments` | array of object (schema `InstallmentResponseDto`) | no |  |  |

##### Response 400

400 Example `Missing request header`:

```json
{
  "code": "EX0002",
  "message": "Missing request header for method parameter of type String"
}
```

##### Response 409

409 Example `Account conflict`:

```json
{
  "message": "Installment advance already exists with this Account_ID and Tracking_ID."
}
```

##### Response 500

500 Example `Internal Server Error`:

```json
{
  "code": "GN0001",
  "message": "Service is unavailable"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `EX0002` | Missing request header for method parameter of type String |
| 500 | `GN0001` | Service is unavailable |

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `balance-installment-advancement-1` | https://developers.pismo.io/events/docs/balance-installment-advancement-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `202;400;409;500`, has examples `False`, emits events `1`, deprecated `True`.

<!-- op: spec=api-specs/Revolving_credit_-_Installment_management.yaml method=GET path=/v1/accounts/{accountId}/installment-advance/{advancementId} operationId=GetIntallmentAdvancementById -->
### `GET /v1/accounts/{accountId}/installment-advance/{advancementId}` — Get installment advancement (deprecated)

- **operationId:** `GetIntallmentAdvancementById`
- **Specification:** `api-specs/Revolving_credit_-_Installment_management.yaml` (Revolving credit - Installment management)
- **Server base URL(s):** `https://sandbox.pismolabs.io/installment-management`
- **Tags:** `Installment advancements`
- **Deprecated in specification:** **yes**
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Get an installment advancement by its ID. This is a DEPRECATED endpoint. Use the non-deprecated [Get installment advancement](ref:getinstallmentadvancementv2byid) endpoint instead.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `accountId` | path | yes | integer | Account ID | format: "int64"; example: 6912345 |
| `x-cid` | header | no | string | The Correlation Identifier field is used to link related API requests and events. The x-cid can help the Pismo engineering team track everything related to a call. You can find the x-cid field in the response header from an API endpoint call. If this field isn't passed, one is automatically generated. | example: "5bb05174-4e80-11ea-b77f-2e728ce88125" |
| `advancementId` | path | yes | integer | Advancement ID | format: "int64"; example: 6912345 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `GetInstallmentAdvancedResponseDto`) |
| 400 | Bad request | `application/json`: object (schema `StandardErrorResponse`) |
| 500 | Internal server error | `application/json`: object (schema `StandardErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `advancement_id` | integer (schema `AdvancementId`) | no | Advancement ID | format: "int64"; example: 67854328 |
| `tracking_id` | string (schema `TrackingID`) | no | Tracking ID. A client-supplied tracking ID that can be used to keep track of an advancement. Must consist of the characters [a-z,A-Z,0-9,-,:] with a range from 1 to 128. | example: "3ea22692-a209-11eb-89a2-f73e179dcbc2" |
| `created_at` | string (schema `CreatedAt`) | no | Date/time advancement was created. Format = yyyy-mm-dd:hr:mm:ss. | format: "date-time"; example: "2021-04-14T12:00:00-03:00" |
| `cancelled_at` | string (schema `CanceledAt`) | no | Date/time advancement was canceled. Format = yyyy-mm-dd:hr:mm:ss. | format: "date-time"; example: "2021-04-14T12:00:00-03:00" |
| `accountId` | integer (schema `AccountID`) | no | Account ID | format: "int64"; example: 67854328 |
| `condition` | string (schema `Condition`) | no | Installments should be advanced for all the contracts for an account (`ALL_CONTRACTS`) or for a specific contract (`SINGLE_CONTRACT`).<br>If `condition` is set to `SINGLE_CONTRACT`, then the `transaction_id` field must be set to the transaction ID of the specific contract.<br> | enum: ["SINGLE_CONTRACT", "ALL_CONTRACTS"]; example: "SINGLE_CONTRACT" |
| `calculator` | string (schema `Calculator`) | no | Type of calculation to apply. Default is `NONE`.<br> | enum: ["PRESENT_VALUE", "REMOVE_ALL_INTEREST", "NONE"]; example: "PRESENT_VALUE" |
| `reschedule` | string (schema `Reschedule`) | no | Reschedule mode to apply. Must be `ADVANCEMENT`.<br> | enum: ["ADVANCEMENT"]; example: "ADVANCEMENT" |
| `number_of_installments_to_advance` | integer (schema `NumberOfInstallmentsToAdvance`) | no | Number of installments to advance<br><br>This field is **REQUIRED** if `contract_condition` is set to `SPECIFIC_NUMBER_OF_INSTALLMENTS`. If `contract_condition` is set to `ALL_CONTRACTS`, this field is ignored.<br> | format: "int32"; example: 3 |
| `installments` | array of object (schema `InstallmentResponseDto`) | no |  |  |

##### Response 400

400 Example `Missing request header`:

```json
{
  "code": "EX0002",
  "message": "Missing request header for method parameter of type String"
}
```

##### Response 500

500 Example `Internal Server Error`:

```json
{
  "code": "GN0001",
  "message": "Service is unavailable"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `EX0002` | Missing request header for method parameter of type String |
| 500 | `GN0001` | Service is unavailable |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;500`, has examples `False`, emits events `0`, deprecated `True`.

Guides that link to this operation: `KU-CRED-installment-advancements-guide`.

<!-- op: spec=api-specs/Revolving_credit_-_Installment_management.yaml method=DELETE path=/v1/accounts/{accountId}/installment-advance/{advancementId} operationId=CancelInstallmentAdvancement -->
### `DELETE /v1/accounts/{accountId}/installment-advance/{advancementId}` — Cancel installment advancement (deprecated)

- **operationId:** `CancelInstallmentAdvancement`
- **Specification:** `api-specs/Revolving_credit_-_Installment_management.yaml` (Revolving credit - Installment management)
- **Server base URL(s):** `https://sandbox.pismolabs.io/installment-management`
- **Tags:** `Installment advancements`
- **Deprecated in specification:** **yes**
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Cancel the installment advancement for an account, and return the installments to their original cycles. If necessary, reinstate original interest on the installments.<br>
> This is a DEPRECATED endpoint. Use the non-deprecated [Cancel installment advancement](ref:cancelinstallmentadvancev2) endpoint instead.
>
> This endpoint generates an <a href='https://developers.pismo.io/events/docs/balance-installment-advancement-cancelled-1'>Installment advanced cancelled</a> event.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `accountId` | path | yes | integer | Account ID | format: "int64"; example: 6912345 |
| `x-cid` | header | no | string | The Correlation Identifier field is used to link related API requests and events. The x-cid can help the Pismo engineering team track everything related to a call. You can find the x-cid field in the response header from an API endpoint call. If this field isn't passed, one is automatically generated. | example: "5bb05174-4e80-11ea-b77f-2e728ce88125" |
| `advancementId` | path | yes | integer | Advancement ID | format: "int64"; example: 6912345 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `CancelInstallmentAdvancedResponseDto`) |
| 400 | Bad request | `application/json`: object (schema `StandardErrorResponse`) |
| 409 | Conflict | `application/json`: object (schema `StandardErrorResponse`) |
| 500 | Internal server error | `application/json`: object (schema `StandardErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `advancement_id` | integer (schema `AdvancementId`) | no | Advancement ID | format: "int64"; example: 67854328 |
| `tracking_id` | string (schema `TrackingID`) | no | Tracking ID. A client-supplied tracking ID that can be used to keep track of an advancement. Must consist of the characters [a-z,A-Z,0-9,-,:] with a range from 1 to 128. | example: "3ea22692-a209-11eb-89a2-f73e179dcbc2" |
| `created_at` | string (schema `CreatedAt`) | no | Date/time advancement was created. Format = yyyy-mm-dd:hr:mm:ss. | format: "date-time"; example: "2021-04-14T12:00:00-03:00" |
| `cancelled_at` | string (schema `CanceledAt`) | no | Date/time advancement was canceled. Format = yyyy-mm-dd:hr:mm:ss. | format: "date-time"; example: "2021-04-14T12:00:00-03:00" |
| `accountId` | integer (schema `AccountID`) | no | Account ID | format: "int64"; example: 67854328 |
| `condition` | string (schema `Condition`) | no | Installments should be advanced for all the contracts for an account (`ALL_CONTRACTS`) or for a specific contract (`SINGLE_CONTRACT`).<br>If `condition` is set to `SINGLE_CONTRACT`, then the `transaction_id` field must be set to the transaction ID of the specific contract.<br> | enum: ["SINGLE_CONTRACT", "ALL_CONTRACTS"]; example: "SINGLE_CONTRACT" |
| `calculator` | string (schema `Calculator`) | no | Type of calculation to apply. Default is `NONE`.<br> | enum: ["PRESENT_VALUE", "REMOVE_ALL_INTEREST", "NONE"]; example: "PRESENT_VALUE" |
| `reschedule` | string (schema `Reschedule`) | no | Reschedule mode to apply. Must be `ADVANCEMENT`.<br> | enum: ["ADVANCEMENT"]; example: "ADVANCEMENT" |
| `installments` | array of object (schema `InstallmentResponseDto`) | no |  |  |

##### Response 400

400 Example `Missing request header`:

```json
{
  "code": "EX0002",
  "message": "Missing request header for method parameter of type String"
}
```

##### Response 409

409 Example `Account conflict`:

```json
{
  "message": "Installment advance already exists with this Account_ID and Tracking_ID."
}
```

##### Response 500

500 Example `Internal Server Error`:

```json
{
  "code": "GN0001",
  "message": "Service is unavailable"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `EX0002` | Missing request header for method parameter of type String |
| 500 | `GN0001` | Service is unavailable |

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `balance-installment-advancement-cancelled-1` | https://developers.pismo.io/events/docs/balance-installment-advancement-cancelled-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;409;500`, has examples `False`, emits events `1`, deprecated `True`.

Guides that link to this operation: `KU-CRED-installment-advancements-guide`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/ContractAdvancementDto -->
### Schema `ContractAdvancementDto`

Pointer: `#/components/schemas/ContractAdvancementDto`. Type: object (schema `ContractAdvancementDto`).

> Contract advancement configuration for multiple contracts mode

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `authorization_id` | integer (schema `AuthorizationID`) | yes | Authorization ID for the contract | format: "int64"; example: 12345 |
| `calculator` | string (schema `Calculator`) | yes | Type of calculation to apply. Default is `NONE`.<br> | enum: ["PRESENT_VALUE", "REMOVE_ALL_INTEREST", "NONE"]; example: "PRESENT_VALUE" |
| `remove_interest_from_current` | boolean (schema `RemoveInterestFromCurrent`) | yes | Whether interest should be removed when an installment is advanced. | default: false; example: false |
| `reschedule` | string (schema `Reschedule`) | yes | Reschedule mode to apply. Must be `ADVANCEMENT`.<br> | enum: ["ADVANCEMENT"]; example: "ADVANCEMENT" |
| `contract_condition` | string (schema `ContractCondition`) | no | Should all the remaining installments for the contract be advanced (`ALL_INSTALLMENTS`) or just a specific number of them (`SPECIFIC_NUMBER_OF_INSTALLMENTS`)?<br><br>If this field is set to `SPECIFIC_NUMBER_OF_INSTALLMENTS`, the `number_of_installments` field must be set. If this field is set to `ALL_INSTALLMENTS`, the `number_of_installments` field is ignored.<br> | enum: ["ALL_INSTALLMENTS", "SPECIFIC_NUMBER_OF_INSTALLMENTS"]; example: "ALL_INSTALLMENTS" |
| `number_of_installments` | integer (schema `NumberOfInstallmentsToAdvance`) | no | Number of installments to advance<br><br>This field is **REQUIRED** if `contract_condition` is set to `SPECIFIC_NUMBER_OF_INSTALLMENTS`. If `contract_condition` is set to `ALL_CONTRACTS`, this field is ignored.<br> | format: "int32"; example: 3 |

<!-- schema: #/components/schemas/ContractAdvancementResponseDto -->
### Schema `ContractAdvancementResponseDto`

Pointer: `#/components/schemas/ContractAdvancementResponseDto`. Type: object (schema `ContractAdvancementResponseDto`).

> Contract advancement response

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `remove_interest_from_current` | boolean (schema `RemoveInterestFromCurrent`) | no | Whether interest should be removed when an installment is advanced. | default: false; example: false |
| `authorization_id` | integer (schema `AuthorizationID`) | no | Authorization ID for the contract | format: "int64"; example: 12345 |
| `number_of_installments` | integer (schema `NumberOfInstallmentsToAdvance`) | no | Number of installments to advance<br><br>This field is **REQUIRED** if `contract_condition` is set to `SPECIFIC_NUMBER_OF_INSTALLMENTS`. If `contract_condition` is set to `ALL_CONTRACTS`, this field is ignored.<br> | format: "int32"; example: 3 |
| `calculator` | string (schema `Calculator`) | no | Type of calculation to apply. Default is `NONE`.<br> | enum: ["PRESENT_VALUE", "REMOVE_ALL_INTEREST", "NONE"]; example: "PRESENT_VALUE" |
| `reschedule` | string (schema `Reschedule`) | no | Reschedule mode to apply. Must be `ADVANCEMENT`.<br> | enum: ["ADVANCEMENT"]; example: "ADVANCEMENT" |

<!-- schema: #/components/schemas/InstallmentResponseDto -->
### Schema `InstallmentResponseDto`

Pointer: `#/components/schemas/InstallmentResponseDto`. Type: object (schema `InstallmentResponseDto`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | integer (schema `TransactionIdOfInstallment`) | no | Transaction ID of the installment | format: "int64"; example: 98457355 |
| `new_amount` | number (schema `NewAmount`) | no | Full installment amount after applying any discount, including principal and interest charges<br> | format: "double"; example: 99.9 |
| `old_amount` | number (schema `OldAmount`) | no | Full installment amount before applying any discount, including principal and interest charges<br> | format: "double"; example: 102.9 |
| `new_interest_amount` | number (schema `NewInterestAmount`) | no | Full interest amount of installment after applying any discount<br> | format: "double"; example: 9.9 |
| `old_interest_amount` | number (schema `OldInterestAmount`) | no | The full interest amount of an installment before applying any discount.<br> | format: "double"; example: 11.9 |
| `new_statement_id` | number (schema `NewStatementId`) | no | ID of the current statement<br> | format: "integer"; example: 1 |
| `old_statement_id` | number (schema `OldStatementId`) | no | ID of the old statement. This is the ID of the statement on which the installment was scheduled to appear before it was advanced. For installments that are not advanced, `old_statement_id` and `new_statement_id` should contain the same values.<br> | format: "integer"; example: 10 |

<!-- schema: #/components/schemas/StandardErrorResponse -->
### Schema `StandardErrorResponse`

Pointer: `#/components/schemas/StandardErrorResponse`. Type: object (schema `StandardErrorResponse`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string (schema `ErrorCode`) | no | Error code | example: "EX0001" |
| `message` | string | no | Error message | example: "Internal error" |

## Lifecycle status

- `POST /v1/accounts/{accountId}/installment-advance` (`CreateInstallmentAdvancement`) is marked `deprecated: true` in the specification.
- `GET /v1/accounts/{accountId}/installment-advance/{advancementId}` (`GetIntallmentAdvancementById`) is marked `deprecated: true` in the specification.
- `DELETE /v1/accounts/{accountId}/installment-advance/{advancementId}` (`CancelInstallmentAdvancement`) is marked `deprecated: true` in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Revolving_credit_-_Installment_management.yaml` | tag `Installment advancements`: POST /v2/accounts/{accountId}/installment-advance, GET /v2/accounts/{accountId}/installment-advance/{advancementId}, DELETE /v2/accounts/{accountId}/installment-advance/{advancementId}, POST /v1/accounts/{accountId}/installment-advance, GET /v1/accounts/{accountId}/installment-advance/{advancementId}, DELETE /v1/accounts/{accountId}/installment-advance/{advancementId} | https://github.com/PismoDevEx/pismo-api-specs | `1a735b324f2927f9…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-CRED-installment-advancements-guide` — Installment advancements
- `KU-ERR-codes-esmg-to-whis` — Error codes: ESMG to WHIS (30 prefixes)
- `KU-ERR-codes-ex` — Error codes: EX
- `KU-EVT-catalogue-balance` — Event catalogue: balance
- `KU-LIFE-api-endpoint-deprecation-and-removal-schedule` — API endpoint deprecation and removal schedule
