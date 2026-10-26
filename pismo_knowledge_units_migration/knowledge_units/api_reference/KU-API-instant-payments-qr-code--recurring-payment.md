---
ku_id: KU-API-instant-payments-qr-code--recurring-payment
title: 'API reference: Instant payments - QR Code — Recurring payment'
category: api_reference
ku_type: api_reference
lifecycle: current
sources:
- path: api-specs/Instant_payments_-_QR_Code.yaml
  sha256: 92acd63f86546e9b570b3ffb1644eb0fa5217f1aaea7e6d85163f0e09b66aa36
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
- post-create-recurrence-cob
- post-create-recurrence-cobv
- post-create-static
- post-create-recurrence
- post-cancel-recurrence
related_kus:
- KU-PAY-pix-and-qr-codes
- KU-PAY-pix-automatic
specification_version: '1.0'
---

# API reference: Instant payments - QR Code — Recurring payment

**KU ID:** `KU-API-instant-payments-qr-code--recurring-payment` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 5 operation(s) tagged `Recurring payment` in `api-specs/Instant_payments_-_QR_Code.yaml` (“Instant payments - QR Code”, version `1.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `POST /v1/pix/qrcode/cob/recurrence` | `post-create-recurrence-cob` | Create recurrent COB QR Code | no |
| `POST /v1/pix/qrcode/cobv/recurrence` | `post-create-recurrence-cobv` | Create recurrent COBV QR Code | no |
| `POST /v1/pix/qrcode/static/recurrence` | `post-create-static` | Create recurrent static QR Code | no |
| `POST /v1/pix/qrcode/recurrence` | `post-create-recurrence` | Create recurrent compound QR Code | no |
| `POST /v1/pix/qrcode/recurrence/cancel` | `post-cancel-recurrence` | Cancel recurrent compound QR Code [Beta] | no |

## Operation contracts

<!-- op: spec=api-specs/Instant_payments_-_QR_Code.yaml method=POST path=/v1/pix/qrcode/cob/recurrence operationId=post-create-recurrence-cob -->
### `POST /v1/pix/qrcode/cob/recurrence` — Create recurrent COB QR Code

- **operationId:** `post-create-recurrence-cob`
- **Specification:** `api-specs/Instant_payments_-_QR_Code.yaml` (Instant payments - QR Code)
- **Server base URL(s):** `https://sandbox-cdn.pismolabs.io/qrcode`
- **Tags:** `Recurring payment`
- **Deprecated in specification:** no
- **Security requirement:** not declared

**Description (from the specification):**

> Create a COB QR Code for a recurring payment as a EMV (Europay Mastercard Visa) string.
>
> COB is short for *cobranca*, which means charge in Portuguese. A COB QR Code has an expiration date while a COBV QR Code has a due date, fine, interest, and rebates.
>
> For more information, refer to [Pix and QR Codes](doc:pix-and-qr-codes).
>
> **Note:** This endpoint takes an account token - an access token encoded with a Pismo account ID.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Account token - token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a <b>401 Unauthorized</b> message.<br> |  |

#### Request body

Required: yes

> Create recurrent COB QR Code request body

**Content type `application/json`** — schema: object (schema `qrcode.CreateRecurrenceQrCodeCobRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `payee` | object (schema `qrcode.PayeeRequest`) | yes | Payee information |  |
| `payer` | object (schema `qrcode.PayerRequest`) | yes | Payer information |  |
| `initial_amount` | number (schema `initialAmount`) | yes | Initial payment amount | example: 86753.09 |
| `transaction_identification` | string (schema `transactionID`) | yes | Client-generated unique transaction ID for client monitoring and tracking.<br> | minLength: 26; maxLength: 36; example: "trans-id-75789947401234567" |
| `payer_solicitation` | string (schema `payerSolicitation`) | no | Payee text sent to payer. | maxLength: 140; example: "For dinner last night" |
| `allows_value_change` | boolean (schema `allowsValueChange`) | no | Can payer change payment values? Default is `false`. | example: true |
| `qrcode_expiration_time` | integer (schema `qrcodeExpirationTime`) | no | QR Code's maximum time for presentation (in seconds) | example: 7200 |
| `additional_information` | array of object (schema `qrcode.Additional`) (schema `additionalInfo`) | no | Additional remarks |  |
| `reusable` | boolean (schema `reusable`) | no | Can QR Code be reused? Default is `false`. | default: false; example: true |
| `location` | object (schema `qrcode.LocationDynamicQrcode`) | no | Location URL information |  |
| `recurrence_id` | string (schema `recurrenceID`) | no | Recurrence ID. Either this or the `recurrence` object is **REQUIRED**. | example: "RN219952X6X02505XXCONTRACTXXX" |
| `recurrence` | object (schema `qrcode.Recurrence`) | no | Recurrence object. Either this or `recurrence_id` is **REQUIRED**. |  |
| `access_token` | string (schema `accessTokenRequest`) | no | Access token related to the `url_payload`/`url_payload_rec` fields, used to register and validate a QR code.<br><br>This field **must** be provided if the PSP requires it. The URL format is described in the Manual of Standards for PIX Initiation.<br> | example: "153ed19a-e738-4417-9e98-a515c276a731" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 202 | Create Recurrence Cob QR Code response | `application/json`: object (schema `qrcode.CreateRecurrenceQrCodeCobResponse`) |
| 400 | Bad request | `application/json`: object (schema `customer.Error`) |
| 401 | Invalid authorization | `application/json`: object (schema `customer.Error`) |
| 403 | Forbidden | `application/json`: object (schema `customer.Error`) |
| 404 | Not found | `application/json`: object (schema `customer.Error`) |
| 409 | Conflict | `application/json`: object (schema `customer.Error`) |
| 429 | Too many reqquests | `application/json`: object (schema `customer.Error`) |
| 500 | Internal Server Error | `application/json`: object (schema `customer.Error`) |
| 502 | Bad Gateway | `application/json`: object (schema `customer.Error`) |
| 504 | Gateway Timeout | `application/json`: object (schema `customer.Error`) |

##### Response 202

- Response header `x-cid`: Request tracking identifier (string)
**202 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | string (schema `qrcodeID`) | yes | Pismo QR Code identifier | example: "442e992a-2f89-46fb-820a-958693bde84d" |
| `access_token` | string (schema `accessToken`) | yes | QR Code access token generated and returned at creation.<br> | example: "1234567890" |
| `external_id` | string (schema `externalID`) | yes | Client-generated record identifier for client tracking and monitoring.<br> | example: "my-external-id-9999-6474" |
| `emv` | string (schema `emv`) | yes | Base 64 encoded discount QR Code payload. EMV = Europay, Mastercard and Visa, a global standard for credit and debit payment. The EMV might include details required for secure transactions such as cardholder informatipn, transaction amount, merchant information, and other relevant data.<br> | example: "00020101021226980014br.gov.bcb.pix2576api-h.developer.btgpactual.com/pc/p/v2/...***63040441" |
| `qrcode_imageb64` | string (schema `qrcode.imageb64`) | no | Base64 encoded QR Code | example: "dfkk7830o*&#)@#9FEE" |
| `recurrence_id` | string (schema `recurrenceID`) | yes | Recurrence ID. Either this or the `recurrence` object is **REQUIRED**. | example: "RN219952X6X02505XXCONTRACTXXX" |
| `jws` | string (schema `jws`) | no | JWS (JSON Web Signature) payload. When a JWT (JSON Web Token) is signed, it becomes a JWS.<br> | example: "eYqqqwq.heif.jk2w" |
| `jws_rec` | string (schema `jwsRec`) | no | Signed JWS payload, referring to the data of the recurrence.<br> | example: "eYqqqwq.heif.jk2w" |

##### Response 400

- Response header `x-cid`: Request tracking identifier (string)
##### Response 401

- Response header `x-cid`: Request tracking identifier (string)
##### Response 403

- Response header `x-cid`: Request tracking identifier (string)
##### Response 404

- Response header `x-cid`: Request tracking identifier (string)
##### Response 409

- Response header `x-cid`: Request tracking identifier (string)
##### Response 429

- Response header `x-cid`: Request tracking identifier (string)
##### Response 500

- Response header `x-cid`: Request tracking identifier (string)
##### Response 502

- Response header `x-cid`: Request tracking identifier (string)
##### Response 504

- Response header `x-cid`: Request tracking identifier (string)

Catalogue row (api-reference-data/operations_catalog.csv): response codes `202;400;401;403;404;409;429;500;502;504`, has examples `False`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-PAY-pix-and-qr-codes`, `KU-PAY-pix-automatic`.

<!-- op: spec=api-specs/Instant_payments_-_QR_Code.yaml method=POST path=/v1/pix/qrcode/cobv/recurrence operationId=post-create-recurrence-cobv -->
### `POST /v1/pix/qrcode/cobv/recurrence` — Create recurrent COBV QR Code

- **operationId:** `post-create-recurrence-cobv`
- **Specification:** `api-specs/Instant_payments_-_QR_Code.yaml` (Instant payments - QR Code)
- **Server base URL(s):** `https://sandbox-cdn.pismolabs.io/qrcode`
- **Tags:** `Recurring payment`
- **Deprecated in specification:** no
- **Security requirement:** not declared

**Description (from the specification):**

> Create a COBV QR Code for a recurring payment as a EMV (Europay Mastercard Visa) string.
>
> For more information, refer to [Pix and QR Codes](doc:pix-and-qr-codes).
>
> **Note:** This endpoint takes an account token - an access token encoded with a Pismo account ID.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Account token - token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a <b>401 Unauthorized</b> message.<br> |  |

#### Request body

Required: no

> Create recurrent Cob QR Code request

**Content type `application/json`** — schema: object (schema `qrcode.CreateRecurrenceQrCodeCobvRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `charge` | object (schema `charge`) | yes | Charge information |  |
| `payee` | object (schema `qrcode.PayeeRequest`) | yes | Payee information |  |
| `payer` | object (schema `qrcode.PayerRequest`) | yes | Payer information |  |
| `initial_amount` | number (schema `initialAmount`) | yes | Initial payment amount | example: 86753.09 |
| `transaction_identification` | string (schema `transactionID`) | yes | Client-generated unique transaction ID for client monitoring and tracking.<br> | minLength: 26; maxLength: 36; example: "trans-id-75789947401234567" |
| `payer_solicitation` | string (schema `payerSolicitation`) | no | Payee text sent to payer. | maxLength: 140; example: "For dinner last night" |
| `allows_value_change` | boolean (schema `allowsValueChange`) | no | Can payer change payment values? Default is `false`. | example: true |
| `additional_information` | array of object (schema `qrcode.Additional`) (schema `additionalInfo`) | no | Additional remarks |  |
| `reusable` | boolean (schema `reusable`) | no | Can QR Code be reused? Default is `false`. | default: false; example: true |
| `location` | object (schema `qrcode.LocationDynamicQrcode`) | no | Location URL information |  |
| `recurrence_id` | string (schema `recurrenceID`) | no | Recurrence ID. Either this or the `recurrence` object is **REQUIRED**. | example: "RN219952X6X02505XXCONTRACTXXX" |
| `recurrence` | object (schema `qrcode.Recurrence`) | no | Recurrence object. Either this or `recurrence_id` is **REQUIRED**. |  |
| `access_token` | string (schema `accessTokenRequest`) | no | Access token related to the `url_payload`/`url_payload_rec` fields, used to register and validate a QR code.<br><br>This field **must** be provided if the PSP requires it. The URL format is described in the Manual of Standards for PIX Initiation.<br> | example: "153ed19a-e738-4417-9e98-a515c276a731" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 202 | Create recurrent COBV QR Code response | `application/json`: object (schema `qrcode.CreateRecurrenceQrCodeCobvResponse`) |
| 400 | Bad request | `application/json`: object (schema `customer.Error`) |
| 401 | Invalid authorization | `application/json`: object (schema `customer.Error`) |
| 403 | Forbidden | `application/json`: object (schema `customer.Error`) |
| 404 | Not found | `application/json`: object (schema `customer.Error`) |
| 409 | Conflict | `application/json`: object (schema `customer.Error`) |
| 429 | Too many reqquests | `application/json`: object (schema `customer.Error`) |
| 500 | Internal Server Error | `application/json`: object (schema `customer.Error`) |
| 502 | Bad Gateway | `application/json`: object (schema `customer.Error`) |
| 504 | Gateway Timeout | `application/json`: object (schema `customer.Error`) |

##### Response 202

- Response header `x-cid`: Request tracking identifier (string)
**202 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | string (schema `qrcodeID`) | yes | Pismo QR Code identifier | example: "442e992a-2f89-46fb-820a-958693bde84d" |
| `access_token` | string (schema `accessToken`) | yes | QR Code access token generated and returned at creation.<br> | example: "1234567890" |
| `external_id` | string (schema `externalID`) | yes | Client-generated record identifier for client tracking and monitoring.<br> | example: "my-external-id-9999-6474" |
| `emv` | string (schema `emv`) | yes | Base 64 encoded discount QR Code payload. EMV = Europay, Mastercard and Visa, a global standard for credit and debit payment. The EMV might include details required for secure transactions such as cardholder informatipn, transaction amount, merchant information, and other relevant data.<br> | example: "00020101021226980014br.gov.bcb.pix2576api-h.developer.btgpactual.com/pc/p/v2/...***63040441" |
| `qrcode_imageb64` | string (schema `qrcode.imageb64`) | no | Base64 encoded QR Code | example: "dfkk7830o*&#)@#9FEE" |
| `recurrence_id` | string (schema `recurrenceID`) | yes | Recurrence ID. Either this or the `recurrence` object is **REQUIRED**. | example: "RN219952X6X02505XXCONTRACTXXX" |
| `jws` | string (schema `jws`) | no | JWS (JSON Web Signature) payload. When a JWT (JSON Web Token) is signed, it becomes a JWS.<br> | example: "eYqqqwq.heif.jk2w" |
| `jws_rec` | string (schema `jwsRec`) | no | Signed JWS payload, referring to the data of the recurrence.<br> | example: "eYqqqwq.heif.jk2w" |

##### Response 400

- Response header `x-cid`: Request tracking identifier (string)
##### Response 401

- Response header `x-cid`: Request tracking identifier (string)
##### Response 403

- Response header `x-cid`: Request tracking identifier (string)
##### Response 404

- Response header `x-cid`: Request tracking identifier (string)
##### Response 409

- Response header `x-cid`: Request tracking identifier (string)
##### Response 429

- Response header `x-cid`: Request tracking identifier (string)
##### Response 500

- Response header `x-cid`: Request tracking identifier (string)
##### Response 502

- Response header `x-cid`: Request tracking identifier (string)
##### Response 504

- Response header `x-cid`: Request tracking identifier (string)

Catalogue row (api-reference-data/operations_catalog.csv): response codes `202;400;401;403;404;409;429;500;502;504`, has examples `False`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-PAY-pix-and-qr-codes`.

<!-- op: spec=api-specs/Instant_payments_-_QR_Code.yaml method=POST path=/v1/pix/qrcode/static/recurrence operationId=post-create-static -->
### `POST /v1/pix/qrcode/static/recurrence` — Create recurrent static QR Code

- **operationId:** `post-create-static`
- **Specification:** `api-specs/Instant_payments_-_QR_Code.yaml` (Instant payments - QR Code)
- **Server base URL(s):** `https://sandbox-cdn.pismolabs.io/qrcode`
- **Tags:** `Recurring payment`
- **Deprecated in specification:** no
- **Security requirement:** not declared

**Description (from the specification):**

> Create a recurrent static QR Code and EMV (Europay Mastercard Visa) string.
>
> For more information, refer to [Pix and QR Codes](doc:pix-and-qr-codes).
>
> **Note:** This endpoint takes an account token - an access token encoded with a Pismo account ID.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Account token - token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a <b>401 Unauthorized</b> message.<br> |  |

#### Request body

Required: yes

> Create Recurrence Static QR Code request

**Content type `application/json`** — schema: object (schema `qrcode.CreateRecurrenceQrCodeStaticRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `payee` | object (schema `qrcode.PayeeRequest`) | yes | Payee information |  |
| `amount` | number (schema `initialAmount`) | yes | Initial payment amount | example: 86753.09 |
| `transaction_identification` | string (schema `transactionIDSmall`) | yes | Client-generated unique transaction ID for client monitoring and tracking.<br> | maxLength: 25; example: "trans-id-7578994740" |
| `additional_information` | string (schema `additionalInformation`) | no | Additional information about the new QR Code creation | maxLength: 64; example: "Additional info about this qrcode" |
| `location` | object (schema `qrcode.LocationStatic`) | no | Location URL information |  |
| `recurrence_id` | string (schema `recurrenceID`) | no | Recurrence ID. Either this or the `recurrence` object is **REQUIRED**. | example: "RN219952X6X02505XXCONTRACTXXX" |
| `recurrence` | object (schema `qrcode.Recurrence`) | no | Recurrence object. Either this or `recurrence_id` is **REQUIRED**. |  |
| `access_token` | string (schema `accessTokenRequest`) | no | Access token related to the `url_payload`/`url_payload_rec` fields, used to register and validate a QR code.<br><br>This field **must** be provided if the PSP requires it. The URL format is described in the Manual of Standards for PIX Initiation.<br> | example: "153ed19a-e738-4417-9e98-a515c276a731" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 202 | Generate COB QR Code response | `application/json`: object (schema `qrcode.CreateRecurrenceQrCodeStaticResponse`) |
| 400 | Bad request | `application/json`: object (schema `customer.Error`) |
| 401 | Invalid authorization | `application/json`: object (schema `customer.Error`) |
| 403 | Forbidden | `application/json`: object (schema `customer.Error`) |
| 404 | Not found | `application/json`: object (schema `customer.Error`) |
| 409 | Conflict | `application/json`: object (schema `customer.Error`) |
| 429 | Too many reqquests | `application/json`: object (schema `customer.Error`) |
| 500 | Internal Server Error | `application/json`: object (schema `customer.Error`) |
| 502 | Bad Gateway | `application/json`: object (schema `customer.Error`) |
| 504 | Gateway Timeout | `application/json`: object (schema `customer.Error`) |

##### Response 202

- Response header `x-cid`: Request tracking identifier (string)
**202 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | string (schema `qrcodeID`) | yes | Pismo QR Code identifier | example: "442e992a-2f89-46fb-820a-958693bde84d" |
| `access_token` | string (schema `accessToken`) | yes | QR Code access token generated and returned at creation.<br> | example: "1234567890" |
| `external_id` | string (schema `externalID`) | yes | Client-generated record identifier for client tracking and monitoring.<br> | example: "my-external-id-9999-6474" |
| `emv` | string (schema `emv`) | yes | Base 64 encoded discount QR Code payload. EMV = Europay, Mastercard and Visa, a global standard for credit and debit payment. The EMV might include details required for secure transactions such as cardholder informatipn, transaction amount, merchant information, and other relevant data.<br> | example: "00020101021226980014br.gov.bcb.pix2576api-h.developer.btgpactual.com/pc/p/v2/...***63040441" |
| `qrcode_imageb64` | string (schema `qrcode.imageb64`) | no | Base64 encoded QR Code | example: "dfkk7830o*&#)@#9FEE" |
| `recurrence_id` | string (schema `recurrenceID`) | yes | Recurrence ID. Either this or the `recurrence` object is **REQUIRED**. | example: "RN219952X6X02505XXCONTRACTXXX" |
| `jws` | string (schema `jws`) | no | JWS (JSON Web Signature) payload. When a JWT (JSON Web Token) is signed, it becomes a JWS.<br> | example: "eYqqqwq.heif.jk2w" |
| `jws_rec` | string (schema `jwsRec`) | no | Signed JWS payload, referring to the data of the recurrence.<br> | example: "eYqqqwq.heif.jk2w" |

##### Response 400

- Response header `x-cid`: Request tracking identifier (string)
##### Response 401

- Response header `x-cid`: Request tracking identifier (string)
##### Response 403

- Response header `x-cid`: Request tracking identifier (string)
##### Response 404

- Response header `x-cid`: Request tracking identifier (string)
##### Response 409

- Response header `x-cid`: Request tracking identifier (string)
##### Response 429

- Response header `x-cid`: Request tracking identifier (string)
##### Response 500

- Response header `x-cid`: Request tracking identifier (string)
##### Response 502

- Response header `x-cid`: Request tracking identifier (string)
##### Response 504

- Response header `x-cid`: Request tracking identifier (string)

Catalogue row (api-reference-data/operations_catalog.csv): response codes `202;400;401;403;404;409;429;500;502;504`, has examples `False`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-PAY-pix-and-qr-codes`.

<!-- op: spec=api-specs/Instant_payments_-_QR_Code.yaml method=POST path=/v1/pix/qrcode/recurrence operationId=post-create-recurrence -->
### `POST /v1/pix/qrcode/recurrence` — Create recurrent compound QR Code

- **operationId:** `post-create-recurrence`
- **Specification:** `api-specs/Instant_payments_-_QR_Code.yaml` (Instant payments - QR Code)
- **Server base URL(s):** `https://sandbox-cdn.pismolabs.io/qrcode`
- **Tags:** `Recurring payment`
- **Deprecated in specification:** no
- **Security requirement:** not declared

**Description (from the specification):**

> Create a compound QR Code containing only recurring payment authorization configuration data.
>
> For more information, refer to [Pix and QR Codes](doc:pix-and-qr-codes).
>
> **Note:** This endpoint takes an account token - an access token encoded with a Pismo account ID.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Account token - token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a <b>401 Unauthorized</b> message.<br> |  |

#### Request body

Required: yes

> Create recurrent QR Code request

**Content type `application/json`** — schema: object (schema `qrcode.CreateRecurrenceQrCodeRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `payee` | object (schema `qrcode.RecurrenceQrcodePayeeRequest`) | yes | Recurence QR Code payee request |  |
| `transaction_identification` | string (schema `transactionIDSmall`) | yes | Client-generated unique transaction ID for client monitoring and tracking.<br> | maxLength: 25; example: "trans-id-7578994740" |
| `location` | object (schema `qrcode.LocationQrcodeComposite`) | no | Location URL information |  |
| `recurrence_id` | string (schema `recurrenceID`) | no | Recurrence ID. Either this or the `recurrence` object is **REQUIRED**. | example: "RN219952X6X02505XXCONTRACTXXX" |
| `recurrence` | object (schema `qrcode.Recurrence`) | no | Recurrence object. Either this or `recurrence_id` is **REQUIRED**. |  |
| `access_token` | string (schema `accessTokenRequest`) | no | Access token related to the `url_payload`/`url_payload_rec` fields, used to register and validate a QR code.<br><br>This field **must** be provided if the PSP requires it. The URL format is described in the Manual of Standards for PIX Initiation.<br> | example: "153ed19a-e738-4417-9e98-a515c276a731" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 202 | Create recurrence QR Code response | `application/json`: object (schema `qrcode.CreateRecurrenceQrCodeResponse`) |
| 400 | Bad request | `application/json`: object (schema `customer.Error`) |
| 401 | Invalid authorization | `application/json`: object (schema `customer.Error`) |
| 403 | Forbidden | `application/json`: object (schema `customer.Error`) |
| 404 | Not found | `application/json`: object (schema `customer.Error`) |
| 409 | Conflict | `application/json`: object (schema `customer.Error`) |
| 429 | Too many reqquests | `application/json`: object (schema `customer.Error`) |
| 500 | Internal Server Error | `application/json`: object (schema `customer.Error`) |
| 502 | Bad Gateway | `application/json`: object (schema `customer.Error`) |
| 504 | Gateway Timeout | `application/json`: object (schema `customer.Error`) |

##### Response 202

- Response header `x-cid`: Request tracking identifier (string)
**202 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | string (schema `qrcodeID`) | yes | Pismo QR Code identifier | example: "442e992a-2f89-46fb-820a-958693bde84d" |
| `access_token` | string (schema `accessToken`) | yes | QR Code access token generated and returned at creation.<br> | example: "1234567890" |
| `external_id` | string (schema `externalID`) | yes | Client-generated record identifier for client tracking and monitoring.<br> | example: "my-external-id-9999-6474" |
| `emv` | string (schema `emv`) | yes | Base 64 encoded discount QR Code payload. EMV = Europay, Mastercard and Visa, a global standard for credit and debit payment. The EMV might include details required for secure transactions such as cardholder informatipn, transaction amount, merchant information, and other relevant data.<br> | example: "00020101021226980014br.gov.bcb.pix2576api-h.developer.btgpactual.com/pc/p/v2/...***63040441" |
| `qrcode_imageb64` | string (schema `qrcode.imageb64`) | no | Base64 encoded QR Code | example: "dfkk7830o*&#)@#9FEE" |
| `recurrence_id` | string (schema `recurrenceID`) | yes | Recurrence ID. Either this or the `recurrence` object is **REQUIRED**. | example: "RN219952X6X02505XXCONTRACTXXX" |
| `jws` | string (schema `jws`) | no | JWS (JSON Web Signature) payload. When a JWT (JSON Web Token) is signed, it becomes a JWS.<br> | example: "eYqqqwq.heif.jk2w" |
| `jws_rec` | string (schema `jwsRec`) | no | Signed JWS payload, referring to the data of the recurrence.<br> | example: "eYqqqwq.heif.jk2w" |

##### Response 400

- Response header `x-cid`: Request tracking identifier (string)
##### Response 401

- Response header `x-cid`: Request tracking identifier (string)
##### Response 403

- Response header `x-cid`: Request tracking identifier (string)
##### Response 404

- Response header `x-cid`: Request tracking identifier (string)
##### Response 409

- Response header `x-cid`: Request tracking identifier (string)
##### Response 429

- Response header `x-cid`: Request tracking identifier (string)
##### Response 500

- Response header `x-cid`: Request tracking identifier (string)
##### Response 502

- Response header `x-cid`: Request tracking identifier (string)
##### Response 504

- Response header `x-cid`: Request tracking identifier (string)

Catalogue row (api-reference-data/operations_catalog.csv): response codes `202;400;401;403;404;409;429;500;502;504`, has examples `False`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-PAY-pix-and-qr-codes`.

<!-- op: spec=api-specs/Instant_payments_-_QR_Code.yaml method=POST path=/v1/pix/qrcode/recurrence/cancel operationId=post-cancel-recurrence -->
### `POST /v1/pix/qrcode/recurrence/cancel` — Cancel recurrent compound QR Code [Beta]

- **operationId:** `post-cancel-recurrence`
- **Specification:** `api-specs/Instant_payments_-_QR_Code.yaml` (Instant payments - QR Code)
- **Server base URL(s):** `https://sandbox-cdn.pismolabs.io/qrcode`
- **Tags:** `Recurring payment`
- **Deprecated in specification:** no
- **Security requirement:** not declared

**Description (from the specification):**

> Cancel a recurring payment authorization (compound) QR Code and return the updated QR Code image, EMV (Europay Mastercard Visa) string, and recurrence payload. 
>
> **Notes:** 
>   * This endpoint takes an account token - an access token encoded with a Pismo account ID.
>   * This endpoint is **beta**, use in the dev-ext environment only.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Account token - token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a <b>401 Unauthorized</b> message.<br> |  |

#### Request body

Required: yes

> Cancel recurrent QR Code request

**Content type `application/json`** — schema: object (schema `qrcode.CancelRecurrenceQrCodeRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | string | yes | Pismo QR Code identifier of the recurrence to cancel. | maxLength: 36; example: "55d3992a-2f89-46fb-820a-958693bde84d" |
| `status` | string | yes | Cancellation status to apply to the recurrence QR Code. | enum: ["REMOVED_BY_PSP", "REMOVED_BY_PAYEE"]; example: "REMOVED_BY_PAYEE" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Cancel recurrence QR Code response | `application/json`: object (schema `qrcode.CancelRecurrenceQrCodeResponse`) |
| 400 | Bad request | `application/json`: object (schema `customer.Error`) |
| 401 | Invalid authorization | `application/json`: object (schema `customer.Error`) |
| 403 | Forbidden | `application/json`: object (schema `customer.Error`) |
| 404 | Not found | `application/json`: object (schema `customer.Error`) |
| 409 | Conflict | `application/json`: object (schema `customer.Error`) |
| 429 | Too many reqquests | `application/json`: object (schema `customer.Error`) |
| 500 | Internal Server Error | `application/json`: object (schema `customer.Error`) |
| 502 | Bad Gateway | `application/json`: object (schema `customer.Error`) |
| 504 | Gateway Timeout | `application/json`: object (schema `customer.Error`) |

##### Response 200

- Response header `x-cid`: Request tracking identifier (string)
**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | string (schema `qrcodeID`) | yes | Pismo QR Code identifier | example: "442e992a-2f89-46fb-820a-958693bde84d" |
| `external_id` | string (schema `externalID`) | yes | Client-generated record identifier for client tracking and monitoring.<br> | example: "my-external-id-9999-6474" |
| `emv` | string (schema `emv`) | no | Base 64 encoded discount QR Code payload. EMV = Europay, Mastercard and Visa, a global standard for credit and debit payment. The EMV might include details required for secure transactions such as cardholder informatipn, transaction amount, merchant information, and other relevant data.<br> | example: "00020101021226980014br.gov.bcb.pix2576api-h.developer.btgpactual.com/pc/p/v2/...***63040441" |
| `qrcode_image_b64` | string (schema `qrcode.imageb64`) | no | Base64 encoded QR Code | example: "dfkk7830o*&#)@#9FEE" |
| `jws_rec` | string (schema `jwsRec`) | no | Signed JWS payload, referring to the data of the recurrence.<br> | example: "eYqqqwq.heif.jk2w" |
| `access_token` | string (schema `accessToken`) | yes | QR Code access token generated and returned at creation.<br> | example: "1234567890" |
| `recurrence_id` | string (schema `recurrenceID`) | yes | Recurrence ID. Either this or the `recurrence` object is **REQUIRED**. | example: "RN219952X6X02505XXCONTRACTXXX" |

##### Response 400

- Response header `x-cid`: Request tracking identifier (string)
##### Response 401

- Response header `x-cid`: Request tracking identifier (string)
##### Response 403

- Response header `x-cid`: Request tracking identifier (string)
##### Response 404

- Response header `x-cid`: Request tracking identifier (string)
##### Response 409

- Response header `x-cid`: Request tracking identifier (string)
##### Response 429

- Response header `x-cid`: Request tracking identifier (string)
##### Response 500

- Response header `x-cid`: Request tracking identifier (string)
##### Response 502

- Response header `x-cid`: Request tracking identifier (string)
##### Response 504

- Response header `x-cid`: Request tracking identifier (string)

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;403;404;409;429;500;502;504`, has examples `False`, emits events `0`, deprecated `False`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/qrcode.PayeeRequest -->
### Schema `qrcode.PayeeRequest`

Pointer: `#/components/schemas/qrcode.PayeeRequest`. Type: object (schema `qrcode.PayeeRequest`).

> Payee information

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `address` | string (schema `address`) | yes | Location | maxLength: 200; example: "10 Downing Street, London  SW1A 2AB, UK" |
| `city` | string (schema `city`) | yes | City where payment occurred. | maxLength: 40; example: "Brasilia" |
| `key` | string (schema `pixKey`) | yes | Payee Pix key (should have Pismo account) | maxLength: 77; example: "chuck@steaks.com" |
| `state` | string (schema `state`) | yes | Brazilian state where payment will occur - two letter ISO 3166 code. | maxLength: 2; example: "DF" |
| `zip_code` | string (schema `zipCode`) | yes | Location postal code. | example: "8675309" |
| `category` | string (schema `merchantCategory`) | no | Receiver ISO 18245 merchant category code. | example: "5651" |

<!-- schema: #/components/schemas/qrcode.PayerRequest -->
### Schema `qrcode.PayerRequest`

Pointer: `#/components/schemas/qrcode.PayerRequest`. Type: object (schema `qrcode.PayerRequest`).

> Payer information

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `name` | string (schema `name`) | yes | Name | maxLength: 25; example: "Eva Destrukion" |
| `document_number` | string (schema `documentNumber`) | yes | Government ID, such as a CPF (Cadastro de Pessoas Fisicas - individual tax ID in Brazil) or a CNPJ (Cadastro Nacional de Pessoa Juridica - business tax ID in Brazil) number.<br> | maxLength: 15; example: "42761202686" |
| `type` | string (schema `legalType`) | yes | Person legal type:<br>  * `LEGAL_PERSON` - Person<br>  * `NATURAL_PERSON` - Company or organization<br> | enum: ["LEGAL_PERSON", "NATURAL_PERSON"]; example: "NATURAL_PERSON" |
| `trade_name` | string (schema `tradeName`) | no | Company name | example: "Acme Widgets" |

<!-- schema: #/components/schemas/qrcode.Additional -->
### Schema `qrcode.Additional`

Pointer: `#/components/schemas/qrcode.Additional`. Type: object (schema `qrcode.Additional`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `name` | string (schema `labelName`) | yes | Label name | maxLength: 140; example: "Purity of essence" |
| `value` | string (schema `value`) | yes | Value | maxLength: 140; example: "5.00" |

<!-- schema: #/components/schemas/qrcode.LocationDynamicQrcode -->
### Schema `qrcode.LocationDynamicQrcode`

Pointer: `#/components/schemas/qrcode.LocationDynamicQrcode`. Type: object (schema `qrcode.LocationDynamicQrcode`).

> Location URL information

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `url_jwk` | string (schema `urlJWK`) | no | PSP Receiver's URL that holds key pairs in JSON format. Should be hosted on the same site associated with the CERTQRC certificate. Use the format "JWK Set URL"  without the protocol (http/https).<br><br>The Central Bank uses this field and `url_payload` to register and validate the QR Code. This field **must** be passed if the PSP requires it.<br><br>The URL format is described in <a href="https://www.bcb.gov.br/content/estabilidadefinanceira/cedsfn/Manual_de_Seguranca_PIX.pdf" target="_blank">Manual de Segurança do PIX</a>.<br> |  |
| `url_payload` | string (schema `urlPayload`) | no | PSP Receiver's URL containing the dynamic QR Code's JSON Web Signature (JWS). Should not include the protocol (http/https).<br><br>The Central Bank uses this field and `url_jwk` to register and validate the QR Code. This field **must** be passed if the PSP requires it.<br><br>The URL format is described in <a href="https://www.bcb.gov.br/content/estabilidadefinanceira/pix/Regulamento_Pix/II_ManualdePadroesparaIniciacaodoPix.pdf" target="_blank">Manual de Padrões para Iniciação do PIX</a>.<br> | maxLength: 77; example: "example.com/pix/8b3da2f3-941-40d1-a91a-bd93113bd441" |
| `url_payload_rec` | string (schema `urlPayloadRec`) | no | PSP Receiver's URL containing the recurence QR Code's JSON Web Signature (JWS). Should not include the protocol (http/https).<br><br>The Central Bank uses this field and `url_jwk` to register and validate the QR Code. This field **must** be passed if the PSP requires it.<br><br>The URL format is described in <a href="https://www.bcb.gov.br/content/estabilidadefinanceira/pix/Regulamento_Pix/II_ManualdePadroesparaIniciacaodoPix.pdf" target="_blank">Manual de Padrões para Iniciação do PIX</a>.<br> | maxLength: 77; example: "example.com/rec/8b3da2f3-941-40d1-a91a-bd93113bd441" |

<!-- schema: #/components/schemas/qrcode.Recurrence -->
### Schema `qrcode.Recurrence`

Pointer: `#/components/schemas/qrcode.Recurrence`. Type: object (schema `qrcode.Recurrence`).

> Recurrence object. Either this or `recurrence_id` is **REQUIRED**.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `frequency_type` | string (schema `frequencyType`) | yes | Recurrence payment type | enum: ["WEEK", "MONTH", "QUARTER", "SEMESTER", "YEAR"]; example: "MONTH" |
| `first_payment_date` | string (schema `firstPaymentDate`) | yes | First charge/payment date. Format = yyyy-mm-dd | format: "datetime"; example: "2025-04-25" |
| `last_payment_date` | string (schema `lastPaymentDate`) | no | Last charge/payment date. Format = yyyy-mm-dd | format: "datetime"; example: "2026-06-10" |
| `amount` | number (schema `amount`) | no | Amount to be transferred. | example: 1050.44 |
| `min_payment_amount` | number (schema `minPaymentAmount`) | no | Payee-defined minimum payment amount for dynamic amount recurrences. | example: 10.09 |
| `debtor` | object (schema `debtor`) | yes |  |  |
| `contract_id` | string (schema `contractID`) | yes | Payee-created external ID for their reference.<br> | maxLength: 35; example: "5509-uroo-78944-9987" |
| `description` | string (schema `recurrenceDescription`) | no | Recurrence payment description | maxLength: 35; example: "Gym membership" |
| `allow_attempts_after_expiration` | boolean (schema `retry`) | no | Allow transaction retries on failure? Default is `false`. | default: false; example: true |
| `taxes` | object (schema `Taxes`) | no | Now only available on EXT environmentand just for direct parciapants. Tax information related to the transaction. |  |

<!-- schema: #/components/schemas/customer.Error -->
### Schema `customer.Error`

Pointer: `#/components/schemas/customer.Error`. Type: object (schema `customer.Error`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string | no | Error code. | example: "EPT0001" |
| `details` | object (schema `customer.DetailMessage`) | no |  |  |
| `message` | string | no | Error message. | example: "User not found" |

<!-- schema: #/components/schemas/charge -->
### Schema `charge`

Pointer: `#/components/schemas/charge`. Type: object (schema `charge`).

> Charge information

Composition: includes the fields of schema `qrcode.Charge` (allOf).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `due_date` | string (schema `dueDate`) | yes | Payment due date. Format = yyyy-mm-dd | format: "date" |
| `validity_after_expiration_day` | integer (schema `validityAfterExpirationDay`) | no | How many days QR Code is valid after expiration |  |
| `discount_type` | string (schema `discountType`) | no | Discount value type.<br> | enum: ["FIXED_VALUE_UNTIL_THE_DATES_INFORMED", "PERCENTAGE_DATE_REPORTED", "AMOUNT_PER_CALENDAR_DAY_ADVANCE", "AMOUNT_ADVANCE_WORKING_DAY", "PERCENTAGE_ADVANCE_CURRENT_DAY", "PERCENTAGE_ADVANCE_WORKING_DAY"]; example: "FIXED_VALUE_UNTIL_THE_DATES_INFORMED" |
| `discount_value` | number (schema `discountValue`) | no | Discount value to be applied when `discount_type` is not `FIXED_VALUE_UNTIL_THE_DATES_INFORMED` or `PERCENTAGE_DATE_REPORTED`.<br> | example: 99 |
| `discount_fixed_dates` | array of object (schema `qrcode.DiscountDate`) (schema `discountFixedDates`) | no | Maximum dates for payment to apply the discount (fixed value). Use this attribute for `discount_type` = `FIXED_VALUE_UNTIL_THE_DATES_INFORMED`<br> |  |
| `fine_type` | string (schema `fineType`) | no | Fine type. | enum: ["FIXED_VALUE", "PERCENT"]; example: "FIXED_VALUE" |
| `fine_value` | number (schema `fineValue`) | no | Fine value. | example: 45.67 |
| `fine_final_amount` | number (schema `fineFinalAmount`) | no | Fine total (calculated). | example: 99.87 |
| `interest_type` | string (schema `interestType`) | no | Interest type to calculate.<br> | enum: ["VALUE_CALENDAR_DAYS", "PERCENTAGE_PER_DAY_CALENDAR_DAYS", "PERCENTAGE_PER_MONTH_CALENDAR_DAYS", "PERCENTAGE_PER_YEAR_CALENDAR_DAYS", "VALUE_WORKING_DAYS", "PERCENTAGE_PER_DAY_WORKING_DAYS", "PERCENTAGE_PER_MONTH_WORKING_DAYS", "PERCENTAGE_PER_YEAR_WORKING_DAYS"]; example: "VALUE_WORKING_DAYS" |
| `interest_value` | number (schema `interestValue`) | no | Value to be applied. | example: 34.09 |
| `interest_final_amount` | number (schema `interestFinalAmount`) | no | Interest total (calculated). | example: 67.89 |
| `settlement_type` | string (schema `settlementType`) | no | Settlement type. | enum: ["FIXED_VALUE", "PERCENT"]; example: "FIXED_VALUE" |
| `settlement_value` | number (schema `settlementValue`) | no | Settlement value (depends on `settlement_type`). | example: 453.98 |
| `settlement_final_amount` | number (schema `settlementFinalAmount`) | no | Total settlement (calculated as fixed or percentage). | example: 876.34 |
| `final_amount` | number (schema `finalAmount`) | no | Total (initial - `settlement_final_amount` - `discount_final_amount` + `interest_final_amount` + `fine_final_amount`)<br> | example: 10 |

<!-- schema: #/components/schemas/qrcode.LocationStatic -->
### Schema `qrcode.LocationStatic`

Pointer: `#/components/schemas/qrcode.LocationStatic`. Type: object (schema `qrcode.LocationStatic`).

> Location URL information

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `url_jwk` | string (schema `urlJWK`) | no | PSP Receiver's URL that holds key pairs in JSON format. Should be hosted on the same site associated with the CERTQRC certificate. Use the format "JWK Set URL"  without the protocol (http/https).<br><br>The Central Bank uses this field and `url_payload` to register and validate the QR Code. This field **must** be passed if the PSP requires it.<br><br>The URL format is described in <a href="https://www.bcb.gov.br/content/estabilidadefinanceira/cedsfn/Manual_de_Seguranca_PIX.pdf" target="_blank">Manual de Segurança do PIX</a>.<br> |  |
| `url_payload_rec` | string (schema `urlPayloadRec`) | no | PSP Receiver's URL containing the recurence QR Code's JSON Web Signature (JWS). Should not include the protocol (http/https).<br><br>The Central Bank uses this field and `url_jwk` to register and validate the QR Code. This field **must** be passed if the PSP requires it.<br><br>The URL format is described in <a href="https://www.bcb.gov.br/content/estabilidadefinanceira/pix/Regulamento_Pix/II_ManualdePadroesparaIniciacaodoPix.pdf" target="_blank">Manual de Padrões para Iniciação do PIX</a>.<br> | maxLength: 77; example: "example.com/rec/8b3da2f3-941-40d1-a91a-bd93113bd441" |

<!-- schema: #/components/schemas/qrcode.RecurrenceQrcodePayeeRequest -->
### Schema `qrcode.RecurrenceQrcodePayeeRequest`

Pointer: `#/components/schemas/qrcode.RecurrenceQrcodePayeeRequest`. Type: object (schema `qrcode.RecurrenceQrcodePayeeRequest`).

> Recurence QR Code payee request

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `category` | string (schema `merchantCategory`) | no | Receiver ISO 18245 merchant category code. | example: "5651" |
| `city` | string (schema `city`) | yes | City where payment occurred. | maxLength: 40; example: "Brasilia" |
| `state` | string (schema `state`) | yes | Brazilian state where payment will occur - two letter ISO 3166 code. | maxLength: 2; example: "DF" |
| `zip_code` | string (schema `zipCode`) | yes | Location postal code. | example: "8675309" |

<!-- schema: #/components/schemas/qrcode.LocationQrcodeComposite -->
### Schema `qrcode.LocationQrcodeComposite`

Pointer: `#/components/schemas/qrcode.LocationQrcodeComposite`. Type: object (schema `qrcode.LocationQrcodeComposite`).

> Location URL information

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `url_jwk` | string (schema `urlJWK`) | no | PSP Receiver's URL that holds key pairs in JSON format. Should be hosted on the same site associated with the CERTQRC certificate. Use the format "JWK Set URL"  without the protocol (http/https).<br><br>The Central Bank uses this field and `url_payload` to register and validate the QR Code. This field **must** be passed if the PSP requires it.<br><br>The URL format is described in <a href="https://www.bcb.gov.br/content/estabilidadefinanceira/cedsfn/Manual_de_Seguranca_PIX.pdf" target="_blank">Manual de Segurança do PIX</a>.<br> |  |
| `url_payload_rec` | string (schema `urlPayloadRec`) | no | PSP Receiver's URL containing the recurence QR Code's JSON Web Signature (JWS). Should not include the protocol (http/https).<br><br>The Central Bank uses this field and `url_jwk` to register and validate the QR Code. This field **must** be passed if the PSP requires it.<br><br>The URL format is described in <a href="https://www.bcb.gov.br/content/estabilidadefinanceira/pix/Regulamento_Pix/II_ManualdePadroesparaIniciacaodoPix.pdf" target="_blank">Manual de Padrões para Iniciação do PIX</a>.<br> | maxLength: 77; example: "example.com/rec/8b3da2f3-941-40d1-a91a-bd93113bd441" |

<!-- schema: #/components/schemas/debtor -->
### Schema `debtor`

Pointer: `#/components/schemas/debtor`. Type: object (schema `debtor`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `document_number` | string (schema `documentNumber`) | yes | Government ID, such as a CPF (Cadastro de Pessoas Fisicas - individual tax ID in Brazil) or a CNPJ (Cadastro Nacional de Pessoa Juridica - business tax ID in Brazil) number.<br> | maxLength: 15; example: "42761202686" |
| `document_type` | string (schema `legalType`) | yes | Person legal type:<br>  * `LEGAL_PERSON` - Person<br>  * `NATURAL_PERSON` - Company or organization<br> | enum: ["LEGAL_PERSON", "NATURAL_PERSON"]; example: "NATURAL_PERSON" |
| `name` | string (schema `name`) | yes | Name | maxLength: 25; example: "Eva Destrukion" |

<!-- schema: #/components/schemas/Taxes -->
### Schema `Taxes`

Pointer: `#/components/schemas/Taxes`. Type: object (schema `Taxes`).

> Now only available on EXT environmentand just for direct parciapants. Tax information related to the transaction.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `tax_identifier` | string (schema `TaxIdentifier`) | no | Tax identifier, referring to the NFe, NFSe or aggregating tax document. The value entered must correspond to the tax document used for calculating the IBS and CBS taxes associated with the transaction. | maxLength: 50; example: "IS0435879820240605bcdb1fhn43a" |
| `records` | array of object (schema `Records`) | no | Group of information on tax record types. It is mandatory to pass 2 objects, at least one with CBS tax type and at least one with IBS tax type."; |  |

<!-- schema: #/components/schemas/customer.DetailMessage -->
### Schema `customer.DetailMessage`

Pointer: `#/components/schemas/customer.DetailMessage`. Type: object (schema `customer.DetailMessage`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `external` | array of object (schema `customer.ExternalMessage`) | no |  |  |
| `parameters` | array of object (schema `customer.ParameterMessage`) | no |  |  |
| `payload` | array of object (schema `customer.PayloadMessage`) | no |  |  |

<!-- schema: #/components/schemas/qrcode.DiscountDate -->
### Schema `qrcode.DiscountDate`

Pointer: `#/components/schemas/qrcode.DiscountDate`. Type: object (schema `qrcode.DiscountDate`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `date` | string (schema `discountDate`) | no | Last date discount can be applied. Format = yyyy-mm-dd. | format: "date"; example: "2024-01-12" |
| `value` | number (schema `discountValue2`) | no | Discount values. | example: 86753.09 |

<!-- schema: #/components/schemas/Records -->
### Schema `Records`

Pointer: `#/components/schemas/Records`. Type: object (schema `Records`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `tax_type` | string (schema `TaxType`) | no | Tax type. 1- IBS (Goods and Services Tax \| 2- CBS Contribution on Goods and Services | enum: ["CBS", "IBS"]; example: "IBS" |
| `amount` | number (schema `TaxAmount`) | no | Tax amount. Must be greater than zero. | minimum: 0; example: 1050.44 |

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
| `field` | string | yes | Detailed field name | example: "query_parameter" |
| `message` | string | yes | Error's message. | example: "Generic error" |

<!-- schema: #/components/schemas/customer.PayloadMessage -->
### Schema `customer.PayloadMessage`

Pointer: `#/components/schemas/customer.PayloadMessage`. Type: object (schema `customer.PayloadMessage`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `field` | string | yes | Detailed field name. | example: "Entity.field" |
| `message` | string | yes | Error message. | example: "Generic error" |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Instant_payments_-_QR_Code.yaml` | tag `Recurring payment`: POST /v1/pix/qrcode/cob/recurrence, POST /v1/pix/qrcode/cobv/recurrence, POST /v1/pix/qrcode/static/recurrence, POST /v1/pix/qrcode/recurrence, POST /v1/pix/qrcode/recurrence/cancel | https://github.com/PismoDevEx/pismo-api-specs | `92acd63f86546e9b…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-PAY-pix-and-qr-codes` — Pix and QR Codes
- `KU-PAY-pix-automatic` — Pix Automatic
