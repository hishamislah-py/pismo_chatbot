---
ku_id: KU-API-core-platform-payment-configurations--payment-method-acceptances
title: 'API reference: Core platform - Payment configurations — Payment method acceptances'
category: api_reference
ku_type: api_reference
lifecycle: current
sources:
- path: api-specs/Core_platform_-_Payment_configurations.yaml
  sha256: 9944fc497cfb5ecc02c32f99e383de5bec595941079508afac11ff36f72b38d5
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
- get-acceptance-by-tenant
- put-acceptance-by-tenant
- post-acceptance-by-tenant
- delete-acceptance-config-by-tenant
- patch-acceptance-by-tenant
- get-acceptance-by-program
- put-acceptance-by-program
- post-acceptance-by-program
- delete-acceptance-config-by-program
- patch-acceptance-by-program
- get-acceptance-by-account
- put-acceptance-by-account
- post-acceptance-by-account
- delete-acceptance-config-by-account
- patch-acceptance-by-account
- get-acceptance-by-priority
related_kus:
- KU-BANK-dated-transactions
- KU-CORE-commercial-cards
- KU-PAY-configure-payment-methods
- KU-PAY-payment-configurations
- KU-PAY-payment-methods
specification_version: 1.0.0
---

# API reference: Core platform - Payment configurations — Payment method acceptances

