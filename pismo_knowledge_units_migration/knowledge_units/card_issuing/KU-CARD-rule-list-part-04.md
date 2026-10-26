---
ku_id: KU-CARD-rule-list-part-04
title: Rule list (part 4 of 4)
category: card_issuing
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/card-issuing/rule-list.md
  sha256: e0e226a5db7724ab4bcb3a3e34992c1a1065af81f0596a307936ea7b70c8dbdb
  url: https://developers.pismo.io/pismo-docs/docs/rule-list
  role: primary_guide
  updated_at: '2026-06-28T21:57:58.000Z'
operations: []
related_kus:
- KU-CARD-authorization-events
grouping_rationale: single source page; split into parts because the page is very large
---

# Rule list (part 4 of 4)

**KU ID:** `KU-CARD-rule-list-part-04` · **Category:** Card issuing · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) (one part of a large page) into one implementation-oriented unit. Grouping rationale: single source page; split into parts because the page is very large

Scope as stated in `docs/card-issuing/rule-list.md`:

> Third party endpoint declined the request.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/card-issuing/rule-list.md`: Unexpected errors; Internal communication errors; Fetch parameters

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/card-issuing/rule-list.md` lines 7006–7403 of the body

Source URL: https://developers.pismo.io/pismo-docs/docs/rule-list · updatedAt: 2026-06-28T21:57:58.000Z

<!-- source:begin path=docs/card-issuing/rule-list.md part=7005-7403 -->
      <td>
        Third party endpoint declined the request.
      </td>

      <td>
        PFT
      </td>

      <td>
        * *Visa:*\* 59
        * *Mastercard:*\* 63
        * *TecBan:*\* 57
        * *RuPay:*\* 63
        * *ELO:*\* 59
      </td>
    </tr>

    <tr>
      <td>
        ANTI\_FRAUD\_REFERRED
      </td>

      <td>
        REJECTED
      </td>

      <td>
        Third party endpoint declined the request and marked it as a referral.
      </td>

      <td>
        PFT
      </td>

      <td>
        * *Visa:*\* 59
        * *Mastercard:*\* 63
        * *TecBan:*\* 57
        * *RuPay:*\* 63
        * *ELO:*\* 59
      </td>
    </tr>

    <tr>
      <td>
        ANTI\_FRAUD\_OVERRIDE\_REFERRED
      </td>

      <td>
        REJECTED
      </td>

      <td>
        Third party endpoint declined the request, marked it as a referral, and overrode the Pismo platform's response code.
      </td>

      <td>
        PFT
      </td>

      <td>
        Response Code returned in the response of the endpoint call.
      </td>
    </tr>

    <tr>
      <td>
        ANTI\_FRAUD\_UNAVAILABLE
      </td>

      <td>
        REJECTED
      </td>

      <td>
        Call to third party endpoint failed, and the Pismo platform was not configured to approve by default when unavailable, so the request was declined.
      </td>

      <td>
        PFT
      </td>

      <td>
        * *Visa:*\* 59
        * *Mastercard:*\* 63
        * *TecBan:*\* 57
        * *RuPay:*\* 63
        * *ELO:*\* 59
      </td>
    </tr>
  </tbody>
</Table>

**Additional data:** Not yet mapped

**Payload example:**

```json
{
    "name": "ANTI_FRAUD",
    "status": "APPROVED",
    "reason": "ANTI_FRAUD_APPROVE",
    "description": "AntiFraud approved this authorization",
    "additional_data": {}
}
```

# Unexpected errors

Pismo Authorization platform performs all validations throughout the authorization flow. If anything breaks into the flow or any unexpected error happens that is not mapped on this list of validations and errors, an `UNKNOWN_ERROR` is thrown and the platform declines the request.

<Callout icon="📘" theme="info">
  This validation is performed for both zero balance and full balance integration.
</Callout>

**Name:** UNKNOWN\_ERROR

**Possible Statuses:** REJECTED

**Possible reasons:**

<Table align={["left","left","left","left","left"]}>
  <thead>
    <tr>
      <th>
        Reason
      </th>

      <th>
        Status
      </th>

      <th>
        Description
      </th>

      <th>
        Custom Code
      </th>

      <th>
        Response Code
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        UNKNOWN\_ERROR
      </td>

      <td>
        REJECTED
      </td>

      <td>
        Unexpected error occurred while processing authorization request.
      </td>

      <td>
        OP1
      </td>

      <td>
        * *Visa:*\* 05
        * *Mastercard:*\* 96
        * *TecBan:*\* 06
        * *RuPay:*\* 96
        * *ELO:*\* 05
      </td>
    </tr>
  </tbody>
</Table>

**Additional data:** `additional_data` will always contain the `custom_code` field since this validation is present only when an unexpected error occurs.

