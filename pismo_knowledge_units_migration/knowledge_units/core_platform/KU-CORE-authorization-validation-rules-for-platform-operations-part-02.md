---
ku_id: KU-CORE-authorization-validation-rules-for-platform-operations-part-02
title: Authorization validation rules for platform operations (part 2 of 2)
category: core_platform
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/core-platform/authorization-validation-rules-for-platform-operations.md
  sha256: ef57f4790279dffc96fedb540663284dfd2f3955c41adb3708247e781731e286
  url: https://developers.pismo.io/pismo-docs/docs/authorization-validation-rules-for-platform-operations
  role: primary_guide
  updated_at: '2026-03-25T14:05:13.000Z'
operations: []
related_kus: []
grouping_rationale: single source page; split into parts because the page is very large
---

# Authorization validation rules for platform operations (part 2 of 2)

**KU ID:** `KU-CORE-authorization-validation-rules-for-platform-operations-part-02` · **Category:** Core platform · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) (one part of a large page) into one implementation-oriented unit. Grouping rationale: single source page; split into parts because the page is very large

Scope as stated in `docs/core-platform/authorization-validation-rules-for-platform-operations.md`:

> **Additional data:** Contains the card status.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/core-platform/authorization-validation-rules-for-platform-operations.md`: Currency validation; External calculation; Flex controls evaluation; Ledger integration; Merchant validation; Payment methods configuration retrieval; Payment methods acceptances retrieval; Payment methods integrity; Payment methods persistence; Operation amount calculation; Original authorization retrieval; Platform authentication; Platform authorization; Processing code mapping; Processing code type validation; Processing code validation; Program parameters retrieval; Program retrieval; Remaining cancellation balance

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/core-platform/authorization-validation-rules-for-platform-operations.md` lines 876–2314 of the body

Source URL: https://developers.pismo.io/pismo-docs/docs/authorization-validation-rules-for-platform-operations · updatedAt: 2026-03-25T14:05:13.000Z

<!-- source:begin path=docs/core-platform/authorization-validation-rules-for-platform-operations.md part=875-2314 -->
| Reason                               | Status   | Description                         | Denial code | Response code |
| :----------------------------------- | :------- | :---------------------------------- | :---------- | :------------ |
| CARD\_STATUS\_VALID                  | APPROVED | Card is in valid status.            | N/A         | 00            |
| CARD\_STATUS\_SKIPPED                | SKIPPED  | Card status validation was skipped. | N/A         | N/A           |
| CARD\_STATUS\_INVALID\_CREATED       | REJECTED | Card is in created status.          | CCD         | 57            |
| CARD\_STATUS\_UNBOUND                | REJECTED | Card is in unbound status.          | CUD         | 57            |
| CARD\_STATUS\_INVALID\_BLOCKED       | REJECTED | Card is in blocked status.          | CBD         | 57            |
| CARD\_STATUS\_INVALID\_WARNING       | REJECTED | Card is in warning status.          | CWD         | 57            |
| CARD\_STATUS\_INVALID\_PENDING       | REJECTED | Card is in pending status.          | CPD         | 57            |
| CARD\_STATUS\_INVALID\_LOST          | REJECTED | Card is in lost status.             | CLD         | 57            |
| CARD\_STATUS\_INVALID\_DELETED       | REJECTED | Card is in deleted status.          | CDD         | 57            |
| CARD\_STATUS\_INVALID\_CANCELED      | REJECTED | Card is in canceled status.         | CBC         | 57            |
| CARD\_STATUS\_INVALID\_ROBBED        | REJECTED | Card is in robbed status.           | CRD         | 57            |
| CARD\_STATUS\_INVALID\_EXPIRED       | REJECTED | Card is in expired status.          | CBE         | 57            |
| CARD\_STATUS\_BROKEN                 | REJECTED | Card is in broken status.           | CBD         | 57            |
| CARD\_STATUS\_INVALID\_DAMAGED       | REJECTED | Card is in damaged status.          | BCD         | 57            |
| CARD\_STATUS\_INVALID\_THEFT         | REJECTED | Card is in theft status.            | CTD         | 57            |
| CARD\_STATUS\_INVALID\_FRAUD         | REJECTED | Card is in fraud status.            | CFD         | 57            |
| CARD\_STATUS\_INVALID\_DEFECT        | REJECTED | Card is in defect status.           | BDD         | 57            |
| CARD\_STATUS\_INVALID\_CLIENT\_ORDER | REJECTED | Card is in client order status.     | CCO         | 57            |
| CARD\_STATUS\_INVALID\_UNRECEIVED    | REJECTED | Card is in unreceived status.       | BUD         | 57            |
| CARD\_STATUS\_INVALID\_INOPERATIVE   | REJECTED | Card is in inoperative status.      | CID         | 57            |
| CARD\_STATUS\_UNKNOWN                | REJECTED | Card is in unknown status.          | CBU         | 57            |

**Additional data:** Contains the card status.

**Fields:** `card_status`

