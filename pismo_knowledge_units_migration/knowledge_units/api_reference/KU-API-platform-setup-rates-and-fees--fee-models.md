---
ku_id: KU-API-platform-setup-rates-and-fees--fee-models
title: 'API reference: Platform setup - Rates and fees — Fee models'
category: api_reference
ku_type: api_reference
lifecycle: current
sources:
- path: api-specs/Platform_setup_-_Rates_and_fees.yaml
  sha256: 0a918b57bd00f81ced58e15b5d39c4f56ef2ef685442e55dc4fd59f237383ec3
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
- listModel
- postModel
- getModel
- putFeeModel
- attachmentByAccount
- getByAccount
- deleteByAccount
- attachmentByProgram
- getByProgram
- deleteAttachByProgram
- getModelByOrg
- attachmentByTenant
related_kus:
- KU-BANK-penalties-for-cd-accounts
- KU-CC-fee-models
- KU-CORE-fee-models-create-and-simulate
specification_version: 1.0.0
---

# API reference: Platform setup - Rates and fees — Fee models

**KU ID:** `KU-API-platform-setup-rates-and-fees--fee-models` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 12 operation(s) tagged `Fee models` in `api-specs/Platform_setup_-_Rates_and_fees.yaml` (“Platform setup - Rates and fees”, version `1.0.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Fee model endpoints.

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `GET /v1/fee/models` | `listModel` | List fee models | no |
| `POST /v1/fee/models` | `postModel` | Create fee model | no |
| `GET /v1/fee/models/{model_id}` | `getModel` | Get fee model | no |
| `PUT /v1/fee/models/{model_id}` | `putFeeModel` | Update fee model | no |
| `PUT /v1/fee/models/{model_id}/attachment/account/{account_id}` | `attachmentByAccount` | Attach fee model to account | no |
| `GET /v1/fee/models/attachment/account/{account_id}` | `getByAccount` | Get account fee model | no |
| `DELETE /v1/fee/models/attachment/account/{account_id}` | `deleteByAccount` | Delete account fee model | no |
| `PUT /v1/fee/models/{model_id}/attachment/program/{program_id}` | `attachmentByProgram` | Attach fee model to program | no |
| `GET /v1/fee/models/attachment/program/{program_id}` | `getByProgram` | Get program fee model | no |
| `DELETE /v1/fee/models/attachment/program/{program_id}` | `deleteAttachByProgram` | Delete program fee model | no |
| `GET /v1/fee/models/attachment/tenant` | `getModelByOrg` | Get org fee model | no |
| `PUT /v1/fee/models/{model_id}/attachment/tenant` | `attachmentByTenant` | Attach fee model to org | no |

## Authentication

- `bearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"}

## Operation contracts

<!-- op: spec=api-specs/Platform_setup_-_Rates_and_fees.yaml method=GET path=/v1/fee/models operationId=listModel -->
### `GET /v1/fee/models` — List fee models

- **operationId:** `listModel`
- **Specification:** `api-specs/Platform_setup_-_Rates_and_fees.yaml` (Platform setup - Rates and fees)
- **Server base URL(s):** `https://sandbox.pismolabs.io/rates`
- **Tags:** `Fee models`
- **Deprecated in specification:** no
- **Security requirement:** `bearerAuth`

**Description (from the specification):**

> Get an organization's fee models. The org ID is derived from the access token.

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: array of object (schema `ModelListItem`) (schema `ModelList`) |
| 400 | Bad request | `application/json`: object (schema `BadRequestError`) |
| 401 | InvalidToken | `application/json`: object (schema `Error`) |
| 500 | Internal Server Error | `application/json`: object (schema `Error`) |

##### Response 200

**200 `application/json` body fields:**

_No fields declared in the schema._


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;500`, has examples `False`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Platform_setup_-_Rates_and_fees.yaml method=POST path=/v1/fee/models operationId=postModel -->
### `POST /v1/fee/models` — Create fee model

- **operationId:** `postModel`
- **Specification:** `api-specs/Platform_setup_-_Rates_and_fees.yaml` (Platform setup - Rates and fees)
- **Server base URL(s):** `https://sandbox.pismolabs.io/rates`
- **Tags:** `Fee models`
- **Deprecated in specification:** no
- **Security requirement:** `bearerAuth`

**Description (from the specification):**

> Create fee model.
>
> A fee model is a structure that defines a collection of fees with custom calculations. You can define the method used to calculate the fee, using a fixed value or a percentage. Fee models can be applied to organizations, programs, and accounts. For more information, see the [Fee model](doc:fee-model) guide.
>
> An accumulator fee model requires you call the <a href="https://developers.pismo.io/pismo-docs/reference/post-v1-accumulator-config" target="_blank">Create accumulator configuration</a> endpoint first to define how transaction totals are kept.
>
> Once the fee model is created, it needs to be <a href="https://developers.pismo.io/pismo-docs/reference/attachmentbyaccount">attached to an account</a>, <a href="https://developers.pismo.io/pismo-docs/reference/attachmentbyprogram">attached to a program</a> or <a href="https://developers.pismo.io/pismo-docs/reference/attachmentbytenant">attached to an org</a>.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Access token, not an account-specific token. Tokens can expire quickly, which can result in an <b>401 Unauthorized</b> message<br> |  |

#### Request body

Required: yes

> Create fee model body parameters

**Content type `application/json`** — schema: object (schema `FeeModel`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `model_description` | string | yes | Model description. | minLength: 1; maxLength: 255; example: "Fee model applied to org" |
| `fees` | array of object (schema `Fee`) | yes |  |  |

Example `Calculation method Percentage`:

```json
{
  "model_description": "Fee model applied to org",
  "fees": [
    {
      "description": "Fee wdl",
      "type": "dom",
      "id": "dom_wdl",
      "deduct_from_transaction_value": false,
      "calculation_basis": "PRINCIPAL_AMOUNT",
      "calculation": {
        "calculation_method": "PERCENTAGE",
        "value": 2.5
      },
      "filters": {
        "processing_codes": [
          "02",
          "0040"
        ]
      },
      "additional_fees": [
        {
          "description": "Foreign currency surchange.",
          "id": "dom_wdl",
          "calculation": {
            "calculation_method": "PERCENTAGE",
            "value": 0.5
          },
          "type": "selios"
        }
      ]
    }
  ]
}
```

Example `Calculation method Fixed`:

```json
{
  "model_description": "Fee model to org",
  "fees": [
    {
      "description": "Fee wdl",
      "type": "dom",
      "id": "dom_wdl",
      "deduct_from_transaction_value": true,
      "calculation_basis": "PRINCIPAL_AMOUNT",
      "calculation": {
        "calculation_method": "FIXED",
        "value": 30
      },
      "filters": {
        "processing_codes": [
          "02",
          "0040"
        ]
      },
      "additional_fees": [
        {
          "description": "Foreign currency surchange.",
          "id": "dom_wdl",
          "calculation": {
            "calculation_method": "FIXED",
            "value": 10
          },
          "type": "selios"
        }
      ]
    }
  ]
}
```

Example `Calculation method IOF`:

```json
{
  "model_description": "Fee model to org",
  "fees": [
    {
      "description": "Fee wdl",
      "type": "dom",
      "id": "dom_wdl",
      "deduct_from_transaction_value": true,
      "calculation_basis": "PRINCIPAL_AMOUNT",
      "calculation": {
        "calculation_method": "IOF",
        "value": 50
      },
      "filters": {
        "processing_codes": [
          "02",
          "0040"
        ]
      },
      "additional_fees": [
        {
          "description": "Foreign currency surchange.",
          "id": "dom_wdl",
          "calculation": {
            "calculation_method": "FIXED",
            "value": 10
          },
          "type": "selios"
        }
      ]
    }
  ]
}
```

Example `Calculation method Greater`:

```json
{
  "model_description": "Fee model to org",
  "fees": [
    {
      "description": "Fee wdl",
      "type": "dom",
      "id": "dom_wdl",
      "deduct_from_transaction_value": false,
      "calculation_basis": "PRINCIPAL_AMOUNT",
      "calculation": {
        "calculation_method": "GREATER",
        "fixed": 30,
        "percentage": 2.5
      },
      "filters": {
        "processing_codes": [
          "02",
          "0040"
        ]
      },
      "additional_fees": [
        {
          "description": "Foreign currency surchange.",
          "id": "dom_wdl",
          "calculation": {
            "calculation_method": "GREATER",
            "fixed": 10,
            "percentage": 0.5
          },
          "type": "selios"
        }
      ]
    }
  ]
}
```

Example `Calculation method Daily Percentage`:

```json
{
  "model_description": "Fee model to org",
  "fees": [
    {
      "description": "Fee wdl",
      "type": "dom",
      "id": "dom_wdl",
      "deduct_from_transaction_value": true,
      "calculation_basis": "PRINCIPAL_AMOUNT",
      "calculation": {
        "calculation_method": "DAILY_PERCENTAGE",
        "value": 1.3
      },
      "filters": {
        "processing_codes": [
          "02",
          "0040"
        ]
      },
      "additional_fees": [
        {
          "description": "Foreign currency surchange.",
          "id": "dom_wdl",
          "calculation": {
            "calculation_method": "PERCENTAGE",
            "value": 0.3
          },
          "type": "selios"
        }
      ]
    }
  ]
}
```

Example `Calculation method Compound Interest`:

```json
{
  "model_description": "Fee model to org",
  "fees": [
    {
      "description": "Fee wdl",
      "type": "dom",
      "id": "dom_wdl",
      "deduct_from_transaction_value": false,
      "calculation_basis": "PRINCIPAL_AMOUNT",
      "calculation": {
        "calculation_method": "COMPOUND_INTEREST",
        "value": 1.3,
        "days_range": 30
      },
      "filters": {
        "processing_codes": [
          "02",
          "0040"
        ]
      },
      "additional_fees": [
        {
          "description": "Foreign currency surchange.",
          "id": "dom_wdl",
          "calculation": {
            "calculation_method": "FIXED",
            "value": 0.3
          },
          "type": "selios"
        }
      ]
    }
  ]
}
```

Example `Calculation method Accumulator`:

```json
{
  "model_description": "Fee model to org",
  "fees": [
    {
      "description": "Fee wdl",
      "type": "dom",
      "id": "dom_wdl",
      "deduct_from_transaction_value": false,
      "calculation_basis": "PRINCIPAL_AMOUNT",
      "calculation": {
        "calculation_method": "ACCUMULATOR",
        "index": "QUANTITY",
        "identifier": "ACC_CASH_OUT",
        "rules": [
          {
            "minimum": 10,
            "maximum": 30,
            "calculation": {
              "calculation_method": "FIXED",
              "value": 10
            }
          },
          {
            "greater_than": 30,
            "calculation": {
              "calculation_method": "FIXED",
              "value": 12
            }
          }
        ]
      },
      "filters": {
        "processing_codes": [
          "02",
          "0040"
        ]
      },
      "additional_fees": [
        {
          "description": "Foreign currency surchange.",
          "id": "dom_wdl",
          "calculation": {
            "calculation_method": "FIXED",
            "value": 0.1
          },
          "type": "selios"
        }
      ]
    }
  ]
}
```

Example `Calculation method Dynamic by amount`:

```json
{
  "model_description": "Fee model to org",
  "fees": [
    {
      "description": "Fee",
      "type": "dynamic",
      "id": "dynamic_by_amount",
      "deduct_from_transaction_value": false,
      "calculation_basis": "PRINCIPAL_AMOUNT",
      "calculation": {
        "calculation_method": "DYNAMIC_BY_AMOUNT",
        "rules": [
          {
            "minimum": 10,
            "maximum": 30,
            "calculation": {
              "calculation_method": "FIXED",
              "value": 10
            }
          },
          {
            "greater_than": 30,
            "calculation": {
              "calculation_method": "FIXED",
              "value": 12
            }
          }
        ]
      },
      "filters": {
        "processing_codes": [
          "02",
          "0040"
        ]
      }
    }
  ]
}
```

Example `Calculation method Price Table`:

```json
{
  "model_description": "Fee model to org",
  "fees": [
    {
      "description": "Fee wdl",
      "type": "dom",
      "id": "dom_wdl",
      "deduct_from_transaction_value": true,
      "calculation_basis": "PRINCIPAL_AMOUNT",
      "calculation": {
        "calculation_method": "PRICE_TABLE",
        "index": "INSTALLMENT",
        "fixed": 5,
        "percentage": 1.3,
        "fixed_iof_rate": 0.4,
        "daily_iof_rate": 0.001,
        "interest_rate": {
          "type": "DYNAMIC",
          "rules": [
            {
              "minimum": 2,
              "maximum": 12,
              "calculation": {
                "calculation_method": "PERCENTAGE",
                "value": 0.8
              }
            },
            {
              "minimum": 13,
              "maximum": 63,
              "calculation": {
                "calculation_method": "PERCENTAGE",
                "value": 0.9
              },
              "progression": {
                "value": 0.02,
                "steps": 10
              }
            },
            {
              "minimum": 64,
              "maximum": 70,
              "calculation": {
                "calculation_method": "PERCENTAGE",
                "value": 1.2
              }
            }
          ]
        }
      },
      "filters": {
        "processing_codes": [
          "02",
          "0040"
        ],
        "amount_range": {
          "minimum": 10,
          "maximum": 1000
        }
      },
      "additional_fees": [
        {
          "description": "Foreign currency surchange.",
          "id": "dom_wdl",
          "calculation": {
            "calculation_method": "PERCENTAGE",
            "value": 0.5
          },
          "type": "selios"
        }
      ]
    }
  ]
}
```

Example `Calculation method Equal Installments`:

```json
{
  "model_description": "Fee model to org",
  "fees": [
    {
      "description": "Equal Installments",
      "id": "123",
      "calculation": {
        "calculation_method": "EQUAL_INSTALLMENTS",
        "day_count_method": "MONTH_30_YEAR_360",
        "interest_rate": {
          "type": "FIXED",
          "value": 1,
          "grace_period": {
            "type": "FIXED",
            "value": 1
          },
          "precedence": 2
        },
        "fees": [
          {
            "calculation": "PERCENTAGE",
            "calculation_basis": "PRINCIPAL_AMOUNT",
            "id": "id",
            "precedence": 0,
            "value": 0.38
          },
          {
            "calculation": "IOF",
            "calculation_basis": "PRINCIPAL_AMOUNT",
            "id": "id",
            "precedence": 1,
            "fixed_iof_rate": 3.5,
            "daily_iof_rate": 0.0082
          }
        ]
      },
      "filters": {
        "processing_codes": [
          "02",
          "0040"
        ],
        "amount_range": {
          "minimum": 10,
          "maximum": 1000
        }
      }
    }
  ]
}
```

Example `Calculation method Aging`:

```json
{
  "model_description": "Fee model applied to org",
  "fees": [
    {
      "description": "Fee wdl",
      "type": "dom",
      "id": "dom_wdl",
      "deduct_from_transaction_value": true,
      "calculation_basis": "PRINCIPAL_AMOUNT",
      "calculation": {
        "calculation_method": "AGING",
        "index": "DAY",
        "rate": {
          "type": "DYNAMIC",
          "rules": [
            {
              "minimum": 1,
              "maximum": 30,
              "calculation": {
                "calculation_method": "PERCENTAGE",
                "value": 1.5
              }
            },
            {
              "minimum": 31,
              "maximum": 180,
              "calculation": {
                "calculation_method": "PERCENTAGE",
                "value": 3.5
              },
              "progression": {
                "value": 0.5,
                "steps": 10
              }
            },
            {
              "minimum": 181,
              "maximum": 360,
              "calculation": {
                "calculation_method": "PERCENTAGE",
                "value": 10
              }
            },
            {
              "greater_than": 360,
              "calculation": {
                "calculation_method": "PERCENTAGE",
                "value": 12
              }
            }
          ]
        }
      },
      "filters": {
        "processing_codes": [
          "02",
          "0040"
        ],
        "amount_range": {
          "minimum": 10,
          "maximum": 1000
        }
      },
      "additional_fees": [
        {
          "description": "Foreign currency surchange.",
          "id": "dom_wdl",
          "calculation": {
            "calculation_method": "PERCENTAGE",
            "value": 0.5
          },
          "type": "selios"
        }
      ]
    }
  ]
}
```

Example `Calculation method Constant Repayment`:

```json
{
  "model_description": "Fee model applied to org",
  "fees": [
    {
      "description": "Fee wdl",
      "type": "dom",
      "id": "dom_wdl",
      "deduct_from_transaction_value": false,
      "calculation_basis": "PRINCIPAL_AMOUNT",
      "precedence": 1,
      "calculation": {
        "calculation_method": "CONSTANT_REPAYMENT",
        "day_count_method": "MONTH_30_YEAR_360",
        "payment_postponement_rules": {
          "basis": "INTEREST",
          "cycles": "1"
        },
        "interest_rate": {
          "type": "FIXED",
          "index": "INSTALLMENT",
          "id": "test",
          "value": 12,
          "precedence": 3,
          "rules": [
            {
              "minimum": 2,
              "maximum": 70,
              "calculation": {
                "calculation_method": "PERCENTAGE",
                "value": 22.5
              }
            }
          ]
        },
        "fees": [
          {
            "calculation": "FIXED",
            "id": "tax1",
            "precedence": 1,
            "value": 10,
            "calculation_basis": "PRINCIPAL_AMOUNT"
          },
          {
            "calculation": "PERCENTAGE",
            "id": "tax2",
            "precedence": 2,
            "value": 12,
            "calculation_basis": "CONTRACT_AMOUNT"
          }
        ]
      },
      "filters": {
        "processing_codes": [
          "02",
          "0040"
        ]
      },
      "additional_fees": [
        {
          "description": "Foreign currency surchange.",
          "id": "dom_wdl",
          "calculation": {
            "calculation_method": "PERCENTAGE",
            "value": 0.5
          },
          "type": "selios"
        }
      ]
    }
  ]
}
```

Example `Calculation method Built In`:

```json
{
  "model_description": "Fee model applied to org",
  "fees": [
    {
      "description": "Fee wdl",
      "type": "dom",
      "id": "dom_wdl",
      "deduct_from_transaction_value": false,
      "calculation_basis": "PRINCIPAL_AMOUNT",
      "precedence": 0,
      "calculation": {
        "calculation_method": "BUILT_IN",
        "value": 1.3
      },
      "filters": {
        "processing_codes": [
          "02",
          "0040"
        ]
      }
    }
  ]
}
```

Example `Calculation method Percentage with all filters filled` (Calculation method Percentage with all filters filled):

```json
{
  "model_description": "Fee model with all filters (required and optional) filled",
  "fees": [
    {
      "description": "Fee wdl",
      "type": "dom",
      "id": "dom_wdl",
      "deduct_from_transaction_value": false,
      "calculation_basis": "PRINCIPAL_AMOUNT",
      "calculation": {
        "calculation_method": "PERCENTAGE",
        "value": 2.5
      },
      "filters": {
        "processing_codes": [
          "02",
          "0040"
        ],
        "amount_range": {
          "minimum": 10,
          "maximum": 1000
        },
        "operation_types": [
          "AUTHORIZATION",
          "CONFIRMATION"
        ]
      }
    }
  ]
}
```

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | OK | `application/json`: object (schema `ModelAttachmentResponse`) |
| 400 | Bad request - the fee model payload is invalid. The response body depends on the validation that failed:<br>* Schema validation (body that is not valid JSON, missing field, wrong type, invalid calculation structure) - list with each invalid field and the violated rule.<br>* Business rule validation across fees (`RCAPI-VALIDATION-ERROR`) - error object with the list of invalid fields and violated rules in `errors`.<br>* Request that cannot be bound, or invalid `model_id` on update (`RCAPI-INVALID-REQUEST-PAYLOAD`) - error object with code and message.<br> | `application/json`: anyOf: array of object (schema `HTTPErrors`), object (schema `ValidationErrorResponse`), object (schema `BadRequestError`) |
| 401 | InvalidToken | `application/json`: object (schema `Error`) |
| 500 | Internal Server Error | `application/json`: object (schema `Error`) |

##### Response 201

**201 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `model_id` | string (schema `ModelID`) | no | Pismo fee model ID | format: "uuid"; example: "d290f1ee-6c54-4b01-90e6-d701748f0851" |

##### Response 400

400 Example `Schema validation`:

```json
[
  {
    "field": "body.fees.0.calculation",
    "violation": "Must validate one and only one schema (oneOf)"
  },
  {
    "field": "body.fees.0.calculation.rules.0",
    "violation": "Must validate one and only one schema (oneOf)"
  },
  {
    "field": "body.fees.0.calculation.rules.0.calculation",
    "violation": "value is required"
  }
]
```

400 Example `Business rule validation`:

```json
{
  "error_code": "RCAPI-VALIDATION-ERROR",
  "message": "Request validation failed",
  "errors": [
    {
      "field": "body.fees[1].filters.amount_range.minimum",
      "violation": "Fees contain overlapping amount ranges"
    }
  ]
}
```

400 Example `Invalid request payload`:

```json
{
  "error_code": "RCAPI-INVALID-REQUEST-PAYLOAD",
  "message": "The request payload is invalid"
}
```


Catalogue row (api-reference-data/operations_catalog.csv): response codes `201;400;401;500`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-BANK-penalties-for-cd-accounts`, `KU-CC-fee-models`, `KU-CORE-fee-models-create-and-simulate`.

<!-- op: spec=api-specs/Platform_setup_-_Rates_and_fees.yaml method=GET path=/v1/fee/models/{model_id} operationId=getModel -->
### `GET /v1/fee/models/{model_id}` — Get fee model

- **operationId:** `getModel`
- **Specification:** `api-specs/Platform_setup_-_Rates_and_fees.yaml` (Platform setup - Rates and fees)
- **Server base URL(s):** `https://sandbox.pismolabs.io/rates`
- **Tags:** `Fee models`
- **Deprecated in specification:** no
- **Security requirement:** `bearerAuth`

**Description (from the specification):**

> Get a fee model given its ID in the path.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `model_id` | path | yes | string | Fee model ID |  |
| `Authorization` | header | yes | string | Access token, not an account-specific token. Tokens can expire quickly, which can result in an <b>401 Unauthorized</b> message<br> |  |
| `withAttachmentsResume` | query | no | boolean | Allows you to add information relating to model attachments to the query result | default: false |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `FeeModel`) |
| 400 | Bad request | `application/json`: object (schema `BadRequestError`) |
| 401 | InvalidToken | `application/json`: object (schema `Error`) |
| 404 | Fee model not found | `application/json`: object (schema `NotFoundModelError`) |
| 500 | Internal Server Error | `application/json`: object (schema `Error`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `model_description` | string | yes | Model description. | minLength: 1; maxLength: 255; example: "Fee model applied to org" |
| `fees` | array of object (schema `Fee`) | yes |  |  |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;404;500`, has examples `False`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Platform_setup_-_Rates_and_fees.yaml method=PUT path=/v1/fee/models/{model_id} operationId=putFeeModel -->
### `PUT /v1/fee/models/{model_id}` — Update fee model

- **operationId:** `putFeeModel`
- **Specification:** `api-specs/Platform_setup_-_Rates_and_fees.yaml` (Platform setup - Rates and fees)
- **Server base URL(s):** `https://sandbox.pismolabs.io/rates`
- **Tags:** `Fee models`
- **Deprecated in specification:** no
- **Security requirement:** `bearerAuth`

**Description (from the specification):**

> Update a fee model

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `model_id` | path | yes | string | Fee model ID |  |

#### Request body

Required: yes

> Update fee model

**Content type `application/json`** — schema: object (schema `FeeModel`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `model_description` | string | yes | Model description. | minLength: 1; maxLength: 255; example: "Fee model applied to org" |
| `fees` | array of object (schema `Fee`) | yes |  |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK |  |
| 400 | Bad request - the fee model payload is invalid. The response body depends on the validation that failed:<br>* Schema validation (body that is not valid JSON, missing field, wrong type, invalid calculation structure) - list with each invalid field and the violated rule.<br>* Business rule validation across fees (`RCAPI-VALIDATION-ERROR`) - error object with the list of invalid fields and violated rules in `errors`.<br>* Request that cannot be bound, or invalid `model_id` on update (`RCAPI-INVALID-REQUEST-PAYLOAD`) - error object with code and message.<br> | `application/json`: anyOf: array of object (schema `HTTPErrors`), object (schema `ValidationErrorResponse`), object (schema `BadRequestError`) |
| 401 | InvalidToken | `application/json`: object (schema `Error`) |
| 404 | Fee model not found | `application/json`: object (schema `NotFoundModelError`) |
| 500 | Internal Server Error | `application/json`: object (schema `Error`) |

##### Response 400

400 Example `Schema validation`:

```json
[
  {
    "field": "body.fees.0.calculation",
    "violation": "Must validate one and only one schema (oneOf)"
  },
  {
    "field": "body.fees.0.calculation.rules.0",
    "violation": "Must validate one and only one schema (oneOf)"
  },
  {
    "field": "body.fees.0.calculation.rules.0.calculation",
    "violation": "value is required"
  }
]
```

400 Example `Business rule validation`:

```json
{
  "error_code": "RCAPI-VALIDATION-ERROR",
  "message": "Request validation failed",
  "errors": [
    {
      "field": "body.fees[1].filters.amount_range.minimum",
      "violation": "Fees contain overlapping amount ranges"
    }
  ]
}
```

400 Example `Invalid request payload`:

```json
{
  "error_code": "RCAPI-INVALID-REQUEST-PAYLOAD",
  "message": "The request payload is invalid"
}
```


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;404;500`, has examples `False`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Platform_setup_-_Rates_and_fees.yaml method=PUT path=/v1/fee/models/{model_id}/attachment/account/{account_id} operationId=attachmentByAccount -->
### `PUT /v1/fee/models/{model_id}/attachment/account/{account_id}` — Attach fee model to account

- **operationId:** `attachmentByAccount`
- **Specification:** `api-specs/Platform_setup_-_Rates_and_fees.yaml` (Platform setup - Rates and fees)
- **Server base URL(s):** `https://sandbox.pismolabs.io/rates`
- **Tags:** `Fee models`
- **Deprecated in specification:** no
- **Security requirement:** `bearerAuth`

**Description (from the specification):**

> Attach the fee model to an account.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `model_id` | path | yes | string | Fee model ID |  |
| `account_id` | path | yes | integer | Pismo account ID |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK |  |
| 400 | Bad request | `application/json`: object (schema `BadRequestError`) |
| 404 | Fee model not found | `application/json`: object (schema `NotFoundModelError`) |
| 409 | Conflict | `application/json`: object (schema `HTTPPutErrors`) |
| 500 | Internal Server Error | `application/json`: object (schema `Error`) |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;404;409;500`, has examples `False`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-CC-fee-models`, `KU-CORE-fee-models-create-and-simulate`.

<!-- op: spec=api-specs/Platform_setup_-_Rates_and_fees.yaml method=GET path=/v1/fee/models/attachment/account/{account_id} operationId=getByAccount -->
### `GET /v1/fee/models/attachment/account/{account_id}` — Get account fee model

- **operationId:** `getByAccount`
- **Specification:** `api-specs/Platform_setup_-_Rates_and_fees.yaml` (Platform setup - Rates and fees)
- **Server base URL(s):** `https://sandbox.pismolabs.io/rates`
- **Tags:** `Fee models`
- **Deprecated in specification:** no
- **Security requirement:** `bearerAuth`

**Description (from the specification):**

> Get the fee model attached to the account.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `account_id` | path | yes | integer | Pismo account ID |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `ModelAttachmentResponse`) |
| 400 | Bad request | `application/json`: object (schema `BadRequestError`) |
| 404 | Fee model not found | `application/json`: object (schema `NotFoundModelError`) |
| 500 | Internal Server Error | `application/json`: object (schema `Error`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `model_id` | string (schema `ModelID`) | no | Pismo fee model ID | format: "uuid"; example: "d290f1ee-6c54-4b01-90e6-d701748f0851" |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;404;500`, has examples `False`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Platform_setup_-_Rates_and_fees.yaml method=DELETE path=/v1/fee/models/attachment/account/{account_id} operationId=deleteByAccount -->
### `DELETE /v1/fee/models/attachment/account/{account_id}` — Delete account fee model

- **operationId:** `deleteByAccount`
- **Specification:** `api-specs/Platform_setup_-_Rates_and_fees.yaml` (Platform setup - Rates and fees)
- **Server base URL(s):** `https://sandbox.pismolabs.io/rates`
- **Tags:** `Fee models`
- **Deprecated in specification:** no
- **Security requirement:** `bearerAuth`

**Description (from the specification):**

> Delete the fee model from an account.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `account_id` | path | yes | integer | Pismo account ID |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK |  |
| 400 | Bad request | `application/json`: object (schema `BadRequestError`) |
| 404 | Fee model not found | `application/json`: object (schema `NotFoundModelError`) |
| 500 | Internal Server Error | `application/json`: object (schema `Error`) |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;404;500`, has examples `False`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Platform_setup_-_Rates_and_fees.yaml method=PUT path=/v1/fee/models/{model_id}/attachment/program/{program_id} operationId=attachmentByProgram -->
### `PUT /v1/fee/models/{model_id}/attachment/program/{program_id}` — Attach fee model to program

- **operationId:** `attachmentByProgram`
- **Specification:** `api-specs/Platform_setup_-_Rates_and_fees.yaml` (Platform setup - Rates and fees)
- **Server base URL(s):** `https://sandbox.pismolabs.io/rates`
- **Tags:** `Fee models`
- **Deprecated in specification:** no
- **Security requirement:** `bearerAuth`

**Description (from the specification):**

> Attach the fee model to a program.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `model_id` | path | yes | string | Fee model ID |  |
| `program_id` | path | yes | integer | Pismo program ID |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK |  |
| 400 | Bad request | `application/json`: object (schema `BadRequestError`) |
| 404 | Fee model not found | `application/json`: object (schema `NotFoundModelError`) |
| 409 | Conflict | `application/json`: object (schema `HTTPPutErrors`) |
| 500 | Internal Server Error | `application/json`: object (schema `Error`) |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;404;409;500`, has examples `False`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-CC-fee-models`, `KU-CORE-fee-models-create-and-simulate`.

<!-- op: spec=api-specs/Platform_setup_-_Rates_and_fees.yaml method=GET path=/v1/fee/models/attachment/program/{program_id} operationId=getByProgram -->
### `GET /v1/fee/models/attachment/program/{program_id}` — Get program fee model

- **operationId:** `getByProgram`
- **Specification:** `api-specs/Platform_setup_-_Rates_and_fees.yaml` (Platform setup - Rates and fees)
- **Server base URL(s):** `https://sandbox.pismolabs.io/rates`
- **Tags:** `Fee models`
- **Deprecated in specification:** no
- **Security requirement:** `bearerAuth`

**Description (from the specification):**

> Get the fee model attached to a program.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `program_id` | path | yes | integer | Pismo program ID |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `ModelAttachmentResponse`) |
| 400 | Bad request | `application/json`: object (schema `BadRequestError`) |
| 404 | Fee model not found | `application/json`: object (schema `NotFoundModelError`) |
| 500 | Internal Server Error | `application/json`: object (schema `Error`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `model_id` | string (schema `ModelID`) | no | Pismo fee model ID | format: "uuid"; example: "d290f1ee-6c54-4b01-90e6-d701748f0851" |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;404;500`, has examples `False`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Platform_setup_-_Rates_and_fees.yaml method=DELETE path=/v1/fee/models/attachment/program/{program_id} operationId=deleteAttachByProgram -->
### `DELETE /v1/fee/models/attachment/program/{program_id}` — Delete program fee model

- **operationId:** `deleteAttachByProgram`
- **Specification:** `api-specs/Platform_setup_-_Rates_and_fees.yaml` (Platform setup - Rates and fees)
- **Server base URL(s):** `https://sandbox.pismolabs.io/rates`
- **Tags:** `Fee models`
- **Deprecated in specification:** no
- **Security requirement:** `bearerAuth`

**Description (from the specification):**

> Delete the fee model from the program.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `program_id` | path | yes | integer | Pismo program ID |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK |  |
| 400 | Bad request | `application/json`: object (schema `BadRequestError`) |
| 404 | Fee model not found | `application/json`: object (schema `NotFoundModelError`) |
| 500 | Internal Server Error | `application/json`: object (schema `Error`) |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;404;500`, has examples `False`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Platform_setup_-_Rates_and_fees.yaml method=GET path=/v1/fee/models/attachment/tenant operationId=getModelByOrg -->
### `GET /v1/fee/models/attachment/tenant` — Get org fee model

- **operationId:** `getModelByOrg`
- **Specification:** `api-specs/Platform_setup_-_Rates_and_fees.yaml` (Platform setup - Rates and fees)
- **Server base URL(s):** `https://sandbox.pismolabs.io/rates`
- **Tags:** `Fee models`
- **Deprecated in specification:** no
- **Security requirement:** `bearerAuth`

**Description (from the specification):**

> Get fee model by organization, which is derived from the access token.

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `ModelAttachmentResponse`) |
| 404 | Fee model not found | `application/json`: object (schema `NotFoundModelError`) |
| 500 | Internal Server Error | `application/json`: object (schema `Error`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `model_id` | string (schema `ModelID`) | no | Pismo fee model ID | format: "uuid"; example: "d290f1ee-6c54-4b01-90e6-d701748f0851" |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;404;500`, has examples `False`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Platform_setup_-_Rates_and_fees.yaml method=PUT path=/v1/fee/models/{model_id}/attachment/tenant operationId=attachmentByTenant -->
### `PUT /v1/fee/models/{model_id}/attachment/tenant` — Attach fee model to org

- **operationId:** `attachmentByTenant`
- **Specification:** `api-specs/Platform_setup_-_Rates_and_fees.yaml` (Platform setup - Rates and fees)
- **Server base URL(s):** `https://sandbox.pismolabs.io/rates`
- **Tags:** `Fee models`
- **Deprecated in specification:** no
- **Security requirement:** `bearerAuth`

**Description (from the specification):**

> Attach a fee model to an org. The org ID is derived from the access token.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `model_id` | path | yes | string | Fee model ID |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK |  |
| 400 | Bad request | `application/json`: object (schema `BadRequestError`) |
| 404 | Fee model not found | `application/json`: object (schema `NotFoundModelError`) |
| 409 | Conflict | `application/json`: object (schema `HTTPPutErrors`) |
| 500 | Internal Server Error | `application/json`: object (schema `Error`) |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;404;409;500`, has examples `False`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-CC-fee-models`, `KU-CORE-fee-models-create-and-simulate`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/BadRequestError -->
### Schema `BadRequestError`

Pointer: `#/components/schemas/BadRequestError`. Type: object (schema `BadRequestError`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `error_code` | string | no | Error code ID | example: "RCAPI-INVALID-REQUEST-PAYLOAD" |
| `message` | string | no | Error description | example: "The request payload is invalid" |

<!-- schema: #/components/schemas/Error -->
### Schema `Error`

Pointer: `#/components/schemas/Error`. Type: object (schema `Error`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `error_code` | string | no | Error code ID. | example: "RCAPI-DOMAIN-VIOLATION" |
| `message` | string | no | Error description. | example: "Internal server error" |

<!-- schema: #/components/schemas/Fee -->
### Schema `Fee`

Pointer: `#/components/schemas/Fee`. Type: object (schema `Fee`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `description` | string | yes | Fee description. | minLength: 1; maxLength: 255; example: "Fee wdl" |
| `id` | string (schema `FeeID`) | yes | Fee ID - a reference from transaction postings. The Pismo transaction team uses fee ID fields to make accounting entries. Talk to your Pismo representative about getting fee IDs for your operations.<br> | example: "sellos_baires" |
| `type` | string | yes | Fee type, represents the fee classification, and is linked with the `id` field.<br> | example: "sellos" |
| `precedence` | integer (schema `Precedence`) | no | Calculation order. All fees with the same precedence number are calculated in the same iteration. The next iteration uses the previous output as its calculation basis.<br> | example: 0 |
| `deduct_from_transaction_value` | boolean | no | Should fee be deducted from transaction value flag. Default=`false`.<br> | example: true |
| `calculation_basis` | string | no | * `PRINCIPAL_AMOUNT` - Taxes are applied to original transaction amount only. This is the default.<br>* `CONTRACT_AMOUNT` -  Taxes are applied to original transaction amount plus fees.<br> | example: "PRINCIPAL_AMOUNT" |
| `calculation` | oneOf: object (schema `FeeCalculationFixed`), object (schema `FeeCalculationGreater`), object (schema `FeeCalculationPercentage`), object (schema `FeeCalculationDailyPercentage`), object (schema `FeeCalculationCompoundInterest`), object (schema `FeeCalculationAccumulator`), object (schema `FeeCalculationDynamicByAmount`), object (schema `FeeCalculationPriceTable`), object (schema `FeeCalculationEqualInstallments`), object (schema `FeeCalculationAging`), object (schema `FeeCalculationIof`), object (schema `FeeCalculationConstantRepayment`), object (schema `FeeCalculationBuiltIn`) | yes |  |  |
| `filters` | object (schema `Filters`) | yes |  |  |
| `additional_fees` | array of object (schema `AdditionalFee`) | no |  |  |

<!-- schema: #/components/schemas/HTTPErrors -->
### Schema `HTTPErrors`

Pointer: `#/components/schemas/HTTPErrors`. Type: array of object (schema `HTTPErrors`).

<!-- schema: #/components/schemas/ValidationErrorResponse -->
### Schema `ValidationErrorResponse`

Pointer: `#/components/schemas/ValidationErrorResponse`. Type: object (schema `ValidationErrorResponse`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `error_code` | string | yes | Error code ID | example: "RCAPI-VALIDATION-ERROR" |
| `message` | string | yes | Error description | example: "Request validation failed" |
| `errors` | array of object (schema `HTTPErrors`) | yes |  |  |
| `errors[].field` | string | no | Incorrect field | example: "body.date" |
| `errors[].violation` | string | no | Describes the rule that the field did not match. | example: "Does not match pattern '^\\\\d{4}\\\\-(0?[1-9]\|1[012])\\\\-(0?[1-9]\|[12][0-9]\|3[01])$'" |

<!-- schema: #/components/schemas/NotFoundModelError -->
### Schema `NotFoundModelError`

Pointer: `#/components/schemas/NotFoundModelError`. Type: object (schema `NotFoundModelError`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `error_code` | string | no | Error code ID | example: "RCAPI-NOT_FOUND-VIOLATION" |
| `message` | string | no | Error description. | example: "Model with the provided key does not exist" |

<!-- schema: #/components/schemas/HTTPPutErrors -->
### Schema `HTTPPutErrors`

Pointer: `#/components/schemas/HTTPPutErrors`. Type: object (schema `HTTPPutErrors`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `error_code` | string | no | Error code ID. | example: "RCAPI-INTEGRITY-VIOLATION" |
| `message` | string | no | Error description | example: "Attachment has been created already" |

<!-- schema: #/components/schemas/FeeCalculationFixed -->
### Schema `FeeCalculationFixed`

Pointer: `#/components/schemas/FeeCalculationFixed`. Type: object (schema `FeeCalculationFixed`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `calculation_method` | string | yes | Calculation method - `FIXED` | enum: ["FIXED"] |
| `value` | number | yes | Fixed fee amount as decimal field. | example: 2.5 |

<!-- schema: #/components/schemas/FeeCalculationGreater -->
### Schema `FeeCalculationGreater`

Pointer: `#/components/schemas/FeeCalculationGreater`. Type: object (schema `FeeCalculationGreater`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `calculation_method` | string | yes | Calculation method - `GREATER`. Whichever value is greater - `fixed` or `percentage` is applied. | enum: ["GREATER"] |
| `fixed` | number | yes | Fixed fee amount as decimal field. | example: 50 |
| `percentage` | number | yes | Percentage amount as decimal field. | example: 1.3 |

<!-- schema: #/components/schemas/FeeCalculationPercentage -->
### Schema `FeeCalculationPercentage`

Pointer: `#/components/schemas/FeeCalculationPercentage`. Type: object (schema `FeeCalculationPercentage`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `calculation_method` | string | yes | Calculation method - `PERCENTAGE`. | enum: ["PERCENTAGE"] |
| `value` | number | yes | Percentage amount as decimal field. | example: 1.3 |

<!-- schema: #/components/schemas/FeeCalculationDailyPercentage -->
### Schema `FeeCalculationDailyPercentage`

Pointer: `#/components/schemas/FeeCalculationDailyPercentage`. Type: object (schema `FeeCalculationDailyPercentage`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `calculation_method` | string | yes | Calculation method - `DAILY_PERCENTAGE`. Applied to credit card cash advances and other loan-type products. | enum: ["DAILY_PERCENTAGE"] |
| `value` | number | yes | Percentage amount as decimal field. | example: 1.3 |

<!-- schema: #/components/schemas/FeeCalculationCompoundInterest -->
### Schema `FeeCalculationCompoundInterest`

Pointer: `#/components/schemas/FeeCalculationCompoundInterest`. Type: object (schema `FeeCalculationCompoundInterest`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `calculation_method` | string | yes | Calculation method - `COMPOUND_INTEREST`. Applied to loan-type products. | enum: ["COMPOUND_INTEREST"] |
| `value` | number | yes | Percentage amount as decimal field. | example: 1.3 |
| `days_range` | integer | yes | Calculation's range of days.<br><br>For example: 10% interest and `days_range` = 20 for $100 purchase; considering 10 days between purchase and cycle close, is applied 0.5% per day (10/20). In the first day, the value will be 0.5 (100 x 0.5%), in the second day the value will be 0.55 (100.05 x 0.5%), and so on.<br> | example: 30 |

<!-- schema: #/components/schemas/FeeCalculationAccumulator -->
### Schema `FeeCalculationAccumulator`

Pointer: `#/components/schemas/FeeCalculationAccumulator`. Type: object (schema `FeeCalculationAccumulator`).

> Fee calculation for ACCUMULATOR model.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `calculation_method` | string | yes | Calculation method - `ACCUMULATOR`. | enum: ["ACCUMULATOR"] |
| `index` | string | yes | Field used to index the calculation.<br>  `AMOUNT` - Fee is based on transaction totals.<br>  `QUANTITY` - Fee is based on number of transactions.<br> | enum: ["AMOUNT", "QUANTITY"]; example: "QUANTITY" |
| `identifier` | string | yes | Accumulator configuration ID. Client-assigned and passed to the <a href="https://developers.pismo.io/pismo-docs/reference/post-v1-accumulator-config" target="_blank">Create accumulator configuration</a> endpoint.<br> | example: "ACC_CASH_OUT" |
| `rules` | array of oneOf: object (schema `RuleRange`), object (schema `RuleGreater`) | yes | Ranges and strategies |  |

<!-- schema: #/components/schemas/FeeCalculationDynamicByAmount -->
### Schema `FeeCalculationDynamicByAmount`

Pointer: `#/components/schemas/FeeCalculationDynamicByAmount`. Type: object (schema `FeeCalculationDynamicByAmount`).

> Fee calculation for `DYNAMIC_BY_AMOUNT` model.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `calculation_method` | string | yes | Calculation method - `DYNAMIC_BY_AMOUNT`. | enum: ["DYNAMIC_BY_AMOUNT"] |
| `rules` | array of oneOf: object (schema `RuleRange`), object (schema `RuleGreater`) | yes | Ranges and strategies |  |

<!-- schema: #/components/schemas/FeeCalculationPriceTable -->
### Schema `FeeCalculationPriceTable`

Pointer: `#/components/schemas/FeeCalculationPriceTable`. Type: object (schema `FeeCalculationPriceTable`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `calculation_method` | string | yes | Calculation method - `PRICE_TABLE`. | enum: ["PRICE_TABLE"] |
| `index` | string | no | Define range type when interest rate is dynamic. | enum: ["INSTALLMENT"] |
| `fixed` | number | no | Fixed fee amount as decimal field. | example: 50 |
| `percentage` | number | no | Percentage amount as decimal field. | example: 1.3 |
| `fixed_iof_rate` | number | yes | Percentage amount as decimal field. IOF = Brazilian tax. | example: 0.38 |
| `daily_iof_rate` | number | yes | Percentage amount as decimal field. IOF = Brazilian tax. | example: 0.0082 |
| `interest_rate` | object (schema `InterestRate`) | yes |  |  |

<!-- schema: #/components/schemas/FeeCalculationEqualInstallments -->
### Schema `FeeCalculationEqualInstallments`

Pointer: `#/components/schemas/FeeCalculationEqualInstallments`. Type: object (schema `FeeCalculationEqualInstallments`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `calculation_method` | string | yes | Calculation method - `EQUAL_INSTALLMENTS`. | enum: ["EQUAL_INSTALLMENTS"] |
| `fees` | array of object (schema `fees`) | yes | List of additional fees. |  |
| `fees[].calculation` | string | yes |  | enum: ["FIXED", "PERCENTAGE", "DAILY_PERCENTAGE", "IOF"]; example: "FIXED" |
| `fees[].id` | string | yes |  | example: "tax1" |
| `fees[].precedence` | integer | yes |  | example: 1 |
| `fees[].value` | number | yes |  | example: 10 |
| `fees[].calculation_basis` | string | yes |  | enum: ["PRINCIPAL_AMOUNT", "CONTRACT_AMOUNT"]; example: "PRINCIPAL_AMOUNT" |
| `fees[].fixed_iof_rate` | number | no |  | example: 3.5 |
| `fees[].daily_iof_rate` | number | no |  | example: 0.0082 |
| `interest_rate` | object (schema `InterestRateWithGracePeriod`) | yes |  |  |
| `precedence` | integer (schema `Precedence`) | yes | Calculation order. All fees with the same precedence number are calculated in the same iteration. The next iteration uses the previous output as its calculation basis.<br> | example: 0 |
| `day_count_method` | string | no |  | enum: ["MONTH_30_YEAR_360", "MONTH_ACTUAL_YEAR_365"]; example: "MONTH_30_YEAR_360" |

<!-- schema: #/components/schemas/FeeCalculationAging -->
### Schema `FeeCalculationAging`

Pointer: `#/components/schemas/FeeCalculationAging`. Type: object (schema `FeeCalculationAging`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `calculation_method` | string | yes | Calculation method - `AGING`. | enum: ["AGING"] |
| `index` | string | no | Define range type when rate is dynamic. | enum: ["DAY"] |
| `rate` | object (schema `Rate`) | yes |  |  |

<!-- schema: #/components/schemas/FeeCalculationIof -->
### Schema `FeeCalculationIof`

Pointer: `#/components/schemas/FeeCalculationIof`. Type: object (schema `FeeCalculationIof`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `calculation_method` | string | yes | Calculation method - `IOF`. | enum: ["IOF"] |
| `value` | number | yes | Percentage amount as decimal and used as base to calculate the fee amount. | example: 100 |

<!-- schema: #/components/schemas/FeeCalculationConstantRepayment -->
### Schema `FeeCalculationConstantRepayment`

Pointer: `#/components/schemas/FeeCalculationConstantRepayment`. Type: object (schema `FeeCalculationConstantRepayment`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `calculation_method` | string | yes | Calculation method - `CONSTANT_REPAYMENT` | enum: ["CONSTANT_REPAYMENT"] |
| `day_count_method` | string (schema `DayCountMethod`) | yes | Day count convention used to calculate interest | enum: ["MONTH_30_YEAR_360", "MONTH_ACTUAL_YEAR_365"]; example: "MONTH_30_YEAR_360" |
| `payment_postponement_rules` | object | no | Rules for payment postponement. |  |
| `payment_postponement_rules.basis` | string | no | Postponement basis. | enum: ["PRINCIPAL", "INTEREST"]; example: "INTEREST" |
| `payment_postponement_rules.cycles` | string | no | Number of cycles to postpone. | example: "1" |
| `interest_rate` | object (schema `InterestRate`) | yes |  |  |
| `fees` | array of object | no | List of additional fees. |  |
| `fees[].calculation` | string | yes |  | enum: ["FIXED", "PERCENTAGE", "DAILY_PERCENTAGE"]; example: "FIXED" |
| `fees[].id` | string | yes |  | example: "tax1" |
| `fees[].precedence` | integer | yes |  | example: 1 |
| `fees[].value` | number | yes |  | example: 10 |
| `fees[].calculation_basis` | string | yes |  | enum: ["PRINCIPAL_AMOUNT", "CONTRACT_AMOUNT"]; example: "PRINCIPAL_AMOUNT" |

<!-- schema: #/components/schemas/FeeCalculationBuiltIn -->
### Schema `FeeCalculationBuiltIn`

Pointer: `#/components/schemas/FeeCalculationBuiltIn`. Type: object (schema `FeeCalculationBuiltIn`).

> Fee calculation for `BUILT_IN` model. A `BUILT_IN` fee is always applied before any other fee. The percentage defined in `value` is applied to the principal amount and the resulting fee amount is incorporated into the principal, so all subsequent fees are calculated over the principal plus the `BUILT_IN` fee.
>
> A `BUILT_IN` fee can only be added if its `precedence` is lower than the `precedence` of every other fee in the same fee model that shares at least one `processing_code` with it. If any of those fees has an equal or lower `precedence`, the API returns `400 Bad Request` with an invalid payload error listing the violated `field` and `violation`.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `calculation_method` | string | yes | Calculation method - `BUILT_IN`. Always applied before any other fee, and its amount is incorporated into the principal. | enum: ["BUILT_IN"] |
| `value` | number | yes | Percentage amount as decimal field, applied to the principal amount. | example: 1.3 |

<!-- schema: #/components/schemas/Filters -->
### Schema `Filters`

Pointer: `#/components/schemas/Filters`. Type: object (schema `Filters`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `processing_codes` | array of string | yes | Processing codes to apply the fee to.  Processing codes identify an operation, such as purchases or debits. Each financial operation within the platform has its processing code. Some you can configure, while others are fixed in the card network flow. Talk to your Pismo representative to get, or create, processing codes. For more information, see <a href="https://developers.pismo.io/pismo-docs/docs/processing-codes-and-transaction-types" target="_blank">Processing codes and transaction types</a>.<br> | example: ["02", "0040"] |
| `operation_types` | array of string | no | Operation types to apply the fee to. If not specified, fees will be applied to all types. | items.enum: ["authorization", "confirmation"] |
| `amount_range` | object | no | Optional amount range filter. When specified, the fee is applied only to operations whose amount falls within the given range. When the object is sent, only `minimum` is required; `maximum` remains optional. When two fees share at least one `processing_code`, their `amount_range` intervals must not overlap — a fee with no `maximum` is treated as unbounded above. |  |
| `amount_range.minimum` | number | yes | Minimum amount (inclusive) for the fee to be applied. BigDecimal value. Required when `amount_range` is provided. | format: "double"; example: 10 |
| `amount_range.maximum` | number | no | Maximum amount (inclusive) for the fee to be applied. BigDecimal value. Optional — when present, must be greater than or equal to `minimum`. | format: "double"; example: 1000 |
| `merchant_category` | object | no | Optional merchant category filter. When specified, the fee is applied only to operations whose Merchant Category Code (MCC) matches the given include/exclude criteria. MCC is treated as an opaque string — no ISO 8583 validation is performed. Omitting the object, or leaving both lists empty, bypasses the filter. Server-side validation — `include` and `exclude` each must not contain duplicate MCC values, and the two lists must not share any MCC value; violations return HTTP 400. |  |
| `merchant_category.include` | array of string | no | When non-empty, the fee is applied only if the request MCC is in this list. A request without an MCC does not match when `include` is populated. | example: ["7995", "5411"] |
| `merchant_category.exclude` | array of string | no | When non-empty, the fee is NOT applied if the request MCC is in this list. | example: ["9999"] |

<!-- schema: #/components/schemas/AdditionalFee -->
### Schema `AdditionalFee`

Pointer: `#/components/schemas/AdditionalFee`. Type: object (schema `AdditionalFee`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `description` | string | yes | Fee description. | example: "Foreign currency surchange." |
| `type` | string | yes | Fee type, represents the fee classification, and is linked with the `id` field. | example: "sellos" |
| `id` | string (schema `FeeID`) | yes | Fee ID - a reference from transaction postings. The Pismo transaction team uses fee ID fields to make accounting entries. Talk to your Pismo representative about getting fee IDs for your operations.<br> | example: "sellos_baires" |
| `calculation` | oneOf: object (schema `FeeCalculationFixed`), object (schema `FeeCalculationGreater`), object (schema `FeeCalculationPercentage`) | yes |  |  |

<!-- schema: #/components/schemas/RuleRange -->
### Schema `RuleRange`

Pointer: `#/components/schemas/RuleRange`. Type: object (schema `RuleRange`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `calculation` | object (schema `RuleCalculation`) | yes |  |  |
| `minimum` | number (schema `minimumRule`) | yes | First tranasction this rule is applied to. For example, if you enter "4", the rule starts being applied on the 4th transaction.<br> | example: 4 |
| `maximum` | number (schema `maximumRule`) | yes | Last transaction the rule is applied to. For example, if you enter "10", rule application ends after the 10th transaction.<br> | example: 100 |

<!-- schema: #/components/schemas/RuleGreater -->
### Schema `RuleGreater`

Pointer: `#/components/schemas/RuleGreater`. Type: object (schema `RuleGreater`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `greater_than` | number | yes | Rule applies to numbers greater than this value. For example, if you enter "4", accumulation starts on the 5th transaction. | example: 10 |
| `calculation` | object (schema `RuleCalculation`) | yes |  |  |

<!-- schema: #/components/schemas/InterestRate -->
### Schema `InterestRate`

Pointer: `#/components/schemas/InterestRate`. Type: object (schema `InterestRate`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `type` | string | yes | Fee type:<br>  `FIXED` - Field `value` is required and will be used as interest rate. Field `grace_period` is optional.<br>  `DYNAMIC` - Field `rules` is required and the value used as interest rate will be selected according to the installment ranges configured.<br> | enum: ["FIXED", "DYNAMIC"]; example: "FIXED" |
| `value` | number | no | Percentage amount as decimal field. Value used as interest rate. **REQUIRED** for `FIXED` type. | example: 0.2 |
| `grace_period` | object | no | Optional grace period before interest begins. Only applicable when interest rate `type` is `FIXED`.<br><br>**Only processed for the `EQUAL_INSTALLMENTS` calculation method.** Silently ignored for all other methods (e.g., `PRICE_TABLE`, `DAILY_PERCENTAGE`).<br> |  |
| `grace_period.type` | string | yes |  | enum: ["FIXED"]; example: "FIXED" |
| `grace_period.value` | number | yes | Number of periods to skip before interest begins. | minimum: 0; example: 1 |
| `rules` | array of object (schema `InterestRateRule`) | no | Installment ranges responsible to configure the value used as interest rate. **REQUIRED** for `DYNAMIC` type. |  |

<!-- schema: #/components/schemas/InterestRateWithGracePeriod -->
### Schema `InterestRateWithGracePeriod`

Pointer: `#/components/schemas/InterestRateWithGracePeriod`. Type: object (schema `InterestRateWithGracePeriod`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `type` | string | yes | Fee type:<br>  `FIXED` - Field `value` is required and will be used as interest rate.<br>  `DYNAMIC` - Field `rules` is required and the value used as interest rate will be selected according to the installment ranges configured.<br> | enum: ["FIXED", "DYNAMIC"]; example: "FIXED" |
| `value` | number | no | Percentage amount as decimal field. Value used as interest rate. **REQUIRED** for `FIXED` type. | example: 0.2 |
| `grace_period` | object | no | Optional grace period before interest begins.<br><br>**Only processed for the `EQUAL_INSTALLMENTS` calculation method.** Silently ignored for all other methods.<br> |  |
| `grace_period.type` | string | yes |  | enum: ["FIXED"]; example: "FIXED" |
| `grace_period.value` | number | yes | Number of periods to skip before interest begins. | minimum: 0; example: 1 |
| `rules` | array of object (schema `InterestRateRule`) | no | Installment ranges responsible to configure the value used as interest rate. **REQUIRED** for `DYNAMIC` type. |  |

<!-- schema: #/components/schemas/Rate -->
### Schema `Rate`

Pointer: `#/components/schemas/Rate`. Type: object (schema `Rate`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `type` | string | yes | Fee type:<br>  `FIXED` - Field `value` is **REQUIRED** and used as rate.<br>  `DYNAMIC` - Field `rules` is **REQUIRED** and the value used as rate is selected according to the day ranges configured.<br> | enum: ["FIXED", "DYNAMIC"]; example: "FIXED" |
| `value` | number | no | Percentage amount as decimal field. Value is used as rate. **REQUIRED** for `FIXED` type. | example: 0.2 |
| `rules` | array of oneOf: object (schema `RateRuleRange`), object (schema `RateRuleGreater`) | no | Ranges responsible to configure the value used as rate. **REQUIRED** for `DYNAMIC` type. |  |

<!-- schema: #/components/schemas/RuleCalculation -->
### Schema `RuleCalculation`

Pointer: `#/components/schemas/RuleCalculation`. Type: object (schema `RuleCalculation`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `calculation_method` | string (schema `CalculationMethodSubset`) | yes | Calculation method. | enum: ["FIXED", "PERCENTAGE"]; example: "FIXED" |
| `value` | number | yes | Value to be applied | example: 0.04 |

<!-- schema: #/components/schemas/InterestRateRule -->
### Schema `InterestRateRule`

Pointer: `#/components/schemas/InterestRateRule`. Type: object (schema `InterestRateRule`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `minimum` | number | yes | First installment the rule is applied to. For example, if you enter "4", rule application begins on the 4th installment.<br>Must be 1 or higher.<br> | minimum: 1; example: 10 |
| `maximum` | number | yes | Last installment the rule is applied to. For example, if you enter "10", rule application ends after the 10th installment.<br> | maximum: 70; example: 30 |
| `calculation` | object (schema `RuleCalculation`) | yes |  |  |
| `progression` | object (schema `Progression`) | no | Rate progression configuration. |  |

<!-- schema: #/components/schemas/RateRuleRange -->
### Schema `RateRuleRange`

Pointer: `#/components/schemas/RateRuleRange`. Type: object (schema `RateRuleRange`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `calculation` | object (schema `RuleCalculation`) | yes |  |  |
| `minimum` | number (schema `minimumRule`) | yes | First tranasction this rule is applied to. For example, if you enter "4", the rule starts being applied on the 4th transaction.<br> | example: 4 |
| `maximum` | number (schema `maximumRule`) | yes | Last transaction the rule is applied to. For example, if you enter "10", rule application ends after the 10th transaction.<br> | example: 100 |
| `progression` | object (schema `Progression`) | no | Rate progression configuration. |  |

<!-- schema: #/components/schemas/RateRuleGreater -->
### Schema `RateRuleGreater`

Pointer: `#/components/schemas/RateRuleGreater`. Type: object (schema `RateRuleGreater`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `greater_than` | number | yes | Rule is applied to numbers greater than this value. | example: 10 |
| `calculation` | object (schema `RuleCalculation`) | yes |  |  |
| `progression` | object (schema `Progression`) | no | Rate progression configuration. |  |

<!-- schema: #/components/schemas/Progression -->
### Schema `Progression`

Pointer: `#/components/schemas/Progression`. Type: object (schema `Progression`).

> Rate progression configuration.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `value` | number | yes | Percentage amount as decimal field added to `rule.calculation.value` base value. | example: 0.02 |
| `steps` | integer | yes | Frequency `value` is applied. | example: 10 |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Platform_setup_-_Rates_and_fees.yaml` | tag `Fee models`: GET /v1/fee/models, POST /v1/fee/models, GET /v1/fee/models/{model_id}, PUT /v1/fee/models/{model_id}, PUT /v1/fee/models/{model_id}/attachment/account/{account_id}, GET /v1/fee/models/attachment/account/{account_id}, DELETE /v1/fee/models/attachment/account/{account_id}, PUT /v1/fee/models/{model_id}/attachment/program/{program_id}, GET /v1/fee/models/attachment/program/{program_id}, DELETE /v1/fee/models/attachment/program/{program_id}, GET /v1/fee/models/attachment/tenant, PUT /v1/fee/models/{model_id}/attachment/tenant | https://github.com/PismoDevEx/pismo-api-specs | `0a918b57bd00f81c…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-BANK-penalties-for-cd-accounts` — Penalties and taxes for CD accounts
- `KU-CC-fee-models` — Control Center fee models: manage and link fee models
- `KU-CORE-fee-models-create-and-simulate` — Creating, applying and simulating fee models
