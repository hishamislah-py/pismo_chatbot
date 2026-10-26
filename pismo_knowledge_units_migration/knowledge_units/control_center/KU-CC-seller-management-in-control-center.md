---
ku_id: KU-CC-seller-management-in-control-center
title: Seller management
category: control_center
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/control-center/seller-management-in-control-center.md
  sha256: 5348d9b5ff65bd4b4039ad00cf87af00c09cfc6b05136bd27597176b7f4d1472
  url: https://developers.pismo.io/pismo-docs/docs/seller-management-in-control-center
  role: primary_guide
  updated_at: '2026-03-18T15:10:56.000Z'
operations: []
related_kus:
- KU-SELL-seller-management-overview-and-onboarding
grouping_rationale: single source page
---

# Seller management

**KU ID:** `KU-CC-seller-management-in-control-center` · **Category:** Control Center · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/control-center/seller-management-in-control-center.md`:

> Seller management can be fully managed through Control Center, including all seller-related configurations and maintenance tasks. You can manage marketplaces, merchants, creditors, and more using seller management features within Control Center. For details about purchasing Seller management, contact your Pismo representative

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/control-center/seller-management-in-control-center.md`: Seller management; Access Seller management; Define marketplaces and group merchants; Maintain merchants (sellers); Maintain creditors; Define creditor operations (Fees/Taxes); Define merchant schedules; View and manage transactions

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/control-center/seller-management-in-control-center.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/seller-management-in-control-center · updatedAt: 2026-03-18T15:10:56.000Z

<!-- source:begin path=docs/control-center/seller-management-in-control-center.md part=0-end -->

# Seller management

Seller management can be fully managed through Control Center, including all seller-related configurations and maintenance tasks. You can manage marketplaces, merchants, creditors, and more using seller management features within Control Center. For details about purchasing Seller management, contact your Pismo representative

For more information and examples, refer to [Seller management overview](https://developers.pismo.io/pismo-docs/docs/seller-management-overview).

The following Seller management features are accessible directly in Control Center:

* [Define marketplaces and group merchants](#define-marketplaces-and-group-merchants)
* [Maintain merchants](#maintain-merchants-sellers), define merchant schedules, and link merchants to marketplaces
* [Maintain creditors](#maintain-creditors) profiles and view linked merchants
* [Define creditor operations](#define-creditor-operations-feestaxes) including Merchant Discount Rates (MDR), fees, and taxes
* [Define merchant schedules](#define-merchant-schedules) and view a calendar of settlement dates
* [View and manage transactions ](#view-and-manage-transactions)

## Access Seller management

Control Center provides role-based access so that only users with assigned Seller management roles can access the Seller management menus. To use Seller management in Control Center, your user role must have Seller management admin assigned in Permissions. If you need access to Seller management, contact your Control Center administrator.

## Define marketplaces and group merchants

Marketplaces group merchants who sell products online or at physical points of sale. Each marketplace can define its own tax structure and settlement schedule.

1. To manage marketplaces, from the main menu, select **Seller management > Marketplace**.
2. You can create, edit, and configure marketplace details directly from this menu.

## Maintain merchants (sellers)

Merchants represent individual sellers within a marketplace. Each merchant is linked to a schedule and transaction register.

1. To manage merchants, from the main menu, select **Seller management > Merchants**.
2. Use this menu to create new merchants and link them to existing marketplaces.

## Maintain creditors

Creditors are the business owners associated with merchants. Each creditor includes a Pismo account that receives settlement funds.

From the main menu, select **Seller management > Creditor** to create and manage creditor profiles. You can also view linked merchants and account details.

## Define creditor operations (Fees/Taxes)

Creditor operations define the Merchant Discount Rate (MDR), fees, and payment schedules for each transaction type. Through these creditor operations, the Pismo platform provides MDR, fees, and sets the days to pay the merchants starting from the transaction date.

1. To configure these, from the main menu, select **Seller management > Marketplace** and then select a Marketplace from the table.
2. On that page you have an **Overview**, **Sellers**, and **Conditions**.
3. In the **Conditions** tab, you access **Edit creditors operations** where you can set different rates (MDR) and transaction fees per transaction type.

## Define merchant schedules

Schedules determine when settlements occur—same day, two days later, or on a custom timeline.

1. To manage merchant schedules, from the main menu, select **Seller management > Merchant** and select a Merchant in the list.
2. On that page you access **Details**, **Fees/Taxes**, **Transactions**, and **Schedule** tabs.
3. On the **Schedule** tab you access a calendar along with reports of **Blocked + Pending,** **Scheduled**, **Total to be paid**, **Settled**, and **Paid** so that you can view schedules for all merchants.

## View and manage transactions

Seller management supports all transaction types, including card network (off-us), on-us, closed loop, and instant payments.

1. To view and manage transactions, from the main menu, select **Seller management > Merchant** and select a Merchant (Seller) from the list.
2. On that page you have **Details**, **Fees/Taxes**, **Transactions**, and **Schedule** tabs.
3. Use the **Transactions** section to monitor transaction flows and settlement status.
4. You can filter by origin date, due date, receiving date, by custom date range, and by status.
<!-- source:end -->

## Lifecycle status

- `docs/control-center/seller-management-in-control-center.md`: updatedAt 2026-03-18T15:10:56.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- None identified by the migration checks.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/control-center/seller-management-in-control-center.md` | whole document | https://developers.pismo.io/pismo-docs/docs/seller-management-in-control-center | `5348d9b5ff65bd4b…` | 2026-03-18T15:10:56.000Z |

## Related knowledge units

- `KU-SELL-seller-management-overview-and-onboarding` — Seller management overview and onboarding