**KU ID:** `KU-API-core-platform-payment-configurations--payment-method-acceptances` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 16 operation(s) tagged `Payment method acceptances` in `api-specs/Core_platform_-_Payment_configurations.yaml` (“Core platform - Payment configurations”, version `1.0.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Payment methods acceptances endpoints.

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `GET /payment-methods-configs/v1/acceptances/processing-codes/{processingCode}` | `get-acceptance-by-tenant` | Get org acceptance configuration | no |
| `PUT /payment-methods-configs/v1/acceptances/processing-codes/{processingCode}` | `put-acceptance-by-tenant` | Replace org acceptance configuration | no |
| `POST /payment-methods-configs/v1/acceptances/processing-codes/{processingCode}` | `post-acceptance-by-tenant` | Create org acceptance configuration | no |
| `DELETE /payment-methods-configs/v1/acceptances/processing-codes/{processingCode}` | `delete-acceptance-config-by-tenant` | Delete org acceptance configuration | no |
| `PATCH /payment-methods-configs/v1/acceptances/processing-codes/{processingCode}` | `patch-acceptance-by-tenant` | Update org acceptance configuration | no |
| `GET /payment-methods-configs/v1/acceptances/processing-codes/{processingCode}/programs/{programId}` | `get-acceptance-by-program` | Get program acceptance configuration | no |
| `PUT /payment-methods-configs/v1/acceptances/processing-codes/{processingCode}/programs/{programId}` | `put-acceptance-by-program` | Replace program acceptance configuration | no |
| `POST /payment-methods-configs/v1/acceptances/processing-codes/{processingCode}/programs/{programId}` | `post-acceptance-by-program` | Create program acceptance configuration | no |
| `DELETE /payment-methods-configs/v1/acceptances/processing-codes/{processingCode}/programs/{programId}` | `delete-acceptance-config-by-program` | Delete program acceptance configuration | no |
| `PATCH /payment-methods-configs/v1/acceptances/processing-codes/{processingCode}/programs/{programId}` | `patch-acceptance-by-program` | Update program acceptance configuration | no |
| `GET /payment-methods-configs/v1/acceptances/processing-codes/{processingCode}/accounts/{accountId}` | `get-acceptance-by-account` | Get account acceptance configuration | no |
| `PUT /payment-methods-configs/v1/acceptances/processing-codes/{processingCode}/accounts/{accountId}` | `put-acceptance-by-account` | Replace account acceptance configuration | no |
| `POST /payment-methods-configs/v1/acceptances/processing-codes/{processingCode}/accounts/{accountId}` | `post-acceptance-by-account` | Create account acceptance configuration | no |
| `DELETE /payment-methods-configs/v1/acceptances/processing-codes/{processingCode}/accounts/{accountId}` | `delete-acceptance-config-by-account` | Delete account acceptance configuration | no |
| `PATCH /payment-methods-configs/v1/acceptances/processing-codes/{processingCode}/accounts/{accountId}` | `patch-acceptance-by-account` | Update account acceptance configuration | no |
| `GET /payment-methods-configs/v1/acceptances/processing-codes/{processing_code}/priority-configs` | `get-acceptance-by-priority` | Get acceptance configuration by hierarchy | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"} — Account access token. Tokens can expire quickly, which can result in an "Unauthorized" error.

## Operation contracts

<!-- op: spec=api-specs/Core_platform_-_Payment_configurations.yaml method=GET path=/payment-methods-configs/v1/acceptances/processing-codes/{processingCode} operationId=get-acceptance-by-tenant -->
### `GET /payment-methods-configs/v1/acceptances/processing-codes/{processingCode}` — Get org acceptance configuration

- **operationId:** `get-acceptance-by-tenant`
- **Specification:** `api-specs/Core_platform_-_Payment_configurations.yaml` (Core platform - Payment configurations)
- **Server base URL(s):** `https://sandbox.pismolabs.io`, `https://gw-pci.pismolabs.io`
- **Tags:** `Payment method acceptances`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Get acceptance configuration for a processing code operation on the organization level.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `processingCode` | path | yes | string | Processing code that defines the operation related to this acceptance configuration. |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Retrieved successfully | `application/json`: object (schema `GetAcceptanceResponse`) |
| 400 | Bad request |  |
| 401 | Access token is missing or invalid |  |
| 403 | The request has been lost |  |
| 404 | The specified resource was not found |  |
| 500 | Internal server error |  |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `processing_code` | string | no | Processing code that defines the operation related to this acceptance configuration. |  |
| `authorization` | object (schema `AuthorizationAcceptanceConfig`) | no | Group of acceptances related to the authorization flow. |  |
| `payment` | object (schema `PaymentAcceptanceConfig`) | no | Group of acceptances related to the payments flow. |  |
| `transfer` | object (schema `TransferAcceptanceConfig`) | no | Group of acceptances related to the transfer flow. |  |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;403;404;500`, has examples `False`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-PAY-configure-payment-methods`.

<!-- op: spec=api-specs/Core_platform_-_Payment_configurations.yaml method=PUT path=/payment-methods-configs/v1/acceptances/processing-codes/{processingCode} operationId=put-acceptance-by-tenant -->
### `PUT /payment-methods-configs/v1/acceptances/processing-codes/{processingCode}` — Replace org acceptance configuration

- **operationId:** `put-acceptance-by-tenant`
- **Specification:** `api-specs/Core_platform_-_Payment_configurations.yaml` (Core platform - Payment configurations)
- **Server base URL(s):** `https://sandbox.pismolabs.io`, `https://gw-pci.pismolabs.io`
- **Tags:** `Payment method acceptances`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Update acceptance configuration for a processing code operation on the organization level. This operation updates the entire configuration, so all fields must be passed to avoid data loss.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `processingCode` | path | yes | string | Processing code that defines the operation related to this acceptance configuration. |  |

#### Request body

Required: yes

> Create acceptance configuration request body.

**Content type `application/json`** — schema: object (schema `UpdateAcceptanceRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `authorization` | object (schema `AuthorizationAcceptanceConfig`) | no | Group of acceptances related to the authorization flow. |  |
| `payment` | object (schema `PaymentAcceptanceConfig`) | no | Group of acceptances related to the payments flow. |  |
| `transfer` | object (schema `TransferAcceptanceConfig`) | no | Group of acceptances related to the transfer flow. |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Updated successfully | `application/json`: object (schema `UpdateAcceptanceResponse`) |
| 400 | Bad request |  |
| 401 | Access token is missing or invalid |  |
| 403 | The request has been lost |  |
| 404 | The specified resource was not found |  |
| 500 | Internal server error |  |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `authorization` | object (schema `AuthorizationAcceptanceConfig`) | no | Group of acceptances related to the authorization flow. |  |
| `payment` | object (schema `PaymentAcceptanceConfig`) | no | Group of acceptances related to the payments flow. |  |
| `transfer` | object (schema `TransferAcceptanceConfig`) | no | Group of acceptances related to the transfer flow. |  |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;403;404;500`, has examples `False`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-PAY-configure-payment-methods`.

<!-- op: spec=api-specs/Core_platform_-_Payment_configurations.yaml method=POST path=/payment-methods-configs/v1/acceptances/processing-codes/{processingCode} operationId=post-acceptance-by-tenant -->
### `POST /payment-methods-configs/v1/acceptances/processing-codes/{processingCode}` — Create org acceptance configuration

- **operationId:** `post-acceptance-by-tenant`
- **Specification:** `api-specs/Core_platform_-_Payment_configurations.yaml` (Core platform - Payment configurations)
- **Server base URL(s):** `https://sandbox.pismolabs.io`, `https://gw-pci.pismolabs.io`
- **Tags:** `Payment method acceptances`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Create acceptance configuration for a processing code operation on the organization level. This level can be used as a default configuration for all programs and accounts in this org. There is always only one configuration by operation by org. New creation attempts for the same operation receive a conflict response.
>
> **Note:** This is a PCI endpoint, use the https://gw-pci.pismolabs.io environment.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `processingCode` | path | yes | string | Processing code that defines the operation related to this acceptance configuration. |  |

#### Request body

Required: yes

> Create acceptance configuration request body.

**Content type `application/json`** — schema: object (schema `CreateAcceptanceRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `authorization` | object (schema `AuthorizationAcceptanceConfig`) | no | Group of acceptances related to the authorization flow. |  |
| `payment` | object (schema `PaymentAcceptanceConfig`) | no | Group of acceptances related to the payments flow. |  |
| `transfer` | object (schema `TransferAcceptanceConfig`) | no | Group of acceptances related to the transfer flow. |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | Created | `application/json`: object (schema `CreateAcceptanceResponse`) |
| 400 | Bad request |  |
| 401 | Access token is missing or invalid |  |
| 403 | The request has been lost |  |
| 409 | Conflict |  |
| 500 | Internal server error |  |

##### Response 201

**201 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `authorization` | object (schema `AuthorizationAcceptanceConfig`) | no | Group of acceptances related to the authorization flow. |  |
| `payment` | object (schema `PaymentAcceptanceConfig`) | no | Group of acceptances related to the payments flow. |  |
| `transfer` | object (schema `TransferAcceptanceConfig`) | no | Group of acceptances related to the transfer flow. |  |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `201;400;401;403;409;500`, has examples `False`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-BANK-dated-transactions`, `KU-CORE-commercial-cards`, `KU-PAY-configure-payment-methods`, `KU-PAY-payment-configurations`, `KU-PAY-payment-methods`.

<!-- op: spec=api-specs/Core_platform_-_Payment_configurations.yaml method=DELETE path=/payment-methods-configs/v1/acceptances/processing-codes/{processingCode} operationId=delete-acceptance-config-by-tenant -->
### `DELETE /payment-methods-configs/v1/acceptances/processing-codes/{processingCode}` — Delete org acceptance configuration

- **operationId:** `delete-acceptance-config-by-tenant`
- **Specification:** `api-specs/Core_platform_-_Payment_configurations.yaml` (Core platform - Payment configurations)
- **Server base URL(s):** `https://sandbox.pismolabs.io`, `https://gw-pci.pismolabs.io`
- **Tags:** `Payment method acceptances`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Delete acceptance configuration for a processing code operation on the organization level.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `processingCode` | path | yes | string | Processing code that defines the operation related to this acceptance configuration. |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 204 | Successfully processed |  |
| 400 | Bad request |  |
| 401 | Access token is missing or invalid |  |
| 403 | The request has been lost |  |
| 404 | The specified resource was not found |  |
| 500 | Internal server error |  |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `204;400;401;403;404;500`, has examples `False`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Core_platform_-_Payment_configurations.yaml method=PATCH path=/payment-methods-configs/v1/acceptances/processing-codes/{processingCode} operationId=patch-acceptance-by-tenant -->
### `PATCH /payment-methods-configs/v1/acceptances/processing-codes/{processingCode}` — Update org acceptance configuration

- **operationId:** `patch-acceptance-by-tenant`
- **Specification:** `api-specs/Core_platform_-_Payment_configurations.yaml` (Core platform - Payment configurations)
- **Server base URL(s):** `https://sandbox.pismolabs.io`, `https://gw-pci.pismolabs.io`
- **Tags:** `Payment method acceptances`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Update acceptance configuration for a processing code operation on the organization level. This operation updates only the fields with the passed values.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `processingCode` | path | yes | string | Processing code that defines the operation related to this acceptance configuration. |  |

#### Request body

Required: yes

> Update acceptance configuration request body.

**Content type `application/json`** — schema: object (schema `PatchAcceptanceRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `authorization` | object (schema `AuthorizationAcceptanceConfig`) | no | Group of acceptances related to the authorization flow. |  |
| `payment` | object (schema `PaymentAcceptanceConfig`) | no | Group of acceptances related to the payments flow. |  |
| `transfer` | object (schema `TransferAcceptanceConfig`) | no | Group of acceptances related to the transfer flow. |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Updated successfully | `application/json`: object (schema `PatchAcceptanceResponse`) |
| 400 | Bad request |  |
| 401 | Access token is missing or invalid |  |
| 403 | The request has been lost |  |
| 404 | The specified resource was not found |  |
| 500 | Internal server error |  |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `authorization` | object (schema `AuthorizationAcceptanceConfig`) | no | Group of acceptances related to the authorization flow. |  |
| `payment` | object (schema `PaymentAcceptanceConfig`) | no | Group of acceptances related to the payments flow. |  |
| `transfer` | object (schema `TransferAcceptanceConfig`) | no | Group of acceptances related to the transfer flow. |  |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;403;404;500`, has examples `False`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-PAY-configure-payment-methods`.

<!-- op: spec=api-specs/Core_platform_-_Payment_configurations.yaml method=GET path=/payment-methods-configs/v1/acceptances/processing-codes/{processingCode}/programs/{programId} operationId=get-acceptance-by-program -->
### `GET /payment-methods-configs/v1/acceptances/processing-codes/{processingCode}/programs/{programId}` — Get program acceptance configuration

- **operationId:** `get-acceptance-by-program`
- **Specification:** `api-specs/Core_platform_-_Payment_configurations.yaml` (Core platform - Payment configurations)
- **Server base URL(s):** `https://sandbox.pismolabs.io`, `https://gw-pci.pismolabs.io`
- **Tags:** `Payment method acceptances`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Get acceptance configuration for a processing code operation on the program level.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `processingCode` | path | yes | string | Processing code that defines the operation related to this acceptance configuration. |  |
| `programId` | path | yes | integer | Program ID to which to apply this configuration. |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Retrieved successfully | `application/json`: object (schema `GetAcceptanceResponse`) |
| 400 | Bad request |  |
| 401 | Access token is missing or invalid |  |
| 403 | The request has been lost |  |
| 404 | The specified resource was not found |  |
| 500 | Internal server error |  |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `processing_code` | string | no | Processing code that defines the operation related to this acceptance configuration. |  |
| `authorization` | object (schema `AuthorizationAcceptanceConfig`) | no | Group of acceptances related to the authorization flow. |  |
| `payment` | object (schema `PaymentAcceptanceConfig`) | no | Group of acceptances related to the payments flow. |  |
| `transfer` | object (schema `TransferAcceptanceConfig`) | no | Group of acceptances related to the transfer flow. |  |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;403;404;500`, has examples `False`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Core_platform_-_Payment_configurations.yaml method=PUT path=/payment-methods-configs/v1/acceptances/processing-codes/{processingCode}/programs/{programId} operationId=put-acceptance-by-program -->
### `PUT /payment-methods-configs/v1/acceptances/processing-codes/{processingCode}/programs/{programId}` — Replace program acceptance configuration

- **operationId:** `put-acceptance-by-program`
- **Specification:** `api-specs/Core_platform_-_Payment_configurations.yaml` (Core platform - Payment configurations)
- **Server base URL(s):** `https://sandbox.pismolabs.io`, `https://gw-pci.pismolabs.io`
- **Tags:** `Payment method acceptances`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Update acceptance configuration for a processing code operation on the program level. This operation updates the entire configuration, so all fields must be sent to avoid data loss.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `processingCode` | path | yes | string | Processing code that defines the operation related to this acceptance configuration. |  |
| `programId` | path | yes | integer | Program ID to which to apply this configuration. |  |

#### Request body

Required: yes

> Update acceptance configuration request body

**Content type `application/json`** — schema: object (schema `UpdateAcceptanceRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `authorization` | object (schema `AuthorizationAcceptanceConfig`) | no | Group of acceptances related to the authorization flow. |  |
| `payment` | object (schema `PaymentAcceptanceConfig`) | no | Group of acceptances related to the payments flow. |  |
| `transfer` | object (schema `TransferAcceptanceConfig`) | no | Group of acceptances related to the transfer flow. |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Updated successfully | `application/json`: object (schema `UpdateAcceptanceResponse`) |
| 400 | Bad request |  |
| 401 | Access token is missing or invalid |  |
| 403 | The request has been lost |  |
| 404 | The specified resource was not found |  |
| 500 | Internal server error |  |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `authorization` | object (schema `AuthorizationAcceptanceConfig`) | no | Group of acceptances related to the authorization flow. |  |
| `payment` | object (schema `PaymentAcceptanceConfig`) | no | Group of acceptances related to the payments flow. |  |
| `transfer` | object (schema `TransferAcceptanceConfig`) | no | Group of acceptances related to the transfer flow. |  |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;403;404;500`, has examples `False`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Core_platform_-_Payment_configurations.yaml method=POST path=/payment-methods-configs/v1/acceptances/processing-codes/{processingCode}/programs/{programId} operationId=post-acceptance-by-program -->
### `POST /payment-methods-configs/v1/acceptances/processing-codes/{processingCode}/programs/{programId}` — Create program acceptance configuration

- **operationId:** `post-acceptance-by-program`
- **Specification:** `api-specs/Core_platform_-_Payment_configurations.yaml` (Core platform - Payment configurations)
- **Server base URL(s):** `https://sandbox.pismolabs.io`, `https://gw-pci.pismolabs.io`
- **Tags:** `Payment method acceptances`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Create acceptance configuration for a processing code operation on the program level. This level can be used as a default configuration for all accounts in this program and at a more granular level than org. There is always only one configuration by operation by program. New creation attempts for the same operation receive a conflict response.
>
> **Note:** This is a PCI endpoint, use the https://gw-pci.pismolabs.io environment.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `processingCode` | path | yes | string | Processing code that defines the operation related to this acceptance configuration. |  |
| `programId` | path | yes | integer | Program ID to which to apply this configuration. |  |

#### Request body

Required: yes

> Create acceptance configuration request body

**Content type `application/json`** — schema: object (schema `CreateAcceptanceRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `authorization` | object (schema `AuthorizationAcceptanceConfig`) | no | Group of acceptances related to the authorization flow. |  |
| `payment` | object (schema `PaymentAcceptanceConfig`) | no | Group of acceptances related to the payments flow. |  |
| `transfer` | object (schema `TransferAcceptanceConfig`) | no | Group of acceptances related to the transfer flow. |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | Created | `application/json`: object (schema `CreateAcceptanceResponse`) |
| 400 | Bad request |  |
| 401 | Access token is missing or invalid |  |
| 403 | The request has been lost |  |
| 409 | Conflict |  |
| 500 | Internal server error |  |

##### Response 201

**201 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `authorization` | object (schema `AuthorizationAcceptanceConfig`) | no | Group of acceptances related to the authorization flow. |  |
| `payment` | object (schema `PaymentAcceptanceConfig`) | no | Group of acceptances related to the payments flow. |  |
| `transfer` | object (schema `TransferAcceptanceConfig`) | no | Group of acceptances related to the transfer flow. |  |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `201;400;401;403;409;500`, has examples `False`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-PAY-configure-payment-methods`.

<!-- op: spec=api-specs/Core_platform_-_Payment_configurations.yaml method=DELETE path=/payment-methods-configs/v1/acceptances/processing-codes/{processingCode}/programs/{programId} operationId=delete-acceptance-config-by-program -->
### `DELETE /payment-methods-configs/v1/acceptances/processing-codes/{processingCode}/programs/{programId}` — Delete program acceptance configuration

- **operationId:** `delete-acceptance-config-by-program`
- **Specification:** `api-specs/Core_platform_-_Payment_configurations.yaml` (Core platform - Payment configurations)
- **Server base URL(s):** `https://sandbox.pismolabs.io`, `https://gw-pci.pismolabs.io`
- **Tags:** `Payment method acceptances`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Delete acceptance configuration for a processing code operation on the program level.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `processingCode` | path | yes | string | Processing code that defines the operation related to this acceptance configuration. |  |
| `programId` | path | yes | integer | Program ID to which to apply this configuration. |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 204 | Successfully processed |  |
| 400 | Bad request |  |
| 401 | Access token is missing or invalid |  |
| 403 | The request has been lost |  |
| 404 | The specified resource was not found |  |
| 500 | Internal server error |  |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `204;400;401;403;404;500`, has examples `False`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Core_platform_-_Payment_configurations.yaml method=PATCH path=/payment-methods-configs/v1/acceptances/processing-codes/{processingCode}/programs/{programId} operationId=patch-acceptance-by-program -->
### `PATCH /payment-methods-configs/v1/acceptances/processing-codes/{processingCode}/programs/{programId}` — Update program acceptance configuration

- **operationId:** `patch-acceptance-by-program`
- **Specification:** `api-specs/Core_platform_-_Payment_configurations.yaml` (Core platform - Payment configurations)
- **Server base URL(s):** `https://sandbox.pismolabs.io`, `https://gw-pci.pismolabs.io`
- **Tags:** `Payment method acceptances`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Update acceptance configuration for a processing code operation on the program level. This operation updates only the fields with the provided values.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `processingCode` | path | yes | string | Processing code that defines the operation related to this acceptance configuration. |  |
| `programId` | path | yes | integer | Program ID to which to apply this configuration. |  |

#### Request body

Required: yes

> Patch acceptance configuration request body

**Content type `application/json`** — schema: object (schema `PatchAcceptanceRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `authorization` | object (schema `AuthorizationAcceptanceConfig`) | no | Group of acceptances related to the authorization flow. |  |
| `payment` | object (schema `PaymentAcceptanceConfig`) | no | Group of acceptances related to the payments flow. |  |
| `transfer` | object (schema `TransferAcceptanceConfig`) | no | Group of acceptances related to the transfer flow. |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Updated successfully | `application/json`: object (schema `PatchAcceptanceResponse`) |
| 400 | Bad request |  |
| 401 | Access token is missing or invalid |  |
| 403 | The request has been lost |  |
| 404 | The specified resource was not found |  |
| 500 | Internal server error |  |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `authorization` | object (schema `AuthorizationAcceptanceConfig`) | no | Group of acceptances related to the authorization flow. |  |
| `payment` | object (schema `PaymentAcceptanceConfig`) | no | Group of acceptances related to the payments flow. |  |
| `transfer` | object (schema `TransferAcceptanceConfig`) | no | Group of acceptances related to the transfer flow. |  |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;403;404;500`, has examples `False`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Core_platform_-_Payment_configurations.yaml method=GET path=/payment-methods-configs/v1/acceptances/processing-codes/{processingCode}/accounts/{accountId} operationId=get-acceptance-by-account -->
### `GET /payment-methods-configs/v1/acceptances/processing-codes/{processingCode}/accounts/{accountId}` — Get account acceptance configuration

- **operationId:** `get-acceptance-by-account`
- **Specification:** `api-specs/Core_platform_-_Payment_configurations.yaml` (Core platform - Payment configurations)
- **Server base URL(s):** `https://sandbox.pismolabs.io`, `https://gw-pci.pismolabs.io`
- **Tags:** `Payment method acceptances`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Get acceptance configuration for a processing code operation on the account level.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `processingCode` | path | yes | string | Processing code that defines the operation related to this acceptance configuration. |  |
| `accountId` | path | yes | integer | ID of account to which to apply the configuration. |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Retrieved successfully | `application/json`: object (schema `GetAcceptanceResponse`) |
| 400 | Bad request |  |
| 401 | Access token is missing or invalid |  |
| 403 | The request has been lost |  |
| 404 | The specified resource was not found |  |
| 500 | Internal server error |  |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `processing_code` | string | no | Processing code that defines the operation related to this acceptance configuration. |  |
| `authorization` | object (schema `AuthorizationAcceptanceConfig`) | no | Group of acceptances related to the authorization flow. |  |
| `payment` | object (schema `PaymentAcceptanceConfig`) | no | Group of acceptances related to the payments flow. |  |
| `transfer` | object (schema `TransferAcceptanceConfig`) | no | Group of acceptances related to the transfer flow. |  |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;403;404;500`, has examples `False`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Core_platform_-_Payment_configurations.yaml method=PUT path=/payment-methods-configs/v1/acceptances/processing-codes/{processingCode}/accounts/{accountId} operationId=put-acceptance-by-account -->
### `PUT /payment-methods-configs/v1/acceptances/processing-codes/{processingCode}/accounts/{accountId}` — Replace account acceptance configuration

- **operationId:** `put-acceptance-by-account`
- **Specification:** `api-specs/Core_platform_-_Payment_configurations.yaml` (Core platform - Payment configurations)
- **Server base URL(s):** `https://sandbox.pismolabs.io`, `https://gw-pci.pismolabs.io`
- **Tags:** `Payment method acceptances`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Update acceptance configuration for a processing code operation on the account level. This operation updates the entire configuration, so all fields must be sent to avoid data loss.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `processingCode` | path | yes | string | Processing code that defines the operation related to this acceptance configuration. |  |
| `accountId` | path | yes | integer | ID of account to which to apply the configuration. |  |

#### Request body

Required: yes

> Update acceptance configuration request body

**Content type `application/json`** — schema: object (schema `UpdateAcceptanceRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `authorization` | object (schema `AuthorizationAcceptanceConfig`) | no | Group of acceptances related to the authorization flow. |  |
| `payment` | object (schema `PaymentAcceptanceConfig`) | no | Group of acceptances related to the payments flow. |  |
| `transfer` | object (schema `TransferAcceptanceConfig`) | no | Group of acceptances related to the transfer flow. |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Updated successfully | `application/json`: object (schema `UpdateAcceptanceResponse`) |
| 400 | Bad request |  |
| 401 | Access token is missing or invalid |  |
| 403 | The request has been lost |  |
| 404 | The specified resource was not found |  |
| 500 | Internal server error |  |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `authorization` | object (schema `AuthorizationAcceptanceConfig`) | no | Group of acceptances related to the authorization flow. |  |
| `payment` | object (schema `PaymentAcceptanceConfig`) | no | Group of acceptances related to the payments flow. |  |
| `transfer` | object (schema `TransferAcceptanceConfig`) | no | Group of acceptances related to the transfer flow. |  |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;403;404;500`, has examples `False`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Core_platform_-_Payment_configurations.yaml method=POST path=/payment-methods-configs/v1/acceptances/processing-codes/{processingCode}/accounts/{accountId} operationId=post-acceptance-by-account -->
### `POST /payment-methods-configs/v1/acceptances/processing-codes/{processingCode}/accounts/{accountId}` — Create account acceptance configuration

- **operationId:** `post-acceptance-by-account`
- **Specification:** `api-specs/Core_platform_-_Payment_configurations.yaml` (Core platform - Payment configurations)
- **Server base URL(s):** `https://sandbox.pismolabs.io`, `https://gw-pci.pismolabs.io`
- **Tags:** `Payment method acceptances`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Create acceptance configuration for a processing code operation on the account level. This is the most granular level allowed and can be used to customize a specific account. There is always only one configuration by operation by account. New creation attempts for the same operation receive a conflict response.
>
> **Note:** This is a PCI endpoint, use the https://gw-pci.pismolabs.io environment.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `processingCode` | path | yes | string | Processing code that defines the operation related to this acceptance configuration. |  |
| `accountId` | path | yes | integer | ID of account to which to apply the configuration. |  |

#### Request body

Required: yes

> Create acceptance configuration request body

**Content type `application/json`** — schema: object (schema `CreateAcceptanceRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `authorization` | object (schema `AuthorizationAcceptanceConfig`) | no | Group of acceptances related to the authorization flow. |  |
| `payment` | object (schema `PaymentAcceptanceConfig`) | no | Group of acceptances related to the payments flow. |  |
| `transfer` | object (schema `TransferAcceptanceConfig`) | no | Group of acceptances related to the transfer flow. |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | Created | `application/json`: object (schema `CreateAcceptanceResponse`) |
| 400 | Bad request |  |
| 401 | Access token is missing or invalid |  |
| 403 | The request has been lost |  |
| 409 | Conflict |  |
| 500 | Internal server error |  |

##### Response 201

**201 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `authorization` | object (schema `AuthorizationAcceptanceConfig`) | no | Group of acceptances related to the authorization flow. |  |
| `payment` | object (schema `PaymentAcceptanceConfig`) | no | Group of acceptances related to the payments flow. |  |
| `transfer` | object (schema `TransferAcceptanceConfig`) | no | Group of acceptances related to the transfer flow. |  |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `201;400;401;403;409;500`, has examples `False`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-PAY-configure-payment-methods`.

<!-- op: spec=api-specs/Core_platform_-_Payment_configurations.yaml method=DELETE path=/payment-methods-configs/v1/acceptances/processing-codes/{processingCode}/accounts/{accountId} operationId=delete-acceptance-config-by-account -->
### `DELETE /payment-methods-configs/v1/acceptances/processing-codes/{processingCode}/accounts/{accountId}` — Delete account acceptance configuration

- **operationId:** `delete-acceptance-config-by-account`
- **Specification:** `api-specs/Core_platform_-_Payment_configurations.yaml` (Core platform - Payment configurations)
- **Server base URL(s):** `https://sandbox.pismolabs.io`, `https://gw-pci.pismolabs.io`
- **Tags:** `Payment method acceptances`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Delete acceptance configuration for a processing code operation on the account level.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `processingCode` | path | yes | string | Processing code that defines the operation related to this acceptance configuration. |  |
| `accountId` | path | yes | integer | ID of account to which to apply the configuration. |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 204 | Successfully processed |  |
| 400 | Bad request |  |
| 401 | Access token is missing or invalid |  |
| 403 | The request has been lost |  |
| 404 | The specified resource was not found |  |
| 500 | Internal server error |  |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `204;400;401;403;404;500`, has examples `False`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Core_platform_-_Payment_configurations.yaml method=PATCH path=/payment-methods-configs/v1/acceptances/processing-codes/{processingCode}/accounts/{accountId} operationId=patch-acceptance-by-account -->
### `PATCH /payment-methods-configs/v1/acceptances/processing-codes/{processingCode}/accounts/{accountId}` — Update account acceptance configuration

- **operationId:** `patch-acceptance-by-account`
- **Specification:** `api-specs/Core_platform_-_Payment_configurations.yaml` (Core platform - Payment configurations)
- **Server base URL(s):** `https://sandbox.pismolabs.io`, `https://gw-pci.pismolabs.io`
- **Tags:** `Payment method acceptances`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Update acceptance configuration for a processing code operation on the account level. This operation updates only the fields with the provided values.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `processingCode` | path | yes | string | Processing code that defines the operation related to this acceptance configuration. |  |
| `accountId` | path | yes | integer | ID of account to which to apply the configuration. |  |

#### Request body

Required: yes

> Update acceptance configuration request body

**Content type `application/json`** — schema: object (schema `PatchAcceptanceRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `authorization` | object (schema `AuthorizationAcceptanceConfig`) | no | Group of acceptances related to the authorization flow. |  |
| `payment` | object (schema `PaymentAcceptanceConfig`) | no | Group of acceptances related to the payments flow. |  |
| `transfer` | object (schema `TransferAcceptanceConfig`) | no | Group of acceptances related to the transfer flow. |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Updated successfully | `application/json`: object (schema `PatchAcceptanceResponse`) |
| 400 | Bad request |  |
| 401 | Access token is missing or invalid |  |
| 403 | The request has been lost |  |
| 404 | The specified resource was not found |  |
| 500 | Internal server error |  |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `authorization` | object (schema `AuthorizationAcceptanceConfig`) | no | Group of acceptances related to the authorization flow. |  |
| `payment` | object (schema `PaymentAcceptanceConfig`) | no | Group of acceptances related to the payments flow. |  |
| `transfer` | object (schema `TransferAcceptanceConfig`) | no | Group of acceptances related to the transfer flow. |  |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;403;404;500`, has examples `False`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Core_platform_-_Payment_configurations.yaml method=GET path=/payment-methods-configs/v1/acceptances/processing-codes/{processing_code}/priority-configs operationId=get-acceptance-by-priority -->
### `GET /payment-methods-configs/v1/acceptances/processing-codes/{processing_code}/priority-configs` — Get acceptance configuration by hierarchy

- **operationId:** `get-acceptance-by-priority`
- **Specification:** `api-specs/Core_platform_-_Payment_configurations.yaml` (Core platform - Payment configurations)
- **Server base URL(s):** `https://sandbox.pismolabs.io`, `https://gw-pci.pismolabs.io`
- **Tags:** `Payment method acceptances`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Get acceptance configuration for a processing code operation based on the hierarchy from the most granular to the least granular (account > program > org).
>
> **Note:** This is a PCI endpoint, use the https://gw-pci.pismolabs.io environment.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `processing_code` | path | yes | string | Processing code that defines the operation related to the acceptance configuration that is being retrieved. |  |
| `program_id` | query | yes | integer | ID of program that the retrived configuration is applied to. You may skip this parameter if the account id parameter is present in the query. |  |
| `account_id` | query | yes | integer | ID of account that the retrieved configuration is applied to. You may skip this parameter if the program id parameter is present in the query. |  |
| `fetch_config` | query | no | boolean | Should authorization configurations be retrieved along with the acceptances? Default is `false`. |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Retrieved Successfully | `application/json`: object (schema `GetAcceptancePriorityResponse`) |
| 400 | Bad request |  |
| 401 | Access token is missing or invalid |  |
| 403 | The request has been lost |  |
| 404 | The specified resource was not found |  |
| 500 | Internal server error |  |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `processing_code` | string | no | Processing code that defines the operation related to this acceptance configuration. |  |
| `authorization` | object (schema `AuthorizationAcceptanceConfig`) | no | Group of acceptances related to the authorization flow. |  |
| `config` | object | no | Get Authorization configuration record response |  |
| `config.authorization` | object (schema `AuthorizationConfig`) | no | Group of configurations related to the authorization flow. |  |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;403;404;500`, has examples `False`, emits events `0`, deprecated `False`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/AuthorizationAcceptanceConfig -->
### Schema `AuthorizationAcceptanceConfig`

Pointer: `#/components/schemas/AuthorizationAcceptanceConfig`. Type: object (schema `AuthorizationAcceptanceConfig`).

> Group of acceptances related to the authorization flow.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `external_calculation_endpoint` | string | no | Endpoint that is called when there is an external integration to simulate and calculate purchases. | example: "https://yourendpoint.com" |
| `cancellation_threshold` | integer (schema `CancellationThreshold`) | no | Time in minutes this operation should be canceled after being approved and not receiving any confirmation. | default: 14400; minimum: 30; maximum: 86400; example: 1440 |
| `confirmation_verification_endpoint` | string (schema `ConfirmationVerificationEndpoint`) | no | Endpoint that is called to verify whether an authorization was confirmed or not. If this endpoint is not configured, no external verification is made and a direct confirmation call should be performed on the payment methods endpoint. | example: "https://yourverificationendpoint.com" |
| `confirmation_verification_mtls` | boolean (schema `ConfirmationVerificationMTLS`) | no | Should the confirmation verification endpoint be called using mTLS? This can only be `true` if `confirmation_verification_endpoint` and `confirmation_verification_mtls_prefix` are passed. Default is `false`. | default: false; example: true |
| `confirmation_verification_mtls_prefix` | string (schema `ConfirmationVerificationMTLSPrefix`) | no | Prefix to be used when the verification endpoint is called using mTLS. This prefix is appended to the host configured in the confirmation verification endpoint when using mTLS. The prefix can be set and is **REQUIRED**  only if `confirmation_verification_mtls` is `true` and the `confirmation_verification_endpoint` is configured. |  |
| `confirmation_verification_rate` | integer (schema `ConfirmationVerificationRate`) | no | Time in minutes the platform should call external endpoint to verify whether the authorization was captured and confirmed or not. <br>If this field is present, the verification endpoint is required to be configured.<br>This verification happens until either the authorization is confirmed or the cancel after N minutes threshold is reached.<br> | default: 60; minimum: 5; maximum: 1440; example: 30 |
| `require_external_authentication` | boolean (schema `RequireExternalAuthentication`) | no | Does this org/program/account require a call to an external authentication entity? Default is `false`. | default: false; example: true |
| `update_balance_after_discharge` | boolean (schema `UpdateBalanceAfterDischarge`) | no | If set to `true`, the platform will update the account balances only after the discharge process is completed. By default, this value is `false`, and the platform updates the account balances during the authorization process. This field applies to credit authorizations only. | default: false; example: true |
| `rules` | object (map of object (schema `RuleConfig`)) (schema `Rules`) | no | Validation rules performed in the payment methods flow. |  |

<!-- schema: #/components/schemas/PaymentAcceptanceConfig -->
### Schema `PaymentAcceptanceConfig`

Pointer: `#/components/schemas/PaymentAcceptanceConfig`. Type: object (schema `PaymentAcceptanceConfig`).

> Group of acceptances related to the payments flow.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `retroactive_payment_time_restriction` | integer (schema `RetroactivePaymentTimeRestriction`) | no | The number of days allowed for this operation be backdated. | default: 7; example: 5 |
| `require_external_authentication` | boolean (schema `RequireExternalAuthentication`) | no | Does this org/program/account require a call to an external authentication entity? Default is `false`. | default: false; example: true |
| `update_balance_after_discharge` | boolean (schema `UpdateBalanceAfterDischarge`) | no | If set to `true`, the platform will update the account balances only after the discharge process is completed. By default, this value is `false`, and the platform updates the account balances during the authorization process. This field applies to credit authorizations only. | default: false; example: true |
| `rules` | object (map of object (schema `RuleConfig`)) (schema `Rules`) | no | Validation rules performed in the payment methods flow. |  |

<!-- schema: #/components/schemas/TransferAcceptanceConfig -->
### Schema `TransferAcceptanceConfig`

Pointer: `#/components/schemas/TransferAcceptanceConfig`. Type: object (schema `TransferAcceptanceConfig`).

> Group of acceptances related to the transfer flow.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `from` | object | no | Group of acceptances related to the source account. |  |
| `from.retroactive_payment_time_restriction` | integer (schema `RetroactivePaymentTimeRestriction`) | no | The number of days allowed for this operation be backdated. | default: 7; example: 5 |
| `from.require_external_authentication` | boolean (schema `RequireExternalAuthentication`) | no | Does this org/program/account require a call to an external authentication entity? Default is `false`. | default: false; example: true |
| `from.rules` | object (map of object (schema `RuleConfig`)) (schema `Rules`) | no | Validation rules performed in the payment methods flow. |  |
| `to` | object | no | Group of acceptances related to the target account. |  |
| `to.retroactive_payment_time_restriction` | integer (schema `RetroactivePaymentTimeRestriction`) | no | The number of days allowed for this operation be backdated. | default: 7; example: 5 |
| `to.require_external_authentication` | boolean (schema `RequireExternalAuthentication`) | no | Does this org/program/account require a call to an external authentication entity? Default is `false`. | default: false; example: true |
| `to.rules` | object (map of object (schema `RuleConfig`)) (schema `Rules`) | no | Validation rules performed in the payment methods flow. |  |

<!-- schema: #/components/schemas/AuthorizationConfig -->
### Schema `AuthorizationConfig`

Pointer: `#/components/schemas/AuthorizationConfig`. Type: object (schema `AuthorizationConfig`).

> Group of configurations related to the authorization flow.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `networks` | array of object (schema `Networks`) | no | List of configurations related to a network that is processed by the Payment methods API. |  |
| `networks[].identifier` | string | no | Network identifier. This field is used to find the configuration based on the network name received in the payment methods authorization call. This field is not case-sensitive. | example: "Mastercard" |
| `networks[].hsm_keys_id` | string | no | HSM keys ID. This field is used to find the HSM keys for performing PIN validation. This value should be provided by the Pismo representative during HSM keys creation. | example: "123456" |
| `cancellation_threshold` | integer | no | Time in minutes after which to cancel the operation that has been approved but hasn't received a confirmation. | default: 14400; minimum: 30; maximum: 86400; example: 1440 |
| `confirmation_verification_endpoint` | string | no | External endpoint to call to verify whether an authorization is confirmed. If this endpoint is not configured, there is no external verification and the payment method endpoint performs a direct confirmation call. | example: "https://yourverificationendpoint.com" |
| `confirmation_verification_mtls` | boolean | no | Should the confirmation verification endpoint be called using Mutual Transport Layer Security (mTLS)? This can only be `true` if `confirmation_verification_endpoint` and `confirmation_verification_mtls_prefix` are passed. Default is `false`. | default: false; example: true |
| `confirmation_verification_mtls_prefix` | string | no | Prefix to be used when the verification endpoint is called using mTLS. This prefix is appended to the host configured in the confirmation verification endpoint when using mTLS. The prefix can be set and is **REQUIRED**  only if `confirmation_verification_mtls` is `true` and the `confirmation_verification_endpoint` is configured. | example: "url-prefix" |
| `confirmation_verification_rate` | integer | no | Time in minutes for the platform to call the external endpoint to verify whether the authorization is confirmed. This verification takes place until either the authorization is confirmed or until the number of minutes specified in this field is reached. <br>If this field is present, the `confirmation_verification_endpoint` is required.<br> | default: 60; minimum: 5; maximum: 1440; example: 30 |
| `allow_authorization_by_document_number` | boolean | no | Is org/program/account allowed to be authorized using document number as the account holder verification method? Default is `false`. | default: false; example: true |
| `require_external_authentication` | boolean | no | Does this org/program/account require a call to an external authentication entity? Default is `false`. | default: false; example: true |
| `update_balance_after_discharge` | boolean | no | If set to `true`, the platform updates account balances only after the discharge process is completed. By default, this value is `false`, and the platform updates account balances during the authorization process. This field applies to credit authorizations only. | default: false; example: true |
| `rules` | object (map of object (schema `RuleConfig`)) (schema `Rules`) | no | Validation rules performed in the payment methods flow. |  |

<!-- schema: #/components/schemas/Rules -->
### Schema `Rules`

Pointer: `#/components/schemas/Rules`. Type: object (map of object (schema `RuleConfig`)) (schema `Rules`).

> Validation rules performed in the payment methods flow.

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Core_platform_-_Payment_configurations.yaml` | tag `Payment method acceptances`: GET /payment-methods-configs/v1/acceptances/processing-codes/{processingCode}, PUT /payment-methods-configs/v1/acceptances/processing-codes/{processingCode}, POST /payment-methods-configs/v1/acceptances/processing-codes/{processingCode}, DELETE /payment-methods-configs/v1/acceptances/processing-codes/{processingCode}, PATCH /payment-methods-configs/v1/acceptances/processing-codes/{processingCode}, GET /payment-methods-configs/v1/acceptances/processing-codes/{processingCode}/programs/{programId}, PUT /payment-methods-configs/v1/acceptances/processing-codes/{processingCode}/programs/{programId}, POST /payment-methods-configs/v1/acceptances/processing-codes/{processingCode}/programs/{programId}, DELETE /payment-methods-configs/v1/acceptances/processing-codes/{processingCode}/programs/{programId}, PATCH /payment-methods-configs/v1/acceptances/processing-codes/{processingCode}/programs/{programId}, GET /payment-methods-configs/v1/acceptances/processing-codes/{processingCode}/accounts/{accountId}, PUT /payment-methods-configs/v1/acceptances/processing-codes/{processingCode}/accounts/{accountId}, POST /payment-methods-configs/v1/acceptances/processing-codes/{processingCode}/accounts/{accountId}, DELETE /payment-methods-configs/v1/acceptances/processing-codes/{processingCode}/accounts/{accountId}, PATCH /payment-methods-configs/v1/acceptances/processing-codes/{processingCode}/accounts/{accountId}, GET /payment-methods-configs/v1/acceptances/processing-codes/{processing_code}/priority-configs | https://github.com/PismoDevEx/pismo-api-specs | `9944fc497cfb5ecc…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-BANK-dated-transactions` — Business-dated and value-dated transactions
- `KU-CORE-commercial-cards` — Commercial cards programs
- `KU-PAY-configure-payment-methods` — Configure payment methods
- `KU-PAY-payment-configurations` — Payment methods configurations overview
- `KU-PAY-payment-methods` — Payment methods
