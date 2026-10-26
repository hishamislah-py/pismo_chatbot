---
ku_id: KU-API-seller-management-marketplace--marketplace-creditor-operations
title: 'API reference: Seller management - Marketplace — Marketplace creditor operations'
category: api_reference
ku_type: api_reference
lifecycle: current
sources:
- path: api-specs/Seller_management_-_Marketplace.yaml
  sha256: 8ffe617b35e772cca857f195c1384b6d7287d6e8bcbf553ed99c3eed14924d2b
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
- GetCreditorsOperationsV2
- PutCreditorsOperationsV2
- PostCreditorsOperationsV2
- PostCreditorsOperations
- PatchCreditorOperationByIdV1
- GetCreditorOperationById
- PutUpdateCreditorOperationById
- DeleteCreditorOperationById
- GetCreditorOperationsByMerchantIDAndMarketplaceID
- GetMerchantsCreditorsV1
related_kus:
- KU-EVT-catalogue-marketplace
- KU-EVT-marketplace-data-events
- KU-SELL-get-started-seller-management
- KU-SELL-how-merchant-settlements-are-processed
- KU-SELL-managing-merchant-transactions
- KU-SELL-seller-management-overview-and-onboarding
- KU-SELL-seller-marketplace-implementation-steps
specification_version: 1.0.0
---

# API reference: Seller management - Marketplace — Marketplace creditor operations

