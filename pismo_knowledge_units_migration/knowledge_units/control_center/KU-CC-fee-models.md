---
ku_id: KU-CC-fee-models
title: 'Control Center fee models: manage and link fee models'
category: control_center
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/control-center/fee-models-in-control-center.md
  sha256: bcf10f6df071f1e7423a918d9fdf14ea00eef203520b714490044765dc62917f
  url: https://developers.pismo.io/pismo-docs/docs/fee-models-in-control-center
  role: primary_guide
  updated_at: '2026-03-18T15:09:32.000Z'
- path: docs/control-center/add-a-fee-to-a-fee-model.md
  sha256: 99d0a003697f277ee23b8a01fbc395137caf36da4216e6c06520b8ed69c0be87
  url: https://developers.pismo.io/pismo-docs/docs/add-a-fee-to-a-fee-model
  role: primary_guide
  updated_at: '2026-08-31T16:23:57.000Z'
- path: docs/control-center/attach-a-fee-model.md
  sha256: 6ac04e2f0089fd391148a5037767eeb8a58cb0adb4f8754a3f52f6252a010878
  url: https://developers.pismo.io/pismo-docs/docs/attach-a-fee-model
  role: primary_guide
  updated_at: '2026-03-18T15:09:35.000Z'
operations:
- attachmentByAccount
- attachmentByProgram
- attachmentByTenant
- postModel
related_kus:
- KU-API-platform-setup-rates-and-fees--fee-models
- KU-CORE-fee-models
grouping_rationale: Fee-model screens.
---

# Control Center fee models: manage and link fee models

**KU ID:** `KU-CC-fee-models` · **Category:** Control Center · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 3 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: Fee-model screens.

Scope as stated in `docs/control-center/fee-models-in-control-center.md`:

> You can use Pismo Control Center to configure fee models and link them to your operations on the Pismo platform. A fee model is a structure that defines a collection of fees with custom calculations. With a fee model, you can define the method used to calculate the fee, such as a fixed value or a percentage. You can think of it as a container for the fees and taxes that are applied to different account activities.

Scope as stated in `docs/control-center/add-a-fee-to-a-fee-model.md`:

> Once you've created a fee model, you can:

Scope as stated in `docs/control-center/attach-a-fee-model.md`:

> A new fee model is detached by default and not linked to anything. When you create a new fee model, you also must link it to an organization, program, or an account. Otherwise, it will not be applied. Only one fee model can be applied to an organization, program, or account at a time.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/control-center/fee-models-in-control-center.md`: Fee models in Control Center; View the list of fee models; Add a fee model
- `docs/control-center/add-a-fee-to-a-fee-model.md`: Manage fees in a fee model; Add a fee to a fee model; Edit an existing fee; Delete a fee
- `docs/control-center/attach-a-fee-model.md`: Link a fee model; Link a fee model to an organization; Link a fee model to a program; Link a fee model with platform operations

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 4 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/control-center/fee-models-in-control-center.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/fee-models-in-control-center · updatedAt: 2026-03-18T15:09:32.000Z

<!-- source:begin path=docs/control-center/fee-models-in-control-center.md part=0-end -->

# Fee models in Control Center

You can use Pismo Control Center to configure fee models and link them to your operations on the Pismo platform. A fee model is a structure that defines a collection of fees with custom calculations. With a fee model, you can define the method used to calculate the fee, such as a fixed value or a percentage. You can think of it as a container for the fees and taxes that are applied to different account activities.

For detailed information about fee models and fees on the Pismo platform, refer to [Fee management](https://developers.pismo.io/pismo-docs/docs/fee-management).

# View the list of fee models

To view the list of fee models:

1. From the main menu, select **Configurations** > **Fee models**.
2. On the **Fee Models** screen, select a fee model to review its details.

> 📘
>
> The default fee model attached to the organization is displayed at the top. Below this is a list of all fee models that are added to the organization.

3. On the **Fee model details** screen, select one of the following tabs to access more information:
   * **Fee model**—View the name and ID of the fee model. This screen also shows the platform objects (such as programs and accounts) where the fee model is attached.
   * **Fees**—View and manage the fees that belong to the fee model.
   * **Association type**—View the platform objects to which the fee model is currently attached.

# Add a fee model

To create a new fee model:

1. From the main menu, select **Configurations** > **Fee models**.
2. On the **Fee models** screen, select **Create**.
3. On the **Add fee model** screen, enter a name for the new fee model in the **Name** field and select **Finish**.

Note that a new fee model is detached by default. When you create a fee model, you also must attach it to an account, a program, or an organization. Refer to [Attach a fee](https://developers.pismo.io/pismo-docs/docs/attach-a-fee-model) model for details.
<!-- source:end -->

### Source 2: `docs/control-center/add-a-fee-to-a-fee-model.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/add-a-fee-to-a-fee-model · updatedAt: 2026-08-31T16:23:57.000Z

<!-- source:begin path=docs/control-center/add-a-fee-to-a-fee-model.md part=0-end -->

# Manage fees in a fee model