**Payload example:**

```json
{
    "name": "CARD_STATUS",
    "status": "APPROVED",
    "reason": "CARD_STATUS_VALID",
    "description": "Card is in valid status.",
    "additional_data": {
        "card_status": "NORMAL"
    }
}
```

# Currency validation

Platform authorization has to perform a validation to determine the currency associated with the account ID of the authorization. The currency can be associated with the account or program level.

**Name:** CURRENCY

**Possible status:** APPROVED, SKIPPED, REJECTED

**Possible reasons:**

| Reason               | Status   | Description                            | Denial code | Response code |
| :------------------- | :------- | :------------------------------------- | :---------- | :------------ |
| CURRENCY\_FOUND      | APPROVED | Currency was found.                    | N/A         | 00            |
| CURRENCY\_SKIPPED    | SKIPPED  | Currency validation was skipped.       | N/A         | N/A           |
| CURRENCY\_NOT\_FOUND | REJECTED | Currency was not found.                | CEN         | 57            |
| CURRENCY\_ERROR      | REJECTED | Currency validation returned an error. | CER         | 96            |

**Additional data:** Contains the currency numeric and alphanumeric codes.

**Fields:** `code`, `numeric_code`

**Payload example:**

```json
{
    "name": "CURRENCY",
    "status": "APPROVED",
    "reason": "CURRENCY FOUNT",
    "description": "Currency was found.",
    "additional_data": {
	"code": "USD",
	"numeric_code": "840"
    }
}
```

# External calculation

If configured, the authorization request from the payment methods service calls an external endpoint to have the amounts of the authorization calculated by an external system. If any error occurs, the authorization is declined.

**Name:**  EXTERNAL\_CALCULATION

**Possible status:** APPROVED, SKIPPED, REJECTED

**Possible reasons:**

| Reason                                   | Status   | Description                                                      | Denial code | Response code |
| :--------------------------------------- | :------- | :--------------------------------------------------------------- | :---------- | :------------ |
| EXTERNAL\_CALCULATION\_SUCCESSFUL        | APPROVED | External calculation was performed successfully.                 | N/A         | 00            |
| EXTERNAL\_CALCULATION\_SKIPPED           | SKIPPED  | External calculation was skipped.                                | N/A         | N/A           |
| EXTERNAL\_CALCULATION\_ERROR             | REJECTED | Internal error when performing external calculation.             | ECE         | 92            |
| EXTERNAL\_CALCULATION\_TIMEOUT           | REJECTED | Timeout when attempting to perform external calculation request. | ECT         | 92            |
| EXTERNAL\_CALCULATION\_DECLINED          | REJECTED | External call declined calculation request.                      | ECD         | 57            |
| EXTERNAL\_CALCULATION\_INVALID\_RESPONSE | REJECTED | External calculation response has invalid values.                | ECI         | 92            |

**Additional data:** Contains the list of validation errors when the external system responds with an unexpected response format or missing required fields.

**Fields:** `response_status_code`, `error_1`, `error_2`, `error_n`

**Payload example:**

```json
{
    "name": "EXTERNAL_CALCULATION",
    "status": "APPROVED",
    "reason": "EXTERNAL_CALCULATION_SUCCESSFUL",
    "description": "External calculation was performed successfully."
}
```

# Flex controls evaluation

Platform authorization evaluates flex controls for the operation.

**Name:**  FLEX\_CONTROLS

**Possible status:** APPROVED, SKIPPED, REJECTED

**Possible reasons:**

| Reason                        | Status   | Description                                                   | Denial code | Response code |
| :---------------------------- | :------- | :------------------------------------------------------------ | :---------- | :------------ |
| FLEX\_CONTROLS\_APPROVED      | APPROVED | Authorization passed flex control evaluation.                 | N/A         | 00            |
| FLEX\_CONTROLS\_SKIPPED       | SKIPPED  | Flex controls evaluation was skipped.                         | N/A         | N/A           |
| FLEX\_CONTROLS\_NOT\_APPROVED | REJECTED | Authorization failed flex control evaluation.                 | FCD         | 57            |
| FLEX\_CONTROLS\_ERROR         | REJECTED | Internal error in the evaluation of flex controls.            | FCE         | 96            |
| UNEXPECTED\_ERROR             | REJECTED | Unexpected error happened while processing the authorization. | SED         | 96            |

**Additional data:** Not mapped yet.

**Payload example:**

```json
{
    "name": "FLEX_CONTROLS",
    "status": "APPROVED",
    "reason": "FLEX_CONTROLS_APPROVED",
    "description": "Authorization passed flex control evaluation."
}
```

# Ledger integration

Platform authorization integrates with Ledger API to evaluate impact on account limits for this operation.

**Name:**  LEDGER

**Possible status:** APPROVED, SKIPPED, REJECTED

**Possible reasons:**

