---
ku_id: KU-PAY-check-posting-and-settlement
title: Check posting and settlement
category: transfers_and_payments
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/core-banking/check-posting-and-settlement.md
  sha256: fc2e2e9e68b5d286434e05f2d8262d1dfdcc71249bb491fa02fc137b414898fa
  url: https://developers.pismo.io/pismo-docs/docs/check-posting-and-settlement
  role: primary_guide
  updated_at: '2026-04-04T18:04:11.000Z'
operations:
- corporate-post-v1-checks
- post-corporate-v1-checks-checkId-cancel
- post-corporate-v1-checks-release
related_kus:
- KU-API-banking-transaction-banking--check-posting
- KU-BANK-account-balance-definitions-for-transaction-banking
- KU-EVT-catalogue-other-domains
grouping_rationale: single source page
---

# Check posting and settlement

**KU ID:** `KU-PAY-check-posting-and-settlement` · **Category:** Transfers and payments · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/core-banking/check-posting-and-settlement.md`:

> Checks are classified as cash‑in instruments and follow a processing and settlement model that differs significantly from real‑time electronic payments. While checks are still commonly issued and accepted in many markets, their clearing relies on an external clearing house that intermediates communication between the receiving and issuing banks.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/core-banking/check-posting-and-settlement.md`: Check posting and settlement; Check posting; Check settlement types; Example 1: `BEGINNING` with check settlement type `DEPOSIT`; Example 2: `END` with check settlement type `PENDING`; Example 3: `BEGINNING` with a combination of `DEPOSIT` and `HOLD`; Check release; Validation rules; Check release examples; Full check settlement; Specific check settlement; Check cancellation; Checks canceled successfully; Bank statements balance impacts; Examples; Checks with `settlement_type` set to `END`; Checks with `settlement_type` set to `BEGINNING`; Events

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 3 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/core-banking/check-posting-and-settlement.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/check-posting-and-settlement · updatedAt: 2026-04-04T18:04:11.000Z

<!-- source:begin path=docs/core-banking/check-posting-and-settlement.md part=0-end -->

# Check posting and settlement

Checks are classified as cash‑in instruments and follow a processing and settlement model that differs significantly from real‑time electronic payments. While checks are still commonly issued and accepted in many markets, their clearing relies on an external clearing house that intermediates communication between the receiving and issuing banks.

Pismo platform’s check‑handling and settlement capabilities combine API‑driven operations with file‑based bulk processing to support flexible and scalable check management. Individual check actions, such as posting, releasing, or canceling, are performed through dedicated APIs, while bulk operations are handled through a bulk‑settlement API endpoint that generates structured output files, and tracked through lifecycle events from creation to completion or failure. The same bulk-settlement endpoint also resolves all pending check operations for a specified division and date, providing consistent batch settlement that aligns with event‑based processing, generated file outputs, and overall operational workflows.

# Check posting

