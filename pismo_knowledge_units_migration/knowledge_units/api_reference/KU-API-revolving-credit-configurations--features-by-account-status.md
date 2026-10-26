---
ku_id: KU-API-revolving-credit-configurations--features-by-account-status
title: 'API reference: Revolving credit - Configurations — Features by account status'
category: api_reference
ku_type: api_reference
lifecycle: current
sources:
- path: api-specs/Revolving_credit_-_Configurations.yaml
  sha256: 5037a85683d87b9b20fa73777d80641130e25e59a6f3e80676d6996df9b88d15
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
- getFeaturesByAccountStatus
- postFeaturesByAccountStatus
- patchFeaturesByAccountStatus
related_kus:
- KU-CRED-credit-liquidation
- KU-CRED-full-balance-credit-program
- KU-ERR-codes-esmg-to-whis
- KU-ERR-codes-ex
specification_version: 2.74.0
---

# API reference: Revolving credit - Configurations — Features by account status

**KU ID:** `KU-API-revolving-credit-configurations--features-by-account-status` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 3 operation(s) tagged `Features by account status` in `api-specs/Revolving_credit_-_Configurations.yaml` (“Revolving credit - Configurations”, version `2.74.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Endpoints to toggle features on or off by account status (at program or organization level)

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `GET /v1/features-by-account-status` | `getFeaturesByAccountStatus` | List features by account status | no |
| `POST /v1/features-by-account-status` | `postFeaturesByAccountStatus` | Configure features by account status | no |
| `PATCH /v1/features-by-account-status` | `patchFeaturesByAccountStatus` | Update features by account status | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"}

## Operation contracts

<!-- op: spec=api-specs/Revolving_credit_-_Configurations.yaml method=GET path=/v1/features-by-account-status operationId=getFeaturesByAccountStatus -->
### `GET /v1/features-by-account-status` — List features by account status

- **operationId:** `getFeaturesByAccountStatus`
- **Specification:** `api-specs/Revolving_credit_-_Configurations.yaml` (Revolving credit - Configurations)
- **Server base URL(s):** `https://sandbox.pismolabs.io/credit-cycle-configurations`
- **Tags:** `Features by account status`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> List account statuses with the corresponding feature toggles at program or organization level.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `programId` | query | no | integer | Program ID | format: "int64"; example: 12345 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `FeaturesByAccountStatusResponse`) |
| 400 | Bad Request | `application/json`: object (schema `StandardErrorResponse`) |
| 404 | Not Found | `application/json`: object (schema `StandardErrorResponse`) |
| 500 | Internal Server Error | `application/json`: object (schema `StandardErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `program_id` | number | no | Program ID | format: "int64"; example: 123 |
| `account_statuses` | array of object (schema `AccountStatusItemResponse`) | yes | List of account statuses with the corresponding features marked to be disabled/enabled |  |

##### Response 400

400 Example `Missing request header or param`:

```json
{
  "code": "EX0001",
  "message": "Request header is missing: x-tenant"
}
```

##### Response 404

404 Example `Configuration not found`:

```json
{
  "code": "EX0004",
  "message": "Validation Error: Configuration not found for this organization."
}
```

##### Response 500

500 Example `Internal Server Error`:

```json
{
  "code": "GN0001",
  "message": "Generic Error"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `EX0001` | Request header is missing: x-tenant |
| 404 | `EX0004` | Validation Error: Configuration not found for this organization. |
| 500 | `GN0001` | Generic Error |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;404;500`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-CRED-full-balance-credit-program`.

<!-- op: spec=api-specs/Revolving_credit_-_Configurations.yaml method=POST path=/v1/features-by-account-status operationId=postFeaturesByAccountStatus -->
### `POST /v1/features-by-account-status` — Configure features by account status

- **operationId:** `postFeaturesByAccountStatus`
- **Specification:** `api-specs/Revolving_credit_-_Configurations.yaml` (Revolving credit - Configurations)
- **Server base URL(s):** `https://sandbox.pismolabs.io/credit-cycle-configurations`
- **Tags:** `Features by account status`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Configure features by account status at the program or organization level.
> <b>Note:</b> This only applies to full balance credit card programs.
>
> You can toggle the following features on or off for a particular account status by setting them to `true` or `false`, respectively. <b>By default, all these features are on (`true`)</b>.
> * `close-statements`: If `false`, the platform doesn't perform any cycle closings if the account has the specified status.
> * `late-payment-fee`: If `false`, the platform doesn't charge any late payment fees if the account has the specified status.
> * `overlimit`: If `false`, the platform doesn't charge any overlimit fees if the account has the specified status.
> * `create-accruals`: If `false`, the platform doesn't calculate new accruals if the account has the specified status.
>
> For example, suppose you set the `close-statements` feature to `false` for the `CANCELLED` account status for a specific program. (That is, you turn the feature off at the program level.) Then the Pismo platform won't perform any cycle closings for accounts in that status if they belong to that program.
>
> <b>Important:</b> Once the status is set to bypass the billing cycle closure and the account reaches that status, it cannot revert to a previous status. In other words, no further cycle closures can occur for this account. The change is irreversible.
>
> There are several points you should keep in mind when using this endpoint.
> * You can use this endpoint to set a feature toggle at the organization level, whether or not you have created any full balance credit programs in your organization. However, if you try to use it to set a feature toggle at the program level, and the program isn't a full balance credit card program, the endpoint throws an error.
> * If a feature is set to `true` or `false` at the program level, this overrules that feature's setting at the organization level. For example, if `close-statements` is set to `false` at the organization level and `true` at the program level, then the platform continues to perform cycle closings for accounts in the specified program. In other words, the organization level setting is ignored.
> * If a feature is not set to `true` or `false` at either the program or organization level, it defaults to `true`.
> * You can't use this endpoint to update a feature setting for an account status if it has already been configured at a particular level. For that, you need to use [Update features by account status](ref:patchfeaturesbyaccountstatus).
>
> You can use the [List statuses](ref:v4-get-account-status) endpoint to list all the account statuses defined for your organization.

#### Request body

Required: no

**Content type `application/json`** — schema: oneOf: object (schema `FeaturesByAccountStatusPostRequest`)

_oneOf option 1: schema `FeaturesByAccountStatusPostRequest`_

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `program_id` | number | no | Program ID | format: "int64"; example: 123 |
| `account_statuses` | array of object | yes | List of account statuses with the corresponding features marked to be disabled/enabled | example: [{"name": "DEFINITIVE_CANCELLATION", "features": {"close-statements": false}}] |
| `account_statuses[].name` | string | no | Account status name | example: "DEFINITIVE_CANCELLATION" |
| `account_statuses[].features` | object | no |  |  |
| `account_statuses[].features.close-statements` | boolean | no | Perform cycle closings? | default: true; example: false |
| `account_statuses[].features.late-payment-fee` | boolean | no | Charge late payment fees? | default: true; example: false |
| `account_statuses[].features.overlimit` | boolean | no | Charge overlimit fees? | default: true; example: false |
| `account_statuses[].features.create-accruals` | boolean | no | Calculate new accruals?<br> | default: true; example: false |


#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | Created |  |
| 400 | Bad Request | `application/json`: object (schema `StandardErrorResponse`) |
| 500 | Internal Server Error | `application/json`: object (schema `StandardErrorResponse`) |

##### Response 400

400 Example `Missing request header or param`:

```json
{
  "code": "EX0001",
  "message": "Request header is missing: x-tenant"
}
```

400 Example `Status not configured`:

```json
{
  "code": "WCCC011",
  "message": "Validation Error: The \"FULL_CANCELLATION\" account status was not found for this organization."
}
```

##### Response 500

500 Example `Internal Server Error`:

```json
{
  "code": "GN0001",
  "message": "Generic Error"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `EX0001` | Request header is missing: x-tenant |
| 400 | `WCCC011` | Validation Error: The "FULL_CANCELLATION" account status was not found for this organization. |
| 500 | `GN0001` | Generic Error |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `201;400;500`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-CRED-credit-liquidation`, `KU-CRED-full-balance-credit-program`.

<!-- op: spec=api-specs/Revolving_credit_-_Configurations.yaml method=PATCH path=/v1/features-by-account-status operationId=patchFeaturesByAccountStatus -->
### `PATCH /v1/features-by-account-status` — Update features by account status

- **operationId:** `patchFeaturesByAccountStatus`
- **Specification:** `api-specs/Revolving_credit_-_Configurations.yaml` (Revolving credit - Configurations)
- **Server base URL(s):** `https://sandbox.pismolabs.io/credit-cycle-configurations`
- **Tags:** `Features by account status`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Update features by account status at the program or organization level.
> <b>Note:</b> This only applies to full balance credit card programs, and only features that were previously configured using [Configure features by account status](ref:postfeaturesbyaccountstatus) can be updated using this endpoint.
>
> You can toggle the following features on or off for a particular account status by setting them to `true` or `false`, respectively. <b>By default, all these features are on (`true`)</b>. In the `FEATURES OBJECT` body parameter, `newKey`, `newKey-1`, and so on, must be one of these features.
> * `close-statements`: If `false`, the platform won't perform any cycle closings if the account has the specified status.
> * `late-payment-fee`: If `false`, the platform won't charge any late payment fees if the account has the specified status.
> * `overlimit`: If `false`, the platform won't charge any overlimit fees if the account has the specified status.
>
> When modifying an existing account status, all the features previously configured must be provided.
> <b>Note:</b> If you send a feature name that does not exist, the endpoint returns an error.
>
> A status can be removed if the `remove_status` flag is set to `true`.  
>
> The configuration can be reset if the `reset_configuration` flag is set to `true`. Resetting the configuration causes all the features to go back to their default values (`true`).
> <b>Note:</b> if you set `reset_configuration` to true, and also try to update some features for that status, the endpoint generates the following error:
> <b>Request body is missing: account_statuses field is not allowed when it is set to reset this configuration.</b>
>
> You can use the [List statuses](ref:v4-get-account-status) endpoint to list all the account statuses defined for your organization.           

#### Request body

Required: no

**Content type `application/json`** — schema: oneOf: object (schema `FeaturesByAccountStatusPatchRequest`)

_oneOf option 1: schema `FeaturesByAccountStatusPatchRequest`_

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `reset_configuration` | boolean | no | Reset configuration? | example: true |
| `program_id` | number | no | Program ID | format: "int64"; example: 123 |
| `account_statuses` | array of object (schema `AccountStatusPatchItemRequest`) | yes | List of account statuses with the corresponding features marked to be disabled/enabled |  |


#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `FeaturesByAccountStatusResponse`) |
| 400 | Bad Request | `application/json`: object (schema `StandardErrorResponse`) |
| 404 | Not Found |  |
| 500 | Internal Server Error | `application/json`: object (schema `StandardErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `program_id` | number | no | Program ID | format: "int64"; example: 123 |
| `account_statuses` | array of object (schema `AccountStatusItemResponse`) | yes | List of account statuses with the corresponding features marked to be disabled/enabled |  |

##### Response 400

400 Example `Missing request header or param`:

```json
{
  "code": "EX0001",
  "message": "Request header is missing: x-tenant"
}
```

400 Example `Status not configured`:

```json
{
  "code": "WCCC011",
  "message": "Validation Error: The \"FULL_CANCELLATION\" account status was not found for this organization."
}
```

##### Response 500

500 Example `Internal Server Error`:

```json
{
  "code": "GN0001",
  "message": "Generic Error"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `EX0001` | Request header is missing: x-tenant |
| 400 | `WCCC011` | Validation Error: The "FULL_CANCELLATION" account status was not found for this organization. |
| 500 | `GN0001` | Generic Error |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;404;500`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-CRED-full-balance-credit-program`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/AccountStatusItemResponse -->
### Schema `AccountStatusItemResponse`

Pointer: `#/components/schemas/AccountStatusItemResponse`. Type: object (schema `AccountStatusItemResponse`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `name` | string | no | Account status name | example: "FULL_CANCELLATION" |
| `features` | object | no | Map of features and the corresponding enabled/disabled status | example: {"close-statements": false, "overlimit": true} |
| `features.close-statements` | boolean | no |  |  |
| `features.overlimit` | boolean | no |  |  |
| `features.late-payment-fee` | boolean | no |  |  |

<!-- schema: #/components/schemas/StandardErrorResponse -->
### Schema `StandardErrorResponse`

Pointer: `#/components/schemas/StandardErrorResponse`. Type: object (schema `StandardErrorResponse`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string | no | Standard error code | example: "1020030" |
| `message` | string | no | Error message | example: "An error occurred when attempting to execute request." |

<!-- schema: #/components/schemas/AccountStatusPatchItemRequest -->
### Schema `AccountStatusPatchItemRequest`

Pointer: `#/components/schemas/AccountStatusPatchItemRequest`. Type: object (schema `AccountStatusPatchItemRequest`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `remove_status` | boolean | no | Remove current status? | example: true |
| `name` | string | no | Account status name | example: "FULL_CANCELLATION" |
| `features` | object (map of boolean) | no | Map of features and the corresponding enabled/disabled status | example: {"close-statements": false, "overlimit": true} |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Revolving_credit_-_Configurations.yaml` | tag `Features by account status`: GET /v1/features-by-account-status, POST /v1/features-by-account-status, PATCH /v1/features-by-account-status | https://github.com/PismoDevEx/pismo-api-specs | `5037a85683d87b9b…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-CRED-credit-liquidation` — Credit liquidation
- `KU-CRED-full-balance-credit-program` — Full balance credit programs: concepts and configuration
- `KU-ERR-codes-esmg-to-whis` — Error codes: ESMG to WHIS (30 prefixes)
- `KU-ERR-codes-ex` — Error codes: EX
