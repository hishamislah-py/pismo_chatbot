---
ku_id: KU-CC-accounts
title: 'Control Center accounts: overview, management, actions and configurations'
category: control_center
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/control-center/accounts-overview-cc.md
  sha256: 0c7a835d1d2a7e9b64655bbbeaa2596aff24158daaa380679dad55df03d504b1
  url: https://developers.pismo.io/pismo-docs/docs/accounts-overview-cc
  role: primary_guide
  updated_at: '2026-08-14T13:11:27.000Z'
- path: docs/control-center/accounts-management-in-control-center.md
  sha256: 82772184590ad8938c797795b1e09495e5cd38f84bc5053c9a523e63ceb8d034
  url: https://developers.pismo.io/pismo-docs/docs/accounts-management-in-control-center
  role: primary_guide
  updated_at: '2026-03-18T16:57:51.000Z'
- path: docs/control-center/account-actions.md
  sha256: 89ac5518baece13ad20960108145651b81418449a45b67fa053a21cdc948ee40
  url: https://developers.pismo.io/pismo-docs/docs/account-actions
  role: primary_guide
  updated_at: '2026-05-06T13:28:37.000Z'
- path: docs/control-center/account-configurations-in-control-center.md
  sha256: 382f213b3d94d0af3ee7ead2c38daf75ff19ebdb269396a1eaf3f4cc4534c409
  url: https://developers.pismo.io/pismo-docs/docs/account-configurations-in-control-center
  role: primary_guide
  updated_at: '2026-09-02T10:26:34.000Z'
- path: docs/control-center/customer-operations.md
  sha256: 6499b1e21a2e272d86565c17d74861403192b45a886a11820bd6e1dfd00e94cd
  url: https://developers.pismo.io/pismo-docs/docs/customer-operations
  role: primary_guide
  updated_at: '2026-04-29T15:10:38.000Z'
operations:
- post-acquisitions-v3-s2s-applications
related_kus:
- KU-API-core-platform-accounts--accounts
- KU-CC-cards
- KU-CC-disputes
- KU-CC-dual-approval
- KU-CORE-accounts-overview
- KU-EVT-catalogue-other-domains
- KU-GS-program-types
- KU-GS-setup-overview
- KU-PAY-force-operation
- KU-PAY-hold-funds
grouping_rationale: Account screens.
---

# Control Center accounts: overview, management, actions and configurations

**KU ID:** `KU-CC-accounts` · **Category:** Control Center · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 5 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: Account screens.

Scope as stated in `docs/control-center/accounts-overview-cc.md`:

> The accounts overview is designed to make all account information readily available, making it simple to manage and monitor accounts. It is the displayed page when you select a customer or an account from the **Account management** page.

Scope as stated in `docs/control-center/accounts-management-in-control-center.md`:

> Pismo Control Center provides account management features that let you review and edit account details, such as balances, credit limits, and customer information.

Scope as stated in `docs/control-center/account-actions.md`:

> When you are on the **Accounts overview** page for a specific account, you can use the **Actions** menu to perform various account management functions.

Scope as stated in `docs/control-center/account-configurations-in-control-center.md`:

> Account information in Control Center is divided into the following categories:

Scope as stated in `docs/control-center/customer-operations.md`:

> Customer operations are settings specific to your customers' accounts.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/control-center/accounts-overview-cc.md`: Accounts overview; Account views; Sessions; Account options
- `docs/control-center/accounts-management-in-control-center.md`: Account management; Find a specific account
- `docs/control-center/account-actions.md`: Account actions; Change account status; Make a single adjustment; Hold funds; Release held funds; Transfer held funds
- `docs/control-center/account-configurations-in-control-center.md`: Account configurations; Customer information; Phone numbers; Add a phone number; Edit a phone number; Addresses; Add an address; Edit an address
- `docs/control-center/customer-operations.md`: Customer operations

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 1 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/control-center/accounts-overview-cc.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/accounts-overview-cc · updatedAt: 2026-08-14T13:11:27.000Z

<!-- source:begin path=docs/control-center/accounts-overview-cc.md part=0-end -->

# Accounts overview

