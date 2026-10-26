---
ku_id: KU-CORE-balance-configurations
title: Balance configurations and filter templates
category: core_platform
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/core-platform/balances-configurations-overview.md
  sha256: e60d58ea45a457a8f246fbbb098fb4375e8372f5480fbce9fbf65a186e4a7f3f
  url: https://developers.pismo.io/pismo-docs/docs/balances-configurations-overview
  role: primary_guide
  updated_at: '2026-06-01T15:51:22.000Z'
- path: docs/core-platform/filter-templates.md
  sha256: 1e00b9906abf8ad437ea58e8ea9c8c0337d71c1a2fb8568994a206d0c0d869d6
  url: https://developers.pismo.io/pismo-docs/docs/filter-templates
  role: primary_guide
  updated_at: '2026-07-29T12:01:36.000Z'
operations:
- get-v1-filter-template-by-id
- get-v1-filter-templates
- post-v1-balances-config
- post-v1-filter-templates
- put-v1-filter-template
related_kus:
- KU-API-core-platform-balance-config-beta--balance-configurations
- KU-API-core-platform-balance-config-beta--filter-templates
- KU-CC-balance-configurations
- KU-CORE-balance-configuration-use-cases
- KU-CORE-processing-codes-and-transaction-types
grouping_rationale: Concept and its filter templates.
---

# Balance configurations and filter templates

**KU ID:** `KU-CORE-balance-configurations` · **Category:** Core platform · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 2 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: Concept and its filter templates.

Scope as stated in `docs/core-platform/balances-configurations-overview.md`:

> Balance configurations are a flexible set of rules that define how the Pismo platform impacts account balances and limits based on transaction activity. You can create balance configurations to manage account balances for your card and banking transactions. This robust functionality allows you to configure different scenarios to meet your business needs.

Scope as stated in `docs/core-platform/filter-templates.md`:

> This guide provides step-by-step guidance how to create and manage filter templates and use them in balance configurations.  It also explains how to maintain and update filter logic efficiently.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/core-platform/balances-configurations-overview.md`: Balance configurations overview; Related topics
- `docs/core-platform/filter-templates.md`: Balance configuration filter templates; When to use filter templates; Validation rules; Create filter template; Validate template creation; Use template in balance configuration; Update filter template; List templates; Migrate inline filters to templates; Before (inline filters); After (using template); Best practices; Reusability; Naming conventions; Governance; Change management

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 5 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/core-platform/balances-configurations-overview.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/balances-configurations-overview · updatedAt: 2026-06-01T15:51:22.000Z

<!-- source:begin path=docs/core-platform/balances-configurations-overview.md part=0-end -->

# Balance configurations overview

Balance configurations are a flexible set of rules that define how the Pismo platform impacts account balances and limits based on transaction activity. You can create balance configurations to manage account balances for your card and banking transactions. This robust functionality allows you to configure different scenarios to meet your business needs.

You can create, edit, and list balance configurations via Control Center or API.

* Use [Control Center](https://developers.pismo.io/pismo-docs/docs/balance-configurations-in-control-center) to manage balance configurations at the program level.
* Use the [balance configurations](https://developers.pismo.io/pismo-docs/reference/post-v1-balances-config) API to manage balance configurations at the organization, program, or account level. Refer to [balance configuration use cases](https://developers.pismo.io/pismo-docs/docs/balance-configuration-use-cases) for configuration examples via API.

<Image align="center" alt="Balance configurations diagram" width="700px" src="https://files.readme.io/3f90b16df47761014040f718426b44912c926e98dfa9d1b65eeb608050cdc1cc-image.png" />

Balance configurations consist of the following concepts.

* The `level` field in the API allows you to apply a balance configuration to an organization, program, or account. This is not available in Control Center because there you can define configurations only at the program level.
* Each configuration has a **name**. In the API, you define each configuration in the `config` field and set its name in the `name` field.
* Each configuration can be set as **active** (activated when created) or **inactive** (created but not activated). In the API, you manage this in the `is_active` field.
* Each configuration contains **filters** and **scenarios**.
  * A **filter** defines how to apply a configuration using [processing codes](https://developers.pismo.io/pismo-docs/docs/processing-codes-and-transaction-types) (required), currency codes, Merchant Category Codes (MCCs), or number of installments. In the API, you manage this in the `filter` object.
    <Callout icon="📘" theme="info">
      For card network authorizations, you must configure the appropriate processing code for the correct network brand. This is necessary because the platform receives the processing code externally during the authorization workflow and uses it to correctly match the transaction against the balance configuration.
    </Callout>
  * A **scenario** defines an evaluated **condition**, specifies which account balances and limits to **consider**, and which balances and limits to **impact**. In the API, you can manage this in the `scenario` object, which contains the `condition` and `result` objects.
* The **condition** can be of either a **default** or **custom** type. You define one **default** condition. You can have many **custom** conditions and define in which order the platform should check them. The  platform checks conditions in the priority order you set, with the default condition always checked and applied last.  In the API, you manage the condition type and order inside the `condition` object in the `type` and `order` fields.
* When a transaction is processed, the platform evaluates (or **considers**) defined balances and limits to determine whether to apply the debit. In the API, the `result.consider` field tells the platform which balances or limits should be checked as part of this evaluation.
* Each scenario defines which account balances and limits to **impact** when the conditions meet the criteria defined in this configuration. In the API, you define this in the `result.impact` field.

# Related topics

* [Balance configurations in Control Center](https://developers.pismo.io/pismo-docs/docs/balance-configurations-in-control-center)
* [Balance configurations API](https://developers.pismo.io/pismo-docs/reference/post-v1-balances-config)
* [Balance configuration use cases](https://developers.pismo.io/pismo-docs/docs/balance-configuration-use-cases)
<!-- source:end -->

### Source 2: `docs/core-platform/filter-templates.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/filter-templates · updatedAt: 2026-07-29T12:01:36.000Z

