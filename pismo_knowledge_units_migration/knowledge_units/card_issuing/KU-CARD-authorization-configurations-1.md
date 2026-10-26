---
ku_id: KU-CARD-authorization-configurations-1
title: Authorization configurations
category: card_issuing
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/card-issuing/authorization-configurations-1.md
  sha256: d6d32b9b48aacb05bdaa9730dbe052b0e308ab208d5a20130ce80dcab524e9d8
  url: https://developers.pismo.io/pismo-docs/docs/authorization-configurations-1
  role: primary_guide
  updated_at: '2026-04-24T17:33:43.000Z'
operations:
- post-authorization-config-by-tenant
related_kus:
- KU-API-card-issuing-authorization-configurations--authorization-configurations-part-01
- KU-CARD-run-the-configuration-requests
grouping_rationale: single source page
---

# Authorization configurations

**KU ID:** `KU-CARD-authorization-configurations-1` · **Category:** Card issuing · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/card-issuing/authorization-configurations-1.md`:

> The [Authorization configurations](https://developers.pismo.io/pismo-docs/reference/post-authorization-config-by-tenant) API can be used to register configurations at the org, program, and account levels. The authorization configuration is retrieved based on the hierarchy Account > Program > Org.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/card-issuing/authorization-configurations-1.md`: Authorization configurations

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 1 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/card-issuing/authorization-configurations-1.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/authorization-configurations-1 · updatedAt: 2026-04-24T17:33:43.000Z

<!-- source:begin path=docs/card-issuing/authorization-configurations-1.md part=0-end -->

# Authorization configurations