The accounts overview is designed to make all account information readily available, making it simple to manage and monitor accounts. It is the displayed page when you select a customer or an account from the **Account management** page.

Accounts in Control Center are grouped by customer—the person or company that holds the account. Select a customer's name to display a menu of all their accounts.

<Image align="center" src="https://files.readme.io/d92d5cf90eb05298816859842d66b3421588a6d7b58da71fd4778570f8f9224d-AccountList.png" />

You can only view one specific account at a time. Select an account to display its **Overview** page.

The following images and table explain the elements of the account overview page. The **Overview** view displays by default.

<Image align="center" alt="Accounts overview with number icons" border={true} width="650px" src="https://files.readme.io/78647ecaa66613882872632c42930f7cad6a69a78004f98e3794dc67c045c443-Accounts_management_new_feature_with_annotations_.png" className="border" />

<Image align="center" alt="Account configurations and Actions menus" border={true} width="400px" src="https://files.readme.io/89e164bc1060c86caca87f504454a1dcc594f80d47ceb2ce7ebd6ae7a91795ca-Accounts_management_new_feature_example_2.png" className="border" />

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        Icon
      </th>

      <th>
        Element
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        1
      </td>

      <td>
        Customer name
      </td>

      <td>
        Name of the customer. You can select the customer's name to open a menu of all the other accounts that belong to that customer.
      </td>
    </tr>

    <tr>
      <td>
        2
      </td>

      <td>
        Breadcrumb trail
      </td>

      <td>
        Navigation aid that shows where you are within the hierarchy. Select any of the links to move up a level in the hierarchy.
      </td>
    </tr>

    <tr>
      <td>
        3
      </td>

      <td>
        Session timer and menus
      </td>

      <td>
        <ul>
          <li>Timer that measures the duration of the current session.</li>
          <li>**Account configurations** and **Actions** menus for accessing account information and performing account operations.</li>
        </ul>
      </td>
    </tr>

    <tr>
      <td>
        4
      </td>

      <td>
        Program summary
      </td>

      <td>
        Basic information about the account, including the name of the program that contains the account, the account number, the account type (such as Credit or Prepaid), and its status (such as Active or Blocked).
      </td>
    </tr>

    <tr>
      <td>
        5
      </td>

      <td>
        Account views
      </td>

      <td>
        Key information about the account, grouped by category. The views shown differ slightly, based on the account type, your role, and other factors. They include details like the account's current balance or available limit, transaction history, requests and approvals, and any related cards.
      </td>
    </tr>
  </tbody>
</Table>

# Account views

Account views are tabs on the **Overview** page that group information about an account into categories. The available views vary based on the account type and your roles.