| Reason                           | Status   | Description                                                        | Denial code | Response code |
| :------------------------------- | :------- | :----------------------------------------------------------------- | :---------- | :------------ |
| LEDGER\_APPROVED                 | APPROVED | Ledger was impacted successfully.                                  | N/A         | 00            |
| LEDGER\_SKIPPED                  | SKIPPED  | Ledger impacting was skipped.                                      | N/A         | N/A           |
| LEDGER\_INSUFFICIENT\_FUNDS      | REJECTED | Amount authorization is greater than the account available limits. | PLD         | 51            |
| LEDGER\_NOT\_ALLOWED\_OPERATION  | REJECTED | Account is blocked from receiving debits or credits.               | PLO         | 57            |
| LEDGER\_DUPLICATED\_TRACKING\_ID | REJECTED | Internal error of duplicated tracking ID in the ledger.            | PLE         | 96            |
| LEDGER\_ERROR                    | REJECTED | Internal error in impacting ledger.                                | PLE         | 96            |
| UNEXPECTED\_ERROR                | REJECTED | Unexpected error happened while processing the authorization.      | SED         | 96            |

**Additional data:** Contains the force flag when calling the ledger force flow and `ignore_status` when impacting the ledger normal flow without validating the account status.

**Fields:** `force`, `ignore_status`

**Payload example:**

```json
{
    "name": "LEDGER",
    "status": "APPROVED",
    "reason": "LEDGER_APPROVED",
    "description": "Ledger was impacted successfully.",
    "additional_data": {
    	"force": true
    	}
    }
}
```

# Merchant validation

To complete an authorization request, the authorization request from the payment methods service calls the merchants API to validate if the merchant can authorize transactions, which is when their status is ACTIVE or APPROVED.

**Name:**  MERCHANT

**Possible status:** APPROVED, SKIPPED, REJECTED

**Possible reasons:**

| Reason                               | Status   | Description                                                 | Denial code | Response code |
| :----------------------------------- | :------- | :---------------------------------------------------------- | :---------- | :------------ |
| MERCHANT\_VALID\_STATUS              | APPROVED | Merchant has valid status.                                  | N/A         | 00            |
| MERCHANT\_SKIPPED                    | SKIPPED  | Merchant validation was skipped.                            | N/A         | N/A           |
| MERCHANT\_INVALID\_STATUS            | REJECTED | Merchant has invalid status.                                | IMD         | 57            |
| MERCHANT\_NOT\_FOUND                 | REJECTED | Merchant was not found.                                     | MNF         | 57            |
| MERCHANT\_MISSING\_MANDATORY\_FIELDS | REJECTED | Missing mandatory fields for performing merchant validation | MMF         | 57            |
| MERCHANT\_ERROR                      | REJECTED | Internal error validating merchant.                         | SED         | 96            |

**Additional data:** Contains the merchant external ID (`external_id` provided by the customer, not the Pismo internal ID) and status.

**Fields:** `merchant_external_id` (external ID provided by the customer, not Pismo internal ID), `status`, `marketplace_id`

**Payload example:**

```json
{
    "name": "MERCHANT",
    "status": "APPROVED",
    "reason": "MERCHANT_VALID_STATUS",
    "description": "Merchant has valid status.",
    "additional_data": {
        "merchant_external_id": "FL-123456",
        "status": "ACTIVE",
        "marketplace_id": "102030"
    }
}
```

# Payment methods configuration retrieval

For every authorization request from the payment methods service, the platform retrieves the configurations related to the account/program/organization performing the request. If anything unexpected happens during this flow, the request may be declined.

**Name:** CONFIG

**Possible status:** APPROVED, SKIPPED, REJECTED

**Possible reasons:**

| Reason             | Status   | Description                                              | Denial code | Response code |
| :----------------- | :------- | :------------------------------------------------------- | :---------- | :------------ |
| CONFIG\_FOUND      | APPROVED | Payment methods configuration was found.                 | N/A         | 00            |
| CONFIG\_SKIPPED    | SKIPPED  | Payment methods configuration validation was skipped.    | N/A         | N/A           |
| CONFIG\_NOT\_FOUND | REJECTED | Payment methods configuration was not found.             | CNF         | 57            |
| CONFIG\_ERROR      | REJECTED | Internal error validating payment methods configuration. | SED         | 96            |

**Additional data:** Not mapped yet.

**Payload example:**

```json
{
    "name": "CONFIG",
    "status": "APPROVED",
    "reason": "CONFIG_FOUND",
    "description": "Payment methods configuration was found."
}
```

# Payment methods acceptances retrieval

For every authorization request from the payment methods service, the platform retrieves the acceptances related to the account, program, and organization and processing code performing the request. If anything unexpected happens during this flow, the request may be declined.

**Name:** ACCEPTANCE

**Possible status:** APPROVED, SKIPPED, REJECTED

**Possible reasons:**

