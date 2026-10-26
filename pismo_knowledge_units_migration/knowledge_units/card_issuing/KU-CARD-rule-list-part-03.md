---
ku_id: KU-CARD-rule-list-part-03
title: Rule list (part 3 of 4)
category: card_issuing
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/card-issuing/rule-list.md
  sha256: e0e226a5db7724ab4bcb3a3e34992c1a1065af81f0596a307936ea7b70c8dbdb
  url: https://developers.pismo.io/pismo-docs/docs/rule-list
  role: primary_guide
  updated_at: '2026-06-28T21:57:58.000Z'
operations:
- get-v1-account-limit
- post-v1-customers-flex-controls
- updateProgramParameter
related_kus:
- KU-API-core-platform-flex-controls--customer-flex-controls-part-01
- KU-API-core-platform-ledger--account-limits
- KU-API-platform-setup-programs--parameters
- KU-EVT-catalogue-audit
grouping_rationale: single source page; split into parts because the page is very large
---

# Rule list (part 3 of 4)

**KU ID:** `KU-CARD-rule-list-part-03` · **Category:** Card issuing · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) (one part of a large page) into one implementation-oriented unit. Grouping rationale: single source page; split into parts because the page is very large

Scope as stated in `docs/card-issuing/rule-list.md`:

> * *Visa:*\* 63
>         * *Mastercard:*\* 63
>         * *TecBan:*\* 01
>         * *RuPay:*\* 05
>         * *ELO:*\* 82

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/card-issuing/rule-list.md`: Operation validation; Password tries validation; Card inputted expiration date validation; Card expiration date validation; Card valid until validation; Card status validation; Fetch account; Fetch account limit details; Account status validation; Max installments number validation; Fetch impact information; Authorization amounts calculation; Purchase with installments and interest validation; Max transactions validation for temporary cards; Max transaction amount validation; Available limits validation; Flex controls validation; Anti-fraud validation

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 3 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/card-issuing/rule-list.md` lines 3852–7005 of the body

Source URL: https://developers.pismo.io/pismo-docs/docs/rule-list · updatedAt: 2026-06-28T21:57:58.000Z

<!-- source:begin path=docs/card-issuing/rule-list.md part=3851-7005 -->
      <td>
        * *Visa:*\* 63
        * *Mastercard:*\* 63
        * *TecBan:*\* 01
        * *RuPay:*\* 05
        * *ELO:*\* 82
      </td>
    </tr>
  </tbody>
</Table>

**Additional data:** `additional data` contains important fields used in ATC validation.

**Fields:** `inputted_card_atc`, `persisted_card_atc`, `is_advice`, `merchant_category`

**Payload example:**

```json
{
    "name": "CARD_ATC",
    "status": "APPROVED",
    "reason": "CARD_ATC_VALID",
    "description": "Received 12 but the last is [9,6,5,1]. Used these params: MinOffset: 5, MaxOffset: 15, IsAdvice: false.",
    "additional_data": {
          "inputted_card_atc": "242",
          "persisted_card_atc": "[241,240,239,238,237,236,235,234,233,232,231,230,229,228,227,226,225,224,223,222,221,220,219,218,217,216,215,214,213,212,211,210,209,208,207,206,205,204,203,202,201,200,199,198,197,196,195,194,193,192,191,190,189,188,187,186,185,184,183,182,181,180,179,178,177,176,175,174,173,172,171,170,169,168,167,166,165,164,163,162,161,160,159,158,157,156,155,154,153,152,151,150,149,148,147,146,145,144,143,142,141,140,139,138,137,136,135,134,133,132,131,130,129,128,127,126,125,124,123,122,121,120,119,118,117,116,115,114,113,112,111,110,109,108,107,106,105,104,103,102,101,100,99,98,97,96,95,94,93,92,91,90,89,88,87,86,85,84,83,82,81,80,79,78,77,76,75,74,73,72,71,70,69,68,67,66,65,64,63,62,61,60,59,58,57,56,55,54,53,52,51,50,49,48,47,46,45,44,43,42,41,40,39,38,37,36,35,34,33,32,31,30,29,28,27,26,25,24,23,22,21,20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1]",
          "is_advice": false,
          "merchant_category": "XAS"
        }
}
```

# Operation validation

The Pismo platform checks to see if the operation is allowed by the issuer. To do this, it checks that the processing code is configured for the program of the card.

<Callout icon="📘" theme="info">
  This validation is performed only for full balance integration.
</Callout>

**Name:** OPERATION

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
        VALID\_OPERATION
      </td>

      <td>
        APPROVED
      </td>

      <td>
        Operation is configured and is allowed by the issuer for the program of the card that was used.
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
        CARD\_NOT\_FOUND
      </td>

      <td>
        SKIPPED
      </td>

      <td>
        Card not found, so validation can’t be performed.
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
        OPERATION\_NOT\_ALLOWED
      </td>

      <td>
        REJECTED
      </td>

      <td>
        Operation not configured by the issuer for the program of the card that was used.
      </td>

      <td>
        ANF
      </td>

      <td>
        * *Visa:*\* 5C
        * *Mastercard:*\* 57
        * *TecBan:*\* 57
        * *RuPay:*\* 57
        * *ELO:*\* 57
      </td>
    </tr>
  </tbody>
</Table>

**Additional data:** `additional_data` contains fields used in the step to define the operation of the transaction.

**Fields:** `org_id`, `processing_code`, `program_id`

**Payload example:**

```json
{
    "name": "OPERATION",
    "status": "APPROVED",
    "reason": "VALID_OPERATION",
    "description": "Valid operation (00) for OrgId (TN-OrgId) and ProgramId (123).",
    "additional_data": {
          "org_id": "TN-OrgId",
          "processing_code": "003100",
          "program_id": "888"
        }
}
```

# Password tries validation

The Pismo platform keeps track of how many times in a row a cardholder enters the wrong password. If this count reaches a configured threshold, the card is blocked and no new requests are allowed. This threshold is configured by the issuer on the Pismo platform.

The counter is only reset when the cardholder inputs the correct password in a new authorization request before reaching the blocking threshold. Requests that don't use a password, like e-commerce or contactless requests, do not reset the counter, even if they are approved. After reaching the threshold even requests that do not require a password are declined.

<Callout icon="📘" theme="info">
  This validation is performed for both zero balance and full balance integration.
</Callout>