**KU ID:** `KU-API-seller-management-marketplace--marketplace-creditor-operations` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 10 operation(s) tagged `Marketplace creditor operations` in `api-specs/Seller_management_-_Marketplace.yaml` (“Seller management - Marketplace”, version `1.0.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Endpoints for creditors operations associated with the marketplace

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `GET /v2/marketplaces/{marketplaceId}/creditors-operations` | `GetCreditorsOperationsV2` | List marketplace creditor operations | no |
| `PUT /v2/marketplaces/{marketplaceId}/creditors-operations` | `PutCreditorsOperationsV2` | Update creditor operations | no |
| `POST /v2/marketplaces/{marketplaceId}/creditors-operations` | `PostCreditorsOperationsV2` | Create marketplace creditor operations | no |
| `POST /marketplaces/{marketplaceId}/creditors-operations` | `PostCreditorsOperations` | Create creditor operation | no |
| `PATCH /v1/marketplaces/{marketplaceId}/creditors-operations/{creditorOperationId}` | `PatchCreditorOperationByIdV1` | Patch creditor operation | no |
| `GET /marketplaces/{marketplaceId}/creditors-operations/{creditorOperationId}` | `GetCreditorOperationById` | Get creditor operation | no |
| `PUT /marketplaces/{marketplaceId}/creditors-operations/{creditorOperationId}` | `PutUpdateCreditorOperationById` | Update creditor operation | no |
| `DELETE /marketplaces/{marketplaceId}/creditors-operations/{creditorOperationId}` | `DeleteCreditorOperationById` | Delete creditor operation | no |
| `GET /marketplaces/{marketplaceId}/merchants/{merchantId}/creditors-operations` | `GetCreditorOperationsByMerchantIDAndMarketplaceID` | List creditor operations for marketplace and merchant | no |
| `GET /marketplaces/v1/{marketplaceId}/merchants-creditors` | `GetMerchantsCreditorsV1` | List merchant creditors | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"}

## Operation contracts

<!-- op: spec=api-specs/Seller_management_-_Marketplace.yaml method=GET path=/v2/marketplaces/{marketplaceId}/creditors-operations operationId=GetCreditorsOperationsV2 -->
### `GET /v2/marketplaces/{marketplaceId}/creditors-operations` — List marketplace creditor operations

- **operationId:** `GetCreditorsOperationsV2`
- **Specification:** `api-specs/Seller_management_-_Marketplace.yaml` (Seller management - Marketplace)
- **Server base URL(s):** `https://sandbox.pismolabs.io/marketplace`
- **Tags:** `Marketplace creditor operations`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> List creditor operations for the specified marketplace.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `marketplaceId` | path | yes | integer | Marketplace ID | format: "int64"; example: 1 |
| `page` | query | no | number | Current page number | format: "int64"; example: 2 |
| `Authorization` | header | no | string | Authorization token. This is a regular access token, which does not need to include an account ID. | example: "Bearer 1JI12J39182H39182JDIOAWJ%=" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object |
| 400 | Bad Request |  |
| 401 | Access token is missing or invalid |  |
| 500 | Internal server error |  |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `current_page` | integer (schema `CurrentPage`) | no | Current page number | default: 1; format: "int32"; example: 2 |
| `per_page` | integer (schema `PerPage`) | no | Number of result items per page | default: 10; format: "int32"; example: 50 |
| `has_next` | boolean (schema `HasNext`) | no | Indicates whether there are more results pages after the current one. | example: false |
| `items` | array of object (schema `GETCreditorsOperationsWithFeesResponse`) | no |  |  |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;500`, has examples `False`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Seller_management_-_Marketplace.yaml method=PUT path=/v2/marketplaces/{marketplaceId}/creditors-operations operationId=PutCreditorsOperationsV2 -->
### `PUT /v2/marketplaces/{marketplaceId}/creditors-operations` — Update creditor operations

- **operationId:** `PutCreditorsOperationsV2`
- **Specification:** `api-specs/Seller_management_-_Marketplace.yaml` (Seller management - Marketplace)
- **Server base URL(s):** `https://sandbox.pismolabs.io/marketplace`
- **Tags:** `Marketplace creditor operations`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Update fields for all creditor operations that match a provided filter criteria: `processing_code`, `start_date`, or `installments`.
>
> This endpoint generates [Marketplace creditor operation updated](https://developers.pismo.io/events/docs/marketplace-marketplace-creditor-operation-updated-1) events.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `marketplaceId` | path | yes | integer | Marketplace ID | format: "int64"; example: 1 |
| `Authorization` | header | no | string | Authorization token. This is a regular access token, which does not need to include an account ID. | example: "Bearer 1JI12J39182H39182JDIOAWJ%=" |

#### Request body

Required: yes

> Request body

**Content type `application/json`** — schema: object (schema `PutCreditorOperationV2`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `merchant_ids` | array of integer | no | List of merchants that this creditor operation applies to | maxItems: 1000; items.format: "int64" |
| `filter` | object | no | Filter to select the creditor operation to update |  |
| `filter.installments` | integer (schema `Installments`) | no | Number of installments | format: "int32"; minimum: 1; example: 3 |
| `filter.processing_code` | string (schema `ProcessingCode`) | no | A processing code is a custom alphanumeric identifier that defines the type of financial operation that the Pismo platform handles.<br><br>For more information, refer to [Processing codes](doc:processing-codes-and-transaction-types).<br> | example: "700203" |
| `filter.start_date` | string (schema `StartDate`) | no | Date from which this operation is considered active. Format = yyyy-mm-dd. | format: "date"; example: "2022-12-21" |
| `creditor_operation` | object | no | Creditor operation configuration |  |
| `creditor_operation.first_installment_days_to_payment` | integer (schema `FirstInstallmentDaysToPayment`) | no | Number of days before first installment is due | format: "int32"; minimum: 1; example: 2 |
| `creditor_operation.n_installment_days_to_payment` | integer (schema `NthInstallmentDaysToPayment`) | no | Number of days before each subsequent installment is due.<br>The customer has `first_installment_days_to_payment` days to pay the first installment.<br>They have `n_installment_days_to_payment` days to pay each installment after that.<br> | format: "int32"; minimum: 1; example: 2 |
| `creditor_operation.mdr` | number (schema `Mdr`) | no | MDR fee. The Merchant Discount Rate (MDR) is the rate charged to a merchant for payment processing services on debit and credit card transactions.<br>The merchant must set up this service and agree to the rate before accepting debit and credit cards as payment.<br> | default: 0; format: "float"; example: 0.01 |
| `creditor_operation.transaction_fee` | number (schema `TransactionFee`) | no | Transaction fee | default: 0; example: 5 |
| `creditor_operation.matched_mdr` | boolean (schema `MatchedMdr`) | no | Indicates whether this is a matched Merchant Discount Rate (MDR). If `false`, the fixed transaction fee and the MDR amount is applied only to the first installment. The default value is `false`.<br> | default: false; example: true |
| `creditor_operation.matched_settlement` | boolean (schema `MatchedSettlement`) | no | Indicates whether this is a matched settlement. A matched settlement means the settlement is paid in several batches, whereas `false` indicates the full amount is paid in one single payment. The default value is `false`. | default: false; example: true |
| `creditor_operation.work_days` | boolean (schema `WorkDays`) | no | If `true`, only business days are used to calculate the date of the next payment.<br> | default: false; example: false |
| `creditor_operation.fees` | array of object (schema `Fee`) (schema `Fees`) | no | Creditor operation additional fees | example: [{"name": "EMISSION_FEE", "value": 1.5}, {"name": "MAINTENANCE_FEE", "value": 0.01}] |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 204 | No Content |  |
| 400 | Bad Request |  |
| 401 | Access token is missing or invalid |  |
| 500 | Internal server error |  |


#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `marketplace-marketplace-creditor-operation-updated-1` | https://developers.pismo.io/events/docs/marketplace-marketplace-creditor-operation-updated-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `204;400;401;500`, has examples `False`, emits events `1`, deprecated `False`.

<!-- op: spec=api-specs/Seller_management_-_Marketplace.yaml method=POST path=/v2/marketplaces/{marketplaceId}/creditors-operations operationId=PostCreditorsOperationsV2 -->
### `POST /v2/marketplaces/{marketplaceId}/creditors-operations` — Create marketplace creditor operations

- **operationId:** `PostCreditorsOperationsV2`
- **Specification:** `api-specs/Seller_management_-_Marketplace.yaml` (Seller management - Marketplace)
- **Server base URL(s):** `https://sandbox.pismolabs.io/marketplace`
- **Tags:** `Marketplace creditor operations`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Create multiple creditor operations for the specified marketplace.
>
> This endpoint creates one creditor operation for each merchant ID and each installment in the request body. The values of `processing_code` and `start_date` are replicated to each creditor operation created based on the installments configuration.
>
> This endpoint generates [Marketplace creditor operation created](https://developers.pismo.io/events/docs/marketplace-marketplace-creditor-operation-created-1) events.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `marketplaceId` | path | yes | integer | Marketplace ID | format: "int64"; example: 1 |
| `Authorization` | header | no | string | Authorization token. This is a regular access token, which does not need to include an account ID. | example: "Bearer 1JI12J39182H39182JDIOAWJ%=" |

#### Request body

Required: yes

> Request body

**Content type `application/json`** — schema: object (schema `PostCreditorOperationV2`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `merchant_ids` | array of integer | yes | List of merchants that this creditor operation applies to | maxItems: 1000; items.format: "int64" |
| `creditor_operation` | object | yes | Creditor operation information |  |
| `creditor_operation.processing_code` | string (schema `ProcessingCode`) | yes | A processing code is a custom alphanumeric identifier that defines the type of financial operation that the Pismo platform handles.<br><br>For more information, refer to [Processing codes](doc:processing-codes-and-transaction-types).<br> | example: "700203" |
| `creditor_operation.start_date` | string (schema `StartDate`) | yes | Date from which this operation is considered active. Format = yyyy-mm-dd. | format: "date"; example: "2022-12-21" |
| `creditor_operation.installments` | array of object | yes | Configuration for each installment | maxItems: 12 |
| `creditor_operation.installments[].installment` | number | yes | Installment number |  |
| `creditor_operation.installments[].first_installment_days_to_payment` | integer (schema `FirstInstallmentDaysToPayment`) | no | Number of days before first installment is due | format: "int32"; minimum: 1; example: 2 |
| `creditor_operation.installments[].n_installment_days_to_payment` | integer (schema `NthInstallmentDaysToPayment`) | no | Number of days before each subsequent installment is due.<br>The customer has `first_installment_days_to_payment` days to pay the first installment.<br>They have `n_installment_days_to_payment` days to pay each installment after that.<br> | format: "int32"; minimum: 1; example: 2 |
| `creditor_operation.installments[].transaction_fee` | number (schema `TransactionFee`) | no | Transaction fee | default: 0; example: 5 |
| `creditor_operation.installments[].mdr` | number (schema `Mdr`) | no | MDR fee. The Merchant Discount Rate (MDR) is the rate charged to a merchant for payment processing services on debit and credit card transactions.<br>The merchant must set up this service and agree to the rate before accepting debit and credit cards as payment.<br> | default: 0; format: "float"; example: 0.01 |
| `creditor_operation.installments[].matched_mdr` | boolean (schema `MatchedMdr`) | no | Indicates whether this is a matched Merchant Discount Rate (MDR). If `false`, the fixed transaction fee and the MDR amount is applied only to the first installment. The default value is `false`.<br> | default: false; example: true |
| `creditor_operation.installments[].matched_settlement` | boolean (schema `MatchedSettlement`) | no | Indicates whether this is a matched settlement. A matched settlement means the settlement is paid in several batches, whereas `false` indicates the full amount is paid in one single payment. The default value is `false`. | default: false; example: true |
| `creditor_operation.installments[].work_days` | boolean (schema `WorkDays`) | no | If `true`, only business days are used to calculate the date of the next payment.<br> | default: false; example: false |
| `creditor_operation.installments[].fees` | array of object (schema `Fee`) (schema `Fees`) | no | Creditor operation additional fees | example: [{"name": "EMISSION_FEE", "value": 1.5}, {"name": "MAINTENANCE_FEE", "value": 0.01}] |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | Created |  |
| 400 | Bad Request |  |
| 401 | Access token is missing or invalid |  |
| 409 | Conflict. One or more submitted creditor operations already exist for the specified merchants. |  |
| 500 | Internal server error |  |


#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `marketplace-marketplace-creditor-operation-created-1` | https://developers.pismo.io/events/docs/marketplace-marketplace-creditor-operation-created-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `201;400;401;409;500`, has examples `False`, emits events `1`, deprecated `False`.

<!-- op: spec=api-specs/Seller_management_-_Marketplace.yaml method=POST path=/marketplaces/{marketplaceId}/creditors-operations operationId=PostCreditorsOperations -->
### `POST /marketplaces/{marketplaceId}/creditors-operations` — Create creditor operation

- **operationId:** `PostCreditorsOperations`
- **Specification:** `api-specs/Seller_management_-_Marketplace.yaml` (Seller management - Marketplace)
- **Server base URL(s):** `https://sandbox.pismolabs.io/marketplace`
- **Tags:** `Marketplace creditor operations`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Create a creditor operation.
>
> This endpoint generates a [Marketplace creditor operation created](https://developers.pismo.io/events/docs/marketplace-marketplace-creditor-operation-created-1) event.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `marketplaceId` | path | yes | integer | Marketplace ID | format: "int64"; example: 1 |
| `Authorization` | header | no | string | Authorization token. This is a regular access token, which does not need to include an account ID. | example: "Bearer 1JI12J39182H39182JDIOAWJ%=" |
| `Content-Type` | header | no | string | Content type | example: "application/json" |

#### Request body

Required: yes

> Request body

**Content type `application/json`** — schema: object (schema `PostCreditorOperation`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `creditor_id` | integer (schema `CreditorID`) | yes | Creditor ID. This represents the owner of a business. | format: "int64"; example: 12345 |
| `first_installment_days_to_payment` | integer (schema `FirstInstallmentDaysToPayment`) | yes | Number of days before first installment is due | format: "int32"; minimum: 1; example: 2 |
| `installments` | integer (schema `Installments`) | yes | Number of installments | format: "int32"; minimum: 1; example: 3 |
| `n_installment_days_to_payment` | integer (schema `NthInstallmentDaysToPayment`) | yes | Number of days before each subsequent installment is due.<br>The customer has `first_installment_days_to_payment` days to pay the first installment.<br>They have `n_installment_days_to_payment` days to pay each installment after that.<br> | format: "int32"; minimum: 1; example: 2 |
| `card_not_present_allowed` | boolean (schema `CardNotPresentAllowed`) | no | Indicates whether a card-not-present (CNP) transaction is allowed. A CNP transaction is a purchase made virtually, without processing a physical card via a card reader or terminal (and without manually entering a PIN). | default: false; example: true |
| `doc_number_allowed` | boolean (schema `DocNumberAllowed`) | no | Indicates whether document number is allowed. | default: false; example: true |
| `matched_mdr` | boolean (schema `MatchedMdr`) | no | Indicates whether this is a matched Merchant Discount Rate (MDR). If `false`, the fixed transaction fee and the MDR amount is applied only to the first installment. The default value is `false`.<br> | default: false; example: true |
| `matched_settlement` | boolean (schema `MatchedSettlement`) | no | Indicates whether this is a matched settlement. A matched settlement means the settlement is paid in several batches, whereas `false` indicates the full amount is paid in one single payment. The default value is `false`. | default: false; example: true |
| `mdr` | number (schema `Mdr`) | no | MDR fee. The Merchant Discount Rate (MDR) is the rate charged to a merchant for payment processing services on debit and credit card transactions.<br>The merchant must set up this service and agree to the rate before accepting debit and credit cards as payment.<br> | default: 0; format: "float"; example: 0.01 |
| `network` | string (schema `Network`) | no | Card network | example: "Visa" |
| `operation_type_id` | integer (schema `OperationTypeID`) | no | Operation type ID defined by the Pismo platform.<br><br>An operation type ID is an operation type processing code, which is a custom alphanumeric identifier that defines how the Pismo platform handles a certain financial operation type. See [Processing codes and transaction types](https://developers.pismo.io/pismo-docs/docs/processing-codes-and-transaction-types) for more information.<br><br><b>Note:</b> Either `operation_type_id` or `processing_code` is **required**. Using `processing_code` is recommended as `operation_type_id` is deprecated and scheduled for removal.<br> | format: "int64"; deprecated: true; example: 4 |
| `processing_code` | string (schema `ProcessingCode`) | no | A processing code is a custom alphanumeric identifier that defines the type of financial operation that the Pismo platform handles.<br><br>For more information, refer to [Processing codes](doc:processing-codes-and-transaction-types).<br> | example: "700203" |
| `start_date` | string (schema `StartDate`) | no | Date from which this operation is considered active. Format = yyyy-mm-dd. | format: "date"; example: "2022-12-21" |
| `transaction_fee` | number (schema `TransactionFee`) | no | Transaction fee | default: 0; example: 5 |
| `work_days` | boolean (schema `WorkDays`) | no | If `true`, only business days are used to calculate the date of the next payment.<br> | default: false; example: false |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object |
| 400 | Bad Request |  |
| 401 | Access token is missing or invalid |  |
| 500 | Internal server error |  |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | integer (schema `CreditorOperationID`) | no | Creditor operation ID | format: "int64"; example: 128427 |
| `success` | string | no | Indicates whether the creditor was successfully created. | example: "true" |


#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `marketplace-marketplace-creditor-operation-created-1` | https://developers.pismo.io/events/docs/marketplace-marketplace-creditor-operation-created-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;500`, has examples `True`, emits events `1`, deprecated `False`.

Guides that link to this operation: `KU-EVT-marketplace-data-events`, `KU-SELL-get-started-seller-management`, `KU-SELL-how-merchant-settlements-are-processed`, `KU-SELL-managing-merchant-transactions`, `KU-SELL-seller-management-overview-and-onboarding`, `KU-SELL-seller-marketplace-implementation-steps`.

<!-- op: spec=api-specs/Seller_management_-_Marketplace.yaml method=PATCH path=/v1/marketplaces/{marketplaceId}/creditors-operations/{creditorOperationId} operationId=PatchCreditorOperationByIdV1 -->
### `PATCH /v1/marketplaces/{marketplaceId}/creditors-operations/{creditorOperationId}` — Patch creditor operation

- **operationId:** `PatchCreditorOperationByIdV1`
- **Specification:** `api-specs/Seller_management_-_Marketplace.yaml` (Seller management - Marketplace)
- **Server base URL(s):** `https://sandbox.pismolabs.io/marketplace`
- **Tags:** `Marketplace creditor operations`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Update creditor operation fields using marketplace and creditor IDs.
>
> This endpoint generates a [Marketplace creditor operation updated](https://developers.pismo.io/events/docs/marketplace-marketplace-creditor-operation-updated-1) event.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `marketplaceId` | path | yes | integer | Marketplace ID | format: "int64"; example: 1 |
| `creditorOperationId` | path | yes | integer | Creditor operation ID | format: "int64"; example: 128427 |
| `Authorization` | header | no | string | Authorization token. This is a regular access token, which does not need to include an account ID. | example: "Bearer 1JI12J39182H39182JDIOAWJ%=" |

#### Request body

Required: yes

> Request body

**Content type `application/json`** — schema: object (schema `PatchCreditorOperation`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `creditor_id` | integer (schema `CreditorID`) | no | Creditor ID. This represents the owner of a business. | format: "int64"; example: 12345 |
| `first_installment_days_to_payment` | integer (schema `FirstInstallmentDaysToPayment`) | no | Number of days before first installment is due | format: "int32"; minimum: 1; example: 2 |
| `installments` | integer (schema `Installments`) | no | Number of installments | format: "int32"; minimum: 1; example: 3 |
| `n_installment_days_to_payment` | integer (schema `NthInstallmentDaysToPayment`) | no | Number of days before each subsequent installment is due.<br>The customer has `first_installment_days_to_payment` days to pay the first installment.<br>They have `n_installment_days_to_payment` days to pay each installment after that.<br> | format: "int32"; minimum: 1; example: 2 |
| `card_not_present_allowed` | boolean (schema `CardNotPresentAllowed`) | no | Indicates whether a card-not-present (CNP) transaction is allowed. A CNP transaction is a purchase made virtually, without processing a physical card via a card reader or terminal (and without manually entering a PIN). | default: false; example: true |
| `doc_number_allowed` | boolean (schema `DocNumberAllowed`) | no | Indicates whether document number is allowed. | default: false; example: true |
| `matched_mdr` | boolean (schema `MatchedMdr`) | no | Indicates whether this is a matched Merchant Discount Rate (MDR). If `false`, the fixed transaction fee and the MDR amount is applied only to the first installment. The default value is `false`.<br> | default: false; example: true |
| `matched_settlement` | boolean (schema `MatchedSettlement`) | no | Indicates whether this is a matched settlement. A matched settlement means the settlement is paid in several batches, whereas `false` indicates the full amount is paid in one single payment. The default value is `false`. | default: false; example: true |
| `mdr` | number (schema `Mdr`) | no | MDR fee. The Merchant Discount Rate (MDR) is the rate charged to a merchant for payment processing services on debit and credit card transactions.<br>The merchant must set up this service and agree to the rate before accepting debit and credit cards as payment.<br> | default: 0; format: "float"; example: 0.01 |
| `network` | string (schema `Network`) | no | Card network | example: "Visa" |
| `processing_code` | string (schema `ProcessingCode`) | no | A processing code is a custom alphanumeric identifier that defines the type of financial operation that the Pismo platform handles.<br><br>For more information, refer to [Processing codes](doc:processing-codes-and-transaction-types).<br> | example: "700203" |
| `start_date` | string (schema `StartDate`) | no | Date from which this operation is considered active. Format = yyyy-mm-dd. | format: "date"; example: "2022-12-21" |
| `transaction_fee` | number (schema `TransactionFee`) | no | Transaction fee | default: 0; example: 5 |
| `work_days` | boolean (schema `WorkDays`) | no | If `true`, only business days are used to calculate the date of the next payment.<br> | default: false; example: false |
| `fees` | array of object (schema `Fee`) (schema `Fees`) | no | Creditor operation additional fees | example: [{"name": "EMISSION_FEE", "value": 1.5}, {"name": "MAINTENANCE_FEE", "value": 0.01}] |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 204 | No Content |  |
| 400 | Bad Request |  |
| 401 | Access token is missing or invalid |  |
| 404 | The specified resource was not found |  |
| 500 | Internal server error |  |


#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `marketplace-marketplace-creditor-operation-updated-1` | https://developers.pismo.io/events/docs/marketplace-marketplace-creditor-operation-updated-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `204;400;401;404;500`, has examples `False`, emits events `1`, deprecated `False`.

<!-- op: spec=api-specs/Seller_management_-_Marketplace.yaml method=GET path=/marketplaces/{marketplaceId}/creditors-operations/{creditorOperationId} operationId=GetCreditorOperationById -->
### `GET /marketplaces/{marketplaceId}/creditors-operations/{creditorOperationId}` — Get creditor operation

- **operationId:** `GetCreditorOperationById`
- **Specification:** `api-specs/Seller_management_-_Marketplace.yaml` (Seller management - Marketplace)
- **Server base URL(s):** `https://sandbox.pismolabs.io/marketplace`
- **Tags:** `Marketplace creditor operations`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Get creditor operation information using marketplace and creditor IDs.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `marketplaceId` | path | yes | integer | Marketplace ID | format: "int64"; example: 1 |
| `creditorOperationId` | path | yes | integer | Creditor operation ID | format: "int64"; example: 128427 |
| `Authorization` | header | no | string | Authorization token. This is a regular access token, which does not need to include an account ID. | example: "Bearer 1JI12J39182H39182JDIOAWJ%=" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `GETCreditorsOperationsWithFeesResponse`) |
| 400 | Bad Request |  |
| 401 | Access token is missing or invalid |  |
| 500 | Internal server error |  |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `card_not_present_allowed` | boolean (schema `CardNotPresentAllowed`) | no | Indicates whether a card-not-present (CNP) transaction is allowed. A CNP transaction is a purchase made virtually, without processing a physical card via a card reader or terminal (and without manually entering a PIN). | default: false; example: true |
| `creditor_id` | integer (schema `CreditorID`) | no | Creditor ID. This represents the owner of a business. | format: "int64"; example: 12345 |
| `creditor_name` | string (schema `CreditorName`) | no | Creditor name | minLength: 1; maxLength: 100; example: "Joe's Bakery LTDA" |
| `doc_number_allowed` | boolean (schema `DocNumberAllowed`) | no | Indicates whether document number is allowed. | default: false; example: true |
| `fees` | array of object (schema `FeeModelsWithValues`) | no | Fee models for a marketplace |  |
| `fees[].name` | string | no | Fee model name | maxLength: 25; example: "F_CUSTOM" |
| `fees[].type` | string | no | Type of rate | enum: ["FIXED", "PERCENTAGE"]; maxLength: 25; example: "FIXED" |
| `fees[].value` | number | no | Value of the rate | format: "double"; example: 10.99 |
| `first_installment_days_to_payment` | integer (schema `FirstInstallmentDaysToPayment`) | no | Number of days before first installment is due | format: "int32"; minimum: 1; example: 2 |
| `id` | integer (schema `CreditorOperationID`) | no | Creditor operation ID | format: "int64"; example: 128427 |
| `installments` | integer (schema `Installments`) | no | Number of installments | format: "int32"; minimum: 1; example: 3 |
| `marketplace_creditors_operations_id` | number (schema `MarketplaceCreditorsOperationsID`) | no | Operations ID for marketplace creditors. This is the same as the `id` field. This field might be removed in the future. | example: 59532 |
| `matched_mdr` | boolean (schema `MatchedMdr`) | no | Indicates whether this is a matched Merchant Discount Rate (MDR). If `false`, the fixed transaction fee and the MDR amount is applied only to the first installment. The default value is `false`.<br> | default: false; example: true |
| `matched_settlement` | boolean (schema `MatchedSettlement`) | no | Indicates whether this is a matched settlement. A matched settlement means the settlement is paid in several batches, whereas `false` indicates the full amount is paid in one single payment. The default value is `false`. | default: false; example: true |
| `mdr` | number (schema `Mdr`) | no | MDR fee. The Merchant Discount Rate (MDR) is the rate charged to a merchant for payment processing services on debit and credit card transactions.<br>The merchant must set up this service and agree to the rate before accepting debit and credit cards as payment.<br> | default: 0; format: "float"; example: 0.01 |
| `n_installment_days_to_payment` | integer (schema `NthInstallmentDaysToPayment`) | no | Number of days before each subsequent installment is due.<br>The customer has `first_installment_days_to_payment` days to pay the first installment.<br>They have `n_installment_days_to_payment` days to pay each installment after that.<br> | format: "int32"; minimum: 1; example: 2 |
| `network` | string (schema `Network`) | no | Card network | example: "Visa" |
| `operation_type_description` | string (schema `OperationTypeDescription`) | no | Operation type description | minLength: 1; maxLength: 50; example: "In one lump sum" |
| `operation_type_id` | integer (schema `OperationTypeID`) | no | Operation type ID defined by the Pismo platform.<br><br>An operation type ID is an operation type processing code, which is a custom alphanumeric identifier that defines how the Pismo platform handles a certain financial operation type. See [Processing codes and transaction types](https://developers.pismo.io/pismo-docs/docs/processing-codes-and-transaction-types) for more information.<br><br><b>Note:</b> Either `operation_type_id` or `processing_code` is **required**. Using `processing_code` is recommended as `operation_type_id` is deprecated and scheduled for removal.<br> | format: "int64"; deprecated: true; example: 4 |
| `processing_code` | string (schema `ProcessingCode`) | no | A processing code is a custom alphanumeric identifier that defines the type of financial operation that the Pismo platform handles.<br><br>For more information, refer to [Processing codes](doc:processing-codes-and-transaction-types).<br> | example: "700203" |
| `start_date` | string (schema `StartDate`) | no | Date from which this operation is considered active. Format = yyyy-mm-dd. | format: "date"; example: "2022-12-21" |
| `transaction_fee` | number (schema `TransactionFee`) | no | Transaction fee | default: 0; example: 5 |
| `work_days` | boolean (schema `WorkDays`) | no | If `true`, only business days are used to calculate the date of the next payment.<br> | default: false; example: false |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;500`, has examples `False`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Seller_management_-_Marketplace.yaml method=PUT path=/marketplaces/{marketplaceId}/creditors-operations/{creditorOperationId} operationId=PutUpdateCreditorOperationById -->
### `PUT /marketplaces/{marketplaceId}/creditors-operations/{creditorOperationId}` — Update creditor operation

- **operationId:** `PutUpdateCreditorOperationById`
- **Specification:** `api-specs/Seller_management_-_Marketplace.yaml` (Seller management - Marketplace)
- **Server base URL(s):** `https://sandbox.pismolabs.io/marketplace`
- **Tags:** `Marketplace creditor operations`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Update creditor operation information using marketplace and creditor IDs.
>
> This endpoint generates a [Marketplace creditor operation updated](https://developers.pismo.io/events/docs/marketplace-marketplace-creditor-operation-updated-1) event.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `creditorOperationId` | path | yes | integer | Creditor operation ID | format: "int64"; example: 128427 |
| `marketplaceId` | path | yes | integer | Marketplace ID | format: "int64"; example: 1 |
| `Authorization` | header | no | string | Authorization token. This is a regular access token, which does not need to include an account ID. | example: "Bearer 1JI12J39182H39182JDIOAWJ%=" |
| `Content-Type` | header | no | string | Content type | example: "application/json" |

#### Request body

Required: yes

> Request body

**Content type `application/json`** — schema: object (schema `PostCreditorOperation`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `creditor_id` | integer (schema `CreditorID`) | yes | Creditor ID. This represents the owner of a business. | format: "int64"; example: 12345 |
| `first_installment_days_to_payment` | integer (schema `FirstInstallmentDaysToPayment`) | yes | Number of days before first installment is due | format: "int32"; minimum: 1; example: 2 |
| `installments` | integer (schema `Installments`) | yes | Number of installments | format: "int32"; minimum: 1; example: 3 |
| `n_installment_days_to_payment` | integer (schema `NthInstallmentDaysToPayment`) | yes | Number of days before each subsequent installment is due.<br>The customer has `first_installment_days_to_payment` days to pay the first installment.<br>They have `n_installment_days_to_payment` days to pay each installment after that.<br> | format: "int32"; minimum: 1; example: 2 |
| `card_not_present_allowed` | boolean (schema `CardNotPresentAllowed`) | no | Indicates whether a card-not-present (CNP) transaction is allowed. A CNP transaction is a purchase made virtually, without processing a physical card via a card reader or terminal (and without manually entering a PIN). | default: false; example: true |
| `doc_number_allowed` | boolean (schema `DocNumberAllowed`) | no | Indicates whether document number is allowed. | default: false; example: true |
| `matched_mdr` | boolean (schema `MatchedMdr`) | no | Indicates whether this is a matched Merchant Discount Rate (MDR). If `false`, the fixed transaction fee and the MDR amount is applied only to the first installment. The default value is `false`.<br> | default: false; example: true |
| `matched_settlement` | boolean (schema `MatchedSettlement`) | no | Indicates whether this is a matched settlement. A matched settlement means the settlement is paid in several batches, whereas `false` indicates the full amount is paid in one single payment. The default value is `false`. | default: false; example: true |
| `mdr` | number (schema `Mdr`) | no | MDR fee. The Merchant Discount Rate (MDR) is the rate charged to a merchant for payment processing services on debit and credit card transactions.<br>The merchant must set up this service and agree to the rate before accepting debit and credit cards as payment.<br> | default: 0; format: "float"; example: 0.01 |
| `network` | string (schema `Network`) | no | Card network | example: "Visa" |
| `operation_type_id` | integer (schema `OperationTypeID`) | no | Operation type ID defined by the Pismo platform.<br><br>An operation type ID is an operation type processing code, which is a custom alphanumeric identifier that defines how the Pismo platform handles a certain financial operation type. See [Processing codes and transaction types](https://developers.pismo.io/pismo-docs/docs/processing-codes-and-transaction-types) for more information.<br><br><b>Note:</b> Either `operation_type_id` or `processing_code` is **required**. Using `processing_code` is recommended as `operation_type_id` is deprecated and scheduled for removal.<br> | format: "int64"; deprecated: true; example: 4 |
| `processing_code` | string (schema `ProcessingCode`) | no | A processing code is a custom alphanumeric identifier that defines the type of financial operation that the Pismo platform handles.<br><br>For more information, refer to [Processing codes](doc:processing-codes-and-transaction-types).<br> | example: "700203" |
| `start_date` | string (schema `StartDate`) | no | Date from which this operation is considered active. Format = yyyy-mm-dd. | format: "date"; example: "2022-12-21" |
| `transaction_fee` | number (schema `TransactionFee`) | no | Transaction fee | default: 0; example: 5 |
| `work_days` | boolean (schema `WorkDays`) | no | If `true`, only business days are used to calculate the date of the next payment.<br> | default: false; example: false |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object |
| 400 | Bad Request |  |
| 401 | Access token is missing or invalid |  |
| 500 | Internal server error |  |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `success` | boolean | no | Indicates if the update was successful. | example: true |


#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `marketplace-marketplace-creditor-operation-updated-1` | https://developers.pismo.io/events/docs/marketplace-marketplace-creditor-operation-updated-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;500`, has examples `True`, emits events `1`, deprecated `False`.

Guides that link to this operation: `KU-EVT-marketplace-data-events`.

<!-- op: spec=api-specs/Seller_management_-_Marketplace.yaml method=DELETE path=/marketplaces/{marketplaceId}/creditors-operations/{creditorOperationId} operationId=DeleteCreditorOperationById -->
### `DELETE /marketplaces/{marketplaceId}/creditors-operations/{creditorOperationId}` — Delete creditor operation

- **operationId:** `DeleteCreditorOperationById`
- **Specification:** `api-specs/Seller_management_-_Marketplace.yaml` (Seller management - Marketplace)
- **Server base URL(s):** `https://sandbox.pismolabs.io/marketplace`
- **Tags:** `Marketplace creditor operations`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Delete creditor operation by ID.
>
> This endpoint generates a [Marketplace creditor operation deleted](https://developers.pismo.io/events/docs/marketplace-marketplace-creditor-operation-deleted-1) event.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `creditorOperationId` | path | yes | integer | Creditor operation ID | format: "int64"; example: 128427 |
| `marketplaceId` | path | yes | integer | Marketplace ID | format: "int64"; example: 1 |
| `Authorization` | header | no | string | Authorization token. This is a regular access token, which does not need to include an account ID. | example: "Bearer 1JI12J39182H39182JDIOAWJ%=" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK |  |
| 400 | Bad Request |  |
| 401 | Access token is missing or invalid |  |
| 404 | The specified resource was not found |  |
| 500 | Internal server error |  |


#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `marketplace-marketplace-creditor-operation-deleted-1` | https://developers.pismo.io/events/docs/marketplace-marketplace-creditor-operation-deleted-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;404;500`, has examples `False`, emits events `1`, deprecated `False`.

Guides that link to this operation: `KU-EVT-marketplace-data-events`.

<!-- op: spec=api-specs/Seller_management_-_Marketplace.yaml method=GET path=/marketplaces/{marketplaceId}/merchants/{merchantId}/creditors-operations operationId=GetCreditorOperationsByMerchantIDAndMarketplaceID -->
### `GET /marketplaces/{marketplaceId}/merchants/{merchantId}/creditors-operations` — List creditor operations for marketplace and merchant

- **operationId:** `GetCreditorOperationsByMerchantIDAndMarketplaceID`
- **Specification:** `api-specs/Seller_management_-_Marketplace.yaml` (Seller management - Marketplace)
- **Server base URL(s):** `https://sandbox.pismolabs.io/marketplace`
- **Tags:** `Marketplace creditor operations`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> List creditor operations using marketplace and merchant IDs.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `marketplaceId` | path | yes | integer | Marketplace ID | format: "int64"; example: 1 |
| `merchantId` | path | yes | number | Merchant ID | example: 1 |
| `Authorization` | header | no | string | Authorization token. This is a regular access token, which does not need to include an account ID. | example: "Bearer 1JI12J39182H39182JDIOAWJ%=" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: array of object (schema `GETCreditorsOperationsResponse`) |
| 400 | Bad Request |  |
| 401 | Access token is missing or invalid |  |
| 500 | Internal server error |  |

##### Response 200

**200 `application/json` body fields:**

_No fields declared in the schema._


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;500`, has examples `False`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-SELL-managing-merchant-transactions`.

<!-- op: spec=api-specs/Seller_management_-_Marketplace.yaml method=GET path=/marketplaces/v1/{marketplaceId}/merchants-creditors operationId=GetMerchantsCreditorsV1 -->
### `GET /marketplaces/v1/{marketplaceId}/merchants-creditors` — List merchant creditors

- **operationId:** `GetMerchantsCreditorsV1`
- **Specification:** `api-specs/Seller_management_-_Marketplace.yaml` (Seller management - Marketplace)
- **Server base URL(s):** `https://sandbox.pismolabs.io/marketplace`
- **Tags:** `Marketplace creditor operations`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> List creditors for the merchants in a marketplace.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `marketplaceId` | path | yes | integer | Marketplace ID | format: "int64"; example: 1 |
| `search` | query | no | string | Search by creditor's name | example: "Acme, Inc." |
| `Authorization` | header | no | string | Authorization token. This is a regular access token, which does not need to include an account ID. | example: "Bearer 1JI12J39182H39182JDIOAWJ%=" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `GETMerchantCreditorsResponse`) |
| 400 | Bad Request |  |
| 401 | Access token is missing or invalid |  |
| 500 | Internal server error |  |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `items` | array of object | no | List of creditors |  |
| `items[].id` | integer (schema `CreditorID`) | no | Creditor ID. This represents the owner of a business. | format: "int64"; example: 12345 |
| `items[].name` | string (schema `CreditorName`) | no | Creditor name | minLength: 1; maxLength: 100; example: "Joe's Bakery LTDA" |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;500`, has examples `False`, emits events `0`, deprecated `False`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/GETCreditorsOperationsWithFeesResponse -->
### Schema `GETCreditorsOperationsWithFeesResponse`

Pointer: `#/components/schemas/GETCreditorsOperationsWithFeesResponse`. Type: object (schema `GETCreditorsOperationsWithFeesResponse`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `card_not_present_allowed` | boolean (schema `CardNotPresentAllowed`) | no | Indicates whether a card-not-present (CNP) transaction is allowed. A CNP transaction is a purchase made virtually, without processing a physical card via a card reader or terminal (and without manually entering a PIN). | default: false; example: true |
| `creditor_id` | integer (schema `CreditorID`) | no | Creditor ID. This represents the owner of a business. | format: "int64"; example: 12345 |
| `creditor_name` | string (schema `CreditorName`) | no | Creditor name | minLength: 1; maxLength: 100; example: "Joe's Bakery LTDA" |
| `doc_number_allowed` | boolean (schema `DocNumberAllowed`) | no | Indicates whether document number is allowed. | default: false; example: true |
| `fees` | array of object (schema `FeeModelsWithValues`) | no | Fee models for a marketplace |  |
| `fees[].name` | string | no | Fee model name | maxLength: 25; example: "F_CUSTOM" |
| `fees[].type` | string | no | Type of rate | enum: ["FIXED", "PERCENTAGE"]; maxLength: 25; example: "FIXED" |
| `fees[].value` | number | no | Value of the rate | format: "double"; example: 10.99 |
| `first_installment_days_to_payment` | integer (schema `FirstInstallmentDaysToPayment`) | no | Number of days before first installment is due | format: "int32"; minimum: 1; example: 2 |
| `id` | integer (schema `CreditorOperationID`) | no | Creditor operation ID | format: "int64"; example: 128427 |
| `installments` | integer (schema `Installments`) | no | Number of installments | format: "int32"; minimum: 1; example: 3 |
| `marketplace_creditors_operations_id` | number (schema `MarketplaceCreditorsOperationsID`) | no | Operations ID for marketplace creditors. This is the same as the `id` field. This field might be removed in the future. | example: 59532 |
| `matched_mdr` | boolean (schema `MatchedMdr`) | no | Indicates whether this is a matched Merchant Discount Rate (MDR). If `false`, the fixed transaction fee and the MDR amount is applied only to the first installment. The default value is `false`.<br> | default: false; example: true |
| `matched_settlement` | boolean (schema `MatchedSettlement`) | no | Indicates whether this is a matched settlement. A matched settlement means the settlement is paid in several batches, whereas `false` indicates the full amount is paid in one single payment. The default value is `false`. | default: false; example: true |
| `mdr` | number (schema `Mdr`) | no | MDR fee. The Merchant Discount Rate (MDR) is the rate charged to a merchant for payment processing services on debit and credit card transactions.<br>The merchant must set up this service and agree to the rate before accepting debit and credit cards as payment.<br> | default: 0; format: "float"; example: 0.01 |
| `n_installment_days_to_payment` | integer (schema `NthInstallmentDaysToPayment`) | no | Number of days before each subsequent installment is due.<br>The customer has `first_installment_days_to_payment` days to pay the first installment.<br>They have `n_installment_days_to_payment` days to pay each installment after that.<br> | format: "int32"; minimum: 1; example: 2 |
| `network` | string (schema `Network`) | no | Card network | example: "Visa" |
| `operation_type_description` | string (schema `OperationTypeDescription`) | no | Operation type description | minLength: 1; maxLength: 50; example: "In one lump sum" |
| `operation_type_id` | integer (schema `OperationTypeID`) | no | Operation type ID defined by the Pismo platform.<br><br>An operation type ID is an operation type processing code, which is a custom alphanumeric identifier that defines how the Pismo platform handles a certain financial operation type. See [Processing codes and transaction types](https://developers.pismo.io/pismo-docs/docs/processing-codes-and-transaction-types) for more information.<br><br><b>Note:</b> Either `operation_type_id` or `processing_code` is **required**. Using `processing_code` is recommended as `operation_type_id` is deprecated and scheduled for removal.<br> | format: "int64"; deprecated: true; example: 4 |
| `processing_code` | string (schema `ProcessingCode`) | no | A processing code is a custom alphanumeric identifier that defines the type of financial operation that the Pismo platform handles.<br><br>For more information, refer to [Processing codes](doc:processing-codes-and-transaction-types).<br> | example: "700203" |
| `start_date` | string (schema `StartDate`) | no | Date from which this operation is considered active. Format = yyyy-mm-dd. | format: "date"; example: "2022-12-21" |
| `transaction_fee` | number (schema `TransactionFee`) | no | Transaction fee | default: 0; example: 5 |
| `work_days` | boolean (schema `WorkDays`) | no | If `true`, only business days are used to calculate the date of the next payment.<br> | default: false; example: false |

<!-- schema: #/components/schemas/Fee -->
### Schema `Fee`

Pointer: `#/components/schemas/Fee`. Type: object (schema `Fee`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `name` | string | yes | Fee model name | maxLength: 25; example: "MAINTENANCE_FEE" |
| `value` | number | yes | Fee value; Dependent on the fee model. Usually a percentage (for example, `0.05` for 5%) or fixed amount (for example, `1.5` for a fixed fee of 1.5 currency units). | format: "float"; example: 0.01 |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Seller_management_-_Marketplace.yaml` | tag `Marketplace creditor operations`: GET /v2/marketplaces/{marketplaceId}/creditors-operations, PUT /v2/marketplaces/{marketplaceId}/creditors-operations, POST /v2/marketplaces/{marketplaceId}/creditors-operations, POST /marketplaces/{marketplaceId}/creditors-operations, PATCH /v1/marketplaces/{marketplaceId}/creditors-operations/{creditorOperationId}, GET /marketplaces/{marketplaceId}/creditors-operations/{creditorOperationId}, PUT /marketplaces/{marketplaceId}/creditors-operations/{creditorOperationId}, DELETE /marketplaces/{marketplaceId}/creditors-operations/{creditorOperationId}, GET /marketplaces/{marketplaceId}/merchants/{merchantId}/creditors-operations, GET /marketplaces/v1/{marketplaceId}/merchants-creditors | https://github.com/PismoDevEx/pismo-api-specs | `8ffe617b35e772cc…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-EVT-catalogue-marketplace` — Event catalogue: marketplace
- `KU-EVT-marketplace-data-events` — Seller management - Marketplace
- `KU-SELL-get-started-seller-management` — Get started with seller management
- `KU-SELL-how-merchant-settlements-are-processed` — How merchant settlements and installments are processed
- `KU-SELL-managing-merchant-transactions` — Managing merchant transactions
- `KU-SELL-seller-management-overview-and-onboarding` — Seller management overview and onboarding
- `KU-SELL-seller-marketplace-implementation-steps` — Seller marketplace implementation steps 1 to 6