Once you've created a fee model, you can:

* [Add a fee to a fee model](https://developers.pismo.io/pismo-docs/docs/add-a-fee-to-a-fee-model#add-a-fee-to-a-fee-model)
* [Edit the fees in a fee model](https://developers.pismo.io/pismo-docs/docs/add-a-fee-to-a-fee-model#edit-an-existing-fee)
* [Delete a fee from a fee model](https://developers.pismo.io/pismo-docs/docs/add-a-fee-to-a-fee-model#delete-a-fee)

Note that while you can delete fees from the fee model, you cannot delete the fee model itself.

# Add a fee to a fee model

To add a fee to a fee model:

1. From the main menu, select **Configurations** > **Fee models**.
2. Do one of the following:
   * To add a fee to the **default** fee model attached to the organization, select **Details**. Skip to step 4.
   * To add a fee to a different fee model, select the fee model in the results list.
3. On the **Fee model details** screen, open the **Fees** tab.
4. On the **Fees** tab, select **Add fee**.
5. On the **Fee description** screen, type a name for the fee in the **Name** field.
6. Select one of the following to specify whether the fee generates a transaction:
   * **Yes, it generates a transaction**
   * **No, it does not generate a transaction**
7. If the fee does generate a transaction, do the following:
   1. In the **ID** and **Type** fields, select the transaction ID to be used.
   2. In the **Calculation basis** field, select one of the following:
      * **Principal amount**—Taxes are applied to the original transaction amount only. This is the default.
      * **Contract amount**—Taxes are applied to the original transaction amount plus fees.
8. Select one of the following to specify the calculation method:
   * **Fixed**
   * **Greater**
   * **Percentage**
   * **Daily percentage**
   * **Compound interest**
   * **Accumulator**
   * **Price table**
   * **Aging**
   * **IOF**\
     For more information about calculation methods, refer to [Fee models](https://developers.pismo.io/pismo-docs/docs/fee-models).
9. Select **Next**.
10. On the Processing code screen, choose the **Select** button for each processing code to which you want to link. For more information, see [Processing codes](https://developers.pismo.io/pismo-docs/docs/fee-models#triggers-processing-codes).
11. Select **Next**.
12. On the **Review** screen, select **Finish**.

# Edit an existing fee

To edit an existing fee in a fee model:

1. From the main menu, select **Configurations** > **Fee models**.
2. On the **Fee Model Details** screen, open the **Fees**tab.
3. Select the fee you want to edit.\
   The **Fee details** screen opens.
4. On the **Fee details** screen, edit the fields as needed and **Save** your changes.

# Delete a fee

<Callout icon="📘" theme="info">
  You can delete the fees in a fee model, but you cannot delete the model itself.
</Callout>

To delete a fee from a fee model:

1. From the main menu, select **Configurations** > **Fee models**.
2. On the **Fee Model Details** screen, open the **Fees**tab.
3. On the **Fee details** screen, select the applicable **Delete fee** button, then select **Yes** in the confirmation dialog.
<!-- source:end -->

### Source 3: `docs/control-center/attach-a-fee-model.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/attach-a-fee-model · updatedAt: 2026-03-18T15:09:35.000Z

<!-- source:begin path=docs/control-center/attach-a-fee-model.md part=0-end -->

# Link a fee model

A new fee model is detached by default and not linked to anything. When you create a new fee model, you also must link it to an organization, program, or an account. Otherwise, it will not be applied. Only one fee model can be applied to an organization, program, or account at a time.

You can link a fee model at the following levels of detail:

* [Organization level](https://developers.pismo.io/pismo-docs/docs/attach-a-fee-model#link-a-fee-model-to-an-organization)—Link to all accounts in your organization, regardless of which program contains the account. For details on the corresponding API endpoint, refer to [Attach fee model to org](https://developers.pismo.io/pismo-docs/reference/attachmentbytenant).
* [Program level](https://developers.pismo.io/pismo-docs/docs/attach-a-fee-model#link-a-fee-model-to-a-program)—Link to all accounts within a specific program. For details on the corresponding API endpoint, refer to [Attach fee model to program](https://developers.pismo.io/pismo-docs/reference/attachmentbyprogram).
* Account level—Link to selected accounts, regardless of which program they are in. This type of link cannot be done through the Control Center. For details on the corresponding API endpoint, refer to [Attach fee model to account](https://developers.pismo.io/pismo-docs/reference/attachmentbyaccount).

In addition, you can optionally link a fee model with one or more [platform operations](https://developers.pismo.io/pismo-docs/docs/attach-a-fee-model#link-a-fee-model-with-platform-operations), such as a credit transaction using one or more processing codes.

You can find sample payloads for each fee model type in the [Create fee model](https://developers.pismo.io/pismo-docs/reference/postmodel) endpoint.

> 📘
>
> You can't use Control Center to attach fee models to accounts. To do this, you must use the endpoint [Attach fee model to account](https://developers.pismo.io/pismo-docs/reference/attachmentbyaccount).
>
> Note that these levels are hierarchical — for any operation performed on an account, the platform applies the most specific fee model, starting with the account level.

# Link a fee model to an organization

Every organization on the platform is linked to a default fee model. This model is used whenever a platform operation requires a fee model but none is linked at the account or program level.

To attach a different fee model to an organization:

1. From the main menu, select **Configurations** > **Fee models**.
2. Select the fee model you want to link.
3. On the **Fee Model Details** screen, open the **Association type** tab and select **Associate to organization**.
4. In the confirmation dialog, select **Yes** then select **Next** to review.
5. On the **Review** screen, verify your changes and select **Finish**.

# Link a fee model to a program

You can link fee model to multiple programs at a time but only one fee model to each program.

To attach a fee model to one or more programs:

1. From the main menu, select **Configurations** > **Fee models**.
2. Select the fee model you want to attach.
3. On the **Fee Model Details** screen, open the **Association type** tab and select **Associate programs**.
4. On the **Associate a program** screen, for each program that you want to link, select its **Add** button then select **Next** to review.
5. On the **Review** screen, verify your changes and select **Finish**.

# Link a fee model with platform operations

Optionally, you can link a fee model with one or more platform operations, such as a credit transaction. To do this, link one or more processing codes to the fee model.  In cases where no charges are applied, simply do not include a processing code.

To link a fee model with platform operations:

1. From the main menu, select **Configurations** > **Fee models**.
2. On the **Fee model details** screen, select the fee model you want to link and then select **Edit**.
3. On the **Processing code** screen, select each processing code you want to link and select **Next** to review.
4. On the **Review** screen, verify your changes and select **Finish**.
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `PUT /v1/fee/models/{model_id}/attachment/tenant` | `attachmentByTenant` | Attach fee model to org | `api-specs/Platform_setup_-_Rates_and_fees.yaml` | no | KU-API-platform-setup-rates-and-fees--fee-models |
| `PUT /v1/fee/models/{model_id}/attachment/program/{program_id}` | `attachmentByProgram` | Attach fee model to program | `api-specs/Platform_setup_-_Rates_and_fees.yaml` | no | KU-API-platform-setup-rates-and-fees--fee-models |
| `PUT /v1/fee/models/{model_id}/attachment/account/{account_id}` | `attachmentByAccount` | Attach fee model to account | `api-specs/Platform_setup_-_Rates_and_fees.yaml` | no | KU-API-platform-setup-rates-and-fees--fee-models |
| `POST /v1/fee/models` | `postModel` | Create fee model | `api-specs/Platform_setup_-_Rates_and_fees.yaml` | no | KU-API-platform-setup-rates-and-fees--fee-models |

### Operation essentials

- **`PUT /v1/fee/models/{model_id}/attachment/tenant`** (`attachmentByTenant`): security `bearerAuth`; required parameters `model_id` (path); required body fields none declared; response statuses 200, 400, 404, 409, 500; error codes in examples none; events none listed.
- **`PUT /v1/fee/models/{model_id}/attachment/program/{program_id}`** (`attachmentByProgram`): security `bearerAuth`; required parameters `model_id` (path), `program_id` (path); required body fields none declared; response statuses 200, 400, 404, 409, 500; error codes in examples none; events none listed.
- **`PUT /v1/fee/models/{model_id}/attachment/account/{account_id}`** (`attachmentByAccount`): security `bearerAuth`; required parameters `model_id` (path), `account_id` (path); required body fields none declared; response statuses 200, 400, 404, 409, 500; error codes in examples none; events none listed.
- **`POST /v1/fee/models`** (`postModel`): security `bearerAuth`; required parameters `Authorization` (header); required body fields `model_description`, `fees`; response statuses 201, 400, 401, 500; error codes in examples none; events none listed.

## Lifecycle status

- `docs/control-center/fee-models-in-control-center.md`: updatedAt 2026-03-18T15:09:32.000Z.
- `docs/control-center/add-a-fee-to-a-fee-model.md`: updatedAt 2026-08-31T16:23:57.000Z.
- `docs/control-center/attach-a-fee-model.md`: updatedAt 2026-03-18T15:09:35.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- None identified by the migration checks.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/control-center/fee-models-in-control-center.md` | whole document | https://developers.pismo.io/pismo-docs/docs/fee-models-in-control-center | `bcf10f6df071f1e7…` | 2026-03-18T15:09:32.000Z |
| `docs/control-center/add-a-fee-to-a-fee-model.md` | whole document | https://developers.pismo.io/pismo-docs/docs/add-a-fee-to-a-fee-model | `99d0a003697f277e…` | 2026-08-31T16:23:57.000Z |
| `docs/control-center/attach-a-fee-model.md` | whole document | https://developers.pismo.io/pismo-docs/docs/attach-a-fee-model | `6ac04e2f0089fd39…` | 2026-03-18T15:09:35.000Z |

## Related knowledge units

- `KU-API-platform-setup-rates-and-fees--fee-models` — API reference: Platform setup - Rates and fees — Fee models
- `KU-CORE-fee-models` — Fee management and fee models
