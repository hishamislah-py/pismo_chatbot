---
ku_id: KU-API-lending--loan-products
title: 'API reference: Lending — Loan products'
category: api_reference
ku_type: api_reference
lifecycle: current
sources:
- path: api-specs/Lending.yaml
  sha256: 6667602e6ada2f8177fdb087e70904d04ae7ac8a59867d0cc5e4e6a12cd74b97
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
- getLoanProductV2
- deleteLoanProductV2
- updateLoanProductV2
- getLoanProductsV2
- createLoanProductV2
related_kus:
- KU-ERR-codes-elnd
- KU-EVT-catalogue-lending
- KU-EVT-lending-data-events
- KU-GS-get-started-with-pismo-apis
- KU-LEND-book-a-loan
- KU-LEND-loan-products
specification_version: 1.0.0
---

# API reference: Lending — Loan products

**KU ID:** `KU-API-lending--loan-products` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 5 operation(s) tagged `Loan products` in `api-specs/Lending.yaml` (“Lending”, version `1.0.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Creates and manages loan product features

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `GET /v2/loan-products/{productId}` | `getLoanProductV2` | Get loan product | no |
| `DELETE /v2/loan-products/{productId}` | `deleteLoanProductV2` | Delete loan product | no |
| `PATCH /v2/loan-products/{productId}` | `updateLoanProductV2` | Update loan product | no |
| `GET /v2/loan-products` | `getLoanProductsV2` | List loan products | no |
| `POST /v2/loan-products` | `createLoanProductV2` | Create loan product | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer"}

## Operation contracts

<!-- op: spec=api-specs/Lending.yaml method=GET path=/v2/loan-products/{productId} operationId=getLoanProductV2 -->
### `GET /v2/loan-products/{productId}` — Get loan product

- **operationId:** `getLoanProductV2`
- **Specification:** `api-specs/Lending.yaml` (Lending)
- **Server base URL(s):** `https://sandbox.pismolabs.io/lending`
- **Tags:** `Loan products`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Get a loan product by its ID.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `productId` | path | yes | string | Loan product ID | example: "99999999-9999-9999-9999-999999999999" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Loan product retrieved | `application/json`: object (schema `LoanProductV2Response`) |
| 400 | A validation error occurred. | `application/json`: object (schema `StandardErrorResponse`) |
| 404 | Not Found | `application/json`: object (schema `StandardErrorResponse`) |
| 500 | Internal Server Error | `application/json`: object (schema `StandardErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `collateral` | string (schema `Collateral`) | yes | Collateral | enum: ["NONE", "SINGLE", "COLLATERAL_MULTIPLE"]; example: "SINGLE" |
| `currency` | integer (schema `CurrencyCode`) | yes | ISO 4217 currency code | format: "int32"; minimum: 0; maximum: 999; example: 999 |
| `disbursement_method` | object (schema `LoanProductV2DisbursementMethod`) | yes | Disbursement method |  |
| `processing_codes` | object (schema `ProcessingCodes`) | yes | Define processing codes for each operation during the loan lifecycle. |  |
| `product_id` | string (schema `LoanProductID`) | yes | Loan product ID. Accepts either a lowercase UUID (e.g., "2717a296-124a-47cc-b2a1-91e80dc723eb") or an uppercase alphanumeric string with underscores (e.g., "MY_LOAN_PRODUCT_001"). If not provided during creation, a UUID is auto-generated. | pattern: "^([0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\|[A-Z0-9_]{1,80})$"; maxLength: 80; example: "2717a296-124a-47cc-b2a1-91e80dc723eb" |
| `product_name` | string (schema `ProductName`) | yes | Open text that describes the product | maxLength: 256; example: "Acme business loan" |
| `status` | string (schema `ProductStatus`) | yes | Product status | enum: ["ACTIVE", "INACTIVE"]; example: "ACTIVE" |
| `created_at` | string (schema `LoanCreatedAt`) | no | Loan created date in UTC. Format = YYYY-MM-DDThh:mm:ss.SSSZ | format: "date-time"; example: "2026-09-03T17:58:35.520Z" |
| `early_final_settlement` | object (schema `LoanProductEFS`) | no | Define some early settlement requirements. |  |
| `grace_period_days` | integer (schema `GracePeriodDays`) | no | Number of calendar days after the installment due date during which late fees and delinquency are not applied. A value of `0` or omitted indicates no grace period. | format: "int32"; minimum: 0; maximum: 365; example: 7 |
| `interest_plan_ids` | array of string (schema `InterestPlanIDs`) | no | List of interest plan IDs | items.format: "uuid" |
| `loan_activation_method` | string (schema `LoanProductLoanActivationMethod`) | no | Indicate when the system changes a loan to active status. Default is `ON_DISBURSEMENT_OR_REPAYMENT`. If disbursement method type is `NONE`, you cannot set to `ON_DISBURSEMENT`, and if set to `ON_DISBURSEMENT_OR_REPAYMENT` the system changes the loan status on repayment. | enum: ["ON_BOOKING", "ON_DISBURSEMENT", "ON_DISBURSEMENT_OR_REPAYMENT", "ON_REPAYMENT"]; example: "ON_BOOKING" |
| `minimum_total_payment` | number (schema `MinimumTotalPayment`) | no | Minimum total payment for the loan product. Must be positive. | format: "double"; minimum: 0; exclusiveMinimum: 0; example: 50 |
| `parameters` | object (schema `LoanProductV2Parameters`) | no | Loan product parameters |  |
| `penalty_plan_codes` | array of string (schema `ProductPenaltyPlanCodes`) | no | List of charge plan codes in order | maxLength: 20; uniqueItems: true; example: ["penalty-001", "penalty-002"] |
| `prepayment` | object (schema `LoanProductPrepayment`) | no | Defines some prepayment requirements. |  |
| `product_type` | string (schema `ProductTypeV2`) | no | Loan product type | enum: ["BNPL", "PERSONAL"]; default: "BNPL"; example: "BNPL" |
| `repayment_calculation_method` | string (schema `RepaymentCalculationMethodV2`) | no | Method used to calculate the repayment amount | enum: ["RATES"]; default: "RATES"; example: "RATES" |
| `repayment_hierarchy_code` | string (schema `RepaymentHierarchyCodeV2`) | no | Repayment hierarchy code. Must be normalized (Unicode NFC), and may contain a UUID, or uppercase letters, numbers, and underscore. | minLength: 1; maxLength: 80; example: "RH001" |
| `updated_at` | string (schema `LoanUpdatedAt`) | no | Loan last updated date in UTC. Format = YYYY-MM-DDThh:mm:ss.SSSZ. | format: "date-time"; example: "2024-03-15T13:00:00.000+00:00" |
| `version` | integer (schema `ProductVersionV2`) | no | Product version | format: "int64"; example: 1762434786787 |

##### Response 400

400 Example `{header field} not passed`:

```json
{
  "code": "ELND0002",
  "message": "{header field} not passed"
}
```

400 Example `{path variable} not passed`:

```json
{
  "code": "ELND0002",
  "message": "{path variable} not passed"
}
```

400 Example `{related data} not found`:

```json
{
  "code": "ELND0005",
  "message": "{related data} not found"
}
```

##### Response 404

404 Example `ELND0005`:

```json
{
  "code": "ELND0005",
  "message": "Loan product not found."
}
```

##### Response 500

500 Example `ELND0001`:

```json
{
  "code": "ELND0001",
  "message": "Unexpected error"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `ELND0002` | {header field} not passed |
| 400 | `ELND0005` | {related data} not found |
| 404 | `ELND0005` | Loan product not found. |
| 500 | `ELND0001` | Unexpected error |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;404;500`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-GS-get-started-with-pismo-apis`, `KU-LEND-book-a-loan`.

<!-- op: spec=api-specs/Lending.yaml method=DELETE path=/v2/loan-products/{productId} operationId=deleteLoanProductV2 -->
### `DELETE /v2/loan-products/{productId}` — Delete loan product

- **operationId:** `deleteLoanProductV2`
- **Specification:** `api-specs/Lending.yaml` (Lending)
- **Server base URL(s):** `https://sandbox.pismolabs.io/lending`
- **Tags:** `Loan products`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Delete a loan product by its ID. This operation marks the loan product as deleted and it cannot be used for new loans.
>
> This endpoint generates a [Loan product updated](https://developers.pismo.io/events/docs/lending-loan-product-update-1) event.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `productId` | path | yes | string | Loan product ID | example: "99999999-9999-9999-9999-999999999999" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 204 | Loan product deleted successfully. | `*/*`: object |
| 400 | A validation error occurred. | `application/json`: object (schema `StandardErrorResponse`) |
| 404 | Not Found | `application/json`: object (schema `StandardErrorResponse`) |
| 500 | Internal Server Error | `application/json`: object (schema `StandardErrorResponse`) |

##### Response 204

**204 `*/*` body fields:**

_No fields declared in the schema._

##### Response 400

400 Example `ELND0002`:

```json
{
  "code": "ELND0002",
  "message": "product_id not passed"
}
```

400 Example `ELND0320`:

```json
{
  "code": "ELND0320",
  "message": "product_id contains invalid characters"
}
```

##### Response 404

404 Example `ELND0005`:

```json
{
  "code": "ELND0005",
  "message": "Loan product not found."
}
```

##### Response 500

500 Example `ELND0001`:

```json
{
  "code": "ELND0001",
  "message": "Unexpected error"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `ELND0002` | product_id not passed |
| 400 | `ELND0320` | product_id contains invalid characters |
| 404 | `ELND0005` | Loan product not found. |
| 500 | `ELND0001` | Unexpected error |

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `lending-loan-product-update-1` | https://developers.pismo.io/events/docs/lending-loan-product-update-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `204;400;404;500`, has examples `True`, emits events `1`, deprecated `False`.

<!-- op: spec=api-specs/Lending.yaml method=PATCH path=/v2/loan-products/{productId} operationId=updateLoanProductV2 -->
### `PATCH /v2/loan-products/{productId}` — Update loan product

- **operationId:** `updateLoanProductV2`
- **Specification:** `api-specs/Lending.yaml` (Lending)
- **Server base URL(s):** `https://sandbox.pismolabs.io/lending`
- **Tags:** `Loan products`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Update an existing loan product with only the fields that are passed in the request body.
>
> This endpoint generates a [Loan product updated](https://developers.pismo.io/events/docs/lending-loan-product-update-1) event.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `productId` | path | yes | string | Loan product ID | example: "99999999-9999-9999-9999-999999999999" |
| `Idempotency-Key` | header | no | string | Optional UUID that makes the request idempotent, enabling you to retry it multiple times while the system processes it only once. | format: "uuid"; example: "4df987e3-8179-11ed-8209-06c7b022d1ee" |

#### Request body

Required: yes

> Request body containing the fields to update.

**Content type `application/json`** — schema: object (schema `UpdateLoanProductV2Request`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `disbursement_method` | object (schema `LoanProductV2DisbursementMethod`) | no | Disbursement method |  |
| `interest_plan_ids` | array of string (schema `InterestPlanIDs`) | no | List of interest plan IDs | items.format: "uuid" |
| `loan_activation_method` | string (schema `LoanProductLoanActivationMethod`) | no | Indicate when the system changes a loan to active status. Default is `ON_DISBURSEMENT_OR_REPAYMENT`. If disbursement method type is `NONE`, you cannot set to `ON_DISBURSEMENT`, and if set to `ON_DISBURSEMENT_OR_REPAYMENT` the system changes the loan status on repayment. | enum: ["ON_BOOKING", "ON_DISBURSEMENT", "ON_DISBURSEMENT_OR_REPAYMENT", "ON_REPAYMENT"]; example: "ON_BOOKING" |
| `minimum_total_payment` | anyOf: number (schema `MinimumTotalPayment`), null | no | Minimum total payment for the loan product. Set to "null" to remove. Must be positive if provided. | example: 50 |
| `parameters` | object (schema `LoanProductV2Parameters`) | no | Loan product parameters |  |
| `processing_codes` | object (schema `UpdateProcessingCodes`) | no | Processing codes to update. Only provided fields will be updated. |  |
| `product_name` | string (schema `ProductName`) | no | Open text that describes the product | maxLength: 256; example: "Acme business loan" |

Example `Update product name`:

```json
{
  "product_name": "Updated Product Name"
}
```

Example `Update loan activation method`:

```json
{
  "loan_activation_method": "ON_DISBURSEMENT"
}
```

Example `Update multiple fields`:

```json
{
  "product_name": "Updated BNPL Product",
  "loan_activation_method": "ON_BOOKING",
  "disbursement_method": {
    "type": "SINGLE"
  },
  "parameters": {
    "stop_accrual_number_of_days": 90
  },
  "interest_plan_ids": [
    "5a1b2c3d-4e5f-6789-abcd-1234567890ef"
  ],
  "processing_codes": {
    "booking": [
      "000011"
    ],
    "repayment": [
      "000012"
    ]
  }
}
```

Example `Update minimum total payment`:

```json
{
  "minimum_total_payment": 50
}
```

Example `Remove minimum total payment`:

```json
{
  "minimum_total_payment": null
}
```

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Loan product updated successfully. | `application/json`: object (schema `LoanProductV2Response`) |
| 202 | Duplicated request identified by Idempotency key. | `application/json`: object (schema `StandardErrorResponse`) |
| 400 | A validation error occurred. | `application/json`: object (schema `StandardErrorResponse`) |
| 404 | Not Found | `application/json`: object (schema `StandardErrorResponse`) |
| 500 | Internal Server Error | `application/json`: object (schema `StandardErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `collateral` | string (schema `Collateral`) | yes | Collateral | enum: ["NONE", "SINGLE", "COLLATERAL_MULTIPLE"]; example: "SINGLE" |
| `currency` | integer (schema `CurrencyCode`) | yes | ISO 4217 currency code | format: "int32"; minimum: 0; maximum: 999; example: 999 |
| `disbursement_method` | object (schema `LoanProductV2DisbursementMethod`) | yes | Disbursement method |  |
| `processing_codes` | object (schema `ProcessingCodes`) | yes | Define processing codes for each operation during the loan lifecycle. |  |
| `product_id` | string (schema `LoanProductID`) | yes | Loan product ID. Accepts either a lowercase UUID (e.g., "2717a296-124a-47cc-b2a1-91e80dc723eb") or an uppercase alphanumeric string with underscores (e.g., "MY_LOAN_PRODUCT_001"). If not provided during creation, a UUID is auto-generated. | pattern: "^([0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\|[A-Z0-9_]{1,80})$"; maxLength: 80; example: "2717a296-124a-47cc-b2a1-91e80dc723eb" |
| `product_name` | string (schema `ProductName`) | yes | Open text that describes the product | maxLength: 256; example: "Acme business loan" |
| `status` | string (schema `ProductStatus`) | yes | Product status | enum: ["ACTIVE", "INACTIVE"]; example: "ACTIVE" |
| `created_at` | string (schema `LoanCreatedAt`) | no | Loan created date in UTC. Format = YYYY-MM-DDThh:mm:ss.SSSZ | format: "date-time"; example: "2026-09-03T17:58:35.520Z" |
| `early_final_settlement` | object (schema `LoanProductEFS`) | no | Define some early settlement requirements. |  |
| `grace_period_days` | integer (schema `GracePeriodDays`) | no | Number of calendar days after the installment due date during which late fees and delinquency are not applied. A value of `0` or omitted indicates no grace period. | format: "int32"; minimum: 0; maximum: 365; example: 7 |
| `interest_plan_ids` | array of string (schema `InterestPlanIDs`) | no | List of interest plan IDs | items.format: "uuid" |
| `loan_activation_method` | string (schema `LoanProductLoanActivationMethod`) | no | Indicate when the system changes a loan to active status. Default is `ON_DISBURSEMENT_OR_REPAYMENT`. If disbursement method type is `NONE`, you cannot set to `ON_DISBURSEMENT`, and if set to `ON_DISBURSEMENT_OR_REPAYMENT` the system changes the loan status on repayment. | enum: ["ON_BOOKING", "ON_DISBURSEMENT", "ON_DISBURSEMENT_OR_REPAYMENT", "ON_REPAYMENT"]; example: "ON_BOOKING" |
| `minimum_total_payment` | number (schema `MinimumTotalPayment`) | no | Minimum total payment for the loan product. Must be positive. | format: "double"; minimum: 0; exclusiveMinimum: 0; example: 50 |
| `parameters` | object (schema `LoanProductV2Parameters`) | no | Loan product parameters |  |
| `penalty_plan_codes` | array of string (schema `ProductPenaltyPlanCodes`) | no | List of charge plan codes in order | maxLength: 20; uniqueItems: true; example: ["penalty-001", "penalty-002"] |
| `prepayment` | object (schema `LoanProductPrepayment`) | no | Defines some prepayment requirements. |  |
| `product_type` | string (schema `ProductTypeV2`) | no | Loan product type | enum: ["BNPL", "PERSONAL"]; default: "BNPL"; example: "BNPL" |
| `repayment_calculation_method` | string (schema `RepaymentCalculationMethodV2`) | no | Method used to calculate the repayment amount | enum: ["RATES"]; default: "RATES"; example: "RATES" |
| `repayment_hierarchy_code` | string (schema `RepaymentHierarchyCodeV2`) | no | Repayment hierarchy code. Must be normalized (Unicode NFC), and may contain a UUID, or uppercase letters, numbers, and underscore. | minLength: 1; maxLength: 80; example: "RH001" |
| `updated_at` | string (schema `LoanUpdatedAt`) | no | Loan last updated date in UTC. Format = YYYY-MM-DDThh:mm:ss.SSSZ. | format: "date-time"; example: "2024-03-15T13:00:00.000+00:00" |
| `version` | integer (schema `ProductVersionV2`) | no | Product version | format: "int64"; example: 1762434786787 |

##### Response 202

**202 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string (schema `ErrorCode`) | no | Lending error code | example: "ELND0001" |
| `message` | string (schema `ErrorMessage`) | no | Lending error message | example: "Unexpected error" |

202 Example `ELND1501`:

```json
{
  "code": "ELND1501",
  "message": "idempotency-key is already in use"
}
```

##### Response 400

400 Example `ELND0002`:

```json
{
  "code": "ELND0002",
  "message": "loan_product_id not passed"
}
```

400 Example `ELND0352`:

```json
{
  "code": "ELND0352",
  "message": "Field processing_codes.booking must be defined between 2 and 6"
}
```

400 Example `ELND0354`:

```json
{
  "code": "ELND0354",
  "message": "Field processing_codes.repayment must be defined between 2 and 6"
}
```

400 Example `ELND0360`:

```json
{
  "code": "ELND0360",
  "message": "Processing code PC_BOOKING already in use by product id 5770c974-dcd5-4a53-b19e-08078a8cb65d, and operation Booking"
}
```

400 Example `ELND0366`:

```json
{
  "code": "ELND0366",
  "message": "Interest plan PLAN1 not found"
}
```

400 Example `ELND0369`:

```json
{
  "code": "ELND0369",
  "message": "Processing codes list must have at most 20 items."
}
```

400 Example `ELND0376`:

```json
{
  "code": "ELND0376",
  "message": "Field minimum_total_payment must be positive"
}
```

400 Example `ELND0379`:

```json
{
  "code": "ELND0379",
  "message": "Field max_backdating_window_days can only be set when backdating_enabled is true"
}
```

400 Example `ELND0380`:

```json
{
  "code": "ELND0380",
  "message": "Field processing_codes.present_value_discount is required when bring_to_present_value_on_delinquency is true."
}
```

##### Response 404

404 Example `ELND0005`:

```json
{
  "code": "ELND0005",
  "message": "Loan product not found."
}
```

##### Response 500

500 Example `ELND0001`:

```json
{
  "code": "ELND0001",
  "message": "Unexpected error"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 202 | `ELND1501` | idempotency-key is already in use |
| 400 | `ELND0002` | loan_product_id not passed |
| 400 | `ELND0352` | Field processing_codes.booking must be defined between 2 and 6 |
| 400 | `ELND0354` | Field processing_codes.repayment must be defined between 2 and 6 |
| 400 | `ELND0360` | Processing code PC_BOOKING already in use by product id 5770c974-dcd5-4a53-b19e-08078a8cb65d, and operation Booking |
| 400 | `ELND0366` | Interest plan PLAN1 not found |
| 400 | `ELND0369` | Processing codes list must have at most 20 items. |
| 400 | `ELND0376` | Field minimum_total_payment must be positive |
| 400 | `ELND0379` | Field max_backdating_window_days can only be set when backdating_enabled is true |
| 400 | `ELND0380` | Field processing_codes.present_value_discount is required when bring_to_present_value_on_delinquency is true. |
| 404 | `ELND0005` | Loan product not found. |
| 500 | `ELND0001` | Unexpected error |

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `lending-loan-product-update-1` | https://developers.pismo.io/events/docs/lending-loan-product-update-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;202;400;404;500`, has examples `True`, emits events `1`, deprecated `False`.

Guides that link to this operation: `KU-EVT-lending-data-events`.

<!-- op: spec=api-specs/Lending.yaml method=GET path=/v2/loan-products operationId=getLoanProductsV2 -->
### `GET /v2/loan-products` — List loan products

- **operationId:** `getLoanProductsV2`
- **Specification:** `api-specs/Lending.yaml` (Lending)
- **Server base URL(s):** `https://sandbox.pismolabs.io/lending`
- **Tags:** `Loan products`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> List loan products.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `nextCursor` | query | yes | string (schema `NextCursor`) | Next page cursor identifier | example: "NmI5NmNlYzUtZTg1Ni00MjY0LTlkNzctNGY5OGIzNTk4YWM1IzE3NDU5NDY2MTg3NTIjMjAyNS0wNC0yOVQxNzoxMDoxOC43MjY3MTY0Mlo"; example: "99999999-9999-9999-9999-999999999999" |
| `limit` | query | no | integer (schema `Limit`) | Maximum number of items to return per page | format: "int32"; maximum: 50; example: 10; example: 10 |
| `loanProductId` | query | no | string (schema `LoanProductID`) | Loan product ID filter | pattern: "^([0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\|[A-Z0-9_]{1,80})$"; maxLength: 80; example: "2717a296-124a-47cc-b2a1-91e80dc723eb"; example: "99999999-9999-9999-9999-999999999999" |
| `loanProductName` | query | no | string (schema `ProductName`) | Loan product name filter | maxLength: 256; example: "Acme business loan"; example: "Home Loan" |
| `productType` | query | no | string (schema `ProductType`) | Loan product type filter | enum: ["BNPL", "PERSONAL", "BUSINESS"]; example: "BNPL"; example: "BNPL" |
| `currency` | query | no | integer (schema `CurrencyCode`) | ISO 4217 currency code filter | format: "int32"; minimum: 0; maximum: 999; example: 999; example: 840 |
| `collateralType` | query | no | string (schema `Collateral`) | Collateral type filter | enum: ["NONE", "SINGLE", "COLLATERAL_MULTIPLE"]; example: "SINGLE" |
| `disbursementType` | query | no | string (schema `LoanProductV2DisbursementType`) | Disbursement method type filter | enum: ["NONE", "SINGLE", "MULTIPLE"]; default: "NONE"; example: "SINGLE" |
| `status` | query | no | string (schema `ProductStatus`) | Loan product status filter | enum: ["ACTIVE", "INACTIVE"]; example: "ACTIVE" |
| `startDate` | query | no | string (schema `DateValue`) | Search for products created from this date | format: "date"; example: "2023-12-31" |
| `endDate` | query | no | string (schema `DateValue`) | Search for products created until this date. Note: If `endDate` is provided, `startDate` must also be provided. This dependency is required by the API. | format: "date"; example: "2023-12-31" |
| `sortField` | query | no | string | Field to sort by | enum: ["PRODUCT_ID", "PRODUCT_NAME", "CREATION_DATE"]; default: "CREATION_DATE" |
| `sortOrder` | query | no | string | Sort direction applied to the `sortField` value. Use `ASC` for ascending or `DESC` for descending | enum: ["ASC", "DESC"]; default: "ASC" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Loan Products Retrieved. | `application/json`: object (schema `ListLoanProductV2Response`) |
| 400 | A validation error occurred. | `application/json`: object (schema `StandardErrorResponse`) |
| 500 | Internal Server Error | `application/json`: object (schema `StandardErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `has_next` | boolean (schema `HasNext`) | yes | Does the query have additional items to return? | example: true |
| `items` | array of object (schema `LoanProductV2Response`) | yes | List of loan products |  |
| `interest_plan_ids` | array of string (schema `InterestPlanIDs`) | no | List of interest plan IDs | items.format: "uuid" |
| `next_cursor` | string (schema `NextCursor`) | no | Opaque pagination cursor returned by the API. Pass back exactly as received to retrieve the next page; do not parse or modify it. | example: "NmI5NmNlYzUtZTg1Ni00MjY0LTlkNzctNGY5OGIzNTk4YWM1IzE3NDU5NDY2MTg3NTIjMjAyNS0wNC0yOVQxNzoxMDoxOC43MjY3MTY0Mlo" |
| `repayment_calculation_method` | string (schema `RepaymentCalculationMethodV2`) | no | Method used to calculate the repayment amount | enum: ["RATES"]; default: "RATES"; example: "RATES" |

##### Response 400

400 Example `{header field} not passed`:

```json
{
  "code": "ELND0002",
  "message": "{header field} not passed"
}
```

400 Example `{path variable} not passed`:

```json
{
  "code": "ELND0002",
  "message": "{path variable} not passed"
}
```

400 Example `{related data} not found`:

```json
{
  "code": "ELND0005",
  "message": "{related data} not found"
}
```

##### Response 500

500 Example `ELND0001`:

```json
{
  "code": "ELND0001",
  "message": "Unexpected error"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `ELND0002` | {header field} not passed |
| 400 | `ELND0005` | {related data} not found |
| 500 | `ELND0001` | Unexpected error |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;500`, has examples `True`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Lending.yaml method=POST path=/v2/loan-products operationId=createLoanProductV2 -->
### `POST /v2/loan-products` — Create loan product

- **operationId:** `createLoanProductV2`
- **Specification:** `api-specs/Lending.yaml` (Lending)
- **Server base URL(s):** `https://sandbox.pismolabs.io/lending`
- **Tags:** `Loan products`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Creates a loan product.
>
> This endpoint generates a [Loan product created](https://developers.pismo.io/events/docs/lending-loan-product-creation-3) event.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Idempotency-Key` | header | no | string | Optional UUID that makes the request idempotent, enabling you to retry it multiple times while the system processes it only once. | format: "uuid"; example: "4df987e3-8179-11ed-8209-06c7b022d1ee" |

#### Request body

Required: yes

> Request body.

**Content type `application/json`** — schema: object (schema `CreateLoanProductV2Request`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `collateral` | string (schema `Collateral`) | yes | Collateral | enum: ["NONE", "SINGLE", "COLLATERAL_MULTIPLE"]; example: "SINGLE" |
| `currency` | integer (schema `CurrencyCode`) | yes | ISO 4217 currency code | format: "int32"; minimum: 0; maximum: 999; example: 999 |
| `disbursement_method` | object (schema `LoanProductV2DisbursementMethod`) | yes | Disbursement method |  |
| `processing_codes` | object (schema `ProcessingCodes`) | yes | Define processing codes for each operation during the loan lifecycle. |  |
| `product_name` | string (schema `ProductName`) | yes | Open text that describes the product | maxLength: 256; example: "Acme business loan" |
| `product_type` | string (schema `ProductTypeV2`) | yes | Loan product type | enum: ["BNPL", "PERSONAL"]; default: "BNPL"; example: "BNPL" |
| `early_final_settlement` | object (schema `LoanProductEFS`) | no | Define some early settlement requirements. |  |
| `grace_period_days` | integer (schema `GracePeriodDays`) | no | Number of calendar days after the installment due date during which late fees and delinquency are not applied. A value of `0` or omitted indicates no grace period. | format: "int32"; minimum: 0; maximum: 365; example: 7 |
| `interest_plan_ids` | array of string (schema `InterestPlanIDs`) | no | List of interest plan IDs | items.format: "uuid" |
| `loan_activation_method` | string (schema `LoanProductLoanActivationMethod`) | no | Indicate when the system changes a loan to active status. Default is `ON_DISBURSEMENT_OR_REPAYMENT`. If disbursement method type is `NONE`, you cannot set to `ON_DISBURSEMENT`, and if set to `ON_DISBURSEMENT_OR_REPAYMENT` the system changes the loan status on repayment. | enum: ["ON_BOOKING", "ON_DISBURSEMENT", "ON_DISBURSEMENT_OR_REPAYMENT", "ON_REPAYMENT"]; example: "ON_BOOKING" |
| `minimum_total_payment` | number (schema `MinimumTotalPayment`) | no | Minimum total payment for the loan product. Must be positive. | format: "double"; minimum: 0; exclusiveMinimum: 0; example: 50 |
| `parameters` | object (schema `LoanProductV2Parameters`) | no | Loan product parameters |  |
| `prepayment` | object (schema `LoanProductPrepayment`) | no | Defines some prepayment requirements. |  |
| `product_id` | string (schema `LoanProductID`) | no | Loan product ID. Accepts either a lowercase UUID (e.g., "2717a296-124a-47cc-b2a1-91e80dc723eb") or an uppercase alphanumeric string with underscores (e.g., "MY_LOAN_PRODUCT_001"). If not provided during creation, a UUID is auto-generated. | pattern: "^([0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\|[A-Z0-9_]{1,80})$"; maxLength: 80; example: "2717a296-124a-47cc-b2a1-91e80dc723eb" |
| `repayment_calculation_method` | string (schema `RepaymentCalculationMethodV2`) | no | Method used to calculate the repayment amount | enum: ["RATES"]; default: "RATES"; example: "RATES" |
| `repayment_hierarchy_code` | string (schema `RepaymentHierarchyCodeV2`) | no | Repayment hierarchy code. Must be normalized (Unicode NFC), and may contain a UUID, or uppercase letters, numbers, and underscore. | minLength: 1; maxLength: 80; example: "RH001" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | Loan Product created. | `application/json`: object (schema `LoanProductPostResponse`) |
| 202 | Duplicated request identified by Idempotency key. | `application/json`: object (schema `StandardErrorResponse`) |
| 400 | A validation error occurred. | `application/json`: object (schema `StandardErrorResponse`) |
| 500 | Internal Server Error | `application/json`: object (schema `StandardErrorResponse`) |

##### Response 201

**201 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `product_id` | string (schema `LoanProductID`) | yes | Loan product ID. Accepts either a lowercase UUID (e.g., "2717a296-124a-47cc-b2a1-91e80dc723eb") or an uppercase alphanumeric string with underscores (e.g., "MY_LOAN_PRODUCT_001"). If not provided during creation, a UUID is auto-generated. | pattern: "^([0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\|[A-Z0-9_]{1,80})$"; maxLength: 80; example: "2717a296-124a-47cc-b2a1-91e80dc723eb" |

##### Response 202

**202 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string (schema `ErrorCode`) | no | Lending error code | example: "ELND0001" |
| `message` | string (schema `ErrorMessage`) | no | Lending error message | example: "Unexpected error" |

202 Example `ELND1501`:

```json
{
  "code": "ELND1501",
  "message": "idempotency-key is already in use"
}
```

##### Response 400

400 Example `ELND0350`:

```json
{
  "code": "ELND0350",
  "message": "Field processing_codes not passed"
}
```

400 Example `ELND0351`:

```json
{
  "code": "ELND0351",
  "message": "Field processing_codes.booking not passed"
}
```

400 Example `ELND0352`:

```json
{
  "code": "ELND0352",
  "message": "Field processing_codes.booking must be defined between 2 and 6"
}
```

400 Example `ELND0353`:

```json
{
  "code": "ELND0353",
  "message": "Field processing_codes.repayment not passed"
}
```

400 Example `ELND0354`:

```json
{
  "code": "ELND0354",
  "message": "Field processing_codes.repayment must be defined between 2 and 6"
}
```

400 Example `ELND0355`:

```json
{
  "code": "ELND0355",
  "message": "Field processing_codes.prepayment_discount must be defined between 2 and 6"
}
```

400 Example `ELND0356`:

```json
{
  "code": "ELND0356",
  "message": "Field processing_codes.penalty_accruals must be defined between 2 and 6"
}
```

400 Example `ELND0357`:

```json
{
  "code": "ELND0357",
  "message": "Field processing_codes.penalty_waiver must be defined between 2 and 6"
}
```

400 Example `ELND0358`:

```json
{
  "code": "ELND0358",
  "message": "Field processing_codes.insurance.booking must be defined between 2 and 6"
}
```

400 Example `ELND0359`:

```json
{
  "code": "ELND0359",
  "message": "Field processing_codes.insurance.repayment must be defined between 2 and 6"
}
```

400 Example `ELND0360`:

```json
{
  "code": "ELND0360",
  "message": "Processing code `%s` already in use by product id %s, and operation %s"
}
```

400 Example `ELND0361`:

```json
{
  "code": "ELND0361",
  "message": "The processing code must be unique for each operation."
}
```

400 Example `ELND0362`:

```json
{
  "code": "ELND0362",
  "message": "Processing code %s is not linked to transactions types."
}
```

400 Example `ELND0363`:

```json
{
  "code": "ELND0363",
  "message": "Processing code %s is invalid or does not exist."
}
```

400 Example `ELND0380`:

```json
{
  "code": "ELND0380",
  "message": "Field processing_codes.present_value_discount is required when bring_to_present_value_on_delinquency is true."
}
```

400 Example `ELND0011`:

```json
{
  "code": "ELND0011",
  "message": "%s %s not valid for Disbursement Method %s"
}
```

400 Example `ELND0012`:

```json
{
  "code": "ELND0012",
  "message": "%s %s not valid. Allowed values : %s"
}
```

400 Example `ELND0379`:

```json
{
  "code": "ELND0379",
  "message": "Field max_backdating_window_days can only be set when backdating_enabled is true"
}
```

##### Response 500

500 Example `ELND0001`:

```json
{
  "code": "ELND0001",
  "message": "Unexpected error"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 202 | `ELND1501` | idempotency-key is already in use |
| 400 | `ELND0350` | Field processing_codes not passed |
| 400 | `ELND0351` | Field processing_codes.booking not passed |
| 400 | `ELND0352` | Field processing_codes.booking must be defined between 2 and 6 |
| 400 | `ELND0353` | Field processing_codes.repayment not passed |
| 400 | `ELND0354` | Field processing_codes.repayment must be defined between 2 and 6 |
| 400 | `ELND0355` | Field processing_codes.prepayment_discount must be defined between 2 and 6 |
| 400 | `ELND0356` | Field processing_codes.penalty_accruals must be defined between 2 and 6 |
| 400 | `ELND0357` | Field processing_codes.penalty_waiver must be defined between 2 and 6 |
| 400 | `ELND0358` | Field processing_codes.insurance.booking must be defined between 2 and 6 |
| 400 | `ELND0359` | Field processing_codes.insurance.repayment must be defined between 2 and 6 |
| 400 | `ELND0360` | Processing code `%s` already in use by product id %s, and operation %s |
| 400 | `ELND0361` | The processing code must be unique for each operation. |
| 400 | `ELND0362` | Processing code %s is not linked to transactions types. |
| 400 | `ELND0363` | Processing code %s is invalid or does not exist. |
| 400 | `ELND0380` | Field processing_codes.present_value_discount is required when bring_to_present_value_on_delinquency is true. |
| 400 | `ELND0011` | %s %s not valid for Disbursement Method %s |
| 400 | `ELND0012` | %s %s not valid. Allowed values : %s |
| 400 | `ELND0379` | Field max_backdating_window_days can only be set when backdating_enabled is true |
| 500 | `ELND0001` | Unexpected error |

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `lending-loan-product-creation-3` | https://developers.pismo.io/events/docs/lending-loan-product-creation-3 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `201;202;400;500`, has examples `True`, emits events `1`, deprecated `False`.

Guides that link to this operation: `KU-EVT-lending-data-events`, `KU-LEND-loan-products`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/LoanProductV2DisbursementMethod -->
### Schema `LoanProductV2DisbursementMethod`

Pointer: `#/components/schemas/LoanProductV2DisbursementMethod`. Type: object (schema `LoanProductV2DisbursementMethod`).

> Disbursement method

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `type` | string (schema `LoanProductV2DisbursementType`) | yes | Disbursement method type or how the loan is delivered. | enum: ["NONE", "SINGLE", "MULTIPLE"]; default: "NONE"; example: "SINGLE" |

<!-- schema: #/components/schemas/ProcessingCodes -->
### Schema `ProcessingCodes`

Pointer: `#/components/schemas/ProcessingCodes`. Type: object (schema `ProcessingCodes`).

> Define processing codes for each operation during the loan lifecycle.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `booking` | array of string (schema `ProcessingCode`) | no | List of booking processing code | items.minLength: 2; items.maxLength: 6 |
| `disbursement` | object (schema `DisbursementPC`) | no | Define processing codes for disbursement operations. |  |
| `early_final_settlement` | object (schema `EfsPC`) | no | Define processing codes for early final settlement (EFS) operations. |  |
| `insurance` | object (schema `InsurancePC`) | no | Define processing codes for insurance operations. |  |
| `penalty_accruals` | array of string (schema `ProcessingCode`) | no | List of penalty accruals processing codes | items.minLength: 2; items.maxLength: 6 |
| `penalty_waiver` | array of string (schema `ProcessingCode`) | no | List of penalty waiver processing codes | items.minLength: 2; items.maxLength: 6 |
| `prepayment` | object (schema `PrepaymentPC`) | no | Define processing codes for prepayment operations. |  |
| `present_value_discount` | array of string (schema `ProcessingCode`) | no | List of present value discount processing codes | items.minLength: 2; items.maxLength: 6 |
| `repayment` | array of string (schema `ProcessingCode`) | no | List of repayment processing codes | items.minLength: 2; items.maxLength: 6 |
| `restructuring` | array of string (schema `ProcessingCode`) | no | List of restructuring processing codes | items.minLength: 2; items.maxLength: 6 |

<!-- schema: #/components/schemas/LoanProductEFS -->
### Schema `LoanProductEFS`

Pointer: `#/components/schemas/LoanProductEFS`. Type: object (schema `LoanProductEFS`).

> Define some early settlement requirements.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `penalty` | object (schema `PenaltyV2`) | yes | Penalty configuration for early settlement or prepayment |  |
| `lock_in_period` | integer (schema `LockInPeriod`) | no | Minimum number of installments that must be made before early settlement is possible. | default: 9; format: "int32"; minimum: 1; example: 9 |

<!-- schema: #/components/schemas/LoanProductV2Parameters -->
### Schema `LoanProductV2Parameters`

Pointer: `#/components/schemas/LoanProductV2Parameters`. Type: object (schema `LoanProductV2Parameters`).

> Loan product parameters

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `overdue_threshold_days` | number | no | Number of days before the account is considered overdue | format: "int32"; minimum: 1; maximum: 365; example: 30 |
| `stop_accrual_number_of_days` | number | no | Maximum period during which delinquency-related charges accrue after a payment is overdue, based on lender policy or local regulations. Once this threshold is reached, new penalty charges stop posting, so the outstanding debt no longer increases. | format: "int32"; minimum: 1; maximum: 365; example: 60 |
| `delinquency_closure_days` | number \\\| null | no | Number of days past due after which all loans for the account are automatically closed or canceled using the delinquency closure process. When `null`, the loan product does not enable this delinquency closure feature.<br>Value must be greater than `overdue_threshold_days` when both fields are provided. Returns `ELND0378` if `delinquency_closure_days` are less than or equal to `overdue_threshold_days`.<br> | format: "int32"; minimum: 1; maximum: 365; example: 90 |
| `bring_to_present_value_on_delinquency` | boolean | no | Should the platform bring future installments to present value before cancellation when closing due to delinquency?<br>When set to `true`, at least one `processing_codes.present_value_discount` code must be configured on the loan product (either provided in the same request or already present on the product for updates). Returns `ELND0380` otherwise.<br> | default: false; example: false |
| `backdating_enabled` | boolean | no | Does the product allow backdated payments? (These payments do not get penalized for arriving after the effective payment date). Defaults to `false`. | default: false; example: true |
| `max_backdating_window_days` | number | no | Maximum age (in days) of a backdated `repayment_date`. Meaningful only when `backdating_enabled` is `true`; defaults to 60 when backdating is enabled and no value is provided. Returns `ELND0379` if set while `backdating_enabled` is not `true`.<br> | format: "int32"; minimum: 1; maximum: 365; example: 60 |

<!-- schema: #/components/schemas/LoanProductPrepayment -->
### Schema `LoanProductPrepayment`

Pointer: `#/components/schemas/LoanProductPrepayment`. Type: object (schema `LoanProductPrepayment`).

> Defines some prepayment requirements.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `penalty` | object (schema `PenaltyV2`) | yes | Penalty configuration for early settlement or prepayment |  |
| `reduce_option` | array of string (schema `ReduceOption`) (schema `ReduceOptionsArray`) | yes | List of options to define how to reduce an outstanding loan amount. `INSTALLMENT` reduces the installment amounts over time but keeps the same maturity date. `TERM` applies the prepayment amount to reduce the loan term (duration), changing the loan maturity date. With either option, if the amount paid is not enough to cover a full installment amount, it partially pays the installment based on the prepayment hierarchy settings.<br> | minItems: 1; uniqueItems: true; example: ["INSTALLMENT", "TERM"]; items.enum: ["INSTALLMENT", "TERM"] |
| `lock_in_period` | integer (schema `LockInPeriod`) | no | Minimum number of installments that must be made before early settlement is possible. | default: 9; format: "int32"; minimum: 1; example: 9 |

<!-- schema: #/components/schemas/StandardErrorResponse -->
### Schema `StandardErrorResponse`

Pointer: `#/components/schemas/StandardErrorResponse`. Type: object (schema `StandardErrorResponse`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string (schema `ErrorCode`) | no | Lending error code | example: "ELND0001" |
| `message` | string (schema `ErrorMessage`) | no | Lending error message | example: "Unexpected error" |

<!-- schema: #/components/schemas/UpdateProcessingCodes -->
### Schema `UpdateProcessingCodes`

Pointer: `#/components/schemas/UpdateProcessingCodes`. Type: object (schema `UpdateProcessingCodes`).

> Processing codes to update. Only provided fields will be updated.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `booking` | array of string (schema `ProcessingCode`) | no | List of booking processing codes | items.minLength: 2; items.maxLength: 6 |
| `disbursement` | object (schema `DisbursementPC`) | no | Define processing codes for disbursement operations. |  |
| `early_final_settlement` | object (schema `EfsPC`) | no | Define processing codes for early final settlement (EFS) operations. |  |
| `insurance` | object (schema `InsurancePC`) | no | Define processing codes for insurance operations. |  |
| `penalty_accruals` | array of string (schema `ProcessingCode`) | no | List of penalty accruals processing codes | items.minLength: 2; items.maxLength: 6 |
| `penalty_waiver` | array of string (schema `ProcessingCode`) | no | List of penalty waiver processing codes | items.minLength: 2; items.maxLength: 6 |
| `prepayment` | object (schema `PrepaymentPC`) | no | Define processing codes for prepayment operations. |  |
| `present_value_discount` | array of string (schema `ProcessingCode`) | no | List of present value discount processing codes | items.minLength: 2; items.maxLength: 6 |
| `repayment` | array of string (schema `ProcessingCode`) | no | List of repayment processing codes | items.minLength: 2; items.maxLength: 6 |
| `restructuring` | array of string (schema `ProcessingCode`) | no | List of restructuring processing codes | items.minLength: 2; items.maxLength: 6 |

<!-- schema: #/components/schemas/LoanProductV2Response -->
### Schema `LoanProductV2Response`

Pointer: `#/components/schemas/LoanProductV2Response`. Type: object (schema `LoanProductV2Response`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `collateral` | string (schema `Collateral`) | yes | Collateral | enum: ["NONE", "SINGLE", "COLLATERAL_MULTIPLE"]; example: "SINGLE" |
| `currency` | integer (schema `CurrencyCode`) | yes | ISO 4217 currency code | format: "int32"; minimum: 0; maximum: 999; example: 999 |
| `disbursement_method` | object (schema `LoanProductV2DisbursementMethod`) | yes | Disbursement method |  |
| `processing_codes` | object (schema `ProcessingCodes`) | yes | Define processing codes for each operation during the loan lifecycle. |  |
| `product_id` | string (schema `LoanProductID`) | yes | Loan product ID. Accepts either a lowercase UUID (e.g., "2717a296-124a-47cc-b2a1-91e80dc723eb") or an uppercase alphanumeric string with underscores (e.g., "MY_LOAN_PRODUCT_001"). If not provided during creation, a UUID is auto-generated. | pattern: "^([0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\|[A-Z0-9_]{1,80})$"; maxLength: 80; example: "2717a296-124a-47cc-b2a1-91e80dc723eb" |
| `product_name` | string (schema `ProductName`) | yes | Open text that describes the product | maxLength: 256; example: "Acme business loan" |
| `status` | string (schema `ProductStatus`) | yes | Product status | enum: ["ACTIVE", "INACTIVE"]; example: "ACTIVE" |
| `created_at` | string (schema `LoanCreatedAt`) | no | Loan created date in UTC. Format = YYYY-MM-DDThh:mm:ss.SSSZ | format: "date-time"; example: "2026-09-03T17:58:35.520Z" |
| `early_final_settlement` | object (schema `LoanProductEFS`) | no | Define some early settlement requirements. |  |
| `grace_period_days` | integer (schema `GracePeriodDays`) | no | Number of calendar days after the installment due date during which late fees and delinquency are not applied. A value of `0` or omitted indicates no grace period. | format: "int32"; minimum: 0; maximum: 365; example: 7 |
| `interest_plan_ids` | array of string (schema `InterestPlanIDs`) | no | List of interest plan IDs | items.format: "uuid" |
| `loan_activation_method` | string (schema `LoanProductLoanActivationMethod`) | no | Indicate when the system changes a loan to active status. Default is `ON_DISBURSEMENT_OR_REPAYMENT`. If disbursement method type is `NONE`, you cannot set to `ON_DISBURSEMENT`, and if set to `ON_DISBURSEMENT_OR_REPAYMENT` the system changes the loan status on repayment. | enum: ["ON_BOOKING", "ON_DISBURSEMENT", "ON_DISBURSEMENT_OR_REPAYMENT", "ON_REPAYMENT"]; example: "ON_BOOKING" |
| `minimum_total_payment` | number (schema `MinimumTotalPayment`) | no | Minimum total payment for the loan product. Must be positive. | format: "double"; minimum: 0; exclusiveMinimum: 0; example: 50 |
| `parameters` | object (schema `LoanProductV2Parameters`) | no | Loan product parameters |  |
| `penalty_plan_codes` | array of string (schema `ProductPenaltyPlanCodes`) | no | List of charge plan codes in order | maxLength: 20; uniqueItems: true; example: ["penalty-001", "penalty-002"] |
| `prepayment` | object (schema `LoanProductPrepayment`) | no | Defines some prepayment requirements. |  |
| `product_type` | string (schema `ProductTypeV2`) | no | Loan product type | enum: ["BNPL", "PERSONAL"]; default: "BNPL"; example: "BNPL" |
| `repayment_calculation_method` | string (schema `RepaymentCalculationMethodV2`) | no | Method used to calculate the repayment amount | enum: ["RATES"]; default: "RATES"; example: "RATES" |
| `repayment_hierarchy_code` | string (schema `RepaymentHierarchyCodeV2`) | no | Repayment hierarchy code. Must be normalized (Unicode NFC), and may contain a UUID, or uppercase letters, numbers, and underscore. | minLength: 1; maxLength: 80; example: "RH001" |
| `updated_at` | string (schema `LoanUpdatedAt`) | no | Loan last updated date in UTC. Format = YYYY-MM-DDThh:mm:ss.SSSZ. | format: "date-time"; example: "2024-03-15T13:00:00.000+00:00" |
| `version` | integer (schema `ProductVersionV2`) | no | Product version | format: "int64"; example: 1762434786787 |

<!-- schema: #/components/schemas/DisbursementPC -->
### Schema `DisbursementPC`

Pointer: `#/components/schemas/DisbursementPC`. Type: object (schema `DisbursementPC`).

> Define processing codes for disbursement operations.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `external` | array of string (schema `ProcessingCode`) | no | List of processing codes for external account | items.minLength: 2; items.maxLength: 6 |
| `internal` | array of string (schema `ProcessingCode`) | no | List of processing codes for internal account | items.minLength: 2; items.maxLength: 6 |

<!-- schema: #/components/schemas/EfsPC -->
### Schema `EfsPC`

Pointer: `#/components/schemas/EfsPC`. Type: object (schema `EfsPC`).

> Define processing codes for early final settlement (EFS) operations.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `fee` | array of string (schema `ProcessingCode`) | no | List of fee processing codes for early final settlement | items.minLength: 2; items.maxLength: 6 |

<!-- schema: #/components/schemas/InsurancePC -->
### Schema `InsurancePC`

Pointer: `#/components/schemas/InsurancePC`. Type: object (schema `InsurancePC`).

> Define processing codes for insurance operations.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `booking` | array of string (schema `ProcessingCode`) | no | List of booking processing codes | items.minLength: 2; items.maxLength: 6 |
| `repayment` | array of string (schema `ProcessingCode`) | no | List of repayment processing codes | items.minLength: 2; items.maxLength: 6 |

<!-- schema: #/components/schemas/PrepaymentPC -->
### Schema `PrepaymentPC`

Pointer: `#/components/schemas/PrepaymentPC`. Type: object (schema `PrepaymentPC`).

> Define processing codes for prepayment operations.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `fee` | array of string (schema `ProcessingCode`) | no | List of fee processing codes for prepayment | items.minLength: 2; items.maxLength: 6 |

<!-- schema: #/components/schemas/PenaltyV2 -->
### Schema `PenaltyV2`

Pointer: `#/components/schemas/PenaltyV2`. Type: object (schema `PenaltyV2`).

> Penalty configuration for early settlement or prepayment

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `type` | string (schema `PenaltyType`) | yes | Type of penalty calculation | enum: ["PERCENTAGE", "FIXED_AMOUNT"]; example: "PERCENTAGE" |
| `value` | number (schema `PenaltyValue`) | yes | Penalty value. For `PERCENTAGE` penalty type, enter a value between 0 and 1 (such as 0.05 for 5%). For `FIXED_AMOUNT` penalty type, enter the fixed amount value. | format: "double"; minimum: 0; example: 0.05 |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Lending.yaml` | tag `Loan products`: GET /v2/loan-products/{productId}, DELETE /v2/loan-products/{productId}, PATCH /v2/loan-products/{productId}, GET /v2/loan-products, POST /v2/loan-products | https://github.com/PismoDevEx/pismo-api-specs | `6667602e6ada2f81…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-ERR-codes-elnd` — Error codes: ELND
- `KU-EVT-catalogue-lending` — Event catalogue: lending
- `KU-EVT-lending-data-events` — Lending events
- `KU-GS-get-started-with-pismo-apis` — Get started with Pismo APIs
- `KU-LEND-book-a-loan` — Book loans
- `KU-LEND-loan-products` — Loan products: overview and creation