| Reason                 | Status   | Description                                            | Denial code | Response code |
| :--------------------- | :------- | :----------------------------------------------------- | :---------- | :------------ |
| ACCEPTANCE\_FOUND      | APPROVED | Payment methods acceptances were found.                | N/A         | 00            |
| ACCEPTANCE\_SKIPPED    | SKIPPED  | Payment methods acceptances validation was skipped.    | N/A         | N/A           |
| ACCEPTANCE\_NOT\_FOUND | REJECTED | Payment methods acceptances were not found.            | AND         | 57            |
| ACCEPTANCE\_ERROR      | REJECTED | Internal error validating payment methods acceptances. | SED         | 96            |

**Additional data:** Not mapped yet.

**Payload example:**

```json
{
    "name": "ACCEPTANCE",
    "status": "APPROVED",
    "reason": "ACCEPTANCE_FOUND",
    "description": "Payment methods acceptances were found."
}
```

# Payment methods integrity

Payment methods flow saves an integrity message to process the integrity validation of the flow later. If this operation fails to register the integrity message, the request is declined.

**Name:** PAYMENT\_METHODS\_INTEGRITY

**Possible status:** APPROVED, REJECTED

**Possible reasons:**

| Reason                               | Status   | Description                                                                   | Denial code | Response code |
| :----------------------------------- | :------- | :---------------------------------------------------------------------------- | :---------- | :------------ |
| PAYMENT\_METHODS\_INTEGRITY\_CREATED | APPROVED | Payment methods integrity message was created successfully.                   | N/A         | 00            |
| PAYMENT\_METHODS\_INTEGRITY\_ERROR   | REJECTED | Unexpected error happened while saving the payment methods integrity message. | OIE         | 96            |

**Additional data:** Not mapped yet.

**Payload example:**

```json
{
    "name": "PAYMENT_METHODS_INTEGRITY",
    "status": "APPROVED",
    "reason": "PAYMENT_METHODS_INTEGRITY_CREATED",
    "description": "Payment methods integrity message was created successfully."
}
```

# Payment methods persistence

Payment methods flow saves the request and response information in the persistence record to guarantee integrity of the flow. If this operation fails to register the information into the database, the request is declined.

**Name:** PAYMENT\_METHODS\_PERSISTENCE

**Possible status:** APPROVED, REJECTED

**Possible reasons:**

| Reason                                 | Status   | Description                                                                    | Denial code | Response code |
| :------------------------------------- | :------- | :----------------------------------------------------------------------------- | :---------- | :------------ |
| PAYMENT\_METHODS\_PERSISTENCE\_CREATED | APPROVED | Payment methods persistence record was created successfully.                   | N/A         | 00            |
| PAYMENT\_METHODS\_PERSISTENCE\_ERROR   | REJECTED | Unexpected error happened while saving the payment methods persistence record. | OPE         | 96            |

**Additional data:** Not mapped yet.

**Payload example:**

```json
{
    "name": "PAYMENT_METHODS_PERSISTENCE",
    "status": "APPROVED",
    "reason": "PAYMENT_METHODS_PERSISTENCE_CREATED",
    "description": "Payment methods persistence record was created successfully."
}
```

# Operation amount calculation

Platform authorization calls the Rates API to calculate the contract amount including taxes and fees on this authorization. If any error occurs, the request is declined.

**Name:**  RATES

**Possible status:** APPROVED, SKIPPED, REJECTED

**Possible reasons:**

| Reason                | Status   | Description                                       | Denial code | Response code |
| :-------------------- | :------- | :------------------------------------------------ | :---------- | :------------ |
| RATES\_APPROVED       | APPROVED | Rates calculation was performed.                  | N/A         | 00            |
| RATES\_SKIPPED        | SKIPPED  | Rates calculation was skipped.                    | N/A         | N/A           |
| RATES\_ERROR          | REJECTED | Internal error in calculating rates.              | PRE         | 96            |
| RATES\_LOGICAL\_ERROR | REJECTED | Non-internal/business error in calculating rates. | PRL         | 57            |

**Additional data:** Not mapped yet.

**Payload example:**

```json
{
    "name": "RATES",
    "status": "APPROVED",
    "reason": "RATES_APPROVED",
    "description": "Rates calculation was performed."
}
```

# Original authorization retrieval

Platform authorization retrieves the original authorization and performs validations.

