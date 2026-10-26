---
ku_id: KU-CARD-rule-list-part-02
title: Rule list (part 2 of 4)
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
- KU-CARD-cards-overview-1
grouping_rationale: single source page; split into parts because the page is very large
---

# Rule list (part 2 of 4)

**KU ID:** `KU-CARD-rule-list-part-02` · **Category:** Card issuing · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) (one part of a large page) into one implementation-oriented unit. Grouping rationale: single source page; split into parts because the page is very large

Scope as stated in `docs/card-issuing/rule-list.md`:

> In this case, Visa performs the validation and returns the account owner information (primary account owner / secondary account owner (optional)).

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/card-issuing/rule-list.md`: Visa verification option (`account_Name_Request = "Y"`); Address Verification Service (AVS); ARQC validation; CVM validation; Entry mode validation; Installments validation; DCC validation; Currency validation (deprecated); Terminal capability validation; Chip values validation; Chip signature validation; Message format validation; Valid card validation; Valid card token validation; Token status validation; Fetch program; Processing code definition; Fetch authorization configuration; Card mode validation; Card mode status validation; Contactless allowed validation; Account type validation; Card ATC validation

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/card-issuing/rule-list.md` lines 276–3851 of the body

Source URL: https://developers.pismo.io/pismo-docs/docs/rule-list · updatedAt: 2026-06-28T21:57:58.000Z

<!-- source:begin path=docs/card-issuing/rule-list.md part=275-3851 -->
## Visa verification option (`account_Name_Request = "Y"`)

In this case, Visa performs the validation and returns the account owner information (primary account owner / secondary account owner (optional)).

**Sample request:**

```json
{
	account_Owner_Data: []
    additional_Service_Request_Data: {
            account_Name_Request      :   "Y"
    }
}
```

**Sample response:**

`name_Account_Match_Decision` values could be:

```json
MATCH,
PARTIAL_MATCH,
NO_MATCH,
UNVERIFIED (When for some reason the validation isn't performed)
```

`account_Name_Request_Result` values could be:

```json
NAME_MATCH_PERFORMED,
NAME_MATCH_NOT_PERFORMED,
NAME_MATCH_NOT_SUPPORTED
```

```json
{
	account_Owner_Data: {
        {
                account_Owner_Type            :   PRIMARY_OWNER,
                account_Owner_Name_First       :   "FirstName",
                account_Owner_Name_Middle      :   "MiddleName",
                account_Owner_Name_Last        :   "LastName",
                additional_Service_Result_Data : {
                        account_Name_Request_Result            :   "NAME_MATCH_PERFORMED",
                        full_Name_Account_Match_Decision        :   "MATCH",
                        last_Name_Account_Match_Decision        :   "MATCH",
                        middle_Name_Account_Match_Decision      :   "NO_MATCH",
                        first_Name_Account_Match_Decision       :   "PARTIAL_MATCH",
                },               
        }
    },
    additional_Service_Request_Data: {
            account_Name_Request                  :   "I"
    }
}
```

# Address Verification Service (AVS)

AVS is a fraud prevention tool implemented by the networks, issuers, and acquirers.\
An authorization request can come with the address data registered by the cardholder when processing transactions.

In the AVS workflow, the issuer must validate the address. It can validate information such postal code and street name/number.

This type of validation delivers a more secure transaction since the issuer uses one more key data to verify the cardholder identity and then approves the request for transaction.

<Callout icon="📘" theme="info">
  Note: this feature is currently available for Mastercard and Visa.
</Callout>

At Pismo, in the full balance workflow, Pismo APIs can use the account data register by the issuers to run the necessary validations. In that scenario, the issuers do not need to manage the data. The only responsibility is to make sure that the information of the cardholder is updated in the Pismo Database.

For zero balance issuers, Pismo sends the required information to the customer to validate the address in the following format along with the other payload data on the webhook.

**Sample request:**

```json
{
	cardholder_postal_code : 12345
	cardholder_street_number : 999
	cardholder_street_address : Production St.
}
```

**Sample response:**

Expected response from zero balance, along with other response fields:

```json
{
	match_address : true
	match_postal_code : true
	no_address_data : false
}
```

# ARQC validation

The Pismo platform checks that the information contained in the **cryptogram** field is valid. It calls the HSM to perform this validation.

<Callout icon="📘" theme="info">
  This validation is performed for both zero balance and full balance integration.
</Callout>

**Name:** ARQC

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
        ARQC\_SIGNATURE\_VALID
      </td>

      <td>
        APPROVED
      </td>

      <td>
        ARQC information present and valid.
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
        NO\_CRYPTOGRAM
      </td>

      <td>
        SKIPPED
      </td>

      <td>
        No ARQC information present in request, so no need for this validation.
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
        INCOMPATIBLE\_PROCESSING\_CODE
      </td>

      <td>
        SKIPPED
      </td>

      <td>
        Request was a credit voucher with no ARQC information, so validation was skipped.
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
        ARQC\_INVALID
      </td>

      <td>
        REJECTED
      </td>

      <td>
        HSM declined the transaction, because the cryptogram information was invalid.
      </td>

      <td>
        FRN
      </td>

      <td>
        * *Visa:*\* 82
        * *Mastercard:*\* 63
        * *TecBan:*\* R9
        * *RuPay:*\* E3
        * *ELO:*\* 82
      </td>
    </tr>

    <tr>
      <td>
        HSM\_COMMUNICATION\_ERROR
      </td>

      <td>
        REJECTED
      </td>

      <td>
        Internal error while calling the HSM.
      </td>

      <td>
        FRN
      </td>

      <td>
        * *Visa:*\* 82
        * *Mastercard:*\* 63
        * *TecBan:*\* R9
        * *RuPay:*\* E3
        * *ELO:*\* 82
      </td>
    </tr>

    <tr>
      <td>
        SHOULD\_HAVE\_CRYPTOGRAM
      </td>

      <td>
        REJECTED
      </td>

      <td>
        Request entry mode is Chip (05), but doesn’t have cryptogram information.
      </td>

      <td>
        FRN
      </td>

      <td>
        * *Visa:*\* 82
        * *Mastercard:*\* 63
        * *TecBan:*\* R9
        * *RuPay:*\* E3
        * *ELO:*\* 82
      </td>
    </tr>

    <tr>
      <td>
        SHOULD\_NOT\_HAVE\_CRYPTOGRAM
      </td>

      <td>
        REJECTED
      </td>

      <td>
        Request contains cryptogram information, but entry mode is not valid for chip operations.
      </td>

      <td>
        FRN
      </td>

      <td>
        * *Visa:*\* 82
        * *Mastercard:*\* 63
        * *TecBan:*\* R9
        * *RuPay:*\* E3
        * *ELO:*\* 82
      </td>
    </tr>
  </tbody>
