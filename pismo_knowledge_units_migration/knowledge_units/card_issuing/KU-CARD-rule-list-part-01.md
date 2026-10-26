---
ku_id: KU-CARD-rule-list-part-01
title: Rule list (part 1 of 4)
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
- KU-CARD-authorization-validation-rules-for-card-network-operations
grouping_rationale: single source page; split into parts because the page is very large
---

# Rule list (part 1 of 4)

**KU ID:** `KU-CARD-rule-list-part-01` · **Category:** Card issuing · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) (one part of a large page) into one implementation-oriented unit. Grouping rationale: single source page; split into parts because the page is very large

Scope as stated in `docs/card-issuing/rule-list.md`:

> The rules used by the Pismo platform to validate transactions are listed below. Refer to [Authorization validation rules for card network operations](https://developers.pismo.io/pismo-docs/docs/authorization-validation-rules-for-card-network-operations) for general information about how to receive and interpret validation results.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/card-issuing/rule-list.md`: Rule list; Magnetic stripe validation; Account number inquiry (ANI); Issuer verification option (`account_Name_Request = "I"`)

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/card-issuing/rule-list.md` lines 1–275 of the body

Source URL: https://developers.pismo.io/pismo-docs/docs/rule-list · updatedAt: 2026-06-28T21:57:58.000Z

<!-- source:begin path=docs/card-issuing/rule-list.md part=0-275 -->

# Rule list

The rules used by the Pismo platform to validate transactions are listed below. Refer to [Authorization validation rules for card network operations](https://developers.pismo.io/pismo-docs/docs/authorization-validation-rules-for-card-network-operations) for general information about how to receive and interpret validation results.

# Magnetic stripe validation

The Pismo platform checks that the country where the authorization is taking place allows the entry mode to be **Magnetic Stripe**. If an authorization request is performed in a country where Magnetic Stripe is not allowed, the authorization is denied by default.

<Callout icon="📘" theme="info">
  This validation is performed for both zero balance and full balance integration.
</Callout>

<NotApplicable />

**Name:** MAGNETIC\_STRIPE

**Possible statuses:** APPROVED, SKIPPED, REJECTED

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
        MAGNETIC\_STRIPE\_VALID
      </td>

      <td>
        APPROVED
      </td>

      <td>
        Magnetic Stripe present and validated.
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
        DEBIT\_ECOMMERCE\_TRANSACTION
      </td>

      <td>
        SKIPPED
      </td>

      <td>
        E-commerce debit transactions might have a Magnetic Stripe built-in by the network. Validation is skipped in this scenario.
      </td>

      <td>
        N/A
      </td>

      <td>
        N/A
      </td>
    </tr>

    <tr>
      <td>
        NO\_MAGNETIC\_STRIPE
      </td>

      <td>
        SKIPPED
      </td>

      <td>
        No Magnet Stripe in the request, so no need for this validation.
      </td>

      <td>
        N/A
      </td>

      <td>
        N/A
      </td>
    </tr>

    <tr>
      <td>
        NO\_MAGNETIC\_STRIPE\_WITH\_CRYPTOGRAM
      </td>

      <td>
        SKIPPED
      </td>

      <td>
        Request contains cryptogram information, so no need for this validation.
      </td>

      <td>
        N/A
      </td>

      <td>
        N/A
      </td>
    </tr>

    <tr>
      <td>
        NO\_MAGNETIC\_STRIPE\_WITH\_VALID\_CVV2
      </td>

      <td>
        SKIPPED
      </td>

      <td>
        Request contains CVV2 information, so no need for this validation.
      </td>

      <td>
        N/A
      </td>

      <td>
        N/A
      </td>
    </tr>

    <tr>
      <td>
        TOKENIZED\_TRANSACTION
      </td>

      <td>
        SKIPPED
      </td>

      <td>
        Request is tokenized, so no need for this validation. (Visa only)
      </td>

      <td>
        N/A
      </td>

      <td>
        N/A
      </td>
    </tr>

    <tr>
      <td>
        COUNTRY\_NOT\_ALLOW\_MAGNETIC\_STRIPE
      </td>

      <td>
        REJECTED
      </td>

      <td>
        Country doesn’t allow Magnetic Stripe operations, so the authorization request is denied.
      </td>

      <td>
        FR5
      </td>

      <td>
        * *Visa:*\* 5C
        * *Mastercard:*\* 57
        * *TecBan:*\* R9
        * *RuPay:*\* 57
        * *ELO:*\* 57
      </td>
    </tr>

    <tr>
      <td />

      <td />

      <td />

      <td />

      <td />
    </tr>
  </tbody>
</Table>

**Additional data:** Not yet mapped

**Payload example:**

```json
{
    "name": "MAGNETIC_STRIPE",
    "status": "APPROVED",
    "reason": "MAGNETIC_STRIPE_VALID",
    "description": "Magnetic stripe valid",
    "additional_data": {}
}
```

# Account number inquiry (ANI)

Account number inquiry (ANI) is a fraud prevention tool implemented by the networks, issuers, and acquirers.\
An authorization request can come with the name of the cardholder on the ISO message.

The Issuer can validate this name data or handle the validation to the network sending the name of the cardholder on their database so the network will compare the data between issuer and acquirer.

Either way this is handled, it is another procedure to ensure that the transaction is safe and free of fraud, since there is key data to be confirmed by the issuer.

It is important for the issuer to confirm the type of enrollment they have in the network, if it is their responsibility to match the names or if it is the network's responsibility.

For Full balance issuers, ANI works as an automatic Pismo validation.\
For Zero balance issuers, Pismo forwards the data via webhook and the issuer performs the validation.

<Callout icon="📘" theme="info">
  This feature is currently available for Mastercard and Visa.
</Callout>

## Issuer verification option (`account_Name_Request = "I"`)

In this case, the customer performs the validation and returns the name matching decision.

**Sample request:**

The `accountOwnerData` is an array which contains the account owner information (sent by Visa for validation).

```json
{
	account_Owner_Data: [
        {
                account_Owner_Type            :   PRIMARY_OWNER,
                account_Owner_Name_First       :   "FirstName",
                account_Owner_Name_Middle      :   "MiddleName",
                account_Owner_Name_Last        :   "LastName",               
        }
    ],
    additional_Service_Request_Data: {
            account_Name_Request                  :   "I"
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
| `docs/card-issuing/rule-list.md` | body lines 1–275 | https://developers.pismo.io/pismo-docs/docs/rule-list | `e0e226a5db7724ab…` | 2026-06-28T21:57:58.000Z |

## Related knowledge units

- `KU-CARD-authorization-validation-rules-for-card-network-operations` — Authorization validation rules for card network operations
