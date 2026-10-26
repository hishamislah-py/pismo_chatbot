---
ku_id: KU-CARD-authorization-validation-rules-for-card-network-operations
title: Authorization validation rules for card network operations
category: card_issuing
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/card-issuing/authorization-validation-rules-for-card-network-operations.md
  sha256: 110b362325dc423dc0bad0eedcc1dbe23d1d2f83231046408a95fcd73651fe6c
  url: https://developers.pismo.io/pismo-docs/docs/authorization-validation-rules-for-card-network-operations
  role: primary_guide
  updated_at: '2026-06-28T21:48:49.000Z'
operations: []
related_kus:
- KU-CARD-anti-fraud-integration
- KU-CARD-authorization-events
- KU-CARD-rule-list-part-01
- KU-CARD-rule-list-part-02
- KU-CARD-rule-list-part-03
- KU-CARD-rule-list-part-04
- KU-CARD-zero-balance-integration
- KU-EVT-catalogue-other-domains
grouping_rationale: single source page
---

# Authorization validation rules for card network operations

**KU ID:** `KU-CARD-authorization-validation-rules-for-card-network-operations` · **Category:** Card issuing · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/card-issuing/authorization-validation-rules-for-card-network-operations.md`:

> The Pismo platform follows a list of rules to validate a transaction. After performing these validations and determining whether to accept or reject the transaction, the platform delivers the validation results data to the client in the [Network authorization event](https://developers.pismo.io/events/docs/networktransactions-network-authorization-1).

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/card-issuing/authorization-validation-rules-for-card-network-operations.md`: Authorization validation rules for card network operations; Overriding the response code; Validation results data; List of Rules

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/card-issuing/authorization-validation-rules-for-card-network-operations.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/authorization-validation-rules-for-card-network-operations · updatedAt: 2026-06-28T21:48:49.000Z

<!-- source:begin path=docs/card-issuing/authorization-validation-rules-for-card-network-operations.md part=0-end -->

# Authorization validation rules for card network operations

