---
ku_id: KU-CC-programs
title: 'Control Center programs: create, edit, clone, export and import'
category: control_center
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/control-center/cc-manage-programs.md
  sha256: 785dfb300c6b1ede7b9e8d07aaf7fca67924c71e025d79f90f1f1ae5143082fd
  url: https://developers.pismo.io/pismo-docs/docs/cc-manage-programs
  role: primary_guide
  updated_at: '2026-05-21T21:32:40.000Z'
- path: docs/control-center/cc-manage-program-details-and-parameters.md
  sha256: 7000d183a6c4f03eabd42e6b7f7238c0cb2b19e8a4412fff607c797f0a0cbf7c
  url: https://developers.pismo.io/pismo-docs/docs/cc-manage-program-details-and-parameters
  role: primary_guide
  updated_at: '2026-04-15T23:52:57.000Z'
- path: docs/control-center/add-a-program-from-a-template.md
  sha256: 00c4598dda8c2c9da928b830b2186e0a264b7e74983ab4d7b75313a7ecee044c
  url: https://developers.pismo.io/pismo-docs/docs/add-a-program-from-a-template
  role: primary_guide
  updated_at: '2026-03-18T16:58:50.000Z'
- path: docs/control-center/clone-a-program.md
  sha256: aaced661c59866387b6bc485ec34331b21c09f47a2343f58754b6812329526c0
  url: https://developers.pismo.io/pismo-docs/docs/clone-a-program
  role: primary_guide
  updated_at: '2026-03-18T16:58:50.000Z'
- path: docs/control-center/export-and-import-a-program.md
  sha256: 410b90410ccf3de06b7091780d2069bbded0900cbeb2af85dad82fe69b66b60b
  url: https://developers.pismo.io/pismo-docs/docs/export-and-import-a-program
  role: primary_guide
  updated_at: '2026-03-18T16:58:35.000Z'
- path: docs/control-center/cc-cloned-and-exported-data.md
  sha256: 408b330d2e75592980be0c3b7c0849babdf441a5c11f8263295175c7f546e69d
  url: https://developers.pismo.io/pismo-docs/docs/cc-cloned-and-exported-data
  role: primary_guide
  updated_at: '2026-04-15T19:29:59.000Z'
operations:
- CopyProgram
- CopyProgramAsync
- CreateProgramBasedOnTemplate
- CreateProgramBasedOnTemplateAsync
- UpdateProgramInfo
- createProgramParameter
related_kus:
- KU-API-platform-setup-programs--parameters
- KU-API-platform-setup-programs--programs-part-01
- KU-API-platform-setup-programs--programs-part-02
- KU-CARD-card-network-integration
- KU-CARD-full-balance-versus-zero-balance
- KU-CARD-physical-card-embossing
- KU-CC-configuration-menus
- KU-CC-dual-approval
- KU-CORE-accounting-overview
- KU-CORE-program-parameters-reference-table
- KU-CRED-configuring-accrual-rates
- KU-CRED-full-balance-credit-program
- KU-CRED-negotiating-credit-card-debt
- KU-EVT-catalogue-other-domains
- KU-GS-program-types
- KU-GS-setup-overview
- KU-SUP-service-desk-requests
grouping_rationale: Program administration tasks.
---

# Control Center programs: create, edit, clone, export and import

**KU ID:** `KU-CC-programs` · **Category:** Control Center · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 6 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: Program administration tasks.

Scope as stated in `docs/control-center/cc-manage-programs.md`:

> Once you've set up your organization, you can create and implement programs for it. A program is a core object that defines a set of properties applicable to a group of accounts. Programs are only assigned to one organization at a time. For more information about programs and other core objects, refer to [Core objects](https://developers.pismo.io/pismo-docs/docs/setup-overview).

Scope as stated in `docs/control-center/cc-manage-program-details-and-parameters.md`:

> Use Control Center to edit certain program settings, including program details, BINs and BIN range, due dates, program parameters, transaction categories, and limits. This guide notes when an update requires an API.

Scope as stated in `docs/control-center/add-a-program-from-a-template.md`:

> To create a program from a template:

Scope as stated in `docs/control-center/clone-a-program.md`:

> You can use Control Center to clone an existing program within the same organization, using the same details and settings. This is helpful when you need to add a program that is largely similar to one that already exists.

Scope as stated in `docs/control-center/export-and-import-a-program.md`:

> As an alternative to adding a program from a template, you can use Control Center to make a copy of an existing program and migrate it to a different environment or organization. You can only do this with **debit**, **credit**, and **prepaid** program types. This is helpful, for instance, when you need to move a program from a test environment into a production environment. When you export a program, it downloads a JSON file to your computer. Using a text editor, you can modify the program's configuration—including program parameter values—before you import it to the new environment or organization.

Scope as stated in `docs/control-center/cc-cloned-and-exported-data.md`:

> The following properties are copied when you clone or import  a program:

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/control-center/cc-manage-programs.md`: Programs; Program types; Card network integration; Program parameters
- `docs/control-center/cc-manage-program-details-and-parameters.md`: Edit programs; Program details; BIN and BIN range; Due date; Program parameters; Transaction categories; Limits
- `docs/control-center/add-a-program-from-a-template.md`: Create a program from a template
- `docs/control-center/clone-a-program.md`: Clone a program
- `docs/control-center/export-and-import-a-program.md`: Export and import a program; Export a program; Import the program to the new environment or organization
- `docs/control-center/cc-cloned-and-exported-data.md`: Cloned and imported program properties; Debit programs (program type: debit / prepaid); Program parameters; Org operations; Credit programs (program type: credit); Program parameters; Transaction categories; Program transaction types; Org operations; Network acceptances

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 6 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/control-center/cc-manage-programs.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/cc-manage-programs · updatedAt: 2026-05-21T21:32:40.000Z

<!-- source:begin path=docs/control-center/cc-manage-programs.md part=0-end -->

# Programs

Once you've set up your organization, you can create and implement programs for it. A program is a core object that defines a set of properties applicable to a group of accounts. Programs are only assigned to one organization at a time. For more information about programs and other core objects, refer to [Core objects](https://developers.pismo.io/pismo-docs/docs/setup-overview).

From Control Center you can:

* Create a program. There are three ways to do this:
  * [Create a program from a template](https://developers.pismo.io/pismo-docs/docs/add-a-program-from-a-template)
  * [Export and import a program](https://developers.pismo.io/pismo-docs/docs/export-and-import-a-program)
  * [Clone a program](https://developers.pismo.io/pismo-docs/docs/clone-a-program)
* [Edit programs](https://developers.pismo.io/pismo-docs/docs/cc-manage-program-details-and-parameters)
* [Enable card issuing](https://developers.pismo.io/pismo-docs/docs/cc-enable-card-issuing) (for debit programs where it's not already enabled)

To create or edit programs without Control Center, use the [Programs API](https://developers.pismo.io/pismo-docs/reference/createprogrambasedontemplate) endpoints.

This page introduces the key concepts of programs:

* [Program types](https://developers.pismo.io/pismo-docs/docs/cc-manage-programs#program-types)
* [Card network integration](https://developers.pismo.io/pismo-docs/docs/cc-manage-programs#card-network-integration)
* [Program parameters](https://developers.pismo.io/pismo-docs/docs/cc-manage-programs#program-parameters)

# Program types

You can assign program types to manage specific kinds of accounts. Pismo offers these program types:

* **Credit**—Customers borrow up to a credit limit, repay over time, and borrow again. **Example:** a credit card
* **Debit**—Money is immediately withdrawn upon making a purchase. **Example:** a debit card
* **Prepaid**—Funds are loaded in advance to pay for a specific service and aren't associated with a bank account. **Example:** a gift card
* **Current accounts**—Customers withdraw and deposit cash for current expenses. **Example:** a checking account
* **Internal accounts**—Accounts used within an organization for internal purposes rather than for transactions with external parties. These accounts help manage and track internal financial activities. **Example:** a bookkeeping account
* **Correspondent accounts**—Accounts financial institutions hold with each other to facilitate international transactions and provide services to their customers in different geographic locations.

For more information, refer to [Program types](https://developers.pismo.io/pismo-docs/docs/program-types).

# Card network integration

For each card program type, you can choose the type of card network integration:

* **Zero balance integration**—You are responsible for managing your customers’ balances and credit limits.
* **Full balance integration**—Pismo handles most of these processes for you.

For more information, refer to [Full balance versus Zero balance integration](https://developers.pismo.io/pismo-docs/docs/full-balance-versus-zero-balance).

# Program parameters

Program parameters manage settings and configurations that determine a program’s characteristics and behaviors. There are over 60 parameters to choose from, depending on the program type. Define the required ones with your Pismo support team and consider using optional parameters to meet your business needs.

Examples of program parameters include:

* **Overdue fee calculation method**—Defines how late fees are applied to overdue transactions.
* **Withdrawal limit percentage**—Maximum allowed percentage for withdrawals and payments, set as a percentage of the maximum credit limit granted by the institution.

For more information, refer to [Program parameters](https://developers.pismo.io/pismo-docs/docs/program-parameters-reference-table).

<Callout icon="📘" theme="info">
  You can use Pismo Control Center to perform most management tasks for program parameters. However, the primary way to manage them is by using API endpoints.
</Callout>
<!-- source:end -->

### Source 2: `docs/control-center/cc-manage-program-details-and-parameters.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/cc-manage-program-details-and-parameters · updatedAt: 2026-04-15T23:52:57.000Z