**Name:** PASSWORD\_ATTEMPTS

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
        CARD\_PASSWORD\_ATTEMPTS\_VALID
      </td>

      <td>
        APPROVED
      </td>

      <td>
        Password was not needed or the correct password was entered before the allowed number of attempts was exceeded.
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
        CARD\_NOT\_FOUND
      </td>

      <td>
        SKIPPED
      </td>

      <td>
        Card not found, so validation can’t be performed.
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
        CARD\_PASSWORD\_ATTEMPTS\_EXCEEDED
      </td>

      <td>
        REJECTED
      </td>

      <td>
        Card was blocked because the allowed number of attempts was exceeded.
      </td>

      <td>
        TSM
      </td>

      <td>
        * *Visa:*\* 75
        * *Mastercard:*\* 75
        * *TecBan:*\* 38
        * *RuPay:*\* 75
        * *ELO:*\* 38
      </td>
    </tr>
  </tbody>
</Table>

**Additional data:** `additional_data` provides detailed information about the password attempts, including the maximum number of allowed tries, the current number of attempts made, and whether any invalid passwords have been entered.

**Fields:** `password_max_tries`, `password_tries`, `has_invalid_password`

**Payload example:**

```json
{
    "name": "PASSWORD_ATTEMPTS",
    "status": "APPROVED",
    "reason": "CARD_PASSWORD_ATTEMPTS_VALID",
    "description": "Password tries is valid.",
    "additional_data": {
          "password_max_tries": "4",
          "password_tries": "1",
          "has_invalid_password": false
   }
}
```

# Card inputted expiration date validation

The Pismo platform checks that the card expiration date provided by the cardholder matches the card's registered expiration date. This validation is also performed on hardware security module (HSM) validations since this information is part of the CVV calculation but the platform performs this validation at this point because not every request goes through HSM validation.

<Callout icon="📘" theme="info">
  This validation is performed for both zero balance and full balance integration.
</Callout>

**Name:** CARD\_INPUTTED\_EXPIRATION\_DATE

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
        CARD\_INPUTTED\_EXPIRATION\_DATE\_VALID
      </td>

      <td>
        APPROVED
      </td>

      <td>
        Correct expiration date entered.
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
        CARD\_NOT\_FOUND
      </td>

      <td>
        SKIPPED
      </td>

      <td>
        Card not found, so validation can’t be performed.
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
        CARD\_INPUTTED\_EXPIRATION\_DATE\_MISMATCH
      </td>

      <td>
        REJECTED
      </td>

      <td>
        Incorrect expiration date entered.
      </td>

      <td>
        CED
      </td>

      <td>
        * *Visa:*\* 54
        * *Mastercard:*\* 54
        * *TecBan:*\* 54
        * *RuPay:*\* 54
        * *ELO:*\* 54
      </td>
    </tr>
  </tbody>
</Table>

**Additional data:** `additional_data`  provides specific details about the card's expiration date, including the actual expiration date and the entered expiration date.

**Fields:** `expiration_date`, `inputted_expiration_date`

**Payload example:**

```json
{
    "name": "CARD_INPUTTED_EXPIRATION_DATE",
    "status": "APPROVED",
    "reason": "CARD_INPUTTED_EXPIRATION_DATE_VALID",
    "description": "Card inputted expiration date is valid.",
    "additional_data": {
          "expiration_date": "2805",
          "inputted_expiration_date": "2805"
        }
}
```

# Card expiration date validation

The Pismo platform validates whether the card is expired by the time of the authorization request. If the card's expiration date has passed, the request is declined.

<Callout icon="📘" theme="info">
  This validation is performed for both zero balance and full balance integration.
</Callout>

**Name:** CARD\_EXPIRATION\_DATE

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
        CARD\_NOT\_EXPIRED
      </td>

      <td>
        APPROVED
      </td>

      <td>
        Registered card expiration date is after the current time of the authorization request.
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
        CARD\_NOT\_FOUND
      </td>

      <td>
        SKIPPED
      </td>

      <td>
        Card not found, so validation can’t be performed.
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
        CARD\_EXPIRED
      </td>

      <td>
        REJECTED
      </td>

      <td>
        Registered card expiration date is before the current time of the authorization request.
      </td>

      <td>
        VNM
      </td>

      <td>
        * *Visa:*\* 54
        * *Mastercard:*\* 54
        * *TecBan:*\* 54
        * *RuPay:*\* 54
        * *ELO:*\* 54
      </td>
    </tr>
  </tbody>
</Table>

**Additional data:** `additional_data` contains the card expiration date. This field is only filled in for APPROVED and REJECTED status scenarios.\
**Field:** `expiration_date`

**Payload example:**

```json
{
    "name": "CARD_EXPIRATION_DATE",
    "status": "APPROVED",
    "reason": "CARD_NOT_EXPIRED",
    "description": "Card not expired.",
    "additional_data": {
      "expiration_date": "2028-05-23"
    }
}
```

# Card valid until validation

Cards can have a second expiration date called "valid until". This feature is used for temporary cards, which might need to be valid for a shorter time than would otherwise be allowed by the actual expiration date. The Pismo platform checks to make sure that  the "valid until" date is greater then the current time. If not, the request is declined.

<Callout icon="📘" theme="info">
  This validation is performed for both zero balance and full balance integration.
</Callout>

**Name:** CARD\_VALID\_UNTIL

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
        CARD\_VALID\_UNTIL\_VALID
      </td>

      <td>
        APPROVED
      </td>

      <td>
        "Until date" is after the current time of the authorization request.
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
        CARD\_NOT\_FOUND
      </td>

      <td>
        SKIPPED
      </td>

      <td>
        Card not found, so validation can’t be performed.
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
        CARD\_VALID\_UNTIL\_INVALID
      </td>

      <td>
        REJECTED
      </td>

      <td>
        "Until date" is before the current time of the authorization request.
      </td>

      <td>
        VEV
      </td>

      <td>
        * *Visa:*\* 54
        * *Mastercard:*\* 54
        * *TecBan:*\* 54
        * *RuPay:*\* 54
        * *ELO:*\* 54
      </td>
    </tr>
  </tbody>
</Table>

**Additional data:** `additional_data` contains the valid until date. This field is only filled in for APPROVED and REJECTED status scenarios.\
**Field:** `valid_until`

**Payload example:**

```json
{
    "name": "CARD_VALID_UNTIL",
    "status": "APPROVED",
    "reason": "CARD_VALID_UNTIL_VALID",
    "description": "Card is valid.",
    "additional_data": {
      "valid_until": "2023-02-04T16:58:14"
    }
}
```

# Card status validation

The Pismo platform checks a card's current status to make sure it is not blocked.

<Callout icon="📘" theme="info">
  This validation is performed for both zero balance and full balance integration.
</Callout>

