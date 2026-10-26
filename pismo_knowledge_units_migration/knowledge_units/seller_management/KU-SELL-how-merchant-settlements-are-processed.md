---
ku_id: KU-SELL-how-merchant-settlements-are-processed
title: How merchant settlements and installments are processed
category: seller_management
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/seller-management/how-merchant-settlements-are-processed.md
  sha256: d2a797fc0ca3478d590a97d900b2b5f9dd13f2b7fb52ee3d5c4de3336cab0e02
  url: https://developers.pismo.io/pismo-docs/docs/how-merchant-settlements-are-processed
  role: primary_guide
  updated_at: '2026-03-18T15:24:22.000Z'
operations:
- PostCreditorsOperations
- post-authorization
related_kus:
- KU-API-core-platform-payment-methods--payment-methods-part-01
- KU-API-seller-management-marketplace--marketplace-creditor-operations
- KU-EVT-catalogue-marketplace
- KU-EVT-catalogue-other-domains
grouping_rationale: single source page
---

# How merchant settlements and installments are processed

**KU ID:** `KU-SELL-how-merchant-settlements-are-processed` · **Category:** Seller management · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/seller-management/how-merchant-settlements-are-processed.md`:

> Transaction settlement is the process of moving funds from the cardholder’s account to the merchant’s account after the cardholder makes a credit or debit purchase.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/seller-management/how-merchant-settlements-are-processed.md`: How merchant settlements and installments are processed; Settlement scenarios; Scheduled settlement; Scheduled settlements and same-day settlements; Scheduled and same-day settlements plus cancellation; Negative balance; Merchant transaction settled event; Overriding the scheduled payment date; Installment plans; Recalculation on the second installment; Recurring decimal breaks

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 2 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/seller-management/how-merchant-settlements-are-processed.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/how-merchant-settlements-are-processed · updatedAt: 2026-03-18T15:24:22.000Z

<!-- source:begin path=docs/seller-management/how-merchant-settlements-are-processed.md part=0-end -->

# How merchant settlements and installments are processed

Transaction settlement is the process of moving funds from the cardholder’s account to the merchant’s account after the cardholder makes a credit or debit purchase.

