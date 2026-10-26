---
ku_id: KU-API-instant-payments-automatic-pix--automatic-pix
title: 'API reference: Instant payments - Automatic Pix — Automatic Pix'
category: api_reference
ku_type: api_reference
lifecycle: current
sources:
- path: api-specs/Instant_payments_-_Automatic_Pix.yaml
  sha256: df884687741cd08944c1b632cd27cb8de615af58e4fc890e04d6b2b8ee35fbe2
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
- post-recurrence-automatic
- update-recurrence-automatic
- cancel-recurrence-automatic
- accept-reject-authorization
- update-order-automatic-pix
- cancel-automatic-pix-payment-order
- resend-automatic-pix-payment-order
related_kus:
- KU-PAY-pix-automatic
specification_version: '1.0'
---

# API reference: Instant payments - Automatic Pix — Automatic Pix

**KU ID:** `KU-API-instant-payments-automatic-pix--automatic-pix` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 7 operation(s) tagged `Automatic Pix` in `api-specs/Instant_payments_-_Automatic_Pix.yaml` (“Instant payments - Automatic Pix”, version `1.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Automatic Pix endpoints.

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `POST /inst-pull-pay/v1/pix/automatic` | `post-recurrence-automatic` | Create recurrence | no |
| `PATCH /inst-pull-pay/v1/pix/automatic/{recurrence_id}` | `update-recurrence-automatic` | Update automatic recurrence | no |
| `POST /inst-pull-pay/v1/pix/automatic/cancel` | `cancel-recurrence-automatic` | Cancel recurrence | no |
| `POST /inst-pull-pay/v1/pix/automatic/payer/authorization` | `accept-reject-authorization` | Accept/reject recurrence authorization | no |
| `PATCH /inst-pull-pay/v1/pix/automatic/payment/order/{end_to_end_id}` | `update-order-automatic-pix` | Update payment order amount | no |
| `POST /inst-pull-pay/v1/pix/automatic/payment/order/cancel` | `cancel-automatic-pix-payment-order` | Cancel payment order | no |
| `POST /inst-pull-pay/v1/pix/automatic/payment/order/{end_to_end_id}/resend` | `resend-automatic-pix-payment-order` | Resend payment order | no |

## Operation contracts

<!-- op: spec=api-specs/Instant_payments_-_Automatic_Pix.yaml method=POST path=/inst-pull-pay/v1/pix/automatic operationId=post-recurrence-automatic -->
### `POST /inst-pull-pay/v1/pix/automatic` — Create recurrence

- **operationId:** `post-recurrence-automatic`
- **Specification:** `api-specs/Instant_payments_-_Automatic_Pix.yaml` (Instant payments - Automatic Pix)
- **Server base URL(s):** `https://sandbox-cdn.pismolabs.io`, `https://sandbox-cdn.pismolabs.io/inst-pull-pay`
- **Tags:** `Automatic Pix`
- **Deprecated in specification:** no
- **Security requirement:** not declared

**Description (from the specification):**

> Initiate a payment request to create a Pix Automatic recurrence payment authorization. 
>
> The Central Bank of Brazil (BACEN) created Pix Automatic - a feature that allows for scheduled and automatic recurring transfers.  
>
> BACEN rules state that a recurrence must support retry attempts to allow execution of additional charges in case the original payment is not completed.
>
> **Retries flow** 
>
> * If the payment order is not paid by 22:00 on the due date, and the recurrence allows retries, Pismo automatically generates a new payment order for that unpaid cycle.
>
> * The new payment order is created with type = `RETRY_OVERDUE`, and its due date is set to D+2, in compliance with Central Bank requirements. Retries can occur up to 3 times, within a maximum period of 7 days after the original due date.
>
> * After these 3 retry attempts, the payment order cycle can no longer be processed via the automatic Pix flow. The payee must manage further collection outside of this flow.
>
> For more information, refer to [Pix Automatic](https://developers.pismo.io/pismo-docs/docs/pix-automatic) 

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `x-account` | header | yes | integer | Pismo account ID. | example: 0 |
| `Idempotency-Key` | header | yes | string | A unique ID to ensure the operation remains idempotent, allowing for operation repitition without causing unintended effects or duplication. An idempotent operation is one that can be applied multiple times, yet the outcome remains the same. it ensures that network errors, retries, or failures can occur without introducing inconsistencies.<br> |  |
| `x-tenant` | header | no | string | Organization ID<br> |  |

#### Request body

Required: yes

**Content type `application/json`** — schema: object (schema `RecurrenceRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `contract_id` | string (schema `ContractID`) | yes | Payee-created external ID for their reference.<br> | maxLength: 35; example: "5509-uroo-78944-9987" |
| `description` | string (schema `RecurrenceDescription`) | yes | Recurrence payment description | maxLength: 35; example: "Gym membership" |
| `frequency_type` | string (schema `FrequencyType`) | yes | Recurrence payment type | enum: ["WEEK", "MONTH", "QUARTER", "SEMESTER", "YEAR"]; example: "MONTH" |
| `allow_attempts_after_expiration` | boolean (schema `AllowAttemptsAfterExpiration`) | yes | Will charge continue after due date?<br><br>If `true` the recurence will receive a `recurrence_id` starting with `RR`. Otherwise, it will start with `RN`.<br> |  |
| `first_payment_date` | string (schema `FirstPaymentDateCreateRecRequest`) | yes | First charge/payment date, must be more than 2 days ahead the recurrence creation date. Format = yyyy-mm-dd | format: "datetime"; example: "2025-04-25" |
| `debtor` | object (schema `Debtor`) | yes |  |  |
| `payer` | object (schema `Payer`) | yes |  |  |
| `dynamic_amount` | boolean (schema `DynamicAmount`) | no | Does recurrence have a dynamic amount? <br><br>If `true`, `min_payment_amount` is **REQUIRED**. <br><br>If `false`, `amount` is **REQUIRED**. Default is `false`.<br> | default: false; example: false |
| `amount` | number (schema `Amount`) | no | Amount to be transferred. | example: 1050.44 |
| `min_payment_amount` | number (schema `MinPaymentAmount`) | no | Payee-defined minimum payment amount for dynamic amount recurrences. | example: 10.09 |
| `last_payment_date` | string (schema `LastPaymentDate`) | no | Last charge/payment date. Format = yyyy-mm-dd | format: "datetime"; example: "2026-06-10" |
| `expiration_date` | string (schema `ExpirationDateCreateRecRequest`) | no | Authorization expiration date, must be at least 2 days before the `first_payment_date`. <br><br>RFC 3339 value. Format = YYYY-MM-DDThh:mm:ss.SSSZ<br><br>If not passed,  the `expiration_date` is automatically generated, up to 2 days before the `first_payment_date`, or a maximum of 30 days from the current date, whichever is due first<br> | format: "datetime"; example: "2020-08-13T13:49:03.000Z" |
| `taxes` | object (schema `TaxesWithOutCategory`) | no | Only available in EXT environment for direct parciapants. Tax information related to the transaction.<br> |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `RecurrenceResponse`) |
| 400 | Bad request | `application/json`: object (schema `customer.Error`) |
| 401 | Unauthorized. Missing or invalid authentication token. | `application/json`: object (schema `customer.Error`) |
| 404 | Not found | `application/json`: object (schema `customer.Error`) |
| 500 | Internal Server Error | `application/json`: object (schema `customer.Error`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `recurrence_id` | string (schema `RecurrenceID`) | no | BACEN recurrence ID | example: "RN000000012025050500012345678" |
| `journey_type` | string (schema `JourneyType`) | no | Recurrence payment type: <br><br> `AUT1` - Bank notification. If the merchant has the payer's banking information, a push notification can be sent directly to the payer's bank app, prompting them to authorize the recurring payment.<br> <br> `AUT2` - Authorization via QR code. Payer scans a merchant provided QR code to authorize recurring payments. This method does not initiate an immediate payment, allowing the first payment to be scheduled for a later date.<br> <br> `AUT3` - Authorization via QR code with first payment.  Similar to the second method, but the QR code includes information for both the authorization and the initial payment, enabling the payer to authorize the recurring payment and make the first payment in a single step.<br> <br> `AUT4` - Post-payment sign-up path. After completing a one-time payment via QR code, the payer is offered the option to authorize recurring payments for future transactions<br> | enum: ["AUT1", "AUT2", "AUT3", "AUT4"]; example: "AUT1" |
| `contract_id` | string (schema `ContractID`) | no | Payee-created external ID for their reference.<br> | maxLength: 35; example: "5509-uroo-78944-9987" |
| `description` | string (schema `RecurrenceDescription`) | no | Recurrence payment description | maxLength: 35; example: "Gym membership" |
| `amount` | number (schema `Amount`) | no | Amount to be transferred. | example: 1050.44 |
| `min_payment_amount` | number (schema `MinPaymentAmount`) | no | Payee-defined minimum payment amount for dynamic amount recurrences. | example: 10.09 |
| `max_payment_amount` | number (schema `MaxPaymentAmount`) | no | Payer-defined maximum payment amount for dynamic amount recurrences. | example: 86753.09 |
| `dynamic_amount` | boolean (schema `DynamicAmount`) | no | Does recurrence have a dynamic amount? <br><br>If `true`, `min_payment_amount` is **REQUIRED**. <br><br>If `false`, `amount` is **REQUIRED**. Default is `false`.<br> | default: false; example: false |
| `frequency_type` | string (schema `FrequencyType`) | no | Recurrence payment type | enum: ["WEEK", "MONTH", "QUARTER", "SEMESTER", "YEAR"]; example: "MONTH" |
| `allow_attempts_after_expiration` | boolean (schema `AllowAttemptsAfterExpiration`) | no | Will charge continue after due date?<br><br>If `true` the recurence will receive a `recurrence_id` starting with `RR`. Otherwise, it will start with `RN`.<br> |  |
| `is_working_days` | boolean (schema `IsWorkingDays`) | no | If the recurrence will only execute on working days | example: false |
| `expiration_date` | string (schema `ExpirationDate`) | no | Authorization expiration date. RFC 3339 value. Format = YYYY-MM-DDThh:mm:ss.SSSZ | format: "datetime"; example: "2020-08-13T13:49:03.000Z" |
| `first_payment_date` | string (schema `FirstPaymentDate`) | no | First charge/payment date. Format = yyyy-mm-dd | format: "datetime"; example: "2025-04-25" |
| `last_payment_date` | string (schema `LastPaymentDate`) | no | Last charge/payment date. Format = yyyy-mm-dd | format: "datetime"; example: "2026-06-10" |
| `payee` | object (schema `Payee`) | no |  |  |
| `payer` | object (schema `Payer`) | no |  |  |
| `debtor` | object (schema `Debtor`) | no |  |  |
| `status` | string (schema `RecurrenceStatus`) | no | Recurrence status | enum: ["CREATED", "ACCEPTED", "APPROVED", "REJECTED", "FINISHED", "EXPIRED", "CANCELLED"]; example: "CREATED" |
| `reason_code` | string (schema `BacenReasonCode`) | no | Cancellation reason code:   <br><br>* `ACCL` - Paying receiving user's account cancelled<br>* `CPCL` - Receiving company closure<br>* `DCSD` - Paying user death <br>* `ERSL` - Receiving user, or their participant, request cancelled due to confirmation request error<br>* `FRUD` - Fraud<br>* `PCFD` - Receiving user participant request because the same recurrence was confirmed another way, for example, via QR code<br>* `SLCR` - Receiving user request<br>* `SLDB` - Paying user request<br>* `OTHS` - Requested by either the payer's participant or the receiver's participant for other reasons not specified in the previous categories<br>* `NRES` - Receiving PSP request due to lack of response to pain.009 within the regulatory period<br> | enum: ["ACCL", "CPCL", "DCSD", "ERSL", "FRUD", "PCFD", "SLCR", "SLDB", "OTHS", "NRES"]; example: "ACCL" |
| `transaction_identification` | string (schema `RecurrencTransactionIdentification`) | no | Recurrence transaction ID. <br> | example: "1a84daf6-a61b-4aba-919a-a9943db7102e" |
| `authorizations` | array of object (schema `AuthorizationResponse`) | no |  |  |
| `created_at` | string (schema `CreatedAt`) | no | Created at datetime. RFC 3339 format <br> | format: "datetime"; example: "2025-11-14T17:54:40Z" |
| `updated_at` | string (schema `UpdatedAt`) | no | Scheduled item last updated time, RFC 3339 format | example: "2024-11-14T17:54:40Z" |
| `taxes` | object (schema `TaxesWithCategory`) | no | Now only available on ext env and just for direct participants. Tax information related to the transaction. |  |

##### Response 400

- Response header `x-cid`: Request tracking ID. (string)
##### Response 404

- Response header `x-cid`: Request tracking ID. (string)
##### Response 500

- Response header `x-cid`: Request tracking ID. (string)

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;404;500`, has examples `False`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-PAY-pix-automatic`.

<!-- op: spec=api-specs/Instant_payments_-_Automatic_Pix.yaml method=PATCH path=/inst-pull-pay/v1/pix/automatic/{recurrence_id} operationId=update-recurrence-automatic -->
### `PATCH /inst-pull-pay/v1/pix/automatic/{recurrence_id}` — Update automatic recurrence

- **operationId:** `update-recurrence-automatic`
- **Specification:** `api-specs/Instant_payments_-_Automatic_Pix.yaml` (Instant payments - Automatic Pix)
- **Server base URL(s):** `https://sandbox-cdn.pismolabs.io`, `https://sandbox-cdn.pismolabs.io/inst-pull-pay`
- **Tags:** `Automatic Pix`
- **Deprecated in specification:** no
- **Security requirement:** not declared

**Description (from the specification):**

> Update automatic recurrence.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Account token - an access token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a <b>401 Unauthorized</b> message. | example: "Bearer eyJhbGci...IUzUx" |
| `x-account` | header | yes | integer | Pismo account ID. | example: 0 |
| `recurrence_id` | path | yes | string | BACEN (Brazil Central Bank) recurrence ID |  |

#### Request body

Required: yes

**Content type `application/json`** — schema: object (schema `PatchRecurrenceRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `max_payment_amount` | number (schema `MaxPaymentAmount`) | no | Payer-defined maximum payment amount for dynamic amount recurrences. | example: 86753.09 |
| `taxes` | object (schema `TaxesWithCategory`) | no | Now only available on ext env and just for direct participants. Tax information related to the transaction. |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 204 | No Content |  |
| 400 | Bad request | `application/json`: object (schema `customer.Error`) |
| 401 | Unauthorized. Missing or invalid authentication token. | `application/json`: object (schema `customer.Error`) |
| 404 | Not found | `application/json`: object (schema `customer.Error`) |
| 500 | Internal Server Error | `application/json`: object (schema `customer.Error`) |

##### Response 400

- Response header `x-cid`: Request tracking ID. (string)
##### Response 404

- Response header `x-cid`: Request tracking ID. (string)
##### Response 500

- Response header `x-cid`: Request tracking ID. (string)

Catalogue row (api-reference-data/operations_catalog.csv): response codes `204;400;401;404;500`, has examples `False`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-PAY-pix-automatic`.

<!-- op: spec=api-specs/Instant_payments_-_Automatic_Pix.yaml method=POST path=/inst-pull-pay/v1/pix/automatic/cancel operationId=cancel-recurrence-automatic -->
### `POST /inst-pull-pay/v1/pix/automatic/cancel` — Cancel recurrence

- **operationId:** `cancel-recurrence-automatic`
- **Specification:** `api-specs/Instant_payments_-_Automatic_Pix.yaml` (Instant payments - Automatic Pix)
- **Server base URL(s):** `https://sandbox-cdn.pismolabs.io`, `https://sandbox-cdn.pismolabs.io/inst-pull-pay`
- **Tags:** `Automatic Pix`
- **Deprecated in specification:** no
- **Security requirement:** not declared

**Description (from the specification):**

> Cancel Pix Automatic recurrence

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Account token - an access token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a <b>401 Unauthorized</b> message. | example: "Bearer eyJhbGci...IUzUx" |
| `Idempotency-Key` | header | yes | string | A unique ID to ensure the operation remains idempotent, allowing for operation repitition without causing unintended effects or duplication. An idempotent operation is one that can be applied multiple times, yet the outcome remains the same. it ensures that network errors, retries, or failures can occur without introducing inconsistencies.<br> |  |

#### Request body

Required: yes

**Content type `application/json`** — schema: object (schema `CancelRecurrenceRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `recurrence_id` | string (schema `RecurrenceID`) | yes | BACEN recurrence ID | example: "RN000000012025050500012345678" |
| `reason_code` | string (schema `BacenReasonCode`) | yes | Cancellation reason code:   <br><br>* `ACCL` - Paying receiving user's account cancelled<br>* `CPCL` - Receiving company closure<br>* `DCSD` - Paying user death <br>* `ERSL` - Receiving user, or their participant, request cancelled due to confirmation request error<br>* `FRUD` - Fraud<br>* `PCFD` - Receiving user participant request because the same recurrence was confirmed another way, for example, via QR code<br>* `SLCR` - Receiving user request<br>* `SLDB` - Paying user request<br>* `OTHS` - Requested by either the payer's participant or the receiver's participant for other reasons not specified in the previous categories<br>* `NRES` - Receiving PSP request due to lack of response to pain.009 within the regulatory period<br> | enum: ["ACCL", "CPCL", "DCSD", "ERSL", "FRUD", "PCFD", "SLCR", "SLDB", "OTHS", "NRES"]; example: "ACCL" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `CancelRecurrenceResponse`) |
| 400 | Bad request | `application/json`: object (schema `customer.Error`) |
| 401 | Unauthorized. Missing or invalid authentication token. | `application/json`: object (schema `customer.Error`) |
| 404 | Not found | `application/json`: object (schema `customer.Error`) |
| 500 | Internal Server Error | `application/json`: object (schema `customer.Error`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `recurrence_id` | string (schema `RecurrenceID`) | no | BACEN recurrence ID | example: "RN000000012025050500012345678" |
| `reason_code` | string (schema `BacenReasonCode`) | no | Cancellation reason code:   <br><br>* `ACCL` - Paying receiving user's account cancelled<br>* `CPCL` - Receiving company closure<br>* `DCSD` - Paying user death <br>* `ERSL` - Receiving user, or their participant, request cancelled due to confirmation request error<br>* `FRUD` - Fraud<br>* `PCFD` - Receiving user participant request because the same recurrence was confirmed another way, for example, via QR code<br>* `SLCR` - Receiving user request<br>* `SLDB` - Paying user request<br>* `OTHS` - Requested by either the payer's participant or the receiver's participant for other reasons not specified in the previous categories<br>* `NRES` - Receiving PSP request due to lack of response to pain.009 within the regulatory period<br> | enum: ["ACCL", "CPCL", "DCSD", "ERSL", "FRUD", "PCFD", "SLCR", "SLDB", "OTHS", "NRES"]; example: "ACCL" |
| `cancelled_at` | string (schema `CancellatedAt`) | no | Cancellation date time, RFC 3339 format: YYYY-MM-DDThh:mm:ssZ. | example: "2024-11-14T17:54:40Z" |

##### Response 400

- Response header `x-cid`: Request tracking ID. (string)
##### Response 404

- Response header `x-cid`: Request tracking ID. (string)
##### Response 500

- Response header `x-cid`: Request tracking ID. (string)

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;404;500`, has examples `False`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-PAY-pix-automatic`.

<!-- op: spec=api-specs/Instant_payments_-_Automatic_Pix.yaml method=POST path=/inst-pull-pay/v1/pix/automatic/payer/authorization operationId=accept-reject-authorization -->
### `POST /inst-pull-pay/v1/pix/automatic/payer/authorization` — Accept/reject recurrence authorization

- **operationId:** `accept-reject-authorization`
- **Specification:** `api-specs/Instant_payments_-_Automatic_Pix.yaml` (Instant payments - Automatic Pix)
- **Server base URL(s):** `https://sandbox-cdn.pismolabs.io`, `https://sandbox-cdn.pismolabs.io/inst-pull-pay`
- **Tags:** `Automatic Pix`
- **Deprecated in specification:** no
- **Security requirement:** not declared

**Description (from the specification):**

> Pix Automatic payee recurrence payment authorization acceptance or rejection

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Account token - an access token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a <b>401 Unauthorized</b> message. | example: "Bearer eyJhbGci...IUzUx" |
| `Idempotency-Key` | header | yes | string | A unique ID to ensure the operation remains idempotent, allowing for operation repitition without causing unintended effects or duplication. An idempotent operation is one that can be applied multiple times, yet the outcome remains the same. it ensures that network errors, retries, or failures can occur without introducing inconsistencies.<br> |  |

#### Request body

Required: yes

**Content type `application/json`** — schema: object (schema `AuthorizationRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `recurrence_id` | string (schema `RecurrenceID`) | yes | BACEN recurrence ID | example: "RN000000012025050500012345678" |
| `status` | string (schema `ApproveAuthorizationStatus`) | yes | Authorization status | enum: ["ACCEPTED", "REJECTED"]; example: "REJECTED" |
| `reason` | string (schema `AuthorizationRejectedReasonCodeRequest`) | no | Rejected authorizations reason code. Mandatory when `status` is `REJECTED`. <br>* `AP13` - Paying user rejects recurrence confirmation for periodic payments due to receiving user not recognized<br>* `AP14` - Paying user rejects recurrence confirmation for periodic payments due to receiving user not interested in using Automatic Pix<br> | enum: ["AP13", "AP14"]; example: "AP14" |
| `max_payment_amount` | number (schema `MaxPaymentAmount`) | no | Payer-defined maximum payment amount for dynamic amount recurrences. | example: 86753.09 |
| `journey_type` | string (schema `JourneyType`) | yes | Recurrence payment type: <br><br> `AUT1` - Bank notification. If the merchant has the payer's banking information, a push notification can be sent directly to the payer's bank app, prompting them to authorize the recurring payment.<br> <br> `AUT2` - Authorization via QR code. Payer scans a merchant provided QR code to authorize recurring payments. This method does not initiate an immediate payment, allowing the first payment to be scheduled for a later date.<br> <br> `AUT3` - Authorization via QR code with first payment.  Similar to the second method, but the QR code includes information for both the authorization and the initial payment, enabling the payer to authorize the recurring payment and make the first payment in a single step.<br> <br> `AUT4` - Post-payment sign-up path. After completing a one-time payment via QR code, the payer is offered the option to authorize recurring payments for future transactions<br> | enum: ["AUT1", "AUT2", "AUT3", "AUT4"]; example: "AUT1" |
| `payment_date_time` | string (schema `PaymentDateTime`) | no | Date time from a successful payment. Mandatory for the `AUT3` journey. RFC 3339 value. Format: YYYY-MM-DDThh:mm:ss.SSSZ.<br> | format: "datetime"; example: "2020-08-13T13:49:03.000Z" |
| `transaction_identification` | string (schema `TransactionIdentification`) | no | Transaction ID from a successful payment. **REQUIRED** for the `AUT3` journey. | maxLength: 35; example: "ttx2020010300000000000000000000001" |
| `city_code` | string (schema `CityCode`) | no | <br>An <a href='https://www.ibge.gov.br/explica/codigos-dos-municipios.php' target="_blank">IBGE</a> municipal code is a 7-digit numerical ID that the Brazilian Institute of Geography and Statistics (IBGE) assigns to uniquely ID each municipality and federal district in Brazil.<br> | minLength: 7; maxLength: 7; example: "3550308" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | OK | `application/json`: object (schema `AuthorizationResponse`) |
| 400 | Bad request | `application/json`: object (schema `customer.Error`) |
| 401 | Unauthorized. Missing or invalid authentication token. | `application/json`: object (schema `customer.Error`) |
| 404 | Not found | `application/json`: object (schema `customer.Error`) |
| 500 | Internal Server Error | `application/json`: object (schema `customer.Error`) |

##### Response 201

**201 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | string (schema `AuthorizationID`) | no | Authorization ID the same as BACEN (Brazil Central Bank) IdSoliReq (request identification code) | example: "IS0435879820240605bcdb1fhn43a" |
| `expiration_date` | string (schema `ExpirationDate`) | no | Authorization expiration date. RFC 3339 value. Format = YYYY-MM-DDThh:mm:ss.SSSZ | format: "datetime"; example: "2020-08-13T13:49:03.000Z" |
| `creted_at` | string (schema `CreatedAt`) | no | Created at datetime. RFC 3339 format <br> | format: "datetime"; example: "2025-11-14T17:54:40Z" |
| `updated_at` | string (schema `UpdatedAt`) | no | Scheduled item last updated time, RFC 3339 format | example: "2024-11-14T17:54:40Z" |
| `reason_code` | string (schema `AuthorizationReasonCode`) | no | Authorization reason code. <br><br>**Note:** "pain.009" is a message sent to the payer when the payee starts a #1 journey (`AUT1`) Automatic Pix recurrence<br><br>* `AC01` - Account not found or not belonging to the paying user<br>* `AC04` - Paying user's transactional account is closed<br>* `AC06` - Paying user's transactional account is blocked<br>* `AP01` - Discrepancy in the field for updating periodic payments recurrence data and the periodic payments recurrence status - lack of synchronization<br>* `AP02` - Paying user's CPF/CNPJ  not found or different from the one in the original pain.009. Or, in the case of cancellation, the paying user's CPF/CNPJ does not match the one contained in the perioduc payments recurrence data.<br>* `AP03` - Paying user's branch not found<br>* `AP04` - Invalid recurrence ID or does not match the original<br>* `AP05` - Inconsistent recurrence status for periodic payments<br>* `AP06` - Receiving user's CPF/CNPJ is different from the one in the pain.009 or the payload. Or, in the case of cancellation, the receiving user's CPF/CNPJ does not match the one contained in the periodic payments recurrence data.<br>* `AP07` - Paying user's recurrence confirmation performed after the confirmation request's expiration or cancellation (pain.009)<br>* `AP08` - First immediate payment associated with the recurrence was not identified. (Valid only for Authorization Journey 3 (`AUT3`))<br>* `AP09` - Recurrence confirmation request for periodic payments was not identified to enable its cancellation<br>* `AP10` - Cancellation requestor's CPF/CNPJ does not match the the paying/receiving user's or the paying/receiving PSP's identification contained in the periodic payments recurrence data.<br>* `AP11` - Paying PSP's ISPB diverges from the information contained in the recurrence for periodic payments<br>* `AP12` - Receiving PSP's ISPB diverges from the information contained in the recurrence for periodic payments<br>* `AP13` = Paying user rejects periodic payments recurrence confirmation request due to receiving user non-recognition<br>* `AP14` - Paying user rejects periodic payments recurrence confirmation request due to receiving user's lack of interest in using Pix Automatic<br>* `AP15` - Paying user's participant rejects recurrence confirmation request for periodic payments as they chose not to offer Pix Automatic usage for corporate clients<br>* `CH16` - Incorrect or incompatible message content with business rules<br>* `MD01` - Cancellation request's recurrence object does not exist. Should not be used for cancellation requests of pain.009 with status = `PDNG`. That is, a recurrence with status = `PDNG` should be considered as an existing recurrence.<br>* `MD20` - Cancellation request's recurrence object has already expired.<br> | enum: ["AC01", "AC04", "AC06", "AP01", "AP02", "AP03", "AP04", "AP05", "AP06", "AP07", "AP08", "AP09", "AP10", "AP11", "AP12", "AP13", "AP14", "AP15", "CH16", "MD01", "MD20"]; example: "AC01" |
| `status` | string | no | Authorization status | enum: ["CREATED", "RECEIVED", "ACCEPTED", "REJECTED", "EXPIRED", "CANCELLED"]; example: "ACCEPTED" |
| `payer` | object (schema `Payer`) | no |  |  |

##### Response 400

- Response header `x-cid`: Request tracking ID. (string)
##### Response 404

- Response header `x-cid`: Request tracking ID. (string)
##### Response 500

- Response header `x-cid`: Request tracking ID. (string)

Catalogue row (api-reference-data/operations_catalog.csv): response codes `201;400;401;404;500`, has examples `False`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-PAY-pix-automatic`.

<!-- op: spec=api-specs/Instant_payments_-_Automatic_Pix.yaml method=PATCH path=/inst-pull-pay/v1/pix/automatic/payment/order/{end_to_end_id} operationId=update-order-automatic-pix -->
### `PATCH /inst-pull-pay/v1/pix/automatic/payment/order/{end_to_end_id}` — Update payment order amount

- **operationId:** `update-order-automatic-pix`
- **Specification:** `api-specs/Instant_payments_-_Automatic_Pix.yaml` (Instant payments - Automatic Pix)
- **Server base URL(s):** `https://sandbox-cdn.pismolabs.io`, `https://sandbox-cdn.pismolabs.io/inst-pull-pay`
- **Tags:** `Automatic Pix`
- **Deprecated in specification:** no
- **Security requirement:** not declared

**Description (from the specification):**

> Update payment order amount.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Account token - an access token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a <b>401 Unauthorized</b> message. | example: "Bearer eyJhbGci...IUzUx" |
| `Idempotency-Key` | header | yes | string | A unique ID to ensure the operation remains idempotent, allowing for operation repitition without causing unintended effects or duplication. An idempotent operation is one that can be applied multiple times, yet the outcome remains the same. it ensures that network errors, retries, or failures can occur without introducing inconsistencies.<br> |  |
| `x-account` | header | yes | integer | Pismo account ID. | example: 0 |
| `end_to_end_id` | path | yes | string | Transaction end-to-end ID. This field is a Brazil Central Bank (BCB) requirement to track all Pix transaction steps. |  |

#### Request body

Required: yes

**Content type `application/json`** — schema: object (schema `UpdatePaymentOrderRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `amount` | number | no | New amount value, can be filled when recurrence has a dynamic amount. Defined by the payee. | example: 101.11 |
| `taxes` | object (schema `TaxesWithCategory`) | no | Now only available on ext env and just for direct participants. Tax information related to the transaction. |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 204 | No Content |  |
| 400 | Bad request | `application/json`: object (schema `customer.Error`) |
| 401 | Unauthorized. Missing or invalid authentication token. | `application/json`: object (schema `customer.Error`) |
| 404 | Not found | `application/json`: object (schema `customer.Error`) |
| 500 | Internal Server Error | `application/json`: object (schema `customer.Error`) |

##### Response 400

- Response header `x-cid`: Request tracking ID. (string)
##### Response 404

- Response header `x-cid`: Request tracking ID. (string)
##### Response 500

- Response header `x-cid`: Request tracking ID. (string)

Catalogue row (api-reference-data/operations_catalog.csv): response codes `204;400;401;404;500`, has examples `False`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-PAY-pix-automatic`.

<!-- op: spec=api-specs/Instant_payments_-_Automatic_Pix.yaml method=POST path=/inst-pull-pay/v1/pix/automatic/payment/order/cancel operationId=cancel-automatic-pix-payment-order -->
### `POST /inst-pull-pay/v1/pix/automatic/payment/order/cancel` — Cancel payment order

- **operationId:** `cancel-automatic-pix-payment-order`
- **Specification:** `api-specs/Instant_payments_-_Automatic_Pix.yaml` (Instant payments - Automatic Pix)
- **Server base URL(s):** `https://sandbox-cdn.pismolabs.io`, `https://sandbox-cdn.pismolabs.io/inst-pull-pay`
- **Tags:** `Automatic Pix`
- **Deprecated in specification:** no
- **Security requirement:** not declared

**Description (from the specification):**

> Cancel the payment order in the provider.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Account token - an access token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a <b>401 Unauthorized</b> message. | example: "Bearer eyJhbGci...IUzUx" |
| `Idempotency-Key` | header | yes | string | A unique ID to ensure the operation remains idempotent, allowing for operation repitition without causing unintended effects or duplication. An idempotent operation is one that can be applied multiple times, yet the outcome remains the same. it ensures that network errors, retries, or failures can occur without introducing inconsistencies.<br> |  |
| `x-account` | header | yes | integer | Pismo account ID. | example: 0 |

#### Request body

Required: yes

**Content type `application/json`** — schema: object (schema `CancelPaymentOrderRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `end_to_end_id` | string (schema `EndToEndID`) | yes | This field is a Brazil Central Bank (BCB) requirement to track all steps of Pix transactions. <br /><br>Basically, there are two steps to a Pix transaction: <br /><br>    1. Initialize a transaction <br /><br>    2. Confirm a transaction <br /><br>The `end_to_end_id` is sent to the BCB in both steps in order to identify all transaction information. <br /><br> | example: "E3030629420200808195101608910248" |
| `reason` | string (schema `PaymentOrderReason`) | yes | Payment order cancellation reason: <br><br>* `ACCT` - Paying or receiving user's transactional account closed<br>* `BLCK` - Paying or receiving user's transactional account blocked<br>* `CCLD` - Recurring payments authorization cancelled<br>* `FAIL` - Settlement process failure or error<br>* `OTHR` - Paying or receiving user requested cancellation for other reasons<br>* `SLBD` - Paying user request<br>* `SLCR` - Receiving user request<br> | enum: ["ACCT", "BLCK", "CCLD", "FAIL", "OTHR", "SLBD", "SLCR"]; example: "ACCT" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `CancelPaymentOrderResponse`) |
| 400 | Bad request | `application/json`: object (schema `customer.Error`) |
| 401 | Unauthorized. Missing or invalid authentication token. | `application/json`: object (schema `customer.Error`) |
| 404 | Not found | `application/json`: object (schema `customer.Error`) |
| 500 | Internal Server Error | `application/json`: object (schema `customer.Error`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `end_to_end_id` | string (schema `EndToEndID`) | yes | This field is a Brazil Central Bank (BCB) requirement to track all steps of Pix transactions. <br /><br>Basically, there are two steps to a Pix transaction: <br /><br>    1. Initialize a transaction <br /><br>    2. Confirm a transaction <br /><br>The `end_to_end_id` is sent to the BCB in both steps in order to identify all transaction information. <br /><br> | example: "E3030629420200808195101608910248" |
| `reason` | string (schema `PaymentOrderReason`) | yes | Payment order cancellation reason: <br><br>* `ACCT` - Paying or receiving user's transactional account closed<br>* `BLCK` - Paying or receiving user's transactional account blocked<br>* `CCLD` - Recurring payments authorization cancelled<br>* `FAIL` - Settlement process failure or error<br>* `OTHR` - Paying or receiving user requested cancellation for other reasons<br>* `SLBD` - Paying user request<br>* `SLCR` - Receiving user request<br> | enum: ["ACCT", "BLCK", "CCLD", "FAIL", "OTHR", "SLBD", "SLCR"]; example: "ACCT" |
| `cancelled_at` | string (schema `CancellatedAt`) | yes | Cancellation date time, RFC 3339 format: YYYY-MM-DDThh:mm:ssZ. | example: "2024-11-14T17:54:40Z" |

##### Response 400

- Response header `x-cid`: Request tracking ID. (string)
##### Response 404

- Response header `x-cid`: Request tracking ID. (string)
##### Response 500

- Response header `x-cid`: Request tracking ID. (string)

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;404;500`, has examples `False`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-PAY-pix-automatic`.

<!-- op: spec=api-specs/Instant_payments_-_Automatic_Pix.yaml method=POST path=/inst-pull-pay/v1/pix/automatic/payment/order/{end_to_end_id}/resend operationId=resend-automatic-pix-payment-order -->
### `POST /inst-pull-pay/v1/pix/automatic/payment/order/{end_to_end_id}/resend` — Resend payment order

- **operationId:** `resend-automatic-pix-payment-order`
- **Specification:** `api-specs/Instant_payments_-_Automatic_Pix.yaml` (Instant payments - Automatic Pix)
- **Server base URL(s):** `https://sandbox-cdn.pismolabs.io`, `https://sandbox-cdn.pismolabs.io/inst-pull-pay`
- **Tags:** `Automatic Pix`
- **Deprecated in specification:** no
- **Security requirement:** not declared

**Description (from the specification):**

> Resend the payment order to the provider. 
>
> You can use this endpoint when: 
>  1. The payer's PSP did not accept the payment order and the status is `REJECTED` or `EXPIRED`, 
>  2. When the payment order was accepted, but the Pix transaction was not found by the due date, with status `CANCELLED`. 
>
>  In these cases, the payment order can be resent to trigger a new attempt to process the payment.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Account token - an access token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a <b>401 Unauthorized</b> message. | example: "Bearer eyJhbGci...IUzUx" |
| `end_to_end_id` | path | yes | string | Transaction end-to-end ID. This field is a Brazil Central Bank (BCB) requirement to track all Pix transaction steps. |  |

#### Request body

Required: yes

**Content type `application/json`** — schema: object (schema `ResendPaymentOrderRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `due_date` | string (schema `CalendarDueDate`) | yes | Calendar due date | example: "2030-10-10" |
| `amount` | number (schema `Amount`) | no | Amount to be transferred. | example: 1050.44 |
| `taxes` | object (schema `TaxesWithCategory`) | no | Now only available on ext env and just for direct participants. Tax information related to the transaction. |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `ResendPaymentOrderResponse`) |
| 400 | Bad request | `application/json`: object (schema `customer.Error`) |
| 401 | Unauthorized. Missing or invalid authentication token. | `application/json`: object (schema `customer.Error`) |
| 404 | Not found | `application/json`: object (schema `customer.Error`) |
| 500 | Internal Server Error | `application/json`: object (schema `customer.Error`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `end_to_end_id` | string (schema `EndToEndID`) | yes | This field is a Brazil Central Bank (BCB) requirement to track all steps of Pix transactions. <br /><br>Basically, there are two steps to a Pix transaction: <br /><br>    1. Initialize a transaction <br /><br>    2. Confirm a transaction <br /><br>The `end_to_end_id` is sent to the BCB in both steps in order to identify all transaction information. <br /><br> | example: "E3030629420200808195101608910248" |
| `created_at` | string (schema `CreatedAt`) | yes | Created at datetime. RFC 3339 format <br> | format: "datetime"; example: "2025-11-14T17:54:40Z" |
| `amount` | number (schema `Amount`) | yes | Amount to be transferred. | example: 1050.44 |
| `due_date` | string (schema `CalendarDueDate`) | yes | Calendar due date | example: "2030-10-10" |
| `cycle_start` | string (schema `CalendarCycleStart`) | yes | Calendar cycle start | example: "2030-10-10" |
| `cycle_end` | string (schema `CalendarCycleEnd`) | yes | Calendar cycle end | example: "2030-10-10" |

##### Response 400

- Response header `x-cid`: Request tracking ID. (string)
##### Response 404

- Response header `x-cid`: Request tracking ID. (string)
##### Response 500

- Response header `x-cid`: Request tracking ID. (string)

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;404;500`, has examples `False`, emits events `0`, deprecated `False`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/Debtor -->
### Schema `Debtor`

Pointer: `#/components/schemas/Debtor`. Type: object (schema `Debtor`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `document_number` | string (schema `DocumentNumber`) | yes | A government document number, such as a Social Security number (US) or Cadastro de Pessoas Físicas number (Brazil). Must be numeric with 11-14 digits.<br> | minLength: 1; maxLength: 14; example: "123412341234" |
| `document_type` | string (schema `PersonType`) | yes | Person type:  <br>* `LEGAL_PERSON` - An actual person with legal rights.<br>* `NATURAL_PERSON` - An entity, such as an organization or company.<br> | enum: ["LEGAL_PERSON", "NATURAL_PERSON"]; example: "NATURAL_PERSON" |
| `name` | string (schema `Name`) | yes | Name | maxLength: 200; example: "Walter Melon" |

<!-- schema: #/components/schemas/Payer -->
### Schema `Payer`

Pointer: `#/components/schemas/Payer`. Type: object (schema `Payer`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `document_number` | string (schema `DocumentNumber`) | yes | A government document number, such as a Social Security number (US) or Cadastro de Pessoas Físicas number (Brazil). Must be numeric with 11-14 digits.<br> | minLength: 1; maxLength: 14; example: "123412341234" |
| `document_type` | string (schema `PersonType`) | yes | Person type:  <br>* `LEGAL_PERSON` - An actual person with legal rights.<br>* `NATURAL_PERSON` - An entity, such as an organization or company.<br> | enum: ["LEGAL_PERSON", "NATURAL_PERSON"]; example: "NATURAL_PERSON" |
| `name` | string (schema `Name`) | yes | Name | maxLength: 200; example: "Walter Melon" |
| `bank` | string (schema `Bank`) | yes | <a href="https://bank.codes/numero-do-banco/bank/banco-central-do-brasil/" target="_blank">ISPB (Identifcador do Sistema de Pagamento Brazil)</a> - the Brazilian Payment System ID for the receiving bank, an 8-digit value. | maxLength: 8; example: "237" |
| `branch` | string (schema `Branch`) | yes | This could be a bank-assigned branch ID or the branch's ISPB number. | maxLength: 4; example: "011" |
| `account_number` | string (schema `AccountNumber2`) | yes | Payer's account number. | maxLength: 20; example: "98765432" |
| `account_type` | string (schema `AccountType`) | no | Account type: <br /><br>  `CACC` - Checking account<br /><br>  `SVGS` - Savings account<br /><br>  `TRAN` - Transactional account (Brazil only). Also known as "conta corrente" in Portuguese, this is a bank account type designed for everyday financial transactions and is the most common type individuals and businesses use for day-to-day banking. <br /><br>  `SLRY` - Salary account. Employer deposits a fixed amount every month.<br /><br> | enum: ["CACC", "SLRY", "SVGS", "TRAN"]; maxLength: 4; example: "TRAN" |
| `city_code` | string (schema `CityCode`) | no | <br>An <a href='https://www.ibge.gov.br/explica/codigos-dos-municipios.php' target="_blank">IBGE</a> municipal code is a 7-digit numerical ID that the Brazilian Institute of Geography and Statistics (IBGE) assigns to uniquely ID each municipality and federal district in Brazil.<br> | minLength: 7; maxLength: 7; example: "3550308" |

<!-- schema: #/components/schemas/TaxesWithOutCategory -->
### Schema `TaxesWithOutCategory`

Pointer: `#/components/schemas/TaxesWithOutCategory`. Type: object (schema `TaxesWithOutCategory`).

> Only available in EXT environment for direct parciapants. Tax information related to the transaction.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `tax_identifier` | string (schema `TaxIdentifier`) | no | Tax identifier, referring to the NF-e, NFS-e or aggregating tax document. <br><br>In Brazil, NF-e and NFS-e are the two primary types of mandatory electronic invoices (Notas Fiscais) used for tax compliance.<br>* NF-e (Nota Fiscal Eletrônica): Used for the sale and movement of physical goods or products. It is regulated at the state level by SEFAZ (SEFAZ (Secretaria da Fazenda) is the State Department of Finance in Brazil.) and travels with the goods.<br>* NFS-e (Nota Fiscal de Serviços Eletrônica): Used for the provision of services (e.g., consulting, repairs, digital subscriptions). It is regulated by individual city governments.<br><br>The value entered must correspond to the tax document used for calculating the IBS and CBS taxes associated with the transaction.<br> | maxLength: 50; example: "IS0435879820240605bcdb1fhn43a" |
| `records` | array of object (schema `RecordsWithOutCategory`) | no | Tax records. At least 2 objects are **REQUIRED** - at least one with `CBS` tax type and at least one with `IBS` tax type<br> |  |

<!-- schema: #/components/schemas/Payee -->
### Schema `Payee`

Pointer: `#/components/schemas/Payee`. Type: object (schema `Payee`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `name` | string (schema `Name`) | yes | Name | maxLength: 200; example: "Walter Melon" |
| `document_number` | string (schema `DocumentNumber`) | yes | A government document number, such as a Social Security number (US) or Cadastro de Pessoas Físicas number (Brazil). Must be numeric with 11-14 digits.<br> | minLength: 1; maxLength: 14; example: "123412341234" |
| `document_type` | string (schema `PersonType`) | yes | Person type:  <br>* `LEGAL_PERSON` - An actual person with legal rights.<br>* `NATURAL_PERSON` - An entity, such as an organization or company.<br> | enum: ["LEGAL_PERSON", "NATURAL_PERSON"]; example: "NATURAL_PERSON" |
| `bank` | string (schema `Bank`) | yes | <a href="https://bank.codes/numero-do-banco/bank/banco-central-do-brasil/" target="_blank">ISPB (Identifcador do Sistema de Pagamento Brazil)</a> - the Brazilian Payment System ID for the receiving bank, an 8-digit value. | maxLength: 8; example: "237" |
| `branch` | string (schema `Branch`) | yes | This could be a bank-assigned branch ID or the branch's ISPB number. | maxLength: 4; example: "011" |
| `account_number` | string (schema `AccountNumber2`) | yes | Payer's account number. | maxLength: 20; example: "98765432" |
| `account_type` | string (schema `AccountType`) | yes | Account type: <br /><br>  `CACC` - Checking account<br /><br>  `SVGS` - Savings account<br /><br>  `TRAN` - Transactional account (Brazil only). Also known as "conta corrente" in Portuguese, this is a bank account type designed for everyday financial transactions and is the most common type individuals and businesses use for day-to-day banking. <br /><br>  `SLRY` - Salary account. Employer deposits a fixed amount every month.<br /><br> | enum: ["CACC", "SLRY", "SVGS", "TRAN"]; maxLength: 4; example: "TRAN" |

<!-- schema: #/components/schemas/AuthorizationResponse -->
### Schema `AuthorizationResponse`

Pointer: `#/components/schemas/AuthorizationResponse`. Type: object (schema `AuthorizationResponse`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | string (schema `AuthorizationID`) | no | Authorization ID the same as BACEN (Brazil Central Bank) IdSoliReq (request identification code) | example: "IS0435879820240605bcdb1fhn43a" |
| `expiration_date` | string (schema `ExpirationDate`) | no | Authorization expiration date. RFC 3339 value. Format = YYYY-MM-DDThh:mm:ss.SSSZ | format: "datetime"; example: "2020-08-13T13:49:03.000Z" |
| `creted_at` | string (schema `CreatedAt`) | no | Created at datetime. RFC 3339 format <br> | format: "datetime"; example: "2025-11-14T17:54:40Z" |
| `updated_at` | string (schema `UpdatedAt`) | no | Scheduled item last updated time, RFC 3339 format | example: "2024-11-14T17:54:40Z" |
| `reason_code` | string (schema `AuthorizationReasonCode`) | no | Authorization reason code. <br><br>**Note:** "pain.009" is a message sent to the payer when the payee starts a #1 journey (`AUT1`) Automatic Pix recurrence<br><br>* `AC01` - Account not found or not belonging to the paying user<br>* `AC04` - Paying user's transactional account is closed<br>* `AC06` - Paying user's transactional account is blocked<br>* `AP01` - Discrepancy in the field for updating periodic payments recurrence data and the periodic payments recurrence status - lack of synchronization<br>* `AP02` - Paying user's CPF/CNPJ  not found or different from the one in the original pain.009. Or, in the case of cancellation, the paying user's CPF/CNPJ does not match the one contained in the perioduc payments recurrence data.<br>* `AP03` - Paying user's branch not found<br>* `AP04` - Invalid recurrence ID or does not match the original<br>* `AP05` - Inconsistent recurrence status for periodic payments<br>* `AP06` - Receiving user's CPF/CNPJ is different from the one in the pain.009 or the payload. Or, in the case of cancellation, the receiving user's CPF/CNPJ does not match the one contained in the periodic payments recurrence data.<br>* `AP07` - Paying user's recurrence confirmation performed after the confirmation request's expiration or cancellation (pain.009)<br>* `AP08` - First immediate payment associated with the recurrence was not identified. (Valid only for Authorization Journey 3 (`AUT3`))<br>* `AP09` - Recurrence confirmation request for periodic payments was not identified to enable its cancellation<br>* `AP10` - Cancellation requestor's CPF/CNPJ does not match the the paying/receiving user's or the paying/receiving PSP's identification contained in the periodic payments recurrence data.<br>* `AP11` - Paying PSP's ISPB diverges from the information contained in the recurrence for periodic payments<br>* `AP12` - Receiving PSP's ISPB diverges from the information contained in the recurrence for periodic payments<br>* `AP13` = Paying user rejects periodic payments recurrence confirmation request due to receiving user non-recognition<br>* `AP14` - Paying user rejects periodic payments recurrence confirmation request due to receiving user's lack of interest in using Pix Automatic<br>* `AP15` - Paying user's participant rejects recurrence confirmation request for periodic payments as they chose not to offer Pix Automatic usage for corporate clients<br>* `CH16` - Incorrect or incompatible message content with business rules<br>* `MD01` - Cancellation request's recurrence object does not exist. Should not be used for cancellation requests of pain.009 with status = `PDNG`. That is, a recurrence with status = `PDNG` should be considered as an existing recurrence.<br>* `MD20` - Cancellation request's recurrence object has already expired.<br> | enum: ["AC01", "AC04", "AC06", "AP01", "AP02", "AP03", "AP04", "AP05", "AP06", "AP07", "AP08", "AP09", "AP10", "AP11", "AP12", "AP13", "AP14", "AP15", "CH16", "MD01", "MD20"]; example: "AC01" |
| `status` | string | no | Authorization status | enum: ["CREATED", "RECEIVED", "ACCEPTED", "REJECTED", "EXPIRED", "CANCELLED"]; example: "ACCEPTED" |
| `payer` | object (schema `Payer`) | no |  |  |

<!-- schema: #/components/schemas/TaxesWithCategory -->
### Schema `TaxesWithCategory`

Pointer: `#/components/schemas/TaxesWithCategory`. Type: object (schema `TaxesWithCategory`).

> Now only available on ext env and just for direct participants. Tax information related to the transaction.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `tax_identifier` | string (schema `TaxIdentifier`) | no | Tax identifier, referring to the NF-e, NFS-e or aggregating tax document. <br><br>In Brazil, NF-e and NFS-e are the two primary types of mandatory electronic invoices (Notas Fiscais) used for tax compliance.<br>* NF-e (Nota Fiscal Eletrônica): Used for the sale and movement of physical goods or products. It is regulated at the state level by SEFAZ (SEFAZ (Secretaria da Fazenda) is the State Department of Finance in Brazil.) and travels with the goods.<br>* NFS-e (Nota Fiscal de Serviços Eletrônica): Used for the provision of services (e.g., consulting, repairs, digital subscriptions). It is regulated by individual city governments.<br><br>The value entered must correspond to the tax document used for calculating the IBS and CBS taxes associated with the transaction.<br> | maxLength: 50; example: "IS0435879820240605bcdb1fhn43a" |
| `records` | array of object (schema `RecordsWithCategory`) | no | Tax records. It is **REQUIRED** to pass a minimum of 2 objects and a maximum of 4 objects, at least one with `CBS` tax type and at least one with `IBS` tax type.<br> |  |

<!-- schema: #/components/schemas/customer.Error -->
### Schema `customer.Error`

Pointer: `#/components/schemas/customer.Error`. Type: object (schema `customer.Error`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string | no | Error's code. | example: "EPT0001" |
| `details` | object (schema `customer.DetailMessage`) | no |  |  |
| `message` | string | no | Error's message. | example: "User not found" |

<!-- schema: #/components/schemas/RecordsWithOutCategory -->
### Schema `RecordsWithOutCategory`

Pointer: `#/components/schemas/RecordsWithOutCategory`. Type: object (schema `RecordsWithOutCategory`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `tax_type` | string (schema `TaxType`) | no | Tax type:<br>* `IBS` = Goods and services tax. A state and municipal tax that unifies and replaces the main subnational consumption taxes (state ICMS and municipal ISS).<br>* `CBS` = Contribution on goods and services. A federal tax that consolidates and replaces previous federal social contributions and taxes (PIS, Cofins, and IPI)<br> | enum: ["CBS", "IBS"]; example: "IBS" |
| `amount` | number (schema `TaxAmount`) | no | Tax amount. Must be greater than zero. | example: 1050.44 |

<!-- schema: #/components/schemas/RecordsWithCategory -->
### Schema `RecordsWithCategory`

Pointer: `#/components/schemas/RecordsWithCategory`. Type: object (schema `RecordsWithCategory`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `tax_type` | string (schema `TaxType`) | no | Tax type:<br>* `IBS` = Goods and services tax. A state and municipal tax that unifies and replaces the main subnational consumption taxes (state ICMS and municipal ISS).<br>* `CBS` = Contribution on goods and services. A federal tax that consolidates and replaces previous federal social contributions and taxes (PIS, Cofins, and IPI)<br> | enum: ["CBS", "IBS"]; example: "IBS" |
| `tax_category` | string (schema `TaxCategory`) | no | Tax category: <br>* `INF` (Conta e Ordem) = Tax information<br>* `COR` (Informar no momento da emissão)) = Corrected tax<br> | enum: ["INF", "COR"]; example: "INF" |
| `amount` | number (schema `TaxAmount`) | no | Tax amount. Must be greater than zero. | example: 1050.44 |

<!-- schema: #/components/schemas/customer.DetailMessage -->
### Schema `customer.DetailMessage`

Pointer: `#/components/schemas/customer.DetailMessage`. Type: object (schema `customer.DetailMessage`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `external` | array of object (schema `customer.ExternalMessage`) | no |  |  |
| `parameters` | array of object (schema `customer.ParameterMessage`) | no |  |  |
| `payload` | array of object (schema `customer.PayloadMessage`) | no |  |  |

<!-- schema: #/components/schemas/customer.ExternalMessage -->
### Schema `customer.ExternalMessage`

Pointer: `#/components/schemas/customer.ExternalMessage`. Type: object (schema `customer.ExternalMessage`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string | yes | Error code. | example: "PBE315" |
| `message` | string | yes | Error message. | example: "Generic error" |

<!-- schema: #/components/schemas/customer.ParameterMessage -->
### Schema `customer.ParameterMessage`

Pointer: `#/components/schemas/customer.ParameterMessage`. Type: object (schema `customer.ParameterMessage`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `field` | string | yes | Parameter field | example: "Query parameter" |
| `message` | string | yes | Message about parameter | example: "Generic error" |

<!-- schema: #/components/schemas/customer.PayloadMessage -->
### Schema `customer.PayloadMessage`

Pointer: `#/components/schemas/customer.PayloadMessage`. Type: object (schema `customer.PayloadMessage`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `field` | string | yes | Payload parameter | example: "Entity.field" |
| `message` | string | yes | Message about error | example: "Generic error" |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Instant_payments_-_Automatic_Pix.yaml` | tag `Automatic Pix`: POST /inst-pull-pay/v1/pix/automatic, PATCH /inst-pull-pay/v1/pix/automatic/{recurrence_id}, POST /inst-pull-pay/v1/pix/automatic/cancel, POST /inst-pull-pay/v1/pix/automatic/payer/authorization, PATCH /inst-pull-pay/v1/pix/automatic/payment/order/{end_to_end_id}, POST /inst-pull-pay/v1/pix/automatic/payment/order/cancel, POST /inst-pull-pay/v1/pix/automatic/payment/order/{end_to_end_id}/resend | https://github.com/PismoDevEx/pismo-api-specs | `df884687741cd089…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-PAY-pix-automatic` — Pix Automatic
