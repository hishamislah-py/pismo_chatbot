---
ku_id: KU-CARD-clearing
title: 'Clearing: Base II and the clearing rules engine'
category: card_issuing
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/card-issuing/clearingbase.md
  sha256: 5934ea09c888b8cc2148157535f3f8df51bfca6baa044ffa9bde09808120a920
  url: https://developers.pismo.io/pismo-docs/docs/clearingbase
  role: primary_guide
  updated_at: '2026-08-03T20:20:53.000Z'
- path: docs/card-issuing/clearing-rules-engine.md
  sha256: e1d406f49298de651c27405320825ed1fd80cfaa8fe7de1bf38ef832a0a02131
  url: https://developers.pismo.io/pismo-docs/docs/clearing-rules-engine
  role: primary_guide
  updated_at: '2026-09-25T17:41:08.000Z'
operations:
- dlq-get-clearing-rules
- performClearingReconciliation
related_kus:
- KU-API-card-issuing-reconciliation--network-transactions-backoffice
- KU-API-pismo-clearing-rules-engine--clearing-rules
- KU-CARD-authorization-events
- KU-CARD-full-and-zero-balance-workflows
- KU-EVT-catalogue-other-domains
- KU-EVT-real-time-event-delivery
- KU-EVT-setting-up-event-file-delivery
grouping_rationale: Clearing processing and its rules engine.
---

# Clearing: Base II and the clearing rules engine

**KU ID:** `KU-CARD-clearing` · **Category:** Card issuing · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 2 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: Clearing processing and its rules engine.

Scope as stated in `docs/card-issuing/clearingbase.md`:

> Pismo processes two types of card network authorization messages:

Scope as stated in `docs/card-issuing/clearing-rules-engine.md`:

> The [Clearing rules engine API](https://developers.pismo.io/pismo-docs/reference/dlq-get-clearing-rules) provides Pismo clients with a set of external endpoints that allow you to configure which clearing events should be automatically processed by the Pismo platform and which should be routed to the dead letter queue (DLQ). The DLQ is the queue for all pending transactions waiting to be cleared.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/card-issuing/clearingbase.md`: Clearing/Base II; Clearing/Base II workflow; Consolidated file and events; Consolidated file; Events; Dual-message scenarios; Original authorization not found; Debit clearing adjustment; Credit clearing adjustment; Original authorization found; Confirmation messages; Pending purchase confirmation; Purchase confirmation of an already confirmed purchase; Confirmation for a canceled purchase; Cancellation messages; Cancellation of a pending/confirmed authorization; Partial cancellation of an authorization; Installment purchases; International purchases
- `docs/card-issuing/clearing-rules-engine.md`: Clearing rules engine; Clearing rules engine API endpoints

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 2 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/card-issuing/clearingbase.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/clearingbase · updatedAt: 2026-08-03T20:20:53.000Z

<!-- source:begin path=docs/card-issuing/clearingbase.md part=0-end -->

# Clearing/Base II

Pismo processes two types of card network authorization messages:

**Single-message system (SMS)** transactions:

* **Online/authorization**  - Message that contains all the data necessary to authorize and settle the transaction. Since there's no need for additional reconciliation, the platform generates the transaction and financially clears it at the time of initial online authorization.

**Dual-message system (DMS)** transactions -  two messages are necessary to settle the authorization:

1. **Online/authorization**  - Message that contains initial information required for an issuer authorization decision.
2. **Offline/clearing/base II** - Message that confirms the first message. The second message is sent later. It contains the additional data the issuer requires to clear and settle the transaction.

In a dual-message scenario, the authorization impacts the account balance immediately. However, the transaction records are generated only after confirmation.

<Callout icon="📘" theme="info">
  It is possible that only the offline/clearing message is received. If the Pismo platform receives a confirmation message from the acquirer that doesn’t link with any authorization record, the platform creates a new authorization record in the account for that message.
</Callout>

# Clearing/Base II workflow

The Clearing/Base II reconciliation process is a central part of the card network authorizations workflow. The reconciliation is responsible for confirming a transaction and posting it to the account. Once the platform confirms an authorization, it triggers other flows within the platform, such as invoice and accounting postings.

The Pismo platform connects to the card network to check if any files are available for processing.

* **Mastercard** - Pismo processes the settlement files every two hours.
* **Visa** - Pismo processes the settlement files once a day.
* **ELO** - Pismo processes the settlement files once a day.

When a settlement file is available, Pismo:

* Downloads it from the card network
* Parses each message within the file, removes any sensitive data
* Issues a raw event for each authorization inside the settlement file.  The event includes data from the message that is consumed by the impacted APIs. The platform uses this data to process the confirmation or cancellation of the transaction within the [authorizations workflow](https://developers.pismo.io/pismo-docs/docs/full-and-zero-balance-workflows).

> 📘 Clearing reconciliation
>
> If a problem is encountered during the clearing process for Clearing/Base II authorization events, a report is sent from the Dead Letter Queue (DLQ) stating that the unprocessed clearing message needs to be reconciled. All messages that are sent to the DLQ can be reconciled and reprocessed through the [clearing-reconciliation](https://developers.pismo.io/pismo-docs/reference/performclearingreconciliation) endpoint.
>
> This endpoint allows you to take over the reprocessing of messages in the DLQ, assuming the responsibility to reconcile unprocessed clearing message sent to DLQ. All messages that have been sent to the DLQ can be reconciled through this endpoint.
>
> NOTE: This endpoint is available only for Visa and Mastercard and is not available for ELO.
>
> Once common scenario for this would be a Cancellation/Confirmation/Installment with a Julian date error.
>
> * Issue—This issue occurs when Pismo receives a Base II / Clearing that contains a Julian date smaller than the last one processed.
> * Action—Adjust Julian Date field and perform the reconciliation. Note that the field that represents the Julian Date varies according to the card brand.
> * Example:
>
>   ```
>   curl --location '[valid-test-environment-url]' \
>   --header 'x-tenant: [tenant]' \
>   --header 'x-cid: [valid-uuid-correlation-id]' \
>   --header 'Content-Type: application/json' \
>   --data '{
>     "card_network": "[network name]",
>     "card_hash": "[card-hash]",
>     "reconciliation_reason": "INVALID_JULIAN_DATE",
>     "adjustments": [
>       {
>         "field": "julianProcessingDate",     
>         "new_value": "5040"
>       }
>      ]
>   }'
>   ```

# Consolidated file and events

Pismo receives a clearing file from the network from which we will produce clearing events (refer to [Clearing/Base II events ](https://developers.pismo.io/pismo-docs/docs/authorization-events#clearingbase-ii-events) in the Authorization events guide for details). In a zero balance product, Issuers are expected to use this event to match against an authorization request received and follow the reconciliation process as necessary.

> 📘 Settlement files are delivered through clearing events.
>
> All settlement-related information is delivered through clearing events. There are no actual *settlement events*.

## Consolidated file

Pismo receives a consolidated settlement file which aggregates all transactions and informs the issuer of balances that need to be settled for a particular clearing cycle. This settlement file is a summary report and is not broken down into events. These files are transferred as-is via the [file flow](https://developers.pismo.io/pismo-docs/docs/setting-up-event-file-delivery).

* For Mastercard, this is the `T140` file, and is available at: `s3://pismo-dataplatform-tn-{your_org_id}/reports/clearing/t140/year=YYYY/month=MM/day=DD/`
* For Visa, this is the `EP747` file that contains the VSS reports. There are multiple files within the EP747 file, which are transferred via the file flow, and are available at: `s3://pismo-dataplatform-tn-{your_org_id}/reports/clearing/ep747/year=YYYY/month=MM/day=DD/`
* For ELO, this is the `AGEMIS` file, and is available at: `s3://pismo-dataplatform-tn-{your_org_id}/reports/clearing/agemis/year=YYYY/month=MM/day=DD/`

## Events

The Pismo platform streams each line of the settlement file in JSON format messages via [real-time event notifications](https://developers.pismo.io/pismo-docs/docs/setting-up-real-time-event-delivery). For instance, if the file contains five purchases and three second presentments, eight events are sent. All generated messages are sent to you through clearing events (such as raw\_credit\_visa, raw\_credit\_mastercard, or raw\_debit\_mastercard) and other generated events related to authorization, transactions, and impacts on the limit/balance of the account. Note that all settlement-related information is delivered through clearing events. There are no direct settlement events.

For more information on the events, see [authorization events](https://developers.pismo.io/pismo-docs/docs/authorization-events).

<Callout icon="📘" theme="info">
  The events do not contain any totals; only consolidated files do.

  JSON messages:

  * Do not contain sensitive data.
  * Follow the field structure that the card network makes available in its manuals.
  * Only contain the `cardHash` of the card as the cardholder identifier.
</Callout>

<Callout icon="🚧" theme="warn">
  * If an issuer transaction is present in the database but is missing in the clearing file after 10 days, it must be **canceled**.
  * If a transaction is missing in the issuer database but is present in the clearing file, then it must be **cleared**.
  * If confirmation comes after cancellation, the authorization can be reopened.
  * If a cancellation message is received and the purchase is open, an authorization is canceled.
</Callout>

# Dual-message scenarios

In a dual-message scenario, the platform performs the reconciliation between the authorization and the clearing/base II message at the time of clearing/base II. At that time, in addition to the transaction generation, there may be changes in authorization values.

To start processing the message, the Pismo authorization platform needs to identify the corresponding original authorization for this message. To do so, the platform compares and verifies message data, such as authorization code and retrieval reference number. After this verification, the original authorization may or may not be identified. For each scenario, the processing is different.

# Original authorization not found

The platform accepts every message received from clearing/base II. Therefore, when an authorization is not linked to the received message, a new authorization is posted to the account. There can be two scenarios in this case: debit clearing adjustment and credit clearing adjustment.

## Debit clearing adjustment

In the debit clearing adjustment, when the Pismo platform receives a confirmation message and this message is not linked to any original authorization, the platform creates a new authorization, and posts debit into the account, decreasing the account balance. Since this is the process of clearing/base II, the transaction is accepted and posted without any additional validations on the card or the account.

There are cases where the Pismo platform receives the debit amount and the transaction has not been confirmed. In these situations, the customer should contact the acquirer.

## Credit clearing adjustment

In the credit clearing adjustment, when the Pismo platform receives a cancellation/credit message and this message is not linked to any original authorization, the platform creates a new authorization, and posts credit into the account, increasing the account balance.

Adhering to the process of clearing/base II, the transaction is accepted and posted without any additional validation on the card or account. There are cases where the Pismo platform receives the credit amount and the transaction has not been confirmed. In these situations, the customer should contact the acquirer.

# Original authorization found

When the original authorization is found, the Pismo platform performs verification whether to perform reconciliation from the received message. The platform doesn't process the clearing/base II messages in the following scenarios.

* Second presentments messages, where there is an open dispute about the purchase.
* Confirmations of split authorizations, where the message is for an installment other than the first.
* The message is earlier than the last clearing/base II recorded for that authorization. This can happen in a reprocessing scenario for old messages.
* Purchase confirmation that was canceled by the clearing/base II on the same day. In this scenario, the cancellation takes precedence.
* Cancellation of an already canceled purchase.
* Partial cancellation of a pending purchase. In this scenario, the message goes back to the queue to wait for the purchase to be confirmed.

Once the platform determines that the message should be processed, it processes the message and performs the reconciliation. The following shows reconciliation scenarios for confirmation and cancellation messages.

## Confirmation messages

### Pending purchase confirmation

This is the most common reconciliation scenario, where the clearing/base II message confirms a pending purchase. In this scenario, the platform accepts the amount received in the reconciliation message. If there is a difference in the value calculated by the online authorization, the platform reflects this difference on the account as debit or credit. The platform posts the transaction in the amount received in clearing/base II.

Examples:

* *Scenario: Authorization is $100, and clearing/base II confirms $100.*\
  In this scenario, the platform confirms the authorization and there is no additional impact on the account. The platform generates a $100 transaction.
* *Scenario: Authorization is $100, and clearing/base II confirms $90.*\
  In this scenario, the platform updates the authorization to $90, posts a $10 credit to the account, and generates a $90 transaction.
* *Scenario: Authorization is $100, and clearing/base II confirms $110.*\
  In this scenario, the platform updates the authorization to $110, posts a $10 debit to the account, and generates a $110 transaction.

### Purchase confirmation of an already confirmed purchase

It is possible to receive a new confirmation message for a purchase that has been confirmed already. In this scenario, the second confirmation message is summed up with the first one. The platform reflects the new amount on the account and generates a new transaction in the value of the second confirmation message.

Example:

* *Scenario: Authorization is $100, the first clearing/base II message confirms $60, and then the second clearing/base II confirms $40.*\
  In this scenario, with the first confirmation message, the platform updates the authorization to $60, posts a $40 credit to the account, and generates a $60 transaction. With the second confirmation message, the platform updates the authorization to $100, posts a $40 debit to the account, and generates a $40 transaction.

### Confirmation for a canceled purchase

When a purchase has been canceled already and the platform receives a confirmation message for this purchase, the platform reopens the purchase, posts the corresponding amount to the account, and generates a new purchase transaction in the amount of the confirmation message.

Examples:

* *Scenario: Authorization of $100 is canceled, but then the platform receives a confirmation reopening the purchase in the same amount.*\
  In this scenario, the platform reopens the authorization, changes its status from canceled to confirmed, posts a $100 debit to the account, and generates a new $100 transaction.
* *Scenario: Authorization of $100 is canceled, but then the platform receives a confirmation reopening the purchase with another amount, $90.*\
  In this scenario, the platform reopens the authorization, changes its status from canceled to confirmed, updates its value to $90, posts a $90 debit to the account, and generates a new $90 transaction.

<Callout icon="📘" theme="info">
  If the platform receives a confirmation for a previously denied purchase, the platform accepts the reconciliation. The logic follows the same pattern as in the confirmation of a canceled purchase scenario.
</Callout>

## Cancellation messages

### Cancellation of a pending/confirmed authorization

In this most common cancellation scenario, the platform receives a cancellation message for an open pending or confirmed purchase. The platform cancels the purchase and posts credit in the total purchase amount to the account. For the previously confirmed purchase, the platform posts a cancellation transaction. For pending purchases, as there was no previous confirmation, the platform doesn't post any transactions.

Examples:

* *Scenario: Cancellation of an already confirmed $100 authorization.*\
  In this scenario, the platform cancels the authorization, posts a $100 credit to the account, and generates a $100 cancellation transaction.
* *Scenario: Cancellation of a pending $100 authorization.*\
  In this scenario, the platform cancels the authorization and posts a $100 credit to the account. The platform does not generate any transactions.

### Partial cancellation of an authorization

This scenario occurs when the platform receives a cancellation message with a value lower than the total purchase amount. In this scenario, the platform keeps the purchase open, issues credit in the cancellation amount to the account, and generates the cancellation transaction.

Examples:

* *Scenario: Authorization of $100 with the cancellation of $50.*\
  In this scenario, the platform keeps the authorization open, issues a $50 credit to the account, and generates a $50 credit transaction.
* *Scenario: Authorization of $100 with two cancellations of $50.*\
  In this scenario,  the platform keeps the authorization open, issues two credits in the amount of $50, and generates two $50 credit transactions.

## Installment purchases

The installment purchases follow the same rules as the previous scenarios, with the only difference being that transactions are generated for all installments. In the case of total cancellation, the platform generates cancellation transactions for all installments. In the case of partial cancellation, the platform generates credit the same way as for a cash purchase, with no impact on the generated installment transactions.

## International purchases

International purchases have the purchase amount calculated for the cardholder's currency using the exchange rate of the day of online authorization. For example, if a purchase was made on the 1st of the month and the clearing message arrived on the 10th, the platform uses the conversion rate from the 1st of the month.

International purchases also follow the same rules as the previously described scenarios. In the case of partial cancellation, the platform generates credit the same way as with the local purchase, only considering the credit amount converted to local currency.

The Pismo platform supports any sequence of processing. It is possible to have scenarios such as:

*Authorization > Confirmation > Cancellation > Confirmation with a new value\
Authorization > Confirmation > Cancellation > Confirmation with a new value > Partial cancellation*

Authorization, confirmation, cancelation, and partial cancelation can happen in any plausible order, as long as it is taken into consideration that the platform does not process the clearing/base II messages in certain scenarios, as described at the beginning of [this section](https://developers.pismo.io/pismo-docs/docs/clearingbase#original-authorization-found).
<!-- source:end -->

### Source 2: `docs/card-issuing/clearing-rules-engine.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/clearing-rules-engine · updatedAt: 2026-09-25T17:41:08.000Z

<!-- source:begin path=docs/card-issuing/clearing-rules-engine.md part=0-end -->

# Clearing rules engine

The [Clearing rules engine API](https://developers.pismo.io/pismo-docs/reference/dlq-get-clearing-rules) provides Pismo clients with a set of external endpoints that allow you to configure which clearing events should be automatically processed by the Pismo platform and which should be routed to the dead letter queue (DLQ). The DLQ is the queue for all pending transactions waiting to be cleared.

With this functionality, you gain more autonomy over exception handling, reduce operational effort required for manual analysis, and increase predictability around what is delivered to the issuer. The Clearing rules engine API offers control and flexibility while managing clearing rules configurations.

The DLQ currently includes the following routing reasons, which may or may not be configurable through the rules engine.

| Routing reason                           | Configurable?                |
| :--------------------------------------- | :--------------------------- |
| `NOT_REFUNDABLE_AUTHORIZATION`           | Configurable (TRUE or FALSE) |
| `NOT_PERMITTED_OPERATION`                | Configurable (TRUE or FALSE) |
| `ACCEPTANCE_NOT_FOUND`                   | Not configurable             |
| `DIFFERENT_PROCESSING_CODE`              | Configurable (TRUE or FALSE) |
| `CLEARING_WITH_ZERO_AMOUNT`              | Configurable (TRUE or FALSE) |
| `INVALID_CARD_MODE`                      | Configurable (TRUE or FALSE) |
| `INVALID_ACCOUNT_STATUS`                 | Configurable (TRUE or FALSE) |
| `MCC_AMOUNT_EXCEEDS_AUTHORIZATION`       | Configurable (TRUE or FALSE) |
| `MCC_AUTHORIZATION_NOT_FOUND`            | Configurable (List of MCC)   |
| `CARD_NOT_FOUND`                         | Configurable (TRUE or FALSE) |
| `INVALID_JULIAN_DATE`                    | Configurable (TRUE or FALSE) |
| `CANCELLATION_AMOUNT_EXCEEDS_AUTHORIZED` | Not configurable             |
| `INVALID_SEMANTIC_CANCELLATION`          | Not configurable             |
| `CONCILIATION_DEADLINE`                  | Configurable (integer)       |
| `INSTALLMENT_PLAN_VERIFICATION`          | Configurable (TRUE or FALSE) |
| `CARD_REGION_RESTRICTION`                | Configurable (TRUE or FALSE) |

Use the [Pending transactions sent](https://developers.pismo.io/events/docs/networktransactions-pending-transactions-2) event to check Rules engine transactions routed to the DLQ. After receiving these transactions, the issuer can use the [Perform clearing reconciliation](https://developers.pismo.io/pismo-docs/reference/performclearingreconciliation) endpoint to request reprocessing.

## Clearing rules engine API endpoints

The Clearing rules engine API provides endpoints to:

* Create and update DLQ rules
* Retrieve the active configuration

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Endpoint
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Update clearing rules engine\
        `PUT /v1/rules`
      </td>

      <td>
        Use this endpoint to create or update the active DLQ rules configuration for a given scope (Org or Program). With it, you can:

        * Configure the rule.
        * Generate the immutable versioned rule set.
        * Update the pointer to the latest version.
        * Return the new version and checksum.
      </td>
    </tr>

    <tr>
      <td>
        Get latest clearing rules configuration `GET /v1/rules`
      </td>

      <td>
        This endpoint returns the latest active configuration for the requested scope (Org or Program), including version metadata.
      </td>
    </tr>
  </tbody>
</Table>

<br />
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `POST /v1/clearing-reconciliation` | `performClearingReconciliation` | Perform clearing reconciliation | `api-specs/Card_issuing_-_Reconciliation.yaml` | no | KU-API-card-issuing-reconciliation--network-transactions-backoffice |
| `GET /v1/rules` | `dlq-get-clearing-rules` | Get latest clearing rules configuration | `api-specs/Pismo_clearing_rules_engine.yaml` | no | KU-API-pismo-clearing-rules-engine--clearing-rules |

### Operation essentials

- **`POST /v1/clearing-reconciliation`** (`performClearingReconciliation`): security `BearerAuth`; required parameters none declared; required body fields `card_network`, `card_hash`, `reconciliation_reason`; response statuses 202, 400, 401, 403, 404, 500; error codes in examples none; events none listed.
- **`GET /v1/rules`** (`dlq-get-clearing-rules`): security `BearerAuth`; required parameters `orgId` (query); required body fields none declared; response statuses 200, 400, 403, 404, 500; error codes in examples none; events none listed.

## Events

Event types linked from the source text (`api-reference-data/event_type_inventory.csv`):

| Event slug | Domain (inventory guess) | Version (inventory guess) | Event page | Emitting operations | Catalogue KU |
| --- | --- | --- | --- | --- | --- |
| `networktransactions-pending-transactions-2` | networktransactions | 2 | https://developers.pismo.io/events/docs/networktransactions-pending-transactions-2 | 1 | KU-EVT-catalogue-other-domains |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/card-issuing/clearingbase.md`: updatedAt 2026-08-03T20:20:53.000Z.
- `docs/card-issuing/clearing-rules-engine.md`: updatedAt 2026-09-25T17:41:08.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- Source content contains MDX/HTML components (for example `<Table>`, `<HTMLBlock>`, `<Callout>`, `<details>`). They are preserved exactly as published; tables inside them were not converted to Markdown.
- The source links to 1 event page(s) under `/events/`. Event payload definitions are not part of the corpus (robots.txt disallows `/events/`), so payload fields are not documented here.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/card-issuing/clearingbase.md` | whole document | https://developers.pismo.io/pismo-docs/docs/clearingbase | `5934ea09c888b8cc…` | 2026-08-03T20:20:53.000Z |
| `docs/card-issuing/clearing-rules-engine.md` | whole document | https://developers.pismo.io/pismo-docs/docs/clearing-rules-engine | `e1d406f49298de65…` | 2026-09-25T17:41:08.000Z |

## Related knowledge units

- `KU-API-card-issuing-reconciliation--network-transactions-backoffice` — API reference: Card issuing - Reconciliation — Network transactions backoffice
- `KU-API-pismo-clearing-rules-engine--clearing-rules` — API reference: Pismo clearing rules engine — Clearing rules
- `KU-CARD-authorization-events` — Authorization events
- `KU-CARD-full-and-zero-balance-workflows` — Full and Zero balance transaction workflows
- `KU-EVT-catalogue-other-domains` — Event catalogue: other event domains (accounting, authorization, availables, average, bulletin, cash, delinquent, fraud, instantpay, intl, ledger, networktransactions, onboarding, orgs, payment, platform, programs, rules, savings, statement)
- `KU-EVT-real-time-event-delivery` — Real-time event delivery: setup, additional subscribers and event filtering
- `KU-EVT-setting-up-event-file-delivery` — Setting up event batch file delivery