<!-- source:begin path=docs/control-center/cc-manage-program-details-and-parameters.md part=0-end -->

# Edit programs

Use Control Center to edit certain program settings, including program details, BINs and BIN range, due dates, program parameters, transaction categories, and limits. This guide notes when an update requires an API.

# Program details

You can configure some program details, including currency, time zone, and country. To update any other program details, you must use the [Update program](https://developers.pismo.io/pismo-docs/reference/updateprograminfo) endpoint.

To edit program details in Control Center:

1. From the main menu, select **Configurations** > **Programs**.
2. On the **Program details** screen, select **Edit**.
3. Make your changes to program name, currency, time zone, and/or country. You cannot change the program type or network integration here—you must the API for that.
4. Select **Save**.

# BIN and BIN range

A Bank Identification Number (BIN) includes the first four to eight digits of a payment card. It is used to identify the card issuer and link transactions to that issuer. The BIN range specifies the beginning and ending sequence of these numbers.

To edit BIN and BIN range:

1. From the main menu, select **Configurations** > **Programs**.
2. On the **Program details** screen, select **BIN range** and then select **Edit**.
3. Make your changes to the BIN, start range, and end range. Note: you cannot change the card brand.
4. Select **Save**.

# Due date

For credit programs, the due date is the day of the month by which the customer must pay the minimum amount due. This field is required for credit full balance program types.

For more information about program due dates on the Pismo platform, refer to [Credit card refinancing](https://developers.pismo.io/pismo-docs/docs/negotiating-credit-card-debt).

# Program parameters

Program parameters are configurable properties that manage how a program is set up and how it behaves. They control aspects like account creation, transaction limits, accrual calculations, and fee amounts. Depending on the parameter, you can use Control Center to enable and disable it, change its value, or both.

You cannot add program parameters through Control Center—you can only do it through the [Parameters API](https://developers.pismo.io/pismo-docs/reference/createprogramparameter).

For details about what program data gets inherited when you clone or import a program, refer to [Cloned and imported program properties](https://developers.pismo.io/pismo-docs/docs/cc-cloned-and-exported-data). For detailed information about program parameters on the Pismo platform, refer to [Program parameters](https://developers.pismo.io/pismo-docs/docs/program-parameters-reference-table).

> 📘 Dual approval
>
> If your company is using the dual approval feature, this change requires approval. With dual approval, you initiate the change and submit a request for approval. A second person must review and approve it. The change doesn't take effect until it's been approved.
>
> For more information about dual approval, refer to [Dual approval](https://developers.pismo.io/pismo-docs/docs/dual-approval).

To edit program parameters:

1. From the main menu, select **Configurations** > **Programs**.
2. On the **Program details** screen, select **Parameters**.
3. Select the parameter you want to edit.
4. In the **Parameter details** modal, edit the selected parameter value.
5. To enable or disable a program parameter, select either **Enable** or **Disable** and then select **Save**.

# Transaction categories

For credit programs, transaction categories are used to configure various accrual types at the program level. They contain fields for specifying refinancing accrual type rates, such as rates applied when the cardholder does not pay the total amount due or the minimum amount due, respectively.

You can add transaction types to existing transaction categories, but you cannot remove them.

For more information, refer to [Using configurable entities](https://developers.pismo.io/pismo-docs/docs/full-balance-credit-program#using-configurable-entities).

# Limits

For credit programs, define program parameters specifically related to limits. These limits apply only to credit programs.

* **Maximum credit limit**—Define the highest amount allowed for accounts in the program. If you lower this value, it doesn't affect existing accounts. To change those accounts, you must update each one individually.
* **Minimum credit limit**—Define the lowest amount allowed for accounts in the program. If you raise this value, it doesn't affect existing accounts. To change those accounts, you must update each one individually.
* **Withdrawal limit percentage**—Define the percentage of approved credit that an account holder can withdraw. The percentage is based on the total credit limit. If you change this value, it does not affect existing accounts. To change those accounts, you must update each one individually.
* **Global program limit**—Define the total amount of credit available across all accounts in this program. Global program limits aren’t applied retroactively. Only accounts created, transferred, or updated after the limit is enabled are counted. Also, if you enable a global program limit, we set the **Program limit validation parameter** to **true**.

> 📘 Dual approval
>
> If your company is using the dual approval feature, this change requires approval. With dual approval, you initiate the change and submit a request for approval. A second person must review and approve it. The change doesn't take effect until it's been approved.
>
> For more information about dual approval, refer to [Dual approval](https://developers.pismo.io/pismo-docs/docs/dual-approval).

To edit limits:

1. From the main menu, select **Configurations** > **Programs**.
2. On the **Program details** screen, select **Limits**.
3. Edit the limits you want to use. For **Global program limit,** you must select **Enabled** for it to be applied going forward.

<br />
<!-- source:end -->

### Source 3: `docs/control-center/add-a-program-from-a-template.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/add-a-program-from-a-template · updatedAt: 2026-03-18T16:58:50.000Z

<!-- source:begin path=docs/control-center/add-a-program-from-a-template.md part=0-end -->

# Create a program from a template

To create a program from a template:

1. From the main menu, select **Configurations** > **Programs**.

2. On the **Programs** screen, select **Create program**.

3. Select the program type, and then select **Next**. For more information on program types, refer to [Program types](https://developers.pismo.io/pismo-docs/docs/program-types).

4. On the **Program details** screen, enter the details about your program, and then select **Next**.
   1. **For Debit types**: Select whether the program will issue physical cards.
   2. **For Debit, credit, and prepaid types**:
      1. Select the card brand.
      2. Select the card network integration, either Full balance or Zero balance. For more information on integration types, refer to [Integration](https://developers.pismo.io/pismo-docs/docs/full-balance-versus-zero-balance).

5. On the **Review** screen, confirm your selections and select **Finish**.

The system takes the parameters you chose, applies them to the Pismo template for that program type, and creates your new program.

> 📘 Asynchronous processing
>
> Your request is processed in the background. You'll be notified when your program has been created. In the meantime, your new program remains in `Processing` status.

To create a program without Control Center, use the [Create program](https://developers.pismo.io/pismo-docs/reference/createprogrambasedontemplate) and [Create program (async)](https://developers.pismo.io/pismo-docs/reference/createprogrambasedontemplateasync) endpoints.
<!-- source:end -->

### Source 4: `docs/control-center/clone-a-program.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/clone-a-program · updatedAt: 2026-03-18T16:58:50.000Z

<!-- source:begin path=docs/control-center/clone-a-program.md part=0-end -->

# Clone a program

You can use Control Center to clone an existing program within the same organization, using the same details and settings. This is helpful when you need to add a program that is largely similar to one that already exists.

For details about what program data is copied to the new program, refer to [Cloned and exported program properties](https://developers.pismo.io/pismo-docs/docs/cc-cloned-and-exported-data).

To copy a program without Control Center, use the [Copy program](https://developers.pismo.io/pismo-docs/reference/copyprogram) and [Copy program (async)](https://developers.pismo.io/pismo-docs/reference/copyprogramasync) endpoints.

To clone a program:

1. From the main menu, select **Configurations** > **Programs**.

2. On the **Programs** screen, select the program that you want to clone.

3. On the **Program information** screen, select **Clone**.

4. On the **Program details screen**, enter program attributes such as the program name, BIN, BIN range, and  time zone. Some values inherited from the source program cannot be changed here.

5. Select **Next**.

6. On the **Review** screen, confirm your settings and then select **Finish**.

> 📘 Asynchronous processing
>
> Your request is processed in the background. You'll be notified when your program has been created. In the meantime, your new program remains in `Processing` status.
<!-- source:end -->

### Source 5: `docs/control-center/export-and-import-a-program.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/export-and-import-a-program · updatedAt: 2026-03-18T16:58:35.000Z

<!-- source:begin path=docs/control-center/export-and-import-a-program.md part=0-end -->

# Export and import a program

As an alternative to adding a program from a template, you can use Control Center to make a copy of an existing program and migrate it to a different environment or organization. You can only do this with **debit**, **credit**, and **prepaid** program types. This is helpful, for instance, when you need to move a program from a test environment into a production environment. When you export a program, it downloads a JSON file to your computer. Using a text editor, you can modify the program's configuration—including program parameter values—before you import it to the new environment or organization.

For details about what program data is copied to the new program, refer to [Cloned and imported program properties](https://developers.pismo.io/pismo-docs/docs/cc-cloned-and-exported-data).

# Export a program

Program export and import supports only the **debit**, **credit**, and **prepaid** program types (both Full balance and Zero balance).

To export a program:

1. From the main menu, select **Configurations** > **Programs**.
2. On the **Programs** screen, select the program that you want to export.
3. On the **Program information** screen, select **Export**.
4. In the confirmation dialog, select **Export**.
   <p>After a few moments, a **Download** button displays on the **Program information** screen.</p>
5. Select **Download**.
   <p>The button remains available for seven days.</p>

<Callout icon="📘" theme="info">
  When a program is first created, its status is `Processing`.  After you clone or import a program, you must request two configuration tasks through the Pismo Service Desk:

  * The Financial Accounts team must configure the accounting scripts that specify how the Pismo platform generates accounting entries for different types of financial operations. The accounting configuration and entry types are unique to each program and are not copied. For more information about accounting on the Pismo platform, refer to [Accounting overview](https://developers.pismo.io/pismo-docs/docs/accounting-overview).
  * For credit programs, the PCI Cards team must perform some verifications and manual configurations, such as for card embossing. For more information about card embossing on the Pismo platform, refer to [Physical card embossing](https://developers.pismo.io/pismo-docs/docs/physical-card-embossing).

  Each of these requests can take up to 90 hours (SLA) to fulfill. Once they are completed, the program's status becomes `Active` and it becomes available for use.
</Callout>

# Import the program to the new environment or organization

To import the program you just exported into a new environment or organization, you must use the JSON file that was generated during the export process (see above). The import process validates the JSON file and displays an error message if it encounters a problem.

<Callout icon="📘" theme="info">
  If the JSON file that you want to import contains a `transaction_category` field whose value is `null`, the program transaction type is not imported. As a result, the value of the `applicable_charges` field will be empty. If this happens, you should modify the program and then export it again.

  For more information about transaction categories on the Pismo platform, refer to [Configuring and managing rates at the program level](https://developers.pismo.io/pismo-docs/docs/configuring-accrual-rates#configuring-and-managing-rates-at-the-program-level).
</Callout>

To import a program to the new environment or organization:

1. From the main menu, select **Configurations** > **Programs**.
2. On the **Programs** screen, select **Import programs**.
3. In the **Import program** dialog, drag the JSON file into the file upload area and then enter the program name.
4. Select **Import**.

> 📘 Asynchronous processing
>
> Your request is processed in the background. You'll be notified when your program has been created. In the meantime, your new program remains in `Processing` status.
<!-- source:end -->

### Source 6: `docs/control-center/cc-cloned-and-exported-data.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/cc-cloned-and-exported-data · updatedAt: 2026-04-15T19:29:59.000Z

<!-- source:begin path=docs/control-center/cc-cloned-and-exported-data.md part=0-end -->

# Cloned and imported program properties

The following properties are copied when you clone or import  a program:

* [Debit programs](https://developers.pismo.io/pismo-docs/docs/cc-cloned-and-exported-data#debit-programs-program-type-debit--prepaid) properties list
* [Credit programs](https://developers.pismo.io/pismo-docs/docs/cc-cloned-and-exported-data#credit-programs-program-type-credit) properties list

> 🚧
>
> When you clone or export and import a program, you must open a [Jira ticket](https://developers.pismo.io/pismo-docs/docs/opening-a-service-desk-ticket)  for accounting and PCI cards for their configurations.
>
> The embossing and accounting configurations are not copied in this process.

# Debit programs (program type: debit / prepaid)

* Card brand
* Currency code
* Time zone
* Country code
* BIN
  * BIN range start
  * BIN range end
* Reference
* Due dates
  * Day
  * Active status
* Origin
* Program export ID

## Program parameters

* Parameter name
* Parameter value
* Account parameter indicator
* Parameter status

## Org operations

* Processing code
* Org operation ID
* Balance impact
* Description
* Standard
* Status
* Type
* Translations

# Credit programs (program type: credit)

* Card brand
* Currency code
* Time zone
* Country code
* BIN
  * BIN range start
  * BIN range end
* Reference
* Due dates
  * Day
  * Active status
* Origin
* Program export ID

## Program parameters

* Parameter name
* Parameter value
* Account parameter indicator
* Parameter status

## Transaction categories

* Transaction category ID
* Transaction category description
* Refinancing rate before due date
* Refinancing rate after due date
* Default rate
* Fine rate
* Overdue rate after due date
* Minimum value
* Charge order

## Program transaction types

* Transaction type ID
* Transaction category
* Description

## Org operations

* Operation type
  * Operation type ID
  * Description
  * Is credit?
  * Processing code
  * Type
* Processing code
* Operation name
* Balance impact
* Type
* Is external?
* Balance impact ID

## Network acceptances

For information about network authorizations on the Pismo platform, refer to [Card network integration](https://developers.pismo.io/pismo-docs/docs/card-network-integration).
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `POST /programs/v1/programs/template` | `CreateProgramBasedOnTemplate` | Create program | `api-specs/Platform_setup_-_Programs.yaml` | no | KU-API-platform-setup-programs--programs-part-01 |
| `PATCH /programs/v1/programs/{id}` | `UpdateProgramInfo` | Update program | `api-specs/Platform_setup_-_Programs.yaml` | no | KU-API-platform-setup-programs--programs-part-02 |
| `POST /programs/v1/programs/{program_id}/parameters` | `createProgramParameter` | Link optional parameter to program | `api-specs/Platform_setup_-_Programs.yaml` | no | KU-API-platform-setup-programs--parameters |
| `POST /programs/v2/programs/template` | `CreateProgramBasedOnTemplateAsync` | Create program (async) | `api-specs/Platform_setup_-_Programs.yaml` | no | KU-API-platform-setup-programs--programs-part-01 |
| `POST /programs/v1/programs/copy` | `CopyProgram` | Copy program | `api-specs/Platform_setup_-_Programs.yaml` | no | KU-API-platform-setup-programs--programs-part-01 |
| `POST /programs/v2/programs/copy` | `CopyProgramAsync` | Copy program (async) | `api-specs/Platform_setup_-_Programs.yaml` | no | KU-API-platform-setup-programs--programs-part-01 |

### Operation essentials

- **`POST /programs/v1/programs/template`** (`CreateProgramBasedOnTemplate`): security `S2SAuthentication`; required parameters none declared; required body fields `name`, `type`, `timezone`, `currency_numeric_code`, `country_code`; response statuses 200, 400, 404, 416, 500; error codes in examples `EOA0017`, `EOA0018`, `EOA0086`, `EOA0029`, `EOA0033`, `EOA0063`, `EOA0055`, `EOA0073`, `EOA0054`, `EOA0040`, `EOA0037`, `EOA0038`, `EOA0039`, `EOA0020`, `EOA0031`, `EOA0064`, `EOA0030`, `EOA0021`, `EOA0022`, `EOA0034`, `EOA0035`, `EOA0036`, `EOA0058`, `EOA0009`, `EOA0010`, `EOA0008`, `EOA0011`, `EOA0015`, `EOA0016`; events `programs-creation-1`.
- **`PATCH /programs/v1/programs/{id}`** (`UpdateProgramInfo`): security `S2SAuthentication`; required parameters `id` (path); required body fields none declared; response statuses 204, 400, 404, 500; error codes in examples `EOA0017`, `EOA0080`, `EOA0018`, `EOA0029`, `EOA0033`, `EOA0063`, `EOA0055`, `EOA0073`, `EOA0054`, `EOA0040`, `EOA0037`, `EOA0038`, `EOA0039`, `EOA0082`, `EOA0059`, `EOA0020`, `EOA0064`, `EOA0034`, `EOA0009`, `EOA0010`, `EOA0008`, `EOA0011`, `EOA0015`, `EOA0016`; events `programs-update-1`.
- **`POST /programs/v1/programs/{program_id}/parameters`** (`createProgramParameter`): security `S2SAuthentication`; required parameters `program_id` (path); required body fields `parameter_name`; response statuses 201, 400; error codes in examples none; events none listed.
- **`POST /programs/v2/programs/template`** (`CreateProgramBasedOnTemplateAsync`): security `S2SAuthentication`; required parameters none declared; required body fields `name`, `type`, `timezone`, `currency_numeric_code`, `country_code`; response statuses 201, 400, 404, 500; error codes in examples `EOA0017`, `EOA0018`, `EOA0086`, `EOA0029`, `EOA0033`, `EOA0063`, `EOA0055`, `EOA0073`, `EOA0054`, `EOA0040`, `EOA0037`, `EOA0038`, `EOA0039`, `EOA0031`, `EOA0030`, `EOA0009`, `EOA0008`, `EOA0015`, `EOA0016`; events `programs-creation-1`.
- **`POST /programs/v1/programs/copy`** (`CopyProgram`): security `S2SAuthentication`; required parameters none declared; required body fields `base_program_id`, `name`, `timezone`, `currency_numeric_code`, `country_code`; response statuses 200, 400, 404, 500; error codes in examples `EOA0017`, `EOA0018`, `EOA0086`, `EOA0029`, `EOA0033`, `EOA0063`, `EOA0055`, `EOA0073`, `EOA0054`, `EOA0040`, `EOA0037`, `EOA0038`, `EOA0039`, `EOA0020`, `EOA0064`, `EOA0021`, `EOA0022`, `EOA0034`, `EOA0035`, `EOA0036`, `EOA0058`, `EOA0009`, `EOA0010`, `EOA0008`, `EOA0011`, `EOA0015`, `EOA0016`; events `programs-creation-1`.
- **`POST /programs/v2/programs/copy`** (`CopyProgramAsync`): security `S2SAuthentication`; required parameters none declared; required body fields `base_program_id`, `name`, `timezone`, `currency_numeric_code`, `country_code`; response statuses 201, 400, 404, 500; error codes in examples `EOA0017`, `EOA0018`, `EOA0086`, `EOA0029`, `EOA0033`, `EOA0063`, `EOA0055`, `EOA0073`, `EOA0054`, `EOA0040`, `EOA0037`, `EOA0038`, `EOA0039`, `EOA0082`, `EOA0085`, `EOA0020`, `EOA0064`, `EOA0009`, `EOA0008`, `EOA0015`, `EOA0016`; events `programs-creation-1`.

## Events

Events emitted by the referenced operations (`api-reference-data/endpoint_event_map.csv`):

| Operation | Event slug |
| --- | --- |
| `CopyProgram` | `programs-creation-1` |
| `CopyProgramAsync` | `programs-creation-1` |
| `CreateProgramBasedOnTemplate` | `programs-creation-1` |
| `CreateProgramBasedOnTemplateAsync` | `programs-creation-1` |
| `UpdateProgramInfo` | `programs-update-1` |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/control-center/cc-manage-programs.md`: updatedAt 2026-05-21T21:32:40.000Z.
- `docs/control-center/cc-manage-program-details-and-parameters.md`: updatedAt 2026-04-15T23:52:57.000Z.
- `docs/control-center/add-a-program-from-a-template.md`: updatedAt 2026-03-18T16:58:50.000Z.
- `docs/control-center/clone-a-program.md`: updatedAt 2026-03-18T16:58:50.000Z.
- `docs/control-center/export-and-import-a-program.md`: updatedAt 2026-03-18T16:58:35.000Z.
- `docs/control-center/cc-cloned-and-exported-data.md`: updatedAt 2026-04-15T19:29:59.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- None identified by the migration checks.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/control-center/cc-manage-programs.md` | whole document | https://developers.pismo.io/pismo-docs/docs/cc-manage-programs | `785dfb300c6b1ede…` | 2026-05-21T21:32:40.000Z |
| `docs/control-center/cc-manage-program-details-and-parameters.md` | whole document | https://developers.pismo.io/pismo-docs/docs/cc-manage-program-details-and-parameters | `7000d183a6c4f03e…` | 2026-04-15T23:52:57.000Z |
| `docs/control-center/add-a-program-from-a-template.md` | whole document | https://developers.pismo.io/pismo-docs/docs/add-a-program-from-a-template | `00c4598dda8c2c9d…` | 2026-03-18T16:58:50.000Z |
| `docs/control-center/clone-a-program.md` | whole document | https://developers.pismo.io/pismo-docs/docs/clone-a-program | `aaced661c5986638…` | 2026-03-18T16:58:50.000Z |
| `docs/control-center/export-and-import-a-program.md` | whole document | https://developers.pismo.io/pismo-docs/docs/export-and-import-a-program | `410b90410ccf3de0…` | 2026-03-18T16:58:35.000Z |
| `docs/control-center/cc-cloned-and-exported-data.md` | whole document | https://developers.pismo.io/pismo-docs/docs/cc-cloned-and-exported-data | `408b330d2e755929…` | 2026-04-15T19:29:59.000Z |

## Related knowledge units

- `KU-API-platform-setup-programs--parameters` — API reference: Platform setup - Programs — Parameters
- `KU-API-platform-setup-programs--programs-part-01` — API reference: Platform setup - Programs — Programs (part 1 of 2)
- `KU-API-platform-setup-programs--programs-part-02` — API reference: Platform setup - Programs — Programs (part 2 of 2)
- `KU-CARD-card-network-integration` — Card network integration and certification
- `KU-CARD-full-balance-versus-zero-balance` — Full balance versus Zero balance integration
- `KU-CARD-physical-card-embossing` — Physical card embossing
- `KU-CC-configuration-menus` — Control Center configuration menus: platform, banking and card configurations
- `KU-CC-dual-approval` — Dual approval
- `KU-CORE-accounting-overview` — Accounting overview and accounting event types
- `KU-CORE-program-parameters-reference-table` — Program parameters
- `KU-CRED-configuring-accrual-rates` — Configuring accrual rates
- `KU-CRED-full-balance-credit-program` — Full balance credit programs: concepts and configuration
- `KU-CRED-negotiating-credit-card-debt` — Credit card refinancing
- `KU-EVT-catalogue-other-domains` — Event catalogue: other event domains (accounting, authorization, availables, average, bulletin, cash, delinquent, fraud, instantpay, intl, ledger, networktransactions, onboarding, orgs, payment, platform, programs, rules, savings, statement)
- `KU-GS-program-types` — Program types
- `KU-GS-setup-overview` — Core objects
- `KU-SUP-service-desk-requests` — Pismo Service Desk: opening, tracking and modifying requests