**Name:** CARD\_STATUS

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
        CARD\_STATUS\_VALID
      </td>

      <td>
        APPROVED
      </td>

      <td>
        Card has status NORMAL or REISSUED.
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
        CARD\_NOT\_FOUND
      </td>

      <td>
        SKIPPED
      </td>

      <td>
        Card not found, so validation can’t be performed.
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
        CARD\_STATUS\_INVALID\_CREATED
      </td>

      <td>
        REJECTED
      </td>

      <td>
        Card has status CREATED.
      </td>

      <td>
        FRB
      </td>

      <td>
        * *Visa:*\* 78
        * *Mastercard:*\* 57
        * *TecBan:*\* 57
        * *RuPay:*\* 57
        * *ELO:*\* 78
      </td>
    </tr>

    <tr>
      <td>
        CARD\_STATUS\_INVALID\_BLOCKED
      </td>

      <td>
        REJECTED
      </td>

      <td>
        Card has status BLOCKED.
      </td>

      <td>
        UBT
      </td>

      <td>
        * *Visa:*\* 78
        * *Mastercard:*\* 57
        * *TecBan:*\* 76
        * *RuPay:*\* 57
        * *ELO:*\* 78
      </td>
    </tr>

    <tr>
      <td>
        CARD\_STATUS\_INVALID\_WARNING
      </td>

      <td>
        REJECTED
      </td>

      <td>
        Card has status WARNING.
      </td>

      <td>
        BNW
      </td>

      <td>
        * *Visa:*\* 59
        * *Mastercard:*\* 63
        * *TecBan:*\* 57
        * *RuPay:*\* 57
        * *ELO:*\* 62
      </td>
    </tr>

    <tr>
      <td>
        CARD\_STATUS\_INVALID\_CANCELED
      </td>

      <td>
        REJECTED
      </td>

      <td>
        Card has status CANCELED.
      </td>

      <td>
        BND
      </td>

      <td>
        * *Visa:*\* 46
        * *Mastercard:*\* 62
        * *TecBan:*\* 57
        * *RuPay:*\* 62
        * *ELO:*\* 46
      </td>
    </tr>

    <tr>
      <td>
        CARD\_STATUS\_INVALID\_CLIENTORDER
      </td>

      <td>
        REJECTED
      </td>

      <td>
        Card has status CLIENTORDER.
      </td>

      <td>
        BND
      </td>

      <td>
        * *Visa:*\* 46
        * *Mastercard:*\* 62
        * *TecBan:*\* 57
        * *RuPay:*\* 62
        * *ELO:*\* 46
      </td>
    </tr>

    <tr>
      <td>
        CARD\_STATUS\_INVALID\_FRAUD
      </td>

      <td>
        REJECTED
      </td>

      <td>
        Card has status FRAUD.
      </td>

      <td>
        BNF
      </td>

      <td>
        * *Visa:*\* 07
        * *Mastercard:*\* 04
        * *TecBan:*\* 57
        * *RuPay:*\* 04
        * *ELO:*\* 57
      </td>
    </tr>

    <tr>
      <td>
        CARD\_STATUS\_INVALID\_LOST
      </td>

      <td>
        REJECTED
      </td>

      <td>
        Card has status LOST.
      </td>

      <td>
        BNP
      </td>

      <td>
        * *Visa:*\* 41
        * *Mastercard:*\* 41
        * *TecBan:*\* 41
        * *RuPay:*\* 41
        * *ELO:*\* 41
      </td>
    </tr>

    <tr>
      <td>
        CARD\_STATUS\_INVALID\_ROBBED
      </td>

      <td>
        REJECTED
      </td>

      <td>
        Card has status ROBBED.
      </td>

      <td>
        BNR
      </td>

      <td>
        * *Visa:*\* 43
        * *Mastercard:*\* 43
        * *TecBan:*\* 43
        * *RuPay:*\* 43
        * *ELO:*\* 43
      </td>
    </tr>

    <tr>
      <td>
        CARD\_STATUS\_INVALID\_THEFT
      </td>

      <td>
        REJECTED
      </td>

      <td>
        Card has status THEFT.
      </td>

      <td>
        BNR
      </td>

      <td>
        * *Visa:*\* 43
        * *Mastercard:*\* 43
        * *TecBan:*\* 43
        * *RuPay:*\* 43
        * *ELO:*\* 43
      </td>
    </tr>

    <tr>
      <td>
        CARD\_STATUS\_INVALID\_DELETED
      </td>

      <td>
        REJECTED
      </td>

      <td>
        Card has status DELETED.
      </td>

      <td>
        VED
      </td>

      <td>
        * *Visa:*\* 46
        * *Mastercard:*\* 57
        * *TecBan:*\* 56
        * *RuPay:*\* 57
        * *ELO:*\* 46
      </td>
    </tr>

    <tr>
      <td>
        CARD\_STATUS\_INVALID\_DAMAGED
      </td>

      <td>
        REJECTED
      </td>

      <td>
        Card has status DAMAGED.
      </td>

      <td>
        BNM
      </td>

      <td>
        * *Visa:*\* 5C
        * *Mastercard:*\* 57
        * *TecBan:*\* 56
        * *RuPay:*\* 57
        * *ELO:*\* 57
      </td>
    </tr>

    <tr>
      <td>
        CARD\_STATUS\_INVALID\_UNRECEIVED
      </td>

      <td>
        REJECTED
      </td>

      <td>
        Card has status UNRECEIVED.
      </td>

      <td>
        BNU
      </td>

      <td>
        * *Visa:*\* 41
        * *Mastercard:*\* 41
        * *TecBan:*\* 41
        * *RuPay:*\* 57
        * *ELO:*\* 14
      </td>
    </tr>

    <tr>
      <td>
        CARD\_STATUS\_INVALID\_INOPERATIVE
      </td>

      <td>
        REJECTED
      </td>

      <td>
        Card has status INOPERATIVE.
      </td>

      <td>
        BNI
      </td>

      <td>
        * *Visa:*\* 14
        * *Mastercard:*\* 57
        * *TecBan:*\* 57
        * *RuPay:*\* 57
        * *ELO:*\* 14
      </td>
    </tr>

    <tr>
      <td>
        CARD\_STATUS\_UNKNOWN
      </td>

      <td>
        REJECTED
      </td>

      <td>
        Card has a status that is not mapped in the authorization system.
      </td>

      <td>
        CSU
      </td>

      <td>
        * *Visa:*\* 14
        * *Mastercard:*\* 57
        * *TecBan:*\* 56
        * *RuPay:*\* 57
        * *ELO:*\* 14
      </td>
    </tr>
  </tbody>
</Table>

**Additional data:** `additional_data` provides the specific status of the card.

**Field:** `status`

**Payload example:**

```json
{
    "name": "CARD_STATUS",
    "status": "APPROVED",
    "reason": "CARD_STATUS_VALID",
    "description": "Card status: NORMAL.",
    "additional_data": {
          "status": "NORMAL"
     }
}
```

# Fetch account

In order to process the authorization flow, the Pismo platform fetches the account to use its configurations. If an error happens while fetching these details, the authorization request is declined.

<Callout icon="📘" theme="info">
  This validation is performed only for Full Balance Flow.