Settlement occurs on the configured settlement date, ensuring that the amount transferred matches what the merchant expects to receive. Although you cannot configure settlement schedules, you can configure the payment schedule rules that determine how many days after a sale a transaction becomes eligible for settlement. For more information, refer to the note in the [Settlement scenarios](#settlement-scenarios) section.

The Pismo platform settles merchant transactions daily according to settlement schedules. Consult with your Pismo representative to choose an appropriate settlement batch time to run settlements based on your timezone and business needs. For example, if you want to settle all the transactions scheduled for the previous day just after midnight, and your timezone is GMT-3, a suitable time would be 03:00 or 04:00 GMT. This gives you some margin for adjustments or updates to the schedule when needed.

The [Merchant transaction settled](https://developers.pismo.io/pismo-docs/docs/how-merchant-settlements-are-processed#merchant-transaction-settled-event) event provides the final settlement date and the net amount to be transferred to the merchant for that day. The platform generates one event for each merchant who has an amount to be settled on that day.

The following scenarios illustrate timeline examples with different settlement stages, including examples of regular sales and examples of sales that include cancellation and negative balances. In these illustrations, you learn how different transactions that occur and settle at different points in time affect final settlement outcomes.

# Settlement scenarios

The example scenarios in this section use the following acronyms for settlement schedules.

D0: Payment scheduled to be settled on the same day as the sale\
D1: Payment scheduled to be settled one day after the sale\
D2: Payment scheduled to be settled two days after the sale\
Dn: Payment scheduled to be settled *n* days after the sale

Because settlement runs once per day, any D0 (Day zero) sale that occurs after the daily settlement batch will settle in the next settlement batch operation.

> 📘 Notes
>
> * You can configure conditions to settle the sales amount to merchants and also the fees applicable on this amount, so that the settlement for the merchant occurs within any range of days after the sale. Specify this range by providing values for `first_installment_days_to_payment` and `n_installment_days_to_payment` in the [Create creditor operation](https://developers.pismo.io/pismo-docs/reference/postcreditorsoperations) endpoint.
> * You can override `first_installment_days_to_payment` by specifying a fixed date for the first payment. For more information, refer to [Overriding the scheduled payment date](https://developers.pismo.io/pismo-docs/docs/how-merchant-settlements-are-processed#overriding-the-scheduled-payment-date).
> * In the following scenarios, the scheduled settlement is set to occur at 07:00 GMT every day.

## Scheduled settlement

<Image alt="Image showing a scheduled settlement." align="center" src="https://files.readme.io/61527d7-diagram-regular-sales_d1d2.png" />

1. Sale A (USD 20,000) takes place on April 22nd, and Sale B on the 23rd (USD 30,000), both are scheduled to settle in the morning of April 24th.
2. On April 24th, the merchant receives a total settlement amount of USD 50,000.

## Scheduled settlements and same-day settlements

<Image alt="Image showing scheduled settlements and same-day settlements" align="center" src="https://files.readme.io/9440bb2-diagram-regular-sales_d1d2d0.png" />

In this scenario, the following takes place:

1. Sale A (USD 20,000) occurs on April 22nd, and the payment is scheduled to settle on the 24th.
2. Sale B (USD 30,000) takes place on April 23rd, and the payment is scheduled for the 24th.
3. Sale C (USD 1,000) occurs on April 24th, and the payment is scheduled  for the 25th.
4. Sale D (USD 2,000) takes place on the 24th, and the payment is scheduled for the 25th.
5. Therefore, on April 24th, the merchant receives the settlement amount of USD 50,000 (Sale A + B) and receives USD 3,000 (Sale C + D) on April 25th.\
   **Note**: Although Sales C and D are D0 (eligible for same‑day settlement), they occurred after the daily settlement batch had already run. As a result, they settle the next day, which is the 25th.

## Scheduled and same-day settlements plus cancellation

<Image alt="Image showing scheduled and same-day settlements plus cancellation" align="center" src="https://files.readme.io/4b9011d-diagram-regular-sales_d1d2d0-cancel1.png" />

In this scenario, a cancellation is added to the settlement process:

1. Sale A (USD 20,000) occurs on April 22nd and is scheduled to settle on the 24th.
2. Sale B (USD 30,000) takes place on the 23rd and is also scheduled to settle on the 24th.
3. Sale C (USD 1,000) happens on the 24th and is scheduled to settle on the 25th.
4. Sale D (USD 2,000) occurs on the 24th and is scheduled to settle on the 25th.
5. Therefore, the total settlement amount for April 24th is USD 50,000 (Sale A + B).
6. However, a cancellation of USD 30,000 takes place on the 24th and is scheduled to settle on the 25th; therefore, the final settlement amount is USD -27,000 on April 25th. This negative settlement amount is carried forward as a balance owed by the merchant.

## Negative balance

<Image alt="Image showing a negative balance." align="center" src="https://files.readme.io/004aeb6-diagram-regular_sales_d1d2d0cancelnegative_balance1.png" />

This scenario becomes even more complex when there is a negative balance involved. In this scenario:

1. Sale A (USD 20,000) occurs on April 22nd and is scheduled to settle on the 24th.
2. Sale B (USD 30,000) takes place on the 23rd and is also scheduled to settle on the 24th.
3. Sale C (USD 1,000) happens on the 24th and is scheduled to settle on the 25th.
4. Sale D (USD 2,000) occurs on the 24th and is scheduled to settle on the 25th.
5. Therefore,  on the 24th, the amount that is settled is USD 50,000.
6. However, on April 24th, a cancellation of Sale B takes place and is scheduled to settle on the 25th.
7. On the 25th, the merchant has a negative settlement amount of USD -27,000 (Sale (C + D) - B).
8. On April 25th, Sale E (USD 5,000) occurs and is scheduled to settle on the 26th; as a result, the merchant’s balance becomes USD -22,000. Because the balance is still negative, the amount from Sale E is applied to reduce the negative balance rather than transferred to the merchant.

# Merchant transaction settled event

As illustrated in the preceding scenarios, one of the complexities is reconciling settlement values. To accurately identify payment dates and the amount that the merchant expects to receive, the Pismo platform generates a [Merchant transaction settled](https://developers.pismo.io/events/docs/merchants-merchant-transaction-settled-1) event, which contains up-to-date information to help you reconcile and understand what the merchant can expect to receive on the settlement date. For example, to identify the settlement amount, use the value in `settlement_amount`. To find the settlement date for a transaction, use the `settlement_date` value.

# Overriding the scheduled payment date

You can override the previously configured `first_installment_days_to_payment` field in [Create creditor operation](https://developers.pismo.io/pismo-docs/reference/postcreditorsoperations) by providing a fixed date for the first payment. To do this, use the [Request authorization](https://developers.pismo.io/pismo-docs/reference/post-authorization) endpoint to send a `minimum_settlement_date` in the `metadata` object. The following sample payload illustrates this.

```json
{
	"mti": "0100",
	"merchant": {
		"id": "mc-12345",
		"name": "Acme Used Books",
		"city": "San Diego",
		"country": "USA",
		"category_code": "5099",
		"marketplace_id": "mkt-1234"
	},
	"amount": 10,
	"currency": "986",
	"network": "Mastercard",
	"account_id": 123456789,
	"authorization_mode": "CREDIT",
	"entry_mode": "05",
	"clearing_type": "ONLINE",
	"processing_code": "P01001",
	"number_of_installments": 2,
	"metadata": {
		"minimum_settlement_date": "2024-07-22"
	}
}
```

As an example of how this feature might be used, suppose you have a marketplace campaign that extends between 15 July 2024 and 21 July 2024. When scheduling the settlement for these purchases, the merchants require that the first payment occur on 22 July 2024 instead of following the default 10‑day schedule. To implement this, use the above endpoint with `minimum_settlement_date` set to "2024-07-22".

# Installment plans

The Pismo platform creates the retailer installment plan (interest-free installments) at the time of purchase confirmation. It divides the total amount into several debit transactions, each representing a separate installment.

The platform also creates a contract transaction used solely for internal bookkeeping. This entry is not shown on the customer invoice.

## Recalculation on the second installment

After creating the plan, the platform divides the total purchase amount by the number of installments. It calculates the amount of each installment at the time of authorization, taking into account possible rounding. For example, for a purchase of R$100.00 in 3 installments, the first installment could be R$33.34 and the remaining installments R$33.33, to ensure the total amount is distributed correctly.

The installment amounts do not change after authorization. Each installment remains fixed unless the purchase is canceled or prepaid. The amount of each installment is already set at the time of purchase and remains fixed until the end of the plan, except in cases of cancellation or advance payment.

## Recurring decimal breaks

When the total purchase amount is not evenly divisible by the number of installments, a recurring decimal break occurs. In this case, the system rounds up the first installment to ensure that the sum of the installments equals the total purchase amount. For example, on a purchase of R$ 100.00 in 3 installments:

1st installment: R$ 33.34

2nd installment: R$ 33.33

3rd installment: R$ 33.33

The platform makes this adjustment automatically, with no impact on the customer or the retailer.
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `POST /marketplaces/{marketplaceId}/creditors-operations` | `PostCreditorsOperations` | Create creditor operation | `api-specs/Seller_management_-_Marketplace.yaml` | no | KU-API-seller-management-marketplace--marketplace-creditor-operations |
| `POST /payment-methods/v1/authorization` | `post-authorization` | Request authorization | `api-specs/Core_platform_-_Payment_methods.yaml` | no | KU-API-core-platform-payment-methods--payment-methods-part-01 |

### Operation essentials

- **`POST /marketplaces/{marketplaceId}/creditors-operations`** (`PostCreditorsOperations`): security `BearerAuth`; required parameters `marketplaceId` (path); required body fields `creditor_id`, `first_installment_days_to_payment`, `installments`, `n_installment_days_to_payment`; response statuses 200, 400, 401, 500; error codes in examples none; events `marketplace-marketplace-creditor-operation-created-1`.
- **`POST /payment-methods/v1/authorization`** (`post-authorization`): security `BearerAuth`; required parameters none declared; required body fields `currency_code`, `mti`, `network`; response statuses 200, 201, 400, 401, 403, 422, 500; error codes in examples `WONA0001`, `WONA0004`, `WONA0005`, `WONA0006`, `WONA0011`, `WONA0012`, `WONA0013`, `WONA0015`, `WONA0016`, `WONA0018`, `WONA0019`, `WONA0020`, `WONA0032`, `WONA0033`, `WONA0036`, `WONA039`, `WONA040`, `WONA041`, `WONA042`, `WONA043`, `EINS0004`, `EINS0005`, `EINS0006`, `EINS0010`, `EINS0011`, `EINS0012`, `EINS0015`, `EINS0016`, `EPAE0004`, `EPAE0001`, `EPAE0002`; events `payment-methods-authorization-1`, `platform-authorization-platform-authorization-1`.

## Events

Events emitted by the referenced operations (`api-reference-data/endpoint_event_map.csv`):

| Operation | Event slug |
| --- | --- |
| `PostCreditorsOperations` | `marketplace-marketplace-creditor-operation-created-1` |
| `post-authorization` | `payment-methods-authorization-1` |
| `post-authorization` | `platform-authorization-platform-authorization-1` |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/seller-management/how-merchant-settlements-are-processed.md`: updatedAt 2026-03-18T15:24:22.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- The source links to 1 event page(s) under `/events/`. Event payload definitions are not part of the corpus (robots.txt disallows `/events/`), so payload fields are not documented here.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/seller-management/how-merchant-settlements-are-processed.md` | whole document | https://developers.pismo.io/pismo-docs/docs/how-merchant-settlements-are-processed | `d2a797fc0ca3478d…` | 2026-03-18T15:24:22.000Z |

## Related knowledge units

- `KU-API-core-platform-payment-methods--payment-methods-part-01` — API reference: Core platform - Payment methods — Payment methods (part 1 of 3)
- `KU-API-seller-management-marketplace--marketplace-creditor-operations` — API reference: Seller management - Marketplace — Marketplace creditor operations
- `KU-EVT-catalogue-marketplace` — Event catalogue: marketplace
- `KU-EVT-catalogue-other-domains` — Event catalogue: other event domains (accounting, authorization, availables, average, bulletin, cash, delinquent, fraud, instantpay, intl, ledger, networktransactions, onboarding, orgs, payment, platform, programs, rules, savings, statement)
