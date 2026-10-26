---
ku_id: KU-CORE-authorization-validation-rules-for-platform-operations-part-01
title: Authorization validation rules for platform operations (part 1 of 2)
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

# Authorization validation rules for platform operations (part 1 of 2)

**KU ID:** `KU-CORE-authorization-validation-rules-for-platform-operations-part-01` · **Category:** Core platform · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) (one part of a large page) into one implementation-oriented unit. Grouping rationale: single source page; split into parts because the page is very large

Scope as stated in `docs/core-platform/authorization-validation-rules-for-platform-operations.md`:

> This guide contains the full list of authorization rules used by the Pismo platform to validate requests. An authorization for platform operations builds a validation result map with the status of each validation. The validation result map contains a list of validation result objects. Each object contains information in the following fields.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/core-platform/authorization-validation-rules-for-platform-operations.md`: Authorization validation rules for platform operations; Response and denial codes; Account retrieval; Account retrieval by bank account; Account retrieval by document number; Account limits retrieval; Account status validation; Account validation; Anti-fraud integration; Authorization registration; Authorization retrieval; Balances configuration retrieval; Card retrieval; Card ARQC validation; Card ATC validation; Card authorization mode validation; Card CVV validation; Card CVV2 validation; Card entered expiration date validation; Card expired date validation; Card password tries validation; Card PIN validation; Card status validation

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/core-platform/authorization-validation-rules-for-platform-operations.md` lines 1–875 of the body

Source URL: https://developers.pismo.io/pismo-docs/docs/authorization-validation-rules-for-platform-operations · updatedAt: 2026-03-25T14:05:13.000Z

<!-- source:begin path=docs/core-platform/authorization-validation-rules-for-platform-operations.md part=0-875 -->

# Authorization validation rules for platform operations

This guide contains the full list of authorization rules used by the Pismo platform to validate requests. An authorization for platform operations builds a validation result map with the status of each validation. The validation result map contains a list of validation result objects. Each object contains information in the following fields.

| Field            | Description                                                                                                                                                                                                                                                                                         |
| :--------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| name             | Name of the evaluated rule. Use this field as the key to find the specific validation since the order of the validations inside the list can change.                                                                                                                                                |
| status           | Identifies if the rule was approved (APPROVED), rejected (REJECTED), or not evaluated during the validation flow (SKIPPED).                                                                                                                                                                         |
| reason           | Identifies the status reason why the specific rule was approved, rejected, or skipped. After identifying the rule itself using the field `name`, you can use the field `reason` to map specific scenarios that you want to monitor or create any rule for it.                                       |
| description      | Describes the validation result. This field should not be used as a key for any rule as it only aims to aid understanding of the validation result.                                                                                                                                                 |
| additional\_data | Contains an object that holds important information related to that validation to help the system map scenarios and create rules over those validations. The contract for this field may be different for each validation, so every rule pattern can be found below. This object can also be empty. |

# Response and denial codes

<Accordion title="Response codes" icon="fa-info-circle">
  | Response code | Description           |
  | ------------- | --------------------- |
  | "00"          | Approved              |
  | "05"          | Do not honor          |
  | "12"          | Invalid transaction   |
  | "14"          | Invalid card          |
  | "30"          | Invalid format        |
  | "51"          | Insufficient funds    |
  | "54"          | Expired card          |
  | "55"          | Invalid PIN           |
  | "57"          | Action not permitted  |
  | "59"          | Suspected fraud       |
  | "62"          | Invalid account       |
  | "63"          | Security violation    |
  | "75"          | PIN tries exceeded    |
  | "92"          | External system error |
  | "96"          | Internal system error |
</Accordion>