</Callout>

**Name:** ACCOUNT

**Possible Status:** APPROVED, SKIPPED, REJECTED

**Possible Reasons:**

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
        ACCOUNT\_FOUND
      </td>

      <td>
        APPROVED
      </td>

      <td>
        Account found.
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
        CARD\_NOT\_FOUND
      </td>

      <td>
        SKIPPED
      </td>

      <td>
        If card was not found, there is no way to find out the account.
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
        ACCOUNT\_NOT\_FOUND
      </td>

      <td>
        REJECTED
      </td>

      <td>
        Account was not found.
      </td>

      <td>
        998
      </td>

      <td>
        * *Visa:*\* 14
        * *Mastercard:*\* 14
        * *TecBan:*\* 56
        * *RuPay:*\* 14
        * *ELO*\*: 14
      </td>
    </tr>

    <tr>
      <td>
        ACCOUNT\_GENERIC\_ERROR
      </td>

      <td>
        REJECTED
      </td>

      <td>
        An unexpected error has happened while fetching the account.
      </td>

      <td>
        AGE
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
        ACCOUNT\_TIMEOUT
      </td>

      <td>
        REJECTED
      </td>

      <td>
        A timeout occurred while fetching account.
      </td>

      <td>
        ACT
      </td>

      <td>
        * *Visa:*\* N0
        * *Mastercard:*\* 96
        * *TecBan:*\* 06
        * *RuPay:*\* 96
        * *ELO*\*: 96
      </td>
    </tr>
  </tbody>
</Table>

**Additional Data:** `additional_data` contains the account ID.

**Field:** `account_id`

**Payload example:**

```json
{
    "name": "ACCOUNT",
    "status": "APPROVED",
    "reason": "ACCOUNT_FOUND",
    "description": "Account found.",
    "additional_data": {
      "account_id": "123"
    }
}
```

# Fetch account limit details

If the Pismo platform cannot retrieve details about the account limits, the request is declined.

<Callout icon="📘" theme="info">
  This validation is performed only for full balance integration.
</Callout>

**Name:** ACCOUNT\_LIMITS

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
        ACCOUNT\_LIMITS\_FOUND
      </td>

      <td>
        APPROVED
      </td>

      <td>
        Account limit details retrieved successfully.
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
        CARD\_NOT\_FOUND
      </td>

      <td>
        SKIPPED
      </td>

      <td>
        Card not found, so validation can’t be performed.
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
        LEDGER\_ACCOUNT\_NOT\_FOUND
      </td>

      <td>
        REJECTED
      </td>

      <td>
        Account limit details not found.
      </td>

      <td>
        LNF
      </td>

      <td>
        * *Visa:*\* 14
        * *Mastercard:*\* 14
        * *TecBan:*\* 56
        * *RuPay:*\* 14
        * *ELO:*\* 14
      </td>
    </tr>

    <tr>
      <td>
        LEDGER\_ACCOUNT\_TIMEOUT
      </td>

      <td>
        REJECTED
      </td>

      <td>
        Timeout occurred  while retrieving account limit details.
      </td>

      <td>
        LCT
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
        LEDGER\_ACCOUNT\_GENERIC\_ERROR
      </td>

      <td>
        REJECTED
      </td>

      <td>
        Unexpected error occurred while retrieving account limit details.
      </td>

      <td>
        LAE
      </td>

      <td>
        * *Visa:*\* N0
        * *Mastercard:*\* 96
        * *TecBan:*\* 06
        * *RuPay:*\* 96
        * *ELO:*\* 96
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

**Additional data:** `additional_data` contains the account ID.

**Field:** `account_id`

**Payload example:**

```json
{
    "name": "ACCOUNT_LIMITS",
    "status": "APPROVED",
    "reason": "ACCOUNT_LIMITS_FOUND",
    "description": "Account limits exists.",
    "additional_data": {
      "account_id": "123"
    }
}
```

# Account status validation

The Pismo platform only authorizes a transaction on an account if the account status is `NORMAL`.

<Callout icon="📘" theme="info">
  This validation is performed only for full balance integration.
</Callout>

**Name:** ACCOUNT\_STATUS

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
        ACCOUNT\_STATUS\_VALID
      </td>

      <td>
        APPROVED
      </td>

      <td>
        Account is not blocked.
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
        CARD\_NOT\_FOUND
      </td>

      <td>
        SKIPPED
      </td>

      <td>
        Card not found, so validation can’t be performed.
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
        ACCOUNT\_STATUS\_INVALID
      </td>

      <td>
        REJECTED
      </td>

      <td>
        Account is blocked.
      </td>

      <td>
        CND
      </td>

      <td>
        * *Visa:*\* 62
        * *Mastercard:*\* 57
        * *TecBan:*\* 57
        * *RuPay:*\* 57
        * *ELO:*\* 62
      </td>
    </tr>
  </tbody>
</Table>

**Additional data:** `additional_data` contains the account status.

**Field:** `status`

**Payload example:**

```json
{
    "name": "ACCOUNT_STATUS",
    "status": "APPROVED",
    "reason": "ACCOUNT_STATUS_VALID",
    "description": "Account has a valid status: true.",
    "additional_data": {
      "status": "NORMAL"
    }
}
```

# Max installments number validation

The Pismo platform validates if the number of installments is less than or equal to the number configured for the program. This validation is based on `maxInstallmentsNumber` config on the `NetworkTransactionsProgramsConfig` table.

<Callout icon="📘" theme="info">
  This validation is performed only for full balance integration.
</Callout>

**Name:** MAX\_INSTALLMENTS\_NUMBER

**Possible statuses:** APPROVED, SKIPPED, REJECTED

**Possible reasons:**

| Reason                                      | Status   | Description                                                     | Custom Code | Response Code         |
| :------------------------------------------ | :------- | :-------------------------------------------------------------- | :---------- | :-------------------- |
| MAX\_INSTALLMENTS\_NUMBER\_VALID            | APPROVED | Number of installments are allowed for the program.             | N/A         | 00 (for all networks) |
| MAX\_INSTALLMENTS\_NUMBER\_NOT\_INSTALLMENT | SKIPPED  | It is not an installment transaction.                           | N/A         | N/A                   |
| MAX\_INSTALLMENTS\_NUMBER\_INVALID          | REJECTED | Number of installments is greater than allowed for the program. | N/A         | N/A                   |

**Additional data:** `additional_data` contains the program ID and the max number of Installments allowed for this program. This field is only filled in APPROVED and REJECTED status scenarios.

**Fields:** `program_id`, `max_installments_number`

**Payload example:**

```json
{
    "name": "MAX_INSTALLMENTS_NUMBER",
    "status": "APPROVED",
    "reason": "MAX_INSTALLMENTS_NUMBER_VALID",
    "description": "Number of installments allowed for the program.",
    "additional_data": {
      "program_id": 123,
      "max_installments_number": 12
    }
}
```