You can submit check deposits using the  [Create check posting](https://developers.pismo.io/pismo-docs/reference/corporate-post-v1-checks) endpoint and determine whether the funds are made available immediately or at a future date. This behavior is controlled by the `settlement_type` field that includes the following options.

| Settlement type | Description                                                                                                                                                                                                                              |
| --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `BEGINNING`     | This settlement type makes funds available immediately upon deposit. It also supports check posting to allow part or all of the deposited amount to be placed on hold.                                                                   |
| `END`           | Deposits made under this type do not include any operational holds. The entire value remains uncleared until the assigned settlement date, the funds become available only after the check is released, which requires a client request. |

## Check settlement types

You may also define whether the check amount is deposited in full or only partially, with any remaining value placed on hold until its corresponding settlement date. You can specify check settlement types using the `type` field of the `settlements` object. Refer to  [Create check posting](https://developers.pismo.io/pismo-docs/reference/corporate-post-v1-checks) for details.

| Check settlement type | Description                                                                                                         | Applicable check settlement type |
| --------------------- | ------------------------------------------------------------------------------------------------------------------- | :------------------------------- |
| `DEPOSIT`             | Specifies the amount to be deposited. This can be the full check value or a partial amount.                         | `BEGINNING`                      |
| `PENDING`             | Indicates the amount that is pending clearance and remains uncleared until its settlement date.                     | `END`                            |
| `HOLD`                | Represents the portion of the check amount placed on hold and kept unavailable until the scheduled settlement date. | `BEGINNING`                      |

<Callout icon="📘">
  **About `settlements.type`**

  * Only **one** `PENDING` is allowed when the `settlements.type` is `END`
  * Up to **three** `HOLD` are allowed when the  `settlements.type` is `BEGINNING`
  * Only **one** `DEPOSIT` is allowed when the `settlements.type` is `BEGINNING`
</Callout>

## Example 1: `BEGINNING` with check settlement type `DEPOSIT`

In this example, the client selects `BEGINNING` as the settlement type, which makes the funds available immediately. The check settlement type `DEPOSIT` indicates that this is an upfront deposit, and the full amount of $2,000 becomes available right away.

```json
{ 
  "check_id": "c462b2f3-55cc-42b4-ae9a-7614df3e8e72", 
  "check_amount": { 
    "value": 2000, 
    "currency": "USD" 
  }, 
  "description": "Check posting", 
  "settlement_type": "BEGINNING", 
  "business_date": "2025-01-04", 
  "settlements": [ 
    { 
      "type": "DEPOSIT", 
      "tracking_id": "73cc7fa5-79f1-4b85-9e13-124cc58c651f", 
      "settlement_date": "2025-01-04", 
      "amount": 2000 
    } 
  ] 
} 
```

## Example 2: `END` with check settlement type `PENDING`

In this case, the client selects `END` as the settlement type, meaning the funds remain unavailable until the scheduled settlement date—in this case, `2025-01-05`. `business_date` indicates when the transaction is recorded in the account’s balance‑history timeline.

Note that `business_date` is an optional field. If you do not specify a value, the Pismo platform defaults to `current_business_date`.

```json
{
  "check_id": "c462b2f3-55cc-42b4-ae9a-7614df3e8e73",
  "check_amount": {
    "value": 2000,
    "currency": "USD"
  },
  "description": "Check posting",
  "settlement_type": "END",
  "business_date": "2025-01-04",
  "settlements": [
    {
      "type": "PENDING",
      "tracking_id": "73cc7fa5-79f1-4b85-9e13-124cc58c651f",
      "settlement_date": "2025-01-05",
      "amount": 2000
    }
  ]
}
```

## Example 3: `BEGINNING` with a combination of `DEPOSIT` and `HOLD`

In this scenario, the client posts the check using the `BEGINNING` settlement type and chooses to make part of the amount available immediately while placing the remainder on hold. In the example, a `DEPOSIT` of `100` becomes available on `2025‑01‑05`, and three separate `HOLD` operations release `800`, `900`, and `200` on `2025‑01‑10`, `2025‑01‑20`, and `2025‑01‑30`, respectively.

```json
{
  "check_id": "c462b2f3-55cc-42b4-ae9a-7614df3e8e72",
  "check_amount": {
    "value": 2000,
    "currency": "USD"
  },
  "description": "Check posting",
  "settlement_type": "BEGINNING",
  "business_date": "2025-01-04",
  "settlements": [
    {
      "type": "DEPOSIT",
      "tracking_id": "73cc7fa5-79f1-4b85-9e13-124cc58c651f",
      "settlement_date": "2025-01-05",
      "amount": 100
    },
    {
      "type": "HOLD",
      "tracking_id": "9d7c898e-dd57-4ab4-bfe3-23a48d56851f",
      "settlement_date": "2025-01-10",
      "amount": 800
    },
    {
      "type": "HOLD",
      "tracking_id": "953109dc-e943-454a-95b6-4b15d2c5b31d",
      "settlement_date": "2025-01-20",
      "amount": 900
    },
    {
      "type": "HOLD",
      "tracking_id": "cd593acd-a056-42a1-aec8-3ae14d427a4d",
      "settlement_date": "2025-01-30",
      "amount": 200
    },
  ]
}
```

# Check release

The check release feature is designed to clear or release uncleared checks. It supports both full and partial releases.

## Validation rules

Checks must meet the following rules to be successfully settled. Refer to [Release check](https://developers.pismo.io/pismo-docs/reference/post-corporate-v1-checks-release) for details.

| Validation item                     | Rule                                                                                                                                                                              |
| ----------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Check existence                     | The check must already exist for the specified `check_id`.                                                                                                                        |
| Check status                        | The check status must be `UNSETTLED`, `UNCLEARED`, or `PARTIALLY_SETTLED`.                                                                                                        |
| Settlement status                   | The settlement status must be `UNSETTLED` or `RELEASE_FAILED`.                                                                                                                    |
| Account reason and operation blocks | There are no account status blocks or reason blocks. Note that accounts must be free of account status restrictions and must not be associated with any operational block.        |
| Tracking ID requires date           | When a `tracking_id` is passed, the request must also include a settlement date.                                                                                                  |
| No tracking ID on full release      | Requests without a settlement date, which represent a full release, cannot include a `tracking_id`. If you do not provide a `track_id`, the Pismo platform generates one for you. |
| Tracking ID uniqueness              | Your `tracking_id` must be unique and cannot already be in use.                                                                                                                   |
| Settlement date match               | The `settlement_date` provided must match the settlement date of an existing settlement, and only the settlement associated with that exact date is released.                     |

## Check release examples

### Full check settlement

You specify a `check_id` in the request without a `settlement_date`, the check is released and the fund is  moved from `check_holds` to `available`.

```json
{
   "check_id": "c462b2f3-55cc-42b4-ae9a-7614df3e8e72"
}
```

### Specific check settlement

If you want to clear only one of the checks you previously submitted, include both `settlement_date` and  `tracking_id` in your request so the transaction can be tracked. If you do not provide a `tracking_id`, the Pismo platform generates one automatically.

```json
{
   "check_id": "c462b2f3-55cc-42b4-ae9a-7614df3e8e72",
   "tracking_id": "1624db2e-ee81-4294-bc5e-c753b2cc5eb9",
   "settlement_date": "2025-06-30"
}
```

# Check cancellation

To cancel checks, you pass a `check_id` in the [Cancel check](https://developers.pismo.io/pismo-docs/reference/post-corporate-v1-checks-checkid-cancel) request.

<Callout icon="📘">
  **Notes**

  * You can only cancel unsettled or partially settled checks.
  * Checks that have been completely settled cannot be canceled.
</Callout>

### Checks canceled successfully

This is a sample response payload indicating a successful check cancellation. Note that only `check_id` is returned.

```json
{
   "check_id": "c462b2f3-55cc-42b4-ae9a-7614df3e8e72"
}
```

# Bank statements balance impacts

Three new balance types are introduced in relation to check posting.

| Balance type               | When it impacts the balance                                                       | Description                                                                                                                                                                                                                                                                                                                      |
| :------------------------- | :-------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `held_funds`               | When `settlement_type` is `BEGINNING`, and the `settlements.type` must be `HOLD`. | `held_funds` represents funds that are temporarily restricted due to regulatory or operational requirements. These funds are not available for transactions and reflect the total amount of balances that are earmarked or otherwise restricted. `held_funds` = `earmarked_balance` + `held_checks_balance` + `restricted_funds` |
| `uncleared_checks_balance` | When `settlement_type` is `END`                                                   | The uncleared check amount remains pending until the specified `settlement_date` to clear.                                                                                                                                                                                                                                       |
| `held_checks_balance`      | When `settlement_type` is `BEGINNING`                                             | The held check amount increases immediately. If the check is flagged as `HOLD` in `settlements.type`, its amount is added to the `held_checks_balance`.                                                                                                                                                                          |

## Examples

### Checks with `settlement_type` set to `END`

When you deposit a check of $1000 and specify `settlement_type` to `END`, the following balance impacts occur.

| Balance Type               | Change |
| -------------------------- | ------ |
| `uncleared_checks_balance` | +$1000 |
| `uncleared_funds`          | +$1000 |
| `ledger_balance`           | +$1000 |

This occurs because the uncleared amount updates both `uncleared_funds` and `ledger_balance`. The ledger balance reflects all funds, both cleared and uncleared.

When the check is settled, the available, book, and value‑dated balances increase, while the uncleared funds and uncleared check balance decrease.

### Checks with `settlement_type` set to `BEGINNING`

When you deposit a $1000 check with `settlement_type = BEGINNING` and one hold operation of $400 is applied, several balances update immediately. The held portion affects both ledger, held checks balance and held‑funds balances, while the deposit affects available and the total amount of the check impacts the book, value‑dated, and ledger balances. When the operation is later settled, the Pismo platform releases the held amount into the available balance and reverses the temporary hold entries, leaving other balances unchanged.

**Before settlement (post checks with a partial hold)**

| Balance type          | Change |
| --------------------- | ------ |
| `available_balance`   | +$600  |
| `held_checks_balance` | +$400  |
| `book_balance`        | +$1000 |
| `value_dated_balance` | +$1000 |
| `ledger_balance`      | +$1000 |
| `held_funds`          | +$400  |

**After settlement**

| Balance type          | Change    |
| --------------------- | --------- |
| `available_balance`   | +$400     |
| `held_checks_balance` | -$400     |
| `book_balance`        | no change |
| `value_dated_balance` | no change |
| `ledger_balance`      | no change |
| `held_funds`          | -$400     |

For more details, refer to [Account balance definitions for transaction banking](https://developers.pismo.io/pismo-docs/docs/account-balance-definitions-for-transaction-banking).

# Events

The following events are generated to indicate success/failure status of check settlements. For details, refer to the [check posting API](https://developers.pismo.io/pismo-docs/reference/corporate-post-v1-checks).

* [Platform authorization created](https://developers.pismo.io/events/docs/platform-authorization-platform-authorization-1)
* [Check posting status changed](https://developers.pismo.io/events/docs/cash-management-check-status-change-1)
* [Check settlement status changed](https://developers.pismo.io/events/docs/cash-management-check-settlement-status-change-1)
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `POST /corporate/v1/checks` | `corporate-post-v1-checks` | Create check posting | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--check-posting |
| `POST /corporate/v1/checks/release` | `post-corporate-v1-checks-release` | Release check | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--check-posting |
| `POST /corporate/v1/checks/{checkId}/cancel` | `post-corporate-v1-checks-checkId-cancel` | Cancel check | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--check-posting |

### Operation essentials

- **`POST /corporate/v1/checks`** (`corporate-post-v1-checks`): security `BearerAuth`; required parameters none declared; required body fields `check_id`, `check_amount`, `settlement_type`, `settlements`; response statuses 202, 400, 401, 403, 409, 500; error codes in examples `WCPT0001`, `WCPT0002`, `WCMN0002`, `WCPT0006`, `WCPT0007`, `WCPT0008`, `WCPT0010`, `WCPT0011`, `WCPT0004`, `WCPT0018`, `WCPT0009`, `WCPT0012`, `WCPT0014`, `WCPT0016`, `WCPT0017`, `WCAC0001`, `WCPT0005`, `WCPT0013`, `ECMN9999`; events `cash-management-check-status-change-1`, `platform-authorization-platform-authorization-1`.
- **`POST /corporate/v1/checks/release`** (`post-corporate-v1-checks-release`): security `BearerAuth`; required parameters none declared; required body fields `check_id`; response statuses 202, 400, 401, 403, 404, 409, 500; error codes in examples `WCPT0001`, `WCPT0002`, `WCPT0004`, `WCPT0018`, `WOBK0007`, `WCPT0011`, `WCPT0015`, `WCPT0003`, `WCPT0013`, `WCPT0019`, `ECMN9999`; events `cash-management-check-status-change-1`, `platform-authorization-platform-authorization-1`.
- **`POST /corporate/v1/checks/{checkId}/cancel`** (`post-corporate-v1-checks-checkId-cancel`): security `BearerAuth`; required parameters `checkId` (path); required body fields none declared; response statuses 202, 400, 401, 403, 404, 409, 500; error codes in examples `WCPT0002`, `WCPT0004`, `WCPT0018`, `WOBK0007`, `WCPT0011`, `WCPT0003`, `WCPT0013`, `WCPT0019`, `ECMN9999`; events `cash-management-check-status-change-1`, `platform-authorization-platform-authorization-1`.

## Events

Events emitted by the referenced operations (`api-reference-data/endpoint_event_map.csv`):

| Operation | Event slug |
| --- | --- |
| `corporate-post-v1-checks` | `cash-management-check-status-change-1` |
| `post-corporate-v1-checks-checkId-cancel` | `cash-management-check-status-change-1` |
| `post-corporate-v1-checks-release` | `cash-management-check-status-change-1` |
| `corporate-post-v1-checks` | `platform-authorization-platform-authorization-1` |
| `post-corporate-v1-checks-checkId-cancel` | `platform-authorization-platform-authorization-1` |
| `post-corporate-v1-checks-release` | `platform-authorization-platform-authorization-1` |

Event types linked from the source text (`api-reference-data/event_type_inventory.csv`):

| Event slug | Domain (inventory guess) | Version (inventory guess) | Event page | Emitting operations | Catalogue KU |
| --- | --- | --- | --- | --- | --- |
| `cash-management-check-status-change-1` | cash | 1 | https://developers.pismo.io/events/docs/cash-management-check-status-change-1 | 3 | KU-EVT-catalogue-other-domains |
| `platform-authorization-platform-authorization-1` | platform | 1 | https://developers.pismo.io/events/docs/platform-authorization-platform-authorization-1 | 32 | KU-EVT-catalogue-other-domains |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/core-banking/check-posting-and-settlement.md`: updatedAt 2026-04-04T18:04:11.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- The source links to 3 event page(s) under `/events/`. Event payload definitions are not part of the corpus (robots.txt disallows `/events/`), so payload fields are not documented here.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/core-banking/check-posting-and-settlement.md` | whole document | https://developers.pismo.io/pismo-docs/docs/check-posting-and-settlement | `fc2e2e9e68b5d286…` | 2026-04-04T18:04:11.000Z |

## Related knowledge units

- `KU-API-banking-transaction-banking--check-posting` — API reference: Banking - Transaction banking — Check posting
- `KU-BANK-account-balance-definitions-for-transaction-banking` — Account balance definitions for transaction banking
- `KU-EVT-catalogue-other-domains` — Event catalogue: other event domains (accounting, authorization, availables, average, bulletin, cash, delinquent, fraud, instantpay, intl, ledger, networktransactions, onboarding, orgs, payment, platform, programs, rules, savings, statement)