<Accordion title="Denial codes" icon="fa-info-circle">
  | Denial code | Description                                                                                                                                                  |   |     |              |
  | ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | - | --- | ------------ |
  | AF001       | Unexpected error occurred during the anti-fraud evaluation                                                                                                   |   |     |              |
  | AF002       | Operation was not approved by the anti-fraud system                                                                                                          |   |     |              |
  | AFD         | Authorization failed anti-fraud evaluation                                                                                                                   |   |     |              |
  | AFE         | Internal error when performing anti-fraud evaluation                                                                                                         |   |     |              |
  | AND         | Payment methods acceptances not found                                                                                                                        |   |     |              |
  | ARE         | Internal error when performing platform authorization retrieval                                                                                              |   |     |              |
  | ARN         | Platform authorization not found                                                                                                                             |   |     |              |
  | ART         | Timeout when attempting to platform authorization retrieval                                                                                                  |   |     |              |
  | ATC         | Invalid ATC                                                                                                                                                  |   |     |              |
  | AU001       | Internal error occurred when attempting to create the authorization                                                                                          |   |     |              |
  | AU002       | Internal error occurred when retrieving authorization                                                                                                        |   |     |              |
  | AU003       | Internal error occurred when retrieving remaining cancellation balance                                                                                       |   |     |              |
  | AU004       | Original authorization not found                                                                                                                             |   |     |              |
  | AU005       | Original authorization is denied                                                                                                                             |   |     |              |
  | AU006       | Total cancellation balance exceeds the authorized amount                                                                                                     |   |     |              |
  | AU007       | Can not partially cancel an authorization pending confirmation                                                                                               |   |     |              |
  | AU008       | Original authorization is from a different account than the account received in the request                                                                  |   |     |              |
  | AU009       | Authorization was already cancelled                                                                                                                          |   |     |              |
  | AU010       | Original authorization impacted limits different from \`AvailableCreditLimit\` and \`AvailableWithdrawalLimit\`, and therefore cannot be partially cancelled |   |     |              |
  | AU011       | Original authorization is not pending                                                                                                                        |   |     |              |
  | AU012       | Original authorization has different configuration                                                                                                           |   |     |              |
  | BAE         | Internal error when validating bank account                                                                                                                  |   |     |              |
  | BAN         | Invalid bank account                                                                                                                                         |   |     |              |
  | BCE         | Balances configuration retrieval returned an error.                                                                                                          |   |     |              |
  | BTO         | Balances configuration retrieval returned a timeout.                                                                                                         |   |     |              |
  | CBD         | Card broken                                                                                                                                                  |   |     |              |
  | CDB         | Card blocked                                                                                                                                                 |   | CEE | Card expired |
  | CIC         | Card data does not match card on file data                                                                                                                   |   |     |              |
  | CNF         | Payment methods configuration not found                                                                                                                      |   |     |              |
  | CVV         | Invalid CVV                                                                                                                                                  |   |     |              |
  | CV2         | Invalid CVV2                                                                                                                                                 |   |     |              |
  | DND         | Document number authorization is not allowed                                                                                                                 |   |     |              |
  | ECD         | Declined by external installment plan calculation                                                                                                            |   |     |              |
  | ECE         | Internal error when calculating external installment plan                                                                                                    |   |     |              |
  | ECI         | Invalid response when calculating external installment plan                                                                                                  |   |     |              |
  | ECT         | Timeout when performing calculation of external installment plan                                                                                             |   |     |              |
  | FC001       | Internal error occurred during flex controls evaluation                                                                                                      |   |     |              |
  | FC002       | Operation was not approved by flex controls                                                                                                                  |   |     |              |
  | FCD         | Authorization failed flex controls evaluation                                                                                                                |   |     |              |
  | FCE         | Internal error when performing flex controls evaluation                                                                                                      |   |     |              |
  | IAD         | Invalid account                                                                                                                                              |   |     |              |
  | IAE         | Internal error when validating account                                                                                                                       |   |     |              |
  | IAM         | Invalid authorization mode                                                                                                                                   |   |     |              |
  | IAS         | Invalid account status                                                                                                                                       |   |     |              |
  | ICR         | Invalid cryptogram                                                                                                                                           |   |     |              |
  | IDN         | Invalid document number                                                                                                                                      |   |     |              |
  | IED         | Invalid expiration date                                                                                                                                      |   |     |              |
  | IMD         | Invalid merchant status                                                                                                                                      |   |     |              |
  | IPD         | Invalid PIN                                                                                                                                                  |   |     |              |
  | KNC         | HSM key not configured                                                                                                                                       |   |     |              |
  | KNF         | HSM key not found                                                                                                                                            |   |     |              |
  | LE001       | Internal error occurred while impacting the balance                                                                                                          |   |     |              |
  | LE002       | Internal error occurred when retrieving account limits                                                                                                       |   |     |              |
  | LE003       | Insufficient funds                                                                                                                                           |   |     |              |
  | LE004       | Duplicate tracking ID                                                                                                                                        |   |     |              |
  | LE005       | Account not found                                                                                                                                            |   |     |              |
  | LE006       | Operation not allowed when impacting funds                                                                                                                   |   |     |              |
  | MDN         | Multiple accounts found linked to document number. Unable to define which one to use.                                                                        |   |     |              |
  | MNF         | Merchant not found                                                                                                                                           |   |     |              |
  | OIE         | Internal error saving payment methods integrity message                                                                                                      |   |     |              |
  | OPE         | Internal error saving payment methods information                                                                                                            |   |     |              |
  | PA001       | Authorized account is different from the one received in the request                                                                                         |   |     |              |
  | PA002       | Invalid processing code                                                                                                                                      |   |     |              |
  | PA003       | Account doesn’t have active credit status                                                                                                                    |   |     |              |
  | PA004       | Account doesn’t have active debit status                                                                                                                     |   |     |              |
  | PA005       | Account not provided                                                                                                                                         |   |     |              |
  | PA006       | Account doesn’t have active credit and debit status                                                                                                          |   |     |              |
  | PAD         | Tracking ID was already used in the platform authorization                                                                                                   |   |     |              |
  | PAE         | Internal error when attempting to perform platform authorization                                                                                             |   |     |              |
  | PAT         | Timeout when attempting to perform platform authorization                                                                                                    |   |     |              |
  | PC001       | Internal error occurred when retrieving processing code                                                                                                      |   |     |              |
  | PC002       | Processing code not found                                                                                                                                    |   |     |              |
  | PC003       | Processing code has a different balance impact than original authorization                                                                                   |   |     |              |
  | PCD         | Invalid processing code                                                                                                                                      |   |     |              |
  | PCE         | Internal error when validating processing code                                                                                                               |   |     |              |
  | PCO         | Internal error when mapping processing code                                                                                                                  |   |     |              |
  | PLD         | Authorization failed ledger impacting                                                                                                                        |   |     |              |
  | PLE         | Internal error when impacting ledger                                                                                                                         |   |     |              |
  | PLO         | Operation not allowed on the ledger                                                                                                                          |   |     |              |
  | PNF         | Card not found                                                                                                                                               |   |     |              |
  | POA         | Invalid original authorization                                                                                                                               |   |     |              |
  | PPD         | Invalid program parameter                                                                                                                                    |   |     |              |
  | PPE         | Internal error when validating program parameter                                                                                                             |   |     |              |
  | PPE         | Platform program error                                                                                                                                       |   |     |              |
  | PPN         | Platform program not found                                                                                                                                   |   |     |              |
  | PR001       | Internal error occurred when retrieving program                                                                                                              |   |     |              |
  | PR002       | Program not found                                                                                                                                            |   |     |              |
  | PRC         | Invalid remaining cancellation balance                                                                                                                       |   |     |              |
  | PRE         | Internal error when calculating rates                                                                                                                        |   |     |              |
  | PTD         | PIN tries exceeded                                                                                                                                           |   |     |              |
  | RA001       | Internal error occurred when calculating amount                                                                                                              |   |     |              |
  | RNM         | Validation reason not mapped                                                                                                                                 |   |     |              |
  | SED         | Internal system error                                                                                                                                        |   |     |              |
  | UE001       | Unexpected error                                                                                                                                             |   |     |              |
</Accordion>

# Account retrieval

When the authorization request from the payment methods service is performed using a Pismo account ID, the platform validates whether that account ID is valid and exists in the database. If any error occurs, the request is declined.

> 📘
>
> In this guide, table entries marked **N/A** indicate **Not Applicable**.

**Name:** ACCOUNT

**Possible statuses:** APPROVED, SKIPPED, REJECTED

**Possible reasons:**

| Reason              | Status   | Description                        | Denial code | Response code |
| :------------------ | :------- | :--------------------------------- | :---------- | :------------ |
| ACCOUNT\_FOUND      | APPROVED | Account was found.                 | N/A         | 00            |
| ACCOUNT\_SKIPPED    | SKIPPED  | Account validation was skipped.    | N/A         | N/A           |
| ACCOUNT\_NOT\_FOUND | REJECTED | Account was not found.             | IAD         | 62            |
| ACCOUNT\_ERROR      | REJECTED | Internal error validating account. | SED         | 96            |

**Additional data:** Contains the account ID received in the request.

**Fields:** `account_id`

**Payload example:**

```json
{
    "name": "ACCOUNT",
    "status": "APPROVED",
    "reason": "ACCOUNT_FOUND",
    "description": "Account was found.",
    "additional_data": {
        "account_id": 9999
    }
}
```

# Account retrieval by bank account

When the payment methods authorization request is performed using the customer's bank, the platform validates whether that bank's information is valid and exists. If any error occurs or the account is not found based on the provided bank information, the request is declined.

**Name:** BANK\_ACCOUNT

**Possible status:** APPROVED, SKIPPED, REJECTED

**Possible reasons:**

| Reason                    | Status   | Description                             | Denial code | Response code |
| :------------------------ | :------- | :-------------------------------------- | :---------- | :------------ |
| BANK\_ACCOUNT\_FOUND      | APPROVED | Bank account was found.                 | N/A         | 00            |
| BANK\_ACCOUNT\_SKIPPED    | SKIPPED  | Bank account validation was skipped.    | N/A         | N/A           |
| BANK\_ACCOUNT\_NOT\_FOUND | SKIPPED  | Bank account was not found.             | BAN         | 62            |
| BANK\_ACCOUNT\_ERROR      | REJECTED | Internal error validating bank account. | BAE         | 96            |

**Additional data:** Contains the account ID returned by the external system.

**Fields:** `account_id`

**Payload example:**

```json
{
	"name": "BANK_ACCOUNT",
	"status": "APPROVED",
	"reason": "BANK_ACCOUNT_FOUND",
	"description": "Bank account was found.",
	"additional_data": {
		"account_id": 9999
	}
}
```

# Account retrieval by document number

When the payment methods authorization request is performed using a document number, the platform validates whether that document number is valid and exists. If any error occurs or the account is not found based on the provided document number, the request is declined.

**Name:** DOCUMENT\_NUMBER

**Possible status:** APPROVED, SKIPPED, REJECTED

**Possible reasons:**

| Reason                                     | Status   | Description                                                                                                                                             | Denial code | Response code |
| :----------------------------------------- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------ | :---------- | :------------ |
| DOCUMENT\_NUMBER\_FOUND                    | APPROVED | Account was found successfully based on document number.                                                                                                | N/A         | 00            |
| DOCUMENT\_NUMBER\_SKIPPED                  | SKIPPED  | Document number validation was skipped.                                                                                                                 | N/A         | N/A           |
| DOCUMENT\_NUMBER\_NOT\_FOUND               | REJECTED | Account was not found based on document number.                                                                                                         | IDN         | 62            |
| DOCUMENT\_NUMBER\_NOT\_PERMITTED           | REJECTED | Document number is not permitted for all accounts found.                                                                                                | DND         | 57            |
| DOCUMENT\_NUMBER\_MULTIPLE\_ACCOUNT\_FOUND | REJECTED | Document number is linked to more than one account that allows authorization using document number. Authorization system can’t define which one to use. | MDN         | 57            |
| DOCUMENT\_NUMBER\_ERROR                    | REJECTED | Internal error validating document number.                                                                                                              | SED         | 96            |

**Additional data:** Contains the field indicating whether the document number is present.

**Fields:** `document_number_present`

**Payload example:**

```json
{
    "name": "DOCUMENT_NUMBER",
    "status": "APPROVED",
    "reason": "DOCUMENT_NUMBER_FOUND",
    "description": "Account was found successfully based on document number.",
    "additional_data": {
        "document_number_present": true
    }
}
```

# Account limits retrieval

Platform authorization retrieves the account limits information to process this authorization request and perform validations.

**Name:**  ACCOUNT\_LIMITS

**Possible status:** APPROVED, SKIPPED, REJECTED

**Possible reasons:**

| Reason                      | Status   | Description                                                   | Denial code | Response code |
| :-------------------------- | :------- | :------------------------------------------------------------ | :---------- | :------------ |
| ACCOUNT\_LIMITS\_FOUND      | APPROVED | Account limits were found.                                    | N/A         | 00            |
| ACCOUNT\_LIMITS\_SKIPPED    | SKIPPED  | Account limits validation was skipped.                        | N/A         | N/A           |
| ACCOUNT\_LIMITS\_NOT\_FOUND | REJECTED | Account limits were not found.                                | IAD         | 62            |
| ACCOUNT\_LIMITS\_ERROR      | REJECTED | Internal error validating account limits.                     | IAE         | 96            |
| UNEXPECTED\_ERROR           | REJECTED | Unexpected error happened while processing the authorization. | SED         | 96            |

**Additional data:** Contains current balances and limits.

**Fields:** `available_credit_limit`, `available_total_installment_credit`, `available_withdrawal_credit`, `total_credit_limit`, `total_installment_credit_limit`, `withdrawal_credit_limit`

**Payload example:**

```json
{
    "name": "ACCOUNT_LIMITS",
    "status": "APPROVED",
    "reason": "ACCOUNT_LIMITS_FOUND",
    "description": "Account limits were found.",
    "additional_data": {
    	  "available_credit_limit": 87459.76,
        "available_total_installment_credit": 179.2,
        "available_withdrawal_credit": 4,
        "total_credit_limit": 0,
        "total_installment_credit_limit": 500,
        "withdrawal_credit_limit": 500
    }
}
```

# Account status validation

Platform authorization performs the account status validation to verify whether the account is allowed to perform the request.

**Name:**  ACCOUNT\_STATUS

**Possible status:** APPROVED, SKIPPED, REJECTED

**Possible reasons:**

| Reason                          | Status   | Description                                                   | Denial code | Response code |
| :------------------------------ | :------- | :------------------------------------------------------------ | :---------- | :------------ |
| ACCOUNT\_STATUS\_PERMITTED      | APPROVED | Account status is permitted.                                  | N/A         | 00            |
| ACCOUNT\_STATUS\_SKIPPED        | SKIPPED  | Account status validation was skipped.                        | N/A         | N/A           |
| ACCOUNT\_STATUS\_NOT\_PERMITTED | REJECTED | Account is blocked from receiving debits or credits.          | IAS         | 57            |
| UNEXPECTED\_ERROR               | REJECTED | Unexpected error happened while processing the authorization. | SED         | 96            |

**Additional data:** Not mapped yet.

**Payload example:**

```json
{
    "name": "ACCOUNT_STATUS",
    "status": "REJECTED",
    "reason": "ACCOUNT_STATUS_NOT_PERMITTED",
    "description": "Account is blocked from receiving debits or credits. "
}
```

# Account validation

Platform authorization validates if the account ID received from the payment methods request is valid.

**Name:**  ACCOUNT\_ID

**Possible status:** APPROVED, SKIPPED, REJECTED

**Possible reasons:**

| Reason                          | Status   | Description                                                           | Denial code | Response code |
| :------------------------------ | :------- | :-------------------------------------------------------------------- | :---------- | :------------ |
| ACCOUNT\_ID\_PERMITTED          | APPROVED | Account ID is permitted.                                              | N/A         | 00            |
| ACCOUNT\_ID\_PERMITTED\_SKIPPED | SKIPPED  | Account ID validation was skipped.                                    | N/A         | N/A           |
| ACCOUNT\_ID\_NOT\_PERMITTED     | REJECTED | Authorized account is different from the one received in the request. | IAD         | 62            |
| ACCOUNT\_ID\_NOT\_PROVIDED      | REJECTED | Account ID was not provided in the request.                           | IAD         | 62            |

**Additional data:** Not mapped yet.

**Payload example:**

```json
{
    "name": "ACCOUNT_ID",
    "status": "APPROVED",
    "reason": "ACCOUNT_ID_PERMITTED",
    "description": "Account ID is permitted."
}
```

# Anti-fraud integration

Platform authorization integrates with an external anti-fraud system to have the issuer-specific rules evaluated by their system.

**Name:**  ANTI\_FRAUD

**Possible status:** APPROVED, SKIPPED, REJECTED

**Possible reasons:**

| Reason                     | Status   | Description                                                   | Denial code | Response code |
| :------------------------- | :------- | :------------------------------------------------------------ | :---------- | :------------ |
| ANTI\_FRAUD\_APPROVED      | APPROVED | Authorization passed anti-fraud evaluation.                   | N/A         | 00            |
| ANTI\_FRAUD\_SKIPPED       | SKIPPED  | Anti-fraud evaluation was skipped.                            | N/A         | N/A           |
| ANTI\_FRAUD\_NOT\_APPROVED | REJECTED | Authorization failed anti-fraud evaluation.                   | AFD         | 59            |
| ANTI\_FRAUD\_ERROR         | REJECTED | Internal error in anti-fraud evaluation.                      | AFE         | 92            |
| UNEXPECTED\_ERROR          | REJECTED | Unexpected error happened while processing the authorization. | SED         | 96            |

**Additional data:** When anti-fraud returns the response code or denial code to replace the authorization response, `additional_data` contains the `override` true/false flag and `override_type` enum (`NONE`, `RESPONSE_CODE_ONLY`, `DENIAL_CODE_ONLY`, `RESPONSE_AND_DENIAL_CODE`) . The `force_approve` flag is `true` when anti-fraud returns that the authorizer must force authorization approval even if any validation has been denied and the validation steps have been executed in the anti-fraud flow.

**Fields:** `override`, `override_type`, `force_approve`, `executed_steps`

**Payload example:**

```json
{
    "name": "ANTI_FRAUD",
    "status": "APPROVED",
    "reason": "ANTI_FRAUD_APPROVED",
    "description": "Authorization passed anti-fraud evaluation.",
    "additional_data": {
      "override": "false",
      "override_type": "NONE",
      "force_approve": "false",
      "executed_steps": {}
    }
}
```

# Authorization registration

Platform authorization registers the authorization information into the database. If something fails on this operation, the authorization may be declined.

**Name:**  AUTHORIZATION

**Possible status:** APPROVED, REJECTED

**Possible reasons:**

| Reason                 | Status   | Description                               | Denial code | Response code |
| :--------------------- | :------- | :---------------------------------------- | :---------- | :------------ |
| AUTHORIZATION\_CREATED | APPROVED | Authorization was created successfully.   | N/A         | 00            |
| AUTHORIZATION\_ERROR   | REJECTED | Internal error in creating authorization. | SED         | 96            |

**Additional data:** Not mapped yet.

**Payload example:**

```json
{
    "name": "AUTHORIZATION",
    "status": "APPROVED",
    "reason": "AUTHORIZATION_CREATED",
    "description": "Authorization was created successfully.",
    "additional_data": {}
}
```

# Authorization retrieval

Payment methods flow retrieves the original authorization on the cancellation flow to perform some validations against its current status and determine whether that request may proceed. If the authorization is retrieved successfully, the flow goes on but if an error happens, the cancellation request is declined.

**Name:** AUTHORIZATION\_RETRIEVAL

**Possible status:** APPROVED, SKIPPED, REJECTED

**Possible reasons:**

| Reason                               | Status   | Description                                                       | Denial code | Response code |
| :----------------------------------- | :------- | :---------------------------------------------------------------- | :---------- | :------------ |
| AUTHORIZATION\_RETRIEVAL\_SUCCESSFUL | APPROVED | Authorization was retrieved successfully.                         | N/A         | 00            |
| AUTHORIZATION\_RETRIEVAL\_SKIPPED    | SKIPPED  | Authorization retrieval was skipped.                              | N/A         | N/A           |
| AUTHORIZATION\_RETRIEVAL\_ERROR      | REJECTED | Unexpected error has happened while retrieving the authorization. | ARE         | 96            |
| AUTHORIZATION\_RETRIEVAL\_TIMEOUT    | REJECTED | Timeout has happened while retrieving the authorization.          | ART         | 96            |
| AUTHORIZATION\_RETRIEVAL\_NOT\_FOUND | REJECTED | Authorization was not found for the identifier provided.          | ARN         | 96            |

**Additional data:** Not mapped yet.

**Payload example:**

```json
{
    "name": "AUTHORIZATION_RETRIEVAL",
    "status": "APPROVED",
    "reason": "AUTHORIZATION_RETRIEVAL_SUCCESSFUL",
    "description": "Authorization was retrieved successfully."
}
```

# Balances configuration retrieval

Payment methods flow integrates with the Balances configuration API to determine which account balances should be impacted by the Ledger in a given authorization. This functionality allows you to create dynamic rules to impact the balance, offering additional flexibility. All rules are associated with a processing code.

**Name:** BALANCES\_CONFIG

**Possible status:** APPROVED, SKIPPED, REJECTED

**Possible reasons:**

| Reason                          | Status   | Description                                           | Denial code | Response code |
| :------------------------------ | :------- | :---------------------------------------------------- | :---------- | :------------ |
| BALANCES\_CONFIG\_FOUND         | APPROVED | Balances configuration was found.                     | N/A         | 00            |
| BALANCES\_CONFIG\_SKIPPED       | SKIPPED  | Balances configuration validation was skipped.        | N/A         | N/A           |
| BALANCES\_CONFIG\_NOT\_FOUND    | SKIPPED  | Balances configuration was not found.                 | N/A         | N/A           |
| BALANCES\_CONFIG\_ERROR         | REJECTED | Balances configuration validation returned an error.  | BCE         | 96            |
| BALANCES\_CONFIG\_INCONSISTENCY | REJECTED | Balances configuration validation returned a timeout. | BCE         | 57            |

**Additional data:** Contains balance impact information returned by the Balances configuration API, which is used to impact the Ledger.

**Fields:** `impact`, `consider`, `amount`, `amount_consider`, `reset_limit`

**Payload example:**

```json
{
	"name": "BALANCES_CONFIG",
	"status": "APPROVED",
	"reason": "BALANCES_CONFIG_FOUND",
	"description": "Balances configuration was found.",
	"additional_data": {
		"amount": "contract_amount",
		"amount_consider": "principal_amount",
		"consider": [
			"AvailableCreditLimit",
			"OverLimit"
		],
		"impact": [
			"AvailableCreditLimit"
		],
		"reset_limit": "last_installment"
	}
}
```

# Card retrieval

When the authorization request from the payment methods service is performed using a card (PAN), the platform validates whether that card number is valid and exists in the database. If any error occurs, the request is declined.

**Name:** CARD

**Possible status:** APPROVED, SKIPPED, REJECTED

**Possible reasons:**

| Reason           | Status   | Description                     | Denial code | Response code |
| :--------------- | :------- | :------------------------------ | :---------- | :------------ |
| CARD\_FOUND      | APPROVED | Card was found.                 | N/A         | 00            |
| CARD\_SKIPPED    | SKIPPED  | Card validation was skipped.    | N/A         | N/A           |
| CARD\_NOT\_FOUND | REJECTED | Card was not found.             | PNF         | 14            |
| CARD\_ERROR      | REJECTED | Internal error validating card. | SED         | 96            |

**Additional data:** Contains the card hash related to the card number received

**Fields:** `card_hash`

**Payload example:**

```json
{
    "name": "CARD",
    "status": "APPROVED",
    "reason": "CARD_FOUND",
    "description": "Card was found.",
    "additional_data": {
        "card_hash": "99999999fOt10YS1QK8V3J6poQ/r1gOsfZZZZzzzzzZkxyiabfxRBPVfSzMlKAlXIs777777777tOwntil9k+A=="
    }
}
```

# Card ARQC validation

When the authorization request from the payment methods service is performed using a card (PAN) and contains the cryptogram (chip) information, the platform validates this Cryptogram information against the HSM to verify whether it is valid.

**Name:** ARQC

**Possible status:** APPROVED, SKIPPED, REJECTED

**Possible reasons:**

| Reason                      | Status   | Description                      | Denial code | Response code |
| :-------------------------- | :------- | :------------------------------- | :---------- | :------------ |
| CARD\_ARQC\_VALID           | APPROVED | ARQC was validated successfully. | N/A         | 00            |
| CARD\_ARQC\_SKIPPED         | SKIPPED  | ARQC validation was skipped.     | N/A         | N/A           |
| CARD\_ARQC\_INVALID         | REJECTED | ARQC is invalid.                 | ICR         | 63            |
| HSM\_REQUIRED\_FIELD\_ERROR | REJECTED | Missing required field.          | KNC         | 57            |
| CARD\_ARQC\_ERROR           | REJECTED | Internal error validating ARQC.  | SED         | 96            |

**Additional data:** Contains the field that indicates whether the cryptogram data is present. When declined by HSM, contains the error code. When validation is skipped, contains the cause.

**Fields:** `arqc_presence`, `code`, `cause`

**Payload example:**

```json
{
    "name": "CARD_ARQC",
    "status": "SKIPPED",
    "reason": "CARD_ARQC_SKIPPED",
    "description": "ARQC validation was skipped.",
    "additional_data": {
        "arqc_presence": false,
        "cause": "Authorization has no cardholder verification method.",
        "code": ""
    }
}
```

# Card ATC validation

ATC is the transaction counter present in the chip information of the card. Every time the cardholder performs a transaction using a POS that reads chip data, the counter is incremented. The Pismo platform compares the counter received in the request with the ones registered in the database from previous authorizations. If the counter is not duplicated and is within an allowed range (configured by the issuer), the request is validated.

**Name:**  CARD\_ATC

**Possible status:** APPROVED, SKIPPED, REJECTED

**Possible reasons:**

| Reason                             | Status   | Description                                                       | Denial code | Response code |
| :--------------------------------- | :------- | :---------------------------------------------------------------- | :---------- | :------------ |
| CARD\_ATC\_WITHIN\_ALLOWED\_RANGE  | APPROVED | ATC is within allowed range.                                      | N/A         | 00            |
| CARD\_ATC\_SKIPPED                 | SKIPPED  | ATC validation was skipped.                                       | N/A         | N/A           |
| CARD\_ATC\_OUTSIDE\_ALLOWED\_RANGE | REJECTED | ATC is outside allowed range.                                     | ATC         | 63            |
| CARD\_ATC\_IS\_DUPLICATED          | REJECTED | ATC is already registered in the database for this card.          | ATC         | 63            |
| MISSING\_PROGRAM\_PARAMETER        | REJECTED | Min or max range parameters were not found to perform validation. | PPD         | 57            |

**Additional data:** Contains the current ATC, the list of previous ATCs, and both min and max offset allowed parameters.

**Fields:** `current_atc`,`previous_atc`, `min_offset_parameter`, `max_offset_parameter`

**Payload example:**

```json
{
    "name": "CARD_ATC",
    "status": "APPROVED",
    "reason": "CARD_ATC_WITHIN_ALLOWED_RANGE",
    "description": "ATC is within allowed range.",
    "additional_data": {
        "current_atc": "10",
        "previous_atc": "[9,8,7,5,1]",
        "min_offset_parameter": "5",
        "max_offset_parameter": "15"
    }
}
```

# Card authorization mode validation

When authorization request from the payment methods service uses a card, the Pismo platform validates if the authorization mode (credit/debit) matches the card mode. Credit cards can only operate on credit mode and debit cards can only operate on debit mode. Combo or multi application cards can operate on both modes but the mode received on the authorization request must be enabled on the card.

**Name:**  CARD\_AUTHORIZATION\_MODE

**Possible status:** APPROVED, SKIPPED, REJECTED

**Possible reasons:**

| Reason                                  | Status   | Description                                   | Denial code | Response code |
| :-------------------------------------- | :------- | :-------------------------------------------- | :---------- | :------------ |
| CARD\_AUTHORIZATION\_MODE\_VALID        | APPROVED | Card has authorization mode enabled.          | N/A         | 00            |
| CARD\_AUTHORIZATION\_MODE\_SKIPPED      | SKIPPED  | Card mode validation was skipped.             | N/A         | N/A           |
| CARD\_AUTHORIZATION\_MODE\_INVALID      | REJECTED | Card mode doesn't allow authorization mode.   | IAM         | 57            |
| CARD\_AUTHORIZATION\_MODE\_NOT\_PRESENT | REJECTED | Card mode not present.                        | IAM         | 57            |
| CARD\_AUTHORIZATION\_MODE\_NOT\_FOUND   | REJECTED | Card doesn't have authorization mode created. | IAM         | 57            |

**Additional data:** Contains the authorization mode.

**Fields:** `authorization_mode`

**Payload example:**

```json
{
    "name": "CARD_AUTHORIZATION_MODE",
    "status": "APPROVED",
    "reason": "CARD_AUTHORIZATION_MODE_VALID",
    "description": "Card has authorization mode enabled.",
    "additional_data": {
        "authorization_mode": "CREDIT"
    }
}
```

# Card CVV validation

When the authorization request from the payment methods service is performed using a card (PAN) and contains a CVV (track1 or track2 data), this CVV information is validated against the HSM to verify whether it is valid.

**Name:** CARD\_CVV

**Possible status:** APPROVED, SKIPPED, REJECTED

**Possible reasons:**

| Reason                      | Status   | Description                     | Denial code | Response code |
| :-------------------------- | :------- | :------------------------------ | :---------- | :------------ |
| CARD\_CVV\_VALID            | APPROVED | CVV was validated successfully. | N/A         | 00            |
| CARD\_CVV\_SKIPPED          | SKIPPED  | CVV validation was skipped.     | N/A         | N/A           |
| CARD\_CVV\_INVALID          | REJECTED | CVV is invalid.                 | CVV         | 14            |
| HSM\_REQUIRED\_FIELD\_ERROR | REJECTED | Missing required field.         | KNC         | 57            |
| CARD\_CVV\_ERROR            | REJECTED | Internal error validating CVV.  | SED         | 96            |

**Additional data:** Contains two fields indicating the track1 and track2 data presence and, when declined by HSM, contains the error code. When validation is skipped, contains the cause.

**Fields:** `track1_presence`, `track2_presence`, `code`, `cause`

**Payload example:**

```json
{
    "name": "CARD_CVV",
    "status": "SKIPPED",
    "reason": "CARD_CVV_SKIPPED",
    "description": "CVV validation was skipped.",
    "additional_data": {
        "track1_presence": false,
        "track2_presence": false,
        "cause": "Authorization has no cardholder verification method.",
        "code": ""
    }
}
```

# Card CVV2 validation

When the authorization request from the payment methods service is performed using a card (PAN) and contains a CVV2, the platform validates this CVV2 information against the HSM to verify whether it is valid. The platform also validates the entered expiration date during this flow since it is used on the CVV2 calculation and must be correct.

**Name:** CARD\_CVV2

**Possible status:** APPROVED, SKIPPED, REJECTED

**Possible reasons:**

| Reason                          | Status   | Description                                           | Denial code | Response code |
| :------------------------------ | :------- | :---------------------------------------------------- | :---------- | :------------ |
| CARD\_CVV2\_VALID               | APPROVED | CVV2 was validated successfully.                      | N/A         | 00            |
| CARD\_CVV2\_SKIPPED             | SKIPPED  | CVV2 validation was skipped.                          | N/A         | N/A           |
| CARD\_CVV2\_INVALID             | REJECTED | CVV2 is invalid.                                      | CV2         | 14            |
| CARD\_EXPIRATION\_DATE\_INVALID | REJECTED | Entered expiration date is invalid.                   | IED         | 54            |
| HSM\_REQUIRED\_FIELD\_ERROR     | REJECTED | Missing required field. Expiration date not provided. | KNC         | 57            |
| CARD\_CVV2\_ERROR               | REJECTED | Internal error validating CVV2.                       | SED         | 96            |

**Additional data:** Contains the field indicating the CVV2 data presence, the entered expiration date, and, when declined by HSM, it contains the error code. When validation is skipped, contains the cause.

**Fields:** `cvv2_presence`, `entered_expiration_date`, `code`, `cause`

**Payload example:**

```json
{
    "name": "CARD_CVV2",
    "status": "SKIPPED",
    "reason": "CARD_CVV2_SKIPPED",
    "description": "CVV2 validation was skipped.",
    "additional_data": {
        "cvv2_presence": false,
        "entered_expiration_date": "2806",
        "cause": "Authorization has no cardholder verification method.",
        "code": ""
    }
}
```

# Card entered expiration date validation

When the authorization request from the payment methods service is performed using a card and cardholder provides the expiration date, the platform validates whether the entered expiration date matches the card’s expiration date.

**Name:**  CARD\_ENTERED\_EXPIRATION\_DATE

**Possible status:** APPROVED, SKIPPED, REJECTED

**Possible reasons:**

| Reason                                   | Status   | Description                                                 | Denial code | Response code |
| :--------------------------------------- | :------- | :---------------------------------------------------------- | :---------- | :------------ |
| CARD\_ENTERED\_EXPIRATION\_DATE\_VALID   | APPROVED | Entered expiration date matches card expiration date.       | N/A         | 00            |
| CARD\_ENTERED\_EXPIRATION\_DATE\_SKIPPED | SKIPPED  | Validation of entered expiration date was skipped.          | N/A         | N/A           |
| CARD\_ENTERED\_EXPIRATION\_DATE\_INVALID | REJECTED | Entered expiration date doesn't match card expiration date. | IED         | 54            |
| CARD\_ENTERED\_EXPIRATION\_DATE\_ERROR   | REJECTED | Internal error validating entered expiration date.          | SED         | 96            |

**Additional data:** Contains the entered expiration date and the card’s expiration date.

**Fields:** `entered_expiration_date`, `card_expiration_date`

**Payload example:**

```json
{
    "name": "CARD_ENTERED_EXPIRATION_DATE",
    "status": "APPROVED",
    "reason": "CARD_ENTERED_EXPIRATION_DATE_VALID",
    "description": "Entered expiration date matches card expiration date.",
    "additional_data": {
        "card_expiration_date": "2806",
        "entered_expiration_date": "2806"
    }
}
```

# Card expired date validation

When the authorization request from the payment methods service is performed using a card, the platform validates whether the card is expired.

**Name:**  CARD\_EXPIRATION\_DATE

**Possible status:** APPROVED, SKIPPED, REJECTED

**Possible reasons:**

| Reason                    | Status   | Description                                     | Denial code | Response code |
| :------------------------ | :------- | :---------------------------------------------- | :---------- | :------------ |
| CARD\_NOT\_EXPIRED        | APPROVED | Card is not expired.                            | N/A         | 00            |
| CARD\_EXPIRATION\_SKIPPED | SKIPPED  | Validation of card expiration date was skipped. | N/A         | N/A           |
| CARD\_EXPIRED             | REJECTED | Card is expired.                                | CEE         | 54            |
| CARD\_EXPIRATION\_ERROR   | REJECTED | Internal error validating card expiration date. | SED         | 96            |

**Additional data:** Contains the card’s expiration date.

**Fields:** `card_expiration_date`

**Payload example:**

```json
{
    "name": "CARD_EXPIRATION_DATE",
    "status": "APPROVED",
    "reason": "CARD_NOT_EXPIRED",
    "description": "Card is not expired.",
    "additional_data": {
        "card_expiration_date": "2806"
    }
}
```

# Card password tries validation

The Pismo platform validates and counts the number of incorrect password tries by the cardholder. If those tries reach a configured threshold, the card is blocked and new requests aren't allowed even if the password is correct. This threshold is configured by the issuer on the Pismo platform.

The password tries error counter is only reset when the cardholder enters the correct password in a new authorization request before reaching the blocking threshold. Requests that don't use the password, such as e-commerce or contactless, even though approved, do not reset the counter. After reaching the threshold, even the requests without a password are declined.

**Name:** CARD\_PASSWORD\_TRIES

**Possible status:** APPROVED, SKIPPED, REJECTED

**Possible reasons:**

| Reason                          | Status   | Description                                                       | Denial code | Response code |
| :------------------------------ | :------- | :---------------------------------------------------------------- | :---------- | :------------ |
| CARD\_PASSWORD\_TRIES\_ALLOWED  | APPROVED | Password tries are within configured threshold.                   | N/A         | 00            |
| CARD\_PASSWORD\_TRIES\_SKIPPED  | SKIPPED  | Password tries validation was skipped.                            | N/A         | N/A           |
| CARD\_PASSWORD\_TRIES\_EXCEEDED | REJECTED | Password tries exceeded configured threshold.                     | PTD         | 75            |
| MISSING\_PROGRAM\_PARAMETER     | REJECTED | Max password tries parameter was not found to perform validation. | PPD         | 57            |

**Additional data:** Contains the current password tries count and the configured threshold.

**Fields:** `current_password_tries`, `password_tries_allowed`

**Payload example:**

```json
{
    "name": "CARD_PASSWORD_TRIES",
    "status": "APPROVED",
    "reason": "CARD_PASSWORD_TRIES_ALLOWED",
    "description": "Password tries are within configured threshold.",
    "additional_data": {
        "current_password_tries": 0,
        "password_tries_allowed": 3
    }
}
```

# Card PIN validation

When the authorization request from the payment methods service is performed using a card (PAN) and contains a PIN block, the platform validates this PIN block information against the HSM.

**Name:** CARD\_PIN

**Possible status:** APPROVED, SKIPPED, REJECTED

**Possible reasons:**

| Reason                      | Status   | Description                     | Denial code | Response code |
| :-------------------------- | :------- | :------------------------------ | :---------- | :------------ |
| CARD\_PIN\_VALID            | APPROVED | PIN was validated successfully. | N/A         | 00            |
| CARD\_PIN\_SKIPPED          | SKIPPED  | PIN validation was skipped.     | N/A         | N/A           |
| CARD\_PIN\_INVALID          | REJECTED | PIN is invalid.                 | IPD         | 55            |
| HSM\_KEY\_NOT\_FOUND        | REJECTED | HSM keys not found.             | KNF         | 57            |
| HSM\_REQUIRED\_FIELD\_ERROR | REJECTED | Missing required field.         | KNC         | 57            |
| CARD\_PIN\_ERROR            | REJECTED | Internal error validating PIN.  | SED         | 96            |

**Additional data:** Contains the field that indicates whether the PIN block data is present. When declined by HSM, contains the error code. When validation is skipped, contains the cause.

**Fields:** `pin_presence`, `code`, `cause`

**Payload example:**

```json
{
    "name": "CARD_PIN",
    "status": "SKIPPED",
    "reason": "CARD_PIN_SKIPPED",
    "description": "PIN validation was skipped.",
    "additional_data": {
        "pin_presence": false,
        "cause": "Authorization has no cardholder verification method.",
        "code": ""
    }
}
```

# Card status validation

When the authorization request from the payment methods service is performed using a card, the platform validates whether the card has a blocked status.

**Name:** CARD\_STATUS

**Possible status:** APPROVED, SKIPPED, REJECTED

**Possible reasons:**
<!-- source:end -->

## Lifecycle status

- `docs/core-platform/authorization-validation-rules-for-platform-operations.md`: updatedAt 2026-03-25T14:05:13.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- None identified by the migration checks.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/core-platform/authorization-validation-rules-for-platform-operations.md` | body lines 1–875 | https://developers.pismo.io/pismo-docs/docs/authorization-validation-rules-for-platform-operations | `ef57f4790279dffc…` | 2026-03-25T14:05:13.000Z |

## Related knowledge units

- None.