> 📘 Dual approval
>
> Dual approval is available for selected changes in the account views. With dual approval, you initiate the change and submit a request for approval. A second person must review and approve it. The change doesn't take effect until it's been approved.
>
> For more information about dual approval, refer to [Dual approval](https://developers.pismo.io/pismo-docs/docs/dual-approval).

The following views are available, with the correct account type and permissions.

* **Overview**—General information. This is the default view.
* **Cards**—Every issued card. Each card has detail tabs for transactions, details, and status change history.
* **Transactions**—Transaction event history, including outgoing, incoming, and pending transactions.
* **Statements** (credit only)—Monthly statement details, including amounts, minimum payment, and related dates.
* **Limits**—Credit limits (credit accounts) or fund balances (debit accounts).
* **Deposit products** (debit only)—Available and attached deposit products.
* **Timeline**—Account event history.
* **History**—Account management session history.
* **Loans**—List of account loans and options to manage them.
* **Requests and approvals**—List of all requests and approvals for the selected account.

# Sessions

Control Center begins an account management session whenever you open an account overview and ends when you close the Web browser or select **Actions** > **End session**.

A session timer is a common feature in CRM applications. Tracking the time spent in an account management session is useful for things like tracking billable hours and gathering data on performance and productivity.

The **Actions** menu contains the following **Sessions** options:

* **History**—Review session history
* **Add notes**—Add session notes
* **End session**—End the session

Control Center maintains a history of all sessions, including their duration. If you leave a session without selecting **End session**, the session is listed in the history as "session abandoned".

When you end a session, you have the option to add information about the outcome (resolved, unresolved, or open) and you can include a reason for any changes. This information helps others to understand what hapened during your session and why.

# Account options

From the account overview, you can also do the following.

* View account information by available category tab
* Manage account configurations such as account details, customers, phone numbers, and addresses (refer to [Account configurations](https://developers.pismo.io/pismo-docs/docs/account-configurations-in-control-center)).
* Perform account management actions such as change the account status, make an adjustment, and manage held funds (refer to [Account actions](https://developers.pismo.io/pismo-docs/docs/account-actions)).
* View and edit card information (refer to [Card information](https://developers.pismo.io/pismo-docs/docs/card-information)).
<!-- source:end -->

### Source 2: `docs/control-center/accounts-management-in-control-center.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/accounts-management-in-control-center · updatedAt: 2026-03-18T16:57:51.000Z

<!-- source:begin path=docs/control-center/accounts-management-in-control-center.md part=0-end -->

# Account management

Pismo Control Center provides account management features that let you review and edit account details, such as balances, credit limits, and customer information.

An account on the Pismo platform represents a financial service provider's account. Each account is contained within a program, and the account’s type (such as credit, debit, or prepaid) is determined by the [type of program](https://developers.pismo.io/pismo-docs/docs/program-types) that contains it. Accounts have balances and credit limits as attributes. They also contain customer information, including their addresses and phone numbers, and any cards issued for the account. For information about accounts on the Pismo platform, refer to [Accounts](https://developers.pismo.io/pismo-docs/docs/accounts-overview).

> 📘
>
> Control Center does not support creating accounts. You must create an account using the Accounts API  [Create account application](https://developers.pismo.io/pismo-docs/reference/post-acquisitions-v3-s2s-applications)  endpoint. For more information on account creation, refer to the [Accounts](https://developers.pismo.io/pismo-docs/docs/accounts-overview) guide.

In Control Center, accounts are organized by customer (a person or company registered on the account). A single account can have multiple customers, as in the case of a joint account, but only one customer can be the account holder, who is responsible for the account. Multiple cards can be issued for an account, one per customer, allowing them to access the same account balance.

# Find a specific account

You can search for accounts by customer document number, Pismo account ID, customer email, or customer name.

To find an account:

1. From the main menu, select **Customer operations** > **Accounts**.
2. On the **Accounts management** screen, select one of the following tabs, depending on how you want to search:
   * **By customer**—Search for all accounts linked to a customer using a document number, Pismo account ID, email, or name.
   * **By specific account**—Search for a specific account using its Pismo account ID.
3. Enter a search value and then select **Search**.
   * If you search by customer, Control Center displays a list of all accounts that are linked to the customer. Select the account you want to open in **Accounts overview.**
<!-- source:end -->

### Source 3: `docs/control-center/account-actions.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/account-actions · updatedAt: 2026-05-06T13:28:37.000Z

<!-- source:begin path=docs/control-center/account-actions.md part=0-end -->

# Account actions

When you are on the **Accounts overview** page for a specific account, you can use the **Actions** menu to perform various account management functions.

<Image align="center" width="300px" src="https://files.readme.io/1ac7cde200f0c48013f936c39a7fedb9dd865415a06e7e9ea048f65f5e629c38-MenuIconsCC.png" />

Use the following options from the **Actions** menu to manage the selected account:

* [Change account status](https://developers.pismo.io/pismo-docs/docs/account-actions#change-account-status)
* [Make single adjustment](https://developers.pismo.io/pismo-docs/docs/account-actions#make-a-single-adjustment)
* [Hold funds](https://developers.pismo.io/pismo-docs/docs/account-actions#hold-funds) (debit accounts only)
* [Release held funds](https://developers.pismo.io/pismo-docs/docs/account-actions#release-held-funds) (debit accounts only)
* [Transfer held funds](https://developers.pismo.io/pismo-docs/docs/account-actions#transfer-held-funds) (debit accounts only)

> 📘
>
> Control Center does not support creating accounts. You must create an account using the Accounts API  [Create account application](https://developers.pismo.io/pismo-docs/reference/post-acquisitions-v3-s2s-applications)  endpoint. For more information on account creation, refer to the [Accounts](https://developers.pismo.io/pismo-docs/docs/accounts-overview) guide.

The **Actions** menu also has options for managing the account session. This includes adding notes and ending the session. For information about session actions, refer to [Accounts overview](https://developers.pismo.io/pismo-docs/docs/accounts-overview-cc).

> 📘 Dual approval
>
> If your company is using the dual approval feature for any of the account actions defined in this guide, changes require approval. With dual approval, you initiate the change and submit a request for approval. A second person must review and approve it. The change doesn't take effect until the request is approved.
>
> For more information about dual approval, refer to [Dual approval](https://developers.pismo.io/pismo-docs/docs/dual-approval).

# Change account status

To edit an account status:

1. On the **Accounts overview** page, select **Actions** > **Change account status**.
2. Choose one of the available account status options.
3. (Optional) Choose one of the available reasons for the change.
4. (Optional) Add any additional comments regarding the change.
5. Select **Done** and then select **Yes** to confirm.

> 📘 Reactivating canceled accounts
>
> You can reactivate a canceled account by changing its status back to **Active**.

For information about account statuses and status change reasons on the Pismo platform outside of Control Center, refer to [Accounts](https://developers.pismo.io/pismo-docs/docs/accounts-overview).

# Make a single adjustment

A single adjustment is when you need to adjust an amount because something occurred outside of ordinary operational scenarios. For example, when transaction data is imported into the Pismo platform, you might need to correct for minor inconsistencies in values due to different rounding methods.

To make a single adjustment:

1. On the **Accounts overview** page, select **Actions** > **Make single adjustment**.
2. Modify the values in any of the following fields, as necessary:
   * **Tracking ID**
   * **Value** (adjustment amount)
   * **Processing code**
   * **Description** (required)
3. Select **Submit** and then select **Yes** to confirm.

For information about adjustments on the Pismo platform outside of Control Center, refer to [Forced operation vs. adjustment](https://developers.pismo.io/pismo-docs/docs/force-operation#forced-operation-vs-adjustment).

# Hold funds

For debit accounts only, you can prevent or limit the movement of funds from out of the account. On the Pismo platform, hold funds (also called block amount) transfers a specified amount of money out of the available account balance and holds it in reserve, so that the account holder no longer has access to it. You can hold part or all of the available account balance.

To hold funds:

1. On the **Accounts overview** page, select **Actions** > **Hold funds**.
2. Modify the values in any of the following fields, as necessary:
   * **Tracking ID**
   * **Amount**
   * **Processing code**
   * **Description** (required)
3. Select **Hold funds** and then select **Yes** to confirm.

For information about hold funds on the Pismo platform outside of Control Center, refer to the [Hold funds](https://developers.pismo.io/pismo-docs/docs/hold-funds) guide.

# Release held funds

Use the **Release held funds** options (also called unblock amount) to release some or all of the held funds balance, making it available to the account holder again. This action is available for debit accounts only.

To release held funds:

1. On the **Accounts overview** page, select **Actions** > **Release held funds**.
2. Modify the values in any of the following fields, as necessary:
   * **Tracking ID**
   * **Amount**
   * **Processing code**
   * **Description** (required)
3. Select **Release held funds** then select **Yes** to confirm.

# Transfer held funds

Use the **Transfer held funds** option to transfer some or all of the balance from held funds out of the Pismo platform to an external third-party account. You can only transfer an amount that has been blocked. This action is available for debit accounts only.

To transfer held funds:

1. On the **Accounts overview** page, select **Actions** > **Transfer held funds**.
2. Modify the values in any of the following fields, as necessary:
   * **Tracking ID**
   * **Amount**
   * **Processing code**
   * **Description** (required)
3. Select **Transfer held funds** then select **Yes** to confirm.
<!-- source:end -->

### Source 4: `docs/control-center/account-configurations-in-control-center.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/account-configurations-in-control-center · updatedAt: 2026-09-02T10:26:34.000Z

<!-- source:begin path=docs/control-center/account-configurations-in-control-center.md part=0-end -->

# Account configurations

Account information in Control Center is divided into the following categories:

* **Account details** (view only)—General account information, including its type, Pismo ID, and creation date.
* **[Customers](https://developers.pismo.io/pismo-docs/docs/account-configurations-in-control-center#customer-information)** —Customer information, including Pismo ID, document number, birth date, and gender.
* **[Phone numbers](https://developers.pismo.io/pismo-docs/docs/account-configurations-in-control-center#phone-numbers)**—Customer's residential, commercial, and mobile phone numbers.
* **[Addresses](https://developers.pismo.io/pismo-docs/docs/account-configurations-in-control-center#addresses)**—Customer address details, including the primary address and any additional addresses.
* **Deposit products** (debit accounts only)—List of deposit products attached to the account.

Use the **Account configurations** menu to view and modify this information.

<Image align="center" width="350px" src="https://files.readme.io/cfea26aad4a3c829f36d1ee6749948d8644cd82b1b3dad93db1033ac62d6db38-MenuIconsCC.png" />

# Customer information

You can edit some personal information for a customer in Control Center, such as their name, birth date, and marital status. However, other details are read only, such as the customer ID and document number.

For more information about customers on the Pismo platform, refer to the [Core objects](https://developers.pismo.io/pismo-docs/docs/setup-overview) guide.

To edit customer information, do the following:

1. On the account screen, select the account configurations icon, and select **Customers**.
2. Select **Edit**.
3. In the **Edit details** dialog, edit the customer information, and select **SAVE**.

# Phone numbers

Review and edit a customer's residential, commercial, and mobile phone numbers.

<Callout icon="📘" theme="info">
  Adding or editing a phone number with a type that already exists replaces the current active number for that type.
</Callout>

## Add a phone number

To add a phone number, do the following:

1. On the account screen, select the account configurations icon, and select **Phone numbers**.
2. Select **Add**.
3. In the **Add new contact details** dialog, configure the phone number details, and select **SAVE**.\
   **Note:** The **Extension** field is optional.

## Edit a phone number

To edit a phone number, do the following:

1. On the account screen, select the account configurations icon, and select **Phone numbers**.
2. Select **Edit** for the phone number you want to edit.
3. In the **Edit details** dialog, edit the phone number details, and select **SAVE**.\
   **Note:** The **Extension** field is optional.

# Addresses

Review and edit address details, including residential, commercial, and other types. If there is more than one address currently active, you can do the following:

* Select one address to be the primary address.
* Mark an address as inactive (this change cannot be undone).

## Add an address

To add an address, do the following:

1. On the account screen, select the account configurations icon, and select **Addresses**.
2. Select **Add**.
3. In the **Add a new address** dialog, configure the address details, and select **ADD**.\
   **Note:** The **Number** field refers to the building number of the address, not a phone number.\
   **Note:** To set the address as the primary address for the customer, select the **Set as the primary address** toggle. This option is applicable only if there is more than one active address.

## Edit an address

> 📘 Dual approval
>
> If your company is using the dual approval feature, this change requires approval. With dual approval, you initiate the change and submit a request for approval. A second person must review and approve it. The change doesn't take effect until it's been approved.
>
> For more information about dual approval, refer to [Dual approval](https://developers.pismo.io/pismo-docs/docs/dual-approval).

To edit an address, do the following:

1. On the account screen, select the account configurations icon, and select **Addresses**.
2. Select **Edit**.
3. Select the more options icon for the address you want to edit and select **Edit**.
4. In the **Edit address details** dialog, edit the address details, and select **SAVE**.\
   **Note:** The **Number** field refers to the building number of the address, not a phone number.\
   **Note:** To set the address as the primary address for the customer, select the **Make this the primary address** toggle. This option is applicable only if there is more than one active address.

If an address is no longer required, you can mark it as inactive.

> 🚧 Marking an address as inactive
>
> When you mark an address as inactive, you won't be able to use it again. If you need to use the address again, you must create a new one.

To mark an address as inactive, do the following:

1. On the account screen, select the account configurations icon, and select **Addresses**.
2. Select **Edit**.
3. Select the more options icon for the address you want to mark as inactive, and select **Mark inactive**.
<!-- source:end -->

### Source 5: `docs/control-center/customer-operations.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/customer-operations · updatedAt: 2026-04-29T15:10:38.000Z

<!-- source:begin path=docs/control-center/customer-operations.md part=0-end -->

# Customer operations

Customer operations are settings specific to your customers' accounts.

Customer operations include:

* [Accounts](https://developers.pismo.io/pismo-docs/docs/accounts-management-in-control-center)—View and manage customer accounts and account details.
* [Disputes](https://developers.pismo.io/pismo-docs/docs/disputes)—Create, view, and manage cardholder transaction disputes.

<br />
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `POST /acquisitions/v3/s2s/applications` | `post-acquisitions-v3-s2s-applications` | Create account application | `api-specs/Core_platform_-_Accounts.yaml` | no | KU-API-core-platform-accounts--accounts |

### Operation essentials

- **`POST /acquisitions/v3/s2s/applications`** (`post-acquisitions-v3-s2s-applications`): security `BearerAuth`; required parameters none declared; required body fields `application`; response statuses 201, 400, 409, 500; error codes in examples none; events `onboarding-prospect-1`, `onboarding-succeeded-1`.

## Events

Events emitted by the referenced operations (`api-reference-data/endpoint_event_map.csv`):

| Operation | Event slug |
| --- | --- |
| `post-acquisitions-v3-s2s-applications` | `onboarding-prospect-1` |
| `post-acquisitions-v3-s2s-applications` | `onboarding-succeeded-1` |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/control-center/accounts-overview-cc.md`: updatedAt 2026-08-14T13:11:27.000Z.
- `docs/control-center/accounts-management-in-control-center.md`: updatedAt 2026-03-18T16:57:51.000Z.
- `docs/control-center/account-actions.md`: updatedAt 2026-05-06T13:28:37.000Z.
- `docs/control-center/account-configurations-in-control-center.md`: updatedAt 2026-09-02T10:26:34.000Z.
- `docs/control-center/customer-operations.md`: updatedAt 2026-04-29T15:10:38.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- Source content contains MDX/HTML components (for example `<Table>`, `<HTMLBlock>`, `<Callout>`, `<details>`). They are preserved exactly as published; tables inside them were not converted to Markdown.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/control-center/accounts-overview-cc.md` | whole document | https://developers.pismo.io/pismo-docs/docs/accounts-overview-cc | `0c7a835d1d2a7e9b…` | 2026-08-14T13:11:27.000Z |
| `docs/control-center/accounts-management-in-control-center.md` | whole document | https://developers.pismo.io/pismo-docs/docs/accounts-management-in-control-center | `82772184590ad893…` | 2026-03-18T16:57:51.000Z |
| `docs/control-center/account-actions.md` | whole document | https://developers.pismo.io/pismo-docs/docs/account-actions | `89ac5518baece13a…` | 2026-05-06T13:28:37.000Z |
| `docs/control-center/account-configurations-in-control-center.md` | whole document | https://developers.pismo.io/pismo-docs/docs/account-configurations-in-control-center | `382f213b3d94d0af…` | 2026-09-02T10:26:34.000Z |
| `docs/control-center/customer-operations.md` | whole document | https://developers.pismo.io/pismo-docs/docs/customer-operations | `6499b1e21a2e272d…` | 2026-04-29T15:10:38.000Z |

## Related knowledge units

- `KU-API-core-platform-accounts--accounts` — API reference: Core platform - Accounts — Accounts
- `KU-CC-cards` — Control Center cards: card information and card network tokenization
- `KU-CC-disputes` — Disputes
- `KU-CC-dual-approval` — Dual approval
- `KU-CORE-accounts-overview` — Accounts
- `KU-EVT-catalogue-other-domains` — Event catalogue: other event domains (accounting, authorization, availables, average, bulletin, cash, delinquent, fraud, instantpay, intl, ledger, networktransactions, onboarding, orgs, payment, platform, programs, rules, savings, statement)
- `KU-GS-program-types` — Program types
- `KU-GS-setup-overview` — Core objects
- `KU-PAY-force-operation` — Force operation
- `KU-PAY-hold-funds` — Hold funds