**Name:**  ORIGINAL\_AUTHORIZATION

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
        Denial code
      </th>

      <th>
        Response code
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        ORIGINAL\_AUTHORIZATION

        * APPROVED
      </td>

      <td>
        APPROVED
      </td>

      <td>
        Original authorization validation was approved.
      </td>

      <td>
        N/A
      </td>

      <td>
        00
      </td>
    </tr>

    <tr>
      <td>
        ORIGINAL\_AUTHORIZATION

        * SKIPPED
      </td>

      <td>
        SKIPPED
      </td>

      <td>
        Original authorization validation was skipped.
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
        ORIGINAL\_AUTHORIZATION

        * NOT\_FOUND
      </td>

      <td>
        REJECTED
      </td>

      <td>
        Original authorization was not found.
      </td>

      <td>
        POA
      </td>

      <td>
        57
      </td>
    </tr>

    <tr>
      <td>
        ORIGINAL\_AUTHORIZATION

        * IS\_DENIED
      </td>

      <td>
        REJECTED
      </td>

      <td>
        Original authorization is denied and therefore can not be cancelled.
      </td>

      <td>
        POA
      </td>

      <td>
        57
      </td>
    </tr>

    <tr>
      <td>
        ORIGINAL\_AUTHORIZATION

        * IS\_FROM\_DIFFERENT\_ACCOUNT
      </td>

      <td>
        REJECTED
      </td>

      <td>
        Original authorization is from a different account.
      </td>

      <td>
        POA
      </td>

      <td>
        57
      </td>
    </tr>

    <tr>
      <td>
        ORIGINAL\_AUTHORIZATION

        * IS\_UNABLE\_TO\_CONFIRM
      </td>

      <td>
        REJECTED
      </td>

      <td>
        Original authorization is not pending.
      </td>

      <td>
        POA
      </td>

      <td>
        57
      </td>
    </tr>

    <tr>
      <td>
        ORIGINAL\_AUTHORIZATION

        * HAS\_DIFFERENT\_CONFIGURATION
      </td>

      <td>
        REJECTED
      </td>

      <td>
        Original authorization has different configuration.
      </td>

      <td>
        POA
      </td>

      <td>
        57
      </td>
    </tr>

    <tr>
      <td>
        ORIGINAL\_AUTHORIZATION\_ERROR
      </td>

      <td>
        REJECTED
      </td>

      <td>
        Internal error validating original authorization.
      </td>

      <td>
        POA
      </td>

      <td>
        96
      </td>
    </tr>

    <tr>
      <td>
        UNEXPECTED\_ERROR
      </td>

      <td>
        REJECTED
      </td>

      <td>
        Unexpected error happened while processing the authorization.
      </td>

      <td>
        SED
      </td>

      <td>
        96
      </td>
    </tr>

    <tr>
      <td>
        ORIGINAL\_AUTHORIZATION

        * IS\_NOT\_PENDING
      </td>

      <td>
        REJECTED
      </td>

      <td>
        Original authorization is not pending and therefore can not be incremented.
      </td>

      <td>
        POA
      </td>

      <td>
        57
      </td>
    </tr>

    <tr>
      <td>
        ORIGINAL\_AUTHORIZATION

        * DIFFERENT\_PROCESSING\_CODE
      </td>

      <td>
        REJECTED
      </td>

      <td>
        Original authorization has different processing code and therefore can not be incremented.
      </td>

      <td>
        POA
      </td>

      <td>
        57
      </td>
    </tr>

    <tr>
      <td>
        ORIGINAL\_AUTHORIZATION

        * DIFFERENT\_CLEARING\_TYPE
      </td>

      <td>
        REJECTED
      </td>

      <td>
        Original authorization has different clearing type and therefore can not be incremented.
      </td>

      <td>
        POA
      </td>

      <td>
        57
      </td>
    </tr>

    <tr>
      <td>
        ORIGINAL\_AUTHORIZATION

        * DIFFERENT\_CURRENCY
      </td>

      <td>
        REJECTED
      </td>

      <td>
        Original authorization has different currency and therefore can not be incremented.
      </td>

      <td>
        POA
      </td>

      <td>
        57
      </td>
    </tr>

    <tr>
      <td>
        ORIGINAL\_AUTHORIZATION

        * DIFFERENT\_NUMBER\_OF\_INSTALLMENTS
      </td>

      <td>
        REJECTED
      </td>

      <td>
        Original authorization has different number of installments and therefore can not be incremented.
      </td>

      <td>
        POA
      </td>

      <td>
        57
      </td>
    </tr>

    <tr>
      <td>
        ORIGINAL\_AUTHORIZATION

        * WITH\_EXTERNAL\_CALCULATION
      </td>

      <td>
        REJECTED
      </td>

      <td>
        Original authorization is calculated externally and therefore can not be incremented.
      </td>

      <td>
        POA
      </td>

      <td>
        57
      </td>
    </tr>

    <tr>
      <td>
        INCREMENTAL\_AUTHORIZATION

        * WITH\_EXTERNAL\_CALCULATION
      </td>

      <td>
        REJECTED
      </td>

      <td>
        Incremental authorization is calculated externally and therefore can not increment.
      </td>

      <td>
        POA
      </td>

      <td>
        57
      </td>
    </tr>

    <tr>
      <td>
        MULTIPlE\_CONFIRMATION\_WITH

        * EXTERNAL\_CALCULATION
      </td>

      <td>
        REJECTED
      </td>

      <td>
        Multiple confirmation is calculated externally and cannot be confirmed.
      </td>

      <td>
        POA
      </td>

      <td>
        57
      </td>
    </tr>

    <tr>
      <td>
        MULTIPlE\_CONFIRMATION\_ORIGINAL

        * AUTHORIZATION\_WITH\_EXTERNAL\_CALCULATION
      </td>

      <td>
        REJECTED
      </td>

      <td>
        Original authorization has different number of installments and cannot be confirmed.
      </td>

      <td>
        POA
      </td>

      <td>
        57
      </td>
    </tr>

    <tr>
      <td>
        MULTIPlE\_CONFIRMATION\_ORIGINAL

        * AUTHORIZATION\_DIFFERENT
        * NUMBER\_OF\_INSTALLMENTS
      </td>

      <td>
        REJECTED
      </td>

      <td>
        Original authorization is calculated externally and cannot be confirmed.
      </td>

      <td>
        POA
      </td>

      <td>
        57
      </td>
    </tr>
  </tbody>
