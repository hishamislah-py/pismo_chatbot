---
ku_id: KU-API-platform-setup-orgs-operation--processing-codes
title: 'API reference: Platform setup - Orgs operation — Processing codes'
category: api_reference
ku_type: api_reference
lifecycle: current
sources:
- path: api-specs/Platform_setup_-_Orgs_Operation.yaml
  sha256: 28c0217338b191bd66f500ec18d4aa50e4d49a2b4e6d3045bc7643f0cda69418
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
- ProcessingCodeList
- CreateProcessingCode
- ProcessingCodeFetchByOrgsOperationId
- ProcessingCodeUpdate
related_kus:
- KU-CC-processing-codes
- KU-CORE-processing-codes-and-transaction-types
- KU-CORE-transactiontypes
- KU-EVT-catalogue-other-domains
- KU-LEND-loan-products
- KU-PAY-installments-payment
- KU-PAY-payments-configurations
- KU-SELL-managing-merchant-transactions
specification_version: v1.0
---

# API reference: Platform setup - Orgs operation — Processing codes

**KU ID:** `KU-API-platform-setup-orgs-operation--processing-codes` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 4 operation(s) tagged `Processing codes` in `api-specs/Platform_setup_-_Orgs_Operation.yaml` (“Platform setup - Orgs operation”, version `v1.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Manage processing codes

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `GET /orgs-operation/v1/processing-codes` | `ProcessingCodeList` | List processing codes | no |
| `POST /orgs-operation/v1/processing-codes` | `CreateProcessingCode` | Create processing code | no |
| `GET /orgs-operation/v1/processing-codes/{processingCode}` | `ProcessingCodeFetchByOrgsOperationId` | Get processing code | no |
| `PATCH /orgs-operation/v1/processing-codes/{processingCode}` | `ProcessingCodeUpdate` | Update processing code | no |

## Authentication

- `S2SAuthentication`: {"type": "http", "scheme": "bearer"} — All requests must be previously authenticated with an account token

## Operation contracts

<!-- op: spec=api-specs/Platform_setup_-_Orgs_Operation.yaml method=GET path=/orgs-operation/v1/processing-codes operationId=ProcessingCodeList -->
### `GET /orgs-operation/v1/processing-codes` — List processing codes

- **operationId:** `ProcessingCodeList`
- **Specification:** `api-specs/Platform_setup_-_Orgs_Operation.yaml` (Platform setup - Orgs operation)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Processing codes`
- **Deprecated in specification:** no
- **Security requirement:** `S2SAuthentication`

**Description (from the specification):**

> Get an organization's processing codes with filtering options.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `nextCursor` | query | no | string | Cursor to get next results. This is the `next_cursor` field in the response. |  |
| `limit` | query | no | string | Maximum items to return. 100 maximum. |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Sucessful response with list of processing codes | `application/json`: object (schema `GetProcessingCodesResponse`) |
| 400 | Bad request error. | `application/json`: object (schema `HTTPError`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `has_next` | boolean | no | Are there more results? |  |
| `next_cursor` | string | no | Cursor to get next results |  |
| `count` | integer | no | Number of processing codes returned |  |
| `items` | array of object (schema `GetProcessingCodeItem`) | no | Processing code items list |  |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400`, has examples `False`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-CORE-processing-codes-and-transaction-types`, `KU-PAY-payments-configurations`.

<!-- op: spec=api-specs/Platform_setup_-_Orgs_Operation.yaml method=POST path=/orgs-operation/v1/processing-codes operationId=CreateProcessingCode -->
### `POST /orgs-operation/v1/processing-codes` — Create processing code

- **operationId:** `CreateProcessingCode`
- **Specification:** `api-specs/Platform_setup_-_Orgs_Operation.yaml` (Platform setup - Orgs operation)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Processing codes`
- **Deprecated in specification:** no
- **Security requirement:** `S2SAuthentication`

**Description (from the specification):**

> Create a processing code for an organization.
>
> Processing codes identify financial operations on the Pismo platform. For example, `00` is a purchase, `01` is a withdrawal, and so on. 
>
> Processing codes need to be mapped to [transaction types](doc:transactiontypes) to create a transaction flow.
>
> This endpoint creates an `AUTHORIZATION` type processing code and generates a [Orgs operation created](https://developers.pismo.io/events/docs/orgs-operation-create-1) event.
>
> **Notes:**
>
>  * The prefix `PSM` is reserved at Pismo platform, customers are not allowed to use this prefix when creating  custom processing codes . Not all standard processing codes have the `PSM`prefix. There are codes created before this standard and are kept for backward compatibility.  New ones, however, will always have this prefix.
>  * On the Pismo platform, 2-digit processing codes are reserved and used only for network processing. Because of this, customers are not allowed to  have 2-digit custom processing codes.
>  * When a new standard processing code is created, it is replicated and configured to all platform organizations, no action is required on your part.
>  * This endpoint generates a [Orgs operation created](https://developers.pismo.io/events/docs/orgs-operation-create-1) event.
>
>
> For more information, refer to <a href="https://developers.pismo.io/pismo-docs/docs/processing-codes-and-transaction-types">Processing codes</a>.

#### Request body

Required: yes

**Content type `application/json`** — schema: object (schema `ProcessingCodeCreateRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `processing_code` | string | yes | Processing code ID<br><br>The following applies to this field:<br>  * It must have between 3 and 6 characters.<br>  * Only letters and numbers are allowed.<br>  * Must be unique and not already exist in the org's database<br>  * Cannot start with the prefix “PSM”, this is reserved for Pismo platform processing codes.<br> | minLength: 3; maxLength: 6; example: "I87654" |
| `balance_impact` | integer (schema `BalanceImpact`) | yes | Balance impact associated with processing code:<br>  * `1` - Credit <br>  * `0` - No impact. Zero balance operations have no impact. Zero balance customers are responsible for settling accounts and generating transactions.<br>  * `-1` - Debit<br> | enum: [1, 0, -1]; example: 1 |
| `description` | string (schema `PcDescription`) | yes | Processing code description | maxLength: 50 |
| `reversal_processing_code` | string (schema `ReversalProcessingCode`) | yes | Reversal processing code. Processing code for cancellation. Used in transactions and accounting flow to post the correct entries related to cancellation. <br><br>Every `AUTHORIZATION` processing code is **REQUIRED** to have a reversal and a partial reversal processing code. If a partial code isn't provided, a default one is assigned based on `balance_impact`. <br><br>The reversal processing code can either currently exist or not. If it exists, its `balance_impact` must be the opposite of the main processing code and its type must be `REVERSAL`.<br><br>For more information, refer to [default reversal processing codes](doc:processing-codes-and-transaction-types#default-reversal-processing-codes).<br> | minLength: 2; maxLength: 6; example: "578739" |
| `reversal_description` | string (schema `ReversalDescription`) | no | Reversal description. If not passed, it is automatically set to "REV " plus the `description` field.  For example, if `description` is "Purchase", the reversal description will be "REV Purchase".<br> | maxLength: 50; example: "Reversal description" |
| `partial_reversal_processing_code` | string (schema `PartialReversalProcessingCode`) | no | Partial reversal processing code. Processing code for partial reversal cancellation. Used in transactions and accounting flow to post the correct entries related to partial cancellation. <br><br>Every `AUTHORIZATION` processing code is **REQUIRED** to have a reversal and a partial reversal processing code. If a partial code isn't provided, a default one is assigned based on `balance_impact`. <br><br>For more information, refer to [default reversal processing codes](doc:processing-codes-and-transaction-types#default-reversal-processing-codes).<br> | example: "578739" |
| `partial_reversal_description` | string (schema `PartialReversalDescription`) | no | Partial reversal description. **REQUIRED** if `partial_reversal_processing_code` does not exist.<br> | maxLength: 50; example: "Partial reversal description" |
| `tags` | array of string (schema `Tags`) | no | Processing code tags.  These tags apply **ONLY** to `AUTHORIZATION` type processing codes. You cannot add tags to reverse processing codes as they may be associated with more than one authorization processing code.<br> | items.enum: ["GLOBAL", "BRAZIL", "ARGENTINA", "INDIA", "NETWORK", "VISA", "MASTERCARD", "ELO", "RUPAY", "TECBAN", "UPI", "PIX", "FPS", "TRANSACTION_BANKING", "BNPL", "LENDING", "DEPRECATED"] |
| `translations` | array of object | no |  |  |
| `translations[].language` | string (schema `TranslatedLanguage`) | no | Translation language. <br><br>For example, the code for English (United States) is `en-US`. The prefix, `en`, is a language code following the ISO 639-1 standard. The suffix, `US`, is a country code following the ISO 3166-1 Alpha-2 standard.<br> | example: "en-US" |
| `translations[].description` | string | no | Translated description | maxLength: 50 |
| `translations[].reversal_description` | string | no | Translated reversal translated description | maxLength: 50 |
| `translations[].partial_reversal_description` | string | no | Translated partial reversal description | maxLength: 50 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | Processing code sucessfully created | `application/json`: object (schema `ProcessingCodeCreateResponse`) |
| 400 | Bad request error. | `application/json`: object (schema `HTTPError`) |

##### Response 201

**201 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `processing_code` | string (schema `ProcessingCode`) | no | A processing code identifies a financial operation on the Pismo platform. Processing codes need to be mapped to transaction type codes to create a transaction flow. <br><br>A custom processing code is created with a `PENDING` status . Initially, its use is not allowed in authorizations. Once the transaction flow for a custom processing code is completely configured, its status changes to `SUCCESS` and it is ready for use. <br><br>For more information, refer to [Processing codes](doc:processing-codes-and-transaction-types)<br> |  |
| `reversal_processing_code` | string (schema `ReversalProcessingCode`) | no | Reversal processing code. Processing code for cancellation. Used in transactions and accounting flow to post the correct entries related to cancellation. <br><br>Every `AUTHORIZATION` processing code is **REQUIRED** to have a reversal and a partial reversal processing code. If a partial code isn't provided, a default one is assigned based on `balance_impact`. <br><br>The reversal processing code can either currently exist or not. If it exists, its `balance_impact` must be the opposite of the main processing code and its type must be `REVERSAL`.<br><br>For more information, refer to [default reversal processing codes](doc:processing-codes-and-transaction-types#default-reversal-processing-codes).<br> | minLength: 2; maxLength: 6; example: "578739" |
| `partial_reversal_processing_code` | string (schema `PartialReversalProcessingCode`) | no | Partial reversal processing code. Processing code for partial reversal cancellation. Used in transactions and accounting flow to post the correct entries related to partial cancellation. <br><br>Every `AUTHORIZATION` processing code is **REQUIRED** to have a reversal and a partial reversal processing code. If a partial code isn't provided, a default one is assigned based on `balance_impact`. <br><br>For more information, refer to [default reversal processing codes](doc:processing-codes-and-transaction-types#default-reversal-processing-codes).<br> | example: "578739" |
| `status` | string (schema `Status`) | no | Processing code status:<br>  * `PENDING` - Missing required configurations. A custom processing code is initially created with a `PENDING` status and its use is not allowed in authorizations. Once the transaction flow for a custom processing code is completely configured, its status changes to `SUCCESS` and it is ready for use. All standard processing codes have a `SUCCESS` status.<br><br>  * `SUCCESS` - Required configurations done<br> | enum: ["SUCCESS", "PENDING"]; example: "SUCCESS" |


#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `orgs-operation-create-1` | https://developers.pismo.io/events/docs/orgs-operation-create-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `201;400`, has examples `False`, emits events `1`, deprecated `False`.

Guides that link to this operation: `KU-CC-processing-codes`, `KU-CORE-processing-codes-and-transaction-types`, `KU-CORE-transactiontypes`, `KU-LEND-loan-products`, `KU-PAY-installments-payment`, `KU-PAY-payments-configurations`, `KU-SELL-managing-merchant-transactions`.

<!-- op: spec=api-specs/Platform_setup_-_Orgs_Operation.yaml method=GET path=/orgs-operation/v1/processing-codes/{processingCode} operationId=ProcessingCodeFetchByOrgsOperationId -->
### `GET /orgs-operation/v1/processing-codes/{processingCode}` — Get processing code

- **operationId:** `ProcessingCodeFetchByOrgsOperationId`
- **Specification:** `api-specs/Platform_setup_-_Orgs_Operation.yaml` (Platform setup - Orgs operation)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Processing codes`
- **Deprecated in specification:** no
- **Security requirement:** `S2SAuthentication`

**Description (from the specification):**

> Get details about a specific processing code.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `processingCode` | path | yes | string | Processing code ID | example: "PC0000" |
| `language` | query | no | string | Description language requested. If this field is not present or the language is not in the translation list, the default description (root description) is returned.<br><br>For example, the code for English (United States) is `en-US`. The prefix, `en`, is a language code following the ISO 639-1 standard. The suffix, `US`, is a country code following the ISO 3166-1 Alpha-2 standard.<br> | example: "en-US" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Successful response | `application/json`: object (schema `ProcessingResponse`) |
| 400 | Bad request error. | `application/json`: object (schema `HTTPError`) |
| 404 | Not found |  |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `processing_code` | string (schema `ProcessingCode`) | no | A processing code identifies a financial operation on the Pismo platform. Processing codes need to be mapped to transaction type codes to create a transaction flow. <br><br>A custom processing code is created with a `PENDING` status . Initially, its use is not allowed in authorizations. Once the transaction flow for a custom processing code is completely configured, its status changes to `SUCCESS` and it is ready for use. <br><br>For more information, refer to [Processing codes](doc:processing-codes-and-transaction-types)<br> |  |
| `org_operation_id` | integer (schema `OrgOperationID`) | no | Org operation ID |  |
| `balance_impact` | integer (schema `BalanceImpact`) | no | Balance impact associated with processing code:<br>  * `1` - Credit <br>  * `0` - No impact. Zero balance operations have no impact. Zero balance customers are responsible for settling accounts and generating transactions.<br>  * `-1` - Debit<br> | enum: [1, 0, -1]; example: 1 |
| `description` | string (schema `PcDescription`) | no | Processing code description | maxLength: 50 |
| `standard` | boolean (schema `Standard`) | no | Is this a standard processing code?  A standard processing code, as opposed to a custom one, is one that is pre-defined for every organization on the Pismo platform. <br><br>For more information, refer to [Standard processing codes](doc:processing-codes-and-transaction-types#standard-processing-codes).   <br> | example: true |
| `reversal_processing_code` | string (schema `ReversalProcessingCode`) | no | Reversal processing code. Processing code for cancellation. Used in transactions and accounting flow to post the correct entries related to cancellation. <br><br>Every `AUTHORIZATION` processing code is **REQUIRED** to have a reversal and a partial reversal processing code. If a partial code isn't provided, a default one is assigned based on `balance_impact`. <br><br>The reversal processing code can either currently exist or not. If it exists, its `balance_impact` must be the opposite of the main processing code and its type must be `REVERSAL`.<br><br>For more information, refer to [default reversal processing codes](doc:processing-codes-and-transaction-types#default-reversal-processing-codes).<br> | minLength: 2; maxLength: 6; example: "578739" |
| `partial_reversal_processing_code` | string (schema `PartialReversalProcessingCode`) | no | Partial reversal processing code. Processing code for partial reversal cancellation. Used in transactions and accounting flow to post the correct entries related to partial cancellation. <br><br>Every `AUTHORIZATION` processing code is **REQUIRED** to have a reversal and a partial reversal processing code. If a partial code isn't provided, a default one is assigned based on `balance_impact`. <br><br>For more information, refer to [default reversal processing codes](doc:processing-codes-and-transaction-types#default-reversal-processing-codes).<br> | example: "578739" |
| `status` | string (schema `Status`) | no | Processing code status:<br>  * `PENDING` - Missing required configurations. A custom processing code is initially created with a `PENDING` status and its use is not allowed in authorizations. Once the transaction flow for a custom processing code is completely configured, its status changes to `SUCCESS` and it is ready for use. All standard processing codes have a `SUCCESS` status.<br><br>  * `SUCCESS` - Required configurations done<br> | enum: ["SUCCESS", "PENDING"]; example: "SUCCESS" |
| `tags` | array of string (schema `Tags`) | no | Processing code tags.  These tags apply **ONLY** to `AUTHORIZATION` type processing codes. You cannot add tags to reverse processing codes as they may be associated with more than one authorization processing code.<br> | items.enum: ["GLOBAL", "BRAZIL", "ARGENTINA", "INDIA", "NETWORK", "VISA", "MASTERCARD", "ELO", "RUPAY", "TECBAN", "UPI", "PIX", "FPS", "TRANSACTION_BANKING", "BNPL", "LENDING", "DEPRECATED"] |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;404`, has examples `False`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Platform_setup_-_Orgs_Operation.yaml method=PATCH path=/orgs-operation/v1/processing-codes/{processingCode} operationId=ProcessingCodeUpdate -->
### `PATCH /orgs-operation/v1/processing-codes/{processingCode}` — Update processing code

- **operationId:** `ProcessingCodeUpdate`
- **Specification:** `api-specs/Platform_setup_-_Orgs_Operation.yaml` (Platform setup - Orgs operation)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Processing codes`
- **Deprecated in specification:** no
- **Security requirement:** `S2SAuthentication`

**Description (from the specification):**

> Update a processing code. Only fields passed are updated.
>
>  This endpoint generates a [Orgs operation updated](https://developers.pismo.io/events/docs/orgs-operation-update-1) event.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `processingCode` | path | yes | string | Processing code ID | example: "PC0000" |

#### Request body

Required: yes

**Content type `application/json`** — schema: object (schema `ProcessingCodeUpdateRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `description` | string (schema `PcDescription`) | no | Processing code description | maxLength: 50 |
| `reversal_processing_code` | string (schema `ReversalProcessingCode`) | no | Reversal processing code. Processing code for cancellation. Used in transactions and accounting flow to post the correct entries related to cancellation. <br><br>Every `AUTHORIZATION` processing code is **REQUIRED** to have a reversal and a partial reversal processing code. If a partial code isn't provided, a default one is assigned based on `balance_impact`. <br><br>The reversal processing code can either currently exist or not. If it exists, its `balance_impact` must be the opposite of the main processing code and its type must be `REVERSAL`.<br><br>For more information, refer to [default reversal processing codes](doc:processing-codes-and-transaction-types#default-reversal-processing-codes).<br> | minLength: 2; maxLength: 6; example: "578739" |
| `partial_reversal_processing_code` | string (schema `PartialReversalProcessingCode`) | no | Partial reversal processing code. Processing code for partial reversal cancellation. Used in transactions and accounting flow to post the correct entries related to partial cancellation. <br><br>Every `AUTHORIZATION` processing code is **REQUIRED** to have a reversal and a partial reversal processing code. If a partial code isn't provided, a default one is assigned based on `balance_impact`. <br><br>For more information, refer to [default reversal processing codes](doc:processing-codes-and-transaction-types#default-reversal-processing-codes).<br> | example: "578739" |
| `tags` | array of string (schema `Tags`) | no | Processing code tags.  These tags apply **ONLY** to `AUTHORIZATION` type processing codes. You cannot add tags to reverse processing codes as they may be associated with more than one authorization processing code.<br> | items.enum: ["GLOBAL", "BRAZIL", "ARGENTINA", "INDIA", "NETWORK", "VISA", "MASTERCARD", "ELO", "RUPAY", "TECBAN", "UPI", "PIX", "FPS", "TRANSACTION_BANKING", "BNPL", "LENDING", "DEPRECATED"] |
| `translations` | array of object (schema `Translations`) | no | Processing code descriptions translation in different languages |  |
| `translations[].language` | string (schema `TranslatedLanguage`) | no | Translation language. <br><br>For example, the code for English (United States) is `en-US`. The prefix, `en`, is a language code following the ISO 639-1 standard. The suffix, `US`, is a country code following the ISO 3166-1 Alpha-2 standard.<br> | example: "en-US" |
| `translations[].description` | string | no | Translated description | maxLength: 50 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 204 | No Content |  |
| 400 | Bad request error. | `application/json`: object (schema `HTTPError`) |
| 404 | Not Found |  |


#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `orgs-operation-update-1` | https://developers.pismo.io/events/docs/orgs-operation-update-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `204;400;404`, has examples `False`, emits events `1`, deprecated `False`.

Guides that link to this operation: `KU-PAY-payments-configurations`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/GetProcessingCodeItem -->
### Schema `GetProcessingCodeItem`

Pointer: `#/components/schemas/GetProcessingCodeItem`. Type: object (schema `GetProcessingCodeItem`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `processing_codes` | string | no | Processing code ID | example: "01" |
| `org_operation_id` | integer | no | Org operation ID |  |
| `balance_impact` | integer (schema `BalanceImpact`) | no | Balance impact associated with processing code:<br>  * `1` - Credit <br>  * `0` - No impact. Zero balance operations have no impact. Zero balance customers are responsible for settling accounts and generating transactions.<br>  * `-1` - Debit<br> | enum: [1, 0, -1]; example: 1 |
| `description` | string | no | Processing code description | example: "International purchase" |
| `standard` | boolean (schema `Standard`) | no | Is this a standard processing code?  A standard processing code, as opposed to a custom one, is one that is pre-defined for every organization on the Pismo platform. <br><br>For more information, refer to [Standard processing codes](doc:processing-codes-and-transaction-types#standard-processing-codes).   <br> | example: true |
| `reversal_processing_code` | string (schema `ReversalProcessingCode`) | no | Reversal processing code. Processing code for cancellation. Used in transactions and accounting flow to post the correct entries related to cancellation. <br><br>Every `AUTHORIZATION` processing code is **REQUIRED** to have a reversal and a partial reversal processing code. If a partial code isn't provided, a default one is assigned based on `balance_impact`. <br><br>The reversal processing code can either currently exist or not. If it exists, its `balance_impact` must be the opposite of the main processing code and its type must be `REVERSAL`.<br><br>For more information, refer to [default reversal processing codes](doc:processing-codes-and-transaction-types#default-reversal-processing-codes).<br> | minLength: 2; maxLength: 6; example: "578739" |
| `partial_reversal_processing_code` | string (schema `PartialReversalProcessingCode`) | no | Partial reversal processing code. Processing code for partial reversal cancellation. Used in transactions and accounting flow to post the correct entries related to partial cancellation. <br><br>Every `AUTHORIZATION` processing code is **REQUIRED** to have a reversal and a partial reversal processing code. If a partial code isn't provided, a default one is assigned based on `balance_impact`. <br><br>For more information, refer to [default reversal processing codes](doc:processing-codes-and-transaction-types#default-reversal-processing-codes).<br> | example: "578739" |
| `status` | string (schema `Status`) | no | Processing code status:<br>  * `PENDING` - Missing required configurations. A custom processing code is initially created with a `PENDING` status and its use is not allowed in authorizations. Once the transaction flow for a custom processing code is completely configured, its status changes to `SUCCESS` and it is ready for use. All standard processing codes have a `SUCCESS` status.<br><br>  * `SUCCESS` - Required configurations done<br> | enum: ["SUCCESS", "PENDING"]; example: "SUCCESS" |
| `tags` | array of string (schema `Tags`) | no | Processing code tags.  These tags apply **ONLY** to `AUTHORIZATION` type processing codes. You cannot add tags to reverse processing codes as they may be associated with more than one authorization processing code.<br> | items.enum: ["GLOBAL", "BRAZIL", "ARGENTINA", "INDIA", "NETWORK", "VISA", "MASTERCARD", "ELO", "RUPAY", "TECBAN", "UPI", "PIX", "FPS", "TRANSACTION_BANKING", "BNPL", "LENDING", "DEPRECATED"] |
| `translations` | array of object (schema `Translations`) | no | Processing code descriptions translation in different languages |  |
| `translations[].language` | string (schema `TranslatedLanguage`) | no | Translation language. <br><br>For example, the code for English (United States) is `en-US`. The prefix, `en`, is a language code following the ISO 639-1 standard. The suffix, `US`, is a country code following the ISO 3166-1 Alpha-2 standard.<br> | example: "en-US" |
| `translations[].description` | string | no | Translated description | maxLength: 50 |

<!-- schema: #/components/schemas/HTTPError -->
### Schema `HTTPError`

Pointer: `#/components/schemas/HTTPError`. Type: object (schema `HTTPError`).

> Code and error message.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string | no | HTTP error code |  |
| `message` | string | no | HTTP error message |  |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Platform_setup_-_Orgs_Operation.yaml` | tag `Processing codes`: GET /orgs-operation/v1/processing-codes, POST /orgs-operation/v1/processing-codes, GET /orgs-operation/v1/processing-codes/{processingCode}, PATCH /orgs-operation/v1/processing-codes/{processingCode} | https://github.com/PismoDevEx/pismo-api-specs | `28c0217338b191bd…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-CC-processing-codes` — Control Center processing codes, transaction types and general ledger accounts
- `KU-CORE-processing-codes-and-transaction-types` — Processing codes
- `KU-CORE-transactiontypes` — Transaction types
- `KU-EVT-catalogue-other-domains` — Event catalogue: other event domains (accounting, authorization, availables, average, bulletin, cash, delinquent, fraud, instantpay, intl, ledger, networktransactions, onboarding, orgs, payment, platform, programs, rules, savings, statement)
- `KU-LEND-loan-products` — Loan products: overview and creation
- `KU-PAY-installments-payment` — Installments payment
- `KU-PAY-payments-configurations` — Payments configurations
- `KU-SELL-managing-merchant-transactions` — Managing merchant transactions
