---
ku_id: KU-API-core-platform-payment-configurations--payment-method-configurations
title: 'API reference: Core platform - Payment configurations — Payment method configurations'
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
- get-config-by-tenant
- put-config-by-tenant
- post-config-by-tenant
- delete-config-by-tenant
- patch-config-by-tenant
- get-config-by-program
- put-config-by-program
- post-config-by-program
- delete-config-by-program
- patch-config-by-program
- get-config-by-account
- put-config-by-account
- post-config-by-account
- delete-config-by-account
- patch-config-by-account
- get-config-by-priority
related_kus:
- KU-CORE-commercial-cards
- KU-PAY-configure-payment-methods
- KU-PAY-payment-configurations
- KU-PAY-payment-methods
specification_version: 1.0.0
---

# API reference: Core platform - Payment configurations — Payment method configurations

**KU ID:** `KU-API-core-platform-payment-configurations--payment-method-configurations` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 16 operation(s) tagged `Payment method configurations` in `api-specs/Core_platform_-_Payment_configurations.yaml` (“Core platform - Payment configurations”, version `1.0.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Payment methods configurations endpoints.

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `GET /payment-methods-configs/v1/configs` | `get-config-by-tenant` | Get org configuration | no |
| `PUT /payment-methods-configs/v1/configs` | `put-config-by-tenant` | Replace org configuration | no |
| `POST /payment-methods-configs/v1/configs` | `post-config-by-tenant` | Create org configuration | no |
| `DELETE /payment-methods-configs/v1/configs` | `delete-config-by-tenant` | Delete org configuration | no |
| `PATCH /payment-methods-configs/v1/configs` | `patch-config-by-tenant` | Update org configuration | no |
| `GET /payment-methods-configs/v1/configs/programs/{programId}` | `get-config-by-program` | Get program configuration | no |
| `PUT /payment-methods-configs/v1/configs/programs/{programId}` | `put-config-by-program` | Replace program configuration | no |
| `POST /payment-methods-configs/v1/configs/programs/{programId}` | `post-config-by-program` | Create program configuration | no |
| `DELETE /payment-methods-configs/v1/configs/programs/{programId}` | `delete-config-by-program` | Delete program configuration | no |
| `PATCH /payment-methods-configs/v1/configs/programs/{programId}` | `patch-config-by-program` | Update program configuration | no |
| `GET /payment-methods-configs/v1/configs/accounts/{accountId}` | `get-config-by-account` | Get account configuration | no |
| `PUT /payment-methods-configs/v1/configs/accounts/{accountId}` | `put-config-by-account` | Replace account configuration | no |
| `POST /payment-methods-configs/v1/configs/accounts/{accountId}` | `post-config-by-account` | Create account configuration | no |
| `DELETE /payment-methods-configs/v1/configs/accounts/{accountId}` | `delete-config-by-account` | Delete account configuration | no |
| `PATCH /payment-methods-configs/v1/configs/accounts/{accountId}` | `patch-config-by-account` | Update account configuration | no |
| `GET /payment-methods-configs/v1/configs/priority-configs` | `get-config-by-priority` | Get configuration by hierarchy | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"} — Account access token. Tokens can expire quickly, which can result in an "Unauthorized" error.

## Operation contracts

<!-- op: spec=api-specs/Core_platform_-_Payment_configurations.yaml method=GET path=/payment-methods-configs/v1/configs operationId=get-config-by-tenant -->
### `GET /payment-methods-configs/v1/configs` — Get org configuration

- **operationId:** `get-config-by-tenant`
- **Specification:** `api-specs/Core_platform_-_Payment_configurations.yaml` (Core platform - Payment configurations)
- **Server base URL(s):** `https://sandbox.pismolabs.io`, `https://gw-pci.pismolabs.io`
- **Tags:** `Payment method configurations`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Get a payment methods configuration at the organization level. Note that the organization and account information is pulled from the access token.

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Retrieved successfully | `application/json`: object (schema `GetPaymentMethodsResponse`) |
| 400 | Bad request |  |
| 401 | Access token is missing or invalid |  |
| 403 | The request has been lost |  |
| 404 | The specified resource was not found |  |
| 500 | Internal server error |  |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `authorization` | object (schema `AuthorizationConfig`) | no | Group of configurations related to the authorization flow. |  |
| `payment` | object (schema `PaymentConfig`) | no | Group of configurations related to the payment methods flow. |  |
| `transfer` | object (schema `TransferConfig`) | no | Group of configurations related to the transfer flow. |  |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;403;404;500`, has examples `False`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-PAY-configure-payment-methods`.

<!-- op: spec=api-specs/Core_platform_-_Payment_configurations.yaml method=PUT path=/payment-methods-configs/v1/configs operationId=put-config-by-tenant -->
### `PUT /payment-methods-configs/v1/configs` — Replace org configuration

- **operationId:** `put-config-by-tenant`
- **Specification:** `api-specs/Core_platform_-_Payment_configurations.yaml` (Core platform - Payment configurations)
- **Server base URL(s):** `https://sandbox.pismolabs.io`, `https://gw-pci.pismolabs.io`
- **Tags:** `Payment method configurations`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Update a payment methods configuration at the organization level. This operation updates the entire configuration, so all fields must be sent to avoid data loss.

#### Request body

Required: yes

> Create Payment methods configuration request body.

**Content type `application/json`** — schema: object (schema `UpdatePaymentMethodsRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `authorization` | object (schema `AuthorizationConfig`) | no | Group of configurations related to the authorization flow. |  |
| `payment` | object (schema `PaymentConfig`) | no | Group of configurations related to the payment methods flow. |  |
| `transfer` | object (schema `TransferConfig`) | no | Group of configurations related to the transfer flow. |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Updated successfully | `application/json`: object (schema `UpdatePaymentMethodsResponse`) |
| 400 | Bad request |  |
| 401 | Access token is missing or invalid |  |
| 403 | The request has been lost |  |
| 404 | The specified resource was not found |  |
| 500 | Internal server error |  |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `authorization` | object (schema `AuthorizationConfig`) | no | Group of configurations related to the authorization flow. |  |
| `payment` | object (schema `PaymentConfig`) | no | Group of configurations related to the payment methods flow. |  |
| `transfer` | object (schema `TransferConfig`) | no | Group of configurations related to the transfer flow. |  |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;403;404;500`, has examples `False`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-PAY-configure-payment-methods`.

<!-- op: spec=api-specs/Core_platform_-_Payment_configurations.yaml method=POST path=/payment-methods-configs/v1/configs operationId=post-config-by-tenant -->
### `POST /payment-methods-configs/v1/configs` — Create org configuration

- **operationId:** `post-config-by-tenant`
- **Specification:** `api-specs/Core_platform_-_Payment_configurations.yaml` (Core platform - Payment configurations)
- **Server base URL(s):** `https://sandbox.pismolabs.io`, `https://gw-pci.pismolabs.io`
- **Tags:** `Payment method configurations`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Create a payment methods configuration for an authorization at the organization (org) level. This level can be used as a default configuration for all programs and accounts in this org. There can be only one org configuration. New creation attempts for the same org receive a conflict response.
>
> **Note:** This is a PCI endpoint, use the https://gw-pci.pismolabs.io environment.

#### Request body

Required: yes

> Create payment methods configuration request body.

**Content type `application/json`** — schema: object (schema `CreatePaymentMethodsConfigRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `authorization` | object (schema `AuthorizationConfig`) | no | Group of configurations related to the authorization flow. |  |
| `payment` | object (schema `PaymentConfig`) | no | Group of configurations related to the payment methods flow. |  |
| `transfer` | object (schema `TransferConfig`) | no | Group of configurations related to the transfer flow. |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | Created | `application/json`: object (schema `CreatePaymentMethodsResponse`) |
| 400 | Bad request |  |
| 401 | Access token is missing or invalid |  |
| 403 | The request has been lost |  |
| 409 | Conflict |  |
| 500 | Internal server error |  |

##### Response 201

**201 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `authorization` | object (schema `AuthorizationConfig`) | no | Group of configurations related to the authorization flow. |  |
| `payment` | object (schema `PaymentConfig`) | no | Group of configurations related to the payment methods flow. |  |
| `transfer` | object (schema `TransferConfig`) | no | Group of configurations related to the transfer flow. |  |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `201;400;401;403;409;500`, has examples `False`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-CORE-commercial-cards`, `KU-PAY-configure-payment-methods`, `KU-PAY-payment-configurations`, `KU-PAY-payment-methods`.

<!-- op: spec=api-specs/Core_platform_-_Payment_configurations.yaml method=DELETE path=/payment-methods-configs/v1/configs operationId=delete-config-by-tenant -->
### `DELETE /payment-methods-configs/v1/configs` — Delete org configuration

- **operationId:** `delete-config-by-tenant`
- **Specification:** `api-specs/Core_platform_-_Payment_configurations.yaml` (Core platform - Payment configurations)
- **Server base URL(s):** `https://sandbox.pismolabs.io`, `https://gw-pci.pismolabs.io`
- **Tags:** `Payment method configurations`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Delete a payment methods configuration at the organization level.

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

<!-- op: spec=api-specs/Core_platform_-_Payment_configurations.yaml method=PATCH path=/payment-methods-configs/v1/configs operationId=patch-config-by-tenant -->
### `PATCH /payment-methods-configs/v1/configs` — Update org configuration

- **operationId:** `patch-config-by-tenant`
- **Specification:** `api-specs/Core_platform_-_Payment_configurations.yaml` (Core platform - Payment configurations)
- **Server base URL(s):** `https://sandbox.pismolabs.io`, `https://gw-pci.pismolabs.io`
- **Tags:** `Payment method configurations`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Update a payment methods configuration at the organization level. This operation updates only the fields with the passed values.

#### Request body

Required: yes

> Update payment methods configuration request body.

**Content type `application/json`** — schema: object (schema `PatchPaymentMethodsRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `authorization` | object (schema `AuthorizationConfig`) | no | Group of configurations related to the authorization flow. |  |
| `payment` | object (schema `PaymentConfig`) | no | Group of configurations related to the payment methods flow. |  |
| `transfer` | object (schema `TransferConfig`) | no | Group of configurations related to the transfer flow. |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Updated successfully | `application/json`: object (schema `PatchPaymentMethodsResponse`) |
| 400 | Bad request |  |
| 401 | Access token is missing or invalid |  |
| 403 | The request has been lost |  |
| 404 | The specified resource was not found |  |
| 500 | Internal server error |  |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `authorization` | object (schema `AuthorizationConfig`) | no | Group of configurations related to the authorization flow. |  |
| `payment` | object (schema `PaymentConfig`) | no | Group of configurations related to the payment methods flow. |  |
| `transfer` | object (schema `TransferConfig`) | no | Group of configurations related to the transfer flow. |  |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;403;404;500`, has examples `False`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-CORE-commercial-cards`, `KU-PAY-configure-payment-methods`.

<!-- op: spec=api-specs/Core_platform_-_Payment_configurations.yaml method=GET path=/payment-methods-configs/v1/configs/programs/{programId} operationId=get-config-by-program -->
### `GET /payment-methods-configs/v1/configs/programs/{programId}` — Get program configuration

- **operationId:** `get-config-by-program`
- **Specification:** `api-specs/Core_platform_-_Payment_configurations.yaml` (Core platform - Payment configurations)
- **Server base URL(s):** `https://sandbox.pismolabs.io`, `https://gw-pci.pismolabs.io`
- **Tags:** `Payment method configurations`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Get the Payment methods configuration on the program level.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `programId` | path | yes | integer | ID of program to which to apply this configuration. |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Retrieved successfully | `application/json`: object (schema `GetPaymentMethodsResponse`) |
| 400 | Bad request |  |
| 401 | Access token is missing or invalid |  |
| 403 | The request has been lost |  |
| 404 | The specified resource was not found |  |
| 500 | Internal server error |  |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `authorization` | object (schema `AuthorizationConfig`) | no | Group of configurations related to the authorization flow. |  |
| `payment` | object (schema `PaymentConfig`) | no | Group of configurations related to the payment methods flow. |  |
| `transfer` | object (schema `TransferConfig`) | no | Group of configurations related to the transfer flow. |  |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;403;404;500`, has examples `False`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Core_platform_-_Payment_configurations.yaml method=PUT path=/payment-methods-configs/v1/configs/programs/{programId} operationId=put-config-by-program -->
### `PUT /payment-methods-configs/v1/configs/programs/{programId}` — Replace program configuration

- **operationId:** `put-config-by-program`
- **Specification:** `api-specs/Core_platform_-_Payment_configurations.yaml` (Core platform - Payment configurations)
- **Server base URL(s):** `https://sandbox.pismolabs.io`, `https://gw-pci.pismolabs.io`
- **Tags:** `Payment method configurations`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Update a payment methods configuration at the program level. This operation updates the entire configuration, so all fields must be passed to avoid data loss.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `programId` | path | yes | integer | ID of program to which to apply this configuration. |  |

#### Request body

Required: yes

> Update payment methods configuration request body

**Content type `application/json`** — schema: object (schema `UpdatePaymentMethodsRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `authorization` | object (schema `AuthorizationConfig`) | no | Group of configurations related to the authorization flow. |  |
| `payment` | object (schema `PaymentConfig`) | no | Group of configurations related to the payment methods flow. |  |
| `transfer` | object (schema `TransferConfig`) | no | Group of configurations related to the transfer flow. |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Updated successfully | `application/json`: object (schema `UpdatePaymentMethodsResponse`) |
| 400 | Bad request |  |
| 401 | Access token is missing or invalid |  |
| 403 | The request has been lost |  |
| 404 | The specified resource was not found |  |
| 500 | Internal server error |  |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `authorization` | object (schema `AuthorizationConfig`) | no | Group of configurations related to the authorization flow. |  |
| `payment` | object (schema `PaymentConfig`) | no | Group of configurations related to the payment methods flow. |  |
| `transfer` | object (schema `TransferConfig`) | no | Group of configurations related to the transfer flow. |  |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;403;404;500`, has examples `False`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Core_platform_-_Payment_configurations.yaml method=POST path=/payment-methods-configs/v1/configs/programs/{programId} operationId=post-config-by-program -->
### `POST /payment-methods-configs/v1/configs/programs/{programId}` — Create program configuration

- **operationId:** `post-config-by-program`
- **Specification:** `api-specs/Core_platform_-_Payment_configurations.yaml` (Core platform - Payment configurations)
- **Server base URL(s):** `https://sandbox.pismolabs.io`, `https://gw-pci.pismolabs.io`
- **Tags:** `Payment method configurations`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Create a payment methods configuration at the program level. This level can be used as a default configuration for all accounts in this program and at a more granular level than org. There can be only one program configuration. New creation attempts for the same program receive a conflict response.
>
> **Note:** This is a PCI endpoint, use the https://gw-pci.pismolabs.io environment.      

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `programId` | path | yes | integer | ID of program to which to apply this configuration. |  |

#### Request body

Required: yes

> Create Payment methods configuration request body

**Content type `application/json`** — schema: object (schema `CreatePaymentMethodsConfigRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `authorization` | object (schema `AuthorizationConfig`) | no | Group of configurations related to the authorization flow. |  |
| `payment` | object (schema `PaymentConfig`) | no | Group of configurations related to the payment methods flow. |  |
| `transfer` | object (schema `TransferConfig`) | no | Group of configurations related to the transfer flow. |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | Created | `application/json`: object (schema `CreatePaymentMethodsResponse`) |
| 400 | Bad request |  |
| 401 | Access token is missing or invalid |  |
| 403 | The request has been lost |  |
| 409 | Conflict |  |
| 500 | Internal server error |  |

##### Response 201

**201 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `authorization` | object (schema `AuthorizationConfig`) | no | Group of configurations related to the authorization flow. |  |
| `payment` | object (schema `PaymentConfig`) | no | Group of configurations related to the payment methods flow. |  |
| `transfer` | object (schema `TransferConfig`) | no | Group of configurations related to the transfer flow. |  |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `201;400;401;403;409;500`, has examples `False`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-PAY-configure-payment-methods`.

<!-- op: spec=api-specs/Core_platform_-_Payment_configurations.yaml method=DELETE path=/payment-methods-configs/v1/configs/programs/{programId} operationId=delete-config-by-program -->
### `DELETE /payment-methods-configs/v1/configs/programs/{programId}` — Delete program configuration

- **operationId:** `delete-config-by-program`
- **Specification:** `api-specs/Core_platform_-_Payment_configurations.yaml` (Core platform - Payment configurations)
- **Server base URL(s):** `https://sandbox.pismolabs.io`, `https://gw-pci.pismolabs.io`
- **Tags:** `Payment method configurations`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Delete a payment methods configuration at the program level.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `programId` | path | yes | integer | ID of program to which to apply this configuration. |  |

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

<!-- op: spec=api-specs/Core_platform_-_Payment_configurations.yaml method=PATCH path=/payment-methods-configs/v1/configs/programs/{programId} operationId=patch-config-by-program -->
### `PATCH /payment-methods-configs/v1/configs/programs/{programId}` — Update program configuration

- **operationId:** `patch-config-by-program`
- **Specification:** `api-specs/Core_platform_-_Payment_configurations.yaml` (Core platform - Payment configurations)
- **Server base URL(s):** `https://sandbox.pismolabs.io`, `https://gw-pci.pismolabs.io`
- **Tags:** `Payment method configurations`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Update a payment methods configuration at the program level. This operation updates only the fields with the provided values.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `programId` | path | yes | integer | ID of program to which to apply this configuration. |  |

#### Request body

Required: yes

> Update payment methods configuration request body

**Content type `application/json`** — schema: object (schema `PatchPaymentMethodsRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `authorization` | object (schema `AuthorizationConfig`) | no | Group of configurations related to the authorization flow. |  |
| `payment` | object (schema `PaymentConfig`) | no | Group of configurations related to the payment methods flow. |  |
| `transfer` | object (schema `TransferConfig`) | no | Group of configurations related to the transfer flow. |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Updated successfully | `application/json`: object (schema `PatchPaymentMethodsResponse`) |
| 400 | Bad request |  |
| 401 | Access token is missing or invalid |  |
| 403 | The request has been lost |  |
| 404 | The specified resource was not found |  |
| 500 | Internal server error |  |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `authorization` | object (schema `AuthorizationConfig`) | no | Group of configurations related to the authorization flow. |  |
| `payment` | object (schema `PaymentConfig`) | no | Group of configurations related to the payment methods flow. |  |
| `transfer` | object (schema `TransferConfig`) | no | Group of configurations related to the transfer flow. |  |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;403;404;500`, has examples `False`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Core_platform_-_Payment_configurations.yaml method=GET path=/payment-methods-configs/v1/configs/accounts/{accountId} operationId=get-config-by-account -->
### `GET /payment-methods-configs/v1/configs/accounts/{accountId}` — Get account configuration

- **operationId:** `get-config-by-account`
- **Specification:** `api-specs/Core_platform_-_Payment_configurations.yaml` (Core platform - Payment configurations)
- **Server base URL(s):** `https://sandbox.pismolabs.io`, `https://gw-pci.pismolabs.io`
- **Tags:** `Payment method configurations`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Get a payment methods configuration at the account level.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `accountId` | path | yes | integer | ID of account to which to apply the configuration. |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Retrieved successfully | `application/json`: object (schema `GetPaymentMethodsResponse`) |
| 400 | Bad request |  |
| 401 | Access token is missing or invalid |  |
| 403 | The request has been lost |  |
| 404 | The specified resource was not found |  |
| 500 | Internal server error |  |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `authorization` | object (schema `AuthorizationConfig`) | no | Group of configurations related to the authorization flow. |  |
| `payment` | object (schema `PaymentConfig`) | no | Group of configurations related to the payment methods flow. |  |
| `transfer` | object (schema `TransferConfig`) | no | Group of configurations related to the transfer flow. |  |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;403;404;500`, has examples `False`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Core_platform_-_Payment_configurations.yaml method=PUT path=/payment-methods-configs/v1/configs/accounts/{accountId} operationId=put-config-by-account -->
### `PUT /payment-methods-configs/v1/configs/accounts/{accountId}` — Replace account configuration

- **operationId:** `put-config-by-account`
- **Specification:** `api-specs/Core_platform_-_Payment_configurations.yaml` (Core platform - Payment configurations)
- **Server base URL(s):** `https://sandbox.pismolabs.io`, `https://gw-pci.pismolabs.io`
- **Tags:** `Payment method configurations`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Update a payment methods configuration at the account level. This operation updates the entire configuration, so all fields must be sent to avoid data loss.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `accountId` | path | yes | integer | ID of account to which to apply the configuration. |  |

#### Request body

Required: yes

> Update Payment methods configuration request body

**Content type `application/json`** — schema: object (schema `UpdatePaymentMethodsRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `authorization` | object (schema `AuthorizationConfig`) | no | Group of configurations related to the authorization flow. |  |
| `payment` | object (schema `PaymentConfig`) | no | Group of configurations related to the payment methods flow. |  |
| `transfer` | object (schema `TransferConfig`) | no | Group of configurations related to the transfer flow. |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Updated successfully | `application/json`: object (schema `UpdatePaymentMethodsResponse`) |
| 400 | Bad request |  |
| 401 | Access token is missing or invalid |  |
| 403 | The request has been lost |  |
| 404 | The specified resource was not found |  |
| 500 | Internal server error |  |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `authorization` | object (schema `AuthorizationConfig`) | no | Group of configurations related to the authorization flow. |  |
| `payment` | object (schema `PaymentConfig`) | no | Group of configurations related to the payment methods flow. |  |
| `transfer` | object (schema `TransferConfig`) | no | Group of configurations related to the transfer flow. |  |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;403;404;500`, has examples `False`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Core_platform_-_Payment_configurations.yaml method=POST path=/payment-methods-configs/v1/configs/accounts/{accountId} operationId=post-config-by-account -->
### `POST /payment-methods-configs/v1/configs/accounts/{accountId}` — Create account configuration

- **operationId:** `post-config-by-account`
- **Specification:** `api-specs/Core_platform_-_Payment_configurations.yaml` (Core platform - Payment configurations)
- **Server base URL(s):** `https://sandbox.pismolabs.io`, `https://gw-pci.pismolabs.io`
- **Tags:** `Payment method configurations`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Create a payment methods configuration at the account level. This is the most granular level allowed and can be used to customize a specific account. There can be only one configuration by account. New creation attempts for the same account receive a conflict response.
>
> **Note:** This is a PCI endpoint, use the https://gw-pci.pismolabs.io environment.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `accountId` | path | yes | integer | ID of account to which to apply the configuration. |  |

#### Request body

Required: yes

> Create Payment methods configuration request body

**Content type `application/json`** — schema: object (schema `CreatePaymentMethodsConfigRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `authorization` | object (schema `AuthorizationConfig`) | no | Group of configurations related to the authorization flow. |  |
| `payment` | object (schema `PaymentConfig`) | no | Group of configurations related to the payment methods flow. |  |
| `transfer` | object (schema `TransferConfig`) | no | Group of configurations related to the transfer flow. |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | Created | `application/json`: object (schema `CreatePaymentMethodsResponse`) |
| 400 | Bad request |  |
| 401 | Access token is missing or invalid |  |
| 403 | The request has been lost |  |
| 409 | Conflict |  |
| 500 | Internal server error |  |

##### Response 201

**201 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `authorization` | object (schema `AuthorizationConfig`) | no | Group of configurations related to the authorization flow. |  |
| `payment` | object (schema `PaymentConfig`) | no | Group of configurations related to the payment methods flow. |  |
| `transfer` | object (schema `TransferConfig`) | no | Group of configurations related to the transfer flow. |  |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `201;400;401;403;409;500`, has examples `False`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-PAY-configure-payment-methods`.

<!-- op: spec=api-specs/Core_platform_-_Payment_configurations.yaml method=DELETE path=/payment-methods-configs/v1/configs/accounts/{accountId} operationId=delete-config-by-account -->
### `DELETE /payment-methods-configs/v1/configs/accounts/{accountId}` — Delete account configuration

- **operationId:** `delete-config-by-account`
- **Specification:** `api-specs/Core_platform_-_Payment_configurations.yaml` (Core platform - Payment configurations)
- **Server base URL(s):** `https://sandbox.pismolabs.io`, `https://gw-pci.pismolabs.io`
- **Tags:** `Payment method configurations`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Delete a payment methods configuration at the account level.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
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

<!-- op: spec=api-specs/Core_platform_-_Payment_configurations.yaml method=PATCH path=/payment-methods-configs/v1/configs/accounts/{accountId} operationId=patch-config-by-account -->
### `PATCH /payment-methods-configs/v1/configs/accounts/{accountId}` — Update account configuration

- **operationId:** `patch-config-by-account`
- **Specification:** `api-specs/Core_platform_-_Payment_configurations.yaml` (Core platform - Payment configurations)
- **Server base URL(s):** `https://sandbox.pismolabs.io`, `https://gw-pci.pismolabs.io`
- **Tags:** `Payment method configurations`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Update a payment methods configuration at the account level. This operation updates only the fields with the provided values.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `accountId` | path | yes | integer | ID of account to which to apply the configuration. |  |

#### Request body

Required: yes

> Update payment methods configuration request body

**Content type `application/json`** — schema: object (schema `PatchPaymentMethodsRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `authorization` | object (schema `AuthorizationConfig`) | no | Group of configurations related to the authorization flow. |  |
| `payment` | object (schema `PaymentConfig`) | no | Group of configurations related to the payment methods flow. |  |
| `transfer` | object (schema `TransferConfig`) | no | Group of configurations related to the transfer flow. |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Updated successfully | `application/json`: object (schema `PatchPaymentMethodsResponse`) |
| 400 | Bad request |  |
| 401 | Access token is missing or invalid |  |
| 403 | The request has been lost |  |
| 404 | The specified resource was not found |  |
| 500 | Internal server error |  |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `authorization` | object (schema `AuthorizationConfig`) | no | Group of configurations related to the authorization flow. |  |
| `payment` | object (schema `PaymentConfig`) | no | Group of configurations related to the payment methods flow. |  |
| `transfer` | object (schema `TransferConfig`) | no | Group of configurations related to the transfer flow. |  |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;403;404;500`, has examples `False`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Core_platform_-_Payment_configurations.yaml method=GET path=/payment-methods-configs/v1/configs/priority-configs operationId=get-config-by-priority -->
### `GET /payment-methods-configs/v1/configs/priority-configs` — Get configuration by hierarchy

- **operationId:** `get-config-by-priority`
- **Specification:** `api-specs/Core_platform_-_Payment_configurations.yaml` (Core platform - Payment configurations)
- **Server base URL(s):** `https://sandbox.pismolabs.io`, `https://gw-pci.pismolabs.io`
- **Tags:** `Payment method configurations`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Get a payment methods configuration based on the hierarchy from the most granular to the least granular (account > program > org).
>
> **Note:** This is a PCI endpoint, use the https://gw-pci.pismolabs.io environment. 

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `program_id` | query | yes | integer | ID of program that the retrieved configuration is applied to. You may skip this parameter if the account ID parameter is present in the query. |  |
| `account_id` | query | yes | integer | ID of account that the retrieved configuration is applied to. You may skip this parameter if the program ID parameter is present in the query. |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Retrieved successfully | `application/json`: object (schema `GetPaymentMethodsResponse`) |
| 400 | Bad request |  |
| 401 | Access token is missing or invalid |  |
| 403 | The request has been lost |  |
| 404 | The specified resource was not found |  |
| 500 | Internal server error |  |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `authorization` | object (schema `AuthorizationConfig`) | no | Group of configurations related to the authorization flow. |  |
| `payment` | object (schema `PaymentConfig`) | no | Group of configurations related to the payment methods flow. |  |
| `transfer` | object (schema `TransferConfig`) | no | Group of configurations related to the transfer flow. |  |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;403;404;500`, has examples `False`, emits events `0`, deprecated `False`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

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

<!-- schema: #/components/schemas/PaymentConfig -->
### Schema `PaymentConfig`

Pointer: `#/components/schemas/PaymentConfig`. Type: object (schema `PaymentConfig`).

> Group of configurations related to the payment methods flow.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `require_external_authentication` | boolean | no | Does this org/program/account require a call to an external authentication entity? Default is `false`. | default: false; example: true |
| `update_balance_after_discharge` | boolean | no | If set to `true`, the platform updates account balances only after the discharge process is completed. By default, this value is `false`, and the platform updates account balances during the authorization process. This field applies to credit authorizations only. | default: false; example: true |
| `rules` | object (map of object (schema `RuleConfig`)) (schema `Rules`) | no | Validation rules performed in the payment methods flow. |  |

<!-- schema: #/components/schemas/TransferConfig -->
### Schema `TransferConfig`

Pointer: `#/components/schemas/TransferConfig`. Type: object (schema `TransferConfig`).

> Group of configurations related to the transfer flow.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `from` | object | no | Group of configurations related to the source account. |  |
| `from.require_external_authentication` | boolean | no | Does this org/program/account require a call to an external authentication entity? Default is `false`. | default: false; example: true |
| `from.rules` | object (map of object (schema `RuleConfig`)) (schema `Rules`) | no | Validation rules performed in the payment methods flow. |  |
| `to` | object | no | Group of configurations related to the target account. |  |
| `to.require_external_authentication` | boolean | no | Does this org/program/account require a call to an external authentication entity? Default is `false`. | default: false; example: true |
| `to.rules` | object (map of object (schema `RuleConfig`)) (schema `Rules`) | no | Validation rules performed in the payment methods flow. |  |

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
| `api-specs/Core_platform_-_Payment_configurations.yaml` | tag `Payment method configurations`: GET /payment-methods-configs/v1/configs, PUT /payment-methods-configs/v1/configs, POST /payment-methods-configs/v1/configs, DELETE /payment-methods-configs/v1/configs, PATCH /payment-methods-configs/v1/configs, GET /payment-methods-configs/v1/configs/programs/{programId}, PUT /payment-methods-configs/v1/configs/programs/{programId}, POST /payment-methods-configs/v1/configs/programs/{programId}, DELETE /payment-methods-configs/v1/configs/programs/{programId}, PATCH /payment-methods-configs/v1/configs/programs/{programId}, GET /payment-methods-configs/v1/configs/accounts/{accountId}, PUT /payment-methods-configs/v1/configs/accounts/{accountId}, POST /payment-methods-configs/v1/configs/accounts/{accountId}, DELETE /payment-methods-configs/v1/configs/accounts/{accountId}, PATCH /payment-methods-configs/v1/configs/accounts/{accountId}, GET /payment-methods-configs/v1/configs/priority-configs | https://github.com/PismoDevEx/pismo-api-specs | `9944fc497cfb5ecc…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-CORE-commercial-cards` — Commercial cards programs
- `KU-PAY-configure-payment-methods` — Configure payment methods
- `KU-PAY-payment-configurations` — Payment methods configurations overview
- `KU-PAY-payment-methods` — Payment methods
