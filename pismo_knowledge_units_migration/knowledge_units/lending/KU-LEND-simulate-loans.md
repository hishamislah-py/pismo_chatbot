---
ku_id: KU-LEND-simulate-loans
title: Simulate loans
category: lending
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/lending/simulate-loans.md
  sha256: 7dbf521f9a0d9a7c34fd8c43d441dd49b8f8878a5d9fba8bd797706af58b130a
  url: https://developers.pismo.io/pismo-docs/docs/simulate-loans
  role: primary_guide
  updated_at: '2026-09-22T17:42:19.000Z'
operations:
- getAccountSimulationAttachment
- getOrgSimulationAttachment
- getProgramSimulationAttachment
- getSimulationConfigs
- post-v1-simulation
related_kus:
- KU-API-core-platform-payment-methods-admin--simulation
- KU-API-platform-setup-rates-and-fees--simulation
- KU-LEND-loan-products
grouping_rationale: single source page
---

# Simulate loans

**KU ID:** `KU-LEND-simulate-loans` · **Category:** Lending · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/lending/simulate-loans.md`:

> Use loan simulation to preview the terms of a loan before booking it. When you create a simulation, the Pismo platform calculates a payment schedule, interest, and other terms based on the loan product configuration and the parameters you provide. This simulation helps you and your customers understand repayment amounts, due dates, and total costs before committing to a loan. Once a simulation has expired, customers cannot proceed to booking with the simulated configuration; you must create a new simulation in this case.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/lending/simulate-loans.md`: Simulate loans; Prerequisites; Simulate a loan; Troubleshooting; Why is the calculation or plan retrieved not what I expected?; What does the `MISSING_SIMULATION_CONFIG` error mean?; Why can't I simulate a down payment as the first installment?; What can I do if the simulation has expired?

## Prerequisites and dependencies

- Prerequisites are described in `docs/lending/simulate-loans.md` section "Prerequisites".
- Depends on 5 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/lending/simulate-loans.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/simulate-loans · updatedAt: 2026-09-22T17:42:19.000Z

<!-- source:begin path=docs/lending/simulate-loans.md part=0-end -->

# Simulate loans

Use loan simulation to preview the terms of a loan before booking it. When you create a simulation, the Pismo platform calculates a payment schedule, interest, and other terms based on the loan product configuration and the parameters you provide. This simulation helps you and your customers understand repayment amounts, due dates, and total costs before committing to a loan. Once a simulation has expired, customers cannot proceed to booking with the simulated configuration; you must create a new simulation in this case.

<Callout icon="📘" theme="info">
  Loan simulations are only valid for one day so they always reflect the most up-to-date rates, fees, and balances. This limit helps ensure the results you see are accurate and not based on outdated information.
</Callout>

# Prerequisites

