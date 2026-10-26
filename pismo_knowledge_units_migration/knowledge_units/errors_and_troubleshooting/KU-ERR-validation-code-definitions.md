---
ku_id: KU-ERR-validation-code-definitions
title: Validation code definitions
category: errors_and_troubleshooting
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/card-issuing/validation-code-definitions.md
  sha256: 852d75488fb272a41237a9626f506a7111051ae9f6bfc38cee66648a91899700
  url: https://developers.pismo.io/pismo-docs/docs/validation-code-definitions
  role: primary_guide
  updated_at: '2026-08-26T19:54:08.000Z'
operations:
- post-acquisitions-v3-s2s-applications
- post-v2-card-atc-reset
related_kus:
- KU-API-card-issuing-cards--cards
- KU-API-core-platform-accounts--accounts
- KU-CARD-digital-wallets
- KU-CORE-flex-controls
- KU-ERR-validation-codes-for-authorization-events-part-01
- KU-ERR-validation-codes-for-authorization-events-part-02
- KU-EVT-catalogue-other-domains
grouping_rationale: single source page
---

# Validation code definitions

**KU ID:** `KU-ERR-validation-code-definitions` · **Category:** Errors and troubleshooting · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/card-issuing/validation-code-definitions.md`:

> To determine the reason an authorization was declined, use one of the following methods, depending on the model you are working with.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/card-issuing/validation-code-definitions.md`: Validation code definitions; Verify authorization decline reasons; Verify authorization decline reason for Full balance transactions; Verify authorization decline reason for Zero balance transactions; 91 - Authorization system or issuer system inoperative; 810 - Available limit validation; 998 - Card hash not present in the database; ACE - network-transactions-api communication error; ACT - A timeout occurred while fetching account; AEE - Anti-fraud external generic error; AET - Anti-fraud external API timeout; AFE - Anti-fraud internal generic error; AGE - Unexpected error while fetching account; AIT - Anti-fraud internal API timeout; ANF - Acceptance not found; AUD - Authorization disabled; BCE - Balance Config generic error; BCT - Balance Config Timeout; BII - Balance inquiry internal error; Card status validation; CAT - Config API timeout; CAV - CAVV 3DS validation result; CED - Invalid expiration date provided; CET - Card timeout; CGE - Card generic error; CLF - Credit limit impact not found; CMD - Card mode disabled; CNC - Account cancelled; CND - Account blocked; CNU - Account status unknown; CTE - Transaction counter exceeded; CTT - Card token timeout; CV3 - CVC3 not configured; DCC - DCC transaction not allowed for program; DCE - distributor-api communication error; DCM - Original authorization not found at refund; DIC - Invalid country for DCC definition; DIY - Invalid currency for DCC definition; ETR - Exceed time to reversal; FAT - ATC validation; Duplicated ATC; ATC minimum offset; ATC maximum offset; FL6 - Card blocked by anti-fraud; FR1 and FR2 - CVV/CVC validation; FR3 - IAV  - intelligent account validation; FR5 - Transaction made with magnetic stripe in a country where it's not allowed to be used; FR6 - Password validation; FR7 - Card not present in database; FRE - Cryptogram data validation; FRH - POS (point-of-sale) entry mode validation; Visa; Mastercard; FRN - Chip field validation; FRO - Chip signature validation; GCD - GCD Gift card denial; HCE - HSM communication error; IAT - Invalid account type; IMA - Invalid message authentication code (MAC); IMF - Invalid message format; ISE - Insufficient statements; IZA - Zero amount not allowed; LAE - An unexpected error happened while getting the account information; LCT - Ledger account timeout; LNF - Account not found; LUD - Limit update duplicated ID error; LUE - Error on update Ledger; LUT - Ledger timeout; MDC - Multi-currency not allowed for DCC authorization; MPC - Program config not found; NCV - Entry mode not allowed with no CVM; OON - Org operation not found; OOT - Orgs operation timeout; OP1 - Message consistency or generic error; PAE - Unexpected error while fetching parameters; PAT - A timeout occurred while fetching parameters; PCE - Unexpected error in processing code definition; PCT - A timeout occurred in processing code definition; PFT - Denied by anti-fraud; PGE - Program Config Generic Error; PIC - Program has invalid currency code; PNP - PIN not present; PRE - Unexpected error while fetching program; PRN - Program not found; PRT - A timeout occurred while fetching program; RAD - Rates API denial; RAE - Rates API error; RAT - Rates API timeout; RED - Operation not allowed by rules / Rules do not honor / Rules internal error / Operation not permitted - credit voucher; STD - Denied by second authorizer; TGE - Card token generic error; TNP - Token not provided; TSM - Password tries exceeded; UBN - NFC disabled; VEV - Expired virtual card; VNM - Expired card; Z30 - Token found, but does not match card; ZBA - Zero balance client webhook returns 401 status code, unauthorized.; ZBD - Zero balance client declined; ZBE - Zero balance client webhook returns general error; ZBF - Zero balance client webhook returns 403 status code, forbidden.; ZBP - Partial authorization response invalid in Zero Balance Flow; ZBT - Zero balance client webhook throws timeout exception.; ZBU - Unavailable endpoint, zero balance client webhook returns 503 status code.

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 2 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/card-issuing/validation-code-definitions.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/validation-code-definitions · updatedAt: 2026-08-26T19:54:08.000Z

<!-- source:begin path=docs/card-issuing/validation-code-definitions.md part=0-end -->

# Validation code definitions

# Verify authorization decline reasons

To determine the reason an authorization was declined, use one of the following methods, depending on the model you are working with.

## Verify authorization decline reason for Full balance transactions

