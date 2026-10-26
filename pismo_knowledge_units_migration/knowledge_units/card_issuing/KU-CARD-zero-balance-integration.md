---
ku_id: KU-CARD-zero-balance-integration
title: Zero balance integration and anti-fraud validations
category: card_issuing
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/card-issuing/zero-balance-integration.md
  sha256: c3a93bb3e8faf434cda2d205da17306950ff5e5dbe5c2b3567501bf88c4c6d7a
  url: https://developers.pismo.io/pismo-docs/docs/zero-balance-integration
  role: primary_guide
  updated_at: '2026-03-18T15:23:47.000Z'
- path: docs/card-issuing/zero-balance-anti-fraud-integration-1.md
  sha256: 68c28663675f8e7610819f0a1b3ba8896dbc5fd5c6e9a4a469d925306484d743
  url: https://developers.pismo.io/pismo-docs/docs/zero-balance-anti-fraud-integration-1
  role: primary_guide
  updated_at: '2026-03-18T15:20:12.000Z'
operations: []
related_kus:
- KU-CARD-card-network-integration
- KU-CARD-clearing
- KU-CARD-full-and-zero-balance-workflows
- KU-CARD-full-balance-versus-zero-balance
- KU-CORE-processing-codes-and-transaction-types
- KU-EVT-client-webhooks-part-01
- KU-EVT-client-webhooks-part-02
- KU-EVT-client-webhooks-part-03
- KU-EVT-client-webhooks-part-04
- KU-EVT-client-webhooks-part-05
- KU-EVT-client-webhooks-part-06
- KU-EVT-client-webhooks-part-07
- KU-EVT-client-webhooks-part-08
- KU-EVT-client-webhooks-part-09
- KU-EVT-client-webhooks-part-10
- KU-EVT-client-webhooks-part-11
- KU-EVT-client-webhooks-part-12
- KU-EVT-client-webhooks-part-13
- KU-EVT-client-webhooks-part-14
grouping_rationale: Issuer guide and its anti-fraud part.
---

# Zero balance integration and anti-fraud validations

**KU ID:** `KU-CARD-zero-balance-integration` · **Category:** Card issuing · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 2 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: Issuer guide and its anti-fraud part.

Scope as stated in `docs/card-issuing/zero-balance-integration.md`:

> This is a guide on integrating with Pismo using the [Zero balance integration model](https://developers.pismo.io/pismo-docs/docs/card-network-integration).

Scope as stated in `docs/card-issuing/zero-balance-anti-fraud-integration-1.md`:

> This guide details the call the Pismo platform makes to a Zero balance issuer during step 5 in the [Full and zero balance transaction workflows](https://developers.pismo.io/pismo-docs/docs/full-and-zero-balance-workflows). Zero balance issuers need to do their own account and limit checks as well as anti-fraud checks.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/card-issuing/zero-balance-integration.md`: Zero balance integration - issuer's guide; Zero balance webhook; Issuer webhook logic; Single and dual message system considerations; Accounting and regulatory reports
- `docs/card-issuing/zero-balance-anti-fraud-integration-1.md`: Zero balance anti-fraud and validations integration; Balance inquiry for Zero balance clients; Visa partial authorization; Partial authorization response

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/card-issuing/zero-balance-integration.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/zero-balance-integration · updatedAt: 2026-03-18T15:23:47.000Z

<!-- source:begin path=docs/card-issuing/zero-balance-integration.md part=0-end -->

# Zero balance integration - issuer's guide

This is a guide on integrating with Pismo using the [Zero balance integration model](https://developers.pismo.io/pismo-docs/docs/card-network-integration).

Existing Zero balance documentation:

* [Full balance versus Zero balance integration](https://developers.pismo.io/pismo-docs/docs/full-balance-versus-zero-balance)—Contains a table summarizing the differences between Full and Zero balance integration. Further details about the different functionality are also provided.
* [Full and Zero balance workflows ](https://developers.pismo.io/pismo-docs/docs/full-and-zero-balance-workflows)—Details the differences between Full and Zero balance workflows for card authorization.
* [Zero balance validations and anti-fraud webhook](https://developers.pismo.io/pismo-docs/docs/client-webhooks#zero-balance-validations-webhook)—Specifications for the Zero balance webhook called during authorization that allows Zero balance customers to do their own validations and anti-fraud checks.

# Zero balance webhook

One of the most critical integration points for Zero balance customers comes when transaction authorization is requested in real time. The response has to be fast and accurate (2 seconds max)  and adhere to network standards. Your response needs to be automated with low application and network latency.

The [client webhook call](https://developers.pismo.io/pismo-docs/docs/client-webhooks#zero-balance-validations-webhook) contains important business information: date, IDs, amount, operation type, merchant, if CVV was validated, if chip was validated, if there is a recommendation to deny and so on.

If your system already has  logic to capture and interpret incoming authorizations, it is common to convert Pismo’s webhook request into a format your system can interpret. Likewise, it may be useful to have a formatter to transform your system's response to Pismo’s response format.

If your system does not have authorization processing logic yet, then directly interacting with Pismo’s webhook request and response formats makes more sense.

# Issuer webhook logic

Before replying back to an authorization request, either to approve or reject, your validations and checks should be done in a logical order. One way to determine that is is to look at the existing rejection reasons and criteria associated with your card network.

You logic should minimize the need to make unnecessary validations or processing. For example, there is no need to validate a transaction if the account is blocked or not in a valid/active status. Another is to look at Pismo's request and see if you agree with what was passed. For example, if you are receiving a card chip transaction and the chip validation failed, you can probably reject this authorization without further processing.

**Other considerations:**

* **Permitted authorization**—Assess if there are any rules that would prevent the authorization, such as a Merchant Category Code (MCC) that you do not accept
* **Balance**—Assess if the customer has enough balance/limit to perform the authorization; for regions with partial authorization, passing the available balance/limit in the reply may be mandatory
* **Anti-fraud and anti-money laundering**—Run additional checks to validate authorization legitimacy.

# Single and dual message system considerations

Most modern product implementations use the dual message system (DMS), though single message system (SMS) still exists in the market. A dual message system is a payment processing method that sends two messages to process a transaction, while a single message system sends one message.

When an authorization is approved in a dual message system (DMS), it does not necessarily mean that it is confirmed. Only a [Clearing/Base II file](https://developers.pismo.io/pismo-docs/docs/clearingbase) confirms an authorization. It is your responsibility to place a hold on an account's available balance/limit until confirmation is made, otherwise there is a risk that the account holder will spend funds without a correct balance/limit.

For most card networks, confirmation arrives between 8-10 days after an authorization is approved. If a confirmation does not arrive, the standard practice is to revert the hold on account balance/limit.

Please note that a Clearing/Base II file may arrive after the usual time and you are expected to make best efforts to post/collect the transaction. It is also possible to receive confirmation for transactions that the authorizer did not approve or has different values. In these cases, you are also expected to make best efforts to post/collect the transaction.

In single message systems (SMS), this flow is simplified as the authorization already constitutes settlement confirmation.

# Accounting and regulatory reports

When working in Zero balance mode, Pismo has a limited view of the issuer’s balance data. Therefore, it is the issuer’s responsibility to ensure proper accounting is taking place.

It is important to control and take into consideration (credit or debit, non-exhaustive list):

* Available balance/limit
* Authorizations
* Reversals
* Chargebacks
* Fraud
* Confirmed transactions
* Taxes
* Fees
<!-- source:end -->

### Source 2: `docs/card-issuing/zero-balance-anti-fraud-integration-1.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/zero-balance-anti-fraud-integration-1 · updatedAt: 2026-03-18T15:20:12.000Z

<!-- source:begin path=docs/card-issuing/zero-balance-anti-fraud-integration-1.md part=0-end -->

# Zero balance anti-fraud and validations integration

This guide details the call the Pismo platform makes to a Zero balance issuer during step 5 in the [Full and zero balance transaction workflows](https://developers.pismo.io/pismo-docs/docs/full-and-zero-balance-workflows). Zero balance issuers need to do their own account and limit checks as well as anti-fraud checks.

Zero balance issuers need to register a webhook URL for this process during setup. This webhook enables you to send an authorization response to the request that is detailed in the [Zero balance anti-fraud and validations request](https://developers.pismo.io/pismo-docs/docs/client-webhooks#zero-balance-validations-webhook) webhook specification.

> 📘 Basic card validations failure
>
> Note that this webhook is not called if an authorization fails the card checks that Pismo does. In that case, Pismo just responds to the network.

Below is the sample payload that the Pismo platform sends to the card issuer. The example contains some simulated information in the fields. The missing values depend on the type of authorization request the Pismo platform receives from the card network.

<details>
  <summary>Sample payload</summary>

  ```Text Sample payload
  {
      "id": "99999999-aaaa-aaaa-1111-1234567abcde",
      "entity": "transaction",
      "fields": {
          "mti": "0100",
          "card_id": 1,
          "account_id": 1,
          "amount_transaction": 10.10,
          "amount_local": 10.10,
          "amount_settlement": 2.05,
          "transaction_timestamp": "2021-11-05T16:00:00",
          "processing_code": "000000",
          "payment_card_brand": "Mastercard",
          "currency": "986",
          "merchant_id_code": "599999000009999",
          "merchant_name": "MERCHANT NAME  ",
          "merchant_city": "MERCHANT CITY     ",
          "merchant_state_or_country_code": "USA",
          "merchant_terminal_id": "",
          "atc_chip": "",
          "atc_database": "",
          "cvv_data": "",
          "entry_mode": "10",
          "mcc": "5942",
          "card_type": "PLASTIC",
          "country_code": "",
          "chip_validation": true,
          "postal_code": "99999999",
          "chip_cryptogram_information_data": "",
          "chip_transaction_date": "",
          "chip_transaction_type": "",
          "chip_amount_authorized": "",
          "chip_transaction_currency_code": "",
          "chip_application_interchange_profile": "",
          "chip_terminal_country_code": "",
          "chip_cardholder_verification_method": "",
          "chip_terminal_capabilities": "",
          "chip_amount_other": "",
          "chip_application_transaction_counter": "",
          "cardholder_postal_code": "",
          "transaction_type": "00",
          "nsu": "999999",
          "retrieval_reference_number": "999919319999",
          "authorization_code": "ABC123",
          "response_code": "00",
          "terminal_capability": "2",
          "tvr": "",
          "cvr": "",
          "number_of_installments": 1,
          "network_score": 0,
          "pos_postal_code": "99999999",
          "acquirer_code": "016205",
          "denial_code": "",
          "financial_network_code": "MRW",
          "banknet_reference_number": "ZZZ999",
          "network_transaction_data": "",
          "original_network_data": {}, 
          "cvv_presence": false,
          "password_present": false,
          "account_type": "00",
          "validation_results": [{}]
      }
  }
  ```
</details>

The expected response from the card issuer for the approved transaction:

```Text JSON
{
  "is_approved":true,
  "response_code":"00"
}
```

The expected response from the card issuer for the declined transaction:

```Text JSON
{
  "is_approved":false,
  "response_code":"57",
  "limit_amount":null
}
```

# Balance inquiry for Zero balance clients

Zero balance customers have the option to check a customer's current available credit limit.  If a Zero balance webhook request is made with [processing code](https://developers.pismo.io/pismo-docs/docs/processing-codes-and-transaction-types)  30 (balance inquiry), then the response should include an `available_credit_limit` object:

```json
{
 "is_approved": true,
 "response_code": "00",
 "available_credit_limit": {
   "amount": 10.0,
   "currency_code": 986
 }
}

```

# Visa partial authorization

Partial authorization addresses insufficient fund declines at the point-of-sale. It provides an alternative to a declined transaction when the available Visa card or account balance is not sufficient to approve a transaction in full. Instead of a decline, the transaction is approved for a portion of the original amount requested. The remainder of the transaction amount may then be paid by other means using split tender functionality, where applicable.

## Partial authorization response

Set the following fields in the `partial_approval_info` object in the authorization response:

* **`local_amount`** - Amount that was partially approved in the transaction's local currency.
* **`settlement_amount`**- Amount that was partially approved in the reconciliation currency.
* **`cardholder_amount`**- Amount that was partially approved in the cardholder's currency.

**Example response**

```Text JSON
{
   "is_approved": true,
   "response_code": "10", 
   "limit_amount": null,

   "partial_approval_info": {
      "local_amount": 10.00,
       "settlement_amount": 2.00,
       "cardholder_amount": 8.50
     }
}
```

> 🚧 Decimal place precision
>
> The number of decimal places is according to ISO 3166-1 and ISO 4217. For example, both the Brazilian real  and United States dollar need to be precise to two decimal places. This applies only to the partial authorization response.

A **`response_code`** = "10" means that the transaction was partially approved, and the issuer needs to return the approved amounts fields. When these fields aren't returned or the amounts are negative, Pismo returns the `ZBD` custom field and **`response_code`** =  96.
<!-- source:end -->

## Lifecycle status

- `docs/card-issuing/zero-balance-integration.md`: updatedAt 2026-03-18T15:23:47.000Z.
- `docs/card-issuing/zero-balance-anti-fraud-integration-1.md`: updatedAt 2026-03-18T15:20:12.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- Source content contains MDX/HTML components (for example `<Table>`, `<HTMLBlock>`, `<Callout>`, `<details>`). They are preserved exactly as published; tables inside them were not converted to Markdown.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/card-issuing/zero-balance-integration.md` | whole document | https://developers.pismo.io/pismo-docs/docs/zero-balance-integration | `c3a93bb3e8faf434…` | 2026-03-18T15:23:47.000Z |
| `docs/card-issuing/zero-balance-anti-fraud-integration-1.md` | whole document | https://developers.pismo.io/pismo-docs/docs/zero-balance-anti-fraud-integration-1 | `68c28663675f8e76…` | 2026-03-18T15:20:12.000Z |

## Related knowledge units

- `KU-CARD-card-network-integration` — Card network integration and certification
- `KU-CARD-clearing` — Clearing: Base II and the clearing rules engine
- `KU-CARD-full-and-zero-balance-workflows` — Full and Zero balance transaction workflows
- `KU-CARD-full-balance-versus-zero-balance` — Full balance versus Zero balance integration
- `KU-CORE-processing-codes-and-transaction-types` — Processing codes
- `KU-EVT-client-webhooks-part-01` — Client webhooks (part 1 of 14)
- `KU-EVT-client-webhooks-part-02` — Client webhooks (part 2 of 14)
- `KU-EVT-client-webhooks-part-03` — Client webhooks (part 3 of 14)
- `KU-EVT-client-webhooks-part-04` — Client webhooks (part 4 of 14)
- `KU-EVT-client-webhooks-part-05` — Client webhooks (part 5 of 14)
- `KU-EVT-client-webhooks-part-06` — Client webhooks (part 6 of 14)
- `KU-EVT-client-webhooks-part-07` — Client webhooks (part 7 of 14)
- `KU-EVT-client-webhooks-part-08` — Client webhooks (part 8 of 14)
- `KU-EVT-client-webhooks-part-09` — Client webhooks (part 9 of 14)
- `KU-EVT-client-webhooks-part-10` — Client webhooks (part 10 of 14)
- `KU-EVT-client-webhooks-part-11` — Client webhooks (part 11 of 14)
- `KU-EVT-client-webhooks-part-12` — Client webhooks (part 12 of 14)
- `KU-EVT-client-webhooks-part-13` — Client webhooks (part 13 of 14)
- `KU-EVT-client-webhooks-part-14` — Client webhooks (part 14 of 14)