# Fetch impact information

If the Pismo platform cannot retrieve the impact information for the operation, the authorization request is declined.

<Callout icon="📘" theme="info">
  This is performed only for full balance integration.
</Callout>

**Name:** CREDIT\_LIMIT

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
        CREDIT\_LIMIT\_IMPACT\_FOUND
      </td>

      <td>
        APPROVED
      </td>

      <td>
        Impact information was found and is correctly configured.
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
        SKIPPED
      </td>

      <td>
        SKIPPED
      </td>

      <td>
        Card not found, so validation can’t be performed.
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
        CREDIT\_LIMIT\_IMPACT\_NOT\_FOUND
      </td>

      <td>
        REJECTED
      </td>

      <td>
        Impact not found or is configured incorrectly.
      </td>

      <td>
        998
      </td>

      <td>
        * *Visa:*\* 14
        * *Mastercard:*\* 14
        * *TecBan:*\* 56
        * *RuPay:*\* 14
        * *ELO:*\* 14
      </td>
    </tr>
  </tbody>
</Table>

**Additional data:** Not yet mapped

**Payload example:**

```json
{
    "name": "CREDIT_LIMIT",
    "status": "APPROVED",
    "reason": "CREDIT_LIMIT_IMPACT_FOUND",
    "description": "Acceptances found.",
    "additional_data": {}
}
```

# Authorization amounts calculation

The Pismo platform performs calculations related to the transaction amount, such as currency conversion, installments calculations, and the application of fees and taxes. If an error occurs in a calculation or some needed information is missing, the authorization request is declined.

<Callout icon="📘" theme="info">
  This validation is performed only for full balance integration.
</Callout>

**Name:** RATES

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
        RATES\_APPROVED
      </td>

      <td>
        APPROVED
      </td>

      <td>
        All calculations performed successfully.
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
        SKIPPED
      </td>

      <td>
        SKIPPED
      </td>

      <td>
        Card not found, so validation can’t be performed.
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
        RATES\_REJECT
      </td>

      <td>
        REJECTED
      </td>

      <td>
        Unexpected error occurred while calculating the authorization amounts.
      </td>

      <td>
        RAE
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

**Additional data:** Not yet mapped

**Payload example:**

```json
{
    "name": "RATES",
    "status": "APPROVED",
    "reason": "RATES_APPROVED",
    "description": "All calculation were performed successfully.",
    "additional_data": {}
}
```

# Purchase with installments and interest validation

If installments and interest need to be calculated for a transaction, the Pismo platform must retrieve all the statements related to the number of installments. This is because the due date of each installment is used in the calculation. If there are more installments than configured statements, the calculation can't be performed, and the authorization request is declined.

<Callout icon="📘" theme="info">
  This validation is performed only for full balance integration.
</Callout>

**Name:** STATEMENTS

**Possible statuses:** REJECTED

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
        INSUFFICIENT\_STATEMENTS
      </td>

      <td>
        REJECTED
      </td>

      <td>
        Insufficient number of created statements to calculate installments.
      </td>

      <td>
        ISE
      </td>

      <td>
        * *Visa:*\* 5C
        * *Mastercard:*\* 57
        * *TecBan:*\* 06
        * *RuPay:*\* 57
        * *ELO:*\* 57
      </td>
    </tr>
  </tbody>
</Table>

**Additional data:** Not yet mapped. The field `custom_code` is only present when the validation is REJECTED.

**Payload example:**

```json
{
    "name": "STATEMENTS",
    "status": "REJECTED",
    "reason": "INSUFFICIENT_STATEMENTS",
    "description": "Insufficient number of created statements to calculate installments.",
    "additional_data": {}
}
```

# Max transactions validation for temporary cards