**Field:** `custom_code`

**Payload example:**

```json
{
    "name": "UNKNOWN_ERROR",
    "status": "REJECTED",
    "reason": "UNKNOWN_ERROR",
    "description": "An unexpected error occurred.",
    "additional_data": {
        "custom_code": "OP1"
    }
}
```

## Internal communication errors

Pismo Authorization platform consists of some APIs that together perform all the authorization request flow. If there is any communication error between those APIs before the Authorization system gets the message and build the validation result map, an error will be thrown and a denial response will be sent to the network. To identify these errors, you must look into the [Card Network Authorization Return](https://developers.pismo.io/pismo-docs/docs/authorization-events#card-network-authorization-return-event) event, that shows the exact message the Pismo Authorization platform sent to the network. The table below shows the Response Code and Custom Code used for those timeout errors. The table below list the response codes and custom codes used for these timeout errors.

<Table align={["left","left","left","left"]}>
  <thead>
    <tr>
      <th>
        Reason
      </th>

      <th>
        Description
      </th>

      <th>
        Custom Code
      </th>

      <th>
        Response Code
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Error while connecting to the Authorization System API
      </td>

      <td>
        Unexpected error occurred when sending request to authorization system.
      </td>

      <td>
        ACE
      </td>

      <td>
        * *Visa:*\* N0
        * *Mastercard:*\* 96
        * *Tecban:*\* 06
        * *Rupay:*\* 96
        * *ELO:*\* 96
      </td>
    </tr>

    <tr>
      <td>
        Error while connecting to the Distributor System API
      </td>

      <td>
        Unexpected error occurred when sending request to distributor system.
      </td>

      <td>
        DCE
      </td>

      <td>
        * *Visa:*\* N0
        * *Mastercard:*\* 96
        * *Tecban:*\* 06
        * *Rupay:*\* 96
        * *ELO:*\* -
      </td>
    </tr>
  </tbody>
</Table>

# Fetch parameters

To process the authorization flow, the platform fetches the parameters to use its configurations. If an error happens while fetching these details, the authorization request is declined.

<Callout icon="📘" theme="info">
  This validation is performed only for full balance integration.
</Callout>

**Name**: PARAMETER

**Possible Status**: APPROVED, REJECTED

**Possible Reasons**:

<Table align={["left","left","left","left","left"]}>
  <thead>
    <tr>
      <th>
        Reason
      </th>

      <th>
        Status
      </th>

      <th>
        Description
      </th>

      <th>
        Custom Code
      </th>

      <th>
        Response Code
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        PARAMETER\_FOUND
      </td>

      <td>
        APPROVED
      </td>

      <td>
        Parameters found.
      </td>

      <td>
        N/A
      </td>

      <td>
        00 (for all networks)
      </td>
    </tr>

    <tr>
      <td>
        PARAMETER\_GENERIC\_ERROR
      </td>

      <td>
        REJECTED
      </td>

      <td>
        An unexpected error has happened while fetching the parameters.
      </td>

      <td>
        PAE
      </td>

      <td>
        * *Visa:*\* N0
        * *Mastercard:*\* 96
        * *TecBan:*\* 06
        * *RuPay:*\* 96
        * *ELO*\*: 96
      </td>
    </tr>

    <tr>
      <td>
        PARAMETER\_TIMEOUT
      </td>

      <td>
        REJECTED
      </td>

      <td>
        A timeout occurred while fetching parameters.
      </td>

      <td>
        PAT
      </td>

      <td>
        * *Visa:*\* N0
        * *Mastercard:*\* 96
        * *TecBan:*\* 06
        * *RuPay:*\* 96
        * *ELO:*\* 96
      </td>
    </tr>
  </tbody>
</Table>

**Additional data:** `additional_data` contains the program ID. This field is only filled in for APPROVED and REJECTED status scenarios.

**Field:** `program_id`

**Payload example:**

```json
{
    "name": "PARAMETER",
    "status": "APPROVED",
    "reason": "PARAMETER_FOUND",
    "description": "Parameter by program found.",
    "additional_data": {
        "program_id": 1
    }
}
```
<!-- source:end -->

## Lifecycle status

- `docs/card-issuing/rule-list.md`: updatedAt 2026-06-28T21:57:58.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- Source content contains MDX/HTML components (for example `<Table>`, `<HTMLBlock>`, `<Callout>`, `<details>`). They are preserved exactly as published; tables inside them were not converted to Markdown.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/card-issuing/rule-list.md` | body lines 7006–7403 | https://developers.pismo.io/pismo-docs/docs/rule-list | `e0e226a5db7724ab…` | 2026-06-28T21:57:58.000Z |

## Related knowledge units

- `KU-CARD-authorization-events` — Authorization events