</Table>

**Additional data:** Not mapped yet.

**Payload example:**

```json
{
    "name": "ORIGINAL_AUTHORIZATION",
    "status": "APPROVED",
    "reason": "ORIGINAL_AUTHORIZATION_APPROVED",
    "description": "Original authorization validation was approved."
}
```

# Platform authentication

Payment methods flow supports external integration to have the request authenticated against an external provider. If authentication is enabled and the information related to this is sent into the request payload, Payment methods API calls the external provider to validate this information. The result of this validation is attached to the validation result map on this entry.

If the platform does not authenticate and decline the request, it does not add an entry to the validation result map, since the flow is stopped and the request receives the 401 - Unauthorized HTTP response.

**Name:** PLATFORM\_AUTHENTICATION

**Possible status:** APPROVED, SKIPPED

**Possible reasons:**

| Reason                                    | Status   | Description                                                                             | Denial code | Response code |
| :---------------------------------------- | :------- | :-------------------------------------------------------------------------------------- | :---------- | :------------ |
| PLATFORM\_AUTHENTICATION\_SUCCESSFUL      | APPROVED | Request was authenticated successfully.                                                 | N/A         | 00            |
| PLATFORM\_AUTHENTICATION\_SKIPPED         | SKIPPED  | Platform authentication call was skipped.                                               | N/A         | N/A           |
| PLATFORM\_AUTHENTICATION\_FAILED\_SKIPPED | SKIPPED  | Platform authentication validation has failed but it was not required for this request. | N/A         | N/A           |

**Additional data:** Not mapped yet.

**Payload example:**

```json
{
    "name": "PLATFORM_AUTHENTICATION",
    "status": "APPROVED",
    "reason": "PLATFORM_AUTHENTICATION_SUCCESSFUL",
    "description": "Request was authenticated successfully."
}
```

# Platform authorization

To complete an authorization request, the authorization request from the payment methods service calls the platform authorization flow that performs all platform validations, such as ledger, rates, flex controls, and anti-fraud. If an error occurs during this call, the request is declined.

**Name:**  PLATFORM\_AUTHORIZATION

**Possible status:** APPROVED, REJECTED

**Possible reasons:**

| Reason                                            | Status   | Description                                                                                 | Denial code | Response code |
| :------------------------------------------------ | :------- | :------------------------------------------------------------------------------------------ | :---------- | :------------ |
| PLATFORM\_AUTHORIZATION\_SUCCESSFUL               | APPROVED | Platform authorization was processed successfully.                                          | N/A         | 00            |
| PLATFORM\_AUTHORIZATION\_ERROR                    | REJECTED | Platform authorization call returned an error.                                              | PAE         | 96            |
| PLATFORM\_AUTHORIZATION\_TIMEOUT                  | REJECTED | Timeout when attempting to perform platform authorization request.                          | PAT         | 96            |
| PLATFORM\_AUTHORIZATION\_DUPLICATED\_TRACKING\_ID | REJECTED | Platform authorization responded an idempotent response since tracking ID was already used. | PAD         | 30            |

**Additional data:** Not mapped yet.

**Payload example:**

```json
{
    "name": "PLATFORM_AUTHORIZATION",
    "status": "REJECTED",
    "reason": "PLATFORM_AUTHORIZATION_ERROR",
    "description": "Platform authorization call returned an error."
}
```

# Processing code mapping

Payment methods flow integrates processing code API to map the correct processing code to the authorization. This allows you to create mapping rules where the processing code received may be changed into a new one to have a specific mapping for each necessary scenario.

**Name:** PROCESSING\_CODE\_MAPPER

**Possible status:** APPROVED, SKIPPED, REJECTED

**Possible reasons:**

| Reason                             | Status   | Description                              | Denial code | Response code |
| :--------------------------------- | :------- | :--------------------------------------- | :---------- | :------------ |
| PROCESSING\_CODE\_MAPPED           | APPROVED | Processing code was mapped successfully. | N/A         | 00            |
| PROCESSING\_CODE\_MAPPING\_SKIPPED | SKIPPED  | Processing code mapping was skipped.     | N/A         | N/A           |
| PROCESSING\_CODE\_MAPPING\_ERROR   | REJECTED | Internal error mapping processing code.  | PCO         | 96            |

**Additional data:** Contains the original processing code received on the request and the mapped processing code that is returned after mapping (this may be the same processing code as the received one if no rule is configured).