The Pismo platform ensures that the number of authorized transactions does not exceed the maximum allowed number of transactions for a temporary card. This parameter is configured in the [program parameters](https://developers.pismo.io/pismo-docs/reference/updateprogramparameter). If this parameter is not set, or the card is not of type `TEMPORARY`, this validation is not performed.

<Callout icon="📘" theme="info">
  This validation is performed only for full balance integration.
</Callout>

**Name:** MAX\_TRANSACTIONS\_FOR\_TEMPORARY\_CARD

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
        MAX\_TRANSACTIONS\_IF\_TEMPORARY\_CARD\_APPROVED
      </td>

      <td>
        APPROVED
      </td>

      <td>
        Card is temporary and the number of transactions is under the configured threshold.
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
        CARD\_NOT\_FOUND
      </td>

      <td>
        SKIPPED
      </td>

      <td>
        Card not found, so validation can’t be performed.
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
        MAX\_TRANSACTIONS\_IF\_TEMPORARY\_CARD\_SKIPPED
      </td>

      <td>
        SKIPPED
      </td>

      <td>
        Card is not temporary.
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
        MAX\_TRANSACTIONS\_IF\_TEMPORARY\_CARD\_EXCEEDED
      </td>

      <td>
        REJECTED
      </td>

      <td>
        Number of transactions performed using temporary card exceeded the configured threshold.
      </td>

      <td>
        CTE
      </td>

      <td>
        * *Visa:*\* 54
        * *Mastercard:*\* 54
        * *Tecban:*\* 54
        * *Rupay:*\* 54
        * *ELO:*\* 54
      </td>
    </tr>
  </tbody>
</Table>

**Additional data:** `additional_data` contains the number of transactions (`transactions`) and the maximum transactions limit (`limit`) for a temporary card. This field is only filled in APPROVED and REJECTED status scenarios.

**Fields:** `limit`, `transactions`

**Payload example:**

```json
{
        "name": "MAX_TRANSACTIONS_FOR_TEMPORARY_CARD",
        "status": "APPROVED",
        "reason": "MAX_TRANSACTIONS_IF_TEMPORARY_CARD_APPROVED",
        "description": "The temporary card has limit for this transaction, limit: 2, number of transactions: 0",
        "additional_data": {
          "limit": 2,
          "transactions": 0
        }
}
```

# Max transaction amount validation

The Pismo platform validates that the transaction amount does not exceed the maximum amount allowed for the card. This validation is not cumulative, so for every new request, the same maximum amount is used. This parameter is configured when the card is created. If the parameter is not set, the validation is not performed.

<Callout icon="📘" theme="info">
  This validation is performed only for full balance integration.
</Callout>

**Name:** CARD\_TRANSACTION\_LIMIT

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
        LIMIT\_APPROVED
      </td>

      <td>
        APPROVED
      </td>

      <td>
        Maximum transaction limit is greater than the amount of the authorization request.
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
        SKIPPED
      </td>

      <td>
        SKIPPED
      </td>

      <td>
        Card not found, so validation can’t be performed.
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
        LIMIT\_INSUFFICIENT\_FUNDS
      </td>

      <td>
        REJECTED
      </td>

      <td>
        Transaction amount is greater than the maximum transaction limit configured for the card.
      </td>

      <td>
        810
      </td>

      <td>
        * *Visa:*\* 51
        * *Mastercard:*\* 51
        * *TecBan:*\* 51
        * *RuPay:*\* 51
        * *ELO:*\* 51
      </td>
    </tr>
  </tbody>
</Table>

**Additional data:** `additional_data` contains the transaction limit. This field is only filled in for APPROVED and REJECTED status scenarios if this limit exists.

**Field:** `transaction_limit`

**Payload example:**

```json
{
    "name": "CARD_TRANSACTION_LIMIT",
    "status": "APPROVED",
    "reason": "LIMIT_APPROVED",
    "description": "Card transaction sufficient limit.",
    "additional_data": {
      "transaction_limit": 9999.0
    }
}
```

# Available limits validation

Pismo Authorization platform validates the accounts limits to define whether the amount of the authorization can be approved or not. At this moment, [Ledger-API](https://developers.pismo.io/pismo-docs/reference/get-v1-account-limit) is called to proceed with the validation and impact of the account limits. Ledge also validates that the account is allowed to receive a debit or  credit, depending on the operation being performed.

<Callout icon="📘" theme="info">
  This validation is performed only for full balance integration.
</Callout>

**Name:** LEDGER

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
        LEDGER\_APPROVED
      </td>

      <td>
        APPROVED
      </td>

      <td>
        All available limits were successfully validated and the authorization can proceed.
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
        SKIPPED
      </td>

      <td>
        SKIPPED
      </td>

      <td>
        If card was not found or there is any previous denial in the authorization request, the ledger is skipped to avoid impacts on the account limits.
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
        LEDGER\_INSUFFICIENT\_BALANCE
      </td>

      <td>
        REJECTED
      </td>

      <td>
        Authorization request is greater than the account available limits.
      </td>

      <td>
        810
      </td>

      <td>
        * *Visa:*\* 51
        * *Mastercard:*\* 51
        * *TecBan:*\* 51
        * *RuPay:*\* 51
        * *ELO:*\* 51
      </td>
    </tr>

    <tr>
      <td>
        LEDGER\_EXCEEDS\_WITHDRAWAL\_LIMIT
      </td>

      <td>
        REJECTED
      </td>

      <td>
        Authorization request is a withdrawal, and the amount is greater than the account available limits.
      </td>

      <td>
        810
      </td>

      <td>
        * *Visa:*\* 61
        * *Mastercard:*\* 61
        * *TecBan:*\* 61
        * *RuPay:*\* 61
        * *ELO:*\* 61
      </td>
    </tr>

    <tr>
      <td>
        LEDGER\_NOT\_ALLOWED\_OPERATION
      </td>

      <td>
        REJECTED
      </td>

      <td>
        Account is blocked from receiving debits or credits.
      </td>

      <td>
        CND
      </td>

      <td>
        * *Visa:*\* 62
        * *Mastercard:*\* 57
        * *TecBan:*\* 57
        * *RuPay:*\* 57
        * *ELO:*\* 62
      </td>
    </tr>

    <tr>
      <td>
        LEDGER\_DUPLICATED\_TRACKING\_ID
      </td>

      <td>
        REJECTED
      </td>

      <td>
        Internal error caused a duplicated tracking ID while calling Ledger.
      </td>

      <td>
        LUD
      </td>

      <td>
        * *Visa:*\* N0
        * *Mastercard:*\* 96
        * *TecBan:*\* 06
        * *RuPay:*\* 96
        * *ELO:*\* 96
      </td>
    </tr>

    <tr>
      <td>
        LEDGER\_LIMIT\_UPDATE\_ERROR
      </td>

      <td>
        REJECTED
      </td>

      <td>
        Unexpected error occurred while calling Ledger.
      </td>

      <td>
        LUE
      </td>

      <td>
        * *Visa:*\* N0
        * *Mastercard:*\* 96
        * *TecBan:*\* 06
        * *RuPay:*\* 96
        * *ELO:*\* 96
      </td>
    </tr>

    <tr>
      <td>
        LEDGER\_TIMEOUT
      </td>

      <td>
        REJECTED
      </td>

      <td>
        Timeout occurred while calling Ledger.
      </td>

      <td>
        LUT
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

**Additional data:** `additional_data` contains the available credit limit, total credit limit, max credit limit, and dry run indicator. These fields are only filled in for APPROVED status scenarios or the REJECTED reason `LEDGER_INSUFFICIENT_BALANCE`.

Validation results from Ledger will be available in `additional_data` for APPROVED and the following REJECTED reasons:

* `LEDGER_INSUFFICIENT_BALANCE`
* `LEDGER_EXCEEDS_WITHDRAWAL_LIMIT`
* `LEDGER_NOT_ALLOWED_OPERATION`

The `dry_run_result` field indicates the result for the dry run validation. For dry run validation, the Ledger validations are performed, but the account balance is not impacted. The dry run is performed for the following statuses:

* `SKIPPED`, except for cases where `There is no Credit Impact configured for this operation`
* `REJECTED`, for these reasons:
  * `LEDGER_INSUFFICIENT_BALANCE`
  * `LEDGER_EXCEEDS_WITHDRAWAL_LIMIT`
  * `LEDGER_NOT_ALLOWED_OPERATION`

The `dry_run_result` field indicates the result for the dry run validation. It will be passed when `dry_run` is `true`. Possible values for this field are:

* `APPROVED`—Ledger dry run approved
* `REJECTED`—Ledger dry run rejected
* `TIMEOUT`—Timeout calling Ledger dry run
* `ERROR`—Error calling Ledger dry run

**Payload examples:**

```json
{
    "name": "LEDGER",
    "status": "APPROVED",
    "reason": "LEDGER_APPROVED",
    "description": "Ledger validations approved.",
    "additional_data": {
        "dry_run": false,
        "available_credit_limit": 1000.00,
        "total_credit_limit": 1000.00,
        "max_credit_limit": 1000.00,
        "validation_results": [
            {
                "account_id": 123456,
                "available_amounts": {
                    "details": {
                        "result": {
                            "overlimit": 0,
                            "held_funds": 0,
                            "additional_funds": 0,
                            "total_overdraft_limit": 0,
                            "available_credit_limit": 1000,
                            "available_withdraw_limit": 100,
                            "available_installment_limit": 0,
                            "available_savings_account_limit": 0
                        }
                    },
                    "validation_status": "APPROVED"
                },
                "ledger_operation_status": {
                    "validation_status": "APPROVED"
                }
            }
        ]
    }
}
```

```json
{
    "name": "LEDGER",
    "status": "REJECTED",
    "reason": "LEDGER_INSUFFICIENT_BALANCE",
    "description": "Account limits is insufficient to perform transaction.",
    "additional_data": {
        "dry_run": true,
      	"dry_run_result": "REJECTED",
        "custom_code": "810",
        "available_credit_limit": 1000.0,
        "total_credit_limit": 15000.0,
        "max_credit_limit": 15000.0,
        "validation_results": [
            {
                "account_id": 123456,
                "available_amounts": {
                    "details": {
                        "mock_result": {
                            "overlimit": 0,
                            "held_funds": 0,
                            "additional_funds": 0,
                            "total_overdraft_limit": 0,
                            "available_credit_limit": -10.0,
                            "available_withdraw_limit": 200,
                            "available_installment_limit": 1000,
                            "available_savings_account_limit": 0
                        }
                    },
                    "validation_status": "REJECTED"
                },
                "ledger_operation_status": {
                    "validation_status": "APPROVED"
                }
            }
        ]
    }
}
```

```Text JSON
{
    "name": "LEDGER",
    "status": "SKIPPED",
    "reason": "SKIPPED",
    "description": "Ledger validations skipped by dry run.",
    "additional_data": {
        "available_credit_limit": 4709.73,
        "total_credit_limit": 15000.0,
        "max_credit_limit": 15000.0,
        "dry_run": true,
        "dry_run_result": "APPROVED",
        "validation_results": [
            {
                "account_id": 123456,
                "ledger_operation_status": {
                    "validation_status": "APPROVED"
                },
                "available_amounts": {
                    "validation_status": "APPROVED",
                    "details": {
                        "result": {
                            "available_credit_limit": 4709.72,
                            "available_withdraw_limit": 450,
                            "available_installment_limit": 1000,
                            "available_savings_account_limit": 0,
                            "held_funds": 0,
                            "additional_funds": 0,
                            "total_overdraft_limit": 0,
                            "overlimit": 0
                        }
                    }
                }
            }
        ]
    }
}
```

<br />

# Flex controls validation

The Pismo Authorization platform calls the [Flex Controls API](https://developers.pismo.io/pismo-docs/reference/post-v1-customers-flex-controls) to evaluate the configured rules against the request being processed. If any rule fails, the request is declined.

**Name:** RULES

**Possible status:** APPROVED, SKIPPED, REJECTED

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
        RULES\_APPROVED
      </td>

      <td>
        APPROVED
      </td>

      <td>
        All rules were successfully evaluated and approved.
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
        SKIPPED
      </td>

      <td>
        SKIPPED
      </td>

      <td>
        There was a preview denial in the authorization flow, so Rules validation will be called in dry run mode.
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
        RULES\_NOT\_ENABLED
      </td>

      <td>
        SKIPPED
      </td>

      <td>
        Flex controls evaluation not enabled for that program/account/card, so the API will not be called.
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
        RULES\_OPERATION\_NOT\_ALLOWED
      </td>

      <td>
        REJECTED
      </td>

      <td>
        Flex controls evaluation reported that some rules declined this request.
      </td>

      <td>
        The custom code configured in Flex Controls API for the evaluated rule. If there is no custom code configured, RED will be used.
      </td>

      <td>
        * *Visa:*\* 78
        * *Mastercard:*\* 05
        * *TecBan:*\* 05
        * *RuPay:*\* 05
        * *ELO:*\* 57
      </td>
    </tr>

    <tr>
      <td>
        RULES\_DO\_NOT\_HONOR
      </td>

      <td>
        REJECTED
      </td>

      <td>
        Flex controls evaluation reported the request declined.
      </td>

      <td>
        RED
      </td>

      <td>
        * *Visa:*\* 78
        * *Mastercard:*\* 57
        * *TecBan:*\* 57
        * *RuPay:*\* 57
        * *ELO:*\* 57
      </td>
    </tr>

    <tr>
      <td>
        RULES\_INTERNAL\_ERROR
      </td>

      <td>
        REJECTED
      </td>

      <td>
        Internal error occurred while calling Flex Controls API.
      </td>

      <td>
        RED
      </td>

      <td>
        * *Visa:*\* N0
        * *Mastercard:*\* 96
        * *TecBan:*\* 06
        * *RuPay:*\* 96
        * *ELO:*\* 96
      </td>
    </tr>

    <tr>
      <td>
        RULES\_OPERATION\_NOT\_ALLOWED\_CREDIT\_VOUCHER
      </td>

      <td>
        REJECTED
      </td>

      <td>
        Flex controls evaluation reported the request declined.
      </td>

      <td>
        RED
      </td>

      <td>
        * *Visa:*\* 59
        * *Mastercard:*\* 57
        * *TecBan:*\* 57
        * *RuPay:*\* 57
        * *ELO:*\* 57
      </td>
    </tr>
  </tbody>
</Table>

> 📘 Flex controls with Zero balance workflows
>
> In Zero Balance workflows, the Pismo platform is not responsible for calculating currency exchange rates, fees, taxes, interest, tariffs, or any other financial components. These values are not provided to the platform.
>
> Because the principal amount is the only monetary value received by the Pismo platform in Zero Balance workflows, and Pismo does not calculate any additional components (fees, taxes, interest, exchange rates, and so on), Flex Controls performs all validations and accumulations exclusively based on the principal amount, rather than the full contract amount.
>
> As a result, the validation of the transaction amount and the accumulated amounts calculated by Flex Controls may be inaccurate when the principal amount differs from the contract amount (for example, principal amount + fees + taxes + interest, and so on).

**Additional data:** `additional_data` contains the custom denial code configured in the Flex Control creation and also the error code returned by the Flex Controls API response. This field is filled in Approved and Operation Not Allowed scenarios.

The dry run information indicates if it is a dry run validation. For dry run validation, Flex Controls validations are performed, but rules values are not impacted/incremented. A dry run validation happens when the authorization already has a previous `REJECTED` validation or `RULES` validation is rejected for one of the following reasons:

* `RULES_OPERATION_NOT_ALLOWED`
* `RULES_OPERATION_NOT_ALLOWED_CREDIT_VOUCHER`

The `Dry Run Result` field indicates the result for the dry run validation. It will be passed when `Dry Run` is `true`. Possible values for this field are:

* APPROVED: `Rules` dry run approved
* REJECTED: `Rules` dry run rejected
* ERROR: Error calling `Rules` dry run

**Fields:**

* For reason RULES\_APPROVED: `dry_run`, `evaluated_controls`
* For reason RULES\_OPERATION\_NOT\_ALLOWED: `dry_run`, `dry_run-result`, `denial_code`, `error_code`, `custom_code`, `evaluated_controls`
* For reason RULES\_INTERNAL\_ERROR: `dry_run`, `custom_code`
* For reason SKIPPED: `dry_run`, `dry_run_result`, `custom_code`, `evaluated_controls`

**Payload examples:**

```json
{
    "name": "RULES",
    "status": "REJECTED",
    "reason": "RULES_OPERATION_NOT_ALLOWED",
    "description": "Transaction not authorized as rule evaluation failed with error code [RULV10400], denial code [DENY_CODE], response code [63] and custom code [null]",
    "additional_data": {
      "dry_run": true,
        "dry_run_result": "REJECTED",
        "denial_code": "DENY_CODE",
        "error_code": "RULV10400",
        "custom_code": "RED",
        "evaluated_controls": [
            {
              "id": "id-rule-1",
              "name": "Rule 1",
              "message": "Message rule 1",
              "deny_code": "DENY_CODE",
              "response_code": "63",
              "available_limit": 0,
              "evaluation_result": false
            },
            {
              "id": "id-rule-2",
              "name": "Rule 2",
              "deny_code": "OTHER_DENY_CODE",
              "max_limit": 200000,
              "custom_code": "R01",
              "response_code": "63",
              "available_limit": 184951,
              "accumulated_limit": 15049,
              "evaluation_result": true
            }
        ]
    }
}
```

```json
{
    "name": "RULES",
    "status": "SKIPPED",
    "reason": "SKIPPED",
    "description": "Rules evaluation skipped by dry run.",
    "additional_data": {
        "dry_run": true,
        "dry_run_result": "REJECTED",
        "custom_code": "RED",
        "evaluated_controls": [
            {
              "id": "id-rule-1",
              "name": "Rule 1",
              "message": "Message rule 1",
              "deny_code": "DENY_CODE",
              "response_code": "63",
              "available_limit": 0,
              "evaluation_result": false
            },
            {
              "id": "id-rule-2",
              "name": "Rule 2",
              "deny_code": "OTHER_DENY_CODE",
              "max_limit": 200000,
              "custom_code": "R01",
              "response_code": "63",
              "available_limit": 184951,
              "accumulated_limit": 15049,
              "evaluation_result": true
            }
        ]
    }
}
```

<br />

# Anti-fraud validation

The Pismo Authorization platform calls an external endpoint to give the issuer the ability to perform any validation they wish. This endpoint can connect to an anti-fraud system or to the issuer themselves.

<Callout icon="📘" theme="info">
  This validation is performed only for full balance integration.
</Callout>

**Name:** ANTI\_FRAUD

**Possible Statuses:** APPROVED, REJECTED

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
        ANTI\_FRAUD\_APPROVE
      </td>

      <td>
        APPROVED
      </td>

      <td>
        Call to third-party endpoint was successful, and the request was approved.
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
        ANTI\_FRAUD\_FORCE\_APPROVE
      </td>

      <td>
        APPROVED
      </td>

      <td>
        Call to third party endpoint was successful and forced the request to be approved by overriding the Pismo platform denial decision.
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
        ANTI\_FRAUD\_APPROVE\_BY\_DEFAULT
      </td>

      <td>
        APPROVED
      </td>

      <td>
        Call to third-party endpoint has failed but it is configured to approve by default when unavailable and keep the Pismo platform decision.
      </td>

      <td>
        N/A
      </td>

      <td>
        ANTI\_FRAUD\_OVERRIDE\_REJECTION
      </td>
    </tr>

    <tr>
      <td>
        ANTI\_FRAUD\_OVERRIDE\_REJECTION
      </td>

      <td>
        REJECTED
      </td>

      <td>
        Third-party endpoint has declined the request and overrode the Pismo platform response code.
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
        ANTI\_FRAUD\_REJECT
      </td>

      <td>
        REJECTED
      </td>
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `PUT /programs/v1/programs/{program_id}/parameters/{program_parameter_id}` | `updateProgramParameter` | Update program parameter | `api-specs/Platform_setup_-_Programs.yaml` | no | KU-API-platform-setup-programs--parameters |
| `GET /v1/accounts/{accountId}/limits` | `get-v1-account-limit` | List account limits | `api-specs/Core_platform_-_Ledger.yaml` | no | KU-API-core-platform-ledger--account-limits |
| `POST /v1/customers/{customerId}/flex-controls` | `post-v1-customers-flex-controls` | Create customer flex control | `api-specs/Core_platform_-_Flex_controls.yaml` | no | KU-API-core-platform-flex-controls--customer-flex-controls-part-01 |

### Operation essentials

- **`PUT /programs/v1/programs/{program_id}/parameters/{program_parameter_id}`** (`updateProgramParameter`): security `S2SAuthentication`; required parameters `program_id` (path), `program_parameter_id` (path); required body fields `value`; response statuses 200, 400; error codes in examples none; events none listed.
- **`GET /v1/accounts/{accountId}/limits`** (`get-v1-account-limit`): security `BearerAuth`; required parameters `accountId` (path); required body fields none declared; response statuses 200, 400, 404, 500; error codes in examples `WLDG0020`, `WLDG0022`, `ELDG9999`; events none listed.
- **`POST /v1/customers/{customerId}/flex-controls`** (`post-v1-customers-flex-controls`): security `BearerAuth`; required parameters `customerId` (path); required body fields `type`, `name`, `account_id`; response statuses 201, 400, 403, 409, 500; error codes in examples `ERUL1101`, `RULVAL0400`, `ERUL1102`, `ERUL1106`, `ERUL0002`, `RULVAL0403`, `WRUL1207`, `RULVAL0409`, `ERUL0005`, `RULREP0500`, `ERUL1105`; events `audit-customer-spending-limit-created-1`.

## Events

Events emitted by the referenced operations (`api-reference-data/endpoint_event_map.csv`):

| Operation | Event slug |
| --- | --- |
| `post-v1-customers-flex-controls` | `audit-customer-spending-limit-created-1` |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/card-issuing/rule-list.md`: updatedAt 2026-06-28T21:57:58.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- Source content contains MDX/HTML components (for example `<Table>`, `<HTMLBlock>`, `<Callout>`, `<details>`). They are preserved exactly as published; tables inside them were not converted to Markdown.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/card-issuing/rule-list.md` | body lines 3852–7005 | https://developers.pismo.io/pismo-docs/docs/rule-list | `e0e226a5db7724ab…` | 2026-06-28T21:57:58.000Z |

## Related knowledge units

- `KU-API-core-platform-flex-controls--customer-flex-controls-part-01` — API reference: Core platform - Flex controls — Customer flex controls (part 1 of 2)
- `KU-API-core-platform-ledger--account-limits` — API reference: Core platform - Ledger — Account limits
- `KU-API-platform-setup-programs--parameters` — API reference: Platform setup - Programs — Parameters
- `KU-EVT-catalogue-audit` — Event catalogue: audit
