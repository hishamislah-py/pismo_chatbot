---
ku_id: KU-CORE-simulation-service
title: Simulation service
category: core_platform
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/core-platform/simulation-service.md
  sha256: bc49f4f2249fd82e4fe594fa568b6ae309a5a23a7806b24cbaa916228e06625f
  url: https://developers.pismo.io/pismo-docs/docs/simulation-service
  role: primary_guide
  updated_at: '2026-06-08T17:05:49.000Z'
operations:
- attachAccountSimulationConfig
- attachOrgSimulationConfig
- attachProgramSimulationConfig
- post-v1-simulation
- simulationConfigs
related_kus:
- KU-API-core-platform-payment-methods-admin--simulation
- KU-API-platform-setup-rates-and-fees--simulation
grouping_rationale: single source page
---

# Simulation service

**KU ID:** `KU-CORE-simulation-service` · **Category:** Core platform · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/core-platform/simulation-service.md`:

> The simulation service allows you to generate simulations for customized payment options. These simulations return predicted information about specified options and provide flexibility in analyzing different conditions.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/core-platform/simulation-service.md`: Simulation service

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 5 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/core-platform/simulation-service.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/simulation-service · updatedAt: 2026-06-08T17:05:49.000Z

<!-- source:begin path=docs/core-platform/simulation-service.md part=0-end -->

# Simulation service

The simulation service allows you to generate simulations for customized payment options. These simulations return predicted information about specified options and provide flexibility in analyzing different conditions.

Perform the following steps to configure the simulation service:

1. [Create a simulation configuration](https://developers.pismo.io/pismo-docs/reference/simulationconfigs) for a customized payment option.
2. Attach a simulation configuration to the required Pismo entity, such as [Attach simulation config to an account](https://developers.pismo.io/pismo-docs/reference/attachaccountsimulationconfig), [Attach simulation config to a program](https://developers.pismo.io/pismo-docs/reference/attachprogramsimulationconfig), or [Attach simulation config to an organization](https://developers.pismo.io/pismo-docs/reference/attachorgsimulationconfig).
3. [Create a simulation](https://developers.pismo.io/pismo-docs/reference/post-v1-simulation) by providing required information such as simulation transaction amount, authorization mode, document number or PAN, plan IDs from the simulation configuration, and merchant IDs.

When you run a simulation, the platform validates provided data to ensure it aligns with the simulation’s scope such available balance and active card status. The platform then generates the simulation, allowing you to predict the expected behavior based on the submitted parameters. The platform returns details of the created simulation that include account and program information and associated configurations.
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `POST /v1/simulation/configs` | `simulationConfigs` | Create simulation config | `api-specs/Platform_setup_-_Rates_and_fees.yaml` | no | KU-API-platform-setup-rates-and-fees--simulation |
| `PUT /v1/simulation/configs/{simulation_config_id}/attachment/account/{account_id}` | `attachAccountSimulationConfig` | Attach simulation config to account | `api-specs/Platform_setup_-_Rates_and_fees.yaml` | no | KU-API-platform-setup-rates-and-fees--simulation |
| `PUT /v1/simulation/configs/{simulation_config_id}/attachment/program/{program_id}` | `attachProgramSimulationConfig` | Attach simulation config to program | `api-specs/Platform_setup_-_Rates_and_fees.yaml` | no | KU-API-platform-setup-rates-and-fees--simulation |
| `PUT /v1/simulation/configs/{simulation_config_id}/attachment/tenant` | `attachOrgSimulationConfig` | Attach simulation config to org | `api-specs/Platform_setup_-_Rates_and_fees.yaml` | no | KU-API-platform-setup-rates-and-fees--simulation |
| `POST /v1/simulations` | `post-v1-simulation` | Create simulation | `api-specs/Core_platform_-_Payment_methods_admin.yaml` | no | KU-API-core-platform-payment-methods-admin--simulation |

### Operation essentials

- **`POST /v1/simulation/configs`** (`simulationConfigs`): security `bearerAuth`; required parameters none declared; required body fields `description`, `plans`; response statuses 200, 400, 401, 500; error codes in examples none; events none listed.
- **`PUT /v1/simulation/configs/{simulation_config_id}/attachment/account/{account_id}`** (`attachAccountSimulationConfig`): security `bearerAuth`; required parameters `simulation_config_id` (path), `account_id` (path); required body fields none declared; response statuses 200, 400, 404, 500; error codes in examples none; events none listed.
- **`PUT /v1/simulation/configs/{simulation_config_id}/attachment/program/{program_id}`** (`attachProgramSimulationConfig`): security `bearerAuth`; required parameters `simulation_config_id` (path), `program_id` (path); required body fields none declared; response statuses 200, 400, 404, 500; error codes in examples none; events none listed.
- **`PUT /v1/simulation/configs/{simulation_config_id}/attachment/tenant`** (`attachOrgSimulationConfig`): security `bearerAuth`; required parameters `simulation_config_id` (path); required body fields none declared; response statuses 200, 400, 404, 500; error codes in examples none; events none listed.
- **`POST /v1/simulations`** (`post-v1-simulation`): security not declared; required parameters none declared; required body fields `amount`, `authorization_mode`; response statuses 200, 400, 422, 500; error codes in examples `DO0002`, `SI001`, `SI003`; events none listed.

## Lifecycle status

- `docs/core-platform/simulation-service.md`: updatedAt 2026-06-08T17:05:49.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- None identified by the migration checks.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/core-platform/simulation-service.md` | whole document | https://developers.pismo.io/pismo-docs/docs/simulation-service | `bc49f4f2249fd82e…` | 2026-06-08T17:05:49.000Z |

## Related knowledge units

- `KU-API-core-platform-payment-methods-admin--simulation` — API reference: Core platform - Payment methods admin — Simulation
- `KU-API-platform-setup-rates-and-fees--simulation` — API reference: Platform setup - Rates and fees — Simulation