For authorizations under the Full balance model, when an authorization is declined, the reason for the rejection is returned in the [Network authorization received](https://developers.pismo.io/events/docs/networktransactions-network-authorization-1) event. In this event, check the field `custom_response_code`,  which contains a code or abbreviation indicating the reason the transaction was declined.

The codes returned in the `custom_response_code` field can be found in the [Validation codes for authorization events](https://developers.pismo.io/pismo-docs/docs/validation-codes-for-authorization-events) guide and their respective definitions are in this guide.

Note: If the authorization is declined and the `custom_response_code` field is empty in the Network authorization received event, this means the rejection did not come from Pismo’s authorizer. There are cases, such as advice transactions, where the card network itself may decline the operation. In such cases, Pismo recommends checking the `incoming_response_code`.

## Verify authorization decline reason for Zero balance transactions

For authorizations under the Zero Balance model, the `custom_response_code` field typically returns the code **ZBD** (Zero Balance Decline). This is because the decision to approve or decline the transaction is always made by the client, and the response is sent to Pismo's authorizer via the Zero Balance Webhook.

In this model, when an authorization is declined, the reason for the rejection is also returned in the [Network authorization received](https://developers.pismo.io/events/docs/networktransactions-network-authorization-1) event. Check the `custom_response_code` field, which contains a code or abbreviation indicating the reason the transaction was declined.

Additionally, you can identify the rejection reason through the validation map (`ValidationResults` field), which is also returned in the Network authorization received event. This field lists all the validations performed by Pismo’s authorizer for the transaction, along with any rejections that occurred.

Note: A transaction may be declined for more than one reason. However, Pismo’s authorizer considers the first rejection encountered as the definitive reason and records it as the official cause of the decline.

# 91 - Authorization system or issuer system inoperative

This error can be returned when the authorizations or route is not available, such as when the issuer host is unavailable, unexpected disconnection, or any unforeseen/platform-mapped error.

To determine the actual reason for the authorization decline, refer to [Verify authorization decline reasons](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#verify-authorization-decline-reasons) in this guide.

# 810 - Available limit validation

If the balance or withdrawal limits are insufficient to complete a transaction, the Pismo platform denies the transaction. For insufficient balance, the response code for all is `51`. For insufficient withdrawal limit, the denial code is `61` (except for ELO, which remains `51`).

To determine the actual reason for the authorization decline, refer to [Verify authorization decline reasons](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#verify-authorization-decline-reasons) in this guide.

# 998 - Card hash not present in the database

There is an encrypted database that associates a hash with a primary account number. If no card is retrieved using the given hash, or if more than one card is retrieved, the transaction is denied.

For a tokenized card, if its status is not active, the transaction is also denied.

To determine the actual reason for the authorization decline, refer to [Verify authorization decline reasons](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#verify-authorization-decline-reasons) in this guide.

# ACE - network-transactions-api communication error

This error occurs when there is a communication error or a timeout with the authorization system during the stateful validations. In this case, there could be a problem with the authorization flow.

To determine the actual reason for the authorization decline, refer to [Verify authorization decline reasons](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#verify-authorization-decline-reasons) in this guide.

# ACT - A timeout occurred while fetching account

During the transaction flow, the [Accounts API](https://developers.pismo.io/pismo-docs/reference/post-acquisitions-v3-s2s-applications) is called in order to retrieve account details. If a timeout happens in the [Accounts API](https://developers.pismo.io/pismo-docs/reference/post-acquisitions-v3-s2s-applications), the transaction is denied.

To determine the actual reason for the authorization decline, refer to [Verify authorization decline reasons](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#verify-authorization-decline-reasons) in this guide.

# AEE - Anti-fraud external generic error

This custom code addresses generic errors (4xx, 5xx) when calling the external anti-fraud system.

To determine the actual reason for the authorization decline, refer to [Verify authorization decline reasons](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#verify-authorization-decline-reasons) in this guide.

# AET - Anti-fraud external API timeout

This custom code applies when the external API does not respond in a timely matter.

To determine the actual reason for the authorization decline, refer to [Verify authorization decline reasons](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#verify-authorization-decline-reasons) in this guide.

# AFE - Anti-fraud internal generic error

This custom code addresses generic errors (4xx) when calling the internal Anti-fraud API, a Pismo API that handles calls to anti-fraud systems. This exception is also used when the internal Anti-fraud API is down.

To determine the actual reason for the authorization decline, refer to [Verify authorization decline reasons](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#verify-authorization-decline-reasons) in this guide.

# AGE - Unexpected error while fetching account

During the transaction flow, the [Accounts API ](https://developers.pismo.io/pismo-docs/reference/post-acquisitions-v3-s2s-applications)is called in order to retrieve account details. If an unexpected error happens while fetching those details in the [Accounts API](https://developers.pismo.io/pismo-docs/reference/post-acquisitions-v3-s2s-applications), the transaction is denied.

To determine the actual reason for the authorization decline, refer to [Verify authorization decline reasons](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#verify-authorization-decline-reasons) in this guide.

# AIT - Anti-fraud internal API timeout

This custom code applies when the internal Anti-fraud API, a Pismo API that handles calls to anti-fraud systems, does not respond in a timely manner.

To determine the actual reason for the authorization decline, refer to [Verify authorization decline reasons](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#verify-authorization-decline-reasons) in this guide.

# ANF - Acceptance not found

Check to see if the first two positions of sub-field Transaction Type from Processing Code (DE3) present at the authorization message body are in internal program parameters. Each Transaction Type domain is an acceptance. If a domain isn’t parameterized, the transaction is denied.

Currently the processing codes 11 - Quasi-Cash Transaction, 39 - Eligibility Inquiry, 40 - Cardholder Account Transfer, 70 - PIN Change, and 72 - PIN Unblock are not mapped.

To determine the actual reason for the authorization decline, refer to [Verify authorization decline reasons](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#verify-authorization-decline-reasons) in this guide.

# AUD - Authorization disabled

This denial code is generated when an option is enabled on the network transactions configuration. The option `deny_all_authorizations` disables all authorizations where the configuration is set. `deny_all_authorizations` can be enabled at the organization, program, or account level. It can also be enabled on a BIN, but must be related to a configuration made on the other levels. This is useful for migration flow scenarios where you want a guarantee that you will process any authorizations before the go-live signal.

To determine the actual reason for the authorization decline, refer to [Verify authorization decline reasons](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#verify-authorization-decline-reasons) in this guide.

# BCE - Balance Config generic error

When the authorization gets an error when trying to retrieve information from the Balance Config API, in this case the card network must be notified that we have an internal error and a message will be generated for this authorization.

To determine the actual reason for the authorization decline, refer to [Verify authorization decline reasons](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#verify-authorization-decline-reasons) in this guide.

# BCT - Balance Config Timeout

This denial occurs when the Balance config API exceeds the time allowed to respond.

To determine the actual reason for the authorization decline, refer to [Verify authorization decline reasons](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#verify-authorization-decline-reasons) in this guide.

# BII - Balance inquiry internal error

This denial code is returned when validating the balance. It occurs when calling the Zero Balance client webhook to check the cardholder's available credit limit and it returns an invalid response. The denial code also is returned when an error occurs while trying to fetch the cardholder's available credit limit from the Ledger API for Full balance customers.

To determine the actual reason for the authorization decline, refer to [Verify authorization decline reasons](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#verify-authorization-decline-reasons) in this guide.

# Card status validation

A card's status determines whether the card can be used. For statuses `NORMAL` and `REISSUED`, all transactions are approved. The `CREATED` status is only approved for tokenized transactions from digital wallets. This provides the cardless experience, which enables a customer to use their card before the physical one arrives. For all other statuses, transactions are denied.

The following table shows the card statuses that are associated with denial codes.

| Denial Code | Card Status                                                                                  |
| :---------- | :------------------------------------------------------------------------------------------- |
| BNB         | Any other status                                                                             |
| BND         | CANCELLED or CLIENTORDER                                                                     |
| BNF         | FRAUD                                                                                        |
| BNI         | INOPERATIVE                                                                                  |
| BNM         | DAMAGED                                                                                      |
| BNP         | LOST                                                                                         |
| BNR         | ROBBED or THEFT                                                                              |
| BNU         | UNRECEIVED                                                                                   |
| BNW         | WARNING                                                                                      |
| CPE         | PENDING                                                                                      |
| CSU         | CARD UNKNOWN                                                                                 |
| FRB         | CREATED (Note that tokenized transactions from digital wallets are allowed for this status.) |
| UBT         | BLOCKED (This denial code also happens when the number of password tries are exceeded.)      |
| VED         | DELETED (Applies only for virtual cards)                                                     |

To determine the actual reason for the authorization decline, refer to [Verify authorization decline reasons](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#verify-authorization-decline-reasons) in this guide.

# CAT - Config API timeout

Returned when the Authorization service is unable to obtain a response from the Platform Config API within the configured timeout period, after all retry attempts have been exhausted. This code specifically identifies an infrastructure timeout condition and is distinct from Platform Config API processing errors, which continue to return `PGE` (Platform Config Generic Error).

To determine the actual reason for the authorization decline, refer to [Verify authorization decline reasons](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#verify-authorization-decline-reasons) in this guide.

# CAV - CAVV 3DS validation result

If CAV was returned in the `denial_code` field, it is necessary to call the PCI-Cards team (cards).

For a 3DS transaction, it's necessary to do the CAVV validation with the Hardware Security Module (HSM). This validation is only needed when the 3DS transaction/customer uses the CAVV algorithm.

To ELO, those 3DS-related values are found on BIT-122.

To determine the actual reason for the authorization decline, refer to [Verify authorization decline reasons](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#verify-authorization-decline-reasons) in this guide.

# CED - Invalid expiration date provided

If a purchase has a cardholder verification method (CVM), such as CVV, password, or chip, it's necessary to verify it using the HSM. If the provided expiration date is invalid inside the Hardware Security Module (HSM), check to see if the transaction is denied. This is a stateless validation, so a further validation to check the values in the database is made: [VNM - Expired card](#vnm---expired-card).

To determine the actual reason for the authorization decline, refer to [Verify authorization decline reasons](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#verify-authorization-decline-reasons) in this guide.

# CET - Card timeout

When the authorization gets a error (timeout reached) while trying to retrieve the card data, the network will be notified that we have an internal error and in some cases a message will be generated for this authorization.

To determine the actual reason for the authorization decline, refer to [Verify authorization decline reasons](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#verify-authorization-decline-reasons) in this guide.

# CGE - Card generic error

When the authorization gets an error (invalid response code) trying to retrieve the card data, the network will be notified that we have an internal error and in some cases a message will be generated for this authorization.

To determine the actual reason for the authorization decline, refer to [Verify authorization decline reasons](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#verify-authorization-decline-reasons) in this guide.

# CLF - Credit limit impact not found

When the authorization gets an error while trying to retrieve information from the Credit Limit Impact, the card network is notified that there is an internal error and a message is generated for this authorization.

To determine the actual reason for the authorization decline, refer to [Verify authorization decline reasons](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#verify-authorization-decline-reasons) in this guide.

# CMD - Card mode disabled

Scenarios in which the card mode is invalid or not registered (very unlikely). This can happen with combo cards that don't have the DEBIT or CREDIT mode specified or if the card is pure credit and doesn’t have the specified credit mode. The same happens for a pure debit card when it doesn’t have the debit mode specified.

To determine the actual reason for the authorization decline, refer to [Verify authorization decline reasons](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#verify-authorization-decline-reasons) in this guide.

# CNC - Account cancelled

Indicates if an account is cancelled, it  is not allowed to operate. It’s a domain from Accounts team and we validate in the online authorization time.

To determine the actual reason for the authorization decline, refer to [Verify authorization decline reasons](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#verify-authorization-decline-reasons) in this guide.

# CND - Account blocked

The following parameters are checked for a transaction.

* `AuthorizationStatus` – Indicates if an account is allowed to operate.
* `CreditStatus` – Indicates if an account can receive a credit.
* `DebitStatus` – Indicates if an account can receive a debit.
* `CollectionStatus` –  Indicates if an account is in normal or overdue status. If an account is overdue, the account holder cannot do a cash-out (purchase, cash withdrawal, and so on).

To determine the actual reason for the authorization decline, refer to [Verify authorization decline reasons](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#verify-authorization-decline-reasons) in this guide.

# CNU - Account status unknown

Indicates if the account status is unknown, then it is not allowed to operate–only `NORMAL` account status is valid. It’s a domain from Accounts team and we validate in the online authorization time.

To determine the actual reason for the authorization decline, refer to [Verify authorization decline reasons](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#verify-authorization-decline-reasons) in this guide.

# CTE - Transaction counter exceeded

> 📘 Internationalization in progress
>
> Work to internationalize the Pismo platform is ongoing. Some parameter names, such as `LIMITE TRANSACOES CARTAO TEMPORARIO`, are still in the original Portuguese.

Applies only for virtual cards. These cards have a transaction counter. When the count exceeds the value set in the program parameter `LIMITE TRANSACOES CARTAO TEMPORARIO`, the transaction is denied.

To determine the actual reason for the authorization decline, refer to [Verify authorization decline reasons](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#verify-authorization-decline-reasons) in this guide.

# CTT - Card token timeout

When the authorization receives an error (timeout reached) while trying to retrieve the card token data, the network should will be notified that there is an internal error. In some cases, a message will be generated for this authorization.

To determine the actual reason for the authorization decline, refer to [Verify authorization decline reasons](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#verify-authorization-decline-reasons) in this guide.

# CV3 - CVC3 not configured

Purchases with entry mode 91 (910, 911, and 912) that are not made via [wallet](https://developers.pismo.io/pismo-docs/docs/wallet-overview) are denied with code CV3, if there is no CVC3 validation configured.

To determine the actual reason for the authorization decline, refer to [Verify authorization decline reasons](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#verify-authorization-decline-reasons) in this guide.

# DCC - DCC transaction not allowed for program

Each program is configured to allow or deny dynamic currency conversion (DCC) transactions. The default is to allow them.

If a program is configured to deny DCC transactions, any transaction that is of type DCC is denied with code DCC.

To determine the actual reason for the authorization decline, refer to [Verify authorization decline reasons](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#verify-authorization-decline-reasons) in this guide.

# DCE - distributor-api communication error

This error occurs when there is a communication error between the authorization system and the Parser API, or there is a timeout during the stateless validations. This could indicate a problem with the authorization flow. Note that the Parser API has 5 seconds to complete authorization validation. If validation is not completed in time, a DCE error occurs.

To determine the actual reason for the authorization decline, refer to [Verify authorization decline reasons](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#verify-authorization-decline-reasons) in this guide.

# DCM - Original authorization not found at refund

When a refund transaction (MTI 0400 or 0420) is received, the original authorization must be retrieved from the database before proceeding. If the original authorization is not found, the transaction is declined.

<Callout icon="📘" theme="info">
  In some cases for `MTI 0400` or `0420`, you may see differences in the response from the [Card network authorization return sent](https://developers.pismo.io/events/docs/networktransactions-network-message-1) event and the [Network authorization received](https://developers.pismo.io/events/docs/networktransactions-network-authorization-1) event. This is because even if the system doesn't find the original transaction, it has to reply `"Authorization_response_code":"00"` to the network to avoid resending the advice and generating costs. You should consider the response advice received from the Network authorization received event to be the true response.
</Callout>

To determine the actual reason for the authorization decline, refer to [Verify authorization decline reasons](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#verify-authorization-decline-reasons) in this guide.

# DIC - Invalid country for DCC definition

The Pismo platform needs a valid country code to determine if a transaction is a dynamic currency conversion (DCC) transaction. If there is no valid country code, the platform denies the transaction with code DIC.

To determine the actual reason for the authorization decline, refer to [Verify authorization decline reasons](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#verify-authorization-decline-reasons) in this guide.

# DIY - Invalid currency for DCC definition

The Pismo platform needs a valid currency code to determine if a transaction is a dynamic currency conversion (DCC) transaction. If there is no valid currency code, the platform denies the transaction with code DIY.

To determine the actual reason for the authorization decline, refer to [Verify authorization decline reasons](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#verify-authorization-decline-reasons) in this guide.

# ETR - Exceed time to reversal

This denial code is specific for ELO. It means that the reversal advice (MTI 0420) came 24 hours or more after the persisted authorization. This behavior is not allowed for ELO in reversal advice cases.

To determine the actual reason for the authorization decline, refer to [Verify authorization decline reasons](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#verify-authorization-decline-reasons) in this guide.

# FAT - ATC validation

The chip card application maintains an Application Transaction Counter (ATC) for security. (Since it runs locally on the chip, it qualifies as a [fat application](https://www.techopedia.com/definition/7140/fat-application).) The ATC is incremented when the  physical card is used to make a purchase.

ATC validation is performed to make the platform safe from fraud attempts such as cloned cards. A duplicated ATC or an unusual jump in its value could be a fraud warning sign.

To determine the actual reason for the authorization decline, refer to [Verify authorization decline reasons](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#verify-authorization-decline-reasons) in this guide.

### Duplicated ATC

The platform compares a provided ATC value with a list of values from previous authorizations. This list can store around 2000 previous ATC values. If a duplicate is found, the authorization is denied.

### ATC minimum offset

The parameter `ATC MIN OFFSET` represents the minimum allowed difference between the provided ATC value and the last ATC value. If the provided ATC value minus the last ATC value is less than `ATC MIN OFFSET`, the platform treats the event as a replay attack and the authorization is denied.

### ATC maximum offset

The parameter `ATC MAX OFFSET` represents the maximum allowed difference between the provided ATC value and the last ATC value. If the provided ATC value minus the last ATC value is greater than `ATC MAX OFFSET`, this indicates unusual behavior. It's not necessarily a replay attack, but it suggests that the chip data was captured for a future attack.

For information about how to reset an ATC list, refer to [Reset card ATC](https://developers.pismo.io/pismo-docs/reference/post-v2-card-atc-reset).

# FL6 - Card blocked by anti-fraud

When the anti-fraud mechanism flags a transaction as a **referral** (which is a specific designation of fraud used by some Brazilian clients), the card is blocked and the Pismo platform denies the transaction with this code.

To determine the actual reason for the authorization decline, refer to [Verify authorization decline reasons](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#verify-authorization-decline-reasons) in this guide.

# FR1 and FR2 - CVV/CVC validation

If CVV/CVC1 is present in the authorization message body, a validation by the Hardware Security Module (HSM) is necessary using the following data: cryptographic key, primary account number, service code, and expiration date. If an error occurs in this HSM validation, the platform returns denial code FR1. However, if CVV/CVC2 is present, the same thing happens, except that FR2 is returned in case of error.

The CVV/CVC 1 or 2 validation is skipped in the following scenarios:

* Tokenized transactions with a safe authentication flag like MDES or VTS (Apple Pay, Samsung Pay, etc.)
* The emitter allowed no-CVM transactions
* Recurring billing with 3DS authentication (SLI - 210), like Netflix or Spotify
* Pre-authorization with 3DS authorization (SLI - 210)
* E-commerce authorizations

To determine the actual reason for the authorization decline, refer to [Verify authorization decline reasons](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#verify-authorization-decline-reasons) in this guide.

# FR3 - IAV  - intelligent account validation

FR3 refers to an error message that may be displayed while processing a transaction with a card. The code indicates that the transaction was denied because the previously provided authorization number for the original transaction is invalid or does not match the expected authorization number.

This can occur for a number of reasons, including entering the authorization number incorrectly or attempting to use a previously invalid or expired authorization number.

To determine the actual reason for the authorization decline, refer to [Verify authorization decline reasons](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#verify-authorization-decline-reasons) in this guide.

# FR5 - Transaction made with magnetic stripe in a country where it's not allowed to be used

When the currency code is 986 - BRL, and the Track 1 or Track 2 data are present in the authorization message body without the chip data, this message is handled as a magnetic stripe and is denied.

At this point, the expiration date, service code, and CVV/CVC are not validated.

At the EMV POS (Europay, Mastercard, and Visa point-of-sale) entry mode, this denial happens before FRE, which is often used to deal with this specific situation.

To determine the actual reason for the authorization decline, refer to [Verify authorization decline reasons](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#verify-authorization-decline-reasons) in this guide.

# FR6 - Password validation

If the password is present, it is validated by the Hardware Security Module (HSM) against the password in the database. If it does not match, the transaction is denied. When the cardholder enters an invalid password, denial code `FR6` is returned.

To determine the actual reason for the authorization decline, refer to [Verify authorization decline reasons](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#verify-authorization-decline-reasons) in this guide.

# FR7 - Card not present in database

Besides the encrypted database, there is a PCI database with card data. If the card is not present in this database, the transaction is denied.

To determine the actual reason for the authorization decline, refer to [Verify authorization decline reasons](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#verify-authorization-decline-reasons) in this guide.

# FRE - Cryptogram data validation

There are multiple possible scenarios for this denial code:

* Missing cryptogram in EMV chip authorizations—This happens when the POS entry mode is 05 (chip) or 07 (contactless) from a physical card (e.g., not a tokenized transaction) without the cryptogram. It’s possible that FR5 occurs in this case due to a validation conflict.
* Cryptogram was sent out of context—This occurs when a cryptogram is retrieved from a message, but the entry mode is neither 05 (chip) nor 07 (contactless).
* Chip values validation failed (Visa processing only)—The Pismo platform checks that information like amount and country in the cryptogram field match the information in the authorization message. If it does not, an FRE denial code is returned.

To determine the actual reason for the authorization decline, refer to [Verify authorization decline reasons](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#verify-authorization-decline-reasons) in this guide.

# FRH - POS (point-of-sale) entry mode validation

Denial list for terminal capability validation (POS or input device) and entry mode. This validation checks how the card data was acquired (card machine, online purchase, NFC, etc.) and the entry mode information. For example, in e-commerce, it’s not possible to retrieve the card chip data, so it’s not a valid entry mode and should be denied. For Visa, entry mode is in Field 22. For Mastercard, it's in DE 61.

To determine the actual reason for the authorization decline, refer to [Verify authorization decline reasons](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#verify-authorization-decline-reasons) in this guide.

The following combinations should be denied according to this specification:

### Visa

**0 - Unknown**

91 - Contactless device-read-originated using magnetic stripe data rules

**1 - Terminal not used**

02 - Magnetic stripe read. CVV checking might not be possible.

03 - Optical code

04 - Reserved for future use

05 - Contact integrated circuit card read using VSDC chip data rules

06 - Reserved for future use

07 - Contactless device-read-originated using qVSDC chip data rules

90 - Magnetic stripe read and exact content of Track 1 or Track 2 included (CVV check possible)

91 - Contactless device-read-originated using magnetic stripe data rules

95 - Integrated circuit card read—CVV or iCVV checking might not be possible

**2 - Magnetic stripe read capability**

03 - Optical code

04 - Reserved for future use

05 - Contact integrated circuit card read using VSDC chip data rules

06 - Reserved for future use

07 - Contactless device-read-originated using qVSDC chip data rules

91 - Contactless device-read-originated using magnetic stripe data rules

95 - Integrated circuit card read—CVV or iCVV checking might not be possible

**3 - Barcode read capability**

02 - Magnetic stripe read. CVV checking might not be possible.

04 - Reserved for future use

05 - Contact integrated circuit card read using VSDC chip data rules

06 - Reserved for future use

07 - Contactless device-read-originated using qVSDC chip data rules

90 - Magnetic stripe read and exact content of Track 1 or Track 2 included (CVV check possible)

91 - Contactless device-read-originated using magnetic stripe data rules

95 - Integrated circuit card read—CVV or iCVV checking might not be possible

**4 - OCR-read capability**

02 - Magnetic stripe read. CVV checking might not be possible.

03 - Optical code

05 - Contact integrated circuit card read using VSDC chip data rules

06 - Reserved for future use

07 - Contactless device-read-originated using qVSDC chip data rules

90 - Magnetic stripe read and exact content of Track 1 or Track 2 included (CVV check possible)

91 - Contactless device-read-originated using magnetic stripe data rules

95 - Integrated circuit card read—CVV or iCVV checking might not be possible

**5 - Chip-readable capability**

03 - Optical code

04 - Reserved for future use

91 - Contactless device-read-originated using magnetic stripe data rules

95 - Integrated circuit card read—CVV or iCVV checking might not be possible

**8 - Proximity-read-capable terminal**

02 - Magnetic stripe read—CVV checking might not be possible

03 - Optical code

04 - Reserved for future use

05 - Contact integrated circuit card read using VSDC chip data rules

91 - Contactless device-read-originated using magnetic stripe data rules

95 - Integrated circuit card read—CVV or iCVV checking might not be possible

**9 - Terminal does not have the capability to read cards data**

02 - Magnetic stripe read—CVV checking might not be possible

03 - Optical code

04 - Reserved for future use

05 - Contact integrated circuit card read using VSDC chip data rules

06 - Reserved for future use

07 - Contactless device-read-originated using qVSDC chip data rules

90 - Magnetic stripe read and exact content of Track 1 or Track 2 included (CVV check possible)

91 - Contactless device-read-originated using magnetic stripe data rules

95 - Integrated circuit card read—CVV or iCVV checking might not be possible

### Mastercard

**0 - Input capability unknown or unspecified**

91 - Contactless magnetic stripe

**1 - No terminal used (voice/ARU authorization)**

02 - Magnetic stripe - not qualified

03 - Bar code reader

04 - OCR

05 - Chip

07 - Contactless magnetic stripe / chip

09 - PAN entry via eCommerce, including remote chip

79 - Chip --> Manual

80 - Chip --> Magnetic stripe

82 - PAN auto entry via server (issuer, acquirer, or third party)

90 - Magnetic stripe - full data

91 - Contactless magnetic stripe

95 - Visa Only - Chip with unreliable CVV

**2 - Supports magnetic stripe input only**

03 - Bar code reader

04 - OCR

05 - Chip

07 - Contactless magnetic stripe / chip

09 - PAN entry via eCommerce, including remote chip

82 - PAN auto entry via server (issuer, acquirer, or third party)

91 - Contactless magnetic stripe

95 - Visa only - Chip with unreliable CVV

**3 - Supports contactless EMV input**

91 - Contactless magnetic stripe

95 - Visa only - Chip with unreliable CVV

**4 - Contactless magnetic stripe (proximity chip)**

03 - Bar code reader

91 - Contactless magnetic stripe

95 - Visa only - Chip with unreliable CVV

**5 - Supports EMV contact chip input and magnetic stripe input**

03 - Bar code reader

04 - OCR

91 - Contactless magnetic stripe

95 - Visa only - Chip with unreliable CVV

**6 - Supports key entry input only**

02 - Magnetic stripe - not qualified

03 - Bar code reader

04 - OCR

05 - Chip

07 - Contactless magnetic stripe / chip

79 - Chip --> Manual

80 - Chip --> Magnetic stripe

90 - Magnetic stripe - full data

91 - Contactless magnetic stripe

95 - Visa only - Chip with unreliable CVV

**7 - Supports magnetic stripe input and key entry input**

03 - Bar code reader

04 - OCR

05 - Chip

07 - Contactless magnetic stripe / chip

91 - Contactless magnetic stripe

95 - Visa only - Chip with unreliable CVV

**8 - Supports EMV contact chip input, magnetic stripe input, and key entry input**

03 - Bar code reader

04 - OCR

07 - Contactless magnetic stripe / chip

91 - Contactless magnetic stripe

**9 - Supports EMV contact chip input only**

02 - Magnetic stripe - not qualified

03 - Bar code reader

04 - OCR

07 - Contactless magnetic stripe / chip

79 - Chip --> Manual

80 - Chip --> Magnetic stripe

90 - Magnetic stripe - full data

91 - Contactless magnetic stripe

95 - Visa Only - Chip with unreliable CVV

# FRN - Chip field validation

Validation of the chip cryptogram. When the field `DE55` is present in the authorization message body, it’s necessary to recalculate the chip cryptogram from the following tags and chip keys:

| Tag  | Chip key                                                                 |
| :--- | :----------------------------------------------------------------------- |
| 5F34 | Application Primary Account Number (PAN)                                 |
| 9F02 | Amount Authorized                                                        |
| 9F03 | Amount Other                                                             |
| 9F1A | Terminal Country Code                                                    |
| 95   | Terminal Verification Results                                            |
| 5F2A | Transaction Currency Code                                                |
| 9A   | Transaction Date                                                         |
| 9C   | Transaction Type                                                         |
| 9F37 | Unpredictable Number                                                     |
| 82   | Application Interchange Profile                                          |
| 9F36 | Application Transaction Counter                                          |
| 9F10 | Issuer Application Data (tag content, key index, and cryptogram version) |
| 9F33 | Terminal Capability Profile                                              |

The calculated response is compared to tag 9F26 - Application Cryptogram, which contains the cryptogram generated by the card. If the values are identical, you should send back the ARPC - Application Response Cryptogram (tag 91) so it can be verified that the transaction was authorized by a trusted comparison method. However, if the values are different, the transaction is denied. The tags C0 - Secondary PIN Block and 91 - Issuer Authentication Data are not used in this validation.

For Visa transactions, the transaction amount and country code are checked against the values present in the `DE55` field (chip data).

To determine the actual reason for the authorization decline, refer to [Verify authorization decline reasons](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#verify-authorization-decline-reasons) in this guide.

# FRO - Chip signature validation

Check the cardholder verification type used by POS at byte 1 of tag 9F34. If it is a deprecated value (1F - No CVM required, 1E or 5E - Signature), then the transaction is denied after the first CVM fails.

![Chip signature validation table](https://files.readme.io/d485341df63fba24d25317a2a7161a8deb5b6b51283bbafc44841f822e6ec267-image.png)

To determine the actual reason for the authorization decline, refer to [Verify authorization decline reasons](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#verify-authorization-decline-reasons) in this guide.

# GCD - GCD Gift card denial

This code is returned when a gift card transaction is denied.

It was necessary to create a new denial code to be used in an ELO response when the transaction kind is a gift card. In this case, the ELO network does not allow this kind of transaction, but this type of block can be done by the client. When GCD appears in the answer, the response code is `57`.

To determine the actual reason for the authorization decline, refer to [Verify authorization decline reasons](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#verify-authorization-decline-reasons) in this guide.

# HCE - HSM communication error

This occurs when there’s a communication error between our applications and the Hardware Security Module (HSM).

To determine the actual reason for the authorization decline, refer to [Verify authorization decline reasons](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#verify-authorization-decline-reasons) in this guide.

# IAT - Invalid account type

Compares the field Account Type content of the Processing Code (`DE3`) sent in the authorization message body with the given card type. If the authorization mode (credit or debit) isn’t allowed for this card, the transaction is denied. For example, a credit card transaction with Account Type 20 (debit) is denied.

To determine the actual reason for the authorization decline, refer to [Verify authorization decline reasons](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#verify-authorization-decline-reasons) in this guide.

# IMA - Invalid message authentication code (MAC)

If the message authentication code received from the network is invalid, the transaction cannot be processed and is denied.

Currently, this validation is only performed for the RuPay network.

To determine the actual reason for the authorization decline, refer to [Verify authorization decline reasons](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#verify-authorization-decline-reasons) in this guide.

# IMF - Invalid message format

If the message received from the network has an invalid format, domain, or value, the transaction cannot be processed and is denied with code IMF.

To determine the actual reason for the authorization decline, refer to [Verify authorization decline reasons](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#verify-authorization-decline-reasons) in this guide.

# ISE - Insufficient statements

If there are installments and interest to be calculated for the transaction, the Pismo platform has to fetch all the statements related to the installments, so it can use the due dates in its calculations. If the number of statements does not match the number of installments, the transaction is denied with code ISE. For example, if the transaction is for 36 installments, but there are only 30 statements created for the account, the transaction is denied.

To determine the actual reason for the authorization decline, refer to [Verify authorization decline reasons](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#verify-authorization-decline-reasons) in this guide.

# IZA - Zero amount not allowed

This ELO-specific denial code indicates that a purchase with a zero amount was not approved.

To determine the actual reason for the authorization decline, refer to [Verify authorization decline reasons](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#verify-authorization-decline-reasons) in this guide.

# LAE - An unexpected error happened while getting the account information

If the authorization system attempts to get a list of the available limits on an account from the Ledger API and a communication error occurs, this can result in an LAE error. For example, if there is a status code `500 - Internal Error` from the API, the Pismo platform sends an LAE error in response.

To determine the actual reason for the authorization decline, refer to [Verify authorization decline reasons](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#verify-authorization-decline-reasons) in this guide.

# LCT - Ledger account timeout

During transaction flow, the Ledger API is called to get a list of account limits. If the request times out, the transaction is denied.

To determine the actual reason for the authorization decline, refer to [Verify authorization decline reasons](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#verify-authorization-decline-reasons) in this guide.

# LNF - Account not found

If a communication error occurs when authorization tries to get a list of account limits from the Ledger API, this can result in an LNF error. For example, if the authorization system sends an invalid field or value in the request payload, it generates a `400 - Bad Request` error, and the Pismo platform sends an LNF error in response.

To determine the actual reason for the authorization decline, refer to [Verify authorization decline reasons](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#verify-authorization-decline-reasons) in this guide.

# LUD - Limit update duplicated ID error

This error occurs when there is a duplicate call. This would change the customer's balance twice for the same purchase, so the transaction is denied.

To determine the actual reason for the authorization decline, refer to [Verify authorization decline reasons](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#verify-authorization-decline-reasons) in this guide.

# LUE - Error on update Ledger

Any error that occurs in the Ledger API service that is not a timeout is denied with this code.

To determine the actual reason for the authorization decline, refer to [Verify authorization decline reasons](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#verify-authorization-decline-reasons) in this guide.

# LUT - Ledger timeout

If a timeout in the Ledger API service prevents the platform from completing a transaction, the Pismo platform denies the transaction.

To determine the actual reason for the authorization decline, refer to [Verify authorization decline reasons](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#verify-authorization-decline-reasons) in this guide.

# MDC - Multi-currency not allowed for DCC authorization

Due to a Mastercard mandate, it is necessary to block DCC (Dynamic Currency Conversion) transactions made with multi-currency cards. This implementation ensures compliance with the network rules and mitigates risks of penalties or disputes.

To determine the actual reason for the authorization decline, refer to [Verify authorization decline reasons](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#verify-authorization-decline-reasons) in this guide.

# MPC - Program config not found

This error occurs if the authorization platform doesn't have a valid program configuration. You need to contact a Pismo representative to fix the configuration.

To determine the actual reason for the authorization decline, refer to [Verify authorization decline reasons](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#verify-authorization-decline-reasons) in this guide.

# NCV - Entry mode not allowed with no CVM

By default, the Pismo platform does not allow authorizations without any cardholder validation method (CVM)–CVV, stripe, chip, password–and that is not marked as recurring and secure.

To determine the actual reason for the authorization decline, refer to [Verify authorization decline reasons](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#verify-authorization-decline-reasons) in this guide.

# OON - Org operation not found

This error occurs when the operation related to the `Transaction Type` subfield of the Processing Code (DE3) present in the body of the authorization message is not configured in the program of the card used.

To determine the actual reason for the authorization decline, refer to [Verify authorization decline reasons](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#verify-authorization-decline-reasons) in this guide.

# OOT - Orgs operation timeout

This denial occurs when the Orgs Operation API exceeds the time allowed to respond.

To determine the actual reason for the authorization decline, refer to [Verify authorization decline reasons](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#verify-authorization-decline-reasons) in this guide.

# OP1 - Message consistency or generic error

OP1 can appear for generic errors in stateless authorizations, such as when the Hardware Security Module (HSM) is unavailable, unexpected content in messages, invalid fields, or any unforeseen/platform-mapped error.

To determine the actual reason for the authorization decline, refer to [Verify authorization decline reasons](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#verify-authorization-decline-reasons) in this guide.

# PAE - Unexpected error while fetching parameters

During the transaction flow, the [Programs API](https://developers.pismo.io/pismo-docs/reference/programs-1) is called in order to retrieve parameters details. If an unexpected error happens while fetching those details in the [Programs API](https://developers.pismo.io/pismo-docs/reference/programs-1), the transaction is denied.

To determine the actual reason for the authorization decline, refer to [Verify authorization decline reasons](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#verify-authorization-decline-reasons) in this guide.

# PAT - A timeout occurred while fetching parameters

During the transaction flow, the [Programs API](https://developers.pismo.io/pismo-docs/reference/programs-1) is called in order to retrieve parameters details. If a timeout happens in [Programs API](https://developers.pismo.io/pismo-docs/reference/programs-1), the transaction is denied.

To determine the actual reason for the authorization decline, refer to [Verify authorization decline reasons](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#verify-authorization-decline-reasons) in this guide.

# PCE - Unexpected error in processing code definition

This could be the result of a timeout in the processing code API.

To determine the actual reason for the authorization decline, refer to [Verify authorization decline reasons](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#verify-authorization-decline-reasons) in this guide.

# PCT - A timeout occurred in processing code definition

This occurs when there is a communication error between the authorization flow and the processing code API. This can be a `400 - Bad Request`, a `500 - Internal Error`, or some other error. In the case of a `400 - Bad Request`, the authorization system could be sending an invalid field or value in the request payload. In all other cases, there is a processing error, which could indicate a bug in the flow.

To determine the actual reason for the authorization decline, refer to [Verify authorization decline reasons](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#verify-authorization-decline-reasons) in this guide.

# PFT - Denied by anti-fraud

This response indicates that an anti-fraud mechanism denied the transaction. In some cases, such as a **referral**, a different response might override this one. A referral is a specific designation of fraud used by some Brazilian clients. This kind of response is regarded as more serious than a simple “fraud” response.

To determine the actual reason for the authorization decline, refer to [Verify authorization decline reasons](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#verify-authorization-decline-reasons) in this guide.

# PGE - Program Config Generic Error

This occurs when the program configuration cannot be retrieved, either because of a communication failure with the API or an internal error.

To determine the actual reason for the authorization decline, refer to [Verify authorization decline reasons](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#verify-authorization-decline-reasons) in this guide.

# PIC - Program has invalid currency code

If the program has an invalid currency code, the transaction is denied with code PIC.

To determine the actual reason for the authorization decline, refer to [Verify authorization decline reasons](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#verify-authorization-decline-reasons) in this guide.

# PNP - PIN not present

Indicates that an authorization request was sent with no PIN in a card-present transaction. This custom code will not affect the PIN count.

To determine the actual reason for the authorization decline, refer to [Verify authorization decline reasons](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#verify-authorization-decline-reasons) in this guide.

# PRE - Unexpected error while fetching program

If an unexpected error occurs while attempting to retrieve the program details, the transaction is denied with code PRE.

To determine the actual reason for the authorization decline, refer to [Verify authorization decline reasons](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#verify-authorization-decline-reasons) in this guide.

# PRN - Program not found

If the program associated with a transaction is not found, the transaction is denied with code PRN.

To determine the actual reason for the authorization decline, refer to [Verify authorization decline reasons](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#verify-authorization-decline-reasons) in this guide.

# PRT - A timeout occurred while fetching program

If a timeout occurs while attempting to retrieve the program details, the transaction is denied with code PRT.

To determine the actual reason for the authorization decline, refer to [Verify authorization decline reasons](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#verify-authorization-decline-reasons) in this guide.

# RAD - Rates API denial

Occurs when a transaction is denied by some logical error in Rates API. This error is the result of a `422 - Unprocessable Entity`.

To determine the actual reason for the authorization decline, refer to [Verify authorization decline reasons](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#verify-authorization-decline-reasons) in this guide.

# RAE - Rates API error

This code indicates an error in the communication with the Rates API service during the authorization amount calculation. This error can be a result of a `400 - Bad Request` response, a `500 - Internal Error` response, or an error in the communication between the authorization system and the API-Rates service. In the Bad Request scenario, the authorization system could be sending an invalid field or value in the request payload. In other scenarios, there could be an error in the processing. If it is a single error, a retry might be enough to fix the problem. Multiple errors might indicate a bug in the flow.

To determine the actual reason for the authorization decline, refer to [Verify authorization decline reasons](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#verify-authorization-decline-reasons) in this guide.

# RAT - Rates API timeout

Returned when the Authorization service is unable to obtain a response from the Rates API within the configured timeout period, after all retry attempts have been exhausted. This code specifically identifies an infrastructure timeout condition and is distinct from Rates API business or processing errors, which continue to return existing codes such as `RAE` (Rates API Error) and `RAD` (Rates API denial).

To determine the actual reason for the authorization decline, refer to [Verify authorization decline reasons](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#verify-authorization-decline-reasons) in this guide.

# RED - Operation not allowed by rules / Rules do not honor / Rules internal error / Operation not permitted - credit voucher

This error occurs when flexible transaction control validation fails. It can be the result of a `400 - Bad Request`, a `500 - Internal Error`, or an error in communication between the authorization system and the API [flex controls](https://developers.pismo.io/pismo-docs/docs/flex-controls). However, in this case, the transaction is a credit voucher.

In the case of a `400 - Bad Request`, the authorization system could be sending an invalid field or value in the request payload.

In other cases, there is an error in the processing. If there is a single error, a retry could be enough to fix the problem. If there are multiple errors, there could be a bug in the flow.

The application of API rules can sometimes result in a transaction being denied and an error with code RED being generated.

To determine the actual reason for the authorization decline, refer to [Verify authorization decline reasons](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#verify-authorization-decline-reasons) in this guide.

# STD - Denied by second authorizer

This error occurs when the second authorizer denies the transaction.

To determine the actual reason for the authorization decline, refer to [Verify authorization decline reasons](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#verify-authorization-decline-reasons) in this guide.

# TGE - Card token generic error

When the authorization receives an error (timeout reached) while trying to retrieve the card token data, the network should will be notified that there is an internal error. In some cases, a message will be generated for this authorization.

To determine the actual reason for the authorization decline, refer to [Verify authorization decline reasons](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#verify-authorization-decline-reasons) in this guide.

# TNP - Token not provided

If Stand-in Processing (STIP) is enabled and a new provisioning attempt is made, it will not be provisioned, and Pismo will use the custom code `TNP` (token not provisioned) and denial code `05` for tokenization.

To determine the actual reason for the authorization decline, refer to [Verify authorization decline reasons](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#verify-authorization-decline-reasons) in this guide.

# TSM - Password tries exceeded

> 📘 Internationalization in progress
>
> Work is ongoing to internationalize parameter names. The guide uses the English phrase “Wrong password attempts” for param `TENTATIVAS SENHA ERRADA`

When the password is present in the body of the authorization message and the password attempt counter exceeds the `Wrong password attempts` program parameter, the transaction will be denied and the card will be blocked.

The program parameter `Wrong password attempts` specifies the maximum number of tries the user is allowed when entering their password. When the password is present in the authorization message body, and the number of tries exceeds the value in `Wrong password attempts`, the transaction is denied.

For example, if the program has the `Wrong password attempts` parameter set to 3, the Pismo platform will send the label `BLOCK_CARD` and the card will have the card status `BLOCKED` at the end of this transaction.

This denial code will only be issued when the password is present and correct after reaching the maximum number of attempts or it is a transaction without a password. Otherwise, the authorization will be denied by FR6 after checking the Hardware Security Module (HSM), as the FR6 code takes precedence over TSM.

<Callout icon="📘" theme="info">
  When the correct password is entered before the limit is exceeded, the counter is reset to **0**. However, when the limit is exceeded, the card is blocked.
</Callout>

For further information about the password tries reset endpoint, refer to [Get OpenID access token](https://developers.pismo.io/pismo-docs/reference/post-passport-v1-oauth2-token-1).

To determine the actual reason for the authorization decline, refer to [Verify authorization decline reasons](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#verify-authorization-decline-reasons) in this guide.

# UBN - NFC disabled

The purchase is denied with code UBN when it is of the contactless type (entry mode 07) and the function is disabled.

To determine the actual reason for the authorization decline, refer to [Verify authorization decline reasons](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#verify-authorization-decline-reasons) in this guide.

# VEV - Expired virtual card

Temporary cards are created with their expiration date set to their creation date plus one day. If a transaction occurs after the expiration date, the transaction is denied. This applies only to the `TEMPORARY` card type, which is the only one that has this value set.

To determine the actual reason for the authorization decline, refer to [Verify authorization decline reasons](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#verify-authorization-decline-reasons) in this guide.

# VNM - Expired card

For transactions which don’t have verification methods (CVV, password, chip), like recurring billings or purchases with a safe flag, this code indicates that the card is expired, based on the printed date on the card (which also is present in the database). This validation is made in two different scenarios:

* **Transactions which have verification methods (CVV, password, chip)** – In this case, the validation is made by the Hardware Security Module (HSM).
* **CED** – Invalid expiration date provided.

To determine the actual reason for the authorization decline, refer to [Verify authorization decline reasons](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#verify-authorization-decline-reasons) in this guide.

# Z30 - Token found, but does not match card

The token and card were found but they are not related to each other, in other words the PAN given by network is not related with the token.

To determine the actual reason for the authorization decline, refer to [Verify authorization decline reasons](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#verify-authorization-decline-reasons) in this guide.

# ZBA - Zero balance client webhook returns 401 status code, unauthorized.

If the zero balance client webhook returns status code 401 - Unauthorized, the transaction is denied with code ZBA.

To determine the actual reason for the authorization decline, refer to [Verify authorization decline reasons](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#verify-authorization-decline-reasons) in this guide.

# ZBD - Zero balance client declined

This is a customer-defined code to indicate that a denial was sent by the Zero balance client.

To determine the actual reason for the authorization decline, refer to [Verify authorization decline reasons](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#verify-authorization-decline-reasons) in this guide.

# ZBE - Zero balance client webhook returns general error

If the zero balance client webhook returns an error status code not covered by one of the other custom codes, the transaction is denied with code ZBE. Example: status code 400, 404, and others.

To determine the actual reason for the authorization decline, refer to [Verify authorization decline reasons](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#verify-authorization-decline-reasons) in this guide.

# ZBF - Zero balance client webhook returns 403 status code, forbidden.

If the zero balance client webhook returns status code 403 - Forbidden, the transaction is denied with code ZBF.

To determine the actual reason for the authorization decline, refer to [Verify authorization decline reasons](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#verify-authorization-decline-reasons) in this guide.

# ZBP - Partial authorization response invalid in Zero Balance Flow

In zero balance flow, it's possible to authorize transactions partially. A response code of "10" signifies that the transaction has been partially approved and the issuer must return the approved amounts. If these amounts are not returned or the amounts are negative, Pismo issues the custom code ZBP.

To determine the actual reason for the authorization decline, refer to [Verify authorization decline reasons](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#verify-authorization-decline-reasons) in this guide.

# ZBT - Zero balance client webhook throws timeout exception.

If the zero balance client webhook exceeds the allowed time (2 seconds), it throws a timeout exception, and the transaction is denied with code ZBT.

To determine the actual reason for the authorization decline, refer to [Verify authorization decline reasons](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#verify-authorization-decline-reasons) in this guide.

# ZBU - Unavailable endpoint, zero balance client webhook returns 503 status code.

If the zero balance client webhook returns status code `503 - Service Unavailable`, the transaction is denied with code ZBU.

To determine the actual reason for the authorization decline, refer to [Verify authorization decline reasons](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#verify-authorization-decline-reasons) in this guide.
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `POST /acquisitions/v3/s2s/applications` | `post-acquisitions-v3-s2s-applications` | Create account application | `api-specs/Core_platform_-_Accounts.yaml` | no | KU-API-core-platform-accounts--accounts |
| `POST /wallet/v2/cards/{cardId}/atc/reset` | `post-v2-card-atc-reset` | Reset card ATC | `api-specs/Card_issuing_-_Cards.yaml` | no | KU-API-card-issuing-cards--cards |

### Operation essentials

- **`POST /acquisitions/v3/s2s/applications`** (`post-acquisitions-v3-s2s-applications`): security `BearerAuth`; required parameters none declared; required body fields `application`; response statuses 201, 400, 409, 500; error codes in examples none; events `onboarding-prospect-1`, `onboarding-succeeded-1`.
- **`POST /wallet/v2/cards/{cardId}/atc/reset`** (`post-v2-card-atc-reset`): security `BearerAuth`; required parameters `cardId` (path); required body fields none declared; response statuses 200, 403, 500; error codes in examples none; events none listed.

### Operation links that do not resolve to a current specification

| Link slug | Link text(s) in source | Status |
| --- | --- | --- |
| `programs-1` | List programs; Programs API | not found in the current OpenAPI specifications and not matched to any removed-endpoint entry; status unverified (possible rename, typo or undocumented removal) |
| `post-passport-v1-oauth2-token-1` | Get OpenID access token; Passport API endpoint | not found in the current OpenAPI specifications and not matched to any removed-endpoint entry; status unverified (possible rename, typo or undocumented removal) |

## Events

Events emitted by the referenced operations (`api-reference-data/endpoint_event_map.csv`):

| Operation | Event slug |
| --- | --- |
| `post-acquisitions-v3-s2s-applications` | `onboarding-prospect-1` |
| `post-acquisitions-v3-s2s-applications` | `onboarding-succeeded-1` |

Event types linked from the source text (`api-reference-data/event_type_inventory.csv`):

| Event slug | Domain (inventory guess) | Version (inventory guess) | Event page | Emitting operations | Catalogue KU |
| --- | --- | --- | --- | --- | --- |
| `networktransactions-network-authorization-1` | networktransactions | 1 | https://developers.pismo.io/events/docs/networktransactions-network-authorization-1 | 2 | KU-EVT-catalogue-other-domains |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/card-issuing/validation-code-definitions.md`: updatedAt 2026-08-26T19:54:08.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- The source links to 2 event page(s) under `/events/`. Event payload definitions are not part of the corpus (robots.txt disallows `/events/`), so payload fields are not documented here.
- Operation link `programs-1` does not resolve: not found in the current OpenAPI specifications and not matched to any removed-endpoint entry; status unverified (possible rename, typo or undocumented removal)
- Operation link `post-passport-v1-oauth2-token-1` does not resolve: not found in the current OpenAPI specifications and not matched to any removed-endpoint entry; status unverified (possible rename, typo or undocumented removal)

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/card-issuing/validation-code-definitions.md` | whole document | https://developers.pismo.io/pismo-docs/docs/validation-code-definitions | `852d75488fb272a4…` | 2026-08-26T19:54:08.000Z |

## Related knowledge units

- `KU-API-card-issuing-cards--cards` — API reference: Card issuing - Cards — Cards
- `KU-API-core-platform-accounts--accounts` — API reference: Core platform - Accounts — Accounts
- `KU-CARD-digital-wallets` — Digital wallets, MDES Token Connect and Click to Pay
- `KU-CORE-flex-controls` — Flexible transaction controls: concepts, examples and simulation
- `KU-ERR-validation-codes-for-authorization-events-part-01` — Validation codes for authorization events (part 1 of 2)
- `KU-ERR-validation-codes-for-authorization-events-part-02` — Validation codes for authorization events (part 2 of 2)
- `KU-EVT-catalogue-other-domains` — Event catalogue: other event domains (accounting, authorization, availables, average, bulletin, cash, delinquent, fraud, instantpay, intl, ledger, networktransactions, onboarding, orgs, payment, platform, programs, rules, savings, statement)
