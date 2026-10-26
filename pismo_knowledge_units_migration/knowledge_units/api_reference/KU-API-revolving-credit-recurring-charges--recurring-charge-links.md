---
ku_id: KU-API-revolving-credit-recurring-charges--recurring-charge-links
title: 'API reference: Revolving credit - Recurring charges — Recurring charge links'
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
- get-recurring-charge-link
- create-recurring-charge-link
- delete-recurring-charge-link
- list-recurring-charge-links
- list-account-links
related_kus:
- KU-AUTH-account-and-external-id-tokens
- KU-CRED-recurring-charges
- KU-EVT-catalogue-balance
- KU-EVT-recurring-charges-data-events
specification_version: 1.0.0
---

# API reference: Revolving credit - Recurring charges — Recurring charge links

**KU ID:** `KU-API-revolving-credit-recurring-charges--recurring-charge-links` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 5 operation(s) tagged `Recurring charge links` in `api-specs/Revolving_credit_-_Recurring_charges.yaml` (“Revolving credit - Recurring charges”, version `1.0.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Endpoints to manage the link between recurring charge plans and accounts.

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `GET /v1/recurring-charge-plans/{recurring_charge_plan_id}/accounts/{account_id}` | `get-recurring-charge-link` | Get link between a plan and an account | no |
| `POST /v1/recurring-charge-plans/{recurring_charge_plan_id}/accounts/{account_id}` | `create-recurring-charge-link` | Create link | no |
| `DELETE /v1/recurring-charge-links/{recurring_charge_link_id}` | `delete-recurring-charge-link` | Delete recurring charge link | no |
| `GET /v1/recurring-charge-plans/{recurring_charge_plan_id}/accounts` | `list-recurring-charge-links` | List recurring charge plan links | no |
| `GET /v1/accounts/{account_id}/recurring-charge-plans` | `list-account-links` | List account links | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"} — Account access token. Tokens can expire quickly, which can result in an "Unauthorized" error.

## Operation contracts

<!-- op: spec=api-specs/Revolving_credit_-_Recurring_charges.yaml method=GET path=/v1/recurring-charge-plans/{recurring_charge_plan_id}/accounts/{account_id} operationId=get-recurring-charge-link -->
### `GET /v1/recurring-charge-plans/{recurring_charge_plan_id}/accounts/{account_id}` — Get link between a plan and an account

- **operationId:** `get-recurring-charge-link`
- **Specification:** `api-specs/Revolving_credit_-_Recurring_charges.yaml` (Revolving credit - Recurring charges)
- **Server base URL(s):** `https://sandbox.pismolabs.io/recurring-charge`
- **Tags:** `Recurring charge links`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Gets the link between a plan and an account, given the plan ID and account ID.
>
> **NOTE:** This endpoint requires an account token — an access token encoded with an account ID. Tokens can expire quickly, which can result in a **401 Unauthorized** message.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `x-cid` | header | no | string | The Correlation IDentifier field is used to link related API requests and events. The x-cid can help the Pismo engineering team track everything related to a call. You can find the x-cid field in the response header from an API endpoint call.<br><br>If this field isn't passed, one is automatically generated.<br> | example: "5bb05174-4e80-11ea-b77f-2e728ce88125" |
| `recurring_charge_plan_id` | path | yes | integer | ID of the recurring charge plan | example: 98660282 |
| `account_id` | path | yes | integer | Account ID | example: 6912345 |
| `page` | query | no | integer | Page number | default: 1; example: 3 |
| `perPage` | query | no | integer | Maximum number of items per page | default: 100; example: 10 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK - Indicates that the server accepted the request and found the link. | `application/json`: object (schema `PagedRecurringChargeLink`) |
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
| `items` | array of object (schema `RecurringChargeLink`) | no |  |  |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;500`, has examples `False`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-AUTH-account-and-external-id-tokens`.

<!-- op: spec=api-specs/Revolving_credit_-_Recurring_charges.yaml method=POST path=/v1/recurring-charge-plans/{recurring_charge_plan_id}/accounts/{account_id} operationId=create-recurring-charge-link -->
### `POST /v1/recurring-charge-plans/{recurring_charge_plan_id}/accounts/{account_id}` — Create link

- **operationId:** `create-recurring-charge-link`
- **Specification:** `api-specs/Revolving_credit_-_Recurring_charges.yaml` (Revolving credit - Recurring charges)
- **Server base URL(s):** `https://sandbox.pismolabs.io/recurring-charge`
- **Tags:** `Recurring charge links`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Creates a link between an active recurring charge plan and an account.
>
> This endpoint generates a [Recurring charge plan linked to account](https://developers.pismo.io/events/docs/balance-recurring-charge-plan-linked-to-account-1) event.
>
> **NOTE:** This endpoint requires an account token — an access token encoded with an account ID. Tokens can expire quickly, which can result in a **401 Unauthorized** message.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `x-cid` | header | no | string | The Correlation IDentifier field is used to link related API requests and events. The x-cid can help the Pismo engineering team track everything related to a call. You can find the x-cid field in the response header from an API endpoint call.<br><br>If this field isn't passed, one is automatically generated.<br> | example: "5bb05174-4e80-11ea-b77f-2e728ce88125" |
| `recurring_charge_plan_id` | path | yes | integer | ID of the recurring charge plan | example: 98660282 |
| `account_id` | path | yes | integer | Account ID | example: 6912345 |

#### Request body

Required: yes

**Content type `application/json`** — schema: object

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `description` | string (schema `LinkDescription`) | no | A description of the scheduled charge that's linked to the account. Use `counter` to specify where the cycle count should be placed.<br>Example: "Annuity {counter}" generates "Annuity 2/12" for the second of twelve annutities.<br>If `counter` is not present, the counter is placed at the end of the description.<br>If no description is configured, the description of the transaction type is used, and the counter is not shown.<br> | minLength: 1; maxLength: 100; example: "Link between an account and a recurring charge plan" |
| `tracking_id` | string (schema `TrackingID`) | yes | Tracking ID | example: "3ea22692-a209-11eb-89a2-f73e179dcbc2" |
| `post_installment_charge_on_current_cycle` | boolean (schema `PostInstallmentChargeOnCurrentCycle`) | no | When it's true, the charge will be apply on the current cycle otherwise, it will be apply on the next cycle | example: true |
| `start_installment_charge_in` | integer (schema `StartInstallmentChargeIn`) | no | Indicates when to start applying the charge. For example, if start_installment_charge_in is 3, then the charge is applied starting with cycle 3. It's not applied to cycles 1 and 2. If post_installment_charge_on_current_cycle is true, start_installment_charge_in should be null. If post_installment_charge_on_current_cycle is false, start_installment_charge_in is required. In this case, it must be greater than or equal to the current cycle and less than or equal to number_of_cycles. | example: 4 |
| `renew` | boolean (schema `Renew`) | no | When it's true the migration has a renovation | example: true |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK - Indicates that the server accepted the request and created the link. | `application/json`: object (schema `LinkCreationResponseDto`) |
| 400 | Bad Request |  |
| 404 | Not Found |  |
| 500 | Internal server error |  |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `recurring_charge_link_id` | integer (schema `RecurringChargeLinkID`) | no | ID of recurring charge link | format: "int64"; example: 98660282 |
| `account_id` | integer (schema `AccountID`) | no | Account ID | format: "int64"; example: 6912345 |
| `recurring_charge_plan_id` | integer (schema `RecurringChargePlanID`) | no | ID of recurring charge plan | format: "int64"; example: 115563 |
| `org_id` | string (schema `OrgID`) | no | Organization ID | example: "TN-cc8f8b89-233a-4582-9f36-63ee85278d6d" |
| `created_at` | string (schema `CreatedAt`) | no | Date/time (GMT-3) that asset was registered on Pismo platform | example: "2023-03-30T12:26:41" |
| `description` | string (schema `LinkDescription`) | no | A description of the scheduled charge that's linked to the account. Use `counter` to specify where the cycle count should be placed.<br>Example: "Annuity {counter}" generates "Annuity 2/12" for the second of twelve annutities.<br>If `counter` is not present, the counter is placed at the end of the description.<br>If no description is configured, the description of the transaction type is used, and the counter is not shown.<br> | minLength: 1; maxLength: 100; example: "Link between an account and a recurring charge plan" |
| `tracking_id` | string (schema `TrackingID`) | no | Tracking ID | example: "3ea22692-a209-11eb-89a2-f73e179dcbc2" |
| `creation_cid` | string (schema `CreationCID`) | no | CID for the creation event | example: "3ea22692-a209-11eb-89a2-f73e179dcbc2" |
| `post_installment_charge_on_current_cycle` | boolean (schema `PostInstallmentChargeOnCurrentCycle`) | no | When it's true, the charge will be apply on the current cycle otherwise, it will be apply on the next cycle | example: true |
| `start_installment_charge_in` | integer (schema `StartInstallmentChargeIn`) | no | Indicates when to start applying the charge. For example, if start_installment_charge_in is 3, then the charge is applied starting with cycle 3. It's not applied to cycles 1 and 2. If post_installment_charge_on_current_cycle is true, start_installment_charge_in should be null. If post_installment_charge_on_current_cycle is false, start_installment_charge_in is required. In this case, it must be greater than or equal to the current cycle and less than or equal to number_of_cycles. | example: 4 |
| `renew` | boolean (schema `Renew`) | no | When it's true the migration has a renovation | example: true |


#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `balance-recurring-charge-plan-linked-to-account-1` | https://developers.pismo.io/events/docs/balance-recurring-charge-plan-linked-to-account-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;404;500`, has examples `False`, emits events `1`, deprecated `False`.

Guides that link to this operation: `KU-AUTH-account-and-external-id-tokens`, `KU-CRED-recurring-charges`, `KU-EVT-recurring-charges-data-events`.

<!-- op: spec=api-specs/Revolving_credit_-_Recurring_charges.yaml method=DELETE path=/v1/recurring-charge-links/{recurring_charge_link_id} operationId=delete-recurring-charge-link -->
### `DELETE /v1/recurring-charge-links/{recurring_charge_link_id}` — Delete recurring charge link

- **operationId:** `delete-recurring-charge-link`
- **Specification:** `api-specs/Revolving_credit_-_Recurring_charges.yaml` (Revolving credit - Recurring charges)
- **Server base URL(s):** `https://sandbox.pismolabs.io/recurring-charge`
- **Tags:** `Recurring charge links`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Cancels the link between a recurring charge plan and an account. Results in the cancellation of all `PENDING` charges for that link. Already canceled links are unaffected.
> This endpoint generates a [Recurring charge plan unlinked from account](https://developers.pismo.io/events/docs/balance-recurring-charge-plan-unlinked-from-account-1) event.
>
> **NOTE:** This endpoint requires an account token — an access token encoded with an account ID. Tokens can expire quickly, which can result in a **401 Unauthorized** message.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `x-cid` | header | no | string | The Correlation IDentifier field is used to link related API requests and events. The x-cid can help the Pismo engineering team track everything related to a call. You can find the x-cid field in the response header from an API endpoint call.<br><br>If this field isn't passed, one is automatically generated.<br> | example: "5bb05174-4e80-11ea-b77f-2e728ce88125" |
| `recurring_charge_link_id` | path | yes | integer | ID of the link between a plan and an account | example: 98660282 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK - Indicates that the server accepted the request and canceled the link. | `application/json`: object (schema `RecurringChargeLink`) |
| 400 | Bad Request |  |
| 409 | The specified resource status conflicts with the current request. |  |
| 500 | Internal server error |  |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `recurring_charge_link_id` | integer (schema `RecurringChargeLinkID`) | no | ID of recurring charge link | format: "int64"; example: 98660282 |
| `account_id` | integer (schema `AccountID`) | no | Account ID | format: "int64"; example: 6912345 |
| `recurring_charge_plan_id` | integer (schema `RecurringChargePlanID`) | no | ID of recurring charge plan | format: "int64"; example: 115563 |
| `previous_recurring_charge_link_id` | integer (schema `PreviousRecurringChargeLinkID`) | no | ID of previous recurring charge link | format: "int64" |
| `org_id` | string (schema `OrgID`) | no | Organization ID | example: "TN-cc8f8b89-233a-4582-9f36-63ee85278d6d" |
| `created_at` | string (schema `CreatedAt`) | no | Date/time (GMT-3) that asset was registered on Pismo platform | example: "2023-03-30T12:26:41" |
| `cancelled_at` | string (schema `CanceledAt`) | no | Date/time (GMT-3) that link was canceled | example: "2023-03-30T12:26:41" |
| `end_date` | string (schema `EndDate`) | no | End date for link (GMT-3). When the final charge for a link is made, `end_date` gets populated. | format: "date-time"; example: "2023-03-30T12:26:41" |
| `description` | string (schema `LinkDescription`) | no | A description of the scheduled charge that's linked to the account. Use `counter` to specify where the cycle count should be placed.<br>Example: "Annuity {counter}" generates "Annuity 2/12" for the second of twelve annutities.<br>If `counter` is not present, the counter is placed at the end of the description.<br>If no description is configured, the description of the transaction type is used, and the counter is not shown.<br> | minLength: 1; maxLength: 100; example: "Link between an account and a recurring charge plan" |
| `tracking_id` | string (schema `TrackingID`) | no | Tracking ID | example: "3ea22692-a209-11eb-89a2-f73e179dcbc2" |
| `creation_cid` | string (schema `CreationCID`) | no | CID for the creation event | example: "3ea22692-a209-11eb-89a2-f73e179dcbc2" |
| `cancellation_cid` | string (schema `CancellationCID`) | no | CID for the cancellation event | example: "3ea22692-a209-11eb-89a2-f73e179dcbc2" |


#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `balance-recurring-charge-plan-unlinked-from-account-1` | https://developers.pismo.io/events/docs/balance-recurring-charge-plan-unlinked-from-account-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;409;500`, has examples `False`, emits events `1`, deprecated `False`.

Guides that link to this operation: `KU-AUTH-account-and-external-id-tokens`, `KU-CRED-recurring-charges`, `KU-EVT-recurring-charges-data-events`.

<!-- op: spec=api-specs/Revolving_credit_-_Recurring_charges.yaml method=GET path=/v1/recurring-charge-plans/{recurring_charge_plan_id}/accounts operationId=list-recurring-charge-links -->
### `GET /v1/recurring-charge-plans/{recurring_charge_plan_id}/accounts` — List recurring charge plan links

- **operationId:** `list-recurring-charge-links`
- **Specification:** `api-specs/Revolving_credit_-_Recurring_charges.yaml` (Revolving credit - Recurring charges)
- **Server base URL(s):** `https://sandbox.pismolabs.io/recurring-charge`
- **Tags:** `Recurring charge links`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Gets all the links for a plan, given the plan ID.
>
> **NOTE:** This endpoint requires an account token — an access token encoded with an account ID. Tokens can expire quickly, which can result in a **401 Unauthorized** message.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `x-cid` | header | no | string | The Correlation IDentifier field is used to link related API requests and events. The x-cid can help the Pismo engineering team track everything related to a call. You can find the x-cid field in the response header from an API endpoint call.<br><br>If this field isn't passed, one is automatically generated.<br> | example: "5bb05174-4e80-11ea-b77f-2e728ce88125" |
| `recurring_charge_plan_id` | path | yes | integer | ID of the recurring charge plan | example: 98660282 |
| `page` | query | no | integer | Page number | default: 1; example: 3 |
| `perPage` | query | no | integer | Maximum number of items per page | default: 100; example: 10 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK - Indicates that the server accepted the request and returned the list of links. If no links are found, an empty array is returned and `total_items` is 0. | `application/json`: object (schema `PagedRecurringChargeLink`) |
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
| `items` | array of object (schema `RecurringChargeLink`) | no |  |  |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;500`, has examples `False`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-AUTH-account-and-external-id-tokens`.

<!-- op: spec=api-specs/Revolving_credit_-_Recurring_charges.yaml method=GET path=/v1/accounts/{account_id}/recurring-charge-plans operationId=list-account-links -->
### `GET /v1/accounts/{account_id}/recurring-charge-plans` — List account links

- **operationId:** `list-account-links`
- **Specification:** `api-specs/Revolving_credit_-_Recurring_charges.yaml` (Revolving credit - Recurring charges)
- **Server base URL(s):** `https://sandbox.pismolabs.io/recurring-charge`
- **Tags:** `Recurring charge links`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Gets the links for a given account.
>
> **NOTE:** This endpoint requires an account token — an access token encoded with an account ID. Tokens can expire quickly, which can result in a **401 Unauthorized** message.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `x-cid` | header | no | string | The Correlation IDentifier field is used to link related API requests and events. The x-cid can help the Pismo engineering team track everything related to a call. You can find the x-cid field in the response header from an API endpoint call.<br><br>If this field isn't passed, one is automatically generated.<br> | example: "5bb05174-4e80-11ea-b77f-2e728ce88125" |
| `account_id` | path | yes | integer | Account ID | example: 6912345 |
| `page` | query | no | integer | Page number | default: 1; example: 3 |
| `perPage` | query | no | integer | Maximum number of items per page | default: 100; example: 10 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK - Indicates that the server accepted the request and returned the list of links. If no links are found, an empty array is returned and `total_items` is 0. | `application/json`: object (schema `PagedRecurringChargeLink`) |
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
| `items` | array of object (schema `RecurringChargeLink`) | no |  |  |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;500`, has examples `False`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-AUTH-account-and-external-id-tokens`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/RecurringChargeLink -->
### Schema `RecurringChargeLink`

Pointer: `#/components/schemas/RecurringChargeLink`. Type: object (schema `RecurringChargeLink`).

> Link between a plan and an account

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `recurring_charge_link_id` | integer (schema `RecurringChargeLinkID`) | no | ID of recurring charge link | format: "int64"; example: 98660282 |
| `account_id` | integer (schema `AccountID`) | no | Account ID | format: "int64"; example: 6912345 |
| `recurring_charge_plan_id` | integer (schema `RecurringChargePlanID`) | no | ID of recurring charge plan | format: "int64"; example: 115563 |
| `previous_recurring_charge_link_id` | integer (schema `PreviousRecurringChargeLinkID`) | no | ID of previous recurring charge link | format: "int64" |
| `org_id` | string (schema `OrgID`) | no | Organization ID | example: "TN-cc8f8b89-233a-4582-9f36-63ee85278d6d" |
| `created_at` | string (schema `CreatedAt`) | no | Date/time (GMT-3) that asset was registered on Pismo platform | example: "2023-03-30T12:26:41" |
| `cancelled_at` | string (schema `CanceledAt`) | no | Date/time (GMT-3) that link was canceled | example: "2023-03-30T12:26:41" |
| `end_date` | string (schema `EndDate`) | no | End date for link (GMT-3). When the final charge for a link is made, `end_date` gets populated. | format: "date-time"; example: "2023-03-30T12:26:41" |
| `description` | string (schema `LinkDescription`) | no | A description of the scheduled charge that's linked to the account. Use `counter` to specify where the cycle count should be placed.<br>Example: "Annuity {counter}" generates "Annuity 2/12" for the second of twelve annutities.<br>If `counter` is not present, the counter is placed at the end of the description.<br>If no description is configured, the description of the transaction type is used, and the counter is not shown.<br> | minLength: 1; maxLength: 100; example: "Link between an account and a recurring charge plan" |
| `tracking_id` | string (schema `TrackingID`) | no | Tracking ID | example: "3ea22692-a209-11eb-89a2-f73e179dcbc2" |
| `creation_cid` | string (schema `CreationCID`) | no | CID for the creation event | example: "3ea22692-a209-11eb-89a2-f73e179dcbc2" |
| `cancellation_cid` | string (schema `CancellationCID`) | no | CID for the cancellation event | example: "3ea22692-a209-11eb-89a2-f73e179dcbc2" |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Revolving_credit_-_Recurring_charges.yaml` | tag `Recurring charge links`: GET /v1/recurring-charge-plans/{recurring_charge_plan_id}/accounts/{account_id}, POST /v1/recurring-charge-plans/{recurring_charge_plan_id}/accounts/{account_id}, DELETE /v1/recurring-charge-links/{recurring_charge_link_id}, GET /v1/recurring-charge-plans/{recurring_charge_plan_id}/accounts, GET /v1/accounts/{account_id}/recurring-charge-plans | https://github.com/PismoDevEx/pismo-api-specs | `d9ee67e0177041de…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-AUTH-account-and-external-id-tokens` — Endpoints that require account-specific or external-ID tokens
- `KU-CRED-recurring-charges` — Recurring charges
- `KU-EVT-catalogue-balance` — Event catalogue: balance
- `KU-EVT-recurring-charges-data-events` — Revolving credit - Recurring charges