**Fields:** `original_processing_code`, `mapped_processing_code`

**Payload example:**

```json
{
    "name": "PROCESSING_CODE_MAPPER",
    "status": "APPROVED",
    "reason": "PROCESSING_CODE_MAPPED",
    "description": "Processing code was mapped successfully.",
    "additional_data": {
        "original_processing_code": "00",
        "mapped_processing_code": "003000"
    }
}
```

# Processing code type validation

Platform authorization validates whether the processing code has a valid balance impact type of credit, debit, or zero balance. If it is an invalid type, the request is declined.

**Name:** PROCESSING\_CODE\_TYPE

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
        Denial code
      </th>

      <th>
        Response code
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        PROCESSING\_CODE\_TYPE\_VALID
      </td>

      <td>
        APPROVED
      </td>

      <td>
        Processing code has a valid balance impact type.
      </td>

      <td>
        N/A
      </td>

      <td>
        00
      </td>
    </tr>

    <tr>
      <td>
        PROCESSING\_CODE\_TYPE\_SKIPPED
      </td>

      <td>
        SKIPPED
      </td>

      <td>
        Processing code balance impact type validation was skipped.
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
        PROCESSING\_CODE\_TYPE\_INVALID
      </td>

      <td>
        REJECTED
      </td>

      <td>
        Processing code has an invalid balance impact type.
      </td>

      <td>
        PCD
      </td>

      <td>
        57
      </td>
    </tr>

    <tr>
      <td>
        REVERSAL\_PROCESSING\_CODE

        * INVALID\_BALANCE\_IMPACT
      </td>

      <td>
        REJECTED
      </td>

      <td>
        Processing code has a different balance impact than original authorization.
      </td>

      <td>
        PCD
      </td>

      <td>
        57
      </td>
    </tr>

    <tr>
      <td>
        PROCESSING\_CODE\_HAS\_DIFFERENT

        * IMPACT\_THAN\_ORIGINAL\_AUTHORIZATION
      </td>

      <td>
        REJECTED
      </td>

      <td>
        Processing code has a different balance impact than original authorization.
      </td>

      <td>
        PCD
      </td>

      <td>
        57
      </td>
    </tr>

    <tr>
      <td>
        PROCESSING\_CODE\_TYPE

        * NOT\_PERMITTED
      </td>

      <td>
        REJECTED
      </td>

      <td>
        Processing code type is not permitted.
      </td>

      <td>
        PCD
      </td>

      <td>
        57
      </td>
    </tr>
  </tbody>
</Table>

**Additional data:** Not mapped yet.

**Payload example:**

```json
{
    "name": "PROCESSING_CODE_TYPE",
    "status": "APPROVED",
    "reason": "PROCESSING_CODE_TYPE_VALID",
    "description": "Processing code has a valid balance impact type."
}
```

# Processing code validation

Platform authorization validates if the processing code is valid.

**Name:**  PROCESSING\_CODE

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
        Denial code
      </th>

      <th>
        Response code
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
        00
      </td>
    </tr>

    <tr>
      <td>
        PROCESSING\_CODE\_SKIPPED
      </td>

      <td>
        SKIPPED
      </td>

      <td>
        Processing code validation was skipped.
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
        PROCESSING\_CODE\_ERROR
      </td>

      <td>
        REJECTED
      </td>

      <td>
        Internal error validating processing code.
      </td>

      <td>
        PCE
      </td>

      <td>
        96
      </td>
    </tr>

    <tr>
      <td>
        PROCESSING\_CODE\_NOT\_FOUND
      </td>

      <td>
        REJECTED
      </td>

      <td>
        Processing code was not found.
      </td>

      <td>
        PCD
      </td>

      <td>
        57
      </td>
    </tr>

    <tr>
      <td>
        UNEXPECTED\_ERROR
      </td>

      <td>
        REJECTED
      </td>

      <td>
        Unexpected error happened while processing the authorization.
      </td>

      <td>
        SED
      </td>

      <td>
        96
      </td>
    </tr>

    <tr>
      <td>
        PROCESSING\_CODE\_STATUS

        * NOT\_PERMITTED
      </td>

      <td>
        REJECTED
      </td>

      <td>
        Processing code status is not permitted.
      </td>

      <td>
        PCD
      </td>

      <td>
        57
      </td>
    </tr>
  </tbody>
</Table>

**Additional data:** Not mapped yet.

**Payload example:**

```json
{
    "name": "PROCESSING_CODE",
    "status": "APPROVED",
    "reason": "PROCESSING_CODE_FOUND",
    "description": "Processing code was found."
}
```

# Program parameters retrieval

To perform card password tries and card ATC validations, the platform needs to retrieve program parameters. If something goes wrong with this retrieval, the authorization may be denied.

**Name:**  PROGRAM\_PARAMETER

**Possible status:** APPROVED, SKIPPED, REJECTED

**Possible reasons:**