</Table>

**Additional data:** Not yet mapped

**Payload example:**

```json
{
    "name": "ARQC",
    "status": "APPROVED",
    "reason": "ARQC_SIGNATURE_VALID",
    "description": "ARQC valid",
    "additional_data": {}
}
```

# CVM validation

The Pismo platform performs a cardholder verification method (CVM) validation to check that the CVV or PIN information contained in the authorization request is valid. If no verification method is present (CVV, Cryptogram, or PIN), the platform checks that  the request is marked as secure, if it is a recurring authorization, or if NoCVM requests are allowed by the issuer.

<Callout icon="📘" theme="info">
  This validation is performed for both zero balance and full balance integration.
</Callout>

**Name:** CVM

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
        PIN\_AND\_CVV\_VALID
      </td>

      <td>
        APPROVED
      </td>

      <td>
        PIN or CVV present and the information was valid.
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
        SAFE\_TRANSACTION
      </td>

      <td>
        APPROVED
      </td>

      <td>
        No CVM information, but authorization was flagged as safe by the Acquirer/Network.
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
        VISA\_PROVISIONING\_VALIDATION\_REQUEST
      </td>

      <td>
        APPROVED
      </td>

      <td>
        No CVM information, but the authorization is a Visa Provisioning Validation request. (Visa only.
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
        RECURRING\_TRANSACTION\_WITH\_NO\_AUTH\_METHOD
      </td>

      <td>
        APPROVED
      </td>

      <td>
        No CVM information, but the transaction is Recurring.
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
        NO\_CVM\_TRANSACTION\_WITH\_NO\_AUTH\_METHOD
      </td>

      <td>
        APPROVED
      </td>

      <td>
        No CVM information, but the issuer enabled the NoCVM configuration to validate the authorization in the anti-fraud system.
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
        PRE\_AUTH\_TRANSACTION\_WITH\_NO\_AUTH\_METHOD
      </td>

      <td>
        APPROVED
      </td>

      <td>
        No CVM information, but the authorization was flagged as safe by the Acquirer/Network and is a pre-authorization. (Mastercard only).
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
        MANUAL\_ENTRY\_MODE\_TRANSACTION\_WITH\_NO\_AUTH\_METHOD
      </td>

      <td>
        APPROVED
      </td>

      <td>
        No CVM information, but the authorization was performed using PAN Manual Entry (Entry Mode = 01).
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
        HSM\_EMPTY\_RESPONSE
      </td>

      <td>
        SKIPPED
      </td>

      <td>
        No response from HSM.
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
        ENTRY\_MODE\_NOT\_ALLOWED\_WITH\_NO\_CVM
      </td>

      <td>
        REJECTED
      </td>

      <td>
        No CVM information and none of the NoCVM exceptions were met to approve this request.
      </td>

      <td>
        NCV
      </td>

      <td>
        * *Visa:*\* 5C
        * *Mastercard:* \*57
        * *TecBan:*\* 57
        * *RuPay:*\* 57
        * *ELO:*\* 57
      </td>
    </tr>

    <tr>
      <td>
        PIN\_INVALID
      </td>

      <td>
        REJECTED
      </td>

      <td>
        Request contained incorrect PIN.
      </td>

      <td>
        FR6
      </td>

      <td>
        * *Visa:*\* 55
        * \*Mastercard:\*\*55
        * *TecBan:*\* 55
        * *RuPay:*\* 55
        * *ELO:*\* 55
      </td>
    </tr>

    <tr>
      <td>
        CVV1\_INVALID
      </td>

      <td>
        REJECTED
      </td>

      <td>
        Request contained incorrect tracking data on Magnetic Stripe.
      </td>

      <td>
        FR1
      </td>

      <td>
        * *Visa:*\* 82
        * *Mastercard:*\* 63
        * *TecBan:*\* 57
        * *RuPay:*\* 05
        * *ELO:*\* 82
      </td>
    </tr>

    <tr>
      <td>
        CVV2\_INVALID
      </td>

      <td>
        REJECTED
      </td>

      <td>
        Request contained incorrect CVV2 information.
      </td>

      <td>
        FR2
      </td>

      <td>
        * \*Visa:\*\*N7
        * *Mastercard:*\* 63
        * *TecBan:*\* 57
        * *RuPay:*\* 05
        * *ELO:*\* 63
      </td>
    </tr>

    <tr>
      <td>
        SERVICE\_CODE\_INVALID
      </td>

      <td>
        REJECTED
      </td>

      <td>
        Internal Service Code to validate CVV was invalid or misconfigured.
      </td>

      <td>
        FR7
      </td>

      <td>
        * *Visa:*\* 14
        * *Mastercard:*\* 14
        * *TecBan:*\* 14
        * *RuPay:*\* 14
        * *ELO:*\* 14
      </td>
    </tr>

    <tr>
      <td>
        EXPIRATION\_DATE\_INVALID
      </td>

      <td>
        REJECTED
      </td>

      <td>
        Expiration date provided in the network message (input by the cardholder) was invalid.
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

    <tr>
      <td>
        INCOMPLETE\_TRANSACTION
      </td>

      <td>
        REJECTED
      </td>

      <td>
        Internal error on HSM response.
      </td>

      <td>
        OP1
      </td>

      <td>
        * *Visa:*\* 12
        * *Mastercard:*\* 30
        * *TecBan:*\* 30
        * *RuPay:*\* 30
        * *ELO:*\* 30
      </td>
    </tr>

    <tr>
      <td>
        GENERIC\_HSM\_ERROR
      </td>

      <td>
        REJECTED
      </td>

      <td>
        Unexpected error from HSM processing.
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

    <tr>
      <td>
        HSM\_UNKNOWN\_ERROR\_RESPONSE
      </td>

      <td>
        REJECTED
      </td>

      <td>
        Unknown error response from HSM processing.
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

**Additional data:** Not yet mapped

**Payload example:**

```json
{
    "name": "CVM",
    "status": "APPROVED",
    "reason": "PIN_AND_CVV_VALID",
    "description": "Pin and CVV are valid",
    "additional_data": {}
}
```

# Entry mode validation

The Pismo platform checks the card's cryptogram information to verify that the entry mode used in the request is allowed.

<Callout icon="📘" theme="info">
  This validation is performed for both zero balance and full balance integration.
</Callout>

**Name:** ENTRY\_MODE

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
        ENTRY\_MODE\_VALID
      </td>

      <td>
        APPROVED
      </td>

      <td>
        Entry mode is valid, based on the cryptogram information.
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
        TRANSACTION\_HAS\_NO\_CRYPTOGRAM
      </td>

      <td>
        REJECTED
      </td>

      <td>
        Entry mode is Chip (05), but there is no cryptogram information in the request.
      </td>

      <td>
        FRE
      </td>

      <td>
        * *Visa:*\* 63
        * *Mastercard:* \*57
        * *TecBan:*\* R9
        * *RuPay:*\* E3
        * *ELO:*\* 82
      </td>
    </tr>

    <tr>
      <td>
        TRANSACTION\_HAS\_CRYPTOGRAM
      </td>

      <td>
        REJECTED
      </td>

      <td>
        Entry mode is not Chip or Contactless, but the operation contains cryptogram information.
      </td>

      <td>
        FRE
      </td>

      <td>
        * *Visa:*\* 63
        * *Mastercard:*\* 57
        * *TecBan:*\* R9
        * *RuPay:*\* E3
        * *ELO:*\* 82
      </td>
    </tr>
  </tbody>
</Table>

**Additional data:** Not yet mapped

**Payload example:**

```json
{
    "name": "ENTRY_MODE",
    "status": "APPROVED",
    "reason": "ENTRY_MODE_VALID",
    "description": "Entry mode valid",
    "additional_data": {}
}
```

# Installments validation

This rule validates if there is a valid number of installments (greater than 1) when it is a installment purchase.

<Callout icon="📘" theme="info">
  This validation is performed for both zero balance and full balance integration.\
  This validation is specific to and performed only for ELO when the processing code is `15`.
</Callout>

**Name:** INSTALLMENTS

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
        INSTALLMENTS\_VALID
      </td>

      <td>
        APPROVED
      </td>

      <td>
        Installments are valid.
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
        INVALID\_INSTALLMENTS\_NUMBER
      </td>

      <td>
        REJECTED
      </td>

      <td>
        Invalid number of installments.
      </td>

      <td>
        OP1
      </td>

      <td>
        * *Visa:*\* 12
        * *Mastercard:* \*30
        * *TecBan:*\* 30
        * *RuPay:*\* 30
        * *ELO:*\* 30
      </td>
    </tr>

    <tr>
      <td>
        NOT\_INSTALLMENT\_TRANSACTION
      </td>

      <td>
        SKIPPED
      </td>

      <td>
        It is not an installment transaction.
      </td>

      <td>
        N/A
      </td>

      <td>
        N/A
      </td>
    </tr>
  </tbody>
</Table>

**Additional data:** Not yet mapped

**Payload example:**

```json
{
    "name": "INSTALLMENTS",
    "status": "APPROVED",
    "reason": "INSTALLMENTS_VALID",
    "description": "Installments are valid",
    "additional_data": {}
}
```

# DCC validation

This rule validates if it is a dynamic currency conversion (DCC) transaction and if the program allows this type of transaction. This validation is based on `disableDCC` config on the `NetworkTransactionsProgramsConfig` table.

<Callout icon="📘" theme="info">
  This validation is performed for both zero balance and full balance integration.
</Callout>

**Name:** DCC

**Possible statuses:** APPROVED, REJECTED, SKIPPED

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
        DCC\_TRANSACTION\_ALLOWED
      </td>

      <td>
        APPROVED
      </td>

      <td>
        DCC transaction allowed for program.
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
        DCC\_TRANSACTION\_NOT\_ALLOWED
      </td>

      <td>
        REJECTED
      </td>

      <td>
        DCC transaction not allowed for program.
      </td>

      <td>
        DCC
      </td>

      <td>
        * *Visa:*\* 5C
        * *Mastercard:* \*57
        * *TecBan:*\* 57
        * *RuPay:*\* 57
        * *ELO:*\* 57
      </td>
    </tr>

    <tr>
      <td>
        DCC\_INVALID\_COUNTRY
      </td>

      <td>
        REJECTED
      </td>

      <td>
        Invalid country for DCC definition.
      </td>

      <td>
        DIC
      </td>

      <td>
        * *Visa:*\* 5C
        * *Mastercard:* \*57
        * *TecBan:*\* 57
        * *RuPay:*\* 57
        * *ELO:*\* 57
      </td>
    </tr>

    <tr>
      <td>
        DCC\_INVALID\_CURRENCY
      </td>

      <td>
        REJECTED
      </td>

      <td>
        Invalid currency for DCC definition.
      </td>

      <td>
        DIY
      </td>

      <td>
        * *Visa:*\* 5C
        * *Mastercard:* \*57
        * *TecBan:*\* 57
        * *RuPay:*\* 57
        * *ELO:*\* 57
      </td>
    </tr>

    <tr>
      <td>
        NOT\_DCC\_TRANSACTION
      </td>

      <td>
        SKIPPED
      </td>

      <td>
        It is not a DCC transaction.
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
        DCC\_INVALID\_PROGRAM
      </td>

      <td>
        SKIPPED
      </td>

      <td>
        Invalid program for DCC definition.
      </td>

      <td>
        N/A
      </td>

      <td>
        N/A
      </td>
    </tr>
  </tbody>
</Table>

**Additional data:** The `additional_data` field provides comprehensive details about the DCC transaction, including the custom code, program ID, whether DCC is enabled, the program's currency and country codes, as well as the transaction's currency and merchant country codes.

**Fields:** `custom_code`, `program_id`, `is_dcc`, `is_disable_dcc_config`, `program_currency_code`, `program_country_code`, `transaction_currency_code`, `transaction_merchant_country_code`

**Payload example:**

```json
{
    "name": "DCC",
    "status": "APPROVED",
    "reason": "DCC_TRANSACTION_ALLOWED",
    "description": "DCC transaction not allowed for program 123",
    "additional_data": {
          "custom_code": "DCC",
          "program_id": 888,
          "is_dcc": true,
          "is_disable_dcc_config": true,
          "program_currency_code": "986",
          "program_country_code": "BRA",
          "transaction_currency_code": "986",
          "transaction_merchant_country_code": "USA"
  }
}
```

# Currency validation (deprecated)

This rule validates if it is a purchase using Brazilian currency outside Brazil.

<Callout icon="📘" theme="info">
  This validation is performed for both zero balance and full balance integration.
</Callout>

<Callout icon="📘" theme="info">
  This validation was deprecated and replaced by DCC validation.
</Callout>

**Name:** CURRENCY

**Possible statuses:** APPROVED, REJECTED

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
        CURRENCY\_ALLOWED
      </td>

      <td>
        APPROVED
      </td>

      <td>
        Purchase is not in Brazilian currency or it originates in Brazil.
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
        CURRENCY\_NOT\_ALLOWED
      </td>

      <td>
        REJECTED
      </td>

      <td>
        Purchase uses Brazilian currency, and it is for an international merchant.
      </td>

      <td>
        DCC
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

**Additional data:** Not yet mapped

**Payload example:**

```json
{
    "name": "CURRENCY",
    "status": "APPROVED",
    "reason": "CURRENCY_ALLOWED",
    "description": "Currency allowed",
    "additional_data": {}
}
```

# Terminal capability validation

The Pismo platform verifies that the POS terminal has the capability required for the entry mode.

<Callout icon="📘" theme="info">
  This validation is performed for both zero balance and full balance integration.
</Callout>

**Name:** TERMINAL\_CAPABILITY

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
        TERMINAL\_CAPABILITY\_VALID
      </td>

      <td>
        APPROVED
      </td>

      <td>
        Terminal has the capability to process the received entry mode.
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
        TERMINAL\_CAPABILITY\_UNKNOWN
      </td>

      <td>
        SKIPPED
      </td>

      <td>
        No mapping for the received terminal capability.
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
        TERMINAL\_CAPABILITY\_INVALID
      </td>

      <td>
        REJECTED
      </td>

      <td>
        Terminal doesn’t have the capability to process the received entry mode.
      </td>

      <td>
        FRH
      </td>

      <td>
        * *Visa:*\* 58
        * *Mastercard:*\* 58
        * *TecBan:*\* 58
        * *RuPay:*\* 58
        * *ELO:*\* 58
      </td>
    </tr>
  </tbody>
</Table>

**Additional data:** Not yet mapped

**Payload example:**

```json
{
    "name": "TERMINAL_CAPABILITY",
    "status": "APPROVED",
    "reason": "TERMINAL_CAPABILITY_VALID",
    "description": "Terminal capability is valid",
    "additional_data": {}
}
```

# Chip values validation

The Pismo platform checks that information like amount and country in the cryptogram field match the information in the authorization message.

<Callout icon="📘" theme="info">
  This validation is performed for both zero balance and full balance integration.
</Callout>

<Callout icon="📘" theme="info">
  This rule today is only applied to Visa processing.
</Callout>

**Name:** CHIP\_VALUES

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
        CHIP\_VALUES\_MATCH
      </td>

      <td>
        APPROVED
      </td>

      <td>
        ARQC information matched with authorization message information.
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
        PROCESSING\_CODE\_WITHDRAWAL
      </td>

      <td>
        SKIPPED
      </td>

      <td>
        Validation is skipped for withdrawals, because some values are expected to be different.
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
        TRANSACTION\_HAS\_NO\_CHIP
      </td>

      <td>
        SKIPPED
      </td>

      <td>
        Operation not being processed using Chip, so no need for this validation.
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
        CHIP\_TRANSACTION\_AMOUNT\_DOES\_NOT\_MATCH
      </td>

      <td>
        REJECTED
      </td>

      <td>
        Amount of the transaction is different from the amount of the transaction in the Chip Information.
      </td>

      <td>
        FRE
      </td>

      <td>
        * *Visa:*\* 63
        * *Mastercard:*\* 57
        * *TecBan:*\* R9
        * *RuPay:*\* E3
        * *ELO:*\* 82
      </td>
    </tr>

    <tr>
      <td>
        CHIP\_TRANSACTION\_COUNTRY\_DOES\_NOT\_MATCH
      </td>

      <td>
        REJECTED
      </td>

      <td>
        Country of the transaction is different from the country of the transaction in the Chip Information.
      </td>

      <td>
        FRE
      </td>

      <td>
        * *Visa:*\* 63
        * *Mastercard:*\* 57
        * *TecBan:*\* R9
        * *RuPay:*\* E3
        * *ELO:*\* 82
      </td>
    </tr>
  </tbody>
</Table>

**Additional data:** Not yet mapped

**Payload example:**

```json
{
    "name": "CHIP_VALUES",
    "status": "APPROVED",
    "reason": "CHIP_VALUES_MATCH",
    "description": "Chip values match",
    "additional_data": {}
}
```

# Chip signature validation

The Pismo platform checks that the verification method specified in the cryptogram data is valid. By default, the platform denies transactions that use Paper Signature as the validation method.

<Callout icon="📘" theme="info">
  This validation is performed for both zero balance and full balance integration.
</Callout>

**Name:** CHIP\_SIGNATURE

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
        CHIP\_SIGNATURE\_VALID
      </td>

      <td>
        APPROVED
      </td>

      <td>
        Validation method used is valid.
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
        NO\_CHIP\_SIGNATURE
      </td>

      <td>
        SKIPPED
      </td>

      <td>
        No chip information, so no need for this validation.
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
        CHIP\_SIGNATURE\_DEPRECATED
      </td>

      <td>
        REJECTED
      </td>

      <td>
        Transaction performed using Paper Signature as validation method.
      </td>

      <td>
        FR0
      </td>

      <td>
        * *Visa:*\* 82
        * *Mastercard:*\* 88
        * *TecBan:*\* R9
        * *RuPay:*\* 81
        * *ELO:*\* 82
      </td>
    </tr>
  </tbody>
</Table>

**Additional data:** Not yet mapped

**Payload example:**

```json
{
    "name": "CHIP_SIGNATURE",
    "status": "APPROVED",
    "reason": "CHIP_SIGNATURE_VALID",
    "description": "Chip signature valid",
    "additional_data": {}
}
```

# Message format validation

The Pismo platform validates if the message coming from the network has a valid format, domain, and values.

Currently, this validation is performed only for the ELO network.

<Callout icon="📘" theme="info">
  This validation is performed for both zero balance and full balance integration.
</Callout>

**Name:** MESSAGE\_FORMAT

**Possible statuses:** APPROVED, REJECTED

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
        VALID\_MESSAGE\_FORMAT
      </td>

      <td>
        APPROVED
      </td>

      <td>
        The message is valid.
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
        INVALID\_MESSAGE\_FORMAT
      </td>

      <td>
        REJECTED
      </td>

      <td>
        The message is invalid.
      </td>

      <td>
        IMF
      </td>

      <td>
        * *Visa:*\* 12 or 5C
        * *Mastercard:*\* 30
        * *TecBan:*\* 30
        * *RuPay:*\* 30
        * *ELO:*\* 30
      </td>
    </tr>
  </tbody>
</Table>

**Additional data:** Not yet mapped

**Payload example:**

```json
{
    "name": "MESSAGE_FORMAT",
    "status": "APPROVED",
    "reason": "VALID_MESSAGE_FORMAT",
    "description": "Message is valid",
    "additional_data": {}
}
```

# Valid card validation

The Pismo platform checks that the card number used for the authorization is registered in Pismo's internal database.

<Callout icon="📘" theme="info">
  This validation is performed for both zero balance and full balance integration.
</Callout>

**Name:** CARD\_EXISTS

**Possible statuses:** APPROVED, REJECTED

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
        CARD\_FOUND
      </td>

      <td>
        APPROVED
      </td>

      <td>
        Card found in the database.
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
        REJECTED
      </td>

      <td>
        Card not found in the database.
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

**Additional data:** `additional_data` contains the card type. This field is only filled in for APPROVED and REJECTED status scenarios.

**Payload example:**

```json
{
    "name": "CARD_EXISTS",
    "status": "APPROVED",
    "reason": "CARD_FOUND",
    "description": "Card exists.",
    "additional_data": {
      "type": "PLASTIC"
    }
}
```

# Valid card token validation

This rule only applies to authorizations that use tokens. The Pismo platform checks that the token used for the authorization is registered in Pismo's internal database.

<Callout icon="📘" theme="info">
  This validation is performed for both zero balance and full balance integration.
</Callout>

**Name:** CARD\_TOKEN

**Possible statuses:** APPROVED, REJECTED

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
        CARD\_FOUND
      </td>

      <td>
        APPROVED
      </td>

      <td>
        Valid card found in the database using the token.
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
        CARD\_TOKEN\_NOT\_FOUND
      </td>

      <td>
        REJECTED
      </td>

      <td>
        Token was not found in the database. The platform will try to get the card information based on the card hash (card number), but the authorization will be declined because the token is not registered.
      </td>

      <td>
        Z26
      </td>

      <td>
        * *Visa:*\* 5C
        * *Mastercard:*\* 14
        * *TecBan:*\* 57
        * *RuPay:*\* 57
        * *ELO:*\* 12
      </td>
    </tr>
  </tbody>
</Table>

**Additional data:** `additional_data` contains card token information.

**Fields:** `custom_code`, `tokenRequestor`, `token`

**Payload example:**

```json
{
    "name": "CARD_TOKEN",
    "status": "REJECTED",
    "reason": "CARD_TOKEN_NOT_FOUND",
    "description": "Card token not found.",
    "additional_data": {
       "custom_code": "Z26",
       "tokenRequestor": "23876743",
       "token": "87287343",
    }
}
```

# Token status validation

This rule only applies to authorizations that use tokens. The Pismo platform checks that the token used for the authorization is valid.

<Callout icon="📘" theme="info">
  This validation is performed for both zero balance and full balance integration.
</Callout>

**Name:** CARD\_TOKEN\_STATUS

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
        CARD\_TOKEN\_STATUS\_VALID
      </td>

      <td>
        APPROVED
      </td>

      <td>
        Token found and has status ACTIVE.
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
        Authorization is not Tokenized, or it is a credit voucher or payment authorization request.
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
        CARD\_TOKEN\_DEACTIVATED
      </td>

      <td>
        REJECTED
      </td>

      <td>
        Token has status DEACTIVATED.
      </td>

      <td>
        Z23
      </td>

      <td>
        * *Visa:*\* 5C
        * *Mastercard:*\* 57
        * *TecBan:*\* 57
        * *RuPay:*\* 57
        * *ELO:*\* 12
      </td>
    </tr>

    <tr>
      <td>
        CARD\_TOKEN\_FAILED
      </td>

      <td>
        REJECTED
      </td>

      <td>
        Token has status FAILED.
      </td>

      <td>
        Z29
      </td>

      <td>
        * *Visa:*\* 5C
        * *Mastercard:*\* 57
        * *TecBan:*\* 57
        * *RuPay:*\* 57
        * *ELO:*\* 12
      </td>
    </tr>

    <tr>
      <td>
        CARD\_TOKEN\_INACTIVE
      </td>

      <td>
        REJECTED
      </td>

      <td>
        Token has status INACTIVE.
      </td>

      <td>
        Z24
      </td>

      <td>
        * *Visa:*\* 5C
        * *Mastercard:*\* 57
        * *TecBan:*\* 57
        * *RuPay:*\* 57
        * *ELO:*\* 12
      </td>
    </tr>

    <tr>
      <td>
        CARD\_TOKEN\_SUSPENDED
      </td>

      <td>
        REJECTED
      </td>

      <td>
        Token has status SUSPENDED.
      </td>

      <td>
        Z22
      </td>

      <td>
        * *Visa:*\* 5C
        * *Mastercard:*\* 57
        * *TecBan:*\* 57
        * *RuPay:*\* 57
        * *ELO:*\* 12
      </td>
    </tr>

    <tr>
      <td>
        CARD\_TOKEN\_STATUS\_UNKNOWN
      </td>

      <td>
        REJECTED
      </td>

      <td>
        Token has a status that is not mapped by the authorization system, and it is different from ACTIVE.
      </td>

      <td>
        Z27
      </td>

      <td>
        * *Visa:*\* 5C
        * *Mastercard:*\* 57
        * *TecBan:*\* 57
        * *RuPay:*\* 57
        * *ELO:*\* 12
      </td>
    </tr>
  </tbody>
</Table>

**Additional data:** `additional_data` contains card token status information.

**Field:** `tokenStatus`

**Payload example:**

```json
{
    "name": "CARD_TOKEN_STATUS",
    "status": "APPROVED",
    "reason": "CARD_TOKEN_STATUS_VALID",
    "description": "Card token status: ACTIVE.",
    "additional_data": {
      "tokenStatus": "ACTIVE"
    }
}
```

# Fetch program

To process the authorization flow, the Pismo platform fetches the program to use its configurations. The program and its configurations are required and when they are not present or are not valid, the authorization request is declined.

<Callout icon="📘" theme="info">
  This validation is performed for both zero balance and full balance integration.
</Callout>

**Name:** PROGRAM

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
        PROGRAM\_FOUND
      </td>

      <td>
        APPROVED
      </td>

      <td>
        The program was found.
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
        If card was not found, there is no way to find out the program or account hence this validation can’t be performed.
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
        PROGRAM\_NOT\_FOUND
      </td>

      <td>
        REJECTED
      </td>

      <td>
        Program was not found.
      </td>

      <td>
        PRN
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
        PROGRAM\_GENERIC\_ERROR
      </td>

      <td>
        REJECTED
      </td>

      <td>
        An unexpected error has happened while fetching the program.
      </td>

      <td>
        PRE
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
        PROGRAM\_TIMEOUT
      </td>

      <td>
        REJECTED
      </td>

      <td>
        A timeout occurred while fetching program.
      </td>

      <td>
        PRT
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
        PROGRAM\_INVALID\_CURRENCY
      </td>

      <td>
        REJECTED
      </td>

      <td>
        Program has invalid currency code.
      </td>

      <td>
        PIC
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

**Additional data:** `additional_data` specifies the program ID.

**Field:** `program_id`

**Payload example:**

```json
{
    "name": "PROGRAM",
    "status": "APPROVED",
    "reason": "PROGRAM_FOUND",
    "description": "Program 123 found.",
    "additional_data": {
          "program_id": 888
    }
}
```

# Processing code definition

If the definition for the transaction processing code cannot be retrieved, the authorization request is declined.

<Callout icon="📘" theme="info">
  This validation is performed for both zero balance and full balance integration.
</Callout>

**Name:** PROCESSING\_CODE

**Possible statuses:** APPROVED, REJECTED

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
        PROCESSING\_CODE\_FOUND
      </td>

      <td>
        APPROVED
      </td>

      <td>
        Processing code was found.
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
        PROCESSING\_CODE\_GENERIC\_ERROR
      </td>

      <td>
        REJECTED
      </td>

      <td>
        Unexpected error occurred while calling the API that defines the processing code to be used.
      </td>

      <td>
        PCE
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
        PROCESSING\_CODE\_TIMEOUT
      </td>

      <td>
        REJECTED
      </td>

      <td>
        Timeout occurred while calling the API that defines the processing code to be used.
      </td>

      <td>
        PCT
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

**Additional data:** When the validation is REJECTED, the `additional_data` field contains the `custom_code` field with the custom rejection code. When the validation is APPROVED, the `additional_data` field provides details about the processing codes: `processing_code_by_network` contains card network codes and `processing_code_mapped` contains custom processing codes created by Pismo.

**FIELDS:**

When validation is REJECTED: `custom_code`

When validation is APPROVED: `processing_code_by_network`, `processing_code_mapped`

**Payload examples:**

```json
{
    "name": "PROCESSING_CODE",
    "status": "REJECTED",
    "reason": "PROCESSING_CODE_GENERIC_ERROR",
    "description": "Unexpected error performing processing code.",
    "additional_data": {
       "custom_code": "PCE"
    }
}
```

```json
{
        "name": "PROCESSING_CODE",
        "status": "APPROVED",
        "reason": "PROCESSING_CODE_FOUND",
        "description": "Processing code by network 00 and processing code mapped is 003100.",
        "additional_data": {
          "processing_code_by_network": "00",
          "processing_code_mapped": "003100"
        }
}
```

# Fetch authorization configuration

The Pismo platform retrieves the configuration related to the platform. This configuration is required. If not found, the authorization request is declined.

<Callout icon="📘" theme="info">
  This validation is performed for both zero balance and full balance integration.
</Callout>

**Name:** PLATFORM\_CONFIG

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
        PLATFORM\_CONFIG\_FOUND
      </td>

      <td>
        APPROVED
      </td>

      <td>
        Valid configuration  found.
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
        If card is not found, there is no way to find the platform or account, so validation can’t be performed.
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
        PLATFORM\_CONFIG\_NOT\_FOUND
      </td>

      <td>
        REJECTED
      </td>

      <td>
        Configuration not found.
      </td>

      <td>
        MPC
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
        PLATFORM\_CONFIG\_GENERIC\_ERROR
      </td>

      <td>
        REJECTED
      </td>

      <td>
        Unexpected error occurred while fetching the configurations.
      </td>

      <td>
        PCE
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
    "name": "PLATFORM_CONFIG",
    "status": "APPROVED",
    "reason": "PLATFORM_CONFIG_FOUND",
    "description": "Platform Config found.",
    "additional_data": {}
}
```

# Card mode validation

This rule applies to [combination cards](https://developers.pismo.io/pismo-docs/docs/cards-overview-1#create-a-combination-card-with-card-modes). The Pismo platform checks if the card has the mode enabled for the account type of the transaction. For example, purchases in credit mode are only approved if the card has the mode `Credit` enabled.

<Callout icon="📘" theme="info">
  This validation is performed for both zero balance and full balance integration.
</Callout>

**Name:** CARD\_MODE

**Possible statuses:** APPROVED, REJECTED

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
        CARD\_MODE\_VALID
      </td>

      <td>
        APPROVED
      </td>

      <td>
        Card mode is valid and enabled for the operation or the card is not a combination card with modes.
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
        CARD\_MODE\_INVALID
      </td>

      <td>
        REJECTED
      </td>

      <td>
        Card mode not enabled for  operation. For example, the purchase is in the credit mode, but the card has only the debit mode enabled.
      </td>

      <td>
        CMD
      </td>

      <td>
        * *Visa:*\* 5C
        * *Mastercard:*\* 57
        * *TecBan:*\* 57
        * \*RuPay:\*\*57 **ELO:**\
          57 (invalid mode)\
          AB (debit)\
          AC (credit)
      </td>
    </tr>
  </tbody>
</Table>

**Additional data:** `additional_data`  specifies the type of card mode.

**Field:** `mode_type`

**Payload example:**

```json
{
    "name": "CARD_MODE",
    "status": "APPROVED",
    "reason": "CARD_MODE_VALID",
    "description": "Valid card mode",
    "additional_data": {
          "mode_type": "CREDIT"
   }
}
```

# Card mode status validation

This rule is applied to cards issued as [combination cards with card modes](https://developers.pismo.io/pismo-docs/docs/cards-overview-1#create-a-combination-card-with-card-modes) (Mode type: COMBO). This validation checks if the card has the mode status enable based on the ACTIVE status. Otherwise, if the card mode is SUSPENDED or INACTIVE, the authorization will be denied.

Card mode status validation is independent of the card status, i.e. either one of them doesn’t change the other. This validation is performed for both Zero Balance and Full Balance Flow.

**Name:** CARD\_MODE\_STATUS

**Possible Status:** APPROVED, REJECTED, SKIPPED

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
        Response code
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        CARD\_MODE\_STATUS\_ACTIVE
      </td>

      <td>
        APPROVED
      </td>

      <td>
        Card mode status: ACTIVE
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
        CARD\_MODE\_STATUS\_DEBIT\_INACTIVE
      </td>

      <td>
        REJECTED
      </td>

      <td>
        Status with  INACTIVE mode
      </td>

      <td>
        CMD
      </td>

      <td>
        * *Visa:*\* 5C
        * *Mastercard:*\* 57
        * *TecBan:*\* 57
        * \*RuPay:\*\*57 **ELO:**\
          57 (invalid mode)\
          AB (debit)\
          AC (credit)
      </td>
    </tr>

    <tr>
      <td>
        CARD\_MODE\_STATUS\_DEBIT\_SUSPENDED
      </td>

      <td>
        REJECTED
      </td>

      <td>
        Status with SUSPENDED mode
      </td>

      <td>
        CMD
      </td>

      <td>
        * *Visa:*\* 5C
        * *Mastercard:*\* 57
        * *TecBan:*\* 57
        * \*RuPay:\*\*57 **ELO:**\
          57 (invalid mode)\
          AB (debit)\
          AC (credit)
      </td>
    </tr>

    <tr>
      <td>
        CARD\_MODE\_STATUS\_CREDIT\_INACTIVE
      </td>

      <td>
        REJECTED
      </td>

      <td>
        Status with INACTIVE  mode
      </td>

      <td>
        CMD
      </td>

      <td>
        * *Visa:*\* 5C
        * *Mastercard:*\* 57
        * *TecBan:*\* 57
        * \*RuPay:\*\*57 **ELO:**\
          57 (invalid mode)\
          AB (debit)\
          AC (credit)
      </td>
    </tr>

    <tr>
      <td>
        CARD\_MODE\_STATUS\_CREDIT\_SUSPENDED
      </td>

      <td>
        REJECTED
      </td>

      <td>
        Status with SUSPENDED  mode
      </td>

      <td>
        CMD
      </td>

      <td>
        * *Visa:*\* 5C
        * *Mastercard:*\* 57
        * *TecBan:*\* 57
        * \*RuPay:\*\*57 **ELO:**\
          57 (invalid mode)\
          AB (debit)\
          AC (credit)
      </td>
    </tr>

    <tr>
      <td>
        CARD\_MODE\_STATUS\_NOT\_FOUND
      </td>

      <td>
        REJECTED
      </td>

      <td>
        Statusless mode
      </td>

      <td>
        CMD
      </td>

      <td>
        * *Visa:*\* 5C
        * *Mastercard:*\* 57
        * *TecBan:*\* 57
        * \*RuPay:\*\*57 **ELO:**\
          57 (invalid mode)\
          AB (debit)\
          AC (credit)
      </td>
    </tr>

    <tr>
      <td>
        CARD\_MODE\_STATUS\_SKIPPED
      </td>

      <td>
        SKIPPED
      </td>

      <td>
        Card with mode type other than COMBO
      </td>

      <td>
        N/A
      </td>

      <td>
        N/A
      </td>
    </tr>
  </tbody>
</Table>

**Additional Data**: `additional_data` contains the card mode status. This field is only filled in for APPROVED and REJECTED scenarios.

**Fields:** `status`, `custom code`

**Payload example**

```json
{
  "name": "CARD_MODE_STATUS",
  "status": "APPROVED",
  "reason": "CARD_MODE_STATUS_ACTIVE",
  "description": "Card status: ACTIVE.",
  "additional_data": {}
}
```

# Contactless allowed validation

The Pismo platform checks to see if the contactless function is allowed for the card.

<Callout icon="📘" theme="info">
  This validation is performed for both zero balance and full balance integration.
</Callout>

**Name:** CONTACTLESS

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
        CONTACTLESS\_ENABLED
      </td>

      <td>
        APPROVED
      </td>

      <td>
        Contactless is enabled or the operation is not using contactless entry mode (07)
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
        CONTACTLESS\_DISABLED
      </td>

      <td>
        REJECTED
      </td>

      <td>
        Authorization has entry mode contactless (07), and this function is disabled for this card.
      </td>

      <td>
        UBN
      </td>

      <td>
        * *Visa:*\* 78
        * *Mastercard:*\* 57
        * *TecBan:*\* 57
        * *RuPay:*\* 57
        * *ELO:*\* 78
      </td>
    </tr>
  </tbody>
</Table>

**Additional data:** `additional_data` provides information related to the contactless feature, including whether it is enabled, the entry mode, and the presence of a token.

**Fields:** `is_contactless_enabled`, `entry_mode`, `is_token_present`

**Payload example:**

```json
{
        "name": "CONTACTLESS",
        "status": "APPROVED",
        "reason": "CONTACTLESS_ENABLED",
        "description": "Contactless enabled.",
        "additional_data": {
          "is_contactless_enabled": true,
          "entry_mode": "051",
          "is_token_present": false
        }
 }
