---
ku_id: KU-API-platform-setup-rates-and-fees--simulation
title: 'API reference: Platform setup - Rates and fees — Simulation'
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
- getSimulationConfigsV1
- simulationConfigs
- getSimulationConfigs
- putSimulationConfigs
- attachOrgSimulationConfig
- getOrgSimulationAttachment
- attachProgramSimulationConfig
- getProgramSimulationAttachment
- detachProgramSimulationConfig
- attachAccountSimulationConfig
- getAccountSimulationAttachment
- detachAccountSimulationConfig
- getSimulationAttachments
related_kus:
- KU-CORE-fee-models-create-and-simulate
- KU-CORE-simulation-service
- KU-LEND-simulate-loans
specification_version: 1.0.0
---

# API reference: Platform setup - Rates and fees — Simulation

**KU ID:** `KU-API-platform-setup-rates-and-fees--simulation` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 13 operation(s) tagged `Simulation` in `api-specs/Platform_setup_-_Rates_and_fees.yaml` (“Platform setup - Rates and fees”, version `1.0.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Simulation endpoints

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `GET /v1/simulation/configs` | `getSimulationConfigsV1` | Get Simulation configuration details | no |
| `POST /v1/simulation/configs` | `simulationConfigs` | Create simulation config | no |
| `GET /v1/simulation/configs/{simulation_config_id}` | `getSimulationConfigs` | Get simulation config | no |
| `PUT /v1/simulation/configs/{simulation_config_id}` | `putSimulationConfigs` | Update simulation config | no |
| `PUT /v1/simulation/configs/{simulation_config_id}/attachment/tenant` | `attachOrgSimulationConfig` | Attach simulation config to org | no |
| `GET /v1/simulation/configs/attachment/tenant` | `getOrgSimulationAttachment` | Get org simulation config | no |
| `PUT /v1/simulation/configs/{simulation_config_id}/attachment/program/{program_id}` | `attachProgramSimulationConfig` | Attach simulation config to program | no |
| `GET /v1/simulation/configs/attachment/program/{program_id}` | `getProgramSimulationAttachment` | Get program simulation config | no |
| `DELETE /v1/simulation/configs/attachment/program/{program_id}` | `detachProgramSimulationConfig` | Detach program simulation config | no |
| `PUT /v1/simulation/configs/{simulation_config_id}/attachment/account/{account_id}` | `attachAccountSimulationConfig` | Attach simulation config to account | no |
| `GET /v1/simulation/configs/attachment/account/{account_id}` | `getAccountSimulationAttachment` | Get account simulation config | no |
| `DELETE /v1/simulation/configs/attachment/account/{account_id}` | `detachAccountSimulationConfig` | Detach account simulation config | no |
| `GET /v1/simulation/configs/attachments` | `getSimulationAttachments` | Get simulation attachments | no |

## Authentication

- `bearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"}

## Operation contracts

<!-- op: spec=api-specs/Platform_setup_-_Rates_and_fees.yaml method=GET path=/v1/simulation/configs operationId=getSimulationConfigsV1 -->
### `GET /v1/simulation/configs` — Get Simulation configuration details

- **operationId:** `getSimulationConfigsV1`
- **Specification:** `api-specs/Platform_setup_-_Rates_and_fees.yaml` (Platform setup - Rates and fees)
- **Server base URL(s):** `https://sandbox.pismolabs.io/rates`
- **Tags:** `Simulation`
- **Deprecated in specification:** no
- **Security requirement:** `bearerAuth`

**Description (from the specification):**

> Retrieve simulation configs based on the filters

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `description` | query | no | string | Filter by any description including simulation config id |  |
| `simulation_config_id` | query | no | string | Filter by Simulation configuration ID |  |
| `programId` | query | no | integer | **Deprecated** - use `program_ids` instead. Filters by a single Pismo<br>program ID. Mutually exclusive with `program_ids`: sending both returns<br>400.<br> | deprecated: true |
| `program_ids` | query | no | array of integer | Filters by one or more Pismo program IDs. **Recommended** over the<br>deprecated `programId` parameter.<br><br>- **Format:** comma-separated list, e.g. `program_ids=1,2,3`. Repeating<br>  the parameter (`program_ids=1&program_ids=2`) is also accepted.<br>- **Values:** each ID must be a positive integer; a value `<= 0` returns<br>  `400 RCAPI-INVALID-QUERY-PARAM`.<br>- **Duplicates:** IDs should be distinct; any repeated IDs are tolerated,<br>  de-duplicated server-side, and do not count toward the maximum.<br>- **Maximum:** up to 20 distinct program IDs per request. Sending more<br>  than 20 returns `400 RCAPI-INVALID-QUERY-PARAM`.<br>- **Mutual exclusivity:** cannot be combined with `programId`; sending<br>  both returns `400 RCAPI-INVALID-QUERY-PARAM`.<br> | minItems: 1; maxItems: 20; uniqueItems: true; example: [1, 2, 3] |
| `has_attachments` | query | no | boolean | Filter by attachment presence |  |
| `exclude_tenant_attached` | query | no | boolean | When set to true, excludes simulation configs that are attached at the TENANT level.<br>This is useful to avoid data duplication on screen, since the tenant-attached config<br>is typically displayed separately as the default configuration.<br> | default: false |
| `page` | query | yes | integer | Page Number(starts from 1) |  |
| `per_page` | query | yes | integer | Number of items per page |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object |
| 400 | Bad request | `application/json`: object (schema `BadRequestError`) |
| 401 | InvalidToken | `application/json`: object (schema `Error`) |
| 500 | Internal Server Error | `application/json`: object (schema `Error`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `items` | array of object (schema `SimulationConfigListResponse`) | no |  |  |
| `pages` | integer | no |  |  |
| `per_page` | integer | no |  |  |
| `total_items` | integer | no |  |  |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;500`, has examples `False`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Platform_setup_-_Rates_and_fees.yaml method=POST path=/v1/simulation/configs operationId=simulationConfigs -->
### `POST /v1/simulation/configs` — Create simulation config

- **operationId:** `simulationConfigs`
- **Specification:** `api-specs/Platform_setup_-_Rates_and_fees.yaml` (Platform setup - Rates and fees)
- **Server base URL(s):** `https://sandbox.pismolabs.io/rates`
- **Tags:** `Simulation`
- **Deprecated in specification:** no
- **Security requirement:** `bearerAuth`

**Description (from the specification):**

> Create simulation configuration for possible custom payment option.
>
> **Note:** EXTERNAL engine plans cannot be fully configured at creation time — `calculation_url` is not accepted during creation.
> Create the config with PISMO plans first, then use the PUT endpoint to add or update EXTERNAL engine plans with their `calculation_url`.

#### Request body

Required: yes

> Create simulation configs

**Content type `application/json`** — schema: object (schema `SimulationConfigRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `description` | string (schema `ConfigDescription`) | yes | Simulation configuration description | example: "This is my simulation configurations" |
| `plans` | array of object (schema `Plans`) | yes | Configuration of Simulation Plans |  |

Example `Calculation method Price Table` — from `#/components/examples/SimulationConfigPriceTable`:

```json
{
  "description": "This is my simulation configurations",
  "plans": [
    {
      "id": "customId1",
      "description": "Electronics",
      "calculation_parameters": {
        "calculation_method": "PRICE_TABLE",
        "daily_iof_rate": 0.0082,
        "index": "INSTALLMENT",
        "fixed_iof_rate": 0.38,
        "interest_rate": {
          "type": "FIXED",
          "value": 13.49
        },
        "fixed": 0,
        "percentage": 0
      },
      "installments": [
        1,
        2,
        3
      ],
      "day_count_method": "MONTH_30_YEAR_360",
      "billing_method": "BNPL",
      "frequency": "MONTHLY",
      "installment_parameters": {
        "minimum_installment_value": {
          "type": "DYNAMIC",
          "values": {
            "1": 3,
            "2": 10
          }
        },
        "number_of_initial_periods_to_skip": {
          "type": "FIXED",
          "value": 1
        }
      },
      "interest_limitation": {
        "calculation_basis": "PRINCIPAL_AMOUNT",
        "percentage": 3.2
      },
      "down_payment_method": {
        "type": "INSTALLMENT_EQUIVALENT"
      },
      "filters": {
        "merchants": [
          "abcdefg"
        ],
        "processing_codes": [
          "01",
          "02"
        ],
        "custom_filters": [
          "custom_filter_01",
          "custom_filter_02"
        ]
      }
    },
    {
      "id": "customId2",
      "description": "Furniture",
      "calculation_parameters": {
        "calculation_method": "PRICE_TABLE",
        "daily_iof_rate": 0.0082,
        "index": "INSTALLMENT",
        "fixed_iof_rate": 0.38,
        "interest_rate": {
          "type": "FIXED",
          "value": 13.49
        },
        "fixed": 0,
        "percentage": 0
      },
      "installments": [
        4,
        5,
        6
      ],
      "billing_method": "BNPL",
      "frequency": "MONTHLY",
      "installment_parameters": {
        "minimum_installment_value": {
          "type": "DYNAMIC",
          "values": {
            "1": 10,
            "2": 3
          }
        },
        "number_of_initial_periods_to_skip": {
          "type": "FIXED",
          "value": 1
        }
      },
      "filters": {
        "merchants": [
          "abcdefg"
        ],
        "processing_codes": [
          "01",
          "02"
        ],
        "custom_filters": [
          "custom_filter_01",
          "custom_filter_02"
        ]
      }
    }
  ]
}
```

Example `Calculation method Daily Percentage` — from `#/components/examples/SimulationConfigDailyPercentage`:

```json
{
  "description": "This is my simulation configurations",
  "plans": [
    {
      "id": "customId1",
      "description": "Electronics",
      "calculation_parameters": {
        "calculation_method": "DAILY_PERCENTAGE",
        "value": 0.03
      },
      "installments": [
        1,
        2,
        3
      ],
      "day_count_method": "MONTH_ACTUAL_YEAR_365",
      "billing_method": "CARD",
      "installment_parameters": {
        "minimum_installment_value": {
          "type": "DYNAMIC",
          "values": {
            "1": 3,
            "2": 10
          }
        },
        "number_of_initial_periods_to_skip": {
          "type": "FIXED",
          "value": 1
        }
      },
      "interest_limitation": {
        "calculation_basis": "PRINCIPAL_AMOUNT",
        "percentage": 3.2
      },
      "down_payment_method": {
        "type": "INSTALLMENT_EQUIVALENT"
      },
      "filters": {
        "merchants": [
          "abcdefg"
        ],
        "processing_codes": [
          "01",
          "02"
        ],
        "custom_filters": [
          "custom_filter_01",
          "custom_filter_02"
        ]
      }
    },
    {
      "id": "customId2",
      "description": "Furniture",
      "calculation_parameters": {
        "calculation_method": "DAILY_PERCENTAGE",
        "value": 0.04
      },
      "installments": [
        4,
        5,
        6
      ],
      "billing_method": "BNPL",
      "frequency": "MONTHLY",
      "day_count_method": "MONTH_ACTUAL_YEAR_365",
      "installment_parameters": {
        "minimum_installment_value": {
          "type": "DYNAMIC",
          "values": {
            "1": 10,
            "2": 3
          }
        },
        "number_of_initial_periods_to_skip": {
          "type": "FIXED",
          "value": 1
        }
      },
      "filters": {
        "merchants": [
          "abcdefg"
        ],
        "processing_codes": [
          "01",
          "02"
        ],
        "custom_filters": [
          "custom_filter_01",
          "custom_filter_02"
        ]
      }
    }
  ]
}
```

Example `Calculation method Equal Installments` — from `#/components/examples/SimulationConfigEqualInstallments`:

```json
{
  "description": "Equal Installments Simulation - 3 Plans",
  "plans": [
    {
      "id": "basic-plan",
      "description": "Basic Installment Plan without Grace Period",
      "billing_method": "CARD",
      "day_count_method": "MONTH_30_YEAR_360",
      "installments": [
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
        12
      ],
      "calculation_parameters": {
        "calculation_method": "EQUAL_INSTALLMENTS",
        "interest_rate": {
          "type": "FIXED",
          "value": 10
        },
        "fees": [
          {
            "calculation": "PERCENTAGE",
            "id": "IOF",
            "precedence": 0,
            "value": 0.38,
            "calculation_basis": "PRINCIPAL_AMOUNT"
          },
          {
            "calculation": "DAILY_PERCENTAGE",
            "id": "IOF-Daily",
            "precedence": 1,
            "value": 0.0082,
            "calculation_basis": "PRINCIPAL_AMOUNT"
          }
        ]
      },
      "filters": {
        "processing_codes": [
          "508"
        ]
      }
    },
    {
      "id": "plan-with-grace-period",
      "description": "Installment Plan with 1-Month Grace Period",
      "billing_method": "CARD",
      "day_count_method": "MONTH_30_YEAR_360",
      "installments": [
        6,
        9,
        12,
        18,
        24
      ],
      "calculation_parameters": {
        "calculation_method": "EQUAL_INSTALLMENTS",
        "interest_rate": {
          "type": "FIXED",
          "value": 12
        },
        "fees": [
          {
            "calculation": "PERCENTAGE",
            "id": "IOF",
            "precedence": 0,
            "value": 0.38,
            "calculation_basis": "PRINCIPAL_AMOUNT"
          },
          {
            "calculation": "DAILY_PERCENTAGE",
            "id": "IOF-Daily",
            "precedence": 1,
            "value": 0.0082,
            "calculation_basis": "PRINCIPAL_AMOUNT"
          }
        ]
      },
      "filters": {
        "processing_codes": [
          "508",
          "005"
        ],
        "merchants": [
          "premium-store"
        ]
      },
      "interest_limitation": {
        "calculation_basis": "PRINCIPAL_AMOUNT",
        "percentage": 5
      }
    },
    {
      "id": "long-term-plan",
      "description": "Long-Term Installment Plan with Down Payment",
      "billing_method": "CARD",
      "day_count_method": "MONTH_30_YEAR_360",
      "installments": [
        12,
        18,
        24,
        36
      ],
      "calculation_parameters": {
        "calculation_method": "EQUAL_INSTALLMENTS",
        "interest_rate": {
          "type": "FIXED",
          "value": 8.5
        },
        "fees": [
          {
            "calculation": "PERCENTAGE",
            "id": "IOF",
            "precedence": 0,
            "value": 0.38,
            "calculation_basis": "PRINCIPAL_AMOUNT"
          },
          {
            "calculation": "DAILY_PERCENTAGE",
            "id": "IOF-Daily",
            "precedence": 1,
            "value": 0.0082,
            "calculation_basis": "PRINCIPAL_AMOUNT"
          }
        ]
      },
      "filters": {
        "custom_filters": [
          "retail-partner"
        ]
      },
      "down_payment_method": {
        "type": "PERCENTAGE",
        "value": 20
      },
      "installment_parameters": {
        "minimum_installment_value": {
          "type": "FIXED",
          "value": 50
        }
      }
    }
  ]
}
```

Example `External Engine Configuration` — from `#/components/examples/SimulationConfigExternalEngine`:

```json
{
  "description": "External calculation engine configuration",
  "plans": [
    {
      "id": "external_plan_001",
      "description": "Premium customer external calculation",
      "engine": "EXTERNAL",
      "calculation_url": "https://api.example.com/calculate",
      "authentication": {
        "authentication_method": "JWT_DEFAULT"
      },
      "installments": [
        1,
        2,
        3,
        6,
        12
      ],
      "filters": {
        "merchants": [
          "MERCHANT_001",
          "MERCHANT_002"
        ],
        "processing_codes": [
          "00",
          "01"
        ]
      }
    }
  ]
}
```

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `SimulationConfigOutput`) |
| 400 | Bad request | `application/json`: object (schema `BadRequestError`) |
| 401 | InvalidToken | `application/json`: object (schema `Error`) |
| 500 | Internal Server Error | `application/json`: object (schema `Error`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `config_id` | string (schema `ConfigID`) | no | Simulation configuration ID. | example: "47589-uuye7-84k9" |
| `description` | string (schema `ConfigDescription`) | no | Simulation configuration description | example: "This is my simulation configurations" |
| `plans` | array of object (schema `PlansOutput`) (schema `Plans2`) | no | Customer plans created | example: [{"id": "customId1", "description": "Electronics"}, {"id": "customId2", "description": "Furniture"}] |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;500`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-CORE-fee-models-create-and-simulate`, `KU-CORE-simulation-service`.

<!-- op: spec=api-specs/Platform_setup_-_Rates_and_fees.yaml method=GET path=/v1/simulation/configs/{simulation_config_id} operationId=getSimulationConfigs -->
### `GET /v1/simulation/configs/{simulation_config_id}` — Get simulation config

- **operationId:** `getSimulationConfigs`
- **Specification:** `api-specs/Platform_setup_-_Rates_and_fees.yaml` (Platform setup - Rates and fees)
- **Server base URL(s):** `https://sandbox.pismolabs.io/rates`
- **Tags:** `Simulation`
- **Deprecated in specification:** no
- **Security requirement:** `bearerAuth`

**Description (from the specification):**

> Get simulation configuration given its ID in the path.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `simulation_config_id` | path | yes | string | Simulation configuration ID |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `SimulationConfigDetails`) |
| 400 | Bad request | `application/json`: object (schema `BadRequestError`) |
| 401 | InvalidToken | `application/json`: object (schema `Error`) |
| 404 | Simulation configuration not found | `application/json`: object (schema `NotFoundSimulationConfigError`) |
| 500 | Internal Server Error | `application/json`: object (schema `Error`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `config_id` | string (schema `ConfigID`) | no | Simulation configuration ID. | example: "47589-uuye7-84k9" |
| `description` | string (schema `ConfigDescription`) | no | Simulation configuration description | example: "This is my simulation configurations" |
| `plans` | array of object (schema `Plans`) | no | Customer plans created |  |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;404;500`, has examples `False`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-CORE-fee-models-create-and-simulate`, `KU-LEND-simulate-loans`.

<!-- op: spec=api-specs/Platform_setup_-_Rates_and_fees.yaml method=PUT path=/v1/simulation/configs/{simulation_config_id} operationId=putSimulationConfigs -->
### `PUT /v1/simulation/configs/{simulation_config_id}` — Update simulation config

- **operationId:** `putSimulationConfigs`
- **Specification:** `api-specs/Platform_setup_-_Rates_and_fees.yaml` (Platform setup - Rates and fees)
- **Server base URL(s):** `https://sandbox.pismolabs.io/rates`
- **Tags:** `Simulation`
- **Deprecated in specification:** no
- **Security requirement:** `bearerAuth`

**Description (from the specification):**

> Update a simulation configuration.
>
> **Note:** EXTERNAL engine plans (with `calculation_url`) can only be set via this endpoint — not during creation (POST).
> Once `calculation_url` is set, it cannot be changed.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `simulation_config_id` | path | yes | string | Simulation configuration ID |  |

#### Request body

Required: yes

> Update simulation configs

**Content type `application/json`** — schema: object (schema `SimulationConfigRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `description` | string (schema `ConfigDescription`) | yes | Simulation configuration description | example: "This is my simulation configurations" |
| `plans` | array of object (schema `Plans`) | yes | Configuration of Simulation Plans |  |

Example `Calculation method Price Table` — from `#/components/examples/SimulationConfigPriceTable`:

```json
{
  "description": "This is my simulation configurations",
  "plans": [
    {
      "id": "customId1",
      "description": "Electronics",
      "calculation_parameters": {
        "calculation_method": "PRICE_TABLE",
        "daily_iof_rate": 0.0082,
        "index": "INSTALLMENT",
        "fixed_iof_rate": 0.38,
        "interest_rate": {
          "type": "FIXED",
          "value": 13.49
        },
        "fixed": 0,
        "percentage": 0
      },
      "installments": [
        1,
        2,
        3
      ],
      "day_count_method": "MONTH_30_YEAR_360",
      "billing_method": "BNPL",
      "frequency": "MONTHLY",
      "installment_parameters": {
        "minimum_installment_value": {
          "type": "DYNAMIC",
          "values": {
            "1": 3,
            "2": 10
          }
        },
        "number_of_initial_periods_to_skip": {
          "type": "FIXED",
          "value": 1
        }
      },
      "interest_limitation": {
        "calculation_basis": "PRINCIPAL_AMOUNT",
        "percentage": 3.2
      },
      "down_payment_method": {
        "type": "INSTALLMENT_EQUIVALENT"
      },
      "filters": {
        "merchants": [
          "abcdefg"
        ],
        "processing_codes": [
          "01",
          "02"
        ],
        "custom_filters": [
          "custom_filter_01",
          "custom_filter_02"
        ]
      }
    },
    {
      "id": "customId2",
      "description": "Furniture",
      "calculation_parameters": {
        "calculation_method": "PRICE_TABLE",
        "daily_iof_rate": 0.0082,
        "index": "INSTALLMENT",
        "fixed_iof_rate": 0.38,
        "interest_rate": {
          "type": "FIXED",
          "value": 13.49
        },
        "fixed": 0,
        "percentage": 0
      },
      "installments": [
        4,
        5,
        6
      ],
      "billing_method": "BNPL",
      "frequency": "MONTHLY",
      "installment_parameters": {
        "minimum_installment_value": {
          "type": "DYNAMIC",
          "values": {
            "1": 10,
            "2": 3
          }
        },
        "number_of_initial_periods_to_skip": {
          "type": "FIXED",
          "value": 1
        }
      },
      "filters": {
        "merchants": [
          "abcdefg"
        ],
        "processing_codes": [
          "01",
          "02"
        ],
        "custom_filters": [
          "custom_filter_01",
          "custom_filter_02"
        ]
      }
    }
  ]
}
```

Example `Calculation method Daily Percentage` — from `#/components/examples/SimulationConfigDailyPercentage`:

```json
{
  "description": "This is my simulation configurations",
  "plans": [
    {
      "id": "customId1",
      "description": "Electronics",
      "calculation_parameters": {
        "calculation_method": "DAILY_PERCENTAGE",
        "value": 0.03
      },
      "installments": [
        1,
        2,
        3
      ],
      "day_count_method": "MONTH_ACTUAL_YEAR_365",
      "billing_method": "CARD",
      "installment_parameters": {
        "minimum_installment_value": {
          "type": "DYNAMIC",
          "values": {
            "1": 3,
            "2": 10
          }
        },
        "number_of_initial_periods_to_skip": {
          "type": "FIXED",
          "value": 1
        }
      },
      "interest_limitation": {
        "calculation_basis": "PRINCIPAL_AMOUNT",
        "percentage": 3.2
      },
      "down_payment_method": {
        "type": "INSTALLMENT_EQUIVALENT"
      },
      "filters": {
        "merchants": [
          "abcdefg"
        ],
        "processing_codes": [
          "01",
          "02"
        ],
        "custom_filters": [
          "custom_filter_01",
          "custom_filter_02"
        ]
      }
    },
    {
      "id": "customId2",
      "description": "Furniture",
      "calculation_parameters": {
        "calculation_method": "DAILY_PERCENTAGE",
        "value": 0.04
      },
      "installments": [
        4,
        5,
        6
      ],
      "billing_method": "BNPL",
      "frequency": "MONTHLY",
      "day_count_method": "MONTH_ACTUAL_YEAR_365",
      "installment_parameters": {
        "minimum_installment_value": {
          "type": "DYNAMIC",
          "values": {
            "1": 10,
            "2": 3
          }
        },
        "number_of_initial_periods_to_skip": {
          "type": "FIXED",
          "value": 1
        }
      },
      "filters": {
        "merchants": [
          "abcdefg"
        ],
        "processing_codes": [
          "01",
          "02"
        ],
        "custom_filters": [
          "custom_filter_01",
          "custom_filter_02"
        ]
      }
    }
  ]
}
```

Example `Calculation method Equal Installments` — from `#/components/examples/SimulationConfigEqualInstallments`:

```json
{
  "description": "Equal Installments Simulation - 3 Plans",
  "plans": [
    {
      "id": "basic-plan",
      "description": "Basic Installment Plan without Grace Period",
      "billing_method": "CARD",
      "day_count_method": "MONTH_30_YEAR_360",
      "installments": [
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
        12
      ],
      "calculation_parameters": {
        "calculation_method": "EQUAL_INSTALLMENTS",
        "interest_rate": {
          "type": "FIXED",
          "value": 10
        },
        "fees": [
          {
            "calculation": "PERCENTAGE",
            "id": "IOF",
            "precedence": 0,
            "value": 0.38,
            "calculation_basis": "PRINCIPAL_AMOUNT"
          },
          {
            "calculation": "DAILY_PERCENTAGE",
            "id": "IOF-Daily",
            "precedence": 1,
            "value": 0.0082,
            "calculation_basis": "PRINCIPAL_AMOUNT"
          }
        ]
      },
      "filters": {
        "processing_codes": [
          "508"
        ]
      }
    },
    {
      "id": "plan-with-grace-period",
      "description": "Installment Plan with 1-Month Grace Period",
      "billing_method": "CARD",
      "day_count_method": "MONTH_30_YEAR_360",
      "installments": [
        6,
        9,
        12,
        18,
        24
      ],
      "calculation_parameters": {
        "calculation_method": "EQUAL_INSTALLMENTS",
        "interest_rate": {
          "type": "FIXED",
          "value": 12
        },
        "fees": [
          {
            "calculation": "PERCENTAGE",
            "id": "IOF",
            "precedence": 0,
            "value": 0.38,
            "calculation_basis": "PRINCIPAL_AMOUNT"
          },
          {
            "calculation": "DAILY_PERCENTAGE",
            "id": "IOF-Daily",
            "precedence": 1,
            "value": 0.0082,
            "calculation_basis": "PRINCIPAL_AMOUNT"
          }
        ]
      },
      "filters": {
        "processing_codes": [
          "508",
          "005"
        ],
        "merchants": [
          "premium-store"
        ]
      },
      "interest_limitation": {
        "calculation_basis": "PRINCIPAL_AMOUNT",
        "percentage": 5
      }
    },
    {
      "id": "long-term-plan",
      "description": "Long-Term Installment Plan with Down Payment",
      "billing_method": "CARD",
      "day_count_method": "MONTH_30_YEAR_360",
      "installments": [
        12,
        18,
        24,
        36
      ],
      "calculation_parameters": {
        "calculation_method": "EQUAL_INSTALLMENTS",
        "interest_rate": {
          "type": "FIXED",
          "value": 8.5
        },
        "fees": [
          {
            "calculation": "PERCENTAGE",
            "id": "IOF",
            "precedence": 0,
            "value": 0.38,
            "calculation_basis": "PRINCIPAL_AMOUNT"
          },
          {
            "calculation": "DAILY_PERCENTAGE",
            "id": "IOF-Daily",
            "precedence": 1,
            "value": 0.0082,
            "calculation_basis": "PRINCIPAL_AMOUNT"
          }
        ]
      },
      "filters": {
        "custom_filters": [
          "retail-partner"
        ]
      },
      "down_payment_method": {
        "type": "PERCENTAGE",
        "value": 20
      },
      "installment_parameters": {
        "minimum_installment_value": {
          "type": "FIXED",
          "value": 50
        }
      }
    }
  ]
}
```

Example `External Engine Configuration` — from `#/components/examples/SimulationConfigExternalEngine`:

```json
{
  "description": "External calculation engine configuration",
  "plans": [
    {
      "id": "external_plan_001",
      "description": "Premium customer external calculation",
      "engine": "EXTERNAL",
      "calculation_url": "https://api.example.com/calculate",
      "authentication": {
        "authentication_method": "JWT_DEFAULT"
      },
      "installments": [
        1,
        2,
        3,
        6,
        12
      ],
      "filters": {
        "merchants": [
          "MERCHANT_001",
          "MERCHANT_002"
        ],
        "processing_codes": [
          "00",
          "01"
        ]
      }
    }
  ]
}
```

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `SimulationConfigOutput`) |
| 400 | Bad request | `application/json`: object (schema `BadRequestError`) |
| 401 | InvalidToken | `application/json`: object (schema `Error`) |
| 404 | Simulation configuration not found | `application/json`: object (schema `NotFoundSimulationConfigError`) |
| 500 | Internal Server Error | `application/json`: object (schema `Error`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `config_id` | string (schema `ConfigID`) | no | Simulation configuration ID. | example: "47589-uuye7-84k9" |
| `description` | string (schema `ConfigDescription`) | no | Simulation configuration description | example: "This is my simulation configurations" |
| `plans` | array of object (schema `PlansOutput`) (schema `Plans2`) | no | Customer plans created | example: [{"id": "customId1", "description": "Electronics"}, {"id": "customId2", "description": "Furniture"}] |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;404;500`, has examples `True`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Platform_setup_-_Rates_and_fees.yaml method=PUT path=/v1/simulation/configs/{simulation_config_id}/attachment/tenant operationId=attachOrgSimulationConfig -->
### `PUT /v1/simulation/configs/{simulation_config_id}/attachment/tenant` — Attach simulation config to org

- **operationId:** `attachOrgSimulationConfig`
- **Specification:** `api-specs/Platform_setup_-_Rates_and_fees.yaml` (Platform setup - Rates and fees)
- **Server base URL(s):** `https://sandbox.pismolabs.io/rates`
- **Tags:** `Simulation`
- **Deprecated in specification:** no
- **Security requirement:** `bearerAuth`

**Description (from the specification):**

> Attach a simulation configuration to an organization/tenant. The org ID is derived from the access token.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `simulation_config_id` | path | yes | string | Simulation configuration ID |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK |  |
| 400 | Bad request | `application/json`: object (schema `BadRequestError`) |
| 404 | Simulation configuration not found | `application/json`: object (schema `NotFoundSimulationConfigError`) |
| 500 | Internal Server Error | `application/json`: object (schema `Error`) |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;404;500`, has examples `False`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-CORE-fee-models-create-and-simulate`, `KU-CORE-simulation-service`.

<!-- op: spec=api-specs/Platform_setup_-_Rates_and_fees.yaml method=GET path=/v1/simulation/configs/attachment/tenant operationId=getOrgSimulationAttachment -->
### `GET /v1/simulation/configs/attachment/tenant` — Get org simulation config

- **operationId:** `getOrgSimulationAttachment`
- **Specification:** `api-specs/Platform_setup_-_Rates_and_fees.yaml` (Platform setup - Rates and fees)
- **Server base URL(s):** `https://sandbox.pismolabs.io/rates`
- **Tags:** `Simulation`
- **Deprecated in specification:** no
- **Security requirement:** `bearerAuth`

**Description (from the specification):**

> Get simulation configuration attached to an org. The org ID is derived from the access token.

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `SimulationConfigIdPayload`) |
| 400 | Bad request | `application/json`: object (schema `BadRequestError`) |
| 404 | Simulation configuration not found | `application/json`: object (schema `NotFoundSimulationConfigError`) |
| 500 | Internal Server Error | `application/json`: object (schema `Error`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `config_id` | string | no | Simulation configuration ID | example: "477589-59572-95734" |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;404;500`, has examples `False`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-LEND-simulate-loans`.

<!-- op: spec=api-specs/Platform_setup_-_Rates_and_fees.yaml method=PUT path=/v1/simulation/configs/{simulation_config_id}/attachment/program/{program_id} operationId=attachProgramSimulationConfig -->
### `PUT /v1/simulation/configs/{simulation_config_id}/attachment/program/{program_id}` — Attach simulation config to program

- **operationId:** `attachProgramSimulationConfig`
- **Specification:** `api-specs/Platform_setup_-_Rates_and_fees.yaml` (Platform setup - Rates and fees)
- **Server base URL(s):** `https://sandbox.pismolabs.io/rates`
- **Tags:** `Simulation`
- **Deprecated in specification:** no
- **Security requirement:** `bearerAuth`

**Description (from the specification):**

> Attach a simulation configuration to a program.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `simulation_config_id` | path | yes | string | Simulation configuration ID |  |
| `program_id` | path | yes | integer | Pismo program ID |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK |  |
| 400 | Bad request | `application/json`: object (schema `BadRequestError`) |
| 404 | Simulation configuration not found | `application/json`: object (schema `NotFoundSimulationConfigError`) |
| 500 | Internal Server Error | `application/json`: object (schema `Error`) |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;404;500`, has examples `False`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-CORE-simulation-service`.

<!-- op: spec=api-specs/Platform_setup_-_Rates_and_fees.yaml method=GET path=/v1/simulation/configs/attachment/program/{program_id} operationId=getProgramSimulationAttachment -->
### `GET /v1/simulation/configs/attachment/program/{program_id}` — Get program simulation config

- **operationId:** `getProgramSimulationAttachment`
- **Specification:** `api-specs/Platform_setup_-_Rates_and_fees.yaml` (Platform setup - Rates and fees)
- **Server base URL(s):** `https://sandbox.pismolabs.io/rates`
- **Tags:** `Simulation`
- **Deprecated in specification:** no
- **Security requirement:** `bearerAuth`

**Description (from the specification):**

> Get the ID of the simulation config attached to a program.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `program_id` | path | yes | integer | Pismo program ID |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `SimulationConfigIdPayload`) |
| 400 | Bad request | `application/json`: object (schema `BadRequestError`) |
| 404 | Simulation configuration not found | `application/json`: object (schema `NotFoundSimulationConfigError`) |
| 500 | Internal Server Error | `application/json`: object (schema `Error`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `config_id` | string | no | Simulation configuration ID | example: "477589-59572-95734" |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;404;500`, has examples `False`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-LEND-simulate-loans`.

<!-- op: spec=api-specs/Platform_setup_-_Rates_and_fees.yaml method=DELETE path=/v1/simulation/configs/attachment/program/{program_id} operationId=detachProgramSimulationConfig -->
### `DELETE /v1/simulation/configs/attachment/program/{program_id}` — Detach program simulation config

- **operationId:** `detachProgramSimulationConfig`
- **Specification:** `api-specs/Platform_setup_-_Rates_and_fees.yaml` (Platform setup - Rates and fees)
- **Server base URL(s):** `https://sandbox.pismolabs.io/rates`
- **Tags:** `Simulation`
- **Deprecated in specification:** no
- **Security requirement:** `bearerAuth`

**Description (from the specification):**

> Detach simulation configuration from a program.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `program_id` | path | yes | integer | Pismo program ID |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK |  |
| 400 | Bad request | `application/json`: object (schema `BadRequestError`) |
| 404 | Simulation configuration not found | `application/json`: object (schema `NotFoundSimulationConfigError`) |
| 500 | Internal Server Error | `application/json`: object (schema `Error`) |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;404;500`, has examples `False`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Platform_setup_-_Rates_and_fees.yaml method=PUT path=/v1/simulation/configs/{simulation_config_id}/attachment/account/{account_id} operationId=attachAccountSimulationConfig -->
### `PUT /v1/simulation/configs/{simulation_config_id}/attachment/account/{account_id}` — Attach simulation config to account

- **operationId:** `attachAccountSimulationConfig`
- **Specification:** `api-specs/Platform_setup_-_Rates_and_fees.yaml` (Platform setup - Rates and fees)
- **Server base URL(s):** `https://sandbox.pismolabs.io/rates`
- **Tags:** `Simulation`
- **Deprecated in specification:** no
- **Security requirement:** `bearerAuth`

**Description (from the specification):**

> Attach simulation configuration to an account.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `simulation_config_id` | path | yes | string | Simulation configuration ID |  |
| `account_id` | path | yes | integer | Pismo account ID |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK |  |
| 400 | Bad request | `application/json`: object (schema `BadRequestError`) |
| 404 | Simulation configuration not found | `application/json`: object (schema `NotFoundSimulationConfigError`) |
| 500 | Internal Server Error | `application/json`: object (schema `Error`) |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;404;500`, has examples `False`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-CORE-simulation-service`.

<!-- op: spec=api-specs/Platform_setup_-_Rates_and_fees.yaml method=GET path=/v1/simulation/configs/attachment/account/{account_id} operationId=getAccountSimulationAttachment -->
### `GET /v1/simulation/configs/attachment/account/{account_id}` — Get account simulation config

- **operationId:** `getAccountSimulationAttachment`
- **Specification:** `api-specs/Platform_setup_-_Rates_and_fees.yaml` (Platform setup - Rates and fees)
- **Server base URL(s):** `https://sandbox.pismolabs.io/rates`
- **Tags:** `Simulation`
- **Deprecated in specification:** no
- **Security requirement:** `bearerAuth`

**Description (from the specification):**

> Get the ID of the simulation configuration attached to an account.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `account_id` | path | yes | integer | Pismo account ID |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `SimulationConfigIdPayload`) |
| 400 | Bad request | `application/json`: object (schema `BadRequestError`) |
| 404 | Simulation configuration not found | `application/json`: object (schema `NotFoundSimulationConfigError`) |
| 500 | Internal Server Error | `application/json`: object (schema `Error`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `config_id` | string | no | Simulation configuration ID | example: "477589-59572-95734" |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;404;500`, has examples `False`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-LEND-simulate-loans`.

<!-- op: spec=api-specs/Platform_setup_-_Rates_and_fees.yaml method=DELETE path=/v1/simulation/configs/attachment/account/{account_id} operationId=detachAccountSimulationConfig -->
### `DELETE /v1/simulation/configs/attachment/account/{account_id}` — Detach account simulation config

- **operationId:** `detachAccountSimulationConfig`
- **Specification:** `api-specs/Platform_setup_-_Rates_and_fees.yaml` (Platform setup - Rates and fees)
- **Server base URL(s):** `https://sandbox.pismolabs.io/rates`
- **Tags:** `Simulation`
- **Deprecated in specification:** no
- **Security requirement:** `bearerAuth`

**Description (from the specification):**

> Detach simulation configuration from an account.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `account_id` | path | yes | integer | Pismo account ID |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK |  |
| 400 | Bad request | `application/json`: object (schema `BadRequestError`) |
| 404 | Simulation configuration not found | `application/json`: object (schema `NotFoundSimulationConfigError`) |
| 500 | Internal Server Error | `application/json`: object (schema `Error`) |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;404;500`, has examples `False`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Platform_setup_-_Rates_and_fees.yaml method=GET path=/v1/simulation/configs/attachments operationId=getSimulationAttachments -->
### `GET /v1/simulation/configs/attachments` — Get simulation attachments

- **operationId:** `getSimulationAttachments`
- **Specification:** `api-specs/Platform_setup_-_Rates_and_fees.yaml` (Platform setup - Rates and fees)
- **Server base URL(s):** `https://sandbox.pismolabs.io/rates`
- **Tags:** `Simulation`
- **Deprecated in specification:** no
- **Security requirement:** `bearerAuth`

**Description (from the specification):**

> Retrieve simulation attachment details based on the filters

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `simulation_config_id` | query | no | string | Filter by Simulation configuration ID |  |
| `attachment_type` | query | no | string | Filter by attachment type | enum: ["PROGRAM", "ACCOUNT", "TENANT"] |
| `program_id` | query | no | string | Filter by program ID |  |
| `account_id` | query | no | string | Filter by account ID |  |
| `page` | query | no | integer | page number for pagination | format: "int64" |
| `per_page` | query | no | integer | items per page for pagination | format: "int64" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object |
| 400 | Bad request | `application/json`: object (schema `BadRequestError`) |
| 500 | Internal Server Error | `application/json`: object (schema `Error`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `items` | array of object (schema `SimulationAttachmentResponse`) | no |  |  |
| `pages` | integer | no |  | format: "int64"; example: 1 |
| `per_page` | integer | no |  | format: "int64"; example: 10 |
| `total_items` | integer | no |  | format: "int64"; example: 1 |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;500`, has examples `True`, emits events `0`, deprecated `False`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/SimulationConfigListResponse -->
### Schema `SimulationConfigListResponse`

Pointer: `#/components/schemas/SimulationConfigListResponse`. Type: object (schema `SimulationConfigListResponse`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `simulation_config_id` | string | no | Simulation configuration ID |  |
| `has_attachments` | boolean | no | Indicates if attachment exists |  |
| `updated_at` | string | no | Last updated timestamp |  |
| `description` | string (schema `ConfigDescription`) | no | Simulation configuration description | example: "This is my simulation configurations" |

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

<!-- schema: #/components/schemas/Plans -->
### Schema `Plans`

Pointer: `#/components/schemas/Plans`. Type: object (schema `Plans`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | string | no | Customer plan identifier | pattern: "^[a-zA-Z0-9_-]+$"; maxLength: 36; example: "customId1" |
| `description` | string | no | Custom simulation plan description | maxLength: 255; example: "Electronics" |
| `engine` | string | no | Calculation engine type:<br>  `PISMO` - Uses Pismo's internal calculation methods (default). Requires `calculation_parameters`, `installments`, and `billing_method`.<br>  `EXTERNAL` - Delegates calculation to an external service. Requires `calculation_url` (set on update only).<br> | enum: ["EXTERNAL", "PISMO"]; default: "PISMO"; example: "PISMO" |
| `calculation_url` | string | no | URL of your external calculation endpoint.<br>**REQUIRED** when `engine` is `EXTERNAL`.<br>**IMPORTANT:** Cannot be provided during plan creation (POST) — set this field on the first update (PUT) after creation.<br>Once set, this URL is immutable and cannot be changed.<br>Your external engine must respond within 3 seconds.<br> | format: "uri"; example: "https://api.example.com/calculate" |
| `authentication` | object | no | Authentication configuration for external calculation engine. **REQUIRED** when `engine` is `EXTERNAL`. |  |
| `authentication.authentication_method` | string | no | Authentication method for calling your external engine. | enum: ["JWT_DEFAULT"]; default: "JWT_DEFAULT"; example: "JWT_DEFAULT" |
| `calculation_parameters` | oneOf: object (schema `SimulationCalculationPriceTable`), object (schema `SimulationCalculationDailyPercentage`), object (schema `SimulationCalculationEqualInstallments`) | no | Calculation parameters for Pismo's internal calculation methods.<br>**REQUIRED** when `engine` is `PISMO` or not specified.<br>**MUST NOT** be provided when `engine` is `EXTERNAL`.<br> |  |
| `interest_limitation` | object (schema `SimulationInterestLimitation`) | no |  |  |
| `down_payment_method` | object (schema `SimulationDownPaymentMethod`) | no |  |  |
| `installments` | array of integer | no | Array containing the installment numbers for which the plan is applicable. **REQUIRED** when `engine` is `PISMO`. | example: [6, 10, 12] |
| `billing_method` | string | no | Plan billing method. **REQUIRED** when `engine` is `PISMO`.<br>  `BNPL` - Field `frequency` is **REQUIRED**<br>  `CARD` - Field `frequency` is the same as the card, and the field should be **NULL**.<br> | enum: ["BNPL", "CARD"]; example: "BNPL" |
| `frequency` | string | no | Frequency of the billing. Required for billing_method = `BNPL` | enum: ["MONTHLY", "WEEKLY", "BIWEEKLY"]; example: "MONTHLY" |
| `installment_parameters` | object (schema `SimulationInstallmentParameters`) | no |  |  |
| `filters` | object | no | Simulation configuration filters |  |
| `filters.merchants` | array of string | no | Array containing the merchants for whom the plan applies | example: ["abcdef"]; items.maxLength: 255 |
| `filters.processing_codes` | array of string | no | Array containing the processing codes for whom the plan applies | example: ["01", "02"]; items.maxLength: 255 |
| `filters.custom_filters` | array of string | no | Array containing plan custom filters | example: ["custom_filter_01", "custom_filter_02"]; items.maxLength: 255 |

<!-- schema: #/components/schemas/PlansOutput -->
### Schema `PlansOutput`

Pointer: `#/components/schemas/PlansOutput`. Type: object (schema `PlansOutput`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | string | no | Customer plans identifier | example: "customId1" |
| `description` | string | no | Plan configuration description | example: "Electronic" |

<!-- schema: #/components/schemas/NotFoundSimulationConfigError -->
### Schema `NotFoundSimulationConfigError`

Pointer: `#/components/schemas/NotFoundSimulationConfigError`. Type: object (schema `NotFoundSimulationConfigError`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `error_code` | string | no | Error code ID | example: "RCAPI-NOT_FOUND-VIOLATION" |
| `message` | string | no | Error description. | example: "Simulation configuration with the provided key does not exist" |

<!-- schema: #/components/schemas/SimulationAttachmentResponse -->
### Schema `SimulationAttachmentResponse`

Pointer: `#/components/schemas/SimulationAttachmentResponse`. Type: object (schema `SimulationAttachmentResponse`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `simulation_config_id` | string | no | Simulation configuration ID |  |
| `attachment_type` | string | no | Attachment Type |  |
| `program_id` | string \\\| null | no | Program ID when `attachment_type` is `PROGRAM` |  |
| `account_id` | string \\\| null | no | Account ID when `attachment_type` is `ACCOUNT` |  |
| `org_id` | string \\\| null | no | Organization ID when `attachment_type` is `TENANT` |  |

<!-- schema: #/components/schemas/SimulationCalculationPriceTable -->
### Schema `SimulationCalculationPriceTable`

Pointer: `#/components/schemas/SimulationCalculationPriceTable`. Type: object (schema `SimulationCalculationPriceTable`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `calculation_method` | string | yes | Calculation method - `PRICE_TABLE`. | enum: ["PRICE_TABLE"] |
| `index` | string | no | Define range type when interest rate is dynamic. | enum: ["INSTALLMENT"] |
| `fixed` | number | no | Fixed fee amount as decimal field. | example: 50 |
| `percentage` | number | no | Percentage amount as decimal field. | example: 1.3 |
| `fixed_iof_rate` | number | yes | Percentage amount as decimal field. IOF = Brazilian tax. | example: 0.38 |
| `daily_iof_rate` | number | yes | Percentage amount as decimal field. IOF = Brazilian tax. | example: 0.0082 |
| `interest_rate` | object (schema `InterestRate`) | yes |  |  |

<!-- schema: #/components/schemas/SimulationCalculationDailyPercentage -->
### Schema `SimulationCalculationDailyPercentage`

Pointer: `#/components/schemas/SimulationCalculationDailyPercentage`. Type: object (schema `SimulationCalculationDailyPercentage`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `calculation_method` | string | yes | Calculation method - `DAILY_PERCENTAGE`. Applied to credit card cash advances and other loan-type products. | enum: ["DAILY_PERCENTAGE"] |
| `value` | number | yes | Percentage amount as decimal field. | example: 0.3 |
| `identifier` | string | yes | Plan identifier used to reference this daily percentage strategy. | pattern: "^[a-zA-Z0-9_-]+$"; maxLength: 36; example: "daily-pct-01" |

<!-- schema: #/components/schemas/SimulationCalculationEqualInstallments -->
### Schema `SimulationCalculationEqualInstallments`

Pointer: `#/components/schemas/SimulationCalculationEqualInstallments`. Type: object (schema `SimulationCalculationEqualInstallments`).

> Calculation parameters for the `EQUAL_INSTALLMENTS` method. Produces equal amortization installments with a fixed or dynamic interest rate and optional internal fees (e.g., IOF).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `calculation_method` | string | yes | Calculation method - `EQUAL_INSTALLMENTS`. | enum: ["EQUAL_INSTALLMENTS"] |
| `day_count_method` | string (schema `DayCountMethod`) | no | Day count convention used to calculate interest | enum: ["MONTH_30_YEAR_360", "MONTH_ACTUAL_YEAR_365"]; example: "MONTH_30_YEAR_360" |
| `interest_rate` | object (schema `InterestRate`) | yes |  |  |
| `identifier` | string | yes | Plan identifier used to reference this equal installments strategy. | pattern: "^[a-zA-Z0-9_-]+$"; maxLength: 36; example: "equal-inst-01" |
| `fees` | array of object (schema `SimulationStrategyInternalFee`) | no | List of internal fees applied within the installment calculation (e.g., IOF).<br>Supported strategies: `PERCENTAGE`, `FIXED`, `DAILY_PERCENTAGE`, `IOF`.<br> |  |

<!-- schema: #/components/schemas/SimulationInterestLimitation -->
### Schema `SimulationInterestLimitation`

Pointer: `#/components/schemas/SimulationInterestLimitation`. Type: object (schema `SimulationInterestLimitation`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `calculation_basis` | string | yes | Basis used to calculate the interest limitation. | enum: ["PRINCIPAL_AMOUNT"]; example: "PRINCIPAL_AMOUNT" |
| `percentage` | number | yes | Maximum interest percentage allowed over the life of the plan. | example: 3.2 |

<!-- schema: #/components/schemas/SimulationDownPaymentMethod -->
### Schema `SimulationDownPaymentMethod`

Pointer: `#/components/schemas/SimulationDownPaymentMethod`. Type: object (schema `SimulationDownPaymentMethod`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `type` | string | yes | Down payment calculation method:<br>  `PERCENTAGE` - Field `value` is **REQUIRED**; the down payment is a percentage of the transaction amount (max 100).<br>  `INSTALLMENT_EQUIVALENT` - Field `value` must be absent; the down payment equals one installment value.<br> | enum: ["PERCENTAGE", "INSTALLMENT_EQUIVALENT"]; example: "PERCENTAGE" |
| `value` | number | no | Percentage value for the down payment. **REQUIRED** when `type` is `PERCENTAGE`.<br>Must be absent when `type` is `INSTALLMENT_EQUIVALENT`.<br> | maximum: 100; example: 20 |

<!-- schema: #/components/schemas/SimulationInstallmentParameters -->
### Schema `SimulationInstallmentParameters`

Pointer: `#/components/schemas/SimulationInstallmentParameters`. Type: object (schema `SimulationInstallmentParameters`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `minimum_installment_value` | object | no |  | example: {"type": "FIXED", "value": 10} |
| `minimum_installment_value.type` | string | no | Value type:<br>  `FIXED` - a single scalar `value` applies to all installments.<br>  `DYNAMIC` - per-installment values provided in the `values` map.<br> | enum: ["FIXED", "DYNAMIC"]; example: "FIXED" |
| `minimum_installment_value.value` | number | no | Minimum installment value (used when `type` is `FIXED`). | example: 100 |
| `minimum_installment_value.values` | object (map of number) | no | Map of installment number (as string key) to minimum value.<br>Used when `type` is `DYNAMIC`. Example: `{"1": 50.0, "2": 100.0}`.<br> | example: {"2": 100, "3": 150} |
| `number_of_initial_periods_to_skip` | object | no | Number of initial installments to be skipped before billing starts. | example: {"type": "FIXED", "value": 1} |
| `number_of_initial_periods_to_skip.type` | string | no | Value type:<br>  `FIXED` - a single scalar `value` applies.<br>  `DYNAMIC` - per-installment values provided in the `values` map.<br> | enum: ["FIXED", "DYNAMIC"]; example: "FIXED" |
| `number_of_initial_periods_to_skip.value` | integer | no | Number of periods to skip (used when `type` is `FIXED`). | example: 1 |
| `number_of_initial_periods_to_skip.values` | object (map of integer) | no | Map of installment number (as string key) to number of periods to skip.<br>Used when `type` is `DYNAMIC`.<br> | example: {"2": 1, "3": 3} |

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

<!-- schema: #/components/schemas/SimulationStrategyInternalFee -->
### Schema `SimulationStrategyInternalFee`

Pointer: `#/components/schemas/SimulationStrategyInternalFee`. Type: object (schema `SimulationStrategyInternalFee`).

> Internal fee applied within the Equal Installments calculation.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `calculation` | string | yes | Fee calculation strategy. | enum: ["PERCENTAGE", "FIXED", "DAILY_PERCENTAGE", "IOF"]; example: "PERCENTAGE" |
| `id` | string | yes | Fee identifier. | maxLength: 36; example: "IOF" |
| `precedence` | integer | yes | Fee calculation order. Lower numbers are applied first. | minimum: 0; example: 0 |
| `value` | number | no | Fee value as a decimal. Required for `PERCENTAGE`, `FIXED`, and `DAILY_PERCENTAGE` strategies. | example: 0.38 |
| `calculation_basis` | string | yes | Calculation basis for the fee. | enum: ["PRINCIPAL_AMOUNT", "CONTRACT_AMOUNT"]; example: "PRINCIPAL_AMOUNT" |
| `fixed_iof_rate` | number | no | Fixed IOF rate as a decimal. Required when `calculation` is `IOF`. | example: 0.38 |
| `daily_iof_rate` | number | no | Daily IOF rate as a decimal. Required when `calculation` is `IOF`. | example: 0.0082 |

<!-- schema: #/components/schemas/InterestRateRule -->
### Schema `InterestRateRule`

Pointer: `#/components/schemas/InterestRateRule`. Type: object (schema `InterestRateRule`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `minimum` | number | yes | First installment the rule is applied to. For example, if you enter "4", rule application begins on the 4th installment.<br>Must be 1 or higher.<br> | minimum: 1; example: 10 |
| `maximum` | number | yes | Last installment the rule is applied to. For example, if you enter "10", rule application ends after the 10th installment.<br> | maximum: 70; example: 30 |
| `calculation` | object (schema `RuleCalculation`) | yes |  |  |
| `progression` | object (schema `Progression`) | no | Rate progression configuration. |  |

<!-- schema: #/components/schemas/RuleCalculation -->
### Schema `RuleCalculation`

Pointer: `#/components/schemas/RuleCalculation`. Type: object (schema `RuleCalculation`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `calculation_method` | string (schema `CalculationMethodSubset`) | yes | Calculation method. | enum: ["FIXED", "PERCENTAGE"]; example: "FIXED" |
| `value` | number | yes | Value to be applied | example: 0.04 |

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
| `api-specs/Platform_setup_-_Rates_and_fees.yaml` | tag `Simulation`: GET /v1/simulation/configs, POST /v1/simulation/configs, GET /v1/simulation/configs/{simulation_config_id}, PUT /v1/simulation/configs/{simulation_config_id}, PUT /v1/simulation/configs/{simulation_config_id}/attachment/tenant, GET /v1/simulation/configs/attachment/tenant, PUT /v1/simulation/configs/{simulation_config_id}/attachment/program/{program_id}, GET /v1/simulation/configs/attachment/program/{program_id}, DELETE /v1/simulation/configs/attachment/program/{program_id}, PUT /v1/simulation/configs/{simulation_config_id}/attachment/account/{account_id}, GET /v1/simulation/configs/attachment/account/{account_id}, DELETE /v1/simulation/configs/attachment/account/{account_id}, GET /v1/simulation/configs/attachments | https://github.com/PismoDevEx/pismo-api-specs | `0a918b57bd00f81c…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-CORE-fee-models-create-and-simulate` — Creating, applying and simulating fee models
- `KU-CORE-simulation-service` — Simulation service
- `KU-LEND-simulate-loans` — Simulate loans