| Reason                      | Status   | Description                                   | Denial code | Response code |
| :-------------------------- | :------- | :-------------------------------------------- | :---------- | :------------ |
| PROGRAM\_PARAMETER\_FOUND   | APPROVED | Program parameters were found successfully.   | N/A         | 00            |
| PROGRAM\_PARAMETER\_SKIPPED | SKIPPED  | Program parameters validation was skipped.    | N/A         | N/A           |
| PROGRAM\_PARAMETER\_ERROR   | REJECTED | Internal error validating program parameters. | PPE         | 96            |

**Additional data:** Contains the program ID related to this request.

**Fields:** `program_id`

**Payload example:**

```json
{
    "name": "PROGRAM_PARAMETER",
    "status": "APPROVED",
    "reason": "PROGRAM_PARAMETER_FOUND",
    "description": "Program parameters were found successfully.",
    "additional_data": {
        "program_id": 99
    }
}
```

# Program retrieval

Platform authorization retrieves the program information to process this authorization request and make some validations.

**Name:**  PROGRAM

**Possible status:** APPROVED, SKIPPED, REJECTED

**Possible reasons:**

| Reason              | Status   | Description                                                   | Denial code | Response code |
| :------------------ | :------- | :------------------------------------------------------------ | :---------- | :------------ |
| PROGRAM\_FOUND      | APPROVED | Program was found.                                            | N/A         | 00            |
| PROGRAM\_SKIPPED    | SKIPPED  | Program validation was skipped.                               | N/A         | N/A           |
| PROGRAM\_NOT\_FOUND | REJECTED | Program was not found.                                        | PPN         | 57            |
| PROGRAM\_ERROR      | REJECTED | Internal error validating program.                            | PPE         | 96            |
| UNEXPECTED\_ERROR   | REJECTED | Unexpected error happened while processing the authorization. | SED         | 96            |

**Additional data:** Not mapped yet.

**Payload example:**

```json
{
    "name": "PROGRAM",
    "status": "APPROVED",
    "reason": "PROGRAM_FOUND",
    "description": "Program was found."
}
```

# Remaining cancellation balance

Platform authorization retrieves the remaining cancellation balance and performs validations.

**Name:**  REMAINING\_CANCELLATION\_BALANCE

**Possible status:** APPROVED, SKIPPED, REJECTED

**Possible reasons:**

| Reason                                                          | Status   | Description                                                                                                                                               | Denial code | Response code |
| :-------------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------- | :------------ |
| REMAINING\_CANCELLATION\_BALANCE\_APPROVED                      | APPROVED | Remaining cancellation balance for this authorization was approved.                                                                                       | N/A         | 00            |
| REMAINING\_CANCELLATION\_BALANCE\_SKIPPED                       | SKIPPED  | Remaining cancellation balance for this authorization was skipped.                                                                                        | N/A         | N/A           |
| CANNOT\_PARTIALLY\_CANCEL\_AUTHORIZATION\_PENDING\_CONFIRMATION | REJECTED | Original authorization is pending confirmation and therefore can not be partially cancelled.                                                              | PRC         | 57            |
| AUTHORIZATION\_ALREADY\_CANCELLED                               | REJECTED | Authorization was already cancelled.                                                                                                                      | PRC         | 57            |
| TOTAL\_CANCELLATION\_BALANCE\_EXCEEDS\_AUTHORIZED               | REJECTED | Total cancellation balance exceeds the authorized amount.                                                                                                 | PRC         | 57            |
| REMAINING\_CANCELLATION\_BALANCE\_IMPACTED\_LIMITS\_ERROR       | REJECTED | Original authorization impacted limits different from `AvailableCreditLimit` and `AvailableWithdrawalLimit`, and therefore cannot be partially cancelled. | PRC         | 57            |
| REMAINING\_CANCELLATION\_BALANCE\_ERROR                         | REJECTED | Internal error in remaining cancellation balance validation.                                                                                              | PRC         | 96            |
| UNEXPECTED\_ERROR                                               | REJECTED | Unexpected error happened while processing the authorization.                                                                                             | SED         | 96            |

**Additional data:** Not mapped yet.

**Payload example:**

```json
{
    "name": "REMAINING_CANCELLATION_BALANCE",
    "status": "APPROVED",
    "reason": "ORIGINAL_AUTHORIZATION_APPROVED",
    "description": "Remaining cancellation balance for this authorization was approved."
}
```
<!-- source:end -->

## Lifecycle status

- `docs/core-platform/authorization-validation-rules-for-platform-operations.md`: updatedAt 2026-03-25T14:05:13.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- Source content contains MDX/HTML components (for example `<Table>`, `<HTMLBlock>`, `<Callout>`, `<details>`). They are preserved exactly as published; tables inside them were not converted to Markdown.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/core-platform/authorization-validation-rules-for-platform-operations.md` | body lines 876–2314 | https://developers.pismo.io/pismo-docs/docs/authorization-validation-rules-for-platform-operations | `ef57f4790279dffc…` | 2026-03-25T14:05:13.000Z |

## Related knowledge units

- None.