```

# Account type validation

The account type must be valid for the card being used. For example, a credit card can’t process a request on a debit account.

<Callout icon="📘" theme="info">
  This validation is performed for both zero balance and full balance integration.
</Callout>

**Name:** ACCOUNT\_TYPE

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
        ACCOUNT\_TYPE\_VALID
      </td>

      <td>
        APPROVED
      </td>

      <td>
        Account type valid for card mode. (Authorization request is in credit mode and card is a credit card, or request is in debit mode and card is a debit card.)
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
        ACCOUNT\_TYPE\_INVALID
      </td>

      <td>
        REJECTED
      </td>

      <td>
        Account type invalid for card mode. (Authorization request is in credit mode but card is a debit card, or request is in debit mode but card is a credit card.)
      </td>

      <td>
        IAT
      </td>

      <td>
        * *Visa:*\* 5C
        * *Mastercard:*\* 57
        * *TecBan:*\* 57
        * \*RuPay:\*\*57 **ELO:**\
          AB (debit)\
          AC (credit)
      </td>
    </tr>
  </tbody>
</Table>

**Additional data:** `additional_data` contains account type field and card mode.

**Fields:** `account_type`, `card_mode`

**Payload example:**

```json
{
    "name": "ACCOUNT_TYPE",
    "status": "APPROVED",
    "reason": "ACCOUNT_TYPE_VALID",
    "description": "Account Type: CREDIT_CARD_ACCOUNT. Card Mode: CREDIT.",
    "additional_data": {
          "account_type": "CREDIT_CARD_ACCOUNT",
          "card_mode": "CREDIT"
        }
}
```

# Card ATC validation

ATC is the transaction counter present in the chip information of the card. Every time the cardholder performs a transaction using a POS that reads chip data, the counter is incremented. The Pismo platform compares the counter value received in the request with the ones registered in the database from previous authorizations. If the value is not duplicated and it is within an allowed range (configured by the issuer), the request is validated.

<Callout icon="📘" theme="info">
  This validation is performed for both zero balance and full balance integration.
</Callout>

**Name:** CARD\_ATC

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
        CARD\_ATC\_VALID
      </td>

      <td>
        APPROVED
      </td>

      <td>
        Request is not using chip data, or, if it is, the ATC is present in the request, is not duplicated, and is within the allowed range.
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
        CARD\_ATC\_INVALID
      </td>

      <td>
        REJECTED
      </td>

      <td>
        ATC is duplicated or is outside the allowed range.
      </td>

      <td>
        FAT
      </td>
<!-- source:end -->

## Lifecycle status

- `docs/card-issuing/rule-list.md`: updatedAt 2026-06-28T21:57:58.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- Source content contains MDX/HTML components (for example `<Table>`, `<HTMLBlock>`, `<Callout>`, `<details>`). They are preserved exactly as published; tables inside them were not converted to Markdown.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/card-issuing/rule-list.md` | body lines 276–3851 | https://developers.pismo.io/pismo-docs/docs/rule-list | `e0e226a5db7724ab…` | 2026-06-28T21:57:58.000Z |

## Related knowledge units

- `KU-CARD-cards-overview-1` — Cards management
