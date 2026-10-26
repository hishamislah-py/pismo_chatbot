---
ku_id: KU-API-card-issuing-disputes--disputes-part-01
title: 'API reference: Card issuing - Disputes — Disputes (part 1 of 2)'
category: api_reference
ku_type: api_reference
lifecycle: current
sources:
- path: api-specs/Card_issuing_-_Disputes.yaml
  sha256: 5c1d5513e1f3a4d1daa4d6bd654885c4edfeb5135eaa60b50f1a74d62031baad
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
- post-v1-networkauthorization-disputes
- get-v1-disputes
- get-v1-disputes-disputeId
- put-v1-disputes-disputeId
- post-v1-disputes-disputeId-event
related_kus:
- KU-AUTH-account-and-external-id-tokens
- KU-CARD-card-issuing-basics
- KU-CARD-disputes-overview
- KU-CARD-disputes-state-machine
- KU-CARD-visa-colloboration-questionaire-part-01
- KU-CARD-visa-dispute-use-case
- KU-CC-disputes
- KU-EVT-catalogue-disputes
- KU-EVT-disputes-endpoint-generated-events
specification_version: 1.0.0
---

# API reference: Card issuing - Disputes — Disputes (part 1 of 2)

**KU ID:** `KU-API-card-issuing-disputes--disputes-part-01` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 5 operation(s) tagged `Disputes` in `api-specs/Card_issuing_-_Disputes.yaml` (“Card issuing - Disputes”, version `1.0.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Endpoints to create and manage disputes

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `POST /v1/networkauthorization-disputes` | `post-v1-networkauthorization-disputes` | Create dispute | no |
| `GET /v1/disputes` | `get-v1-disputes` | List disputes | no |
| `GET /v1/disputes/{disputeId}` | `get-v1-disputes-disputeId` | Get dispute | no |
| `PUT /v1/disputes/{disputeId}` | `put-v1-disputes-disputeId` | Update dispute | no |
| `POST /v1/disputes/{disputeId}/event` | `post-v1-disputes-disputeId-event` | Update dispute status | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"} — Account access token. Tokens can expire quickly, which can result in an "Unauthorized" error.

## Operation contracts

<!-- op: spec=api-specs/Card_issuing_-_Disputes.yaml method=POST path=/v1/networkauthorization-disputes operationId=post-v1-networkauthorization-disputes -->
### `POST /v1/networkauthorization-disputes` — Create dispute

- **operationId:** `post-v1-networkauthorization-disputes`
- **Specification:** `api-specs/Card_issuing_-_Disputes.yaml` (Card issuing - Disputes)
- **Server base URL(s):** `https://sandbox.pismolabs.io/disputes`
- **Tags:** `Disputes`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Create a dispute for a Zero or Full balance program. You can create a dispute for a transaction made with a Pismo-issued card (Full balance) or with another card (Zero balance). You need to pass different parameters depending on which one as noted in the parameter descriptions.
>
> Disputes are initially created with a `PENDING` status. After you've uploaded all your supporting forms and evidence files, call [Update dispute status](https://developers.pismo.io/pismo-docs/reference/post-v1-disputes-disputeid-event) and use the `OPEN` event to change the status to `OPENED` and begin the dispute process with the network.
>
> For more information on events and statuses, refer to the <a href="https://developers.pismo.io/pismo-docs/docs/disputes-state-machine">Disputes state machine</a>.
>
> This endpoint generates a <a href="https://developers.pismo.io/events/docs/disputes-dispute-installment-creation-1">Dispute installment created</a> event.
>
> **Note:** For Zero balance customers, this endpoint takes an account token - an access token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a <b>401 Unauthorized</b> message.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Account token - an access token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a <b>401 Unauthorized</b> message. | example: "Bearer eyJhbGci...IUzUx" |

#### Request body

Required: yes

> Dispute data

**Content type `application/json`** — schema: object (schema `DisputeRequestNetwork`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `modality` | number (schema `reasonCode`) | yes | Each card network, such as Visa or Mastercard, defines and maintains their own unique set of reason codes, which banks that issue credit and debit cards under their brands apply to disputes. Here's a reason code [quick reference](https://www.chargebackgurus.com/blog/a-definitive-guide-to-chargeback-reason-codes-by-card-network#chargback-reason-code-quick-reference-guide) for the major credit card networks.<br><br>For Visa, this would be either `10` (fraud - card present), `11` (authorization), `12` (processing error), or `13` (consumer dispute).<br><br>For more infomation, refer to the [Visa](https://usa.visa.com/dam/VCOM/global/support-legal/documents/chargeback-management-guidelines-for-visa-merchants-vbs-19-may-16-%20v2.pdf) or [Mastercard](https://www.mastercard.us/content/dam/public/mastercardcom/na/global-site/documents/chargeback-guide.pdf) chargeback quides.<br><br>For example - `4853` (Mastercard - cardholder dispute), `12` (Visa - processing error) or `72` (ELO - denied authorization)<br> | example: 4853 |
| `disputed_amount` | number (schema `DisputedAmount`) | yes | Disputed amount. | example: 10 |
| `is_partial` | boolean (schema `IsPartial`) | yes | Is partial amount chargeback? Default is `false`. | default: false; example: false |
| `network_brand_type` | string | yes | Network brand | enum: ["Visa", "Mastercard", "Elo"]; example: "Visa" |
| `authorization_id` | number | no | Related authorization ID. **REQUIRED** when disputed in a Full balance program or the network brand is Elo. | example: 123 |
| `comment` | string (schema `Comment`) | no | Client custom dispute comment.<br><br>**REQUIRED** for Visa partial dispute to explain why partial.<br> | maxLength: 5000; nullable: true; example: "Custom comment" |
| `protocol` | string (schema `Protocol`) | no | Client custom protocol ID. This is primarily for you to internally identify a request. If not provided, Pismo creates a CID (correlation ID) field for this purpose.<br> | maxLength: 500; example: "20251128111532456" |
| `metadata` | object (schema `Metadata`) | no | Can be used for caller's dispute information and process. Objects and name-value pairs.<br><br> **Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis#metadata).<br> | example: {"field1": "value", "field2": "value"} |
| `first_installment_amount` | number | no | Amount to be disputed on first Installment chargeback. | example: 5 |
| `arn` | string | no | Acquirer reference number. **REQUIRED** when disputed in a Zero balance program. | maxLength: 255; example: "0000000000539598" |
| `transaction_date` | string | no | **REQUIRED** when disputed in a Zero balance program. Format = yyyy-mm-dd | format: "Date" |
| `dispute_due_to` | string (schema `disputeDueTo`) | no | **REQUIRED** when dispute is open to Visa Collaboration (Reason code 12 and 13 and Visa network brand). Collaboration is the new name for Visa's old chargeback process, where each party has several chances to investigate and submit evidence in order to determine whether a chargeback is legitimate.<br><br><br>`NR` = Merchandise/services not receive<br><br>`CR` = Cancelled recurring transaction<br><br>`ND` = Not as described<br><br>`DM` = Damaged or defective merchandise<br><br>`Q` = Quality<br><br>`CM` = Counterfeit merchandise<br><br>`M` = Misrepresentation<br><br>`CN` = Credit not processed<br><br>`CS` = Cancelled merchandise/services<br><br>`OC` = Original credit not accepted<br><br>`CL` = Non-receipt of cash<br><br>`TC` = Terms of contract (virtual account)<br><br>`D` = Duplicate<br><br>`IAN` = Incorrect account number<br><br>`IA` = Incorrect amount<br><br>`IC` = Incorrect currency<br><br>`IT` = Incorrect transaction code<br><br>`ID` = Invalid data<br><br>`LP` = Late presentment<br><br>`P` = Paid by other means<br><br><br>For VISA, you need to fill out the `collaborationQuestionnaire` form object in the [Create dispute form](ref:post-v1-disputes-disputeid-forms) endpoint.<br> | enum: ["NR", "CR", "ND", "DM", "Q", "CM", "M", "CN", "CS", "OC", "CL", "TC", "D", "IAN", "IA", "IC", "IT", "ID", "LP", "P"]; example: "NR" |
| `currency_code` | string | no | Dispute ISO4217 currency code. Default is 986 - Brazilian real.<br><br>This is **REQUIRED** if you are creating a dispute in a Zero balance program.<br> | example: "986" |
| `fraud_type` | string | no | Fraud type:<br><br>`0` - Lost<br><br>`1` - Stolen<br><br>`2` - Card not received as issued (NRI)<br><br>`3` - Fraudulent application (cardholder never applied for the card)<br><br>`4` - Issuer-reported counterfeit<br><br>`5` - Miscellaneous<br><br>`6` - Fraudulent use of account number<br><br>`A` = Incorrect processing<br><br>`B` = Account or credentials takeover<br><br>`C` = Merchant misrepresentation<br><br>`D` = Manipulation of account holder<br><br> | enum: ["0", "1", "2", "3", "4", "5", "6", "A", "B", "C", "D"] |
| `document_indicator` | boolean | no | Document submission indicator (ELO). Default is `true`. | default: true; example: true |
| `airport_tax` | boolean | no | For ELO network, should dispute for airport tax be created? Default is `true` for ELO. | example: false |
| `airport_tax_partial` | boolean | no | For ELO network, should airport tax be partially disputed? Default is `false`. | default: false; example: false |
| `airport_tax_amount` | number | no | Airport tax amount to be disputed. **REQUIRED** if `airport_tax_partial` is `true`. | example: 25 |
| `card_hash` | string | no | Card number hash. | example: "XYZdd887tt" |
| `authorization_code` | string (schema `AuthorizationCode`) | no | Authorization code | example: "F0JR9H" |
| `transaction_amount` | number (schema `TransactionAmount`) | no | Transaction amount | example: 86753.09 |

Example `Create a dispute over a multiple Installment authorization with success`:

```json
{
  "authorization_id": 123,
  "modality": 123,
  "comment": "Custom comment",
  "protocol": "20190321L123456",
  "disputed_amount": 10,
  "metadata": {},
  "is_partial": true,
  "first_installment_amount": 5,
  "arn": "0000000000539598",
  "network_brand_type": "Mastercard",
  "currency_code": "986",
  "fraud_type": "1"
}
```

Example `Create a dispute without network authorization`:

```json
{
  "modality": 123,
  "comment": "Custom comment",
  "protocol": "20190321L123456",
  "disputed_amount": 10,
  "metadata": {},
  "is_partial": true,
  "first_installment_amount": 5,
  "arn": "0000000000539598",
  "network_brand_type": "Mastercard",
  "transaction_date": "yyyy-MM-dd",
  "currency_code": "986",
  "fraud_type": "2"
}
```

Example `Create a dispute in Visa Collaboration flux`:

```json
{
  "authorization_id": 123,
  "modality": 13,
  "comment": "Custom comment",
  "protocol": "20190321L123456",
  "disputed_amount": 10,
  "metadata": {},
  "is_network": true,
  "is_partial": false,
  "network_brand_type": "Visa",
  "dispute_due_to": "NR",
  "currency_code": "986",
  "fraud_type": "2"
}
```

Example `Create a dispute in Elo with card invalid`:

```json
{
  "modality": 77,
  "disputed_amount": 86753.09,
  "comment": "Custom comment",
  "protocol": "c20190321L123456",
  "is_network": true,
  "is_partial": false,
  "network_brand_type": "Elo",
  "arn": "0000000000539598",
  "transaction_date": "2023-09-05",
  "transaction_amount": 210,
  "authorization_code": "123456",
  "card_hash": "XYZ"
}
```

**Content type `application/xml`** — schema: object

_No fields declared in the schema._

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `DisputeNetworkResponse`) |
| 400 | Bad Request |  |
| 401 | Unauthorized. Invalid or missing access token. |  |
| 422 | Unprocessable entity |  |
| 500 | Internal server error |  |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | number (schema `DisputeID`) | no | Dispute ID | example: 48670 |
| `authorization_id` | number | no | Network authorization ID | example: 1001 |
| `account_id` | number (schema `AccountID`) | no | Pismo account ID | example: 577830 |
| `airport_tax` | boolean | no | Should dispute for airport tax be created? Default is `true` for the ELO card network. | example: false |
| `airport_tax_partial` | boolean | no | Should airport tax be partially disputed? Default is `false`. | default: false; example: false |
| `airport_tax_amount` | number | no | Airport tax amount to be disputed. **REQUIRED** if `airport_tax_partial` is `true`. | example: 25 |
| `comment` | string (schema `Comment`) | no | Client custom dispute comment.<br><br>**REQUIRED** for Visa partial dispute to explain why partial.<br> | maxLength: 5000; nullable: true; example: "Custom comment" |
| `dispute_installment_id` | integer (schema `DisputeInstallmentId`) | no | Dispute installment ID. | example: 8675309 |
| `reason` | object | no | Pismo's reason object. |  |
| `reason.dispute_reason_id` | number | no | Reason ID. | example: 1 |
| `reason.description` | string | no | Reason description. | example: "Fraudulent transaction - no cardholder authorization" |
| `reason.code` | number (schema `reasonCode`) | no | Each card network, such as Visa or Mastercard, defines and maintains their own unique set of reason codes, which banks that issue credit and debit cards under their brands apply to disputes. Here's a reason code [quick reference](https://www.chargebackgurus.com/blog/a-definitive-guide-to-chargeback-reason-codes-by-card-network#chargback-reason-code-quick-reference-guide) for the major credit card networks.<br><br>For Visa, this would be either `10` (fraud - card present), `11` (authorization), `12` (processing error), or `13` (consumer dispute).<br><br>For more infomation, refer to the [Visa](https://usa.visa.com/dam/VCOM/global/support-legal/documents/chargeback-management-guidelines-for-visa-merchants-vbs-19-may-16-%20v2.pdf) or [Mastercard](https://www.mastercard.us/content/dam/public/mastercardcom/na/global-site/documents/chargeback-guide.pdf) chargeback quides.<br><br>For example - `4853` (Mastercard - cardholder dispute), `12` (Visa - processing error) or `72` (ELO - denied authorization)<br> | example: 4853 |
| `reason.initial_status` | string | no |  | example: "CRIADO" |
| `reason.initial_status_pci` | string | no |  | example: "EFETUADO" |
| `reason.is_fraud` | boolean | no | Is fraud? |  |

200 Example `Dispute created`:

```json
{
  "id": 42,
  "authorization_id": 1001,
  "account_id": 1000101,
  "comment": "Dispute comment",
  "reason": {
    "dispute_reason_id": 1,
    "description": "Fraudulent transaction - no cardholder authorization",
    "code": 4837,
    "initial_status": "CRIADO",
    "initial_status_pci": "EFETUADO",
    "is_fraud": true
  }
}
```

200 Example `Dispute created without authorization`:

```json
{
  "id": 1,
  "account_id": 4,
  "comment": "Simulação para Abertuda de Disputa - Sem Authotization",
  "reason": {
    "dispute_reason_id": 10,
    "description": "Fraudulent transaction - no cardholder authorization",
    "code": 4837,
    "initial_status": "CRIADO",
    "initial_status_pci": "EFETUADO",
    "is_fraud": false
  }
}
```


#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `disputes-dispute-installment-creation-1` | https://developers.pismo.io/events/docs/disputes-dispute-installment-creation-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;422;500`, has examples `True`, emits events `1`, deprecated `False`.

Guides that link to this operation: `KU-AUTH-account-and-external-id-tokens`, `KU-CARD-card-issuing-basics`, `KU-CARD-disputes-overview`, `KU-CARD-visa-colloboration-questionaire-part-01`, `KU-CARD-visa-dispute-use-case`, `KU-CC-disputes`, `KU-EVT-disputes-endpoint-generated-events`.

<!-- op: spec=api-specs/Card_issuing_-_Disputes.yaml method=GET path=/v1/disputes operationId=get-v1-disputes -->
### `GET /v1/disputes` — List disputes

- **operationId:** `get-v1-disputes`
- **Specification:** `api-specs/Card_issuing_-_Disputes.yaml` (Card issuing - Disputes)
- **Server base URL(s):** `https://sandbox.pismolabs.io/disputes`
- **Tags:** `Disputes`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Get disputes with paging and filter options.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Account token - an access token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a <b>401 Unauthorized</b> message. | example: "Bearer eyJhbGci...IUzUx" |
| `beginDate` | query | no | string | Beginning date filter, format= yyyy-mm-dd | example: "2020-01-31" |
| `endDate` | query | no | string | End date filter, format= yyyy-mm-dd | example: "2020-01-31" |
| `page` | query | no | integer | Page to return. | default: 1; minimum: 1; example: 2 |
| `perPage` | query | no | integer | Number of items per page | default: 30; minimum: 1; example: 20 |
| `accountId` | query | no | integer | Account ID filter | minimum: 1; example: 123 |
| `isNetwork` | query | no | boolean | Return only network disputes? Default is `false`. | example: true |
| `isDisputeMigrated` | query | no | boolean | Return only migrated disputes? Default is `false`. | default: false; example: true |
| `isDisputeInvalidTransaction` | query | no | boolean | Return only disputes with invalid transaction? Default is `false`. | default: false; example: true |
| `group` | query | no | string | Status group filter, i.e., `OPEN`. | enum: ["OPEN", "APPROVED", "DENIED", "CARDNETWORK_CHARGEBACK", "ANALYSING", "CARDNETWORK_SECOND_PRESENTMENT", "FAILED", "CARDNETWORK_PREARBITRATION", "RESEND", "LOSS", "WON", "REJECTED", "FAILED_PROCESSED"]; example: "CARDNETWORK_CHARGEBACK"; example: "WON" |
| `status` | query | no | string | Dispute status filter | enum: ["OPENED", "PENDING", "CANCELED", "FAILED", "CHARGEBACK_REJECTED", "CHARGEBACK_CREATED", "CHARGEBACK_ACCEPTED", "CHARGEBACK_CLOSED", "SECOND_PRESENTMENT", "PRE_ARBITRATION_OPENED", "PRE_ARBITRATION_ACCEPTED", "PRE_ARBITRATION_DECLINED", "PRE_ARBITRATION_RECALL", "PRE_ARB_ALLOCATION_OPENED", "FAILED_PRE_ARBITRATION", "PRE_ARB_ALLOCATION_ACCEPTED", "PRE_ARB_ALLOCATION_DECLINED", "PRE_ARB_ALLOCATION_RECALLED", "FAILED_DECLINE_PRE_ARB", "FAILED_ACCEPT_PRE_ARB", "FAILED_ON_CLOSE", "EXPIRED", "ISSUER_LOSS", "MIGRATION", "FAILED_MIGRATION"]; example: "OPENED"; example: "OPENED" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: array of object (schema `FullDisputeResponse`) |
| 400 | Bad Request |  |
| 401 | Unauthorized. Invalid or missing access token. |  |
| 500 | Internal server error |  |

##### Response 200

**200 `application/json` body fields:**

_No fields declared in the schema._

200 Example `List Disputes`:

```json
[
  {
    "id": 1,
    "org_id": "123456789",
    "account_id": 30605,
    "authorization_id": 4352243,
    "disputed_amount": 10.5,
    "comment": "Some comment",
    "dispute_reason": 4855,
    "modality": 4855,
    "dispute_status": "PENDING",
    "timeline": "{ \"data\": \"test\"}",
    "protocol": "20190321L123456",
    "created_at": "2021-02-21",
    "updated_at": "2021-02-22",
    "created_at_utc": "2021-02-21T22:51:43.000000000Z",
    "updated_at_utc": "2021-02-25T01:43:06.000000000Z",
    "is_network": true,
    "is_dispute_migrated": false,
    "reversal_id": 10042,
    "network_return_reason_code": "2833",
    "network_brand_type": "Mastercard",
    "transaction_date": "2021-02-21",
    "stop_automated_installment": true,
    "card_hash": "XYZ",
    "authorization_code": "123456",
    "is_dispute_invalid_transaction": true,
    "transaction_amount": 10.5
  }
]
```


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;500`, has examples `True`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Card_issuing_-_Disputes.yaml method=GET path=/v1/disputes/{disputeId} operationId=get-v1-disputes-disputeId -->
### `GET /v1/disputes/{disputeId}` — Get dispute

- **operationId:** `get-v1-disputes-disputeId`
- **Specification:** `api-specs/Card_issuing_-_Disputes.yaml` (Card issuing - Disputes)
- **Server base URL(s):** `https://sandbox.pismolabs.io/disputes`
- **Tags:** `Disputes`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Get information about a specific dispute given its ID in the path.
>
> You can use the [List disputes](ref:get-v1-disputes) endpoint to get dispute IDs.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `disputeId` | path | yes | number | Dispute ID |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object |
| 201 | Created |  |
| 400 | Bad Request |  |
| 401 | Unauthorized. Invalid or missing access token. |  |
| 404 | Not found |  |
| 500 | Internal server error |  |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | number (schema `DisputeID`) | no | Dispute ID | example: 48670 |
| `org_id` | string (schema `OrgID`) | no | Organization/tenant ID. | example: "TN-34778262-f4f0-464d-b4c6-a14exxxxxxxx" |
| `account_id` | number (schema `AccountID`) | no | Pismo account ID | example: 577830 |
| `authorization_id` | integer | no | Authorization ID. | example: 4352243 |
| `disputed_amount` | number (schema `DisputedAmount`) | no | Disputed amount. | example: 10 |
| `comment` | string (schema `Comment`) | no | Client custom dispute comment.<br><br>**REQUIRED** for Visa partial dispute to explain why partial.<br> | maxLength: 5000; nullable: true; example: "Custom comment" |
| `airport_tax` | boolean | no | For ELO card network, should dispute for airport tax be created? Default is `true` for ELO. | example: false |
| `airport_tax_partial` | boolean | no | For ELO card network, should airport tax be partially disputed? Default is `false`. | default: false; example: false |
| `airport_tax_amount` | number | no | Airport tax amount to be disputed. **REQUIRED** if `airport_tax_partial` is `true`. | example: 25 |
| `dispute_reason` | number (schema `reasonCode`) | no | Each card network, such as Visa or Mastercard, defines and maintains their own unique set of reason codes, which banks that issue credit and debit cards under their brands apply to disputes. Here's a reason code [quick reference](https://www.chargebackgurus.com/blog/a-definitive-guide-to-chargeback-reason-codes-by-card-network#chargback-reason-code-quick-reference-guide) for the major credit card networks.<br><br>For Visa, this would be either `10` (fraud - card present), `11` (authorization), `12` (processing error), or `13` (consumer dispute).<br><br>For more infomation, refer to the [Visa](https://usa.visa.com/dam/VCOM/global/support-legal/documents/chargeback-management-guidelines-for-visa-merchants-vbs-19-may-16-%20v2.pdf) or [Mastercard](https://www.mastercard.us/content/dam/public/mastercardcom/na/global-site/documents/chargeback-guide.pdf) chargeback quides.<br><br>For example - `4853` (Mastercard - cardholder dispute), `12` (Visa - processing error) or `72` (ELO - denied authorization)<br> | example: 4853 |
| `modality` | number | no | Dispute *modality* - legacy term for reason code to file the dispute. | example: 4855 |
| `dispute_status` | string (schema `DisputeStatus`) | no | Dispute status enums.<br> | enum: ["OPENED", "PENDING", "CANCELED", "FAILED", "CHARGEBACK_REJECTED", "CHARGEBACK_CREATED", "CHARGEBACK_ACCEPTED", "CHARGEBACK_CLOSED", "SECOND_PRESENTMENT", "PRE_ARBITRATION_OPENED", "PRE_ARBITRATION_ACCEPTED", "PRE_ARBITRATION_DECLINED", "PRE_ARBITRATION_RECALL", "PRE_ARB_ALLOCATION_OPENED", "FAILED_PRE_ARBITRATION", "PRE_ARB_ALLOCATION_ACCEPTED", "PRE_ARB_ALLOCATION_DECLINED", "PRE_ARB_ALLOCATION_RECALLED", "FAILED_DECLINE_PRE_ARB", "FAILED_ACCEPT_PRE_ARB", "FAILED_ON_CLOSE", "EXPIRED", "ISSUER_LOSS", "MIGRATION", "FAILED_MIGRATION"]; example: "PENDING" |
| `dispute_group_status` | string (schema `DisputeGroupStatus`) | no | Group status enums<br> | enum: ["OPEN", "APPROVED", "DENIED", "CARDNETWORK_CHARGEBACK", "ANALYSING", "CARDNETWORK_SECOND_PRESENTMENT", "FAILED", "CARDNETWORK_PREARBITRATION", "RESEND", "LOSS", "WON", "REJECTED", "FAILED_PROCESSED"]; example: "OPEN" |
| `timeline` | string | no | Client custom timeline information. | example: "{ \\"data\\": \\"test\\"}" |
| `protocol` | string (schema `Protocol`) | no | Client custom protocol ID. This is primarily for you to internally identify a request. If not provided, Pismo creates a CID (correlation ID) field for this purpose.<br> | maxLength: 500; example: "20251128111532456" |
| `metadata` | object (schema `Metadata`) | no | Can be used for caller's dispute information and process. Objects and name-value pairs.<br><br> **Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis#metadata).<br> | example: {"field1": "value", "field2": "value"} |
| `created_at` | string (schema `CreatedAt`) | no | Created at datetime, format = yyyy-mm-dd hh:mm:ss" | example: "2024-10-18 11:21:45" |
| `updated_at` | string (schema `UpdatedAt2`) | no | Dispute last updated date, format = yyyy-mm-dd. | format: "date"; example: "2021-02-22" |
| `created_at_utc` | string (schema `CreatedAtUTC`) | no | Dispute created in UTC date/time. | format: "date-time"; example: "2021-02-21T22:51:43.000000000Z" |
| `updated_at_utc` | string (schema `UpdatedAtUTC`) | no | When dispute updated in UTC date/time. | example: "2022-10-13T19:56:010000000Z" |
| `is_network` | boolean | no | Open a dispute over a network authorization. | example: true |
| `is_dispute_migrated` | boolean | no | Has this dispute been migrated to the Pismo platform? | example: false |
| `reversal_id` | number | no | Dispute credit reversal ID. | example: 10042 |
| `network_return_reason_code` | string | no | Network reason code response. | example: "2833" |
| `network_brand_type` | string (schema `NetworkBrand`) | no | Network brand | enum: ["Visa", "Mastercard", "Elo"]; example: "Visa" |
| `transaction_date` | string | no | Transaction date related to authorization, format = yyyy-mm-dd | example: "2021-02-02" |
| `stop_automated_installment` | boolean (schema `stopAutomatedInstallment`) | no | Automated dispute installment control flag. If an issuer opens a dispute for a transaction that has more than one installment, with installments that can still be posted, the issuer will need to open a dispute for subsequent installments as well. With automated dispute installment control, once you open a chargeback for the first installment, the same information can be used for subsequent transaction installments.<br> | example: true |
| `card_hash` | string | no | Card number hash. | example: "XYZddue74kd8" |
| `authorization_code` | string (schema `AuthorizationCode`) | no | Authorization code | example: "F0JR9H" |
| `transaction_amount` | number (schema `TransactionAmount`) | no | Transaction amount | example: 86753.09 |
| `is_dispute_invalid_transaction` | boolean | no | Is this an invalid authorization dispute? | example: false |
| `dispute_installments` | array of object (schema `DisputeInstallment`) | no |  |  |
| `network_return_reject_reason_code` | integer | no | Formatted network reject reason information. | example: 5000 |
| `network_response_error` | string | no | Network response error. | example: "The network returned [Create First Chargeback - Details provided in the request are invalid.], reasonCode [INVALID_REQUEST] and the source [SYSTEM]" |

200 Example `Dispute without DisputeInstallment`:

```json
{
  "id": 1,
  "org_id": "123456789",
  "account_id": 30605,
  "authorization_id": 4352243,
  "disputed_amount": 10.5,
  "comment": "Some comment",
  "dispute_reason": 4855,
  "modality": 4855,
  "dispute_status": "PENDING",
  "timeline": "{ \"data\": \"test\"}",
  "protocol": "20190321L123456",
  "created_at": "2021-02-21",
  "updated_at": "2021-02-22",
  "created_at_utc": "2021-02-21T22:51:43.000000000Z",
  "updated_at_utc": "2021-02-25T01:43:06.000000000Z",
  "is_network": true,
  "is_dispute_migrated": false,
  "reversal_id": 123,
  "network_return_reason_code": "2833",
  "dispute_installment": [],
  "network_return_reject_reason_code": 5000,
  "network_response_error": "The network returned [Create First Chargeback - Details provided in the request are invalid.], reasonCode [INVALID_REQUEST] and the source [SYSTEM]",
  "transaction_date": "2021-02-21",
  "stop_automated_installment": true,
  "card_hash": "XYZ",
  "authorization_code": "123456",
  "is_dispute_invalid_transaction": true,
  "transaction_amount": 10.5
}
```

200 Example `Dispute registered on Mastercard`:

```json
{
  "id": 1,
  "org_id": "123456789",
  "account_id": 30605,
  "authorization_id": 4352243,
  "disputed_amount": 10.5,
  "comment": "Some comment",
  "dispute_reason": 4855,
  "modality": 4855,
  "dispute_status": "PENDING",
  "timeline": "{ \"data\": \"test\"}",
  "protocol": "20190321L123456",
  "created_at": "2021-02-21",
  "updated_at": "2021-02-22",
  "created_at_utc": "2021-02-21T22:51:43.000000000Z",
  "updated_at_utc": "2021-02-25T01:43:06.000000000Z",
  "is_network": true,
  "is_dispute_migrated": false,
  "reversal_id": 10042,
  "network_return_reason_code": "2833",
  "card_hash": "XYZ",
  "authorization_code": "123456",
  "is_dispute_invalid_transaction": true,
  "transaction_amount": 10.5,
  "dispute_installments": [
    {
      "id": 50068,
      "dispute_id": 42,
      "installment": 2,
      "arn": "000000485723",
      "chargeback_id": "4586",
      "claim_id": "00058678",
      "installment_disputed_amount": 45.5,
      "network_return_reason_code": "4853",
      "reason_code": 4853,
      "network_return_reject_reason": "Code1=5000(00):D0025/000;DE072=D0025\\\\\\\\4837\\\\\\\\\\\\\\\\",
      "network_response_error": null,
      "dispute_status": {
        "id": 5,
        "description": "CHARGEBACK_CONFIDENCE_CREDIT_SYSTEM_DISAGREEMENT",
        "type": "PRIMITIVE",
        "group": "CARDNETWORK_CHARGEBACK"
      },
      "network_response": null,
      "transaction_id": null,
      "dispute_form": null,
      "dispute_form_id": 0,
      "pre_arb_master": null,
      "chargeback_ref_num": null,
      "network_response_amount": 12.3,
      "network_response_currency": "USD",
      "is_first_installment": true,
      "network_return_reject_reason_code": 5000
    }
  ],
  "network_return_reject_reason_code": 5000,
  "network_response_error": "The network returned [Create First Chargeback - Details provided in the request are invalid.], reasonCode [INVALID_REQUEST] and the source [SYSTEM]",
  "transaction_date": "2021-02-21"
}
```

200 Example `Dispute registered on Mastercard with Fraud Report`:

```json
{
  "id": 1,
  "org_id": "123456789",
  "account_id": 30605,
  "authorization_id": 4352243,
  "disputed_amount": 10.5,
  "comment": "Some comment",
  "dispute_reason": 4855,
  "modality": 4855,
  "dispute_status": "PENDING",
  "timeline": "{ \"data\": \"test\"}",
  "protocol": "20190321L123456",
  "created_at": "2021-02-21",
  "updated_at": "2021-02-22",
  "created_at_utc": "2021-02-21T22:51:43.000000000Z",
  "updated_at_utc": "2021-02-25T01:43:06.000000000Z",
  "is_network": true,
  "is_dispute_migrated": false,
  "reversal_id": 10042,
  "network_return_reason_code": "2833",
  "card_hash": "XYZ",
  "authorization_code": "123456",
  "is_dispute_invalid_transaction": true,
  "transaction_amount": 10.5,
  "dispute_installment": [
    {
      "id": 50068,
      "dispute_id": 42,
      "installment": 2,
      "arn": "000000485723",
      "chargeback_id": "4586",
      "claim_id": "00058678",
      "installment_disputed_amount": 45.5,
      "network_return_reason_code": "4853",
      "reason_code": 4853,
      "network_return_reject_reason": "Code1=5000(00):D0025/000;DE072=D0025\\\\\\\\4837\\\\\\\\\\\\\\\\",
      "network_response_error": null,
      "dispute_status": {
        "id": 5,
        "description": "CHARGEBACK_CONFIDENCE_CREDIT_SYSTEM_DISAGREEMENT.",
        "type": "PRIMITIVE",
        "group": "CARDNETWORK_CHARGEBACK"
      },
      "network_response": null,
      "transaction_id": null,
      "dispute_form": null,
      "dispute_fraud_report": {
        "fraud_report_id": 8,
        "status": "FAILED",
        "network_brand_type": "MASTERCARD",
        "report": {
          "sub_type": "K",
          "fraud_type": "00",
          "acct_status": "ACCT_IS_OPEN",
          "device_type": "1",
          "report_date": "2021-02-11",
          "chgbk_indicator": "1",
          "cvc_invalid_indicator": "Y"
        },
        "fraud_report_network_id": 1,
        "comment_network": "Fraud Report Disputed transaction is already reported to the fraud system Last item fraud is not a FD1.",
        "created_at": "2021-12-08 17:44:48",
        "updated_at": "2021-12-09 11:46:55"
      },
      "dispute_form_id": 0,
      "pre_arb_master": null,
      "chargeback_ref_num": null,
      "network_response_amount": 12.3,
      "network_response_currency": "USD",
      "is_first_installment": true,
      "network_return_reject_reason_code": 5000
    }
  ],
  "network_return_reject_reason_code": 5000,
  "network_response_error": "The network returned [Create First Chargeback - Details provided in the request are invalid.], reasonCode [INVALID_REQUEST] and the source [SYSTEM]"
}
```

200 Example `Dispute with Pre Arbitration Registered`:

```json
{
  "id": 1,
  "org_id": "123456789",
  "account_id": 30605,
  "authorization_id": 4352243,
  "disputed_amount": 10.5,
  "comment": "Some comment",
  "dispute_reason": 4855,
  "modality": 4855,
  "dispute_status": "PENDING",
  "timeline": "{ \"data\": \"test\"}",
  "protocol": "20190321L123456",
  "created_at": "2021-02-21",
  "updated_at": "2021-02-22",
  "created_at_utc": "2021-02-21T22:51:43.000000000Z",
  "updated_at_utc": "2021-02-25T01:43:06.000000000Z",
  "is_network": true,
  "is_dispute_migrated": false,
  "reversal_id": 10042,
  "network_return_reason_code": "2833",
  "card_hash": "XYZ",
  "authorization_code": "123456",
  "is_dispute_invalid_transaction": true,
  "transaction_amount": 10.5,
  "dispute_installment": [
    {
      "id": 50068,
      "dispute_id": 42,
      "installment": 2,
      "arn": "000000485723",
      "chargeback_id": "4586",
      "claim_id": "00058678",
      "installment_disputed_amount": 45.5,
      "network_return_reason_code": "4853",
      "reason_code": 4853,
      "network_return_reject_reason": "Code1=5000(00):D0025/000;DE072=D0025\\\\\\\\4837\\\\\\\\\\\\\\\\",
      "network_response_error": null,
      "dispute_status": {
        "id": 5,
        "description": "CHARGEBACK_CONFIDENCE_CREDIT_SYSTEM_DISAGREEMENT.",
        "type": "PRIMITIVE",
        "group": "CARDNETWORK_CHARGEBACK"
      },
      "network_response": null,
      "transaction_id": null,
      "dispute_form": null,
      "dispute_fraud_report": null,
      "dispute_form_id": 0,
      "pre_arb_master": {
        "id": 1,
        "memo": "This is a test memo.",
        "updated_chargeback_reason_code": "4836",
        "merchant_name": "Acme Widgets",
        "acquiring_institution_code": "004321",
        "change_reason_code_reason": "This is a test reason.",
        "case_network_response": "COMPLETED_SND_2/10/2021 8:43:21 AM",
        "acquirer_memo": "Not valid",
        "action": "REJECT",
        "response_date": "2021-02-14"
      },
      "chargeback_ref_num": null,
      "network_response_amount": 12.3,
      "network_response_currency": "USD",
      "is_first_installment": true,
      "network_return_reject_reason_code": 5000
    }
  ],
  "network_return_reject_reason_code": 5000,
  "network_response_error": "The network returned [Create First Chargeback - Details provided in the request are invalid.], reasonCode [INVALID_REQUEST] and the source [SYSTEM]",
  "transaction_date": "2021-02-21"
}
```


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;201;400;401;404;500`, has examples `True`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Card_issuing_-_Disputes.yaml method=PUT path=/v1/disputes/{disputeId} operationId=put-v1-disputes-disputeId -->
### `PUT /v1/disputes/{disputeId}` — Update dispute

- **operationId:** `put-v1-disputes-disputeId`
- **Specification:** `api-specs/Card_issuing_-_Disputes.yaml` (Card issuing - Disputes)
- **Server base URL(s):** `https://sandbox.pismolabs.io/disputes`
- **Tags:** `Disputes`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Update one or more dispute fields. Parameters that are not passed are not updated.
>
> **Note:** You can only update a dispute if its group status is `OPEN`, `FAILED`, `DENIED` or `MIGRATION`. Refer to the [Dispute state machine](https://developers.pismo.io/pismo-docs/docs/disputes-state-machine) for more information.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `disputeId` | path | yes | number | Dispute ID |  |

#### Request body

Required: yes

> New Dispute reason code and comment.

**Content type `application/json`** — schema: object (schema `UpdateDisputeRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `disputed_amount` | number (schema `DisputedAmount`) | no | Disputed amount. | example: 10 |
| `currency_code` | string | no | ISO-4217 code for transaction currency. For example, 986 = Brazilian real.  <br><br>**Note:** Only allowed if you are updating a dispute in a Zero balance program.<br> | example: "986" |
| `reason_code` | number (schema `reasonCode`) | no | Each card network, such as Visa or Mastercard, defines and maintains their own unique set of reason codes, which banks that issue credit and debit cards under their brands apply to disputes. Here's a reason code [quick reference](https://www.chargebackgurus.com/blog/a-definitive-guide-to-chargeback-reason-codes-by-card-network#chargback-reason-code-quick-reference-guide) for the major credit card networks.<br><br>For Visa, this would be either `10` (fraud - card present), `11` (authorization), `12` (processing error), or `13` (consumer dispute).<br><br>For more infomation, refer to the [Visa](https://usa.visa.com/dam/VCOM/global/support-legal/documents/chargeback-management-guidelines-for-visa-merchants-vbs-19-may-16-%20v2.pdf) or [Mastercard](https://www.mastercard.us/content/dam/public/mastercardcom/na/global-site/documents/chargeback-guide.pdf) chargeback quides.<br><br>For example - `4853` (Mastercard - cardholder dispute), `12` (Visa - processing error) or `72` (ELO - denied authorization)<br> | example: 4853 |
| `comment` | string (schema `Comment`) | no | Client custom dispute comment.<br><br>**REQUIRED** for Visa partial dispute to explain why partial.<br> | maxLength: 5000; nullable: true; example: "Custom comment" |
| `first_installment_amount` | number | no | Amount to be updated on first installment chargeback. | example: 86753.09 |
| `stop_automated_installment` | boolean | no | Stop automated dispute installment control. If an issuer opens a dispute for a transaction that has more than one installment, with installments that can still be posted, the issuer will need to open a dispute for subsequent installments as well. With automated dispute installment control, once you open a chargeback for the first installment, the same information can be used for subsequent transaction installments. Default = `false`.<br> | example: true |
| `transaction_amount` | number | no | Transaction amount.<br><br>**Note:** Only allowed if you are updating a dispute in a Zero balance program.<br> | example: 86753.09 |
| `arn` | string | no | Acquirer reference number for first installment<br><br>**Note:** Only allowed if you are updating a dispute in a Zero balance program.<br> | maxLength: 255; example: "73669599903" |
| `transaction_date` | string | no | Transaction date. Format = yyyy-mm-dd<br><br> **Note:** Only allowed if you are updating a dispute in a Zero balance program.<br> | example: "2025-09-23" |

Example `Update a Dispute with success`:

```json
{
  "reason_code": 42,
  "comment": "Some comment",
  "stop_automated_installment": true
}
```

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `DisputeResponse`) |
| 400 | Bad Request |  |
| 401 | Unauthorized. Invalid or missing access token. |  |
| 404 | Not found |  |
| 422 | Unprocessable entity |  |
| 500 | Internal server error |  |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | number (schema `DisputeID`) | no | Dispute ID | example: 48670 |
| `org_id` | string (schema `OrgID`) | no | Organization/tenant ID. | example: "TN-34778262-f4f0-464d-b4c6-a14exxxxxxxx" |
| `account_id` | number (schema `AccountID`) | no | Pismo account ID | example: 577830 |
| `authorization_id` | number | no | Authorization ID. | example: 4352243 |
| `comment` | string (schema `Comment`) | no | Client custom dispute comment.<br><br>**REQUIRED** for Visa partial dispute to explain why partial.<br> | maxLength: 5000; nullable: true; example: "Custom comment" |
| `dispute_reason` | number (schema `reasonCode`) | no | Each card network, such as Visa or Mastercard, defines and maintains their own unique set of reason codes, which banks that issue credit and debit cards under their brands apply to disputes. Here's a reason code [quick reference](https://www.chargebackgurus.com/blog/a-definitive-guide-to-chargeback-reason-codes-by-card-network#chargback-reason-code-quick-reference-guide) for the major credit card networks.<br><br>For Visa, this would be either `10` (fraud - card present), `11` (authorization), `12` (processing error), or `13` (consumer dispute).<br><br>For more infomation, refer to the [Visa](https://usa.visa.com/dam/VCOM/global/support-legal/documents/chargeback-management-guidelines-for-visa-merchants-vbs-19-may-16-%20v2.pdf) or [Mastercard](https://www.mastercard.us/content/dam/public/mastercardcom/na/global-site/documents/chargeback-guide.pdf) chargeback quides.<br><br>For example - `4853` (Mastercard - cardholder dispute), `12` (Visa - processing error) or `72` (ELO - denied authorization)<br> | example: 4853 |
| `modality` | number | no | Dispute *modality* - legacy term for reason code to file the dispute. | example: 4855 |
| `dispute_status` | string (schema `DisputeStatus`) | no | Dispute status enums.<br> | enum: ["OPENED", "PENDING", "CANCELED", "FAILED", "CHARGEBACK_REJECTED", "CHARGEBACK_CREATED", "CHARGEBACK_ACCEPTED", "CHARGEBACK_CLOSED", "SECOND_PRESENTMENT", "PRE_ARBITRATION_OPENED", "PRE_ARBITRATION_ACCEPTED", "PRE_ARBITRATION_DECLINED", "PRE_ARBITRATION_RECALL", "PRE_ARB_ALLOCATION_OPENED", "FAILED_PRE_ARBITRATION", "PRE_ARB_ALLOCATION_ACCEPTED", "PRE_ARB_ALLOCATION_DECLINED", "PRE_ARB_ALLOCATION_RECALLED", "FAILED_DECLINE_PRE_ARB", "FAILED_ACCEPT_PRE_ARB", "FAILED_ON_CLOSE", "EXPIRED", "ISSUER_LOSS", "MIGRATION", "FAILED_MIGRATION"]; example: "PENDING" |
| `dispute_status_group` | string (schema `DisputeGroupStatus`) | no | Group status enums<br> | enum: ["OPEN", "APPROVED", "DENIED", "CARDNETWORK_CHARGEBACK", "ANALYSING", "CARDNETWORK_SECOND_PRESENTMENT", "FAILED", "CARDNETWORK_PREARBITRATION", "RESEND", "LOSS", "WON", "REJECTED", "FAILED_PROCESSED"]; example: "OPEN" |
| `created_at` | string (schema `CreatedAt`) | no | Created at datetime, format = yyyy-mm-dd hh:mm:ss" | example: "2024-10-18 11:21:45" |
| `updated_at` | string (schema `UpdatedAt2`) | no | Dispute last updated date, format = yyyy-mm-dd. | format: "date"; example: "2021-02-22" |
| `created_at_utc` | string (schema `CreatedAtUTC`) | no | Dispute created in UTC date/time. | format: "date-time"; example: "2021-02-21T22:51:43.000000000Z" |
| `updated_at_utc` | string (schema `UpdatedAtUTC`) | no | When dispute updated in UTC date/time. | example: "2022-10-13T19:56:010000000Z" |
| `timeline` | string | no | Client custom timeline information. | nullable: true; example: "{ \\"data\\": \\"test\\"}" |
| `protocol` | string (schema `Protocol`) | no | Client custom protocol ID. This is primarily for you to internally identify a request. If not provided, Pismo creates a CID (correlation ID) field for this purpose.<br> | maxLength: 500; example: "20251128111532456" |
| `metadata` | object (schema `Metadata`) | no | Can be used for caller's dispute information and process. Objects and name-value pairs.<br><br> **Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis#metadata).<br> | example: {"field1": "value", "field2": "value"} |
| `disputed_amount` | number (schema `DisputedAmount`) | no | Disputed amount. | example: 10 |
| `is_network` | boolean | no | Does dispute have a network authorization? | example: true |
| `is_dispute_migrated` | boolean | no | Has this dispute been migrated to the Pismo platform? | example: false |
| `reversal_id` | number | no | Event-generated reversal ID | example: 123 |
| `network_return_reason_code` | string | no | Network reason code. | example: "4853" |
| `network_brand_type` | string (schema `NetworkBrand`) | no | Network brand | enum: ["Visa", "Mastercard", "Elo"]; example: "Visa" |
| `transaction_date` | string | no | Transaction date, format = yyyy-mm-dd hh:mm:ss | example: "2022-08-04 14:26:20" |
| `transaction_amount` | number (schema `TransactionAmount`) | no | Transaction amount | example: 86753.09 |
| `currency_code` | string | no | ISO-4217 code for transaction currency. For example, `986` = Brazilian real.  <br> | example: "986" |

200 Example `Updated Dispute`:

```json
{
  "id": 1,
  "org_id": "123456789",
  "account_id": 30605,
  "authorization_id": 4352243,
  "comment": "Some comment",
  "dispute_reason": 4855,
  "modality": 4855,
  "dispute_status": "PENDING",
  "timeline": "{ \"data\": \"test\"}",
  "protocol": "20190321L123456"
}
```


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;404;422;500`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-CARD-disputes-overview`.

<!-- op: spec=api-specs/Card_issuing_-_Disputes.yaml method=POST path=/v1/disputes/{disputeId}/event operationId=post-v1-disputes-disputeId-event -->
### `POST /v1/disputes/{disputeId}/event` — Update dispute status

- **operationId:** `post-v1-disputes-disputeId-event`
- **Specification:** `api-specs/Card_issuing_-_Disputes.yaml` (Card issuing - Disputes)
- **Server base URL(s):** `https://sandbox.pismolabs.io/disputes`
- **Tags:** `Disputes`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Change a dispute's status via an event. After creating a dispute and uploading all necessary forms, reports, and evidence files, send the event `OPEN` to officially begin the dispute process with the network.
>
> For more information on events and statuses, refer to the <a href="https://developers.pismo.io/pismo-docs/docs/disputes-state-machine">Disputes state machine</a>.
>
> This endpoint generates a [Dispute status changed](https://developers.pismo.io/events/docs/disputes-dispute-installment-status-change-1) event.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `disputeId` | path | yes | number | Dispute ID |  |

#### Request body

Required: yes

> Event data.

**Content type `application/json`** — schema: object

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `event` | string (schema `Event`) | yes | Event enums. An event has to occur to change a dispute's status<br> | enum: ["ISSUER_WORKED", "CANCEL", "OPEN", "FAILED_ON_CREATION", "RESEND", "REOPEN", "REJECTS", "FAILED_ON_CLOSE", "CLOSED_PROCESSED", "CLOSED", "REJECTS_5000_5001", "ISSUER_REPRESENTMENT_UNWORKED", "ISSUER_LOSS", "EXPIRE", "SEND_PRE_ARBITRATION", "ACCEPTED_PRE_ARBITRATION", "REJECT_PRE_ARBITRATION", "ACCEPT_PRE_ARBITRATION", "DECLINE_PRE_ARBITRATION", "RECALL_PRE_ARBITRATION", "FAILED_ON_MIGRATION"]; example: "ISSUER_LOSS" |
| `reason` | string | yes | Status change reason. | example: "Disputed by account holder." |
| `dispute_installment_id` | number | no | Dispute installment ID. If not passed, the first Installment is used. | example: 234 |
| `memo` | string | no | Enter memo pertaining to the case. **REQUIRED** for ELO dispute. Also **REQUIRED** when `event` = `SEND_PRE_ARBITRATION` and network is Mastercard.<br>Maximum length = 13000 chars.<br> | maxLength: 13000; example: "Example memo" |
| `merchant_name` | string | no | Merchant name - 100 characters maximum.<br>**REQUIRED** only for disputes without transaction and `event` = `SEND_PRE_ARBITRATION` and network is Mastercard.<br> | maxLength: 100; example: "Acme Goods" |
| `updated_chargeback_reason_code` | number (schema `reasonCode`) | no | Each card network, such as Visa or Mastercard, defines and maintains their own unique set of reason codes, which banks that issue credit and debit cards under their brands apply to disputes. Here's a reason code [quick reference](https://www.chargebackgurus.com/blog/a-definitive-guide-to-chargeback-reason-codes-by-card-network#chargback-reason-code-quick-reference-guide) for the major credit card networks.<br><br>For Visa, this would be either `10` (fraud - card present), `11` (authorization), `12` (processing error), or `13` (consumer dispute).<br><br>For more infomation, refer to the [Visa](https://usa.visa.com/dam/VCOM/global/support-legal/documents/chargeback-management-guidelines-for-visa-merchants-vbs-19-may-16-%20v2.pdf) or [Mastercard](https://www.mastercard.us/content/dam/public/mastercardcom/na/global-site/documents/chargeback-guide.pdf) chargeback quides.<br><br>For example - `4853` (Mastercard - cardholder dispute), `12` (Visa - processing error) or `72` (ELO - denied authorization)<br> | example: 4853 |
| `change_reason_code_reason` | string | no | Explanation for changing the reason code, if that's what you are doing - 1000 characters maximum.<br>**REQUIRED** if `updated_chargeback_reason_code` is passed,  `event` = `SEND_PRE_ARBITRATION` and network is Mastercard.<br> | maxLength: 1000 |
| `pre_arb_is_partial` | boolean | no | Pre-arbitration is for a partial amount and not the full amount?<br>Used when `event` = `SEND_PRE_ARBITRATION`.<br> |  |
| `pre_arb_currency_code` | string | no | ISO 4217 3-letter currency code, for example, `USD` (United States) or `BRL` (Brazilian Real).<br>**REQUIRED** if `pre_arb_is_partial` = `true` and  `event` = `SEND_PRE_ARBITRATION`.<br> | maxLength: 3; example: "BRL" |
| `justify_not_accepted_fully` | string | no | Explanation for asking for full or partial amount - 10000 characters maximum.<br>**REQUIRED** if `pre_arb_is_partial` = `true` or `event` = DECLINE_PRE_ARBITRATION.<br> | maxLength: 10000; example: "Partial refund based on already being used" |
| `pre_arb_amount` | number | no | Pre-arbitration amount.<br>**REQUIRED** if `pre_arb_is_partial` = `true` and `event` = `SEND_PRE_ARBITRATION`.<br> | example: 18.36 |
| `is_dispute_migrated` | boolean | no | Is dispute migrated? Default is `false`. |  |

Example `Change a Dispute status with success`:

```json
{
  "event": "OPEN",
  "reason": "Disputed by account holder."
}
```

Example `Send Pre-arbitration to Mastercard network`:

```json
{
  "event": "SEND_PRE_ARBITRATION",
  "reason": "Disputed by account holder.",
  "dispute_installment_id": 234,
  "memo": "This is a test memo.",
  "updated_chargeback_reason_code": 4859,
  "change_reason_code_reason": "This is a test reason."
}
```

Example `Send Pre-arbitration to Mastercard network - Dispute without transaction`:

```json
{
  "event": "SEND_PRE_ARBITRATION",
  "reason": "Disputed by account holder.",
  "dispute_installment_id": 234,
  "memo": "This is a test memo.",
  "merchant_name": "Acme Goods",
  "updated_chargeback_reason_code": 4859,
  "change_reason_code_reason": "This is a test reason."
}
```

Example `Send accept full pre-arbitration allocation Visa`:

```json
{
  "event": "ACCEPT_PRE_ARBITRATION",
  "reason": "Disputed by account holder.",
  "dispute_installment_id": 234
}
```

Example `Send Pre-arbitration partial to Mastercard network`:

```json
{
  "event": "SEND_PRE_ARBITRATION",
  "reason": "Disputed by account holder.",
  "dispute_installment_id": 234,
  "memo": "This is a test memo.",
  "updated_chargeback_reason_code": 4859,
  "change_reason_code_reason": "This is a test reason.",
  "pre_arb_is_partial": true,
  "pre_arb_currency_code": "840",
  "pre_arb_amount": 18.36
}
```

Example `Send Pre-arbitration partial to Mastercard network - Dispute without transaction`:

```json
{
  "event": "SEND_PRE_ARBITRATION",
  "reason": "Disputed by account holder.",
  "dispute_installment_id": 234,
  "memo": "This is a test memo.",
  "merchant_name": "Acme Goods",
  "updated_chargeback_reason_code": 4859,
  "change_reason_code_reason": "This is a test reason.",
  "pre_arb_is_partial": true,
  "pre_arb_currency_code": "840",
  "pre_arb_amount": 18.36
}
```

Example `Send accept partial pre-arbitration allocation Visa`:

```json
{
  "event": "ACCEPT_PRE_ARBITRATION",
  "reason": "Disputed by account holder.",
  "dispute_installment_id": 234,
  "pre_arb_is_partial": true,
  "pre_arb_currency_code": "840",
  "justify_not_accepted_fully": "Justification text",
  "pre_arb_amount": 18.36
}
```

Example `Send decline pre-arbitration allocation Visa`:

```json
{
  "event": "DECLINE_PRE_ARBITRATION",
  "reason": "Disputed by account holder.",
  "dispute_installment_id": 234,
  "justify_not_accepted_fully": "Justification text"
}
```

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `DisputeResponse`) |
| 400 | Bad Request |  |
| 401 | Unauthorized. Invalid or missing access token. |  |
| 404 | Not found |  |
| 500 | Internal server error |  |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | number (schema `DisputeID`) | no | Dispute ID | example: 48670 |
| `org_id` | string (schema `OrgID`) | no | Organization/tenant ID. | example: "TN-34778262-f4f0-464d-b4c6-a14exxxxxxxx" |
| `account_id` | number (schema `AccountID`) | no | Pismo account ID | example: 577830 |
| `authorization_id` | number | no | Authorization ID. | example: 4352243 |
| `comment` | string (schema `Comment`) | no | Client custom dispute comment.<br><br>**REQUIRED** for Visa partial dispute to explain why partial.<br> | maxLength: 5000; nullable: true; example: "Custom comment" |
| `dispute_reason` | number (schema `reasonCode`) | no | Each card network, such as Visa or Mastercard, defines and maintains their own unique set of reason codes, which banks that issue credit and debit cards under their brands apply to disputes. Here's a reason code [quick reference](https://www.chargebackgurus.com/blog/a-definitive-guide-to-chargeback-reason-codes-by-card-network#chargback-reason-code-quick-reference-guide) for the major credit card networks.<br><br>For Visa, this would be either `10` (fraud - card present), `11` (authorization), `12` (processing error), or `13` (consumer dispute).<br><br>For more infomation, refer to the [Visa](https://usa.visa.com/dam/VCOM/global/support-legal/documents/chargeback-management-guidelines-for-visa-merchants-vbs-19-may-16-%20v2.pdf) or [Mastercard](https://www.mastercard.us/content/dam/public/mastercardcom/na/global-site/documents/chargeback-guide.pdf) chargeback quides.<br><br>For example - `4853` (Mastercard - cardholder dispute), `12` (Visa - processing error) or `72` (ELO - denied authorization)<br> | example: 4853 |
| `modality` | number | no | Dispute *modality* - legacy term for reason code to file the dispute. | example: 4855 |
| `dispute_status` | string (schema `DisputeStatus`) | no | Dispute status enums.<br> | enum: ["OPENED", "PENDING", "CANCELED", "FAILED", "CHARGEBACK_REJECTED", "CHARGEBACK_CREATED", "CHARGEBACK_ACCEPTED", "CHARGEBACK_CLOSED", "SECOND_PRESENTMENT", "PRE_ARBITRATION_OPENED", "PRE_ARBITRATION_ACCEPTED", "PRE_ARBITRATION_DECLINED", "PRE_ARBITRATION_RECALL", "PRE_ARB_ALLOCATION_OPENED", "FAILED_PRE_ARBITRATION", "PRE_ARB_ALLOCATION_ACCEPTED", "PRE_ARB_ALLOCATION_DECLINED", "PRE_ARB_ALLOCATION_RECALLED", "FAILED_DECLINE_PRE_ARB", "FAILED_ACCEPT_PRE_ARB", "FAILED_ON_CLOSE", "EXPIRED", "ISSUER_LOSS", "MIGRATION", "FAILED_MIGRATION"]; example: "PENDING" |
| `dispute_status_group` | string (schema `DisputeGroupStatus`) | no | Group status enums<br> | enum: ["OPEN", "APPROVED", "DENIED", "CARDNETWORK_CHARGEBACK", "ANALYSING", "CARDNETWORK_SECOND_PRESENTMENT", "FAILED", "CARDNETWORK_PREARBITRATION", "RESEND", "LOSS", "WON", "REJECTED", "FAILED_PROCESSED"]; example: "OPEN" |
| `created_at` | string (schema `CreatedAt`) | no | Created at datetime, format = yyyy-mm-dd hh:mm:ss" | example: "2024-10-18 11:21:45" |
| `updated_at` | string (schema `UpdatedAt2`) | no | Dispute last updated date, format = yyyy-mm-dd. | format: "date"; example: "2021-02-22" |
| `created_at_utc` | string (schema `CreatedAtUTC`) | no | Dispute created in UTC date/time. | format: "date-time"; example: "2021-02-21T22:51:43.000000000Z" |
| `updated_at_utc` | string (schema `UpdatedAtUTC`) | no | When dispute updated in UTC date/time. | example: "2022-10-13T19:56:010000000Z" |
| `timeline` | string | no | Client custom timeline information. | nullable: true; example: "{ \\"data\\": \\"test\\"}" |
| `protocol` | string (schema `Protocol`) | no | Client custom protocol ID. This is primarily for you to internally identify a request. If not provided, Pismo creates a CID (correlation ID) field for this purpose.<br> | maxLength: 500; example: "20251128111532456" |
| `metadata` | object (schema `Metadata`) | no | Can be used for caller's dispute information and process. Objects and name-value pairs.<br><br> **Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis#metadata).<br> | example: {"field1": "value", "field2": "value"} |
| `disputed_amount` | number (schema `DisputedAmount`) | no | Disputed amount. | example: 10 |
| `is_network` | boolean | no | Does dispute have a network authorization? | example: true |
| `is_dispute_migrated` | boolean | no | Has this dispute been migrated to the Pismo platform? | example: false |
| `reversal_id` | number | no | Event-generated reversal ID | example: 123 |
| `network_return_reason_code` | string | no | Network reason code. | example: "4853" |
| `network_brand_type` | string (schema `NetworkBrand`) | no | Network brand | enum: ["Visa", "Mastercard", "Elo"]; example: "Visa" |
| `transaction_date` | string | no | Transaction date, format = yyyy-mm-dd hh:mm:ss | example: "2022-08-04 14:26:20" |
| `transaction_amount` | number (schema `TransactionAmount`) | no | Transaction amount | example: 86753.09 |
| `currency_code` | string | no | ISO-4217 code for transaction currency. For example, `986` = Brazilian real.  <br> | example: "986" |

200 Example `Updated status`:

```json
{
  "id": 1009087,
  "org_id": "TN-34778262-f4f0-464d-b4c6-a14exxxxxxxx",
  "account_id": 30605,
  "authorization_id": 4352243,
  "comment": "Some comment",
  "dispute_reason": 4855,
  "modality": 4855,
  "dispute_status": "OPENED",
  "dispute_status_group": "ANALYSING",
  "timeline": "{ \"data\": \"test\"}",
  "protocol": "20190321L123456"
}
```


#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `disputes-dispute-installment-status-change-1` | https://developers.pismo.io/events/docs/disputes-dispute-installment-status-change-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;404;500`, has examples `True`, emits events `1`, deprecated `False`.

Guides that link to this operation: `KU-CARD-disputes-overview`, `KU-CARD-disputes-state-machine`, `KU-CARD-visa-dispute-use-case`, `KU-EVT-disputes-endpoint-generated-events`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/DisputeInstallment -->
### Schema `DisputeInstallment`

Pointer: `#/components/schemas/DisputeInstallment`. Type: object (schema `DisputeInstallment`).

> Dispute installment information

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | number | no | Dispute installment ID. | example: 50068 |
| `dispute_id` | number (schema `DisputeID`) | no | Dispute ID | example: 48670 |
| `installment` | integer | no | Installment number. | example: 2 |
| `arn` | string | no | Installment acquirer reference number. | example: "000000485723" |
| `chargeback_id` | string | no | Network chargeback ID. | nullable: true; example: "4586" |
| `claim_id` | string | no | Network claim ID. | nullable: true; example: "00058678" |
| `installment_disputed_amount` | number | no | Installment disputed amount. | example: 45.5 |
| `network_return_reason_code` | string | no | Network returned reason code. | nullable: true; example: "4853" |
| `networkStatus` | string | no | Dispute status from the network | example: "Authorization Dispute - Accepted by Acq" |
| `reason_code` | number (schema `reasonCode`) | no | Each card network, such as Visa or Mastercard, defines and maintains their own unique set of reason codes, which banks that issue credit and debit cards under their brands apply to disputes. Here's a reason code [quick reference](https://www.chargebackgurus.com/blog/a-definitive-guide-to-chargeback-reason-codes-by-card-network#chargback-reason-code-quick-reference-guide) for the major credit card networks.<br><br>For Visa, this would be either `10` (fraud - card present), `11` (authorization), `12` (processing error), or `13` (consumer dispute).<br><br>For more infomation, refer to the [Visa](https://usa.visa.com/dam/VCOM/global/support-legal/documents/chargeback-management-guidelines-for-visa-merchants-vbs-19-may-16-%20v2.pdf) or [Mastercard](https://www.mastercard.us/content/dam/public/mastercardcom/na/global-site/documents/chargeback-guide.pdf) chargeback quides.<br><br>For example - `4853` (Mastercard - cardholder dispute), `12` (Visa - processing error) or `72` (ELO - denied authorization)<br> | example: 4853 |
| `network_return_reject_reason` | string | no | Formated network reject reason information. | nullable: true; example: "5000" |
| `network_response_error` | string | no | Network response error. | nullable: true; example: "The network returned [Create First Chargeback - Details provided in the request are invalid.], reasonCode [INVALID_REQUEST] and the source [SYSTEM]" |
| `dispute_status` | object (schema `DisputeStatusObject`) | no | Dispute status information |  |
| `network_response` | object | no | Network response information | nullable: true |
| `network_response.id` | number | no | Network response ID. | example: 5 |
| `network_response.dispute_id` | number (schema `DisputeID`) | no | Dispute ID | example: 48670 |
| `network_response.dispute_installment_id` | integer (schema `DisputeInstallmentId`) | no | Dispute installment ID. | example: 8675309 |
| `network_response.claim_id` | string | no | Network claim ID. | example: "00058678" |
| `network_response.chargeback_id` | string | no | Network chargeback ID. | example: "4586" |
| `network_response.reason_code` | number (schema `reasonCode`) | no | Each card network, such as Visa or Mastercard, defines and maintains their own unique set of reason codes, which banks that issue credit and debit cards under their brands apply to disputes. Here's a reason code [quick reference](https://www.chargebackgurus.com/blog/a-definitive-guide-to-chargeback-reason-codes-by-card-network#chargback-reason-code-quick-reference-guide) for the major credit card networks.<br><br>For Visa, this would be either `10` (fraud - card present), `11` (authorization), `12` (processing error), or `13` (consumer dispute).<br><br>For more infomation, refer to the [Visa](https://usa.visa.com/dam/VCOM/global/support-legal/documents/chargeback-management-guidelines-for-visa-merchants-vbs-19-may-16-%20v2.pdf) or [Mastercard](https://www.mastercard.us/content/dam/public/mastercardcom/na/global-site/documents/chargeback-guide.pdf) chargeback quides.<br><br>For example - `4853` (Mastercard - cardholder dispute), `12` (Visa - processing error) or `72` (ELO - denied authorization)<br> | example: 4853 |
| `network_response.response_error` | string | no | Network response error. | example: "The network returned [[edf00094-c762-49cc-9a92-380c49adf557_V_1638813966704] Visa returned an ApiException], reasonCode [E-200100002] with the source [One or more required fields are missing. Please correct the following errors:PinPreferringCard]." |
| `network_response.reject_reason` | string | no | Network reject reason information. | example: "Code1=0283(00):D0025/000;DE072=D0025\\\\4837\\\\\\\\" |
| `transaction_id` | string | no | Transaction ID. | nullable: true; example: "5000" |
| `dispute_form_list` | array of object (schema `DisputeFormResponse`) | no |  |  |
| `dispute_fraud_report` | object (schema `DisputeFraudReportDto`) | no | Response to a dispute fraud report. |  |
| `pre_arbitration` | object (schema `preArbitrationDto`) | no | Information when dispute is submitted to Pre-Arbitration and case was created. |  |
| `dispute_due_to` | string (schema `disputeDueTo`) | no | **REQUIRED** when dispute is open to Visa Collaboration (Reason code 12 and 13 and Visa network brand). Collaboration is the new name for Visa's old chargeback process, where each party has several chances to investigate and submit evidence in order to determine whether a chargeback is legitimate.<br><br><br>`NR` = Merchandise/services not receive<br><br>`CR` = Cancelled recurring transaction<br><br>`ND` = Not as described<br><br>`DM` = Damaged or defective merchandise<br><br>`Q` = Quality<br><br>`CM` = Counterfeit merchandise<br><br>`M` = Misrepresentation<br><br>`CN` = Credit not processed<br><br>`CS` = Cancelled merchandise/services<br><br>`OC` = Original credit not accepted<br><br>`CL` = Non-receipt of cash<br><br>`TC` = Terms of contract (virtual account)<br><br>`D` = Duplicate<br><br>`IAN` = Incorrect account number<br><br>`IA` = Incorrect amount<br><br>`IC` = Incorrect currency<br><br>`IT` = Incorrect transaction code<br><br>`ID` = Invalid data<br><br>`LP` = Late presentment<br><br>`P` = Paid by other means<br><br><br>For VISA, you need to fill out the `collaborationQuestionnaire` form object in the [Create dispute form](ref:post-v1-disputes-disputeid-forms) endpoint.<br> | enum: ["NR", "CR", "ND", "DM", "Q", "CM", "M", "CN", "CS", "OC", "CL", "TC", "D", "IAN", "IA", "IC", "IT", "ID", "LP", "P"]; example: "NR" |
| `chargeback_ref_num` | string | no | Chargeback reference number. | nullable: true |
| `network_response_amount` | number | no | Last amount disputed in the claim registered when getting new information from network brand. | nullable: true |
| `network_response_currency` | string | no | Last currency of amount disputed in the claim registered when getting new information from network brand. | nullable: true |
| `is_first_installment` | boolean | no | Dispute installment references authorization's first installment. |  |
| `network_return_reject_reason_code` | integer | no | Formatted network reject reason information. | nullable: true; example: 5000 |

<!-- schema: #/components/schemas/DisputeStatusObject -->
### Schema `DisputeStatusObject`

Pointer: `#/components/schemas/DisputeStatusObject`. Type: object (schema `DisputeStatusObject`).

> Dispute status information

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | number (schema `DisputeStatusID`) | no | Dispute status ID | example: 88999 |
| `description` | string | no | Status description |  |
| `type` | string | no | State machine type | enum: ["PRIMITIVE", "PRIMITIVE_ON_US"]; example: "PRIMITIVE" |
| `group` | string (schema `DisputeGroupStatus`) | no | Group status enums<br> | enum: ["OPEN", "APPROVED", "DENIED", "CARDNETWORK_CHARGEBACK", "ANALYSING", "CARDNETWORK_SECOND_PRESENTMENT", "FAILED", "CARDNETWORK_PREARBITRATION", "RESEND", "LOSS", "WON", "REJECTED", "FAILED_PROCESSED"]; example: "OPEN" |

<!-- schema: #/components/schemas/DisputeFormResponse -->
### Schema `DisputeFormResponse`

Pointer: `#/components/schemas/DisputeFormResponse`. Type: object (schema `DisputeFormResponse`).

> Dispute Form response.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | number | no | Dispute form ID. | example: 122 |
| `dispute_installment_id` | number | no | If necessary to join Form to Installment. If not passed, first installment is used. | nullable: true |
| `status` | string (schema `DisputeFormStatus`) | no | Dispute form status. | enum: ["PENDING", "PROCESSED", "FAILED", "INACTIVE"]; example: "PENDING" |
| `network` | string | no | Network for dispute Form. | enum: ["PRIMITIVE_ON_US", "PRIMITIVE"]; example: "PRIMITIVE" |
| `form` | object | no |  |  |
| `form.ebdf` | object | no |  |  |
| `form.ebdf.fraudDrfDocument` | object (schema `FraudDrfDocumentStructure`) | no |  |  |
| `form.ebdf.cardholderDisputeChargebackDrfDocument` | object (schema `CardholderDisputeChargebackDrfDocumentStructure`) | no |  |  |
| `form.ebdf.pointOfInteractionErrorsDrfDocument` | object (schema `PointOfInteractionErrorsDrfDocumentStructure`) | no |  |  |
| `form.allocationQuestionnaire` | object (schema `VisaAllocationQuestionnaireDocumentStructure`) | no |  |  |
| `form.collaborationQuestionnaire` | object (schema `VisaCollaborationQuestionnaireDocumentStructure`) | no |  |  |
| `form.preArbitration` | object (schema `PreArbitration`) | no |  |  |
| `created_at` | string (schema `CreatedAt`) | no | Created at datetime, format = yyyy-mm-dd hh:mm:ss" | example: "2024-10-18 11:21:45" |
| `created_at_utc` | string (schema `CreatedAtUTC`) | no | Dispute created in UTC date/time. | format: "date-time"; example: "2021-02-21T22:51:43.000000000Z" |
| `update_at` | string | no | Update date, format = yyyy-mm-dd | format: "date"; example: "2021-02-22" |
| `update_at_utc` | string | no | Update UTC date | format: "date-time"; example: "2021-02-21T22:51:43.000000000Z" |
| `dispute_form_type` | object (schema `DisputeFormType`) | no |  |  |

<!-- schema: #/components/schemas/DisputeFraudReportDto -->
### Schema `DisputeFraudReportDto`

Pointer: `#/components/schemas/DisputeFraudReportDto`. Type: object (schema `DisputeFraudReportDto`).

> Response to a dispute fraud report.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `fraud_report_id` | number | no | Dispute fraud report ID. | example: 1 |
| `status` | string (schema `DisputeFormStatus`) | no | Dispute form status. | enum: ["PENDING", "PROCESSED", "FAILED", "INACTIVE"]; example: "PENDING" |
| `network_brand_type` | string (schema `NetworkBrand`) | no | Network brand | enum: ["Visa", "Mastercard", "Elo"]; example: "Visa" |
| `report` | object (schema `DisputeFraudReportDocumentStructure`) | no |  |  |
| `fraud_report_network_id` | number | no | Fraud report network identifier. | example: 1 |
| `comment_network` | string | no | Fraud Report comment network. | example: "Fraud report disputed transaction is already reported to the fraud system Last item fraud is not a FD1." |
| `created_at` | string (schema `CreatedAt`) | no | Created at datetime, format = yyyy-mm-dd hh:mm:ss" | example: "2024-10-18 11:21:45" |
| `updated_at` | string (schema `UpdatedAt`) | no | Datetime when updated, format = yyyy-mm-dd hh:mm:ss | example: "2024-10-18 11:21:45" |

<!-- schema: #/components/schemas/preArbitrationDto -->
### Schema `preArbitrationDto`

Pointer: `#/components/schemas/preArbitrationDto`. Type: object (schema `preArbitrationDto`).

> Information when dispute is submitted to Pre-Arbitration and case was created.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `pre_arbitration_response_id` | number | no | Case ID created from Mastercom. | example: 8775309 |
| `memo` | string | no | Enter a memo pertaining to the case. | example: "This is a test memo." |
| `updated_chargeback_reason_code` | number (schema `reasonCode`) | no | Each card network, such as Visa or Mastercard, defines and maintains their own unique set of reason codes, which banks that issue credit and debit cards under their brands apply to disputes. Here's a reason code [quick reference](https://www.chargebackgurus.com/blog/a-definitive-guide-to-chargeback-reason-codes-by-card-network#chargback-reason-code-quick-reference-guide) for the major credit card networks.<br><br>For Visa, this would be either `10` (fraud - card present), `11` (authorization), `12` (processing error), or `13` (consumer dispute).<br><br>For more infomation, refer to the [Visa](https://usa.visa.com/dam/VCOM/global/support-legal/documents/chargeback-management-guidelines-for-visa-merchants-vbs-19-may-16-%20v2.pdf) or [Mastercard](https://www.mastercard.us/content/dam/public/mastercardcom/na/global-site/documents/chargeback-guide.pdf) chargeback quides.<br><br>For example - `4853` (Mastercard - cardholder dispute), `12` (Visa - processing error) or `72` (ELO - denied authorization)<br> | example: 4853 |
| `merchant_name` | string | no | Merchant name. | example: "Acme Dry Goods" |
| `acquiring_institution_code` | string | no | Acquiring institution code. | example: "004321" |
| `change_reason_code_reason` | string | no | Change reason code reason. | example: "This is a test reason" |
| `case_network_response` | string | no | Updates response from Mastecom about the case. | example: "COMPLETED_SND_2/10/2021 8:43:21 AM" |
| `justify_not_accepted_fully` | string | no | Justify why not accepted fully | example: "Only partial amount in dispute." |
| `is_partial` | boolean (schema `IsPartial`) | no | Is partial amount chargeback? Default is `false`. | default: false; example: false |
| `currency_code_request` | string | no | ISO 4217 3-letter currency code request. | example: "840" |
| `currency_code_response` | string (schema `CurrencyCode`) | no | ISO 4217 3-letter currency code, For example, `986` = Brazilian real and `840` = US dollar. | example: "840" |
| `amount_request` | number | no | Request amount | example: 18.36 |
| `amount_response` | number | no | Response amount | example: 15.25 |
| `acquirer_memo` | string | no | Memo from the acquirer included in the Mastercard pre-arbitration rejection response. | example: "Not valid" |
| `action` | string | no | Network pre-arbitration action. | enum: ["ACCEPT", "REJECT", "REBUT", "ESCALATE", "WITHDRAW", "FAVORSENDER", "FAVORRECEIVER", "DECLINED", "MODIFYCASE", "CREATECASE", "EXPIRED"]; example: "REJECT" |
| `response_date` | string | no | Date of the network's pre-arbitration response. Format = yyyy-mm-dd | example: "2021-02-14" |

<!-- schema: #/components/schemas/FraudDrfDocumentStructure -->
### Schema `FraudDrfDocumentStructure`

Pointer: `#/components/schemas/FraudDrfDocumentStructure`. Type: object (schema `FraudDrfDocumentStructure`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `numberOfItems` | string | no | Number of transactions being disputed as string. | maxLength: 19; example: "1" |
| `types` | string | no | Enter any of the valid values comma separated.<br><br>Valid Values/Format: `CARD_CLOSED`, `REPORT_SAFE`, `CAPTURE_CARD`, `LOST_STOLEN`, `COUNTERFEIT`, `RC_4837`, `RC_4840`<br><br>`RC_4837` = Reason code 4837 (Mastercard - fraud)<br><br>`RC_4840` = Reason code 4840 (Mastercard - fraudelent processing of transaction) | enum: ["CARD_CLOSED", "REPORT_SAFE", "CAPTURE_CARD", "LOST_STOLEN", "COUNTERFEIT", "RC_4837", "RC_4840"]; example: "CARD_CLOSED" |
| `additionalInformation` | string | no | Additional information, if needed, 1000 chars max.<br><br>Valid Values/Format: Alphanumeric / Special Char (~!@#$%^&*()_+{}\|:"<>?,./;'[]-=) | maxLength: 1000; example: "Test additional information" |
| `chargebackRepresentative` | string | no | Customer Service/Chargeback Representative<br><br>Valid Values/Format: Alphanumeric / Special Char (~!@#$%^&*()_+{}\|:"<>?,./;'[]-=) | maxLength: 25; example: "Test representative" |
| `cardIssuerRegion` | string | no | Card issuer region.<br><br>Valid Values:<br><br>   `AP` - Asian Pacific<br><br>   `Europe` - Europe<br><br>   `NAM` - North America<br><br>   `LAC` - Latin America and Caribbean<br><br>   `MEA` - Middle East and Africa | enum: ["AP", "Europe", "NAM", "LAC", "MEA"]; example: "Europe" |
| `cardholderVerificationMethod` | object (schema `CardholderVerificationMethodStructure`) | no |  |  |

<!-- schema: #/components/schemas/CardholderDisputeChargebackDrfDocumentStructure -->
### Schema `CardholderDisputeChargebackDrfDocumentStructure`

Pointer: `#/components/schemas/CardholderDisputeChargebackDrfDocumentStructure`. Type: object (schema `CardholderDisputeChargebackDrfDocumentStructure`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `transactionAmount` | string | no | Transaction amount.<br><br> Length: 0-12<br><br> Valid Values/Format: Numeric | example: "100.00" |
| `type` | string | no | Cardholder dispute type. | enum: ["PRODUCT_DISPUTE", "NOT_PROVIDED", "DIGITAL_GOODS", "CREDIT_NOT_PROCESSED", "COUNTERFEIT", "RECURRING_CANCELLED", "RECURRING_DISCLOSURE", "ADDENDUM_DISPUTE", "HOTEL_NO_SHOW", "PURCHASE_INCOMPLETE", "CANCELLATION_AGREEMENT", "POSTED_CREDIT", "FAILED_TRAVEL"]; minLength: 11; maxLength: 22; example: "PRODUCT_DISPUTE" |
| `deliveryDateOfGoodsOrServices` | string | no | In case of `PRODUCT_DISPUTE`, goods or services delivery date. Format = dd-MMM-yyyy<br> | maxLength: 11; example: "18-FEB-2018" |
| `expectedDeliveryDateOfGoodOrServices` | string | no | In case of `NOT_PROVIDED`, goods or services expected delivery date. Format = dd-MMM-yyyy | maxLength: 11; example: "18-FEB-2018" |
| `returnDate` | string | no | In case of `DIGITAL_GOODS`, return or cancellation of the goods or services. Format = dd-MMM-yyyy | maxLength: 11; example: "18-FEB-2018" |
| `cancellationDate` | string | no | In case of `RECURRING_CANCELLED`, cancellation of the goods or services. Format = dd-MMM-yyyy | maxLength: 11; example: "18-FEB-2018" |
| `cardholderParticipation` | boolean | no | Did the cardholder participate in the transaction? | example: false |
| `disputeDetails` | string | no | Describe the cardholder’s complaint in sufficient detail to meet the requirements for the chargeback as described in the Chargeback Guide and to enable all parties to understand the dispute.<br>Valid Values/Format: Alphanumeric / Special Char (~!@#$%^&*()_+{}\|:"<>?,./;'[]-=)<br> | maxLength: 3000; example: "Test dispute details..." |
| `chargebackRepresentative` | string | no | Customer service/chargeback representative.<br>Valid Values/Format: Alphanumeric / Special Char (~!@#$%^&*()_+{}\|:"<>?,./;'[]-=)<br> | maxLength: 25; example: "Ahsta LaVista Baybee" |

<!-- schema: #/components/schemas/PointOfInteractionErrorsDrfDocumentStructure -->
### Schema `PointOfInteractionErrorsDrfDocumentStructure`

Pointer: `#/components/schemas/PointOfInteractionErrorsDrfDocumentStructure`. Type: object (schema `PointOfInteractionErrorsDrfDocumentStructure`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `transactionAmount` | string | no | The transaction amount as string. | maxLength: 12; example: "20000" |
| `type` | string | no | Error type enum, i.e. `DUPLICATE_DEBIT` | enum: ["DUPLICATE_DEBIT", "INCORRECT_AMOUNT", "LTD_TRANSACTION", "CURRENCY_DISPUTE", "UNREASONABLE_AMOUNT", "DUPLICATE_TRANSACTION", "MERCHANT_CREDIT", "IMPROPER_MERCHANT_SURCHARGE"]; example: "DUPLICATE_DEBIT" |
| `alternateMeansOfPaymentDetails` | string | no | In case of `DUPLICATE_DEBIT`, Alternate means of payment details. Max length = 55 chars.<br>Valid Values/Format: Alphanumeric / Special Char (~!@#$%^&*()_+{}\|:"<>?,./;'[]-=)<br> | maxLength: 55; example: "Test alternate means of payment details" |
| `disputeDetails` | string | no | Describe the cardholder's complaint in sufficient detail to meet the requirements for the chargeback as described in the Chargeback Guide and to enable all parties to understand the dispute.<br>Valid Values/Format: Alphanumeric / Special Char (~!@#$%^&*()_+{}\|:"<>?,./;'[]-=) | maxLength: 4800; example: "Test Dispute details" |
| `chargebackRepresentative` | string | no | Customer service/chargeback representative.<br><br> Valid Values/Format: Alphanumeric / Special Char (~!@#$%^&*()_+{}\|:"<>?,./;'[]-=) | maxLength: 25; example: "Test Representative" |

<!-- schema: #/components/schemas/VisaAllocationQuestionnaireDocumentStructure -->
### Schema `VisaAllocationQuestionnaireDocumentStructure`

Pointer: `#/components/schemas/VisaAllocationQuestionnaireDocumentStructure`. Type: object (schema `VisaAllocationQuestionnaireDocumentStructure`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `accountStatus` | string | yes | Valid in VISA Authorization Flux (reason code 11).<br><br>  `AC` = Account closed<br><br>  `CP` = Credit problem<br><br>  `F` = Fraud<br><br> | enum: ["AC", "CP", "F"]; example: "AC" |
| `oneAuthForMultipleSalesInd` | string | no | Valid in VISA Authorization Flux (reason code 11). | enum: ["Y", "N"]; example: "Y" |

<!-- schema: #/components/schemas/VisaCollaborationQuestionnaireDocumentStructure -->
### Schema `VisaCollaborationQuestionnaireDocumentStructure`

Pointer: `#/components/schemas/VisaCollaborationQuestionnaireDocumentStructure`. Type: object (schema `VisaCollaborationQuestionnaireDocumentStructure`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `incorrectCurrencyReason` | string | no | Valid in VISA Processing Errors Flux (reason code 12.3). | enum: ["CD", "DD"]; example: "CD" |
| `authorizationRequestDeclinedValidDataInd` | boolean | no | Valid in VISA Processing Errors Flux (reason code 12). | example: true |
| `explainWhyValidDataInclusionReason` | string | no | Valid in VISA Processing Errors Flux (reason code 12). | maxLength: 10000; example: "Explain why the inclusion of valid data would have caused the Authorization Request to be declined" |
| `correctCurrency` | integer | no | Valid in VISA Processing Errors Flux (reason code 12). | example: 986 |
| `cardholderDidNotAgreeDCC` | string | no | Valid in VISA Processing Errors Flux (reason code 12). | enum: ["Y", "N"]; example: "Y" |
| `transactionCodeIncorrect` | string | no | Valid in VISA Processing Errors Flux (reason code 12). | enum: ["CRI", "CRD", "DCR"]; example: "CRI" |
| `rolTransactionId` | number | no | Valid in VISA Processing Errors Flux (reason code 12). | example: 123 |
| `incorrectTransactionId` | string | no | Valid in VISA Processing Errors Flux (reason code 12). | maxLength: 17 |
| `explainWhyCreditRefundProcessedInError` | string | no | Valid in VISA Processing Errors Flux (reason code 12). | maxLength: 10000; example: "Explain why the credit refund was processed in error" |
| `issuerMasterFileAccountNumberInd` | string | no | Valid in VISA Processing Errors Flux (reason code 12). | enum: ["Y", "N"]; example: "Y" |
| `receiptAccountNumberMatchInd` | string | no | Valid in VISA Processing Errors Flux (reason code 12). | enum: ["Y", "N"]; example: "Y" |
| `cardholderReceiptAmt` | number | no | Valid in VISA Processing Errors Flux (reason code 12). | example: 12 |
| `merchantDisputePriceDiffInd` | string | no | Valid in VISA Processing Errors Flux (reason code 12). | enum: ["Y", "N"]; example: "Y" |
| `bothTransactionsOnSameAcctNumberInd` | string | no | Valid in VISA Processing Errors Flux (reason code 12). | enum: ["Y", "N"]; example: "Y" |
| `duplicateTranId` | string | no | Valid in VISA Processing Errors Flux (reason code 12). | example: "123456789012345" |
| `issuerOrCardholderOtherAcctWithDiffVisaCardInd` | string | no | Valid in VISA Processing Errors Flux (reason code 12). | enum: ["Y", "N"]; example: "Y" |
| `issuerEvidenceMerchantPassedOnFundsInd` | string | no | Valid in VISA Processing Errors Flux (reason code 12). | enum: ["Y", "N"]; example: "Y" |
| `cardholderAttemptToResolve` | string | no | Valid in VISA Processing Errors Flux (reason code 12 and 13). | enum: ["Y", "N"]; example: "Y" |
| `attemptToResolveProhLocalLaw` | string | no | Valid in VISA Processing Errors Flux (reason code 12 and 13). | enum: ["Y", "N"]; example: "Y" |
| `otherTranSameMerchantInd` | string | no | Valid in VISA Processing Errors Flux (reason code 12). | enum: ["Y", "N"]; example: "Y" |
| `providingPaymentProofOtherMeans` | string | no | Valid in VISA Processing Errors Flux (reason code 12). | enum: ["A", "T", "C", "F", "V", "S", "O"]; example: "A" |
| `arn` | string | no | Valid in VISA Processing Errors Flux (reason code 12). | maxLength: 24; example: "001122334455667788991234" |
| `transactionID` | string | no | Valid in VISA Processing Errors Flux (reason code 12). | maxLength: 15; example: "123456789012345" |
| `merchantFacilitiesWithdrawn` | boolean | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | example: false |
| `cardholderDeceased` | boolean | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | example: false |
| `cancellationDate` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | format: "date"; example: "2022-05-20" |
| `contactMethodWithMerchantInd` | boolean | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | example: true |
| `contactMethodMerchantEmailInd` | boolean | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | example: true |
| `contactMethodMerchantCallCenterInd` | boolean | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | example: true |
| `contactMethodMerchantMailInd` | boolean | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | example: true |
| `contactMethodMerchantSMSInd` | boolean | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | example: true |
| `contactMethodMerchantInPersonInd` | boolean | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | example: true |
| `contactMethodMerchantWebformInd` | boolean | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | example: true |
| `contactMerchantDetailsPhoneNumber` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). |  |
| `contactMerchantDetailsEmailAddress` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). |  |
| `contactMerchantDetailsPhysicalAddress` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). |  |
| `contactMerchantDetailsApplicationName` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). |  |
| `otherFormOfPaymentInd` | boolean | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | example: true |
| `otherFormOfPaymentDesc` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). |  |
| `accountClosureDate` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | format: "date"; example: "2022-05-20" |
| `cancellationMethod` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | maxLength: 10000 |
| `disputeRelateToOffpremisesDistanceSellInd` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | enum: ["Y", "N"] |
| `disputeRelateToInd` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | enum: ["Y", "N"]; example: "Y" |
| `contractDate` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | format: "date"; example: "2022-05-20" |
| `merchandiseOrServices` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | enum: ["Merchandise", "Services"]; example: "Merchandise" |
| `serviceType` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | enum: ["T", "G", "O"]; example: "T" |
| `whatWasPurchased` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | maxLength: 10000; example: "Provide details of what was purchased..." |
| `cardholderReceiveMerchandiseInd` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | enum: ["Y", "N"]; example: "Y" |
| `chReceivedOrExpectedMerchandise` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | format: "date"; example: "2022-05-20" |
| `cardholderReturnMerchandiseInd` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | enum: ["Y", "N"]; example: "Y" |
| `cardholderReturnedMerchandiseDate` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | format: "date"; example: "2022-05-20" |
| `returnedMerchandiseReceivedDate` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | format: "date"; example: "2022-05-20" |
| `returnMethod` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | enum: ["FF", "FE", "D", "U", "P", "O"]; example: "FF" |
| `howMerchandiseReturned` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | maxLength: 10000; example: "Explain how the merchandise was returned..." |
| `shippingTrackingNumber` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | maxLength: 50; example: "774-4u7u3-u4u4u-35347" |
| `cardholderAttemptReturnMerchandise` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | enum: ["Y", "N"] |
| `attemptedReturnDate` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | example: "2022-05-20" |
| `howChAttemptReturnAndDispOfMerchandise` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | maxLength: 10000; example: "Provide a detailed description of how the cardholder attempted to return and the disposition of the merchandise." |
| `merchantRefuseAdvise` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | enum: ["MRRM", "MICNRM"]; example: "MRRM" |
| `didCardholderCancel` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | enum: ["Y", "N"]; example: "Y" |
| `didCardholderCancelBeforeShipping` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | enum: ["Y", "N"]; example: "Y" |
| `timeshareDate` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | format: "date"; example: "2022-05-20" |
| `dateOfService` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | format: "date"; example: "2022-05-20" |
| `certificationGuaranteedReservation` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | enum: ["GR", "RC", "AR"]; example: "GR" |
| `cancellationPolicyProvidedInd` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | enum: ["Y", "N"]; example: "Y" |
| `whatWasOrdered` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | maxLength: 10000; example: "What was ordered..." |
| `merchandiseWasCounterfeitDate` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | format: "date"; example: "2022-05-20" |
| `descCounterfeitMerchandise` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | maxLength: 10000; example: "Describe the counterfeit merchandise" |
| `descDispOfCounterfeitMerchandise` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | maxLength: 10000; example: "Describe the disposition of the counterfeit merchandise" |
| `originalCreditNotAccepted` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | enum: ["R", "O"]; example: "R" |
| `explain` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | maxLength: 10000; example: "Explain" |
| `creditVoucherTransactionReceiptDated` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | enum: ["Y", "N"]; example: "Y" |
| `creditVoucherOrTransactionReceiptDate` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | format: "date"; example: "2022-05-20" |
| `cardholderCancelledReturnedMerchDate` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | format: "date"; example: "2022-05-20" |
| `merchantInLiquidationOrReceivershipInd` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | enum: ["Y", "N"]; example: "Y" |
| `whatWasNotReceived` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | example: "What was not received?" |
| `thirdPartyGiftCardInd` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | enum: ["Y", "N"]; example: "Y" |
| `visaComCardVirtualAccInd` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | enum: ["Y", "N"]; example: "Y" |
| `virtualAccFinancialLossInd` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | enum: ["Y", "N"]; example: "Y" |
| `didMerchantCancelInd` | string | no | alid in VISA Consumer Disputes Flux (Reason Code 13). | enum: ["Y", "N"]; example: "Y" |
| `merchantCancellationDate` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | format: "date"; example: "2022-05-20" |
| `nonReceiptOfTravelServicesInd` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | enum: ["Y", "N"]; example: "Y" |
| `disputeInvolveBondingAuthorityInd` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | enum: ["Y", "N"]; example: "Y" |
| `explainAttemptToResolveWithBondAuth` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | maxLength: 10000; example: "Provide an explanation of the attempt to resolve the dispute with the bonding authority/insurance scheme or where the information was obtained to confirm an insufficient bond/insurance scheme" |
| `bondAuthLetterOrAdviceDate` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | format: "date"; example: "2022-05-20" |
| `purchasedInfo` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | maxLength: 10000; example: "Provide detailed description of what was purchased and an explanation of the dispute" |
| `expectedReceiptDate` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | format: "date"; example: "2022-05-20" |
| `expectedReceiptTime` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | maxLength: 25; example: "10:30" |
| `explainDisputePriorDeliveryDate` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | maxLength: 10000; example: "Explanation of dispute initiated prior to the expected delivery date" |
| `didCardholderCancelPriorExpectedDate` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | enum: ["Y", "N"]; example: "Y" |
| `merchandiseDeliveredWrongLocation` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | enum: ["Y", "N"]; example: "Y" |
| `lateDeliveryWrongLocation` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | maxLength: 10000; example: "Provide address of the agreed location or details of late delivery" |
| `didMerchantCancelMerchandiseInd` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | enum: ["Y", "N"]; example: "Y" |
| `merchantCancelMerchandiseDate` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | example: "What was ordered and how it was damaged" |
| `merchandiseReceivedDate` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | format: "date"; example: "2022-05-20" |
| `cardholderMerchantPreviousNegotiationEvidence` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | enum: ["Y", "N"]; example: "Y" |
| `whenNegotiationsBegin` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | format: "date"; example: "2022-05-20" |
| `explainPrevNegotiation` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | maxLength: 10000; example: "Explain the previous ongoing negotiations between the cardholder and merchant." |
| `cardholderFirstNotifiedIssuerDisputeDate` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | format: "date"; example: "2022-05-20" |
| `serviceReceivedDate` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | format: "date"; example: "2022-05-20" |
| `howMerchandiseOrServiceMisrepresented` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | maxLength: 10000; example: "How was the merchandise or service misrepresented?" |
| `merchandiseServiceReceivedDate` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | format: "date"; example: "2022-05-20" |
| `explainPreNegotiation` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | example: "Explain the previous ongoing negotiations between the cardholder and merchant." |
| `orderDetailsNotAsDescribed` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | maxLength: 10000; example: "Provide details of what was ordered and not as described" |
| `merchantReceivedReturnedMerchandiseDate` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | format: "date"; example: "2022-05-20" |
| `merchantAcceptCancellationInd` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | enum: ["Y", "N"]; example: "Y" |
| `qualityOfFoodInd` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). |  |
| `purchasedInfoAndQualityIssue` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | maxLength: 10000; example: "Provide information about what was purchased and the quality issue" |
| `didCardholderPayWorkRedone` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | enum: ["Y", "N"]; example: "Y" |
| `howTermsOfContractNotHonoredByMerchant` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | maxLength: 10000; example: "Provide details how the terms of the contract were either not honored by the merchant or not as described" |
| `nonFiatCurrencyNotDelivered` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | enum: ["Y", "N"]; example: "Y" |
| `merchandiseDeliveredLate` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | enum: ["Y", "N"]; example: "Y" |
| `merchantInBankruptcyLiquidationInd` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | enum: ["Y", "N"]; example: "Y" |
| `nonFiatCurrencyNotMatching` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | enum: ["Y", "N"]; example: "Y" |
| `dispositionOfMerchandise` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | example: "a" |
| `merchantAcceptInd` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). | enum: ["Y", "N"] |
| `explainCreditIssuedLateDetailsOfNegotiations` | string | no | Valid in VISA Consumer Disputes Flux (Reason Code 13). |  |

<!-- schema: #/components/schemas/PreArbitration -->
### Schema `PreArbitration`

Pointer: `#/components/schemas/PreArbitration`. Type: object (schema `PreArbitration`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `preArbReason` | string | yes | Pre-arbitartion reason | example: "Reason for pre-aritration" |
| `newInformationInd` | string | no | New information  - `Y` or `N` | enum: ["Y", "N"]; example: "Y" |
| `newInformationDescription` | string | no | New information description | example: "New information..." |
| `issuerCertifiesCardholderContactedInd` | string | no | Issuer certifies cardholder contact | enum: ["Y", "N"] |

<!-- schema: #/components/schemas/DisputeFormType -->
### Schema `DisputeFormType`

Pointer: `#/components/schemas/DisputeFormType`. Type: object (schema `DisputeFormType`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `dispute_form_type_id` | number | no | Unique id identification |  |
| `type` | string | no | Unique type identification |  |
| `description` | string | no | Generic description |  |

<!-- schema: #/components/schemas/DisputeFraudReportDocumentStructure -->
### Schema `DisputeFraudReportDocumentStructure`

Pointer: `#/components/schemas/DisputeFraudReportDocumentStructure`. Type: object (schema `DisputeFraudReportDocumentStructure`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `acct_status` | string | yes | Account status | enum: ["ACCT_IS_OPEN", "ACCT_HAS_BEEN_CLOSED"]; example: "ACCT_IS_OPEN" |
| `chgbk_indicator` | string | yes | Is this a chargeback? true =  `1`, false = `0`. | enum: ["0", "1"]; example: "1" |
| `cvc_invalid_indicator` | string | yes | Mastercard <a href='https://developer.mastercard.com/fld-fraud-submission/documentation/parameters/annexure-1/#table-15-card-validation-code-cvc-indicator' target='_blank'>CVC invalid code indicator</a><br> | enum: ["Y", "*", "M", "N", "P", "U", "?", "E"]; example: "Y" |
| `device_type` | string | yes | Mastercard <a href='https://developer.mastercard.com/fld-fraud-submission/documentation/parameters/annexure-1/#table-3-account-device-type-codes' target='_blank'>account device type</a>.<br> | enum: ["1", "2", "3", "4", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]; example: "1" |
| `fraud_type` | string | yes | Mastercard <a href='https://developer.mastercard.com/fld-fraud-submission/documentation/parameters/annexure-1/#table-1-fraud-type-codes' target='_blank'>fraud type codes</a><br> | enum: ["00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "51", "55", "56", "57"]; example: "00" |
| `report_date` | string | yes | Fraud report date, format = yyyy-mm-dd. | example: "2021-02-11" |
| `sub_type` | string | yes | Mastercard <a href='https://developer.mastercard.com/fld-fraud-submission/documentation/parameters/annexure-1/#table-2-fraud-sub-type-codes' target='_blank'>fraud sub type codes</a><br> | enum: ["K", "N", "P", "U"]; example: "K" |
| `authorization_origin_indicator` | string | no | Authorization origin indicator, default is null. **REQUIRED** for ELO network.<br><br>  `Y` - Issuer authorized<br><br>  `X` - Parameter authorized<br><br>  `N` - Not Authorized<br><br> | enum: ["Y", "X", "N"]; minLength: 1; maxLength: 1; nullable: true; example: "Y" |
| `notification_code` | string | no | Notification type code. Default is null. **REQUIRED** for ELO network.<br><br>  `1` - First notification<br><br>  `2` - Notification sent again<br><br>  `3` - Change<br><br>  `4` - Deletion (cancellation fraud warning)<br><br>  `5` = Reactivation<br><br> | enum: ["1", "2", "3", "4", "5"]; minLength: 1; maxLength: 1; nullable: true; example: "1" |
| `exchange_indicator` | string | no | Is this an exchange? Default is `N`. **REQUIRED** for ELO network.<br><br>  `Y` - Yes<br><br>  `N` - No<br><br> | enum: ["N", "Y"]; minLength: 1; maxLength: 1; example: "N" |
| `exchange_value` | number | no | Exchange value. **REQUIRED** for ELO network. | example: 9.99 |
| `card_service_code` | string | no | Card type. **REQUIRED** for ELO network.<br><br>  `C` - Chip<br><br>  `M` - Stripe<br><br> | enum: ["C", "M"]; minLength: 1; maxLength: 1; example: "C" |

<!-- schema: #/components/schemas/CardholderVerificationMethodStructure -->
### Schema `CardholderVerificationMethodStructure`

Pointer: `#/components/schemas/CardholderVerificationMethodStructure`. Type: object (schema `CardholderVerificationMethodStructure`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `onlinePIN` | string | no | Online PIN Preferring. PIN preferring means that verficiation will first ask for a PIN.<br><br>Valid Values/Format: 1 | maxLength: 1; example: "1" |
| `offlinePIN` | string | no | Offline PIN.<br><br> Valid Values/Format: 2 | maxLength: 1; example: "2" |
| `signature` | string | no | Signature<br><br>Valid Values/Format: 3 | maxLength: 1; example: "3" |
| `none` | string | no | None (No Cardholder Verfication Method)<br><br>Valid Values/Format: 4 | maxLength: 1; example: "4" |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Card_issuing_-_Disputes.yaml` | tag `Disputes`: POST /v1/networkauthorization-disputes, GET /v1/disputes, GET /v1/disputes/{disputeId}, PUT /v1/disputes/{disputeId}, POST /v1/disputes/{disputeId}/event | https://github.com/PismoDevEx/pismo-api-specs | `5c1d5513e1f3a4d1…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-AUTH-account-and-external-id-tokens` — Endpoints that require account-specific or external-ID tokens
- `KU-CARD-card-issuing-basics` — Card issuing reference
- `KU-CARD-disputes-overview` — Disputes overview
- `KU-CARD-disputes-state-machine` — Disputes state machine
- `KU-CARD-visa-colloboration-questionaire-part-01` — Visa collaboration and allocation questionnaires (part 1 of 7)
- `KU-CARD-visa-dispute-use-case` — Visa dispute use case
- `KU-CC-disputes` — Disputes
- `KU-EVT-catalogue-disputes` — Event catalogue: disputes
- `KU-EVT-disputes-endpoint-generated-events` — Card issuing - Disputes
