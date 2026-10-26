---
ku_id: KU-API-revolving-credit-recurring-charges--recurring-charge-plans
title: 'API reference: Revolving credit - Recurring charges — Recurring charge plans'
category: api_reference
ku_type: api_reference
lifecycle: current
sources:
- path: api-specs/Revolving_credit_-_Recurring_charges.yaml
  sha256: d9ee67e0177041de1023c91140aae3a9cf9ba0e44cb121395f18c1dac13ed7f0
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
- list-recurring-charge-plans
- create-recurring-charge-plan
- get-recurring-charge-plan
- disable-recurring-charge-plan
related_kus:
- KU-AUTH-account-and-external-id-tokens
- KU-CRED-recurring-charges
- KU-EVT-catalogue-balance
- KU-EVT-recurring-charges-data-events
specification_version: 1.0.0
---

# API reference: Revolving credit - Recurring charges — Recurring charge plans

**KU ID:** `KU-API-revolving-credit-recurring-charges--recurring-charge-plans` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 4 operation(s) tagged `Recurring charge plans` in `api-specs/Revolving_credit_-_Recurring_charges.yaml` (“Revolving credit - Recurring charges”, version `1.0.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Endpoints to manage the recurring charge plans.

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `GET /v1/recurring-charge-plans` | `list-recurring-charge-plans` | List recurring charge plans | no |
| `POST /v1/recurring-charge-plans` | `create-recurring-charge-plan` | Create recurring charge plan | no |
| `GET /v1/recurring-charge-plans/{recurring_charge_plan_id}` | `get-recurring-charge-plan` | Get recurring charge plan | no |
| `DELETE /v1/recurring-charge-plans/{recurring_charge_plan_id}` | `disable-recurring-charge-plan` | Disable recurring charge plan | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"} — Account access token. Tokens can expire quickly, which can result in an "Unauthorized" error.

## Operation contracts

<!-- op: spec=api-specs/Revolving_credit_-_Recurring_charges.yaml method=GET path=/v1/recurring-charge-plans operationId=list-recurring-charge-plans -->
### `GET /v1/recurring-charge-plans` — List recurring charge plans

- **operationId:** `list-recurring-charge-plans`
- **Specification:** `api-specs/Revolving_credit_-_Recurring_charges.yaml` (Revolving credit - Recurring charges)
- **Server base URL(s):** `https://sandbox.pismolabs.io/recurring-charge`
- **Tags:** `Recurring charge plans`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Returns a list of recurring charge plans.
>
> **NOTE:** This endpoint requires an account token — an access token encoded with an account ID. Tokens can expire quickly, which can result in a **401 Unauthorized** message.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `x-cid` | header | no | string | The Correlation IDentifier field is used to link related API requests and events. The x-cid can help the Pismo engineering team track everything related to a call. You can find the x-cid field in the response header from an API endpoint call.<br><br>If this field isn't passed, one is automatically generated.<br> | example: "5bb05174-4e80-11ea-b77f-2e728ce88125" |
| `page` | query | no | integer | Page number | default: 1; example: 3 |
| `perPage` | query | no | integer | Maximum number of items per page | default: 100; example: 10 |
| `active` | query | no | boolean | If `true`, the request returns only active plans. | default: false; example: true |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK - Indicates that the server accepted the request and returned the results. If no records are found, the request returns an empty array with `total_items` set to 0. | `application/json`: object (schema `PagedRecurringChargePlan`) |
| 400 | Bad Request |  |
| 500 | Internal server error |  |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `current_page` | integer (schema `CurrentPage`) | no | Current page | format: "int32"; example: 1 |
| `per_page` | integer (schema `PerPage`) | no | Number of items per page | example: 1 |
| `pages` | integer (schema `Pages`) | no | Number of pages | example: 10 |
| `total_items` | integer (schema `TotalItems`) | no | Total items | example: 10 |
| `is_last_page` | boolean (schema `IsLastPage`) | no | Set to `true` if this is the last page. | example: false |
| `items` | array of object (schema `RecurringChargePlan`) | no |  |  |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;500`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-AUTH-account-and-external-id-tokens`.

<!-- op: spec=api-specs/Revolving_credit_-_Recurring_charges.yaml method=POST path=/v1/recurring-charge-plans operationId=create-recurring-charge-plan -->
### `POST /v1/recurring-charge-plans` — Create recurring charge plan

- **operationId:** `create-recurring-charge-plan`
- **Specification:** `api-specs/Revolving_credit_-_Recurring_charges.yaml` (Revolving credit - Recurring charges)
- **Server base URL(s):** `https://sandbox.pismolabs.io/recurring-charge`
- **Tags:** `Recurring charge plans`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Create a recurring charge plan. A recurring charge is a charge that is applied on a monthly basis for a fixed number of cycles. When you create a recurring charge plan, you specify the number of cycles and the amount of the monthly charge.
>
> Creating a plan does not activate it. You must link the plan to an account to activate the charge schedule defined in it.
>
> This endpoint generates a [Recurring charge plan created](https://developers.pismo.io/events/docs/balance-recurring-charge-plan-created-1) event.
>
> **NOTES:**
>
> - If an account is canceled while it has an active recurring charge attached to it, you want the recurring charge to be canceled, too, so that charges don't continue to accrue. To ensure this, set the multivalue program parameter [504 - RECURRING_CHARGE_FINAL_ACCOUNT_STATUS](doc:multivalue-parameters) to the value for an account status. Usually you use `CANCELLED` for this. When the account enters this status, the system cancels all pending recurring charges. (Note that if you provide more than one value, the system only uses the first one, even though this is a multivalue program parameter.)
>
> - This endpoint requires an account token — an access token encoded with an account ID. Tokens can expire quickly, which can result in a **401 Unauthorized** message.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `x-cid` | header | no | string | The Correlation IDentifier field is used to link related API requests and events. The x-cid can help the Pismo engineering team track everything related to a call. You can find the x-cid field in the response header from an API endpoint call.<br><br>If this field isn't passed, one is automatically generated.<br> | example: "5bb05174-4e80-11ea-b77f-2e728ce88125" |

#### Request body

Required: yes

**Content type `application/json`** — schema: object (schema `RecurringChargePlanRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `processing_code` | string (schema `ProcessingCode`) | yes | Processing code for the debit transaction.<br><br>If `split_transaction` is `false` (the default), each recurring payment is recorded as one debit transaction equal to the payment amount minus the discount, and `processing_code` is the processing code for that transaction.<br><br>If `split_transaction` is `true`, each recurring payment is recorded as two transactions: a debit transaction for the payment amount and a credit transaction for the discount. In this case, `processing_code` is the processsing code for the debit transaction, and `second_processing_code` is the processing code for the credit transaction.<br> | example: "99066" |
| `installment_amount` | number (schema `InstallmentAmount`) | yes | `installment_amount` is the full amount of a recurring charge before any discount is applied.<br> | format: "double"; example: 10.9 |
| `description` | string | no | Used if the recurring charge link description is not provided. Use "{counter}" to indicate where the cycle count should be placed.<br>Example: "{counter} Annuity" generates "2/12 Annuity" for the second of twelve recurring charges.<br>If "{counter}" is not present, the counter is placed at the end of the description. If no description is provided, the transaction type's description is used and the counter is not shown.<br> |  |
| `split_transaction` | boolean (schema `SplitTransaction`) | no | Use separate transactions for the amount of the recurring charge and the discount?<br><br>Suppose the recurring charge amount for a cycle is $20, and the discount is $2. If `split_transaction` is `false`, then one debit transaction for $18 ($20 - $2) is posted to the account for that cycle. It also appears as one debit transaction on the statement. If `split_transaction` is `true`, then two transactions are posted to the account—a debit transaction for $20 and a credit transaction for $2—and those two transactions appear on the statement. When `split_transaction` is `true`, `secondary_processing_code` is used to create the credit transaction.<br><br>Note: You aren't forced to specify a debit transaction with `processing_code` and a credit transaction with `secondary_processing_code`, but it's highly recommended. It's difficult to think of a scenario where you would want to do something else.<br> | default: false |
| `secondary_processing_code` | string (schema `SecondaryProcessingCode`) | no | Used to create the transaction for `secondary_installment_amount`. Normally, you should use a processing code for a credit transaction. | example: "99067" |
| `secondary_description` | string | no | Used to create a description for the secondary transaction. Use "{counter}" to indicate where the cycle count should be placed.<br>Example: "{counter} Annuity" generates "2/12 Annuity" for the second of twelve installments. If "{counter}" is not present, the counter is be placed at the end of the description. If no description is provided, the transaction type's description is used and the counter is not shown.<br> |  |
| `number_of_cycles` | integer (schema `NumberOfCycles`) | yes | Number of cycles to apply the charge plan. In other words, this is the number of recurring charges.<br>Must be greater than `first_cycles_to_discount` if used. Otherwise, it must be greater than 0.<br> | format: "int32"; example: 12 |
| `first_cycles_to_discount` | integer (schema `FirstCyclesToDiscount`) | no | The number of cycles the discount (defined by `discount_percentage`) should be applied to before reverting to the full charge.<br>For example, if `number_of_cycles` is 6 and `first_cycles_to_discount` is 2, then the discount is applied to cycles 1 and 2. The full charge is applied to cycles 3 through 6.<br>If present, `first_cycles_to_discount` must be positive and less than `number_of_cycles`."<br> | format: "int32"; example: 3 |
| `discount_percentage` | number (schema `DiscountPercentage`) | no | Percentage value to be discounted if `first_cycles_to_discount` is configured. Range: 0 to 100. | format: "double"; example: 50 |
| `minimum_spend_to_charge` | number (schema `MinimumSpendToCharge`) | no | Minimum debit amount on statement to enable cycle charging. If `minimum_spend_to_charge` is not configured, the charge plan does not check the debit statement amount. | format: "double"; example: 100 |
| `renew_method` | string (schema `RenewMethod`) | no | NO_RENEW: The link does not renew at the end of the cycle.<br>WITHOUT_DISCOUNT: The link is renewed at the end of the cycle, but the discounts registered in the plan are not applied.<br>WITH_DISCOUNT: The link is renewed at the end of the cycle, and the discounts registered in the plan are applied."<br> | enum: ["NO_RENEW", "WITHOUT_DISCOUNT", "WITH_DISCOUNT"]; example: "WITH_DISCOUNT" |
| `tracking_id` | string (schema `TrackingID`) | yes | Tracking ID | example: "3ea22692-a209-11eb-89a2-f73e179dcbc2" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK - The recurring charge plan was created. | `application/json`: object (schema `RecurringChargePlan`) |
| 400 | Bad Request |  |
| 409 | The specified resource status conflicts with the current request. |  |
| 500 | Internal server error |  |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `recurring_charge_plan_id` | integer (schema `RecurringChargePlanID`) | no | ID of recurring charge plan | format: "int64"; example: 115563 |
| `org_id` | string (schema `OrgID`) | no | Organization ID | example: "TN-cc8f8b89-233a-4582-9f36-63ee85278d6d" |
| `processing_code` | string (schema `ProcessingCode`) | no | Processing code for the debit transaction.<br><br>If `split_transaction` is `false` (the default), each recurring payment is recorded as one debit transaction equal to the payment amount minus the discount, and `processing_code` is the processing code for that transaction.<br><br>If `split_transaction` is `true`, each recurring payment is recorded as two transactions: a debit transaction for the payment amount and a credit transaction for the discount. In this case, `processing_code` is the processsing code for the debit transaction, and `second_processing_code` is the processing code for the credit transaction.<br> | example: "99066" |
| `installment_amount` | number (schema `InstallmentAmount`) | no | `installment_amount` is the full amount of a recurring charge before any discount is applied.<br> | format: "double"; example: 10.9 |
| `description` | string | no | Used if the recurring charge link description is not provided. Use "{counter}" to indicate where the cycle count should be placed. Example: "{counter} Annuity" generates "2/12 Annuity" for the second of twelve installments. If "{counter}" is not present, the counter is placed at the end of the description. If no description is provided, the transaction type's description is used and the counter is not shown.<br> |  |
| `split_transaction` | boolean (schema `SplitTransaction`) | no | Use separate transactions for the amount of the recurring charge and the discount?<br><br>Suppose the recurring charge amount for a cycle is $20, and the discount is $2. If `split_transaction` is `false`, then one debit transaction for $18 ($20 - $2) is posted to the account for that cycle. It also appears as one debit transaction on the statement. If `split_transaction` is `true`, then two transactions are posted to the account—a debit transaction for $20 and a credit transaction for $2—and those two transactions appear on the statement. When `split_transaction` is `true`, `secondary_processing_code` is used to create the credit transaction.<br><br>Note: You aren't forced to specify a debit transaction with `processing_code` and a credit transaction with `secondary_processing_code`, but it's highly recommended. It's difficult to think of a scenario where you would want to do something else.<br> | default: false |
| `secondary_processing_code` | string (schema `SecondaryProcessingCode`) | no | Used to create the transaction for `secondary_installment_amount`. Normally, you should use a processing code for a credit transaction. | example: "99067" |
| `secondary_description` | string | no | Used to create a description for the secondary transaction. Use "{counter}" to indicate where the cycle count should be placed. Example: "{counter} Annuity" generates "2/12 Annuity" for the second of twelve recurring charges. If "{counter}" is not present, the counter is placed at the end of the description. If no description is provided, the transaction type's description is used and the counter is not shown.<br> |  |
| `number_of_cycles` | integer (schema `NumberOfCycles`) | no | Number of cycles to apply the charge plan. In other words, this is the number of recurring charges.<br>Must be greater than `first_cycles_to_discount` if used. Otherwise, it must be greater than 0.<br> | format: "int32"; example: 12 |
| `first_cycles_to_discount` | integer (schema `FirstCyclesToDiscount`) | no | The number of cycles the discount (defined by `discount_percentage`) should be applied to before reverting to the full charge.<br>For example, if `number_of_cycles` is 6 and `first_cycles_to_discount` is 2, then the discount is applied to cycles 1 and 2. The full charge is applied to cycles 3 through 6.<br>If present, `first_cycles_to_discount` must be positive and less than `number_of_cycles`."<br> | format: "int32"; example: 3 |
| `discount_percentage` | number (schema `DiscountPercentage`) | no | Percentage value to be discounted if `first_cycles_to_discount` is configured. Range: 0 to 100. | format: "double"; example: 50 |
| `minimum_spend_to_charge` | number (schema `MinimumSpendToCharge`) | no | Minimum debit amount on statement to enable cycle charging. If `minimum_spend_to_charge` is not configured, the charge plan does not check the debit statement amount. | format: "double"; example: 100 |
| `renew_method` | string (schema `RenewMethod`) | no | NO_RENEW: The link does not renew at the end of the cycle.<br>WITHOUT_DISCOUNT: The link is renewed at the end of the cycle, but the discounts registered in the plan are not applied.<br>WITH_DISCOUNT: The link is renewed at the end of the cycle, and the discounts registered in the plan are applied."<br> | enum: ["NO_RENEW", "WITHOUT_DISCOUNT", "WITH_DISCOUNT"]; example: "WITH_DISCOUNT" |
| `tracking_id` | string (schema `TrackingID`) | no | Tracking ID | example: "3ea22692-a209-11eb-89a2-f73e179dcbc2" |
| `cid` | string (schema `CID`) | no | The Correlation IDentifier field is used to link related API requests and events. The x-cid can help the Pismo engineering team track everything related to a call. | example: "3ea22692-a209-11eb-89a2-f73e179dcbc2" |
| `created_at` | string (schema `CreatedAt`) | no | Date/time (GMT-3) that asset was registered on Pismo platform | example: "2023-03-30T12:26:41" |


#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `balance-recurring-charge-plan-created-1` | https://developers.pismo.io/events/docs/balance-recurring-charge-plan-created-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;409;500`, has examples `False`, emits events `1`, deprecated `False`.

Guides that link to this operation: `KU-AUTH-account-and-external-id-tokens`, `KU-CRED-recurring-charges`, `KU-EVT-recurring-charges-data-events`.

<!-- op: spec=api-specs/Revolving_credit_-_Recurring_charges.yaml method=GET path=/v1/recurring-charge-plans/{recurring_charge_plan_id} operationId=get-recurring-charge-plan -->
### `GET /v1/recurring-charge-plans/{recurring_charge_plan_id}` — Get recurring charge plan

- **operationId:** `get-recurring-charge-plan`
- **Specification:** `api-specs/Revolving_credit_-_Recurring_charges.yaml` (Revolving credit - Recurring charges)
- **Server base URL(s):** `https://sandbox.pismolabs.io/recurring-charge`
- **Tags:** `Recurring charge plans`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Gets a recurring charge plan by its ID.
>
> **NOTE:** This endpoint requires an account token — an access token encoded with an account ID. Tokens can expire quickly, which can result in a **401 Unauthorized** message.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `x-cid` | header | no | string | The Correlation IDentifier field is used to link related API requests and events. The x-cid can help the Pismo engineering team track everything related to a call. You can find the x-cid field in the response header from an API endpoint call.<br><br>If this field isn't passed, one is automatically generated.<br> | example: "5bb05174-4e80-11ea-b77f-2e728ce88125" |
| `recurring_charge_plan_id` | path | yes | integer | ID of the recurring charge plan | example: 98660282 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK - Indicates that the server accepted the request and found the plan. | `application/json`: object (schema `RecurringChargePlan`) |
| 400 | Bad Request |  |
| 404 | Not Found |  |
| 500 | Internal server error |  |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `recurring_charge_plan_id` | integer (schema `RecurringChargePlanID`) | no | ID of recurring charge plan | format: "int64"; example: 115563 |
| `org_id` | string (schema `OrgID`) | no | Organization ID | example: "TN-cc8f8b89-233a-4582-9f36-63ee85278d6d" |
| `processing_code` | string (schema `ProcessingCode`) | no | Processing code for the debit transaction.<br><br>If `split_transaction` is `false` (the default), each recurring payment is recorded as one debit transaction equal to the payment amount minus the discount, and `processing_code` is the processing code for that transaction.<br><br>If `split_transaction` is `true`, each recurring payment is recorded as two transactions: a debit transaction for the payment amount and a credit transaction for the discount. In this case, `processing_code` is the processsing code for the debit transaction, and `second_processing_code` is the processing code for the credit transaction.<br> | example: "99066" |
| `installment_amount` | number (schema `InstallmentAmount`) | no | `installment_amount` is the full amount of a recurring charge before any discount is applied.<br> | format: "double"; example: 10.9 |
| `description` | string | no | Used if the recurring charge link description is not provided. Use "{counter}" to indicate where the cycle count should be placed. Example: "{counter} Annuity" generates "2/12 Annuity" for the second of twelve installments. If "{counter}" is not present, the counter is placed at the end of the description. If no description is provided, the transaction type's description is used and the counter is not shown.<br> |  |
| `split_transaction` | boolean (schema `SplitTransaction`) | no | Use separate transactions for the amount of the recurring charge and the discount?<br><br>Suppose the recurring charge amount for a cycle is $20, and the discount is $2. If `split_transaction` is `false`, then one debit transaction for $18 ($20 - $2) is posted to the account for that cycle. It also appears as one debit transaction on the statement. If `split_transaction` is `true`, then two transactions are posted to the account—a debit transaction for $20 and a credit transaction for $2—and those two transactions appear on the statement. When `split_transaction` is `true`, `secondary_processing_code` is used to create the credit transaction.<br><br>Note: You aren't forced to specify a debit transaction with `processing_code` and a credit transaction with `secondary_processing_code`, but it's highly recommended. It's difficult to think of a scenario where you would want to do something else.<br> | default: false |
| `secondary_processing_code` | string (schema `SecondaryProcessingCode`) | no | Used to create the transaction for `secondary_installment_amount`. Normally, you should use a processing code for a credit transaction. | example: "99067" |
| `secondary_description` | string | no | Used to create a description for the secondary transaction. Use "{counter}" to indicate where the cycle count should be placed. Example: "{counter} Annuity" generates "2/12 Annuity" for the second of twelve recurring charges. If "{counter}" is not present, the counter is placed at the end of the description. If no description is provided, the transaction type's description is used and the counter is not shown.<br> |  |
| `number_of_cycles` | integer (schema `NumberOfCycles`) | no | Number of cycles to apply the charge plan. In other words, this is the number of recurring charges.<br>Must be greater than `first_cycles_to_discount` if used. Otherwise, it must be greater than 0.<br> | format: "int32"; example: 12 |
| `first_cycles_to_discount` | integer (schema `FirstCyclesToDiscount`) | no | The number of cycles the discount (defined by `discount_percentage`) should be applied to before reverting to the full charge.<br>For example, if `number_of_cycles` is 6 and `first_cycles_to_discount` is 2, then the discount is applied to cycles 1 and 2. The full charge is applied to cycles 3 through 6.<br>If present, `first_cycles_to_discount` must be positive and less than `number_of_cycles`."<br> | format: "int32"; example: 3 |
| `discount_percentage` | number (schema `DiscountPercentage`) | no | Percentage value to be discounted if `first_cycles_to_discount` is configured. Range: 0 to 100. | format: "double"; example: 50 |
| `minimum_spend_to_charge` | number (schema `MinimumSpendToCharge`) | no | Minimum debit amount on statement to enable cycle charging. If `minimum_spend_to_charge` is not configured, the charge plan does not check the debit statement amount. | format: "double"; example: 100 |
| `renew_method` | string (schema `RenewMethod`) | no | NO_RENEW: The link does not renew at the end of the cycle.<br>WITHOUT_DISCOUNT: The link is renewed at the end of the cycle, but the discounts registered in the plan are not applied.<br>WITH_DISCOUNT: The link is renewed at the end of the cycle, and the discounts registered in the plan are applied."<br> | enum: ["NO_RENEW", "WITHOUT_DISCOUNT", "WITH_DISCOUNT"]; example: "WITH_DISCOUNT" |
| `tracking_id` | string (schema `TrackingID`) | no | Tracking ID | example: "3ea22692-a209-11eb-89a2-f73e179dcbc2" |
| `cid` | string (schema `CID`) | no | The Correlation IDentifier field is used to link related API requests and events. The x-cid can help the Pismo engineering team track everything related to a call. | example: "3ea22692-a209-11eb-89a2-f73e179dcbc2" |
| `created_at` | string (schema `CreatedAt`) | no | Date/time (GMT-3) that asset was registered on Pismo platform | example: "2023-03-30T12:26:41" |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;404;500`, has examples `False`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-AUTH-account-and-external-id-tokens`.

<!-- op: spec=api-specs/Revolving_credit_-_Recurring_charges.yaml method=DELETE path=/v1/recurring-charge-plans/{recurring_charge_plan_id} operationId=disable-recurring-charge-plan -->
### `DELETE /v1/recurring-charge-plans/{recurring_charge_plan_id}` — Disable recurring charge plan

- **operationId:** `disable-recurring-charge-plan`
- **Specification:** `api-specs/Revolving_credit_-_Recurring_charges.yaml` (Revolving credit - Recurring charges)
- **Server base URL(s):** `https://sandbox.pismolabs.io/recurring-charge`
- **Tags:** `Recurring charge plans`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Disables an active recurring charge plan. Already disabled plans are unaffected.
> This endpoint generates a [Recurring charge plan disabled](https://developers.pismo.io/events/docs/balance-recurring-charge-plan-disabled-1) event.
>
> **NOTE:** This endpoint requires an account token — an access token encoded with an account ID. Tokens can expire quickly, which can result in a **401 Unauthorized** message.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `x-cid` | header | no | string | The Correlation IDentifier field is used to link related API requests and events. The x-cid can help the Pismo engineering team track everything related to a call. You can find the x-cid field in the response header from an API endpoint call.<br><br>If this field isn't passed, one is automatically generated.<br> | example: "5bb05174-4e80-11ea-b77f-2e728ce88125" |
| `recurring_charge_plan_id` | path | yes | integer | ID of the recurring charge plan | example: 98660282 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK - Indicates that the server accepted the request and disabled the plan. | `application/json`: object |
| 400 | Bad Request |  |
| 404 | Not Found |  |
| 500 | Internal server error |  |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `recurring_charge_plan_id` | integer (schema `RecurringChargePlanID`) | no | ID of recurring charge plan | format: "int64"; example: 115563 |
| `disabled_at` | string | no | Date and time plan was disabled | format: "date-time" |
| `disable_all_accounts` | boolean | no |  | example: false |


#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `balance-recurring-charge-plan-disabled-1` | https://developers.pismo.io/events/docs/balance-recurring-charge-plan-disabled-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;404;500`, has examples `True`, emits events `1`, deprecated `False`.

Guides that link to this operation: `KU-AUTH-account-and-external-id-tokens`, `KU-CRED-recurring-charges`, `KU-EVT-recurring-charges-data-events`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/RecurringChargePlan -->
### Schema `RecurringChargePlan`

Pointer: `#/components/schemas/RecurringChargePlan`. Type: object (schema `RecurringChargePlan`).

> Recurring charge plan

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `recurring_charge_plan_id` | integer (schema `RecurringChargePlanID`) | no | ID of recurring charge plan | format: "int64"; example: 115563 |
| `org_id` | string (schema `OrgID`) | no | Organization ID | example: "TN-cc8f8b89-233a-4582-9f36-63ee85278d6d" |
| `processing_code` | string (schema `ProcessingCode`) | no | Processing code for the debit transaction.<br><br>If `split_transaction` is `false` (the default), each recurring payment is recorded as one debit transaction equal to the payment amount minus the discount, and `processing_code` is the processing code for that transaction.<br><br>If `split_transaction` is `true`, each recurring payment is recorded as two transactions: a debit transaction for the payment amount and a credit transaction for the discount. In this case, `processing_code` is the processsing code for the debit transaction, and `second_processing_code` is the processing code for the credit transaction.<br> | example: "99066" |
| `installment_amount` | number (schema `InstallmentAmount`) | no | `installment_amount` is the full amount of a recurring charge before any discount is applied.<br> | format: "double"; example: 10.9 |
| `description` | string | no | Used if the recurring charge link description is not provided. Use "{counter}" to indicate where the cycle count should be placed. Example: "{counter} Annuity" generates "2/12 Annuity" for the second of twelve installments. If "{counter}" is not present, the counter is placed at the end of the description. If no description is provided, the transaction type's description is used and the counter is not shown.<br> |  |
| `split_transaction` | boolean (schema `SplitTransaction`) | no | Use separate transactions for the amount of the recurring charge and the discount?<br><br>Suppose the recurring charge amount for a cycle is $20, and the discount is $2. If `split_transaction` is `false`, then one debit transaction for $18 ($20 - $2) is posted to the account for that cycle. It also appears as one debit transaction on the statement. If `split_transaction` is `true`, then two transactions are posted to the account—a debit transaction for $20 and a credit transaction for $2—and those two transactions appear on the statement. When `split_transaction` is `true`, `secondary_processing_code` is used to create the credit transaction.<br><br>Note: You aren't forced to specify a debit transaction with `processing_code` and a credit transaction with `secondary_processing_code`, but it's highly recommended. It's difficult to think of a scenario where you would want to do something else.<br> | default: false |
| `secondary_processing_code` | string (schema `SecondaryProcessingCode`) | no | Used to create the transaction for `secondary_installment_amount`. Normally, you should use a processing code for a credit transaction. | example: "99067" |
| `secondary_description` | string | no | Used to create a description for the secondary transaction. Use "{counter}" to indicate where the cycle count should be placed. Example: "{counter} Annuity" generates "2/12 Annuity" for the second of twelve recurring charges. If "{counter}" is not present, the counter is placed at the end of the description. If no description is provided, the transaction type's description is used and the counter is not shown.<br> |  |
| `number_of_cycles` | integer (schema `NumberOfCycles`) | no | Number of cycles to apply the charge plan. In other words, this is the number of recurring charges.<br>Must be greater than `first_cycles_to_discount` if used. Otherwise, it must be greater than 0.<br> | format: "int32"; example: 12 |
| `first_cycles_to_discount` | integer (schema `FirstCyclesToDiscount`) | no | The number of cycles the discount (defined by `discount_percentage`) should be applied to before reverting to the full charge.<br>For example, if `number_of_cycles` is 6 and `first_cycles_to_discount` is 2, then the discount is applied to cycles 1 and 2. The full charge is applied to cycles 3 through 6.<br>If present, `first_cycles_to_discount` must be positive and less than `number_of_cycles`."<br> | format: "int32"; example: 3 |
| `discount_percentage` | number (schema `DiscountPercentage`) | no | Percentage value to be discounted if `first_cycles_to_discount` is configured. Range: 0 to 100. | format: "double"; example: 50 |
| `minimum_spend_to_charge` | number (schema `MinimumSpendToCharge`) | no | Minimum debit amount on statement to enable cycle charging. If `minimum_spend_to_charge` is not configured, the charge plan does not check the debit statement amount. | format: "double"; example: 100 |
| `renew_method` | string (schema `RenewMethod`) | no | NO_RENEW: The link does not renew at the end of the cycle.<br>WITHOUT_DISCOUNT: The link is renewed at the end of the cycle, but the discounts registered in the plan are not applied.<br>WITH_DISCOUNT: The link is renewed at the end of the cycle, and the discounts registered in the plan are applied."<br> | enum: ["NO_RENEW", "WITHOUT_DISCOUNT", "WITH_DISCOUNT"]; example: "WITH_DISCOUNT" |
| `tracking_id` | string (schema `TrackingID`) | no | Tracking ID | example: "3ea22692-a209-11eb-89a2-f73e179dcbc2" |
| `cid` | string (schema `CID`) | no | The Correlation IDentifier field is used to link related API requests and events. The x-cid can help the Pismo engineering team track everything related to a call. | example: "3ea22692-a209-11eb-89a2-f73e179dcbc2" |
| `created_at` | string (schema `CreatedAt`) | no | Date/time (GMT-3) that asset was registered on Pismo platform | example: "2023-03-30T12:26:41" |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Revolving_credit_-_Recurring_charges.yaml` | tag `Recurring charge plans`: GET /v1/recurring-charge-plans, POST /v1/recurring-charge-plans, GET /v1/recurring-charge-plans/{recurring_charge_plan_id}, DELETE /v1/recurring-charge-plans/{recurring_charge_plan_id} | https://github.com/PismoDevEx/pismo-api-specs | `d9ee67e0177041de…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-AUTH-account-and-external-id-tokens` — Endpoints that require account-specific or external-ID tokens
- `KU-CRED-recurring-charges` — Recurring charges
- `KU-EVT-catalogue-balance` — Event catalogue: balance
- `KU-EVT-recurring-charges-data-events` — Revolving credit - Recurring charges
