---
ku_id: KU-CORE-fee-models-create-and-simulate
title: Creating, applying and simulating fee models
category: core_platform
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/core-platform/create-fee-model.md
  sha256: de30187b28f908121a2efa687469460084d074116e83aaaa2cc120841769e694
  url: https://developers.pismo.io/pismo-docs/docs/create-fee-model
  role: primary_guide
  updated_at: '2026-04-24T02:14:19.000Z'
- path: docs/core-platform/simulating-fee-models.md
  sha256: 0e4ce651e7c03eb7eff31731f1bfd35275efd2c2c63974e90a343a1549b62435
  url: https://developers.pismo.io/pismo-docs/docs/simulating-fee-models
  role: primary_guide
  updated_at: '2026-04-24T02:07:09.000Z'
operations:
- attachOrgSimulationConfig
- attachmentByAccount
- attachmentByProgram
- attachmentByTenant
- getSimulationConfigs
- post-authorization
- post-v1-accumulator-config
- postModel
- post_v1-authorizations
- simulationConfigs
related_kus:
- KU-API-card-issuing-authorization--authorizations
- KU-API-core-platform-accumulator--configuration
- KU-API-core-platform-payment-methods--payment-methods-part-01
- KU-API-platform-setup-rates-and-fees--fee-models
- KU-API-platform-setup-rates-and-fees--simulation
- KU-CARD-simulate-authorizations
- KU-CORE-iof-fee-model
- KU-CORE-processing-codes-and-transaction-types
- KU-EVT-catalogue-other-domains
grouping_rationale: Create then test.
---

# Creating, applying and simulating fee models

**KU ID:** `KU-CORE-fee-models-create-and-simulate` · **Category:** Core platform · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 2 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: Create then test.

Scope as stated in `docs/core-platform/create-fee-model.md`:

> Use the [Create fee model](https://developers.pismo.io/pismo-docs/reference/postmodel) endpoint to create a new fee model. You can also create, define, and link fee models in Control Center. A fee model must have ALL fees and taxes that should be applied to the organization, program, or account level. A fee model is compounded by the sum of fees and each level (organization, program, or account) can have only one fee model attached. Therefore, it is important to make sure that each fee model has all fees included. Pismo will differentiate one fee from another by the processing code indicated for each fee, assuring that each fee will be correctly applied.

Scope as stated in `docs/core-platform/simulating-fee-models.md`:

> Simulation is a Pismo calculation service that allows you to simulate financial scenarios before any actual impact occurs on an account, credit limit, authorization, or accounting records. It is primarily used to simulate installment plans, interest, fees, and future values, returning payment options so you can choose the best alternative.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/core-platform/create-fee-model.md`: Creating and applying fee models; Apply a fee model; Sample fee model payloads
- `docs/core-platform/simulating-fee-models.md`: Simulating and testing fee models; Simulation features; Downpayment methods; Testing the fee model

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 10 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/core-platform/create-fee-model.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/create-fee-model · updatedAt: 2026-04-24T02:14:19.000Z

<!-- source:begin path=docs/core-platform/create-fee-model.md part=0-end -->

# Creating and applying fee models

Use the [Create fee model](https://developers.pismo.io/pismo-docs/reference/postmodel) endpoint to create a new fee model. You can also create, define, and link fee models in Control Center. A fee model must have ALL fees and taxes that should be applied to the organization, program, or account level. A fee model is compounded by the sum of fees and each level (organization, program, or account) can have only one fee model attached. Therefore, it is important to make sure that each fee model has all fees included. Pismo will differentiate one fee from another by the processing code indicated for each fee, assuring that each fee will be correctly applied.

For each model, you specify an array of one or more fee objects (the`fees` property). This object contains (in addition to other properties) a `calculation` object, consisting of a `calculation_method`and one or more other properties which vary depending on the calculation. The `calculation_method` is the method the fee model uses to calculate that particular fee.

The Pismo platform supports the following fee model calculation methods (represented by their enums):

* `FIXED`—Applies fixed amount fees to specified transactions.\
  Example: apply 5 USD on withdrawal.
* `PERCENTAGE`—Applies a percentage fee amount to specified transactions.\
  Example: apply 1% over a value.
* `GREATER`—Applies a fixed or percentage fee amount to specified transactions depending on which is greater.\
  Example: apply 1% or 5 USD over 100 USD—5 USD will be applied.
* `DAILY_PERCENTAGE`—Applies a daily simple interest percentage to things like credit card cash advances and other loan type products until the next cycle closing.\
  Example: apply 0.0082% daily tax for 20 days (until cycle closing).
* `COMPOUND_INTEREST`—Defines when interest is compounded on loan type products.
* `ACCUMULATOR`—Collects totals based on specified transaction types and applies a fixed or percentage fee on a scheduled basis.\
  **Note:** This is a special case in that you must call the [Create accumulator configuration](https://developers.pismo.io/pismo-docs/reference/post-v1-accumulator-config) endpoint to get an identifier for the configuration you can use when creating an accumulator fee model.
* `DYNAMIC_BY_AMOUNT`—Calculation strategy that allows you to apply "automatic" fees over DC accounts (deposit accounts) for situations such as withdrawal before due date.
* `EQUAL_INSTALLMENTS`—Calculates loan repayments (or installment plans) so that all installments have the same total amount throughout the life of the contract. This method ensures a smooth and predictable cash flow for the card holder, while accurately reflecting the financial logic of interest accrual over time. Although the installment value remains constant, its composition changes over time. The interest is higher in the first installments and gradually decreases as the outstanding balance is reduced. The principal repayment is smaller at the beginning and increases over time, compensating for the reduction in interest.\
  For example, given the following details:

  * **Principal**: USD 1,000
  * **Interest rate**: 1% per month
  * **Term**: 5 months
  * **Method**: Equal Installments\
    The monthly installment calculated is USD 206.04 (total contract amount: USD 1030.02).\
    This would be the installment details for each of the five months:

    | Month | Amount     | How calculated                                |
    | :---- | :--------- | :-------------------------------------------- |
    | 1     | USD 206.04 | Principal amount of 196.04 plus interest 10   |
    | 2     | USD 206.04 | Principal amount of 198 plus interest 8.04    |
    | 3     | USD 206.04 | Principal amount of 199.98 plus interest 6.06 |
    | 4     | USD 206.04 | Principal amount of 201.98 plus interest 4.06 |
    | 5     | USD 206.04 | Principal amount of 204 plus interest 2.0     |

<br />

* `PRICE_TABLE` (Brazil only)—Calculates loan repayments (installment plans) so that all installments have the same total amount throughout the life of the contract, adding some specific fee calculations including the IOF amount being financed.
* `AGING` (Brazil only)—Determines how fees are calculated and applied to investments over time.
* `IOF` (Brazil only)—Determines how IOF (Brazilian tax) taxes are calculated for investments.\
  For details on IOF and a sample IOF fee model, refer to the [IOF fee model for Brazil](https://developers.pismo.io/pismo-docs/docs/iof-fee-model) guide.

# Apply a fee model

A new fee model is detached by default and not linked to anything. When you create a new fee model, you must link it to financial operations within an organization, program, or an account.

<Callout icon="📘" theme="info">
  One fee model at a time

  You can only link one fee model to an organization, program, or account at a time
</Callout>

You must link your fee model to an organization, program, or account based on processing codes, which identify the financial operation, such as purchases or debits. Each financial operation within the Pismo platform has its own processing code. You can configure some processing codes, while others are fixed in the card network flow. The fee is ignored if the operation doesn't match the defined processing codes.

Talk to your Pismo representative to get or create processing codes. For details on existing processing codes, refer to the [Processing codes](https://developers.pismo.io/pismo-docs/docs/processing-codes-and-transaction-types) guide.

You can link a fee model at the following levels of detail:

* **Organization level**—Link to all accounts in your organization, regardless of which program contains the account. To link your fee model to a organization, use the [Attach fee model to org](https://developers.pismo.io/pismo-docs/reference/attachmentbytenant) endpoint. You can also do this in Control Center.
* **Program level**—Link to all accounts within a specific program. To link your fee model to a program, use the [Attach fee model to program](https://developers.pismo.io/pismo-docs/reference/attachmentbyprogram) endpoint. You can also do this in Control Center.
* **Account level**—Link to selected accounts, regardless of which program they are in. To link your fee model to a specific account, use the [Attach fee model to account](https://developers.pismo.io/pismo-docs/reference/attachmentbyaccount) endpoint. You cannot link fee models at the account level through Control Center, you can only do this using the endpoint.

# Sample fee model payloads

You can find sample payloads for each fee model type in the [Create fee model](https://developers.pismo.io/pismo-docs/reference/postmodel) endpoint.

<Image align="center" alt="Screenshot of the list of sample fee model payloads" width="400px" src="https://files.readme.io/50105bfd1b21ddfe0573b93f2a524ed4505b1e82422b9267945e6c632e679f48-FeeModelMethodsList.png" />

<br />
<!-- source:end -->

### Source 2: `docs/core-platform/simulating-fee-models.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/simulating-fee-models · updatedAt: 2026-04-24T02:07:09.000Z

<!-- source:begin path=docs/core-platform/simulating-fee-models.md part=0-end -->

# Simulating and testing fee models

Simulation is a Pismo calculation service that allows you to simulate financial scenarios before any actual impact occurs on an account, credit limit, authorization, or accounting records. It is primarily used to simulate installment plans, interest, fees, and future values, returning payment options so you can choose the best alternative.

The Pismo Integrated Service Solution allows you to use our structure without the need for a long development period and major changes to your environment. Pismo offers a complete and personalized experience, with technology and precision, where parameterization occurs quickly and fluidly. The simulation solution is system agnostic, enabling various payment methods, increasing convenience and control.

Pismo provides the following simulation model endpoints for creating simulation parameters to specific types of financial flows:

* [Create simulation config](https://developers.pismo.io/pismo-docs/reference/simulationconfigs)
* [Attach simulation config](https://developers.pismo.io/pismo-docs/reference/attachorgsimulationconfig) (to organization, program, or account)
* [Get simulation config](https://developers.pismo.io/pismo-docs/reference/getsimulationconfigs)

# Simulation features

Simulation features include:

* **Price table**—Calculations are performed using the price method. This is a Brazil-specific calculation method and it includes:
  * **Fixed interest**—The same interest will be applied to all installments.
  * **Dynamic interest**—Interest will be applied dynamically according to the rule applied in the configuration.
  * **Public fees**—In Brazil, for example, the IOF and IOF Aliquot.
* **Filters**—Every fee you define for a simulation is given a `plan_id` that distinguishes it from other fees. It is not necessary to call all `plan_ids` individually, you can create filters for a selection of plans (fees), including processing codes, merchants, and custom filters. This allows you to create a group of simulations for a specific audience (for example, customers in the southern states).
* **Skip periods**—You can specify periods to skip. For example, start paying in 90 days or skip a payment in December.
* **Minimum installment**—Define that every installment must have a minimum value set. For example, minimum of $100.00.
* **Interest limitation**—Set a limit on the interest applied. For example, in Brazil, the government limits the interest rate to up to 100 percent of the original debt. In that case, principal\_amount: $100.00, maximum interest applied: $100.00 (100%).
* **Custom filters**—Use the custom filter to create a group of simulations for a specific audience. For example, you can create simulations geared toward a specific region or state, or specific to students.

## Downpayment methods

The simulation offers different downpayment methods:

* **Percentage**—A percentage is generated based on what you want to apply to the total contract value. The first installment will be issued on D+0.
  Example: 30% of R$1,000.00 = The down payment will be R$300.00.
* **Installment equivalent**—All installments are divided equally, assuming the first installment will be issued on D+0. To use this method, the simulation must be created after the payment cutoff date, and the payment will be made at the next invoice cutoff date.
  Example: R$1,000.00 contract = 10 installments of R$100.00.
* **Already done**—This is used when the consumer has already made part of the payment as a down payment.\
  Example: Contract for $1,000.00; down payment made: $200.00; the simulation will consider the difference in values, that is, $800.00. Down payment: $200.00 + 10 X $80.00.

  **Note**: If the first installment needs to be in the next cut, the installment input information will not be necessary in the `plan_id` configuration.

# Testing the fee model

To test network transactions scenarios, you can create and attach your feel model, then use the [Simulate authorization](https://developers.pismo.io/pismo-docs/reference/post_v1-authorizations) endpoint.

To test payments scenarios, you can create and attach your feel model, then use the [Request authorization](https://developers.pismo.io/pismo-docs/reference/post-authorization) endpoint.

For full details, refer to the [Simulate authorizations](https://developers.pismo.io/pismo-docs/docs/simulate-authorizations) guide.
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `POST /v1/fee/models` | `postModel` | Create fee model | `api-specs/Platform_setup_-_Rates_and_fees.yaml` | no | KU-API-platform-setup-rates-and-fees--fee-models |
| `POST /v1/accumulator-configs` | `post-v1-accumulator-config` | Create accumulator configuration | `api-specs/Core_platform_-_Accumulator.yaml` | no | KU-API-core-platform-accumulator--configuration |
| `PUT /v1/fee/models/{model_id}/attachment/tenant` | `attachmentByTenant` | Attach fee model to org | `api-specs/Platform_setup_-_Rates_and_fees.yaml` | no | KU-API-platform-setup-rates-and-fees--fee-models |
| `PUT /v1/fee/models/{model_id}/attachment/program/{program_id}` | `attachmentByProgram` | Attach fee model to program | `api-specs/Platform_setup_-_Rates_and_fees.yaml` | no | KU-API-platform-setup-rates-and-fees--fee-models |
| `PUT /v1/fee/models/{model_id}/attachment/account/{account_id}` | `attachmentByAccount` | Attach fee model to account | `api-specs/Platform_setup_-_Rates_and_fees.yaml` | no | KU-API-platform-setup-rates-and-fees--fee-models |
| `POST /v1/simulation/configs` | `simulationConfigs` | Create simulation config | `api-specs/Platform_setup_-_Rates_and_fees.yaml` | no | KU-API-platform-setup-rates-and-fees--simulation |
| `PUT /v1/simulation/configs/{simulation_config_id}/attachment/tenant` | `attachOrgSimulationConfig` | Attach simulation config to org | `api-specs/Platform_setup_-_Rates_and_fees.yaml` | no | KU-API-platform-setup-rates-and-fees--simulation |
| `GET /v1/simulation/configs/{simulation_config_id}` | `getSimulationConfigs` | Get simulation config | `api-specs/Platform_setup_-_Rates_and_fees.yaml` | no | KU-API-platform-setup-rates-and-fees--simulation |
| `POST /networktransactions/v1/authorizations` | `post_v1-authorizations` | Simulate authorization | `api-specs/Card_issuing_-_Authorization.yaml` | no | KU-API-card-issuing-authorization--authorizations |
| `POST /payment-methods/v1/authorization` | `post-authorization` | Request authorization | `api-specs/Core_platform_-_Payment_methods.yaml` | no | KU-API-core-platform-payment-methods--payment-methods-part-01 |

### Operation essentials

- **`POST /v1/fee/models`** (`postModel`): security `bearerAuth`; required parameters `Authorization` (header); required body fields `model_description`, `fees`; response statuses 201, 400, 401, 500; error codes in examples none; events none listed.
- **`POST /v1/accumulator-configs`** (`post-v1-accumulator-config`): security `BearerAuth`; required parameters none declared; required body fields `level`, `identifier`, `conditions`, `increase_type`; response statuses 201, 400, 409, 500; error codes in examples `WACM0001`, `WACM0002`; events none listed.
- **`PUT /v1/fee/models/{model_id}/attachment/tenant`** (`attachmentByTenant`): security `bearerAuth`; required parameters `model_id` (path); required body fields none declared; response statuses 200, 400, 404, 409, 500; error codes in examples none; events none listed.
- **`PUT /v1/fee/models/{model_id}/attachment/program/{program_id}`** (`attachmentByProgram`): security `bearerAuth`; required parameters `model_id` (path), `program_id` (path); required body fields none declared; response statuses 200, 400, 404, 409, 500; error codes in examples none; events none listed.
- **`PUT /v1/fee/models/{model_id}/attachment/account/{account_id}`** (`attachmentByAccount`): security `bearerAuth`; required parameters `model_id` (path), `account_id` (path); required body fields none declared; response statuses 200, 400, 404, 409, 500; error codes in examples none; events none listed.
- **`POST /v1/simulation/configs`** (`simulationConfigs`): security `bearerAuth`; required parameters none declared; required body fields `description`, `plans`; response statuses 200, 400, 401, 500; error codes in examples none; events none listed.
- **`PUT /v1/simulation/configs/{simulation_config_id}/attachment/tenant`** (`attachOrgSimulationConfig`): security `bearerAuth`; required parameters `simulation_config_id` (path); required body fields none declared; response statuses 200, 400, 404, 500; error codes in examples none; events none listed.
- **`GET /v1/simulation/configs/{simulation_config_id}`** (`getSimulationConfigs`): security `bearerAuth`; required parameters `simulation_config_id` (path); required body fields none declared; response statuses 200, 400, 401, 404, 500; error codes in examples none; events none listed.
- **`POST /networktransactions/v1/authorizations`** (`post_v1-authorizations`): security `BearerAuth`; required parameters none declared; required body fields none declared; response statuses 200, 400, 404, 500; error codes in examples none; events `networktransactions-network-authorization-1`.
- **`POST /payment-methods/v1/authorization`** (`post-authorization`): security `BearerAuth`; required parameters none declared; required body fields `currency_code`, `mti`, `network`; response statuses 200, 201, 400, 401, 403, 422, 500; error codes in examples `WONA0001`, `WONA0004`, `WONA0005`, `WONA0006`, `WONA0011`, `WONA0012`, `WONA0013`, `WONA0015`, `WONA0016`, `WONA0018`, `WONA0019`, `WONA0020`, `WONA0032`, `WONA0033`, `WONA0036`, `WONA039`, `WONA040`, `WONA041`, `WONA042`, `WONA043`, `EINS0004`, `EINS0005`, `EINS0006`, `EINS0010`, `EINS0011`, `EINS0012`, `EINS0015`, `EINS0016`, `EPAE0004`, `EPAE0001`, `EPAE0002`; events `payment-methods-authorization-1`, `platform-authorization-platform-authorization-1`.

## Events

Events emitted by the referenced operations (`api-reference-data/endpoint_event_map.csv`):

| Operation | Event slug |
| --- | --- |
| `post_v1-authorizations` | `networktransactions-network-authorization-1` |
| `post-authorization` | `payment-methods-authorization-1` |
| `post-authorization` | `platform-authorization-platform-authorization-1` |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/core-platform/create-fee-model.md`: updatedAt 2026-04-24T02:14:19.000Z.
- `docs/core-platform/simulating-fee-models.md`: updatedAt 2026-04-24T02:07:09.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- None identified by the migration checks.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/core-platform/create-fee-model.md` | whole document | https://developers.pismo.io/pismo-docs/docs/create-fee-model | `de30187b28f90812…` | 2026-04-24T02:14:19.000Z |
| `docs/core-platform/simulating-fee-models.md` | whole document | https://developers.pismo.io/pismo-docs/docs/simulating-fee-models | `0e4ce651e7c03eb7…` | 2026-04-24T02:07:09.000Z |

## Related knowledge units

- `KU-API-card-issuing-authorization--authorizations` — API reference: Card issuing - Authorization — Authorizations
- `KU-API-core-platform-accumulator--configuration` — API reference: Core platform - Accumulator — Configuration
- `KU-API-core-platform-payment-methods--payment-methods-part-01` — API reference: Core platform - Payment methods — Payment methods (part 1 of 3)
- `KU-API-platform-setup-rates-and-fees--fee-models` — API reference: Platform setup - Rates and fees — Fee models
- `KU-API-platform-setup-rates-and-fees--simulation` — API reference: Platform setup - Rates and fees — Simulation
- `KU-CARD-simulate-authorizations` — Simulate authorizations
- `KU-CORE-iof-fee-model` — IOF fee model for Brazil
- `KU-CORE-processing-codes-and-transaction-types` — Processing codes
- `KU-EVT-catalogue-other-domains` — Event catalogue: other event domains (accounting, authorization, availables, average, bulletin, cash, delinquent, fraud, instantpay, intl, ledger, networktransactions, onboarding, orgs, payment, platform, programs, rules, savings, statement)