The [Authorization configurations](https://developers.pismo.io/pismo-docs/reference/post-authorization-config-by-tenant) API can be used to register configurations at the org, program, and account levels. The authorization configuration is retrieved based on the hierarchy Account > Program > Org.

If the configuration for the account is not found, the system looks for the configuration at the next higher level successively. If no configuration is found, the system continues with the standard Authorization flow.

Each of the endpoints and parameters are defined in the [Authorization configurations](https://developers.pismo.io/pismo-docs/reference/post-authorization-config-by-tenant) API documentation, but the following table allows you to easily determine which parameters are required for Full balance and which are required for Zero balance. An "X" indicates required.

<Table align={["left","left","left","left","left","left"]}>
  <thead>
    <tr>
      <th style={{ textAlign: "left" }}>
        Field
      </th>

      <th style={{ textAlign: "left" }}>
        Type
      </th>

      <th style={{ textAlign: "left" }}>
        Description
      </th>

      <th style={{ textAlign: "left" }}>
        Default

        value
      </th>

      <th style={{ textAlign: "left" }}>
        Full

        balance
      </th>

      <th style={{ textAlign: "left" }}>
        Zero

        balance
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td style={{ textAlign: "left" }}>
        `approve_anti_fraud_unavailable`
      </td>

      <td style={{ textAlign: "left" }}>
        boolean
      </td>

      <td style={{ textAlign: "left" }}>
        If set to `true` when anti-fraud is unavailable, the anti-fraud check is marked as APPROVED.\
        If set to `false`, it is marked as REJECTED.
      </td>

      <td style={{ textAlign: "left" }}>
        false
      </td>

      <td style={{ textAlign: "left" }}>
        X
      </td>

      <td style={{ textAlign: "left" }} />
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `should_use_anti_fraud_decision`
      </td>

      <td style={{ textAlign: "left" }}>
        boolean
      </td>

      <td style={{ textAlign: "left" }}>
        Flag indicates whether anti-fraud decisions should be used.
      </td>

      <td style={{ textAlign: "left" }}>
        false
      </td>

      <td style={{ textAlign: "left" }}>
        X
      </td>

      <td style={{ textAlign: "left" }} />
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `use_anti_fraud_response_code`
      </td>

      <td style={{ textAlign: "left" }}>
        boolean
      </td>

      <td style={{ textAlign: "left" }}>
        Flag indicates whether we should use the response code sent in anti-fraud.
      </td>

      <td style={{ textAlign: "left" }}>
        false
      </td>

      <td style={{ textAlign: "left" }}>
        X
      </td>

      <td style={{ textAlign: "left" }} />
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `use_rates_fee_models`
      </td>

      <td style={{ textAlign: "left" }}>
        boolean
      </td>

      <td style={{ textAlign: "left" }}>
        Flag indicates whether rate fee models should be used.
      </td>

      <td style={{ textAlign: "left" }}>
        false
      </td>

      <td style={{ textAlign: "left" }}>
        X
      </td>

      <td style={{ textAlign: "left" }} />
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `enabled_partial_authorization`
      </td>

      <td style={{ textAlign: "left" }}>
        boolean
      </td>

      <td style={{ textAlign: "left" }}>
        By default, authorizations don’t validate partial authorization, but if this property is enabled, it allows the platform to process partial authorizations for a given org/program/account.

        NOTE: This property also depends on the merchant, as it is necessary for the merchant to be able to partially authorize.
      </td>

      <td style={{ textAlign: "left" }}>
        false
      </td>

      <td style={{ textAlign: "left" }}>
        X
      </td>

      <td style={{ textAlign: "left" }}>
        X
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `disable_dcc`
      </td>

      <td style={{ textAlign: "left" }}>
        boolean
      </td>

      <td style={{ textAlign: "left" }}>
        This setting indicates whether or not the program allows dynamic currency conversion (DCC)  transactions.

        By default, every program allows DCC transactions. In case it's necessary to block this type of transaction, you must set the configuration to `true`.

        NOTE: A transaction is considered as DCC when:\
        -The merchant's country is different from the cardholder's country\
        -The currency used in the transaction is the same as the cardholder's.

        For example, for a card issued in Brazil, in BRL currency (986):\
        -A purchase in USD (840) in the US is not considered DCC\
        -A purchase in BRL (986) in the US is considered DCC
      </td>

      <td style={{ textAlign: "left" }}>
        false
      </td>

      <td style={{ textAlign: "left" }}>
        X
      </td>

      <td style={{ textAlign: "left" }}>
        X
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `deny_all_authorizations`
      </td>

      <td style={{ textAlign: "left" }}>
        boolean
      </td>

      <td style={{ textAlign: "left" }}>
        Flag indicates whether authorizations should be denied.

        This is useful for cases where a product is deprecated or during a migration process.
      </td>

      <td style={{ textAlign: "left" }}>
        false
      </td>

      <td style={{ textAlign: "left" }}>
        X
      </td>

      <td style={{ textAlign: "left" }} />
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `use_settlement_from_network`
      </td>

      <td style={{ textAlign: "left" }}>
        boolean
      </td>

      <td style={{ textAlign: "left" }}>
        By default, in clearing flow for international purchases, the authorizations use the same settlement amount of authorization (online flow).

        If you set this flag to `true`it means the system will use the settlement amount from the clearing message, which can be different from authorization.
      </td>

      <td style={{ textAlign: "left" }}>
        false
      </td>

      <td style={{ textAlign: "left" }}>
        X
      </td>

      <td style={{ textAlign: "left" }} />
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `call_anti_fraud_when_cancelling`
      </td>

      <td style={{ textAlign: "left" }}>
        boolean
      </td>

      <td style={{ textAlign: "left" }}>
        Flag indicates whether the anti-fraud API should be called during cancellation.
      </td>

      <td style={{ textAlign: "left" }}>
        false
      </td>

      <td style={{ textAlign: "left" }}>
        X
      </td>

      <td style={{ textAlign: "left" }} />
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `days_to_cancel_pre_authorization`
      </td>

      <td style={{ textAlign: "left" }}>
        integer
      </td>

      <td style={{ textAlign: "left" }}>
        Number of days to cancel pre-authorization.

        NOTE: the minimum number of days is `1` and the maximum is `60`.
      </td>

      <td style={{ textAlign: "left" }}>
        35
      </td>

      <td style={{ textAlign: "left" }}>
        X
      </td>

      <td style={{ textAlign: "left" }} />
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `days_to_cancel_authorization`
      </td>

      <td style={{ textAlign: "left" }}>
        integer
      </td>

      <td style={{ textAlign: "left" }}>
        Number of days to cancel authorization.

        NOTE: the minimum number of days is `1` and the maximum is `60`.
      </td>

      <td style={{ textAlign: "left" }}>
        10
      </td>

      <td style={{ textAlign: "left" }}>
        X
      </td>

      <td style={{ textAlign: "left" }} />
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `days_to_cancel_pre_authorization_migration`
      </td>

      <td style={{ textAlign: "left" }}>
        integer
      </td>

      <td style={{ textAlign: "left" }}>
        Number of days to cancel migrated pre-authorization.

        NOTE: the minimum number of days is `1` and the maximum is `60`.
      </td>

      <td style={{ textAlign: "left" }}>
        35
      </td>

      <td style={{ textAlign: "left" }}>
        X
      </td>

      <td style={{ textAlign: "left" }} />
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `days_to_cancel_authorization_migration`
      </td>

      <td style={{ textAlign: "left" }}>
        integer
      </td>

      <td style={{ textAlign: "left" }}>
        Number of days to cancel migrated pre-authorization.

        NOTE: the minimum number of days is `1` and the maximum is `60`.
      </td>

      <td style={{ textAlign: "left" }}>
        10
      </td>

      <td style={{ textAlign: "left" }}>
        X
      </td>

      <td style={{ textAlign: "left" }} />
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `zero_balance_url`
      </td>

      <td style={{ textAlign: "left" }}>
        string
      </td>

      <td style={{ textAlign: "left" }}>
        Indicates that it’s a Zero Balance flow, so the URL to call the customer’s service is informed.

        NOTE: This is only required for Zero balance.
      </td>

      <td style={{ textAlign: "left" }} />

      <td style={{ textAlign: "left" }} />

      <td style={{ textAlign: "left" }}>
        X
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `always_call_ledger_rules`
      </td>

      <td style={{ textAlign: "left" }}>
        boolean
      </td>

      <td style={{ textAlign: "left" }}>
        Flag indicates whether Ledger API and Rules API should be always called, even when the authorization has already been denied.

        NOTE: When this flag is enabled, instead of skipping the Ledger validation due to a previous rejected validation, it will call the Dry Run endpoint from Ledger.

        The Dry Run endpoint does not impact the account balance/limits. It performs the same validations from the standard endpoint and then return the simulated account balance if the account was impacted. These informations are sent to the client’s Anti-Fraud service, where they can perform their own validations using this data.

        For example, after validating the Dry Run results, the client can force approve the authorization via Anti-Fraud. This way, the account balance will be impacted after the Anti-Fraud response.
      </td>

      <td style={{ textAlign: "left" }}>
        false
      </td>

      <td style={{ textAlign: "left" }}>
        X
      </td>

      <td style={{ textAlign: "left" }} />
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        `override_bins`
      </td>

      <td style={{ textAlign: "left" }}>
        object
      </td>

      <td style={{ textAlign: "left" }}>
        This object may contain one or more of the above fields to be overridden individually at the BIN level, applying the default values ​​if absent.

        For an example with override bins, refer to [Run the configuration requests](https://developers.pismo.io/pismo-docs/docs/run-the-configuration-requests).

        NOTE: The BIN configuration currently only occurs for the `deny_all_authorizations` field.
      </td>

      <td style={{ textAlign: "left" }} />

      <td style={{ textAlign: "left" }}>
        X
      </td>

      <td style={{ textAlign: "left" }}>
        X
      </td>
    </tr>
  </tbody>
</Table>
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `POST /v1/config` | `post-authorization-config-by-tenant` | Create authorization configuration by organization | `api-specs/Card_issuing_-_Authorization_configurations.yaml` | no | KU-API-card-issuing-authorization-configurations--authorization-configurations-part-01 |

### Operation essentials

- **`POST /v1/config`** (`post-authorization-config-by-tenant`): security `BearerAuth`; required parameters none declared; required body fields none declared; response statuses 201, 400, 401, 403, 409, 500; error codes in examples none; events none listed.

## Lifecycle status

- `docs/card-issuing/authorization-configurations-1.md`: updatedAt 2026-04-24T17:33:43.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- Source content contains MDX/HTML components (for example `<Table>`, `<HTMLBlock>`, `<Callout>`, `<details>`). They are preserved exactly as published; tables inside them were not converted to Markdown.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/card-issuing/authorization-configurations-1.md` | whole document | https://developers.pismo.io/pismo-docs/docs/authorization-configurations-1 | `d6d32b9b48aacb05…` | 2026-04-24T17:33:43.000Z |

## Related knowledge units

- `KU-API-card-issuing-authorization-configurations--authorization-configurations-part-01` — API reference: Card issuing - Authorization configurations — Authorization configurations (part 1 of 2)
- `KU-CARD-run-the-configuration-requests` — Run the configuration requests