<!-- source:begin path=docs/core-platform/filter-templates.md part=0-end -->

# Balance configuration filter templates

This guide provides step-by-step guidance how to create and manage filter templates and use them in balance configurations.  It also explains how to maintain and update filter logic efficiently.

When [creating a balance configuration](https://developers.pismo.io/pismo-docs/reference/post-v1-balances-config), you can specify filters in the `filters` field or you can refer to a predefined filter template in the `filter_template_id` field. When the Pismo platform processes a transaction, it reads the `filter_template_id`, retrieves the associated template, and applies filters exactly as if they were inline.

# When to use filter templates

Use filter templates with balance configurations when:

* It makes sense to reuse the same filter logic across multiple configurations
* You want to set up centralized control over filtering rules
* You expect frequent updates to filter logic

# Validation rules

When [creating a balance configuration](https://developers.pismo.io/pismo-docs/reference/post-v1-balances-config), the following are valid balance configurations.

* When only `filter_template_id` is provided.
* When only `filters` are provided (legacy mode).

The following invalid balance configurations return errors.

| Scenario                                            | Error           |
| :-------------------------------------------------- | :-------------- |
| Both `filter_template_id` and `filters` provided    | 400 Bad Request |
| Neither `filter_template_id` and `filters` provided | 400 Bad Request |
| Template not found                                  | 404 Not Found   |

# Create filter template

Use the [Create filter template](https://developers.pismo.io/pismo-docs/reference/post-v1-filter-templates)  endpoint to create a reusable filter definition.

In the following request payload example, a new filter template called `transport` defines a processing code (PC), a number of minimum and maximum installments, two Merchant Category Codes (MCCs), and a currency code.

```json
{
  "id": "transport",
  "description": "Transportation-related transactions",
  "filters": {
    "processing_codes": [
      "01"
    ],
    "min_installments": 1,
    "max_installments": 12,
    "mcc": [
      "1234", 
      "5678"
    ],
    "currency_code": "USD"
  }
}
```

<Callout icon="📘" theme="info">
  Important considerations

  * The `id` value must be unique per organization and cannot exceed 36 characters.
  * The `description` value must be a maximum of 50 characters.
  * The `filters` must follow the existing balance configuration filter structure.
</Callout>

# Validate template creation

Use the [Get filter template](https://developers.pismo.io/pismo-docs/reference/get-v1-filter-template-by-id)  endpoint to retrieve the created template by its ID and verify the template was created successfully.

# Use template in balance configuration

Use the [Create balance configuration](https://developers.pismo.io/pismo-docs/reference/post-v1-balances-config)  endpoint to reference the template in the `filter_template_id` field.

```json
{
  "level": "account",
  "account_id": 999,
  "configs": [
    {
      "filter_template_id": "transport",
      "is_active": true,
      "scenarios": [
        {
          "condition": {
            "order": 1,
            "type": "default"
          },
          "result": {
            "impact": [
              "AvailableCreditLimit"
            ],
            "amount": "contract_amount"
          }
        }
      ]
    }
  ]
}
```

# Update filter template

Use the [Update filter template](https://developers.pismo.io/pismo-docs/reference/put-v1-filter-template)  endpoint to modify an existing template. The changes automatically apply to all balance configurations that use this template, so there's no need to update individual configurations.

The following request payload adds a new processing code (`02`) and a new MCC (`9999`) to the existing filter template (`transport`).

```json
{
  "description": "Transport-related transactions",
  "filters": {
    "processing_codes": [
      "01", 
      "02"
    ],
    "mcc": [
      "1234", 
      "5678", 
      "9999"
    ],
    "currency_code": "USD"
  }
}
```

# List templates

Use the [List all filter templates](https://developers.pismo.io/pismo-docs/reference/get-v1-filter-templates) endpoint to list every balance configuration template available to the organization and ensure reuse instead of duplication.

# Migrate inline filters to templates

1. Identify duplicated filter logic across balance configurations.
2. Create a filter template with that logic.
3. Replace inline filters with `filter_template_id`.
4. Validate configurations.

## Before (inline filters)

```json
{
  "filters": {
    "processing_codes": [
    "01"
    ],
    "min_installments": 1,
    "max_installments": 12,
    "mcc": [
    "1234", 
    "5678"
    ],
    "currency_code": "USD"
  }
}
```

## After (using template)

```json
{
  "filter_template_id": "transport"
}
```

# Best practices

## Reusability

Create filter templates for:

* PC lists
* MCC groups
* Currency-based filters
* Installment-based rules

## Naming conventions

Use descriptive filter template IDs. For example:

* `transport_domestic`
* `ecommerce_usd`
* `installments_1_12`

## Governance

* Avoid duplicate templates
* Review existing templates before creating new ones

## Change management

Treat template updates carefully as changes impact all linked balance configurations.
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `POST /v1/balances-config` | `post-v1-balances-config` | Create balance configuration | `api-specs/Core_platform_-_Balance_config_Beta.yaml` | no | KU-API-core-platform-balance-config-beta--balance-configurations |
| `POST /v1/balances-config/filter-templates` | `post-v1-filter-templates` | Create filter template | `api-specs/Core_platform_-_Balance_config_Beta.yaml` | no | KU-API-core-platform-balance-config-beta--filter-templates |
| `GET /v1/balances-config/filter-templates/{id}` | `get-v1-filter-template-by-id` | Get filter template | `api-specs/Core_platform_-_Balance_config_Beta.yaml` | no | KU-API-core-platform-balance-config-beta--filter-templates |
| `PUT /v1/balances-config/filter-templates/{id}` | `put-v1-filter-template` | Update filter template | `api-specs/Core_platform_-_Balance_config_Beta.yaml` | no | KU-API-core-platform-balance-config-beta--filter-templates |
| `GET /v1/balances-config/filter-templates` | `get-v1-filter-templates` | List filter templates | `api-specs/Core_platform_-_Balance_config_Beta.yaml` | no | KU-API-core-platform-balance-config-beta--filter-templates |

### Operation essentials

- **`POST /v1/balances-config`** (`post-v1-balances-config`): security `BearerAuth`; required parameters `x-tenant` (header); required body fields none declared; response statuses 201, 400, 404, 500; error codes in examples `EBCF0321`, `EBCF0320`, `EBCF0317`, `EBLC9999`; events none listed.
- **`POST /v1/balances-config/filter-templates`** (`post-v1-filter-templates`): security `BearerAuth`; required parameters `x-tenant` (header); required body fields `id`, `filters`; response statuses 201, 400, 409, 500; error codes in examples none; events none listed.
- **`GET /v1/balances-config/filter-templates/{id}`** (`get-v1-filter-template-by-id`): security `BearerAuth`; required parameters `id` (path), `x-tenant` (header); required body fields none declared; response statuses 200, 404, 500; error codes in examples none; events none listed.
- **`PUT /v1/balances-config/filter-templates/{id}`** (`put-v1-filter-template`): security `BearerAuth`; required parameters `id` (path), `x-tenant` (header); required body fields `filters`; response statuses 200, 400, 404, 500; error codes in examples none; events none listed.
- **`GET /v1/balances-config/filter-templates`** (`get-v1-filter-templates`): security `BearerAuth`; required parameters `x-tenant` (header); required body fields none declared; response statuses 200, 400, 500; error codes in examples none; events none listed.

## Lifecycle status

- `docs/core-platform/balances-configurations-overview.md`: updatedAt 2026-06-01T15:51:22.000Z.
- `docs/core-platform/filter-templates.md`: updatedAt 2026-07-29T12:01:36.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- None identified by the migration checks.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/core-platform/balances-configurations-overview.md` | whole document | https://developers.pismo.io/pismo-docs/docs/balances-configurations-overview | `e60d58ea45a457a8…` | 2026-06-01T15:51:22.000Z |
| `docs/core-platform/filter-templates.md` | whole document | https://developers.pismo.io/pismo-docs/docs/filter-templates | `1e00b9906abf8ad4…` | 2026-07-29T12:01:36.000Z |

## Related knowledge units

- `KU-API-core-platform-balance-config-beta--balance-configurations` — API reference: Core platform - Balance configurations — Balance configurations
- `KU-API-core-platform-balance-config-beta--filter-templates` — API reference: Core platform - Balance configurations — Filter templates
- `KU-CC-balance-configurations` — Control Center balance configurations
- `KU-CORE-balance-configuration-use-cases` — Balance configuration use cases
- `KU-CORE-processing-codes-and-transaction-types` — Processing codes