The Pismo platform follows a list of rules to validate a transaction. After performing these validations and determining whether to accept or reject the transaction, the platform delivers the validation results data to the client in the [Network authorization event](https://developers.pismo.io/events/docs/networktransactions-network-authorization-1).

<Callout icon="📘" theme="info">
  The [Network Authorization event](https://developers.pismo.io/events/docs/networktransactions-network-authorization-1) is the primary event for verifying authorizations. However, the authorization workflow sends other events that you should also consume. For more information, refer to  [Authorization events](https://developers.pismo.io/pismo-docs/docs/authorization-events).
</Callout>

The transaction validation rules depend on whether the client is full balance or zero balance:

* In full balance integration, the platform sends the same validation results data in a request to an external [anti-fraud](https://developers.pismo.io/pismo-docs/docs/anti-fraud-integration) service provided by one of Pismo's partners. You select which partner you want Pismo to use for this service during program setup.
* In zero balance integration, the platform sends the validation results data in a request to a [card issuer webhook](https://developers.pismo.io/pismo-docs/docs/zero-balance-anti-fraud-integration-1), which you must register during setup. You should use this data to perform your own set of validations.

If the anti-fraud service (for full balance) or your own validation process (for zero balance) denies the transaction, the Pismo platform notifies the card network that the transaction is denied.

If the Pismo platform denies the transaction, but the anti-fraud service or your validation process approves it, the platform's behavior depends on how your program is configured. The next section explains this in detail.

> 📘 International installment purchases
>
> While making purchases in installments is common in Brazil, the Pismo platform does not support this payment method for international purchases. Authorizations for installment purchases will be denied.

# Overriding the response code

There are several settings that can override the response code:

* **Override Response Code** – If this setting is activated, the anti-fraud system can override the Pismo platform's response code. For example, suppose a purchase is declined by Pismo with response code 57. In this scenario, the anti-fraud system might override it with another valid response code such as 63. Since the response code is what the Pismo platform sends to the network, overriding it effectively overrides the platform's decision as far as the network is concerned. Internally, however, the platform's decision is not overridden. To activate this setting, you open a service ticket with the Authorization team.
* **Override Pismo Decision** – If this setting is activated, the anti-fraud system's decision is final. All Pismo platform decisions are overridden. To activate this setting, you open a service ticket with the Authorization team.
* **Override At Request Level** – The anti-fraud system can force the Pismo platform to approve any given authorization request by including the parameter `force_approve` in its response and setting it to `True`.

Refer to [Overwrite the Pismo platform decision](https://developers.pismo.io/pismo-docs/docs/anti-fraud-integration#overwrite-the-pismo-platform-decision) for more information.

# Validation results data

After the Pismo platform finishes applying the validation rules to a transaction, it creates a list of objects containing the validation results. Each object represents the result of applying a specific validation rule. This data is sent to the client in the `validation_results`field of the [Network authorization event](https://developers.pismo.io/events/docs/networktransactions-network-authorization-1). It's also sent to the anti-fraud service (full balance integration) or to the [card issuer webhook](https://developers.pismo.io/pismo-docs/docs/zero-balance-anti-fraud-integration-1) (zero balance integration).

<Callout icon="📘" theme="info">
  The `validation_results` field of the [Network Authorization event](https://developers.pismo.io/events/docs/networktransactions-network-authorization-1) always contains the result for every rule in the list, even if that result is `SKIPPED`.
</Callout>

Every object in the list contains the following fields:

* `name` – Name of the evaluated rule. You use this field to find the result of a specific validation. The order of the validations inside the list can change, so you must use the `name` field for this.
* `status` – Identifies how the rule was evaluated: approved (APPROVED), rejected (REJECTED), or not evaluated (SKIPPED).
* `reason` – The reason the rule was not approved.  After identifying the rule itself using the field name, you can use this information to do your own monitoring. For example, you could monitor how many purchases were denied because of  LEDGER\_INSUFFICIENT\_BALANCE.
* `description` – Describes the validation result in a textual form. This field should not be used as a key. It's only intended to help you understand the validation result.
* `additional_data` – This optional field contains important additional information related to the validation. You can use this information for your own monitoring. For example, you can monitor custom denial codes using the `additional_data` field of the [Flex controls validation](https://developers.pismo.io/pismo-docs/docs/rule-list#flex-controls-validation) rule.

<details>
  <summary>Validation results example</summary>

  ```json
  {
      "validation_results": [
          {
              "name": "MAGNETIC_STRIPE",
              "status": "SKIPPED",
              "reason": "NO_MAGNETIC_STRIPE",
              "description": "No magnetic stripe",
              "additional_data": {}
          },
          {
              "name": "TERMINAL_CAPABILITY",
              "status": "APPROVED",
              "reason": "TERMINAL_CAPABILITY_VALID",
              "description": "Terminal capability is valid",
              "additional_data": {}
          },
          {
              "name": "ARQC",
              "status": "SKIPPED",
              "reason": "NO_CRYPTOGRAM",
              "description": "No cryptogram present",
              "additional_data": {}
          },
          {
              "name": "CVM",
              "status": "APPROVED",
              "reason": "MDES_WITH_PIN_VALIDATED_OFFLINE",
              "description": "Mdes with pin validated offline",
              "additional_data": {}
          },
          {
              "name": "ENTRY_MODE",
              "status": "APPROVED",
              "reason": "ENTRY_MODE_VALID",
              "description": "Entry mode valid",
              "additional_data": {}
          },
          {
              "name": "CHIP_SIGNATURE",
              "status": "SKIPPED",
              "reason": "NO_CHIP_SIGNATURE",
              "description": "No chip signature present",
              "additional_data": {}
          },
          {
              "name": "CARD_EXISTS",
              "status": "APPROVED",
              "reason": "CARD_FOUND",
              "description": "Card exists.",
              "additional_data": {}
          },
          {
              "name": "CARD_MODE",
              "status": "APPROVED",
              "reason": "CARD_MODE_VALID",
              "description": "Valid card mode",
              "additional_data": {}
          },
          {
              "name": "CARD_TOKEN_STATUS",
              "status": "APPROVED",
              "reason": "CARD_TOKEN_STATUS_VALID",
              "description": "Card token status: ACTIVE.",
              "additional_data": {}
          },
          {
              "name": "PROGRAM",
              "status": "APPROVED",
              "reason": "PROGRAM_FOUND",
              "description": "Program ProgramId found.",
              "additional_data": {}
          },
          {
              "name": "PROGRAM_CONFIG",
              "status": "APPROVED",
              "reason": "PROGRAM_CONFIG_FOUND",
              "description": "Program found.",
              "additional_data": {}
          },
          {
              "name": "DCC",
              "status": "SKIPPED",
              "reason": "NOT_DCC_TRANSACTION",
              "description": "It is not a DCC transaction.",
              "additional_data": {}
          },
          {
              "name": "CONTACTLESS",
              "status": "APPROVED",
              "reason": "CONTACTLESS_ENABLED",
              "description": "Contactless enabled.",
              "additional_data": {}
          },
          {
              "name": "ACCOUNT_TYPE",
              "status": "APPROVED",
              "reason": "ACCOUNT_TYPE_VALID",
              "description": "Account Type: CREDIT_CARD_ACCOUNT. Card Mode: CREDIT.",
              "additional_data": {}
          },
          {
              "name": "CARD_ATC",
              "status": "APPROVED",
              "reason": "CARD_ATC_VALID",
              "description": "Received null but the last is null. Used these params: MinOffset: 5, MaxOffset: 15, IsAdvice: false.",
              "additional_data": {}
          },
          {
              "name": "OPERATION",
              "status": "APPROVED",
              "reason": "VALID_OPERATION",
              "description": "Valid operation (00) for OrgId (OrgId) and ProgramId (ProgramId).",
              "additional_data": {}
          },
          {
              "name": "PASSWORD_ATTEMPTS",
              "status": "APPROVED",
              "reason": "CARD_PASSWORD_ATTEMPTS_VALID",
              "description": "Password tries is valid.",
              "additional_data": {}
          },
          {
              "name": "CARD_INPUTTED_EXPIRATION_DATE",
              "status": "APPROVED",
              "reason": "CARD_INPUTTED_EXPIRATION_DATE_VALID",
              "description": "Card inputted expiration date is valid.",
              "additional_data": {}
          },
          {
              "name": "CARD_VALID_UNTIL",
              "status": "APPROVED",
              "reason": "CARD_VALID_UNTIL_VALID",
              "description": "Card is valid.",
              "additional_data": {}
          },
          {
              "name": "CARD_EXPIRATION_DATE",
              "status": "APPROVED",
              "reason": "CARD_NOT_EXPIRED",
              "description": "Card not expired.",
              "additional_data": {}
          },
          {
              "name": "CARD_STATUS",
              "status": "APPROVED",
              "reason": "CARD_STATUS_VALID",
              "description": "Card status: NORMAL.",
              "additional_data": {}
          },
          {
              "name": "ACCOUNT_LIMITS",
              "status": "APPROVED",
              "reason": "ACCOUNT_LIMITS_FOUND",
              "description": "Account limits exists.",
              "additional_data": {}
          },
          {
              "name": "ACCOUNT_STATUS",
              "status": "APPROVED",
              "reason": "ACCOUNT_STATUS_VALID",
              "description": "Account has a valid status: true.",
              "additional_data": {}
          },
          {
              "name": "CREDIT_LIMIT",
              "status": "APPROVED",
              "reason": "CREDIT_LIMIT_IMPACT_FOUND",
              "description": "Acceptances found.",
              "additional_data": {}
          },
          {
              "name": "MAX_TRANSACTIONS_FOR_TEMPORARY_CARD",
              "status": "SKIPPED",
              "reason": "MAX_TRANSACTIONS_IF_TEMPORARY_CARD_SKIPPED",
              "description": "Card is not temporary.",
              "additional_data": {}
          },
          {
              "name": "CARD_TRANSACTION_LIMIT",
              "status": "APPROVED",
              "reason": "LIMIT_APPROVED",
              "description": "Card transaction sufficient limit.",
              "additional_data": {}
          },
          {
              "name": "LEDGER",
              "status": "APPROVED",
              "reason": "LEDGER_APPROVED",
              "description": "Ledger validations approved.",
              "additional_data": {}
          },
          {
              "name": "RULES",
              "status": "APPROVED",
              "reason": "RULES_APPROVED",
              "description": "All rules successfully evaluated and approved.",
              "additional_data": {}
          },
          {
              "name": "ANTI_FRAUD",
              "status": "APPROVED",
              "reason": "ANTI_FRAUD_APPROVE",
              "description": "AntiFraud approved this authorization",
              "additional_data": {}
          },
          {
              "name": "PROGRAM_CONFIG",
              "status": "APPROVED",
              "reason": "PROGRAM_CONFIG_FOUND",
              "description": "Program found.",
              "additional_data": {}
          }
      ]
  }
  ```
</details>

# List of Rules

The following table lists all the rules the Pismo platform uses to validate transactions. Each rule links to a details page.

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        Rule
      </th>

      <th>
        Full balance
      </th>

      <th>
        Zero balance
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        [Account name inquiry (ANI)](https://developers.pismo.io/pismo-docs/docs/rule-list#account-number-inquiry-ani)
      </td>

      <td>
        X
      </td>

      <td>
        X\
        (Pismo forwards data via webhook\
        and issuer performs the validation)
      </td>
    </tr>

    <tr>
      <td>
        [Account type validation](https://developers.pismo.io/pismo-docs/docs/rule-list#account-type-validation)
      </td>

      <td>
        X
      </td>

      <td>
        X
      </td>
    </tr>

    <tr>
      <td>
        [Account status validation](https://developers.pismo.io/pismo-docs/docs/rule-list#account-status-validation)
      </td>

      <td>
        X
      </td>

      <td />
    </tr>

    <tr>
      <td>
        [Address Verification Service (AVS)](https://developers.pismo.io/pismo-docs/docs/rule-list#address-verification-service-avs)
      </td>

      <td>
        X
      </td>

      <td>
        X\
        (Pismo forwards data via webhook\
        and issuer performs the validation)
      </td>
    </tr>

    <tr>
      <td>
        [Anti-fraud validation](https://developers.pismo.io/pismo-docs/docs/rule-list#anti-fraud-validation)
      </td>

      <td>
        X
      </td>

      <td />
    </tr>

    <tr>
      <td>
        [ARQC validation](https://developers.pismo.io/pismo-docs/docs/rule-list#arqc-validation)
      </td>

      <td>
        X
      </td>

      <td>
        X
      </td>
    </tr>

    <tr>
      <td>
        [Authorization amounts calculation](https://developers.pismo.io/pismo-docs/docs/rule-list#authorization-amounts-calculation)
      </td>

      <td>
        X
      </td>

      <td />
    </tr>

    <tr>
      <td>
        [Available limits validation](https://developers.pismo.io/pismo-docs/docs/rule-list#available-limits-validation)
      </td>

      <td>
        X
      </td>

      <td />
    </tr>

    <tr>
      <td>
        [Card ATC validation](https://developers.pismo.io/pismo-docs/docs/rule-list#card-atc-validation)
      </td>

      <td>
        X
      </td>

      <td>
        X
      </td>
    </tr>

    <tr>
      <td>
        [Card inputted expiration date validation](https://developers.pismo.io/pismo-docs/docs/rule-list#card-inputted-expiration-date-validation)
      </td>

      <td>
        X
      </td>

      <td>
        X
      </td>
    </tr>

    <tr>
      <td>
        [Card expiration date validation](https://developers.pismo.io/pismo-docs/docs/rule-list#card-expiration-date-validation)
      </td>

      <td>
        X
      </td>

      <td>
        X
      </td>
    </tr>

    <tr>
      <td>
        [Card mode status validation](https://developers.pismo.io/pismo-docs/docs/rule-list#card-mode-status-validation)
      </td>

      <td>
        X
      </td>

      <td>
        X
      </td>
    </tr>

    <tr>
      <td>
        [Card mode validation](https://developers.pismo.io/pismo-docs/docs/rule-list#card-mode-validation)
      </td>

      <td>
        X
      </td>

      <td>
        X
      </td>
    </tr>

    <tr>
      <td>
        [Chip signature validation](https://developers.pismo.io/pismo-docs/docs/rule-list#chip-signature-validation)
      </td>

      <td>
        X
      </td>

      <td>
        X
      </td>
    </tr>

    <tr>
      <td>
        [Card status validation](https://developers.pismo.io/pismo-docs/docs/rule-list#card-status-validation)
      </td>

      <td>
        X
      </td>

      <td>
        X
      </td>
    </tr>

    <tr>
      <td>
        [Card valid until validation](https://developers.pismo.io/pismo-docs/docs/rule-list#card-valid-until-validation)
      </td>

      <td>
        X
      </td>

      <td>
        X
      </td>
    </tr>

    <tr>
      <td>
        [Chip values validation](https://developers.pismo.io/pismo-docs/docs/rule-list#chip-values-validation)
      </td>

      <td>
        X
      </td>

      <td>
        X
      </td>
    </tr>

    <tr>
      <td>
        [Contactless allowed validation](https://developers.pismo.io/pismo-docs/docs/rule-list#contactless-allowed-validation)
      </td>

      <td>
        X
      </td>

      <td>
        X
      </td>
    </tr>

    <tr>
      <td>
        [Currency validation](https://developers.pismo.io/pismo-docs/docs/rule-list#currency-validation)
      </td>

      <td>
        X
      </td>

      <td>
        X
      </td>
    </tr>

    <tr>
      <td>
        [CVM validation](https://developers.pismo.io/pismo-docs/docs/rule-list#cvm-validation)
      </td>

      <td>
        X
      </td>

      <td>
        X
      </td>
    </tr>

    <tr>
      <td>
        [Entry mode validation](https://developers.pismo.io/pismo-docs/docs/rule-list#entry-mode-validation)
      </td>

      <td>
        X
      </td>

      <td>
        X
      </td>
    </tr>

    <tr>
      <td>
        [Fetch account limit details](https://developers.pismo.io/pismo-docs/docs/rule-list#fetch-account-limit-details)
      </td>

      <td>
        X
      </td>

      <td />
    </tr>

    <tr>
      <td>
        [Fetch authorization configuration](https://developers.pismo.io/pismo-docs/docs/rule-list#fetch-authorization-configuration)
      </td>

      <td>
        X
      </td>

      <td>
        X
      </td>
    </tr>

    <tr>
      <td>
        [Fetch impact information](https://developers.pismo.io/pismo-docs/docs/rule-list#fetch-impact-imformation)
      </td>

      <td>
        X
      </td>

      <td />
    </tr>

    <tr>
      <td>
        [Flex controls validation](https://developers.pismo.io/pismo-docs/docs/rule-list#flex-controls-validation)
      </td>

      <td>
        X
      </td>

      <td>
        X\
        with limitations
      </td>
    </tr>

    <tr>
      <td>
        [Internal communication errors](https://developers.pismo.io/pismo-docs/docs/rule-list#internal-communication-errors)
      </td>

      <td>
        X
      </td>

      <td>
        X
      </td>
    </tr>

    <tr>
      <td>
        [Magnetic stripe validation](https://developers.pismo.io/pismo-docs/docs/rule-list#magnetic-stripe-validation)
      </td>

      <td>
        X
      </td>

      <td>
        X
      </td>
    </tr>

    <tr>
      <td>
        [Max transaction amount validation](https://developers.pismo.io/pismo-docs/docs/rule-list#max-transaction-amount-validation)
      </td>

      <td>
        X
      </td>

      <td />
    </tr>

    <tr>
      <td>
        [Max transactions validation for temporary cards](https://developers.pismo.io/pismo-docs/docs/rule-list#max-transactions-validation-for-temporary-cards)
      </td>

      <td>
        X
      </td>

      <td />
    </tr>

    <tr>
      <td>
        [Operation validation](https://developers.pismo.io/pismo-docs/docs/rule-list#operation-validation)
      </td>

      <td>
        X
      </td>

      <td />
    </tr>

    <tr>
      <td>
        [Password tries validation](https://developers.pismo.io/pismo-docs/docs/rule-list#password-tries-validation)
      </td>

      <td>
        X
      </td>

      <td>
        X
      </td>
    </tr>

    <tr>
      <td>
        [Processing code definition](https://developers.pismo.io/pismo-docs/docs/rule-list#processing-code-definition)
      </td>

      <td>
        X
      </td>

      <td>
        X
      </td>
    </tr>

    <tr>
      <td>
        [Purchase with installments and interest validation](https://developers.pismo.io/pismo-docs/docs/rule-list#purchase-with-installments-and-interest-validation)
      </td>

      <td>
        X
      </td>

      <td />
    </tr>

    <tr>
      <td>
        [Terminal capability validation](https://developers.pismo.io/pismo-docs/docs/rule-list#terminal-capability-validation)
      </td>

      <td>
        X
      </td>

      <td>
        X
      </td>
    </tr>

    <tr>
      <td>
        [Token status validation](https://developers.pismo.io/pismo-docs/docs/rule-list#token-status-validation)
      </td>

      <td>
        X
      </td>

      <td>
        X
      </td>
    </tr>

    <tr>
      <td>
        [Unexpected errors](https://developers.pismo.io/pismo-docs/docs/rule-list#unexpected-errors)
      </td>

      <td>
        X
      </td>

      <td>
        X
      </td>
    </tr>

    <tr>
      <td>
        [Valid card token validation](https://developers.pismo.io/pismo-docs/docs/rule-list#valid-card-token-validation)
      </td>

      <td>
        X
      </td>

      <td>
        X
      </td>
    </tr>

    <tr>
      <td>
        [Valid card validation](https://developers.pismo.io/pismo-docs/docs/rule-list#valid-card-validation)
      </td>

      <td>
        X
      </td>

      <td>
        X
      </td>
    </tr>
  </tbody>
</Table>
<!-- source:end -->

## Events

Event types linked from the source text (`api-reference-data/event_type_inventory.csv`):

| Event slug | Domain (inventory guess) | Version (inventory guess) | Event page | Emitting operations | Catalogue KU |
| --- | --- | --- | --- | --- | --- |
| `networktransactions-network-authorization-1` | networktransactions | 1 | https://developers.pismo.io/events/docs/networktransactions-network-authorization-1 | 2 | KU-EVT-catalogue-other-domains |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/card-issuing/authorization-validation-rules-for-card-network-operations.md`: updatedAt 2026-06-28T21:48:49.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- Source content contains MDX/HTML components (for example `<Table>`, `<HTMLBlock>`, `<Callout>`, `<details>`). They are preserved exactly as published; tables inside them were not converted to Markdown.
- The source links to 1 event page(s) under `/events/`. Event payload definitions are not part of the corpus (robots.txt disallows `/events/`), so payload fields are not documented here.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/card-issuing/authorization-validation-rules-for-card-network-operations.md` | whole document | https://developers.pismo.io/pismo-docs/docs/authorization-validation-rules-for-card-network-operations | `110b362325dc423d…` | 2026-06-28T21:48:49.000Z |

## Related knowledge units

- `KU-CARD-anti-fraud-integration` — Anti-fraud integration
- `KU-CARD-authorization-events` — Authorization events
- `KU-CARD-rule-list-part-01` — Rule list (part 1 of 4)
- `KU-CARD-rule-list-part-02` — Rule list (part 2 of 4)
- `KU-CARD-rule-list-part-03` — Rule list (part 3 of 4)
- `KU-CARD-rule-list-part-04` — Rule list (part 4 of 4)
- `KU-CARD-zero-balance-integration` — Zero balance integration and anti-fraud validations
- `KU-EVT-catalogue-other-domains` — Event catalogue: other event domains (accounting, authorization, availables, average, bulletin, cash, delinquent, fraud, instantpay, intl, ledger, networktransactions, onboarding, orgs, payment, platform, programs, rules, savings, statement)