Before simulating a loan, you must have an existing loan product. For more information, refer to [Create loan products](https://developers.pismo.io/pismo-docs/docs/create-loan-products).

# Simulate a loan

Use the [Create simulation](https://developers.pismo.io/pismo-docs/reference/post-v1-simulation) endpoint to simulate a loan.

<Accordion title="Request payload">
  ```json
  {
    "document_number": 143606741568928,
    "amount": 1500.00,
    "authorization_mode": "CREDIT",
    "plan_ids": [
      "PL-20260803170870"
    ]
  }
  ```
</Accordion>

The Pismo platform returns a response like the following:

<Accordion title="Response payload">
  ```json
  {
    "account_id": 330275493,
    "program_id": 55068,
    "amount": 1500,
    "simulation": [
      {
        "additional_details": {
          "billing_method": "BNPL",
          "day_count_method": "MONTH_ACTUAL_YEAR_365",
          "discarded_options": [],
          "due_dates": {
            "1": "2026-09-03",
            "10": "2027-06-03",
            "11": "2027-07-03",
            "12": "2027-08-03",
            "2": "2026-10-03",
            "3": "2026-11-03",
            "4": "2026-12-03",
            "5": "2027-01-03",
            "6": "2027-02-03",
            "7": "2027-03-03",
            "8": "2027-04-03",
            "9": "2027-05-03"
          },
          "first_payment_date": "2026-09-03",
          "minimum_installment_value": null,
          "real_due_dates": {
            "1": null,
            "10": null,
            "11": null,
            "12": null,
            "2": null,
            "3": null,
            "4": null,
            "5": null,
            "6": null,
            "7": null,
            "8": null,
            "9": null
          }
        },
        "id": "2f9b3e86-8449-42d6-ba4d-4281d29ad276",
        "options": [
          {
            "contract_amount": 1697.12,
            "effective_annual_cost": 327.91,
            "effective_monthly_cost": 12.88,
            "first_installment_amortization_value": 1500,
            "first_installment_value": 1697.12,
            "installment_value": 1697.12,
            "installments": 1,
            "postings": {
              "fee_amount": 0,
              "fixed_iof_amount": 5.74,
              "interest_amount": 187.55,
              "iof_amount": 9.57
            },
            "principal_amount": 1500,
            "rates": {
              "conversion_rate": 1,
              "daily_iof_rate": 0.0082,
              "fixed_iof_rate": 0.38,
              "interest_rate": 12
            }
          },
          {
            "contract_amount": 1795.54,
            "effective_annual_cost": 322.45,
            "effective_monthly_cost": 12.76,
            "first_installment_amortization_value": 702.44,
            "first_installment_value": 897.77,
            "installment_value": 897.77,
            "installments": 2,
            "postings": {
              "fee_amount": 0,
              "fixed_iof_amount": 5.74,
              "interest_amount": 283.98,
              "iof_amount": 11.56
            },
            "principal_amount": 1500,
            "rates": {
              "conversion_rate": 1,
              "daily_iof_rate": 0.0082,
              "fixed_iof_rate": 0.38,
              "interest_rate": 12
            }
          },
          {
            "contract_amount": 1899.93,
            "effective_annual_cost": 319.97,
            "effective_monthly_cost": 12.7,
            "first_installment_amortization_value": 438.37,
            "first_installment_value": 633.31,
            "installment_value": 633.31,
            "installments": 3,
            "postings": {
              "fee_amount": 0,
              "fixed_iof_amount": 5.75,
              "interest_amount": 386.26,
              "iof_amount": 13.67
            },
            "principal_amount": 1500,
            "rates": {
              "conversion_rate": 1,
              "daily_iof_rate": 0.0082,
              "fixed_iof_rate": 0.38,
              "interest_rate": 12
            }
          },
          {
            "contract_amount": 2007.16,
            "effective_annual_cost": 318.7,
            "effective_monthly_cost": 12.67,
            "first_installment_amortization_value": 306.9,
            "first_installment_value": 501.79,
            "installment_value": 501.79,
            "installments": 4,
            "postings": {
              "fee_amount": 0,
              "fixed_iof_amount": 5.76,
              "interest_amount": 491.33,
              "iof_amount": 15.83
            },
            "principal_amount": 1500,
            "rates": {
              "conversion_rate": 1,
              "daily_iof_rate": 0.0082,
              "fixed_iof_rate": 0.38,
              "interest_rate": 12
            }
          },
          {
            "contract_amount": 2119.15,
            "effective_annual_cost": 318.1,
            "effective_monthly_cost": 12.66,
            "first_installment_amortization_value": 228.85,
            "first_installment_value": 423.83,
            "installment_value": 423.83,
            "installments": 5,
            "postings": {
              "fee_amount": 0,
              "fixed_iof_amount": 5.77,
              "interest_amount": 601.06,
              "iof_amount": 18.09
            },
            "principal_amount": 1500,
            "rates": {
              "conversion_rate": 1,
              "daily_iof_rate": 0.0082,
              "fixed_iof_rate": 0.38,
              "interest_rate": 12
            }
          },
          {
            "contract_amount": 2235.48,
            "effective_annual_cost": 317.85,
            "effective_monthly_cost": 12.66,
            "first_installment_amortization_value": 177.43,
            "first_installment_value": 372.58,
            "installment_value": 372.58,
            "installments": 6,
            "postings": {
              "fee_amount": 0,
              "fixed_iof_amount": 5.78,
              "interest_amount": 715.03,
              "iof_amount": 20.45
            },
            "principal_amount": 1500,
            "rates": {
              "conversion_rate": 1,
              "daily_iof_rate": 0.0082,
              "fixed_iof_rate": 0.38,
              "interest_rate": 12
            }
          },
          {
            "contract_amount": 2353.26,
            "effective_annual_cost": 317.81,
            "effective_monthly_cost": 12.65,
            "first_installment_amortization_value": 140.83,
            "first_installment_value": 336.18,
            "installment_value": 336.18,
            "installments": 7,
            "postings": {
              "fee_amount": 0,
              "fixed_iof_amount": 5.79,
              "interest_amount": 830.43,
              "iof_amount": 22.83
            },
            "principal_amount": 1500,
            "rates": {
              "conversion_rate": 1,
              "daily_iof_rate": 0.0082,
              "fixed_iof_rate": 0.38,
              "interest_rate": 12
            }
          },
          {
            "contract_amount": 2475.6,
            "effective_annual_cost": 317.97,
            "effective_monthly_cost": 12.66,
            "first_installment_amortization_value": 113.85,
            "first_installment_value": 309.45,
            "installment_value": 309.45,
            "installments": 8,
            "postings": {
              "fee_amount": 0,
              "fixed_iof_amount": 5.8,
              "interest_amount": 950.29,
              "iof_amount": 25.31
            },
            "principal_amount": 1500,
            "rates": {
              "conversion_rate": 1,
              "daily_iof_rate": 0.0082,
              "fixed_iof_rate": 0.38,
              "interest_rate": 12
            }
          },
          {
            "contract_amount": 2601.45,
            "effective_annual_cost": 318.19,
            "effective_monthly_cost": 12.66,
            "first_installment_amortization_value": 93.17,
            "first_installment_value": 289.05,
            "installment_value": 289.05,
            "installments": 9,
            "postings": {
              "fee_amount": 0,
              "fixed_iof_amount": 5.81,
              "interest_amount": 1073.59,
              "iof_amount": 27.86
            },
            "principal_amount": 1500,
            "rates": {
              "conversion_rate": 1,
              "daily_iof_rate": 0.0082,
              "fixed_iof_rate": 0.38,
              "interest_rate": 12
            }
          },
          {
            "contract_amount": 2731.6,
            "effective_annual_cost": 318.56,
            "effective_monthly_cost": 12.67,
            "first_installment_amortization_value": 76.98,
            "first_installment_value": 273.16,
            "installment_value": 273.16,
            "installments": 10,
            "postings": {
              "fee_amount": 0,
              "fixed_iof_amount": 5.82,
              "interest_amount": 1201.11,
              "iof_amount": 30.49
            },
            "principal_amount": 1500,
            "rates": {
              "conversion_rate": 1,
              "daily_iof_rate": 0.0082,
              "fixed_iof_rate": 0.38,
              "interest_rate": 12
            }
          },
          {
            "contract_amount": 2865.28,
            "effective_annual_cost": 319.01,
            "effective_monthly_cost": 12.68,
            "first_installment_amortization_value": 63.99,
            "first_installment_value": 260.48,
            "installment_value": 260.48,
            "installments": 11,
            "postings": {
              "fee_amount": 0,
              "fixed_iof_amount": 5.83,
              "interest_amount": 1332.08,
              "iof_amount": 33.2
            },
            "principal_amount": 1500,
            "rates": {
              "conversion_rate": 1,
              "daily_iof_rate": 0.0082,
              "fixed_iof_rate": 0.38,
              "interest_rate": 12
            }
          },
          {
            "contract_amount": 3003,
            "effective_annual_cost": 319.54,
            "effective_monthly_cost": 12.69,
            "first_installment_amortization_value": 53.43,
            "first_installment_value": 250.25,
            "installment_value": 250.25,
            "installments": 12,
            "postings": {
              "fee_amount": 0,
              "fixed_iof_amount": 5.84,
              "interest_amount": 1467.01,
              "iof_amount": 35.99
            },
            "principal_amount": 1500,
            "rates": {
              "conversion_rate": 1,
              "daily_iof_rate": 0.0082,
              "fixed_iof_rate": 0.38,
              "interest_rate": 12
            }
          }
        ],
        "plan_id": "PL-20260803170870"
      }
    ]
  }
  ```
</Accordion>

After you simulate the loan, the API response includes the `loan_simulation_id`, which you use to identify the simulation when you book the loan. The response also includes the `repayment_schedule`, which shows the details of the loan schedule, and the `disbursement_schedule`, which shows the details of the loan disbursement.

<Accordion title="Response payload with repayment and disbursement schedules">
  ```json
  {
      "loan_simulation_id": "ae401396-2438-4ff8-8894-27720057522c",
      "product_id": "8753ee7e-d227-4bcf-bd10-af03afca738e",
      "loan_amount": 1000.00,
      "outstanding_balance": {
          "principal": 1000.00,
          "interest": 20.07,
          "total": 1020.07
      },
      "total_payment_amount": 1020.07,
      "start_date": "2026-06-24",
      "days_in_year_method": "ACTUAL_ACTUAL",
      "repayment_calculation_method": "EI_REDUCING_BALANCE",
      "repayment_frequency": {
          "unit": "MONTH"
      },
      "repayment_schedule": [
          {
              "period": 1,
              "payment_amount": 340.02,
              "due_date": "2026-07-24",
              "principal_amount": 330.02,
              "interest_amount": 10.00,
              "fee_amount": 0.00,
              "balance": 669.98,
              "number_of_days": 30,
              "auto": false
          },
          {
              "period": 2,
              "payment_amount": 340.02,
              "due_date": "2026-08-24",
              "principal_amount": 333.32,
              "interest_amount": 6.70,
              "fee_amount": 0.00,
              "balance": 336.66,
              "number_of_days": 31,
              "auto": false
          },
          {
              "period": 3,
              "payment_amount": 340.03,
              "due_date": "2026-09-24",
              "principal_amount": 336.66,
              "interest_amount": 3.37,
              "fee_amount": 0.00,
              "balance": 0.00,
              "number_of_days": 31,
              "auto": false
          }
      ],
      "disbursement_schedule": [
          {
              "date": "2026-06-24",
              "amount": 1000.00,
              "principal": 1000.00,
              "tax": 0.00,
              "fee": 0.00,
              "charge": 0.00
          }
      ],
      "stages": [
          {
              "interest_rate": {
                  "value": 0.12,
                  "unit": "YEAR"
              },
              "period": {
                  "value": 3,
                  "unit": "MONTH"
              }
          }
      ]
  }
  ```
</Accordion>

# Troubleshooting

Use this section to troubleshoot errors or confusion in a loan simulation and understand how to resolve them.

## Why is the calculation or plan retrieved not what I expected?

If the simulation returns an unexpected plan or calculation, it might be due to configuration at a different level (account, program, or organization). For example, if an account has a specific plan attached, it overrides program or organization-level plans.

To resolve:

1. Verify all active plan attachments using the relevant GET endpoints:
   * [Get organization simulation config](https://developers.pismo.io/pismo-docs/reference/getorgsimulationattachment)
   * [Get program simulation config](https://developers.pismo.io/pismo-docs/reference/getprogramsimulationattachment)
   * [Get account simulation config](https://developers.pismo.io/pismo-docs/reference/getaccountsimulationattachment)
2. Check which configuration level is being applied.
3. Retrieve the simulation configuration using the **Get simulation config** endpoint.

Update or remove conflicting attachments as needed.

## What does the `MISSING_SIMULATION_CONFIG` error mean?

This error means no valid simulation configuration was found for the account, program, or organization. The system cannot load any simulation plan.

To fix this:

1. Verify all active attachments using the GET endpoints for [Get organization simulation config](https://developers.pismo.io/pismo-docs/reference/getorgsimulationattachment), [Get program simulation config](https://developers.pismo.io/pismo-docs/reference/getprogramsimulationattachment), and [Get account simulation config](https://developers.pismo.io/pismo-docs/reference/getaccountsimulationattachment).
2. Check which configuration level is being applied.
3. Retrieve the simulation configuration using the [Get simulation config](https://developers.pismo.io/pismo-docs/reference/getsimulationconfigs) endpoint with the `simulation_config_id`.

Update your configuration to ensure at least one valid simulation plan is attached.

## Why can't I simulate a down payment as the first installment?

If you want the first installment to act as a down payment, be aware of the following:

* The first installment calculated by the simulation includes interest. A down payment should not include interest.
* If you use the first installment as a down payment and keep the contract total unchanged, the customer might pay interest on the down payment, resulting in an incorrect contract value.
* In some cases, this action can make the contract value negative.

To avoid this situation, don't use the first installment as a down payment unless your configuration and calculation method support it. Review your simulation parameters and contract structure.

For more information, refer to the [Create simulation](https://developers.pismo.io/pismo-docs/reference/post-v1-simulation) endpoint.

## What can I do if the simulation has expired?

When a loan simulation expires, you can't proceed to booking using that simulated setup. Loan simulations are only valid for one day so they always reflect the most up-to-date rates, fees, and balances, ensuring the results you see are accurate and not based on outdated information.

If the simulation has expired and the customer still wants the loan, create a new simulation and use that new identifier for booking.

<br />
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `POST /v1/simulations` | `post-v1-simulation` | Create simulation | `api-specs/Core_platform_-_Payment_methods_admin.yaml` | no | KU-API-core-platform-payment-methods-admin--simulation |
| `GET /v1/simulation/configs/attachment/tenant` | `getOrgSimulationAttachment` | Get org simulation config | `api-specs/Platform_setup_-_Rates_and_fees.yaml` | no | KU-API-platform-setup-rates-and-fees--simulation |
| `GET /v1/simulation/configs/attachment/program/{program_id}` | `getProgramSimulationAttachment` | Get program simulation config | `api-specs/Platform_setup_-_Rates_and_fees.yaml` | no | KU-API-platform-setup-rates-and-fees--simulation |
| `GET /v1/simulation/configs/attachment/account/{account_id}` | `getAccountSimulationAttachment` | Get account simulation config | `api-specs/Platform_setup_-_Rates_and_fees.yaml` | no | KU-API-platform-setup-rates-and-fees--simulation |
| `GET /v1/simulation/configs/{simulation_config_id}` | `getSimulationConfigs` | Get simulation config | `api-specs/Platform_setup_-_Rates_and_fees.yaml` | no | KU-API-platform-setup-rates-and-fees--simulation |

### Operation essentials

- **`POST /v1/simulations`** (`post-v1-simulation`): security not declared; required parameters none declared; required body fields `amount`, `authorization_mode`; response statuses 200, 400, 422, 500; error codes in examples `DO0002`, `SI001`, `SI003`; events none listed.
- **`GET /v1/simulation/configs/attachment/tenant`** (`getOrgSimulationAttachment`): security `bearerAuth`; required parameters none declared; required body fields none declared; response statuses 200, 400, 404, 500; error codes in examples none; events none listed.
- **`GET /v1/simulation/configs/attachment/program/{program_id}`** (`getProgramSimulationAttachment`): security `bearerAuth`; required parameters `program_id` (path); required body fields none declared; response statuses 200, 400, 404, 500; error codes in examples none; events none listed.
- **`GET /v1/simulation/configs/attachment/account/{account_id}`** (`getAccountSimulationAttachment`): security `bearerAuth`; required parameters `account_id` (path); required body fields none declared; response statuses 200, 400, 404, 500; error codes in examples none; events none listed.
- **`GET /v1/simulation/configs/{simulation_config_id}`** (`getSimulationConfigs`): security `bearerAuth`; required parameters `simulation_config_id` (path); required body fields none declared; response statuses 200, 400, 401, 404, 500; error codes in examples none; events none listed.

## Lifecycle status

- `docs/lending/simulate-loans.md`: updatedAt 2026-09-22T17:42:19.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- None identified by the migration checks.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/lending/simulate-loans.md` | whole document | https://developers.pismo.io/pismo-docs/docs/simulate-loans | `7dbf521f9a0d9a7c…` | 2026-09-22T17:42:19.000Z |

## Related knowledge units

- `KU-API-core-platform-payment-methods-admin--simulation` — API reference: Core platform - Payment methods admin — Simulation
- `KU-API-platform-setup-rates-and-fees--simulation` — API reference: Platform setup - Rates and fees — Simulation
- `KU-LEND-loan-products` — Loan products: overview and creation
