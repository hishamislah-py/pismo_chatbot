---
ku_id: KU-CC-flex-controls
title: Control Center flex controls, with a Pix example
category: control_center
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/control-center/cc-flex-controls.md
  sha256: 607e46a6b8712f11792c78ca7ef3f3495c488f1f146b86e8478719b2945c0bd5
  url: https://developers.pismo.io/pismo-docs/docs/cc-flex-controls
  role: primary_guide
  updated_at: '2026-03-18T15:09:38.000Z'
- path: docs/control-center/example-create-a-flex-control-for-pix-transactions.md
  sha256: 5e5613081a65736d94b1ea864232e7c5068eb3ef2e41e6ae310a9ac7e24a89a3
  url: https://developers.pismo.io/pismo-docs/docs/example-create-a-flex-control-for-pix-transactions
  role: primary_guide
  updated_at: '2026-03-18T15:09:38.000Z'
operations:
- get-v1-accounts-flex-controls
- post-v1-accounts-flex-controls
related_kus:
- KU-API-core-platform-flex-controls--account-flex-controls
- KU-CORE-flex-controls
- KU-EVT-catalogue-audit
- KU-PAY-pix-instant-payments
grouping_rationale: Screen and worked example.
---

# Control Center flex controls, with a Pix example

**KU ID:** `KU-CC-flex-controls` · **Category:** Control Center · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 2 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: Screen and worked example.

Scope as stated in `docs/control-center/cc-flex-controls.md`:

> Flexible transaction controls, also known as just flex controls, are rules that restrict your customers' financial operations. They include various conditions and parameters, such as spending mode, maximum spending limit restrictions, or time-based restrictions.

Scope as stated in `docs/control-center/example-create-a-flex-control-for-pix-transactions.md`:

> Here is an example of how to create a nightly transaction limit for Pix transactions at the program level. The limit is R$1,000 nightly, between the hours of 8:00 PM and 6:00 AM. For more information about Pix, refer to [Pix instant payments (Brazil)](https://developers.pismo.io/pismo-docs/docs/pix-instant-payments).

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/control-center/cc-flex-controls.md`: Flex controls; View flex controls; Create a flex control; Activate or deactivate a flex control
- `docs/control-center/example-create-a-flex-control-for-pix-transactions.md`: Example: Create a flex control for Pix transactions

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 2 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/control-center/cc-flex-controls.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/cc-flex-controls · updatedAt: 2026-03-18T15:09:38.000Z

<!-- source:begin path=docs/control-center/cc-flex-controls.md part=0-end -->

# Flex controls

Flexible transaction controls, also known as just flex controls, are rules that restrict your customers' financial operations. They include various conditions and parameters, such as spending mode, maximum spending limit restrictions, or time-based restrictions.

Note that managing flex controls using Control Center has the following limitations:

* You can apply flex controls to debit accounts only.
* You can apply flex controls at the program level only, to apply to all accounts in the program.

> 📘 Using flex controls
>
> The only way to set up flex controls at the program level is to use Control Center. This means that a control affects all the accounts within a specific program.
>
> To create flex controls at the account or card level, you must use the appropriate endpoint in the [Flex controls API](https://developers.pismo.io/pismo-docs/reference/post-v1-accounts-flex-controls).

For information about flex controls, refer to [Flexible transaction controls](https://developers.pismo.io/pismo-docs/docs/flex-controls).

From Control Center, you can do the following:

* [View flex controls](https://developers.pismo.io/pismo-docs/docs/cc-flex-controls#view-flex-controls)
* [Create a flex control](https://developers.pismo.io/pismo-docs/docs/cc-flex-controls#create-a-flex-control) at the program level
* [Activate or deactivate a flex control](https://developers.pismo.io/pismo-docs/docs/cc-flex-controls#activate-or-deactivate-a-flex-control)

# View flex controls

You can use Control Center to view all existing program-level flex controls. To view flex controls at the account level, you must use the [List account flex controls](https://developers.pismo.io/pismo-docs/reference/get-v1-accounts-flex-controls) endpoint.

To view the list of program-level flex controls:

1. From the main menu, select **Configurations** > **Flex controls**.

2. To find a specific control, use the **Search by name** field to search by flex control name or use the **Select program** field to search for a control by program name.

# Create a flex control

In Control Center, you can add flex controls only at the program level. This means that the flex control affects all accounts in the program to which you apply it. You can add a flex control as **active** (immediately activated) or as **inactive** (saved but not activated).

Once a flex control is active, the platform evaluates it whenever there are events generated for customer accounts that match its defined transaction types.

To add a program-level flex control:

1. From the main menu, select **Configurations** > **Flex controls**.

2. On the **Flex controls** screen, select **Create flex control**.

3. On the **Select a control type** screen, select the type of control (**Restriction control** or **Cumulative control**) and select **Next**.

4. On the **Select processing codes** screen, select **Add** for each processing code to be included in this flex control and select **Next**.

5. On the **Conditions** screen, do one of the following:
   1. If you're adding a cumulative control, proceed to step #6.
   2. If you're adding a restriction control, skip to step #7.

6. (Cumulative control type only) On the **Limits and time period** screen, do the following:

   1. Select the type of limit—**Transactions** (restrict by number of transactions) or **Spending** (restrict by amount).
   2. Provide values and other details about the criteria to use to evaluate the condition (for example, amounts, time zone, and day of the month), then select **Next**.

7. (For restriction controls only) On the **Conditions** screen, select the conditions that you want to include in the flex control. Multiple conditions are allowed, but there can be only one attribute for each condition.

8. Select **Add condition** and then select **Next**.

9. On the **Program** screen, choose **Select** to apply the flex control to at least one program. This affects all accounts in the selected program.

10. Select **Next**.

11. On the **Review and apply flex control** screen, do the following:
    1. Review and confirm each of the configuration settings.
    2. Enter a name for the flex control.
    3. Specify the deny code to return when the evaluation matches the control condition.
    4. Set the rule to apply to personal accounts, business accounts, or  both.
    5. Set whether to create the flex control as **active** (activated immediately on save) or **inactive** (saved but not activated).
    6. Select **Finish**.

# Activate or deactivate a flex control

If you created a flex control and initially set it as inactive, you can set it to **Active** through the Control Center.

To activate an inactive flex control:

1. From the main menu, select **Configurations** > **Flex controls**.
2. Select the inactive flex control you want to activate.
3. On the **Flex control details** page, select **Edit**.
4. Set the **Active** toggle switch on and **Save** your changes.

To deactivate a program-level flex control at any time, use the steps above and set the **Active** toggle switch off.
<!-- source:end -->

### Source 2: `docs/control-center/example-create-a-flex-control-for-pix-transactions.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/example-create-a-flex-control-for-pix-transactions · updatedAt: 2026-03-18T15:09:38.000Z

<!-- source:begin path=docs/control-center/example-create-a-flex-control-for-pix-transactions.md part=0-end -->

# Example: Create a flex control for Pix transactions

Here is an example of how to create a nightly transaction limit for Pix transactions at the program level. The limit is R$1,000 nightly, between the hours of 8:00 PM and 6:00 AM. For more information about Pix, refer to [Pix instant payments (Brazil)](https://developers.pismo.io/pismo-docs/docs/pix-instant-payments).

> 📘 Using flex controls
>
> The only way to set up flex controls at the program level is to use Control Center. This means that a control affects all the accounts within a specific program.
>
> To create flex controls at the account or card level, you must use the appropriate endpoint in the [Flex controls API](https://developers.pismo.io/pismo-docs/reference/post-v1-accounts-flex-controls).

To apply this flex control, follow the procedure to [Create a flex control](https://developers.pismo.io/pismo-docs/docs/cc-flex-controls#create-a-flex-control) but use the following information:

* On the **Select a control type** screen, select **Cumulative control**.
* On the **Select processing codes** screen, add the processing codes to be included in this flex control (any processing codes associated with Pix transactions).
* On the **Limits and time period** screen, do the following:
  * Select **Spending** as the limit type.
  * Select **Per day** and specify the time zone the control must use.
  * Set the **Reset period** to **7:00 AM**. This is the time when the limit resets and can be any hour outside of the nightly range.
  * Enter the spending limit amount `1,000`. Control Center displays a message like **Deny transactions for the selected processing codes after $1,000 daily, starting daily at 7:00 AM, XXX/XXXX time zone.** Use this message to confirm that this is the result you want.\
    Note: You don't need to specify the currency to use because this is set individually by each program linked to the flex control.
* On the **Conditions** screen, do the following:
  * Select the box for **Week, Month, Time of day.**
  * Select the box for **Time of Day** and then select the start time **8:00 PM** and end time **6:00 AM**.
  * Select  **Add condition**.
* On the **Program** screen, select the programs to which you want to apply this control.
* On the **Review and apply flex control** screen, do the following:
  * Review and confirm each setting by selecting its check box.
  * Enter a name for your control (such as `Nightly_PIX_Limit`) and the **Deny code** that you want to receive whenever a transaction exceeds the limit (such as `PIX_nightly_limit_reached`).
* Select **Create control and activate now** and then select **Finish**.
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `POST /v1/accounts/{accountId}/flex-controls` | `post-v1-accounts-flex-controls` | Create account flex control | `api-specs/Core_platform_-_Flex_controls.yaml` | no | KU-API-core-platform-flex-controls--account-flex-controls |
| `GET /v1/accounts/{accountId}/flex-controls` | `get-v1-accounts-flex-controls` | List account flex controls | `api-specs/Core_platform_-_Flex_controls.yaml` | no | KU-API-core-platform-flex-controls--account-flex-controls |

### Operation essentials

- **`POST /v1/accounts/{accountId}/flex-controls`** (`post-v1-accounts-flex-controls`): security `BearerAuth`; required parameters `accountId` (path); required body fields `type`, `name`, `deny_code`; response statuses 201, 400, 403, 409, 500; error codes in examples `ERUL0701`, `RULVAL0400`, `ERUL0702`, `ERUL0703`, `ERUL0704`, `ERUL0706`, `ERUL0004`, `ERUL0002`, `RULVAL0403`, `WRUL0707`, `RULVAL0409`, `ERUL0001`, `RULREP0500`; events `audit-account-spending-limit-created-1`.
- **`GET /v1/accounts/{accountId}/flex-controls`** (`get-v1-accounts-flex-controls`): security `BearerAuth`; required parameters `accountId` (path); required body fields none declared; response statuses 200, 400, 404, 500; error codes in examples `ERUL0801`, `RULVAL0400`, `ERUL0802`, `ERUL0803`, `RULVAL0400`, `ERUL0001`, `RULREP0500`; events none listed.

## Events

Events emitted by the referenced operations (`api-reference-data/endpoint_event_map.csv`):

| Operation | Event slug |
| --- | --- |
| `post-v1-accounts-flex-controls` | `audit-account-spending-limit-created-1` |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/control-center/cc-flex-controls.md`: updatedAt 2026-03-18T15:09:38.000Z.
- `docs/control-center/example-create-a-flex-control-for-pix-transactions.md`: updatedAt 2026-03-18T15:09:38.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- None identified by the migration checks.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/control-center/cc-flex-controls.md` | whole document | https://developers.pismo.io/pismo-docs/docs/cc-flex-controls | `607e46a6b8712f11…` | 2026-03-18T15:09:38.000Z |
| `docs/control-center/example-create-a-flex-control-for-pix-transactions.md` | whole document | https://developers.pismo.io/pismo-docs/docs/example-create-a-flex-control-for-pix-transactions | `5e5613081a65736d…` | 2026-03-18T15:09:38.000Z |

## Related knowledge units

- `KU-API-core-platform-flex-controls--account-flex-controls` — API reference: Core platform - Flex controls — Account flex controls
- `KU-CORE-flex-controls` — Flexible transaction controls: concepts, examples and simulation
- `KU-EVT-catalogue-audit` — Event catalogue: audit
- `KU-PAY-pix-instant-payments` — Pix instant payments (Brazil)
